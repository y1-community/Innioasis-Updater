---
title: "Building Rondo - Innioasis Updater"
description: "Building Rondo This page is for building Rondo from source and working on it. To just use it, see Installing Rondo install.md. What's where app/ Rondo, the Android app at"
language: "en"
source: "https://innioasis.app/post-install/jarvissax-rondo-docs-building.html"
---

# Building Rondo - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y1&software=rondo-y1)

Post-install setup · Rondo · Y1

# Building Rondo

A lightweight, custom audio operating system for the Innioasis Y1.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y1&software=rondo-y1)[Install guide](../guide.html?model=Y1&software=rondo-y1)

# Building Rondo

This page is for building Rondo from source and working on it. To just use it, see [Installing Rondo](https://innioasis.app/guides/rondo-y1.html).

## What's where`app/ Rondo, the Android app at the heart of the firmware (Kotlin, classic Views) app/src/main/java/com/jarvissax/rondo/ ui/ screens, the row list, icons, the theme player/ playback service, ExoPlayer setup, FM radio, lyrics input/ wheel and button handling, vibration local/ the music and videos on the card, playlists net/ the server API, TLS for Android 4.2 dashboard/ the dashboard's web server (the page itself is in assets/dashboard/) firmware/ build.sh, which makes the firmware (rom.zip) from the community's base ROM server/ Rondo server (Node 22, TypeScript, Fastify) src/ routes, YouTube browsing, stream resolving, the range proxy, the admin API admin/ the admin page (plain HTML, CSS and JS) test/ unit tests (vitest) infra/ Dockerfile, compose files, Caddyfile web-updater/ the update page (WebUSB) tools/ dashboard and admin mocks, boot screen generator docs/ guides; device/ holds notes on the Y1, dev/ the API references`

## The app

### What you need

| JDK | 17. Newer JDKs (like the one bundled with recent Android Studio) can't run Gradle 8.9. |
| --- | --- |
| Android SDK | platform 34 and build tools 34, which Gradle downloads on the first build |
| A Y1 with the Rondo firmware | there's no emulator for a click wheel |

Point Gradle at the SDK with `app/local.properties` (Android Studio writes it for you):`sdk.dir=/path/to/Android/sdk`

### Build and run`cd app RONDO_SIGNING=/path/to/keystore.properties ./gradlew :app:assembleRelease adb install -r app/build/outputs/apk/release/app-release.apk`

On the Rondo firmware, Rondo is a built-in app, and `adb install -r` installs a build over it the way an update does: Android keeps the firmware's copy and runs yours, with the same built-in permissions, and everything else stays. adb is on in the firmware; when the Y1 offers the USB drive, choose Not now.

Android only accepts a build signed with the same key as the Rondo in the firmware. To work with your own key (or debug builds), build a firmware with your APK in it once (below) and install that; after that, `adb install -r` takes your builds. A new permission in the manifest is only granted to the firmware's copy, so that one needs a new firmware too.

Rondo logs under the tag `Y1`:`adb logcat -v time -s Y1`

### Rules of the road

The Y1 runs Android 4.2 (API 17), which decides a lot:
  - minSdk 17. Anything that needs API 21 or later is out: Jetpack Compose, Media3, OkHttp 4,

Coil, recent Room. The app uses classic Views, ExoPlayer 2.19.1 (the last ExoPlayer 2) and OkHttp 3.12.13 (the last line that runs below API 21). `androidx.media` stays at 1.6.0, because 1.7.0 needs API 19.
  - TLS: Android 4.2 has TLS 1.2 switched off and doesn't trust Let's Encrypt. `net/Tls.kt`

turns it on and bundles the ISRG roots.
  - The screen is 480×360 and reports mdpi, but it's dense (about 250 ppi). Sizes go through

`dp()`, which scales by the text-size setting.
  - The GPU renderer on 4.2 has quirks: shapes drawn under a scale come out blurry, and

`TransitionDrawable` backgrounds stall. Comments in the code point these out where they matter.

[docs/device/README.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fdevice%2FREADME.md) collects what's known about the Y1 itself: the wheel's key events, the FM chip, the audio paths and the video decoder's timestamp bug.

## The firmware

`firmware/build.sh` turns the y1-community's [Android 4.2 base ROM](https://innioasis.app/firmware.html?model=Y1&software=android-4-2-y1) (Type A) into the Rondo firmware, with the APK you give it:`firmware/build.sh app/app/build/outputs/apk/release/app-release.apk # writes firmware/out/rom.zip`

It needs curl, unzip, zip, JDK 17 and e2fsprogs (`brew install e2fsprogs` on macOS, `apt install e2fsprogs` on Debian and Ubuntu). It downloads the base ROM once (checking its SHA-256), then edits the system and data images in place with debugfs, so nothing is mounted and no root is needed:
  - everything in `/system/app` goes except Android's background services and Rondo, including

Rockbox, the Innioasis player, SystemUI, Settings and the keyboard;
  - Rockbox's button layout and switching scripts go, and the data image is emptied;
  - Rondo goes in as `/system/app/Rondo.apk`, with its boot logo and animation

(`tools/bootscreen/`) and the build name `Rondo <version>`;
  - `fw_package.ini` and `updater.png` tell Innioasis Updater CE what it's installing.

It checks both file systems afterwards and stops if anything is off. Install the result with Innioasis Updater CE: Settings › Install from a file…. The Updater keeps an unpacked copy of each package and reuses it for a file of the same name, so give each build its own name (or delete the copy, see [docs/device](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fdevice%2FREADME.md%23the-rondo-firmware&anchor=the-rondo-firmware)). It also deletes the zip once it has unpacked it, so install a copy of a build you mean to publish.

The firmware has no SystemUI, so Rondo does its visible jobs: the click on each wheel step, the low battery warning, the wallpaper Android waits for before it ends the boot animation, and a power screen for when Power is held. [docs/device](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fdevice%2FREADME.md%23the-rondo-firmware&anchor=the-rondo-firmware) has the details.

## The server`cd server npm ci npm test # unit tests npm run typecheck`

To run it locally, put the settings in `server/.env` (it's gitignored):`YTDLP_BIN=/path/to/yt-dlp CONFIG_FILE=./data/config.json COOKIES_FILE=./data/secrets/cookies.txt TV_TOKENS_FILE=./data/secrets/tv-oauth.json`

Then `npm run dev` starts it on port 3000 and reloads on changes. Its log prints the setup code for `http://localhost:3000/admin`. yt-dlp also needs [deno](https://deno.com) on the PATH for YouTube's challenges. The Docker image (`infra/Dockerfile`) brings yt-dlp, deno and ffmpeg along.

To run your own build in Docker instead of the published image, add the build override to either compose file: `docker compose -f infra/compose.home.yaml -f infra/compose.build.yaml up -d --build`. It also leaves the updater off.

The updater (`src/updater/`, built into its own small image by `infra/updater.Dockerfile`) runs next to the server with Docker's socket. When the admin page's Update asks (through `src/serverUpdate.ts`, with a token the two share on a small volume), it pulls the image the `rondo` container runs, and if it's new, recreates the container on it the way `docker compose` would: same name, volumes, ports, networks and environment, with only the image's own defaults taken from the new image. The old container waits, stopped, until the new one answers `/healthz`, and comes back if it doesn't. It speaks Docker's API from 1.40 up (Docker 29 refuses older clients) and touches no other container. `test/updater.test.ts` covers it with a pretend Docker.

Two rules the server keeps:
  - youtubei.js for browsing, yt-dlp for streams. Everything the user sees (home pages, search,

playlists, up next) comes from youtubei.js. yt-dlp only turns a video ID into stream URLs.
  - No media on disk. Audio and video are proxied as they're requested. Caching metadata (stream

URLs, index ranges, thumbnails) is fine; caching media isn't.

The API is described in [docs/dev/server-api.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fjarvissax%2Frondo%2Fblob%2FHEAD%2Fdocs%2Fdev%2Fserver-api.md).

## Working on the dashboard or admin page

Both pages are plain HTML, CSS and JavaScript, and each has a mock server with made-up data, so you can work on them in a desktop browser without a Y1 or a real server:`node tools/dashboard-mock/server.mjs # http://localhost:8090, prints the pairing code node tools/admin-mock/server.mjs # http://localhost:8095/admin, prints the password`

Each mock lists its options (empty card, slow device, first run, signed out and so on) at the top of its file. The dashboard's files are in `app/app/src/main/assets/dashboard/`; on a real Y1 you need to rebuild the app to see changes. The admin page is in `server/admin/`.

## The update page

`web-updater/` is the page at jarvissax.github.io/rondo: plain HTML and CSS, plus a script bundled with esbuild. It talks to the Y1 with [Tango](https://github.com/yume-chan/ya-webadb) over WebUSB, checks that the Y1 runs the Rondo firmware, and installs the newest `rondo.apk` with `pm install -r` (`src/updater.js`).`cd web-updater npm ci npm run dev # http://localhost:8000, with the locally built release APK if there is one`

Run `adb kill-server` first; the browser can't claim the Y1 while adb holds it. One thing to know about Android 4.2: its adb only has the old `shell:` service, not the `exec:` one Tango's subprocess helpers use (that arrived in Android 5), so `updater.js` opens `shell:` sockets itself.

The page is published by `.github/workflows/release.yml` whenever a release is published, with that release's APK next to it as `rondo.apk` and `latest.json` (version, size, firmware number, release notes). The dashboard's Install button downloads updates from there too, because GitHub Pages lets any page fetch its files and GitHub's release downloads don't. In the repository's settings, Pages must be set to GitHub Actions.

## Updates

Three ways in, one way of installing: the APK goes over the firmware's Rondo with Android's `pm install -r` (`SoftwareUpdate.kt` on the Y1), which needs `INSTALL_PACKAGES`, a permission Android 4.2 gives built-in apps. Android stops Rondo, swaps it and starts it again as the home screen, in about 10 seconds.
  - Settings › Software update asks the server (`GET /update`, `GET /update/rondo.apk`; the

server reads the update page's `latest.json` and passes the APK through).
  - The dashboard sends the APK the browser downloaded, or a file, to `PUT /api/update`.
  - The update page copies it over USB and runs `pm install -r` itself.

All three learn of a release from `latest.json`, which appears only once the release's `rom.zip` is built, so they agree with each other and with Innioasis Updater CE.

An update is just the APK, so it can't change the firmware around Rondo. A release that does raises the firmware number, `firmwareLevel` in `app/app/build.gradle.kts` (1 so far): `firmware/build.sh` writes it into the firmware as `ro.rondo.firmware`, and the APK names it in its manifest (`rondo.firmware`). A Y1 whose firmware is older than a release needs is told to install that release with Innioasis Updater CE instead (with Keep Data, where the Updater offers it, to keep its settings): Settings › Software update and the dashboard show no Install button, the update page won't start, and `SoftwareUpdate.kt` refuses the APK however it arrives. The first Rondo firmware (1.0.0) has no number and counts as 1.

## Making a release
  - Set the version everywhere at once: `tools/set-version.sh 1.0.2` (the app's `versionName` and

`versionCode`, the server's and the update page's `package.json`). If the release changes the firmware around Rondo (a new built-in permission, a change to `firmware/build.sh`), raise `firmwareLevel` in `app/app/build.gradle.kts` too.
  - Build the release APK with the signing key. `RONDO_SIGNING` points at a `keystore.properties`

kept outside the repo (with `storeFile`, `storePassword`, `keyAlias` and `keyPassword`):
` cd app RONDO_SIGNING=/path/to/keystore.properties ./gradlew :app:assembleRelease apksigner verify --min-sdk-version 17 app/build/outputs/apk/release/app-release.apk`
  - Try it on a Y1: `adb install -r` the APK over the previous release to check updating. When the

firmware changes, also build it (`firmware/build.sh app/app/build/outputs/apk/release/app-release.apk`) and install `firmware/out/rom.zip` with Innioasis Updater CE.
  - Add the release to `CHANGELOG.md`, in words a Y1 owner understands. Commit, tag `v<version>`,

push both, and publish a GitHub release for the tag with one asset: `rondo-<version>.apk` (the APK from step 2, renamed). Say in the notes that it's for the Y1, Type A, and whether it needs Innioasis Updater CE (a new firmware number).
  - Publishing starts `.github/workflows/release.yml`, which checks that the tag, the versions and

the APK agree, builds the firmware from that APK and attaches `rom.zip` (the name Innioasis Updater CE reads as Y1 Type A) and `updater.png` (its picture for the release), builds the server and updater images for x86-64 and 64-bit ARM and publishes them as `ghcr.io/jarvissax/rondo-server` and `rondo-updater` (`<version>` and `latest`), then republishes the update page with the new `latest.json`. It takes about 20 minutes; if it fails, fix the cause and run it again from the Actions tab (it redoes the latest release). The first time the images are published, set both packages to Public on GitHub (your profile › Packages › the package › Package settings), or servers can't download them.

Innioasis Updater CE lists every release of this repository that has a `rom.zip`, so a new one shows up there by itself (the Updater keeps its list for up to a day). Every APK has to be signed with the same key, or it won't install over the previous Rondo. Keep the key backed up somewhere safe.

GitHub Actions builds the app and the update page and runs the server tests on every push (`.github/workflows/ci.yml`).

## Extras

### Boot screens

`tools/bootscreen/BootScreen.java` draws Rondo's boot logo and its boot animation, a spinning click wheel, as Android's `bootanimation.zip`. The firmware build puts both in. To try a change to the animation without a new firmware:`java tools/bootscreen/BootScreen.java out/ adb push out/bootanimation.zip /data/local/bootanimation.zip`

Android plays `/data/local/bootanimation.zip` in place of the system's own. Nothing on the system partition changes, and `adb shell rm /data/local/bootanimation.zip` brings the old one back.

These are Rondo's own instructions, shown here word for word.

Published by the [jarvissax/rondo](https://innioasis.app/firmware.html?model=Y1&software=rondo-y1) project [[1]](https://innioasis.app/firmware_info.html?repo=jarvissax%2Frondo&software=rondo-y1)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Ajarvissax)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
