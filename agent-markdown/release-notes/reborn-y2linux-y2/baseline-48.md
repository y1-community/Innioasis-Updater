---
title: "Y2Linux Baseline 48 - Innioasis Updater"
description: "Y2Linux Baseline 48 — a new download screen. Install over Wi-Fi: Settings → About & Updates → Check for Updates → Download Update → Restart and Install charger or at least half a b"
language: "en"
source: "https://innioasis.app/release-notes/reborn-y2linux-y2/baseline-48.html"
---

# Y2Linux Baseline 48 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Firmware release notes · Reborn (Y2Linux) · Y2

# Y2Linux Baseline 48

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.baseline-48Y22026-10-14[schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=reborn-y2linux-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=reborn-y2linux-y2)

Y2Linux Baseline 48 — a new download screen.

Install over Wi-Fi: Settings → About & Updates → Check for Updates → Download Update → Restart and Install (charger or at least half a battery).
  - Downloads show their step, the percentage, a smooth progress bar, MB downloaded, the speed and the time left, then a short check with its own bar.
  - When the download is finished the page turns to Ready to Install and a notice says so, wherever you are.
  - The download is checked once instead of twice (about 12 seconds faster) and runs at low priority, so music and the screen stay smooth.
  - Includes Baseline 47's fix for the dark screen while an update installs.

The new screen appears from the next download on (this download still uses the installed version's screen).

Kernel `6.18.56-y2linux-platform-v1-power-final-48`, release `1.0.0-platform-v1-power-final-candidate.48`, update sequence 4800. Assets: `manifest.json` + `manifest.sig` (Ed25519, key `platform-v1-release-20261015`) and the three payloads pinned by SHA-256. Developer preview.

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

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=y2linux&version=baseline-48&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
