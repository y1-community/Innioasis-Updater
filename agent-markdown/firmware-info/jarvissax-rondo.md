---
title: "About Rondo (Y1) - README.md - Innioasis Updater"
description: "A lightweight, custom audio operating system for the Innioasis Y1."
language: "en"
source: "https://innioasis.app/firmware-info/jarvissax-rondo.html"
---

# About Rondo (Y1) - README.md - Innioasis Updater

[← Firmware Downloads](../firmware.html)

Firmware README · Y1

# About Rondo

A lightweight, custom audio operating system for the Innioasis Y1.

Also known as: README.md · jarvissax/rondo · rondo · Rondo · jarvissax-rondoY1[Open the Rondo guide](../guides/rondo-y1.html)[Install with Updater CE](../firmware.html?model=Y1&software=rondo-y1)[Why Rondo?](../rondo-benefits.html)Downloads from Firmware Archive483

# Rondo

**A click-wheel firmware for the Innioasis Y1: the music on your card, YouTube Music, YouTube and FM radio, all from the wheel.**

Rondo's main menu, with the song that's playing on the rightNow Playing, with the album cover and what's up next

[Install](https://innioasis.app/guides/rondo-y1.html) · [Use](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fusing.md) · [Server](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fserver.md) · [Dashboard](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fdashboard.md) · [Help](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Ftroubleshooting.md) · [What's new](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2FCHANGELOG.md)

The Innioasis Y1 is a small music player with an iPod-style click wheel. Underneath, it runs Android 4.2. Rondo is a firmware for it, built from the community's Android 4.2 base: everything else is taken out, and the Y1 starts straight into menus made for the wheel. Play the music on your microSD card, stream YouTube Music and YouTube, and listen to FM radio, all without a touchscreen. You install it with Innioasis Updater CE, the same way as Rockbox or the Y1's original software, and you can always go back.

## What it does

### Your music, from the card

Copy music onto the microSD card and Rondo sorts it by song, artist and album, using the files' tags. You get covers, lyrics that scroll along with the song, search as you type, and playlists you can make on the Y1 or in your browser. Videos on the card play too, and plugging the Y1 into a computer turns the card into a USB drive.The library: songs, artists, albums, playlists and search
A playlist with album covers
Lyrics following the song

| The library | A playlist | Lyrics that follow the song |
| --- | --- | --- |

FLAC, MP3, M4A, AAC, OGG, Opus and WAV. Lyrics come from the file's tags or an `.lrc` file next to it. Nothing on the card ever needs the internet.

### YouTube Music and YouTube

With a small server you run yourself, the Y1 streams YouTube Music and YouTube: home, search, artists, albums, playlists, lyrics, Shorts, and video up to 720p. Sign the server in to your YouTube account for your own library, subscriptions and history, or use it without an account.Searching YouTube Music
A song streaming from YouTube Music
Searching YouTube
A video playing, scrubbing with the wheel

| Searching YouTube Music | Streaming a song |
| --- | --- |
| Searching YouTube | Watching a video |

Streams play as they arrive: neither the Y1 nor the server ever stores audio or video from YouTube. (In the pictures: Kevin MacLeod's music and Blender Studio's open movie Spring, both openly licensed.)

### Made for the wheel

Every screen works with the wheel and five buttons. Each wheel pulse is one step, like Rockbox, with an optional buzz and click on every step and acceleration for long lists. Searches, Wi-Fi passwords and playlist names are typed on a keyboard you move through with the wheel or the buttons. Choose a light or dark look, an accent color and a text size, and which entries the main menu shows, in which order.The on-screen keyboard
The main menu in the light look with the Mint accent
Settings

| The wheel keyboard | Light look, Mint accent | Settings |
| --- | --- | --- |

### FM radio, Bluetooth and Wi-Fi

The Y1's FM radio, with station names, a scan of the whole band, saved stations and a speaker option; wired headphones are the antenna. Bluetooth headphones and speakers, and Wi-Fi networks, are set up from the wheel as well.

### A dashboard in your browser

Open Settings › Dashboard on the Y1, then the address it shows on your phone or computer. From there you can upload music, make playlists, control what's playing, change the theme and every setting, manage Wi-Fi, Bluetooth and the radio, and shut down, restart or update the Y1. It runs on the Y1 itself, over your Wi-Fi, and needs no internet.

The dashboard's Overview page on a computerThe dashboard on a phone

### Updates that keep everything

A new Rondo installs in about a minute, without reinstalling the firmware: from **Settings › Software update over Wi-Fi, with Install** in the dashboard, or over USB from [the update page](https://jarvissax.github.io/rondo/). Your settings, Wi-Fi, server connection, playlists and music stay as they are. The rare release that changes the firmware itself says so, and installs with Innioasis Updater CE instead.

## What you need
  - An Innioasis Y1, Type A: one that shipped with software 2.0.0 or later. Not sure which type

yours is? See [Before you start](https://innioasis.app/guides/rondo-y1.html).
  - A computer (macOS, Windows or Linux) with Innioasis Updater CE, and a USB-C cable that

carries data, for the install.
  - 2.4 GHz Wi-Fi. The Y1 can't see 5 GHz networks.
  - For YouTube Music and YouTube, a Rondo server: a computer at home that stays on (a 64-bit

Raspberry Pi or a NAS is fine), or a small VPS. Your music card, the radio and Bluetooth work without it.

## Getting started
  - [Install Rondo](https://innioasis.app/guides/rondo-y1.html) with Innioasis Updater CE: choose the Y1, Type A, then

Rondo. It takes about 10 minutes, and your microSD card isn't touched.
  - [First start](https://innioasis.app/guides/rondo-y1.html): join Wi-Fi, copy your music onto the card, and

look through Settings.
  - [Set up a server](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fserver.md) if you want YouTube Music and YouTube. About 15 minutes

with Docker.
  - [Learn the controls](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fusing.md), and open the [dashboard](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fdashboard.md) on

your phone.

### The controls at a glance

| Control | What it does |
| --- | --- |
| Wheel | Moves through lists. On Now Playing, a video or the radio, it changes the volume. |
| Center | Opens or selects. Hold it for options. |
| Menu (top) | Back. |
| Play/Pause (bottom) | Plays and pauses, from any screen. |
| Next / Previous | Next or previous song. Hold to fast-forward or rewind. |
| Power | Screen off and on. Hold it to shut down or restart. |

[Using Rondo](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fusing.md) has the details for every screen, and every setting.

## Your own server

The server's admin page

The Y1 is too old to talk to YouTube directly: Android 4.2 can't handle today's YouTube pages, video formats or encryption. So a small server does that part. You run it with Docker at home or on a VPS, set it up from its admin page in the browser, connect your Y1 with a six-digit code, and optionally sign it in to your YouTube account. It keeps yt-dlp up to date by itself, its admin page tells you when something needs attention, and a new version of the server installs with one click there. One server serves one Y1. See [Setting up a Rondo server](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fserver.md).

## How it works` Innioasis Y1 your Rondo server YouTube ┌──────────────┐ Wi-Fi ┌───────────────────┐ internet ┌─────────┐ │ Rondo │ ─────────▶ │ browse + stream │ ──────────▶ │ │ │ music on SD │ ◀───────── │ (Node, yt-dlp) │ ◀────────── │ │ │ FM, Bluetooth│ audio, └───────────────────┘ └─────────┘ └──────────────┘ video`

The server browses YouTube for the Y1 with [youtubei.js](https://github.com/LuanRT/YouTube.js), finds the streams with [yt-dlp](https://github.com/yt-dlp/yt-dlp), and passes audio and video through to the Y1 in a form it can play. The Y1 only ever talks to your server.

## The project````````````````[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fdevice%2FREADME.md)[](https://github.com/jarvissax/rondo/blob/HEAD/docs/dev/)

| Folder | What's in it |
| --- | --- |
| app/ | Rondo itself, the Android app at the heart of the firmware (Kotlin, classic Views, ExoPlayer 2) |
| firmware/ | The script that builds the firmware (rom.zip) from the community's base ROM |
| server/ | The Rondo server (Node 22, TypeScript, Fastify) |
| infra/ | Docker and Caddy files for running the server |
| web-updater/ | The update page (WebUSB), published on GitHub Pages |
| tools/ | Mock servers for UI work, the boot screen generator, the version script |
| docs/ | Guides, plus notes on the Y1's internals and API references |

Every release is built the same way: the signed app goes up, and GitHub Actions builds the firmware from it and publishes the update page. To build it yourself, start with [Building Rondo](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fbuilding.md).

## Feedback and contributing

If you try Rondo on your Y1, I'd love to hear how it went, good or bad.
  - [Report a problem](https://github.com/jarvissax/rondo/issues/new?template=bug_report.yml)

if something doesn't work.
  - [Share an idea](https://github.com/jarvissax/rondo/issues/new?template=idea.yml) for

something you'd like Rondo to do.
  - [CONTRIBUTING.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2FCONTRIBUTING.md) says what feedback helps most, how to get Rondo's log,

and how to work on the code.

## Thanks

Rondo stands on other people's work:
  - The [y1-community](https://github.com/y1-community): its

[Innioasis Updater CE](https://github.com/y1-community/Innioasis-Updater), which installs Rondo, and its [Android 4.2 base ROM](https://innioasis.app/firmware.html?model=Y1&software=android-4-2-y1), with the Y1's Wi-Fi switched on, which Rondo's firmware is built from.
  - [Rockbox's Y1 port](https://github.com/multiwirth/rockbox-y1), whose wheel handling Rondo

copies, and the [JJ Launcher](https://innioasis.app/firmware.html?model=Y1&software=jj-launcher-y1) and [Inniclassic](https://innioasis.app/firmware.html?model=Y1&software=inniclassic-y1) launchers, which showed how the Y1's buttons behave.
  - youtubei.js, yt-dlp, ExoPlayer, OkHttp, NanoHTTPD, ZXing, Fastify,

sharp and the Roboto font. See [THIRD_PARTY_NOTICES.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2FTHIRD_PARTY_NOTICES.md).

## License and fine print

Rondo is released under the [MIT License](https://github.com/jarvissax/rondo/blob/HEAD/LICENSE).

Rondo is an independent project. It isn't affiliated with or endorsed by Innioasis, Google or YouTube. YouTube and YouTube Music are trademarks of Google LLC. Rondo reaches YouTube the same way other unofficial clients do, which YouTube's terms don't allow and which YouTube can break at any time. Use your own account, and use it at your own risk. The songs and albums in the pictures of the card's library are made up for the screenshots.

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
