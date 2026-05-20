---
name: aircraft-design-rag
description: Retrieve and answer from the local RAG-data Markdown corpus for aircraft, missile, rocket, propulsion, engine, and aerospace design questions. Use when the user asks domain questions that should be grounded in local project knowledge instead of model memory.
allowed-tools:
  - Bash
  - Read
  - Glob
arguments: [query]
max-turns: 6
run-command: python ${CLAUDE_SKILL_DIR}/scripts/search_rag.py --data-dir ${CLAUDE_PROJECT_DIR}/RAG-data --query $ARGUMENTS --format json --use-cache --top-k 8 --max-snippet-chars 700
---

Use the local Markdown corpus under the project `RAG-data` directory as the primary knowledge base.

Workflow:

1. Clawd runs the retriever automatically before the model answers. Use the returned command output as the evidence:
   `python "${CLAUDE_SKILL_DIR}/scripts/search_rag.py" --data-dir "${CLAUDE_PROJECT_DIR}/RAG-data" --query "$ARGUMENTS" --format json --use-cache --top-k 8 --max-snippet-chars 700`
2. If the query contains an exact model or engine designation such as `YF-21`, `RD-170`, or `Orion 50`, search with that exact designation first.
3. If the first retrieval is weak, try one or two shorter alternate queries built from the user's core technical terms.
4. Use the JSON `hits` array as structured evidence. Each hit includes `file`, `start_line`, `end_line`, `heading`, `score`, and `snippet`.
5. Answer only from retrieved evidence. Do not fill gaps with unsupported background knowledge.
6. If the corpus still does not contain the answer, say clearly that the answer was not found in `RAG-data`.

Answer requirements:

- Answer in Chinese by default.
- Do not merely summarize that "many aspects should be considered". Give a direct, useful engineering answer.
- For broad design questions such as "如何设计一个好的发动机", organize the answer as:
  1. `先定义任务和指标`: state the mission/application, thrust or shaft power, fuel consumption, envelope, life, reliability, maintainability, cost, and integration constraints.
  2. `总体方案权衡`: explain the cycle/architecture choice and the trade-offs among performance, weight, temperature, pressure ratio, cooling, complexity, reliability, and maintainability.
  3. `核心子系统设计`: cover inlet/fan/compressor, combustor, turbine, nozzle, control/fuel, cooling/air system, lubrication/accessories, structure/rotor dynamics, materials, and sensors/health monitoring when evidence supports them.
  4. `限制与验证`: include operating limits, stability margin, strength/thermal/vibration margins, reliability and maintainability targets, rig tests, ground tests, and iterative verification.
  5. `可执行检查清单`: end the main answer with concrete checklist items or next design steps.
- If the retrieved evidence is sparse, still synthesize a structured answer from the retrieved evidence, and explicitly mark unsupported gaps as `资料未覆盖`.
- End with an `依据` section that lists the file paths and line ranges you used.
