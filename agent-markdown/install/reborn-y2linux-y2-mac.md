---
title: "Install Reborn (Y2Linux / y2reborn) on Innioasis Y2 with a Mac | macOS install guide"
description: "Step-by-step Reborn (Y2Linux) Y2 macOS install guide. A Debian-based Linux system with the native Reborn music player for the Innioasis Y2. Includes macOS setup, Updater CE steps, drivers, troubleshooting and the stock restore path. People also search for Y2Linux, Y2 Reborn, y2reborn, Reborn Y2; this is the same Reborn (Y2Linux) install."
language: "en"
source: "https://innioasis.app/install/reborn-y2linux-y2-mac.html"
---

# Install Reborn (Y2Linux / y2reborn) on Innioasis Y2 with a Mac | macOS install guide

[Home](../index.html)/[Install guides](index.html)/[Reborn (Y2Linux)](reborn.html)/[Innioasis Y2](y2.html)/macOS guide

Reborn (Y2Linux) · Innioasis Y2 · macOS

# Install Reborn (Y2Linux / y2reborn) on Innioasis Y2 with a Mac

A Debian-based Linux system with the native Reborn music player for the Innioasis Y2. This macOS tutorial is for the Innioasis Y2 only. People also search for Y2Linux, Y2 Reborn, y2reborn, Reborn Y2; this is the same Reborn (Y2Linux) install.[Get Updater CE](../guide.html#macos)[All Reborn (Y2Linux) platforms](reborn.html)[Innioasis Y2 install guides](y2.html)[Open in Updater](../firmware.html?model=Y2&software=reborn-y2linux-y2)Your computer[Windows](reborn-y2linux-y2-windows.html)[macOS](reborn-y2linux-y2-mac.html)[Linux](reborn-y2linux-y2-linux.html)[All platforms](index.html)

## Before you start
  - Player: Innioasis Y2. Check the model printed on the player; Reborn (Y2Linux) packages for another model will not work.
  - Computer: macOS. Intel and Apple Silicon Macs are supported. The current guide targets macOS Monterey (12.0) or later.
  - Cable: a USB cable that carries data, not a charge-only cable.
  - Power: charge the player to at least half before you begin.
  - Backup: Reborn is for the Y2 only. Back up the microSD and internal storage; the install replaces the system. Keep a stock Y2 package available for the way back.

## Prepare macOS for the install
  - Download the macOS disk image (`Innioasis.Updater.for.Mac.dmg`), open it, and drag Innioasis Updater CE into Applications.
  - The first launch is blocked by Gatekeeper until you approve it. Right-click the app and choose Open, or open System Settings → Privacy & Security and click Open Anyway. Do not disable Gatekeeper for the whole Mac.
  - No separate USB driver is needed. Connect the player directly to the Mac, not through an unpowered hub; some USB-C adapters drop the connection during a flash.

Intel and Apple Silicon Macs are supported. The current guide targets macOS Monterey (12.0) or later. [Full macOS setup notes](../drivers.html#macos).

## Install Reborn (Y2Linux) on Innioasis Y2 with a Mac
  - Get Updater CE ready: Install Innioasis Updater CE on a Mac and open it. The macOS setup is covered above; the [main guide](../guide.html#macos) has the download links.
  - Select Innioasis Y2: In Device Model, choose Innioasis Y2. Do not substitute another model, even when the software name is the same.
  - Choose Reborn (Y2Linux): In Software, choose Reborn (Y2Linux). Reborn is for the Y2 only. Back up the microSD and internal storage; the install replaces the system. Keep a stock Y2 package available for the way back.
  - Choose a release: Choose the newest stable release shown for this model. Nightly and pre-release builds are for testing; tick the nightly-builds option only if you need one. Read the release note for the Innioasis Y2 before you continue.
  - Install / Restore: Click Install / Restore. Power the player fully off and connect it only when Updater CE prompts. To confirm the Mac sees it, open System Information → USB, or run `system_profiler SPUSBDataType` in Terminal and look for a brief MediaTek entry.
  - Finish and check: Leave the player and cable alone until Updater CE shows success. After the first start, copy `system.img` from the stock Y2 package into the Firmware folder on Internal Storage to enable Wi-Fi, FM radio and Bluetooth. Follow the Y2 Reborn radio setup guide for the exact steps.
  - Keep the way back: Restore Original Software for Y2 if you want the stock player back. The stock package is always available from the [software archive](../firmware.html?model=Y2).

## If the install does not work
  - macOS says the app is damaged or cannot be opened: that is quarantine, not a corrupt download. Approve it in System Settings → Privacy & Security with Open Anyway.
  - The player disconnects during the install: use a direct port, keep the Mac awake, and avoid hubs or adapters. Reconnect only when Updater CE asks.
  - SP Flash Tool is not available on macOS. Updater CE uses the MTKClient route on a Mac; for manual SP Flash Tool recovery, use a Windows or Linux computer.
  - Wrong package or model: return to Device Model and confirm the printed model. On a Y1, confirm Type A or Type B before choosing the asset again.
  - The player stopped responding: do not keep reconnecting. Read the [recovery guide](../guides/recovery.html) and the [troubleshooting guide](../troubleshooting.html) before trying a manual flash.

For a manual recovery on Innioasis Y2, use the files and scatter file that match the model. [SP Flash Tool notes](../sp-flash-tool.html).

## Going back to Original Software

Restore Original Software for Y2 if you want the stock player back. The stock restore uses the same Updater CE flow: choose Innioasis Y2, choose Original Software, pick a stable release and run Install / Restore.[Open the Innioasis Y2 stock restore](../firmware.html?model=Y2&software=original-y2)[Recovery guide](../guides/recovery.html)

## Questions people askCan I install Reborn (Y2Linux) on Innioasis Y2 on macOS?

Yes. This page is the macOS guide for Reborn (Y2Linux) on the Innioasis Y2. Install Updater CE, select the model, choose the project and follow the install prompt.Do I need a driver on macOS?

No separate driver is needed. macOS includes the USB support, and the app uses the MTKClient route on a Mac.Will this erase my music?

Reborn is for the Y2 only. Back up the microSD and internal storage; the install replaces the system. Keep a stock Y2 package available for the way back. Files on the microSD card are normally left alone, but remove the card first if you want to be certain.Is Y2Linux the same as Reborn (Y2Linux)?

Yes. Y2Linux is one of the names people use for Reborn (Y2Linux). This guide covers the same project on the Innioasis Y2.Does Reborn (Y2Linux) work on other models?

This project is listed only for the Innioasis Y2 in the current catalogue. Never install a package built for another model.How do I undo the install?

Restore Original Software for Y2 if you want the stock player back. Open the [software archive](../firmware.html?model=Y2) or the model restore guide for the exact steps.What if the player is not detected?

Start with the macOS checklist above, then read the [troubleshooting guide](../troubleshooting.html). A data cable, a direct USB port and connecting only at the prompt fix most connection problems.

## Install this on another computer

### Windows install guide

Reborn (Y2Linux) on Windows for the Innioasis Y2.[Windows guide](reborn-y2linux-y2-windows.html)

### Linux install guide

Reborn (Y2Linux) on Linux for the Innioasis Y2.[Linux guide](reborn-y2linux-y2-linux.html)[All Reborn (Y2Linux) guides](reborn.html)[Innioasis Y2 install guides](y2.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
