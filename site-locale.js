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
    var RUNTIME_VERSION = "20261109i18n";
    /* Catalogs are re-fetched under a new URL when their content changes.
       Without this a returning visitor keeps the copy they cached, so a
       language whose catalog was just completed still reads as English. */
    var CATALOG_VERSION = "20261110i18n";;
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
        copies: [],
        prerendered: null
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
            cache: "default",
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
        var tag = String(value || "").toLowerCase().replace(/_/g, "-");
        if (tag === "jp") return "ja";
        if (tag === "zh") return "zh-cn";
        return tag;
    }

    /* ---------------------------------------------------------------- */
    /* Locale resolution                                                */
    /* ---------------------------------------------------------------- */

    function localeIndex() {
        var map = {};
        map[DEFAULT_LOCALE] = { code: DEFAULT_LOCALE, name: "English", native: "English", dir: "ltr" };
        map["en-us"] = { code: "en-US", base: "en", name: "English (United States)", native: "English (US)", dir: "ltr" };
        map["en-gb"] = { code: "en-GB", base: "en", name: "English (United Kingdom)", native: "English (UK)", dir: "ltr" };
        state.locales.forEach(function (entry) {
            var c = entry.code.toLowerCase();
            map[c] = entry;
            if (c === "ja") map["jp"] = entry;
            if (c === "zh-cn") map["zh"] = entry;
        });
        return map;
    }

    function pathLocale() {
        var pathname = (global.location && global.location.pathname) || "";
        // Detect literal static file pattern: <page>_<lang>.html (e.g. index_de.html, index_jp.html)
        var fileMatch = pathname.match(/_([a-z]{2,3}(?:-[a-z0-9]{2,4})?)\.html$/i);
        var map = localeIndex();
        if (fileMatch) {
            var fileTag = normalizeTag(fileMatch[1]);
            if (map[fileTag]) return map[fileTag].code;
            if (fileTag === "jp" && map["ja"]) return map["ja"].code;
        }

        var segments = pathname.split("/").filter(Boolean);
        if (!segments.length) return "";
        var candidate = normalizeTag(segments[0]);
        if (map[candidate]) return map[candidate].code;
        if (candidate === "jp" && map["ja"]) return map["ja"].code;
        return "";
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
            if (/^[a-z]{2,3}(-[a-z0-9]{2,4})?$/.test(requested)) return requested;
        }
        var fromHtml = normalizeTag((document.documentElement && (document.documentElement.getAttribute("data-locale") || document.documentElement.lang)) || "");
        if (fromHtml && fromHtml !== "en") {
            if (map[fromHtml]) return map[fromHtml].code;
            if (fromHtml === "jp" && map["ja"]) return map["ja"].code;
            if (fromHtml === "zh" && map["zh-cn"]) return map["zh-cn"].code;
            if (/^[a-z]{2,3}(-[a-z0-9]{2,4})?$/.test(fromHtml)) return fromHtml;
        }
        var fromPath = pathLocale();
        if (fromPath) return fromPath;
        var stored = normalizeTag(readStorage(STORAGE_LOCALE));
        if (stored && map[stored]) return stored;
        var fromCookie = normalizeTag(getSharedCookie(STORAGE_LOCALE));
        if (fromCookie && map[fromCookie]) return fromCookie;
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
        var ctrl = typeof AbortController === "function" ? new AbortController() : null;
        var timer = ctrl ? setTimeout(function () { ctrl.abort(); }, 1200) : null;
        return fetch(baseUrl + "cdn-cgi/trace", { cache: "no-store", signal: ctrl ? ctrl.signal : undefined })
            .then(function (response) { if (timer) clearTimeout(timer); return response.ok ? response.text() : ""; })
            .then(function (text) {
                var match = /(?:^|\n)loc=([A-Z]{2})(?:\n|$)/.exec(text || "");
                if (!match) return;
                writeStorage(STORAGE_COUNTRY, match[1]);
            })
            .catch(function () { if (timer) clearTimeout(timer); });
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

        /* OS proper nouns must never be translated into dictionary words */
        if (/^(Windows|macOS|Linux|Android|iOS|Windows on ARM|Linux on ARM)$/i.test(core)) {
            if (/^windows$/i.test(core)) return parts[1] + "Windows" + parts[3];
            if (/^macos$/i.test(core)) return parts[1] + "macOS" + parts[3];
            if (/^linux$/i.test(core)) return parts[1] + "Linux" + parts[3];
            if (/^android$/i.test(core)) return parts[1] + "Android" + parts[3];
            if (/^ios$/i.test(core)) return parts[1] + "iOS" + parts[3];
            if (/^windows on arm$/i.test(core)) return parts[1] + "Windows on ARM" + parts[3];
            if (/^linux on arm$/i.test(core)) return parts[1] + "Linux on ARM" + parts[3];
        }

        var regional = regionValue(core);
        if (regional) return parts[1] + regional + parts[3];

        if (!state.strings) return value;
        var translated = state.strings[core];
        if (translated === undefined) {
            noteMissingSource(core);
            return value;
        }
        if (typeof translated === "string") {
            if (translated.indexOf("Spectre") !== -1) {
                translated = translated.replace(/\bRyan Spectre\b/g, "Ryan Specter").replace(/\bSpectre\b/g, "Specter");
            }
            if (/\bWindows\b/.test(core) && !/\b(window|finder window|terminal window)\b/i.test(core)) {
                translated = translated.replace(/\b(jendela|ventanas|fenêtres|finestre|fenster|okna)\b/gi, "Windows");
            }
        }
        return parts[1] + translated + parts[3];
    }

    /* ---- Missing-source collector ---------------------------------------
       A catalog is never complete on the day a page ships, so this is the
       feedback loop that closes the gap instead of waiting for someone to
       notice: when a non-English page finds no catalog entry for a source
       string, the reader sees English, and that string is collected.

       Batches go to /i18n-missing, where a translation run picks them up
       (scripts/i18n/drain_missing.py). Only strings from our own source
       catalogue survive that run, so author-written theme and app
       descriptions are dropped rather than translated.

       Nothing about the reader is sent: no identifier, no typed text, and the
       endpoint keeps no IP or user agent. The queue is deduplicated, capped,
       honours the analytics choice and Do Not Track, and is attempted once per
       page so a broken endpoint cannot become a request loop. */
    var MISSING_KEY = "innioasis-i18n-misses";
    var MISSING_ENDPOINT = "/i18n-missing";
    var MISSING_MAX_QUEUE = 200;
    var MISSING_MAX_SEND = 40;
    var MISSING_MAX_TEXT = 300;
    var missingQueue = null;
    var missingSent = 0;
    var missingTimer = null;

    function missingRead() {
        if (missingQueue) return missingQueue;
        missingQueue = [];
        try {
            var raw = global.localStorage.getItem(MISSING_KEY);
            var parsed = raw ? JSON.parse(raw) : null;
            if (parsed && parsed.length) missingQueue = parsed.slice(0, MISSING_MAX_QUEUE);
        } catch (_) {}
        return missingQueue;
    }

    function missingWrite() {
        try {
            global.localStorage.setItem(MISSING_KEY, JSON.stringify(missingQueue.slice(0, MISSING_MAX_QUEUE)));
        } catch (_) {}
    }

    /* English pages have nothing to collect, and neither do the English
       regional variants: they inherit the source by design. */
    function missingAllowed() {
        var base = baseOfLocale(state.locale || "");
        if (!base || base.toLowerCase() === DEFAULT_LOCALE) return false;
        try {
            if (
                global.INNIOASIS_PRIVACY &&
                typeof global.INNIOASIS_PRIVACY.allows === "function" &&
                !global.INNIOASIS_PRIVACY.allows("analytics")
            ) {
                return false;
            }
        } catch (_) {}
        try {
            if (navigator.doNotTrack === "1" || navigator.globalPrivacyControl === true) return false;
        } catch (_) {}
        return true;
    }

    function noteMissingSource(text) {
        var value = normalise(text);
        if (!value || value.length < 4 || value.length > MISSING_MAX_TEXT) return;
        if (!/[A-Za-z]{2}/.test(value)) return;
        if (!missingAllowed()) return;
        /* A language switch re-translates text that is already in the target
           language; that copy is not a missing source. */
        if (catalogHasValue(value)) return;
        var queue = missingRead();
        if (queue.indexOf(value) !== -1) return;
        if (queue.length >= MISSING_MAX_QUEUE) return;
        queue.push(value);
        missingWrite();
        if (!missingTimer && typeof setTimeout === "function") {
            missingTimer = setTimeout(function () {
                missingTimer = null;
                flushMissingSources(false);
            }, 12000);
        }
    }

    function flushMissingSources(useBeacon) {
        var queue = missingRead();
        if (!queue.length || !missingAllowed()) return;
        if (missingSent >= MISSING_MAX_QUEUE) return;
        var batch = queue.slice(0, MISSING_MAX_SEND);
        var body = JSON.stringify({
            locale: state.locale,
            base: baseOfLocale(state.locale || ""),
            page: (global.location && global.location.pathname) || "/",
            strings: batch
        });

        function done() {
            missingSent += batch.length;
            var sent = {};
            for (var i = 0; i < batch.length; i += 1) sent[batch[i]] = 1;
            missingQueue = missingRead().filter(function (item) {
                return !sent[item];
            });
            missingWrite();
        }

        try {
            if (
                useBeacon &&
                navigator.sendBeacon &&
                navigator.sendBeacon(MISSING_ENDPOINT, new Blob([body], { type: "application/json" }))
            ) {
                done();
                return;
            }
        } catch (_) {}
        try {
            if (global.fetch) {
                global
                    .fetch(MISSING_ENDPOINT, {
                        method: "POST",
                        headers: { "Content-Type": "application/json" },
                        body: body,
                        keepalive: true,
                        mode: "cors"
                    })
                    .then(done)
                    .catch(function () {});
                return;
            }
        } catch (_) {}
        try {
            var xhr = new XMLHttpRequest();
            xhr.open("POST", MISSING_ENDPOINT, true);
            xhr.setRequestHeader("Content-Type", "application/json");
            xhr.onload = done;
            xhr.send(body);
        } catch (_) {}
    }

    try {
        global.addEventListener("pagehide", function () {
            flushMissingSources(true);
        });
        global.addEventListener("visibilitychange", function () {
            if (document.visibilityState === "hidden") flushMissingSources(true);
        });
    } catch (_) {}

    /* Values this locale already has from its catalog. After the catalog pass a
       node holds the translated value, not the English key, so looking only for
       keys sent already-translated copy to the API again and put a spinner on
       text the reader could already read in their own language. */
    var catalogValues = null;

    function catalogValueSet() {
        if (catalogValues) return catalogValues;
        catalogValues = typeof Set === "function" ? new Set() : null;
        if (!catalogValues || !state.strings) return catalogValues;
        for (var key in state.strings) {
            if (!Object.prototype.hasOwnProperty.call(state.strings, key)) continue;
            var value = state.strings[key];
            if (value && value !== key) catalogValues.add(normalise(value));
        }
        return catalogValues;
    }

    /* A rendered label often carries an emoji or a trailing count that the
       catalog entry does not, so an exact lookup says "not translated" and the
       API receives German copy with a new icon in front of it. Strip the
       decoration before deciding. */
    function catalogHasValue(value) {
        var seen = catalogValueSet();
        if (!seen) return false;
        if (seen.has(value)) return true;
        var letters = "0-9A-Za-z\\u00C0-\\u024F\\u0370-\\u03FF\\u0400-\\u04FF\\u0590-\\u05FF\\u0600-\\u06FF\\u0900-\\u097F\\u0E00-\\u0E7F\\u3040-\\u30FF\\u3400-\\u9FFF\\uAC00-\\uD7AF";
        var trimmed = value
            .replace(new RegExp("^[^" + letters + "]+"), "")
            .replace(new RegExp("[^" + letters + "]+$"), "")
            .trim();
        return trimmed !== value && seen.has(trimmed);
    }

    function shouldSkip(element) {
        if (!element) return false;
        if (SKIP_TAGS[element.tagName]) return true;
        if (element.hasAttribute && element.hasAttribute("data-i18n-skip")) return true;
        if (element.getAttribute && element.getAttribute("translate") === "no") return true;
        return false;
    }

    /* The English (or recovered) source stays on the node. A later language
       choice translates that source again, so the reader does not have to
       reload to leave the language already on screen. */
    function recoverSource(text, reverse) {
        var raw = String(text == null ? "" : text);
        if (!reverse) return raw;
        var parts = /^(\s*)([\s\S]*?)(\s*)$/.exec(raw);
        if (!parts) return raw;
        var key = reverse[normalise(parts[2])];
        return key ? parts[1] + key + parts[3] : raw;
    }

    function catalogReverse(strings) {
        var map = {};
        if (!strings) return map;
        for (var key in strings) {
            if (!Object.prototype.hasOwnProperty.call(strings, key)) continue;
            var value = strings[key];
            if (typeof value !== "string" || !value || value === key) continue;
            var norm = normalise(value);
            if (norm && !map[norm]) map[norm] = key;
        }
        return map;
    }

    function textSource(node, reverse) {
        if (node.__y1Source == null) {
            var current = node.nodeValue;
            /* A prerendered _de.html is already translated. Recording that
               text as the source would make every later language look German.
               stampSources passes a reverse map for that case. */
            if (reverse) node.__y1Source = recoverSource(current, reverse);
            else if (!pathLocale()) node.__y1Source = current;
            else return current;
        }
        return node.__y1Source == null ? node.nodeValue : node.__y1Source;
    }

    function translateAttributes(element, reverse) {
        if (!element.getAttribute) return;
        if (!element.__y1Attrs) element.__y1Attrs = {};
        for (var i = 0; i < ATTRIBUTES.length; i += 1) {
            var name = ATTRIBUTES[i];
            if (element.__y1Attrs[name] == null) {
                if (!element.hasAttribute(name)) continue;
                if (reverse) element.__y1Attrs[name] = recoverSource(element.getAttribute(name), reverse);
                else if (!pathLocale()) element.__y1Attrs[name] = element.getAttribute(name);
                else {
                    var live = element.getAttribute(name);
                    var liveNext = translateValue(live);
                    if (liveNext !== live) element.setAttribute(name, liveNext);
                    continue;
                }
            }
            var next = translateValue(element.__y1Attrs[name]);
            if (next !== element.getAttribute(name)) element.setAttribute(name, next);
        }
    }

    function translateTree(root, reverse) {
        if (!root) return;
        if (root.nodeType === 3) {
            var next = translateValue(textSource(root, reverse));
            if (next !== root.nodeValue) {
                root.nodeValue = next;
                state.applied += 1;
                if (catalogApplied) catalogApplied.add(root);
            }
            return;
        }
        if (root.nodeType !== 1 && root.nodeType !== 9 && root.nodeType !== 11) return;
        if (root.nodeType === 1 && shouldSkip(root)) return;

        if (root.nodeType === 1) translateAttributes(root, reverse);

        for (var node = root.firstChild; node; node = node.nextSibling) {
            if (node.nodeType === 3) {
                var value = translateValue(textSource(node, reverse));
                if (value !== node.nodeValue) {
                    node.nodeValue = value;
                    state.applied += 1;
                    if (catalogApplied) catalogApplied.add(node);
                }
            } else if (node.nodeType === 1) {
                translateTree(node, reverse);
            }
        }
    }

    function translateHead() {
        if (document.__y1Title == null && !pathLocale()) document.__y1Title = document.title;
        var titleSource = document.__y1Title == null ? document.title : document.__y1Title;
        if (!state.strings && !Object.keys(state.regionCopy).length) {
            if (document.__y1Title != null && document.title !== document.__y1Title) document.title = document.__y1Title;
        } else {
            var nextTitle = translateValue(titleSource);
            if (nextTitle !== document.title) document.title = nextTitle;
        }

        var metas = document.querySelectorAll(
            'meta[name="description"], meta[name="keywords"], meta[property^="og:"], meta[name^="twitter:"]'
        );
        Array.prototype.forEach.call(metas, function (meta) {
            var key = (meta.getAttribute("name") || meta.getAttribute("property") || "").toLowerCase();
            if (!META_NAMES[key]) return;
            if (meta.__y1Content == null && !pathLocale()) meta.__y1Content = meta.getAttribute("content") || "";
            var metaSource = meta.__y1Content == null ? (meta.getAttribute("content") || "") : meta.__y1Content;
            var next = (state.strings || Object.keys(state.regionCopy).length)
                ? translateValue(metaSource)
                : (meta.__y1Content == null ? meta.getAttribute("content") || "" : meta.__y1Content);
            if (next !== meta.getAttribute("content")) meta.setAttribute("content", next);
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
        "[data-i18n-dynamic]",
        "#release-body",
        "#doc-body",
        "#notices-list",
        "#lumen-notices-tray-body",
        ".lumen-notice-body",
        "[data-doc-view]",
        "article.lumen-doc-body",
        ".lumen-notice-view"
    ].join(", ");
    var DYNAMIC_CACHE_KEY = "innioasis-dynamic-translations";
    var DYNAMIC_MAX_REQUESTS = 800;
    /* Missing strings share a request. A few batches run together so the
       visible page finishes without opening a connection per string. */
    var DYNAMIC_BATCH_MAX = 48;
    var DYNAMIC_CONCURRENCY = (function () {
        var cores = (typeof navigator !== "undefined" && navigator.hardwareConcurrency) || 8;
        var ua = (typeof navigator !== "undefined" && navigator.userAgent) || "";
        var mobile = /Android|iPhone|iPad|iPod|Mobile/i.test(ua);
        try { if (navigator.userAgentData && navigator.userAgentData.mobile) mobile = true; } catch (_) {}
        return (mobile || cores <= 4) ? 1 : 2;
    })();
    var DYNAMIC_BATCH_URL = 6000;
    /* gtx answers without CORS headers once it rate limits, which is a failed
       fetch rather than a status. Remember it and go straight to the endpoint
       that does work, so the spinner is not held open by a dead hop. */
    var gtxBlocked = false;
    var dynamicDrainTimer = null;
    var dynamicCacheTimer = null;
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
        "Innioasis Universal Flash Tool", "Universal Flash Tool", "SP Flash Tool", "SP Flash",
        "MTKClient", "MediaTek", "Innioasis Y1", "Innioasis Y2", "Innioasis",
        "Innioasis Updater CE", "Innioasis Updater", "Updater Community Edition", "Updater CE",
        "Ryan Specter", "Ryan Specter and Team Slide", "Copyleft - Innioasis and Ryan Specter",
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
        "Linux", "Windows", "macOS", "Android", "iOS", "FAQ",
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

    function parseClients5List(data, count) {
        if (count === 1) {
            if (typeof data === "string" && data.trim()) return [data.trim()];
            if (Array.isArray(data) && typeof data[0] === "string") return [String(data[0]).trim()];
            if (Array.isArray(data) && Array.isArray(data[0]) && data[0][0]) return [String(data[0][0]).trim()];
        }
        if (!Array.isArray(data) || data.length !== count) return null;
        var out = [];
        if (typeof data[0] === "string") {
            for (var i = 0; i < data.length; i += 1) out.push(String(data[i] || "").trim());
            return out;
        }
        if (Array.isArray(data[0])) {
            for (var j = 0; j < data.length; j += 1) {
                var row = data[j];
                var cell = Array.isArray(row) ? row[0] : "";
                out.push(cell ? String(cell).trim() : "");
            }
            return out;
        }
        return null;
    }

    function parseGtxList(data, count) {
        var segments = data && data[0];
        if (!Array.isArray(segments) || segments.length !== count) return null;
        var out = [];
        for (var i = 0; i < segments.length; i += 1) {
            out.push(segments[i] && segments[i][0] ? String(segments[i][0]).trim() : "");
        }
        return out;
    }

    function fetchDynamicJson(url) {
        var ctrl = typeof AbortController === "function" ? new AbortController() : null;
        var timer = ctrl ? setTimeout(function () { ctrl.abort(); }, 8000) : null;
        return fetch(url, { method: "GET", mode: "cors", signal: ctrl ? ctrl.signal : undefined })
            .then(function (response) {
                if (timer) clearTimeout(timer);
                if (!response.ok) throw new Error("HTTP " + response.status);
                return response.json();
            })
            .catch(function (error) {
                if (timer) clearTimeout(timer);
                throw error;
            });
    }

    /* One request, many `q` values. A result is used only when it lines up
       with the strings that were sent, so a provider that splits sentences
       cannot write the wrong translation into the page. */
    function requestDynamicBatch(items) {
        var target = dynamicTarget();
        /* Our own endpoint caches every translated string at the edge, so a
           repeated string — from this reader's next page or from anyone else
           reading the same language — never reaches a provider again, and a
           whole batch arrives in one same-origin round trip. The public
           endpoints below stay as the fallback for a site where the function
           is not deployed. */
        function viaCache() {
            if (typeof fetch !== "function") return Promise.reject(new Error("no fetch"));
            return fetch("/i18n-translate", {
                method: "POST",
                mode: "cors",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({
                    locale: target,
                    strings: items.map(function (item) { return item.hidden; })
                })
            }).then(function (response) {
                if (!response.ok) throw new Error("HTTP " + response.status);
                return response.json();
            }).then(function (data) {
                var list = data && data.translations;
                if (!Array.isArray(list) || list.length !== items.length) throw new Error("unaligned");
                return list;
            });
        }
        return viaCache().catch(function () {
            return directBatch(items);
        });
    }

    function directBatch(items) {
        var target = dynamicTarget();
        var query = items.map(function (item) {
            return "q=" + encodeURIComponent(item.hidden);
        }).join("&");
        var clients5Url = "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl=" +
            encodeURIComponent(target) + "&" + query;
        var gtxUrl = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=auto&tl=" +
            encodeURIComponent(target) + "&dt=t&" + query;
        return fetchDynamicJson(clients5Url).then(function (data) {
            var list = parseClients5List(data, items.length);
            if (list) return list;
            throw new Error("unaligned");
        }).catch(function () {
            if (gtxBlocked) throw new Error("unavailable");
            return fetchDynamicJson(gtxUrl).then(function (data) {
                var list = parseGtxList(data, items.length);
                if (list) return list;
                var missed = new Error("unaligned");
                missed.align = true;
                throw missed;
            }).catch(function (error) {
                if (error && error.align) throw error;
                gtxBlocked = true;
                throw error;
            });
        });
    }

    function rememberDynamic(text, translated) {
        if (!translated) return;
        loadDynamicCache()[dynamicKey(text)] = translated;
        if (dynamicCacheTimer) return;
        dynamicCacheTimer = setTimeout(function () {
            dynamicCacheTimer = null;
            persistDynamicCache();
        }, 400);
    }

    function settleDynamic(item, translated) {
        var waiters = dynamicPending[item.key] || [];
        delete dynamicPending[item.key];
        waiters.forEach(function (apply) { apply(translated || null); });
    }

    function takeDynamicBatch() {
        var batch = [];
        var urlLen = 120;
        while (dynamicQueue.length && batch.length < DYNAMIC_BATCH_MAX) {
            var next = dynamicQueue[0];
            var add = encodeURIComponent(next.text).length + 3;
            if (batch.length && urlLen + add > DYNAMIC_BATCH_URL) break;
            dynamicQueue.shift();
            batch.push(next);
            urlLen += add;
            if (urlLen > DYNAMIC_BATCH_URL) break;
        }
        return batch;
    }

    function scheduleDynamicDrain() {
        if (dynamicDrainTimer || !dynamicQueue.length) return;
        dynamicDrainTimer = setTimeout(function () {
            dynamicDrainTimer = null;
            var guard = 0;
            while (dynamicInFlight < DYNAMIC_CONCURRENCY && dynamicQueue.length && guard < DYNAMIC_CONCURRENCY) {
                drainDynamic();
                guard += 1;
            }
        }, 0);
    }

    function drainDynamic() {
        if (dynamicInFlight >= DYNAMIC_CONCURRENCY || !dynamicQueue.length) {
            updateToolbarTranslatingState();
            return;
        }
        if (dynamicRequests >= DYNAMIC_MAX_REQUESTS) {
            var dropped = dynamicQueue.splice(0);
            dropped.forEach(function (item) { settleDynamic(item, ""); });
            updateToolbarTranslatingState();
            return;
        }
        var batch = takeDynamicBatch();
        var prepared = batch.map(function (item) {
            var masked = maskBrands(item.text);
            return { key: item.key, text: item.text, hidden: masked.text, found: masked.found };
        });
        dynamicInFlight += 1;
        dynamicRequests += prepared.length;
        updateToolbarTranslatingState();
        requestDynamicBatch(prepared).then(function (list) {
            prepared.forEach(function (item, index) {
                var raw = list && list[index] ? String(list[index]).trim() : "";
                var value = raw ? restoreBrands(raw, item.found) : "";
                if (value) rememberDynamic(item.text, value);
                settleDynamic(item, value);
            });
        }).catch(function (error) {
            if (error && error.align && prepared.length > 1) {
                var mid = Math.ceil(prepared.length / 2);
                var right = batch.slice(mid);
                var left = batch.slice(0, mid);
                for (var i = right.length - 1; i >= 0; i -= 1) dynamicQueue.unshift(right[i]);
                for (var j = left.length - 1; j >= 0; j -= 1) dynamicQueue.unshift(left[j]);
                return;
            }
            prepared.forEach(function (item) { settleDynamic(item, ""); });
        }).then(function () {
            dynamicInFlight -= 1;
            updateToolbarTranslatingState();
            if (dynamicQueue.length) scheduleDynamicDrain();
        });
    }

    /* ---------------------------------------------------------------- */
    /* Toolbar loading throbber for pending remote translations         */
    /* ---------------------------------------------------------------- */
    /* When dynamic translation is fetching strings remotely, a single
       loading throbber is displayed directly on the toolbar language
       picker button until all items finish translating. No intrusive
       per-element spinners are placed in the page content. */
    var toolbarTranslatingTimer = null;

    function ensureBadgeStyles() {
        if (document.getElementById("site-i18n-badge-styles")) return;
        var style = document.createElement("style");
        style.id = "site-i18n-badge-styles";
        style.textContent = [
            ".site-i18n-badge{display:inline-flex;align-items:center;gap:4px;",
            "margin-inline-start:6px;vertical-align:middle;color:currentColor;opacity:.68;",
            "font-size:.85em;line-height:1;pointer-events:none;user-select:none;}",
            "html[lang^=\"en\"] .site-i18n-badge,html:not([lang]) .site-i18n-badge,[lang^=\"en\"] .site-i18n-badge,[data-locale^=\"en\"] .site-i18n-badge{display:none!important;}",
            ".site-i18n-globe{flex:none;width:13px;height:13px;}",
            ".site-i18n-spinner{flex:none;width:10px;height:10px;border-radius:50%;",
            "border:1.5px solid currentColor;border-top-color:transparent;box-sizing:border-box;",
            "animation:site-i18n-spin .8s linear infinite;}",
            ".site-locale-throbber{display:none;width:12px;height:12px;border-radius:50%;",
            "border:1.5px solid currentColor;border-top-color:transparent;box-sizing:border-box;",
            "animation:site-locale-spin .8s linear infinite;margin-inline-start:6px;vertical-align:middle;flex:none;}",
            "[data-locale-open].is-translating .site-locale-throbber,",
            ".site-locale-toggle.is-translating .site-locale-throbber,",
            ".site-locale-dock-btn.is-translating .site-locale-throbber{display:inline-block!important;}",
            "@keyframes site-i18n-spin{to{transform:rotate(360deg);}}",
            "@keyframes site-locale-spin{to{transform:rotate(360deg);}}",
            "@media (prefers-reduced-motion:reduce){.site-i18n-spinner,.site-locale-throbber{animation:none;opacity:.6;}}"
        ].join("");
        (document.head || document.documentElement).appendChild(style);
    }

    function isTranslatingActive() {
        if (isEnglishLocale(state.locale)) return false;
        return dynamicInFlight > 0 || dynamicQueue.length > 0;
    }

    function ensureThrobber(button) {
        if (!button || button.querySelector(".site-locale-throbber")) return;
        var throbber = document.createElement("span");
        throbber.className = "site-locale-throbber";
        throbber.setAttribute("aria-hidden", "true");
        button.appendChild(throbber);
    }

    function setToolbarTranslating(active) {
        if (toolbarTranslatingTimer) {
            clearTimeout(toolbarTranslatingTimer);
            toolbarTranslatingTimer = null;
        }
        ensureBadgeStyles();
        /* The footer/dock language control is not always the header button: on
           the archive and gallery shells it is a dock button, so every trigger
           carries the same throbber while a batch is in flight. */
        var buttons = document.querySelectorAll(
            "[data-locale-open], .site-locale-toggle, .site-locale-dock-btn, [data-locale-dock]"
        );
        if (buttons.length) {
            for (var i = 0; i < buttons.length; i += 1) {
                var button = buttons[i];
                ensureThrobber(button);
                if (active) {
                    button.classList.add("is-translating");
                    button.setAttribute("aria-busy", "true");
                } else {
                    button.classList.remove("is-translating");
                    button.removeAttribute("aria-busy");
                }
            }
        }
        if (active) {
            toolbarTranslatingTimer = setTimeout(function () {
                setToolbarTranslating(false);
            }, 30000);
        }
    }

    function updateToolbarTranslatingState() {
        setToolbarTranslating(isTranslatingActive());
    }

    /* A string waiting on the batch shows a spinner beside it, so a reader can
       tell which sentence is still English because it is in flight from one the
       catalog simply has no entry for. Bounded: on a long docs page the toolbar
       throbber is the indicator, sixty spinners are enough to show the page is
       working without turning it into a fairground. */
    var DYNAMIC_MAX_SPINNERS = 60;
    var dynamicSpinners = 0;

    function addPendingSpinner(anchor) {
        if (!anchor || !anchor.parentNode) return null;
        if (dynamicSpinners >= DYNAMIC_MAX_SPINNERS) return null;
        if (typeof document.createElement !== "function") return null;
        var parent = anchor.parentNode;
        var tag = String(parent.tagName || "").toUpperCase();
        /* Never inside a control or a heading: there a spinner reads as part of
           the label, and the label is short enough to wait for. */
        if (/^(A|BUTTON|LABEL|OPTION|SUMMARY)$/.test(tag)) return null;
        var spinner = document.createElement("span");
        spinner.className = "site-i18n-spinner";
        spinner.setAttribute("aria-hidden", "true");
        spinner.setAttribute("data-i18n-pending", "1");
        try {
            parent.insertBefore(spinner, anchor.nextSibling);
        } catch (_) {
            return null;
        }
        dynamicSpinners += 1;
        return spinner;
    }

    function removePendingSpinner(spinner) {
        if (!spinner) return;
        dynamicSpinners = Math.max(0, dynamicSpinners - 1);
        try {
            if (spinner.parentNode) spinner.parentNode.removeChild(spinner);
        } catch (_) {}
    }

    function queueDynamicText(text, apply, anchor) {
        var cache = loadDynamicCache();
        var key = dynamicKey(text);
        var spinner = null;
        var waiter = function (value) {
            removePendingSpinner(spinner);
            if (value) apply(value);
        };
        /* The catalog is already in memory, so a string it covers costs no
           request at all. Without this check a docs page sent its whole body
           to the provider even for copy every catalog carries, one batch of
           thirty-two strings at a time. */
        if (state.strings) {
            var known = state.strings[text];
            if (known && known !== text) {
                apply(known);
                return;
            }
        }
        /* Already translated text (a repaint after a language switch) and
           brand-only labels are not missing sources either. */
        if (catalogHasValue(text)) return;
        if (isBrandOnly(text)) return;
        if (cache[key]) {
            waiter(cache[key]);
            return;
        }
        if (dynamicPending[key]) {
            spinner = addPendingSpinner(anchor);
            dynamicPending[key].push(waiter);
            updateToolbarTranslatingState();
            return;
        }
        if (dynamicRequests >= DYNAMIC_MAX_REQUESTS) return;
        spinner = addPendingSpinner(anchor);
        dynamicPending[key] = [waiter];
        dynamicQueue.push({ key: key, text: text });
        updateToolbarTranslatingState();
        scheduleDynamicDrain();
    }

    /* A non-English page can still be showing the English source: the catalog
       had no entry, or a script painted English after the catalog pass. Those
       leftovers go out together and come back onto the same nodes. Text that
       is already a catalog translation is left alone. */
    function queueEnglishGaps(root) {
        if (!dynamicEnabled() || !root || typeof document.createTreeWalker !== "function") return;
        var scope = root.nodeType === 1 || root.nodeType === 9 || root.nodeType === 11 ? root : null;
        if (!scope) return;
        var walker = document.createTreeWalker(scope, NodeFilter.SHOW_TEXT, {
            acceptNode: function (node) {
                var parent = node.parentElement;
                if (!parent) return NodeFilter.FILTER_REJECT;
                if (/^(SCRIPT|STYLE|PRE|CODE|KBD|SAMP|TEXTAREA|NOSCRIPT)$/.test(parent.tagName)) {
                    return NodeFilter.FILTER_REJECT;
                }
                if (parent.closest("[data-i18n-skip], [translate='no'], .theme-card, [data-locale-panel]")) {
                    return NodeFilter.FILTER_REJECT;
                }
                if (parent.closest("[hidden], [aria-hidden='true'], dialog:not([open])")) return NodeFilter.FILTER_REJECT;
                if (catalogApplied && catalogApplied.has(node)) return NodeFilter.FILTER_REJECT;
                if (dynamicSeen && dynamicSeen.has(node)) return NodeFilter.FILTER_REJECT;
                var value = normalise(node.nodeValue);
                if (value.length < 8 || !/[A-Za-z]{3}/.test(value)) return NodeFilter.FILTER_REJECT;
                if (catalogHasValue(value)) return NodeFilter.FILTER_REJECT;
                if (isBrandOnly(value)) return NodeFilter.FILTER_REJECT;
                var known = state.strings && state.strings[value];
                if (known && known !== value) return NodeFilter.FILTER_ACCEPT;
                var source = node.__y1Source == null ? "" : normalise(node.__y1Source);
                if (source && source === value) return NodeFilter.FILTER_ACCEPT;
                if (parent.closest("[data-i18n-english]")) return NodeFilter.FILTER_ACCEPT;
                if (known === value) return NodeFilter.FILTER_ACCEPT;
                return NodeFilter.FILTER_REJECT;
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
                var known = state.strings && state.strings[text];
                if (known && known !== text) {
                    target.nodeValue = prefix + known + suffix;
                    if (catalogApplied) catalogApplied.add(target);
                    return;
                }
                queueDynamicText(text, function (translated) {
                    if (!translated || normalise(translated) === text) return;
                    target.nodeValue = prefix + translated + suffix;
                }, target);
            }(node));
        }
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
                    if (parent.closest("[data-i18n-skip]") || parent.closest("[translate='no']")) return NodeFilter.FILTER_REJECT;
                    /* Theme cards are translated by themes-i18n, in viewport batches. */
                    if (parent.closest(".theme-card")) return NodeFilter.FILTER_REJECT;
                    if (parent.closest("[data-locale-panel]")) return NodeFilter.FILTER_REJECT;
                    /* Collapsed trays and closed dialogs hold fetched notices and
                       markdown that no catalog can carry. Translating them on
                       load spends hundreds of API calls on copy nobody is
                       reading yet; the observer rescans when they open. */
                    if (parent.closest("[hidden], [aria-hidden='true'], dialog:not([open])")) return NodeFilter.FILTER_REJECT;
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
                    if (catalogHasValue(value)) return NodeFilter.FILTER_REJECT;
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
                    queueDynamicText(text, function (translated) {
                        target.nodeValue = prefix + translated + suffix;
                    }, target);
                }(node));
            }
            if (!wholePage) container.setAttribute("data-i18n-dynamic-state", "done");
        });
        queueEnglishGaps(root);

        /* Attribute copy (aria-label, title, alt, placeholder) needs the same
           treatment; the catalog pass only handles what it was given. */
        if (root.querySelectorAll) {
            Array.prototype.forEach.call(
                root.querySelectorAll("[title],[alt],[placeholder],[aria-label],[aria-description]"),
                function (element) {
                    if (element.closest("[data-locale-panel]")) return;
                    if (element.closest("[data-i18n-skip]")) return;
                    if (element.closest(".site-i18n-badge")) return;
                    if (element.closest(".theme-card")) return;
                    if (dynamicAttrSeen.has(element)) return;
                    dynamicAttrSeen.add(element);
                    ATTRIBUTES.forEach(function (name) {
                        var raw = element.getAttribute(name);
                        if (!raw) return;
                        var text = normalise(raw);
                        if (text.length < 4 || !/[A-Za-z]{2}/.test(text)) return;
                        var known = state.strings[text];
                        if (known && known !== text) return;
                        if (catalogHasValue(text)) return;
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
        updateDockLabel();

        if (state.locale === DEFAULT_LOCALE && !Object.keys(state.regionCopy).length) {
            translateHead();
            /* Back to English: put the remembered source text on screen. */
            if (document.body && sourcesReady()) {
                applying = true;
                try { translateTree(document.body); } finally { applying = false; }
            }
            try {
                global.dispatchEvent(new CustomEvent("site-locale-change", { detail: { locale: state.locale } }));
                global.dispatchEvent(new CustomEvent("y1-locale-change", { detail: { locale: state.locale } }));
            } catch (_) {}
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
        try {
            global.dispatchEvent(new CustomEvent("site-locale-change", { detail: { locale: state.locale } }));
            global.dispatchEvent(new CustomEvent("y1-locale-change", { detail: { locale: state.locale } }));
        } catch (_) {}
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
                    } else if (record.type === "attributes") {
                        scheduleDynamicScan();
                    } else if (record.type === "characterData" && record.target) {
                        var value = translateValue(record.target.nodeValue);
                        if (value !== record.target.nodeValue) record.target.nodeValue = value;
                    }
                }
            } finally {
                applying = false;
            }
        });
        observer.observe(document.body, {
            childList: true,
            subtree: true,
            characterData: true,
            /* Opening a tray flips hidden/aria-hidden instead of adding nodes,
               so the scan has to hear about that to translate what appeared. */
            attributes: true,
            attributeFilter: ["hidden", "aria-hidden"]
        });
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
        english: "English (original)",
        suggested: "Suggested for you (US, UK & Europe)",
        globalRegions: "Americas & Asia-Pacific",
        allLanguagesAlpha: "All Languages (A–Z)",
        noMatches: "No matching languages found"
    };

    var SUGGESTED_CODES = [
        "en-US", "en-GB", "en",
        "de", "fr", "es", "it", "nl", "pl",
        "pt-PT", "pt", "ru", "uk", "sv", "no", "da", "fi", "cs", "el", "hu", "ro", "tr"
    ];

    var AMERICAS_APAC_CODES = [
        "es-419", "es-MX", "pt-BR",
        "ja", "ko", "zh-CN", "zh-TW", "zh-HK",
        "vi", "th", "id", "hi", "ar", "he"
    ];

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
            '<strong class="site-locale-panel-title">' + escapeHtml(t("language")) + '</strong>' +
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

    function renderItem(entry, container) {
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
    }

    function renderList(container, query) {
        var needle = normalise(query).toLowerCase();
        container.innerHTML = "";

        var allEntries = state.locales.slice();
        if (!allEntries.some(function (entry) { return entry.code === DEFAULT_LOCALE; })) {
            allEntries.unshift({ code: DEFAULT_LOCALE, name: "English", native: "English", dir: "ltr" });
        }

        var seen = {};
        var entries = [];
        for (var i = 0; i < allEntries.length; i += 1) {
            var item = allEntries[i];
            if (!seen[item.code]) {
                seen[item.code] = true;
                entries.push(item);
            }
        }

        if (needle) {
            var filtered = entries.filter(function (entry) {
                return (entry.code + " " + entry.name + " " + (entry.native || "")).toLowerCase().indexOf(needle) >= 0;
            });
            if (!filtered.length) {
                var empty = document.createElement("div");
                empty.className = "site-locale-empty";
                empty.textContent = t("noMatches");
                container.appendChild(empty);
                return;
            }
            filtered.forEach(function (entry) {
                renderItem(entry, container);
            });
            return;
        }

        var entryMap = {};
        entries.forEach(function (e) {
            entryMap[e.code.toLowerCase()] = e;
        });

        var used = {};
        var suggested = [];
        SUGGESTED_CODES.forEach(function (code) {
            var key = code.toLowerCase();
            if (entryMap[key] && !used[key]) {
                used[key] = true;
                suggested.push(entryMap[key]);
            }
        });

        var americasApac = [];
        AMERICAS_APAC_CODES.forEach(function (code) {
            var key = code.toLowerCase();
            if (entryMap[key] && !used[key]) {
                used[key] = true;
                americasApac.push(entryMap[key]);
            }
        });

        var remaining = entries.filter(function (e) {
            return !used[e.code.toLowerCase()];
        });
        remaining.sort(function (a, b) {
            return (a.name || a.code).localeCompare(b.name || b.code);
        });

        function renderSection(title, list) {
            if (!list.length) return;
            var header = document.createElement("div");
            header.className = "site-locale-section-title";
            header.textContent = title;
            container.appendChild(header);
            list.forEach(function (entry) {
                renderItem(entry, container);
            });
        }

        renderSection(t("suggested"), suggested);
        renderSection(t("globalRegions"), americasApac);
        renderSection(t("allLanguagesAlpha"), remaining);
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

    var COMMON_NATIVE_NAMES = {
        "en": "English",
        "en-gb": "English (UK)",
        "en-us": "English (US)",
        "de": "Deutsch",
        "ja": "日本語",
        "jp": "日本語",
        "es": "Español",
        "fr": "Français",
        "it": "Italiano",
        "pt": "Português",
        "pt-br": "Português (Brasil)",
        "ru": "Русский",
        "zh-cn": "简体中文",
        "zh-tw": "繁體中文",
        "zh": "简体中文",
        "ko": "한국어",
        "kr": "한국어",
        "ar": "العربية",
        "nl": "Nederlands",
        "pl": "Polski",
        "tr": "Türkçe",
        "uk": "Українська",
        "vi": "Tiếng Việt",
        "th": "ไทย",
        "id": "Bahasa Indonesia",
        "he": "עברית",
        "hi": "हिन्दी",
        "cs": "Čeština",
        "el": "Ελληνικά",
        "sv": "Svenska",
        "fa": "فارسی",
        "da": "Dansk",
        "fi": "Suomi",
        "hu": "Magyar",
        "no": "Norsk",
        "ro": "Română"
    };

    function labelFor(code) {
        var clean = normalizeTag(code);
        for (var i = 0; i < state.locales.length; i += 1) {
            if (normalizeTag(state.locales[i].code) === clean) {
                return state.locales[i].native || state.locales[i].name;
            }
        }
        if (COMMON_NATIVE_NAMES[clean]) return COMMON_NATIVE_NAMES[clean];
        var base = clean.split("-")[0];
        if (COMMON_NATIVE_NAMES[base]) return COMMON_NATIVE_NAMES[base];
        return "English";
    }

    function updateDockLabel() {
        var text = labelFor(state.locale);
        Array.prototype.forEach.call(document.querySelectorAll("[data-locale-open] .site-locale-toggle-label"), function (label) {
            label.textContent = text;
        });
        Array.prototype.forEach.call(document.querySelectorAll("[data-locale-open]"), function (button) {
            button.title = t("language");
            button.setAttribute("aria-label", t("language") + ": " + text);
        });
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
        ensureBadgeStyles();
        ensureThrobber(button);
        var label = button.querySelector(".site-locale-toggle-label");
        var text = labelFor(state.locale);
        if (label) label.textContent = text;
        button.title = t("language");
        button.setAttribute("aria-label", t("language") + ": " + text);
        button.setAttribute("aria-haspopup", "dialog");
        button.classList.add("site-locale-toggle");
        if (isTranslatingActive()) {
            button.classList.add("is-translating");
            button.setAttribute("aria-busy", "true");
        } else {
            button.classList.remove("is-translating");
            button.removeAttribute("aria-busy");
        }
    }

    function bindExistingToggle() {
        /* The footer/dock language control is not always the header button: on
           the archive and gallery shells it is a dock button, so every trigger
           carries the same throbber while a batch is in flight. */
        var buttons = document.querySelectorAll(
            "[data-locale-open], .site-locale-toggle, .site-locale-dock-btn, [data-locale-dock]"
        );
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
        if (document.querySelector("[data-locale-open]") || document.querySelector(".site-locale-toggle")) {
            return null;
        }
        var button = document.createElement("button");
        button.type = "button";
        button.className = "site-locale-toggle";
        button.setAttribute("data-locale-open", "1");
        button.innerHTML =
            '<span class="site-locale-globe" aria-hidden="true">' +
            '<svg viewBox="0 0 24 24" width="15" height="15" fill="none" stroke="currentColor" stroke-width="1.8">' +
            '<circle cx="12" cy="12" r="9"></circle><path d="M3 12h18M12 3c2.6 3 2.6 15 0 18M12 3c-2.6 3-2.6 15 0 18"></path>' +
            "</svg></span>" +
            '<span class="site-locale-toggle-label"></span>' +
            '<span class="site-locale-throbber" aria-hidden="true"></span>';
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
        if (document.querySelector(".site-locale-toggle") || document.querySelector("[data-locale-open]")) return;
        /* site-init.js injects support_toolbar.html after DOMContentLoaded.
           Wait for it instead of adding a second, floating control that the
           dock button would then duplicate. */
        var slot = document.getElementById("support-toolbar-slot");
        if (slot && slot.dataset.shellLoaded !== "1") return;
        var dock = document.getElementById("y1-dock-buttons-layer");
        if (dock) return;
        var tools = document.querySelector("#nav-root .nav-tools") || document.querySelector(".nav-tools");
        createToggle(tools);
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

    function literalPathFor(code) {
        var pathname = (global.location && global.location.pathname) || "/";
        var fileName = pathname.split("/").pop() || "index.html";
        if (!fileName || !fileName.endsWith(".html")) fileName = "index.html";
        
        var baseName = fileName.replace(/_[a-z]{2,3}(?:-[a-z0-9]{2,4})?\.html$/i, "");
        if (baseName.endsWith(".html")) baseName = baseName.slice(0, -5);
        if (!baseName) baseName = "index";

        var cleanCode = normalizeTag(code);
        if (cleanCode === DEFAULT_LOCALE) {
            return baseName + ".html";
        }
        return baseName + "_" + cleanCode + ".html";
    }

    function navigateToLiteral(targetFile, code) {
        var url = new URL(global.location.href);
        var dir = url.pathname.substring(0, url.pathname.lastIndexOf("/") + 1);
        url.pathname = dir + targetFile;
        url.searchParams.delete("lang");
        global.location.href = url.pathname + url.search + url.hash;
    }

    function getPrerenderedTarget(baseName, code) {
        if (!state.prerendered || !state.prerendered.pages || !state.prerendered.locales) return null;
        var pages = state.prerendered.pages;
        var locales = state.prerendered.locales;
        var aliases = state.prerendered.aliases || {};

        if (pages.indexOf(baseName) === -1) return null;

        var clean = normalizeTag(code);
        for (var i = 0; i < locales.length; i++) {
            if (locales[i].toLowerCase() === clean) {
                return baseName + "_" + locales[i] + ".html";
            }
        }
        for (var primary in aliases) {
            if (!Object.prototype.hasOwnProperty.call(aliases, primary)) continue;
            var list = aliases[primary] || [];
            for (var j = 0; j < list.length; j++) {
                if (list[j].toLowerCase() === clean) {
                    return baseName + "_" + primary + ".html";
                }
            }
        }
        return null;
    }

    /* A prerendered firmware_de.html is already German, so the English source
       has to be recovered from the catalog before another language can be painted. */
    function stampSources(reverse) {
        if (document.body) translateTree(document.body, reverse);
        if (document.__y1Title == null) document.__y1Title = recoverSource(document.title, reverse);
        var metas = document.querySelectorAll(
            'meta[name="description"], meta[name="keywords"], meta[property^="og:"], meta[name^="twitter:"]'
        );
        Array.prototype.forEach.call(metas, function (meta) {
            if (meta.__y1Content != null) return;
            var key = (meta.getAttribute("name") || meta.getAttribute("property") || "").toLowerCase();
            if (!META_NAMES[key]) return;
            meta.__y1Content = recoverSource(meta.getAttribute("content") || "", reverse);
        });
        if (document.documentElement) document.documentElement.setAttribute("data-i18n-sources", "1");
    }

    function sourcesReady() {
        return document.documentElement && document.documentElement.getAttribute("data-i18n-sources") === "1";
    }

    /* Leave the shareable filters in the address bar and drop a language that
       was encoded in the filename. replaceState does not reload the page. */
    function canonicaliseLocalePath() {
        if (!global.location || !global.history || !global.history.replaceState) return;
        try {
            var url = new URL(global.location.href);
            var file = url.pathname.split("/").pop() || "";
            var match = /^(.*)_([a-z]{2,3}(?:-[a-z0-9]{2,4})?)\.html$/i.exec(file);
            if (match) {
                var dir = url.pathname.slice(0, url.pathname.lastIndexOf("/") + 1);
                url.pathname = dir + (match[1] || "index") + ".html";
            }
            url.searchParams.delete("lang");
            var search = url.searchParams.toString();
            global.history.replaceState(global.history.state, document.title, url.pathname + (search ? "?" + search : "") + url.hash);
        } catch (_) {}
        if (typeof global.y1ClearPreferencesFromUrl === "function") {
            try { global.y1ClearPreferencesFromUrl(); } catch (_) {}
        }
    }

    function setLocale(code) {
        if (!code) {
            closePanel();
            return;
        }
        var map = localeIndex();
        var clean = normalizeTag(code);
        var resolved = (map[clean] && map[clean].code) || code;
        if (normalizeTag(resolved) === normalizeTag(state.locale)) {
            closePanel();
            return;
        }
        closePanel();
        writeStorage(STORAGE_LOCALE, resolved);
        setSharedCookie(STORAGE_LOCALE, resolved);
        track("site_language_change", { language_chosen: resolved });

        if (!sourcesReady()) {
            var reverse = (state.strings && baseOfLocale(state.locale) !== DEFAULT_LOCALE)
                ? catalogReverse(state.strings)
                : null;
            stampSources(reverse);
        }

        state.locale = resolved;
        var entry = map[normalizeTag(resolved)] || {};
        state.dir = entry.dir || "ltr";

        function paint(catalog) {
            state.strings = catalog;
            catalogValues = null;
            applyLanguage();
            canonicaliseLocalePath();
            if (typeof global.y1DecorateLinks === "function") {
                try { global.y1DecorateLinks(); } catch (_) {}
            }
        }

        if (baseOfLocale(resolved) === DEFAULT_LOCALE) {
            paint(null);
            return;
        }
        loadCatalog(resolved).then(function (catalog) {
            paint(catalog || {});
        }).catch(function () {
            paint(null);
        });
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
        var clean = normalizeTag(code);
        var entry = map[clean] || {};
        var specific = entry.code || code;
        var base = entry.base || (clean.indexOf("-") > 0 ? clean.split("-")[0] : code);

        function fetchOne(catName) {
            return fetchJson("i18n/catalogs/" + catName + ".json?v=" + CATALOG_VERSION, 6000)
                .catch(function () { return null; });
        }

        var isVariant = base && base.toLowerCase() !== specific.toLowerCase();
        if (isVariant) {
            return Promise.all([fetchOne(base), fetchOne(specific)])
                .then(function (results) {
                    var baseCat = results[0];
                    var specCat = results[1];
                    if (!baseCat && !specCat) return null;
                    state.dir = (specCat && specCat.dir) || (baseCat && baseCat.dir) || entry.dir || "ltr";
                    var merged = Object.assign({}, (baseCat && baseCat.strings) || {}, (specCat && specCat.strings) || {});
                    return merged;
                });
        }

        return fetchOne(specific)
            .then(function (cat) {
                if (cat) {
                    state.dir = cat.dir || entry.dir || "ltr";
                    return cat.strings || {};
                }
                if (base && base !== specific) {
                    return fetchOne(base).then(function (bcat) {
                        if (!bcat) return null;
                        state.dir = bcat.dir || entry.dir || "ltr";
                        return bcat.strings || {};
                    });
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
            fetchJson("i18n/site-locales.json?v=" + CATALOG_VERSION, 6000).catch(function () { return { locales: [] }; }),
            fetchJson("i18n/regions.json?v=" + CATALOG_VERSION, 6000).catch(function () { return null; }),
            fetchJson("i18n/prerendered.json?v=" + CATALOG_VERSION, 6000).catch(function () { return null; })
        ]).then(function (results) {
            state.locales = (results[0] && results[0].locales) || [];
            state.regions = results[1];
            state.prerendered = results[2];
            global.__y1Prerendered = results[2];
            state.copies = (results[2] && results[2].locales) || [];
            return confirmCountry();
        }).then(function () {
            state.region = resolveRegion();
            state.locale = resolveLocale();
            writeStorage(STORAGE_LOCALE, state.locale);
            setSharedCookie(STORAGE_LOCALE, state.locale);
            updateDockLabel();
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
                catalogValues = null;
                applyLanguage();
                try {
                    global.dispatchEvent(new CustomEvent("site-locale-ready", { detail: { locale: state.locale } }));
                } catch (_) {}
            }
            watch();
            if (document.body) mountToggle();
            else document.addEventListener("DOMContentLoaded", mountToggle);
            /* The dock is injected after DOMContentLoaded by site-init.js, so
               bind its language button when it lands and when the toolbar
               reports ready. */
            global.addEventListener("y1-dock-slot-ready", function () {
                mountToggle();
                bindExistingToggle();
                updateDockLabel();
                var dock = document.getElementById("support-toolbar-container");
                if (dock) queueChrome(dock);
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
            offerLanguageSwitchIfNeeded();
        }).catch(function () {
            /* A failed boot must leave an English page, never a blank one. */
            document.documentElement.setAttribute("data-locale-ready", "1");
        });
    }

    var OFFER_COPY = {
        de: { prompt: "Diese Seite ist auch auf Deutsch verfügbar.", switchBtn: "Zu Deutsch wechseln" },
        fr: { prompt: "Cette page est également disponible en français.", switchBtn: "Passer en français" },
        es: { prompt: "Esta página también está disponible en español.", switchBtn: "Cambiar a español" },
        it: { prompt: "Questa pagina è disponibile anche in italiano.", switchBtn: "Passa all'italiano" },
        ja: { prompt: "このページは日本語でもご覧いただけます。", switchBtn: "日本語に切り替える" },
        ko: { prompt: "이 페이지는 한국어로도 제공됩니다.", switchBtn: "한국어로 전환" },
        zh: { prompt: "此页面也提供中文版本。", switchBtn: "切换至中文" },
        "zh-cn": { prompt: "此页面也提供简体中文版本。", switchBtn: "切换至中文" },
        "zh-tw": { prompt: "此頁面亦提供繁體中文版本。", switchBtn: "切換至繁體中文" },
        pt: { prompt: "Esta página também está disponível em português.", switchBtn: "Mudar para português" },
        "pt-br": { prompt: "Esta página também está disponível em português.", switchBtn: "Mudar para português" },
        ru: { prompt: "Эта страница также доступна на русском языке.", switchBtn: "Переключить на русский" },
        pl: { prompt: "Ta strona jest dostępna również w języku polskim.", switchBtn: "Przełącz na polski" },
        nl: { prompt: "Deze pagina is ook beschikbaar in het Nederlands.", switchBtn: "Overschakelen naar Nederlands" },
        tr: { prompt: "Bu sayfa Türkçe olarak da mevcuttur.", switchBtn: "Türkçe'ye geç" },
        ar: { prompt: "هذه الصفحة متاحة أيضًا باللغة العربية.", switchBtn: "التبديل إلى العربية" },
        uk: { prompt: "Ця сторінка також доступна українською мовою.", switchBtn: "Перейти на українську" }
    };

    function offerLanguageSwitchIfNeeded() {
        try {
            var map = localeIndex();
            var pageLang = pathLocale() || (document.documentElement && document.documentElement.lang) || "en";
            var browserLang = matchBrowserLocale(map);
            if (!browserLang) return;
            var browserBase = baseOfLocale(browserLang);
            var pageBase = baseOfLocale(pageLang);
            if (browserBase === pageBase) return;

            var dismissed = null;
            try { dismissed = sessionStorage.getItem("innioasis-offer-dismissed"); } catch (_) {}
            if (dismissed === browserLang || dismissed === browserBase || dismissed === "all") return;

            /* If the visitor explicitly set a preference in local storage that matches this page, respect it */
            var storedPref = normalizeTag(readStorage(STORAGE_LOCALE));
            if (storedPref && baseOfLocale(storedPref) === pageBase) return;

            var copyKey = normalizeTag(browserLang);
            var copy = OFFER_COPY[copyKey] || OFFER_COPY[copyKey.split("-")[0]];
            if (!copy) {
                var langName = labelFor(browserLang) || browserLang;
                copy = {
                    prompt: "This page is available in " + langName + ".",
                    switchBtn: "Switch to " + langName
                };
            }

            if (document.getElementById("site-locale-offer")) return;
            var banner = document.createElement("div");
            banner.id = "site-locale-offer";
            banner.className = "site-locale-offer";
            banner.setAttribute("role", "status");
            banner.setAttribute("aria-live", "polite");

            var icon = document.createElement("span");
            icon.className = "site-locale-offer-icon";
            icon.innerHTML = '<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"></circle><line x1="2" y1="12" x2="22" y2="12"></line><path d="M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z"></path></svg>';

            var text = document.createElement("span");
            text.className = "site-locale-offer-text";
            text.textContent = copy.prompt;

            var actions = document.createElement("div");
            actions.className = "site-locale-offer-actions";

            var switchBtn = document.createElement("button");
            switchBtn.type = "button";
            switchBtn.className = "site-locale-offer-btn site-locale-offer-btn--switch";
            switchBtn.textContent = copy.switchBtn;
            switchBtn.addEventListener("click", function () {
                try { sessionStorage.setItem("innioasis-offer-dismissed", "all"); } catch (_) {}
                banner.classList.remove("is-visible");
                setTimeout(function () { banner.remove(); }, 300);
                setLocale(browserLang);
            });

            var dismissBtn = document.createElement("button");
            dismissBtn.type = "button";
            dismissBtn.className = "site-locale-offer-btn site-locale-offer-btn--dismiss";
            dismissBtn.setAttribute("aria-label", "Dismiss");
            dismissBtn.innerHTML = "&times;";
            dismissBtn.addEventListener("click", function () {
                try { sessionStorage.setItem("innioasis-offer-dismissed", browserLang); } catch (_) {}
                banner.classList.remove("is-visible");
                setTimeout(function () { banner.remove(); }, 300);
            });

            actions.appendChild(switchBtn);
            actions.appendChild(dismissBtn);
            banner.appendChild(icon);
            banner.appendChild(text);
            banner.appendChild(actions);

            document.body.appendChild(banner);
            requestAnimationFrame(function () {
                banner.classList.add("is-visible");
            });
        } catch (_) {}
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
        /* The footer dock is inserted after the first pass. Translate that
           subtree only, and put any strings the catalog missed into the
           same batch the rest of the page uses. */
        queueChrome: queueChrome,
        /* Translate one string that a page rendered itself (theme cards, list
           rows). Resolves to "" when the locale is English, the request is
           over the page cap, or the provider has nothing to add, so callers
           can keep their own English copy. */
        translateRemote: function (text) {
            var source = normalise(text);
            if (!source || !dynamicEnabled()) return Promise.resolve("");
            if (dynamicRequests >= DYNAMIC_MAX_REQUESTS) return Promise.resolve("");
            if (typeof Promise !== "function") return Promise.resolve("");
            return new Promise(function (resolve) {
                var settled = false;
                function finish(value) {
                    if (settled) return;
                    settled = true;
                    resolve(value || "");
                }
                var timer = setTimeout(function () { finish(""); }, 20000);
                queueDynamicText(source, function (translated) {
                    clearTimeout(timer);
                    finish(translated);
                });
            });
        },
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
