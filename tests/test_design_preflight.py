"""Contract tests for deterministic aircraft-design intake preflight."""

from __future__ import annotations

import pytest

from src.design_intake.coverage import (
    MODEL_COVERAGE_MATRIX,
    assess_model_coverage,
    canonical_coverage_key,
    coverage_for_requirement,
    coverage_matrix_as_dict,
)
from src.design_intake.models import (
    DesignIntent,
    DesignIntentStatus,
    FeasibilityDiagnosis,
    ModelCoverageStatus,
    RequirementField,
    RequirementRole,
    RequirementSource,
)
from src.design_intake.preflight import diagnose_design_intent, preflight_design_intent


UNSUPPORTED_RUNNER_FIELDS = {
    "max_flight_mach",
    "launch_mode",
    "launch_field_altitude_m",
    "booster_end_mach",
    "booster_end_relative_altitude_m",
    "recovery_mode",
    "parachute_open_mach",
    "parachute_open_relative_altitude_m",
    "engine_count",
    "configuration_reference",
    "stealth_requirement",
    "min_cruise_endurance_s",
}


def _field(
    path: str,
    value: object,
    *,
    role: RequirementRole = RequirementRole.HARD_CONSTRAINT,
    locked: bool = True,
    source: RequirementSource = RequirementSource.USER,
) -> RequirementField:
    return RequirementField(
        path=path,
        value=value,
        role=role,
        locked=locked,
        source=source,
    )


def _intent(
    *requirements: RequirementField,
    intent_id: str = "preflight-test",
    **values: object,
) -> DesignIntent:
    return DesignIntent(intent_id=intent_id, requirements=requirements, **values)


def _minimum_core() -> tuple[RequirementField, ...]:
    return (
        _field("mission.range_m", 800_000.0),
        _field("mission.payload_kg", 60.0),
    )


def test_coverage_matrix_explicitly_tracks_every_runner_model_gap() -> None:
    assert UNSUPPORTED_RUNNER_FIELDS <= set(MODEL_COVERAGE_MATRIX)
    for field_name in UNSUPPORTED_RUNNER_FIELDS:
        assert MODEL_COVERAGE_MATRIX[field_name].status is ModelCoverageStatus.UNSUPPORTED

    snapshot = coverage_matrix_as_dict()
    assert snapshot["max_flight_mach"]["status"] == "unsupported"
    assert snapshot["launch_mode"]["model_id"] is None
    assert snapshot["range_m"]["status"] == "covered"
    assert snapshot["min_cruise_endurance_s"]["status"] == "unsupported"


def test_cruise_endurance_without_total_range_fails_closed_for_both_gaps() -> None:
    intent = _intent(
        _field("requirements.payload_kg", 60.0),
        _field("requirements.cruise_mach", 0.6),
        _field("requirements.cruise_altitude_m", 9_500.0),
        _field("performance.min_cruise_endurance_s", 3_600.0),
    )

    diagnosis = diagnose_design_intent(intent)

    assert diagnosis.status is DesignIntentStatus.UNSUPPORTED
    endurance = next(
        item
        for item in diagnosis.coverage
        if item.field_path == "performance.min_cruise_endurance_s"
    )
    assert endurance.status is ModelCoverageStatus.UNSUPPORTED
    assert endurance.blocking is True
    assert any(
        question.question_id == "mission.range.required"
        for question in diagnosis.clarification_questions
    )


@pytest.mark.parametrize(
    ("path", "canonical"),
    [
        ("requirements.max_flight_mach", "max_flight_mach"),
        ("performance.max_mach", "max_flight_mach"),
        ("mission.launch.mode", "launch_mode"),
        ("recovery.parachute_open_mach", "parachute_open_mach"),
        ("propulsion.engine_count", "engine_count"),
        ("configuration.reference", "configuration_reference"),
        ("configuration.stealth_requirement", "stealth_requirement"),
    ],
)
def test_coverage_path_aliases_are_canonical(path: str, canonical: str) -> None:
    assert canonical_coverage_key(path) == canonical


def test_unsupported_soft_reference_is_recorded_without_blocking_solver() -> None:
    reference = _field(
        "configuration.reference",
        "reference-aircraft-style",
        role=RequirementRole.SOFT_GOAL,
        locked=False,
    )
    record = coverage_for_requirement(reference)

    assert record.status is ModelCoverageStatus.UNSUPPORTED
    assert record.blocking is False

    diagnosis = diagnose_design_intent(_intent(*_minimum_core(), reference))
    assert diagnosis.status is DesignIntentStatus.READY_FOR_SOLVER
    assert diagnosis.ready_for_solver is True
    assert diagnosis.coverage[-1].status is ModelCoverageStatus.UNSUPPORTED
    assert diagnosis.coverage[-1].blocking is False


def test_top_level_reference_label_is_not_reinterpreted_as_locked_tail_layout() -> None:
    reference = _field(
        "configuration.reference",
        "Shahed-136",
        role=RequirementRole.SOFT_GOAL,
        locked=False,
    )
    intent = _intent(*_minimum_core(), reference, configuration="Shahed-136")

    diagnosis = diagnose_design_intent(intent)

    coverage = {item.field_path: item for item in diagnosis.coverage}
    assert coverage["configuration.reference"].status is ModelCoverageStatus.UNSUPPORTED
    assert coverage["configuration.reference"].blocking is False
    assert "configuration" not in coverage
    assert diagnosis.status is DesignIntentStatus.READY_FOR_SOLVER


def test_deferred_field_does_not_shadow_active_solver_baseline() -> None:
    intent = _intent(
        _field("mission.range_m", 500_000.0),
        _field("mission.payload_kg", 20.0),
        _field(
            "deferred.requirements.cruise_altitude_m",
            40_000.0,
            role=RequirementRole.SOFT_GOAL,
            locked=False,
        ),
        _field(
            "requirements.cruise_altitude_m",
            6_000.0,
            role=RequirementRole.TECHNOLOGY_ASSUMPTION,
            locked=False,
            source=RequirementSource.DEFAULT,
        ),
        _field(
            "requirements.service_ceiling_m",
            8_000.0,
            role=RequirementRole.TECHNOLOGY_ASSUMPTION,
            locked=False,
            source=RequirementSource.DEFAULT,
        ),
    )

    diagnosis = diagnose_design_intent(intent)

    assert diagnosis.status is DesignIntentStatus.READY_FOR_SOLVER
    deferred = next(
        item
        for item in diagnosis.coverage
        if item.field_path == "deferred.requirements.cruise_altitude_m"
    )
    assert deferred.status is ModelCoverageStatus.UNSUPPORTED
    assert deferred.blocking is False


def test_top_level_launch_and_recovery_are_not_lost_from_coverage() -> None:
    intent = _intent(*_minimum_core(), launch="rocket_assist", recovery="parachute")

    coverage = assess_model_coverage(intent)

    by_path = {item.field_path: item for item in coverage}
    assert by_path["launch"].status is ModelCoverageStatus.UNSUPPORTED
    assert by_path["launch"].blocking is True
    assert by_path["recovery"].status is ModelCoverageStatus.UNSUPPORTED


def test_missing_core_input_requires_bounded_clarification() -> None:
    intent = _intent(_field("mission.payload_kg", 10.0))

    diagnosis = preflight_design_intent(intent)

    assert diagnosis.status is DesignIntentStatus.NEEDS_CLARIFICATION
    assert diagnosis.ready_for_solver is False
    assert [item.question_id for item in diagnosis.clarification_questions] == [
        "mission.range.required"
    ]
    assert diagnosis.change_proposals == ()


def test_high_cruise_altitude_requests_service_ceiling_in_first_question_batch() -> None:
    intent = _intent(
        _field("requirements.range_m", 1_200_000.0),
        _field("requirements.cruise_mach", 0.6),
        _field("requirements.cruise_altitude_m", 10_000.0),
    )

    diagnosis = diagnose_design_intent(intent)

    assert diagnosis.status is DesignIntentStatus.NEEDS_CLARIFICATION
    assert [item.question_id for item in diagnosis.clarification_questions] == [
        "mission.payload.required",
        "propulsion.type.high_speed",
        "performance.service_ceiling.high_cruise",
    ]
    ceiling = diagnosis.clarification_questions[-1]
    assert ceiling.field_path == "requirements.service_ceiling_m"
    assert "10500.0 m" in ceiling.question
    assert ceiling.options == ()


def test_model_gaps_are_unsupported_not_physically_infeasible() -> None:
    paths_and_values = {
        "performance.max_flight_mach": 0.8,
        "launch.mode": "rocket_assist",
        "launch.field_altitude_m": 1_500.0,
        "launch.booster_end_mach": 0.28,
        "launch.booster_end_relative_altitude_m": 40.0,
        "recovery.mode": "parachute",
        "recovery.parachute_open_mach": 0.24,
        "recovery.parachute_open_relative_altitude_m": 1_000.0,
        "propulsion.engine_count": 1,
        "configuration.reference": "reference-aircraft-style",
        "configuration.stealth_requirement": True,
        "performance.min_cruise_endurance_s": 3_600.0,
    }
    requirements = [*_minimum_core()]
    requirements.extend(_field(path, value) for path, value in paths_and_values.items())

    diagnosis = diagnose_design_intent(_intent(*requirements))

    assert diagnosis.status is DesignIntentStatus.UNSUPPORTED
    assert diagnosis.status is not DesignIntentStatus.INFEASIBLE
    assert diagnosis.ready_for_solver is False
    unsupported = {
        canonical_coverage_key(item.field_path)
        for item in diagnosis.coverage
        if item.status is ModelCoverageStatus.UNSUPPORTED
    }
    assert unsupported == UNSUPPORTED_RUNNER_FIELDS
    assert "not a physical infeasibility" in diagnosis.summary
    assert diagnosis.conflicting_fields == ()


def test_locked_ceiling_contradiction_proposes_two_confirmed_alternatives() -> None:
    cruise = _field("performance.cruise_altitude_m", 11_000.0)
    ceiling = _field("performance.service_ceiling_m", 10_000.0)
    intent = _intent(*_minimum_core(), cruise, ceiling)
    before = intent.to_dict()

    diagnosis = diagnose_design_intent(intent)

    assert diagnosis.status is DesignIntentStatus.CONTRADICTORY_REQUIREMENTS
    assert set(diagnosis.conflicting_fields) == {cruise.path, ceiling.path}
    assert {item.proposal_id for item in diagnosis.change_proposals} == {
        "ceiling.raise_service_ceiling",
        "ceiling.lower_cruise_altitude",
    }
    assert all(item.target_locked for item in diagnosis.change_proposals)
    assert all(item.requires_user_confirmation for item in diagnosis.change_proposals)
    assert intent.to_dict() == before
    with pytest.raises(PermissionError, match="requires user confirmation"):
        intent.apply_change(diagnosis.change_proposals[0])


def test_unlocked_derived_ceiling_is_repairable_without_mutation() -> None:
    cruise = _field("performance.cruise_altitude_m", 11_000.0)
    ceiling = _field(
        "performance.service_ceiling_m",
        10_000.0,
        role=RequirementRole.DESIGN_VARIABLE,
        locked=False,
        source=RequirementSource.DERIVED,
    )
    intent = _intent(*_minimum_core(), cruise, ceiling)

    diagnosis = diagnose_design_intent(intent)

    assert diagnosis.status is DesignIntentStatus.REPAIRABLE
    assert diagnosis.conflicting_fields == ()
    raise_ceiling = next(
        item
        for item in diagnosis.change_proposals
        if item.proposal_id == "ceiling.raise_service_ceiling"
    )
    assert raise_ceiling.target_locked is False
    assert raise_ceiling.requires_user_confirmation is False
    assert intent.requirement(ceiling.path).value == 10_000.0


def test_maximum_mach_below_cruise_is_a_logical_conflict_despite_model_gap() -> None:
    cruise = _field("performance.cruise_mach", 0.8)
    maximum = _field("performance.max_flight_mach", 0.7)
    intent = _intent(*_minimum_core(), cruise, maximum, propulsion="jet")

    diagnosis = diagnose_design_intent(intent)

    assert diagnosis.status is DesignIntentStatus.CONTRADICTORY_REQUIREMENTS
    assert set(diagnosis.conflicting_fields) == {cruise.path, maximum.path}
    assert any(
        item.field_path == maximum.path
        and item.status is ModelCoverageStatus.UNSUPPORTED
        for item in diagnosis.coverage
    )
    assert {item.proposal_id for item in diagnosis.change_proposals} >= {
        "mach.raise_maximum_mach",
        "mach.lower_cruise_mach",
    }


def test_high_payload_fraction_is_repairable_with_mass_trade_options() -> None:
    payload = _field("mission.payload_kg", 80.0)
    mtow = _field("weights.max_mtow_kg", 120.0)
    intent = _intent(_field("mission.range_m", 300_000.0), payload, mtow)

    diagnosis = diagnose_design_intent(intent)

    assert diagnosis.status is DesignIntentStatus.REPAIRABLE
    proposals = {item.proposal_id: item for item in diagnosis.change_proposals}
    assert {"mass.increase_mtow_allowance", "mass.reduce_payload"} <= set(proposals)
    assert proposals["mass.increase_mtow_allowance"].proposed_value >= 160.0
    assert proposals["mass.reduce_payload"].proposed_value <= 60.0
    assert all(item.requires_user_confirmation for item in proposals.values())


def test_payload_at_or_above_locked_mtow_is_contradictory() -> None:
    payload = _field("mission.payload_kg", 120.0)
    mtow = _field("weights.max_mtow_kg", 100.0)

    diagnosis = diagnose_design_intent(
        _intent(_field("mission.range_m", 300_000.0), payload, mtow)
    )

    assert diagnosis.status is DesignIntentStatus.CONTRADICTORY_REQUIREMENTS
    assert set(diagnosis.conflicting_fields) == {payload.path, mtow.path}


def test_aspect_ratio_limit_generates_geometry_trade_options() -> None:
    selected = _field(
        "initial_guess.aspect_ratio",
        4.0,
        role=RequirementRole.DESIGN_VARIABLE,
        locked=False,
        source=RequirementSource.DERIVED,
    )
    maximum = _field("geometry.max_aspect_ratio", 2.5)

    diagnosis = diagnose_design_intent(_intent(*_minimum_core(), selected, maximum))

    assert diagnosis.status is DesignIntentStatus.REPAIRABLE
    proposals = {item.proposal_id: item for item in diagnosis.change_proposals}
    assert proposals["geometry.reduce_aspect_ratio"].proposed_value == 2.5
    assert proposals["geometry.reduce_aspect_ratio"].requires_user_confirmation is False
    assert proposals["geometry.relax_aspect_ratio_limit"].requires_user_confirmation is True


def test_long_range_low_reserve_is_repairable_and_never_silently_changed() -> None:
    reserve = _field("mission.reserve_fraction", 0.03)
    intent = _intent(
        _field("mission.range_m", 1_200_000.0),
        _field("mission.payload_kg", 20.0),
        reserve,
    )

    diagnosis = diagnose_design_intent(intent)

    assert diagnosis.status is DesignIntentStatus.REPAIRABLE
    proposal = next(
        item
        for item in diagnosis.change_proposals
        if item.proposal_id == "mission.restore_preliminary_reserve"
    )
    assert proposal.old_value == 0.03
    assert proposal.proposed_value == 0.05
    assert proposal.requires_user_confirmation is True
    assert intent.requirement(reserve.path).value == 0.03


def test_tight_field_length_requests_high_lift_clarification() -> None:
    diagnosis = diagnose_design_intent(
        _intent(*_minimum_core(), _field("mission.takeoff_distance_m", 80.0))
    )

    assert diagnosis.status is DesignIntentStatus.NEEDS_CLARIFICATION
    question = diagnosis.clarification_questions[0]
    assert question.question_id == "field_length.takeoff.assumption"
    assert question.recommended_option == "provide_project_specific_high_lift_data"


def test_diagnosis_is_json_safe_and_round_trips_through_shared_contract() -> None:
    intent = _intent(
        *_minimum_core(),
        _field("performance.cruise_mach", 0.3),
        _field("performance.cruise_altitude_m", 3_000.0),
        _field("performance.service_ceiling_m", 5_000.0),
        _field(
            "initial_guess.wing_loading_pa",
            900.0,
            role=RequirementRole.DESIGN_VARIABLE,
            locked=False,
            source=RequirementSource.DERIVED,
        ),
    )

    diagnosis = diagnose_design_intent(intent)
    restored = FeasibilityDiagnosis.from_dict(diagnosis.to_dict())

    assert diagnosis.status is DesignIntentStatus.READY_FOR_SOLVER
    assert diagnosis.ready_for_solver is True
    assert restored == diagnosis
    assert restored.assumptions == (
        "initial_guess.wing_loading_pa uses a derived value and remains subject to confirmation.",
    )


def test_preflight_accepts_mapping_contract_without_changing_revision() -> None:
    intent = _intent(*_minimum_core(), intent_id="mapping-input")

    diagnosis = diagnose_design_intent(intent.to_dict())

    assert diagnosis.status is DesignIntentStatus.READY_FOR_SOLVER
    assert diagnosis.ready_for_solver is True
    assert intent.revision == 1
