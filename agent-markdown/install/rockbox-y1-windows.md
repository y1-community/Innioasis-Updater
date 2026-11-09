---
title: "Install Rockbox on Innioasis Y1 with a Windows PC | Windows install guide"
description: "Step-by-step Rockbox Y1 Windows install guide. Music-first custom firmware with a tag database, gapless playback, EQ, themes and plugins. Includes Windows setup, Updater CE steps, drivers, troubleshooting and the stock restore path. People also search for Rockbox-Y1, Rockbox-Y2, Rockbox for Y1, Rockbox for Y2; this is the same Rockbox install."
language: "en"
source: "https://innioasis.app/install/rockbox-y1-windows.html"
---

# Install Rockbox on Innioasis Y1 with a Windows PC | Windows install guide

[Home](../index.html)/[Install guides](index.html)/[Rockbox](rockbox.html)/[Innioasis Y1](y1.html)/Windows guide

Rockbox · Innioasis Y1 · Windows

# Install Rockbox on Innioasis Y1 with a Windows PC

Music-first custom firmware with a tag database, gapless playback, EQ, themes and plugins. This Windows tutorial is for the Innioasis Y1 only. People also search for Rockbox-Y1, Rockbox-Y2, Rockbox for Y1, Rockbox for Y2; this is the same Rockbox install.[Get Updater CE](../guide.html#windows)[All Rockbox platforms](rockbox.html)[Innioasis Y1 install guides](y1.html)[Open in Updater](../firmware.html?model=Y1&software=rockbox-y1)Your computer[Windows](rockbox-y1-windows.html)[macOS](rockbox-y1-mac.html)[Linux](rockbox-y1-linux.html)[All platforms](index.html)

## Before you start
  - Player: Innioasis Y1. Check the model printed on the player; Rockbox packages for another model will not work.
  - Computer: Windows. Windows 10 and 11 x64 are the normal targets. ARM64 Windows is experimental.
  - Cable: a USB cable that carries data, not a charge-only cable.
  - Power: charge the player to at least half before you begin.
  - Backup: Use the build for this exact model. Rockbox-Y1 and Rockbox-Y2 are separate packages. On a Y1, check whether the player is Type A or Type B before you pick the asset.
Check the Y1 hardware type.Y1 players shipped in two hardware revisions. Players that shipped with software 2.0.0 or later are Type A; earlier units are Type B. Pick the matching asset in Updater CE.

## Prepare Windows for the install
  - Download the Innioasis Updater CE installer (`installer.exe`) from the official GitHub release and run it. If SmartScreen says “Windows protected your PC”, choose More info then Run anyway only for the file you just downloaded from `github.com/y1-community/Innioasis-Updater`.
  - Install the MediaTek USB driver with `DriverInstall.exe`, then restart the PC. The driver is what lets Windows see a powered-off player when Updater CE asks for it.
  - Use a USB port on the PC itself and a cable that carries data. A charge-only cable or an unpowered hub is the usual reason the player never appears.

Windows 10 and 11 x64 are the normal targets. ARM64 Windows is experimental. [Full Windows setup notes](../drivers.html#windows).

## Install Rockbox on Innioasis Y1 with a Windows PC
  - Get Updater CE ready: Install Innioasis Updater CE on a Windows PC and open it. The Windows setup is covered above; the [main guide](../guide.html#windows) has the download links.
  - Select Innioasis Y1: In Device Model, choose Innioasis Y1. Do not substitute another model, even when the software name is the same.
  - Choose Rockbox: In Software, choose Rockbox. Use the build for this exact model. Rockbox-Y1 and Rockbox-Y2 are separate packages. On a Y1, check whether the player is Type A or Type B before you pick the asset.
  - Choose a release: Choose the newest stable release shown for this model. Nightly and pre-release builds are for testing; tick the nightly-builds option only if you need one. Read the release note for the Innioasis Y1 before you continue.
  - Install / Restore: Click Install / Restore. When Updater CE asks, power the player fully off and plug it into the Windows PC. Device Manager should briefly show a MediaTek PreLoader USB VCOM or MTK USB Port entry while the player is connected.
  - Finish and check: Leave the player and cable alone until Updater CE shows success. On first start, let Rockbox scan the microSD card. Themes and settings live on the card, so keep a copy before you change cards.
  - Keep the way back: Restore Original Software for the same model if you want the stock player back. The stock package is always available from the [software archive](../firmware.html?model=Y1).

## If the install does not work
  - Updater CE cannot see the player: reinstall `DriverInstall.exe`, restart Windows, and try another USB port. If Core isolation / Memory integrity is enabled, Windows Security can block the MediaTek driver. Turn it off, reinstall the driver, then turn it back on when you are finished.
  - The install waits for the device: unplug the cable, power the player off again, click Install / Restore, and reconnect only at the fresh prompt.
  - SmartScreen or antivirus blocks the app: check that the file came from the official `y1-community/Innioasis-Updater` release, then allow it. Do not run an installer from an untrusted mirror.
  - Wrong package or model: return to Device Model and confirm the printed model. On a Y1, confirm Type A or Type B before choosing the asset again.
  - The player stopped responding: do not keep reconnecting. Read the [recovery guide](../guides/recovery.html) and the [troubleshooting guide](../troubleshooting.html) before trying a manual flash.

For a manual recovery on Innioasis Y1, use the files and scatter file that match the model. [SP Flash Tool notes](../sp-flash-tool.html).

## Going back to Original Software

Restore Original Software for the same model if you want the stock player back. The stock restore uses the same Updater CE flow: choose Innioasis Y1, choose Original Software, pick a stable release and run Install / Restore.[Open the Innioasis Y1 stock restore](../firmware.html?model=Y1&software=original-y1)[Recovery guide](../guides/recovery.html)

## Questions people askCan I install Rockbox on Innioasis Y1 on Windows?

Yes. This page is the Windows guide for Rockbox on the Innioasis Y1. Install Updater CE, select the model, choose the project and follow the install prompt.Do I need a driver on Windows?

Yes. Install `DriverInstall.exe` and restart Windows before connecting the powered-off player.Will this erase my music?

Use the build for this exact model. Rockbox-Y1 and Rockbox-Y2 are separate packages. On a Y1, check whether the player is Type A or Type B before you pick the asset. Files on the microSD card are normally left alone, but remove the card first if you want to be certain.Is Rockbox-Y1 the same as Rockbox?

Yes. Rockbox-Y1 is one of the names people use for Rockbox. This guide covers the same project on the Innioasis Y1.Does Rockbox work on other models?

This project is listed for Innioasis Y2. Use the model-specific guide for each player. Never install a package built for another model.How do I undo the install?

Restore Original Software for the same model if you want the stock player back. Open the [software archive](../firmware.html?model=Y1) or the model restore guide for the exact steps.What if the player is not detected?

Start with the Windows checklist above, then read the [troubleshooting guide](../troubleshooting.html). A data cable, a direct USB port and connecting only at the prompt fix most connection problems.

## Install this on another computer

### macOS install guide

Rockbox on macOS for the Innioasis Y1.[macOS guide](rockbox-y1-mac.html)

### Linux install guide

Rockbox on Linux for the Innioasis Y1.[Linux guide](rockbox-y1-linux.html)[All Rockbox guides](rockbox.html)[Innioasis Y1 install guides](y1.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
