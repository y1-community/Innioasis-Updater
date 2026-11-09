---
title: "Install Linux for Y1 (Dev) on Innioasis Y1 with a Windows PC | Windows install guide"
description: "Step-by-step Linux for Y1 (Dev) Y1 Windows install guide. A development Linux image for the Innioasis Y1. Includes Windows setup, Updater CE steps, drivers, troubleshooting and the stock restore path. People also search for Linux for Y1, Y1 Linux, Linux dev ROM; this is the same Linux for Y1 (Dev) install."
language: "en"
source: "https://innioasis.app/install/linux-y1-windows.html"
---

# Install Linux for Y1 (Dev) on Innioasis Y1 with a Windows PC | Windows install guide

[Home](../index.html)/[Install guides](index.html)/[Linux for Y1 (Dev)](linux-dev.html)/[Innioasis Y1](y1.html)/Windows guide

Linux for Y1 (Dev) · Innioasis Y1 · Windows

# Install Linux for Y1 (Dev) on Innioasis Y1 with a Windows PC

A development Linux image for the Innioasis Y1. This Windows tutorial is for the Innioasis Y1 only. People also search for Linux for Y1, Y1 Linux, Linux dev ROM; this is the same Linux for Y1 (Dev) install.[Get Updater CE](../guide.html#windows)[All Linux for Y1 (Dev) platforms](linux-dev.html)[Innioasis Y1 install guides](y1.html)[Open in Updater](../firmware.html?model=Y1&software=linux-y1)Your computer[Windows](linux-y1-windows.html)[macOS](linux-y1-mac.html)[Linux](linux-y1-linux.html)[All platforms](index.html)

## Before you start
  - Player: Innioasis Y1. Check the model printed on the player; Linux for Y1 (Dev) packages for another model will not work.
  - Computer: Windows. Windows 10 and 11 x64 are the normal targets. ARM64 Windows is experimental.
  - Cable: a USB cable that carries data, not a charge-only cable.
  - Power: charge the player to at least half before you begin.
  - Backup: This is an early development build. Keep a stock restore ready and expect rough edges.
Check the Y1 hardware type.Y1 players shipped in two hardware revisions. Players that shipped with software 2.0.0 or later are Type A; earlier units are Type B. Pick the matching asset in Updater CE.

## Prepare Windows for the install
  - Download the Innioasis Updater CE installer (`installer.exe`) from the official GitHub release and run it. If SmartScreen says “Windows protected your PC”, choose More info then Run anyway only for the file you just downloaded from `github.com/y1-community/Innioasis-Updater`.
  - Install the MediaTek USB driver with `DriverInstall.exe`, then restart the PC. The driver is what lets Windows see a powered-off player when Updater CE asks for it.
  - Use a USB port on the PC itself and a cable that carries data. A charge-only cable or an unpowered hub is the usual reason the player never appears.

Windows 10 and 11 x64 are the normal targets. ARM64 Windows is experimental. [Full Windows setup notes](../drivers.html#windows).

## Install Linux for Y1 (Dev) on Innioasis Y1 with a Windows PC
  - Get Updater CE ready: Install Innioasis Updater CE on a Windows PC and open it. The Windows setup is covered above; the [main guide](../guide.html#windows) has the download links.
  - Select Innioasis Y1: In Device Model, choose Innioasis Y1. Do not substitute another model, even when the software name is the same.
  - Choose Linux for Y1 (Dev): In Software, choose Linux for Y1 (Dev). This is an early development build. Keep a stock restore ready and expect rough edges.
  - Choose a release: Choose the newest stable release shown for this model. Nightly and pre-release builds are for testing; tick the nightly-builds option only if you need one. Read the release note for the Innioasis Y1 before you continue.
  - Install / Restore: Click Install / Restore. When Updater CE asks, power the player fully off and plug it into the Windows PC. Device Manager should briefly show a MediaTek PreLoader USB VCOM or MTK USB Port entry while the player is connected.
  - Finish and check: Leave the player and cable alone until Updater CE shows success. Expect missing features and occasional instability. Reinstall Original Software when you finish testing.
  - Keep the way back: Restore Original Software for Y1 when you are done testing. The stock package is always available from the [software archive](../firmware.html?model=Y1).

## If the install does not work
  - Updater CE cannot see the player: reinstall `DriverInstall.exe`, restart Windows, and try another USB port. If Core isolation / Memory integrity is enabled, Windows Security can block the MediaTek driver. Turn it off, reinstall the driver, then turn it back on when you are finished.
  - The install waits for the device: unplug the cable, power the player off again, click Install / Restore, and reconnect only at the fresh prompt.
  - SmartScreen or antivirus blocks the app: check that the file came from the official `y1-community/Innioasis-Updater` release, then allow it. Do not run an installer from an untrusted mirror.
  - Wrong package or model: return to Device Model and confirm the printed model. On a Y1, confirm Type A or Type B before choosing the asset again.
  - The player stopped responding: do not keep reconnecting. Read the [recovery guide](../guides/recovery.html) and the [troubleshooting guide](../troubleshooting.html) before trying a manual flash.

For a manual recovery on Innioasis Y1, use the files and scatter file that match the model. [SP Flash Tool notes](../sp-flash-tool.html).

## Going back to Original Software

Restore Original Software for Y1 when you are done testing. The stock restore uses the same Updater CE flow: choose Innioasis Y1, choose Original Software, pick a stable release and run Install / Restore.[Open the Innioasis Y1 stock restore](../firmware.html?model=Y1&software=original-y1)[Recovery guide](../guides/recovery.html)

## Questions people askCan I install Linux for Y1 (Dev) on Innioasis Y1 on Windows?

Yes. This page is the Windows guide for Linux for Y1 (Dev) on the Innioasis Y1. Install Updater CE, select the model, choose the project and follow the install prompt.Do I need a driver on Windows?

Yes. Install `DriverInstall.exe` and restart Windows before connecting the powered-off player.Will this erase my music?

This is an early development build. Keep a stock restore ready and expect rough edges. Files on the microSD card are normally left alone, but remove the card first if you want to be certain.Is Linux for Y1 the same as Linux for Y1 (Dev)?

Yes. Linux for Y1 is one of the names people use for Linux for Y1 (Dev). This guide covers the same project on the Innioasis Y1.Does Linux for Y1 (Dev) work on other models?

This project is listed only for the Innioasis Y1 in the current catalogue. Never install a package built for another model.How do I undo the install?

Restore Original Software for Y1 when you are done testing. Open the [software archive](../firmware.html?model=Y1) or the model restore guide for the exact steps.What if the player is not detected?

Start with the Windows checklist above, then read the [troubleshooting guide](../troubleshooting.html). A data cable, a direct USB port and connecting only at the prompt fix most connection problems.

## Install this on another computer

### macOS install guide

Linux for Y1 (Dev) on macOS for the Innioasis Y1.[macOS guide](linux-y1-mac.html)

### Linux install guide

Linux for Y1 (Dev) on Linux for the Innioasis Y1.[Linux guide](linux-y1-linux.html)[All Linux for Y1 (Dev) guides](linux-dev.html)[Innioasis Y1 install guides](y1.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
