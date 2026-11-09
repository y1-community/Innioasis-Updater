---
title: "Y2B-250 — Restore ARM time32 nanosleep for the diagnostic heartbeat - Innioasis Updater"
description: "Y2B-250 — Restore ARM time32 nanosleep for the diagnostic heartbeat <!-- knowledge-base-scope: historical-issue-specification -- Historical record. The dates, candidate i"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issues-y2b-250.html"
---

# Y2B-250 — Restore ARM time32 nanosleep for the diagnostic heartbeat - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2B-250 — Restore ARM time32 nanosleep for the diagnostic heartbeat

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2B-250 — Restore ARM time32 nanosleep for the diagnostic heartbeat > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Depends on [Y2B-245 #20](https://github.com/SchulzCode/Y2Linux/issues/20). Owner hardware evidence: renderer, PID1, proc/sysfs mounts work; first sleep returns -38 (ENOSYS), ending at `BEAT: 0 / STOP: SLEEP ERROR`.

Linux v6.18 ARM syscall 162 maps to `sys_nanosleep_time32`, compiled only with `CONFIG_COMPAT_32BIT_TIME`. The tested allnoconfig output disables it; the linked symbol is a weak alias to `sys_ni_syscall`. Enable only that config option. `CONFIG_POSIX_TIMERS` is not the dependency and remains disabled.

## Acceptance
  - Record the exact owner-reported screen and distinguish it from host tests.
  - Resolved config enables time32; linked table slot 162 targets the real function,

not the ENOSYS fallback. A regression rejects an actual table redirected to ENOSYS.
  - One clean locked build; targeted syscall and production PID1 regression tests.
  - Existing D08/layout/BOOTIMG checks pass, without relaxing any bound; record hash/size.
  - CPU0, static DT, watchdog stop, inherited framebuffer guards, initramfs and

preloader/LK/partition layout remain unchanged. No flash, M2 or new subsystem.
  - Trust previously audited source/toolchain/recovery inputs; no repeated full

source/provenance/recovery audit or second reproducibility build for this fix.

Expected next trial: advance beyond sleep error to increasing BEAT/FRAME and runtime fields; after 50 successful sleeps, STOP/RESTORE. Hardware behavior is pending a separately authorized test; offline validation does not prove IRQ timing.

Completed offline at `dff1e82`; [result, hash and targeted validation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2b250-result.md). All acceptance checks passed. Next device trial needs separate authorization.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
