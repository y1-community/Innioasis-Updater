---
title: "Y2Linux 1.0 Beta 9.3.13: Wi-Fi that tries harder, square covers in skins - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.3.13: Wi-Fi that tries harder, square covers in skins Release 1.0.0-beta.9.3.13 , Y2Reborn 1.0.0-beta.9.3.13 , kernel 6.18.56-y2linux-1.0.0-beta.9.3.13"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.3.13.html"
---

# Y2Linux 1.0 Beta 9.3.13: Wi-Fi that tries harder, square covers in skins - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.3.13: Wi-Fi that tries harder, square covers in skins

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.3.13: Wi-Fi that tries harder, square covers in skins

Release `1.0.0-beta.9.3.13`, Y2Reborn `1.0.0-beta.9.3.13`, kernel `6.18.56-y2linux-1.0.0-beta.9.3.13`, update sequence 14600, root `2026.08-platform-v1.244`. Published as GitHub release `baseline-221` (test build 221). Previous release: [Beta 9.3.12](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.12.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

A small release of fixes from your reports. When you pick a Wi-Fi network and the player can't find it, it now does what helped every time by hand: it switches Wi-Fi off and on once and tries again (Y2Linux #83). A network the player can't join now says why ("WPA3 only", "Needs a login", "WEP") instead of only "Unsupported security" (Y2Linux #91). Letter scrolling puts the letter's first entry at the top of the screen in both directions (Y2Reborn #91), and three skin glitches are gone: covers with cut corners in square frames, Winamp's off-centre cover and the line through the title in Cassette (Y2Reborn #81, #82).

## What changed
  - Joining a Wi-Fi network that "isn't found" tries once more after a Wi-Fi restart (Y2Linux #83). A report showed

the player scanning for 34 s after Wi-Fi came on without seeing a network that was right there; Join answered "not found", and switching Wi-Fi off and on found it in 3 s. Now the player does that switch itself the first time a join finds nothing, and the screen keeps saying "Connecting…" meanwhile. The case where a router refuses the player again and again (also #83) is a different problem and still open.
  - A network the player can't join says why (Y2Linux #91). The Y2's Wi-Fi chip can't join WPA3 networks, and no

update can change that: its firmware makes the whole connection itself and only knows open, WEP, WPA and WPA2 networks. Networks that offer WPA2 and WPA3 together (often called "WPA2/WPA3 mixed") work, with WPA2. The row of a network it can't join now reads WPA3 only · Not supported, Needs a login · Not supported (work or school networks) or WEP · Not supported.
  - Letter scrolling lands at the top (Y2Reborn #91). Turning the wheel forward in letter mode put the letter's first

entry at the bottom of the screen, backward at the top; now it is at the top both ways.
  - Covers fit their frames in skins (Y2Reborn #81). Now Playing's cover always had Reborn's rounded corners, so

Terminal, Winamp and Paper showed cut corners inside their square frames. In a skin the cover is now square, and a skin that wants round corners rounds it itself (Bunny Bow). Winamp's cover is centred in its panel.
  - Cassette's stripe no longer runs through the song title (Y2Reborn #82): it sits along the top of the label and

the lines moved down.

## How it was tested
  - Before release: the platform's full check (host tests, recorded outputs, contract, code-quality ratchet),

Reborn's workspace tests (new tests for the Wi-Fi restart before a second try, the reasons a network can't be joined, and letter scrolling at the top) and the 552 tests of the release images.
  - Skins and the Wi-Fi page were checked on host renders of the player's screen (Terminal, Winamp, Paper, Bunny

Bow, Cassette; the Wi-Fi list with WPA3, login and WEP networks).
  - Not yet on a player: this build was not run on the developer's player before release. If anything behaves worse

than in 9.3.12, send an error report.

## Updating

Settings → System → Software Update → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Restore Previous System (Settings → System → About, tap Version seven times, then Diagnostics) goes back to Beta 9.3.12.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) and [Beta 9.3.12](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.12.md%23known-issues&anchor=known-issues) still applies.
  - WPA3-only and Enhanced Open networks can't be joined (hardware). Ask for "WPA2/WPA3 mixed" where you can.
  - A router that keeps refusing the player (Y2Linux #83, busy 2.4 GHz areas, band steering) is still being worked on.
  - Small cover pictures in skins' lists keep Reborn's rounded corners.

## Technical appendix
  - Reborn `crates/reborn-platform/src/wifi.rs``PendingJoin`: on the first `NotFound` it cleans up its block

(`finish`), asks `y2-radiod` for `WifiRestart` (the platform's F60 recovery waits 60 s for the same thing; without the daemon: rfkill off, wait for `wlan0` to go, on), waits up to 20 s for the supplicant and starts the same join once (`rejoin`; a saved network is found again by name). Evidence: report `1da7496c` (9.3.7).
  - WPA3: the gen2 driver offers only `connect` (firmware SME, auth modes open/shared/WPA/WPA2 in `wlan_oid.h`), no

external authentication, and `CFG_SUPPORT_802_11W` is 0; recorded in [m5-connectivity-implementation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm5-connectivity-implementation.md). wpa_supplicant is built without WPA3, so a WPA3-only network prints `[WPA2--CCMP]` (often with `[SAE-H2E]`). Reborn's `NetworkView::security` (`reborn_core::platform::NetworkSecurity`) carries the reason.
  - Skins: `Runtime::show_art` keeps the square cover and uploads it rounded only in Reborn's own look, again on a skin

change; `tools/assets/build_skins.py` (Winamp art y 192, Cassette stripe and rows); `render_previews.py` draws the cover square under a skin.
  - Letter jumps: `actions.rs` sets the scroll to the jump's target (clamped to the last page).
  - Linux `24d50299` (built), Reborn `94f417c` (built); work commits Reborn `5305f2e`, `23655e2`, `fcdf91d`, `1351b70`, Linux `f0ef28aa`,

`5344e69c`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
