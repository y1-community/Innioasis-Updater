---
title: "Y2Linux 1.0 Beta 8.15 (Baseline 112) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.15 Baseline 112 Status: PUBLISHED as GitHub release baseline-112 2026-10-20. Release 1.0.0-beta.8.15 , Reborn 1.0.0-beta.8.15 , kernel 6.18.56-y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.15.html"
---

# Y2Linux 1.0 Beta 8.15 (Baseline 112) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.15 (Baseline 112)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.15 (Baseline 112)

Status: PUBLISHED as GitHub release `baseline-112` (2026-10-20). Release `1.0.0-beta.8.15`, Reborn `1.0.0-beta.8.15`, kernel `6.18.56-y2linux-1.0.0-beta.8.15`, update sequence 7900, Linux `326d924`, Reborn `2ef41d3`. Built with `tools/production/release.py` (133 s, resumed workspace, update based on `baseline-111`): container suite 842 OK, Reborn workspace tests (with and without the CJK font), Clippy `-D warnings` and rustfmt clean; all seal checks PASS, no MediaTek firmware in any image. Not installed on a player before publishing: the owner updates the maintainer's player over the air from the published release ("dont put it on my player, i want to update with OTA"). Milestone audit BETA-8.15 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 95fce8ca697ddcfeb5c0e48d55b4fd7b6661eb320c2d9bff4c87c74b170f608e |
| Y2ROOT | 6b4c4282135adab43beed5724689cca7e10007c4e0db4e4ef7fc0cf3efef75c9 |
| RECOVERY | 556f9bc7b2f5fe1cdd30126431df0ce24ae7229befa2342fd8db64844332dadf |
| Y2DATA (no SSH key) | 3a09ff769199016d83c29247979ca62d80135dbf72c78ef30412ab15ed402b1f |

## What changed since Beta 8.14``````````````````````

| Request / report | Cause | Change |
| --- | --- | --- |
| "Wi-Fi is on, there was an update, now there's no Update button" (user; reports 61caa81e/297f1032 from a player still on 8.12) | After a wake Wi-Fi needs 15–20 s to reconnect (the player sleeps when paused and dark). A Check for Updates in that window failed at once ("Temporary failure in name resolution", "handshake operation timed out"), download.json became Failed, which replaced Update Available with Connect to Wi-Fi; a failed daily check also waited a whole day | update.stage waits up to 30 s for Wi-Fi to be Online, retries a failed lookup/handshake (3 tries), and a failed check keeps the release already offered (last_check_failure); a failed daily check retries with the hourly attempt (Linux abee0c0). Reborn: the failure says Couldn't reach the update server and Update Now stays; the page title is Couldn't Reach the Update Server (Reborn cdf8c7b) |
| Bluetooth codec choice dropped while headphones connect (finding F8, same reports) | SelectCodec refused with "connected A2DP peer required" / "operation in progress" during the connection, and nothing tried again | The Bluetooth worker tries a codec choice refused for a not-ready reason again every 2 s, up to 5 times; a newer choice replaces it (Reborn b8cd9a7) |
| Japanese text (user request; Chinese and Korean too) | Built-in glyph pages cover Latin, Greek and Cyrillic only; CJK showed U+FFFD | Noto Sans CJK JP Regular (OFL-1.1, tag Sans2.004, 16 467 736 bytes, sha256 68a3fc98…75b5) at /usr/share/fonts/noto-cjk/ (Linux 0b3fcb5). Reborn draws missing characters from it at the face's pixel size into a runtime 1024² glyph page (LRU shelves, glyphs of the current and previous frame kept, only changed rows uploaded, at most 48 new glyphs per frame), memory-mapped on first use: 1 MiB CPU + 2 MiB GPU once CJK appears, nothing before (Reborn a3b1943) |

## Checks````

| Check | Result |
| --- | --- |
| Update check after a wake | host tests: never online → no request, offered release kept; three failed lookups → error, offered release kept; a failed download still Failed; daily check retried after a failure (mutation-checked) |
| Codec retry | classification test (not-ready refusals retried, "music playing" not) |
| CJK rendering | 12 preview states (Now Playing JP/KR/mixed/long, Songs, Artists, Albums, Cover Flow, Album, Up Next, Home, Search) rendered on host and compared against host Mesa GLES (gles_compare); 200 glyphs ≈ 1.0–1.4 ms on the host |
| Image | font in the root filesystem; root image 42 → 55.7 MB compressed, about 16.5 MB more free space used |

## Device results after publishing (owner's OTA, maintainer's player, 2026-10-20)````````

| Check | Result |
| --- | --- |
| OTA 8.14 → 8.15 from the published release | Acknowledged 7900 (system step ≈ 9 s), Reborn health ok, no kernel warning, no Errno 22 |
| CJK text on the player (three tagged test songs: Japanese, Korean, Chinese; removed afterwards) | Now Playing, Songs, Artists and Home drew all characters (owner); font mapped by Reborn, no glyph/texture error logged, 1 missed frame in 3051 |
| Check for Updates right after a wake from sleep | waited, then Up to Date (owner); download.jsonChecked, up_to_date: true |

## Known gaps
  - Not run on a player before publishing (owner's choice); checked after the owner's OTA (above). Glyph rasterising

time on the Cortex-A7 was not measured separately.
  - CJK draws in Regular weight inside SemiBold titles; CJK titles sort under "#"; the keyboard is Latin-only.
  - Players on 8.14 or older still have the old check: wait about 20 s after waking before Check for Updates.
  - Unchanged: USB DAC needs the VBUS hardware check; video not for 1.0; Strawberry itself not run; slow crystal, sleep

with a parked CPU, #47 confirmation, WAF rule and billing alert, sleep drain (#42), GC9503V confirmation (#45).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
