"""Deterministic solver-outcome feedback for versioned design intent.

The solver may change bounded design variables internally, but it must never
relax a user requirement.  This module converts trustworthy failed-constraint
evidence into a new, unconfirmed negotiation revision.  It only proposes
changes for explicitly registered fields and never treats an execution error
or a model-coverage gap as proof of physical infeasibility.
"""

from __future__ import annotations

import math
import re
from dataclasses import replace
from typing import Any, Mapping

from .coverage import canonical_coverage_key
from .models import (
    ChangeProposal,
    ClarificationQuestion,
    DesignIntent,
    DesignIntentStatus,
    FeasibilityDiagnosis,
    RequirementField,
)


_ACTIONABLE_STATUSES = {"engineering_infeasible", "nonconverged"}

# Constraint evidence may justify offering a requirement relaxation, but never
# applying one.  The value is the canonical DesignIntent field key.
_REQUIREMENT_RELAXATION_FIELDS: dict[str, str] = {
    "class1.range": "range_m",
    "class1.takeoff_distance": "takeoff_distance_m",
    "class1.landing_distance": "landing_distance_m",
    "declared.max_mtow_kg": "max_mtow_kg",
    "declared.max_aspect_ratio": "max_aspect_ratio",
}

_RELAXATION_BOUNDS: dict[str, tuple[float, float]] = {
    "range_m": (1_000.0, 30_000_000.0),
    "takeoff_distance_m": (20.0, 10_000.0),
    "landing_distance_m": (20.0, 10_000.0),
    "max_mtow_kg": (1.0, 2_000_000.0),
    "max_aspect_ratio": (1.0, 40.0),
}

# When no evidence-backed requirement value exists, ask for one relevant design
# variable instead of inventing a numerical repair.  The solver will still run
# the complete Class I/II validation after the user supplies a value.
_DIAGNOSTIC_QUESTION_FIELDS: tuple[tuple[tuple[str, ...], str], ...] = (
    (("class1.weight_closure",), "mtow_kg"),
    (
        (
            "class1.sustained_turn_thrust",
            "class1.service_ceiling_thrust",
            "advanced.propulsion.cruise_thrust_margin",
            "advanced.propulsion.climb_thrust_margin",
        ),
        "thrust_to_weight",
    ),
    (("class1.fuel_fraction", "advanced.mission.fuel_capacity"), "aspect_ratio"),
    (("advanced.stability.static_margin_min",), "cg_fraction_cbar"),
    (("advanced.structures.weight_feedback",), "thickness_ratio"),
    (("advanced.geometry.fuel_volume",), "thickness_ratio"),
)


def _finite(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    parsed = float(value)
    return parsed if math.isfinite(parsed) else None


def _field_index(intent: DesignIntent) -> dict[str, RequirementField]:
    return {
        canonical_coverage_key(field.path): field
        for field in intent.requirements
        if not field.path.startswith("deferred.")
    }


def _constraint_id(value: Any) -> str | None:
    if not isinstance(value, str) or not value.strip():
        return None
    normalized = re.sub(r"[^A-Za-z0-9_.-]+", "_", value.strip()).strip("._-")
    return normalized[:200] or None


def _failed_constraints(result: Mapping[str, Any]) -> list[dict[str, Any]]:
    engineering = result.get("engineering")
    if not isinstance(engineering, Mapping):
        return []
    raw_constraints = engineering.get("constraints")
    if not isinstance(raw_constraints, (list, tuple)):
        return []
    failed: list[dict[str, Any]] = []
    for raw in raw_constraints:
        if (
            not isinstance(raw, Mapping)
            or raw.get("blocking") is not True
            or raw.get("passed") is not False
        ):
            continue
        constraint_id = _constraint_id(raw.get("id"))
        if constraint_id is None:
            continue
        failed.append(
            {
                "id": constraint_id,
                "label": str(raw.get("label") or constraint_id),
                "direction": raw.get("direction"),
                "required": _finite(raw.get("required")),
                "actual": _finite(raw.get("actual")),
                "margin": _finite(raw.get("margin")),
                "margin_ratio": _finite(raw.get("margin_ratio")),
                "unit": str(raw.get("unit") or ""),
                "recommendation": (
                    str(raw["recommendation"])
                    if raw.get("recommendation") not in (None, "")
                    else None
                ),
            }
        )
    return failed


def _relaxed_value(
    constraint: Mapping[str, Any],
    *,
    canonical_field: str,
) -> float | None:
    required = _finite(constraint.get("required"))
    actual = _finite(constraint.get("actual"))
    if required is None or actual is None:
        return None
    direction = constraint.get("direction")
    if direction == "minimum" and actual < required:
        candidate = actual
    elif direction == "maximum" and actual > required:
        candidate = actual
    else:
        return None
    lower, upper = _RELAXATION_BOUNDS[canonical_field]
    if candidate < lower or candidate > upper:
        return None
    return candidate


def _format_evidence(constraint: Mapping[str, Any]) -> str:
    required = constraint.get("required")
    actual = constraint.get("actual")
    margin = constraint.get("margin")
    unit = str(constraint.get("unit") or "").strip()
    suffix = f" {unit}" if unit else ""
    return (
        f"required={required}{suffix}, actual={actual}{suffix}, "
        f"margin={margin}{suffix}"
    )


def _requirement_proposals(
    intent: DesignIntent,
    failed: list[dict[str, Any]],
    *,
    job_id: str,
) -> list[ChangeProposal]:
    fields = _field_index(intent)
    proposals: list[ChangeProposal] = []
    job_key = re.sub(r"[^A-Za-z0-9_-]+", "-", job_id).strip("-")[:48] or "job"
    for constraint in failed:
        constraint_id = str(constraint["id"])
        canonical_field = _REQUIREMENT_RELAXATION_FIELDS.get(constraint_id)
        if canonical_field is None:
            continue
        field = fields.get(canonical_field)
        if field is None:
            continue
        proposed = _relaxed_value(constraint, canonical_field=canonical_field)
        current = _finite(field.value)
        if proposed is None or current is None or math.isclose(proposed, current):
            continue
        proposals.append(
            ChangeProposal(
                proposal_id=f"solver.{job_key}.{constraint_id}"[:160],
                field_path=field.path,
                old_value=field.value,
                proposed_value=proposed,
                reason=(
                    "The last deterministic run failed this blocking constraint: "
                    f"{_format_evidence(constraint)}. The proposed value matches the "
                    "last modeled capability and is not applied automatically."
                ),
                affected_constraints=(constraint_id,),
                expected_benefit=(
                    "Removes this measured shortfall from the next baseline; the complete "
                    "workflow must be rerun and may expose other failures."
                ),
                engineering_cost=(
                    "Relaxes a user requirement. Accept only if the resulting mission remains useful."
                ),
                target_locked=field.locked,
                requires_user_confirmation=True,
                # The proposal is displayed on the child outcome revision, not
                # on the confirmed parent revision that was submitted.
                source_revision=intent.revision + 1,
            )
        )
        if len(proposals) == 3:
            break
    return proposals


def _diagnostic_questions(
    intent: DesignIntent,
    failed: list[dict[str, Any]],
) -> list[ClarificationQuestion]:
    fields = _field_index(intent)
    failed_by_id = {str(item["id"]): item for item in failed}
    questions: list[ClarificationQuestion] = []
    used_paths: set[str] = set()
    for constraint_ids, canonical_field in _DIAGNOSTIC_QUESTION_FIELDS:
        matched = [failed_by_id[item] for item in constraint_ids if item in failed_by_id]
        field = fields.get(canonical_field)
        if not matched or field is None or field.path in used_paths:
            continue
        evidence = "; ".join(
            f"{item['id']} ({_format_evidence(item)})" for item in matched
        )
        questions.append(
            ClarificationQuestion(
                question_id=f"solver_outcome.{canonical_field}.new_value",
                field_path=field.path,
                question=(
                    f"What revised value should be evaluated for {field.path}? "
                    f"The current value is {field.to_dict()['value']}."
                ),
                reason=(
                    "The solver identified a relevant design variable but did not provide "
                    f"a validated next value. Failed evidence: {evidence}."
                ),
                consequence_if_unanswered=(
                    "The current failure remains unresolved and no new solver run is authorized."
                ),
                blocking=True,
            )
        )
        used_paths.add(field.path)
        if len(questions) == 3:
            break
    return questions


def _nonconvergence_question(intent: DesignIntent) -> ClarificationQuestion:
    fields = _field_index(intent)
    mtow = fields.get("mtow_kg")
    current = mtow.to_dict()["value"] if mtow is not None else None
    current_text = f" The current value is {current}." if current is not None else ""
    return ClarificationQuestion(
        question_id="solver_outcome.nonconverged.mtow_kg.new_value",
        field_path="initial_guess.mtow_kg",
        question=(
            "What initial MTOW should be evaluated for the next sizing retry?"
            + current_text
        ),
        reason=(
            "The numerical loop did not converge and did not establish a trustworthy "
            "aircraft capability. Supply an explicit initial value rather than relaxing a "
            "mission requirement from an unconverged iterate."
        ),
        consequence_if_unanswered=(
            "The unconverged result remains diagnostic only and no new solver run is authorized."
        ),
        blocking=True,
    )


def build_solver_outcome_revision(
    intent: DesignIntent,
    prior_diagnosis: FeasibilityDiagnosis,
    *,
    job_id: str,
    result: Mapping[str, Any],
    result_hash: str,
) -> tuple[DesignIntent, FeasibilityDiagnosis] | None:
    """Build one unconfirmed child revision for an actionable failed solve.

    Returns ``None`` for successful runs and for execution failures that carry no
    engineering evidence.  Callers must separately retain those job results.
    """

    status = result.get("status")
    if status not in _ACTIONABLE_STATUSES:
        return None
    engineering = result.get("engineering")
    engineering = engineering if isinstance(engineering, Mapping) else {}
    failed = _failed_constraints(result)
    numerically_converged = engineering.get("numerical_converged") is True
    engineering_feasible = engineering.get("engineering_feasible")
    blocking_failed_count = engineering.get("blocking_failed_count")

    if status == "engineering_infeasible" and not (
        numerically_converged
        and engineering_feasible is False
        and isinstance(blocking_failed_count, int)
        and not isinstance(blocking_failed_count, bool)
        and blocking_failed_count > 0
        and failed
    ):
        # An incomplete or internally inconsistent result contract is not evidence
        # that a requirement should change. Keep the job diagnostics, but do not
        # create a negotiation revision from it.
        return None

    if status == "engineering_infeasible":
        proposals = _requirement_proposals(intent, failed, job_id=job_id)
        questions = [] if proposals else _diagnostic_questions(intent, failed)
    else:
        # Values from an unconverged iterate are not a validated capability and
        # therefore cannot justify relaxing a hard mission requirement.
        proposals = []
        questions = _diagnostic_questions(intent, failed)
        if not questions:
            questions = [_nonconvergence_question(intent)]

    metadata = intent.to_dict()["metadata"]
    outcomes = list(metadata.get("solver_outcomes") or [])
    outcomes.append(
        {
            "job_id": job_id,
            "result_hash": result_hash,
            "status": status,
            "numerical_converged": engineering.get("numerical_converged"),
            "engineering_feasible": engineering.get("engineering_feasible"),
            "blocking_failed_count": engineering.get("blocking_failed_count"),
            "failed_constraints": failed,
        }
    )
    metadata["solver_outcomes"] = outcomes

    if status == "nonconverged":
        next_status = DesignIntentStatus.NEEDS_CLARIFICATION
        summary = (
            "The deterministic run did not converge. Its last iterate is diagnostic only, "
            "so no mission requirement relaxation was generated."
        )
    elif proposals:
        next_status = DesignIntentStatus.REPAIRABLE
        summary = (
            "The deterministic run failed one or more blocking constraints. "
            "Evidence-backed requirement changes are available but remain unapplied."
        )
    elif questions:
        next_status = DesignIntentStatus.NEEDS_CLARIFICATION
        summary = (
            "The deterministic run failed and did not establish a safe automatic value. "
            "A bounded design-variable clarification is required before another run."
        )
    else:
        next_status = DesignIntentStatus.INFEASIBLE
        summary = (
            "The deterministic run failed within the current model scope, and no registered "
            "evidence-backed parameter change can be proposed."
        )

    child = replace(
        intent,
        revision=intent.revision + 1,
        status=next_status,
        metadata=metadata,
    )
    reasons = [
        f"{item['id']}: {_format_evidence(item)}"
        for item in failed
    ]
    if not reasons:
        reasons = [
            f"Solver status is {status}; no complete failed-constraint evidence was returned."
        ]
    diagnosis = FeasibilityDiagnosis(
        status=next_status,
        summary=summary,
        coverage=prior_diagnosis.coverage,
        clarification_questions=tuple(questions),
        change_proposals=tuple(proposals),
        blocking_reasons=tuple(reasons[:12]),
        assumptions=prior_diagnosis.assumptions,
        ready_for_solver=False,
    )
    return child, diagnosis


__all__ = ["build_solver_outcome_revision"]
