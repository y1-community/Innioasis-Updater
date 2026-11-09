---
title: "Current Reborn state on the Y2 - Innioasis Updater"
description: "Current Reborn state on the Y2 1.0.0-beta.9.3.19 — Y2Linux 1.0 Beta 9.3.19 Baseline 228, 2026-11-08: update notifications published Published as baseline-228 Reborn 520c4"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-current_reborn_state.html"
---

# Current Reborn state on the Y2 - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Current Reborn state on the Y2

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Current Reborn state on the Y2

## 1.0.0-beta.9.3.19 — Y2Linux 1.0 Beta 9.3.19 (Baseline 228), 2026-11-08: update notifications (published)

Published as `baseline-228` (Reborn `520c4b8`; work `e989efb`). Update Notifications (Y2Reborn #97): toggle on Software Update (`Settings.update_notifications`, default off). With it on, `update_watch_due` lets any screen observe the platform every `UPDATE_WATCH` 120 s while online and lit (before: only `platform_backed` screens, so the daily check's answer arrived only in Settings); `update_notice` names each version once (`update_announced` persisted), no toast on Software Update itself ([Beta 9.3.19 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.19.md)).

## 1.0.0-beta.9.3.18 — Y2Linux 1.0 Beta 9.3.18 (Baseline 227), 2026-11-08: Luna XP, bitrate, Cover Flow follows the skin (published)

Published as `baseline-227` (Reborn `56298e9`; work `dba53bf`). Luna XP skin (eNKay; fonts subset, adapted to the shipped-skin rules; seventeen skins). `views_playing::bitrate_label` in skin var `{bitrate}` and Song Info's Format line (Y2Linux #87; average only, no CBR/VBR; Song Info has had no menu entry since UI v3 `ceaae31`). `Ui::online()`: the update page shows "Connect to Wi-Fi" offline (#96). `quick_menu_hold`: holding Select on the Wi-Fi/Bluetooth/Brightness tile opens its settings (#101). `ArtistAlbums` Oldest First/Newest First/A to Z in Customize → Browsing, `catalog::within_artist` (#75). Skin `cover_shape` + `Ui::round_covers()` (covers rounded at upload), native `"captions": false` with `{flow_title}``{flow_artist}``{flow_detail}`, generator `add_cover_flow` (#100). `reborn-library/src/unplayable.rs`: audio without a decoder counted per type and folder (`scan_folder_unplayable`, valid while the folder mtime matches) and named in Settings → Library (#104). Y2Linux side: USB stays a peripheral after every disconnect (#102) ([Beta 9.3.18 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.18.md)).

## 1.0.0-beta.9.3.17 — Y2Linux 1.0 Beta 9.3.17 (Baseline 225), 2026-11-08: covers, Bluetooth first connect, Cover Flow (published)

Published as `baseline-225` (Reborn `e14b17b`; work `0978fb4`, `e9f72a0`, `0f09caa`). Fixes written to hold for every format and headset (owner 2026-11-08). `decode.rs`: `Unsettled::due` settles a song (cover, media state, gapless preopen of the next) once ≥ 250 ms are queued or `SETTLE_WAIT` 500 ms after its first block; 9.3.16's cushion was unreachable with MP3/AAC/Opus blocks (8 per channel, 190–210 ms) and their covers came at the song's end (Y2Reborn #102, Y2Linux #98). Fixtures `cover-3s.{mp3,m4a,opus,ogg,flac}` (`tools/build/fixtures.py --covers`), test `every_codec_gets_its_cover_early_in_the_song_and_after_a_gapless_boundary`. `outputs.rs`: `AutoOutput` is ready on `playback_rate` (stereo, rate known) and retries a failed switch (`AUTO_OUTPUT_RETRY` 2 s, `AUTO_OUTPUT_TRIES` 5; Y2Reborn #103). `artwork.rs`: thumbnail cache name carries `Key::folder_revision` (folder cover candidates' names, sizes, mtimes), prefix `thumb4-` (Y2Reborn #105). Y2Linux side: uMTP patch 0007, every file name copies (#88) ([Beta 9.3.17 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.17.md)).

## 1.0.0-beta.9.3.16 — Y2Linux 1.0 Beta 9.3.16 (Baseline 224), 2026-11-06: steady Bluetooth (published)

Published as `baseline-224` (Reborn `ceb4824`; work `0ed544c`, `d4298f2`, contract `e209e30`). A playing Bluetooth PCM is never left to run dry (F69, Y2Linux #96, Y2Reborn #99): `SinkWorker::bridge` tops a Bluetooth sink up to `BRIDGE_MS` 100 ms of silence whenever no music is written, also while it is the kept sink between two streams (`Playing::idle_wait` 10 ms, `receive` does not wait without a sink); a Bluetooth song end is `drained` once its music is written (no drain to empty); BlueALSA PCMs open with 8 × 1024 frames (`rb_sink_open`, wired 8 × 512). A Bluetooth pause holds in place (no device pause, silence) and `Runtime::hold_limit` releases it after `BLUETOOTH_HOLD_LIMIT` 3 s. `AlsaSink::plan_bluetooth` builds the spec from the observed transport without opening the PCM. Metric `bluetooth_xruns`. `decode.rs``settle`: a song's artwork, media state and the next song's preopen wait until ≥ 250 ms of its audio is queued (or its end). Click stream 2048 frames. Tests `playback/stream_continuity_tests.rs` (real-time fake sink counting underruns). Y2Linux side: BlueALSA 0005/0007/0008 dropped, SBC/AAC fixed rate by default ([Beta 9.3.16 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.16.md)).

## 1.0.0-beta.9.3.7 — Y2Linux 1.0 Beta 9.3.7 (Baseline 215), 2026-11-03: Bluetooth as a client of the radio daemon (published)

Published as `baseline-215` (Reborn `8fc6f69`); test builds 9.3–9.3.6 were never published. No Reborn code change after 9.3.4: the 9.3.5–9.3.7 fixes (AirPods' own AAC configuration, set-up without resolved services, waiting for the codec list) are in Y2Linux's BlueALSA patch 0006 and `y2-radiod`. Known: a pause longer than ≈20 s drops the link once (Y2Linux [Beta 9.3.7 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.3.7.md)).

## 1.0.0-beta.9.3.4 — test build 212, 2026-11-03 (on the developer's player, not published): Bluetooth as a client of the radio daemon

The D-Bus worker (`bluetooth.rs` + `bluetooth/worker.rs`), `CodecReconnect`, busy retries, intents and PCM locks are gone: `reborn-platform/src/bluetooth.rs` is a client of Y2Linux's `y2-radiod` (`/run/y2/radiod.sock`, `y2p_contract::radiod`); its `Status` is built only from the daemon's state, a connected headset still being set up is `settling` and not playable, the sink takes a `StreamLease` around BlueALSA's PCM. The codec choice is always accepted (applied when headphones connect or the stream stops); codec quality applies without a restart. Settings > Bluetooth > a saved device: Connect Automatically (#78). #92: a rolled-back output change keeps the whole library (`runtime::audio::keep_live_parts`); a status without the adapter is no lost peer. Wi-Fi's switch asks the daemon. AVRCP answers only calls that want an answer.

## 1.0.0-beta.9.2.16 — Y2Linux 1.0 Beta 9.2.16 (Baseline 207), 2026-11-02: steadier Bluetooth codecs

Published as `baseline-207` (Reborn `8667100`; sequence 13200). #87 (Sony WH-1000XM4 crackled on AAC 320 kbit/s with Wi-Fi on; the saved LDAC never applied). `854a727`: a codec request refused because playback holds the PCM ("Release the Bluetooth PCM…", "Bluetooth PCM still open…", `codec_pcm_held`) is handed to the app as `Status::codec_deferred {address, seq}` (kept across worker refreshes); `CodecReconnect` re-arms the attempt once per new seq, at most three times per connection (reset on reconnect and when a restarted worker counts from 1), so the choice is asked again at the next pause or stop. `7e9acd8`: Auto ranks AAC, aptX, then SBC; LDAC and aptX HD only when chosen (not even after being negotiated last); the Wi-Fi-heavy-transfer exclusion went with them. The platform side (AAC standard / LDAC mobile defaults, the Wi-Fi codec ceiling in BlueALSA) is in Y2Linux. Not yet tried on a player.

## 1.0.0-beta.9.2.15 — Y2Linux 1.0 Beta 9.2.15 (Baseline 206), 2026-11-01: Settings count

Published as `baseline-206` (Reborn `5745736`; sequence 13100). #85 (PR #86 by mrtngamper, squashed as `97e46a8`): `pages::settings` and `pages::library` count the `tracks` they are given. They read `m.library.tracks`, which the render's `normalize` and `Ui::model_action` borrow out of the model, so `Ui::library_counts` (one slot keyed by `library_stamp`) alternated between the empty borrow and the real list and recounted every track each frame (72 000 songs: ≈19.5 ms per frame on a PC, under 0.5 ms for every screen with the fix). `224f4f9` restores the test name `a_playlist_moves_to_another_place_in_the_playlists_list`. No other reborn-ui code reads `m.library.tracks`.

## 1.0.0-beta.9.2.14 — Y2Linux 1.0 Beta 9.2.14 (Baseline 205), 2026-11-01: Bluetooth sink kept

Published as `baseline-205` (Reborn `786eccb`; sequence 13000). F61 (`3435238`, report c0fe2638): quick radio station changes closed and reopened BlueALSA's PCM twice per station (the plan's probe, then the open), each a transport release and a new AVDTP Start; earbuds that answered in up to 6 s hit BlueZ's timeout and the link ended locally. `keep_sink` now keeps any output; `sink_change` compares the wired epoch only for the jack; the next start takes the kept Bluetooth spec through `keeps_bluetooth_sink` while `validate_bluetooth_observation` accepts the live `BluetoothPcm` (same transport generation, codec, rate, format); idle wheel clicks play only in a wired kept sink; a Bluetooth pause still sends `Stop` (F43). On the owner's player: six skips 2.5 s apart on AirPods Pro, each `sink_reused`, heard. `.github/ISSUE_TEMPLATE` issue forms (`c3277e2`), blank issues off.

## 1.0.0-beta.9.2.13 — Y2Linux 1.0 Beta 9.2.13 (Baseline 204), 2026-11-01: search song, resume, letters

Published as `baseline-204` (Reborn `69d8e37`; sequence 12900). #79 (`76edbe8`): a song picked in search plays alone (one-member `PlayCollection`, source kept); Play All plays every song found. #80 (`9d2c2ae`): `native/seek_index.c` keeps a closing decoder's sparse generic index (4 files, ≤2048 points, spans ≥120 s, keyed by dev/inode/size/mtime) and restores it before the next decoder's first seek, so MP3 (no fast seek) and ADTS AAC no longer read from the start on each resume; memory only. `56405af`: the Bluetooth worker logs BlueZ's `Device1.Disconnected` as `peer_disconnected` {address, reason, bluez_reason, message} (seen on the owner's player). Y2Linux #64 (`141a9ff`): `LETTER_SCROLL_STEPS` 4 → 3. Owed on a player: resume time after sleep, letter-scroll feel.

## 1.0.0-beta.9.2.12 — Y2Linux 1.0 Beta 9.2.12 (Baseline 203), 2026-11-01: light skins' greys

Published as `baseline-203` (Reborn `4a052b3`; sequence 12800). #76: `skin::remap`'s table still had the pre-9.2.3 greys (#A0A4AE, #848894), so the brighter MUTED/DIM stayed unmapped and pale on light skins; it now takes `color::MUTED` and `color::DIM` from the theme. The platform's Bluetooth-off fix needs nothing from Reborn.

## 1.0.0-beta.9.2.11 — Y2Linux 1.0 Beta 9.2.11 (Baseline 202), 2026-10-31: radio icons only while connected

Published as `baseline-202` (Reborn `9cd6368`; sequence 12700). Y2Linux #73 follow-up: the status bar (`components/status.rs`) and skins' `indicators` show Wi-Fi and Bluetooth only while connected; `Flag::WifiConnected` needs the radio on; the indicators' `dim` colour is accepted and checked, unused.

## 1.0.0-beta.9.2.10 — Y2Linux 1.0 Beta 9.2.10 (Baseline 201), 2026-10-31: settings tree, list scrolling

Published as `baseline-201` (Reborn `530f3ae`; sequence 12600; includes test build 200 = 9.2.9). Settings: eight places (Bluetooth, Wi-Fi, Sound, Display, Skin, Customize, Library, System); `customize.rs` (Customize's pages `browsing`/`wheel`, pickers `choose:<setting>`, hints), `pages::sub_page`, `system_menu` (`Screen::Update`; Software Update = filter `software`), `library` (`Screen::SettingsLibrary`), Playback under Sound; the map and the placement rule: [REBORN-SETTINGS-MAP.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-SETTINGS-MAP.md). Lists: settings rows on the screen with `group_window`, glide and rail (#74), Music `MUSIC_ROWS` window, Sound glides; Cover Flow's artist without the year (#73).

## 1.0.0-beta.9.2.8 — Y2Linux 1.0 Beta 9.2.8 (Baseline 199), 2026-10-31: platform Wi-Fi diagnostics only

Published as `baseline-199` (Reborn `a39176e`; sequence 12400). No Reborn change besides the version and the re-recorded platform contract: network.json `supplicant_events` gains `rejects` (Y2Linux #83).

## 1.0.0-beta.9.2.7 — Y2Linux 1.0 Beta 9.2.7 (Baseline 198), 2026-10-31: wheel clicks whenever no music plays

Published as `baseline-198` (Reborn `38946ea`; sequence 12300). `Runtime::wheel_click` sends the wired plan (`click_spec`, planned once) unless a pause holds the output on the right route (a hold on the other route is released); the sink thread's `click_while_idle` plays in the kept wired sink or opens one (`keep_for_clicks`) and keeps it `CLICK_KEEP` 10 s (`KeptSink::until`); a start reuses it via the switch. A sleep request closes a kept sink. Crackle fixed: no rewind of queued silence (`AudioSink::rewind` gone), ≈ 1536 frames queued. Click level from the live volume.

## 1.0.0-beta.9.2.6 — Y2Linux 1.0 Beta 9.2.6 (Baseline 197), 2026-10-31: wheel click while paused

Published as `baseline-197` (Reborn `dc335e8`; sequence 12200). #77: the wired codec has no device pause, so a held stream is drained to SETUP and 9.2.4's clicks failed `ALSA -77`. `click_while_held` now waits for the paused music to play out, prepares the stream (`pause(false)`), clicks over silence and stops it 1 s after the last click; no click while music plays (the rewind-and-replay `Tail`/`joined` removed). `WheelClick` Off/On, On serialized as 9.2.4's `when_paused`, `always` read as On.

## 1.0.0-beta.9.2.5 — Y2Linux 1.0 Beta 9.2.5 (Baseline 196), 2026-10-31: platform Wi-Fi fix only

Published as `baseline-196` (Reborn `f45f6bc`; sequence 12100). No Reborn change besides the version: the platform now switches Wi-Fi off and on when scans keep missing the saved network after a wake (F60, Y2Linux #83). Reborn shows Wi-Fi Off for a moment then; its Wi-Fi preference (`/data/network/enabled`) is untouched.

## 1.0.0-beta.9.2.4 — Y2Linux 1.0 Beta 9.2.4 (Baseline 195), 2026-10-31: own orders, wheel click

Published as `baseline-195` (Reborn `8ecff51`; sequence 12000). Home order under Customize > Home Menu and playlist order through the playlist menu's Move (#53, #33): settings `home_order`/`playlist_order`, reborn-core `home.rs`, reborn-ui `reorder.rs` (`Carry`, `mode_input`). Customize > Wheel Click Off/When Paused/Always (#67): `WheelClick`, `Playback::click`; the sink thread mixes a 4 ms tick into the wired sink only (never Bluetooth, only with a sink open), taking back unplayed frames (`AudioSink::rewind`, `rb_sink_rewind`) and writing them again from `playback/click.rs``Tail`; held, it plays the tick over silence and pauses again 1 s later. Cover Flow text travels with its cover (#71, `flow::centre_x`). Details: Y2Linux `docs/validation/Y2-LINUX-1.0-BETA-9.2.4.md`.

## 1.0.0-beta.9.2.3 — Y2Linux 1.0 Beta 9.2.3 (Baseline 194), 2026-10-31: album years, defaults from the issues

Published as `baseline-194` (Reborn `9a50d47`; sequence 11900). `Track.year` from the date tag (additive column, `METADATA_REVISION` 5, `AlbumTotal`, `year_key`): an artist's albums oldest first, years in album rows and lines (#66). Other Network… for hidden Wi-Fi (`Purpose::WifiName`, `hidden` → `scan_ssid 1`, #61). Cover Flow's position in the status bar, skins' `{position}` (#70). Skins number album songs (`numbered`, `{track_number}` in rows; Y2Linux #75). `MUTED`/`DIM` a step brighter (#59). `send_wifi`, library `has_column`. Details: [Y2Linux Beta 9.2.3 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.3.md).

## 1.0.0-beta.9.2.2 — Y2Linux 1.0 Beta 9.2.2 (Baseline 193), 2026-10-31: status icons in skins, GitHub requests

Published as `baseline-193` (Reborn `29aa1cc`; sequence 11800). Skins: element `indicators` (charging, computer, Bluetooth, Wi-Fi; right to left, closing up) in every shipped skin (`build_skins.py add_status`), variable `{date}` (Y2Linux #70 #73). A 12-hour clock says AM/PM: one `clock::clock_text` and `date_text`, made once a minute (#72). Brightness: Select on the card, then the wheel in 5 % steps from 5 % (`BRIGHTNESS_MIN`, `Ui::brightness_input`, #74). Fast scroll's letter mode from 4 suggested steps (#64). Equalizer files up to 20 filters (`MAX_BANDS`, `RbDspConfig` 680 bytes, #76). The status bar lives in `components/status.rs`. Details: [Y2Linux Beta 9.2.2 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.2.md).

## 1.0.0-beta.9.2 — Y2Linux 1.0 Beta 9.2 (Baseline 191), 2026-10-31: sleep and wake fix in the platform

Published as `baseline-191` (Reborn `f445483`; sequence 11600). The fix is in the platform (the sleep helper's radio quiesce, `bluetooth-power`); Reborn carries the work since Beta 9.1 below and the version. Details: [Y2Linux Beta 9.2 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.2.md).

### Since Beta 9.1 (Y2Linux test build 190, 2026-10-31)

`effect_inner` is an exhaustive table (921 → 299 lines): the 29 longer cases are `on_<effect>` methods in `runtime/effects/` (platform, sound, queue, radios, system). The Bluetooth thread is `BluetoothWorker` (`bluetooth/worker.rs`): `run` reconnects, `session` serves one D-Bus connection, `open` sets it up and `pass` runs seven steps (wait, completions, refresh, discovery, pairing, commands, publish; `command` carries one out). The screen dispatch exists once (`native_screen`), which gives a skin without a Music layout the Music menu again instead of the system page. Code is written to Y2Linux's [coding standard](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FCODING-STANDARD.md) (see `AGENTS.md`).

## 1.0.0-beta.9.1 — Y2Linux 1.0 Beta 9.1 (Baseline 189), 2026-10-30 : the platform's types, smaller files

Published as `baseline-189` (Reborn `e309b49`; sequence 11500). Reborn reads the platform's records in the platform's own types from `y2p-contract` instead of looking up JSON fields: the update page (`update::Status`, the live `DownloadProgress`), the battery and shutdown intent (`power::PowerRecord`, `Intent`), Wi-Fi readiness (`network::Published`), the SD and Y2Media claims (`storage::MediaRecord`, `Y2MediaClaim`), the USB receipt (`usb::Receipt`), report progress (`reports::ReportProgress`), Internal Storage setup and the radio firmware (`f64d454`…`f1637ca`). The recorded contract is unchanged except for `download_percent`, which download.json never filled; the Settings row now shows the live download percentage instead. Split without a code change (the same tests run): `main.rs` 8,268 → 947 lines (`runtime/`, `main_loop.rs`, `main_tests/`; `e6eb756`), `playback.rs` 3,725 → 1,565 (`playback/`; `4c94818`), `reborn-ui/src/lib.rs` 4,493 → 1,069 (`80c76ce`). The main loop is `MainLoop::pass` in 17 sections with `shut_down` and `Watchdog` (`c2691b1`, `fecf263`); the audio threads are `DecodeWorker` (`run`, `play`, `crossfade`) and `SinkWorker` (seven sections) (`a3c7c90`, `9746b91`). 748 workspace tests. Details: [Y2Linux Beta 9.1 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.1.md).

## 1.0.0-beta.9.0 — Y2Linux 1.0 Beta 9.0 (Baseline 186), 2026-10-30: the platform in Rust

Published as `baseline-186` (Reborn `2bc1e2c`; sequence 11400). The platform underneath is Rust now; Reborn reads it through the shared `y2p-contract` crate, and its contract test (`crates/reborn-platform/tests`) runs every platform golden through Reborn's own parsers. Reborn itself: a quieter dark idle (main loop and watchdog every 5 s instead of 1 s while dark and quiet, observations every 10 s; `639049b`), automatic sleep waits while the battery shows a cable after a `charger_or_usb_active` refusal (`764b024`, `68af9ac`), `metrics` answered by the control thread (`7afa346`), "An update check is already running" for `update_in_progress` (`9859348`). 738 workspace tests. Details: [Y2Linux Beta 9.0 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md).

## 1.0.0-beta.8.43 — Y2Linux 1.0 Beta 8.43 (Baseline 164), 2026-10-28: issue fixes

Published as `baseline-164` (Reborn `a08ca5d`, fixes `2eada03`; sequence 11000). #51: Cancel and a held Back leave Search to the screen it was opened from (the router remembers the Back press; the keyboard's dead `Leave` path is gone). #45/#46: `albums::unify_album_artists` on the library thread gives songs without Album Artist the album's single one (same storage, folder, title); `Track::own_album_artist` keeps the tag for Last.fm. #52/#55: `Settings::home_hidden` (Customize › Home Menu lists every place). #60/#25: `QueueOrigin`; Go to Album becomes Go to Playlist/Folder/Search/ Genre/Songs. #57: skin `remap` recolours warp corners. #56: `AlbumOrder` (Customize › Album Order). #30: letter steps while the fast-scroll letter shows (`FAST_SCROLL_LINGER` 700 ms). #62: unplug toast. #28: ticks on a computer connecting and on held seeks (`SEEK_TICK_GAP` 300 ms). Details: [Y2Linux Beta 8.43 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.43.md).

## 1.0.0-beta.8.42 — Y2Linux 1.0 Beta 8.42 (Baseline 163), 2026-10-28: sleep, quick scan, report fixes

Published as `baseline-163` (Reborn `25b8e06`; sequence 10900). From the 2026-10-28 review of 40 error reports: after a Bluetooth loss (a sleep turns Bluetooth off, a link drops) Play with nothing in the jack waits up to 20 s for those headphones instead of the jack or the speaker (`LostPeer`, `3a4860b`); only the platform's credential reasons mean a wrong Wi-Fi password, `ap_unavailable` is Network Not Found (`3a4860b`); a Power key still held after a wake starts a hold (EVIOCGKEY, `13f03d0`); a screen-off refused with EACCES before Reborn set a mode counts as done (`25b8e06`). Details: [Y2Linux Beta 8.42 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.42.md).

Sleep (Y2Linux F47/F48): Power turns the screen off at once, as stock, and no longer opens the Sleep page; a press that wakes the player during the preparation returns where it was; a refused sleep keeps the screen dark (`57b47b2`, `9ee61f0`; test build 160 on the owner's player).

Quick scan (`c2ef3af`, report `d32f8f3c`: 62–70 s per restart to list 70 500 files on exFAT). `ScanMode` Rebuild / Walk / Quick in `reborn-library`. The automatic scans (`Scanner::scan`: start, storage change, after a USB copy) are Quick: a folder whose modification time is unchanged since the last complete walk is not read again while the storage's free space equals the free space then (`quick_fingerprint`: exFAT or ext4 from mountinfo, FAT32 always walked whole because other systems leave its free count stale). Skipped folders keep their songs, counts, playlists and subfolders from the additive tables `scan_folders` / `scan_volumes` (written only after a complete verified walk, with `METADATA_REVISION`); their rows count as seen, so deleted files are still pruned. Scan for Music and the control `scan` command are `Scanner::scan_all` (every folder). A tag edit made on a computer that changes neither a folder's time nor the free space shows after Scan for Music. `scan_completed` gains `quick` and `folders_skipped`. Tests `quick_scan_tests`; workspace tests, strict Clippy and fmt pass. Device timing owed.

## 1.0.0-beta.8.41 — Y2Linux 1.0 Beta 8.41 (Baseline 159), 2026-10-27: internal speaker, haptics

Published as `baseline-159` (Reborn `1358702`; sequence 10700). The Headphone Jack output plays on the internal speaker while the kernel reads the jack empty (Settings > Sound > Output > Speaker, on by default): `reborn_platform::jack` (the card's "Y2Audio Headphone" SW events, the DAC on either I2C bus), `SinkSpec.speaker` and native route 2 (Speaker pin, Master −3 dB), `VolumeRamp::mono` ((L+R)/2: the DAC's speaker route plays the left slot). Headphones in move a playing speaker to them, headphones out pause; jack changes run as model actions (test build 157 hung at "Starting" without). Haptics (#28): Customize > Haptics Off/Light/Strong, `reborn_platform::haptics::Motor`, one 60 ms tick per button press as stock. `rebornctl jack [in|out]` for device tests. Details: [Y2Linux Beta 8.41 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.41.md).

## 1.0.0-beta.8.40 — Y2Linux 1.0 Beta 8.40 (Baseline 154), 2026-10-27: identity only

Published as `baseline-154` (Reborn `77c54e2`; sequence 10500). No Reborn change: the release is a kernel fix (Power Off on a charger restarts into the charging screen, ledger F46). Details: [Y2Linux Beta 8.40 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.40.md).

## 1.0.0-beta.8.39 — Y2Linux 1.0 Beta 8.39 (Baseline 153), 2026-10-26: Folders by file name, Shuffle Albums, playlist Sort, 120 000 songs

Published as `baseline-153` (Reborn `7cf527d`; features `894a99c`; sequence 10470). Folders list folders then songs by name (`sort::natural_key`), songs by file name (`catalog::Row::FolderTrack`), from `folders::FolderIndex` (per library: each folder's songs, folders, song count); a song plays its folder in that order, a folder's Play goes folders first (`FolderIndex::play_order`). `ShuffleMode` Off/Songs/Albums (`settings.shuffle` + `shuffle_albums`, `queue::album_shuffle`, `shuffle_source_albums`; skins `shuffle_albums`). `PlaylistSort` per playlist (`settings.playlist_sort`, `Ui::shown_order`). For 120 000 songs: whole-library lists kept per library, album totals, `Ui::prewarm` while the screen is off, playlists from the scan (`ScanMetrics::playlists`, worker `Job::Known`, `cache/playlists.json`), search folds names once; metrics `ui_action_ms`, `ui_layout_ms`. Device numbers: [Y2Linux Beta 8.39 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-8.39.md).

## 1.0.0-beta.8.38 — Y2Linux 1.0 Beta 8.38 (Baseline 146), 2026-10-25: Bluetooth pause, live wave

Published as `baseline-146` (Reborn `6c37d9f`; F43 `990443f`; sequence 10310). On Bluetooth, `Runtime::pause` releases the sink and Play reopens at the position (BlueALSA in-place resumes stayed silent with AirPods Pro 2, ledger F43). The playing wave (`components::wave_progress`) is an anti-aliased ribbon whose height and ripple follow `Levels` (bass, mids, highs) measured in the audio thread before the volume (`app/reborn/src/meter.rs`, timed by the sink delay; `Playback::heard`, `Ui::set_heard`, smoothed by `Ui::wave_levels`); Home's card shows it too.

## 1.0.0-beta.8.37 — Y2Linux 1.0 Beta 8.37 (Baseline 144), 2026-10-25: sleep timer, search, scrolling

Published as `baseline-144` (Reborn `69232c2`, sequence 10200). Sleep timer picker (`Modal::SleepTimer`, `SLEEP_MINUTES` 5 min to 3 h, `minutes_label`; skins `{sleep}`, `"if": "sleep"`, icon `moon`, every shipped skin's output line), search (#44: `keyboard::Outcome::Leave`, empty start, `Catalog::playlists`, sections of `SECTION_PREVIEW` with `search_all:<section>`, `Catalog::search_songs`), the playlist page's focus, and one way of scrolling: headers stay, only lists scroll ([Product UI v4](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-UI-V4.md), last sections). Device-checked on the owner's player.

## 1.0.0-beta.8.36 — Y2Linux 1.0 Beta 8.36 (Baseline 138), 2026-10-25: issue fixes, one menu order

Published as `baseline-138` (Reborn `92b9c9a`; fixes `d340263`, redesign `92b9c9a`; sequence 10050). Fixes from the GitHub issues: `art_key` gives a song without an album its own cover (#43); skins mark Up Next's playing row by queue entry (`Ui::entry_key`, #60); `keep_up_next_focus` keeps the focused song when rows move, the fallback is the nearest selectable row (#32); `split_genres`/`Track::genres` and `joined_names` ("A, B") for joined tags (#40). Owner's menu rules (spec: [Product UI v4](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-UI-V4.md), last section): one order in every song and collection menu (test `every_menu_lists_its_shared_actions_in_one_order`), Up Next Add to Queue (`entries_last`, `Effect::QueueEntriesLast`), Save Up Next as Playlist… / Clear Queue / Clear Up Next on the song playing, Play and Shuffle for playlists; Customize: Cover Flow On/Off (albums and audiobooks), Artists All / Album Artists (`albumartist:` filter, `album_artist_of`), Now Playing Wheel Volume / Seek (`NowPlayingWheel`); album filters carry a genre (`album_parts`) with Show All N Songs; sheet values and skins' `{detail}` use the room their label leaves (`Scene::label_end`). Device-checked on the owner's player.

## 1.0.0-beta.8.35 — Y2Linux 1.0 Beta 8.35 (Baseline 136), 2026-10-25: louder headphones, safe by default

Published as `baseline-136` (Reborn `e0921a0`, change `5a40103`, sequence 9902). Report F45 (FiiO FH7 too quiet at High): each `HpLevel` has its own DAC Master (`master_db`: Low −9, Medium −6, High 0 dB → ≈0.35/0.71/1.73 Vrms at volume 100; Beta 8.5–8.34 held −19.5 dB for all), set by the C sink (`rb_wired_masters`) for the level the amplifier really runs at, −24 dB until then. The volume is even in dB (`volume_db`: 0.6 dB a step from 10, 3 dB below, −81 dB at 1). Safe level `SAFE_PEAK_DBV` = the old loudest output (−14.7 dBV; safe volume 90/80/67): wired volume up stops there and opens `ConfirmAction::LoudVolume`; `Settings::loud_ok` lapses after `LOUD_LISTENING_LIMIT_S` (20 h) above it. `prepare_wired_start` moves an old-scale volume once (`volume_scale`), gives the wired volume back and caps the start; a return from Bluetooth is capped too; a level change keeps the loudness (`volume_for_level`). Device-checked on the owner's player (migration, Master per level, warning); output not measured with a meter.

## 1.0.0-beta.8.34 — Y2Linux 1.0 Beta 8.34 (Baseline 135), 2026-10-24: MTP fix in the platform

Published as `baseline-135` (Reborn `01f1ed3`, identity only, sequence 9802). The fix is Y2Linux's (#61: MTP no longer hangs when a computer connects); Reborn is unchanged since 8.33.

## 1.0.0-beta.8.33 — Y2Linux 1.0 Beta 8.33 (Baseline 134), 2026-10-24: search page and queue redesign

Published as `baseline-134` (Reborn `eca7f49`, sequence 9702; 8.32 was never published), installed on the owner's player first. Search is one page with the keys over it: first results above the keys, Up/wheel/Search fold the keys into the results (Artists, Albums, Audiobooks, Songs under headings, Play All), the field brings them back. Queue (`reborn_core::queue`): your queued songs play first (Add to Queue before the rest, Play Next on top), queue edits, Shuffle and Repeat no longer restart the song (`Playback::set_upcoming`), Repeat All wraps on Next, Previous restarts the first song, Shuffle on/off reshuffles or restores what plays. Up Next opens on the song playing with a 50-song history above, QUEUE / NEXT FROM headings, Move with the wheel, Select Songs (also Songs, albums, search), queue actions for albums/artists/genres/folders/search, a NEXT line on Now Playing. Session schema 3 (queue by reference). `rebornctl action NAME` for device tests of hold menus. Also #38 (artists of joined tags). Design: last two sections of [Product UI v4](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-UI-V4.md).

## 1.0.0-beta.8.31 — Y2Linux 1.0 Beta 8.31 (Baseline 130), 2026-10-24: left/right balance

Published as `baseline-130` (Reborn `b12a1ee` + identity `b07cb9d`, sequence 9500), installed on the owner's player first. Settings → Sound → Balance (user request: one ear hears less): `settings.balance` -10..=10 dB (negative = left louder), applied per channel at the live sink gain (`VolumeRamp::balance`) by lowering the other side, so it never clips; jack and Bluetooth, live. The list opens on the current value; the Sound page drops its first row once the focus reaches Balance. Previews 29d, 29e.

## 1.0.0-beta.8.30 — Y2Linux 1.0 Beta 8.30 (Baseline 129), 2026-10-24: GitHub triage fixes

Published as `baseline-129` (Reborn `20a493b` + seek fix `44481c3`, sequence 9401), installed on the owner's player first. Music queues never include audiobook parts (`track_matches` requires `is_music`, `play_index` too; Y2Linux #58); a song picked on Songs is followed by the next row (`filtered_indices` uses the catalog for Songs; #21); Previous more than 3 s into a song restarts it (#21), and a pending seek ignores late position reports (the restart kept playing on in the device test); headphones with AVRCP absolute volume follow `settings.volume` through BlueZ's transport `Volume` with the software level at full, changes on the headphones come back, `wired_volume` keeps the wired level and the first takeover never gets louder (#22, not run with real headphones); a toast too long for one line takes two (16 were cut, Y2Linux #55). Preview 44b.

## 1.0.0-beta.8.29 — Y2Linux 1.0 Beta 8.29 (Baseline 128), 2026-10-24: charging fix (platform only)

Published as `baseline-128` (identity `e58980c`, sequence 9300). No Reborn code change: the release fixes charging on players whose PMIC has no die calibration fuse (Y2Linux kernel, report 09888d70).

## 1.0.0-beta.8.28 — Y2Linux 1.0 Beta 8.28 (Baseline 127), 2026-10-23: Wi-Fi wrong password (#20)

Published as `baseline-127` (Reborn `e5b54fb` + identity `f6eb0b2`, sequence 9200), installed on the owner's player first. #20: a wrong password was saved at once and never said. Now the Wi-Fi worker tries a join before saving it (`PendingJoin`: ATTACH, SELECT_NETWORK, the supplicant's events; kept only on connect, older entries of the same name removed, the other saved networks enabled again; a failed try removed and the previous network back). A wrong typed password reopens the keyboard with the text and Wrong password; rows say Checking password… / Wrong password; a saved network whose password failed asks for the new one; Change Password in its menu; `rebornctl test wifi-join` and `wifi-join-wrong`.

## 1.0.0-beta.8.27 — Y2Linux 1.0 Beta 8.27 (Baseline 126), 2026-10-23: SD cards with errors

Published as `baseline-126` (Reborn `c1e60d6` + identity `4947352`, sequence 9100), installed on the owner's player first. The platform mounts a FAT32/exFAT card whose check finds errors read-only: `SdCard::ReadOnly` (or `Unchecked` after an unfinished check) plays, Settings → Storage says Has errors · Playing only and offers Repair SD Card (red confirmation; `PlatformTask::SdRepair` stops playback from the card, runs `y2-platform media repair` and names the outcome); a notice when such a card comes in. A healthy card is read-only between writes: playlist changes on the SD run inside the platform's write window (`client::sd_write_window`), and a read-only refusal is said plainly.

## 1.0.0-beta.8.26 — Y2Linux 1.0 Beta 8.26 (Baseline 125), 2026-10-23: version only (platform report fixes)

Published as `baseline-125` (Reborn `404edb3`, sequence 9000). No Reborn code change: 8.26 fixes platform findings F35–F41 from uploaded reports (battery start on a charger, Wi-Fi switch-on after a sleep with Wi-Fi off, charging, shutdown trail, report evidence; see the Y2Linux Beta 8.26 report).

## 1.0.0-beta.8.25 — Y2Linux 1.0 Beta 8.25 (Baseline 124), 2026-10-23: version only (#52/#54 kernel fix)

Published as `baseline-124` (Reborn `40386bc`, sequence 8901). No Reborn code change: 8.25 changes how the kernel starts the DAC's crystal (#52, #54; see the Y2Linux Beta 8.25 report).

## 1.0.0-beta.8.24 — Y2Linux 1.0 Beta 8.24 (Baseline 123), 2026-10-23: wired output at 44.1 kHz only (#52)

Published as `baseline-123` (Reborn `e199d9c`, sequence 8800), installed on the owner's player before publishing. #52: every failure was a 48 kHz start through the DAC's PLL, which stock never runs (stock output: 44.1 kHz only). The wired plan always asks for `reborn_audio::WIRED_RATE` (44.1 kHz) and the decoder converts other rates; the kept-sink rule is now "wired, 44.1 kHz", so tracks of any rate play on in the open sink (device: 50 reuses across 48/44.1 kHz, 0 reopens). The per-rate `wired_plan`, the rate fallback and the unused rate arguments are gone.

## 1.0.0-beta.8.23 — Y2Linux 1.0 Beta 8.23 (Baseline 122), 2026-10-22: output kept, DAC hold, update task queue

Published as `baseline-122` (Reborn `0779d8b`, sequence 8705), installed on the owner's player before publishing. #52/#54: the wired sink stays open across track changes with the same output, rate, format and wired settings (old audio dropped, 10 ms fade-in, closed 2 s after the last stream or at Stop; `audio/sink_reused`, `audio/sink_reopened`), and `power::dac_hold` keeps the DAC powered through the kernel's `y2_hp/hold` from startup/screen wake to screen-off (`dac_hold` on `screen_wake`/`screen_blank`). F33: Update Now waits for the platform worker's next turn; the update screen gives up after 30 s without a task. Device: 17/17 same-format skips reused the output, hold follows the screen.

## 1.0.0-beta.8.22 — Y2Linux 1.0 Beta 8.22 (Baseline 121), 2026-10-22: Date & Time, report fixes

Published as `baseline-121` (Reborn `e196033`, sequence 8607), installed on the owner's player before publishing. Settings → Display → Date & Time sets the clock by hand (#53; read-only while the clock is network time). Report fixes: a busy wired output is retried for 2 s inside the open deadline and names its holder (F24), an unknown codec outcome clears when the headphones drop or reconnect (F25), Pair waits for the reconnect owner (F28), a cancelled pre-open no longer logs every queued track (F29). The headphone crystal changes (#52/#54) are the kernel's.

## 1.0.0-beta.8.21 — Y2Linux 1.0 Beta 8.21 (Baseline 120), 2026-10-22: headphone crystal run as stock (#52, #54)

Published as `baseline-120` (Reborn `cdc6b43`, sequence 8500), installed on the owner's player before publishing. No Reborn code change (identity only): the fix is the kernel's (Y2Linux overlay 0030: the CS43131 crystal starts with the codec and is used after 1 s like stock, codec autosuspend 5 s). The 5-s sink open deadline of 8.20 covers the 1-s wait.

## 1.0.0-beta.8.20 — Y2Linux 1.0 Beta 8.20 (Baseline 119), 2026-10-22: headphone crystal (#52)

Published as `baseline-119` (Reborn `cdae78e`, sequence 8400), installed on the owner's player before publishing. The sink open deadline is 5 s (`34a07b6`): on a player whose CS43131 crystal misses its start, the kernel's tries and rail cycle take ≈1.4–1.9 s per open and the sink opens twice, so 2 s gave up during the second open (#52). The crystal itself is the kernel's (Y2Linux overlay 0030: 15 µA bias after a failure).

## 1.0.0-beta.8.19 — Y2Linux 1.0 Beta 8.19 (Baseline 118), 2026-10-21: audiobooks, covers, Customize

Published as `baseline-118` (Reborn `da5b777`, sequence 8302; 8.18 was a test build, never published), installed on the owner's player before publishing. Audiobooks (`11febec`…`da5b777`, plan, code map and device test in [REBORN-AUDIOBOOKS](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-AUDIOBOOKS.md)): `reborn_core::books` (detection by folder/`.m4b`/genre, grouping, natural order, chapters, `Listening`, `Shelf` in `state/books.json`, rewind), `rb_media_chapters`, `admit_streams` (cover video track), `av_max_alloc` 128 MiB (long M4B), `heavy_mp4` scan, `RbDspConfig.speed` with `atempo`, sleep timer (`sleep_timer.rs`), Home/list/book page/Now Playing/skins (`views_books.rs`). Covers (`4895db4`): art 180, thumbs 128 from the picture, CPU half/quarter levels (`level_block`/`level_source`), centre crop, Lanczos, 4:2:0 LRU cache of 3 000. Customize (`820fa50`): Wrap Around; When Screen Off and the 15-min headset grace (`ad4fdba`).

## 1.0.0-beta.8.17 — Y2Linux 1.0 Beta 8.17 (Baseline 114), 2026-10-21: report fixes

Published as `baseline-114` (Reborn `6d5458c`, sequence 8100). Bluetooth (`6a31a53`): a disconnect seen in either of two snapshots of a tick is kept (`bt_lost |=`), `StartDiscovery` 15 s with InProgress/late NoReply as scanning, intents go to `/run/y2/bt-intent/bt-control.ini` (the reconnect owner never read `/run/y2`), `BusyRetry` for a busy lock or a busy BlueZ Connect answer (45 s window), a definite failure writes `failed` (only NoReply/timeouts `uncertain`). Player (`d6523b5`): a Play refused for a missing A2DP peer pauses as a disconnect; `SdCard::CheckTimedOut` and refused-card wording instead of "Reinsert"; BlueALSA drain -EIO leaving SETUP is a pause; radio `sniff()` for text/bytes playlists, `station_failed` with HTTP status and content type; one renderer off/on retry for a failed frame within 30 s of a wake (main loop only, not inside `sleep_restore`).

## 1.0.0-beta.8.16 — Y2Linux 1.0 Beta 8.16 (Baseline 113), 2026-10-20: large libraries

Published as `baseline-113` (Reborn `eea9312`, sequence 8000). From a 28 600-song report: `MAX_QUEUE` is 5 000 (`queue_window`: the chosen song with a tenth before it; Shuffle a random 5 000; `play_members` picks positions before cloning; `AppModel::restore` trims an older larger queue) (`122607f`). The scan probe takes matching ids from its indexed lookup instead of an `INSERT…SELECT` planned as a walk over the whole source (749 s of a 759 s no-change rescan) (`5c7e768`). Tags of new/changed files are read by `read_parallel` on up to 3 threads (`scan_workers`, after the LibraryScan lease restored the cores; `reborn_platform::lower_thread_priority` nice 10), applied in file order (`4922cab`).

## 1.0.0-beta.8.15 — Y2Linux 1.0 Beta 8.15 (Baseline 112), 2026-10-20: CJK text, update check, codec retry

Published as `baseline-112` (Reborn `2ef41d3`, sequence 7900). Text lookup is exact face → fallback page → Noto Sans CJK (`/usr/share/fonts/noto-cjk/NotoSansCJKjp-Regular.otf`, `REBORN_CJK_FONT` overrides) → U+FFFD; missing glyphs are rasterised at the face's size into a runtime 1024² A8 page (`reborn-graphics/src/glyphs.rs`, `reborn-ui/src/glyph_cache.rs`, texture slot 9, LRU shelves, ≤ 48 new glyphs a frame), font memory-mapped on first need (`a3b1943`). A failed update check flashes Couldn't reach the update server and the page keeps Update Now; `network_not_online` maps to NeedsNetwork (`cdf8c7b`). The Bluetooth worker retries a codec choice refused while the peer is still connecting (2 s, 5 tries; `b8cd9a7`). Not run on a player before publishing (owner updates by OTA).

## 1.0.0-beta.8.14 — Y2Linux 1.0 Beta 8.14 (Baseline 111), 2026-10-20: shuffle, seek, genre Shuffle, titles

Published as `baseline-111` (Reborn `5cda8bb`, sequence 7800; changes in `2861ec9`). `play_members` seeded its Fisher-Yates shuffle from the selected track's ID and index, and Shuffle rows always selected the first member, so every Shuffle played one fixed order: now `reborn_platform::random_u64()` (getrandom) seeds a splitmix64 shuffle, a Shuffle row (`force_shuffle`) shuffles every member, a song picked with Shuffle on stays first. `Effect::Seek` carries only the direction; `seek_step` sizes held-seek steps 1 s → 3 s (after 1.5 s) → 10 s (after 4 s), at most 1/60 of the song (was 30 s every 90 ms). A genre's album list has Shuffle (`shuffle:collection`) under All Songs, also skipped by Cover Flow's album detail. The Home card's title is fitted to 200 px. Owner checked all four on build 111.

## 1.0.0-beta.8.13 — Y2Linux 1.0 Beta 8.13 (Baseline 110), 2026-10-20: library tags over MTP

Published as `baseline-110` (Reborn `21cd3b0`, sequence 7701); no Reborn source change besides the identity. Y2Linux's MTP responder (umtprd overlay 0005) now reads Reborn's library read-only (`/data/reborn/library.db`: `tracks` joined to online `sources` by absolute `path`, `deleted=0`) to report title, artist, album, album artist, track, duration, sample rate, channels and bitrate to libmtp clients such as Strawberry. **The `tracks`/`sources` columns it reads are now an interface:** renaming them falls back to file names over MTP (no failure). Pause/resume silence on wired output was the #48 crystal path on the reopen after a 180 s hold, fixed in 8.12 and checked on a player.

## 1.0.0-beta.8.12 — Y2Linux 1.0 Beta 8.12 (Baseline 108), 2026-10-20: playlist crash loop, crash isolation, audio open retry

Published as `baseline-108` (Reborn `90f3da6`, sequence 7601). An M3U line with a multi-byte character across byte 8 (`’`, `º`) panicked the playlists thread at `reborn-platform/src/playlists.rs:223` (`trimmed[..8]`) on every scan with the SD card; the panic hook ends the process, so three players crash-looped and updates rolled back (Y2Linux #49). Fixed there and in `reborn-ui/src/playlist_index.rs` (`text[..7]`, `percent_decode`) (`3ff346a`). `reborn_observability::isolated()` turns a panic on one user file into an error: the hook writes `panic-last.json` with `"isolated": true` and returns instead of `exit(101)`; used per playlist file/job, per cover decode and per scanned song (`bc2762d`, test `crates/reborn-observability/tests/isolated_panic.rs`). A refused output open is tried once more after 250 ms (CS43131 crystal, Y2Linux #48; `2db37cf`). Test build 107 on the maintainer's player: crash playlists listed and opened, no panic.

## 1.0.0-beta.8.11 — Y2Linux 1.0 Beta 8.11 (Baseline 106), 2026-10-20: storage setup waiting for a charger

Published as `baseline-106` (Reborn `727fd47`, sequence 7500). `InternalSetup::Pending` carries `SetupWait` from the platform's reason: `battery_low`/`battery_unknown` → Settings → Storage says Connect a charger and restart; anything else (an update's health boot) keeps Restart to finish setting up. Before, every Pending said restart, and a user restarted on battery again and again without the setup ever running (Y2Linux report 20261019-153610; the platform gate is now 25 % by power-on OCV). Preview `32-storage-setup-battery`; tests in `client.rs` and `internal_storage_setup_is_offered_only_for_a_waiting_old_library_and_confirmed_red`. Not checked on a player.

## 1.0.0-beta.8.10 — Y2Linux 1.0 Beta 8.10 (Baseline 105), 2026-10-19: report progress, no topic, uploads

Published as `baseline-105` (Reborn `cfac12b`, sequence 7400), with the uploads entry below.

### Report progress, no topic

Send Report Now sends at once: `PlatformTask::ReportSend` has no topic, `Screen::ReportTopic` and `ReportTopic` are gone (every report holds everything). While a report is made, About & Updates → Error Reports shows its live progress like the update download: `client::report_progress` reads Y2Linux's `/run/y2/report-progress.json` every 200 ms while `ReportSend`/`ReportSave` run (`PlatformState::report`, `ReportLive`, `ReportStep`), and `views_settings::report_progress` draws the steps Collect · Clean · Send (or Save), the percent, the gliding bar, what happens ("260 of 504 KB", "Into the Error Reports folder.") and the time left; before the first record "Starting…" sweeps. Previews 33f, 33l–33o; test `a_running_report_shows_its_steps_percent_and_what_happens`; 545 tests, strict Clippy.

### Uploads

With the platform's uploader (Y2Linux ERROR-REPORTS-PLAN R4): Send Report Now flashes "Report sent" when the report went out at once (`last.state == "sent"` in the reply), "Report saved · waiting to send" otherwise; the page names a dropped report (refused by the receiver or unsent after three days) as "couldn't be sent". The switch, Send Report Now, the install ID and the question appear when the image carries the upload key (`upload: true`).

## 1.0.0-beta.8.9 — Y2Linux 1.0 Beta 8.9 (label 102), 2026-10-19: Save Report without a topic

Built and installed on the owner's player, not published (Reborn `4da5f84`, sequence 7100). Save Report asks only for the storage: `report_dest:<destination>` returns to the Error Reports page and starts `PlatformTask::ReportSave(destination)` (`y2-platform report save --to …`, no `--topic`). The topic never changed a report's content (`report.py` collects the same sections for every topic; it was only a label in `report.json`), and a saved report goes with a GitHub issue that says what went wrong. `Screen::ReportTopic` stays for Send Report Now, where the topic is the only thing the owner tells the receiver. The storage rows lose their chevron. Test `without_an_uploader_reports_are_saved_to_the_chosen_storage` updated; 543 tests, strict Clippy.

## 1.0.0-beta.8.8 — Y2Linux 1.0 Beta 8.8 (Baseline 101), 2026-10-19: Save Report

Published as `baseline-101` (Reborn `b6b6fbc`, sequence 7000), with the error report screens below. About & Updates → Error Reports → Save Report → storage (`ReportState::destinations`, `report_dest:<internal|sd>`) → topic (`Screen::ReportTopic`, filter `save:<destination>`) → `PlatformTask::ReportSave(topic, destination)` → `y2-platform report save --to … --topic …`; afterwards back on the Error Reports page, which shows the progress and "Last report saved to …". While the platform says `upload: false` (no uploader yet), the page shows only Save Report and What Is Saved, About & Updates shows no On/Off and `ask_about_reports()` asks nothing. A report takes ≈10 s. Test `without_an_uploader_reports_are_saved_to_the_chosen_storage`, previews 33h–33k; 543 tests, strict Clippy.

## Error reports screens (2026-10-18; on the owner's player as test build 98, released in 8.8)

Reborn `8ba33b3` and `fbecb77` (versions 1.0.0-beta.8.8 test builds 97–98, not published). Plan: Y2Linux `docs/planning/ERROR-REPORTS-PLAN.md`.
  - About & Updates → Error Reports (`Screen::ErrorReports`, filter `info` for What Is Sent): the switch

(`PlatformTask::ReportEnable`), Send Report Now (`Screen::ReportTopic`, seven `ReportTopic`s → `PlatformTask::ReportSend`), the install ID (`ReportState::short_id`, New ID confirm → `ReportNewId`), the last report's state. The row is hidden on platforms without `y2-platform report`.
  - The platform refresh also reads `y2-platform report status` (`client::report_state`, `PlatformSnapshot::reports`);

report tasks answer `client::Reply::Reports`. One observation runs 20 s after start on any screen.
  - One-time question `ConfirmAction::ReportsQuestion` ("No Thanks" / "Send Reports", both recorded), opened by

`ask_about_reports()` only on a lit screen, with no other dialog and 5 s without a button press.
  - Previews 33b–33g; tests `error_reports_page_switches_sends_and_names_the_last_report`,

`the_error_report_question_records_no_as_well_as_yes`, `report_status_is_read_from_the_platform_record`. 542 tests, strict Clippy.

## 1.0.0-beta.8.7 — Y2Linux 1.0 Beta 8.7 (Baseline 95), 2026-10-18 (latest): identity only

Published as `baseline-95` (Reborn `82fe089`, sequence 6900). No Reborn change: the release identifies GC9503V players from LK's panel name (Y2Linux kernel, #45/#46).

## 1.0.0-beta.8.6 — Y2Linux 1.0 Beta 8.6 (Baseline 94), 2026-10-18: audio playback review

Published as `baseline-94` (Reborn `cefcc8a`, sequence 6800). Device results: Y2Linux Beta 8.6 report (test build 94 on the owner's player = the release: profile list, `dsp_rise_fade`, `fade_continued` after Next, `pause_released`, no restart for the same level; CPU floor 598 MHz with a profile instead of 747.5, ≥16 % fewer decode-thread cycles). Findings and answers: Y2Linux handoff and audits AUDIO-REVIEW-8.5 / BETA-8.6.
  - Fades: an unfinished fade-in carries into a reopened sink (Next, a seek, another rate: `opening_gain`,

`VolumeRamp::fade_in_from`, `fade_progress`), and volume up during a fade keeps fading towards the new volume (volume down still acts at once). A load whose sound settings play ≥ 1 dB louder somewhere than the previous load's fades in over 2 s too (`dsp_rise_fades`, `reborn_core::eq::level_rise_db`, `LoadRequest::fade_in`, event `dsp_rise_fade`): a profile turned off (its preamp and cuts come back), a boosting preset, any Normalize change. Not the first load after start (it plays what was saved, as the level does).
  - Held pause: every sound-settings change (`reload_dsp`, now also Normalize and Reset Settings) releases a held

pause, so Play starts with the new settings instead of the old level/EQ. Choosing the Headphone Level already in use does nothing (it restarted the song).
  - Battery: an equalizer or profile no longer asks for `PlaybackHeavy` (747.5 MHz floor, 1 ms wake-up limit

that blocks deep idle); only crossfade does (`Settings::playback_heavy`). The FFmpeg graph uses one thread (`media.c`): host, FFmpeg 9.0.2, HD 650, 5 min: 43 % (1152-sample frames) / 20 % (4096) less CPU, bit-identical output. Device mA and CPU owed.
  - Profiles: the clip-safe preamp now covers source rates 44.1–384 kHz (filters run before resampling): six

shipped profiles 0.1–0.4 dB lower (Sony WF-1000XM4 −7.7 → −8.1, HD 650 unchanged −6.4); a stored profile is re-sanitized at start. Rates below 44.1 kHz stay out (FFmpeg skips filters above Nyquist; covering them would lower many profiles by up to 6 dB); the limiter covers them. The shipped folder lists only `*ParametricEQ.txt` (the license file appeared as a profile "LICENSE-AutoEq").
  - Tests: layout of `RawDspConfig`/`RawParams` pinned on both sides (`_Static_assert` + `const` assert),

sanitize idempotence over all shipped profiles, `preamp_covers_hi_res_source_rates`, a full HD 650 profile with ReplayGain +6 dB on the new near-full-scale fixture `loud-24-96000-rg.flac` at S24 and S16 (limiter holds ≤ 0.981, mutation without the limiter clips), the real shipped-folder scan (47, no license), fade/opening gain, DSP rise. 539 tests, fmt, strict Clippy.

## 1.0.0-beta.8.5 — Y2Linux 1.0 Beta 8.5 (Baseline 93), 2026-10-18: headphone level, headphone profiles, DAC filter
  - Needs Y2Linux's `HP Output Level` kernel control (older kernels: Master stays −24 dB) and FFmpeg's

`lowshelf`/`highshelf` (Y2Linux `docs/HEADPHONE-OUTPUT.md`). Device results: Y2Linux Beta 8.5 report (test builds 91–93 on the owner's player).
  - Headphone Level (Settings → Sound → Output): `Settings::hp_level` (Low default = stock level, Medium, High), passed to

`reborn_audio::wired_configure` at startup and on a change. `rb_sink_open` sets the kernel controls before the stream starts, sets Master to −19.5 dB with the control (−24 dB without it) and reads `HP Output Level Live` after the pin switch. A higher level fades in over 2 s (`VolumeRamp::fade_in`, `Parameters::level_raised`, `rb_wired_note_live`; also when the rise was chosen with no stream since boot). A change restarts wired playback and releases a held pause.
  - DAC Filter (Settings → Sound → Output): `Settings::dac_filter` (Fast, Fast/Slow phase compensated, Slow,

Nonoversampling), set live through the upstream controls.
  - Headphone Profile (Settings → Sound → Equalizer): `reborn_core::eq` parses AutoEQ / Equalizer APO

`ParametricEQ.txt` (PK, LSC, HSC with Q, OFF lines and comments skipped, anything else refused, ≤ 10 filters). The clip-safe preamp is min(file preamp, −peak of the combined RBJ response from 10 Hz to Nyquist at 44.1/48 kHz), rounded down to 0.1 dB. Files come from `EQ` folders on Internal Storage and SD cards; `Settings::eq_profile` keeps a copy and `eq_profile_on` plays it instead of the five bands (a preset or a band edit turns it off). 47 AutoEq profiles of common headphones and IEMs ship in `assets/eq` (pinned AutoEq commit, MIT, `SOURCES.md`, refetch with `tools/assets/fetch_eq_profiles.py`; test `shipped_profiles_all_import`), installed to `/usr/share/reborn/eq` and listed with the storage `EQ` folders (a storage file replaces a shipped one by name). Engine: `EqBand::kind`, 10 bands across the FFI, `DspConfig::preamp_db` in the gain stage before the filters, `equalizer`/`lowshelf`/`highshelf` in the graph, limiter unchanged. The equalizer curve shows the profile's response.
  - Sound stays one screen (owner chose layout C of three): Equalizer, Normalize, Gapless, Crossfade and the

Output card ("Level Low · Filter Fast" for the jack). The card opens `Screen::Output`: the outputs (current one checked, replacing the output modal there) and a Headphone Jack group with Level and DAC Filter (pickers `HeadphoneLevel`, `DacFilter`; skin layouts `output`, `headphone_level`, `dac_filter`). Settings → Sound names an active profile. Previews 27-sound, 27b-output, 27c-sound-wired, 28-equalizer, 28b, 28c, 29b, 29c. 529 tests, strict Clippy.

## 1.0.0-beta.8.4 — Y2Linux 1.0 Beta 8.4 (Baseline 90), 2026-10-18 (latest): restart display fix
  - No Reborn code change; the release carries Y2Linux's fix for the dark display after a restart (SMI gates reopened

as the last step of a restart). A dark start had made Reborn's first frame time out and an update roll back.

## 1.0.0-beta.8.3 — Y2Linux 1.0 Beta 8.3 (Baseline 89), 2026-10-18: seconds left
  - Checking the Update shows the seconds left from the core's check line (`"<percent> check <seconds>"`, Y2Linux

8.3, `reborn_platform::client::parse_download`); with an older core it keeps This takes a few seconds. The install itself runs in the recovery, whose screen now also shows the seconds left.

## 1.0.0-beta.8.2 — Y2Linux 1.0 Beta 8.2 (Baseline 88), 2026-10-18: faster updates
  - No Reborn code change; the release carries Y2Linux's four-core installer and kept rollback copy (OTA-50). The

update screen's steps are unchanged; the install step now takes about 15 s on the owner's player (was 54 s).

## 1.0.0-beta.8.1 — Y2Linux 1.0 Beta 8.1 (Baseline 86), 2026-10-18: panel power-down
  - No Reborn code change; the release carries Y2Linux's panel power-down at screen-off (#45) for the ST7701S panel.

Screen-on after a screen-off now includes the panel's stock initialization (≈0.5 s).

## 1.0.0-beta.8.0 — Y2Linux 1.0 Beta 8.0 (Baseline 75), 2026-10-18: 1.0 review fixes
  - Library: a supported file FFmpeg cannot open is counted (`ScanMetrics::unreadable`, `ScanSummary::unreadable`,

Settings → Library N can't be read), keeps its row through `DbCommand::Retain` and no longer makes the scan incomplete, so deleted songs are pruned again and `library.error` stays clear; failures are remembered per process (`Unreadable` set), a rebuild retries them. Before, one such file rolled every Y2Linux update back (V1 review B3/B4).
  - `rebornctl status`: `healthy` and `health_reasons` (graphics, database, stuck workers; not scan completeness), which

Y2Linux's update health check now reads (R7).
  - A refused session is kept as `session.json.rejected-<time>`; `recover_settings` keeps every setting this version

understands (B7). Wired audio profile matches whole rates (R4). 517 tests. Device: OTA-installed and acknowledged on the owner's player with a broken file on Internal Storage.

## 1.0.0-beta.7.11 — Y2Linux 1.0 Beta 7.11 (Baseline 74), 2026-10-17: faster copies to the player
  - No Reborn code change; the release carries Y2Linux's multi-packet USB receive DMA (copies to the player ≈30 MB/s on

Internal Storage instead of ≈10). New songs still reach the library through the existing change detection.

## 1.0.0-beta.7.10 — Y2Linux 1.0 Beta 7.10 (Baseline 73), 2026-10-17: USB file operations
  - No Reborn code change; the release carries Y2Linux's musb fix for the zero-length-packet crash and MoveObject/CopyObject

in the MTP responder. Reborn's library follows moves and copies through the existing durable-change generations. 514 tests.

## 1.0.0-beta.7.9 — Y2Linux 1.0 Beta 7.9 (Baseline 72), 2026-10-17: Internal Storage setup, #39, #44
  - `platform::InternalSetup` (Unknown · NotNeeded · Pending · Waiting{files, bytes} · Running · Done{kept} · Failed) from

`storage.internal_setup`; `PlatformTask::InternalStorageSetup` → `y2-platform internal-media setup --confirm-shown`.
  - One-time question (`Settings::internal_setup_asked`) for a large old library; Settings → Storage row *Set Up Internal

Storage* (red, enabled only while Waiting, refused while a computer is connected, restarts the player after); Storage card Not set up · Your old files are kept / Restart to finish setting up; message *Internal Storage is ready · Kept N files in Old Player Files*; boot phases `media_setup*` (word stages, no numbers on the boot screen).
  - Radio firmware page names the Firmware folder on Internal Storage or the Firmware drive and *Not Enough Space for That

File* (#39); `SdCard::NeedsRepair`Needs repair · Check it on a computer (#44). Previews 32-storage-setup-*, 32-firmware-no-space, 32-storage-sd-repair. Device: the automatic setup passed on the owner's player.

## 1.0.0-beta.7.8 — Y2Linux 1.0 Beta 7.8 (Baseline 71), 2026-10-16: Last.fm fixes
  - Now Playing re-announced after a pause, a repeat or a failed attempt (`announce_due`, ≤ every 30 s per play); a play

refused with Last.fm error 6 no longer blocks the queue; sign-in and Now Playing wait for a trusted clock; one sign-in request at a time; radio/clock/platform/lastfm/scrobble log events reach the log (allowlist guard test). Device: QR sign-in and real scrobbles confirmed on 7.7.

## 1.0.0-beta.7.7 — Y2Linux 1.0 Beta 7.7 (Baseline 70), 2026-10-16: Last.fm scrobbling
  - `reborn_core::scrobble` (half or 4 min heard, seeks/pauses add nothing, radio/untagged never), `reborn_platform::scrobble`

(fsynced locked JSONL queue, `drop_sent`, Rockbox log, clock trust, CLOCK_BOOTTIME), `reborn_platform::lastfm` (own MD5, curl form on stdin, QR token flow + mobile-session fallback, batches of 50, back-off with random spread), `app/reborn/src/scrobbling.rs`, Settings → Last.fm with an own QR encoder (native in every skin). App key from `/usr/share/reborn/lastfm-api.json` (release image); session 0600 on Y2DATA. Previews 96–96d. 509 tests, strict Clippy.
  - Device: QR sign-in and the first real scrobble confirmed (2026-10-16); offline play sent after sleep still owed.

## 1.0.0-beta.7.6 — Y2Linux 1.0 Beta 7.6 (Baseline 67), 2026-10-16: smooth update screens
  - Owner: low fps on the update download. Cause: download/check counted only as `spinning` (calm 34-ms frame gap, ≤ 29

fps). `Ui::download_shown` (visible, screen on) joins `gliding()` but not `responding()` (no CPU lease); the percentage follows `download_fill`; the sweep fades at its ends; Connecting eases.
  - `views_settings::steps` (Download · Check · Install) replaces "STEP 1 OF 3", also on `views_system::installing`;

10-px bar with a bright head. Preview `34d-update-installing`. 489 tests, strict Clippy.

## 1.0.0-beta.7.5 — Y2Linux 1.0 Beta 7.5 (Baseline 66), 2026-10-16: larger status bar, Skin in Settings
  - Status bar layout C (owner's choice of four rendered variants): `status_bar` draws the Title Case name beside the

back arrow (SemiBold 15, white; call sites no longer uppercase), `status_cluster(.., roomy)` returns its left edge (clock S15, % S13, icons 18 px, Wi-Fi/Bluetooth 22 px, battery 25 × 13); skins keep `roomy: false`. `components::home_bar`: "Reborn" + `short_version`. Message pill 30 px, SemiBold 15.
  - Theme → Skin, a Settings row of its own (seven 44-px rows, `Icon::Palette` added by

`tools/assets/build_ui_assets.py`; font pages unchanged); Display without the scroll rail; About's Music Library row removed (count on Storage → Scan for Music); `Skins` folders read besides `Themes`. 487 tests, strict Clippy.

## 1.0.0-beta.7.4 — Y2Linux 1.0 Beta 7.4 (Baseline 65), 2026-10-16: status-bar messages, cooler wave
  - `components::toast`: a 26-px pill in the status bar with `toast_icon` (subject icon; red warning for problems); the

StatusBar mark's quads (title and status cluster, not the back arrow) are hidden while it shows. Owner chose this placement (C) over below-the-bar (A) and bottom (B).
  - `Ui::responding()` (button-started motion: Cover Flow, slides, settling springs) drives the Interactive CPU lease;

`gliding()` (incl. the playing wave) only the frame pacing. The wave alone runs at the lowest clock.
  - Measured on 7.3: 62 fps median while moving, 64–65 fps wave, 0 missed, 0 fps at rest. 487 tests, strict Clippy.

## 1.0.0-beta.7.3 — Y2Linux 1.0 Beta 7.3 (Baseline 64), 2026-10-16: USB message and symbol
  - Owner: the locked computer screen (7.1) kept the player unusable while connected; a message and a status-bar symbol

instead. `Ui::observe` flashes "Connected to a computer" / "Copying files from the computer…"; `status_cluster` draws `Icon::Usb` while Ready/Copying (accent while copying). Removed: `usb_overlay`, `views_system::usb`, the input lock, `usb_dismissed`, `Settings::usb_developer` and "Use While Connected". 487 tests, strict Clippy.

## 1.0.0-beta.7.2 — Y2Linux 1.0 Beta 7.2 (Baseline 63), 2026-10-16: motion and the Now Playing wave
  - Owner: more animation for a polished, responsive feel, at 60 fps; the progress as a wave, not a perfect sine.
  - `motion.rs`: per-key eased values (QUICK/CALM), retargetable, frame-rate independent; `Motion::moving()` and

`mark_live` feed `Ui::gliding()`, i.e. Cover Flow's 12-ms frame gap and Interactive lease; at rest nothing redraws. `Ui::ui_motion` (runtime on; previews/tests off); `reborn-preview --motion` captures frames mid-animation.
  - Components mark moving quads (`canvas::Moving`), eased by `motion::apply`: focus row and Home marker glide; smooth list

scrolling (±1 extra row, hidden at rest, status bar kept above; long jumps glide one row); sheets rise; dialogs and toasts fade in; switches slide. `Ui::slide_screens`: screens slide (200 ms), skins included.
  - Now Playing: `shown_position` moves on between reports; `components::wave_progress` (travelling, imperfect wave; flat

when paused); a new song fades in; the play button dips on a change.
  - 487 tests, strict Clippy. Device frame rate owed.

## 1.0.0-beta.7.1 — Y2Linux 1.0 Beta 7.1 (Baseline 62), 2026-10-16: one-step update, USB screen, time zone
  - Update: the check's reply sets Up to Date / Available at once (it waited for the next status refresh). Update Now /

Install Now (`Ui::update_run`) download, check and restart to install on one screen that cannot be left, after the charge rule; Cancel = `Effect::CancelDownload` → `client::abort_download()` → SIGTERM to `update stage` (platform cleans up until its commit point). Three-step progress.
  - USB:`client::usb_now()` (UDC sysfs + `/run/y2/usb-transfer.json`) every 0.5 s on every screen (the status was only

refreshed on Settings screens); the screen lights when a computer opens the drives; the computer screen keeps Back/Home/Select while connected; `Settings::usb_developer` (service page "Use While Connected") lifts that.
  - Time zone:`Settings::time_zone_auto` (`zone_auto()`: on where none was chosen); `reborn_platform::geo::zone()` once

per Wi-Fi network (ipapi.co, ipwho.is), only table zones; picker Automatic, UTC, countries A–Z (`reborn_core::clock::countries`, generated by `tools/clock/countries.py`), cities only where they keep different times.
  - 483 tests, strict Clippy. Device checks owed (Y2Linux Beta 7.1 report).

## 1.0.0-beta.7 — Y2Linux 1.0 Beta 7 (Baseline 61), 2026-10-16: UI v4
  - Owner: the UI looked full and rough after playlists, search and radio; make it consistent and for listeners. Review,

owner decisions and every phase: [Product UI v4](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-UI-V4.md).
  - One system: a fixed accent (`Ui::accent`) for controls and state, the cover's colour (`Ui::cover_accent`) only on Now

Playing and the Home cover card; `components::focus_row`, `button`, `empty_state`/`Mark`, `menu_entry`; one LIVE badge. Skins are drawn with the cover accent as before.
  - Home and Music: Home is Now Playing, Music, Playlists, Radio, Search, Settings; Music lists Artists, Albums, Songs,

Genres, Folders with counts; Settings → Display → Home Menu pins lists (`Settings::home_pins`, `Effect::SetHomePin`, `Screen::HomeMenu`). Display scrolls past the brightness card.
  - Less on screen: no hint lines (hold menus name the actions), no NOW PLAYING label, gapless icon or radio codec tags;

stations "Country · Genre" without ranks; Bluetooth Connected/Paired, Wi-Fi Saved/Secured/Open; folder roots show songs; theme swatches (`SkinInfo::swatch`); Storage bars + Scan, About "1.0 Beta 7" + Music Library; Normalize.
  - 479 tests, strict Clippy; previews of 114 states and 16 skins compared by eye. Device tour with screen capture owed.

## 1.0.0-beta.6.3 — Y2Linux 1.0 Beta 6.3 (Baseline 60), 2026-10-16: sleep while paused
  - Owner: Power while paused "does not go to sleep … finishing another task". Device journal (6.2, battery): four requests

refused `activity_operation:808/reborn` (Reborn's PID). An open sink holds a shared flock on `/run/y2/activity.lock` (`audio.c``rb_sink_open`); pause in place keeps the sink open up to 3 minutes; the platform takes its operation locks before it asks Reborn to prepare, so `prepare_sleep`'s release came too late.
  - A sleep request (Power or automatic) now releases a held pause and waits for the sink to close first

(`release_hold_with(true)` → `Playback::stop_and_wait`); Play then restarts at the same place. Platform refusals are logged (`power/sleep_refused`); the release logs `pause_released` with `for_sleep`. Device check owed.

## 1.0.0-beta.6.2 — Y2Linux 1.0 Beta 6.2 (Baseline 59), 2026-10-16: clock, skins for the newer screens, Bunny Bow
  - Clock (PR #10 by samanz, reviewed and merged): the time in the status bar in a zone chosen under Settings →

Display → Time Zone. `reborn_core::clock` converts UTC with each zone's POSIX TZ rule (`zones.rs`, generated by `tools/clock/zones.py` from tz 2026c; the image ships no zone database); DST, half-hour and southern zones tested; hidden while the system time reads before 2025; 12-hour in zones where that is usual (no switch). Reborn's follow-up: the text is made once per minute and zone (`Ui::clock_cache`; host 337 → 16 ns per call) and the picker's zones once per minute (`Ui::zone_rows`; 167 → 25 µs per frame). No new wakeups: one redraw when the minute changes, none with the screen off. "Time Zone" in Title Case.
  - Skins caught up with the screens added since they were made: skin values `{clock}` and `{station}`, conditions

`has_clock`, `live` and `favorite`, icon `heart`, a `keyboard` overlay layout (the skin's title bar over `keyboard::draw_body`), layout names `search`, `playlists`, `playlist`, `radio`, `radio_stations`, `radio_categories`, `radio_info`. For a station, `{title}`/`{artist}`/`{album}` are the announced song, its artist and the station (`views_playing::lines`, shared with Reborn's own Now Playing), `{remaining}`/`{duration}` read LIVE, the progress bar is full, the cover is the logo or the initials; station rows show logos; Station Info's page carries the station's facts (`views_radio::station_facts`). Every shipped skin uses all of it in its own style (clock, live lines, keyboard header, Favorites heart). Reborn's own look: 110 of 110 previews pixel-identical.
  - Bunny Bow, the sixteenth skin: pastel pixel art (a bunny with a red bow, a cloud holding the clock, sparkles,

hearts, pill bars) drawn by `tools/assets/build_skins.py`, inspired by the Rockbox theme bunnyPod (none of its CC-BY-SA art or its font copied). Font Pixelify Sans (OFL 1.1; sources, licence and hashes in `assets/fonts/pixelify`; Y2Linux's `reborn.mk` lists the licence for legal-info).
  - Skin generator is the source again: the clock, radio, keyboard and heart changes are finishing steps of

`build_skins.py` (`add_clock`, `add_live`, `add_keyboard`, `add_heart`), which reproduces all 14 generated skins byte for byte. Classic's layout stays hand-written (`build_classic_skin.py` draws its pictures).
  - Test: every shipped skin loads without warnings, with a clock, a keyboard layout and no queue position for a

station. 474 tests, strict Clippy.

## 1.0.0-beta.6.1 — Y2Linux 1.0 Beta 6.1 (Baseline 58), 2026-10-16: Bluetooth resume, skipping while a song starts, SD duplicates
  - Bluetooth: no sound after Pause and Play. Device log (Beta 6, AirPods): pause in place used BlueALSA's

`snd_pcm_pause` (`device_pause: true`); after resume the position advanced, so audio was written, but the headphones stayed silent. `rb_sink_pause(s, on, device_pause)`: a `bluealsa:` PCM now drains on pause (non-blocking) and is dropped/prepared on resume, as a start does; other PCMs keep the device's pause. Not yet heard on the device.
  - "Couldn't complete that" when skipping: every action was refused while a start was pending (≈1.1 s on

Bluetooth). Next/Previous then step the queue, hold the output and restart once the start in progress ends (`seek_until`); Play/Pause pauses on the chosen song (an output or codec change still restores what worked). The runtime has no host harness for this; device check owed.
  - SD card songs twice (issue #15, samanz): libraries from an image before card ids carried the CID kept the card

under the bare `uuid:` id as well. A complete, identity-checked scan of the card marks those rows (offline, same root) deleted (`retire_pre_cid_copy`); ids with another CID are other cards. PR #14 (samanz) merged after review: the playlist matcher prefers the copy on the player.
  - Review of the Beta 6 day (below) shipped here too.

### Review of the Beta 6 day's changes (in 1.0.0-beta.6.1)

Owner: "analyse the changes we made today … performance problems or code that is double and could be consolidated". Found and fixed:
  - Logo redraw loop: a station logo that could not be fetched (SVG, dead link) was asked for again every

frame and each answer asked for a new frame: with such a station in a list the player never idled. `LogoFetcher` now settles failed (and undecodable) logos for the session and only a saved logo redraws.
  - Playlists per frame: each frame re-matched and copied every visible playlist's entries (mosaic, length,

missing count). Now `Facts` per playlist, built once per file or library change and shared (`Rc`); the heart's Favorites lookup is a set.
  - Playlists are not re-read while a library scan walks the same storage (its end publishes again).
  - The playlist matcher no longer keeps every song path twice (≈1.5 MB at 20 000 songs); the search cache

keeps only beginnings of the current text.
  - Consolidated: one safe file writer (`reborn_core::atomic_write`, now with a hidden per-file temporary —

it used to replace the extension, so `a.json` and `a.ini` shared one, and a playlist briefly showed as `Name.new` over USB) for favorites, logos and playlists; one curl setup; Radio's own station lists read with the playlists' text rules (Windows-1252 names kept); one `count()` wording helper (thousands grouped), one list window, one tinted icon tile, one library stamp.
  - Test isolation: tests that start a station take turns (`live()` names the process's latest station; a

parallel test replaced it — the "flaky" reconnect test).

Checks: 462 tests three runs in a row, Clippy, previews pixel-identical before/after (109 screens × Reborn, Paper, Classic).

## 1.0.0-beta.6 — Y2Linux 1.0 Beta 6 (Baseline 57), 2026-10-15: Playlists, pause in place, collected seeking

Playlists (owner: a playlist feature like Y2Player's, its own section, add/remove on the device, "highly optimized … fix issues Y2Player had"; decisions: playlists anywhere in the music, edits go into the file itself, a Favorites playlist with a heart, moving with the wheel).
  - The .m3u/.m3u8 file is the playlist: no database copy (Y2Player kept card files and device playlists in two

worlds that never met, and exported "Name (2).m3u8" copies). `reborn_platform::playlists` finds them on Internal Storage and the SD card (not the Radio folder, hidden or system folders; at most 1 000), reads UTF-8, UTF-8/16 with a byte order mark and Windows-1252, and writes them back in their own encoding (switching to UTF-8 with a BOM only when a new title needs it), keeping comments, other tools' tags and entries the player cannot find (Y2Player dropped those for good). Writes go to a hidden temporary file, are flushed and renamed over the playlist. Over 8 MB or with lines over 4 096 characters a playlist is view-only, never rewritten.
  - Entries are positions, not song ids: the same song may appear twice and Remove takes out that one entry

(Y2Player removed every copy). Each edit reads the file fresh and checks the entry is still where it was, so a change made on a computer meanwhile is never overwritten blindly (`reborn_core::playlist`).
  - Matching (`reborn_ui::playlist_index`): relative paths (what Reborn writes, portable to a computer), paths on

the player, Windows/macOS/Linux paths and file:// links from computers by their ending (most trailing folders in common; a bare ambiguous name matches nothing), case-insensitive — all in memory, no file system call per entry (Y2Player made several). 20 000 entries on a 20 000-song library: first open 19 ms on the host, a frame 0.3 µs (rows cached per change, lent out without copying).
  - Section: Home → Playlists (New Playlist, Favorites with its heart, every playlist with a 2×2 mosaic, song count,

length, SD Card / View only); a playlist's page (mosaic, Play, Shuffle, songs; missing ones dimmed "Not on the player"). Hold Select: on a playlist Play Next, Add to Queue, Rename, Duplicate, Delete (confirmed; Favorites can be neither renamed nor deleted); on a song Play Next, Add to Queue, Move (the wheel carries it, Select drops, Back cancels), Remove from Playlist, Add to Playlist…, Go to Album/Artist. Add to Playlist… on any song, an album's or artist's Play row and Now Playing (picker: New, the playlists used last first); Add/Remove from Favorites on songs and Now Playing (a heart there when it is one); Save Queue as Playlist. New playlists are named on the keyboard and saved in `Playlists/` on Internal Storage.
  - File work runs on a `playlists` thread (`app/reborn/src/playlists.rs`); playlists are read again with each

library publish (files copied over USB, the heart works from the start).

Owner: "when playing music and pausing and playing again the player will always buffer"; "scrolling right and left also gives an error". Player log (Beta 5.1, AirPods): Pause closed the PCM at once ("alsa closed" 3 ms after pause); Play reopened the file, sought and reopened `bluealsa:` (open → prepared ≈450 ms), ≈1.3–1.4 s per resume. Holding Previous/Next seeks 30 s every 90 ms; each step restarted the pipeline and the next one hit "audio reconfiguration is still pending" (ten errors in one second).
  - Pause in place (files; a station still stops, it is live): `Playback::hold` keeps decoder, file and device

open; the audio thread pauses the device (`AudioSink::pause` → `rb_sink_pause`: `snd_pcm_pause` where the device has it, BlueALSA included, else drop and prepare on resume; since 1.0.0-beta.6.1 BlueALSA drains instead, see above) and writes nothing; the decoder waits on the full queue (its heartbeat continues). Play continues at once. Wired and Bluetooth alike. The hold is given back after 3 minutes (`HOLD_LIMIT`), before sleep, and by any stop or new start; a seek while paused releases it so Play starts at the new place.
  - Collected seeking: steps only move the position (the sound holds); playback restarts once, 350 ms

(`SEEK_SETTLE`) after the last step and never during a restart in progress, so no error.
  - Test: `a_held_pause_stops_writing_and_resumes_without_reopening`.

## 1.0.0-beta.5.1 — Y2Linux 1.0 Beta 5.1 (Baseline 56), 2026-10-15: live search, a faster search index, Radio as its own section

Radio, reworked (`views_radio`, owner: "radio should feel like its own premium section", "sort everything by alphabet", "top 10 radio stations for each country on top"):
  - Home of Radio: an On Air card for the station playing (logo, ON AIR, the announced song), then Favorites,

Popular, Countries, Genres, Search and My Stations as coloured icon tiles with a line each; without Wi-Fi a Connect to Wi-Fi row on top (favorites and own lists stay usable).
  - Station logos from the directory (`favicon`): downloaded once per logo by a background thread

(`radio::fetch_logo`, ≤300 kB, PNG/JPEG/WebP, the largest PNG in an .ico; failures remembered three days), decoded whole without stretching (`rb_media_logo_file`) and laid on a tile (`art::logo_tile`: a logo's own plain background fills the tile, a picture fills it, a transparent logo sits on a light or dark tile). Without a logo, a tinted tile with the station's initials. Live check: 21 of 24 popular stations' logos.
  - Lists A to Z (stations, favorites, own lists, countries, genres); a country's, a genre's and the popular

list keep their ten most listened stations on top, ranked, the rest A to Z. Station rows: logo, name, country · genre · format, a star on favorites, LIVE on the station playing. Countries carry their code, genres are capitalised.
  - Station Info (hold Select on a station or on Now Playing): logo, country, language, format, votes,

genres, homepage; Play / Now Playing and Favorites.
  - Now Playing: the logo as the picture and colour, a LIVE badge with the station's name, the announced

song as title and artist, the station, format and country; Previous/Next switch to the neighbouring station of the list it was started from.
  - Directory details kept per station (logo, homepage, language, country code, votes, plays); favorites

saved earlier gain them when the station shows up in a list again.
  - Fixed: grouped numbers (1 000 songs and more on Home) used a thin space missing from the fonts.

Live search. The library search shows its results above a compact keyboard while you type: three rows (artists, then albums, then songs, up to 60), the count in the field, a hint while empty. Back on the top key row moves into the results, Down past the last one returns to the keys, Select opens an artist or album or plays a song (the full results page comes first, so Back returns to it); hold Select still opens all results. Password and station search keep the roomy keyboard.

Search index (`reborn_ui::search::Index`): artists, albums and songs are folded and sorted once per library (album counts precomputed); a keystroke searches only what the shorter text found, Delete reuses the earlier search (48 kept), matching allocates nothing per name. Synthetic 20 000-song library on the host (release build): per keystroke mean 6.2 ms → 0.05 ms, worst 7.5 ms → 0.42 ms; the index build (≈20 ms on the host, a few hundred ms on the player for 20 000 songs) happens when the keyboard opens. The results page no longer scans the library once per artist. Benchmark: `cargo test -p reborn-ui --release -- --ignored --nocapture speed`.

## 1.0.0-beta.5 — Y2Linux 1.0 Beta 5 (Baseline 55), 2026-10-15: keyboard and search

Full-screen keyboard (`reborn_ui::keyboard`) for the Wi-Fi password, radio station search and the new library search, replacing the one-row letter wheel. QWERTY in four rows (owner's choice), pages abc/ABC (Shift once, twice = lock), 123, #+= (all printable ASCII, so any WPA passphrase) and àé (accented letters, searches only; passwords get a show/hide key there). Buttons only (owner's choice): `ActionRouter::set_keyboard` turns Back, Play/Pause, Previous and Next into up, down, left and right on press, held Previous/Next repeat every 180 ms, holding Back cancels, the wheel does nothing; Select types, holding Select is Done. Rows wrap, so Done is one press above the letters. Playback buttons do not skip tracks while it is open; volume and Power keep their meaning; headphone buttons still control playback.

Library search (Home → Search, also in the Music menu): artists, albums and songs where every typed word begins a word of the name, folded like A to Z order (`reborn_core::sort::fold`); an album is also found by its artist, a song by title, artist or album. The keyboard shows a live count ("2 artists · 3 albums · 9 songs"); results open as a list (Edit Search, artists, albums, songs); Select on a song plays the result songs in order. Folded names are cached per library (`search::Index`).

Since 1.0.0-beta.4 (in Beta 4.1): a stopped or paused station no longer hangs playback (`Stream::drop` closes its pipe first); Radio follows the Wi-Fi view every loop pass; a late platform network record no longer shows a connected player as offline.

UI pass (all 95 preview states, Reborn's look and skins): one capitalization rule (Title Case for titles, rows, buttons and menu entries; sentence case for descriptions, hints and status values), so "Play Next", "Go to Album", "Scan for Music" (one name instead of two), "Reset Settings", "Wi-Fi Is Off" and so on; notices sit in the status bar instead of over the focused row or the cover; the turn-off hold has a nearly opaque backdrop; the password keyboard's title is "Wi-Fi Password" (the prompt names the network).

Host checks: 437 workspace tests (keyboard layout, movement, pages, limits, Done/Cancel; router keyboard mode with held buttons; search matching; the Wi-Fi, radio and library flows), fmt, strict Clippy; preview renders of the keyboard pages and search results in Reborn's look and in skins. Not yet on the device.

## 1.0.0-beta.4 — Y2Linux 1.0 Beta 4 (Baseline 53), 2026-10-15: internet radio

Internet radio. Home → Radio: Favorites (saved in `/data/reborn/state/radio.json`), Popular, Countries, Genres and Search (wheel keyboard) from radio-browser.info (mirrors found through DNS as the service asks; plays are counted with its `/json/url/` call), and My Stations from `.m3u`/`.pls` files in a `Radio` folder on Internal Storage or the SD card. Hold Select on a station, or on Now Playing, to add or remove a favorite. Now Playing shows LIVE RADIO, the station's announced song (ICY `StreamTitle`) or the connection state, listening time and LIVE instead of a countdown.

How it works: `reborn_platform::radio` runs `curl` (TLS with certificate checks, redirects, `.pls`/`.m3u` indirection, 15-s stall limit) and strips the ICY metadata blocks; the audio bytes go through a pipe to `Decoder::open_stream`, a non-seekable input of the existing FFmpeg decoder (`rbpipe:<fd>`, formats mp3, aac, ogg, flac). FFmpeg keeps `--disable-network` and its `file`-only protocol policy. A dropped connection is retried after 1, 2, 4, 8, 15 and 30 s; the decoder waits up to 45 s. A station is never pre-opened for gapless playback, never seeked, and an SD card change never pauses it. HLS/DASH-only stations are left out of the directory lists and named when a playlist leads to one.

Host checks: 426 workspace tests (radio: ICY splitting at every byte boundary, header/redirect parsing, playlists, Radio folders, directory filtering, favorites, a local Shoutcast server that drops and is reconnected, stream decoding of MP3/AAC/Ogg from a slow pipe, the Radio screens), fmt, strict Clippy. Live (ignored by default): the real directory and two real stations (France Info MP3, Europe 1 AAC) decode through the playback path. Not yet on the device.

## 1.0.0-beta.3 — Y2Linux 1.0 Beta 3 (Baseline 52), 2026-10-15

Bluetooth quality and stability. The platform now runs AAC with the FDK afterburner at the highest rate the headphones accept where a frame still fits one packet (AirPods Pro advertise 256 kbit/s VBR-capable; Beta 2 sent BlueALSA's default 220 kbit/s) and steps the rate down (256 → 192 → 160 → 128 kbit/s) while the link backs up, back up after ~10 s of an empty queue — the AAC counterpart of LDAC's adaptive rate. The service menu (System) shows AAC Quality (High / Standard) and AAC Auto Rate (On / Off) next to the LDAC rows; SBC Quality (XQ, XQ+) no longer needs the experimental switch. Defaults need no action from the owner.

## 1.0.0-beta.2 — Y2Linux 1.0 Beta 2 (Baseline 51), 2026-10-15

Automatic audio output. Bluetooth headphones win over the headphone jack: the first time a connected peer's BlueALSA playback PCM is ready, the output moves to it and playing music continues there (notice Audio switched to …). Once per connection, so choosing the jack by hand sticks until the headphones reconnect; a codec change that recreates the PCM is not a new connection; a working Bluetooth output is never displaced by a second peer. Losing the peer returns to the jack and pauses, as before. Reborn starts on the jack and lets reconnecting headphones take over (a saved Bluetooth output whose peer was absent used to leave playback with nowhere to go). There is no jack detection on this board yet, so the jack is simply the output whenever no Bluetooth headphones are connected. Wi-Fi passwords containing `\` or `"` are sent as typed (they were stored escaped and could never connect); network names go to wpa_supplicant as hex. Live on Beta 1 (2026-10-15): AirPods Pro negotiate AAC 44.1 kHz.

## 1.0.0-beta.1 — Y2Linux 1.0 Beta 1 (Baseline 50), 2026-10-16

Reborn's first public beta, built into the Y2Linux 1.0 Beta 1 images. Since Baseline 48: Wi-Fi and Bluetooth pages explain the one-time radio firmware copy (Firmware drive) and say when it is ready; a cancelled or older failed update no longer hides a newer release; versions read "1.0.0 Beta 1"; merged contributions by @samanz: covers that load reliably (#6), A to Z ignoring case, accents and a leading "The" (#7), genre titles on the album grid (#8). Public codecs SBC, AAC (fdk-aac-free) and LDAC.

## Baseline 48 — 2026-10-16

Reborn 0.3.0 `62af097` is the player in Y2Linux Baseline 48 (POWER-FINAL-48, tag `baseline-48`, the third release on the over-the-air channel). Since Baseline 34: Software Update for full-system updates over Wi-Fi (Y2Linux OTA-35 to 48): check (also once a day, with a Software update available notice), download, Restart and Install (the player restarts into its recovery image and back by itself), Restoring and named refusals (charger or half a battery, needs a computer, couldn't be verified; not enough system space names the MB and says music is not affected). The download screen (48) reads the platform's live progress file: Step 1 of 2 · Download with a percentage, a gliding bar, MB of MB, speed and time left, then Step 2 of 2 · Check; when done the page turns to Ready to Install and a notice says so wherever the owner is. Preview states `34`, `34b`, `34c`.

## Baseline 34 — 2026-10-14

Reborn 0.3.0 `5b69ef5` is the player in Y2Linux Baseline 34 (POWER-FINAL-34, tag `baseline-34`). Since Baseline 24 (`ced5199`): Cover Flow at the panel's rate (no 34-ms frame gate), sub-minute album lengths, macOS `._*` and system folders skipped (25); Bluetooth codecs seen and chosen automatically (26); folder-first artwork with more cover names, `.m4b/.oga/.aifc`, `ALBUM ARTIST` (31); the limiter only when the DSP can raise a peak (30); themes (33, 34): a skin engine (strict `skin.json`, skin atlas texture, TTF fonts, layouts per screen with Reborn's own drawing in the skin's palette as fallback), Settings → Display → Theme, `Themes` folders on Internal Storage and the SD card, `rebornctl theme`, 15 shipped skins ([skins](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fskins.md)); and the battery level for the platform's `stock_oam` source (34). Reborn's own look is unchanged without a skin (every host preview identical to `0892bf2` except the new Theme row). 398 workspace tests, fmt and strict Clippy pass. On hardware: the themes ran on 33 (owner: "it works very good"; Classic 162 ms, the other 13 shipped themes 87–119 ms to load); 34 (battery level, Zune) awaits the flash. Cover Flow frame rate after 25, AAC with AirPods, crossfade and EQ are not yet checked on the device.

## Baseline 24 — 2026-10-13

Reborn 0.3.0 `ced5199` is the player in Y2Linux Baseline 24: Cover Flow for Albums, Genres, animation frame pacing.

## Baseline 15 — 2026-10-12

Reborn 0.3.0 `f68e088` is the player in Y2Linux Baseline 15 (POWER-FINAL-15, tag `baseline-15`). The only change since 13 is the move to Rust 1.99.0 with its stricter Clippy (`as_chunks`, `try_update`, a pointer cast for the signal handler, a zipped queue counter); behaviour is unchanged. 362 workspace tests, fmt and strict Clippy pass on 1.99. On the device it runs against Mesa 26.2.4, FFmpeg 9.0.2, BlueZ 5.87 and bluez-alsa 5.0.0; the owner confirmed display, audio, Bluetooth and library after the flash.

## Baseline 13 — 2026-10-11

Reborn 0.3.0 `71ddb0d` is the player in Y2Linux Baseline 13 (POWER-FINAL-13, tag `baseline-13`). The Product UI v3 and the remaining screens (computer connection and copying, Bluetooth pairing, update download, scanning, low battery, SD removed, songs added) have run on the owner's Y2 since POWER-FINAL-10/11. Reborn was unchanged from 11 to 13; those candidates changed the platform (sleep, charging, stock power settings). Host checks at `71ddb0d`: `cargo fmt`, `cargo test --workspace --locked --offline` and strict Clippy pass. Not checked on hardware: crossfade end-of-track blend, EQ, native high-rate output, non-SBC Bluetooth codecs. Platform issues that affect the player (software-restart dark panel, USB after deep sleep) are listed in the [Y2Linux state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FCURRENT_PLATFORM_STATE.md).

## Product UI v3 — 2026-10-10

Reborn 0.3.0 redesigns the UI (see [Product UI v3](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-UI-V3.md)): Open Sans exact-size type, cover-driven accent, cover thumbnails with a disk cache, a bare volume line, option icons on Now Playing, a flatter Settings tree, hold-to-turn-off without menus, a hidden service menu and new startup/shutdown screens. Host tests, fmt and strict Clippy pass; it is not yet observed on hardware. Dated sections below describe earlier applications.

## Independent Platform 1.0 baseline — 2026-10-04

Compiled Reborn `9cd12baeeb70b204e08299bd4c91c8c35604c304` (runtime bytes unchanged from master dd73dcc) with Linux `98daf3f0220f4a1580bb4893094ee9f0e02362a5`. Fresh 324 workspace tests, fmt, strict Clippy, ARM/QEMU/installed helper/dependency validation PASS. Build `Y2LINUX-PLATFORM-V1-BASELINE-01`, root `2025.02.18-platform-v1.24`, release `1.0.0-platform-v1-baseline-candidate.1`. Final branch `codex/platform-v1-baseline-final`; canonical owner package `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-platform-v1-baseline-candidate`. SOFTWARE_VALIDATED / INTEGRATED_PHYSICAL_NOT_RUN. UART01 CPU and temporary subsystem measurements keep their historical identities; Baseline02 RTC FAIL and public firmware/codec/source/collector blockers stay open. Main unchanged. No flash, push or device qualification by the verifier. Later report-only HEAD is separate from compiled source. Earlier current/next labels are historical.

## Sealed Platform 1.0 software integration — 2026-10-04

READY_FOR_PLATFORM_V1_PHYSICAL_QUALIFICATION. Compiled Reborn `dd73dcc3243045cd33e319dda2f76918ed37ea31`/Linux `4c72466f2f27ddf9f0ca18ba8ddc4d89c52599d2`; actual package/application0.2.0.324tests/fmt/strict Clippy, fresh pinned ARM/QEMU/software/package gates PASS. One candidate `/home/luca/Dokumente/Code/worktrees/platform-v1-integration/Y2Linux/out/y2linux-platform-v1-integration-candidate`. Integrated physical/endurance NOT_RUN and public distribution blocked; current installed stock remains Baseline02/b71 after temporary source-bound benchmarks. See [master](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Frelease%2FY2-PLATFORM-V1-MASTER.md) and [software receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-INTEGRATION.md). Dated progress/physical sections below remain history.

## Platform 1.0 integration — 2026-10-04

Selected source from all eleven finished handoffs is composed on `codex/platform-v1-integration`. All 324 workspace tests, formatting and strict Clippy pass. Fresh production ARM and one integrated physical campaign remain pending. Canonical source/card claims, bounded TEMP scanner, source-aware zero-FD cover cache, one observation worker, sleep quiescence and durable USB refresh share one runtime. Native wired hardware remains S16/44.1/48; wider AFE admission and Bluetooth peer/codecs require evidence.

Installed owner receipts identify Baseline02 Linux `8584ccd8` / Reborn `b71b4688`, boot `88b85fa3` after the failed RTC wake; temporary optimized binary tests are separate from installed stock and the new integrated image. The [master](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Frelease%2FY2-PLATFORM-V1-MASTER.md), [source ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FREBORN-PLATFORM-V1-INTEGRATION.md) and [physical plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Frelease%2FY2-PLATFORM-V1-PHYSICAL-QUALIFICATION.md) are current; the dated observations below retain their original scope.

Updated 2026-10-01. **Software candidate (not flashed, not physically qualified): Reborn Product UI v2** (0.2.0) on the CPU Final Fix03 platform. Smaller product surface, typed platform boundary, one-detent wheel, Reborn boot mark and dark shutdown. See [Product UI v2](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-UI-V2.md), the [pass record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Freview%2FREBORN-PRODUCT-PASS-V2.md) and the [Y2Linux receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-REBORN-PRODUCT-UI-V2.md). Everything below describes the last physically observed application. Updated 2026-10-04. The observed installed application is Product UI v2 (0.2.0), Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, on Y2LINUX-BASELINE-02: Linux `8584ccd85f052f351fe51650b2348c83ca894ed4`, kernel `6.18.0-y2linux-baseline-02`, root `2025.02.18-platform-v1.21`. Final matched tests/restoration observe boot `88b85fa3-2282-4d93-b0b8-818a105ddd0a` with taint 0 and automatic qualified CPU0 C3 policy Enabled, budget -1, disable 0.

The [performance pass](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FREBORN-PLATFORM-V1-PERFORMANCE.md) records reversible temporary ARM executable tests, product benchmarks and their limits. Its source candidate is isolated on `codex/platform-v1-reborn-performance`; the installed executable and original application data are restored after tests. Product v2 design and state ownership remain the contract. This pass does not promote full suspend, electrical battery life or public release qualification. The final tested temporary source is `069415a`; installed Reborn remains `b71b4688`. Playing CPU falls from 87.95% to 11.21% of one core, while all 1,000 wheel steps match and sampled static screens produce zero idle redraws. See [Product UI v2](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-UI-V2.md), the [product pass](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Freview%2FREBORN-PRODUCT-PASS-V2.md), and the paired [current platform state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FCURRENT_PLATFORM_STATE.md).

The dated Fix01 observations below are retained as historical evidence. They describe that image, rather than the installed Baseline02 or performance candidate.

Physical observation from the 2026-09-27 CPU Final Fix01 run. This page describes the exact already-flashed application, not a new image or software build. The [paired Linux state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2FCURRENT_PLATFORM_STATE.md) and [physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md) are the authority for hardware/platform results.````````````

| Identity | Historical Fix01 physical observation |
| --- | --- |
| Reborn compiled source | 36db1869c6bab1ad2d00b7d8e7807ea6ef5b3803 |
| Linux compiled source | 0de6e951b438bf0f2d701e23e476d2b2405ba3c6 |
| Kernel/root | 6.18.0-y2linux-cpu-final-fix01 / 2025.02.18-platform-v1.7 |
| Release | 1.0.0-cpu-final-fix01-candidate.1 |
| Latest observed boot | 81e422f3-43cd-4ad6-877f-692eb1191b36 |

The user interface, controls, artwork, scanner and platform workers generated accepted real workload leases for Idle, PlaybackNormal, PlaybackHeavy, Interactive, ArtworkDecode, LibraryScan, NetworkTransfer and Maintenance. Interaction lasted roughly 250 ms, coalesced and expired; screen-off released it immediately while playback's lease remained. The kernel governor selects MHz. Isolated client tests also covered renew/expiry/close/overlap/killed-process cleanup; actual Reborn process-death restart was not physically tested.

Bounded native 44.1-kHz and 24/96 -> 48-kHz silent fixtures played with no ALSA XRUN, FFmpeg decode/filter errors or corrupt packets. Silent fixtures establish software operation, not listening quality. Crossfade was enabled through the real UI to produce PlaybackHeavy, then restored to zero; an actual track-transition blend and independent EQ path remain untested. The 200-file scan was a small fixture run, not a 20k-track endurance result. The measured `decoder_stalls` counter represents a full producer queue in current source, not corruption or an ALSA underrun. Source output precision and native high-rate hardware are separate from decoding and conversion.

The Fix01 platform qualification FAILS overall: SLIDLE never entered; 1196/1300 MHz stayed safely gated; no same-boot full suspend restore was demonstrated; a loaded USB transfer lost connectivity while the UI stayed usable. Four independent small Wi-Fi roundtrips and the one-retry radio restore passed. No claim about actual Bluetooth peer playback, visual legibility, analog fidelity, battery life, full wake or public release is made here.

Current software ownership remains [media](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Farchitecture%2Freborn-audio-stack-ffmpeg9.md), [live volume](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Farchitecture%2Flive-volume.md), [platform API](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Farchitecture%2Fplatform-api-v1.md), and [UI v1](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-UI-V1.md). The [Luna correctness closure](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FLUNA-CORRECTNESS-CLOSURE-01.md), [UI candidate report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-UI-V1-REPORT.md) and [older system audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F00_SCOPE_AND_EVIDENCE.md) are dated software/review records. Refer to the [document catalog](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2FDOCUMENTATION_CATALOG.md) before treating their older "current" or "next" text as today's policy.

At the Fix01 boundary, next CPU platform work was one coherent Fix02 plan: PM diagnostic safety, PWRAP readiness, MMC runtime clocks/coordinator reachability and loaded USB recovery. This page does not authorize those code changes, flashing or a new application release. It preserves source, candidate and physical evidence tiers.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
