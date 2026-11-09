---
title: "POWER-FINAL-37 — recovery replay fix and the warm-restart display snapshot - Innioasis Updater"
description: "POWER-FINAL-37 — recovery replay fix and the warm-restart display snapshot Status: SEALED, awaiting the owner flash 2026-10-15. Package out/y2linux-platform-v1-power-fina"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-37.html"
---

# POWER-FINAL-37 — recovery replay fix and the warm-restart display snapshot - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-37 — recovery replay fix and the warm-restart display snapshot

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-37 — recovery replay fix and the warm-restart display snapshot

Status: SEALED, awaiting the owner flash (2026-10-15). Package `out/y2linux-platform-v1-power-final-candidate-37/` (fallback = 35, which the player runs), receipts `out/deep-sleep-final/build37-receipts/`. BOOTIMG `7167dd4ad22ec5690a1e1ce3ba5620ebd661821face1431478f653c67f9b048d`, Y2ROOT `2cfdef294fbc7f5f99bd8240de599a28d042d0c1e63ad7b140155cf9247f3082`, RECOVERY `7c789d9ea8b4900022ff20fe8e107b69ab7242832f566e9dd354537ce17a16e2`. Kernel `6.18.56-y2linux-platform-v1-power-final-37`, release `1.0.0-platform-v1-power-final-candidate.37`, update sequence 3700. Container suite 718 OK, all seal checks PASS. 36 (status fix only) was never installed; 37 contains it.

## Why````````````

| Found on the device | Fix in 37 |
| --- | --- |
| 35 → 36 install: the recovery refused its own release (failed_unchanged, downgrade/replay refused, nothing written). The recovery image written by prepare is the new release's, whose compat file names the package's sequence. | The recovery checks replay against the sequence the normal system recorded when it queued the package (regression test with a release key). |
| y2-platform update status called the schema-2 journal unreadable (Reborn could not install; health would never acknowledge). | Python accepts journal schema 2; an unpublished channel (404) means up to date. |
| A software restart (boot_reason 4) leaves the panel dark (archives 130/131): DSI/PHY registers equal a cold start, but OVL never completes and RDMA never reports done; vblank stays 1. The owner saw LK's logo on the restart. REA of the FM LK (platform_init 0x81e004b8): display init and logo run with no boot-reason branch. | Read-only display-path snapshot at /sys/kernel/debug/y2_display_snapshot: two samples of MMSYS, OVL, RDMA, MUTEX, SMI larb0/common, DSI, MIPI TX, APMIXED PLLs, INFRACFG, TOPCKGEN and SPM power status, for a cold/warm diff. |

## Device results
  - Flashed 2026-10-15; cold display snapshot saved (archive `20261015/133`, both samples complete).
  - First full over-the-air install PASSED (reinstall of 37 with the development package, owner tapped Turn Off

and Install, Power, Power): recovery 136 s from kernel start to `installed`, both images read back equal to the package (BOOTIMG `8c92985d…`, RECOVERY `9ea3c9c8…` over the 16 MiB spans), MISC cleared, the new boot acknowledged health (`Acknowledged`, `accepted.json` 3700), staged package removed. Owner: pace OK, wants it faster and more reassuring while waiting; likes the screen.
  - Measured for speed (read-only, normal system): full verification 24.2 s (libsodium SHA-256 ≈30 MB/s dominates),

eMMC read of the root 5.8 s, zlib inflate of the root 7.6 s, CRC-32 ≈200 MB/s. Changes in 38.

## Owner steps
  - Flash 37 (preserve scatter: BOOTIMG + ANDROID; RECOVERY optional — the install test writes 37's recovery

anyway). The first boot is a cold start: the agent saves its snapshot (archive 133).
  - With the owner's OK: one software restart (`y2-platform shutdown reboot`). The panel will probably stay dark;

the agent saves the warm snapshot over SSH, then the owner holds Power 10 s.
  - Install test: `…-37-ota-devtest` staged on the device, Turn Off and Install in Reborn (now enabled), Power,

watch the progress, Power. The agent checks `Acknowledged`, readback and timing.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
