---
title: "Y2Linux 1.0 Beta 9.1: tidying up after the rewrite - Innioasis Updater"
description: "Y2Linux 1.0 Beta 9.1: tidying up after the rewrite Release 1.0.0-beta.9.1 , Y2Reborn 1.0.0-beta.9.1 , kernel 6.18.56-y2linux-1.0.0-beta.9.1 , update sequence 11500, root"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-9.1.html"
---

# Y2Linux 1.0 Beta 9.1: tidying up after the rewrite - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 9.1: tidying up after the rewrite

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 9.1: tidying up after the rewrite

Release `1.0.0-beta.9.1`, Y2Reborn `1.0.0-beta.9.1`, kernel `6.18.56-y2linux-1.0.0-beta.9.1`, update sequence 11500, root `2026.08-platform-v1.213`. Published as GitHub release `baseline-189` (test build 189). Previous release: [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md).

This report is written for people who use the player. A short technical appendix is at the end.

## In one paragraph

Beta 9.1 looks and works like Beta 9.0, with one small visible change: while an update downloads, the Settings list shows how far it is ("Downloading · 40%"), not just "Downloading…". Everything else in this release is housekeeping that Beta 9.0 made possible. With the system services now written in Rust, the music player and the services can share one description of every message they exchange, so a mismatch between the two can no longer slip through unnoticed. The player's own code was also reorganised into smaller, clearer pieces, without changing what it does.

## Why release something you can barely see?

Beta 9.0 rewrote the services underneath the player. Two kinds of follow-up work were left:
  - The player and the services still described their messages separately. The services wrote, for example,

the battery state as a list of named fields; the player looked those fields up by name. If one side renamed a field and the other did not, nothing failed loudly: the player would just show "unknown". Beta 9.0 caught such mistakes with tests. Beta 9.1 goes further: both sides now use the same definitions, so the build itself refuses to finish if they disagree.
  - A few very large files. The player's main program file had grown to over 8,000 lines, and two functions

were more than 1,000 lines long each. That makes every future change slower and riskier.

Doing this now, while the rewrite is fresh, makes the next real features and fixes safer.

## What changed for the messages between player and system

The player now reads these in the system's own definitions:
  - the update page: whether an update is available, downloading, ready to install, or failed and why, and the

live download progress;
  - the battery level and low-battery warnings, and the shutdown notice before the player switches off;
  - whether Wi-Fi is really online;
  - the SD card and Internal Storage checks that decide which music folders the library may read;
  - the USB connection (the "Connected to a computer" screen and when the library refreshes after copying);
  - the progress of an error report you send or save;
  - the Internal Storage setup and the Wi-Fi/Bluetooth firmware state.

To be sure nothing changed by accident, the player's test that replays hundreds of recorded system answers gave exactly the same results before and after, apart from the download percentage mentioned above. That field had never been filled by the system; the Settings row now takes the number from the live download record the update page already used.

## What changed inside the player
  - The main program file went from 8,268 lines to under 1,000; the rest now lives in files named after what they

do (audio output, radio, queue, sleep, themes, the main loop, …).
  - The main loop, which runs all the time, is now split into 17 named steps (buttons, playback events, Bluetooth,

drawing, …), and the two audio threads into a decoding step, a crossfade step and seven output steps.
  - The screen code went from 4,493 lines in one file to about 1,000, plus files for navigation, menus, search and

drawing.

These moves were made by script and checked by comparing the moved code with the original: apart from naming, the code is the same, statement for statement. The same 748 automated tests pass before and after.

## What changed inside the system services

Small clean-ups: one shared check where two copies existed, one shared and carefully checked helper for the signal handling two services each did on their own, and fewer places that call the operating system directly (82 → 63).

## What you'll notice
  - Settings → About & Updates shows the download percentage while an update downloads.
  - Nothing else should look or behave differently. If something does, please send an error report

(Settings → Diagnostics): that would be a mistake in this release.

## How it was tested
  - Before release: the platform's full check on every change (formatting, code checks, the ARM build, the host

tests, the recorded answers of every command, old records still readable), Reborn's 748 tests, and 549 tests of the finished release images.
  - On the developer's player: installed over the air from Beta 9.0 and confirmed by the player itself. All four

services and Reborn running, Wi-Fi online, storage and health OK, no warning or error in Reborn's log since the update. Reborn read the battery record and the SD card's claim through the new shared definitions. Its built-in decoder, playback, storage and baseline tests pass on the player. From Power to the music player: 37.4 s, as with 9.0.
  - Not repeated for this release: overnight sleep, a low-battery shutdown, an SD card repair or format, and a

reset (see Known issues).

## Updating

Settings → About & Updates → Check for Updates → Update Now. Your music, playlists, settings, Wi-Fi networks and Bluetooth pairings stay. Settings → Diagnostics → Restore Previous System goes back to Beta 9.0 if you need to.

## Known issues

Everything listed for [Beta 9.0](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md%23known-issues-and-what-still-needs-your-help&anchor=known-issues-and-what-still-needs-your-help) still applies. In particular, overnight sleep, a low-battery shutdown, an SD card repair or format and a reset have not been repeated on the developer's player since the rewrite.

## Technical appendix
  - Shared contract crate (`y2p-contract`): new modules `update`, `power`, `network`, `storage`, `usb`,

`reports` and `radio`, moved out of the platform; the platform writes them and Reborn's client reads them. The power daemon's separate borrowing copy of power.json's record and the media hand-off's own USB reader are gone. Inventory: [CONTRACT.md "Records Reborn reads in the platform's types"](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fplatform%2FCONTRACT.md).
  - Reborn recorded contract: unchanged except `download_percent` (removed; download.json never carried a byte

count) and the version strings.
  - Reborn file split:`app/reborn/src/main.rs` → `runtime/`, `main_loop.rs`, `main_tests/`; `MainLoop::pass`

in 17 section methods, `shut_down`, `Watchdog`; `playback.rs` → `playback/` with `DecodeWorker` (`run`, `play`, `crossfade`) and `SinkWorker` (`Playing` state, seven sections); `reborn-ui/src/lib.rs` → eight `impl Ui` modules. Each move verified by undoing the renames and comparing with the previous text.
  - Platform:`py::truthy` is `lenient::is_truthy`; `sys::pipe`, `sys::signal_note`; `space.rs` and

`reports/media.rs` on the `sys` wrappers.
  - Checks: platform gate (formatting, clippy, armv7, host tests, goldens, record-compat, Reborn contract) on

every commit; Reborn workspace tests and clippy; container suite 549 tests in the release build.
  - Not in this release: the update core in Rust (it is the signed rescue's trust boundary and needs a hardware

round including recovery boots first).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
