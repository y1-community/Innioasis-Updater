---
title: "POWER-FINAL-49 — firmware-free public images, one-time flash package, public codec set - Innioasis Updater"
description: "POWER-FINAL-49 — firmware-free public images, one-time flash package, public codec set Status: PUBLISHED as GitHub release baseline-49 and installed over Wi-Fi 2026-10-16"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-49.html"
---

# POWER-FINAL-49 — firmware-free public images, one-time flash package, public codec set - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-49 — firmware-free public images, one-time flash package, public codec set

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-49 — firmware-free public images, one-time flash package, public codec set

Status: PUBLISHED as GitHub release `baseline-49` and installed over Wi-Fi (2026-10-16): the update files, a first-install package for SP Flash Tool and the GPL source collection. Linux `b4610ea`, Reborn `ceb6313`, kernel `6.18.56-y2linux-platform-v1-power-final-49`, release `…candidate.49`, update sequence 4900. Container suite 727 OK, all seal checks PASS (public distribution gate included). Packages `out/y2linux-platform-v1-power-final-candidate-49/` (update; `-ota-release/` signed with `platform-v1-release-20261015`) and `out/y2linux-49-first-install/` (public flash package), receipts `out/deep-sleep-final/build49-receipts/`. Owner-private variant with aptX: `…-candidate-49-private/` (`-ota/`), receipts `build49p-receipts/`, not published.``````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | c7ece1080fe5dd76f01b02d671dfbe860e5339901b9526f291b44e9f2a27f1a5 |
| Y2ROOT (public) | f1a073c8014163db53781cb3a339bd92acf09d5d17b90c15610cc074760c0d97 |
| Y2ROOT (private, aptX) | 93405c27600a51a26430822fb1ea52b2c7e03f6f7c5febc3a42026e8bfa48c23 |
| RECOVERY | 7097cce59b90c55196fa581db03dd2d1538a37e48fcf3bc92a69c1b8e3478418 |
| Y2DATA (public, no SSH key) | 1b741e60dd08d4596bcb89294404ed6c7b8341734aabac0b95a95a01f9c8a262 |

## Why

The owner asked for release 49 to carry all images (the one-time flash setup for other developers) and an explanation of the recovery. Preparing it showed that the system image of releases 46–48 (`rootfs.ext4.gz`) contained MediaTek's radio firmware, which may not be redistributed (owner: permission from Innioasis, not from MediaTek). Those assets were removed (notes added; never in Git). The public-distribution gate also blocked AAC, aptX, aptX HD and LDAC.``````````````[](https://innioasis.app/guides/reborn-y2linux-y2.html)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FRECOVERY-AND-UPDATES.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FBUILDING.md)

| Change | Detail |
| --- | --- |
| No firmware in any image | /lib/firmware/mediatek/mt6582 → /data/firmware/mt6582. Seal check refuses firmware files; the final images were searched for the firmware's bytes: none. |
| Existing players | The 49+ recovery copies the reviewed files from the old root to Y2DATA (hash-checked) before it writes the new root. |
| New players | y2_platform.radiofw reads the owner's stock system.img (Android sparse ext4) itself, checks the five files (+ reader library) by SHA-256, derives the two defaults, installs them, deletes the copy and starts the radios. While missing, MTP shows a Firmware drive (one empty Y2DATA folder; responder allowlist extended); Reborn explains on Wi-Fi/Bluetooth. `y2-platform firmware status |
| Codecs | Owner decision 2026-10-16: public SBC, AAC from fdk-aac-free 2.0.3 (AAC-LC only, as Fedora ships), LDAC; aptX/aptX HD only private (build.py --public). |
| Public package | package.py --public: no SSH key (developers personalize Y2DATA with first_owner.py), no local paths, one scatter writing BOOTIMG, RECOVERY, ANDROID, USRDATA. |
| GPL sources | Buildroot legal-info (package sources, patches, licences; Reborn = its tagged repository) and the pinned Linux archive are release assets. |
| Build hygiene | Every build installs into an empty target (a reused workspace had kept aptX and the full FDK in an image); two licence-file hashes of bumped packages recorded. |
| Contributions | Y2Linux #38 (cs43130 on-demand load measurement, two driver fixes), Y2Reborn #6 (artwork worker), #7 (A–Z sort), #8 (genre grid title). |
| Docs | INSTALL (eight-step release install), Recovery and updates, BUILDING. |

## Device results
  - Installed over Wi-Fi from the release (2026-10-16, archive `20261016/153`, boot `1723225f`): PASSED. The

recovery logged `radio firmware kept on Y2DATA` (seven files, reviewed hashes) before writing the new root; install 54 s; recovery screen lit (vblank 16 at 1.28 s; the DSI read lag appeared again and the pipeline ran, as on 47/48); `Acknowledged`, taint 0. `/lib/firmware/mediatek/mt6582` → `/data/firmware/mt6582`, `firmware status` Ready. Radios from the new location: MD1 calibration boot result 0, both WMT patches applied, Wi-Fi Online, Bluetooth powered; codec inventory `public` (SBC, AAC, LDAC), only `libfdk-aac.so.2.0.3`, no aptX.
  - Found on the way: after the cancelled private 49, Reborn kept showing Update Didn't Finish and never offered the

release a later check had found (journal `Failed: owner cancelled` won over everything). Fixed in Reborn `476e281` (a cancel is no failure; a later check supersedes a failure), ships with the next release. Owner unblocked by staging the release over the player's Wi-Fi via SSH.
  - Firmware drive (new-player path), owner test (archive `20261016/154`): works, two bugs found. Firmware backed up

and removed at runtime → `Missing`; the Firmware MTP drive appeared after ~5 s (README only). The owner copied the stock `system.img` (518,590,232 bytes); the installation took ~2 s on the player, all seven hashes identical to the original, the copy deleted, space freed, the drive removed. Bugs: (1) the watcher had seen the firmware at service start and never re-checked, so the copy was taken only by a manual `firmware scan` (a fresh install is not affected); (2) the combined connectivity restart was cut off by a 10 s limit after its stop half, so the radios stayed off until started by hand (then Wi-Fi Online, Bluetooth powered). Both fixed in Linux `d1f1195` (next release). The owner's file manager moved instead of copied: `system.img` restored from the Innioasis zip (hash verified); INSTALL and the drive's README now say copy, don't move.
  - Still to do: AAC playback with the owner's headphones.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
