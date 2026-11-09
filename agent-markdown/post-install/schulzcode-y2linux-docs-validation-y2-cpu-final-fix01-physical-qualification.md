---
title: "Y2 CPU Final Fix01 physical qualification — 2026-09-27 - Innioasis Updater"
description: "Y2 CPU Final Fix01 physical qualification — 2026-09-27 <!-- knowledge-base-scope: historical-validation-receipt; baseline02-sync 2026-10-03 -- Historical exact-image rece"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-cpu-final-fix01-physical-qualification.html"
---

# Y2 CPU Final Fix01 physical qualification — 2026-09-27 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 CPU Final Fix01 physical qualification — 2026-09-27

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 CPU Final Fix01 physical qualification — 2026-09-27

Historical exact-image receipt. This report retains its named Fix image and dated result. It does not describe Baseline02 or negate the newer bounded UART01 C1/C2/C3 passes. See [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) and [latest CPU-idle hardware proof](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md).

Verdict: FAIL for acceptance as the normal Y2 CPU platform. The safe observation sweep is complete. GPT6/GPT4/PPI29, actual highres/NO_HZ, real workload leases, conservative OPPs, hotplug, WFI and bounded native playback pass. SLIDLE still cannot enter, automatic parking was not observed, high OPPs remain gated, the first staged suspend attempt lost recovery, and a subsequent USB transfer lost connectivity while the UI remained usable. DORMANT and full deep wake are not qualified. No implementation source was patched, candidate rebuilt, device flashed, history rewritten or changes pushed during this sweep.

This supersedes only the corresponding CPU Final failures in the [previous physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-PHYSICAL-QUALIFICATION.md). The [Fix01 implementation receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01.md) and [source ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-SOURCES.md) remain software provenance, not hardware acceptance. PASS below applies to the bounded observed behavior; PARTIAL is incomplete evidence; NOT_TESTED never means a hardware pass.

## Identity and evidence

Exact installed identity matched before the first test and after both recoveries:````````````````

| Field | Observed |
| --- | --- |
| Y2Linux runtime commit | 0de6e951b438bf0f2d701e23e476d2b2405ba3c6 |
| Reborn runtime commit | 36db1869c6bab1ad2d00b7d8e7807ea6ef5b3803 |
| Kernel | 6.18.0-y2linux-cpu-final-fix01 |
| Rootfs | 2025.02.18-platform-v1.7 |
| Release / build | 1.0.0-cpu-final-fix01-candidate.1 / Y2LINUX-CPU-FINAL-FIX01 |
| Host Linux HEAD, start and finish | a5598918a7839d10d5349d3354d720050adb97f8 |
| Host Reborn HEAD, start and finish | 36db1869c6bab1ad2d00b7d8e7807ea6ef5b3803 |

The host Linux HEAD is a documentation continuation beyond the runtime source; device identity, rather than host HEAD, determines attribution. Existing dirty documentation and Reborn UI asset changes were preserved. No commit was created.``````

| Boot | ID | Boundary |
| --- | --- | --- |
| Initial | d3f4d265-ced8-4b53-8037-84637d765a89 | identity, primary harness, failed staged request |
| First owner recovery | 1807c573-b7c2-469e-9a16-5645b4d25ecb | immediate retained capture, independent timer/QoS/idle/audio/stress, USB loss |
| Second owner recovery | 81e422f3-43cd-4ad6-877f-692eb1191b36 | immediate retained capture, independent Wi-Fi/awake RTC/timer continuity, cleanup |

Private evidence is under `out/cpu-final-fix01-physical-qualification/20260927T205514Z/` (restricted parent). It contains host UTC and durations, device monotonic samples/boot IDs, runtime source identity, exact remote programs, stdout/stderr, host exit receipts and explicit timeout/failure receipts. `SHA256SUMS` seals the collected files; `qualification-summary.json` records the final classification. Credentials, private keys, bond secrets, NVRAM and calibration were not exported.

The inspected, unchanged `tools/development/qualify-cpu-fix01.py` ran with `--run --host y2 --wifi-host y2-owner-wifi`. A session-local SSH wrapper used the existing owner key and pinned host key; global SSH configuration was not changed. Its Run/REMOTE helpers also retained the supplementary checks. The session wrapper allowed ordinary failures to be recorded independently while stopping suspend on recovery loss. It does not change the installed candidate.

The primary harness cannot cover every requested producer or measurement and treats USB-online as charging. Supplementary SSH checks covered the omissions; the charging distinction is retained below. Temporary Wi-Fi recovery SSH used existing device host keys, key-only access and no forwarding. It was removed after testing. Neither listener nor private key contents were retained.

## Timers and hotplug — PASS

GPT admission is successful on all three boots. The actual inherited GPT4 state was control `0x31`, clock `0`, interrupt-enable `0x10`; GPT6 initially was stopped. Fix01 reports `prepared_13mhz`, `gpt4_sole_owner`, ready/events-ready Y and registration error 0. Thus the formerly rejected inherited GPT4 condition is physically reconciled; this run prepared GPT6 rather than testing adoption of an already-running GPT6. GPT1 is stopped/masked in the live boot evidence.

GPT6 control is `0x31`, clock `0`; it advances. Admission calibration compares GPT2/GPT6/CNTP over approximately 2 ms: initial counts 26000/26005/26000, and final boot 26001/26007/26001. All CPUs report CNTFRQ 13000000, error 0. The final read-only continuity sample sees GPT6 low `0xbe96bee3 -> 0xc0e9242d`, RTC advance three seconds, and continuous raw/monotonic time. Samples are not synchronized frequency-metrology measurements; the calibration and advancing counters are the rate/continuity evidence.

Clocksource is `arch_sys_counter`, all four local events are `arch_sys_timer`, and broadcast is `y2-gpt4-broadcast`. GIC PPI29 `arch_timer` counts advance on all CPUs. `/proc/timer_list` shows `hrtimer_interrupt`, actual hres/nohz state 1 and oneshot broadcast handling. Tick-stopped samples were observed, including CPU0 on the final boot. This verifies runtime NO_HZ, beyond a configuration flag.

Three individual offline/online cycles per secondary plus 4 -> 3 -> 2 -> 1 -> 4 completed. Nine individual re-online receipts retain timer_list proving no dummy local event. CPU affinity and policy recover; all four CPUs are restored. The short event dictionary in one hotplug script used an incorrect sysfs path; its retained timer_list, PPI counts and final correct clockevent sysfs reads provide the actual verification, rather than that empty dictionary.

100 requested 1-ms sleeps per CPU measured medians 1.108, 1.088, 1.089, 1.088 ms; p95 1.132, 1.118, 1.116, 1.094 ms. The previous image measured roughly 10 ms. Evidence: `harness/timer-verdict.json`, `extra-timer-hotplug-recovered/`, `extra-final-timer-continuity/`, and initial/recovery snapshots.

## QoS and real producers — PASS

Accepted kernel leases were observed from the installed app/workers, not just manual kernel requests. The fragmented-writer failure no longer prevents useful requests. No direct syscall write-count trace was taken in this physical sweep; accepted real producer leases establish the repaired integration behavior.

| Producer | Status | Physical observation |
| --- | --- | --- |
| Idle | PASS | idle app lease observed |
| PlaybackNormal | PASS | both playback fixtures; repeated lease renewal, including screen-off |
| PlaybackHeavy | PASS | real UI crossfade configuration set to 5000 ms; accepted heavy lease and 747.5-MHz minimum |
| Interactive | PASS | supported wheel key-event injection through the real input/UI path; expiry and renewed/coalesced bursts |
| ArtworkDecode | PASS | actual Music -> Albums -> Album collection artwork worker, lease captured |
| LibraryScan | PASS | actual Reborn scans, including 200 temporary small fixtures |
| NetworkTransfer | PASS | installed transfer begin/commit service, SHA-verified fixture publication |
| Maintenance | PASS | installed safe export worker, completed temporary export, lease captured |

Interactive single intervals were about 232/209/239 ms when observed after input, consistent with a 250-ms lease. Renewed bursts coalesced. Screen sleep immediately removed Interactive while playback's lease remained and renewed three seconds later. An initial unsupported EV_REL injection was ineffective; the successful test used the actual wheel EV_KEY path. No owner wheel action was required. Crossfade was returned to its original zero setting.

Additional isolated kernel clients exercised all eight encodings, acquire, renew beyond an old expiry, expiry, close, overlaps and killed-child cleanup. This does not certify actual Reborn process-death restart. Application policy still uses leases and schedutil; no app request sets a MHz value. Evidence: `extra-input-heavy-artwork-key-events/`, `extra-artwork-collection-producer/`, `extra-real-worker-fixtures/`, `extra-kernel-qos-lower-opps/`, `extra-library-scan-stress/`.

## OPPs, DVFS and thermal authority

| OPP | Admission | Physical exercise |
| --- | --- | --- |
| 598 MHz | PASS | repeated bounded transitions, idle, thermal cap |
| 747.5 MHz | PASS | repeated transitions, heavy/input leases |
| 1040 MHz | PASS | repeated transitions, schedutil medium/heavy load |
| 1196 MHz | FAIL | NOT_TESTED: requests remain safely capped at 1040 MHz |
| 1300 MHz | FAIL | NOT_TESTED: requests remain safely capped at 1040 MHz |

Bin0 is recognized. The real software selector mode now passes its old blocker: PMIC control `0x216=0`, selected bank `0x21e`, selector/NI feedback `0x48`, baseline 1.15 V. However automatic admission still returns -95 at `pwrap_readiness`, prepared 0. Qualification/policy ceiling is 1040000 kHz, voltage fault N. The static available-frequency list includes high OPPs, but that list is not evidence of admission.

The precise remaining predicate group is in `kernel/platform/pwrap.c`: wrapper base must read 0, base+4 must read 1, base+0x50 must read 0x1ff. Diagnostics do not expose those three operands. A read-only attempt could not inspect MMIO because `/dev/mem` is absent. No node, module, register override or admission bypass was introduced. The exact mismatching operand and board interpretation remain unknown; selector mode itself is no longer the root of rejection.

All exercised lower OPPs stayed at 1.15 V. **Voltage-changing DVFS, up/down voltage ordering, rollback under a voltage fault and high-OPP stress are NOT_TESTED.** Lower frequency changes/readback and schedutil load response pass. A bounded cooling-device state request capped actual/policy at 598 MHz despite a live PlaybackHeavy 747.5-MHz minimum; original state 0 was restored. This demonstrates thermal authority, not a naturally induced overtemperature trip.

Two medium-load workers and four full-load workers completed 10743 SHA checks with zero integrity errors. Heavy load reached 1040 MHz, approximately 99.93% four-core utilization; max sampled CPU/PMIC temperatures 65.4/57.409 C. The 75/65-C test guards did not trip, thermal protection remained enabled, and normal schedutil returned afterward. Evidence: primary OPP matrix, `extra-kernel-qos-lower-opps/`, `extra-readonly-readback/`, `extra-bounded-load-integrity/`.

## Idle, blocker ownership and coordinator

C1 WFI is PASS: counters/residency advance with zero rejected entries. C2 SLIDLE entry is FAIL: registered/enabled but **zero entries and zero residency** throughout; fallback works, restore failures 0, broken N. C3 DORMANT is NOT_TESTED, kept disabled with zero entries/residency.

The former `0xe07800` decodes precisely as bits 11 APDMA, 12 MSDC0, 13 MSDC1, 14 MSDC2, 21 I2C0, 22 I2C1, 23 I2C2. Controlled CPU0-only/598-MHz/screen-off tests now reveal `0x103800` (APDMA/MSDC0/MSDC1/BTIF), falling to `0x3000` with radios off. Unused MSDC2/I2C2 and I2C0/1 are off in the observed idle state; APDMA varies with real activity and BTIF disappears on radio quiescence. Active DMA was never reset and blocker masks were never overridden.

| Bit | Clock/owner | Expected idle behavior | Observation / next correction |
| --- | --- | --- | --- |
| 11 | APDMA, active peripheral DMA users | block during activity, gate when drained | disappears when quiet; retain real busy checks |
| 12 | MSDC0, eMMC host/root/data | gate idle controller without changing card rails/state | host runtime-suspended but source/gate still enabled; runtime retention bypass |
| 13 | MSDC1, SD host | same controller ownership discipline | same runtime retention bypass |
| 14 | MSDC2, unused host | off after checked quiescence | no longer blocking |
| 20 | BTIF, shared radio transport | block while radio transport requires it | additional current blocker; disappears with radios off |
| 21 | I2C0, device users | gate between transactions | no longer blocking in controlled samples |
| 22 | I2C1, device users | gate between transactions | no longer blocking in controlled samples |
| 23 | I2C2, unused controller | off after checked idle | no longer blocking |

Source-backed remaining clock-lifecycle cause: both MMC hosts report runtime `suspended`, control `auto`, autosuspend 50 ms, while CCF MSDC0/MSDC1 source and gate clocks each retain enable/prepare counts 2 and hardware Y. The last hunks of `kernel/patches/0009-y2-msdc-readonly.patch` add a CONFIG_Y2_POWER/Y2 early return inside msdc_runtime_suspend/resume, skipping ordinary register save, clock gate, ungate and restore. The comment speaks of s2idle retention, but the actual branch also affects ordinary runtime PM. Pinned Linux 6.18 `mtk-sd.c:3280` confirms these are runtime callbacks. This explains persistent idle controller ownership; it must be corrected without card resets, rail cycling or protected storage writes. No fix was made during qualification.

Four-CPU diagnostics can show cached mask 0 because topology rejects SLIDLE before reading clock blockers. That is not proof that all clocks are idle. Final third-boot cleanup counters, not combined across boots: C1 CPU0..3 usage 43573/45124/33386/40634 and time 376.318/394.389/383.566/391.945 seconds; SLIDLE attempts/aborts 36916/36916, entries/failures 0/0, last error -16. CIRQ entries/flushes and dormant entries/resumes remain zero.

Automatic parking goal is FAIL in observed normal operation, with overall coordinator evidence PARTIAL: initial 120-s and separate 160-s screen-off periods kept four CPUs online; park/restore counts 0, broken N, last error 0. Quarter-second activity/frequency bursts repeatedly break eligibility (busy samples 0..31%, recurring 1040-MHz demand). A sustained eligible 30-second window was not proven. This does not show the hotplug mechanism itself is broken. Automatic restoration of coordinator-owned parked CPUs is NOT_TESTED because none parked. Display wake correctly left manually offlined secondaries off; explicit restoration brought all four back, a narrow ownership PASS.

Timers/GPT4/CIRQ readiness and physical secondary-off state pass prerequisites. MSDC blockers and remaining domain state prevent complete dormant admission; deadline/CIRQ/SPM context handoff is NOT_TESTED. After the recovery loss, neither C3 nor full sleep was attempted or repeatedly hammered. Evidence: `extra-controlled-slidle/`, `extra-radios-off-slidle/`, `extra-coordinator-normal-policy/`, read-only CCF/MMC diagnostics.

## Suspend, retained evidence and awake RTC

The first staged request was `pm_test=devices` through the installed `y2-suspend --owner-qualify` helper, with USB attached. The helper requested deep mode, but the devices test is not a full RTC deep-suspend attempt. Radios quiesced and sync completed; then USB/Wi-Fi recovery disappeared. Automatic reconnect attempts timed out before asking for Power. One Power press did not recover the session; the owner restarted the device.

| Test | Status | Limit |
| --- | --- | --- |
| Charger refusal / clean -EBUSY unwind | NOT_TESTED | USB online, but BAT0 was Not charging / charger hold; primary harness charging predicate was insufficient |
| First devices-stage attempt | FAIL | no same-boot result or recovery; restart required |
| Freezer / platform / processors / core | NOT_TESTED | further PM entry stopped after loss of recovery |
| Full RTC deep suspend | NOT_TESTED | prerequisites/staged acceptance failed |
| Deliberate full Power wake | NOT_TESTED | no successful full-sleep basis |
| Five full RTC cycles | NOT_TESTED | first successful same-boot full resume absent |
| Full device restoration | NOT_TESTED | clean new boots are not suspend restoration |
| Awake RTC alarm/IRQ | PASS | +8-s alarm armed; PMIC EINT25 and RTC IRQ20 increment; alarm cleared; same boot |

The inability to recover the staged request is a failure regardless of the unproven charger predicate. No post-entry trace identifies an exact stalled instruction, and no retained evidence demonstrates panic/Oops. Previous image's staged success must not be carried forward to this candidate.

**Persistent diagnostics are PARTIAL and fail the requested precise-boundary goal.** `/data/system/platform/suspend-last.json` survives both restarts and ends at `kernel_suspend`, after `quiescing_radios` and `syncing`, request boot `d3f4d265-ced8-4b53-8037-84637d765a89`. Its result 0 is checkpoint bookkeeping, not a successful suspend return. The kernel SRAM current/previous records are valid=0, sequence=0, stage=NONE. The reset entry word is `0x347e3bae` after recovery versus `0x367e3ba2` initially; expected resume stamp `0x59325253` was not observed. SPM wake/PCM/vector/CIRQ/RTC/CPU snapshots inside these invalid records are unavailable, not proven zero register values.

The owner restart's warm/cold retention characteristics are unknown. Therefore invalid SRAM cannot prove the CPU never dispatched, that entry reached SPM, or that journal writes themselves hung. The new first kernel PM journal mark before normal entry logging is a targeted boundary to validate, not an established root cause. Fix02 must first prove safe awake journal write/readback and retention, and recover a usable earlier PM checkpoint before another risky suspend attempt.

Immediate captures on both new boot IDs precede unrelated tests: `extra-immediate-recovery/`, `extra-second-immediate-recovery/`. Primary `harness/` has exact staged request, connection failures and incomplete receipts. `extra-awake-rtc/` proves awake alarm/IRQ only; it cannot certify SPM wake masks, CIRQ replay, CPU0 resume vector or full context restoration.

## Playback, connectivity and recovery

Native ALSA fixture playback at 44.1 kHz and 24/96 -> 48 kHz is PASS for bounded software operation: output state/rate observed, decoded frames advance, zero XRUNs, FFmpeg decode/filter errors and corrupt packets. Fixtures were silent; no perceptual listening or analog fidelity was certified. Configured crossfade exercises heavy policy, not an end-of-track blend or independent EQ test. `decoder_stalls` reached 4872; source `app/reborn/src/playback.rs:174` counts a full producer queue awaiting playback, not decoder corruption or an ALSA underrun. The counter is retained rather than represented as zero.

CONSYS runtime quiesce/restart is PASS: first mandatory STP/WMT boot times out -110, isolation is recorded, exactly one retry then firmware patches, RF calibration, WLAN and HCI return. `radio_boot_retries=1`, activated/powered 1, functions `0x9`, calibrated 1, error/transport errors 0. The existing reconnect authority remains unchanged. This is independent runtime radio restoration, not full suspend restoration. BlueZ/BlueALSA/controller health passes; Bluetooth peer audio was not exercised.

USB is PARTIAL, stress/recovery FAIL. The first 256-KiB bidirectional scratch roundtrip has matching SHA256. During the second bounded transfer SSH stopped responding, host USB connectivity disappeared, and the owner restarted to recover. The owner explicitly confirms the Y2 UI remained usable. This is a transport failure, not demonstrated spontaneous reboot or a complete SoC hang. The third boot's durable history additionally records the second boot's orderly shutdown. The in-RAM USB measurement observer was lost, so its CPU/OPP measurement is N/A. There is insufficient failed-boot IRQ/DMA evidence to label it the old IRQ storm or identify a specific controller fault. Wi-Fi was tried after the owner's restart had already removed the temporary listener; that refusal is not proof Wi-Fi was unavailable before the restart. USB stress was not repeated.

Independent third-boot Wi-Fi integrity PASS: four 256-KiB SHA-verified roundtrips, 1 MiB each direction, no transfer errors. Association/IP/default route are observed afterward; DNS after full resume is NOT_TESTED. Final health reports `wifi: DEGRADED / supplicant_unavailable` despite `iw` association, route and verified TCP transfers; retain this telemetry discrepancy, not an invented Wi-Fi transport failure. Evidence: `network-integrity/`, `wifi-integrity/`, `extra-radios-off-slidle/`, `extra-retained-error-observation/`.

## Workload measurements

Each row uses direct /proc counters and shared policy time_in_state deltas; CPU and C1 percentages are normalized to total four-core capacity. All rows below had four cores online. OPP columns are residency percent in order 598/747.5/1040 MHz; voltage was 1.15 V, highres/NO_HZ active, C2/C3 residency zero. IRQ/context rates are system totals, temperatures are sampled CPU/PMIC. Per-core CPU, absolute entries/residency, idle-exit proxies, actual/requested OPP, lease classes and coordinator state are retained in `workload-measurements.json`. Observer work is included; this is bounded workload policy measurement, not electrical power measurement, maximum throughput or endurance qualification.

| Workload | CPU % | OPP % 598/747.5/1040 | Cores | C1/C2/C3 % | IRQ/s | Context/s | CPU/PMIC C |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Screen-on idle (20 s) | 9.75 | 73.27/1.14/25.58 | 4 | 89.43/0.00/0.00 | 495.82 | 544.81 | 54.4/53.315 |
| Screen-off idle (20 s) | 8.66 | 78.64/0.70/20.67 | 4 | 90.67/0.00/0.00 | 397.25 | 512.88 | 52.2/50.976 |
| Screen-off idle (160 s) | 9.74 | 73.71/1.05/25.24 | 4 | 89.64/0.00/0.00 | 391.49 | 503.93 | 51.8/51.561 |
| 44.1 playback (25 s) | 11.72 | 71.79/0.68/27.53 | 4 | 87.64/0.00/0.00 | 762.04 | 977.32 | 51.2/50.391 |
| 24/96 -> 48 playback (25 s) | 14.20 | 68.87/0.64/30.49 | 4 | 84.51/0.00/0.00 | 768.33 | 964.91 | 52.4/50.391 |
| Heavy policy / crossfade configured (25 s) | 13.83 | 0.00/71.87/28.13 | 4 | 85.27/0.00/0.00 | 849.70 | 960.66 | 56.0/55.655 |
| Scan 200 fixtures (20-s window) | 22.31 | 61.40/0.84/37.76 | 4 | 76.67/0.00/0.00 | 1034.81 | 1576.88 | 54.0/53.315 |
| Wi-Fi bounded transfers (25 s) | 13.02 | 63.83/0.84/35.33 | 4 | 85.91/0.00/0.00 | 574.42 | 699.28 | 53.9/52.146 |
| Medium CPU load (20 s) | 35.32 | 0.10/0.50/99.40 | 4 | 64.05/0.00/0.00 | 524.22 | 566.78 | 57.7/53.900 |
| Heavy CPU load (20 s) | 99.93 | 0.00/0.00/100.00 | 4 | 0.01/0.00/0.00 | 648.35 | 696.00 | 65.4/57.409 |
| USB transfer | N/A, observer lost | N/A | 4 before loss | N/A | N/A | N/A | N/A |

The 200 extra small scan files (about 9.5 MiB) complete discovery in roughly 1.387 s; the 20-s scan row includes idle tail and 5-ms lease polling. It is not a large-library stress result. Wi-Fi's row likewise covers four small transfers inside a 25-s interval. Raw USB measurement loss is preserved as N/A.

Old screen-off baseline: CPU 6.79%, OPP 79.54/1.34/19.12%, C1 91.07%, 467.22 interrupts/s, 418.7 context switches/s. Fix01's short screen-off row has fewer interrupts, but higher CPU/context switching; the 160-s row still has recurring high-frequency demand and no parking/C2. Conditions/observation overhead differ. No overall idle-energy improvement has been demonstrated.

Normal playback mostly uses 598 MHz; heavy playback uses the real 747.5 floor, and CPU work reaches 1040 automatically. Interactive expiry and thermal authority work. Intelligent performance policy is PARTIAL because useful system idle, high voltage operation and suspend remain unqualified.

## Cleanup, safe fallbacks and owner actions

Final snapshot: boot `81e422f3-43cd-4ad6-877f-692eb1191b36`, all four CPUs online, schedutil 598..1040 MHz, thermal request restored, crossfade 0, stopped playback, C3 disabled, radio controllers running, display/GPU/ALSA/Reborn responsive. Temporary scan/playback/artwork/export/transfer files and the test Wi-Fi listener were removed; the original three visible library tracks remain. Durable failed suspend evidence was preserved. Host SSH configuration and device access policy are unchanged. Root/data/SD are rw, all three ext4 error counters 0, taint 0, and final dmesg has no panic/Oops/WARNING/EXT4-fs/I/O-error lines. Final health is DEGRADED only for the recorded Wi-Fi supplicant telemetry discrepancy.

The packaged/runtime/source fallback controls (`y2.cpu_safe=1`, `y2.local_timer=off`, `y2.cpuidle=off`, `y2.deep_idle=off`, `y2.dvfs=off`, `y2.suspend_safe=1`) were inspected for coherence. Their boot activation is NOT_TESTED; no fallback reboot or flash was done. Candidate/fallback artifacts remain unchanged. No unsafe high-OPP/C3 guard, thermal protection or charging refusal was overridden.

Exactly three physical owner actions occurred:
  - Power once after staged-request automatic recovery timed out: no recovery.
  - Restart after that failed staged request: first recovery boot.
  - Restart after USB connection loss while UI stayed usable: second recovery boot.

The second event also required one text clarification to distinguish manual restart from spontaneous reset. No owner shell command, frequency selection, wheel operation, listening request or USB cable action was required.

## Separate acceptance answers and one coherent Fix02 plan

| Question | Answer |
| --- | --- |
| Did the timer fix work? | PASS |
| Are highres timers actually active? | PASS |
| Is NO_HZ actually active? | PASS |
| Are real Reborn workload hints working? | PASS for all eight classes |
| Does SLIDLE enter? | FAIL; zero entries, MSDC0/MSDC1 remain blockers |
| Does automatic core parking work? | PARTIAL; goal not observed, eligible sustained window unproven |
| Are 1196/1300 MHz safely usable? | FAIL admission; physical use NOT_TESTED |
| Does voltage DVFS work? | PARTIAL selector recognition/readback; voltage changes NOT_TESTED |
| Does DORMANT work? | NOT_TESTED |
| Does CIRQ/GPT deadline handoff work? | NOT_TESTED for dormant/full resume |
| Does RTC deep-suspend wake work? | NOT_TESTED; awake RTC IRQ PASS only |
| Does Power deep wake work? | NOT_TESTED; staged recovery Power press ineffective |
| Does full same-boot restoration work? | NOT_TESTED; staged attempt FAIL |
| Is intelligent CPU scaling behaving as intended? | PARTIAL; performance/lease/thermal behavior passes, deeper idle does not |
| Suitable as the normal Y2 CPU platform? | FAIL |

The smallest remaining coherent correction batch is **power-state ownership, readiness and recoverability**, not another CPU architecture restart:
  - Prove early PM journal MMIO safety/readback and retained or backup diagnostics

before another suspend request; expose the first actual PM boundary and error. Re-test true charging refusal then freezer/staged entry before full wake. Do not infer a PCM/resume-vector root cause from an invalid journal.
  - Expose the three raw PWRAP readiness operands and actual ownership/slot

readbacks; reconcile the genuine board condition while retaining voltage and ownership guards. Then qualify high OPP ordering/feedback/fault containment.
  - Separate MMC system-sleep retention from balanced runtime clock gating, with

drained request/DMA and card/rail/storage safety preserved. Reassess coordinator sustained-quiet logic against measured background bursts; keep hysteresis and workload authority, do not force parking or delete clock blockers.
  - Instrument the loaded USB transport failure with durable IRQ/DMA/L1/controller

and host-carrier evidence plus automatic independent Wi-Fi capture before restart. Fix the identified transport cause while retaining proven quiescence and single-owner CONSYS isolation/retry.

Preserve the now-qualified timer/QoS/conservative audio/CPU paths. Produce one Fix02 only after these causes are concretely corrected; no patch, build or flash is part of this physical report. Existing #28/#30/#31/#32 gates remain open; this report does not close any external epic or authorize new scope.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
