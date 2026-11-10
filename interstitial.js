/*
 * Outbound interstitials.
 *
 * A normal website click follows the href in the page. That href is the
 * cross-link Google records, so it is never rewritten to leaving.html or
 * donate.html. Reddit, Discord and donation hosts stay on that direct path:
 * an interstitial in front of them is a noindex hop, and that hop is what
 * drops the outbound link.
 *
 * The app is the exception. It opens the site with ce=true, which the site
 * stores as innioasis-referred-by-ce. Those visits still pass through
 * leaving.html, or donate.html for a donation host, so the visitor is told
 * where they are going. Theme cards' external downloads call window.open
 * directly and are excluded here as well. Site preferences (accent, language,
 * appearance, donation and analytics choices) are read from the query by the
 * normal site shell on the interstitial page, then cleared from the address
 * bar; only to/method are removed here.
 */
(function () {
  "use strict";

  var DONATION_HOSTS = /(^|\.)(ko-fi\.com|buymeacoffee\.com|boosty\.to|paypal\.me|paypal\.com|patreon\.com|revolut\.me|revolut\.com)$/i;
  /* Community profiles the public site links out to. The href on the page is
     the link Google should follow, so a website click is not intercepted. */
  var COMMUNITY_HOSTS = /(^|\.)(reddit\.com|redd\.it|discord\.gg|discord\.com|discordapp\.com)$/i;
  var THANKS = {
    en: "Thank you for supporting us",
    de: "Danke, dass du uns unterstützt",
    es: "Gracias por apoyarnos",
    fr: "Merci de nous soutenir",
    it: "Grazie per il tuo sostegno",
    pt: "Obrigado por nos apoiar",
    "pt-br": "Obrigado por nos apoiar",
    nl: "Bedankt dat je ons steunt",
    pl: "Dziękujemy za wsparcie",
    ru: "Спасибо за поддержку",
    ja: "ご支援ありがとうございます",
    ko: "응원해 주셔서 감사합니다",
    "zh-cn": "感谢你的支持",
    "zh-tw": "感謝你的支持",
    uk: "Дякуємо за підтримку",
    tr: "Bizi desteklediğiniz için teşekkürler",
    ar: "شكرا لدعمك لنا",
    vi: "Cảm ơn bạn đã ủng hộ chúng tôi",
    id: "Terima kasih sudah mendukung kami",
    th: "ขอบคุณที่สนับสนุนเรา",
    sv: "Tack för att du stöttar oss"
  };
  var TAKING = {
    en: "Taking you to",
    de: "Weiter zu",
    es: "Te llevamos a",
    fr: "Redirection vers",
    it: "Ti portiamo su",
    pt: "A caminho de",
    "pt-br": "Levando você para",
    nl: "Je gaat naar",
    pl: "Przechodzimy do",
    ru: "Переходим на",
    ja: "移動しています:",
    ko: "이동 중:",
    "zh-cn": "正在前往",
    "zh-tw": "正在前往",
    uk: "Переходимо на",
    tr: "Yönlendiriliyorsunuz:",
    ar: "جارٍ نقلك إلى",
    vi: "Đang chuyển đến",
    id: "Mengalihkan ke",
    th: "กำลังพาคุณไปที่",
    sv: "Du skickas till"
  };
  /* Which site the visitor is leaving. The naming follows the header switcher:
     the archive, Updater CE and the Themes Gallery are three products on two
     hosts, and a visitor who clicked a Reddit link on a gallery page should not
     be told they are leaving "Innioasis". The app passes ?from=updater-ce so a
     link inside release notes names the app too. */
  var BRANDS = {
    "updater-ce": "Updater CE",
    "themes-gallery": "Themes Gallery",
    "firmware-archive": "Firmware archive"
  };
  var LEAVING = {
    en: "You're leaving {brand}",
    de: "Du verlässt {brand}",
    es: "Vas a salir de {brand}",
    fr: "Vous quittez {brand}",
    it: "Stai lasciando {brand}",
    pt: "Está a sair de {brand}",
    "pt-br": "Você está saindo de {brand}",
    nl: "Je verlaat {brand}",
    pl: "Opuszczasz {brand}",
    ru: "Вы покидаете {brand}",
    ja: "{brand}を離れます",
    ko: "{brand}에서 나갑니다",
    "zh-cn": "你即将离开{brand}",
    "zh-tw": "你即將離開{brand}",
    uk: "Ви залишаєте {brand}",
    tr: "{brand} sitesinden ayrılıyorsunuz",
    ar: "أنت تغادر {brand}",
    vi: "Bạn đang rời {brand}",
    id: "Anda meninggalkan {brand}",
    th: "คุณกำลังออกจาก {brand}",
    sv: "Du lämnar {brand}"
  };
  var METHODS = {
    kofi: "https://ko-fi.com/teamslide",
    bmc: "https://buymeacoffee.com/ryanspecter",
    boosty: "https://boosty.to/ryanspecter"
  };
  var PROVIDERS = {
    kofi: "Ko-fi",
    bmc: "Buy Me a Coffee",
    boosty: "Boosty",
    paypal: "PayPal",
    revolut: "Revolut",
    patreon: "Patreon"
  };

  function brandFor(params) {
    var raw = "";
    try {
      raw = String((params && (params.get("from") || params.get("brand"))) || "").toLowerCase().trim();
    } catch (_) {}
    if (BRANDS[raw]) return BRANDS[raw];
    if (/updater|app|release/.test(raw)) return BRANDS["updater-ce"];
    if (/theme|gallery/.test(raw)) return BRANDS["themes-gallery"];
    if (/archive|firmware|site/.test(raw)) return BRANDS["firmware-archive"];
    var attr = document.body ? document.body.getAttribute("data-interstitial-brand") : "";
    if (attr) return attr;
    if (/^themes\./i.test(window.location.hostname || "")) return BRANDS["themes-gallery"];
    return BRANDS["firmware-archive"];
  }

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

  /* "auth", "login" and "payment" anywhere in the address. A word like
     "author" contains "auth"; that is the innocent case we still refuse,
     because the same letters are how a lookalike login page would be written. */
  function isBlockedRedirect(url) {
    return /payment|login|auth/i.test(url.href);
  }

  function currentFrom() {
    var host = (window.location.hostname || "").toLowerCase();
    if (/^themes\./.test(host)) return "themes-gallery";
    var path = (window.location.pathname || "").toLowerCase();
    if (/firmware|release_view|release-notes|releases/.test(path)) return "firmware-archive";
    return "updater-ce";
  }

  function isInternal(url) {
    if (url.origin === window.location.origin) return true;
    return /(^|\.)innioasis\.app$/i.test(url.hostname) || url.hostname === "localhost" || url.hostname === "127.0.0.1";
  }

  /* Updater CE opens innioasis.app with ce=true. site-init keeps that as
     innioasis-referred-by-ce. Read the same places it writes, because this
     script can run before or after that module. */
  function referredByApp() {
    try {
      if (window.y1Accent && typeof window.y1Accent.referredByCe === "function" && window.y1Accent.referredByCe()) {
        return true;
      }
    } catch (_) {}
    try {
      var params = new URLSearchParams(window.location.search);
      var ce = params.get("ce");
      if (ce !== null && /^(|1|true|yes|on)$/i.test(String(ce).trim())) return true;
      var from = String(params.get("from") || "").toLowerCase();
      if (from === "updater-ce" || from === "app") return true;
    } catch (_) {}
    try {
      var parts = String(document.cookie || "").split(";");
      for (var i = 0; i < parts.length; i++) {
        var part = parts[i].trim();
        if (part.indexOf("innioasis-referred-by-ce=") !== 0) continue;
        var value = decodeURIComponent(part.slice("innioasis-referred-by-ce=".length));
        if (value && value !== "0" && value !== "false") return true;
      }
    } catch (_) {}
    try {
      var stored = window.localStorage.getItem("innioasis-referred-by-ce");
      if (stored && stored !== "0" && stored !== "false") return true;
    } catch (_) {}
    return false;
  }

  function staysDirect(url) {
    if (referredByApp()) return false;
    return DONATION_HOSTS.test(url.hostname) || COMMUNITY_HOSTS.test(url.hostname);
  }

  function stripInterstitialParams() {
    try {
      var url = new URL(window.location.href);
      url.searchParams.delete("to");
      url.searchParams.delete("url");
      url.searchParams.delete("method");
      url.searchParams.delete("from");
      window.history.replaceState(null, "", url.pathname + (url.search ? url.search : "") + url.hash);
    } catch (_) {}
  }

  function installGuard() {
    document.addEventListener("click", function (event) {
      if (event.defaultPrevented || event.button !== 0 || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
      var link = event.target && event.target.closest ? event.target.closest("a[href]") : null;
      if (!link) return;
      if (link.hasAttribute("download") || link.hasAttribute("data-no-interstitial")) return;
      if (link.closest(".theme-card, [data-card-download], [data-direct-install-btn], [data-external-download], [data-theme-download]")) return;
      var url = safeUrl(link.getAttribute("href"));
      if (!url || isInternal(url)) return;
      if (/\.(zip|7z|tar|gz|theme|rbtheme|apk|dmg|exe|msi)$/i.test(url.pathname)) return;
      /* Leave the href alone. A direct click is how the cross-link stays a
         cross-link. App-referred visits still take the interstitial below. */
      if (staysDirect(url)) return;

      var page = DONATION_HOSTS.test(url.hostname) ? "donate.html" : "leaving.html";
      var target = cleanBase() + page + "?from=" + encodeURIComponent(currentFrom()) + "&to=" + encodeURIComponent(url.href);
      event.preventDefault();
      if (link.target === "_blank") window.open(target, "_blank", "noopener");
      else window.location.href = target;
    }, true);
  }

  function providerName(method, url) {
    if (PROVIDERS[method]) return PROVIDERS[method];
    var host = url.hostname.replace(/^www\./, "").toLowerCase();
    if (host === "ko-fi.com" || /\.ko-fi\.com$/.test(host)) return "Ko-fi";
    if (host === "buymeacoffee.com" || /\.buymeacoffee\.com$/.test(host)) return "Buy Me a Coffee";
    if (host === "boosty.to" || /\.boosty\.to$/.test(host)) return "Boosty";
    if (host === "paypal.me" || host === "paypal.com" || /\.paypal\.com$/.test(host)) return "PayPal";
    if (host === "revolut.me" || host === "revolut.com" || /\.revolut\.com$/.test(host)) return "Revolut";
    if (host === "patreon.com" || /\.patreon\.com$/.test(host)) return "Patreon";
    return host;
  }

  function languageFrom(params) {
    var lang = "";
    try {
      lang = (params.get("lang") || "").toLowerCase();
      if (!lang) {
        var cookie = document.cookie.split(";").map(function (part) { return part.trim(); });
        for (var i = 0; i < cookie.length; i++) {
          if (cookie[i].indexOf("innioasis-locale=") === 0) {
            lang = decodeURIComponent(cookie[i].slice(17)).toLowerCase();
          }
        }
      }
    } catch (_) {}
    return lang;
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
    var statusEl = document.getElementById("interstitial-status");
    var fillEl = document.getElementById("interstitial-progress-fill");
    var progressEl = fillEl ? fillEl.closest(".interstitial-progress") : null;

    if (!destination) {
      if (hostEl) hostEl.textContent = "";
      if (goEl) goEl.hidden = true;
      if (statusEl) statusEl.hidden = true;
      if (progressEl) progressEl.hidden = true;
      var fallback = document.getElementById("interstitial-fallback");
      if (fallback) fallback.hidden = false;
      stripInterstitialParams();
      return;
    }

    var hostName = destination.hostname.replace(/^www\./, "");
    var heading = document.querySelector(".interstitial-main h1");
    if (isBlockedRedirect(destination)) {
      var blocked = "To prevent abuse of our redirect interstitial pages for phishing attacks, we've stopped this redirect from happening. This could be for innocent reasons such as \"auth\", \"login\" or \"payment\" appearing in the URL but as these could likely be used as a vector for phishing or social engineering attempts, we will not allow it here.";
      if (heading) heading.textContent = "Redirect stopped";
      document.title = "Redirect stopped - Innioasis";
      var blockedPara = document.querySelector(".interstitial-main p");
      if (blockedPara) blockedPara.textContent = blocked;
      if (hostEl) hostEl.textContent = "";
      if (goEl) goEl.hidden = true;
      if (statusEl) statusEl.hidden = true;
      if (progressEl) progressEl.hidden = true;
      stripInterstitialParams();
      if (cancelEl) {
        cancelEl.addEventListener("click", function () {
          if (window.history.length > 1) window.history.back();
          else window.location.assign("index.html");
        });
      }
      return;
    }

    if (hostEl) hostEl.textContent = hostName;
    if (goEl) goEl.setAttribute("href", destination.href);

    var lang = languageFrom(params);
    var provider = providerName(method, destination);
    if (statusEl) {
      if (kind === "donate") {
        var taking = TAKING[lang] || TAKING[lang.split("-")[0]] || TAKING.en;
        statusEl.textContent = taking + " " + provider + "\u2026";
      } else {
        statusEl.textContent = "Taking you to " + provider + "\u2026";
      }
    }

    if (kind === "donate") {
      if (heading) heading.textContent = THANKS[lang] || THANKS[lang.split("-")[0]] || THANKS.en;
    } else if (heading) {
      var template = LEAVING[lang] || LEAVING[lang.split("-")[0]] || LEAVING.en;
      heading.textContent = template.replace("{brand}", brandFor(params));
      document.title = heading.textContent + " - Innioasis";
    }
    stripInterstitialParams();

    /* Donations leave almost immediately: the bar is the only countdown, and
       the page never sits there counting seconds at the visitor. */
    var delay = kind === "donate" ? 900 : 750;
    if (fillEl) {
      fillEl.style.transitionDuration = delay + "ms";
      requestAnimationFrame(function () {
        requestAnimationFrame(function () {
          fillEl.style.transform = "scaleX(1)";
          if (progressEl) progressEl.setAttribute("aria-valuenow", "100");
        });
      });
    }
    var timer = window.setTimeout(function () {
      window.location.replace(destination.href);
    }, delay);

    if (cancelEl) {
      cancelEl.addEventListener("click", function () {
        window.clearTimeout(timer);
        if (fillEl) {
          fillEl.style.transitionDuration = "0ms";
          fillEl.style.transform = "scaleX(0)";
        }
        if (window.history.length > 1) window.history.back();
        else window.location.assign("index.html");
      });
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
