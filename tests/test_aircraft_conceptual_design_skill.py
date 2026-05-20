from __future__ import annotations

import asyncio
import subprocess
import sys
from pathlib import Path

from src.command_system.skills_integration import load_and_register_skills
from src.command_system.types import CommandContext
from src.skills.loader import clear_skill_registry, get_all_skills
from src.tool_system.context import ToolContext
from src.tool_system.tools import SkillTool


PROJECT_ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = PROJECT_ROOT / ".clawd" / "skills" / "aircraft-conceptual-design"


def teardown_function() -> None:
    clear_skill_registry()


def test_aircraft_conceptual_design_skill_is_discoverable_and_invocable() -> None:
    skills = {skill.name: skill for skill in get_all_skills(project_root=PROJECT_ROOT)}
    design_brief = "设计一架 航程1200km 载荷500kg 的无人机"

    assert "aircraft-conceptual-design" in skills
    skill = skills["aircraft-conceptual-design"]
    assert skill.loaded_from == "project"
    assert skill.skill_root == str(SKILL_DIR)
    assert skill.max_turns == 12
    assert "--top-docs" not in skill.markdown_content
    assert "--max-hits-per-file" not in skill.markdown_content
    assert "--format json" in skill.markdown_content
    assert "可见推理规范" in skill.markdown_content
    assert "设计推理记录" in skill.markdown_content
    assert "工具预算" in skill.markdown_content
    assert "--top-k 4" in skill.markdown_content
    assert "--max-snippet-chars 450" in skill.markdown_content
    assert "最多 4 次" in skill.markdown_content
    assert ".clawd/generated" in skill.markdown_content
    assert "constraint_spec-<run-id>.json" in skill.markdown_content
    assert "不要读取本技能自己的 `SKILL.md`" in skill.markdown_content
    assert "不要调用 `TodoWrite`" in skill.markdown_content

    context = ToolContext(workspace_root=PROJECT_ROOT)
    result = SkillTool().run(
        {"skill": "aircraft-conceptual-design", "args": design_brief},
        context,
    ).output

    assert result["success"] is True
    assert result["loadedFrom"] == "project"
    assert result["skillRoot"] == str(SKILL_DIR)
    assert design_brief in result["prompt"]
    assert f"{PROJECT_ROOT}/RAG-data" in result["prompt"]
    assert f"{SKILL_DIR}/scripts/plot_constraint_boundary.py" in result["prompt"]
    assert "设计推理记录" in result["prompt"]
    assert "工具预算" in result["prompt"]
    assert ".clawd/generated" in result["prompt"]


def test_aircraft_conceptual_design_registers_as_slash_command() -> None:
    design_brief = "设计一架 航程1200km 载荷500kg 的无人机"
    commands = {command.name: command for command in load_and_register_skills(project_root=PROJECT_ROOT)}

    assert "aircraft-conceptual-design" in commands
    command = commands["aircraft-conceptual-design"]
    assert command.loaded_from == "project"
    assert command.skill_root == str(SKILL_DIR)
    assert command.max_turns == 12

    context = CommandContext(
        workspace_root=PROJECT_ROOT,
        cwd=PROJECT_ROOT,
        conversation=None,
        cost_tracker=None,
        history=None,
    )
    blocks = asyncio.run(command.get_prompt_for_command(design_brief, context))

    assert len(blocks) == 1
    prompt = blocks[0]["text"]
    assert design_brief in prompt
    assert f"{PROJECT_ROOT}/RAG-data" in prompt
    assert f"{SKILL_DIR}/scripts/plot_constraint_boundary.py" in prompt
    assert "设计推理记录" in prompt
    assert "工具预算" in prompt


def test_aircraft_conceptual_design_plot_script_renders_example(tmp_path: Path) -> None:
    svg_path = tmp_path / "boundary.svg"
    csv_path = tmp_path / "boundary.csv"
    script_path = SKILL_DIR / "scripts" / "plot_constraint_boundary.py"
    input_path = SKILL_DIR / "references" / "boundary-example.json"

    result = subprocess.run(
        [
            sys.executable,
            str(script_path),
            "--input",
            str(input_path),
            "--output",
            str(svg_path),
            "--csv",
            str(csv_path),
        ],
        cwd=PROJECT_ROOT,
        text=True,
        capture_output=True,
        check=False,
    )

    assert result.returncode == 0, result.stdout + result.stderr
    assert svg_path.exists()
    assert csv_path.exists()
    assert "<svg" in svg_path.read_text(encoding="utf-8")
    csv_lines = csv_path.read_text(encoding="utf-8-sig").splitlines()
    assert csv_lines[0] == "type,name,sense,x,y,source"
    assert any(line.startswith("constraint,") for line in csv_lines[1:])
