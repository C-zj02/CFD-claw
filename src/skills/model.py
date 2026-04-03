from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Sequence


@dataclass(frozen=True)
class Skill:
    name: str
    description: str
    loaded_from: str  # 'skills' | 'commands' | 'bundled' | 'managed' | 'mcp'
    user_invocable: bool
    disable_model_invocation: bool
    content_length: int
    is_hidden: bool
    skill_root: Optional[str]


@dataclass(frozen=True)
class PromptSkill(Skill):
    when_to_use: Optional[str]
    version: Optional[str]
    model: Optional[str]
    allowed_tools: Sequence[str]
    arg_names: Sequence[str]
    context: Optional[str]  # 'inline' | 'fork'
    agent: Optional[str]
    effort: Optional[str]
    paths: Optional[Sequence[str]]
    markdown_content: str

