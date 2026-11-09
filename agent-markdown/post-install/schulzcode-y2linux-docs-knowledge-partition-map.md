---
title: "Partition map and acquisition boundary - Innioasis Updater"
description: "Partition map and acquisition boundary <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-partition-map.html"
---

# Partition map and acquisition boundary - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Partition map and acquisition boundary

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Partition map and acquisition boundary > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-13 clarification: the actual FM kernel implements a23552-sector translation from this stock logical disk to native EMMC_USER. Corrected owner readback confirms all tables and flashed ext4 identity prefixes. [Evidence and three address spaces](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fstorage06-addressing-correction.md). The original metadata and historical acquisition boundary below remain history.

Date: 2026-09-08. Task: [Y2E-110](https://github.com/SchulzCode/Y2Linux/issues/3). Capture: `20260908-partitions`. Status: metadata reconciliation complete, raw acquisition NOT AUTHORIZED.

The [full 21-entry table](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/partition-map.tsv) retains scatter linear and physical byte addresses, runtime vendor values, Linux node mapping, 512-byte sector counts and unresolved cases. Source scatter SHA-256: `e5fe03e9f3219cc9b5ead27892f2ddb722acc16adce3306d27feb87893cd977e`. `/proc/dumchar_info`, `/proc/emmc`, `/proc/partitions`, mount records, aliases and explicit sysfs block metadata were read without opening any block device. Sixty bounded read-only commands captured 13 eMMC/SD nodes. Missing `start` files on whole disks/hardware boot regions are expected observations, not zero-valued partition offsets.

## Confirmed metadata relationships

Internal `mmcblk0` is 15,203,328 sectors = 7,784,103,936 bytes. Each eMMC boot hardware region reports 8,192 sectors = 4,194,304 bytes. The removable card is a separate `mmcblk1`; never infer its identity from an internal-storage partition number.

All eight `/proc/emmc` partition starts/counts match the corresponding sysfs values. PROTECT_F, PROTECT_S, SEC_RO, ANDROID, CACHE, USRDATA and runtime FAT lengths also agree with dumchar. Example: PROTECT_F starts at `0x4800` sectors = 18,432 × 512 = 9,437,184 bytes = `0x900000`; its `0x5000` sectors = 10 MiB matches vendor metadata. Normal fixed EMMC_USER scatter ranges from MBR through USRDATA have no overlaps and are within reported user capacity.````````````````

| Object | Scatter linear bytes | Scatter physical / runtime dumchar bytes | Length | Runtime mapping |
| --- | --- | --- | --- | --- |
| BOOTIMG | 0x3180000 | 0x1d80000 (30,932,992) | 0x1000000 (16,777,216) | parent /dev/block/mmcblk0, no dedicated partition node identified |
| RECOVERY | 0x4180000 | 0x2d80000 (47,710,208) | 0x1000000 (16,777,216) | parent /dev/block/mmcblk0, no dedicated partition node identified |

Scatter and runtime dumchar independently agree on these two ranges. They are metadata findings, not an executable readback contract: parent-device permissions and exact acquisition semantics still require resolution. File sizes of the packaged boot/recovery images are much smaller than their partition spans; packaged images do not cover all partition bytes.

The normal scatter linear address adds `0x1400000` to the stock logical disk address (named `physical_start_addr` in the scatter). A native EMMC_USER command adds `0xb80000` to that logical address; the retained legacy global DA uses the linear address. Hardware boot regions remain separate. Never interchange these coordinates without identifying the tool's actual mode.

## Special cases that prevent a generic recipe
  - PRELOADER: scatter/dumchar report `0x1400000` (20 MiB), whereas each eMMC boot region reports 4 MiB; dumchar maps it through `/dev/misc-sd`. The vendor span is not proven to be an actual region length. Do not transfer it into readback/flash coordinates.
  - EBR1: vendor allocation is 512 KiB, while exposed `mmcblk0p1` contains two sectors (1 KiB). Start agrees. Lengths describe different scopes.
  - FAT: scatter length is zero; dumchar/sysfs resolve it to `0x15dc00000`. This is dynamic allocation, not an empty partition.
  - BMTPOOL: scatter physical `0xffff00a8` differs from runtime `0xfebf00a8`, and the value is not sector aligned. Semantics remain UNKNOWN; no range is approved.
  - The packaged MBR/EBRs all have `55aa` signatures, but include `0xffffffff` length sentinels and vendor-specific extended layout. These are not generic partition-table repair inputs. Offline slot decoding is preserved in the private analysis record.

## Access, mutable data and recovery

`mmcblk0` and boot0 are root:system 0660, boot1 and partition nodes are root:root 0600. The current shell is uid 2000 and is not in the system group. Permission metadata does not demonstrate readable backup access; no open/read was attempted. `/emmc@...` aliases map the ordinary filesystems but do not provide a discovered boot/recovery shortcut.

NVRAM, PRO_INFO, PROTECT_F, PROTECT_S, SECCFG and MISC have no supplied package images. Their exact personalized contents and restore requirements remain UNKNOWN. Protect filesystems are currently writable/mounted, so a later backup also needs a consistency strategy. Do not replace personalized data with factory defaults. Sparse system/userdata package file length is not expanded filesystem size or a whole-partition backup length.

## Review decision

The map is adequate to identify the exact local stock boot input and constrain offline Y2E-115 analysis. It is not adequate to authorize a generic whole-device acquisition tool or any write. Special-region interpretation, access method, personalized data consistency and independent backup storage remain recovery blockers.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
