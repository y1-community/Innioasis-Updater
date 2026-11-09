---
title: "How to install Rockbox on your Innioasis Y1 or Y2 - Innioasis Updater"
description: "Install Rockbox on an Innioasis Y1 or Y2 with Updater: themes, stable releases, Type A and Type B notes, and how to restore Original Software after."
language: "en"
source: "https://innioasis.app/rockbox.html"
---

# How to install Rockbox on your Innioasis Y1 or Y2 - Innioasis Updater

Rockbox reference

# Getting Rockbox on your Y1 or Y2

Rockbox changes the player software and opens up a deeper music-player interface, playback controls, sorting, and theme options. The install is guided, but Y1 and Y2 are separate journeys.[Rockbox on Y1](guides/rockbox-y1.html)[Rockbox on Y2](guides/rockbox-y2.html)[Why Rockbox?](rockbox-benefits.html)

## What the install changes

Rockbox is custom software. It does not remove your ability to return to the stock interface when the matching Original Software package is available. It can improve music browsing and customisation, but features, resolution, battery life, and theme compatibility depend on the build.Do not mix models. Select Y1 for a Y1 player and Y2 for a Y2 player. A similar-looking release name is not enough evidence that a package is compatible.

## Watch the video

Video by Frawgeeys. It shows the Innioasis Updater route; use the model-specific written steps below for your Y1 or Y2.

Video by [Cristian Plaza](https://www.youtube.com/@CristianPlaza) (Spanish), showing Rockbox on a Y1. Use the model-specific steps below for your player.

## The shared Updater route
  - Install Updater and connect nothing until it asks.
  - Choose the model printed on the player in Device Model.
  - Choose Rockbox in Software.
  - Choose a stable release unless you are deliberately testing a nightly build.
  - Click Install / Restore, then follow the power-off and USB connection prompt.
  - Disconnect only after the success message.

## 240p, 360p, and themes

Older Rockbox theme collections may be made for 240p. Y1 community builds also use 360p compatibility labels. Read the release notes and theme source before choosing a build. A theme made for one resolution or software family may not work on another.[Browse community themes](https://themes.innioasis.app/)[Theme tools](https://themes.innioasis.app/)

## Returning to Original Software

Choose the same model again, select Original Software, choose a stable release, and use Install / Restore. If the failure happened before the USB prompt, check the computer and extracted files. If the player was detected but the flash failed, start with [troubleshooting](troubleshooting.html).[Y1 restore](guides/restore-original-y1.html)[Y2 restore](guides/restore-original-y2.html)

## FAQsI reinstalled Rockbox and it didn't fix anything.

Reinstalling Rockbox writes the same build over the same files, so it cannot reset the things Rockbox keeps on the MicroSD. If the problem is a broken setting, theme, playlist, or database that lives on the card, reinstalling will not clear it. The reliable reset is deleting the `.rockbox` folder from the MicroSD — Rockbox builds a fresh one on the next boot.
  - Power the player fully off and remove the MicroSD card, or connect the player as a USB drive.
  - Show hidden files on your computer so the folder is visible. How to show hidden filesShow dotfiles on your computerWindows: in File Explorer open the View tab and tick Hidden items.macOS: in Finder press Cmd+Shift+. to toggle hidden files.Linux · GNOME Files: press Ctrl+H, or open the menu and choose Show Hidden Files.Linux · KDE Dolphin: press Ctrl+H, or use View → Show Hidden Files.
  - Delete the `.rockbox` folder from the card root.
  - Reinsert the card and start the player. Rockbox recreates the folder with defaults.
  - Re-apply your theme and settings. If the problem only comes back after a specific theme, that theme is the cause.

Deleting `.rockbox` does not uninstall Rockbox and does not touch your music — the folder holds settings, themes, and caches, and is rebuilt automatically. If you want to keep your themes, copy the folder out of `.rockbox` before deleting it, or rename the folder to `.rockbox-old` first.Why can't I see the .rockbox folder on my MicroSD?

Folders whose name starts with a dot are hidden by default on most computers. You do not need to see it to install Rockbox — Updater handles the files. If you are troubleshooting and want to delete it, turn on hidden files first. How to show hidden filesShow dotfiles on your computerWindows: in File Explorer open the View tab and tick Hidden items.macOS: in Finder press Cmd+Shift+. to toggle hidden files.Linux · GNOME Files: press Ctrl+H, or open the menu and choose Show Hidden Files.Linux · KDE Dolphin: press Ctrl+H, or use View → Show Hidden Files.Will deleting .rockbox reset my theme and settings?

Yes — `.rockbox` holds Rockbox's settings, theme, playlists, and cached database. Deleting it returns Rockbox to a clean default state. Back up the whole folder (or rename it to `.rockbox-old`) if you might want any of it back, then start the player and Rockbox creates a new folder.

## More Rockbox-Y1 and Rockbox-Y2 guides

Explore step-by-step guides for installing, downloading, theming, restoring, and troubleshooting Rockbox on both models:[Rockbox-Y1 hub](rockbox-y1/)[Rockbox-Y2 hub](rockbox-y2/)[Rockbox ROM downloads](rockbox-rom-download.html)[Rockbox for Y1](rockbox-for-y1.html)[Rockbox for Y2](rockbox-for-y2.html)[Rockbox-Y1 vs Y2](rockbox-y1-vs-y2.html)[Rockbox-Y1 themes](rockbox-y1-themes.html)[Rockbox-Y2 themes](rockbox-y2-themes.html)

## Was this reference useful?

Your answer helps improve this guide.YesNot yet[Let us know how we can improve](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
