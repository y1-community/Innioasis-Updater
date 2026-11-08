/**
 * Cloudflare Pages Function for /download-proxy.
 * Streams release assets with Content-Disposition to force clean filenames in Downloads
 * (e.g. rom_y2.zip instead of rom_y2-windows.zip).
 */

const MAX_FILENAME = 180;
const PLATFORM_SUFFIX = /-(macos|windows|linux|android|windows-arm64|linux-arm64|mac|win)(?=\.zip$)/i;

function safeFilename(name) {
  const base = String(name || "")
    .split(/[\\/]/)
    .pop();
  let cleaned = base
    .replace(/[^A-Za-z0-9._ +()-]/g, "_")
    .replace(/^\.+/, "")
    .trim();
  cleaned = cleaned.replace(PLATFORM_SUFFIX, "");
  return (cleaned || "firmware.zip").slice(0, MAX_FILENAME);
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

function corsHeaders(request, env) {
  const origin = request.headers.get("Origin") || "";
  return {
    "Access-Control-Allow-Origin": origin || "*",
    "Access-Control-Allow-Methods": "GET, HEAD, OPTIONS",
    "Access-Control-Allow-Headers": "Range",
    "Access-Control-Expose-Headers": "Content-Disposition, Content-Length",
    Vary: "Origin",
  };
}

async function handle(request, env) {
  const cors = corsHeaders(request, env);
  if (request.method === "OPTIONS") {
    return new Response(null, { status: 204, headers: cors });
  }
  if (request.method !== "GET" && request.method !== "HEAD") {
    return text(405, "method not allowed", cors);
  }

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
}

export async function onRequest(context) {
  return handle(context.request, context.env || {});
}

export default {
  async fetch(request, env) {
    return handle(request, env || {});
  }
};
