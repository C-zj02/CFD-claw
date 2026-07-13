"""Engineering envelopes, monotonicity, determinism, and OAT regressions."""

from __future__ import annotations

import contextlib
import copy
import io
import json
import sys
from dataclasses import asdict
from pathlib import Path

import pytest

from src.design_execution import (
    AircraftDesignRequest,
    AircraftDesignRunner,
    DesignRunStatus,
)


PROJECT_ROOT = Path(__file__).resolve().parents[1]
UPSTREAM_ROOT = PROJECT_ROOT / "external" / "aircraft-design-skill"
BENCHMARK_ROOT = PROJECT_ROOT / "benchmarks" / "aircraft_design_v2"
if str(UPSTREAM_ROOT) not in sys.path:
    sys.path.insert(0, str(UPSTREAM_ROOT))

from aircraft_design.class2_preliminary.advanced_design import (  # noqa: E402
    execute_stage7_optimization,
)
from aircraft_design.class2_preliminary.design_loop_orchestrator import (  # noqa: E402
    DesignRequirements,
    InitialGuess,
    sizing_loop,
)


CASE_PATHS = sorted((BENCHMARK_ROOT / "cases").glob("*.json"))


def _load_case(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _run_class1(request_payload: dict):
    request = AircraftDesignRequest.from_dict(request_payload)
    requirements = DesignRequirements(**request.requirements.to_dict())
    guess = InitialGuess(**request.initial_guess.to_dict())
    with contextlib.redirect_stdout(io.StringIO()):
        result = sizing_loop(
            requirements,
            guess,
            enable_visualization=False,
            tolerance=request.tolerance,
            max_iter=request.max_iterations,
        )
    return request, result


def _metric(result, name: str) -> float:
    if name == "empty_fraction":
        return result.empty_weight_kg / result.mtow_kg
    if name == "fuel_fraction":
        return result.fuel_weight_kg / result.mtow_kg
    return float(getattr(result, name))


@pytest.mark.parametrize("case_path", CASE_PATHS, ids=lambda path: path.stem)
def test_aircraft_class1_cases_stay_inside_engineering_acceptance_envelopes(
    case_path: Path,
) -> None:
    case = _load_case(case_path)
    request, result = _run_class1(case["request"])

    assert result.numerical_converged is True
    assert result.engineering_feasible is True
    assert result.iteration_history
    assert all(item.get("passed") is True for item in result.constraints if item.get("blocking"))
    for metric_name, envelope in case["acceptance"].items():
        if metric_name == "weight_closure_relative_error_max":
            continue
        value = _metric(result, metric_name)
        assert envelope["minimum"] <= value <= envelope["maximum"], (
            f"{case['case_id']} {metric_name}={value} outside {envelope}"
        )

    summed_weight = result.empty_weight_kg + result.fuel_weight_kg + request.requirements.payload_kg
    closure_error = abs(result.mtow_kg - summed_weight) / result.mtow_kg
    assert closure_error <= case["acceptance"]["weight_closure_relative_error_max"]
    assert result.actual_range_m == pytest.approx(request.requirements.range_m, rel=1e-8)
    assert result.takeoff_distance_m <= request.requirements.takeoff_distance_m
    assert result.landing_distance_m <= request.requirements.landing_distance_m
    assert result.wing_area_m2 > 0.0
    assert result.thrust_sl_n > 0.0


@pytest.mark.parametrize("case_path", CASE_PATHS, ids=lambda path: path.stem)
def test_aircraft_cases_pass_complete_class2_delivery_gates(
    case_path: Path,
    tmp_path: Path,
) -> None:
    case = _load_case(case_path)
    request = AircraftDesignRequest.from_dict(case["request"])
    runner = AircraftDesignRunner(
        PROJECT_ROOT,
        generated_root=tmp_path / case["case_id"],
    )

    result = runner.run(
        request,
        timeout_seconds=30.0,
        run_id=f"benchmark-{case['case_id']}",
    )

    assert result.status is DesignRunStatus.COMPLETED
    assert result.exit_code == 0
    assert result.engineering is not None
    assert result.engineering.engineering_feasible is True
    assert result.engineering.blocking_failed_count == 0
    assert all(
        stage.get("status") == "completed"
        for stage in result.engineering.stage_status.values()
        if stage.get("blocking") is True
    )

    if case["case_id"] in {"business_jet", "medium_uav"}:
        adjustments = result.design_data.get("design_adjustments", [])
        assert adjustments
        assert adjustments[0]["failed_check_id"] == "advanced.geometry.fuel_volume"
        report = (result.output_dir / "design_report_unified.md").read_text(encoding="utf-8")
        assert "有界自动修复记录" in report
        assert any(action["parameter"] in report for action in adjustments[0]["actions"])

    fuel_volume = next(
        constraint
        for constraint in result.engineering.constraints
        if constraint["id"] == "advanced.geometry.fuel_volume"
    )
    volume = fuel_volume["evidence"]["volume_breakdown"]
    assert volume["total_m3"] == pytest.approx(
        volume["wing_m3"] + volume["fuselage_or_center_tank_m3"]
    )
    assert volume["aircraft_role"] == request.requirements.aircraft_role


@pytest.mark.parametrize("case_path", CASE_PATHS, ids=lambda path: path.stem)
def test_aircraft_case_monotonic_check_changes_one_input_only(case_path: Path) -> None:
    case = _load_case(case_path)
    baseline_payload = copy.deepcopy(case["request"])
    varied_payload = copy.deepcopy(baseline_payload)
    check = case["monotonic_check"]
    group, field = check["input_path"].split(".", 1)
    varied_payload[group][field] *= check["factor"]

    changed_paths = []
    for group_name in ("requirements", "initial_guess"):
        for field_name, baseline_value in baseline_payload[group_name].items():
            if varied_payload[group_name][field_name] != baseline_value:
                changed_paths.append(f"{group_name}.{field_name}")
    assert changed_paths == [check["input_path"]]

    _, baseline = _run_class1(baseline_payload)
    _, varied = _run_class1(varied_payload)
    baseline_value = _metric(baseline, check["output"])
    varied_value = _metric(varied, check["output"])

    assert baseline.numerical_converged is True
    assert varied.numerical_converged is True
    if check["direction"] == "increase":
        assert varied_value > baseline_value
    else:
        assert varied_value < baseline_value


def test_seeded_exploration_is_repeatable_and_sensitivity_is_strictly_oat() -> None:
    variables = {
        "wing_loading_pa": (1_500.0, 3_500.0),
        "thrust_to_weight": (0.25, 0.65),
        "aspect_ratio": (7.0, 12.0),
        "cd0": (0.018, 0.04),
        "sfc_cruise_1_s": (0.00012, 0.0003),
        "payload_kg": (350.0, 650.0),
        "range_m": (800_000.0, 1_500_000.0),
    }
    baseline = {name: (bounds[0] + bounds[1]) / 2.0 for name, bounds in variables.items()}

    def evaluate(point: dict[str, float]) -> dict:
        drag_penalty = point["cd0"] * point["wing_loading_pa"] / point["aspect_ratio"]
        mission_penalty = point["sfc_cruise_1_s"] * point["range_m"]
        mtow = point["payload_kg"] * 3.2 + drag_penalty + mission_penalty
        return {
            "mtow_kg": mtow,
            "variables": dict(point),
            "feasible": point["thrust_to_weight"] >= 0.3,
        }

    kwargs = {
        "design_variables": variables,
        "constraints": {
            "positive_payload": lambda point: point["payload_kg"] > 0.0,
            "usable_aspect_ratio": lambda point: point["aspect_ratio"] >= 7.0,
        },
        "objective": "mtow_kg",
        "objective_direction": "minimize",
        "n_iterations": 40,
        "seed": 20260711,
        "baseline_design": baseline,
        "evaluation_func": evaluate,
    }

    first = execute_stage7_optimization(**kwargs)
    repeated = execute_stage7_optimization(**kwargs)
    different_seed = execute_stage7_optimization(**{**kwargs, "seed": 20260712})

    assert asdict(first) == asdict(repeated)
    assert first.exploration_seed == 20260711
    assert first.sensitivity_method == "one_at_a_time"
    assert first.feasible_designs != different_seed.feasible_designs
    sensitivity = first.sensitivity_analysis
    assert sensitivity["_baseline"]["design_point"] == baseline

    for variable_name in variables:
        analysis = sensitivity[variable_name]
        assert analysis["method"] == "one_at_a_time"
        assert [case["case"] for case in analysis["cases"]] == ["low", "baseline", "high"]
        for case in analysis["cases"]:
            evaluated = case["metrics"]["variables"]
            changed = [
                name
                for name, baseline_value in baseline.items()
                if evaluated[name] != baseline_value
            ]
            if case["case"] == "baseline":
                assert changed == []
                assert case["delta"] == 0.0
            else:
                assert changed == [variable_name]
