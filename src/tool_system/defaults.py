from __future__ import annotations

from pathlib import Path

from .loader import load_tools_from_dir
from .registry import ToolRegistry
from .tools import (
    AskUserQuestionTool,
    BashTool,
    BriefTool,
    ConfigTool,
    CronCreateTool,
    CronDeleteTool,
    CronListTool,
    EnterPlanModeTool,
    EnterWorktreeTool,
    ExitPlanModeTool,
    ExitWorktreeTool,
    FileEditTool,
    FileReadTool,
    FileWriteTool,
    GlobTool,
    GrepTool,
    LSPTool,
    ListMcpResourcesTool,
    MCPTool,
    NotebookEditTool,
    PowerShellTool,
    REPLTool,
    ReadMcpResourceTool,
    RemoteTriggerTool,
    SendMessageTool,
    SendUserMessageTool,
    SkillTool,
    SleepTool,
    StructuredOutputTool,
    TeamCreateTool,
    TeamDeleteTool,
    TaskCreateTool,
    TaskGetTool,
    TaskListTool,
    TaskOutputTool,
    TaskStopTool,
    TaskUpdateTool,
    TestingPermissionTool,
    TodoWriteTool,
    WebFetchTool,
    WebSearchTool,
)
from .tools.agent import AgentTool
from .tools.tool_search import ToolSearchTool


def _default_tools(*, enable_ask_user_question: bool = True) -> list[object]:
    tools: list[object] = [
        SendUserMessageTool(),
        BashTool(),
        FileReadTool(),
        FileWriteTool(),
        FileEditTool(),
        GlobTool(),
        GrepTool(),
        WebFetchTool(),
        WebSearchTool(),
        SleepTool(),
        TaskStopTool(),
        ConfigTool(),
        MCPTool(),
        ListMcpResourcesTool(),
        ReadMcpResourceTool(),
        LSPTool(),
        SkillTool(),
        BriefTool(),
        TodoWriteTool(),
        TaskCreateTool(),
        TaskGetTool(),
        TaskListTool(),
        TaskUpdateTool(),
        TaskOutputTool(),
        TeamCreateTool(),
        TeamDeleteTool(),
        EnterPlanModeTool(),
        ExitPlanModeTool(),
        EnterWorktreeTool(),
        ExitWorktreeTool(),
        CronCreateTool(),
        CronListTool(),
        CronDeleteTool(),
        SendMessageTool(),
        StructuredOutputTool(),
        RemoteTriggerTool(),
        PowerShellTool(),
        NotebookEditTool(),
        REPLTool(),
        TestingPermissionTool(),
    ]
    if enable_ask_user_question:
        tools.insert(17, AskUserQuestionTool())
    return tools


def build_default_registry(
    *,
    include_user_tools: bool = True,
    enable_ask_user_question: bool = True,
) -> ToolRegistry:
    registry = ToolRegistry(tools=_default_tools(enable_ask_user_question=enable_ask_user_question))
    registry.register(AgentTool(registry))
    registry.register(ToolSearchTool(registry))

    if include_user_tools:
        user_dir = Path.home() / ".clawd" / "tools"
        for tool in load_tools_from_dir(user_dir):
            registry.register(tool)

    return registry
