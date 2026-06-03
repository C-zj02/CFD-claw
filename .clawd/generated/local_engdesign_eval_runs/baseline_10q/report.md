# EngDesign-style 本机飞行器设计评测报告

- 运行时间：2026-05-31T16:58:52
- 数据文件：`/Users/zejianchen/Desktop/claude_agent/Clawd-Code/.clawd/generated/aircraft_conceptual_design_10q_answers.json`
- 任务目录：`/Users/zejianchen/Desktop/claude_agent/Clawd-Code/benchmarks/aircraft_design_engdesign/tasks`
- 平均分：74.4
- 通过数：8 / 10

| Task | Score | Passed | Status | Log |
|---|---:|:---:|---|---|
| AD_01 | 80.61 | 是 | ok | `/Users/zejianchen/Desktop/claude_agent/Clawd-Code/benchmarks/aircraft_design_engdesign/tasks/AD_01/logs/AD_01_log_baseline_10q_0.jsonl` |
| AD_02 | 76.67 | 是 | ok | `/Users/zejianchen/Desktop/claude_agent/Clawd-Code/benchmarks/aircraft_design_engdesign/tasks/AD_02/logs/AD_02_log_baseline_10q_1.jsonl` |
| AD_03 | 73.81 | 是 | ok | `/Users/zejianchen/Desktop/claude_agent/Clawd-Code/benchmarks/aircraft_design_engdesign/tasks/AD_03/logs/AD_03_log_baseline_10q_2.jsonl` |
| AD_04 | 66.35 | 否 | ok | `/Users/zejianchen/Desktop/claude_agent/Clawd-Code/benchmarks/aircraft_design_engdesign/tasks/AD_04/logs/AD_04_log_baseline_10q_3.jsonl` |
| AD_05 | 65.16 | 否 | ok | `/Users/zejianchen/Desktop/claude_agent/Clawd-Code/benchmarks/aircraft_design_engdesign/tasks/AD_05/logs/AD_05_log_baseline_10q_4.jsonl` |
| AD_06 | 72.86 | 是 | ok | `/Users/zejianchen/Desktop/claude_agent/Clawd-Code/benchmarks/aircraft_design_engdesign/tasks/AD_06/logs/AD_06_log_baseline_10q_5.jsonl` |
| AD_07 | 74.05 | 是 | ok | `/Users/zejianchen/Desktop/claude_agent/Clawd-Code/benchmarks/aircraft_design_engdesign/tasks/AD_07/logs/AD_07_log_baseline_10q_6.jsonl` |
| AD_08 | 72.14 | 是 | ok | `/Users/zejianchen/Desktop/claude_agent/Clawd-Code/benchmarks/aircraft_design_engdesign/tasks/AD_08/logs/AD_08_log_baseline_10q_7.jsonl` |
| AD_09 | 82.38 | 是 | ok | `/Users/zejianchen/Desktop/claude_agent/Clawd-Code/benchmarks/aircraft_design_engdesign/tasks/AD_09/logs/AD_09_log_baseline_10q_8.jsonl` |
| AD_10 | 79.92 | 是 | ok | `/Users/zejianchen/Desktop/claude_agent/Clawd-Code/benchmarks/aircraft_design_engdesign/tasks/AD_10/logs/AD_10_log_baseline_10q_9.jsonl` |

## 说明

该评测按 EngDesign 的任务组织方式落盘：每个任务包含 `LLM_prompt.txt`、`output_structure.py`、`evaluate.py` 和 `logs/*.jsonl`。当前驱动评测的是本机已保存回答，不直接调用模型 API。
