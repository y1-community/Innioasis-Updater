---
title: "M2-PWRAP-01 physical result - Innioasis Updater"
description: "M2-PWRAP-01 physical result <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m2-pwrap-hardware-result.html"
---

# M2-PWRAP-01 physical result - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-PWRAP-01 physical result

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-PWRAP-01 physical result > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-09, owner-supplied photographs `10.jpg` and `50.jpg`. Originals are under `out/m1-y2b250-time32/`, but both screens identify M2-PWRAP-01, kernel `6.18.0-y2-m2-pwrap1`. Retained private copies/manifest: `evidence-private/20260909-m2-pwrap-result/`. This is real photographed hardware, not a rendered fixture. The filename `10` is not the displayed heartbeat.

| Field | 10.jpg | 50.jpg |
| --- | --- | --- |
| BEAT / FRAME | 18 / 116 | 50 / 308 |
| Stage | WAIT 1S / LOOP LIVE | STOP: RESTORE ANDROID |
| Uptime / idle seconds | 20.20 / 18.24 | 55.72 / 50.56 |
| MemTotal | 22208 kB | 22208 kB |
| CPU part / online | 0xc07 / 0 | 0xc07 / 0 |
| DT RAM | 24M + 512K, D08 STATIC | same |
| PWRAP RC / VALID | 0 / 3 | 0 / 3 |
| MUX / WRAP / WACS / INIT | 0 / 1 / 1 / 1 | same |
| ARB / PRE | 0000007F / 003000F7 | same |
| CID / VUSB | 00002023 / 0000C000 | same |
| POST | 0030C000 | same |
| Timer IRQ / last error | TIMER IRQ ERR: -61 / TIMER -61 | same |
| Sleep / proc / sysfs return | 0 / 0 / 0 | same |
| Previous frame write | 804 | 804 |
| Watchdog / framebuffer | STOPPED / GUARD OK | same |

Photo SHA-256:
  - `10.jpg` (267217 bytes): `9e8c226771d06bc7a7063be50c61eb589fb16680e8f1bb312f3cd34818c9bd21`.
  - `50.jpg` (346864 bytes): `853c20550372a6b4e4f89db0b9f63cd76b67f30123fe8b29d55e7f6c599e6225`.

## What this establishes

CONFIRMED narrow prerequisite: on this boot the inherited AP PWRAP transport completed CID and VUSB reads and returned to idle; CID low byte is MT6323 `0x23`. VUSB `0xc000` has software enable bit 14 and reported enable bit 15 set. This supports preserving the inherited supply for the next USB study. No rail enable write is needed merely to discover its state. These fields are one cached snapshot, not two independent bus reads or evidence of continuous rail monitoring. They do not measure 3.3 V or qualify battery/charger telemetry.

The kernel/PID1 remains observable through BEAT 50, with 35.52 seconds of kernel uptime between the photographed states. Those are kernel times, not an independent host-clock accuracy measurement or repeated-boot qualification. MemTotal is 21.6875 MiB under D08; application/subsystem working-set sufficiency is untested.

## Timer diagnostic cause

Pinned v6.18 `drivers/clocksource/timer-of.c:66–68` registers the interrupt action with `np->full_name`, while `timer-mediatek.c` names the clock-event object `mtk-clkevt`. The PID1 parser incorrectly searches for that clock-event name in `/proc/interrupts`. The board DT node is `timer@10008000`; a source-backed parser fix must match the actual action token and numeric IRQ row. The raw hardware interrupt listing is not supplied, so the precise rendered action string/count is still to be confirmed. -61 is the parser's no-data result; it does not show that timer IRQs are absent. Working sleeps and progress remain confirmed.

## Identity and remaining boundaries

The associated candidate is [the retained M2-PWRAP-01 image](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-pwrap-01-result.md), SHA-256 `c51102c861d65d39f5af2425ed73e9c1ba21d8adaae1b016f450a58630946ac0`. The screenshots identify the build, but do not independently confirm selected or flashed/readback SHA-256. Host elapsed time, cable state, reset history and restoration outcome have not been supplied. Do not infer them from the folder name or photographs. M1 remains complete; #23, #27 and M2 stay open.

Next: correct timer reporting and resolve normal-handoff USB clocks/PHY/DMA. Only the scoped PWRAP/VUSB prerequisite has advanced to physical evidence.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
