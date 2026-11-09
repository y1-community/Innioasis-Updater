---
title: "Install software on Innioasis / Timmkoo Q3E on Linux | Linux install guide"
description: "How to install custom software and restore the stock system on the Innioasis / Timmkoo Q3E with Linux. Linux setup, Updater CE steps, model checks and troubleshooting."
language: "en"
source: "https://innioasis.app/install/q3e-linux.html"
---

# Install software on Innioasis / Timmkoo Q3E on Linux | Linux install guide

[Home](../index.html)/[Install guides](index.html)/[Innioasis / Timmkoo Q3E](q3e.html)/Linux

Innioasis / Timmkoo Q3E · Linux

# Install software on Innioasis / Timmkoo Q3E on Linux

Q-series MediaTek player. These are the Linux routes for the Innioasis / Timmkoo Q3E.[Get Updater CE for Linux](../guide.html#linux)[Linux install guides](linux.html)[Linux USB permission notes](../drivers.html#linux)Your computer[Windows](q3e-windows.html)[macOS](q3e-mac.html)[Linux](q3e-linux.html)[All platforms](index.html)

## Prepare Linux for the install
  - Download `UpdaterCE.AppImage`, make it executable with `chmod +x UpdaterCE.AppImage`, and run it. The current AppImage targets Intel/AMD x86_64 systems.
  - If the AppImage does not start on Ubuntu 22.04 or newer, install `libfuse2` with your package manager. On Ubuntu 24.04 the package is `libfuse2t64`. Do not run the app as root.
  - If Updater CE cannot open the player, add the MediaTek USB permission rule: save `SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"` as `/etc/udev/rules.d/51-innioasis.rules`, then run `sudo udevadm control --reload && sudo udevadm trigger`. Add your user to `plugdev` if needed.

The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed. [Full Linux setup notes](../drivers.html#linux).

## Software for the Innioasis / Timmkoo Q3E

### No public custom package yet

The community archive does not list a dedicated custom system for this model yet. Use [the Innioasis / Timmkoo Q3E archive page](../firmware.html?model=Q3E) to check for a stock restore package, and read the [recovery guide](../guides/recovery.html) if the player will not start.

## Restore the stock system

Q-series MediaTek player.[Browse the Innioasis / Timmkoo Q3E archive](../firmware.html?model=Q3E)

## Questions people askCan I install custom software on the Innioasis / Timmkoo Q3E with Linux?

Yes, when the project lists the Innioasis / Timmkoo Q3E. Every project card above opens the Linux guide for that software and model.Do I need a driver on Linux?

Add the udev rule for vendor ID 0e8d and make the AppImage executable.Will I lose my music?

Back up first. A full system install can wipe internal storage; the microSD card is normally left alone.How do I restore the factory software?

Choose the model and Original Software in Updater CE, pick a stable release, then run Install / Restore.

## Other platforms[Windows](q3e-windows.html)[macOS](q3e-mac.html)[All Innioasis / Timmkoo Q3E guides](q3e.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
