---
title: "Install Innioasis and Timmkoo software on Linux | OS-specific install guides"
description: "Every Innioasis and Timmkoo software install guide for Linux. Set up Updater CE, install the required driver or permissions, then follow the model-specific guide for Rockbox, Solar, Reborn, JJ Launcher and the stock restore."
language: "en"
source: "https://innioasis.app/install/linux.html"
---

# Install Innioasis and Timmkoo software on Linux | OS-specific install guides

[Home](../index.html)/[Install guides](index.html)/Linux

Install guides · Linux

# Install Innioasis and Timmkoo software on Linux

Set up Innioasis Updater CE on a Linux computer, then use the model-specific guide for the software you want. The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed.[Get Updater CE for Linux](../guide.html#linux)[Linux install guides](linux.html)[Linux USB permission notes](../drivers.html#linux)

## Prepare Linux for the install
  - Download `UpdaterCE.AppImage`, make it executable with `chmod +x UpdaterCE.AppImage`, and run it. The current AppImage targets Intel/AMD x86_64 systems.
  - If the AppImage does not start on Ubuntu 22.04 or newer, install `libfuse2` with your package manager. On Ubuntu 24.04 the package is `libfuse2t64`. Do not run the app as root.
  - If Updater CE cannot open the player, add the MediaTek USB permission rule: save `SUBSYSTEM=="usb", ATTR{idVendor}=="0e8d", MODE="0666", GROUP="plugdev"` as `/etc/udev/rules.d/51-innioasis.rules`, then run `sudo udevadm control --reload && sudo udevadm trigger`. Add your user to `plugdev` if needed.

The official AppImage is for Intel/AMD Linux. No Linux ARM build is listed. [Full Linux setup notes](../drivers.html#linux).

## Every software guide for Linux
[](original-y1-linux.html)[](original-y2-linux.html)[](original-g1-linux.html)[](original-g3-linux.html)[](original-g5-linux.html)[](original-r1-linux.html)[](original-pr1-linux.html)[](original-sr1-linux.html)[](original-q3-linux.html)[](original-q5-linux.html)[](original-software-linux.html)
[](reborn-y2linux-y2-linux.html)[](reborn-linux.html)
[](rondo-y1-linux.html)[](rondo-linux.html)
[](rockbox-y1-linux.html)[](rockbox-y2-linux.html)[](rockbox-linux.html)
[](solar-y1-linux.html)[](solar-y2-linux.html)[](solar-linux.html)
[](jj-launcher-y1-linux.html)[](jj-launcher-y2-linux.html)[](jj-launcher-linux.html)
[](inniclassic-y1-linux.html)[](inniclassic-y2-linux.html)[](inniclassic-linux.html)
[](y2player-y2-linux.html)[](y2player-linux.html)
[](koensayr-y1-linux.html)[](koensayr-linux.html)
[](better-y-y1-linux.html)[](better-y-linux.html)
[](android-4-2-y1-linux.html)[](android-4-4-y2-linux.html)[](android-dev-linux.html)
[](linux-y1-linux.html)[](linux-dev-linux.html)

| Software | Models | Linux guide |
| --- | --- | --- |
| Original SoftwareInnioasis Y1, Innioasis Y2, Innioasis / Timmkoo G1, Innioasis / Timmkoo G3, Innioasis / Timmkoo G5, Innioasis R1, Innioasis PR1, Innioasis SR1, Innioasis / Timmkoo Q3, Innioasis / Timmkoo Q5 | Innioasis Y1 · Innioasis Y2 · Innioasis / Timmkoo G1 · Innioasis / Timmkoo G3 · Innioasis / Timmkoo G5 · Innioasis R1 · Innioasis PR1 · Innioasis SR1 · Innioasis / Timmkoo Q3 · Innioasis / Timmkoo Q5 | Original Software guide |
| Reborn (Y2Linux)Innioasis Y2 | Innioasis Y2 | Reborn (Y2Linux) guide |
| RondoInnioasis Y1 | Innioasis Y1 | Rondo guide |
| RockboxInnioasis Y1, Innioasis Y2 | Innioasis Y1 · Innioasis Y2 | Rockbox guide |
| SolarInnioasis Y1, Innioasis Y2 | Innioasis Y1 · Innioasis Y2 | Solar guide |
| JJ LauncherInnioasis Y1, Innioasis Y2 | Innioasis Y1 · Innioasis Y2 | JJ Launcher guide |
| InniclassicInnioasis Y1, Innioasis Y2 | Innioasis Y1 · Innioasis Y2 | Inniclassic guide |
| Y2PlayerInnioasis Y2 | Innioasis Y2 | Y2Player guide |
| KoensayrInnioasis Y1 | Innioasis Y1 | Koensayr guide |
| Better-YInnioasis Y1 | Innioasis Y1 | Better-Y guide |
| Android development ROMInnioasis Y1, Innioasis Y2 | Innioasis Y1 · Innioasis Y2 | Android development ROM guide |
| Linux for Y1 (Dev)Innioasis Y1 | Innioasis Y1 | Linux for Y1 (Dev) guide |

## Choose your model

### Innioasis Y1

[Linux install guides](y1-linux.html)

### Innioasis Y2

[Linux install guides](y2-linux.html)

### Innioasis / Timmkoo G1

[Linux install guides](g1-linux.html)

### Innioasis / Timmkoo G3

[Linux install guides](g3-linux.html)

### Innioasis / Timmkoo G5

[Linux install guides](g5-linux.html)

### Innioasis A5

[Linux install guides](a5-linux.html)

### Innioasis D1

[Linux install guides](d1-linux.html)

### Innioasis / Timmkoo Q3

[Linux install guides](q3-linux.html)

### Innioasis / Timmkoo Q3E

[Linux install guides](q3e-linux.html)

### Innioasis / Timmkoo Q5

[Linux install guides](q5-linux.html)

### Innioasis / Timmkoo Q8

[Linux install guides](q8-linux.html)

### Innioasis R1

[Linux install guides](r1-linux.html)

### Innioasis PR1

[Linux install guides](pr1-linux.html)

### Innioasis SR1

[Linux install guides](sr1-linux.html)

## Questions people askDo I need to install a driver on Linux?

No proprietary driver, but add the udev rule for vendor ID 0e8d and make the AppImage executable.Does Updater CE keep my music?

A normal Updater CE install keeps the music on the microSD card. A full stock restore can wipe internal storage, so back up first.Where are the model-specific guides?

Use the software table above, or open the model card for your player. Every install page names the model and platform in its title.Can I use a different computer?

Yes. Each guide has links to the Windows, macOS and Linux versions at the top of the page.

## Other platforms[Windows](windows.html)[macOS](mac.html)[All install guides](index.html)

## Was this useful?

Your answer helps improve this guide.Yes, I found it usefulNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
