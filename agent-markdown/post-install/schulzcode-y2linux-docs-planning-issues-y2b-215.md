---
title: "Y2B-215 — Describe the researched CPU0 first-boot hardware - Innioasis Updater"
description: "Y2B-215 — Describe the researched CPU0 first-boot hardware <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2b-215.html"
---

# Y2B-215 — Describe the researched CPU0 first-boot hardware - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2B-215 — Describe the researched CPU0 first-boot hardware

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2B-215 — Describe the researched CPU0 first-boot hardware > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Depends on Y2B-210 (#10), D08/D09. Offline only.

Create a minimal Y2 DTS from the audited upstream MT6582 CPU/GIC/sysirq/GPT and fixed-clock descriptions. Preserve provenance. Include only CPU0 and the package-default UART3 diagnostic candidate; omit unrelated peripherals. No guessed pinctrl, DMA channels, storage or reserved-memory expansion.

Acceptance:
  -  Exactly D08's two memory banks and permanent 16 KiB FDT reservation.
  -  initrd end derived later from actual gzip bytes; no placeholder may reach a final DTB.
  -  Single CPU, confirmed interrupt/clock addresses; no HYP/PSCI or unresearched device nodes.
  -  Controlled bootargs, stdout-path without early baud override; U10a explicitly remains a launch gate.
  -  Compile DTS syntax using a bounded test initrd length; final DTB requires the real initramfs and independent decoding.

Validation: upstream v6.18 dtc compiled the DTS without warnings using the explicitly test-only 0x1000 initrd length. Final DTB is rebuilt from the actual gzip length; this syntax-check DTB is not an accepted artifact. GIC virtualization register windows are omitted because only CPU0 distributor/CPU-interface operation is selected.

Historical checkpoint: Y2E-140 (#16) later supersedes the initial UART3 choice with installed-evidence UART0/IRQ51 (D10), rebuilding and revalidating the whole artifact. This completed issue remains the original implementation history.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
