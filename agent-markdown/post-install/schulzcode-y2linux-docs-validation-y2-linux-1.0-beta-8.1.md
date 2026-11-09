---
title: "Y2Linux 1.0 Beta 8.1 (Baseline 86) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.1 Baseline 86 Status: PUBLISHED as GitHub release baseline-86 2026-10-18, after the device check on the owner's player. Release 1.0.0-beta.8.1 , Reborn"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.1.html"
---

# Y2Linux 1.0 Beta 8.1 (Baseline 86) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.1 (Baseline 86)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.1 (Baseline 86)

Status: PUBLISHED as GitHub release `baseline-86` (2026-10-18), after the device check on the owner's player. Release `1.0.0-beta.8.1`, Reborn `1.0.0-beta.8.1` (identity only), kernel `6.18.56-y2linux-1.0.0-beta.8.1`, update sequence 6463, Linux `78220dc`, Reborn `a558870`. Built with `tools/production/release.py`: container suite 774 OK, host suite 801 OK, all seal checks PASS, no MediaTek firmware in any image. Baselines 76–85 were test builds of this release (sequences 6450–6462), never published. Milestone audit BETA-8.1 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | c8313097064c9d05453f6ff6d232a0a8ccd20caff8ff14c6c043189d1f0a853f |
| Y2ROOT | a8d3dc55e817b4e0208c14fa41ba52ff56c2f210cb6c1d7c577480474f0e7ed9 |
| RECOVERY | ed5b51dc5508b2816b1f11c8069a37cb5e32ce1bf6a8901dc76b397a75efc0fd |
| Y2DATA (no SSH key) | b2e1059ea8483b4a3fac7f0f3277ba5999c2d68b3a459fb9dc4b03068f9592d6 |

## The panel never powered down (#45)

Reported by samanz: every screen-off logged `Skipping unprepare of already unprepared panel`. Confirmed on the owner's player and in the source: mtk-mmsys's reset controller had no `.status`, `reset_control_status()` returned `-ENOTSUPP`, `gc9503v_prepare()` failed for LK's lit panel and DRM never marked it prepared, so no screen-off ever ran display-off, sleep-in or reset. The panel slept powered and awake since the first release.

Fixing it showed that the Y2 ships with one of two panels and that Y2Linux only knew one. REA on the stock FM kernel (`out/rea/fm-kernel.elf`) and LK (`out/rea/fm-lk.elf`):``````````````````````````````````

| Stock code | Finding |
| --- | --- |
| Two LCM drivers | gc9503v_hvga_dsi_vdo_hsd (GalaxyCore GC9503V) and st7701_hvga_dsi_vdo_boe (Sitronix ST7701S), with different command sets and DSI timing. The owner's player has the ST7701S. |
| GC9503V lcm_init 0xc04a2470 (= lcm_resume) | reset 1/10 ms/0/10 ms/1/120 ms, 40 rows at 0xc09fe924: identical to gc9503v_init_cmds + sleep-out/display-on |
| ST7701S lcm_init 0xc04a2754 (= lcm_resume), lcm_suspend 0xc04a27d8 | reset 1/20 ms/0/50 ms/1/150 ms, 47 rows at 0xc09fffb8; suspend 7 rows at 0xc0a00cf0 + 50 ms, reset left high |
| lcm_compare_id 0xc04a2240 / 0xc04a2534 | GC9503V: DCS 0x04 = xx 95 03/04. ST7701S: 0xA1 = 0x88/0x99 |
| DSI_set_cmdq_V2 0xc05227f8 | commands above 0xAF go out as generic writes (0x13/0x23/0x29), the rest as DCS (0x05/0x15/0x39) |
| LK auto-detect 0x81e0af60, cmdline 0x81e183b0 | lcm=%1d-%s: the digit is LK's DCS 0x0A read result, not the ID match. The name is the first driver of the list [gc9503v, st7701] (0x81e3821c) whose lcm_compare_id matched, else the last one, st7701. The owner's player reports lcm=1-st7701… on some boots and lcm=0-st7701… on soft restarts. Corrected 2026-10-18 (after Beta 8.6): this row first said a failed read gives the last driver's name; a gc9503v name is a match with either digit (GC9503V compare 0x81e1eb60: DCS 0x04 = xx 95 03/04), see #45/#46. |

The first test build (6451) sent GC9503V commands to the owner's ST7701S at screen-on: white stripes. It was rolled back on the device, and the work below kept every step behind a switch.``````````````````````````````````````````````

| Part | Change |
| --- | --- |
| Panel identification (Linux d551d7b, 0fa1a6c, 2fda9d1, 9336bd4) | In order: LK's lcm=1- (y2_boot/metadata panel=, raw token in y2_boot/lcm); the stock ID reads at the first screen-on (panel_kind, read-only); a record from an earlier identified boot on Y2DATA (/data/system/platform/panel.json, handed back as panel_hint). Nothing is ever sent to an unidentified panel. |
| ST7701S support (de80a1a) | Stock init and power-down tables (checked byte for byte against the ELF) and reset timing. |
| GC9503V (372d8db) | Stock packet types for its init and its 27 power-down table. Not yet run on hardware. |
| Reset status (372d8db, overlay 0010) | mtk_mmsys_reset_status() reports the LCM_RST_B line, so LK's lit panel is adopted without a command replay. |
| Switch (372d8db, 430feeb) | panel.power_down (kernel default off = Beta 8.0 behaviour). The platform arms it at application_ready for a confirmed panel (ST7701S); a GC9503V player opts in with {"panel_power_down": true} in /data/system/platform/power-features.json. |
| DSI read lag (80c216b, overlay 0017) | A DSI whose register reads still lag after the power-on retries fails panel commands at once instead of waiting 2.5 s at the first screen-off. |
| Build (0cd2d50) | tools/build/run.py touches an overlay whose content changed for its path: a reverted patch had kept a stale object (test build 6452 shipped backed-out code). |

## Device result (owner's player, ST7701S, test builds 6450–6463, 2026-10-18)``````````

| Check | Result |
| --- | --- |
| Identification | register 0xa1 = 88: ST7701S at 0.92 s on every boot checked, including lcm=0 soft restarts; panel_kind=2, record saved |
| Switch | power_down=Y armed by the platform with no SSH action |
| Screen cycles (6456) | adoption, two power-downs (no errors), two full stock inits ST7701S sleep-out and display-on complete, picture normal (owner) |
| Screen-on time | ≈0.51 s for the full init (stock delays) instead of an instant backlight |
| OTA | every test build 6450–6463 installed and acknowledged; 6451 → rollback to 6450 → 6453 recovered the screen |

## Known gaps
  - Sleep drain with the panel powered down is not measured yet (#42): one overnight sleep on battery is owed. The

reporter's GC9503V unit read ≈4 mA in a first 2-h sleep with their own variant of the fix.
  - The GC9503V path (stock packet types) has not run on hardware; it is off by default until a GC9503V owner confirms

it (instructions in #45).
  - DRM keeps the GC9503V timing for both panels (ST7701S stock: porches 80/80/100/100 and other PLL dividers); the

ST7701S has worked with it since the first release.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
