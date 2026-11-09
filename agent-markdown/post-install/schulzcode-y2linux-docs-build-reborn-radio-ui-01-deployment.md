---
title: "Reborn radio scan UI correction - Innioasis Updater"
description: "Reborn radio scan UI correction <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-reborn-radio-ui-01-deployment.html"
---

# Reborn radio scan UI correction - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Reborn radio scan UI correction

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Reborn radio scan UI correction > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Ready for owner manual installation; physical qualification pending. This is a root-only application correction over the installed REBORN-SPLASH-01 system.

Scan now enables its radio, reports Starting/Scanning, publishes results, and reports empty or failed scans. Off is distinguished from unavailable; radio errors stay on their own screens. Discovery is bounded. New `rebornctl wifi` and `rebornctl bluetooth` scan/on/off commands exercise the actual UI workers.

Built source `a8ae8b6723311b677662759082c55ad226441669`; integration `640ecb828af1ba48edcc6203701edb89f66eb0ac`. The exact images, tests, implementation, manual install/rollback and SSH qualification procedure are recorded at `/home/luca/Dokumente/Code/Y2Reborn/docs/validation/REBORN-RADIO-UI-01.md` and in the package's `INSTALL.md`.

Package: `/home/luca/Dokumente/Code/Y2Linux/out/REBORN-RADIO-UI-01`.``````````

| Payload | SHA256 |
| --- | --- |
| Y2ROOT.img | 79b12172645c4755fdf3219fc6f99971d94de62c42f807a3613a43516d1f7df8 |
| fallback/Y2ROOT.img, exact installed splash root | d40e9337e3a1149d12fdd240a59918b0d2c48e4e6a9974ab5b470685250d900c |
| Existing BOOTIMG, unchanged | 8671de2900fd05cc80a9eb7a3541d5bbdab7e5dd96c18f73f44ca1b13beb19a5 |

Use MT6582_reborn_root_only_scatter.txt, Download Only, ANDROID only. Keep BOOTIMG, USRDATA and all other rows unchecked/NONE; preserve Y2DATA. Do not reuse the preceding splash package's two-image scatter. Fallback is also root-only.

The [validation receipts](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Freborn-radio-ui-01%2FREADME.md) record 64 Rust tests, 20 daemon checks, four tooling tests, eight ARM runtime/shell checks, Clippy, an offline production build, raw ext4 checks and exact content comparison. Only two application binaries and three build identity files change. Root usage increases by 52 KiB; the kernel, native libraries, services, firmware, splash, charging program and partition geometry remain unchanged. No live install or radio setting change was performed while developing this correction.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
