---
title: "Production Storage / Installation v1 partition audit - Innioasis Updater"
description: "Production Storage / Installation v1 partition audit <!-- knowledge-base-scope: historical-design-/-runbook -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-architecture-production-storage-v1.html"
---

# Production Storage / Installation v1 partition audit - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Production Storage / Installation v1 partition audit

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Production Storage / Installation v1 partition audit > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Current correction: [stock Y2 eMMC address compatibility](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fstorage06-addressing-correction.md). Storage05's physical boot failed, but the corrected owner readback at21:10:43 CEST proves intact MBR/EBRs and exact flashed ext4 identity prefixes. The actual stock FM kernel adds23552 native user sectors and exposes15203328 sectors; the port omitted that mapping. Stock geometry/classification below remains unchanged. Upstream Linux6.18 parses these tables without a compatibility parser. [Storage06 ACM](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-13-storage06-owner%2FREADME.md) now confirms internal ext4 read-write root/data and Buildroot. SSH now authenticates with the existing owner key after the manual data initialization. [Accepted deployment](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-production-v1-r6-deployment.md). Deliberate scratch-write/stress acceptance remains outside this read-only check. BOOTIMG now owns loadable modules; rootfs/data and module ownership follow the [update contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fupdate-model.md). No physical success is inferred from builds.

Current correction: the first manual attempt completed BOOTIMG transfer but failed3154 on ANDROID. Selected DA[5] rejects sparse FILL. Storage02 uses raw ext4 transport. DA physical user capacity is7818182656bytes (15269888sectors); the historical Android exported disk remains7784103936bytes (15203328sectors). The difference is outside layoutv1 allocation, never reclaimed. See the [retained failure proof](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-13-storage-flash-failure%2FREADME.md). Partition boundaries and classification below remain unchanged.

2026-09-13, baseline `1583360`. All 21 stock scatter entries reviewed before implementation. Sources: [reconciled physical Android map](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/partition-map.tsv), [map interpretation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fpartition-map.md), [LK/boot contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fboot-chain.md), [recovery material](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/handoff-artifacts.tsv), [native MSDC identity](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-baseline-hardware-result.md), [donor/address research](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md), and local owner-proven FM scatter. No source or ROM-wide rehash was repeated. Only the scatter, overwritten-partition stock sources and table bytes are checked for this package. Current Linux disables eMMC; initial SSH timed out; owner then connected Y2 and read-only SSH succeeded. Native CID/CSD evidence and stock runtime metadata remain the latest available evidence, not live native filesystem proof. 48 kHz remains unqualified; M3 is not closed.

All normal starts below are stock logical disk bytes, matching the scatter's `physical_start_addr` field. Native EMMC_USER commands add0xb80000 (23552 sectors). Legacy global DA coordinates instead add0x1400000. The full JSON preserves the original scatter fields; current packages also carry explicit `storage_addressing` and corrected readback coordinates. PRELOADER (EMMC_BOOT_1) and BMTPOOL (sentinel) are separate: the vendor20MiB PRELOADER span is not a hardware boot-region extent (each boot region is4MiB).````````````````````````````````````````````````````````````````````````````````````

| Stock entry | Classification | Stock logical/scatter start | Stock span | Reason |
| --- | --- | --- | --- | --- |
| PRELOADER | KEEP | 0x0 | 0x1400000 | Boot ROM handoff; special hardware region span unresolved |
| MBR | KEEP | 0x0 | 0x80000 | Stock partition table |
| EBR1 | KEEP | 0x80000 | 0x80000 | Stock extended partition table |
| PRO_INFO | KEEP | 0x100000 | 0x300000 | Device/product identity; exact contents private/unknown |
| NVRAM | KEEP | 0x400000 | 0x500000 | Device-specific calibration and identity |
| PROTECT_F | KEEP | 0x900000 | 0xa00000 | Protected device data |
| PROTECT_S | KEEP | 0x1300000 | 0xa00000 | Protected device data |
| SECCFG | KEEP | 0x1d00000 | 0x20000 | Security configuration |
| UBOOT | KEEP | 0x1d20000 | 0x60000 | Stock LK bootloader |
| BOOTIMG | REUSE | 0x1d80000 | 0x1000000 | Linux kernel + DT + rescue |
| RECOVERY | KEEP | 0x2d80000 | 0x1000000 | Independent stock recovery route |
| SEC_RO | KEEP | 0x3d80000 | 0x600000 | Security/radio configuration |
| MISC | KEEP | 0x4380000 | 0x80000 | Boot/recovery control state |
| LOGO | KEEP | 0x4400000 | 0x300000 | LK display resource |
| EBR2 | KEEP | 0x4700000 | 0x80000 | Stock extended partition table |
| EXPDB | LEGACY | 0x4780000 | 0xa00000 | Legacy crash records; no reclamation without dependency review |
| ANDROID | REUSE | 0x5180000 | 0x33400000 | Y2ROOT ext4; stock /system |
| CACHE | LEGACY | 0x38580000 | 0x7e00000 | Unused Android cache; potential later staging, left untouched |
| USRDATA | REUSE | 0x40380000 | 0x32000000 | Y2DATA ext4; stock /data, destructive first initialization |
| FAT | LEGACY | 0x72380000 | 0x0 | Legacy internal shared/media storage; may contain user files, leave untouched |
| BMTPOOL | UNKNOWN | 0xffff00a8 | 0x1500000 | Vendor sentinel/unaligned special region: DO NOT TOUCH |

FAT's zero scatter length is dynamic: stock runtime resolves 0x15dc00000 bytes from 0x72380000, ending at 0x1cff80000. The historical Android exported bound is 0x1cff80000; DIAG01 confirms native physical capacity 0x1d2000000 (15269888 sectors). BMTPOOL has no approved operational range. EBR1's vendor allocation is 512 KiB, but Linux's stock p1 view is only 1024 bytes; preserve both facts.

## Reuse decision and dependencies

| Component | Stock name / current purpose | Stock logical / global linear start | Partition bytes | Linux stock view | SPFT |
| --- | --- | --- | --- | --- | --- |
| BOOTIMG | BOOTIMG, current M3 Linux boot | 0x1d80000 / 0x3180000 | 16777216 | Whole user disk range; no stock node | Independent NORMAL_ROM row |
| Y2ROOT | ANDROID, stock ext4 /system | 0x5180000 / 0x6580000 | 859832320 (820 MiB) | p5, start 166912 sectors, length 1679360 sectors | Independent YAFFS_IMG row; Storage02 raw ext4 transport |
| Y2DATA | USRDATA, stock ext4 /data | 0x40380000 / 0x41780000 | 838860800 (800 MiB) | p7, start 2104320 sectors, length 1638400 sectors | Independent YAFFS_IMG row; Storage02 raw ext4 transport |

LK reads BOOTIMG's legacy Android/MediaTek envelopes and transfers its ramdisk; it does not need Android /system or /data to run Linux. Preloader loads stock LK and retains the stock partition contract. No table, LK, preloader, recovery or security mutation is required. Stock recovery still expects Android filesystems: never use its wipe/update menus on Y2Linux. Restoring Android requires the verified FM boot/system/userdata images (factory state, not original personal Android data). Original installed Android data is not backed up; take a private USRDATA readback before first install if its personal state must be recoverable. Preserve FAT/media.

Native Linux must check host11230000, nonremovable MMC type, disk capacity and partition start/size before accepting LABEL=Y2ROOT/Y2DATA. Labels alone are not write authorization. No fixed mmcblk number or vendor /emmc alias is assumed. Both native filesystem mounts and owner-key SSH are now **physically confirmed on Storage06**. Broader write/power-fail qualification remains. Resolver failure leaves ACM rescue active.

CACHE (126 MiB) cannot hold the current 512 MiB root image. FAT is large but dynamic and may hold user media; it is unnecessary for v1. ANDROID is sufficient and preserves the stock tables. USRDATA provides independent persistent storage now. A/B BOOTIMG is not cheaply available without taking RECOVERY or changing LK's selection contract. Prefer staged single-slot updates from rescue; reserve no new partitions. Y2DATA can stage compact current system/app payloads; future updater must check free space and expanded size, and permit host-assisted recovery if a larger image cannot be staged. No promise of automatic rollback after torn BOOTIMG.

## Native write policy review

Production MSDC remains at legacy one-bit/13MHz with inherited LK pinmux and rails. The v6.18 MMC core needs EXT_CSD WRITE_BYTE using command-set1 (see locked `include/linux/mmc/mmc.h` and `drivers/mmc/core/mmc_ops.c`), including volatile ERASE_GROUP_DEF initialization that the historical identity-only kernel rejected. Storage03 permits explicitly reviewed volatile EXT_CSD controls and read/identity commands, validated bounded CMD23 companions and idempotent unchanged user-area selection. It refuses boot-configuration changes, other hardware partition selection, erase/trim/sanitize, RPMB/vendor operations and firmware writes. Only sector-addressed cards of the observed capacity in EMMC_USER may issue writes; the complete request must fit ANDROID or USRDATA. Boot-area enumeration is disabled and production uses serialized requests. See the [correction rationale](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fstorage03-corrections.md). All other stock partitions remain outside the write allowlist, including BOOTIMG; future rescue OTA must deliberately extend the guard for that component. This is accident containment, not a security boundary against a replaceable kernel.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
