---
title: "Y2Linux 1.0 Beta 7.10 (Baseline 73) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 7.10 Baseline 73 Status: PUBLISHED as GitHub release baseline-73 2026-10-17. Release 1.0.0-beta.7.10 , Reborn 1.0.0-beta.7.10 , kernel 6.18.56-y2linux-1."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-7.10.html"
---

# Y2Linux 1.0 Beta 7.10 (Baseline 73) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 7.10 (Baseline 73)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 7.10 (Baseline 73)

Status: PUBLISHED as GitHub release `baseline-73` (2026-10-17). Release `1.0.0-beta.7.10`, Reborn `1.0.0-beta.7.10`, kernel `6.18.56-y2linux-1.0.0-beta.7.10`, update sequence 6300, Linux `72a565d`, Reborn `511dbf0`, git tag `baseline-73` in both repositories. Built with `tools/production/release.py` in 120 s on top of Baseline 72: container suite 766 OK, all seal checks PASS, no MediaTek firmware in any image; the rebuilt kernel (musb fix) and MTP responder (MoveObject, CopyObject) were checked in the build and the root image. Milestone audit BETA-7.10 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | c937fe6a2168981c6c81bf3a29a2d0477e44b0f8b845dd0786513be2c04f1b0b |
| Y2ROOT | d67afcb10318eb73344e2383982466bad4ebba79c55f03b3833ff6aa8cf18f78 |
| RECOVERY | be89254d86ac93def59fd4f8ab934d8a5d6b820463ccb9b6add5201cb4bf6382 |
| Y2DATA (no SSH key) | 04586d68d656673965a3f6b3b9e827191d5c258f8da9c7ddd6a406bec4650a0a |

## Device result of Beta 7.9 (owner's player)

The automatic Internal Storage setup passed on real hardware: on the first restart after the confirmed update the stock FAT became Y2MEDIA (label, UUID, start/size, features, 358 336 inodes, 1 432 576 blocks identical to the 2026-10-10 original), 509 old files kept in Old Player Files hash-identical to the backup, the 3 leftovers dropped, setup ≈16 s at start, record and temporary copies removed; on the update's health boot it waited (`update_in_progress`). Deleting Old Player Files over MTP then hung the player: kernel oops (pstore) in `dma_cache_maint_page` from `musb_gadget_queue`, offset 0x10 / length 0 (evidence `20261017/usb-zlp-oops`).

## Since Beta 7.9````````````

| Part | Change |
| --- | --- |
| USB crash | uMTP ends every transfer that ends on a packet boundary with a zero-length packet; FunctionFS gave it kmalloc(0) = ZERO_SIZE_PTR and musb DMA-mapped that address (6.18 dma_map_phys → cache maintenance of a non-existent page). musb now never maps a zero-length request (it is sent by PIO, as before). Any packet-aligned copy, listing or delete could trigger it. (Linux da0917d) |
| Move and copy on the player | MoveObject and CopyObject, announced in DeviceInfo (Windows Explorer and libmtp hosts use them). Same storage: rename, handle kept. Between Internal Storage and the SD card and for copies: each file copied like an upload (space reserve, hidden temporary name, fsync, never replacing a name, time kept), the source of a move removed only after the complete copy. Refused: into itself, over a name, into read-only storage, moving out of Old Storage; copying out of Old Storage works. (Linux 4c0a54d) |
| Host tool | tools/usb/mtp-file-ops.c (libmtp): packet-boundary sizes 0 B–40 MB read back, 600 files, rename, move, copy, folder to the SD card and back, single and folder deletes, liveness after each step. |

Host evidence: 793 Y2Linux host tests (real responder protocol tests for MoveObject/CopyObject, mutation-checked), 514 Reborn tests. Device run of `mtp-file-ops` owed after the OTA install.

## Known gaps

A very large CopyObject or a move of a large folder between storages runs inside one MTP operation; a host may time out while the player keeps copying (the result is complete or nothing). Windows Explorer has not been run against the player in this session.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
