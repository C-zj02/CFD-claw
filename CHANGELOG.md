# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.0] - 2026-04-01

### Added

#### Core Features
- Multi-provider support for Anthropic, OpenAI, and GLM (Zhipu AI)
- Interactive REPL with prompt-toolkit integration
- Streaming response support for real-time output
- Session persistence and management
- Configuration management with encrypted API key storage

#### CLI Commands
- `clawd login` - Interactive API key configuration
- `clawd repl` - Start interactive REPL session
- `clawd config set-api-key` - Set provider API key
- `clawd config set-default-provider` - Set default provider

#### Provider Implementations
- **Anthropic Provider**: Full support for Claude models with streaming
- **OpenAI Provider**: Support for GPT models with streaming
- **GLM Provider**: Support for GLM-4 models with streaming

#### REPL Features
- Command history with persistent storage
- Auto-suggestions from history
- Slash commands: `/help`, `/exit`, `/clear`, `/save`, `/load`
- Syntax highlighting with Rich library
- Multi-line input support (basic)

#### Configuration System
- JSON-based configuration storage
- Base64-encoded API keys for basic obfuscation
- Provider-specific settings (API key, base URL, default model)
- Session auto-save option

#### Session Management
- Unique session ID generation
- Conversation history tracking
- Session save/load functionality
- Conversation clear operation

#### Code Quality
- Type hints for all public functions
- Abstract base class for provider implementations
- Data classes for structured data (ChatMessage, ChatResponse)
- Error handling and validation

#### Testing
- Unit tests for core components
- Integration tests for providers
- End-to-end tests for REPL functionality
- Test coverage for configuration management

### Technical Details

#### Architecture
- Modular provider system with base abstraction
- Conversation management with message history
- Configuration management layer
- REPL engine with prompt-toolkit

#### Dependencies
- `anthropic>=0.18.0` - Anthropic SDK
- `openai>=1.0.0` - OpenAI SDK
- `zhipuai>=2.0.0` - Zhipu AI SDK
- `prompt-toolkit>=3.0.0` - Interactive REPL
- `rich>=13.0.0` - Terminal formatting
- `python-dotenv>=1.0.0` - Environment variables

#### File Structure
```
src/
├── providers/          # LLM provider implementations
│   ├── base.py        # Abstract base class
│   ├── anthropic_provider.py
│   ├── openai_provider.py
│   └── glm_provider.py
├── repl/              # Interactive REPL
│   └── core.py
├── agent/             # Session management
│   ├── session.py
│   └── conversation.py
├── config.py          # Configuration management
└── cli.py             # CLI commands
```

### Known Limitations

- Tab completion not yet implemented
- Advanced multi-line editing needs improvement
- Session loading UI not fully implemented
- Token usage tracking not available for all providers
- No streaming support for reasoning content (experimental feature)

### Migration Notes

This is the initial MVP release. No migration needed.

### Future Roadmap

- [ ] Enhanced REPL with tab completion
- [ ] Advanced multi-line editing
- [ ] Token usage and cost tracking
- [ ] Custom prompt templates
- [ ] Temperature and other parameter configuration
- [ ] Plugin system for extensions
- [ ] Go language implementation
- [ ] Bilingual tutorial edition
- [ ] 24/7 auto-iteration system

---

## Release Notes

### v0.1.0 - MVP Release

This is the first public release of Clawd Codex, a complete reimplementation of Claude Code. This MVP includes:

- Full multi-provider support
- Interactive REPL
- Session management
- Configuration system
- Streaming responses
- Type-safe implementation

The focus was on building a solid foundation with clean architecture, comprehensive testing, and good developer experience. All core features are working and tested.

**Special Thanks**: This project is inspired by Claude Code and aims to provide an open-source alternative for learning and experimentation.

---

[0.1.0]: https://github.com/GPT-AGI/Clawd-Codex/releases/tag/v0.1.0
