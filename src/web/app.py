"""Local browser UI for Clawd Codex."""

from __future__ import annotations

import json
import threading
from dataclasses import dataclass, field
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any
from urllib.parse import urlparse
from uuid import uuid4

from src.agent import Session
from src.config import get_provider_config, load_config
from src.providers import PROVIDER_INFO, get_provider_class
from src.tool_system import ToolContext
from src.tool_system.agent_loop import (
    ToolEvent,
    run_agent_loop,
    summarize_tool_result,
    summarize_tool_use,
)
from src.tool_system.defaults import build_default_registry
from src.tool_system.registry import ToolRegistry
from src.web.rag_service import RagIndexService


AUTO_SKILL_SYSTEM_TEMPLATE = """Web session skill policy:
- The user selected the `{skill_name}` skill for this browser session.
- For every user request that can benefit from local project knowledge or retrieval, proactively call the Skill tool before answering.
- Invoke it as: Skill({{"skill": "{skill_name}", "args": <the user's latest request>}}).
- Treat the skill output as grounding evidence and mention when the selected skill does not contain enough evidence.
- If this message already includes browser-attached RAG evidence for `{skill_name}`, treat that evidence as the skill having already been used for this turn; call the Skill tool again only if the attached evidence is insufficient.
- If the attached RAG evidence says the local index is building or not ready, do not call the Skill tool again in this turn; tell the user retrieval is warming up and answer only from clearly available context.
- Do not wait for the user to type the slash command manually."""


INDEX_HTML = """<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>飞行器设计工作台</title>
  <style>
    :root {
      --bg: #f4f6f2;
      --bg-accent: #dce8e0;
      --panel: rgba(255, 253, 248, 0.94);
      --panel-strong: #fffefa;
      --ink: #1d2a24;
      --muted: #5b6b63;
      --line: rgba(39, 58, 49, 0.12);
      --primary: #1f6d55;
      --primary-strong: #124c3b;
      --sky: #2f6f8f;
      --warm: #d9895b;
      --user: #193b52;
      --tool-bg: #eef5f1;
      --danger: #a53c30;
      --shadow: 0 18px 44px rgba(32, 47, 40, 0.1);
      --radius-xl: 18px;
      --radius-lg: 10px;
      --radius-md: 8px;
    }

    * { box-sizing: border-box; }

    html, body {
      height: 100%;
      margin: 0;
      color: var(--ink);
      background:
        radial-gradient(circle at top left, rgba(217, 137, 91, 0.18), transparent 34%),
        radial-gradient(circle at top right, rgba(31, 109, 85, 0.18), transparent 26%),
        linear-gradient(180deg, #f6f1e7 0%, var(--bg) 56%, #ecf2ea 100%);
      font-family: "IBM Plex Sans", "Avenir Next", "Segoe UI", sans-serif;
    }

    body {
      padding: 16px;
    }

    .shell {
      display: grid;
      grid-template-columns: 380px minmax(0, 1fr);
      gap: 14px;
      height: calc(100vh - 32px);
    }

    .panel {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: var(--radius-xl);
      box-shadow: var(--shadow);
      backdrop-filter: blur(12px);
    }

    .sidebar {
      padding: 18px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      overflow: auto;
    }

    .brand {
      padding: 16px;
      border-radius: var(--radius-lg);
      background:
        linear-gradient(145deg, rgba(255,255,255,0.94), rgba(245, 240, 231, 0.96)),
        linear-gradient(145deg, rgba(31, 109, 85, 0.1), rgba(47, 111, 143, 0.08));
      border: 1px solid rgba(31, 109, 85, 0.12);
    }

    .eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 5px 9px;
      border-radius: 999px;
      background: rgba(31, 109, 85, 0.1);
      color: var(--primary-strong);
      font-size: 12px;
      letter-spacing: 0;
    }

    .brand h1 {
      margin: 12px 0 8px;
      font-family: "Iowan Old Style", "Palatino Linotype", serif;
      font-size: 29px;
      line-height: 1.08;
      letter-spacing: 0;
    }

    .brand p {
      margin: 0;
      color: var(--muted);
      line-height: 1.5;
    }

    .workspace {
      margin-top: 12px;
      padding: 10px;
      background: rgba(31, 109, 85, 0.07);
      border-radius: var(--radius-md);
      font-size: 12px;
      color: var(--primary-strong);
      word-break: break-word;
    }

    .card {
      padding: 14px;
      border: 1px solid var(--line);
      border-radius: var(--radius-lg);
      background: var(--panel-strong);
    }

    .card h2 {
      margin: 0 0 12px;
      font-size: 15px;
      letter-spacing: 0.01em;
    }

    .field {
      display: flex;
      flex-direction: column;
      gap: 8px;
      margin-bottom: 14px;
    }

    .field:last-child {
      margin-bottom: 0;
    }

    .field-help {
      margin: -2px 0 0;
      color: var(--muted);
      font-size: 12px;
      line-height: 1.45;
    }

    .compact-grid {
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 10px;
    }

    .inline-field {
      margin-bottom: 0;
    }

    .mini-button {
      padding: 9px 12px;
      font-size: 12px;
    }

    .model-picker {
      display: grid;
      gap: 8px;
    }

    label {
      font-size: 13px;
      font-weight: 700;
      color: var(--primary-strong);
    }

    input[type="text"],
    input[type="number"],
    select,
    textarea {
      width: 100%;
      border: 1px solid rgba(29, 42, 36, 0.14);
      border-radius: 10px;
      background: #fffdf9;
      color: var(--ink);
      font: inherit;
      padding: 12px 14px;
      transition: border-color 140ms ease, box-shadow 140ms ease, transform 140ms ease;
    }

    input[readonly] {
      color: var(--primary-strong);
      background: rgba(31, 109, 85, 0.06);
      border-color: rgba(31, 109, 85, 0.18);
    }

    textarea {
      min-height: 76px;
      max-height: 220px;
      resize: vertical;
      line-height: 1.45;
    }

    input[type="number"] {
      appearance: textfield;
    }

    input:focus,
    select:focus,
    textarea:focus {
      outline: none;
      border-color: rgba(31, 109, 85, 0.55);
      box-shadow: 0 0 0 4px rgba(31, 109, 85, 0.12);
    }

    .toggle {
      display: flex;
      align-items: center;
      gap: 12px;
      padding: 11px 12px;
      border-radius: 10px;
      background: rgba(31, 109, 85, 0.07);
      color: var(--primary-strong);
      font-size: 14px;
    }

    .toggle input {
      accent-color: var(--primary);
      width: 18px;
      height: 18px;
    }

    .skill-card {
      background:
        linear-gradient(145deg, rgba(31, 109, 85, 0.06), rgba(47, 111, 143, 0.06)),
        var(--panel-strong);
    }

    .settings-panel {
      margin: 12px 0;
      border: 1px solid rgba(31, 109, 85, 0.12);
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.52);
    }

    .settings-panel summary {
      cursor: pointer;
      padding: 11px 12px;
      color: var(--primary-strong);
      font-size: 13px;
      font-weight: 700;
      list-style: none;
    }

    .settings-panel summary::-webkit-details-marker {
      display: none;
    }

    .settings-panel[open] summary {
      border-bottom: 1px solid rgba(31, 109, 85, 0.1);
    }

    .settings-panel-body {
      padding: 12px;
    }

    .skill-status {
      display: flex;
      align-items: center;
      gap: 8px;
      margin-top: 12px;
      color: var(--primary-strong);
      font-size: 13px;
      font-weight: 700;
      line-height: 1.4;
    }

    .skill-status::before {
      content: "";
      width: 9px;
      height: 9px;
      border-radius: 999px;
      background: var(--primary);
      box-shadow: 0 0 0 4px rgba(31, 109, 85, 0.1);
    }

    .rag-index-status {
      margin-top: 10px;
      padding: 10px 12px;
      border: 1px solid rgba(31, 109, 85, 0.12);
      border-radius: 10px;
      background: rgba(255, 255, 255, 0.58);
      color: var(--muted);
      font-size: 12px;
      line-height: 1.45;
    }

    .rag-index-status strong {
      display: block;
      color: var(--primary-strong);
      font-size: 13px;
    }

    .rag-index-status.warning strong {
      color: var(--danger);
    }

    .session-list {
      display: flex;
      flex-direction: column;
      gap: 8px;
      max-height: 220px;
      overflow: auto;
    }

    .session-item {
      width: 100%;
      border-radius: 10px;
      padding: 10px 12px;
      text-align: left;
      background: rgba(31, 109, 85, 0.06);
      color: var(--ink);
      border: 1px solid rgba(31, 109, 85, 0.1);
      box-shadow: none;
    }

    .session-item:hover {
      transform: none;
      background: rgba(31, 109, 85, 0.1);
    }

    .session-item.active {
      border-color: rgba(31, 109, 85, 0.35);
      background: rgba(31, 109, 85, 0.14);
    }

    .session-item strong,
    .session-item span {
      display: block;
    }

    .session-item strong {
      font-size: 12px;
      color: var(--primary-strong);
    }

    .session-item span {
      margin-top: 4px;
      color: var(--muted);
      font-size: 12px;
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
    }

    .rag-results {
      display: none;
      margin-top: 12px;
    }

    .rag-results.visible {
      display: block;
    }

    .actions {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }

    button {
      border: 0;
      border-radius: 10px;
      padding: 12px 18px;
      font: inherit;
      font-weight: 700;
      cursor: pointer;
      transition: transform 140ms ease, box-shadow 140ms ease, opacity 140ms ease;
    }

    button:hover {
      transform: translateY(-1px);
    }

    button:disabled {
      opacity: 0.55;
      cursor: wait;
      transform: none;
    }

    .primary {
      background: linear-gradient(135deg, var(--primary), var(--primary-strong));
      color: white;
      box-shadow: 0 12px 20px rgba(18, 76, 59, 0.16);
    }

    .secondary {
      background: white;
      color: var(--primary-strong);
      border: 1px solid rgba(31, 109, 85, 0.16);
    }

    .main {
      display: grid;
      grid-template-rows: auto minmax(0, 1fr) auto;
      overflow: hidden;
    }

    .topbar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 16px;
      padding: 16px 20px;
      border-bottom: 1px solid var(--line);
      background: rgba(255, 252, 247, 0.92);
    }

    .topbar h2 {
      margin: 0;
      font-size: 18px;
      letter-spacing: -0.02em;
    }

    .meta {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 8px;
      color: var(--muted);
      font-size: 13px;
    }

    .meta span {
      max-width: min(540px, 48vw);
      overflow: hidden;
      text-overflow: ellipsis;
      white-space: nowrap;
      padding: 3px 8px;
      border-radius: 999px;
      background: rgba(31, 109, 85, 0.06);
    }

    .badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      border-radius: 999px;
      padding: 8px 12px;
      background: rgba(31, 109, 85, 0.08);
      color: var(--primary-strong);
      font-size: 13px;
      font-weight: 700;
      flex: 0 0 auto;
      justify-content: center;
      min-width: 70px;
      white-space: nowrap;
    }

    .chat {
      padding: 20px;
      overflow: auto;
      display: flex;
      flex-direction: column;
      gap: 14px;
    }

    .hero {
      padding: 18px 20px;
      border: 1px solid rgba(29, 42, 36, 0.12);
      border-radius: 10px;
      background: linear-gradient(145deg, rgba(255,255,255,0.78), rgba(223, 236, 228, 0.78));
      color: var(--muted);
    }

    .hero strong {
      display: block;
      margin-bottom: 8px;
      color: var(--ink);
      font-size: 18px;
    }

    .message {
      display: flex;
      flex-direction: column;
      gap: 10px;
      max-width: min(920px, 100%);
      animation: fadeIn 180ms ease;
    }

    .message.user {
      align-self: flex-end;
    }

    .bubble {
      border-radius: 14px;
      padding: 16px 18px;
      box-shadow: 0 10px 22px rgba(22, 34, 28, 0.08);
      border: 1px solid rgba(20, 40, 32, 0.08);
      line-height: 1.55;
      word-break: break-word;
    }

    .bubble p {
      margin: 0 0 12px;
    }

    .bubble p:last-child {
      margin-bottom: 0;
    }

    .bubble ul,
    .bubble ol {
      margin: 8px 0 12px 22px;
      padding: 0;
    }

    .bubble blockquote {
      margin: 10px 0;
      padding-left: 12px;
      border-left: 3px solid rgba(31, 109, 85, 0.28);
      color: var(--muted);
    }

    .bubble pre {
      position: relative;
      margin: 12px 0;
      padding: 14px;
      border-radius: 14px;
      background: #16251e;
      color: #eff8f1;
      overflow: auto;
      white-space: pre;
    }

    .bubble code {
      border-radius: 8px;
      padding: 2px 6px;
      background: rgba(31, 109, 85, 0.08);
      color: var(--primary-strong);
      font-family: "IBM Plex Mono", "SFMono-Regular", monospace;
      font-size: 0.92em;
    }

    .bubble pre code {
      display: block;
      padding: 0;
      background: transparent;
      color: inherit;
      white-space: pre;
    }

    .message-tools {
      display: flex;
      justify-content: flex-end;
      gap: 8px;
      margin-top: -4px;
    }

    .message-tool-button,
    .code-copy {
      border-radius: 999px;
      padding: 6px 10px;
      font-size: 11px;
      color: var(--primary-strong);
      background: rgba(255, 255, 255, 0.86);
      border: 1px solid rgba(31, 109, 85, 0.14);
      box-shadow: none;
    }

    .code-copy {
      position: absolute;
      top: 8px;
      right: 8px;
      background: rgba(255, 255, 255, 0.12);
      color: white;
      border-color: rgba(255, 255, 255, 0.16);
    }

    .message.user .bubble {
      background: linear-gradient(135deg, var(--user), #335f7f);
      color: white;
      border-bottom-right-radius: 6px;
    }

    .message.assistant .bubble {
      background: rgba(255, 253, 249, 0.98);
      border-bottom-left-radius: 6px;
    }

    .message.system .bubble {
      background: rgba(217, 137, 91, 0.1);
      color: #6e452f;
    }

    .message-label {
      font-size: 12px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--muted);
      font-weight: 700;
    }

    details.tool-events {
      border-radius: 10px;
      background: var(--tool-bg);
      border: 1px solid rgba(31, 109, 85, 0.1);
      overflow: hidden;
    }

    details.tool-events summary {
      cursor: pointer;
      list-style: none;
      padding: 14px 16px;
      font-weight: 700;
      color: var(--primary-strong);
    }

    details.tool-events summary::-webkit-details-marker {
      display: none;
    }

    .event-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
      padding: 0 14px 14px;
    }

    .event {
      padding: 12px 14px;
      border-radius: 10px;
      background: white;
      border: 1px solid rgba(29, 42, 36, 0.08);
    }

    .event strong {
      display: block;
      margin-bottom: 6px;
      font-size: 13px;
    }

    .event code,
    .tips code {
      background: rgba(31, 109, 85, 0.08);
      color: var(--primary-strong);
      border-radius: 8px;
      padding: 2px 6px;
      font-family: "IBM Plex Mono", "SFMono-Regular", monospace;
      font-size: 12px;
    }

    .event pre {
      margin: 10px 0 0;
      padding: 10px 12px;
      border-radius: 10px;
      background: #f7faf8;
      font-size: 12px;
      overflow: auto;
      white-space: pre-wrap;
    }

    .event.is-error {
      border-color: rgba(165, 60, 48, 0.24);
      background: rgba(165, 60, 48, 0.06);
    }

    .evidence-panel {
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-top: 10px;
    }

    .evidence-summary {
      color: var(--muted);
      font-size: 12px;
    }

    .evidence-card {
      padding: 12px;
      border-radius: 10px;
      background: rgba(255, 253, 249, 0.94);
      border: 1px solid rgba(31, 109, 85, 0.12);
    }

    .evidence-card header {
      display: flex;
      justify-content: space-between;
      gap: 10px;
      color: var(--primary-strong);
      font-size: 12px;
      font-weight: 700;
    }

    .evidence-card p {
      margin: 8px 0 0;
      color: var(--ink);
      font-size: 13px;
      line-height: 1.45;
    }

    .evidence-path {
      word-break: break-word;
    }

    .composer {
      padding: 14px 20px 18px;
      border-top: 1px solid var(--line);
      background: rgba(255, 252, 247, 0.94);
    }

    .prompt-strip {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 10px;
    }

    .prompt-chip {
      padding: 7px 10px;
      border: 1px solid rgba(47, 111, 143, 0.16);
      background: rgba(47, 111, 143, 0.07);
      color: #24546d;
      box-shadow: none;
      font-size: 12px;
      font-weight: 700;
      white-space: nowrap;
    }

    .composer-row {
      display: grid;
      grid-template-columns: minmax(0, 1fr) 92px;
      gap: 12px;
      align-items: stretch;
    }

    .composer-actions {
      display: flex;
      flex-direction: column;
      gap: 8px;
    }

    .composer-actions button {
      width: 100%;
      min-height: 38px;
      padding: 9px 12px;
    }

    .hint {
      color: var(--muted);
      font-size: 13px;
      line-height: 1.5;
    }

    .status {
      color: var(--muted);
      font-size: 13px;
      min-height: 18px;
    }

    .warning {
      color: var(--danger);
      font-weight: 700;
    }

    @keyframes fadeIn {
      from { opacity: 0; transform: translateY(6px); }
      to { opacity: 1; transform: translateY(0); }
    }

    @media (max-width: 980px) {
      body {
        padding: 14px;
      }

      .shell {
        grid-template-columns: 1fr;
        height: auto;
        min-height: calc(100vh - 28px);
      }

      .main {
        min-height: 70vh;
      }

      .composer-row {
        grid-template-columns: 1fr;
      }

      .composer-actions {
        flex-direction: row;
      }

      .compact-grid {
        grid-template-columns: 1fr;
      }

      .topbar {
        align-items: flex-start;
        flex-direction: column;
      }

      .badge {
        align-self: flex-start;
      }

      .prompt-chip {
        white-space: normal;
      }
    }
  </style>
</head>
<body>
  <div class="shell">
    <aside class="panel sidebar">
      <section class="brand">
        <div class="eyebrow">飞行器设计智能体</div>
        <h1>飞行器设计工作台</h1>
        <p>面向总体方案、约束分析、RAG 证据检索和方案界限线图的本地设计界面。</p>
        <div class="workspace" id="workspaceRoot">正在加载工作区...</div>
      </section>

      <section class="card">
        <h2>设计会话</h2>
        <div class="field">
          <label for="providerSelect">模型服务</label>
          <select id="providerSelect"></select>
        </div>
        <div class="field">
          <label for="modelInput">模型</label>
          <div class="model-picker">
            <input id="modelInput" type="text" list="modelDatalist" value="deepseek-v4-pro" placeholder="deepseek-v4-pro" readonly>
            <datalist id="modelDatalist"></datalist>
          </div>
          <p class="field-help">当前网页端固定使用 deepseek-v4-pro。</p>
        </div>
        <div class="toggle">
          <input id="autoApproveToggle" type="checkbox" checked>
          <label for="autoApproveToggle">自动批准当前工作区内的工具权限请求</label>
        </div>
        <div class="actions">
          <button id="newSessionBtn" class="primary" type="button">新建设计会话</button>
          <button id="resetSessionBtn" class="secondary" type="button">清空对话</button>
        </div>
      </section>

      <section class="card">
        <h2>会话记录</h2>
        <div id="sessionList" class="session-list">
          <p class="hint">暂无活动的浏览器会话。</p>
        </div>
      </section>

      <section class="card skill-card">
        <h2>飞行器资料检索</h2>
        <div class="field">
          <label for="skillSelect">自动使用技能</label>
          <select id="skillSelect"></select>
          <p class="field-help">启用后，模型会在回答飞行器设计问题前优先调用所选技能。</p>
        </div>
        <div class="toggle">
          <input id="ragAutoRetrieveToggle" type="checkbox" checked>
          <label for="ragAutoRetrieveToggle">回答前附加本地 RAG 证据</label>
        </div>
        <details class="settings-panel">
          <summary>检索参数</summary>
          <div class="settings-panel-body">
            <div class="compact-grid">
              <div class="field inline-field">
                <label for="ragTopKInput">命中数量</label>
                <input id="ragTopKInput" type="number" min="1" max="20" value="5">
              </div>
              <div class="field inline-field">
                <label for="ragSnippetInput">片段字数</label>
                <input id="ragSnippetInput" type="number" min="80" max="3000" value="280">
              </div>
              <div class="field inline-field">
                <label for="ragCandidateInput">候选片段</label>
                <input id="ragCandidateInput" type="number" min="50" max="10000" value="1200">
              </div>
            </div>
            <div class="toggle">
              <input id="ragCacheToggle" type="checkbox" checked>
              <label for="ragCacheToggle">使用本地索引缓存</label>
            </div>
          </div>
        </details>
        <div class="actions">
          <button id="ragSearchBtn" class="secondary mini-button" type="button">测试检索</button>
          <button id="ragRebuildBtn" class="secondary mini-button" type="button">重建索引</button>
          <button id="ragRefreshBtn" class="secondary mini-button" type="button">刷新状态</button>
        </div>
        <div class="skill-status" id="skillStatus">未选择技能</div>
        <div class="rag-index-status" id="ragIndexStatus">索引状态未知。</div>
        <div id="ragSearchResults" class="rag-results"></div>
      </section>

      <section class="card tips">
        <h2>说明</h2>
        <p class="hint">网页端使用与命令行相同的模型服务配置；如未配置 API Key，请先运行 <code>clawd login</code>。</p>
        <p class="hint">飞行器设计问题建议选择 <code>aircraft-design-rag</code>，以便基于本地 <code>RAG-data</code> 检索资料。</p>
        <p class="hint">网页端会隐藏问卷式工具提示，保证会话响应更稳定。</p>
      </section>
    </aside>

    <main class="panel main">
      <header class="topbar">
        <div>
          <h2 id="sessionTitle">准备开始设计</h2>
          <div class="meta">
            <span id="providerMeta">模型服务：--</span>
            <span id="modelMeta">模型：--</span>
            <span id="skillMeta">技能：无</span>
            <span id="sessionMeta">会话：--</span>
          </div>
        </div>
        <div class="badge" id="statusBadge">空闲</div>
      </header>

      <section id="chatLog" class="chat">
        <div class="hero">
          <strong>飞行器设计流程</strong>
          围绕任务需求、总体参数、约束边界、动力与布局方案开展对话；每轮回答下方可展开查看检索证据和工具活动。
        </div>
      </section>

      <footer class="composer">
        <div class="status" id="statusLine"></div>
        <div class="prompt-strip" aria-label="常用飞行器设计任务">
          <button class="prompt-chip" type="button" data-prompt="设计一架航程 1200 km、载荷 500 kg 的固定翼无人机，给出总体参数、翼载、推重比和约束分析思路。">固定翼无人机总体方案</button>
          <button class="prompt-chip" type="button" data-prompt="基于本地资料，比较电推进、涡桨和活塞动力在中小型无人机方案中的适用边界。">动力方案对比</button>
          <button class="prompt-chip" type="button" data-prompt="为一架低速长航时飞行器梳理约束边界：失速、爬升、巡航、起飞距离和续航。">约束边界梳理</button>
        </div>
        <form id="composerForm" class="composer-row">
          <textarea id="promptInput" placeholder="输入飞行器设计需求，例如：设计一架航程 1200 km、载荷 500 kg 的固定翼无人机..."></textarea>
          <div class="composer-actions">
            <button id="sendBtn" class="primary" type="submit">发送</button>
            <button id="stopBtn" class="secondary" type="button" disabled>停止</button>
            <button id="clearDraftBtn" class="secondary" type="button">清空</button>
          </div>
        </form>
      </footer>
    </main>
  </div>

  <script>
    const STORAGE_KEY = "clawd-web-console";
    const WEB_MODEL = "deepseek-v4-pro";
    const state = {
      config: null,
      sessionId: null,
      provider: null,
      model: null,
      autoSkill: null,
      sessions: [],
      busy: false,
      abortController: null,
      ragStatus: null,
      ragPollTimer: null,
    };

    const providerSelect = document.getElementById("providerSelect");
    const modelInput = document.getElementById("modelInput");
    const modelDatalist = document.getElementById("modelDatalist");
    const skillSelect = document.getElementById("skillSelect");
    const ragAutoRetrieveToggle = document.getElementById("ragAutoRetrieveToggle");
    const ragTopKInput = document.getElementById("ragTopKInput");
    const ragSnippetInput = document.getElementById("ragSnippetInput");
    const ragCandidateInput = document.getElementById("ragCandidateInput");
    const ragCacheToggle = document.getElementById("ragCacheToggle");
    const ragSearchBtn = document.getElementById("ragSearchBtn");
    const ragRebuildBtn = document.getElementById("ragRebuildBtn");
    const ragRefreshBtn = document.getElementById("ragRefreshBtn");
    const ragSearchResults = document.getElementById("ragSearchResults");
    const autoApproveToggle = document.getElementById("autoApproveToggle");
    const newSessionBtn = document.getElementById("newSessionBtn");
    const resetSessionBtn = document.getElementById("resetSessionBtn");
    const sessionList = document.getElementById("sessionList");
    const chatLog = document.getElementById("chatLog");
    const promptInput = document.getElementById("promptInput");
    const sendBtn = document.getElementById("sendBtn");
    const stopBtn = document.getElementById("stopBtn");
    const clearDraftBtn = document.getElementById("clearDraftBtn");
    const statusLine = document.getElementById("statusLine");
    const statusBadge = document.getElementById("statusBadge");
    const sessionTitle = document.getElementById("sessionTitle");
    const providerMeta = document.getElementById("providerMeta");
    const modelMeta = document.getElementById("modelMeta");
    const skillMeta = document.getElementById("skillMeta");
    const sessionMeta = document.getElementById("sessionMeta");
    const workspaceRoot = document.getElementById("workspaceRoot");
    const skillStatus = document.getElementById("skillStatus");
    const ragIndexStatus = document.getElementById("ragIndexStatus");

    function setBusy(isBusy, label = "处理中...") {
      state.busy = isBusy;
      sendBtn.disabled = isBusy;
      newSessionBtn.disabled = isBusy;
      resetSessionBtn.disabled = isBusy;
      providerSelect.disabled = isBusy;
      modelInput.disabled = isBusy;
      skillSelect.disabled = isBusy;
      ragAutoRetrieveToggle.disabled = isBusy;
      ragTopKInput.disabled = isBusy;
      ragSnippetInput.disabled = isBusy;
      ragCandidateInput.disabled = isBusy;
      ragCacheToggle.disabled = isBusy;
      ragSearchBtn.disabled = isBusy;
      ragRebuildBtn.disabled = isBusy;
      ragRefreshBtn.disabled = isBusy;
      autoApproveToggle.disabled = isBusy;
      stopBtn.disabled = !isBusy;
      statusBadge.textContent = isBusy ? label : "空闲";
      statusLine.textContent = isBusy ? "正在运行设计智能体..." : "";
      if (state.config) updateSkillStatus();
    }

    function setStatus(message, isError = false) {
      statusLine.textContent = message || "";
      statusLine.className = "status" + (isError ? " warning" : "");
    }

    function autosizePrompt() {
      promptInput.style.height = "auto";
      promptInput.style.height = Math.min(promptInput.scrollHeight, 220) + "px";
    }

    function setPromptDraft(text) {
      promptInput.value = text || "";
      autosizePrompt();
      promptInput.focus();
      setStatus("已填入常用设计任务，可继续补充约束后发送。");
    }

    function saveLocalState() {
      const payload = {
        sessionId: state.sessionId,
        provider: providerSelect.value || state.provider,
        model: WEB_MODEL,
        autoSkill: skillSelect.value || null,
        autoApprove: autoApproveToggle.checked,
        ragSettings: getRagSettings(),
      };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(payload));
    }

    function loadLocalState() {
      try {
        const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || "null");
        if (saved) saved.autoSkill = null;
        return saved;
      } catch (_err) {
        return null;
      }
    }

    function clampNumber(value, fallback, min, max) {
      const parsed = Number.parseInt(value, 10);
      if (Number.isNaN(parsed)) return fallback;
      return Math.min(max, Math.max(min, parsed));
    }

    function getRagSettings() {
      return {
        auto_retrieve: ragAutoRetrieveToggle.checked,
        top_k: clampNumber(ragTopKInput.value, 5, 1, 20),
        max_snippet_chars: clampNumber(ragSnippetInput.value, 280, 80, 3000),
        candidate_limit: clampNumber(ragCandidateInput.value, 1200, 50, 10000),
        use_cache: ragCacheToggle.checked,
      };
    }

    function applyRagSettings(settings) {
      const defaults = state.config?.rag?.defaults || {};
      const merged = { ...defaults, ...(settings || {}) };
      ragAutoRetrieveToggle.checked = merged.auto_retrieve ?? true;
      ragTopKInput.value = merged.top_k ?? 5;
      ragSnippetInput.value = merged.max_snippet_chars ?? 280;
      ragCandidateInput.value = merged.candidate_limit ?? 1200;
      ragCacheToggle.checked = merged.use_cache ?? true;
    }

    async function api(path, options = {}) {
      const response = await fetch(path, {
        headers: {
          "Content-Type": "application/json",
          ...(options.headers || {}),
        },
        ...options,
      });
      const text = await response.text();
      let payload = {};
      try {
        payload = text ? JSON.parse(text) : {};
      } catch (_err) {
        payload = { error: text || response.statusText };
      }
      if (!response.ok) {
        throw new Error(payload.error || response.statusText);
      }
      return payload;
    }

    function providerByName(name) {
      return (state.config?.providers || []).find((item) => item.name === name) || null;
    }

    function populateProviders() {
      providerSelect.innerHTML = "";
      for (const provider of state.config.providers) {
        const option = document.createElement("option");
        option.value = provider.name;
        option.textContent = provider.label + (provider.configured ? "" : "（未配置 API Key）");
        option.disabled = !provider.configured;
        providerSelect.appendChild(option);
      }
    }

    function firstConfiguredProvider() {
      return (state.config?.providers || []).find((item) => item.configured) || null;
    }

    function preferredWebProvider() {
      const openaiProvider = providerByName("openai");
      if (openaiProvider?.configured) return openaiProvider;
      return firstConfiguredProvider();
    }

    function updateModelSuggestions() {
      modelDatalist.innerHTML = "";
      const provider = providerByName(providerSelect.value);
      for (const model of provider?.available_models || []) {
        const option = document.createElement("option");
        option.value = model;
        modelDatalist.appendChild(option);
      }
    }

    function populateSkills() {
      skillSelect.innerHTML = "";
      const noneOption = document.createElement("option");
      noneOption.value = "";
      noneOption.textContent = "不自动使用技能";
      skillSelect.appendChild(noneOption);

      for (const skill of state.config.skills || []) {
        const option = document.createElement("option");
        option.value = skill.name;
        option.textContent = skillDisplayName(skill.name);
        if (skill.description) option.title = skill.description;
        skillSelect.appendChild(option);
      }
    }

    function skillDisplayName(name) {
      if (!name) return "无";
      if (name === "aircraft-design-rag") return "飞行器设计资料检索（/aircraft-design-rag）";
      if (name === "aircraft-conceptual-design") return "飞行器概念设计（/aircraft-conceptual-design）";
      return "/" + name;
    }

    function updateSkillStatus() {
      const selected = skillSelect.value;
      const ragSelected = selected === "aircraft-design-rag";
      ragAutoRetrieveToggle.disabled = state.busy || !ragSelected;
      ragTopKInput.disabled = state.busy || !ragSelected;
      ragSnippetInput.disabled = state.busy || !ragSelected;
      ragCandidateInput.disabled = state.busy || !ragSelected;
      ragCacheToggle.disabled = state.busy || !ragSelected;
      ragSearchBtn.disabled = state.busy || !ragSelected;
      ragRebuildBtn.disabled = state.busy || !ragSelected;
      ragRefreshBtn.disabled = state.busy || !ragSelected;
      if (!selected) {
        skillStatus.textContent = "未选择技能";
        skillStatus.title = "";
        renderRagStatus(null);
        return;
      }
      const skill = (state.config?.skills || []).find((item) => item.name === selected);
      const ragNote = ragSelected && state.config?.rag?.available ? " · 检索器就绪" : "";
      skillStatus.textContent = "已启用自动技能：" + skillDisplayName(selected) + ragNote;
      if (skill?.description) skillStatus.title = skill.description;
      renderRagStatus(ragSelected ? state.ragStatus : null);
    }

    function applyConfigDefaults(preferred) {
      const provider = preferredWebProvider();
      providerSelect.value = provider?.name || state.config.default_provider;
      modelInput.value = WEB_MODEL;
      updateModelSuggestions();
      const preferredSkill = preferred?.autoSkill || "";
      const skillExists = preferredSkill && (state.config.skills || []).some((item) => item.name === preferredSkill);
      skillSelect.value = skillExists ? preferredSkill : "";
      updateSkillStatus();
      autoApproveToggle.checked = preferred?.autoApprove ?? true;
      applyRagSettings(preferred?.ragSettings);
    }

    function updateMeta(session) {
      sessionTitle.textContent = session.messages.length ? "飞行器设计会话" : "新的设计会话";
      providerMeta.textContent = "模型服务：" + session.provider;
      modelMeta.textContent = "模型：" + WEB_MODEL;
      skillMeta.textContent = "技能：" + skillDisplayName(session.auto_skill);
      sessionMeta.textContent = "会话：" + session.session_id;
      state.sessionId = session.session_id;
      state.provider = session.provider;
      state.model = WEB_MODEL;
      state.autoSkill = session.auto_skill || "";
      providerSelect.value = session.provider;
      modelInput.value = WEB_MODEL;
      skillSelect.value = state.autoSkill;
      applyRagSettings(session.rag_settings);
      updateSkillStatus();
      saveLocalState();
    }

    function escapeHtml(text) {
      return String(text || "")
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;")
        .replaceAll('"', "&quot;")
        .replaceAll("'", "&#39;");
    }

    function inlineMarkdown(text) {
      return escapeHtml(text)
        .replace(/`([^`]+)`/g, "<code>$1</code>")
        .replace(/\\*\\*([^*]+)\\*\\*/g, "<strong>$1</strong>");
    }

    function addCopyButton(container, text, label = "复制") {
      const button = document.createElement("button");
      button.type = "button";
      button.className = label === "复制代码" ? "code-copy" : "message-tool-button";
      button.textContent = label;
      button.addEventListener("click", async () => {
        try {
          await navigator.clipboard.writeText(text || "");
          const old = button.textContent;
          button.textContent = "已复制";
          window.setTimeout(() => { button.textContent = old; }, 900);
        } catch (_err) {
          button.textContent = "复制失败";
        }
      });
      container.appendChild(button);
    }

    function appendTextSegment(container, segment) {
      const lines = segment.replace(/\\r\\n/g, "\\n").split("\\n");
      let paragraph = [];
      let list = null;

      function flushParagraph() {
        if (!paragraph.length) return;
        const p = document.createElement("p");
        p.innerHTML = inlineMarkdown(paragraph.join(" "));
        container.appendChild(p);
        paragraph = [];
      }

      function flushList() {
        if (!list) return;
        container.appendChild(list.node);
        list = null;
      }

      for (const line of lines) {
        const trimmed = line.trim();
        if (!trimmed) {
          flushParagraph();
          flushList();
          continue;
        }
        const heading = trimmed.match(/^(#{1,3})\\s+(.+)$/);
        if (heading) {
          flushParagraph();
          flushList();
          const level = String(Math.min(3, heading[1].length + 2));
          const h = document.createElement("h" + level);
          h.innerHTML = inlineMarkdown(heading[2]);
          container.appendChild(h);
          continue;
        }
        const quote = trimmed.match(/^>\\s?(.+)$/);
        if (quote) {
          flushParagraph();
          flushList();
          const blockquote = document.createElement("blockquote");
          blockquote.innerHTML = inlineMarkdown(quote[1]);
          container.appendChild(blockquote);
          continue;
        }
        const bullet = trimmed.match(/^[-*]\\s+(.+)$/);
        const ordered = trimmed.match(/^\\d+\\.\\s+(.+)$/);
        if (bullet || ordered) {
          flushParagraph();
          const type = bullet ? "ul" : "ol";
          if (!list || list.type !== type) {
            flushList();
            list = { type, node: document.createElement(type) };
          }
          const li = document.createElement("li");
          li.innerHTML = inlineMarkdown((bullet || ordered)[1]);
          list.node.appendChild(li);
          continue;
        }
        flushList();
        paragraph.push(trimmed);
      }
      flushParagraph();
      flushList();
    }

    function renderMarkdownInto(container, text) {
      container.innerHTML = "";
      const source = text || "";
      if (!source) {
        container.textContent = "";
        return;
      }
      const parts = source.split(/```([\\s\\S]*?)```/g);
      for (let index = 0; index < parts.length; index += 1) {
        if (index % 2 === 0) {
          appendTextSegment(container, parts[index]);
          continue;
        }
        const raw = parts[index].replace(/^\\w+\\n/, "");
        const pre = document.createElement("pre");
        const code = document.createElement("code");
        code.textContent = raw.trimEnd();
        pre.appendChild(code);
        addCopyButton(pre, code.textContent, "复制代码");
        container.appendChild(pre);
      }
    }

    function renderPreview(value) {
      if (value == null || value === "") return "";
      if (typeof value === "string") return value;
      try {
        return JSON.stringify(value, null, 2);
      } catch (_err) {
        return String(value);
      }
    }

    function formatMs(value) {
      const number = Number(value);
      if (!Number.isFinite(number)) return "--";
      if (number >= 1000) return (number / 1000).toFixed(number >= 10000 ? 0 : 1) + "s";
      return Math.round(number) + "ms";
    }

    function formatCount(value) {
      const number = Number(value);
      if (!Number.isFinite(number)) return "--";
      return number.toLocaleString();
    }

    function renderRagStatus(status) {
      state.ragStatus = status || null;
      if (!skillSelect.value || skillSelect.value !== "aircraft-design-rag") {
        ragIndexStatus.className = "rag-index-status";
        ragIndexStatus.innerHTML = "<strong>RAG 索引</strong>选择 aircraft-design-rag 后可查看本地资料索引状态。";
        return;
      }
      if (!status) {
        ragIndexStatus.className = "rag-index-status";
        ragIndexStatus.innerHTML = "<strong>RAG 索引</strong>状态未知，请点击“刷新状态”。";
        return;
      }

      const rebuild = status.rebuild || {};
      const cache = status.cache || {};
      const running = Boolean(rebuild.running);
      const ready = Boolean(status.cache_ready);
      const stale = Boolean(status.cache_stale);
      const parts = [
        formatCount(status.markdown_files) + " 个文件",
        formatCount(cache.chunk_count) + " 个片段",
        "清单 " + formatMs(status.timings?.manifest_ms),
      ];
      if (running) parts.push("正在构建");
      if (rebuild.timings?.index_build_ms) parts.push("上次构建 " + formatMs(rebuild.timings.index_build_ms));

      let title = "索引就绪";
      if (running) title = "索引构建中";
      else if (!status.cache_exists) title = "索引不存在";
      else if (stale) title = "索引需要更新";
      ragIndexStatus.className = "rag-index-status" + (ready || running ? "" : " warning");
      ragIndexStatus.innerHTML = "<strong>" + escapeHtml(title) + "</strong>" + escapeHtml(parts.join(" · "));
      if (rebuild.error) {
        ragIndexStatus.innerHTML += "<br>" + escapeHtml("上次重建失败：" + rebuild.error);
      }
    }

    function createEvidencePanel(rag) {
      const panel = document.createElement("div");
      panel.className = "evidence-panel";
      const hits = Array.isArray(rag?.hits) ? rag.hits : [];
      const summary = document.createElement("div");
      summary.className = "evidence-summary";
      const cache = rag?.cache?.enabled
        ? (rag.cache.ready === false ? "索引预热中" : (rag.cache.hit ? "缓存命中" : "缓存未命中"))
        : "缓存关闭";
      summary.textContent = [
        "RAG 证据",
        "命中 " + hits.length,
        "文件 " + (rag?.markdown_files_scanned ?? "--"),
        "片段 " + (rag?.chunks_indexed ?? "--"),
        "候选 " + (rag?.candidate_chunks ?? "--"),
        "检索 " + formatMs(rag?.timings?.total_ms),
        cache,
      ].join(" · ");
      panel.appendChild(summary);

      if (rag?.message) {
        const note = document.createElement("div");
        note.className = "evidence-card";
        note.textContent = rag.message;
        panel.appendChild(note);
      }

      if (!hits.length && !rag?.message) {
        const empty = document.createElement("div");
        empty.className = "evidence-card";
        empty.textContent = "未找到匹配的本地证据。";
        panel.appendChild(empty);
        return panel;
      }

      for (const hit of hits.slice(0, 6)) {
        const card = document.createElement("div");
        card.className = "evidence-card";
        const header = document.createElement("header");
        const path = document.createElement("span");
        path.className = "evidence-path";
        path.textContent = (hit.file || "未知文件") + ":" + (hit.start_line || "?") + "-" + (hit.end_line || "?");
        const score = document.createElement("span");
        score.textContent = "得分 " + (hit.score ?? "--");
        header.appendChild(path);
        header.appendChild(score);
        card.appendChild(header);
        if (hit.heading) {
          const heading = document.createElement("p");
          heading.textContent = hit.heading;
          card.appendChild(heading);
        }
        const snippet = document.createElement("p");
        snippet.textContent = hit.snippet || "";
        card.appendChild(snippet);
        panel.appendChild(card);
      }
      return panel;
    }

    function renderRagResults(rag) {
      ragSearchResults.innerHTML = "";
      if (!rag) {
        ragSearchResults.classList.remove("visible");
        return;
      }
      ragSearchResults.appendChild(createEvidencePanel(rag));
      ragSearchResults.classList.add("visible");
    }

    function createMessage(role, text, events = []) {
      const wrapper = document.createElement("article");
      wrapper.className = "message " + role;

      const label = document.createElement("div");
      label.className = "message-label";
      label.textContent = role === "user" ? "你" : role === "assistant" ? "设计助手" : "系统";
      wrapper.appendChild(label);

      const bubble = document.createElement("div");
      bubble.className = "bubble";
      renderMarkdownInto(bubble, text || (role === "assistant" ? "[没有文本响应]" : ""));
      wrapper.appendChild(bubble);

      if (text) {
        const tools = document.createElement("div");
        tools.className = "message-tools";
        addCopyButton(tools, text);
        wrapper.appendChild(tools);
      }

      if (events.length) {
        const details = document.createElement("details");
        details.className = "tool-events";

        const summary = document.createElement("summary");
        summary.textContent = "工具活动（" + events.length + "）";
        details.appendChild(summary);

        const eventList = document.createElement("div");
        eventList.className = "event-list";

        for (const event of events) {
          const item = document.createElement("div");
          item.className = "event" + (event.is_error ? " is-error" : "");
          const title = document.createElement("strong");
          title.textContent = event.kind === "rag_retrieval"
            ? "RAG · 检索"
            : event.kind === "permission"
            ? "权限 · " + event.tool_name
            : event.tool_name + " · " + event.kind;
          item.appendChild(title);

          const body = document.createElement("div");
          body.textContent = event.summary || event.message || event.error || "";
          item.appendChild(body);

          if (event.rag) {
            item.appendChild(createEvidencePanel(event.rag));
          }

          const preview = event.rag ? "" : renderPreview(event.preview);
          if (preview) {
            const pre = document.createElement("pre");
            pre.textContent = preview;
            item.appendChild(pre);
          }

          eventList.appendChild(item);
        }

        details.appendChild(eventList);
        wrapper.appendChild(details);
      }

      return wrapper;
    }

    function clearRenderedMessages() {
      chatLog.innerHTML = "";
    }

    function renderHero() {
      const hero = document.createElement("div");
      hero.className = "hero";
      hero.innerHTML = "<strong>飞行器设计流程</strong><span>围绕任务需求、总体参数、约束边界、动力与布局方案开展对话；每轮回答下方可展开查看检索证据和工具活动。</span>";
      chatLog.appendChild(hero);
    }

    function renderMessages(messages) {
      clearRenderedMessages();
      if (!messages.length) {
        renderHero();
        return;
      }

      for (const message of messages) {
        if (!message.text && !message.blocks?.length) {
          continue;
        }
        let text = message.text || "";
        if (!text && message.blocks?.length) {
          text = message.blocks.map((block) => block.label).join("\\n");
        }
        chatLog.appendChild(createMessage(message.role, text));
      }
      chatLog.scrollTop = chatLog.scrollHeight;
    }

    function appendAssistantReply(reply) {
      chatLog.appendChild(createMessage("assistant", reply.text, reply.events || []));
      chatLog.scrollTop = chatLog.scrollHeight;
    }

    function renderSessionList() {
      sessionList.innerHTML = "";
      if (!state.sessions.length) {
        const empty = document.createElement("p");
        empty.className = "hint";
        empty.textContent = "暂无活动的浏览器会话。";
        sessionList.appendChild(empty);
        return;
      }
      for (const session of state.sessions) {
        const button = document.createElement("button");
        button.type = "button";
        button.className = "session-item" + (session.session_id === state.sessionId ? " active" : "");
        const title = document.createElement("strong");
        title.textContent = session.provider + " · " + session.model;
        const subtitle = document.createElement("span");
        subtitle.textContent = (session.last_message || "新的设计会话") + " · " + session.message_count + " 条消息";
        button.appendChild(title);
        button.appendChild(subtitle);
        button.addEventListener("click", () => loadSession(session.session_id));
        sessionList.appendChild(button);
      }
    }

    async function refreshSessions() {
      try {
        const payload = await api("/api/sessions");
        state.sessions = payload.sessions || [];
        renderSessionList();
      } catch (_err) {
        state.sessions = [];
        renderSessionList();
      }
    }

    async function refreshRagStatus(options = {}) {
      if (!state.config?.rag?.available) {
        renderRagStatus(null);
        return null;
      }
      try {
        const payload = await api("/api/rag/status");
        renderRagStatus(payload.rag || null);
        if (!options.quiet && payload.rag) {
          const ready = payload.rag.cache_ready ? "就绪" : "未就绪";
          setStatus("RAG 索引状态：" + ready + "。");
        }
        return payload.rag || null;
      } catch (error) {
        if (!options.quiet) setStatus(error.message, true);
        renderRagStatus(null);
        return null;
      }
    }

    function pollRagStatusUntilDone() {
      if (state.ragPollTimer) window.clearInterval(state.ragPollTimer);
      state.ragPollTimer = window.setInterval(async () => {
        const status = await refreshRagStatus({ quiet: true });
        const running = Boolean(status?.rebuild?.running);
        if (!running) {
          window.clearInterval(state.ragPollTimer);
          state.ragPollTimer = null;
          if (status?.cache_ready) setStatus("RAG 索引已就绪，后续检索将走快速路径。");
          if (status?.rebuild?.error) setStatus("RAG 索引重建失败：" + status.rebuild.error, true);
        }
      }, 1800);
    }

    async function startRagRebuild(options = {}) {
      if (!state.config?.rag?.available) return null;
      try {
        const payload = await api("/api/rag/rebuild", {
          method: "POST",
          body: JSON.stringify({
            force: options.force ?? true,
            rag_settings: getRagSettings(),
          }),
        });
        renderRagStatus(payload.rag || null);
        pollRagStatusUntilDone();
        if (!options.quiet) setStatus("RAG 索引已开始在后台重建。");
        return payload.rag || null;
      } catch (error) {
        if (!options.quiet) setStatus(error.message, true);
        return null;
      }
    }

    async function createSession(options = {}) {
      setBusy(true, "正在启动...");
      try {
        const payload = await api("/api/sessions", {
          method: "POST",
          body: JSON.stringify({
            provider: providerSelect.value,
            model: WEB_MODEL,
            auto_skill: skillSelect.value || null,
            auto_approve: autoApproveToggle.checked,
            rag_settings: getRagSettings(),
          }),
        });
        updateMeta(payload.session);
        renderMessages(payload.session.messages);
        await refreshSessions();
        setStatus("新设计会话已就绪。");
      } catch (error) {
        setStatus(error.message, true);
      } finally {
        if (!options.keepBusy) setBusy(false);
      }
    }

    async function loadSession(sessionId) {
      const payload = await api("/api/sessions/" + encodeURIComponent(sessionId));
      updateMeta(payload.session);
      renderMessages(payload.session.messages);
      renderSessionList();
    }

    async function resetSession() {
      if (!state.sessionId) return;
      setBusy(true, "正在清空...");
      try {
        const payload = await api("/api/sessions/" + encodeURIComponent(state.sessionId) + "/reset", {
          method: "POST",
          body: JSON.stringify({
            auto_approve: autoApproveToggle.checked,
            auto_skill: skillSelect.value || null,
            rag_settings: getRagSettings(),
          }),
        });
        updateMeta(payload.session);
        renderMessages(payload.session.messages);
        await refreshSessions();
        setStatus("对话已清空。");
      } catch (error) {
        setStatus(error.message, true);
      } finally {
        setBusy(false);
      }
    }

    async function ensureMatchingSession() {
      if (!state.sessionId) {
        await createSession({ keepBusy: true });
        return;
      }
      if (providerSelect.value !== state.provider || WEB_MODEL !== state.model) {
        await createSession({ keepBusy: true });
        return;
      }
      if ((skillSelect.value || "") !== (state.autoSkill || "")) {
        await createSession({ keepBusy: true });
      }
    }

    function parseSseBlock(block) {
      const lines = block.split("\\n");
      let event = "message";
      const dataLines = [];
      for (const line of lines) {
        if (line.startsWith("event:")) event = line.slice(6).trim();
        if (line.startsWith("data:")) dataLines.push(line.slice(5).trimStart());
      }
      if (!dataLines.length) return null;
      try {
        return { event, data: JSON.parse(dataLines.join("\\n")) };
      } catch (_err) {
        return null;
      }
    }

    async function streamApi(path, body, handlers = {}) {
      const response = await fetch(path, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
        signal: state.abortController?.signal,
      });
      if (!response.ok || !response.body) {
        const text = await response.text();
        let payload = {};
        try { payload = text ? JSON.parse(text) : {}; } catch (_err) { payload = { error: text }; }
        throw new Error(payload.error || response.statusText);
      }

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";
      let finalPayload = null;
      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const blocks = buffer.split("\\n\\n");
        buffer = blocks.pop() || "";
        for (const block of blocks) {
          const parsed = parseSseBlock(block);
          if (!parsed) continue;
          if (parsed.event === "chunk") handlers.onChunk?.(parsed.data.text || "");
          if (parsed.event === "tool") handlers.onTool?.(parsed.data);
          if (parsed.event === "error") throw new Error(parsed.data.error || "流式请求失败");
          if (parsed.event === "done") finalPayload = parsed.data;
        }
      }
      if (buffer.trim()) {
        const parsed = parseSseBlock(buffer);
        if (parsed?.event === "done") finalPayload = parsed.data;
      }
      if (!finalPayload) throw new Error("流式响应在完成前中断。");
      return finalPayload;
    }

    async function sendPrompt(event) {
      event.preventDefault();
      const message = promptInput.value.trim();
      if (!message || state.busy) return;

      setBusy(true, "正在思考...");
      setStatus("");
      state.abortController = new AbortController();
      try {
        await ensureMatchingSession();
        if (!state.sessionId) {
          throw new Error("会话尚未就绪。");
        }

        const userMessage = createMessage("user", message);
        chatLog.appendChild(userMessage);
        chatLog.scrollTop = chatLog.scrollHeight;
        promptInput.value = "";
        autosizePrompt();

        let liveAssistant = null;
        let liveText = "";
        const payload = await streamApi(
          "/api/sessions/" + encodeURIComponent(state.sessionId) + "/messages/stream",
          {
            message,
            auto_approve: autoApproveToggle.checked,
            auto_skill: skillSelect.value || null,
            rag_settings: getRagSettings(),
          },
          {
            onChunk: (chunk) => {
              liveText += chunk;
              if (!liveAssistant) {
                liveAssistant = createMessage("assistant", "");
                chatLog.appendChild(liveAssistant);
              }
              const bubble = liveAssistant.querySelector(".bubble");
              if (bubble) renderMarkdownInto(bubble, liveText);
              chatLog.scrollTop = chatLog.scrollHeight;
            },
            onTool: (toolEvent) => {
              if (toolEvent.rag) renderRagResults(toolEvent.rag);
              if (toolEvent.summary) setStatus(toolEvent.summary);
            },
          },
        );
        if (liveAssistant) liveAssistant.remove();

        updateMeta(payload.session);
        appendAssistantReply(payload.reply);
        await refreshSessions();
        const usage = payload.reply.usage || {};
        const tokenBits = [];
        if (usage.input_tokens) tokenBits.push("输入 " + usage.input_tokens);
        if (usage.output_tokens) tokenBits.push("输出 " + usage.output_tokens);
        setStatus(tokenBits.length ? "本轮完成：" + tokenBits.join(" / ") : "本轮完成。");
      } catch (error) {
        const messageText = error.name === "AbortError" ? "已在本地停止请求；服务器可能仍会完成已开始的回合。" : error.message;
        chatLog.appendChild(createMessage("system", messageText));
        chatLog.scrollTop = chatLog.scrollHeight;
        setStatus(messageText, true);
      } finally {
        state.abortController = null;
        setBusy(false);
      }
    }

    async function runRagSearch() {
      const query = promptInput.value.trim();
      if (!query) {
        setStatus("请先在输入框中输入检索问题。", true);
        promptInput.focus();
        return;
      }
      setBusy(true, "正在检索...");
      setStatus("");
      try {
        if (getRagSettings().use_cache) {
          const status = await refreshRagStatus({ quiet: true });
          if (status && !status.cache_ready) {
            await startRagRebuild({ quiet: true, force: false });
            setStatus("RAG 索引尚未就绪，已开始后台重建；索引就绪后请重试检索。", true);
            return;
          }
        }
        const payload = await api("/api/rag/search", {
          method: "POST",
          body: JSON.stringify({
            query,
            rag_settings: getRagSettings(),
          }),
        });
        renderRagResults(payload.rag);
        const hits = Array.isArray(payload.rag?.hits) ? payload.rag.hits.length : 0;
        setStatus("RAG 检索完成：" + hits + " 条命中。");
        await refreshRagStatus({ quiet: true });
      } catch (error) {
        renderRagResults(null);
        setStatus(error.message, true);
      } finally {
        setBusy(false);
      }
    }

    providerSelect.addEventListener("change", () => {
      const provider = providerByName(providerSelect.value);
      if (provider) {
        modelInput.value = WEB_MODEL;
      }
      updateModelSuggestions();
      saveLocalState();
    });

    skillSelect.addEventListener("change", () => {
      updateSkillStatus();
      saveLocalState();
    });
    modelInput.addEventListener("change", saveLocalState);
    autoApproveToggle.addEventListener("change", saveLocalState);
    ragAutoRetrieveToggle.addEventListener("change", saveLocalState);
    ragTopKInput.addEventListener("change", saveLocalState);
    ragSnippetInput.addEventListener("change", saveLocalState);
    ragCandidateInput.addEventListener("change", saveLocalState);
    ragCacheToggle.addEventListener("change", saveLocalState);

    newSessionBtn.addEventListener("click", createSession);
    resetSessionBtn.addEventListener("click", resetSession);
    ragSearchBtn.addEventListener("click", runRagSearch);
    ragRebuildBtn.addEventListener("click", async () => {
      setBusy(true, "正在启动索引...");
      try {
        await startRagRebuild({ force: true });
      } finally {
        setBusy(false);
      }
    });
    ragRefreshBtn.addEventListener("click", () => refreshRagStatus());
    stopBtn.addEventListener("click", () => {
      state.abortController?.abort();
      setStatus("正在停止本地请求...", true);
    });
    clearDraftBtn.addEventListener("click", () => {
      promptInput.value = "";
      autosizePrompt();
      promptInput.focus();
    });
    document.querySelectorAll(".prompt-chip").forEach((button) => {
      button.addEventListener("click", () => setPromptDraft(button.dataset.prompt || button.textContent || ""));
    });
    promptInput.addEventListener("input", autosizePrompt);
    promptInput.addEventListener("keydown", (event) => {
      if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        document.getElementById("composerForm").requestSubmit();
      }
    });
    document.getElementById("composerForm").addEventListener("submit", sendPrompt);

    async function init() {
      setBusy(true, "正在加载...");
      try {
        state.config = await api("/api/config");
        workspaceRoot.textContent = state.config.workspace_root;
        populateProviders();
        populateSkills();
        const local = loadLocalState();
        applyConfigDefaults(local);
        await refreshRagStatus({ quiet: true });
        if (local?.sessionId) {
          try {
            await loadSession(local.sessionId);
            await refreshSessions();
            setStatus("已恢复上次会话。");
          } catch (_err) {
            await createSession();
          }
        } else {
          await createSession();
        }
      } catch (error) {
        setStatus(error.message, true);
      } finally {
        setBusy(false);
      }
    }

    init();
  </script>
</body>
</html>
"""


@dataclass
class WebRagSettings:
    """Browser-controlled retrieval settings for the local RAG skill."""

    top_k: int = 5
    max_snippet_chars: int = 280
    use_cache: bool = True
    auto_retrieve: bool = True
    candidate_limit: int = 1200

    def to_dict(self) -> dict[str, Any]:
        return {
            "top_k": self.top_k,
            "max_snippet_chars": self.max_snippet_chars,
            "use_cache": self.use_cache,
            "auto_retrieve": self.auto_retrieve,
            "candidate_limit": self.candidate_limit,
        }


@dataclass
class WebSessionState:
    """State tracked for a browser-backed conversation."""

    session: Session
    provider_name: str
    provider: Any
    tool_registry: ToolRegistry
    tool_context: ToolContext
    auto_approve: bool = True
    auto_skill: str | None = None
    rag_settings: WebRagSettings = field(default_factory=WebRagSettings)
    lock: threading.RLock = field(default_factory=threading.RLock)


class ClawdWebService:
    """Owns browser sessions and the local agent runtime."""

    def __init__(self, workspace_root: Path | None = None) -> None:
        self.workspace_root = Path(workspace_root or Path.cwd()).resolve()
        self._sessions: dict[str, WebSessionState] = {}
        self._rag_services: dict[str, RagIndexService] = {}
        self._lock = threading.RLock()

    def get_bootstrap_payload(self) -> dict[str, Any]:
        """Return config data needed by the browser shell."""
        config = load_config()
        configured = config.get("providers", {})
        providers: list[dict[str, Any]] = []
        for name, info in PROVIDER_INFO.items():
            provider_config = configured.get(name, {})
            default_model = "deepseek-v4-pro" if name == "openai" else provider_config.get("default_model", info["default_model"])
            providers.append(
                {
                    "name": name,
                    "label": info["label"],
                    "configured": bool(provider_config.get("api_key")),
                    "base_url": provider_config.get("base_url", info["default_base_url"]),
                    "default_model": default_model,
                    "available_models": info["available_models"],
                }
            )
        return {
            "workspace_root": str(self.workspace_root),
            "default_provider": "openai" if configured.get("openai", {}).get("api_key") else config.get("default_provider", "anthropic"),
            "providers": providers,
            "skills": self._list_project_skills(),
            "default_auto_skill": None,
            "rag": self._rag_bootstrap_payload(),
        }

    def create_session(
        self,
        *,
        provider_name: str | None = None,
        model: str | None = None,
        auto_approve: bool = True,
        auto_skill: str | None = None,
        rag_settings: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Create a new in-memory browser session."""
        config = load_config()
        provider_name = provider_name or ("openai" if config.get("providers", {}).get("openai", {}).get("api_key") else config.get("default_provider", "anthropic"))
        self._ensure_known_provider(provider_name)
        provider_config = get_provider_config(provider_name)
        if not provider_config.get("api_key"):
            raise ValueError(
                f"{provider_name} API Key 未配置。请先运行 `clawd login` 并完成配置。"
            )

        provider_class = get_provider_class(provider_name)
        resolved_model = "deepseek-v4-pro" if provider_name == "openai" else (model or "").strip() or provider_config.get("default_model")
        provider = provider_class(
            api_key=provider_config["api_key"],
            base_url=provider_config.get("base_url"),
            model=resolved_model,
        )

        resolved_skill = self._normalize_skill_name(auto_skill)
        resolved_rag_settings = self._normalize_rag_settings(rag_settings)

        tool_context = ToolContext(workspace_root=self.workspace_root, cwd=self.workspace_root)
        session = Session.create(provider_name, provider.model or resolved_model or "")
        session.session_id = f"{session.session_id}_{uuid4().hex[:6]}"
        session.model = provider.model or resolved_model or session.model
        state = WebSessionState(
            session=session,
            provider_name=provider_name,
            provider=provider,
            tool_registry=build_default_registry(enable_ask_user_question=False),
            tool_context=tool_context,
            auto_approve=auto_approve,
            auto_skill=resolved_skill,
            rag_settings=resolved_rag_settings,
        )

        with self._lock:
            self._sessions[session.session_id] = state
        return {"session": self._serialize_session(state)}

    def get_session_payload(self, session_id: str) -> dict[str, Any]:
        """Load a current browser session payload."""
        state = self._require_session(session_id)
        with state.lock:
            return {"session": self._serialize_session(state)}

    def list_sessions_payload(self) -> dict[str, Any]:
        """Return active in-memory browser sessions for the sidebar."""
        with self._lock:
            states = list(self._sessions.values())
        sessions = []
        for state in states:
            with state.lock:
                sessions.append(self._serialize_session_summary(state))
        sessions.sort(key=lambda item: item.get("updated_at") or "", reverse=True)
        return {"sessions": sessions}

    def reset_session(
        self,
        session_id: str,
        *,
        auto_approve: bool | None = None,
        auto_skill: str | None = None,
        rag_settings: dict[str, Any] | None = None,
        stream: bool = False,
        on_text_chunk: Any | None = None,
        on_tool_event: Any | None = None,
    ) -> dict[str, Any]:
        """Clear the conversation while keeping provider/model choices."""
        state = self._require_session(session_id)
        with state.lock:
            if auto_approve is not None:
                state.auto_approve = auto_approve
            if auto_skill is not None:
                state.auto_skill = self._normalize_skill_name(auto_skill)
            if rag_settings is not None:
                state.rag_settings = self._normalize_rag_settings(rag_settings, base=state.rag_settings)
            state.session.conversation.clear()
            state.tool_context.read_file_fingerprints.clear()
            state.tool_context.outbox.clear()
            state.tool_context.todos.clear()
            state.tool_context.tasks.clear()
            state.session.save()
            return {"session": self._serialize_session(state)}

    def send_message(
        self,
        session_id: str,
        message: str,
        *,
        max_turns: int = 20,
        auto_approve: bool | None = None,
        auto_skill: str | None = None,
        rag_settings: dict[str, Any] | None = None,
        stream: bool = False,
        on_text_chunk: Any | None = None,
        on_tool_event: Any | None = None,
    ) -> dict[str, Any]:
        """Run one agent turn for a browser session."""
        cleaned = message.strip()
        if not cleaned:
            raise ValueError("message must not be empty")

        state = self._require_session(session_id)
        with state.lock:
            if auto_approve is not None:
                state.auto_approve = auto_approve
            if auto_skill is not None:
                state.auto_skill = self._normalize_skill_name(auto_skill)
            if rag_settings is not None:
                state.rag_settings = self._normalize_rag_settings(rag_settings, base=state.rag_settings)

            events: list[dict[str, Any]] = []
            state.tool_context.outbox.clear()
            state.tool_context.ask_user = None
            state.tool_context.permission_handler = self._build_permission_handler(state, events)
            attached_rag = self._maybe_attach_rag_evidence(cleaned, state, events, on_tool_event)
            state.session.conversation.add_user_message(
                self._build_user_message(cleaned, state.auto_skill, attached_rag)
            )

            def record_tool_event(event: ToolEvent) -> None:
                serialized = self._serialize_tool_event(event)
                events.append(serialized)
                if on_tool_event is not None:
                    try:
                        on_tool_event(serialized)
                    except Exception:
                        return

            result = run_agent_loop(
                conversation=state.session.conversation,
                provider=state.provider,
                tool_registry=state.tool_registry,
                tool_context=state.tool_context,
                max_turns=max_turns,
                stream=stream,
                verbose=False,
                on_event=record_tool_event,
                on_text_chunk=on_text_chunk,
            )
            state.session.model = state.provider.model or state.session.model
            state.session.save()

            return {
                "reply": {
                    "text": result.response_text,
                    "usage": result.usage,
                    "num_turns": result.num_turns,
                    "events": events,
                    "outbox": list(state.tool_context.outbox),
                },
                "session": self._serialize_session(state),
            }

    def search_rag(
        self,
        query: str,
        *,
        rag_settings: dict[str, Any] | WebRagSettings | None = None,
    ) -> dict[str, Any]:
        """Run the project RAG retriever directly for preview or browser preflight."""
        cleaned = query.strip()
        if not cleaned:
            raise ValueError("query must not be empty")
        settings = self._normalize_rag_settings(rag_settings)
        rag_payload = self._run_aircraft_rag_search(cleaned, settings)
        return {"rag": rag_payload, "settings": settings.to_dict()}

    def rag_status(self) -> dict[str, Any]:
        """Return readiness information for the local RAG SQLite index."""
        service = self._get_aircraft_rag_service()
        return {"rag": service.status(WebRagSettings())}

    def rebuild_rag(
        self,
        *,
        rag_settings: dict[str, Any] | WebRagSettings | None = None,
        force: bool = True,
    ) -> dict[str, Any]:
        """Start a background rebuild of the local RAG SQLite index."""
        settings = self._normalize_rag_settings(rag_settings)
        service = self._get_aircraft_rag_service()
        return {"rag": service.rebuild(settings, force=force), "settings": settings.to_dict()}

    def _maybe_attach_rag_evidence(
        self,
        query: str,
        state: WebSessionState,
        events: list[dict[str, Any]],
        on_tool_event: Any | None = None,
    ) -> dict[str, Any] | None:
        if state.auto_skill != "aircraft-design-rag" or not state.rag_settings.auto_retrieve:
            return None
        try:
            service = self._get_aircraft_rag_service()
            if state.rag_settings.use_cache and not service.cache_ready(state.rag_settings):
                service.rebuild(state.rag_settings, force=False)
                payload = service.not_ready_payload(query, state.rag_settings)
            else:
                payload = service.search(query, state.rag_settings)
        except Exception as exc:
            event = {
                    "kind": "rag_retrieval",
                    "tool_name": state.auto_skill,
                    "summary": f"RAG 检索失败：{exc}",
                    "preview": {"query": query, "settings": state.rag_settings.to_dict()},
                    "error": str(exc),
                    "is_error": True,
                }
            events.append(event)
            if on_tool_event is not None:
                try:
                    on_tool_event(event)
                except Exception:
                    pass
            return None

        hits = payload.get("hits")
        hit_count = len(hits) if isinstance(hits, list) else 0
        event = {
                "kind": "rag_retrieval",
                "tool_name": state.auto_skill,
                "summary": f"已附加 RAG 证据 · 命中={hit_count}",
                "preview": payload,
                "rag": payload,
                "error": None,
                "is_error": False,
            }
        events.append(event)
        if on_tool_event is not None:
            try:
                on_tool_event(event)
            except Exception:
                pass
        return payload

    def _run_aircraft_rag_search(self, query: str, settings: WebRagSettings) -> dict[str, Any]:
        return self._get_aircraft_rag_service().search(query, settings)

    def _get_aircraft_rag_service(self) -> RagIndexService:
        skill = self._get_project_skill("aircraft-design-rag")
        if skill is None or not skill.skill_root:
            raise ValueError("aircraft-design-rag skill is not available in this workspace")

        script_path = Path(skill.skill_root) / "scripts" / "search_rag.py"
        if not script_path.exists():
            raise ValueError(f"RAG search script not found: {script_path}")
        service_key = str(script_path.resolve())
        with self._lock:
            service = self._rag_services.get(service_key)
            if service is None:
                service = RagIndexService(self.workspace_root, script_path)
                self._rag_services[service_key] = service
        return service

    def _build_permission_handler(
        self,
        state: WebSessionState,
        events: list[dict[str, Any]],
    ):
        def handler(tool_name: str, message: str, suggestion: str | None) -> tuple[bool, bool]:
            events.append(
                {
                    "kind": "permission",
                    "tool_name": tool_name,
                    "message": message,
                    "summary": suggestion or message,
                    "preview": {
                        "autoApproved": state.auto_approve,
                        "message": message,
                        "suggestion": suggestion,
                    },
                }
            )
            return state.auto_approve, True

        return handler

    def _serialize_session(self, state: WebSessionState) -> dict[str, Any]:
        return {
            "session_id": state.session.session_id,
            "provider": state.provider_name,
            "model": state.provider.model or state.session.model,
            "auto_approve": state.auto_approve,
            "auto_skill": state.auto_skill,
            "rag_settings": state.rag_settings.to_dict(),
            "messages": self._serialize_messages(state.session),
            "created_at": state.session.created_at,
            "updated_at": state.session.updated_at,
        }

    def _serialize_session_summary(self, state: WebSessionState) -> dict[str, Any]:
        messages = self._serialize_messages(state.session)
        last_message = ""
        for message in reversed(messages):
            text = (message.get("text") or "").strip()
            if text:
                last_message = text if len(text) <= 90 else text[:87] + "..."
                break
        return {
            "session_id": state.session.session_id,
            "provider": state.provider_name,
            "model": state.provider.model or state.session.model,
            "auto_skill": state.auto_skill,
            "message_count": len(messages),
            "last_message": last_message,
            "created_at": state.session.created_at,
            "updated_at": state.session.updated_at,
        }

    def _normalize_rag_settings(
        self,
        value: dict[str, Any] | WebRagSettings | None,
        *,
        base: WebRagSettings | None = None,
    ) -> WebRagSettings:
        if isinstance(value, WebRagSettings):
            return value
        settings = base or WebRagSettings()
        if value is None:
            return WebRagSettings(**settings.to_dict())
        if not isinstance(value, dict):
            raise ValueError("rag_settings 必须是对象")

        top_k = self._bounded_int(value.get("top_k", settings.top_k), "rag_settings.top_k", 1, 20)
        max_snippet_chars = self._bounded_int(
            value.get("max_snippet_chars", settings.max_snippet_chars),
            "rag_settings.max_snippet_chars",
            80,
            3000,
        )
        use_cache = self._bool_setting(value.get("use_cache", settings.use_cache), "rag_settings.use_cache")
        auto_retrieve = self._bool_setting(
            value.get("auto_retrieve", settings.auto_retrieve),
            "rag_settings.auto_retrieve",
        )
        candidate_limit = self._bounded_int(
            value.get("candidate_limit", settings.candidate_limit),
            "rag_settings.candidate_limit",
            50,
            10000,
        )
        return WebRagSettings(
            top_k=top_k,
            max_snippet_chars=max_snippet_chars,
            use_cache=use_cache,
            auto_retrieve=auto_retrieve,
            candidate_limit=candidate_limit,
        )

    def _bounded_int(self, value: Any, name: str, minimum: int, maximum: int) -> int:
        if isinstance(value, bool):
            raise ValueError(f"{name} 必须是整数")
        try:
            parsed = int(value)
        except (TypeError, ValueError) as exc:
            raise ValueError(f"{name} 必须是整数") from exc
        if parsed < minimum or parsed > maximum:
            raise ValueError(f"{name} 必须在 {minimum} 到 {maximum} 之间")
        return parsed

    def _bool_setting(self, value: Any, name: str) -> bool:
        if not isinstance(value, bool):
            raise ValueError(f"{name} 必须是布尔值")
        return value

    def _rag_bootstrap_payload(self) -> dict[str, Any]:
        skill = self._get_project_skill("aircraft-design-rag")
        script_path = Path(skill.skill_root) / "scripts" / "search_rag.py" if skill and skill.skill_root else None
        return {
            "available": bool(skill and script_path and script_path.exists()),
            "skill_name": "aircraft-design-rag",
            "data_dir": str(self.workspace_root / "RAG-data"),
            "defaults": WebRagSettings().to_dict(),
        }

    def _list_project_skills(self) -> list[dict[str, Any]]:
        try:
            from src.skills.loader import get_all_skills

            skills = get_all_skills(project_root=self.workspace_root)
        except Exception:
            return []

        listed: list[dict[str, Any]] = []
        for skill in skills:
            listed.append(
                {
                    "name": skill.name,
                    "description": skill.description,
                    "when_to_use": skill.when_to_use,
                    "allowed_tools": list(skill.allowed_tools) if skill.allowed_tools else [],
                    "loaded_from": skill.loaded_from,
                }
            )
        return sorted(listed, key=lambda item: item["name"])

    def _get_project_skill(self, name: str):
        try:
            from src.skills.loader import get_all_skills

            skills = get_all_skills(project_root=self.workspace_root)
        except Exception:
            return None
        return next((skill for skill in skills if skill.name == name), None)

    def _default_auto_skill(self) -> str | None:
        return None

    def _normalize_skill_name(self, skill_name: str | None) -> str | None:
        if skill_name is None:
            return None
        normalized = skill_name.strip().removeprefix("/")
        if not normalized:
            return None
        names = {skill["name"] for skill in self._list_project_skills()}
        if normalized not in names:
            raise ValueError(f"未知技能：{normalized}")
        return normalized

    def _build_user_message(
        self,
        message: str,
        auto_skill: str | None,
        attached_rag: dict[str, Any] | None = None,
    ) -> str:
        if not auto_skill:
            return message
        parts = [AUTO_SKILL_SYSTEM_TEMPLATE.format(skill_name=auto_skill)]
        if attached_rag is not None:
            parts.append(
                "Browser-attached RAG evidence for this turn:\n"
                "```json\n"
                f"{json.dumps(attached_rag, ensure_ascii=False, indent=2)}\n"
                "```"
            )
        parts.append(f"User request:\n{message}")
        return "\n\n".join(parts)

    def _serialize_messages(self, session: Session) -> list[dict[str, Any]]:
        serialized: list[dict[str, Any]] = []
        for message in session.conversation.messages:
            text_parts: list[str] = []
            blocks: list[dict[str, Any]] = []
            if isinstance(message.content, str):
                text_parts.append(message.content)
            else:
                for block in message.content:
                    block_type = getattr(block, "type", "")
                    if block_type == "text":
                        text = getattr(block, "text", "")
                        if isinstance(text, str) and text:
                            text_parts.append(text)
                    elif block_type == "tool_use":
                        name = getattr(block, "name", "Tool")
                        blocks.append({"type": "tool_use", "label": f"Tool call: {name}"})
                    elif block_type == "tool_result":
                        blocks.append({"type": "tool_result", "label": "Tool result"})

            # Keep browser history focused on human-visible turns.
            if message.role == "user" and blocks and not text_parts:
                continue

            text = "".join(text_parts).strip()
            if message.role == "user" and "User request:\n" in text:
                text = text.rsplit("User request:\n", 1)[-1].strip()
            if not text and not blocks:
                continue

            serialized.append(
                {
                    "role": message.role,
                    "text": text,
                    "blocks": blocks,
                    "timestamp": message.timestamp,
                }
            )
        return serialized

    def _serialize_tool_event(self, event: ToolEvent) -> dict[str, Any]:
        preview: Any = None
        summary = ""
        if event.kind == "tool_use":
            summary = summarize_tool_use(event.tool_name, event.tool_input or {})
            preview = event.tool_input
        elif event.kind == "tool_result":
            summary = summarize_tool_result(event.tool_name, event.tool_output)
            preview = self._trim_preview(event.tool_output)
        else:
            summary = event.error or ""
            preview = event.tool_input

        serialized = {
            "kind": event.kind,
            "tool_name": event.tool_name,
            "tool_use_id": event.tool_use_id,
            "summary": summary,
            "preview": preview,
            "error": event.error,
            "is_error": event.is_error,
        }
        rag_payload = self._extract_rag_payload_from_tool_output(event.tool_output)
        if rag_payload is not None:
            serialized["rag"] = rag_payload
        return serialized

    def _extract_rag_payload_from_tool_output(self, output: Any) -> dict[str, Any] | None:
        if not isinstance(output, dict):
            return None
        command_output = output.get("retrievedCommandOutput")
        if not isinstance(command_output, str):
            return None
        json_text = self._extract_stdout_json(command_output)
        if not json_text:
            return None
        try:
            payload = json.loads(json_text)
        except json.JSONDecodeError:
            return None
        return payload if isinstance(payload, dict) and isinstance(payload.get("hits"), list) else None

    def _extract_stdout_json(self, command_output: str) -> str | None:
        marker = "STDOUT:"
        start = command_output.find(marker)
        if start >= 0:
            candidate = command_output[start + len(marker):].strip()
            stderr_start = candidate.find("\n\nSTDERR:")
            if stderr_start >= 0:
                candidate = candidate[:stderr_start].strip()
            if candidate:
                return candidate
        first = command_output.find("{")
        last = command_output.rfind("}")
        if first >= 0 and last > first:
            return command_output[first : last + 1]
        return None

    def _trim_preview(self, value: Any, *, limit: int = 1200) -> Any:
        if isinstance(value, str):
            return value if len(value) <= limit else value[:limit] + "..."
        try:
            rendered = json.dumps(value, ensure_ascii=False, indent=2)
        except Exception:
            rendered = str(value)
        if len(rendered) <= limit:
            return value
        return rendered[:limit] + "..."

    def _ensure_known_provider(self, provider_name: str) -> None:
        if provider_name not in PROVIDER_INFO:
            raise ValueError(f"Unknown provider: {provider_name}")

    def _require_session(self, session_id: str) -> WebSessionState:
        with self._lock:
            state = self._sessions.get(session_id)
        if state is None:
            raise KeyError(f"Unknown session: {session_id}")
        return state


class _ClawdHTTPServer(ThreadingHTTPServer):
    """HTTP server carrying the app service instance."""

    daemon_threads = True
    allow_reuse_address = True

    def __init__(self, server_address: tuple[str, int], service: ClawdWebService):
        self.service = service
        super().__init__(server_address, ClawdWebRequestHandler)


class ClawdWebRequestHandler(BaseHTTPRequestHandler):
    """Simple local JSON API and static page handler."""

    server: _ClawdHTTPServer
    protocol_version = "HTTP/1.1"

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        if parsed.path in {"/", "/index.html"}:
            self._send_bytes(HTTPStatus.OK, INDEX_HTML.encode("utf-8"), "text/html; charset=utf-8")
            return
        if parsed.path == "/api/config":
            self._send_json(HTTPStatus.OK, self.server.service.get_bootstrap_payload())
            return
        if parsed.path == "/api/rag/status":
            try:
                self._send_json(HTTPStatus.OK, self.server.service.rag_status())
            except ValueError as exc:
                self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
            return
        if parsed.path == "/api/sessions":
            self._send_json(HTTPStatus.OK, self.server.service.list_sessions_payload())
            return
        if parsed.path.startswith("/api/sessions/"):
            session_id = parsed.path.removeprefix("/api/sessions/")
            if not session_id or "/" in session_id:
                self._send_error_json(HTTPStatus.NOT_FOUND, "未知路由")
                return
            try:
                payload = self.server.service.get_session_payload(session_id)
            except KeyError as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            self._send_json(HTTPStatus.OK, payload)
            return
        self._send_error_json(HTTPStatus.NOT_FOUND, "未知路由")

    def do_POST(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        try:
            payload = self._read_json_body()
        except ValueError as exc:
            self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
            return

        if parsed.path == "/api/sessions":
            try:
                result = self.server.service.create_session(
                    provider_name=self._optional_string(payload, "provider"),
                    model=self._optional_string(payload, "model"),
                    auto_approve=self._optional_bool(payload, "auto_approve", True),
                    auto_skill=self._optional_string(payload, "auto_skill"),
                    rag_settings=self._optional_object(payload, "rag_settings"),
                )
            except ValueError as exc:
                self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
                return
            self._send_json(HTTPStatus.CREATED, result)
            return

        if parsed.path.startswith("/api/sessions/") and parsed.path.endswith("/messages/stream"):
            session_id = parsed.path.removeprefix("/api/sessions/").removesuffix("/messages/stream").rstrip("/")
            message = self._optional_string(payload, "message")
            if message is None:
                self._send_error_json(HTTPStatus.BAD_REQUEST, "message 为必填项")
                return
            self._send_sse_headers()

            def emit(event: str, data: dict[str, Any]) -> None:
                self._write_sse(event, data)

            try:
                result = self.server.service.send_message(
                    session_id,
                    message,
                    auto_approve=self._optional_bool(payload, "auto_approve", None),
                    auto_skill=self._optional_string(payload, "auto_skill"),
                    rag_settings=self._optional_object(payload, "rag_settings"),
                    stream=True,
                    on_text_chunk=lambda chunk: emit("chunk", {"text": chunk}),
                    on_tool_event=lambda event: emit("tool", event),
                )
            except Exception as exc:
                emit("error", {"error": str(exc)})
                return
            emit("done", result)
            return

        if parsed.path.startswith("/api/sessions/") and parsed.path.endswith("/reset"):
            session_id = parsed.path.removeprefix("/api/sessions/").removesuffix("/reset").rstrip("/")
            try:
                result = self.server.service.reset_session(
                    session_id,
                    auto_approve=self._optional_bool(payload, "auto_approve", None),
                    auto_skill=self._optional_string(payload, "auto_skill"),
                    rag_settings=self._optional_object(payload, "rag_settings"),
                )
            except KeyError as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            self._send_json(HTTPStatus.OK, result)
            return

        if parsed.path.startswith("/api/sessions/") and parsed.path.endswith("/messages"):
            session_id = parsed.path.removeprefix("/api/sessions/").removesuffix("/messages").rstrip("/")
            message = self._optional_string(payload, "message")
            if message is None:
                self._send_error_json(HTTPStatus.BAD_REQUEST, "message 为必填项")
                return
            try:
                result = self.server.service.send_message(
                    session_id,
                    message,
                    auto_approve=self._optional_bool(payload, "auto_approve", None),
                    auto_skill=self._optional_string(payload, "auto_skill"),
                    rag_settings=self._optional_object(payload, "rag_settings"),
                )
            except KeyError as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            except ValueError as exc:
                self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
                return
            except Exception as exc:  # pragma: no cover - defensive path
                self._send_error_json(HTTPStatus.INTERNAL_SERVER_ERROR, str(exc))
                return
            self._send_json(HTTPStatus.OK, result)
            return

        if parsed.path == "/api/rag/search":
            query = self._optional_string(payload, "query")
            if query is None:
                self._send_error_json(HTTPStatus.BAD_REQUEST, "query 为必填项")
                return
            try:
                result = self.server.service.search_rag(
                    query,
                    rag_settings=self._optional_object(payload, "rag_settings"),
                )
            except ValueError as exc:
                self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
                return
            self._send_json(HTTPStatus.OK, result)
            return

        if parsed.path == "/api/rag/rebuild":
            try:
                result = self.server.service.rebuild_rag(
                    rag_settings=self._optional_object(payload, "rag_settings"),
                    force=self._optional_bool(payload, "force", True),
                )
            except ValueError as exc:
                self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
                return
            self._send_json(HTTPStatus.ACCEPTED, result)
            return

        self._send_error_json(HTTPStatus.NOT_FOUND, "未知路由")

    def log_message(self, format: str, *args: Any) -> None:
        """Keep the server quiet unless needed for debugging."""
        return

    def _read_json_body(self) -> dict[str, Any]:
        length = int(self.headers.get("Content-Length", "0") or "0")
        if length <= 0:
            return {}
        raw = self.rfile.read(length)
        try:
            data = json.loads(raw.decode("utf-8"))
        except json.JSONDecodeError as exc:
            raise ValueError(f"JSON 请求体无效：{exc.msg}") from exc
        if not isinstance(data, dict):
            raise ValueError("JSON 请求体必须是对象")
        return data

    def _optional_string(self, payload: dict[str, Any], key: str) -> str | None:
        value = payload.get(key)
        if value is None:
            return None
        if not isinstance(value, str):
            raise ValueError(f"{key} 必须是字符串")
        return value

    def _optional_bool(self, payload: dict[str, Any], key: str, default: bool | None) -> bool | None:
        value = payload.get(key, default)
        if value is None:
            return None
        if not isinstance(value, bool):
            raise ValueError(f"{key} 必须是布尔值")
        return value

    def _optional_object(self, payload: dict[str, Any], key: str) -> dict[str, Any] | None:
        value = payload.get(key)
        if value is None:
            return None
        if not isinstance(value, dict):
            raise ValueError(f"{key} 必须是对象")
        return value

    def _send_json(self, status: HTTPStatus, payload: dict[str, Any]) -> None:
        self._send_bytes(status, json.dumps(payload, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

    def _send_error_json(self, status: HTTPStatus, message: str) -> None:
        self._send_json(status, {"error": message})

    def _send_sse_headers(self) -> None:
        self.send_response(HTTPStatus.OK.value)
        self.send_header("Content-Type", "text/event-stream; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Connection", "keep-alive")
        self.end_headers()

    def _write_sse(self, event: str, payload: dict[str, Any]) -> None:
        try:
            data = json.dumps(payload, ensure_ascii=False)
            self.wfile.write(f"event: {event}\ndata: {data}\n\n".encode("utf-8"))
            self.wfile.flush()
        except (BrokenPipeError, ConnectionResetError):
            raise

    def _send_bytes(self, status: HTTPStatus, payload: bytes, content_type: str) -> None:
        self.send_response(status.value)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(payload)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(payload)


def run_web_server(host: str = "127.0.0.1", port: int = 8080, workspace_root: Path | None = None) -> None:
    """Start the local browser UI server."""
    service = ClawdWebService(workspace_root=workspace_root)
    server = _ClawdHTTPServer((host, port), service)
    url = f"http://{host}:{port}"
    print(f"飞行器设计网页端已启动：{url}")
    print(f"工作区：{service.workspace_root}")
    print("按 Ctrl+C 停止服务器。")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n正在停止飞行器设计网页端...")
    finally:
        server.server_close()
