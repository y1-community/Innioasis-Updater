---
title: "Y2 Rockbox Beta V2 Release - Innioasis Updater"
description: "Y2 Rockbox Beta V2 Release Updated: 2026-09-06 Tag: v0.2.0-beta Public release: <https://github.com/SPYCEMAGIC/Y2-Rockbox/releases/tag/v0.2.0-beta Immutable release ident"
language: "en"
source: "https://innioasis.app/post-install/spycemagic-y2-rockbox-00_project_docs-y2_rockbox_beta_v2_release.html"
---

# Y2 Rockbox Beta V2 Release - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=rockbox-y2)

Post-install setup · Rockbox-Y2 · Y2

# Y2 Rockbox Beta V2 Release

The Y2 Rockbox build. Select Y2 before choosing this Software.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=rockbox-y2)[Install guide](../guide.html?model=Y2&software=rockbox-y2)

# Y2 Rockbox Beta V2 Release

Updated: 2026-09-06

Tag: `v0.2.0-beta`

Public release:

[v0.2.0-beta](https://innioasis.app/release_notes.html?author=SPYCEMAGIC&project=Y2-Rockbox&version=v0.2.0-beta&software=rockbox-y2)

## Immutable release identity
  - Candidate parent commit: `7E50B1A8FAABC810669B0753282A89206371D20B`
  - Rockbox source commit: `5073CC9D380F8D01016ACE6DCEEA89E0684038C1`
  - macOS asset: `Y2-Rockbox-Beta-v0.2.0-UPDATE-ONLY.zip`
  - Windows asset: `Y2-Rockbox-Beta-v0.2.0-Windows-UPDATE-ONLY.zip`
  - Size: 361,774,260 bytes each
  - SHA-256: `409DDB4D2D18111FB8C3AB619F10F04B916B6B2A3FC04D1D38011324563F326A`

The two platform files are byte-identical Class A state-preserving updates. Their separate names let each guarded updater bind to the exact qualified delivery contract. This corrected identity replaces every earlier Beta V2 flash archive.

The archive contains only the Y2 scatter, UBOOT, BOOTIMG, RECOVERY, LOGO, ANDROID, its signed update contract, and internal checksums. PRELOADER, partition-table images, SEC_RO, CACHE, USRDATA, and protected/runtime partitions are absent.

## Highlights since Beta V1
  - Bluetooth Settings, pairing, A2DP playback, controls, disconnect, and

reconnect from Rockbox and Stock.
  - Held Previous/Next seeking and optional held-Volume track skipping.
  - Persistent time/date without UI freeze.
  - Adjustable Rockbox wheel haptics, including true-off, independent from Stock.
  - Reliable first-connect and repeated USB Storage lifecycle on both routes.
  - Cleaner boot presentation and reliable saved Rockbox/Stock routing.
  - Centre wake, long-Centre Now Playing context, and improved Back/Database

navigation.
  - PictureFlow cache recovery and a functional album carousel.

## Physical qualification

The exact firmware passed separate end-to-end macOS and Windows updater routes, each beginning from freshly restored official Stock 3.1.7. Both routes wrote only UBOOT, BOOTIMG, RECOVERY, LOGO, and ANDROID and completed mandatory five-range readback verification.

After the required complete unplug and one unplugged pinhole reset, the full functional matrix passed on both platforms: clean 28-second Rockbox boot, playback, controls, seeking, track navigation, screen and power sleep/wake, USB lifecycle, Stock, Boot Settings, saved routes, and shutdown.

## Required post-flash reset

After verified completion, unplug the Y2 completely, power it off if necessary, and press/release the pinhole once while unplugged before normal boot. The updater-attached automatic boot can inherit temporary loader/display state and is not the qualified first boot.

## Withdrawn routes

Do not use or recreate `rom_y2.zip`, the old `InnioasisUpdater_Setup_1.1.2.exe`, or an earlier Beta V2 ZIP. The legacy name enters an unqualified generic full-install path. Public delivery requires the reviewed fail-closed Y2 Class A route and the exact platform assets above.

## Known limitation and Beta V3

The final power-down animation can look imperfect; shutdown itself works. Beta V3 priorities include that polish, lyrics and 480x360 theme diagnostics, high-resolution FLAC stability, DAC and wired-audio qualification, PictureFlow polish, and database/playlist presentation controls. FM remains gated on a Y2 vendor baseline with a demonstrably working tuner.

Device-unique readbacks and raw physical-test logs remain private. Public summaries omit device identifiers and protected partition hashes.

These are Rockbox-Y2's own instructions, shown here word for word.

Published by the [spycemagic/y2-rockbox](https://innioasis.app/firmware.html?model=Y2&software=rockbox-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=spycemagic%2Fy2-rockbox&software=rockbox-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aspycemagic)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
