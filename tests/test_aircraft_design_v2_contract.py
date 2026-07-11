"""Acceptance tests for the aircraft design-data v2 engineering contract."""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

import pytest

from src.design_execution import (
    AircraftDesignRequest,
    AircraftDesignRunResult,
    AircraftDesignRunner,
    DesignRunStatus,
    extract_engineering_result,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
UPSTREAM_ROOT = PROJECT_ROOT / "external" / "aircraft-design-skill"
if str(UPSTREAM_ROOT) not in sys.path:
    sys.path.insert(0, str(UPSTREAM_ROOT))

from aircraft_design.class2_preliminary.constraints import normalized_constraint  # noqa: E402
from aircraft_design.class2_preliminary.fixed_wing_overall import (  # noqa: E402
    run_fixed_wing_overall_design,
)


def _medium_uav_request(*, max_iterations: int = 50) -> AircraftDesignRequest:
    return AircraftDesignRequest.from_dict(
        {
            "project_name": "contract_medium_uav",
            "requirements": {
                "range_m": 1_200_000.0,
                "payload_kg": 500.0,
                "cruise_mach": 0.22,
                "cruise_altitude_m": 6_000.0,
                "service_ceiling_m": 8_000.0,
            },
            "max_iterations": max_iterations,
        }
    )


@pytest.mark.parametrize(
    "direction,required,actual,expected_margin,expected_passed",
    [
        ("minimum", 10.0, 12.0, 2.0, True),
        ("minimum", 10.0, 8.0, -2.0, False),
        ("maximum", 10.0, 8.0, 2.0, True),
        ("maximum", 10.0, 12.0, -2.0, False),
    ],
)
def test_normalized_constraint_uses_positive_pass_margin(
    direction: str,
    required: float,
    actual: float,
    expected_margin: float,
    expected_passed: bool,
) -> None:
    constraint = normalized_constraint(
        constraint_id="acceptance.margin",
        label="Margin convention",
        category="acceptance",
        direction=direction,
        required=required,
        actual=actual,
        unit="unit",
    )

    assert constraint["margin"] == pytest.approx(expected_margin)
    assert constraint["margin_ratio"] == pytest.approx(expected_margin / required)
    assert constraint["passed"] is expected_passed


def test_constraint_tolerance_round_trips_through_engineering_extraction() -> None:
    constraint = normalized_constraint(
        constraint_id="acceptance.tolerance",
        label="Tolerance round trip",
        category="acceptance",
        direction="minimum",
        required=10.0,
        actual=9.75,
        unit="unit",
        tolerance=0.5,
    )
    data = {
        "schema_id": "aircraft-design/design-data",
        "schema_version": 2,
        "numerical_converged": True,
        "engineering_feasible": True,
        "constraints": [constraint],
        "stage_status": {
            "class1_sizing": {
                "status": "completed",
                "blocking": True,
                "message": "Synthetic tolerance fixture",
            }
        },
        "outputs": {"converged": True},
    }

    engineering = extract_engineering_result(data)

    assert constraint["margin"] == pytest.approx(-0.25)
    assert constraint["tolerance"] == pytest.approx(0.5)
    assert constraint["passed"] is True
    assert engineering.constraints[0]["tolerance"] == pytest.approx(0.5)
    assert engineering.constraints[0]["passed"] is True
    assert engineering.engineering_feasible is True


def test_fixed_wing_overall_emits_consumer_compatible_v2_constraints() -> None:
    result = run_fixed_wing_overall_design(
        {
            "mission": {
                "range_m": 1_000_000.0,
                "cruise_altitude_m": 10_000.0,
                "cruise_speed_m_s": 250.0,
                "v_stall_m_s": 50.0,
            },
            "payload": {"payload_kg": 500.0},
            "crew": {"crew_kg": 80.0},
            "aero": {"e": 0.8, "cl_max": 1.5},
            "sizing": {
                "wing_loading_pa": 3_000.0,
                "aspect_ratio": 8.0,
                "thrust_to_weight": 0.4,
            },
            "weights": {"empty_a": 0.9, "empty_b": -0.05},
            "propulsion": {"type": "prop"},
        }
    )

    engineering = extract_engineering_result(result)

    assert isinstance(result["constraints"], list)
    assert result["constraints"]
    assert isinstance(result["constraint_analysis"], dict)
    assert result["constraint_analysis"]["normalized"] == result["constraints"]
    assert len(engineering.constraints) == len(result["constraints"])
    assert engineering.engineering_feasible is result["engineering_feasible"]


def test_runner_preserves_request_input_provenance(tmp_path: Path) -> None:
    request = _medium_uav_request(max_iterations=1)
    runner = AircraftDesignRunner(PROJECT_ROOT, generated_root=tmp_path / "runs")

    result = runner.run(
        request,
        timeout_seconds=30.0,
        run_id="provenance-round-trip",
    )

    request_fields = request.provenance["input_fields"]
    result_fields = result.design_data["provenance"]["input_fields"]
    assert request_fields["requirements"]["cruise_mach"]["source"] == "user"
    assert request_fields["requirements"]["takeoff_distance_m"]["source"] == "default"
    assert request_fields["initial_guess"]["aspect_ratio"]["source"] == "derived"
    assert result_fields["requirements"]["cruise_mach"]["source"] == "user"
    assert result_fields["requirements"]["takeoff_distance_m"]["source"] == "default"
    assert result_fields["initial_guess"]["aspect_ratio"]["source"] == "derived"


@pytest.mark.parametrize(
    "required,actual",
    [
        (100.0, None),
        (100.0, float("nan")),
        (100.0, float("inf")),
        (None, 110.0),
        (float("nan"), 110.0),
    ],
)
def test_missing_nonfinite_or_unknown_constraint_evidence_fails_closed(
    required: float | None,
    actual: float | None,
) -> None:
    data = {
        "schema_id": "aircraft-design/design-data",
        "schema_version": 2,
        "numerical_converged": True,
        "engineering_feasible": True,
        "constraints": [
            {
                "id": "unknown.evidence",
                "label": "Unknown evidence",
                "category": "acceptance",
                "direction": "minimum",
                "required": required,
                "actual": actual,
                "unit": "unit",
                "margin": 999.0,
                "passed": True,
                "blocking": True,
                "evidence": {},
            }
        ],
        "stage_status": {
            "class1_sizing": {
                "status": "completed",
                "blocking": True,
                "message": "Synthetic contract fixture",
            }
        },
        "outputs": {"converged": True},
    }

    engineering = extract_engineering_result(data)

    assert engineering.constraints[0]["margin"] is None
    assert engineering.constraints[0]["passed"] is False
    assert engineering.engineering_feasible is False
    assert engineering.overall_status == "infeasible"


def test_blocking_advanced_stage_failure_cannot_be_completed(tmp_path: Path) -> None:
    request = _medium_uav_request()
    passing_constraint = normalized_constraint(
        constraint_id="class1.range",
        label="Range",
        category="mission",
        direction="minimum",
        required=1_200_000.0,
        actual=1_250_000.0,
        unit="m",
    )
    data = {
        "schema_id": "aircraft-design/design-data",
        "schema_version": 2,
        "numerical_converged": True,
        "engineering_feasible": True,
        "constraints": [passing_constraint],
        "stage_status": {
            "class1_sizing": {
                "status": "completed",
                "blocking": True,
                "message": "Class I converged",
            },
            "stage3_propulsion": {
                "status": "failed",
                "blocking": True,
                "message": "Installed thrust model failed",
                "error": "invalid engine deck",
            },
        },
        "outputs": {"converged": True},
    }
    engineering = extract_engineering_result(data, request=request)
    runner = AircraftDesignRunner(PROJECT_ROOT, generated_root=tmp_path / "runs")

    status = runner._status_from_validation(  # noqa: SLF001 - acceptance of terminal mapping
        0,
        True,
        [],
        engineering=engineering,
    )

    assert engineering.numerical_converged is True
    assert engineering.engineering_feasible is False
    assert status is DesignRunStatus.ENGINEERING_INFEASIBLE
    assert status is not DesignRunStatus.COMPLETED


def test_latest_legacy_advanced_output_migrates_false_positive_status(tmp_path: Path) -> None:
    request = _medium_uav_request()
    task_dir = tmp_path / "legacy-run"
    output_dir = task_dir / "output"
    output_dir.mkdir(parents=True)
    input_path = task_dir / "sizing_input.json"
    input_path.write_text("{}", encoding="utf-8")
    design_data = {
        "inputs": {"requirements": request.requirements.to_dict()},
        "outputs": {
            "converged": True,
            "mtow_kg": 2_450.0,
            "empty_weight_kg": 1_250.0,
            "fuel_weight_kg": 680.0,
            "wing_area_m2": 8.0,
            "thrust_sl_n": 14_000.0,
        },
    }
    (output_dir / "design_data.json").write_text(json.dumps(design_data), encoding="utf-8")
    older = output_dir / "advanced_design_results_older.json"
    latest = output_dir / "advanced_design_results_latest.json"
    older.write_text(
        json.dumps({"stage3_propulsion": {"thrust_margin_climb": 0.25}}),
        encoding="utf-8",
    )
    latest.write_text(
        json.dumps({"stage3_propulsion": {"thrust_margin_climb": -0.35}}),
        encoding="utf-8",
    )
    os.utime(older, ns=(1_000_000_000, 1_000_000_000))
    os.utime(latest, ns=(2_000_000_000, 2_000_000_000))

    restored = AircraftDesignRunResult.from_dict(
        {
            "run_id": "legacy-run",
            "status": "completed",
            "task_dir": str(task_dir),
            "input_path": str(input_path),
            "output_dir": str(output_dir),
            "command": [],
            "exit_code": 0,
            "stdout": "",
            "stderr": "",
            "started_at": "2026-07-11T10:00:00",
            "finished_at": "2026-07-11T10:00:01",
            "duration_seconds": 1.0,
            "converged": True,
            "artifacts": [],
            "issues": [],
            "engineering": {
                "numerical_converged": True,
                "engineering_feasible": True,
                "overall_status": "feasible",
            },
        },
        request=request,
        allowed_root=tmp_path,
    )

    assert restored.status is DesignRunStatus.ENGINEERING_INFEASIBLE
    assert restored.engineering is not None
    assert restored.engineering.engineering_feasible is False
    climb = next(
        item
        for item in restored.engineering.constraints
        if item["id"] == "thrust_margin_climb"
    )
    assert climb["actual"] == pytest.approx(-0.35)
    assert climb["margin"] == pytest.approx(-0.35)
    assert climb["passed"] is False


def test_nonconverged_run_retains_last_estimate_and_diagnostics(tmp_path: Path) -> None:
    runner = AircraftDesignRunner(PROJECT_ROOT, generated_root=tmp_path / "runs")

    result = runner.run(
        _medium_uav_request(max_iterations=1),
        timeout_seconds=30.0,
        run_id="nonconverged-contract",
    )

    assert result.status is DesignRunStatus.NONCONVERGED
    assert result.converged is False
    assert result.output_dir is not None
    assert result.engineering is not None
    assert result.engineering.numerical_converged is False
    assert result.engineering.overall_status == "nonconverged"
    assert result.engineering.iteration_history
    assert result.engineering.design_point["wing_loading_pa"] > 0.0
    assert result.engineering.recommendations
    assert any("iteration" in recommendation.lower() for recommendation in result.engineering.recommendations)
    outputs = result.design_data["outputs"]
    for field in ("mtow_kg", "empty_weight_kg", "fuel_weight_kg", "wing_area_m2", "thrust_sl_n"):
        assert outputs[field] > 0.0
    assert result.design_data["status"]["task_status"] == "not_converged"
    assert "last valid Class I estimate" in result.design_data["status"]["summary"]
    assert (result.output_dir / "design_data.json").is_file()
    assert (result.output_dir / "design_report_v2.md").is_file()
