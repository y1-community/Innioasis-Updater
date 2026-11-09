---
title: "Y2B-250 — ARM time32 nanosleep fix - Innioasis Updater"
description: "Y2B-250 — ARM time32 nanosleep fix <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2b250-result.html"
---

# Y2B-250 — ARM time32 nanosleep fix - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2B-250 — ARM time32 nanosleep fix

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2B-250 — ARM time32 nanosleep fix > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Subsequent owner hardware report confirms working sleep and increasing BEAT/uptime. [M1 core result and exact evidence limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm1-runtime-hardware-result.md). The report does not independently pin the flashed candidate hash; offline artifact identities below remain unchanged.

2026-09-08. [Issue #21](https://github.com/SchulzCode/Y2Linux/issues/21). Offline candidate ready; not flashed.

## Evidence and exact change

[Owner-reported Y2B-245 screen](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2b245-hardware-result.md) proves the real renderer, PID1 and proc/sysfs mounts, then stops with sleep -38 / ENOSYS at BEAT 0. No increasing heartbeat is claimed.

ARM EABI syscall 162 is `sys_nanosleep_time32`. The old linked table targets the weak ENOSYS alias at `0xc00309a8`. The one kernel config change is `CONFIG_COMPAT_32BIT_TIME: n → y`; `CONFIG_POSIX_TIMERS` remains disabled and is not required. No PID1, timer driver, DTS, framebuffer or watchdog code changed.

Code/build source commit `dff1e82`. Previously audited Linux v6.18 commit `7d0a66e4bb9081d75c82ec4957c50034cb0ea449`, Clang/LLD 20.1.8 and the locked environment are unchanged. Source/toolchain hashes are trusted from the prior audit, not recomputed across the source tree.

## Targeted validation
  - Exactly one clean build; resolved config comparison has exactly one changed option.
  - Linked table slot 162 now targets real, non-weak `sys_nanosleep_time32` at `0xc0066500`; `sys_ni_syscall` is separately at `0xc0030aac`.
  - Three syscall regression tests pass: real built mapping, rejection of disabled time32, rejection of table bytes redirected to ENOSYS despite correct config and an available real function.
  - The same check rejects the actual old kernel even with a fabricated enabled config.
  - Production ARM PID1 regression passes all nine syscall-fixture scenarios with console writes trapped. ARM init self-test passes. These are host tests, not proof of timer IRQs on the Y2.
  - D08/layout validation and final Android/MTK BOOTIMG wrappers, padding/read tail and 16 MiB partition bounds pass. No build warnings/errors.
  - DTB, init executable, cpio and gzip are byte-identical to Y2B-245. Emitted watchdog instructions match the previous candidate. PRELOADER/LK/partition layout are unchanged; no device operation occurred.
  - No unrelated full-suite, source/ROM/recovery audit or second reproducibility build was performed.

## Retained candidate

`/home/luca/Dokumente/Code/Y2Linux/out/m1-y2b250-time32/BOOTIMG.img`

1,093,632 bytes; SHA-256 `074c3e6946e6e8ac61bc1df0da4fa53807071dd50ae3db4def97563c9207afce`.

The separate bundle retains ELFs, resolved config, source archive, input lock, logs, layout.json, iteration.json, old-syscall.json and SHA256SUMS.````````````````````

| Object | Half-open physical interval |
| --- | --- |
| zimage | [0x80008000,0x8010f000) |
| appended_dtb | [0x8010f000,0x8010f730) |
| image | [0x80008000,0x80274ec0) |
| resident_kernel | [0x80008000,0x8029d4b0) |
| relocated_copy | [0x80275700,0x8037cd40) |
| relocated_dtb | [0x8037c600,0x8037cd30) |
| compressed_bss | [0x8037cd30,0x8037cd50) |
| malloc | [0x8037dd48,0x8038dd48) |
| initramfs | [0x84000000,0x84000f80) |
| lk_staging | [0x80007e00,0x80112600) |

D08 static RAM remains `[0x80000000,0x81800000)` and `[0x84000000,0x84080000)`, with `[0x80000000,0x80004000)` reserved. CPU0 only, appended DTB, no ATAG import or expansion. BOOTIMG remains within EMMC_USER `[0x01d80000,0x02d80000)`.

## Expected next screen

LK logo → kernel/PID1 status with mounts → successful sleep return, increasing BEAT/FRAME and changing runtime fields → STOP: RESTORE ANDROID after 50 successful sleeps. Existing external 60-second limit takes precedence over iteration completion. No automatic reset/restore.

This removes the confirmed ENOSYS cause. Actual timer wakeup and progress still require the next separately authorized device trial; a frozen screen must be recorded as new evidence. No automatic flash or M2 work.

## Reproduce this localized iteration

Use an unused output directory and the existing audited cache:`python3 tools/build/run.py --output out/m1-y2b250-time32 -- sh /project/tools/build/build.sh test_sleep_syscall.py test_pid1.py`

Omitting test patterns retains the full suite for architecture changes and release validation.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
