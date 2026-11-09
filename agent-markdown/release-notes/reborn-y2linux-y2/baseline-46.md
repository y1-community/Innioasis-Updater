---
title: "Y2Linux Baseline 46 - Innioasis Updater"
description: "Y2Linux Baseline 46 — the first release on the over-the-air update channel. Players with Y2Linux and the Y2 recovery image install this from Settings → About & Updates over Wi-Fi:"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-46.html"
---

# Y2Linux Baseline 46 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux Baseline 46

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-46Y22026-10-14[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Y2Linux Baseline 46 — the first release on the over-the-air update channel.

Players with Y2Linux and the Y2 recovery image install this from Settings → About & Updates over Wi-Fi: Check for Updates → Download Update → Restart and Install (charger or at least half a battery). The player restarts, installs in about a minute, restarts into the new version and confirms it; on any failure it restores the previous one.

New since Baseline 34:
  - Over-the-air updates through a Y2 recovery image: signed releases, verified readback, automatic rollback.
  - Software restart works (the dark panel after a restart is fixed).
  - The display driver detects and recovers a rare dark start.
  - Updates make room on their own (old logs, leftover downloads); music and settings are never touched.
  - Installing restarts into the installer and back by itself.

First install, or players without the Y2 recovery image: build from source and flash with SP Flash Tool — see [BUILDING](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FBUILDING.md), [INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html) and [the recovery install](https://innioasis.app/guides/reborn-y2linux-y2.html).

Assets: `manifest.json` + `manifest.sig` (Ed25519, key `platform-v1-release-20261015`) and the three payloads the manifest pins by SHA-256. Kernel `6.18.56-y2linux-platform-v1-power-final-46`, release `1.0.0-platform-v1-power-final-candidate.46`, update sequence 4600. Developer preview.

Note (2026-10-16): the system image (`rootfs.ext4.gz`) was removed from this release because it contained proprietary MediaTek radio firmware that may not be redistributed. Use Baseline 49 or later; their images contain no firmware.

## Also useful
  - [Install guideStep-by-step install for Reborn (Y2Linux)](../../guides/reborn-y2linux-y2.html)
  - [Y2Linux 1.0 Beta 9.3.19baseline-228 · 2026-11-08](../../release-notes/reborn-y2linux-y2/baseline-228.html)
  - [Y2Linux 1.0 Beta 9.3.18baseline-227 · 2026-11-08](../../release-notes/reborn-y2linux-y2/baseline-227.html)
  - [Y2Linux 1.0 Beta 9.3.17baseline-225 · 2026-11-08](../../release-notes/reborn-y2linux-y2/baseline-225.html)
  - [Y2Linux 1.0 Beta 9.3.16baseline-224 · 2026-11-06](../../release-notes/reborn-y2linux-y2/baseline-224.html)
  - [Y2Linux 1.0 Beta 9.3.15baseline-223 · 2026-11-05](../../release-notes/reborn-y2linux-y2/baseline-223.html)
  - [Y2Linux 1.0 Beta 9.3.13baseline-221 · 2026-11-05](../../release-notes/reborn-y2linux-y2/baseline-221.html)
  - [Y2Linux 1.0 Beta 9.3.12baseline-220 · 2026-11-04](../../release-notes/reborn-y2linux-y2/baseline-220.html)
  - [Y2Linux 1.0 Beta 9.3.7baseline-215 · 2026-11-03](../../release-notes/reborn-y2linux-y2/baseline-215.html)

Notes as published by the Reborn (Y2Linux) project. Install it with Updater CE, or download it from the firmware directory.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-46&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
