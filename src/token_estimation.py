"""
Token estimation utilities.

Uses tiktoken when available (cl100k_base for GPT-4 / Claude-compatible models),
with a character-based fallback for other encodings or when tiktoken is absent.
"""

from __future__ import annotations

import logging
from typing import Any, Optional

logger = logging.getLogger(__name__)

# Module-level encoder cache
_encoder_cache: Optional[object] = None
_encoder_name: Optional[str] = None


def _load_tiktoken(encoding: str = "cl100k_base") -> Optional[object]:
    """Load tiktoken encoder, returning None if unavailable."""
    try:
        import tiktoken
        return tiktoken.get_encoding(encoding)
    except Exception:
        return None


def _get_encoder() -> tuple[Optional[object], str]:
    """Get the cached tiktoken encoder, lazily initialized."""
    global _encoder_cache, _encoder_name
    if _encoder_cache is None:
        _encoder_cache = _load_tiktoken()
        _encoder_name = "cl100k_base" if _encoder_cache else "char_fallback"
    return _encoder_cache, _encoder_name


def count_tokens(text: str) -> int:
    """
    Count tokens in a string using tiktoken (cl100k_base).

    Falls back to character-based estimation (chars / 4.0) if tiktoken
    is not available.
    """
    if not text:
        return 0
    encoder, _ = _get_encoder()
    if encoder is not None:
        try:
            return len(encoder.encode(text))
        except Exception:
            pass
    return max(1, len(text) // 4)


def count_messages_tokens(messages: list[dict[str, Any]]) -> int:
    """
    Count tokens for a list of messages in API format.

    Each message is a dict with 'role' and 'content' (str or list of blocks).
    """
    total = 0
    for msg in messages:
        role = msg.get("role", "")
        total += count_tokens(role) + 4  # role token overhead

        content = msg.get("content", "")
        if isinstance(content, str):
            total += count_tokens(content)
        elif isinstance(content, list):
            for block in content:
                if not isinstance(block, dict):
                    continue
                block_type = block.get("type", "")
                if block_type == "text":
                    total += count_tokens(block.get("text", ""))
                elif block_type == "tool_use":
                    total += count_tokens(block.get("name", ""))
                    total += count_tokens(str(block.get("input", {})))
                elif block_type == "tool_result":
                    total += count_tokens(str(block.get("content", "")))
                elif block_type == "image" or block_type == "document":
                    # Images and documents are heavy
                    total += 500
                else:
                    total += count_tokens(str(block))
    return total


def rough_token_count(text: str) -> int:
    """
    Rough token estimation without tiktoken overhead.

    Used for quick pre-flight checks (e.g., microcompact trigger decisions).
    """
    return max(1, len(text) // 4)
