# 本机 EngDesign 风格评测说明

## 目标

本评测把当前项目里的“飞行器总体设计”能力整理成类似 EngDesign 的任务结构。它不接入网页端，也不改智能体主流程，而是作为独立 benchmark 放在：

```text
benchmarks/aircraft_design_engdesign/
```

每道题一个任务目录，包含：

```text
tasks/AD_01/
├── LLM_prompt.txt
├── output_structure.py
├── evaluate.py
├── rubric.json
└── logs/
```

这与 EngDesign 的核心思想一致：每个任务有输入提示、输出结构、独立评价器和本地日志。

如果需要调用官方 `AGI4Engineering/EngDesign` 的任务与 evaluator，请看：

```text
docs/过程材料/使用官方EngDesign评估本项目.md
```

## 当前任务集

当前整理了 10 个本机飞行器设计任务：

- `AD_01`：1200km 航程、500kg 载荷固定翼无人机总体方案
- `AD_02`：V0 到 V2 的重量与参数闭合
- `AD_03`：600m 跑道起降约束分析
- `AD_04`：长航程货运无人机总体布局与三视图参数
- `AD_05`：活塞、涡桨、混合电推进方案比较
- `AD_06`：巡航高度从 5000m 到 8000m 的性能校核
- `AD_07`：载荷从 500kg 到 800kg 的约束变化
- `AD_08`：方案界限线图、SVG 和 CSV 路径
- `AD_09`：精简输出设计推理、依据、参数和校核
- `AD_10`：工程落地版本、输入/假设/计算结果/风险

## 评测方式

当前驱动脚本评测的是本机已经保存的回答 JSON，不直接调用模型 API：

```bash
python3 benchmarks/aircraft_design_engdesign/evaluate_outputs.py \
  --source .clawd/generated/aircraft_conceptual_design_10q_answers.json \
  --model-label baseline_10q \
  --output-dir .clawd/generated/local_engdesign_eval_runs/baseline_10q \
  --rename-existing-logs
```

如果要评测已有 DeepSeek 生成结果：

```bash
python3 benchmarks/aircraft_design_engdesign/evaluate_outputs.py \
  --source .clawd/generated/deepseek_aircraft_conceptual_design_10q_simple.json \
  --model-label deepseek_simple \
  --task-list AD_01 AD_02 \
  --output-dir .clawd/generated/local_engdesign_eval_runs/deepseek_simple_2q
```

如果后续生成了完整 10 题结果，只需要去掉 `--task-list`：

```bash
python3 benchmarks/aircraft_design_engdesign/evaluate_outputs.py \
  --source .clawd/generated/deepseek_aircraft_conceptual_design_10q_simple.json \
  --model-label deepseek_full_10q \
  --output-dir .clawd/generated/local_engdesign_eval_runs/deepseek_full_10q
```

## 输出位置

每个任务自己的日志会写入对应任务目录：

```text
benchmarks/aircraft_design_engdesign/tasks/AD_01/logs/AD_01_log_<model-label>_0.jsonl
```

总报告会写入：

```text
.clawd/generated/local_engdesign_eval_runs/<run-name>/
├── report.md
├── run_config.json
├── source_answers.json
└── summary.json
```

`logs/*.jsonl` 的字段风格与 EngDesign 类似：

```json
{
  "completion_tokens": 0,
  "response": "...",
  "passed": true,
  "evaluation_result": {},
  "score": 80.61
}
```

## 已完成的本机评测

已对本机 10 条示范回答运行：

```text
平均分：74.4
通过数：8 / 10
报告：.clawd/generated/local_engdesign_eval_runs/baseline_10q/report.md
```

已对现有 DeepSeek 两条完整回答运行：

```text
平均分：95.66
通过数：2 / 2
报告：.clawd/generated/local_engdesign_eval_runs/deepseek_simple_2q/report.md
```

## 评价指标

每个任务的 `rubric.json` 定义任务要求，`evaluate.py` 调用公共评价内核检查：

- 基础可读性
- 题目要点覆盖
- 工程维度覆盖
- 数值、单位和公式
- 工程可追溯性
- 图表与文件引用
- 输出约束遵守
- 过程可见性

这套评测是本机确定性规则评测，适合快速回归和开发对比；如果要接近论文级 benchmark，还需要加入人工标注答案、专家评分或 LLM-as-judge 的复核层。
