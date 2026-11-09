---
title: "CPU Final Fix02 source and binary ledger - Innioasis Updater"
description: "CPU Final Fix02 source and binary ledger <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-cpu-final-fix02-sources.html"
---

# CPU Final Fix02 source and binary ledger - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# CPU Final Fix02 source and binary ledger

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# CPU Final Fix02 source and binary ledger > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Retained sources were read without reacquiring ROM/recovery/calibration. New bounded extracts and fetched BSP files are private in `out/cpu-final-fix02/source/` with a SHA256 `manifest.json`, and are included in the candidate's source collection. Fix01's ledger remains valid for timers, GPT/CIRQ, SPM PCM and the RAM-console map.[](https://github.com/ubports/kernel_krillin/tree/874057f3c28735d606385361fb9a4cd4545ceba6/mediatek)````````````````````````````````````````[](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/?h=v6.18)``````````````````

| Reference | Narrow use |
| --- | --- |
| BQ/Ubuntu krillin 874057f3platform/mt6582/kernel/drivers/mmc-host/{mt_sd.h,sd.c} | MT6582 MSDC register map (no PATCH_BIT2/PAD_DS/EMMC50/FIFO_CFG); stock msdc_clksrc_onoff: MS mode, PERI MSDC CG only, 10 µs, SD/MMC mode, CKSTB; SDC_STS/FIFOCS/DMA_CFG busy bits |
| same, drivers/pmic_wrap/pwrap_hal.{c,h} | Register offsets MUX_SEL 0x00, WRAP_EN 0x04, HIPRIO_ARB_EN 0x50, DVFS_ADR/WDATA 0xe4..; arbiter channels MDINF..GPSINF bits 0..6 (DVFSINF bit 4); pwrap_init writes 0x1ff; WRAPPER_MODE 0 |
| same, core/include/mach/mt_musb_reg.h, mediatek/kernel/drivers/usb20/musbhsdma.c, include/linux/musb/musbhsdma.h, usb20/musb_gadget.c | 8 HSDMA channels, bus-error bit 8, W1C DMA interrupt handling and spurious-IRQ BUSY/count recovery identical to upstream; RX mode-1 selection |
| Retained Y2 FM preloader SHA256 1df1b624…6884a | Arbiter literal 0x1000d050 at file 0xc6e8/0xca08 (ldr r5 at 0xc42e); final movw r1,#0x1ff; str r1,[r5] at 0xc954 (32-byte extract preloader-pwrap-arbiter-store.bin, disassembly preloader-pwrap-init-arbiter.asm). RAM-console guard at 0xacce only rewrites on magic 0x43474244; its else-branch callee writes a DRAM argument block. SRAM literals: 0x0010c000..0x0010c4ac, 0x0010dc00 (guard), 0x0010f040.., never 0x0010dc04..0x0010e0ff |
| Retained Y2 LK SHA256 bb1a93b4…9964a | SRAM references 0x0010f000..0x0010f648; two halfword-aligned matches 0x0010e310/0x0010e352 at odd code offsets lie above the claimed window |
| M2-PWRAP-01 physical photograph evidence-private/20260909-m2-pwrap-result/50.jpg (SHA256 853c2055…6e225) | Real Y2 readback MUX:0 WRAP:1 WACS:1 INIT:1 ARB:0000007F with the same preloader |
| Linux 6.18 locked local source | mtk-sd.c runtime/system PM ops and mmc_rescan card detect; drivers/base/power/main.c callback runner, prepare/complete; kernel/power/suspend.c stages and pm_test; mtk_wdt.c start/stop/ping, suspend/resume only for core-active watchdogs; lock_system_sleep() flags; MUSB indexed endpoint registers and musbhsdma IRQ path |
| Fix01 physical report | Runtime-suspended MMC with enabled CGs, 0x3000, quarter-second bursts, invalid SRAM records, USB loss with live UI, HOLD/"Not charging" with USB online |

Only register behavior corroborated by at least two of the MT6582 BSP, the retained Y2 binaries and a physical Y2 readback was used. No adjacent-SoC constant was imported. The MT6582 arbiter field width follows from the BSP's seven channels plus the physical 0x7f readback of a 0x1ff write; the MSDC register image follows from the BSP map; the RGU backstop uses only the existing upstream MT6582/MT6589 watchdog driver.

Source inspections establish register/software contracts. Synthetic tests establish error handling. Only the next owner-controlled physical receipts can establish actual gating, parking, voltage, wake and USB behavior.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
