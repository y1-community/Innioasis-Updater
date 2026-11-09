---
title: "Y2E-145 — Assess authentication, recovery and bounded handoff launch gates - Innioasis Updater"
description: "Y2E-145 — Assess authentication, recovery and bounded handoff launch gates <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, cand"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2e-145.html"
---

# Y2E-145 — Assess authentication, recovery and bounded handoff launch gates - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2E-145 — Assess authentication, recovery and bounded handoff launch gates

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2E-145 — Assess authentication, recovery and bounded handoff launch gates > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Depends on Y2E-125/130, D08/D10 and the validated M1 artifact; observation remains Y2E-140 (#16). Research only with offline artifacts and safe read-only stock ADB. No security-state change, bypass, DA execution, flash, experimental boot or feature expansion.

Acceptance:
  -  Trace package unsigned-image policy to its actual inputs; distinguish package configuration from installed policy.
  -  Check current-device acquisition access, identify exact BOOTIMG range, and prepare a BOOTIMG-only backup/restore runbook using the owner-proven SPFT setup.
  -  Bound watchdog, storage DMA and final handoff findings to the requested CPU0/initramfs experiment; record adverse evidence.
  -  Record a supported GO / NO-GO decision and preserve artifact hashes.
  -  Obtain installed-loader/security evidence sufficient to accept the unsigned image without altering security.
  -  Retain verified current-device BOOTIMG and required personalized/recovery backups independently; establish exact DA/entry and restore semantics.
  -  Resolve the normal-path inherited watchdog and remaining DMA/secure-state launch risks.

Current decision: NO-GO. This issue stays open for the outstanding proofs; completion of bounded research is not closure of a hardware gate. No first-boot execution issue is created while the decision is NO-GO.

Findings: package ROM_INFO m_sec_boot=0x22 consults the hardware security bit; installed policy remains unobserved. Ordinary USB/ADB cannot provide early UART output, and the preloader USB/UART route requires electrical accessory detection. Current BOOTIMG is EMMC_USER [0x01d80000,0x02d80000), but present shell permissions deny acquisition. Tool/DA rehashed; exact historical operation logs absent. Normal LK arms a nominal 10-second watchdog interval with IRQ/dual mode; identified disable calls are Download/Fastboot, not normal handoff. No-watchdog candidate cannot be approved for 60 seconds. All 28 retained artifact members remain unchanged.

[Evidence/decision](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Flaunch-readiness.md), [prepared BOOTIMG-only runbook](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fbootimg-recovery-runbook.md). No firmware/security change, DA operation, flash, boot or Linux feature added.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
