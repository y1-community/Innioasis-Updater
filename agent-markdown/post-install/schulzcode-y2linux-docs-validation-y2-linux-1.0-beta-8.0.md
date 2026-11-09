---
title: "Y2Linux 1.0 Beta 8.0 (Baseline 75) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.0 Baseline 75 Status: PUBLISHED as GitHub release baseline-75 2026-10-18, after the device check on the owner's player. Release 1.0.0-beta.8.0 , Reborn"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.0.html"
---

# Y2Linux 1.0 Beta 8.0 (Baseline 75) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.0 (Baseline 75)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.0 (Baseline 75)

Status: PUBLISHED as GitHub release `baseline-75` (2026-10-18), after the device check on the owner's player. Release `1.0.0-beta.8.0`, Reborn `1.0.0-beta.8.0`, kernel `6.18.56-y2linux-1.0.0-beta.8.0`, update sequence 6400, Linux `662ff11`, Reborn `1b3a5c1`. Built with `tools/production/release.py` in 100 s on top of Baseline 74: container suite 767 OK, all seal checks PASS, no MediaTek firmware in any image. The fixes come from the 1.0 review ([V1-RELEASE-READINESS](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FV1-RELEASE-READINESS.md), [V1-CODE-REVIEW](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FV1-CODE-REVIEW.md)); milestone audit BETA-8.0 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 527103ee9ee2c839759fdb25791618af09b89d08589f3aec74aea672672379ee |
| Y2ROOT | d977ffaaf69f7a01304aee9f09ed17b370bb248d74cb0bee89fb129d6cb5a943 |
| RECOVERY | a3a821653e47b2507ad18f6b36ec2a544b474cbf9bca7c045ecc14a8ac4b8087 |
| Y2DATA (no SSH key) | b54f5f3377e90734d61abef905f5aa703a0ad153a0e94741c19bdbca42e5fe84 |

## Since Beta 7.11``````````````````````````````````````````````````````````

| Review ID | Part | Change |
| --- | --- | --- |
| B3, B4, P2 | Library (Reborn d11563b) | A supported file FFmpeg cannot open no longer makes a scan incomplete: it is counted (unreadable, Settings → Library N can't be read), keeps its row and no longer stops pruning of deleted songs; the scanner remembers it for the process. Before, one such file left library.error set after every scan. |
| B3, R7 | Update health (Linux e361b8b, Reborn d11563b) | rebornctl status carries healthy + health_reasons (drawing, database working, no stuck worker); health_ack uses it. Before, one unreadable song rolled every OTA back 180 s after install. |
| B7 | Session (Reborn d11563b) | A session Reborn refuses (e.g. after a rollback from a newer release) is kept as session.json.rejected-<time>; every setting this version understands is recovered. |
| B5, R5, P1 | SD admission (Linux 3bc6abb) | media reconcile runs as its own process (150 s limit, then 10 min back-off) instead of with a 7 s deadline inside the service loop; command() kills every descendant on timeout. Before, a card whose check outlasted 7 s never mounted and checkers piled up. |
| B6 | USB receive DMA (Linux ca119ff, overlays 0055/0065) | A multi-packet start that gives up first stops the engine (y2_hsdma_stop) and looks: nothing moved → PIO as before; whole packets → counted, CPU continues; part of one → flushed, request fails with -EIO (host repeats). |
| B8 | Recovery (Linux ebc164e) | A stuck installer powers off after ten minutes without a charger (request kept). |
| R6 | Internal Storage (Linux f261044) | Mounted with noinit_itable, made with nodiscard: no refused background zeroing at every start. |
| A7 | Licensing (Linux 9c45e5c, 662ff11) | New asset Y2Linux-sources-toolchain-f7cda4c7d213.tar: glibc 2.44 snapshot and GCC 15.3.0 sources of the Bootlin toolchain, byte-identical to Buildroot's pinned archives, with the toolchain's summary.csv. |
| B1/A3, A4, A5, A12, A13 | Docs and packages (Linux a90ba0c) | The first-install and computer-update packages ship docs/INSTALL.md as install.md (was a historical runbook); only firmware v3.2.0 works, said loudly; current tag in BUILDING; old feature audit retired; catalog complete. |
| R4 | Audio (Reborn 1a3afc2) | The wired profile check matches whole rates (8000 no longer matched inside 48000). |

## Device result (owner's player, 2026-10-18)``````````````````````````````````

| Check | Result |
| --- | --- |
| OTA install 6352 → 6400 (update stage + apply) | Signature and payloads verified, recovery installed, back after 75 s |
| Health acknowledgement | Acknowledged 6400 at ≈67 s uptime; Reborn healthy: true, library 311 songs, no error |
| B3 on the device | Random 4 KB y2-audit-broken.mp3 on Internal Storage, rescan: unreadable: 1, library.error none, healthy: true; file removed, next scan unreadable: 0 |
| R6 | noinit_itable in /proc/mounts, no mmc_erase line in the kernel log |
| Receive DMA | 256 MiB over SSH (scp) to Internal Storage, SHA-256 identical after a cache drop; 128 MiB piped through ssh identical. Counters m1_prog = dma_done + m1_end (187 101 = 185 725 + 1 376), m1_kick 0, m1_fallback 0 |
| Kernel log | No oops, BUG or warning |

Upload over SSH ran at 8.4 MB/s (scp) and 9.5 MB/s (ssh pipe) with the player idle: the SSH cipher on the one online core is the limit there; the Beta 7.11 figure of 10–14 MB/s for USB Ethernet was a different measurement. MTP uploads (29.6 MB/s in 7.11) use the same receive path, whose normal operation is unchanged.

## Known gaps

Not run with this release: MTP copies (the player was in developer USB mode), the cable pulled mid-copy, sleep and wake, Windows Explorer, a large or slow SD card for B5, the stuck-installer power-off (B8, covered by the fixture test only). Still open from the readiness audit: standby drain (A1, #42), an install and a build by someone else (A2), the owed device checks (A8, A9, A11), headphone detection (A10), and the owner decisions A14/R3, A16, A18.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
