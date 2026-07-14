"""Focused regressions for aircraft-design request negotiation boundaries."""

from __future__ import annotations

from pathlib import Path

import pytest

from src.design_intake.models import DesignIntentStatus, ModelCoverageStatus
from src.design_intake.parser import looks_like_design_request, parse_design_intent
from src.design_intake.preflight import diagnose_design_intent
from src.design_intake.store import DesignRevisionStore
from src.design_intake.workflow import (
    DesignRequirementWorkflow,
    WorkflowActionError,
)


def test_design_request_detector_accepts_fixed_wing_request_without_parameters() -> None:
    assert looks_like_design_request("设计一架固定翼无人机") is True


@pytest.mark.parametrize(
    "question",
    [
        "请解释固定翼无人机总体设计原理",
        "如何优化无人机总体设计技能？",
        "为什么飞机设计结果经常不可行？",
    ],
)
def test_design_request_detector_does_not_capture_explanatory_questions(
    question: str,
) -> None:
    assert looks_like_design_request(question) is False


def test_bounded_answer_rejects_disagreement_between_option_and_value(
    tmp_path: Path,
) -> None:
    workflow = DesignRequirementWorkflow(
        DesignRevisionStore(tmp_path / "requirements")
    )
    initial = workflow.start(
        "session-001",
        "设计一架固定翼无人机，航程500km，载荷20kg，巡航马赫数0.6。",
        client_action_id="start-001",
    )
    questions = {
        item["question_id"]: item
        for item in initial["diagnosis"]["clarification_questions"]
    }
    assert questions["propulsion.type.high_speed"]["options"] == ["jet", "prop"]

    with pytest.raises(WorkflowActionError, match="cannot disagree"):
        workflow.answer_questions(
            "session-001",
            answers=[
                {
                    "question_id": "propulsion.type.high_speed",
                    "option": "jet",
                    "value": "prop",
                }
            ],
            expected_revision_hash=initial["revision_hash"],
            client_action_id="answer-mismatch-001",
        )

    current = workflow.current("session-001")
    assert current["revision_id"] == initial["revision_id"]
    assert current["revision_hash"] == initial["revision_hash"]


def test_cruise_mach_above_registered_envelope_is_unsupported_model_gap() -> None:
    intent = parse_design_intent(
        "设计一架固定翼无人机，航程500km，载荷20kg，采用喷气推进，"
        "巡航马赫数0.9。"
    )

    diagnosis = diagnose_design_intent(intent)
    cruise_coverage = next(
        item
        for item in diagnosis.coverage
        if item.field_path == "requirements.cruise_mach"
    )

    assert diagnosis.status is DesignIntentStatus.UNSUPPORTED
    assert diagnosis.status is not DesignIntentStatus.INFEASIBLE
    assert diagnosis.ready_for_solver is False
    assert cruise_coverage.status is ModelCoverageStatus.UNSUPPORTED
    assert cruise_coverage.blocking is True
    assert cruise_coverage.applicable_envelope == {
        "minimum": 0.03,
        "maximum": 0.85,
    }
    assert "model-applicability gap" in cruise_coverage.reason
    assert "not a physical infeasibility" in diagnosis.summary
