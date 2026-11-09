---
title: "Install software on Innioasis Y1 on Linux | Linux install guide"
description: "How to install custom software and restore the stock system on the Innioasis Y1 with Linux. Linux setup, Updater CE steps, model checks and troubleshooting."
language: "en"
source: "https://innioasis.app/install/y1-linux.html"
---

# Install software on Innioasis Y1 on Linux | Linux install guide

[Home](../index.html)/[Install guides](index.html)/[Innioasis Y1](y1.html)/Linux

Innioasis Y1 · Linux

# Install software on Innioasis Y1 on Linux

4-inch touchscreen player powered by MediaTek MT6580. These are the Linux routes for the Innioasis Y1.[Get Updater CE for Linux](../guide.html#linux)[Linux install guides](linux.html)[Linux USB permission notes](../drivers.html#linux)Your computer[Windows](y1-windows.html)[macOS](y1-mac.html)[Linux](y1-linux.html)[All platforms](index.html)

## Prepare Linux for the install
  - Download `UpdaterCE.AppImage`, make it executable with `chmod +x UpdaterCE.AppImage`, and run it. The current AppImage targets Intel/AMD x86_64 systems.
  - If the AppImage does not start on Ubuntu 22.04 or newer, install `libfuse2` with your package manager. On Ubuntu 24.04 the package is `libfuse2t64`. Do not run the app as root.
  - If Updater CE cannot open the player, add the MediaTek USB permission rule: save `SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"` as `/etc/udev/rules.d/51-innioasis.rules`, then run `sudo udevadm control --reload && sudo udevadm trigger`. Add your user to `plugdev` if needed.

The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed. [Full Linux setup notes](../drivers.html#linux).

## Software for the Innioasis Y1

Original Software

### Original Software on Innioasis Y1

The stock Software path for restoring an Innioasis Y1.[Linux guide](original-y1-linux.html)[Family guides](original-software.html)

Rondo

### Rondo on Innioasis Y1

A lightweight, custom audio operating system for the Innioasis Y1.[Linux guide](rondo-y1-linux.html)[Family guides](rondo.html)

Rockbox

### Rockbox on Innioasis Y1

A music-first custom Software with deep playback and theme options.[Linux guide](rockbox-y1-linux.html)[Family guides](rockbox.html)

Solar

### Solar on Innioasis Y1

A Y1 custom Software with network features, including YouTube support.[Linux guide](solar-y1-linux.html)[Family guides](solar.html)

JJ Launcher

### JJ Launcher on Innioasis Y1

A launcher Software for Y1.[Linux guide](jj-launcher-y1-linux.html)[Family guides](jj-launcher.html)

Inniclassic

### Inniclassic on Innioasis Y1

A classic-style Y1 Software.[Linux guide](inniclassic-y1-linux.html)[Family guides](inniclassic.html)

Koensayr

### Koensayr on Innioasis Y1

A Y1 custom Software maintained by the community.[Linux guide](koensayr-y1-linux.html)[Family guides](koensayr.html)

Better-Y

### Better-Y on Innioasis Y1

Stock launcher, but better: metadata track numbers, artist/genre tag splitting, disc numbers, interactive Now Playing controls, proper caching, and 3.1.2 foundation.[Linux guide](better-y-y1-linux.html)[Family guides](better-y.html)

Android development ROM

### Android 4.2 (Dev) on Innioasis Y1

Android 4.2 development ROM for Innioasis Y1.[Linux guide](android-4-2-y1-linux.html)[Family guides](android-dev.html)

Linux for Y1 (Dev)

### Linux for Y1 (Dev) on Innioasis Y1

Linux development build for Innioasis Y1.[Linux guide](linux-y1-linux.html)[Family guides](linux-dev.html)

## Restore the stock system

4-inch touchscreen player powered by MediaTek MT6580.[Restore Original Software on Innioasis Y1](original-y1-linux.html)[Browse the Innioasis Y1 archive](../firmware.html?model=Y1)

## Questions people askCan I install custom software on the Innioasis Y1 with Linux?

Yes, when the project lists the Innioasis Y1. Every project card above opens the Linux guide for that software and model.Do I need a driver on Linux?

Add the udev rule for vendor ID 0e8d and make the AppImage executable.Will I lose my music?

Back up first. A full system install can wipe internal storage; the microSD card is normally left alone.How do I restore the factory software?

Choose the model and Original Software in Updater CE, pick a stable release, then run Install / Restore.

## Other platforms[Windows](y1-windows.html)[macOS](y1-mac.html)[All Innioasis Y1 guides](y1.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
