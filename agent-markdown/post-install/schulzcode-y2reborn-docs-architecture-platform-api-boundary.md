---
title: "Reborn ↔ Y2Linux platform API boundary - Innioasis Updater"
description: "Reborn ↔ Y2Linux platform API boundary <!-- knowledge-base-scope: source-contract -- Source-contract scope. Ownership in the Reborn 0.2.0 source. The platform side is Pla"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-architecture-platform-api-boundary.html"
---

# Reborn ↔ Y2Linux platform API boundary - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn ↔ Y2Linux platform API boundary

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn ↔ Y2Linux platform API boundary > **Source-contract scope.** Ownership in the Reborn 0.2.0 source. The > platform side is [Platform API v1](https://github.com/SchulzCode/Y2Linux/blob/main/docs/architecture/platform-api-v1.md). `reborn-ui (pages, diagnostics, screens) ← typed models only, no I/O ↑ AppModel / typed views app/reborn (Runtime) ← presents state, executes Effects ↑ typed state, typed actions reborn-platform (client, power, wifi, bluetooth, storage, input, workload, contract) ↑ y2-platform CLI · /run/y2 records · power socket · D-Bus · evdev · sysfs Y2Linux platform services → kernel → hardware`

## Rules
  - Y2-specific access lives in `reborn-platform`. Y2Linux runtime

records (`/run/y2`, `/etc/y2linux`, `/data/system`), the `y2-platform` and `y2-media` tools, Y2 device names, backlight and power-supply sysfs, the workload device and the power socket are only touched there.
  - The UI receives typed models.`reborn-core::platform` defines

`BatteryState`, `ChargingState`, `LowBattery`, `SleepState`/`SleepPhase`/ `SleepProblem`/`WakeReason`, `BluetoothQuality`, `StorageState`, `VolumeSpace`, `SdCard`, `UsbTransfer`, `UpdateState`/`UpdatePhase`/ `UpdateProblem`, `HealthLevel`, `WifiProblem`, `PlatformInfo`, `PlatformSnapshot`, `DiagnosticSection`/`Fact`, `ShutdownIntent` and `OperationResult`. The UI also receives `WifiView`, `BluetoothView` and their device/network views. `reborn-ui` and `reborn-core` production code use no `std::fs`, `std::process`, sockets or `serde_json::Value`.
  - One owner per state. Battery, charging and low battery: Y2Linux

(`/run/y2/power.json` via `power::battery`). Storage, USB, update and health: Y2Linux status (via `client::snapshot`). Wi-Fi readiness: Y2Linux (`readiness` record) via `wifi::problem` and the app projection. Active Bluetooth codec: the BlueALSA transport observation. Reborn presents these; it does not re-derive them.
  - One poller.`client::Client` is a single worker. The application

requests a refresh when a platform-backed screen becomes visible and then at most every 15 s (4 s on PC Transfer and Sleep), never with the display off. Operations trigger one refresh afterwards. Battery is read every 2 s from the platform's power record (file reads, no process).
  - Application-owned standard APIs stay in Reborn. FFmpeg decode and

DSP (`reborn-media`), the ALSA sink (`reborn-audio`), SQLite library (`reborn-library`), DRM/GBM/EGL rendering (`reborn-graphics`), the control socket and Reborn's own `/data/reborn` state.
  - Guarded.`app/reborn/tests/architecture_guard.rs` fails on any new

platform literal (`/sys/`, `/proc/`, `/dev/`, `/run/y2`, `/etc/y2linux`, `/usr/sbin/y2`, `/usr/bin/y2`, `/data/system`, `/run/wpa_supplicant`) or `Command::new` outside `reborn-platform` and an explicit, justified allowlist, and on I/O in `reborn-ui`/`reborn-core`.

## Typed actions``````````````````````````````````````````````

| Action | API |
| --- | --- |
| Wi-Fi on/off, scan, connect, saved connect, forget, disconnect | wifi::Command::{Power, Scan, Connect, Saved, Forget, Disconnect} |
| Bluetooth on/off, scan, pair, connect, disconnect, forget, pairing confirm | bluetooth::Command::{Power, Scan, Pair, Connect, Disconnect, Forget, Confirm} |
| Codec preference | bluetooth::Command::Codec; choices from bluetooth::Status::codec_choices |
| Shutdown / restart request and acknowledgement | power::request_shutdown, power::shutdown_intent, power::acknowledge_shutdown |
| Backlight off/on, brightness | power::blank, power::brightness_available, power::set_brightness |
| Update check, stage, apply, cancel, rollback | PlatformTask::Update* via client::Client |
| Deliberate sleep | PlatformTask::SleepRequest → y2-platform sleep request; typed power.sleep observation |
| SBC/LDAC quality, LDAC ABR | PlatformTask::{SbcQuality, LdacQuality, LdacAbr} → codec-settings; saved/effective state kept separate |
| Redacted report export | PlatformTask::DiagnosticsExport → export-diagnostics; separate from private Export |
| Export, health, network check, benchmarks | PlatformTask::{Export, Health, NetworkCheck, StorageBenchmark, LibraryBenchmark} |
| Bluetooth PCM lease (codec-switch exclusion) | bluetooth::playback_pcm_lease |
| Application readiness, maintenance gate, splash evidence | contract::{application_ready, maintenance_pending, splash_evidence} |

## Migration table````````````````````````````````````````````````````````````````````````````````````````````

| Old direct access | Old owner | New API | Migrated | Justified exception |
| --- | --- | --- | --- | --- |
| y2-platform status/capabilities/health/... JSON in UI (platform.rs, 1,014 lines) | reborn-ui | client::snapshot → typed PlatformSnapshot + DiagnosticSection | Yes | — |
| Two dashboard::Dashboard workers (observer + operations) | app | One client::Client | Yes | — |
| power::status() JSON → power_view() in app | app | power::battery → BatteryState | Yes | — |
| /run/y2/shutdown.json id string | reborn-platform | power::shutdown_intent → ShutdownIntent (restart, low battery) | Yes | — |
| /data/system/platform/maintenance-pending | app main | contract::maintenance_pending | Yes | — |
| /run/reborn-splash/events.jsonl | app main | contract::splash_evidence | Yes | — |
| /run/wpa_supplicant/global probe | app diagnostics | wifi::service_available | Yes | — |
| /etc/y2linux/platform-contract, /run/y2/bt-pcm.lock, bt-codec-uncertain.json | reborn-audio | bluetooth::playback_pcm_lease | Yes | — |
| Wi-Fi readiness strings rendered as labels | app | wifi::problem → WifiProblem; wifi_view | Yes | — |
| BlueZ/BlueALSA status serialized into m.platform.bluetooth | app | bluetooth_view, Status::diagnostic_facts, Status::codec_choices | Yes | — |
| Audio pipeline JSON in m.platform.audio | app | audio_facts → Fact list (Diagnostics only) | Yes | Application-owned observation |
| evdev /dev/input, /sys/class/input | reborn-platform | unchanged, plus evdev_monotonic_clock | Already behind platform | — |
| /proc and /sys in diagnostic snapshots | reborn-observability | unchanged | — | Standard Linux self/kernel identity for bundles |
| /proc/self/mountinfo, /proc/self/fd | reborn-library | unchanged | — | Standard Linux; scanner source identity |
| /dev/kmsg, /proc/self/status | app main | unchanged | — | Standard Linux diagnostic bundle content |
| /dev/dri/card*, /run/reborn-splash/control.sock | reborn-graphics (C) | unchanged | — | Reborn owns the display; the splash handoff is the agreed protocol |
| /usr/lib/reborn/libreborn_media.so | reborn-media | unchanged | — | Application-owned file |

Before: 11 Y2-specific accesses outside the platform crate plus the UI's raw-JSON projection. After: 0 outside the platform crate; 9 standard-Linux or application-owned exceptions, each listed in the guard with its reason.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
