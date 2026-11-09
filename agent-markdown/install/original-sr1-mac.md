---
title: "Restore Original Software (stock firmware) on Innioasis SR1 with a Mac | macOS install guide"
description: "Step-by-step Original Software SR1 macOS install guide. The factory system image from Innioasis or Timmkoo, used to undo a custom install or recover a player that will not boot. Includes macOS setup, Updater CE steps, drivers, troubleshooting and the stock restore path. People also search for stock firmware, factory firmware, stock ROM, original firmware; this is the same Original Software install."
language: "en"
source: "https://innioasis.app/install/original-sr1-mac.html"
---

# Restore Original Software (stock firmware) on Innioasis SR1 with a Mac | macOS install guide

[Home](../index.html)/[Install guides](index.html)/[Original Software](original-software.html)/[Innioasis SR1](sr1.html)/macOS guide

Original Software · Innioasis SR1 · macOS

# Restore Original Software (stock firmware) on Innioasis SR1 with a Mac

The factory system image from Innioasis or Timmkoo, used to undo a custom install or recover a player that will not boot. This macOS tutorial is for the Innioasis SR1 only. People also search for stock firmware, factory firmware, stock ROM, original firmware; this is the same Original Software install.[Get Updater CE](../guide.html#macos)[All Original Software platforms](original-software.html)[Innioasis SR1 install guides](sr1.html)[Open in Updater](../firmware.html?model=SR1&software=original-sr1)Your computer[Windows](original-sr1-windows.html)[macOS](original-sr1-mac.html)[Linux](original-sr1-linux.html)[All platforms](index.html)

## Before you start
  - Player: Innioasis SR1. Check the model printed on the player; Original Software packages for another model will not work.
  - Computer: macOS. Intel and Apple Silicon Macs are supported. The current guide targets macOS Monterey (12.0) or later.
  - Cable: a USB cable that carries data, not a charge-only cable.
  - Power: charge the player to at least half before you begin.
  - Backup: Back up music and recordings first. A stock restore replaces the system and can wipe internal storage; the microSD card is normally left alone.

## Prepare macOS for the install
  - Download the macOS disk image (`Innioasis.Updater.for.Mac.dmg`), open it, and drag Innioasis Updater CE into Applications.
  - The first launch is blocked by Gatekeeper until you approve it. Right-click the app and choose Open, or open System Settings → Privacy & Security and click Open Anyway. Do not disable Gatekeeper for the whole Mac.
  - No separate USB driver is needed. Connect the player directly to the Mac, not through an unpowered hub; some USB-C adapters drop the connection during a flash.

Intel and Apple Silicon Macs are supported. The current guide targets macOS Monterey (12.0) or later. [Full macOS setup notes](../drivers.html#macos).

## Restore Original Software on Innioasis SR1 with a Mac
  - Get Updater CE ready: Install Innioasis Updater CE on a Mac and open it. The macOS setup is covered above; the [main guide](../guide.html#macos) has the download links.
  - Select Innioasis SR1: In Device Model, choose Innioasis SR1. Do not substitute another model, even when the software name is the same.
  - Choose Original Software: In Software, choose Original Software. Back up music and recordings first. A stock restore replaces the system and can wipe internal storage; the microSD card is normally left alone.
  - Choose a release: Choose the newest stable release shown for this model. Nightly and pre-release builds are for testing; tick the nightly-builds option only if you need one. Read the release note for the Innioasis SR1 before you continue.
  - Install / Restore: Click Install / Restore. Power the player fully off and connect it only when Updater CE prompts. To confirm the Mac sees it, open System Information → USB, or run `system_profiler SPUSBDataType` in Terminal and look for a brief MediaTek entry.
  - Finish and check: Leave the player and cable alone until Updater CE shows success. The first start can take a few minutes. Set the language, Wi-Fi and Bluetooth again if the restore cleared them.
  - Keep the way back: This is the restore path itself: choose Original Software for the model and run Install / Restore. The stock package is always available from the [software archive](../firmware.html?model=SR1).

## If the install does not work
  - macOS says the app is damaged or cannot be opened: that is quarantine, not a corrupt download. Approve it in System Settings → Privacy & Security with Open Anyway.
  - The player disconnects during the install: use a direct port, keep the Mac awake, and avoid hubs or adapters. Reconnect only when Updater CE asks.
  - SP Flash Tool is not available on macOS. Updater CE uses the MTKClient route on a Mac; for manual SP Flash Tool recovery, use a Windows or Linux computer.
  - Wrong package or model: return to Device Model and confirm the printed model. On a Y1, confirm Type A or Type B before choosing the asset again.
  - The player stopped responding: do not keep reconnecting. Read the [recovery guide](../guides/recovery.html) and the [troubleshooting guide](../troubleshooting.html) before trying a manual flash.

For a manual recovery on Innioasis SR1, use the files and scatter file that match the model. [SP Flash Tool notes](../sp-flash-tool.html).

## Going back to Original Software

This is the restore path itself: choose Original Software for the model and run Install / Restore. The stock restore uses the same Updater CE flow: choose Innioasis SR1, choose Original Software, pick a stable release and run Install / Restore.[Open the Innioasis SR1 stock restore](../firmware.html?model=SR1&software=original-sr1)[Recovery guide](../guides/recovery.html)

## Questions people askCan I restore Original Software on Innioasis SR1 on macOS?

Yes. This page is the macOS guide for Original Software on the Innioasis SR1. Install Updater CE, select the model, choose the project and follow the install prompt.Do I need a driver on macOS?

No separate driver is needed. macOS includes the USB support, and the app uses the MTKClient route on a Mac.Will this erase my music?

Back up music and recordings first. A stock restore replaces the system and can wipe internal storage; the microSD card is normally left alone. Files on the microSD card are normally left alone, but remove the card first if you want to be certain.Is stock firmware the same as Original Software?

Yes. stock firmware is one of the names people use for Original Software. This guide covers the same project on the Innioasis SR1.Does Original Software work on other models?

This project is listed for Innioasis / Timmkoo G1, Innioasis / Timmkoo G3, Innioasis / Timmkoo G5, Innioasis PR1, Innioasis / Timmkoo Q3, Innioasis / Timmkoo Q5, Innioasis R1, Innioasis Y1, Innioasis Y2. Use the model-specific guide for each player. Never install a package built for another model.How do I undo the install?

This is the restore path itself: choose Original Software for the model and run Install / Restore. Open the [software archive](../firmware.html?model=SR1) or the model restore guide for the exact steps.What if the player is not detected?

Start with the macOS checklist above, then read the [troubleshooting guide](../troubleshooting.html). A data cable, a direct USB port and connecting only at the prompt fix most connection problems.

## Install this on another computer

### Windows install guide

Original Software on Windows for the Innioasis SR1.[Windows guide](original-sr1-windows.html)

### Linux install guide

Original Software on Linux for the Innioasis SR1.[Linux guide](original-sr1-linux.html)[All Original Software guides](original-software.html)[Innioasis SR1 install guides](sr1.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
