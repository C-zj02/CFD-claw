# 外部 EngDesign 评估功能说明

## 目标

本次实现不把 EngDesign 评估接入 Clawd 的前端、智能体运行时或 `src` 模块，而是在项目外层增加一个独立脚本：

```bash
scripts/engdesign_eval_runner.py
```

它的定位是“外部评估工具”：给定本地克隆的 `AGI4Engineering/EngDesign` 仓库路径后，生成并执行官方 `evaluation/evaluate_llm.py` 命令，然后把本次运行的命令、配置、终端输出和汇总结果归档到 `.clawd/generated/engdesign_eval_runs/`。

## 前置准备

先准备 EngDesign 仓库和 Docker 镜像：

```bash
git clone https://github.com/AGI4Engineering/EngDesign.git
cd EngDesign
docker build -t engdesign-sim .
```

如果使用 DeepSeek，建议把密钥放到环境变量里：

```bash
export DEEPSEEK_API_KEY="你的密钥"
```

脚本会根据模型名自动选择默认密钥变量：

- `deepseek*` 使用 `DEEPSEEK_API_KEY`
- `gemini*` 使用 `GEMINI_API_KEY`
- `claude*` 使用 `ANTHROPIC_API_KEY`
- 其他默认使用 `OPENAI_API_KEY`

## 只生成命令不执行

可以先用 dry-run 检查命令是否正确：

```bash
python3 scripts/engdesign_eval_runner.py run \
  --engdesign-root /path/to/EngDesign \
  --model deepseek-v4-pro \
  --api-key-env DEEPSEEK_API_KEY \
  --task-list AB_01 AB_02 \
  --k 1 \
  --docker \
  --dry-run
```

dry-run 会生成：

```text
.clawd/generated/engdesign_eval_runs/run_<时间>/
├── command.txt
└── run_config.json
```

`command.txt` 里的 API key 会被替换成 `***`，避免明文落盘。

## 正式执行评估

推荐使用 Docker 执行，这和 EngDesign 官方说明一致：

```bash
python3 scripts/engdesign_eval_runner.py run \
  --engdesign-root /path/to/EngDesign \
  --model deepseek-v4-pro \
  --api-key-env DEEPSEEK_API_KEY \
  --task-list AB_01 AB_02 \
  --k 1 \
  --docker \
  --rename-existing-logs
```

`--rename-existing-logs` 会先把被测任务目录里的原始 `logs` 文件夹重命名，避免官方示例日志和本次新跑结果混在一起。

正式执行后会生成：

```text
.clawd/generated/engdesign_eval_runs/run_<时间>/
├── command.txt
├── run.log
├── run_config.json
└── summary.json
```

其中：

- `command.txt` 是本次执行命令。
- `run.log` 是命令行输出。
- `run_config.json` 是运行配置。
- `summary.json` 是按任务聚合后的评估结果。

## 汇总已有日志

如果已经跑过 EngDesign，也可以只汇总已有日志：

```bash
python3 scripts/engdesign_eval_runner.py summarize \
  --engdesign-root /path/to/EngDesign \
  --model deepseek-v4-pro \
  --task-list AB_01 AB_02
```

汇总结果包含：

- 总任务数
- trial 数量
- 通过数量
- 有分数的 trial 数
- trial 平均分
- 按任务平均分
- 每个任务下各日志文件的分数、通过状态和 token 数

## 设计取舍

该功能刻意保持为独立脚本，有三个原因：

1. EngDesign 评估依赖 Docker、第三方 API key 和任务目录结构，不适合直接塞进网页端交互流程。
2. 评估输出是实验数据，应该归档到 `.clawd/generated/`，和业务会话记录、前端历史记录分开。
3. 后续如果换评估集或换模型，只需要调整命令参数，不会影响飞行器设计智能体的正常使用。
