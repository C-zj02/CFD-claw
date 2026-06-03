#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import html
import json
import math
import re
import sys
import tempfile
from pathlib import Path
from typing import Any, Iterable


def safe_name(value: Any, default: str) -> str:
    text = str(value or "").strip()
    text = re.sub(r"[^A-Za-z0-9._-]+", "-", text).strip("-._")
    return text or default


def as_rows(value: Any) -> list[dict[str, Any]]:
    if value is None:
        return []
    if isinstance(value, list):
        rows: list[dict[str, Any]] = []
        for item in value:
            if isinstance(item, dict):
                rows.append(item)
            else:
                rows.append({"value": item})
        return rows
    if isinstance(value, dict):
        return [value]
    return [{"value": value}]


def stringify(value: Any) -> str:
    if value is None:
        return ""
    if isinstance(value, (dict, list)):
        return json.dumps(value, ensure_ascii=False, sort_keys=True)
    return str(value)


def collect_columns(rows: Iterable[dict[str, Any]], preferred: list[str] | None = None) -> list[str]:
    columns: list[str] = []
    for col in preferred or []:
        if col not in columns:
            columns.append(col)
    for row in rows:
        for key in row.keys():
            if key not in columns:
                columns.append(key)
    return columns


def write_csv(path: Path, rows: list[dict[str, Any]], preferred: list[str] | None = None) -> bool:
    if not rows:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    columns = collect_columns(rows, preferred)
    with path.open("w", encoding="utf-8-sig", newline="") as fh:
        writer = csv.DictWriter(fh, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({key: stringify(row.get(key)) for key in columns})
    return True


def normalize_table_rows(table: dict[str, Any]) -> tuple[list[str] | None, list[dict[str, Any]]]:
    columns = table.get("columns")
    preferred = [str(col) for col in columns] if isinstance(columns, list) else None
    raw_rows = table.get("rows") or []
    rows: list[dict[str, Any]] = []
    for raw in raw_rows:
        if isinstance(raw, dict):
            rows.append(raw)
        elif isinstance(raw, list):
            if preferred:
                rows.append({preferred[i] if i < len(preferred) else f"col_{i + 1}": raw[i] for i in range(len(raw))})
            else:
                rows.append({f"col_{i + 1}": raw[i] for i in range(len(raw))})
        else:
            rows.append({"value": raw})
    return preferred, rows


def numeric_points(series: dict[str, Any]) -> list[tuple[float, float]]:
    points: list[tuple[float, float]] = []
    for pair in series.get("points") or []:
        if not isinstance(pair, (list, tuple)) or len(pair) < 2:
            continue
        try:
            x = float(pair[0])
            y = float(pair[1])
        except (TypeError, ValueError):
            continue
        if math.isfinite(x) and math.isfinite(y):
            points.append((x, y))
    return points


def expand_range(low: float, high: float) -> tuple[float, float]:
    if low == high:
        delta = abs(low) * 0.1 or 1.0
        return low - delta, high + delta
    pad = (high - low) * 0.06
    return low - pad, high + pad


def write_svg(path: Path, figure: dict[str, Any]) -> bool:
    series_list = figure.get("series") or []
    prepared: list[tuple[dict[str, Any], list[tuple[float, float]]]] = []
    for series in series_list:
        if isinstance(series, dict):
            pts = numeric_points(series)
            if pts:
                prepared.append((series, pts))
    if not prepared:
        return False

    all_x = [x for _, pts in prepared for x, _ in pts]
    all_y = [y for _, pts in prepared for _, y in pts]
    if figure.get("x_range") and len(figure["x_range"]) >= 2:
        x_min, x_max = float(figure["x_range"][0]), float(figure["x_range"][1])
    else:
        x_min, x_max = expand_range(min(all_x), max(all_x))
    if figure.get("y_range") and len(figure["y_range"]) >= 2:
        y_min, y_max = float(figure["y_range"][0]), float(figure["y_range"][1])
    else:
        y_min, y_max = expand_range(min(all_y), max(all_y))

    width, height = 960, 540
    left, right, top, bottom = 90, 40, 60, 82
    plot_w = width - left - right
    plot_h = height - top - bottom

    def sx(x: float) -> float:
        return left + (x - x_min) / (x_max - x_min) * plot_w

    def sy(y: float) -> float:
        return top + (y_max - y) / (y_max - y_min) * plot_h

    colors = ["#2563eb", "#dc2626", "#059669", "#9333ea", "#ea580c", "#0891b2"]
    parts: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text x="{width / 2}" y="30" text-anchor="middle" font-family="Arial, sans-serif" font-size="20" font-weight="700">{html.escape(str(figure.get("title") or "Performance Figure"))}</text>',
        f'<rect x="{left}" y="{top}" width="{plot_w}" height="{plot_h}" fill="#f8fafc" stroke="#334155" stroke-width="1"/>',
    ]

    for i in range(6):
        gx = left + plot_w * i / 5
        gy = top + plot_h * i / 5
        x_val = x_min + (x_max - x_min) * i / 5
        y_val = y_max - (y_max - y_min) * i / 5
        parts.append(f'<line x1="{gx:.2f}" y1="{top}" x2="{gx:.2f}" y2="{top + plot_h}" stroke="#e2e8f0"/>')
        parts.append(f'<line x1="{left}" y1="{gy:.2f}" x2="{left + plot_w}" y2="{gy:.2f}" stroke="#e2e8f0"/>')
        parts.append(f'<text x="{gx:.2f}" y="{top + plot_h + 24}" text-anchor="middle" font-family="Arial, sans-serif" font-size="12" fill="#334155">{x_val:.3g}</text>')
        parts.append(f'<text x="{left - 12}" y="{gy + 4:.2f}" text-anchor="end" font-family="Arial, sans-serif" font-size="12" fill="#334155">{y_val:.3g}</text>')

    parts.append(f'<text x="{left + plot_w / 2}" y="{height - 22}" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="#0f172a">{html.escape(str(figure.get("x_label") or "x"))}</text>')
    parts.append(f'<text transform="translate(24 {top + plot_h / 2}) rotate(-90)" text-anchor="middle" font-family="Arial, sans-serif" font-size="14" fill="#0f172a">{html.escape(str(figure.get("y_label") or "y"))}</text>')

    for idx, (series, pts) in enumerate(prepared):
        color = colors[idx % len(colors)]
        polyline = " ".join(f"{sx(x):.2f},{sy(y):.2f}" for x, y in pts)
        name = html.escape(str(series.get("name") or f"series {idx + 1}"))
        parts.append(f'<polyline points="{polyline}" fill="none" stroke="{color}" stroke-width="2.5"/>')
        for x, y in pts:
            parts.append(f'<circle cx="{sx(x):.2f}" cy="{sy(y):.2f}" r="3.5" fill="{color}"/>')
        legend_x = left + 12 + idx * 150
        legend_y = top + 18
        parts.append(f'<line x1="{legend_x}" y1="{legend_y}" x2="{legend_x + 24}" y2="{legend_y}" stroke="{color}" stroke-width="3"/>')
        parts.append(f'<text x="{legend_x + 30}" y="{legend_y + 4}" font-family="Arial, sans-serif" font-size="12" fill="#0f172a">{name}</text>')

    parts.append("</svg>")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(parts), encoding="utf-8")
    return True


def markdown_table(rows: list[dict[str, Any]], max_rows: int = 12) -> str:
    if not rows:
        return ""
    columns = collect_columns(rows)
    lines = [
        "| " + " | ".join(columns) + " |",
        "| " + " | ".join("---" for _ in columns) + " |",
    ]
    for row in rows[:max_rows]:
        lines.append("| " + " | ".join(stringify(row.get(col)).replace("\n", " ") for col in columns) + " |")
    if len(rows) > max_rows:
        lines.append(f"| ... | {' | '.join('' for _ in columns[1:])} |")
    return "\n".join(lines)


def write_summary(path: Path, bundle: dict[str, Any], written: list[Path]) -> None:
    case = bundle.get("case") or {}
    inputs = bundle.get("inputs") or {}
    results = bundle.get("results") or {}
    metrics = as_rows(results.get("metrics"))
    assumptions = as_rows(bundle.get("assumptions"))
    confirmations = as_rows(bundle.get("confirmations"))

    lines = [
        f"# {case.get('title') or case.get('id') or 'Flight Performance Analysis'}",
        "",
        "## 分析目标",
        "",
        stringify(case.get("goal") or "未填写"),
        "",
        "## 输入状态",
        "",
    ]
    for key in ["aerodynamics", "propulsion", "weight_states", "profile_segments", "environment", "constraints"]:
        rows = as_rows(inputs.get(key))
        confirmed = sum(1 for row in rows if row.get("status") == "confirmed")
        assumed = sum(1 for row in rows if row.get("status") in {"assumed", "pending"})
        lines.append(f"- `{key}`: {len(rows)} 条，confirmed={confirmed}，assumed/pending={assumed}")

    lines.extend(["", "## 关键性能结果", ""])
    lines.append(markdown_table(metrics) or "未填写。")
    lines.extend(["", "## 假设与确认", ""])
    lines.append("### 假设")
    lines.append("")
    lines.append(markdown_table(assumptions) or "无。")
    lines.append("")
    lines.append("### 确认记录")
    lines.append("")
    lines.append(markdown_table(confirmations) or "无。")
    lines.extend(["", "## 文件产物", ""])
    for item in written:
        lines.append(f"- `{item.as_posix()}`")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_bundle(bundle: dict[str, Any], output_dir: Path) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []

    case_path = output_dir / "case.json"
    case_path.write_text(json.dumps(bundle, ensure_ascii=False, indent=2), encoding="utf-8")
    written.append(case_path)

    inputs = bundle.get("inputs") or {}
    input_sections = {
        "aerodynamics": output_dir / "features" / "aerodynamics.csv",
        "propulsion": output_dir / "features" / "propulsion.csv",
        "weight_states": output_dir / "features" / "weight_states.csv",
        "environment": output_dir / "features" / "environment.csv",
        "constraints": output_dir / "features" / "constraints.csv",
        "profile_segments": output_dir / "profiles" / "profile_segments.csv",
    }
    for key, path in input_sections.items():
        if write_csv(path, as_rows(inputs.get(key))):
            written.append(path)

    results = bundle.get("results") or {}
    metrics_path = output_dir / "results" / "performance_metrics.csv"
    if write_csv(metrics_path, as_rows(results.get("metrics"))):
        written.append(metrics_path)

    for idx, table in enumerate(results.get("tables") or []):
        if not isinstance(table, dict):
            continue
        preferred, rows = normalize_table_rows(table)
        table_id = safe_name(table.get("id") or table.get("title"), f"table-{idx + 1}")
        table_path = output_dir / "results" / f"{table_id}.csv"
        if write_csv(table_path, rows, preferred):
            written.append(table_path)

    record_sections = {
        "assumptions": output_dir / "records" / "assumptions.csv",
        "confirmations": output_dir / "records" / "confirmations.csv",
        "sources": output_dir / "records" / "sources.csv",
    }
    for key, path in record_sections.items():
        if write_csv(path, as_rows(bundle.get(key))):
            written.append(path)

    for idx, figure in enumerate(bundle.get("figures") or []):
        if not isinstance(figure, dict):
            continue
        figure_id = safe_name(figure.get("id") or figure.get("title"), f"figure-{idx + 1}")
        figure_path = output_dir / "figures" / f"{figure_id}.svg"
        if write_svg(figure_path, figure):
            written.append(figure_path)

    summary_path = output_dir / "summary.md"
    write_summary(summary_path, bundle, written)
    written.append(summary_path)
    return written


def sample_bundle() -> dict[str, Any]:
    return {
        "case": {
            "id": "sample-flight-performance",
            "title": "样例飞行性能分析",
            "goal": "演示性能分析结果归档结构。",
            "aircraft_type": "fixed-wing UAV",
            "created_by": "flight-performance-analysis",
        },
        "inputs": {
            "aerodynamics": [
                {"id": "aero.CD0", "name": "零升阻力系数", "value": 0.032, "unit": "-", "condition": "clean cruise", "source": "user", "status": "confirmed"},
                {"id": "aero.K", "name": "诱导阻力因子", "value": 0.045, "unit": "-", "condition": "clean cruise", "source": "calculated", "status": "calculated"},
            ],
            "propulsion": [
                {"id": "prop.SFC", "name": "耗油率", "value": 0.32, "unit": "kg/(kW*h)", "condition": "cruise", "source": "assumption", "status": "pending"}
            ],
            "weight_states": [
                {"id": "weight.takeoff", "name": "起飞重量", "value": 1200, "unit": "kg", "condition": "mission start", "source": "user", "status": "confirmed"}
            ],
            "profile_segments": [
                {"segment": "cruise", "mode": "constant altitude", "altitude_m": 3000, "speed": 58, "speed_unit": "m/s", "distance_km": 420, "weight_start_kg": 1120, "weight_end_kg": 1035, "status": "calculated"}
            ],
            "environment": [
                {"id": "env.atmosphere", "name": "大气模型", "value": "ISA", "unit": "-", "source": "user", "status": "confirmed"}
            ],
            "constraints": [
                {"id": "limit.runway", "name": "跑道长度", "value": 800, "unit": "m", "source": "user", "status": "confirmed"}
            ],
        },
        "results": {
            "metrics": [
                {"name": "巡航航程", "value": 435, "unit": "km", "condition": "3000 m, 58 m/s", "method": "segment estimate", "status": "calculated"}
            ],
            "tables": [
                {
                    "id": "segment_weight_trace",
                    "title": "任务段重量递推",
                    "columns": ["segment", "weight_start_kg", "weight_end_kg", "fuel_used_kg"],
                    "rows": [{"segment": "cruise", "weight_start_kg": 1120, "weight_end_kg": 1035, "fuel_used_kg": 85}],
                }
            ],
        },
        "figures": [
            {
                "id": "range-vs-speed",
                "title": "巡航速度对航程的影响",
                "x_label": "速度 (m/s)",
                "y_label": "航程 (km)",
                "series": [{"name": "估算航程", "points": [[45, 390], [55, 435], [65, 410]]}],
            }
        ],
        "assumptions": [
            {"item": "prop.SFC", "value": 0.32, "unit": "kg/(kW*h)", "reason": "演示用假设", "status": "pending"}
        ],
        "confirmations": [
            {"stage": "输入确认", "summary": "样例数据用于脚本自测。", "status": "demo"}
        ],
        "sources": [
            {"title": "sample", "path": "generated", "note": "self-test bundle"}
        ],
    }


def run_self_test() -> int:
    root = Path.cwd()
    with tempfile.TemporaryDirectory(prefix=".flight_perf_selftest_", dir=root) as tmp:
        tmp_path = Path(tmp)
        out_dir = tmp_path / "out"
        written = write_bundle(sample_bundle(), out_dir)
        required = [
            out_dir / "case.json",
            out_dir / "summary.md",
            out_dir / "features" / "aerodynamics.csv",
            out_dir / "profiles" / "profile_segments.csv",
            out_dir / "results" / "performance_metrics.csv",
            out_dir / "figures" / "range-vs-speed.svg",
        ]
        missing = [path for path in required if not path.exists()]
        if missing:
            for path in missing:
                print(f"missing: {path}", file=sys.stderr)
            return 1
        if len(written) < len(required):
            print("unexpectedly few output files", file=sys.stderr)
            return 1
    print("self-test ok")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Write a flight-performance analysis bundle to JSON, CSV, Markdown, and SVG artifacts.")
    parser.add_argument("--input", help="Path to bundle JSON.")
    parser.add_argument("--output", help="Output directory. Defaults to outputs/performance-analysis/<case-id>.")
    parser.add_argument("--sample-json", action="store_true", help="Print a sample bundle JSON and exit.")
    parser.add_argument("--self-test", action="store_true", help="Run a local smoke test and exit.")
    args = parser.parse_args(argv)

    if args.sample_json:
        print(json.dumps(sample_bundle(), ensure_ascii=False, indent=2))
        return 0
    if args.self_test:
        return run_self_test()
    if not args.input:
        parser.error("--input is required unless --sample-json or --self-test is used")

    input_path = Path(args.input)
    bundle = json.loads(input_path.read_text(encoding="utf-8"))
    case = bundle.get("case") or {}
    case_id = safe_name(case.get("id") or input_path.stem, "flight-performance-case")
    output_dir = Path(args.output) if args.output else Path("outputs") / "performance-analysis" / case_id
    written = write_bundle(bundle, output_dir)
    for path in written:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
