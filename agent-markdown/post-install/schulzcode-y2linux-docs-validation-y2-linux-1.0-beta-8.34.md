---
title: "Y2Linux 1.0 Beta 8.34 (Baseline 135) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.34 Baseline 135 Status: PUBLISHED as GitHub release baseline-135 2026-10-24, installed on the owner's player before publishing. Release 1.0.0-beta.8.34"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.34.html"
---

# Y2Linux 1.0 Beta 8.34 (Baseline 135) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.34 (Baseline 135)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.34 (Baseline 135)

Status: PUBLISHED as GitHub release `baseline-135` (2026-10-24), installed on the owner's player before publishing. Release `1.0.0-beta.8.34`, Reborn `1.0.0-beta.8.34`, kernel `6.18.56-y2linux-1.0.0-beta.8.34`, update sequence 9802, root `2026.08-platform-v1.177`, Linux `88febab`, Reborn `01f1ed3`. Built with `tools/production/release.py` (167 s, resumed workspace, update based on `baseline-134`): container suite 881 OK; all seal checks PASS, no MediaTek firmware in any image. Milestone audit BETA-8.34 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | dafa5949523a02e7aee9786119c13f5331cc2573ff56b6019e747f8413b9d680 |
| Y2ROOT | 4da04a178f6f2b4f0d74c83c941903d19160220cdf1a45f88809147b2ed8b7fc |
| RECOVERY | 701c128dcd6af418cb68185694d8158ba1abd3983d614ea92f2046839d587c06 |
| Y2DATA (no SSH key) | e707ba1ca977c9a5adaa61d3ed58476318ed7492b0a88162a9feab88daf8d2fd |

## Why

Y2Linux #61 (report 908888ea, install 0400eb78, Beta 8.31): "Trying to move stuff (or even just open MTP) seems to be non-functional … my file manager (Dolphin) will just hang, and eventually the player will disconnect."

## Cause

Since Beta 8.27 the SD card is read-only until a computer is connected; a few seconds after the cable is connected the platform opens the card's write window and swaps its MTP storage (`usb.py reconcile`: `umtprd -cmd:unmount`, then `mount`). uMTP announces each swap (StoreRemoved, StoreAdded) on the interrupt endpoint **while holding `inotify_mutex`**, which every MTP operation takes, and that write completes only when the host reads the event. KDE's MTP daemon (Dolphin) and libmtp tools do not read events while they set up a session, so every request waited; the host gave up after ~20 s and reset the player. Any SD card file system; reproduced on the owner's player (8.33, exFAT card): stuck `msgqueue_thread` in `ffs_epfile_io`, `io_thread` waiting on the mutex.

## What changed since Beta 8.33``````

| Change | Detail | Evidence |
| --- | --- | --- |
| MTP events never stall requests (#61) | Patch 0006-y2-mtp-events-never-block: events go into a 16-slot queue written by their own thread, outside the mutex; when the host never reads them the oldest is dropped | Linux 8a699dc; tests/usb_mtp_protocol.c pushes 20 events into an unread endpoint under the mutex (hung before the fix, passes after) |

## Device results``

| Check | Result |
| --- | --- |
| Install by OTA staging (owner's player) | sequence 9802 Acknowledged after a normal update restart |
| KDE (kioclient, Dolphin's MTP path) after the restart = reconnect | both storages list at once |
| SD storage swapped 3× under KDE's live session | every listing at once (before: the first swap hung all requests, 20 s timeout) |
| 20 MB copy to Internal Storage and SD card, read back, delete | ~1.3 s each, SHA-256 equal, deleted |

## Open
  - Windows Explorer and macOS (Android File Transfer, OpenMTP) not tried with this build.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
