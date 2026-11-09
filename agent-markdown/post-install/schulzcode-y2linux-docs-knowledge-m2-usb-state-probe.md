---
title: "M2-USBSTATE-01 — inherited USB state, read only - Innioasis Updater"
description: "M2-USBSTATE-01 — inherited USB state, read only <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m2-usb-state-probe.html"
---

# M2-USBSTATE-01 — inherited USB state, read only - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-USBSTATE-01 — inherited USB state, read only

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-USBSTATE-01 — inherited USB state, read only > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

[Physical result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-state-hardware-result.md): all reads pass, with PHY force_suspendm still set. [Next guarded release](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-phy-wake-probe.md).

2026-09-09. Smallest #27 prerequisite after successful physical [PWRAP/VUSB and clock reads](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-clock-hardware-result.md). No USB initialization or new hardware write is implemented.

## Read contract

| Window / offset | Width | Evidence / reason |
| --- | --- | --- |
| MAC 0x11200000 + 0x01 | 8 | MUSB POWER, passive soft-connect/mode state. |
| MAC + 0x60 | 8 | DEVCTL, passive device/host/VBUS/session state. FM dma_controller_irq reads at c03bdb94. |
| MAC + 0x6c | 16 | HWVERS; FM musb_core_init reads at c03a3ba4. Use readw despite upstream header's misleading 8-bit comment, matching upstream musb_core.c. |
| MAC + 0x06, 0x08 | 16 | TX/RX interrupt enable masks, not clear-on-read status; FM mt_usb_interrupt reads at c04d856c / c04d85a8. |
| MAC + 0x0b | 8 | USB interrupt enable mask; FM c04d8534. |
| PHY 0x11210800 + 0x68..0x6e | 8 each | Digital force/suspend/UART/device-mode fields; byte read/modify/write sites in LK 81e09310..81e0947e and FM usb_phy_recover establish ordinary non-clearing byte reads. Only reads here. |
| MAC + 0x204 + 16*n, n=0..7 | 16 each | Eight DMA control words, read-only observation. FM dma_controller_irq c03bdacc..c03bdae0, dma_channel_abort c03bcba0; upstream musb_dma.h/musbhsdma.c. Bit 0 is channel enable; zero at one instant is not proved permanent quiescence. |

Reuse pinned Linux 6.18, manufacturer d53dd75 sources and established FM/LK provenance. Focused FM review is retained as `evidence-private/20260909-m2-usb/fm-usb-state-functions.txt`; preceding functions remain in `fm-usb-functions.txt`, and LK in the established `lk.thumb.txt`. The exact MAC base is corroborated by LK 81e09034 onward and manufacturer mt_reg_base.h. PHY base is independently corroborated by LK 81e09292 onward and FM virtual f1210800 accesses. MUSB POWER and register widths follow pinned `drivers/usb/musb/musb_regs.h`; enable masks are distinct from status offsets 0x02/0x04/0x0a, which this probe never reads. No FIFO/INDEX access occurs.

Require successful PWRAP/CID/VUSB and all four clock reads, VUSB reported enabled, USB0 ungated, mux power-down clear and selector exactly 1 (observed supported handoff), PLL main/reference enabled with reset-bar bit 24 released, and PLL power-on/isolation-off. Reset-bar bit 24 is corroborated by FM sdm_pll_enable_op at c0041d14 (retained in fm-pll-reset-functions.txt), matching manufacturer mt_clkmgr.c; the commented alternative bit 27 is not used. No guessed clock frequency or sibling driver is selected. On refusal show clock values.

Claim MAC [0x11200000,0x11200280) and PHY [0x11210800,0x11210870) before any read; refuse existing claimants or mapping failure. Exact offset/width whitelist also guards the kernel adapter. Run once under the existing PID1-only cached diagnostic read. Preserve per-read validity (21 bits) and stop after any failure. No DMA addresses/counts, interrupt status acknowledgements, control writes, analog calibration, VBUS sourcing or USB mode switch. No actual UDC is enabled.

## Validation and hardware boundary

First access to these windows: full existing offline suite, production guard/ partial-read fault tests, ARM PID1 fixtures and emitted access-width/write review; one clean build and D08/current-memory/layout/BOOTIMG checks. No duplicate build or unchanged full provenance audit. Guards cannot recover a bus hang; show `READ USB STATE` before access and preserve 60 seconds from power-on maximum.

Success means `USB RC:0 VALID:001FFFFF`, raw POWER/DEV/HW, PHY68..6E, DMA0..7 control words and IRQ enable masks, plus continuing heartbeat and no new error. It does not mean enumeration or a ready PHY. The snapshot determines the next smallest initialization/ownership action; actual driver work still needs the remaining PHY/clock-provider/FIFO/IRQ/VBUS/DMA contract. #27 and M2 remain open.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
