#!/usr/bin/env python3
"""End-to-End Test for MVP Release"""

import subprocess
import sys
from pathlib import Path

def test_installation():
    """Test 1: Package installation."""
    print("✓ Test 1: Package Installation")

    result = subprocess.run(
        ["pip", "install", "-e", "."],
        capture_output=True,
        text=True,
        cwd="/root/Clawd-Codex"
    )

    if result.returncode != 0:
        print(f"  ✗ Installation failed: {result.stderr}")
        return False

    print("  ✓ Package installed successfully")
    return True

def test_cli_commands():
    """Test 2: CLI commands."""
    print("\n✓ Test 2: CLI Commands")

    commands = [
        (["clawd", "--version"], "clawd-codex version"),
        (["clawd", "--help"], "Clawd Codex"),
    ]

    for cmd, expected in commands:
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode != 0 or expected not in result.stdout:
            print(f"  ✗ Command failed: {' '.join(cmd)}")
            print(f"     stdout: {result.stdout}")
            print(f"     stderr: {result.stderr}")
            return False
        print(f"  ✓ Command: {' '.join(cmd)}")

    return True

def test_api_integration():
    """Test 3: API integration (with GLM)."""
    print("\n✓ Test 3: API Integration")

    from src.providers import GLMProvider, ChatMessage
    import os
    from dotenv import load_dotenv

    load_dotenv()

    api_key = os.getenv("GLM_API_KEY")
    if not api_key:
        print("  ⊘ Skipped: GLM_API_KEY not set")
        return True

    provider = GLMProvider(api_key=api_key)
    messages = [ChatMessage(role="user", content="Say 'test ok' exactly")]

    try:
        response = provider.chat(messages)
        if len(response.content) > 0:
            print("  ✓ API integration works")
            print(f"    Response: {response.content[:50]}...")
            return True
        else:
            print(f"  ✗ Empty response")
            return False
    except Exception as e:
        print(f"  ✗ API call failed: {e}")
        return False

def test_repl_import():
    """Test 4: REPL import."""
    print("\n✓ Test 4: REPL Import")

    try:
        from src.repl import ClawdREPL
        print("  ✓ ClawdREPL imported successfully")
        return True
    except Exception as e:
        print(f"  ✗ Import failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_session_persistence():
    """Test 5: Session persistence."""
    print("\n✓ Test 5: Session Persistence")

    try:
        from src.agent import Session

        session = Session.create("test", "test-model")
        session.conversation.add_message("user", "test message")
        session.save()

        loaded = Session.load(session.session_id)
        if loaded and len(loaded.conversation.messages) == 1:
            print("  ✓ Session persistence works")
            print(f"    Session ID: {session.session_id}")
            return True
        else:
            print("  ✗ Session load failed")
            return False
    except Exception as e:
        print(f"  ✗ Session test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def test_package_build():
    """Test 6: Package build."""
    print("\n✓ Test 6: Package Build")

    result = subprocess.run(
        ["python", "-m", "build"],
        capture_output=True,
        text=True,
        cwd="/root/Clawd-Codex"
    )

    if result.returncode != 0:
        print(f"  ✗ Build failed: {result.stderr}")
        return False

    # Check dist directory
    dist_dir = Path("/root/Clawd-Codex/dist")
    if not dist_dir.exists():
        print("  ✗ dist/ directory not created")
        return False

    whl_files = list(dist_dir.glob("*.whl"))
    tar_files = list(dist_dir.glob("*.tar.gz"))

    if not whl_files or not tar_files:
        print("  ✗ Package files not generated")
        return False

    print("  ✓ Package builds successfully")
    print(f"    Wheel: {whl_files[0].name}")
    print(f"    Source: {tar_files[0].name}")
    return True

def main():
    print("=" * 60)
    print("End-to-End Test Suite for MVP Release")
    print("=" * 60)

    tests = [
        test_installation,
        test_cli_commands,
        test_api_integration,
        test_repl_import,
        test_session_persistence,
        test_package_build,
    ]

    results = []
    for test in tests:
        try:
            results.append(test())
        except Exception as e:
            print(f"\n✗ Test crashed: {e}")
            import traceback
            traceback.print_exc()
            results.append(False)

    print("\n" + "=" * 60)
    passed = sum(results)
    total = len(results)
    print(f"Final Results: {passed}/{total} tests passed")
    print("=" * 60)

    if all(results):
        print("\n🎉 ALL TESTS PASSED! Ready for release!")
        return 0
    else:
        print("\n❌ Some tests failed. Please review.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
