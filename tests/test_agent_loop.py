"""Test agent loop with mocked provider to verify tool invocation."""

import unittest
from unittest.mock import MagicMock
from pathlib import Path
import tempfile

from src.agent.conversation import Conversation
from src.providers.base import ChatResponse
from src.tool_system.defaults import build_default_registry
from src.tool_system.context import ToolContext
from src.tool_system.agent_loop import run_agent_loop, AgentLoopResult


class TestAgentLoop(unittest.TestCase):
    """Test agent loop logic."""

    def setUp(self):
        """Set up test fixtures."""
        self.temp_dir = tempfile.TemporaryDirectory()
        self.workspace = Path(self.temp_dir.name)
        self.registry = build_default_registry()
        self.context = ToolContext(workspace_root=self.workspace)

    def tearDown(self):
        """Clean up test fixtures."""
        self.temp_dir.cleanup()

    def test_agent_loop_calls_tool(self):
        """Test agent loop correctly dispatches a tool call from mocked LLM."""
        conversation = Conversation()
        conversation.add_user_message("Create a file hello.py with content print('hello world')")

        # Mock provider
        mock_provider = MagicMock()
        mock_provider.chat_stream_response.side_effect = NotImplementedError()

        # First response: tool use Write
        mock_tool_use = {
            "id": "toolu_123",
            "name": "Write",
            "input": {
                "file_path": str(self.workspace / "hello.py"),
                "content": "print('hello world')"
            }
        }
        mock_response1 = ChatResponse(
            content="I will create the file.",
            model="test-model",
            usage={"input_tokens": 10, "output_tokens": 20},
            finish_reason="tool_use",
            tool_uses=[mock_tool_use],
        )

        # Second response: final text after tool result
        mock_response2 = ChatResponse(
            content="File created successfully!",
            model="test-model",
            usage={"input_tokens": 30, "output_tokens": 10},
            finish_reason="stop",
            tool_uses=None,
        )

        mock_provider.chat.side_effect = [mock_response1, mock_response2]

        result = run_agent_loop(
            conversation=conversation,
            provider=mock_provider,
            tool_registry=self.registry,
            tool_context=self.context,
            verbose=False,
        )

        # Verify final response
        self.assertIsInstance(result, AgentLoopResult)
        self.assertEqual(result.response_text, "File created successfully!")

        # Verify provider was called twice
        self.assertEqual(mock_provider.chat.call_count, 2)

        # Verify file was created
        hello_py = self.workspace / "hello.py"
        self.assertTrue(hello_py.exists())
        self.assertEqual(hello_py.read_text(), "print('hello world')")

    def test_agent_loop_creates_hello_world(self):
        """Test agent loop creates hello.py and writes print('hello world')."""
        conversation = Conversation()
        conversation.add_user_message("Create a file hello.py with content print('hello world')")

        mock_provider = MagicMock()
        mock_provider.chat_stream_response.side_effect = NotImplementedError()

        # First response: tool use Write
        hello_path = self.workspace / "hello.py"
        mock_tool_write = {
            "id": "toolu_123",
            "name": "Write",
            "input": {
                "file_path": str(hello_path),
                "content": "print('hello world')"
            }
        }
        mock_response1 = ChatResponse(
            content="I will create the file.",
            model="test-model",
            usage={"input_tokens": 10, "output_tokens": 20},
            finish_reason="tool_use",
            tool_uses=[mock_tool_write],
        )

        # Second response: final
        mock_response2 = ChatResponse(
            content="File created successfully!",
            model="test-model",
            usage={"input_tokens": 30, "output_tokens": 10},
            finish_reason="stop",
            tool_uses=None,
        )

        mock_provider.chat.side_effect = [mock_response1, mock_response2]

        result = run_agent_loop(
            conversation=conversation,
            provider=mock_provider,
            tool_registry=self.registry,
            tool_context=self.context,
            verbose=False,
        )

        self.assertIsInstance(result, AgentLoopResult)
        self.assertEqual(result.response_text, "File created successfully!")
        self.assertTrue(hello_path.exists())
        self.assertEqual(hello_path.read_text(), "print('hello world')")

    def test_agent_loop_forces_final_synthesis_when_max_turns_is_reached(self):
        """When tool turns are exhausted, the loop still makes one final no-tools synthesis pass."""
        conversation = Conversation()
        conversation.add_user_message("Create a file hello.py with content print('hello world')")

        mock_provider = MagicMock()
        mock_provider.chat_stream_response.side_effect = NotImplementedError()
        hello_path = self.workspace / "hello.py"
        mock_provider.chat.side_effect = [
            ChatResponse(
                content="I will create the file.",
                model="test-model",
                usage={"input_tokens": 10, "output_tokens": 20},
                finish_reason="tool_use",
                tool_uses=[{
                    "id": "toolu_123",
                    "name": "Write",
                    "input": {
                        "file_path": str(hello_path),
                        "content": "print('hello world')",
                    },
                }],
            ),
            ChatResponse(
                content="File created successfully!",
                model="test-model",
                usage={"input_tokens": 30, "output_tokens": 10},
                finish_reason="stop",
                tool_uses=None,
            ),
        ]

        result = run_agent_loop(
            conversation=conversation,
            provider=mock_provider,
            tool_registry=self.registry,
            tool_context=self.context,
            max_turns=1,
            verbose=False,
        )

        self.assertIsInstance(result, AgentLoopResult)
        self.assertEqual(result.response_text, "File created successfully!")
        self.assertEqual(result.num_turns, 2)
        self.assertEqual(mock_provider.chat.call_count, 2)
        self.assertTrue(hello_path.exists())

    def test_agent_loop_falls_back_if_final_synthesis_still_requests_tool(self):
        """Final no-tools synthesis must not leak provider-specific tool markup."""
        conversation = Conversation()
        conversation.add_user_message("Read README.md and summarize it")

        mock_provider = MagicMock()
        mock_provider.chat_stream_response.side_effect = NotImplementedError()
        readme_path = self.workspace / "README.md"
        readme_path.write_text("hello", encoding="utf-8")

        mock_provider.chat.side_effect = [
            ChatResponse(
                content="I will read the file.",
                model="deepseek-v4-pro",
                usage={"input_tokens": 10, "output_tokens": 20},
                finish_reason="tool_calls",
                tool_uses=[{
                    "id": "toolu_123",
                    "name": "Read",
                    "input": {"file_path": str(readme_path)},
                }],
            ),
            ChatResponse(
                content="Need one more read.",
                model="deepseek-v4-pro",
                usage={"input_tokens": 30, "output_tokens": 10},
                finish_reason="tool_calls",
                tool_uses=[{
                    "id": "dsml_tool_call_1",
                    "name": "Read",
                    "input": {"file_path": str(readme_path), "offset": 2, "limit": 2},
                }],
            ),
        ]

        chunks: list[str] = []
        result = run_agent_loop(
            conversation=conversation,
            provider=mock_provider,
            tool_registry=self.registry,
            tool_context=self.context,
            max_turns=1,
            stream=True,
            verbose=False,
            on_text_chunk=chunks.append,
        )

        self.assertIn("工具预算已用尽", result.response_text)
        self.assertIn("工具预算已用尽", "".join(chunks))
        self.assertNotIn("DSML", result.response_text)
        self.assertEqual(mock_provider.chat.call_count, 2)

    def test_agent_loop_stream_emits_final_text_chunks(self):
        """Streaming mode emits final response chunks without changing the result."""
        conversation = Conversation()
        conversation.add_user_message("Say hello")

        mock_provider = MagicMock()
        mock_provider.chat_stream_response.side_effect = NotImplementedError()
        mock_provider.chat.return_value = ChatResponse(
            content="Hello from Clawd!",
            model="test-model",
            usage={"input_tokens": 3, "output_tokens": 4},
            finish_reason="stop",
            tool_uses=None,
        )

        chunks: list[str] = []
        result = run_agent_loop(
            conversation=conversation,
            provider=mock_provider,
            tool_registry=self.registry,
            tool_context=self.context,
            stream=True,
            verbose=False,
            on_text_chunk=chunks.append,
        )

        self.assertEqual("".join(chunks), "Hello from Clawd!")
        self.assertEqual(result.response_text, "Hello from Clawd!")
        self.assertEqual(mock_provider.chat.call_count, 1)
        self.assertEqual(len(conversation.messages), 2)
        self.assertEqual(conversation.messages[-1].role, "assistant")
        self.assertEqual(conversation.messages[-1].content, "Hello from Clawd!")

    def test_agent_loop_stream_only_emits_final_turn_text(self):
        """Streaming mode skips interim tool-planning text and emits the final answer only."""
        conversation = Conversation()
        conversation.add_user_message("Create a file hello.py with content print('hello world')")

        mock_provider = MagicMock()
        mock_provider.chat_stream_response.side_effect = NotImplementedError()
        hello_path = self.workspace / "hello.py"
        mock_response1 = ChatResponse(
            content="I will create the file.",
            model="test-model",
            usage={"input_tokens": 10, "output_tokens": 20},
            finish_reason="tool_use",
            tool_uses=[{
                "id": "toolu_123",
                "name": "Write",
                "input": {
                    "file_path": str(hello_path),
                    "content": "print('hello world')",
                },
            }],
        )
        mock_response2 = ChatResponse(
            content="File created successfully!",
            model="test-model",
            usage={"input_tokens": 30, "output_tokens": 10},
            finish_reason="stop",
            tool_uses=None,
        )
        mock_provider.chat.side_effect = [mock_response1, mock_response2]

        chunks: list[str] = []
        result = run_agent_loop(
            conversation=conversation,
            provider=mock_provider,
            tool_registry=self.registry,
            tool_context=self.context,
            stream=True,
            verbose=False,
            on_text_chunk=chunks.append,
        )

        self.assertEqual("".join(chunks), "File created successfully!")
        self.assertEqual(result.response_text, "File created successfully!")
        self.assertTrue(hello_path.exists())

    def test_agent_loop_stream_uses_structured_provider_streaming_for_tool_turns(self):
        """Structured provider streaming can emit pre-tool text and final text across turns."""
        conversation = Conversation()
        conversation.add_user_message("Create hello.py")

        provider = MagicMock()
        hello_path = self.workspace / "hello.py"

        stream_responses = [
            ChatResponse(
                content="I will create the file.",
                model="test-model",
                usage={"input_tokens": 10, "output_tokens": 20},
                finish_reason="tool_use",
                tool_uses=[{
                    "id": "toolu_123",
                    "name": "Write",
                    "input": {
                        "file_path": str(hello_path),
                        "content": "print('hello world')",
                    },
                }],
            ),
            ChatResponse(
                content="File created successfully!",
                model="test-model",
                usage={"input_tokens": 30, "output_tokens": 10},
                finish_reason="stop",
                tool_uses=None,
            ),
        ]

        def stream_side_effect(messages, tools=None, on_text_chunk=None, **kwargs):
            response = stream_responses.pop(0)
            if on_text_chunk is not None and response.content:
                on_text_chunk(response.content)
            return response

        provider.chat_stream_response.side_effect = stream_side_effect
        provider.chat.side_effect = AssertionError("chat() should not be used when structured streaming is available")

        chunks: list[str] = []
        result = run_agent_loop(
            conversation=conversation,
            provider=provider,
            tool_registry=self.registry,
            tool_context=self.context,
            stream=True,
            verbose=False,
            on_text_chunk=chunks.append,
        )

        self.assertEqual("".join(chunks), "I will create the file.File created successfully!")
        self.assertEqual(result.response_text, "File created successfully!")
        self.assertEqual(provider.chat_stream_response.call_count, 2)
        self.assertTrue(hello_path.exists())

    def test_agent_loop_stream_falls_back_when_structured_streaming_is_unavailable(self):
        """If the provider lacks structured streaming, the stable synchronous path still works."""
        conversation = Conversation()
        conversation.add_user_message("Say hello")

        provider = MagicMock()
        provider.chat_stream_response.side_effect = NotImplementedError()
        provider.chat.return_value = ChatResponse(
            content="Hello from fallback!",
            model="test-model",
            usage={"input_tokens": 2, "output_tokens": 3},
            finish_reason="stop",
            tool_uses=None,
        )

        chunks: list[str] = []
        result = run_agent_loop(
            conversation=conversation,
            provider=provider,
            tool_registry=self.registry,
            tool_context=self.context,
            stream=True,
            verbose=False,
            on_text_chunk=chunks.append,
        )

        self.assertEqual("".join(chunks), "Hello from fallback!")
        self.assertEqual(result.response_text, "Hello from fallback!")
        provider.chat.assert_called_once()

    def test_agent_loop_emits_assistant_turn_event_after_tool_results(self):
        """A second model turn after tools should surface an assistant-turn event."""
        conversation = Conversation()
        conversation.add_user_message("Create a file hello.py with content print('hello world')")

        provider = MagicMock()
        provider.chat_stream_response.side_effect = NotImplementedError()
        hello_path = self.workspace / "hello.py"
        provider.chat.side_effect = [
            ChatResponse(
                content="I will create the file.",
                model="test-model",
                usage={"input_tokens": 10, "output_tokens": 20},
                finish_reason="tool_use",
                tool_uses=[{
                    "id": "toolu_123",
                    "name": "Write",
                    "input": {
                        "file_path": str(hello_path),
                        "content": "print('hello world')",
                    },
                }],
            ),
            ChatResponse(
                content="File created successfully!",
                model="test-model",
                usage={"input_tokens": 30, "output_tokens": 10},
                finish_reason="stop",
                tool_uses=None,
            ),
        ]

        events = []
        result = run_agent_loop(
            conversation=conversation,
            provider=provider,
            tool_registry=self.registry,
            tool_context=self.context,
            verbose=False,
            on_event=events.append,
        )

        self.assertEqual(result.response_text, "File created successfully!")
        assistant_turns = [event for event in events if event.kind == "assistant_turn"]
        self.assertEqual(len(assistant_turns), 1)
        self.assertEqual(assistant_turns[0].tool_name, "Assistant")

    def test_agent_loop_preserves_openai_reasoning_content_across_tool_turns(self):
        """Thinking-mode providers require reasoning_content to be echoed with tool-call history."""
        conversation = Conversation()
        conversation.add_user_message("Read README.md")

        provider = MagicMock()
        provider.chat_stream_response.side_effect = NotImplementedError()
        readme_path = self.workspace / "README.md"
        readme_path.write_text("hello", encoding="utf-8")

        response_with_tool = ChatResponse(
            content="I will read the file.",
            model="deepseek-v4-pro",
            usage={"input_tokens": 10, "output_tokens": 20},
            finish_reason="tool_calls",
            reasoning_content="Need to inspect the requested file.",
            tool_uses=[{
                "id": "call_1",
                "name": "Read",
                "input": {"file_path": str(readme_path)},
            }],
        )
        final_response = ChatResponse(
            content="The file says hello.",
            model="deepseek-v4-pro",
            usage={"input_tokens": 30, "output_tokens": 10},
            finish_reason="stop",
            tool_uses=None,
        )
        provider.chat.side_effect = [response_with_tool, final_response]

        result = run_agent_loop(
            conversation=conversation,
            provider=provider,
            tool_registry=self.registry,
            tool_context=self.context,
            verbose=False,
        )

        self.assertEqual(result.response_text, "The file says hello.")
        second_call_messages = provider.chat.call_args_list[1].args[0]
        assistant_messages = [m for m in second_call_messages if m.get("role") == "assistant"]
        self.assertEqual(assistant_messages[0]["reasoning_content"], "Need to inspect the requested file.")
        self.assertEqual(conversation.messages[1].reasoning_content, "Need to inspect the requested file.")


if __name__ == "__main__":
    unittest.main()
