---
title: "Install Rockbox on Windows | Windows install guide"
description: "How to install Rockbox on a Windows PC for every supported Innioasis and Timmkoo model. Music-first custom firmware with a tag database, gapless playback, EQ, themes and plugins. Choose the model first, then follow the Windows Updater CE steps."
language: "en"
source: "https://innioasis.app/install/rockbox-windows.html"
---

# Install Rockbox on Windows | Windows install guide

[Home](../index.html)/[Install guides](index.html)/[Windows](windows.html)/Rockbox

Rockbox · Windows

# Install Rockbox on Windows

Music-first custom firmware with a tag database, gapless playback, EQ, themes and plugins. These Windows guides cover every model the project supports. People also search for Rockbox-Y1, Rockbox-Y2, Rockbox for Y1, Rockbox for Y2; this is the same Rockbox install.[Get Updater CE for Windows](../guide.html#windows)[Windows install guides](windows.html)[Download the Windows MediaTek driver](../drivers.html#windows)Your computer[Windows](rockbox-windows.html)[macOS](rockbox-mac.html)[Linux](rockbox-linux.html)[All platforms](index.html)

## Prepare Windows for the install
  - Download the Innioasis Updater CE installer (`installer.exe`) from the official GitHub release and run it. If SmartScreen says “Windows protected your PC”, choose More info then Run anyway only for the file you just downloaded from `github.com/y1-community/Innioasis-Updater`.
  - Install the MediaTek USB driver with `DriverInstall.exe`, then restart the PC. The driver is what lets Windows see a powered-off player when Updater CE asks for it.
  - Use a USB port on the PC itself and a cable that carries data. A charge-only cable or an unpowered hub is the usual reason the player never appears.

Windows 10 and 11 x64 are the normal targets. ARM64 Windows is experimental. [Full Windows setup notes](../drivers.html#windows).

## Choose your model

Y1

### Rockbox on Innioasis Y1

A music-first custom Software with deep playback and theme options.[Windows guide](rockbox-y1-windows.html)[Model guides](y1.html)

Y2

### Rockbox on Innioasis Y2

The Y2 Rockbox build. Select Y2 before choosing this Software.[Windows guide](rockbox-y2-windows.html)[Model guides](y2.html)

## How the install works
  - Install Updater CE on Windows using the steps above.
  - Select the model printed on the player, then choose Rockbox.
  - Choose a stable release listed for that model.
  - Click Install / Restore, power the player off and connect it at the prompt.
  - Wait for success. On first start, let Rockbox scan the microSD card. Themes and settings live on the card, so keep a copy before you change cards.

## Questions people askWhich Rockbox package should I download on Windows?

Use Innioasis Updater CE and select the model first. The app downloads the package from the project's official release. If you download manually, use the ZIP that names the model and, on a Y1, the correct Type A or Type B asset.Does Rockbox work on every model?

This project is listed for Innioasis Y1, Innioasis Y2. Open the model card for the exact guide.Is Rockbox-Y1 the same as Rockbox?

Yes. Rockbox-Y1, Rockbox-Y2, Rockbox for Y1 are names people use for the same project.Do I need a driver?

Yes. Install the MediaTek driver with DriverInstall.exe and restart before connecting the player.Can I undo it?

Restore Original Software for the same model if you want the stock player back.

## Other platforms[macOS](rockbox-mac.html)[Linux](rockbox-linux.html)[All Rockbox guides](rockbox.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
