---
title: "Rockbox-Y1 and the MicroSD card: .rockbox explained"
description: "How Rockbox-Y1 uses the MicroSD card on the Innioasis Y1: the hidden .rockbox folder, formatting, library updates, and resetting settings safely."
language: "en"
source: "https://innioasis.app/rockbox-y1/sd-card.html"
---

# Rockbox-Y1 and the MicroSD card: .rockbox explained

[← Rockbox-Y1 hub](./)

Rockbox-Y1 · Innioasis Y1

# Rockbox-Y1 and the MicroSD card

Rockbox-Y1 stores your settings, themes, playlists, and music database on the MicroSD card inside a hidden folder named <code>.rockbox</code>.[Get it in Updater CE](../guide.html?model=Y1&software=rockbox-y1)[Full written tutorial](../guides/rockbox-y1.html)

## How the .rockbox folder works

Because the firmware itself lives on the player's internal storage and your settings live in `.rockbox` on the MicroSD card, renaming or deleting `.rockbox` safely resets all settings and themes to defaults without uninstalling Rockbox-Y1.
  - Connect the player over USB or put the MicroSD card into your computer.
  - Show hidden files (macOS: Cmd+Shift+.; Windows: View → Hidden items).
  - Rename `.rockbox` to `.rockbox-backup` to reset your configuration.
  - Restart the player so it creates a fresh `.rockbox` folder.

## MicroSD card tips
  - Organize music in normal folders; Rockbox can browse both by folder and by ID3/vorbis tags.
  - Refresh the database after copying new albums.
  - Use FAT32 (or exFAT where supported) for reliable card reading.

## Frequently asked questionsWill deleting .rockbox erase my music?

No, as long as your music folders are stored outside the .rockbox folder on the card.Why can't I see the .rockbox folder on my computer?

Folders starting with a dot are hidden by default on Windows, macOS, and Linux. Enable hidden files in your file manager.

## More Rockbox-Y1 guides

### [Install Rockbox-Y1 on the Innioasis Y1 (Updater CE guide)](install.html)

### [Rockbox-Y1 ROM download: developer firmware packages](download.html)

### [Rockbox-Y1 local ZIP: install from a downloaded ROM package](portable-zip.html)

### [What you need before installing Rockbox-Y1](requirements.html)

### [Rockbox-Y1 first start: music, themes and settings](first-start.html)

### [Update Rockbox-Y1: moving to a newer stable or nightly build](update.html)

### [Undo Rockbox-Y1: restore the original Y1 software](restore-stock.html)

### [Rockbox-Y1 dual boot: switching back to original software](dual-boot.html)

### [Rockbox-Y1 install problems and how to fix them](troubleshooting.html)

### [Rockbox-Y1 240p and 360p builds: choosing a theme resolution](resolution.html)

### [Rockbox-Y1: an offline music player with no account](offline.html)

### [Remove Rockbox-Y1 or reset it to defaults](uninstall.html)

### [Rockbox-Y1 FAQ: common questions answered](faq.html)

### [Rockbox-Y1 vs Original Software: what changes](vs-stock.html)

### [Rockbox for Y1: overview & downloads](../rockbox-for-y1.html)

### [Rockbox-Y1 vs Rockbox-Y2](../rockbox-y1-vs-y2.html)

### [Rockbox-Y1 themes](../rockbox-y1-themes.html)

### [Full Rockbox-Y1 written tutorial](../guides/rockbox-y1.html)

### [Rockbox-Y1 release notes](../release-notes/rockbox-y1/index.html)

### [Rockbox-Y2 hub](../rockbox-y2/)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
