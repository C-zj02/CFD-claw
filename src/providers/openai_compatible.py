"""OpenAI-compatible provider base class.

This base class consolidates shared logic for providers that use the
OpenAI-style /chat/completions API (OpenAI, GLM, Minimax, etc.).
"""

from __future__ import annotations

import json
import re
from abc import abstractmethod
from typing import Any, Generator, Optional

from .base import BaseProvider, ChatResponse, MessageInput, TextChunkCallback


def _convert_to_openai_tool_schema(anthropic_tool: dict[str, Any]) -> dict[str, Any] | None:
    """Convert Anthropic tool schema to OpenAI/GLM/Minimax function format.

    Returns None if the schema is invalid (missing type, type is None, or other issues).
    """
    input_schema = anthropic_tool.get("input_schema")
    if not input_schema or not isinstance(input_schema, dict):
        return None
    schema_type = input_schema.get("type")
    if schema_type is None or schema_type == "None":
        return None
    # Some providers (Azure) require type=object to have properties
    if schema_type == "object" and "properties" not in input_schema and "anyOf" not in input_schema and "oneOf" not in input_schema:
        # Try to add an empty properties dict if none provided
        input_schema = {**input_schema, "properties": {}}
    return {
        "type": "function",
        "function": {
            "name": anthropic_tool["name"],
            "description": anthropic_tool.get("description", ""),
            "parameters": input_schema,
        },
    }


_DSML_TOOL_CALLS_RE = re.compile(
    r"<｜｜DSML｜｜tool_calls>\s*(?P<body>.*?)\s*</｜｜DSML｜｜tool_calls>",
    re.DOTALL,
)
_DSML_INVOKE_RE = re.compile(
    r"<｜｜DSML｜｜invoke\s+name=\"(?P<name>[^\"]+)\">\s*"
    r"(?P<body>.*?)\s*</｜｜DSML｜｜invoke>",
    re.DOTALL,
)
_DSML_PARAMETER_RE = re.compile(
    r"<｜｜DSML｜｜parameter\s+name=\"(?P<name>[^\"]+)\"\s+string=\"(?P<string>true|false)\">"
    r"(?P<value>.*?)"
    r"</｜｜DSML｜｜parameter>",
    re.DOTALL,
)


def _parse_dsml_value(value: str, *, is_string: bool) -> Any:
    value = value.strip()
    if is_string:
        return value
    try:
        return json.loads(value)
    except Exception:
        lowered = value.lower()
        if lowered == "true":
            return True
        if lowered == "false":
            return False
        if lowered == "null":
            return None
        try:
            return int(value)
        except ValueError:
            pass
        try:
            return float(value)
        except ValueError:
            return value


def _extract_dsml_tool_calls(content: str) -> tuple[str, list[dict[str, Any]]]:
    """Extract DeepSeek-style DSML tool calls that some gateways emit as text."""
    if not content or "<｜｜DSML｜｜tool_calls>" not in content:
        return content, []

    tool_uses: list[dict[str, Any]] = []
    for tool_block in _DSML_TOOL_CALLS_RE.finditer(content):
        for idx, invoke in enumerate(_DSML_INVOKE_RE.finditer(tool_block.group("body"))):
            tool_input: dict[str, Any] = {}
            for param in _DSML_PARAMETER_RE.finditer(invoke.group("body")):
                param_name = param.group("name")
                is_string = param.group("string") == "true"
                tool_input[param_name] = _parse_dsml_value(param.group("value"), is_string=is_string)
            tool_uses.append({
                "id": f"dsml_tool_call_{len(tool_uses) + idx}",
                "name": invoke.group("name"),
                "input": tool_input,
            })

    cleaned = _DSML_TOOL_CALLS_RE.sub("", content).strip()
    return cleaned, tool_uses


def _strip_partial_dsml_tool_block(content: str) -> str:
    """Remove an incomplete DSML tool block from streamed user-visible text."""
    marker = "<｜｜DSML｜｜tool_calls>"
    idx = content.find(marker)
    if idx != -1:
        return content[:idx]
    max_prefix = min(len(marker) - 1, len(content))
    for size in range(max_prefix, 0, -1):
        if marker.startswith(content[-size:]):
            return content[:-size]
    return content


class OpenAICompatibleProvider(BaseProvider):
    """Base class for providers using OpenAI-style chat completions API.

    Subclasses must implement:
    - _create_client(): Create and return the provider-specific SDK client
    - get_available_models(): Return list of available model names

    The client is created lazily on first use.
    """

    def __init__(
        self,
        api_key: str,
        base_url: Optional[str] = None,
        model: Optional[str] = None,
    ):
        """Initialize OpenAI-compatible provider.

        Args:
            api_key: API key for authentication
            base_url: Base URL for API endpoint
            model: Default model to use
        """
        super().__init__(api_key, base_url, model)
        self._client: Optional[Any] = None

    @abstractmethod
    def _create_client(self) -> Any:
        """Create the provider-specific SDK client.

        Returns:
            An instance of the provider's SDK client.
        """
        pass

    @property
    def client(self) -> Any:
        """Get or create the SDK client (lazy initialization)."""
        if self._client is None:
            self._client = self._create_client()
        return self._client

    def _build_usage_dict(self, usage: Any) -> dict[str, Any]:
        if usage is None:
            return {}
        return {
            "input_tokens": getattr(usage, "prompt_tokens", 0),
            "output_tokens": getattr(usage, "completion_tokens", 0),
            "total_tokens": getattr(usage, "total_tokens", 0),
        }

    def chat(
        self,
        messages: list[MessageInput],
        tools: Optional[list[dict[str, Any]]] = None,
        **kwargs
    ) -> ChatResponse:
        """Synchronous chat completion.

        Args:
            messages: List of chat messages
            tools: Optional list of tool schemas (Anthropic format)
            **kwargs: Additional parameters

        Returns:
            Chat response
        """
        model = self._get_model(**kwargs)

        # Convert messages
        provider_messages = self._prepare_messages(messages)

        # Convert tools to OpenAI format
        extra_kwargs: dict[str, Any] = {}
        if tools:
            converted = [_convert_to_openai_tool_schema(t) for t in tools]
            extra_kwargs["tools"] = [t for t in converted if t is not None]

        # Make API call
        response = self.client.chat.completions.create(
            model=model,
            messages=provider_messages,
            **extra_kwargs,
            **{k: v for k, v in kwargs.items() if k not in ["model", "tools"]},
        )

        # Extract content
        choice = response.choices[0]

        # Handle reasoning content (GLM specific, but harmless for others)
        reasoning_content: Optional[str] = None
        if (
            hasattr(choice.message, "reasoning_content")
            and choice.message.reasoning_content
        ):
            reasoning_content = choice.message.reasoning_content

        # Extract tool calls (OpenAI format -> Anthropic format)
        tool_uses: Optional[list[dict[str, Any]]] = None
        if hasattr(choice.message, "tool_calls") and choice.message.tool_calls:
            tool_uses = []
            for tc in choice.message.tool_calls:
                try:
                    args = json.loads(tc.function.arguments) if tc.function.arguments else {}
                except Exception:
                    args = {}
                tool_uses.append({
                    "id": tc.id,
                    "name": tc.function.name,
                    "input": args,
                })

        content, dsml_tool_uses = _extract_dsml_tool_calls(choice.message.content or "")
        if dsml_tool_uses:
            tool_uses = (tool_uses or []) + dsml_tool_uses

        return ChatResponse(
            content=content,
            model=response.model,
            usage=self._build_usage_dict(getattr(response, "usage", None)),
            finish_reason=choice.finish_reason,
            reasoning_content=reasoning_content,
            tool_uses=tool_uses,
        )

    def chat_stream(
        self,
        messages: list[MessageInput],
        tools: Optional[list[dict[str, Any]]] = None,
        **kwargs
    ) -> Generator[str, None, None]:
        """Streaming chat completion.

        Args:
            messages: List of chat messages
            tools: Optional list of tool schemas (Anthropic format)
            **kwargs: Additional parameters

        Yields:
            Chunks of response content
        """
        model = self._get_model(**kwargs)

        # Convert messages
        provider_messages = self._prepare_messages(messages)

        # Convert tools to OpenAI format
        extra_kwargs: dict[str, Any] = {}
        if tools:
            converted = [_convert_to_openai_tool_schema(t) for t in tools]
            extra_kwargs["tools"] = [t for t in converted if t is not None]

        # Stream API call
        stream = self.client.chat.completions.create(
            model=model,
            messages=provider_messages,
            stream=True,
            **extra_kwargs,
            **{k: v for k, v in kwargs.items() if k not in ["model", "tools"]},
        )

        for chunk in stream:
            if chunk.choices[0].delta.content is not None:
                yield chunk.choices[0].delta.content

    def chat_stream_response(
        self,
        messages: list[MessageInput],
        tools: Optional[list[dict[str, Any]]] = None,
        on_text_chunk: TextChunkCallback | None = None,
        **kwargs
    ) -> ChatResponse:
        """Stream OpenAI-compatible chunks while rebuilding the final response."""
        model = self._get_model(**kwargs)
        provider_messages = self._prepare_messages(messages)

        extra_kwargs: dict[str, Any] = {}
        if tools:
            converted = [_convert_to_openai_tool_schema(t) for t in tools]
            extra_kwargs["tools"] = [t for t in converted if t is not None]

        stream = self.client.chat.completions.create(
            model=model,
            messages=provider_messages,
            stream=True,
            **extra_kwargs,
            **{k: v for k, v in kwargs.items() if k not in ["model", "tools"]},
        )

        raw_content_parts: list[str] = []
        emitted_content_len = 0
        response_model = model
        finish_reason = "stop"
        reasoning_parts: list[str] = []
        usage_obj: Any = None
        tool_calls_by_index: dict[int, dict[str, str]] = {}

        for chunk in stream:
            response_model = getattr(chunk, "model", response_model)
            usage_candidate = getattr(chunk, "usage", None)
            if usage_candidate is not None:
                usage_obj = usage_candidate

            choices = getattr(chunk, "choices", None) or []
            if not choices:
                continue
            choice = choices[0]
            if getattr(choice, "finish_reason", None):
                finish_reason = choice.finish_reason

            delta = getattr(choice, "delta", None)
            if delta is None:
                continue

            content_piece = getattr(delta, "content", None)
            if content_piece:
                raw_content_parts.append(str(content_piece))
                if on_text_chunk is not None:
                    visible_content = _strip_partial_dsml_tool_block("".join(raw_content_parts))
                    if len(visible_content) > emitted_content_len:
                        on_text_chunk(visible_content[emitted_content_len:])
                        emitted_content_len = len(visible_content)

            reasoning_piece = getattr(delta, "reasoning_content", None)
            if reasoning_piece:
                reasoning_parts.append(str(reasoning_piece))

            tool_call_deltas = getattr(delta, "tool_calls", None) or []
            for tc in tool_call_deltas:
                idx = getattr(tc, "index", 0)
                entry = tool_calls_by_index.setdefault(idx, {"id": "", "name": "", "arguments": ""})

                tc_id = getattr(tc, "id", None)
                if tc_id:
                    entry["id"] = str(tc_id)

                function = getattr(tc, "function", None)
                if function is not None:
                    fn_name = getattr(function, "name", None)
                    if fn_name:
                        entry["name"] += str(fn_name)
                    fn_args = getattr(function, "arguments", None)
                    if fn_args:
                        entry["arguments"] += str(fn_args)

        tool_uses: list[dict[str, Any]] = []
        for idx in sorted(tool_calls_by_index.keys()):
            item = tool_calls_by_index[idx]
            if not item["name"]:
                continue
            try:
                parsed_args = json.loads(item["arguments"]) if item["arguments"] else {}
            except Exception:
                parsed_args = {}
            tool_uses.append({
                "id": item["id"] or f"tool_call_{idx}",
                "name": item["name"],
                "input": parsed_args,
            })

        content, dsml_tool_uses = _extract_dsml_tool_calls("".join(raw_content_parts))
        tool_uses.extend(dsml_tool_uses)

        reasoning_content = "".join(reasoning_parts) if reasoning_parts else None
        return ChatResponse(
            content=content,
            model=response_model,
            usage=self._build_usage_dict(usage_obj),
            finish_reason=finish_reason,
            reasoning_content=reasoning_content,
            tool_uses=tool_uses or None,
        )
