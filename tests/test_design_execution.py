"""Tests for deterministic aircraft design execution."""

from __future__ import annotations

import json
import tempfile
from pathlib import Path

import pytest

from src.design_execution import (
    AircraftDesignRequest,
    AircraftDesignRunner,
    DesignRunStage,
    DesignRunStatus,
)


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


def test_runner_separates_convergence_from_medium_uav_engineering_feasibility() -> None:
    events = []
    with tempfile.TemporaryDirectory() as temp_dir:
        runner = AircraftDesignRunner(PROJECT_ROOT, generated_root=Path(temp_dir))
        result = runner.run(
            _medium_uav_request(),
            timeout_seconds=30.0,
            on_progress=events.append,
            run_id="integration-run",
        )

        assert result.status is DesignRunStatus.ENGINEERING_INFEASIBLE
        assert not result.succeeded
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
        assert result.design_data["engineering_feasible"] is False
        assert isinstance(result.design_data["constraints"], list)
        assert result.design_data["constraints"]
        assert isinstance(result.design_data["stage_status"], dict)
        assert isinstance(result.design_data["provenance"], dict)
        assert isinstance(result.design_data["iteration_history"], list)
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
        assert result.engineering.engineering_feasible is False
        assert result.engineering.blocking_failed_count > 0
        assert {issue.code for issue in result.issues} >= {
            "blocking_constraint_failed",
            "engineering_infeasible",
        }
        summary = result.to_dict()["summary"]
        assert summary["wing_loading_pa"] > 0
        assert summary["thrust_to_weight"] > 0
        assert summary["span_m"] > 0
        assert summary["iterations"] > 0
        assert summary["artifact_count"] > 0
        manifest = json.loads((result.task_dir / "run_result.json").read_text(encoding="utf-8"))
        assert manifest["status"] == "engineering_infeasible"
        assert manifest["engineering"]["numerical_converged"] is True
        assert manifest["engineering"]["engineering_feasible"] is False

    assert events[0].stage is DesignRunStage.PREPARING
    assert events[-1].stage is DesignRunStage.ENGINEERING_INFEASIBLE
    assert [event.progress for event in events] == sorted(event.progress for event in events)


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
