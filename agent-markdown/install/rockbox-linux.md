---
title: "Install Rockbox on Linux | Linux install guide"
description: "How to install Rockbox on Linux for every supported Innioasis and Timmkoo model. Music-first custom firmware with a tag database, gapless playback, EQ, themes and plugins. Choose the model first, then follow the Linux Updater CE steps."
language: "en"
source: "https://innioasis.app/install/rockbox-linux.html"
---

# Install Rockbox on Linux | Linux install guide

[Home](../index.html)/[Install guides](index.html)/[Linux](linux.html)/Rockbox

Rockbox · Linux

# Install Rockbox on Linux

Music-first custom firmware with a tag database, gapless playback, EQ, themes and plugins. These Linux guides cover every model the project supports. People also search for Rockbox-Y1, Rockbox-Y2, Rockbox for Y1, Rockbox for Y2; this is the same Rockbox install.[Get Updater CE for Linux](../guide.html#linux)[Linux install guides](linux.html)[Linux USB permission notes](../drivers.html#linux)Your computer[Windows](rockbox-windows.html)[macOS](rockbox-mac.html)[Linux](rockbox-linux.html)[All platforms](index.html)

## Prepare Linux for the install
  - Download `UpdaterCE.AppImage`, make it executable with `chmod +x UpdaterCE.AppImage`, and run it. The current AppImage targets Intel/AMD x86_64 systems.
  - If the AppImage does not start on Ubuntu 22.04 or newer, install `libfuse2` with your package manager. On Ubuntu 24.04 the package is `libfuse2t64`. Do not run the app as root.
  - If Updater CE cannot open the player, add the MediaTek USB permission rule: save `SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"` as `/etc/udev/rules.d/51-innioasis.rules`, then run `sudo udevadm control --reload && sudo udevadm trigger`. Add your user to `plugdev` if needed.

The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed. [Full Linux setup notes](../drivers.html#linux).

## Choose your model

Y1

### Rockbox on Innioasis Y1

A music-first custom Software with deep playback and theme options.[Linux guide](rockbox-y1-linux.html)[Model guides](y1.html)

Y2

### Rockbox on Innioasis Y2

The Y2 Rockbox build. Select Y2 before choosing this Software.[Linux guide](rockbox-y2-linux.html)[Model guides](y2.html)

## How the install works
  - Install Updater CE on Linux using the steps above.
  - Select the model printed on the player, then choose Rockbox.
  - Choose a stable release listed for that model.
  - Click Install / Restore, power the player off and connect it at the prompt.
  - Wait for success. On first start, let Rockbox scan the microSD card. Themes and settings live on the card, so keep a copy before you change cards.

## Questions people askWhich Rockbox package should I download on Linux?

Use Innioasis Updater CE and select the model first. The app downloads the package from the project's official release. If you download manually, use the ZIP that names the model and, on a Y1, the correct Type A or Type B asset.Does Rockbox work on every model?

This project is listed for Innioasis Y1, Innioasis Y2. Open the model card for the exact guide.Is Rockbox-Y1 the same as Rockbox?

Yes. Rockbox-Y1, Rockbox-Y2, Rockbox for Y1 are names people use for the same project.Do I need a driver?

No proprietary driver, but the udev rule for vendor ID 0e8d and your user in plugdev are required.Can I undo it?

Restore Original Software for the same model if you want the stock player back.

## Other platforms[Windows](rockbox-windows.html)[macOS](rockbox-mac.html)[All Rockbox guides](rockbox.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
