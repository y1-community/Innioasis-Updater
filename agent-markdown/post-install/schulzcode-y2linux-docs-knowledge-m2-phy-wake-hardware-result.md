---
title: "M2-PHYWAKE-01 physical result - Innioasis Updater"
description: "M2-PHYWAKE-01 physical result <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m2-phy-wake-hardware-result.html"
---

# M2-PHYWAKE-01 physical result - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-PHYWAKE-01 physical result

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-PHYWAKE-01 physical result > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-09, implementation 305f8f9. The owner reports flashing the new build and supplied 10 new.jpg / 50 new.jpg from a confirmed same boot with USB connected. Both identify M2-PHYWAKE-01 / Linux 6.18.0-y2-m2-phywake1. The second photograph actually shows BEAT 49; its filename is not evidence of BEAT 50/STOP.

| Field | 10 new.jpg | 50 new.jpg |
| --- | --- | --- |
| BEAT / FRAME | 10 / 68 | 49 / 302 |
| Stage | WAIT 1S / LOOP LIVE | same |
| Uptime / idle seconds | 11.32 / 10.16 | 54.61 / 49.55 |
| Timer IRQ CPU0 | 1134 | 5463 |
| USB RC / VALID | 0 / 001FFFFF | same |
| PW / CLK | 0 /3 and 0/15 | same |
| WAKE / W / before-after validity | 0 / 1 / 7F-FFF | same |
| Post-read POWER / DEVCTL | 20 / 80 | same |
| PHY 6a before / after | 04 / 00 | same |
| Post-read PHY68..6e | 00 00 00 02 12 00 00 | same |
| Pre-read PHY1a / 1d / 22 / 63 | 10 / 00 / 00 / 00 | same |
| PHY00 / 05 / 15 before-after | 6E/6E / 44/44 / 10/10 | same |
| MemTotal / CPUs online | 22208 kB / 0 | same |
| Last error / sleep / proc / sysfs | NONE / 0 / 0 / 0 | same |
| Frame write / watchdog / framebuffer | 804 / STOPPED / GUARD OK | same |

CONFIRMED: the guarded single force_suspendm release completed with full readback, unchanged three sampled trim bytes and continued PID1/timer progress through BEAT 49. The cached snapshot is taken once near BEAT 1; the photographs do not establish continuous PHY/DMA monitoring. IRQ delta 4329 across 43.29 kernel uptime seconds agrees with 100 Hz, without independent host timing.

USB remains disconnected and DEVCTL reports B-device with no valid VBUS session, despite the owner-confirmed attached cable. This does not establish physical VBUS absence, a broken cable, a ready PHY or USB enumeration. The next smallest observation is the stock PMIC charger-presence bit; see [the CHRDET contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-chrdet-probe.md). No analog/calibration or VBUS forcing is justified solely by these photos.

Private originals and manifests: evidence-private/20260909-m2-phywake-result/.
  - 10 new.jpg: 216478 bytes, SHA-256

`c5f1bc33129096c3e33475e79221f6f5fe894986f47182ff3d91ae1cb3beb247`.
  - 50 new.jpg: 237915 bytes, SHA-256

`5f034d911ec8e9749b62fe1b6c19249c299f1c4fd3fae0a45b106a7a15e65bed`.

The earlier 10.jpg / 50.jpg are retained separately. The former shows a guarded refusal (WAKE -19, W0, V00/000, no PHY write), the latter success at BEAT 44. Their chronology is unresolved; the new confirmed same-boot pair supersedes them for this trial. Unread fields and zero fields without validity are not hardware values. The earlier refusal is not erased or reclassified as a successful write.

Associated candidate: 1,097,728 bytes, SHA-256 `d68c8fbc56721c7aa1fda5b3e321a9aff5876661aac857505864e28d8924793a`. Association is owner-reported and screen-identified, not an independent flash readback. Host elapsed time, final STOP, restoration and broad boot repeatability remain unreported. #23/#27/#28 remain open; M1 complete, M2 incomplete, M3 deferred.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
