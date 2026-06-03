#!/usr/bin/env python3
"""Generate deterministic mock monitor and metric data for workflow validation."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import random
from pathlib import Path
from typing import Any


def load_case(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise SystemExit("case file must contain a JSON object")
    return data


def seed_for(case: dict[str, Any]) -> int:
    digest = hashlib.sha256(str(case.get("case_id", "case")).encode("utf-8")).hexdigest()
    return int(digest[:12], 16)


def metric_rows(case: dict[str, Any], rng: random.Random) -> list[dict[str, str]]:
    analysis_type = case.get("analysis_type")
    rows: list[dict[str, str]] = []

    def add(metric: str, value: float, unit: str, note: str) -> None:
        rows.append(
            {
                "metric": metric,
                "value": f"{value:.6g}",
                "unit": unit,
                "source": "mock",
                "status": "mock",
                "note": note,
            }
        )

    if analysis_type == "external_aero":
        add("CL", 0.25 + rng.random() * 0.5, "-", "non-physical mock coefficient")
        add("CD", 0.015 + rng.random() * 0.08, "-", "non-physical mock coefficient")
        add("Cm", -0.1 + rng.random() * 0.2, "-", "non-physical mock coefficient")
    if analysis_type in {"intake_duct", "coupled_propulsion"}:
        add("mass_flow", 15 + rng.random() * 35, "kg/s", "non-physical mock flow rate")
        add("total_pressure_recovery", 0.88 + rng.random() * 0.09, "-", "non-physical mock recovery")
        add("distortion", 0.02 + rng.random() * 0.08, "-", "non-physical mock distortion")
        add("aip_uniformity", 0.9 + rng.random() * 0.08, "-", "non-physical mock uniformity")
    if analysis_type in {"nozzle_exhaust", "coupled_propulsion"}:
        add("gross_thrust", 8000 + rng.random() * 40000, "N", "non-physical mock thrust")
        add("thrust_coefficient", 0.9 + rng.random() * 0.08, "-", "non-physical mock coefficient")
        add("exit_pressure_ratio", 0.7 + rng.random() * 0.6, "-", "non-physical mock pressure ratio")

    add("mass_balance_error_percent", rng.random() * 0.5, "%", "non-physical mock conservation check")
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, help="Path to case JSON")
    parser.add_argument("--output", required=True, help="Output run directory")
    parser.add_argument("--iterations", type=int, help="Override number of mock iterations")
    args = parser.parse_args()

    case = load_case(Path(args.case))
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    rng = random.Random(seed_for(case))
    iterations = args.iterations or int(case.get("solver", {}).get("iterations", 300) or 300)
    iterations = max(20, min(iterations, 5000))

    residual_names = case.get("monitoring", {}).get("residuals", ["continuity", "x_momentum", "energy"])
    custom_monitors = case.get("monitoring", {}).get("custom_monitors", [])

    monitors_path = output / "monitors.csv"
    with monitors_path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = ["iteration"] + residual_names + custom_monitors
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for iteration in range(1, iterations + 1):
            fraction = iteration / iterations
            row: dict[str, Any] = {"iteration": iteration}
            for index, name in enumerate(residual_names):
                start = 1e-1 / (index + 1)
                floor = 1e-5 * (index + 1)
                noise = 1 + 0.04 * math.sin(iteration / (8 + index))
                row[name] = f"{(start * math.exp(-5 * fraction) + floor) * noise:.7g}"
            for index, name in enumerate(custom_monitors):
                target = 1.0 - 0.04 * index
                row[name] = f"{target - 0.2 * math.exp(-4 * fraction) + 0.002 * math.sin(iteration / 13):.7g}"
            writer.writerow(row)

    metrics_path = output / "metrics.csv"
    with metrics_path.open("w", newline="", encoding="utf-8") as handle:
        fieldnames = ["metric", "value", "unit", "source", "status", "note"]
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        for row in metric_rows(case, rng):
            writer.writerow(row)

    log_path = output / "solver.log"
    log_path.write_text(
        "\n".join(
            [
                "MOCK RUN ONLY - no CFD solver was executed.",
                f"case_id={case.get('case_id')}",
                f"analysis_type={case.get('analysis_type')}",
                f"iterations={iterations}",
                "status=completed",
                "",
            ]
        ),
        encoding="utf-8",
    )

    summary = {"status": "mock_completed", "files": [str(monitors_path), str(metrics_path), str(log_path)]}
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
