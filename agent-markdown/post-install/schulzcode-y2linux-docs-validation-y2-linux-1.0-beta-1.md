---
title: "Y2Linux 1.0 Beta 1 (Baseline 50) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 1 Baseline 50 Status: PUBLISHED as GitHub release baseline-50 2026-10-16. The first public beta of Y2Linux and Y2Reborn: release 1.0.0-beta.1 , Reborn 1."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-1.html"
---

# Y2Linux 1.0 Beta 1 (Baseline 50) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 1 (Baseline 50)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 1 (Baseline 50)

Status: PUBLISHED as GitHub release `baseline-50` (2026-10-16). The first public beta of Y2Linux and Y2Reborn: release `1.0.0-beta.1`, Reborn `1.0.0-beta.1`, kernel `6.18.56-y2linux-1.0.0-beta.1`, update sequence 5000, Linux `5ac955f`, Reborn `e394c38`, git tag `baseline-50` in both repositories. Built with `--public`. Container suite 728 OK, all seal checks PASS (public distribution gate, no radio firmware). Milestone audit: BETA-1 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 55e8ed3a685274c691e82ca4a18d0badb5b4c06a29ef0f995378f3e15547e004 |
| Y2ROOT | cc794c25917d64bad4ca0e7d08b3322a3f03c513ad239422a2aadcde267cb3c8 |
| RECOVERY | b58b8f68bde5390a2c0a0f5270f42ec719de40860ca25bfa19828b390b11a379 |
| Y2DATA (no SSH key) | 28149d30eb9b8f959537643c9bd3e980d1d5e904abff42f382b0912eecfdc343 |

## Release contents
  - `Y2Linux-1.0.0-beta.1-first-install.zip`: BOOTIMG, RECOVERY (Y2 recovery image), Y2ROOT, Y2DATA, the scatter

files for SP Flash Tool (one pass writes all four) and checksums. No MediaTek firmware, no SSH key.
  - The signed over-the-air update (`manifest.json`, `manifest.sig`, three payloads; key `platform-v1-release-20261015`).
  - Corresponding sources: Buildroot legal-info (package sources, patches, licences) and the Linux 6.18.56 archive;

Y2Linux and Y2Reborn at `baseline-50`.

## Since 49````

| Change | Detail |
| --- | --- |
| Firmware watcher | Re-checks every maintenance pass and restarts the radios as stop + start with enough time (owner Firmware-drive test of 49, archive 154). |
| Software Update | A cancel or an older failure no longer hides a newer release (Reborn 476e281). Versions read "1.0.0 Beta 1". |
| Identity | Y2Linux and Reborn 1.0.0-beta.1. |

What the path to the beta brought (35–49): over-the-air updates through a Y2 recovery image with backup, readback and rollback; software restart fixed; the download screen; space for every update; firmware-free public images with the owner's own radio firmware; public codec set SBC, AAC (fdk-aac-free), LDAC. Reports [35](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-35.md)–[49](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-49.md).

## Known gaps (also in the release notes)

Battery in sleep ≈8.3 mA vs stock ≈1.3 mA; rare slow display start after a restart (picture starts since 47); USB after deep-sleep wake not confirmed over many wakes; Bluetooth reconnect after a wake, AAC (fdk-aac-free) with AirPods not yet confirmed; full install from stock run on one player only.

## Device results
  - Owner installed Beta 1 over Wi-Fi from the release: "works" (owner, 2026-10-15). On-device check (version,

health, firmware, radios) pending; the player was not connected when the handoff was written.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
