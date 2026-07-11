"""Deterministic subprocess runner for the integrated aircraft design skill."""

from __future__ import annotations

import json
import math
import os
import signal
import subprocess
import sys
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any, Callable
from uuid import uuid4

from src.design_execution.models import (
    AircraftDesignEngineeringResult,
    AircraftDesignRequest,
    DesignRunEvent,
    DesignRunStage,
    DesignRunStatus,
    DesignValidationIssue,
)


ProgressCallback = Callable[[DesignRunEvent], None]
RESULT_EXTENSIONS = {
    ".csv",
    ".docx",
    ".glb",
    ".gltf",
    ".html",
    ".json",
    ".log",
    ".md",
    ".obj",
    ".pdf",
    ".png",
    ".stl",
    ".svg",
    ".txt",
    ".vsp3",
    ".vspscript",
    ".xlsx",
}


def _as_dict(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _finite_number(value: Any) -> float | None:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        return None
    parsed = float(value)
    return parsed if math.isfinite(parsed) else None


def _bool_or_none(value: Any) -> bool | None:
    return value if isinstance(value, bool) else None


def _first_bool(*values: Any) -> bool | None:
    for value in values:
        parsed = _bool_or_none(value)
        if parsed is not None:
            return parsed
    return None


def _schema_major(design_data: dict[str, Any] | None) -> int | None:
    if not isinstance(design_data, dict):
        return None
    value = design_data.get("schema_version")
    if isinstance(value, bool):
        return None
    if isinstance(value, int):
        return value
    if isinstance(value, float) and math.isfinite(value):
        return int(value)
    if isinstance(value, str):
        try:
            return int(value.strip().split(".", 1)[0])
        except ValueError:
            return None
    return None


def _is_v2_schema(design_data: dict[str, Any] | None) -> bool:
    major = _schema_major(design_data)
    return major is not None and major >= 2


def _infer_direction(
    raw: dict[str, Any],
    actual: float | None,
    required: float | None,
    margin: float | None,
) -> str:
    direction = str(raw.get("direction") or "").strip().lower()
    aliases = {
        "min": "minimum",
        "minimum": "minimum",
        ">=": "minimum",
        "max": "maximum",
        "maximum": "maximum",
        "<=": "maximum",
    }
    if direction in aliases:
        return aliases[direction]
    description = f"{raw.get('description', '')} {raw.get('label', raw.get('name', ''))}"
    if "<=" in description or "maximum" in description.lower() or " limit" in description.lower():
        return "maximum"
    if ">=" in description or "minimum" in description.lower():
        return "minimum"
    if actual is not None and required is not None and margin is not None:
        if math.isclose(margin, required - actual, rel_tol=1e-7, abs_tol=1e-9):
            return "maximum"
    return "minimum"


def _normalize_constraint(
    value: Any,
    index: int,
    *,
    default_category: str = "engineering",
    default_blocking: bool = True,
) -> dict[str, Any] | None:
    if not isinstance(value, dict):
        return None
    raw = value
    actual = _finite_number(raw.get("actual", raw.get("actual_value")))
    required = _finite_number(
        raw.get("required", raw.get("limit_value", raw.get("requirement")))
    )
    supplied_margin = _finite_number(raw.get("margin"))
    direction = _infer_direction(raw, actual, required, supplied_margin)
    if actual is not None and required is not None:
        margin = actual - required if direction == "minimum" else required - actual
    else:
        # A standalone margin cannot prove a constraint when its operands are
        # missing or non-finite. Keep the evidence unknown and fail closed.
        margin = None
    margin_ratio = _finite_number(raw.get("margin_ratio"))
    if margin is not None and required not in (None, 0.0):
        margin_ratio = margin / abs(required)
    elif margin is None:
        margin_ratio = None
    raw_tolerance = _finite_number(raw.get("tolerance"))
    tolerance = abs(raw_tolerance) if raw_tolerance is not None else 0.0
    passed = margin >= -tolerance if margin is not None else False
    blocking = raw.get("blocking", default_blocking)
    if not isinstance(blocking, bool):
        blocking = default_blocking
    severity = str(raw.get("severity") or ("error" if blocking else "warning")).lower()
    if severity not in {"info", "warning", "error"}:
        severity = "error" if blocking else "warning"
    label = str(raw.get("label") or raw.get("name") or raw.get("id") or f"Constraint {index + 1}")
    constraint_id = str(raw.get("id") or label.lower().replace(" ", "_"))
    evidence = raw.get("evidence") if isinstance(raw.get("evidence"), dict) else {}
    if not evidence:
        evidence = {
            "model": str(raw.get("source") or "legacy_output"),
            "prediction": True,
        }
    recommendation = raw.get("recommendation")
    return {
        "id": constraint_id,
        "label": label,
        "category": str(raw.get("category") or default_category),
        "direction": direction,
        "required": required,
        "actual": actual,
        "unit": str(raw.get("unit") or ""),
        "margin": margin,
        "margin_ratio": margin_ratio,
        "tolerance": tolerance,
        "passed": passed,
        "severity": severity,
        "blocking": blocking,
        "evidence": dict(evidence),
        "recommendation": str(recommendation) if recommendation not in (None, "") else None,
    }


def _constraint(
    constraint_id: str,
    label: str,
    category: str,
    direction: str,
    required: float,
    actual: float,
    unit: str,
    recommendation: str,
    model: str,
) -> dict[str, Any]:
    raw = {
        "id": constraint_id,
        "label": label,
        "category": category,
        "direction": direction,
        "required": required,
        "actual": actual,
        "unit": unit,
        "blocking": True,
        "severity": "error",
        "evidence": {"model": model, "prediction": True},
        "recommendation": recommendation,
    }
    normalized = _normalize_constraint(raw, 0)
    assert normalized is not None
    return normalized


def _load_advanced_results(output_dir: Path | None) -> dict[str, Any]:
    if output_dir is None or not output_dir.is_dir():
        return {}
    candidates = list(output_dir.glob("advanced_design_results*.json"))
    candidates.sort(key=lambda path: path.stat().st_mtime_ns, reverse=True)
    for path in candidates:
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            continue
        if isinstance(value, dict):
            return value
    unified_path = output_dir / "design_report_unified.json"
    try:
        unified = json.loads(unified_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}
    return _as_dict(unified.get("advanced_results"))


def _legacy_constraints(
    advanced: dict[str, Any],
    outputs: dict[str, Any],
) -> list[dict[str, Any]]:
    constraints: list[dict[str, Any]] = []
    geometry_constraints = advanced.get("geometry_constraints")
    if isinstance(geometry_constraints, list):
        for raw in geometry_constraints:
            constraint = _normalize_constraint(
                raw,
                len(constraints),
                default_category="geometry",
            )
            if constraint is not None:
                constraint["evidence"] = {
                    "model": "advanced_design.geometry_constraints",
                    "prediction": True,
                }
                if constraint["passed"] is False and "fuel" in constraint["label"].lower():
                    constraint["recommendation"] = (
                        "Increase usable fuel volume or reduce mission fuel demand, then repeat sizing."
                    )
                constraints.append(constraint)

    propulsion = _as_dict(advanced.get("stage3_propulsion"))
    for key, label in (
        ("thrust_margin_cruise", "Cruise thrust margin"),
        ("thrust_margin_climb", "Climb thrust margin"),
    ):
        value = _finite_number(propulsion.get(key))
        if value is not None:
            constraints.append(
                _constraint(
                    key,
                    label,
                    "propulsion",
                    "minimum",
                    0.0,
                    value,
                    "ratio",
                    "Increase available thrust or reduce weight and drag until the margin is positive.",
                    f"advanced_design.stage3_propulsion.{key}",
                )
            )

    mission = _as_dict(advanced.get("stage4_mission"))
    mission_fuel_kg = _finite_number(mission.get("total_fuel_kg"))
    available_fuel_kg = _finite_number(outputs.get("fuel_weight_kg"))
    if mission_fuel_kg is not None and available_fuel_kg is not None:
        constraints.append(
            _constraint(
                "mission_fuel_capacity",
                "Mission fuel capacity",
                "mission",
                "maximum",
                available_fuel_kg,
                mission_fuel_kg,
                "kg",
                "Reduce mission fuel demand or increase usable fuel capacity and close the weight loop again.",
                "advanced_design.stage4_mission.total_fuel_kg",
            )
        )
    fuel_fraction = _finite_number(mission.get("total_fuel_fraction"))
    if fuel_fraction is not None:
        constraints.append(
            _constraint(
                "mission_fuel_fraction",
                "Mission fuel fraction",
                "mission",
                "maximum",
                1.0,
                fuel_fraction,
                "ratio",
                "Reduce range or fuel consumption and repeat the sizing closure.",
                "advanced_design.stage4_mission.total_fuel_fraction",
            )
        )

    stability = _as_dict(advanced.get("stage5_stability"))
    static_margin = _finite_number(stability.get("static_margin"))
    if static_margin is not None:
        constraints.append(
            _constraint(
                "static_margin",
                "Static stability margin",
                "stability",
                "minimum",
                0.0,
                static_margin,
                "c_bar",
                "Move the center of gravity forward or revise tail sizing to recover positive static margin.",
                "advanced_design.stage5_stability.static_margin",
            )
        )
    return constraints


def _normalized_stage_status(
    value: Any,
    *,
    numerical_converged: bool | None,
    advanced: dict[str, Any],
    constraints: list[dict[str, Any]],
) -> dict[str, dict[str, Any]]:
    stages: dict[str, dict[str, Any]] = {}
    if isinstance(value, dict):
        for stage_id, raw in value.items():
            if isinstance(raw, dict):
                status = str(raw.get("status") or "unknown")
                blocking = raw.get("blocking") is True
                item: dict[str, Any] = {
                    "status": status,
                    "blocking": blocking,
                    "message": str(raw.get("message") or ""),
                }
                if raw.get("error") not in (None, ""):
                    item["error"] = str(raw["error"])
                stages[str(stage_id)] = item
            else:
                stages[str(stage_id)] = {
                    "status": str(raw),
                    "blocking": False,
                    "message": "",
                }
        return stages

    stages["requirements"] = {
        "status": "completed",
        "blocking": True,
        "message": "Legacy input requirements were preserved.",
    }
    stages["class1_sizing"] = {
        "status": "completed" if numerical_converged is True else "not_converged",
        "blocking": True,
        "message": "Legacy Class I sizing result.",
    }
    for stage_id in (
        "stage2_aero",
        "stage3_propulsion",
        "stage4_mission",
        "stage5_stability",
        "stage6_structures",
        "stage7_optimization",
    ):
        if stage_id in advanced:
            stages[stage_id] = {
                "status": "completed",
                "blocking": stage_id != "stage7_optimization",
                "message": "Recovered from legacy advanced design output.",
            }
    category_to_stage = {
        "geometry": "geometry",
        "propulsion": "stage3_propulsion",
        "mission": "stage4_mission",
        "stability": "stage5_stability",
    }
    for constraint in constraints:
        if constraint.get("blocking") is not True or constraint.get("passed") is not False:
            continue
        stage_id = category_to_stage.get(str(constraint.get("category")))
        if stage_id is not None:
            stages[stage_id] = {
                "status": "failed",
                "blocking": True,
                "message": f"Blocking constraint failed: {constraint.get('label')}",
            }
    return stages


def extract_engineering_result(
    design_data: dict[str, Any] | None,
    *,
    output_dir: Path | None = None,
    request: AircraftDesignRequest | None = None,
    persisted: dict[str, Any] | None = None,
) -> AircraftDesignEngineeringResult:
    """Normalize schema-v2 evidence and recover useful evidence from legacy outputs."""

    data = design_data if isinstance(design_data, dict) else {}
    outputs = _as_dict(data.get("outputs"))
    status = _as_dict(data.get("status"))
    persisted_data = persisted if isinstance(persisted, dict) else {}
    numerical_converged = _first_bool(
        data.get("numerical_converged"),
        status.get("numerical_converged"),
        outputs.get("numerical_converged"),
        outputs.get("converged"),
        persisted_data.get("numerical_converged"),
    )

    advanced = _as_dict(data.get("advanced_results")) or _as_dict(outputs.get("advanced_results"))
    if not advanced:
        advanced = _load_advanced_results(output_dir)
    raw_constraints = data.get("constraints", outputs.get("constraints"))
    constraints: list[dict[str, Any]] = []
    if isinstance(raw_constraints, list):
        constraints = [
            normalized
            for index, item in enumerate(raw_constraints)
            if (normalized := _normalize_constraint(item, index)) is not None
        ]
    elif not _is_v2_schema(data):
        constraints = _legacy_constraints(advanced, outputs)
    if not constraints and isinstance(persisted_data.get("constraints"), list):
        constraints = [
            normalized
            for index, item in enumerate(persisted_data["constraints"])
            if (normalized := _normalize_constraint(item, index)) is not None
        ]

    stage_status = _normalized_stage_status(
        data.get("stage_status", persisted_data.get("stage_status")),
        numerical_converged=numerical_converged,
        advanced=advanced,
        constraints=constraints,
    )
    schema_v2 = _is_v2_schema(data)
    blocking_constraint_failed = any(
        item.get("blocking") is True and item.get("passed") is False for item in constraints
    )
    blocking_constraint_unproven = schema_v2 and any(
        item.get("blocking") is True and item.get("passed") is not True for item in constraints
    )
    blocking_stage_failed = any(
        item.get("blocking") is True
        and (
            item.get("status") in {"failed", "partial", "not_converged"}
            or (schema_v2 and item.get("status") != "completed")
        )
        for item in stage_status.values()
    )
    explicit_feasible = _first_bool(
        data.get("engineering_feasible"),
        status.get("engineering_feasible"),
        outputs.get("engineering_feasible"),
        persisted_data.get("engineering_feasible"),
    )
    blocking_constraints_passed = _bool_or_none(status.get("blocking_constraints_passed"))
    if (
        blocking_constraint_failed
        or blocking_constraint_unproven
        or blocking_stage_failed
        or blocking_constraints_passed is False
    ):
        engineering_feasible: bool | None = False
    elif explicit_feasible is not None:
        engineering_feasible = explicit_feasible
    elif _is_v2_schema(data):
        engineering_feasible = None
    elif constraints:
        engineering_feasible = all(item.get("passed") is True for item in constraints if item.get("blocking"))
    else:
        engineering_feasible = None

    if numerical_converged is False:
        overall_status = "nonconverged"
    elif engineering_feasible is False:
        overall_status = "infeasible"
    elif numerical_converged is True and engineering_feasible is True:
        overall_status = "feasible"
    else:
        overall_status = "unknown"

    provenance = data.get("provenance")
    if not isinstance(provenance, dict):
        provenance = persisted_data.get("provenance")
    if not isinstance(provenance, dict) and request is not None:
        provenance = request.provenance
    if not isinstance(provenance, dict):
        provenance = {}

    requirement_comparisons = data.get("requirement_comparisons")
    if not isinstance(requirement_comparisons, list):
        requirement_comparisons = persisted_data.get("requirement_comparisons")
    if not isinstance(requirement_comparisons, list):
        requirement_comparisons = [
            {
                key: item.get(key)
                for key in (
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
                )
            }
            for item in constraints
        ]
    else:
        requirement_comparisons = [dict(item) for item in requirement_comparisons if isinstance(item, dict)]

    iteration_history = data.get("iteration_history", outputs.get("iteration_history"))
    if not isinstance(iteration_history, list):
        iteration_history = persisted_data.get("iteration_history")
    if not isinstance(iteration_history, list):
        iteration_history = []
    iteration_history = [dict(item) for item in iteration_history if isinstance(item, dict)]

    design_point = data.get("design_point", outputs.get("design_point"))
    if not isinstance(design_point, dict):
        design_point = persisted_data.get("design_point")
    if not isinstance(design_point, dict):
        design_point = {}
    design_point = dict(design_point)
    mtow_kg = _finite_number(outputs.get("mtow_kg"))
    wing_area_m2 = _finite_number(outputs.get("wing_area_m2"))
    thrust_sl_n = _finite_number(outputs.get("thrust_sl_n"))
    if "wing_loading_pa" not in design_point and mtow_kg and wing_area_m2:
        design_point["wing_loading_pa"] = mtow_kg * 9.80665 / wing_area_m2
    if "thrust_to_weight" not in design_point and mtow_kg and thrust_sl_n:
        design_point["thrust_to_weight"] = thrust_sl_n / (mtow_kg * 9.80665)

    recommendations: list[str] = []
    raw_recommendations = data.get("recommendations", persisted_data.get("recommendations"))
    if isinstance(raw_recommendations, list):
        recommendations.extend(str(item) for item in raw_recommendations if item not in (None, ""))
    for constraint in constraints:
        recommendation = constraint.get("recommendation")
        if constraint.get("passed") is False and recommendation:
            recommendations.append(str(recommendation))
    optimization = _as_dict(advanced.get("stage7_optimization"))
    if engineering_feasible is not False and isinstance(optimization.get("recommendations"), list):
        recommendations.extend(
            str(item) for item in optimization["recommendations"] if item not in (None, "")
        )
    recommendations = list(dict.fromkeys(recommendations))

    return AircraftDesignEngineeringResult(
        numerical_converged=numerical_converged,
        engineering_feasible=engineering_feasible,
        overall_status=overall_status,
        constraints=constraints,
        stage_status=stage_status,
        provenance=dict(provenance),
        requirement_comparisons=requirement_comparisons,
        iteration_history=iteration_history,
        design_point=design_point,
        recommendations=recommendations,
    )


def _append_engineering_issues(
    issues: list[DesignValidationIssue],
    engineering: AircraftDesignEngineeringResult,
    *,
    schema_v2: bool,
) -> None:
    existing = {(issue.code, issue.message) for issue in issues}

    def append(code: str, message: str, severity: str = "error") -> None:
        if (code, message) not in existing:
            issues.append(DesignValidationIssue(code, message, severity=severity))
            existing.add((code, message))

    if engineering.numerical_converged is False:
        append("not_converged", "sizing loop did not converge")
    elif engineering.numerical_converged is None:
        append(
            "missing_numerical_convergence",
            "result does not declare whether the sizing loop converged",
        )
    if schema_v2 and engineering.engineering_feasible is None:
        append(
            "missing_engineering_feasibility",
            "schema v2 result must declare engineering_feasible",
        )
    for constraint in engineering.constraints:
        if constraint.get("blocking") is True and constraint.get("passed") is False:
            append(
                "blocking_constraint_failed",
                f"blocking constraint failed: {constraint.get('label') or constraint.get('id')}",
            )
        elif schema_v2 and constraint.get("blocking") is True and constraint.get("passed") is None:
            append(
                "blocking_constraint_unknown",
                f"blocking constraint has no pass/fail evidence: {constraint.get('label') or constraint.get('id')}",
            )
    for stage_id, stage in engineering.stage_status.items():
        if stage.get("blocking") is True and (
            stage.get("status") in {"failed", "partial", "not_converged"}
            or (schema_v2 and stage.get("status") != "completed")
        ):
            append(
                "blocking_stage_failed",
                f"blocking design stage did not pass: {stage_id} ({stage.get('status')})",
            )
    if engineering.engineering_feasible is False:
        append("engineering_infeasible", "design completed but is not engineering feasible")


@dataclass
class AircraftDesignRunResult:
    run_id: str
    status: DesignRunStatus
    request: AircraftDesignRequest
    task_dir: Path
    input_path: Path
    output_dir: Path | None
    command: list[str]
    exit_code: int | None
    stdout: str
    stderr: str
    started_at: str
    finished_at: str
    duration_seconds: float
    converged: bool | None = None
    design_data: dict[str, Any] | None = None
    artifacts: list[Path] = field(default_factory=list)
    issues: list[DesignValidationIssue] = field(default_factory=list)
    engineering: AircraftDesignEngineeringResult | None = None

    @property
    def succeeded(self) -> bool:
        return self.status is DesignRunStatus.COMPLETED

    def to_dict(self) -> dict[str, Any]:
        outputs = self.design_data.get("outputs", {}) if isinstance(self.design_data, dict) else {}
        performance = outputs.get("performance", {}) if isinstance(outputs, dict) else {}
        geometry = outputs.get("geometry", {}) if isinstance(outputs, dict) else {}
        mtow_kg = outputs.get("mtow_kg") if isinstance(outputs, dict) else None
        wing_area_m2 = outputs.get("wing_area_m2") if isinstance(outputs, dict) else None
        thrust_sl_n = outputs.get("thrust_sl_n") if isinstance(outputs, dict) else None
        wing_loading_pa = None
        thrust_to_weight = None
        if isinstance(mtow_kg, (int, float)) and mtow_kg > 0:
            if isinstance(wing_area_m2, (int, float)) and wing_area_m2 > 0:
                wing_loading_pa = mtow_kg * 9.80665 / wing_area_m2
            if isinstance(thrust_sl_n, (int, float)) and thrust_sl_n > 0:
                thrust_to_weight = thrust_sl_n / (mtow_kg * 9.80665)
        engineering = self.engineering or extract_engineering_result(
            self.design_data,
            output_dir=self.output_dir,
            request=self.request,
        )
        return {
            "run_id": self.run_id,
            "status": self.status.value,
            "request": self.request.to_dict(),
            "task_dir": str(self.task_dir),
            "input_path": str(self.input_path),
            "output_dir": str(self.output_dir) if self.output_dir else None,
            "command": self.command,
            "exit_code": self.exit_code,
            "stdout": self.stdout,
            "stderr": self.stderr,
            "started_at": self.started_at,
            "finished_at": self.finished_at,
            "duration_seconds": self.duration_seconds,
            "converged": self.converged,
            "engineering": engineering.to_dict(),
            "summary": {
                "mtow_kg": mtow_kg,
                "empty_weight_kg": outputs.get("empty_weight_kg"),
                "fuel_weight_kg": outputs.get("fuel_weight_kg"),
                "payload_kg": self.request.requirements.payload_kg,
                "wing_area_m2": wing_area_m2,
                "thrust_sl_n": thrust_sl_n,
                "wing_loading_pa": wing_loading_pa,
                "thrust_to_weight": thrust_to_weight,
                "span_m": geometry.get("span_m") if isinstance(geometry, dict) else None,
                "mean_chord_m": geometry.get("mean_chord_m") if isinstance(geometry, dict) else None,
                "fuselage_length_m": (
                    geometry.get("fuselage_length_m") if isinstance(geometry, dict) else None
                ),
                "iterations": outputs.get("iterations"),
                "actual_range_m": performance.get("actual_range_m") if isinstance(performance, dict) else None,
                "takeoff_distance_m": (
                    performance.get("takeoff_distance_m") if isinstance(performance, dict) else None
                ),
                "landing_distance_m": (
                    performance.get("landing_distance_m") if isinstance(performance, dict) else None
                ),
                "artifact_count": len(self.artifacts),
                "issue_count": len(self.issues),
                "engineering_feasible": engineering.engineering_feasible,
                "engineering_status": engineering.overall_status,
                "blocking_failed_count": engineering.blocking_failed_count,
            },
            "artifacts": [str(path) for path in self.artifacts],
            "issues": [issue.to_dict() for issue in self.issues],
        }

    @classmethod
    def from_dict(
        cls,
        value: dict[str, Any],
        *,
        request: AircraftDesignRequest,
        allowed_root: Path | None = None,
    ) -> "AircraftDesignRunResult":
        """Rebuild a persisted result without executing its recorded command."""
        if not isinstance(value, dict):
            raise ValueError("design run result must be an object")

        root = allowed_root.resolve() if allowed_root is not None else None

        def persisted_path(raw: Any, field_name: str, *, optional: bool = False) -> Path | None:
            if optional and raw is None:
                return None
            if not isinstance(raw, str) or not raw:
                raise ValueError(f"persisted {field_name} must be a path string")
            path = Path(raw).resolve()
            if root is not None:
                try:
                    path.relative_to(root)
                except ValueError as exc:
                    raise ValueError(f"persisted {field_name} is outside the generated root") from exc
            return path

        task_dir = persisted_path(value.get("task_dir"), "task_dir")
        input_path = persisted_path(value.get("input_path"), "input_path")
        output_dir = persisted_path(value.get("output_dir"), "output_dir", optional=True)
        design_data: dict[str, Any] | None = None
        if output_dir is not None:
            data_path = output_dir / "design_data.json"
            try:
                loaded = json.loads(data_path.read_text(encoding="utf-8"))
                if isinstance(loaded, dict):
                    design_data = loaded
            except (OSError, json.JSONDecodeError):
                design_data = None
        if design_data is None and isinstance(value.get("summary"), dict):
            design_data = {"outputs": dict(value["summary"])}

        issues: list[DesignValidationIssue] = []
        for item in value.get("issues", []):
            if not isinstance(item, dict):
                raise ValueError("persisted design issues must be objects")
            issues.append(
                DesignValidationIssue(
                    code=str(item.get("code") or "persisted_issue"),
                    message=str(item.get("message") or "Persisted validation issue"),
                    severity=str(item.get("severity") or "error"),
                )
            )

        command = value.get("command", [])
        if not isinstance(command, list) or not all(isinstance(part, str) for part in command):
            raise ValueError("persisted design command must be a string list")
        artifact_values = value.get("artifacts", [])
        if not isinstance(artifact_values, list) or not all(
            isinstance(path, str) for path in artifact_values
        ):
            raise ValueError("persisted artifacts must be a string list")
        artifacts = [persisted_path(path, "artifact") for path in artifact_values]

        exit_code = value.get("exit_code")
        if exit_code is not None and (isinstance(exit_code, bool) or not isinstance(exit_code, int)):
            raise ValueError("persisted exit_code must be an integer or null")
        converged = value.get("converged")
        if converged is not None and not isinstance(converged, bool):
            raise ValueError("persisted converged must be a boolean or null")

        engineering = extract_engineering_result(
            design_data,
            output_dir=output_dir,
            request=request,
            persisted=value.get("engineering") if isinstance(value.get("engineering"), dict) else None,
        )
        persisted_status = DesignRunStatus(str(value.get("status")))
        if persisted_status is DesignRunStatus.COMPLETED:
            if engineering.numerical_converged is False:
                persisted_status = DesignRunStatus.NONCONVERGED
            elif _is_v2_schema(design_data) and engineering.numerical_converged is None:
                persisted_status = DesignRunStatus.FAILED
            elif engineering.engineering_feasible is False:
                persisted_status = DesignRunStatus.ENGINEERING_INFEASIBLE
            elif _is_v2_schema(design_data) and engineering.engineering_feasible is None:
                persisted_status = DesignRunStatus.FAILED
        _append_engineering_issues(
            issues,
            engineering,
            schema_v2=_is_v2_schema(design_data),
        )

        return cls(
            run_id=str(value.get("run_id") or "persisted-run"),
            status=persisted_status,
            request=request,
            task_dir=task_dir,
            input_path=input_path,
            output_dir=output_dir,
            command=list(command),
            exit_code=exit_code,
            stdout=str(value.get("stdout") or ""),
            stderr=str(value.get("stderr") or ""),
            started_at=str(value.get("started_at") or ""),
            finished_at=str(value.get("finished_at") or ""),
            duration_seconds=float(value.get("duration_seconds") or 0.0),
            converged=converged,
            design_data=design_data,
            artifacts=[path for path in artifacts if path is not None],
            issues=issues,
            engineering=engineering,
        )


class AircraftDesignRunner:
    """Run the upstream sizing workflow without model-generated shell commands."""

    def __init__(
        self,
        workspace_root: Path,
        *,
        source_root: Path | None = None,
        generated_root: Path | None = None,
        python_executable: Path | None = None,
    ) -> None:
        self.workspace_root = Path(workspace_root).resolve()
        self.source_root = Path(
            source_root or self.workspace_root / "external" / "aircraft-design-skill"
        ).resolve()
        self.generated_root = Path(
            generated_root or self.workspace_root / ".clawd" / "generated" / "aircraft_design_runs"
        ).resolve()
        self.python_executable = Path(python_executable or sys.executable).resolve()

    def run(
        self,
        request: AircraftDesignRequest,
        *,
        timeout_seconds: float = 180.0,
        cancel_event: threading.Event | None = None,
        on_progress: ProgressCallback | None = None,
        run_id: str | None = None,
    ) -> AircraftDesignRunResult:
        self._validate_environment()
        if not math.isfinite(timeout_seconds) or timeout_seconds <= 0:
            raise ValueError("timeout_seconds must be a positive finite number")

        normalized_run_id = self._normalize_run_id(run_id)
        task_dir = self.generated_root / normalized_run_id
        task_dir.mkdir(parents=True, exist_ok=False)
        input_path = task_dir / "sizing_input.json"
        output_base = task_dir / "output"
        output_base.mkdir()
        input_path.write_text(
            json.dumps(request.to_upstream_dict(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        command = [
            str(self.python_executable),
            "-m",
            "aircraft_design.class2_preliminary.run_sizing",
            str(input_path),
            "--project-name",
            request.project_name,
            "--output-dir",
            str(output_base),
            "--no-viz",
        ]
        started_wall = datetime.now().isoformat(timespec="seconds")
        started_clock = time.monotonic()
        self._emit(on_progress, DesignRunStage.PREPARING, "输入已校验，准备启动总体设计计算", 10)

        env = os.environ.copy()
        current_pythonpath = env.get("PYTHONPATH")
        env["PYTHONPATH"] = (
            f"{self.source_root}{os.pathsep}{current_pythonpath}"
            if current_pythonpath
            else str(self.source_root)
        )
        process = subprocess.Popen(
            command,
            cwd=self.source_root,
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            start_new_session=True,
        )
        self._emit(
            on_progress,
            DesignRunStage.RUNNING,
            "上游总体设计求解器正在运行",
            35,
            {"pid": process.pid},
        )

        stdout = ""
        stderr = ""
        status_override: DesignRunStatus | None = None
        deadline = started_clock + timeout_seconds
        while True:
            try:
                stdout, stderr = process.communicate(timeout=0.2)
                break
            except subprocess.TimeoutExpired:
                if cancel_event is not None and cancel_event.is_set():
                    status_override = DesignRunStatus.CANCELLED
                    self._stop_process(process)
                    stdout, stderr = process.communicate()
                    break
                if time.monotonic() >= deadline:
                    status_override = DesignRunStatus.TIMED_OUT
                    self._stop_process(process)
                    stdout, stderr = process.communicate()
                    break

        output_dir = self._latest_output_dir(output_base)
        self._emit(on_progress, DesignRunStage.VALIDATING, "计算结束，正在校验工程结果", 80)
        issues, design_data, artifacts, converged = self.validate_output(
            request=request,
            output_dir=output_dir,
            exit_code=process.returncode,
        )
        engineering = extract_engineering_result(
            design_data,
            output_dir=output_dir,
            request=request,
        )
        status = status_override or self._status_from_validation(
            process.returncode,
            converged,
            issues,
            engineering=engineering,
        )
        finished_clock = time.monotonic()
        result = AircraftDesignRunResult(
            run_id=normalized_run_id,
            status=status,
            request=request,
            task_dir=task_dir,
            input_path=input_path,
            output_dir=output_dir,
            command=command,
            exit_code=process.returncode,
            stdout=stdout,
            stderr=stderr,
            started_at=started_wall,
            finished_at=datetime.now().isoformat(timespec="seconds"),
            duration_seconds=round(finished_clock - started_clock, 3),
            converged=converged,
            design_data=design_data,
            artifacts=artifacts,
            issues=issues,
            engineering=engineering,
        )
        (task_dir / "run_result.json").write_text(
            json.dumps(result.to_dict(), ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        final_stage = {
            DesignRunStatus.COMPLETED: DesignRunStage.COMPLETED,
            DesignRunStatus.NONCONVERGED: DesignRunStage.NONCONVERGED,
            DesignRunStatus.ENGINEERING_INFEASIBLE: DesignRunStage.ENGINEERING_INFEASIBLE,
            DesignRunStatus.CANCELLED: DesignRunStage.CANCELLED,
            DesignRunStatus.TIMED_OUT: DesignRunStage.TIMED_OUT,
        }.get(status, DesignRunStage.FAILED)
        final_message = {
            DesignRunStatus.COMPLETED: "总体设计计算完成并通过结果校验",
            DesignRunStatus.NONCONVERGED: "总体设计计算完成，但结果未收敛",
            DesignRunStatus.ENGINEERING_INFEASIBLE: "总体设计计算已收敛，但方案未通过工程约束",
            DesignRunStatus.CANCELLED: "总体设计任务已取消",
            DesignRunStatus.TIMED_OUT: "总体设计任务执行超时",
        }.get(status, "总体设计任务执行失败")
        self._emit(
            on_progress,
            final_stage,
            final_message,
            100,
            {"status": status.value, "issue_count": len(issues)},
        )
        return result

    def validate_output(
        self,
        *,
        request: AircraftDesignRequest,
        output_dir: Path | None,
        exit_code: int | None,
    ) -> tuple[
        list[DesignValidationIssue],
        dict[str, Any] | None,
        list[Path],
        bool | None,
    ]:
        issues: list[DesignValidationIssue] = []
        artifacts: list[Path] = []
        if exit_code not in (0, 2, None):
            issues.append(DesignValidationIssue("process_exit", f"solver exited with code {exit_code}"))
        elif exit_code == 2:
            issues.append(
                DesignValidationIssue(
                    "solver_nonconverged_exit",
                    "solver exited with code 2 to report numerical nonconvergence",
                    severity="warning",
                )
            )
        if output_dir is None or not output_dir.is_dir():
            issues.append(DesignValidationIssue("missing_output_dir", "solver did not create an output directory"))
            return issues, None, artifacts, None

        artifacts = [
            path
            for path in sorted(output_dir.rglob("*"))
            if path.is_file() and path.suffix.lower() in RESULT_EXTENSIONS and not path.name.startswith(".")
        ]
        required_files = ("design_data.json", "design_report.md", "design_report_v2.md")
        for filename in required_files:
            if not (output_dir / filename).is_file():
                issues.append(DesignValidationIssue("missing_artifact", f"missing required artifact: {filename}"))

        data_path = output_dir / "design_data.json"
        if not data_path.is_file():
            return issues, None, artifacts, None
        try:
            design_data = json.loads(data_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            issues.append(DesignValidationIssue("invalid_design_data", f"cannot parse design_data.json: {exc}"))
            return issues, None, artifacts, None
        if not isinstance(design_data, dict):
            issues.append(DesignValidationIssue("invalid_design_data", "design_data.json must contain an object"))
            return issues, None, artifacts, None

        echoed_requirements = design_data.get("inputs", {}).get("requirements", {})
        for name, expected in request.requirements.to_dict().items():
            actual = echoed_requirements.get(name)
            if isinstance(expected, bool):
                preserved = actual is expected
            elif isinstance(expected, (int, float)):
                preserved = (
                    not isinstance(actual, bool)
                    and isinstance(actual, (int, float))
                    and math.isclose(float(actual), float(expected), rel_tol=1e-9, abs_tol=1e-9)
                )
            else:
                preserved = actual == expected
            if not preserved:
                issues.append(
                    DesignValidationIssue(
                        "input_mismatch",
                        f"requirements.{name} was not preserved: expected {expected}, got {actual}",
                    )
                )

        outputs = design_data.get("outputs")
        if not isinstance(outputs, dict):
            issues.append(DesignValidationIssue("missing_outputs", "design_data.json has no outputs object"))
            return issues, design_data, artifacts, None
        status_payload = _as_dict(design_data.get("status"))
        converged = _first_bool(
            design_data.get("numerical_converged"),
            status_payload.get("numerical_converged"),
            outputs.get("numerical_converged"),
            outputs.get("converged"),
        )
        for field_name in ("mtow_kg", "empty_weight_kg", "wing_area_m2", "thrust_sl_n"):
            value = outputs.get(field_name)
            if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(float(value)) or value <= 0:
                issues.append(
                    DesignValidationIssue("invalid_metric", f"outputs.{field_name} must be a positive finite number")
                )
        if converged and not (output_dir / "geometry.obj").is_file():
            issues.append(
                DesignValidationIssue(
                    "missing_geometry",
                    "converged result has no geometry.obj",
                    severity="warning",
                )
            )
        engineering = extract_engineering_result(
            design_data,
            output_dir=output_dir,
            request=request,
        )
        if _is_v2_schema(design_data):
            raw_constraints = design_data.get("constraints")
            if not isinstance(raw_constraints, list):
                issues.append(
                    DesignValidationIssue(
                        "invalid_constraints_contract",
                        "schema v2 result must contain a constraints list",
                    )
                )
            else:
                required_constraint_fields = {
                    "id",
                    "label",
                    "direction",
                    "required",
                    "actual",
                    "passed",
                    "blocking",
                    "tolerance",
                }
                for index, constraint in enumerate(raw_constraints):
                    if not isinstance(constraint, dict):
                        issues.append(
                            DesignValidationIssue(
                                "invalid_constraint_contract",
                                f"constraints[{index}] must be an object",
                            )
                        )
                        continue
                    missing = sorted(required_constraint_fields - set(constraint))
                    tolerance = constraint.get("tolerance")
                    tolerance_valid = (
                        not isinstance(tolerance, bool)
                        and isinstance(tolerance, (int, float))
                        and math.isfinite(float(tolerance))
                        and float(tolerance) >= 0.0
                    )
                    if (
                        missing
                        or not isinstance(constraint.get("passed"), bool)
                        or not isinstance(constraint.get("blocking"), bool)
                        or not tolerance_valid
                    ):
                        issues.append(
                            DesignValidationIssue(
                                "invalid_constraint_contract",
                                f"constraints[{index}] has invalid or missing fields: "
                                f"{', '.join(missing) if missing else 'passed/blocking/tolerance'}",
                            )
                        )
            raw_stages = design_data.get("stage_status")
            if not isinstance(raw_stages, dict):
                issues.append(
                    DesignValidationIssue(
                        "invalid_stage_status_contract",
                        "schema v2 result must contain a stage_status object",
                    )
                )
            else:
                for stage_id, stage in raw_stages.items():
                    if not isinstance(stage, dict) or not isinstance(stage.get("status"), str) or not isinstance(
                        stage.get("blocking"), bool
                    ):
                        issues.append(
                            DesignValidationIssue(
                                "invalid_stage_status_contract",
                                f"stage_status.{stage_id} must declare string status and boolean blocking",
                            )
                        )
            explicit_feasible = _first_bool(
                design_data.get("engineering_feasible"),
                status_payload.get("engineering_feasible"),
                outputs.get("engineering_feasible"),
            )
            if explicit_feasible is True and engineering.engineering_feasible is False:
                issues.append(
                    DesignValidationIssue(
                        "inconsistent_engineering_feasibility",
                        "engineering_feasible=true contradicts blocking constraint or stage evidence",
                    )
                )
        _append_engineering_issues(
            issues,
            engineering,
            schema_v2=_is_v2_schema(design_data),
        )
        return issues, design_data, artifacts, converged

    def _validate_environment(self) -> None:
        if not self.python_executable.is_file():
            raise FileNotFoundError(f"Python executable not found: {self.python_executable}")
        module_path = self.source_root / "aircraft_design" / "class2_preliminary" / "run_sizing.py"
        if not module_path.is_file():
            raise FileNotFoundError(f"aircraft design entry point not found: {module_path}")
        self.generated_root.mkdir(parents=True, exist_ok=True)

    def _normalize_run_id(self, run_id: str | None) -> str:
        if run_id is None:
            return f"run-{datetime.now().strftime('%Y%m%d-%H%M%S')}-{uuid4().hex[:8]}"
        normalized = "".join(char for char in run_id if char.isalnum() or char in "-_").strip("-_")
        if not normalized or len(normalized) > 100:
            raise ValueError("run_id must be 1-100 letters, numbers, hyphens, or underscores")
        return normalized

    def _latest_output_dir(self, output_base: Path) -> Path | None:
        candidates = [path for path in output_base.iterdir() if path.is_dir()]
        return max(candidates, key=lambda path: path.stat().st_mtime_ns) if candidates else None

    def _status_from_validation(
        self,
        exit_code: int | None,
        converged: bool | None,
        issues: list[DesignValidationIssue],
        engineering: AircraftDesignEngineeringResult | None = None,
    ) -> DesignRunStatus:
        if exit_code not in (0, 2, None):
            return DesignRunStatus.FAILED
        if exit_code == 2 or converged is False:
            return DesignRunStatus.NONCONVERGED
        if converged is None:
            return DesignRunStatus.FAILED
        engineering_issue_codes = {
            "blocking_constraint_failed",
            "blocking_constraint_unknown",
            "blocking_stage_failed",
            "engineering_infeasible",
            "inconsistent_engineering_feasibility",
        }
        if any(
            issue.severity == "error" and issue.code not in engineering_issue_codes
            for issue in issues
        ):
            return DesignRunStatus.FAILED
        if engineering is not None and engineering.engineering_feasible is False:
            return DesignRunStatus.ENGINEERING_INFEASIBLE
        if any(issue.severity == "error" for issue in issues):
            return DesignRunStatus.FAILED
        return DesignRunStatus.COMPLETED

    def _stop_process(self, process: subprocess.Popen[str]) -> None:
        if process.poll() is not None:
            return
        try:
            os.killpg(process.pid, signal.SIGTERM)
            process.wait(timeout=2)
        except (OSError, subprocess.TimeoutExpired):
            try:
                os.killpg(process.pid, signal.SIGKILL)
            except OSError:
                process.kill()

    def _emit(
        self,
        callback: ProgressCallback | None,
        stage: DesignRunStage,
        message: str,
        progress: int,
        detail: dict[str, Any] | None = None,
    ) -> None:
        if callback is not None:
            callback(DesignRunEvent(stage=stage, message=message, progress=progress, detail=detail))
