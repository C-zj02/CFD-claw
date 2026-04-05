"""
Microcompact: lightweight message pre-processing.

Strips images/documents from messages and clears old tool results
when the cache is cold (time-based trigger). This reduces tokens
sent to the API without losing the model-visible history structure.
"""

from __future__ import annotations

from typing import Any

# Token size estimate for images/documents in tool results
IMAGE_TOKEN_SIZE = 2000

# Marker inserted for content-cleared tool results
CLEARED_MESSAGE = "[Old tool result content cleared]"

# Tools eligible for microcompact (same as TypeScript COMPACTABLE_TOOLS)
COMPACTABLE_TOOL_NAMES: frozenset[str] = frozenset([
    "Read",
    "Bash",
    "Shell",
    "Grep",
    "Glob",
    "WebSearch",
    "WebFetch",
    "Edit",
    "Write",
])


def count_tool_result_tokens(block: dict[str, Any]) -> int:
    """Count estimated tokens in a tool_result block."""
    content = block.get("content", "")
    if isinstance(content, str):
        from ..token_estimation import rough_token_count
        return rough_token_count(content)
    if isinstance(content, list):
        total = 0
        for item in content:
            if isinstance(item, dict):
                if item.get("type") in ("image", "document"):
                    total += IMAGE_TOKEN_SIZE
                elif item.get("type") == "text":
                    from ..token_estimation import rough_token_count
                    total += rough_token_count(item.get("text", ""))
        return total
    return 0


def is_compactable_tool(tool_name: str) -> bool:
    """Check if a tool is eligible for microcompact."""
    return tool_name in COMPACTABLE_TOOL_NAMES


def strip_images_from_messages(messages: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """
    Strip image/document blocks from user messages.

    Replaces them with [image] / [document] text markers.
    """
    result: list[dict[str, Any]] = []
    for msg in messages:
        if msg.get("role") != "user":
            result.append(msg)
            continue

        content = msg.get("content", "")
        if isinstance(content, str):
            result.append(msg)
            continue

        if not isinstance(content, list):
            result.append(msg)
            continue

        new_content: list[Any] = []
        changed = False
        for block in content:
            if not isinstance(block, dict):
                new_content.append(block)
                continue

            block_type = block.get("type", "")
            if block_type == "image":
                changed = True
                new_content.append({"type": "text", "text": "[image]"})
            elif block_type == "document":
                changed = True
                new_content.append({"type": "text", "text": "[document]"})
            elif block_type == "tool_result" and isinstance(block.get("content"), list):
                # Strip nested images/documents from tool_result content
                new_tool_content: list[Any] = []
                tool_changed = False
                for item in block["content"]:
                    if isinstance(item, dict) and item.get("type") in ("image", "document"):
                        tool_changed = True
                        new_tool_content.append({"type": "text", "text": f"[{item['type']}]"})
                    else:
                        new_tool_content.append(item)
                if tool_changed:
                    changed = True
                    new_block = {**block, "content": new_tool_content}
                    new_content.append(new_block)
                else:
                    new_content.append(block)
            else:
                new_content.append(block)

        if changed:
            result.append({**msg, "content": new_content})
        else:
            result.append(msg)

    return result


def microcompact_messages(
    messages: list[dict[str, Any]],
    keep_recent: int = 3,
) -> tuple[list[dict[str, Any]], int]:
    """
    Lightweight compact of old tool results.

    Clears content from compactable tool results beyond the most recent
    `keep_recent` ones. This mirrors the TypeScript time-based microcompact
    (without the time-gate, for simplicity).

    Returns:
        Tuple of (modified_messages, tokens_saved)
    """
    # Collect compactable tool_use IDs in order
    compactable_ids: list[str] = []
    for msg in messages:
        content = msg.get("content", [])
        if msg.get("type") == "assistant" and isinstance(content, list):
            for block in content:
                if (
                    isinstance(block, dict)
                    and block.get("type") == "tool_use"
                    and is_compactable_tool(block.get("name", ""))
                ):
                    compactable_ids.append(block.get("id", ""))

    # Keep the last N compactable tool results
    if len(compactable_ids) <= keep_recent:
        return list(messages), 0

    keep_set = set(compactable_ids[-keep_recent:])
    clear_set = set(compactable_ids[:-keep_recent])

    tokens_saved = 0
    result: list[dict[str, Any]] = []

    for msg in messages:
        if msg.get("role") != "user":
            result.append(msg)
            continue

        content = msg.get("content", "")
        if isinstance(content, str):
            result.append(msg)
            continue

        if not isinstance(content, list):
            result.append(msg)
            continue

        new_content: list[Any] = []
        changed = False
        for block in content:
            if (
                isinstance(block, dict)
                and block.get("type") == "tool_result"
                and block.get("tool_use_id") in clear_set
                and block.get("content") != CLEARED_MESSAGE
            ):
                saved = count_tool_result_tokens(block)
                tokens_saved += saved
                changed = True
                new_content.append({**block, "content": CLEARED_MESSAGE})
            else:
                new_content.append(block)

        if changed:
            result.append({**msg, "content": new_content})
        else:
            result.append(msg)

    return result, tokens_saved
