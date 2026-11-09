---
title: "POWER-FINAL-35 — over-the-air updates through a Y2 recovery image (OTA-35) - Innioasis Updater"
description: "POWER-FINAL-35 — over-the-air updates through a Y2 recovery image OTA-35 Status: SEALED, awaiting the owner flash 2026-10-15. Package out/y2linux-platform-v1-power-final-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-35.html"
---

# POWER-FINAL-35 — over-the-air updates through a Y2 recovery image (OTA-35) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-35 — over-the-air updates through a Y2 recovery image (OTA-35)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-35 — over-the-air updates through a Y2 recovery image (OTA-35)

Status: SEALED, awaiting the owner flash (2026-10-15). Package `out/y2linux-platform-v1-power-final-candidate-35/` (fallback = 34), receipts `out/deep-sleep-final/build35-receipts/`. BOOTIMG `c27dd33c9d4488b5c7567d90fa1c6ebdbfbc1cae1aaf3b4244475f1ea7e1c391`, Y2ROOT `25ec8077a381b5d19b2cb7f20076a6e0ff06bc7cc1dd66b2f7a365ff12f15eff`, RECOVERY `859227b4fe8e61edee1dca54d306944ef18bf92683aaf45c427b0da64ac704cb`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-35`, kernel `6.18.56-y2linux-platform-v1-power-final-35`, root `2026.08-platform-v1.65`, release `1.0.0-platform-v1-power-final-candidate.35`, update sequence 3500; Linux `3eb96ba`, Reborn `6fbaba8`. Contains 27–34. Contract: [platform-ota-v2](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fplatform-ota-v2.md). Scope audit: OTA-35 in the [roadmap gap audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

## What 35 changes``````````````````````

| Area | Change |
| --- | --- |
| eMMC write policy | A kernel from BOOTIMG may also write RECOVERY and the 4 KiB MISC message; a kernel from RECOVERY (y2.recovery=1) may write BOOTIMG and the message. Neither writes its own image; everything else is unchanged. |
| RECOVERY.img | New, built with the candidate: same zImage and initramfs as BOOTIMG, own DTB (bootargs + y2.recovery=1 only), RECOVERY ramdisk label, name Y2Recovery-1. Installed once with a one-row scatter in recovery-install/. |
| Updater | y2-update-core v2: signed BOOTIMG + Y2ROOT (+ RECOVERY) packages, recovery request through MISC, recovery installer with backup, readback and restore of both images, rescue routing of unfinished updates. Root-only rescue installation retired. |
| Recovery screen | y2-recovery-ui: title, steps and a progress bar (Terminus 16×32 from Linux). Host previews: out/screenshots/recovery/. |
| Platform | Release channel GitHub Releases (allowlisted redirects), per-MiB download progress, charger or ≥ 50 % gate, power-off install, daily background check (never installs), probe-recovery / recovery-status. |
| Reborn | Software Update: Turn Off and Install (press Power), download percent and size, pending restore, charger gate, "Software update available" toast once per release. |
| Keys | Release key platform-v1-release-20261015 (sequences ≥ 3500) added; the development key stays trusted for owner tests. |

## Tests

Host: update core (17 cases: authentication, wrong image slot, install + readback, unchanged recovery, interrupted root and boot writes, readback failure, corrupt backup, unconfirmed health, owner rollback, lost request, probe, battery and space, download staging, up-to-date check, policy/redirect/daily check), eMMC policy in both modes (every sector), wire addresses, rescue and recovery PID1 control flow. Real images: the signed OTA package of the sealed candidate verifies with the image's own trust and compatibility files (full decompression, 1.5 s on the host); one changed byte → `invalid signature`. On the device (34, read-only): the new ARM core found the internal disk by identity, read MISC (no request) and RECOVERY with `O_DIRECT`, and correctly refused the stock recovery (`recovery_image_valid: false`). Reborn: workspace tests and strict clippy clean. Platform: container suite 718 OK, `validate.py` PASS, ELF closure 355 PASS, installed ARM PASS (40 modules), privacy clean, inventory 108 packages.

Not tested: anything after the flash. LK booting our RECOVERY image, the panel in LK's recovery mode, eMMC writes of BOOTIMG/RECOVERY/MISC on the device, install time, power loss.

## Device results
  - Flashed 2026-10-15 (owner, BOOTIMG + ANDROID and the one-row RECOVERY scatter). Archive `20261015/129`:

build/kernel 35, taint 0, Reborn first frame at 20 s, `recovery_image=0`, policy `normal: RECOVERY, MISC message …`, BOOTIMG and RECOVERY on the eMMC byte-identical to the package (RECOVERY tail zero), `recovery_image_valid: true`. The CMD35/WRITE_ZEROES refusal and the boot-stage `OSError` are unchanged from 34.
  - Recovery entry PASSED (`probe-recovery`, then Power): LK booted RECOVERY (`boot_mode=2`), our kernel ran with

`y2.recovery=1` and the recovery write policy, the display came up (owner saw Recovery works), the probe was recorded, MISC cleared, power off; the next Power started the normal system (boot `7676548e`, taint 0). Recovery from kernel start to the recorded outcome: 1.4 s. Evidence: `/data/updates/recovery-probe.json`, `/data/logs/recovery-last.log`.

## Owner steps

1. Flash (one SP Flash Tool session, Download Only).
  - `MT6582_preserve_data_scatter.txt`: BOOTIMG + ANDROID, as always.
  - Then `recovery-install/MT6582_recovery_scatter.txt`: only RECOVERY → RECOVERY.img selected

([runbook](https://innioasis.app/guides/reborn-y2linux-y2.html)). The stock recovery is saved in archive 128.

Start the player. If the panel stays dark: hold Power 10 s, or flash `fallback/` (34); RECOVERY may stay.

2. Read-only check (agent, archive 129). Kernel `…-35`, `/sys/firmware/y2_boot/metadata``recovery_image=0`, dmesg policy line `normal: RECOVERY, MISC message …`, `y2-platform update recovery-status` → `recovery_image_valid: true`, `misc_request: none`.

3. Recovery entry (owner OK, then press Power once).`y2-platform update probe-recovery`: the player turns off. Press Power: the screen says Recovery works, it turns off; press Power again. Then read `/data/updates/recovery-probe.json` (LK `boot_mode=2`, `recovery_image=1`) and `/data/logs/recovery-last.log`. Note whether the recovery screen was visible.

4. First install, no network (owner OK). Copy the signed test package `out/y2linux-platform-v1-power-final-candidate-35-ota-devtest/` (development key, reinstall of 35) to `/data/ota-test`, `y2-platform update stage --package /data/ota-test`. In Reborn: Settings → About & Updates → Turn Off and Install, Power, watch the progress, Power. Afterwards: journal `Acknowledged`, both images equal to the package, install time from `recovery-last.log`.

5. Interruption (optional, owner). Repeat 4 and hold Power during "Installing the system"; Power again: the recovery restores, Update not installed / The previous version was restored.

6. Network. Publishing a GitHub release is the owner's decision; until then `/data/updates/channel.json` can point at a test location.

## Signed OTA packages (not published)``````

| Folder | Key | Use |
| --- | --- | --- |
| out/y2linux-platform-v1-power-final-candidate-35-ota-devtest/ | development, reinstall flag | step 4 on the device (58.7 MB) |
| out/y2linux-platform-v1-power-final-candidate-35-ota-release/ | platform-v1-release-20261015, sequence 3500 | a future GitHub release; a 35 player reports Up to Date for it |

Both are byte-exact signatures over the sealed BOOTIMG, Y2ROOT and RECOVERY (checked against `SHA256SUMS`).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
