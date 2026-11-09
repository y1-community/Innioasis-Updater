---
title: "Y2Linux 1.0 Beta 9.3.16: steady Bluetooth - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.3.16: steady Bluetooth Release 1.0.0-beta.9.3.16 , Y2Reborn 1.0.0-beta.9.3.16 , kernel 6.18.56-y2linux-1.0.0-beta.9.3.16 , update sequence 14900, root"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.3.16.html"
---

# Y2Linux 1.0 Beta 9.3.16: steady Bluetooth - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.3.16: steady Bluetooth

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.3.16: steady Bluetooth

Release `1.0.0-beta.9.3.16`, Y2Reborn `1.0.0-beta.9.3.16`, kernel `6.18.56-y2linux-1.0.0-beta.9.3.16`, update sequence 14900, root `2026.08-platform-v1.247`. Published as GitHub release `baseline-224` (test build 224). Previous release: [Beta 9.3.15](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.15.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

Bluetooth headphones no longer go silent after a skip, a seek or the end of a song (Y2Linux #96, Y2Reborn #99, part of #87). The player now treats the Bluetooth connection the way a phone does: from the moment you press Play until you pause, it keeps sending the headphones a steady stream, music when there is music and silence while the next song gets ready. Before, the stream could run empty for a split second between two songs; the player's audio software then stopped and restarted it, and AirPods (and some other earbuds) stayed silent until you paused and played again. The rest of the Bluetooth path was made plainer at the same time: fewer clever tricks, one fixed rate, the same behaviour for every headset.

## What changed
  - Skips, seeks, the end of a song, gapless songs: the stream to the headphones never stops in between. A skip may

take up to about a fifth of a second longer to be heard; that is the small reserve that keeps the stream full.
  - Pause: the headphones get silence for 3 seconds, then the stream stops, as on a phone. Play within those

3 seconds continues at once; later, the headphones start a fresh stream (about half a second).
  - Play asks the headphones to start once. Before, every Play started, stopped and started the stream again

within a fiftieth of a second, which some earbuds answered slowly.
  - One rate for every headset: 44.1 kHz (48 kHz only for headphones that refuse it), and SBC and AAC at one fixed

bit rate by default, as phones send. LDAC keeps its own adaptive rate. If you changed the codec settings in the maintenance menu before, your choices stay.
  - Headphones that keep dropping right after connecting (for example after they were paired again with another

device and forgot the Y2) are no longer reconnected over and over: after three quick drops the player stops and asks you to remove them in Settings → Bluetooth and pair them again.
  - Wheel clicks with no music playing no longer stutter, and about one in ten gapless song changes no longer

runs the output empty (a click on headphones, silence on Bluetooth).

## How it was tested
  - Reports: every Bluetooth and playback event in the 28 error reports sent since Beta 9.2.16 was read. Since

Beta 9.3.12, 93 of 114 track changes on Bluetooth had run the stream empty (0 of 55 on 9.3.7); every one of the AirPods reports that went silent shows it.
  - Before release: the platform's full check, Reborn's workspace tests and the 552 tests of the release images.

New tests play the stream on a simulated pair of headphones that consumes it at real time and counts every moment it runs empty: quick skips while the next song is slow to open, seeks, songs ending, a pause. All run without a single empty moment; the skip and song-end tests fail on Beta 9.3.15's code. A new radio test: a headset that drops three times right after connecting is left alone until you tap it.
  - On a player: test build 224 installed by update on the developer's player; the AirPods reconnected by

themselves after the restart. The listening checks with AirPods (skips, seeks, song ends, pauses, radio) are next; if anything sounds wrong on your headphones, please send an error report right after it happens.

## Updating

Settings → System → Software Update → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Restore Previous System (Settings → System → About, tap Version seven times, then Diagnostics) goes back to the version you had.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) and [Beta 9.3.15](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.15.md%23known-issues&anchor=known-issues) still applies.
  - Sony WH-1000XM4 on LDAC with Wi-Fi on (Y2Reborn #87): a dropout followed by a fast burst. This release removes the

most likely cause on the player's side, but the shared Wi-Fi/Bluetooth antenna still limits LDAC; AAC or Wi-Fi off is the steadier choice. A report from 9.3.16 tells whether it is gone.
  - A skip, seek or pause is heard up to about 0.2 s later on Bluetooth than before.

## Technical appendix
  - Reborn `d4298f2` (`playback/output.rs`, `sink.rs`, `decode.rs`, `runtime/transport.rs`, `reborn-audio`): the sink

thread's `bridge` also feeds a kept Bluetooth sink between two streams (idle wait 10 ms; no 10 ms PCM wait without a sink); a Bluetooth song end is reported once its music is written (no drain; F69's song-end case); `BRIDGE_MS` 100; BlueALSA PCMs open with 8 × 1024 frames (wired stays 8 × 512); a Bluetooth pause holds in place and releases after `BLUETOOTH_HOLD_LIMIT` 3 s (`Runtime::hold_limit`); `plan_bluetooth` plans from the observed transport without opening the PCM; metric `bluetooth_xruns`; `decode.rs``settle`: a song's cover and the next song's open wait for ≥ 250 ms of its audio queued (F72); click stream 2048 frames (F71). Tests `stream_continuity_tests.rs`.
  - Linux `0c5fe178`: BlueALSA patches 0005 (learned start rate), 0007 (RTP timestamp over a gap) and 0008 (refill

faster than real time after a gap) removed with y2-radiod's start-level learning; `sbc_abr`/`aac_abr` default off; bluealsad `--a2dp-force-audio-cd`; y2-radiod `links::quick_drop` (3 links ending < 10 s park the headset, journal `reconnect_given_up`, F70); journal events carry the address. `5d87f546`: the Buildroot patch copy removes Y2 patches that left the repository (the first run of build 224 still applied 0005/0007/0008).
  - Linux `5d87f546` (built), Reborn `ceb4824` (built). Findings F69–F73 in the report ledger; architecture:

[radio daemon](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fradio-daemon.md).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
