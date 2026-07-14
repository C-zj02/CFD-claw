"""Backend acceptance tests for the web requirement-negotiation gate."""

from __future__ import annotations

import http.client
import json
import threading
from copy import deepcopy
from pathlib import Path
from unittest.mock import patch

import pytest

from src.config import _encode_api_key
from src.design_intake.store import IdempotencyConflictError
from src.design_execution import DesignJobQueueFullError
from src.providers.base import BaseProvider, ChatResponse
from src.tool_system.registry import ToolRegistry
from src.tool_system.tools.bash import BashTool
from src.tool_system.tools.glob import GlobTool
from src.tool_system.tools.read import FileReadTool
from src.tool_system.tools.write import FileWriteTool
from src.web import ClawdWebService
from src.web.app import _ClawdHTTPServer


class _FakeProvider(BaseProvider):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.calls = 0

    def chat(self, messages, tools=None, **kwargs) -> ChatResponse:
        self.calls += 1
        return ChatResponse(
            content="ordinary model response",
            model=self.model or "fake-model",
            usage={"input_tokens": 2, "output_tokens": 3},
            finish_reason="stop",
        )

    def chat_stream(self, messages, tools=None, **kwargs):
        yield "ordinary model response"

    def get_available_models(self) -> list[str]:
        return [self.model or "fake-model"]


@pytest.fixture
def web_service(tmp_path: Path):
    home = tmp_path / "home"
    workspace = tmp_path / "workspace"
    config_dir = home / ".clawd"
    config_dir.mkdir(parents=True)
    workspace.mkdir()
    (config_dir / "config.json").write_text(
        json.dumps(
            {
                "default_provider": "openai",
                "providers": {
                    "openai": {
                        "api_key": _encode_api_key("test-key"),
                        "base_url": "https://example.invalid/v1",
                        "default_model": "test-model",
                    }
                },
            }
        ),
        encoding="utf-8",
    )
    skill_root = workspace / ".clawd" / "skills" / "aircraft-design-skill"
    skill_root.mkdir(parents=True)
    (skill_root / "SKILL.md").write_text(
        "---\nname: aircraft-design-skill\ndescription: Test aircraft skill\n---\nTest.",
        encoding="utf-8",
    )

    with (
        patch("pathlib.Path.home", return_value=home),
        patch("src.web.app.get_provider_class", return_value=_FakeProvider),
        patch(
            "src.web.app.build_default_registry",
            side_effect=lambda **_kwargs: ToolRegistry(),
        ),
    ):
        service = ClawdWebService(workspace_root=workspace)
        try:
            yield service
        finally:
            service._design_jobs.shutdown()


def _create_aircraft_session(service: ClawdWebService) -> str:
    payload = service.create_session(
        provider_name="openai",
        model="test-model",
        auto_skill="aircraft-design-skill",
    )
    return payload["session"]["session_id"]


def _start_ready_design(service: ClawdWebService, session_id: str) -> dict:
    return service.send_message(
        session_id,
        "设计一款无人机，航程500km，载荷20kg。",
    )


def _action_payload(interaction: dict, action: str, action_id: str) -> dict:
    spec = next(item for item in interaction["actions"] if item["action"] == action)
    return {
        **deepcopy(spec.get("payload") or {}),
        "action": action,
        "expected_revision_hash": interaction["revision"]["revision_hash"],
        "client_action_id": action_id,
    }


def test_design_request_is_gated_before_skill_loading_or_llm(web_service) -> None:
    session_id = _create_aircraft_session(web_service)
    streamed_events: list[dict] = []

    with (
        patch.object(
            web_service,
            "_load_active_skill_context",
            side_effect=AssertionError("skill loading must be behind the requirement gate"),
        ) as load_skill,
        patch(
            "src.web.app.run_agent_loop",
            side_effect=AssertionError("LLM must not run during deterministic intake"),
        ) as agent_loop,
    ):
        result = web_service.send_message(
            session_id,
            "设计一款无人机，最大起飞重量不大于150kg，航程500km，载荷90kg。",
            on_tool_event=streamed_events.append,
        )

    load_skill.assert_not_called()
    agent_loop.assert_not_called()
    assert result["reply"]["text"] == ""
    assert result["reply"]["num_turns"] == 0
    assert len(streamed_events) == 1
    event = result["reply"]["events"][0]
    assert event["kind"] == "requirement_interaction"
    interaction = event["preview"]["interaction"]
    assert set(interaction) >= {
        "contract_version",
        "session_id",
        "revision",
        "intent",
        "diagnosis",
        "actions",
    }
    assert interaction["diagnosis"]["status"] == "repairable"
    assert interaction["actions"][0]["action"] == "apply_change"
    assert [message["role"] for message in result["session"]["messages"]] == [
        "user",
        "assistant",
    ]
    assert result["session"]["messages"][1]["text"] == ""
    assert result["session"]["messages"][1]["events"] == [event]


def test_active_skill_ordinary_question_still_uses_existing_agent_path(web_service) -> None:
    session_id = _create_aircraft_session(web_service)
    state = web_service._require_session(session_id)

    with (
        patch.object(web_service, "_load_active_skill_context", return_value=None) as load_skill,
        patch.object(web_service, "_maybe_prepare_design_context", return_value=None),
    ):
        result = web_service.send_message(session_id, "这个总体设计技能如何优化？")

    load_skill.assert_called_once()
    assert state.provider.calls == 1
    assert result["reply"]["text"] == "ordinary model response"
    assert web_service._requirement_workflow.current(session_id) is None


@pytest.mark.parametrize(
    ("message", "auto_skill"),
    [
        ("继续，直接计算", None),
        ("请计算一下当前方案", None),
        ("求解这个方案", None),
        ("请运行这个方案", None),
        ("算一下", None),
        ("开始吧", None),
        ("proceed", None),
        ("execute this design", None),
        ("继续，直接计算", ""),
    ],
)
def test_pending_revision_cannot_bypass_interaction_or_run_agent(
    web_service,
    message: str,
    auto_skill: str | None,
) -> None:
    session_id = _create_aircraft_session(web_service)
    initial = _start_ready_design(web_service, session_id)["reply"]["events"][0][
        "preview"
    ]["interaction"]

    with (
        patch.object(
            web_service,
            "_load_active_skill_context",
            side_effect=AssertionError("pending revision must not load executable skill context"),
        ) as load_skill,
        patch(
            "src.web.app.run_agent_loop",
            side_effect=AssertionError("pending revision must not enter the agent loop"),
        ) as agent_loop,
    ):
        result = web_service.send_message(
            session_id,
            message,
            **({"auto_skill": auto_skill} if auto_skill is not None else {}),
        )

    load_skill.assert_not_called()
    agent_loop.assert_not_called()
    interaction = result["reply"]["events"][0]["preview"]["interaction"]
    assert interaction["revision"]["revision_id"] == initial["revision"]["revision_id"]
    assert interaction["actions"][0]["action"] == "confirm_revision"


def test_conversational_parameter_edit_is_a_diff_against_current_revision(web_service) -> None:
    session_id = _create_aircraft_session(web_service)
    initial = _start_ready_design(web_service, session_id)["reply"]["events"][0][
        "preview"
    ]["interaction"]

    result = web_service.send_message(session_id, "把载荷改为15kg")
    interaction = result["reply"]["events"][0]["preview"]["interaction"]

    assert interaction["revision"]["revision_number"] == (
        initial["revision"]["revision_number"] + 1
    )
    assert interaction["diagnosis"]["status"] == "repairable"
    proposal = interaction["diagnosis"]["change_proposals"][0]
    assert proposal["field_path"] == "requirements.payload_kg"
    assert proposal["old_value"] == 20.0
    assert proposal["proposed_value"] == 15.0
    current_payload = next(
        item["value"]
        for item in interaction["intent"]["requirements"]
        if item["path"] == "requirements.payload_kg"
    )
    assert current_payload == 20.0


def test_aircraft_skill_agent_path_exposes_read_only_tools(web_service) -> None:
    state = web_service._require_session(_create_aircraft_session(web_service))
    state.tool_registry = ToolRegistry(
        [BashTool(), FileReadTool(), GlobTool(), FileWriteTool()]
    )

    filtered = web_service._active_skill_tool_registry(
        state,
        {
            "name": "aircraft-design-skill",
            "allowed_tools": ["Bash", "Read", "Glob", "Write"],
        },
    )

    assert {item.name for item in filtered.list_specs()} == {"Read", "Glob"}


def test_batch_answers_and_repair_actions_create_new_interactions(web_service) -> None:
    session_id = _create_aircraft_session(web_service)
    initial = web_service.send_message(
        session_id,
        "设计一款无人机，巡航马赫数0.3。",
    )["reply"]["events"][0]["preview"]["interaction"]
    assert initial["diagnosis"]["status"] == "needs_clarification"

    answers = [
        {
            "question_id": "mission.range.required",
            "field_path": "mission.range_m",
            "value": 450_000.0,
        },
        {
            "question_id": "mission.payload.required",
            "field_path": "mission.payload_kg",
            "value": 25.0,
        },
    ]
    response = web_service.apply_requirement_revision_action(
        session_id,
        initial["revision"]["revision_id"],
        {
            **_action_payload(initial, "answer_question", "answer-web-001"),
            "decisions": {"clarification_answers": answers},
        },
    )

    assert response["interaction"]["diagnosis"]["status"] == "ready_for_solver"
    assert response["interaction"]["actions"][0]["action"] == "confirm_revision"
    assert response["session"]["messages"][-1]["events"][0]["kind"] == (
        "requirement_interaction"
    )


def test_apply_change_and_defer_unsupported_are_audited_web_actions(web_service) -> None:
    repair_session = _create_aircraft_session(web_service)
    repair = web_service.send_message(
        repair_session,
        "设计一款无人机，最大起飞重量不大于150kg，航程500km，载荷90kg。",
    )["reply"]["events"][0]["preview"]["interaction"]
    proposal_id = repair["diagnosis"]["change_proposals"][0]["proposal_id"]
    repaired = web_service.apply_requirement_revision_action(
        repair_session,
        repair["revision"]["revision_id"],
        {
            **_action_payload(repair, "apply_change", "repair-web-001"),
            "proposal_id": proposal_id,
        },
    )["interaction"]
    assert repaired["revision"]["revision_number"] > repair["revision"][
        "revision_number"
    ]
    assert proposal_id in repaired["intent"]["accepted_change_proposal_ids"]

    unsupported_session = _create_aircraft_session(web_service)
    unsupported = web_service.send_message(
        unsupported_session,
        "设计一款隐身无人机，航程500km，载荷20kg，最大飞行马赫数0.8，"
        "采用火箭助推和伞降回收。",
    )["reply"]["events"][0]["preview"]["interaction"]
    assert unsupported["diagnosis"]["status"] == "unsupported"
    assert "infeasible" not in unsupported["diagnosis"]["status"]
    deferred = web_service.apply_requirement_revision_action(
        unsupported_session,
        unsupported["revision"]["revision_id"],
        _action_payload(unsupported, "defer_unsupported", "defer-web-001"),
    )["interaction"]
    fields = {item["path"]: item for item in deferred["intent"]["requirements"]}
    assert fields["launch.mode"]["role"] == "soft_goal"
    assert fields["recovery.mode"]["locked"] is False


def test_confirmed_revision_submits_one_bounded_repair_job(web_service, monkeypatch) -> None:
    session_id = _create_aircraft_session(web_service)
    initial = _start_ready_design(web_service, session_id)["reply"]["events"][0][
        "preview"
    ]["interaction"]
    confirmed = web_service.apply_requirement_revision_action(
        session_id,
        initial["revision"]["revision_id"],
        _action_payload(initial, "confirm_revision", "confirm-web-001"),
    )["interaction"]
    assert confirmed["revision"]["confirmed"] is True
    assert confirmed["actions"][0]["action"] == "submit_solver"

    jobs: list[dict] = []
    submitted_requests = []

    def submit(request, *, timeout_seconds: float):
        submitted_requests.append(request)
        job = {
            "job_id": "job-requirement-001",
            "status": "queued",
            "stage": "queued",
            "progress": 0,
            "message": "queued",
            "request": request.to_dict(),
            "timeout_seconds": timeout_seconds,
            "created_at": "2026-07-14T00:00:00",
            "started_at": None,
            "finished_at": None,
            "retry_of": None,
            "error": None,
            "terminal": False,
            "last_sequence": 0,
            "events": [],
            "result": None,
        }
        jobs.append(job)
        return deepcopy(job)

    monkeypatch.setattr(web_service._design_jobs, "submit", submit)
    monkeypatch.setattr(
        web_service._design_jobs,
        "list",
        lambda: [{"job_id": item["job_id"]} for item in jobs],
    )
    monkeypatch.setattr(
        web_service._design_jobs,
        "get",
        lambda job_id: deepcopy(next(item for item in jobs if item["job_id"] == job_id)),
    )

    first = web_service.apply_requirement_revision_action(
        session_id,
        confirmed["revision"]["revision_id"],
        _action_payload(confirmed, "submit_solver", "submit-web-001"),
    )
    second_payload = _action_payload(confirmed, "submit_solver", "submit-web-002")
    second = web_service.apply_requirement_revision_action(
        session_id,
        confirmed["revision"]["revision_id"],
        second_payload,
    )

    assert first["job"]["job_id"] == second["job"]["job_id"]
    assert len(submitted_requests) == 1
    assert first["interaction"]["actions"] == []
    current = web_service._requirement_workflow.current(session_id)
    assert current is not None
    assert current["submitted"] is True
    assert current["can_submit"] is False
    submission = current["solver_submission"]
    assert submission["job_id"] == "job-requirement-001"
    assert submission["session_id"] == session_id
    assert submission["revision_id"] == confirmed["revision"]["revision_id"]
    assert submission["revision_hash"] == confirmed["revision"]["revision_hash"]
    assert submission["client_action_id"] == "submit-web-001"
    request = submitted_requests[0]
    assert request.auto_repair_enabled is True
    assert request.max_repair_attempts == 3
    workflow = request.provenance["requirement_workflow"]
    assert workflow["session_id"] == session_id
    assert workflow["revision_id"] == confirmed["revision"]["revision_id"]
    assert workflow["revision_hash"] == confirmed["revision"]["revision_hash"]

    with pytest.raises(IdempotencyConflictError):
        web_service.apply_requirement_revision_action(
            session_id,
            confirmed["revision"]["revision_id"],
            _action_payload(confirmed, "submit_solver", "confirm-web-001"),
        )


def test_trusted_terminal_failure_creates_a_new_negotiation_revision(
    web_service,
    monkeypatch,
) -> None:
    session_id = _create_aircraft_session(web_service)
    initial = web_service.send_message(
        session_id,
        "设计一款无人机，最大起飞重量不大于260kg，航程500km，载荷20kg。",
    )["reply"]["events"][0]["preview"]["interaction"]
    confirmed = web_service.apply_requirement_revision_action(
        session_id,
        initial["revision"]["revision_id"],
        _action_payload(initial, "confirm_revision", "confirm-outcome-web"),
    )["interaction"]
    jobs: dict[str, dict] = {}

    def submit(request, *, timeout_seconds: float):
        job = {
            "job_id": "job-outcome-web-001",
            "status": "queued",
            "stage": "queued",
            "progress": 0,
            "message": "queued",
            "request": request.to_dict(),
            "timeout_seconds": timeout_seconds,
            "created_at": "2026-07-14T00:00:00",
            "started_at": None,
            "finished_at": None,
            "retry_of": None,
            "error": None,
            "terminal": False,
            "last_sequence": 0,
            "events": [],
            "result": None,
        }
        jobs[job["job_id"]] = job
        return deepcopy(job)

    monkeypatch.setattr(web_service._design_jobs, "submit", submit)
    monkeypatch.setattr(
        web_service._design_jobs,
        "list",
        lambda: [{"job_id": job_id} for job_id in jobs],
    )
    monkeypatch.setattr(
        web_service._design_jobs,
        "get",
        lambda job_id: deepcopy(jobs[job_id]),
    )
    submitted = web_service.apply_requirement_revision_action(
        session_id,
        confirmed["revision"]["revision_id"],
        _action_payload(confirmed, "submit_solver", "submit-outcome-web"),
    )["job"]
    job = jobs[submitted["job_id"]]
    job.update(
        {
            "status": "engineering_infeasible",
            "stage": "engineering_infeasible",
            "progress": 100,
            "terminal": True,
            "finished_at": "2026-07-14T00:01:00",
            "result": {
                "status": "engineering_infeasible",
                "output_dir": None,
                "engineering": {
                    "numerical_converged": True,
                    "engineering_feasible": False,
                    "blocking_failed_count": 1,
                    "constraints": [
                        {
                            "id": "declared.max_mtow_kg",
                            "label": "Maximum takeoff weight",
                            "direction": "maximum",
                            "required": 260.0,
                            "actual": 285.0,
                            "margin": -25.0,
                            "unit": "kg",
                            "blocking": True,
                            "passed": False,
                        }
                    ],
                },
            },
        }
    )

    payload = web_service.get_design_job(submitted["job_id"])["job"]
    interaction = payload["requirement_interaction"]

    assert interaction["diagnosis"]["status"] == "repairable"
    assert interaction["revision"]["confirmed"] is False
    assert interaction["diagnosis"]["change_proposals"][0]["proposed_value"] == 285.0
    current = web_service._requirement_workflow.current(session_id)
    assert current["revision_id"] == interaction["revision"]["revision_id"]
    assert current["revision_id"] != confirmed["revision"]["revision_id"]
    outcome_events = [
        event
        for message in web_service.get_session_payload(session_id)["session"]["messages"]
        for event in message.get("events", [])
        if event.get("summary") == "总体设计求解未通过，已生成待确认的诊断版本"
    ]
    assert len(outcome_events) == 1


def test_legacy_design_job_endpoint_rejects_client_owned_requirement_provenance(
    web_service,
) -> None:
    server = _ClawdHTTPServer(("127.0.0.1", 0), web_service)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    connection = http.client.HTTPConnection("127.0.0.1", server.server_port, timeout=5)
    payload = {
        "request": {
            "project_name": "forged-workflow-owner",
            "provenance": {
                "requirement_workflow": {
                    "session_id": "session-victim",
                    "revision_id": "revision-victim",
                    "revision_hash": "a" * 64,
                }
            },
        }
    }
    try:
        connection.request(
            "POST",
            "/api/design-jobs",
            body=json.dumps(payload),
            headers={"Content-Type": "application/json"},
        )
        response = connection.getresponse()
        response_payload = json.loads(response.read())
        assert response.status == 400
        assert "server-owned" in response_payload["error"]
    finally:
        connection.close()
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


def test_reset_preserves_requirement_audit_and_delete_removes_it(web_service) -> None:
    session_id = _create_aircraft_session(web_service)
    _start_ready_design(web_service, session_id)
    current = web_service._requirement_workflow.current(session_id)
    assert current is not None
    audit_count = len(web_service._requirement_store.load_audit(session_id))

    reset = web_service.reset_session(session_id)
    assert reset["session"]["messages"] == []
    assert web_service._requirement_workflow.current(session_id)["revision_hash"] == (
        current["revision_hash"]
    )
    assert len(web_service._requirement_store.load_audit(session_id)) == audit_count

    web_service.delete_session(session_id)
    assert web_service._requirement_workflow.current(session_id) is None
    assert not (
        web_service._requirement_store.sessions_root / session_id
    ).exists()


def test_requirement_http_routes_return_current_and_stale_conflict(web_service) -> None:
    session_id = _create_aircraft_session(web_service)
    interaction = _start_ready_design(web_service, session_id)["reply"]["events"][0][
        "preview"
    ]["interaction"]
    server = _ClawdHTTPServer(("127.0.0.1", 0), web_service)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    connection = http.client.HTTPConnection("127.0.0.1", server.server_port, timeout=5)
    try:
        connection.request(
            "GET",
            f"/api/sessions/{session_id}/requirement-revisions/current",
        )
        current_response = connection.getresponse()
        current_payload = json.loads(current_response.read())
        assert current_response.status == 200
        assert current_payload["interaction"]["revision"]["revision_id"] == (
            interaction["revision"]["revision_id"]
        )

        stale = _action_payload(interaction, "confirm_revision", "confirm-stale-001")
        stale["expected_revision_hash"] = "0" * 64
        connection.request(
            "POST",
            (
                f"/api/sessions/{session_id}/requirement-revisions/"
                f"{interaction['revision']['revision_id']}/actions"
            ),
            body=json.dumps(stale),
            headers={"Content-Type": "application/json"},
        )
        stale_response = connection.getresponse()
        stale_payload = json.loads(stale_response.read())
        assert stale_response.status == 409
        assert "revision" in stale_payload["error"]

        invalid = _action_payload(interaction, "confirm_revision", "bad-action-001")
        invalid["action"] = "replace_server_request"
        connection.request(
            "POST",
            (
                f"/api/sessions/{session_id}/requirement-revisions/"
                f"{interaction['revision']['revision_id']}/actions"
            ),
            body=json.dumps(invalid),
            headers={"Content-Type": "application/json"},
        )
        invalid_response = connection.getresponse()
        invalid_response.read()
        assert invalid_response.status == 400

        connection.request(
            "POST",
            f"/api/sessions/{session_id}/requirement-revisions/rev-missing/actions",
            body=json.dumps(
                _action_payload(interaction, "confirm_revision", "missing-revision-001")
            ),
            headers={"Content-Type": "application/json"},
        )
        missing_response = connection.getresponse()
        missing_response.read()
        assert missing_response.status == 404

        confirmed = web_service.apply_requirement_revision_action(
            session_id,
            interaction["revision"]["revision_id"],
            _action_payload(interaction, "confirm_revision", "confirm-http-001"),
        )["interaction"]
        submit = _action_payload(confirmed, "submit_solver", "submit-http-001")
        with patch.object(
            web_service._design_jobs,
            "submit",
            side_effect=DesignJobQueueFullError("aircraft design job queue is full"),
        ):
            connection.request(
                "POST",
                (
                    f"/api/sessions/{session_id}/requirement-revisions/"
                    f"{confirmed['revision']['revision_id']}/actions"
                ),
                body=json.dumps(submit),
                headers={"Content-Type": "application/json"},
            )
            queue_response = connection.getresponse()
            queue_response.read()
        assert queue_response.status == 429
    finally:
        connection.close()
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


def test_empty_text_message_with_interaction_events_is_serialized(web_service) -> None:
    session_id = _create_aircraft_session(web_service)
    state = web_service._require_session(session_id)
    state.session.conversation.add_assistant_message("")
    state.session.conversation.messages[-1].events = [
        {
            "kind": "requirement_interaction",
            "preview": {"interaction": {"contract_version": 1}},
        }
    ]

    messages = web_service.get_session_payload(session_id)["session"]["messages"]
    assert messages == [
        {
            "role": "assistant",
            "text": "",
            "blocks": [],
            "events": state.session.conversation.messages[-1].events,
            "artifacts": [],
            "timestamp": state.session.conversation.messages[-1].timestamp,
        }
    ]
