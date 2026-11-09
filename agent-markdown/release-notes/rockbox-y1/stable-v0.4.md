---
title: "Rockbox-Y1 v0.4 - Innioasis Updater"
description: "New Features: - Extend lastfm scrobbler plugin to upload directly to Last.fm + ListenBrainz https://github.com/rockbox-y1/rockbox/blob/y1/INTERNET.md scrobbling-lastfm-listenbrainz"
language: "en"
source: "https://innioasis.app/release-notes/rockbox-y1/stable-v0.4.html"
---

# Rockbox-Y1 v0.4 - Innioasis Updater

[← Firmware Downloads](../../firmware.html?model=Y1&software=rockbox-y1)

Firmware release notes · Rockbox-Y1 · Y1

# Rockbox-Y1 v0.4

A music-first custom Software with deep playback and theme options.stable-v0.4Y12026-03-24[rockbox-y1/rockbox](https://innioasis.app/firmware.html?model=Y1&software=rockbox-y1)[Get it in Updater CE](../../guide.html?model=Y1&software=rockbox-y1)[Firmware Downloads](../../firmware.html?model=Y1&software=rockbox-y1)Rockbox Compatibility Warning

This Rockbox-Y1 release predates 0.5. It is not compatible with Y1 units sold after March 2026 with Innioasis OS 3.0.7 pre-installed; flashing it on those devices will prevent booting.

## Download this release

Portable packages include the flashing tool for your computer; the file is saved under the release's own name.

rom_240p.zip[rom_240p.zip 439 MB](https://github.com/rockbox-y1/rockbox/releases/download/stable-v0.4/rom_240p.zip)[macOSportable · 553 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.4/rom_240p-macos.zip)[Windowsportable · 636 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.4/rom_240p-windows.zip)[Linuxportable · 809 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.4/rom_240p-linux.zip)

rom_240p_type_b.zip[rom_240p_type_b.zip 406 MB](https://github.com/rockbox-y1/rockbox/releases/download/stable-v0.4/rom_240p_type_b.zip)[macOSportable · 520 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.4/rom_240p_type_b-macos.zip)[Windowsportable · 602 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.4/rom_240p_type_b-windows.zip)[Linuxportable · 775 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.4/rom_240p_type_b-linux.zip)

rom_360p.zip[rom_360p.zip 441 MB](https://github.com/rockbox-y1/rockbox/releases/download/stable-v0.4/rom_360p.zip)[macOSportable · 555 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.4/rom_360p-macos.zip)[Windowsportable · 637 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.4/rom_360p-windows.zip)[Linuxportable · 810 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.4/rom_360p-linux.zip)

rom_360p_type_b.zip[rom_360p_type_b.zip 408 MB](https://github.com/rockbox-y1/rockbox/releases/download/stable-v0.4/rom_360p_type_b.zip)[macOSportable · 522 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.4/rom_360p_type_b-macos.zip)[Windowsportable · 604 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.4/rom_360p_type_b-windows.zip)[Linuxportable · 777 MB](https://github.com/y1-community/rockbox-mirror/releases/download/stable-v0.4/rom_360p_type_b-linux.zip)

update_240p.zip[update_240p.zip 87 MB](https://github.com/rockbox-y1/rockbox/releases/download/stable-v0.4/update_240p.zip)

update_360p.zip[update_360p.zip 88 MB](https://github.com/rockbox-y1/rockbox/releases/download/stable-v0.4/update_360p.zip)

voices.zip[voices.zip 73 MB](https://github.com/rockbox-y1/rockbox/releases/download/stable-v0.4/voices.zip)

New Features:
  - Extend lastfm_scrobbler plugin to [upload directly to Last.fm + ListenBrainz](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Frockbox-y1%2Frockbox%2Fblob%2Fy1%2FINTERNET.md%23scrobbling-lastfm-listenbrainz-maloja&anchor=scrobbling-lastfm-listenbrainz-maloja)
  - [Podcast downloader plugin](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Frockbox-y1%2Frockbox%2Fblob%2Fy1%2FINTERNET.md%23podcasts&anchor=podcasts)
  - Software Keyboard ([LeanKeyboard](https://github.com/yuliskov/LeanKeyboard))
  - Implement stereo balance
  - Increase available memory to 256MB 
  - Podcast Downloader optimizations
  - Remappings for FM Radio App
  - Rudimentary remaining battery time estimation
  - Use iPod Classic button mappings (mostly)
  - Feature to shutdown device with a 5s press of the center button 
  - Function to reset bluetooth devices
  - Information for Taptic Engine mods
  - Update functionality
  - Enable most plugins
  - Enable regular db updates and autoupdate

Bug Fixes:
  - A-B repeat
  - Idle shutdown/sleep timer when no music is playing
  - Keylock feature + advanced keylock
  - License viewer
  - runtimedb and autoresume
  - Battery optimization: only use wake lock when needed for sleep timers
  - Enable brightness settings for compatibility with existing themes + quickscreen

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

Published by the [rockbox-y1/rockbox](https://innioasis.app/firmware.html?model=Y1&software=rockbox-y1) project [[1]](https://innioasis.app/firmware_info.html?repo=rockbox-y1%2Frockbox&software=rockbox-y1)[[2]](https://innioasis.app/release_notes.html?author=rockbox-y1&project=rockbox&version=stable-v0.4&software=rockbox-y1)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Arockbox-y1)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
