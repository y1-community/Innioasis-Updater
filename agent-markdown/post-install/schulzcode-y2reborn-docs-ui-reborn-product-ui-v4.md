---
title: "Reborn Product UI v4 — one strict system - Innioasis Updater"
description: "Reborn Product UI v4 — one strict system Plan and design contract, 2026-10-16. Phases 0–3 released in Y2Linux 1.0 Beta 7 baseline-61 , refined through Beta 7.6 baseline-6"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-ui-reborn-product-ui-v4.html"
---

# Reborn Product UI v4 — one strict system - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn Product UI v4 — one strict system

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn Product UI v4 — one strict system

Plan and design contract, 2026-10-16. **Phases 0–3 released in Y2Linux 1.0 Beta 7 (`baseline-61`), refined through Beta 7.6 (`baseline-67`, sections at the end); phase 4 (device qualification) open.** Successor to [Product UI v3](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-UI-V3.md); applies to Reborn's own look. Skins keep drawing their own layouts (see Skins).

## Why

Owner, after Beta 6.3: since playlists, search and radio were added "the UI looks kind of full"; the default look is liked but "still a little rough"; it should be "tailored to actual users, not a developer", "consistent everywhere and follow a strict design choice"; removing things users would not need is welcome.

Review basis: a device capture of Beta 6.3 (Settings; matches the host render) and all 92 interactive states of `reborn-preview` (boot and shutdown frames excluded). The roughness is mostly inconsistency: the same idea is drawn three or four ways depending on when its screen was written.

## Findings (Beta 6.3)
  - Focus and colour. Library lists focus with a cover-tinted, outlined row

(`components::accent_row`); Settings with neutral glass (`glass_row`) and a fixed blue for checks, sliders and progress; action sheets with a white filled row and dark text; Folders with glass inside a content list. Toggles are iOS green. The playing song in Songs is accent text in the same colour as the focus, so "playing" and "selected" look alike. The accent changes with every cover, so the same list is orange, teal or blue from one song to the next.
  - Four button styles: accent pill (Artist Play All), glass pills (Album and

Playlist Play/Shuffle), outlined pill (empty library Scan for Music), white and dark pills (dialogs, Station Info).
  - Permanent hint lines: keyboard ("Buttons move · Select types · Hold Select:

done · Hold Back: cancel", although Cancel and Join/Create/Search are keys), Bluetooth ("Select to connect · Hold to forget"), Up Next ("Hold Select to remove"), Radio Favorites ("Hold Select on a station to add it"), playlist move ("turn the wheel, Select to drop"), theme picker ("Add skins by copying…").
  - Information users do not need: "NOW PLAYING" over Now Playing; the gapless

icon (on by default, so always shown); radio `MP3 · 128 KBPS` and country-code tags; "ON AIR", "LIVE" and "ON AIR" for one fact; Popular rank badges plus "Top 2" plus codec/bitrate in one subtitle; Home counts; Wi-Fi "Good signal" beside the bars; Bluetooth codec in the device list; "by Reborn" on every theme; free space in Folders; "Songs in Library" and "From a Computer: Ready" in Storage.
  - Layout rules differ: Settings groups rows in cards, but the Bluetooth and

Wi-Fi device lists sit loose under a carded switch; Radio and Playlists use coloured icon tiles with outlined focus, the library round art with filled focus; empty and info states are drawn four ways (Wi-Fi off centred with icon, firmware left-aligned text, Playlists one plain line, scanning a ring); Display → Album View has no chevron beside rows that have one; spelling mixes "Normalise" and "Favorites".
  - Home has ten items (Now Playing, Artists, Albums, Genres, Songs, Folders,

Playlists, Search, Radio, Settings) with counts and fills the screen.

Also: preview fixtures `70-search-keyboard`, `70b`, `70c` are titled "New Playlist" (fixture labelling, not product); fix before the before/after comparison.

## Owner decisions (2026-10-16)

| Question | Decision |
| --- | --- |
| Cover colour | Now Playing only: its background glow and the Home cover card. Everything else uses one fixed accent. |
| Home | Music submenu + pinning: Now Playing, Music, Playlists, Radio, Search, Settings; Music holds Artists, Albums, Songs, Genres, Folders; a Home Menu setting pins any of them back. |
| Quality on Now Playing | One quiet tag: "Lossless · 96 kHz" for files; radio shows no codec or bitrate (Station Info keeps them). |
| Hint lines | Removed; holding Select opens a menu that names the actions (Forget, Remove, Add to Favorites). |

## Rules (the contract)

One component per idea; screen code must not draw its own variant.``````````````````

| Idea | Rule |
| --- | --- |
| Accent | One fixed accent (theme::color::ACCENT, today's blue) for every control and state. The cover colour is used only by Now Playing's backdrop and the Home cover card. A skin's fixed accent still overrides. |
| Focus | Neutral glass row, bright text, same radius and inset everywhere: lists, settings, sheets, radio, playlists, search. Never colour alone. |
| State | Accent marks state only: playing item, check, switch on, progress, the Home marker. Focus and state never share a treatment. |
| Switches | Accent when on (no separate green). |
| Buttons | One shape. Glass when idle, white fill with dark text when focused. At most one primary per screen; destructive actions only in dialogs. |
| Live radio | One red LIVE pill. No "ON AIR". |
| Empty, info and error states | One component: centred icon, title, one sentence, optional button. Firmware messages use it with numbered steps (keeping system.img; the owner must copy that file). |
| Lists | Content (artists, albums, songs, stations, playlists, results) is flat and full width. Settings-type lists, including Bluetooth and Wi-Fi devices, are grouped cards. A chevron only on rows that open a page; a row that changes a value in place shows the value and no chevron. |
| Hints | No permanent hint lines. Hold-Select actions are listed in the item's menu. The keyboard's Cancel and Done keys are the only instructions it needs. |
| Rows | Title plus at most one secondary line of facts a listener uses (artist, album count, country · genre). No codec, bitrate, rank, free space or internal state in lists. |
| Words | American English, Title Case for titles and labels, sentence case for secondary lines. |
| Menus (8.36) | Menus hold actions on the item; preferences live in Customize. Every song and collection menu lists its shared actions in one order: Play, Shuffle · Play Next, Add to Queue · what this place changes (Move, Remove from …) · Add to Favorites, Add to Playlist… · Go to Album, Go to Artist · Select Songs…. A row that would not change anything is left out. No new row without removing one (test every_menu_lists_its_shared_actions_in_one_order). |
| Scrolling (8.37) | Headers stay; only lists scroll. The focus moves through the rows in view; the list moves one row when the focus reaches an edge, with the list glide. Album, playlist and audiobook headers, Display's brightness card and the search field stay put while the list under them scrolls (components::header_list_*, views_search::search_first, Ui::group_window). |
| Values | A row's value uses the room its label leaves and ends in "…" (sheets, and skins' right-aligned {detail} up to the end of {label}). |

## Screen changes
  - Home: Now Playing, Music, Playlists, Radio, Search, Settings; no counts. Right

side unchanged (playing cover with progress, or Recently Added). Music opens Artists, Albums, Songs, Genres, Folders. Settings → Display → Home Menu pins any of those five onto Home (stored with the other display settings; Reset Settings restores the default).
  - Now Playing: no "NOW PLAYING" eyebrow; mode icons only when they differ from

the default (shuffle, repeat, crossfade, equalizer on, normalise on), so gapless disappears; one quality tag. Radio: station and country line, `LIVE` pill, no codec/bitrate/country-code tags, no "ON AIR" under the bar.
  - Radio lists: "Switzerland · Jazz"; no rank badges, codec or bitrate (Station

Info keeps the facts). Favorites' empty line becomes the empty-state component.
  - Bluetooth: "Connected", "Paired" or "Not paired"; codec on Sound → Output.

Device list in a card; Forget in the device's hold menu.
  - Wi-Fi: "Connected", "Saved", "Open" plus bars; no signal words.
  - Up Next and playlists: Remove and Move in the hold menu; the moving row keeps

the focus style plus a grip mark, without an instruction line.
  - Keyboard: no hint line; keys gain the height.
  - Theme picker: a small preview per theme instead of "by Reborn"; the

how-to-add-skins sentence moves to the empty part of the list only when no external skin is installed.
  - Storage: Internal Storage and SD Card bars, Scan for Music. Song count moves to

About. "From a Computer" stays on the USB page only.
  - About: "Version 1.0 Beta 6.3" (the full build string stays on the hidden

service pages).
  - Folders: song counts, no free space.
  - Display: Album View gets the in-place-value treatment consistently.

Unchanged: the Home typography and layout, Cover Flow, the Now Playing composition, the status bar, dialogs' structure, the boot and shutdown sequences, the service and diagnostics pages (hidden; developer-facing by design).

## Skins

Skins draw layouts by name. The Music submenu needs a layout name (`music`), and the Home Menu setting changes Home's item list, which skins read through the engine. Both go into `tools/assets/build_skins.py` finishing steps (never hand-edited `skin.json`; Classic's hand-written json gets the layout by hand). Every shipped skin must load without warnings and render the new screens.

## Phases
  - Spec and audit (this document). Milestone-boundary audit row in Y2Linux

`docs/planning/roadmap-gap-audit.md`. Fix the preview fixture titles; keep a "before" preview set.
  - Components and tokens (`theme.rs`, `components.rs`): fixed accent outside

Now Playing, one focus row, one button, `LIVE` pill, empty-state component, accent switches; then remove every screen-local variant. Most of the "rough" feeling goes here.
  - Home and Music: submenu, Home Menu setting with persistence and reset,

navigation and back stack, skins' `music` layout.
  - Content trims per Screen changes, hold menus that replace hints.
  - Qualification: host previews before/after for Reborn's look and every skin;

tests and strict Clippy; device walk-through with screen capture while the owner presses the buttons (input cannot be injected over SSH).

Each phase is reviewable and releasable on its own.

## Phase 1 as implemented (2026-10-16)
  - `Ui::accent()` is the fixed accent (a skin's own, else `theme::color::ACCENT`);

`Ui::cover_accent()` is the cover's colour. Now Playing keeps the cover colour for its whole composition (backdrop, tags, mode icons, bar), as one picture; the Home cover card uses it for its glow and progress. Skins are drawn and remapped with the cover accent, so a skin looks as before.
  - `components::focus_row` (neutral glass, `FOCUS_FILL`; `FOCUS_OVER_BG` masks round

artwork on it) replaces `accent_row` and `glass_row` in every list, page, sheet, radio list, playlist, search result and the radio's playing card. Focused secondary lines stay `MUTED`; the playing item keeps its accent title whether focused or not; Up Next lost the outline that looked like a second focus.
  - `components::button` (glass idle, white with dark text focused): album/playlist

Play/Shuffle, artist Play All, Station Info, dialogs (a focused destructive choice keeps `DANGER`), the value page's Back, the empty-state button. The keyboard's focused key is white without the accent ring.
  - `components::empty_state` + `Mark` (icon in a ring, empty ring, spinner) + `empty_button`:

the library's empty and scanning states, Wi-Fi/Bluetooth off, every page hero (firmware, radio loading/errors, USB transfer, battery, Nothing Playing); the icon comes from the screen (`views_settings::hero_mark`).
  - Switches use the accent; Wi-Fi/Bluetooth "Connected" is accent state (was green); the

device and network lists sit in one grouped card with inset focus and rules.
  - One `LIVE` pill: the radio's playing card and Station Info said ON AIR; Now Playing no

longer writes ON AIR under the bar.
  - Information, not state, leaves the accent: the album count/length line in the grid and

Cover Flow is `DIM`. The Playlists and Radio section washes (pink and red glows) are gone; the moving playlist row is the focus row ringed in the accent.
  - Preview fixtures select Home items by key (`home_focus`); `70`–`74` show search again.
  - Evidence: 50 of 110 Reborn previews change (before/after compared by eye); skins: the

same 9 fallback screens in each of the 16 (Cover Flow detail colour, keyboard ring), everything a skin lays out itself is pixel-identical. 474 tests, strict Clippy.

Left for later phases as planned: hint lines, ranks, codec/bitrate, signal words, theme previews, spelling (3).

## Phase 2 as implemented (2026-10-16)
  - Home is Now Playing, Music, Playlists, Radio, Search, Settings, without counts

(`pages::home`). Pinned Music lists stand after Music in `HOME_PINNABLE` order (Artists, Albums, Songs, Genres, Folders); Home lays out up to eleven rows.
  - Music (`Screen::Music`, `views_library::music`) lists Artists, Albums, Songs, Genres and

Folders as menu entries with counts ("7 artists"); Playlists and Search left it (they are on Home). `components::menu_entry` is shared with Radio's menu, so both menus look alike. Back goes Artists → Music → Home (navigation history).
  - Settings → Display → Home Menu (`Screen::HomeMenu`): a switch per Music list;

`Effect::SetHomePin(key, on)`, stored as `Settings::home_pins` (`#[serde(default)]`, so older saved settings load with none; Reset Settings clears them; `Settings::pin_home` keeps Home's order). Display shows "Standard", the pinned names or "N lists added".
  - Display has one row more than fits under the brightness card: the four rows that fit

are drawn, and focusing further scrolls the card away (with a scroll rail).
  - Skins: no new layout was needed. Home rows come from the page, so every skin's `home`

layout shows the new menu (skins still add counts to pinned rows), and Music and Home Menu use each skin's `list`/`page` layout; all 16 checked by eye. `home_menu` is a known layout name for skins that want their own.
  - Previews: `53-home-menu`, `75-music`, `76-home-pinned`, `51b-display-last-row`

(114 states). Tests: Home's six rows, pin order and an eleven-row Home with one focus target, Music rows and Back through Music, Display → Home Menu pin/unpin effects, old settings without pins. 478 tests, strict Clippy.

## Phase 3 as implemented (2026-10-16)
  - Hints gone, menus teach. Removed: the keyboard's "Buttons move · Select types · Hold

Select: done · Hold Back: cancel" (its keys grow from 44 to 48 px), the live search's second lines ("Back on the top row picks one…", "Hold Back to cancel"), Bluetooth's "Select to connect · Hold to forget", Up Next's "Hold Select to remove", the radio Favorites row's "Hold Select on a station to add it" (now "No stations yet"), the moving row's "turn the wheel, Select to drop" (now "Moving"). Every one of those actions was already named in the item's hold-Select menu (Remove from Queue, Move Up/Down, Forget Device, Move, Remove from Playlist, Add to Favorites). Empty states that say how to fill a list stay (No Favorites Yet, an empty playlist): they are not permanent hints.
  - Now Playing: no "NOW PLAYING" label (the title moves up into its place; a station

keeps its LIVE line); no gapless icon (on by default); radio has no MP3/kbps or country-code tags (Station Info has them).
  - Lists: stations read "Switzerland · Jazz" (`views_radio::station_detail`, also the

skins' row text); no rank badges or "Top N". Bluetooth devices read Connected, Paired or Not paired (codec on Sound > Output). Networks read Saved, Secured or Open beside the bars. The Folders roots show song counts instead of free space.
  - Theme picker: a swatch per look (its background with an accent bar, read from the

skin's palette into `SkinInfo::swatch`) instead of "by Reborn"; the how-to-add sentence follows the last theme instead of standing under the list.
  - Storage: two bars and Scan for Music. "Songs in Library" moved to About & Updates as

Music Library (the count; opens Storage). "From a Computer" appears only while a cable is connected, so a dismissed computer screen can be reached again.
  - About & Updates: Version reads "1.0 Beta 6.3" (`short_version` also fixes "1.0.0 (3)"

for dotted betas and "1.0.0" → "1.0"; development candidates keep "1.0.0 (35)").
  - Words: "Normalize Volume" (American English throughout; the skin format's `normalise`

icon name is unchanged for existing skins).
  - Evidence: 38 of 114 Reborn previews change (compared by eye with phase 2); skins change

only where they show Reborn's keyboard, texts or rows (all 16 checked, keyboards fit under every skin's title bar). 479 tests, strict Clippy.

## Beta 7.5 refinements (owner request, 2026-10-16)
  - Status bar (owner chose layout C of four rendered variants): the screen's name sits

beside the back arrow in Title Case (Open Sans SemiBold 15, white) instead of centred tracked caps; clock SemiBold 15 and battery percentage SemiBold 13 in white; icons 18 px with Wi-Fi and Bluetooth at 22 px (they looked smaller than the USB plug at one size); battery 25 × 13; back arrow 22 px. Long names stop short of the cluster (`components::status_cluster` returns its left edge). Skins keep the compact cluster (`roomy: false`) in their own layouts.
  - Home header: "Reborn" and the short version ("1.0 Beta 7.5", muted) where other screens

show their name (`components::home_bar`).
  - Messages: the status-bar pill is 30 px high with SemiBold 15 text and an 18 px icon.
  - Skin: Theme is renamed Skin and is a Settings place of its own (seven rows of 44 px

fit without scrolling; palette icon). Display keeps Brightness and four rows and no longer scrolls. Skins are read from `Skins` folders, and still from `Themes`.
  - About & Updates: the Music Library row (it opened Storage) is gone; the song count is

the secondary text of Storage's Scan for Music.

## Beta 7.6 update screens (owner: "low fps", 2026-10-16)
  - Cause: the download and check counted only as a spinner, which redraws at the calm rate

(34-ms frame gap, ≤ 29 fps); the bar's highlight stepped ≈8 px a frame and jumped back to the start, and the percentage jumped with each platform report (4 a second) while the bar glided.
  - Now:`Ui::download_shown` (download or check visible, screen on) joins `gliding()`, so

these screens run at the panel's full rate; not `responding()`, so the niced download keeps the CPU clock decisions (no Interactive lease). The number counts with the gliding bar; the highlight fades in and out at the ends; the Connecting segment eases at each end.
  - Look: a step tracker (Download · Check · Install; done steps carry a check, the current one

the accent) replaces "STEP 1 OF 3 · DOWNLOAD", also on the restart screen; the bar is 10 px with a bright head where it grows. Preview `34d-update-installing` added.

## Not verified

Everything here is released (Beta 7 to 7.6) and checked on the host (previews, tests). On the device only the motion frame rate is measured (Beta 7.3: 62 fps median). Hold-menu discoverability without hints, the fixed accent, the Beta 7.5 status bar and the Beta 7.6 update screens on the panel need the device walk-through in phase 4.

## Customize and Wrap Around (Beta 8.18)

Settings gains a ninth place, Customize (how Reborn behaves; Display keeps how the screen looks): Wrap Around, Home Menu and Album View, the last two moved from Display. The Settings root shrinks its rows (44 px down to 34 px for nine) so every place stays in view.

Wrap Around (`Settings::wrap_around`, `reborn_core::WrapAround`) continues a list at the other end: past the last row to the first, before the first to the last. One press on the row steps Off → Menus → Everywhere. Menus (the default) covers Home, Music, Settings and its pages, and the hold and context menus; Everywhere adds the long lists (`Ui::is_long_list`: the library catalogs, Queue, Playlists, a playlist, Stations, Time Zone). All of it lives in `Ui::move_focus`, the one place every list moves.
  - Only a single step taken at an end wraps; an accelerated wheel step stops at the end.
  - A list of 40 rows or more (`ACCELERATED_LIST_MINIMUM`) also needs the wheel to rest at the

end for `WRAP_REST` (350 ms), so a fast spin through a long library stops at the last song and one more deliberate detent goes to the top.
  - A scale never wraps (an equalizer band's dB picker); Now Playing's wheel stays volume, and

the keyboard keeps its own grid.
  - A wrapped jump snaps instead of animating across the list (the motion layer already

shortens long jumps).

Previews: `20b-settings-last`, `51c-customize`, `51d-customize-everywhere`. On the player, the feel of the 350 ms rest and of the default still need checking.

## When Screen Off and headphone controls (Beta 8.18)

Customize also holds When Screen Off (`Settings::screen_off_buttons`, `reborn_core::ScreenOffButtons`), Y2Player's "Wheel When Screen Off" redone in the one place that owns screen-off policy, `reborn_platform::input::ActionRouter`:

| Choice | Wheel | Centre | Previous/Next (held: seek) | Play/Pause |
| --- | --- | --- | --- | --- |
| Locked | – | – | – | – |
| Buttons (default; Reborn's behaviour before) | – | – | yes | yes |
| Wheel + Buttons | volume, one step a detent | play/pause | yes | yes |

Back never acts in the dark. A button that rests is swallowed from press to release, even when the screen wakes in between. Power, the volume keys and headphone controls work in every choice: AVRCP commands (AirPods: press play/pause, double next, triple previous) arrive through BlueZ and `reborn_platform::avrcp`, never through the router, and `Action::PlayPause`/`NextTrack`/`PreviousTrack` are handled before the UI's screen-off gate. Holding the AirPods stem switches noise control inside the AirPods; the player is not involved.

A paused player with Bluetooth headphones connected stays awake for `HEADSET_PAUSE_AWAKE_SECS` (15 minutes) before automatic sleep, so the headphones can continue playback; asleep, the radio is off and nothing hears them. The 15 minutes count from the pause itself (`paused_at`) and end with the pause: a hold kept across a resume was already over at the next pause, and the player slept 60 s after it with the headphones connected (Y2Linux #90, F68; `platform::headset_hold_since`). The paused sink is still released after three minutes (`HOLD_LIMIT`); playing again then reopens it.

## Search page (Beta 8.32, owner request 2026-10-24)

Owner: the search "looks good but navigation wise it's a little tricky and also has some visual glitches". Findings before the change: two result views that disagreed (three rows above the keys without audiobooks and capped at 60; a second full page with an "Edit Search" row), results reached only by Up through the top key row (landing on the third row, and the same press wrapping to Done when nothing was found), the wheel dead while typing, Back from an opened result landing on a page never seen, one mixed list without headings, audiobooks matched inside words; the focused live row covered the scroll rail, the count crowded long text out of the field, round artist covers showed grey square corners while the focus glided.
  - One page. Search is the Search screen with the keys over it. The field stays in

place; the first three results show above the keys, each saying what it is ("Artist · 2 albums"). Up from the top key row, a turn of the wheel, Search or holding Select folds the keys away (180 ms) and the focus lands on the first result. Up through a lower row only moves up; with nothing found Up still wraps to Done.
  - The page: the field (Select brings the keys back with the text, rising into place),

then ARTISTS, ALBUMS, AUDIOBOOKS and SONGS headings with counts. Headings are not stops; the window keeps a result's heading and the first heading's field in view. Songs start with Play All (two or more songs), which plays the songs found in the page's order. Songs show "artist · album".
  - Back: from an opened artist or album to the page with the same focus; from the page

back to the keys with the text (#44). On the keys Back is the Up arrow. Cancel, or holding Back while typing (also when its press already folded the keys), leaves Search, text or not, to the screen it was opened from (#51).
  - Matching: audiobooks match as music does (every typed word begins a word of title or

author); the count includes them.
  - Motion: typing changes the page's text without a screen slide; list scrolling uses

`Moving::Scroll` (pixel offset, rows of differing heights); round covers mark `Moving::Corners`, so their corners take the colour under them where the gliding focus is now (also in Artists).
  - Input:`ActionRouter::set_keyboard_wheel` lets wheel turns through while the search's

keys are up; its buttons stay arrow keys.
  - Skins draw the page with their list layout: headings as dim rows, the field as "Edit

Search". Previews `70`–`71e`.

## Queue and Up Next (Beta 8.33, owner request 2026-10-24)

Assessment before the change: every queue edit while playing reloaded the song (`load()` restarted the decoder from the last reported position, ≈0.3 s of audio dropped) only so the gapless pre-open learned the new next song; Add to Queue appended after up to 5 000 songs of All Songs; Next on the last song with Repeat All and Previous on the first song stopped playback; Shuffle changed only what started later; two Play Next ran backwards; Up Next opened on played songs (Y2Linux #60); moving was one menu trip per place (Y2Reborn #32); no multi-select (#26); queue actions missing on albums/artists/genres/folders/search (#31); the session saved ≈820 bytes per queued song on every song change.
  - Model (`reborn_core::queue`): one list in play order. Entries you queue

(`queue_queued`) stay one block right after the song playing (`anchor_queued` after Previous/jumps); the source keeps its own order (`queue_order`, Shuffle off restores it) and name (`queue_source`, from `Effect::PlayCollection::source`). Play Next = top of your queue (newest first), Add to Queue = end of your queue. Repeat All starts over without your played songs (also gapless: `upcoming` wraps, `TrackBoundary` may land near the start). History: last 50 played (`note_played`, source+path), kept in the session.
  - Engine:`Playback::set_upcoming` hands the running decoder the next `UPCOMING` (32)

entries; it re-opens the next song only if it changed. Every edit, Shuffle, Repeat and each song boundary refresh it — no edit restarts the song (test `a_new_upcoming_list_changes_the_next_song_without_a_restart`).
  - Session schema 3: library songs stored as `{"ref":[source, path, id]}` (≈¼ size), filled

from the library when it loads (`rehydrate_queue`); stations whole; older sessions read.
  - Up Next screen (`up_next`, `views_queue`): opens on the song playing; HISTORY above

(a scroll up, played songs dim), QUEUE, NEXT FROM , headings with counts that are not stops. Select plays (a history song plays now, before what was playing). Hold Select: Play Next, Move, Remove from Queue, Select Songs…, Add to Playlist…, Go to Album, Clear Queue / Clear Upcoming. Move: the row lifts (accent outline, title "Moving"), each wheel detent moves it one place, crossing into or out of your queue; Select/Back puts it down.
  - Select Songs (Up Next, Songs, an album, search): Select ticks rows, the title counts

them ("2 Selected"), hold Select acts on them in list order (Play Next, Add to Queue or Remove from Queue, Add to Playlist…, Done), Back ends it. Skins see ticked rows as `RowKind::Check`.
  - Queue actions everywhere: hold Select on an album, artist, genre or folder row, or the

search's Play All: Play, Shuffle, Play Next, Add to Queue, Add to Playlist… (`group_*`). Toasts confirm ("Plays next", "12 songs added to queue", "2 songs removed").
  - Now Playing: a NEXT line under the status icons; its menu's Up Next row names the next

song. Previews `17`–`17f`, `18c`, `10b`.

## One menu order, Customize choices (Beta 8.36, owner request 2026-10-25)

The owner asked that new features not bloat menus and that the UI work the same way everywhere, with labels that mean what they say. Rules added to Rules: menus hold actions, Customize holds preferences, one order for shared actions, no growth without removing a row.
  - Song menus (Songs, an album, an artist page, search, playlists' songs, Up Next):

Play Next, Add to Queue, [Move, Remove from …], [Add to Favorites], Add to Playlist…, Go to Album, Go to Artist, [Select Songs…]. Select Songs moved to the end; Up Next gained Add to Queue (`Effect::QueueEntriesLast`, the end of your queue as everywhere else; for chosen songs too) and Go to Artist; Play Next / Add to Queue are left out where they would not move the song.
  - Up Next's song playing holds what acts on the whole list: Add to Playlist…, Go to Album,

Go to Artist, Save Up Next as Playlist… (moved from Now Playing, which has 8 rows now), Clear Queue, Clear Up Next (was "Clear Upcoming"). Other rows no longer carry Clear.
  - Playlists (hold on a playlist): Play, Shuffle, Play Next, Add to Queue, Rename,

Duplicate, Delete Playlist — as an album.
  - Customize (each row names what it changes; Select steps the value): Home Menu ›,

Cover Flow On/Off (was Album View Cover Flow/Grid; now Albums and Audiobooks), Artists All/Album Artists (#41: `albumartist:` filter, a compilation is one artist, `album_artist_of` falls back to the first artist), Now Playing Wheel Volume/Seek (#34: Seek steps as holding Previous/Next does; stations keep volume; the volume buttons always change the volume), Wrap Around, When Screen Off.
  - An album opened from a genre (#50) shows that genre's songs (`album:` filters carry

`\u{1f}genre:G`; the row plays what it opens), its header says "Jazz · 2 of 3 songs", and a last row Show All 3 Songs opens the whole album. No setting.
  - Values fit their row: the Now Playing menu's Up Next row names the whole next song when

the label leaves room (#60); skins get the same through `{detail}`.
  - Artist page shows the artist it is for (not its first song's whole tag).

Previews `51c-customize`, `09b-album-from-genre`, `17e`–`17h`, `b2-audiobooks` (Cover Flow). Haptics (#28): Customize > Haptics Off (default) / Light / Strong (`Settings::haptics`, `reborn_core::Haptics`). `reborn_platform::haptics::Motor` plays one 60 ms rumble on the kernel's `regulator-haptic` input (PMIC VIBR) for each button press on a lit screen, as the stock firmware's key press (framework `config_virtualKeyVibePattern`); wheel steps do not tick (30 ms per-step ticks felt buzzy on the owner's player). Light is 2.0 V, Strong the stock 2.8 V.

Internal speaker (#28 speaker): Settings > Sound > Output > Speaker (on by default, as stock's "Speaker"). The Headphone Jack output plays on the speaker while the kernel reads the jack empty (`reborn_platform::jack`, "Y2Audio Headphone" SW events; unknown counts as headphones). The output's name then reads "Speaker". The DAC's speaker route plays one channel, so the gain stage mixes (L+R)/2 (`VolumeRamp::mono`); the sink switches the card's Speaker pin with Master −3 dB (stock's top speaker step). Headphones in while the speaker plays: the kernel turns the speaker off at once and playback reopens on the headphones; headphones out while they play: pause, as stock. Not yet heard on a player.

## Sleep timer lengths (Beta 8.37, Y2Reborn #29)

Now Playing's Sleep Timer row opens a picker instead of stepping on each press: Off, End of Song (End of Chapter in a book), 5, 10, 15, 20, 30, 45 min, 1 h, 1 h 15, 1 h 30, 2 h, 2 h 30, 3 h (`SLEEP_MINUTES`). It opens on the timer set (else 30 min), marks it ("23 min left"), stops at its ends; Select starts it, Back leaves it as it was. Now Playing keeps "Sleeps in 23 min" opposite the output and now redraws it as the minutes change, also while paused. Skins get `{sleep}` and `"if": "sleep"`; every shipped skin shows "Headphone Jack · Sleeps in 23 min" on its output line (`build_skins.py``add_sleep`), and the `moon` icon. No menu row added. Previews `14c-now-playing-sleep`, `14d-sleep-timer-picker`.

## Search: one level at a time, short sections, playlists (Beta 8.37, Y2Reborn #44)
  - Back goes up one level: in the results Back raises the keys with the text (as Edit Search);

in the keys Back moves up a row and on the top row leaves the search (`keyboard::Outcome::Leave`; before it went into the results). The wheel or Done/hold Select still folds the keys into the results.
  - A new search starts empty (`library_query` removed); a result opened and Back keeps the search.
  - Playlists are a section after Albums, matched by name like books (`Catalog::playlists`, refreshed

by the playlists' generation; search reads them if Playlists never did). Select opens the playlist, hold Select gives its menu.
  - Short sections: on the whole page each section shows its first `SECTION_PREVIEW` (4) results

and See All N … (`search_all:<section>`), which opens that section alone (filter `query\u{1f}section`, titled by the section, sliding like a page); Back returns to all results. Play All and a song's queue take every song found (`Catalog::search_songs`), not only those shown.

Previews `71f-search-see-all`, `71g-search-songs-alone`, `71h-search-playlist`.

## One way of scrolling (Beta 8.37, owner request)

The playlist page lost its focus below the screen (its header stayed until the sixth song while showing three); the owner then asked for one way of scrolling everywhere and, after trying a header that scrolled away with its list, chose: headers stay, only the list scrolls. Album, playlist and audiobook pages keep their header and scroll the songs or chapters under it (three rows and the next one's top; the list is drawn first, the header over it, so a row gliding up passes under it). Display keeps the brightness card over its rows; the search keeps its field over the results (a section alone has none). Settings pages keep their rows until the focus reaches an edge (`Ui::group_window`, their own memory: the rows that fit under a page's text differ) and glide. Up Next and the long lists were already so. The artist page keeps its sideways row of albums. Tests `a_page_header_stays_and_its_list_scrolls_one_row_at_a_time`, `a_playlist_page_keeps_the_focused_song_on_screen`, `settings_pages_keep_their_rows_until_the_focus_reaches_an_edge`.

## The live wave (Beta 8.38, owner request)

The progress wave on Now Playing (and now Home's card) is drawn as one ribbon: points every 2 px with averaged normals, a 2.6-px core and a 1-px edge on each side fading to transparent through the quad's corner colours — edge anti-aliasing without MSAA, and no beading because the pieces share their joints. It moves with the music (`Levels`: bass, mids, highs, 0..1): height 0.35 + 0.85 × loudness (typical music as tall as before, loud up to about a third more), bass swells it, highs ripple it; without levels (nothing measured) it waves as before. Not a spectrum visualizer (the owner: "not yet"). Previews `14e-now-playing-loud`, `14f-now-playing-quiet`.

## Folders, Shuffle Albums, playlist Sort (Beta 8.39, user report)

A folder-first listener with 120 000 songs and loose tags. Folders shows a folder as a file manager does: its folders, then its songs, both by name (case and accents folded, numbers as numbers), songs by file name without the extension, the line under it the artist; folder rows say how many songs they hold. A song plays its folder's songs in that order; Play on a folder plays its folders first, then its songs, all the way down. Storages are titled SD Card and Internal Storage. Shuffle steps Off → Songs → Albums (Now Playing's menu, Settings → Playback): Albums plays whole albums in random order, each in disc/track/file order (an album = its folder, CD/Disc folders folded, and its album tag); Shuffle Albums is also in the menus of folders, artists, genres, playlists and an artist's Play, not an album's. Sort in a playlist's menus (and on holding its Play or Shuffle) steps Playlist Order → Album → Artist → Title → File Name, the menu staying open; the page shows and plays in that order, the file is unchanged, Move only in Playlist Order. Previews `13-folder`, `13b-folder-songs`. Tests `a_folder_lists_its_folders_then_its_songs_by_file_name`, `playing_a_folder_follows_folders_order_and_offers_shuffle_albums`, `shuffle_steps_through_off_songs_and_albums`, `a_playlist_sorts_its_page_and_plays_in_that_order`.

## One album once, Album Order, letter scrolling (Beta 8.43, Y2Reborn #45 #46 #56 #30)
  - One album once (#45, #46): when the library loads (`reborn_core::albums::unify_album_artists`, on the

library thread), the songs of one album title in one folder of one storage share its album artist: an empty Album Artist takes the one the others carry, spellings that differ only in capitals or spaces take the most common one. Only when the album names exactly one; a compilation without the tag, or an album naming two, stays as it is (falling back to the song's artist would split a compilation per song). Albums, an artist's page, search, counts and Cover Flow then list it once. The library file is unchanged; Last.fm gets each song's own tag (`Track::tagged_album_artist`). Tests `an_album_with_and_without_album_artist_is_listed_once`, `albums::tests`.
  - Album Order (#56): Customize > Album Order Title (default, as before) / Artist (`Settings::album_order`,

`reborn_core::AlbumOrder`): by the artist an album row shows ("The" skipped), then title. Albums and Cover Flow share it; the fast-scroll letter is the artist's. A new Customize row (no existing row holds an order). Test `albums_order_by_title_or_by_artist_and_the_letter_follows`.
  - Letter scrolling (#30): once the wheel turns fast enough (3 steps: six detents, smoothed ≤70 ms apart; Y2Linux #64 — 2 steps came too

easily, 4 was out of reach) that the letter shows in an A to Z list (Songs, Artists, Albums and Cover Flow, Folders), each detent goes to the first row of the next letter, or back to the first row of this letter, else the one before; the letter stays 700 ms (`FAST_SCROLL_LINGER`) after the last detent, so turning back after overshooting stays by letter, then rows step again. After the last letter the wheel goes to the last row; a rested wheel wraps as before. Other lists keep their row steps. No setting. Albums and Cover Flow now show the letter too. Tests `fast_scrolling_steps_by_letter_and_lingers`, `lists_without_letters_keep_their_row_steps`.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
