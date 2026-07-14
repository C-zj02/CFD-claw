"""Session projection tests for requirement-workflow design jobs."""

from __future__ import annotations

import copy
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

import pytest

from src.agent import Session
from src.design_intake.models import DesignIntent, FeasibilityDiagnosis
from src.design_intake.store import canonical_sha256
from src.web import ClawdWebService


class _FakeDesignJobs:
    def __init__(self, jobs: list[dict]) -> None:
        self._jobs = {job["job_id"]: copy.deepcopy(job) for job in jobs}

    def list(self) -> list[dict]:
        return [{"job_id": job_id} for job_id in self._jobs]

    def get(self, job_id: str) -> dict:
        try:
            return copy.deepcopy(self._jobs[job_id])
        except KeyError as exc:
            raise KeyError(f"Unknown design job: {job_id}") from exc


def _workflow_job(
    job_id: str,
    session_id: str,
    *,
    status: str = "completed",
    output_dir: Path | None = None,
    revision_id: str = "revision-001",
    revision_hash: str | None = None,
    terminal: bool = True,
) -> dict:
    workflow = {
        "session_id": session_id,
        "revision_id": revision_id,
    }
    if revision_hash is not None:
        workflow["revision_hash"] = revision_hash
    request = {
        "project_name": f"project_{job_id}",
        "requirements": {"range_m": 120_000.0, "payload_kg": 12.0},
        "initial_guess": {"mtow_kg": 260.0, "aspect_ratio": 7.5},
        "provenance": {"requirement_workflow": workflow},
    }
    result = None
    if output_dir is not None:
        result = {
            "run_id": job_id,
            "status": status,
            "request": copy.deepcopy(request),
            "output_dir": str(output_dir),
            "duration_seconds": 2.5,
            "converged": status == "completed",
            "engineering": {
                "numerical_converged": status == "completed",
                "engineering_feasible": status == "completed",
                "overall_status": "feasible" if status == "completed" else status,
                "blocking_failed_count": 0,
                "constraints": [],
                "stage_status": {},
            },
            "summary": {"mtow_kg": 260.0, "payload_kg": 12.0},
            "artifacts": ["design_report_v2.md", "geometry.obj"],
            "issues": [],
        }
    return {
        "job_id": job_id,
        "status": status,
        "stage": status,
        "progress": 100 if terminal else 25,
        "message": "任务完成" if status == "completed" else "求解器启动失败",
        "request": request,
        "timeout_seconds": 180.0,
        "created_at": "2026-07-14T10:00:00",
        "started_at": "2026-07-14T10:00:01",
        "finished_at": "2026-07-14T10:00:03" if terminal else None,
        "retry_of": None,
        "error": None if status == "completed" else "solver_start_failed",
        "terminal": terminal,
        "last_sequence": 1,
        "events": [],
        "result": result,
    }


def _register_session(service: ClawdWebService, session_id: str) -> None:
    session = Session(session_id=session_id, provider="openai", model="test-model")
    state = service._build_session_state(
        session=session,
        provider_name="openai",
        provider=SimpleNamespace(model="test-model"),
    )
    service._sessions[session_id] = state


def _record_server_owned_submission(
    service: ClawdWebService,
    job: dict,
    *,
    action_suffix: str,
) -> None:
    workflow = job["request"]["provenance"]["requirement_workflow"]
    session_id = workflow["session_id"]
    revision_id = workflow["revision_id"]
    previous = service._requirement_store.load_current(session_id)
    intent_revision = 1 if previous is None else previous["declared_intent"]["revision"] + 1
    revision = service._requirement_store.save_revision(
        session_id,
        DesignIntent(
            intent_id=f"intent-{session_id}",
            revision=intent_revision,
            status="ready_for_solver",
            metadata={"solver_completion": {"completed": True}},
        ),
        FeasibilityDiagnosis(
            status="ready_for_solver",
            summary="Ready for deterministic solver submission.",
            ready_for_solver=True,
        ),
        client_action_id=f"create-{action_suffix}",
        expected_revision_hash=(
            None if previous is None else previous["revision_hash"]
        ),
        revision_id=revision_id,
    )
    workflow["revision_hash"] = revision["revision_hash"]
    if isinstance(job.get("result"), dict):
        job["result"]["request"] = copy.deepcopy(job["request"])
    service._requirement_store.confirm_revision(
        session_id,
        client_action_id=f"confirm-{action_suffix}",
        expected_revision_hash=revision["revision_hash"],
        revision_id=revision_id,
    )
    service._requirement_store.record_solver_submission(
        session_id,
        job_id=job["job_id"],
        revision_id=revision_id,
        expected_revision_hash=revision["revision_hash"],
        request_hash=canonical_sha256(job["request"]),
        client_action_id=f"submit-{action_suffix}",
    )


def test_requirement_workflow_jobs_are_projected_only_to_their_web_session(
    tmp_path: Path,
) -> None:
    fake_home = tmp_path / "home"
    workspace = tmp_path / "workspace"
    fake_home.mkdir()
    workspace.mkdir()
    own_output = workspace / ".clawd" / "generated" / "aircraft_design_runs" / "job-own"
    foreign_output = workspace / ".clawd" / "generated" / "aircraft_design_runs" / "job-foreign"
    own_output.mkdir(parents=True)
    foreign_output.mkdir(parents=True)
    (own_output / "design_report_v2.md").write_text("# own report", encoding="utf-8")
    (own_output / "geometry.obj").write_text("o own_aircraft\n", encoding="utf-8")
    (foreign_output / "design_report_v2.md").write_text("# foreign report", encoding="utf-8")
    (foreign_output / "geometry.obj").write_text("o foreign_aircraft\n", encoding="utf-8")

    jobs = [
        _workflow_job(
            "job-own-completed",
            "session-a",
            output_dir=own_output,
            revision_hash="a" * 64,
        ),
        _workflow_job(
            "job-own-failed",
            "session-a",
            status="failed",
            revision_id="revision-002",
            revision_hash="c" * 64,
        ),
        _workflow_job(
            "job-foreign",
            "session-b",
            output_dir=foreign_output,
            revision_hash="b" * 64,
        ),
        _workflow_job(
            "job-own-running",
            "session-a",
            status="running",
            revision_id="revision-003",
            revision_hash="d" * 64,
            terminal=False,
        ),
        _workflow_job(
            "job-own-incomplete-provenance",
            "session-a",
            revision_hash=None,
        ),
        _workflow_job(
            "job-tampered-owner",
            "session-b",
            revision_id="revision-002",
            revision_hash="e" * 64,
        ),
    ]

    with patch("src.agent.session.Path.home", return_value=fake_home):
        service = ClawdWebService(workspace_root=workspace)
    service._design_jobs.shutdown()
    for index, job in enumerate(jobs):
        if job["job_id"] != "job-own-incomplete-provenance":
            _record_server_owned_submission(
                service,
                job,
                action_suffix=f"{index:03d}",
            )
    jobs[-1]["request"]["provenance"]["requirement_workflow"]["session_id"] = (
        "session-a"
    )
    service._design_jobs = _FakeDesignJobs(jobs)  # type: ignore[assignment]
    _register_session(service, "session-a")
    _register_session(service, "session-b")

    with patch.object(
        service,
        "_sync_requirement_solver_outcome",
        wraps=service._sync_requirement_solver_outcome,
    ) as sync_outcome:
        session_a = service.get_session_payload("session-a")["session"]
    synchronized_job_ids = {call.args[0]["job_id"] for call in sync_outcome.call_args_list}
    assert "job-foreign" not in synchronized_job_ids
    assert "job-tampered-owner" not in synchronized_job_ids
    results_a = {item["job_id"]: item for item in session_a["design_results"]}
    assert set(results_a) == {"job-own-completed", "job-own-failed"}

    completed = results_a["job-own-completed"]
    assert completed["source"] == "conversation"
    assert completed["execution_source"] == "deterministic_job"
    assert completed["session_id"] == "session-a"
    assert completed["requirement_workflow"] == {
        "session_id": "session-a",
        "revision_id": "revision-001",
        "revision_hash": service._requirement_store.load_revision(
            "session-a", "revision-001"
        )["revision_hash"],
    }
    assert completed["result"]["engineering"]["engineering_feasible"] is True
    files = {item["name"]: item for item in completed["result_files"]}
    assert set(files) == {"design_report_v2.md", "geometry.obj"}
    expected_base = "/api/sessions/session-a/design-results/job-own-completed/files/"
    assert files["design_report_v2.md"]["preview_url"].startswith(expected_base)
    assert files["geometry.obj"]["preview_url"].startswith(expected_base)

    failed = results_a["job-own-failed"]
    assert failed["terminal"] is True
    assert failed["result"]["status"] == "failed"
    assert failed["result"]["engineering"]["overall_status"] == "failed"
    assert failed["result"]["issues"][0]["code"] == "job_failed"
    assert failed["result_files"] == []

    session_b_results = service.list_session_design_results("session-b")["results"]
    assert [item["job_id"] for item in session_b_results] == ["job-foreign"]
    assert session_b_results[0]["session_id"] == "session-b"

    own_report = service.resolve_session_design_result_file(
        "session-a",
        "job-own-completed",
        "design_report_v2.md",
    )
    assert own_report["path"].read_text(encoding="utf-8") == "# own report"
    with pytest.raises(KeyError, match="Unknown session design result"):
        service.resolve_session_design_result_file(
            "session-a",
            "job-foreign",
            "design_report_v2.md",
        )
    with pytest.raises(KeyError, match="Unknown session design result"):
        service.resolve_session_design_result_file(
            "session-a",
            "job-own-failed",
            "design_report_v2.md",
        )
