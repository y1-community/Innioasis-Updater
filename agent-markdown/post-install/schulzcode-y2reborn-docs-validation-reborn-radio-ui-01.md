---
title: "REBORN-RADIO-UI-01 — scan feedback correction - Innioasis Updater"
description: "REBORN-RADIO-UI-01 — scan feedback correction <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-validation-reborn-radio-ui-01.html"
---

# REBORN-RADIO-UI-01 — scan feedback correction - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# REBORN-RADIO-UI-01 — scan feedback correction

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# REBORN-RADIO-UI-01 — scan feedback correction > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

Built and validated; stop for owner manual installation. The running device still has source `6209f48`. This correction has not been installed or physically qualified. It builds on the owner-installed, working splash update and keeps its BOOTIMG, kernel, radio drivers/services, audio path, charging code and Y2DATA.

Built Reborn source: `a8ae8b6723311b677662759082c55ad226441669`. Y2Linux integration: `640ecb828af1ba48edcc6203701edb89f66eb0ac`. Rust 1.90.0, ARMv7 hard-float glibc, existing Buildroot GCC 13.3.0 toolchain. Cargo.lock/dependencies/native ABI and the safe Rust application architecture remain unchanged.

## Problem and corrected behavior

The previous [SSH inspection](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2F2026-09-18-radio-inspection.md) proved Wi-Fi scan and Bluetooth adapter/discovery APIs work, but it used separate diagnostic test hooks. The owner subsequently confirmed the actual UI Scan action provided no progress or devices. Source inspection found no scan lifecycle in the UI, scans sent while radios were off, Wi-Fi's disabled state treated as an error, and Bluetooth operation errors not displayed. Wi-Fi errors also overwrote a global notice visible on unrelated screens.

The corrected flow is:
  - Select Scan networks or Scan devices. That explicit action enables

the selected radio if necessary and remembers its On preference.
  - The selected row/footer immediately shows Starting Wi-Fi/Bluetooth…, then

Scanning…. Repeated activation cannot restart/cancel the current scan.
  - Wi-Fi waits for the actual supplicant `CTRL-EVENT-SCAN-RESULTS` event on a

separate attached control socket, then reads results. Commands and events cannot be confused. Startup and scan each have a 15-second deadline, with bounded native call timeouts. Results are strongest-first and deduplicated by SSID/security. Hidden SSIDs cannot be selected by this baseline UI.
  - Bluetooth powers through BlueZ, holds its own discovery session for 15 seconds,

publishes device updates during discovery, then stops that session. Paired and cached BlueZ devices remain in the list; no bonds are deleted.
  - Completion shows the result count. Empty Wi-Fi results say No networks found;

empty Bluetooth results ask for pairing mode. Failure is explicit and remains visible until the next operation. Early Bluetooth service startup can still return a visible retry error; it is no longer a silent action.

Wi-Fi Off is now an available, healthy radio state when rfkill and supplicant respond. Radio notices are owned by their respective screens. Held Select/Right activation no longer repeatedly toggles a radio or activates a row; Up/Down and volume repeats remain. No Wi-Fi network is selected or Bluetooth peer paired merely by pressing Scan. Existing platform saved-network behavior when enabling Wi-Fi remains in effect.

Workers keep bounded channels and their existing fixed threads. The main/UI thread remains responsive during activation/discovery. No runtime dependency, unsafe block, shell radio backend, frame animation loop or new network listener. Structured scan start/active/completion/failure logs share an operation correlation ID; Bluetooth operation errors now identify the method. Status JSON exposes `wifi.scan` and `bluetooth.scan`, each with a typed `state`, plus `found` at completion or `message` on failure.

## SSH validation uses the actual UI workers

New bounded, enumerated commands on the existing protected Unix socket:`rebornctl wifi scan --json rebornctl bluetooth scan --json rebornctl wifi on|off --json rebornctl bluetooth on|off --json rebornctl status --json`

An `accepted` response means the operation is queued; poll status to observe Starting → Scanning → Complete/Failed. The Scan commands call the same application effects/workers as the buttons. Radio commands reject `--follow`; they never execute a shell, accept arbitrary operations or expose a password. The existing diagnostic tests remain available; Wi-Fi's scan test now also waits for completion.

The host [radio UI qualification script](https://github.com/SchulzCode/Y2Reborn/blob/main/tools/qualification/reborn-radio-ui.py) uses pinned owner SSH, verifies the expected source before any operation, refuses to interrupt an active UI scan, retains JSON state samples and checks session continuity, active progress and completion. It restores Off for a radio it enabled from Off. It does not pair peers, choose networks, install software or access key bytes. Empty results are a successful completed scan, not proof of RF peer discovery.

## Validation
  - 64 Rust tests pass, including a fake supplicant with real Unix datagrams

and an isolated D-Bus/BlueZ adapter exercising the actual Bluetooth worker. Tests cover radio enable-before-scan, progress, result delivery, empty scans, timeout/failure, duplicate activation, power-off, retained errors, correlation IDs, UI footer isolation, selectable results and protocol rejection.
  - 20 host daemon checks and 4 host tooling tests pass; Clippy all workspace/

all targets passes with warnings denied.
  - The production cross/rootfs build passes with networking disabled. **8 installed

ARM application/shell checks** pass under QEMU, including decoder/DB/control regressions. These are not hardware scan tests.
  - Raw ext4 validation, pinned fallback hashes, root-only scatter preservation and

complete root content comparison pass. Exactly five file paths change: Reborn, rebornctl, root build ID, versions.json, and os-release. The installed splash helper, services, native libraries, firmware and all other paths match.

Receipts: `/home/luca/Dokumente/Code/Y2Linux/docs/build/evidence/reborn-radio-ui-01/`. Reborn binary: 1,879,004 bytes; rebornctl: 445,356 bytes. Y2ROOT remains 512 MiB; used ext4 space increases by 53,248 bytes (52 KiB).

## Exact package and manual installation

Package: `/home/luca/Dokumente/Code/Y2Linux/out/REBORN-RADIO-UI-01`.``````````

| File | SHA256 |
| --- | --- |
| Y2ROOT.img | 79b12172645c4755fdf3219fc6f99971d94de62c42f807a3613a43516d1f7df8 |
| fallback/Y2ROOT.img — installed splash root | d40e9337e3a1149d12fdd240a59918b0d2c48e4e6a9974ab5b470685250d900c |
| Required installed splash BOOTIMG, unchanged | 8671de2900fd05cc80a9eb7a3541d5bbdab7e5dd96c18f73f44ca1b13beb19a5 |

  - Verify on the host:
` cd /home/luca/Dokumente/Code/Y2Linux/out/REBORN-RADIO-UI-01 sha256sum -c SHA256SUMS`
  - Open the established SP Flash Tool v5.2032 workflow and load this package's

MT6582_reborn_root_only_scatter.txt. Select Download Only.
  - Check ANDROID only, pointing to this package's `Y2ROOT.img`. **BOOTIMG,

USRDATA and every other partition stay unchecked/NONE.** Do not select Format or Firmware Upgrade. This differs from the preceding two-image splash update.
  - Use the established owner shutdown/USB entry procedure: select Download,

connect the powered-off Y2, wait for success, disconnect and boot normally. Y2DATA, saved networks, bonds, settings and music remain in place.
  - If rollback is required, use `fallback/MT6582_reborn_root_only_scatter.txt`

with ANDROID only and its `Y2ROOT.img`. Keep the installed splash BOOTIMG.

## After owner installation

Start with SSH `status`, `health`, `metrics`, and `test baseline --json`, verifying source `a8ae8b6723311b677662759082c55ad226441669`. Then run:`cd /home/luca/Dokumente/Code/Y2Reborn python3 tools/qualification/reborn-radio-ui.py \ --known-hosts /home/luca/Dokumente/Code/Y2Linux/evidence-private/20260915-m5-entry/known_hosts \ --expected-build a8ae8b6723311b677662759082c55ad226441669`

Retain status/progress/results and any related subsystem logs before further changes. Only then request one visible scan confirmation and, if needed, a peer in pairing mode. Wi-Fi association, pairing/A2DP playback, suspend/charging and full Reborn Baseline 01 acceptance are not established by this fix. Do not start Reborn 02. Stop here for manual installation.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
