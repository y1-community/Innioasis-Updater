---
title: "Rockbox-Y1 themes: transferring themes with Updater CE, 240p vs 360p &amp; applying a theme"
description: "How to transfer themes to the Innioasis Y1 with Updater CE (automatic push when available or guided step-by-step transfer after an MTKClient flash on macOS and Linux), plus 240p vs 360p compatibility and applying a theme."
language: "el"
source: "https://innioasis.app/rockbox-y1-themes_el.html"
---

# Rockbox-Y1 themes: transferring themes with Updater CE, 240p vs 360p &amp; applying a theme

[← Rockbox-Y1 hub](rockbox-y1/)

Rockbox-Y1 · themes & Updater CE

# Rockbox-Y1 themes: transfer with Updater CE, pick the build, then the look

Updater CE handles Rockbox-Y1 themes and fonts for you — transferring them to the Y1 automatically whenever it can, and guiding you through the transfer step by step when it cannot happen unattended (for example, right after an MTKClient firmware install on macOS or Linux).[Get Rockbox & Updater CE](guides/rockbox-y1.html)[Browse community themes](https://themes.innioasis.app/)[240p vs 360p](rockbox-y1/resolution.html)

## Transferring themes to the Y1 with Updater CE

Rockbox stores its firmware in the Y1's internal flash, while themes, fonts, and user settings live inside the hidden `.rockbox` folder on the player's storage (MicroSD card). Because flashing a ROM and copying files to storage use two different connections, Ενημερωτής CE adapts automatically to your operating system and install method:
  - Automatic transfer when Updater CE can reach the player: When you install a 360p Rockbox-Y1 build (or enable automatic theme syncing in Settings), Updater CE downloads and merges the curated 360p theme and font pack in the background. As soon as the Y1 is reachable over ADB (Android Debug Bridge) or mounted as a USB drive with a `.rockbox` folder, Updater CE pushes the themes and fonts straight to the player for you with no manual zip extraction required.
  - Guided step-by-step transfer when it cannot happen unattended (e.g. MTKClient on macOS & Linux): When you flash Rockbox using an MTKClient install method on macOS or Linux, the flash happens while the Y1 is powered off in low-level Preloader/BROM mode — before Rockbox has booted for the first time to create `.rockbox` and before the player's storage is mounted on your computer. Whenever Updater CE cannot complete the transfer unattended during the flash, it automatically opens the post-install themes & fonts assistant and walks you through finishing it: 
    - Boot Rockbox first: Updater CE prompts you to disconnect the USB cable if needed and power on the Y1 so Rockbox boots once and initializes the `.rockbox` folder on the card.
    - Reconnect via USB: Plug the Y1 back into your Mac or Linux PC. If ADB is available, Updater CE detects the booted player and pushes the theme and font packs automatically.
    - Or use USB Storage Mode with the guided folder picker: If ADB is not active or you prefer direct storage transfer, Updater CE guides you to enter USB Storage Mode on the Y1, click Select .rockbox Folder, reveal hidden folders (Cmd+Shift+. in the macOS file dialog or Ctrl+H on Linux), and select `.rockbox` on the Y1 drive — then Updater CE merges all themes and fonts into place for you.

  - Add or refresh themes anytime on demand: You can run the same automated or guided transfer at any time without reflashing firmware — open Updater CE and choose Settings → Install Rockbox 360p Themes (Cmd+T on macOS, Ctrl+T on Windows and Linux), or drag individual theme `.zip` packs onto Updater CE's Smart Drop window.

## 240p, 360p, and why the label is on the build

Y1 community builds are published with a resolution label, and the theme collections carry the same label. 240p builds have the broadest compatibility with older theme packs; 360p builds are made for the newer Y1 theme path. Installing one and applying the other is not dangerous — it just looks wrong, with clipped text, missing elements, or an interface you cannot read.

If you have no theme preference yet, take the newer stable build and its default theme, then choose themes that match its label. The [resolution page](rockbox-y1/resolution.html) goes deeper; the rule of thumb is simple: build label and theme label must agree.

## Where themes live

Themes are files on the MicroSD card, inside the `.rockbox` folder — the same folder that holds settings and caches. The firmware itself is on internal flash, so adding, changing or removing a theme never requires reflashing.
  - Copy the theme's own folder into `.rockbox/themes` on the card.
  - Then choose it in the player's theme settings and reboot to see it applied.
  - Keep a copy of a theme you like before updating the build — it is a file, not an installation.

Turn on hidden files first if you cannot see the folder: macOS Cmd+Shift+., Windows View → Hidden items, Linux Ctrl+H.

## Applying a theme, in order
  - Install and boot Rockbox-Y1 first; a theme needs a running build.
  - Copy the theme folder to `.rockbox/themes` on the card.
  - Open the theme settings and select the theme.
  - Reboot so the whole interface — not just the menu — picks it up.
  - If it looks broken, select another theme; the files are still there if you want to retry later.

## Undoing a theme that broke the interface

If the player boots into something unusable, you do not need to reinstall the firmware. Rename or delete the `.rockbox` folder on the card and start the player: the build recreates the folder with default settings and a default theme. Your music is untouched, and you can copy the themes you want back afterwards.[The .rockbox folder](rockbox-y1/sd-card.html)[First start](rockbox-y1/first-start.html)[Updating the build](rockbox-y1/update.html)

## Ερωτήσεις που κάνουν οι άνθρωποιWhy does Updater CE walk me through transferring themes after an MTKClient install on macOS or Linux?

MTKClient flashes the Rockbox ROM to internal storage while your Y1 is powered off in low-level Preloader/BROM mode, before Rockbox has booted to initialize the `.rockbox` folder and before the MicroSD card is mounted on your computer. Whenever Updater CE can reach the booted player directly (via ADB or a mounted USB drive), it transfers the themes automatically; when it cannot do that unattended during the flash, it opens the guided themes & fonts step right after flashing to help you power on the Y1 and complete the transfer via ADB or USB Storage Mode.Will a Y2 theme work on the Y1?

No. The ports are separate, and theme support on the Y2 follows its beta builds. See [Θέματα Rockbox-Y2](rockbox-y2-themes_el.html).Do themes survive an update?

Usually yes, because they live on the card and the flash writes the ROM. If a new build changes the theme path, reapply a theme that matches its label.Why is the theme only half applied?

A reboot normally resolves it. If not, the theme's files are incomplete — re-copy its folder rather than editing individual files.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
