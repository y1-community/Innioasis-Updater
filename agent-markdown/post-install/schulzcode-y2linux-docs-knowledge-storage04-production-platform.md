---
title: "Storage04: one production platform - Innioasis Updater"
description: "Storage04: one production platform <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-storage04-production-platform.html"
---

# Storage04: one production platform - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Storage04: one production platform

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Storage04: one production platform > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Storage03 was manually flashed but failed internal-root discovery and USB startup. Its latest owner photograph shows rescue alive, no partition rows and USB recovery -19 before any write. Storage04 is its uniquely versioned successor, not another diagnostic firmware. The same platform serves normal, rescue and diagnostic userspace. Physical acceptance is still required; no assistant flashed hardware.

## Evidence and cause boundaries

Executing the locked Linux 6.18 `block/partitions/msdos.c` against the retained factory MBR/EBR1/EBR2 exposes p5=166912/1679360 and p7=2104320/1638400 sectors. The sentinel extended lengths do not require a compatibility parser. Primary partitions also parse normally; the oversized legacy FAT is clipped by the block core. The fixture test also rejects missing signatures and invalid boot flags. No physical MBR/EBR readback from this failed boot exists. Factory parsing success does not prove that the current card returns those bytes. Do not invent a new partition map or claim this identifies the device's precise failure.

Storage03's SBC parameter was already an invalid-companion predicate, despite its confusing name. Its code still depended on `host->card`, which Linux assigns only at the end of `mmc_init_card()`, after EXT_CSD reading and possible user-area reselection. It could reject that ordinary initialization step. The new adapter tracks OCR addressing and EXT_CSD hardware region directly from successful controller responses. A partition switch becomes trusted only after CMD13 confirms completion without switch/status errors. Reset invalidates that context. Whole requests validate direction, sector range, SBC flags/count and stop command; standard reads, writes, cache flush, power notification and sleep commands share one path. These are source-backed corrections, not proof that this exact step caused the photographed failure. Table reads now log only sector/count/signature, with DMA ownership synchronized; no identity/calibration contents are logged.

USB previously lived in the diagnostic board endpoint and accepted only narrow loader register snapshots. The physical result proves that preflight refused; the omitted register values prevent identifying its exact failed predicate. The production platform driver now normalizes its owned digital PHY controls using the retained MT6582 `usb_phy_recover` sequence, masks MAC interrupts and disconnects inherited device SOFTCONN before reinitialization. Inherited forced peripheral inputs and dormant DMA configuration are no longer refusal reasons. Active DMA or host mode still refuses takeover. Chip, mapped resources, rail and clock validity are checked; analog trims, PLLs, chargers and VBUS supplies are not rewritten. The fixed peripheral board forces device inputs through the same session code on first attachment and reconnect. Cable-present and late attachment use the same driver, with read-only sysfs `status` and cached legacy ABI.

Sources: locked Linux `drivers/mmc/{host/mtk-sd.c,core/mmc.c,core/block.c}` and `block/partitions/{msdos.c,core.c}`; retained factory metadata and scatter in the [partition audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fproduction-storage-v1.md); MT6582 donor `donorSource/drivers/phy/mediatek/phy-mtk-u2-mt6582.c` and retained stock `usb_phy_recover` disassembly referenced by [Storage03's source review](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fstorage03-corrections.md). Existing GPL notices remain.

## Runtime audit

| Previous mechanism | Classification | Active treatment |
| --- | --- | --- |
| CONFIG_Y2_BOOT_DIAGNOSTIC platform selection | Hardware support under a misleading development name | CONFIG_Y2_PLATFORM; same selected drivers in every build |
| y2_read_only / y2_production MMC modes | Obsolete bring-up split | One internal MMC path, typed request protection |
| Read-only/production diagnostic DT identities | Obsolete mode selection | One innioasis-y2.dts; compatibility filenames include it |
| Shared clocks, pinctrl, PWRAP, display/audio/input support | Permanent hardware support, qualification still bounded | Retained; no repeat bring-up or sibling SoC substitution |
| Protected eMMC ranges and PMIC control ownership | Permanent safety policy | Retained and made operation/context aware |
| Diagnostic read initiating USB | Obsolete ownership | Platform probe initializes hardware; status reads observe it |
| Unplugged boot / exact saved-state USB predicate | Obsolete bring-up behavior | Owned digital state normalization and normal attachment polling |
| Observer loading the display module | Obsolete diagnostic dependency | Production platform startup loads it asynchronously on CPU1 |
| Cached status and kernel logs | Useful instrumentation | Read-only platform sysfs plus y2-status and optional observer |
| SD-root builder/resolver | Historical recovery implementation | Old builder entrypoint forwards to production; history remains in Git |
| Early watchdog stop, inherited PLL rates/rails, one-bit MMC | Partial platform support | Same implementation in all builds; full power/watchdog/PM and throughput remain qualification work |

No new charger/power-entry behavior is implemented. USB presence does not prove charging; battery voltage and the cause of intermittent off-state response remain unknown. USB reconnect and SD hotplug retain physical qualification gaps.

## Storage and component ownership

No partition changes. ANDROID/Y2ROOT is physical EMMC_USER 0x05180000, 0x33400000 bytes; USRDATA/Y2DATA is 0x40380000,0x32000000 bytes. Normal writes may reach only those two spans. Reads include stock metadata/protected user-area partitions. Hardware boot/RPMB access, persistent boot configuration, erase, sanitize, lock/write-protect, vendor commands and BOOTIMG writes are excluded. CMD23 supports ordinary reads/writes, reliable-write and metadata-tag flags; packed writes are not supported. Discard is not a supported operation; mounts omit discard. No table is rewritten and no fixed-offset loop-device fallback exists.

BOOTIMG owns the kernel, DT, rescue and its matching loadable DRM module. Rescue stages the module in /run/y2/modules and binds that RAM tree at /lib/modules in Buildroot. Kernel-only updates therefore no longer require replacing a duplicated module in Y2ROOT. The permanent platform contract is y2-platform-v1; future compatibility checks still reject kernels/userspace that violate its ABI. This candidate needs new BOOTIMG and Y2ROOT for startup/status tools and the module ownership transition. Y2DATA schema and the existing template bytes are unchanged; select the preserve-data scatter. Normal updates never initialize USRDATA.

Rescue discovers both internal filesystems using host identity, geometry and ext4 label/UUID; validates markers; checks and mounts them; then switches root. It never depends on SD. Failure is visible, retains the process and ACM logging where USB is functioning, and does not format or reboot-loop. `y2.rescue=1` is an explicit boot-command-line rescue entry for future recovery integration. OTA, signatures, remote downloads and Y2PlayerNative are not implemented.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
