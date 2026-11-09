---
title: "Third-party software - Innioasis Updater"
description: "Third-party software Rondo is MIT-licensed see LICENSE (LICENSE). It's built on the projects below, each under its own license. In the Android app and the APK Project Lic"
language: "en"
source: "https://innioasis.app/post-install/jarvissax-rondo-third_party_notices.html"
---

# Third-party software - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y1&software=rondo-y1)

Post-install setup · Rondo · Y1

# Third-party software

A lightweight, custom audio operating system for the Innioasis Y1.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y1&software=rondo-y1)[Install guide](../guide.html?model=Y1&software=rondo-y1)

# Third-party software

Rondo is MIT-licensed (see [LICENSE](https://github.com/jarvissax/rondo/blob/HEAD/LICENSE)). It's built on the projects below, each under its own license.

## In the Android app (and the APK)[](https://github.com/google/ExoPlayer)[](https://github.com/square/okhttp)[](https://developer.android.com/jetpack/androidx)[](https://kotlinlang.org)[](https://github.com/NanoHttpd/nanohttpd)[](https://github.com/zxing/zxing)[](https://github.com/googlefonts/roboto-3-classic)``[](https://letsencrypt.org/certificates/)

| Project | License |
| --- | --- |
| ExoPlayer 2.19.1 | Apache-2.0 |
| OkHttp 3.12 and Okio | Apache-2.0 |
| AndroidX (appcompat, core, recyclerview, media, multidex, lifecycle) | Apache-2.0 |
| Kotlin standard library, kotlinx.coroutines, kotlinx.serialization | Apache-2.0 |
| NanoHTTPD | BSD-3-Clause |
| ZXing (QR codes) | Apache-2.0 |
| Roboto font | SIL Open Font License 1.1 (see app/app/src/main/assets/fonts/NOTICE.txt) |
| ISRG Root X1 and ISRG Root YR certificates (Let's Encrypt) | public certificates |

## In the server[](https://github.com/LuanRT/YouTube.js)[](https://github.com/fastify/fastify)[](https://github.com/nodejs/undici)[](https://github.com/lovell/sharp)

| Project | License |
| --- | --- |
| youtubei.js | MIT |
| Fastify and @fastify/rate-limit | MIT |
| undici | MIT |
| sharp (with libvips) | Apache-2.0 (libvips: LGPL-3.0) |

## In the firmware (`rom.zip`)

The firmware is built from the y1-community's [Android 4.2 base ROM](https://innioasis.app/firmware.html?model=Y1&software=android-4-2-y1) (`firmware/build.sh` downloads it): Android 4.2.2 from the Android Open Source Project (mostly Apache-2.0) with the Y1's MediaTek drivers and system files as Innioasis shipped them. Rondo takes apps out of it and adds its own; it redistributes the rest unchanged, as the base ROM does.

## In the update page[](https://github.com/yume-chan/ya-webadb)``[](https://github.com/evanw/esbuild)

| Project | License |
| --- | --- |
| Tango (@yume-chan/adb and its WebUSB and credential packages) | MIT |
| esbuild (build only) | MIT |

## Downloaded when the server's Docker image is built or started

These aren't part of this repository. The Docker image fetches them from their own projects.[](https://github.com/yt-dlp/yt-dlp)[](https://github.com/denoland/deno)[](https://ffmpeg.org)[](https://nodejs.org)[](https://github.com/caddyserver/caddy)``

| Project | License |
| --- | --- |
| yt-dlp | Unlicense |
| Deno | MIT |
| FFmpeg (Debian package) | LGPL-2.1+ / GPL-2.0+ |
| Node.js | MIT |
| Caddy (with compose.vps.yaml) | Apache-2.0 |

YouTube and YouTube Music are trademarks of Google LLC; their logos are shown to identify the services. Innioasis and Y1 are trademarks of their owner. Rondo isn't affiliated with or endorsed by either.

These are Rondo's own instructions, shown here word for word.

Published by the [jarvissax/rondo](https://innioasis.app/firmware.html?model=Y1&software=rondo-y1) project [[1]](https://innioasis.app/firmware_info.html?repo=jarvissax%2Frondo&software=rondo-y1)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Ajarvissax)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
