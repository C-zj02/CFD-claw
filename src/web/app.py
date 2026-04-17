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


INDEX_HTML = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Clawd Web Console</title>
  <style>
    :root {
      --bg: #f3ede3;
      --bg-accent: #d8e5d0;
      --panel: rgba(255, 251, 245, 0.92);
      --panel-strong: #fffdf8;
      --ink: #1d2a24;
      --muted: #5b6b63;
      --line: rgba(39, 58, 49, 0.12);
      --primary: #1f6d55;
      --primary-strong: #124c3b;
      --warm: #d9895b;
      --user: #193b52;
      --tool-bg: #eef5f1;
      --danger: #a53c30;
      --shadow: 0 20px 60px rgba(32, 47, 40, 0.12);
      --radius-xl: 26px;
      --radius-lg: 18px;
      --radius-md: 14px;
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
      padding: 24px;
    }

    .shell {
      display: grid;
      grid-template-columns: 340px minmax(0, 1fr);
      gap: 20px;
      height: calc(100vh - 48px);
    }

    .panel {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: var(--radius-xl);
      box-shadow: var(--shadow);
      backdrop-filter: blur(12px);
    }

    .sidebar {
      padding: 22px;
      display: flex;
      flex-direction: column;
      gap: 18px;
      overflow: auto;
    }

    .brand {
      padding: 18px;
      border-radius: var(--radius-lg);
      background:
        linear-gradient(145deg, rgba(255,255,255,0.92), rgba(245, 238, 228, 0.95)),
        linear-gradient(145deg, rgba(31, 109, 85, 0.12), rgba(217, 137, 91, 0.14));
      border: 1px solid rgba(31, 109, 85, 0.12);
    }

    .eyebrow {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 10px;
      border-radius: 999px;
      background: rgba(31, 109, 85, 0.1);
      color: var(--primary-strong);
      font-size: 12px;
      letter-spacing: 0.08em;
      text-transform: uppercase;
    }

    .brand h1 {
      margin: 14px 0 8px;
      font-family: "Iowan Old Style", "Palatino Linotype", serif;
      font-size: 34px;
      line-height: 1;
      letter-spacing: -0.03em;
    }

    .brand p {
      margin: 0;
      color: var(--muted);
      line-height: 1.5;
    }

    .workspace {
      margin-top: 14px;
      padding: 12px;
      background: rgba(31, 109, 85, 0.07);
      border-radius: var(--radius-md);
      font-size: 13px;
      color: var(--primary-strong);
      word-break: break-word;
    }

    .card {
      padding: 16px;
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

    label {
      font-size: 13px;
      font-weight: 700;
      color: var(--primary-strong);
    }

    input[type="text"],
    select,
    textarea {
      width: 100%;
      border: 1px solid rgba(29, 42, 36, 0.14);
      border-radius: 14px;
      background: #fffdf9;
      color: var(--ink);
      font: inherit;
      padding: 12px 14px;
      transition: border-color 140ms ease, box-shadow 140ms ease, transform 140ms ease;
    }

    textarea {
      min-height: 92px;
      resize: vertical;
      line-height: 1.45;
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
      padding: 12px 14px;
      border-radius: 14px;
      background: rgba(31, 109, 85, 0.07);
      color: var(--primary-strong);
      font-size: 14px;
    }

    .toggle input {
      accent-color: var(--primary);
      width: 18px;
      height: 18px;
    }

    .actions {
      display: flex;
      gap: 10px;
      flex-wrap: wrap;
    }

    button {
      border: 0;
      border-radius: 999px;
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
      box-shadow: 0 16px 24px rgba(18, 76, 59, 0.18);
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
      padding: 18px 22px;
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
      gap: 10px;
      color: var(--muted);
      font-size: 13px;
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
    }

    .chat {
      padding: 24px;
      overflow: auto;
      display: flex;
      flex-direction: column;
      gap: 16px;
    }

    .hero {
      padding: 22px;
      border: 1px dashed rgba(29, 42, 36, 0.18);
      border-radius: 20px;
      background: linear-gradient(145deg, rgba(255,255,255,0.72), rgba(223, 236, 228, 0.82));
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
      border-radius: 22px;
      padding: 16px 18px;
      box-shadow: 0 10px 22px rgba(22, 34, 28, 0.08);
      border: 1px solid rgba(20, 40, 32, 0.08);
      white-space: pre-wrap;
      line-height: 1.55;
      word-break: break-word;
    }

    .message.user .bubble {
      background: linear-gradient(135deg, var(--user), #335f7f);
      color: white;
      border-bottom-right-radius: 10px;
    }

    .message.assistant .bubble {
      background: rgba(255, 253, 249, 0.98);
      border-bottom-left-radius: 10px;
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
      border-radius: 18px;
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
      border-radius: 14px;
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

    .composer {
      padding: 18px 22px 22px;
      border-top: 1px solid var(--line);
      background: rgba(255, 252, 247, 0.94);
    }

    .composer-row {
      display: grid;
      grid-template-columns: minmax(0, 1fr) auto;
      gap: 14px;
      align-items: end;
    }

    .composer-actions {
      display: flex;
      flex-direction: column;
      gap: 10px;
    }

    .hint {
      color: var(--muted);
      font-size: 13px;
      line-height: 1.5;
    }

    .status {
      color: var(--muted);
      font-size: 13px;
      min-height: 20px;
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
    }
  </style>
</head>
<body>
  <div class="shell">
    <aside class="panel sidebar">
      <section class="brand">
        <div class="eyebrow">Clawd Codex</div>
        <h1>Web Console</h1>
        <p>Use the local agent from a browser while keeping the existing CLI intact.</p>
        <div class="workspace" id="workspaceRoot">Loading workspace...</div>
      </section>

      <section class="card">
        <h2>Session Setup</h2>
        <div class="field">
          <label for="providerSelect">Provider</label>
          <select id="providerSelect"></select>
        </div>
        <div class="field">
          <label for="modelInput">Model</label>
          <input id="modelInput" type="text" placeholder="Enter a model name">
        </div>
        <div class="toggle">
          <input id="autoApproveToggle" type="checkbox" checked>
          <label for="autoApproveToggle">Auto-approve tool permission prompts inside this workspace</label>
        </div>
        <div class="actions">
          <button id="newSessionBtn" class="primary" type="button">New Session</button>
          <button id="resetSessionBtn" class="secondary" type="button">Reset Chat</button>
        </div>
      </section>

      <section class="card tips">
        <h2>Notes</h2>
        <p class="hint">The web UI uses the same configured provider credentials as the CLI. If a provider has no API key, create one with <code>clawd login</code>.</p>
        <p class="hint">Questionnaire-style tool prompts are intentionally hidden from the web tool list for now, so the browser session stays responsive.</p>
      </section>
    </aside>

    <main class="panel main">
      <header class="topbar">
        <div>
          <h2 id="sessionTitle">Ready to chat</h2>
          <div class="meta">
            <span id="providerMeta">Provider: --</span>
            <span id="modelMeta">Model: --</span>
            <span id="sessionMeta">Session: --</span>
          </div>
        </div>
        <div class="badge" id="statusBadge">Idle</div>
      </header>

      <section id="chatLog" class="chat">
        <div class="hero">
          <strong>Browser-first workflow</strong>
          Ask about the current workspace, inspect files, or request edits. Tool activity for each answer appears in expandable notes below the assistant response.
        </div>
      </section>

      <footer class="composer">
        <div class="status" id="statusLine"></div>
        <form id="composerForm" class="composer-row">
          <textarea id="promptInput" placeholder="Ask Clawd to inspect the project, explain code, or make a change..."></textarea>
          <div class="composer-actions">
            <button id="sendBtn" class="primary" type="submit">Send</button>
            <button id="clearDraftBtn" class="secondary" type="button">Clear</button>
          </div>
        </form>
      </footer>
    </main>
  </div>

  <script>
    const STORAGE_KEY = "clawd-web-console";
    const state = {
      config: null,
      sessionId: null,
      provider: null,
      model: null,
      busy: false,
    };

    const providerSelect = document.getElementById("providerSelect");
    const modelInput = document.getElementById("modelInput");
    const autoApproveToggle = document.getElementById("autoApproveToggle");
    const newSessionBtn = document.getElementById("newSessionBtn");
    const resetSessionBtn = document.getElementById("resetSessionBtn");
    const chatLog = document.getElementById("chatLog");
    const promptInput = document.getElementById("promptInput");
    const sendBtn = document.getElementById("sendBtn");
    const clearDraftBtn = document.getElementById("clearDraftBtn");
    const statusLine = document.getElementById("statusLine");
    const statusBadge = document.getElementById("statusBadge");
    const sessionTitle = document.getElementById("sessionTitle");
    const providerMeta = document.getElementById("providerMeta");
    const modelMeta = document.getElementById("modelMeta");
    const sessionMeta = document.getElementById("sessionMeta");
    const workspaceRoot = document.getElementById("workspaceRoot");

    function setBusy(isBusy, label = "Working...") {
      state.busy = isBusy;
      sendBtn.disabled = isBusy;
      newSessionBtn.disabled = isBusy;
      resetSessionBtn.disabled = isBusy;
      providerSelect.disabled = isBusy;
      modelInput.disabled = isBusy;
      autoApproveToggle.disabled = isBusy;
      statusBadge.textContent = isBusy ? label : "Idle";
      statusLine.textContent = isBusy ? "Running the agent loop..." : "";
    }

    function setStatus(message, isError = false) {
      statusLine.textContent = message || "";
      statusLine.className = "status" + (isError ? " warning" : "");
    }

    function saveLocalState() {
      const payload = {
        sessionId: state.sessionId,
        provider: state.provider,
        model: state.model,
        autoApprove: autoApproveToggle.checked,
      };
      localStorage.setItem(STORAGE_KEY, JSON.stringify(payload));
    }

    function loadLocalState() {
      try {
        return JSON.parse(localStorage.getItem(STORAGE_KEY) || "null");
      } catch (_err) {
        return null;
      }
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
      const payload = text ? JSON.parse(text) : {};
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
        option.textContent = provider.label + (provider.configured ? "" : " (missing API key)");
        providerSelect.appendChild(option);
      }
    }

    function applyConfigDefaults(preferred) {
      const providerName = preferred?.provider || state.config.default_provider;
      providerSelect.value = providerByName(providerName) ? providerName : state.config.default_provider;
      const provider = providerByName(providerSelect.value);
      const model = preferred?.model || provider?.default_model || "";
      modelInput.value = model;
      autoApproveToggle.checked = preferred?.autoApprove ?? true;
    }

    function updateMeta(session) {
      sessionTitle.textContent = session.messages.length ? "Workspace conversation" : "Fresh session";
      providerMeta.textContent = "Provider: " + session.provider;
      modelMeta.textContent = "Model: " + session.model;
      sessionMeta.textContent = "Session: " + session.session_id;
      state.sessionId = session.session_id;
      state.provider = session.provider;
      state.model = session.model;
      providerSelect.value = session.provider;
      modelInput.value = session.model;
      saveLocalState();
    }

    function escapeHtml(text) {
      return text
        .replaceAll("&", "&amp;")
        .replaceAll("<", "&lt;")
        .replaceAll(">", "&gt;");
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

    function createMessage(role, text, events = []) {
      const wrapper = document.createElement("article");
      wrapper.className = "message " + role;

      const label = document.createElement("div");
      label.className = "message-label";
      label.textContent = role === "user" ? "You" : role === "assistant" ? "Clawd" : "System";
      wrapper.appendChild(label);

      const bubble = document.createElement("div");
      bubble.className = "bubble";
      bubble.textContent = text || (role === "assistant" ? "[No text response]" : "");
      wrapper.appendChild(bubble);

      if (events.length) {
        const details = document.createElement("details");
        details.className = "tool-events";

        const summary = document.createElement("summary");
        summary.textContent = "Tool activity (" + events.length + ")";
        details.appendChild(summary);

        const eventList = document.createElement("div");
        eventList.className = "event-list";

        for (const event of events) {
          const item = document.createElement("div");
          item.className = "event";
          const title = document.createElement("strong");
          title.textContent = event.kind === "permission"
            ? "Permission · " + event.tool_name
            : event.tool_name + " · " + event.kind;
          item.appendChild(title);

          const body = document.createElement("div");
          body.textContent = event.summary || event.message || event.error || "";
          item.appendChild(body);

          const preview = renderPreview(event.preview);
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
      hero.innerHTML = "<strong>Browser-first workflow</strong>Use the same local agent from your browser. The current workspace and tool output stay attached to this session.";
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

    async function createSession() {
      setBusy(true, "Starting...");
      try {
        const payload = await api("/api/sessions", {
          method: "POST",
          body: JSON.stringify({
            provider: providerSelect.value,
            model: modelInput.value.trim(),
            auto_approve: autoApproveToggle.checked,
          }),
        });
        updateMeta(payload.session);
        renderMessages(payload.session.messages);
        setStatus("New session ready.");
      } catch (error) {
        setStatus(error.message, true);
      } finally {
        setBusy(false);
      }
    }

    async function loadSession(sessionId) {
      const payload = await api("/api/sessions/" + encodeURIComponent(sessionId));
      updateMeta(payload.session);
      renderMessages(payload.session.messages);
    }

    async function resetSession() {
      if (!state.sessionId) return;
      setBusy(true, "Resetting...");
      try {
        const payload = await api("/api/sessions/" + encodeURIComponent(state.sessionId) + "/reset", {
          method: "POST",
          body: JSON.stringify({
            auto_approve: autoApproveToggle.checked,
          }),
        });
        updateMeta(payload.session);
        renderMessages(payload.session.messages);
        setStatus("Conversation cleared.");
      } catch (error) {
        setStatus(error.message, true);
      } finally {
        setBusy(false);
      }
    }

    async function ensureMatchingSession() {
      if (!state.sessionId) {
        await createSession();
        return;
      }
      if (providerSelect.value !== state.provider || modelInput.value.trim() !== state.model) {
        await createSession();
      }
    }

    async function sendPrompt(event) {
      event.preventDefault();
      const message = promptInput.value.trim();
      if (!message || state.busy) return;

      setBusy(true, "Thinking...");
      setStatus("");
      try {
        await ensureMatchingSession();
        if (!state.sessionId) {
          throw new Error("Session is not ready yet.");
        }

        const userMessage = createMessage("user", message);
        chatLog.appendChild(userMessage);
        chatLog.scrollTop = chatLog.scrollHeight;
        promptInput.value = "";

        const payload = await api("/api/sessions/" + encodeURIComponent(state.sessionId) + "/messages", {
          method: "POST",
          body: JSON.stringify({
            message,
            auto_approve: autoApproveToggle.checked,
          }),
        });

        updateMeta(payload.session);
        appendAssistantReply(payload.reply);
        const usage = payload.reply.usage || {};
        const tokenBits = [];
        if (usage.input_tokens) tokenBits.push("input " + usage.input_tokens);
        if (usage.output_tokens) tokenBits.push("output " + usage.output_tokens);
        setStatus(tokenBits.length ? "Turn complete: " + tokenBits.join(" / ") : "Turn complete.");
      } catch (error) {
        chatLog.appendChild(createMessage("system", error.message));
        chatLog.scrollTop = chatLog.scrollHeight;
        setStatus(error.message, true);
      } finally {
        setBusy(false);
      }
    }

    providerSelect.addEventListener("change", () => {
      const provider = providerByName(providerSelect.value);
      if (provider) {
        modelInput.value = provider.default_model || "";
      }
    });

    newSessionBtn.addEventListener("click", createSession);
    resetSessionBtn.addEventListener("click", resetSession);
    clearDraftBtn.addEventListener("click", () => {
      promptInput.value = "";
      promptInput.focus();
    });
    document.getElementById("composerForm").addEventListener("submit", sendPrompt);

    async function init() {
      setBusy(true, "Loading...");
      try {
        state.config = await api("/api/config");
        workspaceRoot.textContent = state.config.workspace_root;
        populateProviders();
        const local = loadLocalState();
        applyConfigDefaults(local);
        if (local?.sessionId) {
          try {
            await loadSession(local.sessionId);
            setStatus("Restored previous session.");
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
class WebSessionState:
    """State tracked for a browser-backed conversation."""

    session: Session
    provider_name: str
    provider: Any
    tool_registry: ToolRegistry
    tool_context: ToolContext
    auto_approve: bool = True
    lock: threading.RLock = field(default_factory=threading.RLock)


class ClawdWebService:
    """Owns browser sessions and the local agent runtime."""

    def __init__(self, workspace_root: Path | None = None) -> None:
        self.workspace_root = Path(workspace_root or Path.cwd()).resolve()
        self._sessions: dict[str, WebSessionState] = {}
        self._lock = threading.RLock()

    def get_bootstrap_payload(self) -> dict[str, Any]:
        """Return config data needed by the browser shell."""
        config = load_config()
        configured = config.get("providers", {})
        providers: list[dict[str, Any]] = []
        for name, info in PROVIDER_INFO.items():
            provider_config = configured.get(name, {})
            providers.append(
                {
                    "name": name,
                    "label": info["label"],
                    "configured": bool(provider_config.get("api_key")),
                    "base_url": provider_config.get("base_url", info["default_base_url"]),
                    "default_model": provider_config.get("default_model", info["default_model"]),
                    "available_models": info["available_models"],
                }
            )
        return {
            "workspace_root": str(self.workspace_root),
            "default_provider": config.get("default_provider", "anthropic"),
            "providers": providers,
        }

    def create_session(
        self,
        *,
        provider_name: str | None = None,
        model: str | None = None,
        auto_approve: bool = True,
    ) -> dict[str, Any]:
        """Create a new in-memory browser session."""
        provider_name = provider_name or load_config().get("default_provider", "anthropic")
        self._ensure_known_provider(provider_name)
        provider_config = get_provider_config(provider_name)
        if not provider_config.get("api_key"):
            raise ValueError(
                f"{provider_name} API key is not configured. Run `clawd login` and set one first."
            )

        provider_class = get_provider_class(provider_name)
        resolved_model = (model or "").strip() or provider_config.get("default_model")
        provider = provider_class(
            api_key=provider_config["api_key"],
            base_url=provider_config.get("base_url"),
            model=resolved_model,
        )

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
        )

        with self._lock:
            self._sessions[session.session_id] = state
        return {"session": self._serialize_session(state)}

    def get_session_payload(self, session_id: str) -> dict[str, Any]:
        """Load a current browser session payload."""
        state = self._require_session(session_id)
        with state.lock:
            return {"session": self._serialize_session(state)}

    def reset_session(self, session_id: str, *, auto_approve: bool | None = None) -> dict[str, Any]:
        """Clear the conversation while keeping provider/model choices."""
        state = self._require_session(session_id)
        with state.lock:
            if auto_approve is not None:
                state.auto_approve = auto_approve
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
    ) -> dict[str, Any]:
        """Run one agent turn for a browser session."""
        cleaned = message.strip()
        if not cleaned:
            raise ValueError("message must not be empty")

        state = self._require_session(session_id)
        with state.lock:
            if auto_approve is not None:
                state.auto_approve = auto_approve

            events: list[dict[str, Any]] = []
            state.tool_context.outbox.clear()
            state.tool_context.ask_user = None
            state.tool_context.permission_handler = self._build_permission_handler(state, events)
            state.session.conversation.add_user_message(cleaned)

            result = run_agent_loop(
                conversation=state.session.conversation,
                provider=state.provider,
                tool_registry=state.tool_registry,
                tool_context=state.tool_context,
                max_turns=max_turns,
                stream=False,
                verbose=False,
                on_event=lambda event: events.append(self._serialize_tool_event(event)),
                on_text_chunk=None,
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
            "messages": self._serialize_messages(state.session),
        }

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

        return {
            "kind": event.kind,
            "tool_name": event.tool_name,
            "tool_use_id": event.tool_use_id,
            "summary": summary,
            "preview": preview,
            "error": event.error,
            "is_error": event.is_error,
        }

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
        if parsed.path.startswith("/api/sessions/"):
            session_id = parsed.path.removeprefix("/api/sessions/")
            if not session_id or "/" in session_id:
                self._send_error_json(HTTPStatus.NOT_FOUND, "Unknown route")
                return
            try:
                payload = self.server.service.get_session_payload(session_id)
            except KeyError as exc:
                self._send_error_json(HTTPStatus.NOT_FOUND, str(exc))
                return
            self._send_json(HTTPStatus.OK, payload)
            return
        self._send_error_json(HTTPStatus.NOT_FOUND, "Unknown route")

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
                )
            except ValueError as exc:
                self._send_error_json(HTTPStatus.BAD_REQUEST, str(exc))
                return
            self._send_json(HTTPStatus.CREATED, result)
            return

        if parsed.path.startswith("/api/sessions/") and parsed.path.endswith("/reset"):
            session_id = parsed.path.removeprefix("/api/sessions/").removesuffix("/reset").rstrip("/")
            try:
                result = self.server.service.reset_session(
                    session_id,
                    auto_approve=self._optional_bool(payload, "auto_approve", None),
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
                self._send_error_json(HTTPStatus.BAD_REQUEST, "message is required")
                return
            try:
                result = self.server.service.send_message(
                    session_id,
                    message,
                    auto_approve=self._optional_bool(payload, "auto_approve", None),
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

        self._send_error_json(HTTPStatus.NOT_FOUND, "Unknown route")

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
            raise ValueError(f"Invalid JSON body: {exc.msg}") from exc
        if not isinstance(data, dict):
            raise ValueError("JSON body must be an object")
        return data

    def _optional_string(self, payload: dict[str, Any], key: str) -> str | None:
        value = payload.get(key)
        if value is None:
            return None
        if not isinstance(value, str):
            raise ValueError(f"{key} must be a string")
        return value

    def _optional_bool(self, payload: dict[str, Any], key: str, default: bool | None) -> bool | None:
        value = payload.get(key, default)
        if value is None:
            return None
        if not isinstance(value, bool):
            raise ValueError(f"{key} must be a boolean")
        return value

    def _send_json(self, status: HTTPStatus, payload: dict[str, Any]) -> None:
        self._send_bytes(status, json.dumps(payload, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

    def _send_error_json(self, status: HTTPStatus, message: str) -> None:
        self._send_json(status, {"error": message})

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
    print(f"Clawd Web UI is running at {url}")
    print(f"Workspace root: {service.workspace_root}")
    print("Press Ctrl+C to stop the server.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping Clawd Web UI...")
    finally:
        server.server_close()
