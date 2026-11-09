---
title: "Install Better-Y on Innioasis Y1 on Linux | Linux install guide"
description: "Step-by-step Better-Y Y1 Linux install guide. A polished stock-based Y1 system with metadata fixes, caching and Now Playing controls. Includes Linux setup, Updater CE steps, drivers, troubleshooting and the stock restore path. People also search for Better Y, BetterY, Better-Y Y1; this is the same Better-Y install."
language: "en"
source: "https://innioasis.app/install/better-y-y1-linux.html"
---

# Install Better-Y on Innioasis Y1 on Linux | Linux install guide

[Home](../index.html)/[Install guides](index.html)/[Better-Y](better-y.html)/[Innioasis Y1](y1.html)/Linux guide

Better-Y · Innioasis Y1 · Linux

# Install Better-Y on Innioasis Y1 on Linux

A polished stock-based Y1 system with metadata fixes, caching and Now Playing controls. This Linux tutorial is for the Innioasis Y1 only. People also search for Better Y, BetterY, Better-Y Y1; this is the same Better-Y install.[Get Updater CE](../guide.html#linux)[All Better-Y platforms](better-y.html)[Innioasis Y1 install guides](y1.html)[Open in Updater](../firmware.html?model=Y1&software=better-y-y1)Your computer[Windows](better-y-y1-windows.html)[macOS](better-y-y1-mac.html)[Linux](better-y-y1-linux.html)[All platforms](index.html)

## Before you start
  - Player: Innioasis Y1. Check the model printed on the player; Better-Y packages for another model will not work.
  - Computer: Linux. The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed.
  - Cable: a USB cable that carries data, not a charge-only cable.
  - Power: charge the player to at least half before you begin.
  - Backup: Better-Y releases are Y1 Type A packages. Do not flash them on a Type B Y1; use Rockbox-Y1 Type B for early units.
Check the Y1 hardware type.Better-Y is a Type A build. If your Y1 is Type B, use the Rockbox-Y1 Type B route instead.

## Prepare Linux for the install
  - Download `UpdaterCE.AppImage`, make it executable with `chmod +x UpdaterCE.AppImage`, and run it. The current AppImage targets Intel/AMD x86_64 systems.
  - If the AppImage does not start on Ubuntu 22.04 or newer, install `libfuse2` with your package manager. On Ubuntu 24.04 the package is `libfuse2t64`. Do not run the app as root.
  - If Updater CE cannot open the player, add the MediaTek USB permission rule: save `SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"` as `/etc/udev/rules.d/51-innioasis.rules`, then run `sudo udevadm control --reload && sudo udevadm trigger`. Add your user to `plugdev` if needed.

The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed. [Full Linux setup notes](../drivers.html#linux).

## Install Better-Y on Innioasis Y1 on Linux
  - Get Updater CE ready: Install Innioasis Updater CE on a Linux computer and open it. The Linux setup is covered above; the [main guide](../guide.html#linux) has the download links.
  - Select Innioasis Y1: In Device Model, choose Innioasis Y1. Do not substitute another model, even when the software name is the same.
  - Choose Better-Y: In Software, choose Better-Y. Better-Y releases are Y1 Type A packages. Do not flash them on a Type B Y1; use Rockbox-Y1 Type B for early units.
  - Choose a release: Choose the newest stable release shown for this model. Nightly and pre-release builds are for testing; tick the nightly-builds option only if you need one. Read the release note for the Innioasis Y1 before you continue.
  - Install / Restore: Click Install / Restore. Power the player fully off, then connect it only when Updater CE asks. Run `lsusb` in another terminal to see the MediaTek vendor ID `0e8d` appear briefly.
  - Finish and check: Leave the player and cable alone until Updater CE shows success. No extra setup is needed for the core features. Check the release notes for the stock version it builds on.
  - Keep the way back: Restore Original Software for Y1 if you want the stock software back. The stock package is always available from the [software archive](../firmware.html?model=Y1).

## If the install does not work
  - Permission denied or cannot open the USB port: the udev rule is missing or your user is not in `plugdev`. Add both, unplug the player, and reconnect.
  - The AppImage will not launch: check `chmod +x`, install `libfuse2` or `libfuse2t64`, and confirm you are on x86_64. A blank window under Wayland usually means trying an X11 session.
  - The player is not detected: use a data cable and a direct port, avoid hubs, and connect only at the prompt. Check `lsusb` while the player is plugged in.
  - Wrong package or model: return to Device Model and confirm the printed model. On a Y1, confirm Type A or Type B before choosing the asset again.
  - The player stopped responding: do not keep reconnecting. Read the [recovery guide](../guides/recovery.html) and the [troubleshooting guide](../troubleshooting.html) before trying a manual flash.

For a manual recovery on Innioasis Y1, use the files and scatter file that match the model. [SP Flash Tool notes](../sp-flash-tool.html).

## Going back to Original Software

Restore Original Software for Y1 if you want the stock software back. The stock restore uses the same Updater CE flow: choose Innioasis Y1, choose Original Software, pick a stable release and run Install / Restore.[Open the Innioasis Y1 stock restore](../firmware.html?model=Y1&software=original-y1)[Recovery guide](../guides/recovery.html)

## Questions people askCan I install Better-Y on Innioasis Y1 on Linux?

Yes. This page is the Linux guide for Better-Y on the Innioasis Y1. Install Updater CE, select the model, choose the project and follow the install prompt.Do I need a driver on Linux?

No proprietary driver is needed, but your user needs the udev permission rule for vendor ID `0e8d` before Updater CE can open the player.Will this erase my music?

Better-Y releases are Y1 Type A packages. Do not flash them on a Type B Y1; use Rockbox-Y1 Type B for early units. Files on the microSD card are normally left alone, but remove the card first if you want to be certain.Is Better Y the same as Better-Y?

Yes. Better Y is one of the names people use for Better-Y. This guide covers the same project on the Innioasis Y1.Does Better-Y work on other models?

This project is listed only for the Innioasis Y1 in the current catalogue. Never install a package built for another model.How do I undo the install?

Restore Original Software for Y1 if you want the stock software back. Open the [software archive](../firmware.html?model=Y1) or the model restore guide for the exact steps.What if the player is not detected?

Start with the Linux checklist above, then read the [troubleshooting guide](../troubleshooting.html). A data cable, a direct USB port and connecting only at the prompt fix most connection problems.

## Install this on another computer

### Windows install guide

Better-Y on Windows for the Innioasis Y1.[Windows guide](better-y-y1-windows.html)

### macOS install guide

Better-Y on macOS for the Innioasis Y1.[macOS guide](better-y-y1-mac.html)[All Better-Y guides](better-y.html)[Innioasis Y1 install guides](y1.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
