---
title: "Y2Linux 1.0 Beta 8.30 (Baseline 129) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.30 Baseline 129 Status: PUBLISHED as GitHub release baseline-129 2026-10-24, installed on the owner's player before publishing. Release 1.0.0-beta.8.30"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.30.html"
---

# Y2Linux 1.0 Beta 8.30 (Baseline 129) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.30 (Baseline 129)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.30 (Baseline 129)

Status: PUBLISHED as GitHub release `baseline-129` (2026-10-24), installed on the owner's player before publishing. Release `1.0.0-beta.8.30`, Reborn `1.0.0-beta.8.30`, kernel `6.18.56-y2linux-1.0.0-beta.8.30`, update sequence 9401, root `2026.08-platform-v1.171`, Linux `e510867`, Reborn `44481c3`. Built with `tools/production/release.py` (130 s, resumed workspace, update based on `baseline-128`): container suite 880 OK, host suite 907 OK, Reborn workspace tests, `clippy -D warnings` and `fmt --check` clean; all seal checks PASS, no MediaTek firmware in any image. Milestone audit BETA-8.30 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | cada095e38ee9d9ab416c194d5ffba7e55b65091a09e4f39b205e2ba2212614c |
| Y2ROOT | d7fde44818e49cb3be8282d7f8895c7d213e47adb0d24be98c47457f9a1797c4 |
| RECOVERY | 04ecb5bb51f7751195163317455235940ce59aeba4c413c8be5f73aae5bbce0b |
| Y2DATA (no SSH key) | 90b547a61b8bd4cc670d5cc37d9f84e2695dbaa8751d4f8eef6c3cd138dd578f |

## Why

The GitHub triage of 2026-10-23 (15 open issues against Beta 8.28); the owner chose: #58, #55 (and the same fault elsewhere in Reborn), Y2Reborn #21.1 (Previous), Y2Reborn #22 (Bluetooth volume), the GC9503V power-down default (#42/#45), an assessment of #59, and the GitHub replies.

## What changed since Beta 8.29``````````````````````````````````````````````````````

| Change | Detail | Evidence |
| --- | --- | --- |
| No audiobooks in music queues (#58) | track_matches requires is_music() (it only checked online), so Play/Shuffle from All Songs, a genre, an artist or a folder and the genre song count leave audiobook parts out; the whole-library queue (play_index) too | Reborn 20a493b; UI test music_queues_skip_audiobooks_and_songs_play_in_list_order |
| Songs plays in list order (Y2Reborn #21.3) | A song picked on Songs (sorted A to Z) was queued in library (album) order; filtered_indices now takes the page's own rows for Songs, as for Album and Search | same test |
| Previous restarts the song (Y2Reborn #21.1) | More than 3 s into a song Previous seeks to 0; a second press goes back a song (books already restarted their chapter after 5 s) | Reborn 20a493b; device test below |
| A pending seek keeps its target | The device test found Previous kept playing at 23 s: a late Position report of the held stream overwrote the seek target during the 350-ms settle, so the reload started where the song was. Position reports are ignored while a seek is pending (the wheel seek had the same race) | Reborn 44481c3; device test below |
| Bluetooth absolute volume (Y2Reborn #22) | Headphones whose BlueZ MediaTransport1 carries Volume (AVRCP absolute volume) follow settings.volume: Reborn sets the transport Volume (0–127), keeps its software level at 100 % and adopts changes made on the headphones (reports within 1 s of its own set are echoes). The wired volume is kept in settings.wired_volume; the first takeover multiplies the headphones' level by the software level used so far (bluetooth_absolute_volume), so nothing gets louder. Headphones without Volume keep the software level. BlueALSA 5 already runs native volume by default; no platform change | Reborn 20a493b; unit test levels_round_trip_and_a_takeover_never_gets_louder |
| Recovery screen text (#55) | The screen shows 28 columns: "This takes less than a minute." (30), "Turning off to save the battery." (32) and "Press Power to see this again." (30) were cut; now "This takes under a minute.", "Turning off to save power.", "Press Power to see it again." A test checks every recovery_screen line and stuck reason | Linux 14e2c91; test_recovery_screen_lines_fit_its_28_columns |
| Reborn toasts no longer cut | An audit of all 72 toast strings against the toast's 326-px text width found 16 cut (e.g. "Couldn't reach the update server. Try again in a m…"); a toast too long for one line now takes a second line. The 171 preview states and every dialog title, body and button fit | Reborn 20a493b; UI test a_long_message_takes_two_lines_instead_of_being_cut, preview 44b |
| GC9503V panel power-down by default (#42/#45) | CONFIRMED_PANELS = {'st7701s', 'gc9503v'}: confirmed by the #45 reporter on 8.7 (normal picture through screen-off cycles and deep sleep; ≈1.9 mA overnight instead of 30–37 mA on #42) | Linux 14e2c91; test_power_final_27 |

## #59 assessment (not implemented)

ext4 SD cards are supported and allow any character but `/` in names (FAT/exFAT refuse `"*/:<>?\|`); ext4, f2fs and btrfs all cap a name at 255 bytes, so CJK names can be longer on exFAT (255 UTF-16 units). f2fs would need `CONFIG_F2FS_FS` and f2fs-tools for the read-only check and repair, with no real gain for a read-mostly music card; btrfs is too heavy for the Cortex-A7 (kernel size, RAM, slow checks); ext2 would only need `CONFIG_EXT4_USE_FOR_EXT2` and accepting the type, but has no journal. Answer posted on #59; nothing planned.

## Device results``````````

| Check | Result |
| --- | --- |
| Install by OTA staging (owner's player, ST7701S) | sequence 9400 Acknowledged; the rebuilt 9401 (seek fix) installed, see the next row, then Acknowledged |
| Hung start after the 9401 update restart | The first boot after recovery (b0d8ac40, boot reason 4) showed the splash's Couldn't Start; USB never came up and no Reborn log exists. It wrote its health trail at 4.9 s but never reached the boot.json record (the next boot's previous_boot_id is the 9400 boot), so it hung in early system start after the initramfs. The owner's hard restart cleared the pmsg trail. Same family as ledger F39 / #56 (hung update restart); not in code 8.30 changed. The next boot was healthy and acknowledged |
| Previous 22 s into a song (rebornctl seek 20000; previous; previous) | build 9400: first press kept playing (23.3 s), cause above; build 9401: 3 of 3 runs restart (0.8 s) then go back a song (queue position 3 → 2) |
| Panel switch | ST7701S power_down=Y, unchanged |
| Bluetooth absolute volume | not run: no headphones connected (the owner chose to publish; the #22 reporter is asked to confirm) |

## Open
  - Bluetooth absolute volume has not run with real headphones.
  - F39: the cause of the hung start after an update restart (twice now: #56 on 8.21, the owner's player on 8.30); the

pmsg trail does not survive the long-press reset.
  - #40 (split multi-artist tags), #41 (Album Artists), #50.3/#50.6 (genre to playlist, genre-filtered album) stay open.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
