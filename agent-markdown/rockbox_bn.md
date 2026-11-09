---
title: "How to install Rockbox on your Innioasis Y1 or Y2 - Innioasis Updater"
description: "Install Rockbox on an Innioasis Y1 or Y2 with Updater: themes, stable releases, Type A and Type B notes, and how to restore Original Software after."
language: "bn"
source: "https://innioasis.app/rockbox_bn.html"
---

# How to install Rockbox on your Innioasis Y1 or Y2 - Innioasis Updater

Rockbox reference

# Getting Rockbox on your Y1 or Y2

Rockbox changes the player software and opens up a deeper music-player interface, playback controls, sorting, and theme options. The install is guided, but Y1 and Y2 are separate journeys.[Rockbox on Y1](guides/rockbox-y1.html)[Rockbox on Y2](guides/rockbox-y2.html)[কেন Rockbox?](rockbox-benefits_bn.html)

## What the install changes

Rockbox is custom software. It does not remove your ability to return to the stock interface when the matching Original Software package is available. It can improve music browsing and customisation, but features, resolution, battery life, and theme compatibility depend on the build.Do not mix models. Select Y1 for a Y1 player and Y2 for a Y2 player. A similar-looking release name is not enough evidence that a package is compatible.

## ভিডিওটি দেখুন

Video by Frawgeeys. It shows the Innioasis Updater route; use the model-specific written steps below for your Y1 or Y2.

ভিডিও দ্বারা [ক্রিশ্চিয়ান প্লাজা](https://www.youtube.com/@CristianPlaza) (Spanish), showing Rockbox on a Y1. Use the model-specific steps below for your player.

## The shared Updater route
  - Install Updater and connect nothing until it asks.
  - Choose the model printed on the player in ডিভাইস মডেল.
  - বেছে নিন Rockbox মধ্যে সফটওয়্যার.
  - Choose a stable release unless you are deliberately testing a nightly build.
  - ক্লিক করুন ইনস্টল / পুনরুদ্ধার, then follow the power-off and USB connection prompt.
  - Disconnect only after the success message.

## 240p, 360p, and themes

Older Rockbox theme collections may be made for 240p. Y1 community builds also use 360p compatibility labels. Read the release notes and theme source before choosing a build. A theme made for one resolution or software family may not work on another.[Browse community themes](https://themes.innioasis.app/)[থিম সরঞ্জাম](https://themes.innioasis.app/)

## Returning to Original Software

Choose the same model again, select মূল সফটওয়্যার, choose a stable release, and use ইনস্টল / পুনরুদ্ধার. If the failure happened before the USB prompt, check the computer and extracted files. If the player was detected but the flash failed, start with [সমস্যা সমাধান](troubleshooting_bn.html).[Y1 restore](guides/restore-original-y1.html)[Y2 restore](guides/restore-original-y2.html)

## সাধারণ প্রশ্নI reinstalled Rockbox and it didn't fix anything.

Reinstalling Rockbox writes the same build over the same files, so it cannot reset the things Rockbox keeps on the MicroSD. If the problem is a broken setting, theme, playlist, or database that lives on the card, reinstalling will not clear it. The reliable reset is deleting the `.rockbox` folder from the MicroSD — Rockbox builds a fresh one on the next boot.
  - Power the player fully off and remove the MicroSD card, or connect the player as a USB drive.
  - Show hidden files on your computer so the folder is visible. How to show hidden filesShow dotfiles on your computerWindows: in File Explorer open the View tab and tick Hidden items.macOS: in Finder press Cmd+Shift+. to toggle hidden files.Linux · GNOME Files: প্রেস Ctrl+H, or open the menu and choose Show Hidden Files.Linux · KDE Dolphin: প্রেস Ctrl+H, বা ব্যবহার করুন View → Show Hidden Files.
  - Delete the `.rockbox` folder from the card root.
  - Reinsert the card and start the player. Rockbox recreates the folder with defaults.
  - Re-apply your theme and settings. If the problem only comes back after a specific theme, that theme is the cause.

Deleting `.rockbox` does not uninstall Rockbox and does not touch your music — the folder holds settings, themes, and caches, and is rebuilt automatically. If you want to keep your themes, copy the folder out of `.rockbox` before deleting it, or rename the folder to `.rockbox-old` প্রথমWhy can't I see the .rockbox folder on my MicroSD?

Folders whose name starts with a dot are hidden by default on most computers. You do not need to see it to install Rockbox — Updater handles the files. If you are troubleshooting and want to delete it, turn on hidden files first. How to show hidden filesShow dotfiles on your computerWindows: in File Explorer open the View tab and tick Hidden items.macOS: in Finder press Cmd+Shift+. to toggle hidden files.Linux · GNOME Files: প্রেস Ctrl+H, or open the menu and choose Show Hidden Files.Linux · KDE Dolphin: প্রেস Ctrl+H, বা ব্যবহার করুন View → Show Hidden Files.Will deleting .rockbox reset my theme and settings?

Yes — `.rockbox` holds Rockbox's settings, theme, playlists, and cached database. Deleting it returns Rockbox to a clean default state. Back up the whole folder (or rename it to `.rockbox-old`) if you might want any of it back, then start the player and Rockbox creates a new folder.

## More Rockbox-Y1 and Rockbox-Y2 guides

Explore step-by-step guides for installing, downloading, theming, restoring, and troubleshooting Rockbox on both models:[Rockbox-Y1 হাব](rockbox-y1/)[Rockbox-Y2 হাব](rockbox-y2/)[Rockbox ROM downloads](rockbox-rom-download_bn.html)[Rockbox Y1 এর জন্য](rockbox-for-y1_bn.html)[Rockbox Y2 এর জন্য](rockbox-for-y2_bn.html)[Rockbox-Y1 বনাম Y2](rockbox-y1-vs-y2_bn.html)[Rockbox-Y1 থিম](rockbox-y1-themes_bn.html)[Rockbox-Y2 থিম](rockbox-y2-themes_bn.html)

## Was this reference useful?

আপনার উত্তর এই নির্দেশিকা উন্নত করতে সাহায্য করে.হ্যাঁএখনো না[আমরা কিভাবে উন্নতি করতে পারি তা আমাদের জানান](https://github.com/y1-community/Innioasis-Updater/issues)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
