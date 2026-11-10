/**
 * Portable packages for the archive's download links.
 *
 * A page may link at a project's own rom ZIP
 * (github.com/<owner>/<repo>/releases/download/<tag>/rom.zip) or at one of the
 * mirror's per-OS builds. On Windows and Linux (x86-64 and arm64) and on macOS
 * the y1-community mirror publishes a repackaged build of that same ZIP with
 * the matching flash tool beside it. When the mirror release exists for the
 * same tag and lists the file built for this OS and architecture, the click is
 * sent to the mirror file instead.
 *
 * Android, 32-bit x86, PowerPC and unknown systems keep the project's own
 * release, because the portable packages cannot run there. Type B packages
 * (rom_type_b.zip and its 240p/360p variants) follow exactly the same rule.
 *
 * Windows XP through 8.1 and 32-bit Windows cannot run Updater CE at all, so
 * those visits resolve a separate mirror asset instead: <rom>-windows-legacy.zip,
 * the same rom packed beside the flash-tool-only package published with Updater
 * CE releases (Innioasis-SP-Flash-Tool-windows-legacy.zip). Without that asset
 * in the mirror release, the click keeps the standard Windows build.
 *
 * The file is saved under the release's own name (rom.zip, rom_y2.zip,
 * rom_type_b.zip) rather than the mirror's OS-prefixed name. A cross-origin
 * response cannot be renamed by the download attribute, so when the
 * same-origin download proxy is available the bytes are streamed with real
 * progress and then written to Downloads under the release's name. Otherwise
 * the browser downloads the portable file directly; no page ever assembles a
 * ZIP itself.
 *
 * The custom progress path is deliberately limited to firmware-list.html;
 * firmware.html has its own equivalent in lumen-site.js. Release notes and
 * every other content page keep their direct release links untouched.
 */
(function () {
    "use strict";

    var INDEX_URL = "https://raw.githubusercontent.com/%s/%s/index.json";
    var RELEASE_TAG = "https://api.github.com/repos/%s/releases/tags/%s";
    var ASSET_RE = /^https?:\/\/github\.com\/([^/]+)\/([^/]+)\/releases\/download\/([^/]+)\/([^/?#]+)/i;
    var PLATFORM_SUFFIX = {
        macos: "-macos.zip",
        windows: "-windows.zip",
        "windows-arm64": "-windows-arm64.zip",
        "windows-legacy": "-windows-legacy.zip",
        linux: "-linux.zip",
        "linux-arm64": "-linux-arm64.zip"
    };
    var PLATFORM_LABELS = {
        macos: "macOS",
        windows: "Windows",
        "windows-arm64": "Windows on ARM",
        "windows-legacy": "Windows XP/7/8 (32/64-bit)",
        linux: "Linux",
        "linux-arm64": "Linux on ARM"
    };

    /* Deferred scripts still expose currentScript, so the manifest is always
       fetched from the site root even on pages nested two folders deep. */
    var SELF = document.currentScript && document.currentScript.src ? document.currentScript.src : "";
    var SITE_ROOT = SELF ? SELF.replace(/[^/]*$/, "") : "";

    var indexCache = {};
    var releaseCache = {};
    var manifestCache = null;
    var platformCache = null;
    var proxyCache = {};

    function parseAssetUrl(url) {
        var match = ASSET_RE.exec(String(url || ""));
        if (!match) return null;
        try {
            return {
                repo: match[1] + "/" + match[2],
                tag: decodeURIComponent(match[3]),
                name: decodeURIComponent(match[4])
            };
        } catch (_) {
            return null;
        }
    }

    function isFirmwareZip(name) {
        var value = String(name || "");
        return /\.zip$/i.test(value) && !/sources?|legal-info/i.test(value);
    }

    /* Only the two installer pages use the in-page progress UI. Every
       generated release-notes, guide and content page follows its anchor's
       direct GitHub URL instead. Supports all language variations (e.g. firmware_de.html, firmware-list_jp.html). */
    function isFirmwareDownloadPage() {
        var path = String(window.location.pathname || "").replace(/\/+$/, "");
        return /\/firmware(-list)?(_[a-zA-Z0-9_-]+)?\.html$/i.test(path) || document.querySelector("[data-firmware-page]") !== null || document.getElementById("lumen-firmware-table") !== null;
    }

    /* The mirror publishes x86-64 and arm64 builds plus one universal macOS
       package. Anything 32-bit, PowerPC or unrecognised keeps the original
       download rather than being handed a build it cannot run. Android is
       excluded: its download is the original rom zip (or the Type B build),
       because the portable package wraps a desktop flash tool. */
    function platformKey() {
        if (platformCache) return platformCache;
        /* Windows XP through 8.1 and 32-bit Windows cannot run Updater CE, so
           the flash-tool bundle is the only package that works there. The
           verdict comes from site-legacy.js, which reads the user agent once
           for the whole site; until it loads, the standard build is used. */
        var legacy = legacyKey();
        if (legacy) {
            platformCache = Promise.resolve(legacy);
            return platformCache;
        }
        platformCache = (async function () {
            var ua = navigator.userAgent || "";
            var plat = navigator.platform || "";
            var mac = /Mac/i.test(plat) || /Macintosh/i.test(ua);
            if (mac) return "macos";
            var win = /Win/i.test(plat);
            var linux = /Linux/i.test(plat) && !/Android/i.test(ua);
            if (!win && !linux) return "";

            var arch = "";
            if (navigator.userAgentData && typeof navigator.userAgentData.getHighEntropyValues === "function") {
                try {
                    var data = await navigator.userAgentData.getHighEntropyValues(["architecture", "bitness"]);
                    var reported = String((data && data.architecture) || "").toLowerCase();
                    if (reported.indexOf("arm") !== -1) arch = "arm64";
                    else if (reported.indexOf("x86") !== -1) arch = String(data.bitness) === "32" ? "x86" : "x86-64";
                } catch (_) {}
            }
            if (!arch) {
                if (/arm64|aarch64|armv8/i.test(ua)) arch = "arm64";
                else if (/i686|i386|win32|x86;/i.test(ua)) arch = "x86";
                else if (/x86_64|win64|wow64|amd64/i.test(ua)) arch = "x86-64";
            }
            if (arch === "arm64") return win ? "windows-arm64" : "linux-arm64";
            if (arch === "x86-64") return win ? "windows" : "linux";
            return "";
        })();
        return platformCache;
    }

    /* Legacy Windows (XP through 8.1, and 32-bit) is decided once for the
       whole site by site-legacy.js. Its verdict selects the flash-tool bundle,
       which is the only package that can run there. */
    function legacyKey() {
        try {
            var marker = window.INNIOASIS_LEGACY;
            return marker && marker.isLegacy ? "windows-legacy" : "";
        } catch (_) {
            return "";
        }
    }

    /* repo -> mirror repositories, straight from the manifest the app reads. */
    function mirrorMap() {
        if (!manifestCache) {
            /* The repository copy is read first and SITE_ROOT is the fallback,
               so opening a page does not count against this domain. */
            manifestCache = fetch("https://raw.githubusercontent.com/y1-community/Innioasis-Updater/main/slidia_manifest.xml", { cache: "no-cache" })
                .then(function (res) {
                    if (!res.ok) throw new Error("HTTP " + res.status);
                    return res.text();
                })
                .catch(function () {
                    return fetch(SITE_ROOT + "slidia_manifest.xml", { cache: "no-cache" })
                        .then(function (res) {
                            if (!res.ok) throw new Error("HTTP " + res.status);
                            return res.text();
                        });
                })
                .then(function (text) {
                    var doc = new DOMParser().parseFromString(text, "application/xml");
                    var map = {};
                    Array.prototype.forEach.call(doc.querySelectorAll("package"), function (pkg) {
                        var repo = String(pkg.getAttribute("repo") || "").trim().toLowerCase();
                        var mirrors = String(pkg.getAttribute("portable_zips") || "")
                            .split(/[\s,]+/)
                            .map(function (value) { return value.trim(); })
                            .filter(Boolean);
                        if (!repo || !mirrors.length) return;
                        map[repo] = (map[repo] || []).concat(mirrors.filter(function (mirror) {
                            return (map[repo] || []).indexOf(mirror) === -1;
                        }));
                    });
                    return map;
                })
                .catch(function () { return {}; });
        }
        return manifestCache;
    }

    function fetchIndex(repo) {
        if (!indexCache[repo]) {
            indexCache[repo] = (async function () {
                /* main first, then master for the older mirrors. */
                var branches = ["main", "master"];
                for (var i = 0; i < branches.length; i++) {
                    try {
                        var res = await fetch(INDEX_URL.replace("%s", repo).replace("%s", branches[i]), { cache: "no-store" });
                        if (res.ok) return await res.json();
                    } catch (_) {}
                }
                return null;
            })();
        }
        return indexCache[repo];
    }

    function fetchRelease(repo, tag) {
        var key = String(repo).toLowerCase() + "|" + String(tag).toLowerCase();
        if (!releaseCache[key]) {
            releaseCache[key] = fetch(RELEASE_TAG.replace("%s", repo).replace("%s", encodeURIComponent(tag)), {
                headers: { Accept: "application/vnd.github+json" }
            }).then(function (res) {
                if (!res.ok) return null;
                return res.json();
            }).catch(function () { return null; });
        }
        return releaseCache[key];
    }

    function suffixFor(index, key) {
        var platforms = (index && index.platforms) || [];
        var entry = platforms.find(function (candidate) {
            return candidate && String(candidate.key || "") === key;
        });
        return entry && entry.suffix ? String(entry.suffix) : (PLATFORM_SUFFIX[key] || "");
    }

    function findAsset(index, tag, sourceAsset, key) {
        if (!index || !Array.isArray(index.releases)) return null;
        var release = index.releases.find(function (candidate) {
            return candidate && String(candidate.tag || "").toLowerCase() === String(tag).toLowerCase();
        });
        if (!release || !Array.isArray(release.assets)) return null;
        var base = String(sourceAsset).replace(/\.zip$/i, "");
        var suffix = suffixFor(index, key);
        return release.assets.find(function (asset) {
            if (!asset || !asset.name) return false;
            if (String(asset.platform || "") !== key) return false;
            var declared = String(asset.source_asset || "");
            if (declared) return declared.toLowerCase() === String(sourceAsset).toLowerCase();
            return Boolean(suffix) && String(asset.name) === base + suffix;
        }) || null;
    }

    /* Confirm the candidate against the mirror's own release before the
       reader is sent there, and use the URL the API publishes so the tag and
       file name cannot drift. If api.github.com is rate-limited or blocked,
       the mirror's index.json (which carries the URL and byte size) is the
       fallback, so a usable portable package is not dropped for a 60/hour
       limit. */
    async function verifiedUrl(candidate, declaredSize) {
        var parts = parseAssetUrl(candidate);
        if (!parts) return "";
        var release = await fetchRelease(parts.repo, parts.tag);
        if (!release || !Array.isArray(release.assets)) {
            return Number(declaredSize) > 0 ? candidate : "";
        }
        var asset = release.assets.find(function (entry) {
            return entry && String(entry.name) === parts.name;
        });
        if (!asset || !asset.browser_download_url) return "";
        /* A listed asset can still be an empty placeholder while the mirror
           uploads it. An empty file is worse than the project's own release. */
        if (!(Number(asset.size) > 0)) return "";
        return asset.browser_download_url;
    }

    function parseMirrors(value) {
        return String(value || "").split(/[\s,]+/)
            .map(function (entry) { return entry.trim(); })
            .filter(function (entry) { return entry.indexOf("/") !== -1; });
    }

    /* Returns { url, platform, name } or null when this computer has no
       portable build for the release. */
    async function resolve(sourceUrl, mirrorsValue, tag, sourceName) {
        var parts = parseAssetUrl(sourceUrl);
        if (!parts) return null;
        var key = await platformKey();
        if (!key) return null;
        var repos = parseMirrors(mirrorsValue);
        if (!repos.length) {
            var map = await mirrorMap();
            repos = map[String(parts.repo).toLowerCase()] || [];
        }
        for (var i = 0; i < repos.length; i += 1) {
            var index = await fetchIndex(repos[i]);
            var asset = findAsset(index, tag || parts.tag, sourceName || parts.name, key);
            if (!asset || !asset.name) continue;
            var candidate = /^https:\/\/github\.com\//i.test(String(asset.url || ""))
                ? String(asset.url)
                : "https://github.com/" + repos[i] + "/releases/download/" +
                  encodeURIComponent(tag || parts.tag) + "/" + encodeURIComponent(asset.name);
            var url = await verifiedUrl(candidate, asset.size);
            if (url) return { url: url, platform: key, name: asset.name };
        }
        return null;
    }

    function withTimeout(promise, ms, fallback) {
        return Promise.race([
            promise,
            new Promise(function (done) { setTimeout(function () { done(fallback); }, ms); })
        ]);
    }

    function proxyUrl() {
        var meta = document.querySelector('meta[name="innioasis-download-proxy"]');
        var value = meta ? (meta.getAttribute("content") || "").trim() : "";
        if (value) return value;
        if (/^https?:$/.test(window.location.protocol)) return "/download-proxy";
        return "";
    }

    /* The reader clicked rom.zip; a mirror bundle is rom-macos.zip. Keep
       the release's own filename in Downloads on every path. */
    function releaseFileName(name, fallback) {
        var base = String(name || fallback || "rom.zip").split(/[?#]/)[0].split("/").pop();
        base = base.replace(/[-_]windows[-_]legacy(?=\.zip$)/i, "");
        base = base.replace(/[-_](?:windows[-_]legacy|windows|win|macos|mac|linux|android|darwin)(?:[-_](?:x64|amd64|x86[-_]?64|arm64|aarch64))?(?=\.zip$)/i, "");
        base = base.replace(/[-_](?:x64|amd64|x86[-_]?64|arm64|aarch64)(?=\.zip$)/i, "");
        if (!/\.zip$/i.test(base)) base = fallback || "rom.zip";
        return base;
    }

    function proxyHref(assetUrl, filename) {
        var proxy = proxyUrl();
        if (!proxy) return Promise.resolve("");
        var href = proxy + (proxy.indexOf("?") === -1 ? "?" : "&") +
            "url=" + encodeURIComponent(assetUrl) +
            "&filename=" + encodeURIComponent(filename || "firmware.zip");
        if (proxyCache[href] === undefined) {
            proxyCache[href] = fetch(href, { method: "HEAD", cache: "no-store" })
                .then(function (res) { return Boolean(res.ok); })
                .catch(function () { return false; });
        }
        return proxyCache[href].then(function (usable) { return usable ? href : ""; });
    }

    /* ----------------------------------------------------- inline progress */

    var panel = null;
    var panelTimer = null;
    var hiddenLinks = [];

    /* The tightest container holding the clicked release's zip links. */
    function releaseScope(link) {
        var row = link.closest("tr, .lumen-release-card");
        if (row) return row;
        var scope = link.closest(".lumen-actions, .lumen-release-details, .firmware-list-actions, ul, ol");
        if (scope) return scope;
        var holder = link.parentElement;
        while (holder && holder !== document.body) {
            if (holder.querySelectorAll("a[data-zip-url], a[href*='.zip']").length > 1) return holder;
            holder = holder.parentElement;
        }
        return link.parentElement || link;
    }

    function restoreLinks() {
        hiddenLinks.forEach(function (node) { node.hidden = false; });
        hiddenLinks = [];
    }

    function hideReleaseLinks(link) {
        restoreLinks();
        var scope = releaseScope(link);
        if (!scope || !scope.querySelectorAll) return;
        Array.prototype.forEach.call(scope.querySelectorAll("a[data-zip-url], a[href*='.zip']"), function (node) {
            node.hidden = true;
            hiddenLinks.push(node);
        });
    }

    function ensurePanel() {
        if (panel && panel.isConnected) return panel;
        panel = document.createElement("div");
        panel.className = "lumen-download-progress lumen-download-progress--inline";
        panel.setAttribute("role", "status");
        panel.setAttribute("aria-live", "polite");
        panel.innerHTML =
            '<div class="lumen-download-progress-row">' +
            '  <span class="lumen-download-progress-text" data-toast-label>Preparing your download…</span>' +
            '  <div class="lumen-download-progress-actions">' +
            '    <span class="lumen-download-progress-pct" data-toast-meta></span>' +
            '    <button type="button" class="lumen-download-progress-dismiss" data-toast-dismiss hidden aria-label="Dismiss">' +
            '      <svg viewBox="0 0 16 16" width="13" height="13" fill="currentColor" aria-hidden="true"><path d="M13.78 4.22a.75.75 0 0 1 0 1.06l-7.25 7.25a.75.75 0 0 1-1.06 0L2.22 9.28a.751.751 0 0 1 .018-1.042.751.751 0 0 1 1.042-.018L6 10.94l6.72-6.72a.75.75 0 0 1 1.06 0z"/></svg>' +
            '    </button>' +
            '  </div>' +
            '</div>' +
            '<div class="lumen-download-progress-bar-bg"><div class="lumen-download-progress-bar-fill" data-toast-bar style="width:2%"></div></div>';
        panel.querySelector("[data-toast-dismiss]").addEventListener("click", hideToast);
        return panel;
    }

    /* The box takes the clicked link's place. No scrollIntoView: the reader
       is already looking at the release they chose. */
    function mountPanel(link) {
        var root = ensurePanel();
        var row = link.closest ? link.closest("tr") : null;
        if (row && row.parentNode) {
            var hostRow = document.getElementById("lumen-download-progress-host");
            if (!hostRow) {
                hostRow = document.createElement("tr");
                hostRow.id = "lumen-download-progress-host";
                hostRow.className = "lumen-download-progress-host";
                var cell = document.createElement("td");
                cell.className = "lumen-download-progress-cell";
                hostRow.appendChild(cell);
            }
            var cell = hostRow.querySelector("td");
            if (cell) cell.colSpan = row.cells ? row.cells.length : 3;
            row.parentNode.insertBefore(hostRow, row.nextSibling);
            cell.appendChild(root);
            return root;
        }
        var anchor = link.closest("li") || link.closest("p") || link;
        if (!anchor.parentNode) return root;
        var holder = root.parentNode;
        if (holder && holder.classList && holder.classList.contains("lumen-download-progress-item")) holder.remove();
        if (anchor.tagName === "LI" && /^(UL|OL)$/.test(anchor.parentNode.tagName)) {
            var item = document.createElement("li");
            item.className = "lumen-download-progress-item";
            item.appendChild(root);
            anchor.parentNode.insertBefore(item, anchor.nextSibling);
        } else {
            anchor.parentNode.insertBefore(root, anchor.nextSibling);
        }
        return root;
    }

    function hideToast() {
        if (panelTimer) { clearTimeout(panelTimer); panelTimer = null; }
        if (panel && panel.isConnected) {
            var holder = panel.parentNode;
            panel.remove();
            if (holder && holder.classList && holder.classList.contains("lumen-download-progress-item")) holder.remove();
            var hostRow = document.getElementById("lumen-download-progress-host");
            if (hostRow && hostRow.parentNode && !hostRow.querySelector(".lumen-download-progress")) hostRow.parentNode.removeChild(hostRow);
        }
        restoreLinks();
    }

    function toastNodes() {
        var root = ensurePanel();
        return {
            root: root,
            label: root.querySelector("[data-toast-label]"),
            bar: root.querySelector("[data-toast-bar]"),
            meta: root.querySelector("[data-toast-meta]"),
            dismiss: root.querySelector("[data-toast-dismiss]")
        };
    }

    function toastProgress(loaded, total) {
        if (!panel || !panel.isConnected) return;
        var nodes = toastNodes();
        var pct = total > 0 ? Math.min(99, Math.round((loaded / total) * 100)) : 0;
        nodes.bar.style.width = pct + "%";
        nodes.label.textContent = "Downloading…";
        nodes.meta.textContent = total > 0
            ? pct + "% · " + (loaded / 1024 / 1024).toFixed(1) + " of " + (total / 1024 / 1024).toFixed(1) + " MB"
            : (loaded / 1024 / 1024).toFixed(1) + " MB";
    }

    function toastDone(saveName, osLabel, streamed) {
        if (!panel || !panel.isConnected) return;
        var nodes = toastNodes();
        nodes.bar.style.width = "100%";
        nodes.label.textContent = saveName || "Download finished";
        nodes.meta.textContent = streamed && saveName ? "Saved as " + saveName : "Check your Downloads folder";
        nodes.dismiss.hidden = false;
        if (panelTimer) clearTimeout(panelTimer);
        panelTimer = setTimeout(hideToast, 10000);
    }

    function startToast(link) {
        if (panelTimer) { clearTimeout(panelTimer); panelTimer = null; }
        mountPanel(link);
        hideReleaseLinks(link);
        var nodes = toastNodes();
        nodes.label.textContent = "Preparing your download…";
        nodes.bar.style.width = "2%";
        nodes.meta.textContent = "";
        nodes.dismiss.hidden = true;
    }

    function osLabel(key) {
        return PLATFORM_LABELS[key] || "";
    }

    /* The proxy already answers with Content-Disposition: filename="rom.zip",
       so pointing the browser at it streams the bundle straight to disk. Reading
       it into a Blob first would hold the whole 500-600 MB file in memory and
       only offer the save once the last byte had arrived. */
    async function streamToDownloads(href, saveName, label) {
        var link = document.createElement("a");
        link.href = href;
        link.setAttribute("data-direct-download", "1");
        if (saveName) link.download = saveName;
        link.rel = "noopener";
        document.body.appendChild(link);
        link.click();
        setTimeout(function () {
            if (link.parentNode) link.parentNode.removeChild(link);
        }, 1000);
        toastDone(saveName, label, true);
        return true;
    }

    /* Navigate a hidden frame to the asset. A scripted anchor click can be
       dropped by the browser's automatic-download guard, and such an anchor is
       also claimed by the zip click interceptor below, which sent the fallback
       back into itself. A frame navigation downloads on every path. */
    function downloadFrame() {
        var frame = document.getElementById("innioasis-download-frame");
        if (!frame) {
            frame = document.createElement("iframe");
            frame.id = "innioasis-download-frame";
            frame.setAttribute("aria-hidden", "true");
            frame.tabIndex = -1;
            frame.style.cssText = "display:none;width:0;height:0;border:0;";
            document.body.appendChild(frame);
        }
        return frame;
    }

    function directDownload(href, saveName, label) {
        var isCrossOrigin = /^https?:\/\//i.test(href) && href.indexOf(window.location.origin) !== 0;
        if (isCrossOrigin) {
            downloadFrame().src = href;
            toastDone(saveName, label, false);
            return;
        }
        var link = document.createElement("a");
        link.href = href;
        link.setAttribute("data-direct-download", "1");
        if (saveName) link.download = saveName;
        link.rel = "noopener";
        document.body.appendChild(link);
        link.click();
        setTimeout(function () {
            if (link.parentNode) link.parentNode.removeChild(link);
        }, 1000);
        toastDone(saveName, label, false);
    }

    async function downloadLink(link) {
        var href = link.getAttribute("href") || "";
        var sourceUrl = link.getAttribute("data-zip-url") || href;
        var parts = parseAssetUrl(sourceUrl);
        var displayedName = (link.textContent || "").trim();
        var linkDeclaredName = link.getAttribute("data-zip-name");
        var chosenName = linkDeclaredName || (isFirmwareZip(displayedName) ? displayedName : (parts ? parts.name : ""));
        var saveName = releaseFileName(chosenName, "rom.zip");
        var explicitPlatform = link.getAttribute("data-platform") || "";
        if (!isFirmwareZip(saveName)) return false;

        startToast(link);
        var label = osLabel(explicitPlatform);
        var target = null;
        if (explicitPlatform && explicitPlatform !== "windows-legacy" && !legacyKey() && parseAssetUrl(href)) {
            /* The reader picked a named OS build; honour that link, but save
               it under the release's own name. */
            target = { url: href, platform: explicitPlatform };
        } else {
            target = await withTimeout(
                resolve(sourceUrl, link.getAttribute("data-portable-zips") || "", link.getAttribute("data-release-tag") || "", saveName),
                9000,
                null
            );
            if (target) label = osLabel(target.platform);
        }
        if (!target) target = { url: href, platform: "" };

        var proxied = await proxyHref(target.url, saveName);
        if (proxied) {
            try {
                await streamToDownloads(proxied, saveName, label);
                return true;
            } catch (_) {
                /* Fall through to the browser's own download. */
            }
        }
        directDownload(target.url || href, saveName, label);
        return true;
    }

    document.addEventListener("click", function (event) {
        if (event.defaultPrevented || event.button !== 0) return;
        if (!isFirmwareDownloadPage()) return;
        if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
        var link = event.target && event.target.closest ? event.target.closest("a[href]") : null;
        if (!link || link.hasAttribute("data-save-as") || link.target) return;
        if (link.hasAttribute("data-direct-download")) return;

        var href = link.getAttribute("href") || "";
        var declaredSource = link.getAttribute("data-zip-url") || "";
        var declaredName = link.getAttribute("data-zip-name") || "";
        var explicitPlatform = link.getAttribute("data-platform") || "";
        var parts = parseAssetUrl(declaredSource || href);
        if (!parts) return;
        if (!isFirmwareZip(declaredName || parts.name)) return;

        event.preventDefault();
        downloadLink(link).catch(function () {
            hideToast();
            window.location.href = href;
        });
    }, false);

    /* Exposed so a page script or a test can ask the same question the click
       handler asks, without navigating. */
    window.InnioasisPortableZip = {
        resolve: resolve,
        platform: platformKey,
        download: downloadLink,
        isEnabled: isFirmwareDownloadPage
    };
})();
