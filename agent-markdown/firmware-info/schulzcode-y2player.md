---
title: "About Y2Player (Y2) - README.md - Innioasis Updater"
description: "A Y2 custom Software."
language: "en"
source: "https://innioasis.app/firmware-info/schulzcode-y2player.html"
---

# About Y2Player (Y2) - README.md - Innioasis Updater

[← Firmware Downloads](../firmware.html)

Firmware README · Y2

# About Y2Player

A Y2 custom Software.

Also known as: README.md · schulzcode/Y2Player · Y2Player · schulzcode-y2playerY2[Open the Y2Player guide](../guides/y2player-y2.html)[Install with Updater CE](../firmware.html?model=Y2&software=y2player-y2)[Why Y2Player?](../y2player-benefits.html)Downloads from Firmware Archive1,880

# Y2Player

Y2Player 2.3 is an offline music player and HOME launcher built specifically for the Innioasis Y2. It turns the Android 4.4 device into a focused, click-wheel-driven music player with local library browsing, a persistent playback queue, album artwork, Bluetooth audio, and a compact interface designed for the Y2's 480 × 360 landscape display.

Y2Player is for Y2 owners, firmware modders, and contributors who want a lightweight music-first replacement for the stock launcher. It works without an internet connection and does not include streaming, search, video, or cloud services.

## Project status and bug reports

Y2Player is my first Android app. Although I test each release, the app will likely contain bugs, device-specific issues, or edge cases that I have not found yet.

If you encounter a problem, please:
  - note what you were doing when the issue occurred and whether it can be reproduced;
  - export the diagnostics log from Y2Player as soon as possible;
  - open a [GitHub issue](https://github.com/SchulzCode/Y2Player/issues) and attach the diagnostics log together with your Y2Player version, firmware version, and a short description of the problem.

The diagnostics log is especially helpful because many playback, audio-effect, Bluetooth, storage, and firmware-related problems cannot be reproduced reliably on another device. Please review the exported file before posting it publicly.

## Highlights
  - Browse local music by Songs, Albums, Artists, Genres, Years, Folders, Playlists, Favorites, and Recently Played.
  - Keep your place in Audiobooks, which are grouped by folder and resume at the minute you stopped.
  - Decode every advertised format through one pinned FFmpeg engine, including MP3, AAC/M4A/M4B, ALAC/M4A/M4B, FLAC, WAV/PCM, AIFF/PCM, Ogg Vorbis, and Opus.
  - Play individual tracks, selected batches, or complete collections and manage an explicit Up Next queue with Play Next, reordering, and removal.
  - Use repeat-one/repeat-all, configurable seeking, playback resume, gapless transitions, crossfade, and resume fades.
  - Set a sleep timer for 15, 30, or 60 minutes, or stop at the end of the current track, album, or queue.
  - Navigate entirely with the Y2 click wheel and hardware buttons.
  - Choose between the original dark interface and a light theme, and adjust left/right audio balance independently of firmware effects.
  - View embedded or external album artwork in library menus and on Now Playing alongside metadata, progress, output status, and playback controls.
  - Scan internal storage and removable SD cards, including M3U/M3U8 playlist import and export.
  - Pair and manage Bluetooth A2DP audio devices.

## Version 2.3

Version 2.3 makes the upcoming playback order explicit, expands library browsing, and adds bounded album-art thumbnails throughout the menu system.

The release includes:
  - a rebuilt queue that keeps deliberate Up Next entries ahead of the remaining album, playlist, or shuffled collection;
  - queue rows that show the real upcoming order under Shuffle, with wheel-friendly Play Now, Play Next, Move, and Remove actions;
  - batch queue actions for albums, collections, and manually selected groups of songs;
  - new Genres and Years views with matching track, artist, and album navigation;
  - independent track, album, and year-list sorting, including chronological album order;
  - album-art thumbnails for visible song, album, artist, genre, year, playlist, audiobook, and queue rows;
  - audiobook chapters removed from ordinary music views while remaining available in the dedicated Audiobooks section;
  - correct parsing of repeated Vorbis `ARTIST` values exposed by FFmpeg as semicolon-separated metadata;
  - internal model, diagnostics, playback, queue, and controller cleanup with the complete unit-test suite passing.

The complete release write-up is available in [`docs/Y2PLAYER_V2_3_RELEASE_POST.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2FY2Player%2Fblob%2FHEAD%2Fdocs%2FY2PLAYER_V2_3_RELEASE_POST.md). The shorter [Reddit release post](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2FY2Player%2Fblob%2FHEAD%2Fdocs%2FY2PLAYER_V2_3_REDDIT_POST.md) is also kept in the repository.

## Version 2.2.1

Version 2.2.1 improves playback and volume stability, particularly while the screen is locked, and refines navigation and the Now Playing interface.

The release includes:
  - corrected volume ownership and mode transitions to prevent brief output peaks;
  - reliable held and screen-off volume control through an updated firmware key layout;
  - improved paused-session lifetime and shuffle-queue progression;
  - consistent Previous and Next behavior for Left and Right across every menu;
  - wheel acceleration, optional list wrapping, and clearer active-state indicators;
  - a redesigned Now Playing footer and animated circular playback-options menu;
  - improved metadata layout, text scrolling, album labels, and audiobook ordering.

## Version 2.2

Version 2.2 adds audiobook support and rebuilds the menu structure around the four rows the display shows at once.

The release includes:
  - audiobooks on the main menu, grouped by folder, resuming at the saved position inside a chapter rather than at its start;
  - a chapter list, Start from Beginning, and a confirmed Clear Progress for every book;
  - 47 vector row icons drawn as strokes with no per-frame allocation;
  - a reorganised main menu, Music section, and Settings tree;
  - menus ordered by how often each entry is opened, with reference screens such as About at the bottom;
  - confirmation prompts on all six irreversible actions, including Delete Playlist, Clear History, and Clear Queue;
  - featured artists as their own entries, and albums that no longer lose tracks when browsed by artist;
  - a Shuffle row on album track lists, matching every other collection;
  - a repository-wide comment cleanup verified to leave the compiled behaviour unchanged.

The complete technical release write-up is available in [`docs/Y2PLAYER_V2_2_RELEASE_POST.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2FY2Player%2Fblob%2FHEAD%2Fdocs%2FY2PLAYER_V2_2_RELEASE_POST.md).

Version 2.1 improved the library scanner and refined the FFmpeg media engine using measurements collected directly on physical Y2 hardware, including a collation-correct SQLite index that made the largest measured scanner lookup 98.4% faster on a synthetic 9,178-file library.

See [CHANGELOG.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2FY2Player%2Fblob%2FHEAD%2FCHANGELOG.md) for the complete release history.

## Music library and playback

The library is built from audio files on the Y2's internal music storage and removable SD card. FFmpeg is the sole metadata backend as well as the playback engine; metadata is stored locally in SQLite, and incremental rescans extract metadata only for new or changed files. Scans inspect bounded container data without opening a decoder, while embedded artwork is extracted and downsampled only when requested.

Scanning runs on a dedicated background worker, reports visible progress, and holds a scan-only partial wake lock so a long index is not interrupted when the screen turns off. The lock is released when scanning completes. The 2.1 database index and larger bounded batches reduce the dominant large-library lookup by 98.4%; an unchanged synthetic 9,178-file library measured 19.070 seconds instead of 42.106 seconds on the physical device.

Library views include:
  - all songs, albums, artists, and folders;
  - Favorites and Recently Played smart lists;
  - user-created playlists;
  - M3U and M3U8 playlist import/export, including relocation of portable Windows, macOS, and Linux paths;
  - configurable title, artist, album, recently-added, or file-modified sorting where applicable.

Playback includes a persistent queue, shuffle, repeat one/all, previous/next behavior, short and held seeking, saved resume position, audio-focus handling, and safe pause when storage or a protected audio route disappears. Shuffle All plays one complete randomized pass of the library, then automatically creates a fresh pass. Gapless playback preloads the next track; configurable crossfade takes priority when enabled.

## Controls

| Control | Library and menus | Now Playing |
| --- | --- | --- |
| Wheel counterclockwise / clockwise | Move focus up / down | Adjust volume |
| Center | Open or confirm | Play / pause |
| Hold Center | Open contextual track options | Open playback options |
| Left / Right | Back / open contextual destination | Previous / next track |
| Hold Left / Right | — | Seek backward / forward repeatedly |
| Back button | Return to the previous screen | Return to the previous screen |
| Play button | Play / pause | Play / pause |
| Volume Up / Down | Adjust the configured system or in-app volume | Adjust the configured system or in-app volume |

### Screen-off and lock behavior

When the display is off or Android's keyguard is locked, Y2Player blocks the device's click wheel, navigation buttons, and local Play button by default. Power, Volume, and genuine Bluetooth headset controls remain active. The optional Wheel When Screen Off setting also keeps the local controls active, at the cost of allowing accidental pocket presses. Playback itself continues with the display off.

## Interface and artwork

The main interface is a low-overhead custom-drawn view sized around the Y2's landscape panel and physical focus navigation. Home keeps four primary destinations: Music, Shuffle All, Audio, and Settings. Music contains the library views; Audio groups Playback and Sound; Settings contains Bluetooth and separates Interface, Library, and System preferences. Now Playing shows embedded artwork when available, a fallback graphic otherwise, title/artist/album information, progress and time, playback state, output-route warnings, and cautious DAC information.

### ScreenshotsY2Player library screenY2Player Now Playing screen

| Library | Now Playing |
| --- | --- |

## Bluetooth audio

Y2Player integrates with Android 4.4's Bluetooth A2DP and legacy remote-control APIs. The in-app Bluetooth screen can enable Bluetooth, discover audio devices, pair, connect/disconnect, forget bonds, and refresh the A2DP service.

Transport buttons and AVRCP metadata are supported through the API 19 media-button and remote-control interfaces. Losing an active Bluetooth route pauses playback rather than leaking audio to the speaker; reconnecting requires an explicit Play command.

## Audio quality and sound effects

ReplayGain is available under Playback in three modes:
  - Album Gain preserves the intended loudness differences within an album;
  - Track Gain normalizes each track independently;
  - Track Gain while shuffling uses Album Gain in normal queue order and Track Gain while shuffle is active.

Y2Player reads the standard track/album gain and peak tags exported by FFmpeg. If the selected gain is missing, it falls back to the other tagged gain; if neither is present, that track plays unchanged. Matching peak tags cap positive gain where possible. Audio remains float32 through ReplayGain, balance, fades, ducking, and crossfade, then clips and quantizes once at the final PCM16 AudioTrack boundary. Y2Player does not calculate ReplayGain itself, so untagged files must be analyzed and tagged by another tool. Files without peak tags cannot receive metadata-based clipping prevention.

Two output preferences are available:
  - Balanced uses the normal Android audio path and can enable supported app-session effects.
  - Direct DAC (experimental) records the requested profile but currently falls back explicitly to the same standard AudioTrack output. It is not a mixer-bypass or direct PCM path.

Equalizer presets, custom equalizer bands, bass boost, and loudness appear only when Android reports compatible effects for the playback session. Availability and behavior therefore depend on the installed firmware.

The generated 2.1 firmware contains an audited, guarded primary-audio HAL hook for the recovered 44.1/48 kHz CS43131 frequency command. This is controlled groundwork only: Y2Player still renders 44.1 kHz stereo PCM16 through AudioTrack, AudioFlinger, the MediaTek audio HAL, and the kernel driver. Direct DAC is not a bit-perfect, high-resolution, native-DSD, or Android-mixer-bypass guarantee.

## Storage, diagnostics, and recovery
  - Scans common Y2 internal-storage and removable-SD mount points and retains metadata when a volume is temporarily unavailable.
  - Reacts safely to Android mount, unmount, and media-scanner events. USB/storage status is diagnostic and read-only; Y2Player does not switch USB modes.
  - Provides manual library rescanning, bounded structured logs, confirmed diagnostic clearing, local diagnostic export, and a build-derived report of the native decoder and output capabilities.
  - Provides a manual, versioned Backup & Restore file on the removable card (or the existing writable Y2Player export location).
  - Supports standard Linux `adb` tools for device installation and live diagnostics.
  - Enters Safe Mode after repeated incomplete launcher starts, or on request. Safe Mode suppresses automatic scanning, Bluetooth management, and session restoration so the UI can recover.

### Backup contents

The backup includes Y2Player interface, playback, volume, audio-effect and control settings; favorites; Y2Player-created playlists and their track order; audiobook progress; recently-played timestamps and counts; the saved queue/session; and the bounded listening-history file. Media references use normalized storage-volume and relative-path identities so they can be reconciled after a rescan changes database IDs or an SD card is mounted under a different alias.

It intentionally excludes the scanned library/metadata database, scanner-owned M3U playlists, artwork and temporary caches, diagnostics, APK/native files, database recovery copies, media files, safe-mode crash counters, and Android-owned settings. Card M3U files remain authoritative and are preserved while user-created playlists are restored transactionally.

## Privacy and offline operation

Y2Player has no `INTERNET` permission. Music, metadata, preferences, playlists, playback state, artwork, and diagnostics stay on the device. There is no account, analytics SDK, telemetry service, cloud library, or automatic upload. Exported diagnostics are files created locally for the user to inspect or copy.

## Compatibility````

| Item | Support |
| --- | --- |
| Primary device | Innioasis Y2, MediaTek MT6582 family |
| Display target | 480 × 360 landscape |
| Android | Android 4.4.2 / API 19 (minSdk and targetSdk 19) |
| Navigation | Y2 click wheel and physical buttons |
| Storage | Internal music storage and removable SD card |
| Network | Not required; the app has no internet permission |

Every playable format uses the same pinned FFmpeg engine. The scanner, playback engine, and capabilities screen share one support contract:````````````````````````````

| Extensions | Container / codec | Status |
| --- | --- | --- |
| .mp3 | MP3 | Playable |
| .aac | ADTS AAC-LC | Playable |
| .m4a, .m4b, .m4r | AAC-LC or ALAC in MOV/MP4 | Playable |
| .flac | FLAC | Playable |
| .wav, .wave | Allowlisted integer/float PCM | Playable |
| .ogg, .oga | Vorbis or Opus | Playable |
| .opus | Opus | Playable |
| .aif, .aiff, .aifc | Allowlisted AIFF PCM | Playable |
| A-law WAV | G.711 A-law | Indexed, decoder not included |
| WMA, APE, MP2, AMR, WavPack, AC-3, MKA | Various | Not enabled |

The precise codec and container policy is maintained in [docs/FORMAT_SUPPORT_MATRIX.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2FY2Player%2Fblob%2FHEAD%2Fdocs%2FFORMAT_SUPPORT_MATRIX.md). A recognized extension alone does not make a malformed or unsupported variant playable.

## Build the app

### Requirements
  - JDK 17 or newer;
  - Android SDK Platform 36 and Android Build Tools;
  - an SDK path in `local.properties` (see `local.properties.example`);
  - Linux with `bash`, `make`, `unzip`, `patch`, `curl`, and `sha256sum`;
  - Internet access for the first verified native bootstrap; later builds use the cache.

Build the pinned API-19 ARMv7 runtime, then test, lint, and package a debug APK:`./tools/build-linux.sh native ./tools/build-linux.sh app`

The APK is written to:`app/build/outputs/apk/debug/app-debug.apk`

The maintained build and firmware toolchain targets Linux.

### Build a signed release APK

Copy `keystore.properties.example` to `keystore.properties`, create and back up a release keystore, and replace every example value with your own path and credentials. Android 4.4 requires the v1/JAR signature produced by the configured release build.

Then run:`./tools/build-linux.sh release`

The verified APK and checksum are staged under `dist/firmware/`. Signing material and generated release artifacts are intentionally ignored by Git.

### Build the secure ADB development image

The optional ADB pipeline is separate from the release `system.img` pipeline. It builds a static API-19 ARM `adbd` from pinned official Android 4.4.2 sources and inserts it into a verified copy of the stock MediaTek boot image. The result keeps USB mass storage, RSA authorization, a non-root shell, and the production security properties.`./tools/build-linux.sh adb-boot`

Outputs and verification reports are written to `out/boot-adb/`. This image is for development and requires its own BOOTIMG-only flashing procedure; it is not generated or flashed by the normal firmware build. Read [docs/ADB_BOOT_IMAGE.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2FY2Player%2Fblob%2FHEAD%2Fdocs%2FADB_BOOT_IMAGE.md) before using it.

## Install on a device

### Flash the modified system image with SP Flash Tool

[!WARNING] Flashing modified firmware can permanently damage or brick your device if the wrong file, partition, or flashing mode is selected. Proceed entirely at your own risk. I am not responsible for damaged devices, lost data, failed flashes, or any other consequences.

Read this entire guide carefully before starting. Do not continue until you understand every step. Work slowly, verify every selection, and never guess.

#### Downloads
  - [SP Flash Tool](https://spflashtool.com/)
  - MediaTek Driver 
  - [Original Y2 stock firmware 3.1.7](https://innioasis.app/release_notes.html?author=y1-community&project=y1-stock-rom&version=3.1.7&software=original-y1)

#### Requirements
  - an Innioasis Y2 with the matching stock firmware version;
  - the modified `system.img` from the Y2Player GitHub Release;
  - the matching original `MT6582_Android_scatter.txt` file from the [original Y2 stock firmware](https://innioasis.app/release_notes.html?author=y1-community&project=y1-stock-rom&version=3.1.7&software=original-y1);
  - [SP Flash Tool](https://spflashtool.com/);
  - the required MediaTek USB drivers;
  - a verified copy of the complete original firmware so the device can be restored if necessary.

#### Before flashing
  - Back up any important files from the Y2.
  - Keep the complete original firmware and matching scatter file in a safe location.
  - Confirm that the downloaded release is intended for the Innioasis Y2 and your firmware base.
  - Verify the SHA-256 checksum supplied with the release.
  - Fully charge the Y2 before beginning.
  - Read all remaining steps before opening SP Flash Tool.

The current image retains Android's `Provision.apk`, and Y2Player deliberately does not outrank the provisioning activity during a blank-userdata first boot. A device whose `userdata` was previously reset can therefore complete initial provisioning directly with Y2Player installed; booting the stock launcher first is no longer required. For an ordinary upgrade, leave `userdata` untouched and flash only `system.img` as described below.

#### Flashing steps
  - Extract the Y2Player release ZIP.
  - Install the MediaTek Driver MediaTek Driver
  - Open [SP Flash Tool](https://spflashtool.com/).
  - Load the matching original `MT6582_Android_scatter.txt` file.
  - Select Download Only from the flashing-mode menu.
  - Remove every partition checkmark.
  - Enable only the `ANDROID` partition.
  - In the `ANDROID` row, select the modified Y2Player `system.img`.
  - Carefully verify the configuration before continuing:
    - mode is Download Only;
    - only `ANDROID` is checked;
    - `ANDROID` points to the modified Y2Player `system.img`;
    - no other partition is selected.

  - Turn the Y2 completely off.
  - Click Download in SP Flash Tool.
  - Connect the powered-off Y2 to the computer with a reliable USB data cable.
  - Wait until SP Flash Tool displays the green success indicator.
  - Disconnect the USB cable and start the Y2.
  - Allow extra time for the first boot.

#### Never select these partitions

Do not flash or format any unrelated partition, including:`PRELOADER MBR EBR1 EBR2 UBOOT BOOTIMG RECOVERY SEC_RO LOGO CACHE USRDATA NVRAM`

Do not use Format All + Download or Firmware Upgrade. For this installation, use Download Only and flash only `ANDROID`.

SP Flash Tool configured to flash only the ANDROID partition

SP Flash Tool configured with only the ANDROID partition selected.

#### Restoring the original firmware

If the modified system does not boot or function correctly:
  - Turn the device off.
  - Open SP Flash Tool.
  - Load the matching original scatter file.
  - Select Download Only.
  - Select only the original `ANDROID` partition and original `system.img`.
  - Flash it using the same careful procedure described above.

Do not restore additional partitions unless a verified device-specific recovery guide explicitly requires them.

### Build the system image yourself

The repository can also build a minimized, system-partition-only image from your own matching stock firmware. It replaces the stock launcher with the signed APK at `/system/priv-app/Y2Player.apk`, installs the byte-identical Android 4.4 runtime at `/system/lib/liby2audio.so`, applies the exact-hash-guarded primary-audio HAL frequency-hook patch described above, and prunes 35 standalone media, utility, wallpaper, phone-UI, and engineering packages that are not used by the player appliance.

The package policy is intentionally conservative. Provisioning, Settings, SystemUI, Keyguard, storage/media providers, Bluetooth, input, package-management, thermal/battery, and underlying framework services remain in the image. Both the integrator and independent verifier use the same policy: optional APK/ODEX files must be absent, critical APKs must be present, and freed ext4 blocks must be zero before sparse repacking.

Provide:`OriginalFirmware/system.img OriginalFirmware/MT6582_Android_scatter.txt`

Validate the host environment without producing an image:`./tools/build-linux.sh firmware-validate`

Build and verify the release APK and replacement system image:`./tools/build-linux.sh system-image`

This requires Python 3 and Linux `e2fsprogs` in addition to the Android build requirements. Successful outputs are written to `out/firmware/`, including `Y2Player.apk`, `system.img`, checksums, a manifest, and an independent verification report. The verifier reopens the sparse image and checks the embedded APK, native runtime, patched HAL, package-pruning policy, retained critical packages, ext4 structure, partition size, ownership, modes, SELinux labels, uniqueness, and SHA-256 readback.

The build script only creates files. It never flashes, pushes, reboots, emits a boot image, or modifies the original firmware inputs.

### Build an Innioasis Updater release

To create the complete release archive accepted by the [Innioasis Updater](https://github.com/y1-community/Innioasis-Updater), run:`./tools/build-linux.sh firmware`

This single command first runs the Linux system-image pipeline, so the signed APK and `system.img` are always rebuilt from the current source. It then combines the new system image with the guarded stock Y2 partition set, converts the filesystem images to raw form, adds the portable flashing tool, and produces a maximum-Deflate flat archive at `out/updater/rom_y2.zip`. The known-good flashing-tool template is downloaded and SHA-256 verified on the first run, then kept under `build/downloads/` for subsequent releases. The underlying `tools/firmware/build_full_package.py` command also accepts `--template` for an offline copy.

The output directory contains:`rom_y2.zip checksums.txt build-manifest.txt verification-report.txt`

Upload `rom_y2.zip` to the GitHub release without renaming it. The updater only recognizes the Y2 package under that exact name. The script never uploads or flashes anything itself.

[!WARNING] `rom_y2.zip` is a full-device ROM package and its installation erases user data. The separate sparse `out/firmware/system.img` remains available for the existing system-only SP Flash Tool update procedure.

Validate all local ROM inputs and tools without building or downloading the template:`./tools/build-linux.sh firmware-validate`

## Known limitations
  - Y2Player is designed for the Innioasis Y2 and is not presented as a general-purpose Android player or launcher.
  - Decoder and container support is the pinned FFmpeg allowlist above; malformed or unsupported content can still fail despite a recognized extension.
  - An unchanged-library scan still traverses directories, stats files, updates scan-generation state, and reloads the index. Avoiding that work safely requires a larger change-detection design.
  - Bluetooth on stock KitKat is limited by the firmware stack: typically SBC A2DP, one sink at a time, no BLE Audio, and no synchronized absolute volume. Some connection-management operations depend on hidden OEM APIs and may require Android Settings.
  - Bluetooth discovery can briefly degrade active A2DP audio on older hardware.
  - The Direct DAC preference still uses standard 44.1 kHz stereo PCM16 AudioTrack output. The guarded HAL frequency hook is groundwork and does not enable bit-perfect playback, native DSD, high-rate PCM, or an Android-mixer bypass.
  - Equalizer, bass boost, loudness, haptics, storage aliases, route reporting, and final audio-output behavior are hardware/firmware dependent.
  - The firmware pipeline requires the correct stock Y2 `system.img` and scatter file; these proprietary inputs are not generated by the project.
  - Prebuilt system images are firmware-specific and must only be flashed on the supported Innioasis Y2 firmware base identified by the release.

## Contributing

Contributions should preserve Android 4.4/API 19 compatibility, physical-control navigation, offline operation, and the project's small CPU/heap footprint. Before submitting a change, run:`./tools/build-linux.sh app`

Hardware-dependent changes should describe the Y2 firmware version and include diagnostic evidence where possible.

## License

Y2Player is available under the [MIT License](https://github.com/schulzcode/Y2Player/blob/HEAD/LICENSE). Copyright © 2026 Luca Schulz.

## Community skins

Y2Player includes three file-driven version 2 skins: Neon Grid, Pixel Garden, and Studio Deck. Choose one under Settings → Interface → Display → Skin. Custom skin folders go in `Y2Player/Skins` on readable internal storage or SD card; use Reload Skins after editing. Classic remains available as a fallback. See the [skin authoring guide](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2FY2Player%2Fblob%2FHEAD%2Fapp%2Fsrc%2Fmain%2Fassets%2Fskins%2FREADME.md), [version 2 reference](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2FY2Player%2Fblob%2FHEAD%2Fdocs%2Fskins%2FFORMAT_V2.md), and [Neon Grid example](https://github.com/schulzcode/Y2Player/blob/HEAD/app/src/main/assets/skins/neon-grid/skin.json).

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
