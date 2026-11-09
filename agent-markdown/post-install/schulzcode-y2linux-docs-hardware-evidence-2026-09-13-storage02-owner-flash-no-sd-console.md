---
title: "No-SD console photo - Innioasis Updater"
description: "No-SD console photo Owner confirms USB connected, SD absent, and supplies a photo of Linux fbcon. Visible uptime is approximately 154–156 seconds. Repeated lines identify"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-hardware-evidence-2026-09-13-storage02-owner-flash-no-sd-console.html"
---

# No-SD console photo - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# No-SD console photo

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# No-SD console photo

Owner confirms USB connected, SD absent, and supplies a photo of Linux fbcon. Visible uptime is approximately 154–156 seconds. Repeated lines identify `mtk-msdc 11240000.mmc`, `msdc_track_cmd_data`, CMD55 with argument 0, CMD8 with argument 0x1aa, and `host->error=0x00000002`.

Source interpretation: kernel/dts/innioasis-y2-first-boot.dts maps 11240000 to the removable SD host; 11230000 is internal eMMC. SD uses `broken-cd`, which upstream drivers/mmc/core/host.c maps to MMC_CAP_NEEDS_POLL. The MMC rescan worker retries while no card responds. Upstream mtk-sd.c defines bit 1 as REQ_CMD_TMO and prints each failed command with dev_warn. Production inherits loglevel=8 plus ignore_loglevel, exposing all those expected empty-slot timeouts.

This establishes a running Linux console/display without SD and an empty-slot logging defect. It does not establish internal root/data mounts or explain the absent Linux USB gadget. The photo does not show an internal-eMMC failure, root handover result, kernel panic or the observer USB status rows. No code change or physical write is justified solely as a cure for USB from this photo. A temporary card insertion without reboot can test whether warning traffic stops; production neither automounts the card nor accepts it as root.

Photo retained privately as evidence-private/20260913-storage02-owner-flash/ no-sd-console.png; SHA256 3ad8223d6e3f929963d87f0eabff67178141d1d22eabeab1f9627a4820628dd4

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
