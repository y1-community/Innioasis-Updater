---
title: "Y2Linux 1.0 Beta 9.3.7: Bluetooth rebuilt for reliability - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.3.7: Bluetooth rebuilt for reliability Release 1.0.0-beta.9.3.7 , Y2Reborn 1.0.0-beta.9.3.7 , kernel 6.18.56-y2linux-1.0.0-beta.9.3.7 , update sequence"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.3.7.html"
---

# Y2Linux 1.0 Beta 9.3.7: Bluetooth rebuilt for reliability - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.3.7: Bluetooth rebuilt for reliability

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.3.7: Bluetooth rebuilt for reliability

Release `1.0.0-beta.9.3.7`, Y2Reborn `1.0.0-beta.9.3.7`, kernel `6.18.56-y2linux-1.0.0-beta.9.3.7`, update sequence 14000, root `2026.08-platform-v1.238`. Published as GitHub release `baseline-215` (test build 215). Previous release: [Beta 9.2.16](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.16.md). Versions 9.3 to 9.3.6 were test builds on the developer's player and were never published; everything in them is part of this release.

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

Bluetooth on the Y2 used to be handled by five separate pieces (the player, a reconnect helper, the power switch, the sleep steps and the kernel's own recovery) that coordinated through lock files. When two of them acted at once, headphones stayed half connected, reconnects stalled, or the player waited on a lock until it was restarted. This release replaces all of them with one program that alone owns Bluetooth and the radio it shares with Wi-Fi. The player now only says what it wants ("these headphones, this codec") and the radio program gets there, retries in a fixed order, and repairs itself when a step fails. Every codec, rate and quality setting from 9.2.16 is kept.

## What changed
  - Headphones come back after sleep and when they reconnect by themselves. AirPods Pro were measured on the

developer's player: back and ready 2.5–5 s after the player wakes (often by themselves, with the codec you chose). Before, a wake could take about 15–20 s when the headphones reconnected on their own.
  - Bluetooth repairs itself. When a connection hangs or the Bluetooth service stops, the player cancels the stuck

step, then restarts the radio, then BlueALSA, then BlueZ, a few times each. If all of that fails, it says "Bluetooth stopped working. Turn Bluetooth off and on in Settings." Switching Bluetooth off and on now restarts all of Bluetooth, so that is the one thing to try.
  - Connect Automatically, per device (Y2Reborn #78). Settings → Bluetooth → a paired device → **Connect

Automatically** On/Off. Devices set to Off connect only when you tap them.
  - Codec and quality changes apply without restarting the player. The headphones disconnect and come back with

the new setting in about 7–9 s.
  - Your library is no longer emptied when a Bluetooth output fails (Y2Reborn #92).
  - Headphones that switch off are no longer paged forever. The player tries three times, then waits until they

come back by themselves, you tap them, or the player wakes.
  - Pausing keeps the headphones connected instead of telling them to stop the stream; some headphones answered

that late or not at all and lost the connection (but see Known issues).
  - Wi-Fi makes room while Bluetooth plays: while music streams to headphones, Wi-Fi uses its power saving and

leaves the shared antenna to the headphones between its check-ins; when you pause, Wi-Fi is back at full speed.
  - Wake order: after sleep, Wi-Fi waits (up to 12 s) until the headphones you had are back, so the two radios do not

fight over the antenna while they reconnect.
  - The player remembers how fast each pair of headphones can start and begins at that rate next time, instead of

starting at the top rate and stepping down.

## How it was tested
  - Before release: the platform's full check (host tests, recorded outputs, contract, code-quality ratchet),

Reborn's workspace tests and the 552 tests of the release images. The radio program has unit tests and runs against a fake BlueZ and BlueALSA through six scenarios: power on with a stuck connect, headphones switched off and coming back by themselves, a remote disconnect against your own, a refused codec, a missing audio stream, and a codec change. Each fix in 9.3.5–9.3.7 has a test that fails without it.
  - On a player: the developer's player with AirPods Pro, Wi-Fi on. 19 sleep/wake cycles on 9.3.6/9.3.7 with no

failed connection; Bluetooth on to ready 5.6 s; BlueALSA killed and back in 7.7 s; Bluetooth powered down for sleep in under 0.3 s; codec settings applied without a restart; the radio program uses no CPU while idle. No overnight run on this exact build yet, and AirPods Pro are the only headphones tried.

## Updating

Settings → System → Software Update → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Restore Previous System (Settings → System → About, tap Version seven times, then Diagnostics) goes back to Beta 9.2.16.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) still applies.
  - A pause longer than about 20 seconds drops the Bluetooth connection once (seen with AirPods Pro). About 2 s

after the music stops, the headphones stop answering; 20 s later the connection ends and they reconnect within a few seconds. If you press play during those 20 s, it can stay silent until they are back. Pressing play again after they reconnect works. The cause is being investigated.
  - Only AirPods Pro were tested. If your headphones behave worse than in 9.2.16, please send an error report

(Settings → System → Error Reports): it now contains the Bluetooth journal of the radio program.

## Technical appendix
  - New daemon `y2-radiod` (`platform/crates/y2-radiod`, [architecture](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fradio-daemon.md),

[plan, as built and measurements](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FBLUETOOTH-REIMPLEMENTATION-PLAN.md)): arbiter + one Bluetooth controller thread on the system D-Bus (asynchronous calls with deadlines) + socket `/run/y2/radiod.sock` (`y2p_contract::radiod`). Removed: `y2-bt-reconnect`, `y2-platform bluetooth-power`, intents, `bt-operation.lock`, `bt-pcm.lock`, `bt-codec-uncertain.json`, Reborn's D-Bus worker.
  - BlueALSA patches: 0004 LDAC ≤ MQ under the Wi-Fi ceiling, 0005 learned start level (AAC CBR, LDAC), 0006 accepts

an AAC configuration with stereo plus the channel bits A2DP 1.3 reserves (AirPods reconnecting by themselves send octet 3 = 0x07, refused before as `A2DP.InvalidChannels`). `bluealsad --keep-alive=900`.
  - BlueZ 5.87 resolves no services for a known headset that connects to us (`ServicesResolved` stays false for that

connection); the daemon counts a link as set up when BlueALSA has its stream (9.3.6) and waits up to 3 s for the headset's codec list, which BlueALSA has only after BlueZ asked the headset (9.3.7).
  - Pause drop: HCI disconnect reason 0x08 ≈ 22 s after the stream closed, same with Wi-Fi off and on links either side

opened; no sniff or role change before it; link supervision timeout is the controller default (20 s).
  - Linux `153a88cd` (built), Reborn `8fc6f69` (built); work commits from `bca291fc` to `4dbc51fc` (Linux) and

`e5ccbeb`, `33b6a43`, `e961a43` (Reborn).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
