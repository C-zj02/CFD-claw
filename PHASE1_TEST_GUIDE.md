# Phase 1 Testing Guide

## Overview

Phase 1 has been completed with the following components:
- PyPI publishing configuration
- Configuration management system
- LLM Provider abstraction layer
- CLI entry point

## Testing Steps

### 1. Install Package in Editable Mode

```bash
source .venv/bin/activate
pip install -e .
```

Expected output: Package installed successfully with no errors.

### 2. Test --version Command

```bash
clawd --version
```

Expected output:
```
clawd-codex version 0.1.0 (Python)
```

Alternative tests:
```bash
python -m src.cli --version
python -m src.cli -v
python -m src.cli -V
```

### 3. Test --help Command

```bash
clawd --help
```

Expected output: Help message showing available commands and options.

### 4. Test Configuration System

```bash
# Show current configuration
clawd config

# Or using Python
python -c "from src.config import load_config; print(load_config())"
```

Expected output: Configuration file location and current settings.

### 5. Test Login Command (Interactive)

```bash
clawd login
```

Expected behavior:
- Prompts for provider selection (anthropic/openai/glm)
- Prompts for API key (masked input)
- Optionally prompts for base URL and default model
- Saves configuration successfully

### 6. Test Provider Imports

```bash
python -c "
from src.providers import GLMProvider, AnthropicProvider, OpenAIProvider
print('✓ All providers imported successfully')

glm = GLMProvider(api_key='test_key')
print(f'✓ GLMProvider created with model: {glm.model}')
print(f'✓ Available models: {glm.get_available_models()}')
"
```

Expected output: Providers imported and instantiated successfully.

### 7. Test GLM API Integration (with real API key)

First, ensure GLM API key is configured:
```bash
clawd login
# Select 'glm' and enter your API key
```

Then test:
```bash
python -c "
from src.providers import GLMProvider, ChatMessage
from src.config import get_provider_config

config = get_provider_config('glm')
provider = GLMProvider(
    api_key=config['api_key'],
    base_url=config.get('base_url'),
    model=config.get('default_model')
)

messages = [ChatMessage(role='user', content='你好')]
response = provider.chat(messages)

print(f'✓ Response: {response.content}')
print(f'✓ Model: {response.model}')
print(f'✓ Usage: {response.usage}')
"
```

Expected output: Successful response from GLM API.

### 8. Test Streaming (with real API key)

```bash
python -c "
from src.providers import GLMProvider, ChatMessage
from src.config import get_provider_config

config = get_provider_config('glm')
provider = GLMProvider(
    api_key=config['api_key'],
    base_url=config.get('base_url'),
    model=config.get('default_model')
)

messages = [ChatMessage(role='user', content='Count from 1 to 5')]

print('Streaming response:')
for chunk in provider.chat_stream(messages):
    print(chunk, end='', flush=True)
print()
"
```

Expected output: Streaming text response.

## Automated Test Suite

Run the comprehensive test suite:

```bash
python test_phase1.py
```

Expected output:
```
============================================================
CLAWD CODEX - PHASE 1 TEST SUITE
============================================================

[Test outputs...]

============================================================
TEST SUMMARY
============================================================
Imports: ✅ PASS
Configuration: ✅ PASS
Providers: ✅ PASS
CLI: ✅ PASS
File Structure: ✅ PASS
============================================================
Total: 5/5 tests passed
============================================================

🎉 ALL TESTS PASSED! Phase 1 is complete!
```

## File Structure Verification

Verify all required files exist:

```bash
# PyPI configuration
ls -l pyproject.toml MANIFEST.in LICENSE

# Core modules
ls -l src/__init__.py src/cli.py src/config.py

# Provider modules
ls -l src/providers/__init__.py
ls -l src/providers/base.py
ls -l src/providers/anthropic_provider.py
ls -l src/providers/openai_provider.py
ls -l src/providers/glm_provider.py
```

## Success Criteria

Phase 1 is complete when:
- ✅ `clawd --version` shows version 0.1.0
- ✅ `clawd login` configures API keys interactively
- ✅ `clawd config` displays current configuration
- ✅ All providers can be imported and instantiated
- ✅ GLM API integration works (chat and streaming)
- ✅ Configuration is persisted to `~/.clawd/config.json`

## Troubleshooting

### Import Errors

If you see import errors, ensure:
1. Virtual environment is activated: `source .venv/bin/activate`
2. Package is installed: `pip install -e .`
3. All dependencies are installed: `pip install -r requirements.txt`

### API Key Issues

If API calls fail:
1. Verify API key is set: `clawd config`
2. Check API key is valid (not masked as `********`)
3. Test API key directly with provider's SDK

### Configuration Issues

If configuration is not saved:
1. Check `~/.clawd/` directory exists and is writable
2. Verify JSON format in `~/.clawd/config.json`
3. Try deleting config file and running `clawd login` again

## Next Steps

After Phase 1 verification:
- Proceed to Phase 2: Tool System Development
- Implement MCP-like tool protocol
- Create tool registry and execution engine
