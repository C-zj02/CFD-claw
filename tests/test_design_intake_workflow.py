"""End-to-end contract tests for versioned requirement negotiation."""

from __future__ import annotations

from pathlib import Path

import pytest

from src.design_intake.models import RequirementRole
from src.design_intake.store import (
    DesignRevisionStore,
    RevisionConflictError,
    canonical_sha256,
)
from src.design_intake.workflow import (
    DesignRequirementWorkflow,
    WorkflowActionError,
    WorkflowStateError,
)


def _workflow(tmp_path: Path) -> DesignRequirementWorkflow:
    return DesignRequirementWorkflow(DesignRevisionStore(tmp_path / "requirements"))


_COMPLEX_UNSUPPORTED_REQUEST = (
    "设计一款隐身作战无人机，要求最大起飞重量不大于260kg，任务载荷60kg，"
    "设计巡航高度9.5km，巡航马赫数0.6，要求巡航航时不低于1h，"
    "设计最大飞行马赫数0.8，使用升限10km，采用火箭助推+伞降回收形式，"
    "发射场海拔1500m，火箭助推结束为马赫数0.28、相对高度40m，"
    "开伞速度Ma0.24，相对高度1000m，采用单发布局形式，"
    "布局风格可参考沙赫德-136无人机，展弦比不大于2.5。"
)


def _record_submission(
    workflow: DesignRequirementWorkflow,
    session_id: str,
    confirmed: dict,
    job_id: str,
) -> str:
    request = workflow.project_solver_request(
        session_id,
        expected_revision_hash=confirmed["revision_hash"],
    )
    request_hash = canonical_sha256(request.to_dict())
    workflow.store.record_solver_submission(
        session_id,
        job_id=job_id,
        revision_id=confirmed["revision_id"],
        expected_revision_hash=confirmed["revision_hash"],
        request_hash=request_hash,
        client_action_id=f"submit-{job_id}",
    )
    return request_hash


def test_ready_intake_materializes_defaults_as_auditable_child_revision(tmp_path: Path) -> None:
    workflow = _workflow(tmp_path)

    snapshot = workflow.start(
        "session-001",
        "设计一款无人机，航程500km，载荷20kg。",
        client_action_id="start-001",
    )

    assert snapshot["diagnosis"]["status"] == "ready_for_solver"
    assert snapshot["defaults_materialized"] is True
    assert snapshot["confirmed"] is False
    assert snapshot["allowed_actions"] == ["confirm_revision"]
    assert snapshot["revision_number"] == 2
    assert snapshot["intent"]["revision"] == 2
    assert snapshot["intent"]["metadata"]["solver_completion"]["completed"] is True
    assert any(
        item["path"] == "requirements.cruise_mach" and item["source"] == "default"
        for item in snapshot["intent"]["requirements"]
    )
    assert len(workflow.store.load_audit("session-001")) == 2


def test_same_session_can_start_a_new_design_without_deleting_audit(tmp_path: Path) -> None:
    workflow = _workflow(tmp_path)
    first = workflow.start(
        "session-001",
        "设计一款无人机，航程500km，载荷20kg。",
        client_action_id="start-001",
    )

    second = workflow.start(
        "session-001",
        "设计一款无人机，航程300km，载荷10kg。",
        client_action_id="start-002",
    )

    assert second["revision_number"] == 4
    assert second["intent"]["intent_id"] != first["intent"]["intent_id"]
    assert second["confirmed"] is False
    assert workflow.store.load_revision(
        "session-001", first["revision_id"]
    )["revision_hash"] == first["revision_hash"]
    assert len(workflow.store.load_audit("session-001")) == 4


def test_batch_answers_create_one_user_revision_then_complete_defaults(tmp_path: Path) -> None:
    workflow = _workflow(tmp_path)
    initial = workflow.start(
        "session-001",
        "设计一款无人机，巡航马赫数0.3。",
        client_action_id="start-001",
    )
    assert initial["diagnosis"]["status"] == "needs_clarification"

    answered = workflow.answer_questions(
        "session-001",
        answers=[
            {
                "question_id": "mission.range.required",
                "field_path": "mission.range_m",
                "value": "450000",
            },
            {
                "question_id": "mission.payload.required",
                "field_path": "mission.payload_kg",
                "value": 25.0,
            },
        ],
        expected_revision_hash=initial["revision_hash"],
        client_action_id="answer-001",
    )

    assert answered["diagnosis"]["status"] == "ready_for_solver"
    assert answered["revision_number"] == 3
    fields = {item["path"]: item for item in answered["intent"]["requirements"]}
    assert fields["requirements.range_m"]["value"] == 450_000.0
    assert fields["requirements.payload_kg"]["value"] == 25.0
    assert fields["requirements.range_m"]["source"] == "user"

    repeated = workflow.answer_questions(
        "session-001",
        answers=[
            {
                "question_id": "mission.range.required",
                "field_path": "mission.range_m",
                "value": "450000",
            },
            {
                "question_id": "mission.payload.required",
                "field_path": "mission.payload_kg",
                "value": 25.0,
            },
        ],
        expected_revision_hash=initial["revision_hash"],
        client_action_id="answer-001",
    )
    assert repeated["revision_id"] == answered["revision_id"]


def test_locked_repair_proposal_requires_explicit_confirmation(tmp_path: Path) -> None:
    workflow = _workflow(tmp_path)
    initial = workflow.start(
        "session-001",
        "设计一款无人机，最大起飞重量不大于150kg，航程500km，载荷90kg。",
        client_action_id="start-001",
    )
    assert initial["diagnosis"]["status"] == "repairable"

    with pytest.raises(PermissionError, match="requires user confirmation"):
        workflow.apply_change(
            "session-001",
            proposal_id="mass.increase_mtow_allowance",
            expected_revision_hash=initial["revision_hash"],
            client_action_id="repair-denied",
            user_confirmed=False,
        )

    repaired = workflow.apply_change(
        "session-001",
        proposal_id="mass.increase_mtow_allowance",
        expected_revision_hash=initial["revision_hash"],
        client_action_id="repair-accepted",
        user_confirmed=True,
    )

    assert repaired["diagnosis"]["status"] == "ready_for_solver"
    max_mtow = next(
        item
        for item in repaired["intent"]["requirements"]
        if item["path"] == "weights.max_mtow_kg"
    )
    assert max_mtow["value"] == 180.0
    assert "mass.increase_mtow_allowance" in repaired["intent"][
        "accepted_change_proposal_ids"
    ]


def test_change_proposal_cannot_bypass_pending_clarification(tmp_path: Path) -> None:
    workflow = _workflow(tmp_path)
    initial = workflow.start(
        "session-question-before-change",
        "设计一款无人机，最大起飞重量不大于150kg，任务载荷150kg。",
        client_action_id="start-question-before-change",
    )

    assert initial["allowed_actions"] == ["answer_questions"]
    assert initial["diagnosis"]["clarification_questions"]
    proposal = initial["diagnosis"]["change_proposals"][0]
    with pytest.raises(WorkflowStateError, match="must be answered before"):
        workflow.apply_change(
            "session-question-before-change",
            proposal_id=proposal["proposal_id"],
            expected_revision_hash=initial["revision_hash"],
            client_action_id="change-too-early",
            user_confirmed=True,
        )


def test_unsupported_requirements_are_retained_when_user_accepts_reduced_scope(
    tmp_path: Path,
) -> None:
    workflow = _workflow(tmp_path)
    initial = workflow.start(
        "session-001",
        "设计一款隐身无人机，航程500km，载荷20kg，最大飞行马赫数0.8，"
        "采用火箭助推和伞降回收。",
        client_action_id="start-001",
    )
    assert initial["diagnosis"]["status"] == "unsupported"

    with pytest.raises(PermissionError, match="requires user confirmation"):
        workflow.defer_unsupported(
            "session-001",
            field_paths=None,
            scope_statement="先做当前模型覆盖范围。",
            expected_revision_hash=initial["revision_hash"],
            client_action_id="scope-denied",
            user_confirmed=False,
        )

    deferred = workflow.defer_unsupported(
        "session-001",
        field_paths=None,
        scope_statement="先完成当前 Class I/II 覆盖范围，专项要求保留为后续验证缺口。",
        expected_revision_hash=initial["revision_hash"],
        client_action_id="scope-accepted",
        user_confirmed=True,
    )

    fields = {item["path"]: item for item in deferred["intent"]["requirements"]}
    for path in (
        "performance.max_flight_mach",
        "launch.mode",
        "recovery.mode",
        "configuration.stealth_requirement",
    ):
        assert path in fields
        assert fields[path]["role"] == RequirementRole.SOFT_GOAL.value
        assert fields[path]["locked"] is False
    assert not any(
        item["status"] == "unsupported" and item["blocking"]
        for item in deferred["diagnosis"]["coverage"]
    )
    deferrals = deferred["intent"]["metadata"]["requirement_workflow"][
        "scope_deferrals"
    ][0]
    assert len(deferrals["fields"]) == 4


def test_unsupported_request_answers_blocking_questions_before_scope_deferral(
    tmp_path: Path,
) -> None:
    workflow = _workflow(tmp_path)
    initial = workflow.start(
        "session-two-step",
        _COMPLEX_UNSUPPORTED_REQUEST,
        client_action_id="start-two-step",
    )

    assert initial["diagnosis"]["status"] == "unsupported"
    assert initial["allowed_actions"] == ["answer_questions"]
    questions = {
        item["question_id"]: item
        for item in initial["diagnosis"]["clarification_questions"]
    }
    assert set(questions) == {
        "mission.range.required",
        "propulsion.type.high_speed",
    }
    with pytest.raises(WorkflowStateError, match="must be answered before"):
        workflow.defer_unsupported(
            "session-two-step",
            field_paths=None,
            scope_statement="先求解当前模型覆盖范围。",
            expected_revision_hash=initial["revision_hash"],
            client_action_id="defer-too-early",
            user_confirmed=True,
        )

    answered = workflow.answer_questions(
        "session-two-step",
        answers=[
            {
                "question_id": "mission.range.required",
                "field_path": "mission.range_m",
                "value": 950_000,
            },
            {
                "question_id": "propulsion.type.high_speed",
                "field_path": "propulsion.propulsion_type",
                "value": "jet",
            },
        ],
        expected_revision_hash=initial["revision_hash"],
        client_action_id="answer-two-step",
    )

    assert answered["diagnosis"]["status"] == "unsupported"
    assert answered["diagnosis"]["clarification_questions"] == []
    assert answered["allowed_actions"] == ["defer_unsupported"]
    answered_fields = {
        item["path"]: item for item in answered["intent"]["requirements"]
    }
    assert answered_fields["requirements.range_m"]["value"] == 950_000
    assert answered_fields["requirements.propulsion_type"]["value"] == "jet"

    unsupported_paths = [
        item["field_path"]
        for item in answered["diagnosis"]["coverage"]
        if item["status"] == "unsupported" and item["blocking"]
    ]
    scoped = workflow.defer_unsupported(
        "session-two-step",
        field_paths=unsupported_paths,
        scope_statement=(
            "保留当前模型未覆盖的专项要求作为后续验证缺口，"
            "本轮只求解已覆盖的 Class I/II 范围。"
        ),
        expected_revision_hash=answered["revision_hash"],
        client_action_id="defer-two-step",
        user_confirmed=True,
    )

    assert scoped["diagnosis"]["status"] == "ready_for_solver"
    assert scoped["allowed_actions"] == ["confirm_revision"]
    scoped_fields = {item["path"]: item for item in scoped["intent"]["requirements"]}
    for path in (
        "performance.min_cruise_endurance_s",
        "performance.max_flight_mach",
        "launch.mode",
        "recovery.mode",
        "configuration.stealth_requirement",
    ):
        assert scoped_fields[path]["role"] == "soft_goal"
        assert scoped_fields[path]["source"] == "user"
    assert scoped_fields["requirements.range_m"]["value"] == 950_000
    assert scoped_fields["requirements.propulsion_type"]["value"] == "jet"

    confirmed = workflow.confirm_revision(
        "session-two-step",
        expected_revision_hash=scoped["revision_hash"],
        client_action_id="confirm-two-step",
        user_confirmed=True,
    )
    assert confirmed["confirmed"] is True
    assert confirmed["allowed_actions"] == ["submit_solver"]


def test_confirmation_is_required_before_solver_projection(tmp_path: Path) -> None:
    workflow = _workflow(tmp_path)
    ready = workflow.start(
        "session-001",
        "设计一款无人机，航程500km，载荷20kg。",
        client_action_id="start-001",
    )

    with pytest.raises(WorkflowStateError, match="explicitly confirmed"):
        workflow.project_solver_request(
            "session-001", expected_revision_hash=ready["revision_hash"]
        )

    confirmed = workflow.confirm_revision(
        "session-001",
        expected_revision_hash=ready["revision_hash"],
        client_action_id="confirm-001",
        user_confirmed=True,
    )
    request = workflow.project_solver_request(
        "session-001", expected_revision_hash=confirmed["revision_hash"]
    )

    assert confirmed["confirmed"] is True
    assert confirmed["can_submit"] is True
    assert confirmed["allowed_actions"] == ["submit_solver"]
    assert request.requirements.range_m == 500_000.0
    assert request.provenance["projection"]["intent_revision"] == confirmed["intent"][
        "revision"
    ]


def test_deferred_out_of_envelope_solver_field_is_preserved_but_not_projected(
    tmp_path: Path,
) -> None:
    workflow = _workflow(tmp_path)
    initial = workflow.start(
        "session-001",
        "设计一款无人机，航程500km，载荷20kg，巡航高度40km。",
        client_action_id="start-001",
    )
    assert initial["diagnosis"]["status"] == "unsupported"

    question = initial["diagnosis"]["clarification_questions"][0]
    assert question["question_id"] == "performance.service_ceiling.high_cruise"
    answered = workflow.answer_questions(
        "session-001",
        answers=[
            {
                "question_id": question["question_id"],
                "field_path": question["field_path"],
                "value": 40_000.0,
            }
        ],
        expected_revision_hash=initial["revision_hash"],
        client_action_id="answer-ceiling",
    )
    assert answered["allowed_actions"] == ["defer_unsupported"]
    unsupported_paths = [
        item["field_path"]
        for item in answered["diagnosis"]["coverage"]
        if item["status"] == "unsupported" and item["blocking"]
    ]

    deferred = workflow.defer_unsupported(
        "session-001",
        field_paths=unsupported_paths,
        scope_statement="保留 40 km 目标，先在当前大气模型覆盖范围内完成方案筛选。",
        expected_revision_hash=answered["revision_hash"],
        client_action_id="scope-accepted",
        user_confirmed=True,
    )

    fields = {item["path"]: item for item in deferred["intent"]["requirements"]}
    assert fields["deferred.requirements.cruise_altitude_m"]["value"] == 40_000.0
    assert fields["deferred.requirements.cruise_altitude_m"]["role"] == "soft_goal"
    assert fields["requirements.service_ceiling_m"]["value"] == 40_000.0
    assert fields["requirements.cruise_altitude_m"]["value"] <= 35_000.0
    assert fields["requirements.cruise_altitude_m"]["source"] == "default"

    confirmed = workflow.confirm_revision(
        "session-001",
        expected_revision_hash=deferred["revision_hash"],
        client_action_id="confirm-001",
        user_confirmed=True,
    )
    request = workflow.project_solver_request(
        "session-001", expected_revision_hash=confirmed["revision_hash"]
    )
    assert request.requirements.cruise_altitude_m != 40_000.0
    assert request.provenance["soft_goals"][
        "deferred.requirements.cruise_altitude_m"
    ] == 40_000.0
    preserved = {
        item["path"]: item
        for item in request.provenance["requirement_intent"]["requirements"]
    }
    assert preserved["deferred.requirements.cruise_altitude_m"]["value"] == 40_000.0


def test_mutating_action_rejects_stale_revision_hash(tmp_path: Path) -> None:
    workflow = _workflow(tmp_path)
    current = workflow.start(
        "session-001",
        "设计一款无人机，巡航马赫数0.3。",
        client_action_id="start-001",
    )

    with pytest.raises(RevisionConflictError, match="stale revision hash"):
        workflow.answer_questions(
            "session-001",
            answers=[
                {"question_id": "mission.range.required", "value": 450_000.0},
            ],
            expected_revision_hash="0" * 64,
            client_action_id="answer-stale",
        )

    assert workflow.current("session-001")["revision_id"] == current["revision_id"]


def test_failed_solver_outcome_creates_unconfirmed_evidence_backed_revision(
    tmp_path: Path,
) -> None:
    workflow = _workflow(tmp_path)
    ready = workflow.start(
        "session-outcome",
        "设计一款无人机，最大起飞重量不大于260kg，航程500km，载荷20kg。",
        client_action_id="start-outcome",
    )
    confirmed = workflow.confirm_revision(
        "session-outcome",
        expected_revision_hash=ready["revision_hash"],
        client_action_id="confirm-outcome",
        user_confirmed=True,
    )
    request_hash = _record_submission(
        workflow, "session-outcome", confirmed, "job-outcome-001"
    )
    result = {
        "status": "engineering_infeasible",
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
                    "margin_ratio": -25.0 / 260.0,
                    "unit": "kg",
                    "blocking": True,
                    "passed": False,
                }
            ],
        },
    }

    feedback = workflow.ingest_solver_outcome(
        "session-outcome",
        revision_id=confirmed["revision_id"],
        expected_revision_hash=confirmed["revision_hash"],
        job_id="job-outcome-001",
        request_hash=request_hash,
        result=result,
    )

    assert feedback["revision_number"] == confirmed["revision_number"] + 1
    assert feedback["confirmed"] is False
    assert feedback["diagnosis"]["status"] == "repairable"
    assert feedback["allowed_actions"] == ["apply_change"]
    proposal = feedback["diagnosis"]["change_proposals"][0]
    assert proposal["field_path"] == "weights.max_mtow_kg"
    assert proposal["old_value"] == 260.0
    assert proposal["proposed_value"] == 285.0
    assert proposal["requires_user_confirmation"] is True
    assert "required=260.0 kg" in proposal["reason"]
    assert feedback["intent"]["metadata"]["solver_outcomes"][-1][
        "failed_constraints"
    ][0]["margin"] == -25.0

    repeated = workflow.ingest_solver_outcome(
        "session-outcome",
        revision_id=confirmed["revision_id"],
        expected_revision_hash=confirmed["revision_hash"],
        job_id="job-outcome-001",
        request_hash=request_hash,
        result=result,
    )
    assert repeated["revision_id"] == feedback["revision_id"]

    with pytest.raises(PermissionError, match="requires user confirmation"):
        workflow.apply_change(
            "session-outcome",
            proposal_id=proposal["proposal_id"],
            expected_revision_hash=feedback["revision_hash"],
            client_action_id="reject-silent-outcome-change",
            user_confirmed=False,
        )


def test_failed_solver_outcome_never_proposes_reducing_unmodeled_cruise_endurance(
    tmp_path: Path,
) -> None:
    workflow = _workflow(tmp_path)
    initial = workflow.start(
        "session-endurance-outcome",
        "设计一款无人机，最大起飞重量不大于260kg，航程500km，载荷20kg，"
        "巡航航时不低于1h。",
        client_action_id="start-endurance-outcome",
    )
    assert initial["diagnosis"]["status"] == "unsupported"
    scoped = workflow.defer_unsupported(
        "session-endurance-outcome",
        field_paths=["performance.min_cruise_endurance_s"],
        scope_statement="保留 1 h 巡航航时要求，先求解当前 Class I/II 覆盖范围。",
        expected_revision_hash=initial["revision_hash"],
        client_action_id="defer-endurance-outcome",
        user_confirmed=True,
    )
    confirmed = workflow.confirm_revision(
        "session-endurance-outcome",
        expected_revision_hash=scoped["revision_hash"],
        client_action_id="confirm-endurance-outcome",
        user_confirmed=True,
    )
    request_hash = _record_submission(
        workflow,
        "session-endurance-outcome",
        confirmed,
        "job-endurance-outcome",
    )

    feedback = workflow.ingest_solver_outcome(
        "session-endurance-outcome",
        revision_id=confirmed["revision_id"],
        expected_revision_hash=confirmed["revision_hash"],
        job_id="job-endurance-outcome",
        request_hash=request_hash,
        result={
            "status": "engineering_infeasible",
            "engineering": {
                "numerical_converged": True,
                "engineering_feasible": False,
                "blocking_failed_count": 2,
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
                    },
                    {
                        "id": "declared.min_cruise_endurance_s",
                        "label": "Minimum cruise endurance",
                        "direction": "minimum",
                        "required": 3_600.0,
                        "actual": 1_945.0,
                        "margin": -1_655.0,
                        "unit": "s",
                        "blocking": True,
                        "passed": False,
                    },
                ],
            },
        },
    )

    proposals = feedback["diagnosis"]["change_proposals"]
    assert [proposal["field_path"] for proposal in proposals] == ["weights.max_mtow_kg"]
    assert all("endurance" not in proposal["field_path"] for proposal in proposals)


def test_solver_outcome_requires_matching_server_owned_submission(tmp_path: Path) -> None:
    workflow = _workflow(tmp_path)
    ready = workflow.start(
        "session-untrusted-outcome",
        "设计一款无人机，航程500km，载荷20kg。",
        client_action_id="start-untrusted-outcome",
    )
    confirmed = workflow.confirm_revision(
        "session-untrusted-outcome",
        expected_revision_hash=ready["revision_hash"],
        client_action_id="confirm-untrusted-outcome",
        user_confirmed=True,
    )
    result = {
        "status": "nonconverged",
        "engineering": {
            "numerical_converged": False,
            "engineering_feasible": False,
            "blocking_failed_count": 0,
            "constraints": [],
        },
    }

    with pytest.raises(WorkflowStateError, match="server-owned submission"):
        workflow.ingest_solver_outcome(
            "session-untrusted-outcome",
            revision_id=confirmed["revision_id"],
            expected_revision_hash=confirmed["revision_hash"],
            job_id="job-untrusted-outcome",
            request_hash="a" * 64,
            result=result,
        )

    request_hash = _record_submission(
        workflow,
        "session-untrusted-outcome",
        confirmed,
        "job-untrusted-outcome",
    )
    assert request_hash != "b" * 64
    with pytest.raises(WorkflowStateError, match="server-owned submission"):
        workflow.ingest_solver_outcome(
            "session-untrusted-outcome",
            revision_id=confirmed["revision_id"],
            expected_revision_hash=confirmed["revision_hash"],
            job_id="job-untrusted-outcome",
            request_hash="b" * 64,
            result=result,
        )


def test_nonconverged_outcome_asks_for_bounded_design_variable_without_inventing_value(
    tmp_path: Path,
) -> None:
    workflow = _workflow(tmp_path)
    ready = workflow.start(
        "session-nonconverged",
        "设计一款无人机，航程500km，载荷20kg。",
        client_action_id="start-nonconverged",
    )
    confirmed = workflow.confirm_revision(
        "session-nonconverged",
        expected_revision_hash=ready["revision_hash"],
        client_action_id="confirm-nonconverged",
        user_confirmed=True,
    )
    request_hash = _record_submission(
        workflow, "session-nonconverged", confirmed, "job-nonconverged-001"
    )

    feedback = workflow.ingest_solver_outcome(
        "session-nonconverged",
        revision_id=confirmed["revision_id"],
        expected_revision_hash=confirmed["revision_hash"],
        job_id="job-nonconverged-001",
        request_hash=request_hash,
        result={
            "status": "nonconverged",
            "engineering": {
                "numerical_converged": False,
                "engineering_feasible": False,
                "blocking_failed_count": 1,
                "constraints": [
                    {
                        "id": "class1.weight_closure",
                        "label": "Weight closure",
                        "direction": "maximum",
                        "required": 0.001,
                        "actual": 0.02,
                        "margin": -0.019,
                        "unit": "relative_error",
                        "blocking": True,
                        "passed": False,
                    }
                ],
            },
        },
    )

    assert feedback["diagnosis"]["status"] == "needs_clarification"
    assert feedback["allowed_actions"] == ["answer_questions"]
    question = feedback["diagnosis"]["clarification_questions"][0]
    assert question["field_path"] == "initial_guess.mtow_kg"
    assert question["options"] == []
    assert question["recommended_option"] is None


def test_nonconverged_outcome_never_relaxes_a_hard_requirement(tmp_path: Path) -> None:
    workflow = _workflow(tmp_path)
    ready = workflow.start(
        "session-nonconverged-hard-limit",
        "设计一款无人机，最大起飞重量不大于260kg，航程500km，载荷20kg。",
        client_action_id="start-nonconverged-hard-limit",
    )
    confirmed = workflow.confirm_revision(
        "session-nonconverged-hard-limit",
        expected_revision_hash=ready["revision_hash"],
        client_action_id="confirm-nonconverged-hard-limit",
        user_confirmed=True,
    )
    request_hash = _record_submission(
        workflow,
        "session-nonconverged-hard-limit",
        confirmed,
        "job-nonconverged-hard-limit",
    )

    feedback = workflow.ingest_solver_outcome(
        "session-nonconverged-hard-limit",
        revision_id=confirmed["revision_id"],
        expected_revision_hash=confirmed["revision_hash"],
        job_id="job-nonconverged-hard-limit",
        request_hash=request_hash,
        result={
            "status": "nonconverged",
            "engineering": {
                "numerical_converged": False,
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
    )

    assert feedback["diagnosis"]["status"] == "needs_clarification"
    assert feedback["diagnosis"]["change_proposals"] == []
    assert feedback["diagnosis"]["clarification_questions"][0]["field_path"] == (
        "initial_guess.mtow_kg"
    )
    assert "did not converge" in feedback["diagnosis"]["summary"]
    assert "infeasible" not in feedback["diagnosis"]["summary"].lower()


def test_nonconverged_outcome_without_constraint_evidence_is_not_infeasible(
    tmp_path: Path,
) -> None:
    workflow = _workflow(tmp_path)
    ready = workflow.start(
        "session-nonconverged-no-evidence",
        "设计一款无人机，航程500km，载荷20kg。",
        client_action_id="start-nonconverged-no-evidence",
    )
    confirmed = workflow.confirm_revision(
        "session-nonconverged-no-evidence",
        expected_revision_hash=ready["revision_hash"],
        client_action_id="confirm-nonconverged-no-evidence",
        user_confirmed=True,
    )
    request_hash = _record_submission(
        workflow,
        "session-nonconverged-no-evidence",
        confirmed,
        "job-nonconverged-no-evidence",
    )

    feedback = workflow.ingest_solver_outcome(
        "session-nonconverged-no-evidence",
        revision_id=confirmed["revision_id"],
        expected_revision_hash=confirmed["revision_hash"],
        job_id="job-nonconverged-no-evidence",
        request_hash=request_hash,
        result={
            "status": "nonconverged",
            "engineering": {
                "numerical_converged": False,
                "engineering_feasible": False,
                "blocking_failed_count": 0,
                "constraints": [],
            },
        },
    )

    assert feedback["diagnosis"]["status"] == "needs_clarification"
    assert feedback["diagnosis"]["change_proposals"] == []
    assert feedback["allowed_actions"] == ["answer_questions"]


def test_inconsistent_infeasible_result_does_not_create_a_revision(tmp_path: Path) -> None:
    workflow = _workflow(tmp_path)
    ready = workflow.start(
        "session-inconsistent-infeasible",
        "设计一款无人机，航程500km，载荷20kg。",
        client_action_id="start-inconsistent-infeasible",
    )
    confirmed = workflow.confirm_revision(
        "session-inconsistent-infeasible",
        expected_revision_hash=ready["revision_hash"],
        client_action_id="confirm-inconsistent-infeasible",
        user_confirmed=True,
    )
    request_hash = _record_submission(
        workflow,
        "session-inconsistent-infeasible",
        confirmed,
        "job-inconsistent-infeasible",
    )

    unchanged = workflow.ingest_solver_outcome(
        "session-inconsistent-infeasible",
        revision_id=confirmed["revision_id"],
        expected_revision_hash=confirmed["revision_hash"],
        job_id="job-inconsistent-infeasible",
        request_hash=request_hash,
        result={
            "status": "engineering_infeasible",
            "engineering": {
                "numerical_converged": False,
                "engineering_feasible": False,
                "blocking_failed_count": 1,
                "constraints": [],
            },
        },
    )

    assert unchanged["revision_id"] == confirmed["revision_id"]
    assert unchanged["confirmed"] is True


def test_successful_solver_outcome_does_not_create_an_extra_revision(tmp_path: Path) -> None:
    workflow = _workflow(tmp_path)
    ready = workflow.start(
        "session-feasible",
        "设计一款无人机，航程500km，载荷20kg。",
        client_action_id="start-feasible",
    )
    confirmed = workflow.confirm_revision(
        "session-feasible",
        expected_revision_hash=ready["revision_hash"],
        client_action_id="confirm-feasible",
        user_confirmed=True,
    )
    request_hash = _record_submission(
        workflow, "session-feasible", confirmed, "job-feasible-001"
    )

    unchanged = workflow.ingest_solver_outcome(
        "session-feasible",
        revision_id=confirmed["revision_id"],
        expected_revision_hash=confirmed["revision_hash"],
        job_id="job-feasible-001",
        request_hash=request_hash,
        result={
            "status": "completed",
            "engineering": {
                "numerical_converged": True,
                "engineering_feasible": True,
                "blocking_failed_count": 0,
                "constraints": [],
            },
        },
    )

    assert unchanged["revision_id"] == confirmed["revision_id"]
    assert unchanged["confirmed"] is True


def test_natural_language_change_preserves_baseline_until_each_diff_is_confirmed(
    tmp_path: Path,
) -> None:
    workflow = _workflow(tmp_path)
    ready = workflow.start(
        "session-text-change",
        "设计一款无人机，航程500km，载荷20kg。",
        client_action_id="start-text-change",
    )
    confirmed = workflow.confirm_revision(
        "session-text-change",
        expected_revision_hash=ready["revision_hash"],
        client_action_id="confirm-text-change",
        user_confirmed=True,
    )

    proposed = workflow.propose_text_changes(
        "session-text-change",
        "把航程改为400km，载荷改为15kg",
        expected_revision_hash=confirmed["revision_hash"],
        client_action_id="text-change-001",
    )

    assert proposed["confirmed"] is False
    assert proposed["diagnosis"]["status"] == "repairable"
    assert len(proposed["diagnosis"]["change_proposals"]) == 2
    unchanged_fields = {
        item["path"]: item["value"] for item in proposed["intent"]["requirements"]
    }
    assert unchanged_fields["requirements.range_m"] == 500_000.0
    assert unchanged_fields["requirements.payload_kg"] == 20.0

    range_proposal = next(
        item
        for item in proposed["diagnosis"]["change_proposals"]
        if item["field_path"] == "requirements.range_m"
    )
    first_applied = workflow.apply_change(
        "session-text-change",
        proposal_id=range_proposal["proposal_id"],
        expected_revision_hash=proposed["revision_hash"],
        client_action_id="apply-text-range",
        user_confirmed=True,
    )
    assert first_applied["diagnosis"]["status"] == "repairable"
    assert len(first_applied["diagnosis"]["change_proposals"]) == 1
    remaining = first_applied["diagnosis"]["change_proposals"][0]
    assert remaining["field_path"] == "requirements.payload_kg"
    assert remaining["source_revision"] == first_applied["intent"]["revision"]

    final = workflow.apply_change(
        "session-text-change",
        proposal_id=remaining["proposal_id"],
        expected_revision_hash=first_applied["revision_hash"],
        client_action_id="apply-text-payload",
        user_confirmed=True,
    )
    final_fields = {
        item["path"]: item["value"] for item in final["intent"]["requirements"]
    }
    assert final_fields["requirements.range_m"] == 400_000.0
    assert final_fields["requirements.payload_kg"] == 15.0
    assert final["diagnosis"]["status"] == "ready_for_solver"
    assert final["confirmed"] is False


def test_requirement_change_recomputes_dependent_solver_defaults(tmp_path: Path) -> None:
    workflow = _workflow(tmp_path)
    original = workflow.start(
        "session-recompute-defaults",
        "设计一款固定翼货运无人机，航程600km，载荷120kg，采用螺旋桨推进，"
        "巡航马赫数0.30，巡航高度5000m，实用升限8000m。",
        client_action_id="start-recompute-defaults",
    )
    original_fields = {
        item["path"]: item for item in original["intent"]["requirements"]
    }
    assert original_fields["initial_guess.mtow_kg"]["value"] == 600.0
    assert original["defaults_materialized"] is True

    proposed = workflow.propose_text_changes(
        "session-recompute-defaults",
        "把载荷改为150kg",
        expected_revision_hash=original["revision_hash"],
        client_action_id="propose-payload-recompute",
    )
    proposal = proposed["diagnosis"]["change_proposals"][0]
    updated = workflow.apply_change(
        "session-recompute-defaults",
        proposal_id=proposal["proposal_id"],
        expected_revision_hash=proposed["revision_hash"],
        client_action_id="apply-payload-recompute",
        user_confirmed=True,
    )

    fields = {item["path"]: item for item in updated["intent"]["requirements"]}
    assert fields["requirements.payload_kg"]["value"] == 150.0
    assert fields["requirements.payload_kg"]["source"] == "user"
    assert fields["initial_guess.mtow_kg"]["value"] == 750.0
    assert fields["initial_guess.mtow_kg"]["source"] == "derived"
    assert fields["requirements.range_m"]["value"] == 600_000.0
    completion = updated["intent"]["metadata"]["solver_completion"]
    assert completion["source_revision"] == updated["intent"]["revision"] - 1
    assert completion["valid_for_revision"] == updated["intent"]["revision"]
    assert updated["defaults_materialized"] is True
    assert updated["confirmed"] is False


def test_natural_language_change_cannot_silently_add_a_new_baseline_field(
    tmp_path: Path,
) -> None:
    workflow = _workflow(tmp_path)
    current = workflow.start(
        "session-text-add",
        "设计一款无人机，航程500km，载荷20kg。",
        client_action_id="start-text-add",
    )

    with pytest.raises(WorkflowStateError):
        # The current helper may materialize this field as a default. Use a
        # special mission field that is absent from this baseline instead.
        workflow.project_solver_request(
            "session-text-add", expected_revision_hash=current["revision_hash"]
        )
    with pytest.raises(WorkflowActionError, match="only patch fields already present"):
        workflow.propose_text_changes(
            "session-text-add",
            "把最大飞行马赫数改为0.8",
            expected_revision_hash=current["revision_hash"],
            client_action_id="text-add-rejected",
        )
    assert workflow.current("session-text-add")["revision_id"] == current["revision_id"]
