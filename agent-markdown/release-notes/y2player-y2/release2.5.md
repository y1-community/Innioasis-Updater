---
title: "Y2Player V2.5 - Innioasis Updater"
description: "Y2Player v2.5 - Search, FM Radio, Faster Navigation, and Playback Reliability Version 2.5 brings whole-device search, FM radio support for compatible Y2 hardware, faster navigation"
language: "en"
source: "https://innioasis.app/release-notes/y2player-y2/release2.5.html"
---

# Y2Player V2.5 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=y2player-y2)

Firmware release notes · Y2Player · Y2

# Y2Player V2.5

A Y2 custom Software.Release2.5Y22026-09-04[schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=y2player-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=y2player-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

rom_y2.zip[rom_y2.zip 283 MB](https://github.com/SchulzCode/Y2Player/releases/download/Release2.5/rom_y2.zip)

# Y2Player v2.5 - Search, FM Radio, Faster Navigation, and Playback Reliability

Version 2.5 brings whole-device search, FM radio support for compatible Y2 hardware, faster navigation through large libraries, more flexible sleep-timer controls, and a redesigned equalizer interface.

This release also addresses several reported problems involving screen-off playback, shuffle ordering, audiobook seeking, queue controls, embedded artwork, list wrapping, and general navigation.

## Whole-Device Search

Search is now available directly from the main menu.

The new wheel-driven QWERTY keyboard searches across:
  - Songs
  - Albums
  - Artists
  - Playlists
  - Audiobooks

Track searches include title, artist, album, filename, genre, and composer metadata. Matching is accent-insensitive and supports multiple search terms, with exact and prefix matches ranked first.

Search results reuse the existing playback and browsing flows. Tracks can be played or opened through their context menus, while albums, artists, playlists, and audiobooks open their corresponding library views.

The interface was designed for the Y2’s 480 × 360 display:
  - The keyboard remains visible at the bottom of the screen.
  - Two complete result rows remain visible above it.
  - The wheel moves through keys in QWERTY order.
  - Left and Right move within the current keyboard row.
  - Center enters the selected key.
  - Back deletes the previous character.
  - The Results key moves focus to the matching items.
  - Direct touch works on both keyboard keys and results.
  - Playback controls are suppressed while typing to prevent accidental track changes.

Search also has separate instructions before typing and a dedicated message when no results are found.

To keep it responsive with large libraries, searchable metadata is indexed once per active library. Recent queries are cached, and only the best 100 results are retained. In a synthetic 10,000-track benchmark, ordinary indexed queries completed in approximately 2–5 ms, while cached queries completed in approximately 0.02 ms.

## FM Radio

Y2Player now includes support for the MediaTek MT6627 FM tuner found in newer FM-equipped Y2 hardware revisions.

The FM Radio interface supports:
  - Wheel-controlled frequency tuning
  - Previous and next station seeking
  - Frequency and signal information
  - Wired-headphone antenna detection
  - Tuner power control
  - Safe switching between music playback and FM audio
  - Proper tuner cleanup when leaving the FM screen

### Important Y2 Hardware Notice

Innioasis has confirmed that there are two Y2 hardware revisions.

The original Y2 batch does not contain the required FM radio hardware. These devices may be able to open the FM interface and tune frequencies, but they cannot receive a usable radio signal and will normally output only static.

Newer Y2 units include the required FM circuitry and use the FM-enabled stock firmware.

Because many existing Y2 devices cannot receive FM, the FM Radio entry is hidden by default. Owners of compatible newer hardware can enable it under:

Settings → Interface → FM Radio

Flashing FM-enabled stock firmware cannot add the missing tuner circuitry to an original Y2. FM reception depends on the physical hardware revision, not only the installed firmware.

## Faster Alphabet Navigation

Large alphabetically sorted libraries now support iPod-style alphabet scrolling.

Normal and moderately fast wheel movement retain the existing precise scrolling behavior. Sustained fast movement activates an alphabet scrub mode with a large temporary `#` or `A–Z` overlay.

Alphabet scrolling is available where the visible order is genuinely alphabetical, including supported:
  - Song lists
  - Favorites
  - Artists
  - Albums sorted by title
  - Playlists
  - Filtered library views

It remains disabled for album track order, Recently Played, chronologically sorted albums, Queue, folders, settings, confirmation screens, and circular menus.

The first position for each letter is indexed once per visible list, so moving through a large library does not repeatedly scan every row.

## Improved Sleep Timer

The sleep timer now opens a dedicated wheel-controlled selection screen instead of cycling through a small number of presets.

Available choices include:
  - Off
  - End of track
  - End of album
  - End of queue
  - Every exact duration from 1 through 60 minutes

Reopening the Sleep Timer screen returns to the currently selected option.

Active minute timers now show a live remaining-time countdown throughout the interface. Expired timers are cleared correctly instead of remaining visibly enabled after playback stops.

End of Album and End of Queue follow the active playback collection and queue rather than using an approximate duration.

## More Reliable Screen-Off Playback

Y2Player now holds a service-level playback wake lock throughout Preparing and Playing.

Previously, the decoder-level wake lock could be released during the brief asynchronous handoff between one completed track and the next. If the display was asleep at that exact moment, Android could suspend the CPU before the service completed the transition.

The new ownership closes that gap while still releasing the wake lock when playback is:
  - Paused
  - Idle
  - Stopped
  - In an error state
  - Shutting down

This fixes playback potentially stopping at the end of a track until the screen was turned back on.

## Optional Seeking While Locked

A new option allows the Y2’s Left and Right buttons to seek while the device is locked instead of changing tracks or audiobook chapters.

It can be enabled under:

Settings → Audio → Seeking → Seek When Locked

When enabled, Left and Right use the configured held-seek interval. The option is disabled by default, and headset or Bluetooth transport controls retain their normal behavior.

## Wake-Up Seek Fix

A separate input-routing fix prevents a held seek button from being interpreted as multiple Previous or Next commands when the display wakes.

When the unlocked activity is visible, it now has exclusive ownership of local keypad gestures. The vendor broadcast remains available as a screen-off fallback, while genuine headset and Bluetooth media commands remain unaffected.

This is particularly useful for audiobooks, where an interrupted seek could previously skip several chapters.

## Correct Playback Order After Disabling Shuffle

Disabling Shuffle now rebuilds the ordered continuation around the currently playing track.

Previously, turning Shuffle off after progressing through a playlist could restart or incorrectly arrange the remaining ordered playback.

The corrected behavior:
  - Keeps the current track active.
  - Restores the remaining playlist or collection order.
  - Preserves deliberately added Up Next tracks.
  - Keeps those Up Next entries ahead of the restored continuation.
  - Handles the final track and progressed shuffle sessions correctly.

## Queue Control Fixes

Center-button behavior in Queue now matches other track lists.

A short Center press opens the selected queue entry’s action menu. Holding Center uses the corresponding long-press behavior without accidentally performing both actions.

This removes inconsistent behavior where Queue treated Center differently from Songs and other track views.

## Redesigned Equalizer Controls

Equalizer configuration has been redesigned around explicit wheel-controlled selection screens.

Preset selection now displays a complete list instead of cycling blindly through available presets. The list includes Custom whenever individual band values are active.

Selecting an equalizer band opens a dedicated dB value screen:
  - The current value is preselected.
  - Values use valid 1 dB steps within the range reported by the device.
  - Exact minimum and maximum values remain available.
  - Center applies the selected value and returns.
  - Back cancels without changing the band.
  - Left and Right retain their normal global playback behavior.

This replaces the previous short-press and long-press band adjustment system, making the current and resulting values much clearer.

## Consistent List Wrapping

The Wrap Lists preference is now respected across all selectable screens.

It applies consistently to:
  - Library lists
  - Settings
  - Confirmation choices
  - Equalizer selectors
  - Circular action menus
  - Search keyboard navigation

When Wrap Lists is disabled, selection stops at the beginning and end. When enabled, selection continues from the final item to the first and vice versa.

Queue reordering remains intentionally bounded because that screen edits a target position rather than navigating an ordinary menu.

## Improved Back Navigation

Holding the Y2’s top Back button now returns directly to the main menu, matching classic iPod behavior.
  - A short press returns one screen.
  - A held press clears the navigation stack and returns home.
  - Hold detection works with normal Android key repeats.
  - Release-based detection also supports firmware that does not emit repeat events.
  - The short Back action is suppressed after a recognized hold.

Back also dismisses temporary alerts and status messages before navigating away. A second press performs the normal Back action.

Persistent library, playback, Bluetooth, and diagnostic status information is not intercepted.

## Artist Navigation Fix

Track Options → Browse Track → Go to Artist now opens the selected artist’s album list.

Previously, this route bypassed the normal artist view and opened a flat list containing every song by that artist.

The corrected behavior now matches:

Music → Artists → Artist Albums

Go to Album and existing featured-artist normalization remain unchanged.

## Safer Embedded Artwork

Oversized or malformed embedded artwork is now rejected safely.

Previously, invalid artwork data could trigger an exception while constructing the artwork byte array and potentially crash Y2Player.

The native metadata bridge now:
  - Enforces the configured artwork-size limit before allocation.
  - Detects JNI allocation failures.
  - Clears the resulting exception safely.
  - Returns no artwork instead of bringing down the application.

Valid embedded and external artwork behavior is unchanged.

## Cleaner Now Playing Footer

The permanent transition-mode item and its divider have been removed from the Now Playing footer.

Shuffle and Repeat remain on the left, while queue position remains right-aligned. This gives the footer a more balanced layout and removes information that did not need to remain visible continuously.

This is only a presentation change. Gapless playback, Crossfade, Crossfade Mode, their settings, and their playback behavior remain available.

## USB Connection Feedback

Connecting USB now produces a single perceptible haptic response when haptics are enabled and supported by the device.

The implementation uses the existing coalesced USB state instead of reacting independently to every Android power and USB broadcast.

The following do not cause duplicate vibrations:
  - Initial USB state detection
  - Repeated connected-state broadcasts
  - Power-state refreshes
  - Disconnecting the cable

## Settings and Backup Compatibility

The following new preferences are included in Backup & Restore:
  - FM Radio main-menu visibility
  - Seek When Locked

Older backups remain compatible and receive safe defaults:
  - FM Radio is hidden.
  - Seek When Locked is disabled.

## Validation

Version 2.5 has been checked with the complete debug unit-test suite and Android lint.

The latest validation completed successfully with more than 930 unit tests covering navigation, Search, FM state, playback, queue behavior, sleep timers, input routing, artwork, preferences, and backup compatibility.

## Installation

The release provides the existing system-only update path as well as a complete `rom_y2.zip` package for the Innioasis Updater.

For the system-only method, use SP Flash Tool in Download Only mode with only the ANDROID partition selected, pointing to the supplied `system.img`.

Do not select, format, or flash unrelated partitions.

The complete `rom_y2.zip` installation performs a full-device installation and erases user data. Before using it:
  - Export a Y2Player backup.
  - Copy the backup off the device.
  - Copy any important music, playlists, diagnostics, and other files to a computer.
  - Verify the supplied package checksum.
  - Follow the installation instructions for the Y2 specifically.

Do not use a Y1 package on a Y2.

## Reporting Problems

If you encounter a problem, enable verbose diagnostics before reproducing it:

Settings → System → Diagnostics → Verbose Diagnostics

After reproducing the problem, export the report:

Settings → System → Diagnostics → Export Diagnostics

Attach the exported report to a GitHub issue and include:
  - Whether your Y2 is from the original or FM-enabled hardware batch
  - The audio format being played
  - Whether playback used the speaker, wired headphones, or Bluetooth
  - Whether Shuffle, Repeat, Crossfade, ReplayGain, or the equalizer was enabled
  - The exact screen and hardware-button sequence that produced the problem

For FM problems, also mention whether wired headphones were connected and whether FM works in the FM-enabled Innioasis stock firmware.

Thank you to everyone who submitted issues, tested builds, provided diagnostics, and helped investigate the Y2’s different hardware revisions. Your reports directly shaped the Search interface, navigation improvements, timer redesign, playback fixes, and hardware compatibility behavior in this release.

## Also useful
  - [Install guideStep-by-step install for Y2Player](../../guides/y2player-y2.html)
  - [Y2Player V2.3ReleaseV2.3 · 2026-08-15](../../release-notes/y2player-y2/releasev2.3.html)
  - [Y2Player V2.2.2RealeaseV2.2.2 · 2026-08-10](../../release-notes/y2player-y2/realeasev2.2.2.html)
  - [Y2Player V2.2.1 ReleaseV2.2.1 · 2026-08-03](../../release-notes/y2player-y2/releasev2.2.1.html)
  - [Y2Player V2.2ReleaseV2.2 · 2026-08-01](../../release-notes/y2player-y2/releasev2.2.html)
  - [Y2Player V2.1ReleaseV2.1 · 2026-07-29](../../release-notes/y2player-y2/releasev2.1.html)
  - [Y2Player 2.0 Complete Media Engine RewriteReleaseV2.0 · 2026-07-27](../../release-notes/y2player-y2/releasev2.0.html)
  - [Y2Player V1.2ReleaseV1.2 · 2026-07-26](../../release-notes/y2player-y2/releasev1.2.html)

Notes as published by the Y2Player project. Install it with Updater CE, or download it from the firmware directory.

Published by the [schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2FY2Player&software=y2player-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=Y2Player&version=Release2.5&software=y2player-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
