"""Tests for the browser UI service."""

from __future__ import annotations

import json
import re
import tempfile
import threading
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from src.config import _encode_api_key
from src.providers.base import BaseProvider, ChatResponse
from src.tool_system.agent_loop import ToolEvent
from src.tool_system.defaults import build_default_registry
from src.tool_system.registry import ToolRegistry
from src.web import ClawdWebService
from src.web.app import (
    APP_JS,
    INDEX_HTML as STATIC_INDEX_HTML,
    ORBIT_CONTROLS_JS,
    STYLES_CSS,
    THREE_JS,
)


INDEX_HTML = "\n".join((STATIC_INDEX_HTML, STYLES_CSS, APP_JS))


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


class ArtifactProducingProvider(FakeProvider):
    """Fake provider that follows the injected per-session output contract."""

    def chat(self, messages, tools=None, **kwargs) -> ChatResponse:
        last_message = messages[-1]
        content = str(last_message.get("content", "")) if isinstance(last_message, dict) else str(last_message.content)
        match = re.search(r"Pass this exact base output directory to --output-dir: (.+)", content)
        if match:
            output_dir = Path(match.group(1).strip()) / "case_alpha"
            output_dir.mkdir(parents=True, exist_ok=True)
            (output_dir / "design_report.md").write_text("# report", encoding="utf-8")
            (output_dir / "design_data.json").write_text(
                json.dumps(
                    {
                        "schema_version": 2,
                        "project_name": "case_alpha",
                        "timestamp": "2026-07-13T12:00:00",
                        "inputs": {
                            "requirements": {"range_m": 120_000.0, "payload_kg": 12.0},
                            "initial_guess": {"aspect_ratio": 8.0},
                            "solver_options": {},
                        },
                        "numerical_converged": True,
                        "engineering_feasible": True,
                        "constraints": [],
                        "stage_status": {
                            "requirements": {"status": "completed", "blocking": True},
                            "class1_sizing": {"status": "completed", "blocking": True},
                        },
                        "outputs": {
                            "mtow_kg": 260.0,
                            "empty_weight_kg": 170.0,
                            "fuel_weight_kg": 78.0,
                            "wing_area_m2": 4.2,
                            "thrust_sl_n": 1_020.0,
                            "iterations": 8,
                            "geometry": {"span_m": 5.8},
                            "performance": {"actual_range_m": 120_000.0},
                        },
                    }
                ),
                encoding="utf-8",
            )
            (output_dir / "geometry.obj").write_text("o aircraft", encoding="utf-8")
            (output_dir / "helper.py").write_text("print('not an artifact')", encoding="utf-8")
        return super().chat(messages, tools=tools, **kwargs)


class TestBrowserRegistry(unittest.TestCase):
    """Tool registration behavior for the browser mode."""

    def test_web_registry_excludes_questionnaire_tool(self):
        registry = build_default_registry(enable_ask_user_question=False)
        tool_names = {spec.name for spec in registry.list_specs()}
        self.assertNotIn("AskUserQuestion", tool_names)
        self.assertIn("Read", tool_names)


class TestBrowserMarkup(unittest.TestCase):
    """Static browser UI markup should stay in the Codex-style workbench shape."""

    def test_index_html_uses_workbench_style_hero(self) -> None:
        self.assertIn('class="hero-copy"', INDEX_HTML)
        self.assertIn('class="hero-stack"', INDEX_HTML)
        self.assertIn('process-panel', INDEX_HTML)
        self.assertNotIn('prompt-chip', INDEX_HTML)
        self.assertIn('id="aircraftSkillToggle"', INDEX_HTML)
        self.assertIn('class="topbar-skill-toggle"', INDEX_HTML)
        self.assertIn('deepseek-v4-pro', INDEX_HTML)

    def test_index_html_loads_external_static_assets(self) -> None:
        self.assertIn('href="/static/styles.css"', STATIC_INDEX_HTML)
        self.assertIn('src="/static/vendor/three.min.js"', STATIC_INDEX_HTML)
        self.assertIn('src="/static/vendor/OrbitControls.js"', STATIC_INDEX_HTML)
        self.assertIn('src="/static/app.js"', STATIC_INDEX_HTML)
        self.assertNotIn("<style>", STATIC_INDEX_HTML)
        self.assertNotIn("<script>", STATIC_INDEX_HTML)
        self.assertGreater(len(THREE_JS), 500_000)
        self.assertGreater(len(ORBIT_CONTROLS_JS), 20_000)

    def test_index_html_keeps_codex_style_agent_layout(self) -> None:
        self.assertIn("grid-template-columns: 400px minmax(0, 1fr);", INDEX_HTML)
        self.assertIn(".settings-overlay", INDEX_HTML)
        self.assertIn('id="settingsToggleBtn"', INDEX_HTML)
        self.assertIn('id="chatViewBtn"', INDEX_HTML)
        self.assertIn('id="newSessionBtn"', INDEX_HTML)
        self.assertNotIn('class="window-strip"', INDEX_HTML)
        self.assertNotIn('class="traffic-lights"', INDEX_HTML)
        self.assertNotIn('class="window-actions"', INDEX_HTML)
        self.assertIn('class="topbar-design-tools" aria-label="总体设计工具"', INDEX_HTML)
        self.assertIn('id="designWorkspaceBtn" class="secondary topbar-design-button"', INDEX_HTML)
        self.assertNotIn('id="designWorkspaceBtn" class="nav-item"', INDEX_HTML)
        self.assertNotIn('class="composer-toolbar"', INDEX_HTML)
        self.assertNotIn("在输入框中启用飞行器总体设计技能", INDEX_HTML)
        self.assertNotIn('id="skillsPageBtn"', INDEX_HTML)
        self.assertNotIn('id="skillsView"', INDEX_HTML)
        self.assertNotIn("技能展示", INDEX_HTML)
        self.assertNotIn('id="skillSelect"', INDEX_HTML)
        self.assertIn(".topbar-actions", INDEX_HTML)
        self.assertIn(".message.assistant {\n      align-self: center;", INDEX_HTML)
        self.assertIn("details.open = true;", INDEX_HTML)
        self.assertIn("badge is-idle", INDEX_HTML)
        self.assertIn(".badge.is-busy", INDEX_HTML)
        self.assertIn("grid-template-rows: auto minmax(0, 1fr);", INDEX_HTML)
        self.assertIn(".sidebar .sidebar-group,", INDEX_HTML)
        self.assertIn(".main.is-design-mode .topbar", INDEX_HTML)
        self.assertIn("草稿已清空。", INDEX_HTML)
        self.assertIn("artifact-panel", INDEX_HTML)
        self.assertIn("结果下载", INDEX_HTML)
        self.assertIn("下载结果包", INDEX_HTML)
        self.assertNotIn(">插件<", INDEX_HTML)
        self.assertNotIn(">自动化<", INDEX_HTML)
        self.assertNotRegex(INDEX_HTML, r"letter-spacing:\s*-")

    def test_index_html_exposes_conversation_scoped_result_viewer(self) -> None:
        self.assertIn('hidden>设计结果</button>', INDEX_HTML)
        self.assertIn('aria-label="总体设计结果视图"', INDEX_HTML)
        self.assertIn('id="designResultVersionSelect"', INDEX_HTML)
        self.assertIn('data-design-tab="results"', INDEX_HTML)
        self.assertIn('data-design-tab="compare"', INDEX_HTML)
        self.assertIn('data-design-tab="reports"', INDEX_HTML)
        self.assertIn('>历史对比</button>', INDEX_HTML)
        self.assertIn('id="legacyDesignWorkbench"', INDEX_HTML)
        self.assertIn("function syncSessionDesignResults", INDEX_HTML)
        self.assertIn("session.design_results", INDEX_HTML)
        self.assertIn('const allowed = ["results", "compare", "reports"]', INDEX_HTML)
        self.assertNotIn('designRunForm.addEventListener("submit", submitDesignJob);', INDEX_HTML)
        self.assertNotIn('designCancelBtn.addEventListener("click", cancelDesignJob);', INDEX_HTML)
        self.assertNotIn('designRetryBtn.addEventListener("click", retryDesignJob);', INDEX_HTML)
        self.assertNotIn('designLoadAdjustBtn.addEventListener', INDEX_HTML)
        self.assertNotIn('restoreLatest: true', INDEX_HTML)
        self.assertIn("createDesignResultPanel", INDEX_HTML)
        self.assertIn("design-result-metrics", INDEX_HTML)
        self.assertIn("design-weight-bar", INDEX_HTML)


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
        latest_skill_dir = workspace / ".clawd" / "skills" / "aircraft-design-skill"
        latest_skill_dir.mkdir(parents=True)
        (latest_skill_dir / "SKILL.md").write_text(
            "---\nname: aircraft-design-skill\ndescription: Latest aircraft design skill\n---\nUse latest skill.",
            encoding="utf-8",
        )
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
        self.assertEqual(payload["skills"][0]["name"], "aircraft-design-skill")
        self.assertEqual(payload["skills"][0]["display_name"], "飞行器总体设计")
        self.assertEqual(created["session"]["auto_skill"], "aircraft-design-skill")
        self.assertIn("飞行器总体设计", reply["reply"]["text"])
        self.assertNotIn("aircraft-design-rag", reply["reply"]["text"])
        self.assertNotIn("aircraft-conceptual-design", reply["reply"]["text"])

    @patch("src.agent.session.Path.home")
    @patch("src.web.app.build_default_registry", side_effect=lambda **_kwargs: ToolRegistry())
    @patch("src.web.app.get_provider_class", return_value=FakeProvider)
    def test_bootstrap_payload_exposes_engineering_modes(
        self,
        _mock_provider_class,
        _mock_build_registry,
        mock_session_home,
    ) -> None:
        mock_session_home.return_value = self.home
        workspace = self.home / "workspace"
        for skill_name in (
            "aircraft-design-skill",
            "aircraft-design-rag",
            "aircraft-conceptual-design",
            "aero-intake-exhaust-evaluation",
            "aero-propulsion-analysis",
            "flight-performance-analysis",
        ):
            skill_dir = workspace / ".clawd" / "skills" / skill_name
            skill_dir.mkdir(parents=True, exist_ok=True)
            (skill_dir / "SKILL.md").write_text(
                f"---\nname: {skill_name}\ndescription: demo\n---\nDemo skill.",
                encoding="utf-8",
            )

        with patch("src.config.Path.home", return_value=self.home):
            service = ClawdWebService(workspace_root=workspace)
            payload = service.get_bootstrap_payload()

        names = [skill["name"] for skill in payload["skills"]]
        self.assertEqual(names, ["aircraft-design-skill"])
        self.assertEqual([skill["display_name"] for skill in payload["skills"]], ["飞行器总体设计"])
        self.assertTrue(all(skill["short_label"] for skill in payload["skills"]))

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
        skill_dir = workspace / ".clawd" / "skills" / "aircraft-design-skill"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            "---\nname: aircraft-design-skill\ndescription: Latest aircraft design skill\n---\nUse latest skill.",
            encoding="utf-8",
        )
        service = ClawdWebService(workspace_root=workspace)
        created = service.create_session(
            provider_name="openai",
            model="qwen3-4b",
            auto_approve=False,
            auto_skill="aircraft-design-skill",
            rag_settings={"top_k": 3, "auto_retrieve": False},
        )
        session_id = created["session"]["session_id"]

        service.send_message(session_id, "Keep this after restart")

        session_file = self.home / ".clawd" / "sessions" / f"{session_id}.json"
        preferences_file = self.home / ".clawd" / "web_sessions" / f"{session_id}.json"
        self.assertTrue(session_file.exists())
        self.assertTrue(preferences_file.exists())

        restarted = ClawdWebService(workspace_root=workspace)
        listed = restarted.list_sessions_payload()
        loaded = restarted.get_session_payload(session_id)

        self.assertEqual([item["session_id"] for item in listed["sessions"]], [session_id])
        self.assertEqual(loaded["session"]["messages"][0]["text"], "Keep this after restart")
        self.assertIn("Keep this after restart", loaded["session"]["messages"][1]["text"])
        self.assertFalse(loaded["session"]["auto_approve"])
        self.assertEqual(loaded["session"]["auto_skill"], "aircraft-design-skill")
        restored_state = restarted._require_session(session_id)
        self.assertEqual(restored_state.rag_settings.top_k, 3)
        self.assertFalse(restored_state.rag_settings.auto_retrieve)

    @patch("src.agent.session.Path.home")
    @patch("src.web.app.build_default_registry", side_effect=lambda **_kwargs: ToolRegistry())
    @patch("src.web.app.get_provider_class", return_value=ArtifactProducingProvider)
    def test_aircraft_skill_results_are_packaged_for_download(
        self,
        _mock_provider_class,
        _mock_build_registry,
        mock_session_home,
    ) -> None:
        mock_session_home.return_value = self.home
        workspace = self.home / "workspace"
        skill_dir = workspace / ".clawd" / "skills" / "aircraft-design-skill"
        skill_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            "---\nname: aircraft-design-skill\ndescription: Latest aircraft design skill\n---\nUse latest skill.",
            encoding="utf-8",
        )

        with patch("src.config.Path.home", return_value=self.home):
            service = ClawdWebService(workspace_root=workspace)
            created = service.create_session(
                provider_name="openai",
                model="qwen3-4b",
                auto_skill="aircraft-design-skill",
                rag_settings={"auto_retrieve": False},
            )
            self.assertEqual(created["session"]["design_results"], [])
            reply = service.send_message(created["session"]["session_id"], "生成总体设计结果")

        artifacts = reply["reply"]["artifacts"]
        self.assertEqual(len(artifacts), 1)
        artifact = artifacts[0]
        self.assertEqual(artifact["kind"], "aircraft_design_result_zip")
        self.assertEqual(artifact["name"], "飞行器总体设计结果包")
        self.assertEqual(artifact["file_count"], 3)
        self.assertTrue(artifact["source_dir"].endswith("/case_alpha"))
        self.assertIn(".clawd/generated/aircraft_design_runs/", artifact["source_dir"])
        self.assertIn("/api/artifacts/", artifact["download_url"])
        self.assertEqual(reply["session"]["messages"][1]["artifacts"][0]["id"], artifact["id"])

        design_results = reply["session"]["design_results"]
        self.assertEqual(len(design_results), 1)
        result = design_results[0]
        self.assertEqual(result["source"], "conversation")
        self.assertEqual(result["session_id"], created["session"]["session_id"])
        self.assertEqual(result["request"]["project_name"], "case_alpha")
        self.assertEqual(result["status"], "completed")
        self.assertEqual(result["result"]["summary"]["mtow_kg"], 260.0)
        self.assertTrue(result["result"]["engineering"]["engineering_feasible"])
        result_files = {item["name"]: item for item in result["result_files"]}
        self.assertEqual(set(result_files), {"design_data.json", "design_report.md", "geometry.obj"})
        self.assertIn(
            f"/api/sessions/{created['session']['session_id']}/design-results/",
            result_files["geometry.obj"]["preview_url"],
        )
        resolved_report = service.resolve_session_design_result_file(
            created["session"]["session_id"],
            result["job_id"],
            "design_report.md",
        )
        self.assertEqual(resolved_report["path"].read_text(encoding="utf-8"), "# report")

        download = service.resolve_artifact_download(artifact["id"])
        self.assertTrue(download["path"].exists())
        self.assertEqual(download["filename"], artifact["filename"])
        with zipfile.ZipFile(download["path"]) as zf:
            names = set(zf.namelist())
        self.assertIn("case_alpha/design_report.md", names)
        self.assertIn("case_alpha/design_data.json", names)
        self.assertIn("case_alpha/geometry.obj", names)
        self.assertIn("case_alpha/download_manifest.json", names)
        self.assertNotIn("case_alpha/helper.py", names)

        restarted = ClawdWebService(workspace_root=workspace)
        restored = restarted.get_session_payload(created["session"]["session_id"])
        restored_artifacts = restored["session"]["messages"][1]["artifacts"]
        self.assertEqual(restored_artifacts[0]["id"], artifact["id"])
        self.assertEqual(len(restored["session"]["design_results"]), 1)
        self.assertTrue(restarted.resolve_artifact_download(artifact["id"])["path"].exists())
        reset = restarted.reset_session(created["session"]["session_id"])
        self.assertEqual(reset["session"]["design_results"], [])

    @patch("src.agent.session.Path.home")
    @patch("src.web.app.build_default_registry", side_effect=lambda **_kwargs: ToolRegistry())
    @patch("src.web.app.get_provider_class", return_value=FakeProvider)
    def test_aircraft_skill_does_not_package_stale_results(
        self,
        _mock_provider_class,
        _mock_build_registry,
        mock_session_home,
    ) -> None:
        mock_session_home.return_value = self.home
        workspace = self.home / "workspace"
        skill_dir = workspace / ".clawd" / "skills" / "aircraft-design-skill"
        stale_dir = skill_dir / "output" / "old_case"
        stale_dir.mkdir(parents=True)
        (skill_dir / "SKILL.md").write_text(
            "---\nname: aircraft-design-skill\ndescription: Latest aircraft design skill\n---\nUse latest skill.",
            encoding="utf-8",
        )
        (stale_dir / "design_report.md").write_text("# stale", encoding="utf-8")

        with patch("src.config.Path.home", return_value=self.home):
            service = ClawdWebService(workspace_root=workspace)
            created = service.create_session(
                provider_name="openai",
                model="qwen3-4b",
                auto_skill="aircraft-design-skill",
                rag_settings={"auto_retrieve": False},
            )
            reply = service.send_message(created["session"]["session_id"], "生成总体设计结果")

        self.assertEqual(reply["reply"]["artifacts"], [])
        self.assertEqual(reply["session"]["design_results"], [])
        artifact_events = [event for event in reply["reply"]["events"] if event["kind"] == "artifact"]
        self.assertTrue(artifact_events[0]["is_error"])
        self.assertIn("未检测到新的设计结果", artifact_events[0]["summary"])

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
        latest_skill_dir = workspace / ".clawd" / "skills" / "aircraft-design-skill"
        latest_skill_dir.mkdir(parents=True)
        (latest_skill_dir / "SKILL.md").write_text(
            "---\nname: aircraft-design-skill\ndescription: Latest aircraft design skill\n---\nUse latest skill.",
            encoding="utf-8",
        )
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
                auto_skill="aircraft-design-skill",
            )
            reply = service.send_message(created["session"]["session_id"], "What is RD-170?")

        events = reply["reply"]["events"]
        self.assertEqual(events[0]["kind"], "tool_use")
        self.assertEqual(events[0]["tool_name"], "Skill")
        agent_events = [event for event in events if event["kind"] == "agent_step"]
        self.assertEqual(agent_events[0]["agent_name"], "Supervisor")
        self.assertTrue(any(event.get("agent_name") == "总体设计管理员" for event in events))
        self.assertTrue(any(event.get("agent_name") == "资料检索Agent" for event in events))
        rag_events = [event for event in events if event["kind"] == "rag_retrieval"]
        self.assertEqual(rag_events[0]["tool_name"], "aircraft-design-skill")
        self.assertEqual(rag_events[0]["rag"]["hits"][0]["file"], "RAG-data/engine.md")
        self.assertIn("M1 multi-agent aircraft-design orchestration context", reply["reply"]["text"])
        self.assertIn("Browser-attached local aircraft-design evidence", reply["reply"]["text"])
        self.assertEqual(reply["session"]["auto_skill"], "aircraft-design-skill")
        saved_events = reply["session"]["messages"][1]["events"]
        self.assertEqual(saved_events[0]["kind"], "tool_use")
        self.assertEqual(saved_events[0]["tool_name"], "Skill")
        saved_rag_events = [event for event in saved_events if event["kind"] == "rag_retrieval"]
        self.assertEqual(saved_rag_events[0]["rag"]["hits"][0]["file"], "RAG-data/engine.md")

        restarted = ClawdWebService(workspace_root=workspace)
        restored = restarted.get_session_payload(created["session"]["session_id"])
        restored_events = restored["session"]["messages"][1]["events"]
        restored_rag_events = [event for event in restored_events if event["kind"] == "rag_retrieval"]
        self.assertEqual(restored_rag_events[0]["rag"]["hits"][0]["file"], "RAG-data/engine.md")

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
        latest_skill_dir = workspace / ".clawd" / "skills" / "aircraft-design-skill"
        latest_skill_dir.mkdir(parents=True)
        (latest_skill_dir / "SKILL.md").write_text(
            "---\nname: aircraft-design-skill\ndescription: Latest aircraft design skill\n---\nUse latest skill.",
            encoding="utf-8",
        )
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
                auto_skill="aircraft-design-skill",
            )
            reply = service.send_message(created["session"]["session_id"], "What is RD-170?")

        events = reply["reply"]["events"]
        self.assertEqual(events[0]["kind"], "tool_use")
        self.assertEqual(events[0]["tool_name"], "Skill")
        agent_events = [event for event in events if event["kind"] == "agent_step"]
        self.assertEqual(agent_events[0]["agent_name"], "Supervisor")
        rag_events = [event for event in events if event["kind"] == "rag_retrieval"]
        self.assertEqual(rag_events[0]["tool_name"], "aircraft-design-skill")
        self.assertTrue(rag_events[0]["rag"]["cache"]["build_in_progress"])
        self.assertEqual(reply["session"]["auto_skill"], "aircraft-design-skill")
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

    def test_invalid_tilde_path_hint_does_not_break_artifact_discovery(self) -> None:
        service = ClawdWebService(workspace_root=self.home / "workspace")

        with patch("src.web.app.Path.expanduser", side_effect=RuntimeError("Could not determine home directory.")):
            candidates = service._hinted_aircraft_output_candidates("output may be at ~/unknown", [])

        self.assertEqual(candidates, [])
