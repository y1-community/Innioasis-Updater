---
title: "Reborn startup latency correction - Innioasis Updater"
description: "Reborn startup latency correction <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-validation-reborn-startup-02.html"
---

# Reborn startup latency correction - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn startup latency correction

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn startup latency correction > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

The owner-installed audio candidate was inspected read-only after the report that the startup splash remained visible for too long. The retained boot trace showed the splash visible at `0.828 s`, Y2ROOT completing its handoff at `12.246 s`, and the splash releasing/presenting at `52.047/52.060 s`.

The running Reborn process was created near `19.5 s`, but its first structured application record appeared near `41.0 s`. Its executable directly required all six FFmpeg shared libraries, so the ARM dynamic loader performed their cold relocation and constructor work before `main`. The remaining application trace took about `3.5 s` to reach the scan worker and `6.2 s` to create the Mali400 EGL context; first frame presentation followed at about `11.0 s` from the Reborn session start. A dirty FAT volume was also reported by the kernel, but it is an independent storage-health issue rather than the Reborn loader delay.

The correction keeps FFmpeg 9.0.1 authoritative and moves the media membrane behind a lazy shared boundary. The `reborn` ELF has no FFmpeg `DT_NEEDED` entries; `/usr/lib/reborn/libreborn_media.so` carries the six FFmpeg SONAMEs and is loaded on the first decoder, artwork, conversion, crossfade or runtime component request. Reborn now records millisecond startup phases, opens the GPU context before the library scan, and starts from `S05reborn` after `S02y2-data`. D-Bus, BlueZ, wpa_supplicant and connectivity remain worker dependencies with retry behavior, so early UI startup does not wait for radios.

Host and ARM validation completed for the candidate source: the workspace tests pass, the `reborn-media` crate passes strict Clippy, the ARM cross build passes with the production Buildroot SDK, the Buildroot package installs the shared membrane, and pinned QEMU runs the installed ARM binaries with the actual FFmpeg `9.0.1` runtime manifest. The next startup timing measurement requires the owner to install this root-only candidate; no physical retest is claimed by QEMU or host ELF inspection.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
