---
title: "Y2Linux 1.0 Beta 9.2.4: your own Home order, playlist order, wheel clicks - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.2.4: your own Home order, playlist order, wheel clicks Release 1.0.0-beta.9.2.4 , Y2Reborn 1.0.0-beta.9.2.4 , kernel 6.18.56-y2linux-1.0.0-beta.9.2.4 ,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.2.4.html"
---

# Y2Linux 1.0 Beta 9.2.4: your own Home order, playlist order, wheel clicks - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.2.4: your own Home order, playlist order, wheel clicks

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.2.4: your own Home order, playlist order, wheel clicks

Release `1.0.0-beta.9.2.4`, Y2Reborn `1.0.0-beta.9.2.4`, kernel `6.18.56-y2linux-1.0.0-beta.9.2.4`, update sequence 12000, root `2026.08-platform-v1.218`. Published as GitHub release `baseline-195` (test build 195). Previous release: [Beta 9.2.3](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.3.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

Beta 9.2.4 lets you put Home's items and your playlists in the order you want, adds an optional click on each turn of the wheel, and makes Cover Flow's text move with the covers. Everything new is off or unchanged until you choose it.

## What's new
  - Home in your order (Y2Reborn #53). Settings → Customize → Home Menu lists Home's items in Home's order.

Hold the centre button on one, turn the wheel to move it, and press the centre button to put it there (Back leaves it where it was). Home follows at once. Showing and hiding items works as before.
  - Playlists in your order (Y2Reborn #33). A playlist's menu (hold the centre button on it) has Move: turn the

wheel, press the centre button to put it there. The Playlists list keeps that order; new playlists come at the end.
  - Wheel click (Y2Reborn #67). Settings → Customize → Wheel Click: Off (as before), When Paused or

Always. Each step of the wheel gives a short tick through the headphones or the speaker, following the volume. While music plays the tick sits on top of it without taking anything away from the song; while paused, the music goes on exactly where it stopped.
  - Cover Flow (Y2Reborn #71). While the covers glide, the album's title, artist and details travel with their

cover and fade a little, instead of standing still in the middle. At rest Cover Flow looks as before.

## What you'll notice
  - Nothing changes until you use the new settings; Home and the Playlists list keep their usual order.
  - The wheel click needs a song loaded: it sounds while a song plays, or while it is paused (for the first three

minutes of a pause, while the player keeps the headphones ready). With nothing loaded there is no click: the player would have to power the headphone chip up just for it. It is never played over Bluetooth, whose delay would make the click come late.
  - After Restore Previous System, Beta 9.2.3 shows the standard orders (it does not know the new settings).

## How it was tested
  - Before release: the platform's full check on every change, Reborn's workspace tests and the tests of the

finished release images. New tests: a Home item moved to the end and Home following it, Back leaving it in place; a playlist moved up and the list keeping that order, the playlist menu's Move; Cover Flow's text standing with the incoming cover mid-glide; the click's shape, volume and end; on a simulated headphone output, clicks while playing changing only the click itself and not one sample of music lost or repeated, and clicks while paused playing over silence with the music going on where it paused; Wheel Click stepping Off, When Paused, Always; only wheel steps on a lit screen click.
  - On the developer's player: installed over the air from Beta 9.2.3 and confirmed by the player itself

(Acknowledged); the platform and Reborn running, health OK, kernel not tainted. How the click sounds and how loud it is still needs listening on a player.

## Updating

Settings → About & Updates → Check for Updates → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Settings → Diagnostics → Restore Previous System goes back to Beta 9.2.3 if you need to.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) still applies. How loud the click should be is a first guess; tell us if it is too loud or too soft.

## Technical appendix
  - Order: settings `home_order` and `playlist_order` (place keys and playlist paths; empty: the standard order;

items not listed follow in the standard order, names no longer there are skipped). reborn-core `home.rs` (`HOME_PLACES`, `ordered`, `moved`), reborn-ui `reorder.rs` (`Carry`; `mode_input` takes the wheel for the Brightness card and both moves), `Effect::SetHomeOrder`, `Effect::SetPlaylistOrder`.
  - Wheel click:`WheelClick` Off/WhenPaused/Always, `Playback::click`. The sink thread mixes a 4 ms, 3 kHz tick

(0.3 of full scale times the volume's gain) into the wired sink only. Playing: `AudioSink::rewind` (`rb_sink_rewind`, `snd_pcm_rewind` leaving 256 frames for the DMA; the AFE reads its pointer from `AFE_DL1_CUR`) takes back the unplayed frames, which `playback/click.rs``Tail` (the last 8192 written frames with positions) writes again with the tick at their start. Held: the unplayed music goes back to the pending block, the stream plays the tick over silence and pauses again 1 s after the last tick; the resume rewinds the silence.
  - Cover Flow:`flow::centre_x` places the text under the travelling cover, faded by its distance.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
