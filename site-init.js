/**
 * Shared site shell: body classes, bottom dock, and privacy button (theme-analytics).
 */
(function (global) {
    "use strict";

    var THEME_ANALYTICS_VERSION = "20260524b";
    var THEME_ANALYTICS_CSS_VERSION = "20260518";

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

    function themeAnalyticsScriptCandidates() {
        return [
            "theme-analytics.js?v=" + THEME_ANALYTICS_VERSION,
            "../theme-analytics.js?v=" + THEME_ANALYTICS_VERSION,
            "../../theme-analytics.js?v=" + THEME_ANALYTICS_VERSION,
            "../../../theme-analytics.js?v=" + THEME_ANALYTICS_VERSION,
            "https://themes.innioasis.app/theme-analytics.js?v=" + THEME_ANALYTICS_VERSION,
        ];
    }

    function themeAnalyticsCssHref() {
        try {
            return new URL(
                "theme-analytics.css?v=" + THEME_ANALYTICS_CSS_VERSION,
                document.baseURI || global.location.href
            ).href;
        } catch (_) {
            return (
                "https://themes.innioasis.app/theme-analytics.css?v=" +
                THEME_ANALYTICS_CSS_VERSION
            );
        }
    }

    function themeAnalyticsAlreadyIncluded() {
        if (global.ThemeAnalytics) return true;
        if (document.getElementById("y1-privacy-settings-btn")) return true;
        return !!document.querySelector('script[src*="theme-analytics.js"]');
    }

    function ensureThemeAnalyticsCss() {
        if (document.querySelector('link[href*="theme-analytics.css"]')) return;
        var link = document.createElement("link");
        link.rel = "stylesheet";
        link.href = themeAnalyticsCssHref();
        document.head.appendChild(link);
    }

    function waitForThemeAnalytics(maxMs) {
        return new Promise(function (resolve) {
            if (themeAnalyticsAlreadyIncluded()) {
                resolve();
                return;
            }
            var start = Date.now();
            var timer = setInterval(function () {
                if (themeAnalyticsAlreadyIncluded()) {
                    clearInterval(timer);
                    resolve();
                } else if (Date.now() - start >= maxMs) {
                    clearInterval(timer);
                    resolve();
                }
            }, 50);
        });
    }

    function notifyDockReady() {
        try {
            global.dispatchEvent(new CustomEvent("y1-dock-slot-ready"));
        } catch (_) {}
    }

    function loadThemeAnalyticsOnce() {
        if (themeAnalyticsAlreadyIncluded()) {
            return waitForThemeAnalytics(10000).then(notifyDockReady);
        }
        if (global.__y1ThemeAnalyticsLoading) {
            return global.__y1ThemeAnalyticsLoading.then(notifyDockReady);
        }

        ensureThemeAnalyticsCss();

        global.__y1ThemeAnalyticsLoading = new Promise(function (resolve) {
            var candidates = themeAnalyticsScriptCandidates();
            var index = 0;

            function tryNext() {
                if (index >= candidates.length) {
                    resolve();
                    return;
                }
                var src = candidates[index++];
                var script = document.createElement("script");
                script.src = src;
                script.async = true;
                script.dataset.y1ThemeAnalytics = "1";
                script.onload = function () {
                    resolve();
                };
                script.onerror = function () {
                    tryNext();
                };
                document.head.appendChild(script);
            }

            tryNext();
        }).then(notifyDockReady);

        return global.__y1ThemeAnalyticsLoading;
    }

    async function loadSupportToolbar() {
        var slot = document.getElementById("support-toolbar-slot");
        if (!slot || slot.dataset.shellLoaded === "1") return;
        for (var i = 0; i < toolbarCandidates().length; i++) {
            try {
                var res = await fetch(toolbarCandidates()[i], { cache: "no-cache" });
                if (!res.ok) continue;
                slot.innerHTML = await res.text();
                executeInlineScripts(slot);
                slot.dataset.shellLoaded = "1";
                notifyDockReady();
                return;
            } catch (_) {}
        }
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
        }
        await loadThemeAnalyticsOnce();
    }

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", function () {
            void init();
        });
    } else {
        void init();
    }

    global.y1LoadSupportToolbar = loadSupportToolbar;
    global.y1LoadThemeAnalytics = loadThemeAnalyticsOnce;
})(typeof window !== "undefined" ? window : globalThis);
