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


@pytest.fixture(scope="module")
def e2e_browser():
    # Keep Playwright's sync event loop inside this module.  The plugin's
    # session-scoped fixture otherwise remains active while later tests call
    # asyncio.run(), which Python correctly rejects as a nested event loop.
    with playwright_api.sync_playwright() as playwright:
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


def _session_payload(
    design_results: list[dict] | None = None,
    messages: list[dict] | None = None,
) -> dict:
    return {
        "session_id": "e2e-session",
        "provider": "openai",
        "model": "deepseek-v4-pro",
        "auto_skill": None,
        "auto_approve": True,
        "messages": messages or [],
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


def _requirement_interaction(*, action_enabled: bool = True) -> dict:
    return {
        "contract_version": 1,
        "type": "aircraft_requirement_review",
        "session_id": "e2e-session",
        "revision": {
            "revision_id": "requirement-revision-001",
            "revision_number": 1,
            "revision_hash": "a" * 64,
            "status": "unsupported",
            "confirmed": False,
        },
        "intent": {
            "requirements": [
                {
                    "path": "mission.max_flight_mach",
                    "value": 0.8,
                    "unit": "Mach",
                    "role": "hard_constraint",
                    "locked": True,
                    "source": "user",
                    "applicable_model": None,
                },
                {
                    "path": "launch.mode",
                    "value": "rocket_assist",
                    "unit": None,
                    "role": "hard_constraint",
                    "locked": True,
                    "source": "user",
                    "applicable_model": None,
                },
            ]
        },
        "diagnosis": {
            "status": "unsupported",
            "summary": "火箭助推和最大飞行马赫数尚未进入当前专项模型。",
            "coverage": [
                {
                    "field_path": "mission.max_flight_mach",
                    "status": "unsupported",
                    "model_id": None,
                    "reason": "当前只校核巡航设计点。",
                    "blocking": True,
                },
                {
                    "field_path": "launch.mode",
                    "status": "unsupported",
                    "model_id": None,
                    "reason": "火箭助推轨迹模型尚未接入。",
                    "blocking": True,
                },
            ],
            "clarification_questions": [
                {
                    "question_id": "question-scope-001",
                    "field_path": "launch.mode",
                    "question": "是否先对巡航段开展概念设计？",
                    "reason": "助推段目前不能完成专项验证。",
                    "options": ["先设计巡航段", "等待专项模型"],
                    "recommended_option": "先设计巡航段",
                    "consequence_if_unanswered": "整体方案保持模型未覆盖状态。",
                    "blocking": True,
                },
                {
                    "question_id": "question-mtow-001",
                    "field_path": "mass.maximum_takeoff_mass",
                    "question": "请确认最大起飞重量上限。",
                    "reason": "该数值用于锁定重量闭合边界。",
                    "options": [],
                    "recommended_option": 260,
                    "consequence_if_unanswered": "无法建立重量上限约束。",
                    "blocking": True,
                },
                {
                    "question_id": "question-range-001",
                    "field_path": "mission.range_m",
                    "question": "请确认任务航程。",
                    "reason": "任务航程用于燃油与重量闭合。",
                    "options": [],
                    "recommended_option": None,
                    "consequence_if_unanswered": "无法建立任务闭合边界。",
                    "blocking": True,
                }
            ],
            "change_proposals": [
                {
                    "proposal_id": "scope.cruise_only",
                    "field_path": "launch.mode",
                    "old_value": "rocket_assist",
                    "proposed_value": "out_of_scope",
                    "reason": "先冻结助推接口，仅求解巡航段。",
                    "affected_constraints": ["launch.mode"],
                    "expected_benefit": "可继续评估巡航重量与气动闭合。",
                    "engineering_cost": "不能宣称全任务剖面可行。",
                    "target_locked": True,
                    "requires_user_confirmation": True,
                    "source_revision": 1,
                }
            ],
            "blocking_reasons": ["火箭助推轨迹模型未覆盖。"],
            "conflicting_fields": [],
            "assumptions": [],
            "ready_for_solver": False,
        },
        "actions": [
            {
                "action": "answer_question",
                "label": "提交确认信息",
                "enabled": action_enabled,
                "primary": True,
                "payload": {},
            }
        ],
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
            "range_metric_kind": "evaluated_mission_distance",
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
    messages: list[dict] | None = None,
    requirement_action_response: dict | None = None,
    requirement_action_responses: list[dict] | None = None,
    requirement_action_error: str | None = None,
    stream_completion_job: dict | None = None,
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
        "requirement_action_requests": [],
        "stream_completed": False,
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
            session = _session_payload(jobs, messages)
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
                if session_id == "e2e-session" and state["stream_completed"]:
                    fulfill_json(route, {"session": _session_payload(jobs, messages)})
                    return
                else:
                    fulfill_json(route, {"error": "unknown session"}, status=404)
                    return
            session = _session_payload(summary.get("design_results", []))
            session["session_id"] = session_id
            session["auto_skill"] = summary.get("auto_skill")
            fulfill_json(route, {"session": session})
            return
        if (
            path.startswith("/api/sessions/")
            and "/requirement-revisions/" in path
            and path.endswith("/actions")
            and method == "POST"
        ):
            state["requirement_action_requests"].append(
                {
                    "path": path,
                    "payload": route.request.post_data_json or {},
                }
            )
            if requirement_action_error:
                fulfill_json(route, {"error": requirement_action_error}, status=400)
                return
            response_index = len(state["requirement_action_requests"]) - 1
            sequenced_response = (
                requirement_action_responses[
                    min(response_index, len(requirement_action_responses) - 1)
                ]
                if requirement_action_responses
                else None
            )
            fulfill_json(
                route,
                sequenced_response
                or requirement_action_response
                or {"interaction": _requirement_interaction(action_enabled=False)},
            )
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
            if stream_completion_job is not None:
                state["stream_completed"] = True
                detail_by_id[stream_completion_job["job_id"]] = stream_completion_job
                jobs[:] = [
                    stream_completion_job,
                    *[
                        job
                        for job in jobs
                        if job["job_id"] != stream_completion_job["job_id"]
                    ],
                ]
                route.fulfill(
                    status=200,
                    content_type="text/event-stream; charset=utf-8",
                    body=(
                        "event: done\n"
                        + "data: "
                        + json.dumps({"job": stream_completion_job}, ensure_ascii=False)
                        + "\n\n"
                    ),
                )
                return
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


def test_requirement_interaction_card_renders_and_posts_revision_action(
    e2e_browser,
    static_app_url: str,
) -> None:
    interaction = _requirement_interaction()
    interaction["revision"]["revision_number"] = 2
    historical_interaction = json.loads(json.dumps(interaction))
    historical_interaction["revision"]["revision_id"] = "requirement-revision-000"
    historical_interaction["revision"]["revision_number"] = 1
    historical_interaction["revision"]["revision_hash"] = "b" * 64
    updated_interaction = json.loads(json.dumps(interaction))
    updated_interaction["revision"]["revision_id"] = "requirement-revision-002"
    updated_interaction["revision"]["revision_number"] = 3
    updated_interaction["revision"]["revision_hash"] = "c" * 64
    updated_interaction["diagnosis"]["summary"] = "已记录巡航段优先的用户决定。"
    updated_interaction["actions"][0]["enabled"] = False
    messages = [
        {
            "role": "assistant",
            "text": "上一版需求诊断。",
            "events": [
                {
                    "kind": "requirement_interaction",
                    "preview": {"interaction": historical_interaction},
                }
            ],
        },
        {
            "role": "assistant",
            "text": "请先确认需求诊断，再进入总体参数求解。",
            "events": [
                {
                    "kind": "requirement_interaction",
                    "preview": {"interaction": interaction},
                }
            ],
        }
    ]
    updated_messages = [
        *messages,
        {
            "role": "assistant",
            "text": "需求版本已更新。",
            "events": [
                {
                    "kind": "requirement_interaction",
                    "preview": {"interaction": updated_interaction},
                }
            ],
        },
    ]
    running_job = _job(
        "job-from-requirement-action",
        "Negotiated UAV",
        status="running",
        mtow_kg=260.0,
        engineering_feasible=False,
        terminal=False,
    )
    running_job["result"] = None
    running_job["result_files"] = []
    completed_job = _job(
        "job-from-requirement-action",
        "Negotiated UAV",
        status="completed",
        mtow_kg=255.0,
        engineering_feasible=True,
    )
    context = e2e_browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    mock_state = _install_api_mock(
        page,
        messages=messages,
        requirement_action_response={
            "interaction": updated_interaction,
            "session": _session_payload(messages=updated_messages),
            "job": running_job,
        },
        stream_completion_job=completed_job,
    )
    try:
        page.goto(static_app_url)
        cards = page.locator("[data-testid='requirement-interaction']")
        playwright_api.expect(cards).to_have_count(2)
        historical_card = cards.nth(0)
        playwright_api.expect(historical_card).to_have_attribute("data-current", "false")
        playwright_api.expect(historical_card).to_contain_text("历史需求版本")
        playwright_api.expect(
            historical_card.get_by_role("button", name="提交确认信息")
        ).to_be_disabled()
        card = cards.nth(1)
        playwright_api.expect(card).to_be_visible()
        playwright_api.expect(card.locator(".requirement-status")).to_have_attribute(
            "data-status", "unsupported"
        )
        playwright_api.expect(card.locator(".requirement-status")).to_contain_text("模型未覆盖")
        playwright_api.expect(card).to_contain_text("火箭助推轨迹模型未覆盖")
        playwright_api.expect(card.locator("tr[data-field-path='launch.mode']")).to_contain_text(
            "已锁定"
        )
        assert card.locator(".requirement-lock.is-locked").count() == 2
        assert card.locator(".requirement-question").count() == 3
        numeric_answer = card.locator(
            "input[data-requirement-question='question-mtow-001']"
        )
        playwright_api.expect(numeric_answer).to_have_attribute("type", "number")
        playwright_api.expect(numeric_answer).to_have_value("260")
        range_answer = card.locator(
            "input[data-requirement-question='question-range-001']"
        )
        playwright_api.expect(range_answer).to_have_attribute("type", "number")
        playwright_api.expect(range_answer).to_have_attribute("placeholder", "请输入数值（米）")
        range_answer.fill("500000")
        playwright_api.expect(card).to_contain_text("先冻结助推接口")
        playwright_api.expect(card).to_contain_text("移出本轮求解范围")
        assert "out_of_scope" not in card.inner_text()

        action_button = card.get_by_role("button", name="提交确认信息")
        with page.expect_response(
            re.compile(
                r"/api/sessions/e2e-session/requirement-revisions/"
                r"requirement-revision-001/actions$"
            )
        ) as response_info:
            action_button.click()
        assert response_info.value.status == 200

        assert len(mock_state["requirement_action_requests"]) == 1
        request = mock_state["requirement_action_requests"][0]
        assert request["path"].endswith("/requirement-revision-001/actions")
        payload = request["payload"]
        assert payload["action"] == "answer_question"
        assert payload["expected_revision_hash"] == "a" * 64
        assert payload["client_action_id"]
        assert "proposal_id" not in payload
        assert payload["decisions"]["clarification_answers"] == [
            {
                "question_id": "question-scope-001",
                "field_path": "launch.mode",
                "value": "先设计巡航段",
            },
            {
                "question_id": "question-mtow-001",
                "field_path": "mass.maximum_takeoff_mass",
                "value": 260,
            },
            {
                "question_id": "question-range-001",
                "field_path": "mission.range_m",
                "value": 500000,
            },
        ]
        assert cards.count() == 3
        playwright_api.expect(cards.nth(1)).to_have_attribute("data-current", "false")
        current_card = cards.last
        playwright_api.expect(current_card).to_contain_text("已记录巡航段优先的用户决定")
        playwright_api.expect(
            current_card.get_by_role("button", name="提交确认信息")
        ).to_be_disabled()

        page.set_viewport_size({"width": 390, "height": 844})
        geometry = current_card.evaluate(
            """card => {
                const bounds = card.getBoundingClientRect();
                const table = card.querySelector('.requirement-table-wrap');
                return {
                    left: bounds.left,
                    right: bounds.right,
                    viewportWidth: window.innerWidth,
                    documentWidth: document.documentElement.scrollWidth,
                    tableClientWidth: table.clientWidth,
                    tableScrollWidth: table.scrollWidth,
                };
            }"""
        )
        assert geometry["left"] >= -1
        assert geometry["right"] <= geometry["viewportWidth"] + 1
        assert geometry["documentWidth"] <= geometry["viewportWidth"] + 1
        assert geometry["tableScrollWidth"] >= geometry["tableClientWidth"]

        playwright_api.expect(page.locator("#designWorkspaceBtn")).to_be_visible()
        page.wait_for_function(
            "() => document.querySelector('#designActiveJobLabel')?.textContent.includes('初步可行候选')"
        )
        page.set_viewport_size({"width": 1280, "height": 900})
        page.locator("#designWorkspaceBtn").click()
        playwright_api.expect(page.locator("#designResultsContent")).to_contain_text("初步可行候选")
    finally:
        context.close()


def test_requirement_units_follow_field_semantics(
    e2e_browser,
    static_app_url: str,
) -> None:
    interaction = _requirement_interaction(action_enabled=False)
    interaction["intent"]["requirements"] = [
        {
            "path": path,
            "value": value,
            "unit": unit,
            "role": "technology_assumption",
            "locked": False,
            "source": "default",
            "applicable_model": "aircraft_class_i_ii_v2",
        }
        for path, value, unit in [
            ("requirements.assumed_climb_rate_m_s", 5.0, "s"),
            ("initial_guess.sfc_cruise_1_s", 2.3e-5, "s"),
            ("initial_guess.jet_tsfc_kg_per_n_s", 2.3e-5, "s"),
            ("initial_guess.prop_bsfc_kg_per_j", 8.45e-8, None),
            ("initial_guess.sweep_deg", 35.0, None),
            ("requirements.max_load_factor", 3.8, None),
        ]
    ]
    interaction["diagnosis"]["clarification_questions"] = []
    messages = [
        {
            "role": "assistant",
            "text": "",
            "events": [
                {
                    "kind": "requirement_interaction",
                    "preview": {"interaction": interaction},
                }
            ],
        }
    ]

    context = e2e_browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    _install_api_mock(page, messages=messages)
    try:
        page.goto(static_app_url)
        card = page.locator("[data-testid='requirement-interaction']")
        climb_rate = card.locator(
            "tr[data-field-path='requirements.assumed_climb_rate_m_s']"
        )
        playwright_api.expect(climb_rate.locator("td").nth(2)).to_have_text("m/s")
        playwright_api.expect(
            card.locator("tr[data-field-path='initial_guess.sfc_cruise_1_s'] td").nth(2)
        ).to_have_text("1/s")
        playwright_api.expect(
            card.locator("tr[data-field-path='initial_guess.jet_tsfc_kg_per_n_s'] td").nth(2)
        ).to_have_text("kg/(N·s)")
        playwright_api.expect(
            card.locator("tr[data-field-path='initial_guess.prop_bsfc_kg_per_j'] td").nth(2)
        ).to_have_text("kg/J")
        playwright_api.expect(
            card.locator("tr[data-field-path='initial_guess.sweep_deg'] td").nth(2)
        ).to_have_text("度")
        playwright_api.expect(
            card.locator("tr[data-field-path='requirements.max_load_factor'] td").nth(2)
        ).to_have_text("g")
    finally:
        context.close()


def test_only_latest_card_is_current_when_confirmation_reuses_revision_id(
    e2e_browser,
    static_app_url: str,
) -> None:
    awaiting_confirmation = _requirement_interaction()
    awaiting_confirmation["revision"].update(
        {"status": "ready_for_solver", "confirmed": False}
    )
    awaiting_confirmation["diagnosis"].update(
        {
            "status": "ready_for_solver",
            "clarification_questions": [],
            "blocking_reasons": [],
            "ready_for_solver": True,
        }
    )
    awaiting_confirmation["actions"] = [
        {
            "action": "confirm_revision",
            "label": "确认需求版本",
            "enabled": True,
            "primary": True,
            "payload": {"user_confirmed": True},
        }
    ]
    confirmed = json.loads(json.dumps(awaiting_confirmation))
    confirmed["revision"]["confirmed"] = True
    confirmed["actions"] = [
        {
            "action": "submit_solver",
            "label": "开始总体设计求解",
            "enabled": True,
            "primary": True,
            "payload": {"timeout_seconds": 180.0},
        }
    ]
    messages = [
        {
            "role": "assistant",
            "text": "",
            "events": [
                {
                    "kind": "requirement_interaction",
                    "preview": {"interaction": interaction},
                }
            ],
        }
        for interaction in (awaiting_confirmation, confirmed)
    ]

    context = e2e_browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    _install_api_mock(page, messages=messages)
    try:
        page.goto(static_app_url)
        cards = page.locator("[data-testid='requirement-interaction']")
        playwright_api.expect(cards).to_have_count(2)
        playwright_api.expect(cards.nth(0)).to_have_attribute("data-current", "false")
        playwright_api.expect(
            cards.nth(0).get_by_role("button", name="确认需求版本")
        ).to_be_disabled()
        playwright_api.expect(cards.nth(1)).to_have_attribute("data-current", "true")
        playwright_api.expect(
            cards.nth(1).get_by_role("button", name="开始总体设计求解")
        ).to_be_enabled()
        assert page.locator(
            "[data-testid='requirement-interaction'][data-current='true']"
        ).count() == 1
    finally:
        context.close()


def test_change_proposal_action_posts_only_proposal_id(
    e2e_browser,
    static_app_url: str,
) -> None:
    interaction = _requirement_interaction()
    interaction["diagnosis"]["clarification_questions"] = []
    interaction["actions"] = [
        {
            "action": "apply_change",
            "label": "应用参数修改",
            "enabled": True,
            "primary": True,
            "payload": {"user_confirmed": True},
        }
    ]
    updated = json.loads(json.dumps(interaction))
    updated["revision"].update(
        {
            "revision_id": "requirement-revision-002",
            "revision_number": 2,
            "revision_hash": "b" * 64,
        }
    )
    updated["diagnosis"]["change_proposals"] = []
    updated["diagnosis"]["summary"] = "已应用确认的参数修改。"
    updated["actions"] = []
    messages = [
        {
            "role": "assistant",
            "text": "",
            "events": [
                {
                    "kind": "requirement_interaction",
                    "preview": {"interaction": interaction},
                }
            ],
        }
    ]

    context = e2e_browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    mock_state = _install_api_mock(
        page,
        messages=messages,
        requirement_action_response={"interaction": updated},
    )
    try:
        page.goto(static_app_url)
        card = page.locator("[data-testid='requirement-interaction']")
        card.get_by_role("button", name="应用参数修改").click()
        payload = mock_state["requirement_action_requests"][0]["payload"]
        assert payload["action"] == "apply_change"
        assert payload["proposal_id"] == "scope.cruise_only"
        assert "decisions" not in payload
    finally:
        context.close()


def test_unsupported_request_uses_strict_answer_defer_confirm_sequence(
    e2e_browser,
    static_app_url: str,
) -> None:
    unsupported_paths = [
        "performance.min_cruise_endurance_s",
        "performance.max_flight_mach",
        "launch.mode",
        "recovery.mode",
        "configuration.stealth_requirement",
    ]
    initial = _requirement_interaction()
    initial["revision"] = {
        "revision_id": "complex-revision-001",
        "revision_number": 1,
        "revision_hash": "1" * 64,
        "status": "unsupported",
        "confirmed": False,
    }
    initial["intent"]["requirements"] = [
        {
            "path": "weights.max_mtow_kg",
            "value": 260,
            "unit": "kg",
            "role": "hard_constraint",
            "locked": True,
            "source": "user",
            "applicable_model": "class1.weights",
        },
        {
            "path": "requirements.payload_kg",
            "value": 60,
            "unit": "kg",
            "role": "hard_constraint",
            "locked": True,
            "source": "user",
            "applicable_model": "class1.weights",
        },
        *[
            {
                "path": path,
                "value": {
                    "performance.min_cruise_endurance_s": 3600,
                    "performance.max_flight_mach": 0.8,
                    "launch.mode": "rocket_assist",
                    "recovery.mode": "parachute",
                    "configuration.stealth_requirement": True,
                }[path],
                "unit": None,
                "role": "hard_constraint",
                "locked": True,
                "source": "user",
                "applicable_model": None,
            }
            for path in unsupported_paths
        ],
    ]
    initial["diagnosis"].update(
        {
            "status": "unsupported",
            "summary": "专项任务要求未被当前模型覆盖，且有两个求解输入需要确认。",
            "coverage": [
                {
                    "field_path": path,
                    "status": "unsupported",
                    "model_id": None,
                    "reason": "当前 Class I/II 模型未覆盖该专项要求。",
                    "blocking": True,
                }
                for path in unsupported_paths
            ],
            "clarification_questions": [
                {
                    "question_id": "mission.range.required",
                    "field_path": "mission.range_m",
                    "question": "What design mission range should the sizing solver close?",
                    "reason": "The current solver requires a positive mission range.",
                    "options": [],
                    "recommended_option": None,
                    "consequence_if_unanswered": "The sizing run cannot start.",
                    "blocking": True,
                },
                {
                    "question_id": "propulsion.type.high_speed",
                    "field_path": "propulsion.propulsion_type",
                    "question": "Which propulsion branch should be used?",
                    "reason": "Propulsion type changes the sizing assumptions.",
                    "options": ["jet", "prop"],
                    "recommended_option": "jet",
                    "consequence_if_unanswered": "No propulsion default is applied silently.",
                    "blocking": True,
                },
            ],
            "change_proposals": [],
            "blocking_reasons": ["专项要求未覆盖。"],
            "ready_for_solver": False,
        }
    )
    initial["actions"] = [
        {
            "action": "answer_question",
            "label": "提交确认信息",
            "enabled": True,
            "primary": True,
            "payload": {},
        }
    ]

    answered = json.loads(json.dumps(initial))
    answered["revision"].update(
        {
            "revision_id": "complex-revision-002",
            "revision_number": 2,
            "revision_hash": "2" * 64,
        }
    )
    answered["intent"]["requirements"].extend(
        [
            {
                "path": "requirements.range_m",
                "value": 950000,
                "unit": "m",
                "role": "hard_constraint",
                "locked": True,
                "source": "user",
                "applicable_model": "class1.mission",
            },
            {
                "path": "requirements.propulsion_type",
                "value": "jet",
                "unit": None,
                "role": "hard_constraint",
                "locked": True,
                "source": "user",
                "applicable_model": "class2.propulsion",
            },
        ]
    )
    answered["diagnosis"]["clarification_questions"] = []
    answered["diagnosis"]["summary"] = "确认信息已记录，下一步处理专项模型缺口。"
    answered["actions"] = [
        {
            "action": "defer_unsupported",
            "label": "保留专项需求，先求解已覆盖范围",
            "enabled": True,
            "primary": True,
            "payload": {
                "field_paths": unsupported_paths,
                "scope_statement": "保留专项要求，本轮只求解已覆盖范围。",
                "user_confirmed": True,
            },
        }
    ]

    scoped = json.loads(json.dumps(answered))
    scoped["revision"].update(
        {
            "revision_id": "complex-revision-003",
            "revision_number": 3,
            "revision_hash": "3" * 64,
            "status": "ready_for_solver",
        }
    )
    scoped["diagnosis"].update(
        {
            "status": "ready_for_solver",
            "summary": "专项要求已保留为验证缺口，当前求解范围可以确认。",
            "coverage": [],
            "blocking_reasons": [],
            "ready_for_solver": True,
        }
    )
    for requirement in scoped["intent"]["requirements"]:
        if requirement["path"] in unsupported_paths:
            requirement["role"] = "soft_goal"
            requirement["locked"] = False
    scoped["actions"] = [
        {
            "action": "confirm_revision",
            "label": "确认需求版本",
            "enabled": True,
            "primary": True,
            "payload": {"user_confirmed": True},
        }
    ]

    confirmed = json.loads(json.dumps(scoped))
    confirmed["revision"]["confirmed"] = True
    confirmed["actions"] = [
        {
            "action": "submit_solver",
            "label": "开始总体设计求解",
            "enabled": True,
            "primary": True,
            "payload": {"timeout_seconds": 180.0},
        }
    ]
    messages = [
        {
            "role": "assistant",
            "text": "",
            "events": [
                {
                    "kind": "requirement_interaction",
                    "preview": {"interaction": initial},
                }
            ],
        }
    ]

    context = e2e_browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    mock_state = _install_api_mock(
        page,
        messages=messages,
        requirement_action_responses=[
            {"interaction": answered},
            {"interaction": scoped},
            {"interaction": confirmed},
        ],
    )
    try:
        page.goto(static_app_url)
        card = page.locator("[data-testid='requirement-interaction']")
        playwright_api.expect(card).to_have_count(1)
        playwright_api.expect(
            card.get_by_role("button", name="提交确认信息")
        ).to_be_visible()
        assert card.get_by_role(
            "button", name="保留专项需求，先求解已覆盖范围"
        ).count() == 0
        playwright_api.expect(card).to_contain_text("请确认总体设计需要闭合的任务航程")
        playwright_api.expect(card).to_contain_text("请确认高速巡航需求采用哪种推进类型")
        playwright_api.expect(card).to_contain_text("最大起飞重量上限")
        playwright_api.expect(card).to_contain_text("任务航程 · 单位：米")
        initial_text = card.inner_text()
        assert "What design mission range" not in initial_text
        assert "Which propulsion branch" not in initial_text
        assert "mission.range_m" not in initial_text
        assert "propulsion.propulsion_type" not in initial_text

        card.locator("input[data-requirement-question='mission.range.required']").fill(
            "950000"
        )
        playwright_api.expect(
            card.get_by_role("radio", name="喷气推进（推荐）")
        ).to_be_checked()
        card.get_by_role("button", name="提交确认信息").click()
        playwright_api.expect(card).to_contain_text("确认信息已记录")

        first_payload = mock_state["requirement_action_requests"][0]["payload"]
        assert first_payload["action"] == "answer_question"
        assert first_payload["decisions"]["clarification_answers"] == [
            {
                "question_id": "mission.range.required",
                "field_path": "mission.range_m",
                "value": 950000,
            },
            {
                "question_id": "propulsion.type.high_speed",
                "field_path": "propulsion.propulsion_type",
                "value": "jet",
            },
        ]
        assert card.get_by_role("button", name="提交确认信息").count() == 0
        defer_button = card.get_by_role(
            "button", name="保留专项需求，先求解已覆盖范围"
        )
        playwright_api.expect(defer_button).to_be_visible()
        playwright_api.expect(
            card.locator("tr[data-field-path='requirements.range_m']")
        ).to_contain_text("950000")
        playwright_api.expect(
            card.locator("tr[data-field-path='requirements.propulsion_type']")
        ).to_contain_text("喷气推进")

        defer_button.click()
        playwright_api.expect(card).to_contain_text("当前求解范围可以确认")
        second_payload = mock_state["requirement_action_requests"][1]["payload"]
        assert second_payload["action"] == "defer_unsupported"
        assert "decisions" not in second_payload

        confirm_button = card.get_by_role("button", name="确认需求版本")
        playwright_api.expect(confirm_button).to_be_visible()
        confirm_button.click()
        third_payload = mock_state["requirement_action_requests"][2]["payload"]
        assert third_payload["action"] == "confirm_revision"
        assert "decisions" not in third_payload
        playwright_api.expect(
            card.get_by_role("button", name="开始总体设计求解")
        ).to_be_visible()
        playwright_api.expect(card.locator(".requirement-action-error")).to_be_hidden()
    finally:
        context.close()


def test_requirement_action_backend_error_is_shown_in_chinese(
    e2e_browser,
    static_app_url: str,
) -> None:
    interaction = _requirement_interaction()
    messages = [
        {
            "role": "assistant",
            "text": "",
            "events": [
                {
                    "kind": "requirement_interaction",
                    "preview": {"interaction": interaction},
                }
            ],
        }
    ]
    raw_error = (
        "decisions are not accepted by defer_unsupported; submit clarification "
        "answers with answer_question first"
    )
    context = e2e_browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    _install_api_mock(
        page,
        messages=messages,
        requirement_action_error=raw_error,
    )
    try:
        page.goto(static_app_url)
        card = page.locator("[data-testid='requirement-interaction']")
        card.locator("input[data-requirement-question='question-range-001']").fill(
            "500000"
        )
        card.get_by_role("button", name="提交确认信息").click()
        error = card.locator(".requirement-action-error")
        playwright_api.expect(error).to_be_visible()
        playwright_api.expect(error).to_contain_text("请先完整填写当前需求卡片中的确认信息")
        assert "defer_unsupported" not in error.inner_text()
        assert "answer_question" not in error.inner_text()
        assert "decisions are not accepted" not in error.inner_text()
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
        playwright_api.expect(page.locator("#designResultsContent")).to_contain_text("初步可行候选")
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


def test_design_outcome_requires_all_engineering_gates(
    e2e_browser,
    static_app_url: str,
) -> None:
    blocked = _job(
        "job-inconsistent-blocking-count",
        "inconsistent_engineering_result",
        status="completed",
        mtow_kg=2_300.0,
        engineering_feasible=True,
    )
    blocked["result"]["engineering"]["blocking_failed_count"] = 1
    incomplete = _job(
        "job-missing-blocking-count",
        "incomplete_engineering_result",
        status="completed",
        mtow_kg=2_250.0,
        engineering_feasible=True,
    )
    del incomplete["result"]["engineering"]["blocking_failed_count"]

    context = e2e_browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    _install_api_mock(page, jobs=[blocked, incomplete])
    try:
        page.goto(static_app_url)
        playwright_api.expect(page.locator("#designWorkspaceBtn")).to_be_visible()
        page.locator("#designWorkspaceBtn").click()

        outcome = page.locator("[data-testid='design-outcome']")
        playwright_api.expect(outcome.locator(".design-outcome-copy strong")).to_have_text(
            "工程不可行"
        )
        playwright_api.expect(outcome).to_contain_text("阻断项 1 项未通过")
        playwright_api.expect(outcome).not_to_contain_text("初步可行候选")

        page.locator("#designResultVersionSelect").select_option(
            "job-missing-blocking-count"
        )
        playwright_api.expect(outcome.locator(".design-outcome-copy strong")).to_have_text(
            "计算完成，待工程判定"
        )
        playwright_api.expect(outcome).to_contain_text("阻断项数量未知")
        playwright_api.expect(outcome).not_to_contain_text("初步可行候选")
    finally:
        context.close()


def test_deferred_requirements_remain_visible_as_validation_gaps(
    e2e_browser,
    static_app_url: str,
) -> None:
    result = _job(
        "job-limited-scope-feasible",
        "limited_scope_design",
        status="completed",
        mtow_kg=255.0,
        engineering_feasible=True,
    )
    result["request"]["provenance"] = {
        "requirement_intent": {
            "requirements": [
                {
                    "path": "deferred.requirements.cruise_altitude_m",
                    "value": 40_000.0,
                    "role": "soft_goal",
                    "locked": False,
                }
            ],
            "metadata": {
                "requirement_workflow": {
                    "scope_deferrals": [
                        {
                            "revision": 2,
                            "scope_statement": "本轮仅求解已覆盖范围",
                            "fields": [
                                {
                                    "field_path": "launch.mode",
                                    "retained_field_path": "launch.mode",
                                    "value": "rocket_assist",
                                    "coverage_reason": "火箭助推轨迹模型未接入",
                                    "scope_statement": "本轮仅求解已覆盖范围",
                                }
                            ],
                        }
                    ]
                }
            },
        },
        "soft_goals": {
            "deferred.requirements.cruise_altitude_m": 40_000.0,
            "launch_mode": "rocket_assist",
            "max_flight_mach": 0.8,
            "recovery.mode": "parachute",
            "configuration_reference": "沙赫德-136无人机",
            "stealth_requirement": True,
        },
    }

    context = e2e_browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    _install_api_mock(page, jobs=[result])
    try:
        page.goto(static_app_url)
        playwright_api.expect(page.locator("#designWorkspaceBtn")).to_be_visible()
        page.locator("#designWorkspaceBtn").click()

        results = page.locator("#designResultsContent")
        playwright_api.expect(results).to_contain_text("覆盖范围内初步通过")
        playwright_api.expect(results).to_contain_text("当前模型覆盖范围内的初步候选")
        playwright_api.expect(results).not_to_contain_text("总体设计方案工程可行")

        gaps = page.locator("[data-testid='design-validation-gaps']")
        playwright_api.expect(gaps).to_be_visible()
        assert gaps.locator("tbody tr").count() == 6
        playwright_api.expect(gaps).to_contain_text("巡航高度")
        playwright_api.expect(gaps).to_contain_text("40,000 米")
        playwright_api.expect(gaps).to_contain_text("发射方式")
        assert gaps.locator("tbody tr").filter(has_text="发射方式").count() == 1
        playwright_api.expect(gaps).to_contain_text("火箭助推")
        playwright_api.expect(gaps).to_contain_text("火箭助推轨迹模型未接入")
        playwright_api.expect(gaps).to_contain_text("本轮仅求解已覆盖范围")
        playwright_api.expect(gaps).to_contain_text("最大飞行马赫数")
        playwright_api.expect(gaps).to_contain_text("回收方式")
        playwright_api.expect(gaps).to_contain_text("参考构型")
        playwright_api.expect(gaps).to_contain_text("沙赫德-136无人机")
        stealth_row = gaps.locator("tbody tr").filter(has_text="隐身要求")
        playwright_api.expect(stealth_row).to_contain_text("是")
        gap_text = gaps.inner_text()
        assert "launch.mode" not in gap_text
        assert "max_flight_mach" not in gap_text
        assert "recovery.mode" not in gap_text
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
        playwright_api.expect(page.locator("#designResultsContent")).to_contain_text("初步可行候选")
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
            "螺旋桨功率比油耗（BSFC，kg/J）"
        )
        playwright_api.expect(page.locator("#designSfc")).to_be_enabled()
        playwright_api.expect(page.locator("#designPropEfficiencyField")).to_be_visible()
        playwright_api.expect(page.locator("#designPropEfficiency")).to_have_value("0.8")
        assert float(page.locator("#designSfc").input_value()) == pytest.approx(8.45e-8)

        page.locator("#designPropulsionType").select_option("jet")
        playwright_api.expect(page.locator("#designSfcLabel")).to_have_text(
            "喷气发动机推力比油耗（TSFC，kg/(N·s)）"
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
        ("prop", "prop_bsfc_kg_per_j", "螺旋桨功率比油耗（BSFC，kg/J）"),
        ("jet", "jet_tsfc_kg_per_n_s", "喷气发动机推力比油耗（TSFC，kg/(N·s)）"),
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
    jobs[0]["result"]["engineering"]["provenance"] = {
        "runner_validation": {"status": "complete"},
        "input_fields": {"requirements.range_m": "user"},
    }
    jobs[0]["result"]["engineering"]["stage_status"]["compatibility_weight_loop"] = {
        "status": "not_converged",
        "blocking": True,
        "message": "Weight loop did not converge",
    }
    jobs[0]["result"]["engineering"]["constraints"].extend(
        [
            {
                "id": "static_margin",
                "label": "Static stability margin",
                "category": "stability",
                "direction": "minimum",
                "required": 0.0,
                "actual": -0.03,
                "unit": "c_bar",
                "margin": -0.03,
                "margin_ratio": -0.03,
                "passed": False,
                "severity": "error",
                "blocking": True,
                "evidence": {"model": "E2E fixture", "prediction": True},
                "recommendation": "Move the center of gravity forward.",
            },
            {
                "id": "declared.special_mission_model_coverage",
                "label": "Special mission model coverage",
                "category": "requirements",
                "direction": "minimum",
                "required": 1.0,
                "actual": 0.0,
                "unit": "boolean",
                "margin": -1.0,
                "margin_ratio": -1.0,
                "passed": False,
                "severity": "error",
                "blocking": True,
                "evidence": {"model": "E2E fixture", "prediction": True},
                "recommendation": "Add dedicated mission models.",
            },
        ]
    )
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
        playwright_api.expect(page.locator("#designResultsContent")).to_contain_text("爬升推力裕度")
        playwright_api.expect(page.locator("#designResultsContent")).to_contain_text("平均气动弦长比例")
        playwright_api.expect(page.locator("#designResultsContent")).to_contain_text("专项任务模型覆盖")
        nonconverged_stage = page.locator(".design-stage-item").filter(has_text="未收敛")
        playwright_api.expect(nonconverged_stage).to_have_class(re.compile(r"\bis-fail\b"))
        coverage_row = page.locator("#designResultsContent tbody tr").filter(
            has_text="专项任务模型覆盖"
        )
        playwright_api.expect(coverage_row).to_contain_text("是")
        playwright_api.expect(coverage_row).to_contain_text("否")
        playwright_api.expect(coverage_row).to_contain_text("-1")
        playwright_api.expect(coverage_row).not_to_contain_text("待判定")
        localized_results_text = page.locator("#designResultsContent").inner_text()
        for english_text in (
            "Climb thrust margin",
            "Increase installed thrust",
            "Converged",
            "Propulsion gate",
            "Climb margin failed",
            "AircraftDesignRunner",
            "design_stage",
            "c_bar",
            "boolean",
        ):
            assert english_text not in localized_results_text
        playwright_api.expect(page.locator("#designResultsContent")).to_contain_text("求解器校验")
        playwright_api.expect(page.locator("#designResultsContent")).to_contain_text("输入字段来源")
        assert "runner_validation" not in localized_results_text
        assert "input_fields" not in localized_results_text
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
        playwright_api.expect(page.locator("#designResultsContent")).to_contain_text("初步可行候选")
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


def test_unknown_range_evidence_is_not_labeled_as_evaluated_or_maximum_range(
    e2e_browser,
    static_app_url: str,
) -> None:
    job = _job(
        "job-unknown-range-evidence",
        "Unknown range evidence",
        status="completed",
        mtow_kg=2_300.0,
        engineering_feasible=True,
    )
    job["result"]["summary"]["range_metric_kind"] = "unknown"
    context = e2e_browser.new_context(viewport={"width": 1280, "height": 900})
    page = context.new_page()
    _install_api_mock(page, jobs=[job])
    try:
        page.goto(static_app_url)
        page.locator("#designWorkspaceBtn").click()
        results = page.locator("#designResultsContent")
        playwright_api.expect(results).to_contain_text("航程指标（证据未声明）")
        assert "预测最大航程" not in results.inner_text()
        assert "评估任务航程" not in results.inner_text()
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
