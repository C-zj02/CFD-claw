#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import html
import json
import math
import sys
from pathlib import Path
from typing import Any, Iterable


COLORS = [
    "#1f77b4",
    "#d62728",
    "#2ca02c",
    "#9467bd",
    "#ff7f0e",
    "#17becf",
    "#8c564b",
    "#7f7f7f",
]

SENSE_LABELS = {
    "above": "可行侧：上方",
    "below": "可行侧：下方",
    "left": "可行侧：左侧",
    "right": "可行侧：右侧",
}


def configure_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is not None:
            reconfigure(errors="replace")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render aircraft W/S - T/W constraint boundary data as SVG.")
    parser.add_argument("--input", required=True, help="JSON specification for the constraint boundary chart.")
    parser.add_argument("--output", required=True, help="Output SVG path.")
    parser.add_argument("--csv", help="Optional CSV path for plotted curve data.")
    parser.add_argument("--width", type=int, default=1100, help="SVG width in pixels.")
    parser.add_argument("--height", type=int, default=760, help="SVG height in pixels.")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    configure_stdio()
    args = parse_args(argv or sys.argv[1:])
    input_path = Path(args.input).expanduser().resolve()
    output_path = Path(args.output).expanduser().resolve()
    csv_path = Path(args.csv).expanduser().resolve() if args.csv else None

    spec = json.loads(input_path.read_text(encoding="utf-8"))
    normalized = normalize_spec(spec)
    svg = render_svg(normalized, width=args.width, height=args.height)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(svg)

    if csv_path is not None:
        csv_path.parent.mkdir(parents=True, exist_ok=True)
        write_csv(normalized, csv_path)

    print(f"SVG: {output_path}")
    if csv_path is not None:
        print(f"CSV: {csv_path}")
    return 0


def normalize_spec(spec: dict[str, Any]) -> dict[str, Any]:
    constraints = [normalize_constraint(item, index) for index, item in enumerate(spec.get("constraints", []))]
    regions = [normalize_region(item) for item in spec.get("regions", [])]
    design_points = [normalize_design_point(item) for item in spec.get("design_points", [])]

    if not constraints and not design_points:
        raise ValueError("spec must contain at least one constraint or design point")

    xs: list[float] = []
    ys: list[float] = []
    for item in constraints:
        for x, y in item["points"]:
            xs.append(x)
            ys.append(y)
    for item in regions:
        for x, y in item["points"]:
            xs.append(x)
            ys.append(y)
    for item in design_points:
        xs.append(item["x"])
        ys.append(item["y"])

    x_range = as_range(spec.get("x_range"), xs, pad_ratio=0.08)
    y_range = as_range(spec.get("y_range"), ys, pad_ratio=0.12)

    for item in constraints:
        if item.get("vertical_x") is not None:
            x = item["vertical_x"]
            item["points"] = [(x, y_range[0]), (x, y_range[1])]
        if item.get("horizontal_y") is not None:
            y = item["horizontal_y"]
            item["points"] = [(x_range[0], y), (x_range[1], y)]

    return {
        "title": str(spec.get("title") or "方案界限线图"),
        "subtitle": str(spec.get("subtitle") or ""),
        "x_label": str(spec.get("x_label") or "翼载荷 W/S"),
        "y_label": str(spec.get("y_label") or "推重比 T/W"),
        "x_range": x_range,
        "y_range": y_range,
        "constraints": constraints,
        "regions": regions,
        "design_points": design_points,
        "notes": [str(note) for note in spec.get("notes", [])],
    }


def normalize_constraint(item: dict[str, Any], index: int) -> dict[str, Any]:
    name = str(item.get("name") or f"约束 {index + 1}")
    sense = str(item.get("sense") or "").lower()
    if sense and sense not in SENSE_LABELS:
        raise ValueError(f"unknown sense for {name}: {sense}")

    color = str(item.get("color") or COLORS[index % len(COLORS)])
    points = parse_points(item.get("points", []))
    vertical_x = None
    horizontal_y = None

    if "x" in item:
        vertical_x = as_float(item["x"], f"{name}.x")
        points = []
    if "y" in item:
        horizontal_y = as_float(item["y"], f"{name}.y")
        points = []

    if not points and vertical_x is None and horizontal_y is None:
        raise ValueError(f"constraint {name} must provide points, x, or y")

    return {
        "name": name,
        "sense": sense,
        "color": color,
        "points": points,
        "vertical_x": vertical_x,
        "horizontal_y": horizontal_y,
        "source": str(item.get("source") or ""),
    }


def normalize_region(item: dict[str, Any]) -> dict[str, Any]:
    points = parse_points(item.get("points", []))
    if len(points) < 3:
        raise ValueError("region must contain at least three points")
    return {
        "name": str(item.get("name") or "可行域"),
        "points": points,
        "fill": str(item.get("fill") or "#2ca02c"),
        "opacity": float(item.get("opacity", 0.12)),
    }


def normalize_design_point(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "name": str(item.get("name") or "设计点"),
        "x": as_float(item.get("x"), "design_point.x"),
        "y": as_float(item.get("y"), "design_point.y"),
        "color": str(item.get("color") or "#111827"),
    }


def parse_points(raw_points: Any) -> list[tuple[float, float]]:
    points: list[tuple[float, float]] = []
    for index, raw in enumerate(raw_points or []):
        if not isinstance(raw, (list, tuple)) or len(raw) != 2:
            raise ValueError(f"point #{index + 1} must be [x, y]")
        points.append((as_float(raw[0], "point.x"), as_float(raw[1], "point.y")))
    return points


def as_float(value: Any, label: str) -> float:
    try:
        result = float(value)
    except (TypeError, ValueError) as exc:
        raise ValueError(f"{label} must be numeric") from exc
    if not math.isfinite(result):
        raise ValueError(f"{label} must be finite")
    return result


def as_range(raw_range: Any, values: list[float], *, pad_ratio: float) -> tuple[float, float]:
    if raw_range is not None:
        if not isinstance(raw_range, (list, tuple)) or len(raw_range) != 2:
            raise ValueError("range must be [min, max]")
        low = as_float(raw_range[0], "range.min")
        high = as_float(raw_range[1], "range.max")
    else:
        if not values:
            low, high = 0.0, 1.0
        else:
            low, high = min(values), max(values)
            span = high - low
            pad = span * pad_ratio if span else max(abs(high), 1.0) * pad_ratio
            low -= pad
            high += pad
    if high <= low:
        raise ValueError("range max must be greater than min")
    return (low, high)


def render_svg(spec: dict[str, Any], *, width: int, height: int) -> str:
    margin = {"left": 96, "right": 310, "top": 88, "bottom": 92}
    plot_w = width - margin["left"] - margin["right"]
    plot_h = height - margin["top"] - margin["bottom"]
    x_min, x_max = spec["x_range"]
    y_min, y_max = spec["y_range"]

    def sx(x: float) -> float:
        return margin["left"] + (x - x_min) / (x_max - x_min) * plot_w

    def sy(y: float) -> float:
        return margin["top"] + (y_max - y) / (y_max - y_min) * plot_h

    parts: list[str] = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}">',
        "<style>",
        "text { font-family: 'Microsoft YaHei', 'Noto Sans CJK SC', Arial, sans-serif; fill: #111827; }",
        ".axis { stroke: #111827; stroke-width: 1.6; }",
        ".grid { stroke: #e5e7eb; stroke-width: 1; }",
        ".tick { font-size: 13px; fill: #374151; }",
        ".label { font-size: 17px; font-weight: 600; }",
        ".title { font-size: 26px; font-weight: 700; }",
        ".subtitle { font-size: 14px; fill: #4b5563; }",
        ".legend { font-size: 13px; fill: #1f2937; }",
        "</style>",
        '<rect width="100%" height="100%" fill="#ffffff"/>',
        f'<text class="title" x="{margin["left"]}" y="38">{esc(spec["title"])}</text>',
    ]
    if spec["subtitle"]:
        parts.append(f'<text class="subtitle" x="{margin["left"]}" y="62">{esc(spec["subtitle"])}</text>')

    parts.extend(draw_grid_and_axes(sx, sy, spec, margin, plot_w, plot_h))

    for region in spec["regions"]:
        points = " ".join(f"{sx(x):.2f},{sy(y):.2f}" for x, y in region["points"])
        parts.append(
            f'<polygon points="{points}" fill="{esc(region["fill"])}" opacity="{region["opacity"]:.3f}" '
            f'stroke="{esc(region["fill"])}" stroke-width="1.2"/>'
        )

    for item in spec["constraints"]:
        points = sorted(item["points"], key=lambda p: p[0])
        polyline = " ".join(f"{sx(x):.2f},{sy(y):.2f}" for x, y in points)
        parts.append(
            f'<polyline points="{polyline}" fill="none" stroke="{esc(item["color"])}" '
            'stroke-width="2.4" stroke-linejoin="round" stroke-linecap="round"/>'
        )
        label_x, label_y = points[min(len(points) - 1, max(0, len(points) // 2))]
        parts.append(
            f'<text class="legend" x="{sx(label_x) + 8:.2f}" y="{sy(label_y) - 8:.2f}" '
            f'fill="{esc(item["color"])}">{esc(item["name"])}</text>'
        )

    for point in spec["design_points"]:
        x = sx(point["x"])
        y = sy(point["y"])
        color = esc(point["color"])
        parts.append(f'<circle cx="{x:.2f}" cy="{y:.2f}" r="6.5" fill="{color}" stroke="#ffffff" stroke-width="2"/>')
        parts.append(f'<line x1="{x - 9:.2f}" y1="{y:.2f}" x2="{x + 9:.2f}" y2="{y:.2f}" stroke="{color}" stroke-width="1.4"/>')
        parts.append(f'<line x1="{x:.2f}" y1="{y - 9:.2f}" x2="{x:.2f}" y2="{y + 9:.2f}" stroke="{color}" stroke-width="1.4"/>')
        parts.append(
            f'<text class="legend" x="{x + 12:.2f}" y="{y - 10:.2f}">'
            f'{esc(point["name"])} ({point["x"]:.3g}, {point["y"]:.3g})</text>'
        )

    parts.extend(draw_legend(spec, x=width - margin["right"] + 42, y=margin["top"]))
    parts.append("</svg>")
    return "\n".join(parts) + "\n"


def draw_grid_and_axes(sx, sy, spec: dict[str, Any], margin: dict[str, int], plot_w: int, plot_h: int) -> list[str]:
    x_min, x_max = spec["x_range"]
    y_min, y_max = spec["y_range"]
    parts: list[str] = []

    for value in ticks(x_min, x_max, 6):
        x = sx(value)
        parts.append(f'<line class="grid" x1="{x:.2f}" y1="{margin["top"]}" x2="{x:.2f}" y2="{margin["top"] + plot_h}"/>')
        parts.append(f'<text class="tick" text-anchor="middle" x="{x:.2f}" y="{margin["top"] + plot_h + 24}">{format_tick(value)}</text>')

    for value in ticks(y_min, y_max, 6):
        y = sy(value)
        parts.append(f'<line class="grid" x1="{margin["left"]}" y1="{y:.2f}" x2="{margin["left"] + plot_w}" y2="{y:.2f}"/>')
        parts.append(f'<text class="tick" text-anchor="end" x="{margin["left"] - 12}" y="{y + 4:.2f}">{format_tick(value)}</text>')

    parts.append(f'<rect x="{margin["left"]}" y="{margin["top"]}" width="{plot_w}" height="{plot_h}" fill="none" class="axis"/>')
    parts.append(
        f'<text class="label" text-anchor="middle" x="{margin["left"] + plot_w / 2:.2f}" '
        f'y="{margin["top"] + plot_h + 62}">{esc(spec["x_label"])}</text>'
    )
    parts.append(
        f'<text class="label" text-anchor="middle" transform="translate({margin["left"] - 68},{margin["top"] + plot_h / 2:.2f}) rotate(-90)">'
        f'{esc(spec["y_label"])}</text>'
    )
    return parts


def draw_legend(spec: dict[str, Any], *, x: int, y: int) -> list[str]:
    parts: list[str] = [
        f'<text class="label" x="{x}" y="{y}">图例与可行侧</text>',
    ]
    cursor = y + 28
    for item in spec["constraints"]:
        parts.append(f'<line x1="{x}" y1="{cursor - 4}" x2="{x + 28}" y2="{cursor - 4}" stroke="{esc(item["color"])}" stroke-width="3"/>')
        sense = SENSE_LABELS.get(item["sense"], "可行侧：未指定")
        parts.append(f'<text class="legend" x="{x + 38}" y="{cursor}">{esc(item["name"])}；{esc(sense)}</text>')
        cursor += 24
        if item.get("source"):
            parts.append(f'<text class="legend" x="{x + 38}" y="{cursor}" fill="#6b7280">来源：{esc(item["source"])}</text>')
            cursor += 20

    for region in spec["regions"]:
        parts.append(f'<rect x="{x}" y="{cursor - 13}" width="28" height="14" fill="{esc(region["fill"])}" opacity="{region["opacity"]:.3f}"/>')
        parts.append(f'<text class="legend" x="{x + 38}" y="{cursor}">{esc(region["name"])}</text>')
        cursor += 24

    for note in spec["notes"]:
        for line in wrap_text(note, 32):
            parts.append(f'<text class="legend" x="{x}" y="{cursor}" fill="#4b5563">{esc(line)}</text>')
            cursor += 19
    return parts


def ticks(low: float, high: float, count: int) -> list[float]:
    if count <= 1:
        return [low, high]
    step = (high - low) / (count - 1)
    return [low + step * index for index in range(count)]


def format_tick(value: float) -> str:
    if abs(value) >= 100:
        return f"{value:.0f}"
    if abs(value) >= 10:
        return f"{value:.1f}"
    return f"{value:.2f}".rstrip("0").rstrip(".")


def wrap_text(text: str, width: int) -> Iterable[str]:
    current = ""
    for char in text:
        current += char
        if len(current) >= width:
            yield current
            current = ""
    if current:
        yield current


def write_csv(spec: dict[str, Any], path: Path) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(["type", "name", "sense", "x", "y", "source"])
        for item in spec["constraints"]:
            for x, y in item["points"]:
                writer.writerow(["constraint", item["name"], item["sense"], x, y, item.get("source", "")])
        for item in spec["regions"]:
            for x, y in item["points"]:
                writer.writerow(["region", item["name"], "", x, y, ""])
        for item in spec["design_points"]:
            writer.writerow(["design_point", item["name"], "", item["x"], item["y"], ""])


def esc(value: Any) -> str:
    return html.escape(str(value), quote=True)


if __name__ == "__main__":
    raise SystemExit(main())
