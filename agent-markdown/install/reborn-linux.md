---
title: "Install Reborn (Y2Linux / y2reborn) on Linux | Linux install guide"
description: "How to install Reborn (Y2Linux) on Linux for every supported Innioasis and Timmkoo model. A Debian-based Linux system with the native Reborn music player for the Innioasis Y2. Choose the model first, then follow the Linux Updater CE steps."
language: "en"
source: "https://innioasis.app/install/reborn-linux.html"
---

# Install Reborn (Y2Linux / y2reborn) on Linux | Linux install guide

[Home](../index.html)/[Install guides](index.html)/[Linux](linux.html)/Reborn (Y2Linux)

Reborn (Y2Linux) · Linux

# Install Reborn (Y2Linux / y2reborn) on Linux

A Debian-based Linux system with the native Reborn music player for the Innioasis Y2. These Linux guides cover every model the project supports. People also search for Y2Linux, Y2 Reborn, y2reborn, Reborn Y2; this is the same Reborn (Y2Linux) install.[Get Updater CE for Linux](../guide.html#linux)[Linux install guides](linux.html)[Linux USB permission notes](../drivers.html#linux)Your computer[Windows](reborn-windows.html)[macOS](reborn-mac.html)[Linux](reborn-linux.html)[All platforms](index.html)

## Prepare Linux for the install
  - Download `UpdaterCE.AppImage`, make it executable with `chmod +x UpdaterCE.AppImage`, and run it. The current AppImage targets Intel/AMD x86_64 systems.
  - If the AppImage does not start on Ubuntu 22.04 or newer, install `libfuse2` with your package manager. On Ubuntu 24.04 the package is `libfuse2t64`. Do not run the app as root.
  - If Updater CE cannot open the player, add the MediaTek USB permission rule: save `SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"` as `/etc/udev/rules.d/51-innioasis.rules`, then run `sudo udevadm control --reload && sudo udevadm trigger`. Add your user to `plugdev` if needed.

The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed. [Full Linux setup notes](../drivers.html#linux).

## Choose your model

Y2

### Reborn (Y2Linux) on Innioasis Y2

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.[Linux guide](reborn-y2linux-y2-linux.html)[Model guides](y2.html)

## How the install works
  - Install Updater CE on Linux using the steps above.
  - Select the model printed on the player, then choose Reborn (Y2Linux).
  - Choose a stable release listed for that model.
  - Click Install / Restore, power the player off and connect it at the prompt.
  - Wait for success. After the first start, copy `system.img` from the stock Y2 package into the Firmware folder on Internal Storage to enable Wi-Fi, FM radio and Bluetooth. Follow the Y2 Reborn radio setup guide for the exact steps.

## Questions people askWhich Reborn (Y2Linux) package should I download on Linux?

Use Innioasis Updater CE and select the model first. The app downloads the package from the project's official release. If you download manually, use the ZIP that names the model and, on a Y1, the correct Type A or Type B asset.Does Reborn (Y2Linux) work on every model?

This project is listed for Innioasis Y2. Open the model card for the exact guide.Is Y2Linux the same as Reborn (Y2Linux)?

Yes. Y2Linux, Y2 Reborn, y2reborn are names people use for the same project.Do I need a driver?

No proprietary driver, but the udev rule for vendor ID 0e8d and your user in plugdev are required.Can I undo it?

Restore Original Software for Y2 if you want the stock player back.

## Other platforms[Windows](reborn-windows.html)[macOS](reborn-mac.html)[All Reborn (Y2Linux) guides](reborn.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
