---
title: "Y2B-210 — Select the CPU0-only diagnostic kernel configuration - Innioasis Updater"
description: "Y2B-210 — Select the CPU0-only diagnostic kernel configuration <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate identi"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2b-210.html"
---

# Y2B-210 — Select the CPU0-only diagnostic kernel configuration - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2B-210 — Select the CPU0-only diagnostic kernel configuration

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2B-210 — Select the CPU0-only diagnostic kernel configuration > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Depends on Y2B-205 (#9). Use audited Linux v6.18 with only the documented D09 Kconfig visibility patch, allnoconfig plus a reviewed minimal fragment. D08 is fixed.

Acceptance:
  -  ARMv7 little-endian ARM mode, CPU0 only, non-LPAE/non-highmem; appended DTB enabled and ATAG conversion disabled.
  -  OF/GIC/MTK sysirq/GPT fundamentals; built-in initrd/gzip/ELF, proc/sysfs and diagnostic serial console support only.
  -  No block/eMMC rootfs, network, USB, display, audio, radio, CMA, kexec or peripheral DMA framework.
  -  Reconcile the resolved .config against mandatory options automatically. Document optional serial support as a launch-gated candidate, not proof of physical routing.

Validate configuration resolution in the locked environment. Kernel compilation and DTS/initramfs belong to subsequent checkpoints.

Configuration resolution initially rejected hidden ARM_VIRT_EXT=y. Bounded source review produced D09 (docs/build/kernel-policy.md): one prompt-visibility line, leaving the upstream default intact and allowing the existing no-hyp path. The resolved fragment now passes every mandatory option; memory policy is unchanged.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
