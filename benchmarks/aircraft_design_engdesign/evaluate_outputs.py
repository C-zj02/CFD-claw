#!/usr/bin/env python3
from __future__ import annotations

import argparse
import importlib.util
import json
import shutil
from datetime import datetime
from pathlib import Path
from typing import Any


BENCHMARK_ROOT = Path(__file__).resolve().parent
PROJECT_ROOT = BENCHMARK_ROOT.parents[1]
DEFAULT_TASK_DIR = BENCHMARK_ROOT / "tasks"
DEFAULT_SOURCE = PROJECT_ROOT / ".clawd" / "generated" / "aircraft_conceptual_design_10q_answers.json"
DEFAULT_OUTPUT_ROOT = PROJECT_ROOT / ".clawd" / "generated" / "local_engdesign_eval_runs"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Evaluate local aircraft design outputs in an EngDesign-style task layout.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="JSON answers to evaluate")
    parser.add_argument("--task-dir", type=Path, default=DEFAULT_TASK_DIR, help="EngDesign-style task directory")
    parser.add_argument("--task-list", nargs="*", default=[], help="Specific task ids, e.g. AD_01 AD_02")
    parser.add_argument("--model-label", default="local-project", help="Label used in task logs")
    parser.add_argument("--output-dir", type=Path, default=None, help="Run metadata output directory")
    parser.add_argument("--rename-existing-logs", action="store_true", help="Rename task logs before writing new logs")
    parser.add_argument("--fail-below", type=float, default=None, help="Exit non-zero if average score is below this")
    return parser.parse_args()


def resolve_output_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return DEFAULT_OUTPUT_ROOT / f"run_{stamp}"


def load_json_items(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        raise SystemExit(f"source file does not exist: {path}")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(payload, list):
        raw_items = payload
    elif isinstance(payload, dict) and isinstance(payload.get("items"), list):
        raw_items = payload["items"]
    else:
        raise SystemExit(f"unsupported source JSON shape: {path}")
    return [item for item in raw_items if isinstance(item, dict)]


def selected_tasks(task_dir: Path, task_list: list[str]) -> list[Path]:
    if task_list:
        return [task_dir / task_id for task_id in task_list]
    return sorted(path for path in task_dir.iterdir() if path.is_dir() and not path.name.startswith("."))


def rename_logs(tasks: list[Path]) -> list[dict[str, str]]:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    renamed = []
    for task in tasks:
        logs = task / "logs"
        if not logs.exists():
            continue
        target = task / f"logs_baseline_{stamp}"
        index = 1
        while target.exists():
            target = task / f"logs_baseline_{stamp}_{index}"
            index += 1
        logs.rename(target)
        renamed.append({"task": task.name, "from": str(logs), "to": str(target)})
    return renamed


def task_prompt(task: Path) -> str:
    return (task / "LLM_prompt.txt").read_text(encoding="utf-8").strip()


def build_answer_lookup(items: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    lookup = {}
    for item in items:
        question = str(item.get("question", "")).strip()
        if question:
            lookup[normalize(question)] = item
    return lookup


def normalize(value: str) -> str:
    return " ".join(value.split())


def import_module(path: Path, name: str) -> Any:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import module: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def response_object(task: Path, item: dict[str, Any]) -> Any:
    structure_path = task / "output_structure.py"
    module = import_module(structure_path, f"{task.name}_output_structure")
    cls = module.Response_structure
    return cls(
        answer=str(item.get("answer", "") or ""),
        agent_process_output=str(item.get("agent_process_output", "") or ""),
    )


def write_task_log(task: Path, model_label: str, trial_index: int, entry: dict[str, Any]) -> Path:
    log_dir = task / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = log_dir / f"{task.name}_log_{model_label}_{trial_index}.jsonl"
    log_file.write_text(json.dumps(entry, ensure_ascii=False) + "\n", encoding="utf-8")
    return log_file


def evaluate_task(task: Path, item: dict[str, Any] | None, model_label: str, trial_index: int) -> dict[str, Any]:
    if item is None:
        entry = {
            "completion_tokens": 0,
            "response": "",
            "passed": False,
            "evaluation_result": {"error": "missing_answer_for_task", "task_id": task.name},
            "score": 0.0,
        }
        log_file = write_task_log(task, model_label, trial_index, entry)
        return {
            "task_id": task.name,
            "question": task_prompt(task),
            "status": "missing_answer",
            "passed": False,
            "score": 0.0,
            "log_file": str(log_file),
        }

    evaluator = import_module(task / "evaluate.py", f"{task.name}_evaluate")
    response = response_object(task, item)
    passed, detailed_result, score, _ = evaluator.evaluate_llm_response(response)
    entry = {
        "completion_tokens": 0,
        "response": getattr(response, "answer", ""),
        "passed": bool(passed),
        "evaluation_result": detailed_result,
        "score": score,
    }
    log_file = write_task_log(task, model_label, trial_index, entry)
    return {
        "task_id": task.name,
        "question": task_prompt(task),
        "status": "ok",
        "passed": bool(passed),
        "score": score,
        "log_file": str(log_file),
        "evaluation_result": detailed_result,
    }


def render_report(summary: dict[str, Any]) -> str:
    lines = [
        "# EngDesign-style 本机飞行器设计评测报告",
        "",
        f"- 运行时间：{summary['created_at']}",
        f"- 数据文件：`{summary['source']}`",
        f"- 任务目录：`{summary['task_dir']}`",
        f"- 平均分：{summary['average_score']}",
        f"- 通过数：{summary['passed_count']} / {summary['task_count']}",
        "",
        "| Task | Score | Passed | Status | Log |",
        "|---|---:|:---:|---|---|",
    ]
    for row in summary["tasks"]:
        lines.append(
            f"| {row['task_id']} | {row['score']} | {'是' if row['passed'] else '否'} | {row['status']} | `{row['log_file']}` |"
        )
    lines.extend(
        [
            "",
            "## 说明",
            "",
            "该评测按 EngDesign 的任务组织方式落盘：每个任务包含 `LLM_prompt.txt`、`output_structure.py`、`evaluate.py` 和 `logs/*.jsonl`。当前驱动评测的是本机已保存回答，不直接调用模型 API。",
        ]
    )
    return "\n".join(lines) + "\n"


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def main() -> int:
    args = parse_args()
    source = args.source.resolve()
    task_dir = args.task_dir.resolve()
    output_dir = resolve_output_dir(args.output_dir).resolve()
    tasks = selected_tasks(task_dir, list(args.task_list or []))
    if not tasks:
        raise SystemExit(f"no tasks found under: {task_dir}")
    missing_task_files = [
        str(path)
        for task in tasks
        for path in [task / "LLM_prompt.txt", task / "output_structure.py", task / "evaluate.py", task / "rubric.json"]
        if not path.exists()
    ]
    if missing_task_files:
        raise SystemExit("missing task files:\n" + "\n".join(missing_task_files))

    output_dir.mkdir(parents=True, exist_ok=True)
    renamed = rename_logs(tasks) if args.rename_existing_logs else []
    items = load_json_items(source)
    by_question = build_answer_lookup(items)
    rows = []
    for index, task in enumerate(tasks):
        prompt = task_prompt(task)
        item = by_question.get(normalize(prompt))
        if item is None and index < len(items):
            item = items[index]
        rows.append(evaluate_task(task, item, args.model_label, index))

    scores = [float(row["score"]) for row in rows]
    summary = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": str(source),
        "task_dir": str(task_dir),
        "model_label": args.model_label,
        "task_count": len(rows),
        "passed_count": sum(1 for row in rows if row["passed"]),
        "failed_count": sum(1 for row in rows if not row["passed"]),
        "average_score": round(sum(scores) / len(scores), 2) if scores else 0.0,
        "min_score": min(scores) if scores else 0.0,
        "max_score": max(scores) if scores else 0.0,
        "renamed_logs": renamed,
        "tasks": rows,
    }
    write_json(output_dir / "summary.json", summary)
    (output_dir / "report.md").write_text(render_report(summary), encoding="utf-8")
    shutil.copy2(source, output_dir / "source_answers.json")
    write_json(
        output_dir / "run_config.json",
        {
            "source": str(source),
            "task_dir": str(task_dir),
            "task_list": list(args.task_list or []),
            "model_label": args.model_label,
            "rename_existing_logs": bool(args.rename_existing_logs),
        },
    )

    print(f"tasks = {summary['task_count']}")
    print(f"average_score = {summary['average_score']}")
    print(f"passed = {summary['passed_count']}/{summary['task_count']}")
    print(f"summary = {output_dir / 'summary.json'}")
    print(f"report = {output_dir / 'report.md'}")
    if args.fail_below is not None and summary["average_score"] < args.fail_below:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
