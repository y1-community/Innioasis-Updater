---
title: "Install Rondo on Innioasis Y1 with a Mac | macOS install guide"
description: "Step-by-step Rondo Y1 macOS install guide. A lightweight custom audio system for the Y1 with iPod-style click-wheel menus. Includes macOS setup, Updater CE steps, drivers, troubleshooting and the stock restore path. People also search for Rondo Y1, Rondo firmware, Rondo music player; this is the same Rondo install."
language: "en"
source: "https://innioasis.app/install/rondo-y1-mac.html"
---

# Install Rondo on Innioasis Y1 with a Mac | macOS install guide

[Home](../index.html)/[Install guides](index.html)/[Rondo](rondo.html)/[Innioasis Y1](y1.html)/macOS guide

Rondo · Innioasis Y1 · macOS

# Install Rondo on Innioasis Y1 with a Mac

A lightweight custom audio system for the Y1 with iPod-style click-wheel menus. This macOS tutorial is for the Innioasis Y1 only. People also search for Rondo Y1, Rondo firmware, Rondo music player; this is the same Rondo install.[Get Updater CE](../guide.html#macos)[All Rondo platforms](rondo.html)[Innioasis Y1 install guides](y1.html)[Open in Updater](../firmware.html?model=Y1&software=rondo-y1)Your computer[Windows](rondo-y1-windows.html)[macOS](rondo-y1-mac.html)[Linux](rondo-y1-linux.html)[All platforms](index.html)

## Before you start
  - Player: Innioasis Y1. Check the model printed on the player; Rondo packages for another model will not work.
  - Computer: macOS. Intel and Apple Silicon Macs are supported. The current guide targets macOS Monterey (12.0) or later.
  - Cable: a USB cable that carries data, not a charge-only cable.
  - Power: charge the player to at least half before you begin.
  - Backup: Rondo is for the Y1 Type A only (players that shipped with software 2.0.0 or later). Do not install it on a Type B Y1 or a Y2.
Check the Y1 hardware type.Y1 players shipped in two hardware revisions. Players that shipped with software 2.0.0 or later are Type A; earlier units are Type B. Pick the matching asset in Updater CE.

## Prepare macOS for the install
  - Download the macOS disk image (`Innioasis.Updater.for.Mac.dmg`), open it, and drag Innioasis Updater CE into Applications.
  - The first launch is blocked by Gatekeeper until you approve it. Right-click the app and choose Open, or open System Settings → Privacy & Security and click Open Anyway. Do not disable Gatekeeper for the whole Mac.
  - No separate USB driver is needed. Connect the player directly to the Mac, not through an unpowered hub; some USB-C adapters drop the connection during a flash.

Intel and Apple Silicon Macs are supported. The current guide targets macOS Monterey (12.0) or later. [Full macOS setup notes](../drivers.html#macos).

## Install Rondo on Innioasis Y1 with a Mac
  - Get Updater CE ready: Install Innioasis Updater CE on a Mac and open it. The macOS setup is covered above; the [main guide](../guide.html#macos) has the download links.
  - Select Innioasis Y1: In Device Model, choose Innioasis Y1. Do not substitute another model, even when the software name is the same.
  - Choose Rondo: In Software, choose Rondo. Rondo is for the Y1 Type A only (players that shipped with software 2.0.0 or later). Do not install it on a Type B Y1 or a Y2.
  - Choose a release: Choose the newest stable release shown for this model. Nightly and pre-release builds are for testing; tick the nightly-builds option only if you need one. Read the release note for the Innioasis Y1 before you continue.
  - Install / Restore: Click Install / Restore. Power the player fully off and connect it only when Updater CE prompts. To confirm the Mac sees it, open System Information → USB, or run `system_profiler SPUSBDataType` in Terminal and look for a brief MediaTek entry.
  - Finish and check: Leave the player and cable alone until Updater CE shows success. The first start takes a couple of minutes. For YouTube Music and YouTube, set up a Rondo server; the card, radio and Bluetooth work without one.
  - Keep the way back: Restore Original Software for Y1 if you want the stock player back. The stock package is always available from the [software archive](../firmware.html?model=Y1).

## If the install does not work
  - macOS says the app is damaged or cannot be opened: that is quarantine, not a corrupt download. Approve it in System Settings → Privacy & Security with Open Anyway.
  - The player disconnects during the install: use a direct port, keep the Mac awake, and avoid hubs or adapters. Reconnect only when Updater CE asks.
  - SP Flash Tool is not available on macOS. Updater CE uses the MTKClient route on a Mac; for manual SP Flash Tool recovery, use a Windows or Linux computer.
  - Wrong package or model: return to Device Model and confirm the printed model. On a Y1, confirm Type A or Type B before choosing the asset again.
  - The player stopped responding: do not keep reconnecting. Read the [recovery guide](../guides/recovery.html) and the [troubleshooting guide](../troubleshooting.html) before trying a manual flash.

For a manual recovery on Innioasis Y1, use the files and scatter file that match the model. [SP Flash Tool notes](../sp-flash-tool.html).

## Going back to Original Software

Restore Original Software for Y1 if you want the stock player back. The stock restore uses the same Updater CE flow: choose Innioasis Y1, choose Original Software, pick a stable release and run Install / Restore.[Open the Innioasis Y1 stock restore](../firmware.html?model=Y1&software=original-y1)[Recovery guide](../guides/recovery.html)

## Questions people askCan I install Rondo on Innioasis Y1 on macOS?

Yes. This page is the macOS guide for Rondo on the Innioasis Y1. Install Updater CE, select the model, choose the project and follow the install prompt.Do I need a driver on macOS?

No separate driver is needed. macOS includes the USB support, and the app uses the MTKClient route on a Mac.Will this erase my music?

Rondo is for the Y1 Type A only (players that shipped with software 2.0.0 or later). Do not install it on a Type B Y1 or a Y2. Files on the microSD card are normally left alone, but remove the card first if you want to be certain.Is Rondo Y1 the same as Rondo?

Yes. Rondo Y1 is one of the names people use for Rondo. This guide covers the same project on the Innioasis Y1.Does Rondo work on other models?

This project is listed only for the Innioasis Y1 in the current catalogue. Never install a package built for another model.How do I undo the install?

Restore Original Software for Y1 if you want the stock player back. Open the [software archive](../firmware.html?model=Y1) or the model restore guide for the exact steps.What if the player is not detected?

Start with the macOS checklist above, then read the [troubleshooting guide](../troubleshooting.html). A data cable, a direct USB port and connecting only at the prompt fix most connection problems.

## Install this on another computer

### Windows install guide

Rondo on Windows for the Innioasis Y1.[Windows guide](rondo-y1-windows.html)

### Linux install guide

Rondo on Linux for the Innioasis Y1.[Linux guide](rondo-y1-linux.html)[All Rondo guides](rondo.html)[Innioasis Y1 install guides](y1.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
