---
title: "Y2Player skin engine, version 2 - Innioasis Updater"
description: "Y2Player skin engine, version 2 Version 2 extends the declarative renderer for visual theme editors. Set formatVersion to 2 to use the new properties. Neon Grid, Pixel Ga"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2player-docs-skins-format_v2.html"
---

# Y2Player skin engine, version 2 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=y2player-y2)

Post-install setup · Y2Player · Y2

# Y2Player skin engine, version 2

A Y2 custom Software.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=y2player-y2)[Install guide](../guide.html?model=Y2&software=y2player-y2)

# Y2Player skin engine, version 2

Version 2 extends the declarative renderer for visual theme editors. Set `formatVersion` to `2` to use the new properties. Neon Grid, Pixel Garden, and Studio Deck are bundled version 2 showcases; version 1 community skins remain supported with their original behavior. Older players reject version 2 with a version error; reload failures retain the Classic fallback. Themes never execute scripts.

The structural contract is [skin-v2.schema.json](https://github.com/schulzcode/Y2Player/blob/HEAD/docs/skins/skin-v2.schema.json). Semantic validation in `SkinParser` additionally checks component references, parameters, color names, bindings, focus IDs, file paths, and expansion limits. The schema allows parameter placeholders in templates; the parser validates their resolved values before a skin is published. See [example-v2/skin.json](https://github.com/schulzcode/Y2Player/blob/HEAD/docs/skins/example-v2/skin.json) for an installable example. It is a development example, not another bundled skin.

## Styles and components

`styles` maps names to shared visual/text properties. A node's `style` selects one; explicit node properties override it. Supported style properties: `color`, `background`, `opacity`, `borderColor`, `borderWidth`, `radius`, `size`, `bold`, `font`, `lineSpacing`, `overflow`, `verticalAlign`. Styles do not inherit other styles. Palette references continue to use `colors`.

Components can remain arrays or become objects with `parameters` and `nodes`:`{ "parameters": {"label":"Play", "width":100}, "nodes": [ {"type":"text", "bounds":[0,0,"{param.width}",40], "text":"{param.label}"} ] }`

Supply `props` on a component instance to override defaults. Parameters are strings, numbers, or booleans; overrides must have the same scalar type. A whole `{param.name}` token preserves its type; tokens embedded in strings interpolate. Resolved values still undergo normal action/color/path/binding validation. Defaults are required, unknown parameters are rejected, and each instance is compiled independently. Use parameterized focus IDs when repeating components. A component instance becomes a group; its children use local coordinates. Use `anchor: "stretch"` or a layout container for content that should resize.

## Drawing and text``````````````````````````````````````````````

| Property | Values and behavior |
| --- | --- |
| font | Per-element system family or relative font file; omitted inherits the skin font |
| lineSpacing | Font-spacing multiplier, 0.5–3; default 1 |
| verticalAlign | top, center (default), bottom |
| overflow | ellipsis (default), clip, marquee |
| marqueeSpeed | 8–80 logical units/second; default 24 |
| imageFit | stretch (legacy default), fit (contain), crop (cover) |
| imageX, imageY | Image alignment from 0 to 1; default 0.5 |
| opacity | 0–1, including descendants of groups |
| radius | Rounded rectangle or image clipping radius |
| borderColor, borderWidth | Independent outline, up to 16 units |
| gradient | { "endColor":"accent", "direction":"vertical" }; horizontal also supported |

Version 2 text honors explicit newlines. Wrapping uses font measurements, whole Unicode code points, and word boundaries. Marquee is a single-line, back-and-forth scroll with one-second pauses at the ends. Its clock resets on screen changes; hidden screens do not schedule animation. `clip` clips overflow without an ellipsis. Fonts load during reload, not during drawing.

New primitives:
  - `circle`: ellipse inscribed in bounds; equal width/height produces a circle.
  - `line`: from top-left to bottom-right; use a path for other directions.
  - `path`: restricted vector polyline/polygon using 2–128 normalized `[x,y]`

points, each coordinate between 0 and 1. `closed` joins the endpoints. Open paths are stroked; closed paths are filled unless `stroke` is positive.

Gradients fill primitives/text; they do not tint artwork or images. Borders are rectangular/rounded except for circles. Image fit/crop is clipped to the node bounds. Touch targets use the clipped bounding rectangle.

## Layout

Groups and component instances accept `layout`:
  - `absolute` (default): each child's local bounds and anchor determine placement.
  - `row` / `column`: children retain their specified main-axis size. Positive

`weight` values divide remaining space proportionally; the cross-axis fills the container. This provides automatic sizing without measuring content.
  - `grid`: equal cells with the specified `columns`; row count follows children.
  - `stack`: every child fills the inner rectangle in drawing order.

`padding` is a uniform inset and `gap` is spacing between cells. In absolute layout, `anchor` accepts `topLeft`, `topRight`, `bottomLeft`, `bottomRight`, `center`, or `stretch`. Corner offsets are margins from that corner. Center uses x/y as offsets. Stretch uses x/y as symmetric insets; width/height are ignored. Anchors are evaluated against the current parent, including resized row cells. Top-level anchors use the skin viewport. Oversized content clips; containers do not scroll unless they are row repeaters.

## Lists and keyboards

`rows` accepts `listMode`:
  - `grid`: existing row-major grid with `columns` and `rowHeight`.
  - `horizontal`: one horizontal strip of `rowWidth` × `rowHeight` cells.
  - `carousel`: horizontal strip whose visible window follows selection, centered

when possible; end pages can have empty slots.
  - `radial`: `columns` evenly spaced cells around an ellipse, clockwise from the

top; `rowWidth`/`rowHeight` determine each cell's size. Up to eight slots.

`scrolling` is `page` (default), `follow` (keep selection at the end once past capacity), or `center`. Carousel always uses center behavior. These are discrete selection-driven windows, not animated free-scrolling. The same cell geometry is used for drawing and hit testing; overlapping cells use last-drawn priority.

`keyboard.keyStyle` controls `gap`, `radius`, `color`, `background`, `focusColor`, `focusBackground`, `borderColor`, and `borderWidth`. Font, bold, and size come from the keyboard node. Key labels and wheel behavior remain owned by SearchKeyboard. Search retains its native keyboard/results navigation.

## Visual states and motion

`states` maps state names to overrides of `color`, `background`, `opacity`, `borderColor`, `borderWidth`, `radius`, `size`, and `bold`. Applicable states are applied in this order: `normal`, `paused`/`playing`, `active`, `focused`, `pressed`, `disabled`. Later properties win. State overrides do not alter action or geometry. `disabled: true` blocks a node and all descendant controls. Unavailable rows get disabled styling but retain row selection behavior so the player can explain availability. New visibility conditions are `pressed`, `disabled`, `enabled`, and `charging`.

`transitionMs` (0–500, default 0) interpolates colors, opacity, radius, and border width between visual states. Text size and weight switch immediately. Motion is limited to 30 redraws/second, stops when the view is hidden/detached, and retains at most one transition per visible node. No general animation timeline or scripts are supported.

## Controls, focus, and seeking

Add an entry to top-level `navigation` to opt a screen into custom wheel focus:`"navigation": {"now_playing":{"initial":"play", "wrap":true}}`

Focusable nodes provide an action (or are row containers) and:`"focus": {"id":"play", "group":"transport", "order":1, "previous":"previous", "next":"next"}`

IDs are unique per screen. Groups sort by name and items by order, preserving source order for ties. Optional previous/next references override wheel order. Disabled, hidden, or fully clipped controls are excluded. `nextGroup` and `previousGroup` actions move to the adjacent group. Confirm activates the focused action. A focused row container enters row navigation on Confirm; Back leaves that mode before leaving the screen. Back otherwise keeps the normal reducer behavior, including dismissing messages. Search cannot opt in.

Screens without navigation entries keep all existing wheel behavior. Explicit Now Playing navigation uses the wheel for focus; add `volumeUp`/`volumeDown` controls there. Physical transport and volume shortcuts remain available. Navigation under `default` applies only to screens using the default layout.

Additional actions: `volumeUp`, `volumeDown`, `shuffle`, `repeat`. They dispatch validated reducer commands and are blocked in Search/FM. Existing actions remain supported. `progress.seekable: true` seeks on tap release; horizontal progress goes left-to-right, vertical bottom-to-top, and circular clockwise from twelve o'clock. Seek fractions are clamped and ignored without a track or duration, or on Search/FM. No intermediate drag seeks are emitted.

## Additional bindings````````````````````````````````````

| Binding | Value |
| --- | --- |
| volume | Effective system or perceptual volume percentage; -- when unavailable |
| volume.mode | Volume mode enum name |
| shuffle, repeat | ON/OFF, repeat mode enum name |
| track.codec | Track metadata codec |
| track.sampleRate, track.bitDepth, track.channels, track.bitrate | Metadata numbers, empty if unknown; Hz, bits, channels, bits/sec |
| device.charging, device.storageAvailable | true or false |
| device.model | Reported device model |
| display.brightness | Brightness percentage |

These describe track metadata, not an assertion about the actual DAC output. System volume is cached for one second by the view and refreshed when drawing.

## Bounds, compatibility, and checks

Manifest limit remains 256 KiB. JSON nesting is capped at 64 before parsing. Version 1 retains its 512-node source limit. Version 2 compilation has a global 4096-node budget, including validation of unused templates, and each expanded screen remains limited to 4096 nodes including repeated cells. Nested repeaters are rejected even when the outer repeater has capacity one. Source child nesting is capped at 12; component graphs must be acyclic. At most 16 font faces are loaded per skin; external font files retain the 2 MiB limit. Existing image and asset-path limits still apply.

Run from the repository root:`ANDROID_SDK_ROOT=/opt/android-sdk ./gradlew testDebugUnitTest lintDebug assembleRelease node tools/skin-preview/check.mjs`

[preview-fixtures.json](https://github.com/schulzcode/Y2Player/blob/HEAD/docs/skins/preview-fixtures.json) is consumed by Kotlin tests and the dependency-free browser module. It covers geometry, image fitting, seeking, and text wrapping with a deterministic measurement adapter. Real browser/Android font rasterization is not guaranteed identical: the editor must supply the same fonts and compare device captures for font-metric differences. This module is preview infrastructure, not the web editor UI.

The debug-only `SkinPreviewService` renders synthetic state on Android and checks navigation/touch without dispatching to playback. Instructions are in [the preview tools README](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2FY2Player%2Fblob%2FHEAD%2Ftools%2Fskin-preview%2FREADME.md).

These are Y2Player's own instructions, shown here word for word.

Published by the [schulzcode/Y2Player](https://innioasis.app/firmware.html?model=Y2&software=y2player-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2FY2Player&software=y2player-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
