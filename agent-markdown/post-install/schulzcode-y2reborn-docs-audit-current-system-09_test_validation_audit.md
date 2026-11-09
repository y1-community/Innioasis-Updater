---
title: "Test and validation quality - Innioasis Updater"
description: "Test and validation quality <!-- knowledge-base-scope: historical-audit/review -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-audit-current-system-09_test_validation_audit.html"
---

# Test and validation quality - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Test and validation quality

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Test and validation quality > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

## What was executed in this audit

No kernel/Buildroot/Cargo build, physical command, flash or qualification run was performed. Existing host binaries were executed; they are cached artifacts, not a fresh build of both audited HEADs. [Exact commands/results](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F15_EXECUTED_CHECKS.md) record that limitation.
  - Cached Rust suites: 83 tests passed across playback, media, core, library, UI, observability, control, audio and platform. Playback's six tests also passed under default parallel execution after the serial run.
  - Current `tests/tooling.py`: four tests passed.
  - `tests/host-daemon.py` against cached host executables: 20 black-box checks passed, including six-track scanning/reuse/removal, control bounds, diagnostics sanitization and restart persistence.
  - Retained Buildroot generated FFmpeg configuration/ELF boundary: validator passed.
  - Additional host-native probes: repeated decoder closure still accompanied accumulating RSS; 500-ms seek returned extra audio frames despite the target position label. These exposed gaps rather than certifying the pipeline.

Test totals are receipts, not the basis of the assessment. Most important is what these tests leave uncontrolled.

## Evidence quality by tier

| Tier | Meaningful strengths | Limits |
| --- | --- | --- |
| Core state transitions | Stale generations, queue validation, restore normalization | Duplicate queue IDs, repeat with automatic chaining and live edits are not comprehensively covered. |
| UI/action tests | Focus invariant, modal/destructive confirmation, wheel/long semantics, password hiding | Effects often tested in isolation, not executed against runtime/worker queue or real ALSA. |
| Media fixtures | Real FFmpeg decode across codecs, artwork pixels, conversion, cancellation, malformed/truncated files | A decode producing frames is weaker than precision/delay/seek correctness. APE/WavPack fixtures are silent specimens. |
| Playback fixtures | Real media membrane plus injected sink; same-rate FLAC ramp boundary and exact count | Fake sink lacks exclusive-open, maximum-block, clock/drain/XRUN and BlueALSA behavior; long crossfades are not represented. |
| Library | Source online/offline, ID reuse, incremental scan/error cases, SQLite validation | No scan-wide commit error causality, realistic ENOSPC, power-cut or corrupt-DB recovery test. |
| Radio adapters | Mock Unix supplicant protocol and private D-Bus services exercise state machines and errors | No RF/controller, WPA handshake, DHCP/DNS, remote SBC or actual BlueZ pairing compatibility. |
| Observability/control | Storm/drop/rotation bounds, malformed protocol rejection, redaction, private socket | Sanitizer cases do not prove all free-form logs anonymous; health metrics can be semantically wrong. |
| ARM/QEMU | Native ABI/library resolution, headless decoder/DB/control integration | No real DRM, ALSA, DMA, PMIC, storage hotplug or radio hardware. |
| Rootfs/package validation | Filesystem labels/UUIDs, allowed payloads, hashes, SSH material policy, ELF dependencies | Can enforce stale semantics (application “unimplemented”); cannot prove manual install choice or device runtime. |
| Kernel host harnesses | Production helper/function extraction; failure-injection, register masks/order, bounded recovery | Mock MMIO/clocks/IRQs omit electrical behavior and many real concurrency/timing interactions. |
| Hardware observations | Actual GPU rendering/runtime PM, quiet ALSA tones, evdev captures, Wi-Fi scans, power observations | Exact-build, narrow scenario evidence. Several tests explicitly failed or remain pending. |

Examples of worthwhile tests to keep: `tests/test_charger.py` injects individual I/O failures and checks protection ordering; `tests/test_wifi.py` extracts the production TX-power command completion path rather than reimplementing only a toy expected result. These are substantially better than string-count-only tests. They still cannot prove battery safety or real firmware DMA ordering.

## Playback fixtures: actual verdict

All six available cached playback tests passed serially and in parallel. The same-rate gapless test is meaningful: two known 4096-frame ramps, total 8192 output frames, positive local slope and matching boundary step. Do not discard it. It is not a lossy encoder-delay test, a real output-clock test or a cross-rate test.

Crossfade testing uses a 50-ms overlap and an unbounded fake sink. It cannot catch the real sink's 524,288-byte maximum, which normal UI durations exceed. Sink-open tests do not model concurrent exclusive hardware ownership. Queue fixture tests mostly load a fixed queue; they do not invoke Runtime effects during a transition. Current seek tests assert position labels, precisely the surface that the new probe showed can be wrong.

The current corruption loop permits open failure or a bounded amount of successful decoding; this is useful crash/hang smoke coverage, not proof of correct recovery/error reporting for every truncation. Generated codec fixtures use the same FFmpeg ecosystem as the implementation; use independently characterized reference samples and expected sample counts/LSBs for precision claims. Silent external APE/WavPack samples prove decoder/container handling, not musical fidelity.

No specific historical failing playback log was identified that permits a responsible root-cause conclusion. The correct answer is not reproduced with available cached binaries; historical cause UNKNOWN. Rebuild current HEAD under a controlled environment in a separately authorized implementation/validation turn, preserve exact failing command/library version/fixture hashes, then investigate any recurrence. It would be wrong to label the old report “stale UI noise.”

## Reports that must not be promoted to current proof: F14/F27

The tracked [ARM evidence](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/arm-tests.json) records build `77e6732...`, `baseline.01`, and FFmpeg 6.1.5, despite the current QEMU script checking 9.0.1. This is a historical receipt, not current FFmpeg9 validation. [Dependency metadata](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/architecture/dependencies.json) still names `font8x8` although current Cargo/UI uses checked-in DejaVu atlases. Baseline host/rootfs/package reports must be tied to their original source, not treated as evergreen badges.

[UI-POLISH-02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FREBORN-UI-POLISH-02.md) clearly says host-validated candidate with manual installation/physical viewing pending. The title's “physical-device legibility” wording is not proof of viewing. The [radio qualification script](https://github.com/SchulzCode/Y2Reborn/blob/main/tools/qualification/reborn-radio-ui.py) intentionally reports `physical_acceptance: false` and permits a completed zero-peer scan; that pass means state progression, not discovery of a working headset.

The baseline classifier treats absent SD, saved Wi-Fi and Bluetooth peer as warnings, allowing a useful core baseline pass. Do not interpret that pass as storage hotplug/network/BT audio qualification. This is a report-consumption issue as well as a test-design issue.

## Physical evidence ledger

| Claim | Evidence | Responsible classification |
| --- | --- | --- |
| Linux boots/rescue/root-data contract | Production scripts plus retained storage/recovery evidence | Strong owner baseline; current public installation UNKNOWN |
| Real Mali acceleration | GPU01 rendering/runtime captures; older Reborn inspection reports Mali400 | VERIFIED historical hardware path; latest UI experience not qualified |
| Clean wired sound | GPU01 audio/owner observations, S16/44100 aplay tones | VERIFIED narrow heard baseline, not Reborn end-to-end/high-resolution |
| Input | Captured device names/events plus application mapping tests | IMPLEMENTED with physical mapping evidence; strict simultaneous input/GPU coverage explicitly incomplete |
| Wi-Fi | CONNECTIVITY-10 and later scans through Reborn/GPU harness | VERIFIED scanning/power; association/IP/DNS/data UNKNOWN |
| Bluetooth | Powered HCI adapter/BlueZ, discovery with no peer | IMPLEMENTED adapter; actual pairing/SBC/reconnect UNKNOWN |
| Useful charging | 70-mA baseline shows declining voltage; later owner POWER-03 acceptance | Mixed historical evidence; current profile/pack safety UNKNOWN |
| Deep suspend | GPU01 failed attempt and CPU3 status-bit mismatch; later source correction | PARTIAL; same-boot current resume UNKNOWN |
| Long-session memory | Host repeated-decode probe grows; source allocation leak | WEAK; target endurance not measured |

## High-value missing tests—ordered, not an exhaustive wishlist
  - Runtime-to-realistic-sink tests: exclusive open, stop/open ordering, rapid volume/seek/skip/output switch, failed negotiation and state rollback.
  - Queue sequence tests through Runtime: duplicates, remove/reorder/insert while decoding, repeat-one, shuffle changes and album-only play.
  - Native allocation sanitizer/leak test; repeated decode/seek/next-track/artwork and failure paths.
  - Full UI crossfade choices with the real sink contract, bounded chunk sizes and injected crossfade failure preserving every sample.
  - Known-waveform seek and gapless: FLAC plus MP3/AAC/Opus delay/padding, differing rates, decoder/filter flush, actual output frame count and continuity.
  - SQLite commit failures and ENOSPC mid-scan; source disappearance during traversal; corrupt DB boot; power loss around atomic state rename and WAL writes.
  - Current-image wired listening/measurement, screen-off audio, renderer close/reopen/timeout recovery and extended playback memory/XRUN soak.
  - WPA2 authentication/IP/DNS/traffic and Bluetooth fresh pairing/SBC/reconnect/disconnect/output switch, followed by sustained coexistence.
  - Current power envelope, low-battery behavior and explicitly scoped suspend/wake regression; use independent voltage/current/temperature evidence.
  - 10k/20k realistic metadata/artwork library RAM/latency/scan cost, followed by a clean-machine paired release build and independent install/recovery exercise.

Tests should be added at the failure-owning layer. More assertions in a mock that omits the failing contract will not close these gaps.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
