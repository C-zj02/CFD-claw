# 使用官方 EngDesign 评估本项目

## 目标

本次评估使用的是官方 `AGI4Engineering/EngDesign` 仓库，而不是自定义仿制任务集。流程如下：

1. 读取官方 `EngDesign-Open/<task_id>/LLM_prompt.txt`
2. 解析官方 `output_structure.py` 中的结构化输出字段
3. 使用本项目已配置的 OpenAI-compatible provider 调用模型
4. 将模型输出转换成官方 evaluator 可接收的结构
5. 调用官方 `EngDesign-Open/<task_id>/evaluate.py`
6. 按 EngDesign 风格写入 `<task_id>/logs/*.jsonl`

适配脚本：

```text
scripts/engdesign_project_eval.py
```

官方 EngDesign 已克隆到：

```text
/Users/zejianchen/Desktop/claude_agent/EngDesign
```

## 为什么需要适配脚本

官方 `evaluation/evaluate_llm.py` 是直接评模型 API 的；如果直接运行，它评的是模型本身，不是本机项目。

本项目评估需要经过项目自己的 provider 配置、模型名、base_url 和调用逻辑，因此新增桥接器 `scripts/engdesign_project_eval.py`。它仍然使用官方 EngDesign 的 prompt 和 evaluator，只是把模型调用入口换成本项目。

## 已运行任务

当前先选了两个与飞行器/航天/工程设计更接近的开放任务：

- `ZH_02`：小型航天器再入热防护半径设计
- `ZH_04`：浮力驱动水下滑翔器参数设计

## 运行命令

Dry-run 检查 prompt：

```bash
/Users/zejianchen/miniconda3/bin/python3.13 scripts/engdesign_project_eval.py \
  --engdesign-root /Users/zejianchen/Desktop/claude_agent/EngDesign \
  --task-list ZH_02 ZH_04 \
  --dry-run \
  --output-dir .clawd/generated/engdesign_project_eval_runs/dry_run_zh02_zh04
```

使用本项目配置的 `deepseek-v4-flash` 进行评估：

```bash
/Users/zejianchen/miniconda3/bin/python3.13 scripts/engdesign_project_eval.py \
  --engdesign-root /Users/zejianchen/Desktop/claude_agent/EngDesign \
  --task-list ZH_02 ZH_04 \
  --model deepseek-v4-flash \
  --model-label clawd_deepseek_v4_flash \
  --output-dir .clawd/generated/engdesign_project_eval_runs/zh02_zh04_clawd_deepseek_flash_final \
  --request-timeout 120 \
  --max-tokens 800 \
  --rename-existing-logs
```

## 当前结果

`ZH_04` 单任务评估：

```text
分数：100 / 100
结果：通过
报告：.clawd/generated/engdesign_project_eval_runs/zh02_zh04_clawd_deepseek_flash_final/report.md
```

官方 evaluator 输出：

```text
horizontal_distance_m = 4537.03
time_seconds = 4607.02
energy_required_Wh = 198.31
volume_m3 = 0.3
density_kg_per_m3 = 1000.0
passed = true
```

`ZH_02` 有效评估记录：

```text
分数：70 / 100
结果：未完全通过
报告：.clawd/generated/engdesign_project_eval_runs/zh02_zh04_clawd_deepseek_flash/report.md
```

该任务未完全通过的主要原因是热载荷约束没有满足；官方 evaluator 对 `ZH_02` 只有 100 分才算通过。

在最终合并运行中，`ZH_02` 出现了一次模型调用超时，因此最终合并报告里的 `ZH_02` 为 `error`；上面的 70 分记录来自此前一次已成功解析并进入官方 evaluator 的运行。

## 模型适配问题

`deepseek-v4-pro` 在 `ZH_02` 上多次输出长推理而不是 JSON，导致官方 evaluator 无法解析结构化结果。因此当前官方 EngDesign 评估优先使用 `deepseek-v4-flash`。

已在脚本中加入：

- 单题模型调用超时隔离
- raw response 保存
- prompt 保存
- parse error 记录
- 官方 logs 写入

## 输出位置

总报告：

```text
.clawd/generated/engdesign_project_eval_runs/<run-name>/
├── prompts/
├── raw_responses/
├── report.md
├── run_config.json
└── summary.json
```

官方任务日志：

```text
/Users/zejianchen/Desktop/claude_agent/EngDesign/EngDesign-Open/<task_id>/logs/
```

## 后续建议

如果要扩大评估范围，建议先按主题分批运行：

```bash
--task-list ZH_02 ZH_03 ZH_04 XG_13 RK_01 RK_02
```

不建议一次性跑完整 `EngDesign-Open` 67 个任务，因为成本、耗时和依赖差异都比较大；应先确认每一类任务的输出结构化稳定性。
