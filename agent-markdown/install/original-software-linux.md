---
title: "Restore Original Software (stock firmware) on Linux | Linux install guide"
description: "How to restore Original Software on Linux for every supported Innioasis and Timmkoo model. The factory system image from Innioasis or Timmkoo, used to undo a custom install or recover a player that will not boot. Choose the model first, then follow the Linux Updater CE steps."
language: "en"
source: "https://innioasis.app/install/original-software-linux.html"
---

# Restore Original Software (stock firmware) on Linux | Linux install guide

[Home](../index.html)/[Install guides](index.html)/[Linux](linux.html)/Original Software

Original Software · Linux

# Restore Original Software (stock firmware) on Linux

The factory system image from Innioasis or Timmkoo, used to undo a custom install or recover a player that will not boot. These Linux guides cover every model the project supports. People also search for stock firmware, factory firmware, stock ROM, original firmware; this is the same Original Software install.[Get Updater CE for Linux](../guide.html#linux)[Linux install guides](linux.html)[Linux USB permission notes](../drivers.html#linux)Your computer[Windows](original-software-windows.html)[macOS](original-software-mac.html)[Linux](original-software-linux.html)[All platforms](index.html)

## Prepare Linux for the install
  - Download `UpdaterCE.AppImage`, make it executable with `chmod +x UpdaterCE.AppImage`, and run it. The current AppImage targets Intel/AMD x86_64 systems.
  - If the AppImage does not start on Ubuntu 22.04 or newer, install `libfuse2` with your package manager. On Ubuntu 24.04 the package is `libfuse2t64`. Do not run the app as root.
  - If Updater CE cannot open the player, add the MediaTek USB permission rule: save `SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"` as `/etc/udev/rules.d/51-innioasis.rules`, then run `sudo udevadm control --reload && sudo udevadm trigger`. Add your user to `plugdev` if needed.

The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed. [Full Linux setup notes](../drivers.html#linux).

## Choose your model

Y1

### Original Software on Innioasis Y1

The stock Software path for restoring an Innioasis Y1.[Linux guide](original-y1-linux.html)[Model guides](y1.html)

Y2

### Original Software on Innioasis Y2

The stock Software path for restoring an Innioasis Y2.[Linux guide](original-y2-linux.html)[Model guides](y2.html)

G1

### Original Software on Innioasis / Timmkoo G1

The stock Software path for restoring a Innioasis G1.[Linux guide](original-g1-linux.html)[Model guides](g1.html)

G3

### Original Software on Innioasis / Timmkoo G3

The stock Software path for restoring a Innioasis G3.[Linux guide](original-g3-linux.html)[Model guides](g3.html)

G5

### Original Software on Innioasis / Timmkoo G5

The stock Software path for restoring a Innioasis G5.[Linux guide](original-g5-linux.html)[Model guides](g5.html)

R1

### Original Software on Innioasis R1

The stock Software path for restoring a Innioasis R1.[Linux guide](original-r1-linux.html)[Model guides](r1.html)

PR1

### Original Software on Innioasis PR1

The stock Software path for restoring a Innioasis PR1.[Linux guide](original-pr1-linux.html)[Model guides](pr1.html)

SR1

### Original Software on Innioasis SR1

The stock Software path for restoring a Timmkoo SR1.[Linux guide](original-sr1-linux.html)[Model guides](sr1.html)

Q3

### Original Software on Innioasis / Timmkoo Q3

The stock Software path for restoring a Timmkoo Q3.[Linux guide](original-q3-linux.html)[Model guides](q3.html)

Q5

### Original Software on Innioasis / Timmkoo Q5

The stock Software path for restoring a Timmkoo Q5.[Linux guide](original-q5-linux.html)[Model guides](q5.html)

## How the install works
  - Install Updater CE on Linux using the steps above.
  - Select the model printed on the player, then choose Original Software.
  - Choose a stable release listed for that model.
  - Click Install / Restore, power the player off and connect it at the prompt.
  - Wait for success. The first start can take a few minutes. Set the language, Wi-Fi and Bluetooth again if the restore cleared them.

## Questions people askWhich Original Software package should I download on Linux?

Use Innioasis Updater CE and select the model first. The app downloads the package from the project's official release. If you download manually, use the ZIP that names the model and, on a Y1, the correct Type A or Type B asset.Does Original Software work on every model?

This project is listed for Innioasis Y1, Innioasis Y2, Innioasis / Timmkoo G1, Innioasis / Timmkoo G3, Innioasis / Timmkoo G5, Innioasis R1, Innioasis PR1, Innioasis SR1, Innioasis / Timmkoo Q3, Innioasis / Timmkoo Q5. Open the model card for the exact guide.Is stock firmware the same as Original Software?

Yes. stock firmware, factory firmware, stock ROM are names people use for the same project.Do I need a driver?

No proprietary driver, but the udev rule for vendor ID 0e8d and your user in plugdev are required.Can I undo it?

This is the restore path itself: choose Original Software for the model and run Install / Restore.

## Other platforms[Windows](original-software-windows.html)[macOS](original-software-mac.html)[All Original Software guides](original-software.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
