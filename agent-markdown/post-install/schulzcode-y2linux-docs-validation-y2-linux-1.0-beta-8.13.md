---
title: "Y2Linux 1.0 Beta 8.13 (Baseline 110) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.13 Baseline 110 Status: PUBLISHED as GitHub release baseline-110 2026-10-20. Release 1.0.0-beta.8.13 , Reborn 1.0.0-beta.8.13 , kernel 6.18.56-y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.13.html"
---

# Y2Linux 1.0 Beta 8.13 (Baseline 110) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.13 (Baseline 110)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.13 (Baseline 110)

Status: PUBLISHED as GitHub release `baseline-110` (2026-10-20). Release `1.0.0-beta.8.13`, Reborn `1.0.0-beta.8.13`, kernel `6.18.56-y2linux-1.0.0-beta.8.13`, update sequence 7701, Linux `1a92e05`, Reborn `21cd3b0`. Built with `tools/production/release.py` (104 s, resumed workspace, update based on `baseline-108`): container suite 842 OK, host suite 888 OK; all seal checks PASS, no MediaTek firmware in any image. Build 110 itself was installed on the maintainer's player over the air (stage + apply) and checked (below); test build 109 (sequence 7700) before it found the hidden-file case. Owner: "fix all of this, publish 8.13 and mark all of these reports as solved". Milestone audit BETA-8.13 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 5d62c5b9d6130317c092945c12c3b1580778037c2d85eb3c70d7d4ccbc35f916 |
| Y2ROOT | 58995bf3103d75b7996f6bbcca342f6fd5f2a03bd93d0dbeb3b6154ca5c5b558 |
| RECOVERY | 2366385b73599bd932b4e8c4a610b08139596dbe307f3585c79389a732f15be5 |
| Y2DATA (no SSH key) | 47e6be94fd53b336f4897636cbe54db088c2d0052bd2666edfa8d0dbc9ad1c9f |

## The reports

Five uploaded error reports from four players (Beta 8.10–8.12) and two user messages, read against Beta 8.12:````````````````````````

| Finding | Players | Evidence | Verdict |
| --- | --- | --- | --- |
| Strawberry sees Internal Storage but not the SD card | ef0d23eb (8.11) | SD card exported correctly (storage 0xFFFF0002, removable, rw), no MTP errors; every file reported as ObjectFormat Undefined; libmtp's track list skips Undefined objects (libmtp.cLIBMTP_Get_Tracklisting), Strawberry also drops tracks without a title; host mtp-tracks against 8.12: 0 tracks | open on 8.12 → fixed |
| Wi-Fi connection dropped | 69635cdc (8.12) | WARNING … net/wireless/sme.c:845 __cfg80211_connect_result (bss_not_found); 7 real disconnects in 42 min; the driver reported only the BSSID and cfg80211 looked the BSS up again by wpa_supplicant's SSID in its event work | open on 8.12 → fixed |
| Exception ignored while flushing sys.stdout: OSError [Errno 22] at every boot | all (8.8–8.12) | reborn-boot-services sent boot-stage services_started output (boot history, several KiB) raw to /dev/kmsg, which refuses a record over 1 KiB; the stage itself was saved before | cosmetic → fixed |
| Silence after pause/resume (user message) | ef0d23eb (8.11, wired) | an in-place resume at 813 s after 60 s, reopen 40 s later; no kernel log of that boot. A pause over 180 s releases the output, and Play reopens it: the #48 crystal path (silent until the next track) | fixed in 8.12; checked on 8.12 (below) |
| reborn_crash sent from 8.12 | dbe84d46 | the old 8.10 playlists.rs:223 panic re-sent once: 8.12 keys the panic by content instead of mtime | once per install, no change |
| Reborn crash loop, unclean restart | dbe84d46 (8.10) | #49 playlists.rs:223 | fixed in 8.12 |

## What changed since Beta 8.12````````````````````````````

| Part | Change |
| --- | --- |
| MTP track listing | umtprd overlay 0005: music files report their format by extension (MP3, WAV, WMA, OGG/Opus, AAC, M4A, FLAC; hidden files and everything else stay Undefined) in ObjectInfo, ObjectFormat and GetObjectPropList; DeviceInfo lists them as playback formats. Name = the tag title (file name without extension when unknown), plus Artist, AlbumName, AlbumArtist, Track, Duration, SampleRate, NumberOfChannels, AudioBitRate, read-only from Reborn's library (/data/reborn/library.db, read-only, online sources only, no snapshot held, file-name fallback when missing or busy). ObjectFileName is unchanged, renames keep working. Linux 207e920, 3f4f3d1, tests test_mtp_music_tags.py, SQLite stub for the container 338e408. |
| Wi-Fi connect | The driver hands the BSS entry it looked up (or informed from its own scan record) to cfg80211_connect_bss, which takes that reference, instead of only the BSSID. Linux 9595a50. |
| Boot log | The services_started stage record goes to /dev/null; errors still go to the kernel log. Linux 0f18219. |
| Report tools (maintainer PC) | fetch.py --flat --notify --pending, a systemd user timer every 15 min into UserReports/, and the REVIEWED.md ledger. Linux d456790. |

## Device results (maintainer's player, ST7701S)````````

| Check | Result |
| --- | --- |
| Pause/resume on 8.12, wired headphones (before any change) | ~25 s pause: drained → SETUP, prepare → RUNNING, sound (owner listening); 3.5 min pause: released at 180 s, Play reopened (generation 6→8), sound; no XTAL line in dmesg |
| OTA 8.12 → test build 109 → build 110 (stage + apply) | install ≈16 s each, Acknowledged 7700 and 7701 |
| mtp-tracks (libmtp 1.1.23, the call Strawberry uses) | 8.12: 0 tracks. 109: 322 (11 of them macOS ._ files). 110: 311 tracks = 311 music files = 311 live library rows, every one with artist and duration; 300 FLAC, 11 MP3 |
| Wi-Fi | connected at boot; 3 × off/on: COMPLETED with DNS after 8 s each; no sme.c warning, no "not in the scan table" |
| Boot log | no Errno 22 |

## Known gaps
  - Strawberry itself was not run (no Strawberry on the maintainer's PC); `mtp-tracks` uses the same libmtp call and the

same fields Strawberry reads.
  - Windows Explorer may show music files by their title (MTP Name) instead of the file name, as older Android phones

did; copying still uses the real file name. Owner's choice (title for libmtp clients). Not checked on Windows.
  - Songs copied by a libmtp client show their file name as title until Reborn has scanned them.
  - The in-place pause path (under 180 s) could not be made silent on 8.12; if it recurs, 8.12+ reports include the

codec registers.
  - Unchanged from 8.12: slow crystal, sleep with a parked CPU, Couldn't Start on a player, #47 confirmation, WAF rule

and billing alert, sleep drain (#42), GC9503V confirmation (#45).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
