"""LLM Providers for Clawd Codex."""

from __future__ import annotations

from .base import BaseProvider, ChatMessage, ChatResponse
from .anthropic_provider import AnthropicProvider
from .openai_provider import OpenAIProvider
from .glm_provider import GLMProvider


def get_provider_class(provider_name: str):
    """Get provider class by name."""
    providers = {
        "anthropic": AnthropicProvider,
        "openai": OpenAIProvider,
        "glm": GLMProvider,
    }

    if provider_name not in providers:
        raise ValueError(f"Unknown provider: {provider_name}")

    return providers[provider_name]


__all__ = [
    "BaseProvider",
    "ChatMessage",
    "ChatResponse",
    "AnthropicProvider",
    "OpenAIProvider",
    "GLMProvider",
    "get_provider_class",
]
