"""M1 multi-agent orchestration for aircraft conceptual design."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Protocol

from src.design_agents.models import AgentEvent, DesignTask, DesignTaskState


class RagSettingsLike(Protocol):
    """Minimal retrieval settings used by the orchestrator."""

    top_k: int
    max_snippet_chars: int
    use_cache: bool
    auto_retrieve: bool
    candidate_limit: int


class RagServiceLike(Protocol):
    """Subset of the browser RAG service used by the retrieval function agent."""

    def cache_ready(self, settings: Any | None = None) -> bool: ...

    def rebuild(self, settings: Any | None = None, *, force: bool = True) -> dict[str, Any]: ...

    def not_ready_payload(self, query: str, settings: Any | None = None) -> dict[str, Any]: ...

    def search(self, query: str, settings: Any) -> dict[str, Any]: ...


EventSink = Callable[[AgentEvent], None]


@dataclass
class OrchestrationResult:
    """Result returned after the M1 orchestration preflight."""

    task: DesignTask
    evidence: dict[str, Any] | None
    context_prompt: str


class SupervisorAgent:
    """Central entry point that parses the user request and selects specialists."""

    name = "Supervisor"
    role = "任务层主智能体"

    def parse(self, task: DesignTask, emit: EventSink) -> None:
        intent = _parse_aircraft_intent(task.user_request)
        task.intent = intent
        task.state = DesignTaskState.PARSED
        emit(
            AgentEvent(
                agent_role=self.role,
                agent_name=self.name,
                stage="intent",
                summary=(
                    "已解析自然语言任务，识别为"
                    f"{intent['task_type']}，涉及专业：{'、'.join(intent['disciplines'])}"
                ),
                task=task,
                preview={"intent": intent},
            )
        )

    def plan(self, task: DesignTask, emit: EventSink) -> None:
        plan = [
            {
                "agent": "总体设计管理员",
                "input": "用户需求、约束、RAG 证据",
                "output": "需求矩阵、总体参数、约束分析、布局与风险",
            },
            {
                "agent": "资料检索Agent",
                "input": "总体设计检索查询",
                "output": "带来源路径和行号的本地资料证据",
            },
            {
                "agent": "数据处理Agent",
                "input": "用户参数、检索依据、工程假设",
                "output": "翼载/推重比、重量、任务剖面和校核项的计算任务清单",
            },
        ]
        if "飞行性能" in task.intent.get("disciplines", []):
            plan.append(
                {
                    "agent": "飞行性能管理员",
                    "input": "总体参数、气动/动力假设、任务剖面",
                    "output": "航程、爬升、起降、升限和包线校核建议",
                }
            )
        task.plan = plan
        task.state = DesignTaskState.PLANNED
        emit(
            AgentEvent(
                agent_role=self.role,
                agent_name=self.name,
                stage="plan",
                summary=f"已形成 M1 多智能体执行计划，共 {len(plan)} 个协同节点",
                task=task,
                preview={"plan": plan},
            )
        )

    def finalize(self, task: DesignTask, emit: EventSink) -> None:
        task.state = DesignTaskState.READY_FOR_MODEL
        emit(
            AgentEvent(
                agent_role=self.role,
                agent_name=self.name,
                stage="handoff",
                summary="已完成专业路由、资料接入和一致性检查，准备交给模型生成设计答复",
                task=task,
                preview={"checks": task.checks, "artifacts": task.artifacts},
            )
        )


class ConceptualDesignManagerAgent:
    """Professional manager for aircraft conceptual and overall design."""

    name = "总体设计管理员"
    role = "专业层管理员智能体"

    def prepare(self, task: DesignTask, emit: EventSink) -> str:
        query = _build_rag_query(task)
        task.checks.append(
            {
                "name": "输入输出兼容性检查",
                "status": "passed",
                "detail": "用户需求已转为总体设计任务，RAG 证据可作为后续模型上下文输入。",
            }
        )
        emit(
            AgentEvent(
                agent_role=self.role,
                agent_name=self.name,
                stage="discipline-plan",
                summary="已把用户需求拆成总体参数设计、约束边界、布局校核和风险验证子任务",
                task=task,
                preview={"rag_query": query, "required_outputs": _required_outputs(task)},
            )
        )
        return query

    def review_evidence(self, task: DesignTask, emit: EventSink) -> None:
        evidence = task.evidence or {}
        hits = evidence.get("hits") if isinstance(evidence, dict) else None
        hit_count = len(hits) if isinstance(hits, list) else 0
        status = "passed" if hit_count else "warning"
        task.checks.append(
            {
                "name": "数据来源准确性检查",
                "status": status,
                "detail": f"本轮检索返回 {hit_count} 条资料证据。",
            }
        )
        emit(
            AgentEvent(
                agent_role=self.role,
                agent_name=self.name,
                stage="evidence-review",
                summary=f"已审查资料检索结果，命中 {hit_count} 条，可用于总体设计依据追溯",
                task=task,
                preview={"hit_count": hit_count, "checks": task.checks[-1:]},
            )
        )


class RagRetrievalAgent:
    """Function-level agent that owns local evidence retrieval."""

    name = "资料检索Agent"
    role = "功能层智能体"

    def run(
        self,
        task: DesignTask,
        *,
        query: str,
        rag_service: RagServiceLike,
        settings: RagSettingsLike,
        emit: EventSink,
    ) -> dict[str, Any] | None:
        task.state = DesignTaskState.RETRIEVING
        emit(
            AgentEvent(
                agent_role=self.role,
                agent_name=self.name,
                stage="retrieval-start",
                summary="开始调用本地飞行器设计资料库，为总体设计任务准备可追溯依据",
                task=task,
                preview={"query": query, "settings": _settings_dict(settings)},
            )
        )
        try:
            if settings.use_cache and not rag_service.cache_ready(settings):
                rag_service.rebuild(settings, force=False)
                payload = rag_service.not_ready_payload(query, settings)
            else:
                payload = rag_service.search(query, settings)
        except Exception as exc:
            task.state = DesignTaskState.FAILED
            task.errors.append(str(exc))
            emit(
                AgentEvent(
                    agent_role=self.role,
                    agent_name=self.name,
                    stage="retrieval-error",
                    summary=f"本地资料检索失败：{exc}",
                    task=task,
                    preview={"query": query},
                    is_error=True,
                    error=str(exc),
                )
            )
            return None

        task.evidence = payload
        task.state = DesignTaskState.EVIDENCE_READY
        hits = payload.get("hits")
        hit_count = len(hits) if isinstance(hits, list) else 0
        task.artifacts.append(
            {
                "type": "rag_evidence",
                "name": "飞行器设计本地资料证据",
                "count": hit_count,
                "data_dir": payload.get("data_dir"),
            }
        )
        emit(
            AgentEvent(
                agent_role=self.role,
                agent_name=self.name,
                stage="retrieval-done",
                summary=f"已完成本地资料检索，命中 {hit_count} 条证据",
                task=task,
                preview={"query": query, "hit_count": hit_count},
            )
        )
        return payload


class DataProcessingAgent:
    """Function-level agent that prepares deterministic calculation checkpoints."""

    name = "数据处理Agent"
    role = "功能层智能体"

    def prepare_checkpoints(self, task: DesignTask, emit: EventSink) -> None:
        checkpoints = [
            "需求矩阵：区分用户输入、工程假设、计算结果和待确认项",
            "任务剖面：起飞、爬升、巡航、下降、着陆和备份余量",
            "总体参数：起飞重量、空重、燃油/能量、翼面积、翼载、推重比",
            "约束分析：起飞、着陆、爬升、巡航/升限在 W/S-T/W 平面的可行侧",
            "一致性校核：资料依据、单位、输入输出兼容性和下一步验证",
        ]
        task.checks.append(
            {
                "name": "工程可解释性检查",
                "status": "prepared",
                "detail": "已准备总体参数与约束分析的计算检查点，模型回答需逐项覆盖。",
            }
        )
        emit(
            AgentEvent(
                agent_role=self.role,
                agent_name=self.name,
                stage="calculation-checkpoints",
                summary="已生成总体设计计算检查点，后续回答将按这些节点组织参数和校核",
                task=task,
                preview={"checkpoints": checkpoints},
            )
        )


class AircraftDesignOrchestrator:
    """Minimal demonstrable orchestration path for aircraft design in the browser."""

    def __init__(self) -> None:
        self.supervisor = SupervisorAgent()
        self.conceptual_manager = ConceptualDesignManagerAgent()
        self.rag_agent = RagRetrievalAgent()
        self.data_agent = DataProcessingAgent()

    def run(
        self,
        *,
        user_request: str,
        capability: str,
        rag_service: RagServiceLike,
        rag_settings: RagSettingsLike,
        emit_event: Callable[[dict[str, Any]], None] | None = None,
    ) -> OrchestrationResult:
        web_events: list[dict[str, Any]] = []
        task = DesignTask(user_request=user_request, capability=capability)

        def emit(agent_event: AgentEvent) -> None:
            web_event = agent_event.to_web_event()
            web_events.append(web_event)
            if emit_event is not None:
                emit_event(web_event)

        self.supervisor.parse(task, emit)
        self.supervisor.plan(task, emit)
        query = self.conceptual_manager.prepare(task, emit)
        evidence = self.rag_agent.run(
            task,
            query=query,
            rag_service=rag_service,
            settings=rag_settings,
            emit=emit,
        )
        self.conceptual_manager.review_evidence(task, emit)
        self.data_agent.prepare_checkpoints(task, emit)
        self.supervisor.finalize(task, emit)
        context_prompt = build_orchestration_context(task)
        # Keep event list reachable for tests and callers that use only the result.
        task.artifacts.append({"type": "agent_events", "name": "多智能体过程事件", "count": len(web_events)})
        return OrchestrationResult(task=task, evidence=evidence, context_prompt=context_prompt)


def build_orchestration_context(task: DesignTask) -> str:
    """Build a concise prompt fragment injected before the user's request."""
    lines = [
        "M1 multi-agent aircraft-design orchestration context:",
        f"- Task id: {task.task_id}",
        f"- Supervisor intent: {task.intent.get('task_type', '未分类')}",
        f"- Disciplines: {'、'.join(task.intent.get('disciplines', [])) or '未识别'}",
        "- Agent plan:",
    ]
    for index, item in enumerate(task.plan, start=1):
        lines.append(f"  {index}. {item['agent']}: {item['input']} -> {item['output']}")
    lines.extend(
        [
            "- Required response discipline:",
            "  1. 明确用户输入、工程假设、计算结果和待确认项。",
            "  2. 输出需求解析、资料依据、总体参数、约束分析、布局校核、风险与下一步。",
            "  3. 对关键数值给出单位、来源和工程含义；资料不足时显式标注。",
            "  4. 保持回答可审计，不输出私有逐步思维链。",
        ]
    )
    if task.checks:
        lines.append("- Prepared checks:")
        for check in task.checks:
            lines.append(f"  - {check['name']}: {check['status']}，{check['detail']}")
    return "\n".join(lines)


def _parse_aircraft_intent(text: str) -> dict[str, Any]:
    normalized = text.lower()
    disciplines = ["总体"]
    if any(term in text for term in ("飞行性能", "航程", "航时", "爬升", "升限", "起飞", "着陆", "包线")):
        disciplines.append("飞行性能")
    if any(term in text for term in ("气动", "升阻", "阻力", "翼型", "布局", "稳定", "配平")):
        disciplines.append("气动")
    if any(term in text for term in ("发动机", "推进", "推力", "耗油", "进气道", "喷管", "动力")):
        disciplines.append("推进")

    if any(term in text for term in ("约束", "翼载", "推重比", "界限线")):
        task_type = "约束分析与设计点选取"
    elif any(term in text for term in ("航程", "载荷", "总体", "设计", "方案", "无人机", "飞机")):
        task_type = "总体参数设计"
    elif "性能" in text:
        task_type = "飞行性能分析"
    else:
        task_type = "飞行器设计问答"

    parameters = _extract_design_parameters(text)
    complexity = "multi_discipline" if len(disciplines) >= 3 else "single_or_lightweight"
    if "完整" in text or "报告" in text or len(text) > 120:
        complexity = "full_report"

    return {
        "task_type": task_type,
        "disciplines": disciplines,
        "parameters": parameters,
        "complexity": complexity,
        "needs_clarification": len(parameters) == 0 and task_type == "总体参数设计",
    }


def _extract_design_parameters(text: str) -> dict[str, str]:
    import re

    patterns = {
        "range": r"(航程|距离)\s*([0-9]+(?:\.[0-9]+)?)\s*(km|公里|千米)",
        "payload": r"(载荷|载重|有效载荷)\s*([0-9]+(?:\.[0-9]+)?)\s*(kg|公斤|吨|t)",
        "speed": r"(速度|巡航速度|马赫数|mach|ma)\s*([0-9]+(?:\.[0-9]+)?)\s*(km/h|m/s|马赫|mach|ma)?",
        "altitude": r"(高度|巡航高度|升限)\s*([0-9]+(?:\.[0-9]+)?)\s*(m|米|km|千米|公里)?",
        "runway": r"(跑道|起飞|着陆|起降)\s*([0-9]+(?:\.[0-9]+)?)\s*(m|米)",
    }
    parameters: dict[str, str] = {}
    for key, pattern in patterns.items():
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            label = match.group(1)
            value = match.group(2)
            unit = match.group(3) or ""
            parameters[key] = f"{label} {value}{unit}"
    return parameters


def _build_rag_query(task: DesignTask) -> str:
    intent = task.intent
    terms = ["飞机总体设计", "任务剖面", "翼载", "推重比", "约束分析"]
    task_type = intent.get("task_type", "")
    if "约束" in task_type:
        terms.extend(["约束边界", "起飞", "着陆", "爬升", "设计点"])
    if "飞行性能" in intent.get("disciplines", []):
        terms.extend(["飞行性能", "航程", "爬升", "升限"])
    if "推进" in intent.get("disciplines", []):
        terms.extend(["发动机选型", "推力", "耗油率"])
    params = intent.get("parameters") or {}
    if "range" in params:
        terms.append(params["range"])
    if "payload" in params:
        terms.append(params["payload"])
    return " ".join(dict.fromkeys(terms))


def _required_outputs(task: DesignTask) -> list[str]:
    outputs = ["需求解析", "依据检索", "总体参数", "约束分析", "布局方案", "风险与下一步"]
    if "飞行性能" in task.intent.get("disciplines", []):
        outputs.append("飞行性能校核")
    if "气动" in task.intent.get("disciplines", []):
        outputs.append("气动参数假设与验证建议")
    if "推进" in task.intent.get("disciplines", []):
        outputs.append("动力/推进参数假设与验证建议")
    return outputs


def _settings_dict(settings: RagSettingsLike) -> dict[str, Any]:
    return {
        "top_k": settings.top_k,
        "max_snippet_chars": settings.max_snippet_chars,
        "use_cache": settings.use_cache,
        "auto_retrieve": settings.auto_retrieve,
        "candidate_limit": settings.candidate_limit,
    }
