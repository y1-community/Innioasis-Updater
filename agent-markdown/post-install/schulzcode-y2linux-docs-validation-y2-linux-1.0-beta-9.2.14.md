---
title: "Y2Linux 1.0 Beta 9.2.14: Bluetooth stays connected while you change stations - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.2.14: Bluetooth stays connected while you change stations Release 1.0.0-beta.9.2.14 , Y2Reborn 1.0.0-beta.9.2.14 , kernel 6.18.56-y2linux-1.0.0-beta.9."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.2.14.html"
---

# Y2Linux 1.0 Beta 9.2.14: Bluetooth stays connected while you change stations - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.2.14: Bluetooth stays connected while you change stations

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.2.14: Bluetooth stays connected while you change stations

Release `1.0.0-beta.9.2.14`, Y2Reborn `1.0.0-beta.9.2.14`, kernel `6.18.56-y2linux-1.0.0-beta.9.2.14`, update sequence 13000, root `2026.08-platform-v1.228`. Published as GitHub release `baseline-205` (test build 205). Previous release: [Beta 9.2.13](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.13.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

A user's Bluetooth earbuds disconnected while they listened to internet radio. Their error report showed why: each time they changed station, the player closed the Bluetooth output and opened it again (twice), and every time the earbuds were asked to start streaming anew. These earbuds sometimes took six seconds to answer, the most the Bluetooth system waits, and when an answer came later the connection was ended. The player now keeps the Bluetooth output open from one station or song to the next, as it already did for the headphone jack, so the headphones are not asked again. Pause still releases Bluetooth at once.

## What changed
  - Bluetooth no longer drops on quick station changes (error report `c0fe2638`): five stations in 30 seconds

made the earbuds miss one start request and the player end the link three seconds later; the same happened the day before with three stations. Now the next station or song plays in the open Bluetooth output whenever the headphones, their codec, sample rate and format are unchanged. After a reconnect, a codec change or a switch to other headphones or the jack, a new output opens as before. Skipping songs on Bluetooth gains the same.
  - New issue forms on GitHub (both repositories): a new issue opens a short form for its kind of problem

(something wrong, slow, battery and sleep, sound and Bluetooth, Wi-Fi and radio, install or update, a feature request, a question). Each asks for the version, an error report and what that kind of problem needs, for example the number of songs for a slow screen or the charger for a charging problem.

## How it was tested
  - Before release: the platform's full check, Reborn's workspace tests (775) and the tests of the finished release

images. New and changed tests: a Bluetooth sink plays the next stream without reopening and closes on a stop (which a Bluetooth pause sends); a kept Bluetooth sink is taken only while the observed connection, codec, rate and format are unchanged; a Bluetooth sink is kept for the same transport whatever the wired settings, not after a reconnect or another codec.
  - On the developer's player (from Beta 9.2.13 by update): staged in 7.8 s, installed and acknowledged on the first

start about 90 s after Apply; Reborn drew its first frame 20.7 s after the start, with no error. With AirPods Pro: six skips 2.5 s apart while playing, each in the open output (`sink_reused`, no new open, no Bluetooth error), and music heard after every one (Beta 8.38 had found AirPods silent when a stream restarted inside BlueALSA after a pause; a kept output drops its queued audio instead, as the headphone jack's does).
  - Still to check: quick station changes with the reporter's earbuds.

## Updating

Settings → System → Software Update → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Restore Previous System (Settings → System → About, tap Version seven times, then Diagnostics) goes back to Beta 9.2.13.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) still applies.

## Technical appendix
  - Evidence (report `c0fe2638`, install `d833b3da`, 9.2.13): `radio.station_started` at 17:41:50, :42:01, :07, :12,

:20 UTC, each preceded by `alsa.closed` and an `enabled_format` probe; `alsa.prepared` up to 6 s after the probe; bluetoothd `avdtp.c:cancel_request() Start: Connection timed out (110)` at 17:42:26 with `alsa.open_failed` -5, then `peer_disconnected` reason `local` ("Connection terminated by local host") at 17:42:29. Same on 10-31 21:24:48 (9.2.10) and 21:36:43 (a 44.1 → 48 kHz local change). No other saved report has an AVDTP Start timeout. Ledger F61.
  - bluez-alsa 5.0 releases the transport only when the PCM FIFO closes (`transport_threads_cancel_if_no_clients`);

`snd_pcm_drop` sends "Drop" and keeps it.
  - Reborn `3435238`: `keep_sink` keeps any output; `sink_change` compares the wired epoch only for the jack;

`keeps_bluetooth_sink` (main.rs) takes the kept spec while `SinkSpec::validate_bluetooth_observation` accepts the live `BluetoothPcm` (the plan's probe opens the PCM and cannot run while it is kept); idle wheel clicks play only in a wired kept sink; `Runtime::pause` on Bluetooth still sends `Stop` (F43).
  - Y2Linux `7176cb97`, Y2Reborn `c3277e2`: `.github/ISSUE_TEMPLATE/` (eight forms, `blank_issues_enabled: false`);

labels `performance`, `power`, `sound`, `wifi`, `update` created in both repositories.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
