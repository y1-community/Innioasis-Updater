---
title: "Y2Linux 1.0 Beta 9.2.2: a status bar in every skin, finer brightness - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.2.2: a status bar in every skin, finer brightness Release 1.0.0-beta.9.2.2 , Y2Reborn 1.0.0-beta.9.2.2 , kernel 6.18.56-y2linux-1.0.0-beta.9.2.2 , upda"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.2.2.html"
---

# Y2Linux 1.0 Beta 9.2.2: a status bar in every skin, finer brightness - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.2.2: a status bar in every skin, finer brightness

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.2.2: a status bar in every skin, finer brightness

Release `1.0.0-beta.9.2.2`, Y2Reborn `1.0.0-beta.9.2.2`, kernel `6.18.56-y2linux-1.0.0-beta.9.2.2`, update sequence 11800, root `2026.08-platform-v1.216`. Published as GitHub release `baseline-193` (test build 193). Previous release: [Beta 9.2](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.md). Fixes after Beta 9.2 are numbered 9.2.1, 9.2.2 and so on; 9.2.1 was a test build only, and everything in it is part of this release.

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

Beta 9.2.2 answers requests from the GitHub issues and fixes one sleep problem from an error report. Every skin now shows Wi-Fi, Bluetooth, charging and a connected computer in its title bar, like the standard look. A 12-hour clock says AM or PM. Brightness goes in 5 % steps down to 5 %, set with the wheel. Fast scrolling jumps by letter only when you really spin the wheel. Equalizer files may hold up to 20 filters. And a player whose SD card does not answer its "power is going off" notice can sleep again.

## What's new
  - Status icons in every skin (Y2Linux #70, #73). The standard look showed Wi-Fi and Bluetooth (bright once

connected), a charging bolt and the computer icon; skins showed only the battery and the clock. All 16 shipped skins now show the same icons in their own colours and close the gap when one is off. Skin authors use the new `indicators` element ([skin guide](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fskins.md)).
  - AM and PM (Y2Linux #72). Where the time zone reads a 12-hour clock (the Americas and others), the status bar

and every skin show "9:41 PM" instead of "9:41". Skins can also show the short date with `{date}` ("Sat 31 Oct", or "Sat, Oct 31" with a 12-hour clock).
  - Finer brightness (Y2Linux #74). Select on the Brightness card in Settings → Display, then turn the wheel: it

moves in 5 % steps from 5 % to 100 % (the screen has 32 levels). Select or Back ends. Before, Select only cycled 20, 40, 60, 80 and 100 %. 5 % is darker than anything before, for use at night.
  - Fast scroll by letter only when you spin (Y2Linux #64). In long lists the letter jumps started after four quick

clicks, so a list could not be read through at speed. Now a quick, steady turn moves row by row (several rows per click when fast), and the letter jumps start only at the wheel's fastest speed.
  - Equalizer files with up to 20 filters (Y2Linux #76). AutoEQ writes ten, other tools more; files with 11 to 20

filters were refused. Twenty filters use about 6 % of one processor core while playing, ten about 3 %.
  - Sleep with SD cards that ignore the power-off notice (error reports 39778b8a and 8b00b513). Before sleep, the

player tells the SD card that its power is about to go off and waits for the card to confirm. One player's card never confirmed, so every first sleep failed, and the player then refused to sleep at all until the next update. Now the player writes the card's cache first, and a card that does not confirm is put to sleep the way cards without this notice always were (the stock firmware never sent it). And a device that refuses to sleep no longer blocks sleep for good: the player tries again two minutes later.

## What you'll notice
  - Wi-Fi and Bluetooth icons in your skin's title bar, and AM/PM in 12-hour time zones.
  - In Settings → Display: Select on Brightness, then the wheel.
  - Long lists scroll row by row at a quick, steady turn; spin hard for letters.
  - If your player sometimes would not sleep with an SD card in, it should now.

## How it was tested
  - Before release: the platform's full check on every change (formatting, code checks, the ARM build, the host

tests, the recorded answers of every command, old records still readable, Reborn's contract), Reborn's workspace tests, and the tests of the finished release images. New tests: the status icons in a skin and in every shipped skin, AM/PM at midnight and noon and the short date, brightness steps and their ends, the fast-scroll threshold, 20 and 21 equalizer filters, the SD-card patch, and a device that refuses to sleep (proven only when the kernel's own counters show exactly that attempt failing in that step).
  - Skins: every skin drawn on the computer in all its screens before and after; the title bars checked with all

icons on and with a 12-hour clock ("4:41 AM"). Code moves were checked to draw exactly the same.
  - On the developer's player: installed over the air from Beta 9.2 and confirmed by the player itself (Acknowledged);

all four services and Reborn running, health OK (Bluetooth was switched off), the music player ready 37.4 s after the restart, kernel not tainted, Wi-Fi online, every installed skin carries the new icons.
  - Not on the developer's player: the SD card that ignores the notice (only the reporter's card does that); the

feel of the new fast-scroll threshold and brightness wheel by hand.

## Updating

Settings → About & Updates → Check for Updates → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Settings → Diagnostics → Restore Previous System goes back to Beta 9.2 if you need to.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) still applies. Big Type cuts long screen titles a little earlier now that its title bar holds the icons.

## Technical appendix
  - F59 kernel (patch 0071, `drivers/mmc/core/sd.c`): on the Y2 SD host (`innioasis,y2-sd`, `CONFIG_Y2_POWER`),

`_mmc_sd_suspend` flushes the SD cache, then sends the power-off notification; on `-ETIMEDOUT` it clears `SD_EXT_POWER_OFF_NOTIFY` for the card and deselects it. Cause in the reports: `mmc1: Card stuck being busy! __mmc_poll_for_busy`,`mmc_bus_suspend returns -110` 1.1 s after the freeze (SDXC 116 GiB, manfid 0x11, oemid 0x455a, 03/2026).
  - F59 platform:`Run::kernel_refusal` treats a failed `/sys/power/state` write as a refusal (guard cleared,

`device_suspend_refused`, the 120-s retry gate) when `suspend_stats` show one more failure than before the write, in step `suspend`, with the write's errno. Other steps, stale counters or another error still quarantine.
  - Skins: element `indicators` (x = right edge, y, size, gap, color, dim, charge), drawn from the skin flags

`charging`, `bluetooth(_connected)`, `wifi(_connected)` and the USB state; `build_skins.py add_status` places it in the 15 generated skins, applied once to the hand-written Classic. Variable `{date}`.
  - Clock: one `clock_text` (AM/PM) and `date_text` in reborn-core, made once a minute with the clock.
  - Brightness:`BRIGHTNESS_MIN`/`BRIGHTNESS_STEP` (5) replace `BRIGHTNESS_LEVELS`; `Ui::brightness_input`.
  - Fast scroll: letter mode from 4 suggested steps (was 2).
  - Equalizer:`MAX_BANDS` 20; `RbDspConfig` 680 bytes. Host: 20 filters 2.07 s, 10 filters 1.11 s, none 0.36 s per

600 s of 48 kHz stereo.
  - Coding standard: the length limits are ceilings (functions 150, files 1500 lines; aim for 100 and 1000), so a

small change no longer needs a refactor first; the status bar moved to `components/status.rs`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
