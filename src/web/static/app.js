    const LOCAL_STATE_KEY = "clawd-web-console";
    const WEB_MODEL = "deepseek-v4-pro";
    const WEB_AIRCRAFT_SKILL = "aircraft-design-skill";
    const DESIGN_ENERGY_CONFIG = Object.freeze({
      prop: Object.freeze({
        field: "prop_bsfc_kg_per_j",
        label: "螺旋桨功率比油耗（BSFC，kg/J）",
        inputLabel: "螺旋桨功率比油耗",
        defaultValue: 8.45e-8,
        min: 1e-10,
        max: 1e-5,
      }),
      jet: Object.freeze({
        field: "jet_tsfc_kg_per_n_s",
        label: "喷气发动机推力比油耗（TSFC，kg/(N·s)）",
        inputLabel: "喷气发动机推力比油耗",
        defaultValue: 2.3e-5,
        min: 1e-9,
        max: 1e-3,
      }),
    });
    const state = {
      config: null,
      sessionId: null,
      provider: null,
      model: null,
      autoSkill: null,
      sessions: [],
      busy: false,
      abortController: null,
      view: "chat",
      designJobId: null,
      designJobRunning: false,
      designJobEvents: [],
      designJobMessage: null,
      designJobSequence: 0,
      designJobs: [],
      renderedDesignJobId: null,
      designStreamController: null,
      designTab: "results",
      activeDesignJob: null,
      designJobDetails: {},
      compareJobIds: [],
      selectedResultFile: null,
      designModelViewer: null,
      preflightRequestFingerprint: null,
      preflightFingerprint: null,
      confirmedPreflightFingerprint: null,
      designFieldSources: {},
      designEnergyValues: {
        prop: DESIGN_ENERGY_CONFIG.prop.defaultValue,
        jet: DESIGN_ENERGY_CONFIG.jet.defaultValue,
      },
      designLegacyEnergy: { prop: null, jet: null },
    };

    const providerSelect = document.getElementById("providerSelect");
    const modelInput = document.getElementById("modelInput");
    const modelDatalist = document.getElementById("modelDatalist");
    const aircraftSkillToggle = document.getElementById("aircraftSkillToggle");
    const autoApproveToggle = document.getElementById("autoApproveToggle");
    const newSessionBtn = document.getElementById("newSessionBtn");
    const chatViewBtn = document.getElementById("chatViewBtn");
    const resetSessionBtn = document.getElementById("resetSessionBtn");
    const sessionList = document.getElementById("sessionList");
    const chatLog = document.getElementById("chatLog");
    const mainPanel = document.querySelector(".main");
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
    const evidenceMode = document.getElementById("evidenceMode");
    const toolMode = document.getElementById("toolMode");
    const designWorkspaceBtn = document.getElementById("designWorkspaceBtn");
    const designBackChatBtn = document.getElementById("designBackChatBtn");
    const designWorkspace = document.getElementById("designWorkspace");
    const designActiveJobLabel = document.getElementById("designActiveJobLabel");
    const settingsOverlay = document.getElementById("settingsOverlay");
    const settingsToggleBtn = document.getElementById("settingsToggleBtn");
    const settingsTopBtn = document.getElementById("settingsTopBtn");
    const settingsCloseBtn = document.getElementById("settingsCloseBtn");
    const composer = document.querySelector(".composer");
    const designRunForm = document.getElementById("designRunForm");
    const designProjectName = document.getElementById("designProjectName");
    const designRangeKm = document.getElementById("designRangeKm");
    const designPayloadKg = document.getElementById("designPayloadKg");
    const designCruiseMach = document.getElementById("designCruiseMach");
    const designCruiseAltitude = document.getElementById("designCruiseAltitude");
    const designTakeoffDistance = document.getElementById("designTakeoffDistance");
    const designLandingDistance = document.getElementById("designLandingDistance");
    const designServiceCeiling = document.getElementById("designServiceCeiling");
    const designMaxLoadFactor = document.getElementById("designMaxLoadFactor");
    const designSustainedTurnG = document.getElementById("designSustainedTurnG");
    const designAircraftRole = document.getElementById("designAircraftRole");
    const designPropulsionType = document.getElementById("designPropulsionType");
    const designReserveFraction = document.getElementById("designReserveFraction");
    const designTailLayout = document.getElementById("designTailLayout");
    const designClmaxTakeoff = document.getElementById("designClmaxTakeoff");
    const designClmaxLanding = document.getElementById("designClmaxLanding");
    const designAssumedClimbRate = document.getElementById("designAssumedClimbRate");
    const designUncertaintyEnabled = document.getElementById("designUncertaintyEnabled");
    const designAutoRepairEnabled = document.getElementById("designAutoRepairEnabled");
    const designMaxRepairAttempts = document.getElementById("designMaxRepairAttempts");
    const designUseAdvanced = document.getElementById("designUseAdvanced");
    const designAdvancedPanel = document.getElementById("designAdvancedPanel");
    const designMtowGuess = document.getElementById("designMtowGuess");
    const designWingLoading = document.getElementById("designWingLoading");
    const designThrustWeight = document.getElementById("designThrustWeight");
    const designAspectRatio = document.getElementById("designAspectRatio");
    const designSweepDeg = document.getElementById("designSweepDeg");
    const designTaperRatio = document.getElementById("designTaperRatio");
    const designThicknessRatio = document.getElementById("designThicknessRatio");
    const designSfc = document.getElementById("designSfc");
    const designSfcLabel = document.getElementById("designSfcLabel");
    const designPropEfficiencyField = document.getElementById("designPropEfficiencyField");
    const designPropEfficiency = document.getElementById("designPropEfficiency");
    const designCd0 = document.getElementById("designCd0");
    const designOswald = document.getElementById("designOswald");
    const designCgFraction = document.getElementById("designCgFraction");
    const designTailVolume = document.getElementById("designTailVolume");
    const designTolerance = document.getElementById("designTolerance");
    const designMaxIterations = document.getElementById("designMaxIterations");
    const designRunBtn = document.getElementById("designRunBtn");
    const designCancelBtn = document.getElementById("designCancelBtn");
    const designRetryBtn = document.getElementById("designRetryBtn");
    const designProgress = document.getElementById("designProgress");
    const designRunStatus = document.getElementById("designRunStatus");
    const designJobHistoryList = document.getElementById("designJobHistoryList");
    const designHistoryRefreshBtn = document.getElementById("designHistoryRefreshBtn");
    const designRunTimeline = document.getElementById("designRunTimeline");
    const designResultsContent = document.getElementById("designResultsContent");
    const designLoadAdjustBtn = document.getElementById("designLoadAdjustBtn");
    const designResultVersionSelect = document.getElementById("designResultVersionSelect");
    const designTabCompare = document.getElementById("designTabCompare");
    const designCompareSelector = document.getElementById("designCompareSelector");
    const designCompareContent = document.getElementById("designCompareContent");
    const designReportList = document.getElementById("designReportList");
    const designReportPreview = document.getElementById("designReportPreview");
    const designPreflightBtn = document.getElementById("designPreflightBtn");
    const designPreflightState = document.getElementById("designPreflightState");
    const designPreflightSummary = document.getElementById("designPreflightSummary");
    const designPreflightConfirm = document.getElementById("designPreflightConfirm");
    let settingsReturnFocus = null;
    let designPreflightTimer = null;
    const designFieldPaths = new Map([
      [designProjectName, "project_name"],
      [designRangeKm, "requirements.range_m"],
      [designPayloadKg, "requirements.payload_kg"],
      [designCruiseMach, "requirements.cruise_mach"],
      [designCruiseAltitude, "requirements.cruise_altitude_m"],
      [designTakeoffDistance, "requirements.takeoff_distance_m"],
      [designLandingDistance, "requirements.landing_distance_m"],
      [designMaxLoadFactor, "requirements.max_load_factor"],
      [designSustainedTurnG, "requirements.sustained_turn_g"],
      [designServiceCeiling, "requirements.service_ceiling_m"],
      [designAircraftRole, "requirements.aircraft_role"],
      [designPropulsionType, "requirements.propulsion_type"],
      [designReserveFraction, "requirements.reserve_fraction"],
      [designTailLayout, "requirements.tail_layout"],
      [designClmaxTakeoff, "requirements.cl_max_takeoff"],
      [designClmaxLanding, "requirements.cl_max_landing"],
      [designAssumedClimbRate, "requirements.assumed_climb_rate_m_s"],
      [designUncertaintyEnabled, "requirements.uncertainty_enabled"],
      [designAutoRepairEnabled, "solver.auto_repair_enabled"],
      [designMaxRepairAttempts, "solver.max_repair_attempts"],
      [designMtowGuess, "initial_guess.mtow_kg"],
      [designWingLoading, "initial_guess.wing_loading_pa"],
      [designThrustWeight, "initial_guess.thrust_to_weight"],
      [designAspectRatio, "initial_guess.aspect_ratio"],
      [designSweepDeg, "initial_guess.sweep_deg"],
      [designTaperRatio, "initial_guess.taper_ratio"],
      [designThicknessRatio, "initial_guess.thickness_ratio"],
      [designPropEfficiency, "initial_guess.prop_efficiency"],
      [designCd0, "initial_guess.cd0"],
      [designOswald, "initial_guess.oswald_e"],
      [designCgFraction, "initial_guess.cg_fraction_cbar"],
      [designTailVolume, "initial_guess.horizontal_tail_volume_coefficient"],
      [designTolerance, "solver.tolerance"],
      [designMaxIterations, "solver.max_iterations"],
    ]);

    function setBusy(isBusy, label = "处理中...") {
      state.busy = isBusy;
      sendBtn.disabled = isBusy;
      newSessionBtn.disabled = isBusy;
      resetSessionBtn.disabled = isBusy;
      providerSelect.disabled = isBusy;
      modelInput.disabled = isBusy;
      designWorkspaceBtn.disabled = isBusy || !state.designJobs.length;
      aircraftSkillToggle.disabled = isBusy || !skillByName(WEB_AIRCRAFT_SKILL);
      autoApproveToggle.disabled = isBusy;
      stopBtn.disabled = !isBusy;
      statusBadge.textContent = isBusy ? label : "待命";
      statusBadge.className = "badge " + (isBusy ? "is-busy" : "is-idle");
      statusLine.textContent = isBusy ? "正在运行工程智能体..." : "";
      if (state.config) updateSkillStatus();
    }

    function setStatus(message, isError = false) {
      statusLine.textContent = message || "";
      statusLine.className = "status" + (isError ? " warning" : "");
      statusLine.setAttribute("role", isError ? "alert" : "status");
      statusLine.setAttribute("aria-live", isError ? "assertive" : "polite");
    }

    function setDesignRunBusy(isBusy, message = "") {
      state.designJobRunning = isBusy;
      if (designRunBtn) designRunBtn.disabled = isBusy || !designPreflightConfirm?.checked;
      if (designCancelBtn) designCancelBtn.disabled = !isBusy || !state.designJobId;
      if (designRetryBtn) designRetryBtn.disabled = isBusy || !state.designJobId;
      if (designPreflightBtn) designPreflightBtn.disabled = isBusy;
      for (const input of designRunForm?.querySelectorAll("input, select") || []) {
        input.disabled = isBusy || (input.hasAttribute("data-design-advanced") && !designUseAdvanced?.checked);
      }
      if (designRunForm) {
        syncDesignEnergyMode();
        syncAutoRepairInputs();
      }
      if (designPreflightConfirm) designPreflightConfirm.disabled = isBusy || !state.preflightFingerprint;
      if (message && designRunStatus) designRunStatus.textContent = message;
      if (isBusy) {
        statusBadge.textContent = "计算中";
        statusBadge.className = "badge is-busy";
      } else if (!state.busy) {
        statusBadge.textContent = "待命";
        statusBadge.className = "badge is-idle";
      }
      renderDesignRunTimeline();
    }

    function setActiveView(view) {
      if (view === "design" && !state.designJobs.length) {
        view = "chat";
        setStatus("当前对话尚未生成总体设计结果。请先在对话中启用技能并提交总体设计需求。", true);
      }
      if (view !== "design") disposeDesignModelViewer();
      state.view = view;
      chatLog.hidden = view !== "chat";
      designWorkspace.hidden = view !== "design";
      composer.hidden = view !== "chat";
      designWorkspaceBtn.classList.toggle("active", view === "design");
      chatViewBtn.classList.toggle("active", view === "chat");
      mainPanel.classList.toggle("is-design-mode", view === "design");
      if (view === "design") {
        renderDesignWorkspace();
      } else {
        refreshHeroIfEmpty();
      }
    }

    function setSettingsOpen(isOpen) {
      if (isOpen) settingsReturnFocus = document.activeElement;
      settingsOverlay.classList.toggle("is-open", isOpen);
      settingsOverlay.setAttribute("aria-hidden", isOpen ? "false" : "true");
      document.querySelector(".shell").inert = isOpen;
      if (isOpen) {
        settingsCloseBtn.focus();
      } else if (settingsReturnFocus instanceof HTMLElement) {
        settingsReturnFocus.focus();
        settingsReturnFocus = null;
      }
    }

    function setDesignTab(tab, options = {}) {
      const allowed = ["results", "compare", "reports"];
      const requested = allowed.includes(tab) ? tab : "results";
      const selected = requested === "compare" && state.designJobs.length < 2 ? "results" : requested;
      state.designTab = selected;
      for (const button of document.querySelectorAll("[data-design-tab]")) {
        const active = button.dataset.designTab === selected;
        button.classList.toggle("is-active", active);
        button.setAttribute("aria-selected", active ? "true" : "false");
        button.tabIndex = active ? 0 : -1;
        if (active && options.focus) button.focus();
      }
      for (const panel of document.querySelectorAll("[data-design-panel]")) {
        panel.hidden = panel.dataset.designPanel !== selected;
      }
      if (selected !== "results") disposeDesignModelViewer();
      if (selected === "results") requestAnimationFrame(activateDesignModelPreview);
      if (selected === "compare") renderDesignComparison();
      if (selected === "reports") renderDesignReports();
    }

    function autosizePrompt() {
      promptInput.style.height = "auto";
      promptInput.style.height = Math.min(promptInput.scrollHeight, 220) + "px";
    }

    function saveLocalState() {
      const payload = {
        sessionId: state.sessionId,
        provider: providerSelect.value || state.provider,
        model: WEB_MODEL,
        autoSkill: selectedSkillName() || null,
        autoApprove: autoApproveToggle.checked,
        designJobId: state.designJobId,
      };
      localStorage.setItem(LOCAL_STATE_KEY, JSON.stringify(payload));
    }

    function loadLocalState() {
      try {
        const saved = JSON.parse(localStorage.getItem(LOCAL_STATE_KEY) || "null");
        return saved;
      } catch (_err) {
        return null;
      }
    }

    function toUiSkillName(name) {
      return name || "";
    }

    function toInternalSkillName(name) {
      return name || null;
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
      const skill = skillByName(WEB_AIRCRAFT_SKILL);
      aircraftSkillToggle.disabled = state.busy || !skill;
      aircraftSkillToggle.title = skill?.description || "当前工作区未提供飞行器总体设计技能";
      if (!skill) aircraftSkillToggle.checked = false;
    }

    function skillByName(name) {
      return (state.config?.skills || []).find((item) => item.name === name) || null;
    }

    function skillDisplayName(name) {
      if (!name) return "无";
      const skill = skillByName(name);
      if (skill?.display_name) return skill.display_name;
      if (name === WEB_AIRCRAFT_SKILL) return "飞行器总体设计";
      return "/" + name;
    }

    function selectedSkillName() {
      return aircraftSkillToggle.checked ? WEB_AIRCRAFT_SKILL : "";
    }

    function setSelectedSkill(name) {
      aircraftSkillToggle.checked = toUiSkillName(name) === WEB_AIRCRAFT_SKILL;
    }

    function updateSkillMetaFromSelection() {
      const selected = selectedSkillName();
      const sessionSkill = state.autoSkill || "";
      const pending = selected !== sessionSkill;
      skillMeta.textContent = "工程模式：" + skillDisplayName(selected) + (pending ? "（下次发送生效）" : "");
    }

    function updateSkillStatus() {
      const selected = selectedSkillName();
      const ragSelected = selected === WEB_AIRCRAFT_SKILL;
      evidenceMode.textContent = selected ? (ragSelected ? "自动检索" : "按需检索") : "未启用";
      if (toolMode) toolMode.textContent = autoApproveToggle.checked ? "自动批准" : "手动确认";
      updateSkillMetaFromSelection();
      refreshHeroIfEmpty();
    }

    function applyConfigDefaults(preferred) {
      const provider = preferredWebProvider();
      providerSelect.value = provider?.name || state.config.default_provider;
      modelInput.value = WEB_MODEL;
      updateModelSuggestions();
      const preferredSkill = toUiSkillName(preferred?.autoSkill || "");
      const skillExists = preferredSkill === WEB_AIRCRAFT_SKILL && Boolean(skillByName(preferredSkill));
      setSelectedSkill(skillExists ? preferredSkill : "");
      autoApproveToggle.checked = preferred?.autoApprove ?? true;
      updateSkillStatus();
    }

    function syncSessionDesignResults(results) {
      const nextResults = Array.isArray(results)
        ? results.filter((item) => item?.source === "conversation" && item?.terminal === true && item?.result)
        : [];
      const previousId = state.activeDesignJob?.job_id;
      state.designJobs = nextResults;
      state.designJobDetails = Object.fromEntries(nextResults.map((item) => [item.job_id, item]));
      state.activeDesignJob = nextResults.find((item) => item.job_id === previousId) || nextResults[0] || null;
      state.designJobId = state.activeDesignJob?.job_id || null;
      state.compareJobIds = state.compareJobIds.filter((jobId) => nextResults.some((item) => item.job_id === jobId));
      state.selectedResultFile = null;

      const hasResults = nextResults.length > 0;
      designWorkspaceBtn.hidden = !hasResults;
      designWorkspaceBtn.disabled = state.busy || !hasResults;
      designWorkspaceBtn.setAttribute("aria-hidden", hasResults ? "false" : "true");
      designTabCompare.hidden = nextResults.length < 2;
      designTabCompare.setAttribute("aria-hidden", nextResults.length < 2 ? "true" : "false");
      if (state.designTab === "compare" && nextResults.length < 2) state.designTab = "results";
      if (!hasResults && state.view === "design") setActiveView("chat");
      if (hasResults && state.view === "design") renderDesignWorkspace();
    }

    function updateMeta(session) {
      sessionTitle.textContent = session.messages.length ? "工程设计会话" : "新的设计会话";
      providerMeta.textContent = "模型服务：" + session.provider;
      modelMeta.textContent = "模型：" + WEB_MODEL;
      skillMeta.textContent = "工程模式：" + skillDisplayName(toUiSkillName(session.auto_skill));
      sessionMeta.textContent = "会话：" + session.session_id;
      state.sessionId = session.session_id;
      state.provider = session.provider;
      state.model = WEB_MODEL;
      state.autoSkill = toUiSkillName(session.auto_skill);
      providerSelect.value = session.provider;
      modelInput.value = WEB_MODEL;
      setSelectedSkill(state.autoSkill);
      syncSessionDesignResults(session.design_results);
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
      return renderInlineWithMath(text);
    }

    function splitInlineMath(text) {
      const parts = [];
      let index = 0;
      while (index < text.length) {
        const inlineParen = text.indexOf("\\(", index);
        const dollar = text.indexOf("$", index);
        const candidates = [inlineParen, dollar].filter((item) => item >= 0);
        const next = candidates.length ? Math.min(...candidates) : -1;
        if (next < 0) {
          parts.push({ type: "text", value: text.slice(index) });
          break;
        }
        if (next > index) parts.push({ type: "text", value: text.slice(index, next) });
        if (next === inlineParen) {
          const end = text.indexOf("\\)", next + 2);
          if (end < 0) {
            parts.push({ type: "text", value: text.slice(next) });
            break;
          }
          parts.push({ type: "math", value: text.slice(next + 2, end) });
          index = end + 2;
          continue;
        }
        if (text[next + 1] === "$") {
          parts.push({ type: "text", value: "$$" });
          index = next + 2;
          continue;
        }
        const end = text.indexOf("$", next + 1);
        if (end < 0) {
          parts.push({ type: "text", value: text.slice(next) });
          break;
        }
        parts.push({ type: "math", value: text.slice(next + 1, end) });
        index = end + 1;
      }
      return parts;
    }

    function renderInlineWithMath(text) {
      const codeParts = text.split(/`([^`]+)`/g);
      return codeParts.map((part, index) => {
        if (index % 2 === 1) return "<code>" + escapeHtml(part) + "</code>";
        return splitInlineMath(part).map((innerPart) => {
          if (innerPart.type === "math") return renderLatex(innerPart.value, false);
          return renderInlineMarkdownText(innerPart.value);
        }).join("");
      }).join("");
    }

    function renderInlineMarkdownText(text) {
      return escapeHtml(text).replace(/(^|\s)\*\*([^*]+)\*\*(?=\s|$|[,.，。；;:：!?！？])/g, "$1<strong>$2</strong>");
    }

    function splitDisplayMath(text) {
      const parts = [];
      let index = 0;
      while (index < text.length) {
        const dollar = text.indexOf("$$", index);
        const bracket = text.indexOf("\\[", index);
        const candidates = [dollar, bracket].filter((item) => item >= 0);
        const next = candidates.length ? Math.min(...candidates) : -1;
        if (next < 0) {
          parts.push({ type: "text", value: text.slice(index) });
          break;
        }
        if (next > index) parts.push({ type: "text", value: text.slice(index, next) });
        if (next === dollar) {
          const end = text.indexOf("$$", next + 2);
          if (end < 0) {
            parts.push({ type: "text", value: text.slice(next) });
            break;
          }
          parts.push({ type: "math", value: text.slice(next + 2, end) });
          index = end + 2;
          continue;
        }
        const end = text.indexOf("\\]", next + 2);
        if (end < 0) {
          parts.push({ type: "text", value: text.slice(next) });
          break;
        }
        parts.push({ type: "math", value: text.slice(next + 2, end) });
        index = end + 2;
      }
      return parts;
    }

    function normalizeLatex(source) {
      return String(source || "")
        .replace(/\s+/g, " ")
        .replace(/\\left/g, "")
        .replace(/\\right/g, "")
        .trim();
    }

    function findMatchingBrace(source, openIndex) {
      let depth = 0;
      for (let index = openIndex; index < source.length; index += 1) {
        const char = source[index];
        if (char === "{" && source[index - 1] !== "\\") depth += 1;
        if (char === "}" && source[index - 1] !== "\\") {
          depth -= 1;
          if (depth === 0) return index;
        }
      }
      return -1;
    }

    function readLatexGroup(source, start) {
      if (source[start] !== "{") return null;
      const end = findMatchingBrace(source, start);
      if (end < 0) return null;
      return { value: source.slice(start + 1, end), end };
    }

    function renderLatex(source, display = false) {
      return '<span class="' + (display ? "math-display" : "math-inline") + '">' + renderLatexContent(normalizeLatex(source)) + "</span>";
    }

    function renderLatexContent(source) {
      const greek = {
        alpha: "α", beta: "β", gamma: "γ", Gamma: "Γ", delta: "δ", Delta: "Δ",
        epsilon: "ε", varepsilon: "ε", zeta: "ζ", eta: "η", theta: "θ", Theta: "Θ",
        lambda: "λ", Lambda: "Λ", mu: "μ", nu: "ν", xi: "ξ", pi: "π", Pi: "Π",
        rho: "ρ", sigma: "σ", Sigma: "Σ", tau: "τ", phi: "φ", varphi: "φ",
        Phi: "Φ", chi: "χ", psi: "ψ", Psi: "Ψ", omega: "ω", Omega: "Ω",
      };
      const commands = {
        cdot: "·", times: "×", pm: "±", mp: "∓", le: "≤", leq: "≤", ge: "≥", geq: "≥",
        approx: "≈", sim: "∼", neq: "≠", ne: "≠", infty: "∞", partial: "∂", nabla: "∇",
        degree: "°", circ: "°", to: "→", rightarrow: "→", leftarrow: "←",
      };
      let html = "";
      let index = 0;
      while (index < source.length) {
        if (source.startsWith("\\frac", index)) {
          const numerator = readLatexGroup(source, index + 5);
          const denominator = numerator ? readLatexGroup(source, numerator.end + 1) : null;
          if (numerator && denominator) {
            html += '<span class="math-frac"><span class="math-num">' + renderLatexContent(numerator.value) + '</span><span class="math-den">' + renderLatexContent(denominator.value) + "</span></span>";
            index = denominator.end + 1;
            continue;
          }
        }
        if (source.startsWith("\\sqrt", index)) {
          const group = readLatexGroup(source, index + 5);
          if (group) {
            html += '<span class="math-sqrt"><span class="math-root">√</span><span class="math-radicand">' + renderLatexContent(group.value) + "</span></span>";
            index = group.end + 1;
            continue;
          }
        }
        if (source.startsWith("\\text", index) || source.startsWith("\\mathrm", index)) {
          const offset = source.startsWith("\\text", index) ? 5 : 7;
          const group = readLatexGroup(source, index + offset);
          if (group) {
            html += '<span class="math-roman">' + escapeHtml(group.value) + "</span>";
            index = group.end + 1;
            continue;
          }
        }
        if (source[index] === "\\") {
          const match = source.slice(index + 1).match(/^[A-Za-z]+/);
          if (match) {
            const command = match[0];
            html += greek[command] || commands[command] || escapeHtml(command);
            index += command.length + 1;
            continue;
          }
          html += escapeHtml(source[index + 1] || "");
          index += 2;
          continue;
        }
        if (source[index] === "^" || source[index] === "_") {
          const isSup = source[index] === "^";
          const group = source[index + 1] === "{" ? readLatexGroup(source, index + 1) : null;
          const value = group ? group.value : source[index + 1] || "";
          html += (isSup ? "<sup>" : "<sub>") + renderLatexContent(value) + (isSup ? "</sup>" : "</sub>");
          index = group ? group.end + 1 : index + 2;
          continue;
        }
        if ("+-=<>≈≤≥×·/()[]|,".includes(source[index])) {
          html += '<span class="math-operator">' + escapeHtml(source[index]) + "</span>";
          index += 1;
          continue;
        }
        if (source[index] === "{") {
          const group = readLatexGroup(source, index);
          if (group) {
            html += renderLatexContent(group.value);
            index = group.end + 1;
            continue;
          }
        }
        html += source[index] === " " ? " " : escapeHtml(source[index]);
        index += 1;
      }
      return html;
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
      const lines = segment.replace(/\r\n/g, "\n").split("\n");
      let paragraph = [];
      let list = null;

      function flushParagraph() {
        if (!paragraph.length) return;
        appendMarkdownText(container, paragraph.join("\n"));
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
        const heading = trimmed.match(/^(#{1,3})\s+(.+)$/);
        if (heading) {
          flushParagraph();
          flushList();
          const level = String(Math.min(3, heading[1].length + 2));
          const h = document.createElement("h" + level);
          h.innerHTML = inlineMarkdown(heading[2]);
          container.appendChild(h);
          continue;
        }
        const quote = trimmed.match(/^>\s?(.+)$/);
        if (quote) {
          flushParagraph();
          flushList();
          const blockquote = document.createElement("blockquote");
          blockquote.innerHTML = inlineMarkdown(quote[1]);
          container.appendChild(blockquote);
          continue;
        }
        const bullet = trimmed.match(/^[-*]\s+(.+)$/);
        const ordered = trimmed.match(/^\d+\.\s+(.+)$/);
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

    function appendMarkdownText(container, text) {
      for (const part of splitDisplayMath(text)) {
        if (!part.value) continue;
        if (part.type === "math") {
          const wrapper = document.createElement("div");
          wrapper.innerHTML = renderLatex(part.value, true);
          container.appendChild(wrapper.firstChild);
          continue;
        }
        const lines = part.value.split("\n").map((line) => line.trim()).filter(Boolean);
        if (!lines.length) continue;
        const p = document.createElement("p");
        p.innerHTML = inlineMarkdown(lines.join(" "));
        container.appendChild(p);
      }
    }

    function renderMarkdownInto(container, text) {
      container.innerHTML = "";
      const source = text || "";
      if (!source) {
        container.textContent = "";
        return;
      }
      const parts = source.split(/```([\s\S]*?)```/g);
      for (let index = 0; index < parts.length; index += 1) {
        if (index % 2 === 0) {
          appendTextSegment(container, parts[index]);
          continue;
        }
        const raw = parts[index].replace(/^\w+\n/, "");
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

    function formatDuration(value) {
      const number = Number(value);
      if (!Number.isFinite(number) || number < 0) return "";
      const totalSeconds = Math.max(1, Math.round(number / 1000));
      if (totalSeconds < 60) return totalSeconds + "s";
      const minutes = Math.floor(totalSeconds / 60);
      const seconds = String(totalSeconds % 60).padStart(2, "0");
      if (minutes < 60) return minutes + "m " + seconds + "s";
      const hours = Math.floor(minutes / 60);
      const remainingMinutes = String(minutes % 60).padStart(2, "0");
      return hours + "h " + remainingMinutes + "m";
    }

    function formatCount(value) {
      const number = Number(value);
      if (!Number.isFinite(number)) return "--";
      return number.toLocaleString();
    }

    function formatBytes(value) {
      const number = Number(value);
      if (!Number.isFinite(number) || number < 0) return "--";
      if (number < 1024) return Math.round(number) + " B";
      const units = ["KB", "MB", "GB"];
      let scaled = number / 1024;
      let unitIndex = 0;
      while (scaled >= 1024 && unitIndex < units.length - 1) {
        scaled /= 1024;
        unitIndex += 1;
      }
      return scaled.toFixed(scaled >= 10 ? 1 : 2) + " " + units[unitIndex];
    }

    function cleanUiText(value) {
      return String(value ?? "")
        .replaceAll("aero-intake-exhaust-evaluation", "气动/进排气评估")
        .replaceAll("aero-propulsion-analysis", "气动/推进特性分析")
        .replaceAll("flight-performance-analysis", "飞行性能分析")
        .replaceAll("aircraft-design-skill", "飞行器总体设计")
        .replaceAll("aircraft-design-rag", "飞行器总体设计")
        .replaceAll("aircraft-design", "飞行器总体设计")
        .replaceAll("RAG index", "本地资料索引")
        .replaceAll("RAG", "本地资料");
    }

    function normalizeMessageOptions(options) {
      if (Array.isArray(options)) return { events: options };
      return options || {};
    }

    function mergeMessageEvents(...groups) {
      const merged = [];
      const seen = new Set();
      for (const group of groups) {
        if (!Array.isArray(group)) continue;
        for (const event of group) {
          if (!event || typeof event !== "object") continue;
          let key = "";
          if (event.event_id != null) key = "event:" + event.event_id;
          else if (event.sequence != null) key = "sequence:" + event.sequence + ":" + (event.kind || "");
          else {
            try { key = "value:" + JSON.stringify(event); } catch (_err) { key = ""; }
          }
          if (key && seen.has(key)) continue;
          if (key) seen.add(key);
          merged.push(event);
        }
      }
      return merged;
    }

    function requirementInteractionFromEvents(events = []) {
      for (let index = events.length - 1; index >= 0; index -= 1) {
        const event = events[index];
        const interaction = event?.kind === "requirement_interaction" ? event.preview?.interaction : null;
        if (interaction && typeof interaction === "object") return interaction;
      }
      return null;
    }

    function requirementRevisionId(interaction) {
      return String(interaction?.revision?.revision_id || "");
    }

    function latestRequirementRevisionId(messages = []) {
      let revisionId = "";
      for (const message of messages) {
        const interaction = requirementInteractionFromEvents(message?.events || []);
        if (interaction) revisionId = requirementRevisionId(interaction) || revisionId;
      }
      return revisionId;
    }

    function eventTitle(event) {
      if (event.kind === "design_stage") return "总体设计计算";
      if (event.kind === "agent_step") return cleanUiText(event.agent_name || event.tool_name || "智能体");
      if (event.kind === "planning") return "开始分析";
      if (event.kind === "drafting") return "组织回答";
      if (event.kind === "rag_retrieval") return "资料检索";
      const toolName = cleanUiText(event.tool_name || "工具");
      if (event.kind === "permission") return "权限确认 · " + toolName;
      if (event.kind === "tool_use") return "调用工具 · " + toolName;
      if (event.kind === "tool_result") return "工具结果 · " + toolName;
      return cleanUiText(event.tool_name || "工作项") + " · " + cleanUiText(event.kind || "记录");
    }

    function eventSummary(event) {
      return cleanUiText(event.summary || event.message || event.error || "");
    }

    function compactEventSummary(text, limit = 220) {
      const cleaned = cleanUiText(text).replace(/\s+/g, " ").trim();
      if (!cleaned) return "";
      return cleaned.length <= limit ? cleaned : cleaned.slice(0, limit - 1) + "…";
    }

    function toolDisplayName(event) {
      return cleanUiText(event.tool_name || event.tool || "工具");
    }

    function extractPreviewText(event) {
      if (event.rag || event.kind === "requirement_interaction") return "";
      const preview = renderPreview(event.preview);
      return compactEventSummary(preview, 360);
    }

    function eventStatsAt(events, index) {
      const stats = {
        searches: 0,
        fileLists: 0,
        fileReads: 0,
        commands: 0,
        previews: 0,
      };
      for (const event of events.slice(0, index + 1)) {
        const toolName = toolDisplayName(event).toLowerCase();
        const isDone = event.kind !== "tool_use";
        if (!isDone) continue;
        if (event.kind === "rag_retrieval" || toolName.includes("grep") || toolName.includes("search")) stats.searches += 1;
        else if (toolName.includes("glob")) stats.fileLists += 1;
        else if (toolName.includes("read")) stats.fileReads += 1;
        else if (toolName.includes("bash")) stats.commands += 1;
        else if (toolName.includes("preview")) stats.previews += 1;
      }
      return stats;
    }

    function eventStatusLabel(event, index = 0, events = []) {
      const toolName = toolDisplayName(event);
      const stats = eventStatsAt(events, index);
      if (event.kind === "rag_retrieval") {
        const hits = Array.isArray(event.rag?.hits) ? event.rag.hits.length : null;
        if (hits != null) return "已探索 " + hits + " 条资料";
        return "已完成资料检索";
      }
      if (event.kind === "design_stage") return designJobStatusLabel(event.stage);
      if (event.kind === "agent_step") return cleanUiText(event.agent_role || "智能体") + " · " + cleanUiText(event.stage || "协同");
      if (event.kind === "planning") return "已开始分析";
      if (event.kind === "permission") return "已确认权限";
      if (event.kind === "tool_use") {
        const lower = toolName.toLowerCase();
        if (lower.includes("grep") || lower.includes("search")) return "正在搜索";
        if (lower.includes("glob")) return "正在列出文件";
        if (lower.includes("read")) return "正在查看文件";
        if (lower.includes("bash")) return "正在执行命令";
        return "正在调用 " + toolName;
      }
      if (event.kind === "tool_result") {
        const lower = toolName.toLowerCase();
        if (lower.includes("grep") || lower.includes("search")) return "已探索 " + stats.searches + " 次搜索";
        if (lower.includes("glob")) return "已列出文件";
        if (lower.includes("read")) return "已探索 " + stats.fileReads + " 个文件";
        if (lower.includes("bash")) return "已执行 " + stats.commands + " 次命令";
        if (toolName.toLowerCase().includes("preview")) return "已查看 Preview";
        return "已完成 " + toolName;
      }
      if (event.kind === "request") return event.is_error ? "请求已中断" : "请求状态";
      if (event.kind === "drafting") return "已开始组织回答";
      return eventTitle(event);
    }

    function eventNarrative(event, index, events) {
      const summary = eventSummary(event);
      if (event.is_error) return compactEventSummary(summary || "这一步遇到错误，已记录下来供排查。");
      if (event.kind === "planning") {
        return compactEventSummary(summary || "我先拆解本轮工程设计需求，判断是否需要检索资料、查看文件或进行计算。");
      }
      if (event.kind === "drafting") {
        return compactEventSummary(summary || "我已经开始把可用依据、计算关系和设计结论组织成回答。");
      }
      if (event.kind === "rag_retrieval") {
        const hits = Array.isArray(event.rag?.hits) ? event.rag.hits.length : 0;
        if (hits > 0) return "我已经从本地资料里找到 " + hits + " 条相关证据，先把可用依据带入本轮设计判断。";
        return "我检查了本地资料，但这一轮没有找到直接匹配的证据，会基于已知条件和明确假设继续。";
      }
      if (event.kind === "agent_step") {
        const role = cleanUiText(event.agent_role || "智能体");
        const name = cleanUiText(event.agent_name || event.tool_name || "协同节点");
        return compactEventSummary(summary || role + "「" + name + "」完成了本轮协同设计流程中的一个检查点。");
      }
      if (event.kind === "permission") {
        return compactEventSummary(summary || "我确认了这一步所需的本地工具权限，然后继续执行。");
      }
      if (event.kind === "tool_use") {
        const toolName = toolDisplayName(event);
        const lower = toolName.toLowerCase();
        if (lower.includes("grep") || lower.includes("search")) return "我在相关资料和项目文件中继续搜索，想把关键参数或依据来源找得更准一些。";
        if (lower.includes("glob")) return "我先把候选文件列出来，缩小后续查看和引用的范围。";
        if (lower.includes("read")) return "我打开候选文件查看关键片段，避免只凭文件名或模糊印象判断。";
        if (lower.includes("bash")) return "我运行本地命令获取可验证输出，再把结果纳入回答。";
        return "我调用 " + toolName + " 来推进这一轮任务，并记录工具输入用于复查。";
      }
      if (event.kind === "tool_result") {
        const toolName = toolDisplayName(event);
        const lower = toolName.toLowerCase();
        if (lower.includes("grep") || lower.includes("search")) return "这次搜索已经返回结果，我会从里面挑出和当前设计问题最相关的依据。";
        if (lower.includes("glob")) return "候选文件列表已经出来了，下一步可以集中查看最可能有用的资料。";
        if (lower.includes("read")) return "我已经查看了文件内容，接下来把其中能支撑设计判断的部分整理进回答。";
        if (lower.includes("bash")) return "命令已经执行完，我会根据输出继续校核或汇总。";
        return compactEventSummary(summary || "这一步工具已经返回结果，我会把可用信息合并到最终回答里。");
      }
      return compactEventSummary(summary || "这一步执行完成，已记录到过程里。");
    }

    function eventIcon(event) {
      const toolName = toolDisplayName(event).toLowerCase();
      if (event.is_error) return "!";
      if (event.kind === "planning") return "›";
      if (event.kind === "drafting") return "✎";
      if (event.kind === "rag_retrieval") return "⌕";
      if (event.kind === "agent_step") {
        const name = cleanUiText(event.agent_name || event.tool_name || "");
        if (name.includes("Supervisor")) return "S";
        if (name.includes("管理员")) return "M";
        if (name.includes("检索")) return "⌕";
        if (name.includes("数据")) return "ƒ";
        return "A";
      }
      if (event.kind === "permission") return "✓";
      if (toolName.includes("grep") || toolName.includes("search")) return "⌕";
      if (toolName.includes("glob")) return "▣";
      if (toolName.includes("read")) return "□";
      if (toolName.includes("bash")) return "›";
      if (toolName.includes("preview")) return "⌘";
      return "·";
    }

    function latestEventSummary(events) {
      if (!events.length) return "";
      const latest = events[events.length - 1];
      const summary = eventSummary(latest);
      return summary ? eventTitle(latest) + " · " + summary : eventTitle(latest);
    }

    function summarizeProcess(events, options = {}) {
      const elapsed = formatDuration(options.elapsedMs);
      const parts = [options.isRunning ? "处理中" : "已处理"];
      if (elapsed) parts.push(elapsed);
      if (options.isRunning) {
        const latest = latestEventSummary(events);
        if (latest) parts.push(latest);
      } else if (events.length) {
        parts.push("过程记录 " + events.length);
      }
      return parts.join(" · ");
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
        "资料证据",
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
        note.textContent = cleanUiText(rag.message);
        panel.appendChild(note);
      }

      if (!hits.length && !rag?.message) {
        const empty = document.createElement("div");
        empty.className = "evidence-card";
        empty.textContent = "未找到匹配的本地证据。";
        panel.appendChild(empty);
        return panel;
      }

      const initialLimit = 3;
      let visibleLimit = Math.min(initialLimit, hits.length);
      const cards = document.createElement("div");
      cards.className = "evidence-panel";
      panel.appendChild(cards);

      const renderHits = () => {
        cards.innerHTML = "";
        for (const hit of hits.slice(0, visibleLimit)) {
          cards.appendChild(createEvidenceCard(hit));
        }
      };

      renderHits();

      if (hits.length > visibleLimit) {
        const more = document.createElement("button");
        more.type = "button";
        more.className = "evidence-more";
        more.textContent = "查看更多资料";
        more.addEventListener("click", () => {
          visibleLimit = Math.min(10, hits.length);
          renderHits();
          more.remove();
        });
        panel.appendChild(more);
      }
      return panel;
    }

    function createEvidenceCard(hit) {
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
        return card;
    }

    function collectEvidenceFromEvents(events = []) {
      return events
        .filter((event) => event && event.kind === "rag_retrieval" && event.rag)
        .map((event) => event.rag);
    }

    function createAnswerEvidence(events = []) {
      const evidences = collectEvidenceFromEvents(events);
      if (!evidences.length) return null;
      const latest = evidences[evidences.length - 1];
      const hits = Array.isArray(latest?.hits) ? latest.hits : [];

      const details = document.createElement("details");
      details.className = "answer-evidence";
      details.open = hits.length > 0;

      const summary = document.createElement("summary");
      const title = document.createElement("span");
      title.className = "answer-evidence-title";
      const strong = document.createElement("span");
      strong.textContent = "本轮参考资料";
      const small = document.createElement("small");
      const cache = latest?.cache?.enabled
        ? (latest.cache.ready === false ? "资料索引预热中" : (latest.cache.hit ? "缓存命中" : "完成本地检索"))
        : "本地资料检索";
      small.textContent = [
        cache,
        "用时 " + formatMs(latest?.timings?.total_ms),
        "候选 " + (latest?.candidate_chunks ?? "--"),
      ].join(" · ");
      title.appendChild(strong);
      title.appendChild(small);
      const count = document.createElement("span");
      count.className = "answer-evidence-count";
      count.textContent = "命中 " + hits.length + " 条";
      summary.appendChild(title);
      summary.appendChild(count);
      details.appendChild(summary);

      const body = document.createElement("div");
      body.className = "answer-evidence-body";
      body.appendChild(createEvidencePanel(latest));
      details.appendChild(body);
      return details;
    }

    function createArtifactsPanel(artifacts = []) {
      const visibleArtifacts = artifacts.filter((artifact) => artifact && artifact.download_url);
      if (!visibleArtifacts.length) return null;

      const panel = document.createElement("section");
      panel.className = "artifact-panel";

      const header = document.createElement("div");
      header.className = "artifact-panel-header";
      const title = document.createElement("span");
      title.textContent = "结果下载";
      const count = document.createElement("span");
      count.textContent = visibleArtifacts.length + " 个文件包";
      header.appendChild(title);
      header.appendChild(count);
      panel.appendChild(header);

      const list = document.createElement("div");
      list.className = "artifact-list";
      for (const artifact of visibleArtifacts) {
        const item = document.createElement("div");
        item.className = "artifact-item";

        const info = document.createElement("div");
        info.className = "artifact-info";
        const name = document.createElement("div");
        name.className = "artifact-name";
        name.textContent = cleanUiText(artifact.name || artifact.filename || "飞行器设计结果包");
        const meta = document.createElement("div");
        meta.className = "artifact-meta";
        const bits = [];
        if (artifact.file_count != null) bits.push("产物 " + formatCount(artifact.file_count));
        if (artifact.size_bytes != null) bits.push(formatBytes(artifact.size_bytes));
        if (artifact.source_dir) bits.push("来源 " + artifact.source_dir);
        meta.textContent = bits.join(" · ") || "可下载的技能生成结果";
        info.appendChild(name);
        info.appendChild(meta);

        const link = document.createElement("a");
        link.className = "artifact-download";
        link.href = artifact.download_url;
        link.download = artifact.filename || "";
        link.textContent = "下载结果包";

        item.appendChild(info);
        item.appendChild(link);
        list.appendChild(item);
      }
      panel.appendChild(list);
      return panel;
    }

    function createEventList(events) {
      const eventList = document.createElement("div");
      eventList.className = "event-list";

      for (let index = 0; index < events.length; index += 1) {
        const event = events[index];
        const item = document.createElement("div");
        item.className = "event" + (event.is_error ? " is-error" : "");

        const meta = document.createElement("div");
        meta.className = "event-meta";
        const icon = document.createElement("span");
        icon.className = "event-icon";
        icon.textContent = eventIcon(event);
        const label = document.createElement("span");
        label.className = "event-label";
        label.textContent = eventStatusLabel(event, index, events);
        meta.appendChild(icon);
        meta.appendChild(label);
        item.appendChild(meta);

        const body = document.createElement("div");
        body.className = "event-body";
        body.textContent = eventNarrative(event, index, events);
        item.appendChild(body);

        const summary = eventSummary(event);
        if (summary && summary !== body.textContent) {
          const subtext = document.createElement("div");
          subtext.className = "event-subtext";
          subtext.textContent = summary;
          item.appendChild(subtext);
        }

        if (event.rag) {
          item.appendChild(createEvidencePanel(event.rag));
        }

        const preview = extractPreviewText(event);
        if (preview) {
          const pre = document.createElement("div");
          pre.className = "event-preview";
          pre.textContent = preview;
          item.appendChild(pre);
        }

        eventList.appendChild(item);
      }

      return eventList;
    }

    function updateProcessPanel(wrapper, events = [], options = {}) {
      let details = wrapper.querySelector(":scope > details.process-panel");
      const bubble = wrapper.querySelector(":scope > .bubble");
      if (!details) {
        details = document.createElement("details");
        details.className = "process-panel";
        if (bubble) wrapper.insertBefore(details, bubble);
        else wrapper.appendChild(details);
      }
      details.classList.toggle("is-running", Boolean(options.isRunning));
      details.classList.toggle("is-error", Boolean(options.isError));
      details.open = true;

      details.innerHTML = "";
      const summary = document.createElement("summary");
      const text = document.createElement("span");
      text.className = "process-summary";
      text.textContent = summarizeProcess(events, options);
      const chevron = document.createElement("span");
      chevron.className = "process-chevron";
      chevron.textContent = ">";
      summary.appendChild(text);
      summary.appendChild(chevron);
      details.appendChild(summary);

      const body = document.createElement("div");
      body.className = "process-body";
      if (events.length) {
        body.appendChild(createEventList(events));
      } else {
        const empty = document.createElement("div");
        empty.className = "process-empty";
        empty.textContent = options.isRunning ? "正在等待模型输出和工具活动。" : "本轮没有调用工具或资料检索。";
        body.appendChild(empty);
      }
      details.appendChild(body);
      return details;
    }

    function requirementStatusMeta(status) {
      const statuses = {
        needs_clarification: ["待澄清", "warn"],
        unsupported: ["模型未覆盖", "blocked"],
        contradictory_requirements: ["需求冲突", "blocked"],
        infeasible: ["当前不可行", "blocked"],
        repairable: ["可协商修正", "warn"],
        ready_for_solver: ["可进入求解", "pass"],
        conceptually_feasible: ["概念可行", "pass"],
        preliminary_feasible: ["初步可行", "pass"],
        robust_preliminary_feasible: ["稳健初步可行", "pass"],
      };
      const normalized = String(status || "needs_clarification");
      const [label, tone] = statuses[normalized] || ["状态待确认", "neutral"];
      return { label, tone };
    }

    const REQUIREMENT_FIELD_LABELS = Object.freeze({
      "weights.max_mtow_kg": "最大起飞重量上限",
      "requirements.range_m": "任务航程",
      "requirements.payload_kg": "任务载荷",
      "requirements.cruise_mach": "巡航马赫数",
      "requirements.cruise_altitude_m": "巡航高度",
      "requirements.takeoff_distance_m": "起飞距离",
      "requirements.landing_distance_m": "着陆距离",
      "requirements.max_load_factor": "最大过载",
      "requirements.sustained_turn_g": "持续盘旋过载",
      "requirements.service_ceiling_m": "实用升限",
      "requirements.aircraft_role": "飞行器任务类型",
      "requirements.propulsion_type": "推进类型",
      "requirements.reserve_fraction": "储备燃油比例",
      "requirements.tail_layout": "尾翼布局",
      "requirements.cl_max_takeoff": "起飞最大升力系数",
      "requirements.cl_max_landing": "着陆最大升力系数",
      "requirements.assumed_climb_rate_m_s": "假定爬升率",
      "requirements.uncertainty_enabled": "不确定性分析",
      "performance.min_cruise_endurance_s": "最低巡航航时",
      "performance.max_flight_mach": "最大飞行马赫数",
      "geometry.max_aspect_ratio": "最大展弦比",
      "launch.mode": "发射方式",
      "launch.field_altitude_m": "发射场海拔",
      "launch.booster_end_mach": "助推结束马赫数",
      "launch.booster_end_relative_altitude_m": "助推结束相对高度",
      "recovery.mode": "回收方式",
      "recovery.parachute_open_mach": "开伞马赫数",
      "recovery.parachute_open_relative_altitude_m": "开伞相对高度",
      "propulsion.engine_count": "发动机数量",
      "configuration.reference": "参考构型",
      "configuration.stealth_requirement": "隐身要求",
      "initial_guess.mtow_kg": "最大起飞重量初值",
      "initial_guess.wing_loading_pa": "翼载初值",
      "initial_guess.thrust_to_weight": "推重比初值",
      "initial_guess.aspect_ratio": "展弦比初值",
      "initial_guess.sweep_deg": "后掠角初值",
      "initial_guess.taper_ratio": "梯形比初值",
      "initial_guess.thickness_ratio": "厚度比初值",
      "initial_guess.sfc_cruise_1_s": "巡航等效耗油率",
      "initial_guess.jet_tsfc_kg_per_n_s": "喷气发动机推力比油耗",
      "initial_guess.prop_bsfc_kg_per_j": "螺旋桨发动机功率比油耗",
      "initial_guess.prop_efficiency": "螺旋桨效率",
      "initial_guess.cd0": "零升阻力系数",
      "initial_guess.oswald_e": "奥斯瓦尔德效率因子",
      "initial_guess.cg_fraction_cbar": "重心位置",
      "initial_guess.horizontal_tail_volume_coefficient": "平尾容积系数",
      "solver.tolerance": "收敛容差",
      "solver.max_iterations": "最大迭代次数",
      "solver.auto_repair_enabled": "自动修正",
      "solver.max_repair_attempts": "最大修正轮次",
      "project_name": "项目名称",
      "initial_guess": "初始设计参数",
    });

    const REQUIREMENT_PATH_ALIASES = Object.freeze({
      "mission.range_m": "requirements.range_m",
      "mission.payload_kg": "requirements.payload_kg",
      "mission.cruise_mach": "requirements.cruise_mach",
      "mission.cruise_altitude_m": "requirements.cruise_altitude_m",
      "mission.max_flight_mach": "performance.max_flight_mach",
      "propulsion.propulsion_type": "requirements.propulsion_type",
      "mass.maximum_takeoff_mass": "weights.max_mtow_kg",
      "configuration.reference_style": "configuration.reference",
    });

    const REQUIREMENT_UNITS_BY_PATH = Object.freeze({
      "requirements.assumed_climb_rate_m_s": "m/s",
      "requirements.max_load_factor": "g",
      "requirements.sustained_turn_g": "g",
      "requirements.reserve_fraction": "无量纲",
      "requirements.cl_max_takeoff": "无量纲",
      "requirements.cl_max_landing": "无量纲",
      "initial_guess.thrust_to_weight": "无量纲",
      "initial_guess.aspect_ratio": "无量纲",
      "initial_guess.sweep_deg": "度",
      "initial_guess.taper_ratio": "无量纲",
      "initial_guess.thickness_ratio": "无量纲",
      "initial_guess.sfc_cruise_1_s": "1/s",
      "initial_guess.jet_tsfc_kg_per_n_s": "kg/(N·s)",
      "initial_guess.prop_bsfc_kg_per_j": "kg/J",
      "initial_guess.prop_efficiency": "无量纲",
      "initial_guess.cd0": "无量纲",
      "initial_guess.oswald_e": "无量纲",
      "initial_guess.cg_fraction_cbar": "平均气动弦长比例",
      "initial_guess.horizontal_tail_volume_coefficient": "无量纲",
      "solver.tolerance": "无量纲",
    });

    const REQUIREMENT_VALUE_LABELS = Object.freeze({
      jet: "喷气推进",
      prop: "螺旋桨推进",
      uav: "无人机",
      fighter: "战斗机",
      transport: "运输机",
      general_aviation: "通用航空飞机",
      rocket_assist: "火箭助推",
      parachute: "伞降回收",
      conventional: "常规尾翼",
      t_tail: "T 形尾翼",
      v_tail: "V 形尾翼",
      twin_fin: "双垂尾",
      provide_project_specific_high_lift_data: "提供项目专用增升数据",
      accept_preliminary_clmax_assumption: "采用初步最大升力系数假设",
      relax_field_length_requirement: "放宽场长要求",
      out_of_scope: "移出本轮求解范围",
    });

    const REQUIREMENT_ACTION_LABELS = Object.freeze({
      answer_question: "提交确认信息",
      apply_change: "应用参数修改",
      defer_unsupported: "保留专项需求，先求解已覆盖范围",
      confirm_revision: "确认需求版本",
      submit_solver: "开始总体设计求解",
    });

    const REQUIREMENT_COVERAGE_REASONS = Object.freeze({
      "weights.max_mtow_kg": "将在重量闭合后复核，目前不是直接优化约束。",
      "requirements.range_m": "已接入任务航程与燃油闭合模型。",
      "requirements.payload_kg": "已接入重量与任务闭合模型。",
      "requirements.cruise_mach": "已接入亚声速巡航气动与推进评估。",
      "requirements.cruise_altitude_m": "已接入巡航大气、阻力、推力与任务评估。",
      "requirements.takeoff_distance_m": "已接入预测起飞距离的硬约束校核。",
      "requirements.landing_distance_m": "已接入预测着陆距离的硬约束校核。",
      "requirements.service_ceiling_m": "已接入实用升限推力约束。",
      "requirements.propulsion_type": "已接入喷气与螺旋桨两类通用推进分支。",
      "performance.min_cruise_endurance_s": "当前模型未独立预测燃油受限的最大巡航航时。",
      "performance.max_flight_mach": "当前模型未接入最大速度、跨声速阻力增量、推进极限和颤振联合验证。",
      "geometry.max_aspect_ratio": "将在几何闭合后复核，并由有界修正过程遵守该上限。",
      "launch.mode": "当前模型未接入发射轨迹及其与飞行器载荷的接口校核。",
      "launch.field_altitude_m": "当前模型尚未把发射场大气条件耦合到发射轨迹。",
      "launch.booster_end_mach": "当前模型未接入火箭助推分离轨迹校核。",
      "launch.booster_end_relative_altitude_m": "当前模型未接入火箭助推分离高度校核。",
      "recovery.mode": "当前模型未接入回收系统展开过程与载荷校核。",
      "recovery.parachute_open_mach": "当前模型未接入开伞包线与开伞冲击校核。",
      "recovery.parachute_open_relative_altitude_m": "当前模型未接入伞降过程与高度裕度校核。",
      "propulsion.engine_count": "当前模型可完成通用推力设计，但尚未验证发动机数量与安装方案。",
      "configuration.reference": "参考构型尚未转换为经过验证的几何约束。",
      "configuration.stealth_requirement": "当前模型未接入雷达散射截面、进排气遮蔽、材料和特征控制验证。",
    });

    const REQUIREMENT_QUESTION_COPY = Object.freeze({
      "mission.range.required": {
        question: "请确认总体设计需要闭合的任务航程。",
        reason: "当前确定性求解需要正的任务航程；系统不会把巡航航时静默换算成任务航程。",
        consequence: "未确认任务航程前，不能启动总体参数求解。",
      },
      "mission.payload.required": {
        question: "请确认任务载荷质量。",
        reason: "任务载荷是重量闭合的必要输入，且必须为非负数。",
        consequence: "未确认任务载荷前，不能启动总体参数求解。",
      },
      "propulsion.type.high_speed": {
        question: "请确认高速巡航需求采用哪种推进类型。",
        reason: "推进类型会显著改变耗油率、推力衰减和安装假设。",
        consequence: "该选择影响较大，系统不会静默采用任务类型默认值。",
      },
      "performance.service_ceiling.high_cruise": {
        question: "请确认高空巡航任务采用的实用升限。",
        reason: "默认实用升限低于当前巡航高度，不能直接作为未确认假设。",
        consequence: "实用升限未确认前，系统无法完成求解输入闭合。",
      },
      "field_length.takeoff.assumption": {
        question: "请确认如何建立起飞阶段的增升能力假设。",
        reason: "小于 100 米的起飞距离对最大升力系数、越障和场地条件高度敏感。",
        consequence: "未确认前，不能把该起飞距离作为稳健的初步设计约束。",
      },
      "field_length.landing.assumption": {
        question: "请确认如何建立着陆阶段的增升能力假设。",
        reason: "小于 100 米的着陆距离对最大升力系数、越障和场地条件高度敏感。",
        consequence: "未确认前，不能把该着陆距离作为稳健的初步设计约束。",
      },
    });

    const REQUIREMENT_PROPOSAL_COPY = Object.freeze({
      "ceiling.raise_service_ceiling": ["提高实用升限，使其不低于巡航高度并保留初步裕度。", "恢复巡航高度与实用升限的合理顺序。", "可能增加爬升能力、推进系统或机翼面积需求。"],
      "ceiling.lower_cruise_altitude": ["降低巡航高度，使其低于已声明的实用升限。", "在不提高升限要求的情况下消除高度冲突。", "会改变大气、阻力、航程和隐身假设。"],
      "mach.raise_maximum_mach": ["提高最大飞行马赫数，使其高于巡航马赫数。", "恢复必要的速度裕度。", "可能需要不同的推进方案和跨声速气动弹性验证。"],
      "mach.lower_cruise_mach": ["降低巡航马赫数，使其低于最大飞行马赫数。", "消除巡航与最大速度之间的直接冲突。", "会增加任务时间，并改变航程与燃油设计。"],
      "mass.increase_mtow_allowance": ["当前任务载荷占最大起飞重量的比例过高，建议放宽重量上限。", "为结构、推进、系统和燃油恢复初步重量空间。", "会增加飞行器尺寸、发射需求、成本和潜在特征。"],
      "mass.reduce_payload": ["当前任务载荷占最大起飞重量的比例过高，建议降低载荷。", "降低重量闭合的主要压力。", "会降低任务载荷能力。"],
      "geometry.reduce_aspect_ratio": ["将设计展弦比降到声明的上限以内。", "使几何输入满足展弦比上限。", "通常会增加诱导阻力或机翼面积需求。"],
      "geometry.relax_aspect_ratio_limit": ["放宽展弦比上限以包含当前几何方案。", "保留当前气动几何输入。", "会增加翼展，并可能与包装或发射约束冲突。"],
      "mission.restore_preliminary_reserve": ["长航程任务应保留默认的初步性能储备。", "降低大气、航路和模型不确定性的影响。", "会增加燃油需求或降低载荷航程能力。"],
    });

    function containsChineseText(value) {
      return /[\u3400-\u9fff]/.test(String(value || ""));
    }

    function requirementPathKey(path) {
      const raw = String(path || "");
      const active = raw.startsWith("deferred.") ? raw.slice("deferred.".length) : raw;
      return REQUIREMENT_PATH_ALIASES[active] || active;
    }

    function requirementFieldLabel(path) {
      const raw = String(path || "");
      const prefix = raw.startsWith("deferred.") ? "保留目标：" : "";
      const key = requirementPathKey(raw);
      return prefix + (REQUIREMENT_FIELD_LABELS[key] || "其他工程参数");
    }

    function requirementModelLabel(model) {
      return ({
        aircraft_class_i_ii_v2: "总体设计 I/II 级模型",
        class1: "一级总体设计模型",
        class2: "二级初步设计模型",
      })[model] || (model ? "专项工程模型" : "");
    }

    function requirementUnitLabel(unit, path) {
      const fieldUnit = REQUIREMENT_UNITS_BY_PATH[requirementPathKey(path)];
      if (fieldUnit) return fieldUnit;
      const leaf = requirementPathKey(path).split(".").pop() || "";
      const inferredUnit = unit
        || (leaf.endsWith("_kg") ? "kg" : "")
        || (leaf.endsWith("_m") ? "m" : "")
        || (leaf.endsWith("_s") ? "s" : "")
        || (leaf.endsWith("_pa") ? "Pa" : "")
        || (leaf.includes("mach") ? "Mach" : "")
        || (leaf === "engine_count" ? "count" : "");
      return ({ Mach: "马赫", m: "米", s: "秒", count: "个", ratio: "比值", deg: "度" })[inferredUnit]
        || inferredUnit
        || "--";
    }

    function requirementValueLabel(value) {
      return typeof value === "string" ? (REQUIREMENT_VALUE_LABELS[value] || value) : value;
    }

    function localizeCoverageReason(path, reason = "") {
      if (containsChineseText(reason)) return reason;
      const localized = REQUIREMENT_COVERAGE_REASONS[requirementPathKey(path)];
      if (localized) return localized;
      return reason ? "当前总体模型已记录该字段的覆盖状态，详细证据保留在工程审计中。" : "";
    }

    function localizedRequirementQuestion(question) {
      const questionId = String(question?.question_id || "");
      const known = REQUIREMENT_QUESTION_COPY[questionId];
      if (known) return known;
      const fieldLabel = requirementFieldLabel(question?.field_path);
      if (questionId.startsWith("solver_completion.")) {
        return {
          question: `请确认${fieldLabel}的有效求解值。`,
          reason: "当前需求已通过上层检查，但该字段仍不满足确定性求解器的输入契约。",
          consequence: "未确认前，不能补齐默认值或确认需求版本。",
        };
      }
      if (questionId.startsWith("solver_outcome.")) {
        return {
          question: `请确认下一轮需要评估的${fieldLabel}。`,
          reason: "上一次求解提供了相关诊断证据，但没有可安全自动采用的新值。",
          consequence: "未确认前，当前失败仍只作为诊断记录，不能授权新一轮求解。",
        };
      }
      return {
        question: `请确认${fieldLabel}。`,
        reason: containsChineseText(question?.reason) ? question.reason : "该参数会直接影响总体设计求解和工程判定。",
        consequence: containsChineseText(question?.consequence_if_unanswered)
          ? question.consequence_if_unanswered
          : "未确认前不能进入下一步求解。",
      };
    }

    function localizedRequirementSummary(diagnosis) {
      if (containsChineseText(diagnosis?.summary)) return diagnosis.summary;
      return ({
        unsupported: "存在当前总体模型尚未覆盖的强制要求。这表示模型覆盖不足，并不代表已经判定方案在物理上不可行。",
        needs_clarification: "部分关键输入需要确认，完成确认后才能进入确定性总体参数求解。",
        contradictory_requirements: "需求中存在明确的跨字段冲突。系统尚未修改任何要求，请确认下方修正方案。",
        repairable: "当前需求可通过明确的参数修改继续推进；用户输入和锁定值在确认前保持不变。",
        ready_for_solver: "必要输入已补齐，跨字段检查通过，当前版本可以由用户确认后进入求解。工程可行性仍需以完整求解结果为准。",
      })[diagnosis?.status] || "当前需求已完成总体设计求解前诊断。";
    }

    function localizedRequirementBlocker(reason) {
      if (containsChineseText(reason)) return reason;
      const unsupported = String(reason || "").match(/^No applicable model for ([^:]+):/);
      if (unsupported) {
        const path = unsupported[1];
        return `${requirementFieldLabel(path)}：${localizeCoverageReason(path, reason)}`;
      }
      const exact = {
        "The locked service ceiling is below the locked cruise altitude.": "已锁定的实用升限低于已锁定的巡航高度。",
        "The locked maximum Mach number is below locked cruise Mach.": "已锁定的最大飞行马赫数低于已锁定的巡航马赫数。",
        "The locked payload equals or exceeds the locked maximum takeoff mass.": "已锁定的任务载荷等于或超过最大起飞重量上限。",
        "The locked aspect ratio exceeds the locked upper bound.": "已锁定的展弦比超过已锁定的上限。",
        "One or more high-impact inputs must be clarified before deterministic sizing.": "确定性总体参数求解前，必须确认一项或多项高影响输入。",
        "The current revision has a deterministic repair proposal that has not been applied.": "当前版本包含尚未确认应用的确定性修正建议。",
        "One or more user-requested field changes have not yet been confirmed.": "一项或多项用户提出的字段修改尚未确认。",
      };
      return exact[String(reason || "")] || "当前需求仍有一项必须处理的工程阻断条件。";
    }

    function localizedProposalCopy(proposal, index) {
      const known = REQUIREMENT_PROPOSAL_COPY[proposal?.proposal_id];
      if (known) return known[index] || "";
      const values = [proposal?.reason, proposal?.expected_benefit, proposal?.engineering_cost];
      if (containsChineseText(values[index])) return values[index];
      return [
        "该建议用于消除当前需求或设计变量中的工程冲突。",
        "采用后将通过完整重算评估对总体方案的影响。",
        "可能改变重量、几何、推进、性能或验证裕度。",
      ][index];
    }

    function localizedRequirementError(message) {
      const text = String(message || "");
      if (containsChineseText(text)) return text;
      if (/stale|does not match|not current|conflict|expected_revision_hash/i.test(text)) {
        return "需求版本已更新，请在最新的需求卡片上重新操作。";
      }
      if (/requires.*confirmation|user confirmation|explicitly confirmed/i.test(text)) {
        return "本步骤需要明确确认后才能继续。";
      }
      if (/not ready|ready for solver|can_submit/i.test(text)) {
        return "当前需求版本尚未达到可求解状态，请先处理卡片中的待确认项。";
      }
      if (/clarification|answer|question/i.test(text)) {
        return "请先完整填写当前需求卡片中的确认信息，再提交本步骤。";
      }
      if (/proposal/i.test(text)) {
        return "请选择当前版本中可用的参数修改建议。";
      }
      if (/unsupported|scope|defer/i.test(text)) {
        return "当前专项需求范围尚未满足该操作的前置条件。";
      }
      return "需求操作未完成，请检查当前版本中的确认项后重试。";
    }

    function requirementRoleLabel(role) {
      return ({
        hard_constraint: "硬约束",
        soft_goal: "软目标",
        design_variable: "设计变量",
        technology_assumption: "技术假设",
      })[role] || "未分类";
    }

    function requirementSourceLabel(source) {
      return ({
        user: "用户",
        derived: "推导",
        default: "默认",
        reference: "参考",
      })[source] || "未声明";
    }

    function requirementCoverageMeta(record, requirement) {
      const status = record?.status || (requirement?.applicable_model ? "covered" : "unknown");
      const labels = {
        covered: ["已覆盖", "pass"],
        partial: ["部分覆盖", "warn"],
        unsupported: ["未覆盖", "blocked"],
        unknown: ["未声明", "neutral"],
      };
      const [label, tone] = labels[status] || ["状态未知", "neutral"];
      return {
        label,
        tone,
        model: requirementModelLabel(record?.model_id || requirement?.applicable_model || ""),
        reason: localizeCoverageReason(record?.field_path || requirement?.path, record?.reason || ""),
      };
    }

    function formatRequirementValue(value) {
      if (value == null || value === "") return "--";
      if (typeof value === "boolean") return value ? "是" : "否";
      if (typeof value === "number") return Number.isInteger(value) ? String(value) : String(Number(value.toPrecision(8)));
      if (typeof value === "string") return requirementValueLabel(value);
      try { return JSON.stringify(value); } catch (_err) { return String(value); }
    }

    function requirementOptionLabel(option) {
      if (option && typeof option === "object" && !Array.isArray(option)) {
        return formatRequirementValue(option.label ?? option.value ?? option.id ?? option);
      }
      return formatRequirementValue(option);
    }

    function requirementActionId() {
      if (globalThis.crypto && typeof globalThis.crypto.randomUUID === "function") {
        return globalThis.crypto.randomUUID();
      }
      return "requirement-" + Date.now().toString(36) + "-" + Math.random().toString(36).slice(2, 12);
    }

    function collectRequirementDecisions(panel) {
      const answers = [];
      for (const input of panel.querySelectorAll("input[data-requirement-question]")) {
        const isChoice = input.type === "radio" || input.type === "checkbox";
        if (isChoice && !input.checked) continue;
        if (!isChoice && !input.value.trim()) continue;
        let value = input.value.trim();
        if (isChoice) {
          value = input.dataset.optionValue ?? input.value;
          try { value = JSON.parse(value); } catch (_err) { /* Keep the choice label unchanged. */ }
        } else if (input.type === "number" && Number.isFinite(Number(input.value))) {
          value = Number(input.value);
        }
        answers.push({
          question_id: input.dataset.requirementQuestion,
          field_path: input.dataset.fieldPath || "",
          value,
        });
      }
      return answers.length ? { clarification_answers: answers } : {};
    }

    function setRequirementControlsPending(panel, isPending, activeButton = null) {
      for (const control of panel.querySelectorAll("button, input")) {
        if (isPending) {
          control.dataset.requirementWasDisabled = control.disabled ? "true" : "false";
          control.disabled = true;
        } else if (control.dataset.requirementWasDisabled === "false") {
          control.disabled = false;
        }
        if (!isPending) delete control.dataset.requirementWasDisabled;
      }
      if (activeButton) {
        if (isPending) {
          activeButton.dataset.requirementLabel = activeButton.textContent;
          activeButton.textContent = "提交中...";
        } else if (activeButton.dataset.requirementLabel) {
          activeButton.textContent = activeButton.dataset.requirementLabel;
          delete activeButton.dataset.requirementLabel;
        }
      }
      panel.setAttribute("aria-busy", isPending ? "true" : "false");
    }

    function markHistoricalRequirementCards(currentRevisionId = "") {
      const cards = Array.from(chatLog.querySelectorAll(".requirement-interaction"));
      const effectiveCurrentId = currentRevisionId || cards.at(-1)?.dataset.revisionId || "";
      let currentCard = cards.at(-1) || null;
      if (effectiveCurrentId) {
        for (let index = cards.length - 1; index >= 0; index -= 1) {
          if (cards[index].dataset.revisionId === effectiveCurrentId) {
            currentCard = cards[index];
            break;
          }
        }
      }
      for (const card of cards) {
        const historical = card !== currentCard;
        card.classList.toggle("is-historical", historical);
        card.dataset.current = historical ? "false" : "true";
        const note = card.querySelector(".requirement-history-note");
        if (note) note.hidden = !historical;
        for (const control of card.querySelectorAll("button, input")) {
          if (historical) control.disabled = true;
        }
      }
    }

    async function refreshRequirementActionSession(sessionId) {
      try {
        const payload = await api("/api/sessions/" + encodeURIComponent(sessionId));
        if (!payload.session || state.sessionId !== sessionId) return;
        updateMeta(payload.session);
        if (state.view === "design") renderDesignWorkspace();
      } catch (_err) {
        // The monitored job remains available even if the session refresh is temporarily unavailable.
      }
    }

    function registerRequirementActionJob(job, sessionId) {
      if (!job?.job_id) return;
      state.designStreamController?.abort();
      state.designStreamController = null;
      if (state.designJobMessage) state.designJobMessage.remove();
      state.designJobMessage = null;
      state.designJobId = job.job_id;
      state.activeDesignJob = job;
      state.designJobDetails[job.job_id] = job;
      state.designJobs = [job, ...state.designJobs.filter((item) => item.job_id !== job.job_id)];
      state.designJobSequence = job.last_sequence || 0;
      state.designJobEvents = (job.events || []).map(designProgressEvent);
      state.renderedDesignJobId = null;
      state.selectedResultFile = null;
      designWorkspaceBtn.hidden = false;
      designWorkspaceBtn.disabled = state.busy;
      designWorkspaceBtn.setAttribute("aria-hidden", "false");
      saveLocalState();
      renderDesignWorkspace();

      if (job.terminal) {
        state.designJobRunning = false;
        if (state.view === "design") setDesignTab("results");
        void refreshRequirementActionSession(sessionId);
        return;
      }

      setDesignRunBusy(true, localizedJobMessage(job.message, job.status) || "总体设计任务已启动");
      refreshDesignJobMessage();
      void monitorDesignJob(job.job_id).finally(() => refreshRequirementActionSession(sessionId));
    }

    async function submitRequirementAction(panel, interaction, actionSpec, button) {
      if (panel.dataset.current === "false" || panel.getAttribute("aria-busy") === "true") return;
      const sessionId = String(interaction.session_id || state.sessionId || "");
      const revision = interaction.revision || {};
      const revisionId = String(revision.revision_id || "");
      const revisionHash = String(revision.revision_hash || "");
      const errorBox = panel.querySelector(".requirement-action-error");
      if (errorBox) {
        errorBox.hidden = true;
        errorBox.textContent = "";
      }
      if (!sessionId || !revisionId || !revisionHash) {
        if (errorBox) {
          errorBox.textContent = "此需求版本缺少会话或修订标识，无法提交操作。";
          errorBox.hidden = false;
        }
        return;
      }

      const actionPayload = actionSpec?.payload && typeof actionSpec.payload === "object"
        ? { ...actionSpec.payload }
        : {};
      const actionName = String(actionSpec?.action || "");
      const acceptsAnswers = actionName === "answer_question" || actionName === "answer_questions";
      const acceptsProposal = actionName === "apply_change" || actionName === "apply_change_proposal";
      const selectedProposal = acceptsProposal
        ? panel.querySelector("input[data-requirement-proposal]:checked")?.value || ""
        : "";
      const proposalId = acceptsProposal
        ? actionPayload.proposal_id || actionSpec.proposal_id || selectedProposal
        : "";
      const collectedDecisions = acceptsAnswers ? collectRequirementDecisions(panel) : {};
      const configuredDecisions = actionPayload.decisions;
      delete actionPayload.decisions;
      const decisions = configuredDecisions && typeof configuredDecisions === "object" && !Array.isArray(configuredDecisions)
        ? { ...configuredDecisions, ...collectedDecisions }
        : (Object.keys(collectedDecisions).length ? collectedDecisions : configuredDecisions);
      const request = {
        ...actionPayload,
        action: actionSpec.action,
        expected_revision_hash: revisionHash,
        client_action_id: requirementActionId(),
      };
      if (decisions != null && (typeof decisions !== "object" || Object.keys(decisions).length)) {
        request.decisions = decisions;
      }
      if (proposalId) request.proposal_id = proposalId;

      setRequirementControlsPending(panel, true, button);
      try {
        const response = await api(
          "/api/sessions/" + encodeURIComponent(sessionId)
            + "/requirement-revisions/" + encodeURIComponent(revisionId) + "/actions",
          { method: "POST", body: JSON.stringify(request) },
        );
        if (response.session) updateMeta(response.session);
        const responseMessages = response.session?.messages;
        if (Array.isArray(responseMessages)) {
          renderMessages(responseMessages);
        } else if (response.interaction) {
          const replacement = createRequirementInteraction(response.interaction, { isCurrent: true });
          panel.replaceWith(replacement);
        } else {
          setRequirementControlsPending(panel, false, button);
        }
        const responseRevisionId = requirementRevisionId(response.interaction)
          || latestRequirementRevisionId(responseMessages || []);
        if (responseRevisionId) markHistoricalRequirementCards(responseRevisionId);
        if (response.job) registerRequirementActionJob(response.job, sessionId);
        setStatus(response.job && !response.job.terminal
          ? "需求版本已确认，总体设计任务已启动。"
          : "需求版本操作已提交。" );
      } catch (error) {
        setRequirementControlsPending(panel, false, button);
        const localizedError = localizedRequirementError(error.message);
        if (errorBox) {
          errorBox.textContent = localizedError;
          errorBox.hidden = false;
        }
        setStatus(localizedError, true);
      }
    }

    function createRequirementInteraction(interaction, options = {}) {
      const diagnosis = interaction?.diagnosis || {};
      const intent = interaction?.intent || {};
      const revision = interaction?.revision || {};
      const revisionId = requirementRevisionId(interaction);
      const requirements = Array.isArray(intent.requirements) ? intent.requirements : [];
      const coverage = Array.isArray(diagnosis.coverage) ? diagnosis.coverage : [];
      const coverageByPath = new Map(coverage.map((item) => [item.field_path, item]));
      const questions = Array.isArray(diagnosis.clarification_questions)
        ? diagnosis.clarification_questions.slice(0, 3)
        : [];
      const proposals = Array.isArray(diagnosis.change_proposals) ? diagnosis.change_proposals : [];
      const actions = Array.isArray(interaction.actions) ? interaction.actions : [];
      const historical = options.isCurrent === false;

      const panel = document.createElement("section");
      panel.className = "requirement-interaction" + (historical ? " is-historical" : "");
      panel.dataset.revisionId = revisionId;
      panel.dataset.revisionHash = String(revision.revision_hash || "");
      panel.dataset.current = historical ? "false" : "true";
      panel.dataset.testid = "requirement-interaction";
      panel.setAttribute("aria-label", "飞行器需求诊断");

      const header = document.createElement("header");
      header.className = "requirement-header";
      const heading = document.createElement("div");
      heading.className = "requirement-heading";
      const title = document.createElement("strong");
      title.textContent = "需求诊断";
      const revisionLabel = document.createElement("span");
      const revisionBits = [];
      if (revision.revision_number != null) revisionBits.push("版本 " + revision.revision_number);
      if (revision.confirmed) revisionBits.push("已确认");
      revisionLabel.textContent = revisionBits.join(" · ") || "待建立版本";
      heading.appendChild(title);
      heading.appendChild(revisionLabel);
      const statusMeta = requirementStatusMeta(diagnosis.status || revision.status);
      const status = document.createElement("span");
      status.className = "requirement-status is-" + statusMeta.tone;
      status.dataset.status = String(diagnosis.status || revision.status || "");
      status.textContent = statusMeta.label;
      if (statusMeta.tone === "blocked") status.setAttribute("role", "status");
      header.appendChild(heading);
      header.appendChild(status);
      panel.appendChild(header);

      if (diagnosis.summary) {
        const summary = document.createElement("p");
        summary.className = "requirement-summary";
        summary.textContent = localizedRequirementSummary(diagnosis);
        panel.appendChild(summary);
      }

      const blockingReasons = Array.from(new Set(
        (Array.isArray(diagnosis.blocking_reasons) ? diagnosis.blocking_reasons : [])
          .map(localizedRequirementBlocker),
      ));
      if (blockingReasons.length) {
        const blockers = document.createElement("div");
        blockers.className = "requirement-blockers";
        const blockersTitle = document.createElement("strong");
        blockersTitle.textContent = "阻断原因";
        blockers.appendChild(blockersTitle);
        const list = document.createElement("ul");
        for (const reason of blockingReasons) {
          const item = document.createElement("li");
          item.textContent = reason;
          list.appendChild(item);
        }
        blockers.appendChild(list);
        panel.appendChild(blockers);
      }

      if (requirements.length) {
        const fields = document.createElement("div");
        fields.className = "requirement-section";
        const fieldsTitle = document.createElement("div");
        fieldsTitle.className = "requirement-section-title";
        fieldsTitle.textContent = "需求字段（" + requirements.length + "）";
        fields.appendChild(fieldsTitle);
        const tableWrap = document.createElement("div");
        tableWrap.className = "requirement-table-wrap";
        const table = document.createElement("table");
        table.className = "requirement-table";
        const thead = document.createElement("thead");
        const headingRow = document.createElement("tr");
        for (const label of ["字段", "值", "单位", "类型", "锁定", "来源", "模型支持"]) {
          const cell = document.createElement("th");
          cell.scope = "col";
          cell.textContent = label;
          headingRow.appendChild(cell);
        }
        thead.appendChild(headingRow);
        table.appendChild(thead);
        const tbody = document.createElement("tbody");
        for (const requirement of requirements) {
          const row = document.createElement("tr");
          row.dataset.fieldPath = requirement.path || "";
          const values = [
            requirementFieldLabel(requirement.path),
            formatRequirementValue(requirement.value),
            requirementUnitLabel(requirement.unit, requirement.path),
            requirementRoleLabel(requirement.role),
          ];
          for (const value of values) {
            const cell = document.createElement("td");
            cell.textContent = value;
            row.appendChild(cell);
          }
          const lockCell = document.createElement("td");
          const lock = document.createElement("span");
          lock.className = "requirement-lock" + (requirement.locked ? " is-locked" : "");
          lock.textContent = requirement.locked ? "已锁定" : "可调整";
          lockCell.appendChild(lock);
          row.appendChild(lockCell);
          const sourceCell = document.createElement("td");
          sourceCell.textContent = requirementSourceLabel(requirement.source);
          row.appendChild(sourceCell);
          const coverageCell = document.createElement("td");
          const coverageMeta = requirementCoverageMeta(coverageByPath.get(requirement.path), requirement);
          const coverageStatus = document.createElement("span");
          coverageStatus.className = "requirement-coverage is-" + coverageMeta.tone;
          coverageStatus.textContent = coverageMeta.label;
          coverageStatus.title = coverageMeta.reason;
          coverageCell.appendChild(coverageStatus);
          if (coverageMeta.model) {
            const model = document.createElement("small");
            model.textContent = coverageMeta.model;
            coverageCell.appendChild(model);
          }
          row.appendChild(coverageCell);
          tbody.appendChild(row);
        }
        table.appendChild(tbody);
        tableWrap.appendChild(table);
        fields.appendChild(tableWrap);
        panel.appendChild(fields);
      }

      if (questions.length) {
        const questionSection = document.createElement("div");
        questionSection.className = "requirement-section";
        const questionTitle = document.createElement("div");
        questionTitle.className = "requirement-section-title";
        questionTitle.textContent = "需要确认（最多 3 项）";
        questionSection.appendChild(questionTitle);
        questions.forEach((question, questionIndex) => {
          const localizedQuestion = localizedRequirementQuestion(question);
          const fieldset = document.createElement("fieldset");
          fieldset.className = "requirement-question";
          const legend = document.createElement("legend");
          legend.textContent = (questionIndex + 1) + ". " + localizedQuestion.question;
          fieldset.appendChild(legend);
          const meta = document.createElement("div");
          meta.className = "requirement-question-meta";
          const questionUnit = requirementUnitLabel(question.unit, question.field_path);
          meta.textContent = [
            requirementFieldLabel(question.field_path),
            questionUnit === "--" ? "" : "单位：" + questionUnit,
            localizedQuestion.reason,
          ].filter(Boolean).join(" · ");
          fieldset.appendChild(meta);
          const questionOptions = Array.isArray(question.options) ? question.options : [];
          if (questionOptions.length) {
            const optionList = document.createElement("div");
            optionList.className = "requirement-options";
            questionOptions.forEach((option, optionIndex) => {
              const optionLabel = document.createElement("label");
              optionLabel.className = "requirement-option";
              const input = document.createElement("input");
              input.type = "radio";
              input.name = "requirement-question-" + revisionId + "-" + questionIndex;
              input.dataset.requirementQuestion = question.question_id || String(questionIndex);
              input.dataset.fieldPath = question.field_path || "";
              input.dataset.optionValue = JSON.stringify(option);
              input.checked = JSON.stringify(option) === JSON.stringify(question.recommended_option);
              input.disabled = historical;
              const optionText = document.createElement("span");
              optionText.textContent = requirementOptionLabel(option)
                + (input.checked ? "（推荐）" : "");
              optionLabel.appendChild(input);
              optionLabel.appendChild(optionText);
              optionList.appendChild(optionLabel);
            });
            fieldset.appendChild(optionList);
          } else {
            const input = document.createElement("input");
            const questionPath = String(question.field_path || "");
            const numeric = typeof question.recommended_option === "number"
              || /(?:_kg|_m|_s|_pa|mach)$/.test(questionPath.toLowerCase());
            input.type = numeric ? "number" : "text";
            input.className = "requirement-question-input";
            input.dataset.requirementQuestion = question.question_id || String(questionIndex);
            input.dataset.fieldPath = question.field_path || "";
            input.placeholder = numeric
              ? "请输入数值" + (questionUnit === "--" ? "" : `（${questionUnit}）`)
              : "请输入回答";
            if (numeric) input.step = "any";
            if (question.recommended_option != null) input.value = formatRequirementValue(question.recommended_option);
            input.disabled = historical;
            fieldset.appendChild(input);
          }
          if (localizedQuestion.consequence) {
            const consequence = document.createElement("div");
            consequence.className = "requirement-question-consequence";
            consequence.textContent = "未确认影响：" + localizedQuestion.consequence;
            fieldset.appendChild(consequence);
          }
          questionSection.appendChild(fieldset);
        });
        panel.appendChild(questionSection);
      }

      if (proposals.length) {
        const proposalSection = document.createElement("div");
        proposalSection.className = "requirement-section";
        const proposalTitle = document.createElement("div");
        proposalTitle.className = "requirement-section-title";
        proposalTitle.textContent = "参数修改建议（" + proposals.length + "）";
        proposalSection.appendChild(proposalTitle);
        proposals.forEach((proposal, proposalIndex) => {
          const proposalRow = document.createElement("label");
          proposalRow.className = "requirement-proposal";
          const input = document.createElement("input");
          input.type = "radio";
          input.name = "requirement-proposal-" + revisionId;
          input.value = proposal.proposal_id || "";
          input.dataset.requirementProposal = proposal.proposal_id || "";
          input.checked = proposals.length === 1 && proposalIndex === 0;
          input.disabled = historical;
          const copy = document.createElement("span");
          copy.className = "requirement-proposal-copy";
          const change = document.createElement("strong");
          change.textContent = requirementFieldLabel(proposal.field_path) + "："
            + formatRequirementValue(proposal.old_value) + " → " + formatRequirementValue(proposal.proposed_value);
          const reason = document.createElement("span");
          reason.textContent = localizedProposalCopy(proposal, 0);
          copy.appendChild(change);
          copy.appendChild(reason);
          const details = [localizedProposalCopy(proposal, 1), localizedProposalCopy(proposal, 2)].filter(Boolean).join(" · ");
          if (details) {
            const detail = document.createElement("small");
            detail.textContent = details;
            copy.appendChild(detail);
          }
          if (proposal.target_locked) {
            const warning = document.createElement("em");
            warning.textContent = "涉及已锁定需求，须由用户确认";
            copy.appendChild(warning);
          }
          proposalRow.appendChild(input);
          proposalRow.appendChild(copy);
          proposalSection.appendChild(proposalRow);
        });
        panel.appendChild(proposalSection);
      }

      const footer = document.createElement("div");
      footer.className = "requirement-actions";
      const actionGroup = document.createElement("div");
      actionGroup.className = "requirement-action-group";
      for (const action of actions) {
        if (!action?.action) continue;
        const button = document.createElement("button");
        button.type = "button";
        button.className = "requirement-action" + (action.primary ? " is-primary" : "");
        button.textContent = action.label || REQUIREMENT_ACTION_LABELS[action.action] || "执行当前步骤";
        button.disabled = historical || action.enabled === false || !revisionId || !revision.revision_hash;
        if (action.enabled === false && action.reason) button.title = action.reason;
        button.addEventListener("click", () => submitRequirementAction(panel, interaction, action, button));
        actionGroup.appendChild(button);
      }
      footer.appendChild(actionGroup);
      const historyNote = document.createElement("span");
      historyNote.className = "requirement-history-note";
      historyNote.textContent = "历史需求版本，仅供查看";
      historyNote.hidden = !historical;
      footer.appendChild(historyNote);
      const error = document.createElement("div");
      error.className = "requirement-action-error";
      error.setAttribute("role", "alert");
      error.hidden = true;
      footer.appendChild(error);
      panel.appendChild(footer);

      return panel;
    }

    function designRangeMetricLabel(kind) {
      if (kind === "independent_capability_prediction") return "预测最大航程";
      if (kind === "evaluated_mission_distance") return "评估任务航程";
      return "航程指标（证据未声明）";
    }

    function createDesignResultPanel(job) {
      if (!job?.result) return null;
      const summary = job.result.summary || {};
      const panel = document.createElement("section");
      panel.className = "design-result-panel";

      const header = document.createElement("div");
      header.className = "design-result-header";
      const title = document.createElement("strong");
      title.textContent = job.request?.project_name || "总体设计结果";
      const outcome = designOutcome(job);
      const status = document.createElement("span");
      status.className = "design-result-state is-" + outcome.tone + (outcome.tone === "fail" ? " is-error" : "");
      status.textContent = outcome.label;
      status.setAttribute("role", outcome.tone === "fail" ? "alert" : "status");
      header.appendChild(title);
      header.appendChild(status);
      panel.appendChild(header);

      const metricData = [
        ["最大起飞重量", summary.mtow_kg, "kg", 1],
        ["机翼面积", summary.wing_area_m2, "m²", 2],
        ["翼载", summary.wing_loading_pa, "Pa", 0],
        ["推重比", summary.thrust_to_weight, "", 3],
        ["海平面推力", summary.thrust_sl_n, "N", 0],
        ["翼展", summary.span_m, "m", 2],
        [designRangeMetricLabel(summary.range_metric_kind), Number(summary.actual_range_m) / 1000, "km", 0],
        ["迭代次数", summary.iterations, "次", 0],
      ];
      const metrics = document.createElement("div");
      metrics.className = "design-result-metrics";
      for (const [labelText, rawValue, unit, digits] of metricData) {
        const metric = document.createElement("div");
        metric.className = "design-result-metric";
        const label = document.createElement("span");
        label.textContent = labelText;
        const value = document.createElement("strong");
        const numeric = Number(rawValue);
        value.textContent = Number.isFinite(numeric) ? numeric.toFixed(digits) + (unit ? " " + unit : "") : "--";
        metric.appendChild(label);
        metric.appendChild(value);
        metrics.appendChild(metric);
      }
      panel.appendChild(metrics);

      const mtow = Number(summary.mtow_kg);
      const weightParts = [
        ["空重", Number(summary.empty_weight_kg), "design-weight-empty"],
        ["燃油", Number(summary.fuel_weight_kg), "design-weight-fuel"],
        ["载荷", Number(summary.payload_kg), "design-weight-payload"],
      ];
      if (Number.isFinite(mtow) && mtow > 0 && weightParts.every((part) => Number.isFinite(part[1]))) {
        const accounted = weightParts.reduce((total, part) => total + Math.max(0, part[1]), 0);
        weightParts.push(["其他", Math.max(0, mtow - accounted), "design-weight-other"]);
        const weight = document.createElement("div");
        weight.className = "design-weight-summary";
        const weightTitle = document.createElement("span");
        weightTitle.textContent = "重量组成";
        const bar = document.createElement("div");
        bar.className = "design-weight-bar";
        const legend = document.createElement("div");
        legend.className = "design-weight-legend";
        for (const [name, value, className] of weightParts) {
          const segment = document.createElement("span");
          segment.className = className;
          segment.style.width = Math.max(0, value / mtow * 100).toFixed(2) + "%";
          segment.title = name + " " + value.toFixed(1) + " kg";
          bar.appendChild(segment);
          const item = document.createElement("span");
          item.textContent = name + " " + value.toFixed(1) + " kg";
          legend.appendChild(item);
        }
        weight.appendChild(weightTitle);
        weight.appendChild(bar);
        weight.appendChild(legend);
        panel.appendChild(weight);
      }

      const footer = document.createElement("div");
      footer.className = "design-result-footer";
      const footerItems = [
        "耗时 " + Number(job.result.duration_seconds || 0).toFixed(1) + " s",
        "自动修正 " + Number(summary.auto_repair_attempts || 0) + " 轮",
        "产物 " + (summary.artifact_count ?? job.result.artifacts?.length ?? 0),
        "校验问题 " + (summary.issue_count ?? job.result.issues?.length ?? 0),
        "任务 " + job.job_id,
      ];
      for (const text of footerItems) {
        const item = document.createElement("span");
        item.textContent = text;
        footer.appendChild(item);
      }
      panel.appendChild(footer);
      return panel;
    }

    function createMessage(role, text, options = {}) {
      const normalized = normalizeMessageOptions(options);
      const events = normalized.events || [];
      const requirementInteraction = role === "assistant" ? requirementInteractionFromEvents(events) : null;
      const artifacts = Array.isArray(normalized.artifacts) ? normalized.artifacts : [];
      const wrapper = document.createElement("article");
      wrapper.className = "message " + role;

      const label = document.createElement("div");
      label.className = "message-label";
      label.textContent = role === "user" ? "你" : role === "assistant" ? "工程助手" : "系统";
      wrapper.appendChild(label);

      const bubble = document.createElement("div");
      bubble.className = "bubble";
      const fallbackText = role === "assistant" && !normalized.isRunning && !requirementInteraction ? "[没有文本响应]" : "";
      renderMarkdownInto(bubble, text || fallbackText);
      bubble.hidden = Boolean(requirementInteraction && !text && !fallbackText);
      wrapper.appendChild(bubble);

      if (role === "assistant") {
        const processEvents = events.filter((event) => event?.kind !== "requirement_interaction");
        if (processEvents.length || normalized.isRunning || !requirementInteraction) {
          updateProcessPanel(wrapper, processEvents, {
            elapsedMs: normalized.elapsedMs,
            isRunning: Boolean(normalized.isRunning),
            isError: Boolean(normalized.isError),
            open: Boolean(normalized.openProcess && processEvents.length),
          });
        }
        if (requirementInteraction) {
          const currentRevisionId = normalized.currentRequirementRevisionId || requirementRevisionId(requirementInteraction);
          wrapper.appendChild(createRequirementInteraction(requirementInteraction, {
            isCurrent: !currentRevisionId || currentRevisionId === requirementRevisionId(requirementInteraction),
          }));
        }
        const answerEvidence = createAnswerEvidence(events);
        if (answerEvidence) wrapper.appendChild(answerEvidence);
        const designResult = createDesignResultPanel(normalized.designJob);
        if (designResult) wrapper.appendChild(designResult);
        const artifactsPanel = createArtifactsPanel(artifacts);
        if (artifactsPanel) wrapper.appendChild(artifactsPanel);
      }

      if (text) {
        const tools = document.createElement("div");
        tools.className = "message-tools";
        addCopyButton(tools, text);
        wrapper.appendChild(tools);
      }

      return wrapper;
    }

    function clearRenderedMessages() {
      chatLog.innerHTML = "";
    }

    function renderHero() {
      const hero = document.createElement("div");
      hero.className = "hero";
      const activeSkill = selectedSkillName();
      const selectedSkill = activeSkill ? skillDisplayName(activeSkill) : "未启用工程模式";
      const evidenceLabel = activeSkill
        ? (activeSkill === WEB_AIRCRAFT_SKILL ? "自动检索" : "按需检索")
        : "未启用";
      const toolLabel = autoApproveToggle.checked ? "自动批准" : "手动确认";
      hero.innerHTML =
        '<div class="hero-copy">' +
          "<strong>工程设计流程</strong>" +
          "<span>在右上角启用总体设计技能后，直接在对话中提交任务与约束；生成结果后，右上角会出现“设计结果”入口。</span>" +
        "</div>" +
        '<div class="hero-stack" aria-label="当前工作台状态">' +
          '<div class="hero-stat"><span>默认模型</span><strong>' + WEB_MODEL + "</strong></div>" +
          '<div class="hero-stat"><span>工程模式</span><strong>' + escapeHtml(selectedSkill) + "</strong></div>" +
          '<div class="hero-stat"><span>资料证据</span><strong>' + escapeHtml(evidenceLabel) + "</strong></div>" +
          '<div class="hero-stat"><span>工具确认</span><strong>' + escapeHtml(toolLabel) + "</strong></div>" +
        "</div>";
      chatLog.appendChild(hero);
    }

    function renderMessages(messages) {
      clearRenderedMessages();
      if (!messages.length) {
        renderHero();
        return;
      }

      const currentRequirementRevisionId = latestRequirementRevisionId(messages);
      for (const message of messages) {
        const hasRequirementInteraction = Boolean(requirementInteractionFromEvents(message.events || []));
        if (!message.text && !message.blocks?.length && !message.artifacts?.length && !hasRequirementInteraction) {
          continue;
        }
        let text = message.text || "";
        if (!text && message.blocks?.length) {
          text = message.blocks.map((block) => block.label).join("\n");
        }
        chatLog.appendChild(createMessage(message.role, text, {
          events: message.events || [],
          artifacts: message.artifacts || [],
          currentRequirementRevisionId,
        }));
      }
      markHistoricalRequirementCards(currentRequirementRevisionId);
      chatLog.scrollTop = chatLog.scrollHeight;
    }

    function refreshHeroIfEmpty() {
      if (chatLog.querySelector(".message")) return;
      renderMessages([]);
    }

    function appendAssistantReply(reply, options = {}) {
      const events = options.events || reply.events || [];
      const artifacts = options.artifacts || reply.artifacts || [];
      chatLog.appendChild(createMessage("assistant", reply.text, {
        events,
        artifacts,
        designJob: options.designJob,
        elapsedMs: options.elapsedMs,
        openProcess: Boolean(options.openProcess),
        currentRequirementRevisionId: options.currentRequirementRevisionId,
      }));
      const currentRequirementRevisionId = requirementRevisionId(requirementInteractionFromEvents(events));
      if (currentRequirementRevisionId) markHistoricalRequirementCards(currentRequirementRevisionId);
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
        const row = document.createElement("div");
        row.className = "session-row";
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

        const deleteButton = document.createElement("button");
        deleteButton.type = "button";
        deleteButton.className = "session-delete";
        deleteButton.textContent = "×";
        deleteButton.title = "删除会话记录";
        deleteButton.setAttribute("aria-label", "删除会话记录 " + session.session_id);
        deleteButton.addEventListener("click", (event) => {
          event.stopPropagation();
          deleteSession(session.session_id);
        });

        row.appendChild(button);
        row.appendChild(deleteButton);
        sessionList.appendChild(row);
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

    async function createSession(options = {}) {
      syncSessionDesignResults([]);
      setBusy(true, "正在启动...");
      try {
        const payload = await api("/api/sessions", {
          method: "POST",
          body: JSON.stringify({
            provider: providerSelect.value,
            model: WEB_MODEL,
            auto_skill: toInternalSkillName(selectedSkillName()),
            auto_approve: autoApproveToggle.checked,
          }),
        });
        updateMeta(payload.session);
        renderMessages(payload.session.messages);
        setActiveView("chat");
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
      setActiveView("chat");
      renderSessionList();
    }

    async function deleteSession(sessionId) {
      if (state.busy) return;
      const isCurrent = sessionId === state.sessionId;
      if (!window.confirm("删除这条会话记录？此操作会移除服务器上的历史文件。")) return;
      setBusy(true, "正在删除...");
      try {
        await api("/api/sessions/" + encodeURIComponent(sessionId), { method: "DELETE" });
        state.sessions = state.sessions.filter((session) => session.session_id !== sessionId);
        if (isCurrent) {
          state.sessionId = null;
          saveLocalState();
          await createSession({ keepBusy: true });
        } else {
          await refreshSessions();
        }
        setStatus("会话记录已删除。");
      } catch (error) {
        setStatus(error.message, true);
      } finally {
        setBusy(false);
      }
    }

    async function resetSession() {
      if (!state.sessionId) return;
      setBusy(true, "正在清空...");
      try {
        const payload = await api("/api/sessions/" + encodeURIComponent(state.sessionId) + "/reset", {
          method: "POST",
          body: JSON.stringify({
            auto_approve: autoApproveToggle.checked,
            auto_skill: toInternalSkillName(selectedSkillName()),
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
      if (selectedSkillName() !== (state.autoSkill || "")) {
        await createSession({ keepBusy: true });
      }
    }

    function parseSseBlock(block) {
      const lines = block.split("\n");
      let event = "message";
      const dataLines = [];
      for (const line of lines) {
        if (line.startsWith("event:")) event = line.slice(6).trim();
        if (line.startsWith("data:")) dataLines.push(line.slice(5).trimStart());
      }
      if (!dataLines.length) return null;
      try {
        return { event, data: JSON.parse(dataLines.join("\n")) };
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
        const blocks = buffer.split("\n\n");
        buffer = blocks.pop() || "";
        for (const block of blocks) {
          const parsed = parseSseBlock(block);
          if (!parsed) continue;
          if (parsed.event === "chunk") handlers.onChunk?.(parsed.data.text || "");
          if (parsed.event === "tool") handlers.onTool?.(parsed.data);
          if (parsed.event === "error") throw new Error(parsed.data.error || "流式请求失败");
          if (parsed.event === "done") {
            finalPayload = parsed.data;
            await reader.cancel().catch(() => {});
            break;
          }
        }
        if (finalPayload) break;
      }
      if (buffer.trim()) {
        const parsed = parseSseBlock(buffer);
        if (parsed?.event === "done") finalPayload = parsed.data;
      }
      if (!finalPayload) throw new Error("流式响应在完成前中断。");
      return finalPayload;
    }

    function designInputNumber(input, label) {
      const value = Number(input.value);
      if (!Number.isFinite(value)) throw new Error(label + "必须是有效数字。");
      return value;
    }

    function currentDesignEnergyMode() {
      return designPropulsionType.value === "jet" ? "jet" : "prop";
    }

    function designEnergyPath(mode = currentDesignEnergyMode()) {
      return "initial_guess." + DESIGN_ENERGY_CONFIG[mode].field;
    }

    function resetDesignEnergyValues() {
      state.designEnergyValues.prop = DESIGN_ENERGY_CONFIG.prop.defaultValue;
      state.designEnergyValues.jet = DESIGN_ENERGY_CONFIG.jet.defaultValue;
      state.designLegacyEnergy.prop = null;
      state.designLegacyEnergy.jet = null;
      designPropEfficiency.value = "0.8";
    }

    function captureDesignEnergyValue() {
      const mode = designSfc.dataset.energyMode;
      const value = Number(designSfc.value);
      if (DESIGN_ENERGY_CONFIG[mode] && Number.isFinite(value)) {
        state.designEnergyValues[mode] = value;
      }
    }

    function designCruiseSpeedMps() {
      const altitudeM = Math.max(0, Number(designCruiseAltitude.value) || 0);
      const mach = Math.max(0, Number(designCruiseMach.value) || 0);
      const temperatureK = 288.15 - 0.0065 * Math.min(altitudeM, 11000);
      return mach * Math.sqrt(1.4 * 287.05287 * temperatureK);
    }

    function migrateLegacyDesignSfc(value, mode) {
      const legacy = Number(value);
      if (!Number.isFinite(legacy) || legacy <= 0) return null;
      if (mode === "jet") return legacy / 9.80665;
      const efficiency = Number(designPropEfficiency.value);
      const speedMps = designCruiseSpeedMps();
      if (!Number.isFinite(efficiency) || efficiency <= 0 || speedMps <= 0) return null;
      return legacy * efficiency / (9.80665 * speedMps);
    }

    function syncDesignEnergyMode(options = {}) {
      if (options.captureCurrent !== false) captureDesignEnergyValue();
      const mode = currentDesignEnergyMode();
      const config = DESIGN_ENERGY_CONFIG[mode];
      designSfc.dataset.energyMode = mode;
      designSfcLabel.textContent = config.label;
      designSfc.min = String(config.min);
      designSfc.max = String(config.max);
      designSfc.value = String(state.designEnergyValues[mode] ?? config.defaultValue);
      designPropEfficiencyField.hidden = mode !== "prop";
      designSfc.disabled = state.designJobRunning || !designUseAdvanced.checked;
      designPropEfficiency.disabled = state.designJobRunning || !designUseAdvanced.checked || mode !== "prop";
    }

    function restoreDesignFieldSources(provenance = null) {
      state.designFieldSources = {};
      for (const path of designFieldPaths.values()) state.designFieldSources[path] = "default";
      state.designFieldSources[designEnergyPath("prop")] = "default";
      state.designFieldSources[designEnergyPath("jet")] = "default";
      if (!provenance || typeof provenance !== "object") return;
      const inputFields = provenance.input_fields || {};
      for (const group of ["requirements", "initial_guess", "solver"]) {
        const fields = inputFields[group];
        if (!fields || typeof fields !== "object") continue;
        for (const [name, entry] of Object.entries(fields)) {
          const source = typeof entry === "string" ? entry : entry?.source;
          if (["user", "default", "derived"].includes(source)) state.designFieldSources[group + "." + name] = source;
        }
      }
      const projectSource = typeof provenance.project_name === "string" ? provenance.project_name : provenance.project_name?.source;
      if (["user", "default", "derived"].includes(projectSource)) state.designFieldSources.project_name = projectSource;
    }

    function buildDesignRequestProvenance(request) {
      const inputFields = { requirements: {} };
      for (const [name, value] of Object.entries(request.requirements || {})) {
        const path = "requirements." + name;
        inputFields.requirements[name] = {
          source: state.designFieldSources[path] || "default",
          value,
        };
      }
      if (request.initial_guess) {
        inputFields.initial_guess = {};
        for (const [name, value] of Object.entries(request.initial_guess)) {
          const path = "initial_guess." + name;
          inputFields.initial_guess[name] = {
            source: state.designFieldSources[path] || "default",
            value,
          };
        }
      }
      if (
        request.tolerance !== undefined
        || request.max_iterations !== undefined
        || request.auto_repair_enabled !== undefined
        || request.max_repair_attempts !== undefined
      ) {
        inputFields.solver = {};
        if (request.tolerance !== undefined) {
          inputFields.solver.tolerance = {
            source: state.designFieldSources["solver.tolerance"] || "default",
            value: request.tolerance,
          };
        }
        if (request.max_iterations !== undefined) {
          inputFields.solver.max_iterations = {
            source: state.designFieldSources["solver.max_iterations"] || "default",
            value: request.max_iterations,
          };
        }
        if (request.auto_repair_enabled !== undefined) {
          inputFields.solver.auto_repair_enabled = {
            source: state.designFieldSources["solver.auto_repair_enabled"] || "default",
            value: request.auto_repair_enabled,
          };
        }
        if (request.max_repair_attempts !== undefined) {
          inputFields.solver.max_repair_attempts = {
            source: state.designFieldSources["solver.max_repair_attempts"] || "default",
            value: request.max_repair_attempts,
          };
        }
      }
      const energyMode = request.requirements?.propulsion_type === "jet" ? "jet" : "prop";
      const energyField = DESIGN_ENERGY_CONFIG[energyMode].field;
      const energyWasSubmitted = Object.prototype.hasOwnProperty.call(request.initial_guess || {}, energyField);
      const legacyEnergy = energyWasSubmitted && Boolean(state.designLegacyEnergy[energyMode]);
      return {
        request_contract_version: 2,
        propulsion_energy: {
          propulsion_type: request.requirements?.propulsion_type,
          canonical_field: energyField,
          source: !energyWasSubmitted
            ? "default"
            : legacyEnergy
            ? "legacy_migrated_at_cruise_condition"
            : (state.designFieldSources[designEnergyPath(energyMode)] || "default"),
          legacy_field: legacyEnergy ? "sfc_cruise_1_s" : null,
          legacy_semantics: legacyEnergy
            ? "equivalent fuel-weight-flow / thrust at the declared cruise condition [1/s]"
            : null,
        },
        project_name: {
          source: state.designFieldSources.project_name || "default",
          value: request.project_name,
        },
        input_fields: inputFields,
        ui: { custom_initial_guess: designUseAdvanced.checked },
      };
    }

    function buildDesignJobRequest() {
      const request = {
        project_name: designProjectName.value.trim(),
        auto_repair_enabled: designAutoRepairEnabled.checked,
        max_repair_attempts: Math.trunc(designInputNumber(designMaxRepairAttempts, "最大修正轮次")),
        requirements: {
          range_m: designInputNumber(designRangeKm, "航程") * 1000,
          payload_kg: designInputNumber(designPayloadKg, "有效载荷"),
          cruise_mach: designInputNumber(designCruiseMach, "巡航马赫数"),
          cruise_altitude_m: designInputNumber(designCruiseAltitude, "巡航高度"),
          takeoff_distance_m: designInputNumber(designTakeoffDistance, "起飞距离"),
          landing_distance_m: designInputNumber(designLandingDistance, "着陆距离"),
          max_load_factor: designInputNumber(designMaxLoadFactor, "最大过载"),
          sustained_turn_g: designInputNumber(designSustainedTurnG, "持续盘旋过载"),
          service_ceiling_m: designInputNumber(designServiceCeiling, "实用升限"),
          aircraft_role: designAircraftRole.value,
          propulsion_type: designPropulsionType.value,
          reserve_fraction: designInputNumber(designReserveFraction, "储备燃油比例"),
          tail_layout: designTailLayout.value,
          cl_max_takeoff: designInputNumber(designClmaxTakeoff, "起飞 CLmax"),
          cl_max_landing: designInputNumber(designClmaxLanding, "着陆 CLmax"),
          assumed_climb_rate_m_s: designInputNumber(designAssumedClimbRate, "假定爬升率"),
          uncertainty_enabled: designUncertaintyEnabled.checked,
        },
      };
      if (request.requirements.service_ceiling_m < request.requirements.cruise_altitude_m) {
        throw new Error("实用升限不能低于巡航高度。");
      }
      if (designUseAdvanced.checked) {
        const energyConfig = DESIGN_ENERGY_CONFIG[currentDesignEnergyMode()];
        request.initial_guess = {
          mtow_kg: designInputNumber(designMtowGuess, "最大起飞重量初值"),
          wing_loading_pa: designInputNumber(designWingLoading, "翼载初猜"),
          thrust_to_weight: designInputNumber(designThrustWeight, "推重比初猜"),
          aspect_ratio: designInputNumber(designAspectRatio, "展弦比"),
          sweep_deg: designInputNumber(designSweepDeg, "后掠角"),
          taper_ratio: designInputNumber(designTaperRatio, "梯形比"),
          thickness_ratio: designInputNumber(designThicknessRatio, "厚度比"),
          cd0: designInputNumber(designCd0, "零升阻力系数"),
          oswald_e: designInputNumber(designOswald, "Oswald 效率因子"),
          cg_fraction_cbar: designInputNumber(designCgFraction, "重心位置"),
          horizontal_tail_volume_coefficient: designInputNumber(designTailVolume, "平尾容积系数"),
        };
        request.initial_guess[energyConfig.field] = designInputNumber(designSfc, energyConfig.inputLabel);
        if (request.requirements.propulsion_type === "prop") {
          request.initial_guess.prop_efficiency = designInputNumber(designPropEfficiency, "螺旋桨效率");
        }
        request.tolerance = designInputNumber(designTolerance, "收敛容差");
        request.max_iterations = Math.trunc(designInputNumber(designMaxIterations, "最大迭代次数"));
      }
      request.provenance = buildDesignRequestProvenance(request);
      return request;
    }

    function designProgressEvent(event) {
      const failed = ["failed", "engineering_infeasible", "nonconverged", "cancelled", "timed_out", "interrupted"].includes(event.stage);
      return {
        kind: "design_stage",
        tool_name: "总体设计求解器",
        stage: event.stage,
        summary: localizedStageMessage(event.message, event.stage),
        preview: event.detail || { progress: event.progress },
        is_error: failed,
        error: failed ? localizedStageMessage(event.message, event.stage) : null,
      };
    }

    function refreshDesignJobMessage() {
      if (!state.designJobMessage) {
        state.designJobMessage = createMessage("assistant", "", {
          events: state.designJobEvents,
          isRunning: true,
          openProcess: true,
        });
        chatLog.appendChild(state.designJobMessage);
      }
      updateProcessPanel(state.designJobMessage, state.designJobEvents, {
        isRunning: true,
        open: true,
      });
      chatLog.scrollTop = chatLog.scrollHeight;
    }

    function designJobStatusLabel(status) {
      return {
        queued: "排队中",
        preparing: "准备中",
        running: "计算中",
        validating: "工程校验中",
        completed: "已完成",
        engineering_infeasible: "工程不可行",
        nonconverged: "未收敛",
        failed: "失败",
        cancelled: "已取消",
        timed_out: "已超时",
        interrupted: "已中断",
      }[status] || "状态未知";
    }

    function designJobTimestamp(value) {
      const date = new Date(value || "");
      if (Number.isNaN(date.getTime())) return "时间未知";
      return date.toLocaleString("zh-CN", {
        month: "2-digit",
        day: "2-digit",
        hour: "2-digit",
        minute: "2-digit",
      });
    }

    function designNode(tag, className = "", textContent = "") {
      const node = document.createElement(tag);
      if (className) node.className = className;
      if (textContent !== "") node.textContent = textContent;
      return node;
    }

    function finiteDesignNumber(value) {
      const parsed = Number(value);
      return Number.isFinite(parsed) ? parsed : null;
    }

    const DESIGN_CONSTRAINT_LABELS = Object.freeze({
      "class1.range": "任务航程",
      "class1.fuel_fraction": "任务燃油质量分数",
      "class1.takeoff_distance": "预测起飞距离",
      "class1.landing_distance": "预测着陆距离",
      "class1.sustained_turn_thrust": "持续盘旋推重比",
      "class1.service_ceiling_thrust": "实用升限推重比",
      "class1.weight_closure": "最大起飞重量闭合误差",
      "advanced.propulsion.cruise_thrust_margin": "巡航推力裕度",
      "advanced.propulsion.climb_thrust_margin": "爬升推力裕度",
      "advanced.mission.fuel_capacity": "可用任务燃油",
      "advanced.stability.static_margin_min": "最小静稳定裕度",
      "advanced.stability.static_margin_max": "建议最大静稳定裕度",
      "advanced.structures.weight_feedback": "结构重量反馈",
      "advanced.geometry.fuel_volume": "可用燃油容积",
      "advanced.geometry.aspect_ratio_limit": "展弦比上限",
      "advanced.optimization.reduced_order_screened_candidates": "降阶筛选候选方案数",
      "declared.max_mtow_kg": "最大起飞重量上限",
      "declared.max_aspect_ratio": "最大展弦比",
      "declared.min_cruise_endurance_s": "最低巡航航时",
      "declared.special_mission_model_coverage": "专项任务模型覆盖",
      "thrust_margin_cruise": "巡航推力裕度",
      "thrust_margin_climb": "爬升推力裕度",
      "mission_fuel_capacity": "任务燃油容量",
      "mission_fuel_fraction": "任务燃油质量分数",
      "static_margin": "静稳定裕度",
      "Evaluated mission distance": "评估任务航程",
      "Predicted mission range": "预测最大航程",
      "Range metric with undeclared evidence": "航程指标（证据未声明）",
      "Mission fuel mass fraction": "任务燃油质量分数",
      "Predicted takeoff distance": "预测起飞距离",
      "Predicted landing distance": "预测着陆距离",
      "Sustained-turn thrust-to-weight": "持续盘旋推重比",
      "Service-ceiling thrust-to-weight": "实用升限推重比",
      "Relative MTOW closure error": "最大起飞重量闭合相对误差",
      "Cruise thrust margin": "巡航推力裕度",
      "Climb thrust margin": "爬升推力裕度",
      "Available mission fuel": "可用任务燃油",
      "Mission fuel capacity": "任务燃油容量",
      "Mission fuel fraction": "任务燃油质量分数",
      "Static stability margin": "静稳定裕度",
      "Minimum static margin": "最小静稳定裕度",
      "Maximum recommended static margin": "建议最大静稳定裕度",
      "Advanced structural-weight feedback": "结构重量反馈",
      "Fuel Volume": "可用燃油容积",
      "Fuel volume": "可用燃油容积",
      "Aspect Ratio Limit": "展弦比上限",
      "Reduced-order screened candidates": "降阶筛选候选方案数",
      "Maximum takeoff weight": "最大起飞重量上限",
      "Maximum aspect ratio": "最大展弦比",
      "Minimum cruise endurance": "最低巡航航时",
      "Weight closure": "重量闭合",
    });

    const DESIGN_RECOMMENDATION_LABELS = Object.freeze({
      "Increase installed thrust.": "增加安装推力，并重新校核巡航与爬升推力裕度。",
      "Increase available thrust or reduce weight and drag until the margin is positive.": "增加可用推力，或降低重量与阻力，直至推力裕度为正。",
      "Increase T/W, reduce W/S, or increase takeoff CLmax.": "提高推重比、降低翼载，或提高起飞最大升力系数。",
      "Reduce W/S, increase landing CLmax, or improve braking assumptions.": "降低翼载、提高着陆最大升力系数，或改进制动假设。",
      "Increase T/W or reduce turn load factor and induced drag.": "提高推重比，或降低盘旋过载与诱导阻力。",
      "Increase installed thrust or reduce ceiling requirement.": "增加安装推力，或适当降低实用升限要求。",
      "Reduce mission demand or improve aerodynamic and propulsion efficiency.": "降低任务需求，或提高气动与推进效率。",
      "Reduce mission fuel demand or increase usable fuel capacity and close the weight loop again.": "降低任务燃油需求，或增加可用燃油容量，并重新执行重量闭合。",
      "Move the CG forward or increase horizontal-tail effectiveness.": "前移重心，或提高平尾效能。",
      "Increase usable wing tank volume or reduce mission fuel.": "增加机翼可用油箱容积，或降低任务燃油需求。",
    });

    const DESIGN_PROVENANCE_LABELS = Object.freeze({
      auto_repair: "自动修正记录",
      requirement_workflow: "需求协商记录",
      propulsion_energy: "推进能耗模型",
      input_fields: "输入字段来源",
      request_contract_version: "请求契约版本",
      solver_submission: "求解提交记录",
      design_attempt_history: "设计尝试记录",
      validation_level: "验证层级",
      model_version: "模型版本",
      requirement_intent: "需求意图记录",
      user_requirements: "用户原始要求",
      soft_goals: "保留软目标",
      projection: "求解输入投影",
      runner_validation: "求解器校验",
      auto_repair_history: "自动修正历史",
      project_name: "项目名称",
      ui: "界面提交信息",
    });

    function designConstraintLabel(item) {
      const record = item && typeof item === "object" ? item : { id: item };
      const id = String(record.id || "");
      const raw = String(record.label || record.name || id || "");
      if (DESIGN_CONSTRAINT_LABELS[id]) return DESIGN_CONSTRAINT_LABELS[id];
      if (DESIGN_CONSTRAINT_LABELS[raw]) return DESIGN_CONSTRAINT_LABELS[raw];
      if (containsChineseText(raw)) return raw;
      return "其他工程约束";
    }

    function designStageStatusLabel(status) {
      return ({
        passed: "通过",
        pass: "通过",
        completed: "已完成",
        feasible: "可行",
        failed: "未通过",
        fail: "未通过",
        infeasible: "不可行",
        not_converged: "未收敛",
        nonconverged: "未收敛",
        error: "错误",
        pending: "待处理",
        running: "计算中",
        unknown: "待判定",
      })[String(status || "unknown").toLowerCase()] || "待判定";
    }

    function localizedStageMessage(message, status = "") {
      if (!message) return "";
      if (containsChineseText(message)) return message;
      const normalized = String(status || "").toLowerCase();
      if (["failed", "fail", "infeasible", "not_converged", "nonconverged", "error"].includes(normalized)) {
        return "该阶段未通过，请查看约束裕度和诊断记录。";
      }
      return "该阶段已更新工程状态。";
    }

    function localizedJobMessage(message, status = "") {
      if (!message) return "";
      if (containsChineseText(message)) return message;
      const normalized = String(status || "").toLowerCase();
      if (["failed", "engineering_infeasible", "nonconverged", "cancelled", "timed_out", "interrupted"].includes(normalized)) {
        return "任务未通过，请查看约束裕度和诊断建议。";
      }
      if (["queued", "preparing", "running", "validating"].includes(normalized)) {
        return `任务${designJobStatusLabel(normalized)}。`;
      }
      return "任务状态已更新。";
    }

    function localizedEngineeringRecommendation(value) {
      const text = String(value || "");
      if (containsChineseText(text)) return text;
      return DESIGN_RECOMMENDATION_LABELS[text]
        || "请根据未通过的约束调整相关设计变量，并执行完整重算。";
    }

    function localizedEngineeringIssue(issue) {
      const code = String(issue?.code || "");
      const message = String(issue?.message || "");
      if (containsChineseText(message)) return message;
      const labels = {
        process_exit: "求解器进程异常退出。",
        solver_nonconverged_exit: "求解器未完成数值收敛。",
        missing_output_dir: "求解器没有生成结果目录。",
        missing_artifact: "缺少必要的工程结果文件。",
        invalid_design_data: "工程结果数据无法解析。",
        input_mismatch: "结果中的输入快照与本次提交不一致。",
        missing_outputs: "工程结果缺少总体输出数据。",
        invalid_metric: "工程结果包含无效的关键指标。",
        missing_geometry: "工程结果缺少可用的几何数据。",
        invalid_constraints_contract: "约束结果不符合当前数据契约。",
        invalid_constraint_contract: "一项约束结果不完整。",
        invalid_stage_status_contract: "阶段门结果不符合当前数据契约。",
        inconsistent_engineering_feasibility: "工程可行性标记与阻断证据不一致。",
        blocking_constraint_failed: "一项阻断约束未通过。",
        blocking_constraint_unknown: "一项阻断约束缺少明确判定。",
        blocking_stage_failed: "一项阻断阶段门未通过。",
        engineering_infeasible: "当前方案未通过工程可行性判定。",
      };
      return labels[code] || "工程校验发现一项需要处理的问题。";
    }

    function designProvenanceLabel(key) {
      const raw = String(key || "");
      if (DESIGN_PROVENANCE_LABELS[raw]) return DESIGN_PROVENANCE_LABELS[raw];
      if (REQUIREMENT_FIELD_LABELS[raw]) return REQUIREMENT_FIELD_LABELS[raw];
      if (containsChineseText(raw)) return raw;
      return "其他追溯信息";
    }

    function formatDesignProvenanceValue(value) {
      if (value && typeof value === "object") {
        const size = Array.isArray(value) ? value.length : Object.keys(value).length;
        return `已记录 ${size} 项结构化数据`;
      }
      return formatDesignValue(value);
    }

    function formatDesignValue(value, unit = "", digits = 2) {
      if (value === null || value === undefined || value === "") return "--";
      if (typeof value === "boolean") return value ? "是" : "否";
      if (unit === "boolean") {
        if (value === 1 || value === "1") return "是";
        if (value === 0 || value === "0") return "否";
        return "待判定";
      }
      const localizedUnit = ({
        ratio: "比值",
        count: "个",
        cbar: "平均气动弦长比例",
        c_bar: "平均气动弦长比例",
        m3: "m³",
        relative_error: "相对误差",
        Mach: "马赫",
      })[unit] || unit;
      const numeric = finiteDesignNumber(value);
      if (numeric !== null) {
        const magnitude = Math.abs(numeric);
        const places = magnitude >= 100 ? 1 : magnitude >= 10 ? Math.min(digits, 2) : digits;
        return numeric.toLocaleString("zh-CN", { maximumFractionDigits: places }) + (localizedUnit ? " " + localizedUnit : "");
      }
      if (typeof value === "object") return JSON.stringify(value);
      return String(requirementValueLabel(value)) + (localizedUnit ? " " + localizedUnit : "");
    }

    function formatConstraintMargin(item) {
      return formatDesignValue(item?.margin, item?.unit === "boolean" ? "" : item?.unit);
    }

    function formatRepairValue(value) {
      const numeric = finiteDesignNumber(value);
      if (numeric === null) return "--";
      const magnitude = Math.abs(numeric);
      if (magnitude > 0 && magnitude < 0.001) return numeric.toExponential(5);
      return numeric.toLocaleString("zh-CN", { maximumSignificantDigits: 6 });
    }

    function designEngineering(job) {
      return job?.result?.engineering || {};
    }

    function designValidationGaps(job) {
      const provenance = job?.request?.provenance;
      if (!provenance || typeof provenance !== "object") return [];
      const requirementIntent = provenance.requirement_intent;
      const gaps = new Map();
      const fieldPathAliases = {
        max_mtow_kg: "weights.max_mtow_kg",
        max_aspect_ratio: "geometry.max_aspect_ratio",
        min_cruise_endurance_s: "performance.min_cruise_endurance_s",
        max_flight_mach: "performance.max_flight_mach",
        launch_mode: "launch.mode",
        launch_field_altitude_m: "launch.field_altitude_m",
        booster_end_mach: "launch.booster_end_mach",
        booster_end_relative_altitude_m: "launch.booster_end_relative_altitude_m",
        recovery_mode: "recovery.mode",
        parachute_open_mach: "recovery.parachute_open_mach",
        parachute_open_relative_altitude_m: "recovery.parachute_open_relative_altitude_m",
        engine_count: "propulsion.engine_count",
        configuration_reference: "configuration.reference",
        stealth_requirement: "configuration.stealth_requirement",
      };
      const normalizedPath = (value) => {
        const rawPath = String(value || "").trim();
        const path = rawPath.startsWith("deferred.")
          ? rawPath.slice("deferred.".length)
          : rawPath;
        return fieldPathAliases[path] || path;
      };
      const addGap = ({ path: rawPath, value, unit, reason, source, scopeStatement = "", preferReason = false }) => {
        const path = normalizedPath(rawPath);
        if (!path) return;
        const existing = gaps.get(path);
        if (!existing) {
          gaps.set(path, { path, value, unit, reason, source, scopeStatement });
          return;
        }
        gaps.set(path, {
          ...existing,
          value: existing.value === undefined ? value : existing.value,
          unit: existing.unit || unit,
          reason: preferReason && reason ? reason : existing.reason || reason,
          source: preferReason && source ? source : existing.source || source,
          scopeStatement: preferReason && scopeStatement
            ? scopeStatement
            : existing.scopeStatement || scopeStatement,
        });
      };

      for (const requirement of requirementIntent?.requirements || []) {
        const path = String(requirement?.path || "");
        if (!path.startsWith("deferred.")) continue;
        addGap({
          path,
          value: requirement.value,
          unit: requirement.unit,
          reason: "该要求已从当前求解范围延后，仍需完成对应专项验证。",
          source: "延后需求",
        });
      }

      const scopeDeferrals = requirementIntent?.metadata?.requirement_workflow?.scope_deferrals;
      for (const deferral of Array.isArray(scopeDeferrals) ? scopeDeferrals : []) {
        for (const field of Array.isArray(deferral?.fields) ? deferral.fields : []) {
          addGap({
            path: field?.field_path || field?.retained_field_path,
            value: field?.value,
            unit: field?.unit,
            reason: field?.coverage_reason || field?.scope_statement || deferral?.scope_statement
              || "当前总体模型尚未覆盖该专项要求。",
            source: "范围协商记录",
            scopeStatement: field?.scope_statement || deferral?.scope_statement || "",
            preferReason: true,
          });
        }
      }

      const softGoals = provenance.soft_goals;
      if (softGoals && typeof softGoals === "object" && !Array.isArray(softGoals)) {
        for (const [path, value] of Object.entries(softGoals)) {
          addGap({
            path,
            value,
            reason: "保留的专项目标，当前求解未完成专项验证。",
            source: "保留软目标",
          });
        }
      }
      return Array.from(gaps.values());
    }

    function designOutcome(job) {
      if (!job) return { tone: "warn", label: "尚未选择任务", detail: "选择任务后查看工程状态。" };
      const engineering = designEngineering(job);
      const overall = String(engineering.overall_status || "").toLowerCase();
      const numerical = engineering.numerical_converged ?? job.result?.converged ?? null;
      const feasible = engineering.engineering_feasible ?? null;
      const blockingFailedCount = engineering.blocking_failed_count;
      const validationGaps = designValidationGaps(job);
      const outcome = (value) => ({
        ...value,
        limitedScope: validationGaps.length > 0,
        validationGaps,
      });
      const failedStatuses = ["failed", "cancelled", "timed_out", "interrupted"];
      if (failedStatuses.includes(job.status)) {
        return outcome({ tone: "fail", label: designJobStatusLabel(job.status), detail: localizedJobMessage(job.error || job.message, job.status) || "任务未完成。" });
      }
      if (job.status === "nonconverged" || overall === "nonconverged" || numerical === false) {
        return outcome({ tone: "fail", label: "数值未收敛", detail: "当前结果不能作为工程可行方案。" });
      }
      if (job.status === "engineering_infeasible" || overall === "infeasible" || feasible === false || blockingFailedCount > 0) {
        const detail = blockingFailedCount > 0
          ? `计算已完成，但仍有 ${blockingFailedCount} 个阻断约束或阶段门未通过。`
          : "计算已完成，但至少一个阻断约束或阶段门未通过。";
        return outcome({ tone: "fail", label: "工程不可行", detail });
      }
      const hardGatesPass = numerical === true && feasible === true && blockingFailedCount === 0;
      if (hardGatesPass && validationGaps.length) {
        return outcome({
          tone: "pass",
          label: "覆盖范围内初步通过",
          detail: `数值已收敛，当前覆盖范围内的阻断约束和阶段门均通过。这是当前模型覆盖范围内的初步候选，仍有 ${validationGaps.length} 项专项验证缺口。`,
        });
      }
      if (hardGatesPass) {
        return outcome({
          tone: "pass",
          label: "初步可行候选",
          detail: "数值已收敛，阻断约束和阶段门均通过。该结论仅代表当前初步模型结论，不代表生产就绪或飞行安全。",
        });
      }
      if (["queued", "running", "preparing", "validating"].includes(job.status) || !job.terminal) {
        return outcome({ tone: "warn", label: designJobStatusLabel(job.status), detail: localizedJobMessage(job.message, job.status) || "工程校验尚未完成。" });
      }
      return outcome({
        tone: "warn",
        label: job.status === "completed" ? "计算完成，待工程判定" : designJobStatusLabel(job.status),
        detail: "结果缺少数值收敛、工程可行性或阻断项计数中的完整判定字段，不能标记为通过。",
      });
    }

    function normalizeDesignStages(value) {
      if (Array.isArray(value)) return value;
      if (!value || typeof value !== "object") return [];
      return Object.entries(value).map(([id, item]) => ({ id, ...(item || {}) }));
    }

    function normalizeDesignConstraints(value) {
      if (Array.isArray(value)) return value;
      if (!value || typeof value !== "object") return [];
      return Object.entries(value).map(([id, item]) => ({ id, ...(item || {}) }));
    }

    function formatConstraintRequirement(item) {
      const direction = {
        min: ">=", minimum: ">=", greater_than_or_equal: ">=", ">=": ">=",
        max: "<=", maximum: "<=", less_than_or_equal: "<=", "<=": "<=",
        eq: "=", equal: "=", "=": "=",
      }[item.direction] || item.direction || "";
      return (direction ? direction + " " : "") + formatDesignValue(item.required ?? item.target, item.unit);
    }

    function createDesignTable(headers, rows, className = "") {
      const wrapper = designNode("div", "design-table-wrap");
      const table = designNode("table", "design-data-table" + (className ? " " + className : ""));
      const thead = document.createElement("thead");
      const headingRow = document.createElement("tr");
      for (const headerText of headers) headingRow.appendChild(designNode("th", "", headerText));
      thead.appendChild(headingRow);
      table.appendChild(thead);
      const tbody = document.createElement("tbody");
      for (const row of rows) {
        const tr = document.createElement("tr");
        if (row.className) tr.className = row.className;
        for (const cellValue of row.cells) {
          const td = document.createElement("td");
          if (cellValue instanceof Node) td.appendChild(cellValue);
          else td.textContent = cellValue;
          tr.appendChild(td);
        }
        tbody.appendChild(tr);
      }
      table.appendChild(tbody);
      wrapper.appendChild(table);
      return wrapper;
    }

    function renderDesignRunTimeline() {
      if (!designRunTimeline) return;
      designRunTimeline.innerHTML = "";
      const events = state.designJobEvents || [];
      if (!events.length) {
        designRunTimeline.appendChild(designNode("div", "design-empty-state compact", "任务开始后，这里会显示阶段进度。"));
        return;
      }
      const list = designNode("ol", "design-timeline-list");
      for (const event of events) {
        const item = designNode("li", event.is_error ? "is-fail" : "");
        item.appendChild(designNode("strong", "", designJobStatusLabel(event.stage)));
        item.appendChild(designNode("span", "", localizedStageMessage(event.summary, event.stage) || "阶段已更新"));
        list.appendChild(item);
      }
      designRunTimeline.appendChild(list);
    }

    function localPreflightPayload(request) {
      const assumptions = [
        { path: "requirements.aircraft_role", value: request.requirements.aircraft_role, source: "user" },
        { path: "requirements.propulsion_type", value: request.requirements.propulsion_type, source: "user" },
        { path: "requirements.reserve_fraction", value: request.requirements.reserve_fraction, source: "user" },
        { path: "requirements.tail_layout", value: request.requirements.tail_layout, source: "user" },
        { path: "requirements.cl_max_takeoff", value: request.requirements.cl_max_takeoff, source: "user" },
        { path: "requirements.cl_max_landing", value: request.requirements.cl_max_landing, source: "user" },
        { path: "initial_guess", value: request.initial_guess ? "自定义" : "按任务自动选择", source: request.initial_guess ? "user" : "default" },
      ];
      const warnings = [];
      if (request.requirements.reserve_fraction < 0.05) warnings.push("储备燃油比例低于 5%，应确认任务放行规则。");
      if (request.requirements.cl_max_landing < request.requirements.cl_max_takeoff) warnings.push("着陆 CLmax 低于起飞 CLmax，请确认增升构型。");
      return { ready: true, request, assumptions, warnings, field_sources: {} };
    }

    function applyClientProvenanceToPreflight(payload, request) {
      const normalized = payload?.request || request;
      const fields = request?.provenance?.input_fields || {};
      const assumptions = Array.isArray(payload.assumptions) ? [...payload.assumptions] : [];
      const fieldSources = { ...(payload.field_sources || {}) };
      for (const group of ["requirements", "initial_guess", "solver"]) {
        for (const [name, entry] of Object.entries(fields[group] || {})) {
          const path = group + "." + name;
          const source = typeof entry === "string" ? entry : entry?.source;
          if (!["user", "default", "derived"].includes(source)) continue;
          fieldSources[path] = source;
          const existingIndex = assumptions.findIndex((item) => item.path === path);
          const value = normalized?.[group]?.[name] ?? entry?.value;
          if (source === "user" && existingIndex >= 0) {
            assumptions.splice(existingIndex, 1);
          } else if (source !== "user" && existingIndex >= 0) {
            assumptions[existingIndex] = { ...assumptions[existingIndex], value, source };
          } else if (source !== "user") {
            assumptions.push({ path, value, source });
          }
        }
      }
      payload.field_sources = fieldSources;
      payload.assumptions = assumptions;
      return payload;
    }

    function renderDesignPreflight(payload, usedFallback = false) {
      designPreflightSummary.innerHTML = "";
      const assumptions = Array.isArray(payload?.assumptions) ? [...payload.assumptions] : [];
      const warnings = Array.isArray(payload?.warnings) ? payload.warnings : [];
      const fieldSources = payload?.field_sources && typeof payload.field_sources === "object" ? payload.field_sources : {};
      const valueAtPath = (root, path) => String(path).split(".").reduce((value, key) => value?.[key], root);
      for (const [path, source] of Object.entries(fieldSources)) {
        if (assumptions.some((item) => item.path === path)) continue;
        assumptions.push({ path, value: valueAtPath(payload?.request, path), source });
      }
      const summary = designNode("div", "design-preflight-grid");
      for (const assumption of assumptions) {
        const item = designNode("div", "design-preflight-item");
        item.appendChild(designNode("span", "", requirementFieldLabel(assumption.path || assumption.name)));
        item.appendChild(designNode("strong", "", formatDesignValue(assumption.value)));
        item.appendChild(designNode("small", "", assumption.source === "user" ? "用户输入" : assumption.source === "derived" ? "推导值" : "默认值"));
        summary.appendChild(item);
      }
      designPreflightSummary.appendChild(summary);
      if (warnings.length) {
        const warningBox = designNode("div", "design-preflight-warnings");
        warningBox.setAttribute("role", "alert");
        warningBox.appendChild(designNode("strong", "", "需要确认"));
        const list = document.createElement("ul");
        for (const warning of warnings) {
          const message = typeof warning === "string" ? warning : warning?.message;
          list.appendChild(designNode("li", "", containsChineseText(message)
            ? message
            : "预检发现一项需要确认的工程问题。"));
        }
        warningBox.appendChild(list);
        designPreflightSummary.appendChild(warningBox);
      }
      designPreflightState.textContent = payload?.ready === false ? "存在冲突" : usedFallback ? "本地检查" : "服务端已校验";
      designPreflightState.className = payload?.ready === false ? "is-fail" : warnings.length ? "is-warn" : "is-pass";
      designPreflightConfirm.disabled = payload?.ready === false;
      designRunBtn.disabled = state.designJobRunning || !designPreflightConfirm.checked || payload?.ready === false;
    }

    function designRequestFingerprint(request) {
      return JSON.stringify(request);
    }

    function markDesignPreflightDirty() {
      state.preflightFingerprint = null;
      state.preflightRequestFingerprint = null;
      state.confirmedPreflightFingerprint = null;
      designPreflightConfirm.checked = false;
      designPreflightConfirm.disabled = true;
      designRunBtn.disabled = true;
      designPreflightState.textContent = "需要重新检查";
      designPreflightState.className = "is-warn";
    }

    function scheduleDesignPreflight() {
      window.clearTimeout(designPreflightTimer);
      designPreflightTimer = window.setTimeout(() => void runDesignPreflight(), 280);
    }

    async function runDesignPreflight() {
      if (!designRunForm.checkValidity()) {
        designPreflightState.textContent = "请完善字段";
        designPreflightState.className = "is-fail";
        designPreflightConfirm.disabled = true;
        designRunBtn.disabled = true;
        return null;
      }
      let request;
      try {
        request = buildDesignJobRequest();
      } catch (error) {
        designPreflightState.textContent = containsChineseText(error.message)
          ? error.message
          : "预检失败，请检查输入字段。";
        designPreflightState.className = "is-fail";
        designPreflightConfirm.disabled = true;
        designRunBtn.disabled = true;
        return null;
      }
      const fingerprint = designRequestFingerprint(request);
      designPreflightState.textContent = "正在检查";
      designPreflightState.className = "is-warn";
      designPreflightBtn.disabled = true;
      let payload;
      let usedFallback = false;
      try {
        payload = await api("/api/design-jobs/preflight", {
          method: "POST",
          body: JSON.stringify({ request }),
        });
      } catch (_error) {
        payload = localPreflightPayload(request);
        payload.warnings = ["预检服务暂不可用，已完成本地字段检查。", ...(payload.warnings || [])];
        usedFallback = true;
      } finally {
        designPreflightBtn.disabled = false;
      }
      payload = applyClientProvenanceToPreflight(payload, request);
      let currentFingerprint;
      try {
        currentFingerprint = designRequestFingerprint(buildDesignJobRequest());
      } catch (_error) {
        return null;
      }
      if (fingerprint !== currentFingerprint) return null;
      const reviewFingerprint = JSON.stringify({
        request: fingerprint,
        assumptions: payload?.assumptions || [],
        warnings: payload?.warnings || [],
        field_sources: payload?.field_sources || {},
      });
      const changed = state.preflightFingerprint !== reviewFingerprint;
      state.preflightRequestFingerprint = fingerprint;
      state.preflightFingerprint = reviewFingerprint;
      if (changed && state.confirmedPreflightFingerprint !== reviewFingerprint) designPreflightConfirm.checked = false;
      renderDesignPreflight(payload, usedFallback);
      return payload;
    }

    function renderDesignVersionSelector() {
      designResultVersionSelect.innerHTML = "";
      for (const job of state.designJobs) {
        const option = document.createElement("option");
        option.value = job.job_id;
        option.textContent = [
          job.request?.project_name || "未命名设计",
          designJobTimestamp(job.finished_at || job.created_at),
          designOutcome(job).label,
        ].join(" · ");
        option.selected = job.job_id === state.designJobId;
        designResultVersionSelect.appendChild(option);
      }
      designResultVersionSelect.disabled = state.designJobs.length <= 1;
    }

    function selectSessionDesignResult(jobId) {
      const job = state.designJobs.find((item) => item.job_id === jobId);
      if (!job) return;
      state.designJobId = job.job_id;
      state.activeDesignJob = job;
      state.selectedResultFile = null;
      saveLocalState();
      renderDesignWorkspace();
    }

    function renderDesignWorkspace() {
      const job = state.activeDesignJob;
      if (job) {
        const outcome = designOutcome(job);
        designActiveJobLabel.textContent = (job.request?.project_name || "未命名设计") + " · " + outcome.label + " · " + designJobTimestamp(job.finished_at || job.created_at);
      } else {
        designActiveJobLabel.textContent = "当前对话尚无可查看的总体设计结果。";
      }
      renderDesignVersionSelector();
      setDesignTab(state.designTab);
      renderDesignResults();
      renderDesignCompareSelector();
      renderDesignComparison();
      renderDesignReports();
    }

    function designStatusChip(label, tone = "warn") {
      return designNode("span", "design-status-chip is-" + tone, label);
    }

    function stageDisplayName(id) {
      return {
        requirements: "需求归一化",
        declared_requirement: "声明需求",
        mission: "任务性能",
        weight: "重量闭合",
        performance: "飞行性能",
        numerical: "数值收敛",
        propulsion: "推进校核",
        stability: "稳定与操纵",
        structures: "结构与载荷",
        optimization: "方案优化",
        class1: "一级总体闭合",
        class1_sizing: "一级总体闭合",
        class2: "二级初步设计",
        stage2_aero: "气动分析",
        stage3_propulsion: "推进校核",
        stage4_mission: "任务性能",
        stage5_stability: "稳定与操纵",
        stage6_structures: "结构与载荷",
        stage7_optimization: "方案优化",
        class3: "三级几何与结构",
        geometry: "几何生成",
        report: "统一报告",
        reporting: "统一报告",
      }[id] || "其他工程阶段";
    }

    function createDesignSection(title, description = "") {
      const section = designNode("section", "design-data-section");
      const heading = designNode("div", "design-data-section-heading");
      heading.appendChild(designNode("h4", "", title));
      if (description) heading.appendChild(designNode("p", "", description));
      section.appendChild(heading);
      return section;
    }

    function convergenceSeries(history) {
      if (!Array.isArray(history)) return { points: [], label: "" };
      const candidates = [
        { keys: ["mtow_kg", "mtow", "weight_kg", "weight"], label: "最大起飞重量（kg）" },
        { keys: ["error", "relative_error", "residual", "delta"], label: "收敛误差" },
      ];
      for (const candidate of candidates) {
        const points = history.map((item, index) => {
          const value = candidate.keys.map((key) => finiteDesignNumber(item?.[key])).find((entry) => entry !== null);
          const iteration = finiteDesignNumber(item?.iteration) ?? finiteDesignNumber(item?.index) ?? index + 1;
          return value === undefined || value === null ? null : { x: iteration, y: value };
        }).filter(Boolean);
        if (points.length >= 2) return { points, label: candidate.label };
      }
      return { points: [], label: "" };
    }

    function createConvergenceChart(history) {
      const series = convergenceSeries(history);
      if (series.points.length < 2) return designNode("div", "design-empty-state compact", "当前结果未提供可绘制的迭代历史。" );
      const width = 760;
      const height = 240;
      const pad = { left: 58, right: 24, top: 26, bottom: 42 };
      const xs = series.points.map((point) => point.x);
      const ys = series.points.map((point) => point.y);
      const minX = Math.min(...xs);
      const maxX = Math.max(...xs);
      let minY = Math.min(...ys);
      let maxY = Math.max(...ys);
      const yPadding = Math.max((maxY - minY) * 0.12, Math.abs(maxY) * 0.002, 1e-8);
      minY -= yPadding;
      maxY += yPadding;
      const xScale = (value) => pad.left + ((value - minX) / Math.max(maxX - minX, 1)) * (width - pad.left - pad.right);
      const yScale = (value) => height - pad.bottom - ((value - minY) / Math.max(maxY - minY, 1e-12)) * (height - pad.top - pad.bottom);
      const ns = "http://www.w3.org/2000/svg";
      const svg = document.createElementNS(ns, "svg");
      svg.setAttribute("class", "design-convergence-chart");
      svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
      svg.setAttribute("role", "img");
      svg.setAttribute("aria-labelledby", "designConvergenceTitle designConvergenceDesc");
      const title = document.createElementNS(ns, "title");
      title.id = "designConvergenceTitle";
      title.textContent = "总体设计迭代收敛曲线";
      const desc = document.createElementNS(ns, "desc");
      desc.id = "designConvergenceDesc";
      desc.textContent = `${series.points.length} 个迭代点，显示 ${series.label} 随迭代次数的变化。`;
      svg.appendChild(title);
      svg.appendChild(desc);
      for (const [x1, y1, x2, y2] of [
        [pad.left, pad.top, pad.left, height - pad.bottom],
        [pad.left, height - pad.bottom, width - pad.right, height - pad.bottom],
      ]) {
        const line = document.createElementNS(ns, "line");
        line.setAttribute("x1", x1);
        line.setAttribute("y1", y1);
        line.setAttribute("x2", x2);
        line.setAttribute("y2", y2);
        line.setAttribute("class", "design-chart-axis");
        svg.appendChild(line);
      }
      const polyline = document.createElementNS(ns, "polyline");
      polyline.setAttribute("points", series.points.map((point) => `${xScale(point.x)},${yScale(point.y)}`).join(" "));
      polyline.setAttribute("class", "design-chart-line");
      svg.appendChild(polyline);
      for (const point of series.points) {
        const circle = document.createElementNS(ns, "circle");
        circle.setAttribute("cx", xScale(point.x));
        circle.setAttribute("cy", yScale(point.y));
        circle.setAttribute("r", 3.5);
        circle.setAttribute("class", "design-chart-point");
        svg.appendChild(circle);
      }
      const labels = [
        [pad.left - 8, pad.top + 4, formatDesignValue(maxY, "", 3), "end"],
        [pad.left - 8, height - pad.bottom + 4, formatDesignValue(minY, "", 3), "end"],
        [pad.left, height - 14, String(minX), "middle"],
        [width - pad.right, height - 14, String(maxX), "middle"],
      ];
      for (const [x, y, textValue, anchor] of labels) {
        const textNode = document.createElementNS(ns, "text");
        textNode.setAttribute("x", x);
        textNode.setAttribute("y", y);
        textNode.setAttribute("text-anchor", anchor);
        textNode.setAttribute("class", "design-chart-label");
        textNode.textContent = textValue;
        svg.appendChild(textNode);
      }
      return svg;
    }

    function disposeDesignModelViewer() {
      const viewer = state.designModelViewer;
      if (!viewer) return;
      cancelAnimationFrame(viewer.frameId);
      viewer.resizeObserver?.disconnect();
      viewer.controls?.dispose();
      if (viewer.resetButton && viewer.resetHandler) {
        viewer.resetButton.removeEventListener("click", viewer.resetHandler);
        viewer.resetButton.disabled = true;
      }
      const geometries = new Set();
      const materials = new Set();
      viewer.scene?.traverse((object) => {
        if (object.geometry) geometries.add(object.geometry);
        const entries = Array.isArray(object.material) ? object.material : object.material ? [object.material] : [];
        for (const material of entries) materials.add(material);
      });
      for (const geometry of geometries) geometry.dispose();
      for (const material of materials) material.dispose();
      viewer.renderer?.dispose();
      if (viewer.viewport?.isConnected) {
        viewer.renderer?.domElement?.remove();
        delete viewer.viewport.dataset.modelMounted;
      }
      state.designModelViewer = null;
    }

    function parseDesignObjGeometry(source) {
      const vertices = [];
      const positions = [];
      for (const rawLine of String(source || "").split(/\r?\n/)) {
        const line = rawLine.trim();
        if (!line || line.startsWith("#")) continue;
        const parts = line.split(/\s+/);
        if (parts[0] === "v" && parts.length >= 4) {
          const vertex = parts.slice(1, 4).map(Number);
          if (vertex.every(Number.isFinite)) vertices.push(vertex);
          continue;
        }
        if (parts[0] !== "f" || parts.length < 4) continue;
        const indices = parts.slice(1).map((token) => {
          const rawIndex = Number.parseInt(token.split("/")[0], 10);
          if (!Number.isInteger(rawIndex) || rawIndex === 0) return null;
          return rawIndex > 0 ? rawIndex - 1 : vertices.length + rawIndex;
        });
        if (indices.some((index) => index === null || index < 0 || index >= vertices.length)) continue;
        for (let index = 1; index < indices.length - 1; index += 1) {
          for (const vertexIndex of [indices[0], indices[index], indices[index + 1]]) {
            positions.push(...vertices[vertexIndex]);
          }
        }
      }
      if (!positions.length) throw new Error("OBJ 文件没有可渲染的面片。");
      const geometry = new THREE.BufferGeometry();
      geometry.setAttribute("position", new THREE.Float32BufferAttribute(positions, 3));
      geometry.computeVertexNormals();
      geometry.rotateX(-Math.PI / 2);
      geometry.center();
      geometry.computeBoundingSphere();
      if (!geometry.boundingSphere || !Number.isFinite(geometry.boundingSphere.radius) || geometry.boundingSphere.radius <= 0) {
        geometry.dispose();
        throw new Error("OBJ 模型尺寸无效。");
      }
      return geometry;
    }

    async function mountDesignObjViewer(viewport, file) {
      const requestKey = resultFileKey(file);
      viewport.dataset.modelMounted = requestKey;
      try {
        if (!window.THREE || typeof THREE.WebGLRenderer !== "function" || typeof THREE.OrbitControls !== "function") {
          throw new Error("本地三维渲染组件未加载。");
        }
        const response = await fetch(file.preview_url);
        if (!response.ok) throw new Error("无法加载 OBJ 模型。");
        const geometry = parseDesignObjGeometry(await response.text());
        if (!viewport.isConnected || viewport.dataset.modelMounted !== requestKey) {
          geometry.dispose();
          return;
        }

        viewport.innerHTML = "";
        const renderer = new THREE.WebGLRenderer({ antialias: true, preserveDrawingBuffer: true });
        renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
        renderer.setClearColor(0xf1f4f2, 1);
        if ("outputEncoding" in renderer) renderer.outputEncoding = THREE.sRGBEncoding;
        renderer.domElement.setAttribute("role", "img");
        renderer.domElement.setAttribute("aria-label", `${file.name || "飞行器"} 三维模型`);
        viewport.appendChild(renderer.domElement);

        const scene = new THREE.Scene();
        const radius = geometry.boundingSphere.radius;
        const camera = new THREE.PerspectiveCamera(36, 1, Math.max(radius / 100, 0.001), radius * 100);
        camera.position.set(radius * 1.7, radius * 1.1, radius * 1.9);

        const material = new THREE.MeshStandardMaterial({
          color: 0x657a78,
          metalness: 0.12,
          roughness: 0.72,
          side: THREE.DoubleSide,
        });
        const mesh = new THREE.Mesh(geometry, material);
        scene.add(mesh);
        const edges = new THREE.LineSegments(
          new THREE.EdgesGeometry(geometry, 28),
          new THREE.LineBasicMaterial({ color: 0x33413f, transparent: true, opacity: 0.34 }),
        );
        scene.add(edges);
        scene.add(new THREE.HemisphereLight(0xffffff, 0x63706b, 1.45));
        const keyLight = new THREE.DirectionalLight(0xffffff, 1.2);
        keyLight.position.set(radius * 2, radius * 3, radius * 2);
        scene.add(keyLight);
        const fillLight = new THREE.DirectionalLight(0xb7d8d2, 0.55);
        fillLight.position.set(-radius * 2, radius, -radius);
        scene.add(fillLight);

        const controls = new THREE.OrbitControls(camera, renderer.domElement);
        controls.enableDamping = true;
        controls.dampingFactor = 0.07;
        controls.autoRotate = true;
        controls.autoRotateSpeed = 0.75;
        controls.minDistance = radius * 0.45;
        controls.maxDistance = radius * 12;
        controls.target.set(0, 0, 0);
        controls.update();
        controls.saveState();

        const resetButton = viewport.closest(".design-model-pane")?.querySelector("[data-model-reset]");
        const resetHandler = () => {
          controls.reset();
          controls.autoRotate = true;
        };
        if (resetButton) {
          resetButton.disabled = false;
          resetButton.addEventListener("click", resetHandler);
        }

        const resize = () => {
          const width = Math.max(viewport.clientWidth, 1);
          const height = Math.max(viewport.clientHeight, 1);
          renderer.setSize(width, height, false);
          camera.aspect = width / height;
          camera.updateProjectionMatrix();
        };
        const resizeObserver = new ResizeObserver(resize);
        resizeObserver.observe(viewport);
        resize();

        const viewer = {
          viewport,
          renderer,
          scene,
          camera,
          controls,
          resizeObserver,
          resetButton,
          resetHandler,
          frameId: 0,
        };
        state.designModelViewer = viewer;
        const animate = () => {
          if (state.designModelViewer !== viewer || !viewport.isConnected) return;
          controls.update();
          renderer.render(scene, camera);
          viewer.frameId = requestAnimationFrame(animate);
        };
        animate();
      } catch (error) {
        if (!viewport.isConnected || viewport.dataset.modelMounted !== requestKey) return;
        viewport.innerHTML = "";
        const failure = designNode("div", "design-empty-state is-error", error.message || "无法显示 OBJ 模型。");
        failure.setAttribute("role", "alert");
        viewport.appendChild(failure);
      }
    }

    function designImageLabel(file) {
      const name = String(file.path || file.name || file.filename || "").toLowerCase();
      const labels = [
        ["view_top", "外形俯视图"],
        ["threeview_top", "外形俯视图"],
        ["view_side", "外形侧视图"],
        ["threeview_side", "外形侧视图"],
        ["aero_cl_alpha", "升力曲线"],
        ["lift_curve", "升力曲线"],
        ["aero_drag_polar", "阻力极曲线"],
        ["drag_polar", "阻力极曲线"],
        ["perf_thrust", "推力曲线"],
        ["thrust_curve", "推力曲线"],
        ["perf_flight_envelope", "飞行包线"],
        ["flight_envelope", "飞行包线"],
        ["struct_vn", "V-n 图"],
        ["vn_diagram", "V-n 图"],
        ["weight_iteration", "重量收敛"],
        ["constraint", "约束边界"],
      ];
      return labels.find(([key]) => name.includes(key))?.[1] || file.name || file.filename || "工程结果图";
    }

    function sortDesignImages(files) {
      const priority = ["view_top", "view_side", "aero_cl", "aero_drag", "perf_thrust", "perf_flight", "struct_vn"];
      return [...files].sort((left, right) => {
        const leftName = String(left.path || left.name || "").toLowerCase();
        const rightName = String(right.path || right.name || "").toLowerCase();
        const rank = (name) => {
          const found = priority.findIndex((key) => name.includes(key));
          return found < 0 ? priority.length : found;
        };
        return rank(leftName) - rank(rightName) || leftName.localeCompare(rightName);
      });
    }

    function createDesignVisualizationSection(job) {
      const files = designResultFiles(job);
      const modelFile = files.find((file) => resultFileKind(file) === "model");
      const imageFiles = sortDesignImages(files.filter((file) => resultFileKind(file) === "image"));
      const section = createDesignSection("几何与工程图", "本轮计算生成的三维外形与配套分析图。" );
      section.dataset.testid = "design-visualization";
      const layout = designNode("div", "design-visualization-layout");

      const modelPane = designNode("div", "design-model-pane");
      const modelHeader = designNode("div", "design-visual-pane-header");
      modelHeader.appendChild(designNode("strong", "", modelFile ? modelFile.name || "geometry.obj" : "OBJ 三维模型"));
      const modelActions = designNode("div", "design-visual-actions");
      const resetButton = designNode("button", "icon-button design-model-reset", "↺");
      resetButton.type = "button";
      resetButton.title = "重置视角";
      resetButton.setAttribute("aria-label", "重置三维模型视角");
      resetButton.dataset.modelReset = "true";
      resetButton.disabled = true;
      modelActions.appendChild(resetButton);
      if (modelFile?.download_url) {
        const download = designNode("a", "secondary design-visual-download", "下载 OBJ");
        download.href = modelFile.download_url;
        download.download = modelFile.name || "geometry.obj";
        modelActions.appendChild(download);
      }
      modelHeader.appendChild(modelActions);
      modelPane.appendChild(modelHeader);
      const viewport = designNode("div", "design-model-viewport");
      if (modelFile?.preview_url) {
        viewport.dataset.modelPreviewUrl = modelFile.preview_url;
        viewport.dataset.modelName = modelFile.name || "geometry.obj";
        viewport.appendChild(designNode("div", "design-model-loading", "正在加载三维模型..."));
      } else {
        viewport.appendChild(designNode("div", "design-empty-state compact", "本轮结果没有生成 OBJ 模型。"));
      }
      modelPane.appendChild(viewport);
      layout.appendChild(modelPane);

      const imagePane = designNode("div", "design-image-pane");
      const imageHeader = designNode("div", "design-visual-pane-header");
      imageHeader.appendChild(designNode("strong", "", `工程图片${imageFiles.length ? ` · ${imageFiles.length}` : ""}`));
      imagePane.appendChild(imageHeader);
      if (!imageFiles.length) {
        imagePane.appendChild(designNode("div", "design-empty-state compact", "本轮结果没有生成可预览图片。"));
      } else {
        const stage = designNode("figure", "design-image-stage");
        const primary = document.createElement("img");
        primary.className = "design-gallery-primary";
        primary.src = imageFiles[0].preview_url;
        primary.alt = designImageLabel(imageFiles[0]);
        const caption = designNode("figcaption", "", designImageLabel(imageFiles[0]));
        stage.appendChild(primary);
        stage.appendChild(caption);
        imagePane.appendChild(stage);
        const thumbnails = designNode("div", "design-image-thumbnails");
        const selectImage = (file, button) => {
          primary.src = file.preview_url;
          primary.alt = designImageLabel(file);
          caption.textContent = designImageLabel(file);
          for (const candidate of thumbnails.querySelectorAll("button")) {
            const selected = candidate === button;
            candidate.classList.toggle("is-active", selected);
            candidate.setAttribute("aria-pressed", selected ? "true" : "false");
          }
        };
        imageFiles.forEach((file, index) => {
          const button = designNode("button", "design-image-thumbnail" + (index === 0 ? " is-active" : ""));
          button.type = "button";
          button.title = designImageLabel(file);
          button.setAttribute("aria-label", `查看${designImageLabel(file)}`);
          button.setAttribute("aria-pressed", index === 0 ? "true" : "false");
          const image = document.createElement("img");
          image.src = file.preview_url;
          image.alt = "";
          image.loading = "lazy";
          button.appendChild(image);
          button.addEventListener("click", () => selectImage(file, button));
          thumbnails.appendChild(button);
        });
        imagePane.appendChild(thumbnails);
      }
      layout.appendChild(imagePane);
      section.appendChild(layout);
      return section;
    }

    function activateDesignModelPreview() {
      if (state.view !== "design" || state.designTab !== "results" || state.designModelViewer) return;
      const viewport = designResultsContent.querySelector("[data-model-preview-url]");
      if (!viewport || viewport.dataset.modelMounted) return;
      void mountDesignObjViewer(viewport, {
        name: viewport.dataset.modelName || "geometry.obj",
        preview_url: viewport.dataset.modelPreviewUrl,
      });
    }

    function renderDesignResults() {
      disposeDesignModelViewer();
      designResultsContent.innerHTML = "";
      const job = state.activeDesignJob;
      if (!job) {
        designResultsContent.appendChild(designNode("div", "design-empty-state", "选择一个历史任务后查看工程结果。"));
        return;
      }
      const engineering = designEngineering(job);
      const outcome = designOutcome(job);
      const summary = job.result?.summary || {};
      const headline = designNode("section", "design-outcome is-" + outcome.tone);
      headline.dataset.testid = "design-outcome";
      headline.setAttribute("role", outcome.tone === "fail" ? "alert" : "status");
      const headlineCopy = designNode("div", "design-outcome-copy");
      headlineCopy.appendChild(designNode("span", "", "工程判定"));
      headlineCopy.appendChild(designNode("strong", "", outcome.label));
      headlineCopy.appendChild(designNode("p", "", outcome.detail));
      headline.appendChild(headlineCopy);
      const headlineStates = designNode("div", "design-outcome-states");
      const numerical = engineering.numerical_converged ?? job.result?.converged ?? null;
      const feasible = engineering.engineering_feasible ?? null;
      const blockingFailedCount = engineering.blocking_failed_count;
      headlineStates.appendChild(designStatusChip(numerical === true ? "数值已收敛" : numerical === false ? "数值未收敛" : "收敛状态未知", numerical === true ? "pass" : numerical === false ? "fail" : "warn"));
      const blockingPass = feasible === true && blockingFailedCount === 0;
      const blockingLabel = blockingPass
        ? "阻断约束已通过"
        : blockingFailedCount > 0
          ? `阻断项 ${blockingFailedCount} 项未通过`
          : feasible === false
            ? "工程约束未通过"
            : feasible === true
              ? "阻断项数量未知"
              : "可行性待判定";
      headlineStates.appendChild(designStatusChip(blockingLabel, blockingPass ? "pass" : feasible === false || blockingFailedCount > 0 ? "fail" : "warn"));
      if (outcome.validationGaps?.length) {
        headlineStates.appendChild(designStatusChip(`专项验证缺口 ${outcome.validationGaps.length} 项`, "warn"));
      }
      headline.appendChild(headlineStates);
      designResultsContent.appendChild(headline);

      if (outcome.validationGaps?.length) {
        const gapSection = createDesignSection(
          "专项验证缺口",
          "以下要求仍保留在需求基线中，但当前总体模型尚未完成对应专项验证。",
        );
        gapSection.dataset.testid = "design-validation-gaps";
        const rows = outcome.validationGaps.map((gap) => ({
          className: "is-warn",
          cells: [
            requirementFieldLabel(gap.path),
            formatDesignValue(
              gap.value,
              requirementUnitLabel(gap.unit, gap.path) === "--"
                ? ""
                : requirementUnitLabel(gap.unit, gap.path),
            ),
            localizeCoverageReason(gap.path, gap.reason) || "--",
            [gap.scopeStatement, gap.source ? "来源：" + gap.source : ""].filter(Boolean).join(" · ") || "--",
          ],
        }));
        gapSection.appendChild(createDesignTable(["字段", "保留值", "覆盖原因", "范围说明 / 来源"], rows));
        designResultsContent.appendChild(gapSection);
      }

      const metricSection = createDesignSection("关键设计点");
      const metricData = [
        ["最大起飞重量", summary.mtow_kg, "kg", 1],
        ["机翼面积", summary.wing_area_m2, "m²", 2],
        ["翼载", engineering.design_point?.wing_loading_pa ?? summary.wing_loading_pa, "Pa", 0],
        ["推重比", engineering.design_point?.thrust_to_weight ?? summary.thrust_to_weight, "", 3],
        ["海平面推力", summary.thrust_sl_n, "N", 0],
        ["翼展", summary.span_m, "m", 2],
        [designRangeMetricLabel(summary.range_metric_kind), finiteDesignNumber(summary.actual_range_m) === null ? null : Number(summary.actual_range_m) / 1000, "km", 1],
        ["迭代次数", summary.iterations, "次", 0],
      ];
      const metrics = designNode("div", "design-result-metrics workspace-metrics");
      for (const [label, value, unit, digits] of metricData) {
        const metric = designNode("div", "design-result-metric");
        metric.appendChild(designNode("span", "", label));
        metric.appendChild(designNode("strong", "", formatDesignValue(value, unit, digits)));
        metrics.appendChild(metric);
      }
      metricSection.appendChild(metrics);
      designResultsContent.appendChild(metricSection);

      designResultsContent.appendChild(createDesignVisualizationSection(job));

      const autoRepair = engineering.provenance?.auto_repair;
      if (autoRepair && typeof autoRepair === "object") {
        const repairSection = createDesignSection("有界自动修正");
        const repairState = designNode("div", "design-outcome-states");
        const repairAttempts = Number(autoRepair.attempts_executed || 0);
        const repairSucceeded = autoRepair.succeeded_after_repair === true;
        repairState.appendChild(designStatusChip(
          repairAttempts === 0 ? "未触发" : `已执行 ${repairAttempts} 轮`,
          repairAttempts === 0 ? "warn" : repairSucceeded ? "pass" : "fail",
        ));
        repairState.appendChild(designStatusChip(
          autoRepair.requirements_changed === false ? "用户需求未修改" : "需求发生变化",
          autoRepair.requirements_changed === false ? "pass" : "fail",
        ));
        repairSection.appendChild(repairState);
        const rows = [];
        for (const record of autoRepair.history || []) {
          for (const action of record.actions || []) {
            rows.push({
              className: record.result_status === "completed" ? "is-pass" : "is-warn",
              cells: [
                record.repair_attempt,
                requirementFieldLabel(action.path),
                formatRepairValue(action.from),
                formatRepairValue(action.to),
                (action.trigger_constraint_ids || []).map((id) => designConstraintLabel({ id })).join("、") || "--",
              ],
            });
          }
        }
        if (rows.length) repairSection.appendChild(createDesignTable(["轮次", "参数", "原值", "新值", "触发约束"], rows));
        designResultsContent.appendChild(repairSection);
      }

      const constraints = normalizeDesignConstraints(engineering.constraints);
      const constraintSection = createDesignSection("约束裕度", constraints.length ? "正裕度表示满足当前约束；阻断项未通过时方案不可行。" : "");
      if (constraints.length) {
        const rows = constraints.map((item) => {
          const passed = item.passed;
          const tone = passed === true ? "pass" : passed === false ? "fail" : "warn";
          const label = designConstraintLabel(item);
          const constraintName = designNode("div", "design-constraint-name");
          constraintName.appendChild(designNode("strong", "", label));
          if (item.blocking) constraintName.appendChild(designNode("small", "", "阻断约束"));
          const marginText = formatConstraintMargin(item);
          const ratio = finiteDesignNumber(item.margin_ratio);
          return {
            className: "is-" + tone,
            cells: [
              constraintName,
              stageDisplayName(item.stage || item.category),
              formatConstraintRequirement(item),
              formatDesignValue(item.actual, item.unit),
              marginText + (ratio === null ? "" : ` (${(ratio * 100).toFixed(1)}%)`),
              designStatusChip(passed === true ? "通过" : passed === false ? "未通过" : "待判定", tone),
            ],
          };
        });
        const constraintTable = createDesignTable(["约束", "阶段", "要求", "实际", "裕度", "判定"], rows);
        constraintTable.dataset.testid = "design-constraints-table";
        constraintSection.appendChild(constraintTable);
      } else {
        constraintSection.appendChild(designNode("div", "design-empty-state compact", "该任务未输出逐项约束，不能仅凭任务完成状态判断工程可行。"));
      }
      designResultsContent.appendChild(constraintSection);

      const stages = normalizeDesignStages(engineering.stage_status);
      const stageSection = createDesignSection("阶段门");
      if (stages.length) {
        const grid = designNode("div", "design-stage-grid");
        for (const stage of stages) {
          const rawStatus = String(stage.status || "unknown").toLowerCase();
          const tone = ["passed", "pass", "completed", "feasible"].includes(rawStatus) ? "pass" : ["failed", "fail", "infeasible", "not_converged", "nonconverged", "error"].includes(rawStatus) ? "fail" : "warn";
          const item = designNode("div", "design-stage-item is-" + tone);
          item.appendChild(designNode("span", "", stageDisplayName(stage.name || stage.id)));
          item.appendChild(designStatusChip(designStageStatusLabel(rawStatus), tone));
          if (stage.message || stage.error) item.appendChild(designNode("p", "", localizedStageMessage(stage.message || stage.error, rawStatus)));
          grid.appendChild(item);
        }
        stageSection.appendChild(grid);
      } else {
        stageSection.appendChild(designNode("div", "design-empty-state compact", "该任务未输出阶段门状态。"));
      }
      designResultsContent.appendChild(stageSection);

      const history = engineering.iteration_history || job.result?.iteration_history || [];
      const convergenceSection = createDesignSection("收敛历史");
      convergenceSection.appendChild(createConvergenceChart(history));
      designResultsContent.appendChild(convergenceSection);

      const comparisons = normalizeDesignConstraints(engineering.requirement_comparisons);
      const requirementSection = createDesignSection("需求与实际");
      if (comparisons.length) {
        const rows = comparisons.map((item) => ({
          className: item.passed === true ? "is-pass" : item.passed === false ? "is-fail" : "is-warn",
          cells: [
            designConstraintLabel(item),
            formatConstraintRequirement(item),
            formatDesignValue(item.actual, item.unit),
            formatConstraintMargin(item),
            designStatusChip(item.passed === true ? "满足" : item.passed === false ? "不满足" : "待判定", item.passed === true ? "pass" : item.passed === false ? "fail" : "warn"),
          ],
        }));
        requirementSection.appendChild(createDesignTable(["指标", "需求", "实际", "裕度", "判定"], rows));
      } else {
        requirementSection.appendChild(designNode("div", "design-empty-state compact", "该任务未输出独立回算的需求对比。"));
      }
      designResultsContent.appendChild(requirementSection);

      const recommendations = [...new Set([
        ...(Array.isArray(engineering.recommendations) ? engineering.recommendations : []),
        ...(Array.isArray(engineering.diagnostic_recommendations) ? engineering.diagnostic_recommendations : []),
      ].map(localizedEngineeringRecommendation))];
      if (recommendations.length) {
        const recommendationSection = createDesignSection("诊断与下一步");
        const list = designNode("ol", "design-recommendations");
        for (const recommendation of recommendations) list.appendChild(designNode("li", "", String(recommendation)));
        recommendationSection.appendChild(list);
        designResultsContent.appendChild(recommendationSection);
      }

      const provenance = engineering.provenance;
      if (provenance && typeof provenance === "object" && Object.keys(provenance).length) {
        const provenanceSection = createDesignSection("结果追溯");
        const list = designNode("dl", "design-provenance");
        for (const [key, value] of Object.entries(provenance)) {
          list.appendChild(designNode("dt", "", designProvenanceLabel(key)));
          list.appendChild(designNode("dd", "", formatDesignProvenanceValue(value)));
        }
        provenanceSection.appendChild(list);
        designResultsContent.appendChild(provenanceSection);
      }
      requestAnimationFrame(activateDesignModelPreview);
    }

    function designJobById(jobId) {
      return state.designJobDetails[jobId] || state.designJobs.find((job) => job.job_id === jobId) || null;
    }

    async function fetchDesignJobDetail(jobId) {
      const cached = state.designJobDetails[jobId];
      if (cached) return cached;
      const payload = await api("/api/design-jobs/" + encodeURIComponent(jobId));
      if (payload.job) state.designJobDetails[jobId] = payload.job;
      return payload.job || null;
    }

    function loadDesignForAdjustment(job) {
      if (!job?.request) return;
      applyDesignJobRequest(job.request);
      markDesignPreflightDirty();
      setActiveView("design");
      setDesignTab("requirements", { focus: true });
      designProjectName.focus();
      scheduleDesignPreflight();
      setStatus("已载入 " + (job.request.project_name || job.job_id) + "，修改需求并重新确认后即可运行。" );
    }

    function renderDesignCompareSelector() {
      designCompareSelector.innerHTML = "";
      if (state.designJobs.length < 2) {
        designCompareSelector.appendChild(designNode("div", "design-empty-state compact", "当前对话只有一个结果版本，无需进行历史对比。"));
        return;
      }
      state.compareJobIds = state.compareJobIds.filter((jobId) => state.designJobs.some((job) => job.job_id === jobId));
      const selectedCount = state.compareJobIds.length;
      for (const job of state.designJobs.slice(0, 20)) {
        const selected = state.compareJobIds.includes(job.job_id);
        const row = designNode("div", "design-compare-option" + (selected ? " is-selected" : ""));
        const label = document.createElement("label");
        const checkbox = document.createElement("input");
        checkbox.type = "checkbox";
        checkbox.checked = selected;
        checkbox.disabled = !selected && selectedCount >= 4;
        checkbox.value = job.job_id;
        const copy = designNode("span", "design-compare-option-copy");
        copy.appendChild(designNode("strong", "", job.request?.project_name || "未命名设计"));
        copy.appendChild(designNode("small", "", designJobTimestamp(job.finished_at || job.created_at) + " · " + designOutcome(job).label));
        label.appendChild(checkbox);
        label.appendChild(copy);
        checkbox.addEventListener("change", () => {
          if (checkbox.checked) {
            if (state.compareJobIds.length >= 4) {
              checkbox.checked = false;
              return;
            }
            state.compareJobIds.push(job.job_id);
          } else {
            state.compareJobIds = state.compareJobIds.filter((jobId) => jobId !== job.job_id);
          }
          renderDesignCompareSelector();
          renderDesignComparison();
        });
        row.appendChild(label);
        designCompareSelector.appendChild(row);
      }
    }

    function compareMetricValue(job, key) {
      const summary = job?.result?.summary || {};
      if (key === "actual_range_km") {
        const value = finiteDesignNumber(summary.actual_range_m);
        return value === null ? null : value / 1000;
      }
      if (key === "wing_loading_pa") return finiteDesignNumber(designEngineering(job).design_point?.wing_loading_pa ?? summary.wing_loading_pa);
      if (key === "thrust_to_weight") return finiteDesignNumber(designEngineering(job).design_point?.thrust_to_weight ?? summary.thrust_to_weight);
      return finiteDesignNumber(summary[key]);
    }

    function formatDesignDelta(value, baseline, unit, digits) {
      if (value === null || baseline === null) return "--";
      const delta = value - baseline;
      const sign = delta > 0 ? "+" : "";
      return formatDesignValue(value, unit, digits) + " (Δ " + sign + formatDesignValue(delta, unit, digits) + ")";
    }

    function renderDesignComparison() {
      designCompareContent.innerHTML = "";
      const jobs = state.compareJobIds.map(designJobById).filter(Boolean);
      if (jobs.length < 2) {
        designCompareContent.appendChild(designNode("div", "design-empty-state", "至少选择两个任务开始对比。"));
        return;
      }
      const headline = createDesignSection("工程判定对比", "第一列为基准方案。" );
      const outcomeRows = [{
        cells: ["工程状态", ...jobs.map((job) => designStatusChip(designOutcome(job).label, designOutcome(job).tone))],
      }];
      headline.appendChild(createDesignTable(["项目", ...jobs.map((job, index) => (index === 0 ? "基准 · " : "") + (job.request?.project_name || job.job_id))], outcomeRows));
      designCompareContent.appendChild(headline);

      const rangeKinds = jobs.map((job) => job.result?.summary?.range_metric_kind);
      const rangeLabel = rangeKinds.every((kind) => kind === rangeKinds[0])
        ? designRangeMetricLabel(rangeKinds[0])
        : "航程指标（证据类型不同）";
      const metrics = [
        ["mtow_kg", "最大起飞重量", "kg", 1],
        ["empty_weight_kg", "空重", "kg", 1],
        ["fuel_weight_kg", "燃油重量", "kg", 1],
        ["wing_area_m2", "机翼面积", "m²", 2],
        ["wing_loading_pa", "翼载", "Pa", 0],
        ["thrust_to_weight", "推重比", "", 3],
        ["span_m", "翼展", "m", 2],
        ["actual_range_km", rangeLabel, "km", 1],
      ];
      const metricRows = metrics.map(([key, label, unit, digits]) => {
        const values = jobs.map((job) => compareMetricValue(job, key));
        return {
          cells: [label, formatDesignValue(values[0], unit, digits), ...values.slice(1).map((value) => formatDesignDelta(value, values[0], unit, digits))],
        };
      });
      const metricSection = createDesignSection("参数差值");
      metricSection.appendChild(createDesignTable(["参数", ...jobs.map((job, index) => index === 0 ? "基准值" : job.request?.project_name || `方案 ${index + 1}`)], metricRows, "design-delta-table"));
      designCompareContent.appendChild(metricSection);

      const constraintIds = [];
      const constraintMaps = jobs.map((job) => {
        const map = new Map();
        for (const constraint of normalizeDesignConstraints(designEngineering(job).constraints)) {
          const id = constraint.id || constraint.label || constraint.name;
          if (id && !constraintIds.includes(id)) constraintIds.push(id);
          if (id) map.set(id, constraint);
        }
        return map;
      });
      if (constraintIds.length) {
        const constraintRows = constraintIds.map((id) => {
          const label = designConstraintLabel(
            constraintMaps.map((map) => map.get(id)).find(Boolean) || { id },
          );
          return {
            cells: [label, ...constraintMaps.map((map) => {
              const constraint = map.get(id);
              if (!constraint) return "--";
              const tone = constraint.passed === true ? "pass" : constraint.passed === false ? "fail" : "warn";
              const copy = designNode("span", "design-margin-value is-" + tone, formatConstraintMargin(constraint));
              return copy;
            })],
          };
        });
        const constraintSection = createDesignSection("约束裕度对比");
        constraintSection.appendChild(createDesignTable(["约束", ...jobs.map((job) => job.request?.project_name || job.job_id)], constraintRows));
        designCompareContent.appendChild(constraintSection);
      }
    }

    function designResultFiles(job) {
      const candidates = job?.result_files || job?.result?.result_files || job?.result?.files || [];
      return Array.isArray(candidates) ? candidates : [];
    }

    function resultFileKey(file) {
      return file.id || file.preview_url || file.download_url || file.name || file.filename;
    }

    function resultFileKind(file) {
      const declared = String(file.kind || file.format || "").toLowerCase();
      const name = String(file.name || file.filename || "").toLowerCase();
      if (declared.includes("image") || /\.(png|jpe?g|webp|gif)$/.test(name)) return "image";
      if (declared.includes("model") || declared === "obj" || name.endsWith(".obj")) return "model";
      if (declared.includes("markdown") || declared === "md" || name.endsWith(".md")) return "markdown";
      if (declared.includes("html") || name.endsWith(".html")) return "html";
      if (declared.includes("json") || name.endsWith(".json")) return "json";
      if (declared.includes("text") || /\.(txt|log|csv)$/.test(name)) return "text";
      return "download";
    }

    function resultFileKindLabel(kind) {
      return ({
        image: "图片",
        model: "三维模型",
        markdown: "设计报告",
        html: "交互式报告",
        json: "结构化数据",
        text: "文本数据",
        download: "结果文件",
      })[kind] || "结果文件";
    }

    function renderDesignReports() {
      designReportList.innerHTML = "";
      const job = state.activeDesignJob;
      const files = designResultFiles(job);
      if (!job) {
        designReportList.appendChild(designNode("div", "design-empty-state compact", "选择一个任务后查看报告。"));
        designReportPreview.innerHTML = "";
        delete designReportPreview.dataset.fileKey;
        designReportPreview.appendChild(designNode("div", "design-empty-state", "选择文件后在这里预览。"));
        return;
      }
      if (!files.length) {
        designReportList.appendChild(designNode("div", "design-empty-state compact", "该任务尚未提供可预览文件。"));
      }
      if (files.length && !files.some((file) => resultFileKey(file) === state.selectedResultFile)) {
        state.selectedResultFile = resultFileKey(files[0]);
      }
      for (const file of files) {
        const key = resultFileKey(file);
        const button = designNode("button", "design-report-item" + (state.selectedResultFile === key ? " is-active" : ""));
        button.type = "button";
        button.appendChild(designNode("strong", "", file.name || file.filename || "结果文件"));
        button.appendChild(designNode("span", "", resultFileKindLabel(resultFileKind(file)) + (file.size_bytes ? " · " + formatBytes(file.size_bytes) : "")));
        button.addEventListener("click", () => {
          state.selectedResultFile = key;
          renderDesignReports();
        });
        designReportList.appendChild(button);
      }
      for (const artifact of job.artifacts || []) {
        if (!artifact.download_url) continue;
        const link = designNode("a", "design-report-download");
        link.href = artifact.download_url;
        link.download = artifact.filename || "";
        link.appendChild(designNode("strong", "", artifact.name || "完整结果包"));
        link.appendChild(designNode("span", "", "下载 " + (artifact.format || "文件") + (artifact.size_bytes ? " · " + formatBytes(artifact.size_bytes) : "")));
        designReportList.appendChild(link);
      }
      const selected = files.find((file) => resultFileKey(file) === state.selectedResultFile);
      if (selected && designReportPreview.dataset.fileKey !== resultFileKey(selected)) {
        void previewDesignResultFile(selected);
      } else if (!files.length) {
        designReportPreview.innerHTML = "";
        delete designReportPreview.dataset.fileKey;
        designReportPreview.appendChild(designNode("div", "design-empty-state", "报告预览接口尚未提供，可下载完整结果包。"));
      }
    }

    async function previewDesignResultFile(file) {
      disposeDesignModelViewer();
      const key = resultFileKey(file);
      designReportPreview.innerHTML = "";
      designReportPreview.dataset.fileKey = key;
      const toolbar = designNode("div", "design-report-preview-header");
      toolbar.appendChild(designNode("strong", "", file.name || file.filename || "结果预览"));
      if (file.download_url) {
        const download = designNode("a", "secondary", "下载");
        download.href = file.download_url;
        download.download = file.filename || "";
        toolbar.appendChild(download);
      }
      designReportPreview.appendChild(toolbar);
      const kind = resultFileKind(file);
      const previewUrl = file.preview_url;
      if (!previewUrl && file.content === undefined) {
        designReportPreview.appendChild(designNode("div", "design-empty-state", "该文件不支持在线预览。"));
        return;
      }
      try {
        if (kind === "image") {
          const image = document.createElement("img");
          image.src = previewUrl;
          image.alt = file.name || file.filename || "工程结果图";
          image.className = "design-report-image";
          image.addEventListener("error", () => {
            if (state.selectedResultFile !== key) return;
            delete designReportPreview.dataset.fileKey;
            image.replaceWith(designNode("div", "design-empty-state is-error", "无法加载图片预览，可使用下载链接查看文件。"));
          }, { once: true });
          designReportPreview.appendChild(image);
          return;
        }
        if (kind === "model") {
          const viewport = designNode("div", "design-model-viewport design-report-model");
          viewport.dataset.modelPreviewUrl = previewUrl;
          viewport.dataset.modelName = file.name || file.filename || "geometry.obj";
          viewport.appendChild(designNode("div", "design-model-loading", "正在加载三维模型..."));
          designReportPreview.appendChild(viewport);
          await mountDesignObjViewer(viewport, file);
          return;
        }
        if (kind === "html") {
          const frame = document.createElement("iframe");
          frame.src = previewUrl;
          frame.title = file.name || file.filename || "交互式工程报告";
          frame.className = "design-report-frame";
          frame.setAttribute("sandbox", "allow-scripts");
          designReportPreview.appendChild(frame);
          return;
        }
        let content = file.content;
        if (content === undefined) {
          const response = await fetch(previewUrl);
          if (!response.ok) throw new Error("无法加载文件预览。");
          content = kind === "json" ? await response.json() : await response.text();
        }
        if (state.selectedResultFile !== key) return;
        if (kind === "markdown") {
          const article = designNode("article", "design-report-markdown bubble");
          renderMarkdownInto(article, String(content || ""));
          designReportPreview.appendChild(article);
        } else {
          const pre = designNode("pre", "design-report-code");
          pre.textContent = typeof content === "string" ? content : JSON.stringify(content, null, 2);
          designReportPreview.appendChild(pre);
        }
      } catch (error) {
        if (state.selectedResultFile !== key) return;
        delete designReportPreview.dataset.fileKey;
        const failure = designNode("div", "design-empty-state is-error", error.message);
        failure.setAttribute("role", "alert");
        designReportPreview.appendChild(failure);
      }
    }

    function renderDesignJobHistory() {
      if (!designJobHistoryList) {
        renderDesignCompareSelector();
        return;
      }
      designJobHistoryList.innerHTML = "";
      if (!state.designJobs.length) {
        const empty = document.createElement("div");
        empty.className = "design-job-history-empty";
        empty.textContent = "暂无总体设计任务。";
        designJobHistoryList.appendChild(empty);
        return;
      }
      for (const job of state.designJobs.slice(0, 12)) {
        const button = document.createElement("button");
        button.type = "button";
        button.className = "design-job-history-row" + (job.job_id === state.designJobId ? " is-active" : "");
        button.dataset.jobId = job.job_id;
        button.title = "打开任务 " + job.job_id;

        const copy = document.createElement("span");
        copy.className = "design-job-history-copy";
        const title = document.createElement("strong");
        title.textContent = job.request?.project_name || "未命名设计";
        const requirements = job.request?.requirements || {};
        const meta = document.createElement("span");
        const rangeKm = Number(requirements.range_m) / 1000;
        meta.textContent = [
          Number.isFinite(rangeKm) ? rangeKm.toFixed(0) + " km" : "航程未知",
          Number.isFinite(requirements.payload_kg) ? requirements.payload_kg.toFixed(0) + " kg" : "载荷未知",
          designJobTimestamp(job.finished_at || job.created_at),
        ].join(" · ");
        copy.appendChild(title);
        copy.appendChild(meta);

        const outcome = designOutcome(job);
        const status = document.createElement("span");
        status.className = "design-job-history-status is-" + outcome.tone;
        status.textContent = outcome.label;
        button.appendChild(copy);
        button.appendChild(status);
        button.addEventListener("click", async () => {
          setActiveView("design");
          setDesignTab(job.terminal ? "results" : "run", { focus: true });
          try {
            await openDesignJob(job.job_id, { renderResult: false, monitor: true });
          } catch (error) {
            setStatus(error.message, true);
          }
        });
        designJobHistoryList.appendChild(button);
      }
      renderDesignCompareSelector();
    }

    function applyDesignJobRequest(request) {
      if (!request) return;
      resetDesignEnergyValues();
      restoreDesignFieldSources(request.provenance);
      const requirements = request.requirements || {};
      designProjectName.value = request.project_name || "uav_design";
      if (Number.isFinite(requirements.range_m)) designRangeKm.value = requirements.range_m / 1000;
      if (Number.isFinite(requirements.payload_kg)) designPayloadKg.value = requirements.payload_kg;
      if (Number.isFinite(requirements.cruise_mach)) designCruiseMach.value = requirements.cruise_mach;
      if (Number.isFinite(requirements.cruise_altitude_m)) designCruiseAltitude.value = requirements.cruise_altitude_m;
      if (Number.isFinite(requirements.takeoff_distance_m)) designTakeoffDistance.value = requirements.takeoff_distance_m;
      if (Number.isFinite(requirements.landing_distance_m)) designLandingDistance.value = requirements.landing_distance_m;
      if (Number.isFinite(requirements.max_load_factor)) designMaxLoadFactor.value = requirements.max_load_factor;
      if (Number.isFinite(requirements.sustained_turn_g)) designSustainedTurnG.value = requirements.sustained_turn_g;
      if (Number.isFinite(requirements.service_ceiling_m)) designServiceCeiling.value = requirements.service_ceiling_m;
      if (requirements.aircraft_role) designAircraftRole.value = requirements.aircraft_role;
      if (requirements.propulsion_type) designPropulsionType.value = requirements.propulsion_type;
      const reserveFraction = requirements.reserve_fraction ?? requirements.reserve_fuel_fraction;
      if (Number.isFinite(reserveFraction)) designReserveFraction.value = reserveFraction;
      if (requirements.tail_layout) designTailLayout.value = requirements.tail_layout;
      const clmaxTakeoff = requirements.cl_max_takeoff ?? requirements.clmax_takeoff;
      const clmaxLanding = requirements.cl_max_landing ?? requirements.clmax_landing;
      if (Number.isFinite(clmaxTakeoff)) designClmaxTakeoff.value = clmaxTakeoff;
      if (Number.isFinite(clmaxLanding)) designClmaxLanding.value = clmaxLanding;
      if (Number.isFinite(requirements.assumed_climb_rate_m_s)) designAssumedClimbRate.value = requirements.assumed_climb_rate_m_s;
      const uncertainty = requirements.uncertainty_enabled ?? requirements.allow_uncertainty;
      if (typeof uncertainty === "boolean") designUncertaintyEnabled.checked = uncertainty;
      if (typeof request.auto_repair_enabled === "boolean") designAutoRepairEnabled.checked = request.auto_repair_enabled;
      if (Number.isFinite(request.max_repair_attempts)) designMaxRepairAttempts.value = request.max_repair_attempts;
      const initial = request.initial_guess;
      if (initial) {
        const initialSources = request.provenance?.input_fields?.initial_guess || {};
        const provenanceExplicit = Object.values(initialSources).some((entry) => (typeof entry === "string" ? entry : entry?.source) === "user");
        const useAdvanced = request.provenance?.ui?.custom_initial_guess ?? (request.provenance ? provenanceExplicit : true);
        designUseAdvanced.checked = Boolean(useAdvanced);
        designAdvancedPanel.open = Boolean(useAdvanced);
        if (Number.isFinite(initial.mtow_kg)) designMtowGuess.value = initial.mtow_kg;
        if (Number.isFinite(initial.wing_loading_pa)) designWingLoading.value = initial.wing_loading_pa;
        if (Number.isFinite(initial.thrust_to_weight)) designThrustWeight.value = initial.thrust_to_weight;
        if (Number.isFinite(initial.aspect_ratio)) designAspectRatio.value = initial.aspect_ratio;
        if (Number.isFinite(initial.sweep_deg)) designSweepDeg.value = initial.sweep_deg;
        if (Number.isFinite(initial.taper_ratio)) designTaperRatio.value = initial.taper_ratio;
        if (Number.isFinite(initial.thickness_ratio)) designThicknessRatio.value = initial.thickness_ratio;
        if (Number.isFinite(initial.prop_efficiency)) designPropEfficiency.value = initial.prop_efficiency;
        for (const mode of ["prop", "jet"]) {
          const field = DESIGN_ENERGY_CONFIG[mode].field;
          if (Number.isFinite(initial[field])) state.designEnergyValues[mode] = initial[field];
        }
        const energyMode = currentDesignEnergyMode();
        const energyField = DESIGN_ENERGY_CONFIG[energyMode].field;
        const energyProvenance = request.provenance?.propulsion_energy;
        const migratedCanonical = Number.isFinite(initial[energyField])
          && energyProvenance?.canonical_field === energyField
          && (
            energyProvenance?.source === "legacy_migrated_at_cruise_condition"
            || energyProvenance?.source === "legacy_sfc_cruise_1_s_migrated"
            || energyProvenance?.legacy_field === "sfc_cruise_1_s"
          );
        if (migratedCanonical) {
          state.designLegacyEnergy[energyMode] = energyProvenance.legacy_field || true;
        }
        if (!Number.isFinite(initial[energyField]) && Number.isFinite(initial.sfc_cruise_1_s)) {
          const migrated = migrateLegacyDesignSfc(initial.sfc_cruise_1_s, energyMode);
          if (Number.isFinite(migrated)) {
            state.designEnergyValues[energyMode] = migrated;
            state.designLegacyEnergy[energyMode] = initial.sfc_cruise_1_s;
            const legacyEntry = initialSources.sfc_cruise_1_s;
            const legacySource = typeof legacyEntry === "string" ? legacyEntry : legacyEntry?.source;
            state.designFieldSources[designEnergyPath(energyMode)] = ["user", "default", "derived"].includes(legacySource)
              ? legacySource
              : "user";
          }
        }
        if (Number.isFinite(initial.cd0)) designCd0.value = initial.cd0;
        if (Number.isFinite(initial.oswald_e)) designOswald.value = initial.oswald_e;
        if (Number.isFinite(initial.cg_fraction_cbar)) designCgFraction.value = initial.cg_fraction_cbar;
        if (Number.isFinite(initial.horizontal_tail_volume_coefficient)) designTailVolume.value = initial.horizontal_tail_volume_coefficient;
        if (Number.isFinite(request.tolerance)) designTolerance.value = request.tolerance;
        if (Number.isFinite(request.max_iterations)) designMaxIterations.value = request.max_iterations;
      }
      syncDesignEnergyMode({ captureCurrent: false });
      syncAdvancedInputs();
      syncAutoRepairInputs();
      markDesignPreflightDirty();
    }

    function syncAdvancedInputs() {
      for (const input of designRunForm.querySelectorAll("[data-design-advanced]")) {
        input.disabled = state.designJobRunning || !designUseAdvanced.checked;
      }
      if (designUseAdvanced.checked) designAdvancedPanel.open = true;
      syncDesignEnergyMode();
    }

    function syncAutoRepairInputs() {
      designMaxRepairAttempts.disabled = state.designJobRunning || !designAutoRepairEnabled.checked;
    }

    async function refreshDesignJobs(options = {}) {
      try {
        const payload = await api("/api/design-jobs");
        state.designJobs = payload.jobs || [];
        renderDesignJobHistory();
        if (!options.restoreLatest || !state.designJobs.length) return;
        const preferredId = options.preferredJobId || state.designJobId;
        const selected = state.designJobs.find((job) => job.job_id === preferredId) || state.designJobs[0];
        await openDesignJob(selected.job_id, { renderResult: true, monitor: true, restoring: true });
      } catch (error) {
        state.designJobs = [];
        renderDesignJobHistory();
        if (!options.silent) setStatus("无法刷新总体设计任务，请稍后重试。", true);
      }
    }

    async function openDesignJob(jobId, options = {}) {
      state.designStreamController?.abort();
      state.designStreamController = null;
      const payload = await api("/api/design-jobs/" + encodeURIComponent(jobId));
      const job = payload.job;
      const previousJobId = state.activeDesignJob?.job_id;
      state.designJobId = job.job_id;
      state.activeDesignJob = job;
      state.designJobDetails[job.job_id] = job;
      if (previousJobId !== job.job_id) state.selectedResultFile = null;
      state.designJobSequence = job.last_sequence || 0;
      state.designJobEvents = (job.events || []).map(designProgressEvent);
      if (state.designJobMessage) state.designJobMessage.remove();
      state.designJobMessage = null;
      applyDesignJobRequest(job.request);
      designProgress.value = job.progress || 0;
      designRunStatus.textContent = localizedJobMessage(job.message, job.status) || designJobStatusLabel(job.status);
      saveLocalState();
      renderDesignJobHistory();
      renderDesignWorkspace();

      if (!job.terminal) {
        setDesignRunBusy(true, localizedJobMessage(job.message, job.status) || "正在恢复任务");
        refreshDesignJobMessage();
        if (options.monitor !== false) void monitorDesignJob(job.job_id);
        return job;
      }

      setDesignRunBusy(false);
      designRetryBtn.disabled = false;
      if (options.renderResult !== false && state.renderedDesignJobId !== job.job_id) {
        appendAssistantReply(
          { text: designResultText(job), artifacts: job.artifacts || [] },
          { events: state.designJobEvents, artifacts: job.artifacts || [], designJob: job, openProcess: false },
        );
        state.renderedDesignJobId = job.job_id;
      }
      if (options.restoring) {
        const outcome = designOutcome(job);
        setStatus("已恢复最近一次总体设计任务：" + outcome.label + "。", outcome.tone === "fail");
      }
      return job;
    }

    async function streamDesignJob(jobId, afterSequence, signal) {
      const streamPath = "/api/design-jobs/" + encodeURIComponent(jobId) + "/stream?after=" + afterSequence;
      const response = await fetch(streamPath, { signal });
      if (!response.ok || !response.body) throw new Error("无法连接设计任务进度流。");
      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";
      let completed = null;
      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const blocks = buffer.split("\n\n");
        buffer = blocks.pop() || "";
        for (const block of blocks) {
          const parsed = parseSseBlock(block);
          if (!parsed) continue;
          if (parsed.event === "progress") {
            if ((parsed.data.sequence || 0) <= state.designJobSequence) continue;
            state.designJobSequence = parsed.data.sequence || state.designJobSequence;
            if (designProgress) designProgress.value = parsed.data.progress || 0;
            if (designRunStatus) designRunStatus.textContent = localizedJobMessage(
              parsed.data.message,
              parsed.data.stage || "running",
            ) || "正在计算";
            state.designJobEvents.push(designProgressEvent(parsed.data));
            refreshDesignJobMessage();
            renderDesignRunTimeline();
          }
          if (parsed.event === "error") throw new Error(parsed.data.error || "设计任务进度流失败。");
          if (parsed.event === "done") {
            completed = parsed.data;
            await reader.cancel().catch(() => {});
            break;
          }
        }
        if (completed) break;
      }
      if (!completed) throw new Error("设计任务在返回结果前中断。");
      return completed;
    }

    function waitForDesignPoll(delayMs, signal) {
      return new Promise((resolve, reject) => {
        if (signal.aborted) {
          reject(new DOMException("Aborted", "AbortError"));
          return;
        }
        const timer = window.setTimeout(() => {
          signal.removeEventListener("abort", onAbort);
          resolve();
        }, delayMs);
        const onAbort = () => {
          window.clearTimeout(timer);
          reject(new DOMException("Aborted", "AbortError"));
        };
        signal.addEventListener("abort", onAbort, { once: true });
      });
    }

    async function pollDesignJobUntilTerminal(jobId, signal) {
      let transientFailures = 0;
      while (!signal.aborted && state.designJobId === jobId) {
        try {
          const payload = await api("/api/design-jobs/" + encodeURIComponent(jobId), { signal });
          const job = payload.job;
          transientFailures = 0;
          state.activeDesignJob = job;
          state.designJobDetails[job.job_id] = job;
          state.designJobSequence = job.last_sequence || state.designJobSequence;
          state.designJobEvents = (job.events || []).map(designProgressEvent);
          if (designProgress) designProgress.value = job.progress || 0;
          if (designRunStatus) designRunStatus.textContent = localizedJobMessage(job.message, job.status) || designJobStatusLabel(job.status);
          renderDesignRunTimeline();
          if (job.terminal) return { job };
        } catch (error) {
          if (signal.aborted) throw error;
          transientFailures += 1;
          if (designRunStatus) designRunStatus.textContent = "任务仍在服务端运行，正在重新查询" + (transientFailures > 1 ? "（" + transientFailures + "）" : "");
        }
        await waitForDesignPoll(Math.min(1000 + transientFailures * 500, 5000), signal);
      }
      throw new DOMException("Aborted", "AbortError");
    }

    function designResultText(job) {
      const outcome = designOutcome(job);
      const issueText = (job.result?.issues || []).map((issue) => "- " + localizedEngineeringIssue(issue)).join("\n");
      const title = outcome.tone === "pass"
        ? outcome.limitedScope ? "总体设计：覆盖范围内初步通过" : "总体设计：初步可行候选（当前模型）"
        : outcome.tone === "fail" ? "总体设计方案未通过工程判定" : "总体设计计算已完成";
      return "### " + title + "\n\n" + outcome.detail + (issueText ? "\n\n" + issueText : "");
    }

    async function monitorDesignJob(jobId) {
      const controller = new AbortController();
      state.designStreamController = controller;
      let reconnects = 0;
      try {
        let payload = null;
        while (!payload) {
          try {
            payload = await streamDesignJob(jobId, state.designJobSequence, controller.signal);
          } catch (error) {
            if (controller.signal.aborted || state.designJobId !== jobId) return;
            reconnects += 1;
            if (reconnects > 3) {
              if (designRunStatus) designRunStatus.textContent = "实时进度连接不可用，已切换为任务状态查询";
              payload = await pollDesignJobUntilTerminal(jobId, controller.signal);
              break;
            }
            if (designRunStatus) designRunStatus.textContent = "进度连接中断，正在继续接收...";
            await new Promise((resolve) => setTimeout(resolve, reconnects * 350));
          }
        }
        if (state.designJobId !== jobId) return;
        let job = payload.job;
        try {
          const detailPayload = await api("/api/design-jobs/" + encodeURIComponent(jobId));
          job = detailPayload.job || job;
        } catch (_error) {
          // The terminal stream payload still contains the engineering result.
        }
        state.activeDesignJob = job;
        state.designJobDetails[job.job_id] = job;
        if (state.designJobMessage) state.designJobMessage.remove();
        state.designJobMessage = null;
        appendAssistantReply(
          { text: designResultText(job), artifacts: job.artifacts || [] },
          { events: state.designJobEvents, artifacts: job.artifacts || [], designJob: job, openProcess: false },
        );
        state.renderedDesignJobId = job.job_id;
        if (designProgress) designProgress.value = 100;
        if (designRunStatus) designRunStatus.textContent = localizedJobMessage(job.message, job.status) || designJobStatusLabel(job.status);
        setDesignRunBusy(false);
        if (designRetryBtn) designRetryBtn.disabled = false;
        const outcome = designOutcome(job);
        setStatus("总体设计任务结束：" + outcome.label + "。", outcome.tone === "fail");
        renderDesignWorkspace();
        if (state.view === "design") setDesignTab("results", { focus: true });
        await refreshDesignJobs({ silent: true });
      } catch (error) {
        if (controller.signal.aborted || state.designJobId !== jobId) return;
        const localizedError = localizedJobMessage(error.message, "failed") || "总体设计任务未完成。";
        if (state.designJobMessage) state.designJobMessage.remove();
        state.designJobMessage = null;
        chatLog.appendChild(createMessage("system", localizedError));
        setDesignRunBusy(false, localizedError);
        setStatus(localizedError, true);
      } finally {
        if (state.designStreamController === controller) state.designStreamController = null;
      }
    }

    async function submitDesignJob(event) {
      event.preventDefault();
      if (state.designJobRunning) return;
      try {
        const request = buildDesignJobRequest();
        const fingerprint = designRequestFingerprint(request);
        if (
          !designPreflightConfirm.checked
          || state.preflightRequestFingerprint !== fingerprint
          || state.confirmedPreflightFingerprint !== state.preflightFingerprint
        ) {
          await runDesignPreflight();
          setActiveView("design");
          setDesignTab("requirements", { focus: true });
          throw new Error("需求或假设已变化，请重新核对并勾选提交前确认。" );
        }
        setSettingsOpen(false);
        setActiveView("design");
        setDesignTab("run", { focus: true });
        state.designJobEvents = [];
        state.designJobMessage = null;
        state.designJobSequence = 0;
        state.renderedDesignJobId = null;
        designProgress.value = 0;
        setDesignRunBusy(true, "正在提交任务");
        refreshDesignJobMessage();
        const payload = await api("/api/design-jobs", {
          method: "POST",
          body: JSON.stringify({ request, timeout_seconds: 180 }),
        });
        state.designJobId = payload.job.job_id;
        state.activeDesignJob = payload.job;
        state.designJobDetails[payload.job.job_id] = payload.job;
        saveLocalState();
        state.designJobs = [payload.job, ...state.designJobs.filter((job) => job.job_id !== payload.job.job_id)];
        renderDesignJobHistory();
        renderDesignWorkspace();
        designCancelBtn.disabled = false;
        await monitorDesignJob(state.designJobId);
      } catch (error) {
        const localizedError = localizedJobMessage(error.message, "failed") || "总体设计任务提交失败。";
        setDesignRunBusy(false, localizedError);
        setStatus(localizedError, true);
      }
    }

    async function cancelDesignJob() {
      if (!state.designJobId || !state.designJobRunning) return;
      designCancelBtn.disabled = true;
      designRunStatus.textContent = "正在取消任务";
      try {
        await api("/api/design-jobs/" + encodeURIComponent(state.designJobId) + "/cancel", {
          method: "POST",
          body: "{}",
        });
      } catch (error) {
        setStatus(localizedJobMessage(error.message, "failed") || "取消任务失败。", true);
      }
    }

    async function retryDesignJob() {
      if (!state.designJobId || state.designJobRunning) return;
      try {
        setActiveView("design");
        setDesignTab("run", { focus: true });
        state.designJobEvents = [];
        state.designJobMessage = null;
        state.designJobSequence = 0;
        state.renderedDesignJobId = null;
        designProgress.value = 0;
        setDesignRunBusy(true, "正在重新提交任务");
        refreshDesignJobMessage();
        const payload = await api("/api/design-jobs/" + encodeURIComponent(state.designJobId) + "/retry", {
          method: "POST",
          body: "{}",
        });
        state.designJobId = payload.job.job_id;
        state.activeDesignJob = payload.job;
        state.designJobDetails[payload.job.job_id] = payload.job;
        saveLocalState();
        state.designJobs = [payload.job, ...state.designJobs.filter((job) => job.job_id !== payload.job.job_id)];
        renderDesignJobHistory();
        renderDesignWorkspace();
        await monitorDesignJob(state.designJobId);
      } catch (error) {
        const localizedError = localizedJobMessage(error.message, "failed") || "重新提交任务失败。";
        setDesignRunBusy(false, localizedError);
        setStatus(localizedError, true);
      }
    }

    async function sendPrompt(event) {
      event.preventDefault();
      const message = promptInput.value.trim();
      if (!message || state.busy) return;

      setBusy(true, "正在思考...");
      setStatus("");
      state.abortController = new AbortController();
      const turnStartedAt = performance.now();
      let liveAssistant = null;
      let liveText = "";
      let hasDraftEvent = false;
      const liveEvents = [{
        kind: "planning",
        tool_name: skillDisplayName(selectedSkillName()) || "工程设计",
        summary: "我先拆解任务目标、约束条件和可能需要补充的资料，再开始组织回答。",
        is_error: false,
      }];
      const ensureLiveAssistant = () => {
        if (!liveAssistant) {
          liveAssistant = createMessage("assistant", "", {
            events: liveEvents,
            elapsedMs: performance.now() - turnStartedAt,
            isRunning: true,
          });
          chatLog.appendChild(liveAssistant);
        }
        return liveAssistant;
      };
      const refreshLiveProcess = (openProcess = false) => {
        const assistant = ensureLiveAssistant();
        updateProcessPanel(assistant, liveEvents, {
          elapsedMs: performance.now() - turnStartedAt,
          isRunning: true,
          open: true,
        });
      };
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
        refreshLiveProcess(true);
        chatLog.scrollTop = chatLog.scrollHeight;

        const payload = await streamApi(
          "/api/sessions/" + encodeURIComponent(state.sessionId) + "/messages/stream",
          {
            message,
            auto_approve: autoApproveToggle.checked,
            auto_skill: toInternalSkillName(selectedSkillName()),
          },
          {
            onChunk: (chunk) => {
              liveText += chunk;
              if (!hasDraftEvent) {
              liveEvents.push({
                kind: "drafting",
                  tool_name: skillDisplayName(selectedSkillName()) || "工程设计",
                  summary: "我已经开始把当前可用信息整理成正式回答。",
                  is_error: false,
              });
                hasDraftEvent = true;
              }
              const assistant = ensureLiveAssistant();
              const bubble = assistant.querySelector(".bubble");
              if (bubble) renderMarkdownInto(bubble, liveText);
              updateProcessPanel(assistant, liveEvents, {
                elapsedMs: performance.now() - turnStartedAt,
                isRunning: true,
              });
              chatLog.scrollTop = chatLog.scrollHeight;
            },
            onTool: (toolEvent) => {
              liveEvents.push(toolEvent);
              refreshLiveProcess(true);
              chatLog.scrollTop = chatLog.scrollHeight;
              if (toolEvent.summary) setStatus(toolEvent.summary);
            },
          },
        );
        if (liveAssistant) liveAssistant.remove();

        updateMeta(payload.session);
        const finalEvents = mergeMessageEvents(liveEvents, payload.reply.events || []);
        appendAssistantReply(payload.reply, {
          elapsedMs: performance.now() - turnStartedAt,
          events: finalEvents,
          artifacts: payload.reply.artifacts,
        });
        await refreshSessions();
        const usage = payload.reply.usage || {};
        const tokenBits = [];
        if (usage.input_tokens) tokenBits.push("输入 " + usage.input_tokens);
        if (usage.output_tokens) tokenBits.push("输出 " + usage.output_tokens);
        const resultArtifacts = payload.reply.artifacts || [];
        const artifactFailure = (payload.reply.events || []).find((item) => item.kind === "artifact" && item.is_error);
        if (resultArtifacts.length) {
          setStatus("本轮完成，设计结果包已生成。" + (tokenBits.length ? " " + tokenBits.join(" / ") : ""));
        } else if (selectedSkillName() === WEB_AIRCRAFT_SKILL && artifactFailure) {
          setStatus("计算未生成新的结果文件，请展开过程查看失败原因。", true);
        } else {
          setStatus(tokenBits.length ? "本轮完成：" + tokenBits.join(" / ") : "本轮完成。");
        }
      } catch (error) {
        const messageText = error.name === "AbortError" ? "已在本地停止请求；服务器可能仍会完成已开始的回合。" : error.message;
        if (liveAssistant) {
          liveEvents.push({
            kind: "request",
            tool_name: "网页请求",
            summary: messageText,
            error: messageText,
            is_error: true,
          });
          updateProcessPanel(liveAssistant, liveEvents, {
            elapsedMs: performance.now() - turnStartedAt,
            isError: true,
            open: true,
          });
        }
        chatLog.appendChild(createMessage("system", messageText));
        chatLog.scrollTop = chatLog.scrollHeight;
        setStatus(messageText, true);
      } finally {
        state.abortController = null;
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

    aircraftSkillToggle.addEventListener("change", () => {
      updateSkillStatus();
      saveLocalState();
      setStatus(
        aircraftSkillToggle.checked
          ? "已启用飞行器总体设计技能，将在下一次发送时生效。"
          : "已关闭飞行器总体设计技能，将在下一次发送时生效。",
      );
    });
    modelInput.addEventListener("change", saveLocalState);
    autoApproveToggle.addEventListener("change", () => {
      updateSkillStatus();
      saveLocalState();
    });

    newSessionBtn.addEventListener("click", () => {
      setActiveView("chat");
      createSession();
    });
    chatViewBtn.addEventListener("click", () => setActiveView("chat"));
    designWorkspaceBtn.addEventListener("click", () => {
      setDesignTab("results");
      setActiveView("design");
    });
    designBackChatBtn.addEventListener("click", () => setActiveView("chat"));
    settingsToggleBtn.addEventListener("click", () => setSettingsOpen(true));
    settingsTopBtn.addEventListener("click", () => setSettingsOpen(true));
    settingsCloseBtn.addEventListener("click", () => setSettingsOpen(false));
    settingsOverlay.addEventListener("click", (event) => {
      if (event.target === settingsOverlay) setSettingsOpen(false);
    });
    document.addEventListener("keydown", (event) => {
      if (!settingsOverlay.classList.contains("is-open")) return;
      if (event.key === "Escape") {
        event.preventDefault();
        setSettingsOpen(false);
        return;
      }
      if (event.key === "Tab") {
        const focusable = Array.from(settingsOverlay.querySelectorAll("button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), a[href], [tabindex]:not([tabindex='-1'])"));
        if (!focusable.length) return;
        const first = focusable[0];
        const last = focusable[focusable.length - 1];
        if (event.shiftKey && document.activeElement === first) {
          event.preventDefault();
          last.focus();
        } else if (!event.shiftKey && document.activeElement === last) {
          event.preventDefault();
          first.focus();
        }
      }
    });
    resetSessionBtn.addEventListener("click", resetSession);
    designResultVersionSelect.addEventListener("change", () => selectSessionDesignResult(designResultVersionSelect.value));
    document.querySelectorAll("[data-design-tab]").forEach((button) => {
      button.addEventListener("click", () => setDesignTab(button.dataset.designTab));
      button.addEventListener("keydown", (event) => {
        if (!["ArrowLeft", "ArrowRight", "Home", "End"].includes(event.key)) return;
        event.preventDefault();
        const tabs = Array.from(document.querySelectorAll("[data-design-tab]:not([hidden])"));
        const current = tabs.indexOf(button);
        const next = event.key === "Home" ? 0 : event.key === "End" ? tabs.length - 1 : (current + (event.key === "ArrowRight" ? 1 : -1) + tabs.length) % tabs.length;
        setDesignTab(tabs[next].dataset.designTab, { focus: true });
      });
    });
    stopBtn.addEventListener("click", () => {
      state.abortController?.abort();
      setStatus("正在停止本地请求...", true);
    });
    clearDraftBtn.addEventListener("click", () => {
      promptInput.value = "";
      autosizePrompt();
      promptInput.focus();
      setStatus("草稿已清空。");
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
        if (local?.sessionId) {
          try {
            await loadSession(local.sessionId);
            const pendingSkill = toUiSkillName(local.autoSkill || "");
            if (pendingSkill === WEB_AIRCRAFT_SKILL && skillByName(pendingSkill)) {
              setSelectedSkill(pendingSkill);
              updateSkillStatus();
              saveLocalState();
            }
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
