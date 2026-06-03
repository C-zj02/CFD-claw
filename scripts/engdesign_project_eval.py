#!/usr/bin/env python3
"""Evaluate this project with official EngDesign task evaluators.

This is a bridge, not a replacement for EngDesign:
- prompts and ``evaluate.py`` come from a local clone of AGI4Engineering/EngDesign
- model calls go through this project's configured OpenAI-compatible provider
- logs are written in EngDesign-style ``<task>/logs/*.jsonl`` files
"""

from __future__ import annotations

import argparse
import ast
import importlib.util
import json
import multiprocessing
import os
import re
import sys
import time
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_ENGDESIGN_ROOT = ROOT.parent / "EngDesign"
DEFAULT_OUTPUT_ROOT = ROOT / ".clawd" / "generated" / "engdesign_project_eval_runs"

if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.config import get_provider_config
from src.providers.openai_provider import OpenAIProvider


@dataclass
class TaskSchema:
    config_fields: list[dict[str, str]]
    response_fields: list[dict[str, str]]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run official EngDesign tasks through this project's provider configuration.")
    parser.add_argument("--engdesign-root", type=Path, default=DEFAULT_ENGDESIGN_ROOT)
    parser.add_argument("--task-dir", type=Path, default=None, help="Defaults to <engdesign-root>/EngDesign-Open")
    parser.add_argument("--task-list", nargs="*", default=["ZH_02", "ZH_04"], help="Official EngDesign task ids")
    parser.add_argument("--provider", default="openai", help="Project provider name from ~/.clawd/config.json")
    parser.add_argument("--model", default=None, help="Override provider default model")
    parser.add_argument("--model-label", default=None, help="Label used in EngDesign logs")
    parser.add_argument("--output-dir", type=Path, default=None)
    parser.add_argument("--dry-run", action="store_true", help="Write prompts/config only; do not call the model")
    parser.add_argument("--temperature", type=float, default=0.0)
    parser.add_argument("--max-tokens", type=int, default=800)
    parser.add_argument("--request-timeout", type=float, default=60.0, help="Seconds allowed for each model call")
    parser.add_argument("--rename-existing-logs", action="store_true")
    parser.add_argument("--fail-below", type=float, default=None)
    return parser.parse_args()


def resolve_task_dir(root: Path, task_dir: Path | None) -> Path:
    if task_dir is not None:
        return task_dir
    return root / "EngDesign-Open"


def resolve_output_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return DEFAULT_OUTPUT_ROOT / f"run_{stamp}"


def selected_tasks(task_dir: Path, task_list: list[str]) -> list[Path]:
    if task_list:
        return [task_dir / task_id for task_id in task_list]
    return sorted(path for path in task_dir.iterdir() if path.is_dir() and not path.name.startswith("."))


def validate_task(task: Path) -> None:
    missing = [
        path
        for path in [task / "LLM_prompt.txt", task / "output_structure.py", task / "evaluate.py"]
        if not path.exists()
    ]
    if missing:
        raise SystemExit("Missing EngDesign task files:\n" + "\n".join(str(path) for path in missing))


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


def parse_schema(output_structure_path: Path) -> TaskSchema:
    tree = ast.parse(output_structure_path.read_text(encoding="utf-8"))
    config_fields = fields_for_class(tree, "ConfigFile")
    response_fields = fields_for_class(tree, "Response_structure")
    return TaskSchema(config_fields=config_fields, response_fields=response_fields)


def fields_for_class(tree: ast.AST, class_name: str) -> list[dict[str, str]]:
    fields = []
    for node in ast.walk(tree):
        if not isinstance(node, ast.ClassDef) or node.name != class_name:
            continue
        for stmt in node.body:
            if isinstance(stmt, ast.AnnAssign) and isinstance(stmt.target, ast.Name):
                fields.append(
                    {
                        "name": stmt.target.id,
                        "type": ast.unparse(stmt.annotation) if hasattr(ast, "unparse") else "Any",
                        "description": field_description(stmt.value),
                    }
                )
    return fields


def field_description(value: ast.AST | None) -> str:
    if not isinstance(value, ast.Call):
        return ""
    for keyword in value.keywords:
        if keyword.arg == "description" and isinstance(keyword.value, ast.Constant):
            return str(keyword.value.value)
    return ""


def build_prompt(task: Path, schema: TaskSchema) -> str:
    task_prompt = (task / "LLM_prompt.txt").read_text(encoding="utf-8").strip()
    config_lines = []
    for field in schema.config_fields:
        desc = f" - {field['description']}" if field["description"] else ""
        config_lines.append(f'- "{field["name"]}" ({field["type"]}){desc}')
    if not config_lines:
        for field in schema.response_fields:
            if field["name"] != "reasoning":
                desc = f" - {field['description']}" if field["description"] else ""
                config_lines.append(f'- "{field["name"]}" ({field["type"]}){desc}')
    schema_hint = "\n".join(config_lines)
    return f"""You are being evaluated on an official EngDesign task.

Solve the task and return ONLY valid JSON. The first character of your response must be "{{".
Do not include Markdown fences. Do not write prose outside the JSON object.
Keep "reasoning" under 80 English words and put all reasoning inside the JSON string.

Required JSON shape:
{{
  "reasoning": "brief but sufficient engineering reasoning",
  "config": {{
    ... fill every required config field listed below ...
  }}
}}

Required config fields:
{schema_hint}

Official EngDesign task prompt:
{task_prompt}

Return only the JSON object now.
"""


def create_provider(provider_name: str, model_override: str | None) -> tuple[OpenAIProvider, str, str]:
    config = get_provider_config(provider_name)
    api_key = config.get("api_key")
    if not api_key:
        raise SystemExit(f"Provider {provider_name!r} has no configured api_key")
    model = model_override or config.get("default_model") or "deepseek-v4-pro"
    if provider_name != "openai":
        raise SystemExit("This bridge currently supports the project's OpenAI-compatible provider only.")
    provider = OpenAIProvider(api_key=api_key, base_url=config.get("base_url"), model=model)
    return provider, model, config.get("base_url") or ""


def call_project_provider_direct(provider: OpenAIProvider, prompt: str, *, temperature: float, max_tokens: int) -> tuple[str, dict[str, Any]]:
    response = provider.chat(
        [
                {
                    "role": "system",
                    "content": "You are a precise engineering design solver. Return only valid JSON. The first character must be { and there must be no prose outside JSON.",
                },
            {"role": "user", "content": prompt},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return (response.content or response.reasoning_content or ""), response.usage


def provider_worker(queue: Any, provider_name: str, model: str, prompt: str, temperature: float, max_tokens: int) -> None:
    try:
        provider, _, _ = create_provider(provider_name, model)
        raw_text, usage = call_project_provider_direct(provider, prompt, temperature=temperature, max_tokens=max_tokens)
        queue.put({"ok": True, "raw_text": raw_text, "usage": usage})
    except BaseException as exc:
        queue.put({"ok": False, "error": repr(exc)})


def call_project_provider_isolated(provider_name: str, model: str, prompt: str, *, temperature: float, max_tokens: int, request_timeout: float) -> tuple[str, dict[str, Any]]:
    ctx = multiprocessing.get_context("spawn")
    queue: Any = ctx.Queue()
    process = ctx.Process(target=provider_worker, args=(queue, provider_name, model, prompt, temperature, max_tokens))
    process.start()
    process.join(request_timeout)
    if process.is_alive():
        process.terminate()
        process.join(5)
        raise TimeoutError(f"model call exceeded {request_timeout:g}s")
    if queue.empty():
        raise RuntimeError(f"model worker exited without a result, exitcode={process.exitcode}")
    payload = queue.get()
    if not payload.get("ok"):
        raise RuntimeError(payload.get("error", "model worker failed"))
    return str(payload["raw_text"]), dict(payload.get("usage") or {})


def extract_json_object(text: str) -> dict[str, Any]:
    fenced = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", text, re.DOTALL)
    candidates = [fenced.group(1)] if fenced else []
    candidates.append(text)
    decoder = json.JSONDecoder()
    for candidate in candidates:
        for start in [match.start() for match in re.finditer(r"\{", candidate)]:
            try:
                obj, _ = decoder.raw_decode(candidate[start:])
            except json.JSONDecodeError:
                continue
            if isinstance(obj, dict):
                return obj
    raise ValueError("No valid JSON object found in model response")


def namespace(value: Any) -> Any:
    if isinstance(value, dict):
        return SimpleNamespace(**{key: namespace(item) for key, item in value.items()})
    if isinstance(value, list):
        return [namespace(item) for item in value]
    return value


def response_object(parsed: dict[str, Any]) -> Any:
    if "config" not in parsed:
        parsed = {"reasoning": parsed.get("reasoning", ""), "config": {k: v for k, v in parsed.items() if k != "reasoning"}}
    return namespace(parsed)


def import_evaluator(task: Path) -> Any:
    path = task / "evaluate.py"
    spec = importlib.util.spec_from_file_location(f"engdesign_{task.name}_evaluate", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot import evaluator: {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def evaluate_with_official_task(task: Path, parsed: dict[str, Any]) -> tuple[bool, Any, Any, Any]:
    module = import_evaluator(task)
    old_cwd = Path.cwd()
    try:
        os.chdir(task)
        return module.evaluate_llm_response(response_object(parsed))
    finally:
        os.chdir(old_cwd)


def write_task_log(task: Path, model_label: str, trial_index: int, entry: dict[str, Any]) -> Path:
    logs = task / "logs"
    logs.mkdir(parents=True, exist_ok=True)
    path = logs / f"{task.name}_log_{model_label}_{trial_index}.jsonl"
    path.write_text(json.dumps(entry, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def run_task(task: Path, provider_name: str, model: str, model_label: str, trial_index: int, *, dry_run: bool, temperature: float, max_tokens: int, request_timeout: float, output_dir: Path) -> dict[str, Any]:
    validate_task(task)
    schema = parse_schema(task / "output_structure.py")
    prompt = build_prompt(task, schema)
    (output_dir / "prompts").mkdir(parents=True, exist_ok=True)
    (output_dir / "prompts" / f"{task.name}.txt").write_text(prompt, encoding="utf-8")
    if dry_run:
        return {
            "task_id": task.name,
            "status": "dry_run",
            "score": None,
            "passed": False,
            "prompt_file": str(output_dir / "prompts" / f"{task.name}.txt"),
        }

    started = time.time()
    raw_text, usage = call_project_provider_isolated(
        provider_name,
        model,
        prompt,
        temperature=temperature,
        max_tokens=max_tokens,
        request_timeout=request_timeout,
    )
    raw_dir = output_dir / "raw_responses"
    raw_dir.mkdir(parents=True, exist_ok=True)
    raw_response_file = raw_dir / f"{task.name}.txt"
    raw_response_file.write_text(raw_text, encoding="utf-8")
    try:
        parsed = extract_json_object(raw_text)
    except Exception as exc:
        entry = {
            "completion_tokens": usage.get("output_tokens", 0),
            "response": "",
            "raw_response": raw_text,
            "passed": False,
            "evaluation_result": {"error": f"parse_error: {exc}"},
            "score": None,
            "confidence": None,
        }
        log_file = write_task_log(task, model_label, trial_index, entry)
        return {
            "task_id": task.name,
            "status": "parse_error",
            "passed": False,
            "score": None,
            "error": repr(exc),
            "usage": usage,
            "duration_seconds": round(time.time() - started, 3),
            "log_file": str(log_file),
            "prompt_file": str(output_dir / "prompts" / f"{task.name}.txt"),
            "raw_response_file": str(raw_response_file),
        }
    passed, detailed_result, score, confidence = evaluate_with_official_task(task, parsed)
    entry = {
        "completion_tokens": usage.get("output_tokens", 0),
        "response": json.dumps(parsed, ensure_ascii=False),
        "raw_response": raw_text,
        "passed": bool(passed),
        "evaluation_result": detailed_result,
        "score": score,
        "confidence": confidence,
    }
    log_file = write_task_log(task, model_label, trial_index, entry)
    return {
        "task_id": task.name,
        "status": "ok",
        "passed": bool(passed),
        "score": score,
        "confidence": confidence,
        "usage": usage,
        "duration_seconds": round(time.time() - started, 3),
        "log_file": str(log_file),
        "prompt_file": str(output_dir / "prompts" / f"{task.name}.txt"),
        "raw_response_file": str(raw_response_file),
        "evaluation_result": detailed_result,
        "parsed_response": parsed,
    }


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def jsonable_args(args: argparse.Namespace) -> dict[str, Any]:
    payload = {}
    for key, value in vars(args).items():
        payload[key] = str(value) if isinstance(value, Path) else value
    return payload


def render_report(summary: dict[str, Any]) -> str:
    lines = [
        "# 使用官方 EngDesign 评估本项目",
        "",
        f"- 运行时间：{summary['created_at']}",
        f"- EngDesign：`{summary['engdesign_root']}`",
        f"- 模型：`{summary['model']}`",
        f"- 平均分：{summary['average_score']}",
        f"- 通过数：{summary['passed_count']} / {summary['task_count']}",
        "",
        "| Task | Score | Passed | Status | Log |",
        "|---|---:|:---:|---|---|",
    ]
    for row in summary["tasks"]:
        lines.append(f"| {row['task_id']} | {row.get('score')} | {'是' if row.get('passed') else '否'} | {row['status']} | `{row.get('log_file', '')}` |")
    lines.append("")
    lines.append("说明：任务 prompt 与 evaluator 来自官方 EngDesign；模型调用走本项目配置的 OpenAI-compatible provider。")
    return "\n".join(lines) + "\n"


def main() -> int:
    args = parse_args()
    engdesign_root = args.engdesign_root.resolve()
    task_dir = resolve_task_dir(engdesign_root, args.task_dir).resolve()
    output_dir = resolve_output_dir(args.output_dir).resolve()
    tasks = selected_tasks(task_dir, list(args.task_list or []))
    if not engdesign_root.exists():
        raise SystemExit(f"EngDesign root does not exist: {engdesign_root}")
    if not task_dir.exists():
        raise SystemExit(f"EngDesign task dir does not exist: {task_dir}")
    if not tasks:
        raise SystemExit("No EngDesign tasks selected")

    output_dir.mkdir(parents=True, exist_ok=True)
    renamed = rename_logs(tasks) if args.rename_existing_logs else []
    model = args.model or ""
    base_url = ""
    if not args.dry_run:
        os.environ["CLAWD_OPENAI_TIMEOUT"] = str(args.request_timeout)
        _, model, base_url = create_provider(args.provider, args.model)
    else:
        config = get_provider_config(args.provider)
        model = args.model or config.get("default_model") or "deepseek-v4-pro"
        base_url = config.get("base_url") or ""
    model_label = args.model_label or model.replace("/", "_").replace(":", "_")

    rows = []
    for index, task in enumerate(tasks):
        print(f"[{index + 1}/{len(tasks)}] {task.name}", flush=True)
        try:
            rows.append(
                run_task(
                    task,
                    args.provider,
                    model,
                    model_label,
                    index,
                    dry_run=bool(args.dry_run),
                    temperature=float(args.temperature),
                    max_tokens=int(args.max_tokens),
                    request_timeout=float(args.request_timeout),
                    output_dir=output_dir,
                )
            )
        except Exception as exc:
            rows.append({"task_id": task.name, "status": "error", "passed": False, "score": None, "error": repr(exc)})
            print(f"  error: {exc}", flush=True)

    numeric_scores = [float(row["score"]) for row in rows if isinstance(row.get("score"), (int, float))]
    summary = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "engdesign_root": str(engdesign_root),
        "task_dir": str(task_dir),
        "task_list": [task.name for task in tasks],
        "provider": args.provider,
        "base_url": base_url,
        "model": model,
        "model_label": model_label,
        "dry_run": bool(args.dry_run),
        "renamed_logs": renamed,
        "task_count": len(rows),
        "scored_task_count": len(numeric_scores),
        "passed_count": sum(1 for row in rows if row.get("passed")),
        "average_score": round(sum(numeric_scores) / len(numeric_scores), 2) if numeric_scores else None,
        "tasks": rows,
    }
    write_json(output_dir / "summary.json", summary)
    write_json(output_dir / "run_config.json", jsonable_args(args) | {"engdesign_root": str(engdesign_root), "task_dir": str(task_dir)})
    (output_dir / "report.md").write_text(render_report(summary), encoding="utf-8")
    print(f"average_score = {summary['average_score']}")
    print(f"passed = {summary['passed_count']}/{summary['task_count']}")
    print(f"summary = {output_dir / 'summary.json'}")
    print(f"report = {output_dir / 'report.md'}")
    if args.fail_below is not None and numeric_scores and summary["average_score"] < args.fail_below:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
