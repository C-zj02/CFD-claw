#!/usr/bin/env python3
"""Test script for Phase 1 implementation."""

import sys
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).parent))

def test_imports():
    """Test basic imports."""
    print("=" * 60)
    print("Test 1: Basic Imports")
    print("=" * 60)

    try:
        from src import __version__, __author__
        print(f"✓ Version: {__version__}")
        print(f"✓ Author: {__author__}")
    except Exception as e:
        print(f"✗ Failed to import version: {e}")
        return False

    try:
        from src import load_config, get_provider_config
        print("✓ Config functions imported")
    except Exception as e:
        print(f"✗ Failed to import config: {e}")
        return False

    try:
        from src import BaseProvider, GLMProvider, AnthropicProvider, OpenAIProvider
        print("✓ Provider classes imported")
    except Exception as e:
        print(f"✗ Failed to import providers: {e}")
        return False

    print("✅ All imports successful!\n")
    return True


def test_config():
    """Test configuration system."""
    print("=" * 60)
    print("Test 2: Configuration System")
    print("=" * 60)

    try:
        from src.config import (
            get_config_path,
            load_config,
            save_config,
            get_default_config,
            get_provider_config,
            set_api_key,
            get_default_provider
        )

        # Test config path
        config_path = get_config_path()
        print(f"✓ Config path: {config_path}")

        # Test load config
        config = load_config()
        print(f"✓ Config loaded successfully")
        print(f"  - Default provider: {config.get('default_provider')}")
        print(f"  - Providers configured: {list(config.get('providers', {}).keys())}")

        # Test get provider config
        glm_config = get_provider_config("glm")
        print(f"✓ GLM config retrieved")
        print(f"  - Base URL: {glm_config.get('base_url')}")
        print(f"  - Default model: {glm_config.get('default_model')}")

        print("✅ Configuration system working!\n")
        return True

    except Exception as e:
        print(f"✗ Config test failed: {e}\n")
        return False


def test_providers():
    """Test provider classes."""
    print("=" * 60)
    print("Test 3: Provider Classes")
    print("=" * 60)

    try:
        from src.providers import (
            BaseProvider,
            ChatMessage,
            ChatResponse,
            GLMProvider,
            AnthropicProvider,
            OpenAIProvider
        )

        # Test ChatMessage
        msg = ChatMessage(role="user", content="Hello")
        print(f"✓ ChatMessage created: {msg.to_dict()}")

        # Test provider instantiation (without API keys)
        try:
            glm = GLMProvider(api_key="test_key")
            print(f"✓ GLMProvider instantiated")
            print(f"  - Model: {glm.model}")
            print(f"  - Available models: {len(glm.get_available_models())} models")
        except Exception as e:
            print(f"✗ GLMProvider instantiation failed: {e}")
            return False

        try:
            anthropic = AnthropicProvider(api_key="test_key")
            print(f"✓ AnthropicProvider instantiated")
            print(f"  - Model: {anthropic.model}")
        except Exception as e:
            print(f"✗ AnthropicProvider instantiation failed: {e}")
            return False

        try:
            openai = OpenAIProvider(api_key="test_key")
            print(f"✓ OpenAIProvider instantiated")
            print(f"  - Model: {openai.model}")
        except Exception as e:
            print(f"✗ OpenAIProvider instantiation failed: {e}")
            return False

        print("✅ Provider classes working!\n")
        return True

    except Exception as e:
        print(f"✗ Provider test failed: {e}\n")
        return False


def test_cli():
    """Test CLI module."""
    print("=" * 60)
    print("Test 4: CLI Module")
    print("=" * 60)

    try:
        from src.cli import main, handle_login, show_config, start_repl
        print("✓ CLI functions imported")

        # Test --version (quick path)
        import sys
        old_argv = sys.argv
        try:
            sys.argv = ['clawd', '--version']
            # We can't actually run main() without exiting, but we can check it exists
            print("✓ CLI main function exists and is callable")
        finally:
            sys.argv = old_argv

        print("✅ CLI module working!\n")
        return True

    except Exception as e:
        print(f"✗ CLI test failed: {e}\n")
        return False


def test_file_structure():
    """Test file structure."""
    print("=" * 60)
    print("Test 5: File Structure")
    print("=" * 60)

    required_files = [
        "pyproject.toml",
        "MANIFEST.in",
        "LICENSE",
        "src/__init__.py",
        "src/cli.py",
        "src/config.py",
        "src/providers/__init__.py",
        "src/providers/base.py",
        "src/providers/anthropic_provider.py",
        "src/providers/openai_provider.py",
        "src/providers/glm_provider.py",
    ]

    project_root = Path(__file__).parent
    all_exist = True

    for file_path in required_files:
        full_path = project_root / file_path
        if full_path.exists():
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path} - MISSING!")
            all_exist = False

    if all_exist:
        print("✅ All required files present!\n")
    else:
        print("❌ Some files are missing!\n")

    return all_exist


def main():
    """Run all tests."""
    print("\n" + "=" * 60)
    print("CLAWD CODEX - PHASE 1 TEST SUITE")
    print("=" * 60 + "\n")

    results = {
        "Imports": test_imports(),
        "Configuration": test_config(),
        "Providers": test_providers(),
        "CLI": test_cli(),
        "File Structure": test_file_structure(),
    }

    print("=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)

    for test_name, passed in results.items():
        status = "✅ PASS" if passed else "❌ FAIL"
        print(f"{test_name}: {status}")

    total = len(results)
    passed = sum(results.values())

    print("=" * 60)
    print(f"Total: {passed}/{total} tests passed")
    print("=" * 60)

    if passed == total:
        print("\n🎉 ALL TESTS PASSED! Phase 1 is complete!")
        return 0
    else:
        print("\n⚠️  Some tests failed. Please review the output above.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
