---
title: "Y2Linux 1.0 Beta 9.2.8: why a Wi-Fi router turns the player away - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.2.8: why a Wi-Fi router turns the player away Release 1.0.0-beta.9.2.8 , Y2Reborn 1.0.0-beta.9.2.8 , kernel 6.18.56-y2linux-1.0.0-beta.9.2.8 , update s"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.2.8.html"
---

# Y2Linux 1.0 Beta 9.2.8: why a Wi-Fi router turns the player away - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.2.8: why a Wi-Fi router turns the player away

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.2.8: why a Wi-Fi router turns the player away

Release `1.0.0-beta.9.2.8`, Y2Reborn `1.0.0-beta.9.2.8`, kernel `6.18.56-y2linux-1.0.0-beta.9.2.8`, update sequence 12400, root `2026.08-platform-v1.222`. Published as GitHub release `baseline-199` (test build 199). Previous release: [Beta 9.2.7](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.7.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

Beta 9.2.8 changes nothing you will see. It makes error reports more useful for one Wi-Fi problem (Y2Linux #83): some routers refuse the player again and again although it is in range. From now on the player notes the reason each refusal gives, so a report shows whether the router turns the player away on purpose or never hears it.

## What changed
  - Wi-Fi refusals are recorded (Y2Linux #83). In the reports behind #83 the player saw the owner's network

clearly (a good signal), among about 50 other networks, yet the router refused to let it join up to 20 times in a few minutes. After each refusal the Wi-Fi waits a little longer before trying again, so the player could stay offline for minutes. The reports could not say why the router refused. Now they count each refusal by the code the router sent (or note that it never answered). Nothing that identifies the router is recorded.

## If your player keeps failing to join your Wi-Fi

Send an error report (Settings → Diagnostics) right after it happens. If your router uses one network name for 2.4 and 5 GHz ("band steering" or "Smart Connect"), it may push devices towards 5 GHz; the Y2 only has 2.4 GHz. A separate 2.4 GHz network name, if your router offers one, is worth a try.

## How it was tested
  - Before release: the platform's full check, Reborn's workspace tests and the tests of the finished release

images. New test: refusals are counted by their code and by "no answer", and no router address is kept.
  - On the developer's player: installed over the air from Beta 9.2.7 and confirmed by the player itself

(Acknowledged); the platform and Reborn running, health OK, kernel not tainted; its Wi-Fi status carries the new count (empty: that router never refused it).

## Updating

Settings → About & Updates → Check for Updates → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Settings → Diagnostics → Restore Previous System goes back to Beta 9.2.7 if you need to.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) still applies. Some routers refuse the player for minutes (#83); the cause is being investigated with the new reports.

## Technical appendix
  - `EventMonitor::count_reject`: `CTRL-EVENT-ASSOC-REJECT` and `CTRL-EVENT-AUTH-REJECT` counted as

`rejects {"association <status_code>[ timeout]": n, "authentication <status_code>": n}` in network.json's `supplicant_events` and the self-heal journal rows' `events` (no BSSID). Goldens and recordings re-recorded (only the new field); Reborn's platform contract re-recorded.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
