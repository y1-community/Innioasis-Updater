/* Windows XP / Vista / 7 / 8 / 8.1 and 32-bit Windows.
 *
 * Updater CE is a 64-bit application and needs Windows 10 1809 or newer, so a
 * reader on an older or 32-bit Windows PC cannot install it at all. Those
 * readers can still flash their player: every firmware package has a
 * Windows XP/7/8 (32/64-bit) portable zip that carries SP Flash Tool beside
 * the rom, which works back to Windows XP.
 *
 * This module notices that visit and changes what the page offers:
 *
 *   - "Get Updater CE" becomes "Browse firmwares" on the home page, because an
 *     install link they cannot run is worse than no link;
 *   - every other Updater CE call to action becomes "Get Zip" and resolves
 *     the same release's Windows XP/7/8 portable package, keeping the button
 *     markup and styling; the programmatic firmware list is the fallback;
 *   - guide links carry platform=windows-legacy, and the shared guide page
 *     swaps its Updater CE sections for the portable package steps, so the
 *     visit reads the same guide as everyone else instead of a warning panel.
 *
 * Detection is deliberately conservative. Windows NT 5.x-6.3 (XP through 8.1)
 * is legacy; Windows 10 and 11 are always treated as supported, because the
 * build number that distinguishes 1507-1709 from 1809+ is not exposed to the
 * browser. A 32-bit Windows 10/11 browser is legacy, but an unknown bitness is
 * never assumed to be 32-bit, so a reader is never blocked on a guess.
 *
 * Nobody else is told about any of this: the page is unchanged for supported
 * Windows, macOS, Linux, Android and Apple mobile visitors, and the guidance
 * page stays reachable by URL for search.
 */
(function (global) {
    "use strict";
    if (global.InnioasisLegacy) return;

    var doc = global.document;
    if (!doc) return;

    var PLATFORM_KEY = "windows-legacy";
    var BIG_LABEL = "Windows XP/7/8 32/64-bit";
    var LIST = "firmware-list.html";
    var ZIP_LABEL = "Get Zip";
    /* Declared above the early return below: refresh() is callable on any
       visit through the published API, and a var initialised further down
       would be undefined there. */
    var UPDATER_TEXT = /updater\s*(ce|installer|2\.)/i;

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

    function detectBits(ua) {
        if (/arm64|aarch64/i.test(ua)) return 64;
        if (/wow64|win64|x64|amd64|x86_64/i.test(ua)) return 64;
        if (/win32|i686|i386/i.test(ua)) return 32;
        return 0;
    }

    function detect() {
        var nav = global.navigator || {};
        var ua = String(nav.userAgent || "");
        /* Windows Phone and other mobile shells are not this audience. */
        if (/windows phone|iemobile|mobile/i.test(ua)) return null;
        if (!/windows/i.test(ua)) return null;
        var match = /Windows NT (\d+\.\d+)/i.exec(ua);
        if (!match) return null;
        var nt = match[1];
        var bits = detectBits(ua);
        var name = VERSION_NAMES[nt] || ("Windows NT " + nt);

        if (nt !== "10.0") {
            return { isLegacy: true, nt: nt, name: name, bits: bits, reason: "version" };
        }
        /* Windows 10/11: the browser cannot report the build number, so only a
           clearly 32-bit browser is treated as unable to run Updater CE. */
        if (bits === 32) {
            return { isLegacy: true, nt: nt, name: name, bits: 32, reason: "bits" };
        }
        return { isLegacy: false, nt: nt, name: name, bits: bits, reason: "" };
    }

    var state = detect();

    function publish(current) {
        if (current && current.isLegacy) {
            global.INNIOASIS_LEGACY = {
                isLegacy: true,
                platformKey: PLATFORM_KEY,
                label: BIG_LABEL,
                version: current.name,
                nt: current.nt,
                bits: current.bits,
                reason: current.reason
            };
            return;
        }
        /* An explicit ?platform=windows-legacy link uses the portable route
           on any computer. Publish the same marker so the table buttons, the
           guide and every lookup make one shared choice. */
        global.INNIOASIS_LEGACY = requestedPlatform() === PLATFORM_KEY ? {
            isLegacy: true,
            platformKey: PLATFORM_KEY,
            label: BIG_LABEL,
            version: "requested",
            nt: "",
            bits: 0,
            reason: "query"
        } : null;
    }

    publish(state);

    /* Windows 10 and 11 are never classified from the user agent alone: the
       build number that decides 1809+ is not exposed to the browser, so the
       safe default there is "supported". Chromium can still report the browser
       bitness on request, and a 32-bit browser cannot run the 64-bit app. The
       call is skipped for every other visitor. */
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
            if (!data || String(data.bitness) !== "32") return;
            var found = detect();
            if (!found || String(found.nt) !== "10.0") return;
            state = { isLegacy: true, nt: found.nt, name: found.name, bits: 32, reason: "bits" };
            publish(state);
            init();
        }).catch(function () {});
    }

    /* The API is published on every visit so a page script or a test can ask
       the same question this module asks, and reapply the swaps after the
       catalogue paints new rows. */
    global.InnioasisLegacy = {
        platformKey: PLATFORM_KEY,
        label: BIG_LABEL,
        detect: detect,
        refresh: refresh
    };

    /* A shared link can name the portable route directly, so a supported
       machine opening ?platform=windows-legacy still reads that guide. */
    function requestedPlatform() {
        try {
            return String(new URLSearchParams(global.location.search).get("platform") || "").trim().toLowerCase();
        } catch (_) {
            return "";
        }
    }

    if (!state || !state.isLegacy) {
        if (requestedPlatform() === PLATFORM_KEY) {
            /* root and the helper declarations finish below; run after this
               script has finished executing. */
            global.setTimeout(init, 0);
        } else {
            upgradeFromUserAgentData();
        }
        return;
    }

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

    function each(selector, callback) {
        Array.prototype.forEach.call(doc.querySelectorAll(selector), callback);
    }

    function inChrome(node) {
        return Boolean(node.closest && node.closest("nav, #nav-root, footer, #footer-root, #support-toolbar-slot"));
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

    /* Every remaining Updater CE call to action becomes the portable package
       they can actually run. Anchors that already download a zip are left to
       the firmware table, which resolves the legacy build itself. */
    function swapUpdaterCtas() {
        each("main a, main button", function (node) {
            if (node.getAttribute("data-legacy-browse") === "1") return;
            if (node.getAttribute("data-legacy-cta") === "1") return;
            if (node.classList && node.classList.contains("lumen-updater-button")) return;
            if (inChrome(node)) return;
            var text = String(node.textContent || "").replace(/\s+/g, " ").trim();
            if (!UPDATER_TEXT.test(text)) return;
            var href = node.getAttribute("href") || "";
            if (/\.zip(\?|#|$)/i.test(href)) return;
            if (/windows-legacy\.html/i.test(href)) return;
            node.setAttribute("data-legacy-cta", "1");
            node.setAttribute("data-legacy-original-label", text);
            node.textContent = ZIP_LABEL;
            node.setAttribute("href", absolute(LIST));
            node.removeAttribute("download");
            node.removeAttribute("target");
        });
    }

    /* Updater CE cannot run here, so its header link is not a useful first
       stop. Put the firmware catalogue in that slot instead, without changing
       the rest of the navigation or the labels the i18n pass already built. */
    function adjustHeaderCta() {
        var cta = doc.getElementById("lumen-nav-install-cta");
        if (cta) {
            cta.hidden = true;
            cta.style.display = "none";
            cta.setAttribute("aria-hidden", "true");
            cta.setAttribute("tabindex", "-1");
        }
        each('#navLinks a[href*="view=software"]', function (link) {
            if (link.getAttribute("data-legacy-primary") === "1") return;
            link.setAttribute("data-legacy-primary", "1");
            link.classList.add("lumen-nav-install-cta", "lumen-nav-install-cta--legacy");
            link.style.color = "var(--lumen-accent)";
            link.style.background = "var(--lumen-accent-wash)";
        });
    }

    /* The table's Updater column is the same promise as its buttons. Keep the
       original label so a supported visitor never sees the swap. */
    function swapTableHeadings() {
        each("th", function (heading) {
            if (heading.getAttribute("data-legacy-heading") === "1") return;
            var text = String(heading.textContent || "").replace(/\s+/g, " ").trim();
            if (!/Updater CE/i.test(text)) return;
            heading.setAttribute("data-legacy-heading", "1");
            heading.setAttribute("data-legacy-original-label", text);
            heading.textContent = ZIP_LABEL;
        });
    }

    /* The firmware table renders after this module starts. The button keeps
       its icon and layout; only the label changes. The actual package is the
       same release's windows-legacy mirror asset, resolved from the metadata
       lumen-site.js puts on the anchor. */
    function relabelUpdaterButtons() {
        each("a.lumen-updater-button", function (link) {
            if (link.getAttribute("data-legacy-zip") === "1") return;
            link.setAttribute("data-legacy-zip", "1");
            link.setAttribute("data-legacy-original-label", String(link.textContent || "").replace(/\s+/g, " ").trim());
            var strong = link.querySelector("strong");
            var small = link.querySelector("small");
            if (strong) strong.textContent = ZIP_LABEL;
            else link.textContent = ZIP_LABEL;
            if (small) small.textContent = "portable package";
            link.setAttribute("href", absolute(LIST));
            link.removeAttribute("target");
            resolveLegacyZip(link);
        });
    }

    function resolveLegacyZip(link) {
        if (!link || link.getAttribute("data-legacy-zip-resolved") === "1") return;
        var source = link.getAttribute("data-zip-url") || "";
        var resolver = global.InnioasisPortable && global.InnioasisPortable.resolve;
        if (!source || typeof resolver !== "function") return;
        try {
            Promise.resolve(resolver(
                source,
                link.getAttribute("data-portable-zips") || "",
                link.getAttribute("data-release-tag") || "",
                link.getAttribute("data-zip-name") || ""
            )).then(function (target) {
                if (!target || !target.url) return;
                link.setAttribute("href", target.url);
                link.setAttribute("download", "");
                link.setAttribute("data-legacy-zip-resolved", "1");
                link.setAttribute("title", "Download the " + BIG_LABEL + " portable zip");
            }).catch(function () {});
        } catch (_) {}
    }

    /* The firmware rows carry one button per desktop OS. On this computer the
       Windows button is the flash-tool package, so it is relabelled that way
       and its click is told to resolve the legacy asset. The macOS and Linux
       builds stay visible: a reader may be collecting files for another PC. */
    function relabelPortableButtons() {
        each('.lumen-portable-downloads a[data-platform="windows"], a.lumen-zip-download-button[data-platform="windows"]', function (link) {
            if (link.getAttribute("data-legacy-relabel") === "1") return;
            link.setAttribute("data-legacy-relabel", "1");
            link.setAttribute("data-platform", PLATFORM_KEY);
            link.setAttribute("title", "SP Flash Tool package for " + BIG_LABEL);
            var strong = link.querySelector("strong");
            if (strong) strong.textContent = BIG_LABEL;
        });
    }

    /* The shared guide page accepts URL parameters. Marking guide links keeps
       a legacy visit on the same page as everyone else; the guide itself shows
       the portable steps when that parameter is present. */
    function rewriteGuideLinks() {
        each("a[href]", function (link) {
            if (link.getAttribute("data-legacy-guide-link") === "1") return;
            var href = link.getAttribute("href") || "";
            if (!href || /^(#|mailto:|tel:|javascript:)/i.test(href)) return;
            var url;
            try {
                url = new URL(href, global.location.href);
            } catch (_) {
                return;
            }
            if (url.origin !== global.location.origin) return;
            if (!/(^|\/)(?:guide|firmware-guide)\.html$/i.test(url.pathname)) return;
            url.searchParams.set("platform", PLATFORM_KEY);
            link.setAttribute("href", url.pathname + url.search + url.hash);
            link.setAttribute("data-legacy-guide-link", "1");
        });
    }

    function notifyPortableReady() {
        try {
            global.dispatchEvent(new CustomEvent("innioasis-portable-ready"));
        } catch (_) {}
    }

    function stamp() {
        doc.documentElement.setAttribute("data-windows-legacy", "true");
        doc.documentElement.setAttribute("data-os", "windows-legacy");
        if (doc.body) doc.body.classList.add("windows-legacy");
    }

    function refresh() {
        swapUpdaterAvailability();
        swapUpdaterCtas();
        adjustHeaderCta();
        swapTableHeadings();
        relabelUpdaterButtons();
        relabelPortableButtons();
        rewriteGuideLinks();
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
           two timed passes catch late call to actions without a busy loop. */
        global.setTimeout(refresh, 300);
        global.setTimeout(refresh, 1200);
    }

    function init() {
        stamp();
        swapUpdaterAvailability();
        swapUpdaterCtas();
        adjustHeaderCta();
        swapTableHeadings();
        relabelUpdaterButtons();
        relabelPortableButtons();
        rewriteGuideLinks();
        notifyPortableReady();
        observe();
    }

    if (doc.readyState === "loading") {
        doc.addEventListener("DOMContentLoaded", init);
    } else {
        init();
    }
})(typeof window !== "undefined" ? window : globalThis);
