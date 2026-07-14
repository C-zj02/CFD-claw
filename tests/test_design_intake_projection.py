"""Projection tests between design intent and the strict solver contract."""

from __future__ import annotations

import pytest

from src.design_execution.models import AircraftDesignRequest
from src.design_intake.models import DesignIntentStatus, RequirementRole, RequirementSource
from src.design_intake.parser import parse_design_intent, with_intent_status
from src.design_intake.projection import intent_from_aircraft_request, solver_request_from_intent
from src.design_intake.projection import complete_intent_with_solver_defaults


def test_existing_solver_request_becomes_auditable_intent() -> None:
    request = AircraftDesignRequest.from_dict(
        {
            "project_name": "projection",
            "requirements": {"range_m": 400_000.0, "payload_kg": 25.0},
            "initial_guess": {"cd0": 0.028},
            "provenance": {
                "input_fields": {
                    "requirements": {
                        "range_m": {"source": "user"},
                        "payload_kg": {"source": "user"},
                    },
                    "initial_guess": {"cd0": {"source": "user"}},
                },
                "user_requirements": {"max_aspect_ratio": 8.5},
            },
        }
    )

    intent = intent_from_aircraft_request(request)

    assert intent.requirement("requirements.range_m").locked is True
    assert intent.requirement("requirements.cruise_mach").source is RequirementSource.DEFAULT
    assert intent.requirement("initial_guess.cd0").role is RequirementRole.TECHNOLOGY_ASSUMPTION
    assert intent.requirement("initial_guess.cd0").locked is False
    assert intent.requirement("geometry.max_aspect_ratio").locked is True


def test_request_presence_can_supply_sources_when_custom_provenance_is_incomplete() -> None:
    request = AircraftDesignRequest.from_dict(
        {
            "project_name": "source_override",
            "requirements": {
                "range_m": 400_000.0,
                "payload_kg": 25.0,
                "cruise_mach": 0.7,
            },
            "provenance": {"user_requirements": {"max_flight_mach": 0.6}},
        }
    )

    intent = intent_from_aircraft_request(
        request,
        field_sources={
            "requirements.range_m": "user",
            "requirements.payload_kg": "user",
            "requirements.cruise_mach": "user",
        },
    )

    assert intent.requirement("requirements.cruise_mach").source is RequirementSource.USER
    assert intent.requirement("requirements.cruise_mach").locked is True


def test_projection_refuses_unconfirmed_or_incomplete_intent() -> None:
    intent = parse_design_intent("设计一款无人机，航程500km，载荷20kg。")

    with pytest.raises(ValueError, match="ready_for_solver"):
        solver_request_from_intent(intent)

    incomplete = parse_design_intent("设计一款无人机，载荷20kg。")
    with pytest.raises(ValueError, match="missing solver requirements: range_m"):
        solver_request_from_intent(incomplete, require_ready=False)


def test_projection_preserves_special_requirements_in_provenance() -> None:
    intent = parse_design_intent(
        "设计一款隐身无人机，航程500km，载荷20kg，采用火箭助推和伞降回收，"
        "最大飞行马赫数0.7，单发布局，布局可参考某型无人机。"
    )
    request = solver_request_from_intent(intent, require_ready=False)

    declared = request.provenance["user_requirements"]
    assert declared["launch_mode"] == "rocket_assist"
    assert declared["recovery_mode"] == "parachute"
    assert declared["max_flight_mach"] == 0.7
    assert declared["engine_count"] == 1
    assert declared["stealth_requirement"] is True
    assert request.provenance["soft_goals"]["configuration_reference"] == "某型无人机"
    assert request.provenance["projection"]["complete_declared_intent_preserved"] is True


def test_ready_projection_honors_declared_mtow_and_aspect_ratio_as_initial_bounds() -> None:
    intent = parse_design_intent(
        "设计一款无人机，最大起飞重量不大于260kg，航程500km，载荷60kg，"
        "展弦比不大于2.5。"
    )
    ready = with_intent_status(intent, DesignIntentStatus.READY_FOR_SOLVER)

    request = solver_request_from_intent(ready)

    assert request.initial_guess.mtow_kg == 260.0
    assert request.initial_guess.aspect_ratio == 2.5
    assert request.provenance["user_requirements"]["max_mtow_kg"] == 260.0
    assert request.provenance["user_requirements"]["max_aspect_ratio"] == 2.5


def test_solver_defaults_are_materialized_without_overwriting_user_fields() -> None:
    intent = parse_design_intent("设计一款无人机，航程500km，载荷20kg。")

    completed = complete_intent_with_solver_defaults(intent)

    assert completed.requirement("requirements.range_m").value == 500_000.0
    assert completed.requirement("requirements.range_m").source is RequirementSource.USER
    default_cruise = completed.requirement("requirements.cruise_mach")
    assert default_cruise.source is RequirementSource.DEFAULT
    assert default_cruise.role is RequirementRole.TECHNOLOGY_ASSUMPTION
    assert default_cruise.locked is False
    assert completed.requirement("initial_guess.cd0").source is RequirementSource.DERIVED
    added = completed.metadata["solver_completion"]["added_field_paths"]
    assert "requirements.cruise_mach" in added
    assert "initial_guess.cd0" in added
    assert completed.revision == intent.revision
