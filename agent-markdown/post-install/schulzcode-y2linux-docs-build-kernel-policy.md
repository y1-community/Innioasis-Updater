---
title: "First-boot kernel and console policy - Innioasis Updater"
description: "First-boot kernel and console policy <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-kernel-policy.html"
---

# First-boot kernel and console policy - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# First-boot kernel and console policy

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# First-boot kernel and console policy > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Current diagnostic overlay: [D11–D13](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frisk-accepted-diagnostic.md) adds a board-specific early watchdog stop and guarded inherited-video writes. The general watchdog/display driver stacks remain disabled; D08 RAM and UART0 remain exact. Older no-display/no-watchdog artifact descriptions below refer to the prior candidate.

D08 is unchanged. Configuration starts from allnoconfig and `kernel/config/first-boot.config`; resolved configuration is checked, never trusted merely because a fragment requested an option. The ARMv7 generic DT machine fallback handles `mediatek,mt6582`; no false MT6589 board compatible is added. ARCH_MEDIATEK supplies GIC, sysirq, common clocks and MTK GPT support. No arch timer/SMP/PSCI startup is selected.

## D09 — Make the existing D08 no-hypervisor selection enforceable

On 2026-09-08, configuration resolution stopped: v6.18 `arch/arm/mm/Kconfig:706` declares ARM_VIRT_EXT as a hidden bool with `default y if CPU_V7`. Kconfig ignores an explicit `n` for this hidden symbol. Accepting its resolved `y` would violate D08. [Upstream Kconfig](https://github.com/torvalds/linux/blob/v6.18/arch/arm/mm/Kconfig) and the guarded entry paths in `arch/arm/boot/compressed/head.S`, its Makefile, `arch/arm/kernel/head.S`, kernel Makefile and `arch/arm/include/asm/virt.h` were reviewed.

Decision: apply a one-line Kconfig prompt-visibility patch, under EXPERT, so the existing `n` code path can be selected. Preserve the upstream default. This adds no C/assembly/hardware behavior and changes neither memory limits nor the D08 entry contract. The audited release archive remains pristine. The build mounts exactly one generated Kconfig file over its original path; base/result hashes and an exact unified diff are checked against `kernel/patches/manifest.json`. Consequently the honest baseline description is v6.18 plus one Kconfig visibility patch, not unmodified v6.18. No hand-edit of generated `.config` or compiler macro override is used. Built ELFs must contain no hyp startup symbols.

This deliberately requires the SVC entry contract traced from FM LK. It does not make entry from HYP safe or close installed-loader/secure-state gate U07c. If installed LK differs, return to research before launch. Other configuration corrections remove obsolete EMBEDDED and unnecessary TMPFS; initramfs uses built-in ramfs and requires no shmem.

## Candidate diagnostic serial path (U10a remains open)

[D10 / Y2E-140](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fobservation-path.md) corrects the sole controller to UART0 at `0x11002000`, IRQ51, 26 MHz, exposed as Linux `ttyS0` through alias `serial0`. Fresh installed `/proc/consoles`, sysfs and `/proc/iomem`, plus remapped FM driver instructions, supersede the earlier package-default UART3 candidate. The normal console requests 921600 baud, eight data bits, no parity, one stop bit. This rate is supported by package LK but still requires actual stock wire capture; no physical pinout or live baud is claimed.

The upstream MT6577-compatible 8250 driver supports this audited MT6582 block. Its OF earlycon sets 32-bit accesses with register shift 2. The generic earlycon parser can set device baud before that callback, so stdout-path is exactly `serial0` (no suffix), and current-speed is omitted. With baud zero, early_serial8250_setup only masks UART interrupts and preserves the inherited baud until the normal console configures it. The ordinary driver uses the unnamed fixed clock fallback from upstream mt6582.dtsi; no bus-clock register/pinctrl data is invented. Serial DMA is compiled out and no DMA properties are supplied. Full serial probe writes UART registers, so compilation is not evidence of physical console safety.

Chosen bootargs: `rdinit=/init earlycon console=ttyS0,921600n8 loglevel=8 ignore_loglevel panic=0`. `earlycon` discovers `/chosen/stdout-path`; no `keep_bootcon` duplicate writer. Panic remains halted for observation. No console is promised before decompressor completion: DEBUG_LL is off because reliable physical routing/entry initialization is unproved. U10a must establish port selection, pinout/voltage, captured stock output and an observation path before this candidate can be launched. A different confirmed port requires a reviewed artifact revision.

The final fragment fixes `PHYS_OFFSET=0x80000000`, `ARM_PATCH_PHYS_VIRT=n` and 3G/1G virtual split (`PAGE_OFFSET=0xc0000000`). An allnoconfig physical-base default of zero is not acceptable for this board; the actual artifact checkpoint added these explicit checks before accepting a payload. The kernel virtual entry is `0xc0008000`, while the physical entry is `0x80008000`. The validator reconstructs Image from ELF section load addresses, including high-VMA ARM vectors/stubs, and compares every byte. It also checks the compressed ELF layout table, LC1 stack pointer, gzip contents and embedded inflated-size/BSS words.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
