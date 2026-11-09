---
title: "M2-USBCLK-01 — inherited USB clock state - Innioasis Updater"
description: "M2-USBCLK-01 — inherited USB clock state <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m2-usb-clock-probe.html"
---

# M2-USBCLK-01 — inherited USB clock state - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2-USBCLK-01 — inherited USB clock state

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2-USBCLK-01 — inherited USB clock state > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

[Physical result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-clock-hardware-result.md): all four clock reads pass, timer reporting works, and BEAT 50 is photographed without errors. The next bounded step is [read-only USB state observation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-state-probe.md).

2026-09-09. Smallest next #27 prerequisite after [physical PWRAP/VUSB success](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-pwrap-hardware-result.md). Correct the source- identified timer action-name parser error in the same localized candidate.

## Exact read-only contract

Read only four 32-bit always-on clock control/status registers. Do not enable, disable, reset, switch or measure a clock, and do not access USB MAC/PHY/DMA or analog calibration registers. A clock source selection number is raw evidence; do not assign an unproved frequency to it. This determines the inherited gate state before specifying safe MAC/PHY access or a minimal clock provider.````````````````````````````

| Physical read | Meaning / exact FM corroboration |
| --- | --- |
| 0x10003018 | PERI_PDN0_STA. FM CG_PERI descriptor at 0xc09b1a6c points to virtual 0xf0003018; vendor clock ID 10 is PERI_USB0. Status bit 10=1 means gated. |
| 0x10000060 | CLK_CFG_2. FM MUX_USB20 descriptor at 0xc09b1900 points to 0xf0000060, selector mask 0x70000, gate mask 0x800000, shift 16, three inputs. Preserve shared SPI/UART/MSDC fields. |
| 0x10209220 | UNIVPLL_CON0. FM UNIVPLL descriptor at 0xc09b1720 points to 0xf0209220; FM USB clock enable at 0xc04d9b24 reads/modifies bit 26. Snapshot only, not a PLL programming contract. |
| 0x1020922c | UNIVPLL_PWR_CON0. Same FM descriptor points to 0xf020922c; observe raw inherited power/isolation controls. |

Pinned manufacturer `arch/arm/mach-mt6582/mt_clkmgr.c` at commit d53dd75, SHA-256 `f73bbe0a4c3c07e2831e4c2bc5cabd3de7909c52e2ce572863fabfc46eadbc8d`, corroborates the descriptors (`MUX_USB20`, `UNIVPLL`, `CG_PERI`) and ordinary non-clearing register reads. Header/source and focused FM descriptor extraction are retained under `evidence-private/20260909-m2-usb/`; existing FM provenance is reused. [Manufacturer source](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/arch/arm/mach-mt6582/mt_clkmgr.c).

Claim each four-byte resource before mapping; refuse an existing claimant or mapping failure. These providers are not enabled in the current kernel. Run only after successful PWRAP/CID/VUSB reads with reported VUSB enable set. Cache all results once per boot. Preserve a validity mask so partially acquired evidence cannot be mistaken for a zero register. An MMIO bus hang itself is not software- timeout recoverable; show the pre-probe stage before access and preserve the established 60-second manual test/recovery boundary.

Show PWRAP RC/valid and CID/VUSB alongside CLOCK RC/valid, PERI/MUX and PLL/PWR. No USB controller or PHY register is read until its prerequisite contract is established. A successful clock snapshot is not an observed 48 MHz waveform, USB enumeration or permission to alter a shared PLL.

## Timer parser correction

`timer-of.c` uses `np->full_name` as request_irq's action name. Match the complete DT action token `timer@10008000` (optional leading slash), in a numeric IRQ row, instead of `mtk-clkevt`; reject substring matches, unrelated timer addresses, non-numeric counts and diagnostic summary lines. CPU0's first decimal counter is sufficient because SMP remains disabled. The existing read limit is unchanged.

One clean build, affected parser/PID1/probe tests, emitted read-only adapter review and D08/layout/BOOTIMG checks suffice: no memory, DMA or packaging policy change. Hardware test must show increasing timer counts, continued heartbeat through the STOP stage, and all raw clock fields/validity. #27 remains open until its full controller/PHY/VBUS/FIFO/IRQ/DMA and host-log evidence is established.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
