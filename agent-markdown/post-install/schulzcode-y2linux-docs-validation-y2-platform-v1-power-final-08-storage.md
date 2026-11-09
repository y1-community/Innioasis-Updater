---
title: "POWER-FINAL-08 — internal storage, SD handling, cumulative with 06 and 07 - Innioasis Updater"
description: "POWER-FINAL-08 — internal storage, SD handling, cumulative with 06 and 07 Status: implementation complete and offline-qualified; physical NOT RUN. The agent has not flash"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-08-storage.html"
---

# POWER-FINAL-08 — internal storage, SD handling, cumulative with 06 and 07 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-08 — internal storage, SD handling, cumulative with 06 and 07

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-08 — internal storage, SD handling, cumulative with 06 and 07

Status: implementation complete and offline-qualified; physical NOT_RUN. The agent has not flashed or provisioned. Readiness: MORE_WORK_REQUIRED.

Identity: Linux `d9fd5a7b57927fc22b4d62d9ee49a8e03c3cb170` (branch `codex/platform-v1-power-final-08`), Reborn `ac5502ea96f4d85a9cdbb32f210d46e658430abd`, kernel `6.18.0-y2linux-platform-v1-power-final-08`, root `2025.02.18-platform-v1.38`, release `1.0.0-platform-v1-power-final-candidate.8`. BOOTIMG `ad39788aa61303633d875ee4ff30068faa87ef5778496f31ec768144b449efb1`, Y2ROOT `e79bac968b559e19332a54dafa00566a552e028c0ea86999b46f2e8424eec71a`. Fallback pair = sealed 07.

## Findings that motivated it (live, 06 image, 2026-10-10)
  - MTP reported 808 MB / 511 MB: Internal Storage was a folder on the 800 MiB Y2DATA; the SD filesystem was a 512 MiB root-image copy on a 121 GiB partition (also carrying the root's `Y2ROOT` label and a UUID in the root's family).
  - eMMC is 7423 MiB; p8 (5596 MiB, stock FAT, serial 3F93-07E6, 541 files/31 MB, stale dirty bit) was unused and write-blocked by the guard. File-level backup retained.
  - MTP throughput (libusb direct, 06): upload 8.4-11 MB/s, download about 37.7 MB/s on both volumes, hashes verified.

## Changes
  - eMMC write guard: one added span (3742720 to the exposed disk end). Tests pin ANDROID, USRDATA, p8 and every native sector reachable by a write; straddling spans, CACHE, boot/protected areas, the disk-end sector and the hidden tail stay refused. Owner-approved in chat 2026-10-10; audit entry in `docs/planning/roadmap-gap-audit.md`.
  - Y2Media (`tools/platform/y2_platform/internal_media.py`): exact-geometry/label/UUID mount after `e2fsck -p`, ready record, `/media/internal`, never boot-critical (`S02y2-media`). Explicit `provision` names the stock serial, refuses mounted/other filesystems, migrates `/data/music` with SHA-256 and removes originals only after full verification (symlinks/special files/oversize/target-differs abort with originals intact).
  - Exports: MTP Internal Storage = `/media/internal/music` (same fixed slot); SFTP root and the verified-upload tool follow it (cross-filesystem publish by verified copy + non-replacing link); storage status has a fourth volume; health, capabilities, bench and the USB qualification harness know it; factory reset leaves Y2Media music.
  - SD: `media format`/`grow` (CID-confirmed, only the card controller), undersized report, recycled-mount-id marker fix, `resize2fs`.
  - Reborn: internal music directory chosen from the platform's Ready record (this boot, this mount) with legacy fallback; internal volume/diagnostics follow it.

## Tests
  - Locked-container production suite (`tools/production/tests.sh`): PASS, 629 cases (07: 598). The first run stopped at one stale fixture (`mmc-transport-main.c` still listed p8's first sector as protected); fixed in commit `c65080d` and the suite re-run complete (first-run log kept as `production-tests-first-run-fail.log`).
  - 29 packaging-host and 27 native splash cases PASS; package, ELF closure (385 files / 1416 edges), installed-ARM, release inventory and privacy (tree and root image) PASS.
  - Host broad run: 691 tests (07: 660), the same 48 environment errors (missing pyelftools) as 07, none new.
  - New: `tests/test_internal_media.py` (15), `tests/test_media_change.py` (13); extended transfer (3), eMMC guard, USB views and harness tests. Reborn: `cargo fmt`, strict Clippy, full workspace tests PASS (including 2 new storage tests and 1 client test).
  - Physical: NOT_RUN. Not tested: provisioning on the device, MTP to Y2Media, Reborn library rescan after the root change, power loss on Y2Media, 06 power-down.

## Verdict

IMPLEMENTATION_READY_PROVISIONING_PENDING

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
