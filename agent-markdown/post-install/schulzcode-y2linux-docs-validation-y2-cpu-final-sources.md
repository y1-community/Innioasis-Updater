---
title: "CPU Final source and register provenance - Innioasis Updater"
description: "CPU Final source and register provenance <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-cpu-final-sources.html"
---

# CPU Final source and register provenance - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# CPU Final source and register provenance

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# CPU Final source and register provenance > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-27. Source downloads and hashes are retained in private `out/cpu-final/source/{manifest,huawei-manifest}.json`. No binary dump, per-device identifier or protected calibration file is published here. Existing stock source identity remains `docs/knowledge/evidence/m4-power-source.json`; acquisition is not repeated. Linux reference version is the locked 6.18 archive/overlay inventory.[](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/arch/arm/mach-mt6582/)[](https://android.googlesource.com/kernel/mediatek/+/3be93a68c209393cfe24a842e2d5896a17ea37dc/arch/arm/mach-mt6582/)[](https://github.com/ferhung-mtk/android_kernel_huawei_h30t00/tree/3fec42ddadbefcf95c8fea4a10affb1c0abf5231/kernel-3.4/mediatek/platform/mt6582/kernel/core)[](https://documentation-service.arm.com/static/5f042da1dbdee951c1cd8c11)

| Source/version | Files/symbols | Applicability |
| --- | --- | --- |
| MediaTek sprout BSP d53dd75c | mt_dormant.c, cpu_dormant.S, mt_cirq.c/headers, mt_spm_sleep.c, mt_idle.c, mt_gpt.c, mt_cpufreq.c | Direct MT6582 register/protocol reference; PCM independently matched to Y2 binary. Android context assembly replaced with Linux helpers. |
| MediaTek BSP 3be93a68 | Same dormant/CIRQ/GPT/idle/power files | Independent version cross-check of register offsets, IRQ64 base, edge-only enable, explicit flush and L2 bit4. Adjacent platform paths are not imported. |
| Huawei MT6582 tree 3fec42dd | mt_dormant.c, mt_cirq.c, mt_idle.c, mt_spm_sleep.c, mt_cpufreq.c | Separate vendor tree corroborates the MT6582 protocol; board-specific OPP/PTP differences are not assumed applicable to Y2. |
| Retained Y2 FM kernel 7287acf1… | cpu_power_down at c003951c; retained generic_timer_setup, mt_gpt_init, boot_secondary/platform_cpu_die, stock tables; __pcm_dpidle | Primary board evidence. Existing narrow disassembly in out/m4-finish-reference/stock and out/platform-v1-hardware-ceiling/stock-reference, stock SLIDLE extracts in out/hardware-final/source-idle. |
| Cortex-A7 TRM | Dormant/reset, ACTLR.SMP, L1/cache ordering, generic timer | ARMv7-A context/coherency constraints. Linux's A7 implementation supplies the actual ported sequence. |
| Linux 6.18 | arch/arm/kernel/suspend.c, suspend.S, proc-v7.S, arch/arm/vfp/vfpmodule.c, drivers/irqchip/irq-gic.c, drivers/clocksource/arm_arch_timer.c, drivers/cpuidle/cpuidle.c, kernel/time/tick-broadcast.c | Architectural context, CPU/cluster PM, VFP, GIC and deadline lifecycle ownership. No duplicate custom register context. |
| Linux irq-mtk-cirq.c | v1 offsets, pending preservation discussion | Supports offset/pending model; newer hardware FLUSH bit is not applicable to retained MT6582 stock. A Y2 latch owner uses stock explicit pending replay. |
| Hardware02 real receipts12/16; earlier receipt49 | counter rollover/highres/nohz/checked hotplug; CPU restore/USB storm/WMT timeout | Evidence input, not fresh candidate qualification. Processor-stage WMT first restart failed, next complete restart succeeded. |

## Critical operations and ownership

Addresses are physical; vendor 0xF… static virtual aliases are never copied into MMIO calls. Ordering is stock sync-writel/DSB where controller strobes or coherency require it; ordinary Linux readl/writel supplies MMIO ordering elsewhere.

| Owner / operation | Register / mask / value | Prerequisite and restore |
| --- | --- | --- |
| GPT owner / counter | 10008000+60 GPT6 ctrl=30 then31; +64 clk=0, no IRQ bit5; high counter +78 | Exact 13 MHz GPT2 calibration, idle inherited registers. Restore original on failure, never reset a live counter. GPT6 stays free-running. |
| GPT owner / broadcast | GPT4 ctrl+40, clk+44=0, count+48, compare+4c; IRQ enable bit3 and ACK bit3 | Linux timer registration, same shared IRQ. GPT1 stopped and masked on promotion. Linux clockevent resume re-enables the selected timer. No runtime code claims GPT4. |
| ARM clockevent / per-CPU | CNTP_CTL p15 c14,c2,1; CNTP_CVAL mrrc/mcrr p15,2,c14; CNTFRQ c14,c0,0=13000000 | PPI29 physical routing from exact stock/receipt. Bounded per-CPU advancement/readback; CPU PM saves compare/control/frequency, disables before restoring compare then control/ISB. Tick owns deadlines. |
| CIRQ owner / clone | 10204000+40 ACK, +c0/+100 mask set/clear, +180/+1c0 sens set/clear, +240/+280 polarity set/clear, +300 control3 | CPU0 only, IRQs disabled, other cores physically off. 155 lines/5 valid banks; final valid mask07ffffff. Preserve parent-enabled pending events. |
| CIRQ owner / parent | GIC10211000 enable+100/clear+180, pending+200; config+c00; sysirq10200100 polarity | Read masks/config/polarity before masking SPIs, unmask only SPM149. Post CPU/cluster PM replay latch status into GIC pending-set, disable CIRQ control2, restore exact masks. |
| CCF / slow clock | TOP10000000+4 expected0f ->8f; PERI10003000+18 disabled bits, blocker00f00800 plus MSDC7800 | Sole CCF lock; CPU0/single online; unknown value or active clocks abort. Restore saved bus value and readback, persistent fault disables slow state. |
| CCF / runtime clock | TOP+70 audintbus clear07000000; PERI active mask02fe87fd plus7800; INFRA10001000+40 maska080 plusAFE bit5 | SPM verifies off domains; CCF lock excludes new consumers. Save/restore complete audio/bus mux words; readback fault disables deep path. |
| SPM / dormant PCM | 10006000 IM_PTR+318, IM_LEN+31c=479; CON0/CON1 keyed0b16; vectors0/9/28/68; APMCU_PWRCTL bit6 | Own coherent DMA 480-word stock program, both copies CPUs1–3 off, UART ACK bounded10x10us. Retained INFRA/DDRPHY, CPU dormant allowed, runtime GPT/EINT/AFE/CIRQ wake. Clean and reinstall normal 28-word PCM on every return. |
| SPM / system PCM | IM_LEN596, vectors0/26/55/99; bounded UART ACK, RTC/Power EINT wake, 600s timer plus30s WDT | Linux device suspend/secondary-off/PMIC prepare. Infrastructure retained. CPU/cluster PM, wake capture, clean normal PCM and CIRQ replay before devices. |
| Platform / boot resume | INFRACFG_AO+800=physical cpu_resume_arm, +804 bit31 | Shared CCF owner serializes boot/hotplug vectors. Stock boot-ROM dispatch only, no loader modification. |
| Platform / dormant context | MCU_BIU10208000 saved word; MCUCFG10200000 bit4 L2 reset-invalidate disable | Save before CPU suspend, restore on reset/abort. Linux MMU/CP15/VFP/GIC context remains separate. Cache flush/coherency exit and SMP/cache abort re-entry use Cortex-A7 helpers. |
| CCF/PWRAP/SPM / DVFS | ARMPLL via MAINPLL/2; PMIC220 selectors72/80/88; normal SPM voltage request604 bits2:0, ACK31 | Exact bin0, baseline1.15 V, slot/arbitration readback. Increase voltage then clock, decrease clock then voltage,40us settle. Error caps high OPPs; unsafe readback lowers clock. Existing source-backed policy tests cover rollback. |
| MUSB / quiesce restore | L1 mask11200000+a4=0; sampled W1C USB/TX/RX/DMA status; SOFTCONN POWER bit6 | Disconnect through gadget request owner; refuse any enabled DMA channel, no live buffer reset. Clear only quiescent system status before context/IRQ restore; preserve runtime/failed-DMA completion status. Restore exact runtime L1 gate after endpoints, connection for system enumeration, reset quiescent IRQ burst window. |
| CONSYS / restart containment | Existing reset/SPM/rail/BTIF/firmware owners | One retry only after all power/DMA/clock/rail flags off. New firmware/interface readiness precedes consumer success. No second app reconnect owner. |

## Port choices

The complete Android switcher/VFP/MMU/GIC assembly is not copied: Linux's CPU PM notifiers and cpu_suspend implement their own layout and exception return contract. The retained A7 uses integrated coherency, so no A9 SCU control is invented. Runtime DORMANT is single-CPU stock dpidle; no shared SPM program is swapped while four online cores execute. The separate vendor MCDI/SODI programs are research references, not silently treated as this board's validated runtime firmware. Normal four-core automatic policy uses schedutil and WFI; SLIDLE/DORMANT preflight never hot-unplugs cores or ignores active display/DMA clocks merely to claim entry.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
