# 输出规范

默认结果目录：

```text
outputs/aero-intake-exhaust-evaluation/<case-id>/
  case.json
  validation_report.json
  configs/
  run/
  results/
  figures/
  summary.md
  manifest.json
```

## 指标表 metrics.csv

建议列：

- `metric`
- `value`
- `unit`
- `source`
- `status`
- `note`

常用指标：

- 外流：`CL`、`CD`、`Cm`、`CY`、`Cl`、`Cn`。
- 进气道：`mass_flow`、`total_pressure_recovery`、`distortion`、`aip_uniformity`。
- 喷管：`gross_thrust`、`thrust_coefficient`、`exit_pressure_ratio`、`exit_mach_uniformity`。
- 守恒：`mass_balance_error_percent`。

## 监测量 monitors.csv

建议列：

- `iteration`
- `monitor`
- `value`
- `unit`

或使用宽表：

- `iteration`
- `continuity`
- `x_momentum`
- `energy`
- `mass_flow`
- `total_pressure_recovery`

## summary.md

摘要必须包含：

1. 任务目标和工况。
2. 工具链和 run_mode。
3. 模板、默认值和假设。
4. 边界命名与质量门禁状态。
5. 生成的配置文件。
6. dry-run 检查或 mock 结果。
7. 风险项和真实执行前待确认项。

## 状态标记

- `ok`：检查通过。
- `warning`：可继续，但存在工程风险或默认假设。
- `blocked`：缺失关键输入，不应执行。
- `mock`：非物理模拟数据。
- `pending_confirmation`：等待用户确认。

