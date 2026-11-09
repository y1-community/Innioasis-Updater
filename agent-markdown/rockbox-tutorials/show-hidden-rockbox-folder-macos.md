---
title: "Find the hidden .rockbox folder on your Y1 from macOS"
description: "Rockbox keeps themes, fonts and settings in a hidden .rockbox folder. Here&#x27;s how to connect your Innioasis Y1 in USB Storage Mode and show that folder in Finder on macOS."
language: "en"
source: "https://innioasis.app/rockbox-tutorials/show-hidden-rockbox-folder-macos.html"
---

# Find the hidden .rockbox folder on your Y1 from macOS

[← Rockbox tutorials](index.html)

Rockbox-Y1 · macOS

# Find the hidden .rockbox folder on your Y1 from macOS

Rockbox keeps themes, fonts and settings in a hidden .rockbox folder. Here's how to connect your Innioasis Y1 in USB Storage Mode and show that folder in Finder on macOS.

Using another computer? macOS · [Windows](show-hidden-rockbox-folder-windows.html) · [Linux](show-hidden-rockbox-folder-linux.html)

## Show .rockbox, step by step
  - Start Rockbox on the Y1 once before you begin. Rockbox makes its `.rockbox` folder on the first start.
  - Plug the Y1 into your computer with a USB data cable. When the player asks, choose USB Storage Mode. It shows up in the Finder sidebar under Locations.
  - Open the Y1 in Finder.
  - Press Cmd+Shift+. (the full stop key). Hidden items appear dimmed, and `.rockbox` is one of them.
  - Open `.rockbox`. Press the same keys again later to hide hidden items.

## What's inside
  - `themes`: the small `.cfg` file that names each theme.
  - `wps`, `backdrops`, `icons`, `fonts`: the parts a theme is made of.
  - Your settings, playlists and the music database also live here, so copy into it rather than replacing it.

macOS leaves small files whose names start with `._` on the player. They're harmless, and Rockbox doesn't need them.

## When you're done

Click the eject button next to the Y1 in the Finder sidebar, wait for it to disappear, then unplug.

## Frequently asked questionsI can't see .rockbox at all, even with hidden items on.

Start Rockbox on the Y1 once, then connect again. The folder only exists after Rockbox has started.Can I delete .rockbox?

Yes, if you want a clean start. Rockbox makes a new one with default settings on the next start, and the Rockbox-Y1 0.5 release notes suggest it as a fix for odd path problems. Your themes and settings go with it.

## More Rockbox tutorials

### [Install 360p themes by hand](install-rockbox-y1-themes-macos.html)

macOS

### [Album art for PictureFlow](pictureflow-album-art-macos.html)

macOS

### [Rockbox-Y1 themes](../rockbox-y1-themes.html)

### [Rockbox-Y1 hub](../rockbox-y1/)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
