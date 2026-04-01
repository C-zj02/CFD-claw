"""Conversation management for Clawd Codex."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional
from datetime import datetime


@dataclass
class Message:
    """Conversation message."""
    role: str  # "user", "assistant", "system"
    content: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())


@dataclass
class Conversation:
    """Conversation manager."""
    messages: list[Message] = field(default_factory=list)
    max_history: int = 100

    def add_message(self, role: str, content: str):
        """Add a message to conversation."""
        if len(self.messages) >= self.max_history:
            self.messages.pop(0)

        self.messages.append(Message(role=role, content=content))

    def get_messages(self) -> list[dict]:
        """Get messages in API format."""
        return [
            {"role": msg.role, "content": msg.content}
            for msg in self.messages
        ]

    def clear(self):
        """Clear conversation."""
        self.messages.clear()

    def to_dict(self) -> dict:
        """Serialize conversation."""
        return {
            "messages": [
                {"role": msg.role, "content": msg.content, "timestamp": msg.timestamp}
                for msg in self.messages
            ],
            "max_history": self.max_history
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Conversation':
        """Deserialize conversation."""
        conv = cls(max_history=data.get("max_history", 100))
        for msg_data in data.get("messages", []):
            conv.messages.append(Message(
                role=msg_data["role"],
                content=msg_data["content"],
                timestamp=msg_data.get("timestamp", "")
            ))
        return conv
