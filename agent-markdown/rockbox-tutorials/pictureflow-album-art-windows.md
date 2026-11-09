---
title: "Add album art for Rockbox PictureFlow with Mp3tag on Windows"
description: "Make PictureFlow on your Innioasis Y1 show every album cover: add the art with Mp3tag on Windows, copy the music across, then let Rockbox build its database and PictureFlow cache."
language: "en"
source: "https://innioasis.app/rockbox-tutorials/pictureflow-album-art-windows.html"
---

# Add album art for Rockbox PictureFlow with Mp3tag on Windows

[← Rockbox tutorials](index.html)

Rockbox-Y1 · PictureFlow · Windows

# Add album art for Rockbox PictureFlow with Mp3tag on Windows

Make PictureFlow on your Innioasis Y1 show every album cover: add the art with Mp3tag on Windows, copy the music across, then let Rockbox build its database and PictureFlow cache.

Using another computer? [macOS](pictureflow-album-art-macos.html) · Windows · [Linux](pictureflow-album-art-linux.html)

## Get the art right first
  - Use a square JPEG. Rockbox doesn't show progressive JPEGs; if a cover stays blank, re-save it as a standard JPEG.
  - Big images aren't sharper on a 480×360 screen; they just make the cache slower to build. 500×500 is plenty.
  - One cover per album: PictureFlow groups by the album tag, so tracks with matching album and artist tags stay together.

## Add the covers with Mp3tag
  - Install Mp3tag for Windows from [mp3tag.de](https://www.mp3tag.de/en/).
  - Choose File → Change Directory and open one album's folder.
  - Select every track of that album (Ctrl+A).
  - In the Tag Panel on the left, right-click the cover box and choose Add cover, then pick the image. Dragging the image onto the box works too.
  - Save with Ctrl+S. The cover is now inside every selected file.

## Put them on the Y1
  - Start Rockbox on the Y1 once before you begin. Rockbox makes its `.rockbox` folder on the first start.
  - Plug the Y1 into your computer with a USB data cable. When the player asks, choose USB Storage Mode. It shows up in File Explorer under This PC as a new drive.
  - Copy your albums to the player in File Explorer.
  - Right-click the Y1's drive in File Explorer, choose Eject, then unplug.
  - On the Y1, open Settings → General Settings → Database and choose Initialize Now.
  - Open Plugins → Demos → PictureFlow. The first start builds its cover cache, which takes a while with a big library.

## Frequently asked questionsNew albums don't show up in PictureFlow.

Update the database again, then rebuild PictureFlow's cache from its own settings menu.Some covers are blank.

Check the image is a standard (baseline) JPEG and that every track of the album carries the same album tag.

## More Rockbox tutorials

### [Install 360p themes by hand](install-rockbox-y1-themes-windows.html)

Windows

### [Find the hidden .rockbox folder](show-hidden-rockbox-folder-windows.html)

Windows

### [Rockbox-Y1 themes](../rockbox-y1-themes.html)

### [Rockbox-Y1 hub](../rockbox-y1/)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
