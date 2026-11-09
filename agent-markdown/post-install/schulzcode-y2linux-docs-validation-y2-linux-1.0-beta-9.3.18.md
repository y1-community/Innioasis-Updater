---
title: "Y2Linux 1.0 Beta 9.3.18: USB that always reconnects, Luna XP, bitrate, quicker settings - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.3.18: USB that always reconnects, Luna XP, bitrate, quicker settings Release 1.0.0-beta.9.3.18 , Y2Reborn 1.0.0-beta.9.3.18 , kernel 6.18.56-y2linux-1."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.3.18.html"
---

# Y2Linux 1.0 Beta 9.3.18: USB that always reconnects, Luna XP, bitrate, quicker settings - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.3.18: USB that always reconnects, Luna XP, bitrate, quicker settings

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.3.18: USB that always reconnects, Luna XP, bitrate, quicker settings

Release `1.0.0-beta.9.3.18`, Y2Reborn `1.0.0-beta.9.3.18`, kernel `6.18.56-y2linux-1.0.0-beta.9.3.18`, update sequence 15200, root `2026.08-platform-v1.250`. Published as GitHub release `baseline-227` (test build 227). Previous release: [Beta 9.3.17](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.17.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

A computer always finds the player over USB again (Y2Linux #102): after an unplug at the wrong moment the player's USB chip could believe it was the computer's host, and no computer saw the player until a restart. Beside that fix come a new skin, Luna XP, contributed by eNKay; the bitrate for skins (#87); a "Connect to Wi-Fi" step on the update page when Wi-Fi is off (Y2Reborn #96); **holding Select on a Quick Menu tile to open its settings (Y2Reborn #101); a choice of how an artist's albums are sorted** (Y2Reborn #75); Cover Flow in the skin's own style (Y2Reborn #100); and a line in Settings → Library that says **which files the player cannot play** (Y2Reborn #104).

## What changed
  - USB: when the cable came out during the few seconds in which the player restarts its file transfer service, the

USB chip switched itself to host mode (the role a computer has). From then on it took every greeting of a computer for a fault, logged "Babble", and the player stayed invisible to every computer, cable and port until a restart. The player is a USB device only, so it now returns to device mode after every unplug, sleep or stop, and before every reconnect.
  - Luna XP skin: blue title bars, green start button and rolling hills, by eNKay. Its fonts were trimmed to the

letters the player needs (2 MB → 264 KB). There are now seventeen skins.
  - Bitrate (#87): skins can show a song's bitrate with `{bitrate}` ("320 kbps"). It is the file's average;

whether a file is CBR or VBR is not shown yet, and no shipped skin shows it yet.
  - Updates without Wi-Fi (Y2Reborn #96): with Wi-Fi off or not connected, Software Update shows **Connect to

Wi-Fi** ("Updates need the internet"), which opens the Wi-Fi settings, instead of a check that cannot work.
  - Quick Menu (Y2Reborn #101): hold Select on the Wi-Fi, Bluetooth or Brightness tile to open that page of

Settings; Back returns.
  - Artist's Albums (Y2Reborn #75): Settings → Customize → Browsing → Artist's Albums: Oldest First (as

before), Newest First or A to Z. It applies on an artist's page and inside each artist of Albums By Artist.
  - Cover Flow follows the skin (Y2Reborn #100): every skin now draws Cover Flow in its own colours and fonts, with

square covers where the skin's Now Playing cover is square (all but Bunny Bow and Big Type). Skin makers can style it with a `cover_flow` layout and `"cover_shape"`; the [skin guide](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fskins.md) has the details.
  - Files the player cannot play (Y2Reborn #104): WMA, DSD, Musepack, MIDI, .mp4 and similar files are not added

to the library. Settings → Library now says so, for example "40 files can't be played here (WMA), so they aren't in your library."

## How it was tested
  - USB: the reporter's error report showed the first connection working, then "Babble" 160 ms after every

plug-in. On the developer's player a script repeated the same steps (USB service stopped, cable "unplugged", service started, cable "plugged in"). On 9.3.18's test build 226 the player logged Babble 157 ms after the reconnect and never connected; on test build 227 it connected again 0.5 s after the reconnect, with no Babble. A new test models the stock disconnect code and shows the host mode it leaves behind without the fix.
  - New Reborn tests for each feature: the bitrate label, the update page offline, Quick Menu holds, the three

album orders, Cover Flow captions and square covers in every shipped skin, Luna XP against the rules every shipped skin follows, and the counts of files that cannot be played (they survive a quick scan that skips unchanged folders).
  - Before release: the platform's full check, Reborn's workspace tests and the tests of the release images.
  - On a player: test builds 226 and 227 installed by update on the developer's player; 227 is this release.

## Updating

Settings → System → Software Update → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Restore Previous System (Settings → System → About, tap Version seven times, then Diagnostics) goes back to the version you had.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help), [Beta 9.3.15](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.15.md%23known-issues&anchor=known-issues), [Beta 9.3.16](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.16.md%23known-issues&anchor=known-issues) and [Beta 9.3.17](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.17.md%23known-issues&anchor=known-issues) still applies.
  - A charge-only USB cable (no data wires) only charges; the player cannot tell it apart from a wall charger.
  - Skins that bring their own fonts (Luna XP, Winamp and others) show boxes for Chinese, Japanese and Korean titles.
  - Bitrate is the average only, and only skins that use `{bitrate}` show it; CBR or VBR is not shown yet (#87).

## Technical appendix
  - Linux `48503dbe` (`kernel/usb/role.h`, `kernel/platform/usb.c`): `musb_g_disconnect()` treats every OTG state

outside its B-device list as an unhandled disconnect and sets `A_IDLE` + `is_host`. The state is `OTG_STATE_UNDEFINED` whenever no gadget is bound (`musb_gadget_stop`, e.g. while the MTP responder restarts); `musb_gadget_start` only sets `B_IDLE` and nothing clears `is_host`, so `musb_handle_intr_reset()` took every bus reset for babble (ledger F78, report e17c1a4d). `y2_musb_disconnect()` wraps all three platform disconnects (sleep quiesce, stop, detach) and `y2_musb_peripheral()` resets the role before `musb_start` in `y2_usb_reconnect()`. Tests `tests/test_usb_role.py`; fixture mocks in `9e864a3d`.
  - Reborn `dba53bf`: `views_playing::bitrate_label`, `Ui::online()` for the update page, `quick_menu_hold`,

`ArtistAlbums` + `catalog::within_artist`, skin manifest `cover_shape` / `Ui::round_covers()` with covers rounded at upload, native element `"captions": false` with `{flow_title}``{flow_artist}``{flow_detail}`, the generator's `add_cover_flow`, `skins/luna-xp`, and `reborn-library/src/unplayable.rs` (per-folder counts in the additive table `scan_folder_unplayable`, valid while their mtime matches the folder record). Bump + contract `56298e9`.
  - Version 9.3.18 was first built as test build 226 (sequence 15100); test build 227 (sequence 15200) adds the USB fix

and is the published build.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
