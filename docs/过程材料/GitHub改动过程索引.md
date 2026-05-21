# GitHub 改动过程索引

本文档按最近几次 GitHub 提交整理飞行器设计功能的研发过程，重点说明每次改动的动机、实现范围、验证方式和对后续研发的意义。

## 时间线

| 时间 | 提交 | 改动主题 | 研发目标 |
|------|------|----------|----------|
| 2026-05-20 16:55 | `6e0b9b3` | Optimize aircraft design web UI | 将原始网页端改造成面向飞行器设计的中文工作台。 |
| 2026-05-20 16:58 | `5bf2bb7` | Enhance aircraft design skill runtime | 让飞行器设计技能在 DeepSeek/OpenAI-compatible 模型下稳定运行。 |
| 2026-05-20 16:59 | `b9a9170` | Add aircraft design generated artifacts | 固化示范数据、10 问测试结果、约束图和生成脚本。 |
| 2026-05-20 18:21 | `48ba84c` | Disable default web auto skill | 网页端默认不自动使用技能，避免用户误触发资料检索。 |
| 2026-05-20 18:43 | `2fa162a` | Hide RAG internals from aircraft design web UI | 前端只显示“飞行器设计”，隐藏内部资料检索实现。 |
| 2026-05-20 19:05 | `4b98cdb` | Fix web stream completion state | 修复 SSE 完成后前端仍等待连接关闭的问题。 |
| 2026-05-20 19:33 | `67fe444` | Render LaTeX in web chat messages | 让网页回答中的公式显示为公式样式。 |

## 改动主线

这组提交可以归纳为四条主线。

第一条是领域化：把通用 Clawd Code 网页端改成飞行器设计工作台，固定模型为 `deepseek-v4-pro`，界面语言改为中文，并围绕总体方案、约束分析、动力布局、本地资料证据组织交互。

第二条是工程稳定性：增强技能运行时、限制工具回合、处理 DeepSeek DSML 工具调用格式、修复网页端流式结束状态，目标是让长链路设计任务能完成并返回最终答案。

第三条是产品抽象：前端不暴露 `aircraft-design-rag`、RAG 参数、内部缓存等工程细节，只给用户一个可理解的“飞行器设计”能力入口。

第四条是可交付验证：将 10 个飞行器设计问题、DeepSeek 输出、局部调用结果、约束界限线图、CSV/SVG/JSON 等生成物纳入仓库，便于复现实验。

## 验证总览

| 验证项 | 命令或方法 | 覆盖内容 |
|--------|------------|----------|
| Python 语法检查 | `python -m py_compile src/web/app.py` | 网页端 HTML/JS 嵌入 Python 字符串后的语法完整性。 |
| 网页服务测试 | `python -m pytest tests/test_web.py` | 会话创建、技能名映射、内部参数隐藏、流式响应。 |
| 技能测试 | `python -m pytest tests/test_aircraft_conceptual_design_skill.py` | 飞行器设计技能发现、提示词和检索链路。 |
| Agent Loop 测试 | `python -m pytest tests/test_agent_loop.py` | 工具调用、最终合成、回合控制。 |
| Provider 测试 | `python -m pytest tests/test_providers.py` | DeepSeek/OpenAI-compatible 工具调用解析和流式行为。 |
| 本地网页启动 | `python -m src.cli web --host 127.0.0.1 --port 8081` | 浏览器端初始化、中文界面、模型与能力显示。 |

## 提交说明建议

后续如果把过程文档一起提交，可以使用类似提交信息：

```text
Document aircraft design development process

Add process notes for recent GitHub changes covering the aircraft design web UI,
runtime stability work, generated artifacts, capability abstraction, streaming
fixes, and LaTeX rendering.
```
