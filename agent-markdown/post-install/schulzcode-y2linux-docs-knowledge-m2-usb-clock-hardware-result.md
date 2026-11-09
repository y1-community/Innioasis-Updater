---
title: "M2-USBCLK-01 physical result - Innioasis Updater"
description: "M2-USBCLK-01 physical result <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m2-usb-clock-hardware-result.html"
---

# M2-USBCLK-01 physical result - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-USBCLK-01 physical result

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-USBCLK-01 physical result > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-09, owner supplied `out/m2-usbclk-01/{10,50}.jpg` and reports no errors. Both photos identify M2-USBCLK-01 / Linux 6.18.0-y2-m2-usbclk1. Copies and hashes are retained in `evidence-private/20260909-m2-usbclk-result/manifest.json`.

| Field | 10.jpg | 50.jpg |
| --- | --- | --- |
| BEAT / FRAME | 15 / 98 | 50 / 308 |
| Stage | WAIT 1S / LOOP LIVE | STOP: RESTORE ANDROID |
| Uptime / idle | 16.87 / 15.21 | 55.72 / 50.56 |
| Timer IRQ CPU0 | 1689 | 5574 |
| MemTotal | 22208 kB | same |
| PWRAP RC / VALID | 0 / 3 | same |
| CID / VUSB | 00002023 / 0000C000 | same |
| CLOCK RC / VALID | 0 / 15 | same |
| PERI / MUX | 00000000 / 01010100 | same |
| PLL / PWR | FD000001 / 80000001 | same |
| LAST ERR | NONE | NONE |
| Sleep / proc mount / sysfs mount | 0 / 0 / 0 | same |
| Previous frame write | 804 | same |
| CPU part / online | 0xc07 / 0 | same |
| Memory policy / watchdog / display | D08 / STOPPED / GUARD OK | same |

10.jpg: 278033 bytes, SHA-256 `b6c4aa3d9958147a81da0b70a52bd1ed3005c392a2cb00bc65c1db4350b822d6`. 50.jpg: 330751 bytes, SHA-256 `bd2d967a6a1cfb48f35c04659db24f1c97aace825cf641202fc39cc58cb01562`. Inspection crops were used only to read the original photos; originals are retained.

## Interpretation and limits

CONFIRMED: timer reporting is corrected and counts increase; the delta is 3885 interrupts over 38.85 kernel uptime seconds, consistent with CONFIG_HZ=100. These are kernel-derived times, not independent host-clock calibration.

The [clock contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-clock-probe.md) decodes PERI bit 10 clear (USB0 ungated), mux power-down bit 23 clear with selector 1, UNIVPLL USB reference enable bit 26 and main enable bit 0 set. PLL power bit 0 is set and isolation bit 1 clear (vendor mt_clkmgr.c PLL_PWR_ON / PLL_ISO_EN). Preserve unrelated bits, including the high PWR bit. This is one cached snapshot, not continuous clock monitoring or a measured frequency. VUSB remains reported enabled.

The source-backed next step can inspect the inherited USB MAC and digital PHY state without enabling clocks, changing analog trims or taking DMA ownership. MAC/PHY access itself remains untested until that candidate runs. Controller initialization, peripheral/VBUS behavior and DMA quiescence are still unresolved.

Associated [candidate](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbclk-01-result.md) SHA-256 is `602080eb199f3a4be30082ee114dfeb97ef414e10d8ad4acf5d239f2096cd6ec`. The owner supplied build-identifying photographs, not selected/flashed/readback hash confirmation. Host time, cable state and restoration outcome are unreported. M1 remains complete; #23/#27/#28 remain open. No USB logging or M2 exit is claimed.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
