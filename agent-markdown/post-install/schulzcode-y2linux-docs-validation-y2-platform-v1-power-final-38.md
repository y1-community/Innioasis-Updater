---
title: "POWER-FINAL-38 — stock restart sequence, faster installs, clearer progress - Innioasis Updater"
description: "POWER-FINAL-38 — stock restart sequence, faster installs, clearer progress Status: SEALED, awaiting the owner 2026-10-15. Package out/y2linux-platform-v1-power-final-cand"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-38.html"
---

# POWER-FINAL-38 — stock restart sequence, faster installs, clearer progress - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-38 — stock restart sequence, faster installs, clearer progress

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-38 — stock restart sequence, faster installs, clearer progress

Status: SEALED, awaiting the owner (2026-10-15). Package `out/y2linux-platform-v1-power-final-candidate-38/` (fallback = 37), receipts `out/deep-sleep-final/build38-receipts/`. BOOTIMG `d4e99ba51149e4effd37b34eff7fea0a90b645497b01ef47df1f25b473abcf9d`, Y2ROOT `5670c063fa84ff0eba939510996f7ca7b9b1692cbd7d504afd3dbf8198ff6709`, RECOVERY `953c3153fd5bcffcf823585fc9f5eed4fe52ba380c8615cf46cc25cee6283857`. Kernel `6.18.56-y2linux-platform-v1-power-final-38`, release `1.0.0-platform-v1-power-final-candidate.38`, update sequence 3800. Container suite 718 OK, all seal checks PASS. Signed OTA (release key): `out/y2linux-platform-v1-power-final-candidate-38-ota-release/`.

## Why

A software restart leaves the panel dark (since 11; archives 130/131 on 35). LK shows its logo and initialises the display without a boot-reason branch (REA, FM `lk.bin``platform_init` 0x81e004b8). The stock kernel's restart (REA, FM kernel `wdt_arch_reset` 0xc0541d10) writes `WDT_MODE = (mode & 0xffffffa6) | 0x22000014` — external reset to the PMIC and auto-restart — waits 2.5 ms, then `WDT_SWRST = 0x1209`. Upstream `mtk_wdt_restart` (ours) only wrote `WDT_SWRST`, so display-path state survived and Linux got no frames after the logo.````````

| Change | Detail |
| --- | --- |
| Restart | mtk_wdt_restart on MT6582 uses the stock sequence (patch 0037). The suspend backstop watchdog is unchanged. |
| Updates | Restart instead of power-off only with the owner switch /data/updates/restart.json{"mode": "reboot"} (apply and recovery), until a restart is proven on the device. |
| Snapshot | 37's read-only display snapshot stays for a cold/warm diff if a restart still fails. |
| Install speed | 37 took 136 s in recovery (SHA-256 of the 512 MiB root about five times). 38 authenticates the encoded payloads by their signed SHA-256 only, checks backups by their compressed-file hash, reads back by CRC-32, skips unchanged root chunks (root_bytes_written) and logs each step's time. Backups from before 38 still restore. |
| Recovery screen | "Step n of 4", a bar that moves within each step, a shimmer in the unfilled part, the time left from the rate so far, "This takes 1-2 minutes." |

## Device results
  - First release-key over-the-air update PASSED, 37 → 38 (2026-10-15; package staged locally, owner: Turn Off

and Install, Power, Power). 38's recovery ran the install (written by `prepare` before entry) in 52 s (37: 136 s): verify 1.9 s, backup 31.1 s, system 13.0 s (19 046 063 of 536 870 912 bytes written), check 4.9 s, kernel 0.7 s. New system: kernel `…-power-final-38`, taint 0, health acknowledged at 47 s uptime, `accepted.json` 3800, package removed. Automatic restart not yet switched on (restart test pending).
  - Software restart on 38: panel still dark (archive `20261015/135`); the stock reset sequence alone is not the

fix. Cause and fix: [POWER-FINAL-39](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-39.md).

## Owner steps
  - Install 38 (SP Flash Tool BOOTIMG + ANDROID, or over the air from 37 with the signed package — this also measures the new install time).
  - With the owner's OK: one `y2-platform shutdown reboot`. Panel lit → restart fixed; then

`restart.json` on, and an install test without pressing Power. Panel dark → hold Power 10 s; the agent diffs the snapshots (cold: archive 133).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
