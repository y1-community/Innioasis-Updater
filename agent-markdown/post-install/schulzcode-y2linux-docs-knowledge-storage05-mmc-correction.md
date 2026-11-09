---
title: "Storage05 integrated production MMC correction - Innioasis Updater"
description: "Storage05 integrated production MMC correction <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-storage05-mmc-correction.html"
---

# Storage05 integrated production MMC correction - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Storage05 integrated production MMC correction

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Storage05 integrated production MMC correction > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-13 update: Superseded addressing conclusion: the21:10:43 corrected physical readback matches every expected table/image prefix. The actual FM binary has a23552-sector offset absent from the public donor. [Storage06 evidence and correction](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fstorage06-addressing-correction.md) supersedes zero-offset claims below; Storage05 still fails internal boot.

## Latest physical result: still in rescue

The owner's subsequent [SPFT Readback](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-13-storage05-owner%2FREADME.md%23latest-spft-readback-completed-in-a-different-address-mode&anchor=latest-spft-readback-completed-in-a-different-address-mode) completed all six files, but the assistant's physical-offset instructions did not match the tool's actual legacy global address mode. The supposed Y2ROOT prefix exactly matches stock SEC_RO; the BOOTIMG identity control fails. This does not establish intended MBR/EBR or ext4 contents. The [corrected readback coordinates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fstorage05-readback.md) use the same observed tool mode. No Linux address translation, table repair, image rewrite or additional firmware is justified by this acquisition mismatch.

The earlier [successful ACM capture](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-13-storage05-owner%2FREADME.md%23earlier-read-only-acm-capture-succeeds&anchor=earlier-read-only-acm-capture-succeeds) retains 2736 contiguous kernel records, including sector-addressed=1, capacity 15269888 and PART_CONFIG=0x48 (user-area access bits zero). The same CMD18 signature0000 and successful SBC/R1 remain; rescue fails at 40.853244 seconds. There is no eMMC guard rejection or reported transport error in that interval. This further constrains the cause without proving actual MBR bytes. LOG1 cannot read arbitrary sectors. The next concrete evidence step is the [13.5-KiB manual Readback batch](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fstorage05-readback.md); no new image or table repair is prepared. Additional vendor check.c/genhd.c inspection found no PMT replacement parser on the reviewed path; no compatibility override is justified.

The [owner's Storage05 photograph](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-13-storage05-owner%2FREADME.md) supersedes pending physical acceptance below. CMD18 sector 0 reports4096 bytes, signature0000, SBC8/00000900 and R1=00000900. Software SBC sequencing did not fix the physical boot blocker. Internal root/data remain undiscovered and Buildroot does not start. The reproduced source defects remain valid findings, but must not be presented as the established cause of that failed read.

The retained vendor MMC block code only reduces exported capacity at the end; its DOS parser still requires55aa at sector 0. Additional inspection found no vendor-generated replacement MBR in these paths. Sources: [vendor block.c](https://android.googlesource.com/kernel/mediatek/+/58a89abc8fc05796b12fd8829dac415c9e3f01e2/drivers/mmc/card/block.c), [vendor msdos.c](https://android.googlesource.com/kernel/mediatek/+/58a89abc8fc05796b12fd8829dac415c9e3f01e2/block/partitions/msdos.c). An independent read-only sector observation remains necessary to separate actual metadata failure from incorrect Linux read data. No additional firmware was built.

## Original correction scope

Entry: `37e4a3f` with the already-pending Storage04 ACM evidence and build-input preparation fixes. One production candidate is authorized. No new diagnostic firmware, physical write, table repair, alternate DT or SD boot dependency.

## Evidence and cause limits

The [owner's Storage04 ACM capture](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-13-storage04-live%2FREADME.md) proves Linux 6.18, four CPUs, 954380 KiB RAM, the expected 15269888-sector eMMC, and `partition read sector=0 bytes=4096 signature=0000`. There are no partitions or internal root/data mounts. EXT_CSD identification and the first block request complete without a logged internal transport/policy error. The later expected CMD8/CMD55 timeouts belong to the empty removable host, not eMMC. Current host inspection finds no ACM device; LOG1 only exports retained logs, not a remote shell/raw-read API. The supplied log remains the physical evidence for this pass.

The source review identifies real protocol/error-handling defects, **not a proven physical explanation of the zero signature**. There is no current independent 512-byte read or physical MBR/EBR readback. Do not report that AutoCMD23 is broken in silicon or that the MBR is erased. MT6582's vendor driver itself supports AutoCMD23. Explicit software SBC is a permanent conservative sequencing choice; the new candidate's physical boot is the acceptance boundary.

An additional definite blocker was reproduced with the actual Storage04 ARM BusyBox under QEMU: `set -i` exits with status 2 (`illegal option -i`). Production rescue invoked it immediately before switch_root. BusyBox accepts -i at shell startup only. That line would kill PID1 after otherwise successful internal mounts. The corrected handover uses a supported EXIT trap for shell exec failure; successful exec preserves PID1 and enters the normal switch_root applet. The trap restores moved filesystems and returns to rescue if exec itself fails. A failure inside an already-executing switch_root cannot return to the old shell; identity, executable and mount preflights remain essential.

## Working SD versus internal production path

| Concern | Last working SD AUDIO-02 | Storage04 and this correction |
| --- | --- | --- |
| Host setup | MSDC1/11240000, one bit/13 MHz, 26-MHz source, SD pinctrl | MSDC0/11230000, same upstream DMA transport/timing; inherited eMMC pins/rails; no new electrical settings |
| MMC policy | No internal filesystem path; internal host disabled | Complete requests allow reads in identified EMMC_USER and writes wholly inside ANDROID or USRDATA; this boundary remains |
| SBC/CMD23 | SD uses software SBC where supported, otherwise CMD12 | eMMC previously used hardware AutoCMD23 for ordinary requests and software for flag-bearing writes; now all Y2 eMMC SBC runs explicitly before data, preserving exact count/FUA/tag bits |
| Block address | SD core chooses byte/sector addressing | eMMC OCR/EXT_CSD prove sector addressing before I/O; wire arguments remain exactly Linux LBAs, including zero, 1024 and 145408; no scatter-linear offset is added |
| EXT_CSD/CMD6 | SD protocol has no EXT_CSD | Read before host->card registration; standard volatile controls and user-area reselection accepted; boot enable/ack bits preserved; failed selection invalidates context |
| LK state | Controller reset; inherited supplies | Same reset/legacy bus path; CMD0 invalidates address/region context, EXT_CSD establishes it, CMD13 confirms successful region switching; no loader/calibration rewrite |
| Partition discovery | Linux DOS partition parser on SD | Same Linux 6.18 parser; actual retained stock MBR/EBR1/EBR2 yield p5/p7 at the required geometry; no compatibility parser needed |
| Root resolver | Removable Y2ROOT | Production host/type/capacity/start/length/ext4 label/UUID validation of both internal filesystems; unchanged, no fallback offset/loop device |

Locked primary sources: Linux v6.18 [`mtk-sd.c`](https://github.com/torvalds/linux/blob/v6.18/drivers/mmc/host/mtk-sd.c), [`mmc.c`](https://github.com/torvalds/linux/blob/v6.18/drivers/mmc/core/mmc.c), [`block.c`](https://github.com/torvalds/linux/blob/v6.18/drivers/mmc/core/block.c), and [`msdos.c`](https://github.com/torvalds/linux/blob/v6.18/block/partitions/msdos.c). Retained MT6582 vendor [`sd.c`](https://android.googlesource.com/kernel/mediatek/+/58a89abc8fc05796b12fd8829dac415c9e3f01e2/drivers/misc/mediatek/mmc-host/mt6582/sd.c) implements zero address offset, opcode-based data type, software/automatic SBC, and normal block-count programming. Its local copy is in evidence-private/20260910-baseline. Existing copyright notices remain.

## Production changes

The production MSDC implementation sends a validated SBC as a real CMD23, checks its R1/transport result, and only then issues CMD18/CMD25. The count and reliable write/metadata tag flags are not stripped. CMD23 capability stays enabled; there is no single-sector-only policy or read-only eMMC mode. CMD12 remains available for open-ended transfers and normal core error recovery.

The controller data type now follows CMD18/CMD25 even when Linux requests one block, as it does for a one-sector reliable write. Previously that request was encoded as a single-block protocol despite its multiblock opcode. CMD17/CMD24 and EXT_CSD remain ordinary single-block commands. No address translation changes.

For Y2 eMMC, DMA CRC/timeout/descriptor/protection errors and failure to stop DMA cannot be reported as a successful byte count, including simultaneous completion and error interrupts. A rejected SBC or data R1 cannot start DMA. MMC core retains its own CMD6/CMD13 status handling, including optional-feature switch errors. Partition-switch context becomes pending before CMD6 is sent, and a transport failure invalidates it; a later plain ready status cannot bless that failed switch.

Only ANDROID [166912,1846272) and USRDATA [2104320,3742720) sectors are writable. BOOTIMG, PRELOADER/boot hardware areas, LK, NVRAM, calibration, PRO_INFO, PROTECT_F/S, SEC_RO, SECCFG, BMTPOOL, tables and every other range remain excluded. Boot/RPMB/GP hardware-region selection, boot configuration changes, erase, sanitize, write protection, lock and vendor commands remain refused. Standard cache flush and power notification remain supported. This is storage accident containment under the supplied kernel, not protection against replacing it.

## Images and handover

BOOTIMG contains the new production kernel and matching DRM module, the same hardware DT, and the production rescue with the corrected exec handover and updated version text. The builder reuses the hash-checked Storage04 userspace binaries, uses the same production config/DT/archive/artifact path, and never rebuilds either ext4 image. The module still travels in RAM to /lib/modules in Buildroot. Y2ROOT stays 2025.02.17-storage.4, Y2DATA stays schema 1, and y2-platform-v1 is unchanged.

The update manifest has one BOOTIMG payload and separately records the unchanged installed root/data identities and original source commit. Its sole scatter selects BOOTIMG; every other filename is NONE and every other row is unchecked. Fallback is the retained owner-observed Storage04 BOOTIMG (rescue/ACM, not a working internal root). Factory restoration is unchanged and is not rerun.

## Offline and physical acceptance

The transport harness executes actual production request, raw-command, command completion and data completion functions. It covers CMD23→CMD18 at sector zero, the factory 55aa fixture through an injected DMA response, unchanged wire LBAs, one-block reliable/tagged CMD25, CMD12, refused R1, concurrent ready/CRC, all DMA faults and stop timeouts, and protected writes rejected before DMA. Injected card/MMIO responses prove software behavior, not actual eMMC contents. The context tests cover initialization before card registration, failed/confirmed selection, DMA ownership and CMD0 invalidation. The actual upstream parser and production resolver validate stock geometry and reject malformed/shifted/SD clones.

Package acceptance also checks existing ext4 integrity/UUID/labels/markers, independent component versions, no-SD rescue→validated root/data→switch_root, module ABI, ARM userspace, kernel/DT/initramfs memory bounds, Android/MTK BOOTIMG envelopes/hash and exact stock scatter selection. Final test/build records belong to docs/build/evidence/y2linux-production-v1-r5.

After the single manual BOOTIMG-only flash, boot once without SD and observe whether both partitions appear and rescue logs `switching to Buildroot`. Expected normal services can then start; the existing missing matching SSH client key is unchanged. Internal boot/write success and physical protected-byte preservation are not claimed until hardware evidence establishes them.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
