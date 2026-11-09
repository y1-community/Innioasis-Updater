---
title: "Install software on Innioasis A5 with a Windows PC | Windows install guide"
description: "How to install custom software and restore the stock system on the Innioasis A5 with a Windows PC. Windows setup, Updater CE steps, model checks and troubleshooting."
language: "en"
source: "https://innioasis.app/install/a5-windows.html"
---

# Install software on Innioasis A5 with a Windows PC | Windows install guide

[Home](../index.html)/[Install guides](index.html)/[Innioasis A5](a5.html)/Windows

Innioasis A5 · Windows

# Install software on Innioasis A5 with a Windows PC

A-series MediaTek player. These are the Windows routes for the Innioasis A5.[Get Updater CE for Windows](../guide.html#windows)[Windows install guides](windows.html)[Download the Windows MediaTek driver](../drivers.html#windows)Your computer[Windows](a5-windows.html)[macOS](a5-mac.html)[Linux](a5-linux.html)[All platforms](index.html)

## Prepare Windows for the install
  - Download the Innioasis Updater CE installer (`installer.exe`) from the official GitHub release and run it. If SmartScreen says “Windows protected your PC”, choose More info then Run anyway only for the file you just downloaded from `github.com/y1-community/Innioasis-Updater`.
  - Install the MediaTek USB driver with `DriverInstall.exe`, then restart the PC. The driver is what lets Windows see a powered-off player when Updater CE asks for it.
  - Use a USB port on the PC itself and a cable that carries data. A charge-only cable or an unpowered hub is the usual reason the player never appears.

Windows 10 and 11 x64 are the normal targets. ARM64 Windows is experimental. [Full Windows setup notes](../drivers.html#windows).

## Software for the Innioasis A5

### No public custom package yet

The community archive does not list a dedicated custom system for this model yet. Use [the Innioasis A5 archive page](../firmware.html?model=A5) to check for a stock restore package, and read the [recovery guide](../guides/recovery.html) if the player will not start.

## Restore the stock system

A-series MediaTek player.[Browse the Innioasis A5 archive](../firmware.html?model=A5)

## Questions people askCan I install custom software on the Innioasis A5 with Windows?

Yes, when the project lists the Innioasis A5. Every project card above opens the Windows guide for that software and model.Do I need a driver on Windows?

Yes, install the MediaTek driver and restart.Will I lose my music?

Back up first. A full system install can wipe internal storage; the microSD card is normally left alone.How do I restore the factory software?

Choose the model and Original Software in Updater CE, pick a stable release, then run Install / Restore.

## Other platforms[macOS](a5-mac.html)[Linux](a5-linux.html)[All Innioasis A5 guides](a5.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
