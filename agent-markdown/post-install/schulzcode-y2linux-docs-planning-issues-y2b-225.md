---
title: "Y2B-225 — Build and validate zImage with appended DTB - Innioasis Updater"
description: "Y2B-225 — Build and validate zImage with appended DTB <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2b-225.html"
---

# Y2B-225 — Build and validate zImage with appended DTB - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2B-225 — Build and validate zImage with appended DTB

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2B-225 — Build and validate zImage with appended DTB > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Depends on Y2B-220 (#12), D08/D09. Offline only.

Build v6.18 plus the single reviewed Kconfig visibility patch using the locked tools/config. Build the final DTS with actual initramfs length. Append exactly the DTB padded to 8 bytes at zImage _edata.

Acceptance:
  -  Real kernel and compressed ELF symbols, Image bytes, gzip/inflated-size word and zImage agree.
  -  Exact D08 relocation/stack/BSS/malloc and DTB survival checks pass for actual symbols; missing evidence fails closed.
  -  Independent DT decoding verifies exact memory/reservations/initrd, CPU0 and reviewed hardware/bootargs; config and ELF entry architecture match.
  -  Emit actual physical interval manifest and hashes. No BOOTIMG/device action in this checkpoint.

Validation: actual Image 2,543,296 bytes; zImage 1,076,072; DTB 1,835 (1,840 padded); initramfs 1,582. Real ELF/DT/gzip cross-checks and every D08 interval pass. Physical-base defaults are explicitly fixed and checked; ELF vector load addresses are used. See out/first/layout.json (ignored build product); durable final report follows the packaging/reproducibility checkpoint.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
