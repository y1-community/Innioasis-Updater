---
title: "USB DMA observations and current scope - Innioasis Updater"
description: "USB DMA observations and current scope <!-- knowledge-base-scope: maintained-summary; baseline02-sync 2026-10-03 -- Current Baseline02 / UART01 scope UART01 bounded USB c"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-usb-dma-observation.html"
---

# USB DMA observations and current scope - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# USB DMA observations and current scope

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# USB DMA observations and current scope

## Current Baseline02 / UART01 scope

UART01 bounded USB checksum regression passes three 1 MiB bidirectional rounds with an independent Wi-Fi observer. Baseline02 retains that repaired source. Lifetime allocation/program counters still do not prove payload completion or wire throughput. The earlier source/guard descriptions and failure notes below belong to their exact snapshots; use current kernel source and the UART01 receipt for current behavior. Endurance, host-sleep/reconnect and full-suspend restoration remain separate.

[Baseline02 seal](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md), [UART01 hardware](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) and [current state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md) carry exact identities, counters and limits.

## Historical source research and physical checkpoints

The following text retains earlier dated decisions and results. Its “current”, “next” and candidate labels belong to those sessions; the Baseline02 summary above takes precedence. Historical failures and seal-time NOT_RUN receipts remain evidence for their exact images.

# Hardware Final USB DMA observations

Latest physical boundary, 2026-09-27: Fix01's first small SHA-checked USB transfer passes, but the next transfer loses connectivity while UI remains usable. These lifetime counters do not reveal the failed interval after the owner's restart. Loaded transfer recovery and full suspend restoration remain unqualified. [Actual result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md%23playback-connectivity-and-recovery&anchor=playback-connectivity-and-recovery).

The sole active peripheral adapter is `kernel/platform/usb.c`. Hardware 02's physical census on 2026-09-27 reports Inventra DMA active, advancing DMA IRQs and zero DMA errors. This establishes activity, not the throughput ceiling, channel utilization, or suspend qualification.

Hardware Final adds read-only fields to the existing `/sys/devices/platform/11200000.usb/status` interface:````````````````````````````

| Fields | Meaning |
| --- | --- |
| transfer, dma_irqs, dma_errors | Existing controller mode, aggregate DMA IRQs and detected bus faults |
| dma_allocations, dma_alloc_failures, dma_releases | Successful upstream channel allocations, allocation refusals and normal release calls |
| dma_allocated | Currently allocated channels; allocation does not imply an in-flight transfer |
| dma_rx_programs, dma_tx_programs | Accepted upstream channel-program calls, from the device's perspective |
| dma_rx_programmed_bytes, dma_tx_programmed_bytes | Bytes in those accepted programming requests; not completed bytes, wire traffic or TCP goodput |
| dma_program_failures | Upstream programming refusals; normal PIO fallback may follow |
| dma_aborts, dma_abort_failures | Abort calls and their nonzero returns; an idle-channel abort is still a call |

Totals span the driver's lifetime. Teardown resets the current allocation gauge; upstream emergency controller stop may release remaining channels directly, so allocation minus normal releases is not a substitute for the gauge. RX/TX classification follows allocation direction, independently of DMA mode 0/1. Atomic 64-bit totals avoid torn reads and short byte-counter wrap on ARM32. Each field is individually coherent; the whole multiline report is not an atomic snapshot of ongoing traffic. Use bounded before/after deltas.

The wrappers delegate allocation, programming, abort and release unchanged. Allocation/program failure remains the upstream result. Existing `y2.usb_dma=off`, allocation fallback, 32-bit DMA addressing, peripheral-only role and terminal bus-fault teardown remain in force. Throughput and CPU cost must be remeasured on the final candidate, including instrumentation cost.

The existing IRQ-overflow snapshot retains sampled L1/core/endpoint status and masks before teardown. The Physical 01 suspend failure alone does not prove a particular stuck endpoint, bad restore ordering, or a DMA defect (that image used PIO). Hardware 02 introduced the snapshot; a repeat failure's retained snapshot is required before attributing its root cause. The current 512-IRQs per-jiffy guard remains unchanged. High IRQ rate is not independently proof of an electrical fault; retain throughput, elapsed time and status when it fires.

Targeted host validation extracts and executes the actual wrappers, covering successful delegation, allocation exhaustion/reuse, rejected programming, RX/TX direction independent of mode, byte totals crossing 4 GiB, and abort failure propagation. The existing USB lifecycle/recovery tests and DMA bus-error teardown test also pass. These checks do not certify physical throughput, reconnect, suspend or fault recovery.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
