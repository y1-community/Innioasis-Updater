---
title: "Install software on Innioasis D1 on Linux | Linux install guide"
description: "How to install custom software and restore the stock system on the Innioasis D1 with Linux. Linux setup, Updater CE steps, model checks and troubleshooting."
language: "en"
source: "https://innioasis.app/install/d1-linux.html"
---

# Install software on Innioasis D1 on Linux | Linux install guide

[Home](../index.html)/[Install guides](index.html)/[Innioasis D1](d1.html)/Linux

Innioasis D1 · Linux

# Install software on Innioasis D1 on Linux

D-series MediaTek player. These are the Linux routes for the Innioasis D1.[Get Updater CE for Linux](../guide.html#linux)[Linux install guides](linux.html)[Linux USB permission notes](../drivers.html#linux)Your computer[Windows](d1-windows.html)[macOS](d1-mac.html)[Linux](d1-linux.html)[All platforms](index.html)

## Prepare Linux for the install
  - Download `UpdaterCE.AppImage`, make it executable with `chmod +x UpdaterCE.AppImage`, and run it. The current AppImage targets Intel/AMD x86_64 systems.
  - If the AppImage does not start on Ubuntu 22.04 or newer, install `libfuse2` with your package manager. On Ubuntu 24.04 the package is `libfuse2t64`. Do not run the app as root.
  - If Updater CE cannot open the player, add the MediaTek USB permission rule: save `SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"` as `/etc/udev/rules.d/51-innioasis.rules`, then run `sudo udevadm control --reload && sudo udevadm trigger`. Add your user to `plugdev` if needed.

The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed. [Full Linux setup notes](../drivers.html#linux).

## Software for the Innioasis D1

### No public custom package yet

The community archive does not list a dedicated custom system for this model yet. Use [the Innioasis D1 archive page](../firmware.html?model=D1) to check for a stock restore package, and read the [recovery guide](../guides/recovery.html) if the player will not start.

## Restore the stock system

D-series MediaTek player.[Browse the Innioasis D1 archive](../firmware.html?model=D1)

## Questions people askCan I install custom software on the Innioasis D1 with Linux?

Yes, when the project lists the Innioasis D1. Every project card above opens the Linux guide for that software and model.Do I need a driver on Linux?

Add the udev rule for vendor ID 0e8d and make the AppImage executable.Will I lose my music?

Back up first. A full system install can wipe internal storage; the microSD card is normally left alone.How do I restore the factory software?

Choose the model and Original Software in Updater CE, pick a stable release, then run Install / Restore.

## Other platforms[Windows](d1-windows.html)[macOS](d1-mac.html)[All Innioasis D1 guides](d1.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
