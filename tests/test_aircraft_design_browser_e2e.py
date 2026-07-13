"""Browser acceptance scaffolding for the aircraft design workspace."""

from __future__ import annotations

import json
import math
import re
import threading
from pathlib import Path
from urllib.parse import urlparse

import pytest


pytest.importorskip("pytest_playwright", reason="pytest-playwright is not installed")
playwright_api = pytest.importorskip("playwright.sync_api", reason="Playwright is not installed")

from src.web.app import _ClawdHTTPServer  # noqa: E402


pytestmark = pytest.mark.e2e


class _StaticOnlyService:
    """The browser route mock owns APIs; the real server supplies production assets."""


@pytest.fixture(scope="session")
def e2e_browser(playwright):
    try:
        browser = playwright.chromium.launch(headless=True)
    except playwright_api.Error as exc:
        message = str(exc).lower()
        if "executable doesn't exist" in message or "please run the following command" in message:
            pytest.skip(f"Playwright Chromium binary is unavailable: {exc}")
        raise
    yield browser
    browser.close()


@pytest.fixture()
def static_app_url():
    server = _ClawdHTTPServer(("127.0.0.1", 0), _StaticOnlyService())  # type: ignore[arg-type]
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield f"http://127.0.0.1:{server.server_port}/"
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=2)


def _session_payload(design_results: list[dict] | None = None) -> dict:
    return {
        "session_id": "e2e-session",
        "provider": "openai",
        "model": "deepseek-v4-pro",
        "auto_skill": None,
        "auto_approve": True,
        "messages": [],
        "design_results": design_results or [],
    }


def _request(project_name: str, *, payload_kg: float = 500.0) -> dict:
    return {
        "project_name": project_name,
        "requirements": {
            "range_m": 1_200_000.0,
            "payload_kg": payload_kg,
            "cruise_mach": 0.22,
            "cruise_altitude_m": 6_000.0,
            "takeoff_distance_m": 1_000.0,
            "landing_distance_m": 1_000.0,
            "max_load_factor": 3.8,
            "sustained_turn_g": 2.0,
            "service_ceiling_m": 8_000.0,
            "aircraft_role": "uav",
            "propulsion_type": "prop",
            "reserve_fraction": 0.05,
            "tail_layout": "conventional",
            "cl_max_takeoff": 1.8,
            "cl_max_landing": 2.0,
            "assumed_climb_rate_m_s": 5.0,
            "uncertainty_enabled": False,
        },
        "initial_guess": {
            "mtow_kg": 2_500.0,
            "wing_loading_pa": 3_000.0,
            "thrust_to_weight": 0.6,
            "aspect_ratio": 10.0,
            "sweep_deg": 5.0,
            "taper_ratio": 0.5,
            "thickness_ratio": 0.12,
            "prop_bsfc_kg_per_j": 8.45e-8,
            "prop_efficiency": 0.8,
            "cd0": 0.025,
            "oswald_e": 0.82,
        },
        "tolerance": 0.001,
        "max_iterations": 50,
    }


def _job(
    job_id: str,
    project_name: str,
    *,
    status: str,
    mtow_kg: float,
    engineering_feasible: bool,
    terminal: bool = True,
) -> dict:
    infeasible = not engineering_feasible
    constraint = {
        "id": "advanced.propulsion.climb_thrust_margin",
        "label": "Climb thrust margin",
        "category": "propulsion",
        "direction": "minimum",
        "required": 0.0,
        "actual": -0.35 if infeasible else 0.12,
        "unit": "ratio",
        "margin": -0.35 if infeasible else 0.12,
        "margin_ratio": -0.35 if infeasible else 0.12,
        "passed": not infeasible,
        "severity": "error" if infeasible else "info",
        "blocking": True,
        "evidence": {"model": "E2E fixture", "prediction": True},
        "recommendation": "Increase installed thrust." if infeasible else None,
    }
    result = {
        "status": status,
        "converged": True,
        "engineering": {
            "numerical_converged": True,
            "engineering_feasible": engineering_feasible,
            "overall_status": "feasible" if engineering_feasible else "infeasible",
            "blocking_failed_count": 0 if engineering_feasible else 1,
            "constraints": [constraint],
            "stage_status": {
                "class1_sizing": {
                    "status": "completed",
                    "blocking": True,
                    "message": "Converged",
                },
                "stage3_propulsion": {
                    "status": "completed" if engineering_feasible else "failed",
                    "blocking": True,
                    "message": "Propulsion gate",
                },
            },
            "requirement_comparisons": [constraint],
            "iteration_history": [
                {"iteration": 1, "mtow_kg": mtow_kg * 1.08},
                {"iteration": 2, "mtow_kg": mtow_kg},
            ],
            "design_point": {"wing_loading_pa": 3_000.0, "thrust_to_weight": 0.6},
            "recommendations": ["Increase installed thrust."] if infeasible else [],
        },
        "summary": {
            "mtow_kg": mtow_kg,
            "empty_weight_kg": mtow_kg * 0.52,
            "fuel_weight_kg": mtow_kg * 0.28,
            "payload_kg": mtow_kg * 0.2,
            "wing_area_m2": mtow_kg * 9.80665 / 3_000.0,
            "thrust_sl_n": mtow_kg * 9.80665 * 0.6,
            "wing_loading_pa": 3_000.0,
            "thrust_to_weight": 0.6,
            "span_m": 9.0,
            "actual_range_m": 1_200_000.0,
            "iterations": 12,
            "engineering_feasible": engineering_feasible,
            "engineering_status": "feasible" if engineering_feasible else "infeasible",
            "blocking_failed_count": 0 if engineering_feasible else 1,
        },
        "issues": (
            [{"code": "engineering_infeasible", "message": "Climb margin failed", "severity": "error"}]
            if infeasible
            else []
        ),
    }
    return {
        "job_id": job_id,
        "session_id": "e2e-session",
        "source": "conversation",
        "status": status,
        "stage": status,
        "progress": 100 if terminal else 35,
        "message": "任务已收敛，但方案未通过工程约束" if infeasible else "任务完成",
        "request": _request(project_name, payload_kg=500.0 if infeasible else 420.0),
        "timeout_seconds": 180.0,
        "created_at": "2026-07-11T10:00:00",
        "started_at": "2026-07-11T10:00:01",
        "finished_at": "2026-07-11T10:00:03" if terminal else None,
        "retry_of": None,
        "error": None,
        "terminal": terminal,
        "last_sequence": 2,
        "events": [
            {
                "sequence": 1,
                "timestamp": "2026-07-11T10:00:01",
                "stage": "running",
                "message": "计算中",
                "progress": 35,
                "detail": None,
            },
            {
                "sequence": 2,
                "timestamp": "2026-07-11T10:00:03",
                "stage": status,
                "message": "任务完成",
                "progress": 100 if terminal else 35,
                "detail": None,
            },
        ],
        "result": result,
        "result_files": [
            {
                "name": "design_report_v2.md",
                "path": "design_report_v2.md",
                "kind": "markdown",
                "format": "md",
                "size_bytes": 128,
                "preview_url": f"/api/design-jobs/{job_id}/files/design_report_v2.md",
                "download_url": f"/api/design-jobs/{job_id}/files/design_report_v2.md?download=1",
            },
            {
                "name": "geometry.obj",
                "path": "geometry.obj",
                "kind": "model",
                "format": "obj",
                "size_bytes": 256,
                "preview_url": f"/api/design-jobs/{job_id}/files/geometry.obj",
                "download_url": f"/api/design-jobs/{job_id}/files/geometry.obj?download=1",
            },
            {
                "name": "view_top_static.png",
                "path": "view_top_static.png",
                "kind": "image",
                "format": "png",
                "size_bytes": 128,
                "preview_url": f"/api/design-jobs/{job_id}/files/view_top_static.png",
                "download_url": f"/api/design-jobs/{job_id}/files/view_top_static.png?download=1",
            },
            {
                "name": "view_side_static.png",
                "path": "view_side_static.png",
                "kind": "image",
                "format": "png",
                "size_bytes": 128,
                "preview_url": f"/api/design-jobs/{job_id}/files/view_side_static.png",
                "download_url": f"/api/design-jobs/{job_id}/files/view_side_static.png?download=1",
            },
        ],
        "artifacts": [],
    }


def _install_api_mock(
    page,
    *,
    jobs: list[dict] | None = None,
    sessions: list[dict] | None = None,
    running_fallback: bool = False,
):
    jobs = jobs or []
    sessions = sessions or []
    detail_by_id = {job["job_id"]: job for job in jobs}
    state = {
        "detail_reads": 0,
        "stream_failures": 0,
        "preflight_calls": 0,
        "preflight_requests": [],
        "session_requests": [],
    }

    config = {
        "workspace_root": "/tmp/e2e-aircraft-workspace",
        "default_provider": "openai",
        "providers": [
            {
                "name": "openai",
                "label": "OpenAI",
                "configured": True,
                "base_url": "http://127.0.0.1",
                "default_model": "deepseek-v4-pro",
                "available_models": ["deepseek-v4-pro"],
            }
        ],
        "skills": [
            {
                "name": "aircraft-design-skill",
                "display_name": "飞行器总体设计",
                "description": "固定翼总体设计与分析工具包。",
                "when_to_use": "用于固定翼总体设计任务。",
                "status_note": "可用",
            }
        ],
        "default_auto_skill": None,
        "design_jobs": {
            "available": True,
            "max_timeout_seconds": 3_600,
            "max_concurrent_jobs": 1,
            "max_queued_jobs": 4,
            "max_history_jobs": 50,
            "history_ttl_days": 30,
        },
    }

    def fulfill_json(route, payload: dict, status: int = 200) -> None:
        route.fulfill(
            status=status,
            content_type="application/json; charset=utf-8",
            body=json.dumps(payload, ensure_ascii=False),
        )

    def handler(route) -> None:
        parsed = urlparse(route.request.url)
        path = parsed.path
        method = route.request.method
        if path == "/api/config":
            fulfill_json(route, config)
            return
        if path == "/api/sessions" and method == "POST":
            request = route.request.post_data_json or {}
            state["session_requests"].append(request)
            session = _session_payload(jobs)
            session["auto_skill"] = request.get("auto_skill")
            fulfill_json(route, {"session": session}, status=201)
            return
        if path == "/api/sessions" and method == "GET":
            fulfill_json(route, {"sessions": sessions})
            return
        if path.startswith("/api/sessions/") and method == "GET":
            session_id = path.removeprefix("/api/sessions/").strip("/")
            summary = next((item for item in sessions if item.get("session_id") == session_id), None)
            if summary is None:
                fulfill_json(route, {"error": "unknown session"}, status=404)
                return
            session = _session_payload(summary.get("design_results", []))
            session["session_id"] = session_id
            session["auto_skill"] = summary.get("auto_skill")
            fulfill_json(route, {"session": session})
            return
        if path == "/api/design-jobs/preflight" and method == "POST":
            state["preflight_calls"] += 1
            request = route.request.post_data_json["request"]
            state["preflight_requests"].append(request)
            fulfill_json(
                route,
                {
                    "ready": True,
                    "request": request,
                    "field_sources": {
                        "requirements.range_m": "user",
                        "initial_guess.mtow_kg": "derived",
                    },
                    "assumptions": [
                        {"path": "initial_guess.mtow_kg", "value": 2_500.0, "source": "derived"}
                    ],
                    "warnings": ["请复核默认与推导假设。"],
                },
            )
            return
        if path == "/api/design-jobs" and method == "GET":
            fulfill_json(route, {"jobs": jobs})
            return
        if path.endswith("/stream"):
            state["stream_failures"] += 1
            route.fulfill(status=503, content_type="text/plain", body="stream unavailable")
            return
        if path.endswith("/files/design_report_v2.md"):
            route.fulfill(
                status=200,
                content_type="text/markdown; charset=utf-8",
                body="# Engineering diagnostic\n\nClimb thrust margin failed.",
            )
            return
        if path.endswith("/files/geometry.obj"):
            route.fulfill(
                status=200,
                content_type="text/plain; charset=utf-8",
                body=(
                    "o aircraft\n"
                    "v -2 -1 0\nv 2 -1 0\nv 2 1 0\nv -2 1 0\n"
                    "v 0 0 0.8\n"
                    "f 1 2 5\nf 2 3 5\nf 3 4 5\nf 4 1 5\nf 1 4 3 2\n"
                ),
            )
            return
        if path.endswith("/files/view_top_static.png") or path.endswith("/files/view_side_static.png"):
            route.fulfill(
                status=200,
                content_type="image/svg+xml",
                body=(
                    '<svg xmlns="http://www.w3.org/2000/svg" width="640" height="420">'
                    '<rect width="640" height="420" fill="#f3f5f3"/>'
                    '<path d="M90 230 L320 90 L550 230 L350 205 L320 340 L290 205 Z" '
                    'fill="#607d78" stroke="#263d39" stroke-width="8"/>'
                    "</svg>"
                ),
            )
            return
        if path.startswith("/api/design-jobs/") and method == "GET":
            job_id = path.removeprefix("/api/design-jobs/").strip("/")
            job = detail_by_id.get(job_id)
            if job is None:
                fulfill_json(route, {"error": "unknown job"}, status=404)
                return
            state["detail_reads"] += 1
            if running_fallback and state["detail_reads"] > 1:
                terminal = _job(
                    job_id,
                    job["request"]["project_name"],
                    status="engineering_infeasible",
                    mtow_kg=2_450.0,
                    engineering_feasible=False,
                    terminal=True,
                )
                detail_by_id[job_id] = terminal
                fulfill_json(route, {"job": terminal})
            else:
                fulfill_json(route, {"job": job})
            return
        fulfill_json(route, {"error": f"unhandled mock route: {method} {path}"}, status=404)

    page.route("**/api/**", handler)
    return state


def test_chat_header_owns_aircraft_skill_toggle(
    e2e_browser,
    static_app_url: str,
) -> None:
    context = e2e_browser.new_context(viewport={"width": 1280, "height": 800})
    page = context.new_page()
    mock_state = _install_api_mock(page)
    try:
        page.goto(static_app_url)
        toggle = page.locator("#aircraftSkillToggle")
        playwright_api.expect(toggle).to_be_visible()
        playwright_api.expect(toggle).to_be_enabled()
        playwright_api.expect(toggle).not_to_be_checked()
        assert page.locator(".topbar-design-tools #aircraftSkillToggle").count() == 1
        assert page.locator("#composerForm #aircraftSkillToggle").count() == 0
        assert page.locator(".prompt-chip").count() == 0
        assert page.locator("#skillsPageBtn, #skillsView, #skillSelect").count() == 0
        playwright_api.expect(page.locator("#designWorkspaceBtn")).to_be_hidden()
        playwright_api.expect(page.locator("#designWorkspace")).to_be_hidden()
        assert page.locator("#designRunForm, #designPanelRun").count() == 0

        toggle.check()
        playwright_api.expect(toggle).to_be_checked()
        playwright_api.expect(page.locator("#skillMeta")).to_contain_text("下次发送生效")

        page.locator("#promptInput").fill("检查当前方案的总体设计约束。")
        with page.expect_response(re.compile(r"/messages/stream$")) as response_info:
            page.locator("#sendBtn").click()
        assert response_info.value.status == 503
        assert mock_state["session_requests"][-1]["auto_skill"] == "aircraft-design-skill"
    finally:
        context.close()


def test_chat_and_design_workspace_switch_without_creating_session(
    e2e_browser,
    static_app_url: str,
) -> None:
    context = e2e_browser.new_context(viewport={"width": 1280, "height": 800})
    page = context.new_page()
    result = _job(
        "conversation-result-current",
        "current_conversation_design",
        status="completed",
        mtow_kg=2_300.0,
        engineering_feasible=True,
    )
    mock_state = _install_api_mock(page, jobs=[result])
    try:
        page.goto(static_app_url)
        page.wait_for_function(
            "() => document.querySelector('#sessionMeta')?.textContent.includes('e2e-session')"
        )
        initial_session_requests = len(mock_state["session_requests"])
        assert page.locator(".sidebar-nav > #chatViewBtn").count() == 1
        assert page.locator(".sidebar-nav #designWorkspaceBtn").count() == 0
        assert page.locator(".topbar-design-tools #designWorkspaceBtn").count() == 1
        assert page.locator("#composerForm #designWorkspaceBtn").count() == 0
        assert page.locator(".window-strip, .traffic-lights, .window-actions").count() == 0
        playwright_api.expect(page.locator("#designWorkspaceBtn")).to_be_visible()

        page.locator("#designWorkspaceBtn").click()
        playwright_api.expect(page.locator("#designWorkspace")).to_be_visible()
        playwright_api.expect(page.locator("#chatLog")).to_be_hidden()
        playwright_api.expect(page.locator("#designPanelResults")).to_be_visible()
        playwright_api.expect(page.locator("#designResultsContent")).to_contain_text("工程可行")
        assert page.locator("#designRunForm, #designPanelRun, #designTabRequirements, #designTabRun").count() == 0
        playwright_api.expect(page.locator("#designTabCompare")).to_be_hidden()

        page.locator("#chatViewBtn").click()
        playwright_api.expect(page.locator("#chatLog")).to_be_visible()
        playwright_api.expect(page.locator("#composerForm")).to_be_visible()
        playwright_api.expect(page.locator("#designWorkspace")).to_be_hidden()
        assert len(mock_state["session_requests"]) == initial_session_requests

        page.locator("#designWorkspaceBtn").click()
        page.locator("#designBackChatBtn").click()
        playwright_api.expect(page.locator("#chatLog")).to_be_visible()
        assert len(mock_state["session_requests"]) == initial_session_requests
    finally:
        context.close()


def test_design_result_entry_tracks_the_selected_conversation(
    e2e_browser,
    static_app_url: str,
) -> None:
    result = _job(
        "conversation-result-history",
        "history_design",
        status="completed",
        mtow_kg=1_900.0,
        engineering_feasible=True,
    )
    sessions = [
        {
            "session_id": "plain-conversation",
            "provider": "openai",
            "model": "deepseek-v4-pro",
            "last_message": "普通问答",
            "message_count": 2,
            "updated_at": "2026-07-13T10:00:00",
            "design_results": [],
        },
        {
            "session_id": "design-conversation",
            "provider": "openai",
            "model": "deepseek-v4-pro",
            "last_message": "已完成总体设计",
            "message_count": 4,
            "updated_at": "2026-07-13T11:00:00",
            "design_results": [result],
        },
    ]
    context = e2e_browser.new_context(viewport={"width": 1280, "height": 800})
    page = context.new_page()
    mock_state = _install_api_mock(page, jobs=[result], sessions=sessions)
    try:
        page.goto(static_app_url)
        playwright_api.expect(page.locator("#designWorkspaceBtn")).to_be_visible()
        initial_session_requests = len(mock_state["session_requests"])

        page.get_by_text(re.compile(r"^普通问答 · 2 条消息$")).click()
        playwright_api.expect(page.locator("#sessionMeta")).to_contain_text("plain-conversation")
        playwright_api.expect(page.locator("#designWorkspaceBtn")).to_be_hidden()
        playwright_api.expect(page.locator("#designWorkspace")).to_be_hidden()

        page.get_by_text(re.compile(r"^已完成总体设计 · 4 条消息$")).click()
        playwright_api.expect(page.locator("#sessionMeta")).to_contain_text("design-conversation")
        playwright_api.expect(page.locator("#designWorkspaceBtn")).to_be_visible()
        page.locator("#designWorkspaceBtn").click()
        playwright_api.expect(page.locator("#designResultsContent")).to_contain_text("工程可行")
        assert len(mock_state["session_requests"]) == initial_session_requests
    finally:
        context.close()


@pytest.mark.parametrize(
    "viewport",
    [
        {"width": 390, "height": 844},
        {"width": 768, "height": 1024},
        {"width": 1440, "height": 900},
    ],
    ids=["mobile-390", "tablet-768", "desktop-1440"],
)
def test_workspace_tabs_keyboard_focus_and_responsive_layout(
    e2e_browser,
    static_app_url: str,
    viewport: dict[str, int],
) -> None:
    context = e2e_browser.new_context(viewport=viewport)
    page = context.new_page()
    long_session_history = [
        {
            "session_id": f"responsive-session-{index}",
            "provider": "openai",
            "model": "deepseek-v4-pro",
            "last_message": "A deliberately long session title used to exercise responsive navigation",
            "message_count": index + 1,
            "updated_at": "2026-07-11T10:00:00",
        }
        for index in range(24)
    ]
    responsive_result = _job(
        "conversation-result-responsive",
        "responsive_design",
        status="completed",
        mtow_kg=2_100.0,
        engineering_feasible=True,
    )
    _install_api_mock(page, jobs=[responsive_result], sessions=long_session_history)
    try:
        page.goto(static_app_url)
        playwright_api.expect(page.locator(".topbar-design-tools")).to_be_visible()
        assert page.locator("#composerForm #aircraftSkillToggle, #composerForm #designWorkspaceBtn").count() == 0
        header_geometry = page.evaluate(
            """() => {
                const topbar = document.querySelector('.topbar').getBoundingClientRect();
                const tools = document.querySelector('.topbar-design-tools').getBoundingClientRect();
                const utilities = document.querySelector('.topbar-utility-actions').getBoundingClientRect();
                const overlaps = !(
                    tools.right <= utilities.left ||
                    utilities.right <= tools.left ||
                    tools.bottom <= utilities.top ||
                    utilities.bottom <= tools.top
                );
                return {
                    scrollWidth: document.documentElement.scrollWidth,
                    innerWidth: window.innerWidth,
                    toolsLeft: tools.left,
                    toolsRight: tools.right,
                    toolsTop: tools.top,
                    toolsBottom: tools.bottom,
                    topbarLeft: topbar.left,
                    topbarRight: topbar.right,
                    topbarTop: topbar.top,
                    topbarBottom: topbar.bottom,
                    overlaps,
                };
            }"""
        )
        assert header_geometry["scrollWidth"] <= header_geometry["innerWidth"] + 2
        assert header_geometry["toolsLeft"] >= header_geometry["topbarLeft"] - 1
        assert header_geometry["toolsRight"] <= header_geometry["topbarRight"] + 1
        assert header_geometry["toolsTop"] >= header_geometry["topbarTop"] - 1
        assert header_geometry["toolsBottom"] <= header_geometry["topbarBottom"] + 1
        assert header_geometry["overlaps"] is False

        page.locator("#designWorkspaceBtn").click()
        playwright_api.expect(page.locator("#designWorkspace")).to_be_visible()
        playwright_api.expect(page.locator("#designPanelResults")).to_be_visible()

        page.locator("#designTabResults").focus()
        page.keyboard.press("End")
        playwright_api.expect(page.locator("#designTabReports")).to_be_focused()
        playwright_api.expect(page.locator("#designPanelReports")).to_be_visible()
        page.keyboard.press("Home")
        playwright_api.expect(page.locator("#designTabResults")).to_be_focused()

        geometry = page.evaluate(
            """() => ({
                scrollWidth: document.documentElement.scrollWidth,
                innerWidth: window.innerWidth,
                workspaceRight: document.querySelector('#designWorkspace').getBoundingClientRect().right,
                workspaceLeft: document.querySelector('#designWorkspace').getBoundingClientRect().left,
                workspaceTop: document.querySelector('#designWorkspace').getBoundingClientRect().top,
                workspaceHeight: document.querySelector('#designWorkspace').getBoundingClientRect().height,
                mainHeight: document.querySelector('.main').getBoundingClientRect().height,
                chatDisplay: getComputedStyle(document.querySelector('#chatLog')).display,
                sidebarBottom: document.querySelector('.sidebar').getBoundingClientRect().bottom,
                sidebarRight: document.querySelector('.sidebar').getBoundingClientRect().right,
                projectDisplay: getComputedStyle(document.querySelector('.sidebar-project')).display,
                sessionGroupDisplay: getComputedStyle(document.querySelector('.sidebar-group')).display,
                compactActionsVisible: Array.from(document.querySelectorAll(
                    '#chatViewBtn, #settingsToggleBtn'
                )).every((element) => {
                    const rect = element.getBoundingClientRect();
                    return rect.width > 0 && rect.height >= 40;
                })
            })"""
        )
        assert geometry["scrollWidth"] <= geometry["innerWidth"] + 2
        assert geometry["workspaceLeft"] >= -2
        assert geometry["workspaceRight"] <= geometry["innerWidth"] + 2
        if viewport["width"] <= 980:
            assert geometry["workspaceTop"] <= 140
            assert geometry["workspaceHeight"] >= geometry["mainHeight"] - 2
            assert geometry["chatDisplay"] == "none"
            assert geometry["sidebarBottom"] <= 80
            assert geometry["sidebarRight"] <= geometry["innerWidth"] + 2
            assert geometry["projectDisplay"] == "none"
            assert geometry["sessionGroupDisplay"] == "none"
            assert geometry["compactActionsVisible"] is True
    finally:
        context.close()


def test_result_viewer_does_not_expose_standalone_preflight_or_submit_controls(
    e2e_browser,
    static_app_url: str,
) -> None:
    context = e2e_browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    api_state = _install_api_mock(page)
    try:
        page.goto(static_app_url)
        playwright_api.expect(page.locator("#designWorkspaceBtn")).to_be_hidden()
        assert page.locator(
            "#designRunForm, #designPreflightBtn, #designRunBtn, #designCancelBtn, #designRetryBtn"
        ).count() == 0
        assert api_state["preflight_calls"] == 0
    finally:
        context.close()


def _legacy_propulsion_energy_editor_contract(
    e2e_browser,
    static_app_url: str,
) -> None:
    context = e2e_browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    api_state = _install_api_mock(page)
    try:
        page.goto(static_app_url)
        page.locator("#designWorkspaceBtn").click()
        page.locator("#designUseAdvanced").check()

        playwright_api.expect(page.locator("#designSfcLabel")).to_have_text(
            "螺旋桨 BSFC（kg/J）"
        )
        playwright_api.expect(page.locator("#designSfc")).to_be_enabled()
        playwright_api.expect(page.locator("#designPropEfficiencyField")).to_be_visible()
        playwright_api.expect(page.locator("#designPropEfficiency")).to_have_value("0.8")
        assert float(page.locator("#designSfc").input_value()) == pytest.approx(8.45e-8)

        page.locator("#designPropulsionType").select_option("jet")
        playwright_api.expect(page.locator("#designSfcLabel")).to_have_text(
            "喷气 TSFC（kg/(N·s)）"
        )
        playwright_api.expect(page.locator("#designPropEfficiencyField")).to_be_hidden()
        playwright_api.expect(page.locator("#designPropEfficiency")).to_be_disabled()
        assert float(page.locator("#designSfc").input_value()) == pytest.approx(2.3e-5)

        page.locator("#designPropulsionType").select_option("prop")
        page.locator("#designSfc").fill("9.1e-8")
        page.locator("#designPropEfficiency").fill("0.83")
        page.locator("#designPropulsionType").select_option("jet")
        page.locator("#designSfc").fill("3.2e-5")
        page.locator("#designPropulsionType").select_option("prop")
        assert float(page.locator("#designSfc").input_value()) == pytest.approx(9.1e-8)
        assert float(page.locator("#designPropEfficiency").input_value()) == pytest.approx(0.83)

        calls_before_prop = api_state["preflight_calls"]
        page.locator("#designPreflightBtn").click()
        playwright_api.expect(page.locator("#designPreflightState")).to_have_text("服务端已校验")
        assert api_state["preflight_calls"] > calls_before_prop
        prop_request = api_state["preflight_requests"][-1]
        prop_initial = prop_request["initial_guess"]
        assert prop_request["requirements"]["propulsion_type"] == "prop"
        assert prop_initial["prop_bsfc_kg_per_j"] == pytest.approx(9.1e-8)
        assert prop_initial["prop_efficiency"] == pytest.approx(0.83)
        assert "jet_tsfc_kg_per_n_s" not in prop_initial
        assert "sfc_cruise_1_s" not in prop_initial
        prop_provenance = prop_request["provenance"]
        assert prop_provenance["propulsion_energy"]["canonical_field"] == "prop_bsfc_kg_per_j"
        assert prop_provenance["input_fields"]["initial_guess"]["prop_bsfc_kg_per_j"] == {
            "source": "user",
            "value": pytest.approx(9.1e-8),
        }

        page.locator("#designPropulsionType").select_option("jet")
        assert float(page.locator("#designSfc").input_value()) == pytest.approx(3.2e-5)
        calls_before_jet = api_state["preflight_calls"]
        page.locator("#designPreflightBtn").click()
        playwright_api.expect(page.locator("#designPreflightState")).to_have_text("服务端已校验")
        assert api_state["preflight_calls"] > calls_before_jet
        jet_request = api_state["preflight_requests"][-1]
        jet_initial = jet_request["initial_guess"]
        assert jet_request["requirements"]["propulsion_type"] == "jet"
        assert jet_initial["jet_tsfc_kg_per_n_s"] == pytest.approx(3.2e-5)
        assert "prop_bsfc_kg_per_j" not in jet_initial
        assert "prop_efficiency" not in jet_initial
        assert "sfc_cruise_1_s" not in jet_initial
        jet_provenance = jet_request["provenance"]
        assert jet_provenance["propulsion_energy"]["canonical_field"] == "jet_tsfc_kg_per_n_s"
        assert jet_provenance["input_fields"]["initial_guess"]["jet_tsfc_kg_per_n_s"] == {
            "source": "user",
            "value": pytest.approx(3.2e-5),
        }
    finally:
        context.close()


@pytest.mark.parametrize(
    ("propulsion_type", "canonical_field", "label"),
    [
        ("prop", "prop_bsfc_kg_per_j", "螺旋桨 BSFC（kg/J）"),
        ("jet", "jet_tsfc_kg_per_n_s", "喷气 TSFC（kg/(N·s)）"),
    ],
)
def _legacy_sfc_editor_migration_contract(
    e2e_browser,
    static_app_url: str,
    propulsion_type: str,
    canonical_field: str,
    label: str,
) -> None:
    legacy_sfc = 0.0002222222
    request = _request(f"Legacy {propulsion_type} UAV")
    request["requirements"]["propulsion_type"] = propulsion_type
    request["initial_guess"].pop("prop_bsfc_kg_per_j")
    request["initial_guess"].pop("prop_efficiency")
    request["initial_guess"]["sfc_cruise_1_s"] = legacy_sfc
    request["provenance"] = {
        "request_contract_version": 1,
        "input_fields": {
            "initial_guess": {
                "sfc_cruise_1_s": {"source": "user", "value": legacy_sfc},
            }
        },
        "ui": {"custom_initial_guess": True},
    }
    legacy_job = _job(
        f"job-legacy-{propulsion_type}",
        request["project_name"],
        status="completed",
        mtow_kg=2_350.0,
        engineering_feasible=True,
    )
    legacy_job["request"] = request

    temperature_k = 288.15 - 0.0065 * 6_000.0
    cruise_speed_m_s = 0.22 * math.sqrt(1.4 * 287.05287 * temperature_k)
    expected_value = (
        legacy_sfc / 9.80665
        if propulsion_type == "jet"
        else legacy_sfc * 0.8 / (9.80665 * cruise_speed_m_s)
    )

    context = e2e_browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    api_state = _install_api_mock(page, jobs=[legacy_job])
    try:
        page.goto(static_app_url)
        page.locator("#designWorkspaceBtn").click()
        playwright_api.expect(
            page.locator("#designActiveJobLabel")
        ).to_contain_text(f"job-legacy-{propulsion_type}")
        playwright_api.expect(page.locator("#designUseAdvanced")).to_be_checked()
        playwright_api.expect(page.locator("#designSfcLabel")).to_have_text(label)
        playwright_api.expect(page.locator("#designSfc")).to_be_enabled()
        assert float(page.locator("#designSfc").input_value()) == pytest.approx(expected_value)

        calls_before = api_state["preflight_calls"]
        page.locator("#designPreflightBtn").click()
        playwright_api.expect(page.locator("#designPreflightState")).to_have_text("服务端已校验")
        assert api_state["preflight_calls"] > calls_before
        migrated_request = api_state["preflight_requests"][-1]
        migrated_initial = migrated_request["initial_guess"]
        assert migrated_request["requirements"]["propulsion_type"] == propulsion_type
        assert migrated_initial[canonical_field] == pytest.approx(expected_value)
        assert "sfc_cruise_1_s" not in migrated_initial
        if propulsion_type == "prop":
            assert migrated_initial["prop_efficiency"] == pytest.approx(0.8)
            assert "jet_tsfc_kg_per_n_s" not in migrated_initial
        else:
            assert "prop_efficiency" not in migrated_initial
            assert "prop_bsfc_kg_per_j" not in migrated_initial

        provenance = migrated_request["provenance"]
        energy_provenance = provenance["propulsion_energy"]
        assert energy_provenance["canonical_field"] == canonical_field
        assert energy_provenance["source"] == "legacy_migrated_at_cruise_condition"
        assert energy_provenance["legacy_field"] == "sfc_cruise_1_s"
        assert provenance["input_fields"]["initial_guess"][canonical_field] == {
            "source": "user",
            "value": pytest.approx(expected_value),
        }
        assert "sfc_cruise_1_s" not in provenance["input_fields"]["initial_guess"]

        page.evaluate("request => applyDesignJobRequest(request)", migrated_request)
        page.locator("#designPreflightBtn").click()
        playwright_api.expect(page.locator("#designPreflightState")).to_have_text("服务端已校验")
        reloaded_request = api_state["preflight_requests"][-1]
        assert reloaded_request["provenance"]["propulsion_energy"]["source"] == (
            "legacy_migrated_at_cruise_condition"
        )

        page.locator("#designUseAdvanced").uncheck()
        page.locator("#designPreflightBtn").click()
        playwright_api.expect(page.locator("#designPreflightState")).to_have_text("服务端已校验")
        defaulted_request = api_state["preflight_requests"][-1]
        assert "initial_guess" not in defaulted_request
        assert defaulted_request["provenance"]["propulsion_energy"] == {
            "propulsion_type": propulsion_type,
            "canonical_field": canonical_field,
            "source": "default",
            "legacy_field": None,
            "legacy_semantics": None,
        }
    finally:
        context.close()


def test_history_recovery_infeasible_result_report_preview_and_comparison(
    e2e_browser,
    static_app_url: str,
) -> None:
    jobs = [
        _job(
            "job-infeasible",
            "Medium UAV",
            status="engineering_infeasible",
            mtow_kg=2_450.0,
            engineering_feasible=False,
        ),
        _job(
            "job-feasible",
            "Adjusted UAV",
            status="completed",
            mtow_kg=2_300.0,
            engineering_feasible=True,
        ),
    ]
    context = e2e_browser.new_context(viewport={"width": 1440, "height": 900})
    page = context.new_page()
    _install_api_mock(page, jobs=jobs)
    try:
        page.goto(static_app_url)
        page.locator("#designWorkspaceBtn").click()
        version_select = page.locator("#designResultVersionSelect")
        playwright_api.expect(version_select).to_have_value("job-infeasible")
        assert version_select.locator("option").count() == 2
        playwright_api.expect(page.locator("#designTabCompare")).to_be_visible()
        assert page.locator("#designRunForm, #designPanelRun").count() == 0

        playwright_api.expect(page.locator("#designResultsContent")).to_contain_text("工程不可行")
        playwright_api.expect(page.locator("#designResultsContent")).to_contain_text("数值已收敛")
        playwright_api.expect(page.locator("#designResultsContent")).to_contain_text("Climb thrust margin")
        playwright_api.expect(page.locator("[data-testid='design-visualization']")).to_be_visible()
        playwright_api.expect(page.locator(".design-model-viewport canvas")).to_be_visible()
        playwright_api.expect(page.locator(".design-gallery-primary")).to_have_attribute(
            "alt", "外形俯视图"
        )
        side_view_button = page.get_by_role("button", name="查看外形侧视图")
        assert side_view_button.count() == 1
        side_view_button.click()
        playwright_api.expect(page.locator(".design-gallery-primary")).to_have_attribute(
            "alt", "外形侧视图"
        )

        canvas = page.locator(".design-model-viewport canvas")
        first_frame = canvas.evaluate(
            """canvas => {
                const gl = canvas.getContext('webgl2') || canvas.getContext('webgl');
                const pixels = new Uint8Array(canvas.width * canvas.height * 4);
                gl.readPixels(0, 0, canvas.width, canvas.height, gl.RGBA, gl.UNSIGNED_BYTE, pixels);
                let min = 255;
                let max = 0;
                let checksum = 0;
                for (let index = 0; index < pixels.length; index += 97) {
                    min = Math.min(min, pixels[index]);
                    max = Math.max(max, pixels[index]);
                    checksum = (checksum + pixels[index] * (index + 1)) % 2147483647;
                }
                return {min, max, checksum};
            }"""
        )
        assert first_frame["max"] - first_frame["min"] > 20
        page.wait_for_timeout(400)
        second_checksum = canvas.evaluate(
            """canvas => {
                const gl = canvas.getContext('webgl2') || canvas.getContext('webgl');
                const pixels = new Uint8Array(canvas.width * canvas.height * 4);
                gl.readPixels(0, 0, canvas.width, canvas.height, gl.RGBA, gl.UNSIGNED_BYTE, pixels);
                let checksum = 0;
                for (let index = 0; index < pixels.length; index += 97) {
                    checksum = (checksum + pixels[index] * (index + 1)) % 2147483647;
                }
                return checksum;
            }"""
        )
        assert second_checksum != first_frame["checksum"]

        version_select.select_option("job-feasible")
        playwright_api.expect(page.locator("#designResultsContent")).to_contain_text("工程可行")
        version_select.select_option("job-infeasible")
        playwright_api.expect(page.locator("#designResultsContent")).to_contain_text("工程不可行")

        page.locator("#designTabReports").click()
        playwright_api.expect(page.locator("#designReportList")).to_contain_text("design_report_v2.md")
        playwright_api.expect(page.locator("#designReportPreview")).to_contain_text("Engineering diagnostic")

        page.locator("#designTabCompare").click()
        checkboxes = page.locator("#designCompareSelector input[type='checkbox']")
        checkboxes.nth(0).check()
        checkboxes.nth(1).check()
        playwright_api.expect(page.locator("#designCompareContent")).to_contain_text("参数差值")
        playwright_api.expect(page.locator("#designCompareContent")).to_contain_text("约束裕度对比")
        playwright_api.expect(page.locator("#designCompareContent")).to_contain_text("Δ")
    finally:
        context.close()


def test_running_task_is_not_exposed_as_a_conversation_result(e2e_browser, static_app_url: str) -> None:
    running = _job(
        "job-running",
        "Recovered running UAV",
        status="running",
        mtow_kg=2_450.0,
        engineering_feasible=False,
        terminal=False,
    )
    context = e2e_browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    api_state = _install_api_mock(page, jobs=[running], running_fallback=True)
    try:
        page.goto(static_app_url)
        playwright_api.expect(page.locator("#designWorkspaceBtn")).to_be_hidden()
        playwright_api.expect(page.locator("#designWorkspace")).to_be_hidden()
        assert api_state["stream_failures"] == 0
        assert api_state["detail_reads"] == 0
    finally:
        context.close()
