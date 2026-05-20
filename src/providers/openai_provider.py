"""OpenAI provider implementation."""

from __future__ import annotations

import os
from typing import Any, Optional

try:
    from openai import OpenAI  # type: ignore
except ModuleNotFoundError:  # pragma: no cover
    OpenAI = None

try:
    import httpx  # type: ignore
except ModuleNotFoundError:  # pragma: no cover
    httpx = None

from .openai_compatible import OpenAICompatibleProvider


def _env_flag(name: str, *, default: bool = False) -> bool:
    value = os.environ.get(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _env_float(name: str, *, default: float) -> float:
    value = os.environ.get(name)
    if value is None:
        return default
    try:
        return float(value)
    except ValueError:
        return default


class OpenAIProvider(OpenAICompatibleProvider):
    """OpenAI provider using OpenAI SDK."""

    def __init__(
        self, api_key: str, base_url: Optional[str] = None, model: Optional[str] = None
    ):
        """Initialize OpenAI provider.

        Args:
            api_key: OpenAI API key
            base_url: Base URL (optional, for custom endpoints)
            model: Default model (default: deepseek-v4-pro)
        """
        super().__init__(api_key, base_url, model or "deepseek-v4-pro")

    def _create_client(self) -> Any:
        """Create OpenAI SDK client."""
        if OpenAI is None:  # pragma: no cover
            raise ModuleNotFoundError(
                "openai package is not installed. Install optional dependencies to use OpenAIProvider."
            )
        timeout = _env_float("CLAWD_OPENAI_TIMEOUT", default=120.0)
        kwargs: dict[str, Any] = {
            "api_key": self.api_key,
            # Some OpenAI-compatible gateways are slow to complete TLS handshakes,
            # especially when a local proxy is involved.
            "timeout": timeout,
        }
        if httpx is not None:
            # The OpenAI SDK/httpx respects HTTP(S)_PROXY by default. A broken
            # local proxy commonly causes TLS handshake resets for OpenAI-compatible
            # gateways, so Clawd defaults to direct connections. Users who need
            # environment proxies can opt back in with CLAWD_OPENAI_TRUST_ENV=1.
            kwargs["http_client"] = httpx.Client(
                timeout=timeout,
                trust_env=_env_flag("CLAWD_OPENAI_TRUST_ENV", default=False),
            )
        if self.base_url:
            kwargs["base_url"] = self.base_url
        return OpenAI(**kwargs)

    def get_available_models(self) -> list[str]:
        """Get list of available OpenAI models.

        Returns:
            List of model names
        """
        return [
            # DeepSeek models (OpenAI-compatible endpoints)
            "deepseek-v4-pro",
            "deepseek-v4-flash",
            # GPT-5.4 series (latest flagship)
            "gpt-5.4",
            "gpt-5.4-pro",
            "gpt-5.4-mini",
            "gpt-5.4-nano",
            # GPT-5.2 series
            "gpt-5.2",
            "gpt-5.2-pro",
            "gpt-5.2-mini",
            "gpt-5.2-nano",
            # GPT-5.3-Codex (coding-specialized)
            "gpt-5.3-codex",
            # Legacy GPT-4 series
            "gpt-4o",
            "gpt-4o-mini",
            "gpt-4-turbo",
            "gpt-4",
            "gpt-3.5-turbo",
        ]
