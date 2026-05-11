"""Explicit trace-to-skill memory support."""

from __future__ import annotations

import json
import re
import shutil
import threading
import uuid
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from .providers.base import BaseProvider


DEFAULT_TRACE_DIR = ".clawd/traces"
DEFAULT_CANDIDATE_DIR = ".clawd/skill-candidates"
DEFAULT_PROJECT_SKILLS_DIR = ".clawd/skills"


def get_default_skill_memory_config() -> dict[str, Any]:
    return {
        "enabled": True,
        "default_mode": "off",
        "trace_level": "full",
        "postprocess": "background",
        "trace_dir": DEFAULT_TRACE_DIR,
        "candidate_dir": DEFAULT_CANDIDATE_DIR,
    }


def skill_memory_config(config: dict[str, Any] | None = None) -> dict[str, Any]:
    cfg = get_default_skill_memory_config()
    if isinstance(config, dict):
        raw = config.get("skill_memory")
        if isinstance(raw, dict):
            cfg.update(raw)
    return cfg


@dataclass
class TraceRecorder:
    workspace_root: Path
    session_id: str
    task: str
    provider_name: str
    model: str
    trace_level: str = "full"
    trace_dir: str = DEFAULT_TRACE_DIR
    trace_id: str = field(default_factory=lambda: f"{datetime.now().strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}")
    started_at: str = field(default_factory=lambda: datetime.now().isoformat())
    events: list[dict[str, Any]] = field(default_factory=list)

    def record_event(self, event: Any) -> None:
        payload = {
            "timestamp": datetime.now().isoformat(),
            "kind": getattr(event, "kind", None),
            "tool_name": getattr(event, "tool_name", None),
            "tool_input": getattr(event, "tool_input", None),
            "tool_output": getattr(event, "tool_output", None),
            "tool_use_id": getattr(event, "tool_use_id", None),
            "is_error": getattr(event, "is_error", False),
            "error": getattr(event, "error", None),
        }
        self.events.append(_json_safe(payload))

    def record_direct_response(self, text: str) -> None:
        self.events.append(_json_safe({
            "timestamp": datetime.now().isoformat(),
            "kind": "direct_response",
            "content": text,
        }))

    def finish(
        self,
        *,
        status: str,
        final_response: str = "",
        error: str | None = None,
        conversation: dict[str, Any] | None = None,
    ) -> Path:
        trace_path = self.path
        trace_path.parent.mkdir(parents=True, exist_ok=True)
        data = {
            "trace_id": self.trace_id,
            "session_id": self.session_id,
            "task": self.task,
            "started_at": self.started_at,
            "ended_at": datetime.now().isoformat(),
            "provider": self.provider_name,
            "model": self.model,
            "trace_level": self.trace_level,
            "events": self.events,
            "conversation": conversation or {},
            "final_response": final_response,
            "status": status,
            "error": error,
            "postprocess": {"status": "pending"},
        }
        trace_path.write_text(json.dumps(_json_safe(data), indent=2, ensure_ascii=False), encoding="utf-8")
        return trace_path

    @property
    def path(self) -> Path:
        return self.workspace_root / self.trace_dir / f"{self.trace_id}.json"


def process_trace_to_candidate(
    *,
    trace_path: str | Path,
    provider: BaseProvider,
    model: str,
    workspace_root: str | Path,
    candidate_dir: str = DEFAULT_CANDIDATE_DIR,
) -> dict[str, Any]:
    root = Path(workspace_root).expanduser().resolve()
    path = Path(trace_path).expanduser().resolve()
    trace = json.loads(path.read_text(encoding="utf-8"))

    try:
        if _trace_used_existing_skill(trace):
            return _mark_trace(path, trace, {"status": "skipped_existing_skill", "reason": "Trace used an existing Skill tool."})

        evaluation = _generate_skill_candidate(trace, provider, model)

        skill_name = _sanitize_skill_name(str(evaluation.get("skill_name") or "learned-skill"))
        candidate_id = f"{trace.get('trace_id', uuid.uuid4().hex[:8])}_{skill_name}"
        candidate_root = root / candidate_dir / candidate_id
        candidate_root.mkdir(parents=True, exist_ok=True)

        skill_content = _render_candidate_skill(
            description=str(evaluation.get("description") or f"Learned workflow: {skill_name}"),
            when_to_use=str(evaluation.get("when_to_use") or ""),
            body=str(evaluation.get("body") or ""),
        )
        (candidate_root / "SKILL.md").write_text(skill_content, encoding="utf-8")
        metadata = {
            "id": candidate_id,
            "status": "pending",
            "created_at": datetime.now().isoformat(),
            "trace_path": str(path),
            "skill_name": skill_name,
            "description": str(evaluation.get("description") or ""),
            "reason": str(evaluation.get("reason") or ""),
            "confidence": evaluation.get("confidence"),
            "generation_mode": "explicit_learn",
        }
        (candidate_root / "metadata.json").write_text(
            json.dumps(_json_safe(metadata), indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        _mark_trace(path, trace, {"status": "candidate_created", "candidate_id": candidate_id})
        return metadata
    except Exception as exc:
        return _mark_trace(path, trace, {"status": "failed", "error": str(exc)})


def process_trace_to_candidate_background(**kwargs: Any) -> threading.Thread:
    thread = threading.Thread(
        target=process_trace_to_candidate,
        kwargs=kwargs,
        name="clawd-skill-memory",
        daemon=True,
    )
    thread.start()
    return thread


def list_candidates(workspace_root: str | Path, candidate_dir: str = DEFAULT_CANDIDATE_DIR) -> list[dict[str, Any]]:
    base = Path(workspace_root).expanduser().resolve() / candidate_dir
    if not base.exists():
        return []
    items: list[dict[str, Any]] = []
    for entry in sorted(base.iterdir()):
        if not entry.is_dir():
            continue
        metadata_path = entry / "metadata.json"
        if not metadata_path.exists():
            continue
        try:
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        except Exception:
            continue
        metadata["_path"] = str(entry)
        items.append(metadata)
    return items


def get_candidate(
    workspace_root: str | Path,
    candidate_id: str,
    candidate_dir: str = DEFAULT_CANDIDATE_DIR,
) -> tuple[Path, dict[str, Any], str]:
    base = Path(workspace_root).expanduser().resolve() / candidate_dir / candidate_id
    metadata_path = base / "metadata.json"
    skill_path = base / "SKILL.md"
    if not metadata_path.exists() or not skill_path.exists():
        raise FileNotFoundError(f"candidate not found: {candidate_id}")
    metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
    return base, metadata, skill_path.read_text(encoding="utf-8")


def approve_candidate(
    workspace_root: str | Path,
    candidate_id: str,
    *,
    candidate_dir: str = DEFAULT_CANDIDATE_DIR,
    skills_dir: str = DEFAULT_PROJECT_SKILLS_DIR,
) -> dict[str, Any]:
    root = Path(workspace_root).expanduser().resolve()
    candidate_root, metadata, _content = get_candidate(root, candidate_id, candidate_dir)
    if metadata.get("status") == "approved":
        return metadata
    skill_name = _sanitize_skill_name(str(metadata.get("skill_name") or candidate_id))
    dest_dir = root / skills_dir / skill_name
    if dest_dir.exists():
        raise FileExistsError(f"skill already exists: {skill_name}")
    dest_dir.parent.mkdir(parents=True, exist_ok=True)
    dest_dir.mkdir()
    shutil.copy2(candidate_root / "SKILL.md", dest_dir / "SKILL.md")
    metadata["status"] = "approved"
    metadata["approved_at"] = datetime.now().isoformat()
    metadata["skill_path"] = str(dest_dir / "SKILL.md")
    (candidate_root / "metadata.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")
    return metadata


def reject_candidate(
    workspace_root: str | Path,
    candidate_id: str,
    *,
    candidate_dir: str = DEFAULT_CANDIDATE_DIR,
) -> dict[str, Any]:
    candidate_root, metadata, _content = get_candidate(workspace_root, candidate_id, candidate_dir)
    metadata["status"] = "rejected"
    metadata["rejected_at"] = datetime.now().isoformat()
    (candidate_root / "metadata.json").write_text(json.dumps(metadata, indent=2, ensure_ascii=False), encoding="utf-8")
    return metadata


def _generate_skill_candidate(trace: dict[str, Any], provider: BaseProvider, model: str) -> dict[str, Any]:
    prompt = (
        "The user explicitly enabled /learn, so convert this completed coding-assistant trace into a reusable Clawd SKILL.md candidate.\n"
        "Do not judge whether the trace is valuable; the user has already requested extraction.\n"
        "Return only JSON with keys: skill_name (kebab-case), description, when_to_use, "
        "body (markdown instructions), reason, confidence (0-1).\n"
        "Remove failed, irrelevant, duplicated, environment-specific, or sensitive actions. "
        "Keep only the reusable workflow that would help future tasks of the same kind. "
        "If the trace was messy or partially failed, distill the intended successful workflow instead of refusing.\n\n"
        f"Trace:\n{json.dumps(trace, ensure_ascii=False)[:60000]}"
    )
    response = provider.chat(
        [{"role": "user", "content": prompt}],
        tools=None,
        model=model,
    )
    return _extract_json_object(response.content)


def _extract_json_object(text: str) -> dict[str, Any]:
    raw = text.strip()
    fence = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", raw, flags=re.DOTALL)
    if fence:
        raw = fence.group(1)
    else:
        start = raw.find("{")
        end = raw.rfind("}")
        if start >= 0 and end > start:
            raw = raw[start:end + 1]
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("evaluator response must be a JSON object")
    return data


def _trace_used_existing_skill(trace: dict[str, Any]) -> bool:
    for event in trace.get("events", []):
        if not isinstance(event, dict):
            continue
        if str(event.get("kind", "")).lower() == "tool_use" and str(event.get("tool_name", "")).lower() == "skill":
            return True
    return False


def _render_candidate_skill(*, description: str, when_to_use: str, body: str) -> str:
    safe_description = _frontmatter_line(description)
    safe_when_to_use = _frontmatter_line(when_to_use)
    lines = [
        "---",
        f"description: {safe_description}",
        "user-invocable: true",
        "disable-model-invocation: false",
    ]
    if safe_when_to_use:
        lines.append(f"when_to_use: {safe_when_to_use}")
    lines.extend(["---", "", body.strip() or "Use this skill for the learned workflow."])
    return "\n".join(lines) + "\n"


def _sanitize_skill_name(value: str) -> str:
    lowered = value.strip().lower()
    lowered = re.sub(r"[^a-z0-9]+", "-", lowered)
    lowered = re.sub(r"-+", "-", lowered).strip("-")
    return lowered or "learned-skill"


def _frontmatter_line(value: str) -> str:
    return " ".join(str(value).split())


def _mark_trace(path: Path, trace: dict[str, Any], status: dict[str, Any]) -> dict[str, Any]:
    trace["postprocess"] = _json_safe(status)
    path.write_text(json.dumps(_json_safe(trace), indent=2, ensure_ascii=False), encoding="utf-8")
    return status


def _json_safe(value: Any) -> Any:
    try:
        json.dumps(value, ensure_ascii=False)
        return value
    except TypeError:
        if isinstance(value, dict):
            return {str(k): _json_safe(v) for k, v in value.items()}
        if isinstance(value, (list, tuple, set)):
            return [_json_safe(v) for v in value]
        return str(value)
