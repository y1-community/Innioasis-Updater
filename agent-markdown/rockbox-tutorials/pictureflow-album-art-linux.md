---
title: "Add album art for Rockbox PictureFlow on Linux"
description: "Make PictureFlow on your Innioasis Y1 show every album cover: add the art with a cover.jpg file on Linux, copy the music across, then let Rockbox build its database and PictureFlow cache."
language: "en"
source: "https://innioasis.app/rockbox-tutorials/pictureflow-album-art-linux.html"
---

# Add album art for Rockbox PictureFlow on Linux

[← Rockbox tutorials](index.html)

Rockbox-Y1 · PictureFlow · Linux

# Add album art for Rockbox PictureFlow on Linux

Make PictureFlow on your Innioasis Y1 show every album cover: add the art with a cover.jpg file on Linux, copy the music across, then let Rockbox build its database and PictureFlow cache.

Using another computer? [macOS](pictureflow-album-art-macos.html) · [Windows](pictureflow-album-art-windows.html) · Linux

## Get the art right first
  - Use a square JPEG. Rockbox doesn't show progressive JPEGs; if a cover stays blank, re-save it as a standard JPEG.
  - Big images aren't sharper on a 480×360 screen; they just make the cache slower to build. 500×500 is plenty.
  - One cover per album: PictureFlow groups by the album tag, so tracks with matching album and artist tags stay together.

## Add the covers with a cover.jpg file
  - Mp3tag has no Linux version, and you don't need one: Rockbox also reads a `cover.jpg` file in the album's folder.
  - Save the album's cover as `cover.jpg` in the same folder as its tracks.
  - Repeat for each album. A file manager or `cp` is all it takes.
  - Prefer art inside the files? Tag editors packaged for Linux, such as Kid3, can embed a cover too.

## Put them on the Y1
  - Start Rockbox on the Y1 once before you begin. Rockbox makes its `.rockbox` folder on the first start.
  - Plug the Y1 into your computer with a USB data cable. When the player asks, choose USB Storage Mode. It mounts like any USB drive, usually under `/media/<you>/` or `/run/media/<you>/`.
  - Copy your albums to the player in your file manager.
  - Click the eject icon next to the Y1 in your file manager, wait for it to finish, then unplug.
  - On the Y1, open Settings → General Settings → Database and choose Initialize Now.
  - Open Plugins → Demos → PictureFlow. The first start builds its cover cache, which takes a while with a big library.

## Frequently asked questionsNew albums don't show up in PictureFlow.

Update the database again, then rebuild PictureFlow's cache from its own settings menu.Some covers are blank.

Check the image is a standard (baseline) JPEG and that every track of the album carries the same album tag.

## More Rockbox tutorials

### [Install 360p themes by hand](install-rockbox-y1-themes-linux.html)

Linux

### [Find the hidden .rockbox folder](show-hidden-rockbox-folder-linux.html)

Linux

### [Rockbox-Y1 themes](../rockbox-y1-themes.html)

### [Rockbox-Y1 hub](../rockbox-y1/)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
