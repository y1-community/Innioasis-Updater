/**
 * Shared site shell: body classes and bottom dock.
 */
(function (global) {
    "use strict";

    function resolveEffectiveTheme(theme) {
        if (theme === "auto" || theme === "light" || !theme) return "dark";
        return (theme === "high-contrast" || theme === "2077") ? theme : "dark";
    }

    function applyStoredTheme() {
        var allowed = ["auto", "dark", "high-contrast", "2077"];
        var stored = null;
        try { stored = global.localStorage.getItem("lumen-theme"); } catch (_) {}
        var theme = allowed.indexOf(stored) >= 0 ? stored : "auto";
        if (document.documentElement) document.documentElement.setAttribute("data-lumen-theme", resolveEffectiveTheme(theme));
        return theme;
    }

    applyStoredTheme();

    /* Shared cross-subdomain cookie helper (.innioasis.app) */
    function setSharedCookie(name, value, days) {
        try {
            var d = new Date();
            d.setTime(d.getTime() + ((days || 365) * 24 * 60 * 60 * 1000));
            var expires = "; expires=" + d.toUTCString();
            var host = (global.location && global.location.hostname) || "";
            var domain = /(^|\.)innioasis\.app$/i.test(host) ? "; domain=.innioasis.app" : "";
            document.cookie = name + "=" + encodeURIComponent(value) + expires + "; path=/" + domain + "; SameSite=Lax";
        } catch (_) {}
    }

    function getSharedCookie(name) {
        try {
            var prefix = name + "=";
            var parts = (document.cookie || "").split(";");
            for (var i = 0; i < parts.length; i++) {
                var item = parts[i].trim();
                if (item.indexOf(prefix) === 0) return decodeURIComponent(item.substring(prefix.length));
            }
        } catch (_) {}
        return null;
    }

    /* Privacy consent. The site uses Google Analytics (via Google Tag Manager)
       and Cloudflare to measure and optimise performance and protect the site
       from attacks. Local storage remembers the visitor's own theme choice
       (always remembered — it is the look they picked) plus, only when allowed,
       their answers to the "was this useful?" prompts and their
       nightly-builds preference. The consent record itself is kept so the
       privacy panel does not open on every visit.
       URL variables (?privacy=all, ?privacy=none, etc.) and cross-subdomain
       cookies carry consent between innioasis.app and themes.innioasis.app. */
    var CONSENT_KEY = "innioasis-consent";

    function parsePrivacyParam() {
        try {
            var search = (global.location && global.location.search) || "";
            var params = new URLSearchParams(search);
            var raw = params.get("privacy");
            if (raw) {
                var v = String(raw).trim().toLowerCase();
                if (v === "all" || v === "1" || v === "true" || v === "yes") return { feedback: true, nightly: true };
                if (v === "none" || v === "0" || v === "false" || v === "no") return { feedback: false, nightly: false };
                if (v === "feedback") return { feedback: true, nightly: false };
                if (v === "nightly") return { feedback: false, nightly: true };
            }
            var pf = params.get("privacy_feedback");
            var pn = params.get("privacy_nightly");
            if (pf !== null || pn !== null) {
                return {
                    feedback: pf === "1" || pf === "true" || pf === "yes",
                    nightly: pn === "1" || pn === "true" || pn === "yes"
                };
            }
        } catch (_) {}
        return null;
    }

    function readConsent() {
        try {
            var raw = global.localStorage.getItem(CONSENT_KEY);
            if (raw) {
                var data = JSON.parse(raw);
                if (data && typeof data === "object") {
                    var fb = typeof data.feedback === "boolean" ? data.feedback : true;
                    var nl = typeof data.nightly === "boolean" ? data.nightly : true;
                    var an = data.analytics === "off" ? "off" : "essential";
                    return { feedback: fb, nightly: nl, analytics: an };
                }
            }
        } catch (_) {}

        // Fallback to shared cross-subdomain cookie if available
        try {
            var fromCookie = getSharedCookie(CONSENT_KEY);
            if (fromCookie) {
                var cookieData = JSON.parse(fromCookie);
                if (cookieData && typeof cookieData === "object") {
                    var cfb = typeof cookieData.feedback === "boolean" ? cookieData.feedback : true;
                    var cnl = typeof cookieData.nightly === "boolean" ? cookieData.nightly : true;
                    var can = cookieData.analytics === "off" ? "off" : "essential";
                    var parsed = { feedback: cfb, nightly: cnl, analytics: can };
                    try { global.localStorage.setItem(CONSENT_KEY, JSON.stringify(parsed)); } catch (_) {}
                    return parsed;
                }
            }
        } catch (_) {}

        return null;
    }

    function applyAnalyticsConsent(mode) {
        var isOff = mode === "off";
        global["ga-disable-GTM-TNDGC37L"] = isOff;
        if (typeof global.gtag === "function") {
            try {
                global.gtag("consent", "update", {
                    analytics_storage: isOff ? "denied" : "granted",
                    ad_storage: "denied"
                });
            } catch (_) {}
        }
        if (global.ThemeAnalytics && typeof global.ThemeAnalytics.setConsent === "function") {
            try {
                global.ThemeAnalytics.setConsent({ analytics: !isOff });
            } catch (_) {}
        }
    }

    function writeConsent(prefs) {
        var anMode = (prefs && prefs.analytics === "off") ? "off" : "essential";
        var next = {
            feedback: prefs.feedback !== false,
            nightly: prefs.nightly !== false,
            analytics: anMode
        };
        try {
            global.localStorage.setItem(CONSENT_KEY, JSON.stringify(next));
        } catch (_) {}
        setSharedCookie(CONSENT_KEY, JSON.stringify(next));
        setSharedCookie("innioasis-privacy", next.feedback && next.nightly ? "all" : (!next.feedback && !next.nightly ? "none" : (next.feedback ? "feedback" : "nightly")));
        setSharedCookie("innioasis-privacy-analytics", anMode);

        applyAnalyticsConsent(anMode);

        if (!next.feedback) {
            try {
                var doomed = [];
                for (var i = 0; i < global.localStorage.length; i += 1) {
                    var key = global.localStorage.key(i);
                    if (key && key.indexOf("innioasis-feedback-") === 0) doomed.push(key);
                }
                doomed.forEach(function (key) { global.localStorage.removeItem(key); });
            } catch (_) {}
        }
        if (!next.nightly) {
            try { global.localStorage.removeItem("innioasis-show-nightly"); } catch (_) {}
        }
        /* Let the page react immediately: the directory drops a remembered
           nightly filter and the guide pages forget a displayed answer. */
        try {
            global.dispatchEvent(new CustomEvent("innioasis-privacy-change", { detail: next }));
        } catch (_) {}
        if (typeof global.y1DecorateLinks === "function") {
            try { global.y1DecorateLinks(); } catch (_) {}
        }
        return next;
    }

    (function initPrivacyFromUrlOrCookie() {
        var fromUrl = parsePrivacyParam();
        if (fromUrl !== null) {
            writeConsent(fromUrl);
        } else {
            var existing = readConsent();
            if (existing !== null) {
                setSharedCookie(CONSENT_KEY, JSON.stringify(existing));
                applyAnalyticsConsent(existing.analytics);
            }
        }
    })();

    /* The archive has no consent panel of its own, so the footer control
       sends visitors to the part of the privacy page that explains and changes
       the setting. The gallery mounts its own panel, and that handler runs
       first; leave its click alone. */
    document.addEventListener("click", function (event) {
        var trigger = event.target && event.target.closest ? event.target.closest("[data-privacy-open]") : null;
        if (!trigger) return;
        if (document.getElementById("y1-privacy-panel")) return;
        event.preventDefault();
        global.location.href = "/privacy.html#choices";
    });

    global.INNIOASIS_PRIVACY = {
        read: readConsent,
        save: writeConsent,
        hasDecided: function () { return readConsent() !== null; },
        /* Whether the site may remember a given preference. Theme is always
           allowed; optional preferences only after explicit consent. */
        allows: function (feature) {
            if (feature === "theme") return true;
            var prefs = readConsent();
            if (!prefs) return false;
            if (feature === "analytics") return prefs.analytics !== "off";
            return prefs[feature] === true;
        }
    };
    global.setSharedCookie = setSharedCookie;
    global.getSharedCookie = getSharedCookie;

    function executeInlineScripts(container) {
        if (!container) return;
        container.querySelectorAll("script").forEach(function (oldScript) {
            var newScript = document.createElement("script");
            Array.from(oldScript.attributes).forEach(function (attr) {
                newScript.setAttribute(attr.name, attr.value);
            });
            newScript.textContent = oldScript.textContent;
            oldScript.parentNode.replaceChild(newScript, oldScript);
        });
    }

    function toolbarCandidates() {
        return [
            "support_toolbar.html",
            "../support_toolbar.html",
            "../../support_toolbar.html",
            "../../../support_toolbar.html",
            "https://innioasis.app/support_toolbar.html",
            "https://themes.innioasis.app/support_toolbar.html",
        ];
    }

    function addThemeFallback() {
        if (document.getElementById("nav-root") || document.getElementById("lumen-theme-fallback")) return;
        var control = document.createElement("label");
        control.id = "lumen-theme-fallback";
        control.className = "lumen-theme-control lumen-theme-control--fallback";
        control.innerHTML = '<span>Theme</span><select aria-label="Choose site colour theme"><option value="auto">Auto</option><option value="dark">Dark</option><option value="high-contrast">High contrast</option><option value="2077">2077</option></select>';
        var select = control.querySelector("select");
        var stored = "auto";
        try { stored = global.localStorage.getItem("lumen-theme") || "auto"; } catch (_) {}
        select.value = ["auto", "dark", "high-contrast", "2077"].indexOf(stored) >= 0 ? stored : "auto";
        select.addEventListener("change", function () {
            document.documentElement.setAttribute("data-lumen-theme", resolveEffectiveTheme(select.value));
            try { global.localStorage.setItem("lumen-theme", select.value); } catch (_) {}
        });
        document.body.appendChild(control);
    }

    function notifyDockReady() {
        try {
            global.dispatchEvent(new CustomEvent("y1-dock-slot-ready"));
        } catch (_) {}
    }

    function removeDuplicateSupportToolbars(slot) {
        var toolbars = Array.from(document.querySelectorAll("#support-toolbar-container"));
        var mounted = slot ? slot.querySelector("#support-toolbar-container") : null;
        toolbars.forEach(function (toolbar) {
            if (!mounted) {
                mounted = toolbar;
                return;
            }
            if (toolbar !== mounted) toolbar.remove();
        });
    }

    async function loadSupportToolbar() {
        var slot = document.getElementById("support-toolbar-slot");
        if (!slot || slot.dataset.shellLoaded === "1" || slot.dataset.shellLoading === "1") return;
        slot.dataset.shellLoading = "1";
        removeDuplicateSupportToolbars(slot);
        try {
            for (var i = 0; i < toolbarCandidates().length; i++) {
                try {
                    var res = await fetch(toolbarCandidates()[i], { cache: "no-cache" });
                    if (!res.ok) continue;
                    slot.innerHTML = await res.text();
                    executeInlineScripts(slot);
                    removeDuplicateSupportToolbars(slot);
                    slot.dataset.shellLoaded = "1";
                    notifyDockReady();
                    return;
                } catch (_) {}
            }
        } finally {
            delete slot.dataset.shellLoading;
        }
    }

    function loadAdManager() {
        if (global.AdManager || document.getElementById("ad-manager-script")) return;
        var s = document.createElement("script");
        s.id = "ad-manager-script";
        s.src = "/ad-manager.js?v=20261109";
        s.defer = true;
        (document.head || document.documentElement).appendChild(s);
    }

    async function init() {
        if (document.documentElement) {
            document.documentElement.classList.add("site-themes-html");
        }
        if (document.body) {
            document.body.classList.add("site-themes-app");
        }
        await loadSupportToolbar();
        if (document.body) {
            document.body.classList.add("site-dock-mode");
            addThemeFallback();
        }
        loadAdManager();
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", function () {
            void init();
        });
    } else {
        void init();
    }

    global.y1LoadSupportToolbar = loadSupportToolbar;
})(typeof window !== "undefined" ? window : globalThis);
