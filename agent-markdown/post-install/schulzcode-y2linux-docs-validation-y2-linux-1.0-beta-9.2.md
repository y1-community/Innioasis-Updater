---
title: "Y2Linux 1.0 Beta 9.2: waking up at once - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.2: waking up at once Release 1.0.0-beta.9.2 , Y2Reborn 1.0.0-beta.9.2 , kernel 6.18.56-y2linux-1.0.0-beta.9.2 , update sequence 11600, root 2026.08-pla"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.2.html"
---

# Y2Linux 1.0 Beta 9.2: waking up at once - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.2: waking up at once

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.2: waking up at once

Release `1.0.0-beta.9.2`, Y2Reborn `1.0.0-beta.9.2`, kernel `6.18.56-y2linux-1.0.0-beta.9.2`, update sequence 11600, root `2026.08-platform-v1.214`. Published as GitHub release `baseline-191` (test build 191). Previous release: [Beta 9.1](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.1.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

If you pressed Power to put the player to sleep and then pressed it again to wake it, the screen could stay dark for up to about 20 seconds. This happened when the player had Bluetooth headphones saved that were switched off or out of reach. Beta 9.2 fixes that: a press to wake now lights the screen at once, and the player no longer waits for the headphones before it goes to sleep. Beta 9.2 also fixes a rare case where Reset refused with "the plan changed" although nothing had changed.

## What was wrong with sleep and wake

After every wake the player tries to reconnect your saved Bluetooth headphones. When they are off, each try takes about 20 seconds before it gives up. During that time the Bluetooth radio is busy.

If you pressed Power to sleep while such a try was running, the screen went dark at once, as it should. But before the player can really sleep it has to switch the radios off, and it waited for the headphone try to finish first. While it waited, it did not look at the Power button. A second press to wake was only noticed once the headphone try had given up: on the developer's player that took 6 to 18 seconds.

Beta 9.2 changes two things:
  - A press to wake is noticed at once, also while the radios are being switched off. The screen comes back

immediately and the player stays awake.
  - The player no longer waits for the headphones. When it wants to switch Bluetooth off and a headphone try is

running, it asks for that try to be cancelled (the same way the Bluetooth page already did when you switched Bluetooth off yourself). Going to sleep takes 1–2 seconds again instead of up to 20.

Your headphones still reconnect automatically after a wake when they are switched on.

## The Reset fix

Settings → Diagnostics → Reset first shows what it will remove and then asks you to confirm. To make sure nothing changed in between, the player compares the plan it showed you with the plan it saved. For about one plan in 450, a number in the saved plan was read back very slightly differently (in its last binary digit), and the reset refused with "reset plan changed". Trying again usually worked. Numbers are now read back exactly.

## Also in this release
  - In a skin without its own Music page, Music opens the Music menu again instead of a plain system page.
  - Code clean-ups in the player and the system services that do not change what they do.

## What you'll notice
  - Power to sleep, Power to wake: the screen lights at once, even with your headphones off.
  - Nothing else should look or behave differently. If something does, please send an error report

(Settings → Diagnostics).

## How it was tested
  - Before release: the platform's full check on every change (formatting, code checks, the ARM build, the host

tests, the recorded answers of every command, old records still readable, Reborn's contract), new tests for a wake press while Bluetooth is busy, while the radio chip switches off, for the cancelled headphone try and for the Reset plan, Reborn's workspace tests, and the tests of the finished release images.
  - On the developer's player: installed over the air from test build 190 and confirmed by the player itself

(Acknowledged); all four services and Reborn running, health OK, the music player on screen 20.7 s after the restart. With the saved headphones switched off and the player paging them, switching Bluetooth off the way sleep does was refused once, the page was cancelled and the second try went through 1.1 s after the first (before: up to ≈20 s). Bluetooth came back on and went on trying to reconnect the headphones.
  - Not yet checked on the player: the press to wake during that moment itself, because sleep needs the USB

cable out and the developer's checks run over it. The new tests cover it.
  - Not repeated for this release: overnight sleep, a low-battery shutdown, an SD card repair or format, and a

reset on the player (see Known issues).

## Updating

Settings → About & Updates → Check for Updates → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Settings → Diagnostics → Restore Previous System goes back to Beta 9.1 if you need to.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) still applies.

## Technical appendix
  - Cause (power journal of test build 190):`suspend_quiescing_radios` → `suspend_product_refused

wake_event_in_progress`took 17.6, 17.7, 6.4 and 15.6 s, each ending with bluetoothd's`avdtp_connect_cb … Host is down`for the saved headset.`y2-bt-reconnect`holds`/run/y2/bt-operation.lock` for its page; `bluetooth-power off` refused as busy and the sleep helper retried once a second for up to 25 s without reading the wake IRQs. The Python platform behaved the same; the rewrite did not cause it.
  - Fixes: the sleep helper's wake check is one function (`woken`) and now also runs in the radio quiesce retry

and while waiting for the connectivity chip to power down; a busy `bluetooth-power on|off` writes the `power_pending` intent, which makes `y2-bt-reconnect` cancel its page (`Device1.Disconnect`) and hold automatic attempts until the intent's deadline.
  - Reset: serde_json now has `float_roundtrip`; without it about 1 in 450 numbers read back one ULP off, and the

reset plan's confirmation is a hash over the plan as read from /data.
  - Tests: the reset goldens' target identity `device` (the host's st_dev of the fixture copy) is volatile like

`inode`; `record-compat.py` treats the `<volatile>` placeholder like null.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
