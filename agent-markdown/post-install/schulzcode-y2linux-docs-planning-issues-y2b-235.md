---
title: "Y2B-235 — Prove offline reproducibility and publish the launch-gated result - Innioasis Updater"
description: "Y2B-235 — Prove offline reproducibility and publish the launch-gated result <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, can"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2b-235.html"
---

# Y2B-235 — Prove offline reproducibility and publish the launch-gated result - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2B-235 — Prove offline reproducibility and publish the launch-gated result

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2B-235 — Prove offline reproducibility and publish the launch-gated result > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Depends on Y2B-230 (#14). Final small checkpoint of this offline wave; M1 hardware first boot is not yet authorized.

Acceptance:
  -  One documented build command reconstructs all products from locked inputs, with no network/device access while compiling.
  -  Two separate clean output directories produce identical kernel/config/DT/initramfs/BOOTIMG bytes and ELF evidence.
  -  Full source-tree comparison against the locked archive confirms only the reviewed Kconfig overlay differs at build time.
  -  Actual-artifact negative tests reject malformed DT/config/ELF/compressed/package evidence; final D08 report and hashes retained.
  -  Update knowledge and milestone state with bounded offline research of U07b/U07c/U10a and backup/recovery gaps. Do not invent evidence or perform device operations.
  -  Retain an accessible complete artifact/evidence bundle and report the conditional first-device experiment, stopping before hardware.

Validation: two clean builds match across 11 outputs; full 91,166-file/link source check passes. Nine tests pass with 20 actual-artifact corruption cases and 25 package mutation/extent cases. Final bundle is revalidated before retention. Exact reports and unresolved launch gates are in docs/build/first-boot-result.md and docs/knowledge/first-boot-launch-gates.md. M0/M1 remain open; no device command was run.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
