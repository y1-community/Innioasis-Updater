---
title: "Making skins for Reborn - Innioasis Updater"
description: "Making skins for Reborn A skin changes how Reborn looks: its colours, fonts, pictures and the layout of its screens. You write it as one text file, skin.json , plus any p"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-skins.html"
---

# Making skins for Reborn - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Making skins for Reborn

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Making skins for Reborn

A skin changes how Reborn looks: its colours, fonts, pictures and the layout of its screens. You write it as one text file, `skin.json`, plus any pictures and fonts you want, and copy the folder onto the player. No programming and no computer tools are needed; a text editor is enough.

A skin only changes the look. What the buttons do, the menus, playback and settings stay the same in every skin. Reborn's own look is always available as Reborn in the skin picker, so you can never lock yourself out.

This guide starts with the quickest way to a skin and builds up step by step. The [reference](#reference) at the end lists everything a skin can use.
  - [Install a skin](#install-a-skin)
  - [The fastest start: change a shipped skin](#the-fastest-start-change-a-shipped-skin)
  - [Your first skin, step by step](#your-first-skin-step-by-step)
  - [The example skins](#the-example-skins)
  - [Recipes for a completely different look](#recipes-for-a-completely-different-look)
  - [How Reborn chooses what to draw](#how-reborn-chooses-what-to-draw)
  - [Checklist for a complete skin](#checklist-for-a-complete-skin)
  - [Testing your skin](#testing-your-skin)
  - [Sharing your skin](#sharing-your-skin)
  - [When something goes wrong](#when-something-goes-wrong)
  - [Reference](#reference)

## Install a skin
  - Connect the player to your computer.
  - Make a folder named `Skins` on Internal Storage or on the SD card, if there isn't one yet.
  - Copy the skin's folder into it, so that its `skin.json` ends up at, for example,

`Internal Storage/Skins/Ember/skin.json`.
  - On the player: Settings → Skin, then pick it. It applies at once and is remembered.

The Skin list is read again every time you open it, so after changing `skin.json` just open Settings → Skin again and pick your skin once more to see the change. A skin with a problem shows greyed out with the reason; see [When something goes wrong](#when-something-goes-wrong).

## The fastest start: change a shipped skin

Reborn comes with 17 skins, and each is a complete example. The easiest way to make your own is to copy one and change it:
  - Download a skin folder from [`skins/`](https://github.com/SchulzCode/Y2Reborn/tree/main/skins) on GitHub, for

example `neon` or `paper`, or the example skin of this guide, [`docs/skin-example/Ember`](https://github.com/SchulzCode/Y2Reborn/tree/main/docs/skin-example/Ember).
  - Rename the folder (for example to `MyNeon`) and change `"name"` inside `skin.json`. A folder with the same name

as a shipped skin is hidden behind the shipped one.
  - Change the colours in `"palette"` (see [step 1](#step-1-colours-only)), copy the folder into `Skins` and pick it.

## Your first skin, step by step

This walks you through Ember, a warm dark skin. The finished skin is in [`docs/skin-example/Ember`](https://github.com/SchulzCode/Y2Reborn/tree/main/docs/skin-example/Ember). Two more examples, [Poster and Console](#the-example-skins), show how far a skin can go from there.

The screen is 480 × 360 pixels. Positions are measured from the top-left corner: `x` goes right, `y` goes down.

### Step 1: colours only

The smallest useful skin is just a name and a few colours. Every screen keeps Reborn's own layout, drawn in your colours:`{ "format": 1, "name": "Ember", "author": "Your Name", "version": "1.0", "description": "Warm orange on dark brown.", "palette": { "bg": "#1B1410", "text": "#FFF4E6", "muted": "#C9B8A6", "dim": "#8F7F70", "accent": "#FF9F43" } }`

Ember with colours only: Now Playing and Home in Reborn's layouts with warm colours
  - `format` is always `1`, and `name` is what the picker shows. These two are the only fields a skin must have.
  - `bg` is the background, `text` the main text, `muted` and `dim` the quieter texts, `accent` the highlight colour.

The [palette table](#palette) lists all colour names. Leave `accent` out (or write `"cover"`) and the highlight follows the colours of the playing album cover, as in Reborn's own look.
  - Colours are written as `#RRGGBB`, like on websites. Any colour picker shows these codes.

Many good skins stop here. The next steps replace Reborn's layouts with your own.

### Step 2: your own Now Playing screen

A screen is a list of elements, drawn in order: later ones on top of earlier ones. Add a `screens` section next to `palette`:`"screens": { "now_playing": [ { "type": "art", "x": 16, "y": 52, "size": 196, "source": "current", "radius": 14 }, { "type": "text", "x": 230, "y": 56, "w": 234, "h": 0, "lines": 2, "text": "{title}", "font": "S25" }, { "type": "text", "x": 230, "y": 128, "w": 234, "h": 24, "text": "{artist}", "font": "R17", "color": "muted" }, { "type": "text", "x": 230, "y": 154, "w": 234, "h": 22, "text": "{album}", "font": "R15", "color": "dim" }, { "type": "icon", "x": 230, "y": 214, "size": 32, "icon": "play_pause", "color": "accent" }, { "type": "bar", "x": 16, "y": 268, "w": 448, "h": 6, "value": "progress", "track": "track", "fill": "accent", "radius": 3 }, { "type": "text", "x": 16, "y": 280, "w": 100, "h": 20, "text": "{elapsed}", "font": "R13", "color": "muted" }, { "type": "text", "x": 364, "y": 280, "w": 100, "h": 20, "text": "{remaining}", "font": "R13", "color": "muted", "align": "right" } ] }`

What each element does:
  - `art` draws the cover of the song playing, `size` pixels square, with rounded corners (`radius`).
  - `text` writes text into a box `w` wide and `h` high. Words in curly braces are filled in by Reborn:

`{title}`, `{artist}`, `{elapsed}` and [many more](#text-values). Text that doesn't fit ends with "…". With `"h": 0` and `"lines": 2`, long titles wrap onto a second line.
  - `font` picks a size and weight. `R` is regular, `S` semibold, `L` light, and the number is the size in pixels:

`R13`, `S25` and so on ([list](#fonts)). Step 4 shows how to use your own fonts.
  - `icon` draws one of Reborn's [icons](#icons). `play_pause` shows pause while music plays and play otherwise.
  - `bar` draws a progress bar. `value` says what it shows: `progress`, `volume`, `battery` or `brightness`.

Only Now Playing changed; every other screen still uses Reborn's layout in your colours.

### Step 3: a title bar for every screen, and lists

The same status bar on every screen would mean repeating it many times. Parts solve that: describe it once under `parts` and place it with `{ "type": "part", "name": "…" }`.`"parts": { "titlebar": [ { "type": "rect", "x": 0, "y": 0, "w": 480, "h": 36, "color": "#120D0A" }, { "type": "icon", "if": "back", "x": 10, "y": 8, "size": 20, "icon": "back", "color": "muted" }, { "type": "text", "if": "has_clock", "x": 290, "y": 0, "w": 70, "h": 36, "text": "{clock}", "font": "R13", "color": "muted", "align": "right" }, { "type": "indicators", "x": 418, "y": 10 }, { "type": "bar", "x": 424, "y": 12, "w": 40, "h": 12, "value": "battery", "track": "track", "fill": "text", "radius": 3 } ] }`
  - `rect` is a filled rectangle, here the bar's background.
  - `"if"` draws an element only in some situations. `back` is true on every screen except Home, so the back

arrow only shows where Back does something. `has_clock` is true once the player knows the time. [All conditions](#conditions).
  - `indicators` draws the status icons Reborn's own bar has (charging, computer connected, Bluetooth, Wi-Fi),

closing up when one is off. `x` is its right edge.

Put `{ "type": "part", "name": "titlebar" }` first in `now_playing`, followed by the screen's name (`{ "type": "text", "x": 38, "y": 0, "w": 250, "h": 36, "text": "{screen}", "font": "S15" }`), and do the same on every screen you describe.

Now a `list` screen, used for every list in Reborn: the main menu, your music, settings, pickers and more:`"list": [ { "type": "part", "name": "titlebar" }, { "type": "text", "x": 38, "y": 0, "w": 250, "h": 36, "text": "{screen}", "font": "S15" }, { "type": "list", "x": 0, "y": 40, "w": 480, "rows": 7, "row_height": 44, "row": [ { "type": "part", "name": "row" } ], "focused": [ { "type": "rect", "x": 6, "y": 2, "w": 468, "h": 40, "color": "accent", "radius": 8 }, { "type": "part", "name": "row" } ], "scrollbar": { "x": 474, "w": 4, "track": "track", "thumb": "accent" } } ]`
  - The `list` element shows `rows` rows of `row_height` pixels and scrolls by itself.
  - `row` is drawn for every row and `focused` for the selected one. Inside a row, `x` and `y` count from the

row's top-left corner.
  - `{screen}` is the screen's name ("Albums", "Settings"). It is empty on Home.

And the row part, under `parts` next to `titlebar`:`"row": [ { "type": "text", "if": "numbered", "x": 16, "y": 0, "w": 36, "h": 44, "text": "{track_number}", "font": "R15", "color": "dim" }, { "type": "art", "if": "row_art & !numbered", "x": 16, "y": 6, "size": 32, "source": "row", "radius": 6 }, { "type": "text", "if": "row_art | numbered", "x": 60, "y": 0, "w": 250, "h": 44, "text": "{label}", "font": "S17" }, { "type": "text", "if": "!row_art & !numbered", "x": 16, "y": 0, "w": 294, "h": 44, "text": "{label}", "font": "S17" }, { "type": "text", "if": "has_detail", "x": 310, "y": 0, "w": 136, "h": 44, "text": "{detail}", "font": "R13", "color": "muted", "align": "right" }, { "type": "icon", "if": "chevron", "x": 450, "y": 14, "size": 16, "icon": "chevron", "color": "dim" }, { "type": "icon", "if": "checked | toggle & on", "x": 446, "y": 12, "size": 20, "icon": "check", "color": "accent" } ]`
  - `{label}` is the row's text and `{detail}` its value on the right ("24 songs", "Brightness 80%").
  - `row_art` is true for rows with a cover (albums, songs); `numbered` for songs on an album page, which show their

track number instead. `!` means "not", `&` "and", `|` "or".
  - `chevron` rows open another page; `toggle` rows switch something on and off (`on` when it is on); `checked`

marks the current choice in a picker.

### Step 4: your own fonts and pictures

Put font files in a `fonts` folder and pictures in an `images` folder inside your skin, then give them names:`"fonts": { "title": { "file": "fonts/DejaVuSansCondensed-Bold.ttf", "size": 24 }, "label": { "file": "fonts/DejaVuSansCondensed-Bold.ttf", "size": 17 } }, "images": { "highlight": "images/highlight.png" }`

Then use the names: `"font": "title"` in a text element, and the picture in an `image` element, here as the selected row's background instead of the `rect`:`{ "type": "image", "x": 6, "y": 2, "w": 468, "h": 40, "image": "highlight", "slice": [6, 6, 6, 6] }`

`slice` keeps 6 pixels at each edge (left, top, right, bottom) at their size and stretches only the middle, so a small picture with rounded corners fits any width. Each font entry is one size; for two sizes, add two entries pointing at the same file.

### Step 5: Cover Flow and square covers

Cover Flow is drawn by Reborn, but your skin decides what goes around it. Draw Reborn's Cover Flow with a `native` element, then your title bar over it:`"cover_flow": [ { "type": "native", "part": "screen" }, { "type": "part", "name": "titlebar" }, { "type": "text", "x": 38, "y": 0, "w": 250, "h": 36, "text": "{screen} · {position}", "font": "S15" } ]`

Reborn's drawing includes its own title, so give your title bar an opaque background (the `rect` in step 3) to cover it. `{position}` says where you are, such as "25 of 100". Add `"captions": false` to the `native` element to write the album's name, artist and length yourself with `{flow_title}`, `{flow_artist}` and `{flow_detail}`.

Album covers have rounded corners unless the skin says `"cover_shape": "square"` at the top level of `skin.json` (next to `"name"`). This applies in lists and in Cover Flow.

The finished Ember: Now Playing, Home, Cover Flow and Now Playing with a sleep timer.

The finished Ember skin on four screens

## The example skins

Three example skins come with this guide, in [`docs/skin-example`](https://github.com/SchulzCode/Y2Reborn/tree/main/docs/skin-example). They look nothing alike, and between them they use every element, field, text value and condition the engine has, so whatever you look up in the [reference](#reference), one of them shows it at work. Copy one into `Skins` to try it, or take pieces from them. Their files are free to use (CC0); the fonts keep their own free licences, included.[](https://github.com/SchulzCode/Y2Reborn/tree/main/docs/skin-example/Ember)[](https://github.com/SchulzCode/Y2Reborn/tree/main/docs/skin-example/Poster)[](https://github.com/SchulzCode/Y2Reborn/tree/main/docs/skin-example/Console)

| Example | Look | What to learn from it |
| --- | --- | --- |
| Ember | warm and calm, close to Reborn's own layout | the basics, as in the steps above: palette, parts, lists, a font, a stretched picture, Cover Flow |
| Poster | the cover fills the screen, big capital letters, colours follow the cover | your own Home screen, layouts for single screens (Artists, Up Next), fades over the cover, toggles and checkmarks drawn yourself, empty lists, groups, a progress bar with a knob, live radio, toasts and the volume |
| Console | a pocket game console from pictures and a pixel font | a full-screen background picture, window frames and bars made of pictures, a vertical volume bar, tinted pictures, menus and questions (also the red "danger" kind), pages with facts, the brightness bar, the keyboard and equalizer, one row template for every state |

Poster: Now Playing, Home, Artists and a radio station

Console: Now Playing, Wi-Fi, a question and the volume

## Recipes for a completely different look

The ideas behind Poster and Console, so you can build your own design instead of changing Reborn's.

The cover as the background (Poster). Draw the cover first and big, then lay vertical `gradient`s over it that fade into the background, and put the text on top:`{ "type": "art", "x": 60, "y": 0, "size": 360, "source": "current" }, { "type": "gradient", "x": 0, "y": 110, "w": 480, "h": 160, "top": "clear", "bottom": "ink" }`

`clear` and `ink` are names from Poster's `colors` (`#0B0B0C00`, fully transparent, and `#0B0B0C`). A cover is at most 360 pixels; gradients only run from top to bottom. With `"accent": "cover"` in the palette, everything drawn in `accent` takes the colours of the playing cover.

Your own Home screen (Poster). Describe `home` and it replaces Reborn's main menu. Its `list` holds the menu entries (`{label}`); add what you like around it: the cover behind it (`"if": "has_art"`), the song playing, the skin's name (`{skin}`).

One layout for one screen (Poster). A layout named after a screen wins over `list`: Poster's `artists` shows names in big letters with `{number} / {count}`, and its `queue` (Up Next) adds the position in the queue. The [screen names](#screens) are listed in the reference.

Everything from pictures (Console). Draw small pictures and stretch them with `slice`:
  - a window: a 24 × 24 frame picture with `"slice": [6, 6, 6, 6]` stretches to any size and keeps its borders;
  - a selection cursor: the same idea for the focused row;
  - bars: `track_image` and `fill_image` (with `slice`) instead of colours; `"vertical": true` fills upwards;
  - a background: a full 480 × 360 picture as the first element of a screen;
  - tinting: a white picture with `"tint": "accent"` takes exactly that colour, so one picture serves every colour

(Console's logo, and its red question frame with `"tint": "danger"`).

Draw states yourself. Rows tell you what they are: `toggle` with `on`, `check` with `checked`, `chevron`, `disabled`, `current` (the song playing), `first`, `last`, `odd`. Poster draws a switch from two rounded `rect`s; Console writes `[ON]` and `[x]`. A single row template with `"if": "focused"` parts (Console) works as well as separate `row` and `focused` templates (Poster).

Menus, questions, messages and volume.`sheet` is for menus that slide up, `dialog` for questions (`danger` when it deletes or resets something), `toast` for short messages (`error` when something failed) and `volume` for the volume. Start a `sheet` or `dialog` with a full-screen `rect` in `scrim` colour to dim what is behind it.

Pages with facts.`page` screens (About, Storage and others) have a heading (`{page_title}`), a text (`{page_body}`), label and value pairs (a `list` with `"source": "facts"`) and sometimes buttons (`"if": "interactive"`). Console shows all four.

Reborn's parts inside your design. A `native` element draws a piece of Reborn in your palette: `screen` for the whole screen (Cover Flow, the equalizer, the keyboard), `status` for Reborn's clock, battery and radio icons (Poster). `"recolor": false` keeps Reborn's own colours (Console's equalizer). Draw your own title bar over a `screen` part, with an opaque background so Reborn's title doesn't show through.

Fonts. One font file can be listed several times at different sizes (Ember, Poster). For a very large size, `"charset": "ascii"` keeps only plain letters and saves room in the texture (Console's big pixel font).

## How Reborn chooses what to draw

For each screen, Reborn looks for the most specific layout your skin has, and falls back step by step:
  - the screen's own name, for example `albums` or `wifi` ([all names](#screens));
  - its group: `list` for lists, `page` for pages with a heading or facts (About, Storage);
  - Reborn's own layout, in your colours.

`home` falls back to `list`, so a skin with a `list` layout changes the main menu too unless it also has `home`. Some screens are always Reborn's, in your colours: pairing a Bluetooth device, installing an update, the Quick Menu, starting and turning off. Cover Flow, the equalizer and the keyboard use only their own name, never `list`.

## Checklist for a complete skin

Reborn's shipped skins all do these five things, and a skin that wants to ship with Reborn must too. They are good practice for every skin, because without them a listener misses something Reborn's own look shows:
  - Status icons: an `indicators` element in the title bar (charging, computer, Bluetooth, Wi-Fi).
  - Sleep timer: on Now Playing, `{output} · {sleep}` when a sleep timer runs:

```json { "type": "text", "if": "!sleep", "x": 16, "y": 318, "w": 448, "h": 24, "text": "{output}", "align": "center" }, { "type": "text", "if": "sleep", "x": 16, "y": 318, "w": 448, "h": 24, "text": "{output} · {sleep}", "align": "center" } ```
  - Track numbers: list rows show `{track_number}` where `"if": "numbered"`, as in step 3.
  - Cover Flow: a `cover_flow` layout, as in step 5.
  - Cover shape:`"cover_shape": "rounded"` or `"square"`, matching your Now Playing cover.

Also worth checking: an empty list (`"if": "empty"` with `{empty_title}` and `{empty_body}`), the volume overlay (`volume`), menus that slide up (`sheet`) and questions (`dialog`). A skin that leaves them out gets Reborn's, in its colours, which is fine.

## Testing your skin

On the player: copy the folder into `Skins`, open Settings → Skin and pick it. After each change, copy `skin.json` again and pick the skin again. A skin with a mistake is greyed out with the reason.

On a computer (for people comfortable with a terminal): Reborn's preview draws every screen in your skin, over 200 of them, so you see them all at once. From a [Y2Reborn](https://github.com/SchulzCode/Y2Reborn) checkout, with Rust and the FFmpeg development files installed:`cargo run --bin reborn-preview -- out/preview --skin path/to/Ember python3 tools/preview/render_previews.py out/preview`

`out/preview/png/` then holds a picture of every screen and a contact sheet.

## Sharing your skin
  - Share the whole folder (zipped is fine). Others install it the same way, into `Skins`.
  - Only include fonts and pictures you may share. Free fonts under the SIL Open Font License or similar are fine;

fonts that came with your computer usually are not. Put their licence files in the folder, and a `LICENSE.txt` saying where your pictures come from.
  - Want your skin shipped with Reborn? Open an issue or pull request on

[Y2Reborn](https://github.com/SchulzCode/Y2Reborn) with the folder. It needs the [checklist](#checklist-for-a-complete-skin) and licences that allow sharing, as Luna XP (contributed by eNKay) does.

## When something goes wrong

Reborn checks a skin when you pick it and names the first problem and where it is. The skin is then greyed out in Settings → Skin and the player keeps its current look. If a chosen skin disappears (the SD card was taken out), Reborn uses its own look until the skin is back.````````[](#text-values)````````````[](#elements)``[](#conditions)````````

| The message says | What to do |
| --- | --- |
| palette: text on bg has a contrast of 1.2:1; at least 3:1 is needed | Text must be readable on the background: make text lighter or bg darker (or the other way round). Below 4.5:1 the skin still loads, with a warning. |
| screens.list[0] (text): unknown value "{lyrics}" | Only the text values exist. list[0] means the first element of the list screen (counting from 0). |
| skin.json: unknown field `colour`, expected one of … at line 1 column 106 | A misspelt field name (here colour instead of color). The line and column show where. |
| screens.list[0]: "text" has no field "radius" | That element type does not take this field. The elements table lists what each type takes. |
| screens.list[0] (text): unknown condition "playng" | A misspelt condition. The conditions list has all names. |
| a JSON error with a line number | A missing comma, quote or bracket near that line. A code editor or a JSON checker website shows where. |
| the pictures and fonts do not fit the 1024 x 1024 skin atlas | Too many or too large pictures and fonts: use smaller pictures, fewer font sizes, or "charset": "ascii" for large display fonts. |
| glyph … is too large at … px | A font size is too large for some letters: use a smaller size or "charset": "ascii". |

Mistakes are never silently ignored: an unknown name or a typo is reported, so a skin works as written or not at all.

## Reference

### `skin.json` at a glance`{ "format": 1, "name": "Ember", "author": "Your Name", "version": "1.0", "description": "One line for the picker.", "cover_shape": "rounded", "palette": { "bg": "#1B1410", "text": "#FFF4E6", "accent": "#FF9F43" }, "colors": { "ember": "#FF6A1A" }, "fonts": { "title": { "file": "fonts/MyFont-Bold.ttf", "size": 24 } }, "images": { "highlight": "images/highlight.png" }, "parts": { "titlebar": [ … ] }, "screens": { "now_playing": [ … ], "list": [ … ] } }`

Only `format` (always `1`) and `name` are required. File paths are relative to the skin's folder, use `/`, and must stay inside the folder.

### Palette``````````````````````````````````````````````````

| Name | Used for | Reborn's own |
| --- | --- | --- |
| bg | the background (always opaque) | #06070A |
| text | main text | #F6F6F8 |
| muted | secondary text | #A0A4AE |
| dim | hints, disabled rows | #848894 |
| accent | highlights; "cover" follows the playing cover | cover |
| glass | translucent raised areas | #FFFFFF |
| scrim | dimming behind menus that slide up | #000000 |
| sheet | surfaces of menus and questions | #0E1014 |
| track | the empty part of bars and rings | #1E2023 |
| danger, success, warning | red, green and yellow states | #FF7864, #3CC878, #FFBE3C |

`text` on `bg` needs a contrast of at least 3:1; below 4.5:1, and for `muted` or `dim` below 3:1, you get a warning.

### Colours

Wherever an element asks for a colour, write `#RRGGBB`, `#RRGGBBAA` (with transparency), a palette name, or a name you defined under `colors`. Add `/` and a percentage for transparency: `"accent/40"`, `"#000000/30"`. The palette and `colors` themselves take only `#RRGGBB` or `#RRGGBBAA` (and `"cover"` for `accent`), and a name in `colors` cannot be a palette name.

### Fonts

Your fonts: `"name": { "file": "fonts/….ttf", "size": 17 }` (TrueType or OpenType, size 8 to 72 pixels, at most 8 fonts of 8 MB each). Each covers Latin letters with accents; characters a font lacks (Chinese, Japanese, Korean, emoji) come from Reborn's font. `"charset": "ascii"` keeps only plain ASCII, which saves room for very large sizes.

Reborn's fonts, usable by name in any skin:````````````````````````````

| Weight | Names |
| --- | --- |
| Regular | R11R13R15R17 |
| Light | L23L44 |
| Semibold | S10S13S15S17S20S25S28S36 |

### Pictures

PNG, JPEG or WebP, at most 480 × 360 pixels each and 64 in all. They can be drawn at any size; `slice` (in the `image` element) keeps the edges at their size. All pictures and font letters share one 1024 × 1024 texture; a skin that does not fit is refused.

### Screens

The screen names `screens` can use. Each falls back as described in [How Reborn chooses what to draw](#how-reborn-chooses-what-to-draw).``````````````````````````````````````````````````[](#step-5-cover-flow-and-square-covers)````````````````````````````````````````````````````````````````````````````````````

| Name | Shown for |
| --- | --- |
| home | the main menu (else list) |
| now_playing | Now Playing |
| list | every list without its own layout |
| page | pages with a heading or facts (About, Storage, Song Info…) |
| music, artists, albums, genres, songs, folders, album, artist, queue | Music and its library screens; queue is Up Next |
| audiobooks, book | Audiobooks and one book |
| playlists, playlist, search | Playlists, one playlist, Search |
| radio, radio_stations, radio_categories, radio_info | Radio, a station list, countries or genres, Station Info |
| cover_flow | Albums in Cover Flow (only this name): see step 5 |
| equalizer | the equalizer (only this name) |
| settings, wifi, bluetooth, sound, balance, playback, crossfade, output, headphone_level, dac_filter, display, theme, customize, home_menu, screen_off, library, computer | Settings and its pages; theme is the Skin picker |
| updates, time_zone, date_time, error_reports, maintenance, about, storage, battery, sleep, service, diagnostics, diagnostic, value, song_info | System pages and the service menu |
| sheet | menus and pickers that slide up over a screen |
| dialog | questions such as "Reset settings?" (else sheet) |
| toast | short messages at the top |
| volume | the volume indicator |
| keyboard | the keyboard (search, Wi-Fi password, playlist names): only this name; draw your title bar and {sheet_title} over a nativescreen element, which then draws the field and keys without a header |

### Elements

Every element has `"type"` and may have `"if"` ([conditions](#conditions)). `x` and `y` default to 0; inside a list row, a `group` or a `part` they count from that row's or group's corner.````````````````````````````````````````````````````````````````````````[](#icons)````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

| Type | Fields | What it draws |
| --- | --- | --- |
| rect | x y w h color · radius · stroke (1–3: outline only) | a rectangle |
| gradient | x y w h top bottom | a rectangle fading from the top colour to bottom |
| image | x y w h image · slice [left, top, right, bottom] · tint | a picture from images; tint multiplies a colour in (a white picture becomes exactly that colour) |
| text | x y w h text · font (default R15) · color (default text) · align (left, center, right) · lines (1–6) · line_height · tracking (letter spacing) · case (upper, lower) | text, cut with "…" when too long; one line is centred in h, several start at y when h is 0 |
| icon | x y size icon · color | one of the icons |
| bar | x y w h value · trackfill (colours) or track_imagefill_image (+ slice) · radius · vertical · knob (colour) knob_radius | a bar for valueprogress, volume, battery or brightness |
| art | x y size (at most 360) · source (current: the cover playing, a station's logo; row: inside list rows) · radius | a cover |
| list | x y w rows row_height row · focused · source (rows, facts, sheet) · scrollbar {x, w, track, thumb} | the screen's list: rows its rows, facts a page's label and value pairs, sheet the choices of a menu or question |
| group | elements · x y | its elements, moved by x y |
| part | name · x y | a part from parts, moved by x y |
| native | part (screen: Reborn's drawing of this screen; status: Reborn's battery and radio icons) · x y · recolor (default true: in your palette) · captions (Cover Flow; false: you write them) | Reborn's own drawing |
| indicators | x y (right edge, top) · size (16) · gap (4) · color (text) · charge (success) | the status icons: charging, a computer (accent while copying), Bluetooth and Wi-Fi while connected |

### Text values

Write these in curly braces inside `text`, for example `"{artist} · {album}"`.``````````````````````````````````````````````````````````````````````````````````````````````````````````````````

| Value | Shows |
| --- | --- |
| titleartistalbumalbum_artistgenretrack_number | the song playing; for a radio station, the song it announces |
| station | the radio station playing (empty for a song) |
| elapsedremainingduration | 1:23, -2:05, 3:28 |
| queue_indexqueue_length | for "3 of 12" |
| quality | LOSSLESS · 96 kHz, MP3 · 44.1 kHz |
| bitrate | 320 kbps (empty when unknown) |
| output | Headphone Jack or the Bluetooth device |
| playback | Playing, Paused, Stopped |
| sleep | a sleep timer: Sleeps in 23 min, Sleeps after song; empty without one |
| screen | the screen's name (empty on Home) |
| position | where the selection is in the list: 25 of 100 |
| batteryvolume | numbers 0–100 |
| clockdate | 21:41 or 9:41 PM; Sat 31 Oct; empty until the player knows the time |
| flow_titleflow_artistflow_detail | Cover Flow's centre album: its name, artist, songs and length |
| status | a page's status line (Wi-Fi, Bluetooth, pickers) |
| page_titlepage_body | a page's heading and explanation |
| empty_titleempty_bodyempty_action | what an empty list says |
| message | a toast's text |
| sheet_titlesheet_body | a menu's or question's heading and text |
| skin | your skin's name |
| inside list rows: labeldetailnumbercounttrack_number | the row's text, its value, its position, the list's length, the row's song's track number |

### Conditions

`"if"` takes names joined with `&` (and), `|` (or) and `!` (not): `"playing & !shuffle"`. `&` binds before `|`, so `"a | b & c"` means a, or both b and c. There are no brackets: write `"a & c | b & c"` for "a or b, and c".````````````````````````````````````````````````````````````````````````````````````````````

| Where | Names |
| --- | --- |
| Playback | playingpausedhas_trackhas_artlive (a radio station plays) favorite (the song is in Favorites) shuffleshuffle_albumsrepeatrepeat_oneeqgaplesscrossfadenormalisesleep |
| Player | chargingbattery_lowbluetoothbluetooth_connectedwifiwifi_connectedhas_clock |
| Screen | back (not Home) empty (an empty list) has_statushas_titlehas_bodyhas_actionhas_factsinteractiveerror (an error toast) danger (a question that deletes or resets) |
| Inside list rows | focuseddisabledtoggleoncheckcheckedchevronhas_detailrow_artnumberedcurrent (the song playing) firstlastodd |

### Icons

`back``chevron``check``close``play``pause``prev``next``play_large``pause_large``prev_large``next_large``shuffle``repeat``repeat_one``gapless``eq``normalise``moon``bluetooth``wifi``lock``bolt``folder``note``speaker``headphones``sd``usb``warning``info``sun``drive``power``download``refresh``search``vinyl``person``crossfade``heart``palette`, and three that follow the player's state: `play_pause`, `play_pause_large` (pause while playing, else play) and `repeat_mode` (repeat or repeat one).

### Limits

`skin.json` up to 256 KB · 64 pictures of at most 480 × 360 · 8 fonts of at most 8 MB · 4000 elements · one 1024 × 1024 texture for all pictures and letters.

### The shipped skins

Reborn ships 17 skins in [`skins/`](https://github.com/SchulzCode/Y2Reborn/tree/main/skins): Classic, Nano Glass, Walkman, Terminal, Winamp, Paper, Big Type, Cassette, Neon Night, Zune, Bunny Bow, Mini Silver, Pink, Blue, Green and Gold, and Luna XP (contributed by eNKay). Each is a complete example to read and copy. Classic's pictures are made by `tools/assets/build_classic_skin.py` and most others by `tools/assets/build_skins.py`; Luna XP is written by hand.

For developers with SSH access to a player: `rebornctl theme` lists the installed skins with their problems, and `rebornctl theme Ember` (or `theme reborn`) switches.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
