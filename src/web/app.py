"""Local browser UI for Clawd Codex."""

from __future__ import annotations

import json
import re
import sys
import threading
import time
from dataclasses import dataclass, field
from datetime import datetime
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import parse_qs, quote, urlparse
from uuid import uuid4

from src.agent import Session
from src.config import get_provider_config, load_config
from src.design_agents import AircraftDesignOrchestrator
from src.design_execution import (
    AircraftDesignJobManager,
    AircraftDesignRequest,
    AircraftDesignRunner,
    DesignJobQueueFullError,
)
from src.providers import PROVIDER_INFO, get_provider_class
from src.tool_system import ToolContext
from src.tool_system.agent_loop import (
    DEFAULT_AGENT_MAX_TURNS,
    ToolEvent,
    run_agent_loop,
    summarize_tool_result,
    summarize_tool_use,
)
from src.tool_system.defaults import build_default_registry
from src.tool_system.registry import ToolRegistry
from src.tool_system.tools import SkillTool
from src.web.artifacts import AircraftArtifactStore
from src.web.rag_service import RagIndexService
from src.web.sessions import WebSessionStore


WEB_AIRCRAFT_SKILL_NAME = "aircraft-design-skill"
LEGACY_BROWSER_AIRCRAFT_SKILL_NAME = "aircraft-design"
INTERNAL_AIRCRAFT_RAG_SKILL_NAME = "aircraft-design-rag"
LEGACY_AIRCRAFT_DESIGN_SKILL_NAME = "aircraft-conceptual-design"
AIRCRAFT_SKILL_DISPLAY_NAME = "飞行器总体设计"

OUTPUT_PATH_RE = re.compile(r"(?:(?:\.{1,2}|~|/)[^\s`\"'<>，。；、)）\]]+)")


BROWSER_CAPABILITY_PROFILES: dict[str, dict[str, str]] = {
    WEB_AIRCRAFT_SKILL_NAME: {
        "internal_name": WEB_AIRCRAFT_SKILL_NAME,
        "display_name": AIRCRAFT_SKILL_DISPLAY_NAME,
        "short_label": "总体",
        "description": "接入 BaiSongt/aircraft-design-skill 的固定翼飞机总体设计与分析工具包，支持总体设计、重量闭合、约束分析、参数化几何和报告生成。",
        "when_to_use": "当问题涉及固定翼飞行器总体设计、Class I/II 重量闭合、约束分析、参数化几何、OpenVSP 或设计报告生成时使用。",
        "status_note": "最新技能",
        "policy": """Web session capability policy:
- The user selected the “飞行器总体设计” capability for this browser session.
- Treat aircraft-design-skill as the active engineering skill. Do not expose legacy skill names to the user.
- Use the browser-attached local aircraft-design evidence when it is present, and treat it as grounding material rather than as the user's own words.
- If the attached local evidence says the local index is building or not ready, tell the user retrieval is warming up and answer only from clearly available context.
- Use the M1 multi-agent orchestration context when present: treat Supervisor, discipline-manager, function-agent events as auditable process guidance for this turn.
- Keep the answer focused on aircraft-design reasoning, assumptions, constraints, and next-step calculations.
- Do not mention internal retrieval implementation names unless the user explicitly asks about system internals.""",
    },
}

DEFAULT_BROWSER_CAPABILITY_POLICY = BROWSER_CAPABILITY_PROFILES[WEB_AIRCRAFT_SKILL_NAME]["policy"]


WEB_STATIC_ROOT = Path(__file__).with_name("static")
INDEX_HTML = (WEB_STATIC_ROOT / "index.html").read_text(encoding="utf-8")
STYLES_CSS = (WEB_STATIC_ROOT / "styles.css").read_text(encoding="utf-8")
APP_JS = (WEB_STATIC_ROOT / "app.js").read_text(encoding="utf-8")


@dataclass
class WebRagSettings:
    """Internal retrieval settings for the local aircraft-design evidence path."""

    top_k: int = 5
    max_snippet_chars: int = 280
    use_cache: bool = True
    auto_retrieve: bool = True
    candidate_limit: int = 1200

    def to_dict(self) -> dict[str, Any]:
        return {
            "top_k": self.top_k,
            "max_snippet_chars": self.max_snippet_chars,
            "use_cache": self.use_cache,
            "auto_retrieve": self.auto_retrieve,
            "candidate_limit": self.candidate_limit,
        }


@dataclass
class WebSessionState:
    """State tracked for a browser-backed conversation."""

    session: Session
    provider_name: str
    provider: Any
    tool_registry: ToolRegistry
    tool_context: ToolContext
    auto_approve: bool = True
    auto_skill: str | None = None
    rag_settings: WebRagSettings = field(default_factory=WebRagSettings)
    lock: threading.RLock = field(default_factory=threading.RLock)


class ClawdWebService:
    """Owns browser sessions and the local agent runtime."""

    def __init__(self, workspace_root: Path | None = None) -> None:
        self.workspace_root = Path(workspace_root or Path.cwd()).resolve()
        self._sessions: dict[str, WebSessionState] = {}
        self._session_store = WebSessionStore()
        self._rag_services: dict[str, RagIndexService] = {}
        self._aircraft_orchestrator = AircraftDesignOrchestrator()
        self._aircraft_runner = AircraftDesignRunner(self.workspace_root)
        self._artifact_store = AircraftArtifactStore(self.workspace_root)
        self._design_jobs = AircraftDesignJobManager(
            self._aircraft_runner,
            metadata_root=self.workspace_root / ".clawd" / "generated" / "design_jobs",
            artifact_root=self._artifact_store.root,
        )
        self._design_job_artifacts: dict[str, dict[str, Any]] = {}
        self._lock = threading.RLock()
        self._restore_persisted_sessions()

    def get_bootstrap_payload(self) -> dict[str, Any]:
        """Return config data needed by the browser shell."""
        config = load_config()
        configured = config.get("providers", {})
        providers: list[dict[str, Any]] = []
        for name, info in PROVIDER_INFO.items():
            provider_config = configured.get(name, {})
            default_model = "deepseek-v4-pro" if name == "openai" else provider_config.get("default_model", info["default_model"])
            providers.append(
                {
                    "name": name,
                    "label": info["label"],
                    "configured": bool(provider_config.get("api_key")),
                    "base_url": provider_config.get("base_url", info["default_base_url"]),
                    "default_model": default_model,
                    "available_models": info["available_models"],
                }
            )
        return {
            "workspace_root": str(self.workspace_root),
            "default_provider": "openai" if configured.get("openai", {}).get("api_key") else config.get("default_provider", "anthropic"),
            "providers": providers,
            "skills": self._list_browser_skills(),
            "default_auto_skill": None,
            "design_jobs": {
                "available": True,
                "max_timeout_seconds": 3600,
                "max_concurrent_jobs": self._design_jobs.max_concurrent_jobs,
                "max_queued_jobs": self._design_jobs.max_queued_jobs,
                "max_history_jobs": self._design_jobs.max_history_jobs,
                "history_ttl_days": self._design_jobs.history_ttl_days,
            },
        }

    def submit_design_job(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Validate and enqueue a deterministic aircraft design run."""
        if not isinstance(payload, dict):
            raise ValueError("design job payload must be an object")
        request_payload = payload.get("request", payload)
        if not isinstance(request_payload, dict):
            raise ValueError("request must be an object")
        request = AircraftDesignRequest.from_dict(request_payload)
        timeout = payload.get("timeout_seconds", 180.0) if "request" in payload else 180.0
        if isinstance(timeout, bool) or not isinstance(timeout, (int, float)):
            raise ValueError("timeout_seconds must be a number")
        return {"job": self._design_jobs.submit(request, timeout_seconds=float(timeout))}

    def preflight_design_job(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Normalize a design request and expose defaults before execution."""
        if not isinstance(payload, dict):
            raise ValueError("design job payload must be an object")
        request_payload = payload.get("request", payload)
        if not isinstance(request_payload, dict):
            raise ValueError("request must be an object")
        request = AircraftDesignRequest.from_dict(request_payload)
        normalized = request.to_dict()
        provided_requirements = request_payload.get("requirements", {})
        provided_initial = request_payload.get("initial_guess", {})
        if not isinstance(provided_requirements, dict):
            provided_requirements = {}
        if not isinstance(provided_initial, dict):
            provided_initial = {}

        field_sources: dict[str, str] = {}
        assumptions: list[dict[str, Any]] = []
        normalized_provenance = normalized.get("provenance", {})
        provenance_fields = (
            normalized_provenance.get("input_fields", {})
            if isinstance(normalized_provenance, dict)
            and isinstance(normalized_provenance.get("input_fields", {}), dict)
            else {}
        )
        for group, provided in (
            ("requirements", provided_requirements),
            ("initial_guess", provided_initial),
        ):
            values = normalized.get(group, {})
            group_provenance = provenance_fields.get(group, {})
            if not isinstance(group_provenance, dict):
                group_provenance = {}
            if not isinstance(values, dict):
                continue
            for name, value in values.items():
                path = f"{group}.{name}"
                declared = group_provenance.get(name)
                declared_source = declared.get("source") if isinstance(declared, dict) else None
                if declared_source in {"user", "default", "derived"}:
                    source = declared_source
                elif name in provided:
                    source = "user"
                elif group == "initial_guess" and name == "mtow_kg":
                    source = "derived"
                else:
                    source = "default"
                field_sources[path] = source
                if source != "user":
                    assumptions.append({"path": path, "value": value, "source": source})

        warnings: list[str] = []
        requirements = normalized.get("requirements", {})
        initial = normalized.get("initial_guess", {})
        payload_kg = requirements.get("payload_kg") if isinstance(requirements, dict) else None
        mtow_kg = initial.get("mtow_kg") if isinstance(initial, dict) else None
        if isinstance(payload_kg, (int, float)) and isinstance(mtow_kg, (int, float)) and mtow_kg > 0:
            if payload_kg / mtow_kg > 0.5:
                warnings.append("有效载荷超过 MTOW 初猜的 50%，重量闭合风险较高。")
        takeoff = requirements.get("takeoff_distance_m") if isinstance(requirements, dict) else None
        landing = requirements.get("landing_distance_m") if isinstance(requirements, dict) else None
        if any(isinstance(value, (int, float)) and value < 100 for value in (takeoff, landing)):
            warnings.append("起降距离小于 100 m，需要明确高升力装置、障碍高度和场地假设。")
        reserve = requirements.get("reserve_fraction") if isinstance(requirements, dict) else None
        range_m = requirements.get("range_m") if isinstance(requirements, dict) else None
        if (
            isinstance(reserve, (int, float))
            and isinstance(range_m, (int, float))
            and range_m > 1_000_000
            and reserve < 0.05
        ):
            warnings.append("超过 1000 km 的任务采用低于 5% 的储备比例，建议复核任务剖面。")
        if assumptions:
            warnings.append(f"本次请求包含 {len(assumptions)} 个默认或推导字段，请在运行前确认。")

        return {
            "ready": True,
            "request": normalized,
            "field_sources": field_sources,
            "assumptions": assumptions,
            "warnings": warnings,
        }

    def list_design_jobs(self) -> dict[str, Any]:
        return {"jobs": self._design_jobs.list()}

    def get_design_job(self, job_id: str) -> dict[str, Any]:
        job = self._design_jobs.get(job_id)
        artifact = self._ensure_design_job_artifact(job)
        if artifact is not None:
            job["artifacts"] = [artifact]
        else:
            job["artifacts"] = []
        job["result_files"] = self._design_job_files(job)
        return {"job": job}

    def list_design_job_files(self, job_id: str) -> dict[str, Any]:
        """Return safe preview metadata for one deterministic design run."""
        job = self._design_jobs.get(job_id)
        return {"job_id": job_id, "files": self._design_job_files(job)}

    def resolve_design_job_file(self, job_id: str, relative_path: str) -> dict[str, Any]:
        """Resolve one output file beneath a known job's output directory."""
        job = self._design_jobs.get(job_id)
        output_dir = self._design_job_output_dir(job)
        if output_dir is None:
            raise KeyError(f"Design job has no result files: {job_id}")
        return self._artifact_store.resolve_result_file(output_dir, relative_path)

    def get_design_job_events(self, job_id: str, after_sequence: int = 0) -> dict[str, Any]:
        return self._design_jobs.events_after(job_id, after_sequence)

    def wait_for_design_job_events(
        self,
        job_id: str,
        after_sequence: int = 0,
        timeout_seconds: float = 15.0,
    ) -> dict[str, Any]:
        return self._design_jobs.wait_for_events(
            job_id,
            after_sequence=after_sequence,
            timeout_seconds=timeout_seconds,
        )

    def cancel_design_job(self, job_id: str) -> dict[str, Any]:
        return {"job": self._design_jobs.cancel(job_id)}

    def retry_design_job(self, job_id: str) -> dict[str, Any]:
        return {"job": self._design_jobs.retry(job_id)}

    def _ensure_design_job_artifact(self, job: dict[str, Any]) -> dict[str, Any] | None:
        job_id = str(job.get("job_id") or "")
        if not job_id or not job.get("terminal"):
            return None
        with self._lock:
            existing = self._design_job_artifacts.get(job_id)
        if existing is not None:
            return existing
        path = self._design_job_output_dir(job)
        if path is None:
            return None
        artifact = self._artifact_store.package(job_id, path)
        if artifact is not None:
            with self._lock:
                self._design_job_artifacts[job_id] = artifact
        return artifact

    def _design_job_files(self, job: dict[str, Any]) -> list[dict[str, Any]]:
        job_id = str(job.get("job_id") or "")
        output_dir = self._design_job_output_dir(job)
        if not job_id or output_dir is None:
            return []
        return self._artifact_store.list_result_files(job_id, output_dir)

    def _design_job_output_dir(self, job: dict[str, Any]) -> Path | None:
        result = job.get("result")
        output_dir = result.get("output_dir") if isinstance(result, dict) else None
        if not isinstance(output_dir, str):
            return None
        path = Path(output_dir).resolve()
        if not self._is_under_workspace(path) or not path.is_dir():
            return None
        return path

    def create_session(
        self,
        *,
        provider_name: str | None = None,
        model: str | None = None,
        auto_approve: bool = True,
        auto_skill: str | None = None,
        rag_settings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Create a new in-memory browser session."""
        config = load_config()
        provider_name = provider_name or ("openai" if config.get("providers", {}).get("openai", {}).get("api_key") else config.get("default_provider", "anthropic"))
        provider, resolved_model = self._build_provider(provider_name, model)
        resolved_skill = self._normalize_browser_skill_name(auto_skill)
        resolved_rag_settings = self._normalize_rag_settings(rag_settings)

        session = Session.create(provider_name, provider.model or resolved_model or "")
        session.session_id = f"{session.session_id}_{uuid4().hex[:6]}"
        session.model = provider.model or resolved_model or session.model
        state = self._build_session_state(
            session=session,
            provider_name=provider_name,
            provider=provider,
            auto_approve=auto_approve,
            auto_skill=resolved_skill,
            rag_settings=resolved_rag_settings,
        )

        with self._lock:
            self._sessions[session.session_id] = state
        session.save()
        self._save_session_preferences(state)
        return {"session": self._serialize_session(state)}

    def get_session_payload(self, session_id: str) -> dict[str, Any]:
        """Load a current browser session payload."""
        state = self._require_session(session_id)
        with state.lock:
            return {"session": self._serialize_session(state)}

    def list_sessions_payload(self) -> dict[str, Any]:
        """Return active in-memory browser sessions for the sidebar."""
        self._restore_persisted_sessions()
        with self._lock:
            states = list(self._sessions.values())
        sessions = []
        for state in states:
            locked = state.lock.acquire(blocking=False)
            try:
                sessions.append(self._serialize_session_summary(state))
            finally:
                if locked:
                    state.lock.release()
        sessions.sort(key=lambda item: item.get("updated_at") or "", reverse=True)
        return {"sessions": sessions}

    def delete_session(self, session_id: str) -> dict[str, Any]:
        """Remove a browser session from memory and disk."""
        with self._lock:
            state = self._sessions.get(session_id)
        if state is None and not self._session_store.session_exists(session_id):
            raise KeyError(f"Unknown session: {session_id}")

        if state is not None:
            locked = state.lock.acquire(blocking=False)
            if not locked:
                raise ValueError("会话正在运行，请先停止后再删除。")
            try:
                with self._lock:
                    self._sessions.pop(session_id, None)
            finally:
                state.lock.release()

        self._session_store.delete(session_id)

        return {"deleted": True, "session_id": session_id}

    def reset_session(
        self,
        session_id: str,
        *,
        auto_approve: bool | None = None,
        auto_skill: str | None = None,
        rag_settings: dict[str, Any] | None = None,
        stream: bool = False,
        on_text_chunk: Any | None = None,
        on_tool_event: Any | None = None,
    ) -> dict[str, Any]:
        """Clear the conversation while keeping provider/model choices."""
        state = self._require_session(session_id)
        with state.lock:
            if auto_approve is not None:
                state.auto_approve = auto_approve
            if auto_skill is not None:
                state.auto_skill = self._normalize_browser_skill_name(auto_skill)
            if rag_settings is not None:
                state.rag_settings = self._normalize_rag_settings(rag_settings, base=state.rag_settings)
            state.session.conversation.clear()
            state.tool_context.read_file_fingerprints.clear()
            state.tool_context.outbox.clear()
            state.tool_context.todos.clear()
            state.tool_context.tasks.clear()
            state.session.save()
            self._save_session_preferences(state)
            return {"session": self._serialize_session(state)}

    def send_message(
        self,
        session_id: str,
        message: str,
        *,
        max_turns: int = DEFAULT_AGENT_MAX_TURNS,
        auto_approve: bool | None = None,
        auto_skill: str | None = None,
        rag_settings: dict[str, Any] | None = None,
        stream: bool = False,
        on_text_chunk: Any | None = None,
        on_tool_event: Any | None = None,
    ) -> dict[str, Any]:
        """Run one agent turn for a browser session."""
        cleaned = message.strip()
        if not cleaned:
            raise ValueError("message must not be empty")

        state = self._require_session(session_id)
        with state.lock:
            if auto_approve is not None:
                state.auto_approve = auto_approve
            if auto_skill is not None:
                state.auto_skill = self._normalize_browser_skill_name(auto_skill)
            if rag_settings is not None:
                state.rag_settings = self._normalize_rag_settings(rag_settings, base=state.rag_settings)

            events: list[dict[str, Any]] = []
            state.tool_context.outbox.clear()
            state.tool_context.ask_user = None
            state.tool_context.permission_handler = self._build_permission_handler(state, events)
            turn_started_at = time.time()
            result_snapshot = self._snapshot_aircraft_result_dirs(state.session.session_id)
            active_skill = self._load_active_skill_context(cleaned, state, events, on_tool_event)
            attached_context = self._maybe_prepare_design_context(cleaned, state, events, on_tool_event)
            if active_skill is not None:
                attached_context = dict(attached_context or {})
                attached_context["active_skill"] = active_skill
            state.session.conversation.add_user_message(
                self._build_user_message(cleaned, state.auto_skill, attached_context)
            )

            def record_tool_event(event: ToolEvent) -> None:
                serialized = self._serialize_tool_event(event)
                events.append(serialized)
                if on_tool_event is not None:
                    try:
                        on_tool_event(serialized)
                    except Exception:
                        return

            result = run_agent_loop(
                conversation=state.session.conversation,
                provider=state.provider,
                tool_registry=self._active_skill_tool_registry(state, active_skill),
                tool_context=state.tool_context,
                max_turns=min(max_turns, 30) if active_skill is not None else max_turns,
                stream=stream,
                verbose=False,
                on_event=record_tool_event,
                on_text_chunk=on_text_chunk,
            )
            state.session.model = state.provider.model or state.session.model
            artifacts = self._maybe_create_aircraft_design_artifacts(
                state,
                result.response_text,
                events,
                result_snapshot=result_snapshot,
                turn_started_at=turn_started_at,
            )
            self._append_artifact_status_event(state, artifacts, events, on_tool_event)
            self._attach_turn_metadata_to_latest_assistant_message(state.session, events, artifacts)
            try:
                state.session.save()
                self._save_session_preferences(state)
            except Exception as exc:
                self._emit_web_event(
                    {
                        "kind": "persistence",
                        "tool_name": "Session",
                        "summary": f"结果已返回，但会话记录保存失败：{exc}",
                        "preview": None,
                        "error": str(exc),
                        "is_error": True,
                    },
                    events,
                    on_tool_event,
                )

            return {
                "reply": {
                    "text": result.response_text,
                    "usage": result.usage,
                    "num_turns": result.num_turns,
                    "events": events,
                    "artifacts": artifacts,
                    "outbox": list(state.tool_context.outbox),
                },
                "session": self._serialize_session(state),
            }

    def search_rag(
        self,
        query: str,
        *,
        rag_settings: dict[str, Any] | WebRagSettings | None = None,
    ) -> dict[str, Any]:
        """Run the project retriever directly for preview or browser preflight."""
        cleaned = query.strip()
        if not cleaned:
            raise ValueError("query must not be empty")
        settings = self._normalize_rag_settings(rag_settings)
        rag_payload = self._run_aircraft_rag_search(cleaned, settings)
        return {"rag": rag_payload, "settings": settings.to_dict()}

    def rag_status(self) -> dict[str, Any]:
        """Return readiness information for the local retrieval SQLite index."""
        service = self._get_aircraft_rag_service()
        return {"rag": service.status(WebRagSettings())}

    def rebuild_rag(
        self,
        *,
        rag_settings: dict[str, Any] | WebRagSettings | None = None,
        force: bool = True,
    ) -> dict[str, Any]:
        """Start a background rebuild of the local retrieval SQLite index."""
        settings = self._normalize_rag_settings(rag_settings)
        service = self._get_aircraft_rag_service()
        return {"rag": service.rebuild(settings, force=force), "settings": settings.to_dict()}

    def resolve_artifact_download(self, artifact_id: str) -> dict[str, Any]:
        """Resolve a browser artifact id to a local zip file for download."""
        return self._artifact_store.resolve_download(artifact_id)

    def _maybe_create_aircraft_design_artifacts(
        self,
        state: WebSessionState,
        reply_text: str,
        events: list[dict[str, Any]],
        *,
        result_snapshot: dict[str, tuple[int, int, int]],
        turn_started_at: float,
    ) -> list[dict[str, Any]]:
        if state.auto_skill != WEB_AIRCRAFT_SKILL_NAME:
            return []
        try:
            source_dir = self._latest_aircraft_result_dir(
                reply_text,
                events,
                session_id=state.session.session_id,
                result_snapshot=result_snapshot,
                turn_started_at=turn_started_at,
            )
            if source_dir is None:
                return []
            artifact = self._artifact_store.package(state.session.session_id, source_dir)
        except Exception as exc:
            events.append(
                {
                    "kind": "artifact",
                    "tool_name": WEB_AIRCRAFT_SKILL_NAME,
                    "summary": f"设计结果打包失败：{exc}",
                    "preview": None,
                    "error": str(exc),
                    "is_error": True,
                }
            )
            return []
        return [artifact] if artifact is not None else []

    def _latest_aircraft_result_dir(
        self,
        reply_text: str,
        events: list[dict[str, Any]],
        *,
        session_id: str,
        result_snapshot: dict[str, tuple[int, int, int]],
        turn_started_at: float,
    ) -> Path | None:
        candidates: list[Path] = []
        candidates.extend(self._standard_aircraft_output_candidates(session_id))
        candidates.extend(self._hinted_aircraft_output_candidates(reply_text, events))

        unique: dict[str, Path] = {}
        for candidate in candidates:
            try:
                resolved = candidate.expanduser().resolve()
            except (OSError, RuntimeError):
                continue
            if not resolved.exists():
                continue
            if resolved.is_file():
                resolved = resolved.parent
            if not self._is_under_workspace(resolved):
                continue
            if self._artifact_store.file_count(resolved) <= 0:
                continue
            fingerprint = self._artifact_store.fingerprint(resolved)
            previous = result_snapshot.get(str(resolved))
            if previous is not None and previous == fingerprint:
                continue
            if previous is None and self._artifact_store.latest_mtime(resolved) < turn_started_at:
                continue
            unique[str(resolved)] = resolved

        if not unique:
            return None
        return max(unique.values(), key=self._artifact_store.latest_mtime)

    def _standard_aircraft_output_candidates(self, session_id: str | None = None) -> list[Path]:
        skill_root = self.workspace_root / ".clawd" / "skills" / WEB_AIRCRAFT_SKILL_NAME
        output_root = skill_root / "output"
        candidates: list[Path] = []
        if output_root.exists():
            candidates.extend(path for path in output_root.iterdir() if path.is_dir())
            if self._artifact_store.file_count(output_root, direct=True) > 0:
                candidates.append(output_root)

        external_root = self.workspace_root / "external" / "aircraft-design-skill"
        for dirname in ("output", "outputs"):
            external_output = external_root / dirname
            if external_output.exists():
                candidates.extend(path for path in external_output.iterdir() if path.is_dir())
                if self._artifact_store.file_count(external_output, direct=True) > 0:
                    candidates.append(external_output)

        generated_root = self.workspace_root / ".clawd" / "generated" / "aircraft_design_runs"
        session_root = generated_root / session_id if session_id else generated_root
        if session_root.exists():
            candidates.extend(path for path in session_root.iterdir() if path.is_dir())
            if self._artifact_store.file_count(session_root, direct=True) > 0:
                candidates.append(session_root)

        if not candidates and self._artifact_store.file_count(skill_root) > 0:
            candidates.append(skill_root)
        return candidates

    def _snapshot_aircraft_result_dirs(self, session_id: str) -> dict[str, tuple[int, int, int]]:
        snapshot: dict[str, tuple[int, int, int]] = {}
        for candidate in self._standard_aircraft_output_candidates(session_id):
            try:
                resolved = candidate.resolve()
                if resolved.is_dir() and self._artifact_store.file_count(resolved) > 0:
                    snapshot[str(resolved)] = self._artifact_store.fingerprint(resolved)
            except OSError:
                continue
        return snapshot

    def _aircraft_session_output_root(self, session_id: str) -> Path:
        return self.workspace_root / ".clawd" / "generated" / "aircraft_design_runs" / session_id

    def _hinted_aircraft_output_candidates(self, reply_text: str, events: list[dict[str, Any]]) -> list[Path]:
        text_parts = [reply_text or ""]
        for event in events:
            try:
                text_parts.append(json.dumps(event, ensure_ascii=False))
            except (TypeError, ValueError):
                continue
        combined = "\n".join(text_parts)
        candidates: list[Path] = []
        for match in OUTPUT_PATH_RE.findall(combined):
            cleaned = match.strip().strip("`'\"()[]{}<>，。；;、,.")
            if not cleaned:
                continue
            try:
                path = Path(cleaned).expanduser()
            except (OSError, RuntimeError):
                continue
            if not path.is_absolute():
                path = self.workspace_root / path
            candidates.append(path)
        return candidates

    def _is_under_workspace(self, path: Path) -> bool:
        try:
            path.resolve().relative_to(self.workspace_root)
            return True
        except ValueError:
            return False

    def _maybe_prepare_design_context(
        self,
        query: str,
        state: WebSessionState,
        events: list[dict[str, Any]],
        on_tool_event: Any | None = None,
    ) -> dict[str, Any] | None:
        if state.auto_skill != WEB_AIRCRAFT_SKILL_NAME or not state.rag_settings.auto_retrieve:
            return None

        def emit(event: dict[str, Any]) -> None:
            events.append(event)
            if on_tool_event is not None:
                try:
                    on_tool_event(event)
                except Exception:
                    pass

        try:
            service = self._get_aircraft_rag_service()
        except Exception as exc:
            self._append_rag_error_event(str(exc), query, events, on_tool_event)
            return None

        result = self._aircraft_orchestrator.run(
            user_request=query,
            capability=WEB_AIRCRAFT_SKILL_NAME,
            rag_service=service,
            rag_settings=state.rag_settings,
            emit_event=emit,
        )
        if result.evidence is not None:
            self._append_rag_event(result.evidence, events, on_tool_event, agent_name="资料检索Agent")
        elif result.task.errors:
            self._append_rag_error_event(result.task.errors[-1], query, events, on_tool_event)
        return {
            "orchestration": result.context_prompt,
            "task": result.task.to_dict(),
            "rag": result.evidence,
        }

    def _load_active_skill_context(
        self,
        user_request: str,
        state: WebSessionState,
        events: list[dict[str, Any]],
        on_tool_event: Any | None = None,
    ) -> dict[str, Any] | None:
        if not state.auto_skill:
            return None

        tool_use_id = f"web-skill-{uuid4().hex[:12]}"
        tool_input = {"skill": state.auto_skill, "args": user_request}
        use_event = self._serialize_tool_event(
            ToolEvent(
                kind="tool_use",
                tool_name="Skill",
                tool_input=tool_input,
                tool_use_id=tool_use_id,
            )
        )
        use_event["summary"] = f"正在加载 {AIRCRAFT_SKILL_DISPLAY_NAME} 执行规范"
        self._emit_web_event(use_event, events, on_tool_event)

        try:
            result = SkillTool().run(tool_input, state.tool_context)
        except Exception as exc:
            error_event = {
                "kind": "tool_result",
                "tool_name": "Skill",
                "tool_use_id": tool_use_id,
                "summary": f"加载 {AIRCRAFT_SKILL_DISPLAY_NAME} 失败：{exc}",
                "preview": None,
                "error": str(exc),
                "is_error": True,
            }
            self._emit_web_event(error_event, events, on_tool_event)
            raise ValueError(error_event["summary"]) from exc

        output = result.output if isinstance(result.output, dict) else {}
        prompt = output.get("prompt")
        if result.is_error or not isinstance(prompt, str) or not prompt.strip():
            error = output.get("error") or "技能没有返回可执行规范"
            error_event = {
                "kind": "tool_result",
                "tool_name": "Skill",
                "tool_use_id": tool_use_id,
                "summary": f"加载 {AIRCRAFT_SKILL_DISPLAY_NAME} 失败：{error}",
                "preview": self._trim_preview(output),
                "error": str(error),
                "is_error": True,
            }
            self._emit_web_event(error_event, events, on_tool_event)
            raise ValueError(error_event["summary"])

        result_event = self._serialize_tool_event(
            ToolEvent(
                kind="tool_result",
                tool_name="Skill",
                tool_output=output,
                tool_use_id=tool_use_id,
            )
        )
        result_event["summary"] = f"已加载 {AIRCRAFT_SKILL_DISPLAY_NAME}，准备执行工程计算"
        self._emit_web_event(result_event, events, on_tool_event)

        output_root = self._aircraft_session_output_root(state.session.session_id)
        output_root.mkdir(parents=True, exist_ok=True)
        return {
            "name": state.auto_skill,
            "prompt": prompt.strip(),
            "allowed_tools": list(output.get("allowedTools") or []),
            "python_executable": str(Path(sys.executable).resolve()),
            "source_root": str((self.workspace_root / "external" / "aircraft-design-skill").resolve()),
            "output_root": str(output_root.resolve()),
        }

    def _active_skill_tool_registry(
        self,
        state: WebSessionState,
        active_skill: dict[str, Any] | None,
    ) -> ToolRegistry:
        if active_skill is None:
            return state.tool_registry
        allowed = active_skill.get("allowed_tools")
        if not isinstance(allowed, list) or not allowed:
            return state.tool_registry
        # Write is required to construct sizing_input.json before the upstream run.
        return state.tool_registry.filtered([*allowed, "Write"])

    def _emit_web_event(
        self,
        event: dict[str, Any],
        events: list[dict[str, Any]],
        on_tool_event: Any | None = None,
    ) -> None:
        events.append(event)
        if on_tool_event is not None:
            try:
                on_tool_event(event)
            except Exception:
                pass

    def _append_artifact_status_event(
        self,
        state: WebSessionState,
        artifacts: list[dict[str, Any]],
        events: list[dict[str, Any]],
        on_tool_event: Any | None = None,
    ) -> None:
        if state.auto_skill != WEB_AIRCRAFT_SKILL_NAME:
            return
        if artifacts:
            artifact = artifacts[0]
            event = {
                "kind": "artifact",
                "tool_name": WEB_AIRCRAFT_SKILL_NAME,
                "summary": f"已生成结果包，包含 {artifact['file_count']} 个设计产物",
                "preview": artifact,
                "error": None,
                "is_error": False,
            }
        else:
            event = {
                "kind": "artifact",
                "tool_name": WEB_AIRCRAFT_SKILL_NAME,
                "summary": "本轮未检测到新的设计结果文件，请查看计算过程中的失败信息",
                "preview": {"expected_root": str(self._aircraft_session_output_root(state.session.session_id))},
                "error": "no_new_aircraft_design_artifacts",
                "is_error": True,
            }
        self._emit_web_event(event, events, on_tool_event)

    def _append_rag_event(
        self,
        payload: dict[str, Any],
        events: list[dict[str, Any]],
        on_tool_event: Any | None = None,
        *,
        agent_name: str = WEB_AIRCRAFT_SKILL_NAME,
    ) -> None:
        hits = payload.get("hits")
        hit_count = len(hits) if isinstance(hits, list) else 0
        event = {
            "kind": "rag_retrieval",
            "tool_name": WEB_AIRCRAFT_SKILL_NAME,
            "agent_role": "功能层智能体",
            "agent_name": agent_name,
            "stage": "retrieval-evidence",
            "summary": f"资料检索Agent 已附加本地资料证据 · 命中={hit_count}",
            "preview": payload,
            "rag": payload,
            "error": None,
            "is_error": False,
        }
        events.append(event)
        if on_tool_event is not None:
            try:
                on_tool_event(event)
            except Exception:
                pass

    def _append_rag_error_event(
        self,
        error: str,
        query: str,
        events: list[dict[str, Any]],
        on_tool_event: Any | None = None,
    ) -> None:
        event = {
            "kind": "rag_retrieval",
            "tool_name": WEB_AIRCRAFT_SKILL_NAME,
            "agent_role": "功能层智能体",
            "agent_name": "资料检索Agent",
            "stage": "retrieval-error",
            "summary": f"本地资料检索失败：{error}",
            "preview": {"query": query},
            "error": error,
            "is_error": True,
        }
        events.append(event)
        if on_tool_event is not None:
            try:
                on_tool_event(event)
            except Exception:
                pass

    def _maybe_attach_rag_evidence(
        self,
        query: str,
        state: WebSessionState,
        events: list[dict[str, Any]],
        on_tool_event: Any | None = None,
    ) -> dict[str, Any] | None:
        if state.auto_skill != WEB_AIRCRAFT_SKILL_NAME or not state.rag_settings.auto_retrieve:
            return None
        try:
            service = self._get_aircraft_rag_service()
            if state.rag_settings.use_cache and not service.cache_ready(state.rag_settings):
                service.rebuild(state.rag_settings, force=False)
                payload = service.not_ready_payload(query, state.rag_settings)
            else:
                payload = service.search(query, state.rag_settings)
        except Exception as exc:
            event = {
                    "kind": "rag_retrieval",
                    "tool_name": WEB_AIRCRAFT_SKILL_NAME,
                    "summary": f"本地资料检索失败：{exc}",
                    "preview": {"query": query},
                    "error": str(exc),
                    "is_error": True,
                }
            events.append(event)
            if on_tool_event is not None:
                try:
                    on_tool_event(event)
                except Exception:
                    pass
            return None

        hits = payload.get("hits")
        hit_count = len(hits) if isinstance(hits, list) else 0
        event = {
                "kind": "rag_retrieval",
                "tool_name": WEB_AIRCRAFT_SKILL_NAME,
                "summary": f"已附加本地资料证据 · 命中={hit_count}",
                "preview": payload,
                "rag": payload,
                "error": None,
                "is_error": False,
            }
        events.append(event)
        if on_tool_event is not None:
            try:
                on_tool_event(event)
            except Exception:
                pass
        return payload

    def _run_aircraft_rag_search(self, query: str, settings: WebRagSettings) -> dict[str, Any]:
        return self._get_aircraft_rag_service().search(query, settings)

    def _get_aircraft_rag_service(self) -> RagIndexService:
        skill = self._get_project_skill(INTERNAL_AIRCRAFT_RAG_SKILL_NAME)
        if skill is None or not skill.skill_root:
            raise ValueError("飞行器设计资料能力在当前工作区不可用")

        script_path = Path(skill.skill_root) / "scripts" / "search_rag.py"
        if not script_path.exists():
            raise ValueError(f"RAG search script not found: {script_path}")
        service_key = str(script_path.resolve())
        with self._lock:
            service = self._rag_services.get(service_key)
            if service is None:
                service = RagIndexService(self.workspace_root, script_path)
                self._rag_services[service_key] = service
        return service

    def _build_permission_handler(
        self,
        state: WebSessionState,
        events: list[dict[str, Any]],
    ):
        def handler(tool_name: str, message: str, suggestion: str | None) -> tuple[bool, bool]:
            events.append(
                {
                    "kind": "permission",
                    "tool_name": tool_name,
                    "message": message,
                    "summary": suggestion or message,
                    "preview": {
                        "autoApproved": state.auto_approve,
                        "message": message,
                        "suggestion": suggestion,
                    },
                }
            )
            return state.auto_approve, True

        return handler

    def _serialize_session(self, state: WebSessionState) -> dict[str, Any]:
        return {
            "session_id": state.session.session_id,
            "provider": state.provider_name,
            "model": state.provider.model or state.session.model,
            "auto_approve": state.auto_approve,
            "auto_skill": self._to_browser_skill_name(state.auto_skill),
            "messages": self._serialize_messages(state.session),
            "created_at": state.session.created_at,
            "updated_at": state.session.updated_at,
        }

    def _serialize_session_summary(self, state: WebSessionState) -> dict[str, Any]:
        messages = self._serialize_messages(state.session)
        last_message = ""
        for message in reversed(messages):
            text = (message.get("text") or "").strip()
            if text:
                last_message = text if len(text) <= 90 else text[:87] + "..."
                break
        return {
            "session_id": state.session.session_id,
            "provider": state.provider_name,
            "model": state.provider.model or state.session.model,
            "auto_skill": self._to_browser_skill_name(state.auto_skill),
            "message_count": len(messages),
            "last_message": last_message,
            "created_at": state.session.created_at,
            "updated_at": state.session.updated_at,
        }

    def _normalize_rag_settings(
        self,
        value: dict[str, Any] | WebRagSettings | None,
        *,
        base: WebRagSettings | None = None,
    ) -> WebRagSettings:
        if isinstance(value, WebRagSettings):
            return value
        settings = base or WebRagSettings()
        if value is None:
            return WebRagSettings(**settings.to_dict())
        if not isinstance(value, dict):
            raise ValueError("资料检索设置必须是对象")

        top_k = self._bounded_int(value.get("top_k", settings.top_k), "资料检索设置.top_k", 1, 20)
        max_snippet_chars = self._bounded_int(
            value.get("max_snippet_chars", settings.max_snippet_chars),
            "资料检索设置.max_snippet_chars",
            80,
            3000,
        )
        use_cache = self._bool_setting(value.get("use_cache", settings.use_cache), "资料检索设置.use_cache")
        auto_retrieve = self._bool_setting(
            value.get("auto_retrieve", settings.auto_retrieve),
            "资料检索设置.auto_retrieve",
        )
        candidate_limit = self._bounded_int(
            value.get("candidate_limit", settings.candidate_limit),
            "资料检索设置.candidate_limit",
            50,
            10000,
        )
        return WebRagSettings(
            top_k=top_k,
            max_snippet_chars=max_snippet_chars,
            use_cache=use_cache,
            auto_retrieve=auto_retrieve,
            candidate_limit=candidate_limit,
        )

    def _bounded_int(self, value: Any, name: str, minimum: int, maximum: int) -> int:
        if isinstance(value, bool):
            raise ValueError(f"{name} 必须是整数")
        try:
            parsed = int(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{name} 必须是整数") from exc
        if parsed < minimum or parsed > maximum:
            raise ValueError(f"{name} 必须在 {minimum} 到 {maximum} 之间")
        return parsed

    def _bool_setting(self, value: Any, name: str) -> bool:
        if not isinstance(value, bool):
            raise ValueError(f"{name} 必须是布尔值")
        return value

    def _rag_bootstrap_payload(self) -> dict[str, Any]:
        skill = self._get_project_skill(INTERNAL_AIRCRAFT_RAG_SKILL_NAME)
        script_path = Path(skill.skill_root) / "scripts" / "search_rag.py" if skill and skill.skill_root else None
        return {
            "available": bool(skill and script_path and script_path.exists()),
            "skill_name": WEB_AIRCRAFT_SKILL_NAME,
            "data_dir": str(self.workspace_root / "RAG-data"),
            "defaults": WebRagSettings().to_dict(),
        }

    def _list_browser_skills(self) -> list[dict[str, Any]]:
        listed: list[dict[str, Any]] = []
        for browser_name, profile in BROWSER_CAPABILITY_PROFILES.items():
            internal_name = profile["internal_name"]
            skill = self._get_project_skill(internal_name)
            if skill is None:
                continue
            listed.append(
                {
                    "name": browser_name,
                    "display_name": profile["display_name"],
                    "short_label": profile["short_label"],
                    "description": profile["description"],
                    "when_to_use": profile["when_to_use"],
                    "allowed_tools": [],
                    "loaded_from": skill.loaded_from,
                    "status_note": profile["status_note"],
                }
            )
        return listed

    def _list_project_skills(self) -> list[dict[str, Any]]:
        try:
            from src.skills.loader import get_all_skills

            skills = get_all_skills(project_root=self.workspace_root)
        except Exception:
            return []

        listed: list[dict[str, Any]] = []
        for skill in skills:
            listed.append(
                {
                    "name": skill.name,
                    "description": skill.description,
                    "when_to_use": skill.when_to_use,
                    "allowed_tools": list(skill.allowed_tools) if skill.allowed_tools else [],
                    "loaded_from": skill.loaded_from,
                }
            )
        return sorted(listed, key=lambda item: item["name"])

    def _get_project_skill(self, name: str):
        try:
            from src.skills.loader import get_all_skills

            skills = get_all_skills(project_root=self.workspace_root)
        except Exception:
            return None
        return next((skill for skill in skills if skill.name == name), None)

    def _default_auto_skill(self) -> str | None:
        return None

    def _to_internal_skill_name(self, skill_name: str | None) -> str | None:
        if skill_name is None:
            return None
        normalized = skill_name.strip().removeprefix("/")
        if not normalized:
            return None
        if normalized in {
            WEB_AIRCRAFT_SKILL_NAME,
            LEGACY_BROWSER_AIRCRAFT_SKILL_NAME,
            INTERNAL_AIRCRAFT_RAG_SKILL_NAME,
            LEGACY_AIRCRAFT_DESIGN_SKILL_NAME,
        }:
            return WEB_AIRCRAFT_SKILL_NAME
        profile = BROWSER_CAPABILITY_PROFILES.get(normalized)
        if profile is not None:
            return profile["internal_name"]
        return normalized

    def _to_browser_skill_name(self, skill_name: str | None) -> str | None:
        if skill_name in {
            WEB_AIRCRAFT_SKILL_NAME,
            LEGACY_BROWSER_AIRCRAFT_SKILL_NAME,
            INTERNAL_AIRCRAFT_RAG_SKILL_NAME,
            LEGACY_AIRCRAFT_DESIGN_SKILL_NAME,
        }:
            return WEB_AIRCRAFT_SKILL_NAME
        for browser_name, profile in BROWSER_CAPABILITY_PROFILES.items():
            if skill_name == profile["internal_name"]:
                return browser_name
        return skill_name

    def _normalize_browser_skill_name(self, skill_name: str | None) -> str | None:
        internal = self._to_internal_skill_name(skill_name)
        return self._normalize_skill_name(internal)

    def _normalize_skill_name(self, skill_name: str | None) -> str | None:
        if skill_name is None:
            return None
        normalized = skill_name.strip().removeprefix("/")
        if not normalized:
            return None
        names = {skill["name"] for skill in self._list_project_skills()}
        if normalized not in names:
            raise ValueError(f"未知技能：{normalized}")
        return normalized

    def _build_user_message(
        self,
        message: str,
        auto_skill: str | None,
        attached_context: dict[str, Any] | None = None,
    ) -> str:
        if not auto_skill:
            return message
        browser_skill_name = self._to_browser_skill_name(auto_skill)
        profile = BROWSER_CAPABILITY_PROFILES.get(browser_skill_name or "")
        policy = profile["policy"] if profile is not None else DEFAULT_BROWSER_CAPABILITY_POLICY
        parts = [policy]
        if attached_context is not None:
            active_skill = attached_context.get("active_skill")
            if isinstance(active_skill, dict):
                skill_prompt = active_skill.get("prompt")
                python_executable = active_skill.get("python_executable")
                source_root = active_skill.get("source_root")
                output_root = active_skill.get("output_root")
                if all(isinstance(value, str) and value for value in (skill_prompt, python_executable, source_root, output_root)):
                    parts.append(
                        "Selected aircraft design skill execution contract:\n"
                        "- The selected Skill has already been loaded below; do not call the Skill tool again.\n"
                        "- For a request that asks for a design, calculation, model, plot, or report, a prose-only answer is incomplete.\n"
                        "- The web server has already validated the Python executable, core imports, and output directory.\n"
                        "- Execute the sizing workflow first. Do not reread runbooks or inspect source code before the first execution attempt.\n"
                        "- If the user names a bundled example, read only that example, adapt it to the run_sizing requirements/initial_guess schema, and run it.\n"
                        "- The input JSON must use the run_sizing top-level requirements and initial_guess objects; do not pass the legacy mission/payload/sizing example schema directly.\n"
                        "- When the user does not specify takeoff or landing distance, use 1000 m for both. For a medium UAV, start with wing_loading_pa=3000, thrust_to_weight=0.6, sfc_cruise_1_s=0.8/3600, cd0=0.025, and oswald_e=0.82.\n"
                        "- Create the required sizing input JSON, then execute the upstream no-GUI sizing workflow with Bash.\n"
                        f"- Use this Python executable: {python_executable}\n"
                        f"- Use this upstream source root as PYTHONPATH: {source_root}\n"
                        f"- Pass this exact base output directory to --output-dir: {output_root}\n"
                        "- Use module aircraft_design.class2_preliminary.run_sizing and include --no-viz.\n"
                        "- If an 80 m landing constraint produces zero feasible wing loading, retry once with a clearly disclosed 300 m preliminary-design assumption.\n"
                        "- Never edit files under the upstream source root during a design request. If the solver fails, report the failure and preserve the log for diagnosis.\n"
                        "- Do not claim success unless the new run directory contains design_data.json and design_report.md.\n"
                        "- In the final answer, state the new run directory and summarize the generated files.\n\n"
                        "Loaded Skill instructions:\n"
                        f"{skill_prompt}"
                    )
            orchestration = attached_context.get("orchestration")
            if isinstance(orchestration, str) and orchestration.strip():
                parts.append(orchestration.strip())
            task = attached_context.get("task")
            if isinstance(task, dict):
                parts.append(
                    "M1 design task state:\n"
                    "```json\n"
                    f"{json.dumps(task, ensure_ascii=False, indent=2)}\n"
                    "```"
                )
            attached_rag = attached_context.get("rag")
            if isinstance(attached_rag, dict):
                parts.append(
                    "Browser-attached local aircraft-design evidence for this turn:\n"
                    "```json\n"
                    f"{json.dumps(attached_rag, ensure_ascii=False, indent=2)}\n"
                    "```"
                )
        parts.append(f"User request:\n{message}")
        return "\n\n".join(parts)

    def _attach_turn_metadata_to_latest_assistant_message(
        self,
        session: Session,
        events: list[dict[str, Any]],
        artifacts: list[dict[str, Any]],
    ) -> None:
        if not events and not artifacts:
            return
        for message in reversed(session.conversation.messages):
            if message.role == "assistant":
                if events:
                    message.events = list(events)
                if artifacts:
                    message.artifacts = list(artifacts)
                return

    def _serialize_messages(self, session: Session) -> list[dict[str, Any]]:
        serialized: list[dict[str, Any]] = []
        for message in session.conversation.messages:
            text_parts: list[str] = []
            blocks: list[dict[str, Any]] = []
            if isinstance(message.content, str):
                text_parts.append(message.content)
            else:
                for block in message.content:
                    block_type = getattr(block, "type", "")
                    if block_type == "text":
                        text = getattr(block, "text", "")
                        if isinstance(text, str) and text:
                            text_parts.append(text)
                    elif block_type == "tool_use":
                        name = getattr(block, "name", "Tool")
                        blocks.append({"type": "tool_use", "label": f"Tool call: {name}"})
                    elif block_type == "tool_result":
                        blocks.append({"type": "tool_result", "label": "Tool result"})

            # Keep browser history focused on human-visible turns.
            if message.role == "user" and blocks and not text_parts:
                continue

            text = "".join(text_parts).strip()
            if message.role == "user" and "User request:\n" in text:
                text = text.rsplit("User request:\n", 1)[-1].strip()
            if not text and not blocks:
                continue

            serialized.append(
                {
                    "role": message.role,
                    "text": text,
                    "blocks": blocks,
                    "events": list(getattr(message, "events", []) or []),
                    "artifacts": list(getattr(message, "artifacts", []) or []),
                    "timestamp": message.timestamp,
                }
            )
        return serialized

    def _serialize_tool_event(self, event: ToolEvent) -> dict[str, Any]:
        preview: Any = None
        summary = ""
        if event.kind == "tool_use":
            summary = summarize_tool_use(event.tool_name, event.tool_input or {})
            preview = event.tool_input
        elif event.kind == "tool_result":
            summary = summarize_tool_result(event.tool_name, event.tool_output)
            preview = self._trim_preview(event.tool_output)
        else:
            summary = event.error or ""
            preview = event.tool_input

        serialized = {
            "kind": event.kind,
            "tool_name": event.tool_name,
            "tool_use_id": event.tool_use_id,
            "summary": summary,
            "preview": preview,
            "error": event.error,
            "is_error": event.is_error,
        }
        rag_payload = self._extract_rag_payload_from_tool_output(event.tool_output)
        if rag_payload is not None:
            serialized["rag"] = rag_payload
        return serialized

    def _extract_rag_payload_from_tool_output(self, output: Any) -> dict[str, Any] | None:
        if not isinstance(output, dict):
            return None
        command_output = output.get("retrievedCommandOutput")
        if not isinstance(command_output, str):
            return None
        json_text = self._extract_stdout_json(command_output)
        if not json_text:
            return None
        try:
            payload = json.loads(json_text)
        except json.JSONDecodeError:
            return None
        return payload if isinstance(payload, dict) and isinstance(payload.get("hits"), list) else None

    def _extract_stdout_json(self, command_output: str) -> str | None:
        marker = "STDOUT:"
        start = command_output.find(marker)
        if start >= 0:
            candidate = command_output[start + len(marker):].strip()
            stderr_start = candidate.find("\n\nSTDERR:")
            if stderr_start >= 0:
                candidate = candidate[:stderr_start].strip()
            if candidate:
                return candidate
        first = command_output.find("{")
        last = command_output.rfind("}")
        if first >= 0 and last > first:
            return command_output[first : last + 1]
        return None

    def _trim_preview(self, value: Any, *, limit: int = 1200) -> Any:
        if isinstance(value, str):
            return value if len(value) <= limit else value[:limit] + "..."
        try:
            rendered = json.dumps(value, ensure_ascii=False, indent=2)
        except Exception:
            rendered = str(value)
        if len(rendered) <= limit:
            return value
        return rendered[:limit] + "..."

    def _ensure_known_provider(self, provider_name: str) -> None:
        if provider_name not in PROVIDER_INFO:
            raise ValueError(f"Unknown provider: {provider_name}")

    def _build_provider(self, provider_name: str, model: str | None = None) -> tuple[Any, str]:
        self._ensure_known_provider(provider_name)
        provider_config = get_provider_config(provider_name)
        if not provider_config.get("api_key"):
            raise ValueError(
                f"{provider_name} API Key 未配置。请先运行 `clawd login` 并完成配置。"
            )

        provider_class = get_provider_class(provider_name)
        resolved_model = "deepseek-v4-pro" if provider_name == "openai" else (model or "").strip() or provider_config.get("default_model")
        provider = provider_class(
            api_key=provider_config["api_key"],
            base_url=provider_config.get("base_url"),
            model=resolved_model,
        )
        return provider, resolved_model or ""

    def _build_session_state(
        self,
        *,
        session: Session,
        provider_name: str,
        provider: Any,
        auto_approve: bool = True,
        auto_skill: str | None = None,
        rag_settings: WebRagSettings | None = None,
    ) -> WebSessionState:
        tool_context = ToolContext(workspace_root=self.workspace_root, cwd=self.workspace_root)
        return WebSessionState(
            session=session,
            provider_name=provider_name,
            provider=provider,
            tool_registry=build_default_registry(enable_ask_user_question=False),
            tool_context=tool_context,
            auto_approve=auto_approve,
            auto_skill=auto_skill,
            rag_settings=rag_settings or WebRagSettings(),
        )

    def _restore_persisted_sessions(self) -> None:
        for session_id in self._session_store.list_session_ids():
            with self._lock:
                if session_id in self._sessions:
                    continue
            state = self._load_persisted_session(session_id)
            if state is None:
                continue
            with self._lock:
                self._sessions.setdefault(session_id, state)

    def _load_persisted_session(self, session_id: str) -> WebSessionState | None:
        try:
            session = Session.load(session_id)
        except Exception:
            return None
        if session is None:
            return None
        try:
            provider, resolved_model = self._build_provider(session.provider, session.model)
        except Exception:
            return None
        session.model = provider.model or resolved_model or session.model
        preferences = self._session_store.load_preferences(session_id)
        auto_approve = preferences.get("auto_approve", True)
        if not isinstance(auto_approve, bool):
            auto_approve = True
        auto_skill_value = preferences.get("auto_skill")
        try:
            auto_skill = self._normalize_browser_skill_name(
                auto_skill_value if isinstance(auto_skill_value, str) else None
            )
        except ValueError:
            auto_skill = None
        rag_value = preferences.get("rag_settings")
        try:
            rag_settings = self._normalize_rag_settings(
                rag_value if isinstance(rag_value, dict) else None
            )
        except ValueError:
            rag_settings = WebRagSettings()
        return self._build_session_state(
            session=session,
            provider_name=session.provider,
            provider=provider,
            auto_approve=auto_approve,
            auto_skill=auto_skill,
            rag_settings=rag_settings,
        )

    def _save_session_preferences(self, state: WebSessionState) -> None:
        self._session_store.save_preferences(
            state.session.session_id,
            {
                "auto_approve": state.auto_approve,
                "auto_skill": state.auto_skill,
                "rag_settings": state.rag_settings.to_dict(),
            },
        )

    def _require_session(self, session_id: str) -> WebSessionState:
        with self._lock:
            state = self._sessions.get(session_id)
        if state is None:
            state = self._load_persisted_session(session_id)
            if state is not None:
                with self._lock:
                    state = self._sessions.setdefault(session_id, state)
        if state is None:
            raise KeyError(f"Unknown session: {session_id}")
        return state


class _ClawdHTTPServer(ThreadingHTTPServer):
    """HTTP server carrying the app service instance."""

    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, server_address: tuple[str, int], service: ClawdWebService):
        self.service = service
        super().__init__(server_address, ClawdWebRequestHandler)


class ClawdWebRequestHandler(BaseHTTPRequestHandler):
    """Simple local JSON API and static page handler."""

    server: _ClawdHTTPServer
    protocol_version = "HTTP/1.1"

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path in {"/", "/index.html"}:
            self._send_bytes(HTTPStatus.OK, INDEX_HTML.encode("utf-8"), "text/html; charset=utf-8")
            return
        if parsed.path == "/static/styles.css":
            self._send_bytes(HTTPStatus.OK, STYLES_CSS.encode("utf-8"), "text/css; charset=utf-8")
            return
        if parsed.path == "/static/app.js":
            self._send_bytes(
                HTTPStatus.OK,
                APP_JS.encode("utf-8"),
                "text/javascript; charset=utf-8",
            )
            return
        if parsed.path == "/api/config":
            self._send_json(HTTPStatus.OK, self.server.service.get_bootstrap_payload())
            return
        if parsed.path == "/api/rag/status":
            try:
                self._send_json(HTTPStatus.OK, self.server.service.rag_status())
            except ValueError as exc:
                self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
            return
        if parsed.path == "/api/sessions":
            self._send_json(HTTPStatus.OK, self.server.service.list_sessions_payload())
            return
        if parsed.path == "/api/design-jobs":
            self._send_json(HTTPStatus.OK, self.server.service.list_design_jobs())
            return
        if parsed.path.startswith("/api/design-jobs/") and parsed.path.endswith("/stream"):
            job_id = parsed.path.removeprefix("/api/design-jobs/").removesuffix("/stream").strip("/")
            query = parse_qs(parsed.query)
            try:
                sequence = int((query.get("after") or ["0"])[0])
            except ValueError as exc:
                self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
                return
            self._send_sse_headers()
            while True:
                try:
                    update = self.server.service.wait_for_design_job_events(job_id, sequence)
                except KeyError as exc:
                    self._write_sse("error", {"error": str(exc)})
                    return
                for event in update["events"]:
                    if not self._write_sse("progress", event):
                        return
                    sequence = max(sequence, int(event["sequence"]))
                if update["terminal"]:
                    try:
                        payload = self.server.service.get_design_job(job_id)
                    except KeyError as exc:
                        self._write_sse("error", {"error": str(exc)})
                        return
                    self._write_sse("done", payload)
                    return
                if not update["events"]:
                    if not self._write_sse("heartbeat", {"sequence": sequence}):
                        return
        if parsed.path.startswith("/api/design-jobs/") and parsed.path.endswith("/events"):
            job_id = parsed.path.removeprefix("/api/design-jobs/").removesuffix("/events").strip("/")
            query = parse_qs(parsed.query)
            try:
                after = int((query.get("after") or ["0"])[0])
                payload = self.server.service.get_design_job_events(job_id, after)
            except (KeyError, ValueError) as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND if isinstance(exc, KeyError) else HTTPStatus.BAD_REQUEST, str(exc))
                return
            self._send_json(HTTPStatus.OK, payload)
            return
        if parsed.path.startswith("/api/design-jobs/") and "/files/" in parsed.path:
            job_and_path = parsed.path.removeprefix("/api/design-jobs/")
            job_id, marker, relative_path = job_and_path.partition("/files/")
            if not marker or not job_id or "/" in job_id or not relative_path:
                self._send_error_json(HTTPStatus.NOT_FOUND, "未知设计结果文件")
                return
            query = parse_qs(parsed.query)
            try:
                result_file = self.server.service.resolve_design_job_file(job_id, relative_path)
            except (KeyError, ValueError) as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            download = (query.get("download") or ["0"])[0] in {"1", "true", "yes"}
            if download:
                self._send_download_file(
                    HTTPStatus.OK,
                    result_file["path"],
                    result_file["content_type"],
                    result_file["filename"],
                )
            else:
                self._send_inline_file(
                    HTTPStatus.OK,
                    result_file["path"],
                    result_file["content_type"],
                    result_file["filename"],
                )
            return
        if parsed.path.startswith("/api/design-jobs/") and parsed.path.endswith("/files"):
            job_id = parsed.path.removeprefix("/api/design-jobs/").removesuffix("/files").strip("/")
            if not job_id or "/" in job_id:
                self._send_error_json(HTTPStatus.NOT_FOUND, "未知设计任务")
                return
            query = parse_qs(parsed.query)
            relative_path = (query.get("path") or [None])[0]
            try:
                if relative_path is None:
                    payload = self.server.service.list_design_job_files(job_id)
                    self._send_json(HTTPStatus.OK, payload)
                    return
                result_file = self.server.service.resolve_design_job_file(job_id, relative_path)
            except (KeyError, ValueError) as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            download = (query.get("download") or ["0"])[0] in {"1", "true", "yes"}
            if download:
                self._send_download_file(
                    HTTPStatus.OK,
                    result_file["path"],
                    result_file["content_type"],
                    result_file["filename"],
                )
            else:
                self._send_inline_file(
                    HTTPStatus.OK,
                    result_file["path"],
                    result_file["content_type"],
                    result_file["filename"],
                )
            return
        if parsed.path.startswith("/api/design-jobs/"):
            job_id = parsed.path.removeprefix("/api/design-jobs/").strip("/")
            if not job_id or "/" in job_id:
                self._send_error_json(HTTPStatus.NOT_FOUND, "未知设计任务")
                return
            try:
                payload = self.server.service.get_design_job(job_id)
            except KeyError as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            self._send_json(HTTPStatus.OK, payload)
            return
        if parsed.path.startswith("/api/artifacts/") and parsed.path.endswith("/download"):
            artifact_id = parsed.path.removeprefix("/api/artifacts/").removesuffix("/download").strip("/")
            if not artifact_id or "/" in artifact_id:
                self._send_error_json(HTTPStatus.NOT_FOUND, "未知下载文件")
                return
            try:
                download = self.server.service.resolve_artifact_download(artifact_id)
            except KeyError as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            self._send_download_file(
                HTTPStatus.OK,
                download["path"],
                download["content_type"],
                download["filename"],
            )
            return
        if parsed.path.startswith("/api/sessions/"):
            session_id = parsed.path.removeprefix("/api/sessions/")
            if not session_id or "/" in session_id:
                self._send_error_json(HTTPStatus.NOT_FOUND, "未知路由")
                return
            try:
                payload = self.server.service.get_session_payload(session_id)
            except KeyError as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            self._send_json(HTTPStatus.OK, payload)
            return
        self._send_error_json(HTTPStatus.NOT_FOUND, "未知路由")

    def do_DELETE(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path.startswith("/api/sessions/"):
            session_id = parsed.path.removeprefix("/api/sessions/")
            if not session_id or "/" in session_id:
                self._send_error_json(HTTPStatus.NOT_FOUND, "未知路由")
                return
            try:
                payload = self.server.service.delete_session(session_id)
            except KeyError as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            except ValueError as exc:
                self._send_error_json(HTTPStatus.CONFLICT, str(exc))
                return
            self._send_json(HTTPStatus.OK, payload)
            return
        self._send_error_json(HTTPStatus.NOT_FOUND, "未知路由")

    def do_POST(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        try:
            payload = self._read_json_body()
        except ValueError as exc:
            self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
            return

        if parsed.path == "/api/design-jobs/preflight":
            try:
                result = self.server.service.preflight_design_job(payload)
            except ValueError as exc:
                self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
                return
            self._send_json(HTTPStatus.OK, result)
            return

        if parsed.path == "/api/sessions":
            try:
                result = self.server.service.create_session(
                    provider_name=self._optional_string(payload, "provider"),
                    model=self._optional_string(payload, "model"),
                    auto_approve=self._optional_bool(payload, "auto_approve", True),
                    auto_skill=self._optional_string(payload, "auto_skill"),
                    rag_settings=self._optional_object(payload, "rag_settings"),
                )
            except ValueError as exc:
                self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
                return
            self._send_json(HTTPStatus.CREATED, result)
            return

        if parsed.path == "/api/design-jobs":
            try:
                result = self.server.service.submit_design_job(payload)
            except DesignJobQueueFullError as exc:
                self._send_error_json(HTTPStatus.TOO_MANY_REQUESTS, str(exc))
                return
            except ValueError as exc:
                self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
                return
            self._send_json(HTTPStatus.ACCEPTED, result)
            return

        if parsed.path.startswith("/api/design-jobs/") and parsed.path.endswith("/cancel"):
            job_id = parsed.path.removeprefix("/api/design-jobs/").removesuffix("/cancel").strip("/")
            try:
                result = self.server.service.cancel_design_job(job_id)
            except KeyError as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            self._send_json(HTTPStatus.ACCEPTED, result)
            return

        if parsed.path.startswith("/api/design-jobs/") and parsed.path.endswith("/retry"):
            job_id = parsed.path.removeprefix("/api/design-jobs/").removesuffix("/retry").strip("/")
            try:
                result = self.server.service.retry_design_job(job_id)
            except KeyError as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            except ValueError as exc:
                self._send_error_json(HTTPStatus.CONFLICT, str(exc))
                return
            self._send_json(HTTPStatus.ACCEPTED, result)
            return

        if parsed.path.startswith("/api/sessions/") and parsed.path.endswith("/messages/stream"):
            session_id = parsed.path.removeprefix("/api/sessions/").removesuffix("/messages/stream").rstrip("/")
            message = self._optional_string(payload, "message")
            if message is None:
                self._send_error_json(HTTPStatus.BAD_REQUEST, "message 为必填项")
                return
            self._send_sse_headers()

            def emit(event: str, data: dict[str, Any]) -> None:
                self._write_sse(event, data)

            try:
                result = self.server.service.send_message(
                    session_id,
                    message,
                    auto_approve=self._optional_bool(payload, "auto_approve", None),
                    auto_skill=self._optional_string(payload, "auto_skill"),
                    rag_settings=self._optional_object(payload, "rag_settings"),
                    stream=True,
                    on_text_chunk=lambda chunk: emit("chunk", {"text": chunk}),
                    on_tool_event=lambda event: emit("tool", event),
                )
            except Exception as exc:
                emit("error", {"error": str(exc)})
                return
            emit("done", result)
            return

        if parsed.path.startswith("/api/sessions/") and parsed.path.endswith("/reset"):
            session_id = parsed.path.removeprefix("/api/sessions/").removesuffix("/reset").rstrip("/")
            try:
                result = self.server.service.reset_session(
                    session_id,
                    auto_approve=self._optional_bool(payload, "auto_approve", None),
                    auto_skill=self._optional_string(payload, "auto_skill"),
                    rag_settings=self._optional_object(payload, "rag_settings"),
                )
            except KeyError as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            self._send_json(HTTPStatus.OK, result)
            return

        if parsed.path.startswith("/api/sessions/") and parsed.path.endswith("/messages"):
            session_id = parsed.path.removeprefix("/api/sessions/").removesuffix("/messages").rstrip("/")
            message = self._optional_string(payload, "message")
            if message is None:
                self._send_error_json(HTTPStatus.BAD_REQUEST, "message 为必填项")
                return
            try:
                result = self.server.service.send_message(
                    session_id,
                    message,
                    auto_approve=self._optional_bool(payload, "auto_approve", None),
                    auto_skill=self._optional_string(payload, "auto_skill"),
                    rag_settings=self._optional_object(payload, "rag_settings"),
                )
            except KeyError as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            except ValueError as exc:
                self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
                return
            except Exception as exc:  # pragma: no cover - defensive path
                self._send_error_json(HTTPStatus.INTERNAL_SERVER_ERROR, str(exc))
                return
            self._send_json(HTTPStatus.OK, result)
            return

        if parsed.path == "/api/rag/search":
            query = self._optional_string(payload, "query")
            if query is None:
                self._send_error_json(HTTPStatus.BAD_REQUEST, "query 为必填项")
                return
            try:
                result = self.server.service.search_rag(
                    query,
                    rag_settings=self._optional_object(payload, "rag_settings"),
                )
            except ValueError as exc:
                self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
                return
            self._send_json(HTTPStatus.OK, result)
            return

        if parsed.path == "/api/rag/rebuild":
            try:
                result = self.server.service.rebuild_rag(
                    rag_settings=self._optional_object(payload, "rag_settings"),
                    force=self._optional_bool(payload, "force", True),
                )
            except ValueError as exc:
                self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
                return
            self._send_json(HTTPStatus.ACCEPTED, result)
            return

        self._send_error_json(HTTPStatus.NOT_FOUND, "未知路由")

    def log_message(self, format: str, *args: Any) -> None:
        """Keep the server quiet unless needed for debugging."""
        return

    def _read_json_body(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length", "0") or "0")
        if length <= 0:
            return {}
        raw = self.rfile.read(length)
        try:
            data = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError(f"JSON 请求体无效：{exc.msg}") from exc
        if not isinstance(data, dict):
            raise ValueError("JSON 请求体必须是对象")
        return data

    def _optional_string(self, payload: dict[str, Any], key: str) -> str | None:
        value = payload.get(key)
        if value is None:
            return None
        if not isinstance(value, str):
            raise ValueError(f"{key} 必须是字符串")
        return value

    def _optional_bool(self, payload: dict[str, Any], key: str, default: bool | None) -> bool | None:
        value = payload.get(key, default)
        if value is None:
            return None
        if not isinstance(value, bool):
            raise ValueError(f"{key} 必须是布尔值")
        return value

    def _optional_object(self, payload: dict[str, Any], key: str) -> dict[str, Any] | None:
        value = payload.get(key)
        if value is None:
            return None
        if not isinstance(value, dict):
            raise ValueError(f"{key} 必须是对象")
        return value

    def _send_json(self, status: HTTPStatus, payload: dict[str, Any]) -> None:
        self._send_bytes(status, json.dumps(payload, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

    def _send_error_json(self, status: HTTPStatus, message: str) -> None:
        self._send_json(status, {"error": message})

    def _send_sse_headers(self) -> None:
        self.send_response(HTTPStatus.OK.value)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Connection", "close")
        self.end_headers()
        self.close_connection = True

    def _write_sse(self, event: str, payload: dict[str, Any]) -> bool:
        try:
            data = json.dumps(payload, ensure_ascii=False)
            self.wfile.write(f"event: {event}\ndata: {data}\n\n".encode("utf-8"))
            self.wfile.flush()
            return True
        except (BrokenPipeError, ConnectionResetError):
            return False

    def _send_bytes(self, status: HTTPStatus, payload: bytes, content_type: str) -> None:
        self.send_response(status.value)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)

    def _send_download_file(
        self,
        status: HTTPStatus,
        path: Path,
        content_type: str,
        filename: str,
    ) -> None:
        payload = path.read_bytes()
        ascii_filename = re.sub(r"[^A-Za-z0-9_.-]+", "_", filename).strip("_") or path.name
        self.send_response(status.value)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.send_header(
            "Content-Disposition",
            f"attachment; filename=\"{ascii_filename}\"; filename*=UTF-8''{quote(filename)}",
        )
        self.end_headers()
        self.wfile.write(payload)

    def _send_inline_file(
        self,
        status: HTTPStatus,
        path: Path,
        content_type: str,
        filename: str,
    ) -> None:
        payload = path.read_bytes()
        ascii_filename = re.sub(r"[^A-Za-z0-9_.-]+", "_", filename).strip("_") or path.name
        self.send_response(status.value)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.send_header("X-Content-Type-Options", "nosniff")
        self.send_header("Cross-Origin-Resource-Policy", "same-origin")
        self.send_header(
            "Content-Disposition",
            f"inline; filename=\"{ascii_filename}\"; filename*=UTF-8''{quote(filename)}",
        )
        if content_type.startswith("text/html"):
            self.send_header("X-Frame-Options", "SAMEORIGIN")
            self.send_header(
                "Content-Security-Policy",
                "default-src 'self' data: blob:; script-src 'self' 'unsafe-inline'; "
                "style-src 'self' 'unsafe-inline'; img-src 'self' data: blob:; "
                "connect-src 'none'; frame-ancestors 'self'",
            )
        self.end_headers()
        self.wfile.write(payload)


def run_web_server(host: str = "127.0.0.1", port: int = 8080, workspace_root: Path | None = None) -> None:
    """Start the local browser UI server."""
    service = ClawdWebService(workspace_root=workspace_root)
    server = _ClawdHTTPServer((host, port), service)
    url = f"http://{host}:{port}"
    print(f"飞行器工程网页端已启动：{url}")
    print(f"工作区：{service.workspace_root}")
    print("按 Ctrl+C 停止服务器。")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n正在停止飞行器工程网页端...")
    finally:
        server.server_close()
