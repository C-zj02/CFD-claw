from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DEFAULT_SOURCE = ROOT / ".clawd" / "generated" / "deepseek_aircraft_conceptual_design_10q_dataset.partial.json"
DEFAULT_OUTPUT = ROOT / ".clawd" / "generated" / "aircraft_conceptual_design_10q_local_generated_answers.json"


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract question/answer pairs from an aircraft design run dataset.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    payload = json.loads(args.source.read_text(encoding="utf-8"))
    items = []
    for item in payload.get("items", []):
        if item.get("status") != "completed":
            continue
        items.append({
            "question": item.get("question", ""),
            "answer": item.get("answer", ""),
        })

    args.output.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"source = {args.source}")
    print(f"output = {args.output}")
    print(f"items = {len(items)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
