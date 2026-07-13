---
name: aircraft-design-skill
description: 接入 BaiSongt/aircraft-design-skill 的可交付固定翼总体设计工具包。用于 Class I/II 重量、分段任务燃油、结构与几何闭合，有界自动修正与完整复验、阻断约束验收、气动/推进/操稳分析、外形参数化和设计报告生成。
allowed-tools:
  - Bash
  - Read
  - Glob
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

## 可交付门槛

只在以下条件同时成立时，将结果称为“可交付的初步设计候选”：

- `design_data.json.engineering_feasible` 为 `true`；
- `status.numerical_converged` 为 `true`；
- 所有 `blocking=true` 的约束均为 `passed=true`；
- 所有阻断阶段的 `stage_status.status` 均为 `completed`；
- CLI 退出码为 `0`。

退出码 `2` 表示计算完成但未收敛或工程不可行，只能作为下一轮诊断输入。不得把最后迭代值、仅通过 Class I 的结果或 Stage 7 降阶筛选候选表述为最终方案。

报告时必须列出 `design_adjustments`、约束裕度和仍未覆盖的高保真气动、详细结构/疲劳/气动弹性、系统安装、制造与适航验证缺口。

## 自动修正规则

- 用户启用 `auto_repair_enabled` 后，对未通过的阻断约束最多执行 `max_repair_attempts` 轮修正。
- 只调整 `initial_guess` 中声明的设计变量和求解设置；不得修改航程、载荷、速度、高度、起降距离等用户任务需求。
- 根据失败约束有界调整翼载、推重比、展弦比、厚度比、阻力/效率、推进耗油、重心位置和平尾容积系数。
- 每轮修正后必须从 Class I 重量闭合开始重新执行完整 Class I/II 阶段门，禁止只修改报告或结果 JSON。
- 保存每轮触发约束、原值、新值、边界、原因和复验结果。
- 搜索耗尽仍不可行时，明确输出“未找到可行解”；不得放宽约束、删除失败项或声称保证可行。
- 对尚未建模的火箭助推、伞降回收、RCS、气动弹性和适航需求，标记验证缺口，不得用自动修正代替专项模型。

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
