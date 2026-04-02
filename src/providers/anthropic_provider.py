"""Anthropic provider implementation."""

from __future__ import annotations

from typing import Generator, Optional

import anthropic

from .base import BaseProvider, ChatResponse, MessageInput


class AnthropicProvider(BaseProvider):
    """Anthropic Claude provider."""

    def __init__(
        self, api_key: str, base_url: Optional[str] = None, model: Optional[str] = None
    ):
        """Initialize Anthropic provider.

        Args:
            api_key: Anthropic API key
            base_url: Base URL (optional)
            model: Default model (default: claude-sonnet-4-20250514)
        """
        super().__init__(api_key, base_url, model or "claude-sonnet-4-20250514")

        # Initialize client
        client_kwargs = {"api_key": api_key}
        if base_url:
            client_kwargs["base_url"] = base_url

        self.client = anthropic.Anthropic(**client_kwargs)

    def chat(self, messages: list[MessageInput], **kwargs) -> ChatResponse:
        """Synchronous chat completion.

        Args:
            messages: List of chat messages
            **kwargs: Additional parameters (model, max_tokens, temperature, etc.)

        Returns:
            Chat response
        """
        model = self._get_model(**kwargs)
        max_tokens = kwargs.get("max_tokens", 4096)

        # Convert messages to Anthropic format
        anthropic_messages = self._prepare_messages(messages)

        # Make API call
        response = self.client.messages.create(
            model=model,
            max_tokens=max_tokens,
            messages=anthropic_messages,
            **{k: v for k, v in kwargs.items() if k not in ["model", "max_tokens"]},
        )

        # Extract content
        content = response.content[0].text

        return ChatResponse(
            content=content,
            model=response.model,
            usage={
                "input_tokens": response.usage.input_tokens,
                "output_tokens": response.usage.output_tokens,
            },
            finish_reason=response.stop_reason,
        )

    def chat_stream(
        self, messages: list[MessageInput], **kwargs
    ) -> Generator[str, None, None]:
        """Streaming chat completion.

        Args:
            messages: List of chat messages
            **kwargs: Additional parameters

        Yields:
            Chunks of response content
        """
        model = self._get_model(**kwargs)
        max_tokens = kwargs.get("max_tokens", 4096)

        # Convert messages
        anthropic_messages = self._prepare_messages(messages)

        # Stream API call
        with self.client.messages.stream(
            model=model,
            max_tokens=max_tokens,
            messages=anthropic_messages,
            **{k: v for k, v in kwargs.items() if k not in ["model", "max_tokens"]},
        ) as stream:
            for text in stream.text_stream:
                yield text

    def get_available_models(self) -> list[str]:
        """Get list of available Anthropic models.

        Returns:
            List of model names
        """
        return [
            "claude-sonnet-4-20250514",
            "claude-3-5-sonnet-20241022",
            "claude-3-5-haiku-20241022",
            "claude-3-opus-20240229",
            "claude-3-sonnet-20240229",
            "claude-3-haiku-20240307",
        ]
