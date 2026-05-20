from __future__ import annotations

import asyncio
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from src.agent.conversation import Conversation
from src.command_system.skills_integration import load_and_register_skills
from src.command_system.types import CommandContext
from src.config import get_provider_config
from src.providers.openai_provider import OpenAIProvider
from src.tool_system.agent_loop import (
    ToolEvent,
    run_agent_loop,
    summarize_tool_result,
    summarize_tool_use,
)
from src.tool_system.context import ToolContext
from src.tool_system.defaults import build_default_registry


QUESTIONS = [
    "设计一架航程1200km、载荷500kg的固定翼无人机，输出需求解析、任务剖面、总体参数、约束分析、布局方案和风险。",
    "在只给出航程1200km和载荷500kg的情况下，如何估算起飞重量、空机重量、燃油重量、翼面积和推重比？请给出V0到V2的闭合过程。",
    "如果这架无人机要求600m跑道起降，请重新做约束分析，并说明翼载荷、推重比、CLmax、起飞距离和着陆距离该如何调整。",
    "请设计一种适合长航程货运任务的无人机总体布局，并给出机翼、机身、尾翼、起落架、动力布置和三视图参数。",
    "请比较活塞、涡桨和混合电推进三种方案，选出最适合航程1200km、载荷500kg的无人机方案，并说明理由。",
    "如果巡航高度从5000m提高到8000m，请重新做任务剖面和主要性能校核，并说明关键参数会发生什么变化。",
    "如果载荷从500kg增加到800kg而航程不变，方案中最先受影响的约束是什么？请给出需要重新迭代的参数。",
    "请输出完整的方案界限线图，包含起飞、着陆、爬升和巡航约束，并给出推荐设计点、SVG路径和CSV路径。",
    "请只输出设计推理记录、依据检索、总体参数和校核结果，不要展开长篇解释。",
    "请把这架无人机设计成可工程落地的版本，明确哪些参数是用户输入、哪些是工程假设、哪些是计算结果，并说明主要风险与下一步验证。",
]


def _jsonable(value: Any) -> Any:
    try:
        json.dumps(value, ensure_ascii=False)
        return value
    except TypeError:
        return repr(value)


def _event_to_line(event: ToolEvent) -> str:
    if event.kind == "assistant_turn":
        turn = None
        if isinstance(event.tool_input, dict):
            turn = event.tool_input.get("turn")
        return f"• Assistant turn {turn or ''} integrating tool results...".strip()
    if event.kind == "tool_use":
        summary = summarize_tool_use(event.tool_name, event.tool_input or {})
        suffix = f" ({summary})" if summary else ""
        return f"• {event.tool_name}{suffix} running..."
    if event.kind == "tool_result":
        if event.is_error:
            return f"  ↳ Error: {event.tool_output}"
        return f"  ↳ {summarize_tool_result(event.tool_name, event.tool_output)}"
    if event.kind == "tool_error":
        return f"  ↳ {event.error or 'Error'}"
    return f"• {event.kind}: {event.tool_name}"


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


def main() -> int:
    os.environ.setdefault("CLAWD_OPENAI_TIMEOUT", "300")
    provider_config = get_provider_config("openai")
    model = "deepseek-v4-pro"
    if not provider_config.get("api_key"):
        raise SystemExit("openai provider api_key is not configured")

    commands = {cmd.name: cmd for cmd in load_and_register_skills(project_root=ROOT)}
    command = commands["aircraft-conceptual-design"]
    command_context = CommandContext(
        workspace_root=ROOT,
        cwd=ROOT,
        conversation=None,
        cost_tracker=None,
        history=None,
    )

    output_path = ROOT / ".clawd" / "generated" / "deepseek_aircraft_conceptual_design_10q_dataset.json"
    partial_path = ROOT / ".clawd" / "generated" / "deepseek_aircraft_conceptual_design_10q_dataset.partial.json"
    payload: dict[str, Any] = {
        "meta": {
            "created_at": datetime.now().isoformat(timespec="seconds"),
            "model": model,
            "provider": "openai",
            "skill": "aircraft-conceptual-design",
            "question_count": len(QUESTIONS),
            "max_turns": command.max_turns,
            "allowed_tools": list(command.allowed_tools),
            "captures": ["agent_process_output", "process_events", "streamed_text", "answer"],
        },
        "items": [],
    }

    for idx, question in enumerate(QUESTIONS, start=1):
        print(f"[{idx}/{len(QUESTIONS)}] running: {question[:42]}", flush=True)
        started = time.time()
        process_lines = ["Assistant"]
        process_events: list[dict[str, Any]] = []
        stream_chunks: list[str] = []

        def on_event(event: ToolEvent) -> None:
            line = _event_to_line(event)
            process_lines.append(line)
            print(line, flush=True)
            process_events.append({
                "kind": event.kind,
                "tool_name": event.tool_name,
                "tool_input": _jsonable(event.tool_input),
                "tool_output": _jsonable(event.tool_output),
                "tool_use_id": event.tool_use_id,
                "is_error": event.is_error,
                "error": event.error,
                "terminal_line": line,
            })

        def on_text_chunk(chunk: str) -> None:
            if chunk:
                stream_chunks.append(chunk)

        item: dict[str, Any] = {
            "id": idx,
            "question": question,
            "model": model,
            "skill": "aircraft-conceptual-design",
            "status": "running",
            "started_at": datetime.now().isoformat(timespec="seconds"),
        }

        try:
            prompt_blocks = asyncio.run(command.get_prompt_for_command(question, command_context))
            prompt_text = next(block.get("text", "") for block in prompt_blocks if block.get("type") == "text")
            conversation = Conversation(max_history=200)
            conversation.add_user_message(prompt_text)
            provider = OpenAIProvider(
                api_key=provider_config["api_key"],
                base_url=provider_config.get("base_url"),
                model=model,
            )
            tool_context = ToolContext(workspace_root=ROOT, cwd=ROOT)
            tool_registry = build_default_registry().filtered(command.allowed_tools)
            result = run_agent_loop(
                conversation=conversation,
                provider=provider,
                tool_registry=tool_registry,
                tool_context=tool_context,
                max_turns=max(1, int(command.max_turns or 20)),
                stream=True,
                verbose=False,
                on_event=on_event,
                on_text_chunk=on_text_chunk,
            )
            answer = result.response_text
            if stream_chunks:
                process_lines.append("")
                process_lines.append("Final streamed output:")
                process_lines.append("".join(stream_chunks))
            item.update({
                "status": "completed",
                "answer": answer,
                "agent_process_output": "\n".join(process_lines),
                "process_events": process_events,
                "streamed_text": "".join(stream_chunks),
                "usage": result.usage,
                "num_turns": result.num_turns,
                "duration_seconds": round(time.time() - started, 3),
            })
        except Exception as exc:
            line = f"Error: {exc}"
            process_lines.append(line)
            print(line, flush=True)
            item.update({
                "status": "error",
                "answer": "",
                "agent_process_output": "\n".join(process_lines),
                "process_events": process_events,
                "streamed_text": "".join(stream_chunks),
                "error": repr(exc),
                "duration_seconds": round(time.time() - started, 3),
            })

        payload["items"].append(item)
        _write_json(partial_path, payload)
        print(f"[{idx}/{len(QUESTIONS)}] {item['status']} in {item['duration_seconds']}s", flush=True)

    payload["meta"]["finished_at"] = datetime.now().isoformat(timespec="seconds")
    payload["meta"]["completed_count"] = sum(1 for item in payload["items"] if item["status"] == "completed")
    payload["meta"]["error_count"] = sum(1 for item in payload["items"] if item["status"] == "error")
    _write_json(output_path, payload)
    print(f"wrote {output_path}", flush=True)
    return 0 if payload["meta"]["error_count"] == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
