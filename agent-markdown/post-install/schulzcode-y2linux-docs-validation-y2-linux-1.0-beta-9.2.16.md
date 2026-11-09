---
title: "Y2Linux 1.0 Beta 9.2.16: steadier Bluetooth sound - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.2.16: steadier Bluetooth sound Release 1.0.0-beta.9.2.16 , Y2Reborn 1.0.0-beta.9.2.16 , kernel 6.18.56-y2linux-1.0.0-beta.9.2.16 , update sequence 1320"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.2.16.html"
---

# Y2Linux 1.0 Beta 9.2.16: steadier Bluetooth sound - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.2.16: steadier Bluetooth sound

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.2.16: steadier Bluetooth sound

Release `1.0.0-beta.9.2.16`, Y2Reborn `1.0.0-beta.9.2.16`, kernel `6.18.56-y2linux-1.0.0-beta.9.2.16`, update sequence 13200, root `2026.08-platform-v1.230`. Published as GitHub release `baseline-207` (test build 207). Previous release: [Beta 9.2.15](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.15.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

A user with Sony WH-1000XM4 headphones heard crackling and short cut-outs over Bluetooth (Y2Reborn #87). Their error report showed the player sending AAC at 320 kbit/s, the most these headphones accept, while Wi-Fi was on. The player itself kept up (no gaps in its own sound, no errors), so the losses happened on the way through the air. The Y2 has a single antenna that Wi-Fi and Bluetooth take turns on. Beta 9.2.16 therefore prefers steady sound over the highest numbers: lower default rates, and an extra limit while Wi-Fi is on. The same report showed a second fault: the codec chosen in the service menu (LDAC) was never used when the headphones connected while music was already playing. That is fixed too.

## What changed
  - Lower default rates for every Bluetooth connection. AAC now runs at 220 kbit/s (it was up to 320 kbit/s on

headphones that accept that), LDAC at 330 kbit/s (it was 660). At these rates AAC still sounds very good and leaves the radio room to repeat a lost packet in time.
  - An extra limit while Wi-Fi is on. As long as the Wi-Fi radio is switched on, AAC stays at or below 192 kbit/s

and SBC one step below its top quality. When Wi-Fi goes off (also by itself after a few idle minutes), the full rate comes back. The change happens while the music plays, without a pause or reconnect.
  - Auto picks AAC first. With the codec set to Auto, the player now asks for AAC, then aptX, then SBC. LDAC and

aptX HD are only used when you choose them yourself (service menu: Settings → System → About, tap Version seven times, then the codec page).
  - Your codec choice is used even when the headphones connect during playback (Y2Reborn #87). Before, the player

asked for it once, was refused because music was already playing, and gave up until the headphones reconnected. Now it asks again at the next pause.
  - If you prefer the highest rate anyway: the same service menu still offers AAC quality High and LDAC quality Standard or High. The Wi-Fi limit applies to them too while Wi-Fi is on.

## How it was tested
  - Before release: the platform's full check (581 host tests, recorded outputs, contract, code-quality ratchet),

Reborn's workspace tests (778) and the tests of the finished release images (554); the built `bluealsad` carries the ceiling check. New tests: the Wi-Fi limit's decisions for AAC and SBC (taken straight from the BlueALSA patches), that the encoders look at it on the first frame and then about once a second, that the platform keeps the limit exactly while the Wi-Fi radio is on, the new defaults, Auto's order, and that a refused codec choice is asked again at the next pause (the sequence from the report).
  - On a player: not yet. The developer's player was not connected when this release was built. Please send an

error report (Settings → System → Error Reports) if Bluetooth sounds worse or behaves differently than in 9.2.15.

## Updating

Settings → System → Software Update → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Restore Previous System (Settings → System → About, tap Version seven times, then Diagnostics) goes back to Beta 9.2.15.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) still applies. Whether the lower rates and the Wi-Fi limit remove the crackling for the #87 reporter is not confirmed yet.

## Technical appendix
  - Evidence (F63, report y2linux-report-20261101-185714, 9.2.14): AAC CBR 320 kbit/s at 48 kHz (XM4 capability

`c0 01 8c 04 e2 00`), BlueALSA `encoder_errors` 0, `aac_abr_adjustments` 0, Reborn Bluetooth xruns 0, no disconnects, no BTIF/WMT errors, Wi-Fi associated throughout. Host-side back-pressure never appeared, so BlueALSA patch 0002's adaptive rate never stepped down.
  - Platform defaults (`codec.rs``Policy::defaults`): `aac_quality` standard (no `--aac-afterburner

--aac-bitrate=320000`),`ldac_quality`mobile. An owner policy file (`/data/bluetooth/codec-policy.json`) keeps what it says.
  - Ceiling: the service daemon's coexistence pass keeps `/run/y2/bt-codec-ceiling` while the Wi-Fi state is not Off

(every pass, 3 s / 10 s dark; a removed file comes back) and reports it as `coexistence.json``codec_bitrate_override`. BlueALSA patch 0002 adds `y2-codec-ceiling.h`; the AAC encoder (0002) caps CBR at 192 kbit/s and takes its adaptive levels from the ceiling (the link's level is kept), the SBC encoder (0003) keeps off its top bit-pool (53 -> 45). Checked on the first frame/packet and then once per second of PCM; the rate changes in place through the encoders' existing runtime paths. VBR AAC and LDAC are untouched; packets stay sized for the configured rate, which is never exceeded.
  - Reborn `854a727`: the worker hands "playback holds the output" codec refusals to the app

(`Status::codec_deferred`, a growing sequence per refusal); `CodecReconnect` re-arms the attempt once per refusal, at most three times per connection. Reborn `7e9acd8`: Auto ranks AAC, aptX; LDAC and aptX HD only when chosen.
  - Linux `ea102152` (patches, platform, tests, re-recorded goldens and recordings, contract text); release bump Linux

`1b7df30e`, Reborn `8667100`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
