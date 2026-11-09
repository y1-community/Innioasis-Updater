---
title: "Find the hidden .rockbox folder on your Y1 from Linux"
description: "Rockbox keeps themes, fonts and settings in a hidden .rockbox folder. Here&#x27;s how to connect your Innioasis Y1 in USB Storage Mode and show that folder in your file manager on Linux."
language: "en"
source: "https://innioasis.app/rockbox-tutorials/show-hidden-rockbox-folder-linux.html"
---

# Find the hidden .rockbox folder on your Y1 from Linux

[← Rockbox tutorials](index.html)

Rockbox-Y1 · Linux

# Find the hidden .rockbox folder on your Y1 from Linux

Rockbox keeps themes, fonts and settings in a hidden .rockbox folder. Here's how to connect your Innioasis Y1 in USB Storage Mode and show that folder in your file manager on Linux.

Using another computer? [macOS](show-hidden-rockbox-folder-macos.html) · [Windows](show-hidden-rockbox-folder-windows.html) · Linux

## Show .rockbox, step by step
  - Start Rockbox on the Y1 once before you begin. Rockbox makes its `.rockbox` folder on the first start.
  - Plug the Y1 into your computer with a USB data cable. When the player asks, choose USB Storage Mode. It mounts like any USB drive, usually under `/media/<you>/` or `/run/media/<you>/`.
  - Open the Y1's drive in your file manager.
  - Press Ctrl+H to show hidden files in GNOME Files (Nautilus), Nemo and Thunar. In KDE Dolphin it's Alt+. or Ctrl+H.
  - Open `.rockbox`. In a terminal, `ls -a` lists it too.

## What's inside
  - `themes`: the small `.cfg` file that names each theme.
  - `wps`, `backdrops`, `icons`, `fonts`: the parts a theme is made of.
  - Your settings, playlists and the music database also live here, so copy into it rather than replacing it.

If the drive doesn't mount on its own, open your file manager and click it in the sidebar. It mounts on first click.

## When you're done

Click the eject icon next to the Y1 in your file manager, wait for it to finish, then unplug.

## Frequently asked questionsI can't see .rockbox at all, even with hidden items on.

Start Rockbox on the Y1 once, then connect again. The folder only exists after Rockbox has started.Can I delete .rockbox?

Yes, if you want a clean start. Rockbox makes a new one with default settings on the next start, and the Rockbox-Y1 0.5 release notes suggest it as a fix for odd path problems. Your themes and settings go with it.

## More Rockbox tutorials

### [Install 360p themes by hand](install-rockbox-y1-themes-linux.html)

Linux

### [Album art for PictureFlow](pictureflow-album-art-linux.html)

Linux

### [Rockbox-Y1 themes](../rockbox-y1-themes.html)

### [Rockbox-Y1 hub](../rockbox-y1/)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
