---
title: "Y2Linux 1.0 Beta 2 (Baseline 51) - Innioasis Updater"
description: "Y2Linux 1.0 Beta 2 Baseline 51 Status: PUBLISHED as GitHub release baseline-51 2026-10-15. Second public beta: release 1.0.0-beta.2 , Reborn 1.0.0-beta.2 , kernel 6.18.56"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-linux-1.0-beta-2.html"
---

# Y2Linux 1.0 Beta 2 (Baseline 51) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2Linux 1.0 Beta 2 (Baseline 51)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2Linux 1.0 Beta 2 (Baseline 51)

Status: PUBLISHED as GitHub release `baseline-51` (2026-10-15). Second public beta: release `1.0.0-beta.2`, Reborn `1.0.0-beta.2`, kernel `6.18.56-y2linux-1.0.0-beta.2`, update sequence 5100, Linux `fc1f5ea`, Reborn `009cd32`, git tag `baseline-51` in both repositories. Built with `--public`. Container suite 731 OK, all seal checks PASS (public distribution gate, no radio firmware). Milestone audit: BETA-2 in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).````````

| Image | SHA-256 |
| --- | --- |
| BOOTIMG | bb600504ac4d2fccfc3f6ca7a18c0ae79e34863a733aa2f2c0d9a860baef230c |
| Y2ROOT | 8e0917adc2a8a3d257d2e259dd0584e603a46fda3c71cc1f3dc17a36bd134667 |
| RECOVERY | 08009b9d7a0a91c40d19b7ffca63c322fb23f3eb9143556f10875272ac4fad61 |
| Y2DATA (no SSH key) | 77f38ef58ef35f9fb4e6d4e7f3587ee34e789132c195063a5c6a64aae8114796 |

## Why

A Bluetooth/Wi-Fi review of Beta 1 (2026-10-15) against archive `20261016/155` and the live player (AirPods Pro connected, AAC negotiated at 44.1 kHz) found the faults below; the owner asked to fix all of them and to choose the audio output automatically.

## Since Beta 1````````````````````````````````````

| Change | Evidence | Fix |
| --- | --- | --- |
| BTIF receive lost bytes | Every BTIF timeout on record (4 of 4, incl. 155's morning wake) showed the reply already in the RX ring, unread: RX flag=0 valid=7 / valid=2. The handler read the write pointer, drained, then cleared the (edge-like, write-one-to-clear) RX status, dropping the interrupt of bytes that landed in between. Cost: a 4 s WMT timeout (opcode 07/08 −110) and a full controller restart. | btif.c: acknowledge first, then drain until the write pointer stops moving. New host test reproduces the race; it fails on Beta 1's handler. |
| Reconnect gave up for good | With the AirPods away, BlueZ answered "Host is down" ~18–19 s after the radio came up (three wakes in 155); y2-bt-reconnect stopped waiting at 10 s, could not tell what happened and inhibited every later reconnect (completion_unknown_user_retry_required, also on the 26 nights). | reconnect.c waits 45 s for BlueZ's answer; an absent peer is an ordinary failed attempt. The HCI driver programs the page timeout to 0x2000 slots (5.12 s) after init (Linux stores BlueZ's PageTimeout but never sends it) and logs the value it replaced. |
| Wi-Fi start slowed by the failing page | 155 morning wake: 22.4 s from wlan0 to DHCP while the page ran; 7.5 s on 2026-10-15 with the AirPods present. Shared 2.4 GHz radio. | Shorter page timeout above; to be measured on the next wake. |
| DNS re-check every 30 s forever | Live: dns.json rewritten at 4077 → 4109 → 4137 s; each probe starts python3 (260 ms CPU measured) and a radio exchange. | Confirmed lease re-checked every 300 s, failures every 30 s; Online stays fresh for 420 s. |
| Sleep counted as a Wi-Fi drop | 2026-10-15: 5 real_disconnects, all sleep rfkill blocks; no real drop. | A disconnect while Wi-Fi is soft-blocked counts as radio_off_disconnects. |
| Bluetooth class | Adapter class 0x080000 (Miscellaneous). | Class=0x00041C (Audio/Video, Portable Audio). |
| Automatic audio output (Reborn) | Owner had to switch to the headphones by hand. | Bluetooth headphones win over the jack as soon as their audio is ready (playback continues there); jack again when they disconnect (pauses). Once per connection, so a manual jack choice sticks. Reborn starts on the jack. No jack detection exists on this board yet: "jack" means "no Bluetooth headphones". |
| Wi-Fi passwords with or " (Reborn) | wpa_supplicant reads "…" literally; Reborn escaped both characters, so such passwords were stored wrong and failed as "wrong password". | Passwords sent as typed, network names as hex. |
| Identity |  | Y2Linux and Reborn 1.0.0-beta.2. |

Not changed, on purpose: Wi-Fi power save stays off (owner decision; association blocks deep idle either way); the Wi-Fi status loop keeps its `wpa_cli`/`ip` probes (0.2–0.7 % CPU measured; they feed the Online/update decision); BlueZ's `uinput` message stays (headphone buttons reach Reborn through its media player; a second, uinput key path could deliver them twice).

## Release contents
  - `Y2Linux-1.0.0-beta.2-first-install.zip`: BOOTIMG, RECOVERY (Y2 recovery image), Y2ROOT, Y2DATA, the scatter

files for SP Flash Tool and checksums. No MediaTek firmware, no SSH key.
  - The signed over-the-air update (`manifest.json`, `manifest.sig`, three payloads; key `platform-v1-release-20261015`).
  - Corresponding sources: Buildroot legal-info and the Linux 6.18.56 archive; Y2Linux and Y2Reborn at `baseline-51`.

## Device results

Published without a device test first (owner: "publish directly, i want to update only over ota in the future"). Owed after the owner's over-the-air install: version/health/firmware check; `page timeout … slots` line in the kernel log; radio start without BTIF timeouts over many wakes; AirPods away at wake → state `Exhausted`/`Waiting`, not `Inhibited`, and they connect when taken out; output switches to the AirPods on connect; Wi-Fi time to Online after a wake.

## Known gaps

Battery in sleep ≈9.4 mA (Beta 1 night, archive 155) vs stock ≈1.3 mA; rare slow display start after a restart; USB after deep-sleep wake not confirmed over many wakes; AAC with AirPods negotiated but not listened to; no headphone-jack detection; full install from stock run on one player only; maintenance self-wake race (`wake_event_in_progress`) open.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
