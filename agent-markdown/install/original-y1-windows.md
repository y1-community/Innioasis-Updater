---
title: "Restore Original Software (stock firmware) on Innioasis Y1 with a Windows PC | Windows install guide"
description: "Step-by-step Original Software Y1 Windows install guide. The factory system image from Innioasis or Timmkoo, used to undo a custom install or recover a player that will not boot. Includes Windows setup, Updater CE steps, drivers, troubleshooting and the stock restore path. People also search for stock firmware, factory firmware, stock ROM, original firmware; this is the same Original Software install."
language: "en"
source: "https://innioasis.app/install/original-y1-windows.html"
---

# Restore Original Software (stock firmware) on Innioasis Y1 with a Windows PC | Windows install guide

[Home](../index.html)/[Install guides](index.html)/[Original Software](original-software.html)/[Innioasis Y1](y1.html)/Windows guide

Original Software · Innioasis Y1 · Windows

# Restore Original Software (stock firmware) on Innioasis Y1 with a Windows PC

The factory system image from Innioasis or Timmkoo, used to undo a custom install or recover a player that will not boot. This Windows tutorial is for the Innioasis Y1 only. People also search for stock firmware, factory firmware, stock ROM, original firmware; this is the same Original Software install.[Get Updater CE](../guide.html#windows)[All Original Software platforms](original-software.html)[Innioasis Y1 install guides](y1.html)[Open in Updater](../firmware.html?model=Y1&software=original-y1)Your computer[Windows](original-y1-windows.html)[macOS](original-y1-mac.html)[Linux](original-y1-linux.html)[All platforms](index.html)

## Before you start
  - Player: Innioasis Y1. Check the model printed on the player; Original Software packages for another model will not work.
  - Computer: Windows. Windows 10 and 11 x64 are the normal targets. ARM64 Windows is experimental.
  - Cable: a USB cable that carries data, not a charge-only cable.
  - Power: charge the player to at least half before you begin.
  - Backup: Back up music and recordings first. A stock restore replaces the system and can wipe internal storage; the microSD card is normally left alone.
Check the Y1 hardware type.Y1 players shipped in two hardware revisions. Players that shipped with software 2.0.0 or later are Type A; earlier units are Type B. Pick the matching asset in Updater CE.

## Prepare Windows for the install
  - Download the Innioasis Updater CE installer (`installer.exe`) from the official GitHub release and run it. If SmartScreen says “Windows protected your PC”, choose More info then Run anyway only for the file you just downloaded from `github.com/y1-community/Innioasis-Updater`.
  - Install the MediaTek USB driver with `DriverInstall.exe`, then restart the PC. The driver is what lets Windows see a powered-off player when Updater CE asks for it.
  - Use a USB port on the PC itself and a cable that carries data. A charge-only cable or an unpowered hub is the usual reason the player never appears.

Windows 10 and 11 x64 are the normal targets. ARM64 Windows is experimental. [Full Windows setup notes](../drivers.html#windows).

## Restore Original Software on Innioasis Y1 with a Windows PC
  - Get Updater CE ready: Install Innioasis Updater CE on a Windows PC and open it. The Windows setup is covered above; the [main guide](../guide.html#windows) has the download links.
  - Select Innioasis Y1: In Device Model, choose Innioasis Y1. Do not substitute another model, even when the software name is the same.
  - Choose Original Software: In Software, choose Original Software. Back up music and recordings first. A stock restore replaces the system and can wipe internal storage; the microSD card is normally left alone.
  - Choose a release: Choose the newest stable release shown for this model. Nightly and pre-release builds are for testing; tick the nightly-builds option only if you need one. Read the release note for the Innioasis Y1 before you continue.
  - Install / Restore: Click Install / Restore. When Updater CE asks, power the player fully off and plug it into the Windows PC. Device Manager should briefly show a MediaTek PreLoader USB VCOM or MTK USB Port entry while the player is connected.
  - Finish and check: Leave the player and cable alone until Updater CE shows success. The first start can take a few minutes. Set the language, Wi-Fi and Bluetooth again if the restore cleared them.
  - Keep the way back: This is the restore path itself: choose Original Software for the model and run Install / Restore. The stock package is always available from the [software archive](../firmware.html?model=Y1).

## If the install does not work
  - Updater CE cannot see the player: reinstall `DriverInstall.exe`, restart Windows, and try another USB port. If Core isolation / Memory integrity is enabled, Windows Security can block the MediaTek driver. Turn it off, reinstall the driver, then turn it back on when you are finished.
  - The install waits for the device: unplug the cable, power the player off again, click Install / Restore, and reconnect only at the fresh prompt.
  - SmartScreen or antivirus blocks the app: check that the file came from the official `y1-community/Innioasis-Updater` release, then allow it. Do not run an installer from an untrusted mirror.
  - Wrong package or model: return to Device Model and confirm the printed model. On a Y1, confirm Type A or Type B before choosing the asset again.
  - The player stopped responding: do not keep reconnecting. Read the [recovery guide](../guides/recovery.html) and the [troubleshooting guide](../troubleshooting.html) before trying a manual flash.

For a manual recovery on Innioasis Y1, use the files and scatter file that match the model. [SP Flash Tool notes](../sp-flash-tool.html).

## Going back to Original Software

This is the restore path itself: choose Original Software for the model and run Install / Restore. The stock restore uses the same Updater CE flow: choose Innioasis Y1, choose Original Software, pick a stable release and run Install / Restore.[Open the Innioasis Y1 stock restore](../firmware.html?model=Y1&software=original-y1)[Recovery guide](../guides/recovery.html)

## Questions people askCan I restore Original Software on Innioasis Y1 on Windows?

Yes. This page is the Windows guide for Original Software on the Innioasis Y1. Install Updater CE, select the model, choose the project and follow the install prompt.Do I need a driver on Windows?

Yes. Install `DriverInstall.exe` and restart Windows before connecting the powered-off player.Will this erase my music?

Back up music and recordings first. A stock restore replaces the system and can wipe internal storage; the microSD card is normally left alone. Files on the microSD card are normally left alone, but remove the card first if you want to be certain.Is stock firmware the same as Original Software?

Yes. stock firmware is one of the names people use for Original Software. This guide covers the same project on the Innioasis Y1.Does Original Software work on other models?

This project is listed for Innioasis / Timmkoo G1, Innioasis / Timmkoo G3, Innioasis / Timmkoo G5, Innioasis PR1, Innioasis / Timmkoo Q3, Innioasis / Timmkoo Q5, Innioasis R1, Innioasis SR1, Innioasis Y2. Use the model-specific guide for each player. Never install a package built for another model.How do I undo the install?

This is the restore path itself: choose Original Software for the model and run Install / Restore. Open the [software archive](../firmware.html?model=Y1) or the model restore guide for the exact steps.What if the player is not detected?

Start with the Windows checklist above, then read the [troubleshooting guide](../troubleshooting.html). A data cable, a direct USB port and connecting only at the prompt fix most connection problems.

## Install this on another computer

### macOS install guide

Original Software on macOS for the Innioasis Y1.[macOS guide](original-y1-mac.html)

### Linux install guide

Original Software on Linux for the Innioasis Y1.[Linux guide](original-y1-linux.html)[All Original Software guides](original-software.html)[Innioasis Y1 install guides](y1.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
