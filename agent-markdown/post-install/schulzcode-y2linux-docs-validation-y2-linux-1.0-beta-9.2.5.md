---
title: "Y2Linux 1.0 Beta 9.2.5: Wi-Fi finds your network again after a wake - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.2.5: Wi-Fi finds your network again after a wake Release 1.0.0-beta.9.2.5 , Y2Reborn 1.0.0-beta.9.2.5 , kernel 6.18.56-y2linux-1.0.0-beta.9.2.5 , updat"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.2.5.html"
---

# Y2Linux 1.0 Beta 9.2.5: Wi-Fi finds your network again after a wake - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.2.5: Wi-Fi finds your network again after a wake

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.2.5: Wi-Fi finds your network again after a wake

Release `1.0.0-beta.9.2.5`, Y2Reborn `1.0.0-beta.9.2.5`, kernel `6.18.56-y2linux-1.0.0-beta.9.2.5`, update sequence 12100, root `2026.08-platform-v1.219`. Published as GitHub release `baseline-196` (test build 196). Previous release: [Beta 9.2.4](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.4.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

Beta 9.2.5 fixes one Wi-Fi problem from an error report (Y2Linux #83): after the player woke up, Wi-Fi sometimes kept looking for your network without ever seeing it, and neither waiting nor Connect helped; only switching Wi-Fi off and on did. The player now does that itself when it happens.

## What's fixed
  - Wi-Fi that does not find your network after a wake (Y2Linux #83, finding F60). The player turns Wi-Fi off

after five minutes in the dark to save battery and on again when you wake it. In the report, the Wi-Fi then searched for 45 seconds, saw four other networks but never the owner's, and Connect said "not found". Switching Wi-Fi off and on in Settings connected within 5 seconds, with a good signal (−59 dBm). Now, when Wi-Fi has searched at least four times over a minute without seeing any saved network, the player switches it off and on once by itself, at most every ten minutes until it connects. Your Wi-Fi setting stays as you set it.

## What you'll notice
  - Usually nothing. If it happens, the Wi-Fi icon goes off for a moment about a minute after the wake and the player

connects shortly after.
  - Out of range of every saved network, the player does this once and then every ten minutes at most; it costs a

few seconds of the radio each time.

## About Wi-Fi range

The report also asked about range. The logs show a good signal once connected (−59 dBm), so the reconnect problem was not range. The Y2's small antenna does reach less far than a phone or laptop; that is a limit of the hardware that software cannot change.

## How it was tested
  - Before release: the platform's full check on every change, Reborn's workspace tests and the tests of the

finished release images. New tests: four searches over a minute that never see the saved network switch Wi-Fi off and on once, not again within ten minutes, again after a connect; a network that is seen, a wrong password, your own Disconnect and a connection in progress never do.
  - On the developer's player: switching Wi-Fi off and on the way the player now does: the Wi-Fi interface was

gone 20 ms after the switch-off, and Wi-Fi was connected again 12 s after the switch-on. The update was installed over the air from Beta 9.2.4 and confirmed by the player itself (Acknowledged); the platform and Reborn running, health OK, kernel not tainted. The failure itself could not be made to happen on purpose; it is tested with the report's sequence of events.

## Updating

Settings → About & Updates → Check for Updates → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Settings → Diagnostics → Restore Previous System goes back to Beta 9.2.4 if you need to.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) still applies. Why the Wi-Fi misses the network after a wake is not proven; both times in the report the Bluetooth headphones were reconnecting at the same moment, and Wi-Fi and Bluetooth share one radio. This release works around it.

## Technical appendix
  - F60:`WifiRecovery::restart_unseen` (connectivity `wifi/recovery.rs`): with the radio present and unblocked,

state SCANNING, DISCONNECTED or INACTIVE, no credential verdict and no held Disconnect, ≥ 4 `NETWORK-NOT-FOUND` (`EventMonitor::total`) over ≥ 60 s and no saved network in `scan_results` → write `1` to Wi-Fi's rfkill `soft` (`network::wlan_rfkill_soft`), wait ≤ 3 s for `wlan0` to go (the driver's `radio_work` coalesces a block undone before it runs), write `0`. At most every 600 s until CONNECTED. Journal row `wifi_restart` {unseen_s, not_found, saved, scan_entries, blocked, gone, unblocked, events}. The F52 self-heal never acted in the report because the supplicant stayed SCANNING.
  - Structure: the F52 lookup is `Look`; `network::wlan_rfkill` lists Wi-Fi's rfkill entries.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
