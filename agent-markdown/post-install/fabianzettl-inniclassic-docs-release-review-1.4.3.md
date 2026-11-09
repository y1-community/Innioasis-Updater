---
title: "InniClassic 1.4.3 release candidate review - Innioasis Updater"
description: "InniClassic 1.4.3 release candidate review The source version is 1.4.3 143. This is a locally built, debug-signed test candidate, not a published release or a ROM image."
language: "en"
source: "https://innioasis.app/post-install/fabianzettl-inniclassic-docs-release-review-1.4.3.html"
---

# InniClassic 1.4.3 release candidate review - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y1&software=inniclassic-y1)

Post-install setup · Inniclassic · Y1

# InniClassic 1.4.3 release candidate review

A classic-style Y1 Software.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y1&software=inniclassic-y1)[Install guide](../guide.html?model=Y1&software=inniclassic-y1)

# InniClassic 1.4.3 release candidate review

The source version is 1.4.3 (143). This is a locally built, debug-signed test candidate, not a published release or a ROM image.

## Verified
  - `JAVA_HOME=/usr/lib/jvm/java-17-openjdk ./gradlew assembleDebug testDebugUnitTest lintDebug`: successful.
  - Lint: 0 errors, 463 warnings. The legacy receiver helper has one narrowly scoped suppression because API 17 has no receiver-flags overload; Android 33+ uses the explicit flags overload.
  - `SafeFilesTest`: traversal, absolute paths, sibling-prefix escape, symlink escape, invalid names, interrupted writes, replacement, empty saves and temporary-file cleanup.
  - `Y1WebServerTest`: actual socket requests for uploads, truncated bodies, traversal, root deletion, cross-origin writes, rename/readback, unknown routes and shutdown.
  - Both generated browser scripts pass `node --check`.
  - `git diff --check`: clean.
  - No device is connected to ADB. Current Android screens have not been visually inspected on hardware.

## Design basis

The checked-in screenshots were reviewed alongside the menu/status-bar description in [Apple's iPod classic guide](https://cdsassets.apple.com/live/6GJYWVAV/user/ma1195_ipod_classic_160gb_user_guide.pdf). This change is a closer interpretation, not a verified pixel-perfect reproduction. Existing Nimbus Sans regular and bold files remain; Classic row typography is centralized and the main-menu selection now uses the same gradient as other lists. Theme version migration will reinstall bundled themes on first launch of version 143.

Last.fm response handling follows the distinction between HTTP status and API responses in the [official scrobbling documentation](https://www.last.fm/api/scrobbling).

## Architecture and remaining limits

`MainActivity` remains about 17,000 lines and owns navigation, library operations, playback coordination and UI rendering. This pass extracts independently testable file operations and centralizes dynamic IDs; it does not replace the application architecture. A future incremental split should separate library indexing and navigation before moving screen controllers.

The Wi-Fi server remains an unauthenticated local-network feature and must be treated as access to the shared SD card while enabled. Canonical path checks and origin checks are not authentication. Its existing HTTP Last.fm password page remains; the device's browser-based token flow is preferable. HTTP range seeking is not implemented, and the server no longer advertises range support. Renames use same-directory temporary files for complete uploads; abrupt power loss and concurrent edits are not covered by host tests.

Other existing limitations remain: gapless playback has queue/format restrictions, native decoders and FM hardware are device-specific, album art extraction still uses background threads and static activity coupling, and the lint warnings have not all been resolved. Last.fm live authentication/submission was not tested against a real account.

## Before publishing
  - Install on a Y1 with the intended signing certificate; verify the previous release's certificate before choosing update versus uninstall. Do not uninstall merely to bypass an unknown signing mismatch, because that clears private settings.
  - Inspect Main Menu, Music, Artists, Albums, Songs, Settings and Now Playing in light and dark themes. Check long titles, accented/CJK text, focus arrows and cover reflection on the actual display.
  - Exercise wheel focus/wrap, Menu/Center/hold, Cover Flow navigation and equalizer focus after the ID migration.
  - Play MP3, FLAC, Ogg/Opus, ALAC and a short gapless album; check shuffle/repeat, resume, headphone removal, sleep/wake, Bluetooth reconnect, video sync and FM.
  - Check audiobook resume, podcasts/downloads, library rescans, Last.fm offline-to-online retries and theme upgrades with existing settings.
  - Upload a directory containing more than 100 files, interrupt an overwrite, verify the old file, and stop/restart the server.
  - Capture fresh device screenshots, finalize release notes and sign/package the approved APK. Build a ROM separately if one is to be distributed.

These are Inniclassic's own instructions, shown here word for word.

Published by the [FabianZettl/inniclassic](https://innioasis.app/firmware.html?model=Y1&software=inniclassic-y1) project [[1]](https://innioasis.app/firmware_info.html?repo=FabianZettl%2Finniclassic&software=inniclassic-y1)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3AFabianZettl)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
