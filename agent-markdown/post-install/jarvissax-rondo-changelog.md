---
title: "What's new in Rondo - Innioasis Updater"
description: "What's new in Rondo Rondo's releases, newest first. Each one is on the releases page https://github.com/jarvissax/rondo/releases, with the firmware rom.zip for Innioasis"
language: "en"
source: "https://innioasis.app/post-install/jarvissax-rondo-changelog.html"
---

# What's new in Rondo - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y1&software=rondo-y1)

Post-install setup · Rondo · Y1

# What's new in Rondo

A lightweight, custom audio operating system for the Innioasis Y1.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y1&software=rondo-y1)[Install guide](../guide.html?model=Y1&software=rondo-y1)

# What's new in Rondo

Rondo's releases, newest first. Each one is on the [releases page](https://innioasis.app/firmware.html?model=Y1&software=rondo-y1), with the firmware (`rom.zip`) for Innioasis Updater CE and the update for a Y1 that already runs Rondo.

## 1.0.2 (November 3, 2026)

Nothing changes on the Y1 itself; this release is about the server.

### Server
  - Update with one click. When a newer Rondo is out, the server's admin page offers Update:

the server downloads the new version and restarts on it in a minute or two, keeping your settings, YouTube account and connected Y1. A small companion container, `rondo-updater`, does the work; it only ever touches the Rondo server's own container.
  - Ready-made server images. Installing the server now downloads it instead of building it, for

regular PCs and 64-bit ARM (Raspberry Pi 4 and 5, many NAS boxes), which makes the first start much quicker on small machines.
  - Moving an older server over: a server set up before 1.0.2 built itself and has no updater

yet. Update it by hand once ([how](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fserver.md%23keeping-it-running&anchor=keeping-it-running)); after that, Update on the admin page does it.

## 1.0.1 (November 3, 2026)

An update over Wi-Fi, the dashboard or USB: no reinstall needed, and everything on your Y1 stays.

### Fixed
  - Click sound stays off. Turning off Settings › Click sound (or the switch in the

dashboard) now lasts through a restart. Before, the Y1's own sound profile turned the click back on every time it started.

### Updates
  - Every release now comes with its firmware. The `rom.zip` that Innioasis Updater CE installs

is built automatically for each release, so a new install always gets the newest Rondo.
  - Rondo knows which updates it can install. The firmware now carries a version of its own.

If a future release changes the firmware itself (not only Rondo), Settings › Software update, the dashboard and the update page say so and point you to Innioasis Updater CE, instead of offering an install that couldn't work. The Y1 refuses such an update however it arrives.
  - One place for news of a release. The Y1 (through your server), the dashboard and the update

page all learn about a new Rondo from the update page, and only once its firmware is ready, so they always agree with each other and with Innioasis Updater CE.

### Server
  - The server's version is now 1.0.1 as well. It reads Rondo's updates from the update page and

tells a Y1 when a release needs a new firmware. Update it as described in [Keeping it running](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fserver.md%23keeping-it-running&anchor=keeping-it-running).

### Documentation
  - A new README with screenshots, and updated guides for installing, using, updating and the

dashboard.

## 1.0.0 (November 2, 2026)

The first release of Rondo as a firmware: the Y1 starts straight into Rondo, with nothing else on it. Install it with Innioasis Updater CE (Y1, Type A, then Rondo).
  - iPod-style menus for the click wheel, with optional vibration and a click on every step, and

wheel acceleration for long lists.
  - Your music and videos from the microSD card, with covers, lyrics, search and playlists, and

the card as a USB drive when the Y1 is plugged into a computer.
  - YouTube Music and YouTube, streamed live through your own Rondo server, including Shorts, with

or without a YouTube account.
  - FM radio with station names, scanning and saved stations.
  - Bluetooth headphones and speakers, and Wi-Fi, set up from the wheel.
  - A dashboard in your phone's browser for music, playlists, settings, the theme, Wi-Fi,

Bluetooth, the radio and updates.
  - Light and dark looks, accent colors, text sizes and a main menu you can reorder.
  - Shut down and restart from Settings, or by holding the Power button.
  - Updates without reinstalling: from the Y1 over Wi-Fi, the dashboard, or the update page over

USB.

These are Rondo's own instructions, shown here word for word.

Published by the [jarvissax/rondo](https://innioasis.app/firmware.html?model=Y1&software=rondo-y1) project [[1]](https://innioasis.app/firmware_info.html?repo=jarvissax%2Frondo&software=rondo-y1)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Ajarvissax)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
