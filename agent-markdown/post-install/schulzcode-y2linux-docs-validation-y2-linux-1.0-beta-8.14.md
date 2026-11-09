---
title: "Y2Linux 1.0 Beta 8.14 (Baseline 111) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 8.14 Baseline 111 Status: PUBLISHED as GitHub release baseline-111 2026-10-20. Release 1.0.0-beta.8.14 , Reborn 1.0.0-beta.8.14 , kernel 6.18.56-y2linux-"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-8.14.html"
---

# Y2Linux 1.0 Beta 8.14 (Baseline 111) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 8.14 (Baseline 111)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 8.14 (Baseline 111)

Status: PUBLISHED as GitHub release `baseline-111` (2026-10-20). Release `1.0.0-beta.8.14`, Reborn `1.0.0-beta.8.14`, kernel `6.18.56-y2linux-1.0.0-beta.8.14`, update sequence 7800, Linux `8e21366`, Reborn `5cda8bb`. Built with `tools/production/release.py` (130 s, resumed workspace, update based on `baseline-110`): container suite 842 OK, Reborn tests and Clippy (`-D warnings`) clean; all seal checks PASS, no MediaTek firmware in any image. Build 111 itself was installed on the maintainer's player over the air and checked by the owner (below). Owner: "build 8.14 with 1–4 and publish it". Milestone audit BETA-8.14 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | 71db0088e3f5fb62fa32699a70636a754834c8c282dfe13fe2ab514cde21bbcf |
| Y2ROOT | 25301d97268bf24d0dd3dc22cb3d9cc52d92849ca729df683e5653813058de96 |
| RECOVERY | 445bee09645e4d2a4beac71bc0f178e85366af1a770b291d09660a5cc0c9b26e |
| Y2DATA (no SSH key) | ce7d1b76dbc06d1319aedf0b8e9b37d746e0dd5100a3e5910c0f797bc2266d3c |

## What changed since Beta 8.13````````````````````````

| Request / report | Cause | Change |
| --- | --- | --- |
| "Every shuffle is the same order" | The shuffle seed was the start song's ID plus its index (main.rsplay_members), and Shuffle rows always started on the first song: identical order every time | Seed from getrandom per shuffle (reborn_platform::random_u64), splitmix64 with a 64-bit range reduction; a Shuffle row lets any song start; a song picked with Shuffle on still plays first. Reborn 2861ec9, tests shuffle_and_seek_tests |
| "Seeking jumps ~30 s per tick" | A held Previous/Next sent Seek(±30 000) every 90 ms (≈ 5.5 min of song per second) | The UI sends the direction; the step is 1 s for the first 1.5 s held, then 3 s, then 10 s, at most 1/60 of the song (Reborn 2861ec9) |
| "All Songs and Shuffle on Genres" | All Songs existed since 8.8; Shuffle did not | A Shuffle row under All Songs on a genre (also in Cover Flow) |
| "Long titles push into the menu" | The Home card's now-playing title was drawn unshortened at x=356 | Fitted to 200 px with an ellipsis, like the line below |
| Report bf017f02: storage_error "I/O error, dev mmcblk0 … WRITE_ZEROES" during the Internal Storage setup | The eMMC advertised TRIM, so mke2fs's zero-out became an erase, which the MSDC guard refuses (storage-policy.h); the kernel then wrote zeros, data fine | Overlay 0009: the guarded eMMC marks TRIM broken in init_card, so zero-outs write zero pages (Linux f9a3bd8) |

## Device results (build 111, maintainer's player)````

| Check | Result |
| --- | --- |
| OTA 8.13 → 8.14 (stage + apply) | Acknowledged 7800, Reborn health ok |
| /sys/block/mmcblk0/queue/write_zeroes_max_bytes | 51 904 512 on 8.13 → 0 (discard still advertised, 104 MB, unused: nodiscard, no discard mount, no fstrim) |
| Shuffle twice on an album, held Next, genre Shuffle row, long title on Home | checked by the owner on the player: all as intended |

## Known gaps
  - The seek schedule is a first tuning; it may change with more feedback.
  - Japanese/Chinese/Korean text still shows "�" (planned next: a Noto Sans CJK fallback with a runtime glyph cache).
  - USB DAC output needs a hardware check of the port's 5 V supply first; video playback is not planned for 1.0.
  - Unchanged from 8.13: Strawberry itself not run, Windows Explorer display of music Names, slow crystal, sleep with a

parked CPU, #47 confirmation, WAF rule and billing alert, sleep drain (#42), GC9503V confirmation (#45).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
