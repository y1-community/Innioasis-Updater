(function () {
  "use strict";

  /* Donation appeals and cross-subdomain / inter-page preference persistence.
     Carries language, donation, and privacy preferences between pages and between
     innioasis.app and themes.innioasis.app subdomains via URL query parameters
     and shared cookies (.innioasis.app). */
  var DONATIONS_KEY = "innioasis-donations-off";

  function setSharedCookie(name, value, days) {
    try {
      var d = new Date();
      d.setTime(d.getTime() + ((days || 365) * 24 * 60 * 60 * 1000));
      var expires = "; expires=" + d.toUTCString();
      var host = window.location.hostname || "";
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

  function donationsParam() {
    try {
      var raw = new URLSearchParams(window.location.search).get("donations");
      if (raw === null) return null;
      var value = String(raw).trim().toLowerCase();
      if (value === "false" || value === "0" || value === "no" || value === "off") return false;
      if (value === "true" || value === "1" || value === "yes" || value === "on") return true;
    } catch (_) {}
    return null;
  }

  function donationsStored() {
    try {
      if (window.localStorage.getItem(DONATIONS_KEY) === "1") return true;
    } catch (_) {}
    try {
      if (getSharedCookie(DONATIONS_KEY) === "1") return true;
    } catch (_) {}
    return false;
  }

  function isY1DonationsDisabled() {
    if (donationsParam() === false) return true;
    return donationsStored();
  }

  var DONATIONS_CSS =
    "html.y1-donations-off [data-donations-appeal]," +
    "html.y1-donations-off .y1-contributor-stream-box { display: none !important; }";

  function applyDonationsState() {
    var root = document.documentElement;
    if (!root) return;
    root.classList.toggle("y1-donations-off", isY1DonationsDisabled());
    if (document.getElementById("y1-donations-css")) return;
    var style = document.createElement("style");
    style.id = "y1-donations-css";
    style.textContent = DONATIONS_CSS;
    (document.head || root).appendChild(style);
  }

  window.isY1DonationsDisabled = isY1DonationsDisabled;
  window.hasY1DonationsPreference = donationsStored;

  window.setY1DonationsDisabled = function (disabled) {
    try {
      if (disabled) {
        window.localStorage.setItem(DONATIONS_KEY, "1");
        setSharedCookie(DONATIONS_KEY, "1");
      } else {
        window.localStorage.removeItem(DONATIONS_KEY);
        setSharedCookie(DONATIONS_KEY, "0");
      }
    } catch (_) {}
    applyDonationsState();
    try {
      window.dispatchEvent(new CustomEvent("y1-donations-change", { detail: { disabled: !!disabled } }));
    } catch (_) {}
    if (typeof window.y1DecorateLinks === "function") {
      window.y1DecorateLinks();
    }
  };

  (function rememberDonationChoiceFromUrl() {
    var fromUrl = donationsParam();
    if (fromUrl !== null) {
      try {
        if (fromUrl) {
          window.localStorage.removeItem(DONATIONS_KEY);
          setSharedCookie(DONATIONS_KEY, "0");
        } else {
          window.localStorage.setItem(DONATIONS_KEY, "1");
          setSharedCookie(DONATIONS_KEY, "1");
        }
      } catch (_) {}
    } else {
      var cookieVal = getSharedCookie(DONATIONS_KEY);
      if (cookieVal === "1") {
        try { window.localStorage.setItem(DONATIONS_KEY, "1"); } catch (_) {}
      }
    }
  })();

  applyDonationsState();

  /* ---------------------------------------------------------------- */
  /* Cross-Subdomain & Inter-Page Preference URL Decoration           */
  /* ---------------------------------------------------------------- */

  function getActiveLocale() {
    try {
      var param = new URLSearchParams(window.location.search).get("lang");
      if (param) {
        var p = param.toLowerCase();
        return p === "jp" ? "ja" : (p === "zh" ? "zh-cn" : p);
      }
      var htmlLocale = (document.documentElement && (document.documentElement.getAttribute("data-locale") || document.documentElement.lang)) || "";
      if (htmlLocale && htmlLocale !== "en") {
        var h = htmlLocale.toLowerCase();
        return h === "jp" ? "ja" : (h === "zh" ? "zh-cn" : h);
      }
      var match = (window.location.pathname || "").match(/_([a-z]{2,3}(?:-[a-z0-9]{2,4})?)\.html$/i);
      if (match) {
        var m = match[1].toLowerCase();
        return m === "jp" ? "ja" : (m === "zh" ? "zh-cn" : m);
      }
      if (window.SiteLocale && typeof window.SiteLocale.locale === "function") {
        var sl = String(window.SiteLocale.locale()).toLowerCase();
        if (sl && sl !== "en") return sl === "jp" ? "ja" : sl;
      }
      if (window.InnioasisLocale && window.InnioasisLocale.locale) {
        var loc = String(window.InnioasisLocale.locale).toLowerCase();
        return loc === "jp" ? "ja" : loc;
      }
      var stored = window.localStorage.getItem("innioasis-locale");
      if (stored) return stored.toLowerCase();
      var cookie = getSharedCookie("innioasis-locale");
      if (cookie) return cookie.toLowerCase();
    } catch (_) {}
    return "en";
  }

  function getPrivacyAnalyticsParam() {
    try {
      var raw = new URLSearchParams(window.location.search).get("privacy_analytics");
      if (raw) return raw;
      if (window.INNIOASIS_PRIVACY && window.INNIOASIS_PRIVACY.read) {
        var prefs = window.INNIOASIS_PRIVACY.read();
        if (prefs && (prefs.analytics === false || prefs.analytics === "off")) return "off";
        if (prefs && prefs.analytics === "essential") return "essential";
      }
      var cookie = getSharedCookie("innioasis-privacy-analytics");
      if (cookie) return cookie;
    } catch (_) {}
    return null;
  }

  function getPrivacyParam() {
    try {
      var raw = new URLSearchParams(window.location.search).get("privacy");
      if (raw) return raw;
      if (window.INNIOASIS_PRIVACY && window.INNIOASIS_PRIVACY.hasDecided()) {
        var prefs = window.INNIOASIS_PRIVACY.read();
        if (prefs) {
          if (prefs.feedback && prefs.nightly) return "all";
          if (!prefs.feedback && !prefs.nightly) return "none";
          if (prefs.feedback && !prefs.nightly) return "feedback";
          if (!prefs.feedback && prefs.nightly) return "nightly";
        }
      }
      var cookie = getSharedCookie("innioasis-privacy");
      if (cookie) return cookie;
    } catch (_) {}
    return null;
  }

  /* A visitor whose browser reports de-AT, fr-CA or nl-BE still reads German,
     French or Dutch, and those pages exist as _de/_fr/_nl.html. Matching the
     raw tag against the core list missed every regional variant, so links fell
     back to the English page and only the runtime translated it. */
  function baseLocaleCode(code) {
    var clean = String(code || "").toLowerCase().trim();
    if (!clean) return "";
    var base = clean.split("-")[0];
    if (base === "zh") {
      return /-(tw|hk|mo)$/.test(clean) ? "zh-TW" : "zh-CN";
    }
    return base;
  }

  var prerenderedData = null;
  function getPrerenderedData() {
    if (prerenderedData) return prerenderedData;
    if (window.__y1Prerendered && window.__y1Prerendered.pages) {
      prerenderedData = window.__y1Prerendered;
      return prerenderedData;
    }
    return null;
  }
  try {
    var pUrl = (window.location && window.location.origin ? window.location.origin : "") + "/i18n/prerendered.json";
    fetch(pUrl).then(function (r) {
      if (r.ok) return r.json();
    }).then(function (data) {
      if (data && data.pages) {
        prerenderedData = data;
        window.__y1Prerendered = data;
      }
    }).catch(function () {});
  } catch (_) {}

  function resolveStaticLocaleCode(loc, data) {
    if (!loc || loc === "en") return null;
    var clean = String(loc).toLowerCase().trim().replace(/_/g, "-");
    var locales = (data && data.locales) || [];
    var aliases = (data && data.aliases) || {};

    for (var i = 0; i < locales.length; i++) {
      if (locales[i].toLowerCase() === clean) return locales[i];
    }
    for (var primary in aliases) {
      if (!Object.prototype.hasOwnProperty.call(aliases, primary)) continue;
      var list = aliases[primary] || [];
      for (var j = 0; j < list.length; j++) {
        if (list[j].toLowerCase() === clean) return primary;
      }
    }
    var base = baseLocaleCode(loc);
    if (base && base.toLowerCase() !== clean) {
      for (var k = 0; k < locales.length; k++) {
        if (locales[k].toLowerCase() === base.toLowerCase()) return locales[k];
      }
    }
    return null;
  }

  function getPrerenderedStaticPath(dir, name, loc) {
    var data = getPrerenderedData();
    var cleanDir = (dir || "").replace(/^\/+/, "").replace(/\/+$/, "");
    var targetPage = cleanDir ? (cleanDir + "/" + name) : name;
    if (data && data.pages) {
      if (data.pages.indexOf(targetPage) === -1 && data.pages.indexOf(name) === -1) {
        return null;
      }
    }
    var matchedCode = resolveStaticLocaleCode(loc, data);
    if (!matchedCode) return null;
    var d = dir || "";
    if (d && !d.endsWith("/")) d += "/";
    return d + name + "_" + matchedCode + ".html";
  }

  function getActiveTheme() {
    try {
      var stored = window.localStorage.getItem("lumen-theme");
      if (stored && ["auto", "dark", "light", "high-contrast", "2077"].indexOf(stored) >= 0) {
        return stored;
      }
      var cookie = getSharedCookie("innioasis-theme");
      if (cookie && ["auto", "dark", "light", "high-contrast", "2077"].indexOf(cookie) >= 0) {
        return cookie;
      }
      var attr = document.documentElement && (document.documentElement.getAttribute("data-theme") || document.documentElement.getAttribute("data-lumen-theme"));
      if (attr && ["dark", "light", "high-contrast", "2077"].indexOf(attr) >= 0) {
        return attr;
      }
    } catch (_) {}
    return "dark";
  }

  /* The accent the header picked (or the app handed over), read from the same
     places the shell writes it, so cross-site links can carry it. */
  function getActiveAccent() {
    try {
      if (typeof window.y1GetAccent === "function") {
        var live = window.y1GetAccent();
        if (live) return live;
      }
      var stored = window.localStorage.getItem("lumen-accent");
      if (stored && /^#[0-9a-f]{6}$/i.test(stored)) return stored;
      var cookie = getSharedCookie("innioasis-accent");
      if (cookie && /^#[0-9a-f]{6}$/i.test(cookie)) return cookie;
      var attr = document.documentElement && document.documentElement.getAttribute("data-accent");
      if (attr && /^#[0-9a-f]{6}$/i.test(attr)) return attr;
    } catch (_) {}
    return null;
  }

  function hasCeAccent() {
    try {
      if (typeof window.y1HasPcAccent === "function") return Boolean(window.y1HasPcAccent());
      return Boolean(window.localStorage.getItem("innioasis-pc-accent") || getSharedCookie("innioasis-pc-accent"));
    } catch (_) {}
    return false;
  }

  function getActiveAccessibility() {
    try {
      var stored = window.localStorage.getItem("innioasis-accessibility");
      if (stored) return stored;
      var cookie = getSharedCookie("innioasis-accessibility");
      if (cookie) return cookie;
      if (document.documentElement && (document.documentElement.classList.contains("reduce-motion") || document.documentElement.getAttribute("data-reduced-motion") === "true")) {
        return "reduce-motion";
      }
      if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        return "reduce-motion";
      }
    } catch (_) {}
    return null;
  }

  function getActiveFontScale() {
    try {
      var p = new URLSearchParams(window.location.search);
      var raw = p.get("fontSize") || p.get("fontScale") || p.get("font-scale") || p.get("fs") || p.get("lumen-font-scale");
      if (raw) {
        var v = parseFloat(String(raw).replace("%", ""));
        if (v > 10) v = v / 100;
        if (v >= 0.7 && v <= 1.6) return +(v.toFixed(2));
      }
      var stored = parseFloat(window.localStorage.getItem("lumen-font-scale") || "");
      if (stored >= 0.7 && stored <= 1.6) return +(stored.toFixed(2));
      var cookie = parseFloat(getSharedCookie("lumen-font-scale") || "");
      if (cookie >= 0.7 && cookie <= 1.6) return +(cookie.toFixed(2));
    } catch (_) {}
    return null;
  }

  function decorateLinkUrl(rawHref) {
    if (!rawHref) return rawHref;
    var raw = String(rawHref).trim();
    if (!raw || /^(mailto:|tel:|javascript:|#|blob:|data:)/i.test(raw)) return raw;
    var url;
    var isAbsoluteInput = /^[a-z]+:\/\//i.test(raw) || raw.indexOf("//") === 0;
    try {
      url = new URL(raw, window.location.href);
    } catch (_) {
      return raw;
    }

    /* A GitHub releases page is served by our own release view: the same
       releases, plus the portable builds for this computer, on our site. */
    if (/(^|\.)github\.com$/i.test(url.hostname)) {
      var ghRelease = url.pathname.match(/^\/([^/]+)\/([^/]+)\/releases(?:\/tag\/([^/]+))?\/?$/i);
      if (ghRelease) {
        var viewQuery = "repo=" + encodeURIComponent(ghRelease[1] + "/" + ghRelease[2]);
        if (ghRelease[3]) viewQuery += "&tag=" + encodeURIComponent(decodeURIComponent(ghRelease[3]));
        return "/release_view.html?" + viewQuery;
      }
    }

    /* Origin, not hostname: a dev server on port 8081 and the main site on
       8080 are two sites, and the handoff has to reach the other one there
       too. On the real domains the two tests are the same. */
    var isSameHost = url.origin === window.location.origin;
    var isSubdomain = /(^|\.)innioasis\.app$/i.test(url.hostname) || url.hostname === "localhost" || url.hostname === "127.0.0.1";
    if (!isSameHost && !isSubdomain) return raw;

    /* Clean all preference parameters from link targets so users share clean, scary-free URLs */
    var prefKeys = [
      "donations",
      "privacy",
      "analytics",
      "telemetry",
      "privacy_analytics",
      "privacy_feedback",
      "privacy_nightly",
      "site_theme",
      "accent",
      "accent_color",
      "accent-color",
      "accentColor",
      "accentColour",
      "ce",
      "accessibility",
      "a11y",
      "fontSize",
      "fontScale",
      "font-scale",
      "fs",
      "lumen-font-scale",
      "lang"
    ];
    prefKeys.forEach(function (k) {
      url.searchParams.delete(k);
    });
    if (url.searchParams.has("theme")) {
      var tVal = (url.searchParams.get("theme") || "").toLowerCase().trim();
      var isSiteTheme = ["auto", "dark", "high-contrast", "2077", "light"].indexOf(tVal) >= 0;
      var isThemeGalleryDetail = /theme(?:_[a-zA-Z0-9_-]+)?\.html$/i.test(url.pathname);
      if (isSiteTheme || !isThemeGalleryDetail) {
        url.searchParams.delete("theme");
      }
    }

    /* Language preference: route to pre-rendered static path if appropriate without query bloat */
    var loc = getActiveLocale();
    if (loc && loc !== "en") {
      var path = url.pathname;
      var dir = "";
      var name = "";
      if (path === "/" || path === "") {
        dir = "/";
        name = "index";
      } else {
        var htmlMatch = path.match(/^(.+?\/)?([a-zA-Z0-9_-]+)\.html$/i);
        if (htmlMatch && !/_[a-zA-Z0-9_-]+$/i.test(htmlMatch[2])) {
          dir = htmlMatch[1] || "";
          name = htmlMatch[2];
        }
      }
      if (name) {
        var staticPath = getPrerenderedStaticPath(dir, name, loc);
        if (staticPath) {
          url.pathname = staticPath.charAt(0) === "/" ? staticPath : ("/" + staticPath);
        }
      }
    }

    /* Same-origin links stay clean. A link to the other Innioasis site
       carries the visitor's appearance and text size so the destination
       paints correctly before its own shell has read storage. */
    if (!isSameHost || isAbsoluteInput) {
      if (url.origin !== window.location.origin) {
        var curTheme = getActiveTheme();
        if (curTheme) {
          if (/theme(?:_[a-zA-Z0-9_-]+)?\.html$/i.test(url.pathname)) {
            url.searchParams.set("site_theme", curTheme);
          } else {
            url.searchParams.set("theme", curTheme);
          }
        }
        var curA11y = getActiveAccessibility();
        if (curA11y) url.searchParams.set("accessibility", curA11y);
        var curFs = getActiveFontScale();
        if (curFs && curFs !== 0.8) url.searchParams.set("fontSize", String(curFs));
        /* The visitor's accent, and whether the app handed it over, travel
           with links to the other Innioasis site so its header and its
           "Match my PC's theme colours" choice agree with this one. */
        var curAccent = getActiveAccent();
        if (curAccent) url.searchParams.set("accent", curAccent);
        if (hasCeAccent()) url.searchParams.set("ce", "true");
        var handoffLang = getActiveLocale();
        if (handoffLang && handoffLang !== "en") url.searchParams.set("lang", handoffLang);
        url.searchParams.set("donations", isY1DonationsDisabled() ? "false" : "true");
        var handoffPrivacy = getPrivacyParam();
        if (handoffPrivacy) url.searchParams.set("privacy", handoffPrivacy);
      }
      return url.toString();
    }
    var query = url.searchParams.toString();
    return url.pathname + (query ? ("?" + query) : "") + url.hash;
  }

  function handleLinkClick(event) {
    var link = event.target && event.target.closest ? event.target.closest("a[href]") : null;
    if (!link) return;
    var href = link.getAttribute("href");
    if (!href) return;
    var decorated = decorateLinkUrl(href);
    if (decorated && decorated !== href) {
      link.href = decorated;
    }
  }

  document.addEventListener("click", handleLinkClick, true);
  document.addEventListener("auxclick", handleLinkClick, true);

  function decorateAllDocumentLinks() {
    try {
      if (typeof window.y1ClearPreferencesFromUrl === "function") {
        window.y1ClearPreferencesFromUrl();
      }
      var links = document.querySelectorAll("a[href]");
      for (var i = 0; i < links.length; i++) {
        var link = links[i];
        var href = link.getAttribute("href");
        if (!href) continue;
        var decorated = decorateLinkUrl(href);
        if (decorated && decorated !== href) {
          link.href = decorated;
        }
      }
    } catch (_) {}
  }

  window.y1DecorateLinks = decorateAllDocumentLinks;
  window.y1DecorateUrl = decorateLinkUrl;

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", decorateAllDocumentLinks);
  } else {
    decorateAllDocumentLinks();
  }

  window.addEventListener("y1-dock-slot-ready", decorateAllDocumentLinks);
  window.addEventListener("site-locale-ready", decorateAllDocumentLinks);
  window.addEventListener("site-locale-change", decorateAllDocumentLinks);
  window.addEventListener("y1-donations-change", decorateAllDocumentLinks);
  window.addEventListener("innioasis-privacy-change", decorateAllDocumentLinks);


  function canonicalPageKey() {
    var path = (window.location.pathname || "").toLowerCase();
    var file = path.split("/").pop() || "";
    if (!file || file === "." || file === "..") return "index";
    file = file.replace(/\.html?$/, "");
    /* Pre-rendered locale copies carry a language suffix (index_de, guide_pt-BR,
       about_zh-CN). They are the same page as the English original, so the
       suffix must not change which product the page belongs to. */
    file = file.replace(/_(?:[a-z]{2,3})(?:-[a-z0-9]{2,4})?$/, "");
    return file || "index";
  }

  function detectPersona() {
    var key = canonicalPageKey();
    if (
      key === "index" ||
      key === "guide" ||
      key === "installguide" ||
      key === "troubleshooting" ||
      key === "credits" ||
      key === "support_devs" ||
      key === "updater-comparison" ||
      key === "about"
    ) {
      return "updater";
    }
    return "firmware";
  }

  function decorateCrossDomainHref(href) {
    if (!href) return href;
    return decorateLinkUrl(href);
  }

  var isThemesSite = (window.location.hostname === "themes.innioasis.app") || (window.location.port === "8081") || !!document.querySelector(".gallery-topbar");

  function decorateMainSiteHref(path) {
    if (!path) return path;
    if (isThemesSite) {
      var base = (window.location.hostname === "localhost" || window.location.hostname === "127.0.0.1")
        ? (window.location.protocol + "//" + window.location.hostname + ":8080")
        : "https://innioasis.app";
      return decorateLinkUrl(base + path);
    }
    return decorateLinkUrl(path);
  }

  var persona = detectPersona();
  var isFirmwarePersona = persona === "firmware";
  var activeTitle = isThemesSite ? "Themes Gallery" : (isFirmwarePersona ? "Firmware Archive" : "Updater CE");
  var activeHomeHref = isFirmwarePersona ? "/firmware.html" : "/";

  (function updateDocumentTitle() {
    var path = (window.location.pathname || "").toLowerCase();
    var t = document.title || "";
    if (isThemesSite) {
      if (path === "" || path === "/" || path.endsWith("/index.html")) {
        document.title = "Innioasis Themes Gallery - Y1 and Y2 Rockbox themes";
        return;
      }
      if (t.indexOf("Themes Gallery") === -1) {
        var themeBase = t.split(/\s+[|\u00b7-]\s+Innioasis/)[0].trim();
        document.title = (themeBase || t) + " - Innioasis Themes Gallery";
      }
      return;
    }
    if (isFirmwarePersona) {
      if (t.indexOf("Innioasis Firmware Downloads") === -1) {
        var base = t.replace(/\s+[|·-]\s+Innioasis [^|·-]*$/, "").trim();
        document.title = (base || t) + " - Innioasis Firmware Downloads";
      }
    } else if (t.indexOf("Innioasis Updater") === -1) {
      var uBase = t.replace(/\s+[|·-]\s+Innioasis [^|·-]*$/, "").trim();
      document.title = (uBase || t) + " - Innioasis Updater";
    }
  })();

  var allSwitcherItems = [
    {
      id: "firmware",
      title: "Innioasis Firmware Archive",
      subtitle: "Original Software, custom ROMs & guides",
      href: "/firmware.html",
      icon: '<span class="lumen-app-icon lumen-app-icon--firmware" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m16 6 4 14"/><path d="M12 6v14"/><path d="M8 8v12"/><path d="M4 4v16"/></svg></span>'
    },
    {
      id: "updater",
      title: "Updater CE",
      subtitle: "One-click installer for Windows, macOS & Linux",
      href: "/",
      icon: '<span class="lumen-app-icon lumen-app-icon--updater" aria-hidden="true"><img src="/assets/icon.ico" width="34" height="34" alt="" aria-hidden="true"></span>'
    },
    {
      id: "themes",
      title: "Themes Gallery",
      subtitle: "Themes for Innioasis Y1 & Y2 players",
      href: "https://themes.innioasis.app/",
      external: true,
      icon: '<span class="lumen-app-icon lumen-app-icon--themes" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" fill="currentColor"><path d="M12 3a9 9 0 1 0 0 18c1.2 0 2-.8 2-2 0-.5-.2-1-.5-1.3-.4-.4-.6-.9-.6-1.4 0-1.2 1-2.1 2.1-2.1H17a4 4 0 0 0 4-4C21 6.4 17 3 12 3zm-4.5 9a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm3-4a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm5 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"/></svg></span>'
    }
  ];

  /* Only show the other two community sites that the user is not currently on */
  var switcherListHtml = allSwitcherItems
    .filter(function (item) {
      return item.id !== persona;
    })
    .map(function (item) {
      var crossSite = !!item.external || isThemesSite;
      var href = item.external
        ? decorateCrossDomainHref(item.href)
        : (isThemesSite ? decorateMainSiteHref(item.href) : item.href);
      return (
        '<li>' +
        '<a class="lumen-site-switcher-item" href="' + escapeHtml(href) + '"' + (crossSite ? ' data-cross-site-link="1"' : '') + '>' +
        '<span class="lumen-site-switcher-item-icon">' + item.icon + '</span>' +
        '<span class="lumen-site-switcher-item-copy">' +
        '<strong>' + escapeHtml(item.title) + '</strong>' +
        '<small>' + escapeHtml(item.subtitle) + '</small>' +
        '</span>' +
        '</a>' +
        '</li>'
      );
    }).join("");

  /* The download itself is a desktop app, so a phone, tablet or ChromeOS
     visitor gets the neutral label instead of "for macOS" on an iPhone or
     "for Linux" on an Android tablet. */
  function detectUserPlatformLabel() {
    var ua = (typeof navigator !== "undefined" && (navigator.userAgentData && navigator.userAgentData.platform) || navigator.userAgent || "").toLowerCase();
    if (/android|iphone|ipad|ipod|ipados|mobile|tablet|cros|chrome os|chromeos|kindle|silk|iemobile/i.test(ua)) return "";
    if (/mac/i.test(ua)) return "macOS";
    if (/win/i.test(ua)) return "Windows";
    if (/linux|x11/i.test(ua)) return "Linux";
    return "";
  }
  /* The button is translated like every other label, but the product name in
     it is not: "Get Updater for macOS" was one opaque string no catalog could
     hold, so it stayed English on every non-English page. Keeping the wording
     and the platform in separate nodes leaves "Get Updater" a catalog key and
     the platform a proper noun. */
  var platformLabel = detectUserPlatformLabel();
  var ctaLabel = platformLabel ? "Get Updater" : "Get Updater CE";
  var ctaPlatformHtml = platformLabel
    ? '<span class="lumen-nav-install-cta-platform" translate="no" class="notranslate" data-i18n-skip> · ' + escapeHtml(platformLabel) + "</span>"
    : "";

  var brandIconHtml = isFirmwarePersona
    ? '<span class="lumen-brand-icon lumen-brand-icon--firmware" aria-hidden="true"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="1.9" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m16 6 4 14"/><path d="M12 6v14"/><path d="M8 8v12"/><path d="M4 4v16"/></svg></span>'
    : '<span class="lumen-brand-icon lumen-brand-icon--updater" aria-hidden="true"><img src="/assets/icon.ico" width="38" height="38" alt="" aria-hidden="true"></span>';


  var root = document.getElementById("nav-root");
  if (root) {
    root.innerHTML =
      '<nav aria-label="Primary navigation">' +
      '<div class="nav-container">' +
      '<div class="logo lumen-brand-switcher-wrap">' +
      '<div class="lumen-brand-bar">' +
      '<a class="lumen-brand-home" href="' + escapeHtml(activeHomeHref) + '">' +
      brandIconHtml +
      '<span class="lumen-brand-title" id="lumen-brand-title">' + escapeHtml(activeTitle) + '</span>' +
      '</a>' +
      '<button type="button" class="lumen-site-switcher-toggle" id="lumen-site-switcher-toggle" aria-expanded="false" aria-controls="lumen-site-switcher-tray" aria-label="Switch Innioasis site persona" title="Switch site">' +
      '<svg class="lumen-site-switcher-glyph" viewBox="0 0 16 16" width="12" height="12" fill="currentColor" aria-hidden="true"><path d="M4.2 6.2a.75.75 0 0 1 1.06 0L8 8.94l2.74-2.74a.75.75 0 1 1 1.06 1.06l-3.27 3.27a.75.75 0 0 1-1.06 0L4.2 7.26a.75.75 0 0 1 0-1.06z"/></svg>' +
      '</button>' +
      '</div>' +
      '<div class="lumen-site-switcher-tray" id="lumen-site-switcher-tray" hidden role="menu" aria-label="Switch between Themes Gallery, Updater CE, and Firmware Archive">' +
      '<p class="lumen-site-switcher-heading">Innioasis Sites</p>' +
      '<ul class="lumen-site-switcher-list">' + switcherListHtml + '</ul>' +
      '</div>' +
      '</div>' +
      '<div class="nav-tools">' +
      '<div class="lumen-notices-wrap" id="lumen-notices-wrap">' +
      '<button type="button" class="lumen-notices-btn" id="lumen-notices-btn" aria-expanded="false" aria-controls="lumen-notices-tray" aria-label="Notices and device safety alerts" title="Notices">' +
      '<svg viewBox="0 0 20 20" width="18" height="18" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 2.5a4.5 4.5 0 0 0-4.5 4.5v2.6c0 .8-.3 1.6-.8 2.2L3.5 13.2h13l-1.2-1.4a3.4 3.4 0 0 1-.8-2.2V7A4.5 4.5 0 0 0 10 2.5z"/><path d="M8.2 15.5a2 2 0 0 0 3.6 0"/></svg>' +
      '<span class="lumen-notices-badge" id="lumen-notices-badge" hidden style="display: none;"></span>' +
      '</button>' +
      '<div class="lumen-notices-tray" id="lumen-notices-tray" hidden role="region" aria-label="Notices">' +
      '<div class="lumen-notices-tray-header">' +
      '<strong>Notices</strong>' +
      '<a href="' + escapeHtml(decorateMainSiteHref("/notices.html")) + '" class="lumen-notices-all-link">All notices &rarr;</a>' +
      '</div>' +
      '<div class="lumen-notices-tray-body" id="lumen-notices-tray-body">' +
      '<p class="lumen-notices-empty">Loading notices...</p>' +
      '</div>' +
      '</div>' +
      '</div>' +
      '<label class="lumen-theme-control"><span>Theme</span><select id="lumen-theme-select" aria-label="Choose site colour theme"><option value="auto">Auto</option><option value="dark">Dark</option><option value="light">Light</option><option value="high-contrast">High contrast</option><option value="2077">2077</option></select></label>' +
      '<button class="hamburger" id="hamburger" type="button" aria-label="Open navigation menu" aria-controls="navLinks" aria-expanded="false"><span></span><span></span><span></span></button>' +
      '</div>' +
      '<ul class="nav-links" id="navLinks">' +
      '<li><a class="lumen-nav-install-cta" id="lumen-nav-install-cta" href="' + escapeHtml(decorateMainSiteHref("/guide.html")) + '"><span class="lumen-nav-install-cta-label">' + escapeHtml(ctaLabel) + '</span>' + ctaPlatformHtml + '</a></li>' +
      '<li><a href="' + escapeHtml(decorateMainSiteHref("/firmware.html?view=software")) + '">Software Updates</a></li>' +
      '<li><a href="' + escapeHtml(decorateMainSiteHref("/firmware.html?view=firmware")) + '">Firmware Downloads</a></li>' +
      '<li><a href="' + escapeHtml(decorateCrossDomainHref("https://themes.innioasis.app/")) + '" data-cross-site-link="1">Themes</a></li>' +
      '</ul>' +
      '</div>' +
      '</nav>';
  }

  /* One sticky header per page: the gallery bar wins where it exists. */
  var stickyNav = root ? root.querySelector("nav") : null;
  if (stickyNav && !document.querySelector(".gallery-topbar")) stickyNav.classList.add("site-sticky");

  /* Site Switcher Dropdown Logic */
  var switcherToggle = document.getElementById("lumen-site-switcher-toggle");
  var switcherTray = document.getElementById("lumen-site-switcher-tray");
  function setSwitcherOpen(open) {
    if (!switcherToggle || !switcherTray) return;
    if (open) {
      setNoticesOpen(false);
      setMenuOpen(false);
    }
    switcherTray.hidden = !open;
    switcherToggle.setAttribute("aria-expanded", open ? "true" : "false");
    if (open) adjustSwitcherTrayPosition();
  }

  /* The switcher tray is absolutely positioned inside the sticky nav. Place
     it from the toggle's real rectangle so a long translated brand name can
     never push the tray past the viewport edge. */
  function adjustSwitcherTrayPosition() {
    if (!switcherTray || !switcherToggle) return;
    var navEl = switcherToggle.closest("nav");
    if (!navEl) return;
    var navRect = navEl.getBoundingClientRect();
    var rect = switcherToggle.getBoundingClientRect();
    var viewportW = window.innerWidth || document.documentElement.clientWidth || 320;
    var width = Math.min(352, viewportW - 24);
    var left = Math.round(rect.left - navRect.left - 12);
    left = Math.max(8, Math.min(left, navEl.clientWidth - width - 8));
    var top = Math.round(rect.bottom - navRect.top + 8);
    switcherTray.style.position = "absolute";
    switcherTray.style.top = top + "px";
    switcherTray.style.left = left + "px";
    switcherTray.style.right = "auto";
    switcherTray.style.width = width + "px";
    switcherTray.style.maxWidth = "calc(100vw - 24px)";
    switcherTray.style.maxHeight = Math.max(160, window.innerHeight - rect.bottom - 24) + "px";
    switcherTray.style.overflowY = "auto";
  }
  if (switcherToggle && switcherTray) {
    switcherToggle.addEventListener("click", function (e) {
      e.preventDefault();
      e.stopPropagation();
      setNoticesOpen(false);
      setSwitcherOpen(switcherTray.hidden);
    });
  }

  /* Notices Bell Logic */
  var noticesBtn = document.getElementById("lumen-notices-btn");
  var noticesTray = document.getElementById("lumen-notices-tray");
  var noticesBadge = document.getElementById("lumen-notices-badge");
  var noticesBody = document.getElementById("lumen-notices-tray-body");

  /* The nav uses backdrop-filter, which makes it the containing block for
     position: fixed descendants. Move the notices tray to the body so its
     viewport coordinates (set below) mean what they say. */
  if (noticesTray && noticesTray.parentNode !== document.body) {
    document.body.appendChild(noticesTray);
  }

  function adjustNoticesTrayPosition() {
    if (!noticesTray || !noticesBtn) return;
    var rect = noticesBtn.getBoundingClientRect();
    var navEl = noticesBtn.closest("nav") || noticesBtn.closest(".navbar") || noticesBtn.closest(".nav-container");
    var navBottom = navEl ? navEl.getBoundingClientRect().bottom : rect.bottom;
    var topPos = Math.round(Math.max(rect.bottom + 8, navBottom + 6));

    var dockEl = document.getElementById("y1-site-dock-bar") || document.getElementById("support-toolbar-container") || document.querySelector(".y1-site-dock-wrap") || document.querySelector(".y1-site-dock-bar");
    var viewportH = window.innerHeight || document.documentElement.clientHeight || 600;
    var dockTop = (dockEl && !dockEl.hidden) ? dockEl.getBoundingClientRect().top : (viewportH - 80);
    var maxTrayBottom = Math.min(dockTop - 12, viewportH - 84);
    var maxAvailableHeight = Math.max(140, Math.floor(maxTrayBottom - topPos));

    noticesTray.style.position = "fixed";
    noticesTray.style.top = topPos + "px";
    noticesTray.style.maxHeight = maxAvailableHeight + "px";
    noticesTray.style.overflowY = "auto";
    noticesTray.style.webkitOverflowScrolling = "touch";

    if (window.innerWidth <= 640) {
      noticesTray.style.left = "12px";
      noticesTray.style.right = "12px";
      noticesTray.style.width = "auto";
      noticesTray.style.maxWidth = "calc(100% - 24px)";
      return;
    }

    var trayWidth = Math.min(360, window.innerWidth - 24);
    var bellCenter = rect.left + (rect.width / 2);
    var desiredLeft = Math.round(bellCenter - (trayWidth / 2));
    desiredLeft = Math.max(12, Math.min(desiredLeft, window.innerWidth - trayWidth - 12));

    noticesTray.style.left = desiredLeft + "px";
    noticesTray.style.right = "auto";
    noticesTray.style.width = trayWidth + "px";
    noticesTray.style.maxWidth = "calc(100% - 24px)";
  }

  function setNoticesOpen(open) {
    if (!noticesBtn || !noticesTray) return;
    if (open) {
      setSwitcherOpen(false);
      setMenuOpen(false);
    }
    noticesTray.hidden = !open;
    noticesBtn.setAttribute("aria-expanded", open ? "true" : "false");
    if (open) {
      adjustNoticesTrayPosition();
      noticesTray.scrollTop = 0;
      if (noticesBadge) {
        try {
          var ids = (noticesTray.getAttribute("data-notice-ids") || "").split(",").filter(Boolean);
          if (ids.length) localStorage.setItem("y1_seen_notices", ids.join(","));
        } catch (_) {}
        noticesBadge.textContent = "";
        noticesBadge.hidden = true;
        noticesBadge.style.display = "none";
      }
    }
  }

  window.addEventListener("resize", function () {
    if (noticesTray && !noticesTray.hidden) adjustNoticesTrayPosition();
    if (switcherTray && !switcherTray.hidden) adjustSwitcherTrayPosition();
  });
  window.addEventListener("scroll", function () {
    if (noticesTray && !noticesTray.hidden) adjustNoticesTrayPosition();
    if (switcherTray && !switcherTray.hidden) adjustSwitcherTrayPosition();
  }, { passive: true });

  if (noticesBtn && noticesTray) {
    noticesBtn.addEventListener("click", function (e) {
      e.preventDefault();
      e.stopPropagation();
      setSwitcherOpen(false);
      setNoticesOpen(noticesTray.hidden);
    });
  }

  /* Minimal, safe Markdown for a notice's <full_content>: images, headings, lists,
     quotes, fenced code, rules, bold, italic, inline code and https links/images.
     The text is escaped before anything is added, so a notice can never
     inject markup or script into the page. */
  function renderNoticeMarkdown(source) {
    var text = String(source == null ? "" : source).replace(/\r\n?/g, "\n").trim();
    if (!text) return "";
    function esc(s) {
      return s.replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;").replace(/'/g, "&#39;");
    }
    function inline(s) {
      var out = esc(s);
      out = out.replace(/`([^`]+)`/g, "<code>$1</code>");
      out = out.replace(/!\[([^\]]*)\]\((https?:\/\/[^\s)]+)\)/g, function (m, alt, src) {
      return '<img src="' + src + '" alt="' + alt + '" loading="lazy" decoding="async" class="notice-image">';
    });
    out = out.replace(/\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>');
      out = out.replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>");
      out = out.replace(/__([^_]+)__/g, "<strong>$1</strong>");
      out = out.replace(/(^|[\s(])\*([^*\n]+)\*/g, "$1<em>$2</em>");
      out = out.replace(/(^|[\s(])_([^_\n]+)_/g, "$1<em>$2</em>");
      return out;
    }
    var lines = text.split("\n");
    var html = [];
    var para = [];
    var i = 0;
    function flush() {
      if (!para.length) return;
      html.push("<p>" + para.map(inline).join("<br>") + "</p>");
      para = [];
    }
    while (i < lines.length) {
      var line = lines[i];
      if (/^\s*```/.test(line)) {
        flush();
        var code = [];
        i += 1;
        while (i < lines.length && !/^\s*```/.test(lines[i])) { code.push(lines[i]); i += 1; }
        i += 1;
        html.push("<pre><code>" + esc(code.join("\n")) + "</code></pre>");
        continue;
      }
      if (!line.trim()) { flush(); i += 1; continue; }
      var heading = line.match(/^(#{1,6})\s+(.*)$/);
      if (heading) {
        flush();
        var level = Math.min(6, heading[1].length + 1);
        html.push("<h" + level + ">" + inline(heading[2]) + "</h" + level + ">");
        i += 1;
        continue;
      }
      if (/^\s*(-{3,}|\*{3,}|_{3,})\s*$/.test(line)) { flush(); html.push("<hr>"); i += 1; continue; }
      if (/^\s*>\s?/.test(line)) {
        flush();
        var quote = [];
        while (i < lines.length && /^\s*>\s?/.test(lines[i])) { quote.push(lines[i].replace(/^\s*>\s?/, "")); i += 1; }
        html.push("<blockquote>" + quote.map(inline).join("<br>") + "</blockquote>");
        continue;
      }
      if (/^\s*([-*+]|\d+[.)])\s+/.test(line)) {
        flush();
        var ordered = /^\s*\d+[.)]\s+/.test(line);
        var items = [];
        while (i < lines.length && /^\s*([-*+]|\d+[.)])\s+/.test(lines[i])) {
          items.push(lines[i].replace(/^\s*([-*+]|\d+[.)])\s+/, ""));
          i += 1;
        }
        var tag = ordered ? "ol" : "ul";
        html.push("<" + tag + ">" + items.map(function (item) { return "<li>" + inline(item) + "</li>"; }).join("") + "</" + tag + ">");
        continue;
      }
      para.push(line);
      i += 1;
    }
    flush();
    return html.join("\n");
  }

  /* Every notice has its own page, so "read more" never dumps the visitor on
     the site root. A notice whose <url>/<link> is just the bare site is
     treated as having no destination. */
  function noticeIsBareSiteUrl(raw) {
    if (!raw) return true;
    try {
      var url = new URL(raw, window.location.origin);
      if (!/(^|\.)innioasis\.app$/i.test(url.hostname)) return false;
      return !url.pathname.replace(/\//g, "") && !url.search && !url.hash;
    } catch (_) {
      return true;
    }
  }

  function noticeDetailHref(id) {
    var path = "/notices.html?notice=" + encodeURIComponent(String(id || ""));
    try {
      if (typeof decorateMainSiteHref === "function") return decorateMainSiteHref(path);
    } catch (_) {}
    return path;
  }

  window.y1NoticeMarkdown = renderNoticeMarkdown;
  window.y1NoticeIsBareUrl = noticeIsBareSiteUrl;
  window.y1NoticeDetailHref = noticeDetailHref;

  function parseNoticesXml(xmlText) {
    if (!xmlText || !xmlText.trim()) return [];
    try {
      var parser = new DOMParser();
      var doc = parser.parseFromString(xmlText, "application/xml");
      var errorNode = doc.querySelector("parsererror");
      if (errorNode) return [];
      var nodes = doc.querySelectorAll("notice");
      var list = [];
      nodes.forEach(function (n) {
        var textOf = function (tag) {
          var el = n.querySelector(tag);
          return el && el.textContent ? el.textContent.trim() : "";
        };
        list.push({
          id: n.getAttribute("id") || "",
          type: n.getAttribute("type") || n.getAttribute("severity") || "info",
          date: n.getAttribute("date") || n.getAttribute("from") || "",
          from: n.getAttribute("from") || n.getAttribute("date") || "",
          until: n.getAttribute("until") || "",
          persistent: (n.getAttribute("persistent") || "").toLowerCase() === "true",
          models: n.getAttribute("models") || "",
          deviceType: n.getAttribute("device_type") || "",
          firmwareRepo: n.getAttribute("firmware_repo") || "",
          firmwareVersion: n.getAttribute("firmware_version") || "",
          title: textOf("title"),
          summary: textOf("summary") || textOf("content") || textOf("body"),
          link: textOf("url") || textOf("link"),
          fullContent: textOf("full_content") || textOf("content") || textOf("body")
        });
      });
      return list;
    } catch (_) {
      return [];
    }
  }

  /* ---- Contextual notices ---------------------------------------------------
     One feed, two jobs. The bell tray and the Notices page list every current
     notice with no filtering, so those views always show what everyone was
     told. A page that knows what the visitor is looking at (device model,
     hardware type, software repo, release tag) puts the same id on a slot and
     the card below shows exactly ONE notice at a time, rotating through the
     notices that both match the current context and deserve to interrupt the
     release list: a warning-level notice (or worse) that names the firmware
     or the release it is about. Broadcasts and info notices stay in the bell
     tray and on the notices page. See the specification in notice.xml. */
  var noticeFeed = [];
  var noticeContext = {};
  var noticeCard = null;
  var noticeRotateMs = 9000;
  var noticeSeverityRank = { critical: 3, warning: 2, severe: 2, alert: 2, info: 1 };
  /* Severities the inline firmware-directory card may show. */
  var noticeCardSeverities = { critical: true, warning: true, severe: true, alert: true };

  function noticeSplit(value) {
    return String(value == null ? "" : value).split(",").map(function (part) {
      return part.trim();
    }).filter(Boolean);
  }
  function noticeIsAny(value) {
    var text = String(value == null ? "" : value).trim();
    return !text || text === "*";
  }
  function noticeRepoKey(value) {
    return String(value == null ? "" : value).trim().toLowerCase()
      .replace(/^https?:\/\/(www\.)?github\.com\//, "")
      .replace(/\.git$/, "")
      .replace(/\/+$/, "");
  }
  function noticeVersionKey(value) {
    return String(value == null ? "" : value).trim().toLowerCase().replace(/^v(?=\d)/, "");
  }
  function noticeVersionMatches(pattern, version) {
    var want = noticeVersionKey(pattern);
    var have = noticeVersionKey(version);
    if (!want || want === "*") return true;
    if (!have) return false;
    if (want.indexOf("*") === -1) return want === have;
    var rx = new RegExp("^" + want.replace(/[.+?^${}()|[\]\\]/g, "\\$&").replace(/\*/g, ".*") + "$");
    return rx.test(have);
  }
  function noticeListMatches(raw, value, compare) {
    if (noticeIsAny(raw)) return true;
    if (!value) return false;
    return noticeSplit(raw).some(function (entry) {
      return noticeIsAny(entry) || compare(entry, value);
    });
  }
  function noticeModelEquals(a, b) {
    return String(a).toUpperCase() === String(b).toUpperCase();
  }

  /* Fail closed: a dimension the context does not know cannot satisfy a
     notice that declares it. */
  function noticeMatches(notice, context) {
    var ctx = context || {};
    return noticeListMatches(notice.models, ctx.model, noticeModelEquals) &&
      noticeListMatches(notice.deviceType, ctx.deviceType, noticeModelEquals) &&
      noticeListMatches(notice.firmwareRepo, ctx.repo, function (a, b) { return noticeRepoKey(a) === noticeRepoKey(b); }) &&
      noticeListMatches(notice.firmwareVersion, ctx.version, noticeVersionMatches);
  }

  function noticeHasTargeting(notice) {
    return !noticeIsAny(notice.models) || !noticeIsAny(notice.deviceType) ||
      !noticeIsAny(notice.firmwareRepo) || !noticeIsAny(notice.firmwareVersion);
  }

  function noticeTargetLabel(notice) {
    var bits = [];
    if (!noticeIsAny(notice.models)) bits.push(noticeSplit(notice.models).join(", ").toUpperCase());
    if (!noticeIsAny(notice.deviceType)) bits.push("Type " + noticeSplit(notice.deviceType).join(", ").toUpperCase());
    if (!noticeIsAny(notice.firmwareRepo)) bits.push(noticeSplit(notice.firmwareRepo).map(function (repo) {
      var parts = String(repo).split("/");
      return parts[parts.length - 1];
    }).join(", "));
    if (!noticeIsAny(notice.firmwareVersion)) bits.push(noticeSplit(notice.firmwareVersion).join(", "));
    return bits.join(" · ");
  }

  function noticeToday() {
    var now = new Date();
    var pad = function (n) { return (n < 10 ? "0" : "") + n; };
    return now.getFullYear() + "-" + pad(now.getMonth() + 1) + "-" + pad(now.getDate());
  }
  function noticeIsActive(notice, today) {
    var day = today || noticeToday();
    if (notice.from && String(notice.from).slice(0, 10) > day) return false;
    if (notice.until && String(notice.until).slice(0, 10) < day) return false;
    return true;
  }
  function noticeRank(a, b) {
    var weight = (noticeSeverityRank[String(b.type || "").toLowerCase()] || 1) -
      (noticeSeverityRank[String(a.type || "").toLowerCase()] || 1);
    if (weight) return weight;
    var dateA = String(a.date || "").slice(0, 10);
    var dateB = String(b.date || "").slice(0, 10);
    if (dateA !== dateB) return dateA < dateB ? 1 : -1;
    return String(a.id) < String(b.id) ? -1 : 1;
  }
  function noticeEligible(context) {
    var ctx = context || noticeContext;
    var today = noticeToday();
    return noticeFeed.filter(function (notice) {
      return noticeIsActive(notice, today) && noticeMatches(notice, ctx);
    }).sort(noticeRank);
  }

  /* A notice belongs on the inline card only when it names the firmware or
     the release it is about, so a broadcast never lands beside a release
     list it says nothing about. */
  function noticeNamesFirmware(notice) {
    return !noticeIsAny(notice.firmwareRepo) || !noticeIsAny(notice.firmwareVersion);
  }

  /* What the inline card shows: warning or worse, naming a firmware or a
     specific release, and matching the reader's current context. */
  function noticeCardEligible(context) {
    return noticeEligible(context).filter(function (notice) {
      return noticeCardSeverities[String(notice.type || "").toLowerCase()] === true && noticeNamesFirmware(notice);
    });
  }

  function noticeCardMarkup(notice, index, total) {
    var severity = String(notice.type || "info").toLowerCase();
    var target = noticeTargetLabel(notice);
    var detail = noticeDetailHref(notice.id);
    var pageUrl = (notice.link && !noticeIsBareSiteUrl(notice.link)) ? notice.link : "";
    var dots = "";
    if (total > 1) {
      var buttons = [];
      for (var i = 0; i < total; i++) {
        buttons.push('<button type="button" class="lumen-context-dot' + (i === index ? " is-active" : "") +
          '" data-notice-index="' + i + '" aria-label="Show notice ' + (i + 1) + ' of ' + total + '"' +
          (i === index ? ' aria-current="true"' : "") + '></button>');
      }
      dots = '<div class="lumen-context-dots" role="group" aria-label="Notices">' + buttons.join("") + '</div>';
    }
    return '<div class="lumen-context-head">' +
      '<span class="lumen-context-kicker">Notice' + (total > 1 ? " " + (index + 1) + "/" + total : "") + '</span>' +
      '<span class="lumen-context-severity">' + escapeHtml(severity.toUpperCase()) + '</span>' +
      (target ? '<span class="lumen-context-target">' + escapeHtml(target) + '</span>' : '') +
      '<a class="lumen-context-all" href="' + escapeHtml(decorateMainSiteHref("/notices.html")) + '">All notices &rarr;</a>' +
      '</div>' +
      '<p class="lumen-context-title"><a href="' + escapeHtml(detail) + '">' + escapeHtml(notice.title || "Notice") + '</a></p>' +
      (notice.summary ? '<p class="lumen-context-summary">' + escapeHtml(notice.summary) + '</p>' : "") +
      ((dots || pageUrl)
        ? '<div class="lumen-context-foot">' + dots +
          (pageUrl ? '<a class="lumen-context-link" href="' + escapeHtml(pageUrl) + '" target="_blank" rel="noopener noreferrer">Open linked page</a>' : "") +
          '</div>'
        : "");
  }

  function clearNoticeTimer() {
    if (noticeCard && noticeCard.timer) {
      clearTimeout(noticeCard.timer);
      noticeCard.timer = null;
    }
  }
  function scheduleNoticeRotation() {
    if (!noticeCard) return;
    clearNoticeTimer();
    if (noticeCard.paused) return;
    if (!noticeCard.items || noticeCard.items.length < 2) return;
    if (window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;
    noticeCard.timer = window.setTimeout(function () {
      noticeCardShow(noticeCard.index + 1, false);
    }, noticeRotateMs);
  }
  function noticeCardShow(index, manual) {
    if (!noticeCard) return;
    var items = noticeCard.items || [];
    var el = noticeCard.el;
    if (!items.length) {
      el.innerHTML = "";
      el.hidden = true;
      clearNoticeTimer();
      return;
    }
    el.hidden = false;
    if (index < 0) index = items.length - 1;
    if (index >= items.length) index = 0;
    noticeCard.index = index;
    var notice = items[index];
    el.setAttribute("data-severity", String(notice.type || "info").toLowerCase());
    function paint() {
      el.innerHTML = noticeCardMarkup(notice, index, items.length);
      el.classList.remove("is-fading");
    }
    clearTimeout(noticeCard.fadeTimer);
    if (manual) {
      paint();
    } else {
      el.classList.add("is-fading");
      noticeCard.fadeTimer = window.setTimeout(paint, 140);
    }
    scheduleNoticeRotation();
  }
  function renderNoticeCard(freshIds) {
    if (!noticeCard) return;
    var previous = noticeCard.items && noticeCard.items[noticeCard.index];
    var items = noticeCardEligible();
    if (freshIds && freshIds.length) {
      /* A notice that just became relevant (the visitor picked Y2, or Rockbox)
         is what they should see next, not whatever was already on screen. */
      items.sort(function (a, b) {
        var freshA = freshIds.indexOf(a.id) === -1 ? 1 : 0;
        var freshB = freshIds.indexOf(b.id) === -1 ? 1 : 0;
        return freshA - freshB || noticeRank(a, b);
      });
    }
    var key = items.map(function (notice) { return notice.id; }).join("|");
    var unchanged = key === noticeCard.key;
    noticeCard.items = items;
    if (unchanged && !(freshIds && freshIds.length)) return;
    noticeCard.key = key;
    if (!items.length) {
      noticeCardShow(0, true);
      return;
    }
    var targetIndex = 0;
    var i;
    if (freshIds && freshIds.length) {
      for (i = 0; i < items.length; i++) {
        if (freshIds.indexOf(items[i].id) !== -1) { targetIndex = i; break; }
      }
    } else if (previous) {
      for (i = 0; i < items.length; i++) {
        if (items[i].id === previous.id) { targetIndex = i; break; }
      }
    }
    noticeCardShow(targetIndex, false);
  }
  function pauseNoticeCard() {
    if (!noticeCard) return;
    noticeCard.paused = true;
    clearNoticeTimer();
  }
  function resumeNoticeCard() {
    if (!noticeCard) return;
    noticeCard.paused = false;
    scheduleNoticeRotation();
  }
  function bindNoticeCard(el) {
    el.addEventListener("click", function (event) {
      var dot = event.target && event.target.closest ? event.target.closest("[data-notice-index]") : null;
      if (!dot) return;
      event.preventDefault();
      pauseNoticeCard();
      noticeCardShow(parseInt(dot.getAttribute("data-notice-index"), 10) || 0, true);
    });
    el.addEventListener("pointerenter", pauseNoticeCard);
    el.addEventListener("pointerleave", resumeNoticeCard);
    el.addEventListener("focusin", pauseNoticeCard);
    el.addEventListener("focusout", function (event) {
      if (!el.contains(event.relatedTarget)) resumeNoticeCard();
    });
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) pauseNoticeCard();
      else if (!el.contains(document.activeElement)) resumeNoticeCard();
    });
  }

  function mountNoticeCard() {
    var el = document.getElementById("lumen-context-notice");
    if (!el || noticeCard) return noticeCard;
    noticeCard = { el: el, items: [], index: 0, timer: null, fadeTimer: null, paused: false, key: "" };
    bindNoticeCard(el);
    var stored = window.INNIOASIS_NOTICE_CONTEXT;
    if (stored && typeof stored === "object") {
      Object.keys(stored).forEach(function (key) {
        var value = stored[key];
        if (value !== undefined && value !== null && value !== "") noticeContext[key] = value;
      });
    }
    renderNoticeCard([]);
    return noticeCard;
  }

  /* A page calls this whenever the viewer's selection changes. Dimensions left
     empty are forgotten, so a stale repo cannot keep a notice alive. */
  function setNoticeContext(patch) {
    var before = noticeCardEligible().map(function (notice) { return notice.id; });
    Object.keys(patch || {}).forEach(function (key) {
      var value = patch[key];
      if (value === undefined || value === null || value === "") delete noticeContext[key];
      else noticeContext[key] = value;
    });
    window.INNIOASIS_NOTICE_CONTEXT = {};
    Object.keys(noticeContext).forEach(function (key) {
      window.INNIOASIS_NOTICE_CONTEXT[key] = noticeContext[key];
    });
    var eligible = noticeCardEligible();
    var fresh = eligible.filter(function (notice) { return before.indexOf(notice.id) === -1; })
      .map(function (notice) { return notice.id; });
    if (!noticeCard) mountNoticeCard();
    renderNoticeCard(fresh);
    return { eligible: eligible, fresh: fresh };
  }

  window.InnioasisNotices = {
    setContext: setNoticeContext,
    getContext: function () {
      var copy = {};
      Object.keys(noticeContext).forEach(function (key) { copy[key] = noticeContext[key]; });
      return copy;
    },
    getNotices: function () { return noticeFeed.slice(); },
    eligible: function (context) { return noticeEligible(context); },
    matches: noticeMatches,
    isTargeted: noticeHasTargeting,
    refresh: function () {
      if (!noticeCard) mountNoticeCard();
      else renderNoticeCard([]);
    }
  };

  var noticesLoaded = false;
  function loadCommunityNotices() {
    if (noticesLoaded || !noticesBody) return;
    /* One feed only: /notice.xml. The plural spelling used to sit in this
       list as a fallback, so a stray plural feed could silently win. */
    /* The repository copy is read first and the site's own copy only as a
       fallback, so a page view does not count against this domain. */
    var candidates = [
      "https://raw.githubusercontent.com/y1-community/Innioasis-Updater/main/notice.xml",
      "/notice.xml",
      "notice.xml",
      "https://innioasis.app/notice.xml"
    ];
    var idx = 0;
    function tryFetch() {
      if (idx >= candidates.length) {
        noticesBody.innerHTML = '<p class="lumen-notices-empty">No notices at this time.</p>';
        if (noticesBadge) {
          noticesBadge.textContent = "";
          noticesBadge.hidden = true;
          noticesBadge.style.display = "none";
        }
        return;
      }
      var target = candidates[idx++];
      fetch(target, { cache: "no-cache" })
        .then(function (res) {
          if (!res.ok) throw new Error("HTTP " + res.status);
          return res.text();
        })        .then(function (xmlText) {
          var items = parseNoticesXml(xmlText);

          if (!items || !items.length) {
            tryFetch();
            return;
          }
          noticesLoaded = true;
          var seenIds = (localStorage.getItem("y1_seen_notices") || "").split(",").filter(Boolean);
          var allIds = [];
          var unreadCount = 0;

          var html = items.map(function (item) {
            if (item.id) {
              allIds.push(item.id);
              if (seenIds.indexOf(item.id) === -1) unreadCount++;
            }
            var typeTag = (item.type || "INFO").toUpperCase();
            /* The tray is the unfiltered view: every current notice is listed
               whatever its targeting, with its targets named so a reader can
               tell who it was written for. */
            var targetLabel = noticeTargetLabel(item);
            var modelsBadge = targetLabel
              ? '<span class="lumen-notice-models">' + escapeHtml(targetLabel) + '</span>'
              : '';
            /* The tray opens the notice itself. A notice that only points at
               the bare site has no page of its own to send anyone to. */
            var detailHref = item.id ? noticeDetailHref(item.id) : "";
            var linkHtml = detailHref
              ? '<a class="lumen-notice-link" href="' + escapeHtml(detailHref) + '">Read more &rarr;</a>'
              : '';
            /* The card carries the whole notice, Markdown and images included,
               in its own scroll box so a long warning stays readable in place. */
            var fullHtml = renderNoticeMarkdown(item.fullContent || item.summary || "");
            var pageUrl = (item.link && !noticeIsBareSiteUrl(item.link)) ? item.link : "";
            var openHtml = pageUrl
              ? '<a class="lumen-notice-open" href="' + escapeHtml(pageUrl) + '" target="_blank" rel="noopener noreferrer" title="Open the linked page" aria-label="Open the linked page">' +
                '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9"></circle><path d="M3 12h18"></path><path d="M12 3c2.5 2.4 3.9 5.5 3.9 9S14.5 18.6 12 21c-2.5-2.4-3.9-5.5-3.9-9S9.5 5.4 12 3Z"></path></svg></a>'
              : "";
            return (
              '<article class="lumen-notice-card lumen-notice-card--' + escapeHtml(item.type) + '">' +
              '<div class="lumen-notice-meta">' +
              '<span class="lumen-notice-type">' + escapeHtml(typeTag) + '</span>' +
              modelsBadge +
              (item.date ? '<time class="lumen-notice-date">' + escapeHtml(item.date) + '</time>' : '') +
              '</div>' +
              '<h4 class="lumen-notice-title">' + escapeHtml(item.title) + '</h4>' +
              '<div class="lumen-notice-full">' + fullHtml + '</div>' +
              ((linkHtml || openHtml) ? '<div class="lumen-notice-actions">' + linkHtml + openHtml + '</div>' : '') +
              '</article>'
            );
          }).join("");

          if (window.location.pathname.endsWith("/notices.html") || window.location.pathname.endsWith("/notices")) {
            try {
              if (allIds.length) localStorage.setItem("y1_seen_notices", allIds.join(","));
              unreadCount = 0;
            } catch (_) {}
          }

          noticeFeed = items;
          mountNoticeCard();
          try {
            document.dispatchEvent(new CustomEvent("innioasis:notices", { detail: items }));
          } catch (_) {}
          noticesBody.innerHTML = html;
          noticesTray.setAttribute("data-notice-ids", allIds.join(","));
          if (noticesBadge) {
            if (unreadCount > 0) {
              noticesBadge.textContent = String(unreadCount);
              noticesBadge.hidden = false;
              noticesBadge.style.display = "flex";
            } else {
              noticesBadge.textContent = "";
              noticesBadge.hidden = true;
              noticesBadge.style.display = "none";
            }
          }
        })
        .catch(function () {
          tryFetch();
        });
    }
    tryFetch();
  }
  loadCommunityNotices();

  /* Global dismissal when clicking outside switcher or notices trays */
  document.addEventListener("click", function (e) {
    if (switcherTray && !switcherTray.hidden) {
      if (!switcherTray.contains(e.target) && !switcherToggle.contains(e.target)) {
        setSwitcherOpen(false);
      }
    }
    if (noticesTray && !noticesTray.hidden) {
      if (!noticesTray.contains(e.target) && !noticesBtn.contains(e.target)) {
        setNoticesOpen(false);
      }
    }
  });

  /* Appearance control. The shell owns storage, the shared cookie and the
     system-preference listener; this wires the header select to it. */
  var themeSelect = document.getElementById("lumen-theme-select");
  function resolveEffectiveTheme(theme) {
    if (!theme || theme === "auto") {
      try {
        if (window.matchMedia && window.matchMedia("(prefers-color-scheme: light)").matches) return "light";
      } catch (_) {}
      return "dark";
    }
    return (theme === "light" || theme === "high-contrast" || theme === "2077" || theme === "dark") ? theme : "dark";
  }
  function setAppearance(theme) {
    if (typeof window.y1ApplyAppearance === "function") {
      window.y1ApplyAppearance(theme, true);
    } else {
      var effective = resolveEffectiveTheme(theme);
      document.documentElement.setAttribute("data-lumen-theme", effective);
      document.documentElement.setAttribute("data-theme", effective);
      try { localStorage.setItem("lumen-theme", theme); } catch (_) {}
      setSharedCookie("innioasis-theme", theme);
    }
    /* Links already on the page carry the old preference in their URL. */
    if (typeof window.y1DecorateLinks === "function") {
      try { window.y1DecorateLinks(); } catch (_) {}
    }
  }
  if (themeSelect) {
    if (typeof window.y1GetAppearance === "function") themeSelect.value = window.y1GetAppearance();
    themeSelect.addEventListener("change", function () { setAppearance(themeSelect.value); });
  }

  /* Hamburger Toggle for Mobile */
  var menu = document.getElementById("navLinks");
  var hamburger = document.getElementById("hamburger");
  function setMenuOpen(open) {
    if (!menu || !hamburger) return;
    if (open) {
      /* Only one header tray is ever open at a time. */
      setSwitcherOpen(false);
      setNoticesOpen(false);
    }
    menu.classList.toggle("active", open);
    if (open) positionCompactMenu();
    hamburger.classList.toggle("is-active", open);
    hamburger.setAttribute("aria-expanded", open ? "true" : "false");
    hamburger.setAttribute("aria-label", open ? "Close navigation menu" : "Open navigation menu");
  }
  if (hamburger) {
    hamburger.addEventListener("click", function (event) {
      event.stopPropagation();
      setMenuOpen(!menu.classList.contains("active"));
    });
  }
  /* A menu that only closes by tapping a link feels stuck: close it on an
     outside click or Escape too, like the other header trays. */
  document.addEventListener("click", function (event) {
    if (!menu || !menu.classList.contains("active")) return;
    var target = event.target;
    if (target && target.closest && (target.closest("#navLinks") || target.closest("#hamburger"))) return;
    setMenuOpen(false);
  });
  document.addEventListener("keydown", function (event) {
    if (event.key !== "Escape") return;
    if (menu && menu.classList.contains("active")) setMenuOpen(false);
  });
  /* The panel is fixed to the viewport and placed from the button's real
     rectangle, so a header wider than the screen cannot drag it off the edge. */
  function positionCompactMenu() {
    if (!menu || !hamburger) return;
    if (!navShell || !navShell.classList.contains("nav-compact")) return;
    var rect = hamburger.getBoundingClientRect();
    var top = Math.round(rect.bottom + 8);
    menu.style.position = "fixed";
    menu.style.top = top + "px";
    menu.style.left = "auto";
    menu.style.right = Math.max(12, Math.round(window.innerWidth - rect.right)) + "px";
    menu.style.maxHeight = Math.max(180, Math.round(window.innerHeight - top - 16)) + "px";
  }
  window.addEventListener("resize", function () {
    if (menu && menu.classList.contains("active")) positionCompactMenu();
  });
  if (menu) {
    menu.querySelectorAll("a").forEach(function (link) {
      link.addEventListener("click", function () {
        setMenuOpen(false);
      });
    });
  }

  /* Responsive header: as soon as the inline links stop fitting next to the
     brand and the tool buttons, collapse the whole menu into the hamburger.
     Measuring instead of guessing a breakpoint means no link is ever squeezed
     out of the bar, whatever the viewport, font size or translated title. */
  var navShell = document.querySelector("#nav-root .nav-container");
  function navLinksFit(shell) {
    var links = document.getElementById("navLinks");
    var brand = shell.querySelector(".lumen-brand-switcher-wrap");
    var tools = shell.querySelector(".nav-tools");
    if (!links || !brand || !tools) return true;
    var styles = window.getComputedStyle(shell);
    var space = shell.clientWidth - (parseFloat(styles.paddingLeft) || 0) - (parseFloat(styles.paddingRight) || 0);
    var gaps = (parseFloat(styles.columnGap) || 0) * 2;
    /* scrollWidth measures the intrinsic label widths even while the flex
       row is squeezing the anchors, so translated strings that no longer fit
       are caught instead of wrapping silently. */
    var needed = brand.scrollWidth + tools.scrollWidth + links.scrollWidth + gaps;
    return needed <= space + 1;
  }
  function syncNavCompact() {
    if (!navShell) return;
    var wasCompact = navShell.classList.contains("nav-compact");
    if (wasCompact) navShell.classList.remove("nav-compact");
    var compact = !navLinksFit(navShell);
    if (compact) navShell.classList.add("nav-compact");
    if (compact !== wasCompact) setMenuOpen(false);
  }
  var navSyncQueued = false;
  function queueNavSync() {
    if (navSyncQueued) return;
    navSyncQueued = true;
    window.setTimeout(function () {
      navSyncQueued = false;
      syncNavCompact();
    }, 0);
  }
  queueNavSync();
  window.addEventListener("resize", queueNavSync);
  window.addEventListener("orientationchange", queueNavSync);
  window.addEventListener("load", queueNavSync);
  window.addEventListener("site-locale-ready", queueNavSync);
  window.addEventListener("site-locale-change", queueNavSync);
  window.addEventListener("y1-locale-change", queueNavSync);
  /* Translations replace text nodes in place, which does not resize the
     shell. Watch the header text too, so a longer locale still collapses. */
  if (typeof window.MutationObserver === "function" && navShell) {
    new window.MutationObserver(queueNavSync).observe(navShell, {
      childList: true,
      subtree: true,
      characterData: true
    });
  }
  if (document.fonts && document.fonts.ready && typeof document.fonts.ready.then === "function") {
    document.fonts.ready.then(queueNavSync, function () {});
  }
  if (typeof window.ResizeObserver === "function" && navShell) {
    var lastNavBox = "";
    var navResizeObserver = new window.ResizeObserver(function () {
      var brand = navShell.querySelector(".lumen-brand-switcher-wrap");
      var tools = navShell.querySelector(".nav-tools");
      var box = [
        navShell.clientWidth,
        brand ? Math.round(brand.getBoundingClientRect().width) : 0,
        tools ? Math.round(tools.getBoundingClientRect().width) : 0
      ].join("|");
      if (box === lastNavBox) return;
      lastNavBox = box;
      queueNavSync();
    });
    navResizeObserver.observe(navShell);
    var navBrandEl = navShell.querySelector(".lumen-brand-switcher-wrap");
    if (navBrandEl) navResizeObserver.observe(navBrandEl);
    var navToolsEl = navShell.querySelector(".nav-tools");
    if (navToolsEl) navResizeObserver.observe(navToolsEl);
  }
  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      setMenuOpen(false);
      setSwitcherOpen(false);
      setNoticesOpen(false);
    }
  });

  /* Footer Injection */
  var footerRoot = document.getElementById("footer-root");
  if (!footerRoot && document.body && !document.querySelector("footer")) {
    /* Pages that forget the mount point still get a footer. */
    footerRoot = document.createElement("div");
    footerRoot.id = "footer-root";
    var toolbarSlot = document.getElementById("support-toolbar-slot");
    if (toolbarSlot && toolbarSlot.parentNode === document.body) {
      document.body.insertBefore(footerRoot, toolbarSlot);
    } else {
      document.body.appendChild(footerRoot);
    }
  }
  if (footerRoot) {
    footerRoot.innerHTML =
      '<footer class="site-footer ' + (isFirmwarePersona ? "site-footer--firmware" : "site-footer--updater") + '">' +
      '<div class="footer-grid">' +
      '<div class="footer-col">' +
      '<h4>Software &amp; Guides</h4>' +
      '<a href="' + escapeHtml(decorateMainSiteHref("/guide.html")) + '">Installation Guide</a>' +
      '<a href="' + escapeHtml(decorateMainSiteHref("/manuals/index.html")) + '">Player manuals</a>' +
      (isThemesSite
        ? '<a href="' + escapeHtml(decorateMainSiteHref("/firmware.html")) + '">Player Updates and Firmware</a>'
        : '<a href="' + escapeHtml(decorateMainSiteHref("/firmware.html?view=software")) + '">Software Updates</a>' +
          '<a href="' + escapeHtml(decorateMainSiteHref("/firmware.html?view=firmware")) + '">Custom Firmware Downloads</a>'
      ) +
      '<a href="' + escapeHtml(decorateMainSiteHref("/rockbox-benefits.html")) + '">Rockbox on Innioasis</a>' +
      '<a href="' + escapeHtml(decorateMainSiteHref("/reborn-y2linux-benefits.html")) + '">Reborn (Y2Linux) for Y2</a>' +
      '<a href="' + escapeHtml(decorateMainSiteHref("/rondo-benefits.html")) + '">Rondo for Y1</a>' +
      '<a href="' + escapeHtml(decorateMainSiteHref("/updater-comparison.html")) + '">Which tool should I use?</a>' +
      '<a href="' + escapeHtml(decorateMainSiteHref("/troubleshooting.html")) + '">Troubleshooting</a>' +
      '</div>' +
      '<div class="footer-col">' +
      '<h4>Developers</h4>' +
      '<a href="' + escapeHtml(decorateMainSiteHref("/developers.html")) + '">Developer Guide &amp; Tooling</a>' +
      '<a href="' + escapeHtml(decorateCrossDomainHref("https://innioasis.app/")) + '">Updater CE</a>' +
      '<a href="' + escapeHtml(decorateMainSiteHref("/firmware.html")) + '">Firmware Archive</a>' +
      '<a href="' + escapeHtml(decorateCrossDomainHref("https://themes.innioasis.app/")) + '" data-cross-site-link="1">Themes Gallery</a>' +
      '<a href="https://discord.gg/zHrT2zrcek" target="_blank" rel="noopener noreferrer">Discord Server</a>' +
      '<a href="https://reddit.com/r/innioasis" target="_blank" rel="noopener noreferrer">r/innioasis on Reddit</a>' +
      '<a href="https://github.com/y1-community/Innioasis-Updater" target="_blank" rel="noopener noreferrer">Updater CE Source Code</a>' +
      '<a href="' + escapeHtml(decorateMainSiteHref("/credits.html#donate")) + '" data-donations-appeal>Support Independent Projects</a>' +
      '<a href="' + escapeHtml(decorateMainSiteHref("/credits.html")) + '">Credits</a>' +
      '</div>' +
      '</div>' +
      '<div class="footer-bottom"><span class="footer-copyleft">Copyleft - Innioasis and <span translate="no" data-i18n-skip>Ryan Specter</span></span>' +
      '<span class="footer-legal"><a href="' + escapeHtml(decorateMainSiteHref("/about.html")) + '">About &amp; Editorial</a>' +
      '<a href="/privacy.html">Privacy</a>' +
      '<a class="footer-privacy-button" href="/privacy.html#choices">Privacy settings</a></span></div>' +
      '</footer>';
  }

  function escapeHtml(text) {
    var div = document.createElement("div");
    div.textContent = text == null ? "" : String(text);
    return div.innerHTML;
  }
})();