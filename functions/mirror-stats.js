/**
 * Cloudflare Pages Function for /mirror-stats.
 *
 * Returns every per-release stats.txt from one portable mirror in a single
 * same-origin response. The browser cannot fetch GitHub release assets
 * directly (they do not send CORS headers), so this function does it server
 * side and caches the result.
 *
 * The mirror's index.json already lists every release and its stats_url, so
 * one raw file plus the stats assets is enough. If the index is missing we
 * fall back to the GitHub releases API.
 */

const ALLOWED_REPO = /^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/;
const MAX_STATS_BYTES = 512 * 1024;
const FETCH_CONCURRENCY = 6;

function json(body, status = 200, extra = {}) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
      ...extra,
    },
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

async function readIndex(repo) {
  const branches = ["main", "master"];
  for (const branch of branches) {
    const response = await fetch(
      `https://raw.githubusercontent.com/${repo}/${branch}/index.json`,
      { headers: { Accept: "application/json", "User-Agent": "Innioasis-Updater" } }
    );
    if (!response.ok) continue;
    const data = await response.json();
    if (!data || !Array.isArray(data.releases)) continue;
    return data;
  }
  return null;
}

async function readApiReleases(repo, token) {
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
    const tag = String(release && release.tag || "");
    const url = validStatsUrl(release && release.stats_url);
    if (tag && url) entries.push({ tag, url: url.toString() });
  }
  return entries;
}

function statsEntriesFromApi(releases) {
  const entries = [];
  for (const release of releases || []) {
    const tag = String(release && release.tag_name || "");
    const asset = (release.assets || []).find(
      (candidate) => String(candidate && candidate.name || "").toLowerCase() === "stats.txt"
    );
    const url = validStatsUrl(asset && asset.browser_download_url);
    if (tag && url) entries.push({ tag, url: url.toString() });
  }
  return entries;
}

async function readStats(entry) {
  try {
    const response = await fetch(entry.url, {
      redirect: "follow",
      headers: { Accept: "text/plain", "User-Agent": "Innioasis-Updater" },
    });
    if (!response.ok) return null;
    const text = await response.text();
    if (!text || text.length > MAX_STATS_BYTES) return null;
    return { tag: entry.tag, text };
  } catch (_) {
    return null;
  }
}

async function readAllStats(entries) {
  const output = [];
  for (let i = 0; i < entries.length; i += FETCH_CONCURRENCY) {
    const batch = entries.slice(i, i + FETCH_CONCURRENCY);
    const results = await Promise.all(batch.map(readStats));
    results.forEach((result) => {
      if (result) output.push(result);
    });
  }
  return output;
}

async function handle(context) {
  const request = context.request;
  if (request.method !== "GET") return json({ error: "method not allowed" }, 405);

  const url = new URL(request.url);
  const repo = String(url.searchParams.get("repo") || "").trim();
  if (!ALLOWED_REPO.test(repo)) return json({ error: "invalid mirror repository" }, 400);

  const cacheKey = new Request(`https://mirror-stats.cache/${encodeURIComponent(repo)}`);
  const cache = typeof caches !== "undefined" && caches.default ? caches.default : null;
  if (cache) {
    const hit = await cache.match(cacheKey);
    if (hit) return hit;
  }

  try {
    let entries = [];
    let generatedAt = "";
    const index = await readIndex(repo);
    if (index) {
      entries = statsEntriesFromIndex(index);
      generatedAt = String(index.generated_at || "");
    }
    if (!entries.length) {
      const token = context.env && context.env.GITHUB_TOKEN;
      entries = statsEntriesFromApi(await readApiReleases(repo, token));
    }

    const releases = await readAllStats(entries);
    const response = json({
      repo,
      generatedAt,
      releases,
      releaseCount: releases.length,
    });
    response.headers.set("Cache-Control", "public, max-age=600, s-maxage=3600");
    if (cache && typeof context.waitUntil === "function") {
      context.waitUntil(cache.put(cacheKey, response.clone()));
    }
    return response;
  } catch (error) {
    return json(
      { repo, error: "mirror statistics are unavailable", detail: String(error && error.message || error) },
      502
    );
  }
}

export async function onRequest(context) {
  return handle(context);
}

export default {
  async fetch(request, env) {
    return handle({ request, env: env || {}, waitUntil: () => {} });
  },
};
