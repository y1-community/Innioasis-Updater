---
title: "Install Linux for Y1 (Dev) on Windows | Windows install guide"
description: "How to install Linux for Y1 (Dev) on a Windows PC for every supported Innioasis and Timmkoo model. A development Linux image for the Innioasis Y1. Choose the model first, then follow the Windows Updater CE steps."
language: "en"
source: "https://innioasis.app/install/linux-dev-windows.html"
---

# Install Linux for Y1 (Dev) on Windows | Windows install guide

[Home](../index.html)/[Install guides](index.html)/[Windows](windows.html)/Linux for Y1 (Dev)

Linux for Y1 (Dev) · Windows

# Install Linux for Y1 (Dev) on Windows

A development Linux image for the Innioasis Y1. These Windows guides cover every model the project supports. People also search for Linux for Y1, Y1 Linux, Linux dev ROM; this is the same Linux for Y1 (Dev) install.[Get Updater CE for Windows](../guide.html#windows)[Windows install guides](windows.html)[Download the Windows MediaTek driver](../drivers.html#windows)Your computer[Windows](linux-dev-windows.html)[macOS](linux-dev-mac.html)[Linux](linux-dev-linux.html)[All platforms](index.html)

## Prepare Windows for the install
  - Download the Innioasis Updater CE installer (`installer.exe`) from the official GitHub release and run it. If SmartScreen says “Windows protected your PC”, choose More info then Run anyway only for the file you just downloaded from `github.com/y1-community/Innioasis-Updater`.
  - Install the MediaTek USB driver with `DriverInstall.exe`, then restart the PC. The driver is what lets Windows see a powered-off player when Updater CE asks for it.
  - Use a USB port on the PC itself and a cable that carries data. A charge-only cable or an unpowered hub is the usual reason the player never appears.

Windows 10 and 11 x64 are the normal targets. ARM64 Windows is experimental. [Full Windows setup notes](../drivers.html#windows).

## Choose your model

Y1

### Linux for Y1 (Dev) on Innioasis Y1

Linux development build for Innioasis Y1.[Windows guide](linux-y1-windows.html)[Model guides](y1.html)

## How the install works
  - Install Updater CE on Windows using the steps above.
  - Select the model printed on the player, then choose Linux for Y1 (Dev).
  - Choose a stable release listed for that model.
  - Click Install / Restore, power the player off and connect it at the prompt.
  - Wait for success. Expect missing features and occasional instability. Reinstall Original Software when you finish testing.

## Questions people askWhich Linux for Y1 (Dev) package should I download on Windows?

Use Innioasis Updater CE and select the model first. The app downloads the package from the project's official release. If you download manually, use the ZIP that names the model and, on a Y1, the correct Type A or Type B asset.Does Linux for Y1 (Dev) work on every model?

This project is listed for Innioasis Y1. Open the model card for the exact guide.Is Linux for Y1 the same as Linux for Y1 (Dev)?

Yes. Linux for Y1, Y1 Linux, Linux dev ROM are names people use for the same project.Do I need a driver?

Yes. Install the MediaTek driver with DriverInstall.exe and restart before connecting the player.Can I undo it?

Restore Original Software for Y1 when you are done testing.

## Other platforms[macOS](linux-dev-mac.html)[Linux](linux-dev-linux.html)[All Linux for Y1 (Dev) guides](linux-dev.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
