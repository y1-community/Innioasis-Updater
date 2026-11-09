---
title: "Current Y2Linux platform state - Innioasis Updater"
description: "Current Y2Linux platform state Y2Linux 1.0 Beta 9.3.19, Baseline 228 — 2026-11-08 latest, published Release 1.0.0-beta.9.3.19 , tag baseline-228 , Linux d6c404e4 , Reborn"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-current_platform_state.html"
---

# Current Y2Linux platform state - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Current Y2Linux platform state

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Current Y2Linux platform state

## Y2Linux 1.0 Beta 9.3.19, Baseline 228 — 2026-11-08 (latest, published)

Release `1.0.0-beta.9.3.19`, tag `baseline-228`, Linux `d6c404e4`, Reborn `520c4b8`, sequence 15300, root v1.251. Update Notifications (Y2Reborn #97): a toggle on Software Update, off by default; with it on, Reborn observes the platform on any screen every 120 s while online and the screen is lit, and says "Software update available" once per version (`update_announced` persisted). Before, only Settings screens observed, so the daily `update auto-check` answer reached Reborn only when Settings was opened. Device-checked on test build 228 (switch off: nothing; named version: nothing; new version: toast after 64 s). Release text in the listener format with `github-only` markers (docs/RELEASE-NOTES-TEMPLATE.md). Details: [Beta 9.3.19 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.19.md).

## Y2Linux 1.0 Beta 9.3.18, Baseline 227 — 2026-11-08 (published)

Release `1.0.0-beta.9.3.18`, tag `baseline-227`, Linux `9e864a3d`, Reborn `56298e9`, sequence 15200, root v1.250. USB always enumerates again (F78, Y2Linux #102): a disconnect while no gadget was bound left musb in host mode (`musb_g_disconnect` default case), so every bus reset was "Babble" until a restart; `kernel/usb/role.h` keeps the controller a peripheral after every disconnect and before every reconnect (device repro: 226 Babble + no enumeration, 227 configured 0.5 s after reconnect). Reborn: Luna XP skin (eNKay, seventeen skins), skin var `{bitrate}` (#87; the Song Info page that also shows it has no menu entry since UI v3), update page "Connect to Wi-Fi" offline (Y2Reborn #96), Quick Menu hold opens settings (#101), Artist's Albums order (#75), Cover Flow follows the skin (`cover_shape`, captions; #100), unplayable files counted and named in Settings → Library (#104). Installed on the developer's player as test build 227. Details: [Beta 9.3.18 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.18.md).

## Y2Linux 1.0 Beta 9.3.17, Baseline 225 — 2026-11-08 (published)

Release `1.0.0-beta.9.3.17`, tag `baseline-225`, Linux `132cbec9`, Reborn `e14b17b`, sequence 15000. Report fixes, written to hold for every format, name and headset (owner 2026-11-08): Now Playing covers for MP3/AAC/Opus/Ogg again (F74, Y2Reborn #102, Y2Linux #98: 9.3.16's 250 ms `settle` cushion was unreachable with 8 small decoder blocks; now ≥ 250 ms queued or 500 ms after the first block); uMTP patch 0007 accepts every name a computer sends (F75, #88: ".." inside names, emoji surrogate pairs both ways, ';' kept, 1024-byte names); Bluetooth output switches once the PCM is negotiated and retries a failed switch (F76, Y2Reborn #103); Cover Flow thumbnails follow folder cover images (F77, Y2Reborn #105). Installed on the developer's player (Acknowledged in 87 s; folder cover 0.8 s after Play, gapless cover, 0 xruns). Details: [Beta 9.3.17 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.17.md).

## Y2Linux 1.0 Beta 9.3.16, Baseline 224 — 2026-11-06 (published)

Release `1.0.0-beta.9.3.16`, tag `baseline-224`, Linux `5d87f546`, Reborn `ceb4824`, sequence 14900. Steady Bluetooth (Y2Linux #96, Y2Reborn #99, #87): Reborn keeps a playing Bluetooth PCM open and fed with music or silence (kept sink fed between streams, no drain at a song end, 8 × 1024-frame BlueALSA ring, pause holds 3 s then releases, no probe open at Play; F69 had 93 of 114 reuses run dry since 9.3.12); BlueALSA patches 0005/0007/0008 removed, SBC/AAC adaptive rate off by default, bluealsad `--a2dp-force-audio-cd`; y2-radiod parks a headset after 3 quick drops (F70). Gapless boundaries and wheel clicks no longer underrun (F71, F72). Installed on the developer's player; listening checks owed. Details: [Beta 9.3.16 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.16.md).

## Y2Linux 1.0 Beta 9.3.15, Baseline 223 — 2026-11-05 (published)

Release `1.0.0-beta.9.3.15`, tag `baseline-223`, Linux `e9bcdee5`, Reborn `e2555d2`, sequence 14800 (test build 222 = 9.3.14, the same menu as a list, never published). Holding Power opens the Quick Menu (Y2Linux #85): a centred, animated panel of tiles (Wi-Fi, Bluetooth, Brightness, Sleep Timer, Restart, Power Off); holding on fills the turn-off ring around Power Off (3 s + 1.2 s). Reborn `quick_menu.rs` / `views_quick.rs`. Installed on the developer's player. Details: [Beta 9.3.15 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.15.md).

## Y2Linux 1.0 Beta 9.3.13, Baseline 221 — 2026-11-05 (published)

Release `1.0.0-beta.9.3.13`, tag `baseline-221`, Linux `24d50299`, Reborn `94f417c`, sequence 14600. A Wi-Fi join that finds nothing restarts Wi-Fi once (`y2-radiod``WifiRestart`) and tries again (Y2Linux #83, report 1da7496c: 34 s of blind scans after Wi-Fi came on). Networks the player cannot join say why (WPA3 only, Needs a login, WEP; Y2Linux #91): WPA3 is impossible on this hardware (firmware SME with open/WEP/WPA/WPA2 only, no external auth, PMF compiled out). Letter jumps land at the top (Y2Reborn #91); the Now Playing cover is square under a skin, Winamp's centred, Cassette's stripe above the title (Y2Reborn #81, #82). Not run on a player before release. Details: [Beta 9.3.13 report](validation/Y2-LINUX-1.0-BETA-9.3.13.md).

## Y2Linux 1.0 Beta 9.3.12, Baseline 220 — 2026-11-04 (published)

Release `1.0.0-beta.9.3.12`, tag `baseline-220`, Linux `31d3987e`, Reborn `d52589a`, sequence 14500 (test builds 216–220 = 9.3.8–9.3.12; only 220 published). A pause ends the Bluetooth stream again (`bluealsad --keep-alive=0`, as 9.2.16 and phones): the stream kept started without packets had muted the AirPods after every pause/resume gap and after skips, and made them stop answering 2 s into a pause (the 9.3.7 supervision-timeout drop). A track change keeps the Bluetooth sink's queued audio and does no drain (no packet gap at all, btmon). The 15-min paused-headset hold now counts from each pause (Y2Linux #90, F68: the stale hold let the player sleep 60 s after a pause). F66 codec-change loop (Y2Reborn #94) fixed. BlueALSA 0007/0008 (timestamp over a gap, refill). Details: [Beta 9.3.12 report](validation/Y2-LINUX-1.0-BETA-9.3.12.md).

## Y2Linux 1.0 Beta 9.3.7, Baseline 215 — 2026-11-03 (published)

Release `1.0.0-beta.9.3.7`, tag `baseline-215`, Linux `153a88cd`, Reborn `8fc6f69`, sequence 14000 (test builds 208–215 = 9.3–9.3.7; only 215 published). The radio daemon below, plus: BlueALSA patch 0006 (AirPods' own AAC configuration with A2DP 1.3 reserved channel bits accepted), a link counts as set up once BlueALSA has its stream (BlueZ 5.87 resolves no services for a headset that connects to us), the codec decision waits up to 3 s for the headset's codec list. On the developer's player: 19 wakes without a failed link, AirPods back by themselves in 2.5–4.9 s. Open: a pause longer than ≈22 s ends in a supervision timeout (HCI 0x08) and a reconnect; no overnight on this build; only AirPods Pro tried. Details: [Beta 9.3.7 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.7.md).

## Y2Linux 1.0 Beta 9.3.4 test build 212 — 2026-11-03 (on the developer's player, not published)

Release `1.0.0-beta.9.3.4`, label 212, sequence 13700 (test builds 208–212 = 9.3–9.3.4). Bluetooth rebuilt around one owner, the radio daemon `y2-radiod` ([architecture](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fradio-daemon.md), [plan and as built](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FBLUETOOTH-REIMPLEMENTATION-PLAN.md)): `y2-bt-reconnect`, `bluetooth-power`, the intent file and the operation/PCM locks are gone; Reborn is a client. BlueALSA patches 0004 (LDAC under the Wi-Fi ceiling) and 0005 (learned start rate per headset); `--keep-alive=900`. Wi-Fi power and the wake order go through the daemon; power save while Bluetooth streams. Y2Reborn #92 (library emptied by a Bluetooth rollback) fixed in Reborn.

Device checks on 9.3–9.3.4 (owner's player, AirPods Pro): Bluetooth on → Ready 5.6 s; bluealsad killed → Ready 7.7 s; sleep radio steps down in 0.17–0.25 s, Wi-Fi held at the wake until the headset was back; four pause rounds and a 30 s pause without a link drop (with a 10 s keep-alive one Suspend in three went unanswered and dropped the link); codec settings applied without a restart (headphones back in 7–9 s); Wi-Fi power save on while playing, off when paused, still associated; daemon idle 0 CPU ticks. Open: when the AirPods reconnect on their own after a wake, BlueALSA refuses their AAC configuration (`A2DP.InvalidChannels`); the daemon cancels after 8 s and connects them itself (wake → Ready ≈ 15 s instead of ≈ 6 s). Not yet: an overnight, other headsets, the Wi-Fi join controller (P7).

## Y2Linux 1.0 Beta 9.2.16, Baseline 207 — 2026-11-02 (published)

Release `1.0.0-beta.9.2.16`, tag `baseline-207`, Linux `1b7df30e`, Reborn `8667100`, sequence 13200. Steadier Bluetooth (Y2Reborn #87, F63: XM4 crackled on AAC 320 kbit/s with Wi-Fi on the shared antenna, no host-side loss visible): codec defaults AAC standard (220 kbit/s) and LDAC mobile; `/run/y2/bt-codec-ceiling` while the Wi-Fi radio is on (service daemon) caps CBR AAC at 192 kbit/s and SBC below its top bit-pool in BlueALSA patches 0002/0003 (`y2-codec-ceiling.h`); Reborn Auto ranks AAC, aptX (LDAC/aptX HD only when chosen; the Auto order noted for 26 below no longer applies) and applies a codec choice refused during playback at the next pause. Not yet tried on a player. Details: [Beta 9.2.16 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.16.md).

## Y2Linux 1.0 Beta 9.2.15, Baseline 206 — 2026-11-01 (published)

Release `1.0.0-beta.9.2.15`, tag `baseline-206`, Linux `28c83e60`, Reborn `5745736`, sequence 13100. Reborn only: Settings and Settings > Library count the `tracks` they are given instead of the borrowed (empty) model list, so the song-count cache no longer recounts the library every frame (Y2Reborn #85, contributor PR #86 = `97e46a8`). Installed on the developer's player from 9.2.14 (Acknowledged). Details: [Beta 9.2.15 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.15.md).

## Y2Linux 1.0 Beta 9.2.14, Baseline 205 — 2026-11-01 (published)

Release `1.0.0-beta.9.2.14`, tag `baseline-205`, Linux `6f391669`, Reborn `786eccb`, sequence 13000. Reborn only: the Bluetooth sink is kept between streams like the wired one (Reborn `3435238`, F61, report c0fe2638: quick station changes reopened BlueALSA's PCM twice per station, an AVDTP Start timed out and BlueZ ended the link). GitHub issue forms replace blank issues in both repositories. Installed on the developer's player from 9.2.13 (Acknowledged); six quick skips on AirPods Pro played in the kept sink and were heard. Details: [Beta 9.2.14 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.14.md).

## Y2Linux 1.0 Beta 9.2.13, Baseline 204 — 2026-11-01 (published)

Release `1.0.0-beta.9.2.13`, tag `baseline-204`, Linux `263c67d7`, Reborn `69d8e37`, sequence 12900. Reborn only: a song picked in search plays alone (Reborn #79); long MP3/raw AAC files resume from kept seek points instead of reading from the start (Reborn #80, `native/seek_index.c`, memory only); letter fast scroll at 3 wheel steps again (Y2Linux #64; 9.2.2's 4 steps were out of reach); `peer_disconnected` logs BlueZ's disconnect reason. Details: [Beta 9.2.13 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.13.md).

## Y2Linux 1.0 Beta 9.2.12, Baseline 203 — 2026-11-01 (published)

Release `1.0.0-beta.9.2.12`, tag `baseline-203`, Linux `7dc369a6`, Reborn `4a052b3`, sequence 12800. Bluetooth off no longer waits for `y2-bt-reconnect`'s page of absent headphones (~20 s, then taps switched it on again): off skips `bt-operation.lock`, writes `power_off` and runs `bluetoothctl power off`; on still waits; the sleep quiesce gains the same. Reborn #76: the skin remap table takes MUTED/DIM from the theme (9.2.3's brighter greys stayed light on light skins). Details: [Beta 9.2.12 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.12.md).

## Y2Linux 1.0 Beta 9.2.11, Baseline 202 — 2026-10-31 (published)

Release `1.0.0-beta.9.2.11`, tag `baseline-202`, Linux `6f56156a`, Reborn `9cd6368`, sequence 12700. Reborn only (Y2Linux #73 follow-up): Wi-Fi and Bluetooth status icons only while connected (they showed dim while only on), in the standard bar and skins' `indicators`; `wifi_connected` needs the radio on. Details: [Beta 9.2.11 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.11.md).

## Y2Linux 1.0 Beta 9.2.10, Baseline 201 — 2026-10-31 (published)

Release `1.0.0-beta.9.2.10`, tag `baseline-201`, Linux `1034c242`, Reborn `530f3ae`, sequence 12600 (includes test build 200 = 9.2.9). Reborn only: Settings reorganised into Bluetooth, Wi-Fi, Sound, Display, Skin, Customize (Home Menu, Browsing, Wheel & Buttons), Library, System, with pickers and hints (`customize.rs`; map and placement rule in Y2Reborn `docs/ui/REBORN-SETTINGS-MAP.md`; sub-pages reuse existing screens so sessions stay rollback-safe); menus scroll on the screen like lists (#74), Music scrolls, Cover Flow's year once (#73). User guides follow the new paths. Details: [Beta 9.2.10 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.10.md).

## Y2Linux 1.0 Beta 9.2.8, Baseline 199 — 2026-10-31 (published)

Release `1.0.0-beta.9.2.8`, tag `baseline-199`, Linux `c824964c`, Reborn `a39176e`, sequence 12400. Platform diagnostics only (Y2Linux #83, F60 reopened): `EventMonitor::count_reject` records association/authentication rejects by status code (and timeout) in network.json `supplicant_events.rejects` and the self-heal journal rows. #83's reports: saved AP seen at −55…−61 dBm among ≈50 networks, rejected 12–20 times. Details: [Beta 9.2.8 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.8.md).

## Y2Linux 1.0 Beta 9.2.7, Baseline 198 — 2026-10-31 (published)

Release `1.0.0-beta.9.2.7`, tag `baseline-198`, Linux `949d4577`, Reborn `38946ea`, sequence 12300. Reborn only: wheel clicks whenever no music plays (owner, #77) — with no stream the sink thread opens or keeps a wired sink for clicks (10 s after the last; a start reuses it), a hold on the other route is released, a sleep request closes a kept sink; the 9.2.6 crackle (silence rewound on a stale pointer → xruns) fixed by never rewinding (`rb_sink_rewind` gone). Device-checked: open 40 ms, close 10 s after. Details: [Beta 9.2.7 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.7.md).

## Y2Linux 1.0 Beta 9.2.6, Baseline 197 — 2026-10-31 (published)

Release `1.0.0-beta.9.2.6`, tag `baseline-197`, Linux `b3848c9a`, Reborn `dc335e8`, sequence 12200. Reborn only: Y2Reborn #77 (report ec243f8c) — the wired codec has no device pause, so a held stream is drained to SETUP and 9.2.4's clicks failed `ALSA -77`; clicks now prepare the stream after the paused music played out, only while paused; Wheel Click Off/On (`when_paused` kept as On's name). Details: [Beta 9.2.6 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.6.md).

## Y2Linux 1.0 Beta 9.2.5, Baseline 196 — 2026-10-31 (published)

Release `1.0.0-beta.9.2.5`, tag `baseline-196`, Linux `76bd154d`, Reborn `f45f6bc`, sequence 12100. Platform only: F60 (Y2Linux #83, report fa30bf96) — `WifiRecovery::restart_unseen` blocks and unblocks Wi-Fi's rfkill (waiting for wlan0 to go) after ≥ 4 NETWORK-NOT-FOUND over ≥ 60 s with no saved network in the scan, at most every 600 s until a connect; journal row `wifi_restart`. Cause of the blind scans unproven (Bluetooth reconnect at the same time). Details: [Beta 9.2.5 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.5.md).

## Y2Linux 1.0 Beta 9.2.4, Baseline 195 — 2026-10-31 (published)

Release `1.0.0-beta.9.2.4`, tag `baseline-195`, Linux `0a31c6c4`, Reborn `8ecff51`, sequence 12000. Reborn only: Home order (Customize > Home Menu, `home_order`) and playlist order (`playlist_order`, the playlist menu's Move), Customize > Wheel Click Off/When Paused/Always (a tick mixed into the wired sink only, with a song loaded; `AudioSink::rewind`/`rb_sink_rewind` take back unplayed frames and `playback/click.rs` writes them again), Cover Flow text travelling with its cover. GitHub: Y2Reborn #53 #33 #67 #71. Details: [Beta 9.2.4 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.4.md).

## Y2Linux 1.0 Beta 9.2.3, Baseline 194 — 2026-10-31 (published)

Release `1.0.0-beta.9.2.3`, tag `baseline-194`, Linux `1f206bf4`, Reborn `9a50d47`, sequence 11900. Reborn only (owner: "do all the defaults", no new settings): release year (`Track.year`, additive column, `METADATA_REVISION` 5 = one tag re-read after the update; artist albums oldest first; host 150k timing unchanged), Other Network… for hidden Wi-Fi (`scan_ssid 1`), Cover Flow position in the title (`{position}`), numbered album songs in skins (`numbered`), brighter `MUTED`/`DIM`. GitHub: Y2Reborn #66 #61 #70 #59, Y2Linux #75. Details: [Beta 9.2.3 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.3.md).

## Y2Linux 1.0 Beta 9.2.2, Baseline 193 — 2026-10-31 (published)

Release `1.0.0-beta.9.2.2`, tag `baseline-193`, Linux `275c1ab1`, Reborn `29aa1cc`, sequence 11800. Fix releases after 9.2 are numbered 9.2.x (owner); 9.2.1 (test build 192, sequence 11700) was not published and is included. F59 (reports 39778b8a, 8b00b513): an SD card that never sets Power Off Notification Ready failed every first suspend (-110), and the helper then quarantined sleep on the image; kernel patch 0071 (Y2 SD host: flush the cache, on a notify timeout drop the feature and deselect) and `Run::kernel_refusal` (a refusal in step `suspend` proven by `suspend_stats` retries after 120 s instead of quarantining). GitHub requests: skins' `indicators` element and every shipped skin's status icons (#70, #73), AM/PM and skins' `{date}` (#72), brightness 5–100 % in 5 % steps by the wheel (#74), letter fast scroll only at 4 suggested steps (#64), 20 equalizer filters (#76). Coding standard: length limits are ceilings (functions 150, files 1500). Details: [Beta 9.2.2 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.2.md).

## Y2Linux 1.0 Beta 9.2, Baseline 191 — 2026-10-31 (published)

Release `1.0.0-beta.9.2`, tag `baseline-191`, Linux `7f5d29db`, Reborn `f445483`, sequence 11600. Owner: "a wake problem … pressing the button again to wake takes extremely long". Cause: the sleep helper's radio quiesce retried Bluetooth off for up to 25 s while `y2-bt-reconnect` paged headphones that were off (≈20 s, holding `bt-operation.lock`) and did not read the wake IRQs meanwhile (power journal of 190: 17.6/17.7/6.4/15.6 s). Fixes: a Power/RTC wake during the quiesce and the chip power-down wait refuses at once (`woken`); a busy `bluetooth-power` writes `power_pending`, so the owner cancels its page (checked on the player: off after one refusal, 1.1 s). Also: serde_json `float_roundtrip` (≈1 in 450 floats read one ULP off; reset plans refused as `reset_plan_changed`), the reset goldens' host `device` volatile. Includes test build 190 (below). Details: [Beta 9.2 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.md).

## Since Beta 9.1 (test build 190, sequence 11510, 2026-10-31; in Beta 9.2)

Code clean-up after an audit of both repositories, and the [coding standard](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCODING-STANDARD.md) with its enforcement: the platform gate now runs `tools/development/code-quality.py`, a ratchet over the platform's and Reborn's production code (function and file length, `unsafe`, `unwrap`, panics, lint exceptions, raw JSON lookups, lines rustfmt cannot format, TODO markers) against `code-quality-baseline.json`. Changes: one command runner in y2p-core (`run_passing_fd` was a second copy), Reborn's screen dispatch once (the skin fallback had lost Music), `effect_inner` an exhaustive table (921 → 299 lines, the long cases in `runtime/effects/`), the Bluetooth thread a worker (`run`, `session`, `open`, seven steps, `command`), eight stale development scripts in `tools/archive/`. Behaviour unchanged except the Music fallback; every move checked token for token.

## Y2Linux 1.0 Beta 9.1, Baseline 189 — 2026-10-30 (published)

Release `1.0.0-beta.9.1`, tag `baseline-189`, Linux `2851b70d`, Reborn `e309b49`, sequence 11500. Housekeeping after the rewrite (owner: "do all the stuff you mentioned"): Reborn reads the platform's records in `y2p-contract` types (`update`, `power`, `network`, `storage`, `usb`, `reports`, `radio`; CONTRACT.md), Reborn's `main.rs`, `playback.rs` and `reborn-ui/src/lib.rs` split and its main loop and audio threads cut into named sections (no code change, verified by comparing the moved text), platform leftovers into y2p-core. Visible: the Settings row shows the update download percentage. Test builds 187–188 built only; 189 = the published images. Details: [Beta 9.1 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.1.md).

## Y2Linux 1.0 Beta 9.0, Baseline 186 — 2026-10-30 (published)

Release `1.0.0-beta.9.0`, tag `baseline-186`, Linux `1e55c79f`, Reborn `2bc1e2c`, sequence 11400. The platform is Rust (no Python on the player): the port (test builds 165–171), the refactor (172–179) and typed records (180–185, owner decisions: /data rollback-safe, status shape may change, the critical path fails closed with one reason). Fixes: SD write window closed on USB unplug, expired windows re-protected, SFTP root, two update checks, Restore Previous System's battery gate, radio firmware failures, DNS after a DHCP renew, Reborn's sleep requests on the cable. Test build 186 = the published images. Details: [Beta 9.0 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md).

## Y2Linux 1.0 Beta 8.43, Baseline 164 — 2026-10-28 (published)

Release `1.0.0-beta.8.43`, tag `baseline-164`, Linux `f5529b7`, Reborn `a08ca5d`, sequence 11000. Reborn only (the platform changes the version): Y2Reborn issues #51 (leaving Search), #45/#46 (one album per folder and title), #52/#55 (Home items can be hidden), #60/#25 (Go to the source), #57 (Cover Flow shelf in skins), #56 (Album Order), #30 (letter steps), #62 (unplug message), #28 (USB and seek ticks). Test build 164 = the published images, Acknowledged on the owner's player. Details: [Beta 8.43 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.43.md).

## Y2Linux 1.0 Beta 8.42, Baseline 163 — 2026-10-28 (published)

Release `1.0.0-beta.8.42`, tag `baseline-163`, Linux `7e5b151`, Reborn `25b8e06`, sequence 10900. Sleep without relighting (F47/F48: UART0 RX pad to GPIO in sleep, a refused sleep stays dark, Reborn blanks at once and has no Sleep page); large SD cards checked in the background (F49) and Reborn's quick scan; Wi-Fi and Bluetooth on players whose PROTECT_F/S were never formatted (#62); fixes from the 2026-10-28 review of 40 error reports: shutdown watchdog and per-step trail (F39), a power-off that never returns (F50), recovery watchdog from the first step and both partitions at start (F34, F23, #63), Play waits for lost Bluetooth headphones (F51), Wi-Fi reasons, WRONG_KEY latch and heal (F52/F53), battery percent after a warm restart and the sleep floor (F54/F55), Power held after a wake (F57), DSI restart for a dark start (F17), PMIC power status in the boot evidence (F56). `CONFIG_LOG_BUF_SHIFT` 19 (log from `log_buf_len=1M`) to stay under the 12 MiB Image cap. Test builds 160–162 on the owner's player. Details: [Beta 8.42 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.42.md).

## Y2Linux 1.0 Beta 8.41, Baseline 159 — 2026-10-27 (published)

Release `1.0.0-beta.8.41`, tag `baseline-159`, Linux `af69742`, Reborn `1358702`, sequence 10700. Internal speaker (OCA72559/AW87559 with stock tables, stock speaker route, exclusive outputs), headphone detection (200 ms detector poll while the codec is powered, no codec IRQ), Reborn Output > Speaker with mono downmix, plug moves to headphones and unplug pauses; haptic feedback (VIBR regulator-haptic, Customize > Haptics, 60 ms per button press as stock). Test builds 155–158 on the owner's player. Details: [Beta 8.41 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.41.md).

## Y2Linux 1.0 Beta 8.40, Baseline 154 — 2026-10-27 (published)

Release `1.0.0-beta.8.40`, tag `baseline-154`, Linux `1b09963`, Reborn `77c54e2`, sequence 10500. Kernel only: power off with a charger attached restarts into LK's charging mode (stock `charger` reset: WDT without AUTO_RESTART, boot reason 3 → mode 8 → offline charging) instead of staying off and never charging (ledger F46, install 02f46e9f and the fleet's power journals). Checked on the owner's player: `mode=8 reason=3` after Power Off on a charger, unplug there switches off. Details: [Beta 8.40 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.40.md).

## Y2Linux 1.0 Beta 8.39, Baseline 153 — 2026-10-26 (published)

Release `1.0.0-beta.8.39`, tag `baseline-153`, Linux `1c599c5`, Reborn `7cf527d`, sequence 10470. Reborn only: Folders list folders then songs by file name with numbers in number order and play in that order, Shuffle is Off / Songs / Albums, playlists have a Sort, and a 120 000-song card was measured and made fast on the player (folder index, lists kept per library and made ahead with the screen off, Cover Flow 71 fps, playlists found by the scan instead of a 94-s walk per visit). Details: [Beta 8.39 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.39.md).

## Y2Linux 1.0 Beta 8.38, Baseline 146 — 2026-10-25 (published)

Release `1.0.0-beta.8.38`, tag `baseline-146`, Linux `4c79cdb`, Reborn `6c37d9f`, sequence 10310. Reborn only: on Bluetooth, Pause releases the output and Play opens a new stream (ledger F43, AirPods Pro 2: in-place BlueALSA resumes stayed silent), and the playing wave is anti-aliased and follows the music's loudness (three bands measured before the volume, timed by the output's delay), on Now Playing and Home. Details: [Beta 8.38 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.38.md).

## Y2Linux 1.0 Beta 8.37, Baseline 144 — 2026-10-25 (published)

Release `1.0.0-beta.8.37`, tag `baseline-144`, Linux `69f9f4c`, Reborn `69232c2`, sequence 10200. Reborn only: sleep timer lengths picked with the wheel (Y2Reborn #29, skins show the timer), the search goes back one level at a time, starts empty, finds playlists and shortens long sections with See All (#44), the playlist page keeps its focus on screen, and one way of scrolling everywhere (headers stay, only lists scroll). Labels 139–143 were device test builds. Details: [Beta 8.37 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.37.md).

## Y2Linux 1.0 Beta 8.36, Baseline 138 — 2026-10-25 (published)

Release `1.0.0-beta.8.36`, tag `baseline-138`, Linux `8d22ba1`, Reborn `92b9c9a`, sequence 10050. The open GitHub issues assessed in the code: own covers for songs without an album (Y2Reborn #43), the playing mark in skins' Up Next (#60), Up Next keeps the focused song (#32), joined genres split and joined artists read with commas (#40); one menu order everywhere and Customize choices (Cover Flow for albums and audiobooks, Album Artists, a seeking Now Playing wheel), genre-limited album pages, Add to Queue in Up Next; the Couldn't Start screen saves an error report onto Internal Storage. Label 137 (sequence 10002) was a device test build. Details: [Beta 8.36 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.36.md).

## Y2Linux 1.0 Beta 8.35, Baseline 136 — 2026-10-25 (published)

Release `1.0.0-beta.8.35`, tag `baseline-136`, Linux `fc733e8`, Reborn `e0921a0`, sequence 9902. Louder headphones, safe by default (report F45, FiiO FH7 too quiet at High): each Headphone Level has its own DAC Master (Low ≈0.35, Medium ≈0.71, High 1.73 Vrms at full volume, was 0.11/0.15/0.18), the volume steps are even in dB, and going past the old loudest output asks once (Raise the Volume?, again after 20 h of loud listening). Details: [Beta 8.35 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.35.md).

## Y2Linux 1.0 Beta 8.34, Baseline 135 — 2026-10-24 (published)

Release `1.0.0-beta.8.34`, tag `baseline-135`, Linux `88febab`, Reborn `01f1ed3`, sequence 9802. MTP no longer hangs when a computer connects (#61): uMTP's storage events were written under the mutex every request takes and waited for the host to read them; they are queued for their own thread now. Details: [Beta 8.34 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.34.md).

## Y2Linux 1.0 Beta 8.33, Baseline 134 — 2026-10-24 (published)

Release `1.0.0-beta.8.33`, tag `baseline-134`, Linux `0caf312`, Reborn `eca7f49`, sequence 9702 (8.32 was not published). Search is one page with the keys over it, folding into its results (owner request). Queue redesign: your queue plays first, queue edits/Shuffle/Repeat no longer restart the song (`Playback::set_upcoming`), Repeat All wraps on Next and Previous restarts the first song, Up Next with history, Move and Select Songs, queue actions for albums/artists/genres/folders/search, session schema 3 (queue by reference). Y2Reborn #38 artists of joined tags. Details: [Beta 8.33 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.33.md).

## Y2Linux 1.0 Beta 8.31, Baseline 130 — 2026-10-24 (published)

Release `1.0.0-beta.8.31`, tag `baseline-130`, Linux `b0b8ae6`, Reborn `b07cb9d`, sequence 9500. Settings → Sound → Balance (user request): Left +10 dB … Center … Right +10 dB, applied at the live sink gain by lowering the other side, jack and Bluetooth. Reborn only. Details: [Beta 8.31 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.31.md).

## Y2Linux 1.0 Beta 8.30, Baseline 129 — 2026-10-24 (published)

Release `1.0.0-beta.8.30`, tag `baseline-129`, Linux `e510867`, Reborn `44481c3`, sequence 9401. GitHub triage fixes: music queues never include audiobook parts (#58); a song picked on Songs is followed by the next row (Y2Reborn #21); Previous more than 3 s into a song restarts it (Y2Reborn #21); Bluetooth headphones with AVRCP absolute volume follow the player's volume through BlueZ's transport `Volume`, changes on the headphones come back, the wired volume is kept apart (Y2Reborn #22); the recovery screen's lines fit its 28 columns and long Reborn toasts take two lines (#55); the GC9503V panel powers down at screen-off by default (#45/#42). Details: [Beta 8.30 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.30.md).

## Y2Linux 1.0 Beta 8.29, Baseline 128 — 2026-10-24 (published)

Release `1.0.0-beta.8.29`, tag `baseline-128`, Linux `4d97301`, Reborn `e58980c`, sequence 9300. Charging (reports 09888d70/8fc8eea6/ba0bb428: a player never charged): an MT6323 without its die-temperature calibration fuse used to return no die temperature, which the charger took as an ADC fault and inhibited charging forever. It now uses the stock nominal coefficients read 10 °C high (derating and the 150 °C stops act early). Calibrated players are unchanged. Not run on an affected player yet. Details: [Beta 8.29 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.29.md).

## Y2Linux 1.0 Beta 8.28, Baseline 127 — 2026-10-23 (published)

Release `1.0.0-beta.8.28`, tag `baseline-127`, Linux `f3f938a`, Reborn `f6eb0b2`, sequence 9200. Wi-Fi (Y2Reborn #20: a wrong password was never said, the player showed "Connecting…" then "Saved"): the platform reports a wrong password as Failed until the next connect; Reborn tries a join before saving it, reopens the keyboard with the typed text and "Wrong password", keeps one entry per network and the other saved networks enabled, and offers Change Password. Checked on the owner's player (reproduced on 8.27 first). Details: [Beta 8.28 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.28.md).

## Y2Linux 1.0 Beta 8.27, Baseline 126 — 2026-10-23 (published)

Release `1.0.0-beta.8.27`, tag `baseline-126`, Linux `65e1c47`, Reborn `4947352`, sequence 9100. SD cards (F12, report 29ed4ccb: every card "Needs Repair" after a pull while mounted): a FAT32/exFAT card whose check finds errors plays read-only instead of being refused; Settings → Storage → Repair SD Card (owner-confirmed, charger or 30 %, a copy of the card's tables kept) repairs it on the player; a healthy card is read-only between writes (USB, playlist changes, reports, the firmware import open short windows), so taking it out during playback leaves it clean. Checked on the owner's player. Details: [Beta 8.27 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.27.md).

## Y2Linux 1.0 Beta 8.26, Baseline 125 — 2026-10-23 (published)

Release `1.0.0-beta.8.26`, tag `baseline-125`, Linux `518c641`, Reborn `404edb3`, sequence 9000. From the review of twelve uploaded reports (F35–F41): a player that turned off at 5 % no longer turns off again at every start on a charger (F36); Wi-Fi switched on after a sleep with Wi-Fi off connects at the first tap (F37); nonstandard chargers get 450 mA instead of 70 mA (F38); every shutdown step goes to pstore and the journal writes get 3 s (F39); a Wi-Fi re-association no longer warns (F35); reports record more about "network not found" (F13) and refused SD cards (F12) and keep version strings (F41). Installed and checked on the owner's player (F37 reproduced on 8.25 first). Details: [Beta 8.26 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.26.md).

## Y2Linux 1.0 Beta 8.25, Baseline 124 — 2026-10-23 (published)

Release `1.0.0-beta.8.25`, tag `baseline-124`, Linux `f7f23d4`, Reborn `40386bc`, sequence 8901. #52/#54 on 8.24: both players' CS43131 crystals flagged XTAL_ERR right at power-up (not a PLL problem). Stock starts the crystal with the chip powered (`PWDN_CTL=0`); Y2Linux powered only the clocks. Each DAC power-up now starts it with the chip powered except the headphone amplifier (which made static), retries with a 500 ms rail cycle up to three times, and the first song after a failed power-up gets one more cold start. Test switches `y2_xtal_full_power`, `y2_xtal_start_hp`, `y2_xtal_quiet_start` and `echo cycle > y2_hp/xtal` for the reporters. Installed and tested on the owner's player. Confirmed by both reporters on 2026-10-23 (#54 report: `tries=1 ready_ms=30 errors=0`; #52 and #54 closed). Details: [Beta 8.25 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.25.md), [analysis handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FISSUE-52-54-CRYSTAL-HANDOFF.md).

## Y2Linux 1.0 Beta 8.24, Baseline 123 — 2026-10-23 (published)

Release `1.0.0-beta.8.24`, tag `baseline-123`, Linux `2a21690`, Reborn `e199d9c`, sequence 8800. #52: every failure of the reporter's player was a 48 kHz start through the CS43131's PLL, which stock never runs (stock output: 44.1 kHz only). The headphone output now runs at 44.1 kHz only, Reborn converts other rates, the codec refuses rates the crystal does not clock, and a crystal error at a stream start power-cycles the codec. Installed and tested on the owner's player. Details: [Beta 8.24 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.24.md).

## Y2Linux 1.0 Beta 8.23, Baseline 122 — 2026-10-22 (published)

Release `1.0.0-beta.8.23`, tag `baseline-122`, Linux `e3195fd`, Reborn `0779d8b`, sequence 8705. F34: a recovery install that stops making progress (the "Step 1 of 4" freeze) restarts the player through the SoC watchdog and leaves its trail in `/data/logs/recovery-previous-boot.txt`. #52/#54: the CS43131 powers up as stock (crystal, PLL and CLKOUT together, crystal selected 20 ms later, DAC rails in one burst), stays powered while the screen is on (`y2_hp/hold`), and Reborn keeps the headphone output open across same-format track changes. Installed and tested on the owner's player. Details: [Beta 8.23 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.23.md).

## Y2Linux 1.0 Beta 8.22, Baseline 121 — 2026-10-22 (published)

Release `1.0.0-beta.8.22`, tag `baseline-121`, Linux `073aa0c`, Reborn `e196033`, sequence 8607. Fixes from the review of all pending reports (F23–F32) and #53: update health boots leave a reset-surviving stage trail and evidence in `/data/updates/health`, the recovery stops its UI and backlight before restarting; a play right after waking is no longer refused as busy; Bluetooth recovers from an interrupted codec switch; one kernel WARN no longer blocks sleep; an interrupted download no longer leaves "Downloading Update…" forever; the date and time can be set by hand; the headphone crystal runs as stock runs it (#52/#54: started at boot, kept two idle minutes, no clock switch per track). Installed and tested on the owner's player. Details: [Beta 8.22 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.22.md).

## Y2Linux 1.0 Beta 8.21, Baseline 120 — 2026-10-22 (published)

Release `1.0.0-beta.8.21`, tag `baseline-120`, Linux `2e914d6`, Reborn `cdc6b43`, sequence 8500. #52/#54: the CS43131 crystal now runs as stock runs it (stock never waits for or reads its ready/error flags): it starts when the codec powers up, stops only with the rails, a stream waits until it has run 1 s and then uses it anyway; no automatic 15 µA boost, no rail cycle; codec autosuspend 5 s. Installed and tested on the owner's player before publishing. Details: [Beta 8.21 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.21.md).

## Y2Linux 1.0 Beta 8.20, Baseline 119 — 2026-10-22 (published)

Release `1.0.0-beta.8.20`, tag `baseline-119`, Linux `0f0b4ed`, Reborn `cdae78e`, sequence 8400. #52: a CS43131 crystal that fails to start or stops while running gets the chip's strongest bias (15 µA) for the boot (one player's crystal flags XTAL_ERR at the stock 12.5 µA); Reborn waits 5 s for an open (the kernel's rail cycle and its own second open); reports collect `y2_hp/xtal`. Installed and tested on the owner's player before publishing (stock and forced 15 µA). Details: [Beta 8.20 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.20.md).

## Y2Linux 1.0 Beta 8.19, Baseline 118 — 2026-10-21 (published)

Release `1.0.0-beta.8.19`, tag `baseline-118`, Linux `6649c89`, Reborn `da5b777`, sequence 8302 (8.18 was a test build, never published). Audiobooks: their own Home entry, chapters from the files' marks or one per file, the place kept per book with a rewind, speed 0.75–2× (FFmpeg `atempo`), a sleep timer; long M4B books play (FFmpeg allocation ceiling 128 MiB). Sharper covers (180/128 px, crop, Lanczos, smaller copies), Settings → Customize (wrap-around lists, screen-off buttons). Installed on the owner's player before publishing. Details: [Beta 8.19 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.19.md).

## Y2Linux 1.0 Beta 8.17, Baseline 114 — 2026-10-21 (published)

Release `1.0.0-beta.8.17`, tag `baseline-114`, Linux `8719042`, Reborn `6d5458c`, sequence 8100. User reports and #51: the headphone crystal keeps running between songs as on stock (no more `ALSA -110` until a reboot), SD cards with findings Windows mounts over are admitted, output leaves Bluetooth when headphones drop, Bluetooth search and Connect no longer fail while busy, SBC lowers its bitpool on a weak link, update checks retry after a failure. Details: [Beta 8.17 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.17.md).

## Y2Linux 1.0 Beta 8.16, Baseline 113 — 2026-10-20 (published)

Release `1.0.0-beta.8.16`, tag `baseline-113`, Linux `342a130`, Reborn `eea9312`, sequence 8000. Large libraries (report from a 28 600-song card): All Songs plays again (queue window of 5 000, random part for Shuffle), a rescan with no changes no longer spends 12.5 min in one database statement, and new files' tags are read on three cores. Details: [Beta 8.16 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.16.md).

## Y2Linux 1.0 Beta 8.15, Baseline 112 — 2026-10-20 (published)

Release `1.0.0-beta.8.15`, tag `baseline-112`, Linux `326d924`, Reborn `2ef41d3`, sequence 7900. Japanese, Chinese and Korean text from Noto Sans CJK through a runtime glyph page; a Check for Updates waits for Wi-Fi after a wake, retries, and keeps a release it already offered (Update Now vanished after a failed check); a Bluetooth codec choice made while headphones connect is tried again. Not installed on a player before publishing (owner updates by OTA). Details: [Beta 8.15 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.15.md).

## Y2Linux 1.0 Beta 8.14, Baseline 111 — 2026-10-20 (published)

Release `1.0.0-beta.8.14`, tag `baseline-111`, Linux `8e21366`, Reborn `5cda8bb`, sequence 7800. User requests and one report: every shuffle now gets a fresh random order (the seed came from the track ID), a held seek starts at 1 s and grows to 3 s and 10 s (was 30 s per step), a Shuffle row on a genre, the Home card's long titles end with "…", and the guarded internal eMMC no longer advertises TRIM, so the Internal Storage setup's zero-out writes zeros instead of an erase the guard rejected (false `storage_error` report). Build 111 installed and checked on the maintainer's player. Details: [Beta 8.14 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.14.md).

## Y2Linux 1.0 Beta 8.13, Baseline 110 — 2026-10-20 (published)

Release `1.0.0-beta.8.13`, tag `baseline-110`, Linux `1a92e05`, Reborn `21cd3b0`, sequence 7701. From five uploaded reports and two user messages: music files over USB (MTP) now carry their format and tags from Reborn's library, so libmtp track clients such as Strawberry list the songs on Internal Storage and the SD card (`mtp-tracks`: 0 → 311 on the maintainer's player); the Wi-Fi driver hands the connected BSS to cfg80211 (a dropped connection with a `sme.c:845` warning); no `Errno 22` line at every boot. Pause/resume silence was the #48 crystal path, fixed in 8.12 and checked on a player. Build 110 installed and checked on the maintainer's player. Details: [Beta 8.13 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.13.md).

## Y2Linux 1.0 Beta 8.12, Baseline 108 — 2026-10-20 (published)

Release `1.0.0-beta.8.12`, tag `baseline-108`, Linux `570ed90`, Reborn `90f3da6`, sequence 7601. Fixes from #48, #49 and 16 uploaded reports: an M3U line with a multi-byte character across byte 8 crashed Reborn at every start (crash loop, garbled screen, update rollback), now parsed safely and any panic on one user file is isolated; the CS43131 crystal gets a retry and a failed clock fails the open instead of playing silence; a CPU parked just before suspend no longer fails the PM prepare chain and such a refusal is retried, not quarantined; the loader-display SMI hold checks with the clock provider active; reports collect `/proc`/debugfs and send one report per check; Couldn't Start after five failed starts. Test build 107 checked on the maintainer's player; 108 not installed. Details: [Beta 8.12 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.12.md).

## Y2Linux 1.0 Beta 8.11, Baseline 106 — 2026-10-20 (published)

Release `1.0.0-beta.8.11`, tag `baseline-106`, Linux `9c7f079`, Reborn `727fd47`, sequence 7500. The automatic Internal Storage setup on battery needs 25 % read from the power-on OCV (was 3.7 V under the boot load, ≈45 %), and a setup waiting for the battery says Connect a charger and restart instead of Restart to finish setting up (user report 20261019-153610: restarts on battery never set it up). Not installed on a player before publishing. Details: [Beta 8.11 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.11.md), [Storage](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FSTORAGE.md).

## Y2Linux 1.0 Beta 8.10, Baseline 105 — 2026-10-19 (published)

Release `1.0.0-beta.8.10`, tag `baseline-105`, Linux `9df5ccf`, Reborn `cfac12b`, sequence 7400. Charging no longer refuses charger settings left by other software (#47: CV 4.1875 V blocked every charger); opt-in error reports over Wi-Fi to the Cloudflare receiver (budgeted inside R2's free tier); no topic, live report progress; fewer false triggers. Details: [Beta 8.10 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.10.md), [user guide](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FERROR-REPORTS.md).

## Y2Linux 1.0 Beta 8.9, label 102 — 2026-10-19 (built, on the owner's player, not published)

Release `1.0.0-beta.8.9` (no tag), Linux `0e0760f`, Reborn `4da5f84`, sequence 7100. Save Report asks only for the storage and saves at once; the topic step is gone (it never changed what a report holds). No platform code change. Details: [Beta 8.9 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.9.md), [user guide](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FERROR-REPORTS.md).

## Y2Linux 1.0 Beta 8.8, Baseline 101 — 2026-10-19 (published)

Release `1.0.0-beta.8.8`, tag `baseline-101`, Linux `be71b6d`, Reborn `b6b6fbc`, sequence 7000. Error reports can be saved: About & Updates → Error Reports → Save Report writes the scrubbed report to `Error Reports/` on Internal Storage (`/media/internal/music`) or the SD card in ≈10 s (4 worker processes, nice 10); no uploader yet, so the switch and the question stay hidden. Details: [Beta 8.8 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.8.md), [user guide](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FERROR-REPORTS.md).

## Y2Linux 1.0 Beta 8.7, Baseline 95 — 2026-10-18 (published)

Release `1.0.0-beta.8.7`, tag `baseline-95`, Linux `f7b4fb5`, Reborn `82fe089`, sequence 6900. LK's `gc9503v` panel name counts with either `lcm=` digit (stock LK names the first driver whose compare_id matched), so GC9503V players are identified (#45/#46); the GC9503V power-down stays opt-in. Details: [Beta 8.7 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.7.md).

## Y2Linux 1.0 Beta 8.6, Baseline 94 — 2026-10-18 (published)

Release `1.0.0-beta.8.6`, tag `baseline-94`, Linux `fd32cdb`, Reborn `cefcc8a`, sequence 6800. Audio playback review: the headphone level is written under DAPM's lock, `hpload_measure` refuses an open stream, fades carry over restarts and louder sound settings fade in, held pauses take new settings, an equalizer no longer holds the CPU at 747.5 MHz, one filter-graph thread, preamp over 44.1–384 kHz. On the owner's player as test build 94. Details: [Beta 8.6 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.6.md).

## Y2Linux 1.0 Beta 8.5, Baseline 93 — 2026-10-18 (published)

Release `1.0.0-beta.8.5`, tag `baseline-93`, Linux `04e2dc8`, Reborn `b694670`, sequence 6752. Headphone output level (kernel `HP Output Level`, default Low = stock, written only while the amplifier is down; Master −19.5 dB), headphone profiles (AutoEq, 47 shipped, FFmpeg lowshelf/highshelf), DAC filter, Sound on one screen with an Output page. On the owner's player as test build 93. Details: [Beta 8.5 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.5.md), [Headphone output](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FHEADPHONE-OUTPUT.md).

## Y2Linux 1.0 Beta 8.4, Baseline 90 — 2026-10-18 (published)

Release `1.0.0-beta.8.4`, tag `baseline-90`, Linux `c339919`, Reborn `000876f`, sequence 6700. The dark display after a restart (the 8.3 OTA rolled back for it) is the leftover closed SMI gate of POWER-FINAL-40: no SMI hold at probe, larb0 stuck from LK, DSI reads lagging as a consequence. 42's restart handler (reopen SMI common/larb0 as the last step before the watchdog) is back next to 43's hold. Not yet run on a player. Details: [Beta 8.4 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.4.md).

## Y2Linux 1.0 Beta 8.3, Baseline 89 — 2026-10-18 (published)

Release `1.0.0-beta.8.3`, tag `baseline-89`, Linux `029d93e`, Reborn `03e6dff`, sequence 6600. The installer estimates its own time left from a model of its phases (owner's player) corrected by the measured rates; the recovery screen and Reborn's check step show the seconds, and the bar moves with time. The kept root is hashed in parallel with verify, and each install records its phase timings in the journal. Not yet run on a player (the owner installs it over the air). Details: [Beta 8.3 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.3.md).

## Y2Linux 1.0 Beta 8.2, Baseline 88 — 2026-10-18 (published)

Release `1.0.0-beta.8.2`, tag `baseline-88`, Linux `1d463f6`, Reborn `5aad5f1`, sequence 6501. Faster updates (OTA-50): the root payload is a segmented gzip that the recovery decodes, backs up and reads back on four cores, and the acknowledged package stays on Y2DATA as the next install's rollback copy. On the owner's player the installer took 14.9 s (Beta 8.1: 53.5 s; 23.6 s when it has to back up the live root). Rollback from a kept package is host-tested only. Details: [Beta 8.2 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.2.md).

## Y2Linux 1.0 Beta 8.1, Baseline 86 — 2026-10-18 (published)

Release `1.0.0-beta.8.1`, tag `baseline-86`, Linux `78220dc`, Reborn `a558870`, sequence 6463. The panel finally powers down at screen-off (#45): the Y2 ships with a GC9503V or an ST7701S panel (stock kernel and LK, REA); Y2Linux identifies it (LK's `lcm=1-`, the stock ID reads, a Y2DATA record) and uses the stock init and power-down. On by default for the ST7701S (owner's player, confirmed), opt-in for the GC9503V. Sleep effect not measured yet. Details: [Beta 8.1 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.1.md).

## Y2Linux 1.0 Beta 8.0, Baseline 75 — 2026-10-18 (published)

Release `1.0.0-beta.8.0`, tag `baseline-75`, Linux `662ff11`, Reborn `1b3a5c1`, sequence 6400. Fixes from the 1.0 review: one unreadable song no longer rolls an update back or stops pruning (B3/B4), SD cards whose check is slow mount (B5), settings survive a rollback (B7), a stuck installer powers off on battery (B8), safer receive-DMA fallback (B6), toolchain sources in the release (A7), the real install guide in the packages. Installed on the owner's player by OTA, acknowledged, the broken-file case checked on the device. Details: [Beta 8.0 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.0.md).

## Y2Linux 1.0 Beta 7.11, Baseline 74 — 2026-10-17 (published)

Release `1.0.0-beta.7.11`, tag `baseline-74`, Linux `9c3e4f1`, Reborn `814cd14`. Copies to the player about three times faster: multi-packet receive DMA for USB (Internal Storage 29.6 MB/s instead of ≈10, SD 23.3 MB/s), measured with every byte hashed on the owner's player; Dolphin copies confirmed. Details: [Beta 7.11 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.11.md).

## Y2Linux 1.0 Beta 7.10, Baseline 73 — 2026-10-17 (published)

Release `1.0.0-beta.7.10`, tag `baseline-73`, Linux `72a565d`, Reborn `511dbf0`. USB file operations: the musb crash on packet-aligned MTP transfers (zero-length packet, Beta 7.9 oops) is fixed; moving and copying on the player (MoveObject, CopyObject) for Windows Explorer and libmtp hosts. Beta 7.9's automatic Internal Storage passed on the owner's player. Details: [Beta 7.10 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.10.md).

## Y2Linux 1.0 Beta 7.9, Baseline 72 — 2026-10-17 (published)

Release `1.0.0-beta.7.9`, tag `baseline-72`, Linux `2ac6abd`, Reborn `926ef45`. Every player gets Internal Storage (Y2MEDIA) by itself at start, keeping up to 400 MB of old files in Old Player Files (a larger library waits, shown read-only as Old Storage); the radio firmware copy goes into Internal Storage's Firmware folder (#39); pulled FAT SD cards mount again (#44). Details: [Beta 7.9 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.9.md).

## Y2Linux 1.0 Beta 7.8, Baseline 71 — 2026-10-16 (published)

Release `1.0.0-beta.7.8` (Reborn `1.0.0-beta.7.8`), tag `baseline-71`, Linux `21d5ba0`, Reborn `35a3d56`. Beta 7.7's scrobbling worked on the owner's player (QR sign-in, real scrobble on last.fm). Fixes: Now Playing again after a pause or repeat, an invalid play no longer blocks sending, sign-in waits for a trusted clock, Last.fm/radio/clock/platform events reach the log again. Details: [Beta 7.8 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.8.md).

## Y2Linux 1.0 Beta 7.7, Baseline 70 — 2026-10-16 (published)

Release `1.0.0-beta.7.7` (Reborn `1.0.0-beta.7.7`), tag `baseline-70`, Linux `bcb7815`, Reborn `f117586`. Last.fm scrobbling: sign-in by QR code, offline queue, Now Playing, optional `.scrobbler.log`. Details: [Beta 7.7 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.7.md).

## Y2Linux 1.0 Beta 7.6, Baseline 67 — 2026-10-16 (published)

Release `1.0.0-beta.7.6` (Reborn `1.0.0-beta.7.6`), tag `baseline-67`, Linux `58de7d8`, Reborn `36e6994`. The update download and check draw at the full frame rate (were ≤ 29 fps) with a Download · Check · Install step tracker. Details: [Beta 7.6 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.6.md).

## Y2Linux 1.0 Beta 7.5, Baseline 66 — 2026-10-16 (published)

Release `1.0.0-beta.7.5` (Reborn `1.0.0-beta.7.5`), tag `baseline-66`, Linux `2ec56d2`, Reborn `0291d69`. Larger status bar with the screen's name beside the back arrow, a Home header, larger messages; Theme is now Settings → Skin. Details: [Beta 7.5 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.5.md).

## Y2Linux 1.0 Beta 7.4, Baseline 65 — 2026-10-16 (published)

Release `1.0.0-beta.7.4` (Reborn `1.0.0-beta.7.4`), tag `baseline-65`, Linux `d909231`, Reborn `8c0f8c4`. Messages as a slim pill in the status bar with an icon; the playing wave no longer holds the CPU lease. Motion measured on 7.3: 62 fps median while moving, 64–65 fps wave, 0 missed frames. Details: [Beta 7.4 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.4.md).

## Y2Linux 1.0 Beta 7.3, Baseline 64 — 2026-10-16 (published)

Release `1.0.0-beta.7.3` (Reborn `1.0.0-beta.7.3`), tag `baseline-64`, Linux `cbab171`, Reborn `7175c76`. A computer connecting shows a message and a USB symbol in the status bar instead of a screen that covered the player. Details: [Beta 7.3 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.3.md).

## Y2Linux 1.0 Beta 7.2, Baseline 63 — 2026-10-16 (published)

Release `1.0.0-beta.7.2` (Reborn `1.0.0-beta.7.2`), tag `baseline-63`, Linux `78b548b`, Reborn `846da2d`. Reborn motion at 60 fps (gliding focus, smooth lists, screen slides, sheets, fades, switches) and a travelling wave for the Now Playing progress. Device frame rate to be measured. Details: [Beta 7.2 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.2.md).

## Y2Linux 1.0 Beta 7.1, Baseline 62 — 2026-10-16 (published)

Release `1.0.0-beta.7.1` (Reborn `1.0.0-beta.7.1`), tag `baseline-62`, Linux `e9427a9`, Reborn `81a907e`. One-step update (Update Now: download, check, restart; Cancel during the download), Check for Updates answers at once, the computer screen follows the cable on every screen and stays while connected, automatic time zone over Wi-Fi with a country-first picker. Details: [Beta 7.1 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.1.md).

## Y2Linux 1.0 Beta 7, Baseline 61 — 2026-10-16 (published)

Release `1.0.0-beta.7` (Reborn `1.0.0-beta.7`), tag `baseline-61`, Linux `7c0ee9f`, Reborn `7ade64b`. Reborn UI v4: one fixed accent, one focus row, button and empty state; Home with a Music menu and Home Menu pins; hint lines and developer details removed. Platform: the CPU thermal zone survives sleep (it was disabled after the first INFRA power-down), and a Power sleep is no longer refused by a battery notification. Overnight on 6.3: ≈7.8 mA. Details: [Beta 7 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-7.md).

## Y2Linux 1.0 Beta 6.3, Baseline 60 — 2026-10-16 (published)

Release `1.0.0-beta.6.3` (Reborn `1.0.0-beta.6.3`), tag `baseline-60`, Linux `b20404c`, Reborn `b18d98c`. Reborn fix: Power while paused was refused ("finishing another task") because the held sink's activity lease blocked the platform's lock check; a sleep request now releases the held pause first. Details: [Beta 6.3 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-6.3.md).

## Y2Linux 1.0 Beta 6.2, Baseline 59 — 2026-10-16 (published)

Release `1.0.0-beta.6.2` (Reborn `1.0.0-beta.6.2`), tag `baseline-59`, Linux `8e07f47`, Reborn `f0f1091`. Reborn: a status-bar clock with a Time Zone setting (PR #10), the clock and today's screens (radio, Station Info, keyboard, Favorites heart) in every skin, and a sixteenth skin, Bunny Bow (pixel art, Pixelify Sans). Details: [Beta 6.2 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-6.2.md).

## Y2Linux 1.0 Beta 6.1, Baseline 58 — 2026-10-16 (published)

Release `1.0.0-beta.6.1` (Reborn `1.0.0-beta.6.1`), tag `baseline-58`, Linux `faf85ba`, Reborn `78e36db`. Reborn fixes: sound after pause/resume on Bluetooth (drain instead of BlueALSA pause), Next/Previous while a song starts, SD card songs listed twice under a pre-CID source id (Y2Reborn #15, #14). Details: [Beta 6.1 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-6.1.md).

## Y2Linux 1.0 Beta 6, Baseline 57 — 2026-10-15 (published)

Release `1.0.0-beta.6` (Reborn `1.0.0-beta.6`), tag `baseline-57`, Linux `45d3696`, Reborn `544d3c9`. Reborn: Playlists (the .m3u8 file is the playlist; made and changed on the player; Favorites with a heart), pause in place (instant resume, wired and Bluetooth) and collected seeking. Details: [Beta 6 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-6.md).

## Y2Linux 1.0 Beta 5.1, Baseline 56 — 2026-10-15 (published)

Release `1.0.0-beta.5.1` (Reborn `1.0.0-beta.5.1`), tag `baseline-56`, Linux `e9ac2a5`, Reborn `35e333d`. Reborn: live library search with a ~130× faster index, and Radio as its own section (station logos, Station Info, LIVE badges, A–Z lists with each country's top 10 on top, Previous/Next between stations). Details: [Beta 5.1 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-5.1.md).

## Y2Linux 1.0 Beta 5, Baseline 55 — 2026-10-15 (published)

Release `1.0.0-beta.5` (Reborn `1.0.0-beta.5`), tag `baseline-55`, Linux `5dd995f`, Reborn `84df9ae`. Reborn only: a full-screen keyboard driven by the buttons (Wi-Fi password, station search, library search), library search (Home → Search) and a UI pass over every screen. Details: [Beta 5 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-5.md).

## Y2Linux 1.0 Beta 4.1, Baseline 54 — 2026-10-15 (published)

Release `1.0.0-beta.4.1` (Reborn `1.0.0-beta.4.1`), tag `baseline-54`, Linux `929ea0d`, Reborn `d0008dd`. Fixes from Beta 4 on the player: stopping or pausing a station no longer hangs playback ("playback command queue full"); Wi-Fi no longer shows as not connected after screen-off (late platform record); update checks work right after deep sleep (TLS clock compared with `CLOCK_BOOTTIME`). Details: [Beta 4.1 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-4.1.md).

## Y2Linux 1.0 Beta 4, Baseline 53 — 2026-10-15 (published)

Release `1.0.0-beta.4` (Reborn `1.0.0-beta.4`), tag `baseline-53`, Linux `d681990`, Reborn `94eae20`. Internet radio in Reborn (radio-browser.info directory, own `.m3u`/`.pls` lists, favorites, search, live song titles); the player's `curl` receives streams and FFmpeg stays built without networking. Device checks owed after the OTA install. FM radio next. Details: [Beta 4 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-4.md).

## Y2Linux 1.0 Beta 3, Baseline 52 — 2026-10-15 (published)

Release `1.0.0-beta.3` (Reborn `1.0.0-beta.3`), tag `baseline-52`, Linux `2731169`, Reborn `8cd4362`. AAC with the FDK afterburner up to the peer's rate within one packet per frame (AirPods 256 kbit/s; Beta 2: 220 kbit/s CBR) and an adaptive AAC bit rate (BlueALSA patch 0002, 256 → 128 kbit/s under congestion); AAC encoder state in the platform status; SBC XQ without the experimental switch; service-menu rows AAC Quality / AAC Auto Rate. First release through `tools/production/release.py` (119 s). Device listening and range checks owed. Details: [Beta 3 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-3.md).

## Y2Linux 1.0 Beta 2, Baseline 51 — 2026-10-15 (published)

Release `1.0.0-beta.2` (Reborn `1.0.0-beta.2`), tag `baseline-51`, Linux `fc1f5ea`, Reborn `009cd32`. Bluetooth/Wi-Fi review of Beta 1 (archive `20261016/155` and the live player): BTIF receive acknowledges before draining (every BTIF timeout on record had the WMT reply unread in the ring); the controller page timeout is set to 5.12 s; `y2-bt-reconnect` waits 45 s for BlueZ instead of inhibiting all reconnects after a 10 s client timeout; DNS re-check every 5 min instead of 30 s; sleep no longer counts as a Wi-Fi link loss; Bluetooth class Portable Audio. Reborn: the output follows the headphones (Bluetooth wins over the jack); Wi-Fi passwords with `\` or `"` work. Published without a device test first (owner: OTA only). Details: [Beta 2 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-2.md).

## Y2Linux 1.0 Beta 1, Baseline 50 — 2026-10-16 (published: first public beta)

Release `1.0.0-beta.1` (Reborn `1.0.0-beta.1`), tag `baseline-50`: first-install images, the signed update and the GPL sources on GitHub. 49 plus the firmware watcher and radio restart fixes and Reborn's cancel/failure precedence fix. Known gaps: sleep ≈8.3 mA (stock ≈1.3), rare slow display start after a restart, USB after deep-sleep wake, Bluetooth reconnect, AAC with AirPods unconfirmed, install from stock run on one player. Details: [Beta 1 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-1.md).

## POWER-FINAL-49 firmware-free public images, Baseline 49 — 2026-10-16 (published)

Release `baseline-49` (Linux `b4610ea`, Reborn `ceb6313`): first-install images for SP Flash Tool (BOOTIMG, RECOVERY, system, data without SSH key), the signed update and the GPL sources. No image carries the MediaTek radio firmware: updated players keep theirs (the recovery copies it to Y2DATA), new players take it from the owner's `system.img` on the Firmware drive. Public Bluetooth codecs: SBC, AAC (fdk-aac-free), LDAC; aptX only in owner-private builds. Merged contributions #38 (Y2Linux), #6–#8 (Y2Reborn). Suite 727. Physical: installed over Wi-Fi; firmware kept by the recovery, radios up from `/data/firmware`, recovery screen lit (archive `20261016/153`). Details: [49 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-49.md).

## POWER-FINAL-48 download screen, Baseline 48 — 2026-10-16 (published)

`out/y2linux-platform-v1-power-final-candidate-48/` (Linux `d5cc381`, Reborn `62af097`; BOOTIMG `5a1fa90e…d74b`, Y2ROOT `1d7c4bca…e047`, RECOVERY `6c14a2f7…0a3f`), fallback 47; git tag and GitHub release `baseline-48`. The update download shows its step, percentage, a gliding bar, MB, speed and time left (live progress in `/run/y2`), checks the package once instead of twice (about 12 s less), runs at low priority, and turns to Ready to Install with a notice when done. Contains 47 (DSI DCM off). Suite 718. Physical: 48 installed over Wi-Fi, recovery screen lit; five restart-entered recovery probes all lit and returned on their own (archive `20261016/151`). The DSI read lag still occurs (2 of 5 entries) but no longer stops the picture; its own cause is open. Details: [48 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-48.md).

## POWER-FINAL-47 DSI clock gating off, Baseline 47 — 2026-10-16 (published)

`out/y2linux-platform-v1-power-final-candidate-47/` (Linux `ba7a003`, Reborn `850687d`; BOOTIMG `97f2ef87…e280`, Y2ROOT `efb3f4e6…0bce`, RECOVERY `4293cfca…ce35`), fallback 46; git tag and GitHub release `baseline-47`. 46 installed over Wi-Fi from its release (archive `20261016/150`) but its recovery screen stayed dark: the DSI register reads lag from Linux's first modeset, not from the hand-over, and power-cycling the DSI does not clear it. 47 keeps MMSYS DCM off for DSI/DPI (stock enables DCM only once, while its display streams) and lets `probe-recovery` restart, for repeated recovery-screen tests. Suite 718. Physical: pending (install, then five recovery probes). Details: [47 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-47.md).

## POWER-FINAL-46 update space, restart by default, Baseline 46 — 2026-10-16 (published)

`out/y2linux-platform-v1-power-final-candidate-46/` (Linux `d03ab29`, Reborn `850687d`; BOOTIMG `d5bacc9e…583f`, Y2ROOT `e8dde2d1…d87a`, RECOVERY `476567c5…e1e2`), fallback 45; git tag `baseline-46` in both repositories and the first GitHub release on the update channel (signed with `platform-v1-release-20261015`). Since Baseline 34: over-the-air updates through a Y2 recovery image (35–38: install in about a minute, verified readback, automatic rollback), software restart fixed (43: SMI hold for the loader's display), display read-lag retry (44), the installer screen visible on a restart entry (45), and in 46 space for every update (stale package and disposable logs removed before a download, rollback copies counted as free, refusal names the MB) and restart into the installer and back by default. Suite 718. Physical: 45 installed over the air without a cable or Power press (archive `20261016/149`); 46 awaits its Wi-Fi install from the release. Details: [46 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-46.md).

## POWER-FINAL-34 shipped themes, battery display, Baseline 34 — 2026-10-14 (published)

`out/y2linux-platform-v1-power-final-candidate-34/` (Linux `de62fa9`, Reborn `5b69ef5`; BOOTIMG `ee80a82c…c30c`, Y2ROOT `9d3e93c1…ff6c`), fallback 33; git tag `baseline-34` in both repositories. 15 Reborn themes shipped in `/usr/share/reborn/skins` (Classic, Nano Glass, Walkman, Terminal, Winamp, Paper, Big Type, Cassette, Neon Night, Zune, Mini Silver/Pink/Blue/Green/Gold; OFL fonts); skin fonts may carry ASCII only and text may be lowercased (Zune). Reborn shows the battery level again: since 29 the platform reports the source `stock_oam`, which Reborn ignored (seen on the 33 device capture as an empty battery). Suite 715. Physical: 13 of the themes loaded on the 33 device (87–119 ms each, trial copies in `Themes`); 34 itself awaits the owner's flash (battery level, Zune). Details: [34 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-34.md).

## POWER-FINAL-33 Reborn themes — 2026-10-14 (installed)

`out/y2linux-platform-v1-power-final-candidate-33/` (Linux `b42a391`, Reborn `76e681d`; BOOTIMG `1d19f288…3eb2`, Y2ROOT `2d9b07a6…7788`), fallback 32; contains 27–32. Skin engine in Reborn (format, strict validation, skin atlas texture, TTF fonts, live picker in Settings → Display → Theme, `Themes` folders on Internal Storage and the SD card, `rebornctl theme`), the Classic skin, and Reborn's own look unchanged when no skin is chosen. Suite 713. Physical: installed; owner: "it works very good"; Classic loaded in 162 ms. Details: [33 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-33.md), authoring guide in Y2Reborn `docs/skins.md`.

## POWER-FINAL-27 to 32 — 2026-10-14
  - 27 stock panel power-down, VGP2 off when the DAC idles, VSYS buck sleep mode (switches in

`power-features.json`); installed (archive 125), overnight drain not yet measured. [27 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-27.md)
  - 28/29 stock battery percentage (UI SOC, power-on OCV, kept across restarts) and stock top-off (450 → 200 →

70 mA finish, plateau completion, 3 h budget); 29 installed, full charge qualified (archive 127: rest 4.128 V, display 100, no fault). [28](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-28.md), [29](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-29.md)
  - 30 plugged exFAT/FAT/ext4 directory readahead (cold SD scan measured ≈7 s on 29), `noatime`, Reborn limiter

only when the DSP can raise a peak; never flashed alone, contained in 33; cold-scan time not yet re-measured. [30 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-30.md)
  - 31 folder-first artwork, more cover names, `.m4b/.oga/.aifc`, `ALBUM ARTIST`; contained in 33.

[31 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-31.md)
  - 32 deep idle during screen-off playback (`deep_idle_audio`); contained in 33; the wired screen-off playback test

(xruns, idle counters) is still owed. [32 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-32.md)

## POWER-FINAL-26 Bluetooth codec auto-selection — 2026-10-13 (installed)

`out/y2linux-platform-v1-power-final-candidate-26/` (Linux `64b3cc4`, Reborn `1c9edd4`; BOOTIMG `f4ca442b…585a`, Y2ROOT `66efd3ed…405f`), fallback 25. Reborn matched BlueALSA 5.0's `A2DP-source:` codec prefix only in lower case, so no codec counted as available and the codec choice was hidden (BlueZ still negotiated AAC by itself); 26 matches it case-insensitively, defaults to Auto (LDAC → aptX-HD → aptX → AAC → SBC) and moves the old SBC default to Auto once. Suite 693. Physical: installed; the first boot could not play because the AirPods never connected (the platform reconnect timed out twice and is inhibited until a manual connect; unchanged code). Manual connect, Auto → AAC without a link drop, and the overnight sleep test are pending. Details: [26 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-26.md).

## POWER-FINAL-25 Cover Flow frame gate, card hygiene — 2026-10-13 (installed)

`out/y2linux-platform-v1-power-final-candidate-25/` (Linux `f7eb741`, Reborn `ed6a8cb`; BOOTIMG `44a9c3cf…3cf7`, Y2ROOT `6f629a89…8f67`), fallback 24. 24's 27 fps came from the render gate still requiring 34 ms between frames; 25 uses 12 ms while Cover Flow glides and holds the Interactive CPU lease, caches album detail, shows sub-minute albums as m:ss and skips macOS `._*` files and system folders. Physical: healthy; the owner's card scans complete (311 files, 0 failures); Cover Flow frame rate not yet measured. Details: [25 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-25.md).

## POWER-FINAL-24 animation frame pacing, Baseline 24 — 2026-10-13 (previous baseline)

`out/y2linux-platform-v1-power-final-candidate-24/` (Linux `d2b38e8`, Reborn `ced5199`; BOOTIMG `653c7d85…dda7`, Y2ROOT `21f21e47…860b`), fallback 23. On 23 Cover Flow looked right but ran at ≈10 fps although frames cost only 3–17 ms: the main loop slept its idle wait between wheel events. 24 paces animation frames at the panel rate. Suite 693; package checks PASS. Physical: installed; Cover Flow 27 fps median (31 max, half the panel rate; CPU-bound at the low clock); the white shutdown screen is gone (21); the start-up flash fix (22) is not yet confirmed by the owner. Sleep tests on 19–24 still pending. Tagged `baseline-24`. Details: [24 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-24.md).

## POWER-FINAL-23 Reborn Cover Flow and Genres — 2026-10-13 (installed; ≈10 fps → 24)

`out/y2linux-platform-v1-power-final-candidate-23/` (Linux `7f5445d`, Reborn `83c9127`, root `2026.08-platform-v1.53`; BOOTIMG `9ea7a943…75cb`, Y2ROOT `8fff0f83…d297`), fallback 22. Albums opens a perspective Cover Flow (smooth glide, cover flight into the album page; Grid stays available in Settings → Display), and Genres joins the main list (genre → All Songs + albums). Reborn 370 tests, clippy clean; host GLES matches the reference on all 77 screens; container suite 693; package checks PASS. Physical: not flashed yet; Mali-400 frame times to measure. Details: [23 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-23.md).

## POWER-FINAL-22 dark DSI hand-over — 2026-10-13

`out/y2linux-platform-v1-power-final-candidate-22/` (Linux `430ff11`, root `2026.08-platform-v1.52`; BOOTIMG `f73ba54c…402b`, Y2ROOT `d7d21d71…6a0d`), fallback 21. On 21 the shutdown is dark (fixed) but the startup still flashed colours: the DSI hand-over parked the bootloader's stream ≈40 ms before Linux's first modeset with the panel lit. 22 darkens the backlight for that hand-over and relights after the first Linux frame. Suite 693, exit 0; package checks PASS. Physical: not flashed yet. Details: [22 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-22.md).

## POWER-FINAL-21 quiet display power transitions — 2026-10-13 (shutdown fixed on hardware)

`out/y2linux-platform-v1-power-final-candidate-21/` (Linux `0b3e0e1`, Reborn `217e28d` unchanged, root `2026.08-platform-v1.51`; BOOTIMG `ea1da0b7…908e`, Y2ROOT `9a9b99ce…7b77`), fallback 20. 20 plus fixes for the owner's display report: DRM no longer switches the backlight on (it re-lit the panel over a stale white/colour buffer after the shutdown animation), the backlight is switched off at power-off, and the boot splash keeps the light off across its DSI re-initialising modeset (colour flash). Container suite 692, exit 0; package checks PASS. **Physical: not flashed yet.** Details: [21 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-21.md).

## POWER-FINAL-20 UART1 clock reclaim — 2026-10-13

`out/y2linux-platform-v1-power-final-candidate-20/` (Linux `c853915`, Reborn `217e28d` unchanged, root `2026.08-platform-v1.50`; BOOTIMG `1ffdb4a2…3c55`, Y2ROOT `98ffdca9…9548`), fallback 19. The never-initialised, unowned UART1 kept its bootloader clock on (an all-zero register set was taken for a busy transmitter); 20 reclaims it like UART2/3, so the last peripheral gate also matches stock at sleep entry. Container suite 689, exit 0; package checks PASS. Physical (archive 117): working boot healthy, UART1 gated; the first boot after the flash had dead USB networking until an off/on + replug (seen milder on 18 too; open). Details: [20 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-20.md).

## POWER-FINAL-19 PMIC_WRAP clock gate — 2026-10-13

`out/y2linux-platform-v1-power-final-candidate-19/` (Linux `0fa5135`, Reborn `217e28d` unchanged, root `2026.08-platform-v1.49`; BOOTIMG `49494899…44ed`, Y2ROOT `1e6a61fc…f4d5`), fallback 18. Gates the AP's PMIC_WRAP clock (the only INFRA clock still differing from stock at sleep entry) for the PCM sleep only, after the last PMIC access and before every restore; an owner-authorised live test on 18 showed the gate is safe and fully reversible while awake. Container suite 689, exit 0; package checks PASS. Physical (boot `d4f9a0f1`, archives 115/116): first boot healthy; a 47-min sleep clean, the PMIC_WRAP gate worked 2/2 (INFRA gates at sleep entry now exactly stock), INFRA still retained. Details: [19 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-19.md).

## POWER-FINAL-18 stock PMIC suspend fields, Baseline 18 — 2026-10-13

`out/y2linux-platform-v1-power-final-candidate-18/` (Linux `d2fff53`, Reborn `217e28d` unchanged, root `2026.08-platform-v1.48`; BOOTIMG `5d405228…2ace`, Y2ROOT `71852869…2c612`), fallback 17. REA showed the SoC sleep side is stock-identical; 18 brings the PMIC to its stock suspend values inside the sleep entry and restores them exactly: the audio 26 MHz clock-square request and audio DAC clock (Linux never released them), unused PMIC clocks, VREF18. VEMC3V3 (eMMC supply) stays on: the root eMMC is retained across suspend by design. Container suite 685, exit 0; package checks PASS. Physical (boot `69ef8c26`, archive 113): first boot healthy (taint 0, player ready 44 s, Wi-Fi, Bluetooth, USB/SSH, charging; `pmic_sleep=7` armed, modem gate active). 1-h sleep (archive 114) clean, PMIC fields applied/restored 3/3, PMIC golden differences 15 → 7, INFRA still retained. Tagged `baseline-18`. Details: [18 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-18.md).

## POWER-FINAL-17 modem request gate and screen-first wake, Baseline 17 — 2026-10-13

`out/y2linux-platform-v1-power-final-candidate-17/` (Linux `0459116`, Reborn `217e28d` unchanged, root `2026.08-platform-v1.47`; BOOTIMG `2ddd8d38…0b76`, Y2ROOT `dc1f057a…3e76`), fallback 16. Gates the never-used modem's clock requests (stock golden; suspect for INFRA never powering down), lights the screen before Wi-Fi/Bluetooth on a wake (16: ≈2.6 s to the screen, 1.9 s of it waiting for the radios), and carries 16's two follow-ups (MMSYS DCM, DMA-unmask readback). Container suite 682, exit 0; package checks PASS. **Physical (boot `de37f6bc`, archives 111/112):** first boot healthy, audio/Wi-Fi/Bluetooth/USB/SSH up; an 18-min sleep clean, screen ≈0.5 s after the wake (16: ≈2.5 s), modem requests gated at entry, a real lost USB DMA unmask caught and re-armed; INFRA still never powers down. Overnight drain pending. Tagged `baseline-17`. Details: [17 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-17.md).

## POWER-FINAL-16 stock sleep parity installed, Baseline 16 — 2026-10-13

`out/y2linux-platform-v1-power-final-candidate-16/` (Linux `a4e9c3b`, Reborn `f68e088` unchanged, root `2026.08-platform-v1.46`; BOOTIMG `2f1cd1c0…debf`, Y2ROOT `bd4a12a0…3d9f`), fallback 15. Built from the Y2's own stock kernel analysed with REA ([ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fstock-suspend-re-ledger.md)): USB-after-wake re-arm, stock 450 mA on any PC port and sleep with an idle cable, display power domain off at screen-off and in sleep, stock DCM, golden sleep entry (PLLs, muxes, unused clock gates, exact restore), read-only PMIC golden capture, stock fuel-gauge profile. Offline: container suite 676, exit 0; package checks PASS. Physical (boot `0b0e8a77`): display off/on 5/5, Wi-Fi, Bluetooth, MTP, SSH, audio up; one 36-min sleep clean and USB worked after the wake (first time since 13; cause not yet proven); golden SoC differences 26 → 11, PMIC 15/44. Live test: the AP may gate the never-used modem's clock requests (planned for 17). First night (boot `f871fd6a`, archive 110): 16 h unplugged, 33/33 sleeps clean, USB worked after the morning replug, drain ≈8.6 mA on the stock curve (15: ≈10 mA; stock ≈1.3 mA); INFRA still never powers down. Tagged `baseline-16`. Details: [16 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-16.md). Readiness remains MORE_WORK_REQUIRED.

## POWER-FINAL-15 dependency-update candidate sealed — 2026-10-12

`out/y2linux-platform-v1-power-final-candidate-15/` (Linux `be1aac2`, Reborn `f68e088`, root `2026.08-platform-v1.45`; BOOTIMG `86dc957a…844d`, Y2ROOT `0b14b794…20ae`) is 14 rebuilt on the newest release of every component: Linux 6.18.56 (the owner kept the 6.18 line), Buildroot 2026.08, Bootlin GCC 15.3/glibc 2.44, Rust 1.99, Mesa 26.2.4, OpenSSL 4.0.3, Python 3.15.0 and the rest. Offline: container suite 664 cases, exit 0; package, ELF, ARM, inventory and privacy checks PASS. Not flashed; physical NOT_RUN. The display (panel `prepare_prev_first`, Mesa 26/Lima) needs checking first. Details: [15 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-15.md). Readiness remains MORE_WORK_REQUIRED.

## POWER-FINAL-14 diagnostics candidate sealed — 2026-10-11

`out/y2linux-platform-v1-power-final-candidate-14/` (Linux `9d06ac4`, Reborn `63ac4a7` with code identical to 13, root v1.44; BOOTIMG `273dc927…3e5a`, Y2ROOT `78203697…14b9`) is 13 plus persistent sleep and USB diagnostics: `/data/system/platform/sleep-diagnostics.jsonl` rows at each suspend stage and around USB state changes, and the USB/network snapshot in every power-journal row. Not flashed; physical NOT_RUN. Why: the USB-after-wake defect (Defect B) recurred at 18:39 and 20:56 on 13. The only recovery is a hold-Power restart, which erased 13's in-memory counters. Details: [14 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-14.md). Readiness remains MORE_WORK_REQUIRED.

## Baseline 13 (POWER-FINAL-13) installed and published — 2026-10-11

Image: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-13`, kernel `6.18.0-y2linux-platform-v1-power-final-13`, root `2025.02.18-platform-v1.43`, release `1.0.0-platform-v1-power-final-candidate.13`; compiled from Linux `47c1cf2` and Reborn 0.3.0 `71ddb0d`. BOOTIMG `f73c24da…c178`, Y2ROOT `e62cb6c7…1915`. Git tag `baseline-13` (both repositories) is this source plus the tests, the `package.py --stock` packaging fix and documentation. Build and install: [BUILDING](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FBUILDING.md), [INSTALL](https://innioasis.app/guides/reborn-y2linux-y2.html).

What 12 and 13 changed: 12 made device suspend synchronous (the intermittent pre-SPM stall did not recur over a 5.5 h night, 34 suspends) and added a real charger "Full" state. 13 fixed the sleep guard that blocked all sleep after a radio-quiesce race (Defect A). It also applied the stock firmware's suspend settings, taken from the Y2's own stock kernel: VPROC 0.85 V while asleep, LP_SEL on VMC/VMCH/VEMC3V3, USB PHY save-current, click-wheel controller sleep, and a 30-min maintenance wake. Each one can be switched off at run time. Details: [13 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-13.md).

Hardware results on 13 (2026-10-11): first check healthy (taint 0, every new switch active). First unplugged sleep: 15:17 to 18:39, 12,104 s suspended in 7 kernel suspends with 6 clean 1800 s maintenance wakes, Power-button wake, restore result 0. Battery 76% to 76% (4.036 V to about 4.007 V) over 3.4 h. That is one short run, and the percentage comes from voltage; 12's overnight drain was about 2.2 points/h. USB networking failed after that wake: the gadget enumerated 5 s after the wake and the device reported it configured, but the host received 0 bytes for 3 min (same symptom as 12's "Defect B"; this time without a preceding sleep failure). Power off and on recovered it. That restart lost the in-memory counters for the new features (VPROC, PHY, wheel, INFRA power-down, golden entry capture), so the run does not show whether they worked as intended.

Open, in priority order: (1) USB traffic after a wake (Defect B). (2) Repeat the sleep test and read the new counters and the `golden` capture at sleep entry, then an overnight drain. (3) A warm reboot leaves the panel dark (`flip_done timed out`); use power off and on only. (4) Screen-off while awake keeps the display pipeline running (about 4.9 points/h). (5) PLL/clock-gating parity at sleep entry, eMMC supply in suspend, VGP2/DAC rail, panel deep standby. No current sensor exists, so no mA figure is claimed. Readiness: MORE_WORK_REQUIRED (developer preview).

## POWER-FINAL-11 remaining-screens candidate sealed — 2026-10-11

`out/y2linux-platform-v1-power-final-candidate-11/` (Linux build `5741d16`, Reborn 0.3.0 `abbb203`, root v1.41; BOOTIMG `1482316d…ee08`, Y2ROOT `4773d90d…d73c`) is 10 plus the computer, pairing, download, scanning and battery screens and a redrawn offline charging screen; not flashed, physical NOT_RUN. The installed image is 10. Kernel and drivers unchanged; the rescue charger's decision logic is untouched (display only). Details: [validation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-11-SCREENS.md), [scope audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md). Readiness remains MORE_WORK_REQUIRED.

## POWER-FINAL-10 Reborn UI v3 candidate sealed — 2026-10-10

`out/y2linux-platform-v1-power-final-candidate-10/` (Linux build `04aa8f9`, Reborn 0.3.0 `f31c94c`, root v1.40; BOOTIMG `9d1f00a5…0ca`, Y2ROOT `77a41a33…16`) is 09 plus the redesigned Reborn UI, startup screen and shutdown animation; not flashed, physical NOT_RUN. The installed image is 09. Kernel, drivers and partitions are unchanged. Details: [validation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-10-UI.md), [scope audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md), Reborn `docs/ui/REBORN-PRODUCT-UI-V3.md`. Readiness remains MORE_WORK_REQUIRED.

## POWER-FINAL-08 cumulative candidate sealed — 2026-10-10

`out/y2linux-platform-v1-power-final-candidate-08/` (Linux `d9fd5a7`, Reborn `ac5502e`, root v1.38; BOOTIMG `ad39788a…efb1`, Y2ROOT `e79bac96…c71a`) is the one image containing 06 (deep-sleep power-down bring-up), 07 (charging policy) and 08 (internal storage). Not flashed; physical NOT_RUN. The installed image is 06. 08 turns the stock FAT partition into ext4 Y2Media (`/media/internal`), exports it as MTP Internal Storage and adds explicit SD `format`/`grow`; the one-time provisioning runs only after the owner flashes. Details: [storage](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Finternal-storage.md), [policy](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fcharging-current-policy.md), [handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FNEXT-SESSION-HANDOFF.md). Readiness remains MORE_WORK_REQUIRED.

## POWER-FINAL-07 charging candidate sealed — 2026-10-10

`out/y2linux-platform-v1-power-final-candidate-07/` (Linux `551baad`, Reborn `97ff8c3` unchanged, root v1.37; BOOTIMG `65a1daf4…a3001`, Y2ROOT `83a61c1e…e66`) is 06 plus the full vendor charging policy and is built and offline-qualified; it is not flashed (physical NOT_RUN). The installed image is 06 (healthy at first check, power-down cycle still to run). The stock 16-step `CS_VTH` table and per-source requests (DCP/nonstandard 1100, Apple 800, CDP 650, SDP 450) are implemented behind one decision function with PMIC-die derating; the default ceiling stays 650 mA and nonstandard stays 70 mA because no cell charge rating, pack temperature or independent current measurement exists. Details: [policy](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fcharging-current-policy.md), [validation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-FINAL-07-CHARGING.md) (on branch `codex/platform-v1-power-final-07`), [handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FNEXT-SESSION-HANDOFF.md). Readiness remains MORE_WORK_REQUIRED.

## POWER-FINAL-06 bring-up candidate sealed — 2026-10-09

`out/y2linux-platform-v1-power-final-candidate-06/` (Linux `c1ef37a`, Reborn `97ff8c3` unchanged, root v1.36; BOOTIMG `64a91628…7869f`, Y2ROOT `e1c0bcd3…c23e4be`) is built and offline-qualified; it is not flashed (physical NOT_RUN) and not production. Correction: Y2Linux already ran the vendor 597-word `pcm_suspend`; the 05 report's "480-word dpidle" was the runtime-idle line. The real difference from stock is `infra_pdn=0`; 06 enables the vendor `infra_pdn=1` (INFRASYS/DDRPHY power-down) with a verified PERICFG restore, an automatic retained-mode fallback and a boot-to-boot guard. The 05 overnight defects are addressed: the MUSB L1 interrupt guard no longer storms on an unowned PHY level bit, and a terminal USB stop parks the controller instead of unregistering it (the Wi-Fi-time Oops was a dangling `usb0` parent, not `wlan0`). A 9 h idle capture of 05 (archive 89) showed 95.6% in SPM sleep with no recurrence (single run). Next: owner flashes 06, read-only check, first power-down cycle, repeated cycles, overnight drain vs. 05's about 2.1 points/h (voltage-derived); production cleanup only after hardware qualification. Details: [handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FNEXT-SESSION-HANDOFF.md). Readiness remains MORE_WORK_REQUIRED.

## POWER-FINAL-05 overnight result — 2026-10-09

The first overnight unplugged run on 05 (archive 88, same boot `3cae62f2`, taint 0) suspended 38,052 s of 38,235 s (99.5%) across 64 cycles and 63 600 s maintenance wakes, 88%→66% (voltage-derived, about 2.1 points/h, indicative only, no current sensor). It also exposed two new defects: (1) a terminal `Y2USB IRQ overflow` at 01:34 CEST with no cable, after which USB did not enumerate or charge until reboot, and (2) a kernel NULL-dereference Oops (`rtnl_fill_ifinfo`; later shown to be the `usb0` netdev's dangling parent after the 01:34 terminal USB stop, not `wlan0`) at the first Wi-Fi restore after the Power-button wake, followed by `kernel_sleep_unavailable` refusals (link unverified). Nothing was changed on the device by that analysis; the fixes are in 06. Details: [handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FNEXT-SESSION-HANDOFF.md), [data](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/data/y2-power05-overnight-20261009.json). Readiness remains MORE_WORK_REQUIRED.

## POWER-FINAL-05 installed — 2026-10-08

The owner flashed POWER-FINAL-05 (Linux `837b614`, Reborn `97ff8c3`, root v1.35; BOOTIMG `0137a855…44117`, Y2ROOT `9175185f…99a4d`). It is DEEPSLEEP-FINAL-04 plus the vendor MT6323 `LP_SEL` low-power select on five always-on LDOs (VA, VIO28, VUSB, VM, VIO18) with a root runtime revert at `/sys/firmware/y2_pmic/lp_sel`. Installed and probed: same boot, taint 0, 1573 s asleep with two maintenance wakes, SPM 3/3, vendor golden-table differences at suspend entry 22→17. No battery or current benefit is claimed (no current sensor, unknown capacity, voltage-derived SOC). Overnight drain, Power/RTC wake and early-boot on 05 are next. Details: [handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FNEXT-SESSION-HANDOFF.md), [report §40](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-DEEP-SLEEP-FINAL.md%2340-power-final-05-suspend-power-campaign-2026-10-08&anchor=40-power-final-05-suspend-power-campaign-2026-10-08). Readiness remains MORE_WORK_REQUIRED.

## DEEPSLEEP-FINAL-04 installed — 2026-10-08

The owner flashed the diagnostic successor DEEPSLEEP-FINAL-04 (Linux `5e26757`, Reborn `97ff8c3`, root v1.34, BOOTIMG `4738de48…ace5f6`, Y2ROOT `b0e66751…c041`). It differs from 03 only by retained per-device `WAIT`/`LOCK` records and a built-in device-phase stall sampler. Normal automatic suspend then ran cleanly on the first owner trial (469 s) and a one-hour unplugged trial (3805 s suspended, six maintenance wakes, SPM 9/9 entries/resumes, taint 0, ext4 errors 0). This does not resolve the intermittent pre-SPM stall (nine clean entries; timing perturbation possible). Next: owner reboot with an early unplug, then an overnight drain test. Readiness remains MORE_WORK_REQUIRED. See the [handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FNEXT-SESSION-HANDOFF.md) and [report §39](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-DEEP-SLEEP-FINAL.md%2339-diagnostic-successor-04--analysis-build-and-physical-trials-2026-10-08&anchor=39-diagnostic-successor-04--analysis-build-and-physical-trials-2026-10-08).

## DEEPSLEEP-FINAL-03 late analysis — 2026-10-08

Local analysis of archives65/66 against the exact03 suspend code finds the device-phase failure stops in a step the retained callback ring cannot record, about half a minute before the reset (consistent with the 30 s backstop). A diagnostic successor source (per-device `WAIT`/`LOCK` records and a built-in stall sampler) is prepared and unit/cross-compile tested but not built, flashed or run. The installed image, the pending recovery guard and all evidence are unchanged. See the [handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FNEXT-SESSION-HANDOFF.md). Readiness remains MORE_WORK_REQUIRED.

## DEEPSLEEP-FINAL-03 evening follow-up — 2026-10-08

Archive67 shows an orderly user-requested poweroff around09:55:39 CEST after the morning inspection, then a new03 boot about16 seconds later. Its retained guard still prevents full suspend (SPM0/0,421 refusals before USB return). The current boot's provisional journal estimate fell57%→32% across roughly seven hours unplugged; the 17:00 connected reading is Charging31% with no reported charger fault. Exact03 hashes and basic application/filesystem health remain sound. The earlier pre-SPM failure is unresolved. See the [handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FNEXT-SESSION-HANDOFF.md) and [audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23clean-corrective-image-physical-admission&anchor=clean-corrective-image-physical-admission). Readiness remains MORE_WORK_REQUIRED.

## DEEPSLEEP-FINAL-03 morning observation — 2026-10-08

Current installed image is DEEPSLEEP-FINAL-03, Linux `cfb7e09` / Reborn `97ff8c3`, rootv1.33. The owner reports about88%→55% over approximately six unplugged hours and no manual restart. Archived logs confirm a failed automatic suspend attempt on boot0132fb21, retained DPM_PREPARED/seq8, and an unclean reboot to81dce40c. The new boot records no full-system suspend and380 recovery-guard refusals. Runtime CPU0 DORMANT did run; it does not qualify whole-system sleep.

Morning read-only SSH confirms the same03 files, taint0, responsive/paused player, closed PCM, no scan, radios off, ext4 errors/warnings0 and fault-free charging. Pre-cable55% is preserved separately from connected samples. Exact reset cause and battery capacity/current remain unknown. The pending03 guard is preserved; no new trial, deployment or flash occurred. MORE_WORK_REQUIRED; the recurring device-phase suspend failure precedes further endurance acceptance. See the [current handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FNEXT-SESSION-HANDOFF.md), [overnight report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-DEEP-SLEEP-FINAL.md%2332-overnight-result--2026-10-08&anchor=32-overnight-result--2026-10-08) and [audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23clean-corrective-image-physical-admission&anchor=clean-corrective-image-physical-admission). The dated entries below retain historical states.

## USB02 power investigation / POWER01 owner installation next — 2026-10-05

The actually installed pair is USB-FINAL-02 Linux `0cb7792` / Reborn `2444e0f`, root v1.26, not the older baseline identities below. Last night's recorded 3.400268 V orderly shutdown is real; the owner's 88% UI and retained maximum 3.920141 V/full=0 do not prove a full starting pack. No system sleep occurred. Current recovery boot `e043cb75…` has DRM WARN/taint512, frozen display and safe C3 quarantine. A 30-minute PC window gains 3.881469→3.937500 V at the validated 450 mA configured ceiling/fault0; C2 85.7193%, C3 zero. Original components and saved Wi-Fi state are restored; MTP/ECM Ready. Battery capacity/health/current/NTC remain unproven.

One source-bound preserving POWER-FINAL-01 candidate is software validated: Linux `fedc005ba68b3f5020a45258e38d641aa191b12a` / Reborn `ccf450ac1388228dbd859318a05e13adf667c9aa`, kernel `6.18.0-y2linux-platform-v1-power-final-01`, root v1.27. It corrects runtime PCM PMIC slots, charging C3 admission, first display takeover and measured polling, and adds a bounded power/idle journal. Canonical location: `out/y2linux-platform-v1-power-final-candidate/`. BOOTIMG/ANDROID only; DATA is preserved. No flash/push/main merge has occurred. Full suspend, warning-free new-image idle, near-full charge and endurance remain open: MORE_WORK_REQUIRED. See [the final power report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-BATTERY-FINAL.md), [machine windows](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/data/y2-platform-v1-power-final.json) and [handoff audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23power-candidate-owner-handoff--2026-10-05&anchor=power-candidate-owner-handoff--2026-10-05). Resume this investigation immediately after the owner confirms installation.

## Baseline01 physical gate interrupted / USB diagnosis pending — 2026-10-04

Exact installed Baseline01 Linux `98daf3f` / Reborn `9cd12bae`, kernel baseline-01 and root v1.24 passes original machine/owner smoke on boot `ef2c8f2f…`, taint 0. All-four-core C1, 18 hotplug transitions, five OPP/voltage readbacks and natural parking/C2 pass; C2 has 4,857 entries and 85.4572% residency in 60.05534 seconds, zero restore faults. Eight scratch hash rounds each on DATA/SD after C2 pass. The owner restarted after an overlong deliberate USB-off C3 topology wait; C3 has no recorded armed/entered cycle and remains unqualified, not a proven C3 crash. Recovered boot `9d4d0245…` logs a DRM WARNING; automatic C3 correctly reports Skipped. Earlier post-flash USB disconnects remain independently open. Host ECM static-IP/autoconnect matching is corrected and saved; the host harness now keeps USB attached during parking and bounds its offline window to 180 s. Thirty affected host tests pass; installed firmware/images are unchanged. The owner prioritizes the separate wired-audio session holding the shared lock; USB diagnosis waits for its completion. No further CPU/transfer/suspend stress. Full Power and RTC wake remain separately NOT_RUN, historical Baseline02 RTC FAIL stays open, and endurance/electrical/distribution gates remain unqualified. See [the physical receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-BASELINE-PHYSICAL.md). All 233 feature identities are retained; sealed package metadata remains its seal-time record. No main merge, push, flash or public/physical promotion.

## Newest independent Platform 1.0 baseline — 2026-10-04

`Y2LINUX-PLATFORM-V1-BASELINE-01`: compiled Linux `98daf3f0220f4a1580bb4893094ee9f0e02362a5` / Reborn `9cd12baeeb70b204e08299bd4c91c8c35604c304`; root `2025.02.18-platform-v1.24`, kernel `6.18.0-y2linux-platform-v1-baseline-01`. SOFTWARE_VALIDATED / INTEGRATED_PHYSICAL_NOT_RUN; owner-local physical qualification ready, public distribution not ready. Baseline02 RTC FAIL remains open; UART01 CPU evidence/fallback is historical. Owner main and earlier candidates preserved. Canonical candidate `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-platform-v1-baseline-candidate`. Details in `docs/release/Y2-PLATFORM-V1-BASELINE.md`. Older current/next labels below belong to their recorded observation times.

## Integrated Platform 1.0 software candidate — 2026-10-04

READY_FOR_PLATFORM_V1_PHYSICAL_QUALIFICATION. All eleven source handoffs are composed on paired codex/platform-v1-integration branches. One sealed candidate: `/home/luca/Dokumente/Code/worktrees/platform-v1-integration/Y2Linux/out/y2linux-platform-v1-integration-candidate`. Compiled Linux `4c72466f2f27ddf9f0ca18ba8ddc4d89c52599d2` / Reborn `dd73dcc3243045cd33e319dda2f76918ed37ea31`; kernel `6.18.0-y2linux-platform-v1-integration-01`, root `2025.02.18-platform-v1.23`. Broad source/kernel/ARM/QEMU/ELF/package/privacy/source checks PASS; integrated hardware/endurance NOT_RUN and public distribution blocked. See the [master](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-MASTER.md), [233-feature matrix](https://github.com/schulzcode/y2linux/blob/HEAD/docs/release/Y2-COMMUNITY-BETA-FEATURES.json) and [one physical plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-PHYSICAL-QUALIFICATION.md).

Latest owner-installed receipts remain Baseline02 Linux8584ccd8/Rebornb71b4688, boot88b85fa3/taint0 after a failed full RTC trial. Temporary optimized binaries were restored to stock. UART01 remains the protected bounded CPU-idle authority. No new integrated image has run on hardware. Older dated sections below retain their original scope; a documentation HEAD is separate from compiled identity.

## Parallel integration observation — 2026-10-04

[Master status](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-MASTER.md): INTEGRATION_IN_PROGRESS. All eleven source-frozen handoffs are composed on isolated paired master branches; no final Platform 1.0 integration candidate exists. New Bluetooth/Wi-Fi owner receipts identify installed Baseline02 (Linux `8584ccd8`, Reborn `b71b4688`, root v1.21, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0). Their locations and limitations are recorded in the [live inventory](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-INTEGRATION-STATUS.md). This supersedes the older awaiting-installation identity below; it does not qualify automatic cold-boot C3 or the changed subsystem binaries. UART01 remains the exact-image physical authority for bounded C1/C2/C3. The dated Baseline02 seal and historical evidence remain intact. No master device access occurred.

Later owner RTC full-sleep evidence on the same installed Baseline02 is FAIL: watchdog recovery changes boot `27e6d684` to `88b85fa3-2282-4d93-b0b8-818a105ddd0a`, taint 0; retained journal stops at DEVICES_RESUMING (wake 0x20, full PCM 596, reset stamp 0x59325253), with no complete/exit proof. Direct scratch hashes and zero ext4 counters after reboot prove recovery only. New suspend source was not installed. Preserve prior UART01 C1/C2/C3 evidence; full resume and automatic C3 remain separate gates. Master archives the raw failure receipts offline and neither repeats the trial nor closes any milestone. Review the source-bound owner handoff before integration. 2026-10-04 [wired precision source/evidence update](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-HIGHRES-AUDIO.md): locked read-only access now observes installed Baseline02 Linux8584ccd8 / Rebornb71b4688, boot27e6d684-3794-4490-95db-a489027cd4f4, taint0. This supersedes the earlier installed-image identity below, while UART01 remains the retained CPU hardware qualification. No new cold-boot/CPU qualification follows from the identity read. Native wired admission remains S16_LE stereo44100/48000, 16 meaningful bits in32-bit slots; the MT6582 silicon maximum is unresolved. Precision diagnostics/quantization/fixtures are validated in isolated worktrees, not installed; fresh playback and CPU costs are NOT_RUN due to device-lock contention. No flash, push, merge or hardware milestone closure.

Updated 2026-10-03 from the sealed Baseline02 receipts and retained UART01 hardware evidence. This synchronization changes documentation only; it does not build, flash, push or run a new physical qualification.

## Retained Baseline02 seal and installed evidence``````````````

| Field | Sealed Baseline02 |
| --- | --- |
| Build | Y2LINUX-BASELINE-02 |
| Candidate | out/y2linux-baseline-02-candidate/ |
| Kernel | 6.18.0-y2linux-baseline-02 |
| Rootfs / release | 2025.02.18-platform-v1.21 / 1.0.0-baseline-candidate.2 |
| Compiled Linux | 8584ccd85f052f351fe51650b2348c83ca894ed4 |
| Compiled Reborn | b71b468860233faa0a42b8448ec5777fa952b8e3 |
| ABI / feature contract / layout / data | 1 / 2 / 1 / 1 |
| Software / package | PASS |
| New-image hardware / automatic cold boot | PHYSICAL_NOT_RUN |

The protected bounded CPU-idle hardware receipt is UART01, kernel `6.18.0-y2linux-cpu-c3-uart-01`, Linux `e9e8d63f9c94232c2b6627881e0967583e202dac`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, root `2025.02.18-platform-v1.20`, boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b`, taint 0. C1, C2 and C3 are physically working on that image. Baseline02 retains that kernel architecture; its new image and automatic cold-boot activation remain PHYSICAL_NOT_RUN until owner installation and the guarded checks.

See the [sealed receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md), [exact candidate and fallback identities](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fcandidate-index.md) and [authoritative hardware report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md). Compiled source identity comes from the manifest; a later documentation HEAD or published branch tip does not identify the installed kernel/rootfs.

## CPU hardware results carried forward

| Behavior | Exact UART01 bounded result |
| --- | --- |
| C1 WFI | All four CPUs enabled; entry/residency advance; rejected 0; 400 bounded wakes |
| C2 SLIDLE | +6,971 entries; 50.654676 s / 60.054881 s = 84.3473%; clock restore failures 0 |
| C3 DORMANT | 21 guarded reset-and-return trials, then +3,624 entries; 39.204662 s / 60.088344 s = 65.2450% |
| Final C3 accounting | 3,647 entries = resumes = successes = UART ACKs; timer/context/CIRQ/clock restore failures 0 |
| Core parking | Natural CPU0-only topology; owned mask 0xe; both secondary power status copies 0 |
| Hotplug | 18 supported transitions; park 3→2→1, restore 1→2→3 |
| Timers | GPT6, GPT4 sole broadcast, 13 MHz CNTFRQ, PPI29 on all cores, highres and NO_HZ pass |
| DVFS | 598 / 747.5 / 1040 / 1196 / 1300 MHz guarded readback before and after C3 passes |
| Storage | eMMC and inserted SD: eight fsynced checksum rounds each after C2 and after C3; ext4 errors 0 |
| Wake and I/O | Workload/screen demand restore, real FFmpeg/ALSA playback, bounded USB transfer and independent Wi-Fi observer pass |

UART1's retained clock is handled by the exact MT6582 UART sleep request/ACK contract and Linux UART ownership. It is no longer an unresolved C3 blocker. No forced UART peripheral gate or weakened admission guard was used.

## Baseline02 boot policy

Baseline02 enables qualified CPU0 C3 automatically after boot through `S05y2-cpu-idle`. The kernel initially registers C3 disabled with budget 0. The once-per-boot service checks identity, taint and static SPM/CIRQ/timer/context foundations, sets budget -1, enables CPU0 state2 and reads both controls back. Failures roll back; CPU1–3 C3 remains disabled. Dynamic topology, frequency, screen/workload/radio/USB, clock/domain, future-deadline, UART ACK and restore fault guards remain intact. The service does not force parking or gate UART1.

`y2-platform cpu-idle-policy stop` disables C3 for the current boot and prevents another start from overriding that choice. Recovery boot options `y2.deep_idle=off` and `y2.cpu_safe=1` retain the safe fallback. Runtime C3 is separate from full system suspend.

## Software validation and release limits

Fresh kernel/config/DT/module/ABI, Buildroot ARM and Reborn ARM checks pass. The integrated suite has 391 cases: 386 passed and 5 dependency skips; 27 native filesystem/GIO and 3 ALSA checks plus installed ARM checks cover the missing minimal-environment dependencies. All 125 focused source tests and 238 Reborn tests, formatting/lint, Cortex-A7 QEMU, installed ARM applications, ELF/dependencies and preserving-package checks pass. These are retained build receipts, not tests rerun by this documentation update.

Full system suspend with same-boot Power/RTC wake remains open. This pass does not qualify additional CIRQ edge injection, long endurance, electrical battery savings, native 24-bit/high-rate wired output, optional Bluetooth peer/codec behavior, USB host/VBUS, a calibrated battery gauge or public binary distribution. All five guarded active OPPs remain available; a C3 entry cap of 747.5 MHz does not lower the active CPU ceiling.

Source/license collection passed with recorded collector limitations. The package remains owner-local; successful collection is not redistribution permission or a byte-identical rebuild demonstration. The [community feature audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-COMMUNITY-BETA-FEATURE-AUDIT.md) retains 233 features and the separate unresolved release gates.

## Next owner boundary

Verify the sealed package and use `MT6582_preserve_data_scatter.txt` in Download Only mode, selecting BOOTIMG and ANDROID/Y2ROOT only. Preserve USRDATA/Y2DATA and every protected partition. After owner installation, the packaged SSH harness verifies exact identity and real cold-boot activation, quarantines C3 for foundation tests, runs one guarded C3 trial plus 20 cycles, and checks normal runtime, wake and I/O regressions. No installation is inferred from the user's earlier confirmation for UART01.

## Historical snapshots

The following text retains earlier dated decisions and results. Its “current”, “next” and candidate labels belong to those sessions; the Baseline02 summary above takes precedence. Historical failures and seal-time NOT_RUN receipts remain evidence for their exact images.

# Current Y2Linux platform state

## Baseline02 sealed precedence — 2026-10-03

New latest-source preserving candidate is sealed at `out/y2linux-baseline-02-candidate/`: Linux`8584ccd85f052f351fe51650b2348c83ca894ed4`, Reborn`b71b468860233faa0a42b8448ec5777fa952b8e3`, kernel6.18.0-y2linux-baseline-02/rootv1.21. Fresh build,391 production cases, source/native/Reborn/ARM/QEMU/ELF/config/DT/ABI/package checks pass. Owner-selected automatic qualified CPU0 C3 boot policy is included; all existing guards remain. Only BOOTIMG/Y2ROOT; preserve Y2DATA and protected partitions. New-image hardware/ cold-boot qualification NOT_RUN. Installed UART01 still proves C1/C2/C3 working, 3647 real C3 returns, same boot/taint0 and zero restore failures. Earlier summaries below are historical. See [sealed baseline record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md). No flash or push; owner installation is the next boundary.

## Baseline02 preparation precedence — 2026-10-03

Installed UART01 is physically qualified for C1/C2/C3 on Linuxe9e8d63/Rebornb71b4688, with3647 real C3 returns and clean restores, same boot/taint0. Earlier summaries below are historical. Owner requests a latest integrated Baseline02 preserving candidate and selects automatic qualified C3 boot policy. Source tests/live ARM control transaction pass; fresh build/seal and new-image physical checks are separate boundaries. See [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) and [UART01 hardware](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md).

## Current audit precedence — 2026-10-02

The [community beta master audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-COMMUNITY-BETA-FEATURE-AUDIT.md) now reconciles source, builds and hardware across both repositories; the [RC1 plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-COMMUNITY-BETA-PLAN.md) defines the shortest proposed beta path. At its17:49:54 CEST cutoff: Linux `dcbd7d1` candidate4 source/build activity, Reborn `b92d312`; latest sealed/reported installed candidate3, with narrow SD characterization in a concurrently edited draft; latest broad physical report remains Fix02. The exact baseline and conflicting older “unflashed” text are documented there. Earlier summaries below are historical and must not override that baseline. No hardware acceptance is created by this documentation update.

Updated 2026-09-29 from the CPU Final Fix02 physical qualification. This documentation update made no source repair, build or flash.

Working development baseline; FAIL for normal CPU-platform acceptance. The awake CPU platform is substantially qualified: timers, QoS, MMC runtime gating, automatic parking and 1196/1300-MHz voltage DVFS pass. Remaining gates are full-suspend resume completion, the SLIDLE bus-DCM predicate and loaded USB upload. The [Fix02 physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX02-PHYSICAL-QUALIFICATION.md) is authoritative for actual behavior, ahead of software receipts.

Storage ceiling candidate 2, 2026-10-01 (the candidate to flash):`out/y2linux-storage-ceiling-02-candidate/`, Linux `4db6d6de`, kernel `6.18.0-y2linux-storage-ceiling-02`, BOOTIMG `5c17f744…`, Y2ROOT `dc611011…`. Candidate 1 booted: eMMC ran HS200 cleanly (~133 MB/s read), but no SD card initialised because the PMIC write gate refused the SD rail writes. Candidate 2 admits exactly those fields. SD at the ceiling is not yet observed on hardware.

Storage ceiling candidate 1, 2026-10-01 (superseded):`out/y2linux-storage-ceiling-candidate/` is the Product UI v2 candidate plus the storage hardware ceiling pass. eMMC goes from 50 MHz HS52 to HS200 (8-bit, 200 MHz, fixed 1.8 V VIO18 IO, CMD21 tuning). SD goes from 50 MHz SD HS at 3.3 V to UHS-I up to SDR104 (4-bit, 200 MHz, MT6323 VMC 3.3→1.8 V switch, CMD19 tuning). Both have automatic fallback ladders and readback verification. Linux `540ae029`, Reborn `b92d312c`, kernel `6.18.0-y2linux-storage-ceiling`, root `2025.02.18-platform-v1.11`, BOOTIMG `4332d4f2…`, Y2ROOT `72eab34a…`. Software-validated; **not flashed or physically qualified; no mode above 50 MHz has run on a Y2 yet**. See the [storage ceiling record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-STORAGE-CEILING.md).

Product candidate, 2026-10-01 (superseded by the storage ceiling candidate):`out/y2linux-reborn-product-ui-v2-candidate/` is the Fix03 platform (same kernel) plus Reborn Product UI v2, a Reborn-mark splash and a platform backlight-off step before power-down. Linux `5cfe04cb`, Reborn `bd8436dd`, root `2025.02.18-platform-v1.10`, BOOTIMG `8a974cb5…`, Y2ROOT `a5c2914e…`. Software-validated; not flashed or physically qualified. See the [Product UI v2 receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-REBORN-PRODUCT-UI-V2.md).

Software candidate, 2026-10-01: one CPU Final Fix03 preserving candidate (Linux `76a5d41d`, Reborn `77cf83e0`, BOOTIMG `c55b2640…`, Y2ROOT `04cafd4b…`) is built and software-validated, but not flashed or physically qualified. It reconciles the SLIDLE bus-DCM baseline and makes the USB storm guard progress-aware. It fixes wake escalation, SD identity and the DVFS label, and instruments the resume window so the next RTC attempt names the stalled call. See the [Fix03 receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX03.md). The Fix02 result below remains the latest observed hardware state.

## Latest physically observed identity``````````````

| Field | Exact identity, observed 2026-09-29 |
| --- | --- |
| Linux compiled source | 1a1a6693dcd82f62daecd4c1491ef512823a86c5 |
| Reborn compiled source | 77cf83e09a18f82a867040e72d35b6e70b26fa85 |
| Kernel | 6.18.0-y2linux-cpu-final-fix02 |
| Rootfs | 2025.02.18-platform-v1.8 |
| Release / build | 1.0.0-cpu-final-fix02-candidate.1 / Y2LINUX-CPU-FINAL-FIX02 |
| Final boot | 6bb70fad-29a7-4a8e-a1a1-b69884434127 |

Later documentation HEADs are not compiled source identities. The report retains all four boot IDs and the retained-journal capture. No fresh device observation is implied by the date of a documentation commit.

## Physical coverage``````````

| Area | Status | Observed scope |
| --- | --- | --- |
| GPT6/GPT4/PPI29, highres/NO_HZ | PASS | 13-MHz CNTFRQ all CPUs, sole GPT4 broadcast, PPI29 on CPU0–3, ~1.09-ms 1-ms sleeps |
| Hotplug, schedutil, workload QoS, thermal override | PASS | eight classes, real input/playback/scan/transfer/maintenance producers, screen-off interaction release |
| C1 WFI | PASS | entries/residency advance, rejected 0 |
| MMC runtime clock gating | PASS | eMMC/SD gated at rest, CCF counts 0, 16/16 hash rounds, no errors or mismatches |
| C2 SLIDLE | FAIL | clock mask 0 with radios off, but TOPCKGEN+4 reads 0x0, not the required 0x0f |
| Automatic parking / restore | PASS | 3→2→1 at 5-s pacing, display restore 0.63 s; wake counted as pressure restore |
| High OPP / voltage DVFS | PASS | PWRAP 0x7f ready; 1196 @ 1.20 V, 1300 @ 1.25 V readback; sampled ordering; integrity 0 errors |
| C3 / CIRQ deadline handoff | NOT_TESTED | preflight unmet: topology, frequency, domains, clocks, bus |
| SRAM journal | PASS | awake self-test; warm-reboot retention; valid records after backstop reset |
| Charger refusal / staged PM | PASS | active-charging -EBUSY clean unwind; freezer/devices/platform/processors/core same boot |
| Full RTC suspend | FAIL | SPM return and resume vector proven; reset by 30-s backstop after device resume, before PM exit |
| Power wake / RTC cycles / restoration | NOT_TESTED | no same-boot full resume |
| USB loaded transfer | FAIL | 0/10; EP1 RX DMA channel 5 IRQ storm, twice, UI alive, Wi-Fi-observed |
| Wi-Fi / CONSYS | PASS, bounded | 4 × 1-MiB SHA roundtrips; radio restore after quiesce |
| SD media lifecycle | FAIL (non-CPU) | kernfs inode/ctime inventory remounts /media/sd after reclaim |

Screen-off idle, parked: 2.71 % of four cores (Fix01 9.74 %), 171 IRQ/s (391), 355 context switches/s (504). This is a CPU idle improvement, not a measured battery improvement. Owner actions: USB unplug and reconnect only.

## Enabled software and unfinished qualification
  - S16 stereo 44.1/48 output is enabled. Native S24/S32/preserved 24-bit and

88.2/96-kHz output remain gated; decoding high-rate sources is separate.
  - Optional AAC/aptX/aptX-HD/LDAC encoders are included in the private experiment

build. Normal runtime disables their endpoints; SBC is baseline and Auto retains qualification/distribution gates. Fix01 peer audio is NOT_TESTED.
  - Schema-2 low-voltage policy is enabled and provisional: critical/warning/

recovery 3.4/3.5/3.6 V. Estimated SOC is not measured current, coulomb count or calibrated capacity. Pack thermal and discharge/reserve/full-cycle charging acceptance remain open. See the [power contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fplatform-power-v1.md).
  - Automatic deep sleep, C3 promotion, AP watchdog recovery, USB host/VBUS/UAC

and NCM activation remain unqualified/gated. Screen-off is not system sleep.
  - Root-only OTA/recovery/maintenance software exists; production trust,

distribution/provisioning, recovery/endurance and byte-identical image reproducibility remain separate gates. Automatic BOOTIMG OTA is excluded.

The [capability ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-HARDWARE-FINAL-CAPABILITIES.md) separates latest observations from historical build flags. Runtime status determines actual admission/faults. [Hardware gates](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fplatform-v1-hardware-gates.md) and [Reborn state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2FCURRENT_REBORN_STATE.md) retain other limits.

## Next smallest correction boundary

CPU Final Fix03 is an implemented, unflashed candidate. The owner's single Fix03 run (prepared in [Fix03 physical qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX03-PHYSICAL-QUALIFICATION.md)) checks the regression gate, SLIDLE with radios off, USB 10 × 1 MiB, then RTC → Power → 5 cycles. If resume still stalls, the timed ring names the one call to correct next. The Fix02 EP1 "IRQ storm" was legitimate throughput tripping the guard, not a re-arm defect. Preserve all Fix02 physical passes. Do not bypass guards or restart CPU architecture. The [roadmap](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Fplatform-v1-roadmap.md) and [standing audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23standing-milestone-boundary-rule&anchor=standing-milestone-boundary-rule) govern implementation and acceptance; this page does not authorize new scope.

## Candidate, fallback and evidence

Latest candidate: `out/y2linux-cpu-final-fix02-candidate/`, already owner-flashed before qualification. Preserve-data payload is BOOTIMG/Y2ROOT only. Exact known-good fallback is Hardware02, kernel `6.18.0-y2linux-hardware-02` / root `2025.02.18-platform-v1.4`. The [candidate index](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fcandidate-index.md) holds full hashes and identity; [reconstruction](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fplatform-v1-reconstruction.md) uses the built pair rather than later docs HEADs.

Private evidence: `out/cpu-final-fix02-physical-qualification/20260929T152328Z/`, 460 sealed files (Fix01: `out/cpu-final-fix01-physical-qualification/20260927T205514Z/`). Raw secrets, firmware and calibration are not published. [Documentation index](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FREADME.md), [catalog](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FDOCUMENTATION_CATALOG.md) and [knowledge rules](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FKNOWLEDGE_BASE.md) identify current contracts versus history. Older candidate/evidence reports preserve their original scope and failures.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
