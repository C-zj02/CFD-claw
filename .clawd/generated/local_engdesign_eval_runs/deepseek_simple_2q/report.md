# EngDesign-style 本机飞行器设计评测报告

- 运行时间：2026-05-31T16:59:13
- 数据文件：`/Users/zejianchen/Desktop/claude_agent/Clawd-Code/.clawd/generated/deepseek_aircraft_conceptual_design_10q_simple.json`
- 任务目录：`/Users/zejianchen/Desktop/claude_agent/Clawd-Code/benchmarks/aircraft_design_engdesign/tasks`
- 平均分：95.66
- 通过数：2 / 2

| Task | Score | Passed | Status | Log |
|---|---:|:---:|---|---|
| AD_01 | 97.28 | 是 | ok | `/Users/zejianchen/Desktop/claude_agent/Clawd-Code/benchmarks/aircraft_design_engdesign/tasks/AD_01/logs/AD_01_log_deepseek_simple_0.jsonl` |
| AD_02 | 94.05 | 是 | ok | `/Users/zejianchen/Desktop/claude_agent/Clawd-Code/benchmarks/aircraft_design_engdesign/tasks/AD_02/logs/AD_02_log_deepseek_simple_1.jsonl` |

## 说明

该评测按 EngDesign 的任务组织方式落盘：每个任务包含 `LLM_prompt.txt`、`output_structure.py`、`evaluate.py` 和 `logs/*.jsonl`。当前驱动评测的是本机已保存回答，不直接调用模型 API。
