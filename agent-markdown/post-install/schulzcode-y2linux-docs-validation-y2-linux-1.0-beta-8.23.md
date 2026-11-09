---
title: "Y2Linux 1.0 Beta 8.23 (Baseline 122) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.23 Baseline 122 Status: PUBLISHED as GitHub release baseline-122 2026-10-22. Release 1.0.0-beta.8.23 , Reborn 1.0.0-beta.8.23 , kernel 6.18.56-y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.23.html"
---

# Y2Linux 1.0 Beta 8.23 (Baseline 122) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.23 (Baseline 122)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.23 (Baseline 122)

Status: PUBLISHED as GitHub release `baseline-122` (2026-10-22). Release `1.0.0-beta.8.23`, Reborn `1.0.0-beta.8.23`, kernel `6.18.56-y2linux-1.0.0-beta.8.23`, update sequence 8705 (test builds 8700–8704 on the owner's player, see below), root `2026.08-platform-v1.161`, Linux `e3195fd`, Reborn `0779d8b`. Built with `tools/production/release.py` (117 s, resumed workspace, update based on `baseline-121`): container suite 867 OK, host suite 888 of 894 before the build (the other six read the 8.22 DTB from the artifact root, which still had a 50 ms delay on every DAC rail; the build's own DTB check passes), Reborn workspace 626 tests, clippy and fmt clean; all seal checks PASS, no MediaTek firmware in any image. Milestone audit BETA-8.23 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 70c9551ea2b05924fab64cd39de69e65e4eb9a1930274703a2fb7060257a5cb7 |
| Y2ROOT | 51d9c0109184d4b634f7803b0ae382b3b2db0358cf165370498621ec69c96ba8 |
| RECOVERY | bbf700126c5f559bdcc9dfe01b9f6921a8f6d17145604a231c1f21332bdd958e |
| Y2DATA (no SSH key) | f6d3677b6501fee48fccbed7d189bd639ebd5c2b2872f0bf362d43f70c5d5bbc |

## What changed since Beta 8.22````````````````````````````````````

| Finding | Change | Evidence |
| --- | --- | --- |
| F34 (users and the owner's player): after an update restarted the player, the recovery screen stood at "Installing Update – Checking the update. Step 1 of 4" for hours until Power was held; a forced restart then worked | The recovery feeds the SoC watchdog (31 s) only while the installer runs and its progress file changes; 120 s without progress stops the feeding and the watchdog restarts the player, which resumes or restores the install. The installer's steps go to pstore's message buffer, and the recovery keeps the previous start's trail and console in /data/logs/recovery-previous-boot.txt (reports collect it). The freeze's cause is still unknown; the next one leaves its trail | Linux aa0b483, 565b1a6; tests/test_production_handover.py (keeper, and every command the initramfs scripts run exists in the initramfs) |
| #52 on 8.22: the crystal started, but stopped while skipping quickly (17 error flags) | Reborn keeps the headphone output open across track changes with the same output, rate, format and wired settings (old audio dropped, 10 ms fade-in; closed 2 s after the last stream or at Stop), so the amplifier and its charge pump no longer power-cycle per track. Stock keeps its output open too | Reborn 0779d8b (sink_reused / sink_reopened events) |
| #54 on 8.22: the crystal was not ready even 45.9 s after power-up | The codec powers up as stock cs43131_hw_init: the crystal, the PLL and CLKOUT come up together, 20 ms later the crystal becomes MCLK (22.5792 MHz) and stays it until the codec powers down; its ready flag is read once there (ready_ms). The three DAC enables switch back to back with one 50 ms settle after the last (stock cs43131_on; was 50 ms after each) | Linux 16c0911, d04ee8e (overlay 0030, DT, tests/test_codec_clock.py, tools/validation/dev_dtb.py) |
| #52/#54: stock keeps the DAC powered from screen-on to screen-off | y2_hp/hold (kernel) holds the codec powered; Reborn sets it at startup and screen wake and releases it at screen-off and shutdown. System sleep still forces the codec down; after screen-off it powers down after the 2-min idle delay | Linux 16c0911, Reborn 0779d8b |
| F33 (Reborn): Update Now pressed while the platform worker was busy could be dropped | A task the owner starts waits for the worker's next turn; the update screen gives up after 30 s without a task; update tasks are logged | Reborn 6ec7ea7 |

## Device results (owner's player)````````````````````

| Check | Result |
| --- | --- |
| OTA 8607 → 8700 … 8705 | 8701/8702 installed but never restarted (the keeper's stop file used touch, absent from the initramfs; the watchdog then reset the player after ≈2.5 min, boot_reason=4) → fixed in 8703; 8703, 8704 and 8705 restarted by themselves 63–68 s after Update, Acknowledged on health boot 1 |
| Watchdog | a starved keeper resets the player in recovery and in the normal system (boot_reason=4) |
| Power-up as stock (8705) | after boot, before any Play: PWDN_CTL=f0 (crystal, PLL, CLKOUT on), SYS_CLK_CTL_1=04 (crystal, 22.5792 MHz), codec active, hold=1, ready_ms=30 (8704 showed the first stream's time, 62920 ms, fixed in d04ee8e) |
| Playback (8704, 8705) | 9/9 each: play, 20 Next/Previous 0.6 s apart, 3 × 20 at 0.3 s, 48 kHz (PLL), 96 kHz, back to 44.1 kHz; errors=0 unconfirmed=0, no crystal/ASoC kernel line |
| Output kept | 17/17 same-format skips reused the open output (sink_reused), 96 reuses in the session, 0 reopen failures |
| Hold | screen on: held; screen off: released, codec down 141–160 s later (2-min delay plus a later busy mark); screen on: held again with the crystal selected; play after wake PASS |

## Open
  - Not checked on a player: a real sleep and wake with this build (product sleep refuses with USB attached), a full

power-off/power-on, the battery cost of the crystal running while the screen is on (stock does the same), a click at a track change with the output kept (needs listening).
  - The hold write at screen wake powers the codec up synchronously (≈70 ms) when it was down.
  - #52/#54: confirmation from the reporters (`y2_hp/xtal`: `ready_ms`, `errors`, `unconfirmed`).
  - F34's cause: the next frozen install's `recovery-previous-boot.txt`. #56 (install 07e62fce, 8.17 → 8.21, frozen ≈1 h)

is the same freeze; its report holds only the successful second run (8.21 kept no trail of the frozen one). It also lost 93 % → 39 % in that hour while on a charger: not analysed (whether recovery charges, and what the frozen installer and its screen drew). F23 unchanged.
  - GitHub: comments on #52, #54 (retest, Send Error Reports + Install ID) and #56 posted 2026-10-22; the #56 comment's

last paragraph presents the battery drain as explained, which it is not (an edit was blocked; owner may correct it).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
