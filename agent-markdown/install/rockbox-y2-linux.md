---
title: "Install Rockbox on Innioasis Y2 on Linux | Linux install guide"
description: "Step-by-step Rockbox Y2 Linux install guide. Music-first custom firmware with a tag database, gapless playback, EQ, themes and plugins. Includes Linux setup, Updater CE steps, drivers, troubleshooting and the stock restore path. People also search for Rockbox-Y1, Rockbox-Y2, Rockbox for Y1, Rockbox for Y2; this is the same Rockbox install."
language: "en"
source: "https://innioasis.app/install/rockbox-y2-linux.html"
---

# Install Rockbox on Innioasis Y2 on Linux | Linux install guide

[Home](../index.html)/[Install guides](index.html)/[Rockbox](rockbox.html)/[Innioasis Y2](y2.html)/Linux guide

Rockbox · Innioasis Y2 · Linux

# Install Rockbox on Innioasis Y2 on Linux

Music-first custom firmware with a tag database, gapless playback, EQ, themes and plugins. This Linux tutorial is for the Innioasis Y2 only. People also search for Rockbox-Y1, Rockbox-Y2, Rockbox for Y1, Rockbox for Y2; this is the same Rockbox install.[Get Updater CE](../guide.html#linux)[All Rockbox platforms](rockbox.html)[Innioasis Y2 install guides](y2.html)[Open in Updater](../firmware.html?model=Y2&software=rockbox-y2)Your computer[Windows](rockbox-y2-windows.html)[macOS](rockbox-y2-mac.html)[Linux](rockbox-y2-linux.html)[All platforms](index.html)

## Before you start
  - Player: Innioasis Y2. Check the model printed on the player; Rockbox packages for another model will not work.
  - Computer: Linux. The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed.
  - Cable: a USB cable that carries data, not a charge-only cable.
  - Power: charge the player to at least half before you begin.
  - Backup: Use the build for this exact model. Rockbox-Y1 and Rockbox-Y2 are separate packages. On a Y1, check whether the player is Type A or Type B before you pick the asset.

## Prepare Linux for the install
  - Download `UpdaterCE.AppImage`, make it executable with `chmod +x UpdaterCE.AppImage`, and run it. The current AppImage targets Intel/AMD x86_64 systems.
  - If the AppImage does not start on Ubuntu 22.04 or newer, install `libfuse2` with your package manager. On Ubuntu 24.04 the package is `libfuse2t64`. Do not run the app as root.
  - If Updater CE cannot open the player, add the MediaTek USB permission rule: save `SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"` as `/etc/udev/rules.d/51-innioasis.rules`, then run `sudo udevadm control --reload && sudo udevadm trigger`. Add your user to `plugdev` if needed.

The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed. [Full Linux setup notes](../drivers.html#linux).

## Install Rockbox on Innioasis Y2 on Linux
  - Get Updater CE ready: Install Innioasis Updater CE on a Linux computer and open it. The Linux setup is covered above; the [main guide](../guide.html#linux) has the download links.
  - Select Innioasis Y2: In Device Model, choose Innioasis Y2. Do not substitute another model, even when the software name is the same.
  - Choose Rockbox: In Software, choose Rockbox. Use the build for this exact model. Rockbox-Y1 and Rockbox-Y2 are separate packages. On a Y1, check whether the player is Type A or Type B before you pick the asset.
  - Choose a release: Choose the newest stable release shown for this model. Nightly and pre-release builds are for testing; tick the nightly-builds option only if you need one. Read the release note for the Innioasis Y2 before you continue.
  - Install / Restore: Click Install / Restore. Power the player fully off, then connect it only when Updater CE asks. Run `lsusb` in another terminal to see the MediaTek vendor ID `0e8d` appear briefly.
  - Finish and check: Leave the player and cable alone until Updater CE shows success. On first start, let Rockbox scan the microSD card. Themes and settings live on the card, so keep a copy before you change cards.
  - Keep the way back: Restore Original Software for the same model if you want the stock player back. The stock package is always available from the [software archive](../firmware.html?model=Y2).

## If the install does not work
  - Permission denied or cannot open the USB port: the udev rule is missing or your user is not in `plugdev`. Add both, unplug the player, and reconnect.
  - The AppImage will not launch: check `chmod +x`, install `libfuse2` or `libfuse2t64`, and confirm you are on x86_64. A blank window under Wayland usually means trying an X11 session.
  - The player is not detected: use a data cable and a direct port, avoid hubs, and connect only at the prompt. Check `lsusb` while the player is plugged in.
  - Wrong package or model: return to Device Model and confirm the printed model. On a Y1, confirm Type A or Type B before choosing the asset again.
  - The player stopped responding: do not keep reconnecting. Read the [recovery guide](../guides/recovery.html) and the [troubleshooting guide](../troubleshooting.html) before trying a manual flash.

For a manual recovery on Innioasis Y2, use the files and scatter file that match the model. [SP Flash Tool notes](../sp-flash-tool.html).

## Going back to Original Software

Restore Original Software for the same model if you want the stock player back. The stock restore uses the same Updater CE flow: choose Innioasis Y2, choose Original Software, pick a stable release and run Install / Restore.[Open the Innioasis Y2 stock restore](../firmware.html?model=Y2&software=original-y2)[Recovery guide](../guides/recovery.html)

## Questions people askCan I install Rockbox on Innioasis Y2 on Linux?

Yes. This page is the Linux guide for Rockbox on the Innioasis Y2. Install Updater CE, select the model, choose the project and follow the install prompt.Do I need a driver on Linux?

No proprietary driver is needed, but your user needs the udev permission rule for vendor ID `0e8d` before Updater CE can open the player.Will this erase my music?

Use the build for this exact model. Rockbox-Y1 and Rockbox-Y2 are separate packages. On a Y1, check whether the player is Type A or Type B before you pick the asset. Files on the microSD card are normally left alone, but remove the card first if you want to be certain.Is Rockbox-Y1 the same as Rockbox?

Yes. Rockbox-Y1 is one of the names people use for Rockbox. This guide covers the same project on the Innioasis Y2.Does Rockbox work on other models?

This project is listed for Innioasis Y1. Use the model-specific guide for each player. Never install a package built for another model.How do I undo the install?

Restore Original Software for the same model if you want the stock player back. Open the [software archive](../firmware.html?model=Y2) or the model restore guide for the exact steps.What if the player is not detected?

Start with the Linux checklist above, then read the [troubleshooting guide](../troubleshooting.html). A data cable, a direct USB port and connecting only at the prompt fix most connection problems.

## Install this on another computer

### Windows install guide

Rockbox on Windows for the Innioasis Y2.[Windows guide](rockbox-y2-windows.html)

### macOS install guide

Rockbox on macOS for the Innioasis Y2.[macOS guide](rockbox-y2-mac.html)[All Rockbox guides](rockbox.html)[Innioasis Y2 install guides](y2.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
