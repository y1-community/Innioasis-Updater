---
title: "Last.fm scrobbling on the player — plan (2026-10-16) - Innioasis Updater"
description: "Last.fm scrobbling on the player — plan 2026-10-16 Status 2026-10-16: phases 1–3 IMPLEMENTED on main Reborn 60bea96; Y2Linux release plumbing; phase 4 owed — the owner's"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-lastfm-scrobble-plan.html"
---

# Last.fm scrobbling on the player — plan (2026-10-16) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Last.fm scrobbling on the player — plan (2026-10-16)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Last.fm scrobbling on the player — plan (2026-10-16)

**Status (2026-10-16): phases 1–3 IMPLEMENTED on `main` (Reborn 60bea96; Y2Linux release plumbing); phase 4 owed — the owner's API key file, one live sign-in/scrobble run, the device test and the release.** Separate from FM radio (FM stays on `beta8-fm`). Owner decisions 2026-10-16 ("go with your recommendations… ship this separate from fm… i will register a api key as long as this is secure"): the owner registers one Last.fm API account; sign-in by QR approval on a phone (password typing only as a fallback); library tracks only; Now Playing updates on; an optional Rockbox-format `.scrobbler.log`; ListenBrainz later; released from `main` as its own beta.

## How it works
  - What counts (Last.fm rules): a track longer than 30 s scrobbles once it has been heard for half its length or

4 minutes, whichever comes first. Paused time does not count; seeking does not add listening time; skipping before the threshold sends nothing; a repeat is a new play. The timestamp is the track's start (UTC). Library files only — internet radio and FM never scrobble. Tracks without artist or title are skipped.
  - Offline first: each scrobble is appended (fsync) to `/data/reborn/state/scrobbles.jsonl` the moment it counts, so

sleep, a flat battery or an update lose nothing. With Wi-Fi online a background worker sends up to 50 per request, with back-off on errors. It never wakes the player or keeps Wi-Fi up. Last.fm ignores plays older than about 14 days; older queue entries are dropped when sent and stay only in the log file (below). At most 10 000 entries are kept.
  - Clock: a play is stamped only with a trustworthy clock (`/run/y2/time-status.json` valid). A play during an

unknown clock keeps its boot-relative time and is stamped when the clock becomes valid in the same boot, otherwise dropped (never sent with a wrong date).
  - `.scrobbler.log` (setting, off by default): the same plays in the Rockbox AUDIOSCROBBLER/1.1 format at the top of

Internal Storage, for players that are rarely online, for upload tools and for ListenBrainz/Libre.fm. Works without an account.
  - Sign-in: Settings → Last.fm shows a QR code and a short address; the listener approves on a phone; the player then

holds only a session key. Fallback: username and password typed once (sent once over HTTPS, never stored).
  - Settings → Last.fm: Connect, "Scrobbling as ", "N waiting to send", Scrobble on/off, Now Playing on/off,

Send Now, Disconnect, Also write .scrobbler.log. An invalid session pauses sending and says "Sign in to Last.fm again".

## Security``````

| Secret | Where | Protection |
| --- | --- | --- |
| Listener password | never on the player (QR flow); fallback: in memory for one request | HTTPS with certificate check, never stored or logged |
| Session key | /data/reborn/state/lastfm.json | 0600 root, Y2DATA only (never in images or logs), deleted by Disconnect and by a settings reset |
| App API key + shared secret | owner's ~/.local/share/y2linux/lastfm-api.json (0600, not in git) → /usr/share/reborn/lastfm-api.json in release images (0600) | not in public source; the release privacy check verifies it is the only Last.fm material in an image. Like every client app the binary image carries it: someone extracting it could send requests in the app's name, but gets no access to any account. A build without the file hides Last.fm. |

Requests: `https://ws.audioscrobbler.com/2.0/`, POST form data, `api_sig` = MD5 of the sorted parameters plus the shared secret (Last.fm's scheme), JSON replies. `curl` as for internet radio (TLS, redirects, timeouts); no other new network code, no new Y2Linux service.

## Phases``````````

| Phase | Content | Evidence |
| --- | --- | --- |
| 1 | Counting rules (reborn_core::scrobble), durable queue and .scrobbler.log (reborn_platform::scrobble), wired to playback | Unit tests: thresholds, pause, seek, repeat, gapless boundary, short and untagged tracks, unknown clock, truncated queue line |
| 2 | Last.fm client: signing (MD5), token/QR sign-in and mobile-session fallback, batch submit, Now Playing, errors (9 invalid session, 11/16 unavailable, 29 rate limit, ignored plays) | MD5/RFC 1321 and signature vectors, stand-in curl (REBORN_CURL), one live run with the owner's account |
| 3 | Settings → Last.fm, QR code (own encoder), status-bar message | UI tests, previews |
| 4 | Release plumbing (key file into the image, privacy check), device test, beta release from main | Owner's player: real scrobbles, offline queue across sleep, sending after reconnect |

## Implemented
  - `reborn_core::scrobble` (rules), `reborn_platform::scrobble` (queue, log, clock trust, CLOCK_BOOTTIME),

`reborn_platform::lastfm` (MD5, signing, curl with the form on stdin, sign-in, Now Playing, batches, errors, back-off), `app/reborn/src/scrobbling.rs` (tracking, worker replies, polling, sending), Settings → Last.fm with an own QR encoder (decoded by zbar in `app/reborn/tests/qr_reader.rs`; the rendered preview decodes too). 508 Reborn tests, strict Clippy.
  - Y2Linux: `tools/production/build.py` copies `~/.local/share/y2linux/lastfm-api.json` (must be 0600, exactly `api_key` and

`shared_secret`, 32 hex each) into the build folder; `post-build-production.sh` installs it 0600 as `/usr/share/reborn/lastfm-api.json`; without the file the image has no Last.fm. The privacy check refuses `lastfm.json`, `scrobbles.jsonl` and `.scrobbler.log` in any image (`data/reborn/` was already refused). 771 host tests.

## Open

The owner's API account (application name "Y2Reborn", callback URL left empty): put the API key and shared secret into `~/.local/share/y2linux/lastfm-api.json` as `{"api_key": "…", "shared_secret": "…"}` with mode 0600 before phase 2's live run.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
