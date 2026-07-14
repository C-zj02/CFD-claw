"""Deterministic, non-mutating feasibility preflight for aircraft intent.

This module handles logical consistency, model applicability, clarification,
and bounded change proposals before an expensive Class I/II solve.  It never
claims physical infeasibility from a model gap and never applies a proposed
change to the versioned DesignIntent.
"""

from __future__ import annotations

import math
from typing import Any, Mapping

from src.design_execution.models import AircraftDesignRequirements
from src.design_intake.coverage import assess_model_coverage, canonical_coverage_key
from src.design_intake.models import (
    ChangeProposal,
    ClarificationQuestion,
    DesignIntent,
    DesignIntentStatus,
    FeasibilityDiagnosis,
    ModelCoverageStatus,
    RequirementField,
    RequirementRole,
    RequirementSource,
)


_MIN_PRELIMINARY_RESERVE = 0.05
_HIGH_PAYLOAD_FRACTION = 0.50
_TIGHT_FIELD_LENGTH_M = 100.0
_DEFAULT_SERVICE_CEILING_M = float(
    AircraftDesignRequirements.__dataclass_fields__["service_ceiling_m"].default
)


def _finite(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    parsed = float(value)
    return parsed if math.isfinite(parsed) else None


def _stable_unique(values: list[str]) -> tuple[str, ...]:
    return tuple(dict.fromkeys(values))


def _field_index(intent: DesignIntent) -> dict[str, RequirementField]:
    result: dict[str, RequirementField] = {}
    for field in intent.requirements:
        # Explicitly deferred requirements remain in coverage/provenance, but
        # they are outside the active solver baseline and must not shadow the
        # replacement field introduced during default completion.
        if field.path.startswith("deferred."):
            continue
        result.setdefault(canonical_coverage_key(field.path), field)
    return result


def _protected(field: RequirementField) -> bool:
    return field.locked or field.role is RequirementRole.HARD_CONSTRAINT


def _requires_confirmation(field: RequirementField) -> bool:
    # An unlocked derived/default design variable may be optimized without an
    # extra round trip.  User values, hard constraints, and assumptions remain
    # proposals until explicitly accepted.
    return (
        _protected(field)
        or field.source is RequirementSource.USER
        or field.role is RequirementRole.TECHNOLOGY_ASSUMPTION
    )


def _change_proposal(
    *,
    intent: DesignIntent,
    proposal_id: str,
    field: RequirementField,
    proposed_value: Any,
    reason: str,
    affected_constraints: tuple[str, ...],
    expected_benefit: str,
    engineering_cost: str,
) -> ChangeProposal:
    return ChangeProposal(
        proposal_id=proposal_id,
        field_path=field.path,
        old_value=field.value,
        proposed_value=proposed_value,
        reason=reason,
        affected_constraints=affected_constraints,
        expected_benefit=expected_benefit,
        engineering_cost=engineering_cost,
        target_locked=field.locked,
        requires_user_confirmation=_requires_confirmation(field),
        source_revision=intent.revision,
    )


def _missing_question(
    *,
    question_id: str,
    field_path: str,
    question: str,
    reason: str,
    options: tuple[Any, ...] = (),
    recommended_option: Any | None = None,
    consequence: str,
) -> ClarificationQuestion:
    return ClarificationQuestion(
        question_id=question_id,
        field_path=field_path,
        question=question,
        reason=reason,
        options=options,
        recommended_option=recommended_option,
        consequence_if_unanswered=consequence,
        blocking=True,
    )


def _append_ceiling_diagnosis(
    intent: DesignIntent,
    fields: Mapping[str, RequirementField],
    proposals: list[ChangeProposal],
    blocking_reasons: list[str],
    conflicting_fields: list[str],
) -> None:
    cruise = fields.get("cruise_altitude_m")
    ceiling = fields.get("service_ceiling_m")
    if cruise is None or ceiling is None:
        return
    cruise_value = _finite(cruise.value)
    ceiling_value = _finite(ceiling.value)
    if cruise_value is None or ceiling_value is None or ceiling_value >= cruise_value:
        return

    constraint_id = ("cross.service_ceiling_not_below_cruise",)
    if _protected(cruise) and _protected(ceiling):
        blocking_reasons.append(
            "The locked service ceiling is below the locked cruise altitude."
        )
        conflicting_fields.extend((cruise.path, ceiling.path))
    proposed_ceiling = max(cruise_value * (1.0 + _MIN_PRELIMINARY_RESERVE), cruise_value + 1.0)
    proposed_cruise = min(
        ceiling_value,
        ceiling_value / (1.0 + _MIN_PRELIMINARY_RESERVE),
    )
    proposals.extend(
        (
            _change_proposal(
                intent=intent,
                proposal_id="ceiling.raise_service_ceiling",
                field=ceiling,
                proposed_value=proposed_ceiling,
                reason="Restore the required ordering between cruise altitude and service ceiling.",
                affected_constraints=constraint_id,
                expected_benefit="Provides a preliminary five-percent altitude reserve above cruise.",
                engineering_cost="Requires more climb capability and may increase propulsion or wing area.",
            ),
            _change_proposal(
                intent=intent,
                proposal_id="ceiling.lower_cruise_altitude",
                field=cruise,
                proposed_value=proposed_cruise,
                reason="Move cruise below the declared service ceiling.",
                affected_constraints=constraint_id,
                expected_benefit="Removes the direct altitude contradiction without increasing ceiling demand.",
                engineering_cost="Changes atmospheric, drag, range, and observability assumptions.",
            ),
        )
    )


def _append_mach_diagnosis(
    intent: DesignIntent,
    fields: Mapping[str, RequirementField],
    proposals: list[ChangeProposal],
    blocking_reasons: list[str],
    conflicting_fields: list[str],
) -> None:
    cruise = fields.get("cruise_mach")
    maximum = fields.get("max_flight_mach")
    if cruise is None or maximum is None:
        return
    cruise_value = _finite(cruise.value)
    maximum_value = _finite(maximum.value)
    if cruise_value is None or maximum_value is None or maximum_value >= cruise_value:
        return

    constraint_id = ("cross.maximum_mach_not_below_cruise",)
    if _protected(cruise) and _protected(maximum):
        blocking_reasons.append("The locked maximum Mach number is below locked cruise Mach.")
        conflicting_fields.extend((cruise.path, maximum.path))
    proposed_maximum = max(
        cruise_value * (1.0 + _MIN_PRELIMINARY_RESERVE),
        cruise_value + 0.01,
    )
    proposed_cruise = min(
        maximum_value,
        maximum_value / (1.0 + _MIN_PRELIMINARY_RESERVE),
    )
    proposals.extend(
        (
            _change_proposal(
                intent=intent,
                proposal_id="mach.raise_maximum_mach",
                field=maximum,
                proposed_value=proposed_maximum,
                reason="Restore the required ordering between cruise and maximum Mach.",
                affected_constraints=constraint_id,
                expected_benefit="Provides preliminary speed margin above cruise.",
                engineering_cost="May require a different propulsion system and transonic aeroelastic validation.",
            ),
            _change_proposal(
                intent=intent,
                proposal_id="mach.lower_cruise_mach",
                field=cruise,
                proposed_value=proposed_cruise,
                reason="Move cruise below the declared maximum speed.",
                affected_constraints=constraint_id,
                expected_benefit="Removes the direct speed contradiction.",
                engineering_cost="Increases mission time and can change range and fuel sizing.",
            ),
        )
    )


def _append_payload_mtow_diagnosis(
    intent: DesignIntent,
    fields: Mapping[str, RequirementField],
    proposals: list[ChangeProposal],
    blocking_reasons: list[str],
    conflicting_fields: list[str],
) -> None:
    payload = fields.get("payload_kg")
    mtow = fields.get("max_mtow_kg") or fields.get("mtow_kg")
    if payload is None or mtow is None:
        return
    payload_value = _finite(payload.value)
    mtow_value = _finite(mtow.value)
    if payload_value is None or mtow_value is None or mtow_value <= 0.0:
        return
    ratio = payload_value / mtow_value
    if ratio <= _HIGH_PAYLOAD_FRACTION:
        return

    is_cap = canonical_coverage_key(mtow.path) == "max_mtow_kg"
    constraint_id = ("cross.payload_mass_fraction",)
    if ratio >= 1.0 and is_cap and _protected(payload) and _protected(mtow):
        blocking_reasons.append(
            "The locked payload equals or exceeds the locked maximum takeoff mass."
        )
        conflicting_fields.extend((payload.path, mtow.path))
    target_mtow = max(mtow_value + 1.0, payload_value / _HIGH_PAYLOAD_FRACTION)
    target_payload = max(0.0, mtow_value * _HIGH_PAYLOAD_FRACTION)
    proposals.extend(
        (
            _change_proposal(
                intent=intent,
                proposal_id="mass.increase_mtow_allowance",
                field=mtow,
                proposed_value=target_mtow,
                reason="The declared payload fraction leaves high mass-closure risk.",
                affected_constraints=constraint_id,
                expected_benefit="Restores preliminary allowance for structure, propulsion, systems, and fuel.",
                engineering_cost="Increases vehicle size, launch demand, cost, and possibly signature.",
            ),
            _change_proposal(
                intent=intent,
                proposal_id="mass.reduce_payload",
                field=payload,
                proposed_value=target_payload,
                reason="The declared payload fraction leaves high mass-closure risk.",
                affected_constraints=constraint_id,
                expected_benefit="Reduces the dominant mass-closure pressure while preserving the MTOW target.",
                engineering_cost="Reduces mission payload capability.",
            ),
        )
    )


def _append_aspect_ratio_diagnosis(
    intent: DesignIntent,
    fields: Mapping[str, RequirementField],
    proposals: list[ChangeProposal],
    blocking_reasons: list[str],
    conflicting_fields: list[str],
) -> None:
    aspect_ratio = fields.get("aspect_ratio")
    maximum = fields.get("max_aspect_ratio")
    if aspect_ratio is None or maximum is None:
        return
    actual = _finite(aspect_ratio.value)
    limit = _finite(maximum.value)
    if actual is None or limit is None or actual <= limit:
        return
    constraint_id = ("cross.aspect_ratio_upper_bound",)
    if _protected(aspect_ratio) and _protected(maximum):
        blocking_reasons.append("The locked aspect ratio exceeds the locked upper bound.")
        conflicting_fields.extend((aspect_ratio.path, maximum.path))
    proposals.extend(
        (
            _change_proposal(
                intent=intent,
                proposal_id="geometry.reduce_aspect_ratio",
                field=aspect_ratio,
                proposed_value=limit,
                reason="Bring the selected geometry inside the declared aspect-ratio bound.",
                affected_constraints=constraint_id,
                expected_benefit="Makes the geometry input consistent with the upper bound.",
                engineering_cost="Usually increases induced drag or wing area demand.",
            ),
            _change_proposal(
                intent=intent,
                proposal_id="geometry.relax_aspect_ratio_limit",
                field=maximum,
                proposed_value=actual,
                reason="Raise the upper bound to include the selected geometry.",
                affected_constraints=constraint_id,
                expected_benefit="Preserves the current aerodynamic geometry input.",
                engineering_cost="Increases span and may conflict with packaging or launch constraints.",
            ),
        )
    )


def _append_mission_risk_diagnosis(
    intent: DesignIntent,
    fields: Mapping[str, RequirementField],
    proposals: list[ChangeProposal],
) -> None:
    range_field = fields.get("range_m")
    reserve = fields.get("reserve_fraction")
    if range_field is None or reserve is None:
        return
    range_value = _finite(range_field.value)
    reserve_value = _finite(reserve.value)
    if (
        range_value is None
        or reserve_value is None
        or range_value <= 1_000_000.0
        or reserve_value >= _MIN_PRELIMINARY_RESERVE
    ):
        return
    proposals.append(
        _change_proposal(
            intent=intent,
            proposal_id="mission.restore_preliminary_reserve",
            field=reserve,
            proposed_value=_MIN_PRELIMINARY_RESERVE,
            reason="Long-range missions should preserve the default preliminary performance reserve.",
            affected_constraints=("mission.minimum_reserve",),
            expected_benefit="Reduces sensitivity to atmosphere, routing, and model uncertainty.",
            engineering_cost="Increases required fuel or reduces payload-range capability.",
        )
    )


def _append_core_questions(
    intent: DesignIntent,
    fields: Mapping[str, RequirementField],
    questions: list[ClarificationQuestion],
) -> None:
    range_field = fields.get("range_m")
    if range_field is None or (_finite(range_field.value) or 0.0) <= 0.0:
        questions.append(
            _missing_question(
                question_id="mission.range.required",
                field_path=range_field.path if range_field is not None else "mission.range_m",
                question="What design mission range should the sizing solver close?",
                reason="The current solver requires a positive mission range; endurance is not silently converted to range.",
                consequence="The deterministic sizing run cannot start without a normalized range.",
            )
        )
    payload = fields.get("payload_kg")
    payload_value = _finite(payload.value) if payload is not None else None
    if payload is None or payload_value is None or payload_value < 0.0:
        questions.append(
            _missing_question(
                question_id="mission.payload.required",
                field_path=payload.path if payload is not None else "mission.payload_kg",
                question="What mission payload mass should the design carry?",
                reason="Payload is required for mass closure and must be a non-negative mass.",
                consequence="The deterministic sizing run cannot start without a normalized payload.",
            )
        )

    cruise_mach = fields.get("cruise_mach")
    cruise_value = _finite(cruise_mach.value) if cruise_mach is not None else None
    if cruise_value is not None and cruise_value >= 0.5:
        propulsion = fields.get("propulsion_type")
        if propulsion is None and intent.propulsion is None:
            questions.append(
                _missing_question(
                    question_id="propulsion.type.high_speed",
                    field_path="propulsion.propulsion_type",
                    question="Which propulsion branch should be used for the high-speed cruise requirement?",
                    reason="Propulsion type materially changes fuel, thrust-lapse, and installation assumptions at this Mach number.",
                    options=("jet", "prop"),
                    recommended_option="jet",
                    consequence="A task-class default would be too influential to apply silently.",
                )
            )

    cruise_altitude = fields.get("cruise_altitude_m")
    cruise_altitude_value = (
        _finite(cruise_altitude.value) if cruise_altitude is not None else None
    )
    if (
        cruise_altitude_value is not None
        and cruise_altitude_value > _DEFAULT_SERVICE_CEILING_M
        and fields.get("service_ceiling_m") is None
    ):
        minimum_ceiling = max(
            cruise_altitude_value * (1.0 + _MIN_PRELIMINARY_RESERVE),
            cruise_altitude_value + 1.0,
        )
        questions.append(
            _missing_question(
                question_id="performance.service_ceiling.high_cruise",
                field_path="requirements.service_ceiling_m",
                question=(
                    "What service ceiling should be used for this high-altitude cruise "
                    f"requirement? Use at least {minimum_ceiling:.1f} m for the preliminary "
                    "five-percent altitude reserve."
                ),
                reason=(
                    "The solver default service ceiling is below the declared cruise altitude "
                    "and cannot be applied silently."
                ),
                consequence=(
                    "Default completion would fail because service ceiling cannot be below "
                    "cruise altitude."
                ),
            )
        )

    for distance_key, cl_key, phase in (
        ("takeoff_distance_m", "cl_max_takeoff", "takeoff"),
        ("landing_distance_m", "cl_max_landing", "landing"),
    ):
        distance = fields.get(distance_key)
        distance_value = _finite(distance.value) if distance is not None else None
        if distance_value is None or distance_value >= _TIGHT_FIELD_LENGTH_M or cl_key in fields:
            continue
        options = (
            "provide_project_specific_high_lift_data",
            "accept_preliminary_clmax_assumption",
            "relax_field_length_requirement",
        )
        questions.append(
            _missing_question(
                question_id=f"field_length.{phase}.assumption",
                field_path=f"requirements.{cl_key}",
                question=f"How should the {phase} high-lift assumption be established?",
                reason=f"A {phase} distance below 100 m is highly sensitive to CLmax, obstacle, and field-condition assumptions.",
                options=options,
                recommended_option=options[0],
                consequence="The field-length requirement cannot be treated as a robust preliminary constraint.",
            )
        )


def _assumption_descriptions(intent: DesignIntent) -> tuple[str, ...]:
    descriptions = []
    for field in intent.requirements:
        if field.source in {RequirementSource.DEFAULT, RequirementSource.DERIVED}:
            descriptions.append(
                f"{field.path} uses a {field.source.value} value and remains subject to confirmation."
            )
    return _stable_unique(descriptions)


def diagnose_design_intent(
    intent: DesignIntent | Mapping[str, Any],
) -> FeasibilityDiagnosis:
    """Return one fail-closed preflight diagnosis without mutating input state."""

    normalized = intent if isinstance(intent, DesignIntent) else DesignIntent.from_dict(intent)
    fields = _field_index(normalized)
    coverage = assess_model_coverage(normalized)
    questions: list[ClarificationQuestion] = []
    proposals: list[ChangeProposal] = []
    blocking_reasons: list[str] = []
    conflicting_fields: list[str] = []

    _append_core_questions(normalized, fields, questions)
    _append_ceiling_diagnosis(
        normalized, fields, proposals, blocking_reasons, conflicting_fields
    )
    _append_mach_diagnosis(
        normalized, fields, proposals, blocking_reasons, conflicting_fields
    )
    _append_payload_mtow_diagnosis(
        normalized, fields, proposals, blocking_reasons, conflicting_fields
    )
    _append_aspect_ratio_diagnosis(
        normalized, fields, proposals, blocking_reasons, conflicting_fields
    )
    _append_mission_risk_diagnosis(normalized, fields, proposals)

    # Keep one user turn bounded to the three highest-impact questions.
    questions = questions[:3]
    blocking_unsupported = [
        item
        for item in coverage
        if item.status is ModelCoverageStatus.UNSUPPORTED and item.blocking
    ]
    if conflicting_fields:
        status = DesignIntentStatus.CONTRADICTORY_REQUIREMENTS
        summary = (
            "The request contains explicit cross-field contradictions. "
            "No requirement has been changed; select and confirm a proposed revision."
        )
    elif blocking_unsupported:
        status = DesignIntentStatus.UNSUPPORTED
        blocking_reasons.extend(
            f"No applicable model for {item.field_path}: {item.reason}"
            for item in blocking_unsupported
        )
        summary = (
            "One or more mandatory requirements are outside the registered model coverage. "
            "This is an unsupported-model result, not a physical infeasibility finding."
        )
    elif questions:
        status = DesignIntentStatus.NEEDS_CLARIFICATION
        blocking_reasons.append(
            "One or more high-impact inputs must be clarified before deterministic sizing."
        )
        summary = "The request needs a bounded clarification before it can enter the solver."
    elif proposals:
        status = DesignIntentStatus.REPAIRABLE
        blocking_reasons.append(
            "The current revision has a deterministic repair proposal that has not been applied."
        )
        summary = (
            "The request is repairable through explicit requirement or design-variable changes. "
            "Locked and user-provided values remain unchanged until confirmation."
        )
    else:
        status = DesignIntentStatus.READY_FOR_SOLVER
        summary = (
            "Required inputs are present, cross-field checks pass, and no blocking model gap "
            "was found. The revision is eligible for explicit confirmation; solver execution "
            "is not yet authorized and engineering feasibility is not proven."
        )

    return FeasibilityDiagnosis(
        status=status,
        summary=summary,
        coverage=coverage,
        clarification_questions=tuple(questions),
        change_proposals=tuple(proposals),
        blocking_reasons=_stable_unique(blocking_reasons),
        conflicting_fields=_stable_unique(conflicting_fields),
        assumptions=_assumption_descriptions(normalized),
        ready_for_solver=status is DesignIntentStatus.READY_FOR_SOLVER,
    )


def preflight_design_intent(
    intent: DesignIntent | Mapping[str, Any],
) -> FeasibilityDiagnosis:
    """Readable alias for API and orchestration callers."""

    return diagnose_design_intent(intent)


__all__ = ["diagnose_design_intent", "preflight_design_intent"]
