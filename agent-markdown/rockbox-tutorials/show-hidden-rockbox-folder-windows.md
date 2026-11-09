---
title: "Find the hidden .rockbox folder on your Y1 from Windows"
description: "Rockbox keeps themes, fonts and settings in a hidden .rockbox folder. Here&#x27;s how to connect your Innioasis Y1 in USB Storage Mode and show that folder in File Explorer on Windows."
language: "en"
source: "https://innioasis.app/rockbox-tutorials/show-hidden-rockbox-folder-windows.html"
---

# Find the hidden .rockbox folder on your Y1 from Windows

[← Rockbox tutorials](index.html)

Rockbox-Y1 · Windows

# Find the hidden .rockbox folder on your Y1 from Windows

Rockbox keeps themes, fonts and settings in a hidden .rockbox folder. Here's how to connect your Innioasis Y1 in USB Storage Mode and show that folder in File Explorer on Windows.

Using another computer? [macOS](show-hidden-rockbox-folder-macos.html) · Windows · [Linux](show-hidden-rockbox-folder-linux.html)

## Show .rockbox, step by step
  - Start Rockbox on the Y1 once before you begin. Rockbox makes its `.rockbox` folder on the first start.
  - Plug the Y1 into your computer with a USB data cable. When the player asks, choose USB Storage Mode. It shows up in File Explorer under This PC as a new drive.
  - Open the Y1's drive in File Explorer. Windows usually shows `.rockbox` straight away: a leading dot doesn't hide a folder on Windows.
  - Can't see it? On Windows 11 choose View → Show → Hidden items. On Windows 10 open the View tab and tick Hidden items.
  - Open `.rockbox`.

## What's inside
  - `themes`: the small `.cfg` file that names each theme.
  - `wps`, `backdrops`, `icons`, `fonts`: the parts a theme is made of.
  - Your settings, playlists and the music database also live here, so copy into it rather than replacing it.

## When you're done

Right-click the Y1's drive in File Explorer, choose Eject, then unplug.

## Frequently asked questionsI can't see .rockbox at all, even with hidden items on.

Start Rockbox on the Y1 once, then connect again. The folder only exists after Rockbox has started.Can I delete .rockbox?

Yes, if you want a clean start. Rockbox makes a new one with default settings on the next start, and the Rockbox-Y1 0.5 release notes suggest it as a fix for odd path problems. Your themes and settings go with it.

## More Rockbox tutorials

### [Install 360p themes by hand](install-rockbox-y1-themes-windows.html)

Windows

### [Album art for PictureFlow](pictureflow-album-art-windows.html)

Windows

### [Rockbox-Y1 themes](../rockbox-y1-themes.html)

### [Rockbox-Y1 hub](../rockbox-y1/)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
