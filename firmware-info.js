/* Firmware README reader.
 *
 * Two pages share this script:
 *   firmware-info/<repo>.html   static copies the generator writes when a
 *                               project README names Updater CE
 *   firmware_info.html          live reader for every other project
 *
 * The Markdown parser is docs-viewer.js (window.InnioasisDocs), so a README
 * renders with the same link rewriting, images, tables and code blocks as the
 * release notes. The archive download total is read from the repository API:
 * a token from config.ini first, then the next token, then an anonymous call,
 * so the page keeps working when the tokens are missing or rate-limited. The
 * mirror ledgers replace that fallback and open a ZIP-by-ZIP breakdown.
 */
(function () {
  "use strict";

  var D = null;
  var root = null;
  var item = null;
  var repo = "";
  var params = new URLSearchParams(window.location.search);
  var latestReleases = [];
  var breakdownState = null;
  var breakdownRequested = false;
  var lastBreakdownFocus = null;

  /* Updater CE installs only what slidia_manifest.xml lists. A project that is
     present in the feeds but has no manifest entry keeps its README, its guide
     and its own rom.zip, but it must not offer an Updater CE route: the app
     would have no package to install. */
  var MANIFEST_SOURCES = [
    "https://raw.githubusercontent.com/y1-community/Innioasis-Updater/main/slidia_manifest.xml",
    "slidia_manifest.xml",
    "../slidia_manifest.xml",
    "/slidia_manifest.xml",
    "https://innioasis.app/slidia_manifest.xml"
  ];
  var listedReposPromise = null;

  function docs() {
    if (!D && window.InnioasisDocs) D = window.InnioasisDocs;
    return D;
  }

  function escapeHtml(value) {
    return String(value == null ? "" : value).replace(/[&<>'"]/g, function (char) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", "'": "&#39;", '"': "&quot;" }[char];
    });
  }

  function catalog() {
    return Array.isArray(window.INNIOASIS_FIRMWARE_CATALOG) ? window.INNIOASIS_FIRMWARE_CATALOG : [];
  }

  function sameRepo(a, b) {
    return String(a || "").toLowerCase() === String(b || "").toLowerCase();
  }

  /* The catalog item named by ?software=<slug>, then by ?repo=<owner/name>,
     or the page's own data-repo attribute (static pages know their project). */
  function resolveItem() {
    var slug = (params.get("software") || "").toLowerCase();
    var wanted = params.get("repo") || root.getAttribute("data-repo") || "";
    var list = catalog();
    var bySlug = null;
    var byRepo = null;
    list.forEach(function (entry) {
      if (slug && entry.slug === slug) bySlug = entry;
      if (wanted && !byRepo && sameRepo(entry.repo, wanted)) byRepo = entry;
    });
    return bySlug || byRepo || null;
  }

  /* Every model a repository ships for, so one README page can say Y1 and Y2. */
  function itemsForRepo(target) {
    return catalog().filter(function (entry) { return sameRepo(entry.repo, target); });
  }

  function readmePage(repoName) {
    var map = window.INNIOASIS_README_PAGES || {};
    var entry = map[String(repoName || "").toLowerCase()];
    return entry && entry.page ? entry.page : "";
  }

  function sourceCtx(repoName) {
    var api = docs();
    var source = api && api.parseSource("https://github.com/" + repoName + "/blob/HEAD/README.md");
    if (source) return source;
    return {
      repo: repoName,
      ref: "HEAD",
      dirRaw: "https://raw.githubusercontent.com/" + repoName + "/HEAD/",
      dirBlob: "https://github.com/" + repoName + "/blob/HEAD/"
    };
  }

  /* ---------------------------------------------------------------- identity */

  function paintIcon(source) {
    var box = document.getElementById("fi-icon");
    if (!box) return;
    if (source) {
      box.innerHTML = '<img src="' + escapeHtml(source) + '" width="40" height="40" alt="" loading="lazy" style="width:40px;height:40px;object-fit:cover;border-radius:10px;display:block;">';
      return;
    }
    box.innerHTML = box.getAttribute("data-generic") || "";
  }

  function iconFor(entries, base) {
    var icon = "";
    entries.forEach(function (entry) {
      if (!icon && entry.icon) icon = entry.icon;
    });
    if (icon) return icon;
    var map = window.INNIOASIS_RELEASE_ICONS || {};
    var asset = map[String(base.repo || "").toLowerCase()];
    return asset || "";
  }

  function paintIdentity(entries) {
    var primary = entries[0] || item || {};
    var name = primary.name || repo.split("/").pop();
    var models = [];
    entries.forEach(function (entry) {
      if (entry.model && models.indexOf(entry.model) === -1) models.push(entry.model);
    });
    var repoShort = repo.split("/").pop();
    /* The heading names the software; the alias line under it carries the
       README filename and repository, so searching for either finds this page. */
    var aliases = ["README.md", repo, repoShort, name].filter(function (part, index, list) {
      return part && list.indexOf(part) === index;
    });
    document.title = "About " + name + (models.length ? " (" + models.join(", ") + ")" : "") + " - README.md - Innioasis Updater";
    var title = document.getElementById("fi-title");
    if (title) title.textContent = "About " + name;
    var kicker = document.getElementById("fi-kicker");
    if (kicker) kicker.textContent = "Firmware README · " + (models.join(" · ") || "project");
    var readmeLine = document.getElementById("fi-readme-line");
    if (readmeLine) readmeLine.textContent = "Also known as: " + aliases.join(" · ");
    var lead = document.getElementById("fi-lead");
    if (lead) {
      lead.textContent = primary.description ||
        "The project's own README, shown here so you can read about the firmware without leaving the site.";
    }
    paintIcon(iconFor(entries, primary));

    var meta = document.getElementById("fi-meta");
    if (meta) {
      meta.innerHTML = models.length ? escapeHtml(models.join(" · ")) : "";
    }

    var actions = document.getElementById("fi-actions");
    if (actions) {
      var buttons = [];
      if (primary.guide) {
        buttons.push('<a class="lumen-button lumen-button--primary" href="' + escapeHtml(relative(primary.guide)) + '">Open the ' + escapeHtml(name) + " guide</a>");
      }
      var directory = "firmware.html" + (primary.slug ? "?model=" + encodeURIComponent(primary.model || "") + "&software=" + encodeURIComponent(primary.slug) : "");
      buttons.push('<a class="lumen-button" href="' + escapeHtml(relative(directory)) + '" data-updater-ce>Install with Updater CE</a>');
      if (primary.benefits) {
        buttons.push('<a class="lumen-button" href="' + escapeHtml(relative(primary.benefits)) + '">Why ' + escapeHtml(name) + "?</a>");
      }
      var staticPage = readmePage(repo);
      if (staticPage && window.location.pathname.indexOf("/firmware-info/") === -1) {
        buttons.push('<a class="lumen-button" href="' + escapeHtml(staticPage) + '">Permanent copy</a>');
      }
      actions.innerHTML = buttons.join("");
    }
  }

  /* The repositories an active <package> in the manifest names, lowercased.
     Resolves null when no copy of the manifest could be read, so a blocked
     network never hides a button that a listed project should have. */
  function fetchManifestText() {
    var index = 0;
    function attempt() {
      if (index >= MANIFEST_SOURCES.length) return Promise.resolve("");
      var url = MANIFEST_SOURCES[index++];
      return fetch(url, { cache: "no-cache" })
        .then(function (response) {
          if (!response.ok) throw new Error("HTTP " + response.status);
          return response.text();
        })
        .catch(function () { return attempt(); });
    }
    return attempt();
  }

  function listedRepos() {
    if (listedReposPromise) return listedReposPromise;
    listedReposPromise = fetchManifestText().then(function (text) {
      if (!text || typeof DOMParser === "undefined") return null;
      var doc = new DOMParser().parseFromString(text, "application/xml");
      if (doc.querySelector("parsererror")) return null;
      var listed = {};
      Array.prototype.forEach.call(doc.querySelectorAll("package"), function (pkg) {
        var name = String(pkg.getAttribute("name") || "").trim();
        var handler = pkg.getAttribute("handler") || "";
        if (!name || /please update/i.test(name)) return;
        if (handler && handler !== "Custom Firmware") return;
        var key = String(pkg.getAttribute("repo") || "").trim().toLowerCase();
        if (key) listed[key] = true;
      });
      return listed;
    }).catch(function () { return null; });
    return listedReposPromise;
  }

  /* Called after the action buttons are painted: a project with no manifest
     entry loses the Updater CE route, whatever the feeds still publish. */
  function applyManifestListing() {
    listedRepos().then(function (listed) {
      if (!listed) return;
      if (listed[String(repo || "").toLowerCase()]) return;
      Array.prototype.forEach.call(
        document.querySelectorAll("[data-updater-ce]"),
        function (button) {
          if (button.parentNode) button.parentNode.removeChild(button);
        }
      );
    });
  }

  /* Static pages sit one folder down, so their links take one ../ step. */
  function relative(href) {
    if (!href) return "";
    if (/^(https?:|mailto:|#|\/)/.test(href)) return href;
    return window.location.pathname.indexOf("/firmware-info/") !== -1 ? "../" + href : href;
  }

  /* ------------------------------------------------------------------- stats */

  /* The repository API allows more calls with a configured token, so the
     site's pool is tried first and an anonymous call is the fallback. */
  var tokenPool = null;
  function loadTokens() {
    if (tokenPool) return tokenPool;
    tokenPool = fetch("config.ini", { cache: "no-store" })
      .then(function (response) { return response.ok ? response.text() : ""; })
      .then(function (text) {
        return String(text || "").split(/\r?\n/)
          .map(function (line) { return line.trim(); })
          .filter(function (line) { return /^(key_\d+|token)\s*=/.test(line); })
          .map(function (line) { return line.split("=").slice(1).join("=").trim(); })
          .filter(function (value) { return value.length > 10; })
          .map(function (value) {
            return /^(github_pat_|ghp_|gho_|ghu_)/.test(value) ? value : "github_pat_" + value;
          });
      })
      .catch(function () { return []; });
    return tokenPool;
  }

  /* One repository API call: rotate the configured tokens, then go anonymous. */
  function apiJson(url) {
    return loadTokens().then(function (tokens) {
      var tried = [];
      function attempt() {
        var available = tokens.filter(function (token) { return tried.indexOf(token) === -1; });
        var token = available.length ? available[Math.floor(Math.random() * available.length)] : "";
        if (token) tried.push(token);
        var headers = { Accept: "application/vnd.github+json" };
        if (token) headers.Authorization = "Bearer " + token;
        return fetch(url, { headers: headers })
          .then(function (response) {
            if (!response.ok) {
              var error = new Error("HTTP " + response.status);
              error.status = response.status;
              throw error;
            }
            return response.json();
          })
          .catch(function (error) {
            if (token && (error.status === 401 || error.status === 403 || error.status === 429)) return attempt();
            throw error;
          });
      }
      return attempt();
    });
  }

  function number(value) {
    return typeof value === "number" && isFinite(value) ? value.toLocaleString() : "—";
  }

  function setStat(name, value) {
    var el = root ? root.querySelector('[data-stat="' + name + '"]') : null;
    if (el && value !== undefined && value !== null && value !== "") el.textContent = value;
  }

  /* Downloads from Firmware Archive: firmware ZIP downloads across the
     project's public releases. The mirror stats replace this with the
     combined source + portable total when they arrive; this remains the
     fallback while GitHub is loading or rate-limited. */
  function paintDownloads(releases) {
    latestReleases = releases || [];
    var downloads = 0;
    latestReleases.forEach(function (release) {
      if (!release || release.draft) return;
      (release.assets || []).forEach(function (asset) {
        if (!/\.zip$/i.test(String(asset.name || ""))) return;
        downloads += Number(asset.download_count) || 0;
      });
    });
    setStat("downloads", number(downloads));
    loadDownloadBreakdown();
  }

  function fallbackStatsFromBackup() {
    var lower = String(repo || "").toLowerCase();
    var statsMap = window.INNIOASIS_REPO_STATS || {};
    if (statsMap[lower] && typeof statsMap[lower].downloads === "number") {
      setStat("downloads", number(statsMap[lower].downloads));
      loadDownloadBreakdown();
      return;
    }
    var hardcoded = window.INNIOASIS_HARDCODED_RELEASES || {};
    var key = Object.keys(hardcoded).find(function (k) { return k.toLowerCase() === lower; });
    if (key && Array.isArray(hardcoded[key]) && hardcoded[key].length) {
      paintDownloads(hardcoded[key]);
      return;
    }
    var feedUrl = relative("feeds/" + lower + "/releases.json");
    fetch(feedUrl, { cache: "no-store" })
      .then(function (res) { return res.ok ? res.json() : null; })
      .then(function (list) {
        if (Array.isArray(list) && list.length) {
          paintDownloads(list);
          return;
        }
        var note = document.getElementById("fi-stats-note");
        if (note) note.textContent = "Download totals are unavailable right now.";
      })
      .catch(function () {
        var note = document.getElementById("fi-stats-note");
        if (note) note.textContent = "Download totals are unavailable right now.";
      });
  }

  function loadStats() {
    var collected = [];
    function page(index) {
      if (index > 3) { paintDownloads(collected); return; }
      apiJson("https://api.github.com/repos/" + repo + "/releases?per_page=100&page=" + index)
        .then(function (batch) {
          if (!Array.isArray(batch) || !batch.length) {
            if (collected.length) paintDownloads(collected);
            else fallbackStatsFromBackup();
            return;
          }
          collected = collected.concat(batch);
          if (batch.length < 100) { paintDownloads(collected); return; }
          page(index + 1);
        })
        .catch(function () {
          if (collected.length) { paintDownloads(collected); return; }
          fallbackStatsFromBackup();
        });
    }
    page(1);
  }

  /* ---------------------------------------------------------- download modal */

  /* A project's catalog entry names the portable mirror it publishes to. */
  function mirrorRepoFor(entries) {
    var list = entries || [];
    for (var i = 0; i < list.length; i++) {
      var value = String(list[i] && list[i].portable_zips || "").trim();
      if (value) return value.split(/[\s,]+/)[0];
    }
    return "";
  }

  function fallbackBreakdown() {
    if (!window.InnioasisMirrorStats) return null;
    return window.InnioasisMirrorStats.aggregate([], { sourceReleases: latestReleases });
  }

  /* Fetch every release ledger once, sum it, and let the modal explain the
     total. A failed request still leaves the source-release fallback usable. */
  function loadDownloadBreakdown() {
    if (breakdownRequested) return;
    breakdownRequested = true;
    var entries = itemsForRepo(repo);
    if (!entries.length && item) entries = [item];
    var mirror = mirrorRepoFor(entries);

    function finish(data) {
      var docs = data && Array.isArray(data.releases) ? data.releases : [];
      var aggregate = null;
      if (window.InnioasisMirrorStats) {
        aggregate = window.InnioasisMirrorStats.aggregate(docs, { sourceReleases: latestReleases });
        if ((!aggregate || !aggregate.total) && docs.length) aggregate = fallbackBreakdown();
      }
      if (!aggregate) return;
      breakdownState = aggregate;
      if (aggregate.total > 0) setStat("downloads", number(aggregate.total));
      attachDownloadBreakdown();
    }

    if (!mirror || !window.InnioasisMirrorStats) {
      finish(null);
      return;
    }
    fetch("/mirror-stats?repo=" + encodeURIComponent(mirror), { cache: "no-store" })
      .then(function (response) { return response.ok ? response.json() : null; })
      .then(finish)
      .catch(function () { finish(null); });
  }

  function attachDownloadBreakdown() {
    if (!root) return;
    var el = root.querySelector('[data-stat="downloads"]');
    if (!el) return;
    el.classList.add("lumen-stat-breakdown");
    el.setAttribute("role", "button");
    el.setAttribute("tabindex", "0");
    el.setAttribute("aria-haspopup", "dialog");
    el.setAttribute("aria-label", "See the download breakdown");
    el.title = "See the download breakdown";
    if (!el.getAttribute("data-breakdown-bound")) {
      el.setAttribute("data-breakdown-bound", "1");
      el.addEventListener("click", openDownloadBreakdown);
      el.addEventListener("keydown", function (event) {
        if (event.key === "Enter" || event.key === " ") {
          event.preventDefault();
          openDownloadBreakdown();
        }
      });
    }

    var stat = el.closest(".lumen-stat");
    if (stat && !stat.querySelector(".lumen-stat-info")) {
      var info = document.createElement("button");
      info.type = "button";
      info.className = "lumen-stat-info";
      info.textContent = "i";
      info.setAttribute("aria-label", "See the download breakdown");
      info.title = "See the download breakdown";
      info.addEventListener("click", openDownloadBreakdown);
      stat.appendChild(info);
    }
  }

  function ensureBreakdownModal() {
    var modal = document.getElementById("lumen-download-breakdown");
    if (modal) return modal;
    modal = document.createElement("div");
    modal.id = "lumen-download-breakdown";
    modal.className = "lumen-stats-modal";
    modal.setAttribute("data-i18n-skip", "1");
    modal.setAttribute("translate", "no");
    modal.hidden = true;
    modal.innerHTML =
      '<div class="lumen-stats-backdrop" data-stats-close></div>' +
      '<div class="lumen-stats-dialog" role="dialog" aria-modal="true" ' +
        'aria-labelledby="lumen-stats-title" aria-describedby="lumen-stats-desc">' +
        '<button type="button" class="lumen-stats-close" data-stats-close ' +
          'aria-label="Close download breakdown">×</button>' +
        '<div class="lumen-stats-body"></div>' +
      '</div>';
    document.body.appendChild(modal);
    modal.addEventListener("click", function (event) {
      if (event.target === modal || event.target.closest("[data-stats-close]")) closeDownloadBreakdown();
    });
    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && !modal.hidden) closeDownloadBreakdown();
    });
    return modal;
  }

  function breakdownRows(rows, emptyText) {
    if (!rows || !rows.length) return '<li class="lumen-stats-empty">' + escapeHtml(emptyText) + '</li>';
    return rows.map(function (row) {
      return '<li' + (row.count ? '' : ' class="is-zero"') + '>' +
        '<span>' + escapeHtml(row.label || row.name) + '</span>' +
        '<strong>' + number(row.count) + '</strong>' +
      '</li>';
    }).join("");
  }

  function openDownloadBreakdown() {
    var aggregate = breakdownState || fallbackBreakdown();
    if (!aggregate) return;
    var modal = ensureBreakdownModal();
    var body = modal.querySelector(".lumen-stats-body");
    if (!body) return;
    var heading = root ? root.querySelector(".lumen-release-titles h1") : null;
    var title = heading ? heading.textContent.trim() : "Firmware downloads";
    var originals = (aggregate.originals || []).slice();
    var sourceNote = aggregate.hasStats
      ? "Combined source and mirror downloads for each original ZIP."
      : "Live mirror statistics could not be loaded; this is the source archive count.";

    body.innerHTML =
      '<p class="lumen-kicker">Download breakdown</p>' +
      '<h2 id="lumen-stats-title">' + escapeHtml(title) + '</h2>' +
      '<p class="lumen-stats-total">' + number(aggregate.total) + '</p>' +
      '<p class="lumen-stats-desc" id="lumen-stats-desc">' +
        'Total GitHub download events for firmware ZIPs and portable packages. ' +
        'These are downloads, not unique people.' +
      '</p>' +
      '<h3>Original firmware ZIPs</h3>' +
      '<p class="lumen-stats-sub">' + escapeHtml(sourceNote) + '</p>' +
      '<ul class="lumen-stats-list">' + breakdownRows(originals, "No original ZIP downloads recorded yet.") + '</ul>' +
      '<h3>Portable packages</h3>' +
      '<p class="lumen-stats-sub">Repackaged builds published by the portable mirror.</p>' +
      '<ul class="lumen-stats-list">' + breakdownRows(aggregate.portable, "No portable package downloads recorded yet.") + '</ul>' +
      '<p class="lumen-stats-note">Totals count firmware ZIPs and portable packages only. ' +
        'README images, manifests, checksums and other mirrored files are excluded.</p>';

    lastBreakdownFocus = document.activeElement;
    modal.hidden = false;
    document.documentElement.classList.add("lumen-stats-modal-open");
    var close = modal.querySelector(".lumen-stats-close");
    if (close) close.focus();
  }

  function closeDownloadBreakdown() {
    var modal = document.getElementById("lumen-download-breakdown");
    if (!modal) return;
    modal.hidden = true;
    document.documentElement.classList.remove("lumen-stats-modal-open");
    if (lastBreakdownFocus && typeof lastBreakdownFocus.focus === "function") lastBreakdownFocus.focus();
    lastBreakdownFocus = null;
  }

  /* ------------------------------------------------------------------- readme */

  var README_PATHS = ["README.md", "readme.md", "Readme.md", "README.markdown", "README.MD", "docs/README.md"];

  function loadReadme() {
    var body = document.getElementById("fi-body");
    if (!body) return;
    /* Static pages already carry the rendered README, so a failed API call
       must never replace them with an error. */
    if (window.location.pathname.indexOf("/firmware-info/") !== -1) return;
    var api = docs();
    if (!api || typeof api.fetchRepoMarkdown !== "function") {
      body.innerHTML = '<p class="lumen-doc-status">The README reader did not load. ' +
        '<a href="' + escapeHtml(relative((item && item.guide) || "firmware.html")) + '">Open the install guide</a> instead.</p>';
      return;
    }
    function attempt(index) {
      if (index >= README_PATHS.length) {
        body.innerHTML = '<p class="lumen-doc-status">This project has no README the site can read. ' +
          'Read the <a href="' + escapeHtml(relative((item && item.guide) || "firmware.html")) + '">install guide</a> instead.</p>';
        return;
      }
      api.fetchRepoMarkdown(repo, "HEAD", README_PATHS[index])
        .then(function (result) {
          var markdown = result && result.markdown ? result.markdown : "";
          if (!markdown.trim()) throw new Error("empty");
          body.innerHTML = api.markdownToHtml(markdown, sourceCtx(repo));
          body.setAttribute("data-readme-path", README_PATHS[index]);
        })
        .catch(function () { attempt(index + 1); });
    }
    attempt(0);
  }

  /* -------------------------------------------------------------------- mount */

  function mount() {
    root = document.querySelector("[data-firmware-info]");
    if (!root) return;
    item = resolveItem();
    repo = (item && item.repo) || params.get("repo") || root.getAttribute("data-repo") || "";
    if (!repo || repo.indexOf("/") === -1) {
      var body = document.getElementById("fi-body");
      if (body) {
        body.innerHTML = '<p class="lumen-doc-status">No firmware project was named. ' +
          '<a href="firmware.html">Open the firmware directory</a> and pick a release first.</p>';
      }
      return;
    }
    var entries = itemsForRepo(repo);
    if (!entries.length && item) entries = [item];
    paintIdentity(entries);
    applyManifestListing();
    loadStats();
    loadReadme();
  }

  window.InnioasisFirmwareInfo = {
    mount: mount,
    readmePage: readmePage
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", mount);
  } else {
    mount();
  }
})();
