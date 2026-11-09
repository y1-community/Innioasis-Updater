---
title: "Install software on Innioasis Y2 on Linux | Linux install guide"
description: "How to install custom software and restore the stock system on the Innioasis Y2 with Linux. Linux setup, Updater CE steps, model checks and troubleshooting."
language: "en"
source: "https://innioasis.app/install/y2-linux.html"
---

# Install software on Innioasis Y2 on Linux | Linux install guide

[Home](../index.html)/[Install guides](index.html)/[Innioasis Y2](y2.html)/Linux

Innioasis Y2 · Linux

# Install software on Innioasis Y2 on Linux

Compact button and touchscreen player powered by MediaTek MT6572 / MT6580. These are the Linux routes for the Innioasis Y2.[Get Updater CE for Linux](../guide.html#linux)[Linux install guides](linux.html)[Linux USB permission notes](../drivers.html#linux)Your computer[Windows](y2-windows.html)[macOS](y2-mac.html)[Linux](y2-linux.html)[All platforms](index.html)

## Prepare Linux for the install
  - Download `UpdaterCE.AppImage`, make it executable with `chmod +x UpdaterCE.AppImage`, and run it. The current AppImage targets Intel/AMD x86_64 systems.
  - If the AppImage does not start on Ubuntu 22.04 or newer, install `libfuse2` with your package manager. On Ubuntu 24.04 the package is `libfuse2t64`. Do not run the app as root.
  - If Updater CE cannot open the player, add the MediaTek USB permission rule: save `SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"` as `/etc/udev/rules.d/51-innioasis.rules`, then run `sudo udevadm control --reload && sudo udevadm trigger`. Add your user to `plugdev` if needed.

The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed. [Full Linux setup notes](../drivers.html#linux).

## Software for the Innioasis Y2

Original Software

### Original Software on Innioasis Y2

The stock Software path for restoring an Innioasis Y2.[Linux guide](original-y2-linux.html)[Family guides](original-software.html)

Reborn (Y2Linux)

### Reborn (Y2Linux) on Innioasis Y2

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.[Linux guide](reborn-y2linux-y2-linux.html)[Family guides](reborn.html)

Rockbox

### Rockbox on Innioasis Y2

The Y2 Rockbox build. Select Y2 before choosing this Software.[Linux guide](rockbox-y2-linux.html)[Family guides](rockbox.html)

Solar

### Solar on Innioasis Y2

Listed for Y2 in the current Updater CE catalogue. Check release notes before installing.[Linux guide](solar-y2-linux.html)[Family guides](solar.html)

JJ Launcher

### JJ Launcher on Innioasis Y2

Listed for Y2 in the current Updater CE catalogue. Check release notes before installing.[Linux guide](jj-launcher-y2-linux.html)[Family guides](jj-launcher.html)

Inniclassic

### Inniclassic on Innioasis Y2

Inniclassic build for the Innioasis Y2.[Linux guide](inniclassic-y2-linux.html)[Family guides](inniclassic.html)

Y2Player

### Y2Player on Innioasis Y2

A Y2 custom Software.[Linux guide](y2player-y2-linux.html)[Family guides](y2player.html)

Android development ROM

### Android 4.4 (Dev) on Innioasis Y2

Android 4.4 development ROM for Innioasis Y2.[Linux guide](android-4-4-y2-linux.html)[Family guides](android-dev.html)

## Restore the stock system

Compact button and touchscreen player powered by MediaTek MT6572 / MT6580.[Restore Original Software on Innioasis Y2](original-y2-linux.html)[Browse the Innioasis Y2 archive](../firmware.html?model=Y2)

## Questions people askCan I install custom software on the Innioasis Y2 with Linux?

Yes, when the project lists the Innioasis Y2. Every project card above opens the Linux guide for that software and model.Do I need a driver on Linux?

Add the udev rule for vendor ID 0e8d and make the AppImage executable.Will I lose my music?

Back up first. A full system install can wipe internal storage; the microSD card is normally left alone.How do I restore the factory software?

Choose the model and Original Software in Updater CE, pick a stable release, then run Install / Restore.

## Other platforms[Windows](y2-windows.html)[macOS](y2-mac.html)[All Innioasis Y2 guides](y2.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
