---
title: "Rockbox-Y1 v0.5 - Innioasis Updater"
description: "As a preparation for eventually submitting this port to the upstream Rockbox project a lot had to change under the hood. For now this means the removal of very specific and rarely"
language: "en"
source: "https://innioasis.app/release-notes/rockbox-y1/stable-v0.5.html"
---

# Rockbox-Y1 v0.5 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y1&software=rockbox-y1)

Firmware release notes · Rockbox-Y1 · Y1

# Rockbox-Y1 v0.5

A music-first custom Software with deep playback and theme options.stable-v0.5Y12026-05-16[rockbox-y1/rockbox](https://innioasis.app/firmware.html?model=Y1&software=rockbox-y1)[Get it in Updater CE](../../guide.html?model=Y1&software=rockbox-y1)[Firmware Downloads](../../firmware.html?model=Y1&software=rockbox-y1)

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

rom.zip[rom.zip 510 MB](https://github.com/rockbox-y1/rockbox/releases/download/stable-v0.5/rom.zip)[macOSportable · 624 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.5/rom-macos.zip)[Windowsportable · 706 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.5/rom-windows.zip)[Linuxportable · 879 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.5/rom-linux.zip)

rom_type_b.zip[rom_type_b.zip 422 MB](https://github.com/rockbox-y1/rockbox/releases/download/stable-v0.5/rom_type_b.zip)[macOSportable · 536 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.5/rom_type_b-macos.zip)[Windowsportable · 618 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.5/rom_type_b-windows.zip)[Linuxportable · 791 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.5/rom_type_b-linux.zip)

update.zip[update.zip 94 MB](https://github.com/rockbox-y1/rockbox/releases/download/stable-v0.5/update.zip)

As a preparation for eventually submitting this port to the upstream Rockbox project a lot had to change under the hood.

For now this means the removal of very specific and rarely used features like the Apps menu. It also means simpler merges of new upstream features. 360p only, there won't be any future 240p releases.

If you have issues, try these steps:
  - Full flash of the new ROM.
  - Delete `.rockbox` on your SD card, this should fix any weird path issues you might encounter (especially shortcuts)
  - Themes have been updated, see here: [https://github.com/rockbox-y1/themes/releases/tag/for_the_gays_and_the_theys](https://innioasis.app/rockbox-y1-themes.html)
  - If you want to use any custom themes that worked for older Rockbox-Y1 versions, you will need to change paths in the theme files from `/.rockbox` to `/sdcard/.rockbox`
  - Install font pack: [https://download.rockbox.org/release/4.0/rockbox-fonts-4.0.zip](https://download.rockbox.org/release/4.0/rockbox-fonts-4.0.zip)

New:
  - Discontinuation of the 240p versions
  - Updated stock app
  - Support for devices that came with stock firmware 3.0.7
  - Black screen bug mitigations
  - Fixes plugins as start screen
  - Fixes audio not pausing on BT disconnect
  - Minor fixes (scrobble upload)

## Also useful
  - [Install guideStep-by-step install for Rockbox-Y1](../../guides/rockbox-y1.html)
  - [Rockbox-Y1 v0.6stable-v0.6 · 2026-10-29](../../release-notes/rockbox-y1/stable-v0.6.html)
  - [Rockbox-Y1 Nightly-25-10-2026nightly-9c92b93a5d582b3819a119162a14ad0b4178d2cd · 2026-10-25](../../release-notes/rockbox-y1/nightly-9c92b93a5d582b3819a119162a14ad0b4178d2cd.html)
  - [Rockbox-Y1 Nightly-23-10-2026nightly-11d9072b8ae950dfe76b8d867f67ff1a048a8c24 · 2026-10-23](../../release-notes/rockbox-y1/nightly-11d9072b8ae950dfe76b8d867f67ff1a048a8c24.html)
  - [Rockbox-Y1 Nightly-18-10-2026nightly-9733397325a7c3239cac067d86ca7682b11136b2 · 2026-10-18](../../release-notes/rockbox-y1/nightly-9733397325a7c3239cac067d86ca7682b11136b2.html)
  - [Rockbox-Y1 Nightly-05-10-2026nightly-e879e4813d025c07d66dd89e17065fdedd3ba5c5 · 2026-10-05](../../release-notes/rockbox-y1/nightly-e879e4813d025c07d66dd89e17065fdedd3ba5c5.html)
  - [Rockbox-Y1 Nightly-24-09-2026nightly-107480ccb359ec26a8f9d161d4e86efd3d6b1144 · 2026-09-24](../../release-notes/rockbox-y1/nightly-107480ccb359ec26a8f9d161d4e86efd3d6b1144.html)
  - [Rockbox-Y1 Nightly-09-09-2026nightly-e8b9dbab0ab4ab93c28dcb325fbcc032d07cf87b · 2026-09-09](../../release-notes/rockbox-y1/nightly-e8b9dbab0ab4ab93c28dcb325fbcc032d07cf87b.html)
  - [Rockbox-Y1 Nightly-24-08-2026nightly-f588b0f654632913a2bbb9f832e7ddf4571b7c40 · 2026-08-24](../../release-notes/rockbox-y1/nightly-f588b0f654632913a2bbb9f832e7ddf4571b7c40.html)

Notes as published by the Rockbox-Y1 project. Install it with Updater CE, or download it from the firmware directory.

Published by the [rockbox-y1/rockbox](https://innioasis.app/firmware.html?model=Y1&software=rockbox-y1) project [[1]](https://innioasis.app/firmware_info.html?repo=rockbox-y1%2Frockbox&software=rockbox-y1)[[2]](https://innioasis.app/release_notes.html?author=rockbox-y1&project=rockbox&version=stable-v0.5&software=rockbox-y1)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Arockbox-y1)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
