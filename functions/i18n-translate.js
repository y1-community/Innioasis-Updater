/**
 * Pages Function for /i18n-translate.
 *
 * The locale runtime sends the strings a page cannot get from its catalog.
 * This function answers from a KV cache keyed per string, and only the misses
 * go to a provider — once. That is what makes a second page view free, and
 * what keeps repeat copy from being paid for again by every reader in the
 * same language.
 *
 *   POST /i18n-translate
 *   {"locale":"de","strings":["Skip to content","Terms of use"]}
 *   -> {"translations":["Zum Inhalt springen","Nutzungsbedingungen"],"cached":1,"fetched":1}
 *
 * Bind a KV namespace as I18N_TRANSLATIONS. Without it the function still
 * translates, it just cannot remember. The response is always aligned with
 * the request, with an empty string where a provider gave nothing back, so a
 * caller never paints the wrong sentence into the wrong node.
 *
 * Nothing about the reader is stored: the key is a hash of locale + source
 * string, never an IP, cookie or user agent.
 */

const MAX_BODY = 12000;
const MAX_STRINGS = 60;
const MAX_STRING = 400;
const CACHE_TTL = 60 * 60 * 24 * 60;
const PROVIDER_TIMEOUT = 8000;

function json(status, body, cors) {
  return new Response(JSON.stringify(body) + "\n", {
    status,
    headers: Object.assign(
      { "Content-Type": "application/json; charset=utf-8", "Cache-Control": "no-store" },
      cors || {}
    ),
  });
}

function text(status, message) {
  return new Response(message + "\n", {
    status,
    headers: { "Content-Type": "text/plain; charset=utf-8", "Cache-Control": "no-store" },
  });
}

function clean(value) {
  return String(value == null ? "" : value)
    .replace(/[\u0000-\u001f\u007f]/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, MAX_STRING);
}

function usable(text) {
  if (!text || text.length < 2) return false;
  if (!/[A-Za-z]{2}/.test(text)) return false;
  return true;
}

/* Locale + source string, hashed. The source is never part of the key, so a
   long paragraph does not blow up a KV key and nothing readable is stored. */
async function cacheKey(locale, source) {
  const bytes = new TextEncoder().encode(locale + "\u0000" + source);
  const digest = await crypto.subtle.digest("SHA-256", bytes);
  const hex = Array.from(new Uint8Array(digest))
    .map((byte) => byte.toString(16).padStart(2, "0"))
    .join("");
  return `t:${locale}:${hex.slice(0, 32)}`;
}

function listFromClients5(payload, count) {
  if (!Array.isArray(payload) || payload.length !== count) return null;
  const out = [];
  for (const item of payload) {
    if (typeof item === "string") out.push(item.trim());
    else if (Array.isArray(item) && item[0]) out.push(String(item[0]).trim());
    else out.push("");
  }
  return out;
}

async function providerFetch(url) {
  const controller = new AbortController();
  const timer = setTimeout(() => controller.abort(), PROVIDER_TIMEOUT);
  try {
    return await fetch(url, {
      headers: { "User-Agent": "innioasis-site-i18n/1.0" },
      signal: controller.signal,
    });
  } finally {
    clearTimeout(timer);
  }
}

/* One request per batch, at the provider. clients5 keeps answering when the
   translate_a/single endpoint rate-limits a Cloudflare egress IP. */
async function translateRemote(strings, target) {
  const params = new URLSearchParams();
  params.set("client", "dict-chrome-ex");
  params.set("sl", "auto");
  params.set("tl", target);
  for (const source of strings) params.append("q", source);

  try {
    const response = await providerFetch(
      "https://clients5.google.com/translate_a/t?" + params.toString()
    );
    if (response.ok) {
      const aligned = listFromClients5(await response.json(), strings.length);
      if (aligned) return aligned;
    }
  } catch (_) {}

  const gtx = new URLSearchParams();
  gtx.set("client", "gtx");
  gtx.set("sl", "auto");
  gtx.set("tl", target);
  gtx.set("dt", "t");
  gtx.set("q", strings.join("\n"));
  const response = await providerFetch(
    "https://translate.googleapis.com/translate_a/single?" + gtx.toString()
  );
  if (!response.ok) throw new Error("provider HTTP " + response.status);
  const payload = await response.json();
  const joined = (payload[0] || [])
    .map((segment) => (segment && segment[0] ? segment[0] : ""))
    .join("");
  const parts = joined.split("\n").map((part) => part.trim());
  return parts.length === strings.length ? parts : null;
}

async function handle(request, env) {
  if (request.method !== "POST") return text(405, "method not allowed");

  const raw = await request.text();
  if (raw.length > MAX_BODY) return text(413, "too large");

  let body;
  try {
    body = JSON.parse(raw);
  } catch (_) {
    return text(400, "invalid json");
  }
  if (!body || !Array.isArray(body.strings)) return text(400, "unexpected payload");

  const locale = clean(body.locale, 24).toLowerCase();
  if (!/^[a-z]{2,3}(-[a-z0-9]{2,4})?$/.test(locale)) return text(400, "bad locale");
  /* English is the source: nothing to translate, nothing to cache. */
  if (locale === "en" || locale.startsWith("en-")) {
    return json(200, {
      translations: body.strings.slice(0, MAX_STRINGS).map((item) => clean(item)),
      cached: 0,
      fetched: 0,
    });
  }

  const strings = [];
  for (const item of body.strings.slice(0, MAX_STRINGS)) {
    const value = clean(item);
    if (usable(value)) strings.push(value);
    else strings.push("");
  }
  if (!strings.length) return json(200, { translations: [], cached: 0, fetched: 0 });

  const out = new Array(strings.length).fill("");
  const wanted = [];
  const keys = new Array(strings.length).fill(null);

  const cache = env.I18N_TRANSLATIONS;
  if (cache && typeof cache.get === "function") {
    try {
      const all = await Promise.all(
        strings.map(async (source, index) => {
          if (!source) return null;
          keys[index] = await cacheKey(locale, source);
          return cache.get(keys[index]).catch(() => null);
        })
      );
      all.forEach((hit, index) => {
        if (typeof hit === "string" && hit) out[index] = hit;
        else if (strings[index]) wanted.push(index);
      });
    } catch (_) {
      strings.forEach((source, index) => {
        if (source) wanted.push(index);
      });
    }
  } else {
    strings.forEach((source, index) => {
      if (source) wanted.push(index);
    });
  }

  if (wanted.length) {
    let translated = null;
    try {
      translated = await translateRemote(
        wanted.map((index) => strings[index]),
        locale
      );
    } catch (_) {
      translated = null;
    }
    if (translated) {
      for (let i = 0; i < wanted.length; i += 1) {
        const value = String(translated[i] || "").trim();
        const index = wanted[i];
        if (!value) continue;
        out[index] = value;
        if (cache && typeof cache.put === "function" && keys[index]) {
          try {
            await cache.put(keys[index], value, { expirationTtl: CACHE_TTL });
          } catch (_) {}
        }
      }
    }
  }

  const cached = out.filter((value, index) => value && wanted.indexOf(index) === -1).length;
  return json(200, {
    translations: out,
    cached,
    fetched: wanted.length,
    locale,
  });
}

export async function onRequestPost(context) {
  return handle(context.request, context.env);
}

export async function onRequest(context) {
  return handle(context.request, context.env);
}
