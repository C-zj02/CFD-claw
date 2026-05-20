from __future__ import annotations

import argparse
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
from src.config import get_provider_config, load_config
from src.providers.anthropic_provider import AnthropicProvider
from src.providers.glm_provider import GLMProvider
from src.providers.minimax_provider import MinimaxProvider
from src.providers.openai_provider import OpenAIProvider
from src.tool_system.agent_loop import (
    ToolEvent,
    run_agent_loop,
    summarize_tool_result,
    summarize_tool_use,
)
from src.tool_system.context import ToolContext
from src.tool_system.defaults import build_default_registry


DEFAULT_SOURCE = ROOT / ".clawd" / "generated" / "aircraft_conceptual_design_10q_answers.json"
DEFAULT_OUTPUT = ROOT / ".clawd" / "generated" / "aircraft_conceptual_design_10q_local_test_answers.json"


PROVIDERS = {
    "anthropic": AnthropicProvider,
    "openai": OpenAIProvider,
    "glm": GLMProvider,
    "minimax": MinimaxProvider,
}


def _load_questions(path: Path) -> list[str]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    questions = [item.get("question", "").strip() for item in payload if item.get("question")]
    if not questions:
        raise SystemExit(f"no questions found in {path}")
    return questions


def _write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    tmp.replace(path)


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


def _build_provider(provider_name: str, model: str | None):
    provider_config = get_provider_config(provider_name)
    api_key = provider_config.get("api_key")
    if not api_key:
        raise SystemExit(f"{provider_name} provider api_key is not configured")

    provider_cls = PROVIDERS[provider_name]
    selected_model = model or provider_config.get("default_model")
    kwargs = {
        "api_key": api_key,
        "base_url": provider_config.get("base_url"),
        "model": selected_model,
    }
    return provider_cls(**kwargs), selected_model


def main() -> int:
    parser = argparse.ArgumentParser(description="Run 10 aircraft conceptual design local-call tests.")
    parser.add_argument("--source", type=Path, default=DEFAULT_SOURCE, help="JSON file containing question/answer examples")
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT, help="Output JSON file in question/answer format")
    parser.add_argument("--provider", default=None, choices=sorted(PROVIDERS), help="Provider name; defaults to config default_provider")
    parser.add_argument("--model", default=None, help="Model name; defaults to provider config model")
    parser.add_argument("--limit", type=int, default=0, help="Only run the first N questions; 0 means all")
    parser.add_argument("--max-turns", type=int, default=6, help="Maximum tool turns per question")
    args = parser.parse_args()

    os.environ.setdefault("CLAWD_OPENAI_TIMEOUT", "300")
    questions = _load_questions(args.source)
    if args.limit > 0:
        questions = questions[: args.limit]

    provider_name = args.provider or load_config().get("default_provider", "openai")
    provider, model = _build_provider(provider_name, args.model)

    commands = {cmd.name: cmd for cmd in load_and_register_skills(project_root=ROOT)}
    command = commands["aircraft-conceptual-design"]
    command_context = CommandContext(
        workspace_root=ROOT,
        cwd=ROOT,
        conversation=None,
        cost_tracker=None,
        history=None,
    )
    tool_context = ToolContext(workspace_root=ROOT, cwd=ROOT)
    tool_registry = build_default_registry().filtered(command.allowed_tools)

    results: list[dict[str, str]] = []
    meta = {
        "created_at": datetime.now().isoformat(timespec="seconds"),
        "source": str(args.source),
        "provider": provider_name,
        "model": model,
        "skill": "aircraft-conceptual-design",
        "question_count": len(questions),
    }

    for idx, question in enumerate(questions, start=1):
        started = time.time()
        print(f"[{idx}/{len(questions)}] running: {question[:52]}", flush=True)

        process_lines = ["Assistant"]
        stream_chunks: list[str] = []

        def on_event(event: ToolEvent) -> None:
            line = _event_to_line(event)
            process_lines.append(line)
            print(line, flush=True)

        def on_text_chunk(chunk: str) -> None:
            if chunk:
                stream_chunks.append(chunk)

        try:
            prompt_blocks = asyncio.run(command.get_prompt_for_command(question, command_context))
            prompt_text = next(block.get("text", "") for block in prompt_blocks if block.get("type") == "text")

            conversation = Conversation(max_history=200)
            conversation.add_user_message(prompt_text)
            result = run_agent_loop(
                conversation=conversation,
                provider=provider,
                tool_registry=tool_registry,
                tool_context=tool_context,
                max_turns=max(1, args.max_turns),
                stream=True,
                verbose=False,
                on_event=on_event,
                on_text_chunk=on_text_chunk,
            )
            answer = result.response_text
        except Exception as exc:
            answer = f"ERROR: {exc!r}"
            print(answer, flush=True)

        results.append({"question": question, "answer": answer})
        _write_json(args.output, results)
        print(f"[{idx}/{len(questions)}] completed in {time.time() - started:.1f}s", flush=True)

    meta_path = args.output.with_name(args.output.stem + "_meta.json")
    meta["finished_at"] = datetime.now().isoformat(timespec="seconds")
    _write_json(args.output, results)
    _write_json(meta_path, meta)
    print(f"output = {args.output}", flush=True)
    print(f"meta = {meta_path}", flush=True)
    print(f"items = {len(results)}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
