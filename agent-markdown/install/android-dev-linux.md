---
title: "Install Android 4.2 / 4.4 development ROM on Linux | Linux install guide"
description: "How to install Android development ROM on Linux for every supported Innioasis and Timmkoo model. A development Android image for testing, not a daily-driver system. Choose the model first, then follow the Linux Updater CE steps."
language: "en"
source: "https://innioasis.app/install/android-dev-linux.html"
---

# Install Android 4.2 / 4.4 development ROM on Linux | Linux install guide

[Home](../index.html)/[Install guides](index.html)/[Linux](linux.html)/Android development ROM

Android development ROM · Linux

# Install Android 4.2 / 4.4 development ROM on Linux

A development Android image for testing, not a daily-driver system. These Linux guides cover every model the project supports. People also search for Android 4.2, Android 4.4, Android dev ROM, ATA ROM; this is the same Android development ROM install.[Get Updater CE for Linux](../guide.html#linux)[Linux install guides](linux.html)[Linux USB permission notes](../drivers.html#linux)Your computer[Windows](android-dev-windows.html)[macOS](android-dev-mac.html)[Linux](android-dev-linux.html)[All platforms](index.html)

## Prepare Linux for the install
  - Download `UpdaterCE.AppImage`, make it executable with `chmod +x UpdaterCE.AppImage`, and run it. The current AppImage targets Intel/AMD x86_64 systems.
  - If the AppImage does not start on Ubuntu 22.04 or newer, install `libfuse2` with your package manager. On Ubuntu 24.04 the package is `libfuse2t64`. Do not run the app as root.
  - If Updater CE cannot open the player, add the MediaTek USB permission rule: save `SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"` as `/etc/udev/rules.d/51-innioasis.rules`, then run `sudo udevadm control --reload && sudo udevadm trigger`. Add your user to `plugdev` if needed.

The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed. [Full Linux setup notes](../drivers.html#linux).

## Choose your model

Y1

### Android development ROM on Innioasis Y1

Android 4.2 development ROM for Innioasis Y1.[Linux guide](android-4-2-y1-linux.html)[Model guides](y1.html)

Y2

### Android development ROM on Innioasis Y2

Android 4.4 development ROM for Innioasis Y2.[Linux guide](android-4-4-y2-linux.html)[Model guides](y2.html)

## How the install works
  - Install Updater CE on Linux using the steps above.
  - Select the model printed on the player, then choose Android development ROM.
  - Choose a stable release listed for that model.
  - Click Install / Restore, power the player off and connect it at the prompt.
  - Wait for success. Boot may take longer. Reinstall Original Software when you finish testing.

## Questions people askWhich Android development ROM package should I download on Linux?

Use Innioasis Updater CE and select the model first. The app downloads the package from the project's official release. If you download manually, use the ZIP that names the model and, on a Y1, the correct Type A or Type B asset.Does Android development ROM work on every model?

This project is listed for Innioasis Y1, Innioasis Y2. Open the model card for the exact guide.Is Android 4.2 the same as Android development ROM?

Yes. Android 4.2, Android 4.4, Android dev ROM are names people use for the same project.Do I need a driver?

No proprietary driver, but the udev rule for vendor ID 0e8d and your user in plugdev are required.Can I undo it?

Restore Original Software for the same model when you are done testing.

## Other platforms[Windows](android-dev-windows.html)[macOS](android-dev-mac.html)[All Android development ROM guides](android-dev.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
