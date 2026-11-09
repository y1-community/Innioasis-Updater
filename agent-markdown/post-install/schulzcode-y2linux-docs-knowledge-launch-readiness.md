---
title: "First BOOTIMG-only experiment: launch readiness - Innioasis Updater"
description: "First BOOTIMG-only experiment: launch readiness <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-launch-readiness.html"
---

# First BOOTIMG-only experiment: launch readiness - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# First BOOTIMG-only experiment: launch readiness

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# First BOOTIMG-only experiment: launch readiness > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Current: [risk-accepted diagnostic GO](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Frisk-diagnostic-result.md), pending separate flash authorization. The earlier candidate/assessment below is retained as history.

Current policy: [D11–D13 risk-accepted diagnostic](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frisk-accepted-diagnostic.md) supersedes the earlier absolute authentication/current-backup/full-handoff gates below. This document retains the historical assessment; watchdog, observation, verified recovery and BOOTIMG-only scope remain mandatory. No flash authorized.

2026-09-08 follow-up, [Y2E-145 / #17](https://github.com/SchulzCode/Y2Linux/issues/17), with [Y2E-140 / #16](https://github.com/SchulzCode/Y2Linux/issues/16). NO-GO for the first Linux hardware boot. The owner confirms only ordinary USB/ADB is available, with no additional UART hardware/evidence. Bounded offline analysis and read-only ADB improved the gates but did not pass them. No device mode change, DA execution, partition read/write, security modification, experimental boot or Linux feature change occurred.

The existing UART0 candidate stays byte-identical: BOOTIMG SHA-256 `574061649e10266927267b68afbc95da7fe0761dc9823e88767741bac9363fd9`, build `b4fcc12fc86d025dfa626c671db0eb611bf97943`. All 28 retained bundle members were rehashed successfully. D08 and all kernel/DT/initramfs bytes remain unchanged. Offline validation is not withdrawn; hardware readiness is explicitly rejected for the requested 60-second experiment.

## Observation: ordinary USB is not a verified early console

Fresh `/proc/consoles` still selects ttyMT0 / hardware UART0. The prior native-domain evidence remains 1.8 V, with 921600 8N1 the firmware-supported starting setting. Neither native PCB TX/GND pads nor voltage at an exposed point is confirmed. Further targeted public searches produced no usable Y2-specific pinout. The previously inspected teardown image remains revision-unmatched and unlabelled; no connection can be inferred from pad appearance.

The USB alternative now has actual FM preloader control-flow evidence, not only strings:
  - `0x0020b584` calls the detector at `0x0021065c`.
  - The detector configures PHY registers around `0x11210868`, then reads line-state at `0x11200620`. Comparisons at `0x002106d2` / `0x002106d8` recognize values 0xc0 or 0x80, print the Prolific/FTDI cable message, and return 1; other states take the USB/no-cable path and return 0.
  - A nonzero result at `0x0020b588` reaches `0x0020b596`, calling the UART-mode switch at `0x0020b024`, and records a mode flag. A zero result takes `0x0020b5a4`, the “Keep stay in USB Mode” branch.
  - The switch includes PHY changes and UART0's routing register at `0x11002090`; its sibling vendor implementation is already pinned in the previous observation capture. These are raw electrical/mux operations, not an Android ADB service or host serial protocol negotiated through the normal USB cable.

Consequently this lead does not make the owner's present USB/ADB cable an early serial receiver. Cable wiring/level/detection requirements and persistence through installed LK into Linux are still unknown. Native 1.8 V UART-pad data must not be applied blindly to USB connector pins. No guessed cable, resistor, host voltage or live PHY switch is justified.

Current `sys.usb.config` is `mass_storage,adb`; that reports the running Android gadget. The candidate has no USB controller/gadget or adbd. USB enumeration/disconnect monitoring would indicate only gross activity, not distinguish LK rejection, decompressor failure, kernel panic or PID1 progress. The existing last_kmsg export is a previous stock shutdown tail, not an early serial capture. A RAM-log alternative still needs a proved retained interval, compatible format/reader and reset preservation; none is established, and silently adding it would change the first-artifact architecture. Y2E-140 remains open.

## U07b: package secure boot is hardware-dependent

The owner-used FM preloader SHA-256 remains `1df1b62498754aab0c7ddc80a79d310a92fcf81f29b515730c562aaeeb6a884a`; LK is `bb1a93b4c1f02eab09ebad1314a8fdc25d94d3ca99771fc14e21cb18a289964a`.

The preloader contains `AND_ROMINFO_v` at file offset 0x4fc, version 2, and `AND_SECCTRL_v` at structure offset 0xd0. Its `m_sec_usb_dl` (+0xe4) and `m_sec_boot` (+0xe8) are both 0x22. Structure correspondence is independently supported by pinned MediaTek [sec_rom_info.h](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/masp/mt6582/asf/asf_inc/sec_rom_info.h) and [sec_ctrl.h](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/masp/mt6582/asf/asf_inc/sec_ctrl.h). No key material is published.

Exact LK instructions, rather than enum names from another source version, define the interpretation:``````````

| Input/path | Package LK behavior |
| --- | --- |
| Runtime ROM_INFO +0xe8 = 0x11 | 0x81e20262 returns 1: verification required. |
| +0xe8 = 0x22 or 0 | 0x81e2022e calls 0x81e27d1c, which reads bit 1 of 0x10206060. A set bit returns the S-CHIP/enabled result; clear returns NS-CHIP/0. Thus 0x22 is not unconditional disable in this LK. |
| Other +0xe8 | Invalid configuration/assertion path. |
| Normal security check, software-secure override absent, helper returns 0 | 0x81e207f8 branches to 0x81e209e0, the no-check path. |
| Helper returns nonzero | BOOTIMG verification/unlock/SEC_RO branches remain relevant; current seccfg state and normal-call arguments matter. |

The policy initializer `0x81e202b8` clears the runtime policy structure and writes zero to +0x10 (software-secure override) at `0x81e202e4` before ROM_INFO discovery. That default is not proof that later code or installed configuration cannot alter it. `0x81e236d4` searches PRELOADER for ROM_INFO; the observed package field is therefore an input candidate, not an installed RAM read.

Installed conclusion: unsigned-image acceptance remains unproved. No MMIO/security register was read or changed on the live device. ADB is uid 2000, ro.secure=1, ro.debuggable=0, bootloader/bootmode properties say unknown, and modern verified-boot/lock properties are empty. Android `test-keys`, adbd availability and ro.secure do not report this LK's hardware bit or partition verification policy. No accessible security-state export was established. `/dev/sec` and loader/boot device permissions exclude this shell. The successful owner SPFT operation establishes recovery compatibility, not arbitrary unsigned BOOTIMG acceptance.

Smallest remaining authentication proof: acquire installed loader identity and the selected secure-boot result through an established readback/stock-log route. A matching package loader plus independently observed NS-CHIP/no-check normal path could close this gate. If authentication is enforced, stop and use an owner-authorized supported signing route; do not alter fuses/seccfg, unlock as a workaround, patch verification or use an unsigned trial as the test.

## Current BOOTIMG recovery status

Fresh dumchar metadata agrees with the existing partition map. BOOTIMG occupies EMMC_USER [0x01d80000,0x02d80000), exactly 0x01000000 = 16,777,216 bytes. Scatter logical 0x03180000 is not the physical EMMC_USER readback address. UBOOT/LK is [0x01d20000,0x01d80000).

`/dev/block/mmcblk0` is root:system 0660, `/dev/bootimg` root:system 0640, and `/dev/uboot` root:root 0600. The ADB shell lacks system/root membership; `test -r /dev/block/mmcblk0` returns remote status 1. No raw read was attempted through those denied interfaces, and no privilege escalation/root restart was used. A package file or local generated boot-stock.img is not a current-device backup. There is no acquired current BOOTIMG backup or independent backup copy.

SPFT executable and bundled DA hashes were reverified. `history.ini` still names the FM scatter; authHistory is invalid/empty. `option.ini` points to `/tmp/SP_FT_Logs`, but that directory does not exist. Its Format_All_Download/Firmware_Upgrade/Download_Only flags describe available scenes, not historical selected mode. `CustomScene CheckedItems=9,11` is not a semantic, authenticated record of the prior write targets. The bundled readback XML targets another chip/partitions and is unsuitable as a Y2 recipe. The flasher was not launched.

The [prepared BOOTIMG-only runbook](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fbootimg-recovery-runbook.md) fixes exact ranges, artifacts, readback checks, restore selection and abort criteria. Operational gaps: exact DA/connection sequence from the successful use, actual raw acquisition, independent retention, and verified bounded write/readback semantics. Owner-proven v5.2032 recovery remains accepted; a destructive rehearsal or whole-device reflash is not requested.

## U07c: normal-boot watchdog is an adverse finding

The package LK arms the AP watchdog during platform initialization: direct call `0x81e00338 → 0x81e10e20`. At `0x81e10e7e` it passes 10 to `0x81e10df4`, whose write is `(10 << 11) | 8 = 0x5008` at 0x10007004. At `0x81e10ea4..0x81e10ea8` it ORs mode bits 0x5d plus key 0x22000000 into 0x10007000, then restarts via key 0x1971 at 0x10007008.

The pinned MediaTek [watchdog implementation](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/wdt/mt6582/mtk_wdt.c) defines the seconds-to-register conversion; [mt_wdt.h](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/arch/arm/mach-mt6582/include/mach/mt_wdt.h) identifies enable, external reset, IRQ and dual-mode bits. This is a nominal 10-second interval with IRQ/dual-mode behavior, not a measured claim that the board resets exactly ten seconds after kernel entry. Remaining count, clock tolerance, dual-stage timing and other watchdogs are not measured.

A real disable helper exists at `0x81e10ddc` (clear enable bit 0, keyed write). Its identified direct callers are Download boot at 0x81e006c8 and fastboot_init at 0x81e18ad6. These are not the normal BOOTIMG launch path. The normal final sequence at `0x81e1816c` calls platform cleanup `0x81e00458`, then interrupt/cache/MMU cleanup before kernel entry. The platform cleanup contains LED and GIC cleanup, not that watchdog-disable helper. Nearby 0x7000 register-offset matches were checked: display accesses are at 0x14007000, not AP_RGU 0x10007000. No normal-handoff AP watchdog disable was established.

Decision: Treat an armed watchdog as inherited until installed evidence proves otherwise. Current M1 has no watchdog driver or service. It cannot be approved as a 60-second unattended diagnostic run. Do not silently substitute Download/Fastboot entry, shorten success criteria, or patch the candidate merely to work around an unverified installed handoff. A reviewed minimal watchdog policy may be required once installed normal-path behavior is established; D08 does not need expansion for this research finding.

Other bounded handoff findings:

| Concern | Evidence and limit for this experiment |
| --- | --- |
| eMMC DMA | Exact package stop routine 0x81e05334 sets DMA control at +0x98, issues DSB, then polls active bit at +0x9c until clear (0x81e0535e..0x81e05362). Previously traced normal storage use supports storage DMA quiescence. Installed identity remains unverified. |
| Display / modem / connectivity bus masters | D08 omits identified framebuffer/modem/connectivity storage; first Linux enables none of their drivers. Final LED/GIC cleanup is not proof those masters cannot access low RAM. No new full-peripheral investigation or blind register sweep was undertaken. |
| CPU / secure state | Existing package SVC/r0-r2/cache/MMU contract remains the candidate architecture. D09 explicitly excludes hyp startup; no PSCI/SMP support is introduced. Exact installed loader and secure/shared-memory behavior still require corroboration. |
| Power | Fresh Android battery service still reports contradictory duplicated fields (100/50%, present true/false) while USB-powered. This is not trusted independent power evidence. No power transition was attempted. |

The watchdog finding alone is enough to reject the requested timing premise; additional broad peripheral bring-up is unnecessary to reach today's decision.

## Decision and smallest next evidence boundary

NO-GO. Observation, installed authentication, current-device recovery backup/operational procedure and watchdog/entry assurance remain open. No first experimental boot issue was created. A host-only script or another offline rebuild cannot supply the missing physical/installed facts.

Next work should obtain a safe acquisition/observation route: either verified UART hardware/pinout, or a fully specified supported USB accessory/readback route with the operator able to perform the required physical connection/power steps. Do not infer that the ordinary connected ADB cable meets either requirement. Acquire and independently retain current BOOTIMG (and required recovery/personalized evidence), establish installed loader/security lineage, and then resolve the normal-path watchdog policy before reconsidering GO. No preloader/LK/table/calibration write is part of that boundary.

Private evidence group `20260908-launch-gates/` includes exact command/status/UTC records, package slices, full preloader disassembly for audit, ROM_INFO values, pinned sources, local SPFT settings and artifact-preservation results. Hashes are in [capture-index.tsv](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/capture-index.tsv). Disassembly annotations are leads and were checked against local instructions at the cited branches; literal pools and sequential register annotations are not treated as proof of reachable execution or runtime values.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
