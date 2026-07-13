"""Tests for deterministic aircraft design execution."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from src.design_execution import (
    AircraftDesignEngineeringResult,
    AircraftDesignRequest,
    AircraftDesignRunner,
    DesignRunStage,
    DesignRunStatus,
)
from src.design_execution.repair import propose_aircraft_design_repair


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _medium_uav_request() -> AircraftDesignRequest:
    return AircraftDesignRequest.from_dict(
        {
            "project_name": "UAV 1200 km / 500 kg",
            "requirements": {
                "range_m": 1_200_000.0,
                "payload_kg": 500.0,
                "cruise_mach": 0.22,
                "cruise_altitude_m": 6_000.0,
                "service_ceiling_m": 8_000.0,
            },
        }
    )


def test_request_applies_stable_medium_uav_defaults() -> None:
    request = _medium_uav_request()

    assert request.project_name == "UAV_1200_km_500_kg"
    assert request.requirements.takeoff_distance_m == 1_000.0
    assert request.requirements.landing_distance_m == 1_000.0
    assert request.initial_guess.mtow_kg == 2_500.0
    assert request.initial_guess.wing_loading_pa == 3_000.0
    assert request.initial_guess.thrust_to_weight == 0.6
    assert request.initial_guess.sfc_cruise_1_s is None
    assert request.initial_guess.jet_tsfc_kg_per_n_s is None
    assert request.initial_guess.prop_bsfc_kg_per_j == pytest.approx(8.45e-8)
    assert request.initial_guess.prop_bsfc_kg_per_j != pytest.approx(0.8 / 3_600.0)
    assert request.to_upstream_dict()["solver_options"]["max_iter"] == 50
    assert request.auto_repair_enabled is False
    assert request.max_repair_attempts == 3
    assert request.initial_guess.cg_fraction_cbar == pytest.approx(0.30)
    assert request.initial_guess.horizontal_tail_volume_coefficient == pytest.approx(0.40)


def test_request_contract_round_trips_and_accepts_legacy_solver_options() -> None:
    request = AircraftDesignRequest.from_dict(
        {
            **_medium_uav_request().to_dict(),
            "tolerance": 0.002,
            "max_iterations": 75,
        }
    )

    assert AircraftDesignRequest.from_dict(request.to_dict()) == request

    legacy = request.to_dict()
    legacy.pop("tolerance")
    legacy.pop("max_iterations")
    legacy["solver_options"] = {"tolerance": 0.002, "max_iter": 75}
    assert AircraftDesignRequest.from_dict(legacy) == request


@pytest.mark.parametrize(
    "payload,error",
    [
        ({"requirements": {"range_m": 1_000.0}}, "payload_kg"),
        (
            {"requirements": {"range_m": 1_000.0, "payload_kg": 1.0, "unknown": 2}},
            "unsupported requirement fields",
        ),
        (
            {
                "requirements": {
                    "range_m": 1_000.0,
                    "payload_kg": 1.0,
                    "cruise_altitude_m": 10_000.0,
                    "service_ceiling_m": 8_000.0,
                }
            },
            "service_ceiling_m",
        ),
    ],
)
def test_request_rejects_invalid_contract(payload: dict, error: str) -> None:
    with pytest.raises(ValueError, match=error):
        AircraftDesignRequest.from_dict(payload)


def test_runner_delivers_medium_uav_after_full_engineering_closure() -> None:
    events = []
    with tempfile.TemporaryDirectory() as temp_dir:
        runner = AircraftDesignRunner(PROJECT_ROOT, generated_root=Path(temp_dir))
        result = runner.run(
            _medium_uav_request(),
            timeout_seconds=30.0,
            on_progress=events.append,
            run_id="integration-run",
        )

        assert result.status is DesignRunStatus.COMPLETED
        assert result.succeeded
        assert result.converged is True
        assert result.exit_code == 0
        assert result.output_dir is not None
        assert (result.output_dir / "design_data.json").is_file()
        assert (result.output_dir / "design_report.md").is_file()
        assert any(path.name == "geometry.obj" for path in result.artifacts)
        assert result.design_data["inputs"]["requirements"]["range_m"] == 1_200_000.0
        assert result.design_data["inputs"]["requirements"]["payload_kg"] == 500.0
        assert result.design_data["schema_id"] == "aircraft-design/design-data"
        assert result.design_data["schema_version"] == 2
        assert result.design_data["numerical_converged"] is True
        assert result.design_data["engineering_feasible"] is True
        assert isinstance(result.design_data["constraints"], list)
        assert result.design_data["constraints"]
        assert isinstance(result.design_data["stage_status"], dict)
        assert isinstance(result.design_data["provenance"], dict)
        assert isinstance(result.design_data["iteration_history"], list)
        assert isinstance(result.design_data["design_adjustments"], list)
        assert isinstance(result.design_data["design_point"], dict)
        for constraint in result.design_data["constraints"]:
            assert {
                "id",
                "label",
                "category",
                "direction",
                "required",
                "actual",
                "unit",
                "margin",
                "margin_ratio",
                "passed",
                "severity",
                "blocking",
                "evidence",
                "recommendation",
            } <= constraint.keys()
        assert result.engineering is not None
        assert result.engineering.numerical_converged is True
        assert result.engineering.engineering_feasible is True
        assert result.engineering.blocking_failed_count == 0
        assert not [issue for issue in result.issues if issue.severity == "error"]
        summary = result.to_dict()["summary"]
        assert summary["wing_loading_pa"] > 0
        assert summary["thrust_to_weight"] > 0
        assert summary["span_m"] > 0
        assert summary["iterations"] > 0
        assert summary["artifact_count"] > 0
        manifest = json.loads((result.task_dir / "run_result.json").read_text(encoding="utf-8"))
        assert manifest["status"] == "completed"
        assert manifest["engineering"]["numerical_converged"] is True
        assert manifest["engineering"]["engineering_feasible"] is True
        unified_report = (result.output_dir / "design_report_unified.md").read_text(
            encoding="utf-8"
        )
        assert "有界自动修复记录" in unified_report

    assert events[0].stage is DesignRunStage.PREPARING
    assert events[-1].stage is DesignRunStage.COMPLETED
    assert [event.progress for event in events] == sorted(event.progress for event in events)


def test_runner_maps_converged_cli_exit_two_to_engineering_infeasible() -> None:
    request_payload = _medium_uav_request().to_dict()
    request_payload["project_name"] = "Aspect ratio gate"
    request_payload["initial_guess"]["aspect_ratio"] = 15.0
    request = AircraftDesignRequest.from_dict(request_payload)

    with tempfile.TemporaryDirectory() as temp_dir:
        runner = AircraftDesignRunner(PROJECT_ROOT, generated_root=Path(temp_dir))
        result = runner.run(
            request,
            timeout_seconds=30.0,
            run_id="infeasible-exit-two",
        )

    assert result.status is DesignRunStatus.ENGINEERING_INFEASIBLE
    assert result.exit_code == 2
    assert result.converged is True
    assert result.engineering is not None
    assert result.engineering.engineering_feasible is False
    assert "advanced.geometry.aspect_ratio_limit" in {
        constraint["id"]
        for constraint in result.engineering.constraints
        if constraint.get("blocking") is True and constraint.get("passed") is False
    }


def test_repair_policy_changes_design_variables_only_and_honors_user_ar_limit() -> None:
    payload = _medium_uav_request().to_dict()
    payload["auto_repair_enabled"] = True
    payload["provenance"] = {"user_requirements": {"max_aspect_ratio": 10.2}}
    request = AircraftDesignRequest.from_dict(payload)
    engineering = AircraftDesignEngineeringResult(
        numerical_converged=True,
        engineering_feasible=False,
        overall_status="infeasible",
        constraints=[
            {
                "id": "class1.range",
                "blocking": True,
                "passed": False,
                "required": 1_200_000.0,
                "actual": 1_000_000.0,
                "margin": -200_000.0,
            },
            {
                "id": "advanced.stability.static_margin_min",
                "blocking": True,
                "passed": False,
                "required": 0.05,
                "actual": -0.03,
                "margin": -0.08,
            },
        ],
    )

    proposal = propose_aircraft_design_repair(
        request,
        engineering,
        {},
        repair_attempt=1,
    )

    assert proposal is not None
    assert proposal.request.requirements == request.requirements
    assert proposal.record["requirements_changed"] is False
    assert proposal.request.initial_guess.aspect_ratio <= 10.2
    assert proposal.request.initial_guess.cd0 < request.initial_guess.cd0
    assert (
        proposal.request.initial_guess.cg_fraction_cbar
        < request.initial_guess.cg_fraction_cbar
    )
    assert (
        proposal.request.initial_guess.horizontal_tail_volume_coefficient
        > request.initial_guess.horizontal_tail_volume_coefficient
    )
    assert all(action["path"].startswith(("initial_guess.", "solver.")) for action in proposal.record["actions"])


def test_declared_supplemental_requirements_fail_closed_when_unmodeled() -> None:
    payload = _medium_uav_request().to_dict()
    payload["provenance"] = {
        "user_requirements": {
            "max_mtow_kg": 260.0,
            "min_cruise_endurance_s": 3_600.0,
            "launch_mode": "rocket_assist",
        }
    }
    request = AircraftDesignRequest.from_dict(payload)
    design_data = {
        "engineering_feasible": True,
        "constraints": [],
        "stage_status": {},
        "outputs": {"engineering_feasible": True, "mtow_kg": 900.0},
        "advanced_results": {
            "stage4_mission": {
                "segment_breakdown": [
                    {"name": "cruise", "details": {"time_s": 2_500.0}}
                ]
            }
        },
    }

    AircraftDesignRunner._apply_declared_user_requirements(design_data, request)

    assert design_data["engineering_feasible"] is False
    failed = {
        item["id"]
        for item in design_data["constraints"]
        if item["blocking"] and not item["passed"]
    }
    assert failed == {
        "declared.max_mtow_kg",
        "declared.min_cruise_endurance_s",
        "declared.special_mission_model_coverage",
    }
    assert design_data["stage_status"]["declared_requirements"]["status"] == "failed"


def test_runner_auto_repairs_static_margin_and_revalidates_complete_workflow() -> None:
    payload = _medium_uav_request().to_dict()
    payload.update(
        {
            "project_name": "auto_repair_static_margin",
            "auto_repair_enabled": True,
            "max_repair_attempts": 2,
        }
    )
    payload["initial_guess"]["cg_fraction_cbar"] = 0.55
    payload["initial_guess"]["horizontal_tail_volume_coefficient"] = 0.10
    request = AircraftDesignRequest.from_dict(payload)

    with tempfile.TemporaryDirectory() as temp_dir:
        runner = AircraftDesignRunner(PROJECT_ROOT, generated_root=Path(temp_dir))
        result = runner.run(
            request,
            timeout_seconds=60.0,
            run_id="auto-repair-static-margin",
        )

        assert result.status is DesignRunStatus.COMPLETED
        assert result.exit_code == 0
        assert result.engineering is not None
        assert result.engineering.engineering_feasible is True
        repair = result.design_data["auto_repair"]
        assert repair["attempts_executed"] >= 1
        assert repair["succeeded_after_repair"] is True
        assert repair["requirements_changed"] is False
        paths = {
            action["path"]
            for record in repair["history"]
            for action in record["actions"]
        }
        assert "initial_guess.cg_fraction_cbar" in paths
        assert len(list(result.task_dir.glob("attempt-*"))) >= 2
        report = (result.output_dir / "design_report_unified.md").read_text(encoding="utf-8")
        assert "有界自动修正审计" in report


def test_validator_rejects_nonconverged_and_mismatched_result() -> None:
    request = _medium_uav_request()
    with tempfile.TemporaryDirectory() as temp_dir:
        output_dir = Path(temp_dir)
        (output_dir / "design_report.md").write_text("report", encoding="utf-8")
        (output_dir / "design_report_v2.md").write_text("report", encoding="utf-8")
        (output_dir / "design_data.json").write_text(
            json.dumps(
                {
                    "inputs": {"requirements": {**request.requirements.to_dict(), "range_m": 42.0}},
                    "outputs": {
                        "converged": False,
                        "mtow_kg": 1_000.0,
                        "empty_weight_kg": 500.0,
                        "wing_area_m2": 20.0,
                        "thrust_sl_n": 5_000.0,
                    },
                }
            ),
            encoding="utf-8",
        )
        runner = AircraftDesignRunner(PROJECT_ROOT, generated_root=output_dir / "generated")
        issues, _, _, converged = runner.validate_output(request=request, output_dir=output_dir, exit_code=0)

    assert converged is False
    assert {issue.code for issue in issues} >= {"input_mismatch", "not_converged"}
