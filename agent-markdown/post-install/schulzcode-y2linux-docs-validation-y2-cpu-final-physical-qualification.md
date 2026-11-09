---
title: "Y2 CPU Final physical qualification - Innioasis Updater"
description: "Y2 CPU Final physical qualification <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-cpu-final-physical-qualification.html"
---

# Y2 CPU Final physical qualification - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 CPU Final physical qualification

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 CPU Final physical qualification > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-27, real Y2. This is the first observation sweep of the owner-flashed candidate; no implementation source edits, rebuild or flash. Private raw evidence: `out/cpu-final-physical-qualification/20260927T161145Z/`. Commands, stdout/stderr, exit codes, host UTC/duration and expected source/boot identity accompany receipts. Raw network/device identifiers remain private; no credentials/bond secrets or protected/calibration data were collected.

## Exact identity and admission
  - Linux: `ff586dfff2b5e7abd28af339c055375307308f1f`.
  - Reborn: `afcf9ffa1bc45073e97520d592c0284ce73fefcf`.
  - Kernel: `6.18.0-y2linux-cpu-final`.
  - Root: `2025.02.18-platform-v1.6`; release `1.0.0-cpu-final-candidate.1`, API1.
  - Boot: `18248d38-f426-4090-add7-a99a7a3a067d`.
  - Identity matches the sealed CPU Final manifest (receipt00).
  - Admission taint0, root/data/SD rw, all ext4 error counters0, CPU55C/PMIC53.315C.

## First runtime sweep``````

| Feature | Result | Implemented / actual physical observation |
| --- | --- | --- |
| GPT6 foundation | FAIL | Boot Y2TIMER: GPT6 preflight rejected; arch init returns -19. No counter preparation/arch registration. Exact rejected predicate is not instrumented. |
| GPT4 broadcast | FAIL | Normal GPT4 promotion did not run; actual broadcast is legacy mtk-clkevt. |
| PPI29 / per-CPU arch clockevents / CNTFRQ13MHz | FAIL / NOT_TESTED | All four actual events are dummy_timer; no arch timer interrupt registered. Per-core CP15 readback is unavailable through installed telemetry in this fallback. |
| High resolution / NO_HZ | FAIL | Runtime highres0/nohz0 on each CPU; hotplug logs dummy clockevent cannot enter oneshot/highres. 1ms sleeps have approximately10ms median on every core. |
| Legacy timer continuity | PASS | 182.297s monotonic /182.303s raw /182s RTC, same boot; interrupts advance, Err0. Interval exceeds the documented sched_clock half-wrap interval; no direct GPT2 register read was captured. |
| CPU1–3 hotplug | PASS narrow | Three individual cycles per core plus 4→3→2→1→4, scheduler affinity checked, secondary-off result0. All restored. Local architectural timer lifecycle remains unqualified. |
| Lower OPP scaling | PASS narrow | 598000/747500/1040000kHz: three ascending/descending sequences, requested/current/actual readback matches, no voltage fault. |
| High stock OPP admission | PARTIAL / gated | Silicon bin0 accepted; auto admission -95 (-EOPNOTSUPP), ceiling1040000. Table lists1196000/1300000, but policy forbids them; no override/stress attempted. |
| DVFS voltage change | NOT_TESTED / admission unavailable | PMIC216=0, fixed selector21e=48hex (=72), readback1.15V. Prepare explicitly requires216bit1; no voltage transition was attempted. Lower OPPs all use the same stock voltage. |
| schedutil | PASS bounded | Dynamic actual frequencies reach1040 under heavy load and return mostly598 afterward; no permanently pinned OPP. Legacy periodic timer/background load leaves appreciable high residency even when idle. |
| Kernel workload QoS | PASS | All eight classes, floor constraints, overlap, renewal beyond old deadline, expiry, process-death close, invalid class/duration rejection. Normal playback min0; maximum remains thermal/admission owned. |
| Reborn workload / interaction integration | FAIL | Actual path-filtered strace: write(fd,"Idle",4)=-EINVAL and write(fd,"Interactive",11)=-EINVAL. Formatted writes split the complete parser request. No playback/interaction lease appears despite real app playback/input. Scoped artwork uses the same writer. |
| Thermal maximum priority | PASS narrow | Existing cooling device state4 caps actual/policy to598 despite PlaybackHeavy floor747.5. Original state0 restored. No heat-trip experiment. |
| C1 WFI | PASS narrow | Usage/residency grows on all online cores; no rejected C1 states. |
| C2 SLIDLE | PARTIAL | Registered/enabled; no successful entry. CPU0-only, <=747.5MHz, screen-off, stopped audio and radios-off session produces busy fallback, blocker0xe07800 (initial0xf07800); no restore fault. |
| C3 DORMANT / deadline / CIRQ replay | NOT_TESTED | Default disabled; failed local-timer prerequisite makes entry unavailable. No forced blocker override or unsafe C3 entry. CIRQ is ready/inactive with entries/flushes0. |
| RTC alarm while awake | PASS | +8s alarm reads back, PMIC/EINT and RTC IRQ each advance once, alarm disables/clears after delivery. This is not SPM wake qualification. |
| Playback / resampling | PASS narrow | Silent60s FLAC fixtures: 44.1kHz and24/96→48kHz native ALSA S16, decode/filter counters advance, no XRUN/recovery/decode errors. Audible quality/EQ/ReplayGain/crossfade are not certified. |
| USB/Wi-Fi bounded data | PASS narrow | Reverse HTTP RAM fixture, six8MiB reads on each interface, identical SHA256. Deliberately paced transfer, not peak throughput. Host-bound HTTP attempt timed out; reverse direction works. DNS/TCP over Wi-Fi checked. |

## Suspend and restoration observations

First attached-USB sweep: freezer PASS with one5s debug sleep. Devices FAIL at `y2_charger_prepare_pm` (-16) before device suspend, because charging is active. This is an intentional active-USB guard. PM unwind emits a warning at `kernel/power/main.c:41` via `dpm_resume_end`, taint becomes512. There is no Oops, panic or reboot in this receipt. Filesystems stay rw/error0; all four cores, legacy timer and SSH recover. MUSB pm_suspends/restores remain0, so neither its corrected stale-status lifecycle nor full device resume has been exercised here.

CONSYS boots after freezer and failed devices unwind with full STP/patch/RF calibration, functions0x9, error0, transport_errors0 and boot_retries0. WLAN association/IP/route/DNS/TCP recovers. Some immediate service observations time out/report supplicant unavailable despite later direct COMPLETED andOnline records; distinguish readiness timing from controller boot failure. HCI/BlueZ/ BlueALSA return. The saved Bluetooth peer is disconnected and reconnect owner records completion_unknown_user_retry_required; no peer/PCM success is claimed.

Battery continuation completed devices/platform/processors/core on the original boot. Helper result0, all four CPUs restored, taint remains the known512, all ext4 errors0. Devices/platform/processors/core durations including radio lifecycle: 10.648/9.611/9.621/8.596s. The core debug stage logs a5s wait while IRQ/timekeeping is suspended; its console timestamps are not independent wall-time measurements.

MUSB now has pm_suspends4/pm_restores8, pm_stale0, DMA errors/program errors0. The cable was absent: this qualifies quiescent device context suspend/restore, not live ECM/ACM re-enumeration or post-resume transfer. Controller IRQ count remains132878 across these battery stages, without the old USB storm. CPUs1–3 each report power-off result0 and return online after processors/core. DSI/PHY/OVL are reprogrammed after each stage; no kernel Oops/panic/new WARN.

Core-stage radio restoration reproduces WMT mandatory STP opcode08/parameter02 -110 at monotonic1905.938. The implemented isolation/retry starts at1905.979, verifies full STP, applies both patches and calibrates RF at1906.965. Final powered1, functions0x9,error0,transport_errors0,boot_retries1. This is a physically observed successful fallback; Bluetooth peer/PCM readiness still lacks an available peer.

Full RTC suspend FAIL: first battery full-suspend session armed an18s RTC alarm through the harness and called the existing qualification helper. Persistent state stays `battery-rtc-suspend-0`, armed at monotonic1910.775; the last retained kernel line is `PM: suspend entry (deep)` at1912.921. There is no returned helper, after snapshot, SPM resume result, RTC wake reason or same-boot recovery. Wi-Fi was absent after radio quiesce; reconnecting USB did not enumerate the gadget. Owner reported screen off and restarted the Y2. Recovery boot is `2aff9ecf-dac0-4479-913e-46dc343964d0`, with previous orderly_shutdown=false, reset cause not observed and no pstore files. Logs do not establish an Oops/panic, the exact lost instruction, actual PCM entry or an electrical/battery failure. Classify as a qualification failure with a probable deep-entry/wake/context implementation defect, not a confirmed power fault.

Loss of the recovery path ended risky qualification under the owner's stop rule. No second full attempt, five-cycle endurance, controlled Power wake or separate RTC sleep-wake test was run. Owner restart is recovery, not a Power wake PASS. No full-suspend USB/radio/display/GPU/ALSA/Reborn restoration is promoted from the successful staged tests or the later fresh boot.

## Measurement method

See private `workload-measurements.json` for per-core CPU, OPP time-in-state, C1 entries/residency, system interrupts/context switches and temperature deltas. CPU percentages are capacity-normalized across four cores. OPP residency is the shared policy, not four independent PLLs. Idle exits/s is an explicitly labelled wake proxy; it is not the hardware wakeup_sources count. Low-level wake latency for never-entered C2/C3 is unavailable. Values include observation overhead.

Exploratory receipt06 overlapped hotplug/QoS/input and is excluded from isolated workload conclusions. Receipt16 initial idle overlapped the end of app tests; receipt18 supplies isolated idle/light/24-96 playback. Earlier receipt15 screen idle/44.1 playback and later receipt16 medium/heavy/return-idle are retained. Small incremental scan is a fixture check, not a large-library stress result. No fresh long endurance or electrical/power-consumption result is inferred.

## Recovery controls

Existing installed boot option source/packaged documentation confirms `y2.cpu_safe=1` → legacy timer,598MHz ceiling,WFI,suspend disabled and isolated `y2.local_timer=off`, `y2.cpuidle=off`, `y2.deep_idle=off`, `y2.dvfs=off`, `y2.suspend_safe=1`. Runtime normal flags are allfalse. No reboot into safe mode or recovery-image deployment is part of this first sweep; physical recovery boot qualification remains NOT_TESTED.

## Final assessment

Not suitable for acceptance as the normal CPU Final platform. The runtime fallback remains usable, with reliable bounded lower-OPP scaling/hotplug/WFI, software-observed native playback and data transfer. The new timer architecture, highres/NO_HZ and Reborn semantic hints fail; high OPP/DVFS voltage admission is unavailable. SLIDLE never enters, DORMANT/deadline/CIRQ replay remain unqualified, and the first full RTC suspend loses recovery until owner restart. Successful staged resume and CONSYS retry are meaningful partial improvements, not full same-boot suspend success. Do not enable automatic system suspend or C3 based on this candidate's software completion claims.

## Bounded runtime workload measurements

15–21s windows, four online CPUs, schedutil; all idle time below is C1 WFI. C2/C3 successful entries/residency are0. Frequencies share one policy. Network payload is paced, not peak throughput. USB payload/hash success is retained, but its observer lacked the final snapshot; no USB CPU/OPP percentage is invented.

| Workload | Total CPU % | OPP % 598 /747.5 /1040 MHz | Average C1 idle % | Idle exits/s proxy | Interrupts/s /context switches/s | CPU /PMIC C at end |
| --- | --- | --- | --- | --- | --- | --- |
| screen-on-idle | 8.31 | 73.14 / 1.15 / 25.72 | 89.37 | 469.27 | 540.68 / 445.45 | 56.6 / 54.485 |
| screen-off-idle | 6.79 | 79.54 / 1.34 / 19.12 | 91.07 | 416.79 | 467.22 / 418.7 | 56.3 / 53.315 |
| playback-44100-screen-off | 12.65 | 68.36 / 0.96 / 30.68 | 84.11 | 499.77 | 590.01 / 673.74 | 57.4 / 53.9 |
| isolated-playback-96000-screenoff | 11.58 | 68.37 / 1.15 / 30.48 | 82.81 | 506.12 | 604.68 / 682.29 | 58.5 / 54.485 |
| medium | 24.94 | 1.66 / 5.17 / 93.17 | 68.87 | 326.94 | 453.24 / 474.81 | 60.0 / 54.485 |
| heavy | 85.41 | 0.0 / 0.0 / 100.0 | 13.07 | 62.7 | 451.38 / 541.05 | 65.8 / 58.579 |
| return-idle | 9.62 | 69.21 / 1.02 / 29.78 | 88.42 | 393.65 | 458.5 / 418.89 | 58.5 / 54.485 |
| wifi-transfer-actual | 12.07 | 76.47 / 1.01 / 22.51 | 80.79 | 2219.97 | 2661.99 / 2611.1 | 60.1 / 55.655 |

Light load remains mostly low OPP; medium/heavy demand scales upward. Idle and playback still spend19–31% at1040MHz and approximately100Hz GPT +100Hz broadcast IPIs to each online secondary remain; NO_HZ is actually inactive. Screen-off reduces activity relative to the paired screen-on window, releases GPU runtime power and prevents continuous rendering, but does not establish optimal idle. Per-core CPU values and exact raw durations remain in the private JSON.

## Coverage, runtime idle counters and limits

| Requested area | Final physical status / limit |
| --- | --- |
| Exact identity / full pre-test snapshot | PASS;00/01 capture identity, health, CPU/timer/IRQ/memory/thermal/power/audio/USB/radio and boot evidence. |
| Timer routing/CNTFRQ/oneshot/hres/nohz | FAIL admission; fallback continuity PASS. CP15 frequency/counter per-core readback NOT_TESTED because installed fallback offers no such readback. |
| Hotplug / core combinations | PASS bounded; three individual cycles per secondary plus combinations; processors/core staged resume adds further cycles. |
| Lower OPP transitions / load / schedutil | PASS bounded;1040MHz highest stable observed. High bins gated;1196/1300 NOT_TESTED. Voltage/frequency ordering and rollback physically NOT_TESTED because voltage path was not admitted. |
| Eight kernel workload classes | PASS acquisition/renewal/overlap/expiry/process-death/invalid requests; real Reborn writer FAIL. Kernel250ms renewal/expiry PASS; app input/playback/scan hint integration FAIL, artwork inherits the confirmed writer defect. |
| Playback / screen / scan / transfer | PASS narrow fixtures and actual bounded USB/WLAN payloads; large scan, DSP/EQ/ReplayGain/crossfade, audible quality NOT_TESTED. |
| C1 / C2 / C3 | C1 PASS; C2 PARTIAL registered/enabled but blocked; C3 NOT_TESTED and left disabled. No C2/C3 exit latency measured. |
| CIRQ / GPT deadline handoff / deeper fallback | NOT_TESTED entry/replay; ready/inactive telemetry only. Safe C2→C1 fallback observed; C3 hierarchy cannot be physically exercised with failed local timer. |
| Thermal priority | PASS narrow cooling-device cap versus workload floor; actual thermal trip NOT_TESTED, no overheating induced. |
| Safe-mode / isolated recovery boot options | Source/package presence PASS; reboot into each option NOT_TESTED. |
| Suspend | Freezer PASS; USB-attached devices refused with unwind WARN. Battery devices/platform/processors/core PASS. Full RTC first attempt FAIL; further cycles stopped. |
| Power wake / RTC sleep wake | NOT_TESTED controlled Power wake; RTC sleep wake FAIL as a complete end-to-end attempt, awake RTC alarm PASS. Exact RTC-vs-CPU-resume fault not isolated. |
| Post-full-resume playback/network/UI | NOT_TESTED because no same-boot full resume. Fresh-boot app/renderer/USB/radio/network health recorded separately. |
| High-bin stress | NOT_TESTED; admission guard retained, no manual unsupported OPP request. |

Final recovery snapshot31, on the new boot (these are not accumulated old-boot campaign totals): C1 CPU0 usage26473/time148.008s; CPU1 16083/137.110s; CPU2 18801/144.494s; CPU3 18245/148.315s. C1 rejected0; C2/C3 usages/time0. SLIDLE aborts25444, restore failures0, last_error-16, slow_broken=N; C3 disabled on each CPU. Earlier deliberate CPU0-only blocker test has about1397 additional aborts in20s, mask0xe07800; standard four-core topology also rejects SLIDLE's single-CPU prerequisite. Nominal exit latency1/50/500us is configuration, not a physical latency measurement. Observed software timer granularity remains10ms.

`decoder_stalls` increases during successful fixture playback. Source `app/reborn/src/playback.rs:174` counts a full bounded producer queue and sleeps5ms; it does not identify ALSA starvation. XRUN/recovery/decode/filter error counts remain0. The synthetic files are silent; no listening claim is made.

## Failure classification and one prioritized CPU Final Fix Batch

No implementation correction was made during this sweep. One coherent batch:
  - Deep-suspend recovery (qualification failure, probable implementation bug):

add retained stage breadcrumbs around the actual SPM/CIRQ/CPU-context entry and return, reconcile wake masks/RTC and CPU boot vector/coherency restoration, and keep automatic suspend unavailable until same-boot recovery succeeds. Battery pm_test passes isolate the observed failure beyond staged coverage; absent full-entry breadcrumbs prevent a narrower proven root cause.
  - Timer admission (configuration/ownership incompatibility, likely regression):

fix the GPT4/GPT6 inherited-owner admission in `kernel/platform/local-timer.c` with exact predicate/register diagnostics. Combined preflight currently rejects before PPI29 registration on both observed boots. Preserve legacy fallback; do not blindly remove hardware guards. This blocks highres/NO_HZ and dormant.
  - Reborn semantic hints (confirmed implementation bug): serialize `Class ms\n`

into one `write_all` request in `crates/reborn-platform/src/workload.rs`; device strace proves partial formatted writes getEINVAL. Validate playback, interaction/coalescing/screen-off, artwork, scan and transfer producers against the actual installed character-device parser.
  - Board DVFS admission (hardware mode/configuration incompatibility): reconcile

stock software-selector mode with source-backed voltage ownership before enabling high bins. PMIC216=0 fails the required hardware-selector bit1 gate in `kernel/platform/pwrap.c`; fixed1.15V lower OPP scaling works. No electrical instability or unsupported silicon bin has been demonstrated.
  - Idle and PM unwind (configuration blockers / implementation defect): resolve

retained peripheral/MSDC/APDMA/I2C clock ownership behind0xe07800, retain real blockers, then qualify SLIDLE/dormant/CIRQ/deadline restoration. Correct the charging.prepare refusal unwind WARN; retain the active-USB safety guard. Preserve the physically successful CONSYS isolated retry and its single reconnect owner; add service readiness observation after controller boot.

Successful fallbacks: GPT timer after arch admission rejection;1040MHz ceiling at stock voltage after DVFS admission refusal; SLIDLE→WFI; C3 remains disabled; thermal ceiling overrides a higher QoS floor; one failed WMT boot is isolated and its second boot succeeds. Full suspend did not recover autonomously.

## Owner actions, final state and evidence retention

Owner actions: USB unplug; USB reconnect and screen observation (initially on, then corrected off); restart after the requested Power wake attempt. Restart method/press duration was not specified. No commands, frequency selection, audio listening, manual wheel action or repeated suspend approvals were requested.

Recovery receipt28/29/31: same installed source pair/release, new boot above, taint0, all CPUs online, schedutil598–1040MHz, cooling state0, C3 disabled, pm_test none, RTC alarm cleared, root/data/SD rw/error0, USB configured with DMA errors0, CONSYS/HCI/BlueZ/BlueALSA ready, WLAN COMPLETED/IP/route/DNS/TCP works. Some immediate API radio readiness reads still time out; later direct association and endpoint checks succeed. Screen auto-off is normal app policy, not sleep. Fresh-boot recovery does not qualify device resume.

Only the two owned silent files and their empty qualification music directory were removed; incremental rescan restores original library count3. Playback left stopped, wired output and volume preserved. The app retains a stopped selected fixture ID; no raw session/database edits or audible user-track start were made. Owned persistent suspend evidence remains on Y2 and is copied locally. Reboot removed volatile test server/harnesses; no CPU loads, trace attachment or alarm remain. No protected/calibration regions or user media were altered.

Private receipts00–31, command/exit/timing JSON, path-filtered workload trace, measurement exclusions, workload-measurements.json, persistent battery-stage archive/extracted logs, previous-boot tail and host transport observer are kept under the timestamped directory. The initial gzip-tar retrieval failed because target BusyBox lacks -z; plain tar retry succeeded. A narrow read-only status observer lost Wi-Fi during quiesce; persistent local receipts establish completion. BusyBox sync ignored -f arguments but still performed global sync; stage logs and metadata survived restart. No source/build artifact was substituted during tests.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
