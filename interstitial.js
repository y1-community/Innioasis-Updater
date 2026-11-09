/*
 * Outbound interstitials.
 *
 * Every link that leaves Innioasis passes through leaving.html, except a
 * donation host, which passes through donate.html so the visitor is thanked
 * first. Theme cards' external downloads are buttons that call window.open
 * directly and are excluded here as well. Site preferences (accent, language,
 * appearance, donation and analytics choices) are read from the query by the
 * normal site shell on the interstitial page, then cleared from the address
 * bar; only to/method are removed here.
 */
(function () {
  "use strict";

  var DONATION_HOSTS = /(^|\.)(ko-fi\.com|buymeacoffee\.com|boosty\.to)$/i;
  var METHODS = {
    kofi: "https://ko-fi.com/teamslide",
    bmc: "https://buymeacoffee.com/ryanspecter",
    boosty: "https://boosty.to/ryanspecter"
  };

  function cleanBase() {
    var me = document.currentScript || document.querySelector('script[src*="interstitial.js"]');
    if (me && me.src) return me.src.replace(/[^\/]*$/, "");
    return "";
  }

  function safeUrl(raw) {
    if (!raw) return null;
    try {
      var url = new URL(String(raw), window.location.origin);
      if (url.protocol !== "https:" && url.protocol !== "http:") return null;
      if (/^(javascript|data|blob):/i.test(raw)) return null;
      return url;
    } catch (_) {
      return null;
    }
  }

  function isInternal(url) {
    if (url.origin === window.location.origin) return true;
    return /(^|\.)innioasis\.app$/i.test(url.hostname) || url.hostname === "localhost" || url.hostname === "127.0.0.1";
  }

  function stripInterstitialParams() {
    try {
      var url = new URL(window.location.href);
      url.searchParams.delete("to");
      url.searchParams.delete("url");
      url.searchParams.delete("method");
      window.history.replaceState(null, "", url.pathname + (url.search ? url.search : "") + url.hash);
    } catch (_) {}
  }

  function installGuard() {
    document.addEventListener("click", function (event) {
      if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      var link = event.target && event.target.closest ? event.target.closest("a[href]") : null;
      if (!link) return;
      if (link.hasAttribute("download") || link.hasAttribute("data-no-interstitial")) return;
      if (link.closest(".theme-card, [data-card-download], [data-direct-install-btn]")) return;
      var url = safeUrl(link.getAttribute("href"));
      if (!url || isInternal(url)) return;
      if (/\.(zip|7z|tar|gz|theme|rbtheme|apk|dmg|exe|msi)$/i.test(url.pathname)) return;

      var page = DONATION_HOSTS.test(url.hostname) ? "donate.html" : "leaving.html";
      var target = cleanBase() + page + "?to=" + encodeURIComponent(url.href);
      event.preventDefault();
      if (link.target === "_blank") window.open(target, "_blank", "noopener");
      else window.location.href = target;
    }, true);
  }

  function initPage() {
    var kind = document.body ? document.body.getAttribute("data-interstitial") : "";
    var params = new URLSearchParams(window.location.search);
    var method = String(params.get("method") || "").toLowerCase();
    var destination = safeUrl(params.get("to") || params.get("url"));
    if (!destination && method && METHODS[method]) destination = safeUrl(METHODS[method]);

    var hostEl = document.getElementById("interstitial-host");
    var goEl = document.getElementById("interstitial-continue");
    var cancelEl = document.getElementById("interstitial-cancel");

    if (!destination) {
      if (hostEl) hostEl.textContent = "";
      if (goEl) { goEl.hidden = true; }
      var fallback = document.getElementById("interstitial-fallback");
      if (fallback) fallback.hidden = false;
      stripInterstitialParams();
      return;
    }

    if (hostEl) hostEl.textContent = destination.hostname.replace(/^www\./, "");
    if (goEl) goEl.setAttribute("href", destination.href);
    stripInterstitialParams();

    var delay = kind === "donate" ? 2600 : 0;
    if (delay) {
      var left = Math.ceil(delay / 1000);
      var countEl = document.getElementById("interstitial-count");
      if (countEl) countEl.textContent = String(left);
      var timer = setInterval(function () {
        left -= 1;
        if (countEl) countEl.textContent = String(Math.max(left, 0));
        if (left <= 0) {
          clearInterval(timer);
          window.location.replace(destination.href);
        }
      }, 1000);
      if (cancelEl) cancelEl.addEventListener("click", function () { clearInterval(timer); });
    }
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", function () {
      if (document.body && document.body.hasAttribute("data-interstitial")) initPage();
      else installGuard();
    });
  } else {
    if (document.body && document.body.hasAttribute("data-interstitial")) initPage();
    else installGuard();
  }
})();
