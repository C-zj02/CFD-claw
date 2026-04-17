"""Tests for the browser UI service."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.config import _encode_api_key
from src.providers.base import BaseProvider, ChatResponse
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

    def tearDown(self) -> None:
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
            self.assertEqual(session["model"], "qwen3-4b")
            self.assertEqual(session["messages"], [])

            reply = service.send_message(session["session_id"], "Hello from the browser")

            self.assertEqual(reply["reply"]["text"], "Echo: Hello from the browser")
            self.assertEqual(reply["reply"]["usage"]["input_tokens"], 3)
            self.assertEqual(len(reply["session"]["messages"]), 2)
            self.assertEqual(reply["session"]["messages"][0]["role"], "user")
            self.assertEqual(reply["session"]["messages"][1]["role"], "assistant")

    def test_bootstrap_payload_marks_configured_providers(self) -> None:
        with patch("src.config.Path.home", return_value=self.home):
            service = ClawdWebService(workspace_root=self.home / "workspace")
            payload = service.get_bootstrap_payload()

        providers = {provider["name"]: provider for provider in payload["providers"]}
        self.assertEqual(payload["default_provider"], "openai")
        self.assertTrue(providers["openai"]["configured"])
        self.assertFalse(providers["anthropic"]["configured"])

