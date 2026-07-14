"""Durable, auditable storage for versioned aircraft design intent.

The store deliberately exposes JSON-compatible dictionaries so a web service can
return the persisted contracts without another serialization layer.  Revision
files are immutable; mutable workflow state only points at the current revision
and records idempotency results and explicit confirmation state.
"""

from __future__ import annotations

import hashlib
import json
import math
import os
import re
import shutil
import tempfile
import threading
import uuid
from collections.abc import Mapping
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from .models import DesignIntent, FeasibilityDiagnosis


_SCHEMA_VERSION = 1
_IDENTIFIER_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$")
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class DesignRevisionStoreError(RuntimeError):
    """Base class for persistence contract failures."""


class InvalidIdentifierError(ValueError, DesignRevisionStoreError):
    """A caller supplied an unsafe session, revision, or action identifier."""


class SessionNotFoundError(FileNotFoundError, DesignRevisionStoreError):
    """The requested design session does not exist."""


class RevisionNotFoundError(FileNotFoundError, DesignRevisionStoreError):
    """The requested immutable revision does not exist."""


class RevisionAlreadyExistsError(FileExistsError, DesignRevisionStoreError):
    """An immutable revision identifier is already present."""


class RevisionConflictError(DesignRevisionStoreError):
    """Optimistic concurrency rejected a stale or unguarded mutation."""


class IdempotencyConflictError(DesignRevisionStoreError):
    """A client action identifier was reused for a different request."""


class DataIntegrityError(DesignRevisionStoreError):
    """Persisted JSON, a content hash, or the audit chain is invalid."""


def canonical_json_bytes(value: Any) -> bytes:
    """Return the one canonical JSON representation used for every SHA-256 hash."""

    normalized = _normalize_json(value, "value")
    return json.dumps(
        normalized,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def canonical_sha256(value: Any) -> str:
    """Hash JSON data after deterministic key ordering and whitespace removal."""

    return hashlib.sha256(canonical_json_bytes(value)).hexdigest()


def _normalize_json(value: Any, name: str) -> Any:
    if value is None or isinstance(value, (str, bool, int)):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise ValueError(f"{name} must contain only finite numbers")
        return value
    if isinstance(value, Mapping):
        result: dict[str, Any] = {}
        for key, item in value.items():
            if not isinstance(key, str):
                raise ValueError(f"{name} object keys must be strings")
            result[key] = _normalize_json(item, f"{name}.{key}")
        return result
    if isinstance(value, (list, tuple)):
        return [
            _normalize_json(item, f"{name}[{index}]")
            for index, item in enumerate(value)
        ]
    raise ValueError(f"{name} must be JSON-serializable")


def _identifier(value: Any, name: str) -> str:
    if not isinstance(value, str) or not _IDENTIFIER_RE.fullmatch(value):
        raise InvalidIdentifierError(
            f"{name} must be 1-128 ASCII letters, numbers, '_' or '-', "
            "and must start with a letter or number"
        )
    return value


def _utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="microseconds").replace("+00:00", "Z")


def _is_positive_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value >= 1


class DesignRevisionStore:
    """File-backed source of truth for one or more design conversations.

    Layout beneath ``root``::

        design_sessions/<session_id>/workflow.json
        design_sessions/<session_id>/revisions/<revision_id>.json
        design_sessions/<session_id>/audit.jsonl

    A single instance is safe for concurrent thread use.  Callers must retain one
    store instance per web process; cross-process locking is intentionally outside
    this local-store contract.
    """

    def __init__(self, root: str | os.PathLike[str]) -> None:
        self.root = Path(root).expanduser().resolve()
        self.sessions_root = self.root / "design_sessions"
        self._lock = threading.RLock()

    def save_revision(
        self,
        session_id: str,
        declared_intent: DesignIntent | Mapping[str, Any],
        diagnosis: FeasibilityDiagnosis | Mapping[str, Any],
        *,
        client_action_id: str,
        expected_revision_hash: str | None = None,
        revision_id: str | None = None,
        solver_request: Any | None = None,
        decisions: Any | None = None,
        actor: str = "system",
    ) -> dict[str, Any]:
        """Persist a new immutable revision and make it current.

        ``expected_revision_hash`` must equal the current hash once a session has
        a revision.  It must be ``None`` for the first revision.  Retrying the same
        request with the same ``client_action_id`` returns the original revision.
        """

        session_id = _identifier(session_id, "session_id")
        client_action_id = _identifier(client_action_id, "client_action_id")
        if revision_id is not None:
            revision_id = _identifier(revision_id, "revision_id")
        actor = self._actor(actor)
        intent_payload = self._intent_payload(declared_intent)
        diagnosis_payload = self._diagnosis_payload(diagnosis)
        solver_payload = (
            None if solver_request is None else _normalize_json(solver_request, "solver_request")
        )
        decisions_payload = None if decisions is None else _normalize_json(decisions, "decisions")
        request = {
            "action": "save_revision",
            "declared_intent": intent_payload,
            "diagnosis": diagnosis_payload,
            "solver_request": solver_payload,
            "decisions": decisions_payload,
            "requested_revision_id": revision_id,
            "actor": actor,
        }
        request_hash = canonical_sha256(request)

        with self._lock:
            workflow = self._load_workflow_unlocked(session_id)
            repeated = self._idempotent_result(
                session_id,
                workflow,
                client_action_id,
                "save_revision",
                request_hash,
            )
            if repeated is not None:
                return self._load_revision_unlocked(session_id, repeated["revision_id"])

            self._check_expected_hash(workflow, expected_revision_hash)
            revision_number = 1 if workflow is None else workflow["current_revision_number"] + 1
            parent_id = None if workflow is None else workflow["current_revision_id"]
            parent_hash = None if workflow is None else workflow["current_revision_hash"]
            actual_revision_id = revision_id or (
                f"rev-{revision_number:06d}-{uuid.uuid4().hex[:12]}"
            )
            actual_revision_id = _identifier(actual_revision_id, "revision_id")
            created_at = _utc_now()
            revision: dict[str, Any] = {
                "schema_version": _SCHEMA_VERSION,
                "session_id": session_id,
                "revision_id": actual_revision_id,
                "revision_number": revision_number,
                "parent_revision_id": parent_id,
                "parent_revision_hash": parent_hash,
                "declared_intent": intent_payload,
                "diagnosis": diagnosis_payload,
                "created_at": created_at,
            }
            if solver_payload is not None:
                revision["solver_request"] = solver_payload
            if decisions_payload is not None:
                revision["decisions"] = decisions_payload
            revision["revision_hash"] = canonical_sha256(revision)

            revision_path = self._revision_path(session_id, actual_revision_id)
            if revision_path.exists():
                raise RevisionAlreadyExistsError(
                    f"revision '{actual_revision_id}' already exists in session '{session_id}'"
                )
            self._atomic_write_json(revision_path, revision, overwrite=False)

            event = self._append_audit_event_unlocked(
                session_id,
                event_type="revision_created",
                client_action_id=client_action_id,
                revision_id=actual_revision_id,
                revision_hash=revision["revision_hash"],
                actor=actor,
                details={
                    "parent_revision_id": parent_id,
                    "revision_number": revision_number,
                    "request_hash": request_hash,
                },
            )
            updated_workflow = self._workflow_after_revision(
                workflow,
                session_id=session_id,
                revision=revision,
                client_action_id=client_action_id,
                request_hash=request_hash,
                event_hash=event["event_hash"],
            )
            self._atomic_write_json(self._workflow_path(session_id), updated_workflow)
            return dict(revision)

    def confirm_revision(
        self,
        session_id: str,
        *,
        client_action_id: str,
        expected_revision_hash: str,
        revision_id: str | None = None,
        decisions: Any | None = None,
        confirmed_by: str = "user",
    ) -> dict[str, Any]:
        """Record explicit user confirmation of the current revision.

        Confirmation does not alter the immutable revision.  It updates workflow
        state and appends a ``revision_confirmed`` hash-chained audit event.
        """

        session_id = _identifier(session_id, "session_id")
        client_action_id = _identifier(client_action_id, "client_action_id")
        if revision_id is not None:
            revision_id = _identifier(revision_id, "revision_id")
        confirmed_by = self._actor(confirmed_by, name="confirmed_by")
        decisions_payload = None if decisions is None else _normalize_json(decisions, "decisions")

        with self._lock:
            workflow = self._load_workflow_unlocked(session_id)
            if workflow is None:
                raise SessionNotFoundError(f"design session '{session_id}' does not exist")
            target_revision_id = revision_id or workflow["current_revision_id"]
            request = {
                "action": "confirm_revision",
                "revision_id": target_revision_id,
                "revision_hash": expected_revision_hash,
                "decisions": decisions_payload,
                "confirmed_by": confirmed_by,
            }
            request_hash = canonical_sha256(request)
            repeated = self._idempotent_result(
                session_id,
                workflow,
                client_action_id,
                "confirm_revision",
                request_hash,
            )
            if repeated is not None:
                return dict(repeated["confirmation"])

            self._check_expected_hash(workflow, expected_revision_hash)
            if target_revision_id != workflow["current_revision_id"]:
                raise RevisionConflictError(
                    f"revision '{target_revision_id}' is not the current revision"
                )
            existing_confirmation = workflow.get("confirmation")
            if existing_confirmation is not None:
                raise RevisionConflictError(
                    f"revision '{target_revision_id}' has already been confirmed"
                )

            confirmation: dict[str, Any] = {
                "revision_id": target_revision_id,
                "revision_hash": workflow["current_revision_hash"],
                "confirmed_by": confirmed_by,
                "confirmed_at": _utc_now(),
            }
            if decisions_payload is not None:
                confirmation["decisions"] = decisions_payload
            event = self._append_audit_event_unlocked(
                session_id,
                event_type="revision_confirmed",
                client_action_id=client_action_id,
                revision_id=target_revision_id,
                revision_hash=workflow["current_revision_hash"],
                actor=confirmed_by,
                details={"decisions": decisions_payload, "request_hash": request_hash},
            )
            updated = dict(workflow)
            updated["confirmation"] = confirmation
            updated["updated_at"] = confirmation["confirmed_at"]
            actions = dict(updated["client_actions"])
            actions[client_action_id] = {
                "action": "confirm_revision",
                "request_hash": request_hash,
                "event_hash": event["event_hash"],
                "confirmation": confirmation,
            }
            updated["client_actions"] = actions
            self._atomic_write_json(self._workflow_path(session_id), updated)
            return dict(confirmation)

    def record_solver_submission(
        self,
        session_id: str,
        *,
        job_id: str,
        revision_id: str,
        expected_revision_hash: str,
        request_hash: str,
        client_action_id: str,
        actor: str = "system",
    ) -> dict[str, Any]:
        """Bind one server-created solver job to a confirmed requirement revision.

        ``request_hash`` is the canonical SHA-256 of the complete request persisted
        by the job manager.  Consumers must compare it with the job before trusting
        the session/revision ownership recorded here.
        """

        session_id = _identifier(session_id, "session_id")
        job_id = _identifier(job_id, "job_id")
        revision_id = _identifier(revision_id, "revision_id")
        client_action_id = _identifier(client_action_id, "client_action_id")
        actor = self._actor(actor)
        self._require_sha256(expected_revision_hash, "expected_revision_hash")
        self._require_sha256(request_hash, "request_hash")
        action_request = {
            "action": "record_solver_submission",
            "job_id": job_id,
            "session_id": session_id,
            "revision_id": revision_id,
            "revision_hash": expected_revision_hash,
            "request_hash": request_hash,
            "actor": actor,
        }
        action_request_hash = canonical_sha256(action_request)

        with self._lock:
            workflow = self._load_workflow_unlocked(session_id)
            if workflow is None:
                raise SessionNotFoundError(f"design session '{session_id}' does not exist")
            repeated = self._idempotent_result(
                session_id,
                workflow,
                client_action_id,
                "record_solver_submission",
                action_request_hash,
            )
            if repeated is not None:
                submission = repeated.get("submission")
                if not isinstance(submission, dict):  # pragma: no cover - integrity guard
                    raise DataIntegrityError(
                        f"client action '{client_action_id}' has no solver submission result"
                    )
                return self._validate_solver_submission_unlocked(
                    session_id,
                    workflow,
                    submission,
                )

            self._check_expected_hash(workflow, expected_revision_hash)
            if revision_id != workflow["current_revision_id"]:
                raise RevisionConflictError(
                    f"revision '{revision_id}' is not the current revision"
                )
            confirmation = workflow.get("confirmation")
            if not isinstance(confirmation, Mapping) or (
                confirmation.get("revision_id") != revision_id
                or confirmation.get("revision_hash") != expected_revision_hash
            ):
                raise RevisionConflictError(
                    f"revision '{revision_id}' must be confirmed before solver submission"
                )

            submissions = workflow.get("solver_submissions", {})
            if not isinstance(submissions, dict):
                raise DataIntegrityError("workflow solver_submissions must be an object")
            for stored in submissions.values():
                if not isinstance(stored, Mapping):
                    raise DataIntegrityError("workflow contains an invalid solver submission")
                if (
                    stored.get("revision_id") == revision_id
                    and stored.get("revision_hash") == expected_revision_hash
                ):
                    raise RevisionConflictError(
                        f"revision '{revision_id}' already has a solver submission"
                    )
            if job_id in submissions:
                raise RevisionConflictError(f"job '{job_id}' is already bound to a submission")

            submitted_at = _utc_now()
            submission: dict[str, Any] = {
                "schema_version": _SCHEMA_VERSION,
                "job_id": job_id,
                "session_id": session_id,
                "revision_id": revision_id,
                "revision_hash": expected_revision_hash,
                "request_hash": request_hash,
                "client_action_id": client_action_id,
                "submitted_at": submitted_at,
                "action_request_hash": action_request_hash,
            }
            submission["submission_hash"] = canonical_sha256(submission)
            event = self._append_audit_event_unlocked(
                session_id,
                event_type="solver_submitted",
                client_action_id=client_action_id,
                revision_id=revision_id,
                revision_hash=expected_revision_hash,
                actor=actor,
                details={
                    "job_id": job_id,
                    "request_hash": request_hash,
                    "action_request_hash": action_request_hash,
                    "submission_hash": submission["submission_hash"],
                },
            )
            submission["audit_event_hash"] = event["event_hash"]

            updated = dict(workflow)
            updated_submissions = dict(submissions)
            updated_submissions[job_id] = submission
            updated["solver_submissions"] = updated_submissions
            updated["updated_at"] = submitted_at
            actions = dict(updated["client_actions"])
            actions[client_action_id] = {
                "action": "record_solver_submission",
                "request_hash": action_request_hash,
                "event_hash": event["event_hash"],
                "submission": submission,
            }
            updated["client_actions"] = actions
            self._atomic_write_json(self._workflow_path(session_id), updated)
            return dict(submission)

    def load_solver_submission(
        self,
        session_id: str,
        *,
        job_id: str | None = None,
        revision_id: str | None = None,
        revision_hash: str | None = None,
        client_action_id: str | None = None,
    ) -> dict[str, Any] | None:
        """Return one hash/audit-verified server-owned solver submission."""

        session_id = _identifier(session_id, "session_id")
        if job_id is not None:
            job_id = _identifier(job_id, "job_id")
        if revision_id is not None:
            revision_id = _identifier(revision_id, "revision_id")
        if revision_hash is not None:
            self._require_sha256(revision_hash, "revision_hash")
        if client_action_id is not None:
            client_action_id = _identifier(client_action_id, "client_action_id")
        if all(value is None for value in (job_id, revision_id, revision_hash, client_action_id)):
            raise ValueError("at least one solver submission selector is required")

        with self._lock:
            workflow = self._load_workflow_unlocked(session_id)
            if workflow is None:
                return None
            submissions = workflow.get("solver_submissions", {})
            if not isinstance(submissions, dict):
                raise DataIntegrityError("workflow solver_submissions must be an object")
            matches: list[dict[str, Any]] = []
            for stored_job_id, stored in submissions.items():
                if not isinstance(stored, dict) or stored.get("job_id") != stored_job_id:
                    raise DataIntegrityError("workflow contains an invalid solver submission")
                if job_id is not None and stored_job_id != job_id:
                    continue
                if revision_id is not None and stored.get("revision_id") != revision_id:
                    continue
                if revision_hash is not None and stored.get("revision_hash") != revision_hash:
                    continue
                if (
                    client_action_id is not None
                    and stored.get("client_action_id") != client_action_id
                ):
                    continue
                matches.append(
                    self._validate_solver_submission_unlocked(
                        session_id,
                        workflow,
                        stored,
                    )
                )
            if len(matches) > 1:
                raise DataIntegrityError("multiple solver submissions match one ownership query")
            return None if not matches else matches[0]

    def load_workflow(self, session_id: str) -> dict[str, Any] | None:
        """Load mutable workflow state, or ``None`` when the session is empty/missing."""

        session_id = _identifier(session_id, "session_id")
        with self._lock:
            workflow = self._load_workflow_unlocked(session_id)
            return None if workflow is None else dict(workflow)

    def load_current(self, session_id: str) -> dict[str, Any] | None:
        """Load the current immutable revision, or ``None`` when none exists."""

        session_id = _identifier(session_id, "session_id")
        with self._lock:
            workflow = self._load_workflow_unlocked(session_id)
            if workflow is None:
                return None
            return self._load_revision_unlocked(session_id, workflow["current_revision_id"])

    def load_revision(self, session_id: str, revision_id: str) -> dict[str, Any]:
        """Load and hash-verify one immutable revision."""

        session_id = _identifier(session_id, "session_id")
        revision_id = _identifier(revision_id, "revision_id")
        with self._lock:
            return self._load_revision_unlocked(session_id, revision_id)

    def load_audit(self, session_id: str) -> list[dict[str, Any]]:
        """Load all audit events after verifying the complete SHA-256 chain."""

        session_id = _identifier(session_id, "session_id")
        with self._lock:
            return self._load_audit_unlocked(session_id)

    def reset(
        self,
        session_id: str,
        *,
        expected_revision_hash: str | None = None,
    ) -> bool:
        """Clear a session while retaining an empty session/revisions directory."""

        session_id = _identifier(session_id, "session_id")
        with self._lock:
            session_path = self._session_path(session_id)
            if not session_path.exists():
                return False
            workflow = self._load_workflow_unlocked(session_id)
            self._check_expected_hash(workflow, expected_revision_hash)
            shutil.rmtree(session_path)
            self._revisions_path(session_id).mkdir(parents=True, exist_ok=False)
            return True

    def delete(
        self,
        session_id: str,
        *,
        expected_revision_hash: str | None = None,
    ) -> bool:
        """Delete a complete session after an optimistic-concurrency check."""

        session_id = _identifier(session_id, "session_id")
        with self._lock:
            session_path = self._session_path(session_id)
            if not session_path.exists():
                return False
            workflow = self._load_workflow_unlocked(session_id)
            self._check_expected_hash(workflow, expected_revision_hash)
            shutil.rmtree(session_path)
            return True

    @staticmethod
    def _actor(value: Any, *, name: str = "actor") -> str:
        if not isinstance(value, str) or not value.strip() or len(value.strip()) > 160:
            raise ValueError(f"{name} must be a non-empty string of at most 160 characters")
        return value.strip()

    @staticmethod
    def _require_sha256(value: Any, name: str) -> str:
        if not isinstance(value, str) or not _SHA256_RE.fullmatch(value):
            raise ValueError(f"{name} must be a lowercase SHA-256 hex digest")
        return value

    @staticmethod
    def _intent_payload(value: DesignIntent | Mapping[str, Any]) -> dict[str, Any]:
        try:
            intent = value if isinstance(value, DesignIntent) else DesignIntent.from_dict(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"invalid declared_intent: {exc}") from exc
        return intent.to_dict()

    @staticmethod
    def _diagnosis_payload(
        value: FeasibilityDiagnosis | Mapping[str, Any],
    ) -> dict[str, Any]:
        try:
            diagnosis = (
                value
                if isinstance(value, FeasibilityDiagnosis)
                else FeasibilityDiagnosis.from_dict(value)
            )
        except (TypeError, ValueError) as exc:
            raise ValueError(f"invalid diagnosis: {exc}") from exc
        return diagnosis.to_dict()

    def _session_path(self, session_id: str) -> Path:
        path = self.sessions_root / session_id
        self._assert_contained(path, self.sessions_root, "session path")
        return path

    def _revisions_path(self, session_id: str) -> Path:
        path = self._session_path(session_id) / "revisions"
        self._assert_contained(path, self._session_path(session_id), "revisions path")
        return path

    def _revision_path(self, session_id: str, revision_id: str) -> Path:
        revision_id = _identifier(revision_id, "revision_id")
        path = self._revisions_path(session_id) / f"{revision_id}.json"
        self._assert_contained(path, self._revisions_path(session_id), "revision path")
        return path

    def _workflow_path(self, session_id: str) -> Path:
        return self._session_path(session_id) / "workflow.json"

    def _audit_path(self, session_id: str) -> Path:
        return self._session_path(session_id) / "audit.jsonl"

    @staticmethod
    def _assert_contained(path: Path, parent: Path, name: str) -> None:
        try:
            path.resolve(strict=False).relative_to(parent.resolve(strict=False))
        except ValueError as exc:
            raise InvalidIdentifierError(f"unsafe {name}") from exc

    @staticmethod
    def _check_expected_hash(
        workflow: Mapping[str, Any] | None,
        expected_revision_hash: str | None,
    ) -> None:
        if expected_revision_hash is not None and (
            not isinstance(expected_revision_hash, str)
            or not _SHA256_RE.fullmatch(expected_revision_hash)
        ):
            raise ValueError("expected_revision_hash must be a lowercase SHA-256 hex digest")
        if workflow is None:
            if expected_revision_hash is not None:
                raise RevisionConflictError(
                    "expected_revision_hash was supplied, but the session has no current revision"
                )
            return
        current = workflow["current_revision_hash"]
        if expected_revision_hash is None:
            raise RevisionConflictError(
                "expected_revision_hash is required when mutating an existing session"
            )
        if expected_revision_hash != current:
            raise RevisionConflictError(
                f"stale revision hash: expected '{expected_revision_hash}', current is '{current}'"
            )

    def _load_workflow_unlocked(self, session_id: str) -> dict[str, Any] | None:
        path = self._workflow_path(session_id)
        if not path.exists():
            return None
        payload = self._read_json(path, "workflow")
        required = {
            "schema_version",
            "session_id",
            "current_revision_id",
            "current_revision_hash",
            "current_revision_number",
            "created_at",
            "updated_at",
            "client_actions",
        }
        if not isinstance(payload, dict) or not required.issubset(payload):
            raise DataIntegrityError("workflow.json is missing required fields")
        if payload["schema_version"] != _SCHEMA_VERSION or payload["session_id"] != session_id:
            raise DataIntegrityError("workflow.json schema or session identifier does not match")
        try:
            _identifier(payload["current_revision_id"], "workflow.current_revision_id")
        except InvalidIdentifierError as exc:
            raise DataIntegrityError(str(exc)) from exc
        if not _SHA256_RE.fullmatch(str(payload["current_revision_hash"])):
            raise DataIntegrityError("workflow current_revision_hash is invalid")
        if not _is_positive_int(payload["current_revision_number"]):
            raise DataIntegrityError("workflow current_revision_number is invalid")
        if not isinstance(payload["client_actions"], dict):
            raise DataIntegrityError("workflow client_actions must be an object")
        solver_submissions = payload.get("solver_submissions", {})
        if not isinstance(solver_submissions, dict):
            raise DataIntegrityError("workflow solver_submissions must be an object")
        current = self._load_revision_unlocked(session_id, payload["current_revision_id"])
        if (
            current["revision_hash"] != payload["current_revision_hash"]
            or current["revision_number"] != payload["current_revision_number"]
        ):
            raise DataIntegrityError("workflow current pointer does not match its revision")
        return payload

    def _validate_solver_submission_unlocked(
        self,
        session_id: str,
        workflow: Mapping[str, Any],
        submission: Mapping[str, Any],
    ) -> dict[str, Any]:
        required = {
            "schema_version",
            "job_id",
            "session_id",
            "revision_id",
            "revision_hash",
            "request_hash",
            "client_action_id",
            "submitted_at",
            "action_request_hash",
            "submission_hash",
            "audit_event_hash",
        }
        if set(submission) != required:
            raise DataIntegrityError("solver submission contains missing or unsupported fields")
        if submission.get("schema_version") != _SCHEMA_VERSION:
            raise DataIntegrityError("solver submission schema version is invalid")
        if submission.get("session_id") != session_id:
            raise DataIntegrityError("solver submission belongs to another session")
        try:
            job_id = _identifier(submission.get("job_id"), "submission.job_id")
            revision_id = _identifier(
                submission.get("revision_id"),
                "submission.revision_id",
            )
            client_action_id = _identifier(
                submission.get("client_action_id"),
                "submission.client_action_id",
            )
        except InvalidIdentifierError as exc:
            raise DataIntegrityError(str(exc)) from exc
        for field_name in (
            "revision_hash",
            "request_hash",
            "action_request_hash",
            "submission_hash",
            "audit_event_hash",
        ):
            try:
                self._require_sha256(submission.get(field_name), f"submission.{field_name}")
            except ValueError as exc:
                raise DataIntegrityError(str(exc)) from exc
        if not isinstance(submission.get("submitted_at"), str) or not submission["submitted_at"]:
            raise DataIntegrityError("solver submission submitted_at is invalid")

        hash_payload = {
            key: value
            for key, value in submission.items()
            if key not in {"submission_hash", "audit_event_hash"}
        }
        if canonical_sha256(hash_payload) != submission["submission_hash"]:
            raise DataIntegrityError("solver submission failed SHA-256 verification")

        revision = self._load_revision_unlocked(session_id, revision_id)
        if revision["revision_hash"] != submission["revision_hash"]:
            raise DataIntegrityError("solver submission revision hash does not match its revision")

        action = workflow.get("client_actions", {}).get(client_action_id)
        if not isinstance(action, Mapping) or (
            action.get("action") != "record_solver_submission"
            or action.get("request_hash") != submission["action_request_hash"]
            or action.get("event_hash") != submission["audit_event_hash"]
            or action.get("submission") != submission
        ):
            raise DataIntegrityError("solver submission client action binding is invalid")

        events = self._load_audit_unlocked(session_id)
        event = next(
            (
                item
                for item in events
                if item.get("event_hash") == submission["audit_event_hash"]
            ),
            None,
        )
        expected_details = {
            "job_id": job_id,
            "request_hash": submission["request_hash"],
            "action_request_hash": submission["action_request_hash"],
            "submission_hash": submission["submission_hash"],
        }
        if not isinstance(event, Mapping) or (
            event.get("event_type") != "solver_submitted"
            or event.get("client_action_id") != client_action_id
            or event.get("revision_id") != revision_id
            or event.get("revision_hash") != submission["revision_hash"]
            or event.get("details") != expected_details
        ):
            raise DataIntegrityError("solver submission audit binding is invalid")
        return dict(submission)

    def _load_revision_unlocked(
        self,
        session_id: str,
        revision_id: str,
    ) -> dict[str, Any]:
        path = self._revision_path(session_id, revision_id)
        if not path.exists():
            raise RevisionNotFoundError(
                f"revision '{revision_id}' does not exist in session '{session_id}'"
            )
        payload = self._read_json(path, "revision")
        required = {
            "schema_version",
            "session_id",
            "revision_id",
            "revision_number",
            "parent_revision_id",
            "parent_revision_hash",
            "declared_intent",
            "diagnosis",
            "created_at",
            "revision_hash",
        }
        allowed = required | {"solver_request", "decisions"}
        if not isinstance(payload, dict) or set(payload) != (required | (set(payload) & allowed)):
            raise DataIntegrityError("revision contains missing or unsupported fields")
        if not required.issubset(payload):
            raise DataIntegrityError("revision is missing required fields")
        if (
            payload["schema_version"] != _SCHEMA_VERSION
            or payload["session_id"] != session_id
            or payload["revision_id"] != revision_id
        ):
            raise DataIntegrityError("revision schema, session, or revision identifier does not match")
        if not _is_positive_int(payload["revision_number"]):
            raise DataIntegrityError("revision_number must be a positive integer")
        if payload["revision_number"] == 1:
            if payload["parent_revision_id"] is not None or payload["parent_revision_hash"] is not None:
                raise DataIntegrityError("the first revision must not have a parent")
        else:
            try:
                _identifier(payload["parent_revision_id"], "parent_revision_id")
            except InvalidIdentifierError as exc:
                raise DataIntegrityError(str(exc)) from exc
            if not _SHA256_RE.fullmatch(str(payload["parent_revision_hash"])):
                raise DataIntegrityError("parent_revision_hash is invalid")
        revision_hash = payload["revision_hash"]
        if not isinstance(revision_hash, str) or not _SHA256_RE.fullmatch(revision_hash):
            raise DataIntegrityError("revision_hash is invalid")
        unhashed = {key: value for key, value in payload.items() if key != "revision_hash"}
        if canonical_sha256(unhashed) != revision_hash:
            raise DataIntegrityError(f"revision '{revision_id}' failed SHA-256 verification")
        try:
            DesignIntent.from_dict(payload["declared_intent"])
            FeasibilityDiagnosis.from_dict(payload["diagnosis"])
        except (TypeError, ValueError) as exc:
            raise DataIntegrityError(f"revision contract is invalid: {exc}") from exc
        return payload

    def _load_audit_unlocked(self, session_id: str) -> list[dict[str, Any]]:
        path = self._audit_path(session_id)
        if not path.exists():
            return []
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except OSError as exc:
            raise DataIntegrityError(f"cannot read audit log: {exc}") from exc
        events: list[dict[str, Any]] = []
        previous_hash: str | None = None
        for line_number, line in enumerate(lines, start=1):
            if not line.strip():
                raise DataIntegrityError(f"audit line {line_number} is empty")
            try:
                event = json.loads(line)
            except json.JSONDecodeError as exc:
                raise DataIntegrityError(f"audit line {line_number} is invalid JSON") from exc
            if not isinstance(event, dict):
                raise DataIntegrityError(f"audit line {line_number} must be an object")
            event_hash = event.get("event_hash")
            if not isinstance(event_hash, str) or not _SHA256_RE.fullmatch(event_hash):
                raise DataIntegrityError(f"audit line {line_number} has an invalid event_hash")
            unhashed = {key: value for key, value in event.items() if key != "event_hash"}
            if canonical_sha256(unhashed) != event_hash:
                raise DataIntegrityError(f"audit line {line_number} failed SHA-256 verification")
            if event.get("previous_event_hash") != previous_hash:
                raise DataIntegrityError(f"audit chain is broken at line {line_number}")
            if event.get("session_id") != session_id:
                raise DataIntegrityError(f"audit line {line_number} belongs to another session")
            events.append(event)
            previous_hash = event_hash
        return events

    def _append_audit_event_unlocked(
        self,
        session_id: str,
        *,
        event_type: str,
        client_action_id: str,
        revision_id: str,
        revision_hash: str,
        actor: str,
        details: Any,
    ) -> dict[str, Any]:
        events = self._load_audit_unlocked(session_id)
        event: dict[str, Any] = {
            "schema_version": _SCHEMA_VERSION,
            "session_id": session_id,
            "event_id": f"evt-{len(events) + 1:06d}-{uuid.uuid4().hex[:12]}",
            "event_type": event_type,
            "client_action_id": client_action_id,
            "revision_id": revision_id,
            "revision_hash": revision_hash,
            "actor": actor,
            "details": _normalize_json(details, "audit.details"),
            "created_at": _utc_now(),
            "previous_event_hash": events[-1]["event_hash"] if events else None,
        }
        event["event_hash"] = canonical_sha256(event)
        events.append(event)
        data = b"".join(canonical_json_bytes(item) + b"\n" for item in events)
        self._atomic_write_bytes(self._audit_path(session_id), data)
        return event

    def _idempotent_result(
        self,
        session_id: str,
        workflow: Mapping[str, Any] | None,
        client_action_id: str,
        action: str,
        request_hash: str,
    ) -> dict[str, Any] | None:
        if workflow is None:
            return None
        entry = workflow["client_actions"].get(client_action_id)
        if entry is None:
            return None
        if not isinstance(entry, dict):
            raise DataIntegrityError(f"client action '{client_action_id}' is invalid")
        if entry.get("action") != action or entry.get("request_hash") != request_hash:
            raise IdempotencyConflictError(
                f"client_action_id '{client_action_id}' was already used for another request"
            )
        if action == "save_revision":
            revision_id = entry.get("revision_id")
            if not isinstance(revision_id, str):
                raise DataIntegrityError(f"client action '{client_action_id}' has no revision result")
        elif action == "confirm_revision" and not isinstance(entry.get("confirmation"), dict):
            raise DataIntegrityError(f"client action '{client_action_id}' has no confirmation result")
        elif action == "record_solver_submission" and not isinstance(
            entry.get("submission"), dict
        ):
            raise DataIntegrityError(
                f"client action '{client_action_id}' has no solver submission result"
            )
        return entry

    @staticmethod
    def _workflow_after_revision(
        workflow: Mapping[str, Any] | None,
        *,
        session_id: str,
        revision: Mapping[str, Any],
        client_action_id: str,
        request_hash: str,
        event_hash: str,
    ) -> dict[str, Any]:
        now = revision["created_at"]
        actions = {} if workflow is None else dict(workflow["client_actions"])
        actions[client_action_id] = {
            "action": "save_revision",
            "request_hash": request_hash,
            "event_hash": event_hash,
            "revision_id": revision["revision_id"],
            "revision_hash": revision["revision_hash"],
        }
        return {
            "schema_version": _SCHEMA_VERSION,
            "session_id": session_id,
            "current_revision_id": revision["revision_id"],
            "current_revision_hash": revision["revision_hash"],
            "current_revision_number": revision["revision_number"],
            "confirmation": None,
            "solver_submissions": (
                {} if workflow is None else dict(workflow.get("solver_submissions", {}))
            ),
            "created_at": now if workflow is None else workflow["created_at"],
            "updated_at": now,
            "client_actions": actions,
        }

    @staticmethod
    def _read_json(path: Path, label: str) -> Any:
        try:
            return json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            raise DataIntegrityError(f"cannot read {label} JSON: {exc}") from exc

    def _atomic_write_json(
        self,
        path: Path,
        value: Any,
        *,
        overwrite: bool = True,
    ) -> None:
        self._atomic_write_bytes(
            path,
            canonical_json_bytes(value) + b"\n",
            overwrite=overwrite,
        )

    @staticmethod
    def _atomic_write_bytes(path: Path, data: bytes, *, overwrite: bool = True) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        if not overwrite and path.exists():
            raise RevisionAlreadyExistsError(f"refusing to overwrite immutable file '{path.name}'")
        file_descriptor, temporary_name = tempfile.mkstemp(
            prefix=f".{path.name}.",
            suffix=".tmp",
            dir=path.parent,
        )
        temporary_path = Path(temporary_name)
        try:
            with os.fdopen(file_descriptor, "wb") as handle:
                handle.write(data)
                handle.flush()
                os.fsync(handle.fileno())
            if not overwrite and path.exists():
                raise RevisionAlreadyExistsError(
                    f"refusing to overwrite immutable file '{path.name}'"
                )
            os.replace(temporary_path, path)
            try:
                directory_descriptor = os.open(path.parent, os.O_RDONLY)
            except OSError:
                directory_descriptor = None
            if directory_descriptor is not None:
                try:
                    os.fsync(directory_descriptor)
                finally:
                    os.close(directory_descriptor)
        finally:
            try:
                temporary_path.unlink()
            except FileNotFoundError:
                pass


__all__ = [
    "DataIntegrityError",
    "DesignRevisionStore",
    "DesignRevisionStoreError",
    "IdempotencyConflictError",
    "InvalidIdentifierError",
    "RevisionAlreadyExistsError",
    "RevisionConflictError",
    "RevisionNotFoundError",
    "SessionNotFoundError",
    "canonical_json_bytes",
    "canonical_sha256",
]
