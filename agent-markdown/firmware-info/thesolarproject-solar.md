---
title: "About Solar (Y1, Y2) - README.md - Innioasis Updater"
description: "A Y1 custom Software with network features, including YouTube support."
language: "en"
source: "https://innioasis.app/firmware-info/thesolarproject-solar.html"
---

# About Solar (Y1, Y2) - README.md - Innioasis Updater

[← Firmware Downloads](../firmware.html)

Firmware README · Y1 · Y2

# About Solar

A Y1 custom Software with network features, including YouTube support.

Also known as: README.md · thesolarproject/solar · solar · Solar · thesolarproject-solarY1 · Y2[Open the Solar guide](../guides/solar-y1.html)[Install with Updater CE](../firmware.html?model=Y1&software=solar-y1)[Why Solar?](../solar-benefits.html)Downloads from Firmware Archive4,022

Solar logo

# Solar

Custom firmware and launcher for the Innioasis Y1 and Y2 — a full interface replacement with podcast downloads, a global quick menu, Reach (Deezer + Soulseek), Stem Player (stem separation powered by [Lalal.ai](https://www.lalal.ai)), Y1 theme support, and Rockbox-Y1 on the same ROM (switch without reboot).

Full usage and developer guides:[docs/README.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fthesolarproject%2Fsolar%2Fblob%2FHEAD%2Fdocs%2FREADME.md)

## Features
  - Stem Player — Gen1-style vocal / drums / bass / melody mixing with the scroll wheel; separate local library tracks via Lalal.ai stem separation, cache stems on device, and mash up one to three songs
  - Reach — search, play and download music from Deezer and Soulseek
  - Podcasts — search and download episodes to your Y1 over the internet
  - Quick menu — global context menu for playback, queue, Wi‑Fi, Bluetooth, and more from any screen
  - Y1 themes — install and apply themes from the original Y1 firmware
  - Rockbox-Y1 — co-installed; switch launchers from Settings (unified keymap, no reboot)

## ScreenshotsAbout SolarReach searchReach browseGet Music searchSoulseek messagingPodcastsPodcast episodesArtists viewQuick controlsACmp3 theme

| About Solar — version, attribution, and OTA update check | Reach search — unified Deezer + Soulseek results |
| --- | --- |
| Reach browse — peer library and download actions | Get Music — combined Deezer and Reach search |
| Soulseek messaging | Podcasts — subscribe and browse shows |
| Podcast episodes — episode list and downloads | Artists view — music library by artist > album |
| Quick controls — global context menu (playback, queue, Wi‑Fi) | ACmp3 theme — Y1 custom theme applied in Solar |

## Deezer account setup in Reach

A Demo Account is included for testers, please configure your own to ensure reliable playback and downloads, please do not submit issues about failed downloads / streams if still using the demo account as a Deezer account will offer a single playback slot to an account at one time.

Reach can search, stream, and download from [Deezer](https://www.deezer.com) using your account’s `arl` session cookie (the same method used by other Deezer download tools). You need a free or Premium Deezer account and a PC on the same Wi‑Fi as the Y1.

### On the Y1
  - Open Settings → Deezer.
  - Select Set up on PC. Solar starts a small setup server and shows a URL like `http://192.168.x.x:8080/deezer`.

### On your PC
  - In a browser, open the URL shown on the Y1 (use the Y1’s IP — not `localhost`).
  - In another tab, log in at [deezer.com/login](https://www.deezer.com/login) if you are not already signed in.
  - Copy your `arl` cookie from the browser:
    - Chrome:`F12` → Application → Cookies → `https://www.deezer.com` → copy the arl value (long hex string).
    - Firefox:`F12` → Storage → Cookies → `https://www.deezer.com` → arl.

  - On the Solar setup page, paste arl, choose MP3 or FLAC (Premium), and tap Save & Test.
  - Wait for Deezer login verified before closing the page.

### Back on the Y1
  - Press Back to leave the setup screen (confirm I'm finished if asked).
  - Try Get Music from the home menu, or Settings → Deezer → Search, and download or queue a track.

### Notes
  - Treat arl like a password — only paste it on the setup page on your home network.
  - If arl is missing in DevTools, refresh deezer.com while logged in, or sign out and back in.
  - Some test builds ship with a shared demo account; paste your own arl to replace it.
  - To switch accounts or quality later: Settings → Deezer → Set up on PC again.
  - FLAC requires Deezer Premium; free accounts should use MP3.

# How to get started with Solar

Head to the [Solar GitHub repository](https://innioasis.app/firmware.html?model=Y1&software=solar-y1) and download a copy of the ROM from the [Releases](https://innioasis.app/firmware.html?model=Y1&software=solar-y1) tab.

### Install in Innioasis updater app:

[1.Download](https://innioasis.app/firmware.html?model=Y1&software=solar-y1) the [rom.zip](https://innioasis.app/firmware.html?model=Y1&software=solar-y1) file
  - click "Browse Files" in the updater app and select the [rom.zip](https://innioasis.app/firmware.html?model=Y1&software=solar-y1) file
  - Installation will begin

### Install with SP Flash Tool 5.1924:

Extract [rom.zip](https://innioasis.app/firmware.html?model=Y1&software=solar-y1) contents and [apply these instructions to the files](https://support.innioasis.com/download/flashing_tutorial/Flashing_tutorial-Y1_EN%20v2.0.7-20241021.pdf) extracted from the zip

### Install with MTKClient
  - Install [MTKClient](https://github.com/bkerler/mtkclient)
  - Download [the latest Solar firmware](https://innioasis.app/firmware.html?model=Y1&software=solar-y1) (rom.zip or rom\_type\_b.zip) (Try Type A first, if scrolling doesn't work then try B)
  - Unpack the archive:mkdir rom && cd rom unzip ../rom.zip
  - Turn of the device, disconnect from the PC
  - Start the flashing process:cd rom python ../mtk.py w logo,uboot,bootimg,recovery,android,usrdata logo.bin,lk.bin,boot.img,recovery.img,system.img,userdata.img
  - Connect the device via USB
  - Unplug the device when the process has finished
  - Power on the device

# How to leave feedback and report issues.

Please leave your feedback and issue reports in the [Issues Tracker](https://github.com/thesolarproject/solar/issues)

## Developers

Local Solar Designer (1:1 GUI simulator / agent bridge) lives at `solar-designer/` and is gitignored — clone the tree or create it locally, then `cd solar-designer && npm install && npm start`. See `solar-designer/README.md` when present.

# solar-os

# solar-os

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
