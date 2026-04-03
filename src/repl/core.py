"""Interactive REPL for Clawd Codex."""

from __future__ import annotations

try:
    from prompt_toolkit import PromptSession
    from prompt_toolkit.history import FileHistory
    from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
    from prompt_toolkit.styles import Style
    from prompt_toolkit.completion import WordCompleter
    try:
        from prompt_toolkit.completion import FuzzyCompleter
    except Exception:  # pragma: no cover
        FuzzyCompleter = None  # type: ignore
    from prompt_toolkit.key_binding import KeyBindings
except ModuleNotFoundError:  # pragma: no cover
    class FileHistory:  # type: ignore
        def __init__(self, *args, **kwargs):
            pass

    class AutoSuggestFromHistory:  # type: ignore
        def __init__(self, *args, **kwargs):
            pass

    class Style:  # type: ignore
        @staticmethod
        def from_dict(*args, **kwargs):
            return None

    class WordCompleter:  # type: ignore
        def __init__(self, *args, **kwargs):
            pass
    FuzzyCompleter = None  # type: ignore

    class KeyBindings:  # type: ignore
        def __init__(self, *args, **kwargs):
            pass

    class PromptSession:  # type: ignore
        def __init__(self, *args, **kwargs):
            pass

        def prompt(self, *args, **kwargs):
            raise EOFError()

try:
    from rich.console import Console
    from rich.markdown import Markdown
except ModuleNotFoundError:  # pragma: no cover
    class Console:  # type: ignore
        def print(self, *args, **kwargs):
            return None

    class Markdown:  # type: ignore
        def __init__(self, text: str):
            self.text = text
from pathlib import Path
import sys
import json

from src.agent import Session
from src.config import get_provider_config
from src.providers import get_provider_class
from src.providers.base import ChatMessage
from src.tool_system.context import ToolContext
from src.tool_system.defaults import build_default_registry
from src.tool_system.protocol import ToolCall
from src.tool_system.agent_loop import ToolEvent, run_agent_loop, summarize_tool_result, summarize_tool_use


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

        self.tool_registry = build_default_registry()
        self.tool_context = ToolContext(workspace_root=Path.cwd())
        self.tool_context.ask_user = self._ask_user_questions

        # Prompt toolkit with tab completion
        history_file = Path.home() / ".clawd" / "history"
        history_file.parent.mkdir(parents=True, exist_ok=True)

        self._built_in_commands = [
            "/",
            "/help",
            "/exit",
            "/quit",
            "/q",
            "/clear",
            "/save",
            "/load",
            "/multiline",
            "/tools",
            "/tool",
        ]
        self.completer = WordCompleter(self._get_slash_command_words(), ignore_case=True)

        # Key bindings for multiline
        self.bindings = KeyBindings()
        if hasattr(self.bindings, "add"):
            @self.bindings.add("/")  # type: ignore[attr-defined]
            def _show_slash_completions(event):  # type: ignore[no-untyped-def]
                buf = event.current_buffer
                if buf.text == "":
                    buf.insert_text("/")
                    buf.start_completion(select_first=False)

        self.prompt_session = PromptSession(
            history=FileHistory(str(history_file)),
            auto_suggest=AutoSuggestFromHistory(),
            completer=self.completer,
            style=Style.from_dict({
                'prompt': 'bold blue',
            }),
            key_bindings=self.bindings,
            complete_while_typing=True,
        )

    def _ask_user_questions(self, questions: list[dict]) -> dict[str, str]:
        answers: dict[str, str] = {}
        for q in questions:
            question_text = str(q.get("question", "")).strip()
            options = q.get("options") or []
            multi = bool(q.get("multiSelect", False))
            if not question_text or not isinstance(options, list) or len(options) < 2:
                continue

            self.console.print(f"\n[bold]{question_text}[/bold]")
            labels: list[str] = []
            for i, opt in enumerate(options, start=1):
                label = str((opt or {}).get("label", "")).strip()
                desc = str((opt or {}).get("description", "")).strip()
                labels.append(label)
                self.console.print(f"  {i}. {label}  [dim]{desc}[/dim]")
            other_idx = len(labels) + 1
            self.console.print(f"  {other_idx}. Other  [dim]Provide custom text[/dim]")

            prompt = "Select (comma-separated) > " if multi else "Select > "
            raw = self.prompt_session.prompt(prompt).strip()
            if not raw:
                choice_str = "1"
            else:
                choice_str = raw

            selected: list[str] = []
            parts = [p.strip() for p in choice_str.split(",") if p.strip()]
            if not parts:
                parts = ["1"]
            for part in parts:
                try:
                    idx = int(part)
                except ValueError:
                    idx = -1
                if idx == other_idx:
                    free = self.prompt_session.prompt("Other > ").strip()
                    if free:
                        selected.append(free)
                    continue
                if 1 <= idx <= len(labels):
                    selected.append(labels[idx - 1])
            if not selected:
                selected = [labels[0]]
            answers[question_text] = ", ".join(selected) if multi else selected[0]
        return answers

    def _get_slash_command_words(self) -> list[str]:
        words = list(self._built_in_commands)
        try:
            from src.skills.loader import get_all_skills

            cwd = self.tool_context.cwd or self.tool_context.workspace_root
            for s in get_all_skills(project_root=cwd):
                words.append(f"/{s.name}")
        except Exception:
            pass
        deduped: list[str] = []
        seen: set[str] = set()
        for w in words:
            lw = w.lower()
            if lw in seen:
                continue
            seen.add(lw)
            deduped.append(w)
        return deduped

    def _refresh_completer(self) -> None:
        try:
            words = self._get_slash_command_words()
            try:
                base = WordCompleter(words, ignore_case=True, match_middle=True)
            except TypeError:
                base = WordCompleter(words, ignore_case=True)
            self.completer = FuzzyCompleter(base) if FuzzyCompleter is not None else base
            if hasattr(self, "prompt_session") and getattr(self.prompt_session, "completer", None) is not None:
                self.prompt_session.completer = self.completer
        except Exception:
            return

    def _show_slash_palette(self, query: str | None = None) -> None:
        q = (query or "").strip().lower()
        self.console.print("\n[bold]Available commands and skills:[/bold]")
        for cmd in self._built_in_commands:
            if cmd == "/":
                continue
            if q and q not in cmd.lower():
                continue
            self.console.print(f"  {cmd}")
        try:
            from src.skills.loader import get_all_skills

            cwd = self.tool_context.cwd or self.tool_context.workspace_root
            skills = list(get_all_skills(project_root=cwd))
            skills.sort(key=lambda s: s.name.lower())
            if skills:
                self.console.print("\n[bold]Skills:[/bold]")
                for s in skills:
                    if q and q not in s.name.lower() and q not in (s.description or "").lower():
                        continue
                    desc = (s.description or "").strip()
                    loaded = (getattr(s, "loaded_from", "") or "").strip()
                    tag = f"[{loaded}]" if loaded else ""
                    model = (getattr(s, "model", None) or "").strip()
                    allowed_tools = list(getattr(s, "allowed_tools", []) or [])
                    parts: list[str] = []
                    if tag:
                        parts.append(tag)
                    if model:
                        parts.append(f"model={model}")
                    if allowed_tools:
                        shown = ", ".join(allowed_tools[:6])
                        more = f" (+{len(allowed_tools) - 6})" if len(allowed_tools) > 6 else ""
                        parts.append(f"tools={shown}{more}")
                    meta = f"  [dim]{' · '.join(parts)}[/dim]" if parts else ""
                    suffix = f"  [dim]{desc}[/dim]" if desc else ""
                    self.console.print(f"  /{s.name}{meta}{suffix}")
        except Exception:
            pass
        self.console.print()

    def _shorten_path_text(self, text: str) -> str:
        root = str(self.tool_context.workspace_root)
        cwd = str(self.tool_context.cwd or self.tool_context.workspace_root)
        for base in (cwd, root):
            prefix = base.rstrip("/") + "/"
            if text.startswith(prefix):
                return "./" + text[len(prefix):]
            text = text.replace(prefix, "")
        return text

    def run(self):
        """Run the REPL."""
        from src import __version__
        import os

        # 🦊 GitHub/GitLab-style Fox Mascot ASCII Art
        fox_ascii = """[orange3]
          ^._.^
         / o o \\
        (   T   )
         `~---~'
        [/orange3]"""

        self.console.print(fox_ascii)
        self.console.print(f"[bold white]Clawd Codex [dim]v{__version__}[/dim][/bold white]")
        
        # Provider & Model Info
        provider_info = f"[dim]{self.provider.model} · {self.provider_name.upper()} Provider[/dim]"
        self.console.print(provider_info)

        # Current Directory (with home shortening)
        cwd = os.getcwd()
        home = os.path.expanduser("~")
        display_path = cwd.replace(home, "~") if cwd.startswith(home) else cwd
        self.console.print(f"[bold blue]{display_path}[/bold blue]\n")

        while True:
            try:
                self._refresh_completer()
                # Dynamic prompt based on multiline mode
                # Using '❯' for a modern feel
                prompt_text = '... ' if self.multiline_mode else '❯ '
                user_input = self.prompt_session.prompt(
                    prompt_text,
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
        raw = command.strip()
        if raw == "/":
            self._show_slash_palette()
            return
        if raw.startswith("/") and " " not in raw and raw.lower() not in (c.lower() for c in self._built_in_commands):
            query = raw[1:]
            if query:
                self._show_slash_palette(query=query)
                return
        cmd = raw.lower()

        if cmd in ['/exit', '/quit', '/q']:
            self.console.print("[blue]Goodbye![/blue]")
            sys.exit(0)

        elif cmd == '/help':
            self.show_help()

        elif cmd == '/tools':
            names = [spec.name for spec in self.tool_registry.list_specs()]
            names.sort(key=str.lower)
            self.console.print("\n[bold]Available tools:[/bold]")
            for name in names:
                self.console.print(f"  - {name}")
            self.console.print()

        elif cmd.startswith('/tool'):
            parts = command.strip().split(maxsplit=2)
            if len(parts) < 2:
                self.console.print("[red]Usage: /tool <name> <json-input>[/red]")
                return
            name = parts[1]
            payload = {}
            if len(parts) == 3:
                try:
                    payload = json.loads(parts[2])
                except json.JSONDecodeError as e:
                    self.console.print(f"[red]Invalid JSON input: {e}[/red]")
                    return
            try:
                result = self.tool_registry.dispatch(ToolCall(name=name, input=payload), self.tool_context)
            except Exception as e:
                self.console.print(f"[red]Tool error: {e}[/red]")
                return
            self.console.print("\n[bold]Tool result:[/bold]")
            self.console.print(json.dumps(result.output, indent=2, ensure_ascii=False))
            self.console.print()

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
            if raw.startswith("/"):
                if self._try_run_skill_slash(raw):
                    return
            self.console.print(f"[red]Unknown command: {command}[/red]")

    def _try_run_skill_slash(self, raw: str) -> bool:
        text = raw.strip()
        if not text.startswith("/"):
            return False
        body = text[1:]
        if not body:
            return False
        if body.split(maxsplit=1)[0].lower() in {c.lstrip("/").lower() for c in self._built_in_commands if c != "/"}:
            return False

        parts = body.split(maxsplit=1)
        skill_name = parts[0].strip()
        args = parts[1] if len(parts) > 1 else ""
        if not skill_name:
            return False

        try:
            result = self.tool_registry.dispatch(
                ToolCall(name="Skill", input={"skill": skill_name, "args": args}),
                self.tool_context,
            )
        except Exception as e:
            self.console.print(f"[red]Skill error: {e}[/red]")
            return True

        payload = result.output if isinstance(result.output, dict) else {}
        if result.is_error or not payload.get("success"):
            err = payload.get("error") if isinstance(payload.get("error"), str) else "Unknown skill error"
            self.console.print(f"[red]{err}[/red]")
            return True

        self.console.print(f"[dim]Launching skill: {payload.get('commandName', skill_name)}[/dim]")
        meta_parts: list[str] = []
        loaded = payload.get("loadedFrom")
        if isinstance(loaded, str) and loaded:
            meta_parts.append(f"source={loaded}")
        model = payload.get("model")
        if isinstance(model, str) and model:
            meta_parts.append(f"model={model}")
        tools = payload.get("allowedTools")
        if isinstance(tools, list) and tools:
            shown = ", ".join(str(t) for t in tools[:6])
            more = f" (+{len(tools) - 6})" if len(tools) > 6 else ""
            meta_parts.append(f"tools={shown}{more}")
        if meta_parts:
            self.console.print(f"[dim]{' · '.join(meta_parts)}[/dim]")

        prompt = payload.get("prompt")
        if not isinstance(prompt, str) or not prompt.strip():
            self.console.print("[red]Skill produced empty prompt[/red]")
            return True

        self.chat(prompt)
        return True

    def show_help(self):
        """Show help message."""
        help_text = """
**Available Commands:**

- `/` - Show all commands and skills
- `/help` - Show this help message
- `/exit`, `/quit`, `/q` - Exit the REPL
- `/clear` - Clear conversation history
- `/save` - Save current session
- `/load <session-id>` - Load a previous session
- `/multiline` - Toggle multiline input mode
- `/tools` - List available built-in tools
- `/tool <name> <json>` - Run a tool directly

**Usage:**
- Type your message and press Enter to chat
- Use Tab for command completion
- Press Ctrl+C to interrupt current operation
- Press Ctrl+D to exit
- Use `/multiline` for multi-paragraph inputs
"""
        self.console.print(Markdown(help_text))

    def _is_recoverable_tool_error(self, tool_name: str, tool_output) -> bool:
        if not isinstance(tool_name, str):
            return False
        if not isinstance(tool_output, dict):
            return False
        name = tool_name.strip().lower()
        err = tool_output.get("error")
        if not isinstance(err, str):
            return False
        e = err.lower()
        if name == "read" and e.startswith("file not found:"):
            p = err.split(":", 2)[-1].strip()
            if "/.clawd/skills/" in p or "\\.clawd\\skills\\" in p or "/.claude/skills/" in p or "\\.claude\\skills\\" in p:
                return True
        return False

    def chat(self, user_input: str):
        """Send message to LLM and display response."""
        # Add user message
        self.session.conversation.add_user_message(user_input)

        try:
            self.console.print("\n[bold]Assistant[/bold]")

            def on_event(ev: ToolEvent) -> None:
                if ev.kind == "tool_use":
                    summary = summarize_tool_use(ev.tool_name, ev.tool_input or {})
                    if isinstance(summary, str) and summary:
                        summary = self._shorten_path_text(summary)
                    suffix = f" [dim]({summary})[/dim]" if summary else ""
                    self.console.print(f"[dim]•[/dim] [cyan]{ev.tool_name}[/cyan]{suffix} [dim]running...[/dim]")
                    return
                if ev.kind == "tool_result":
                    if ev.is_error:
                        if self._is_recoverable_tool_error(ev.tool_name, ev.tool_output):
                            return
                        msg = ""
                        if isinstance(ev.tool_output, dict) and isinstance(ev.tool_output.get("error"), str):
                            msg = ev.tool_output["error"]
                        self.console.print(f"[red]  ↳ {msg or 'Error'}[/red]")
                        return
                    msg = summarize_tool_result(ev.tool_name, ev.tool_output)
                    if isinstance(msg, str):
                        prefix = f"{ev.tool_name} · "
                        if msg.startswith(prefix):
                            msg = msg[len(prefix):]
                        msg = self._shorten_path_text(msg)
                    self.console.print(f"[dim]  ↳ {msg}[/dim]")
                    return
                if ev.kind == "tool_error":
                    msg = ev.error or "Error"
                    self.console.print(f"[red]  ↳ {msg}[/red]")

            # Use agent loop with tools for any provider that supports it
            from rich.status import Status
            with self.console.status("[dim]Thinking...[/dim]", spinner="dots"):
                response_text = run_agent_loop(
                    conversation=self.session.conversation,
                    provider=self.provider,
                    tool_registry=self.tool_registry,
                    tool_context=self.tool_context,
                    verbose=False,
                    on_event=on_event,
                )
            
            self.console.print(Markdown(response_text))
            self.console.print("\n")

        except Exception as e:
            error_str = str(e)

            # Check for authentication errors
            if "401" in error_str or "authentication" in error_str.lower() or "令牌" in error_str:
                self.console.print(f"\n[red]❌ Authentication Error: {e}[/red]")
                self.console.print("\n[yellow]Your API key appears to be invalid or expired.[/yellow]")

                # Ask if user wants to reconfigure
                from rich.prompt import Prompt
                choice = Prompt.ask(
                    "\nWould you like to reconfigure your API key now?",
                    choices=["y", "n"],
                    default="y"
                )

                if choice == "y":
                    self._handle_relogin()
                else:
                    self.console.print("\n[dim]You can run [bold]clawd login[/bold] later to update your API key.[/dim]")
            else:
                # Generic error handling
                self.console.print(f"\n[red]Error: {e}[/red]")
                import traceback
                traceback.print_exc()

    def _handle_relogin(self):
        """Handle re-authentication when API key fails."""
        from rich.prompt import Prompt
        from src.config import set_api_key, set_default_provider

        self.console.print("\n[bold blue]🔑 Reconfigure API Key[/bold blue]\n")

        # Select provider
        provider = Prompt.ask(
            "Select LLM provider",
            choices=["anthropic", "openai", "glm"],
            default=self.provider_name
        )

        # Input API Key
        api_key = Prompt.ask(
            f"Enter {provider.upper()} API Key",
            password=True
        )

        if not api_key:
            self.console.print("\n[red]Error: API Key cannot be empty[/red]")
            return

        # Optional: Base URL
        self.console.print(f"\n[dim]Press Enter to keep current, or enter custom base URL[/dim]")
        base_url = Prompt.ask(
            f"{provider.upper()} Base URL (optional)",
            default=""
        )

        # Save configuration
        kwargs = {"api_key": api_key}
        if base_url:
            kwargs["base_url"] = base_url

        set_api_key(provider, **kwargs)
        set_default_provider(provider)

        self.console.print(f"\n[green]✓ {provider.upper()} API Key updated successfully![/green]\n")

        # Reinitialize provider
        from src.config import get_provider_config
        from src.providers import get_provider_class

        config = get_provider_config(provider)
        provider_class = get_provider_class(provider)

        self.provider = provider_class(
            api_key=config["api_key"],
            base_url=config.get("base_url"),
            model=config.get("default_model")
        )
        self.provider_name = provider

        self.console.print("[green]✓ Provider reinitialized. You can continue chatting![/green]\n")

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
