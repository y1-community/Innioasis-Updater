---
title: "Wi-Fi, Bluetooth &amp; FM Radio Setup for Reborn (Y2Linux) - Innioasis Updater"
description: "Short post-install guide for Reborn (Y2Linux / Y2Reborn) on Innioasis Y2: copy system.img, then set up Wi-Fi, Bluetooth and FM radio."
language: "ms"
source: "https://innioasis.app/y2reborn_wifibt_ms.html"
---

# Wi-Fi, Bluetooth &amp; FM Radio Setup for Reborn (Y2Linux) - Innioasis Updater

Innioasis Y2 · Reborn Post-Install

# Set up Wi-Fi, Bluetooth & FM radio.

Copy one file to your player. Reborn handles the rest.[Download system.img (860 MB)](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)[Install Guide](guides/reborn-y2linux-y2.html)[Why Y2Reborn?](reborn-y2linux-benefits_ms.html)

## Why this file?

Wi-Fi, Bluetooth and FM radio need five MediaTek firmware modules that Reborn cannot ship. They are inside the official Y2 `system.img`. Reborn extracts them once, checks them, and deletes the file.

## Setup
  - Download system.img

Download the v3.2.0 FM `system.img` to your computer.[ Download system.img ](https://github.com/y1-community/y1-stock-rom/releases/download/3.2.0-fm/system.img)
  - Boot Reborn once

Turn the player on. Wait for Setting up storage to finish, then restart it once.
  - Connect to your computer

Use a USB data cable. The player appears as Internal Storage.On a Mac?

Pasang [OpenMTP](https://openmtp.ganeshrvel.com/) to browse the player. Windows and Linux mount it automatically.
  - Copy system.img to Firmware

Create a folder called `Firmware` at the root of Internal Storage. Copy `system.img` into it.
  - Wait for setup to finish

Reborn installs the radio firmware automatically and deletes `system.img`. This takes about 10–20 seconds. Wait for Wi-Fi and Bluetooth are ready.
  - Connect Wi-Fi, Bluetooth and FM radio
    - Wi-Fi: Settings → System → Network → Wi-Fi. Choose your 2.4 GHz network.
    - Bluetooth: Put your headphones in pairing mode. Settings → Bluetooth → select them.
    - FM radio: Plug in wired headphones as the antenna, then open FM Radio.

  - Update over Wi-Fi

Future Reborn updates install from Settings → System → Software Update. Your radio firmware stays put.

## Was this guide helpful?

Did you find this post-install setup guide helpful? Yes, it helped! [ Need help on Discord ](https://discord.gg/zHrT2zrcek) Thank you for your feedback! Enjoy your wireless listening on Y2Reborn.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
