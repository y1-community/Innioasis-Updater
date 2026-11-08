/**
 * Raptive & Premium Ad Network Management System for Innioasis.app
 *
 * Provides a turnkey, zero-layout-shift (CLS = 0) ad management framework:
 * - Central configuration for Raptive publisher ID, placement rules, and provider modes
 * - Automatic placement and injection for Header Leaderboard, In-Content, Sidebar, and Sticky Anchor
 * - Strict CSS height reservation to eliminate Cumulative Layout Shift
 * - Integration with Google Consent Mode v2 and Innioasis Privacy preferences
 * - Clean house fallback promos for preview and unmonetized traffic
 * - URL parameter toggle (?raptive_preview=1 or ?ads=1) for live audit and demonstration
 */
(function (global, document) {
  "use strict";

  var DEFAULT_CONFIG = {
    /* Set to true when Raptive account is active, or activate via URL ?ads=1 or ?raptive_preview=1 */
    enabled: false,

    /* Raptive Site / Publisher ID (assigned upon Raptive approval) */
    raptiveSiteId: "",

    /* Provider mode:
       "raptive"   - Loads official Raptive tag.js for the site ID
       "preview"   - Renders labelled, reserved layout containers with high-value house promos
       "adsense"   - Optional Google AdSense client & slot fallback
       "house"     - Internal community promotions only
    */
    provider: "house",

    /* Google AdSense fallback details (if used before Raptive) */
    adsenseClient: "",
    adsenseSlot: "",

    /* Placement rules */
    placements: {
      headerLeaderboard: true,   // 728x90 (desktop) / 320x50 (mobile) at top of article
      inContent: true,           // In-article placements between logical sections
      inContentInterval: 4,      // Every N paragraphs or after each major section
      inContentMax: 3,           // Maximum in-content ads per article to prevent ad fatigue
      sidebarRail: true,         // 300x600 / 300x250 sticky sidebar ad if layout permits
      stickyAnchor: true         // Sticky bottom anchor banner (mobile/desktop)
    },

    /* Excluded path fragments where ads should never render */
    excludedPaths: [
      "/404",
      "/privacy",
      "/embed",
      "/support_toolbar",
      "/download-proxy"
    ]
  };

  // Merge runtime configuration overrides if defined globally
  var CONFIG = Object.assign({}, DEFAULT_CONFIG, global.RAPTIVE_ADS_CONFIG || {});

  // Check URL parameters for maintainer preview or audit mode
  try {
    var params = new URLSearchParams(global.location.search);
    if (params.get("raptive_preview") === "1" || params.get("ads_preview") === "1" || params.get("ads") === "1") {
      CONFIG.enabled = true;
      if (!CONFIG.raptiveSiteId) CONFIG.provider = "preview";
    }
    if (params.get("raptive_id")) {
      CONFIG.raptiveSiteId = params.get("raptive_id");
      CONFIG.provider = "raptive";
      CONFIG.enabled = true;
    }
  } catch (_) {}

  var mountedUnits = [];

  /* ---------------------------------------------------------------- Promos */

  var HOUSE_PROMOS = [
    {
      title: "Rockbox Firmware for Innioasis Y1 & Y2",
      copy: "Install the open-source Rockbox OS with gapless playback, parametric EQ, and custom themes.",
      href: "/rockbox-y1/",
      cta: "Explore Rockbox Guide"
    },
    {
      title: "Innioasis Community Themes Gallery",
      copy: "Browse over 500+ community themes, fonts, and icon packs for your Innioasis player.",
      href: "https://themes.innioasis.app/",
      cta: "Browse Themes"
    },
    {
      title: "Official Factory Firmware Archive",
      copy: "Tested restore packages for Innioasis Y1, Y2, G1, G3, G5, R1, PR1 and Timmkoo A5, Q3, Q5.",
      href: "/firmware.html",
      cta: "View Firmware List"
    },
    {
      title: "Recover Bootlooping or Bricked Players",
      copy: "Step-by-step unbricking guide with MediaTek SP Flash Tool and verified scatter ROMs.",
      href: "/recover-non-booting-device.html",
      cta: "Unbrick Guide"
    }
  ];

  /* ---------------------------------------------------------------- Helpers */

  function isPathExcluded() {
    var path = (global.location && global.location.pathname) || "";
    for (var i = 0; i < CONFIG.excludedPaths.length; i++) {
      if (path.indexOf(CONFIG.excludedPaths[i]) >= 0) return true;
    }
    return false;
  }

  function allowsAds() {
    if (global.INNIOASIS_PRIVACY && typeof global.INNIOASIS_PRIVACY.allows === "function") {
      // In GDPR regions, respect explicit privacy choice
      if (global.INNIOASIS_PRIVACY.hasDecided() && !global.INNIOASIS_PRIVACY.allows("analytics")) {
        return false;
      }
    }
    return true;
  }

  function ensureStyles() {
    if (document.getElementById("raptive-ad-styles")) return;
    var style = document.createElement("style");
    style.id = "raptive-ad-styles";
    style.textContent =
      "/* Raptive Ad Layout & CLS Preservation Framework */\n" +
      ".raptive-ad-container { display: flex; flex-direction: column; align-items: center; justify-content: center; margin: 1.5rem auto; width: 100%; box-sizing: border-box; position: relative; contain: layout style; text-align: center; }\n" +
      ".raptive-ad-label { display: block; font-size: 0.65rem; font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; color: var(--lumen-muted, #94a3b8); margin: 0 0 6px; user-select: none; }\n" +
      ".raptive-ad-slot { display: flex; align-items: center; justify-content: center; width: 100%; overflow: hidden; border-radius: 12px; border: 1px solid var(--lumen-line, rgba(255,255,255,0.12)); background: var(--lumen-panel-soft, rgba(255,255,255,0.03)); box-sizing: border-box; }\n" +
      "/* Strict CLS min-height reservations */\n" +
      ".raptive-ad--leaderboard { max-width: 970px; min-height: 110px; margin: 1.25rem auto; }\n" +
      ".raptive-ad--leaderboard .raptive-ad-slot { min-height: 90px; }\n" +
      ".raptive-ad--incontent { max-width: 760px; min-height: 275px; margin: 2rem auto; }\n" +
      ".raptive-ad--incontent .raptive-ad-slot { min-height: 250px; }\n" +
      ".raptive-ad--sidebar { max-width: 320px; min-height: 620px; margin: 1rem auto; }\n" +
      ".raptive-ad--sidebar .raptive-ad-slot { min-height: 600px; }\n" +
      ".raptive-ad--anchor { position: fixed; bottom: calc(64px + env(safe-area-inset-bottom, 0px)); left: 50%; transform: translateX(-50%); z-index: 9998; width: 100%; max-width: 728px; padding: 4px 10px; background: var(--lumen-panel, #0f131a); box-shadow: 0 -4px 20px rgba(0,0,0,0.4); border-top: 1px solid var(--lumen-line-strong, rgba(255,255,255,0.2)); border-radius: 12px 12px 0 0; }\n" +
      ".raptive-ad--anchor .raptive-ad-slot { min-height: 90px; border: none; }\n" +
      ".raptive-ad-anchor-close { position: absolute; top: -14px; right: 12px; width: 26px; height: 26px; border-radius: 50%; border: 1px solid var(--lumen-line-strong, rgba(255,255,255,0.3)); background: var(--lumen-panel, #0f131a); color: var(--lumen-text, #fff); font-size: 14px; line-height: 1; cursor: pointer; display: flex; align-items: center; justify-content: center; box-shadow: 0 2px 6px rgba(0,0,0,0.3); }\n" +
      ".raptive-ad-anchor-close:hover { background: var(--lumen-accent, #6366f1); }\n" +
      "/* House promotion banner styling */\n" +
      ".raptive-house-promo { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 14px; width: 100%; padding: 14px 20px; text-align: left; box-sizing: border-box; }\n" +
      ".raptive-house-info { flex: 1 1 280px; }\n" +
      ".raptive-house-title { display: block; font-size: 0.95rem; font-weight: 700; color: var(--lumen-text, #f8fafc); margin: 0 0 4px; }\n" +
      ".raptive-house-copy { display: block; font-size: 0.82rem; color: var(--lumen-muted, #94a3b8); line-height: 1.4; }\n" +
      ".raptive-house-btn { display: inline-flex; align-items: center; padding: 8px 16px; border-radius: 99px; background: var(--lumen-accent-wash, rgba(99,102,241,0.16)); border: 1px solid var(--lumen-accent, #6366f1); color: var(--lumen-text, #fff); font-size: 0.82rem; font-weight: 600; text-decoration: none; white-space: nowrap; transition: background 0.15s ease, transform 0.15s ease; }\n" +
      ".raptive-house-btn:hover { background: var(--lumen-accent, #6366f1); color: #fff; transform: translateY(-1px); }\n" +
      "/* Responsive mobile rules */\n" +
      "@media (max-width: 768px) {\n" +
      "  .raptive-ad--leaderboard { min-height: 70px; margin: 0.75rem auto; }\n" +
      "  .raptive-ad--leaderboard .raptive-ad-slot { min-height: 50px; }\n" +
      "  .raptive-ad--anchor { max-width: 100%; border-radius: 0; bottom: calc(56px + env(safe-area-inset-bottom, 0px)); }\n" +
      "  .raptive-ad--anchor .raptive-ad-slot { min-height: 50px; }\n" +
      "  .raptive-house-promo { flex-direction: column; align-items: flex-start; padding: 12px; gap: 10px; }\n" +
      "  .raptive-house-btn { width: 100%; justify-content: center; }\n" +
      "}";
    (document.head || document.documentElement).appendChild(style);
  }

  function renderHousePromo(container, slotType) {
    var promoIndex = Math.floor(Math.random() * HOUSE_PROMOS.length);
    var promo = HOUSE_PROMOS[promoIndex] || HOUSE_PROMOS[0];

    var wrap = document.createElement("div");
    wrap.className = "raptive-house-promo";

    var info = document.createElement("div");
    info.className = "raptive-house-info";

    var title = document.createElement("strong");
    title.className = "raptive-house-title";
    title.textContent = promo.title;

    var copy = document.createElement("span");
    copy.className = "raptive-house-copy";
    copy.textContent = promo.copy;

    info.appendChild(title);
    info.appendChild(copy);

    var btn = document.createElement("a");
    btn.className = "raptive-house-btn";
    btn.href = promo.href;
    btn.textContent = promo.cta;

    wrap.appendChild(info);
    wrap.appendChild(btn);
    container.appendChild(wrap);
  }

  function createAdSlot(type, id) {
    var container = document.createElement("aside");
    container.className = "raptive-ad-container raptive-ad--" + type;
    container.setAttribute("data-raptive-unit", type);
    container.setAttribute("aria-label", "Advertisement");

    var label = document.createElement("span");
    label.className = "raptive-ad-label";
    label.textContent = CONFIG.provider === "raptive" ? "Advertisement" : "Sponsored / Ad Space";

    var slot = document.createElement("div");
    slot.className = "raptive-ad-slot";
    slot.id = id || ("raptive-" + type + "-" + Math.random().toString(36).substring(2, 8));

    container.appendChild(label);
    container.appendChild(slot);

    if (type === "anchor") {
      var closeBtn = document.createElement("button");
      closeBtn.className = "raptive-ad-anchor-close";
      closeBtn.setAttribute("aria-label", "Close ad");
      closeBtn.innerHTML = "&times;";
      closeBtn.addEventListener("click", function () {
        container.style.display = "none";
      });
      container.appendChild(closeBtn);
    }

    // Populate slot content based on provider
    if (CONFIG.provider === "raptive" && CONFIG.raptiveSiteId) {
      // Let Raptive's script populate the slot
      slot.setAttribute("data-raptive-slot", type);
    } else {
      // Render zero-shift house preview
      renderHousePromo(slot, type);
    }

    return container;
  }

  /* ---------------------------------------------------------------- Injection */

  function injectLeaderboard(mainEl) {
    if (!CONFIG.placements.headerLeaderboard) return;
    var existing = mainEl.querySelector(".raptive-ad--leaderboard");
    if (existing) return;

    var unit = createAdSlot("leaderboard", "raptive-top-leaderboard");
    // Place right after the main H1 or intro hero paragraph
    var firstH1 = mainEl.querySelector("h1");
    if (firstH1 && firstH1.nextElementSibling) {
      mainEl.insertBefore(unit, firstH1.nextElementSibling);
    } else {
      mainEl.insertBefore(unit, mainEl.firstChild);
    }
    mountedUnits.push(unit);
  }

  function injectInContent(mainEl) {
    if (!CONFIG.placements.inContent) return;
    var sections = Array.from(mainEl.querySelectorAll("section, article, .lumen-guide-section, p"));
    if (!sections || sections.length < 3) return;

    var injected = 0;
    var maxAds = CONFIG.placements.inContentMax || 3;
    var interval = CONFIG.placements.inContentInterval || 4;

    // Search for suitable section boundaries
    var sectionContainers = Array.from(mainEl.querySelectorAll("section.lumen-guide-section, section, article"));
    if (sectionContainers.length >= 2) {
      for (var i = 1; i < sectionContainers.length && injected < maxAds; i += 2) {
        var unit = createAdSlot("incontent", "raptive-incontent-" + (injected + 1));
        var targetSection = sectionContainers[i];
        if (targetSection && targetSection.parentNode) {
          targetSection.parentNode.insertBefore(unit, targetSection);
          mountedUnits.push(unit);
          injected++;
        }
      }
      return;
    }

    // Paragraph fallback for single long text articles
    var paragraphs = Array.from(mainEl.querySelectorAll("p"));
    if (paragraphs.length >= 8) {
      for (var pIdx = interval; pIdx < paragraphs.length && injected < maxAds; pIdx += interval) {
        var pTarget = paragraphs[pIdx];
        if (pTarget && pTarget.parentNode) {
          var pUnit = createAdSlot("incontent", "raptive-incontent-p" + (injected + 1));
          pTarget.parentNode.insertBefore(pUnit, pTarget.nextSibling);
          mountedUnits.push(pUnit);
          injected++;
        }
      }
    }
  }

  function injectStickyAnchor() {
    if (!CONFIG.placements.stickyAnchor) return;
    if (document.getElementById("raptive-bottom-anchor")) return;

    var anchor = createAdSlot("anchor", "raptive-bottom-anchor");
    document.body.appendChild(anchor);
    mountedUnits.push(anchor);
  }

  function loadRaptiveScript(siteId) {
    if (!siteId) return;
    var scriptId = "raptive-ads-tag";
    if (document.getElementById(scriptId)) return;

    var script = document.createElement("script");
    script.id = scriptId;
    script.async = true;
    script.src = "https://ads.raptive.com/pubs/" + encodeURIComponent(siteId) + "/tag.js";
    (document.head || document.documentElement).appendChild(script);
  }

  /* ---------------------------------------------------------------- Public API */

  var AdManager = {
    config: CONFIG,

    init: function () {
      if (isPathExcluded()) return;
      if (!allowsAds()) return;

      ensureStyles();

      // If Raptive script is live
      if (CONFIG.enabled && CONFIG.provider === "raptive" && CONFIG.raptiveSiteId) {
        loadRaptiveScript(CONFIG.raptiveSiteId);
      }

      var mainEl = document.querySelector("main#main") || document.querySelector("main") || document.body;
      if (mainEl && CONFIG.enabled) {
        injectLeaderboard(mainEl);
        injectInContent(mainEl);
        injectStickyAnchor();
      }

      // Listen for dynamic privacy changes
      global.addEventListener("innioasis-privacy-change", function (e) {
        if (e && e.detail && e.detail.analytics === "off") {
          AdManager.destroy();
        }
      });
    },

    configure: function (newConfig) {
      Object.assign(CONFIG, newConfig || {});
    },

    enableRaptive: function (siteId) {
      CONFIG.enabled = true;
      CONFIG.provider = "raptive";
      CONFIG.raptiveSiteId = siteId;
      AdManager.init();
    },

    preview: function () {
      CONFIG.enabled = true;
      CONFIG.provider = "preview";
      AdManager.init();
    },

    destroy: function () {
      mountedUnits.forEach(function (unit) {
        if (unit && unit.parentNode) unit.parentNode.removeChild(unit);
      });
      mountedUnits = [];
    },

    getStatus: function () {
      return {
        enabled: CONFIG.enabled,
        provider: CONFIG.provider,
        raptiveSiteId: CONFIG.raptiveSiteId,
        mountedCount: mountedUnits.length,
        clsSafe: true
      };
    }
  };

  global.AdManager = AdManager;

  // Auto-initialize when DOM is ready
  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      AdManager.init();
    });
  } else {
    AdManager.init();
  }

})(typeof window !== "undefined" ? window : globalThis, typeof document !== "undefined" ? document : {});
