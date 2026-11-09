---
title: "Install Better-Y on Innioasis Y1 with a Mac | macOS install guide"
description: "Step-by-step Better-Y Y1 macOS install guide. A polished stock-based Y1 system with metadata fixes, caching and Now Playing controls. Includes macOS setup, Updater CE steps, drivers, troubleshooting and the stock restore path. People also search for Better Y, BetterY, Better-Y Y1; this is the same Better-Y install."
language: "en"
source: "https://innioasis.app/install/better-y-y1-mac.html"
---

# Install Better-Y on Innioasis Y1 with a Mac | macOS install guide

[Home](../index.html)/[Install guides](index.html)/[Better-Y](better-y.html)/[Innioasis Y1](y1.html)/macOS guide

Better-Y · Innioasis Y1 · macOS

# Install Better-Y on Innioasis Y1 with a Mac

A polished stock-based Y1 system with metadata fixes, caching and Now Playing controls. This macOS tutorial is for the Innioasis Y1 only. People also search for Better Y, BetterY, Better-Y Y1; this is the same Better-Y install.[Get Updater CE](../guide.html#macos)[All Better-Y platforms](better-y.html)[Innioasis Y1 install guides](y1.html)[Open in Updater](../firmware.html?model=Y1&software=better-y-y1)Your computer[Windows](better-y-y1-windows.html)[macOS](better-y-y1-mac.html)[Linux](better-y-y1-linux.html)[All platforms](index.html)

## Before you start
  - Player: Innioasis Y1. Check the model printed on the player; Better-Y packages for another model will not work.
  - Computer: macOS. Intel and Apple Silicon Macs are supported. The current guide targets macOS Monterey (12.0) or later.
  - Cable: a USB cable that carries data, not a charge-only cable.
  - Power: charge the player to at least half before you begin.
  - Backup: Better-Y releases are Y1 Type A packages. Do not flash them on a Type B Y1; use Rockbox-Y1 Type B for early units.
Check the Y1 hardware type.Better-Y is a Type A build. If your Y1 is Type B, use the Rockbox-Y1 Type B route instead.

## Prepare macOS for the install
  - Download the macOS disk image (`Innioasis.Updater.for.Mac.dmg`), open it, and drag Innioasis Updater CE into Applications.
  - The first launch is blocked by Gatekeeper until you approve it. Right-click the app and choose Open, or open System Settings → Privacy & Security and click Open Anyway. Do not disable Gatekeeper for the whole Mac.
  - No separate USB driver is needed. Connect the player directly to the Mac, not through an unpowered hub; some USB-C adapters drop the connection during a flash.

Intel and Apple Silicon Macs are supported. The current guide targets macOS Monterey (12.0) or later. [Full macOS setup notes](../drivers.html#macos).

## Install Better-Y on Innioasis Y1 with a Mac
  - Get Updater CE ready: Install Innioasis Updater CE on a Mac and open it. The macOS setup is covered above; the [main guide](../guide.html#macos) has the download links.
  - Select Innioasis Y1: In Device Model, choose Innioasis Y1. Do not substitute another model, even when the software name is the same.
  - Choose Better-Y: In Software, choose Better-Y. Better-Y releases are Y1 Type A packages. Do not flash them on a Type B Y1; use Rockbox-Y1 Type B for early units.
  - Choose a release: Choose the newest stable release shown for this model. Nightly and pre-release builds are for testing; tick the nightly-builds option only if you need one. Read the release note for the Innioasis Y1 before you continue.
  - Install / Restore: Click Install / Restore. Power the player fully off and connect it only when Updater CE prompts. To confirm the Mac sees it, open System Information → USB, or run `system_profiler SPUSBDataType` in Terminal and look for a brief MediaTek entry.
  - Finish and check: Leave the player and cable alone until Updater CE shows success. No extra setup is needed for the core features. Check the release notes for the stock version it builds on.
  - Keep the way back: Restore Original Software for Y1 if you want the stock software back. The stock package is always available from the [software archive](../firmware.html?model=Y1).

## If the install does not work
  - macOS says the app is damaged or cannot be opened: that is quarantine, not a corrupt download. Approve it in System Settings → Privacy & Security with Open Anyway.
  - The player disconnects during the install: use a direct port, keep the Mac awake, and avoid hubs or adapters. Reconnect only when Updater CE asks.
  - SP Flash Tool is not available on macOS. Updater CE uses the MTKClient route on a Mac; for manual SP Flash Tool recovery, use a Windows or Linux computer.
  - Wrong package or model: return to Device Model and confirm the printed model. On a Y1, confirm Type A or Type B before choosing the asset again.
  - The player stopped responding: do not keep reconnecting. Read the [recovery guide](../guides/recovery.html) and the [troubleshooting guide](../troubleshooting.html) before trying a manual flash.

For a manual recovery on Innioasis Y1, use the files and scatter file that match the model. [SP Flash Tool notes](../sp-flash-tool.html).

## Going back to Original Software

Restore Original Software for Y1 if you want the stock software back. The stock restore uses the same Updater CE flow: choose Innioasis Y1, choose Original Software, pick a stable release and run Install / Restore.[Open the Innioasis Y1 stock restore](../firmware.html?model=Y1&software=original-y1)[Recovery guide](../guides/recovery.html)

## Questions people askCan I install Better-Y on Innioasis Y1 on macOS?

Yes. This page is the macOS guide for Better-Y on the Innioasis Y1. Install Updater CE, select the model, choose the project and follow the install prompt.Do I need a driver on macOS?

No separate driver is needed. macOS includes the USB support, and the app uses the MTKClient route on a Mac.Will this erase my music?

Better-Y releases are Y1 Type A packages. Do not flash them on a Type B Y1; use Rockbox-Y1 Type B for early units. Files on the microSD card are normally left alone, but remove the card first if you want to be certain.Is Better Y the same as Better-Y?

Yes. Better Y is one of the names people use for Better-Y. This guide covers the same project on the Innioasis Y1.Does Better-Y work on other models?

This project is listed only for the Innioasis Y1 in the current catalogue. Never install a package built for another model.How do I undo the install?

Restore Original Software for Y1 if you want the stock software back. Open the [software archive](../firmware.html?model=Y1) or the model restore guide for the exact steps.What if the player is not detected?

Start with the macOS checklist above, then read the [troubleshooting guide](../troubleshooting.html). A data cable, a direct USB port and connecting only at the prompt fix most connection problems.

## Install this on another computer

### Windows install guide

Better-Y on Windows for the Innioasis Y1.[Windows guide](better-y-y1-windows.html)

### Linux install guide

Better-Y on Linux for the Innioasis Y1.[Linux guide](better-y-y1-linux.html)[All Better-Y guides](better-y.html)[Innioasis Y1 install guides](y1.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
