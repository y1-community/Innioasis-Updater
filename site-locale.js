/*!
 * Site i18n — locale copies and region editions
 * ---------------------------------------------------------------
 * The site ships in English. Every other language is a pre-translated
 * catalog in i18n/catalogs/<locale>.json, produced by
 * scripts/i18n/translate.py. This file picks the visitor's locale, loads
 * that catalog and swaps the page's text, attributes, title and meta
 * description in place. Nothing is fetched until the locale is known to
 * differ from English, so an English visit costs one small request for
 * the picker list.
 *
 * A "copy" of the site lives at /<locale>/<page>.html. Those copies are
 * pre-rendered by scripts/i18n/prerender.py, so search engines see the
 * translated text in the HTML rather than after script execution. On a
 * copy, this runtime detects the path prefix, keeps the same page when
 * the language changes, and leaves the text alone because it is already
 * translated.
 *
 * Region editions are separate from language: a region decides what the
 * page may offer. Elements marked data-availability="updater" only render
 * where the updater app is usable, data-region-only="cn" only in the China
 * edition, and region copy overrides replace a source string after
 * translation. The rules live in i18n/regions.json.
 *
 * RULE: new user-facing copy belongs in the HTML (or a catalog), not in a
 * JavaScript string with no translation entry. The shell strings harvested
 * by scripts/i18n/harvest_ui_strings.py cover the ones that must stay in JS.
 * ---------------------------------------------------------------
 */
(function (global) {
    "use strict";

    var DEFAULT_LOCALE = "en";
    var RUNTIME_VERSION = "20261108b";
    var STORAGE_LOCALE = "innioasis-locale";
    var STORAGE_REGION = "innioasis-region";
    var STORAGE_COUNTRY = "innioasis-country";

    var SKIP_TAGS = {
        SCRIPT: 1, STYLE: 1, PRE: 1, CODE: 1, KBD: 1, SAMP: 1, TEXTAREA: 1
    };

    var ATTRIBUTES = ["title", "alt", "placeholder", "aria-label", "aria-description"];
    var META_NAMES = {
        "description": 1,
        "keywords": 1,
        "og:title": 1,
        "og:description": 1,
        "og:site_name": 1,
        "twitter:title": 1,
        "twitter:description": 1
    };

    var state = {
        locale: DEFAULT_LOCALE,
        dir: "ltr",
        strings: null,
        locales: [],
        regions: null,
        region: "intl",
        availability: {},
        regionCopy: {},
        applied: 0,
        panel: null,
        copies: []
    };

    var observer = null;
    var applying = false;
    var baseUrl = "/";
    /* Text this runtime already replaced from a catalog. Without this, the API
       fallback would see German text, treat it as English source and translate
       it a second time. */
    var catalogApplied = typeof WeakSet === "function" ? new WeakSet() : null;

    /* ---------------------------------------------------------------- */
    /* Utilities                                                        */
    /* ---------------------------------------------------------------- */

    function scriptBase() {
        var script = document.currentScript;
        if (!script) {
            var scripts = document.querySelectorAll('script[src*="site-locale.js"]');
            script = scripts.length ? scripts[scripts.length - 1] : null;
        }
        if (!script || !script.src) return "/";
        return script.src.replace(/[^/]*$/, "");
    }

    function readStorage(key) {
        try { return global.localStorage.getItem(key); } catch (_) { return null; }
    }

    function writeStorage(key, value) {
        try { global.localStorage.setItem(key, value); } catch (_) {}
    }

    function normalise(text) {
        return String(text == null ? "" : text).replace(/\s+/g, " ").trim();
    }

    function fetchJson(path, timeoutMs) {
        var controller = typeof AbortController === "function" ? new AbortController() : null;
        var timer = null;
        if (controller && timeoutMs) {
            timer = setTimeout(function () { controller.abort(); }, timeoutMs);
        }
        return fetch(baseUrl + path, {
            cache: "no-cache",
            signal: controller ? controller.signal : undefined
        }).then(function (response) {
            if (timer) clearTimeout(timer);
            if (!response.ok) throw new Error("HTTP " + response.status + " for " + path);
            return response.json();
        }).catch(function (error) {
            if (timer) clearTimeout(timer);
            throw error;
        });
    }

    function normalizeTag(value) {
        return String(value || "").toLowerCase().replace(/_/g, "-");
    }

    /* ---------------------------------------------------------------- */
    /* Locale resolution                                                */
    /* ---------------------------------------------------------------- */

    function localeIndex() {
        var map = {};
        state.locales.forEach(function (entry) { map[entry.code.toLowerCase()] = entry; });
        return map;
    }

    function pathLocale() {
        var segments = global.location.pathname.split("/").filter(Boolean);
        if (!segments.length) return "";
        var candidate = normalizeTag(segments[0]);
        var map = localeIndex();
        return map[candidate] ? map[candidate].code : "";
    }

    function param(name) {
        try {
            return new URLSearchParams(global.location.search).get(name) || "";
        } catch (_) {
            return "";
        }
    }

    function browserLocales() {
        var list = (navigator.languages && navigator.languages.length)
            ? navigator.languages
            : [navigator.language || ""];
        return list.map(normalizeTag).filter(Boolean);
    }

    function matchBrowserLocale(map) {
        var candidates = browserLocales();
        for (var i = 0; i < candidates.length; i += 1) {
            var tag = candidates[i];
            if (map[tag]) return map[tag].code;
            var language = tag.split("-")[0];
            if (language === "zh") {
                /* Simplified unless the region says otherwise. */
                if (/-(tw|hk|mo)$/.test(tag)) {
                    if (map["zh-tw"]) return "zh-TW";
                    if (map["zh-hant"]) return map["zh-hant"].code;
                }
                if (map["zh-cn"]) return "zh-CN";
                continue;
            }
            if (map[language]) return map[language].code;
            /* en-GB and friends exist as variants; fall back to their base. */
            for (var code in map) {
                if (!Object.prototype.hasOwnProperty.call(map, code)) continue;
                if (map[code].base === language) return map[code].code;
            }
        }
        return "";
    }

    function regionDefaultLocale() {
        var region = state.regions && state.regions.regions[state.region];
        if (!region) return "";
        var country = readStorage(STORAGE_COUNTRY) || "";
        var mapped = country && region.autoLocales ? region.autoLocales[country] : "";
        if (mapped) return mapped;
        return (region.locales && region.locales[0]) || "";
    }

    function resolveLocale() {
        var map = localeIndex();
        var requested = normalizeTag(param("lang"));
        if (requested) {
            if (map[requested]) return map[requested].code;
            /* The picker list can be missing on a partial deploy; an explicit
               ?lang= is still the visitor's instruction, so honour it and let
               the catalog fetch decide whether the language exists. */
            if (/^[a-z]{2,3}(-[a-z0-9]{2,4})?$/.test(requested)) return requested;
        }
        var fromPath = pathLocale();
        if (fromPath) return fromPath;
        var stored = normalizeTag(readStorage(STORAGE_LOCALE));
        if (stored && map[stored]) return stored;
        /* The browser's own languages are a stronger signal than a country's
           default. A German visitor on an English-region machine must get
           German, not English with a German country code. */
        var fromBrowser = matchBrowserLocale(map);
        if (fromBrowser) return fromBrowser;
        var fromRegion = normalizeTag(regionDefaultLocale());
        if (fromRegion && map[fromRegion]) return fromRegion;
        return DEFAULT_LOCALE;
    }

    /* ---------------------------------------------------------------- */
    /* Region resolution                                                */
    /* ---------------------------------------------------------------- */

    function resolveRegion() {
        var regions = state.regions && state.regions.regions ? state.regions.regions : {};
        var requested = normalizeTag(param("region"));
        if (requested && regions[requested]) return requested;
        var stored = normalizeTag(readStorage(STORAGE_REGION));
        if (stored && regions[stored]) return stored;
        var country = readStorage(STORAGE_COUNTRY);
        var mapped = country && state.regions && state.regions.countryRegions
            ? state.regions.countryRegions[country]
            : "";
        if (mapped && regions[mapped]) return mapped;
        return (state.regions && state.regions.default) || "intl";
    }

    /* Cloudflare's /cdn-cgi/trace is the only reliable, same-origin way to
       learn the visitor's country without a third party. It exists only
       behind Cloudflare, and a failed lookup changes nothing. */
    function confirmCountry() {
        if (readStorage(STORAGE_COUNTRY)) return Promise.resolve();
        if (param("region")) return Promise.resolve();
        return fetch(baseUrl + "cdn-cgi/trace", { cache: "no-store" })
            .then(function (response) { return response.ok ? response.text() : ""; })
            .then(function (text) {
                var match = /(?:^|\n)loc=([A-Z]{2})(?:\n|$)/.exec(text || "");
                if (!match) return;
                writeStorage(STORAGE_COUNTRY, match[1]);
            })
            .catch(function () {});
    }

    /* ---------------------------------------------------------------- */
    /* Translation                                                      */
    /* ---------------------------------------------------------------- */

    function regionValue(source) {
        var entry = state.regionCopy[source];
        if (!entry) return "";
        return entry[state.locale] || entry[state.locale.split("-")[0]] || entry.en || "";
    }

    function translateValue(value) {
        var text = String(value == null ? "" : value);
        var parts = /^(\s*)([\s\S]*?)(\s*)$/.exec(text);
        if (!parts) return value;
        var core = normalise(parts[2]);
        if (!core) return value;

        var regional = regionValue(core);
        if (regional) return parts[1] + regional + parts[3];

        if (!state.strings) return value;
        var translated = state.strings[core];
        if (translated === undefined) return value;
        return parts[1] + translated + parts[3];
    }

    function shouldSkip(element) {
        if (!element) return false;
        if (SKIP_TAGS[element.tagName]) return true;
        if (element.hasAttribute && element.hasAttribute("data-i18n-skip")) return true;
        if (element.getAttribute && element.getAttribute("translate") === "no") return true;
        return false;
    }

    function translateAttributes(element) {
        if (!element.getAttribute) return;
        for (var i = 0; i < ATTRIBUTES.length; i += 1) {
            var name = ATTRIBUTES[i];
            if (!element.hasAttribute(name)) continue;
            var value = element.getAttribute(name);
            var next = translateValue(value);
            if (next !== value) element.setAttribute(name, next);
        }
    }

    function translateTree(root) {
        if (!root) return;
        if (root.nodeType === 3) {
            var next = translateValue(root.nodeValue);
            if (next !== root.nodeValue) {
                root.nodeValue = next;
                state.applied += 1;
                if (catalogApplied) catalogApplied.add(root);
            }
            return;
        }
        if (root.nodeType !== 1 && root.nodeType !== 9 && root.nodeType !== 11) return;
        if (root.nodeType === 1 && shouldSkip(root)) return;

        if (root.nodeType === 1) translateAttributes(root);

        for (var node = root.firstChild; node; node = node.nextSibling) {
            if (node.nodeType === 3) {
                var value = translateValue(node.nodeValue);
                if (value !== node.nodeValue) {
                    node.nodeValue = value;
                    state.applied += 1;
                    if (catalogApplied) catalogApplied.add(node);
                }
            } else if (node.nodeType === 1) {
                translateTree(node);
            }
        }
    }

    function translateHead() {
        if (!state.strings && !Object.keys(state.regionCopy).length) return;
        var title = document.title;
        var nextTitle = translateValue(title);
        if (nextTitle !== title) document.title = nextTitle;

        var metas = document.querySelectorAll(
            'meta[name="description"], meta[name="keywords"], meta[property^="og:"], meta[name^="twitter:"]'
        );
        Array.prototype.forEach.call(metas, function (meta) {
            var key = (meta.getAttribute("name") || meta.getAttribute("property") || "").toLowerCase();
            if (!META_NAMES[key]) return;
            var content = meta.getAttribute("content") || "";
            var next = translateValue(content);
            if (next !== content) meta.setAttribute("content", next);
        });
    }

    /* ---------------------------------------------------------------- */
    /* Dynamic content                                                  */
    /* ---------------------------------------------------------------- */
    /* Release notes, READMEs, notices and parsed markdown are fetched and
       rendered after the catalog was built, so no catalog can contain them.
       This translates those containers on demand through the same keyless
       public endpoint the Updater app uses, caches the result per language
       (so a second page view costs nothing), and leaves the English text in
       place if the request fails. Only explicitly marked content areas are
       sent, never the whole document. */
    var DYNAMIC_CONTAINERS = [
        "body",
        "html",
        "[data-i18n-dynamic]",
        "#release-body",
        "#doc-body",
        "#notices-list",
        "#lumen-notices-tray-body",
        ".lumen-notice-body",
        "[data-doc-view]",
        "main",
        "article.lumen-doc-body",
        ".lumen-notice-view"
    ].join(", ");
    var DYNAMIC_CACHE_KEY = "innioasis-dynamic-translations";
    var DYNAMIC_MAX_REQUESTS = 800;
    var DYNAMIC_CONCURRENCY = 2;
    var dynamicCache = null;
    var dynamicSeen = typeof WeakSet === "function" ? new WeakSet() : null;
    var dynamicAttrSeen = typeof WeakSet === "function" ? new WeakSet() : new Map();
    var dynamicQueue = [];
    var dynamicPending = {};
    var dynamicInFlight = 0;
    var dynamicRequests = 0;

    function loadDynamicCache() {
        if (dynamicCache) return dynamicCache;
        try {
            dynamicCache = JSON.parse(global.localStorage.getItem(DYNAMIC_CACHE_KEY) || "{}") || {};
        } catch (_) {
            dynamicCache = {};
        }
        return dynamicCache;
    }

    function persistDynamicCache() {
        var cache = loadDynamicCache();
        var keys = Object.keys(cache);
        if (keys.length > 800) {
            keys.slice(0, keys.length - 800).forEach(function (key) { delete cache[key]; });
        }
        try { global.localStorage.setItem(DYNAMIC_CACHE_KEY, JSON.stringify(cache)); } catch (_) {}
    }

    function dynamicEntry() {
        var map = localeIndex();
        return map[normalizeTag(state.locale)] || {};
    }

    function isEnglishLocale(code) {
        if (!code) return true;
        var tag = String(code).toLowerCase().replace(/_/g, "-").trim();
        return tag === "en" || tag.indexOf("en-") === 0;
    }

    function dynamicEnabled() {
        if (isEnglishLocale(state.locale)) return false;
        var entry = dynamicEntry();
        var base = entry.base || entry.code || normalizeTag(state.locale);
        if (isEnglishLocale(base)) return false;
        return String(base).toLowerCase() !== DEFAULT_LOCALE;
    }

    function dynamicTarget() {
        var entry = dynamicEntry();
        return entry.google || state.locale;
    }

    function dynamicKey(text) {
        return state.locale + "|" + text;
    }

    /* Brand and product names stay as written: a service that translates
       "Discord" returns the German word for strife, and "Y1" becomes "J1".
       Sentences that mention a brand are still translated; the name is
       masked out and restored afterwards. */
    var DYNAMIC_BRANDS = [
        "Innioasis Updater CE", "Innioasis Updater", "Updater Community Edition", "Updater CE",
        "Innioasis Universal Flash Tool", "Universal Flash Tool", "SP Flash Tool", "SP Flash",
        "MTKClient", "MediaTek", "Innioasis Y1", "Innioasis Y2", "Innioasis",
        "Timmkoo", "Mechen H11", "Mechen H1", "Mechen",
        "Rockbox-Y1", "Rockbox-Y2", "Rockbox",
        "Better-Y", "Y2Linux", "Y2Player", "Y2Reborn", "Reborn",
        "Inniclassic", "JJ Launcher", "Koensayr", "Rondo", "Solar", "Lithium",
        "Type A", "Type B", "Type-A", "Type-B",
        "Y1", "Y2", "G1", "G3", "G5", "PR1", "R1", "D1", "Q3", "Q5", "A5", "SR1", "Q3E", "Q8",
        "rom.zip", "rom_y2.zip", "rom_type_b.zip", "rom_g1.zip", "rom_g3.zip", "rom_g5.zip",
        "rom_pr1.zip", "rom_q3.zip", "rom_q5.zip", "rom_r1.zip", "rom_sr1.zip", "system.zip",
        "scatter.txt", "MicroSD", "microSD", "SD Card", "SD card", "APK", "ROM", "USB",
        "Buy Me a Coffee", "Honeygain", "Cloudflare", "Google Analytics", "Google Tag Manager",
        "GitHub", "Discord", "Ko-fi", "PayPal", "Patreon", "Revolut", "Boosty", "YouTube", "Reddit", "TikTok",
        "Bitcoin (BTC)", "Bitcoin", "BTC", "Ethereum (ETH)", "Ethereum", "ETH", "Shiba Inu (SHIB)", "Shiba Inu", "SHIB"
    ];
    var dynamicBrandPattern = new RegExp(
        "(^|[^A-Za-z0-9])(" + DYNAMIC_BRANDS.slice().sort(function (a, b) {
            return b.length - a.length;
        }).map(function (term) {
            return term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
        }).join("|") + ")(?![A-Za-z0-9])",
        "g"
    );

    function maskBrands(text) {
        var found = [];
        var masked = String(text).replace(dynamicBrandPattern, function (match, prefix, brand) {
            found.push(brand);
            return prefix + "[[" + (found.length - 1) + "]]";
        });
        return { text: masked, found: found };
    }

    function restoreBrands(text, found) {
        var restored = String(text).replace(/\[\[\s*(\d+)\s*\]\]/g, function (match, index) {
            var value = found[Number(index)];
            return value === undefined ? match : value;
        });
        for (var i = 0; i < found.length; i += 1) {
            if (restored.indexOf(found[i]) === -1) return "";
        }
        return restored;
    }

    function isBrandOnly(text) {
        var value = String(text).trim();
        /* Release tags, versions, package names, repos and model codes are
           identifiers, not prose: 0.5, stable-v0.5, rom.zip, owner/repo, Y1. */
        if (/^(?:v?\d+(?:\.\d+)*(?:[-._][A-Za-z0-9]+)*|[a-z0-9]+-v?\d+(?:\.\d+)*(?:[-._][A-Za-z0-9]+)*|[A-Z0-9]+(?:[-_.][A-Z0-9]+)+|[\w.-]+\.(?:zip|apk|img|bin|tar|gz|md|txt|json|rar|7z|iso)|[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+|[A-Z]{1,3}\d+[A-Za-z]?|Type[- ][AB])$/.test(value)) return true;
        var stripped = value.replace(dynamicBrandPattern, "$1");
        return !/[A-Za-z\u00C0-\u024F\u0400-\u04FF]/.test(stripped);
    }

    function requestDynamic(text) {
        var masked = maskBrands(text);
        var hidden = masked.text;
        var target = dynamicTarget();
        var gtxUrl = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=" +
            encodeURIComponent(target) + "&dt=t&q=" + encodeURIComponent(hidden);
        var clients5Url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl=" +
            encodeURIComponent(target) + "&q=" + encodeURIComponent(hidden);
        var mymemoryUrl = "https://api.mymemory.translated.net/get?q=" +
            encodeURIComponent(hidden) + "&langpair=en|" + encodeURIComponent(target);

        function tryGTX() {
            return fetch(gtxUrl, { method: "GET", mode: "cors" })
                .then(function (r) { if (!r.ok) throw new Error(); return r.json(); })
                .then(function (data) {
                    var segments = (data && data[0]) || [];
                    var translated = "";
                    for (var i = 0; i < segments.length; i += 1) {
                        if (segments[i] && segments[i][0]) translated += segments[i][0];
                    }
                    if (!translated) throw new Error();
                    return translated;
                });
        }

        function tryClients5() {
            return fetch(clients5Url, { method: "GET", mode: "cors" })
                .then(function (r) { if (!r.ok) throw new Error(); return r.json(); })
                .then(function (data) {
                    if (Array.isArray(data) && data.length) {
                        var first = data[0];
                        if (Array.isArray(first) && first.length) return String(first[0]).trim();
                        if (typeof first === "string") return first.trim();
                    }
                    throw new Error();
                });
        }

        function tryMyMemory() {
            return fetch(mymemoryUrl, { method: "GET", mode: "cors" })
                .then(function (r) { if (!r.ok) throw new Error(); return r.json(); })
                .then(function (data) {
                    var match = data && data.responseData && data.responseData.translatedText;
                    if (match && match.trim()) return match.trim();
                    throw new Error();
                });
        }

        return tryGTX()
            .catch(tryClients5)
            .catch(tryMyMemory)
            .then(function (translated) {
                if (!translated || !translated.trim()) return "";
                var value = restoreBrands(translated.trim(), masked.found);
                if (!value) return "";
                loadDynamicCache()[dynamicKey(text)] = value;
                persistDynamicCache();
                return value;
            })
            .catch(function () {
                return "";
            });
    }

    function drainDynamic() {
        while (dynamicInFlight < DYNAMIC_CONCURRENCY && dynamicQueue.length) {
            var item = dynamicQueue.shift();
            dynamicInFlight += 1;
            dynamicRequests += 1;
            requestDynamic(item.text).then(function (key) {
                return function (translated) {
                    dynamicInFlight -= 1;
                    var waiters = dynamicPending[key] || [];
                    delete dynamicPending[key];
                    /* Null on failure so the badge is removed even when no
                       translation arrived. */
                    waiters.forEach(function (apply) { apply(translated || null); });
                    drainDynamic();
                };
            }(item.key));
        }
    }

    /* ---------------------------------------------------------------- */
    /* Pending-translation indicator                                     */
    /* ---------------------------------------------------------------- */
    /* Text that is still being fetched is original-language copy, so the
       reader gets a small globe and a spinner beside it until the translated
       text replaces it. One badge per element, counted, and removed on both
       success and failure (a failed request leaves the English text, not a
       spinner that never stops). */
    var pendingByElement = typeof WeakMap === "function" ? new WeakMap() : null;
    var BADGE_HTML = '<svg class="site-i18n-globe" viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.7 5.7 3.7 9s-1.2 6.4-3.7 9c-2.5-2.6-3.7-5.7-3.7-9S9.5 5.6 12 3z"/></svg><span class="site-i18n-spinner" aria-hidden="true"></span>';

    /* Most pages do not link site-locale.css, so the badge carries its own
       styles. One <style> element, injected the first time it is needed. */
    function ensureBadgeStyles() {
        if (document.getElementById("site-i18n-badge-styles")) return;
        var style = document.createElement("style");
        style.id = "site-i18n-badge-styles";
        style.textContent = [
            ".site-i18n-badge{display:inline-flex;align-items:center;gap:4px;",
            "margin-inline-start:6px;vertical-align:middle;color:currentColor;opacity:.68;",
            "pointer-events:none;user-select:none;font-size:.85em;line-height:1;}",
            "html[lang^=\"en\"] .site-i18n-badge,html:not([lang]) .site-i18n-badge,[lang^=\"en\"] .site-i18n-badge,[data-locale^=\"en\"] .site-i18n-badge{display:none!important;}",
            "button .site-i18n-badge,[role=\"button\"] .site-i18n-badge,a .site-i18n-badge,.btn .site-i18n-badge,.button .site-i18n-badge,nav .site-i18n-badge,.nav .site-i18n-badge,.y1-dock .site-i18n-badge,table .site-i18n-badge,th .site-i18n-badge,td .site-i18n-badge,h1 .site-i18n-badge,h2 .site-i18n-badge,h3 .site-i18n-badge,h4 .site-i18n-badge,h5 .site-i18n-badge,h6 .site-i18n-badge,.kicker .site-i18n-badge,.lumen-kicker .site-i18n-badge,.chip .site-i18n-badge,.badge .site-i18n-badge{display:none!important;}",
            ".site-i18n-globe{flex:none;width:13px;height:13px;}",
            ".site-i18n-spinner{flex:none;width:10px;height:10px;border-radius:50%;",
            "border:1.5px solid currentColor;border-top-color:transparent;",
            "animation:site-i18n-spin .8s linear infinite;}",
            "@keyframes site-i18n-spin{to{transform:rotate(360deg);}}",
            "@media (prefers-reduced-motion:reduce){.site-i18n-spinner{animation:none;opacity:.6;}}"
        ].join("");
        (document.head || document.documentElement).appendChild(style);
    }

    /* Loading throbbers are attached on a pragmatic basis: near paragraphs and
       copywriting specifically. Never shown in English languages, and never on
       interactive UI controls, buttons, table cells, or compact navigation. */
    function isCopywritingElement(element) {
        if (!element || element.nodeType !== 1) return false;
        var tag = (element.tagName || "").toUpperCase();

        // 1. Exclude interactive controls, inputs, headers, navigation, table cells, code
        if (/^(BUTTON|A|INPUT|SELECT|TEXTAREA|NAV|HEADER|FOOTER|THEAD|TBODY|TR|TH|TD|H1|H2|H3|H4|H5|H6|CODE|PRE|KBD|SAMP)$/.test(tag)) {
            return false;
        }
        if (element.closest && element.closest("button, [role='button'], a, .btn, .button, input, select, textarea, nav, .nav, .y1-dock, .site-locale-panel, [data-locale-panel], table, th, td, ul, ol, li, .chip, .badge, h1, h2, h3, h4, h5, h6, dialog, [role='dialog'], [role='menu'], [role='toolbar'], [role='tab']")) {
            return false;
        }

        // 2. Direct paragraph and blockquote elements
        if (tag === "P" || tag === "BLOCKQUOTE" || tag === "DD") {
            // Exclude kickers / eyebrows (e.g. <p class="lumen-kicker">Videos</p>)
            if (element.classList && (element.classList.contains("lumen-kicker") || element.classList.contains("kicker"))) {
                return false;
            }
            return true;
        }

        // 3. Recognized copywriting / prose containers
        if (element.classList) {
            if (element.classList.contains("prose") ||
                element.classList.contains("upload-prose") ||
                element.classList.contains("lumen-notice-body") ||
                element.classList.contains("notice-body") ||
                element.classList.contains("markdown-body") ||
                element.classList.contains("copywriting")) {
                return true;
            }
        }

        return false;
    }

    function getCopywritingContainer(node) {
        if (!node || node.nodeType !== 3) return null;
        if (isEnglishLocale(state.locale)) return null;

        var text = normalise(node.nodeValue);
        // Only trigger throbber for substantial prose / sentence copywriting
        if (text.length < 25 || !/[.!?]/.test(text)) {
            return null;
        }

        var parent = node.parentElement;
        if (!parent) return null;

        // Strictly reject if inside any interactive control, button, anchor, nav, dock, table, dialog, header
        if (parent.closest && parent.closest("button, [role='button'], a, input, select, textarea, nav, .nav, .y1-dock, .site-locale-panel, [data-locale-panel], table, th, td, h1, h2, h3, h4, h5, h6, dialog, [role='dialog'], [role='toolbar'], [role='menu'], [role='tab'], .chip, .badge, .lumen-kicker, .kicker, .btn, .button")) {
            return null;
        }

        var curr = parent;
        while (curr && curr !== document.body && curr !== document.documentElement) {
            if (/^(BUTTON|A|NAV|TABLE|DIALOG|HEADER|FOOTER|H1|H2|H3|H4|H5|H6)$/.test(curr.tagName)) {
                return null;
            }
            if (isCopywritingElement(curr)) {
                var blockText = (curr.textContent || "").trim();
                if (blockText.length >= 25) {
                    return curr;
                }
            }
            curr = curr.parentElement;
        }
        return null;
    }

    function showTranslatingBadge(element) {
        if (isEnglishLocale(state.locale)) return;
        if (!element || !pendingByElement || !element.appendChild) return;
        if (element.closest && element.closest("button, [role='button'], a, nav, .nav, .y1-dock, table, td, th, h1, h2, h3, h4, h5, h6, dialog")) {
            return;
        }
        ensureBadgeStyles();
        var count = pendingByElement.get(element) || 0;
        pendingByElement.set(element, count + 1);
        if (count > 0) return;
        var badge = document.createElement("span");
        badge.className = "site-i18n-badge";
        badge.setAttribute("data-i18n-skip", "");
        badge.setAttribute("translate", "no");
        badge.setAttribute("role", "status");
        badge.setAttribute("aria-label", "Translating");
        badge.innerHTML = BADGE_HTML;
        /* A stuck request must not leave a permanent spinner behind. */
        badge.setAttribute("data-i18n-timeout", String(setTimeout(function () {
            hideTranslatingBadge(element);
        }, 30000)));
        element.appendChild(badge);
    }

    function hideTranslatingBadge(element) {
        if (!element || !pendingByElement) return;
        var count = (pendingByElement.get(element) || 0) - 1;
        if (count > 0) {
            pendingByElement.set(element, count);
            return;
        }
        pendingByElement.delete(element);
        var badges = element.querySelectorAll ? element.querySelectorAll(".site-i18n-badge") : [];
        if (badges.length) {
            for (var i = 0; i < badges.length; i += 1) {
                var badge = badges[i];
                if (badge.getAttribute("data-i18n-timeout")) {
                    clearTimeout(Number(badge.getAttribute("data-i18n-timeout")));
                }
                badge.remove();
            }
        } else if (element.children) {
            for (var j = element.children.length - 1; j >= 0; j -= 1) {
                var child = element.children[j];
                if (child.classList && child.classList.contains("site-i18n-badge")) {
                    if (child.getAttribute("data-i18n-timeout")) {
                        clearTimeout(Number(child.getAttribute("data-i18n-timeout")));
                    }
                    child.remove();
                }
            }
        }
    }

    function queueDynamicText(text, apply, element) {
        var cache = loadDynamicCache();
        var key = dynamicKey(text);
        var waiter = function (value) {
            try {
                if (value) apply(value);
            } finally {
                hideTranslatingBadge(element);
            }
        };
        if (cache[key]) {
            waiter(cache[key]);
            return;
        }
        if (dynamicPending[key]) {
            dynamicPending[key].push(waiter);
            if (element) showTranslatingBadge(element);
            return;
        }
        if (dynamicRequests >= DYNAMIC_MAX_REQUESTS) return;
        dynamicPending[key] = [waiter];
        if (element) showTranslatingBadge(element);
        dynamicQueue.push({ key: key, text: text });
        drainDynamic();
    }

    function queueDynamic(root) {
        if (!dynamicEnabled() || !root) return;
        var containers = [];
        if (root.nodeType === 1 && root.matches && root.matches(DYNAMIC_CONTAINERS)) {
            containers.push(root);
        }
        if (root.querySelectorAll) {
            containers = containers.concat(
                Array.prototype.slice.call(root.querySelectorAll(DYNAMIC_CONTAINERS))
            );
        }
        containers.forEach(function (container) {
            var wholePage = container === document.body;
            if (!wholePage && container.getAttribute("data-i18n-dynamic-state") === "done") return;
            if (!wholePage) container.setAttribute("data-i18n-dynamic-state", "loading");
            if (typeof document.createTreeWalker !== "function") return;
            var walker = document.createTreeWalker(container, NodeFilter.SHOW_TEXT, {
                acceptNode: function (node) {
                    var parent = node.parentElement;
                    if (!parent) return NodeFilter.FILTER_REJECT;
                    if (/^(SCRIPT|STYLE|PRE|CODE|KBD|SAMP|TEXTAREA)$/.test(parent.tagName)) {
                        return NodeFilter.FILTER_REJECT;
                    }
                    if (parent.closest("[data-i18n-skip]")) return NodeFilter.FILTER_REJECT;
                    if (parent.closest("[data-locale-panel]")) return NodeFilter.FILTER_REJECT;
                    if (catalogApplied && catalogApplied.has(node)) return NodeFilter.FILTER_REJECT;
                    if (dynamicSeen && dynamicSeen.has(node)) return NodeFilter.FILTER_REJECT;
                    var value = normalise(node.nodeValue);
                    if (value.length < 4 || !/[A-Za-z]{2}/.test(value)) return NodeFilter.FILTER_REJECT;
                    /* Sizes, versions, paths and code are not prose. */
                    if (/^\d+([.,]\d+)?\s?(MB|GB|KB|TB|MBps)$/i.test(value)) return NodeFilter.FILTER_REJECT;
                    if (/^(https?:\/\/|mailto:|www\.)/i.test(value)) return NodeFilter.FILTER_REJECT;
                    if (/^[\d\s.,:%+\-–—/()×]+$/.test(value)) return NodeFilter.FILTER_REJECT;
                    /* Covered by the catalog, unless the entry only repeats the
                       English text (what the provider returns for copy it
                       leaves untouched); that still needs the API. */
                    var known = state.strings[value];
                    if (known && known !== value) return NodeFilter.FILTER_REJECT;
                    /* A label that is only a brand name stays as written. */
                    if (isBrandOnly(value)) return NodeFilter.FILTER_REJECT;
                    return NodeFilter.FILTER_ACCEPT;
                }
            });
            var node;
            while ((node = walker.nextNode())) {
                if (dynamicSeen) dynamicSeen.add(node);
                (function (target) {
                    var raw = target.nodeValue;
                    var prefix = /^\s*/.exec(raw)[0];
                    var suffix = /\s*$/.exec(raw)[0];
                    var text = normalise(raw);
                    var badgeTarget = getCopywritingContainer(target);
                    queueDynamicText(text, function (translated) {
                        target.nodeValue = prefix + translated + suffix;
                    }, badgeTarget);
                }(node));
            }
            if (!wholePage) container.setAttribute("data-i18n-dynamic-state", "done");
        });

        /* Attribute copy (aria-label, title, alt, placeholder) needs the same
           treatment; the catalog pass only handles what it was given. */
        if (root.querySelectorAll) {
            Array.prototype.forEach.call(
                root.querySelectorAll("[title],[alt],[placeholder],[aria-label],[aria-description]"),
                function (element) {
                    if (element.closest("[data-locale-panel]")) return;
                    if (element.closest("[data-i18n-skip]")) return;
                    if (element.closest(".site-i18n-badge")) return;
                    if (dynamicAttrSeen.has(element)) return;
                    dynamicAttrSeen.add(element);
                    ATTRIBUTES.forEach(function (name) {
                        var raw = element.getAttribute(name);
                        if (!raw) return;
                        var text = normalise(raw);
                        if (text.length < 4 || !/[A-Za-z]{2}/.test(text)) return;
                        var known = state.strings[text];
                        if (known && known !== text) return;
                        if (isBrandOnly(text)) return;
                        queueDynamicText(text, function (translated) {
                            element.setAttribute(name, translated);
                        }, null);
                    });
                }
            );
        }
    }

    var dynamicScanTimer = null;

    function scheduleDynamicScan() {
        if (!dynamicEnabled()) return;
        if (dynamicScanTimer) return;
        dynamicScanTimer = setTimeout(function () {
            dynamicScanTimer = null;
            queueDynamic(document.body);
        }, 400);
    }

    function applyLanguage() {
        var root = document.documentElement;
        if (!root) return;
        root.setAttribute("lang", state.locale);
        root.setAttribute("dir", state.dir);
        root.setAttribute("data-locale", state.locale);
        /* Keep the dock label in the reader's language, wherever it is. */
        Array.prototype.forEach.call(document.querySelectorAll("[data-locale-open] .site-locale-toggle-label"), function (label) {
            label.textContent = labelFor(state.locale);
        });

        if (state.locale === DEFAULT_LOCALE && !Object.keys(state.regionCopy).length) {
            translateHead();
            return;
        }
        if (!document.body) return;
        applying = true;
        try {
            translateTree(document.body);
        } finally {
            applying = false;
        }
        scheduleDynamicScan();
        translateHead();
    }

    function watch() {
        if (observer || typeof MutationObserver !== "function" || !document.body) return;
        observer = new MutationObserver(function (records) {
            if (applying) return;
            if (!state.strings && !Object.keys(state.regionCopy).length) return;
            applying = true;
            try {
                for (var i = 0; i < records.length; i += 1) {
                    var record = records[i];
                    if (record.type === "childList") {
                        for (var j = 0; j < record.addedNodes.length; j += 1) {
                            var added = record.addedNodes[j];
                            if (added.nodeType === 3) translateTree(added);
                            else if (added.nodeType === 1 && !added.hasAttribute("data-locale-panel")) {
                                translateTree(added);
                                /* Release notes, READMEs and notices land here. */
                                scheduleDynamicScan();
                            }
                        }
                    } else if (record.type === "characterData" && record.target) {
                        var value = translateValue(record.target.nodeValue);
                        if (value !== record.target.nodeValue) record.target.nodeValue = value;
                    }
                }
            } finally {
                applying = false;
            }
        });
        observer.observe(document.body, { childList: true, subtree: true, characterData: true });
    }

    /* ---------------------------------------------------------------- */
    /* Region gating                                                    */
    /* ---------------------------------------------------------------- */

    function listed(value) {
        return String(value || "").split(",").map(function (part) {
            return part.trim().toLowerCase();
        }).filter(Boolean);
    }

    function regionAllows(element) {
        var only = element.getAttribute("data-region-only");
        if (only && listed(only).indexOf(state.region) < 0) return false;
        var hide = element.getAttribute("data-region-hide");
        if (hide && listed(hide).indexOf(state.region) >= 0) return false;
        var need = element.getAttribute("data-availability");
        if (need && !state.availability[normalise(need).toLowerCase()]) return false;
        var deny = element.getAttribute("data-availability-hide");
        if (deny && state.availability[normalise(deny).toLowerCase()]) return false;
        return true;
    }

    function applyRegions() {
        var nodes = document.querySelectorAll(
            "[data-region-only], [data-region-hide], [data-availability], [data-availability-hide]"
        );
        Array.prototype.forEach.call(nodes, function (element) {
            if (regionAllows(element)) {
                element.removeAttribute("hidden");
                element.removeAttribute("data-region-hidden");
                if (element.getAttribute("data-region-was-display") !== null) {
                    element.style.display = element.getAttribute("data-region-was-display");
                    element.removeAttribute("data-region-was-display");
                }
            } else {
                element.setAttribute("data-region-hidden", "1");
                element.setAttribute("hidden", "");
                if (element.style && element.style.display && element.style.display !== "none") {
                    element.setAttribute("data-region-was-display", element.style.display);
                    element.style.display = "none";
                }
            }
        });
        document.documentElement.setAttribute("data-region", state.region);
    }

    /* ---------------------------------------------------------------- */
    /* Picker                                                           */
    /* ---------------------------------------------------------------- */

    var STRINGS = {
        language: "Language",
        region: "Edition",
        search: "Search languages",
        close: "Close",
        allLanguages: "All languages",
        editionNote: "The edition changes what this site offers, not just the language.",
        english: "English (original)"
    };

    function t(key) {
        if (!state.strings) return STRINGS[key];
        return state.strings[STRINGS[key]] || STRINGS[key];
    }

    function buildPanel() {
        if (state.panel) return state.panel;

        var panel = document.createElement("div");
        panel.className = "site-locale-panel";
        panel.id = "site-locale-panel";
        panel.setAttribute("data-locale-panel", "1");
        panel.setAttribute("role", "dialog");
        panel.setAttribute("aria-modal", "true");
        panel.setAttribute("aria-label", t("language"));
        panel.hidden = true;

        var header = document.createElement("div");
        header.className = "site-locale-panel-head";
        header.innerHTML =
            '<strong class="site-locale-panel-title"></strong>' +
            '<button type="button" class="site-locale-close" aria-label="' + escapeHtml(t("close")) + '">×</button>';
        panel.appendChild(header);

        var search = document.createElement("input");
        search.type = "search";
        search.className = "site-locale-search";
        search.placeholder = t("search");
        search.setAttribute("aria-label", t("search"));
        panel.appendChild(search);

        var list = document.createElement("div");
        list.className = "site-locale-list";
        list.setAttribute("role", "listbox");
        panel.appendChild(list);

        /* No edition picker: the market is decided by geography, not by a
           visitor choosing it next to the language. */
        document.body.appendChild(panel);
        state.panel = panel;

        header.querySelector(".site-locale-close").addEventListener("click", closePanel);
        search.addEventListener("input", function () {
            renderList(list, search.value);
        });
        panel.addEventListener("click", function (event) {
            if (event.target === panel) closePanel();
        });
        document.addEventListener("keydown", function (event) {
            if (event.key === "Escape" && !panel.hidden) closePanel();
        });

        renderList(list, "");
        return panel;
    }

    function escapeHtml(value) {
        return String(value).replace(/[&<>"']/g, function (character) {
            return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[character];
        });
    }

    function renderList(container, query) {
        var needle = normalise(query).toLowerCase();
        container.innerHTML = "";

        var entries = state.locales.filter(function (entry) {
            if (!needle) return true;
            return (entry.code + " " + entry.name + " " + entry.native).toLowerCase().indexOf(needle) >= 0;
        });

        if (!entries.some(function (entry) { return entry.code === DEFAULT_LOCALE; })) {
            entries.unshift({ code: DEFAULT_LOCALE, name: "English", native: "English", dir: "ltr" });
        }

        entries.forEach(function (entry) {
            var button = document.createElement("button");
            button.type = "button";
            button.className = "site-locale-item";
            button.setAttribute("role", "option");
            button.setAttribute("data-code", entry.code);
            if (entry.code === state.locale) {
                button.classList.add("is-current");
                button.setAttribute("aria-selected", "true");
            }
            var native = document.createElement("span");
            native.className = "site-locale-native";
            native.setAttribute("lang", entry.code);
            native.setAttribute("dir", entry.dir || "ltr");
            native.textContent = entry.native || entry.name;
            var english = document.createElement("span");
            english.className = "site-locale-english";
            english.textContent = entry.name;
            button.appendChild(native);
            button.appendChild(english);
            button.addEventListener("click", function () { setLocale(entry.code); });
            container.appendChild(button);
        });
    }

    function renderEditions(container) {
        container.hidden = true;
        return;
        var regions = state.regions && state.regions.regions ? state.regions.regions : {};
        var codes = Object.keys(regions);
        if (codes.length < 2) {
            container.hidden = true;
            return;
        }
        container.innerHTML = "";
        var label = document.createElement("div");
        label.className = "site-locale-editions-label";
        label.textContent = t("region");
        container.appendChild(label);

        var row = document.createElement("div");
        row.className = "site-locale-editions-row";
        codes.forEach(function (code) {
            var button = document.createElement("button");
            button.type = "button";
            button.className = "site-locale-edition";
            button.textContent = regions[code].label || code;
            if (code === state.region) button.classList.add("is-current");
            button.addEventListener("click", function () { setRegion(code); });
            row.appendChild(button);
        });
        container.appendChild(row);

        var note = document.createElement("p");
        note.className = "site-locale-note";
        note.textContent = t("editionNote");
        container.appendChild(note);
    }

    function openPanel() {
        var panel = buildPanel();
        panel.hidden = false;
        document.documentElement.classList.add("site-locale-open");
        var search = panel.querySelector(".site-locale-search");
        if (search) {
            search.value = "";
            renderList(panel.querySelector(".site-locale-list"), "");
            search.focus();
        }
    }

    function closePanel() {
        if (!state.panel) return;
        state.panel.hidden = true;
        document.documentElement.classList.remove("site-locale-open");
    }

    function togglePanel() {
        var panel = buildPanel();
        if (panel.hidden) openPanel();
        else closePanel();
    }

    function labelFor(code) {
        for (var i = 0; i < state.locales.length; i += 1) {
            if (state.locales[i].code === code) return state.locales[i].native || state.locales[i].name;
        }
        return "English";
    }

    /* GA4 / GTM. Every page already ships the Google Tag Manager container;
       these events tell GA4 which language the visitor is actually reading,
       which a page URL alone cannot (the runtime swaps language in place).
       A site may also set a direct GA4 measurement id with
       <meta name="ga4-measurement-id" content="G-..."> or
       window.INNIOASIS_GA4_ID; in that case gtag.js is loaded once with
       manual page views so a language switch is a counted page view rather
       than a silent text swap. */
    var analyticsReady = false;

    function ga4MeasurementId() {
        var meta = document.querySelector('meta[name="ga4-measurement-id"]');
        var id = (meta && meta.getAttribute("content")) || global.INNIOASIS_GA4_ID || "";
        return /^G-[A-Z0-9]{4,}$/i.test(id) ? id : "";
    }

    function initAnalytics() {
        if (analyticsReady) return;
        analyticsReady = true;
        global.dataLayer = global.dataLayer || [];
        var id = ga4MeasurementId();
        if (!id) return;
        if (!global.gtag) {
            global.gtag = function () { global.dataLayer.push(arguments); };
        }
        if (!document.querySelector('script[src*="googletagmanager.com/gtag/js"]')) {
            var tag = document.createElement("script");
            tag.async = true;
            tag.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(id);
            document.head.appendChild(tag);
        }
        global.gtag("js", new Date());
        global.gtag("config", id, { send_page_view: false });
        global.gtag("set", { user_properties: { site_language: state.locale || DEFAULT_LOCALE } });
    }

    function track(event, params) {
        initAnalytics();
        var payload = {
            event: event,
            site_language: state.locale || DEFAULT_LOCALE,
            site_locale_label: labelFor(state.locale || DEFAULT_LOCALE),
            site_region: state.region || "intl",
            page_path: global.location.pathname + global.location.search
        };
        Object.keys(params || {}).forEach(function (key) {
            payload[key] = params[key];
        });
        global.dataLayer.push(payload);
        if (global.gtag && ga4MeasurementId()) {
            global.gtag("event", event, payload);
        }
    }

    function trackPageView() {
        if (!ga4MeasurementId()) {
            track("site_language_view");
            return;
        }
        track("page_view", {
            page_title: document.title,
            page_location: global.location.href,
            language: state.locale || DEFAULT_LOCALE
        });
    }

    /* The language control lives in the bottom support dock, which every page
       mounts (support_toolbar.html). The static button is bound when it
       arrives; when a page has no dock, the old nav/floating control is
       created so the picker is never unreachable. */
    function markToggle(button) {
        var label = button.querySelector(".site-locale-toggle-label");
        var text = labelFor(state.locale);
        if (label) label.textContent = text;
        button.title = t("language");
        button.setAttribute("aria-label", t("language") + ": " + text);
        button.setAttribute("aria-haspopup", "dialog");
        button.classList.add("site-locale-toggle");
    }

    function bindExistingToggle() {
        var buttons = document.querySelectorAll("[data-locale-open]");
        var bound = 0;
        Array.prototype.forEach.call(buttons, function (button) {
            markToggle(button);
            bound += 1;
            if (button.dataset.localeBound === "1") return;
            button.dataset.localeBound = "1";
            button.addEventListener("click", function (event) {
                event.preventDefault();
                togglePanel();
            });
        });
        return bound;
    }

    function createToggle(host) {
        var button = document.createElement("button");
        button.type = "button";
        button.className = "site-locale-toggle";
        button.setAttribute("data-locale-open", "1");
        button.innerHTML =
            '<span class="site-locale-globe" aria-hidden="true">' +
            '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.8">' +
            '<circle cx="12" cy="12" r="9"></circle><path d="M3 12h18M12 3c2.6 3 2.6 15 0 18M12 3c-2.6 3-2.6 15 0 18"></path>' +
            "</svg></span>" +
            '<span class="site-locale-toggle-label"></span>';
        markToggle(button);
        button.addEventListener("click", function (event) {
            event.preventDefault();
            togglePanel();
        });
        button.dataset.localeBound = "1";

        if (host) {
            if (host.id === "nav-root" || host.classList.contains("nav-tools")) {
                host.insertBefore(button, host.firstChild);
            } else {
                host.appendChild(button);
            }
        } else {
            button.classList.add("site-locale-toggle--floating");
            document.body.appendChild(button);
        }
        return button;
    }

    function mountToggle() {
        if (bindExistingToggle()) return;
        if (document.querySelector(".site-locale-toggle")) return;
        /* site-init.js injects support_toolbar.html after DOMContentLoaded.
           Wait for it instead of adding a second, floating control that the
           dock button would then duplicate. */
        var slot = document.getElementById("support-toolbar-slot");
        if (slot && slot.dataset.shellLoaded !== "1") return;
        var dock = document.getElementById("y1-dock-buttons-layer");
        var tools = document.querySelector("#nav-root .nav-tools") || document.querySelector(".nav-tools");
        createToggle(dock || tools);
    }

    /* ---------------------------------------------------------------- */
    /* Switching                                                         */
    /* ---------------------------------------------------------------- */

    function navigate(params) {
        var url = new URL(global.location.href);
        Object.keys(params).forEach(function (key) {
            url.searchParams.set(key, params[key]);
        });
        global.location.href = url.pathname + url.search + url.hash;
    }

    /* Two routes to the same page in another language, because the hosting may
       serve pre-rendered copies or only the English tree:
         1. a copy at /<locale>/<page> when the build published one (best: the
            text is translated in the HTML, with hreflang),
         2. ?lang=<locale> on the current page otherwise (always available).
       The copy list is written by prerender.py, so a site that never ran it
       simply never sees route 1. */
    function copyPathFor(code) {
        var map = localeIndex();
        var segments = global.location.pathname.split("/").filter(Boolean);
        if (segments.length && map[normalizeTag(segments[0])]) segments.shift();
        if (code === DEFAULT_LOCALE) return "/" + segments.join("/");
        return "/" + code + (segments.length ? "/" + segments.join("/") : "/");
    }

    function hasCopy(code) {
        if (!state.copies || !state.copies.length) return false;
        return state.copies.indexOf(code) >= 0;
    }

    function goToCopy(code) {
        var target = copyPathFor(code);
        var fallback = function () { navigate({ lang: code }); };
        try {
            fetch(target, { method: "HEAD", cache: "no-store" })
                .then(function (response) {
                    if (response.ok) global.location.href = target + (global.location.hash || "");
                    else fallback();
                })
                .catch(fallback);
        } catch (_) {
            fallback();
        }
    }

    function setLocale(code) {
        if (!code || code === state.locale) {
            closePanel();
            return;
        }
        writeStorage(STORAGE_LOCALE, code);
        track("site_language_change", { language_chosen: code });

        var map = localeIndex();
        var onCopy = !!map[normalizeTag(global.location.pathname.split("/").filter(Boolean)[0] || "")];

        if (hasCopy(code) || onCopy) {
            goToCopy(code);
            return;
        }
        /* No pre-rendered copies shipped: the URL variable is the switch. */
        navigate({ lang: code });
    }

    function setRegion(code) {
        if (!code) return;
        writeStorage(STORAGE_REGION, code);
        navigate({ region: code, lang: state.locale });
    }

    /* ---------------------------------------------------------------- */
    /* Boot                                                             */
    /* ---------------------------------------------------------------- */

    function loadCatalog(code) {
        var map = localeIndex();
        var entry = map[normalizeTag(code)] || {};
        var base = entry.base || code;
        return fetchJson("i18n/catalogs/" + base + ".json", 6000)
            .then(function (catalog) {
                state.dir = catalog.dir || entry.dir || "ltr";
                return catalog.strings || {};
            })
            .catch(function () {
                if (base !== code && base.indexOf("-") > 0) {
                    var language = base.split("-")[0];
                    return fetchJson("i18n/catalogs/" + language + ".json", 6000)
                        .then(function (catalog) {
                            state.dir = catalog.dir || entry.dir || "ltr";
                            return catalog.strings || {};
                        })
                        .catch(function () { return null; });
                }
                return null;
            });
    }

    function injectStylesheet() {
        if (document.getElementById("site-locale-styles")) return;
        var link = document.createElement("link");
        link.id = "site-locale-styles";
        link.rel = "stylesheet";
        link.href = baseUrl + "site-locale.css?v=" + RUNTIME_VERSION;
        document.head.appendChild(link);
    }

    function start() {
        baseUrl = scriptBase();
        injectStylesheet();

        Promise.all([
            fetchJson("i18n/site-locales.json", 6000).catch(function () { return { locales: [] }; }),
            fetchJson("i18n/regions.json", 6000).catch(function () { return null; }),
            fetchJson("i18n/prerendered.json", 6000).catch(function () { return null; })
        ]).then(function (results) {
            state.locales = (results[0] && results[0].locales) || [];
            state.regions = results[1];
            state.copies = (results[2] && results[2].locales) || [];
            return confirmCountry();
        }).then(function () {
            state.region = resolveRegion();
            state.locale = resolveLocale();
            var map = localeIndex();
            var entry = map[normalizeTag(state.locale)] || {};
            state.dir = entry.dir || "ltr";

            /* The China edition is a Chinese-language edition. A stored or
               auto-detected edition must not survive an explicit choice of
               another language, or the page ends up Chinese in German
               clothing. An explicit ?region= stays respected. */
            if (!param("region") && state.region === "cn" && !/^zh(-|$)/.test(state.locale)) {
                state.region = (state.regions && state.regions.default) || "intl";
            }
            var resolvedRegion = state.regions && state.regions.regions
                ? state.regions.regions[state.region]
                : null;
            state.availability = (resolvedRegion && resolvedRegion.availability) || {};
            state.regionCopy = (resolvedRegion && resolvedRegion.copy) || {};

            applyRegions();
            applyLanguage();

            var needsCatalog = baseOfLocale(state.locale) !== DEFAULT_LOCALE;
            if (!needsCatalog) return null;
            return loadCatalog(state.locale);
        }).then(function (catalog) {
            if (catalog) {
                state.strings = catalog;
                applyLanguage();
            }
            watch();
            if (document.body) mountToggle();
            else document.addEventListener("DOMContentLoaded", mountToggle);
            /* The dock is injected after DOMContentLoaded by site-init.js, so
               bind its language button when it lands and when the toolbar
               reports ready. */
            global.addEventListener("y1-dock-slot-ready", function () {
                mountToggle();
                if (bindExistingToggle()) applyLanguage();
            });
            document.addEventListener("click", function (event) {
                var trigger = event.target.closest && event.target.closest("[data-locale-open]");
                if (!trigger) return;
                if (trigger.dataset.localeBound !== "1") {
                    /* The first click on an injected dock button must open the
                       panel, not merely bind the listener for a second click. */
                    bindExistingToggle();
                    event.preventDefault();
                    togglePanel();
                }
            }, true);
            document.documentElement.setAttribute("data-locale-ready", "1");
            trackPageView();
        }).catch(function () {
            /* A failed boot must leave an English page, never a blank one. */
            document.documentElement.setAttribute("data-locale-ready", "1");
        });
    }

    function baseOfLocale(code) {
        if (isEnglishLocale(code)) return DEFAULT_LOCALE;
        var map = localeIndex();
        var entry = map[normalizeTag(code)];
        if (!entry) return normalizeTag(code).split("-")[0];
        var base = normalizeTag(entry.base || entry.code);
        return isEnglishLocale(base) ? DEFAULT_LOCALE : base;
    }

    global.InnioasisLocale = {
        get locale() { return state.locale; },
        get direction() { return state.dir; },
        get region() { return state.region; },
        availability: function (feature) {
            return !!state.availability[String(feature || "").toLowerCase()];
        },
        set: setLocale,
        setRegion: setRegion,
        open: openPanel,
        close: closePanel,
        /* Re-run translation over content a page rendered after boot (release
           notes, READMEs, firmware lists). The MutationObserver covers most
           of it; this is the explicit hook for a page that replaces a large
           subtree in one write. */
        refresh: applyLanguage,
        translateDynamic: queueDynamic,
        translate: function (text) {
            var source = normalise(text);
            if (!source) return text;
            return translateValue(source);
        },
        label: labelFor
    };

    if (document.readyState === "loading") {
        document.addEventListener("DOMContentLoaded", function () { void start(); });
    } else {
        void start();
    }
})(typeof window !== "undefined" ? window : globalThis);
