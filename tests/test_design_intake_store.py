"""Persistence tests for versioned aircraft-design intake workflows."""

from __future__ import annotations

import json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pytest

from src.design_intake.models import (
    DesignIntent,
    FeasibilityDiagnosis,
    RequirementField,
)
from src.design_intake.store import (
    DataIntegrityError,
    DesignRevisionStore,
    IdempotencyConflictError,
    InvalidIdentifierError,
    RevisionAlreadyExistsError,
    RevisionConflictError,
    RevisionNotFoundError,
    canonical_sha256,
)


def _intent(*, revision: int = 1, mtow_kg: float = 260.0) -> DesignIntent:
    return DesignIntent(
        intent_id="stealth-uav-001",
        revision=revision,
        original_request="Design a fixed-wing UAV.",
        requirements=(
            RequirementField(
                path="performance.max_takeoff_weight_kg",
                value=mtow_kg,
                unit="kg",
                role="hard_constraint",
                locked=True,
            ),
        ),
    )


def _diagnosis(summary: str = "More information is required.") -> FeasibilityDiagnosis:
    return FeasibilityDiagnosis(status="needs_clarification", summary=summary)


def _save_first(store: DesignRevisionStore, session_id: str = "session-001") -> dict:
    return store.save_revision(
        session_id,
        _intent(),
        _diagnosis(),
        client_action_id="create-001",
        revision_id="revision-001",
    )


def test_first_revision_uses_required_layout_and_canonical_hash(tmp_path: Path) -> None:
    store = DesignRevisionStore(tmp_path)

    saved = store.save_revision(
        "session-001",
        _intent(),
        _diagnosis(),
        client_action_id="create-001",
        revision_id="revision-001",
        solver_request={"mission": {"cruise_mach": 0.6}},
        decisions=[{"kind": "classification", "field": "mission.cruise_mach"}],
    )

    session_dir = tmp_path / "design_sessions" / "session-001"
    revision_path = session_dir / "revisions" / "revision-001.json"
    assert revision_path.is_file()
    assert (session_dir / "workflow.json").is_file()
    assert (session_dir / "audit.jsonl").is_file()
    assert saved["revision_number"] == 1
    assert saved["parent_revision_id"] is None
    assert saved["declared_intent"] == _intent().to_dict()
    assert saved["diagnosis"] == _diagnosis().to_dict()
    assert saved["solver_request"]["mission"]["cruise_mach"] == 0.6
    assert saved["decisions"][0]["kind"] == "classification"

    unhashed = {key: value for key, value in saved.items() if key != "revision_hash"}
    assert saved["revision_hash"] == canonical_sha256(unhashed)
    assert json.loads(revision_path.read_text(encoding="utf-8")) == saved
    assert store.load_current("session-001") == saved
    assert store.load_revision("session-001", "revision-001") == saved


def test_second_revision_has_parent_and_requires_current_hash(tmp_path: Path) -> None:
    store = DesignRevisionStore(tmp_path)
    first = _save_first(store)

    with pytest.raises(RevisionConflictError, match="required"):
        store.save_revision(
            "session-001",
            _intent(revision=2, mtow_kg=285.0),
            _diagnosis("User accepted the mass change."),
            client_action_id="create-unguarded",
        )
    with pytest.raises(RevisionConflictError, match="stale"):
        store.save_revision(
            "session-001",
            _intent(revision=2, mtow_kg=285.0),
            _diagnosis("User accepted the mass change."),
            client_action_id="create-stale",
            expected_revision_hash="0" * 64,
        )

    second = store.save_revision(
        "session-001",
        _intent(revision=2, mtow_kg=285.0),
        _diagnosis("User accepted the mass change."),
        client_action_id="create-002",
        revision_id="revision-002",
        expected_revision_hash=first["revision_hash"],
    )
    assert second["revision_number"] == 2
    assert second["parent_revision_id"] == first["revision_id"]
    assert second["parent_revision_hash"] == first["revision_hash"]
    workflow = store.load_workflow("session-001")
    assert workflow is not None
    assert workflow["current_revision_id"] == "revision-002"
    assert workflow["confirmation"] is None


def test_revision_ids_are_immutable_and_client_actions_are_idempotent(tmp_path: Path) -> None:
    store = DesignRevisionStore(tmp_path)
    first = _save_first(store)

    repeated = store.save_revision(
        "session-001",
        _intent(),
        _diagnosis(),
        client_action_id="create-001",
        revision_id="revision-001",
    )
    assert repeated == first
    assert len(store.load_audit("session-001")) == 1
    assert len(list((tmp_path / "design_sessions/session-001/revisions").glob("*.json"))) == 1

    with pytest.raises(IdempotencyConflictError, match="another request"):
        store.save_revision(
            "session-001",
            _intent(mtow_kg=300.0),
            _diagnosis(),
            client_action_id="create-001",
            expected_revision_hash=first["revision_hash"],
        )
    with pytest.raises(RevisionAlreadyExistsError, match="already exists"):
        store.save_revision(
            "session-001",
            _intent(revision=2, mtow_kg=285.0),
            _diagnosis(),
            client_action_id="create-002",
            expected_revision_hash=first["revision_hash"],
            revision_id="revision-001",
        )


def test_confirmation_is_explicit_audited_and_idempotent(tmp_path: Path) -> None:
    store = DesignRevisionStore(tmp_path)
    first = _save_first(store)
    decisions = {"accepted_change_proposal_ids": ["change-mtow-001"]}

    confirmation = store.confirm_revision(
        "session-001",
        client_action_id="confirm-001",
        expected_revision_hash=first["revision_hash"],
        decisions=decisions,
    )
    assert confirmation["revision_id"] == first["revision_id"]
    assert confirmation["revision_hash"] == first["revision_hash"]
    assert confirmation["confirmed_by"] == "user"
    assert confirmation["decisions"] == decisions
    assert store.load_revision("session-001", first["revision_id"]) == first
    assert store.load_workflow("session-001")["confirmation"] == confirmation

    repeated = store.confirm_revision(
        "session-001",
        client_action_id="confirm-001",
        expected_revision_hash=first["revision_hash"],
        decisions=decisions,
    )
    assert repeated == confirmation
    events = store.load_audit("session-001")
    assert [event["event_type"] for event in events] == [
        "revision_created",
        "revision_confirmed",
    ]
    assert events[1]["previous_event_hash"] == events[0]["event_hash"]
    for event in events:
        unhashed = {key: value for key, value in event.items() if key != "event_hash"}
        assert event["event_hash"] == canonical_sha256(unhashed)


def test_confirmation_rejects_stale_noncurrent_or_duplicate_actions(tmp_path: Path) -> None:
    store = DesignRevisionStore(tmp_path)
    first = _save_first(store)

    with pytest.raises(RevisionConflictError, match="stale"):
        store.confirm_revision(
            "session-001",
            client_action_id="confirm-stale",
            expected_revision_hash="0" * 64,
        )
    with pytest.raises(RevisionConflictError, match="not the current"):
        store.confirm_revision(
            "session-001",
            client_action_id="confirm-other",
            expected_revision_hash=first["revision_hash"],
            revision_id="unknown-revision",
        )
    store.confirm_revision(
        "session-001",
        client_action_id="confirm-001",
        expected_revision_hash=first["revision_hash"],
    )
    with pytest.raises(RevisionConflictError, match="already been confirmed"):
        store.confirm_revision(
            "session-001",
            client_action_id="confirm-002",
            expected_revision_hash=first["revision_hash"],
        )


def test_solver_submission_is_idempotent_hash_audited_and_queryable(tmp_path: Path) -> None:
    store = DesignRevisionStore(tmp_path)
    first = _save_first(store)
    store.confirm_revision(
        "session-001",
        client_action_id="confirm-001",
        expected_revision_hash=first["revision_hash"],
    )
    request_hash = canonical_sha256(
        {"project_name": "audited", "requirements": {"range_m": 120_000.0}}
    )

    submission = store.record_solver_submission(
        "session-001",
        job_id="job-001",
        revision_id=first["revision_id"],
        expected_revision_hash=first["revision_hash"],
        request_hash=request_hash,
        client_action_id="submit-001",
    )

    assert submission["job_id"] == "job-001"
    assert submission["session_id"] == "session-001"
    assert submission["revision_id"] == first["revision_id"]
    assert submission["revision_hash"] == first["revision_hash"]
    assert submission["request_hash"] == request_hash
    assert submission["client_action_id"] == "submit-001"
    assert store.load_solver_submission("session-001", job_id="job-001") == submission
    assert (
        store.load_solver_submission(
            "session-001",
            revision_id=first["revision_id"],
            revision_hash=first["revision_hash"],
        )
        == submission
    )
    repeated = store.record_solver_submission(
        "session-001",
        job_id="job-001",
        revision_id=first["revision_id"],
        expected_revision_hash=first["revision_hash"],
        request_hash=request_hash,
        client_action_id="submit-001",
    )
    assert repeated == submission
    events = store.load_audit("session-001")
    assert [event["event_type"] for event in events] == [
        "revision_created",
        "revision_confirmed",
        "solver_submitted",
    ]
    assert events[-1]["event_hash"] == submission["audit_event_hash"]

    with pytest.raises(IdempotencyConflictError, match="another request"):
        store.record_solver_submission(
            "session-001",
            job_id="job-other",
            revision_id=first["revision_id"],
            expected_revision_hash=first["revision_hash"],
            request_hash=request_hash,
            client_action_id="submit-001",
        )


def test_solver_submission_tampering_fails_closed(tmp_path: Path) -> None:
    store = DesignRevisionStore(tmp_path)
    first = _save_first(store)
    store.confirm_revision(
        "session-001",
        client_action_id="confirm-001",
        expected_revision_hash=first["revision_hash"],
    )
    store.record_solver_submission(
        "session-001",
        job_id="job-001",
        revision_id=first["revision_id"],
        expected_revision_hash=first["revision_hash"],
        request_hash="a" * 64,
        client_action_id="submit-001",
    )
    workflow_path = tmp_path / "design_sessions/session-001/workflow.json"
    workflow = json.loads(workflow_path.read_text(encoding="utf-8"))
    workflow["solver_submissions"]["job-001"]["request_hash"] = "b" * 64
    workflow_path.write_text(json.dumps(workflow), encoding="utf-8")

    with pytest.raises(DataIntegrityError, match="SHA-256"):
        store.load_solver_submission("session-001", job_id="job-001")


@pytest.mark.parametrize(
    ("session_id", "revision_id", "action_id"),
    [
        ("../escape", "revision-001", "create-001"),
        ("session-001", "../../escape", "create-001"),
        ("session-001", "revision-001", "../escape"),
        ("a/b", "revision-001", "create-001"),
    ],
)
def test_identifiers_cannot_escape_the_store_root(
    tmp_path: Path,
    session_id: str,
    revision_id: str,
    action_id: str,
) -> None:
    store = DesignRevisionStore(tmp_path)
    with pytest.raises(InvalidIdentifierError):
        store.save_revision(
            session_id,
            _intent(),
            _diagnosis(),
            client_action_id=action_id,
            revision_id=revision_id,
        )
    assert not (tmp_path.parent / "escape.json").exists()


def test_hash_and_audit_tampering_fail_closed(tmp_path: Path) -> None:
    store = DesignRevisionStore(tmp_path)
    first = _save_first(store)
    revision_path = tmp_path / "design_sessions/session-001/revisions/revision-001.json"
    payload = json.loads(revision_path.read_text(encoding="utf-8"))
    payload["declared_intent"]["aircraft_class"] = "tampered"
    revision_path.write_text(json.dumps(payload), encoding="utf-8")
    with pytest.raises(DataIntegrityError, match="SHA-256"):
        store.load_revision("session-001", "revision-001")

    # Restore the immutable revision and tamper with the audit event independently.
    revision_path.write_bytes(
        json.dumps(first, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
        + b"\n"
    )
    audit_path = tmp_path / "design_sessions/session-001/audit.jsonl"
    event = json.loads(audit_path.read_text(encoding="utf-8"))
    event["actor"] = "tampered"
    audit_path.write_text(json.dumps(event) + "\n", encoding="utf-8")
    with pytest.raises(DataIntegrityError, match="SHA-256"):
        store.load_audit("session-001")


def test_reset_and_delete_require_fresh_hash_and_have_distinct_results(tmp_path: Path) -> None:
    store = DesignRevisionStore(tmp_path)
    first = _save_first(store)
    with pytest.raises(RevisionConflictError, match="required"):
        store.reset("session-001")

    assert store.reset("session-001", expected_revision_hash=first["revision_hash"]) is True
    assert store.load_current("session-001") is None
    revisions_dir = tmp_path / "design_sessions/session-001/revisions"
    assert revisions_dir.is_dir()
    with pytest.raises(RevisionNotFoundError):
        store.load_revision("session-001", "revision-001")

    replacement = store.save_revision(
        "session-001",
        _intent(),
        _diagnosis(),
        client_action_id="replacement-001",
    )
    assert store.delete(
        "session-001", expected_revision_hash=replacement["revision_hash"]
    ) is True
    assert not (tmp_path / "design_sessions/session-001").exists()
    assert store.delete("session-001") is False


def test_rlock_serializes_threads_competing_on_one_expected_hash(tmp_path: Path) -> None:
    store = DesignRevisionStore(tmp_path)
    first = _save_first(store)

    def write(index: int) -> str:
        try:
            store.save_revision(
                "session-001",
                _intent(revision=2, mtow_kg=280.0 + index),
                _diagnosis(f"candidate {index}"),
                client_action_id=f"thread-{index}",
                expected_revision_hash=first["revision_hash"],
            )
        except RevisionConflictError:
            return "conflict"
        return "saved"

    with ThreadPoolExecutor(max_workers=2) as executor:
        results = list(executor.map(write, (1, 2)))
    assert sorted(results) == ["conflict", "saved"]
    assert store.load_current("session-001")["revision_number"] == 2
    assert len(store.load_audit("session-001")) == 2
