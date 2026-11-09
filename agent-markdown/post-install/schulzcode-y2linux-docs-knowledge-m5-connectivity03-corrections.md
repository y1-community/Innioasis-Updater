---
title: "CONNECTIVITY-03: factory-path normalization - Innioasis Updater"
description: "CONNECTIVITY-03: factory-path normalization <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m5-connectivity03-corrections.html"
---

# CONNECTIVITY-03: factory-path normalization - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# CONNECTIVITY-03: factory-path normalization

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# CONNECTIVITY-03: factory-path normalization > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

The CONNECTIVITY-02 exception is now narrowed to a concrete service error using the installed strace and one bounded radio restart through the production core. The raw request/reply capture stays private under `evidence-private/20260916-m5-connectivity03/`; no new protected-partition copy, userspace MMIO or replacement service was deployed to the Y2.

Request 53 is OPEN (`0x1001`, flags `0x01010400`) of the existing factory record `X:\\MP0D_000`. The firmware sends two separators after the drive. The native path parser rejected the empty component and returned `-2`; MD immediately signalled `MD_EX`. The provider had already supplied this four-byte record; the failure was path handling, not missing factory acquisition.

Normalize repeated separators within the bounded virtual filesystem, selecting the same seeded record as the single-separator spelling. Unsupported drives, non-ASCII paths, traversal and embedded-NUL suffixes remain rejected. No modem path reaches the host filesystem. Existing immutable factory copies and RAM-only write shadows remain intact.

Host replay of this unit's 53 requests reproduced every observed result using the old source. Corrected source leaves results 1–52 unchanged and opens request 53 successfully. Synthetic seed bytes suffice for this prefix because no factory READ occurs before request 54. Neither captured requests nor private bytes are committed or installed as replay data. A regression test covers repeated root and nested separators, canonical identity, unchanged seed contents and invalid paths. This is a source-level reproduction, not a physical full-startup pass.

The kernel also identifies MD_EX explicitly and reports the last completed FS opcode/status without logging arguments, names or record contents. It retains fail-closed shutdown; an exception never counts as firmware readiness. The radio settings helper now recognizes the kernel's actual `functions=0x0` status when requesting recovery, in addition to decimal zero.

This correction changes Y2ROOT (calibration service/settings helper) and BOOTIMG (exception context/version). Packages and firmware provenance remain those of CONNECTIVITY-01. M4, DT sources, memory reservations and protected-write policy are unchanged. Y2DATA is preserved. Buildroot's existing offline build workspace may be resumed to avoid recompiling unchanged packages; finished prior release images remain untouched. The new component markers are CONNECTIVITY-03.

After manual installation, first verify progress past exchange 53, full MD calibration/shutdown and radio initialization. Continue the existing M5 physical procedure if readiness succeeds; target any further failure from its evidence. M5 remains open until end-user radio qualification passes.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
