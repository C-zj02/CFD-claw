# 飞行性能分析数据契约

本文件用于在执行飞行性能分析前统一输入、确认记录和输出归档结构。轻量任务可只使用相关子集，完整任务应尽量填满这些字段。

## 输入台账字段

每条输入记录至少包含：

- `id`：稳定标识，例如 `aero.CLmax_landing`。
- `name`：中文名称或工程名称。
- `value`：数值、数组、表格引用或文件路径。
- `unit`：单位，量纲为 1 时写 `-`。
- `condition`：适用状态，例如 `landing flap 30 deg`、`ISA sea level`。
- `source`：`user`、`file`、`rag`、`calculated`、`assumption`。
- `status`：`confirmed`、`pending`、`assumed`、`rejected`。
- `note`：适用范围、插值方式、外推风险或版本说明。

## Bundle JSON 结构

推荐先整理为一个 JSON，再用 `scripts/write_performance_bundle.py` 归档。

```json
{
  "case": {
    "id": "uav-range-check-v1",
    "title": "无人机巡航航程性能分析",
    "goal": "计算 3000 m 高度巡航航程并检查燃油裕度",
    "aircraft_type": "fixed-wing UAV",
    "created_by": "flight-performance-analysis"
  },
  "inputs": {
    "aerodynamics": [
      {
        "id": "aero.CD0",
        "name": "零升阻力系数",
        "value": 0.032,
        "unit": "-",
        "condition": "cruise clean",
        "source": "user",
        "status": "confirmed"
      }
    ],
    "propulsion": [
      {
        "id": "prop.SFC",
        "name": "巡航耗油率",
        "value": 0.32,
        "unit": "kg/(kW*h)",
        "condition": "75% power",
        "source": "assumption",
        "status": "pending"
      }
    ],
    "weight_states": [
      {
        "id": "weight.takeoff",
        "name": "起飞重量",
        "value": 1200,
        "unit": "kg",
        "condition": "mission start",
        "source": "user",
        "status": "confirmed"
      }
    ],
    "profile_segments": [
      {
        "segment": "cruise",
        "mode": "constant altitude",
        "altitude_m": 3000,
        "speed": 58,
        "speed_unit": "m/s",
        "distance_km": 420,
        "weight_start_kg": 1120,
        "weight_end_kg": 1035,
        "status": "calculated"
      }
    ],
    "environment": [
      {
        "id": "env.atmosphere",
        "name": "大气模型",
        "value": "ISA",
        "unit": "-",
        "source": "user",
        "status": "confirmed"
      }
    ],
    "constraints": [
      {
        "id": "limit.runway",
        "name": "可用跑道长度",
        "value": 800,
        "unit": "m",
        "source": "user",
        "status": "confirmed"
      }
    ]
  },
  "results": {
    "metrics": [
      {
        "name": "巡航航程",
        "value": 435,
        "unit": "km",
        "condition": "3000 m, 58 m/s",
        "method": "Breguet range estimate",
        "status": "calculated"
      }
    ],
    "tables": [
      {
        "id": "segment_weight_trace",
        "title": "任务段重量递推",
        "columns": ["segment", "weight_start_kg", "weight_end_kg", "fuel_used_kg"],
        "rows": [
          {"segment": "cruise", "weight_start_kg": 1120, "weight_end_kg": 1035, "fuel_used_kg": 85}
        ]
      }
    ]
  },
  "figures": [
    {
      "id": "range-vs-speed",
      "title": "巡航速度对航程的影响",
      "x_label": "速度 (m/s)",
      "y_label": "航程 (km)",
      "series": [
        {"name": "估算航程", "points": [[45, 390], [55, 435], [65, 410]]}
      ]
    }
  ],
  "assumptions": [
    {
      "item": "prop.SFC",
      "value": 0.32,
      "unit": "kg/(kW*h)",
      "reason": "用户未给定发动机耗油率，先用于首轮估算",
      "status": "pending"
    }
  ],
  "confirmations": [
    {
      "stage": "输入确认",
      "summary": "用户确认起飞重量、巡航高度和巡航速度；SFC 暂按工程假设。",
      "status": "partial"
    }
  ],
  "sources": [
    {
      "title": "用户输入",
      "path": "conversation",
      "note": "起飞重量、巡航高度、巡航速度"
    }
  ]
}
```

## 输出目录约定

保存到 `outputs/performance-analysis/<case-id>/`：

- `case.json`：完整 bundle。
- `summary.md`：面向用户的摘要、输入状态、结果和风险。
- `features/aerodynamics.csv`：气动特性输入。
- `features/propulsion.csv`：动力特性输入。
- `features/weight_states.csv`：重量状态。
- `features/environment.csv`：环境条件。
- `features/constraints.csv`：限制条件。
- `profiles/profile_segments.csv`：飞行剖面。
- `results/performance_metrics.csv`：关键性能指标。
- `results/<table-id>.csv`：补充结果表。
- `figures/<figure-id>.svg`：由 bundle 中序列生成的简易图。
- `records/assumptions.csv`：工程假设。
- `records/confirmations.csv`：人机确认记录。
- `records/sources.csv`：资料和输入来源。

## 确认状态规则

- `confirmed`：用户或权威项目文件已确认，可直接用于正式计算。
- `pending`：等待用户确认，不应作为最终结论依据。
- `assumed`：已明确标为工程假设，可用于方案探索，但最终报告必须突出风险。
- `calculated`：由确认输入计算得到，需能追溯公式或脚本。
- `rejected`：已废弃或被用户否定，保留在记录中但不参与计算。
