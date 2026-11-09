---
title: "Storage03 correction candidate - Innioasis Updater"
description: "Storage03 correction candidate <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-storage03-corrections.html"
---

# Storage03 correction candidate - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Storage03 correction candidate

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Storage03 correction candidate > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

The owner's 2026-09-13 DIAG01 photos show Linux alive, internal MMC at 15269888 sectors, no exported partitions, and both filesystem resolvers absent/rejected. The storage warning's command/argument is outside the photographed 60-column window. The rejected opcode is unknown. USB is PREFLIGHT -19, configured=0, polls=0, IRQ=0; initial CHRDET=007b, wake=-19/written=0. These are failures, not physical acceptance. Original photographs are retained privately under evidence-private/20260913-storage-diag01-owner.

The owner also reports cable-dependent startup, ineffective off-state buttons, and apparent SD-dependent progress. Earlier no-SD console evidence proves Linux can execute without SD; it does not prove internal Buildroot boot. Empty-slot CMD55/CMD8 logs were obscuring rescue. There is no new evidence establishing why stock power entry behaves differently. Kernel/root/data changes cannot be claimed to repair a fault before Linux executes; no speculative PMIC, battery, preloader, LK or MISC changes are made.

## Request boundary

Locked Linux 6.18 drivers/mmc/core/block.c prepares bounded multiblock requests in mmc_blk_rw_rq_prep, and mmc_blk_part_switch may reselect EMMC_USER after its partition cache is invalidated during error recovery. Storage03 accepts CMD23 only as a companion to a 512-byte CMD18/CMD25 transfer on the identified user area, with the exact block count. Reliable-write and metadata-tag bits are accepted only for range-checked writes, as required by Linux FUA/metadata requests; packed commands and other flags are refused. The main request must still pass the original root/data write bounds. A standalone CMD23 remains denied. User selection accepts only a byte-for-byte unchanged PARTITION_CONFIG with user access already selected; boot-enable/ack/reserved bits cannot change. All boot/RPMB selection, erase/trim/sanitize and protected data writes remain denied. MMC_CAP2_BOOTPART_NOACC suppresses boot-area enumeration. Production eMMC uses the ordinary serialized request path instead of HSQ; the working development/removable SD path is retained. The stock MT8135-compatible host already implements bounded AutoCMD23 in msdc_cmd_prepare_raw_cmd.

This corrects unsupported request/recovery cases and avoids forbidden boot-area probing. It does not prove which command the owner's truncated log rejected or that its rejection alone caused the absent partition nodes. Short Y2GUARD lines now retain opcode and argument on the display if a failure persists. No fallback invented partition table, offset mount or internal formatting is introduced.

## Cable-present USB startup

The old driver latched -ENODEV permanently when the initial CHRDET was asserted; its wake predicate also required the unplugged PHY6a=04 state. A historically observed connected-start PHY6a=BE is a saved-current force state. Replugging cannot restart a worker that was never scheduled.

Production's explicit DT property selects the MT6582 digital PHY recovery prefix. The retained stock ELF's usb_phy_recover at c04d98ac, byte operations c04d98d8 through c04d9a18, agrees with donorSource/drivers/phy/mediatek/phy-mtk-u2-mt6582.c: clear BIST, UART enable/force, force_suspendm, D+/D- pulldowns, XCVRSEL, TERMSEL, DATAIN and their force controls; disable BC1.1 switch; enable VBUS comparator; settle 800 us. This is followed by the existing checked peripheral session path. The ELF is the retained Y2Player/reverse/ghidra/exports/y2-kernel-with-kallsyms.elf; its symbols differ from the separately retained FM addresses in older M2 docs. The older addresses must not be applied to this export. No full ROM audit repeated.

Recovery requires the existing exact power/clock/SoC identity checks, disconnected MAC, B-device mode, zero DMA controls and only reviewed digital modes. Every masked byte write is read back. Oscillator/trim bytes 00/05/15 and other controls are checked for preservation; no calibration, PLL, supply or host VBUS write is added. An active inherited controller or unknown mode remains a visible refusal. The development profile retains its earlier one-bit wake sequence. Both cable present and absent at Linux startup are handled by the production worker; actual enumeration and reconnect are still physical acceptance items.

## Rescue and package

Production console loglevel 3 prevents expected empty-slot warnings from burying status; full kernel logs remain buffered. Rescue prints a compact error, cached USB status, internal partition geometry and shortened guard log directly to tty0. It remains running without reboot, SD fallback or formatting. The Buildroot image contains the matching Storage03 module/version; Y2DATA remains schema 1 with the same owner public key and no private credentials. Existing Y2DATA is compatible and can be preserved using the two-row profile. A fresh data template is supplied for explicit reinitialization only. All stock partition boundaries and future OTA/install contracts remain layout version 1.

Tests exercise real extracted request-guard code with Linux's actual READ/WRITE flag values, bounded reads/writes, protected overlaps, malformed CMD23 and unchanged-versus-mutated partition selection. PHY tests cover both cable states, passive/saved-current states, active/unknown state refusal, each failed read and write readback mismatch. Fixtures are not hardware proof. Complete image/package validation follows the build; no claim of power-entry or no-SD success is made.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
