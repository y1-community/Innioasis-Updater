---
title: "Y2E-125 — Stock loader handoff and Linux 6.18 strategy - Innioasis Updater"
description: "Y2E-125 — Stock loader handoff and Linux 6.18 strategy <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2e-125.html"
---

# Y2E-125 — Stock loader handoff and Linux 6.18 strategy - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2E-125 — Stock loader handoff and Linux 6.18 strategy

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2E-125 — Stock loader handoff and Linux 6.18 strategy > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Canonical issue: [https://github.com/SchulzCode/Y2Linux/issues/6](https://github.com/SchulzCode/Y2Linux/issues/6)

The owner has successfully flashed this Y2 using SP Flash Tool and `y2_v3.2.0_FM-20260813`. Incorporate that recovery evidence, then establish the stock loader contract needed to design an upstream Linux 6.18 boot strategy.

Depends on completed Y2E-101 (#1), Y2E-105 (#2), Y2E-110 (#3), Y2E-115 (#4), and Y2E-120 (#5). This extends their findings; it does not duplicate or reopen their bounded inventories.

Ownership: research and architecture. This is not an implementation handoff.

Scope: offline inspection of the exact local preloader/LK/BOOTIMG and existing safe stock captures; source audit at upstream v6.18. Preserve provenance and distinguish owner observations, binary-derived facts, inferences and unknowns.

Acceptance criteria:
  -  Record owner-observed successful recovery, exact local ROM/scatter hashes, and the best supported previous SP Flash Tool version without claiming unknown DA/settings.
  -  Trace normal BOOTIMG load/launch addresses, machine identifier, boot-data format, ramdisk relocation and command-line source with binary offsets.
  -  Explain the header/runtime address discrepancy and identify DRAM/reservation limitations.
  -  Compare the contract with exact Linux v6.18 ARM/MT6582 source; specify a candidate packaging/DT/initramfs approach and its limits.
  -  Assess later eMMC rootfs options without treating all space after BOOTIMG as disposable.
  -  Update boot-chain, recovery, open-unknowns and linux-6.18-support; state the smallest remaining artifact blocker and a bounded next research proof.

No flashing, formatting, partition changes, boot-image edits/builds, kernel/DTS implementation or experimental boots. No implementation-ready issue until remaining architecture choices are resolved. M0 stays open while its separate backup/recovery prerequisites remain incomplete.

Result: bounded investigation complete. See [boot-chain](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fboot-chain.md), [recovery](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frecovery.md), [upstream audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Flinux-6.18-support.md) and [remaining unknowns](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fopen-unknowns.md). Candidate strategy established; safe memory envelope and ATAG policy remain the next research proof. No implementation handoff.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
