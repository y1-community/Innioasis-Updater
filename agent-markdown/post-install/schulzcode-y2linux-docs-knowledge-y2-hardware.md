---
title: "Y2 hardware evidence baseline - Innioasis Updater"
description: "Y2 hardware evidence baseline <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-y2-hardware.html"
---

# Y2 hardware evidence baseline - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 hardware evidence baseline

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 hardware evidence baseline > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Current hardware result: [owner-observed M1 runtime success](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm1-runtime-hardware-result.md) confirms Linux 6.18, native PID1, increasing BEAT/uptime, working sleep, proc/sysfs mounts, CPU0, D08 RAM visibility, framebuffer diagnostics and stopped-watchdog status. M1 core achieved. Exact flashed hash and unreported diagnostic fields remain unverified. Earlier dated statements below are historical.

Y2B-240 hardware result: the owner reports solid green, which the implemented state machine reaches through initramfs `/init` running as PID1. M1's Linux 6.18 plus PID1 boot objective is achieved. No heartbeat/checkerboard success is claimed. [Y2B-245 / D14](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fon-screen-diagnostics.md) is the offline follow-up for readable runtime diagnostics.

Date: 2026-09-08. Related research: Y2E-101/105/110/115/120. Scope: one current device plus explicitly identified historical captures. CONFIRMED always means confirmed in the cited input/session, not every Y2 revision.````[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fstock-system-baseline.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fpartition-map.md)``````[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frecovery.md)

| Status | Fact | Evidence | Implication |
| --- | --- | --- | --- |
| CONFIRMED, current | MT6582, ARMv7, Cortex-A7 part 0xc07 with NEON/VFPv4 | 20260908-stock/cpuinfo.stdout | Linux target family supported by evidence; complete Linux board support not established. |
| CONFIRMED, current | Kernel reports version 3.4.67; Android 4.4.2/API 19 | version.stdout, selected getprop in baseline | Stock-family system only; exact installed image is UNKNOWN. |
| CONFIRMED, current | 7,784,103,936-byte internal eMMC user region and separate SD | partition map, capture 20260908-partitions | Respect hardware regions and vendor metadata differences. |
| CONFIRMED, historical | CS43131 and AW87559 driver bindings on I2C bus 1 | Verified snapshot 2026-07-29_004935/hardware/i2c-identities.txt | Separate headphone and speaker dependencies; wiring and analog behavior remain open. |
| CONFIRMED, historical | APT32F and UPDATE driver names on I2C bus 0 | Same snapshot | Name/binding does not establish controller function or firmware protocol. |
| CONFIRMED, historical | pmic_mt6323, input/controller nodes | Verified snapshot platform/input inventories | Useful discovery anchors for fresh passive subsystem research. |
| UNKNOWN | Physical PCB/FM revision, exact installed boot/system lineage, trusted battery readings | recovery assessment, current conflicting battery service output | Required before selecting a recovery baseline. |

The archive contains engineering reports rather than electrical verification of all routes. The current session did not re-run audio/FM experiments or scan hardware buses. See [evidence provenance](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fevidence-index.md) for hash validation and superseded claims, [open unknowns](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fopen-unknowns.md) for blockers, and subsystem documents for next proof requirements.

## Y2E-140 installed console evidence

2026-09-08: installed console core selects ttyMT0; sysfs and `/proc/iomem` map it to UART0 at 0x11002000. The FM driver was remapped to rule out index swapping. [Observation-path evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fobservation-path.md) supersedes UART3 as the first-artifact candidate. Native UART logic is expected to be 1.8 V from the manufacturer pin-domain table; no Y2 pad voltage or TX/GND test point is confirmed. Physical UART and actual LK/kernel wire capture remain a launch prerequisite.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
