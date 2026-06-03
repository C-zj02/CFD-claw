#!/usr/bin/env python3
"""Create a CFD evaluation case JSON from a bundled template."""

from __future__ import annotations

import argparse
import json
import re
from copy import deepcopy
from pathlib import Path
from typing import Any


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise SystemExit(f"expected JSON object in {path}")
    return data


def deep_merge(base: dict[str, Any], patch: dict[str, Any]) -> dict[str, Any]:
    result = deepcopy(base)
    for key, value in patch.items():
        if isinstance(value, dict) and isinstance(result.get(key), dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value
    return result


def set_path(data: dict[str, Any], dotted_path: str, value: Any) -> None:
    parts = dotted_path.split(".")
    cursor: dict[str, Any] = data
    for part in parts[:-1]:
        next_value = cursor.get(part)
        if not isinstance(next_value, dict):
            next_value = {}
            cursor[part] = next_value
        cursor = next_value
    cursor[parts[-1]] = value


def parse_value(raw: str) -> Any:
    lowered = raw.lower()
    if lowered == "null":
        return None
    if lowered == "true":
        return True
    if lowered == "false":
        return False
    try:
        if re.fullmatch(r"[-+]?\d+", raw):
            return int(raw)
        if re.fullmatch(r"[-+]?\d*\.\d+(e[-+]?\d+)?", raw, flags=re.IGNORECASE) or re.fullmatch(
            r"[-+]?\d+e[-+]?\d+", raw, flags=re.IGNORECASE
        ):
            return float(raw)
    except ValueError:
        pass
    if "," in raw:
        return [parse_value(item.strip()) for item in raw.split(",")]
    return raw


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--template", required=True, help="Path to template JSON")
    parser.add_argument("--case-id", required=True, help="Case identifier")
    parser.add_argument("--output", required=True, help="Output case JSON")
    parser.add_argument("--overrides", help="Optional JSON object with overrides")
    parser.add_argument(
        "--set",
        action="append",
        default=[],
        metavar="PATH=VALUE",
        help="Set a dotted field, for example flow_conditions.mach=0.8",
    )
    args = parser.parse_args()

    case = load_json(Path(args.template))
    case["case_id"] = args.case_id

    if args.overrides:
        override_data = json.loads(args.overrides)
        if not isinstance(override_data, dict):
            raise SystemExit("--overrides must be a JSON object")
        case = deep_merge(case, override_data)

    for item in args.set:
        if "=" not in item:
            raise SystemExit(f"--set expects PATH=VALUE, got {item!r}")
        path, raw_value = item.split("=", 1)
        set_path(case, path.strip(), parse_value(raw_value.strip()))

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    with output.open("w", encoding="utf-8") as handle:
        json.dump(case, handle, ensure_ascii=False, indent=2)
        handle.write("\n")
    print(f"wrote {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
