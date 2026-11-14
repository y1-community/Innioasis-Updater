/* Download figures for a firmware release.

   Every release row shows one combined number: the project's own firmware
   ZIPs plus every portable package the mirror carries for the same release.
   That single figure is what a reader sees; the breakdown is what they ask
   for next. This module turns the number into a control that opens a small
   modal listing both halves:

     - the firmware ZIPs in the original repository, and
     - the portable install packages built for each computer.

   The breakdown travels with the page. A generated list embeds it in
   data-download-stats; a row drawn at runtime hands it over through
   window.InnioasisDownloadStats.open(). When a release arrives without the
   per-platform counts (an older feed), the modal fetches the mirror's own
   release listing once and fills them in, so the numbers are never silently
   replaced by zeros.

   The control keeps working without JavaScript only as the plain figure that
   was rendered, which is why the markup starts as text and is upgraded here.
*/
(function (global) {
    "use strict";
    if (global.InnioasisDownloadStats) return;

    var doc = global.document;
    if (!doc || !global.addEventListener) return;

    var VERSION = "20261117stats6";

    /* The order a reader thinks in: the usual desktop first, the legacy
       builds after the platform they belong to. */
    var PLATFORM_ORDER = [
        "windows", "windows-arm64", "windows-legacy",
        "macos", "linux", "linux-arm64", "linux-legacy"
    ];

    var PLATFORM_LABELS = {
        windows: "Windows 10/11 portable install package",
        "windows-arm64": "Windows on ARM portable install package",
        "windows-legacy": "Windows 7-10 32-bit portable install package",
        macos: "macOS install package",
        linux: "Linux x64 portable install package",
        "linux-arm64": "Linux arm64 portable install package",
        "linux-legacy": "32-bit Linux portable install package"
    };

    /* Short names for the same packages, used when a row already names the
       platform and a long sentence would wrap badly. */
    var PLATFORM_SHORT = {
        windows: "Windows 10/11",
        "windows-arm64": "Windows on ARM",
        "windows-legacy": "Windows 7-10 32-bit",
        macos: "macOS",
        linux: "Linux x64",
        "linux-arm64": "Linux arm64",
        "linux-legacy": "32-bit Linux"
    };

    var stylesInjected = false;
    var overlay = null;
    var lastTrigger = null;
    var cache = { index: {}, releases: {} };

    function num(value) {
        var n = Number(value);
        return Number.isFinite(n) && n > 0 ? Math.round(n) : 0;
    }

    function fmt(value) {
        try { return num(value).toLocaleString("en-US"); }
        catch (_) { return String(num(value)); }
    }

    /* A release can arrive with the project's ZIP and the mirror's copy of
       that same ZIP as two rows. They are one file to the reader, so merge
       them and keep the mirror share for the explanation line. */
    function combineFirmware(list) {
        var out = [];
        var at = {};
        (list || []).forEach(function (entry) {
            if (!entry || typeof entry !== "object") return;
            var key = String(entry.name || "").toLowerCase();
            if (!key) { out.push(entry); return; }
            if (at[key] === undefined) { at[key] = out.length; out.push(entry); return; }
            var primary = out[at[key]];
            var other = entry;
            if (other.mirror && !primary.mirror) {
                if (!num(primary.mirror_downloads)) {
                    primary.downloads = num(primary.downloads) + num(other.downloads);
                    primary.mirror_downloads = num(other.downloads);
                }
                if (!primary.mirror_url && other.url) primary.mirror_url = other.url;
            } else if (!other.mirror && primary.mirror) {
                other.downloads = num(other.downloads) + num(primary.downloads);
                other.mirror_downloads = num(primary.downloads);
                if (primary.url) other.mirror_url = primary.url;
                out[at[key]] = other;
            } else {
                primary.downloads = num(primary.downloads) + num(other.downloads);
                primary.mirror_downloads = num(primary.mirror_downloads) +
                    num(other.mirror_downloads);
            }
        });
        return out;
    }

    function label(platform) {
        return PLATFORM_LABELS[platform] || String(platform || "Package");
    }

    function shortLabel(platform) {
        return PLATFORM_SHORT[platform] || label(platform);
    }

    function parse(raw) {
        if (!raw) return null;
        try {
            var data = typeof raw === "string" ? JSON.parse(raw) : raw;
            return data && typeof data === "object" ? data : null;
        } catch (_) {
            return null;
        }
    }

    /* ------------------------------------------------------------- enriching

       A mirror publishes its per-OS packages in index.json (name, platform,
       URL) and its download counts in the normal GitHub release listing. Two
       cached reads reconstruct the breakdown for a release that arrived
       without one. Failures are silent: the modal still shows everything the
       page already knew. */

    function fetchJson(url) {
        return fetch(url, { cache: "no-cache", credentials: "omit" })
            .then(function (response) {
                if (!response.ok) throw new Error("HTTP " + response.status);
                return response.json();
            });
    }

    function mirrorIndex(repo) {
        if (!repo) return Promise.resolve(null);
        if (!cache.index[repo]) {
            cache.index[repo] = fetchJson("https://raw.githubusercontent.com/" + repo + "/main/index.json")
                .catch(function () {
                    return fetchJson("https://raw.githubusercontent.com/" + repo + "/master/index.json");
                })
                .catch(function () { return null; });
        }
        return cache.index[repo];
    }

    function mirrorReleases(repo) {
        if (!repo) return Promise.resolve([]);
        var path = "feeds/" + String(repo).toLowerCase() + "/releases.json";
        if (!cache.releases[repo]) {
            cache.releases[repo] = fetchJson(path)
                .catch(function () { return fetchJson("https://innioasis.app/" + path); })
                .catch(function () { return []; })
                .then(function (list) { return Array.isArray(list) ? list : []; });
        }
        return cache.releases[repo];
    }

    /* Add the mirror's counts to portable entries that only have a name and
       URL. A release tag is matched exactly, as the packager mirrors tags
       verbatim. */
    function enrich(breakdown) {
        if (!breakdown) return Promise.resolve(breakdown);
        breakdown.portable = Array.isArray(breakdown.portable) ? breakdown.portable : [];
        breakdown.firmware = combineFirmware(
            Array.isArray(breakdown.firmware) ? breakdown.firmware : []
        );
        if (!breakdown.mirrors) return Promise.resolve(breakdown);
        var pending = breakdown.portable.filter(function (entry) {
            return entry && !entry.downloads && entry.platform;
        });
        var repos = String(breakdown.mirrors).split(/[\s,]+/).filter(Boolean);
        /* The mirror also keeps a copy of the project's own ZIP, and those
           downloads belong to the combined figure. Look the mirror up while
           that copy is still missing, even when every portable package
           already carries its count. */
        var wantsCopies = breakdown.firmware.some(function (entry) {
            return entry && entry.name && !entry.mirror && !num(entry.mirror_downloads);
        });
        if (!repos.length || (!pending.length && !wantsCopies)) {
            return Promise.resolve(breakdown);
        }

        /* Only packages built from this release's own firmware belong in its
           breakdown: a mirror also carries the other hardware revision. */
        var firmwareNames = (breakdown.firmware || []).map(function (entry) {
            return String(entry && entry.name || "").toLowerCase();
        });

        return Promise.all(repos.map(function (repo) {
            return Promise.all([mirrorIndex(repo), mirrorReleases(repo)]).then(function (both) {
                return { repo: repo, index: both[0], releases: both[1] };
            });
        })).then(function (answers) {
            var tag = String(breakdown.tag || "").toLowerCase();
            answers.forEach(function (answer) {
                var release = (answer.releases || []).find(function (entry) {
                    return String(entry && entry.tag_name || "").toLowerCase() === tag;
                });
                var counts = {};
                var copies = {};
                (release && release.assets || []).forEach(function (asset) {
                    var assetName = String(asset.name || "").toLowerCase();
                    counts[assetName] = num(asset.download_count);
                    copies[assetName] = asset;
                });
                var packages = [];
                ((answer.index && answer.index.releases) || []).forEach(function (entry) {
                    if (String(entry.tag || "").toLowerCase() !== tag) return;
                    (entry.assets || []).forEach(function (asset) {
                        if (!asset.platform) return;
                        var name = String(asset.name || "").toLowerCase();
                        if (firmwareNames.length && firmwareNames.indexOf(String(asset.source_asset || "").toLowerCase()) === -1) return;
                        packages.push({
                            platform: String(asset.platform),
                            name: name,
                            url: String(asset.url || ""),
                            size: num(asset.size),
                            downloads: counts[name] || 0
                        });
                    });
                });
                breakdown.portable.forEach(function (entry) {
                    if (!entry || !entry.platform) return;
                    var name = String(entry.name || "").toLowerCase();
                    var found = packages.find(function (pkg) { return pkg.name === name; });
                    if (found) {
                        if (!entry.downloads) entry.downloads = found.downloads;
                        if (!entry.url) entry.url = found.url;
                        if (!entry.size) entry.size = found.size;
                    }
                });
                /* A platform the page did not list yet can still be added:
                   the mirror's index is the authority on what exists. */
                packages.forEach(function (pkg) {
                    var known = breakdown.portable.some(function (entry) {
                        return String(entry && entry.name || "").toLowerCase() === pkg.name;
                    });
                    if (!known) breakdown.portable.push(pkg);
                });
                /* The mirror republishes the original ZIP beside its portable
                   packages so Updater CE can fetch one release from one place.
                   Those downloads are part of the combined figure, so the
                   dialog names the copy next to the project's own ZIP. */
                breakdown.firmware.forEach(function (entry) {
                    if (!entry || entry.mirror) return;
                    var name = String(entry.name || "").toLowerCase();
                    var copy = copies[name];
                    if (!name || !copy) return;
                    /* The feed already merged this copy (and its stats.txt
                       baseline) into the original row. Do not count it
                       again. */
                    if (!num(entry.mirror_downloads)) {
                        entry.downloads = num(entry.downloads) + num(copy.download_count);
                        entry.mirror_downloads = num(copy.download_count);
                    }
                    if (!entry.mirror_url) entry.mirror_url = String(copy.browser_download_url || "");
                });
                breakdown.firmware = combineFirmware(breakdown.firmware);
            });
            breakdown.portable.sort(function (a, b) {
                var ai = PLATFORM_ORDER.indexOf(a.platform);
                var bi = PLATFORM_ORDER.indexOf(b.platform);
                return (ai === -1 ? 99 : ai) - (bi === -1 ? 99 : bi);
            });
            /* The page's figure was built before the mirror's per-file counts
               were known. When the detail adds up to more, the total follows
               it so the modal never disagrees with its own list. */
            var counted = 0;
            (breakdown.firmware || []).forEach(function (entry) { counted += num(entry && entry.downloads); });
            breakdown.portable.forEach(function (entry) { counted += num(entry && entry.downloads); });
            if (counted > num(breakdown.total)) breakdown.total = counted;
            return breakdown;
        });
    }

    /* --------------------------------------------------------------- styling */

    function injectStyles() {
        if (stylesInjected || !doc.head) return;
        stylesInjected = true;
        var style = doc.createElement("style");
        style.id = "site-download-stats-styles";
        style.textContent = [
            ".lumen-download-stats{display:inline-flex;align-items:center;gap:.35rem;flex-wrap:wrap;margin:.15rem 0;}",
            ".lumen-download-stats__figure{border:0;background:none;padding:0;font:inherit;color:inherit;cursor:pointer;text-decoration:underline;text-decoration-style:dotted;text-underline-offset:2px;}",
            ".lumen-download-stats__figure:hover{color:var(--lumen-accent,#6b9fff);}",
            ".lumen-download-stats__figure:focus-visible,.lumen-download-stats__info:focus-visible{outline:2px solid var(--lumen-accent,#6b9fff);outline-offset:2px;border-radius:6px;}",
            ".lumen-download-stats__info{display:inline-flex;align-items:center;justify-content:center;width:18px;height:18px;padding:0;border:1px solid var(--lumen-line-strong,rgba(255,255,255,.28));border-radius:999px;background:none;color:var(--lumen-muted,#9aa3b5);font:700 11px/1 var(--lumen-body,system-ui,sans-serif);cursor:pointer;}",
            ".lumen-download-stats__info:hover{color:var(--lumen-text,#fff);border-color:currentColor;}",
            ".dl-stats-overlay{position:fixed;inset:0;z-index:2147483000;display:flex;align-items:center;justify-content:center;padding:1.1rem;background:rgba(6,8,13,.66);backdrop-filter:blur(3px);}",
            ".dl-stats-overlay[hidden]{display:none!important;}",
            ".dl-stats{box-sizing:border-box;width:min(560px,100%);max-height:min(86vh,760px);overflow:auto;padding:1.1rem 1.15rem 1rem;border:1px solid var(--lumen-line-strong,rgba(255,255,255,.2));border-radius:16px;background:var(--lumen-panel,#161a24);color:var(--lumen-text,#f4f6fb);font:400 13.5px/1.5 var(--lumen-body,system-ui,sans-serif);box-shadow:0 24px 60px rgba(0,0,0,.45);}",
            ".dl-stats__head{display:flex;align-items:flex-start;gap:.75rem;margin-bottom:.4rem;}",
            ".dl-stats__head h2{margin:0;font:700 1.05rem/1.3 var(--lumen-display,system-ui,sans-serif);flex:1;min-width:0;}",
            ".dl-stats__close{border:0;background:none;color:var(--lumen-muted,#9aa3b5);font:700 20px/1 system-ui,sans-serif;cursor:pointer;padding:0 .15rem;}",
            ".dl-stats__close:hover{color:var(--lumen-text,#fff);}",
            ".dl-stats__total{margin:0 0 .8rem;color:var(--lumen-muted,#9aa3b5);font-size:12.5px;}",
            ".dl-stats__total strong{color:var(--lumen-accent,#6b9fff);font-size:1.15rem;}",
            ".dl-stats h3{margin:.9rem 0 .35rem;font:700 .92rem/1.3 var(--lumen-display,system-ui,sans-serif);}",
            ".dl-stats__list{list-style:none;margin:0;padding:0;display:grid;gap:.3rem;}",
            ".dl-stats__row{display:flex;align-items:baseline;gap:.6rem;padding:.4rem .55rem;border:1px solid var(--lumen-line,rgba(255,255,255,.1));border-radius:9px;background:var(--lumen-panel-soft,var(--lumen-panel,#1b2030));}",
            ".dl-stats__copy{flex:1;min-width:0;}",
            ".dl-stats__name{display:block;font-weight:600;overflow-wrap:anywhere;}",
            ".dl-stats__meta{display:block;color:var(--lumen-muted,#9aa3b5);font-size:11.5px;overflow-wrap:anywhere;}",
            ".dl-stats__count{flex:0 0 auto;font-variant-numeric:tabular-nums;font-weight:700;color:var(--lumen-accent,#6b9fff);}",
            ".dl-stats__row a.dl-stats__get{flex:0 0 auto;font-size:11.5px;color:var(--lumen-accent,#6b9fff);}",
            ".dl-stats__empty{margin:.2rem 0;color:var(--lumen-muted,#9aa3b5);font-size:12px;}",
            ".dl-stats__note{margin:.85rem 0 0;color:var(--lumen-muted,#9aa3b5);font-size:11.5px;}",
            "@media (max-width:520px){.dl-stats{padding:.9rem;border-radius:14px;}.dl-stats__row{flex-wrap:wrap;}}",
            "@media (prefers-reduced-motion:reduce){.dl-stats-overlay{backdrop-filter:none;}}"
        ].join("");
        doc.head.appendChild(style);
    }

    /* ------------------------------------------------------------------- DOM */

    function el(tag, className, text) {
        var node = doc.createElement(tag);
        if (className) node.className = className;
        if (text != null) node.textContent = text;
        return node;
    }

    function totalOf(breakdown) {
        if (!breakdown) return 0;
        if (typeof breakdown.total === "number") return num(breakdown.total);
        var total = 0;
        (breakdown.firmware || []).forEach(function (entry) { total += num(entry && entry.downloads); });
        (breakdown.portable || []).forEach(function (entry) { total += num(entry && entry.downloads); });
        return total;
    }

    function section(title) {
        var wrap = doc.createDocumentFragment();
        wrap.appendChild(el("h3", null, title));
        return wrap;
    }

    function row(entry, kind) {
        var item = el("li", "dl-stats__row");
        var copy = el("div", "dl-stats__copy");
        var portable = kind === "portable";
        var name = portable ? label(entry.platform)
            : (entry.name || "firmware ZIP");
        copy.appendChild(el("span", "dl-stats__name", name));
        var meta = portable
            ? (entry.name || "portable package") + (entry.size ? " · " + size(entry.size) : "")
            : entry.mirror ? "Firmware ZIP in the portable mirror" : "Original firmware ZIP";
        if (!portable && num(entry.mirror_downloads)) {
            meta += " · includes " + fmt(entry.mirror_downloads) + " from the mirror copy";
        }
        copy.appendChild(el("span", "dl-stats__meta", meta));
        item.appendChild(copy);
        item.appendChild(el("span", "dl-stats__count", fmt(entry.downloads) + " downloads"));
        if (entry.url) {
            var link = el("a", "dl-stats__get", "Download");
            link.href = entry.url;
            link.rel = "noopener noreferrer nofollow";
            link.setAttribute("download", "");
            item.appendChild(link);
        }
        return item;
    }

    function size(bytes) {
        var n = Number(bytes) || 0;
        if (n < 1024) return n + " B";
        var kb = n / 1024;
        if (kb < 1024) return kb.toFixed(kb < 10 ? 1 : 0) + " KB";
        var mb = kb / 1024;
        if (mb < 1024) return mb.toFixed(1) + " MB";
        return (mb / 1024).toFixed(2) + " GB";
    }

    function build(breakdown) {
        var panel = el("div", "dl-stats");
        panel.setAttribute("role", "dialog");
        panel.setAttribute("aria-modal", "true");
        panel.setAttribute("aria-labelledby", "dl-stats-title");

        var head = el("div", "dl-stats__head");
        var title = el("h2", null, breakdown.title || "Download figures");
        title.id = "dl-stats-title";
        head.appendChild(title);
        var close = el("button", "dl-stats__close", "\u00d7");
        close.type = "button";
        close.setAttribute("aria-label", "Close download figures");
        head.appendChild(close);
        panel.appendChild(head);

        var total = el("p", "dl-stats__total");
        total.innerHTML = "Combined downloads: <strong>" + fmt(totalOf(breakdown)) + "</strong>";
        panel.appendChild(total);

        var firmware = breakdown.firmware || [];
        panel.appendChild(section("Firmware ZIPs"));
        if (firmware.length) {
            var fit = el("ul", "dl-stats__list");
            firmware.forEach(function (entry) { fit.appendChild(row(entry, "firmware")); });
            panel.appendChild(fit);
        } else {
            panel.appendChild(el("p", "dl-stats__empty", "No firmware ZIP is listed for this release."));
        }

        var portable = (breakdown.portable || []).slice().sort(function (a, b) {
            var ai = PLATFORM_ORDER.indexOf(a.platform);
            var bi = PLATFORM_ORDER.indexOf(b.platform);
            return (ai === -1 ? 99 : ai) - (bi === -1 ? 99 : bi);
        });
        panel.appendChild(section("Portable install packages"));
        if (portable.length) {
            var pit = el("ul", "dl-stats__list");
            portable.forEach(function (entry) { pit.appendChild(row(entry, "portable")); });
            panel.appendChild(pit);
        } else {
            panel.appendChild(el("p", "dl-stats__empty", "No portable package is published for this release."));
        }

        var note = el("p", "dl-stats__note",
            "Firmware counts combine the project's release with the mirror's copy of the same ZIP. Portable counts come from the mirror that repackages it.");
        panel.appendChild(note);

        close.addEventListener("click", hide);
        panel.addEventListener("click", function (event) {
            if (event.target === panel) event.stopPropagation();
        });
        return panel;
    }

    function onKey(event) {
        if (!overlay || overlay.hidden) return;
        if (event.key === "Escape") {
            event.preventDefault();
            hide();
            return;
        }
        if (event.key !== "Tab") return;
        var focusable = overlay.querySelectorAll("button, a[href]");
        if (!focusable.length) return;
        var first = focusable[0];
        var last = focusable[focusable.length - 1];
        if (event.shiftKey && doc.activeElement === first) {
            event.preventDefault();
            last.focus();
        } else if (!event.shiftKey && doc.activeElement === last) {
            event.preventDefault();
            first.focus();
        }
    }

    function show(breakdown, trigger) {
        if (!breakdown) return;
        injectStyles();
        lastTrigger = trigger || doc.activeElement || null;
        hide();
        overlay = el("div", "dl-stats-overlay");
        var panel = build(breakdown);
        overlay.appendChild(panel);
        overlay.addEventListener("click", function (event) {
            if (event.target === overlay) hide();
        });
        (doc.body || doc.documentElement).appendChild(overlay);
        doc.documentElement.classList.add("dl-stats-open");
        doc.addEventListener("keydown", onKey, true);
        var close = panel.querySelector(".dl-stats__close");
        if (close) close.focus();
    }

    function hide() {
        if (!overlay) return;
        doc.removeEventListener("keydown", onKey, true);
        if (overlay.parentNode) overlay.parentNode.removeChild(overlay);
        overlay = null;
        doc.documentElement.classList.remove("dl-stats-open");
        if (lastTrigger && typeof lastTrigger.focus === "function") {
            try { lastTrigger.focus(); } catch (_) {}
        }
        lastTrigger = null;
    }

    /* A download module claims a click before default navigation and asks for
       the release control that opened the breakdown. Return it after closing
       the overlay so the inline progress card starts on the page instead of
       on a link that is about to be removed with the modal. */
    function dismissForDownload() {
        if (!overlay) return null;
        var trigger = lastTrigger;
        hide();
        return trigger;
    }

    /* ---------------------------------------------------------------- wiring */

    /* The figure carries the payload; the (i) beside it opens the same modal
       without a second copy of the JSON in the page. */
    function payloadOf(trigger) {
        if (!trigger) return null;
        var own = parse(trigger.getAttribute("data-download-stats"));
        if (own) return own;
        var group = trigger.closest ? trigger.closest(".lumen-download-stats") : null;
        var carrier = group ? group.querySelector("[data-download-stats]") : null;
        return carrier ? parse(carrier.getAttribute("data-download-stats")) : null;
    }

    function openFigure(trigger) {
        var breakdown = payloadOf(trigger);
        if (!breakdown) return;
        enrich(breakdown).then(function (filled) {
            show(filled, trigger);
        });
    }

    function upgrade(trigger) {
        if (!trigger || trigger.getAttribute("data-download-stats-ready") === "1") return;
        trigger.setAttribute("data-download-stats-ready", "1");
        trigger.setAttribute("aria-haspopup", "dialog");
        if (!trigger.getAttribute("aria-label")) {
            trigger.setAttribute("aria-label", (trigger.textContent || "Download figures").trim() +
                " — open the download figures and breakdown");
        }
    }

    function boot() {
        injectStyles();
        Array.prototype.forEach.call(
            doc.querySelectorAll("[data-download-stats], .lumen-download-stats__figure, .lumen-download-stats__info"), upgrade);
        doc.addEventListener("click", function (event) {
            var trigger = event.target && event.target.closest
                ? event.target.closest("[data-download-stats], .lumen-download-stats__figure, .lumen-download-stats__info")
                : null;
            if (!trigger) return;
            event.preventDefault();
            event.stopPropagation();
            openFigure(trigger);
        }, true);
    }

    global.InnioasisDownloadStats = {
        version: VERSION,
        open: function (breakdown, trigger) { show(breakdown, trigger); },
        close: hide,
        dismissForDownload: dismissForDownload,
        rich: function (breakdown) { return enrich(breakdown); },
        label: label
    };

    if (doc.readyState === "loading") doc.addEventListener("DOMContentLoaded", boot);
    else boot();
})(typeof window !== "undefined" ? window : globalThis);
