# Clawd Codex

[English](#english) | [中文](#中文)

---

<a name="english"></a>
## English

**A complete reimplementation of Claude Code source.**

This project is a **full-scale port and reconstruction** of Claude Code, maximizing fidelity to the original while introducing improvements. Python version is available now, with Go version in active development.

### Highlights

- **Complete Port** — Every command, tool, and subsystem rebuilt from the ground up
- **Maximum Fidelity** — Preserving the original architecture while optimizing implementations
- **Continuous Improvement** — Enhanced with better error handling, testing, and documentation

### Project Status

| Component | Status | Count |
|-----------|--------|-------|
| Commands | ✅ Ported | 150+ |
| Tools | ✅ Ported | 100+ |
| Subsystems | ✅ Ported | 28+ |
| Test Cases | ✅ Passing | 40+ |

### Roadmap

| Milestone | Status |
|-----------|--------|
| Python complete reimplementation | ✅ Done |
| Full test coverage | ✅ Done |
| Session management & persistence | ✅ Done |
| **Go version (full port)** | 🚧 In Progress |
| Bilingual tutorial edition | 📋 Planned |
| 24/7 auto-iteration system | 📋 Planned |

### Installation

```bash
# Clone the repository
git clone https://github.com/GPT-AGI/Clawd-Codex.git
cd Clawd-Codex

# Create virtual environment (recommended)
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install package in development mode
pip install -e .
```

### Quick Start

#### 1. Configure API Key

```bash
# Interactive login (recommended)
clawd login

# Or manually configure
clawd config set-api-key glm YOUR_API_KEY
clawd config set-default-provider glm
```

#### 2. Start Interactive REPL

```bash
# Start with default provider
clawd repl

# Start with specific provider
clawd repl --provider anthropic
clawd repl --provider openai
clawd repl --provider glm
```

#### 3. Basic Usage

```python
# In the REPL:
>>> Hello, how are you?           # Chat with AI
>>> /help                         # Show available commands
>>> /save                         # Save current session
>>> /clear                        # Clear conversation
>>> /exit                         # Exit REPL
```

#### 4. CLI Commands

```bash
# View reimplementation summary
python3 -m src.main summary

# List all ported commands
python3 -m src.main commands --limit 20

# Run tests
python3 -m unittest discover -s tests -v
```

### Configuration

#### API Keys

Clawd Codex supports multiple LLM providers:

- **Anthropic**: Get your API key from [console.anthropic.com](https://console.anthropic.com)
- **OpenAI**: Get your API key from [platform.openai.com](https://platform.openai.com)
- **GLM (Zhipu AI)**: Get your API key from [open.bigmodel.cn](https://open.bigmodel.cn)

#### Configuration File

Configuration is stored in `~/.clawd/config.json`:

```json
{
  "default_provider": "glm",
  "providers": {
    "anthropic": {
      "api_key": "...",
      "base_url": "https://api.anthropic.com",
      "default_model": "claude-sonnet-4-20250514"
    },
    "openai": {
      "api_key": "...",
      "base_url": "https://api.openai.com/v1",
      "default_model": "gpt-4"
    },
    "glm": {
      "api_key": "...",
      "base_url": "https://open.bigmodel.cn/api/paas/v4",
      "default_model": "glm-4.5"
    }
  }
}
```

#### Environment Variables (Optional)

You can also use environment variables:

```bash
export ANTHROPIC_API_KEY=your_key_here
export OPENAI_API_KEY=your_key_here
export GLM_API_KEY=your_key_here
```

### Features

- **Multi-Provider Support**: Seamlessly switch between Anthropic, OpenAI, and GLM
- **Interactive REPL**: Rich terminal UI with syntax highlighting and auto-suggestions
- **Session Persistence**: Save and load conversation sessions
- **Streaming Responses**: Real-time response streaming
- **Configuration Management**: Easy API key and provider configuration
- **Type-Safe**: Full type hints and runtime validation

### Development

```bash
# Run tests
python3 -m pytest tests/ -v

# Run specific test
python3 -m pytest tests/test_porting_workspace.py -v

# Format code (requires black and isort)
black src/ tests/
isort src/ tests/

# Type checking (requires mypy)
mypy src/
```

### Contributing

PRs welcome! We're building the most complete open-source Claude Code reimplementation together.

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for development guidelines.

### Disclaimer

- Independent reimplementation of Claude Code source for learning purposes
- Not affiliated with, endorsed by, or maintained by Anthropic
- We respect the original creators' intellectual property

---

<a name="中文"></a>
## 中文

**Claude Code 源码的完整重构实现。**

本项目是对 Claude Code 的**全量移植和重建**，在最大程度还原原始实现的同时引入改进。Python 版本现已可用，Go 版本正在积极开发中。

### 亮点

- **完整移植** — 每个命令、工具和子系统均从底层重建
- **最大程度还原** — 保留原始架构的同时优化实现
- **持续改进** — 增强错误处理、测试覆盖和文档

### 项目状态

| 组件 | 状态 | 数量 |
|------|------|------|
| 命令 | ✅ 已移植 | 150+ |
| 工具 | ✅ 已移植 | 100+ |
| 子系统 | ✅ 已移植 | 28+ |
| 测试用例 | ✅ 通过 | 40+ |

### 路线图

| 里程碑 | 状态 |
|--------|------|
| Python 完整重构 | ✅ 完成 |
| 完整测试覆盖 | ✅ 完成 |
| 会话管理与持久化 | ✅ 完成 |
| **Go 版本（完整移植）** | 🚧 开发中 |
| 中英文双语教学版 | 📋 计划中 |
| 24小时自动迭代系统 | 📋 计划中 |

### 安装

```bash
# 克隆仓库
git clone https://github.com/GPT-AGI/Clawd-Codex.git
cd Clawd-Codex

# 创建虚拟环境（推荐）
python3 -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt

# 开发模式安装
pip install -e .
```

### 快速开始

#### 1. 配置 API Key

```bash
# 交互式登录（推荐）
clawd login

# 或手动配置
clawd config set-api-key glm YOUR_API_KEY
clawd config set-default-provider glm
```

#### 2. 启动交互式 REPL

```bash
# 使用默认 provider 启动
clawd repl

# 使用指定 provider 启动
clawd repl --provider anthropic
clawd repl --provider openai
clawd repl --provider glm
```

#### 3. 基本使用

```python
# 在 REPL 中：
>>> 你好，最近怎么样？           # 与 AI 聊天
>>> /help                         # 显示可用命令
>>> /save                         # 保存当前会话
>>> /clear                        # 清空对话
>>> /exit                         # 退出 REPL
```

#### 4. CLI 命令

```bash
# 查看重构摘要
python3 -m src.main summary

# 列出所有已移植命令
python3 -m src.main commands --limit 20

# 运行测试
python3 -m unittest discover -s tests -v
```

### 配置

#### API Keys

Clawd Codex 支持多个 LLM 提供商：

- **Anthropic**: 从 [console.anthropic.com](https://console.anthropic.com) 获取 API key
- **OpenAI**: 从 [platform.openai.com](https://platform.openai.com) 获取 API key
- **GLM (智谱 AI)**: 从 [open.bigmodel.cn](https://open.bigmodel.cn) 获取 API key

#### 配置文件

配置存储在 `~/.clawd/config.json`：

```json
{
  "default_provider": "glm",
  "providers": {
    "anthropic": {
      "api_key": "...",
      "base_url": "https://api.anthropic.com",
      "default_model": "claude-sonnet-4-20250514"
    },
    "openai": {
      "api_key": "...",
      "base_url": "https://api.openai.com/v1",
      "default_model": "gpt-4"
    },
    "glm": {
      "api_key": "...",
      "base_url": "https://open.bigmodel.cn/api/paas/v4",
      "default_model": "glm-4.5"
    }
  }
}
```

#### 环境变量（可选）

也可以使用环境变量：

```bash
export ANTHROPIC_API_KEY=your_key_here
export OPENAI_API_KEY=your_key_here
export GLM_API_KEY=your_key_here
```

### 功能特性

- **多 Provider 支持**: 在 Anthropic、OpenAI 和 GLM 之间无缝切换
- **交互式 REPL**: 丰富的终端 UI，支持语法高亮和自动建议
- **会话持久化**: 保存和加载对话会话
- **流式响应**: 实时响应流
- **配置管理**: 简单的 API key 和 provider 配置
- **类型安全**: 完整的类型提示和运行时验证

### 开发

```bash
# 运行测试
python3 -m pytest tests/ -v

# 运行特定测试
python3 -m pytest tests/test_porting_workspace.py -v

# 格式化代码（需要 black 和 isort）
black src/ tests/
isort src/ tests/

# 类型检查（需要 mypy）
mypy src/
```

### 参与贡献

欢迎提交 PR！我们正在共同构建最完整的 Claude Code 开源重构实现。

请阅读 [CONTRIBUTING.md](CONTRIBUTING.md) 了解开发指南。

### 免责声明

- 对 Claude Code 源码的独立重构实现，用于学习目的
- 不隶属于 Anthropic，未被其认可或维护
- 我们尊重原始创作者的知识产权

---

<p align="center">
Star ⭐ | Fork 🍴 | Watch 👀
</p>
