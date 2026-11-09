---
title: "Reborn radio inspection after owner splash installation - Innioasis Updater"
description: "Reborn radio inspection after owner splash installation <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-validation-2026-09-18-radio-inspection.html"
---

# Reborn radio inspection after owner splash installation - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn radio inspection after owner splash installation

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn radio inspection after owner splash installation > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

The owner reports that the flashed splash update works. Existing pinned owner SSH confirms `Y2LINUX-REBORN-SPLASH-01`, Reborn source `6209f48402a00a077759df042916f0ae2c89783a`, and the Mali400 hardware renderer. The inspection used Reborn's existing JSON diagnostic commands. No application, firmware, boot image, credentials or persistent radio preference was changed.

## Findings

Both radios were off at entry: `/data/network/enabled=0`, Wi-Fi rfkill soft block set, and BlueZ `Powered=false`. The connectivity owner was activated/calibrated, with no transport errors or recoveries. Supplicant, BlueZ and BlueALSA were alive.

Reborn's event ring records Wi-Fi power requests on → off → on → off, followed by two scan errors while the interface was off. This proves the requested sequence, not whether repeated user presses or key repeat caused it. Bluetooth recorded five `org.bluez.Error.NotReady` responses while its adapter was off; the existing Bluetooth error records omit the method, so they cannot identify the exact failed UI operation on their own.

There are two confirmed application status/presentation defects:
  - `crates/reborn-platform/src/wifi.rs::status` treats the normal absence of a

per-interface supplicant socket when Wi-Fi is disabled as `unavailable` and sets an error. It does not distinguish Off, Starting and a missing service.
  - `app/reborn/src/main.rs` copies every Wi-Fi status error into the global

`Ui.notice`, regardless of the current screen. Successful updates do not clear that notice. A Wi-Fi error can therefore remain visible on Bluetooth and other screens. The Bluetooth event handler does not display its own `Status.error`.

The radio tests below succeed through the running Reborn process using the same rfkill/supplicant and BlueZ D-Bus helpers as the application. They do not prove network association, Bluetooth pairing or Bluetooth audio playback.````````

| SSH command | Physical result |
| --- | --- |
| rebornctl test wifi-scan --json | Pass; 28 networks, interface available; 5.129 s including SSH |
| rebornctl test bluetooth --json | Pass; adapter and BlueALSA available, no connected peer |
| rebornctl test bluetooth-scan --seconds 10 --json | Pass; powered adapter and completed discovery, 0 discoverable peers; 11.261 s including SSH |
| rebornctl test baseline --json | Pass; 10 checks including hardware graphics readback, six decoder formats/artwork, DB, storage and service availability; SD absent warning |

Final state matches entry: both radio preferences remain off, Wi-Fi soft block restored, BlueZ powered off, same Reborn session and boot ID. No increase in Wi-Fi/Bluetooth errors, audio XRUNs, playback errors or graphics context losses during these tests. Kernel connectivity status still reports `error=0`, `transport_errors=0`, `recoveries=0`.

For this deployed build, select Turn Wi-Fi on or Turn Bluetooth on once, wait several seconds for activation, then select Scan. After activation the first row changes to Turn … off; selecting it again disables the radio. Bluetooth discovery additionally needs a nearby peer in pairing/discoverable mode. A stale Wi-Fi footer is not evidence that Bluetooth is unavailable.

## Evidence and limits

[Machine-readable summary](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/radio-inspection-20260918.json). Full bounded local captures, including the before/after snapshots, subsystem logs and kernel radio excerpts, are retained under `out/radio-inspection-20260918T115744Z/`; they are not committed because future captures may contain local network or peer identifiers. No passwords, bond keys, SSH private keys or raw calibration records were read.

The splash reports console hidden at boot 698 ms, visible at 828 ms, READY release at 49,448 ms and the first Reborn frame presented at 49,456 ms. This agrees with the owner's successful visible boot report. It is not an offline-charging, suspend/resume or complete Reborn Baseline 01 acceptance result. This inspection does not install a UI status fix or leave the radios enabled.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
