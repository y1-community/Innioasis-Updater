/**
 * Pages Function for /i18n-missing.
 *
 * The locale runtime posts a small batch of source strings that a non-English
 * page could not translate from its catalog. This endpoint validates the
 * batch and either stores it in a KV namespace or forwards it to a webhook,
 * so a translation run can pick it up later:
 *
 *   I18N_MISSES          KV namespace binding (preferred). Entries expire
 *                        after 90 days.
 *   I18N_MISS_WEBHOOK    optional fallback: an endpoint that accepts one JSON
 *                        document per POST.
 *
 *   wrangler kv namespace create I18N_MISSES --config wrangler.i18n-missing.toml
 *   wrangler secret put I18N_MISS_WEBHOOK --config wrangler.i18n-missing.toml
 *
 * Request:
 *   POST /i18n-missing
 *   {"locale":"de","base":"de","page":"/guide.html","strings":["Skip to content"]}
 *
 * Nothing about the reader is kept: no IP, no user agent, no cookie. The
 * strings are our own source copy, never anything a visitor typed. A batch
 * that is not configured with either binding still answers 204, so a browser
 * does not retry a queue that has nowhere to go.
 */

const MAX_BODY = 16384;
const MAX_STRINGS = 60;
const MAX_STRING = 300;
const MAX_PAGE = 200;
const KEEP_DAYS = 90;

function parseList(value) {
  return String(value || "")
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function corsHeaders(request, env) {
  const allowed = parseList(env.ALLOWED_ORIGINS);
  const origin = request.headers.get("Origin") || "";
  if (!allowed.length) return { "Access-Control-Allow-Origin": "*", Vary: "Origin" };
  if (!origin) return {};
  if (!allowed.includes(origin)) return null;
  return {
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Methods": "POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type",
    Vary: "Origin",
  };
}

function text(status, message, cors) {
  return new Response(message + "\n", {
    status,
    headers: Object.assign(
      { "Content-Type": "text/plain; charset=utf-8", "Cache-Control": "no-store" },
      cors || {}
    ),
  });
}

function empty(status, cors) {
  return new Response(null, {
    status,
    headers: Object.assign({ "Cache-Control": "no-store" }, cors || {}),
  });
}

function json(status, body, cors) {
  return new Response(JSON.stringify(body) + "\n", {
    status,
    headers: Object.assign(
      {
        "Content-Type": "application/json; charset=utf-8",
        "Cache-Control": "no-store",
      },
      cors || {}
    ),
  });
}

function clean(value, limit) {
  return String(value == null ? "" : value)
    .replace(/[\u0000-\u001f\u007f]/g, " ")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, limit);
}

/* A string worth translating: prose from our own shell or pages. Anything
   shorter than four characters, without a letter, or longer than a paragraph
   is noise the catalog cannot use. */
function usableString(value) {
  if (typeof value !== "string") return null;
  const text = clean(value, MAX_STRING);
  if (text.length < 4) return null;
  if (!/[A-Za-z]{2}/.test(text)) return null;
  if (text.length > MAX_STRING) return null;
  return text;
}

function batchKey(base) {
  const stamp = Date.now();
  let suffix = "";
  try {
    suffix = crypto.randomUUID().slice(0, 8);
  } catch (_) {
    suffix = Math.random().toString(36).slice(2, 10);
  }
  return `miss:${base}:${stamp}:${suffix}`;
}

async function handle(request, env) {
  const cors = corsHeaders(request, env);
  if (request.method === "OPTIONS") {
    if (!cors) return text(403, "origin not allowed");
    return empty(204, cors);
  }
  if (request.method !== "POST") return text(405, "method not allowed", cors);
  if (!cors) return text(403, "origin not allowed");

  const raw = await request.text();
  if (raw.length > MAX_BODY) return text(413, "too large", cors);

  let body;
  try {
    body = JSON.parse(raw);
  } catch (_) {
    return text(400, "invalid json", cors);
  }
  if (!body || typeof body !== "object" || !Array.isArray(body.strings)) {
    return text(400, "unexpected payload", cors);
  }

  const locale = clean(body.locale, 24).toLowerCase();
  if (!/^[a-z]{2,3}(-[a-z0-9]{2,4})?$/.test(locale)) return text(400, "bad locale", cors);
  /* English pages have nothing to translate, and neither do the English
     regional variants: they inherit the source by design. */
  if (locale === "en" || locale.startsWith("en-")) return empty(204, cors);

  const base = clean(body.base, 24).toLowerCase() || locale.split("-")[0];
  const strings = [];
  const seen = new Set();
  for (const item of body.strings.slice(0, MAX_STRINGS)) {
    const text = usableString(item);
    if (!text || seen.has(text)) continue;
    seen.add(text);
    strings.push(text);
  }
  if (!strings.length) return empty(204, cors);

  const batch = {
    locale,
    base,
    page: clean(body.page, MAX_PAGE) || "/",
    strings,
    at: new Date().toISOString(),
  };

  const store = env.I18N_MISSES;
  if (store && typeof store.put === "function") {
    try {
      await store.put(batchKey(base), JSON.stringify(batch), {
        expirationTtl: 60 * 60 * 24 * KEEP_DAYS,
      });
      return json(202, { stored: strings.length }, cors);
    } catch (_) {
      return text(503, "storage unavailable", cors);
    }
  }

  const hook = env.I18N_MISS_WEBHOOK;
  if (hook) {
    try {
      const sent = await fetch(hook, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(batch),
      });
      if (!sent.ok) return text(502, "webhook refused the batch", cors);
      return json(202, { stored: strings.length }, cors);
    } catch (_) {
      return text(502, "webhook unreachable", cors);
    }
  }

  /* Nothing is configured yet. Accept and drop, so the client queue clears
     instead of retrying the same strings on every page. */
  return empty(204, cors);
}

export async function onRequestPost(context) {
  return handle(context.request, context.env);
}

export async function onRequestOptions(context) {
  return handle(context.request, context.env);
}

export async function onRequest(context) {
  return handle(context.request, context.env);
}
