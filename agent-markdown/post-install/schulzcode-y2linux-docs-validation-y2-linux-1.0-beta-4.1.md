---
title: "Y2Linux 1.0 Beta 4.1 (Baseline 54) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 4.1 Baseline 54 Status: PUBLISHED as GitHub release baseline-54 2026-10-15. Release 1.0.0-beta.4.1 , Reborn 1.0.0-beta.4.1 , kernel 6.18.56-y2linux-1.0.0"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-4.1.html"
---

# Y2Linux 1.0 Beta 4.1 (Baseline 54) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 4.1 (Baseline 54)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 4.1 (Baseline 54)

Status: PUBLISHED as GitHub release `baseline-54` (2026-10-15). Release `1.0.0-beta.4.1`, Reborn `1.0.0-beta.4.1`, kernel `6.18.56-y2linux-1.0.0-beta.4.1`, update sequence 5350, Linux `929ea0d`, Reborn `d0008dd`, git tag `baseline-54` in both repositories. Built with `tools/production/release.py` (`--public`) in 147 s: container suite 740 OK, all seal checks PASS, no MediaTek firmware in any image. Milestone audit: BETA-4.1 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 97edc9a403c097434bf1cdbac8715b498f68a17ad390457e9f8eca7c1df8e6dc |
| Y2ROOT | 473bdf414c34f2f85c6d87812a14506f0f37bd129fabb8861ca796bb0f45463b |
| RECOVERY | 7a6ea2627052fa3aa88ddc81085c9f55bd6717702325bd0d38b1f33a0ae71bc5 |
| Y2DATA (no SSH key) | bedcc7c0724bd83321f5a3abf817da48c0fa4d87cf4266847f8679af90f6f8c8 |

## Beta 4 on the player (owner, 2026-10-15) and the fixes````````````````````

| Owner report | Cause (evidence) | Fix |
| --- | --- | --- |
| "playback command queue full", health failed while a station was stopped or paused | Stream::drop joined the curl fetcher while its own pipe read end was still open; with playback no longer reading, the full pipe held the fetcher in write() forever and the decode thread with it (Reborn log: heartbeat deadline exceeded; a [curl] <defunct> left over). | The read end is closed first, so the fetcher's write fails at once. Host test stopping_a_station_with_a_full_pipe_returns_promptly (hangs without the fix). Radio jobs get a 60-s heartbeat (a reconnect may wait 45 s). |
| "Connect to Wi-Fi to listen to radio" while connected | Radio availability was only recomputed on a Wi-Fi event. | Recomputed on every loop pass; only a disconnected Wi-Fi refuses a station. |
| After screen-off, Wi-Fi shown as not connected; the owner restarted Wi-Fi (16:00, 18:37, 18:56 UTC, each after a screen-off, no suspend in those windows) | Reborn trusted /run/y2/network.json for 15 s and mapped a missing record to "not connected". With the screen dark the platform writes it every 10 s; measured ages on the player reach 12.0 s (837 samples over 7 min, none over 15 s in that window). | An Online record stays valid for 45 s (still matched to the live BSSID and address); without a record the supplicant state decides. |
| Updates: "Connect to Wi-Fi to check for updates" after sleep | The TLS clock check compared the wall clock with CLOCK_MONOTONIC, which stops in suspend: after any sleep over 60 s tls_ready stayed false until ntpd's next callback. | Time anchors record CLOCK_BOOTTIME, and the check compares against it (host test test_tls_clock_stays_ready_across_suspend). |

Not reproduced: a Bluetooth problem after waking ("possible bt also"). The logs show one "operation in progress" refusal at a wake and nothing else.

## Device checks owed (after the owner's over-the-air install)

Stop, pause and switch stations while playing (no "queue full"); after 10+ minutes of screen-off the Wi-Fi page and Radio work without restarting Wi-Fi; after a deep sleep, Check for Updates works; Bluetooth reconnects after waking.

## Known gaps

As in [Beta 4](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-4.md): FM radio next; HLS stations; sleep ≈9.4 mA vs stock ≈1.3 mA; Bluetooth range hardware-limited; no headphone-jack detection.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
