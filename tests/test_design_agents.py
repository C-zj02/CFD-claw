"""Tests for the M1 aircraft design multi-agent orchestration path."""

from __future__ import annotations

from src.design_agents import AircraftDesignOrchestrator, DesignTaskState


class DummySettings:
    top_k = 3
    max_snippet_chars = 180
    use_cache = True
    auto_retrieve = True
    candidate_limit = 500


class DummyRagService:
    def cache_ready(self, settings=None) -> bool:
        return True

    def rebuild(self, settings=None, *, force=True):
        return {"rebuild": {"running": True}}

    def not_ready_payload(self, query, settings=None):
        return {"query": query, "hits": [], "cache": {"ready": False}}

    def search(self, query, settings):
        return {
            "query": query,
            "markdown_files_scanned": 2,
            "chunks_indexed": 12,
            "candidate_chunks": 12,
            "cache": {"enabled": True, "hit": True, "path": "cache.sqlite"},
            "hits": [
                {
                    "rank": 1,
                    "score": 9.2,
                    "file": "RAG-data/aircraft.md",
                    "start_line": 10,
                    "end_line": 20,
                    "heading": "总体设计",
                    "snippet": "翼载和推重比是总体参数选择的关键。",
                }
            ],
        }


def test_aircraft_orchestrator_builds_m1_closed_loop_context() -> None:
    events = []
    orchestrator = AircraftDesignOrchestrator()

    result = orchestrator.run(
        user_request="设计一架航程1200km、载荷500kg的固定翼无人机，输出总体参数和约束分析",
        capability="aircraft-design",
        rag_service=DummyRagService(),
        rag_settings=DummySettings(),
        emit_event=events.append,
    )

    assert result.task.state == DesignTaskState.READY_FOR_MODEL
    assert result.task.intent["task_type"] == "约束分析与设计点选取"
    assert "总体" in result.task.intent["disciplines"]
    assert "飞行性能" in result.task.intent["disciplines"]
    assert result.evidence is not None
    assert result.evidence["hits"][0]["file"] == "RAG-data/aircraft.md"
    assert "Supervisor intent" in result.context_prompt
    assert "总体设计管理员" in result.context_prompt
    assert [event["kind"] for event in events].count("agent_step") >= 6
    assert events[0]["agent_name"] == "Supervisor"
    assert any(event["agent_name"] == "资料检索Agent" for event in events)
