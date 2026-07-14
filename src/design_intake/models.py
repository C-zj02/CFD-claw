"""Immutable contracts for aircraft-design requirement intake and diagnosis."""

from __future__ import annotations

import math
import re
from dataclasses import dataclass, field, replace
from enum import Enum
from types import MappingProxyType
from typing import Any, Mapping, TypeVar


class RequirementRole(str, Enum):
    """How one requirement participates in design-space exploration."""

    HARD_CONSTRAINT = "hard_constraint"
    SOFT_GOAL = "soft_goal"
    DESIGN_VARIABLE = "design_variable"
    TECHNOLOGY_ASSUMPTION = "technology_assumption"


class RequirementSource(str, Enum):
    """Provenance of a normalized requirement value."""

    USER = "user"
    DERIVED = "derived"
    DEFAULT = "default"
    REFERENCE = "reference"


class DesignIntentStatus(str, Enum):
    """Fail-closed lifecycle states for normalized design intent."""

    NEEDS_CLARIFICATION = "needs_clarification"
    UNSUPPORTED = "unsupported"
    CONTRADICTORY_REQUIREMENTS = "contradictory_requirements"
    INFEASIBLE = "infeasible"
    REPAIRABLE = "repairable"
    READY_FOR_SOLVER = "ready_for_solver"
    CONCEPTUALLY_FEASIBLE = "conceptually_feasible"
    PRELIMINARY_FEASIBLE = "preliminary_feasible"
    ROBUST_PRELIMINARY_FEASIBLE = "robust_preliminary_feasible"


class ModelCoverageStatus(str, Enum):
    """Coverage of one requirement by the active engineering model set."""

    COVERED = "covered"
    PARTIAL = "partial"
    UNSUPPORTED = "unsupported"


_EnumT = TypeVar("_EnumT", bound=Enum)
_FIELD_PATH_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_.-]*$")


def _enum(value: Any, enum_type: type[_EnumT], name: str) -> _EnumT:
    if isinstance(value, enum_type):
        return value
    if not isinstance(value, str):
        raise ValueError(f"{name} must be a string")
    try:
        return enum_type(value)
    except ValueError as exc:
        choices = ", ".join(item.value for item in enum_type)
        raise ValueError(f"{name} must be one of: {choices}") from exc


def _text(value: Any, name: str, *, maximum: int = 2_000) -> str:
    if not isinstance(value, str):
        raise ValueError(f"{name} must be a string")
    cleaned = value.strip()
    if not cleaned:
        raise ValueError(f"{name} must not be empty")
    if len(cleaned) > maximum:
        raise ValueError(f"{name} must be at most {maximum} characters")
    return cleaned


def _optional_text(value: Any, name: str, *, maximum: int = 2_000) -> str | None:
    if value is None:
        return None
    return _text(value, name, maximum=maximum)


def _field_path(value: Any, name: str = "field_path") -> str:
    path = _text(value, name, maximum=240)
    if not _FIELD_PATH_RE.fullmatch(path):
        raise ValueError(
            f"{name} must use dotted ASCII identifiers (letters, numbers, '_', '-', '.')"
        )
    return path


def _finite_number(value: Any, name: str) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be a number")
    result = float(value)
    if not math.isfinite(result):
        raise ValueError(f"{name} must be finite")
    return result


def _positive_integer(value: Any, name: str) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value < 1:
        raise ValueError(f"{name} must be a positive integer")
    return value


def _boolean(value: Any, name: str) -> bool:
    if not isinstance(value, bool):
        raise ValueError(f"{name} must be a boolean")
    return value


def _freeze_json(value: Any, name: str) -> Any:
    """Validate JSON data and recursively make containers immutable."""
    if value is None or isinstance(value, (str, bool, int)):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError(f"{name} must contain only finite numbers")
        return value
    if isinstance(value, Mapping):
        frozen: dict[str, Any] = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise ValueError(f"{name} object keys must be strings")
            frozen[key] = _freeze_json(item, f"{name}.{key}")
        return MappingProxyType(frozen)
    if isinstance(value, (list, tuple)):
        return tuple(_freeze_json(item, f"{name}[{index}]") for index, item in enumerate(value))
    raise ValueError(f"{name} must be JSON-serializable")


def _thaw_json(value: Any) -> Any:
    if isinstance(value, Mapping):
        return {key: _thaw_json(item) for key, item in value.items()}
    if isinstance(value, tuple):
        return [_thaw_json(item) for item in value]
    return value


def _payload(
    value: Any,
    *,
    allowed: set[str],
    required: set[str],
    name: str,
) -> dict[str, Any]:
    if not isinstance(value, Mapping):
        raise ValueError(f"{name} must be an object")
    if any(not isinstance(key, str) for key in value):
        raise ValueError(f"{name} fields must be strings")
    unknown = sorted(set(value) - allowed)
    if unknown:
        raise ValueError(f"unsupported {name} fields: {', '.join(unknown)}")
    missing = sorted(required - set(value))
    if missing:
        raise ValueError(f"missing {name} fields: {', '.join(missing)}")
    return dict(value)


def _text_tuple(value: Any, name: str, *, field_paths: bool = False) -> tuple[str, ...]:
    if not isinstance(value, (list, tuple)):
        raise ValueError(f"{name} must be an array")
    result = tuple(
        _field_path(item, f"{name}[{index}]")
        if field_paths
        else _text(item, f"{name}[{index}]")
        for index, item in enumerate(value)
    )
    if len(set(result)) != len(result):
        raise ValueError(f"{name} must not contain duplicates")
    return result


@dataclass(frozen=True)
class RequirementField:
    """One normalized input with role, provenance, and modification policy."""

    path: str
    value: Any
    role: RequirementRole
    unit: str | None = None
    locked: bool = False
    source: RequirementSource = RequirementSource.USER
    tolerance: float | None = None
    confidence: float = 1.0
    applicable_model: str | None = None
    source_reference: str | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "path", _field_path(self.path, "requirement.path"))
        object.__setattr__(self, "value", _freeze_json(self.value, f"requirement.{self.path}.value"))
        object.__setattr__(
            self, "role", _enum(self.role, RequirementRole, f"requirement.{self.path}.role")
        )
        object.__setattr__(
            self, "source", _enum(self.source, RequirementSource, f"requirement.{self.path}.source")
        )
        object.__setattr__(
            self, "unit", _optional_text(self.unit, f"requirement.{self.path}.unit", maximum=80)
        )
        object.__setattr__(
            self,
            "applicable_model",
            _optional_text(
                self.applicable_model,
                f"requirement.{self.path}.applicable_model",
                maximum=160,
            ),
        )
        object.__setattr__(
            self,
            "source_reference",
            _optional_text(
                self.source_reference,
                f"requirement.{self.path}.source_reference",
                maximum=1_000,
            ),
        )
        object.__setattr__(self, "locked", _boolean(self.locked, f"requirement.{self.path}.locked"))
        confidence = _finite_number(self.confidence, f"requirement.{self.path}.confidence")
        if confidence < 0.0 or confidence > 1.0:
            raise ValueError(f"requirement.{self.path}.confidence must be between 0 and 1")
        object.__setattr__(self, "confidence", confidence)
        if self.tolerance is not None:
            tolerance = _finite_number(self.tolerance, f"requirement.{self.path}.tolerance")
            if tolerance < 0.0:
                raise ValueError(f"requirement.{self.path}.tolerance must not be negative")
            object.__setattr__(self, "tolerance", tolerance)
        if self.source is RequirementSource.REFERENCE and self.source_reference is None:
            raise ValueError(
                f"requirement.{self.path}.source_reference is required for reference values"
            )

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "RequirementField":
        payload = _payload(
            value,
            allowed={
                "path",
                "value",
                "role",
                "unit",
                "locked",
                "source",
                "tolerance",
                "confidence",
                "applicable_model",
                "source_reference",
            },
            required={"path", "value", "role"},
            name="requirement",
        )
        return cls(**payload)

    def to_dict(self) -> dict[str, Any]:
        return {
            "path": self.path,
            "value": _thaw_json(self.value),
            "role": self.role.value,
            "unit": self.unit,
            "locked": self.locked,
            "source": self.source.value,
            "tolerance": self.tolerance,
            "confidence": self.confidence,
            "applicable_model": self.applicable_model,
            "source_reference": self.source_reference,
        }

    def with_value(self, value: Any, *, user_confirmed: bool = False) -> "RequirementField":
        """Return a replacement, refusing silent changes to locked requirements."""
        user_confirmed = _boolean(user_confirmed, "user_confirmed")
        if self.locked and not user_confirmed:
            raise PermissionError(f"locked requirement '{self.path}' requires user confirmation")
        return replace(self, value=value)


@dataclass(frozen=True)
class DesignIntent:
    """Versioned normalized intent used as the source of truth for one design."""

    intent_id: str
    requirements: tuple[RequirementField, ...] = ()
    revision: int = 1
    status: DesignIntentStatus = DesignIntentStatus.NEEDS_CLARIFICATION
    original_request: str | None = None
    mission: Mapping[str, Any] = field(default_factory=dict)
    aircraft_class: str | None = None
    configuration: str | None = None
    propulsion: str | None = None
    launch: str | None = None
    recovery: str | None = None
    metadata: Mapping[str, Any] = field(default_factory=dict)
    accepted_change_proposal_ids: tuple[str, ...] = ()

    def __post_init__(self) -> None:
        object.__setattr__(self, "intent_id", _text(self.intent_id, "intent_id", maximum=160))
        object.__setattr__(self, "revision", _positive_integer(self.revision, "revision"))
        object.__setattr__(self, "status", _enum(self.status, DesignIntentStatus, "status"))
        if not isinstance(self.requirements, (list, tuple)):
            raise ValueError("requirements must be an array")
        requirements = tuple(
            item if isinstance(item, RequirementField) else RequirementField.from_dict(item)
            for item in self.requirements
        )
        paths = [item.path for item in requirements]
        if len(set(paths)) != len(paths):
            raise ValueError("requirements must not contain duplicate paths")
        object.__setattr__(self, "requirements", requirements)
        object.__setattr__(
            self,
            "original_request",
            _optional_text(self.original_request, "original_request", maximum=20_000),
        )
        for name in (
            "aircraft_class",
            "configuration",
            "propulsion",
            "launch",
            "recovery",
        ):
            object.__setattr__(
                self,
                name,
                _optional_text(getattr(self, name), name, maximum=240),
            )
        object.__setattr__(self, "mission", _freeze_json(self.mission, "mission"))
        if not isinstance(self.mission, Mapping):
            raise ValueError("mission must be an object")
        object.__setattr__(self, "metadata", _freeze_json(self.metadata, "metadata"))
        if not isinstance(self.metadata, Mapping):
            raise ValueError("metadata must be an object")
        object.__setattr__(
            self,
            "accepted_change_proposal_ids",
            _text_tuple(self.accepted_change_proposal_ids, "accepted_change_proposal_ids"),
        )

    @property
    def locked_field_paths(self) -> tuple[str, ...]:
        return tuple(item.path for item in self.requirements if item.locked)

    def requirement(self, path: str) -> RequirementField:
        normalized_path = _field_path(path)
        for requirement in self.requirements:
            if requirement.path == normalized_path:
                return requirement
        raise KeyError(f"unknown requirement field: {normalized_path}")

    def apply_change(
        self,
        proposal: "ChangeProposal",
        *,
        user_confirmed: bool = False,
    ) -> "DesignIntent":
        """Create a new revision after validating confirmation and stale-write guards."""
        if not isinstance(proposal, ChangeProposal):
            raise ValueError("proposal must be a ChangeProposal")
        user_confirmed = _boolean(user_confirmed, "user_confirmed")
        if proposal.source_revision != self.revision:
            raise ValueError(
                f"proposal revision {proposal.source_revision} does not match intent revision {self.revision}"
            )
        requirement = self.requirement(proposal.field_path)
        if _thaw_json(requirement.value) != _thaw_json(proposal.old_value):
            raise ValueError(f"proposal old_value is stale for '{proposal.field_path}'")
        if requirement.locked != proposal.target_locked:
            raise ValueError(f"proposal target_locked does not match '{proposal.field_path}'")
        if proposal.requires_user_confirmation and not user_confirmed:
            raise PermissionError(f"proposal '{proposal.proposal_id}' requires user confirmation")
        replacement = requirement.with_value(
            proposal.proposed_value,
            user_confirmed=user_confirmed,
        )
        updated = tuple(
            replacement if item.path == requirement.path else item for item in self.requirements
        )
        return replace(
            self,
            requirements=updated,
            revision=self.revision + 1,
            status=DesignIntentStatus.NEEDS_CLARIFICATION,
            accepted_change_proposal_ids=(
                *self.accepted_change_proposal_ids,
                proposal.proposal_id,
            ),
        )

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "DesignIntent":
        payload = _payload(
            value,
            allowed={
                "intent_id",
                "requirements",
                "revision",
                "status",
                "original_request",
                "mission",
                "aircraft_class",
                "configuration",
                "propulsion",
                "launch",
                "recovery",
                "metadata",
                "accepted_change_proposal_ids",
            },
            required={"intent_id"},
            name="design intent",
        )
        return cls(**payload)

    def to_dict(self) -> dict[str, Any]:
        return {
            "intent_id": self.intent_id,
            "requirements": [item.to_dict() for item in self.requirements],
            "revision": self.revision,
            "status": self.status.value,
            "original_request": self.original_request,
            "mission": _thaw_json(self.mission),
            "aircraft_class": self.aircraft_class,
            "configuration": self.configuration,
            "propulsion": self.propulsion,
            "launch": self.launch,
            "recovery": self.recovery,
            "metadata": _thaw_json(self.metadata),
            "accepted_change_proposal_ids": list(self.accepted_change_proposal_ids),
        }


@dataclass(frozen=True)
class ClarificationQuestion:
    """One bounded question required to normalize or unlock design intent."""

    question_id: str
    field_path: str
    question: str
    reason: str
    options: tuple[Any, ...] = ()
    recommended_option: Any | None = None
    consequence_if_unanswered: str | None = None
    blocking: bool = True

    def __post_init__(self) -> None:
        object.__setattr__(self, "question_id", _text(self.question_id, "question_id", maximum=160))
        object.__setattr__(self, "field_path", _field_path(self.field_path))
        object.__setattr__(self, "question", _text(self.question, "question", maximum=4_000))
        object.__setattr__(self, "reason", _text(self.reason, "reason", maximum=4_000))
        if not isinstance(self.options, (list, tuple)):
            raise ValueError("options must be an array")
        options = tuple(
            _freeze_json(item, f"options[{index}]") for index, item in enumerate(self.options)
        )
        object.__setattr__(self, "options", options)
        recommended = _freeze_json(self.recommended_option, "recommended_option")
        if recommended is not None and not options:
            raise ValueError("recommended_option requires at least one option")
        if recommended is not None and recommended not in options:
            raise ValueError("recommended_option must match one of options")
        object.__setattr__(self, "recommended_option", recommended)
        object.__setattr__(
            self,
            "consequence_if_unanswered",
            _optional_text(
                self.consequence_if_unanswered,
                "consequence_if_unanswered",
                maximum=4_000,
            ),
        )
        object.__setattr__(self, "blocking", _boolean(self.blocking, "blocking"))

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "ClarificationQuestion":
        payload = _payload(
            value,
            allowed={
                "question_id",
                "field_path",
                "question",
                "reason",
                "options",
                "recommended_option",
                "consequence_if_unanswered",
                "blocking",
            },
            required={"question_id", "field_path", "question", "reason"},
            name="clarification question",
        )
        return cls(**payload)

    def to_dict(self) -> dict[str, Any]:
        return {
            "question_id": self.question_id,
            "field_path": self.field_path,
            "question": self.question,
            "reason": self.reason,
            "options": [_thaw_json(item) for item in self.options],
            "recommended_option": _thaw_json(self.recommended_option),
            "consequence_if_unanswered": self.consequence_if_unanswered,
            "blocking": self.blocking,
        }


@dataclass(frozen=True)
class ChangeProposal:
    """Auditable, unapplied proposal for changing one normalized requirement."""

    proposal_id: str
    field_path: str
    old_value: Any
    proposed_value: Any
    reason: str
    affected_constraints: tuple[str, ...] = ()
    expected_benefit: str | None = None
    engineering_cost: str | None = None
    target_locked: bool = False
    requires_user_confirmation: bool = True
    source_revision: int = 1

    def __post_init__(self) -> None:
        object.__setattr__(self, "proposal_id", _text(self.proposal_id, "proposal_id", maximum=160))
        object.__setattr__(self, "field_path", _field_path(self.field_path))
        object.__setattr__(self, "old_value", _freeze_json(self.old_value, "old_value"))
        object.__setattr__(
            self, "proposed_value", _freeze_json(self.proposed_value, "proposed_value")
        )
        if _thaw_json(self.old_value) == _thaw_json(self.proposed_value):
            raise ValueError("proposed_value must differ from old_value")
        object.__setattr__(self, "reason", _text(self.reason, "reason", maximum=4_000))
        object.__setattr__(
            self,
            "affected_constraints",
            _text_tuple(self.affected_constraints, "affected_constraints", field_paths=True),
        )
        object.__setattr__(
            self,
            "expected_benefit",
            _optional_text(self.expected_benefit, "expected_benefit", maximum=4_000),
        )
        object.__setattr__(
            self,
            "engineering_cost",
            _optional_text(self.engineering_cost, "engineering_cost", maximum=4_000),
        )
        object.__setattr__(self, "target_locked", _boolean(self.target_locked, "target_locked"))
        object.__setattr__(
            self,
            "requires_user_confirmation",
            _boolean(self.requires_user_confirmation, "requires_user_confirmation"),
        )
        object.__setattr__(
            self, "source_revision", _positive_integer(self.source_revision, "source_revision")
        )
        if self.target_locked and not self.requires_user_confirmation:
            raise ValueError("locked requirement changes must require user confirmation")

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "ChangeProposal":
        payload = _payload(
            value,
            allowed={
                "proposal_id",
                "field_path",
                "old_value",
                "proposed_value",
                "reason",
                "affected_constraints",
                "expected_benefit",
                "engineering_cost",
                "target_locked",
                "requires_user_confirmation",
                "source_revision",
            },
            required={"proposal_id", "field_path", "old_value", "proposed_value", "reason"},
            name="change proposal",
        )
        return cls(**payload)

    def to_dict(self) -> dict[str, Any]:
        return {
            "proposal_id": self.proposal_id,
            "field_path": self.field_path,
            "old_value": _thaw_json(self.old_value),
            "proposed_value": _thaw_json(self.proposed_value),
            "reason": self.reason,
            "affected_constraints": list(self.affected_constraints),
            "expected_benefit": self.expected_benefit,
            "engineering_cost": self.engineering_cost,
            "target_locked": self.target_locked,
            "requires_user_confirmation": self.requires_user_confirmation,
            "source_revision": self.source_revision,
        }


@dataclass(frozen=True)
class ModelCoverageRecord:
    """Traceable statement of model support for one requirement field."""

    field_path: str
    status: ModelCoverageStatus
    model_id: str | None = None
    reason: str | None = None
    applicable_envelope: Mapping[str, Any] = field(default_factory=dict)
    blocking: bool | None = None

    def __post_init__(self) -> None:
        object.__setattr__(self, "field_path", _field_path(self.field_path))
        object.__setattr__(self, "status", _enum(self.status, ModelCoverageStatus, "coverage.status"))
        object.__setattr__(
            self, "model_id", _optional_text(self.model_id, "coverage.model_id", maximum=240)
        )
        object.__setattr__(
            self, "reason", _optional_text(self.reason, "coverage.reason", maximum=4_000)
        )
        envelope = _freeze_json(self.applicable_envelope, "coverage.applicable_envelope")
        if not isinstance(envelope, Mapping):
            raise ValueError("coverage.applicable_envelope must be an object")
        object.__setattr__(self, "applicable_envelope", envelope)
        blocking = self.status is ModelCoverageStatus.UNSUPPORTED if self.blocking is None else self.blocking
        blocking = _boolean(blocking, "coverage.blocking")
        object.__setattr__(self, "blocking", blocking)
        if self.status is not ModelCoverageStatus.COVERED and self.reason is None:
            raise ValueError("partial or unsupported model coverage requires a reason")

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "ModelCoverageRecord":
        payload = _payload(
            value,
            allowed={
                "field_path",
                "status",
                "model_id",
                "reason",
                "applicable_envelope",
                "blocking",
            },
            required={"field_path", "status"},
            name="model coverage record",
        )
        return cls(**payload)

    def to_dict(self) -> dict[str, Any]:
        return {
            "field_path": self.field_path,
            "status": self.status.value,
            "model_id": self.model_id,
            "reason": self.reason,
            "applicable_envelope": _thaw_json(self.applicable_envelope),
            "blocking": self.blocking,
        }


@dataclass(frozen=True)
class FeasibilityDiagnosis:
    """Preflight outcome that either authorizes solving or explains why it cannot."""

    status: DesignIntentStatus
    summary: str
    coverage: tuple[ModelCoverageRecord, ...] = ()
    clarification_questions: tuple[ClarificationQuestion, ...] = ()
    change_proposals: tuple[ChangeProposal, ...] = ()
    blocking_reasons: tuple[str, ...] = ()
    conflicting_fields: tuple[str, ...] = ()
    assumptions: tuple[str, ...] = ()
    ready_for_solver: bool = False

    def __post_init__(self) -> None:
        object.__setattr__(self, "status", _enum(self.status, DesignIntentStatus, "diagnosis.status"))
        object.__setattr__(self, "summary", _text(self.summary, "diagnosis.summary", maximum=8_000))
        for name, item_type in (
            ("coverage", ModelCoverageRecord),
            ("clarification_questions", ClarificationQuestion),
            ("change_proposals", ChangeProposal),
        ):
            value = getattr(self, name)
            if not isinstance(value, (list, tuple)):
                raise ValueError(f"diagnosis.{name} must be an array")
            normalized = tuple(
                item if isinstance(item, item_type) else item_type.from_dict(item) for item in value
            )
            object.__setattr__(self, name, normalized)
        object.__setattr__(
            self, "blocking_reasons", _text_tuple(self.blocking_reasons, "blocking_reasons")
        )
        object.__setattr__(
            self,
            "conflicting_fields",
            _text_tuple(self.conflicting_fields, "conflicting_fields", field_paths=True),
        )
        object.__setattr__(self, "assumptions", _text_tuple(self.assumptions, "assumptions"))
        object.__setattr__(
            self, "ready_for_solver", _boolean(self.ready_for_solver, "ready_for_solver")
        )
        self._validate_unique_keys()
        has_blocker = bool(self.blocking_reasons) or any(item.blocking for item in self.coverage)
        has_blocker = has_blocker or any(item.blocking for item in self.clarification_questions)
        if self.ready_for_solver and has_blocker:
            raise ValueError("ready_for_solver diagnosis must not contain blocking items")
        allowed_ready_statuses = {
            DesignIntentStatus.READY_FOR_SOLVER,
            DesignIntentStatus.CONCEPTUALLY_FEASIBLE,
            DesignIntentStatus.PRELIMINARY_FEASIBLE,
            DesignIntentStatus.ROBUST_PRELIMINARY_FEASIBLE,
        }
        if self.ready_for_solver and self.status not in allowed_ready_statuses:
            raise ValueError(f"diagnosis status '{self.status.value}' cannot be ready_for_solver")
        if self.status is DesignIntentStatus.READY_FOR_SOLVER and not self.ready_for_solver:
            raise ValueError("ready_for_solver status requires ready_for_solver=true")
        if self.status is DesignIntentStatus.UNSUPPORTED and not any(
            item.status is ModelCoverageStatus.UNSUPPORTED for item in self.coverage
        ):
            raise ValueError("unsupported diagnosis requires an unsupported coverage record")
        if self.status is DesignIntentStatus.REPAIRABLE and not self.change_proposals:
            raise ValueError("repairable diagnosis requires at least one change proposal")
        if self.status is DesignIntentStatus.CONTRADICTORY_REQUIREMENTS and not self.conflicting_fields:
            raise ValueError("contradictory diagnosis requires conflicting_fields")

    def _validate_unique_keys(self) -> None:
        collections = (
            ("coverage", [item.field_path for item in self.coverage]),
            ("clarification question", [item.question_id for item in self.clarification_questions]),
            ("change proposal", [item.proposal_id for item in self.change_proposals]),
        )
        for label, values in collections:
            if len(set(values)) != len(values):
                raise ValueError(f"diagnosis must not contain duplicate {label} identifiers")

    @classmethod
    def from_dict(cls, value: Mapping[str, Any]) -> "FeasibilityDiagnosis":
        payload = _payload(
            value,
            allowed={
                "status",
                "summary",
                "coverage",
                "clarification_questions",
                "change_proposals",
                "blocking_reasons",
                "conflicting_fields",
                "assumptions",
                "ready_for_solver",
            },
            required={"status", "summary"},
            name="feasibility diagnosis",
        )
        return cls(**payload)

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status.value,
            "summary": self.summary,
            "coverage": [item.to_dict() for item in self.coverage],
            "clarification_questions": [item.to_dict() for item in self.clarification_questions],
            "change_proposals": [item.to_dict() for item in self.change_proposals],
            "blocking_reasons": list(self.blocking_reasons),
            "conflicting_fields": list(self.conflicting_fields),
            "assumptions": list(self.assumptions),
            "ready_for_solver": self.ready_for_solver,
        }
