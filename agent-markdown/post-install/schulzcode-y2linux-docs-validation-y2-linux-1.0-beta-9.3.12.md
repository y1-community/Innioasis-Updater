---
title: "Y2Linux 1.0 Beta 9.3.12: Bluetooth pauses and skips like a phone - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.3.12: Bluetooth pauses and skips like a phone Release 1.0.0-beta.9.3.12 , Y2Reborn 1.0.0-beta.9.3.12 , kernel 6.18.56-y2linux-1.0.0-beta.9.3.12 , updat"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.3.12.html"
---

# Y2Linux 1.0 Beta 9.3.12: Bluetooth pauses and skips like a phone - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.3.12: Bluetooth pauses and skips like a phone

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.3.12: Bluetooth pauses and skips like a phone

Release `1.0.0-beta.9.3.12`, Y2Reborn `1.0.0-beta.9.3.12`, kernel `6.18.56-y2linux-1.0.0-beta.9.3.12`, update sequence 14500, root `2026.08-platform-v1.243`. Published as GitHub release `baseline-220` (test build 220). Previous release: [Beta 9.3.7](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.7.md). Versions 9.3.8 to 9.3.11 were test builds on the developer's player and were never published; everything in them is part of this release.

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

Beta 9.3.7 made the player keep a Bluetooth stream open while you paused, so that no headphones would be asked to stop and start again. That is a state phones never put headphones in, and it turned out to be the cause of three complaints: silence after a pause or after the second or third song (AirPods, Y2Linux #89), a dropped connection about 20 s into every pause (AirPods Pro), and Samsung Buds that "disconnected" a minute into a pause (Y2Linux #90, where the player had in fact gone to sleep). This release goes back to what phones and Beta 9.2.16 do: a pause stops the stream at once and Play starts a fresh one. On top of that a track change no longer interrupts the stream at all, and a paused player with Bluetooth headphones stays awake the 15 minutes it was always meant to.

## What changed
  - Pause stops the stream, Play starts a new one (as a phone does and as 9.2.16 did). Headphones that went silent

after a pause or a skip, and the connection drop about 20 s into a pause, both came from a stream kept open without sound: the headphones play what is in their buffer, run dry, and some (AirPods) never recover until a new stream starts. Measured on the developer's player: the packets to the headphones ran on without a single gap at the skips; the silence followed every pause/resume gap inside the kept stream.
  - A track change no longer interrupts the stream. Before, the player threw away the last tenth of a second of the

old song and the stream stopped for about 60 ms per skip. Now the old song's last fraction plays out and the next song follows it without a gap. (Y2Linux #89: "the second song is laggy, the third plays without sound".)
  - A paused player with Bluetooth headphones stays awake 15 minutes before it sleeps, so their play button keeps

working (Y2Linux #90). The 15 minutes were there since Beta 8.18 but counted from the first pause after boot rather than from each pause, so after a resume the next pause slept after 60 s, and sleep ends the Bluetooth link. On the reporter's log every "disconnect" was such a sleep, and the Buds reconnected within 5 s of every wake.
  - Headphones that connect with a different codec than the one you chose no longer drop and reconnect in a loop

(Y2Reborn #94: Bose SoundLink Flex 2, Sony WF-C710N). The codec change is now sent once the link is set up, and a change that ends the link is not sent to that headset again until you pick a codec again.
  - Two BlueALSA improvements for skips with a kept stream: the RTP timestamp follows real time across a gap, and the

sender refills the headphones' buffer after one.

## How it was tested
  - Before release: the platform's full check (host tests, recorded outputs, contract, code-quality ratchet),

Reborn's workspace tests (new tests for the paused-headset hold and the kept Bluetooth sink) and the 552 tests of the release images.
  - On a player: the developer's player with AirPods Pro: skips in a row, pauses of a few seconds and longer, all

with sound afterwards (test build 220, 2026-11-04). Test build 219, which still kept the stream open, was captured with btmon during the same actions: 47 packets per second without a gap at the skips, silence only after the pause/resume gaps, which is what settled the cause. AirPods Pro are the only headphones the developer has; the reports of #89, #90 and #94 were read against this build but not re-tested by their reporters yet.

## Updating

Settings → System → Software Update → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Restore Previous System (Settings → System → About, tap Version seven times, then Diagnostics) goes back to Beta 9.3.7.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) still applies.
  - After a sleep (a pause longer than 15 minutes, or the Power button) the Bluetooth link ends; the player reconnects

within a few seconds of waking. Buds that have meanwhile gone back to a phone must be picked again (Settings → Bluetooth, tap them).
  - The Hisense soundbar of Y2Reborn #94 (SBC only, connected but silent) is not resolved; try SBC quality High in

Settings → Bluetooth → Codec.
  - Only AirPods Pro were tested here. If your headphones behave worse than in 9.3.7, send an error report (Settings →

System → Error Reports): it contains the Bluetooth journal.

## Technical appendix
  - `y2-radiod` starts `bluealsad --keep-alive=0` again (`bt/supervise.rs`). 9.3.7–9.3.11 used 900 s because a Suspend

sent 10 s into an idle stream had gone unanswered one time in three (2026-11-03); the stream kept started without packets is what muted the AirPods (F43 in Beta 6 was the same effect) and made them stop answering the baseband 2 s into a pause (supervision timeout 0x08 20 s later).
  - Reborn: `platform::headset_hold_since` (hold from `paused_at`, cleared while playing; F68 in the report ledger);

`playback/sink.rs keep_sink` keeps a Bluetooth sink's queued audio and `reuse_kept` prepares it again on reuse; `output.rs hold()` does no device pause on a Bluetooth sink (that was a drain, a gap). F66: `bt/settle.rs``SWITCH_QUIET` 3 s after the link came up, `Codecs::kept` across reconnects, `Record::unset_since` for the half-connected rule.
  - BlueALSA patches 0007 (RTP timestamp on real time across a gap) and 0008 (refill up to 200 ms after a gap).

0008 can only send what the ALSA plugin's io thread has delivered, which it paces per period; it is not what fixed the skips.
  - Linux `31d3987e` (built), Reborn `d52589a` (built); work commits `75b6fad2`, `756c5e53`, `b13c1fbb`, `7bd63437`

(Linux) and `33ee726`, `8136838`, `5fa7e23` (Reborn).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
