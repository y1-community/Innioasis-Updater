---
title: "M2-USBSTATE-01 physical result - Innioasis Updater"
description: "M2-USBSTATE-01 physical result <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m2-usb-state-hardware-result.html"
---

# M2-USBSTATE-01 physical result - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-USBSTATE-01 physical result

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-USBSTATE-01 physical result > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-09. Owner-supplied 10.jpg / 50.jpg in out/m2-usbstate-01; both identify M2-USBSTATE-01 and Linux 6.18.0-y2-m2-usbstate1. Private originals/manifest: evidence-private/20260909-m2-usbstate-result/.

| Field | 10.jpg | 50.jpg |
| --- | --- | --- |
| BEAT / FRAME | 11 / 74 | 50 / 308 |
| Stage | WAIT 1S / LOOP LIVE | STOP: RESTORE ANDROID |
| Uptime / idle | 12.43 / 11.17 | 55.72 / 50.56 |
| Timer IRQ CPU0 | 1245 | 5574 |
| USB RC / VALID | 0 / 001FFFFF | same |
| PW / CLK | 0 /3 and 0/15 | same |
| POWER / DEV / HW | 20 / 80 / 6503 | same |
| PHY 68..6e | 00 00 04 02 12 00 00 | same |
| DMA0..7 control | eight 0000 words | same |
| IRQ enable TX / RX / USB | 01FF / 01FE / 06 | same |
| MemTotal | 22204 kB | same |
| CPU online / memory policy | 0 / D08 24M+512K | same |
| Last error / sleep / proc / sysfs | NONE / 0 / 0 / 0 | same |
| Frame write / watchdog / display | 804 / STOPPED / GUARD OK | same |

10.jpg: 289741 bytes, SHA-256 `1aaf6a19d11839942e9acebe93d7959a363801f57ead1bad848bcf965ec51043`. 50.jpg: 303975 bytes, SHA-256 `da7f608547d6f95180a5ba8ca4d0bd4919a3d0fff3dd6ff967cf57e7cc8f4e92`.

CONFIRMED: all 21 guarded MAC/digital-PHY/DMA-control reads complete and PID1 continues without a reported error through BEAT 50. Both photos show the same cached snapshot, not repeated DMA sampling. Timer delta 4329 over 43.29 kernel uptime seconds is consistent with 100 Hz, not independent host timing.

POWER 0x20 has high-speed enable set and soft-connect clear. DEVCTL 0x80 reports B-device, host/session clear and VBUS below the valid threshold; physical cable state was not supplied and cannot be inferred from an inactive PHY. HWVERS 0x6503 is recorded raw, not promoted to a silicon identity or sibling compatibility. DMA controls are zero at the snapshot, not an ownership/quiescence guarantee. TX/RX/USB masks remain inherited; no Linux USB IRQ handler is installed.

PHY 0x6a=04 forces suspendm while 0x68's suspendm value is zero. UART force/enable are clear. This identifies the smallest next functional step: guarded release of that single force bit, after reading/checking remaining mode controls. See [the PHY wake contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-phy-wake-probe.md). Analog trims/calibration and VBUS forcing must be preserved; no full vendor recover sequence is justified yet.

Associated image SHA-256: `8c1f701b61a1adb70b1377071e6cb885cda989a422fd75d626cd5c7da5bdb5e7`. Photos identify the build; selected/flashed/readback hash, cable state, independent host timing and restoration outcome remain unreported. M1 stays complete, #23/#27/#28 stay open, and M2 exit is not met.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
