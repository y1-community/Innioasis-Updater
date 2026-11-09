---
title: "Install Koensayr on Linux | Linux install guide"
description: "How to install Koensayr on Linux for every supported Innioasis and Timmkoo model. A stock-derived Y1 patch that adds Artist-to-Album navigation and root while keeping the stock feel. Choose the model first, then follow the Linux Updater CE steps."
language: "en"
source: "https://innioasis.app/install/koensayr-linux.html"
---

# Install Koensayr on Linux | Linux install guide

[Home](../index.html)/[Install guides](index.html)/[Linux](linux.html)/Koensayr

Koensayr · Linux

# Install Koensayr on Linux

A stock-derived Y1 patch that adds Artist-to-Album navigation and root while keeping the stock feel. These Linux guides cover every model the project supports. People also search for Koensayr Y1, Koensayr Auto, Koensayr firmware; this is the same Koensayr install.[Get Updater CE for Linux](../guide.html#linux)[Linux install guides](linux.html)[Linux USB permission notes](../drivers.html#linux)Your computer[Windows](koensayr-windows.html)[macOS](koensayr-mac.html)[Linux](koensayr-linux.html)[All platforms](index.html)

## Prepare Linux for the install
  - Download `UpdaterCE.AppImage`, make it executable with `chmod +x UpdaterCE.AppImage`, and run it. The current AppImage targets Intel/AMD x86_64 systems.
  - If the AppImage does not start on Ubuntu 22.04 or newer, install `libfuse2` with your package manager. On Ubuntu 24.04 the package is `libfuse2t64`. Do not run the app as root.
  - If Updater CE cannot open the player, add the MediaTek USB permission rule: save `SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"` as `/etc/udev/rules.d/51-innioasis.rules`, then run `sudo udevadm control --reload && sudo udevadm trigger`. Add your user to `plugdev` if needed.

The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed. [Full Linux setup notes](../drivers.html#linux).

## Choose your model

Y1

### Koensayr on Innioasis Y1

A Y1 custom Software maintained by the community.[Linux guide](koensayr-y1-linux.html)[Model guides](y1.html)

## How the install works
  - Install Updater CE on Linux using the steps above.
  - Select the model printed on the player, then choose Koensayr.
  - Choose a stable release listed for that model.
  - Click Install / Restore, power the player off and connect it at the prompt.
  - Wait for success. Open the after-install notes for the extra patch options and the first-start checks.

## Questions people askWhich Koensayr package should I download on Linux?

Use Innioasis Updater CE and select the model first. The app downloads the package from the project's official release. If you download manually, use the ZIP that names the model and, on a Y1, the correct Type A or Type B asset.Does Koensayr work on every model?

This project is listed for Innioasis Y1. Open the model card for the exact guide.Is Koensayr Y1 the same as Koensayr?

Yes. Koensayr Y1, Koensayr Auto, Koensayr firmware are names people use for the same project.Do I need a driver?

No proprietary driver, but the udev rule for vendor ID 0e8d and your user in plugdev are required.Can I undo it?

Restore Original Software for Y1 if you want the untouched stock software back.

## Other platforms[Windows](koensayr-windows.html)[macOS](koensayr-mac.html)[All Koensayr guides](koensayr.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
