"""
Compact boundary marker messages.

A compact boundary is a special system message inserted into the conversation
to mark where a compaction occurred. It preserves metadata about what was
summarized and is filtered out when sending to the API.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Optional, Union

from ..agent.conversation import Message, TextContentBlock


@dataclass
class CompactBoundaryMetadata:
    """Metadata stored inside a compact boundary marker."""
    trigger: str = "manual"  # "manual" | "auto"
    pre_compact_token_count: int = 0
    last_message_uuid: Optional[str] = None
    pre_compact_discovered_tools: list[str] = field(default_factory=list)
    messages_summarized: int = 0
    user_context: Optional[str] = None


def create_compact_boundary_message(
    trigger: str = "manual",
    pre_compact_token_count: int = 0,
    last_message_uuid: Optional[str] = None,
    user_context: Optional[str] = None,
    messages_summarized: int = 0,
    discovered_tools: Optional[list[str]] = None,
) -> Message:
    """
    Create a compact boundary marker message.

    This message is inserted into the conversation to mark the compaction point.
    It is filtered out when building API messages via conversation.get_messages().
    """
    metadata = CompactBoundaryMetadata(
        trigger=trigger,
        pre_compact_token_count=pre_compact_token_count,
        last_message_uuid=last_message_uuid,
        user_context=user_context,
        messages_summarized=messages_summarized,
        pre_compact_discovered_tools=discovered_tools or [],
    )
    content = TextContentBlock(
        type="text",
        text=f"[COMPACT BOUNDARY: {trigger}] metadata={_serialize_metadata(metadata)}",
    )
    msg = Message(
        role="system",
        content=[content],
        timestamp=datetime.now().isoformat(),
    )
    # Mark as internal so it gets filtered from API messages
    msg._is_internal = True  # type: ignore[attr-defined]
    return msg


def is_compact_boundary_message(msg: Message) -> bool:
    """Check if a message is a compact boundary marker."""
    return getattr(msg, "_is_internal", False) and msg.role == "system"


def _serialize_metadata(m: CompactBoundaryMetadata) -> str:
    """Serialize compact boundary metadata to a compact string representation."""
    parts = [f"trigger={m.trigger}", f"tokens={m.pre_compact_token_count}"]
    if m.last_message_uuid:
        parts.append(f"last_uuid={m.last_message_uuid[:8]}")
    if m.messages_summarized:
        parts.append(f"summarized={m.messages_summarized}")
    return "; ".join(parts)


def create_compact_summary_message(
    summary_text: str,
    suppress_follow_up: bool = False,
    is_visible_in_transcript_only: bool = False,
    summarize_metadata: Optional[dict[str, Any]] = None,
) -> Message:
    """
    Create the user-visible summary message inserted after compaction.
    """
    # Build the full summary text
    full_text = _format_summary_text(
        summary_text,
        suppress_follow_up=suppress_follow_up,
        is_visible_in_transcript_only=is_visible_in_transcript_only,
    )

    content = TextContentBlock(type="text", text=full_text)
    msg = Message(
        role="user",
        content=[content],
        timestamp=datetime.now().isoformat(),
    )
    # Attach compact summary metadata
    if summarize_metadata:
        msg._compact_summary_meta = summarize_metadata  # type: ignore[attr-defined]
    return msg


def _format_summary_text(
    summary: str,
    suppress_follow_up: bool = False,
    is_visible_in_transcript_only: bool = False,
) -> str:
    """Format the summary text with surrounding context."""
    lines = [
        "This session is being continued from a previous conversation.",
        "",
        summary,
    ]
    if suppress_follow_up:
        lines.extend([
            "",
            "Please continue helping the user without asking if they want to continue.",
        ])
    if is_visible_in_transcript_only:
        lines.insert(0, "[This message is visible in transcript only]")
    return "\n".join(lines)


def get_messages_after_boundary(
    messages: list[Message],
) -> list[Message]:
    """
    Return only the messages after the last compact boundary marker.

    Used to exclude already-summarized messages from the next summarization.
    """
    boundary_indices = [
        i for i, m in enumerate(messages)
        if is_compact_boundary_message(m)
    ]
    if not boundary_indices:
        return list(messages)
    last_boundary = max(boundary_indices)
    return list(messages[last_boundary + 1:])
