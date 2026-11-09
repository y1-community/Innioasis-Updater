---
title: "Y2Linux 1.0 Beta 7 (Baseline 61) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 7 Baseline 61 Status: PUBLISHED as GitHub release baseline-61 2026-10-16. Release 1.0.0-beta.7 , Reborn 1.0.0-beta.7 , kernel 6.18.56-y2linux-1.0.0-beta."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-7.html"
---

# Y2Linux 1.0 Beta 7 (Baseline 61) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 7 (Baseline 61)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 7 (Baseline 61)

Status: PUBLISHED as GitHub release `baseline-61` (2026-10-16). Release `1.0.0-beta.7`, Reborn `1.0.0-beta.7`, kernel `6.18.56-y2linux-1.0.0-beta.7`, update sequence 5800, Linux `7c0ee9f`, Reborn `7ade64b`, git tag `baseline-61` in both repositories. Built with `tools/production/release.py` in 94 s: container suite 743 OK, all seal checks PASS, no MediaTek firmware in any image. Milestone audit: UI-V4 and BETA-7 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 328574ce484e319e4e6404bdfe52be54e22011ae7d01a42b225a75c869f631f7 |
| Y2ROOT | 38c19cc310c69c2ffe87d36fe2a1b003906f80c04585a7298e9c8cf5f50762a7 |
| RECOVERY | c0c96adafa18b6c0b2ed9021935e18ec7f45956fe53295eabbf5c23f2443e719 |
| Y2DATA (no SSH key) | 958d3135b0827facd6d411d8305794f02272f68a8c43c8ac3d2b829100b9ca59 |

## Since Beta 6.3

### Reborn: UI v4, one strict system

Owner (2026-10-16): since playlists, search and radio the UI "looks kind full"; the default look is liked but "still a little rough"; make it consistent everywhere, for listeners rather than developers, and remove what users would not need. Review of all 92 interactive screens (host renders, one device capture), the plan, the owner's four decisions and every phase are recorded in Reborn's [Product UI v4](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-UI-V4.md).

| Part | Change |
| --- | --- |
| Colour | One fixed accent for every control and state; the cover's colour only on Now Playing and the Home cover card. Skins keep their own accent. |
| Components | One focus row (neutral glass) in every list, page and menu; one button; one empty/info state (icon, title, sentence); one LIVE badge. Wi-Fi/Bluetooth lists in a grouped card, switches in the accent. |
| Home | Now Playing, Music, Playlists, Radio, Search, Settings (was ten items with counts). Music lists Artists, Albums, Songs, Genres and Folders with counts; Settings → Display → Home Menu pins any of them back on Home. |
| Less on screen | No hint lines (the hold-Select menus already name every action); no "NOW PLAYING" label, gapless icon or radio codec tags; stations read "Country · Genre" without ranks; Bluetooth Connected/Paired, Wi-Fi Saved/Secured/Open; folders show songs, not free space; theme picker shows each look's colours; Storage has bars and Scan; About shows "1.0 Beta 7" and the library size. |

Host evidence: 479 Reborn tests, strict Clippy, fmt; before/after previews of all 114 states and of all 16 skins compared by eye (skins change only where they show Reborn's own keyboard, rows or texts).

### Platform: two fixes from the Beta 6.3 overnight test (archive 156)``````````

| Part | Detail |
| --- | --- |
| Overnight | Beta 6.3, 14 h asleep (01:13–15:21), 27 maintenance wakes, all SPM/INFRA/PMIC/wheel/PHY counters clean, INFRA lost 0; drain ≈7.8 mA (8.3 build 26, 9.4 Beta 1). |
| CPU thermal zone | The 1100b000 monitor was programmed only at probe; INFRA power-down in sleep wipes it (monitor/period/filter/poll read 0), y2_soc_temp returned -ENODATA and the thermal core disabled cpu-thermal (passive 110 °C, critical 120 °C) until the next boot. Seen in archives 124, 125, 155 and 156. kernel/platform/thermal.c now programs the monitor again on resume when it is off. |
| Refused Power sleep | A routine BAT0 notification during sleep preparation invalidated the wakeup count (wake_event_in_progress; the screen went off for 4 s and came back; Beta 1's 06:38 self-wake had the same cause). product_sleep takes a fresh count up to two times; Power/RTC interrupts and the cable are checked again on each pass. 3 new host tests. |

## Device checks owed (after the owner's over-the-air install)
  - A tour of every screen with screen capture while the owner presses the buttons (UI v4 phase 4): Home, Music, Home Menu

pins, Now Playing (song and station), lists, menus, keyboard, Settings, Wi-Fi/Bluetooth, theme picker, About.
  - After a night asleep: `/sys/class/thermal/thermal_zone1/mode` is `enabled` and `temp` reads a value.
  - Wake with Power and press Power again within a few seconds: the player sleeps (no `wake_event_in_progress` refusal).
  - Still open: Beta 6.3 sleep while paused on battery, Beta 6.1/6.2 checks.

## Known gaps

FM radio (next beta, Beta 8); no 12/24-hour switch; in-place decoder seek (≈1 s on Bluetooth); sleep ≈7.8–9.4 mA vs stock ≈1.3 mA; Bluetooth range hardware-limited; no headphone-jack detection.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
