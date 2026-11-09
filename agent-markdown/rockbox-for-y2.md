---
title: "Rockbox for Y2 (Rockbox-Y2): overview, builds and install guide"
description: "Rockbox for Y2, Rockbox-Y2 and rockbox-y2 refer to the community Rockbox firmware port for the Innioasis Y2. Learn what it includes and how to install it with Innioasis Updater CE."
language: "en"
source: "https://innioasis.app/rockbox-for-y2.html"
---

# Rockbox for Y2 (Rockbox-Y2): overview, builds and install guide

[← Firmware Downloads](firmware.html?model=Y2&software=rockbox-y2)

Rockbox-Y2 · Innioasis Y2

# Rockbox for Y2 (Rockbox-Y2)

Rockbox-Y2 (also called “Rockbox for Y2”) is the dedicated community Rockbox firmware port for the Innioasis Y2. It uses its own ROM package (`rom_y2.zip`) and is installed directly through Innioasis Updater CE.[Install Rockbox-Y2](rockbox-y2/install.html)[Download the ROM](rockbox-y2/download.html)[Written tutorial](guides/rockbox-y2.html)[Rockbox-Y2 hub](rockbox-y2/)

## Built specifically for the Innioasis Y2

In Innioasis Updater CE, this firmware is listed as Rockbox when Y2 is selected. Its releases are published by the [spycemagic/y2-rockbox](firmware.html?model=Y2&software=rockbox-y2) project with the package name `rom_y2.zip`.

Never install a Y1 firmware package on a Y2. Selecting Y2 in Updater CE automatically filters the release list to Y2-compatible builds only.

## What Rockbox-Y2 offers
  - Tag-based music library — browse albums, artists, and genres from your audio file tags, or browse folders directly.
  - Playback controls — gapless playback, crossfade, ReplayGain, and equalizer settings.
  - Custom themes — install themes compatible with your Rockbox-Y2 build ([Y2 theme guide](rockbox-y2-themes.html)).
  - 100% offline — plays local files from your MicroSD card with no accounts or subscriptions.
  - Easy factory restore — return to Y2 Original Software at any time in Updater CE.

## Choosing a Rockbox-Y2 release
  - Always select Y2 in Device Model first.
  - Choose the latest release unless you are testing a specific version.
  - Read the [Rockbox-Y2 release notes](release-notes/rockbox-y2/index.html) to see what changed in each build.

## Direct downloads from the community developers

Innioasis Updater CE always downloads firmware packages directly from the community firmware developers ([spycemagic/y2-rockbox](firmware.html?model=Y2&software=rockbox-y2)), and those developers are solely responsible for listing their software releases in Updater CE.

You can let Updater CE download and flash `rom_y2.zip` automatically, or download the package from our [Rockbox-Y2 downloads page](rockbox-y2/download.html) and [Rockbox ROM download page](rockbox-rom-download.html).[Rockbox-Y2 downloads](rockbox-y2/download.html)[Install from a local ZIP](rockbox-y2/portable-zip.html)

## How to install Rockbox-Y2
  - Open Innioasis Updater CE and set Device Model to Y2.
  - Select Rockbox in Software.
  - Pick a Y2 release from the list.
  - Click Install / Restore so Updater CE downloads the package directly from the developer.
  - Power the Y2 completely off and connect it with a USB data cable when Updater CE asks.
  - Wait for the completion message, then unplug and turn on your Y2.

For the full step-by-step walkthrough, read the [Rockbox-Y2 tutorial](guides/rockbox-y2.html).

## Restoring the original Y2 software

To go back to factory firmware, select Y2 and Original Software in Updater CE, choose a stable release, and click Install / Restore. See the [restore guide](rockbox-y2/restore-stock.html) and [Y2 Original Software page](original-software-y2.html).

## Frequently asked questionsWhere does Updater CE download Rockbox-Y2 from?

Updater CE always downloads firmware packages directly from the community firmware developers' own releases (`spycemagic/y2-rockbox`). The developers are solely responsible for listing their software releases in Updater CE.Why is the package named rom_y2.zip?

The developer names the Y2 firmware archive `rom_y2.zip` so it cannot be confused with the Y1's `rom.zip`.Do Y1 themes work on the Y2?

Not always. Check the release notes for your Y2 build and see the [Rockbox-Y2 theme guide](rockbox-y2-themes.html).

## Related guides

### [Rockbox-Y2 hub](rockbox-y2/)

All Y2 guides: install, downloads, themes, restore, dual boot, and troubleshooting.

### [Rockbox-Y1 vs Rockbox-Y2](rockbox-y1-vs-y2.html)

How the Y1 and Y2 Rockbox builds differ.

### [Rockbox-Y2 themes](rockbox-y2-themes.html)

Installing and resetting themes on Rockbox-Y2.

### [Rockbox for Y1](rockbox-for-y1.html)

Overview and install guide for the Innioasis Y1 port.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
