---
title: "M2-PHYWAKE-01 — bounded suspend-force release - Innioasis Updater"
description: "M2-PHYWAKE-01 — bounded suspend-force release <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m2-phy-wake-probe.html"
---

# M2-PHYWAKE-01 — bounded suspend-force release - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-PHYWAKE-01 — bounded suspend-force release

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-PHYWAKE-01 — bounded suspend-force release > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-09, #27/#23 prerequisite. The [physical state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-state-hardware-result.md) shows clocks/supply usable, MAC disconnected/B-device, DMA controls zero and PHY suspendm forced low. This is a diagnostic wake step, not USB enumeration.

## Exact scope and evidence

Preserve the existing PWRAP/clock/21-register snapshot. Under the same claimed MAC/PHY windows, read seven additional PHY bytes: 00,05,15,1a,1d,22,63. They are ordinary non-clearing registers corroborated by FM/LK byte accesses:
  - FM usb_phy_recover: 00 at c04da024, 05 at c04d9fd8, 15 at c04d9f20,

1a at c04d9df0, 1d at c04d9cd8.
  - FM usb_phy_poweron: 22 at c04d9c08. LK savecurrent reads 63 at 81e093ac.
  - FM usb_phy_poweron clears only force_suspendm bit 2 at c04d9c1c..c04d9c34

and waits 800 us before subsequent device-mode forcing. LK 81e092da..81e092e2 independently matches the bit clear and wait; FM recover c04d9d14..c04d9d20 uses the same bit. Reuse pinned sources and existing focused disassembly.

Refuse before writing unless the full USB snapshot succeeded, HWVERS is the observed 6503, POWER is the observed disconnected 20, DEVCTL B-device/host/session bits are 80, all eight DMA words are zero, and digital PHY controls match the observed passive state (68=00,69=00,6a=04,6b=02,6d=00,6e=00; IDDIG high). Also require BC1.1 switch off (1a bit7), pull-up/down BIST off (1d bit4), DP/DM 100K pulls off (22 low two bits), and calibration ring oscillator off (15 bit7). Any unknown/mismatched mode produces visible refusal and zero writes.

The kernel's only new write adapter re-reads 6a, refuses unless it is still 04, then writes 00 once with writeb. It exposes no arbitrary address/value write API. Wait 800 us. Re-read PHY68..6e, calibration-related bytes 00/05/15, MAC POWER and DEVCTL. Report per-read validity and whether the write occurred. Require 6a=00, unchanged calibration bytes and continued disconnected/B-device state; otherwise report an error without retrying or compensating writes.

No clock/PLL/regulator, analog trim, calibration, BC1.1, pull-resistor, VBUS force, MAC connection, interrupt, FIFO or DMA-control write is added. The remaining vendor poweron/recover operations are deliberately outside this diagnostic: they include forced VBUS signals and calibration changes. The comparator state is reported rather than forced; no physical cable state or USB readiness is inferred from DEVCTL alone. A released force bit is not proof of a ready PHY.

## Scope/validation boundary

This first PHY control write requires the standing scope audit, full existing offline suite, production guard/fault tests, ARM PID1 fixtures, emitted single-byte write review, and D08/layout/BOOTIMG checks. One clean build suffices; preserve all unchanged ROM/source/recovery evidence. No RAM or DMA ownership change.

Only owner BOOTIMG testing may execute it physically. Keep the established 60-second power-on boundary and framebuffer fallback. There is no new USB driver, IRQ handler, packet traffic or persistent calibration write. Observe before/after force state and trims, and stop for the next hardware result. M2 remains open.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
