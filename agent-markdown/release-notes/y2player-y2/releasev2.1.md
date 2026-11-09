---
title: "Y2Player V2.1 - Innioasis Updater"
description: "Y2Player v2.1 — Library Scanner and Media Engine Improvements Version 2.1 is the result of a much deeper development effort than previous Y2Player updates. Its main focus is faster"
language: "en"
source: "https://innioasis.app/release-notes/y2player-y2/releasev2.1.html"
---

# Y2Player V2.1 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y2&software=y2player-y2)

Firmware release notes · Y2Player · Y2

# Y2Player V2.1

A Y2 custom Software.ReleaseV2.1Y22026-07-29[schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2)[Get it in Updater CE](../../guide.html?model=Y2&software=y2player-y2)[Firmware Downloads](../../firmware.html?model=Y2&software=y2player-y2)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

system.zip[system.zip 215 MB](https://github.com/SchulzCode/Y2Player/releases/download/ReleaseV2.1/system.zip)

# Y2Player v2.1 — Library Scanner and Media Engine Improvements

Version 2.1 is the result of a much deeper development effort than previous Y2Player updates. Its main focus is faster and more reliable library scanning, accompanied by several important metadata, playback-engine, playlist, and diagnostic improvements.

## Building a Proper Development Environment

One of the largest obstacles when developing Y2Player was that the original firmware does not provide a functional ADB environment. Without ADB, it is extremely difficult to profile the application, collect detailed traces, inspect database behavior, or determine what Android is doing during a library scan.

To overcome this limitation, I built a static API-19 ARM `adbd` from pinned official Android 4.4.2 source and integrated it into a verified copy of the stock MediaTek boot image.

The resulting development image preserves USB mass storage, uses RSA-authorized non-root ADB, and keeps the production security properties enabled. This gave me a reliable way to profile Y2Player directly on the physical hardware without turning the device into an insecure general-purpose debug system.

With this environment, I could instrument every stage of the scanner, examine SQLite query plans, collect native FFmpeg timings, monitor memory and wake-lock behavior, and test changes against real and synthetic music libraries.

The improvements in v2.1 are therefore based on measured physical-device results rather than trial-and-error optimization.

## Finding the Main Scanner Bottleneck

The largest confirmed scanner problem was an inefficient database lookup.

During a first scan, Y2Player attempts to match each discovered file against an existing database entry. One fallback query compared the storage volume and relative path case-insensitively. Unfortunately, the database did not contain an index that matched both the columns and the required collation.

As the library grew, Android’s SQLite implementation repeatedly scanned an increasingly large part of the database. On a synthetic 9,178-file library, this single operation consumed 258.160 seconds more than four minutes and approximately 43% of the instrumented baseline.

Adding the correct composite, case-insensitive index changed the query into an exact covering-index lookup. The same phase then completed in 4.124 seconds.

That is a measured reduction of 98.4%.

Scanner batches were also increased from 64 to 400 files. Unchanged-file update chunks were increased from 192 to 400 while remaining below Android’s SQLite parameter limit. This reduced fingerprint queries and database transactions from 144 to 23.

## Measured Scanner Results

The optimized synthetic first scan completed in:

5 minutes 9.882 seconds for 9,178 files.

The instrumentation accounted for 99.83% of that time, leaving only 0.531 seconds unattributed.

Other measured results include:
  - The problematic relative-path lookup fell from 258.160 to 4.124 seconds.
  - Fingerprint-query time fell from 8.109 to 1.913 seconds.
  - Database commit time fell from 3.368 to 1.669 seconds.
  - An unchanged 9,178-file library fell from 42.106 to 19.070 seconds.
  - A real 225-file initial scan improved by approximately 14% after the database and batching changes.
  - Later FFmpeg probe tuning reduced repeated real-library scan time by an additional measured average of 12%.

The large synthetic library was designed to test scanner scaling, traversal, and database behavior. It is not presented as an exact reproduction of any particular real-world library, since actual scan time also depends on codecs, tags, artwork, directory layout, SD-card performance, fragmentation, and filesystem cache state.

## Faster Incremental Scanning

Existing libraries now update more efficiently because metadata extraction only runs for files that have actually changed.

Tests covering adding, modifying, renaming, and deleting individual files confirmed that:
  - Adding one file performs one metadata read.
  - Modifying one file performs one metadata read.
  - Renaming one file indexes the new path and marks the old path unavailable.
  - Deleting one file performs no metadata read and marks the deleted path unavailable.
  - Unchanged files perform zero FFmpeg metadata calls and reread zero metadata bytes.

The scanner still traverses the library and checks file fingerprints so that removals and external changes are detected correctly. Avoiding that traversal entirely would require a more substantial change-detection architecture.

## FFmpeg Metadata Improvements

Version 2.1 also refines the metadata pipeline introduced alongside the FFmpeg engine.

The scanner performs one metadata-only JNI call per changed file. It uses FFmpeg’s container layer but does not initialize an audio decoder, decode PCM, or load embedded artwork into memory during indexing.

Attached-picture payloads are skipped during scanning. The scanner records whether artwork exists, while the compressed artwork itself is loaded separately and only when required by Now Playing, album views, or remote controls.

The retained FFmpeg metadata settings are now:
  - 32 KiB probe size, reduced from 512 KiB.
  - 100 ms maximum analysis duration, reduced from 2 seconds.

These settings were not chosen based on timing alone. Every candidate was validated against the complete media regression corpus before being accepted.

On the controlled physical-card benchmark, the final settings produced:
  - 12.0% lower average scan time.
  - 22.9% fewer metadata bytes read.
  - 69.7% less time in FFmpeg stream analysis.
  - Zero additional metadata failures.

The remaining dominant operation is now `avformat_open_input`, particularly for files containing large tag or artwork regions. This is why further substantial improvements will require more than another simple probe-limit adjustment.

## Metadata Correctness

The new regression suite also uncovered several metadata correctness issues.

Version 2.1 fixes or improves:
  - Comments and track/disc totals throughout JNI, database storage, and library reloads.
  - ReplayGain tags in Vorbis and Opus containers.
  - Deterministic selection when duplicate ReplayGain tags exist.
  - Rejection of malformed ReplayGain values instead of treating them as zero.
  - ADTS AAC sample-rate and channel detection without opening a decoder.
  - FLAC bit-depth detection directly from STREAMINFO when required.
  - Removal of misleading PCM bit-depth values from lossy codecs.
  - More consistent classification of unsupported, corrupt, and partially playable files.
  - Detection of skipped invalid packets and unexpectedly short decoded output.
  - Handling of extremely large metadata values through a bounded text contract.
  - Correct artwork-presence detection without decoding or retaining the image during a scan.

These changes also required a database migration so the additional metadata fields remain available after the application restarts.

## Scanner Reliability and Progress

Long scans now hold a dedicated partial wake lock only while scanning is active. This prevents the CPU from suspending in the middle of a large scan when the screen turns off.

Physical-device testing confirmed that the scanner wake lock is released immediately after the work finishes and is not retained while the application is idle.

The interface also displays scan progress while the library is being built, providing visible feedback instead of leaving the user to wonder whether indexing is still active.

## Playlist Portability

Playlist importing has been improved for playlists created on desktop operating systems.

Y2Player can now relocate Windows, macOS, and Linux absolute paths to matching files stored near the playlist on the device. Once one desktop directory has been mapped to a device directory, later entries from the same source directory use the cached mapping instead of repeating the search.

Relative paths and normal device-local paths continue to work as before.

## Playback Engine Refinements

Although version 2.0 introduced the new FFmpeg playback engine, version 2.1 contains another substantial internal refinement.

Decoded audio now remains in float32 throughout Y2Player’s processing path. ReplayGain, balance, fades, ducking, gapless transitions, and crossfade mixing are all applied before one final conversion to PCM16 at the Android 4.4 AudioTrack boundary.

This provides several benefits:
  - Temporary signal headroom is preserved during processing.
  - Intermediate clipping is avoided.
  - Crossfades no longer quantize each track before mixing.
  - Reusable buffers eliminate unnecessary per-block allocation.
  - Android 4.4 receives the PCM16 format required by its public AudioTrack implementation.

The update also fixes a race where an old cancellation request could affect a newly prepared decoder or seek operation. Decoder commands and abort signals are now ordered together so a stale abort cannot cross into replacement work.

Additional engine improvements include:
  - Reliable fallback seeking for very short FLAC files without seek tables.
  - Bounded recovery from malformed audio packets.
  - More deterministic damaged-file warnings.
  - Correct gapless and crossfade promotion without flushing AudioTrack.
  - No wake-lock gap during a successful prepared-track transition.
  - Suppression of expected FFmpeg decoder-rejection noise during metadata-only scans while genuine decoder errors remain visible.
  - Removal of an unnecessary duplicate foreground-notification update during playback start.

Normal playback, gapless promotion, crossfades, screen-off playback, Bluetooth output, physical controls, scanning during playback, notification state, and wake-lock release were validated separately on the physical device.

## Automated Regression Testing

One of the most valuable results of this work is something users will never directly see: a permanent automated media regression suite.

The current corpus contains 76 deterministic fixtures:
  - 35 metadata cases.
  - 24 technical-format cases.
  - 17 malformed or unsupported cases.

It covers MP3, FLAC, AAC/M4A, ADTS AAC, ALAC, WAV integer and floating-point PCM, AIFF, Ogg Vorbis, Opus, ReplayGain combinations, embedded artwork, unusual text encodings, truncated files, corrupt metadata, invalid packets, missing tags, and several boundary cases.

On the physical Innioasis Y2, the final validation passed:
  - 76 of 76 fixtures.
  - 1,394 of 1,394 independently declared metadata assertions.
  - Decode-to-EOF checks for every playable fixture.
  - Midpoint seek checks for every applicable fixture.
  - Production scanner and database comparisons.
  - 25 complete resource-test cycles.
  - 1,900 metadata calls and 1,900 decode attempts.
  - Zero leaked file descriptors.
  - Zero leaked threads.
  - No crashes, ANRs, SQLite errors, non-finite PCM, or metadata failures.

The automated corpus validates the media engine below AudioTrack. Hardware transport, Bluetooth routing, notifications, physical controls, screen-off playback, gapless transitions, crossfades, and wake locks are tested separately on the real device.

## Firmware Work

The firmware pipeline now also contains a guarded patch for the stock primary-audio HAL’s previously inactive DAC-frequency hook.

This is groundwork for future 44.1/48 kHz output work. It does not currently change Y2Player’s advertised output format: the application still uses the proven 44.1 kHz stereo PCM16 Android path. Version 2.1 therefore does not claim native high-resolution output.

The generated firmware independently verifies the APK, native library, patched HAL, filesystem metadata, SELinux contexts, partition size, and readback hashes before producing `system.img`.

## Is This the Fastest It Can Possibly Be?

Probably not.

The current scanner architecture prioritizes correctness, compatibility, and reliability. Every new or changed file is still opened through FFmpeg so metadata is handled consistently across all supported formats.

After the database and probe improvements, FFmpeg’s container-opening stage is the main remaining first-scan bottleneck. On an unchanged library, the remaining cost comes from directory traversal, file-stat checks, fingerprint queries, seen-token updates, and rebuilding the in-memory index.

Potential future work includes:
  - Reducing container and metadata parsing overhead for common formats.
  - Improving handling of very large embedded artwork and tag regions.
  - Reusing compiled SQLite statements in the changed-file update path.
  - Avoiding unnecessary unchanged-file database writes.
  - Investigating durable per-directory change detection.
  - Measuring cold SD-card block I/O with better kernel tracing.
  - Carefully evaluating limited parallel metadata extraction.

Parallel scanning is not automatically faster on this device. The Y2 has limited memory, a relatively slow removable-storage path, and only a small number of CPU cores. Multiple FFmpeg probes could increase contention, memory pressure, or playback interruptions. Any parallel implementation therefore needs to be measured and validated rather than assumed to be an improvement.

## Looking Ahead

The new ADB development environment and permanent regression suite make future optimization much safer.

Changes can now be tested against known metadata, playback, corruption, seeking, memory, and resource expectations before they reach a release. This makes it possible to improve performance without silently breaking unusual files or introducing subtle playback regressions.

My goal remains the same: correctness first, performance second.

A scan that is consistently accurate and reliable is ultimately more valuable than one that is only marginally faster.

Feedback from real-world libraries is especially useful. If you have a large collection, unusual metadata, embedded artwork that causes problems, or files that do not behave as expected, I would be very interested in hearing about it. Those reports help identify where Y2Player can improve next.

## Also useful
  - [Install guideStep-by-step install for Y2Player](../../guides/y2player-y2.html)
  - [Y2Player V2.5Release2.5 · 2026-09-04](../../release-notes/y2player-y2/release2.5.html)
  - [Y2Player V2.3ReleaseV2.3 · 2026-08-15](../../release-notes/y2player-y2/releasev2.3.html)
  - [Y2Player V2.2.2RealeaseV2.2.2 · 2026-08-10](../../release-notes/y2player-y2/realeasev2.2.2.html)
  - [Y2Player V2.2.1 ReleaseV2.2.1 · 2026-08-03](../../release-notes/y2player-y2/releasev2.2.1.html)
  - [Y2Player V2.2ReleaseV2.2 · 2026-08-01](../../release-notes/y2player-y2/releasev2.2.html)
  - [Y2Player 2.0 Complete Media Engine RewriteReleaseV2.0 · 2026-07-27](../../release-notes/y2player-y2/releasev2.0.html)
  - [Y2Player V1.2ReleaseV1.2 · 2026-07-26](../../release-notes/y2player-y2/releasev1.2.html)

Notes as published by the Y2Player project. Install it with Updater CE, or download it from the firmware directory.

Published by the [schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2FY2Player&software=y2player-y2)[[2]](https://innioasis.app/release_notes.html?author=schulzcode&project=Y2Player&version=ReleaseV2.1&software=y2player-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
