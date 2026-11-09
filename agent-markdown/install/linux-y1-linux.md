---
title: "Install Linux for Y1 (Dev) on Innioasis Y1 on Linux | Linux install guide"
description: "Step-by-step Linux for Y1 (Dev) Y1 Linux install guide. A development Linux image for the Innioasis Y1. Includes Linux setup, Updater CE steps, drivers, troubleshooting and the stock restore path. People also search for Linux for Y1, Y1 Linux, Linux dev ROM; this is the same Linux for Y1 (Dev) install."
language: "en"
source: "https://innioasis.app/install/linux-y1-linux.html"
---

# Install Linux for Y1 (Dev) on Innioasis Y1 on Linux | Linux install guide

[Home](../index.html)/[Install guides](index.html)/[Linux for Y1 (Dev)](linux-dev.html)/[Innioasis Y1](y1.html)/Linux guide

Linux for Y1 (Dev) · Innioasis Y1 · Linux

# Install Linux for Y1 (Dev) on Innioasis Y1 on Linux

A development Linux image for the Innioasis Y1. This Linux tutorial is for the Innioasis Y1 only. People also search for Linux for Y1, Y1 Linux, Linux dev ROM; this is the same Linux for Y1 (Dev) install.[Get Updater CE](../guide.html#linux)[All Linux for Y1 (Dev) platforms](linux-dev.html)[Innioasis Y1 install guides](y1.html)[Open in Updater](../firmware.html?model=Y1&software=linux-y1)Your computer[Windows](linux-y1-windows.html)[macOS](linux-y1-mac.html)[Linux](linux-y1-linux.html)[All platforms](index.html)

## Before you start
  - Player: Innioasis Y1. Check the model printed on the player; Linux for Y1 (Dev) packages for another model will not work.
  - Computer: Linux. The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed.
  - Cable: a USB cable that carries data, not a charge-only cable.
  - Power: charge the player to at least half before you begin.
  - Backup: This is an early development build. Keep a stock restore ready and expect rough edges.
Check the Y1 hardware type.Y1 players shipped in two hardware revisions. Players that shipped with software 2.0.0 or later are Type A; earlier units are Type B. Pick the matching asset in Updater CE.

## Prepare Linux for the install
  - Download `UpdaterCE.AppImage`, make it executable with `chmod +x UpdaterCE.AppImage`, and run it. The current AppImage targets Intel/AMD x86_64 systems.
  - If the AppImage does not start on Ubuntu 22.04 or newer, install `libfuse2` with your package manager. On Ubuntu 24.04 the package is `libfuse2t64`. Do not run the app as root.
  - If Updater CE cannot open the player, add the MediaTek USB permission rule: save `SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"` as `/etc/udev/rules.d/51-innioasis.rules`, then run `sudo udevadm control --reload && sudo udevadm trigger`. Add your user to `plugdev` if needed.

The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed. [Full Linux setup notes](../drivers.html#linux).

## Install Linux for Y1 (Dev) on Innioasis Y1 on Linux
  - Get Updater CE ready: Install Innioasis Updater CE on a Linux computer and open it. The Linux setup is covered above; the [main guide](../guide.html#linux) has the download links.
  - Select Innioasis Y1: In Device Model, choose Innioasis Y1. Do not substitute another model, even when the software name is the same.
  - Choose Linux for Y1 (Dev): In Software, choose Linux for Y1 (Dev). This is an early development build. Keep a stock restore ready and expect rough edges.
  - Choose a release: Choose the newest stable release shown for this model. Nightly and pre-release builds are for testing; tick the nightly-builds option only if you need one. Read the release note for the Innioasis Y1 before you continue.
  - Install / Restore: Click Install / Restore. Power the player fully off, then connect it only when Updater CE asks. Run `lsusb` in another terminal to see the MediaTek vendor ID `0e8d` appear briefly.
  - Finish and check: Leave the player and cable alone until Updater CE shows success. Expect missing features and occasional instability. Reinstall Original Software when you finish testing.
  - Keep the way back: Restore Original Software for Y1 when you are done testing. The stock package is always available from the [software archive](../firmware.html?model=Y1).

## If the install does not work
  - Permission denied or cannot open the USB port: the udev rule is missing or your user is not in `plugdev`. Add both, unplug the player, and reconnect.
  - The AppImage will not launch: check `chmod +x`, install `libfuse2` or `libfuse2t64`, and confirm you are on x86_64. A blank window under Wayland usually means trying an X11 session.
  - The player is not detected: use a data cable and a direct port, avoid hubs, and connect only at the prompt. Check `lsusb` while the player is plugged in.
  - Wrong package or model: return to Device Model and confirm the printed model. On a Y1, confirm Type A or Type B before choosing the asset again.
  - The player stopped responding: do not keep reconnecting. Read the [recovery guide](../guides/recovery.html) and the [troubleshooting guide](../troubleshooting.html) before trying a manual flash.

For a manual recovery on Innioasis Y1, use the files and scatter file that match the model. [SP Flash Tool notes](../sp-flash-tool.html).

## Going back to Original Software

Restore Original Software for Y1 when you are done testing. The stock restore uses the same Updater CE flow: choose Innioasis Y1, choose Original Software, pick a stable release and run Install / Restore.[Open the Innioasis Y1 stock restore](../firmware.html?model=Y1&software=original-y1)[Recovery guide](../guides/recovery.html)

## Questions people askCan I install Linux for Y1 (Dev) on Innioasis Y1 on Linux?

Yes. This page is the Linux guide for Linux for Y1 (Dev) on the Innioasis Y1. Install Updater CE, select the model, choose the project and follow the install prompt.Do I need a driver on Linux?

No proprietary driver is needed, but your user needs the udev permission rule for vendor ID `0e8d` before Updater CE can open the player.Will this erase my music?

This is an early development build. Keep a stock restore ready and expect rough edges. Files on the microSD card are normally left alone, but remove the card first if you want to be certain.Is Linux for Y1 the same as Linux for Y1 (Dev)?

Yes. Linux for Y1 is one of the names people use for Linux for Y1 (Dev). This guide covers the same project on the Innioasis Y1.Does Linux for Y1 (Dev) work on other models?

This project is listed only for the Innioasis Y1 in the current catalogue. Never install a package built for another model.How do I undo the install?

Restore Original Software for Y1 when you are done testing. Open the [software archive](../firmware.html?model=Y1) or the model restore guide for the exact steps.What if the player is not detected?

Start with the Linux checklist above, then read the [troubleshooting guide](../troubleshooting.html). A data cable, a direct USB port and connecting only at the prompt fix most connection problems.

## Install this on another computer

### Windows install guide

Linux for Y1 (Dev) on Windows for the Innioasis Y1.[Windows guide](linux-y1-windows.html)

### macOS install guide

Linux for Y1 (Dev) on macOS for the Innioasis Y1.[macOS guide](linux-y1-mac.html)[All Linux for Y1 (Dev) guides](linux-dev.html)[Innioasis Y1 install guides](y1.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
