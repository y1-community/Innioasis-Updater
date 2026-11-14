/* One platform's downloads, with the rest behind "Other downloads".
 *
 * Every release row offers a package per computer, and the installer cards on
 * the guide pages repeat that per platform. Seeing all of them at once makes
 * a reader compare filenames to find the one that runs, and on an older or
 * 32-bit machine the useful button sits beside two that cannot work there.
 *
 * This module keeps the build for the visitor's computer in place and puts
 * the others behind a plain text button, so nothing is hidden from someone
 * collecting a package for a different machine. A visitor whose platform is
 * unknown, and every phone or tablet, sees the full list unchanged.
 */
(function (global) {
    "use strict";
    var doc = global.document;
    if (!doc || !global.addEventListener) return;
    if (global.InnioasisDownloadChoices) return;

    var GROUPS = ".lumen-portable-downloads, .lumen-zip-download-row, .lumen-download-options[data-platform-detect]";
    /* The first entry of each list is the exact build, the next one is the
       build that still runs on that computer. Windows on ARM uses the x64
       package through emulation, and a 32-bit visitor can open the ordinary
       build of their platform as a fallback when the legacy one is missing. */
    var MATCH = {
        "windows-legacy": ["windows-legacy", "windows"],
        "linux-legacy": ["linux-legacy", "linux"],
        "windows": ["windows"],
        "windows-arm64": ["windows-arm64", "windows"],
        "linux": ["linux"],
        "linux-arm64": ["linux-arm64", "linux"],
        "macos": ["macos"]
    };
    var HEADER = "Other downloads";
    var FEWER = "Show fewer";

    function legacyKey() {
        try {
            var marker = global.INNIOASIS_LEGACY;
            return marker && marker.isLegacy ? String(marker.platformKey || "windows-legacy") : "";
        } catch (_) {
            return "";
        }
    }

    function browserKey() {
        var ua = String((global.navigator && global.navigator.userAgent) || "");
        if (/android|iphone|ipad|ipod|mobile|tablet|kindle|silk/i.test(ua)) return "";
        var platform = String((global.navigator && global.navigator.platform) || "") + " " + ua;
        if (/win/i.test(platform)) return /arm64/i.test(ua) ? "windows-arm64" : "windows";
        if (/mac/i.test(platform)) return "macos";
        if (/linux|x11/i.test(platform)) return /aarch64|arm64/i.test(ua) ? "linux-arm64" : "linux";
        return "";
    }

    function visitorKey() {
        return legacyKey() || browserKey();
    }

    function itemsOf(group) {
        var nodes = group.querySelectorAll("a[data-platform], .lumen-download-option[data-platform]");
        return Array.prototype.filter.call(nodes, function (node) {
            return Boolean(node.getAttribute("data-platform"));
        });
    }

    function chosen(items, key) {
        var order = MATCH[key] || [];
        for (var i = 0; i < order.length; i++) {
            var found = items.filter(function (item) {
                return String(item.getAttribute("data-platform") || "") === order[i];
            });
            if (found.length) return found;
        }
        return [];
    }

    function injectStyles() {
        if (doc.getElementById("site-download-choices-styles")) return;
        var style = doc.createElement("style");
        style.id = "site-download-choices-styles";
        style.textContent = [
            ".lumen-other-downloads{display:inline-flex;align-items:center;gap:.3rem;margin:.35rem 0 .15rem;padding:0;border:0;background:none;color:var(--lumen-muted,#9aa3b5);font:inherit;font-size:.82rem;text-decoration:underline;text-underline-offset:3px;cursor:pointer;}",
            ".lumen-other-downloads:hover{color:var(--lumen-text,#f4f6fb);}",
            ".lumen-other-downloads:focus-visible{outline:2px solid var(--lumen-accent,#6b9fff);outline-offset:3px;border-radius:4px;}",
            ".lumen-other-downloads svg{transition:transform .15s ease;}",
            ".lumen-other-downloads[aria-expanded=\"true\"] svg{transform:rotate(180deg);}",
            "@media (prefers-reduced-motion: reduce){.lumen-other-downloads svg{transition:none;}}"
        ].join("");
        (doc.head || doc.documentElement).appendChild(style);
    }

    function toggleFor(group) {
        var next = group.nextElementSibling;
        if (next && next.classList && next.classList.contains("lumen-other-downloads")) return next;
        var button = doc.createElement("button");
        button.type = "button";
        button.className = "lumen-other-downloads";
        button.setAttribute("aria-expanded", "false");
        button.setAttribute("data-other-downloads", "1");
        button.innerHTML = '<span data-other-label>' + HEADER + '</span>' +
            '<svg viewBox="0 0 16 16" width="11" height="11" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m4 6 4 4 4-4"/></svg>';
        group.parentNode.insertBefore(button, group.nextSibling);
        return button;
    }

    function apply(group) {
        var key = visitorKey();
        if (!key || !MATCH[key]) return;
        /* site-legacy.js replaces the installer card on an older or 32-bit
           machine and hides the original. Nothing in it can be pressed, so a
           disclosure button there would only be dead markup. */
        if (group.closest("[hidden], [aria-hidden='true']")) return;
        var items = itemsOf(group);
        if (items.length < 2) return;
        var shown = chosen(items, key);
        if (!shown.length) return;
        var signature = key + ":" + items.length + ":" + shown.length;
        if (group.getAttribute("data-choices") === signature) return;
        group.setAttribute("data-choices", signature);

        var hidden = items.filter(function (item) { return shown.indexOf(item) === -1; });
        shown.forEach(function (item) { item.hidden = false; });
        hidden.forEach(function (item) { item.hidden = true; });

        /* A group that now shows every package needs no disclosure. */
        if (!hidden.length) {
            var existing = group.nextElementSibling;
            if (existing && existing.classList && existing.classList.contains("lumen-other-downloads")) {
                existing.parentNode.removeChild(existing);
            }
            return;
        }

        var button = toggleFor(group);
        var label = button.querySelector("[data-other-label]");
        button.setAttribute("aria-expanded", "false");
        if (label) label.textContent = HEADER;
        button.onclick = function () {
            var open = button.getAttribute("aria-expanded") === "true";
            hidden.forEach(function (item) { item.hidden = open; });
            button.setAttribute("aria-expanded", open ? "false" : "true");
            if (label) label.textContent = open ? HEADER : FEWER;
        };
    }

    function applyAll(root) {
        Array.prototype.forEach.call((root || doc).querySelectorAll(GROUPS), apply);
    }

    var timer = null;
    function schedule() {
        if (timer) return;
        timer = global.setTimeout(function () {
            timer = null;
            applyAll(doc);
        }, 120);
    }

    function boot() {
        injectStyles();
        applyAll(doc);
        /* The catalogue and the firmware tables paint after this module
           starts, and site-legacy.js renames a button once it has detected an
           older system, so the groups are re-read rather than cached. */
        if (global.MutationObserver) {
            new MutationObserver(schedule).observe(doc.body, { childList: true, subtree: true });
        }
        global.setTimeout(schedule, 400);
        global.setTimeout(schedule, 1500);
        global.addEventListener("y1-locale-change", schedule);
    }

    global.InnioasisDownloadChoices = {
        platform: visitorKey,
        apply: schedule
    };

    if (doc.readyState === "loading") doc.addEventListener("DOMContentLoaded", boot);
    else boot();
})(typeof window !== "undefined" ? window : globalThis);
