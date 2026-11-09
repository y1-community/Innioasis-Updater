---
title: "Y2Linux 1.0 Beta 8.17 (Baseline 114) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.17 Baseline 114 Status: PUBLISHED as GitHub release baseline-114 2026-10-21. Release 1.0.0-beta.8.17 , Reborn 1.0.0-beta.8.17 , kernel 6.18.56-y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.17.html"
---

# Y2Linux 1.0 Beta 8.17 (Baseline 114) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.17 (Baseline 114)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.17 (Baseline 114)

Status: PUBLISHED as GitHub release `baseline-114` (2026-10-21). Release `1.0.0-beta.8.17`, Reborn `1.0.0-beta.8.17`, kernel `6.18.56-y2linux-1.0.0-beta.8.17`, update sequence 8100, Linux `8719042`, Reborn `6d5458c`. Built with `tools/production/release.py` (135 s, resumed workspace, update based on `baseline-113`): container suite 857 OK, host suite 884 OK, Reborn workspace tests, Clippy `-D warnings` and rustfmt clean; all seal checks PASS, no MediaTek firmware in any image. Not installed on a player before publishing; the owner updates by OTA. Milestone audit BETA-8.17 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 722d7aed7348482faf0b3157418f008500bdd0cae35583ea784ef2d5eaf32214 |
| Y2ROOT | 4e2d06d5d01341edf48d73453cc94ee71ac59f120866975bff14290b90d4ffd3 |
| RECOVERY | 4d81a13a9f0b1a6784c31b893de7a21ebe4e658690aff6f88d81bbb642a1d1f1 |
| Y2DATA (no SSH key) | b02a224358a429addba6cb50117edcd8d43675be5b94daa8bd55737c56f9da17 |

## Sources

Issue [#51](https://github.com/SchulzCode/Y2Linux/issues/51) (with a report), nine uploaded reports of 2026-10-20/21 (8.10–8.16) and four Reddit posts without reports. Every finding was checked against the 8.16 source before a change; nothing 8.13–8.16 had already fixed was changed again. Ledger: `UserReports/REVIEWED.md` (F12–F22, maintainer only).

## What changed since Beta 8.16``````````````````````````

| Finding | Evidence | Change |
| --- | --- | --- |
| #51: headphones silent after pause, lock and Next; ALSA -110 on every Play until a reboot | #51 report (install 2813306c, the #48 player, 8.16): 12 failed opens, both crystal tries XTAL_READY -110 each time, also after runtime rail cycles | Stock starts the CS43131 crystal with the codec and never stops it between streams (REA on the stock kernel); the upstream driver stopped it at every hw_free and restarted it at the next hw_params. Now a started crystal runs until the codec runtime-suspends; a start forces its writes to the chip, clears a stale ready flag, logs the live clock state when it fails, and cycles the codec rails once before an open fails. y2_hp/xtal counts failures and recoveries (kernel overlay 0030) |
| F12: SD card "needs repair, use a PC" though the PC reads it | c75aae95 (8.16, 7 791-song card refused at every insertion), Reddit (fixed by reformatting) | fsck.fat -n findings Windows mounts over are admitted: stale free count, label mismatch or invalid/lowercase label, unused clusters, backup boot sector differences, with or without the dirty bit. Each check records its classes and time; a slow check is a timeout, not "needs repair"; the last 10 admissions are in reports. Reborn says "needs repair" or "took too long" instead of "Reinsert the SD card" |
| F20: "Couldn't complete that" on every button until a restart | 61caa81e/297f1032, 319dab53, 26db176e (8.12) + Reddit | A disconnect seen in one of two queued Bluetooth snapshots was overwritten by the next; output stayed on Bluetooth. Kept now, and a Play refused for a missing peer pauses with "Bluetooth disconnected" |
| F21: Bluetooth search fails the first presses | 685c003a, 09cabe08, dbe84d46 | StartDiscovery 15 s; InProgress and a late NoReply count as scanning |
| F14: Connect refused while auto-reconnect pages a switched-off headset | 70cce0f1, 319dab53, 69635cdc | Reborn's intents went to /run/y2/bt-control.ini, the reconnect owner reads /run/y2/bt-intent/ (since Oct 5): never seen. Fixed; a user Connect cancels the automatic page (lock free in ≈ 0.2 s on the test bus), Connect retries a busy lock or a busy BlueZ answer for 45 s; a failed Connect, pending or codec intent holds auto-reconnect only until its 30 s deadline |
| F22: SBC soundbar stutters | Reddit (no report) | BlueALSA steps the SBC bitpool 53 → 45 → 35 when packets queue and back after 10 s clear (patch 0003, --sbc-abr, on by default); bitpool and steps in reports |
| F15: pause_failed on every Bluetooth pause | 70cce0f1, d8152ea6 | BlueALSA's drain timeout that leaves the PCM ready counts as a pause |
| F16: a failed update check delayed the next by a day | ef22a23d (8.15, never offered 8.16) | Only a successful check's time counts |
| F5: an earlier release's panic reported again after an update | 19a41489, d48362a7 | Recorded, not reported, when its version is not the running one (versions.json) |
| F19: own radio stations (UK m3u) don't play | Reddit; no report shows a My Stations play | Mostly BBC, HLS/DASH only (not supported; planned for a later beta). Playlists served as text or bytes are recognised; station_failed logs reason, HTTP status and content type |
| F13: Wi-Fi does not find the saved network after a wake | 70cce0f1 (dbe84d46, 3 boots) | Cause unproven; wifi-failure.json now records scan counts, the saved network's signal and channel, and the country (no names) |
| F18: hang right after a wake from a sleep requested before Reborn was ready | 4fed1b6a (8.12) | Sleep waits up to 60 s for application_ready early in a boot (Power cancels); journal rows around the screen restore |
| F17: GC9503V wake stays dark (DSI reads lag after a screen-off) | 51f3b06d (8.12) | After 3 power cycles still lag, every DSI register is read twice (the lag is one read deep); Reborn's next frame after a failed wake frame tries one screen off/on |

## Known gaps
  - Not run on a player before publishing. Owed on the owner's player: #51 (pause 3 min, lock, Next, 50 quick Nexts,

`y2_hp/xtal`), codec rails idle after stop, sleep drain with the crystal running while the codec is active, a Connect while auto-reconnect pages, SBC steps at range, the F17/F18 paths (rare).
  - The rail cycle and the DSI double read are untested on hardware; both only run on an already failing path.
  - HLS radio (BBC) and an on-device SD repair: later betas (owner decision 2026-10-21).
  - Unchanged: #42, #45, #47 confirmation, WAF rule and billing alert, USB DAC check, video not for 1.0.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
