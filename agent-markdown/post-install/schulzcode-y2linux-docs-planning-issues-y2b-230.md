---
title: "Y2B-230 — Package the legacy MTK BOOTIMG offline - Innioasis Updater"
description: "Y2B-230 — Package the legacy MTK BOOTIMG offline <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2b-230.html"
---

# Y2B-230 — Package the legacy MTK BOOTIMG offline - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2B-230 — Package the legacy MTK BOOTIMG offline

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2B-230 — Package the legacy MTK BOOTIMG offline > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Depends on Y2B-225 (#13). Preserve stock preloader/LK and partition layout; no flashing commands.

Package only a validated zImage+DTB and external diagnostic initramfs. Use the FM legacy Android header with 2048-byte pages, declared 0x100... addresses, 512-byte MTK KERNEL/ROOTFS wrappers and deterministic metadata. Runtime addresses remain the independently validated LK/D08 contract.

Acceptance:
  -  Strict independent parser checks every header field, wrapper magic/name/length/padding, Android SHA-1 ID and actual payload bytes.
  -  Zero-fill file padding through LK's complete read (including its extra two pages); final file fits the 16 MiB BOOTIMG partition.
  -  Require successful actual artifact validation before writing; reject altered/missing evidence and do not change limits.
  -  Emit packaged size/hash and roundtrip checks; no signed-image/authentication claim.

Validation: BOOTIMG 1,089,536 bytes, SHA-256 8e2fdae1f90c7589073676f69c0418af25cb0671a288ad838d83077f04b6d2f5. Seven tests pass, including 25 altered/truncated/extended package cases. Stock header SHA-1 semantics independently reproduced from the FM bytes. No authentication or launch claim.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
