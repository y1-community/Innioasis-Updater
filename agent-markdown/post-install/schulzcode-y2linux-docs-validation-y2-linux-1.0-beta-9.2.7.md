---
title: "Y2Linux 1.0 Beta 9.2.7: wheel clicks whenever the music is not playing - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.2.7: wheel clicks whenever the music is not playing Release 1.0.0-beta.9.2.7 , Y2Reborn 1.0.0-beta.9.2.7 , kernel 6.18.56-y2linux-1.0.0-beta.9.2.7 , up"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.2.7.html"
---

# Y2Linux 1.0 Beta 9.2.7: wheel clicks whenever the music is not playing - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.2.7: wheel clicks whenever the music is not playing

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.2.7: wheel clicks whenever the music is not playing

Release `1.0.0-beta.9.2.7`, Y2Reborn `1.0.0-beta.9.2.7`, kernel `6.18.56-y2linux-1.0.0-beta.9.2.7`, update sequence 12300, root `2026.08-platform-v1.221`. Published as GitHub release `baseline-198` (test build 198). Previous release: [Beta 9.2.6](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.6.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

Beta 9.2.7 finishes the wheel click. It now clicks whenever no music is playing, also when no song is loaded or the song was paused long ago, on the headphones or on the speaker, whichever is in use; and quick turns of the wheel no longer crackle.

## What's new and fixed
  - Clicks without a song (Y2Reborn #77). With Wheel Click on (Settings → Customize), the wheel now clicks

whenever the music is not playing: nothing loaded, paused, or paused for a long time. The player switches the headphone or speaker output on for the clicks and off again ten seconds after the last one. A song you start in those ten seconds plays in the same output, so it starts as quickly as before.
  - Clicks follow the headphones. A song paused with headphones in and the headphones then pulled out clicked into

the empty headphone output; now the clicks move to the speaker (and back when the headphones go in).
  - No more crackle when turning the wheel quickly while paused. Beta 9.2.6 threw away the silence it had queued

for each click to make the next one sooner, and sometimes left the output with nothing to play, which crackled. Now each click simply goes into the next bit of silence; a click waits at most about 35 ms.

## What you'll notice
  - After a long quiet time the first click can come a fraction of a second late while the sound chip wakes up; the

next ones are immediate. On the developer's player the output was ready 40 ms after the wheel step.
  - The wheel stays silent while music plays, and on Bluetooth.
  - The click's loudness follows the volume.

## How it was tested
  - Before release: the platform's full check, Reborn's workspace tests and the tests of the finished release

images. New tests on a simulated headphone output: with no song, clicks open the output once, the next clicks use it, and a song started then plays in it without opening again; clicks while paused play over silence and the song goes on where it paused; a click while music plays leaves the music untouched.
  - On the developer's player: installed over the air from Beta 9.2.6 and confirmed by the player itself

(Acknowledged); the platform and Reborn running, health OK, kernel not tainted. With a song paused since the restart (no output open), two wheel steps opened the speaker output in 40 ms, played their clicks without an error or a gap, dropped the queued silence a second later and closed the output ten seconds after the last click.

## Updating

Settings → About & Updates → Check for Updates → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Settings → Diagnostics → Restore Previous System goes back to Beta 9.2.6 if you need to.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) still applies. How loud the click should be is a first guess; tell us if it is too loud or too soft.

## Technical appendix
  - Crackle: each click while clicking rewound the queued silence (`snd_pcm_rewind` of `snd_pcm_rewindable`,

which rests on a hardware pointer alsa-lib had not refreshed), so the queue could end empty: bursts of `xrun -32`. Now nothing is rewound; `click_over_silence` keeps ≈ 1536 frames queued in 256-frame pieces. `AudioSink::rewind`/`rb_sink_rewind` are gone.
  - Clicks without a stream:`Runtime::wheel_click` (wired output only; speaker route or headphones in) releases a

hold on the other route, sets the live volume and sends the wired plan (`click_spec`, planned once) with `Playback::click`; `SinkCommand::Click` wakes an idle sink thread. `click_while_idle` plays in the kept wired sink or opens one (`keep_for_clicks`, `sink_change` decides) and keeps it `CLICK_KEEP` (10 s, `KeptSink::until`) after the last click; `LINGER` (1 s) after it the queued silence is dropped (`discard`). A start reuses the sink through the usual switch. A sleep request now also closes a kept sink (`stop_and_wait`; its activity lease refused sleep).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
