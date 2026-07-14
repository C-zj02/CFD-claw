"""Versioned requirement negotiation before aircraft sizing.

This service is the only layer that turns conversation actions into persisted
``DesignIntent`` revisions.  It deliberately keeps requirement negotiation
separate from solver execution: unsupported requirements remain visible,
defaults are materialized as their own revision, and projection is allowed
only for the explicitly confirmed current revision.
"""

from __future__ import annotations

import json
import re
from collections.abc import Iterable, Mapping, Sequence
from dataclasses import replace
from typing import Any

from src.design_execution.models import (
    AircraftDesignInitialGuess,
    AircraftDesignRequest,
    AircraftDesignRequirements,
)

from .models import (
    ChangeProposal,
    ClarificationQuestion,
    DesignIntent,
    DesignIntentStatus,
    FeasibilityDiagnosis,
    ModelCoverageStatus,
    RequirementField,
    RequirementRole,
    RequirementSource,
)
from .outcome import build_solver_outcome_revision
from .parser import parse_design_intent, with_intent_status
from .preflight import diagnose_design_intent
from .projection import complete_intent_with_solver_defaults, solver_request_from_intent
from .store import (
    DesignRevisionStore,
    IdempotencyConflictError,
    RevisionConflictError,
    SessionNotFoundError,
    canonical_json_bytes,
    canonical_sha256,
)


_QUESTION_PATH_ALIASES = {
    "mission.range_m": "requirements.range_m",
    "mission.payload_kg": "requirements.payload_kg",
    "propulsion.propulsion_type": "requirements.propulsion_type",
}

_PRELIMINARY_ASSUMPTION_OPTIONS = {
    ("requirements.cl_max_takeoff", "accept_preliminary_clmax_assumption"): 1.8,
    ("requirements.cl_max_landing", "accept_preliminary_clmax_assumption"): 2.0,
}


class DesignWorkflowError(RuntimeError):
    """Base class for requirement-workflow state or action failures."""


class WorkflowStateError(DesignWorkflowError):
    """The requested transition is not allowed from the current state."""


class WorkflowActionError(ValueError, DesignWorkflowError):
    """An action payload does not identify a valid current decision."""


class DesignRequirementWorkflow:
    """Coordinate parse, diagnosis, negotiation, confirmation, and projection.

    ``DesignRevisionStore`` remains the durable source of truth.  Every method
    that changes declared intent writes a child revision guarded by the current
    revision hash.  Retrying the same ``client_action_id`` with the same payload
    returns the previously produced final revision.
    """

    def __init__(self, store: DesignRevisionStore) -> None:
        if not isinstance(store, DesignRevisionStore):
            raise ValueError("store must be a DesignRevisionStore")
        self.store = store

    def start(
        self,
        session_id: str,
        text: str,
        *,
        client_action_id: str,
        intent_id: str | None = None,
    ) -> dict[str, Any]:
        """Parse, diagnose, and persist the first requirement revision."""

        action = self._action_payload(
            "start",
            text=text,
            intent_id=intent_id,
        )
        repeated = self._existing_action_revision(session_id, client_action_id, action)
        if repeated is not None:
            return self._finish_ready_revision(session_id, repeated, client_action_id)

        previous = self.store.load_current(session_id)
        expected_revision_hash = (
            None if previous is None else previous["revision_hash"]
        )

        parsed = parse_design_intent(text, intent_id=intent_id)
        intent, diagnosis = self._diagnosed(parsed)
        revision = self.store.save_revision(
            session_id,
            intent,
            diagnosis,
            client_action_id=client_action_id,
            expected_revision_hash=expected_revision_hash,
            decisions={"workflow_action": action},
            actor="user",
        )
        return self._finish_ready_revision(session_id, revision, client_action_id)

    def apply_change(
        self,
        session_id: str,
        *,
        proposal_id: str,
        expected_revision_hash: str,
        client_action_id: str,
        user_confirmed: bool = False,
    ) -> dict[str, Any]:
        """Apply one proposal from the current diagnosis as a child revision."""

        self._require_boolean(user_confirmed, "user_confirmed")
        action = self._action_payload(
            "apply_change",
            proposal_id=proposal_id,
            expected_revision_hash=expected_revision_hash,
            user_confirmed=user_confirmed,
        )
        repeated = self._existing_action_revision(session_id, client_action_id, action)
        if repeated is not None:
            return self._finish_ready_revision(session_id, repeated, client_action_id)

        current = self._load_current_guarded(session_id, expected_revision_hash)
        intent = DesignIntent.from_dict(current["declared_intent"])
        diagnosis = FeasibilityDiagnosis.from_dict(current["diagnosis"])
        if diagnosis.clarification_questions:
            raise WorkflowStateError(
                "clarification questions must be answered before change proposals "
                "can be applied"
            )
        proposal = next(
            (item for item in diagnosis.change_proposals if item.proposal_id == proposal_id),
            None,
        )
        if proposal is None:
            raise WorkflowActionError(
                f"proposal '{proposal_id}' is not available on the current revision"
            )

        changed = intent.apply_change(proposal, user_confirmed=user_confirmed)
        changed = self._detach_explicit_solver_fields(
            changed,
            (proposal.field_path,),
            user_provided=user_confirmed,
        )
        pending_text_paths = {
            item.field_path
            for item in diagnosis.change_proposals
            if item.proposal_id != proposal_id
            and item.proposal_id.startswith("user-text.")
        }
        if not pending_text_paths:
            changed = self._invalidate_solver_completion(changed)
        changed, next_diagnosis = self._diagnosed(changed)
        changed, next_diagnosis = self._carry_pending_text_proposals(
            changed,
            next_diagnosis,
            diagnosis,
            applied_proposal_id=proposal_id,
        )
        revision = self.store.save_revision(
            session_id,
            changed,
            next_diagnosis,
            client_action_id=client_action_id,
            expected_revision_hash=expected_revision_hash,
            decisions={
                "workflow_action": action,
                "accepted_proposal": proposal.to_dict(),
            },
            actor="user" if user_confirmed else "system",
        )
        return self._finish_ready_revision(session_id, revision, client_action_id)

    def propose_text_changes(
        self,
        session_id: str,
        text: str,
        *,
        expected_revision_hash: str,
        client_action_id: str,
    ) -> dict[str, Any]:
        """Turn an explicit natural-language edit into reviewable field diffs."""

        if not isinstance(text, str) or not text.strip():
            raise WorkflowActionError("requirement change text must be non-empty")
        action = self._action_payload(
            "propose_text_changes",
            text=text.strip(),
            expected_revision_hash=expected_revision_hash,
        )
        repeated = self._existing_action_revision(session_id, client_action_id, action)
        if repeated is not None:
            snapshot = self.current(session_id)
            if snapshot is None:  # pragma: no cover - persisted action proves the session
                raise SessionNotFoundError(f"design session '{session_id}' does not exist")
            return snapshot

        current = self._load_current_guarded(session_id, expected_revision_hash)
        intent = DesignIntent.from_dict(current["declared_intent"])
        diagnosis = FeasibilityDiagnosis.from_dict(current["diagnosis"])
        parsed = parse_design_intent(text, intent_id=intent.intent_id)
        existing = {field.path: field for field in intent.requirements}
        requested: list[tuple[RequirementField, RequirementField]] = []
        unsupported_paths: list[str] = []
        for candidate in parsed.requirements:
            if candidate.source is not RequirementSource.USER:
                continue
            current_field = existing.get(candidate.path)
            if current_field is None:
                unsupported_paths.append(candidate.path)
                continue
            if current_field.to_dict()["value"] == candidate.to_dict()["value"]:
                continue
            requested.append((current_field, candidate))

        if unsupported_paths:
            raise WorkflowActionError(
                "natural-language edits can only patch fields already present in the current "
                "revision; use a new complete design request to add: "
                + ", ".join(unsupported_paths)
            )
        if not requested:
            raise WorkflowActionError(
                "no changed field with an explicit value was found in the current revision"
            )
        if len(requested) > 3:
            raise WorkflowActionError(
                "one natural-language edit may change at most three fields"
            )

        next_revision = intent.revision + 1
        text_digest = canonical_sha256(
            {
                "text": text.strip(),
                "parent_revision_hash": expected_revision_hash,
            }
        )[:12]
        proposals = tuple(
            ChangeProposal(
                proposal_id=(
                    f"user-text.{text_digest}.{current_field.path.replace('.', '_')}"
                )[:160],
                field_path=current_field.path,
                old_value=current_field.value,
                proposed_value=candidate.value,
                reason=(
                    "The user requested this explicit field change in conversation. "
                    "The current baseline remains unchanged until this diff is confirmed."
                ),
                affected_constraints=("conversation.user_requested_change",),
                expected_benefit="Evaluates the newly requested value in a complete solver rerun.",
                engineering_cost=(
                    "May change mass, geometry, propulsion, performance, and feasibility margins."
                ),
                target_locked=current_field.locked,
                requires_user_confirmation=True,
                source_revision=next_revision,
            )
            for current_field, candidate in requested
        )
        metadata = self._append_workflow_history(
            intent,
            "text_change_requests",
            {
                "revision": next_revision,
                "text": text.strip(),
                "proposals": [item.to_dict() for item in proposals],
            },
        )
        child = replace(
            intent,
            revision=next_revision,
            status=DesignIntentStatus.REPAIRABLE,
            metadata=metadata,
        )
        child_diagnosis = FeasibilityDiagnosis(
            status=DesignIntentStatus.REPAIRABLE,
            summary=(
                "The conversation contains explicit changes to the current baseline. "
                "Review and confirm each field diff before another solver run."
            ),
            coverage=diagnosis.coverage,
            change_proposals=proposals,
            blocking_reasons=(
                "One or more user-requested field changes have not yet been confirmed.",
            ),
            assumptions=diagnosis.assumptions,
            ready_for_solver=False,
        )
        revision = self.store.save_revision(
            session_id,
            child,
            child_diagnosis,
            client_action_id=client_action_id,
            expected_revision_hash=expected_revision_hash,
            decisions={
                "workflow_action": action,
                "text_change_proposals": [item.to_dict() for item in proposals],
            },
            actor="user",
        )
        snapshot = self.current(session_id)
        if snapshot is None:  # pragma: no cover - revision was just persisted
            raise SessionNotFoundError(f"design session '{session_id}' does not exist")
        if snapshot["revision_id"] != revision["revision_id"]:
            raise RevisionConflictError("text-change proposal revision is not current")
        return snapshot

    def answer_question(
        self,
        session_id: str,
        *,
        question_id: str,
        answer: Any,
        expected_revision_hash: str,
        client_action_id: str,
        field_path: str | None = None,
    ) -> dict[str, Any]:
        """Answer one current clarification question."""

        item: dict[str, Any] = {"question_id": question_id, "value": answer}
        if field_path is not None:
            item["field_path"] = field_path
        return self.answer_questions(
            session_id,
            answers=(item,),
            expected_revision_hash=expected_revision_hash,
            client_action_id=client_action_id,
        )

    def answer_questions(
        self,
        session_id: str,
        *,
        answers: Sequence[Mapping[str, Any]],
        expected_revision_hash: str,
        client_action_id: str,
    ) -> dict[str, Any]:
        """Atomically apply up to three answers to current bounded questions."""

        normalized_answers = self._normalize_answers(answers)
        action = self._action_payload(
            "answer_questions",
            answers=normalized_answers,
            expected_revision_hash=expected_revision_hash,
        )
        repeated = self._existing_action_revision(session_id, client_action_id, action)
        if repeated is not None:
            return self._finish_ready_revision(session_id, repeated, client_action_id)

        current = self._load_current_guarded(session_id, expected_revision_hash)
        intent = DesignIntent.from_dict(current["declared_intent"])
        diagnosis = FeasibilityDiagnosis.from_dict(current["diagnosis"])
        questions = {item.question_id: item for item in diagnosis.clarification_questions}

        requirements = {field.path: field for field in intent.requirements}
        applied_answers: list[dict[str, Any]] = []
        target_paths: set[str] = set()
        for answer in normalized_answers:
            question_id = answer["question_id"]
            question = questions.get(question_id)
            if question is None:
                raise WorkflowActionError(
                    f"question '{question_id}' is not available on the current revision"
                )
            supplied_path = answer.get("field_path")
            if supplied_path is not None and supplied_path != question.field_path:
                raise WorkflowActionError(
                    f"question '{question_id}' targets '{question.field_path}', not '{supplied_path}'"
                )

            target_path = _QUESTION_PATH_ALIASES.get(question.field_path, question.field_path)
            if target_path in target_paths:
                raise WorkflowActionError(
                    f"multiple answers target the same requirement field '{target_path}'"
                )
            target_paths.add(target_path)
            value, selected_option, accepted_default = self._answer_value(
                question,
                target_path,
                answer,
            )
            existing = requirements.get(target_path)
            if existing is None:
                replacement = self._new_answer_field(
                    target_path,
                    value,
                    answer,
                    accepted_default=accepted_default,
                )
            else:
                replacement = existing.with_value(value, user_confirmed=True)
                if accepted_default:
                    replacement = replace(
                        replacement,
                        source=RequirementSource.DEFAULT,
                        confidence=0.75,
                    )
                else:
                    replacement = replace(
                        replacement,
                        source=(
                            RequirementSource.REFERENCE
                            if answer.get("source_reference")
                            else RequirementSource.USER
                        ),
                        confidence=1.0,
                        applicable_model=None,
                        source_reference=answer.get("source_reference"),
                    )
            requirements[target_path] = replacement
            applied_answers.append(
                {
                    "question_id": question_id,
                    "question_field_path": question.field_path,
                    "requirement_field_path": target_path,
                    "value": value,
                    "selected_option": selected_option,
                    "accepted_preliminary_default": accepted_default,
                }
            )

        new_revision_number = intent.revision + 1
        metadata = self._append_workflow_history(
            intent,
            "answered_questions",
            {
                "revision": new_revision_number,
                "answers": applied_answers,
            },
        )
        changed = replace(
            intent,
            requirements=tuple(requirements.values()),
            revision=new_revision_number,
            status=DesignIntentStatus.NEEDS_CLARIFICATION,
            metadata=metadata,
        )
        changed = self._detach_explicit_solver_fields(
            changed,
            target_paths,
            user_provided=False,
        )
        changed = self._invalidate_solver_completion(changed)
        changed, next_diagnosis = self._diagnosed(changed)
        revision = self.store.save_revision(
            session_id,
            changed,
            next_diagnosis,
            client_action_id=client_action_id,
            expected_revision_hash=expected_revision_hash,
            decisions={
                "workflow_action": action,
                "applied_answers": applied_answers,
            },
            actor="user",
        )
        return self._finish_ready_revision(session_id, revision, client_action_id)

    def defer_unsupported(
        self,
        session_id: str,
        *,
        field_paths: Iterable[str] | None,
        scope_statement: str,
        expected_revision_hash: str,
        client_action_id: str,
        user_confirmed: bool = False,
    ) -> dict[str, Any]:
        """Explicitly move unsupported blockers outside the solved hard scope.

        The selected fields are retained as unlocked soft goals.  Their values,
        source, coverage records, and the user's scope statement remain visible
        in the intent and audit; no unsupported requirement is deleted.
        """

        self._require_boolean(user_confirmed, "user_confirmed")
        if not user_confirmed:
            raise PermissionError("deferring unsupported requirements requires user confirmation")
        if not isinstance(scope_statement, str) or not scope_statement.strip():
            raise WorkflowActionError("scope_statement must be a non-empty user decision")
        scope_statement = scope_statement.strip()
        requested_paths = self._normalize_field_paths(field_paths)
        action = self._action_payload(
            "defer_unsupported",
            field_paths=requested_paths,
            scope_statement=scope_statement,
            expected_revision_hash=expected_revision_hash,
            user_confirmed=True,
        )
        repeated = self._existing_action_revision(session_id, client_action_id, action)
        if repeated is not None:
            return self._finish_ready_revision(session_id, repeated, client_action_id)

        current = self._load_current_guarded(session_id, expected_revision_hash)
        intent = DesignIntent.from_dict(current["declared_intent"])
        diagnosis = FeasibilityDiagnosis.from_dict(current["diagnosis"])
        if diagnosis.status is not DesignIntentStatus.UNSUPPORTED:
            raise WorkflowStateError(
                "unsupported requirements can be deferred only from the unsupported state"
            )
        if diagnosis.clarification_questions:
            raise WorkflowStateError(
                "clarification questions must be answered before unsupported requirements "
                "can be deferred"
            )
        blockers = {
            record.field_path: record
            for record in diagnosis.coverage
            if record.status is ModelCoverageStatus.UNSUPPORTED and record.blocking
        }
        if not blockers:
            raise WorkflowStateError("the current revision has no blocking unsupported field")
        selected_paths = list(requested_paths) if requested_paths else list(blockers)
        unknown = [path for path in selected_paths if path not in blockers]
        if unknown:
            raise WorkflowActionError(
                "fields are not current blocking unsupported requirements: "
                + ", ".join(unknown)
            )

        requirements = {field.path: field for field in intent.requirements}
        missing = [path for path in selected_paths if path not in requirements]
        if missing:
            raise WorkflowActionError(
                "unsupported fields lack an explicit requirement representation: "
                + ", ".join(missing)
            )

        deferrals: list[dict[str, Any]] = []
        for path in selected_paths:
            field = requirements.pop(path)
            record = blockers[path]
            retained_path = (
                f"deferred.{path}" if self._is_solver_input_path(path) else path
            )
            if retained_path in requirements:
                raise WorkflowActionError(
                    f"deferred requirement path already exists: {retained_path}"
                )
            requirements[retained_path] = replace(
                field,
                path=retained_path,
                role=RequirementRole.SOFT_GOAL,
                locked=False,
            )
            deferrals.append(
                {
                    "field_path": path,
                    "retained_field_path": retained_path,
                    "value": field.to_dict()["value"],
                    "original_role": field.role.value,
                    "original_locked": field.locked,
                    "coverage_reason": record.reason,
                    "scope_statement": scope_statement,
                }
            )

        new_revision_number = intent.revision + 1
        metadata = self._append_workflow_history(
            intent,
            "scope_deferrals",
            {
                "revision": new_revision_number,
                "scope_statement": scope_statement,
                "fields": deferrals,
            },
        )
        changed = replace(
            intent,
            requirements=tuple(requirements.values()),
            revision=new_revision_number,
            status=DesignIntentStatus.NEEDS_CLARIFICATION,
            metadata=metadata,
        )
        changed = self._invalidate_solver_completion(changed)
        changed, next_diagnosis = self._diagnosed(changed)
        revision = self.store.save_revision(
            session_id,
            changed,
            next_diagnosis,
            client_action_id=client_action_id,
            expected_revision_hash=expected_revision_hash,
            decisions={
                "workflow_action": action,
                "scope_deferrals": deferrals,
            },
            actor="user",
        )
        return self._finish_ready_revision(session_id, revision, client_action_id)

    def confirm_revision(
        self,
        session_id: str,
        *,
        expected_revision_hash: str,
        client_action_id: str,
        user_confirmed: bool = False,
        decisions: Any | None = None,
    ) -> dict[str, Any]:
        """Explicitly confirm the current, diagnosed, default-complete baseline."""

        self._require_boolean(user_confirmed, "user_confirmed")
        if not user_confirmed:
            raise PermissionError("confirm_revision requires explicit user confirmation")
        current = self._load_current_guarded(session_id, expected_revision_hash)
        intent = DesignIntent.from_dict(current["declared_intent"])
        diagnosis = FeasibilityDiagnosis.from_dict(current["diagnosis"])
        self._require_solver_ready(intent, diagnosis)
        self.store.confirm_revision(
            session_id,
            client_action_id=client_action_id,
            expected_revision_hash=expected_revision_hash,
            revision_id=current["revision_id"],
            decisions=decisions,
            confirmed_by="user",
        )
        snapshot = self.current(session_id)
        if snapshot is None:  # pragma: no cover - guarded by the loaded revision above
            raise SessionNotFoundError(f"design session '{session_id}' does not exist")
        return snapshot

    def project_solver_request(
        self,
        session_id: str,
        *,
        expected_revision_hash: str,
        project_name: str | None = None,
    ) -> AircraftDesignRequest:
        """Project only the explicitly confirmed current revision."""

        current = self._load_current_guarded(session_id, expected_revision_hash)
        workflow = self.store.load_workflow(session_id)
        if workflow is None:  # pragma: no cover - guarded by the loaded revision above
            raise SessionNotFoundError(f"design session '{session_id}' does not exist")
        confirmation = workflow.get("confirmation")
        if not isinstance(confirmation, Mapping) or (
            confirmation.get("revision_id") != current["revision_id"]
            or confirmation.get("revision_hash") != current["revision_hash"]
        ):
            raise WorkflowStateError(
                "the current requirement revision must be explicitly confirmed before projection"
            )
        intent = DesignIntent.from_dict(current["declared_intent"])
        diagnosis = FeasibilityDiagnosis.from_dict(current["diagnosis"])
        self._require_solver_ready(intent, diagnosis)
        return solver_request_from_intent(
            intent,
            project_name=project_name,
            require_ready=True,
        )

    def ingest_solver_outcome(
        self,
        session_id: str,
        *,
        revision_id: str,
        expected_revision_hash: str,
        job_id: str,
        request_hash: str,
        result: Mapping[str, Any],
    ) -> dict[str, Any]:
        """Persist one evidence-backed, unconfirmed child after a failed solve."""

        if not isinstance(revision_id, str) or not revision_id.strip():
            raise WorkflowActionError("revision_id must be a non-empty string")
        if not isinstance(job_id, str) or not job_id.strip():
            raise WorkflowActionError("job_id must be a non-empty string")
        if not isinstance(request_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", request_hash):
            raise WorkflowActionError("request_hash must be a lowercase SHA-256 hex digest")
        if not isinstance(result, Mapping):
            raise WorkflowActionError("solver result must be an object")
        submission = self.store.load_solver_submission(
            session_id,
            job_id=job_id.strip(),
            revision_id=revision_id.strip(),
            revision_hash=expected_revision_hash,
        )
        if submission is None or submission["request_hash"] != request_hash:
            raise WorkflowStateError(
                "solver outcome requires a matching server-owned submission audit"
            )
        normalized_result = self._json_safe(result)
        result_hash = canonical_sha256(normalized_result)
        action = self._action_payload(
            "ingest_solver_outcome",
            revision_id=revision_id.strip(),
            expected_revision_hash=expected_revision_hash,
            job_id=job_id.strip(),
            request_hash=request_hash,
            result_hash=result_hash,
        )
        action_id = self._solver_outcome_action_id(
            job_id.strip(),
            result_hash,
            expected_revision_hash,
        )
        repeated = self._existing_action_revision(session_id, action_id, action)
        if repeated is not None:
            snapshot = self.current(session_id)
            if snapshot is None:  # pragma: no cover - persisted action proves the session
                raise SessionNotFoundError(f"design session '{session_id}' does not exist")
            return snapshot

        current = self._load_current_guarded(session_id, expected_revision_hash)
        if current["revision_id"] != revision_id.strip():
            raise RevisionConflictError(
                f"solver outcome revision '{revision_id}' is not the current revision"
            )
        intent = DesignIntent.from_dict(current["declared_intent"])
        diagnosis = FeasibilityDiagnosis.from_dict(current["diagnosis"])
        built = build_solver_outcome_revision(
            intent,
            diagnosis,
            job_id=job_id.strip(),
            result=normalized_result,
            result_hash=result_hash,
        )
        if built is None:
            return self.current(session_id) or current
        child, child_diagnosis = built
        revision = self.store.save_revision(
            session_id,
            child,
            child_diagnosis,
            client_action_id=action_id,
            expected_revision_hash=expected_revision_hash,
            decisions={
                "workflow_action": action,
                "solver_outcome": child.metadata["solver_outcomes"][-1],
            },
            actor="system",
        )
        snapshot = self.current(session_id)
        if snapshot is None:  # pragma: no cover - revision was just persisted
            raise SessionNotFoundError(f"design session '{session_id}' does not exist")
        if snapshot["revision_id"] != revision["revision_id"]:
            raise RevisionConflictError("solver-outcome revision is not current")
        return snapshot

    def current(self, session_id: str) -> dict[str, Any] | None:
        """Return a web-ready snapshot of the current persisted revision."""

        revision = self.store.load_current(session_id)
        if revision is None:
            return None
        workflow = self.store.load_workflow(session_id)
        if workflow is None:  # pragma: no cover - store integrity prevents this
            raise SessionNotFoundError(f"design session '{session_id}' does not exist")
        intent = DesignIntent.from_dict(revision["declared_intent"])
        diagnosis = FeasibilityDiagnosis.from_dict(revision["diagnosis"])
        confirmation = workflow.get("confirmation")
        confirmed = isinstance(confirmation, Mapping) and (
            confirmation.get("revision_id") == revision["revision_id"]
            and confirmation.get("revision_hash") == revision["revision_hash"]
        )
        submission = self.store.load_solver_submission(
            session_id,
            revision_id=revision["revision_id"],
            revision_hash=revision["revision_hash"],
        )
        submitted = submission is not None
        defaults_materialized = self._defaults_materialized(intent)
        can_submit = bool(
            confirmed
            and not submitted
            and defaults_materialized
            and diagnosis.ready_for_solver
            and diagnosis.status is DesignIntentStatus.READY_FOR_SOLVER
            and intent.status is DesignIntentStatus.READY_FOR_SOLVER
        )
        return {
            "contract_version": 1,
            "session_id": session_id,
            "revision_id": revision["revision_id"],
            "revision_hash": revision["revision_hash"],
            "revision_number": revision["revision_number"],
            "persisted_revision": revision,
            "intent": revision["declared_intent"],
            "diagnosis": revision["diagnosis"],
            "confirmation": dict(confirmation) if isinstance(confirmation, Mapping) else None,
            "confirmed": bool(confirmed),
            "solver_submission": submission,
            "submitted": submitted,
            "defaults_materialized": defaults_materialized,
            "allowed_actions": self._allowed_actions(
                diagnosis,
                confirmed=bool(confirmed),
                defaults_materialized=defaults_materialized,
                submitted=submitted,
            ),
            "can_submit": can_submit,
        }

    def _finish_ready_revision(
        self,
        session_id: str,
        revision: Mapping[str, Any],
        origin_action_id: str,
    ) -> dict[str, Any]:
        diagnosis = FeasibilityDiagnosis.from_dict(revision["diagnosis"])
        intent = DesignIntent.from_dict(revision["declared_intent"])
        if diagnosis.status is not DesignIntentStatus.READY_FOR_SOLVER:
            snapshot = self.current(session_id)
            if snapshot is None:  # pragma: no cover - revision was just persisted
                raise SessionNotFoundError(f"design session '{session_id}' does not exist")
            return snapshot
        if self._defaults_materialized(intent):
            snapshot = self.current(session_id)
            if snapshot is None:  # pragma: no cover - revision was just persisted
                raise SessionNotFoundError(f"design session '{session_id}' does not exist")
            return snapshot

        intent = self._invalidate_solver_completion(intent)
        try:
            completed = complete_intent_with_solver_defaults(intent)
        except ValueError as exc:
            failure_intent, failure_diagnosis = self._completion_failure(intent, diagnosis, exc)
            action_id = self._system_action_id("completion-failure", revision["revision_hash"])
            failure_revision = self.store.save_revision(
                session_id,
                failure_intent,
                failure_diagnosis,
                client_action_id=action_id,
                expected_revision_hash=revision["revision_hash"],
                decisions={
                    "workflow_action": {
                        "type": "solver_completion_failed",
                        "origin_action_id": origin_action_id,
                        "parent_revision_hash": revision["revision_hash"],
                        "error": str(exc),
                    }
                },
                actor="system",
            )
            snapshot = self.current(session_id)
            if snapshot is None:  # pragma: no cover - revision was just persisted
                raise SessionNotFoundError(f"design session '{session_id}' does not exist")
            if snapshot["revision_id"] != failure_revision["revision_id"]:
                raise RevisionConflictError("solver-completion failure is not current")
            return snapshot

        metadata = completed.to_dict()["metadata"]
        completion = dict(metadata.get("solver_completion") or {})
        completed_revision_number = intent.revision + 1
        completion.update(
            {
                "completed": True,
                "source_revision": intent.revision,
                "valid_for_revision": completed_revision_number,
            }
        )
        metadata["solver_completion"] = completion
        completed = replace(
            completed,
            revision=completed_revision_number,
            status=DesignIntentStatus.NEEDS_CLARIFICATION,
            metadata=metadata,
        )
        completed, completed_diagnosis = self._diagnosed(completed)
        action_id = self._system_action_id("solver-defaults", revision["revision_hash"])
        completed_revision = self.store.save_revision(
            session_id,
            completed,
            completed_diagnosis,
            client_action_id=action_id,
            expected_revision_hash=revision["revision_hash"],
            decisions={
                "workflow_action": {
                    "type": "materialize_solver_defaults",
                    "origin_action_id": origin_action_id,
                    "parent_revision_hash": revision["revision_hash"],
                    "added_field_paths": completion.get("added_field_paths", []),
                }
            },
            actor="system",
        )
        snapshot = self.current(session_id)
        if snapshot is None:  # pragma: no cover - revision was just persisted
            raise SessionNotFoundError(f"design session '{session_id}' does not exist")
        if snapshot["revision_id"] != completed_revision["revision_id"]:
            raise RevisionConflictError("solver-default completion is not current")
        return snapshot

    def _completion_failure(
        self,
        intent: DesignIntent,
        prior_diagnosis: FeasibilityDiagnosis,
        error: ValueError,
    ) -> tuple[DesignIntent, FeasibilityDiagnosis]:
        message = str(error)
        match = re.search(r"(?:requirements|initial_guess)\.[A-Za-z0-9_]+", message)
        field_path = match.group(0) if match else "requirements.solver_input"
        question = ClarificationQuestion(
            question_id=f"solver_completion.{field_path.replace('.', '_')}.required",
            field_path=field_path,
            question=f"What value should be used for {field_path} so the solver input is valid?",
            reason=(
                "The declared fields passed the high-level preflight, but deterministic "
                f"solver input completion rejected the resulting baseline: {message}"
            ),
            consequence_if_unanswered="Solver defaults cannot be materialized or confirmed.",
            blocking=True,
        )
        metadata = intent.to_dict()["metadata"]
        failures = list(metadata.get("solver_completion_failures") or [])
        failures.append(
            {
                "source_revision": intent.revision,
                "field_path": field_path,
                "error": message,
            }
        )
        metadata["solver_completion_failures"] = failures
        failed_intent = replace(
            intent,
            revision=intent.revision + 1,
            status=DesignIntentStatus.NEEDS_CLARIFICATION,
            metadata=metadata,
        )
        diagnosis = FeasibilityDiagnosis(
            status=DesignIntentStatus.NEEDS_CLARIFICATION,
            summary=(
                "The baseline needs one solver-contract clarification before defaults "
                "can be materialized. No user requirement was changed."
            ),
            coverage=prior_diagnosis.coverage,
            clarification_questions=(question,),
            blocking_reasons=(message,),
            assumptions=prior_diagnosis.assumptions,
            ready_for_solver=False,
        )
        return failed_intent, diagnosis

    @staticmethod
    def _carry_pending_text_proposals(
        intent: DesignIntent,
        diagnosis: FeasibilityDiagnosis,
        previous_diagnosis: FeasibilityDiagnosis,
        *,
        applied_proposal_id: str,
    ) -> tuple[DesignIntent, FeasibilityDiagnosis]:
        """Rebase remaining diffs from one multi-field conversational edit."""

        if diagnosis.status not in {
            DesignIntentStatus.READY_FOR_SOLVER,
            DesignIntentStatus.REPAIRABLE,
        }:
            return intent, diagnosis
        remaining: list[ChangeProposal] = []
        current_fields = {field.path: field for field in intent.requirements}
        for proposal in previous_diagnosis.change_proposals:
            if (
                proposal.proposal_id == applied_proposal_id
                or not proposal.proposal_id.startswith("user-text.")
            ):
                continue
            field = current_fields.get(proposal.field_path)
            if field is None or field.to_dict()["value"] != proposal.to_dict()["old_value"]:
                continue
            remaining.append(
                replace(
                    proposal,
                    source_revision=intent.revision,
                    target_locked=field.locked,
                )
            )
        if not remaining:
            return intent, diagnosis

        occupied_paths = {item.field_path for item in remaining}
        merged = [*remaining]
        merged.extend(
            item
            for item in diagnosis.change_proposals
            if item.field_path not in occupied_paths
        )
        updated_intent = replace(intent, status=DesignIntentStatus.REPAIRABLE)
        updated_diagnosis = FeasibilityDiagnosis(
            status=DesignIntentStatus.REPAIRABLE,
            summary=(
                "Additional field diffs from the same conversational edit remain unapplied."
            ),
            coverage=diagnosis.coverage,
            change_proposals=tuple(merged),
            blocking_reasons=(
                "One or more user-requested field changes have not yet been confirmed.",
            ),
            assumptions=diagnosis.assumptions,
            ready_for_solver=False,
        )
        return updated_intent, updated_diagnosis

    @staticmethod
    def _diagnosed(intent: DesignIntent) -> tuple[DesignIntent, FeasibilityDiagnosis]:
        diagnosis = diagnose_design_intent(intent)
        return with_intent_status(intent, diagnosis.status), diagnosis

    def _load_current_guarded(
        self,
        session_id: str,
        expected_revision_hash: str,
    ) -> dict[str, Any]:
        current = self.store.load_current(session_id)
        if current is None:
            raise SessionNotFoundError(f"design session '{session_id}' does not exist")
        if expected_revision_hash != current["revision_hash"]:
            raise RevisionConflictError(
                f"stale revision hash: expected '{expected_revision_hash}', "
                f"current is '{current['revision_hash']}'"
            )
        return current

    def _existing_action_revision(
        self,
        session_id: str,
        client_action_id: str,
        action: Mapping[str, Any],
    ) -> dict[str, Any] | None:
        workflow = self.store.load_workflow(session_id)
        if workflow is None:
            return None
        entry = workflow.get("client_actions", {}).get(client_action_id)
        if entry is None:
            return None
        if entry.get("action") != "save_revision" or not isinstance(
            entry.get("revision_id"), str
        ):
            raise IdempotencyConflictError(
                f"client_action_id '{client_action_id}' was already used for another request"
            )
        revision = self.store.load_revision(session_id, entry["revision_id"])
        decisions = revision.get("decisions")
        persisted_action = (
            decisions.get("workflow_action") if isinstance(decisions, Mapping) else None
        )
        if persisted_action != action:
            raise IdempotencyConflictError(
                f"client_action_id '{client_action_id}' was already used for another request"
            )
        return revision

    @staticmethod
    def _action_payload(action_type: str, **payload: Any) -> dict[str, Any]:
        return DesignRequirementWorkflow._json_safe({"type": action_type, **payload})

    @staticmethod
    def _json_safe(value: Any) -> Any:
        return json.loads(canonical_json_bytes(value).decode("utf-8"))

    @staticmethod
    def _normalize_answers(
        answers: Sequence[Mapping[str, Any]],
    ) -> list[dict[str, Any]]:
        if not isinstance(answers, (list, tuple)) or not answers:
            raise WorkflowActionError("answers must contain between one and three items")
        if len(answers) > 3:
            raise WorkflowActionError("answers must contain between one and three items")
        allowed = {
            "question_id",
            "field_path",
            "value",
            "option",
            "unit",
            "source_reference",
        }
        normalized: list[dict[str, Any]] = []
        seen: set[str] = set()
        for index, item in enumerate(answers):
            if not isinstance(item, Mapping):
                raise WorkflowActionError(f"answers[{index}] must be an object")
            unknown = sorted(set(item) - allowed)
            if unknown:
                raise WorkflowActionError(
                    f"answers[{index}] contains unsupported fields: {', '.join(unknown)}"
                )
            question_id = item.get("question_id")
            if not isinstance(question_id, str) or not question_id.strip():
                raise WorkflowActionError(f"answers[{index}].question_id must be non-empty")
            question_id = question_id.strip()
            if question_id in seen:
                raise WorkflowActionError(f"duplicate question_id '{question_id}'")
            seen.add(question_id)
            if "value" not in item and "option" not in item:
                raise WorkflowActionError(
                    f"answers[{index}] must contain value or option"
                )
            entry = dict(item)
            entry["question_id"] = question_id
            normalized.append(DesignRequirementWorkflow._json_safe(entry))
        return normalized

    @staticmethod
    def _answer_value(
        question: ClarificationQuestion,
        target_path: str,
        answer: Mapping[str, Any],
    ) -> tuple[Any, Any | None, bool]:
        selected_option = answer.get("option")
        has_value = "value" in answer
        value = answer.get("value")
        options = [DesignRequirementWorkflow._json_safe(item) for item in question.options]
        if options:
            if selected_option is None and has_value and value in options:
                selected_option = value
            if selected_option is None:
                raise WorkflowActionError(
                    f"question '{question.question_id}' requires one of its bounded options"
                )
            if selected_option not in options:
                raise WorkflowActionError(
                    f"answer option for '{question.question_id}' is not one of the current options"
                )

        default_key = (target_path, selected_option)
        accepted_default = default_key in _PRELIMINARY_ASSUMPTION_OPTIONS
        if options and has_value and value != selected_option and not accepted_default:
            raise WorkflowActionError(
                f"answer for '{question.question_id}' cannot disagree with its selected option"
            )
        if not has_value:
            if accepted_default:
                value = _PRELIMINARY_ASSUMPTION_OPTIONS[default_key]
            elif target_path in {
                "requirements.cl_max_takeoff",
                "requirements.cl_max_landing",
            }:
                raise WorkflowActionError(
                    f"option '{selected_option}' also requires a numeric value for {target_path}"
                )
            else:
                value = selected_option
        numeric_path = bool(
            re.search(r"(?:_kg|_m|_s|_pa|mach)$", target_path.lower())
        )
        if numeric_path and isinstance(value, str):
            try:
                value = float(value.strip())
            except ValueError as exc:
                raise WorkflowActionError(
                    f"answer for '{question.question_id}' must be numeric"
                ) from exc
        return DesignRequirementWorkflow._json_safe(value), selected_option, accepted_default

    @staticmethod
    def _new_answer_field(
        path: str,
        value: Any,
        answer: Mapping[str, Any],
        *,
        accepted_default: bool,
    ) -> RequirementField:
        technology_assumption = path in {
            "requirements.cl_max_takeoff",
            "requirements.cl_max_landing",
        }
        design_variable = path.startswith("initial_guess.")
        source_reference = answer.get("source_reference")
        if source_reference is not None and (
            not isinstance(source_reference, str) or not source_reference.strip()
        ):
            raise WorkflowActionError("source_reference must be a non-empty string")
        return RequirementField(
            path=path,
            value=value,
            unit=answer.get("unit") or DesignRequirementWorkflow._unit_for(path),
            role=(
                RequirementRole.TECHNOLOGY_ASSUMPTION
                if technology_assumption
                else (
                    RequirementRole.DESIGN_VARIABLE
                    if design_variable
                    else RequirementRole.HARD_CONSTRAINT
                )
            ),
            locked=not technology_assumption and not design_variable,
            source=(
                RequirementSource.DEFAULT
                if accepted_default
                else (
                    RequirementSource.REFERENCE
                    if source_reference
                    else RequirementSource.USER
                )
            ),
            confidence=0.75 if accepted_default else 1.0,
            applicable_model=(
                "aircraft_design preliminary solver default accepted by user"
                if accepted_default
                else None
            ),
            source_reference=source_reference,
        )

    @staticmethod
    def _unit_for(path: str) -> str | None:
        leaf = path.rsplit(".", 1)[-1]
        if leaf.endswith("_kg"):
            return "kg"
        if leaf.endswith("_m"):
            return "m"
        if leaf.endswith("_s"):
            return "s"
        if leaf.endswith("_pa"):
            return "Pa"
        if "mach" in leaf:
            return "Mach"
        return None

    @staticmethod
    def _append_workflow_history(
        intent: DesignIntent,
        key: str,
        entry: Mapping[str, Any],
    ) -> dict[str, Any]:
        metadata = intent.to_dict()["metadata"]
        workflow = dict(metadata.get("requirement_workflow") or {})
        history = list(workflow.get(key) or [])
        history.append(DesignRequirementWorkflow._json_safe(entry))
        workflow[key] = history
        metadata["requirement_workflow"] = workflow
        return metadata

    @staticmethod
    def _normalize_field_paths(field_paths: Iterable[str] | None) -> list[str]:
        if field_paths is None:
            return []
        if isinstance(field_paths, str):
            raise WorkflowActionError("field_paths must be an array, not a string")
        result: list[str] = []
        for path in field_paths:
            if not isinstance(path, str) or not path.strip():
                raise WorkflowActionError("field_paths must contain non-empty strings")
            normalized = path.strip()
            if normalized not in result:
                result.append(normalized)
        return result

    @staticmethod
    def _is_solver_input_path(path: str) -> bool:
        if path.startswith("requirements."):
            name = path.removeprefix("requirements.")
            return name in AircraftDesignRequirements.__dataclass_fields__
        if path.startswith("initial_guess."):
            name = path.removeprefix("initial_guess.")
            return name in AircraftDesignInitialGuess.__dataclass_fields__
        return False

    @staticmethod
    def _defaults_materialized(intent: DesignIntent) -> bool:
        completion = intent.metadata.get("solver_completion")
        return bool(
            isinstance(completion, Mapping)
            and completion.get("completed") is True
            and completion.get("valid_for_revision") == intent.revision
        )

    @staticmethod
    def _detach_explicit_solver_fields(
        intent: DesignIntent,
        field_paths: Iterable[str],
        *,
        user_provided: bool,
    ) -> DesignIntent:
        """Stop explicitly selected fields from being discarded as old defaults."""

        paths = set(field_paths)
        if not paths:
            return intent
        requirements: list[RequirementField] = []
        for field in intent.requirements:
            if field.path in paths and user_provided:
                field = replace(
                    field,
                    source=RequirementSource.USER,
                    confidence=1.0,
                    applicable_model=None,
                    source_reference=None,
                )
            requirements.append(field)
        metadata = intent.to_dict()["metadata"]
        completion = metadata.get("solver_completion")
        if isinstance(completion, Mapping):
            updated = dict(completion)
            added = updated.get("added_field_paths")
            if isinstance(added, list):
                updated["added_field_paths"] = [path for path in added if path not in paths]
            metadata["solver_completion"] = updated
        return replace(intent, requirements=tuple(requirements), metadata=metadata)

    @staticmethod
    def _invalidate_solver_completion(intent: DesignIntent) -> DesignIntent:
        """Remove defaults derived for an older requirement revision."""

        metadata = intent.to_dict()["metadata"]
        completion = metadata.get("solver_completion")
        if not isinstance(completion, Mapping):
            return intent
        added = completion.get("added_field_paths")
        derived_paths = set(added) if isinstance(added, list) else set()
        requirements = tuple(
            field
            for field in intent.requirements
            if not (
                field.path in derived_paths
                and field.source in {RequirementSource.DEFAULT, RequirementSource.DERIVED}
            )
        )
        metadata.pop("solver_completion", None)
        return replace(intent, requirements=requirements, metadata=metadata)

    @staticmethod
    def _require_solver_ready(
        intent: DesignIntent,
        diagnosis: FeasibilityDiagnosis,
    ) -> None:
        if (
            intent.status is not DesignIntentStatus.READY_FOR_SOLVER
            or diagnosis.status is not DesignIntentStatus.READY_FOR_SOLVER
            or not diagnosis.ready_for_solver
        ):
            raise WorkflowStateError("the current requirement revision is not ready for solver")
        if not DesignRequirementWorkflow._defaults_materialized(intent):
            raise WorkflowStateError(
                "solver defaults must be materialized as an explicit revision before confirmation"
            )

    @staticmethod
    def _allowed_actions(
        diagnosis: FeasibilityDiagnosis,
        *,
        confirmed: bool,
        defaults_materialized: bool,
        submitted: bool = False,
    ) -> list[str]:
        if diagnosis.clarification_questions:
            return ["answer_questions"]
        if diagnosis.status in {
            DesignIntentStatus.CONTRADICTORY_REQUIREMENTS,
            DesignIntentStatus.REPAIRABLE,
        }:
            return ["apply_change"]
        if diagnosis.status is DesignIntentStatus.UNSUPPORTED:
            return ["defer_unsupported"]
        if diagnosis.status is DesignIntentStatus.READY_FOR_SOLVER:
            if not defaults_materialized:
                return []
            if submitted:
                return []
            return ["submit_solver"] if confirmed else ["confirm_revision"]
        return []

    @staticmethod
    def _system_action_id(kind: str, parent_revision_hash: str) -> str:
        digest = canonical_sha256(
            {"kind": kind, "parent_revision_hash": parent_revision_hash}
        )[:32]
        return f"system-{kind}-{digest}"

    @staticmethod
    def _solver_outcome_action_id(
        job_id: str,
        result_hash: str,
        parent_revision_hash: str,
    ) -> str:
        digest = canonical_sha256(
            {
                "kind": "solver-outcome",
                "job_id": job_id,
                "result_hash": result_hash,
                "parent_revision_hash": parent_revision_hash,
            }
        )[:32]
        return f"system-solver-outcome-{digest}"

    @staticmethod
    def _require_boolean(value: Any, name: str) -> None:
        if not isinstance(value, bool):
            raise WorkflowActionError(f"{name} must be a boolean")


__all__ = [
    "DesignRequirementWorkflow",
    "DesignWorkflowError",
    "WorkflowActionError",
    "WorkflowStateError",
]
