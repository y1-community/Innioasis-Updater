---
title: "Install Inniclassic (iPod Classic interface) on Innioasis Y1 with a Mac | macOS install guide"
description: "Step-by-step Inniclassic Y1 macOS install guide. An iPod Classic-style interface for the Innioasis Y1 and Y2. Includes macOS setup, Updater CE steps, drivers, troubleshooting and the stock restore path. People also search for InniClassic, Inni Classic, iPod Classic firmware, Classic Y1; this is the same Inniclassic install."
language: "en"
source: "https://innioasis.app/install/inniclassic-y1-mac.html"
---

# Install Inniclassic (iPod Classic interface) on Innioasis Y1 with a Mac | macOS install guide

[Home](../index.html)/[Install guides](index.html)/[Inniclassic](inniclassic.html)/[Innioasis Y1](y1.html)/macOS guide

Inniclassic · Innioasis Y1 · macOS

# Install Inniclassic (iPod Classic interface) on Innioasis Y1 with a Mac

An iPod Classic-style interface for the Innioasis Y1 and Y2. This macOS tutorial is for the Innioasis Y1 only. People also search for InniClassic, Inni Classic, iPod Classic firmware, Classic Y1; this is the same Inniclassic install.[Get Updater CE](../guide.html#macos)[All Inniclassic platforms](inniclassic.html)[Innioasis Y1 install guides](y1.html)[Open in Updater](../firmware.html?model=Y1&software=inniclassic-y1)Your computer[Windows](inniclassic-y1-windows.html)[macOS](inniclassic-y1-mac.html)[Linux](inniclassic-y1-linux.html)[All platforms](index.html)

## Before you start
  - Player: Innioasis Y1. Check the model printed on the player; Inniclassic packages for another model will not work.
  - Computer: macOS. Intel and Apple Silicon Macs are supported. The current guide targets macOS Monterey (12.0) or later.
  - Cable: a USB cable that carries data, not a charge-only cable.
  - Power: charge the player to at least half before you begin.
  - Backup: The Y1 and Y2 builds come from separate release lines. Never cross-flash them, and pick the Type B asset if you have an early Y1.
Check the Y1 hardware type.Y1 players shipped in two hardware revisions. Players that shipped with software 2.0.0 or later are Type A; earlier units are Type B. Pick the matching asset in Updater CE.

## Prepare macOS for the install
  - Download the macOS disk image (`Innioasis.Updater.for.Mac.dmg`), open it, and drag Innioasis Updater CE into Applications.
  - The first launch is blocked by Gatekeeper until you approve it. Right-click the app and choose Open, or open System Settings → Privacy & Security and click Open Anyway. Do not disable Gatekeeper for the whole Mac.
  - No separate USB driver is needed. Connect the player directly to the Mac, not through an unpowered hub; some USB-C adapters drop the connection during a flash.

Intel and Apple Silicon Macs are supported. The current guide targets macOS Monterey (12.0) or later. [Full macOS setup notes](../drivers.html#macos).

## Install Inniclassic on Innioasis Y1 with a Mac
  - Get Updater CE ready: Install Innioasis Updater CE on a Mac and open it. The macOS setup is covered above; the [main guide](../guide.html#macos) has the download links.
  - Select Innioasis Y1: In Device Model, choose Innioasis Y1. Do not substitute another model, even when the software name is the same.
  - Choose Inniclassic: In Software, choose Inniclassic. The Y1 and Y2 builds come from separate release lines. Never cross-flash them, and pick the Type B asset if you have an early Y1.
  - Choose a release: Choose the newest stable release shown for this model. Nightly and pre-release builds are for testing; tick the nightly-builds option only if you need one. Read the release note for the Innioasis Y1 before you continue.
  - Install / Restore: Click Install / Restore. Power the player fully off and connect it only when Updater CE prompts. To confirm the Mac sees it, open System Information → USB, or run `system_profiler SPUSBDataType` in Terminal and look for a brief MediaTek entry.
  - Finish and check: Leave the player and cable alone until Updater CE shows success. The first boot may take longer while the library indexes. Let the scan finish before you judge performance.
  - Keep the way back: Restore Original Software for the same model if you want the stock interface back. The stock package is always available from the [software archive](../firmware.html?model=Y1).

## If the install does not work
  - macOS says the app is damaged or cannot be opened: that is quarantine, not a corrupt download. Approve it in System Settings → Privacy & Security with Open Anyway.
  - The player disconnects during the install: use a direct port, keep the Mac awake, and avoid hubs or adapters. Reconnect only when Updater CE asks.
  - SP Flash Tool is not available on macOS. Updater CE uses the MTKClient route on a Mac; for manual SP Flash Tool recovery, use a Windows or Linux computer.
  - Wrong package or model: return to Device Model and confirm the printed model. On a Y1, confirm Type A or Type B before choosing the asset again.
  - The player stopped responding: do not keep reconnecting. Read the [recovery guide](../guides/recovery.html) and the [troubleshooting guide](../troubleshooting.html) before trying a manual flash.

For a manual recovery on Innioasis Y1, use the files and scatter file that match the model. [SP Flash Tool notes](../sp-flash-tool.html).

## Going back to Original Software

Restore Original Software for the same model if you want the stock interface back. The stock restore uses the same Updater CE flow: choose Innioasis Y1, choose Original Software, pick a stable release and run Install / Restore.[Open the Innioasis Y1 stock restore](../firmware.html?model=Y1&software=original-y1)[Recovery guide](../guides/recovery.html)

## Questions people askCan I install Inniclassic on Innioasis Y1 on macOS?

Yes. This page is the macOS guide for Inniclassic on the Innioasis Y1. Install Updater CE, select the model, choose the project and follow the install prompt.Do I need a driver on macOS?

No separate driver is needed. macOS includes the USB support, and the app uses the MTKClient route on a Mac.Will this erase my music?

The Y1 and Y2 builds come from separate release lines. Never cross-flash them, and pick the Type B asset if you have an early Y1. Files on the microSD card are normally left alone, but remove the card first if you want to be certain.Is InniClassic the same as Inniclassic?

Yes. InniClassic is one of the names people use for Inniclassic. This guide covers the same project on the Innioasis Y1.Does Inniclassic work on other models?

This project is listed for Innioasis Y2. Use the model-specific guide for each player. Never install a package built for another model.How do I undo the install?

Restore Original Software for the same model if you want the stock interface back. Open the [software archive](../firmware.html?model=Y1) or the model restore guide for the exact steps.What if the player is not detected?

Start with the macOS checklist above, then read the [troubleshooting guide](../troubleshooting.html). A data cable, a direct USB port and connecting only at the prompt fix most connection problems.

## Install this on another computer

### Windows install guide

Inniclassic on Windows for the Innioasis Y1.[Windows guide](inniclassic-y1-windows.html)

### Linux install guide

Inniclassic on Linux for the Innioasis Y1.[Linux guide](inniclassic-y1-linux.html)[All Inniclassic guides](inniclassic.html)[Innioasis Y1 install guides](y1.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
