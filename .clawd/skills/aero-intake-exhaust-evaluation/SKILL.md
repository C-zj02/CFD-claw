---
name: aero-intake-exhaust-evaluation
description: 面向气动/进气道/排气喷管 CFD 特性评估的中文工程技能。用于用户提出 StarCCM+、OpenFOAM、MATLAB 或自研工具相关的气动评估、进排气仿真、几何模型接收、边界命名、网格与求解参数设置、dry-run/mock/execute 流程验证、配置脚本生成、仿真监测、发散提醒和结果包输出等任务。
---

# 气动/进排气特性评估

使用本技能把用户的自然语言评估需求转换为可确认、可执行、可追踪的 CFD 评估流程。默认先支持 `dry_run` 和 `mock`，在 StarCCM+、OpenFOAM、MATLAB 或甲方自研工具准备好后再切换到 `execute`。

## 工作原则

1. 先形成结构化 `case.json`，再生成任何工具配置。所有默认值必须标注为 `default_template` 或 `engineering_assumption`。
2. 外部工具不是前置依赖。没有安装工具时使用 `dry_run` 检查输入完整性、边界命名、模板参数和输出目录；使用 `mock` 生成非物理的流程演示数据。
3. 必须在关键节点记录人机确认：评估工具选择、边界命名、几何质量、网格策略、求解模型、开始执行、发散处理、最终结果输出。
4. 不把 LLM 当 CFD 求解器。LLM 负责任务解析、配置编排、质量门禁、监测解释和结果整理；流场计算由外部工具完成。
5. 涉及军用或双用途对象时，只讨论总体气动、进排气匹配、网格/求解质量和工程评估，不提供武器使用、规避或杀伤优化细节。

## 快速流程

1. **需求解析**：提取对象、几何文件、评估类型、工况、边界条件、湍流模型、定常/非定常、迭代/CFL、监测量、云图、网格数量级、加密区域、自定义变量和输出物。
2. **选择模板**：按任务选择 `assets/templates/*.json`。用户没有明确要求时，快速评估默认用 `quick_external_aero`，进气道用 `intake_duct`，喷管/排气用 `nozzle_exhaust`，高精度用 `high_fidelity_external_aero`。
3. **建立 case**：生成 `case.json`，字段规范见 `references/parameter-schema.md`。可用脚本：

```bash
python "${CLAUDE_SKILL_DIR}/scripts/case_from_template.py" --template "${CLAUDE_SKILL_DIR}/assets/templates/intake_duct.json" --case-id "<case-id>" --output "<case.json>"
```

4. **确认节点 A**：向用户确认评估目标、run_mode、工具、几何文件、边界命名、缺失输入和默认假设。边界命名规则见 `references/boundary-naming.md`。
5. **校验 case**：

```bash
python "${CLAUDE_SKILL_DIR}/scripts/validate_case.py" --case "<case.json>" --output "<validation_report.json>"
```

6. **生成工具配置草稿**：

```bash
python "${CLAUDE_SKILL_DIR}/scripts/generate_solver_config.py" --case "<case.json>" --tool all --output "<config-dir>"
```

7. **dry-run 或 mock**：`dry_run` 只输出检查报告和配置文件；`mock` 生成残差、监测量和指标示例：

```bash
python "${CLAUDE_SKILL_DIR}/scripts/mock_run.py" --case "<case.json>" --output "<run-dir>"
```

8. **结果包归档**：

```bash
python "${CLAUDE_SKILL_DIR}/scripts/write_result_bundle.py" --case "<case.json>" --run-dir "<run-dir>" --output "<bundle-dir>"
```

9. **最终回复**：说明需求解析、确认记录、生成文件、检查结果、风险项、下一步真实工具接入建议。

## 运行模式

- `dry_run`：默认模式。检查字段完整性，生成 StarCCM+/OpenFOAM/MATLAB 配置草稿，不启动外部软件。
- `mock`：生成模拟残差、监测曲线和指标表，仅用于流程验收、演示和 UI 联调。必须明确标注为非物理结果。
- `execute`：仅当用户确认工具安装路径、许可证、运行命令和工作目录后使用。执行前必须再次确认。

## 工具选择

按现有环境和甲方要求选择最小可用工具链：

- `starccm`：适合商业流程、复杂几何、自动化宏和工程团队已有 StarCCM+ 资产。需要许可证、版本和 `starccm+ -batch` 命令。
- `openfoam`：适合开源、可复现实验、Linux/WSL/Docker/HPC 流程。需要求解器、网格器和 case 字典。
- `matlab`：适合数据整理、进排气指标计算、试验/仿真曲线后处理、报告图表。通常不作为主 CFD 求解器。
- `custom`：甲方自研工具或平台。按 `references/tool-adapter-contract.md` 填写输入/输出契约。

## 人机确认点

必须主动确认或记录：

- **目标确认**：评估对象、快速/高精度、外流/进气道/喷管/耦合任务、输出文件。
- **几何确认**：几何文件路径、单位、坐标轴、对称性、是否已清理小特征。
- **边界命名确认**：远场、壁面、入口、出口、AIP/发动机面、喷管入口/喉道/出口、对称面、周期面。
- **网格确认**：数量级、边界层、y+ 目标、加密类型和区域。
- **求解确认**：定常/非定常、湍流模型、可压缩设置、CFL、迭代步数、收敛标准。
- **执行确认**：从 `dry_run/mock` 切到 `execute` 前，确认工具路径、许可证、预计耗时、输出目录和覆盖风险。
- **异常确认**：模型质量未通过、残差发散、质量不守恒、监测量振荡、结果超出经验范围。

## 参考文件

按需读取，不要一次加载全部：

- `references/workflow.md`：完整流程、质量门禁和执行状态机。
- `references/parameter-schema.md`：`case.json` 字段契约。
- `references/default-templates.md`：默认模板选择和参数解释。
- `references/boundary-naming.md`：边界命名规范。
- `references/tool-adapter-contract.md`：StarCCM+、OpenFOAM、MATLAB 和自研工具适配器契约。
- `references/output-spec.md`：结果包、指标表和报告格式。

## 输出规范

最终答复尽量使用以下结构，并按任务规模裁剪：

1. `需求解析`
2. `采用模板与默认假设`
3. `确认记录`
4. `生成的配置/脚本`
5. `校验或模拟结果`
6. `风险与待确认项`
7. `下一步工具接入`

保存文件时默认使用 `outputs/aero-intake-exhaust-evaluation/<case-id>/`，除非用户指定其他路径。不要覆盖已有结果目录，除非用户明确确认。
