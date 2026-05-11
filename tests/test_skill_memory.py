from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock

from src.providers.base import ChatResponse
from src.skill_memory import (
    TraceRecorder,
    approve_candidate,
    list_candidates,
    process_trace_to_candidate,
    reject_candidate,
)
from src.skills.loader import get_all_skills


class TestSkillMemory(unittest.TestCase):
    def test_trace_with_existing_skill_is_skipped(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            recorder = TraceRecorder(
                workspace_root=root,
                session_id="s1",
                task="Use an existing skill",
                provider_name="glm",
                model="glm-4.5",
            )
            event = Mock(kind="tool_use", tool_name="Skill", tool_input={"skill": "x"}, tool_output=None)
            recorder.record_event(event)
            trace_path = recorder.finish(status="completed", final_response="done")

            provider = Mock()
            status = process_trace_to_candidate(
                trace_path=trace_path,
                provider=provider,
                model="glm-4.5",
                workspace_root=root,
            )

            self.assertEqual(status["status"], "skipped_existing_skill")
            provider.chat.assert_not_called()
            self.assertEqual(list_candidates(root), [])

    def test_explicit_learn_trace_creates_candidate_and_approve_loads_skill(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            recorder = TraceRecorder(
                workspace_root=root,
                session_id="s1",
                task="Debug a recurring provider bug",
                provider_name="deepseek",
                model="deepseek-v4-flash",
            )
            trace_path = recorder.finish(status="completed", final_response="fixed")

            provider = Mock()
            provider.chat.return_value = ChatResponse(
                content=json.dumps({
                    "skill_name": "debug-provider-bug",
                    "description": "Debug provider API errors",
                    "when_to_use": "Use when provider chat calls fail after tool use.",
                    "body": "Inspect provider responses and preserve required metadata.",
                    "reason": "Reusable provider debugging workflow.",
                    "confidence": 0.9,
                }),
                model="deepseek-v4-flash",
                usage={},
                finish_reason="stop",
            )

            metadata = process_trace_to_candidate(
                trace_path=trace_path,
                provider=provider,
                model="deepseek-v4-flash",
                workspace_root=root,
            )

            self.assertEqual(metadata["status"], "pending")
            self.assertEqual(metadata["generation_mode"], "explicit_learn")
            self.assertEqual(len(list_candidates(root)), 1)
            skills_before = get_all_skills(project_root=root)
            self.assertNotIn("debug-provider-bug", [s.name for s in skills_before])

            approved = approve_candidate(root, metadata["id"])
            self.assertEqual(approved["status"], "approved")
            skills_after = get_all_skills(project_root=root)
            self.assertIn("debug-provider-bug", [s.name for s in skills_after])

    def test_reject_candidate_marks_metadata(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            candidate = root / ".clawd" / "skill-candidates" / "c1"
            candidate.mkdir(parents=True)
            (candidate / "SKILL.md").write_text("---\ndescription: test\n---\nbody\n", encoding="utf-8")
            (candidate / "metadata.json").write_text(
                json.dumps({"id": "c1", "status": "pending", "skill_name": "test"}),
                encoding="utf-8",
            )

            metadata = reject_candidate(root, "c1")
            self.assertEqual(metadata["status"], "rejected")

    def test_explicit_learn_does_not_require_value_field(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            recorder = TraceRecorder(
                workspace_root=root,
                session_id="s1",
                task="Summarize a tiny workflow",
                provider_name="glm",
                model="glm-4.5",
            )
            trace_path = recorder.finish(status="completed", final_response="workflow")

            provider = Mock()
            provider.chat.return_value = ChatResponse(
                content=json.dumps({
                    "skill_name": "tiny-workflow",
                    "description": "A tiny learned workflow",
                    "when_to_use": "Use for tiny workflow tasks.",
                    "body": "Follow the tiny workflow.",
                    "reason": "Explicit /learn requested extraction.",
                    "confidence": 0.5,
                }),
                model="glm-4.5",
                usage={},
                finish_reason="stop",
            )

            metadata = process_trace_to_candidate(
                trace_path=trace_path,
                provider=provider,
                model="glm-4.5",
                workspace_root=root,
            )

            self.assertEqual(metadata["status"], "pending")
            self.assertEqual(metadata["skill_name"], "tiny-workflow")

    def test_gitignore_ignores_trace_and_candidates_only(self):
        gitignore = Path(__file__).resolve().parents[1] / ".gitignore"
        content = gitignore.read_text(encoding="utf-8")
        self.assertIn(".clawd/traces/", content)
        self.assertIn(".clawd/skill-candidates/", content)
        self.assertNotIn(".clawd/skills/", content)
