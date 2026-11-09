---
title: "Y2E-130 — Establish the safe initial Linux RAM map - Innioasis Updater"
description: "Y2E-130 — Establish the safe initial Linux RAM map <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2e-130.html"
---

# Y2E-130 — Establish the safe initial Linux RAM map - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2E-130 — Establish the safe initial Linux RAM map

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2E-130 — Establish the safe initial Linux RAM map > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Canonical issue: [https://github.com/SchulzCode/Y2Linux/issues/7](https://github.com/SchulzCode/Y2Linux/issues/7)

Depends on Y2E-125 (#6). Resolve U07a with offline FM-kernel/preloader/LK analysis and retained safe stock evidence. Ownership: research and architecture; no implementation handoff until the policy is fixed.

Acceptance criteria:
  -  Remap FM kernel reservation logic independently of old symbol offsets.
  -  Record preloader/LK RAM-bank construction, display, modem/connectivity and identifiable loader/secure/shared-memory exclusions, distinguishing static facts from actual runtime observations.
  -  Assess DMA risks at entry and choose a deliberately bounded initial memory map.
  -  Specify exact permitted kernel/decompression, appended-DTB and initramfs intervals, byte budgets and offline validation formulas; do not invent the actual size of an unbuilt kernel.
  -  Choose static DT memory or ATAG import and document all memory/initrd/command-line implications.
  -  Update authoritative knowledge and state whether offline implementation may begin. Keep this issue open if the memory policy remains architecturally unresolved.

No Linux build, DTS/kernel implementation, BOOTIMG creation/modification, flashing, device writes or delegated research. Recovery and launch gates remain separate from offline artifact-design readiness.

Result: offline memory policy complete under D08; see [initial-ram-map](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Finitial-ram-map.md). U07c remains an explicit inherited-DMA/secure-state launch gate. No Linux artifact or implementation issue created; M0 not passed.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
