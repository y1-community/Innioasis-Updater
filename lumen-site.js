(function () {
    "use strict";

    function escapeHtml(value) {
        return String(value == null ? "" : value).replace(/[&<>'"]/g, function (char) {
            return { "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[char];
        });
    }

    function zipAssets(release) {
        if (!release || !Array.isArray(release.assets)) return [];
        return release.assets.filter(function (asset) {
            return asset.name && asset.name.toLowerCase().endsWith(".zip");
        });
    }

    /* The canonical firmware packages, labelled by which model each one
       installs. Y1 Type A devices shipped with software 2.0.0 or later;
       Y1 Type B devices shipped with an earlier version. Y2 devices use
       rom_y2.zip. Release details offer these for manual download. */
    var MODEL_ZIPS = [
        { name: "rom.zip", label: "Y1 · Type A", title: "For Y1 players that shipped with software 2.0.0 or later" },
        { name: "rom_type_b.zip", label: "Y1 · Type B", title: "For Y1 players that shipped with an earlier software version" },
        { name: "rom_y2.zip", label: "Y2", title: "For Y2 players" }
    ];

    /* The packages a release may ship for an item. Y1 releases can use
       rom.zip (Type A) or rom_type_b.zip (Type B); Y2 releases use rom_y2.zip. */
    function packageNamesFor(item) {
        var names = [item.packageName.toLowerCase()];
        if (names[0] === "rom.zip") names.push("rom_type_b.zip");
        return names;
    }

    /* Releases that actually carry an item's model package. Shared repos
       hold releases for both models, so model matching happens per item. */
    function matchingReleases(releaseList, item) {
        if (!Array.isArray(releaseList) || !releaseList.length) return [];
        var names = packageNamesFor(item);
        return releaseList.filter(function (release) {
            return zipAssets(release).some(function (asset) {
                return names.indexOf(asset.name.toLowerCase()) !== -1;
            });
        });
    }

    /* A nightly build is a GitHub pre-release, or a release whose tag or
       name says so. Rockbox Y1 and Y2 ship nightly builds, so a project
       can have nightlies without any stable release. A release tagged
       "stable" is always treated as stable, matching the Updater app. */
    function isNightly(release) {
        if (!release) return false;
        var tag = (release.tag_name || "").toLowerCase();
        if (tag.indexOf("stable") !== -1) return false;
        var label = (tag + " " + (release.name || "")).toLowerCase();
        return !!release.prerelease || label.indexOf("nightly") !== -1;
    }

    /* Clean display version for a release, mirroring the Updater app's
       parse_version_designations: a YYYYMMDD-HHMM timestamp in the tag
       wins, then a v-prefixed dotted number anywhere in the tag, then a
       trailing dotted number, then the tag itself with hex commit suffixes
       removed. "launcher-v0.9" becomes "0.9"; a tag like "Solar 20260630-0550"
       is kept as its timestamp. */
    function displayVersion(tag) {
        var name = String(tag == null ? "" : tag);
        var clean = name.replace(/-[a-f0-9]{16,}!?$/, "").replace(/[-!]+$/, "");
        var extracted = null;
        var timestamp = clean.match(/(\d{8})-(\d{4})\b/);
        if (timestamp) extracted = timestamp[1] + "-" + timestamp[2];
        if (!extracted) {
            var versionPattern = clean.match(/\bv([\d.]+)\b/i);
            if (versionPattern) extracted = versionPattern[1];
        }
        if (!extracted && clean.indexOf("-") !== -1) {
            var lastPart = clean.split("-").pop();
            if (/^v/i.test(lastPart)) lastPart = lastPart.slice(1);
            if (/^[\d.]+$/.test(lastPart)) extracted = lastPart;
        }
        return extracted || clean;
    }

    /* Sortable key for a release so newer builds come first, mirroring the
       Updater app's _release_sort_key: a tag-embedded YYYYMMDD-HHMM
       timestamp sorts highest, then the semantic version tuple, then the
       GitHub published date as the tiebreaker, then the tag name. Releases
       with no usable version sort below the versioned ones. */
    function releaseSortKey(release) {
        var tag = (release && release.tag_name) || "";
        var version = displayVersion(tag);
        var tagTimestamp = 0;
        var timestampMatch = version.match(/^(\d{8})-(\d{4})$/);
        if (timestampMatch) {
            var digits = timestampMatch[1];
            var time = timestampMatch[2];
            tagTimestamp = Date.UTC(Number(digits.slice(0, 4)), Number(digits.slice(4, 6)) - 1, Number(digits.slice(6, 8)), Number(time.slice(0, 2)), Number(time.slice(2, 4)));
        }
        var semver = null;
        if (!tagTimestamp && /^\d+(\.\d+)*$/.test(version)) {
            semver = version.split(".").map(function (part) { return Number(part); });
        }
        var published = 0;
        if (release && release.published_at) {
            var parsed = Date.parse(release.published_at);
            if (!isNaN(parsed)) published = parsed;
        }
        return [tagTimestamp || semver ? 1 : 0, tagTimestamp, semver || [], published, tag.toLowerCase()];
    }

    /* Compare two releaseSortKey arrays, newest first. Elements 0-2 are
       numeric or numeric arrays, element 3 is the published date, and the
       tag name breaks any remaining tie. */
    function compareReleaseKeys(a, b) {
        for (var i = 0; i < 4; i += 1) {
            var left = a[i];
            var right = b[i];
            if (Array.isArray(left) && Array.isArray(right)) {
                var length = Math.max(left.length, right.length);
                for (var part = 0; part < length; part += 1) {
                    var leftPart = part < left.length ? left[part] : 0;
                    var rightPart = part < right.length ? right[part] : 0;
                    if (leftPart !== rightPart) return leftPart - rightPart;
                }
            } else if (left !== right) {
                return left - right;
            }
        }
        return a[4].localeCompare(b[4]);
    }

    /* GitHub access tokens from config.ini. Entries may be stored with or
       without the github_pat_ prefix; a missing prefix is re-added so the
       token is accepted by the API. The public release directory uses a
       random token per request to ride out rate limits and falls back to
       an unauthenticated request when every token has been tried. */
    var githubTokens = [];

    function loadGithubTokens() {
        return fetch("config.ini", { cache: "no-store" })
            .then(function (response) { return response.ok ? response.text() : ""; })
            .then(function (text) {
                githubTokens = (text || "").split(/\r?\n/)
                    .map(function (line) { return line.trim(); })
                    .filter(function (line) { return /^(key_\d+|token)\s*=/.test(line); })
                    .map(function (line) { return line.split("=").slice(1).join("=").trim(); })
                    .filter(function (value) { return value.length > 10; })
                    .map(function (value) {
                        return /^(github_pat_|ghp_|gho_|ghu_)/.test(value) ? value : "github_pat_" + value;
                    });
                return githubTokens;
            })
            .catch(function () { githubTokens = []; return githubTokens; });
    }

    /* One page of releases for a repo, trying a random configured token per
       attempt, then one unauthenticated request, then giving up. */
    function fetchReleasesPage(repo, page) {
        var url = "https://api.github.com/repos/" + repo + "/releases?per_page=100&page=" + page;
        var tokens = githubTokens.slice();
        for (var i = tokens.length - 1; i > 0; i -= 1) {
            var j = Math.floor(Math.random() * (i + 1));
            var tmp = tokens[i]; tokens[i] = tokens[j]; tokens[j] = tmp;
        }
        function attempt(useAuth) {
            var token = useAuth && tokens.length ? tokens.pop() : null;
            var headers = { Accept: "application/vnd.github+json" };
            if (token) headers.Authorization = "Bearer " + token;
            return fetch(url, { headers: headers })
                .then(function (response) {
                    if (response.ok) return response;
                    var retriable = response.status === 401 || response.status === 403 || response.status === 429;
                    if (retriable && useAuth) {
                        if (tokens.length) return attempt(true);
                        return attempt(false);
                    }
                    return response;
                });
        }
        return attempt(githubTokens.length > 0);
    }

    function fetchAllReleases(repo, page, collected) {
        if (page > 100) return Promise.resolve({ releases: collected, complete: false });
        return fetchReleasesPage(repo, page)
            .then(function (response) {
                if (!response.ok) return collected.length ? { releases: collected, complete: false } : null;
                return response.json().then(function (releaseList) {
                    if (!Array.isArray(releaseList)) return collected.length ? { releases: collected, complete: false } : null;
                    var all = collected.concat(releaseList);
                    var link = response.headers.get("Link") || "";
                    var hasNext = /<[^>]+>;\s*rel=["']next["']/.test(link);
                    return (hasNext || releaseList.length === 100) ? fetchAllReleases(repo, page + 1, all) : { releases: all, complete: true };
                });
            });
    }

    function initCarousel(root) {
        var slides = Array.from(root.querySelectorAll(".lumen-carousel-slide"));
        var stage = root.querySelector(".lumen-carousel-stage");
        var previous = root.querySelector("[data-carousel-previous]");
        var next = root.querySelector("[data-carousel-next]");
        var creditLink = root.querySelector("[data-carousel-credit-link]");
        var current = 0;
        if (!slides.length) return;

        function shuffle(items) {
            for (var i = items.length - 1; i > 0; i -= 1) {
                var j = Math.floor(Math.random() * (i + 1));
                var item = items[i];
                items[i] = items[j];
                items[j] = item;
            }
            return items;
        }

        function arrangeSlides() {
            if (!stage) return;
            var fixed = slides.filter(function (slide) { return slide.getAttribute("data-carousel-fixed") === "true"; })
                .sort(function (a, b) { return Number(a.getAttribute("data-carousel-order") || 99) - Number(b.getAttribute("data-carousel-order") || 99); });
            /* 50/50 opening pick: Frawgeey or Dammit Jeff leads on each visit. */
            if (fixed.length >= 2 && Math.random() < 0.5) {
                fixed = [fixed[1], fixed[0]];
            }
            var rotating = shuffle(slides.filter(function (slide) { return fixed.indexOf(slide) === -1; }));
            if (/Mac|iPhone|iPad/.test(navigator.userAgent)) {
                var macFirst = rotating.findIndex(function (slide) { return slide.getAttribute("data-video-key") === "veromarstars-rockbox-themes"; });
                if (macFirst > 0) rotating.unshift(rotating.splice(macFirst, 1)[0]);
            }
            slides = fixed.concat(rotating);
            slides.forEach(function (slide, index) {
                slide.setAttribute("aria-label", "Video " + (index + 1) + " of " + slides.length);
                slide.setAttribute("aria-roledescription", "slide");
                stage.appendChild(slide);
            });
        }

        function setSlide(index) {
            current = (index + slides.length) % slides.length;
            slides.forEach(function (slide, i) {
                var active = i === current;
                slide.setAttribute("aria-hidden", active ? "false" : "true");
                slide.inert = !active;
                slide.querySelectorAll("iframe").forEach(function (iframe) {
                    var originalSrc = iframe.getAttribute("data-carousel-src") || iframe.getAttribute("src");
                    if (originalSrc) iframe.setAttribute("data-carousel-src", originalSrc);
                    if (active) {
                        if (originalSrc && iframe.getAttribute("src") === "about:blank") iframe.setAttribute("src", originalSrc);
                    } else if (iframe.getAttribute("src") !== "about:blank") {
                        iframe.setAttribute("src", "about:blank");
                    }
                });
                slide.querySelectorAll("a, button, details, iframe").forEach(function (control) {
                    control.tabIndex = active ? 0 : -1;
                });
            });
            var activeSlide = slides[current];
            if (creditLink) {
                var creditName = activeSlide.getAttribute("data-credit");
                var creditUrl = activeSlide.getAttribute("data-video-url");
                if (creditName) creditLink.textContent = creditName;
                if (creditUrl) creditLink.setAttribute("href", creditUrl);
            }
        }

        if (previous) previous.addEventListener("click", function () { setSlide(current - 1); });
        if (next) next.addEventListener("click", function () { setSlide(current + 1); });
        root.addEventListener("keydown", function (event) {
            if (event.key === "ArrowLeft") { event.preventDefault(); setSlide(current - 1); }
            if (event.key === "ArrowRight") { event.preventDefault(); setSlide(current + 1); }
        });
        arrangeSlides();
        setSlide(0);
    }

    var LUMEN_DONATE_METHODS = [
        { name: "Ko-fi", href: "https://ko-fi.com/teamslide" },
        { name: "PayPal", href: "https://paypal.me/respectyarn" },
        { name: "Patreon", href: "https://www.patreon.com/teamslide" }
    ];

    function showDialog(dialog) {
        try { dialog.showModal(); } catch (_) { dialog.setAttribute("open", ""); }
    }

    function closeDialog(dialog) {
        try { dialog.close(); } catch (_) { dialog.removeAttribute("open"); }
    }

    function openDonateDialog() {
        var existing = document.getElementById("lumen-donate-dialog");
        if (existing) { showDialog(existing); return; }
        var dialog = document.createElement("dialog");
        dialog.id = "lumen-donate-dialog";
        dialog.className = "lumen-donate-dialog";
        dialog.setAttribute("aria-labelledby", "lumen-donate-title");
        dialog.setAttribute("aria-describedby", "lumen-donate-intro");
        dialog.innerHTML =
            '<div class="lumen-donate-card">' +
            '<p class="lumen-kicker">Support Updater and the Themes Gallery</p>' +
            '<h2 id="lumen-donate-title">It takes you.</h2>' +
            '<p class="lumen-donate-intro" id="lumen-donate-intro"><strong>Updater and the Themes Gallery are community hobbyist projects.</strong> Hosting, domain renewals, moderation, and release work have real costs. If this guide helped, a small donation keeps the tools available.</p>' +
            '<div class="lumen-donate-links">' +
            LUMEN_DONATE_METHODS.map(function (method) {
                return '<a class="lumen-donate-method" href="' + escapeHtml(method.href) + '" target="_blank" rel="noopener noreferrer">' + escapeHtml(method.name) + '</a>';
            }).join("") +
            '</div>' +
            '<button class="lumen-donate-close" type="button" data-donate-close>Maybe later</button>' +
            '</div>';
        dialog.querySelector("[data-donate-close]").addEventListener("click", function () { closeDialog(dialog); });
        document.body.appendChild(dialog);
        showDialog(dialog);
    }

    function initFeedback(root) {
        var key = "innioasis-feedback-" + (root.getAttribute("data-feedback") || location.pathname);
        var support = root.querySelector("[data-feedback-support]");
        root.querySelectorAll("button[data-feedback-value]").forEach(function (button) {
            button.addEventListener("click", function () {
                var value = button.getAttribute("data-feedback-value");
                /* Only persist the answer when the visitor has allowed it;
                   otherwise the choice lives for the rest of the visit only. */
                if (!window.INNIOASIS_PRIVACY || window.INNIOASIS_PRIVACY.allows("feedback")) {
                    try { localStorage.setItem(key, value); } catch (_) {}
                }
                root.querySelectorAll("button[data-feedback-value]").forEach(function (other) {
                    other.setAttribute("aria-pressed", other === button ? "true" : "false");
                });
                if (value === "yes") {
                    openDonateDialog();
                }
                if (support) support.hidden = value !== "no";
            });
        });
    }

    function detectPlatform() {
        var ua = navigator.userAgent || "";
        var platform = (navigator.userAgentData && navigator.userAgentData.platform) || ua;
        var p = (platform + " " + ua).toLowerCase();
        if (p.indexOf("win") !== -1) return "windows";
        if (p.indexOf("mac") !== -1 || p.indexOf("iphone") !== -1 || p.indexOf("ipad") !== -1 || p.indexOf("ipod") !== -1) return "macos";
        if (p.indexOf("linux") !== -1 || p.indexOf("x11") !== -1 || p.indexOf("android") !== -1) return "linux";
        return null;
    }

    function initPlatformReveal() {
        document.querySelectorAll("[data-platform-detect]").forEach(function (options) {
            var detected = detectPlatform();
            var cards = Array.prototype.slice.call(options.querySelectorAll("[data-platform]"));
            if (!detected || cards.length < 2) return;
            var chosen = cards.filter(function (card) { return card.getAttribute("data-platform") === detected; })[0];
            if (!chosen) return;
            /* Move the detected platform's card to the front and hide the rest,
               keeping them in the document so anchors like #macos still work. */
            options.insertBefore(chosen, options.firstChild);
            options.classList.add("lumen-download-options--single");
            cards.forEach(function (card) { if (card !== chosen) card.hidden = true; });
            var toggle = options.querySelector("[data-another-platform]");
            if (toggle) {
                toggle.hidden = false;
                toggle.addEventListener("click", function () {
                    cards.forEach(function (card) { card.hidden = false; });
                    options.classList.remove("lumen-download-options--single");
                    toggle.hidden = true;
                });
            }
        });
    }

    function copyTextFallback(text) {
        var area = document.createElement("textarea");
        area.value = text;
        area.setAttribute("readonly", "");
        area.style.position = "absolute";
        area.style.left = "-9999px";
        document.body.appendChild(area);
        area.select();
        try { document.execCommand("copy"); } catch (_) {}
        document.body.removeChild(area);
    }

    /* Download links with data-download-confirm swap their label for the
       confirm phrase once the browser starts the download (e.g. the Windows
       installer button reads "Download started"). The label is translated
       for the Night City theme when that theme is active. */
    function initDownloadConfirm() {
        document.querySelectorAll("[data-download-confirm]").forEach(function (link) {
            link.addEventListener("click", function () {
                var label = link.getAttribute("data-download-confirm");
                if (window.INNIOASIS_I18N && window.INNIOASIS_I18N.isActive && window.INNIOASIS_I18N.isActive()) {
                    label = window.INNIOASIS_I18N.translate(label);
                }
                link.textContent = label;
            });
        });
    }

    function initCopyButtons() {
        document.querySelectorAll("[data-copy-target]").forEach(function (button) {
            button.addEventListener("click", function () {
                var target = document.getElementById(button.getAttribute("data-copy-target"));
                if (!target) return;
                var text = target.textContent;
                function confirm() {
                    var original = button.textContent;
                    button.textContent = "Copied!";
                    button.classList.add("is-copied");
                    setTimeout(function () {
                        button.textContent = original;
                        button.classList.remove("is-copied");
                    }, 1600);
                }
                if (navigator.clipboard && navigator.clipboard.writeText) {
                    navigator.clipboard.writeText(text).then(confirm, function () { copyTextFallback(text); confirm(); });
                } else {
                    copyTextFallback(text);
                    confirm();
                }
            });
        });
    }

    function initFirmwareDirectory() {
        var table = document.getElementById("lumen-firmware-table");
        if (!table || !Array.isArray(window.INNIOASIS_FIRMWARE_CATALOG)) return;
        var model = document.getElementById("lumen-model-filter");
        var software = document.getElementById("lumen-software-filter");
        var status = document.getElementById("lumen-release-status");
        var y2Switch = document.querySelector("[data-y2-switch]");
        var filterSection = document.getElementById("firmware-filters");
        var catalog = window.INNIOASIS_FIRMWARE_CATALOG;
        var releases = {};
        var releaseState = {};
        var fetchedRepos = {};
        /* URL filters: ?model=Y1|Y2 and ?software=slug preselect the dropdowns,
           so a link can point straight at one model's release list. The legacy
           #y1 / #y2 hash anchors still work for older links. */
        var searchParams = new URLSearchParams(window.location.search);
        var modelParam = (searchParams.get("model") || "").toUpperCase();
        /* Nightly / pre-release filter, mirroring the Updater app's
           "Show nightly builds" checkbox. Off by default: stable releases
           only. Tick it to see preview, nightly, and RC builds. The URL
           ?nightly=1 param wins so filtered views stay shareable; without
           it we reuse the same preference as the home page table. */
        var nightly = document.getElementById("lumen-nightly-filter");
        var storedNightly = false;
        if (!window.INNIOASIS_PRIVACY || window.INNIOASIS_PRIVACY.allows("nightly")) {
            try { storedNightly = localStorage.getItem("innioasis-show-nightly") === "1"; } catch (_) {}
        }
        var showNightly = (searchParams.get("nightly") || "") === "1" ? true : storedNightly;
        if (nightly) {
            nightly.checked = showNightly;
            nightly.addEventListener("change", function () {
                showNightly = nightly.checked;
                if (!window.INNIOASIS_PRIVACY || window.INNIOASIS_PRIVACY.allows("nightly")) {
                    try { localStorage.setItem("innioasis-show-nightly", showNightly ? "1" : "0"); } catch (_) {}
                }
                render();
                syncUrl();
            });
        }
        var hashModel = (window.location.hash || "").slice(1).toUpperCase();
        var wantedModel = (modelParam === "Y1" || modelParam === "Y2") ? modelParam : ((hashModel === "Y1" || hashModel === "Y2") ? hashModel : "");
        if (model && wantedModel) {
            model.value = wantedModel;
            if (filterSection) window.setTimeout(function () { filterSection.scrollIntoView({ block: "start" }); }, 0);
        }
        /* ?software=slug preselects a project; the slug embeds the model (original-y1, rockbox-y2). */
        var softwareParam = (searchParams.get("software") || "").toLowerCase();
        if (softwareParam && model) {
            var paramItem = catalog.find(function (item) { return item.slug === softwareParam; });
            if (paramItem) {
                if (!wantedModel) model.value = paramItem.model;
                if (filterSection && !wantedModel) window.setTimeout(function () { filterSection.scrollIntoView({ block: "start" }); }, 0);
            }
        }
        /* Original Software is the default software filter for the page. */
        function originalSlug() {
            return (model && model.value === "Y2") ? "original-y2" : "original-y1";
        }
        if (y2Switch) {
            y2Switch.addEventListener("click", function (event) {
                event.preventDefault();
                if (model) {
                    model.value = "Y2";
                    fillSoftwareFilter();
                    render();
                    refreshLive();
                    if (filterSection) filterSection.scrollIntoView({ block: "start" });
                }
            });
        }

        function matchingItems() {
            var selectedModel = model ? model.value : "Y1";
            var selectedSoftware = software ? software.value : "all";
            return catalog.filter(function (item) {
                return item.model === selectedModel &&
                    (selectedSoftware === "all" || item.slug === selectedSoftware);
            });
        }

        function activeRepos() {
            var selectedModel = model ? model.value : "Y1";
            return Array.from(new Set(catalog.filter(function (item) { return item.model === selectedModel; }).map(function (item) { return item.repo; })));
        }

        /* A release belongs to an item only when it actually carries that
           model's package. Shared repos (stock, Solar, JJ Launcher) hold
           releases for both models, so a Y2-only release must not appear
           under the Y1 row or the other way round. Returns null when the
           repo has releases but none fit the selected model. */
        function releasesForItem(item) {
            var repoReleases = releases[item.repo];
            if (!Array.isArray(repoReleases) || !repoReleases.length) return null;
            var matching = matchingReleases(repoReleases, item);
            return matching.length ? matching : null;
        }

        /* Apply the nightly filter on top of the model-matched releases.
           Unchecked: stable releases only. Checked: every release, with
           stable builds still included alongside previews. Returns null
           when releases exist but the current filter hides them all. */
        function visibleReleases(item) {
            var all = releasesForItem(item);
            if (!all) return null;
            if (!showNightly) all = all.filter(function (release) { return !isNightly(release); });
            if (!all.length) return null;
            /* Newest version first: timestamp/semver order with the published
               date as tiebreaker, mirroring the Updater app. GitHub's own
               order is creation-based, which scrambles same-day releases. */
            all = all.slice().sort(function (a, b) {
                return compareReleaseKeys(releaseSortKey(b), releaseSortKey(a));
            });
            return all;
        }

        /* Release details list only the zips that belong to the selected
           item's model, so a combined release never offers a rom_y2.zip
           under the Y1 row or a rom.zip under the Y2 row. */
        function releaseDetails(release, item) {
            if (!release) return '';
            var names = packageNamesFor(item);
            var assets = zipAssets(release);
            var links = [];
            MODEL_ZIPS.forEach(function (entry) {
                if (names.indexOf(entry.name) === -1) return;
                var asset = assets.find(function (candidate) { return candidate.name.toLowerCase() === entry.name; });
                if (asset) {
                    links.push('<li><a class="lumen-download-link" href="' + escapeHtml(asset.browser_download_url) + '" download title="' + entry.title + '">' + escapeHtml(asset.name) + ' <span class="lumen-meta">' + entry.label + '</span></a></li>');
                }
            });
            var assetLinks = links.length ? links.join("") : '<li>No ZIP asset was found in this release.</li>';
            return '<details class="lumen-release-details"><summary>Release details and zip</summary><p><strong>' + escapeHtml(release.name || release.tag_name || "Public release") + '</strong>' + (release.published_at ? ' · ' + escapeHtml(release.published_at.slice(0, 10)) : '') + '</p><ul>' + assetLinks + '</ul></details>';
        }

        function releaseRows(release, item, state) {
            /* The Release column label. When the feed is unavailable the
               Software name stands in, bold, so the row still names the
               project the user is looking at instead of an error string. */
            var versionText = release ? displayVersion(release.tag_name || release.name || "Public release")
                : state === "failed" ? item.name
                : state === "empty" ? "No public releases"
                : state === "nomatch" ? "No release with " + item.packageName
                : state === "filtered-stable" ? "No stable release yet"
                : "Checking public releases";
            var versionHtml = (state === "failed" && !release) ? "<strong>" + escapeHtml(versionText) + "</strong>" : escapeHtml(versionText);
            var hint = release ? '' : state === "filtered-stable" ? '<span class="lumen-muted-inline">Tick the nightly-builds option to see previews</span>' : '';
            var guideUrl = 'guide.html?model=' + encodeURIComponent(item.model) + '&software=' + encodeURIComponent(item.slug);
            var updater = '<a class="lumen-updater-button lumen-updater-button--table" href="' + guideUrl + '" aria-label="Get ' + escapeHtml(item.name) + ' for ' + escapeHtml(item.model) + ' on Innioasis Updater"><img src="mtkclient/gui/images/icon.png" width="28" height="28" alt=""><span><strong>Get it on Updater</strong><small>with guided install</small></span></a>';
            /* The Software name is not shown here: the software filter above
               already sets the project, so every row belongs to it. */
            /* The GitHub link goes straight to this release's own page when
               a release is shown; loading and empty-state rows fall back to
               the project's release list. */
            var githubUrl = release && release.tag_name
                ? 'https://github.com/' + item.repo + '/releases/tag/' + encodeURIComponent(release.tag_name)
                : 'https://github.com/' + item.repo + '/releases';
            return '<tr>' +
                '<td>' + versionHtml + (release && release.published_at ? '<br><span class="lumen-meta">' + escapeHtml(release.published_at.slice(0, 10)) + '</span>' : '') + '</td>' +
                /* The package is not shown: the Release details expander lists
                   the rom zips this release is packaged in. */
                '<td><div class="lumen-actions">' + updater + hint + '</div>' + releaseDetails(release, item) + '</td>' +
                '<td><a class="lumen-github-link" href="' + githubUrl + '" target="_blank" rel="noopener noreferrer" aria-label="Open ' + escapeHtml(release && release.tag_name ? release.tag_name : item.name) + ' on GitHub"><svg viewBox="0 0 16 16" width="20" height="20" fill="currentColor" aria-hidden="true"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27s1.36.09 2 .27c1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.01 8.01 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg></a></td>' +
                '</tr>';
        }

        function render() {
            var items = matchingItems();
            if (!items.length) {
                table.innerHTML = '<tr><td colspan="3">No firmware project is currently listed for this model and filter. Try another project or check the project release pages.</td></tr>';
                return;
            }
            var rows = [];
            items.forEach(function (item) {
                var itemReleases = visibleReleases(item);
                var modelReleases = releasesForItem(item);
                if (itemReleases) {
                    itemReleases.forEach(function (release) { rows.push(releaseRows(release, item, "loaded")); });
                } else if (modelReleases) {
                    /* The repo has model-matched releases, but the stable
                       filter hides them all: no stable build exists yet.
                       In nightly mode every release is shown, so this
                       state can only happen when the filter is off. */
                    rows.push(releaseRows(null, item, "filtered-stable"));
                } else {
                    var repoReleases = releases[item.repo];
                    var repoLoaded = Array.isArray(repoReleases) && repoReleases.length > 0;
                    rows.push(releaseRows(null, item, repoLoaded ? "nomatch" : (releaseState[item.repo] || "loading")));
                }
            });
            table.innerHTML = rows.join("");
        }

        function fillSoftwareFilter() {
            if (!software) return;
            var previous = software.value;
            var items = catalog.filter(function (item) { return !model || item.model === model.value; });
            var options = Array.from(new Map(items.map(function (item) { return [item.slug, item.name]; })).entries()).sort(function (a, b) { return a[1].localeCompare(b[1]); });
            software.innerHTML = '<option value="all">All Software</option>' + options.map(function (entry) { return '<option value="' + escapeHtml(entry[0]) + '">' + escapeHtml(entry[1]) + '</option>'; }).join("");
            var requested = softwareParam && options.some(function (entry) { return entry[0] === softwareParam; }) ? softwareParam : previous;
            software.value = options.some(function (entry) { return entry[0] === requested; }) ? requested : originalSlug();
            if (y2Switch) {
                var selectedModel = model ? model.value : "Y1";
                if (selectedModel === "Y2") {
                    y2Switch.setAttribute("aria-hidden", "true");
                    y2Switch.setAttribute("tabindex", "-1");
                    y2Switch.textContent = "Y2";
                } else {
                    y2Switch.removeAttribute("aria-hidden");
                    y2Switch.removeAttribute("tabindex");
                    y2Switch.textContent = "Y2 ready";
                }
            }
        }


        function refreshLive() {
            var repos = activeRepos();
            var selectedModel = model ? model.value : "Y1";
            var pending = repos.filter(function (repo) { return !fetchedRepos[repo]; });
            if (status) status.textContent = pending.length ? "Loading public release information for " + selectedModel + "…" : "Loading public release information…";
            if (table) table.setAttribute("aria-busy", "true");
            pending.forEach(function (repo) { releaseState[repo] = "loading"; });
            Promise.all(pending.map(function (repo) {
                return fetchAllReleases(repo, 1, [])
                    .then(function (result) {
                        fetchedRepos[repo] = true;
                        if (result && Array.isArray(result.releases)) {
                            releases[repo] = result.releases;
                            releaseState[repo] = result.releases.length ? (result.complete ? "loaded" : "partial") : "empty";
                        } else {
                            releaseState[repo] = "failed";
                        }
                    })
                    .catch(function () { fetchedRepos[repo] = true; releaseState[repo] = "failed"; });
            })).then(function () {
                render();
                if (table) table.setAttribute("aria-busy", "false");
                var loaded = repos.filter(function (repo) { return releaseState[repo] === "loaded" || releaseState[repo] === "partial"; }).length;
                var failed = repos.filter(function (repo) { return releaseState[repo] === "failed"; }).length;
                var partial = repos.filter(function (repo) { return releaseState[repo] === "partial"; }).length;
                if (status) status.textContent = loaded ? ((failed || partial) ? "Release information for " + selectedModel + " loaded where available; some project histories may be incomplete." : "All public " + selectedModel + " releases are shown.") : "Release information is not available right now. The project links remain available.";
            });
        }

        /* Keep the address bar shareable: mirror the chosen filters back
           into the URL whenever the user changes them. */
        function syncUrl() {
            if (!model) return;
            var params = new URLSearchParams(window.location.search);
            if (model.value === "Y1" || model.value === "Y2") params.set("model", model.value);
            else params.delete("model");
            if (software && software.value && software.value !== "all") params.set("software", software.value);
            else params.delete("software");
            if (showNightly) params.set("nightly", "1");
            else params.delete("nightly");
            var qs = params.toString();
            try { history.replaceState(null, "", "?" + qs + window.location.hash); } catch (_) {}
        }

        if (model) model.addEventListener("change", function () { fillSoftwareFilter(); render(); refreshLive(); syncUrl(); });
        if (software) software.addEventListener("change", function () { render(); syncUrl(); });
        fillSoftwareFilter();
        render();
        refreshLive();
    }

    /* Compact "what can I install" table for the homepage. One row per
       Software, with a button per model that opens the matching release
       list in the full directory. Names come straight from the catalog
       (the Updater catalogue), so no release feeds are fetched here. */
    function initHomeFirmware() {
        var body = document.getElementById("lumen-home-firmware-table");
        if (!body || !Array.isArray(window.INNIOASIS_FIRMWARE_CATALOG)) return;
        var catalog = window.INNIOASIS_FIRMWARE_CATALOG;
        var groups = [];
        var seen = {};
        catalog.forEach(function (item) {
            if (!seen[item.name]) {
                seen[item.name] = { name: item.name, items: [] };
                groups.push(seen[item.name]);
            }
            seen[item.name].items.push(item);
        });
        if (!groups.length) {
            body.innerHTML = '<tr><td colspan="2">No software is currently listed for the Y1 or Y2. Check back soon.</td></tr>';
            return;
        }
        body.innerHTML = groups.map(function (group) {
            var first = group.items[0];
            /* One button per model; each opens the model-matched release
               list in the full firmware directory. */
            var releaseButtons = group.items.map(function (item) {
                return '<a class="lumen-button lumen-button--model" href="firmware.html?model=' + encodeURIComponent(item.model) + '&software=' + encodeURIComponent(item.slug) + '" aria-label="' + escapeHtml(item.model) + ' releases">' + escapeHtml(item.model) + '</a>';
            }).join(" ");
            return "<tr>" +
                '<td><a class="lumen-project-link" href="' + escapeHtml(first.seoPage || first.guide) + '"><strong>' + escapeHtml(group.name) + "</strong></a></td>" +
                "<td>" + releaseButtons + "</td>" +
                "</tr>";
        }).join("");
    }

    function initPersonalisedGuide() {
        var section = document.getElementById("personalised-steps");
        if (!section) return;
        var params = new URLSearchParams(window.location.search);
        var model = (params.get("model") || "").toUpperCase();
        var slug = params.get("software") || "";
        if (!model || !slug) return;
        var item = null;
        if (Array.isArray(window.INNIOASIS_FIRMWARE_CATALOG)) {
            item = window.INNIOASIS_FIRMWARE_CATALOG.find(function (entry) { return entry.model === model && entry.slug === slug; }) || null;
        }
        if (!item) return;
        var restoring = /original/.test(item.slug);
        var name = item.name;
        var heading = restoring ? "Restore Original Software on your " + model : "Install " + name + " on your " + model;
        var kicker = section.querySelector("[data-personalised-kicker]");
        if (kicker) kicker.textContent = restoring ? "Restore · " + model : name + " · " + model;
        var headingEl = section.querySelector("[data-personalised-heading]");
        if (headingEl) headingEl.textContent = heading;
        var lead = section.querySelector("[data-personalised-lead]");
        if (lead) lead.textContent = restoring
            ? "Follow these steps in Updater. The player you want to restore is the " + model + "."
            : "Follow these steps in Updater. You have the " + model + " and want " + name + " on it.";
        var steps = [
            "Open Updater on your computer, or install it first with the button below.",
            "In Device Model, select " + model + ".",
            restoring ? "In Software, select Original Software." : "In Software, select " + name + ".",
            "Select a stable release shown for the " + model + ".",
            "Click Install / Restore, then power off the player.",
            "Connect the player only when Updater says it is ready.",
            "Wait for the success message, then disconnect and start the player."
        ];
        var list = section.querySelector("[data-personalised-steps]");
        if (list) {
            list.innerHTML = "";
            steps.forEach(function (text) {
                var li = document.createElement("li");
                li.textContent = text;
                list.appendChild(li);
            });
        }
        var note = section.querySelector("[data-personalised-note]");
        if (note) note.textContent = restoring
            ? "That puts the " + model + " back on its original software. The download and computer setup sections below still apply if you need them."
            : "That is the whole " + name + " install on the " + model + ". The download and computer setup sections below still apply if you need them.";
        /* The generic firmware guide page fills its copy with the project
           name and model from the URL, so any listed firmware gets a
           readable tutorial even without a dedicated page. */
        document.querySelectorAll("[data-personalised-software]").forEach(function (el) { el.textContent = name; });
        document.querySelectorAll("[data-personalised-model]").forEach(function (el) { el.textContent = model; });
        var missing = document.querySelector("[data-personalised-missing]");
        if (missing) missing.hidden = true;
        document.querySelectorAll("[data-personalised-reveal]").forEach(function (el) { el.hidden = false; });
        var guideLink = section.querySelector("[data-personalised-guide]");
        var dedicatedGuide = item.guide || item.seoPage || "";
        if (guideLink) {
            if (dedicatedGuide) {
                guideLink.href = dedicatedGuide;
                guideLink.textContent = restoring ? "Open the full " + model + " restore tutorial" : "Open the full " + name + " " + model + " tutorial";
            } else {
                /* No dedicated page yet: this URL-driven page is the guide. */
                guideLink.hidden = true;
            }
        }
        var headerKicker = document.querySelector("#main > header .lumen-kicker");
        if (headerKicker) headerKicker.textContent = (restoring ? "Restore " : "Install ") + name + " on " + model + " · beginner route";
        var h1 = document.querySelector("#main > header h1");
        if (h1) h1.textContent = heading + ".";
        document.title = heading + " | Innioasis Updater";
        section.hidden = false;
        if (!window.location.hash) {
            window.setTimeout(function () { section.scrollIntoView({ block: "start" }); }, 0);
        }
    }

    /* The "Software guides by model" cards, built from the catalog so any
       firmware in the Updater manifest gets a button. Projects with a
       dedicated guide link to it; everything else falls back to the generic
       URL-driven guide page (firmware-guide.html?model=…&software=…). */
    function initSoftwareGuideLinks() {
        if (!Array.isArray(window.INNIOASIS_FIRMWARE_CATALOG)) return;
        var catalog = window.INNIOASIS_FIRMWARE_CATALOG;
        ["Y1", "Y2"].forEach(function (model) {
            var slot = document.querySelector('[data-guides-model="' + model + '"]');
            if (!slot) return;
            /* Keep the restore path (Original Software) at the end of the
               card, matching the hand-written ordering it replaces. */
            var items = catalog.filter(function (item) { return item.model === model; })
                .sort(function (a, b) {
                    return (/original/.test(a.slug) ? 1 : 0) - (/original/.test(b.slug) ? 1 : 0);
                });
            slot.innerHTML = items.map(function (item) {
                var dedicated = item.guide || item.seoPage || "";
                var href = dedicated || ("firmware-guide.html?model=" + encodeURIComponent(item.model) + "&software=" + encodeURIComponent(item.slug));
                return '<a class="lumen-button" href="' + escapeHtml(href) + '">' + escapeHtml(item.name) + '</a>';
            }).join("");
        });
    }

    /* Tap / hover hint modals (.lumen-tip). A toggle button shows a small
       popover on hover (mouse) and on tap (click), so dotfile tips work
       on both pointer and touch. Hover is bound to pointerenter only for
       pointerType mouse: on touch, the browser fires a synthetic mouseenter
       before click, which would open the popover and then the click would
       toggle it straight back closed. Escape and a click elsewhere close
       the popover. */
    function initLumenTips() {
        document.querySelectorAll("[data-lumen-tip]").forEach(function (tip) {
            var toggle = tip.querySelector(".lumen-tip-toggle");
            var popover = tip.querySelector(".lumen-tip-popover");
            if (!toggle || !popover) return;
            var open = false;
            var openedBy = null;
            var hideTimer = null;
            function show(source) {
                clearTimeout(hideTimer);
                open = true;
                openedBy = source;
                popover.hidden = false;
                toggle.setAttribute("aria-expanded", "true");
            }
            function hide() {
                clearTimeout(hideTimer);
                open = false;
                openedBy = null;
                popover.hidden = true;
                toggle.setAttribute("aria-expanded", "false");
            }
            function scheduleHide() {
                clearTimeout(hideTimer);
                hideTimer = setTimeout(hide, 120);
            }
            function onPointerEnter(event) {
                if (event.pointerType === "mouse") show("pointer");
            }
            function onPointerLeave(event) {
                if (event.pointerType === "mouse") scheduleHide();
            }
            toggle.addEventListener("pointerenter", onPointerEnter);
            toggle.addEventListener("pointerleave", onPointerLeave);
            toggle.addEventListener("focus", function () { show("focus"); });
            toggle.addEventListener("blur", scheduleHide);
            /* The click toggles only when the popover was itself opened by a
               previous click; a hover- or focus-opened popover stays open on
               the first click so touch taps (which fire focus + click) and
               mouse clicks never flash open then shut. */
            toggle.addEventListener("click", function (event) {
                event.stopPropagation();
                if (open && openedBy === "click") hide(); else show("click");
            });
            popover.addEventListener("pointerenter", onPointerEnter);
            popover.addEventListener("pointerleave", onPointerLeave);
            document.addEventListener("click", function (event) {
                if (open && !tip.contains(event.target)) hide();
            });
            document.addEventListener("keydown", function (event) {
                if (event.key === "Escape" && open) hide();
            });
        });
    }

    document.addEventListener("DOMContentLoaded", function () {
        document.querySelectorAll("[data-lumen-carousel]").forEach(initCarousel);
        document.querySelectorAll("[data-lumen-feedback]").forEach(initFeedback);
        initHomeFirmware();
        initPersonalisedGuide();
        initSoftwareGuideLinks();
        initPlatformReveal();
        initCopyButtons();
        initDownloadConfirm();
        initLumenTips();
        /* The release directory is authenticated against GitHub rate limits
           with tokens from config.ini, so wait for those before fetching. */
        loadGithubTokens().then(function () { initFirmwareDirectory(); });
    });
})();
