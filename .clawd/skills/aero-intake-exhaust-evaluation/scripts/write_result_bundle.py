#!/usr/bin/env python3
"""Write a portable evaluation result bundle from case and run artifacts."""

from __future__ import annotations

import argparse
import csv
import json
import shutil
from pathlib import Path
from typing import Any


def load_case(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise SystemExit("case file must contain a JSON object")
    return data


def copy_if_exists(source: Path, destination: Path) -> list[str]:
    copied: list[str] = []
    if not source.exists():
        return copied
    if source.is_file():
        if source.resolve() == destination.resolve():
            return [str(destination)]
        destination.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, destination)
        return [str(destination)]
    for item in source.rglob("*"):
        if item.is_file():
            target = destination / item.relative_to(source)
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(item, target)
            copied.append(str(target))
    return copied


def read_metrics(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def summary_markdown(case: dict[str, Any], metrics: list[dict[str, str]], copied_files: list[str]) -> str:
    assumptions = case.get("assumptions", [])
    confirmation_log = case.get("confirmation_log", [])
    metric_lines = ["| Metric | Value | Unit | Source | Status |", "| --- | ---: | --- | --- | --- |"]
    for row in metrics:
        metric_lines.append(
            f"| {row.get('metric', '')} | {row.get('value', '')} | {row.get('unit', '')} | {row.get('source', '')} | {row.get('status', '')} |"
        )
    if len(metric_lines) == 2:
        metric_lines.append("| No metrics found |  |  |  |  |")

    assumption_lines = [f"- `{item.get('field')}` = `{item.get('value')}` ({item.get('source')})" for item in assumptions if isinstance(item, dict)]
    if not assumption_lines:
        assumption_lines = ["- No assumptions recorded."]

    confirmation_lines = [
        f"- {item.get('node', 'unknown')}: {item.get('status', 'unknown')} - {item.get('note', '')}"
        for item in confirmation_log
        if isinstance(item, dict)
    ]
    if not confirmation_lines:
        confirmation_lines = ["- No confirmation records found."]

    file_lines = [f"- `{path}`" for path in copied_files]
    if not file_lines:
        file_lines = ["- No external artifacts copied."]

    return f"""# Aero Intake Exhaust Evaluation Summary

## Case

- Case ID: `{case.get('case_id')}`
- Analysis type: `{case.get('analysis_type')}`
- Fidelity: `{case.get('fidelity')}`
- Run mode: `{case.get('run_mode')}`
- Preferred tool: `{case.get('toolchain', {}).get('preferred_tool')}`

## Metrics

{chr(10).join(metric_lines)}

## Assumptions

{chr(10).join(assumption_lines)}

## Confirmation Log

{chr(10).join(confirmation_lines)}

## Files

{chr(10).join(file_lines)}

## Notes

Mock results are not physical CFD results. Execute mode requires confirmed external tool installation, license, command, and model quality checks.
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", required=True, help="Path to case JSON")
    parser.add_argument("--run-dir", help="Optional solver/mock run directory")
    parser.add_argument("--config-dir", help="Optional generated config directory")
    parser.add_argument("--output", required=True, help="Output bundle directory")
    args = parser.parse_args()

    case_path = Path(args.case)
    case = load_case(case_path)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)

    copied: list[str] = []
    copied.extend(copy_if_exists(case_path, output / "case.json"))
    if args.config_dir:
        copied.extend(copy_if_exists(Path(args.config_dir), output / "configs"))
    if args.run_dir:
        copied.extend(copy_if_exists(Path(args.run_dir), output / "run"))

    metrics = read_metrics(output / "run" / "metrics.csv")
    results_dir = output / "results"
    results_dir.mkdir(exist_ok=True)
    if (output / "run" / "metrics.csv").exists():
        copied.extend(copy_if_exists(output / "run" / "metrics.csv", results_dir / "metrics.csv"))

    summary_path = output / "summary.md"
    summary_path.write_text(summary_markdown(case, metrics, copied), encoding="utf-8")
    copied.append(str(summary_path))

    manifest = {"case_id": case.get("case_id"), "status": "bundled", "files": copied}
    manifest_path = output / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    copied.append(str(manifest_path))

    print(json.dumps({"status": "ok", "bundle": str(output), "files": copied}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
