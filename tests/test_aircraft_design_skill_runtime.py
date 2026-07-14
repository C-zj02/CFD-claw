"""Runtime regressions for the integrated upstream aircraft design skill."""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
UPSTREAM_ROOT = PROJECT_ROOT / "external" / "aircraft-design-skill"
sys.path.insert(0, str(UPSTREAM_ROOT))

from aircraft_design.class2_preliminary.design_loop_orchestrator import (  # noqa: E402
    DesignRequirements,
    InitialGuess,
    SizedAircraft,
    sizing_loop,
)
from aircraft_design.class2_preliminary import advanced_design as advanced_design_module  # noqa: E402
from aircraft_design.class2_preliminary.advanced_design import (  # noqa: E402
    AdvancedDesignStageError,
    Stage2AeroResult,
    Stage3PropulsionResult,
    Stage4MissionResult,
    Stage5StabilityResult,
    execute_advanced_design,
)
from aircraft_design.class2_preliminary.run_sizing import setup_output_directory  # noqa: E402
from aircraft_design.class2_preliminary.server import SizingResponse  # noqa: E402
from aircraft_design.class2_preliminary.result_contract import (  # noqa: E402
    normalized_advanced_constraints,
)
from aircraft_design.utils.report_generator_unified import UnifiedReportGenerator  # noqa: E402


def test_sizing_api_response_preserves_range_evidence_kind() -> None:
    response = SizingResponse(
        converged=True,
        mtow_kg=250.0,
        empty_weight_kg=130.0,
        fuel_weight_kg=60.0,
        wing_area_m2=8.0,
        thrust_sl_n=1_800.0,
        geometry={},
        weight_breakdown={},
        performance={
            "actual_range_m": 500_000.0,
            "range_metric_kind": "evaluated_mission_distance",
            "takeoff_distance_m": 300.0,
            "landing_distance_m": 250.0,
        },
        iterations=12,
    )

    assert response.performance.range_metric_kind == "evaluated_mission_distance"
    assert response.model_dump()["performance"]["range_metric_kind"] == (
        "evaluated_mission_distance"
    )


def test_sized_aircraft_range_evidence_defaults_to_unknown() -> None:
    result = SizedAircraft(
        mtow_kg=1.0,
        empty_weight_kg=0.5,
        fuel_weight_kg=0.25,
        wing_area_m2=1.0,
        thrust_sl_n=10.0,
        weight_breakdown={},
        geometry={},
        actual_range_m=1_000.0,
        takeoff_distance_m=10.0,
        landing_distance_m=10.0,
        converged=True,
        iterations=1,
    )

    assert result.range_metric_kind == "unknown"


def test_unified_report_fails_closed_for_unknown_range_evidence() -> None:
    section = UnifiedReportGenerator(project_name="unknown-range")._section_requirements_analysis(
        {},
        {},
        {"actual_range_m": 500_000.0, "range_metric_kind": "unknown"},
    )

    assert "航程指标（证据类型未声明）" in section
    assert "不得解释为实际、已达或最大航程能力" in section
    assert "预测最大航程" not in section
    assert "评估任务航程" not in section


def test_medium_uav_sizing_initializes_scale_classification() -> None:
    requirements = DesignRequirements(
        range_m=1_200_000.0,
        payload_kg=500.0,
        cruise_mach=0.22,
        cruise_altitude_m=6_000.0,
        takeoff_distance_m=600.0,
        landing_distance_m=500.0,
        max_load_factor=3.8,
        sustained_turn_g=2.0,
        service_ceiling_m=8_000.0,
    )
    guess = InitialGuess(
        mtow_kg=5_000.0,
        wing_loading_pa=3_000.0,
        thrust_to_weight=0.6,
        aspect_ratio=10.0,
        sweep_deg=5.0,
        taper_ratio=0.5,
        thickness_ratio=0.12,
        sfc_cruise_1_s=0.5 / 3_600.0,
        cd0=0.025,
        oswald_e=0.82,
    )

    result = sizing_loop(
        requirements,
        guess,
        enable_visualization=False,
        max_iter=1,
    )

    assert result.iterations == 1
    assert result.mtow_kg > 0.0
    assert result.range_metric_kind == "evaluated_mission_distance"


def test_infeasible_landing_distance_preserves_finite_design_state() -> None:
    requirements = DesignRequirements(
        range_m=120_000.0,
        payload_kg=10.0,
        cruise_mach=0.25,
        cruise_altitude_m=3_000.0,
        takeoff_distance_m=350.0,
        landing_distance_m=350.0,
        max_load_factor=3.8,
        sustained_turn_g=2.0,
        service_ceiling_m=6_000.0,
        propulsion_type="jet",
    )
    guess = InitialGuess(
        mtow_kg=50.0,
        wing_loading_pa=350.0,
        thrust_to_weight=0.35,
        aspect_ratio=9.0,
        sweep_deg=0.0,
        taper_ratio=0.5,
        thickness_ratio=0.12,
        jet_tsfc_kg_per_n_s=2.3e-5,
        cd0=0.032,
        oswald_e=0.82,
    )

    result = sizing_loop(
        requirements,
        guess,
        enable_visualization=False,
        max_iter=1,
    )

    assert result.mtow_kg > 0.0
    assert result.wing_area_m2 > 0.0
    assert result.design_point["wing_loading_pa"] == pytest.approx(100.0)
    landing = next(item for item in result.constraints if item["id"] == "class1.landing_distance")
    assert landing["passed"] is False


def test_setup_output_directory_keeps_sanitized_project_inside_base(tmp_path: Path) -> None:
    output_base = tmp_path / "generated" / "output"

    output_path = setup_output_directory(
        str(output_base),
        project_name="../../nested/project",
    )

    relative = output_path.resolve().relative_to(output_base.resolve())
    assert output_path.parent == output_base.resolve()
    assert len(relative.parts) == 1
    assert relative.name.startswith("nested_project_")


def test_unified_report_improvements_preserve_canonical_failure_recommendations() -> None:
    recommendations = [
        "Increase installed climb thrust.",
        "Reduce mission fuel demand.",
        "Restore positive static margin.",
        "Reduce structural utilization.",
    ]
    canonical_constraints = [
        {
            "id": constraint_id,
            "passed": False,
            "recommendation": recommendation,
        }
        for constraint_id, recommendation in zip(
            ("propulsion.climb", "mission.fuel", "stability.static_margin", "structures.utilization"),
            recommendations,
            strict=True,
        )
    ]
    generator = UnifiedReportGenerator(project_name="canonical-constraints")

    section = generator._section_improvements(
        outputs={"converged": True},
        metrics={"thrust_to_weight": 0.5, "wing_loading_pa": 3_000.0},
        advanced_data={"geometry_constraints": [{"name": "Fuel volume", "passed": False}]},
        status={"engineering_feasible": False},
        constraints=canonical_constraints,
    )

    assert "几何约束未通过" in section
    for recommendation in recommendations:
        assert recommendation in section
    assert generator._fmt_num(8.2e-8) == "8.2000e-08"


def test_stage6_failure_preserves_stage2_through_stage5_partial_results(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    stage2 = Stage2AeroResult(0.025, {}, 0.0, 0.0, 0.01, 0.035, 0.22, {})
    stage3 = Stage3PropulsionResult(5_000.0, 5_500.0, 0.2, 0.1, 1e-5, 1e-5, 1.0, 1.1)
    stage4 = Stage4MissionResult(0.2, 500.0, [], 10_000.0, 1_000_000.0)
    stage5 = Stage5StabilityResult(0.1, -0.2, 0.32, 0.22, 0.3, 0.5, 4.0, 1.5)
    stage6_cause = RuntimeError("synthetic Stage 6 failure")

    monkeypatch.setattr(advanced_design_module, "execute_stage2_aero", lambda **_kwargs: stage2)
    monkeypatch.setattr(advanced_design_module, "execute_stage3_propulsion", lambda **_kwargs: stage3)
    monkeypatch.setattr(advanced_design_module, "build_propulsion_model", lambda *_args, **_kwargs: object())
    monkeypatch.setattr(advanced_design_module, "execute_stage4_mission", lambda **_kwargs: stage4)
    monkeypatch.setattr(advanced_design_module, "execute_stage5_stability", lambda **_kwargs: stage5)

    def fail_stage6(**_kwargs):
        raise stage6_cause

    monkeypatch.setattr(advanced_design_module, "execute_stage6_structures", fail_stage6)

    with pytest.raises(AdvancedDesignStageError) as caught:
        execute_advanced_design(
            design_input={
                "cruise_altitude_m": 6_000.0,
                "cruise_speed_m_s": 70.0,
                "mtow_kg": 2_500.0,
                "cl_cruise": 0.6,
            },
            mission_input={},
            propulsion_input={"type": "prop"},
            geometry_input={
                "s_ref_m2": 20.0,
                "b_m": 14.0,
                "cbar_m": 1.5,
                "wing_t_c": 0.12,
                "fuselage_length_m": 8.0,
                "fuselage_diameter_m": 1.2,
                "sweep_quarter_chord_deg": 5.0,
                "aspect_ratio": 10.0,
                "taper_ratio": 0.5,
            },
            stability_input={},
            structures_input={},
        )

    error = caught.value
    assert error.stage_id == "stage6_structures"
    assert error.cause is stage6_cause
    assert error.__cause__ is stage6_cause
    assert error.partial_results == {
        "stage2_aero": stage2,
        "stage3_propulsion": stage3,
        "stage4_mission": stage4,
        "stage5_stability": stage5,
    }


def test_partial_advanced_results_do_not_fabricate_unexecuted_constraints() -> None:
    constraints = normalized_advanced_constraints(
        {
            "stage2_aero": {"cd0": 0.025},
            "failure": {"stage_id": "stage3_propulsion", "error": "synthetic"},
        },
        available_fuel_kg=100.0,
        class1_structure_kg=200.0,
    )

    assert constraints == []


def test_unified_report_loads_preserved_partial_advanced_results(tmp_path: Path) -> None:
    partial = {
        "stage2_aero": {"cd0": 0.025},
        "stage3_propulsion": {"thrust_margin_cruise": 0.1},
        "failure": {"stage_id": "stage4_mission", "error": "synthetic"},
    }
    partial_path = tmp_path / "advanced_design_partial.json"
    partial_path.write_text(json.dumps(partial), encoding="utf-8")

    filename, loaded = UnifiedReportGenerator(
        project_name="partial-advanced-results"
    )._load_latest_advanced_results(tmp_path)

    assert filename == partial_path.name
    assert loaded == partial
