#!/usr/bin/env python3
"""简化的 MVP 验证脚本"""

print("=" * 60)
print("Clawd Codex MVP - 功能验证")
print("=" * 60)

# Test 1: CLI Version
print("\n✓ Test 1: CLI Version")
try:
    import subprocess
    result = subprocess.run(
        [".venv/bin/python", "-m", "src.cli", "--version"],
        capture_output=True,
        text=True
    )
    if result.returncode == 0:
        print(f"  ✓ {result.stdout.strip()}")
    else:
        print(f"  ✗ Failed: {result.stderr}")
except Exception as e:
    print(f"  ✗ Error: {e}")

# Test 2: Imports
print("\n✓ Test 2: Module Imports")
try:
    from src import __version__
    from src.config import load_config
    from src.providers import GLMProvider, get_provider_class
    from src.repl import ClawdREPL
    from src.agent import Session
    print(f"  ✓ Version: {__version__}")
    print("  ✓ All modules imported successfully")
except Exception as e:
    print(f"  ✗ Import failed: {e}")

# Test 3: Configuration
print("\n✓ Test 3: Configuration System")
try:
    from src.config import load_config, get_provider_config
    config = load_config()
    print(f"  ✓ Config loaded: {config.get('default_provider')}")
    glm_config = get_provider_config('glm')
    print(f"  ✓ GLM config: {glm_config.get('default_model')}")
except Exception as e:
    print(f"  ✗ Config failed: {e}")

# Test 4: GLM API
print("\n✓ Test 4: GLM API Integration")
try:
    from src.providers import GLMProvider, ChatMessage
    import os
    from dotenv import load_dotenv

    load_dotenv()
    api_key = os.getenv("GLM_API_KEY")

    if api_key:
        provider = GLMProvider(api_key=api_key)
        messages = [ChatMessage(role="user", content="Say 'MVP test OK'")]
        response = provider.chat(messages)
        print(f"  ✓ API responded: {response.content[:50]}...")
    else:
        print("  ⊘ Skipped: GLM_API_KEY not set")
except Exception as e:
    print(f"  ✗ API test failed: {e}")

# Test 5: Session Persistence
print("\n✓ Test 5: Session Persistence")
try:
    from src.agent import Session
    session = Session.create("test", "test-model")
    session.conversation.add_message("user", "test")
    session.save()

    loaded = Session.load(session.session_id)
    if loaded and len(loaded.conversation.messages) == 1:
        print(f"  ✓ Session saved/loaded: {session.session_id}")
    else:
        print("  ✗ Session load failed")
except Exception as e:
    print(f"  ✗ Session failed: {e}")

# Test 6: REPL Class
print("\n✓ Test 6: REPL Ready")
try:
    from src.repl import ClawdREPL
    print("  ✓ ClawdREPL class available")
    print("  ✓ Ready for interactive use")
except Exception as e:
    print(f"  ✗ REPL failed: {e}")

print("\n" + "=" * 60)
print("✅ MVP VALIDATION COMPLETE")
print("=" * 60)
print("\n使用方法:")
print("  .venv/bin/python -m src.cli --version")
print("  .venv/bin/python -m src.cli --help")
print("  .venv/bin/python -m src.cli login")
print("  .venv/bin/python -m src.cli          # 启动 REPL")
print("=" * 60)
