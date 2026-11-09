---
title: "Y2 + Reborn Bluetooth Platform 1.0 optimization - Innioasis Updater"
description: "Y2 + Reborn Bluetooth Platform 1.0 optimization 2026-10-04. Recommendation: MORE WORK REQUIRED. The control/observation fixes are implemented and software-validated. The"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-bluetooth-optimization.html"
---

# Y2 + Reborn Bluetooth Platform 1.0 optimization - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 + Reborn Bluetooth Platform 1.0 optimization

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 + Reborn Bluetooth Platform 1.0 optimization

2026-10-04. Recommendation: MORE_WORK_REQUIRED. The control/observation fixes are implemented and software-validated. The retained controller architecture is sound in the measured idle scope. This is not a headset/audio qualification: the owner explicitly reports no peer available, and another session's device lock prevented running the changed binaries on the Y2. No battery-energy gain, physical reconnect improvement, or audio/coexistence success is claimed.

## Identity, authority and receipts

Dedicated `codex/platform-v1-bluetooth` branches/worktrees start from Linux `b5aea93` and Reborn `b71b468`; neither main checkout is edited. No other branch is merged, no push/flash/image build occurs, and Git identity is preserved.

Locked SSH identifies Y2LINUX-BASELINE-02, installed Linux `8584ccd85f052f351fe51650b2348c83ca894ed4` / Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, kernel `6.18.0-y2linux-baseline-02`, root `2025.02.18-platform-v1.21`, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0. This updates the installed identity relative to older UART01 documentation, without qualifying Baseline02 cold boot or redoing CPU milestone tests. CONSYS identifies MT6582/E2: chip `6582`, HVR `8a01`, FVR `8a00`.

All live batches acquire `/tmp/y2-platform-v1-device.lock` through nonblocking `flock`, with 12–57s host deadlines. Busy attempts send no device command and return immediately; repeated busy results are not hardware failures. The completed radio batch uses existing `y2-radio ... *-runtime` controls and restores Bluetooth off. Discovery uses Reborn's existing bounded scan. Wi-Fi remains associated; bonds, saved radio preferences, calibration, firmware, raw storage, CPU policy, screen policy and protected partitions are not changed. Source fixes are NOT_INSTALLED / PHYSICAL_AFTER_NOT_RUN, not an overlaid image acceptance.

Private raw evidence and full test/build logs are retained in this Linux worktree's `out/bluetooth-optimization/`. Nearby device names/addresses and raw D-Bus observations are not copied into the public report. The [measurement summary](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-bluetooth-optimization.json) records numbers, identity, limits and hashes of the original private receipts. The [boundary admission](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23bluetooth-optimization-admission--2026-10-04&anchor=bluetooth-optimization-admission--2026-10-04) and [roadmap](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Fplatform-v1-roadmap.md%23bluetooth-optimization-boundary--2026-10-04&anchor=bluetooth-optimization-boundary--2026-10-04) keep #28/#31/#34 open. F102–F108/F145/F166/F229 retain their physical gates; this pass does not promote the 233-feature release inventory.

## Starting implementation and research

Reviewed current Buildroot configuration/service arguments, reconnect owner, radio/codec policy, native diagnostics, Reborn worker/PCM/lifetime code, CONSYS core/BTIF/HCI/STP/WMT paths, release inventory and latest physical reports. The requested codec architecture page lives in Y2Reborn, at `docs/architecture/bluetooth-codecs.md`; Linux has the platform Bluetooth contract. Older SBC-only source descriptions do not override the current private profile.

The pipeline remains FFmpeg decode → shared Reborn DSP → final sink conversion at the observed format/rate → BlueALSA encoder → BlueZ/HCI → headset. Buildroot pins BlueZ 5.87 and BlueALSA 5.0.0. The installed manager advertises SBC, AAC, aptX, aptX-HD and LDAC source endpoints; advertisement is not negotiated output. Requested SBC high/XQ/XQ+, LDAC quality/ABR and actual encoder observation remain separate. No Reborn encoder or competing reconnect loop exists or is added.

Primary references checked against the pinned source:
  - [BlueZ 5.87 Adapter API](https://raw.githubusercontent.com/bluez/bluez/5.87/doc/org.bluez.Adapter.rst): discovery is a per-client session; property signals and bounded Pairable/Discoverable policies are available.
  - [BlueZ 5.87 Device API](https://raw.githubusercontent.com/bluez/bluez/5.87/doc/org.bluez.Device.rst): connection, pairing, bonding and trust have separate meanings.
  - [GIO ObjectManager client](https://docs.gtk.org/gio/class.DBusObjectManagerClient.html): signal-maintained proxy/property cache and name-owner replacement handling support removing recurring enumeration.
  - [BlueALSA 5.0.0 PCM API](https://raw.githubusercontent.com/arkq/bluez-alsa/v5.0.0/doc/org.bluealsa.PCM1.7.rst): negotiated PCM properties and transport objects remain authoritative.
  - Pinned Rust `dbus` 0.9.9 `channel/ffichannel.rs` and `blocking.rs`: enabled descriptor watches plus nonblocking `process` drain buffered messages and flush asynchronous requests. No new dependency is needed.

Exact MT6582 vendor-derived register/lifecycle contracts are already retained in `kernel/platform/connectivity/{core,btif,hci,stp,wmt}.c` and the existing native connectivity tests. No unresolved operand in this pass justified additional register research or importing another MediaTek generation's definitions.

## Physical baseline

Two endpoint samples, approximately 20s apart, read `/proc/stat`, per-process and per-thread CPU/context/RSS counters, interrupt counts and cpuidle residency. CPU percentages mean one logical CPU, not percentage of four-core capacity. HZ is 100; a CPU tick is coarse over these short windows. Context switches are wake/activity proxies, not an electrical measurement or exact timer attribution. USB SSH is attached and Wi-Fi is associated idle. CPU0 is the only online core in both samples. The Python observer itself and existing background services contribute to total CPU/IRQ/context rates.

| Metric | Bluetooth off, 20.169s | Enabled, disconnected, 20.230s |
| --- | --- | --- |
| Reborn whole process CPU | 3.371% | 3.460% |
| Reborn Bluetooth thread CPU | 0.694% | 0.692% |
| Bluetooth thread voluntary context switches/s | 50.374 | 50.372 |
| Reconnect helper CPU | 0.248% | 0.395% |
| BlueZ CPU | 0.149% | 0.148% |
| BlueALSA CPU | 0.099% | 0.099% |
| D-Bus daemon CPU | 0.198% | 0.198% |
| Total interrupt events/s | 179.680 | 172.174 |
| Total context switches/s | 351.774 | 352.851 |
| CONSYS/BTIF IRQs 202–206 | delta 0 on each | delta 0 on each |
| CPU0 C1 residency | 89.35% | 89.03% |
| CPU0 C2/C3 entries | 0 / 0 | 0 / 0 |

The tiny IRQ difference is ordinary short-window variation, not an optimization. No C2/C3 entry was observed with this USB/Wi-Fi configuration; it cannot isolate Bluetooth as a deep-idle blocker. Natural secondary-core parking worked with both Bluetooth states. No display-state mutation or exact screen-state receipt was collected, so these are idle-process samples, not a controlled screen-off comparison. Historical UART01 separately proves guarded C1/C2/C3. Active CONSYS ownership is retained while Wi-Fi or Bluetooth needs it; forcing a clock gate from Bluetooth would violate the shared owner and the established idle guards.

| RSS, KiB | Off | Enabled disconnected |
| --- | --- | --- |
| BlueZ | 3,848 | 3,852 |
| BlueALSA | 5,656 | 5,664 |
| Reconnect owner | 4,348 | 4,412 |
| Reborn, all services | 23,696 | 23,720 |
| D-Bus daemon | 1,700 | 1,712 |

Radio enable command completes in 0.952s, disable in 0.589s. These include Python/shell/bluetoothctl control overhead, not just controller hardware latency. CONSYS was already active for Wi-Fi, so this is not cold firmware boot timing. Discovery command acceptance takes 0.0685s; `Discovering=true` is observed about one second later. Acceptance is not the exact discovery-start latency. Reborn requests a 15s discovery session. The terminal native snapshot is invalid JSON because a nearby peer exposes numeric ManufacturerData keys; therefore that raw snapshot does not certify exact discovery completion timing. Bounded scan completion and session ownership are covered by the existing extended fake-bus test. Pairable and Discoverable are false in the valid active-discovery snapshot.

After radio disable: CONSYS `functions=0x8` (Wi-Fi only), `error=0`, `transport_errors=0`, `recoveries=0`, same boot and taint 0. This is a bounded controller/idle result, not a firmware-fault or reset-recovery exercise.

## Shortcomings and implemented fixes
  - Idle polling and repeated enumeration. Reborn's 20ms D-Bus wait creates

about 50 idle wakes/s even with the radio off, alongside full 2s BlueZ/BlueALSA snapshots. The reconnect helper also performs synchronous GetManagedObjects every 2s and writes runtime records every pass. It has no reason to enumerate a quiet, disabled radio continuously.

 The helper now uses GIO ObjectManager's signal-maintained cache, relevant adapter/device changes, daemon-owner changes and intent-file notifications. Retries and the 30s stable-link check use one-shot deadlines. A 5s heartbeat retains the existing <10s status-freshness contract without querying D-Bus. Intent is reread under the common operation lock before each request.

 Reborn now waits on the D-Bus descriptor, a notified eight-command queue, or the next actual operation/scan/pairing deadline. Relevant typed signals trigger coalesced observations; a 30s reconciliation backstop remains. Encoder statistics/RSSI do not trigger full enumeration. Pending publication is retried if the two-slot status queue is full. Buffered D-Bus messages and late/coalesced command notifications are drained without spinning. Per-epoch codec capability caching is preserved.
  - Unnecessary reconnect delay after successful explicit intent. The old

helper retains the 30s intent-validity deadline as a reconnect admission time. Thus a known disconnected candidate can wait roughly 30–32s after successful power-on/connect, before any BlueZ request. A committed successful intent now rearms immediately after its shared lease is released. Pending/failed/expired or uncertain intents still inhibit; they do not gain a retry loophole.
  - Bond correctness and owner recovery. Automatic candidates now require

Bonded as well as Paired/Trusted, and cannot displace any resolved connected audio peer. Requests target the unique BlueZ owner. Owner disappearance clears cached connection observations while preserving consumed budget; same-boot restart preserves pending uncertainty. Reborn clears stale PCM/devices on a failed snapshot and recreates its pairing agent when BlueZ returns, including reacquisition of the same unique connection. Read-only Refresh no longer erases a previous operation error.
  - Discovery breaks native JSON diagnostics. Observed

`ManufacturerData={uint16:variant}` becomes `{null:[...]}` in the old serializer, invalidating the entire observation. Numeric D-Bus keys now become JSON strings; unsigned/signed 64-bit counters are retained and nonfinite doubles become null. Platform status exposes independent Bonded, Pairable and Discoverable fields; fixed diagnostic-field allowlists preserve those names.

A bounded read-only collector, `tools/development/measure-bluetooth-idle.py`, makes CPU/IRQ/idle/RSS measurements repeatable, verifies same-boot intervals and returns 75 without device commands when the shared lock is busy. It does not create radio/screen/CPU activity.

## Before/after evidence and limits

| Item | Before | After | Evidence scope |
| --- | --- | --- | --- |
| Reborn idle periodic wait | 20ms, ~50.37 voluntary switches/s on Y2 | Descriptor/command/deadline wait; no 20ms tick | Source + real private-bus worker test |
| Reborn routine full snapshots | ~every 2s | Relevant changes + 30s backstop | Fake bus counts no recurring snapshots in a 2.2s idle window |
| Quiet worker context switches | Physical ~50.37/s | At most 2 in 2.2s host idle test | Different environments; not a matched physical speedup |
| Helper recurring GetManagedObjects | every 2s | None after initial cache/replacement acquisition | Real GIO fake-bus test retains exactly one initial snapshot while quiet |
| Helper freshness timer | 2s enumeration/records | 5s records, no bus query | Source; same freshness contract |
| Committed-intent request admission | Derived ~30–32s with candidate available | 111.928ms in Cortex-A7 QEMU fake bus; <500ms guarded test | Request dispatch, not headset connection completion |
| Explicit Reborn command response | Worker checks queue every 20ms | Immediate descriptor notification; power-off observation <500ms test bound | Private bus; no physical UX timing claim |
| Physical CPU/RSS/IRQ after changed binaries | — | NOT_RUN_DEVICE_LOCK_BUSY | No matched before/after battery or CPU claim |
| Pair/connect/reconnect/A2DP PCM/audible startup | Peer unavailable | Peer unavailable | NOT_MEASURED |

The QEMU dispatch number includes event debounce and fake-service processing. It must not be labelled connection or A2DP-ready latency. Actual connected idle, SBC CPU, active screen-off playback, audio startup, PCM underruns and reconnect attempts under peer disappearance remain unmeasured for this source pair.

## Transport, recovery and optimizations rejected

Keep the existing PCM settings: 512-frame period, 4096-frame buffer and two-period start threshold, negotiated using ALSA `*_near` and verified format/rate. At 44.1/48 kHz the requested period is 11.61/10.67ms, buffer 92.88/85.33ms and local start threshold 23.22/21.33ms. These are configuration durations, **not audible Bluetooth latency**, and BlueALSA/codec/peer buffering is additional. Partial writes retain original PCM and advance by actual frames; the engine bounds each write to 512 frames, recovery waits are bounded, and no-progress failure is contained. There is no justified evidence for changing periods, removing gain work/copies, raising real-time priority or minimizing buffers on Cortex-A7.

The exact CONSYS runtime-PM/clock owner, 1s autosuspend, interrupt-driven BTIF DMA, stock-derived HCI sleep/configuration, bounded DMA polling, firmware lifecycle, isolated one-retry boot recovery and latched fault handling are retained. Idle BTIF IRQ deltas are zero; none warrants a new gate, PIO switch or reset policy. No later MediaTek register definitions are transplanted. Repeated cold firmware boot and injected controller faults are not tested here.

Do not add perpetual scanning, Pairable/Discoverable enablement, background bluetoothctl, availability probes or an unlimited exponential reconnect loop. The existing two 10s automatic calls within a 25s attempt-start episode remain; 30s stable connectivity rearms a later link-loss episode. A local timeout means completion is unknown and inhibits further calls, even across helper restart. A peer returning after exhaustion still needs explicit user action; without physical peer evidence, replacing that conservative policy is unjustified.

Do not add encoders to Reborn, repeatedly probe unchanged codec capabilities, change SBC/XQ/AAC/aptX/aptX-HD/LDAC quality, or override bitrate because Wi-Fi is busy. The actual negotiated format/codec and transport epoch remain authoritative for every codec. No optional codec's CPU, quality or battery effect is inferred.

## Coexistence, battery and remaining acceptance gates

With Wi-Fi associated idle, Bluetooth enable/discovery/disable completes without CONSYS transport errors or controller recovery. This proves only that narrow control workload. There is no Bluetooth audio traffic, so Wi-Fi scan/transfer dropouts, retransmission symptoms, audio CPU spikes and reconnect behavior are NOT_TESTED. Wi-Fi off/controller-only, connected idle and controlled screen-off comparisons were not run once the device lock was occupied. Wi-Fi is not redesigned.

Removing unnecessary timer and enumeration work should reduce CPU activity; the wake-source removal is source/test-backed. Electrical current, charge consumption, matched on-device after-state, C2/C3 gain and battery runtime are unavailable. There is no defensible mA, mWh, percentage battery saving or extra-hours estimate.

To call the Bluetooth subsystem Platform 1.0, the remaining smallest boundary is running these binaries under the shared lock, followed by a real bonded headset: fresh pair/trust/forget, fast known-peer reconnect and long-absence behavior, BlueZ/BlueALSA/peer-loss/PCM recovery, actual A2DP and audible startup, SBC CPU/RSS/ XRUNs, screen-off idle/playback, and Wi-Fi off/associated/scan/transfer coexistence. Then retain a representative endurance run. Optional codec feature completion, public codec redistribution, full system suspend and general release qualification remain their separate projects. The measured idle controller paths do not need kernel redesign; pending physical evidence prevents a PLATFORM_V1_READY label.

## Validation and changed files
  - Linux Bluetooth observation/reconnect/serializer: 12 tests PASS.
  - Connectivity: 15 cases, 14 PASS / 1 SKIP, unchanged emitted-DT artifact opt-in;

the initial isolated-worktree cache prerequisite failure was resolved with the existing pinned source cache, then the suite passed.
  - Radio/codec policy: 7 PASS; platform contract: 11 PASS; targeted telemetry

regressions also pass. No Wi-Fi implementation is changed.
  - Reborn: `cargo fmt --all -- --check`,

`cargo clippy --workspace --all-targets --locked -- -D warnings`, and `cargo test --workspace --locked`: PASS, 238 tests.
  - ARM helper/observer and Reborn release builds pass with the retained Baseline02

ARM toolchain/sysroot, isolated output. Native event/JSON contracts pass under Cortex-A7 QEMU; neither test accesses HCI or a real Bluetooth peer.
  - Collector baseline replay, changed-boot rejection and lock-busy refusal pass;

`git diff --check` passes. No root image, kernel build or flash is required.

Linux changes: `tools/connectivity/{reconnect,bt-observe}.c`, `tools/platform/y2_platform/{bluetooth,diagnostic_fields}.py`, `tools/development/measure-bluetooth-idle.py`, `tests/test_platform_bluetooth.py`, `tests/native/{bt-reconnect-events,bt-observe-json}.c`, `docs/architecture/platform-bluetooth-v1.md`, the two planning boundary pages, this report and its measurement JSON. Reborn changes: `crates/reborn-platform/src/{bluetooth,native}.rs` and `docs/architecture/bluetooth-codecs.md`. Candidate Reborn commit: `de092094c27ad4ebba3cc0ba7003f29944de53ac`. Linux implementation/receipt commit is the local `codex/platform-v1-bluetooth` branch tip at handoff. The measurement JSON also pins the changed compiled sources and ARM binaries. Both commits remain local; the final handoff records their exact IDs.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
