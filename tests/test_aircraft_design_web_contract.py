"""Web-boundary acceptance tests for deterministic aircraft design results."""

from __future__ import annotations

import http.client
import threading
from pathlib import Path
from unittest.mock import patch
from urllib.parse import quote

import pytest

from src.web import ClawdWebService
from src.web.app import _ClawdHTTPServer
from src.web.artifacts import AircraftArtifactStore


def test_design_preflight_reports_user_default_and_derived_sources(tmp_path: Path) -> None:
    fake_home = tmp_path / "home"
    workspace = tmp_path / "workspace"
    fake_home.mkdir()
    workspace.mkdir()
    with patch("src.agent.session.Path.home", return_value=fake_home):
        service = ClawdWebService(workspace_root=workspace)

    try:
        payload = service.preflight_design_job(
            {
                "request": {
                    "project_name": "preflight_sources",
                    "requirements": {
                        "range_m": 250_000.0,
                        "payload_kg": 20.0,
                    },
                }
            }
        )

        assert payload["ready"] is True
        assert payload["field_sources"]["requirements.range_m"] == "user"
        assert payload["field_sources"]["requirements.cruise_mach"] == "default"
        assert payload["field_sources"]["initial_guess.mtow_kg"] == "derived"
        assert payload["field_sources"]["solver.auto_repair_enabled"] == "default"
        assumptions = {item["path"]: item for item in payload["assumptions"]}
        assert assumptions["requirements.cruise_mach"]["source"] == "default"
        assert assumptions["initial_guess.mtow_kg"]["source"] == "derived"
        assert assumptions["solver.auto_repair_enabled"]["source"] == "default"
        assert any("默认或推导字段" in warning for warning in payload["warnings"])
    finally:
        service._design_jobs.shutdown()


def test_design_preflight_surfaces_engineering_risk_warnings(tmp_path: Path) -> None:
    fake_home = tmp_path / "home"
    workspace = tmp_path / "workspace"
    fake_home.mkdir()
    workspace.mkdir()
    with patch("src.agent.session.Path.home", return_value=fake_home):
        service = ClawdWebService(workspace_root=workspace)

    try:
        payload = service.preflight_design_job(
            {
                "request": {
                    "project_name": "preflight_risks",
                    "requirements": {
                        "range_m": 1_200_000.0,
                        "payload_kg": 90.0,
                        "takeoff_distance_m": 80.0,
                        "landing_distance_m": 90.0,
                        "reserve_fraction": 0.04,
                    },
                    "initial_guess": {"mtow_kg": 150.0},
                }
            }
        )

        warnings = "\n".join(payload["warnings"])
        assert "有效载荷超过 MTOW 初猜的 50%" in warnings
        assert "起降距离小于 100 m" in warnings
        assert "超过 1000 km" in warnings
        assert payload["field_sources"]["initial_guess.mtow_kg"] == "user"
    finally:
        service._design_jobs.shutdown()


def test_result_file_listing_filters_unsafe_files_and_external_symlinks(tmp_path: Path) -> None:
    workspace = tmp_path / "workspace"
    output = workspace / ".clawd" / "generated" / "run" / "output"
    nested = output / "plots"
    hidden = output / ".private"
    nested.mkdir(parents=True)
    hidden.mkdir()
    (output / "design report.md").write_text("# Design", encoding="utf-8")
    (nested / "constraint.png").write_bytes(b"png")
    (output / "geometry.obj").write_text("o aircraft\nv 0 0 0\n", encoding="utf-8")
    (output / "interactive.html").write_text("<h1>Chart</h1>", encoding="utf-8")
    (output / "solver.exe").write_bytes(b"not allowed")
    (hidden / "notes.md").write_text("hidden", encoding="utf-8")
    outside = workspace / "outside.md"
    outside.write_text("outside", encoding="utf-8")
    try:
        (output / "external.md").symlink_to(outside)
    except OSError:
        pass
    store = AircraftArtifactStore(workspace)

    files = store.list_result_files("job id", output)

    paths = {item["path"] for item in files}
    assert paths == {
        "design report.md",
        "geometry.obj",
        "interactive.html",
        "plots/constraint.png",
    }
    report = next(item for item in files if item["path"] == "design report.md")
    assert report["kind"] == "markdown"
    assert "job%20id" in report["preview_url"]
    assert "design%20report.md" in report["preview_url"]
    model = next(item for item in files if item["path"] == "geometry.obj")
    assert model["kind"] == "model"
    assert report["download_url"].endswith("?download=1")


@pytest.mark.parametrize(
    "relative_path",
    [
        "../outside.md",
        "%2e%2e/outside.md",
        "/absolute.md",
        ".",
        "",
        "solver.exe",
    ],
)
def test_result_file_resolution_rejects_traversal_and_nonpreview_files(
    tmp_path: Path,
    relative_path: str,
) -> None:
    workspace = tmp_path / "workspace"
    output = workspace / "output"
    output.mkdir(parents=True)
    (output / "report.md").write_text("report", encoding="utf-8")
    (output / "solver.exe").write_bytes(b"binary")
    store = AircraftArtifactStore(workspace)

    with pytest.raises(KeyError, match="Unknown result file"):
        store.resolve_result_file(output, relative_path)


class _ResultFileService:
    def __init__(self, store: AircraftArtifactStore, output_dir: Path) -> None:
        self.store = store
        self.output_dir = output_dir

    def resolve_design_job_file(self, job_id: str, relative_path: str) -> dict:
        if job_id != "job-preview":
            raise KeyError(job_id)
        return self.store.resolve_result_file(self.output_dir, relative_path)


def test_http_result_file_supports_inline_preview_download_and_traversal_rejection(
    tmp_path: Path,
) -> None:
    workspace = tmp_path / "workspace"
    output = workspace / "output"
    output.mkdir(parents=True)
    report_text = "# Engineering report\n\nConstraint margin: -0.35"
    report_name = "统一报告.md"
    (output / report_name).write_text(report_text, encoding="utf-8")
    service = _ResultFileService(AircraftArtifactStore(workspace), output)
    server = _ClawdHTTPServer(("127.0.0.1", 0), service)  # type: ignore[arg-type]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    connection = http.client.HTTPConnection("127.0.0.1", server.server_port, timeout=10)
    encoded_name = quote(report_name)

    try:
        connection.request("GET", f"/api/design-jobs/job-preview/files/{encoded_name}")
        inline = connection.getresponse()
        assert inline.status == 200
        assert inline.read().decode("utf-8") == report_text
        assert inline.getheader("Content-Type") == "text/markdown; charset=utf-8"
        assert inline.getheader("Content-Disposition").startswith("inline;")
        assert inline.getheader("X-Content-Type-Options") == "nosniff"

        connection.request(
            "GET",
            f"/api/design-jobs/job-preview/files/{encoded_name}?download=1",
        )
        download = connection.getresponse()
        assert download.status == 200
        assert download.read().decode("utf-8") == report_text
        assert download.getheader("Content-Disposition").startswith("attachment;")

        connection.request(
            "GET",
            "/api/design-jobs/job-preview/files/%2e%2e%2foutside.md",
        )
        traversal = connection.getresponse()
        traversal.read()
        assert traversal.status == 404
    finally:
        connection.close()
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)
