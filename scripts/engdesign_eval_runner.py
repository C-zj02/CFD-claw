#!/usr/bin/env python3
"""Standalone runner for EngDesign / EngDesign-Open evaluations.

This script intentionally lives outside ``src`` so it can be used as an
extra evaluation utility without becoming part of the Clawd runtime.
"""

from __future__ import annotations

import argparse
import json
import os
import shlex
import shutil
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


DEFAULT_OUTPUT_ROOT = Path(".clawd/generated/engdesign_eval_runs")


@dataclass
class RunConfig:
    engdesign_root: Path
    task_dir: Path
    output_dir: Path
    model: str
    api_key: str | None
    k: int
    task_list: list[str]
    reasoning_effort: str | None
    use_docker: bool
    docker_image: str
    use_xvfb: bool
    dry_run: bool
    rename_existing_logs: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run or summarize EngDesign-Open evaluations as a standalone project utility.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    run = subparsers.add_parser("run", help="Build and optionally run EngDesign evaluation command")
    add_common_args(run)
    run.add_argument("--model", required=True, help="EngDesign model name, e.g. deepseek-chat or gpt-4o")
    run.add_argument("--api-key", default=None, help="API key value. Prefer --api-key-env for shell history safety.")
    run.add_argument("--api-key-env", default=None, help="Environment variable containing the API key")
    run.add_argument("--k", type=int, default=1, help="Number of repetitions per task")
    run.add_argument("--task-list", nargs="*", default=[], help="Specific task ids, e.g. AB_01 AB_02")
    run.add_argument("--reasoning-effort", default=None, help="Optional reasoning effort, e.g. high")
    run.add_argument("--docker", action="store_true", help="Run through Docker instead of local Python")
    run.add_argument("--docker-image", default="engdesign-sim", help="Docker image name")
    run.add_argument("--no-xvfb", action="store_true", help="Do not prefix the command with xvfb-run")
    run.add_argument("--dry-run", action="store_true", help="Only write command and config; do not execute")
    run.add_argument(
        "--rename-existing-logs",
        action="store_true",
        help="Rename selected task logs folders before running to avoid mixing bundled and new logs",
    )

    summarize = subparsers.add_parser("summarize", help="Summarize existing EngDesign task logs")
    add_common_args(summarize)
    summarize.add_argument("--model", default=None, help="Only include logs containing this model name")
    summarize.add_argument("--task-list", nargs="*", default=[], help="Specific task ids to summarize")

    return parser.parse_args()


def add_common_args(parser: argparse.ArgumentParser) -> None:
    parser.add_argument(
        "--engdesign-root",
        required=True,
        type=Path,
        help="Path to the cloned AGI4Engineering/EngDesign repository",
    )
    parser.add_argument(
        "--task-dir",
        type=Path,
        default=None,
        help="Task directory. Defaults to <engdesign-root>/EngDesign-Open",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=None,
        help="Directory for run metadata and summary. Defaults to .clawd/generated/engdesign_eval_runs/<timestamp>",
    )


def default_api_key_env(model: str) -> str:
    lowered = model.lower()
    if "deepseek" in lowered:
        return "DEEPSEEK_API_KEY"
    if "gemini" in lowered:
        return "GEMINI_API_KEY"
    if "claude" in lowered:
        return "ANTHROPIC_API_KEY"
    return "OPENAI_API_KEY"


def resolve_output_dir(value: Path | None) -> Path:
    if value is not None:
        return value
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return DEFAULT_OUTPUT_ROOT / f"run_{stamp}"


def resolve_task_dir(root: Path, task_dir: Path | None) -> Path:
    if task_dir is not None:
        return task_dir
    preferred = root / "EngDesign-Open"
    if preferred.exists():
        return preferred
    return root / "tasks"


def validate_paths(root: Path, task_dir: Path, *, need_driver: bool) -> None:
    if not root.exists():
        raise SystemExit(f"EngDesign root does not exist: {root}")
    if not task_dir.exists():
        raise SystemExit(f"Task directory does not exist: {task_dir}")
    if need_driver and not (root / "evaluation" / "evaluate_llm.py").exists():
        raise SystemExit(f"Missing evaluation/evaluate_llm.py under: {root}")


def resolve_api_key(args: argparse.Namespace) -> tuple[str | None, str | None]:
    env_name = args.api_key_env or default_api_key_env(args.model)
    api_key = args.api_key or os.environ.get(env_name)
    return api_key, env_name


def selected_task_dirs(task_dir: Path, task_list: list[str]) -> list[Path]:
    if task_list:
        return [task_dir / task_id for task_id in task_list]
    return sorted(path for path in task_dir.iterdir() if path.is_dir() and not path.name.startswith("."))


def rename_logs(task_dirs: list[Path]) -> list[dict[str, str]]:
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    renamed: list[dict[str, str]] = []
    for task in task_dirs:
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


def eval_command(config: RunConfig, *, force_xvfb: bool = False) -> list[str]:
    command = [
        "python3",
        "evaluation/evaluate_llm.py",
        "--model",
        config.model,
        "--api_key",
        config.api_key or "",
        "--task_dir",
        relative_or_absolute(config.task_dir, config.engdesign_root),
        "--k",
        str(config.k),
    ]
    if config.task_list:
        command.extend(["--task_list", *config.task_list])
    if config.reasoning_effort:
        command.extend(["--reasoning_effort", config.reasoning_effort])

    if config.use_xvfb and (force_xvfb or shutil.which("xvfb-run")):
        return [
            "xvfb-run",
            "-a",
            "-e",
            "/dev/stdout",
            "--server-args=-screen 0 1024x768x24",
            *command,
        ]
    return command


def local_eval_command(config: RunConfig) -> list[str]:
    return eval_command(config, force_xvfb=False)


def docker_eval_command(config: RunConfig) -> list[str]:
    inner = shlex.join(eval_command(config, force_xvfb=True))
    return [
        "docker",
        "run",
        "--rm",
        "-v",
        f"{config.engdesign_root.resolve()}:/app",
        "-w",
        "/app",
        "--entrypoint",
        "bash",
        config.docker_image,
        "-lc",
        inner,
    ]


def relative_or_absolute(path: Path, root: Path) -> str:
    try:
        return str(path.resolve().relative_to(root.resolve()))
    except ValueError:
        return str(path)


def masked_command(command: list[str], api_key: str | None) -> str:
    masked = []
    for part in command:
        masked.append("***" if api_key and part == api_key else part)
    return shlex.join(masked)


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def run_command(command: list[str], cwd: Path, log_path: Path) -> int:
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("w", encoding="utf-8") as log:
        process = subprocess.Popen(
            command,
            cwd=str(cwd),
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
            bufsize=1,
        )
        assert process.stdout is not None
        for line in process.stdout:
            print(line, end="")
            log.write(line)
        return process.wait()


def run(args: argparse.Namespace) -> None:
    root = args.engdesign_root.resolve()
    task_dir = resolve_task_dir(root, args.task_dir).resolve()
    output_dir = resolve_output_dir(args.output_dir).resolve()
    validate_paths(root, task_dir, need_driver=True)
    api_key, api_key_env = resolve_api_key(args)
    if not api_key and not args.dry_run:
        raise SystemExit(f"No API key found. Pass --api-key or set {api_key_env}.")

    config = RunConfig(
        engdesign_root=root,
        task_dir=task_dir,
        output_dir=output_dir,
        model=args.model,
        api_key=api_key,
        k=args.k,
        task_list=list(args.task_list or []),
        reasoning_effort=args.reasoning_effort,
        use_docker=bool(args.docker),
        docker_image=args.docker_image,
        use_xvfb=not args.no_xvfb,
        dry_run=bool(args.dry_run),
        rename_existing_logs=bool(args.rename_existing_logs),
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    renamed = rename_logs(selected_task_dirs(task_dir, config.task_list)) if config.rename_existing_logs else []
    command = docker_eval_command(config) if config.use_docker else local_eval_command(config)

    write_json(
        output_dir / "run_config.json",
        {
            "engdesign_root": str(root),
            "task_dir": str(task_dir),
            "model": config.model,
            "api_key_env": api_key_env,
            "api_key_present": bool(api_key),
            "k": config.k,
            "task_list": config.task_list,
            "reasoning_effort": config.reasoning_effort,
            "use_docker": config.use_docker,
            "docker_image": config.docker_image,
            "use_xvfb": config.use_xvfb,
            "dry_run": config.dry_run,
            "renamed_logs": renamed,
        },
    )
    (output_dir / "command.txt").write_text(masked_command(command, api_key) + "\n", encoding="utf-8")
    print(f"Run directory: {output_dir}")
    print(f"Command: {masked_command(command, api_key)}")
    if config.dry_run:
        print("Dry run only; no evaluation was executed.")
        return

    exit_code = run_command(command, root, output_dir / "run.log")
    summary = summarize_logs(task_dir, model=config.model, task_list=config.task_list)
    summary["exit_code"] = exit_code
    write_json(output_dir / "summary.json", summary)
    if exit_code != 0:
        raise SystemExit(exit_code)


def summarize(args: argparse.Namespace) -> None:
    root = args.engdesign_root.resolve()
    task_dir = resolve_task_dir(root, args.task_dir).resolve()
    output_dir = resolve_output_dir(args.output_dir).resolve()
    validate_paths(root, task_dir, need_driver=False)
    summary = summarize_logs(task_dir, model=args.model, task_list=list(args.task_list or []))
    write_json(output_dir / "summary.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    print(f"Summary written to: {output_dir / 'summary.json'}")


def summarize_logs(task_dir: Path, *, model: str | None, task_list: list[str]) -> dict[str, Any]:
    tasks = selected_task_dirs(task_dir, task_list)
    rows = [summarize_task(task, model=model) for task in tasks]
    rows = [row for row in rows if row is not None]
    score_values = [
        score
        for row in rows
        for score in row.get("scores", [])
        if isinstance(score, (int, float))
    ]
    task_average_values = [
        row["average_score"] for row in rows if isinstance(row.get("average_score"), (int, float))
    ]
    passed_count = sum(int(row.get("passed_count", 0)) for row in rows)
    trial_count = sum(int(row.get("trial_count", 0)) for row in rows)
    return {
        "task_dir": str(task_dir),
        "model_filter": model,
        "task_count": len(rows),
        "trial_count": trial_count,
        "passed_count": passed_count,
        "scored_trial_count": len(score_values),
        "average_score": sum(score_values) / len(score_values) if score_values else None,
        "average_task_score": sum(task_average_values) / len(task_average_values) if task_average_values else None,
        "tasks": rows,
    }


def summarize_task(task: Path, *, model: str | None) -> dict[str, Any] | None:
    logs = task / "logs"
    if not logs.exists():
        return {
            "task_id": task.name,
            "latest_log_file": None,
            "trial_count": 0,
            "passed_count": 0,
            "scores": [],
            "average_score": None,
            "status": "no_logs",
            "trials": [],
        }
    candidates = sorted(logs.glob("*.jsonl"), key=lambda path: path.stat().st_mtime, reverse=True)
    if model:
        candidates = [path for path in candidates if model in path.name]
    if not candidates:
        return {
            "task_id": task.name,
            "latest_log_file": None,
            "trial_count": 0,
            "passed_count": 0,
            "scores": [],
            "average_score": None,
            "status": "no_matching_logs",
            "trials": [],
        }
    trials = []
    for log_file in candidates:
        parsed = read_jsonl(log_file)
        last = parsed[-1] if parsed else {}
        score = find_score(last)
        passed = find_bool(last, "passed")
        completion_tokens = find_number(last, "completion_tokens")
        trials.append(
            {
                "log_file": str(log_file),
                "line_count": len(parsed),
                "score": score,
                "passed": passed,
                "completion_tokens": completion_tokens,
                "status": "ok" if parsed else "empty_log",
                "last_record_keys": sorted(last.keys()) if isinstance(last, dict) else [],
            }
        )
    scores = [trial["score"] for trial in trials if isinstance(trial.get("score"), (int, float))]
    passed_values = [trial["passed"] for trial in trials if isinstance(trial.get("passed"), bool)]
    return {
        "task_id": task.name,
        "latest_log_file": trials[0]["log_file"] if trials else None,
        "trial_count": len(trials),
        "passed_count": sum(1 for passed in passed_values if passed),
        "scores": scores,
        "average_score": sum(scores) / len(scores) if scores else None,
        "status": "ok" if trials else "no_matching_logs",
        "trials": trials,
    }


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            data = json.loads(line)
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict):
            records.append(data)
    return records


def find_score(record: Any) -> float | None:
    if isinstance(record, dict):
        for key, value in record.items():
            lowered = str(key).lower()
            if "score" in lowered and isinstance(value, (int, float)):
                return float(value)
        for value in record.values():
            found = find_score(value)
            if found is not None:
                return found
    if isinstance(record, list):
        for item in record:
            found = find_score(item)
            if found is not None:
                return found
    return None


def find_bool(record: Any, target_key: str) -> bool | None:
    if isinstance(record, dict):
        for key, value in record.items():
            if str(key).lower() == target_key and isinstance(value, bool):
                return value
        for value in record.values():
            found = find_bool(value, target_key)
            if found is not None:
                return found
    if isinstance(record, list):
        for item in record:
            found = find_bool(item, target_key)
            if found is not None:
                return found
    return None


def find_number(record: Any, target_key: str) -> float | None:
    if isinstance(record, dict):
        for key, value in record.items():
            if str(key).lower() == target_key and isinstance(value, (int, float)):
                return float(value)
        for value in record.values():
            found = find_number(value, target_key)
            if found is not None:
                return found
    if isinstance(record, list):
        for item in record:
            found = find_number(item, target_key)
            if found is not None:
                return found
    return None


def main() -> int:
    args = parse_args()
    if args.command == "run":
        run(args)
    elif args.command == "summarize":
        summarize(args)
    else:
        raise SystemExit(f"Unknown command: {args.command}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
