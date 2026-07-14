"""Contract tests for structured aircraft-design requirement intake."""

from __future__ import annotations

import json
from dataclasses import FrozenInstanceError

import pytest

from src.design_intake import (
    ChangeProposal,
    ClarificationQuestion,
    DesignIntent,
    DesignIntentStatus,
    FeasibilityDiagnosis,
    ModelCoverageRecord,
    ModelCoverageStatus,
    RequirementField,
    RequirementRole,
    RequirementSource,
)


def _locked_mtow() -> RequirementField:
    return RequirementField(
        path="performance.max_takeoff_weight_kg",
        value=260.0,
        unit="kg",
        role=RequirementRole.HARD_CONSTRAINT,
        locked=True,
        source=RequirementSource.USER,
        tolerance=0.5,
    )


def _intent() -> DesignIntent:
    return DesignIntent(
        intent_id="stealth-uav-001",
        requirements=(
            _locked_mtow(),
            RequirementField(
                path="geometry.aspect_ratio",
                value={"maximum": 2.5},
                role="hard_constraint",
                source="user",
                locked=False,
            ),
        ),
        original_request="Design a fixed-wing UAV.",
        mission={"segments": ["boost", "cruise", "recovery"]},
        aircraft_class="fixed-wing UAV",
        launch="rocket assisted",
        recovery="parachute",
        metadata={"parser": {"version": 1}},
    )


def _locked_change() -> ChangeProposal:
    return ChangeProposal(
        proposal_id="change-mtow-001",
        field_path="performance.max_takeoff_weight_kg",
        old_value=260.0,
        proposed_value=285.0,
        reason="The current mass budget has no non-negative fuel allocation.",
        affected_constraints=("performance.endurance_h", "mass.fuel_fraction"),
        expected_benefit="Restores a positive fuel and structure margin.",
        engineering_cost="Higher launch-system load and acquisition cost.",
        target_locked=True,
        requires_user_confirmation=True,
        source_revision=1,
    )


def test_enums_are_stable_string_contracts() -> None:
    assert RequirementRole.HARD_CONSTRAINT == "hard_constraint"
    assert RequirementSource.REFERENCE.value == "reference"
    assert DesignIntentStatus.READY_FOR_SOLVER.value == "ready_for_solver"
    assert ModelCoverageStatus.UNSUPPORTED.value == "unsupported"


def test_requirement_field_round_trips_as_json_and_freezes_nested_values() -> None:
    field = RequirementField.from_dict(
        {
            "path": "mission.cruise_altitude_m",
            "value": {"minimum": 9_500.0, "conditions": ["ISA"]},
            "role": "hard_constraint",
            "unit": "m",
            "locked": True,
            "source": "reference",
            "source_reference": "Mission requirement document, revision A",
            "confidence": 0.95,
        }
    )

    with pytest.raises(TypeError):
        field.value["minimum"] = 8_000.0
    with pytest.raises(FrozenInstanceError):
        field.locked = False

    payload = field.to_dict()
    assert json.loads(json.dumps(payload)) == payload
    assert RequirementField.from_dict(payload) == field


@pytest.mark.parametrize(
    "payload,error",
    [
        ({"path": "mission.range_m", "value": 1_000.0}, "role"),
        (
            {
                "path": "mission.range_m",
                "value": 1_000.0,
                "role": "hard_constraint",
                "unexpected": True,
            },
            "unsupported requirement fields",
        ),
        (
            {"path": "mission range", "value": 1_000.0, "role": "hard_constraint"},
            "dotted ASCII identifiers",
        ),
        (
            {
                "path": "mission.range_m",
                "value": float("nan"),
                "role": "hard_constraint",
            },
            "finite",
        ),
        (
            {
                "path": "mission.range_m",
                "value": 1_000.0,
                "role": "reference_value",
            },
            "must be one of",
        ),
        (
            {
                "path": "mission.range_m",
                "value": 1_000.0,
                "role": "hard_constraint",
                "source": "reference",
            },
            "source_reference",
        ),
    ],
)
def test_requirement_field_rejects_invalid_contract(payload: dict, error: str) -> None:
    with pytest.raises(ValueError, match=error):
        RequirementField.from_dict(payload)


def test_design_intent_round_trips_and_reports_locked_fields() -> None:
    intent = _intent()

    assert intent.locked_field_paths == ("performance.max_takeoff_weight_kg",)
    assert intent.requirement("geometry.aspect_ratio").value["maximum"] == 2.5
    with pytest.raises(KeyError, match="unknown requirement field"):
        intent.requirement("mission.unknown")
    with pytest.raises(TypeError):
        intent.metadata["parser"] = {"version": 2}

    payload = intent.to_dict()
    assert json.loads(json.dumps(payload)) == payload
    assert DesignIntent.from_dict(payload) == intent


def test_design_intent_rejects_duplicate_paths_and_unknown_fields() -> None:
    requirement = _locked_mtow().to_dict()
    with pytest.raises(ValueError, match="duplicate paths"):
        DesignIntent.from_dict(
            {
                "intent_id": "duplicate",
                "requirements": [requirement, requirement],
            }
        )
    with pytest.raises(ValueError, match="unsupported design intent fields"):
        DesignIntent.from_dict({"intent_id": "unknown", "silent_override": True})


def test_locked_requirement_cannot_be_changed_without_explicit_confirmation() -> None:
    field = _locked_mtow()
    with pytest.raises(PermissionError, match="requires user confirmation"):
        field.with_value(285.0)
    with pytest.raises(ValueError, match="user_confirmed must be a boolean"):
        field.with_value(285.0, user_confirmed=1)

    changed = field.with_value(285.0, user_confirmed=True)
    assert changed.value == 285.0
    assert field.value == 260.0


def test_locked_change_proposal_requires_confirmation_and_creates_audited_revision() -> None:
    intent = _intent()
    proposal = _locked_change()

    with pytest.raises(PermissionError, match="requires user confirmation"):
        intent.apply_change(proposal)

    changed = intent.apply_change(proposal, user_confirmed=True)
    assert changed.revision == 2
    assert changed.status is DesignIntentStatus.NEEDS_CLARIFICATION
    assert changed.requirement(proposal.field_path).value == 285.0
    assert changed.accepted_change_proposal_ids == (proposal.proposal_id,)
    assert intent.requirement(proposal.field_path).value == 260.0


def test_change_application_rejects_stale_or_mismatched_proposals() -> None:
    intent = _intent()
    stale = ChangeProposal.from_dict({**_locked_change().to_dict(), "source_revision": 2})
    with pytest.raises(ValueError, match="does not match intent revision"):
        intent.apply_change(stale, user_confirmed=True)

    wrong_lock = ChangeProposal.from_dict(
        {
            **_locked_change().to_dict(),
            "target_locked": False,
            "requires_user_confirmation": False,
        }
    )
    with pytest.raises(ValueError, match="target_locked does not match"):
        intent.apply_change(wrong_lock)

    stale_value = ChangeProposal.from_dict({**_locked_change().to_dict(), "old_value": 250.0})
    with pytest.raises(ValueError, match="old_value is stale"):
        intent.apply_change(stale_value, user_confirmed=True)


def test_locked_change_proposal_cannot_disable_confirmation() -> None:
    with pytest.raises(ValueError, match="must require user confirmation"):
        ChangeProposal.from_dict(
            {
                **_locked_change().to_dict(),
                "requires_user_confirmation": False,
            }
        )


def test_diagnosis_round_trips_nested_contracts_and_is_json_serializable() -> None:
    question = ClarificationQuestion(
        question_id="clarify-endurance",
        field_path="performance.endurance_h",
        question="Is one hour of cruise a locked minimum?",
        reason="The wording does not identify which requirement may be traded.",
        options=("locked minimum", "soft target"),
        recommended_option="locked minimum",
        consequence_if_unanswered="The solver remains blocked.",
    )
    coverage = ModelCoverageRecord(
        field_path="recovery.parachute_open_mach",
        status="unsupported",
        reason="No validated parachute deployment model is installed.",
        applicable_envelope={"maximum_mach": 0.0},
    )
    diagnosis = FeasibilityDiagnosis(
        status="unsupported",
        summary="The aerodynamic cruise segment is covered, but recovery is not.",
        coverage=(coverage,),
        clarification_questions=(question,),
        change_proposals=(_locked_change(),),
        blocking_reasons=("Parachute deployment is outside model coverage.",),
        assumptions=("ISA atmosphere",),
    )

    assert diagnosis.coverage[0].blocking is True
    payload = diagnosis.to_dict()
    assert json.loads(json.dumps(payload)) == payload
    assert FeasibilityDiagnosis.from_dict(payload) == diagnosis


def test_ready_for_solver_diagnosis_is_explicit_and_fail_closed() -> None:
    covered = ModelCoverageRecord(
        field_path="mission.cruise_mach",
        status=ModelCoverageStatus.COVERED,
        model_id="class-i-cruise-v2",
        applicable_envelope={"minimum": 0.03, "maximum": 0.8},
    )
    diagnosis = FeasibilityDiagnosis(
        status=DesignIntentStatus.READY_FOR_SOLVER,
        summary="All locked fields are covered and internally consistent.",
        coverage=(covered,),
        ready_for_solver=True,
    )
    assert FeasibilityDiagnosis.from_dict(diagnosis.to_dict()) == diagnosis

    with pytest.raises(ValueError, match="must not contain blocking items"):
        FeasibilityDiagnosis(
            status="ready_for_solver",
            summary="Incorrectly marked ready.",
            coverage=(
                ModelCoverageRecord(
                    field_path="launch.booster_end_mach",
                    status="unsupported",
                    reason="No launch model is installed.",
                ),
            ),
            ready_for_solver=True,
        )
    with pytest.raises(ValueError, match="requires ready_for_solver=true"):
        FeasibilityDiagnosis(
            status="ready_for_solver",
            summary="Missing readiness flag.",
        )


def test_unsupported_soft_goal_can_be_non_blocking() -> None:
    soft_reference = ModelCoverageRecord(
        field_path="configuration.reference_style",
        status="unsupported",
        reason="Reference styling is not evaluated by an engineering model.",
        blocking=False,
    )
    diagnosis = FeasibilityDiagnosis(
        status="ready_for_solver",
        summary="Unsupported styling preference does not block engineering sizing.",
        coverage=(soft_reference,),
        ready_for_solver=True,
    )

    assert soft_reference.blocking is False
    assert FeasibilityDiagnosis.from_dict(diagnosis.to_dict()) == diagnosis


def test_status_specific_diagnosis_evidence_is_required() -> None:
    with pytest.raises(ValueError, match="unsupported coverage record"):
        FeasibilityDiagnosis(status="unsupported", summary="No evidence supplied.")
    with pytest.raises(ValueError, match="at least one change proposal"):
        FeasibilityDiagnosis(status="repairable", summary="No proposal supplied.")
    with pytest.raises(ValueError, match="requires conflicting_fields"):
        FeasibilityDiagnosis(
            status="contradictory_requirements",
            summary="No conflict fields supplied.",
        )


def test_nested_contracts_reject_unknown_fields() -> None:
    with pytest.raises(ValueError, match="unsupported clarification question fields"):
        ClarificationQuestion.from_dict(
            {
                "question_id": "q1",
                "field_path": "mission.range_m",
                "question": "Which range?",
                "reason": "Range is missing.",
                "auto_answer": True,
            }
        )
    with pytest.raises(ValueError, match="unsupported model coverage record fields"):
        ModelCoverageRecord.from_dict(
            {
                "field_path": "mission.range_m",
                "status": "covered",
                "optimistic": True,
            }
        )
    with pytest.raises(ValueError, match="unsupported feasibility diagnosis fields"):
        FeasibilityDiagnosis.from_dict(
            {
                "status": "needs_clarification",
                "summary": "Missing payload.",
                "silent_defaults": True,
            }
        )
