---
name: aircraft-design-skill
description: 接入 BaiSongt/aircraft-design-skill 的固定翼飞机总体设计与分析工具包。用于固定翼总体设计、Class I/II 重量闭合、约束分析、初步性能、气动/推进/操稳/结构子模块调用、外形参数化和设计报告生成。
when_to_use: 用户明确要求使用 aircraft-design-skill、BaiSongt/aircraft-design-skill、固定翼总体设计工具包、Class I/II 总体设计闭环、固定翼约束分析、重量闭合、参数化几何、OpenVSP/可视化相关流程时使用。
allowed-tools:
  - Bash
  - Read
  - Glob
arguments: [design_request]
max-turns: 100
---

# Aircraft Design Skill 项目入口

本技能是当前项目对 GitHub 仓库 `BaiSongt/aircraft-design-skill` 的集成入口。上游代码已同步到：

```text
${CLAUDE_PROJECT_DIR}/external/aircraft-design-skill
```

上游 Trae 风格子技能位于：

```text
${CLAUDE_PROJECT_DIR}/external/aircraft-design-skill/.trae/skills
```

## 能力边界

该工具包主要面向固定翼飞机设计，覆盖：

- Class I / Class II 总体重量估算与闭合；
- 起飞、着陆、爬升、巡航、机动等约束分析；
- 固定翼总体设计点选择；
- 气动、推进、性能、稳定操纵、结构载荷等初步分析；
- 参数化几何、外形建模、OpenVSP 桥接和可视化；
- 设计报告、设计数据和图表输出。

当前项目中原有的 `aircraft-conceptual-design` 仍然是本项目自己的 RAG 增强总体设计 Skill；本技能用于调用和参考外部 `BaiSongt/aircraft-design-skill` 工具包，两者不要混淆。

## 首要动作

收到 `$ARGUMENTS` 后，先判断用户需要哪类能力：

1. 若用户只是问“这个 skill 是什么、怎么用”，读取上游 `README.md` 和 `.trae/skills/README.md` 后说明。
2. 若用户要运行固定翼总体设计闭环，优先读取：
   - `external/aircraft-design-skill/.trae/skills/00_entry/overall_sizing_runbook/SKILL.md`
   - `external/aircraft-design-skill/.trae/skills/00_entry/overall_sizing_spec/SKILL.md`
3. 若用户要查某个子模块，按上游 `.trae/skills/README.md` 的阶段分类读取对应 `SKILL.md`。
4. 若用户要直接执行代码，先做环境检查，不要直接假设完整 GUI/可视化依赖已经安装。

## 环境检查

该上游仓库需要 Python 3.10+。当前 macOS 系统自带 `/usr/bin/python3` 可能是 Python 3.9，不能直接运行该仓库全部代码。执行前先检查：

```bash
python3 --version
```

若系统 Python 低于 3.10，使用项目可用的高版本 Python，例如 Codex bundled Python 或用户虚拟环境。

检查导入：

```bash
PYTHONPATH="${CLAUDE_PROJECT_DIR}/external/aircraft-design-skill" python3 - <<'PY'
from aircraft_design.class2_preliminary.design_loop_orchestrator import DesignRequirements, InitialGuess, sizing_loop
print("aircraft-design-skill core import ok")
PY
```

完整 `run_sizing` 入口还需要 `numpy`、`scipy`、`matplotlib`，可视化模式还需要 `PySide6`、`PySide6-Addons`、`pyvista`、`pyvistaqt`。若缺依赖，先说明缺失项，再建议安装方式。

## 推荐命令

在项目根目录运行：

```bash
cd "${CLAUDE_PROJECT_DIR}/external/aircraft-design-skill"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

如果只做纯计算、不启用 GUI，可先从核心模块和测试级输入开始，减少 GUI 依赖风险。

运行固定翼总体设计闭环的上游入口是：

```bash
PYTHONPATH="${CLAUDE_PROJECT_DIR}/external/aircraft-design-skill" python3 -m aircraft_design.class2_preliminary.run_sizing <input.json> --project-name "<project_name>" --output-dir "<output_dir>" --no-viz
```

注意：上游 README 中部分命令写作 `python -m aircraft_design.run_sizing`，但当前同步版本实际存在的入口是：

```text
aircraft_design/class2_preliminary/run_sizing.py
```

因此优先使用：

```bash
python3 -m aircraft_design.class2_preliminary.run_sizing
```

## 输出要求

回答用户时应给出：

- 使用了哪个上游子技能或代码模块；
- 输入 JSON 或关键字段如何构造；
- 是否实际运行了工具；
- 若运行成功，列出输出目录、`design_data.json`、`design_report.md` 等结果；
- 若运行失败，说明是 Python 版本、依赖缺失、输入不合法，还是上游代码问题；
- 不要把外部工具包输出与本项目 RAG 增强总体设计输出混为一谈。

## 重要文件

```text
external/aircraft-design-skill/README.md
external/aircraft-design-skill/.trae/skills/README.md
external/aircraft-design-skill/.trae/skills/00_entry/overall_sizing_runbook/SKILL.md
external/aircraft-design-skill/.trae/skills/00_entry/overall_sizing_spec/SKILL.md
external/aircraft-design-skill/aircraft_design/class2_preliminary/run_sizing.py
external/aircraft-design-skill/aircraft_design/class2_preliminary/design_loop_orchestrator.py
external/aircraft-design-skill/examples/
```
