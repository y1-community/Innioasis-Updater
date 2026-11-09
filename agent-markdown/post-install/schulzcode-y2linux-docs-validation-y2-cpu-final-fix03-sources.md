---
title: "CPU Final Fix03 source and evidence ledger - Innioasis Updater"
description: "CPU Final Fix03 source and evidence ledger <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-cpu-final-fix03-sources.html"
---

# CPU Final Fix03 source and evidence ledger - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# CPU Final Fix03 source and evidence ledger

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# CPU Final Fix03 source and evidence ledger > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Fix03 uses no new ROM, recovery or calibration input. The BSP files fetched for this batch are kept private in `out/cpu-final-fix03/source/`, with a SHA256 `manifest.json`, and go into the candidate's source collection. The [Fix02 ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX02-SOURCES.md) still covers MSDC, PWRAP, MUSB DMA and the RAM-console map.[](https://github.com/ubports/kernel_krillin/tree/874057f3c28735d606385361fb9a4cd4545ceba6/mediatek)``````````````````````````````````````````````````````````````[](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/?h=v6.18)````````````````````````````````````````````````

| Reference | Narrow use |
| --- | --- |
| BQ/Ubuntu krillin 874057f3platform/mt6582/kernel/core/mt_dcm.c and include/mach/mt_dcm.h | DCM_CFG is INFRA_BASE + 0x0004 (TOPCKGEN+4, "AXI bus dcm"). DCM_ENABLE_DCM_CFG is undefined, so DCM init never writes it ("default value are all 0, use default value"). bus_dcm_enable writes 1 << 7 \| 0xF (0x8f) and bus_dcm_disable clears only bit 7, so the stock steady state is 0x00, then 0x0f after the first idle |
| same, core/mt_idle.c | slidle_before_wfi/after_wfi and spm_dpidle_before_wfi/after_wfi call bus_dcm_enable/disable without checking the inherited value; the stock slidle PERI mask is 0x00f00800 |
| same, core/include/mach/mt_wdt.h, drivers/wdt/mtk_wdt.c | MTK_WDT_STATUS is +0x0c, with bits HWWDT 0x80000000, SWWDT 0x40000000, IRQWDT 0x20000000, DEBUGWDT 0x00080000, SPMWDT 0x0001. The stock driver only reads it (wdt_dump_reg, FIQ copy into NONRST_REG) |
| same, core/mt_spm_sleep.c | Reference for the SPM sleep/resume sequence around UART and wake. Fix03 changes nothing there |
| .../usb20/musb_gadget.c and musbhsdma.c (Fix02 ledger) | Stock RX keeps a packet pending without a request (rx_pending). The DMA IRQ handler is the same W1C/spurious-recovery path as upstream. A mode-0 RX packet costs one endpoint and one DMA interrupt |
| Linux 6.18 locked local source | suspend_devices_and_enter, suspend_finish (thaw, filesystems_thaw, PM_POST_SUSPEND, pm_restore_console), console_resume_all (pr_flush(1000, true)), upstream musb_g_rx/rxstate/dma_controller_irq, mtk_wdt_probe order, CONFIG_HZ_100 |
| Fix02 physical evidence out/cpu-final-fix02-physical-qualification/20260929T152328Z/ | x-rtc-retained.json: stage DEVICES_RESUMING, ring of balanced phase-8 pairs through faux, reset stamp 0x59325253. harness/ and usb-retest/usb-loaded-stress.json: ISR, DMA-interrupt and DMA-programming deltas. x-slidle-radios-off/result.json: slow_reject_bus and the clock mask. harness/slidle-coordinator.json: busy_percent=100, burst_ms=780 before the wake |

## USB arithmetic (Fix02 receipts)

| Run | ISR Δ | DMA-IRQ Δ | RX + TX DMA programs Δ | Upper bound if every packet costs two interrupts |
| --- | --- | --- | --- | --- |
| Boot 1 (harness) | 1155 | 597 | 512 + 99 = 611 | 1222 |
| Boot 3 (retest) | 916 | 473 | 407 + 81 = 488 | 976 |

The observed interrupt totals stay below the per-packet bound. A stuck source would have added at least 513 interrupts on top of it. The 513 counted in one 10-ms jiffy were therefore legitimate per-packet work, about 12 MB/s.

Only behavior corroborated by the MT6582 BSP and the physical Y2 receipts was used. No adjacent-SoC constant was imported. Whether the loader preserves `WDT_STATUS` until the kernel reads it, and which resume call stalls, are physical questions for the next owner run. Synthetic tests establish only the software contract.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
