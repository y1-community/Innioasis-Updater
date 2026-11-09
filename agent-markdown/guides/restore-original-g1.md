---
title: "Restore Original Software on Innioasis G1 - step-by-step"
description: "How to restore official Original Software on an Innioasis G1 with Innioasis Updater CE or SP Flash Tool, using the verified rom_g1.zip package."
language: "en"
source: "https://innioasis.app/guides/restore-original-g1.html"
---

# Restore Original Software on Innioasis G1 - step-by-step

Restore guide · Innioasis G1

# Restore Original Software on Innioasis G1

A clean return to the software the player shipped with. Use it after a failed update, before selling the player, or whenever a custom system is not for you.[Get Updater CE](../guide.html#platform)[G1 downloads](../firmware.html?model=G1)[G1 manual](../manuals/g1.html)

Install guide for your computer

## Restore Original Software on your G1 with your computer

Pick the guide for the computer you are using. Every version has the platform setup, Updater CE steps and the way back to stock.[Windows guide](/install/original-g1-windows.html)[macOS guide](/install/original-g1-mac.html)[Linux guide](/install/original-g1-linux.html)

[All Innioasis G1 guides](/install/g1.html) · [All Original Software guides](/install/original-software.html)

## What you need
  - A Windows, macOS or Linux computer. Updater CE runs on all three.
  - The USB data cable that came with the player. Charge-only cables will not work.
  - The official `rom_g1.zip` package, which Updater downloads for you, or a copy from the [G1 archive](../firmware.html?model=G1) if you prefer to install by hand.
  - Charge in the player. A restore that loses power is the only common way to make a bad situation worse.

This replaces the system and erases internal storage. Copy music, recordings and photos to a computer first.

## Route A: Updater CE (recommended)
  - Install [Innioasis Updater CE](../guide.html#platform) and open it.
  - Set Device Model to G1. The model must match the player exactly.
  - Choose Original Software in the Software list.
  - Pick a release. The newest stable build is the safe default.
  - Press Install / Restore and wait while the package downloads and extracts.
  - Power the player fully off, then connect the USB cable only when Updater asks.
  - Do not touch the player or the cable until the success message. Disconnect and start the player.
Never choose a different model to "make it work". A G1 needs a G1 package. Mixing models is how players end up needing a manual recovery.

## Route B: SP Flash Tool (manual)

Use this when a computer cannot run Updater CE, or when you already have the package and prefer the classic tool.
  - Download `rom_g1.zip` from the [G1 archive](../firmware.html?model=G1) and unzip it.
  - Keep the scatter file next to the images. Do not rename or move the images.
  - Open SP Flash Tool, choose Download Only, and load the scatter file.
  - Power the player off, press Download, then connect the cable.
  - Wait for the green success mark before disconnecting.

The [SP Flash Tool guide](../sp-flash-tool.html) covers drivers and the Windows prompts in more detail. On Linux and macOS, Updater CE is the easier route because it brings its own USB handling.

## After the restore
  - Disconnect the player and let it start on its own.
  - Choose your language and set the clock.
  - Reconnect to Wi-Fi or Bluetooth if you use them.
  - Copy your music back. The [transfer guide](../manuals/transfer-music.html) has the folder names.

If the player starts but the screen, wheel or buttons still misbehave, the restore worked; that is a hardware or setup question, not a software one. The [troubleshooting guide](../troubleshooting.html) is the next stop.

## If it does not work

### Updater never sees the player

Change the cable, then the USB port. Avoid hubs. On Windows, install the MediaTek driver from the [driver page](../drivers.html).

### The installation stops early

Reconnect, charge the player, and start again. Do not switch to a different model's package.

### The player stays black

Charge for an hour, then hold power for ten seconds. If it is still dead, read the [recovery guide](../guides/recovery.html) before trying again.

## Questions people ask

### Will this delete my music?

Yes, internal storage is erased. Files on a microSD card usually survive, but copy them somewhere safe first.

### Can I go back to Rockbox afterwards?

Yes. Restoring Original Software is not a one-way door; the custom software page for your model can install it again.

### Do I need the Type A / Type B setting?

Only the Y1 has that choice, and only for Original Software. Every other model uses a single package.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
