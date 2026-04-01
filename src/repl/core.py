"""Interactive REPL for Clawd Codex."""

from __future__ import annotations

from prompt_toolkit import PromptSession
from prompt_toolkit.history import FileHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.styles import Style
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.key_binding import KeyBindings
from rich.console import Console
from rich.markdown import Markdown
from pathlib import Path
import sys

from src.agent import Session
from src.config import get_provider_config
from src.providers import get_provider_class
from src.providers.base import ChatMessage


class ClawdREPL:
    """Interactive REPL for Clawd Codex."""

    def __init__(self, provider_name: str = "glm"):
        self.console = Console()
        self.provider_name = provider_name
        self.multiline_mode = False

        # Load configuration
        config = get_provider_config(provider_name)
        if not config.get("api_key"):
            self.console.print("[red]Error: API key not configured.[/red]")
            self.console.print("Run [bold]clawd login[/bold] to configure.")
            sys.exit(1)

        # Initialize provider
        provider_class = get_provider_class(provider_name)
        self.provider = provider_class(
            api_key=config["api_key"],
            base_url=config.get("base_url"),
            model=config.get("default_model")
        )

        # Create session
        self.session = Session.create(
            provider_name,
            self.provider.model
        )

        # Prompt toolkit with tab completion
        history_file = Path.home() / ".clawd" / "history"
        history_file.parent.mkdir(parents=True, exist_ok=True)

        # Command completer
        commands = ["/help", "/exit", "/quit", "/q", "/clear", "/save", "/load", "/multiline"]
        self.completer = WordCompleter(commands, ignore_case=True)

        # Key bindings for multiline
        self.bindings = KeyBindings()

        self.prompt_session = PromptSession(
            history=FileHistory(str(history_file)),
            auto_suggest=AutoSuggestFromHistory(),
            completer=self.completer,
            style=Style.from_dict({
                'prompt': 'bold blue',
            }),
            key_bindings=self.bindings
        )

    def run(self):
        """Run the REPL."""
        self.console.print("[bold blue]Clawd Codex REPL[/bold blue]")
        self.console.print(f"Provider: [green]{self.provider_name}[/green]")
        self.console.print(f"Model: [green]{self.provider.model}[/green]")
        self.console.print("Type [bold]/help[/bold] for commands, [bold]/exit[/bold] to quit.\n")

        while True:
            try:
                # Dynamic prompt based on multiline mode
                prompt = '... ' if self.multiline_mode else '>>> '
                user_input = self.prompt_session.prompt(
                    prompt,
                    multiline=self.multiline_mode
                )

                if not user_input.strip():
                    self.multiline_mode = False
                    continue

                # Handle commands
                if user_input.startswith('/'):
                    self.handle_command(user_input)
                    continue

                # Send to LLM
                self.chat(user_input)
                self.multiline_mode = False

            except KeyboardInterrupt:
                self.console.print("\n[yellow]Interrupted. Type /exit to quit.[/yellow]")
                self.multiline_mode = False
                continue
            except EOFError:
                self.console.print("\n[blue]Goodbye![/blue]")
                break

    def handle_command(self, command: str):
        """Handle slash commands."""
        cmd = command.strip().lower()

        if cmd in ['/exit', '/quit', '/q']:
            self.console.print("[blue]Goodbye![/blue]")
            sys.exit(0)

        elif cmd == '/help':
            self.show_help()

        elif cmd == '/clear':
            self.session.conversation.clear()
            self.console.print("[green]Conversation cleared.[/green]")

        elif cmd == '/save':
            self.save_session()

        elif cmd == '/multiline':
            self.multiline_mode = not self.multiline_mode
            status = "enabled" if self.multiline_mode else "disabled"
            self.console.print(f"[green]Multiline mode {status}.[/green]")
            if self.multiline_mode:
                self.console.print("[dim]Press Meta+Enter or Esc+Enter to submit.[/dim]")

        elif cmd.startswith('/load'):
            parts = command.strip().split(maxsplit=1)
            if len(parts) < 2:
                self.console.print("[red]Usage: /load <session-id>[/red]")
            else:
                session_id = parts[1]
                self.load_session(session_id)

        else:
            self.console.print(f"[red]Unknown command: {command}[/red]")

    def show_help(self):
        """Show help message."""
        help_text = """
**Available Commands:**

- `/help` - Show this help message
- `/exit`, `/quit`, `/q` - Exit the REPL
- `/clear` - Clear conversation history
- `/save` - Save current session
- `/load <session-id>` - Load a previous session
- `/multiline` - Toggle multiline input mode

**Usage:**
- Type your message and press Enter to chat
- Use Tab for command completion
- Press Ctrl+C to interrupt current operation
- Press Ctrl+D to exit
- Use `/multiline` for multi-paragraph inputs
"""
        self.console.print(Markdown(help_text))

    def chat(self, user_input: str):
        """Send message to LLM and display response."""
        # Add user message
        self.session.conversation.add_message("user", user_input)

        try:
            # Call LLM (streaming)
            self.console.print("\n[bold green]Assistant:[/bold green]")

            response_text = ""
            for chunk in self.provider.chat_stream(self.session.conversation.get_messages()):
                response_text += chunk
                self.console.print(chunk, end="", style="green")

            self.console.print("\n")

            # Add assistant message
            self.session.conversation.add_message("assistant", response_text)

        except Exception as e:
            self.console.print(f"\n[red]Error: {e}[/red]")
            import traceback
            traceback.print_exc()

    def save_session(self):
        """Save current session."""
        self.session.save()
        self.console.print(f"[green]Session saved: {self.session.session_id}[/green]")

    def load_session(self, session_id: str):
        """Load a previous session.

        Args:
            session_id: Session ID to load
        """
        from src.agent import Session

        loaded_session = Session.load(session_id)
        if loaded_session is None:
            self.console.print(f"[red]Session not found: {session_id}[/red]")
            return

        # Replace current session
        self.session = loaded_session
        self.console.print(f"[green]Session loaded: {session_id}[/green]")
        self.console.print(f"[dim]Provider: {loaded_session.provider}, Model: {loaded_session.model}[/dim]")
        self.console.print(f"[dim]Messages: {len(loaded_session.conversation.messages)}[/dim]")

        # Show conversation history
        if loaded_session.conversation.messages:
            self.console.print("\n[bold]Conversation History:[/bold]")
            for msg in loaded_session.conversation.messages[-5:]:  # Show last 5 messages
                role_color = "blue" if msg.role == "user" else "green"
                self.console.print(f"[{role_color}]{msg.role}[/{role_color}]: {msg.content[:100]}...")

