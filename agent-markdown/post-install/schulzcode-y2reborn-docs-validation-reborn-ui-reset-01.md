---
title: "Reborn UI reset 01 - Innioasis Updater"
description: "Reborn UI reset 01 <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-validation-reborn-ui-reset-01.html"
---

# Reborn UI reset 01 - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn UI reset 01

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn UI reset 01 > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

This is the presentation-layer reset for the supplied Reborn Y2 UI Implementation Pack. It keeps the existing playback, media, library, storage, radio, power, persistence, diagnostics, and service architecture. Y2Linux was not modified.

## Source and artifacts
  - implementation commits: `bd28e10` (reset), `c2ab6cb` (wired-control audit), `404cb42` (radio-forget fix)
  - recoverable pre-reset checkpoint: `0a104dd`
  - ARM target: `armv7-unknown-linux-gnueabihf`, Cortex-A7 hard-float
  - production SDK used: `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-reborn-audio-final/buildroot`
  - production bundle: `out/reborn-ui-reset-01/`
  - checksum file: `out/reborn-ui-reset-01/SHA256SUMS`

The stripped ARM candidate binaries are:````````

| File | Bytes | SHA-256 |
| --- | --- | --- |
| armv7/release/reborn | 2,448,588 | feeed433ba44d4d57d865bfe7b4d845a098326ac2bf1fb19664443b4aa1d5ae0 |
| armv7/release/rebornctl | 445,532 | 77d5e93e53d89fe46f000c3b1f54eb09f445db0bcd516cc908de9753926b6f18 |

Rollback binaries were built from checkpoint `0a104dd`:````````

| File | SHA-256 |
| --- | --- |
| fallback/armv7/release/reborn | 5bc77f2109271fdf6b48c70b24a2d1a02ba06ac3da26b35f9b2086090509d21c |
| fallback/armv7/release/rebornctl | 0ea4ea80f39ff629f2a8c078cc66a5c040e8d304bb1240cb4be691e75db480af |

The bundle contains eight deterministic 480x360 PNG previews and a manifest. No Y2ROOT image was produced because normal UI logic belongs in Y2Reborn and Y2Linux was intentionally left unchanged. QEMU runtime qualification was not run because `qemu-arm` is not installed on this host; physical installation and device qualification are pending owner action.

## Manual SSH installation

This is a userspace replacement only. Do not flash partitions and do not alter Y2DATA. Use the existing owner SSH workflow and substitute its approved host, known-hosts file, and identity below:`cd /home/luca/Dokumente/Code/Y2Reborn/out/reborn-ui-reset-01 (cd . && sha256sum -c SHA256SUMS) scp armv7/release/reborn <owner-host>:/tmp/reborn.ui-reset-01 scp armv7/release/rebornctl <owner-host>:/tmp/rebornctl.ui-reset-01 ssh <owner-host> ' set -eu test "$(sha256sum /tmp/reborn.ui-reset-01 | cut -d" " -f1)" = 609329f4a932b5c6ee360392756a93de7e5cf0f82b396c8fb65cecd42314d6cc test "$(sha256sum /tmp/rebornctl.ui-reset-01 | cut -d" " -f1)" = 77d5e93e53d89fe46f000c3b1f54eb09f445db0bcd516cc908de9753926b6f18 /etc/init.d/S05reborn stop cp -p /usr/bin/reborn /data/reborn/state/reborn.pre-ui-reset cp -p /usr/bin/rebornctl /data/reborn/state/rebornctl.pre-ui-reset install -m 0755 /tmp/reborn.ui-reset-01 /usr/bin/reborn.ui-reset-01 install -m 0755 /tmp/rebornctl.ui-reset-01 /usr/bin/rebornctl.ui-reset-01 mv -f /usr/bin/reborn.ui-reset-01 /usr/bin/reborn mv -f /usr/bin/rebornctl.ui-reset-01 /usr/bin/rebornctl /etc/init.d/S05reborn start rebornctl status --json '`

If the health check fails, stop Reborn, restore the two backups from `/data/reborn/state/` to `/usr/bin/reborn` and `/usr/bin/rebornctl`, then run `/etc/init.d/S05reborn start`. The fallback binaries in this bundle are also available for a controlled rollback. No private SSH key is part of the bundle.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
