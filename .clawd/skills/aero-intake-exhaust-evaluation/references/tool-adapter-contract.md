# 工具适配器契约

所有外部工具适配器都围绕 `case.json` 工作。适配器必须能在未安装工具时生成配置草稿，在安装工具后切换到真实执行。

## 统一输入

- `case.json`
- 几何文件列表
- 模板名和默认假设
- 输出目录
- `run_mode`: `dry_run`、`mock`、`execute`

## 统一输出

- `resolved_case.json`：模板和用户输入合并后的 case。
- `configs/`：工具配置、脚本、字典或宏。
- `run/`：日志、残差、监测量。
- `results/`：指标 CSV、云图、切片数据。
- `summary.md`：摘要报告。
- `manifest.json`：文件清单和状态。

## StarCCM+

输入草稿：

- Java macro：建立导入、网格、物理模型、边界、监测和报告的骨架。
- batch 命令草稿：`starccm+ -batch run_starccm.java -np <n> <case.sim>`。

真实执行前确认：

- StarCCM+ 版本。
- 许可证是否可用。
- `starccm+` 命令或安装路径。
- 是否已有 `.sim` 模板。
- 几何导入和边界命名是否可通过宏访问。

## OpenFOAM

输入草稿：

- `system/controlDict`
- `system/fvSchemes`
- `system/fvSolution`
- `system/decomposeParDict`
- `constant/transportProperties`
- `README_OPENFOAM.md`

真实执行前确认：

- Windows 使用 WSL、Docker 还是 Linux/HPC。
- OpenFOAM 版本。
- 网格来源：snappyHexMesh、cfMesh、外部网格或已存在 mesh。
- 求解器：`rhoSimpleFoam`、`rhoPimpleFoam`、`simpleFoam` 等。

## MATLAB

输入草稿：

- `postprocess_case.m`
- 读取 monitors.csv、metrics.csv。
- 计算自定义变量、绘图并导出表格。

真实执行前确认：

- MATLAB 版本。
- `matlab -batch` 是否可用。
- 是否需要特定 toolbox。

## custom

自研工具适配器需要补齐：

```json
{
  "tool_name": "customer_cfd",
  "input_files": ["case.json", "mesh.xxx"],
  "config_format": "json|yaml|ini|template",
  "run_command": "...",
  "monitor_files": ["residual.csv"],
  "result_files": ["metrics.csv"],
  "success_criteria": ["exit_code=0", "residual_target", "mass_balance"]
}
```

不要把自研工具的路径、许可证、服务器地址写死在 skill 中，应放在用户环境配置或 case 的 `toolchain` 字段里。

