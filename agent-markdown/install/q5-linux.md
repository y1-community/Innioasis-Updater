---
title: "Install software on Innioasis / Timmkoo Q5 on Linux | Linux install guide"
description: "How to install custom software and restore the stock system on the Innioasis / Timmkoo Q5 with Linux. Linux setup, Updater CE steps, model checks and troubleshooting."
language: "en"
source: "https://innioasis.app/install/q5-linux.html"
---

# Install software on Innioasis / Timmkoo Q5 on Linux | Linux install guide

[Home](../index.html)/[Install guides](index.html)/[Innioasis / Timmkoo Q5](q5.html)/Linux

Innioasis / Timmkoo Q5 · Linux

# Install software on Innioasis / Timmkoo Q5 on Linux

Q-series MediaTek Android player. These are the Linux routes for the Innioasis / Timmkoo Q5.[Get Updater CE for Linux](../guide.html#linux)[Linux install guides](linux.html)[Linux USB permission notes](../drivers.html#linux)Your computer[Windows](q5-windows.html)[macOS](q5-mac.html)[Linux](q5-linux.html)[All platforms](index.html)

## Prepare Linux for the install
  - Download `UpdaterCE.AppImage`, make it executable with `chmod +x UpdaterCE.AppImage`, and run it. The current AppImage targets Intel/AMD x86_64 systems.
  - If the AppImage does not start on Ubuntu 22.04 or newer, install `libfuse2` with your package manager. On Ubuntu 24.04 the package is `libfuse2t64`. Do not run the app as root.
  - If Updater CE cannot open the player, add the MediaTek USB permission rule: save `SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"` as `/etc/udev/rules.d/51-innioasis.rules`, then run `sudo udevadm control --reload && sudo udevadm trigger`. Add your user to `plugdev` if needed.

The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed. [Full Linux setup notes](../drivers.html#linux).

## Software for the Innioasis / Timmkoo Q5

Original Software

### Original Software on Innioasis / Timmkoo Q5

The stock Software path for restoring a Timmkoo Q5.[Linux guide](original-q5-linux.html)[Family guides](original-software.html)

## Restore the stock system

Q-series MediaTek Android player.[Restore Original Software on Innioasis / Timmkoo Q5](original-q5-linux.html)[Browse the Innioasis / Timmkoo Q5 archive](../firmware.html?model=Q5)

## Questions people askCan I install custom software on the Innioasis / Timmkoo Q5 with Linux?

Yes, when the project lists the Innioasis / Timmkoo Q5. Every project card above opens the Linux guide for that software and model.Do I need a driver on Linux?

Add the udev rule for vendor ID 0e8d and make the AppImage executable.Will I lose my music?

Back up first. A full system install can wipe internal storage; the microSD card is normally left alone.How do I restore the factory software?

Choose the model and Original Software in Updater CE, pick a stable release, then run Install / Restore.

## Other platforms[Windows](q5-windows.html)[macOS](q5-mac.html)[All Innioasis / Timmkoo Q5 guides](q5.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
