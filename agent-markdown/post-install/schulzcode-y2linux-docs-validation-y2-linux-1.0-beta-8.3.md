---
title: "Y2Linux 1.0 Beta 8.3 (Baseline 89) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.3 Baseline 89 Status: PUBLISHED as GitHub release baseline-89 2026-10-18. Release 1.0.0-beta.8.3 , Reborn 1.0.0-beta.8.3 , kernel 6.18.56-y2linux-1.0.0"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.3.html"
---

# Y2Linux 1.0 Beta 8.3 (Baseline 89) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.3 (Baseline 89)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.3 (Baseline 89)

Status: PUBLISHED as GitHub release `baseline-89` (2026-10-18). Release `1.0.0-beta.8.3`, Reborn `1.0.0-beta.8.3`, kernel `6.18.56-y2linux-1.0.0-beta.8.3`, update sequence 6600, Linux `029d93e`, Reborn `03e6dff`. Built with `tools/production/release.py`: container suite 774 OK, host suite 801 OK, update suite (`tests.test_platform_update`) 34 OK, also under ThreadSanitizer and AddressSanitizer/UBSan, Reborn 517 OK (fmt, clippy clean); all seal checks PASS, no MediaTek firmware in any image. Not yet run on a player: the owner installs it over the air. Milestone audit BETA-8.3 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | f274a076a3f3008116723be42a8129ea1efb6eeabfa00dda2802dec036f0eb7f |
| Y2ROOT | 9c3663f01be5fccbdc1ba19202629db0f83f23f85eececb088e7ebd0996f571b |
| RECOVERY | 717aa95967ca41d1132d66a53bcb73fdcaeabb5114c92e3ca4a2e194149ccc69 |
| Y2DATA (no SSH key) | 05ffbf1afa1695bdab21bf439374e8498073398b255ecb516931ee5ce7ad1bd4 |

## A time left you can trust

Since Beta 8.2 the installer takes about 15 s, but its screen still said "This takes 1-2 minutes", showed "Estimating time left" for the first 8 s and then only "Less than a minute left"; the bar gave the backup 37 % of its length although the backup now takes about 2 s.````````````````

| Part | Change |
| --- | --- |
| Installer estimate (Linux 27cf2cf) | Each recovery run has a plan of its phases with a modelled duration from the owner's player: hashing 30, live-root backup 21, write 10 and readback 7.5 ms per MiB, fixed parts for the kept root (0.3 s), the boot backup (1.7 s) and BOOTIMG (0.8 s). Finished phases rescale the rest by how fast they really ran (another eMMC, a busier CPU); inside a phase with byte progress its own rate takes over. The bar moves with time and never goes back. |
| Progress line | "<percent> <step> <seconds left>" in /run/y2/recovery-progress and /run/y2/update-check-progress; the kernel log's step lines carry left=Ns. Older readers use the first two fields as before. |
| Recovery screen | About 15 seconds left (fives, as on Reborn's download screen), A few seconds left under ten; it counts down between reports and only raises the number when the estimate grew by ten seconds. With an older core it keeps the minutes. The first screen reads This takes less than a minute. |
| Reborn (59a8702) | The Checking the Update step shows the seconds left from the core's line instead of This takes a few seconds. |
| Faster verify (9c7dae7) | The kept root is hashed on its own core while verify hashes the new package's payloads, also in parallel; the backup step is logged where it starts (8.2 counted the kept-package check under verify: 3.2 s). |
| Phase timings | Each install and restore records its phases in milliseconds in the journal (timings: verify, backup_root, backup_boot, system, check, boot; restore, restore_check, restore_boot). |

Model against the 8.2 measurements on the owner's player: live-backup install 23.7 s modelled / 23.6 s measured, rollback 11.7 / 12.2 s, kept-package install 13.2 s modelled (8.2 measured 14.9 s with the serial hashing).

## What the owner's OTA to 8.3 will show

The player is on 6500 after the rollback test (Beta 8.2 report). Its kept 6501 package is not the running release, so the queue drops it and the recovery backs up the live root on four cores (about 24 s, estimated as such). The download check runs in 8.2's core (no seconds yet); the install runs in 8.3's recovery (seconds left). The update after that uses the kept package. `y2-platform update status` shows `timings` after each install.

## Device result: the owner's OTA 6500 → 6600 (2026-10-18)

Install (live root backup on four cores, as expected: the kept 6501 package was not the running release):``

| Phase (journal timings) | verify | backup_root | backup_boot | system | check | boot | Installer |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 8.3 | 1.37 s | 10.83 s | 1.32 s | 4.37 s | 3.98 s | 0.76 s | 22.6 s |
| 8.2 (6500, same path) | 1.8 s | 12.5 s (both backups) |  | 4.5 s | 3.9 s | 0.8 s | 23.6 s |

Estimate (kernel log step lines against the real end, 24.53 s): at `verify` 24 s left (real 22.6), at `backup` 21 s (21.3), at `system` 10 s (8.7), at `check` 5 s (4.7), at `boot` 1 s (0.8). The recovery's display ran normally (LK `lcm=1-st7701…`, panel adopted, vblanks about 67/s, backlight back at 1.0 s), so the countdown was drawn; the owner did not see it (to be confirmed whether the screen was dark already then).

Display fault after the restart into 6600: LK reported `lcm=0-st7701…`; the hand-over read the DSI correctly, then at the first modeset the DSI register reads lagged one register (`read-back ps=00000000 vact=000305a0`), three DSI power cycles did not clear it, panel commands were skipped (read-lag fail-fast, 8.1) and no frame completed (`flip_done timed out`, `commit wait timed out`). The same signature as the dark screens of 43/46 ([DSI read lag](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-44.md)); cause still unknown, nothing in 8.3 touches the display. Reborn never presented a first frame, so the health check queued the rollback at its 180 s deadline (`RollbackPending`, MISC set, no power-off): the next start restores 6500. Logs: `out/ota-89-owner/` (local).

## Known gaps
  - The DSI read lag after a restart is back and is now the most likely way an update fails (here the fourth

restart out of the recovery on 2026-10-18; the three of the 8.2 tests were lit). Its cause is still unknown.
  - The countdown on the recovery screen has not been seen by the owner yet.
  - Unchanged: the sleep drain with the panel powered down is not measured yet (#42); the GC9503V panel path awaits

a GC9503V owner (#45).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
