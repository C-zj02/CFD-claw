# Aircraft Conceptual Design Skill 使用说明

本文档说明项目内置技能 `aircraft-conceptual-design` 的用途、调用方式、输入建议、输出内容、验证方法和常见问题。该技能面向飞行器总体设计与概念方案设计，适合用本地 `RAG-data` 知识库辅助生成可追溯、可校核、可迭代的总体设计方案。

## 1. 技能位置

技能目录：

```text
.clawd/skills/aircraft-conceptual-design/
```

核心文件：

```text
.clawd/skills/aircraft-conceptual-design/SKILL.md
.clawd/skills/aircraft-conceptual-design/references/workflow.md
.clawd/skills/aircraft-conceptual-design/references/boundary-example.json
.clawd/skills/aircraft-conceptual-design/scripts/plot_constraint_boundary.py
```

相关依赖技能：

```text
.clawd/skills/aircraft-design-rag/
```

`aircraft-conceptual-design` 会优先使用 `aircraft-design-rag` 中的本地检索脚本，从项目根目录下的 `RAG-data` 检索飞行器设计资料。

## 2. 适用场景

当用户提出以下任务时，适合调用该技能：

- 飞行器总体设计或飞机总体设计。
- 固定翼无人机、通航飞机、民用运输机、军用固定翼、运输机、旋翼机、高速或高超声速飞行器的概念设计。
- 任务剖面拆解、航程/航时估算、载荷与重量闭合。
- 翼载荷 `W/S`、推重比 `T/W` 或功率载荷 `W/P` 的约束分析。
- 起飞距离、着陆距离、爬升率、升限、巡航、机动或过载约束分析。
- 方案界限线图绘制。
- 起飞重量、翼面积、翼展、展弦比、推力或功率的初步估算。
- 三视图参数、总体布局参数和后续 CFD/风洞/MDAO 分析建议。

不适合使用该技能的情况：

- 只需要普通聊天或非航空航天问题。
- 只想做代码调试、网页开发、数据清洗等非飞行器设计任务。
- 希望获得武器使用、打击、规避、杀伤优化等操作性内容。该技能只讨论总体性能、载荷包线、重量和布置层面的工程约束。

## 3. 启动智能体

进入项目根目录：

```bash
cd /Users/zejianchen/Desktop/claude_agent/Clawd-Code
```

如果使用虚拟环境，先激活：

```bash
source .venv/bin/activate
```

启动 REPL：

```bash
PYTHONPATH=. python -m src.cli
```

启动成功后会看到类似界面：

```text
CLAWD CODE
Model qwen3-4b
Provider OPENAI Provider
Workspace ~/Desktop/claude_agent/Clawd-Code
```

然后会出现输入提示符：

```text
❯
```

在这个提示符后输入 slash 命令即可调用技能。

## 4. 查看技能是否可用

在 REPL 中输入：

```text
/skills
```

正常情况下，输出列表中应包含：

```text
aircraft-conceptual-design
```

如果没有看到该技能，请确认当前工作目录是项目根目录：

```text
/Users/zejianchen/Desktop/claude_agent/Clawd-Code
```

项目级技能只会从当前项目的 `.clawd/skills/` 目录加载。若在其他目录启动 REPL，可能无法发现该技能。

## 5. 基本调用方式

在 REPL 中输入：

```text
/aircraft-conceptual-design 设计一架航程1200km、载荷500kg的无人机
```

更完整的示例：

```text
/aircraft-conceptual-design 设计一架航程1200km、载荷500kg、巡航高度5000m、跑道长度800m以内的固定翼无人机，输出总体参数、约束分析和方案界限线图
```

如果调用成功，不应出现：

```text
unknown skill: aircraft-conceptual-design
```

智能体会进入飞行器总体设计流程，并优先检索本地 `RAG-data`，再基于检索证据和工程假设输出设计结果。

## 6. 推荐输入格式

输入越完整，输出越可校核。推荐把设计需求写成一段清晰的设计 brief：

```text
/aircraft-conceptual-design 设计一架固定翼无人机：
用途：支线物流运输；
有效载荷：500kg；
航程：1200km；
巡航高度：5000m；
巡航速度：180km/h；
跑道长度：800m以内；
动力：活塞发动机或混动方案均可比较；
输出：需求矩阵、RAG依据、任务剖面、约束分析、总体参数、布局方案、方案界限线图、风险与下一步。
```

建议尽量提供以下信息：

- 用途和飞行器类型，例如固定翼无人机、通航飞机、运输机、旋翼机。
- 有效载荷、乘员或任务设备重量。
- 航程、航时、作战半径或待机时间。
- 巡航速度、最大速度、巡航高度、升限。
- 起飞距离、着陆距离、跑道条件、场高和温度。
- 爬升率、过载、盘旋、升限等性能指标。
- 动力形式，例如涡扇、涡桨、活塞、电推进、混动。
- 交付物要求，例如参数表、界限线图、三视图参数、设计报告。

如果缺少关键输入，技能会给出工程假设或列出待补充项，不会把缺失输入伪装成确定数据。

## 7. 输出内容

完整总体设计任务通常会输出以下部分。

### 7.1 需求解析

把自然语言设计任务拆成需求矩阵，包括用途、载荷、航程/航时、速度/高度、起降、爬升、升限、机动、动力、燃料或能量、维护、成本和交付物。

### 7.2 依据检索

列出本地 `RAG-data` 中检索到的资料来源，包括文件路径、行号范围和该证据支持的设计环节。

示例：

```text
依据：
- RAG-data/飞机设计手册_第4册_军用飞机总体设计...md:1200-1220
- RAG-data/飞机设计手册_第5册_民用飞机总体设计...md:880-905
```

### 7.3 任务剖面

将任务拆成起飞、爬升、巡航、待机或盘旋、下降、着陆、备份燃油或能量等阶段，说明每段的速度、高度、时间、距离和重量状态。

### 7.4 约束翻译

把设计要求转换到 `W/S - T/W` 或 `W/P` 平面中，说明每条约束的公式、参数、可行侧和数据点。

常见约束包括：

- 起飞距离约束。
- 着陆距离或失速速度约束。
- 爬升率或爬升梯度约束。
- 巡航或最大速度约束。
- 升限或剩余功率约束。
- 盘旋、过载或机动约束。

### 7.5 方案界限线图

当任务要求总体设计方案、约束分析或界限线图时，技能会使用自带脚本输出 SVG 和 CSV。

输出示例：

```text
方案界限线图：
SVG: /tmp/aircraft-boundary.svg
CSV: /tmp/aircraft-boundary.csv
推荐设计点：W/S = 430 kg/m^2, T/W = 0.78
```

SVG 用于查看图形，CSV 用于后续数据分析或复核。

### 7.6 总体参数

输出初步总体参数，包括：

- 起飞重量、空机重量、有效载荷、燃油或能量重量。
- 翼面积、翼展、展弦比、翼载荷。
- 推重比、总推力或总功率。
- 最大升力系数、升阻比、阻力参数。
- 机身长度、机翼根弦/尖弦、平均气动弦、尾翼参数。

### 7.7 布局方案

给出构型选择和布置建议，例如机翼形式、尾翼形式、动力布置、起落架、载荷舱、燃油或电池位置、重心范围和三视图参数。

### 7.8 校核结果

对起飞、着陆、爬升、巡航、航程、升限、燃油或能量、重心、稳定性、结构和运行约束进行初步校核。

### 7.9 迭代记录

说明 V0、V1、V2 设计轮次之间的参数变化。若起飞重量、翼载荷、推重比或关键几何变化超过约 5%，技能会建议继续迭代；若变化接近或超过约 30%，会提示初始设计点或布局可能不合理。

### 7.10 风险与下一步

列出主要风险、缺失数据和后续建议，例如 CFD、风洞试验、OpenVSP 建模、重量平衡、结构分析、MDAO 或参数敏感性分析。

## 8. RAG 检索机制

技能会优先使用项目内已有检索脚本：

```bash
python "${CLAUDE_PROJECT_DIR}/.clawd/skills/aircraft-design-rag/scripts/search_rag.py" \
  --data-dir "${CLAUDE_PROJECT_DIR}/RAG-data" \
  --query "<检索词>" \
  --format json \
  --use-cache \
  --top-k 8 \
  --max-snippet-chars 700
```

推荐查询词会按设计阶段拆分，而不是只跑一个大查询。

常见查询词：

```text
飞机总体设计 任务剖面 翼载 推重比 起飞重量 约束分析
约束边界分析 推重比 翼载荷 起飞 着陆 爬升 盘旋
民用飞机总体设计 初始参数估算 巡航马赫数 航程 爬升 起飞着陆
军用飞机总体设计 任务剖面 过载 盘旋 爬升 推重比 翼载荷
方案三视图 飞机几何参数 展弦比 后掠角 翼面积 机身长度
重量平衡 控制 空机重量 燃油重量 起飞重量 重心
发动机选型 推力 特性曲线 耗油率 总体设计
```

原则：

- 先检索本地 `RAG-data`，再进行设计推理。
- 每个关键数值必须标明来源：用户给定、本地知识库证据、计算得到或工程假设。
- 如果检索结果不足，要明确说明资料未覆盖，不应凭空给出精确参数。

## 9. 方案界限线图脚本

绘图脚本位置：

```text
.clawd/skills/aircraft-conceptual-design/scripts/plot_constraint_boundary.py
```

脚本用途：

- 读取约束图 JSON。
- 绘制 `W/S - T/W`、`W/S - W/P` 或类似二维约束图。
- 输出 SVG 图像。
- 可选输出 CSV 数据。

命令示例：

```bash
python .clawd/skills/aircraft-conceptual-design/scripts/plot_constraint_boundary.py \
  --input .clawd/skills/aircraft-conceptual-design/references/boundary-example.json \
  --output /tmp/aircraft-boundary.svg \
  --csv /tmp/aircraft-boundary.csv
```

成功输出：

```text
SVG: /private/tmp/aircraft-boundary.svg
CSV: /private/tmp/aircraft-boundary.csv
```

打开图：

```bash
open /tmp/aircraft-boundary.svg
```

JSON 基本结构：

```json
{
  "title": "方案界限线图",
  "x_label": "翼载荷 W/S (kg/m^2)",
  "y_label": "推重比 T/W",
  "x_range": [200, 800],
  "y_range": [0.2, 1.4],
  "constraints": [
    {
      "name": "起飞距离约束",
      "sense": "above",
      "points": [[250, 0.42], [350, 0.48], [450, 0.56], [550, 0.68]]
    },
    {
      "name": "着陆距离约束",
      "sense": "left",
      "x": 520
    }
  ],
  "design_points": [
    {"name": "推荐设计点", "x": 430, "y": 0.72}
  ]
}
```

`sense` 含义：

- `above`：曲线上方可行。
- `below`：曲线下方可行。
- `left`：曲线左侧可行。
- `right`：曲线右侧可行。

## 10. 终端验证方法

进入项目根目录：

```bash
cd /Users/zejianchen/Desktop/claude_agent/Clawd-Code
```

运行技能专项测试：

```bash
PYTHONPATH=. pytest -q tests/test_aircraft_conceptual_design_skill.py
```

预期输出：

```text
3 passed
```

该测试覆盖：

- 项目能发现 `aircraft-conceptual-design`。
- `SkillTool` 能调用该技能。
- slash 命令注册层能识别该技能。
- 绘图脚本能生成 SVG 和 CSV。

底层调用测试：

```bash
PYTHONPATH=. python - <<'PY'
from pathlib import Path
from src.skills.loader import get_all_skills
from src.tool_system.context import ToolContext
from src.tool_system.tools import SkillTool

root = Path.cwd()
skills = {skill.name: skill for skill in get_all_skills(project_root=root)}
print("skill_found =", "aircraft-conceptual-design" in skills)

ctx = ToolContext(workspace_root=root)
result = SkillTool().run(
    {
        "skill": "aircraft-conceptual-design",
        "args": "设计一架航程1200km、载荷500kg的无人机",
    },
    ctx,
).output

print("invoke_success =", result.get("success"))
print("command_name =", result.get("commandName"))
print("prompt_has_rag_data =", f"{root}/RAG-data" in result.get("prompt", ""))
print("prompt_has_plot_script =", "plot_constraint_boundary.py" in result.get("prompt", ""))
PY
```

预期输出：

```text
skill_found = True
invoke_success = True
command_name = aircraft-conceptual-design
prompt_has_rag_data = True
prompt_has_plot_script = True
```

RAG 检索测试：

```bash
python .clawd/skills/aircraft-design-rag/scripts/search_rag.py \
  --data-dir RAG-data \
  --query "飞机总体设计 任务剖面 翼载 推重比" \
  --format json \
  --use-cache \
  --top-k 1 \
  --max-snippet-chars 260
```

预期输出应包含 `hits` 数组，并显示命中的 `RAG-data/...md` 文件、行号和片段。

绘图脚本测试：

```bash
python .clawd/skills/aircraft-conceptual-design/scripts/plot_constraint_boundary.py \
  --input .clawd/skills/aircraft-conceptual-design/references/boundary-example.json \
  --output /tmp/aircraft-boundary.svg \
  --csv /tmp/aircraft-boundary.csv
```

如果你需要自己生成 JSON 规格，优先放到 `.clawd/generated/` 里的临时文件，不要反复覆盖仓库根目录下的 `constraint_spec.json`。

预期输出：

```text
SVG: /private/tmp/aircraft-boundary.svg
CSV: /private/tmp/aircraft-boundary.csv
```

## 11. 常见问题

### 11.1 unknown skill: aircraft-conceptual-design

原因通常是当前工作目录不对，或者项目没有加载 `.clawd/skills`。

处理步骤：

```bash
cd /Users/zejianchen/Desktop/claude_agent/Clawd-Code
PYTHONPATH=. python -m src.cli
```

进入 REPL 后再运行：

```text
/skills
```

确认列表中存在 `aircraft-conceptual-design`。

### 11.2 RAG 检索没有结果

先确认 `RAG-data` 存在：

```bash
ls RAG-data
```

再直接运行检索脚本：

```bash
python .clawd/skills/aircraft-design-rag/scripts/search_rag.py \
  --data-dir RAG-data \
  --query "飞机总体设计" \
  --format json \
  --top-k 3
```

如果 `hits` 为空，可以换更短、更明确的查询词，例如 `翼载荷`、`推重比`、`任务剖面`、`起飞重量`。

### 11.3 启动后立刻 Goodbye

如果在脚本化或非交互执行环境里启动 REPL，可能会因为标准输入关闭而立即退出。这不一定表示项目有问题。请在 macOS Terminal、iTerm 或真实交互终端中执行：

```bash
cd /Users/zejianchen/Desktop/claude_agent/Clawd-Code
PYTHONPATH=. python -m src.cli
```

正常情况下应停在 `❯` 提示符等待输入。

### 11.4 卡在 Thinking

如果已经看到多次 `Bash`、`Read` 工具执行成功，但最后长时间停在 `Thinking...`，通常表示工具阶段已经结束，模型正在综合一个较大的最终回答。建议优先用流式模式启动：

```bash
cd /Users/zejianchen/Desktop/claude_agent/Clawd-Code
clawd code --stream
```

或者进入 REPL 后执行：

```text
/stream on
```

该技能已经限制默认工具预算：常规任务最多 3 次 RAG 检索，完整详细报告最多 4 次检索；原文 `Read` 最多 2 个片段，每段最多 80 行。若仍然很慢，可以把任务拆成两步，先让技能输出 `需求解析、依据检索、总体参数`，再单独要求 `约束图和布局校核`。

当前版本还增加了运行时回合护栏：通过 slash 命令执行 `aircraft-conceptual-design` 时，默认最多允许 12 轮工具回合；`aircraft-design-rag` 默认最多 6 轮。达到工具回合上限后，运行时会强制进入无工具最终合成，避免技能在证据已经足够时继续长时间探索，也避免只停在内部工具调用标记而没有最终结果。

### 11.5 输出参数不够精确

这通常是因为输入缺失或本地资料没有覆盖。该技能会优先给出范围和工程假设，而不是编造精确值。想提高输出质量，可以补充巡航速度、动力形式、跑道海拔、温度、升阻比、最大升力系数、备份燃油或能量策略等信息。

### 11.6 没有生成界限线图

如果用户只问轻量问题，技能可能只输出相关子集。若明确需要图，请在调用中写清楚：

```text
输出方案界限线图，并给出 SVG 和 CSV 文件路径
```

## 12. 维护说明

当修改技能时，建议同步检查以下文件：

```text
.clawd/skills/aircraft-conceptual-design/SKILL.md
.clawd/skills/aircraft-conceptual-design/references/workflow.md
.clawd/skills/aircraft-conceptual-design/scripts/plot_constraint_boundary.py
tests/test_aircraft_conceptual_design_skill.py
```

修改后至少运行：

```bash
PYTHONPATH=. pytest -q tests/test_aircraft_conceptual_design_skill.py
```

如果改动涉及 slash 命令、技能加载器或 RAG 参数，也建议运行相关回归测试：

```bash
PYTHONPATH=. pytest -q \
  tests/test_tool_system_tools.py::TestSkillTool::test_skill_run_command_includes_retrieved_output \
  tests/test_repl.py::TestREPL::test_handle_command_project_skill_registers_and_expands_skill_dir \
  tests/test_repl.py::TestREPL::test_handle_command_skill_invokes_skill_tool_and_chats_with_prompt
```
