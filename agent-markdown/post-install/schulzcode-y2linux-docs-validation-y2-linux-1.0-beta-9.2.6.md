---
title: "Y2Linux 1.0 Beta 9.2.6: wheel clicks while paused - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.2.6: wheel clicks while paused Release 1.0.0-beta.9.2.6 , Y2Reborn 1.0.0-beta.9.2.6 , kernel 6.18.56-y2linux-1.0.0-beta.9.2.6 , update sequence 12200,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.2.6.html"
---

# Y2Linux 1.0 Beta 9.2.6: wheel clicks while paused - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.2.6: wheel clicks while paused

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.2.6: wheel clicks while paused

Release `1.0.0-beta.9.2.6`, Y2Reborn `1.0.0-beta.9.2.6`, kernel `6.18.56-y2linux-1.0.0-beta.9.2.6`, update sequence 12200, root `2026.08-platform-v1.220`. Published as GitHub release `baseline-197` (test build 197). Previous release: [Beta 9.2.5](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.5.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

Beta 9.2.6 fixes the wheel click from Beta 9.2.4 (Y2Reborn #77): it was heard only while music played, not while paused. Now Wheel Click is simply On or Off, and it clicks while the music is paused, never over the music.

## What's fixed
  - Wheel click while paused (Y2Reborn #77). On Beta 9.2.4 the click sounded only over playing music; while

paused, every click failed. The player's headphone chip has no real pause: pausing lets the last moment of music play out and stops the sound output, and the click was sent to the stopped output. Now the first click starts the output again (after the paused music has played out), the clicks play over silence, and the output stops again a second after the last click. When you press Play, the song goes on exactly where it paused.
  - Wheel Click is On or Off (Settings → Customize). It clicks only while the music is paused; with music playing

the wheel stays silent. If you had chosen When Paused or Always on Beta 9.2.4, it is now On.

## What you'll notice
  - Pause a song with headphones in (or on the speaker), turn the wheel: a soft tick per step.
  - Still no click when no song is loaded, after a pause longer than three minutes (the player then lets the

headphone output rest) or on Bluetooth.

## How it was tested
  - Before release: the platform's full check, Reborn's workspace tests and the tests of the finished release

images. The click is now tested on a simulated headphone output that, like the real one, stops on a pause and refuses sound until started again (the test of 9.2.4 did not, which is how the bug slipped through): clicks while paused play over silence and the music goes on where it paused; a click asked for while music plays leaves the music untouched; the setting reads all of 9.2.4's choices.
  - On the developer's player: installed over the air from Beta 9.2.5 and confirmed by the player itself

(Acknowledged); the platform and Reborn running, health OK, kernel not tainted. Listening to the click by ear is still owed.

## Updating

Settings → About & Updates → Check for Updates → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Settings → Diagnostics → Restore Previous System goes back to Beta 9.2.5 if you need to.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) still applies. How loud the click should be is a first guess; tell us if it is too loud or too soft.

## Technical appendix
  - Cause (report ec243f8c): the AFE's DL1 has no `SNDRV_PCM_INFO_PAUSE`, so `rb_sink_pause` drains and the stream

ends in SETUP; 9.2.4 rewound and wrote to it: `ALSA -77` (EBADFD) for every held click.
  - Fix:`click_while_held` waits until `delay()` is 0 (the paused music played out), `pause(false)` prepares the

stream, `click_over_silence` writes; `LINGER` (1 s) after the last click `pause(true)` drains and stops it; the resume rewinds queued silence. A click requested while music is written is dropped. The rewind-and-replay of playing music (`Tail`, `joined`) is gone. `WheelClick` Off/On; On serializes as 9.2.4's `when_paused`, `always` reads as On.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
