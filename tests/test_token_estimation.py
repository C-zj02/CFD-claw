"""
Tests for token estimation utilities.
"""

from __future__ import annotations

import unittest
from unittest.mock import patch, MagicMock


class TestCountTokens(unittest.TestCase):
    """Tests for count_tokens()."""

    def test_empty_string(self):
        """Empty string returns 0 tokens."""
        from src.token_estimation import count_tokens
        self.assertEqual(count_tokens(""), 0)

    def test_simple_text_with_tiktoken(self):
        """Simple text with tiktoken returns expected count."""
        from src.token_estimation import count_tokens
        # "hello world" = 2 tokens in cl100k_base
        result = count_tokens("hello world")
        self.assertGreater(result, 0)
        self.assertLess(result, 10)

    def test_longer_text(self):
        """Longer text returns reasonable count."""
        from src.token_estimation import count_tokens
        text = "The quick brown fox jumps over the lazy dog. " * 10
        result = count_tokens(text)
        self.assertGreater(result, 50)
        self.assertLess(result, 200)

    def test_fallback_when_tiktoken_unavailable(self):
        """Falls back to char/4 when tiktoken unavailable."""
        from src.token_estimation import count_tokens, _get_encoder, _encoder_cache
        # Temporarily clear the cache
        import src.token_estimation as te
        old_cache = te._encoder_cache
        te._encoder_cache = None
        te._encoder_name = None
        try:
            # Patch _load_tiktoken to return None
            with patch('src.token_estimation._load_tiktoken', return_value=None):
                result = count_tokens("hello world")
                # ~11 chars / 4 = ~3
                self.assertGreaterEqual(result, 2)
                self.assertLessEqual(result, 4)
        finally:
            te._encoder_cache = old_cache


class TestCountMessagesTokens(unittest.TestCase):
    """Tests for count_messages_tokens()."""

    def test_empty_messages(self):
        """Empty message list returns 0."""
        from src.token_estimation import count_messages_tokens
        result = count_messages_tokens([])
        self.assertEqual(result, 0)

    def test_single_user_message(self):
        """Single user message returns reasonable count."""
        from src.token_estimation import count_messages_tokens
        messages = [{"role": "user", "content": "Hello"}]
        result = count_messages_tokens(messages)
        self.assertGreater(result, 0)

    def test_assistant_with_tool_use(self):
        """Assistant message with tool use."""
        from src.token_estimation import count_messages_tokens
        messages = [
            {
                "role": "assistant",
                "content": [
                    {"type": "text", "text": "Let me check..."},
                    {"type": "tool_use", "name": "Read", "input": {"file_path": "test.py"}},
                ]
            }
        ]
        result = count_messages_tokens(messages)
        self.assertGreater(result, 0)

    def test_mixed_messages(self):
        """Mixed role messages."""
        from src.token_estimation import count_messages_tokens
        messages = [
            {"role": "user", "content": "Hello world"},
            {"role": "assistant", "content": "Hi there!"},
            {"role": "user", "content": "How are you?"},
        ]
        result = count_messages_tokens(messages)
        self.assertGreater(result, 0)


class TestRoughTokenCount(unittest.TestCase):
    """Tests for rough_token_count()."""

    def test_empty_string(self):
        """Empty string returns 1 (minimum)."""
        from src.token_estimation import rough_token_count
        self.assertEqual(rough_token_count(""), 1)

    def test_short_string(self):
        """Short string uses char/4."""
        from src.token_estimation import rough_token_count
        # "hello" = 5 chars / 4 = 1.25 → 1
        result = rough_token_count("hello")
        self.assertEqual(result, 1)

    def test_long_string(self):
        """Long string returns reasonable rough estimate."""
        from src.token_estimation import rough_token_count
        text = "x" * 100
        result = rough_token_count(text)
        self.assertEqual(result, 25)


if __name__ == "__main__":
    unittest.main()
