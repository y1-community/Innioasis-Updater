---
title: "Install Android 4.2 / 4.4 development ROM on Windows | Windows install guide"
description: "How to install Android development ROM on a Windows PC for every supported Innioasis and Timmkoo model. A development Android image for testing, not a daily-driver system. Choose the model first, then follow the Windows Updater CE steps."
language: "en"
source: "https://innioasis.app/install/android-dev-windows.html"
---

# Install Android 4.2 / 4.4 development ROM on Windows | Windows install guide

[Home](../index.html)/[Install guides](index.html)/[Windows](windows.html)/Android development ROM

Android development ROM · Windows

# Install Android 4.2 / 4.4 development ROM on Windows

A development Android image for testing, not a daily-driver system. These Windows guides cover every model the project supports. People also search for Android 4.2, Android 4.4, Android dev ROM, ATA ROM; this is the same Android development ROM install.[Get Updater CE for Windows](../guide.html#windows)[Windows install guides](windows.html)[Download the Windows MediaTek driver](../drivers.html#windows)Your computer[Windows](android-dev-windows.html)[macOS](android-dev-mac.html)[Linux](android-dev-linux.html)[All platforms](index.html)

## Prepare Windows for the install
  - Download the Innioasis Updater CE installer (`installer.exe`) from the official GitHub release and run it. If SmartScreen says “Windows protected your PC”, choose More info then Run anyway only for the file you just downloaded from `github.com/y1-community/Innioasis-Updater`.
  - Install the MediaTek USB driver with `DriverInstall.exe`, then restart the PC. The driver is what lets Windows see a powered-off player when Updater CE asks for it.
  - Use a USB port on the PC itself and a cable that carries data. A charge-only cable or an unpowered hub is the usual reason the player never appears.

Windows 10 and 11 x64 are the normal targets. ARM64 Windows is experimental. [Full Windows setup notes](../drivers.html#windows).

## Choose your model

Y1

### Android development ROM on Innioasis Y1

Android 4.2 development ROM for Innioasis Y1.[Windows guide](android-4-2-y1-windows.html)[Model guides](y1.html)

Y2

### Android development ROM on Innioasis Y2

Android 4.4 development ROM for Innioasis Y2.[Windows guide](android-4-4-y2-windows.html)[Model guides](y2.html)

## How the install works
  - Install Updater CE on Windows using the steps above.
  - Select the model printed on the player, then choose Android development ROM.
  - Choose a stable release listed for that model.
  - Click Install / Restore, power the player off and connect it at the prompt.
  - Wait for success. Boot may take longer. Reinstall Original Software when you finish testing.

## Questions people askWhich Android development ROM package should I download on Windows?

Use Innioasis Updater CE and select the model first. The app downloads the package from the project's official release. If you download manually, use the ZIP that names the model and, on a Y1, the correct Type A or Type B asset.Does Android development ROM work on every model?

This project is listed for Innioasis Y1, Innioasis Y2. Open the model card for the exact guide.Is Android 4.2 the same as Android development ROM?

Yes. Android 4.2, Android 4.4, Android dev ROM are names people use for the same project.Do I need a driver?

Yes. Install the MediaTek driver with DriverInstall.exe and restart before connecting the player.Can I undo it?

Restore Original Software for the same model when you are done testing.

## Other platforms[macOS](android-dev-mac.html)[Linux](android-dev-linux.html)[All Android development ROM guides](android-dev.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
