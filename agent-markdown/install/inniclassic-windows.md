---
title: "Install Inniclassic (iPod Classic interface) on Windows | Windows install guide"
description: "How to install Inniclassic on a Windows PC for every supported Innioasis and Timmkoo model. An iPod Classic-style interface for the Innioasis Y1 and Y2. Choose the model first, then follow the Windows Updater CE steps."
language: "en"
source: "https://innioasis.app/install/inniclassic-windows.html"
---

# Install Inniclassic (iPod Classic interface) on Windows | Windows install guide

[Home](../index.html)/[Install guides](index.html)/[Windows](windows.html)/Inniclassic

Inniclassic · Windows

# Install Inniclassic (iPod Classic interface) on Windows

An iPod Classic-style interface for the Innioasis Y1 and Y2. These Windows guides cover every model the project supports. People also search for InniClassic, Inni Classic, iPod Classic firmware, Classic Y1; this is the same Inniclassic install.[Get Updater CE for Windows](../guide.html#windows)[Windows install guides](windows.html)[Download the Windows MediaTek driver](../drivers.html#windows)Your computer[Windows](inniclassic-windows.html)[macOS](inniclassic-mac.html)[Linux](inniclassic-linux.html)[All platforms](index.html)

## Prepare Windows for the install
  - Download the Innioasis Updater CE installer (`installer.exe`) from the official GitHub release and run it. If SmartScreen says “Windows protected your PC”, choose More info then Run anyway only for the file you just downloaded from `github.com/y1-community/Innioasis-Updater`.
  - Install the MediaTek USB driver with `DriverInstall.exe`, then restart the PC. The driver is what lets Windows see a powered-off player when Updater CE asks for it.
  - Use a USB port on the PC itself and a cable that carries data. A charge-only cable or an unpowered hub is the usual reason the player never appears.

Windows 10 and 11 x64 are the normal targets. ARM64 Windows is experimental. [Full Windows setup notes](../drivers.html#windows).

## Choose your model

Y1

### Inniclassic on Innioasis Y1

A classic-style Y1 Software.[Windows guide](inniclassic-y1-windows.html)[Model guides](y1.html)

Y2

### Inniclassic on Innioasis Y2

Inniclassic build for the Innioasis Y2.[Windows guide](inniclassic-y2-windows.html)[Model guides](y2.html)

## How the install works
  - Install Updater CE on Windows using the steps above.
  - Select the model printed on the player, then choose Inniclassic.
  - Choose a stable release listed for that model.
  - Click Install / Restore, power the player off and connect it at the prompt.
  - Wait for success. The first boot may take longer while the library indexes. Let the scan finish before you judge performance.

## Questions people askWhich Inniclassic package should I download on Windows?

Use Innioasis Updater CE and select the model first. The app downloads the package from the project's official release. If you download manually, use the ZIP that names the model and, on a Y1, the correct Type A or Type B asset.Does Inniclassic work on every model?

This project is listed for Innioasis Y1, Innioasis Y2. Open the model card for the exact guide.Is InniClassic the same as Inniclassic?

Yes. InniClassic, Inni Classic, iPod Classic firmware are names people use for the same project.Do I need a driver?

Yes. Install the MediaTek driver with DriverInstall.exe and restart before connecting the player.Can I undo it?

Restore Original Software for the same model if you want the stock interface back.

## Other platforms[macOS](inniclassic-mac.html)[Linux](inniclassic-linux.html)[All Inniclassic guides](inniclassic.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
