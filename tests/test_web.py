"""Tests for the browser UI service."""

from __future__ import annotations

import json
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch

from src.config import _encode_api_key
from src.providers.base import BaseProvider, ChatResponse
from src.tool_system.agent_loop import ToolEvent
from src.tool_system.defaults import build_default_registry
from src.tool_system.registry import ToolRegistry
from src.web import ClawdWebService


class FakeProvider(BaseProvider):
    """Minimal provider for exercising the browser service."""

    def chat(self, messages, tools=None, **kwargs) -> ChatResponse:
        last_message = messages[-1]
        if isinstance(last_message, dict):
            content = str(last_message.get("content", ""))
        else:
            content = str(getattr(last_message, "content", ""))
        model = self._get_model(**kwargs) or "fake-model"
        return ChatResponse(
            content=f"Echo: {content}",
            model=model,
            usage={"input_tokens": 3, "output_tokens": 5},
            finish_reason="stop",
        )

    def chat_stream(self, messages, tools=None, **kwargs):
        yield "unused"

    def get_available_models(self) -> list[str]:
        return [self.model or "fake-model"]


class TestBrowserRegistry(unittest.TestCase):
    """Tool registration behavior for the browser mode."""

    def test_web_registry_excludes_questionnaire_tool(self):
        registry = build_default_registry(enable_ask_user_question=False)
        tool_names = {spec.name for spec in registry.list_specs()}
        self.assertNotIn("AskUserQuestion", tool_names)
        self.assertIn("Read", tool_names)


class TestClawdWebService(unittest.TestCase):
    """Core browser service behavior."""

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.home = Path(self.temp_dir.name)
        config_dir = self.home / ".clawd"
        config_dir.mkdir(parents=True, exist_ok=True)
        config = {
            "default_provider": "openai",
            "providers": {
                "openai": {
                    "api_key": _encode_api_key("test-key"),
                    "base_url": "https://example.com/v1",
                    "default_model": "qwen3-4b",
                },
                "anthropic": {
                    "api_key": "",
                    "base_url": "https://api.anthropic.com",
                    "default_model": "claude-sonnet-4-6",
                },
                "glm": {
                    "api_key": "",
                    "base_url": "https://open.bigmodel.cn/api/paas/v4",
                    "default_model": "zai/glm-5",
                },
                "minimax": {
                    "api_key": "",
                    "base_url": "https://api.minimaxi.com/anthropic",
                    "default_model": "MiniMax-M2.7",
                },
            },
            "session": {"auto_save": True, "max_history": 100},
        }
        (config_dir / "config.json").write_text(json.dumps(config), encoding="utf-8")
        self.home_patcher = patch("pathlib.Path.home", return_value=self.home)
        self.home_patcher.start()

    def tearDown(self) -> None:
        self.home_patcher.stop()
        self.temp_dir.cleanup()

    @patch("src.agent.session.Path.home")
    @patch("src.web.app.build_default_registry", side_effect=lambda **_kwargs: ToolRegistry())
    @patch("src.web.app.get_provider_class", return_value=FakeProvider)
    def test_create_session_and_send_message(
        self,
        _mock_provider_class,
        _mock_build_registry,
        mock_session_home,
    ) -> None:
        mock_session_home.return_value = self.home
        with patch("src.config.Path.home", return_value=self.home):
            service = ClawdWebService(workspace_root=self.home / "workspace")
            created = service.create_session(provider_name="openai", model="qwen3-4b")
            session = created["session"]

            self.assertEqual(session["provider"], "openai")
            self.assertEqual(session["model"], "deepseek-v4-pro")
            self.assertEqual(session["messages"], [])

            reply = service.send_message(session["session_id"], "Hello from the browser")

            self.assertEqual(reply["reply"]["text"], "Echo: Hello from the browser")
            self.assertEqual(reply["reply"]["usage"]["input_tokens"], 3)
            self.assertEqual(len(reply["session"]["messages"]), 2)
            self.assertEqual(reply["session"]["messages"][0]["role"], "user")
            self.assertEqual(reply["session"]["messages"][1]["role"], "assistant")

    @patch("src.agent.session.Path.home")
    @patch("src.web.app.build_default_registry", side_effect=lambda **_kwargs: ToolRegistry())
    @patch("src.web.app.get_provider_class", return_value=FakeProvider)
    def test_auto_skill_is_exposed_and_injected(
        self,
        _mock_provider_class,
        _mock_build_registry,
        mock_session_home,
    ) -> None:
        mock_session_home.return_value = self.home
        workspace = self.home / "workspace"
        skill_dir = workspace / ".clawd" / "skills" / "aircraft-design-rag"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            "---\nname: aircraft-design-rag\ndescription: RAG test skill\n---\nUse local RAG.",
            encoding="utf-8",
        )

        with patch("src.config.Path.home", return_value=self.home):
            service = ClawdWebService(workspace_root=workspace)
            payload = service.get_bootstrap_payload()
            created = service.create_session(
                provider_name="openai",
                model="qwen3-4b",
                auto_skill="aircraft-design",
            )
            reply = service.send_message(created["session"]["session_id"], "What is RD-170?")

        self.assertEqual(payload["default_auto_skill"], None)
        self.assertEqual(payload["skills"][0]["name"], "aircraft-design")
        self.assertEqual(payload["skills"][0]["display_name"], "飞行器设计")
        self.assertEqual(created["session"]["auto_skill"], "aircraft-design")
        self.assertIn("飞行器设计", reply["reply"]["text"])
        self.assertNotIn("aircraft-design-rag", reply["reply"]["text"])

    def test_bootstrap_payload_marks_configured_providers(self) -> None:
        with patch("src.config.Path.home", return_value=self.home):
            service = ClawdWebService(workspace_root=self.home / "workspace")
            payload = service.get_bootstrap_payload()

        providers = {provider["name"]: provider for provider in payload["providers"]}
        self.assertEqual(payload["default_provider"], "openai")
        self.assertTrue(providers["openai"]["configured"])
        self.assertFalse(providers["anthropic"]["configured"])
        self.assertIn("skills", payload)
        self.assertNotIn("rag", payload)

    @patch("src.agent.session.Path.home")
    @patch("src.web.app.build_default_registry", side_effect=lambda **_kwargs: ToolRegistry())
    @patch("src.web.app.get_provider_class", return_value=FakeProvider)
    def test_rag_settings_are_internal_and_sessions_are_listed(
        self,
        _mock_provider_class,
        _mock_build_registry,
        mock_session_home,
    ) -> None:
        mock_session_home.return_value = self.home
        with patch("src.config.Path.home", return_value=self.home):
            service = ClawdWebService(workspace_root=self.home / "workspace")
            created = service.create_session(
                provider_name="openai",
                model="qwen3-4b",
                rag_settings={
                    "top_k": 3,
                    "max_snippet_chars": 160,
                    "candidate_limit": 600,
                    "use_cache": False,
                    "auto_retrieve": False,
                },
            )
            listed = service.list_sessions_payload()

        self.assertNotIn("rag_settings", created["session"])
        self.assertEqual(len(listed["sessions"]), 1)
        self.assertEqual(listed["sessions"][0]["session_id"], created["session"]["session_id"])

    @patch("src.web.app.build_default_registry", side_effect=lambda **_kwargs: ToolRegistry())
    @patch("src.web.app.get_provider_class", return_value=FakeProvider)
    def test_persisted_sessions_are_loaded_after_service_restart(
        self,
        _mock_provider_class,
        _mock_build_registry,
    ) -> None:
        workspace = self.home / "workspace"
        service = ClawdWebService(workspace_root=workspace)
        created = service.create_session(provider_name="openai", model="qwen3-4b")
        session_id = created["session"]["session_id"]

        service.send_message(session_id, "Keep this after restart")

        session_file = self.home / ".clawd" / "sessions" / f"{session_id}.json"
        self.assertTrue(session_file.exists())

        restarted = ClawdWebService(workspace_root=workspace)
        listed = restarted.list_sessions_payload()
        loaded = restarted.get_session_payload(session_id)

        self.assertEqual([item["session_id"] for item in listed["sessions"]], [session_id])
        self.assertEqual(loaded["session"]["messages"][0]["text"], "Keep this after restart")
        self.assertEqual(loaded["session"]["messages"][1]["text"], "Echo: Keep this after restart")

    @patch("src.web.app.build_default_registry", side_effect=lambda **_kwargs: ToolRegistry())
    @patch("src.web.app.get_provider_class", return_value=FakeProvider)
    def test_listing_sessions_does_not_wait_for_busy_session_lock(
        self,
        _mock_provider_class,
        _mock_build_registry,
    ) -> None:
        service = ClawdWebService(workspace_root=self.home / "workspace")
        created = service.create_session(provider_name="openai", model="qwen3-4b")
        session_id = created["session"]["session_id"]
        state = service._require_session(session_id)
        locked = threading.Event()
        release = threading.Event()

        def hold_lock() -> None:
            with state.lock:
                locked.set()
                release.wait(timeout=5)

        worker = threading.Thread(target=hold_lock)
        worker.start()
        self.assertTrue(locked.wait(timeout=1))
        try:
            listed = service.list_sessions_payload()
        finally:
            release.set()
            worker.join(timeout=1)

        self.assertEqual(len(listed["sessions"]), 1)
        self.assertEqual(listed["sessions"][0]["session_id"], session_id)

    @patch("src.web.app.build_default_registry", side_effect=lambda **_kwargs: ToolRegistry())
    @patch("src.web.app.get_provider_class", return_value=FakeProvider)
    def test_delete_session_removes_memory_and_disk_records(
        self,
        _mock_provider_class,
        _mock_build_registry,
    ) -> None:
        service = ClawdWebService(workspace_root=self.home / "workspace")
        created = service.create_session(provider_name="openai", model="qwen3-4b")
        session_id = created["session"]["session_id"]
        session_file = self.home / ".clawd" / "sessions" / f"{session_id}.json"

        self.assertTrue(session_file.exists())

        deleted = service.delete_session(session_id)

        self.assertEqual(deleted, {"deleted": True, "session_id": session_id})
        self.assertFalse(session_file.exists())
        self.assertEqual(service.list_sessions_payload()["sessions"], [])
        with self.assertRaises(KeyError):
            service.get_session_payload(session_id)

    @patch("src.web.app.build_default_registry", side_effect=lambda **_kwargs: ToolRegistry())
    @patch("src.web.app.get_provider_class", return_value=FakeProvider)
    def test_delete_session_rejects_busy_session(
        self,
        _mock_provider_class,
        _mock_build_registry,
    ) -> None:
        service = ClawdWebService(workspace_root=self.home / "workspace")
        created = service.create_session(provider_name="openai", model="qwen3-4b")
        session_id = created["session"]["session_id"]
        state = service._require_session(session_id)
        locked = threading.Event()
        release = threading.Event()

        def hold_lock() -> None:
            with state.lock:
                locked.set()
                release.wait(timeout=5)

        worker = threading.Thread(target=hold_lock)
        worker.start()
        self.assertTrue(locked.wait(timeout=1))
        try:
            with self.assertRaises(ValueError):
                service.delete_session(session_id)
        finally:
            release.set()
            worker.join(timeout=1)

    def test_rag_settings_validation_rejects_out_of_range_values(self) -> None:
        service = ClawdWebService(workspace_root=self.home / "workspace")
        with self.assertRaises(ValueError):
            service._normalize_rag_settings({"top_k": 0})
        with self.assertRaises(ValueError):
            service._normalize_rag_settings({"max_snippet_chars": 40})
        with self.assertRaises(ValueError):
            service._normalize_rag_settings({"use_cache": "yes"})
        with self.assertRaises(ValueError):
            service._normalize_rag_settings({"candidate_limit": 20})

    @patch("src.agent.session.Path.home")
    @patch("src.web.app.build_default_registry", side_effect=lambda **_kwargs: ToolRegistry())
    @patch("src.web.app.get_provider_class", return_value=FakeProvider)
    def test_streaming_send_message_emits_text_chunks(
        self,
        _mock_provider_class,
        _mock_build_registry,
        mock_session_home,
    ) -> None:
        mock_session_home.return_value = self.home
        chunks: list[str] = []
        with patch("src.config.Path.home", return_value=self.home):
            service = ClawdWebService(workspace_root=self.home / "workspace")
            created = service.create_session(provider_name="openai", model="qwen3-4b")
            reply = service.send_message(
                created["session"]["session_id"],
                "Hello streamed browser",
                stream=True,
                on_text_chunk=chunks.append,
            )

        self.assertEqual(reply["reply"]["text"], "Echo: Hello streamed browser")
        self.assertEqual("".join(chunks), "Echo: Hello streamed browser")

    @patch("src.web.app.RagIndexService.search")
    def test_search_rag_uses_in_process_rag_service_with_settings(self, mock_search) -> None:
        workspace = self.home / "workspace"
        skill_dir = workspace / ".clawd" / "skills" / "aircraft-design-rag"
        script_dir = skill_dir / "scripts"
        script_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            "---\nname: aircraft-design-rag\ndescription: RAG test skill\n---\nUse local RAG.",
            encoding="utf-8",
        )
        (script_dir / "search_rag.py").write_text("print('{}')", encoding="utf-8")
        (workspace / "RAG-data").mkdir(parents=True)
        rag_payload = {
            "query": "RD-170",
            "markdown_files_scanned": 1,
            "chunks_indexed": 1,
            "cache": {"enabled": False, "hit": False, "path": None},
            "hits": [],
        }
        mock_search.return_value = rag_payload

        service = ClawdWebService(workspace_root=workspace)
        result = service.search_rag(
            "RD-170",
            rag_settings={
                "top_k": 2,
                "max_snippet_chars": 120,
                "candidate_limit": 500,
                "use_cache": False,
                "auto_retrieve": True,
            },
        )

        called_query, called_settings = mock_search.call_args.args
        self.assertEqual(result["rag"]["query"], "RD-170")
        self.assertEqual(called_query, "RD-170")
        self.assertEqual(called_settings.top_k, 2)
        self.assertEqual(called_settings.max_snippet_chars, 120)
        self.assertEqual(called_settings.candidate_limit, 500)
        self.assertFalse(called_settings.use_cache)

    @patch("src.web.app.RagIndexService.rebuild")
    @patch("src.web.app.RagIndexService.status")
    def test_rag_status_and_rebuild_use_in_process_service(self, mock_status, mock_rebuild) -> None:
        workspace = self.home / "workspace"
        skill_dir = workspace / ".clawd" / "skills" / "aircraft-design-rag"
        script_dir = skill_dir / "scripts"
        script_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            "---\nname: aircraft-design-rag\ndescription: RAG test skill\n---\nUse local RAG.",
            encoding="utf-8",
        )
        (script_dir / "search_rag.py").write_text("print('{}')", encoding="utf-8")
        (workspace / "RAG-data").mkdir(parents=True)
        mock_status.return_value = {"cache_ready": True, "cache": {"chunk_count": 1}}
        mock_rebuild.return_value = {"rebuild": {"running": True}}

        service = ClawdWebService(workspace_root=workspace)
        status = service.rag_status()
        rebuild = service.rebuild_rag(
            rag_settings={"candidate_limit": 500},
            force=False,
        )

        self.assertTrue(status["rag"]["cache_ready"])
        self.assertTrue(rebuild["rag"]["rebuild"]["running"])
        called_settings = mock_rebuild.call_args.args[0]
        self.assertEqual(called_settings.candidate_limit, 500)
        self.assertFalse(mock_rebuild.call_args.kwargs["force"])

    @patch("src.agent.session.Path.home")
    @patch("src.web.app.RagIndexService.search")
    @patch("src.web.app.RagIndexService.cache_ready", return_value=True)
    @patch("src.web.app.build_default_registry", side_effect=lambda **_kwargs: ToolRegistry())
    @patch("src.web.app.get_provider_class", return_value=FakeProvider)
    def test_auto_rag_preflight_attaches_evidence_event(
        self,
        _mock_provider_class,
        _mock_build_registry,
        _mock_cache_ready,
        mock_search,
        mock_session_home,
    ) -> None:
        mock_session_home.return_value = self.home
        workspace = self.home / "workspace"
        skill_dir = workspace / ".clawd" / "skills" / "aircraft-design-rag"
        script_dir = skill_dir / "scripts"
        script_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            "---\nname: aircraft-design-rag\ndescription: RAG test skill\n---\nUse local RAG.",
            encoding="utf-8",
        )
        (script_dir / "search_rag.py").write_text("print('{}')", encoding="utf-8")
        (workspace / "RAG-data").mkdir(parents=True)
        rag_payload = {
            "query": "RD-170",
            "markdown_files_scanned": 1,
            "chunks_indexed": 1,
            "cache": {"enabled": True, "hit": True, "path": "cache.json"},
            "hits": [
                {
                    "rank": 1,
                    "score": 7.5,
                    "file": "RAG-data/engine.md",
                    "start_line": 2,
                    "end_line": 8,
                    "heading": "RD-170",
                    "snippet": "RD-170 is a staged-combustion engine.",
                }
            ],
        }
        mock_search.return_value = rag_payload

        with patch("src.config.Path.home", return_value=self.home):
            service = ClawdWebService(workspace_root=workspace)
            created = service.create_session(
                provider_name="openai",
                model="qwen3-4b",
                auto_skill="aircraft-design",
            )
            reply = service.send_message(created["session"]["session_id"], "What is RD-170?")

        events = reply["reply"]["events"]
        self.assertEqual(events[0]["kind"], "rag_retrieval")
        self.assertEqual(events[0]["tool_name"], "aircraft-design")
        self.assertEqual(events[0]["rag"]["hits"][0]["file"], "RAG-data/engine.md")
        self.assertIn("Browser-attached local aircraft-design evidence", reply["reply"]["text"])
        self.assertEqual(reply["session"]["auto_skill"], "aircraft-design")
        self.assertEqual(reply["session"]["messages"][1]["events"][0]["kind"], "rag_retrieval")
        self.assertEqual(reply["session"]["messages"][1]["events"][0]["rag"]["hits"][0]["file"], "RAG-data/engine.md")

        restarted = ClawdWebService(workspace_root=workspace)
        restored = restarted.get_session_payload(created["session"]["session_id"])
        self.assertEqual(restored["session"]["messages"][1]["events"][0]["rag"]["hits"][0]["file"], "RAG-data/engine.md")

    @patch("src.agent.session.Path.home")
    @patch("src.web.app.RagIndexService.search")
    @patch("src.web.app.RagIndexService.not_ready_payload")
    @patch("src.web.app.RagIndexService.rebuild")
    @patch("src.web.app.RagIndexService.cache_ready", return_value=False)
    @patch("src.web.app.build_default_registry", side_effect=lambda **_kwargs: ToolRegistry())
    @patch("src.web.app.get_provider_class", return_value=FakeProvider)
    def test_auto_rag_preflight_starts_background_rebuild_when_cache_is_cold(
        self,
        _mock_provider_class,
        _mock_build_registry,
        _mock_cache_ready,
        mock_rebuild,
        mock_not_ready_payload,
        mock_search,
        mock_session_home,
    ) -> None:
        mock_session_home.return_value = self.home
        workspace = self.home / "workspace"
        skill_dir = workspace / ".clawd" / "skills" / "aircraft-design-rag"
        script_dir = skill_dir / "scripts"
        script_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            "---\nname: aircraft-design-rag\ndescription: RAG test skill\n---\nUse local RAG.",
            encoding="utf-8",
        )
        (script_dir / "search_rag.py").write_text("print('{}')", encoding="utf-8")
        (workspace / "RAG-data").mkdir(parents=True)
        mock_not_ready_payload.return_value = {
            "query": "What is RD-170?",
            "markdown_files_scanned": 1,
            "chunks_indexed": 0,
            "candidate_chunks": 0,
            "cache": {"enabled": True, "ready": False, "build_in_progress": True},
            "message": "RAG index is building in the background.",
            "hits": [],
        }

        with patch("src.config.Path.home", return_value=self.home):
            service = ClawdWebService(workspace_root=workspace)
            created = service.create_session(
                provider_name="openai",
                model="qwen3-4b",
                auto_skill="aircraft-design",
            )
            reply = service.send_message(created["session"]["session_id"], "What is RD-170?")

        events = reply["reply"]["events"]
        self.assertEqual(events[0]["kind"], "rag_retrieval")
        self.assertEqual(events[0]["tool_name"], "aircraft-design")
        self.assertTrue(events[0]["rag"]["cache"]["build_in_progress"])
        self.assertEqual(reply["session"]["auto_skill"], "aircraft-design")
        mock_rebuild.assert_called_once()
        mock_search.assert_not_called()

    def test_skill_tool_event_extracts_rag_payload(self) -> None:
        service = ClawdWebService(workspace_root=self.home / "workspace")
        rag_payload = {
            "query": "RD-170",
            "markdown_files_scanned": 1,
            "chunks_indexed": 1,
            "cache": {"enabled": True, "hit": False, "path": None},
            "hits": [{"rank": 1, "score": 1, "file": "a.md", "start_line": 1, "end_line": 2, "snippet": "hit"}],
        }
        event = ToolEvent(
            kind="tool_result",
            tool_name="Skill",
            tool_output={
                "success": True,
                "retrievedCommandOutput": "Command: search\n\nExit code: 0\n\nSTDOUT:\n"
                + json.dumps(rag_payload),
            },
        )

        serialized = service._serialize_tool_event(event)

        self.assertEqual(serialized["rag"]["query"], "RD-170")
        self.assertEqual(serialized["rag"]["hits"][0]["file"], "a.md")
