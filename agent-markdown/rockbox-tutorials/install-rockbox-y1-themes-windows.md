---
title: "Install Rockbox-Y1 360p themes by hand on Windows"
description: "Copy the 360p Rockbox-Y1 themes onto an Innioasis Y1 from Windows: download the theme pack, unzip it, merge its .rockbox folder into the player&#x27;s, then pick a theme. Works on Rockbox-Y1 0.5 or later."
language: "en"
source: "https://innioasis.app/rockbox-tutorials/install-rockbox-y1-themes-windows.html"
---

# Install Rockbox-Y1 360p themes by hand on Windows

[← Rockbox tutorials](index.html)

Rockbox-Y1 · Windows

# Install Rockbox-Y1 360p themes by hand on Windows

Copy the 360p Rockbox-Y1 themes onto an Innioasis Y1 from Windows: download the theme pack, unzip it, merge its .rockbox folder into the player's, then pick a theme. Works on Rockbox-Y1 0.5 or later.

Using another computer? [macOS](install-rockbox-y1-themes-macos.html) · Windows · [Linux](install-rockbox-y1-themes-linux.html)

## Faster: let Updater CE do it

Updater CE 2.5 or later installs every 360p Rockbox-Y1 theme for you during a Rockbox-Y1 install. Already on Rockbox? Open Updater CE and choose Settings → Install Rockbox 360p Themes, or press Ctrl+T.[Get Updater CE](../guide.html)[All Rockbox-Y1 theme options](../rockbox-y1-themes.html)

## Before you start
  - Rockbox-Y1 0.5 or later on any Y1. These are 360p themes; 0.5 and later is 360p only.
  - A USB data cable. Charge-only cables don't show the player as a drive.
  - About 400 MB free on your computer for the theme pack and its unzipped copy.

## Download[Theme pack (360p)](/download-proxy?url=https%3A%2F%2Fgithub.com%2Frockbox-y1%2Fthemes%2Freleases%2Fdownload%2Ffor_the_gays_and_the_theys%2Fthemepack.zip&filename=rockbox-y1-360p-themepack.zip)[Individual themes (360p)](/download-proxy?url=https%3A%2F%2Fgithub.com%2Frockbox-y1%2Fthemes%2Freleases%2Fdownload%2Ffor_the_gays_and_the_theys%2Fthemes_individual.zip&filename=rockbox-y1-360p-themes-individual.zip)[Rockbox fonts 4.0](https://download.rockbox.org/release/4.0/rockbox-fonts-4.0.zip)

Text looks wrong or missing after picking a theme? Unzip the Rockbox fonts pack and merge its `.rockbox` folder in the same way.

## Install, step by step
  - Download the theme pack below. It holds every theme as one merged `.rockbox` folder. The individual themes download has each theme in its own folder, each with its own `.rockbox` inside.
  - Right-click the zip in File Explorer, choose Extract All, then Extract.
  - Start Rockbox on the Y1 once before you begin. Rockbox makes its `.rockbox` folder on the first start.
  - Plug the Y1 into your computer with a USB data cable. When the player asks, choose USB Storage Mode. It shows up in File Explorer under This PC as a new drive.
  - Show hidden items and open the Y1's `.rockbox` folder ([how to show it on Windows](show-hidden-rockbox-folder-windows.html)).
  - Open the theme's own `.rockbox` folder.
  - Select everything inside it (Ctrl+A) and copy it (Ctrl+C).
  - Open the Y1's `.rockbox` folder and paste (Ctrl+V). File Explorer merges folders with the same name on its own.
  - When it asks about files that already exist, choose Replace the files in the destination.
  - Right-click the Y1's drive in File Explorer, choose Eject, then unplug.
  - On the Y1, open Settings → Theme Settings → Browse Theme Files and pick a theme.

## On a Y2

The same 360p files can be copied by hand onto a Y2 running Rockbox-Y2: merge them into the `.rockbox` folder Rockbox-Y2 made on the player. Rockbox-Y2 is a separate port, so read the release notes for your version first. Updater CE's automatic theme install is for Rockbox-Y1.[Rockbox-Y2 hub](../rockbox-y2/)

## Frequently asked questionsA theme I used before 0.5 no longer works.

Rockbox-Y1 0.5 moved its files. The release notes say to change paths inside old theme files from `/.rockbox` to `/sdcard/.rockbox`. The themes in this pack are already updated.Can I use 240p themes?

Not on Rockbox-Y1 0.5 or later, which is 360p only. 240p themes need a 240p build: 240p builds can't be used on a Y1 bought new after May 2026, or on any Y1 that shipped with Original Software 3.0.7 or later. Flashing one there stops the player from starting.Will this delete my settings?

No, as long as you merge. Replacing the whole `.rockbox` folder would.

## More Rockbox tutorials

### [Find the hidden .rockbox folder](show-hidden-rockbox-folder-windows.html)

Windows

### [Album art for PictureFlow](pictureflow-album-art-windows.html)

Windows

### [Rockbox-Y1 themes](../rockbox-y1-themes.html)

### [Rockbox-Y1 hub](../rockbox-y1/)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
