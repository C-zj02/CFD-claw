"""Shared data contracts for design-agent orchestration."""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any
from uuid import uuid4


class DesignTaskState(str, Enum):
    """Lifecycle states for one browser design turn."""

    CREATED = "created"
    PARSED = "parsed"
    PLANNED = "planned"
    RETRIEVING = "retrieving"
    EVIDENCE_READY = "evidence_ready"
    READY_FOR_MODEL = "ready_for_model"
    FAILED = "failed"


@dataclass
class DesignTask:
    """Structured state passed between Supervisor, managers, and function agents."""

    user_request: str
    capability: str
    task_id: str = field(default_factory=lambda: f"design-{uuid4().hex[:10]}")
    state: DesignTaskState = DesignTaskState.CREATED
    intent: dict[str, Any] = field(default_factory=dict)
    plan: list[dict[str, Any]] = field(default_factory=list)
    evidence: dict[str, Any] | None = None
    artifacts: list[dict[str, Any]] = field(default_factory=list)
    checks: list[dict[str, Any]] = field(default_factory=list)
    errors: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        """Return a JSON-serializable task snapshot for event previews."""
        return {
            "task_id": self.task_id,
            "capability": self.capability,
            "state": self.state.value,
            "intent": self.intent,
            "plan": self.plan,
            "evidence_ready": self.evidence is not None,
            "artifacts": self.artifacts,
            "checks": self.checks,
            "errors": self.errors,
        }


@dataclass
class AgentEvent:
    """Auditable event emitted by a design agent."""

    agent_role: str
    agent_name: str
    stage: str
    summary: str
    task: DesignTask
    kind: str = "agent_step"
    preview: dict[str, Any] = field(default_factory=dict)
    is_error: bool = False
    error: str | None = None

    def to_web_event(self) -> dict[str, Any]:
        """Convert to the browser event schema used by the current UI."""
        payload = dict(self.preview)
        payload.setdefault("task", self.task.to_dict())
        return {
            "kind": self.kind,
            "tool_name": self.agent_name,
            "agent_role": self.agent_role,
            "agent_name": self.agent_name,
            "stage": self.stage,
            "summary": self.summary,
            "preview": payload,
            "error": self.error,
            "is_error": self.is_error,
        }
