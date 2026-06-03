#!/usr/bin/env python3
"""Validate an aero/intake/exhaust evaluation case JSON."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any


REQUIRED_TOP_LEVEL = [
    "case_id",
    "run_mode",
    "analysis_type",
    "fidelity",
    "toolchain",
    "geometry",
    "flow_conditions",
    "boundary_conditions",
    "mesh",
    "solver",
    "monitoring",
    "postprocessing",
]

VALID_RUN_MODES = {"dry_run", "mock", "execute"}
VALID_ANALYSIS_TYPES = {"external_aero", "intake_duct", "nozzle_exhaust", "coupled_propulsion", "postprocess_only"}
VALID_TOOLS = {"starccm", "openfoam", "matlab", "custom", "all"}


def load_case(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise SystemExit("case file must contain a JSON object")
    return data


def names(case: dict[str, Any], key: str) -> list[str]:
    boundary_names = case.get("geometry", {}).get("boundary_names", {})
    value = boundary_names.get(key, [])
    if isinstance(value, str):
        return [value] if value else []
    if isinstance(value, list):
        return [str(item) for item in value if str(item)]
    return []


def add(messages: list[dict[str, str]], level: str, field: str, message: str) -> None:
    messages.append({"level": level, "field": field, "message": message})


def validate(case: dict[str, Any], case_path: Path) -> dict[str, Any]:
    messages: list[dict[str, str]] = []

    for field in REQUIRED_TOP_LEVEL:
        if field not in case:
            add(messages, "error", field, "missing required top-level field")

    case_id = str(case.get("case_id", ""))
    if not case_id or not re.fullmatch(r"[A-Za-z0-9_.-]+", case_id):
        add(messages, "error", "case_id", "use only letters, numbers, underscore, dot, or hyphen")

    run_mode = case.get("run_mode")
    if run_mode not in VALID_RUN_MODES:
        add(messages, "error", "run_mode", f"expected one of {sorted(VALID_RUN_MODES)}")

    analysis_type = case.get("analysis_type")
    if analysis_type not in VALID_ANALYSIS_TYPES:
        add(messages, "error", "analysis_type", f"expected one of {sorted(VALID_ANALYSIS_TYPES)}")

    preferred_tool = case.get("toolchain", {}).get("preferred_tool")
    if preferred_tool not in VALID_TOOLS:
        add(messages, "warning", "toolchain.preferred_tool", f"expected one of {sorted(VALID_TOOLS)}")

    if run_mode == "execute":
        command = case.get("toolchain", {}).get("execute_command")
        if not command:
            add(messages, "error", "toolchain.execute_command", "execute mode requires explicit command")

    geometry = case.get("geometry", {})
    geometry_files = geometry.get("files", [])
    if not geometry_files:
        add(messages, "warning", "geometry.files", "no geometry files listed; dry-run can continue")
    elif isinstance(geometry_files, list):
        for index, item in enumerate(geometry_files):
            if not isinstance(item, dict):
                add(messages, "error", f"geometry.files[{index}]", "file entry must be an object")
                continue
            raw_path = item.get("path")
            if not raw_path:
                add(messages, "error", f"geometry.files[{index}].path", "missing geometry path")
                continue
            file_path = Path(str(raw_path))
            if not file_path.is_absolute():
                file_path = (case_path.parent / file_path).resolve()
            if not file_path.exists():
                add(messages, "warning", f"geometry.files[{index}].path", f"file not found during offline check: {file_path}")
    else:
        add(messages, "error", "geometry.files", "must be a list")

    if not geometry.get("unit"):
        add(messages, "warning", "geometry.unit", "geometry unit is not confirmed")

    flow = case.get("flow_conditions", {})
    if analysis_type != "postprocess_only":
        if flow.get("mach") is None and flow.get("velocity_mps") is None:
            add(messages, "warning", "flow_conditions", "missing Mach or velocity")
        if flow.get("altitude_m") is None and flow.get("pressure_pa") is None:
            add(messages, "warning", "flow_conditions", "missing altitude or static pressure")

    mesh = case.get("mesh", {})
    if mesh.get("target_cell_count") is None:
        add(messages, "warning", "mesh.target_cell_count", "missing target cell count")
    boundary_layer = mesh.get("boundary_layer", {})
    if boundary_layer.get("enabled") and boundary_layer.get("target_y_plus") is None:
        add(messages, "warning", "mesh.boundary_layer.target_y_plus", "missing y+ target")

    solver = case.get("solver", {})
    if solver.get("turbulence_model") is None and analysis_type != "postprocess_only":
        add(messages, "warning", "solver.turbulence_model", "missing turbulence model")
    if solver.get("iterations") is None and analysis_type != "postprocess_only":
        add(messages, "warning", "solver.iterations", "missing iteration count")
    if solver.get("cfl") is None and analysis_type != "postprocess_only":
        add(messages, "warning", "solver.cfl", "missing CFL number")

    if analysis_type == "external_aero":
        if not names(case, "farfield"):
            add(messages, "error", "geometry.boundary_names.farfield", "external aero requires farfield boundary")
        if not names(case, "walls"):
            add(messages, "error", "geometry.boundary_names.walls", "external aero requires wall boundaries")
        refs = geometry.get("reference_values", {})
        if refs.get("area_ref_m2") is None or refs.get("length_ref_m") is None:
            add(messages, "warning", "geometry.reference_values", "force/moment coefficients need reference area and length")

    if analysis_type == "intake_duct":
        if not names(case, "aip"):
            add(messages, "error", "geometry.boundary_names.aip", "intake evaluation requires AIP or engine-face boundary")
        if not names(case, "walls"):
            add(messages, "error", "geometry.boundary_names.walls", "intake evaluation requires duct wall boundaries")
        if not (names(case, "inlets") or names(case, "farfield")):
            add(messages, "error", "geometry.boundary_names.inlets", "intake evaluation requires inlet or farfield boundary")
        if not names(case, "outlets"):
            add(messages, "warning", "geometry.boundary_names.outlets", "engine-face outlet is not confirmed")

    if analysis_type == "nozzle_exhaust":
        if not names(case, "nozzle_inlet"):
            add(messages, "error", "geometry.boundary_names.nozzle_inlet", "nozzle evaluation requires nozzle inlet")
        if not names(case, "nozzle_exit"):
            add(messages, "error", "geometry.boundary_names.nozzle_exit", "nozzle evaluation requires nozzle exit")
        if not names(case, "walls"):
            add(messages, "error", "geometry.boundary_names.walls", "nozzle evaluation requires nozzle wall boundaries")

    if analysis_type == "coupled_propulsion":
        for key in ["aip", "nozzle_inlet", "nozzle_exit", "walls"]:
            if not names(case, key):
                add(messages, "error", f"geometry.boundary_names.{key}", f"coupled propulsion requires {key}")

    error_count = sum(1 for item in messages if item["level"] == "error")
    warning_count = sum(1 for item in messages if item["level"] == "warning")
    status = "blocked" if error_count else ("warning" if warning_count else "ok")

    return {
        "case_id": case.get("case_id"),
        "status": status,
        "error_count": error_count,
        "warning_count": warning_count,
        "messages": messages,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, help="Path to case JSON")
    parser.add_argument("--output", help="Optional validation report JSON")
    args = parser.parse_args()

    case_path = Path(args.case).resolve()
    report = validate(load_case(case_path), case_path)
    if args.output:
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open("w", encoding="utf-8") as handle:
            json.dump(report, handle, ensure_ascii=False, indent=2)
            handle.write("\n")
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if report["status"] == "blocked" else 0


if __name__ == "__main__":
    raise SystemExit(main())
