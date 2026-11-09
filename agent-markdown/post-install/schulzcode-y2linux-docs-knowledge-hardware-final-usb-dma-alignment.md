---
title: "USB DMA alignment evidence and current regression - Innioasis Updater"
description: "USB DMA alignment evidence and current regression <!-- knowledge-base-scope: maintained-summary; baseline02-sync 2026-10-03 -- Current Baseline02 / UART01 scope UART01 pa"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-hardware-final-usb-dma-alignment.html"
---

# USB DMA alignment evidence and current regression - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# USB DMA alignment evidence and current regression

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# USB DMA alignment evidence and current regression

## Current Baseline02 / UART01 scope

UART01 passes three 1 MiB bidirectional USB checksum rounds with an independent Wi-Fi observer, after idle qualification, same boot and no filesystem errors. The current source retains alignment and progress-aware DMA protections. Earlier failed transfers remain historical evidence for those images; bounded success does not qualify large-transfer/reconnect/host-sleep endurance or USB host/VBUS.

[Baseline02 seal](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md), [UART01 hardware](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) and [current state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md) carry exact identities, counters and limits.

## Historical source research and physical checkpoints

The following text retains earlier dated decisions and results. Its “current”, “next” and candidate labels belong to those sessions; the Baseline02 summary above takes precedence. Historical failures and seal-time NOT_RUN receipts remain evidence for their exact images.

# Hardware Final: ECM request alignment and Inventra DMA

Latest physical boundary, 2026-09-27: Fix01 passes one 256-KiB bidirectional hash transfer, then loses USB connectivity during the next transfer while the display/UI remains usable. The failed-interval DMA/IRQ observer was lost and the precise transport cause is unknown. Do not infer that the earlier alignment correction failed, that the old IRQ storm returned, or that sustained DMA/recovery qualified from a single small transfer. [Fix01 physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md%23playback-connectivity-and-recovery&anchor=playback-connectivity-and-recovery).

2026-09-27 source correction; physical execution of the new kernel remains pending. Hardware 02 reported an allocated Inventra controller while its DMA IRQ counter stayed at six over large bidirectional ECM transfers. USB throughput remained near the PIO baseline. Allocation is not evidence of payload DMA.

The pinned Linux 6.18 source explains a concrete mismatch:
  - `u_ether.c::rx_submit` allocates an aligned skb, then reserves

`NET_IP_ALIGN` (two bytes) unless the gadget has `quirk_avoids_skb_reserve`. Hardware 02 does not select that quirk. USB receives into `skb->data`.
  - `musb_gadget.c::map_dma_buffer` maps that exact data pointer.

`musbhsdma.c::dma_channel_program` rejects addresses not divisible by four for controller RTL 1.8 or later. Its comment documents hardware masking the bottom two address bits; bypassing the guard would corrupt data.
  - Transmitted Ethernet skbs commonly also start two bytes off a word boundary

because their IP headers are aligned. Omitting the RX reserve alone does not fix this TX path. USB TX queues the final `skb->data` after protocol wrapping.

This strongly supports silent PIO fallback as the cause of the observed lack of DMA progress. The old image does not expose actual request-address rejection counters, so source analysis alone is not a physically observed DMA rejection.

The correction selects the existing gadget no-reserve quirk only after the Y2 DMA controller is successfully allocated. Explicit `y2.usb_dma=off` and DMA allocation failure retain the previous PIO skb layout. A new pinned u_ether overlay copies only misaligned TX buffers, after ECM/protocol wrapping, through `skb_copy_expand` with word-aligned headroom. The kernel helper preserves packet contents and checksum/header metadata. If atomic allocation fails, it keeps the original skb and the existing controller alignment guard retains PIO fallback. It never changes the frame on the wire or disables the hardware alignment guard.

RX changes where the Ethernet header resides, so IP/checksum alignment must be considered explicitly. This Y2 config selects ARMv7 efficient unaligned access and disables IPv6. The pinned ARM `csum_partial` has byte/halfword alignment handling; `ip_fast_csum` uses single-word LDR instructions supported unaligned on this CPU. An executable built from the exact `ip_fast_csum` assembly checks 2,816 IPv4 header patterns and lengths at both word and halfword alignment against a scalar checksum. It passes ARM QEMU. This does not replace physical DMA, checksum and data-integrity qualification, and is not an assertion about other ARM architectures or future IPv6 configurations.

The existing DMA allocation/programming observer now also counts rejected misaligned programming requests as `dma_alignment_rejects`. Accepted programming bytes are deliberately not labelled USB delivery or application throughput. Host tests execute the actual patched TX helper and cover no-copy, copy, byte/metadata preservation, atomic allocation failure and original ownership; DMA observer tests preserve callback return values and count alignment rejects.

Final same-boot qualification must capture the new counters before and after RAM-to-PC and PC-to-RAM transfers, then storage-backed transfers. Require increasing directional DMA program counts/bytes and IRQs, checked DNS/TCP, payload hashes, stable RX/TX error counters, no DMA bus faults, and reconnect and suspend recovery. Compare PIO only through the existing owner-controlled boot fallback. A faster configuration is not qualified until its measured throughput/CPU/temperature and failure behavior are retained. This repair needs no intermediate flash to complete the independent campaign source work.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
