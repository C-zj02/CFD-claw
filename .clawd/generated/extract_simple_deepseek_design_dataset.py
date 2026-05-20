from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / ".clawd" / "generated" / "deepseek_aircraft_conceptual_design_10q_dataset.partial.json"
FINAL_SOURCE = ROOT / ".clawd" / "generated" / "deepseek_aircraft_conceptual_design_10q_dataset.json"
OUTPUT = ROOT / ".clawd" / "generated" / "deepseek_aircraft_conceptual_design_10q_simple.json"


def main() -> int:
    source = FINAL_SOURCE if FINAL_SOURCE.exists() else SOURCE
    if not source.exists():
        raise SystemExit(f"source dataset not found: {source}")

    payload = json.loads(source.read_text(encoding="utf-8"))
    items = []
    for item in payload.get("items", []):
        if item.get("status") != "completed":
            continue
        items.append({
            "question": item.get("question", ""),
            "answer": item.get("answer", ""),
            "agent_process_output": item.get("agent_process_output", ""),
        })

    OUTPUT.write_text(json.dumps(items, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"source = {source}")
    print(f"output = {OUTPUT}")
    print(f"items = {len(items)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
