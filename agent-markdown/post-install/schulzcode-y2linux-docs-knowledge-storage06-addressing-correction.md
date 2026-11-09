---
title: "Production stock eMMC address compatibility - Innioasis Updater"
description: "Production stock eMMC address compatibility <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-storage06-addressing-correction.html"
---

# Production stock eMMC address compatibility - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Production stock eMMC address compatibility

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Production stock eMMC address compatibility > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-13, entry `d7ee4f2`; physical Storage05 BOOTIMG `2af64e0fe0831a038ea681e82b93209bb21360995772a54699b7f0ef6be22efa`. The candidate built from bea30cd and the owner flashed it. [ACM confirms internal boot](../hardware-evidence/2026-09-13-storage06-owner/README.md). The remaining owner-key mismatch was corrected through Y2DATA initialization, with no new kernel. [Authenticated SSH acceptance](https://github.com/schulzcode/y2linux/blob/HEAD/docs/hardware-evidence/2026-09-13-storage06-owner/ssh-result.json) now confirms the complete BOOTIMG hash and all three stock table hashes through normal Linux block reads. The integrated correction is deployed.

## Evidence and root cause

The owner's corrected SPFT readback at21:10:43 CEST matches all six expected samples: Storage05 BOOTIMG prefix, complete stock MBR/EBR1/EBR2, and the flashed Y2ROOT/Y2DATA 4-KiB prefixes. All tables have55aa and unchanged geometry. The filesystem samples contain the expected ext4 magic, labels and UUIDs. This proves location/header identity, not whole on-device filesystem integrity. [Machine-readable analysis](https://github.com/schulzcode/y2linux/blob/HEAD/docs/hardware-evidence/2026-09-13-storage05-owner/readback-corrected-analysis.json) and [DA command/capacity excerpt](https://github.com/schulzcode/y2linux/blob/HEAD/docs/hardware-evidence/2026-09-13-storage05-owner/readback-corrected-log-excerpt.txt). The earlier21:00 batch used the wrong DA coordinates and is retained separately.

The actual stock FM kernel contains a nonzero `msdc_get_offset`, unlike the public donor source reviewed for Storage05. Its own decompressed binary SHA256 is `7287acf1b397d243c927dde5c6ef9d5d871c9c158207cdd98e0e820923f4c197`. Recovered symbols identify `msdc_get_offset` at0xc04e66ec, `msdc_get_other_capacity` at0xc04e6668, `msdc_get_reserve` at0xc04eac1c and `msdc_command_start.isra.8` at0xc04efd6c. Disassembly shows:
  - Offset = `(20 MiB - other hardware region bytes) >> 9`.
  - Other regions = both boot partitions, RPMB and four GP partitions from EXT_CSD.
  - CMD17/18/24/25 user-area arguments receive this offset before SDC_ARG.

Non-user access bypasses it. The zero-LBA path calculates the cached offset.
  - `mmc_blk_probe` at0xc034a0fc calls `msdc_get_info` for the reserve,

then subtracts it at0xc034a108 before allocating the disk. The reserve includes this offset plus `(BMTPOOL sentinel & 0xffff) << 8`:0xa800 sectors.

[Selected own-binary instructions](https://github.com/schulzcode/y2linux/blob/HEAD/docs/hardware-evidence/2026-09-13-storage05-owner/stock-fm-addressing-excerpt.txt). Full disassembly, acquired samples and SPFT logs stay in private evidence. This supersedes Storage05's assertion that stock only reduces the tail and that Linux should use raw SEC_COUNT coordinates. No physical corruption is indicated.

## Three coordinate spaces

| Quantity | Value |
| --- | --- |
| Native EMMC_USER SEC_COUNT | 15269888 sectors /0x1d2000000 bytes |
| DA concatenated non-user areas | boot1 0x400000 + boot2 0x400000 + RPMB 0x80000; GP1–4 zero |
| Global legacy DA MBR address | 0x1400000 bytes |
| Native user MBR address | 0x1400000 −0x880000 =0xb80000 bytes /23552 sectors |
| Stock logical disk sector0 | MBR; logical sector +23552 = native wire argument |
| Exposed stock disk size | 15203328 sectors /0x1cff80000 bytes |
| Excluded native tail | 43008 sectors /21 MiB |

Scatter `physical_start_addr` is the old stock logical disk coordinate for these partitions; it is not a direct native EMMC_USER command address. Scatter `linear_start_addr` is the legacy global DA coordinate used by the retained SPFT session. The difference0x1400000 between those scatter fields must not itself be added to Linux wire addresses. Existing scatter entries remain unchanged.

| Partition | Logical start | Length sectors | Native user start | Legacy DA start bytes |
| --- | --- | --- | --- | --- |
| ANDROID /Y2ROOT | 166912 | 1679360 | 190464 | 0x06580000 |
| USRDATA /Y2DATA | 2104320 | 1638400 | 2127872 | 0x41780000 |

## Permanent production correction

One canonical Y2 eMMC host translates CMD17/18/24/25 once at register emission, after validating the original logical request. It leaves `cmd->arg` untouched for retries, and CMD6/CMD8/CMD13/CMD23/CMD12 retain their standard arguments. The real EXT_CSD remains unmodified; raw capacity and boot/RPMB/GP geometry must match the observed layout before user data I/O is admitted. The Y2 main block disk alone exposes the stock15203328 sectors. Removable SD and other MMC hosts retain upstream addressing and capacity.

Reads cover the stock logical disk. Writes remain bounded to the exact original ANDROID/USRDATA spans before translation. The hidden native prefix/tail, tables, BOOTIMG/LK, NVRAM, PRO_INFO, PROTECT_F/S, SEC_RO, SECCFG, BMTPOOL and every other non-allowlisted span remain unavailable to ordinary writes. Boot/GP/RPMB region selection, erase, sanitize, write-protect and vendor commands remain refused. Standard bounded block writes, software CMD23, flush and status work normally.

Linux6.18's existing MSDOS parser accepts the actual stock tables. No parser, table, filesystem, DT, memory or clock change is needed. Rescue resolves exact logical geometry plus ext4 label/UUID and switches to existing internal Buildroot; SD remains optional user media. This addresses the internal-only regression: the working external SD never needed the stock eMMC address translation.

## Validation boundary

Tests must exercise the actual host request/command functions with the MBR at native sector23552, the scoped block capacity quirk, unmodified EXT_CSD and unshifted companion commands, retries, bounds and protected regions. Existing stock parser, resolver, no-SD handover, ext4 identity/integrity and BOOTIMG bounds/manifest checks apply. No physical acceptance is inferred from these. Entry validation passes25 targeted host tests: actual request/MMIO functions, strict EXT_CSD geometry, actual main-disk allocation, every native sector against the write allowlist, stock parser, resolver, companions/retries/faults, readback mode metadata and rejected contract changes. Full ARM/package checks follow the single build.

The storage deliverable was one BOOTIMG-only update using unchanged root/data images; the owner's flash and internal boot succeeded. The separately authorized SSH correction then changed only the initial Y2DATA public key. Both steps use the same production platform and are now physically observed; see the [completed deployment](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-production-v1-r6-deployment.md).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
