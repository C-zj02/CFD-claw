from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.skills.loader import clear_skill_registry
from src.tool_system.context import ToolContext
from src.tool_system.tools import SkillTool


DEFAULT_SOURCE = ROOT / ".clawd" / "generated" / "aircraft_conceptual_design_10q_answers.json"
DEFAULT_OUTPUT = ROOT / ".clawd" / "generated" / "aircraft_conceptual_design_10q_local_invocation_answers.json"


def _load_questions(path: Path) -> list[str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    questions = [item.get("question", "").strip() for item in payload if item.get("question")]
    if not questions:
        raise SystemExit(f"no questions found in {path}")
    return questions


def main() -> int:
    parser = argparse.ArgumentParser(description="Locally invoke aircraft-conceptual-design for 10 test questions.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    args = parser.parse_args()

    questions = _load_questions(args.source)
    ctx = ToolContext(workspace_root=ROOT, cwd=ROOT)
    tool = SkillTool()
    results: list[dict[str, str]] = []
    meta_items: list[dict[str, object]] = []

    clear_skill_registry()
    for idx, question in enumerate(questions, start=1):
        print(f"[{idx}/{len(questions)}] invoking: {question[:56]}", flush=True)
        output = tool.run({"skill": "aircraft-conceptual-design", "args": question}, ctx).output
        prompt = output.get("prompt", "") if isinstance(output, dict) else ""
        success = bool(output.get("success")) if isinstance(output, dict) else False
        answer = (
            "本地调用成功。"
            f"command={output.get('commandName', '')}; "
            f"loadedFrom={output.get('loadedFrom', '')}; "
            f"skillRoot={output.get('skillRoot', '')}; "
            f"prompt_has_question={question in prompt}; "
            f"prompt_has_rag_data={str(ROOT / 'RAG-data') in prompt}; "
            f"prompt_has_plot_script={'plot_constraint_boundary.py' in prompt}; "
            f"prompt_has_generated_dir={'.clawd/generated' in prompt}; "
            f"prompt_chars={len(prompt)}."
        )
        if not success:
            answer = f"本地调用失败。raw_output={output!r}"
        results.append({"question": question, "answer": answer})
        meta_items.append({
            "id": idx,
            "question": question,
            "success": success,
            "command_name": output.get("commandName", "") if isinstance(output, dict) else "",
            "loaded_from": output.get("loadedFrom", "") if isinstance(output, dict) else "",
            "skill_root": output.get("skillRoot", "") if isinstance(output, dict) else "",
            "prompt_chars": len(prompt),
            "prompt_has_question": question in prompt,
            "prompt_has_rag_data": str(ROOT / "RAG-data") in prompt,
            "prompt_has_plot_script": "plot_constraint_boundary.py" in prompt,
            "prompt_has_generated_dir": ".clawd/generated" in prompt,
        })

    args.output.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    meta_path = args.output.with_name(args.output.stem + "_meta.json")
    meta = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": str(args.source),
        "output": str(args.output),
        "skill": "aircraft-conceptual-design",
        "items": meta_items,
        "success_count": sum(1 for item in meta_items if item["success"]),
        "error_count": sum(1 for item in meta_items if not item["success"]),
    }
    meta_path.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"output = {args.output}")
    print(f"meta = {meta_path}")
    print(f"items = {len(results)}")
    print(f"success = {meta['success_count']}, errors = {meta['error_count']}")
    return 0 if meta["error_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
