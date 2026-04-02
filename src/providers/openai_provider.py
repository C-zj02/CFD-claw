"""OpenAI provider implementation."""

from __future__ import annotations

from typing import Any, Generator, Optional

from openai import OpenAI

from .base import BaseProvider, ChatResponse, MessageInput


class OpenAIProvider(BaseProvider):
    """OpenAI provider."""

    def __init__(
        self, api_key: str, base_url: Optional[str] = None, model: Optional[str] = None
    ):
        """Initialize OpenAI provider.

        Args:
            api_key: OpenAI API key
            base_url: Base URL (optional, for custom endpoints)
            model: Default model (default: gpt-4)
        """
        super().__init__(api_key, base_url, model or "gpt-4")

        # Initialize client
        client_kwargs = {"api_key": api_key}
        if base_url:
            client_kwargs["base_url"] = base_url

        self.client = OpenAI(**client_kwargs)

    def chat(self, messages: list[MessageInput], **kwargs) -> ChatResponse:
        """Synchronous chat completion.

        Args:
            messages: List of chat messages
            **kwargs: Additional parameters

        Returns:
            Chat response
        """
        model = self._get_model(**kwargs)

        # Convert messages
        openai_messages = self._prepare_messages(messages)

        # Make API call
        response = self.client.chat.completions.create(
            model=model,
            messages=openai_messages,
            **{k: v for k, v in kwargs.items() if k != "model"},
        )

        # Extract content
        choice = response.choices[0]

        return ChatResponse(
            content=choice.message.content,
            model=response.model,
            usage={
                "input_tokens": response.usage.prompt_tokens,
                "output_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens,
            },
            finish_reason=choice.finish_reason,
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

        # Convert messages
        openai_messages = self._prepare_messages(messages)

        # Stream API call
        stream = self.client.chat.completions.create(
            model=model,
            messages=openai_messages,
            stream=True,
            **{k: v for k, v in kwargs.items() if k != "model"},
        )

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content

    def get_available_models(self) -> list[str]:
        """Get list of available OpenAI models.

        Returns:
            List of model names
        """
        return [
            "gpt-4",
            "gpt-4-turbo",
            "gpt-4o",
            "gpt-4o-mini",
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-16k",
        ]
