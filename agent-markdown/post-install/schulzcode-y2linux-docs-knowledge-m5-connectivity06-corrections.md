---
title: "CONNECTIVITY-06: rearm APDMA TX completion for each transfer - Innioasis Updater"
description: "CONNECTIVITY-06: rearm APDMA TX completion for each transfer <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate ide"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m5-connectivity06-corrections.html"
---

# CONNECTIVITY-06: rearm APDMA TX completion for each transfer - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# CONNECTIVITY-06: rearm APDMA TX completion for each transfer

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# CONNECTIVITY-06: rearm APDMA TX completion for each transfer > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

CONNECTIVITY-05 physically leaves the final two bytes of its first 26-byte STP/WMT command in TX DMA (`wpt=0x1a rpt=0x18 valid=2 flush=0`). RX stays empty and no TX interrupt is serviced. MD calibration and Linux stability remain intact.

TX interrupt enable is a hardware-cleared threshold enable, as documented in pinned Linux 6.18 `drivers/dma/mediatek/mtk-uart-apdma.c`. The retained stock `hal_dma_send_data` masks TX IRQ while filling, enables DMA before publishing WPT, and enables the interrupt after every submission. Native code instead armed it only once on the empty FIFO at startup, and published WPT before EN.

Restore the stock per-transfer order: mask TX IRQ, copy/coherently publish, enable DMA, advance WPT, flush an already-short tail and rearm TX IRQ. The threaded IRQ handles a tail that becomes short asynchronously. Clear its flag under the same TX mutex. Leave TX IRQ disabled while idle at initialization. Reject STOP before submitting; never combine STOP and FLUSH. Timeout diagnostics now include the TX interrupt-enable readback, without payloads or addresses.

The regression executes the actual send/IRQ functions against a FIFO model with hardware-cleared IRQ enable and asynchronous eight-byte bursts. It reproduces the exact 26-byte stall with CONNECTIVITY-05, passes repeated submissions, all short-tail residues, buffer wrap, full chunks and rejected STOP/flush/space waits with the correction. This is a verified code fix; physical radio readiness still requires the new image. No padding, busy polling workaround, global APDMA reset, new clocks, firmware change, M4 redesign or protected write is introduced.

Build a production BOOTIMG-only update retaining CONNECTIVITY-03 root and Y2DATA. Then stop for manual owner installation and inspect startup/IRQ progression. Continue the existing coherent M5 qualification once interfaces become usable.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
