/**
 * Shared site shell: body classes and bottom dock.
 */
(function (global) {
    "use strict";

    /* ---- Appearance -------------------------------------------------------
       One choice, four palettes. The preference is kept locally, mirrored to
       the shared .innioasis.app cookie so it follows the visitor between
       innioasis.app and themes.innioasis.app, and applied as data-theme /
       data-lumen-theme — the attributes tokens.css keys every palette off.
       "Auto" follows the operating system and re-applies when it changes. */
    var APPEARANCE_KEY = "lumen-theme";
    var APPEARANCES = ["auto", "dark", "light", "high-contrast", "2077"];

    function systemAppearance() {
        try {
            if (global.matchMedia && global.matchMedia("(prefers-color-scheme: light)").matches) return "light";
        } catch (_) {}
        return "dark";
    }

    function resolveEffectiveTheme(theme) {
        if (!theme || theme === "auto" || APPEARANCES.indexOf(theme) < 0) return systemAppearance();
        return theme;
    }

    function storedAppearance() {
        /* The shared cookie is the last choice made on either site. This
           origin's own storage is only the fallback for a first visit. */
        var value = getSharedCookie("innioasis-theme");
        if (APPEARANCES.indexOf(value) < 0) {
            try { value = global.localStorage.getItem(APPEARANCE_KEY); } catch (_) {}
        }
        return APPEARANCES.indexOf(value) >= 0 ? value : "auto";
    }

    function applyAppearance(theme, persist) {
        if (APPEARANCES.indexOf(theme) < 0) theme = "auto";
        var effective = resolveEffectiveTheme(theme);
        var root = document.documentElement;
        if (root) {
            root.setAttribute("data-theme", effective);
            root.setAttribute("data-lumen-theme", effective);
            root.setAttribute("data-appearance", theme);
        }
        if (persist) {
            try { global.localStorage.setItem(APPEARANCE_KEY, theme); } catch (_) {}
            setSharedCookie("innioasis-theme", theme);
            try {
                global.dispatchEvent(new CustomEvent("y1-appearance-change", { detail: { theme: theme } }));
            } catch (_) {}
        }
        var selects = document.querySelectorAll("#lumen-theme-select");
        for (var i = 0; i < selects.length; i++) {
            if (selects[i].value !== theme) selects[i].value = theme;
        }
        var meta = document.querySelector('meta[name="theme-color"]');
        if (meta && root) {
            var colour = "";
            try { colour = global.getComputedStyle(root).getPropertyValue("--lumen-theme-color").trim(); } catch (_) {}
            if (colour) meta.setAttribute("content", colour);
        }
        return effective;
    }

    function applyStoredTheme() {
        var theme = storedAppearance();
        var urlTheme = null;
        try {
            var p = new URLSearchParams((global.location && global.location.search) || "");
            urlTheme = p.get("site_theme") || p.get("theme");
            if (urlTheme) {
                urlTheme = urlTheme.toLowerCase().trim();
                if (APPEARANCES.indexOf(urlTheme) < 0) urlTheme = null;
            }
        } catch (_) {}
        if (urlTheme) theme = urlTheme;
        applyAppearance(theme, true);
        return theme;
    }

    applyStoredTheme();

    /* Follow the OS while the visitor is on Auto, without a reload. */
    (function watchSystemAppearance() {
        try {
            var mq = global.matchMedia ? global.matchMedia("(prefers-color-scheme: light)") : null;
            if (!mq) return;
            var onChange = function () {
                if (storedAppearance() === "auto") applyAppearance("auto", false);
            };
            if (typeof mq.addEventListener === "function") mq.addEventListener("change", onChange);
            else if (typeof mq.addListener === "function") mq.addListener(onChange);
        } catch (_) {}
    })();

    /* Accessibility preference (e.g. reduce-motion) */
    function applyAccessibility() {
        var raw = null;
        try {
            var p = new URLSearchParams(global.location.search);
            raw = p.get("accessibility") || p.get("a11y");
        } catch (_) {}
        if (!raw) raw = getSharedCookie("innioasis-accessibility");
        if (!raw) {
            try { raw = global.localStorage.getItem("innioasis-accessibility"); } catch (_) {}
        }
        /* The operating system setting applies on this visit only. Writing it
           into storage made every other Innioasis site inherit it as a choice. */
        if (!raw && global.matchMedia && global.matchMedia("(prefers-reduced-motion: reduce)").matches) {
            if (document.documentElement) {
                document.documentElement.classList.add("reduce-motion");
                document.documentElement.setAttribute("data-reduced-motion", "true");
            }
            return;
        }
        if (raw) {
            var v = String(raw).toLowerCase().trim();
            if (v === "reduce-motion" || v === "reduced-motion" || v === "no-motion" || v === "1" || v === "true") {
                if (document.documentElement) {
                    document.documentElement.classList.add("reduce-motion");
                    document.documentElement.setAttribute("data-reduced-motion", "true");
                }
                try { global.localStorage.setItem("innioasis-accessibility", "reduce-motion"); } catch (_) {}
                setSharedCookie("innioasis-accessibility", "reduce-motion");
            } else if (v === "none" || v === "0" || v === "false" || v === "default") {
                if (document.documentElement) {
                    document.documentElement.classList.remove("reduce-motion");
                    document.documentElement.removeAttribute("data-reduced-motion");
                }
                try { global.localStorage.removeItem("innioasis-accessibility"); } catch (_) {}
                setSharedCookie("innioasis-accessibility", "default");
            }
        }
    }
    applyAccessibility();

    /* Accessibility font size adjustment with URL variables & cross-site persistence */
    function applyFontScale() {
        var raw = null;
        try {
            var search = (global.location && global.location.search) || "";
            var p = new URLSearchParams(search);
            raw = p.get("fontSize") || p.get("fontScale") || p.get("font-scale") || p.get("fs") || p.get("lumen-font-scale");
        } catch (_) {}
        var fontScale = 0.8;
        var hasScale = false;
        if (raw) {
            var cleaned = String(raw).trim().replace("%", "");
            var val = parseFloat(cleaned);
            if (val > 10) val = val / 100;
            if (val >= 0.7 && val <= 1.6) {
                fontScale = +(val.toFixed(2));
                hasScale = true;
                try { global.localStorage.setItem("lumen-font-scale-default-80", "1"); } catch (_) {}
            }
        }
        if (!hasScale) {
            var cookieScale = parseFloat(getSharedCookie("lumen-font-scale") || "");
            if (cookieScale >= 0.7 && cookieScale <= 1.6) {
                if (cookieScale === 1 && global.localStorage.getItem("lumen-font-scale-default-80") !== "1") {
                    cookieScale = 0.8;
                    try { global.localStorage.setItem("lumen-font-scale-default-80", "1"); } catch (_) {}
                }
                fontScale = +(cookieScale.toFixed(2));
                hasScale = true;
            }
        }
        if (!hasScale) {
            try {
                var storedScale = parseFloat(global.localStorage.getItem("lumen-font-scale") || "");
                if (storedScale >= 0.7 && storedScale <= 1.6) {
                    if (storedScale === 1 && global.localStorage.getItem("lumen-font-scale-default-80") !== "1") {
                        storedScale = 0.8;
                        global.localStorage.setItem("lumen-font-scale-default-80", "1");
                    }
                    fontScale = +(storedScale.toFixed(2));
                    hasScale = true;
                }
            } catch (_) {}
        }
        if (document.documentElement) {
            document.documentElement.style.setProperty("--lumen-font-scale", String(fontScale));
            document.documentElement.setAttribute("data-font-scale", String(fontScale));
        }
        try { global.localStorage.setItem("lumen-font-scale", String(fontScale)); } catch (_) {}
        setSharedCookie("lumen-font-scale", String(fontScale), 365);
        return fontScale;
    }
    applyFontScale();
    global.y1ApplyFontScale = applyFontScale;

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

    (function rememberDonationsAndLangFromUrl() {
        try {
            var search = (global.location && global.location.search) || "";
            var p = new URLSearchParams(search);
            var d = p.get("donations");
            if (d !== null) {
                var dv = String(d).trim().toLowerCase();
                if (dv === "false" || dv === "0" || dv === "no" || dv === "off") {
                    try { global.localStorage.setItem("innioasis-donations-off", "1"); } catch (_) {}
                    setSharedCookie("innioasis-donations-off", "1");
                } else if (dv === "true" || dv === "1" || dv === "yes" || dv === "on") {
                    try { global.localStorage.removeItem("innioasis-donations-off"); } catch (_) {}
                    setSharedCookie("innioasis-donations-off", "0");
                }
            }
            var l = p.get("lang");
            if (l) {
                var lv = String(l).trim();
                if (lv) {
                    try { global.localStorage.setItem("innioasis-locale", lv); } catch (_) {}
                    setSharedCookie("innioasis-locale", lv);
                }
            }
        } catch (_) {}
    })();

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
            var result = null;
            var raw = params.get("privacy");
            if (raw) {
                var v = String(raw).trim().toLowerCase();
                if (v === "all" || v === "1" || v === "true" || v === "yes") result = { feedback: true, nightly: true };
                else if (v === "none" || v === "0" || v === "false" || v === "no") result = { feedback: false, nightly: false };
                else if (v === "feedback") result = { feedback: true, nightly: false };
                else if (v === "nightly") result = { feedback: false, nightly: true };
            }
            if (!result) {
                var pf = params.get("privacy_feedback");
                var pn = params.get("privacy_nightly");
                if (pf !== null || pn !== null) {
                    result = {
                        feedback: pf === "1" || pf === "true" || pf === "yes",
                        nightly: pn === "1" || pn === "true" || pn === "yes"
                    };
                }
            }
            var analytics = params.get("privacy_analytics");
            if (analytics) {
                var mode = String(analytics).trim().toLowerCase();
                var analyticsMode = null;
                if (mode === "off" || mode === "false" || mode === "0" || mode === "none" || mode === "no") analyticsMode = "off";
                else if (mode === "essential" || mode === "on" || mode === "true" || mode === "1" || mode === "yes") analyticsMode = "essential";
                if (analyticsMode) {
                    if (!result) result = { feedback: true, nightly: true };
                    result.analytics = analyticsMode;
                }
            }
            return result;
        } catch (_) {}
        return null;
    }

    function readConsent() {
        try {
            var fromCookie = getSharedCookie(CONSENT_KEY);
            if (fromCookie) {
                var cookieData = JSON.parse(fromCookie);
                if (cookieData && typeof cookieData === "object") {
                    var parsed = {
                        feedback: typeof cookieData.feedback === "boolean" ? cookieData.feedback : true,
                        nightly: typeof cookieData.nightly === "boolean" ? cookieData.nightly : true,
                        analytics: cookieData.analytics === "off" ? "off" : "essential"
                    };
                    try { global.localStorage.setItem(CONSENT_KEY, JSON.stringify(parsed)); } catch (_) {}
                    return parsed;
                }
            }
        } catch (_) {}

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

        // Default: feedback and nightly selection are enabled for all users by default
        return { feedback: true, nightly: true, analytics: "essential", decided: true };
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
        hasDecided: function () { return true; },
        /* Whether the site may remember a given preference. Theme is always
           allowed; feedback and nightly builds are enabled for all users by default. */
        allows: function (feature) {
            if (feature === "theme") return true;
            var prefs = readConsent();
            if (!prefs) return true;
            if (feature === "analytics") return prefs.analytics !== "off";
            if (feature === "feedback") return prefs.feedback !== false;
            if (feature === "nightly") return prefs.nightly !== false;
            return prefs[feature] !== false;
        }
    };
    global.setSharedCookie = setSharedCookie;
    global.getSharedCookie = getSharedCookie;
    global.y1ApplyAppearance = applyAppearance;
    global.y1GetAppearance = storedAppearance;

    /* ---- Accent colour ---------------------------------------------------
       One accent, derived into every accent token the site already uses, so a
       page keeps its palette but takes the visitor's colour. Three things set
       it: the header picker, an `accent` URL variable (#rrggbb, bare rrggbb,
       rgb()/rgba() or a CSS colour name), and the accent Updater CE sends
       with `ce=true` when it opens an innioasis.app link, read from the
       computer's own theme. The choice is kept locally and mirrored to the
       shared .innioasis.app cookie, like the palette, so both sites agree.
       The computer's accent is stored apart from the visitor's own pick:
       that is what lets the picker offer "Match my PC's theme colours" only
       after the app has handed a colour over, and remember a refusal. */
    var ACCENT_KEY = "lumen-accent";
    var ACCENT_COOKIE = "innioasis-accent";
    var ACCENT_PC_KEY = "innioasis-pc-accent";
    var ACCENT_PC_COOKIE = "innioasis-pc-accent";
    var ACCENT_MATCH_KEY = "innioasis-accent-match-pc";
    var ACCENT_MATCH_COOKIE = "innioasis-accent-match-pc";
    var ACCENT_CE_KEY = "innioasis-referred-by-ce";
    var ACCENT_CE_COOKIE = "innioasis-referred-by-ce";
    var ACCENT_SWATCHES = [
        "#4f8cff", "#7c5cff", "#12b5a5", "#2fb344", "#f0a01a",
        "#ff6b35", "#e5484d", "#e93d82", "#8d6e63", "#6b7280"
    ];
    var ACCENT_TOKENS = [
        "--lumen-accent", "--lumen-accent-strong", "--lumen-accent-wash",
        "--lumen-on-accent", "--site-accent", "--accent", "--primary", "--primary-dark"
    ];

    /* Pages carry their own legacy palette variables, and a page-level
       `--accent` on <body> beats the one set on <html>. Mirroring the accent
       onto the body keeps those older declarations from painting a different
       colour than the rest of the page. */
    function mirrorAccentOnBody(hex) {
        var body = document.body;
        if (!body || !body.style) return;
        if (hex) {
            body.style.setProperty("--accent", hex);
            body.style.setProperty("--primary", hex);
            body.style.setProperty("--primary-dark", "color-mix(in oklab, " + hex + " 84%, black)");
        } else {
            body.style.removeProperty("--accent");
            body.style.removeProperty("--primary");
            body.style.removeProperty("--primary-dark");
        }
    }

    /* Some widgets were drawn before the accent existed and still name a
       literal blue: numbered step circles, primary buttons, progress bars and
       the active tab. These rules put the decorations the accent is supposed
       to cover on the visitor's colour, injected once with !important because
       the rules they override are literal values in older markup. */
    var ACCENT_DECOR_ID = "innioasis-accent-decor-styles";

    function ensureAccentDecorStyles() {
        if (!document || typeof document.createElement !== "function") return;
        if (document.getElementById && document.getElementById(ACCENT_DECOR_ID)) return;
        var style = document.createElement("style");
        style.id = ACCENT_DECOR_ID;
        style.textContent = [
            ".step-number,.progress-step .step-number,.lumen-step-number{",
            "background:var(--lumen-accent,#2563eb)!important;",
            "color:var(--lumen-on-accent,#fff)!important;",
            "border-color:var(--lumen-accent,#2563eb)!important;}",
            ".progress-step.active .step-number,.progress-step.completed .step-number{",
            "background:var(--lumen-accent,#2563eb)!important;",
            "color:var(--lumen-on-accent,#fff)!important;}",
            ".lumen-steps li::before{",
            "background:var(--lumen-accent,#2563eb)!important;",
            "color:var(--lumen-on-accent,#fff)!important;}",
            ".btn-primary,.btn.primary,.button-primary,.btn--primary,.lumen-btn-primary,a.btn-primary{",
            "background:var(--lumen-accent,#2563eb)!important;",
            "border-color:var(--lumen-accent-strong,var(--lumen-accent,#2563eb))!important;",
            "color:var(--lumen-on-accent,#fff)!important;}",
            ".lumen-progress>span,.progress-bar>span,.lumen-bar>span{",
            "background:var(--lumen-accent,#2563eb)!important;}",
            ".lumen-tab.is-active,.tab.is-active,.lumen-chip.is-active,.chip.is-active{",
            "border-color:var(--lumen-accent,#2563eb)!important;",
            "color:var(--lumen-accent,#2563eb)!important;}"
        ].join("");
        try {
            (document.head || document.documentElement).appendChild(style);
        } catch (_) {}
    }

    function accentRead(key, cookie) {
        var value = getSharedCookie(cookie);
        if (!value) {
            try { value = global.localStorage.getItem(key); } catch (_) {}
        }
        return value || null;
    }

    function accentWrite(key, cookie, value) {
        try {
            if (value) global.localStorage.setItem(key, value);
            else global.localStorage.removeItem(key);
        } catch (_) {}
        setSharedCookie(cookie, value || "", value ? 365 : -1);
    }

    function accentHexOf(r, g, b) {
        var clamp = function (n) {
            n = Math.round(Number(n));
            if (isNaN(n)) n = 0;
            return Math.max(0, Math.min(255, n));
        };
        return "#" + ((1 << 24) + (clamp(r) << 16) + (clamp(g) << 8) + clamp(b)).toString(16).slice(1);
    }

    /* Whatever CSS understands becomes one 6-digit hex; anything it does not
       understand, or a fully transparent colour, is rejected so a broken
       link leaves the palette alone instead of painting something arbitrary. */
    function normalizeAccent(value) {
        var text = String(value == null ? "" : value).trim();
        if (!text) return null;
        if (/^[0-9a-f]{3}$/i.test(text) || /^[0-9a-f]{6}$/i.test(text) || /^[0-9a-f]{8}$/i.test(text)) text = "#" + text;
        if (/^#[0-9a-f]{8}$/i.test(text)) text = text.slice(0, 7);
        try {
            if (global.CSS && typeof global.CSS.supports === "function" && !global.CSS.supports("color", text)) {
                return null;
            }
        } catch (_) {}
        try {
            var canvas = document.createElement("canvas");
            canvas.width = 1;
            canvas.height = 1;
            var ctx = canvas.getContext && canvas.getContext("2d");
            if (!ctx) return null;
            ctx.fillStyle = "#000000";
            ctx.fillStyle = text;
            var resolved = String(ctx.fillStyle || "");
            if (/^#[0-9a-f]{6}$/i.test(resolved)) return resolved.toLowerCase();
            if (/^#[0-9a-f]{3}$/i.test(resolved)) {
                return ("#" + resolved.charAt(1) + resolved.charAt(1) +
                    resolved.charAt(2) + resolved.charAt(2) +
                    resolved.charAt(3) + resolved.charAt(3)).toLowerCase();
            }
            var parts = resolved.match(/^rgba?\(\s*([0-9.]+)\s*,\s*([0-9.]+)\s*,\s*([0-9.]+)\s*(?:,\s*([0-9.]+)\s*)?\)$/i);
            if (parts) {
                if (parts[4] !== undefined && Number(parts[4]) === 0) return null;
                return accentHexOf(parts[1], parts[2], parts[3]);
            }
        } catch (_) {}
        return null;
    }

    function accentHsl(hue, sat, light) {
        var h = Number(hue) || 0;
        var s = Math.max(0, Math.min(100, Number(sat))) / 100;
        var l = Math.max(0, Math.min(100, Number(light))) / 100;
        var c = (1 - Math.abs(2 * l - 1)) * s;
        var x = c * (1 - Math.abs(((h / 60) % 2) - 1));
        var m = l - c / 2;
        var r = 0, g = 0, b = 0;
        if (h < 60) { r = c; g = x; }
        else if (h < 120) { r = x; g = c; }
        else if (h < 180) { g = c; b = x; }
        else if (h < 240) { g = x; b = c; }
        else if (h < 300) { r = x; b = c; }
        else { r = c; b = x; }
        return accentHexOf(Math.round((r + m) * 255), Math.round((g + m) * 255), Math.round((b + m) * 255));
    }

    /* The hue of a stored accent, so the hue slider starts where the colour
       already is instead of snapping the page to blue when the tray opens. */
    function accentHue(hex) {
        var value = normalizeAccent(hex);
        if (!value) return 212;
        var r = parseInt(value.slice(1, 3), 16) / 255;
        var g = parseInt(value.slice(3, 5), 16) / 255;
        var b = parseInt(value.slice(5, 7), 16) / 255;
        var max = Math.max(r, g, b), min = Math.min(r, g, b), delta = max - min;
        if (!delta) return 0;
        var hue;
        if (max === r) hue = ((g - b) / delta) % 6;
        else if (max === g) hue = (b - r) / delta + 2;
        else hue = (r - g) / delta + 4;
        hue *= 60;
        return Math.round(hue < 0 ? hue + 360 : hue);
    }

    /* Text drawn on the accent: dark ink on light colours, white on dark
       ones, by relative luminance rather than by guesswork. */
    function accentInk(hex) {
        var value = String(hex || "").replace("#", "");
        if (value.length !== 6) return "#ffffff";
        var channel = function (i) {
            var c = parseInt(value.slice(i, i + 2), 16) / 255;
            return c <= 0.03928 ? c / 12.92 : Math.pow((c + 0.055) / 1.055, 2.4);
        };
        var luminance = 0.2126 * channel(0) + 0.7152 * channel(2) + 0.0722 * channel(4);
        return luminance > 0.45 ? "#0a0b0f" : "#ffffff";
    }

    /* Browsers expose no API for the OS accent, but the CSS AccentColor
       system colour resolves to it where it is supported. Read it from a
       probe and compare against an inherited probe, so a browser that does
       not know the keyword (and simply inherits the text colour) is not
       mistaken for a real match. */
    function browserAccent() {
        try {
            if (!global.CSS || typeof global.CSS.supports !== "function") return null;
            if (!global.CSS.supports("color", "AccentColor")) return null;
            var host = document.body || document.documentElement;
            if (!host) return null;
            var probe = document.createElement("span");
            probe.style.cssText = "position:absolute;left:-9999px;top:-9999px;color:AccentColor";
            var control = document.createElement("span");
            control.style.cssText = "position:absolute;left:-9999px;top:-9999px;color:inherit";
            host.appendChild(probe);
            host.appendChild(control);
            var accent = normalizeAccent(global.getComputedStyle(probe).color);
            var inherited = normalizeAccent(global.getComputedStyle(control).color);
            host.removeChild(probe);
            host.removeChild(control);
            if (!accent || accent === inherited) return null;
            return accent;
        } catch (_) {
            return null;
        }
    }

    function currentAccent() {
        if (document.documentElement) {
            var attr = document.documentElement.getAttribute("data-accent");
            if (attr) return attr;
        }
        return normalizeAccent(accentRead(ACCENT_KEY, ACCENT_COOKIE));
    }

    function pcAccent() {
        return normalizeAccent(accentRead(ACCENT_PC_KEY, ACCENT_PC_COOKIE));
    }

    /* Un-ticked is stored as "0"; anything else means "follow the computer",
       which is what a first visit does once the app has handed a colour over. */
    function matchesPcTheme() {
        return accentRead(ACCENT_MATCH_KEY, ACCENT_MATCH_COOKIE) !== "0";
    }

    function referredByCe() {
        return Boolean(accentRead(ACCENT_CE_KEY, ACCENT_CE_COOKIE));
    }

    function applyAccent(value, persist) {
        var root = document.documentElement;
        var hex = value ? normalizeAccent(value) : null;
        ensureAccentDecorStyles();
        if (root) {
            if (hex) {
                root.style.setProperty("--lumen-accent", hex);
                root.style.setProperty("--lumen-accent-strong", "color-mix(in oklab, " + hex + " 84%, black)");
                root.style.setProperty("--lumen-accent-wash", "color-mix(in srgb, " + hex + " 30%, transparent)");
                root.style.setProperty("--lumen-on-accent", accentInk(hex));
                root.style.setProperty("--site-accent", hex);
                root.style.setProperty("--primary", hex);
                root.style.setProperty("--primary-dark", "color-mix(in oklab, " + hex + " 84%, black)");
                root.setAttribute("data-accent", hex);
            } else {
                for (var i = 0; i < ACCENT_TOKENS.length; i++) {
                    root.style.removeProperty(ACCENT_TOKENS[i]);
                }
                root.removeAttribute("data-accent");
            }
        }
        /* site-init can run before <body> exists, so the body mirror also
           happens on DOMContentLoaded below. */
        mirrorAccentOnBody(hex);
        if (persist) accentWrite(ACCENT_KEY, ACCENT_COOKIE, hex);
        syncAccentPicker();
        try {
            global.dispatchEvent(new CustomEvent("innioasis-accent-change", { detail: { accent: hex } }));
        } catch (_) {}
        return hex;
    }

    function setMatchPcTheme(enabled) {
        accentWrite(ACCENT_MATCH_KEY, ACCENT_MATCH_COOKIE, enabled ? "1" : "0");
        if (enabled) {
            var pc = pcAccent();
            if (pc) applyAccent(pc, true);
        }
        syncAccentPicker();
    }

    /* The early call paints the tokens on <html> before first paint; this one
       repeats it once <body> is there so page-level palette variables pick the
       same colour up. */
    try {
        document.addEventListener("DOMContentLoaded", function () {
            applyAccent(currentAccent(), false);
        });
    } catch (_) {}

    function applyStoredAccent() {
        var params = null;
        try {
            params = new URLSearchParams((global.location && global.location.search) || "");
        } catch (_) {}
        var urlAccent = params
            ? (params.get("accent") || params.get("accent_color") || params.get("accent-color") ||
                params.get("accentColor") || params.get("accentColour"))
            : null;
        var ceParam = params ? params.get("ce") : null;
        var fromCe = ceParam !== null && /^(|1|true|yes|on)$/i.test(String(ceParam).trim());

        if (fromCe) accentWrite(ACCENT_CE_KEY, ACCENT_CE_COOKIE, "1");

        var handed = normalizeAccent(urlAccent);
        /* The app sends the accent it read from the desktop; when it could
           not read one it still marks the handoff, and the browser's own
           AccentColor is the next best source. */
        if (fromCe && !handed) handed = browserAccent();

        if (handed) {
            if (fromCe) {
                accentWrite(ACCENT_PC_KEY, ACCENT_PC_COOKIE, handed);
                if (matchesPcTheme()) return void applyAccent(handed, true);
                /* Refused on an earlier visit: keep the visitor's own colour
                   instead of overriding it every time the app opens a page. */
                return void applyAccent(accentRead(ACCENT_KEY, ACCENT_COOKIE), false);
            }
            return void applyAccent(handed, true);
        }

        var pc = pcAccent();
        if (pc && matchesPcTheme()) return void applyAccent(pc, false);
        applyAccent(accentRead(ACCENT_KEY, ACCENT_COOKIE), false);
    }

    var pickerHsv = { h: 220, s: 0.72, v: 1 };

    function hexToHsv(hex) {
        var n = normalizeAccent(hex);
        if (!n) return null;
        var r = parseInt(n.slice(1, 3), 16) / 255;
        var g = parseInt(n.slice(3, 5), 16) / 255;
        var b = parseInt(n.slice(5, 7), 16) / 255;
        var max = Math.max(r, g, b);
        var min = Math.min(r, g, b);
        var d = max - min;
        var h = 0;
        if (d) {
            if (max === r) h = ((g - b) / d) % 6;
            else if (max === g) h = (b - r) / d + 2;
            else h = (r - g) / d + 4;
            h *= 60;
            if (h < 0) h += 360;
        }
        return { h: h, s: max ? d / max : 0, v: max };
    }

    function hsvToHex(h, s, v) {
        var c = v * s;
        var x = c * (1 - Math.abs((h / 60) % 2 - 1));
        var m = v - c;
        var r = 0;
        var g = 0;
        var b = 0;
        if (h < 60) { r = c; g = x; }
        else if (h < 120) { r = x; g = c; }
        else if (h < 180) { g = c; b = x; }
        else if (h < 240) { g = x; b = c; }
        else if (h < 300) { r = x; b = c; }
        else { r = c; b = x; }
        function byte(channel) {
            var value = Math.max(0, Math.min(255, Math.round((channel + m) * 255)));
            var text = value.toString(16);
            return text.length < 2 ? "0" + text : text;
        }
        return "#" + byte(r) + byte(g) + byte(b);
    }

    function paintSpectrum(hex) {
        var hsv = hexToHsv(hex || currentAccent() || "#4f8cff");
        if (!hsv) return;
        pickerHsv = hsv;
        var pad = document.getElementById("lumen-accent-pad");
        var thumb = document.getElementById("lumen-accent-pad-thumb");
        var hue = document.getElementById("lumen-accent-hue");
        if (pad) pad.style.setProperty("--hue", hsvToHex(hsv.h, 1, 1));
        if (thumb) {
            thumb.style.left = (hsv.s * 100) + "%";
            thumb.style.top = ((1 - hsv.v) * 100) + "%";
            thumb.style.background = normalizeAccent(hex) || hsvToHex(hsv.h, hsv.s, hsv.v);
        }
        if (hue && document.activeElement !== hue) hue.value = String(Math.round(hsv.h));
    }

    function accentPickerMarkup() {
        var swatches = "";
        for (var i = 0; i < ACCENT_SWATCHES.length; i++) {
            swatches += '<button type="button" class="lumen-accent-swatch" data-accent-value="' +
                ACCENT_SWATCHES[i] + '" style="--swatch:' + ACCENT_SWATCHES[i] +
                '" aria-label="Use ' + ACCENT_SWATCHES[i] + '" aria-pressed="false"></button>';
        }
        return '<div class="lumen-accent-wrap" id="lumen-accent-picker">' +
            '<button type="button" class="lumen-accent-toggle" id="lumen-accent-toggle" ' +
            'aria-expanded="false" aria-controls="lumen-accent-tray" aria-label="Accent colour" title="Accent colour">' +
            '<span class="lumen-accent-dot" id="lumen-accent-dot" aria-hidden="true"></span>' +
            '</button>' +
            '<div class="lumen-accent-tray" id="lumen-accent-tray" hidden>' +
            '<p class="lumen-accent-heading">Accent colour</p>' +
            '<div class="lumen-accent-pad" id="lumen-accent-pad" role="slider" aria-label="Saturation and brightness" aria-valuemin="0" aria-valuemax="100">' +
            '<span class="lumen-accent-pad-thumb" id="lumen-accent-pad-thumb"></span></div>' +
            '<label class="lumen-accent-row">Hue' +
            '<input type="range" id="lumen-accent-hue" class="lumen-accent-hue" min="0" max="360" step="1" value="220" aria-label="Hue"></label>' +
            '<label class="lumen-accent-row">Hex' +
            '<input type="text" id="lumen-accent-hex" class="lumen-accent-hex" value="" placeholder="#4f8cff" spellcheck="false" autocapitalize="off" maxlength="9" aria-label="Accent hex code" inputmode="text"></label>' +
            '<label class="lumen-accent-row">' +
            '<input type="color" id="lumen-accent-input" value="#4f8cff" aria-label="Accent colour"></label>' +
            '<div class="lumen-accent-swatches">' + swatches + '</div>' +
            '<label class="lumen-accent-row lumen-accent-range-row">Hue' +
            '<input type="range" id="lumen-accent-hue" class="lumen-accent-hue" min="0" max="359" step="1" value="212" aria-label="Accent hue"></label>' +
            '<button type="button" class="lumen-accent-eyedrop" id="lumen-accent-eyedrop" hidden>Pick a colour from the screen</button>' +
            '<label class="lumen-accent-match" id="lumen-accent-match-row" hidden>' +
            '<input type="checkbox" id="lumen-accent-match"><span>Match my PC\'s theme colours</span></label>' +
            '<button type="button" class="lumen-accent-reset" id="lumen-accent-reset">Use the site default</button>' +
            '</div></div>';
    }

    function accentPickerNode() {
        var host = document.createElement("div");
        host.innerHTML = accentPickerMarkup();
        return host.firstChild;
    }

    function syncAccentPicker() {
        var picker = document.getElementById("lumen-accent-picker");
        if (!picker) return;
        var accent = currentAccent();
        var dot = document.getElementById("lumen-accent-dot");
        if (dot) dot.style.background = accent || "";
        var input = document.getElementById("lumen-accent-input");
        if (input) input.value = accent || "#4f8cff";
        var hexField = document.getElementById("lumen-accent-hex");
        if (hexField && document.activeElement !== hexField) hexField.value = accent || "";
        var swatches = picker.querySelectorAll(".lumen-accent-swatch");
        for (var i = 0; i < swatches.length; i++) {
            swatches[i].setAttribute("aria-pressed",
                swatches[i].getAttribute("data-accent-value") === accent ? "true" : "false");
        }
        var hueField = document.getElementById("lumen-accent-hue");
        if (hueField) hueField.value = String(accentHue(accent));
        var eyedropButton = document.getElementById("lumen-accent-eyedrop");
        if (eyedropButton) eyedropButton.hidden = typeof global.EyeDropper !== "function";
        var pc = pcAccent();
        var matchRow = document.getElementById("lumen-accent-match-row");
        var matchInput = document.getElementById("lumen-accent-match");
        if (matchRow) matchRow.hidden = !pc;
        if (matchInput) {
            matchInput.disabled = !pc;
            matchInput.checked = Boolean(pc) && matchesPcTheme();
        }
        var reset = document.getElementById("lumen-accent-reset");
        if (reset) reset.disabled = !accent;
        paintSpectrum(accent);
    }

    function wireAccentPicker() {
        var picker = document.getElementById("lumen-accent-picker");
        if (!picker) return;
        var toggle = document.getElementById("lumen-accent-toggle");
        var tray = document.getElementById("lumen-accent-tray");
        var input = document.getElementById("lumen-accent-input");
        var hexField = document.getElementById("lumen-accent-hex");
        var matchInput = document.getElementById("lumen-accent-match");
        var reset = document.getElementById("lumen-accent-reset");
        var hue = document.getElementById("lumen-accent-hue");
        var eyedrop = document.getElementById("lumen-accent-eyedrop");

        if (hue) {
            hue.addEventListener("input", function () {
                setMatchPcTheme(false);
                applyAccent(accentHsl(hue.value, 72, 55), true);
            });
        }
        /* Chromium can sample any pixel on screen; elsewhere the native colour
           input already opens the system picker, so the button stays hidden. */
        if (eyedrop && typeof global.EyeDropper === "function") {
            eyedrop.addEventListener("click", function () {
                new global.EyeDropper().open().then(function (result) {
                    var picked = normalizeAccent(result && result.sRGBHex);
                    if (!picked) return;
                    setMatchPcTheme(false);
                    applyAccent(picked, true);
                }).catch(function () {});
            });
        }

        function placeTray() {
            if (!tray || !toggle || tray.hidden) return;
            if (tray.parentNode !== document.body) document.body.appendChild(tray);
            var rect = toggle.getBoundingClientRect();
            var width = tray.offsetWidth || 280;
            var height = tray.offsetHeight || 360;
            var left = rect.right - width;
            if (left < 8) left = 8;
            if (left + width > window.innerWidth - 8) left = Math.max(8, window.innerWidth - width - 8);
            var top = rect.bottom + 8;
            if (top + height > window.innerHeight - 8) top = Math.max(8, rect.top - height - 8);
            tray.style.top = Math.round(top) + "px";
            tray.style.left = Math.round(left) + "px";
            tray.style.right = "auto";
        }
        function setOpen(open) {
            if (!tray) return;
            tray.hidden = !open;
            if (toggle) toggle.setAttribute("aria-expanded", open ? "true" : "false");
            if (open) placeTray();
        }
        window.addEventListener("resize", placeTray);
        window.addEventListener("scroll", placeTray, true);
        if (toggle) {
            toggle.addEventListener("click", function (event) {
                event.preventDefault();
                event.stopPropagation();
                setOpen(tray ? tray.hidden : false);
            });
        }
        /* A colour the visitor picks is their own, so it turns the PC match off:
           otherwise the next page Updater CE opens sees the match still ticked
           and puts the desktop colour back over the one they just chose. */
        if (input) {
            input.addEventListener("input", function () { applyAccent(input.value, false); });
            input.addEventListener("change", function () {
                setMatchPcTheme(false);
                applyAccent(input.value, true);
            });
        }
        function commitHex() {
            if (!hexField) return;
            var next = normalizeAccent(hexField.value);
            if (!next) return;
            setMatchPcTheme(false);
            applyAccent(next, true);
        }
        if (hexField) {
            hexField.addEventListener("change", commitHex);
            hexField.addEventListener("keydown", function (event) {
                if (event.key !== "Enter") return;
                event.preventDefault();
                commitHex();
            });
        }
        var pad = document.getElementById("lumen-accent-pad");
        var hue = document.getElementById("lumen-accent-hue");
        function fromPad(event, persist) {
            if (!pad) return;
            var rect = pad.getBoundingClientRect();
            pickerHsv.s = Math.min(1, Math.max(0, (event.clientX - rect.left) / Math.max(1, rect.width)));
            pickerHsv.v = Math.min(1, Math.max(0, 1 - (event.clientY - rect.top) / Math.max(1, rect.height)));
            var next = hsvToHex(pickerHsv.h, pickerHsv.s, pickerHsv.v);
            if (persist) setMatchPcTheme(false);
            applyAccent(next, persist);
        }
        if (pad) {
            pad.addEventListener("pointerdown", function (event) {
                if (pad.setPointerCapture) pad.setPointerCapture(event.pointerId);
                fromPad(event, false);
            });
            pad.addEventListener("pointermove", function (event) {
                if (pad.hasPointerCapture && !pad.hasPointerCapture(event.pointerId)) return;
                fromPad(event, false);
            });
            pad.addEventListener("pointerup", function (event) { fromPad(event, true); });
        }
        if (hue) {
            hue.addEventListener("input", function () {
                pickerHsv.h = Number(hue.value) || 0;
                applyAccent(hsvToHex(pickerHsv.h, pickerHsv.s, pickerHsv.v), false);
            });
            hue.addEventListener("change", function () {
                setMatchPcTheme(false);
                applyAccent(hsvToHex(pickerHsv.h, pickerHsv.s, pickerHsv.v), true);
            });
        }
        picker.addEventListener("click", function (event) {
            var swatch = event.target && event.target.closest ? event.target.closest(".lumen-accent-swatch") : null;
            if (!swatch) return;
            setMatchPcTheme(false);
            applyAccent(swatch.getAttribute("data-accent-value"), true);
        });
        if (matchInput) {
            matchInput.addEventListener("change", function () {
                setMatchPcTheme(Boolean(matchInput.checked));
            });
        }
        if (reset) {
            reset.addEventListener("click", function () {
                setMatchPcTheme(false);
                applyAccent(null, true);
            });
        }
        document.addEventListener("click", function (event) {
            if (!tray || tray.hidden) return;
            if (tray.contains(event.target) || (toggle && toggle.contains(event.target))) return;
            setOpen(false);
        });
        document.addEventListener("keydown", function (event) {
            if (event.key === "Escape") setOpen(false);
        });
        syncAccentPicker();
    }

    function accentHost() {
        var candidates = [
            document.querySelector("#nav-root .nav-tools"),
            document.querySelector(".gallery-topbar"),
            document.querySelector(".nav-tools")
        ];
        var first = null;
        for (var i = 0; i < candidates.length; i++) {
            if (!candidates[i]) continue;
            if (!first) first = candidates[i];
            if (candidates[i].getClientRects().length) return candidates[i];
        }
        return first;
    }

    function mountAccentPicker() {
        var existing = document.getElementById("lumen-accent-picker");
        var host = accentHost();
        if (existing) {
            /* The themes gallery mounts a header of its own; move the control
               if this page's live header changed underneath it. */
            if (host && existing.parentNode !== host) host.appendChild(existing);
            syncAccentPicker();
            return;
        }
        if (!host) return;
        var anchor = host.querySelector(".lumen-theme-control");
        if (anchor && anchor.parentNode === host) host.insertBefore(accentPickerNode(), anchor);
        else host.appendChild(accentPickerNode());
        wireAccentPicker();
    }

    applyStoredAccent();

    try {
        global.addEventListener("storage", function (event) {
            if (!event) return;
            if (event.key !== ACCENT_KEY && event.key !== ACCENT_PC_KEY && event.key !== ACCENT_MATCH_KEY) return;
            var pc = pcAccent();
            if (pc && matchesPcTheme()) applyAccent(pc, false);
            else applyAccent(accentRead(ACCENT_KEY, ACCENT_COOKIE), false);
        });
    } catch (_) {}

    global.y1Accent = {
        get: currentAccent,
        set: function (value) { return applyAccent(value, true); },
        clear: function () { return applyAccent(null, true); },
        normalize: normalizeAccent,
        pc: pcAccent,
        hasPcAccent: function () { return Boolean(pcAccent()); },
        matchesPcTheme: matchesPcTheme,
        setMatchPcTheme: setMatchPcTheme,
        referredByCe: referredByCe
    };
    global.y1GetAccent = currentAccent;
    global.y1SetAccent = function (value) { return applyAccent(value, true); };
    global.y1ApplyAccent = applyAccent;
    global.y1HasPcAccent = function () { return Boolean(pcAccent()); };

    function clearPreferenceParamsFromUrl() {
        if (!global.location || !global.history || !global.history.replaceState) return;
        try {
            var url = new URL(global.location.href);
            var params = url.searchParams;
            var modified = false;

            var prefKeys = [
                "privacy",
                "privacy_analytics",
                "privacy_feedback",
                "privacy_nightly",
                "donations",
                "site_theme",
                "accent",
                "accent_color",
                "accent-color",
                "accentColor",
                "accentColour",
                "ce",
                "accessibility",
                "a11y",
                "reduce-motion",
                "reduce_motion",
                "lang",
                "analytics",
                "telemetry",
                "fontSize",
                "fontScale",
                "font-scale",
                "fs",
                "lumen-font-scale",
                "utm_source",
                "utm_medium",
                "utm_campaign",
                "utm_term",
                "utm_content",
                "ref",
                "fbclid",
                "gclid"
            ];

            if (params.has("theme")) {
                var tVal = (params.get("theme") || "").toLowerCase().trim();
                var isSiteTheme = ["auto", "dark", "high-contrast", "2077", "light"].indexOf(tVal) >= 0;
                /* theme.html?theme= names a gallery theme someone can share.
                   Only an appearance value (dark, light, …) is a preference. */
                if (isSiteTheme) {
                    params.delete("theme");
                    modified = true;
                }
            }

            prefKeys.forEach(function (k) {
                if (params.has(k)) {
                    params.delete(k);
                    modified = true;
                }
            });

            if (modified) {
                var searchStr = params.toString();
                var newUrl = url.pathname + (searchStr ? ("?" + searchStr) : "") + url.hash;
                global.history.replaceState(global.history.state, document.title, newUrl);
            }
        } catch (_) {}
    }

    global.y1ClearPreferencesFromUrl = clearPreferenceParamsFromUrl;
    /* Run immediately synchronously so address bar transforms before first paint */
    clearPreferenceParamsFromUrl();

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", clearPreferenceParamsFromUrl);
    } else {
        if (typeof setTimeout === "function") {
            setTimeout(clearPreferenceParamsFromUrl, 0);
        } else {
            clearPreferenceParamsFromUrl();
        }
    }
    window.addEventListener("load", clearPreferenceParamsFromUrl);

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
        control.innerHTML = '<span>Theme</span><select aria-label="Choose site colour theme"><option value="auto">Auto</option><option value="dark">Dark</option><option value="light">Light</option><option value="high-contrast">High contrast</option><option value="2077">2077</option></select>';
        var select = control.querySelector("select");
        select.value = storedAppearance();
        select.addEventListener("change", function () { applyAppearance(select.value, true); });
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

    function pinDockToViewport() {
        var dock = document.getElementById("support-toolbar-container");
        if (dock && dock.parentNode !== document.body) document.body.appendChild(dock);
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
                    pinDockToViewport();
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
            mountAccentPicker();
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

    /* In-page downloads live in their own file so this shell stays readable.
       Pages need no extra script tag: the module is fetched from the directory
       that holds this script and upgrades every download link it finds. */
    function loadSiteDownloads() {
        if (global.InnioasisDownloads || document.getElementById("site-downloads-script")) return;
        var base = "";
        try {
            var scripts = document.getElementsByTagName("script");
            for (var i = 0; i < scripts.length; i++) {
                var src = scripts[i].src || "";
                if (src.indexOf("site-init.js") === -1) continue;
                base = src.replace(/[?#].*$/, "").replace(/[^/]*$/, "");
                break;
            }
        } catch (_) {}
        var node = document.createElement("script");
        node.id = "site-downloads-script";
        node.src = base + "site-downloads.js?v=20261109dl";
        node.defer = true;
        document.head.appendChild(node);
    }
    loadSiteDownloads();

    global.y1LoadSupportToolbar = loadSupportToolbar;
})(typeof window !== "undefined" ? window : globalThis);
