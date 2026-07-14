"""Local browser UI for Clawd Codex."""

from __future__ import annotations

import hashlib
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
from urllib.parse import parse_qs, quote, unquote, urlparse
from uuid import uuid4

from src.agent import Session
from src.config import get_provider_config, load_config
from src.design_agents import AircraftDesignOrchestrator
from src.design_intake.parser import (
    looks_like_design_request,
    looks_like_requirement_change,
)
from src.design_intake.preflight import diagnose_design_intent
from src.design_intake.projection import intent_from_aircraft_request
from src.design_intake.store import (
    DesignRevisionStore,
    IdempotencyConflictError,
    RevisionConflictError,
    RevisionNotFoundError,
    SessionNotFoundError,
    canonical_sha256,
)
from src.design_intake.workflow import (
    DesignRequirementWorkflow,
    WorkflowActionError,
    WorkflowStateError,
)
from src.design_execution import (
    AircraftDesignJobManager,
    AircraftDesignRequest,
    AircraftDesignRunner,
    DesignJobQueueFullError,
    extract_engineering_result,
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
REQUIREMENT_ACTION_ID_RE = re.compile(r"[A-Za-z0-9][A-Za-z0-9_-]{0,127}")
REQUIREMENT_REVISION_HASH_RE = re.compile(r"[0-9a-f]{64}")


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
AIRCRAFT_WEB_ASSET_ROOT = Path(__file__).parents[2] / "external" / "aircraft-design-skill" / "assets"
INDEX_HTML = (WEB_STATIC_ROOT / "index.html").read_text(encoding="utf-8")
STYLES_CSS = (WEB_STATIC_ROOT / "styles.css").read_text(encoding="utf-8")
APP_JS = (WEB_STATIC_ROOT / "app.js").read_text(encoding="utf-8")
THREE_JS = (AIRCRAFT_WEB_ASSET_ROOT / "three.min.js").read_bytes()
ORBIT_CONTROLS_JS = (AIRCRAFT_WEB_ASSET_ROOT / "OrbitControls.js").read_bytes()


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
        self._requirement_store = DesignRevisionStore(
            self.workspace_root / ".clawd" / "generated" / "requirement_revisions"
        )
        self._requirement_workflow = DesignRequirementWorkflow(self._requirement_store)
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
        provenance = request_payload.get("provenance")
        if isinstance(provenance, dict) and "requirement_workflow" in provenance:
            raise ValueError(
                "requirement_workflow provenance is server-owned; submit a confirmed "
                "revision through its submit_solver action"
            )
        preflight = self.preflight_design_job({"request": request_payload})
        diagnosis = preflight.get("diagnosis")
        if not isinstance(diagnosis, dict) or diagnosis.get("ready_for_solver") is not True:
            status = diagnosis.get("status") if isinstance(diagnosis, dict) else "invalid"
            raise ValueError(
                "design request is not ready for the deterministic solver "
                f"(preflight status: {status}); resolve it through the requirement workflow"
            )
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

        provided_solver = {
            name: request_payload[name]
            for name in (
                "tolerance",
                "max_iterations",
                "auto_repair_enabled",
                "max_repair_attempts",
            )
            if name in request_payload
        }
        solver_values = {
            "tolerance": request.tolerance,
            "max_iterations": request.max_iterations,
            "auto_repair_enabled": request.auto_repair_enabled,
            "max_repair_attempts": request.max_repair_attempts,
        }
        solver_provenance = provenance_fields.get("solver", {})
        if not isinstance(solver_provenance, dict):
            solver_provenance = {}
        for name, value in solver_values.items():
            path = f"solver.{name}"
            declared = solver_provenance.get(name)
            declared_source = declared.get("source") if isinstance(declared, dict) else None
            if declared_source in {"user", "default", "derived"}:
                source = declared_source
            else:
                source = "user" if name in provided_solver else "default"
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

        intent = intent_from_aircraft_request(request, field_sources=field_sources)
        diagnosis = diagnose_design_intent(intent)
        if diagnosis.status.value == "unsupported":
            warnings.append("存在阻断型模型覆盖缺口；这表示当前模型未覆盖，不能据此判定物理不可行。")
        elif diagnosis.status.value == "contradictory_requirements":
            warnings.append("需求中存在相互矛盾的锁定字段，必须确认一个修改方案后才能求解。")
        elif diagnosis.status.value == "needs_clarification":
            warnings.append("存在高影响待确认字段，补充或确认后才能进入确定性求解。")
        elif diagnosis.status.value == "repairable":
            warnings.append("预检生成了有界修改建议；用户字段尚未改变，确认新需求版本后才能求解。")

        intent_payload = intent.to_dict()
        intent_payload["status"] = diagnosis.status.value

        return {
            "contract_version": 2,
            "ready": diagnosis.ready_for_solver,
            "request": normalized,
            "field_sources": field_sources,
            "assumptions": assumptions,
            "warnings": warnings,
            "intent": intent_payload,
            "diagnosis": diagnosis.to_dict(),
            "model_coverage": [item.to_dict() for item in diagnosis.coverage],
            "workflow": {
                "state": diagnosis.status.value,
                "can_confirm": diagnosis.ready_for_solver,
                "can_submit": diagnosis.ready_for_solver,
                "requires_user_action": not diagnosis.ready_for_solver,
            },
        }

    def get_current_requirement_revision(self, session_id: str) -> dict[str, Any]:
        """Return the current requirement revision as the browser interaction contract."""

        state = self._require_session(session_id)
        with state.lock:
            snapshot = self._requirement_workflow.current(session_id)
            return {
                "session_id": session_id,
                "interaction": (
                    None if snapshot is None else self._requirement_interaction(snapshot)
                ),
            }

    def apply_requirement_revision_action(
        self,
        session_id: str,
        revision_id: str,
        payload: dict[str, Any],
    ) -> dict[str, Any]:
        """Apply one optimistic, idempotent requirement-workflow action."""

        if not isinstance(payload, dict):
            raise ValueError("requirement action payload must be an object")
        state = self._require_session(session_id)
        with state.lock:
            action = self._requirement_action_name(payload.get("action"))
            expected_hash = self._requirement_revision_hash(
                payload.get("expected_revision_hash")
            )
            client_action_id = self._requirement_client_action_id(
                payload.get("client_action_id")
            )
            target_revision = self._requirement_store.load_revision(session_id, revision_id)
            if target_revision["revision_hash"] != expected_hash:
                raise RevisionConflictError(
                    f"revision '{revision_id}' does not match expected_revision_hash"
                )
            current = self._requirement_workflow.current(session_id)
            if current is None:
                raise SessionNotFoundError(
                    f"design session '{session_id}' has no requirement revision"
                )

            decisions = payload.get("decisions")
            if decisions is None:
                decisions = {}
            if not isinstance(decisions, dict):
                raise WorkflowActionError("decisions must be an object")

            job: dict[str, Any] | None = None
            if action == "apply_change":
                self._reject_unused_requirement_decisions(action, decisions)
                self._check_requirement_action_fields(
                    payload,
                    {"proposal_id", "user_confirmed"},
                )
                proposal_id = payload.get("proposal_id")
                if not isinstance(proposal_id, str) or not proposal_id.strip():
                    raise WorkflowActionError("proposal_id must be a non-empty string")
                snapshot = self._requirement_workflow.apply_change(
                    session_id,
                    proposal_id=proposal_id.strip(),
                    expected_revision_hash=expected_hash,
                    client_action_id=client_action_id,
                    user_confirmed=payload.get("user_confirmed", False),
                )
            elif action == "answer_question":
                unknown_decisions = sorted(set(decisions) - {"clarification_answers"})
                if unknown_decisions:
                    raise WorkflowActionError(
                        "unsupported answer decisions: " + ", ".join(unknown_decisions)
                    )
                self._check_requirement_action_fields(
                    payload,
                    {"question_id", "answer", "field_path"},
                )
                answers = decisions.get("clarification_answers")
                if answers is None and isinstance(payload.get("question_id"), str):
                    answer: dict[str, Any] = {
                        "question_id": payload["question_id"],
                        "value": payload.get("answer"),
                    }
                    if payload.get("field_path"):
                        answer["field_path"] = payload["field_path"]
                    answers = [answer]
                answers = self._normalize_browser_clarification_answers(answers)
                snapshot = self._requirement_workflow.answer_questions(
                    session_id,
                    answers=answers,
                    expected_revision_hash=expected_hash,
                    client_action_id=client_action_id,
                )
            elif action == "defer_unsupported":
                self._reject_unused_requirement_decisions(action, decisions)
                self._check_requirement_action_fields(
                    payload,
                    {"field_paths", "scope_statement", "user_confirmed"},
                )
                snapshot = self._requirement_workflow.defer_unsupported(
                    session_id,
                    field_paths=payload.get("field_paths"),
                    scope_statement=payload.get("scope_statement", ""),
                    expected_revision_hash=expected_hash,
                    client_action_id=client_action_id,
                    user_confirmed=payload.get("user_confirmed", False),
                )
            elif action == "confirm_revision":
                self._check_requirement_action_fields(payload, {"user_confirmed"})
                snapshot = self._requirement_workflow.confirm_revision(
                    session_id,
                    expected_revision_hash=expected_hash,
                    client_action_id=client_action_id,
                    user_confirmed=payload.get("user_confirmed", False),
                    decisions=decisions or None,
                )
            else:
                self._reject_unused_requirement_decisions(action, decisions)
                self._check_requirement_action_fields(payload, {"timeout_seconds"})
                if revision_id != current["revision_id"] or expected_hash != current["revision_hash"]:
                    raise RevisionConflictError(
                        f"revision '{revision_id}' is not the current revision"
                    )
                snapshot = current
                job = self._submit_confirmed_requirement_revision(
                    session_id,
                    snapshot,
                    client_action_id=client_action_id,
                    timeout_seconds=payload.get("timeout_seconds", 180.0),
                )
                refreshed = self._requirement_workflow.current(session_id)
                if refreshed is None:  # pragma: no cover - revision was loaded above
                    raise SessionNotFoundError(
                        f"design session '{session_id}' has no requirement revision"
                    )
                snapshot = refreshed

            interaction = self._requirement_interaction(snapshot)
            event = self._persist_requirement_interaction(
                state,
                interaction,
                client_action_id=client_action_id,
                summary=self._requirement_action_summary(action, job=job),
            )
            return {
                "session": self._serialize_session(state),
                "interaction": interaction,
                "event": event,
                **({"job": job} if job is not None else {}),
            }

    @staticmethod
    def _requirement_action_name(value: Any) -> str:
        if not isinstance(value, str) or not value.strip():
            raise WorkflowActionError("action must be a non-empty string")
        aliases = {
            "apply_change_proposal": "apply_change",
            "answer_questions": "answer_question",
        }
        action = aliases.get(value.strip(), value.strip())
        allowed = {
            "apply_change",
            "answer_question",
            "defer_unsupported",
            "confirm_revision",
            "submit_solver",
        }
        if action not in allowed:
            raise WorkflowActionError(f"unsupported requirement action: {action}")
        return action

    @staticmethod
    def _requirement_revision_hash(value: Any) -> str:
        if not isinstance(value, str) or not REQUIREMENT_REVISION_HASH_RE.fullmatch(value):
            raise WorkflowActionError(
                "expected_revision_hash must be a lowercase SHA-256 hex digest"
            )
        return value

    @staticmethod
    def _requirement_client_action_id(value: Any) -> str:
        if not isinstance(value, str) or not REQUIREMENT_ACTION_ID_RE.fullmatch(value):
            raise WorkflowActionError(
                "client_action_id must contain 1-128 ASCII letters, numbers, '_' or '-'"
            )
        return value

    @staticmethod
    def _check_requirement_action_fields(
        payload: dict[str, Any],
        action_fields: set[str],
    ) -> None:
        common = {
            "action",
            "expected_revision_hash",
            "client_action_id",
            "decisions",
        }
        unknown = sorted(set(payload) - common - action_fields)
        if unknown:
            raise WorkflowActionError(
                "unsupported requirement action fields: " + ", ".join(unknown)
            )

    @staticmethod
    def _normalize_browser_clarification_answers(value: Any) -> list[dict[str, Any]]:
        if not isinstance(value, list) or not value:
            raise WorkflowActionError(
                "decisions.clarification_answers must contain between one and three items"
            )
        normalized: list[dict[str, Any]] = []
        for item in value:
            if not isinstance(item, dict):
                raise WorkflowActionError("each clarification answer must be an object")
            answer = dict(item)
            if answer.get("field_path") == "":
                answer.pop("field_path")
            normalized.append(answer)
        return normalized

    @staticmethod
    def _reject_unused_requirement_decisions(
        action: str,
        decisions: dict[str, Any],
    ) -> None:
        if decisions:
            raise WorkflowActionError(
                f"decisions are not accepted by {action}; submit clarification answers "
                "with answer_question first"
            )

    def _submit_confirmed_requirement_revision(
        self,
        session_id: str,
        snapshot: dict[str, Any],
        *,
        client_action_id: str,
        timeout_seconds: Any,
    ) -> dict[str, Any]:
        if isinstance(timeout_seconds, bool) or not isinstance(timeout_seconds, (int, float)):
            raise WorkflowActionError("timeout_seconds must be a number")
        timeout = float(timeout_seconds)
        if timeout <= 0 or timeout > 3_600:
            raise WorkflowActionError("timeout_seconds must be between 0 and 3600")

        # Projection is deliberately performed before any idempotent job lookup.
        # This keeps confirmation/current-revision checks authoritative even if a
        # persisted job happens to carry matching provenance.
        projected = self._requirement_workflow.project_solver_request(
            session_id,
            expected_revision_hash=snapshot["revision_hash"],
        )

        workflow_state = self._requirement_store.load_workflow(session_id)
        prior_submission = self._requirement_store.load_solver_submission(
            session_id,
            client_action_id=client_action_id,
        )
        if prior_submission is not None:
            if (
                prior_submission.get("revision_id") == snapshot["revision_id"]
                and prior_submission.get("revision_hash") == snapshot["revision_hash"]
            ):
                return self._job_for_requirement_submission(prior_submission)
            raise IdempotencyConflictError(
                f"client_action_id '{client_action_id}' was already used for another request"
            )
        prior_requirement_action = (
            workflow_state.get("client_actions", {}).get(client_action_id)
            if isinstance(workflow_state, dict)
            else None
        )
        if prior_requirement_action is not None:
            raise IdempotencyConflictError(
                f"client_action_id '{client_action_id}' was already used for another request"
            )

        existing = self._find_requirement_revision_job(
            session_id,
            snapshot["revision_id"],
            snapshot["revision_hash"],
        )
        if existing is not None:
            return existing
        request_payload = projected.to_dict()
        provenance = dict(request_payload.get("provenance") or {})
        confirmation = snapshot.get("confirmation")
        provenance["requirement_workflow"] = {
            "contract_version": 1,
            "session_id": session_id,
            "revision_id": snapshot["revision_id"],
            "revision_hash": snapshot["revision_hash"],
            "revision_number": snapshot["revision_number"],
            "client_action_id": client_action_id,
            "confirmed_at": (
                confirmation.get("confirmed_at")
                if isinstance(confirmation, dict)
                else None
            ),
        }
        request_payload.update(
            {
                "auto_repair_enabled": True,
                "max_repair_attempts": 3,
                "provenance": provenance,
            }
        )
        request = AircraftDesignRequest.from_dict(request_payload)
        job = self._design_jobs.submit(request, timeout_seconds=timeout)
        job_id = job.get("job_id") if isinstance(job, dict) else None
        persisted_request = job.get("request") if isinstance(job, dict) else None
        if not isinstance(job_id, str) or not job_id:
            raise WorkflowStateError("the job manager returned no solver job identifier")
        if not isinstance(persisted_request, dict):
            raise WorkflowStateError("the job manager returned no persisted solver request")
        expected_request_hash = canonical_sha256(request.to_dict())
        actual_request_hash = canonical_sha256(persisted_request)
        if actual_request_hash != expected_request_hash:
            raise WorkflowStateError(
                "the job manager persisted a request that differs from the confirmed projection"
            )
        self._requirement_store.record_solver_submission(
            session_id,
            job_id=job_id,
            revision_id=snapshot["revision_id"],
            expected_revision_hash=snapshot["revision_hash"],
            request_hash=actual_request_hash,
            client_action_id=client_action_id,
            actor="system",
        )
        return job

    def _find_requirement_revision_job(
        self,
        session_id: str,
        revision_id: str,
        revision_hash: str,
    ) -> dict[str, Any] | None:
        submission = self._requirement_store.load_solver_submission(
            session_id,
            revision_id=revision_id,
            revision_hash=revision_hash,
        )
        if submission is None:
            return None
        return self._job_for_requirement_submission(submission)

    def _job_for_requirement_submission(
        self,
        submission: dict[str, Any],
    ) -> dict[str, Any]:
        job_id = submission["job_id"]
        try:
            job = self._design_jobs.get(job_id)
        except KeyError as exc:
            raise WorkflowStateError(
                f"solver job '{job_id}' was already submitted but is no longer available"
            ) from exc
        request = job.get("request") if isinstance(job, dict) else None
        if not isinstance(request, dict) or canonical_sha256(request) != submission["request_hash"]:
            raise WorkflowStateError(
                f"solver job '{job_id}' no longer matches its server-owned submission audit"
            )
        return self.get_design_job(job_id)["job"]

    def _requirement_interaction(self, snapshot: dict[str, Any]) -> dict[str, Any]:
        diagnosis = snapshot["diagnosis"]
        allowed = set(snapshot.get("allowed_actions") or [])
        actions: list[dict[str, Any]] = []
        has_questions = bool(diagnosis.get("clarification_questions"))
        if has_questions and (
            "answer_questions" in allowed or "apply_change" in allowed
        ):
            # A contradictory diagnosis may expose both a prerequisite question
            # and repair proposals.  The browser submits every visible answer with
            # its button, so resolve the questions first and present proposals on
            # the next immutable revision.
            actions.append(
                {
                    "action": "answer_question",
                    "label": "提交确认信息",
                    "enabled": True,
                    "primary": True,
                    "payload": {},
                }
            )
        elif "apply_change" in allowed:
            actions.append(
                {
                    "action": "apply_change",
                    "label": "采用选中的修改建议",
                    "enabled": bool(diagnosis.get("change_proposals")),
                    "primary": True,
                    "payload": {"user_confirmed": True},
                    "reason": (
                        None
                        if diagnosis.get("change_proposals")
                        else "当前版本没有可应用的修改建议"
                    ),
                }
            )
        elif "answer_questions" in allowed:
            actions.append(
                {
                    "action": "answer_question",
                    "label": "提交确认信息",
                    "enabled": bool(diagnosis.get("clarification_questions")),
                    "primary": True,
                    "payload": {},
                }
            )
        if "defer_unsupported" in allowed:
            unsupported_paths = [
                item.get("field_path")
                for item in diagnosis.get("coverage", [])
                if item.get("status") == "unsupported" and item.get("blocking") is True
            ]
            actions.append(
                {
                    "action": "defer_unsupported",
                    "label": "保留专项需求，先求解已覆盖范围",
                    "enabled": bool(unsupported_paths),
                    "primary": True,
                    "payload": {
                        "field_paths": unsupported_paths,
                        "scope_statement": (
                            "保留当前模型未覆盖的专项要求作为后续验证缺口，"
                            "本轮只求解已覆盖的 Class I/II 范围。"
                        ),
                        "user_confirmed": True,
                    },
                }
            )
        if "confirm_revision" in allowed:
            actions.append(
                {
                    "action": "confirm_revision",
                    "label": "确认需求版本",
                    "enabled": True,
                    "primary": True,
                    "payload": {"user_confirmed": True},
                }
            )
        if "submit_solver" in allowed:
            actions.append(
                {
                    "action": "submit_solver",
                    "label": "开始总体设计求解",
                    "enabled": bool(snapshot.get("can_submit")),
                    "primary": True,
                    "payload": {"timeout_seconds": 180.0},
                }
            )
        return {
            "contract_version": 1,
            "type": "aircraft_requirement_review",
            "session_id": snapshot["session_id"],
            "revision": {
                "revision_id": snapshot["revision_id"],
                "revision_number": snapshot["revision_number"],
                "revision_hash": snapshot["revision_hash"],
                "status": diagnosis.get("status"),
                "confirmed": bool(snapshot.get("confirmed")),
                "submitted": bool(snapshot.get("submitted")),
                "defaults_materialized": bool(snapshot.get("defaults_materialized")),
                "can_submit": bool(snapshot.get("can_submit")),
            },
            "intent": snapshot["intent"],
            "diagnosis": diagnosis,
            "actions": actions,
        }

    def _persist_requirement_interaction(
        self,
        state: WebSessionState,
        interaction: dict[str, Any],
        *,
        client_action_id: str,
        summary: str,
        on_tool_event: Any | None = None,
    ) -> dict[str, Any]:
        event = {
            "kind": "requirement_interaction",
            "tool_name": WEB_AIRCRAFT_SKILL_NAME,
            "summary": summary,
            "preview": {
                "interaction": interaction,
                "client_action_id": client_action_id,
            },
            "error": None,
            "is_error": False,
        }
        already_persisted = any(
            existing.get("kind") == "requirement_interaction"
            and isinstance(existing.get("preview"), dict)
            and existing["preview"].get("client_action_id") == client_action_id
            for message in state.session.conversation.messages
            for existing in (getattr(message, "events", None) or [])
            if isinstance(existing, dict)
        )
        if not already_persisted:
            state.session.conversation.add_assistant_message("")
            state.session.conversation.messages[-1].events = [event]
            state.session.save()
            self._save_session_preferences(state)
        if on_tool_event is not None:
            try:
                on_tool_event(event)
            except Exception:
                pass
        return event

    @staticmethod
    def _requirement_action_summary(
        action: str,
        *,
        job: dict[str, Any] | None = None,
    ) -> str:
        if action == "submit_solver":
            return (
                "已从确认需求版本启动总体设计任务"
                if job is not None
                else "需求版本已确认，可进入总体设计求解"
            )
        return {
            "apply_change": "已按用户确认生成新的需求版本",
            "answer_question": "已记录澄清信息并重新诊断需求",
            "defer_unsupported": "已保留专项验证缺口并生成新的求解范围",
            "confirm_revision": "已确认当前需求版本",
        }[action]

    def list_design_jobs(self) -> dict[str, Any]:
        return {"jobs": self._design_jobs.list()}

    def get_design_job(self, job_id: str) -> dict[str, Any]:
        job = self._design_jobs.get(job_id)
        interaction = self._sync_requirement_solver_outcome(job)
        artifact = self._ensure_design_job_artifact(job)
        if artifact is not None:
            job["artifacts"] = [artifact]
        else:
            job["artifacts"] = []
        job["result_files"] = self._design_job_files(job)
        if interaction is not None:
            job["requirement_interaction"] = interaction
        return {"job": job}

    def _sync_requirement_solver_outcome(
        self,
        job: dict[str, Any],
    ) -> dict[str, Any] | None:
        """Feed a trusted failed terminal job back into requirement negotiation."""

        if job.get("terminal") is not True:
            return None
        result = job.get("result")
        if not isinstance(result, dict) or result.get("status") not in {
            "engineering_infeasible",
            "nonconverged",
        }:
            return None
        job_id = job.get("job_id")
        request = job.get("request")
        provenance = request.get("provenance") if isinstance(request, dict) else None
        workflow_hint = (
            provenance.get("requirement_workflow")
            if isinstance(provenance, dict)
            else None
        )
        session_id = (
            workflow_hint.get("session_id")
            if isinstance(workflow_hint, dict)
            else None
        )
        if (
            not isinstance(job_id, str)
            or not REQUIREMENT_ACTION_ID_RE.fullmatch(job_id)
            or not isinstance(session_id, str)
            or not REQUIREMENT_ACTION_ID_RE.fullmatch(session_id)
            or not isinstance(request, dict)
        ):
            return None

        trusted = self._requirement_workflow_for_session(job, session_id)
        if trusted is None:
            return None
        try:
            state = self._require_session(session_id)
        except KeyError:
            return None
        with state.lock:
            before = self._requirement_workflow.current(session_id)
            if before is None:
                return None
            try:
                after = self._requirement_workflow.ingest_solver_outcome(
                    session_id,
                    revision_id=trusted["revision_id"],
                    expected_revision_hash=trusted["revision_hash"],
                    job_id=job_id,
                    request_hash=canonical_sha256(request),
                    result=result,
                )
            except RevisionConflictError:
                # A user-created child revision supersedes a late job result.
                return None
            interaction = self._requirement_interaction(after)
            if after["revision_id"] == before["revision_id"]:
                return interaction
            action_id = (
                "system-outcome-"
                + canonical_sha256({"job_id": job_id, "result": result})[:32]
            )
            self._persist_requirement_interaction(
                state,
                interaction,
                client_action_id=action_id,
                summary="总体设计求解未通过，已生成待确认的诊断版本",
            )
            return interaction

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

    def _design_job_files(
        self,
        job: dict[str, Any],
        *,
        url_base: str | None = None,
    ) -> list[dict[str, Any]]:
        job_id = str(job.get("job_id") or "")
        output_dir = self._design_job_output_dir(job)
        if not job_id or output_dir is None:
            return []
        return self._artifact_store.list_result_files(
            job_id,
            output_dir,
            url_base=url_base,
        )

    def _design_job_output_dir(self, job: dict[str, Any]) -> Path | None:
        result = job.get("result")
        output_dir = result.get("output_dir") if isinstance(result, dict) else None
        if not isinstance(output_dir, str):
            return None
        path = Path(output_dir).resolve()
        if not self._is_under_workspace(path) or not path.is_dir():
            return None
        return path

    def list_session_design_results(self, session_id: str) -> dict[str, Any]:
        """Return view-only overall-design results produced by one conversation."""
        state = self._require_session(session_id)
        with state.lock:
            results = [item[0] for item in self._session_design_result_entries(state)]
        return {"session_id": session_id, "results": results}

    def resolve_session_design_result_file(
        self,
        session_id: str,
        result_id: str,
        relative_path: str,
    ) -> dict[str, Any]:
        """Resolve a preview file only when it belongs to the requested session result."""
        state = self._require_session(session_id)
        with state.lock:
            entries = self._session_design_result_entries(state)
        for result, source_dir in entries:
            if result.get("job_id") == result_id and source_dir is not None:
                return self._artifact_store.resolve_result_file(source_dir, relative_path)
        raise KeyError(f"Unknown session design result: {result_id}")

    def _session_design_result_entries(
        self,
        state: WebSessionState,
    ) -> list[tuple[dict[str, Any], Path | None]]:
        session_id = state.session.session_id
        session_root = self._aircraft_session_output_root(session_id).resolve()
        result_sources: dict[Path, dict[str, Any]] = {}

        for source_dir, artifact in self._session_design_artifact_sources(state):
            candidates = sorted(source_dir.rglob("design_data.json"))
            if not candidates:
                continue
            try:
                source_dir.relative_to(session_root)
                session_scoped = True
            except ValueError:
                session_scoped = False
            if not session_scoped and len(candidates) > 1:
                candidates = [max(candidates, key=lambda item: item.stat().st_mtime_ns)]
            for data_path in candidates:
                try:
                    resolved_data = data_path.resolve()
                    resolved_data.relative_to(source_dir)
                    result_dir = resolved_data.parent
                except (OSError, ValueError):
                    continue
                result_sources[result_dir] = artifact

        entries: list[tuple[dict[str, Any], Path | None]] = []
        for result_dir, artifact in result_sources.items():
            data_path = result_dir / "design_data.json"
            try:
                design_data = json.loads(data_path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                continue
            if not isinstance(design_data, dict):
                continue
            relative_source = result_dir.relative_to(self.workspace_root).as_posix()
            digest = hashlib.sha256(
                f"{session_id}\0{relative_source}".encode("utf-8")
            ).hexdigest()[:16]
            result_id = f"conversation-result-{digest}"
            entries.append(
                (
                    self._serialize_session_design_result(
                        state,
                        result_id=result_id,
                        result_dir=result_dir,
                        design_data=design_data,
                        artifact=artifact,
                    ),
                    result_dir,
                )
            )

        deterministic_entries = self._session_design_job_entries(state)
        deterministic_dirs = {
            source_dir
            for _, source_dir in deterministic_entries
            if source_dir is not None
        }
        if deterministic_dirs:
            entries = [
                item
                for item in entries
                if item[1] not in deterministic_dirs
            ]
        entries.extend(deterministic_entries)

        entries.sort(
            key=lambda item: (
                str(item[0].get("finished_at") or ""),
                (
                    item[1].stat().st_mtime_ns
                    if item[1] is not None and item[1].exists()
                    else 0
                ),
            ),
            reverse=True,
        )
        return entries

    def _session_design_job_entries(
        self,
        state: WebSessionState,
    ) -> list[tuple[dict[str, Any], Path | None]]:
        """Project terminal requirement-workflow jobs into one conversation."""
        entries: list[tuple[dict[str, Any], Path | None]] = []
        for summary in self._design_jobs.list():
            job_id = summary.get("job_id") if isinstance(summary, dict) else None
            if not isinstance(job_id, str) or not job_id:
                continue
            try:
                job = self._design_jobs.get(job_id)
            except KeyError:
                # A history-prune operation can race with session serialization.
                continue
            workflow = self._requirement_workflow_for_session(
                job,
                state.session.session_id,
            )
            if workflow is None:
                continue
            # Filter ownership before outcome synchronization. Session payload
            # serialization already holds this session's RLock; acquiring a
            # foreign session lock here would invert lock order across requests.
            self._sync_requirement_solver_outcome(job)
            if job.get("terminal") is not True:
                continue
            serialized, source_dir = self._serialize_session_design_job(
                state,
                job=job,
                workflow=workflow,
            )
            entries.append((serialized, source_dir))
        return entries

    def _requirement_workflow_for_session(
        self,
        job: dict[str, Any],
        session_id: str,
    ) -> dict[str, str] | None:
        job_id = job.get("job_id")
        request = job.get("request")
        if (
            not isinstance(job_id, str)
            or not REQUIREMENT_ACTION_ID_RE.fullmatch(job_id)
            or not isinstance(request, dict)
        ):
            return None
        submission = self._requirement_store.load_solver_submission(
            session_id,
            job_id=job_id,
        )
        if submission is None:
            return None
        if canonical_sha256(request) != submission["request_hash"]:
            return None
        return {
            "session_id": submission["session_id"],
            "revision_id": submission["revision_id"],
            "revision_hash": submission["revision_hash"],
        }

    def _serialize_session_design_job(
        self,
        state: WebSessionState,
        *,
        job: dict[str, Any],
        workflow: dict[str, str],
    ) -> tuple[dict[str, Any], Path | None]:
        """Reuse a deterministic job payload with session-scoped result URLs."""
        serialized = dict(job)
        job_id = str(serialized.get("job_id") or "")
        output_dir = self._design_job_output_dir(serialized)
        encoded_session = quote(state.session.session_id, safe="")
        encoded_result = quote(job_id, safe="")
        url_base = f"/api/sessions/{encoded_session}/design-results/{encoded_result}"
        result_files = self._design_job_files(serialized, url_base=url_base)

        artifact = self._ensure_design_job_artifact(serialized)
        serialized["artifacts"] = [artifact] if artifact is not None else []
        serialized["result_files"] = result_files
        serialized["source"] = "conversation"
        serialized["execution_source"] = "deterministic_job"
        serialized["session_id"] = state.session.session_id
        serialized["requirement_workflow"] = dict(workflow)

        result = serialized.get("result")
        if isinstance(result, dict):
            serialized["result"] = dict(result)
        else:
            status = str(serialized.get("status") or "failed")
            error = serialized.get("error")
            message = str(error or serialized.get("message") or "设计任务未生成结果")
            serialized["result"] = {
                "run_id": job_id,
                "status": status,
                "output_dir": None,
                "duration_seconds": 0.0,
                "converged": None,
                "engineering": {
                    "numerical_converged": None,
                    "engineering_feasible": None,
                    "overall_status": status,
                    "blocking_failed_count": 0,
                    "constraints": [],
                    "stage_status": {},
                },
                "summary": {},
                "artifacts": [],
                "issues": [
                    {
                        "code": f"job_{status}",
                        "message": message,
                        "severity": "error",
                    }
                ],
            }
        return serialized, output_dir

    def _session_design_artifact_sources(
        self,
        state: WebSessionState,
    ) -> list[tuple[Path, dict[str, Any]]]:
        sources: dict[Path, dict[str, Any]] = {}
        generated_root = (
            self.workspace_root / ".clawd" / "generated" / "aircraft_design_runs"
        ).resolve()
        session_root = (generated_root / state.session.session_id).resolve()
        for message in state.session.conversation.messages:
            artifacts = getattr(message, "artifacts", []) or []
            if not isinstance(artifacts, list):
                continue
            for artifact in artifacts:
                if not isinstance(artifact, dict):
                    continue
                if artifact.get("kind") != "aircraft_design_result_zip":
                    continue
                source_value = artifact.get("source_dir")
                if not isinstance(source_value, str) or not source_value.strip():
                    continue
                source_dir = Path(source_value).expanduser()
                if not source_dir.is_absolute():
                    source_dir = self.workspace_root / source_dir
                try:
                    source_dir = source_dir.resolve()
                    source_dir.relative_to(self.workspace_root)
                except (OSError, ValueError):
                    continue
                try:
                    source_dir.relative_to(generated_root)
                    generated_output = True
                except ValueError:
                    generated_output = False
                if generated_output:
                    try:
                        source_dir.relative_to(session_root)
                    except ValueError:
                        continue
                if source_dir.is_dir():
                    sources[source_dir] = dict(artifact)
        return list(sources.items())

    def _serialize_session_design_result(
        self,
        state: WebSessionState,
        *,
        result_id: str,
        result_dir: Path,
        design_data: dict[str, Any],
        artifact: dict[str, Any],
    ) -> dict[str, Any]:
        inputs = design_data.get("inputs")
        inputs = inputs if isinstance(inputs, dict) else {}
        requirements = inputs.get("requirements")
        requirements = dict(requirements) if isinstance(requirements, dict) else {}
        initial_guess = inputs.get("initial_guess")
        initial_guess = dict(initial_guess) if isinstance(initial_guess, dict) else {}
        solver_options = inputs.get("solver_options")
        solver_options = solver_options if isinstance(solver_options, dict) else {}
        project_name = str(design_data.get("project_name") or result_dir.name)
        request: dict[str, Any] = {
            "project_name": project_name,
            "requirements": requirements,
            "initial_guess": initial_guess,
        }
        for key in (
            "tolerance",
            "max_iterations",
            "auto_repair_enabled",
            "max_repair_attempts",
        ):
            if key in solver_options:
                request[key] = solver_options[key]
        if isinstance(design_data.get("provenance"), dict):
            request["provenance"] = dict(design_data["provenance"])

        engineering = extract_engineering_result(
            design_data,
            output_dir=result_dir,
        ).to_dict()
        outputs = design_data.get("outputs")
        outputs = outputs if isinstance(outputs, dict) else {}
        geometry = outputs.get("geometry")
        geometry = geometry if isinstance(geometry, dict) else {}
        performance = outputs.get("performance")
        performance = performance if isinstance(performance, dict) else {}
        design_point = engineering.get("design_point")
        design_point = design_point if isinstance(design_point, dict) else {}
        constraints = engineering.get("constraints")
        constraints = constraints if isinstance(constraints, list) else []
        issues = [
            {
                "code": "blocking_constraint_failed" if item.get("blocking") else "constraint_failed",
                "message": f"{item.get('label') or item.get('id') or 'constraint'} did not pass",
                "severity": "error" if item.get("blocking") else "warning",
            }
            for item in constraints
            if isinstance(item, dict) and item.get("passed") is False
        ]

        numerical = engineering.get("numerical_converged")
        feasible = engineering.get("engineering_feasible")
        if numerical is False:
            status = "nonconverged"
            message = "总体设计计算未收敛"
        elif feasible is False:
            status = "engineering_infeasible"
            message = "总体设计已完成，但方案未通过工程约束"
        else:
            status = "completed"
            message = "总体设计结果已生成"

        encoded_session = quote(state.session.session_id, safe="")
        encoded_result = quote(result_id, safe="")
        url_base = f"/api/sessions/{encoded_session}/design-results/{encoded_result}"
        result_files = self._artifact_store.list_result_files(
            result_id,
            result_dir,
            url_base=url_base,
        )
        timestamp = design_data.get("timestamp")
        finished_at = (
            str(timestamp)
            if timestamp not in (None, "")
            else str(artifact.get("created_at") or datetime.fromtimestamp(result_dir.stat().st_mtime).isoformat(timespec="seconds"))
        )
        auto_repair = outputs.get("auto_repair")
        auto_repair = auto_repair if isinstance(auto_repair, dict) else {}
        summary = {
            "mtow_kg": outputs.get("mtow_kg"),
            "empty_weight_kg": outputs.get("empty_weight_kg"),
            "fuel_weight_kg": outputs.get("fuel_weight_kg"),
            "payload_kg": requirements.get("payload_kg"),
            "wing_area_m2": outputs.get("wing_area_m2"),
            "thrust_sl_n": outputs.get("thrust_sl_n"),
            "wing_loading_pa": design_point.get("wing_loading_pa"),
            "thrust_to_weight": design_point.get("thrust_to_weight"),
            "span_m": geometry.get("span_m"),
            "mean_chord_m": geometry.get("mean_chord_m"),
            "fuselage_length_m": geometry.get("fuselage_length_m"),
            "iterations": outputs.get("iterations"),
            "actual_range_m": performance.get("actual_range_m"),
            "range_metric_kind": performance.get("range_metric_kind"),
            "takeoff_distance_m": performance.get("takeoff_distance_m"),
            "landing_distance_m": performance.get("landing_distance_m"),
            "artifact_count": artifact.get("file_count", len(result_files)),
            "issue_count": len(issues),
            "engineering_feasible": feasible,
            "engineering_status": engineering.get("overall_status"),
            "blocking_failed_count": engineering.get("blocking_failed_count", 0),
            "auto_repair_attempts": auto_repair.get("attempts_executed", 0),
            "auto_repair_succeeded": auto_repair.get("succeeded_after_repair", False),
        }
        relative_source = result_dir.relative_to(self.workspace_root).as_posix()
        artifact_copy = dict(artifact)
        return {
            "job_id": result_id,
            "session_id": state.session.session_id,
            "source": "conversation",
            "status": status,
            "stage": status,
            "progress": 100,
            "message": message,
            "request": request,
            "created_at": finished_at,
            "started_at": None,
            "finished_at": finished_at,
            "terminal": True,
            "last_sequence": 0,
            "events": [],
            "result": {
                "run_id": result_id,
                "status": status,
                "output_dir": relative_source,
                "duration_seconds": 0.0,
                "converged": numerical,
                "engineering": engineering,
                "summary": summary,
                "artifacts": [item.get("path") for item in result_files],
                "issues": issues,
            },
            "result_files": result_files,
            "artifacts": [artifact_copy],
        }

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
                current_requirement = self._requirement_workflow.current(session_id)
                if current_requirement is not None:
                    self._requirement_store.delete(
                        session_id,
                        expected_revision_hash=current_requirement["revision_hash"],
                    )
                with self._lock:
                    self._sessions.pop(session_id, None)
            finally:
                state.lock.release()
        else:
            current_requirement = self._requirement_workflow.current(session_id)
            if current_requirement is not None:
                self._requirement_store.delete(
                    session_id,
                    expected_revision_hash=current_requirement["revision_hash"],
                )

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
            requirement_result = self._maybe_handle_requirement_turn(
                state,
                cleaned,
                events,
                on_tool_event=on_tool_event,
            )
            if requirement_result is not None:
                return requirement_result
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

    def _maybe_handle_requirement_turn(
        self,
        state: WebSessionState,
        message: str,
        events: list[dict[str, Any]],
        *,
        on_tool_event: Any | None = None,
    ) -> dict[str, Any] | None:
        """Keep design creation, edits, and solver commands behind revision review."""

        current = self._requirement_workflow.current(state.session.session_id)
        pending = current is not None and not current.get("submitted")
        workflow_active = state.auto_skill == WEB_AIRCRAFT_SKILL_NAME
        if not workflow_active and not pending:
            return None
        client_action_id: str
        summary: str
        if looks_like_design_request(message):
            client_action_id = f"web-start-{uuid4().hex}"
            snapshot = self._requirement_workflow.start(
                state.session.session_id,
                message,
                client_action_id=client_action_id,
            )
            summary = "已完成需求解析和求解前诊断，等待用户确认"
        elif (
            current is not None
            and (workflow_active or pending)
            and looks_like_requirement_change(message)
        ):
            client_action_id = f"web-change-{uuid4().hex}"
            snapshot = self._requirement_workflow.propose_text_changes(
                state.session.session_id,
                message,
                expected_revision_hash=current["revision_hash"],
                client_action_id=client_action_id,
            )
            summary = "已将对话中的参数修改整理为待确认差异"
        elif pending:
            client_action_id = f"web-pending-{uuid4().hex}"
            snapshot = current
            summary = "当前需求版本仍需完成卡片中的确认操作"
        else:
            return None

        interaction = self._requirement_interaction(snapshot)
        state.session.conversation.add_user_message(message)
        event = self._persist_requirement_interaction(
            state,
            interaction,
            client_action_id=client_action_id,
            summary=summary,
            on_tool_event=on_tool_event,
        )
        events.append(event)
        return {
            "reply": {
                "text": "",
                "usage": {"input_tokens": 0, "output_tokens": 0},
                "num_turns": 0,
                "events": events,
                "artifacts": [],
                "outbox": [],
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
        if active_skill.get("name") == WEB_AIRCRAFT_SKILL_NAME:
            allowed_names = {
                str(name).lower()
                for name in allowed
                if isinstance(name, str)
            } if isinstance(allowed, list) else set()
            read_only = [
                spec.name
                for spec in state.tool_registry.list_specs()
                if spec.is_read_only and spec.name.lower() in allowed_names
            ]
            return (
                state.tool_registry.filtered(read_only)
                if read_only
                else ToolRegistry()
            )
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
            "design_results": [
                item[0] for item in self._session_design_result_entries(state)
            ],
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
                        "- If a declared field-length constraint has no feasible design point, preserve the failed requirement and propose a revised value for explicit user confirmation; never rerun with a silently relaxed distance.\n"
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
            message_events = list(getattr(message, "events", []) or [])
            message_artifacts = list(getattr(message, "artifacts", []) or [])
            if not text and not blocks and not message_events and not message_artifacts:
                continue

            serialized.append(
                {
                    "role": message.role,
                    "text": text,
                    "blocks": blocks,
                    "events": message_events,
                    "artifacts": message_artifacts,
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
        if parsed.path == "/static/vendor/three.min.js":
            self._send_bytes(HTTPStatus.OK, THREE_JS, "text/javascript; charset=utf-8")
            return
        if parsed.path == "/static/vendor/OrbitControls.js":
            self._send_bytes(HTTPStatus.OK, ORBIT_CONTROLS_JS, "text/javascript; charset=utf-8")
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
        if (
            parsed.path.startswith("/api/sessions/")
            and parsed.path.endswith("/requirement-revisions/current")
        ):
            session_id = (
                parsed.path.removeprefix("/api/sessions/")
                .removesuffix("/requirement-revisions/current")
                .rstrip("/")
            )
            if not session_id or "/" in session_id:
                self._send_error_json(HTTPStatus.NOT_FOUND, "未知会话")
                return
            try:
                payload = self.server.service.get_current_requirement_revision(
                    unquote(session_id)
                )
            except KeyError as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            except ValueError as exc:
                self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
                return
            self._send_json(HTTPStatus.OK, payload)
            return
        if parsed.path.startswith("/api/sessions/") and "/design-results/" in parsed.path and "/files/" in parsed.path:
            session_and_result = parsed.path.removeprefix("/api/sessions/")
            session_id, marker, result_and_path = session_and_result.partition("/design-results/")
            result_id, file_marker, relative_path = result_and_path.partition("/files/")
            if (
                not marker
                or not file_marker
                or not session_id
                or "/" in session_id
                or not result_id
                or "/" in result_id
                or not relative_path
            ):
                self._send_error_json(HTTPStatus.NOT_FOUND, "未知会话设计结果文件")
                return
            query = parse_qs(parsed.query)
            try:
                result_file = self.server.service.resolve_session_design_result_file(
                    unquote(session_id),
                    unquote(result_id),
                    relative_path,
                )
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
        if parsed.path.startswith("/api/sessions/") and parsed.path.endswith("/design-results"):
            session_id = parsed.path.removeprefix("/api/sessions/").removesuffix("/design-results").strip("/")
            if not session_id or "/" in session_id:
                self._send_error_json(HTTPStatus.NOT_FOUND, "未知会话")
                return
            try:
                payload = self.server.service.list_session_design_results(unquote(session_id))
            except KeyError as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            self._send_json(HTTPStatus.OK, payload)
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

        if (
            parsed.path.startswith("/api/sessions/")
            and "/requirement-revisions/" in parsed.path
            and parsed.path.endswith("/actions")
        ):
            session_and_revision = parsed.path.removeprefix("/api/sessions/")
            session_id, marker, revision_and_action = session_and_revision.partition(
                "/requirement-revisions/"
            )
            revision_id = revision_and_action.removesuffix("/actions").rstrip("/")
            if (
                not marker
                or not session_id
                or "/" in session_id
                or not revision_id
                or "/" in revision_id
            ):
                self._send_error_json(HTTPStatus.NOT_FOUND, "未知需求版本操作")
                return
            try:
                result = self.server.service.apply_requirement_revision_action(
                    unquote(session_id),
                    unquote(revision_id),
                    payload,
                )
            except DesignJobQueueFullError as exc:
                self._send_error_json(HTTPStatus.TOO_MANY_REQUESTS, str(exc))
                return
            except (
                RevisionConflictError,
                IdempotencyConflictError,
                WorkflowStateError,
                PermissionError,
            ) as exc:
                self._send_error_json(HTTPStatus.CONFLICT, str(exc))
                return
            except (SessionNotFoundError, RevisionNotFoundError, KeyError) as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            except (WorkflowActionError, ValueError) as exc:
                self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
                return
            self._send_json(HTTPStatus.OK, result)
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
