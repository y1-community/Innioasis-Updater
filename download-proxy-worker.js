/*
 * Optional same-origin download proxy for firmware.html.
 *
 * GitHub release assets cannot be renamed by the browser: they are served from
 * release-assets.githubusercontent.com without CORS headers, and the HTML
 * `download` attribute is ignored cross-origin. This Worker streams an allowed
 * GitHub release asset with a Content-Disposition filename, so the site can
 * save a portable package under the original firmware name (for example
 * rom.zip).
 *
 * Deploy with Wrangler and set:
 *   ALLOWED_REPOS   comma-separated, e.g. "you/y1-stock-rom-portable"
 *   ALLOWED_ORIGINS comma-separated, e.g. "https://innioasis.app"
 *
 * Request:
 *   GET /?url=<github release asset url>&filename=rom.zip
 *
 * Usage from the page:
 *   PortablePackages.download(asset.url, "rom.zip", {
 *     proxyUrl: "https://dl.innioasis.app/"
 *   });
 */

const MAX_FILENAME = 180;

function parseList(value) {
  return String(value || "")
    .split(",")
    .map((item) => item.trim())
    .filter(Boolean);
}

function corsHeaders(request, env) {
  const allowed = parseList(env.ALLOWED_ORIGINS);
  const origin = request.headers.get("Origin") || "";
  if (!allowed.length) {
    return { "Access-Control-Allow-Origin": "*", Vary: "Origin" };
  }
  // A plain anchor download is a navigation and carries no Origin.  It needs
  // no CORS headers, so let it through; only cross-origin fetch is checked.
  if (!origin) return {};
  if (!allowed.includes(origin)) return null;
  return {
    "Access-Control-Allow-Origin": origin,
    "Access-Control-Allow-Methods": "GET, HEAD, OPTIONS",
    "Access-Control-Allow-Headers": "Range",
    "Access-Control-Expose-Headers": "Content-Disposition, Content-Length",
    Vary: "Origin",
  };
}

const PLATFORM_SUFFIX = /[-_](windows[-_]legacy|macos|mac|windows|win|linux|android|darwin)([-_](x64|amd64|x86_64|x86-64|arm64|aarch64))?(?=\.zip$)/i;
const ARCH_SUFFIX = /[-_](x64|amd64|x86_64|x86-64|arm64|aarch64)(?=\.zip$)/i;

function safeFilename(name) {
  const base = String(name || "")
    .split(/[\\/]/)
    .pop();
  let cleaned = base
    .replace(/[^A-Za-z0-9._ +()-]/g, "_")
    .replace(/^\.+/, "")
    .trim();
  /* A mirror bundle is named rom-macos.zip, but the reader clicked rom.zip.
     Save it under the release's own name so Downloads matches the link. */
  cleaned = cleaned.replace(PLATFORM_SUFFIX, "").replace(ARCH_SUFFIX, "");
  return (cleaned || "firmware.zip").slice(0, MAX_FILENAME);
}

/* ------------------------------------------------------------- mirror stats */

const STATS_MAX_BYTES = 512 * 1024;
const STATS_CONCURRENCY = 6;

function jsonResponse(body, status, extra) {
  return new Response(JSON.stringify(body), {
    status,
    headers: Object.assign(
      {
        "Content-Type": "application/json; charset=utf-8",
        "Cache-Control": "no-store",
        "Access-Control-Allow-Origin": "*",
      },
      extra || {}
    ),
  });
}

function validStatsUrl(value) {
  try {
    const url = new URL(String(value || ""));
    return url.protocol === "https:" && url.hostname === "github.com" ? url : null;
  } catch (_) {
    return null;
  }
}

async function readMirrorIndex(repo) {
  for (const branch of ["main", "master"]) {
    const response = await fetch(
      `https://raw.githubusercontent.com/${repo}/${branch}/index.json`,
      { headers: { Accept: "application/json", "User-Agent": "Innioasis-Updater" } }
    );
    if (!response.ok) continue;
    const data = await response.json();
    if (data && Array.isArray(data.releases)) return data;
  }
  return null;
}

async function readMirrorReleases(repo, token) {
  const headers = {
    Accept: "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
    "User-Agent": "Innioasis-Updater",
  };
  if (token) headers.Authorization = `Bearer ${token}`;
  const releases = [];
  for (let page = 1; page <= 3; page++) {
    const response = await fetch(
      `https://api.github.com/repos/${repo}/releases?per_page=100&page=${page}`,
      { headers }
    );
    if (!response.ok) throw new Error(`GitHub ${response.status}`);
    const batch = await response.json();
    if (!Array.isArray(batch) || !batch.length) break;
    releases.push(...batch);
    if (batch.length < 100) break;
  }
  return releases;
}

function statsEntriesFromIndex(index) {
  const entries = [];
  for (const release of index.releases || []) {
    const tag = String((release && release.tag) || "");
    const url = validStatsUrl(release && release.stats_url);
    if (tag && url) entries.push({ tag, url: url.toString() });
  }
  return entries;
}

function statsEntriesFromReleases(releases) {
  const entries = [];
  for (const release of releases || []) {
    const tag = String((release && release.tag_name) || "");
    const asset = (release.assets || []).find(
      (candidate) => String((candidate && candidate.name) || "").toLowerCase() === "stats.txt"
    );
    const url = validStatsUrl(asset && asset.browser_download_url);
    if (tag && url) entries.push({ tag, url: url.toString() });
  }
  return entries;
}

async function readOneStat(entry) {
  try {
    const response = await fetch(entry.url, {
      redirect: "follow",
      headers: { Accept: "text/plain", "User-Agent": "Innioasis-Updater" },
    });
    if (!response.ok) return null;
    const text = await response.text();
    if (!text || text.length > STATS_MAX_BYTES) return null;
    return { tag: entry.tag, text };
  } catch (_) {
    return null;
  }
}

async function readAllStats(entries) {
  const output = [];
  for (let i = 0; i < entries.length; i += STATS_CONCURRENCY) {
    const batch = entries.slice(i, i + STATS_CONCURRENCY);
    const results = await Promise.all(batch.map(readOneStat));
    results.forEach((result) => {
      if (result) output.push(result);
    });
  }
  return output;
}

/* GET /mirror-stats?repo=<owner>/<repo>
   The browser cannot read GitHub release assets, which carry no CORS headers,
   so this same-origin route gathers each mirror release's stats.txt ledger and
   answers with them in one cached response. */
async function mirrorStats(request, env) {
  if (request.method !== "GET" && request.method !== "HEAD") {
    return jsonResponse({ error: "method not allowed" }, 405);
  }
  const url = new URL(request.url);
  const repo = String(url.searchParams.get("repo") || "").trim().toLowerCase();
  if (!/^[a-z0-9_.-]+\/[a-z0-9_.-]+$/.test(repo)) {
    return jsonResponse({ error: "invalid mirror repository" }, 400);
  }
  const allowed = parseList(env.ALLOWED_REPOS).map((item) => item.toLowerCase());
  if (allowed.length && !allowed.includes(repo)) {
    return jsonResponse({ error: "mirror repository not allowed" }, 403);
  }

  const cache = typeof caches !== "undefined" && caches.default ? caches.default : null;
  const cacheKey = new Request("https://mirror-stats.cache/" + encodeURIComponent(repo));
  if (cache) {
    const hit = await cache.match(cacheKey);
    if (hit) return hit;
  }

  try {
    let entries = [];
    let generatedAt = "";
    const index = await readMirrorIndex(repo);
    if (index) {
      entries = statsEntriesFromIndex(index);
      generatedAt = String(index.generated_at || "");
    }
    if (!entries.length) {
      entries = statsEntriesFromReleases(await readMirrorReleases(repo, env.GITHUB_TOKEN));
    }
    const releases = await readAllStats(entries);
    const response = jsonResponse(
      { repo, generatedAt, releases, releaseCount: releases.length },
      200,
      { "Cache-Control": "public, max-age=600, s-maxage=3600" }
    );
    if (cache) await cache.put(cacheKey, response.clone());
    return response;
  } catch (_) {
    return jsonResponse({ repo, error: "mirror statistics are unavailable" }, 502);
  }
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

export default {
  async fetch(request, env) {
    if (new URL(request.url).pathname === "/mirror-stats") return mirrorStats(request, env);
    const cors = corsHeaders(request, env);
    if (request.method === "OPTIONS") {
      if (!cors) return text(403, "origin not allowed");
      return new Response(null, { status: 204, headers: cors });
    }
    if (request.method !== "GET" && request.method !== "HEAD") {
      return text(405, "method not allowed", cors);
    }
    if (!cors) return text(403, "origin not allowed");

    const requestUrl = new URL(request.url);
    const targetParam = requestUrl.searchParams.get("url");
    if (!targetParam) return text(400, "missing url", cors);

    let target;
    try {
      target = new URL(targetParam);
    } catch (_) {
      return text(400, "invalid url", cors);
    }
    if (target.protocol !== "https:" || target.hostname !== "github.com") {
      return text(403, "only https://github.com assets are allowed", cors);
    }

    const parts = target.pathname.split("/").filter(Boolean);
    if (parts.length < 6 || parts[2] !== "releases" || parts[3] !== "download") {
      return text(403, "only release assets are allowed", cors);
    }
    const repo = (parts[0] + "/" + parts[1]).toLowerCase();
    const allowedRepos = parseList(env.ALLOWED_REPOS).map((item) => item.toLowerCase());
    if (allowedRepos.length && !allowedRepos.includes(repo)) {
      return text(403, "repository not allowed", cors);
    }

    const filename = safeFilename(
      requestUrl.searchParams.get("filename") || parts[parts.length - 1]
    );

    const upstream = await fetch(target.toString(), {
      method: "GET",
      redirect: "follow",
      headers: { Accept: "application/octet-stream" },
    });
    if (!upstream.ok || !upstream.body) {
      return text(upstream.status || 502, "upstream error", cors);
    }

    const headers = new Headers(cors);
    headers.set("Content-Type", "application/octet-stream");
    headers.set(
      "Content-Disposition",
      'attachment; filename="' + filename.replace(/["\\]/g, "_") + '"'
    );
    headers.set("Cache-Control", "no-store");
    const length = upstream.headers.get("Content-Length");
    if (length) headers.set("Content-Length", length);

    if (request.method === "HEAD") {
      return new Response(null, { status: 200, headers });
    }
    return new Response(upstream.body, { status: 200, headers });
  },
};
