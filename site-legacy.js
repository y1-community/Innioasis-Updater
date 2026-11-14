/* Older Windows and 32-bit Linux.
 *
 * Updater CE is published for 64-bit Windows 10 and 11, macOS, x86-64 Linux
 * and ARM64 Linux. A reader on Windows XP through 8.1, on any 32-bit Windows,
 * or on a 32-bit Intel Linux desktop cannot run any of those builds. Their
 * player is still supported: every firmware release also has a legacy zip
 * that carries a small stand-alone installer beside the rom, and that
 * installer runs on those systems.
 *
 * This module notices such a visit and changes what the page offers:
 *
 *   - the Updater CE download card becomes a store-style button for the
 *     software install zip built for this computer;
 *   - "Get Updater CE" on the home page becomes "Browse firmwares", and the
 *     other Updater CE calls to action become "Get the software install zip";
 *   - the firmware table's own button for this platform is renamed.
 *
 * Nothing is injected as a callout: a reader on an older computer sees the same
 * pages as everyone else, with the download and the guide links pointing at the
 * package that computer can actually use.
 *
 * The zip is the archive's own package: it carries the firmware, the driver
 * and the installer together. Nothing here sends a reader to a third-party
 * flashing tool or asks them to assemble a kit themselves.
 *
 * Detection is conservative. Windows NT 5.x-6.3 (XP through 8.1) is legacy,
 * and so is a Windows or Linux browser that reports 32-bit. Windows 10 and 11
 * are otherwise treated as supported, because the build number that separates
 * 1507-1709 from 1809+ is not exposed to the browser. An unknown bitness is
 * never assumed to be 32-bit, so nobody is blocked on a guess.
 *
 * Supported Windows, macOS, 64-bit Linux, Android and Apple mobile visitors
 * are not told about any of this, and the guidance pages stay reachable by
 * URL for search.
 */
(function (global) {
    "use strict";
    if (global.InnioasisLegacy) return;

    var doc = global.document;
    if (!doc) return;

    var LIST = "firmware-list.html";
    var GUIDES = {
        "windows-legacy": "windows-legacy.html",
        "linux-legacy": "linux-legacy.html"
    };
    var OS_PLATFORM = { "windows-legacy": "windows", "linux-legacy": "linux" };
    var UPDATER_TEXT = /updater\s*(ce|installer|2\.)/i;
    var ICON = '<svg viewBox="0 0 24 24" width="22" height="22" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><path d="M12 7.2v7"/><path d="m8.9 11.3 3.1 3.1 3.1-3.1"/><path d="M8.4 17.1h7.2"/></svg>';

    var VERSION_NAMES = {
        "5.0": "Windows 2000",
        "5.1": "Windows XP",
        "5.2": "Windows XP x64",
        "6.0": "Windows Vista",
        "6.1": "Windows 7",
        "6.2": "Windows 8",
        "6.3": "Windows 8.1",
        "10.0": "Windows 10 or 11"
    };

    function windowsBits(ua) {
        if (/arm64|aarch64/i.test(ua)) return 64;
        if (/wow64|win64|x64|amd64|x86_64/i.test(ua)) return 64;
        if (/win32|i686|i386|i586/i.test(ua)) return 32;
        return 0;
    }

    function legacyState(system, name, bits, reason) {
        var key = system + "-legacy";
        return {
            isLegacy: true,
            system: system,
            platformKey: key,
            label: system === "windows" ? "Windows XP/7/8 (32/64-bit)" : "32-bit Linux",
            name: name,
            bits: bits,
            reason: reason
        };
    }

    function detectWindows(ua) {
        if (!/windows/i.test(ua)) return null;
        var match = /Windows NT (\d+\.\d+)/i.exec(ua);
        if (!match) return null;
        var nt = match[1];
        var bits = windowsBits(ua);
        var name = VERSION_NAMES[nt] || ("Windows NT " + nt);
        if (nt !== "10.0") return legacyState("windows", name, bits, "version");
        /* Windows 10/11: the browser cannot report the build number, so only a
           clearly 32-bit browser is treated as unable to run Updater CE. */
        if (bits === 32) return legacyState("windows", name, 32, "bits");
        return { isLegacy: false, system: "windows", name: name, bits: bits, nt: nt };
    }

    /* Updater CE's Linux builds are x86-64 and ARM64, so a 32-bit Intel
       desktop has nothing to run. A browser built for i386 reports itself as
       such in the user agent and in navigator.platform; an unknown or 64-bit
       one is left alone. */
    function detectLinux(ua, nav) {
        if (/android/i.test(ua)) return null;
        var platform = String(nav.platform || "");
        var linux = /linux|ubuntu|debian|fedora|x11/i.test(platform) || /linux/i.test(ua);
        if (!linux) return null;
        if (/i[3-6]86/i.test(platform) || /i[3-6]86/i.test(ua)) {
            return legacyState("linux", "32-bit Linux", 32, "bits");
        }
        return { isLegacy: false, system: "linux", name: "Linux", bits: windowsBits(ua) };
    }

    function detect() {
        var nav = global.navigator || {};
        var ua = String(nav.userAgent || "");
        /* Windows Phone and other mobile shells are not this audience. */
        if (/windows phone|iemobile|mobile/i.test(ua)) return null;
        return detectWindows(ua) || detectLinux(ua, nav);
    }

    var state = detect();

    function publish(current) {
        global.INNIOASIS_LEGACY = current && current.isLegacy ? {
            isLegacy: true,
            platformKey: current.platformKey,
            label: current.label,
            system: current.system,
            version: current.name,
            name: current.name,
            bits: current.bits,
            reason: current.reason
        } : null;
        if (global.InnioasisLegacy && current) {
            global.InnioasisLegacy.platformKey = current.platformKey || "";
            global.InnioasisLegacy.label = current.label || "";
        }
    }

    publish(state);

    /* Chromium can report the browser bitness on request, which settles the
       cases the user agent leaves out: a 32-bit browser on 64-bit Windows 10,
       and a 32-bit browser on a distribution whose user agent claims x86_64.
       The call is skipped for every other visitor. */
    function upgradeFromUserAgentData() {
        var uaData = global.navigator && global.navigator.userAgentData;
        if (!uaData || typeof uaData.getHighEntropyValues !== "function") return;
        var pending;
        try {
            pending = uaData.getHighEntropyValues(["bitness", "architecture"]);
        } catch (_) {
            return;
        }
        Promise.resolve(pending).then(function (data) {
            if (!data) return;
            var bits = Number(data.bitness);
            if (bits !== 32 && bits !== 64) return;
            var found = detect();
            if (!found) return;
            if (found.isLegacy) {
                /* Already legacy on the version. The browser can still report
                   the bitness the user agent leaves out, so the package is
                   named "Windows 7 32-bit" instead of just "Windows 7". */
                /* found.bits is 0 when the user agent left the bitness out;
                   the reported value fills it in rather than being ignored. */
                if (found.bits === bits) return;
                state = legacyState(found.system, found.name, bits, found.reason);
                publish(state);
                rerender();
                return;
            }
            if (bits !== 32) return;
            var system = String(data.architecture || "").toLowerCase().indexOf("arm") !== -1 ? "" : found.system;
            if (!system) return;
            /* Only a 32-bit browser on the platform itself counts: a 64-bit
               kernel with a 32-bit browser is still a 32-bit userland. */
            state = legacyState(system, found.name, 32, "bits");
            publish(state);
            init();
        }).catch(function () {});
    }

    /* The API is published on every visit so a page script or a test can ask
       the same question this module asks, and reapply the swaps after the
       catalogue paints new rows. */
    global.InnioasisLegacy = {
        platformKey: state && state.isLegacy ? state.platformKey : "",
        label: state && state.isLegacy ? state.label : "",
        detect: detect,
        refresh: refresh
    };

    /* Ask for the reported bitness on every visit: a legacy page still needs
       it to name the zip correctly, and a supported page may turn out to be a
       32-bit browser. */
    upgradeFromUserAgentData();

    if (!state || !state.isLegacy) return;

    var root = "";
    try {
        var scripts = doc.getElementsByTagName("script");
        for (var i = 0; i < scripts.length; i++) {
            var src = scripts[i].src || "";
            if (src.indexOf("site-legacy.js") === -1) continue;
            root = src.replace(/[?#].*$/, "").replace(/[^/]*$/, "");
            break;
        }
    } catch (_) {
        root = "";
    }
    if (!root) {
        var own = doc.currentScript && doc.currentScript.src;
        if (own) root = own.replace(/[?#].*$/, "").replace(/[^/]*$/, "");
    }

    function absolute(path) {
        return root ? root + path : path;
    }

    function guideFor() {
        return GUIDES[state.platformKey] || GUIDES["windows-legacy"];
    }

    function systemName() {
        var name = String(state.name || "");
        if (state.system === "linux") return /32-bit/i.test(name) ? name : name + ", 32-bit";
        var label = /^Windows/i.test(name) ? name : "Windows " + name;
        if (state.bits === 32 && !/32-bit/i.test(label)) label += ", 32-bit";
        else if (state.bits === 64 && !/64-bit/i.test(label)) label += ", 64-bit";
        return label;
    }

    function each(selector, callback) {
        Array.prototype.forEach.call(doc.querySelectorAll(selector), callback);
    }

    function inChrome(node) {
        return Boolean(node.closest && node.closest("nav, #nav-root, footer, #footer-root, #support-toolbar-slot"));
    }

    function injectStyles() {
        if (doc.getElementById("site-legacy-styles")) return;
        var style = doc.createElement("style");
        style.id = "site-legacy-styles";
        style.textContent = [
            ".lumen-legacy-download{display:grid;gap:.55rem;margin:1.1rem 0;}",
            ".lumen-unavailable-line{margin:0;color:var(--lumen-muted,#9aa3b5);font-size:.92rem;}",
            ".lumen-store-badge{display:inline-flex;align-items:center;gap:.7rem;width:max-content;max-width:100%;padding:.58rem 1.05rem .58rem .85rem;border-radius:999px;background:#101218;color:#fff;text-decoration:none;border:1px solid rgba(255,255,255,.16);box-shadow:0 6px 18px rgba(0,0,0,.22);transition:transform .15s ease,box-shadow .15s ease;}",
            ".lumen-store-badge:hover{transform:translateY(-1px);box-shadow:0 10px 24px rgba(0,0,0,.28);color:#fff;}",
            ".lumen-store-badge:focus-visible{outline:2px solid var(--lumen-accent,#6b9fff);outline-offset:3px;}",
            ".lumen-store-badge svg{flex:0 0 auto;}",
            ".lumen-store-badge-copy{display:grid;line-height:1.15;text-align:start;}",
            ".lumen-store-badge-copy small{font-size:.66rem;letter-spacing:.07em;text-transform:uppercase;color:rgba(255,255,255,.72);}",
            ".lumen-store-badge-copy strong{font-size:.98rem;font-weight:700;}",
            "@media (prefers-reduced-motion: reduce){.lumen-store-badge{transition:none;}.lumen-store-badge:hover{transform:none;}}"
        ].join("");
        (doc.head || doc.documentElement).appendChild(style);
    }

    /* The home page asks for Updater CE where it means "start here". A reader
       who cannot install the app gets the catalogue instead. */
    function swapUpdaterAvailability() {
        each('a[data-availability="updater"]', function (link) {
            if (link.getAttribute("data-legacy-browse") === "1") return;
            link.setAttribute("data-legacy-browse", "1");
            link.setAttribute("data-legacy-original-label", (link.textContent || "").trim());
            link.textContent = "Browse firmwares";
            link.setAttribute("href", absolute(LIST));
            link.removeAttribute("download");
            link.removeAttribute("target");
        });
    }

    /* Every remaining Updater CE call to action becomes the legacy zip they
       can actually use. Anchors that already download a zip are left to the
       firmware table, which resolves the legacy build itself. */
    function swapUpdaterCtas() {
        each("main a, main button", function (node) {
            if (node.getAttribute("data-legacy-browse") === "1") return;
            if (node.getAttribute("data-legacy-cta") === "1") return;
            if (inChrome(node)) return;
            var text = String(node.textContent || "").replace(/\s+/g, " ").trim();
            if (!UPDATER_TEXT.test(text)) return;
            var href = node.getAttribute("href") || "";
            if (/\.zip(\?|#|$)/i.test(href)) return;
            if (/(windows|linux)-legacy\.html/i.test(href)) return;
            node.setAttribute("data-legacy-cta", "1");
            node.setAttribute("data-legacy-original-label", text);
            node.textContent = "Get the software";
            node.setAttribute("href", absolute(guideFor()));
            node.removeAttribute("download");
            node.removeAttribute("target");
        });
    }

    /* The firmware rows carry one button per desktop platform. On this
       computer the matching button is the legacy zip, so it is renamed and
       its click is told to resolve the legacy asset. The other platforms stay
       visible, because a reader may be collecting files for another PC. */
    function relabelPortableButtons() {
        var osPlatform = OS_PLATFORM[state.platformKey];
        if (!osPlatform) return;
        each('.lumen-portable-downloads, .lumen-zip-download-row', function (group) {
            if (group.querySelector('[data-platform="' + state.platformKey + '"]')) return;
            var link = group.querySelector('a[data-platform="' + osPlatform + '"]');
            if (!link || link.getAttribute("data-legacy-relabel") === "1") return;
            link.setAttribute("data-legacy-relabel", "1");
            link.setAttribute("data-platform", state.platformKey);
            link.setAttribute("title", "Download for this computer");
            var strong = link.querySelector("strong");
            if (strong) strong.textContent = "Download";
        });
        each('a.lumen-zip-download-button[data-platform="' + osPlatform + '"]', function (link) {
            if (link.getAttribute("data-legacy-relabel") === "1") return;
            var group = link.closest(".lumen-portable-downloads, .lumen-zip-download-row");
            if (group && group.querySelector('[data-platform="' + state.platformKey + '"]')) return;
            link.setAttribute("data-legacy-relabel", "1");
            link.setAttribute("data-platform", state.platformKey);
            link.setAttribute("title", "Download for this computer");
            var strong = link.querySelector("strong");
            if (strong) strong.textContent = "Download";
        });
    }

    function cardHtml() {
        return '' +
            '<p class="lumen-kicker notranslate" translate="no">' + systemName() + '</p>' +
            '<h2>Install on this computer</h2>' +
            '<p class="lead">Pick the software you want. The download for this computer already includes everything needed to install it, so there is nothing else to find or set up first.</p>' +
            '<a class="lumen-store-badge" href="' + absolute(LIST) + '" data-legacy-store>' +
            ICON + '<span class="lumen-store-badge-copy"><small>Get</small><strong><span>Software for</span> ' +
            '<span class="notranslate" translate="no" data-i18n-skip>' + systemName() + '</span></strong></span></a>' +
            '<p class="lumen-unavailable-line"><span>Every entry in the list has it.</span> ' +
            '<a href="' + absolute(guideFor()) + '">How installation works</a></p>';
    }

    function downloadCard() {
        var card = doc.createElement("section");
        card.className = "lumen-section lumen-legacy-download";
        card.setAttribute("data-legacy-download", "1");
        card.setAttribute("data-i18n-english", "");
        card.innerHTML = cardHtml();
        return card;
    }

    /* Chromium can report the bitness after the first paint, which changes the
       package's name. Repaint the injected blocks in place so the page never
       keeps a label that no longer matches the detected computer. */
    function rerender() {
        each("[data-legacy-download]", function (card) {
            card.innerHTML = cardHtml();
        });
        relabelPortableButtons();
        swapUpdaterCtas();
    }

    /* The Updater CE download card lists an installer per desktop. On a
       computer that cannot run any of them, the whole card is replaced with
       one button that leads to the firmware list. */
    function replaceUpdaterCards() {
        each("[data-platform-detect]", function (options) {
            if (options.getAttribute("data-legacy-replaced") === "1") return;
            options.setAttribute("data-legacy-replaced", "1");
            var host = options.closest("section.lumen-updater-download, section.lumen-platforms, details#download-updater, section, details, .lumen-platform-panel");
            if (!host || !host.parentNode) return;
            host.parentNode.insertBefore(downloadCard(), host.nextSibling);
            host.hidden = true;
            host.setAttribute("aria-hidden", "true");
            /* A disclosure button the download module added before this
               swap belongs to a hidden card now, so it goes with it. */
            var stray = host.querySelector(".lumen-other-downloads");
            if (stray && stray.parentNode) stray.parentNode.removeChild(stray);
        });
    }

    function stamp() {
        doc.documentElement.setAttribute("data-os", state.platformKey);
        doc.documentElement.setAttribute("data-legacy", state.platformKey);
        if (state.system === "windows") doc.documentElement.setAttribute("data-windows-legacy", "true");
        else doc.documentElement.setAttribute("data-linux-legacy", "true");
        if (doc.body) doc.body.classList.add(state.platformKey);
    }

    function refresh() {
        replaceUpdaterCards();
        swapUpdaterAvailability();
        swapUpdaterCtas();
        relabelPortableButtons();
    }

    function observe() {
        if (!global.MutationObserver || !doc.body) return;
        var pending = null;
        var observer = new MutationObserver(function () {
            if (pending) return;
            pending = global.setTimeout(function () {
                pending = null;
                refresh();
            }, 60);
        });
        observer.observe(doc.body, { childList: true, subtree: true });
        /* The firmware catalogue paints its rows after this module starts, so
           two timed passes catch late calls to action without a busy loop. */
        global.setTimeout(refresh, 300);
        global.setTimeout(refresh, 1200);
    }

    function init() {
        injectStyles();
        stamp();
        replaceUpdaterCards();
        swapUpdaterAvailability();
        swapUpdaterCtas();
        relabelPortableButtons();
        observe();
    }

    if (doc.readyState === "loading") {
        doc.addEventListener("DOMContentLoaded", init);
    } else {
        init();
    }
})(typeof window !== "undefined" ? window : globalThis);
