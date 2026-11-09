---
title: "Rockbox-Y2 and the MicroSD card: .rockbox explained"
description: "How Rockbox-Y2 uses the MicroSD card on the Innioasis Y2: the hidden .rockbox folder, formatting, library updates, and resetting settings safely."
language: "en"
source: "https://innioasis.app/rockbox-y2/sd-card.html"
---

# Rockbox-Y2 and the MicroSD card: .rockbox explained

[← Rockbox-Y2 hub](./)

Rockbox-Y2 · Innioasis Y2

# Rockbox-Y2 and the MicroSD card

Rockbox-Y2 stores your settings, themes, playlists, and music database on the MicroSD card inside a hidden folder named <code>.rockbox</code>.[Get it in Updater CE](../guide.html?model=Y2&software=rockbox-y2)[Full written tutorial](../guides/rockbox-y2.html)

## How the .rockbox folder works

Because the firmware itself lives on the player's internal storage and your settings live in `.rockbox` on the MicroSD card, renaming or deleting `.rockbox` safely resets all settings and themes to defaults without uninstalling Rockbox-Y2.
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

## More Rockbox-Y2 guides

### [Install Rockbox-Y2 on the Innioasis Y2 (Updater CE guide)](install.html)

### [Rockbox-Y2 ROM download: developer firmware packages](download.html)

### [Rockbox-Y2 local ZIP: install from a downloaded ROM package](portable-zip.html)

### [What you need before installing Rockbox-Y2](requirements.html)

### [Rockbox-Y2 first start: music, themes and settings](first-start.html)

### [Update Rockbox-Y2: moving to a newer stable or nightly build](update.html)

### [Undo Rockbox-Y2: restore the original Y2 software](restore-stock.html)

### [Rockbox-Y2 dual boot: switching back to original software](dual-boot.html)

### [Rockbox-Y2 install problems and how to fix them](troubleshooting.html)

### [Rockbox-Y2 240p and 360p builds: choosing a theme resolution](resolution.html)

### [Rockbox-Y2: an offline music player with no account](offline.html)

### [Remove Rockbox-Y2 or reset it to defaults](uninstall.html)

### [Rockbox-Y2 FAQ: common questions answered](faq.html)

### [Rockbox-Y2 vs Original Software: what changes](vs-stock.html)

### [Rockbox for Y2: overview & downloads](../rockbox-for-y2.html)

### [Rockbox-Y1 vs Rockbox-Y2](../rockbox-y1-vs-y2.html)

### [Rockbox-Y2 themes](../rockbox-y2-themes.html)

### [Full Rockbox-Y2 written tutorial](../guides/rockbox-y2.html)

### [Rockbox-Y2 release notes](../release-notes/rockbox-y2/index.html)

### [Rockbox-Y1 hub](../rockbox-y1/)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
