---
title: "Rockbox-Y2 themes: installing and resetting themes on the Y2"
description: "How to install, manage, and reset Rockbox-Y2 themes on the Innioasis Y2: where themes live in the .rockbox folder and how to check build compatibility."
language: "da"
source: "https://innioasis.app/rockbox-y2-themes_da.html"
---

# Rockbox-Y2 themes: installing and resetting themes on the Y2

[← Rockbox-Y2 hub](rockbox-y2/)

Rockbox-Y2 · themes

# Rockbox-Y2 temaer

How to install themes on Rockbox-Y2, check theme compatibility with your installed build, and reset a theme if it does not display properly.[Rockbox-Y2 release notes](release-notes/rockbox-y2/index.html)[Browse community themes](https://themes.innioasis.app/)[Installer Rockbox-Y2](rockbox-y2/install.html)

## Check theme compatibility for your build

Rockbox-Y2 is developed separately from the Y1 port, so theme compatibility follows the Y2 build version you have installed. Check the [Rockbox-Y2 release notes](release-notes/rockbox-y2/index.html) for your version before installing a theme pack.

See [Rockbox-Y1 mod Rockbox-Y2](rockbox-y1-vs-y2_da.html) for a full comparison of the two ports.

## How to install themes on the Y2

Themes are stored on your MicroSD card inside the hidden `.rockbox` folder.
  - Start Rockbox-Y2 at least once so it creates the `.rockbox` folder on your MicroSD card.
  - Extract or copy the theme files into `.rockbox/` (so `themes`, `wps`, `fonts`, og `backdrops` merge into `.rockbox/`).
  - On the player, open Settings → Theme Settings → Browse Theme Files and select your theme.

To view hidden folders on your computer: press Cmd+Shift+. on macOS, enable View → Hidden items on Windows, or press Ctrl+H on Linux.

## How to reset a broken theme

If a theme makes the screen hard to read, rename or delete the `.rockbox` folder on your MicroSD card and restart the player. Rockbox-Y2 will create a fresh `.rockbox` folder with the default theme while keeping your music intact.[The .rockbox folder](rockbox-y2/sd-card.html)[Updating Rockbox-Y2](rockbox-y2/update.html)[Rockbox-Y2 build notes](rockbox-y2/resolution.html)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
