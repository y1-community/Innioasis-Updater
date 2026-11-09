---
title: "Y2Player V2.2.1 - Innioasis Updater"
description: "Y2Player v2.2.1 — Playback Stability, Improved Controls, and Now Playing Updates Version 2.2.1 focuses on feedback received after the 2.2 release. The largest changes address volum"
language: "en"
source: "https://innioasis.app/release-notes/y2player-y2/releasev2.2.1.html"
---

# Y2Player V2.2.1 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=y2player-y2)

Firmware release notes · Y2Player · Y2

# Y2Player V2.2.1 

A Y2 custom Software.ReleaseV2.2.1Y22026-08-03[schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=y2player-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=y2player-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

rom_y2.zip[rom_y2.zip 283 MB](https://github.com/SchulzCode/Y2Player/releases/download/ReleaseV2.2.1/rom_y2.zip)

system.img.zip[system.img.zip 215 MB](https://github.com/SchulzCode/Y2Player/releases/download/ReleaseV2.2.1/system.img.zip)

# Y2Player v2.2.1 — Playback Stability, Improved Controls, and Now Playing Updates

 Version 2.2.1 focuses on feedback received after the 2.2 release. The largest changes address volume peaks, lock-screen playback, physical controls, queue reliability, and the Now Playing interface.

## Volume and Lock-Screen Playback

 Several issues could cause the output volume to briefly jump when changing volume modes, pausing playback, locking the device, or waking the screen.

 Volume ownership has been reworked so that the player's software gain is applied before Android's system stream is changed. This prevents the system stream from becoming audible at full volume during the handover.

 The following cases have been corrected:
  - Switching between In-App and System / Hardware Keys volume modes no longer causes a brief volume peak.
    - Starting playback after changing volume mode while paused no longer produces a loud initial burst.
    - Pausing, locking, unlocking, and waking the screen no longer briefly exposes the system stream at maximum volume.
    - Volume changes made while the screen is locked are no longer overwritten when the screen turns back on.
    - In-App volume can now be raised and lowered while the screen is locked.
    - Holding a volume button continues changing the volume instead of requiring repeated individual presses.
    - Paused tracks remain loaded when the interface or screen goes away, preventing playback from unexpectedly returning to the beginning.

## Firmware Volume-Key Handling

 The firmware now contains a guarded keypad-layout patch for the Y2's physical volume buttons.

 The local volume keys are delivered directly to Y2Player instead of allowing Android to modify the system stream before the app can respond. This is particularly important for In-App volume control and screen-off operation.

 Only the Y2's physical volume scan codes are remapped. Genuine headset and Bluetooth media controls remain unchanged.

## Playback and Queue Reliability

 Paused playback is now treated as an active, resumable session. Locking the device or leaving the interface no longer unloads a paused track simply because the activity disconnected.

 Shuffle handling has also been corrected. Changing Shuffle mode now preserves the portion of the queue that has already been played and rebuilds only the remaining order. This prevents unplayed tracks from becoming stranded behind the current position and avoids reaching a false end of the shuffled queue.

 Seeking has additional endpoint protection so a seek cannot land inside an unusable final fragment of a track.

## Navigation Changes

 Left and Right now have one consistent purpose throughout the entire interface:
  - Left plays the previous track.
    - Right plays the next track.
    - Hold Left or Right seeks backward or forward.
    - Center opens the selected menu or activates the selected option.
    - Back returns to the previous menu.

 Left and Right no longer enter or leave menus. Context menus that were previously opened with Right are now opened by holding Center.

 A short Center press on the Now Playing screen no longer pauses or resumes playback. It simply keeps the display awake. The dedicated Play/Pause button remains responsible for playback.

## Main Menu Cleanup

 The duplicate Now Playing entry has been removed from the main menu because the current track is already visible in the Now Playing panel.

 When there is no active or restored playback session, the same position is used for Shuffle All. Shuffle All is hidden once a session exists so it cannot accidentally replace the current queue.

## Circular Now Playing Menu

 Holding Center on the Now Playing screen now opens a new circular playback menu over the current screen.

 The scroll wheel moves around the available controls, and a short Center press activates the selected item. Back or another long Center press closes the menu.

 The radial menu includes:
  - Shuffle
    - Repeat
    - Queue
    - Favorite
    - Sleep Timer
    - Add to Playlist
    - Track Options

 The menu blends over the Now Playing screen with a short fade and scale animation. Active options use the same accent color and visual state system as the rest of the interface.

## Now Playing Status Information

 The old button-hint footer has been replaced with useful playback information.

 The footer now displays:
  - Shuffle status
    - Repeat mode
    - Effective transition mode
    - Current queue position

 The transition indicator distinguishes between standard playback, gapless playback, and crossfade, including the configured fade duration.

## Additional Metadata Layout

 When Additional Metadata is enabled, its information is now divided into two dedicated lines:
  - Genre
    - Codec, bitrate, sample rate, and bit depth

 This prevents the metadata from being compressed into one long line and reduces clipping on the right side of the display.

 Long selected text can now scroll after a short delay instead of remaining permanently truncated. Scrolling stops while the screen is off and restarts when needed.

## Album Information

 The album line on the Now Playing screen is now always displayed when album information exists.

 Previously, the album line disappeared when an album had the same name as its artist. Artist and album are separate metadata fields, so matching names no longer cause either field to be hidden.

## Favorites and Active-State Indicators

 Favorite actions now have a clear visual state.

 Favorited tracks use a filled heart instead of continuing to display the same empty heart. Other enabled options also use consistent accent coloring, active surfaces, markers, or check indicators where appropriate.

 This makes it easier to tell whether options such as Favorite, Shuffle, Repeat, and other toggles are currently enabled.

## Scroll-Wheel Improvements

 Rapid wheel movement now accelerates through long collections such as Songs, Albums, Artists, Playlists, Queue, and Audiobooks.

 Acceleration is deliberately disabled in short settings menus so individual options remain easy to select. Slowing down or reversing direction immediately restores one-row precision.

 A new Wrap Lists option has also been added under Controls:
  - When enabled, moving past the final item returns to the first.
    - When disabled, selection stops at the beginning and end of ordinary lists.
    - Circular selectors and the new radial menu continue wrapping naturally.

## Haptic Feedback

 Haptic feedback now occurs only when an input was actually accepted.

 Pressing against the end of a non-wrapping list or performing an unavailable action no longer produces a misleading vibration. Accepted navigation and control actions still provide immediate feedback.

## Library and Browsing Fixes

 Several smaller library issues have also been corrected:
  - Artist names differing only by capitalization or surrounding spaces are now treated as the same artist.
    - Various Artists is filtered consistently regardless of capitalization.
    - Multi-disc audiobook chapters now sort by disc, folder, track number, filename, and title instead of interleaving tracks whose numbering restarts on each disc.
    - Single-track playlists no longer display a meaningless Shuffle option.
    - Library reset now waits for scanning and pending state writes before deleting and rebuilding the library.
    - User-copyable exports prefer removable storage when it is available.

### Update schedule notice

 Development of Y2Player will continue, but future updates may take a little longer to arrive. My vacation from work is now over, so I have less free time available for development and testing. I still plan to address reported issues and improve the player whenever possible, and I appreciate your patience and continued feedback.

### What’s Planned Next

 The next update is planned to focus on improvements to the queue and playback systems, alongside multi-select actions and faster library navigation with letter-based scrolling. I also want to make the scroll wheel configurable on the Now Playing screen, allowing it to control either volume or seeking. FM Radio support has already been implemented experimentally, but the device is not currently receiving a signal, so further hardware investigation is required and may take some time. Additional themes and interface options are also planned, with the goal of supporting more personal preferences without making the player bloated or unintuitive. This is one of the most challenging parts of development, as different users often prefer very different controls and layouts, so these features will need careful design and testing.

## Also useful
  - [Install guideStep-by-step install for Y2Player](../../guides/y2player-y2.html)
  - [Y2Player V2.5Release2.5 · 2026-09-04](../../release-notes/y2player-y2/release2.5.html)
  - [Y2Player V2.3ReleaseV2.3 · 2026-08-15](../../release-notes/y2player-y2/releasev2.3.html)
  - [Y2Player V2.2.2RealeaseV2.2.2 · 2026-08-10](../../release-notes/y2player-y2/realeasev2.2.2.html)
  - [Y2Player V2.2ReleaseV2.2 · 2026-08-01](../../release-notes/y2player-y2/releasev2.2.html)
  - [Y2Player V2.1ReleaseV2.1 · 2026-07-29](../../release-notes/y2player-y2/releasev2.1.html)
  - [Y2Player 2.0 Complete Media Engine RewriteReleaseV2.0 · 2026-07-27](../../release-notes/y2player-y2/releasev2.0.html)
  - [Y2Player V1.2ReleaseV1.2 · 2026-07-26](../../release-notes/y2player-y2/releasev1.2.html)

Notes as published by the Y2Player project. Install it with Updater CE, or download it from the firmware directory.

Published by the [schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2FY2Player&software=y2player-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=Y2Player&version=ReleaseV2.2.1&software=y2player-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
