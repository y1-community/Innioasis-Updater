---
title: "Install Android 4.2 / 4.4 development ROM on Innioasis Y2 with a Windows PC | Windows install guide"
description: "Step-by-step Android development ROM Y2 Windows install guide. A development Android image for testing, not a daily-driver system. Includes Windows setup, Updater CE steps, drivers, troubleshooting and the stock restore path. People also search for Android 4.2, Android 4.4, Android dev ROM, ATA ROM; this is the same Android development ROM install."
language: "en"
source: "https://innioasis.app/install/android-4-4-y2-windows.html"
---

# Install Android 4.2 / 4.4 development ROM on Innioasis Y2 with a Windows PC | Windows install guide

[Home](../index.html)/[Install guides](index.html)/[Android development ROM](android-dev.html)/[Innioasis Y2](y2.html)/Windows guide

Android development ROM · Innioasis Y2 · Windows

# Install Android 4.2 / 4.4 development ROM on Innioasis Y2 with a Windows PC

A development Android image for testing, not a daily-driver system. This Windows tutorial is for the Innioasis Y2 only. People also search for Android 4.2, Android 4.4, Android dev ROM, ATA ROM; this is the same Android development ROM install.[Get Updater CE](../guide.html#windows)[All Android development ROM platforms](android-dev.html)[Innioasis Y2 install guides](y2.html)[Open in Updater](../firmware.html?model=Y2&software=android-4-4-y2)Your computer[Windows](android-4-4-y2-windows.html)[macOS](android-4-4-y2-mac.html)[Linux](android-4-4-y2-linux.html)[All platforms](index.html)

## Before you start
  - Player: Innioasis Y2. Check the model printed on the player; Android development ROM packages for another model will not work.
  - Computer: Windows. Windows 10 and 11 x64 are the normal targets. ARM64 Windows is experimental.
  - Cable: a USB cable that carries data, not a charge-only cable.
  - Power: charge the player to at least half before you begin.
  - Backup: This is a development build. Expect missing features, and keep a stock restore package ready before you flash.

## Prepare Windows for the install
  - Download the Innioasis Updater CE installer (`installer.exe`) from the official GitHub release and run it. If SmartScreen says “Windows protected your PC”, choose More info then Run anyway only for the file you just downloaded from `github.com/y1-community/Innioasis-Updater`.
  - Install the MediaTek USB driver with `DriverInstall.exe`, then restart the PC. The driver is what lets Windows see a powered-off player when Updater CE asks for it.
  - Use a USB port on the PC itself and a cable that carries data. A charge-only cable or an unpowered hub is the usual reason the player never appears.

Windows 10 and 11 x64 are the normal targets. ARM64 Windows is experimental. [Full Windows setup notes](../drivers.html#windows).

## Install Android development ROM on Innioasis Y2 with a Windows PC
  - Get Updater CE ready: Install Innioasis Updater CE on a Windows PC and open it. The Windows setup is covered above; the [main guide](../guide.html#windows) has the download links.
  - Select Innioasis Y2: In Device Model, choose Innioasis Y2. Do not substitute another model, even when the software name is the same.
  - Choose Android development ROM: In Software, choose Android development ROM. This is a development build. Expect missing features, and keep a stock restore package ready before you flash.
  - Choose a release: Choose the newest stable release shown for this model. Nightly and pre-release builds are for testing; tick the nightly-builds option only if you need one. Read the release note for the Innioasis Y2 before you continue.
  - Install / Restore: Click Install / Restore. When Updater CE asks, power the player fully off and plug it into the Windows PC. Device Manager should briefly show a MediaTek PreLoader USB VCOM or MTK USB Port entry while the player is connected.
  - Finish and check: Leave the player and cable alone until Updater CE shows success. Boot may take longer. Reinstall Original Software when you finish testing.
  - Keep the way back: Restore Original Software for the same model when you are done testing. The stock package is always available from the [software archive](../firmware.html?model=Y2).

## If the install does not work
  - Updater CE cannot see the player: reinstall `DriverInstall.exe`, restart Windows, and try another USB port. If Core isolation / Memory integrity is enabled, Windows Security can block the MediaTek driver. Turn it off, reinstall the driver, then turn it back on when you are finished.
  - The install waits for the device: unplug the cable, power the player off again, click Install / Restore, and reconnect only at the fresh prompt.
  - SmartScreen or antivirus blocks the app: check that the file came from the official `y1-community/Innioasis-Updater` release, then allow it. Do not run an installer from an untrusted mirror.
  - Wrong package or model: return to Device Model and confirm the printed model. On a Y1, confirm Type A or Type B before choosing the asset again.
  - The player stopped responding: do not keep reconnecting. Read the [recovery guide](../guides/recovery.html) and the [troubleshooting guide](../troubleshooting.html) before trying a manual flash.

For a manual recovery on Innioasis Y2, use the files and scatter file that match the model. [SP Flash Tool notes](../sp-flash-tool.html).

## Going back to Original Software

Restore Original Software for the same model when you are done testing. The stock restore uses the same Updater CE flow: choose Innioasis Y2, choose Original Software, pick a stable release and run Install / Restore.[Open the Innioasis Y2 stock restore](../firmware.html?model=Y2&software=original-y2)[Recovery guide](../guides/recovery.html)

## Questions people askCan I install Android development ROM on Innioasis Y2 on Windows?

Yes. This page is the Windows guide for Android development ROM on the Innioasis Y2. Install Updater CE, select the model, choose the project and follow the install prompt.Do I need a driver on Windows?

Yes. Install `DriverInstall.exe` and restart Windows before connecting the powered-off player.Will this erase my music?

This is a development build. Expect missing features, and keep a stock restore package ready before you flash. Files on the microSD card are normally left alone, but remove the card first if you want to be certain.Is Android 4.2 the same as Android development ROM?

Yes. Android 4.2 is one of the names people use for Android development ROM. This guide covers the same project on the Innioasis Y2.Does Android development ROM work on other models?

This project is listed for Innioasis Y1. Use the model-specific guide for each player. Never install a package built for another model.How do I undo the install?

Restore Original Software for the same model when you are done testing. Open the [software archive](../firmware.html?model=Y2) or the model restore guide for the exact steps.What if the player is not detected?

Start with the Windows checklist above, then read the [troubleshooting guide](../troubleshooting.html). A data cable, a direct USB port and connecting only at the prompt fix most connection problems.

## Install this on another computer

### macOS install guide

Android development ROM on macOS for the Innioasis Y2.[macOS guide](android-4-4-y2-mac.html)

### Linux install guide

Android development ROM on Linux for the Innioasis Y2.[Linux guide](android-4-4-y2-linux.html)[All Android development ROM guides](android-dev.html)[Innioasis Y2 install guides](y2.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
