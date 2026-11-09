---
title: "Add album art for Rockbox PictureFlow with Mp3tag on macOS"
description: "Make PictureFlow on your Innioasis Y1 show every album cover: add the art with Mp3tag on macOS, copy the music across, then let Rockbox build its database and PictureFlow cache."
language: "en"
source: "https://innioasis.app/rockbox-tutorials/pictureflow-album-art-macos.html"
---

# Add album art for Rockbox PictureFlow with Mp3tag on macOS

[← Rockbox tutorials](index.html)

Rockbox-Y1 · PictureFlow · macOS

# Add album art for Rockbox PictureFlow with Mp3tag on macOS

Make PictureFlow on your Innioasis Y1 show every album cover: add the art with Mp3tag on macOS, copy the music across, then let Rockbox build its database and PictureFlow cache.

Using another computer? macOS · [Windows](pictureflow-album-art-windows.html) · [Linux](pictureflow-album-art-linux.html)

## Get the art right first
  - Use a square JPEG. Rockbox doesn't show progressive JPEGs; if a cover stays blank, re-save it as a standard JPEG.
  - Big images aren't sharper on a 480×360 screen; they just make the cache slower to build. 500×500 is plenty.
  - One cover per album: PictureFlow groups by the album tag, so tracks with matching album and artist tags stay together.

## Add the covers with Mp3tag
  - Get Mp3tag for Mac from the Mac App Store.
  - Drag one album's folder onto the Mp3tag window.
  - Select every track of that album (Cmd+A).
  - Drag the cover image onto the artwork box in the editor panel.
  - Save with Cmd+S. The cover is now inside every selected file.

## Put them on the Y1
  - Start Rockbox on the Y1 once before you begin. Rockbox makes its `.rockbox` folder on the first start.
  - Plug the Y1 into your computer with a USB data cable. When the player asks, choose USB Storage Mode. It shows up in the Finder sidebar under Locations.
  - Copy your albums to the player in Finder.
  - Click the eject button next to the Y1 in the Finder sidebar, wait for it to disappear, then unplug.
  - On the Y1, open Settings → General Settings → Database and choose Initialize Now.
  - Open Plugins → Demos → PictureFlow. The first start builds its cover cache, which takes a while with a big library.

## Frequently asked questionsNew albums don't show up in PictureFlow.

Update the database again, then rebuild PictureFlow's cache from its own settings menu.Some covers are blank.

Check the image is a standard (baseline) JPEG and that every track of the album carries the same album tag.

## More Rockbox tutorials

### [Install 360p themes by hand](install-rockbox-y1-themes-macos.html)

macOS

### [Find the hidden .rockbox folder](show-hidden-rockbox-folder-macos.html)

macOS

### [Rockbox-Y1 themes](../rockbox-y1-themes.html)

### [Rockbox-Y1 hub](../rockbox-y1/)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
