---
title: "Install Reborn (Y2Linux / y2reborn) on Innioasis Y2 with a Windows PC | Windows install guide"
description: "Step-by-step Reborn (Y2Linux) Y2 Windows install guide. A Debian-based Linux system with the native Reborn music player for the Innioasis Y2. Includes Windows setup, Updater CE steps, drivers, troubleshooting and the stock restore path. People also search for Y2Linux, Y2 Reborn, y2reborn, Reborn Y2; this is the same Reborn (Y2Linux) install."
language: "en"
source: "https://innioasis.app/install/reborn-y2linux-y2-windows.html"
---

# Install Reborn (Y2Linux / y2reborn) on Innioasis Y2 with a Windows PC | Windows install guide

[Home](../index.html)/[Install guides](index.html)/[Reborn (Y2Linux)](reborn.html)/[Innioasis Y2](y2.html)/Windows guide

Reborn (Y2Linux) · Innioasis Y2 · Windows

# Install Reborn (Y2Linux / y2reborn) on Innioasis Y2 with a Windows PC

A Debian-based Linux system with the native Reborn music player for the Innioasis Y2. This Windows tutorial is for the Innioasis Y2 only. People also search for Y2Linux, Y2 Reborn, y2reborn, Reborn Y2; this is the same Reborn (Y2Linux) install.[Get Updater CE](../guide.html#windows)[All Reborn (Y2Linux) platforms](reborn.html)[Innioasis Y2 install guides](y2.html)[Open in Updater](../firmware.html?model=Y2&software=reborn-y2linux-y2)Your computer[Windows](reborn-y2linux-y2-windows.html)[macOS](reborn-y2linux-y2-mac.html)[Linux](reborn-y2linux-y2-linux.html)[All platforms](index.html)

## Before you start
  - Player: Innioasis Y2. Check the model printed on the player; Reborn (Y2Linux) packages for another model will not work.
  - Computer: Windows. Windows 10 and 11 x64 are the normal targets. ARM64 Windows is experimental.
  - Cable: a USB cable that carries data, not a charge-only cable.
  - Power: charge the player to at least half before you begin.
  - Backup: Reborn is for the Y2 only. Back up the microSD and internal storage; the install replaces the system. Keep a stock Y2 package available for the way back.

## Prepare Windows for the install
  - Download the Innioasis Updater CE installer (`installer.exe`) from the official GitHub release and run it. If SmartScreen says “Windows protected your PC”, choose More info then Run anyway only for the file you just downloaded from `github.com/y1-community/Innioasis-Updater`.
  - Install the MediaTek USB driver with `DriverInstall.exe`, then restart the PC. The driver is what lets Windows see a powered-off player when Updater CE asks for it.
  - Use a USB port on the PC itself and a cable that carries data. A charge-only cable or an unpowered hub is the usual reason the player never appears.

Windows 10 and 11 x64 are the normal targets. ARM64 Windows is experimental. [Full Windows setup notes](../drivers.html#windows).

## Install Reborn (Y2Linux) on Innioasis Y2 with a Windows PC
  - Get Updater CE ready: Install Innioasis Updater CE on a Windows PC and open it. The Windows setup is covered above; the [main guide](../guide.html#windows) has the download links.
  - Select Innioasis Y2: In Device Model, choose Innioasis Y2. Do not substitute another model, even when the software name is the same.
  - Choose Reborn (Y2Linux): In Software, choose Reborn (Y2Linux). Reborn is for the Y2 only. Back up the microSD and internal storage; the install replaces the system. Keep a stock Y2 package available for the way back.
  - Choose a release: Choose the newest stable release shown for this model. Nightly and pre-release builds are for testing; tick the nightly-builds option only if you need one. Read the release note for the Innioasis Y2 before you continue.
  - Install / Restore: Click Install / Restore. When Updater CE asks, power the player fully off and plug it into the Windows PC. Device Manager should briefly show a MediaTek PreLoader USB VCOM or MTK USB Port entry while the player is connected.
  - Finish and check: Leave the player and cable alone until Updater CE shows success. After the first start, copy `system.img` from the stock Y2 package into the Firmware folder on Internal Storage to enable Wi-Fi, FM radio and Bluetooth. Follow the Y2 Reborn radio setup guide for the exact steps.
  - Keep the way back: Restore Original Software for Y2 if you want the stock player back. The stock package is always available from the [software archive](../firmware.html?model=Y2).

## If the install does not work
  - Updater CE cannot see the player: reinstall `DriverInstall.exe`, restart Windows, and try another USB port. If Core isolation / Memory integrity is enabled, Windows Security can block the MediaTek driver. Turn it off, reinstall the driver, then turn it back on when you are finished.
  - The install waits for the device: unplug the cable, power the player off again, click Install / Restore, and reconnect only at the fresh prompt.
  - SmartScreen or antivirus blocks the app: check that the file came from the official `y1-community/Innioasis-Updater` release, then allow it. Do not run an installer from an untrusted mirror.
  - Wrong package or model: return to Device Model and confirm the printed model. On a Y1, confirm Type A or Type B before choosing the asset again.
  - The player stopped responding: do not keep reconnecting. Read the [recovery guide](../guides/recovery.html) and the [troubleshooting guide](../troubleshooting.html) before trying a manual flash.

For a manual recovery on Innioasis Y2, use the files and scatter file that match the model. [SP Flash Tool notes](../sp-flash-tool.html).

## Going back to Original Software

Restore Original Software for Y2 if you want the stock player back. The stock restore uses the same Updater CE flow: choose Innioasis Y2, choose Original Software, pick a stable release and run Install / Restore.[Open the Innioasis Y2 stock restore](../firmware.html?model=Y2&software=original-y2)[Recovery guide](../guides/recovery.html)

## Questions people askCan I install Reborn (Y2Linux) on Innioasis Y2 on Windows?

Yes. This page is the Windows guide for Reborn (Y2Linux) on the Innioasis Y2. Install Updater CE, select the model, choose the project and follow the install prompt.Do I need a driver on Windows?

Yes. Install `DriverInstall.exe` and restart Windows before connecting the powered-off player.Will this erase my music?

Reborn is for the Y2 only. Back up the microSD and internal storage; the install replaces the system. Keep a stock Y2 package available for the way back. Files on the microSD card are normally left alone, but remove the card first if you want to be certain.Is Y2Linux the same as Reborn (Y2Linux)?

Yes. Y2Linux is one of the names people use for Reborn (Y2Linux). This guide covers the same project on the Innioasis Y2.Does Reborn (Y2Linux) work on other models?

This project is listed only for the Innioasis Y2 in the current catalogue. Never install a package built for another model.How do I undo the install?

Restore Original Software for Y2 if you want the stock player back. Open the [software archive](../firmware.html?model=Y2) or the model restore guide for the exact steps.What if the player is not detected?

Start with the Windows checklist above, then read the [troubleshooting guide](../troubleshooting.html). A data cable, a direct USB port and connecting only at the prompt fix most connection problems.

## Install this on another computer

### macOS install guide

Reborn (Y2Linux) on macOS for the Innioasis Y2.[macOS guide](reborn-y2linux-y2-mac.html)

### Linux install guide

Reborn (Y2Linux) on Linux for the Innioasis Y2.[Linux guide](reborn-y2linux-y2-linux.html)[All Reborn (Y2Linux) guides](reborn.html)[Innioasis Y2 install guides](y2.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
