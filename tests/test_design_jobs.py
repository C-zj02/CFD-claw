"""Tests for background aircraft design jobs and web service integration."""

from __future__ import annotations

import http.client
import json
import tempfile
import threading
import time
import zipfile
from datetime import datetime, timedelta
from pathlib import Path
from unittest.mock import patch

import pytest

from src.design_execution import (
    AircraftDesignJobManager,
    AircraftDesignRequest,
    AircraftDesignRunner,
    DesignJobQueueFullError,
)
from src.web import ClawdWebService
from src.web.app import _ClawdHTTPServer


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def _request_payload() -> dict:
    return {
        "project_name": "background_uav",
        "requirements": {
            "range_m": 1_200_000.0,
            "payload_kg": 500.0,
            "cruise_mach": 0.22,
            "cruise_altitude_m": 6_000.0,
            "service_ceiling_m": 8_000.0,
        },
    }


def _wait_for_terminal(manager: AircraftDesignJobManager, job_id: str, timeout: float = 10.0) -> dict:
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        job = manager.get(job_id)
        if job["terminal"]:
            return job
        time.sleep(0.02)
    raise AssertionError(f"job did not finish within {timeout} seconds")


def test_background_infeasible_job_has_ordered_events_and_can_retry() -> None:
    request = AircraftDesignRequest.from_dict(_request_payload())
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        runner = AircraftDesignRunner(
            PROJECT_ROOT,
            generated_root=root / "runs",
        )
        manager = AircraftDesignJobManager(runner, metadata_root=root / "jobs", max_concurrent_jobs=1)
        submitted = manager.submit(request, timeout_seconds=30)
        completed = _wait_for_terminal(manager, submitted["job_id"])

        assert completed["status"] == "engineering_infeasible"
        assert completed["result"]["converged"] is True
        assert completed["result"]["engineering"]["numerical_converged"] is True
        assert completed["result"]["engineering"]["engineering_feasible"] is False
        assert completed["progress"] == 100
        sequences = [event["sequence"] for event in completed["events"]]
        assert sequences == list(range(1, len(sequences) + 1))
        assert (root / "jobs" / f"{completed['job_id']}.json").is_file()
        assert "stdout" not in manager.list()[0]["result"]

        retried = manager.retry(completed["job_id"])
        assert retried["retry_of"] == completed["job_id"]
        retry_completed = _wait_for_terminal(manager, retried["job_id"])
        assert retry_completed["status"] == "engineering_infeasible"
        manager.shutdown()


def test_infeasible_job_is_restored_with_result_and_can_be_retried() -> None:
    request = AircraftDesignRequest.from_dict(
        {**_request_payload(), "tolerance": 0.002, "max_iterations": 75}
    )
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        runner = AircraftDesignRunner(PROJECT_ROOT, generated_root=root / "runs")
        manager = AircraftDesignJobManager(runner, metadata_root=root / "jobs")
        submitted = manager.submit(request, timeout_seconds=30)
        completed = _wait_for_terminal(manager, submitted["job_id"])
        manager.shutdown()

        restored_manager = AircraftDesignJobManager(runner, metadata_root=root / "jobs")
        restored = restored_manager.get(completed["job_id"])

        assert restored["status"] == "engineering_infeasible"
        assert restored["request"]["tolerance"] == 0.002
        assert restored["request"]["max_iterations"] == 75
        assert restored["result"]["summary"]["mtow_kg"] > 0
        assert Path(restored["result"]["output_dir"]).is_dir()

        retried = restored_manager.retry(completed["job_id"])
        assert (
            _wait_for_terminal(restored_manager, retried["job_id"])["status"]
            == "engineering_infeasible"
        )
        restored_manager.shutdown()


def test_unfinished_persisted_job_is_marked_interrupted_on_restart() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        runner = AircraftDesignRunner(PROJECT_ROOT, generated_root=root / "runs")
        metadata_root = root / "jobs"
        metadata_root.mkdir()
        job_id = "job-20260711-120000-interrupt"
        persisted = {
            "job_id": job_id,
            "request": AircraftDesignRequest.from_dict(_request_payload()).to_dict(),
            "timeout_seconds": 30,
            "status": "running",
            "stage": "running",
            "progress": 35,
            "message": "solver running",
            "created_at": "2026-07-11T12:00:00",
            "started_at": "2026-07-11T12:00:01",
            "finished_at": None,
            "retry_of": None,
            "error": None,
            "events": [
                {
                    "sequence": 1,
                    "timestamp": "2026-07-11T12:00:00",
                    "stage": "running",
                    "message": "solver running",
                    "progress": 35,
                    "detail": None,
                }
            ],
            "result": None,
        }
        (metadata_root / f"{job_id}.json").write_text(json.dumps(persisted), encoding="utf-8")

        manager = AircraftDesignJobManager(runner, metadata_root=metadata_root)
        restored = manager.get(job_id)

        assert restored["status"] == "failed"
        assert restored["stage"] == "interrupted"
        assert restored["error"] == "service_restarted"
        assert restored["events"][-1]["detail"]["reason"] == "service_restarted"
        manager.shutdown()


class _BlockingRunner:
    def __init__(self, generated_root: Path) -> None:
        self.generated_root = generated_root
        self.generated_root.mkdir(parents=True)
        self.started = threading.Event()
        self.release = threading.Event()

    def run(self, *_args, **_kwargs):
        self.started.set()
        self.release.wait(timeout=5)
        raise RuntimeError("test runner released")


def test_job_pool_enforces_concurrency_and_queue_capacity() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        runner = _BlockingRunner(root / "runs")
        manager = AircraftDesignJobManager(
            runner,
            metadata_root=root / "jobs",
            max_concurrent_jobs=1,
            max_queued_jobs=1,
        )
        request = AircraftDesignRequest.from_dict(_request_payload())
        first = manager.submit(request)
        assert runner.started.wait(timeout=2)
        second = manager.submit(request)

        with pytest.raises(DesignJobQueueFullError, match="queue is full"):
            manager.submit(request)

        manager.cancel(second["job_id"])
        runner.release.set()
        assert _wait_for_terminal(manager, first["job_id"])["status"] == "failed"
        assert manager.get(second["job_id"])["status"] == "cancelled"
        manager.shutdown()


def test_job_history_prunes_old_terminal_metadata() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        root = Path(temp_dir)
        runner = AircraftDesignRunner(PROJECT_ROOT, generated_root=root / "runs")
        metadata_root = root / "jobs"
        metadata_root.mkdir()
        artifact_root = root / "artifacts"
        artifact_root.mkdir()
        request = AircraftDesignRequest.from_dict(_request_payload()).to_dict()
        now = datetime.now()
        for index in range(2):
            job_id = f"job-20260711-12000{index}-history"
            timestamp = (now - timedelta(minutes=index)).isoformat(timespec="seconds")
            payload = {
                "job_id": job_id,
                "request": request,
                "timeout_seconds": 30,
                "status": "failed",
                "stage": "failed",
                "progress": 100,
                "message": "failed",
                "created_at": timestamp,
                "started_at": timestamp,
                "finished_at": timestamp,
                "retry_of": None,
                "error": "test",
                "events": [],
                "result": None,
            }
            (metadata_root / f"{job_id}.json").write_text(json.dumps(payload), encoding="utf-8")
            (artifact_root / job_id).mkdir()
            (artifact_root / job_id / "result.zip").write_bytes(b"zip")

        manager = AircraftDesignJobManager(
            runner,
            metadata_root=metadata_root,
            max_history_jobs=1,
            history_ttl_days=None,
            artifact_root=artifact_root,
        )

        jobs = manager.list()
        assert len(jobs) == 1
        assert jobs[0]["job_id"] == "job-20260711-120000-history"
        assert len(list(metadata_root.glob("job-*.json"))) == 1
        assert not (artifact_root / "job-20260711-120001-history").exists()
        manager.shutdown()


def test_web_service_exposes_infeasible_job_and_diagnostic_artifact() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        workspace = Path(temp_dir) / "workspace"
        workspace.mkdir()
        generated = workspace / ".clawd" / "generated"
        runner = AircraftDesignRunner(
            PROJECT_ROOT,
            generated_root=generated / "aircraft_design_runs",
        )
        manager = AircraftDesignJobManager(runner, metadata_root=generated / "design_jobs")
        fake_home = Path(temp_dir) / "home"
        fake_home.mkdir()
        with patch("src.agent.session.Path.home", return_value=fake_home):
            service = ClawdWebService(workspace_root=workspace)
        service._aircraft_runner = runner
        service._design_jobs = manager

        submitted = service.submit_design_job({"request": _request_payload(), "timeout_seconds": 30})
        job_id = submitted["job"]["job_id"]
        _wait_for_terminal(manager, job_id)
        payload = service.get_design_job(job_id)

        assert payload["job"]["status"] == "engineering_infeasible"
        assert payload["job"]["result"]["engineering"]["engineering_feasible"] is False
        assert len(payload["job"]["artifacts"]) == 1
        artifact = payload["job"]["artifacts"][0]
        download = service.resolve_artifact_download(artifact["id"])
        assert download["path"].is_file()
        assert download["size_bytes"] > 0
        assert {item["name"] for item in payload["job"]["result_files"]} >= {
            "design_data.json",
            "design_report_v2.md",
        }
        with zipfile.ZipFile(download["path"]) as archive:
            packaged_names = set(archive.namelist())
        assert any(name.endswith("/design_data.json") for name in packaged_names)
        assert any(name.endswith("/design_report_v2.md") for name in packaged_names)
        assert any(name.endswith("/download_manifest.json") for name in packaged_names)

        manager.shutdown()
        with patch("src.agent.session.Path.home", return_value=fake_home):
            restarted = ClawdWebService(workspace_root=workspace)
        restored_payload = restarted.get_design_job(job_id)
        restored_artifact = restored_payload["job"]["artifacts"][0]
        assert restored_payload["job"]["status"] == "engineering_infeasible"
        assert restarted.resolve_artifact_download(restored_artifact["id"])["path"].is_file()
        restarted._design_jobs.shutdown()


def test_http_infeasible_job_streams_progress_and_downloadable_diagnostics() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        workspace = Path(temp_dir) / "workspace"
        workspace.mkdir()
        generated = workspace / ".clawd" / "generated"
        runner = AircraftDesignRunner(
            PROJECT_ROOT,
            generated_root=generated / "aircraft_design_runs",
        )
        manager = AircraftDesignJobManager(runner, metadata_root=generated / "design_jobs")
        fake_home = Path(temp_dir) / "home"
        fake_home.mkdir()
        with patch("src.agent.session.Path.home", return_value=fake_home):
            service = ClawdWebService(workspace_root=workspace)
        service._aircraft_runner = runner
        service._design_jobs = manager

        server = _ClawdHTTPServer(("127.0.0.1", 0), service)
        server_thread = threading.Thread(target=server.serve_forever, daemon=True)
        server_thread.start()
        connection = http.client.HTTPConnection("127.0.0.1", server.server_port, timeout=30)
        try:
            for path, content_type, marker in (
                ("/static/styles.css", "text/css", b".design-result-panel"),
                ("/static/app.js", "text/javascript", b"createDesignResultPanel"),
            ):
                connection.request("GET", path)
                static_response = connection.getresponse()
                static_body = static_response.read()
                assert static_response.status == 200
                assert content_type in static_response.getheader("Content-Type")
                assert marker in static_body

            body = json.dumps({"request": _request_payload(), "timeout_seconds": 30})
            connection.request("POST", "/api/design-jobs", body, {"Content-Type": "application/json"})
            submitted_response = connection.getresponse()
            submitted = json.loads(submitted_response.read().decode("utf-8"))

            assert submitted_response.status == 202
            job_id = submitted["job"]["job_id"]

            connection.request("GET", f"/api/design-jobs/{job_id}/stream")
            stream_response = connection.getresponse()
            stream_body = stream_response.read().decode("utf-8")

            assert stream_response.status == 200
            assert stream_response.getheader("Connection") == "close"
            blocks = [block for block in stream_body.split("\n\n") if block.strip()]
            progress_events = []
            done_payload = None
            for block in blocks:
                lines = block.splitlines()
                event_name = next(line[6:].strip() for line in lines if line.startswith("event:"))
                data = json.loads("\n".join(line[5:].lstrip() for line in lines if line.startswith("data:")))
                if event_name == "progress":
                    progress_events.append(data)
                elif event_name == "done":
                    done_payload = data

            assert progress_events
            assert [event["sequence"] for event in progress_events] == list(
                range(1, len(progress_events) + 1)
            )
            assert done_payload is not None
            assert done_payload["job"]["status"] == "engineering_infeasible"
            artifact = done_payload["job"]["artifacts"][0]

            resume_connection = http.client.HTTPConnection(
                "127.0.0.1",
                server.server_port,
                timeout=30,
            )
            try:
                resume_connection.request("GET", f"/api/design-jobs/{job_id}/stream?after=3")
                resume_response = resume_connection.getresponse()
                resume_body = resume_response.read().decode("utf-8")
                resume_blocks = [block for block in resume_body.split("\n\n") if block.strip()]
                resumed_sequences = []
                resumed_done = False
                for block in resume_blocks:
                    lines = block.splitlines()
                    event_name = next(line[6:].strip() for line in lines if line.startswith("event:"))
                    data = json.loads(
                        "\n".join(line[5:].lstrip() for line in lines if line.startswith("data:"))
                    )
                    if event_name == "progress":
                        resumed_sequences.append(data["sequence"])
                    elif event_name == "done":
                        resumed_done = data["job"]["status"] == "engineering_infeasible"
                assert resume_response.status == 200
                assert resumed_sequences
                assert all(sequence > 3 for sequence in resumed_sequences)
                assert resumed_done
            finally:
                resume_connection.close()

            connection.request("GET", artifact["download_url"])
            download_response = connection.getresponse()
            download_body = download_response.read()
            assert download_response.status == 200
            assert download_body
            assert download_response.getheader("Content-Disposition")
        finally:
            connection.close()
            server.shutdown()
            server.server_close()
            server_thread.join(timeout=2)


def test_job_request_validation_rejects_unknown_fields() -> None:
    with tempfile.TemporaryDirectory() as temp_dir:
        workspace = Path(temp_dir)
        with patch("src.agent.session.Path.home", return_value=workspace):
            service = ClawdWebService(workspace_root=workspace)

        try:
            service.submit_design_job(
                {
                    "request": {
                        **_request_payload(),
                        "requirements": {**_request_payload()["requirements"], "mystery": 1},
                    }
                }
            )
        except ValueError as exc:
            assert "unsupported requirement fields" in str(exc)
        else:
            raise AssertionError("invalid request was accepted")
