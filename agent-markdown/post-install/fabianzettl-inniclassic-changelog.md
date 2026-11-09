---
title: "Changelog - Innioasis Updater"
description: "Changelog All notable changes to InniClassic formerly"
language: "en"
source: "https://innioasis.app/post-install/fabianzettl-inniclassic-changelog.html"
---

# Changelog - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y1&software=inniclassic-y1)

Post-install setup · Inniclassic · Y1

# Changelog

A classic-style Y1 Software.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y1&software=inniclassic-y1)[Install guide](../guide.html?model=Y1&software=inniclassic-y1)

# Changelog

All notable changes to InniClassic (formerly "JJ Launcher Classic Version") are documented here. This project is based on JJ Launcher `0.11`; this changelog covers only what changed on top of that base.

## [1.4.5] - 2026-09-30

### Fixed
  - Theme could silently revert to the default after connecting the device as USB Mass Storage — the selected theme was persisted only as a numeric index into the SD card's theme folder listing, and that listing's order isn't guaranteed stable across a mount/unmount cycle (common FAT32 behavior). The saved index could end up pointing at a completely different theme once the card was reconnected. The theme's name is now saved alongside the index and resolved by name on startup — independent of scan order — with the old index kept only as a fallback for upgrades.
  - `.scrobbler.log` declared its timestamps as `#TZ/UNKNOWN` even though they're genuinely UTC (`System.currentTimeMillis()` is always UTC epoch time, regardless of the device's local timezone setting). Now correctly declared as `#TZ/UTC`, so any tool that imports the log trusts the timestamps instead of asking or guessing. Only affects newly created log files — an existing `.scrobbler.log`'s header isn't rewritten.
  - On-screen keyboard was missing common punctuation, making some Wi-Fi passwords (and anything else typed through it — podcast search, Last.fm login, etc.) impossible to enter. Added `; : , / \ ( ) [ ] { } < > ' ~ \``and`|`.

## [1.4.4] - 2026-09-29

A hardware-input overhaul: a real Hold/lock switch, a proper video/music handoff, and a round of Now Playing and Videos polish.

### Added
  - Hold (key lock) — hold Center for 0.8s to lock the wheel/buttons (and physically turn the display off); hold Center again to unlock. This is the real fix for "screen wakes up randomly in my pocket": instead of trying to guess which button presses are accidental, you can now lock input entirely, matching the real iPod Classic's Hold switch.
  - Toggle Favorite is back in the Now Playing hold-menu (long-press Play/Pause) — the redesigned Center gesture handling below removed the old "double-click Center" favorite shortcut without anywhere else to reach it, so this restores it in a sensible new spot before release.

### Fixed
  - Video Play/Pause was starting music instead of pausing the video. Two compounding bugs: (1) the physical Play/Pause button is delivered both through the app's normal input path and independently through a registered hardware media-button receiver, and only the first one knew about video — with "Screen Off Control" enabled in Settings, the receiver would call the music player regardless of what was on screen; (2) opening a video didn't stop any music that was already playing. Both are fixed: the media-button receiver now ignores playback keys entirely while a video is open, and opening a video now pauses active music first.
  - Videos list ignored the wheel/Center in some cases — the screen was unconditionally swallowing every key before the shared list-navigation code could see it.
  - Now Playing wheel seeking now behaves as a real preview-then-confirm: turning the wheel in Seek mode moves a pending position in 5-second steps without touching actual playback, and only applies it once you press Center again (otherwise Center just continues cycling Progress → Seek → Shuffle & Repeat → Rating). The preview no longer gets silently overwritten by the normal progress-bar update ticking in the background.
  - Center-button handling is now centralized in one place instead of being spread across multiple key handlers — fixes a hold sometimes also registering as a select, and holding Center no longer incorrectly opens the song menu or toggles video seek mode (that's long Play/Pause and short Center respectively now).
  - Pausing on the Classic theme no longer dims the album artwork or leaves a leftover audio-format overlay on screen; whichever Now Playing bottom-bar mode you were in survives a pause/resume instead of resetting.
  - Removed a duplicate progress-callback registration that caused Now Playing's timers to accumulate extra callbacks the longer a session ran.

### Changed
  - More compact Now Playing progress/volume bars, fixed-width time labels, and evenly spaced rating marks.
  - Video playback now seeks via the Previous/Next buttons (±10s); the wheel is volume-only during video (its old long-press-to-toggle-seek-mode gesture no longer has a way to trigger it now that long-press Center is reserved for Hold, so this is the new way to seek).
  - Classic Videos list now shares the same background/row styling as every other list instead of its own slightly different look.

Full engineering write-up: [`docs/release-review-1.4.4.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FFabianZettl%2Finniclassic%2Fblob%2FHEAD%2Fdocs%2Frelease-review-1.4.4.md).

## [1.4.3] - 2026-09-22

A theme-consistency pass plus a round of real correctness/security fixes underneath, including a Last.fm crash and a Wireless PC Upload path-traversal issue.

### Changed
  - Classic themes tightened up: edge-to-edge, tighter main-menu rows; consistent 21dp bold list type; saturated blue selection gradient shared by both the dynamic menus and library lists; silver status-bar gradient, darker secondary text, and more compact chevrons. Existing Nimbus Sans regular/bold font files are unchanged.
  - Battery silhouette is more rectangular, and battery percentage is now clamped to 0–100 (guards against a reading briefly overshooting during charge-state transitions).
  - Main Menu, Cover Flow, Wi-Fi and equalizer views now use generated Android view IDs with a stable logical-key mapping, instead of ad hoc constants — reduces the risk of ID collisions as the UI grows.

### Fixed
  - Last.fm scrobbling could crash its background worker outright — the pending-scrobble queue called `JSONArray.remove(int)`, which doesn't exist on the Y1's Android API 17 (added in API 19). Replaced with a manual queue-trim helper. Also: Last.fm can return HTTP 200 with an API-level error payload, which was previously treated as a successful scrobble and silently dropped from the retry queue — now correctly kept queued for retry.
  - Wireless PC Upload (the web server) had a path-traversal weakness — uploaded/renamed file paths weren't confined to the shared folder. All file operations now resolve and canonicalize against the shared root and reject anything that escapes it, reject cross-origin writes, and render filenames as plain text (not raw HTML) in the browser UI. Interrupted uploads now write to a temp file and atomically replace the target only once complete, so a dropped connection can no longer corrupt or truncate an existing file.
  - Server connections now have timeouts and a bounded worker pool instead of growing unbounded; shutdown properly closes active sockets; large directory listings are read in batches instead of all at once.
  - Recycled album rows in the library list could show a stale cover art thumbnail if a newer request for that row was still in flight when it got recycled for a different album; also fixes focus/marquee highlighting not always restoring correctly on a recycled row.
  - Removed a duplicate broadcast-receiver registration and duplicate manifest permission entries; added the newer Android receiver-flags overload (with a documented fallback for API 17, which predates it) and additional Bluetooth/location permission checks before use.
  - Sound Check no longer calls an API-19-only method unguarded on this API-17 device.
  - Launcher icons switched from WebP to PNG for reliable API 17 rendering; fixed a malformed vector icon path.
  - Audiobook bookmark saving now checks that the playlist index is still valid before writing, guarding against a save racing the Activity being destroyed.

Full engineering write-up, including what was and wasn't independently verifiable before hardware testing: [`docs/release-review-1.4.3.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FFabianZettl%2Finniclassic%2Fblob%2FHEAD%2Fdocs%2Frelease-review-1.4.3.md).

## [1.4.2] - 2026-09-02

Theme-consistency and Podcasts fixes from user feedback.

### Fixed
  - Status bar headphone/Bluetooth icons were hardcoded white, making them nearly invisible on the light iPod Classic theme's light gray status bar. Now use the theme's own text color like the rest of the status bar.
  - On-screen keyboard's selected character was unreadable on the light theme — pure white text on a barely-tinted overlay meant it could blend into a light background almost completely. The keyboard panel's backdrop is now solidly dark so the white text always has real contrast, regardless of theme.
  - Podcast episode loading always said "No internet connection" even when the real problem was something else entirely (a bad feed URL, a server error, an expired certificate, malformed XML, etc.) — the actual error was being silently discarded. The toast now shows the real failure reason so it's actually possible to diagnose.

### Added
  - `tools/airpods_fix/` — an experimental, opt-in fix for AirPods Pro 2 connecting over Bluetooth but staying silent, ported from [Semy0nBu/y1-airpods-rtpfix](https://github.com/Semy0nBu/y1-airpods-rtpfix) (all credit for the original fix goes there). Not bundled into the ROM or APK — it replaces a system-level Bluetooth driver, which is riskier and affects all Bluetooth devices, not just AirPods, so it ships as a separate, clearly-documented install/uninstall script pair instead of being forced on everyone. See its README for details and the exact risk tradeoffs before using it.

## [1.4.1] - 2026-08-28

Another round of Reddit-reported feedback.

### Changed
  - Larger list/settings text — Songs/Albums/Artists/Genres/Composers rows, folder browsing, and every Settings row are a bit bigger (title 21→23px, settings rows 18→20px, album subtitle 14→15px).
  - Cover Flow now groups by artist — previously sorted purely alphabetically by album title, scattering an artist's albums throughout the list; now sorted by artist first, album second, matching the real iPod Classic.

### Fixed
  - Folders with many files lagged noticeably when opened — every row was built synchronously in one go; now built in chunks of 25 with a frame yielded in between, so the screen stays responsive while filling in instead of freezing.
  - Screen could randomly wake up in a pocket while listening to music — a side effect of the 1.3.0 fix that made the real screen-off state wake back up on any key press; pocket pressure on the click wheel could trigger it unintentionally. Only the Center button now wakes the real display back up.

## [1.4.0] - 2026-08-28

Video feature catch-up, plus a new boot logo.

### Added
  - Video thumbnails — the Videos list now shows a real frame from each file (grabbed ~1s in) instead of a generic icon, loaded in the background so opening the list stays instant even with many videos.
  - Video resume-position — playback remembers where you left off (past the first few seconds, short of the last few) and jumps back there next time you open that file; videos watched to the end start over from the beginning like normal.
  - Fill Video Screen setting — Settings → Fill Video Screen lets you choose between the original aspect ratio (letterboxed) or stretching to fill the whole screen with no black bars. Direct response to a GitHub issue request.
  - New boot logo — replaces the Rockbox-branded splash the ROM's `LOGO` partition had been carrying over since this project's very first release (an artifact of the source device's stock → Rockbox → InniClassic history) with a plain black screen showing "InniClassic".

## [1.3.2] - 2026-08-03

Small follow-up polish release.

### Fixed
  - Videos screen looked out of place compared to every other menu (Settings, Bluetooth, Wi-Fi) — it was missing the uppercase title header those screens have. Added, matching the existing look exactly.

## [1.3.1] - 2026-07-29

Another round of Reddit-reported bugs, mostly around the Music library screens.

### Fixed
  - "Albums" was completely broken — tapping into it either showed a black screen, froze, or silently bounced back to the Music menu. `getAlbumRowView()` was doing a full library scan plus a synchronous `MediaMetadataRetriever` lookup on the UI thread for every row, every time it scrolled into view - fine for a handful of albums, but an ANR/freeze risk for a real-sized library. Cover art lookup now runs on a background thread (placeholder shown immediately, real art swapped in once ready), and the per-album file lookup is precomputed once instead of rescanning the whole library per row.
  - Videos screen: nothing could be selected or played — rows were added to the list but never given initial focus, so spinning the wheel had no "current" row to move from (you'd hear the click sound but nothing would highlight or respond). Now the first row gets focus like every other list in the app.
  - Some FLAC albums showed no cover art in "Albums" (but did show it correctly on Now Playing/Cover Flow) — the Albums screen's cover lookup skipped embedded art entirely for FLAC files with no fallback, so only albums with a folder `cover.jpg`/`folder.jpg` showed anything. It now uses the same dedicated FLAC metadata parser Now Playing already relies on.
  - Confusion around Last.fm scrobbling / "where's my .scrobbler.log?" — the local scrobble log was silently gated behind the "Scrobble to Last.fm" toggle (off by default) even though it's just a private text file that needs no account. It's now written automatically for every played track, no setup required; the Settings toggle (renamed Sync Scrobbles to Last.fm) now only controls whether scrobbles are also sent to a real Last.fm account. Also documented in the README that `.scrobbler.log` is a dotfile and hidden by default in most file managers.
  - Cover art looking noticeably blurry/soft while panning on the Main Menu and Music menu — cover art was always decoded at half resolution (`inSampleSize=2`) regardless of its actual size, which compounded badly for anyone using smaller (e.g. 300×300) cover images against a pan panel rendered near full screen height. Downsampling now only kicks in for genuinely large source images; small covers are decoded at full resolution. README now recommends 600×600 minimum, 1000×1000+ ideally.

## [1.3.0] - 2026-07-29

A Music Quiz overhaul, a Now Playing polish pass, and another batch of Reddit-reported bugs — mostly sleep/wake and audio.

### Added
  - Music Quiz: five new question types — alongside "What song is playing?", it can now ask which artist released a track, which album it's from, what year it came out, and what genre it is (each only offered when your library actually has enough distinct values to make a fair question). Also new: a visual question type showing 3 album covers side by side to pick from instead of text answers.
  - Music Quiz: all 4 answers now fit on screen at once, no more scrolling to see the other options — the album cover was removed from the question card and chrome (badges, progress bar, score row) was shrunk to make room.

### Changed
  - Now Playing: the album cover sits slightly lower, spacing between Title/Artist/Album is now perfectly consistent, the star rating moved between Album and the track counter, and the "X of Y" track counter is now bold at the same size as the rest of the info block.
  - Documented the existing (but easy-to-miss) synced lyrics support in the README: drop a `.lrc` file next to a song (same filename) or embed lyrics in ID3/FLAC/ALAC tags, then long-press Center on Now Playing → Toggle Visualizer to see them scroll in sync with playback.

### Fixed
  - Screen never came back on after the backlight timer put it to sleep — two separate bugs, both now fixed:
    - The "virtual" sleep used while FM Radio or the web server is running (so the CPU stays alive) set a flag to fake the screen off but never had any code path that turned it back off. Once it triggered, the screen stayed black forever (vibration/click feedback still worked, since the app itself never stopped running) until a full reboot.
    - The "real" sleep used during ordinary music playback simulates a power-button press to turn the display off, but nothing ever simulated a second press to turn it back on. The wheel/buttons aren't registered as Android "wake keys" on this hardware, so nothing brought the display back short of the actual hardware power button.

  - Full device lockup (required a paperclip reset) when playing FM Radio through wired headphones for a few minutes — the backlight timer's "virtual sleep" path was also toggling Wi-Fi off, even while the FM tuner was actively running. On this chipset, FM/Wi-Fi/Bluetooth share the same combo radio hardware; killing Wi-Fi out from under a live FM session could wedge the shared chip badly enough to need a hard reset. Wi-Fi is now left alone whenever the radio is on, the same way it was already left alone whenever the web server is running.
  - Screen dimming during active use — the out-of-the-box Backlight Timer default was 10 seconds, which is aggressive enough to feel like the screen "won't stay on" during normal browsing/listening. Default is now 1 minute (still adjustable down to 10 seconds in Settings if you want it).
  - Bluetooth headphones (reported with AirPods) noticeably quiet — a known AVRCP "absolute volume" quirk where the phone-side volume slider becomes the headset's actual volume, and the negotiated level can end up low. Absolute volume is now disabled on connect, so headphones fall back to using their own physical volume control.
  - Some FLAC files failed to play with "Legacy Player Error: 262" — the native decoder used for FLAC (to avoid a separate ExoPlayer FLAC hang bug) rejects a handful of files that ExoPlayer's own FLAC extension can actually decode. Failing files now automatically retry once through ExoPlayer's FLAC extension instead of just giving up; the error message also now includes the decoder's `extra` code for easier triage if a file still fails both engines.

## [1.2.0] - 2026-07-27

A big visual consistency pass across every screen, plus two new features and a round of performance/battery work.

### Added
  - Video playback — a new "Videos" entry in the Main Menu, its own folder on the SD card (`/storage/sdcard0/Videos`), and a full-screen player with wheel-driven volume/seek (long-press Center to switch between the two, short-press to play/pause). Now powered by libVLC instead of ExoPlayer: ExoPlayer's precise frame-timing API only exists from Android API 21 onward, and its fallback for older devices turned out to be broken on the Y1's API 17 — audio and the position clock stayed correct, but picture played back many times faster than real time, decoupled from the audio entirely. libVLC brings its own native, battle-tested AV-sync engine that isn't tied to that Android API, giving stable, correctly-synced playback. Audio-only playback is untouched and still runs on ExoPlayer. Thumbnails in the video list and resume-position are still unaddressed for now.
  - Gapless playback — automatically kicks in for albums and playlists of 15 tracks or fewer, as long as shuffle is off and no FLAC files are in the queue (FLAC uses a separate playback engine that can't join ExoPlayer's native queue, and large/shuffled queues intentionally keep the older, proven per-track loading path). Track transitions inside a gapless queue no longer stop and reload — ExoPlayer switches internally with no gap.
  - Favorites are now visible at a glance — Now Playing shows a hollow heart normally and a filled red heart when the current track is favorited, instead of showing nothing at all unless it happened to already be a favorite.

### Changed
  - Consistent look across every menu — Main Menu, Music menu, Artists, Albums, Songs, and Settings/Bluetooth/Wi-Fi lists were all using slightly different font sizes, left margins, and row padding. Everything now shares the same left alignment (flush with the status bar title), the same row spacing, and one font-size scale.
  - Right-arrow indicator now only shows on the focused (blue) row everywhere, instead of being visible (just dimmer) on every row all the time.
  - Album rows got a larger cover thumbnail and slightly taller rows for better legibility, at the cost of one or two fewer rows fitting on screen.
  - Status bar redesigned to match the real iPod's proportions (thinner, smaller icons) and now consistently narrows to the left column on both the Main Menu and Music menu, letting the album cover on the right bleed all the way to the top behind it.
  - Main Menu and Music menu covers are now visually identical, including the slow panning ("Ken Burns") animation — previously only the Main Menu had it, the Music menu's cover was a static crop.
  - Now Playing: bigger album cover, "X of X" track counter in bold, more breathing room between the album name and track counter, and titles too long to fit now scroll (marquee) instead of just being cut off.
  - Progress/volume bar now has a subtle glass-like highlight through the middle instead of a flat fill.

### Fixed
  - Two real bugs found while reworking the Artist/Album row styling: the focus arrow's color was tied to the theme instead of being fixed white like the rest of the app, and — more importantly — a recycled (scrolled-past-and-back) row could have its blue focused background incorrectly reset to the normal background on every re-render regardless of whether it was actually focused.
  - Now Playing's progress ticker kept doing full work every 0.5 seconds even when Now Playing wasn't the visible screen (e.g. browsing the library while music played in the background) — updating position, remaining time, and lyric auto-scroll on views nobody could see. Now skipped entirely unless Now Playing is actually on screen.
  - The clock/widget refresh loop ran every second forever, including during "screen off" playback (the screen-off state is a virtual black overlay, not a real display power-off, so the app keeps running underneath) — rebuilding a date formatter and refreshing Main Menu widgets every second regardless. Now drops to one no-op tick every 15 seconds while the screen is virtually off, and skips widget work entirely outside the Main Menu.

### Optional: reduce background bloat

A number of stock Android/MediaTek system apps that a dedicated music player never uses (Exchange mail sync, the phone/telephony stack, SIM toolkit, text-to-speech, live-wallpaper demos, calendar, an OEM RAM-cleaner utility, and others) can be safely disabled to free up RAM and stop unnecessary background activity. Two of them — the stock FM Radio app and the Download Manager provider — are not safe to remove, since InniClassic's own Radio and PC Upload features depend on them under the hood. This isn't baked into the ROM yet; ask if you want the exact list of packages.

## [1.1.2] - 2026-07-27

Another batch of Reddit-reported bugs, this time from multiple users.

### Added
  - Shuffle: a "Shuffle" row now appears at the top of All Songs, matching the stock Y1 firmware — picks a random play order and starts playback immediately.
  - FM Radio is back in the Main Menu (both the light and dark iPod Classic theme) — it had quietly gone missing from the theme config.

### Fixed
  - Crash when browsing Artists, Album Artists, Albums, Songs, or Genres — for some libraries, a song with a missing artist or album tag could be stored with a `null` value; anything that later compared against it (e.g. building the Albums list, matching songs to an artist) threw a crash instead of just treating it as "Unknown". Every song now always gets a safe "Unknown Artist"/"Unknown Album" fallback, closing this off for good.
  - FLAC files stuck at 0:00 — FLAC playback was supposed to fall back to a dedicated engine on devices where ExoPlayer's FLAC support hangs, but the switch that was supposed to enable it was never actually turned on. It's wired up correctly now.
  - Screen turning off during active use — spinning the wheel didn't reset the auto-lock timer (the code that did lived in a method that never actually runs for wheel input), so the screen could sleep mid-session unless you pressed the center button. Any input now resets the timer correctly.
  - Charging indicator — the battery icon was supposed to show a small lightning bolt while charging, but the drawing code for it had been left disabled, so charging only caused a faint color shift. It now draws a proper bolt icon.
  - Long album/track names could visually run into the battery/Bluetooth icons in the status bar. Long titles are now truncated with an ellipsis instead of overlapping.

## [1.1.1] - 2026-07-23

Two bug fixes reported by u/withclay on Reddit. Also: the project is now named InniClassic, and installable as a full ROM.

### Added
  - Flashable ROM: `rom.zip`, installable directly via the [Innioasis Updater](https://innioasis.app/guide.html) — no ADB required (the Updater expects this exact filename). Ships the latest Y1 Firmware 3.1.2 with InniClassic pre-installed as the system launcher.

### Changed
  - Project renamed to InniClassic (still based on and credited to JJ Launcher — see README). No functional/version change, same 1.1.1 build.

### Fixed
  - Wireless PC Upload (web server) status text was hardcoded white, making it invisible against the iPod Classic theme's white background once the server was started. Also fixed the same hardcoded-near-white issue on the Bluetooth/Wi-Fi/Brightness/Storage/Settings screen titles, which had the identical problem.
  - The wheel stayed active while the device was locked (screen off) — turning it could still change the volume. The guard against this already existed in code, but it lived in a method that never actually runs on this device (`dispatchKeyEvent` intercepts and consumes these keys before it would ever be reached); moved the guard to where it's actually effective.

## [1.1.0] - 2026-07-23

Focused on getting closer to the real iPod Classic experience — especially a proper depth to the Now Playing screen, plus a cleanup pass on the Main Menu and some visual consistency fixes.

### Added
  - Now Playing sub-menus: a center-click on the Now Playing screen now cycles through four states, exactly like a real iPod Classic — Progress bar → Seek (scrub bar with a diamond thumb, wheel jumps the track ±5s) → Shuffle & Repeat (quick toggle, wheel cycles each) → Rating (wheel sets 1-5 stars) → back to Progress. The wheel reverts to volume control outside of these states, same as on a real device.
  - Star ratings: rate any track 1-5 stars from the Now Playing Rating state above; shown as ★★★☆☆ under the track counter.
  - On-The-Go playlist: the classic always-available instant playlist. Reachable as a one-tap "Add to On-The-Go" action from the Now Playing hold-menu, or as a pinned entry in the full Add to Playlist dialog.
  - Now Playing hold-menu: long-press Center on Now Playing for Add to On-The-Go, Browse Album, Browse Artist, and Cancel — matching the real iPod's menu, plus a Toggle Visualizer entry for this fork's bonus spectrum/lyrics view.
  - Composers grouping in the Music menu, alongside the existing Artists/Albums/Genres/Years grouping.
  - Fast-scroll letter jump: spin the wheel quickly through an alphabetized list (Artists/Albums/Songs/Genres/Composers/Search) to jump straight to the next first-letter group, with an on-screen letter overlay while jumping — tuned so it triggers reliably without being overly twitchy on a quick spin.
  - Status bar now shows the current screen's name (Music/Now Playing/Settings/etc.) instead of a clock, matching the real iPod's title bar.

### Changed
  - Main Menu cleanup: Cover Flow, Audiobooks, Folders, Years, Recently Added, and My Favorites have moved out of the Main Menu and into the Music menu where they belong on a real iPod. Main Menu is back down to Now Playing, Music, Music Quiz, Podcasts, Bluetooth, Wi-Fi, Settings, and Web Server.
  - The Main Menu's split-view album cover now genuinely fills the entire remaining screen edge-to-edge (computed from the real screen size) instead of a fixed-size box, so it bleeds above the status bar the same way the Music menu's cover panel already did.

### Fixed
  - Menu text size was inconsistent between screens: Music-menu-style rows (Artists/Albums/Composers/Songs/Settings) were sized in `sp` while the Main Menu's buttons were sized in raw pixels — same nominal number, different unit, so they never quite matched. Everything now renders at the exact same size.

## [1.0.0] - 2026-07-21

First public release.

### Added
  - Bundled "iPod Classic" theme:
    - Two-pane Main Menu with a slowly panning, full-bleed album cover on the right that extends up behind the status bar
    - Two-pane Music menu (Cover Flow, Playlists, Artists, Albums, Songs, Genres, Search) with the same cover panel
    - Redesigned Now Playing screen: angled cover with reflection, centered track info, thick square progress bar
    - Redesigned Artists/Albums lists: icon-free artist rows, large-cover two-line album rows (bold name + song count), "All Songs" shortcut per artist
    - New text search screen (title/artist/album)
    - System-wide bold Nimbus Sans typography, tightened list indents, consistent status bar color, gradient battery icon

  - Last.fm scrobbling:
    - Local Rockbox-style `.scrobbler.log` (Audioscrobbler 1.1 format)
    - Live scrobbling via the Last.fm API with browser-based login (no on-device typing required)

  - Music Quiz: a first version of the classic iPod Music Quiz mini-game built from your own library (10s clips, 5-answer rounds, lives, score), styled after the original's 2000s "Fruitiger Aero" look
  - OGG Vorbis playback and library scanning, with automatic detection of Opus-encoded files mislabeled with an `.ogg` extension
  - Main Menu shortcuts for Music Quiz, Podcasts, Audiobooks, Folders, Years, Recently Added, and My Favorites

### Fixed
  - Duplicate songs appearing in album track lists after interrupted library scans
  - Missing album art in Artist → Albums lists (now falls back to folder `cover.jpg`/`folder.jpg`)
  - OGG files not appearing in the library at all
  - Out-of-memory crash loop while scanning very large libraries on-device
  - Album art forced to a true 1:1 crop regardless of source image aspect ratio

### Changed
  - Last.fm API credentials are no longer hardcoded; they're read from a local, gitignored `local.properties` file (see README)

These are Inniclassic's own instructions, shown here word for word.

Published by the [FabianZettl/inniclassic](https://innioasis.app/firmware.html?model=Y1&software=inniclassic-y1) project [[1]](https://innioasis.app/firmware_info.html?repo=FabianZettl%2Finniclassic&software=inniclassic-y1)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3AFabianZettl)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
