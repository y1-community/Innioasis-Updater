---
title: "CONNECTIVITY-07: identify factory storage through mounted root/data - Innioasis Updater"
description: "CONNECTIVITY-07: identify factory storage through mounted root/data <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candid"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m5-connectivity07-corrections.html"
---

# CONNECTIVITY-07: identify factory storage through mounted root/data - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# CONNECTIVITY-07: identify factory storage through mounted root/data

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# CONNECTIVITY-07: identify factory storage through mounted root/data > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

CONNECTIVITY-06 is running, but this boot assigns internal eMMC `mmcblk1`. Mounted Y2ROOT/Y2DATA and logical capacity are correct; the factory provider assumes `mmcblk0` and exits before radio activation. This is a device-enumeration bug, not missing calibration or a reason to rewrite factory partitions.

The provider now resolves the block parents of the mounted `/` and `/data` through `/sys/dev/block/<major>:<minor>`. It requires partitions 5 and 7 on the same `mmcblkN` parent, type `MMC`, an actual matching block-node device number, and the unchanged 7784103936-byte logical geometry. It opens that parent with O_RDONLY/O_NOFOLLOW and only then performs the existing bounded protected reads. Wrong partition, another card, SD, absent node, regular file, mismatched device number or geometry fails closed. No `/dev/mmcblk0` alias or guessed fallback exists.

The regression exercises the production resolver for mmcblk0 through mmcblk7 and twelve failure conditions. Factory decoding, private outputs, identities, firmware and calibration contents are unchanged. The CONNECTIVITY-06 TX fix and all M4 hardware ownership are retained; its physical transport result is pending.

Rebuild the existing production Y2ROOT helper and package BOOTIMG + Y2ROOT with the preserving scatter. Keep Y2DATA and protected partitions untouched. Verify the new helper actually resides in the ext4 payload. After manual installation, inspect provider/MD/BTIF/WMT startup over SSH, then proceed with the original M5 qualification as interfaces become usable. M5 remains open; no new audit/inventory.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
