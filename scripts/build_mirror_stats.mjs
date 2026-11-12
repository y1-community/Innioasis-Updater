/*
 * Build the static download breakdown for every portable mirror.
 *
 * GitHub release assets carry no CORS headers, so a browser cannot read a
 * mirror's stats.txt itself. This script gathers each mirror's ledgers once,
 * the site's own aggregator sums them, and the compact result is written to
 * mirror-stats/<owner>--<repo>.json for firmware-info.js to fetch.
 *
 * Usage:
 *   node scripts/build_mirror_stats.mjs            # every mirror in the catalog
 *   node scripts/build_mirror_stats.mjs owner/repo # one mirror (for testing)
 */

import { createRequire } from "node:module";
import { readFileSync, writeFileSync, mkdirSync, readdirSync, existsSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const { aggregate } = require("../mirror-stats.js");

const root = join(dirname(fileURLToPath(import.meta.url)), "..");
const outputDir = join(root, "mirror-stats");
const MAX_STATS_BYTES = 512 * 1024;
const CONCURRENCY = 8;

function catalogMirrors() {
  const source = readFileSync(join(root, "firmware-catalog.js"), "utf8");
  const mirrors = new Set();
  for (const match of source.matchAll(/"portable_zips"\s*:\s*"([^"]+)"/g)) {
    const value = match[1].trim().split(/[\s,]+/)[0];
    if (/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(value)) mirrors.add(value.toLowerCase());
  }
  return [...mirrors].sort();
}

function slugFor(repo) {
  return repo.toLowerCase().replace("/", "--");
}

function mapLimit(items, limit, worker) {
  const results = new Array(items.length);
  let next = 0;
  async function pump() {
    while (next < items.length) {
      const index = next++;
      results[index] = await worker(items[index], index);
    }
  }
  return Promise.all(Array.from({ length: Math.min(limit, items.length) }, pump)).then(() => results);
}

async function readIndex(repo) {
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

function validStatsUrl(value) {
  try {
    const url = new URL(String(value || ""));
    return url.protocol === "https:" && url.hostname === "github.com" ? url : null;
  } catch (_) {
    return null;
  }
}

async function readStat(entry) {
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

async function buildMirror(repo) {
  const index = await readIndex(repo);
  if (!index) throw new Error("no index.json");
  const entries = [];
  for (const release of index.releases) {
    const tag = String((release && release.tag) || "");
    const url = validStatsUrl(release && release.stats_url);
    if (tag && url) entries.push({ tag, url: url.toString() });
  }
  const docs = (await mapLimit(entries, CONCURRENCY, readStat)).filter(Boolean);
  if (!docs.length) throw new Error("no stats.txt ledgers");
  const result = aggregate(docs);
  return {
    repo,
    generatedAt: String(index.generated_at || ""),
    aggregate: result,
  };
}

async function main() {
  const requested = process.argv.slice(2).filter((arg) => !arg.startsWith("-"));
  const mirrors = requested.length ? requested.map((repo) => repo.toLowerCase()) : catalogMirrors();
  mkdirSync(outputDir, { recursive: true });
  let written = 0;
  for (const repo of mirrors) {
    const target = join(outputDir, `${slugFor(repo)}.json`);
    try {
      const data = await buildMirror(repo);
      writeFileSync(target, JSON.stringify(data, null, 1) + "\n");
      written++;
      console.log(`${repo}: ${data.aggregate.total} downloads across ${data.aggregate.releases} ledgers`);
    } catch (error) {
      const kept = existsSync(target) ? " (kept the previous file)" : "";
      console.warn(`::warning::${repo}: ${error.message}${kept}`);
    }
  }
  console.log(`Wrote ${written} of ${mirrors.length} mirror files.`);
  /* A stale file is better than a missing one, so only a total wipeout fails. */
  if (written === 0 && readdirSync(outputDir).filter((name) => name.endsWith(".json")).length === 0) {
    process.exitCode = 1;
  }
}

await main();
