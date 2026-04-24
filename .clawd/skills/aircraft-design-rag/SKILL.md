---
name: aircraft-design-rag
description: Retrieve and answer from the local RAG-data Markdown corpus for aircraft, missile, rocket, propulsion, engine, and aerospace design questions. Use when the user asks domain questions that should be grounded in local project knowledge instead of model memory.
allowed-tools:
  - Bash
  - Read
  - Glob
arguments: [query]
run-command: python ${CLAUDE_SKILL_DIR}/scripts/search_rag.py --data-dir ${CLAUDE_PROJECT_DIR}/RAG-data --query $ARGUMENTS
---

Use the local Markdown corpus under the project `RAG-data` directory as the primary knowledge base.

Workflow:

1. Clawd runs the retriever automatically before the model answers. Use the returned command output as the evidence:
   `python "${CLAUDE_SKILL_DIR}/scripts/search_rag.py" --data-dir "${CLAUDE_PROJECT_DIR}/RAG-data" --query "$ARGUMENTS"`
2. If the query contains an exact model or engine designation such as `YF-21`, `RD-170`, or `Orion 50`, search with that exact designation first.
3. If the first retrieval is weak, try one or two shorter alternate queries built from the user's core technical terms.
4. Read the top returned file and line ranges when you need more context or a cleaner excerpt.
5. Answer only from retrieved evidence. Do not fill gaps with unsupported background knowledge.
6. If the corpus still does not contain the answer, say clearly that the answer was not found in `RAG-data`.

Output requirements:

- Answer in Chinese by default.
- Keep the main answer concise and grounded.
- End with a `依据` section that lists the file paths and line ranges you used.
