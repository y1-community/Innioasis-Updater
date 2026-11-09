---
title: "Rondo server admin - Innioasis Updater"
description: "Rondo server admin The music server's own admin page, at <server /admin : set up a fresh server, sign in its YouTube account cookies.txt, connect the one Rondo device, ke"
language: "en"
source: "https://innioasis.app/post-install/jarvissax-rondo-docs-dev-server-api.html"
---

# Rondo server admin - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y1&software=rondo-y1)

Post-install setup · Rondo · Y1

# Rondo server admin

A lightweight, custom audio operating system for the Innioasis Y1.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y1&software=rondo-y1)[Install guide](../guide.html?model=Y1&software=rondo-y1)

# Rondo server admin

The music server's own admin page, at `<server>/admin`: set up a fresh server, sign in its YouTube account (cookies.txt), connect the one Rondo device, keep yt-dlp current, see what went wrong. Served by the server itself (any time, from any browser), in the same look as the device and its dashboard (`docs/dev/dashboard-api.md`). It works over `http://` (at home, by IP) and `https://` (on a VPS behind Caddy), and pairs one device with one token. This page describes how it works and its API; for setting a server up, see [docs/server.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fserver.md).

## How it fits together
  - First run: no admin password yet. The server prints a one-time setup code in its log

(`docker logs y1`): `Rondo setup: open <base>/admin and enter 482-913`. The page asks for that code and a new admin password (at least 10 characters). The code changes on every restart until setup is done.
  - Admin sign-in: password → session cookie `rondo_admin` (HttpOnly, SameSite=Strict, Secure

when the request came over HTTPS), 12 h. 5 wrong passwords a minute → `429`.
  - The device token: one at a time. The admin page creates a 6-digit connect code (10

minutes, one use). On the Rondo, Settings › Server › Connect to a server (or the dashboard's Server page) takes the server address and that code; the Rondo calls `POST /device/pair` and keeps the token it gets back. Pairing replaces the previous token (the old device stops working). "Disconnect" removes it. - Existing installs: until a device is paired through the admin page, the `API_TOKEN` from the environment (if set) is the device token, so the current Y1 keeps working. The first pairing or Disconnect retires it for good (`envRetired` in `/data/config.json`).
  - YouTube account (optional): without one, YouTube and YouTube Music run signed out and the

Rondo hides Library, Subscriptions and History (`GET /healthz` → `"account": {"music": bool, "videos": bool}`). **Sign in with a code** (smart-TV style,`server/src/tv.ts`): the page shows a code, the owner enters it at google.com/device; the OAuth tokens live in `/data/secrets/tv-oauth.json` (0600) and renew themselves. YouTube accepts them only from its TV client, so they serve YouTube home / subscriptions / history and the account's playlists and liked music; YouTube Music's own home and history still need cookies.txt. Signed out, YouTube's home mixes the TV app's topic pages (music, gaming, news, sports), since its own home is empty and Trending is gone.
  - Forgotten admin password: remove `adminHash` from `/data/config.json` and restart; the log

shows a new setup code (`docs/server.md` has the command). The device stays connected.
  - http and https: the server speaks plain HTTP on port 3000. On a VPS, Caddy in front adds

HTTPS (with the Android 4.2 cipher settings, see CLAUDE.md). At home, the Rondo can use `http://<server-ip>:3000` directly; the admin page and the dashboard mark such a connection "not encrypted: use it only on your home network".
  - Settings are kept in `/data/config.json` on the server's volume (admin password hash, device

token hash, pairing time, last seen). Secrets are never returned by any endpoint.

## Guessing limits``````

| What | Limit |
| --- | --- |
| Admin password (sign-in, password change) | 5 wrong a minute per address; 30 wrong an hour from all addresses together → 429 until the oldest one ages out (a restart clears it) |
| Setup code (fresh server) | the same, plus: 5 wrong codes from anywhere → a new code in the log and a minute's pause |
| Connect code (POST /device/pair) | 10 minutes, one use; 5 wrong tries cancel it |
| Device token, admin session | 256-bit and 192-bit random: nothing to guess, no limit |
| Rondo dashboard pairing code (on the device, port 8080) | 5 wrong → a new code on the screen and a 30 s pause for everyone (429); wrong guesses don't keep the dashboard from its 15-minute idle stop |

## Admin API (JSON; errors `{"error": "<reason>"}`)

Paths under `/admin/api`. Everything except `state`, `setup`, `login` needs the admin session (`401 {"error": "signin"}` otherwise → the page shows sign-in).
  - `GET /admin/api/state` → `{"setup": true | false, "signedIn": true | false, "https": bool, "version": "1.0.2"}`

(no sign-in needed; the page watches `version` change while the server updates itself) (`setup: true` = no admin password yet).
  - `POST /admin/api/setup``{"code": "482913", "password": "…"}` → `{"ok": true}` and signs in.

`403 {"error": "code"}`, `400 {"error": "password"}` (too short), `409` if already set up.
  - `POST /admin/api/login``{"password": "…"}` → `{"ok": true}`; `403 {"error": "password"}`,

`429 {"error": "wait", "retryAfterSec": n}`.
  - `POST /admin/api/logout` → `{"ok": true}`
  - `POST /admin/api/password``{"current": "…", "next": "…"}` → `{"ok": true}` with a new session cookie;

every other session is signed out. `403`/`400`, `429` like sign-in.
  - `GET /admin/api/status` →

```json {"server": {"version": "1.0.0", "uptimeSec": 5400, "https": true}, "ytdlp": {"version": "2026.10.29.232701", "lastResolveOk": true}, "cookies": {"present": true, "signedIn": true, "account": {"name": "Alex", "handle": "@alex"} | null, "checkedAt": 1793449000000 | null}, "device": {"paired": true, "source": "paired" | "env" | null, "name": "Rondo" | null, "pairedAt": 1793440000000 | null, "lastSeenAt": 1793449100000 | null, "lastIp": "203.0.113.…" | null, "userAgent": "Rondo/1.0.0 …" | null}, "pairing": {"code": "123456", "expiresAt": 1793449600000} | null, "updates": {"server": {"version": "1.0.1", "url": "https://github.com/…", "publishedAt": …} | null, "ytdlp": {"version": "2026.11.01.233542", "url": "…", "publishedAt": …} | null, "checkedAt": … | null}} ``` `updates` names only releases newer than what runs (`server/src/updates.ts`): the latest Rondo release (from the update page's `latest.json`) and yt-dlp's latest nightly (from GitHub), asked at most every 6 hours in the background. `UPDATE_CHECK=0` in the environment turns that off. `signedIn` is null when not checked yet; the server checks after a cookies upload and every 15 minutes.
  - `POST /admin/api/cookies` with the cookies.txt text as the body (`Content-Type: text/plain`,

at most 1 MB) → `{"ok": true, "signedIn": bool, "account": {…} | null}`; `400 {"error": "format"}` when it is not a Netscape cookies file with youtube.com cookies.
  - `DELETE /admin/api/cookies` → `{"ok": true}` (YouTube Music home/library/history stop working).
  - `POST /admin/api/cookies/check` → `{"signedIn": bool, "account": {…} | null}`
  - `POST /admin/api/ytdlp/update` → `{"ok": true, "before": "…", "after": "…"}` (up to ~2 min).
  - `GET /admin/api/server/update` → `{"available": true, "state": "idle" | "pulling" | "restarting" | "updated" | "current" | "failed", "message": "…", "at": ms}`,

or `{"available": false}` without the updater container (`src/serverUpdate.ts`). `POST` the same path to start an update: `{"ok": true}`, `409 {"error": "busy"}` while one runs, `503 {"error": "unavailable"}` without the updater. The server then restarts on the new image and everyone signs in again.
  - The updater itself (`src/updater/main.ts`, reachable only on the compose network, every call with

`Authorization: Bearer <the token in /run/updater/token>`): `GET /v1/status` → `{state, message, at, target}`, `POST /v1/update` → `202 {"started": true}` or `409` while busy.
  - `POST /admin/api/ytdlp/test` → `{"ok": true, "ms": 1840}` or `{"ok": false, "error": "…"}`

(resolves a known video).
  - `POST /admin/api/device/code` → `{"code": "123456", "expiresAt": …}` (replaces an unused one).
  - `DELETE /admin/api/device/code` → `{"ok": true}` (cancel).
  - `DELETE /admin/api/device` → `{"ok": true}` (disconnect: the token stops working).
  - `POST /admin/api/tv` → `{"url": "https://www.google.com/device", "code": "ABC-DEF-GHI", "expiresAt": …}`

(a new code; replaces a waiting one; `502 {"error": "google"}` when Google gives none). The approval arrives in `status.tv`: `{"signedIn": bool, "account": {"name", "handle"} | null, "pending": {url, code, expiresAt} | null, "error": "denied" | "expired" | "revoked" | "failed" | null}`.
  - `DELETE /admin/api/tv/code` → `{"ok": true}` (cancel; an approval that still arrives is revoked).
  - `DELETE /admin/api/tv` → `{"ok": true}` (sign out: tokens deleted and revoked at Google).
  - `GET /admin/api/logs` → `{"lines": [{"time": 1793449000000, "level": "warn" | "error", "msg": "…"}]}`

(the last 100 warnings and errors, newest first, no secrets).

## Device pairing (called by the Rondo, not the admin page)
  - `POST /device/pair``{"code": "123456", "name": "Rondo"}` → `{"token": "<64 hex>"}`;

`403 {"error": "code"}` (wrong or expired; 5 wrong tries cancel the code). No auth header.

## Software updates for the Rondo (device token)
  - `GET /update?firmware=1` → `{"version": "1.0.1", "size": 6413645, "notes": "<release page>", "firmware": 1}`

for the newest Rondo release on the update page (`jarvissax.github.io/rondo/latest.json`, out once the release's `rom.zip` is built), or `{"version": null}`. The device compares it with its own version (Settings › Software update). `firmware` in the query is the device's firmware number (`ro.rondo.firmware`); a release whose `firmware` is higher installs only with Innioasis Updater CE, and the device says so instead of offering it. Without the query (Rondo 1.0.0, from before firmware numbers) only releases for firmware 1 are named.
  - `GET /update/rondo.apk` → that APK (the update page's `rondo.apk`), passed through as it downloads

(`application/vnd.android.package-archive`), so the Y1 never talks to anyone but its server. Android on the Y1 installs it only when it's signed with the same key as the firmware's Rondo.

These are Rondo's own instructions, shown here word for word.

Published by the [jarvissax/rondo](https://innioasis.app/firmware.html?model=Y1&software=rondo-y1) project [[1]](https://innioasis.app/firmware_info.html?repo=jarvissax%2Frondo&software=rondo-y1)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Ajarvissax)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
