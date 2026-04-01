"""GLM (Zhipu AI) provider implementation."""

from __future__ import annotations

from typing import Any, Generator, Optional

from zhipuai import ZhipuAI

from .base import BaseProvider, ChatMessage, ChatResponse


class GLMProvider(BaseProvider):
    """GLM (Zhipu AI) provider."""

    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        model: Optional[str] = None
    ):
        """Initialize GLM provider.

        Args:
            api_key: Zhipu AI API key
            base_url: Base URL (optional)
            model: Default model (default: glm-4.5)
        """
        super().__init__(api_key, base_url, model or "glm-4.5")

        # Initialize client
        self.client = ZhipuAI(api_key=api_key)

    def chat(
        self,
        messages: list[ChatMessage],
        **kwargs
    ) -> ChatResponse:
        """Synchronous chat completion.

        Args:
            messages: List of chat messages
            **kwargs: Additional parameters

        Returns:
            Chat response
        """
        model = self._get_model(**kwargs)

        # Convert messages
        glm_messages = [msg.to_dict() for msg in messages]

        # Make API call
        response = self.client.chat.completions.create(
            model=model,
            messages=glm_messages,
            **{k: v for k, v in kwargs.items() if k != "model"}
        )

        # Extract content
        choice = response.choices[0]

        # GLM-4.5 specific: reasoning_content
        reasoning_content = None
        if hasattr(choice.message, 'reasoning_content') and choice.message.reasoning_content:
            reasoning_content = choice.message.reasoning_content

        return ChatResponse(
            content=choice.message.content,
            model=response.model,
            usage={
                "input_tokens": response.usage.prompt_tokens,
                "output_tokens": response.usage.completion_tokens,
                "total_tokens": response.usage.total_tokens
            },
            finish_reason=choice.finish_reason,
            reasoning_content=reasoning_content
        )

    def chat_stream(
        self,
        messages: list[ChatMessage],
        **kwargs
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
        glm_messages = [msg.to_dict() for msg in messages]

        # Stream API call
        response = self.client.chat.completions.create(
            model=model,
            messages=glm_messages,
            stream=True,
            **{k: v for k, v in kwargs.items() if k != "model"}
        )

        for chunk in response:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content

    def get_available_models(self) -> list[str]:
        """Get list of available GLM models.

        Returns:
            List of model names
        """
        return [
            "glm-4.5",
            "glm-4",
            "glm-4-air",
            "glm-4-airx",
            "glm-4-flash",
            "glm-4-plus",
            "glm-3-turbo"
        ]
