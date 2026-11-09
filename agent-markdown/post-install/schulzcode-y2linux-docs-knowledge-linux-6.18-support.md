---
title: "Linux 6.18 boot-fundamentals audit - Innioasis Updater"
description: "Linux 6.18 boot-fundamentals audit <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-linux-6.18-support.html"
---

# Linux 6.18 boot-fundamentals audit - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Linux 6.18 boot-fundamentals audit

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Linux 6.18 boot-fundamentals audit > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Current hardware result: [owner-observed M1 runtime success](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm1-runtime-hardware-result.md) confirms Linux 6.18, native PID1, increasing BEAT/uptime, working sleep, proc/sysfs mounts, CPU0, D08 RAM visibility, framebuffer diagnostics and stopped-watchdog status. M1 core achieved. Exact flashed hash and unreported diagnostic fields remain unverified. Earlier dated statements below are historical.

Y2B-240 hardware result: the owner reports solid green, which the implemented state machine reaches through initramfs `/init` running as PID1. M1's Linux 6.18 plus PID1 boot objective is achieved. No heartbeat/checkerboard success is claimed. [Y2B-245 / D14](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fon-screen-diagnostics.md) is the offline follow-up for readable runtime diagnostics.

Hardware update 2026-09-08: [Y2B-240](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Ffirst-experiment-result.md) provides strong owner-observed evidence of the reviewed Linux 6.18 candidate reaching PID1 with static DT RAM and inherited framebuffer output. Timed heartbeat/stability validation remains unproven.

Y2E-150 adds an explicitly temporary board diagnostic overlay to audited v6.18: early AP watchdog stop plus guarded writes to LK-inherited RGB565 memory. Upstream MT6582 watchdog support exists, but normal probe cannot cover decompression. This is not full native display support. See [D12/D13](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frisk-accepted-diagnostic.md).

Date: 2026-09-08. Y2E-125, extended by [Y2E-130](https://github.com/SchulzCode/Y2Linux/issues/7). Status: source support CONFIRMED; Y2 execution UNKNOWN. Target remains upstream Linux 6.18 LTS, not 6.12 or a forward-ported Android kernel.

Pinned upstream tag: `v6.18`; tag object `f7b88edb52c8dd01b7e576390d658ae6eef0e134`; peeled commit `7d0a66e4bb9081d75c82ec4957c50034cb0ea449`. This is a reproducible architecture baseline, not a final selection of the 6.18.y patch release. The [kernel.org release page](https://www.kernel.org/category/releases.html) identifies the longterm series; that does not certify Y2 support. Successful source files/URLs/hashes are in [linux-6.18-sources.tsv](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/linux-6.18-sources.tsv). Failed/rate-limited requests remain explicitly recorded privately; claims below use retrieved primary source.

## Existing support in v6.18[](https://github.com/torvalds/linux/blob/v6.18/arch/arm/boot/dts/mediatek/mt6582.dtsi)[](https://github.com/torvalds/linux/blob/v6.18/arch/arm/mm/proc-v7.S)[](https://github.com/torvalds/linux/blob/v6.18/arch/arm/mach-mediatek/Kconfig)[](https://github.com/torvalds/linux/blob/v6.18/arch/arm/mach-mediatek/mediatek.c)[](https://github.com/torvalds/linux/blob/v6.18/arch/arm/kernel/devtree.c)[](https://github.com/torvalds/linux/blob/v6.18/arch/arm/kernel/time.c)``````[](https://github.com/torvalds/linux/blob/v6.18/drivers/irqchip/irq-mtk-sysirq.c)````[](https://github.com/torvalds/linux/blob/v6.18/drivers/clocksource/timer-mediatek.c)````````[](https://github.com/torvalds/linux/blob/v6.18/drivers/tty/serial/8250/8250_mtk.c)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fobservation-path.md)``[](https://github.com/torvalds/linux/blob/v6.18/drivers/watchdog/mtk_wdt.c)[](https://github.com/torvalds/linux/blob/v6.18/arch/arm/mach-mediatek/platsmp.c)[](https://github.com/torvalds/linux/blob/v6.18/drivers/mmc/host/mtk-sd.c)

| Fundamental | Exact source evidence | Implication for Y2 |
| --- | --- | --- |
| CPU / SoC | mt6582.dtsi defines four Cortex-A7 CPUs and mt6582 compatibility; proc-v7.S provides ARMv7 support. | A real MT6582 CPU0 foundation exists. |
| Platform selection | Kconfig supports ARCH_MULTI_V7 and selects GIC/MTK_TIMER. mediatek.c omits mt6582 from its compatible list. | Do not invent an mt6589 root compatible. devtree.c provides GENERIC_DT fallback; time.c has default OF clock/timer initialization. A legacy machine-ID 6582 port is not inherently required. |
| Interrupts | Cortex-A7 GIC at 0x10211000 / 0x10212000 plus additional CPU-interface ranges; sysirq at 0x10200100. irq-mtk-sysirq.c matches mt6577-sysirq fallback in the dtsi. | GIC and polarity-controller mechanisms exist; board behavior untested. |
| Timer | MT6577-compatible GPT, actual reg 0x10008000, length 0x80, SPI 112 active-low; timer-mediatek.c registers this compatible. | GPT is the starting timer. The dtsi node name is timer@11008000 but its reg says 0x10008000: derive MMIO from reg, and retain this inconsistency for review. |
| UART | Four disabled UART nodes at 0x11002000 through 0x11005000, SPI 51–54; mt6582-uart / mt6577-uart. 8250_mtk.c implements normal and earlycon paths. | Y2E-140 installed evidence selects UART0 at 0x11002000 / SPI51; D10 corrects the sole serial0/ttyS0 node and reruns offline validation. Physical pads, inherited routing and measured baud remain U10a. Evidence. |
| Initial clocks | dtsi supplies fixed 13 MHz system, 32 kHz RTC and 26 MHz UART clocks. | Minimal timer/UART scaffolding, not a full clock/reset/power implementation or independent clock measurement on Y2. |
| Watchdog | dtsi 0x10007000, mt6582-wdt / mt6589-wdt; mtk_wdt.c matches the latter. | Driver path exists; inherited state and experiment policy are unverified. |
| Secondary CPUs | mt6582 CPU nodes lack enable-method; platsmp.c does not establish mt6582 CPU-release semantics. | Use CPU0 initially. Four CPU nodes do not prove working SMP. |
| eMMC | No MMC node in mt6582.dtsi; mtk-sd.c has no mt6582/mt6589/mt6577 match. Audited clock/pinctrl directories contain no mt6582-named implementation. | Persistent storage needs additional research. A sibling compatible is not proof of hardware support. Start with initramfs. |

The [Prestigio tablet DTS](https://github.com/torvalds/linux/blob/v6.18/arch/arm/boot/dts/mediatek/mt6582-prestigio-pmt5008-3g.dts) is an upstream consumer of the SoC description. Its 1 GiB memory and UART choices are tablet settings, not Y2 evidence. No Y2 board description is established in these inputs. Panel, audio/DAC, controls, USB, charging, radios and complete clock/pinctrl support are outside the proof delivered here.

## DT kernel behind an ATAG bootloader

The [ARM boot protocol](https://github.com/torvalds/linux/blob/v6.18/Documentation/arch/arm/booting.rst) accepts tags or FDT through r2 and requires initialized RAM, suitable CPU/cache state and quiesced DMA. [boot-chain.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fboot-chain.md) traces stock LK's `r0=0`, `r1=6582`, `r2=0x80000100`, entry `0x80008000`, with ATAGs.

[ARM Kconfig](https://github.com/torvalds/linux/blob/v6.18/arch/arm/Kconfig) and [compressed/head.S](https://github.com/torvalds/linux/blob/v6.18/arch/arm/boot/compressed/head.S) support `ARM_APPENDED_DTB` for old loaders. The DTB belongs immediately after zImage inside KERNEL, not in an assumed Android DT section. This lets a DT-based upstream kernel run behind a loader that still supplies ATAGs; it does not require a legacy Android board-file port.

`ARM_ATAG_DTB_COMPAT` uses [atags_to_fdt.c](https://github.com/torvalds/linux/blob/v6.18/arch/arm/boot/compressed/atags_to_fdt.c), which accepts LK's two-word CORE tag and transfers standard MEM, CMDLINE, INITRD2 and SERIAL data. It does not translate vendor framebuffer/modem reservations. MEM can replace `/memory/reg`; default command-line policy replaces DT bootargs, while EXTEND appends loader arguments after DT arguments. A small DT memory range or clean DT command line therefore does not automatically win.

Y2E-130 now selects static DT memory with `ARM_ATAG_DTB_COMPAT=n`. LK's tags remain physically present but their RAM, command line and initrd properties are not imported. Controlled DT `/chosen/bootargs` uses ordinary command-line precedence; `/chosen/linux,initrd-start/end` use LK's fixed destination and the actual inner compressed payload length. See the [initial RAM policy](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Finitial-ram-map.md); no config was authored in the research phase.

## Y2E-130 memory and decompressor audit

Ten exact v6.18 files were retrieved from the official Torvalds Gitiles tree and hashed, including compressed/kernel head.S, both linker scripts, compressed Makefile and OF/ARM memory initialization. The full [RAM policy](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Finitial-ram-map.md) gives exact formulas, symbols and primary-source links. File-size-only reasoning is insufficient: the in-place zImage relocates itself, includes the appended DTB, compensates for kernel BSS and uses a stack plus 64 KiB malloc workspace. The linker requires appended-DTB file alignment and exposes the sizes needed for an offline verifier.

D08 admits 24 MiB low RAM plus 512 KiB at `0x84000000`, with all loading/decompression below `0x81800000`. Static OF memory scanning and chosen initrd properties support this sparse physical map; non-LPAE page tables occupy `0x80004000..0x80008000`. This is source-supported design, not a demonstrated execution or measured working-set claim. If a minimal build exceeds the declared caps, it must be reduced or returned for research review, never automatically given more RAM.

## Current decision boundary

The memory/import architecture is fixed sufficiently for a small offline implementation task after its precise issue is written. Target remains upstream Linux 6.18; retain preloader/LK, use appended DTB plus external initramfs and CPU0. Y2E-130 created no artifact or implementation issue.

The ARM boot requirement to quiesce DMA remains a separate unsatisfied launch condition (U07c). DT exclusions cannot enforce bus-master isolation. Installed loader/security, physical console and backup/recovery/power controls also remain gates. No hardware boot is authorized by closing the bounded memory-policy research.

## M1 offline implementation result

[The first candidate](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Ffirst-boot-result.md) compiles as Linux `6.18.0-y2-m1` using Clang/LLD 20.1.8. The precise baseline is upstream v6.18 plus [one Kconfig visibility patch](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fkernel-policy.md), needed because hidden ARM_VIRT_EXT otherwise defaults to y for CPU_V7. No C/assembly driver or board-file patch was required for this offline build. D08 remains static DT, appended DTB, no ATAG conversion and CPU0. All real ELF/DT/compression/package checks and two-clean-build byte comparisons pass.

Successful compilation proves that this configuration and artifact layout can be produced. It does not prove GIC/GPT/UART operation on this board, sufficient runtime memory, installed unsigned-image acceptance, inherited-state safety or recovery readiness. Those remain in the [hardware launch gates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Ffirst-boot-launch-gates.md). No device was touched.

## Y2E-145 first-experiment limit

The existing v6.18 artifact and D08 map are unchanged and retain their offline validation. [Normal package LK watchdog evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Flaunch-readiness.md) indicates a nominal 10-second interval; upstream kernel compilation and a disabled watchdog driver cannot guarantee a 60-second runtime. A minimal watchdog policy requires a separate reviewed decision after installed-handoff confirmation. No watchdog, USB observation, RAM logging or peripheral feature was added in this research. Hardware launch remains NO-GO.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
