/*
 * Download analytics shared by innioasis.app and themes.innioasis.app.
 *
 * Every download pushes one `innioasis_download` event into the Google Tag
 * Manager data layer (container GTM-TNDGC37L, already on every page). The
 * parameters use the Updater CE link contract names, so a download from the
 * app, a firmware row and a theme card read the same in reports:
 *
 *   what            firmware | theme
 *   software        manifest package name, e.g. Rockbox
 *   version         release tag, or "latest"
 *   model           Y1, Y2, ...
 *   brand           Innioasis | Timmkoo
 *   type            A | B (Y1 only)
 *   resolution      240p | 360p
 *   id              theme id/slug when what=theme
 *   action          open | install
 *   client, client_version          set by Updater CE on links it opens
 *   utm_source, utm_medium, utm_campaign, ref   passed through
 *
 * `theme=` is the visitor's colour preference, never a theme id.
 *
 * A theme download that starts on themes.innioasis.app is also handed to
 * innioasis.app: a hidden frame opens /analytics-handoff.html there with the
 * same parameters in its URL, and that page records the event under the
 * innioasis.app hostname. Nothing is sent when the visitor turned analytics
 * off in Privacy settings.
 */
(function (global) {
    "use strict";

    var CONTRACT_KEYS = [
        "what", "software", "version", "model", "brand", "type", "resolution",
        "id", "action", "client", "client_version",
        "utm_source", "utm_medium", "utm_campaign", "ref"
    ];
    /* Who sent the visitor here lasts for the visit, so a download three
       pages after an Updater CE link still credits the app. */
    var STICKY_KEYS = ["client", "client_version", "utm_source", "utm_medium", "utm_campaign", "ref"];
    var SESSION_KEY = "innioasis-download-context";
    var EVENT_NAME = "innioasis_download";
    var LANDING_EVENT = "innioasis_handoff";

    function clean(value) {
        if (value === undefined || value === null) return "";
        return String(value).trim().slice(0, 100);
    }

    function analyticsAllowed() {
        var privacy = global.INNIOASIS_PRIVACY;
        if (privacy && typeof privacy.allows === "function") {
            try { return privacy.allows("analytics"); } catch (_) {}
        }
        return true;
    }

    function queryParams(search) {
        var out = {};
        var params;
        try { params = new URLSearchParams(search == null ? global.location.search : search); } catch (_) { return out; }
        CONTRACT_KEYS.forEach(function (key) {
            var value = clean(params.get(key));
            if (value) out[key] = value;
        });
        return out;
    }

    function storedContext() {
        try {
            var raw = global.sessionStorage.getItem(SESSION_KEY);
            var parsed = raw ? JSON.parse(raw) : null;
            return parsed && typeof parsed === "object" ? parsed : {};
        } catch (_) {
            return {};
        }
    }

    function rememberContext(fromUrl) {
        var context = storedContext();
        var changed = false;
        STICKY_KEYS.forEach(function (key) {
            if (fromUrl[key] && context[key] !== fromUrl[key]) {
                context[key] = fromUrl[key];
                changed = true;
            }
        });
        if (changed) {
            try { global.sessionStorage.setItem(SESSION_KEY, JSON.stringify(context)); } catch (_) {}
        }
        return context;
    }

    var landing = queryParams();
    var context = rememberContext(landing);

    function siteHost() {
        var host = global.location.hostname || "";
        if (host === "localhost" || host === "127.0.0.1") {
            return global.location.port === "8081" ? "themes.innioasis.app" : "innioasis.app";
        }
        return host;
    }

    function isThemesSite() {
        return siteHost() === "themes.innioasis.app";
    }

    function mainSiteOrigin() {
        var host = global.location.hostname;
        if (host === "localhost" || host === "127.0.0.1") {
            return global.location.protocol + "//" + host + ":8080";
        }
        return "https://innioasis.app";
    }

    function buildPayload(params) {
        var payload = { event: EVENT_NAME, download_site: siteHost() };
        Object.keys(context).forEach(function (key) {
            if (context[key]) payload[key] = context[key];
        });
        Object.keys(params || {}).forEach(function (key) {
            var value = clean(params[key]);
            if (value) payload[key] = value;
        });
        if (!payload.page_path) payload.page_path = global.location.pathname;
        return payload;
    }

    function push(payload) {
        global.dataLayer = global.dataLayer || [];
        global.dataLayer.push(payload);
    }

    function handoffQuery(payload, extra) {
        var params = new URLSearchParams();
        CONTRACT_KEYS.forEach(function (key) {
            if (payload[key]) params.set(key, payload[key]);
        });
        Object.keys(extra || {}).forEach(function (key) {
            if (extra[key]) params.set(key, extra[key]);
        });
        return params;
    }

    /* The frame is created only when a download happens and removed once
       its tag has had time to send, so gallery pages carry no extra weight. */
    function handoffToMainSite(payload) {
        if (!document.body) return;
        var params = handoffQuery(payload, {
            utm_source: payload.utm_source || "themes.innioasis.app",
            utm_medium: payload.utm_medium || "referral",
            utm_campaign: payload.utm_campaign || "theme_download",
            ref: payload.ref || ("themes:" + (payload.page_path || "/")),
            file_name: payload.file_name || "",
            download_method: payload.download_method || ""
        });
        var frame = document.createElement("iframe");
        frame.src = mainSiteOrigin() + "/analytics-handoff.html?" + params.toString();
        frame.title = "";
        frame.setAttribute("aria-hidden", "true");
        frame.setAttribute("tabindex", "-1");
        frame.setAttribute("loading", "eager");
        frame.style.cssText = "position:absolute;width:1px;height:1px;border:0;left:-9999px;top:-9999px;visibility:hidden;";
        document.body.appendChild(frame);
        setTimeout(function () {
            if (frame.parentNode) frame.parentNode.removeChild(frame);
        }, 15000);
    }

    function track(params) {
        if (!analyticsAllowed()) return null;
        var payload = buildPayload(params);
        push(payload);
        if (payload.what === "theme" && isThemesSite()) handoffToMainSite(payload);
        return payload;
    }

    /* Adds the contract parameters to a link into the other site, so the
       landing page can credit where the visitor came from. */
    function decorate(href, params) {
        if (!href) return href;
        var url;
        try { url = new URL(href, global.location.href); } catch (_) { return href; }
        var merged = {};
        Object.keys(context).forEach(function (key) { merged[key] = context[key]; });
        Object.keys(params || {}).forEach(function (key) { merged[key] = params[key]; });
        CONTRACT_KEYS.forEach(function (key) {
            var value = clean(merged[key]);
            if (value && !url.searchParams.has(key)) url.searchParams.set(key, value);
        });
        return url.toString();
    }

    /* A visit that arrives with the contract in its URL (from Updater CE or
       from the themes gallery) is recorded once, as the landing. */
    (function recordLanding() {
        if (!landing.what && !landing.client) return;
        if (!analyticsAllowed()) return;
        var payload = buildPayload(landing);
        payload.event = LANDING_EVENT;
        push(payload);
    })();

    global.InnioasisDownloads = {
        keys: CONTRACT_KEYS.slice(),
        context: function () { return buildPayload({}); },
        landing: function () { return JSON.parse(JSON.stringify(landing)); },
        track: track,
        decorate: decorate
    };
})(window);
