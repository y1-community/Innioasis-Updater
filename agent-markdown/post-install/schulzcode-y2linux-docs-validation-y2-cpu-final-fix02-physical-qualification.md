---
title: "Y2 CPU Final Fix02 physical qualification — 2026-09-29 - Innioasis Updater"
description: "Y2 CPU Final Fix02 physical qualification — 2026-09-29 <!-- knowledge-base-scope: historical-validation-receipt; baseline02-sync 2026-10-03 -- Historical exact-image rece"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-cpu-final-fix02-physical-qualification.html"
---

# Y2 CPU Final Fix02 physical qualification — 2026-09-29 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 CPU Final Fix02 physical qualification — 2026-09-29

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 CPU Final Fix02 physical qualification — 2026-09-29

Historical exact-image receipt. This report retains its named Fix image and dated result. It does not describe Baseline02 or negate the newer bounded UART01 C1/C2/C3 passes. See [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) and [latest CPU-idle hardware proof](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md).

**Verdict: FAIL for acceptance as the normal Y2 CPU platform; the awake CPU platform is substantially qualified.** Timers, hotplug, QoS, thermal authority, MMC runtime clock gating, automatic core parking, PWRAP readiness and 1196/1300 MHz voltage DVFS pass on the device. The SRAM journal passes its awake self-test and warm-reboot retention, and every staged PM level passes on the same boot. Three defects remain: SLIDLE is refused by one bus-DCM register predicate, loaded USB upload still ends in a terminal IRQ storm, and full RTC deep suspend returns from SPM but resets 30 s later, after device resume and before `pm_suspend` exit. No implementation source was changed, nothing was built or flashed, no history was rewritten and nothing was pushed.

This supersedes the corresponding rows of the [Fix01 physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md). The [Fix02 receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX02.md) and [source ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX02-SOURCES.md) remain software provenance. PASS applies to the bounded observed behavior; PARTIAL is incomplete evidence; NOT_TESTED never means a hardware pass.

## Identity and evidence

Installed identity matched the candidate manifest before the first test and on every later boot:````````````````

| Field | Observed |
| --- | --- |
| Y2Linux runtime / Reborn runtime | 1a1a6693dcd82f62daecd4c1491ef512823a86c5 / 77cf83e09a18f82a867040e72d35b6e70b26fa85 |
| Kernel / rootfs | 6.18.0-y2linux-cpu-final-fix02 / 2025.02.18-platform-v1.8 |
| Release / build | 1.0.0-cpu-final-fix02-candidate.1 / Y2LINUX-CPU-FINAL-FIX02 |
| Host Linux / Reborn HEAD | 5437b8f86fbc (documentation continuation) / 77cf83e09a18 |
````````

| Boot | ID | Boundary |
| --- | --- | --- |
| 1 | d83cfbde-3c9d-45b8-9b87-3a4a81af4766 | identity, harness awake checks, first USB fault, self-test |
| 2 | cc90dc77-9e9c-44e6-ab72-b5b2e24652d3 | intended warm reboot (retention); regressions, MMC, SLIDLE, DVFS, matrix, staged PM, RTC attempt |
| 3 | c3ce3cfb-48ef-473a-88af-f0f83558aa15 | RGU backstop warm reset after RTC wake; retained capture, USB retest |
| 4 | 6bb70fad-29a7-4a8e-a1a1-b69884434127 | ordinary reboot over Wi-Fi to recover the terminal USB fault; final state |

Private evidence: `out/cpu-final-fix02-physical-qualification/20260929T152328Z/` (restricted). It holds the unchanged harness run (`harness/`), every supplementary remote program with stdout/stderr/exit/duration/UTC (`x-*/`), the reused harness `Run.suspend()` receipts (`suspend/`), device-side staged-run directories, raw measurement snapshots, SRAM records, USB fault snapshots, `qualification-summary.json` and `SHA256SUMS`. No keys, bond secrets, NVRAM or calibration were exported.

The harness ran unchanged as `qualify-cpu-fix02.py --run --host y2 --wifi-host y2-owner-wifi --allow-warm-reboot`. The Wi-Fi alias came from a session-local SSH config, as in Fix01. It uses the pinned device host key and a temporary key-only dropbear on `wlan0` started over USB. The listener was lost at each new boot and is gone at the end. The harness stops before suspend when any awake check fails. Its QoS and coordinator verdicts failed for harness reasons (below). Independent phases therefore continued through session-local scripts that reuse the harness helpers and its own `Run.suspend()` and `usb_stress()`.

## Timers, hotplug, QoS, thermal — PASS (regression gate)

GPT6 control `0x31` running; GPT4 `gpt4_sole_owner` broadcast (`y2-gpt4-broadcast`); admission `prepared_13mhz`, calibration 26000/26006/26000; CNTFRQ 13000000 on all CPUs, error 0; PPI29 `arch_timer` advances on all four CPUs; clocksource `arch_sys_counter`; all local events `arch_sys_timer`; `hrtimer_interrupt` and oneshot broadcast; hres 1 and nohz 1 per CPU with stopped ticks observed. 100 requested 1-ms sleeps: medians 1.09 ms on every CPU, p95 ≤ 1.133 ms. Nine individual CPU1–3 re-onlines plus 4→1→4 completed; taint 0. Identical on boots 3/4.

All eight workload classes were accepted with their floors (Idle/PlaybackNormal 0, PlaybackHeavy/Interactive/ArtworkDecode/LibraryScan 747.5 MHz, NetworkTransfer/Maintenance 598 MHz). Overlap, renewal, expiry and killed-child cleanup work. The cpufreq cooling device at max capped the policy at 598 MHz despite a live PlaybackHeavy lease (restored to 0). Real input: Back key → Interactive lease after 22 ms, lasting ≈274 ms; click-wheel likewise; screen-off drops Interactive immediately and wheel input while dark adds none. Real producers observed: PlaybackNormal, PlaybackHeavy, Interactive, LibraryScan, NetworkTransfer, Maintenance. C1 WFI usage/residency advances; rejected 0.

The harness QoS FAIL is a harness defect: it injects KEY_UP (103) into "Y2 navigation buttons", which Reborn maps only for 28/158/105/106/164.

## MMC runtime clock gating — PASS (storage), with one media-lifecycle defect

`y2_runtime_pm` for eMMC (`11230000.mmc`) and SD (`11240000.mmc`) reports `gated=1` at rest, suspends/resumes balanced, `retained` equal to resumes, `restored=0`, `last_mismatch=0x0` and `error=0`. The only refusals are `refused_request` (a pending request, the intended retry). DMA, controller, FIFO and interrupt refusals are all 0. CCF shows `y2-msdc0`/`y2-msdc1` gates with enable/prepare 0, hardware N. The harness 1-MiB eMMC and 64-KiB SD checks pass. A further 8 × 1 MiB eMMC and 8 × 512 KiB SD rounds each wrote, fsynced, dropped caches, observed the host re-gated, then read back. All 16 SHA-256 matches passed. ext4 error counters stayed 0, mounts stayed rw, and there were no MMC CRC/timeout/reset lines.

Defect (non-CPU, SD media lifecycle):`media.inventory()` identifies the SD by the kernfs inode number and ctime of `/sys/class/block/mmcblk1*`. Dropping caches evicts those kernfs inodes, and the recreated inodes compare as a changed inventory. The readiness loop then unmounted and remounted `/media/sd` twice during the test. One scratch file survived its `unlink` because the unlink ran against the momentarily empty mountpoint. Test-provoked here, but ordinary memory pressure reclaims kernfs inodes too. No data was damaged.

## SLIDLE — FAIL (single identified predicate)

With radios on, the clock-blocker mask while parked is `0x100800` (APDMA + BTIF, the CONSYS transport). That is legitimate while Wi-Fi/BT run. MSDC0/MSDC1 are no longer persistent blockers; they appear only transiently.

With radios runtime-off, screen off and no forced topology/frequency, the coordinator parked naturally. The clock mask read 0 for 200 s, yet entries stayed 0: every attempt then failed `slow_reject_bus` (0 → 20809). In `y2_ccf_slow_idle()` that is `readl(TOPCKGEN+4) != 0x0f`. `dormant_preflight` reads the same register as `bus=0x0` on this board. Stock `bus_dcm_enable` writes `0x8f` and its disable clears bit 7, with no inherited-value check. The Y2 predicate assumes an inherited `0x0f` that this boot chain never sets. This is the same class of mismatch as Fix01's PWRAP `0x1ff`/`0x7f`. Nothing was overridden. Attempts/entries 61924/0, restore failures 0, broken N.

## Automatic core parking — PASS; one attribution defect

Harness 240-s silent screen-off window: CPU3, CPU2, CPU1 powered off at 546.2/551.3/556.5 s (5-s pacing) after eligibility, `parked_mask=0xe`, online `0`, last reset none, load 161 mc, high-frequency 214‰. Display wake restored `0-3` in 0.63 s. The radios-off run and the 330-s measurement parked the same way and stayed parked. Manual offline/online during hotplug tests was never claimed. The harness coordinator FAIL comes from requiring C2 entries in the same verdict.

Defect: after a user wake the state shows `last_reset=burst reset_burst=1 pressure_restores=1 hold_ms=120000`. The wake's render burst is counted as a pressure restore, which doubles the parking hold (up to 960 s, reset after ten stable parked minutes). Frequent real wakes would delay parking.

## Screen-off CPU behavior — improved (CPU idle improvement, not battery)

| Screen-off idle | Fix01 (160 s) | Fix02 (330 s, parked) |
| --- | --- | --- |
| CPU, % of four cores | 9.74 | 2.71 (CPU0 10.98 % busy) |
| Cores online | 4 | 1 |
| OPP % 598/747.5/1040/1196/1300 | 73.71/1.05/25.24/–/– | 85.10/2.46/2.57/1.03/8.84 |
| C1 % of four cores | 89.64 | 21.96 (87.8 % of CPU0; CPU1–3 powered off) |
| C2 / C3 | 0 / 0 | 0 / 0 |
| IRQ/s | 391.49 | 171.43 |
| Context switches/s | 503.93 | 355.42 |
| Max CPU / PMIC °C | 51.8 / 51.561 | 50.2 / 48.052 |

Busy CPU time falls about 3.6×, IRQs 2.3×, context switches 1.4×. Measured in the same configuration (radios on, USB attached, charging). Harness attribution over 243 s: Reborn 8.19 s CPU, three long-lived platform Python daemons about 2.9 s each, y2-bt-reconnect 0.75 s. The harness `percent_of_one_core` field is 10× too large (harness defect). Dark bursts now reach 1300 MHz @ 1.25 V for 8.8 % of the time. No electrical power was measured.

## PWRAP / high OPP — PASS

`pwrap_readiness`: `mux=0x0 wrap_en=0x1 hiprio_arb_en=0x7f implemented=0x7f wacs2_en=0x1 init_done2=0x1 live=ready last=ready`, DVFS slots `0x21e:0x58/0x50/0x48`. Automatic admission `qualification_max_khz=1300000`, bin Y, `voltage_fault=N`. `admission_error=1` is `freq_qos_update_request()`'s positive "changed" return, i.e. success (cosmetic).

| OPP | Clock readback | Voltage readback | Selector |
| --- | --- | --- | --- |
| 598 / 747.5 / 1040 MHz | exact | 1.15 V | 0x48 |
| 1196 MHz | exact | 1.20 V | 0x50 |
| 1300 MHz | exact | 1.25 V | 0x58 |

Five cycles of 1040→1196→1300→1196→1040→598→1040 (30 steps) reached exact clock/voltage every step, `last_error=0 first_error=0`. There is no tracefs, so ordering was checked by a concurrent sampler on CPU3 (7796 frequency-then-voltage pairs). No UP-direction violation occurred. The four (high clock, lower voltage) pairs all fell 2 ms into DOWN steps, which is the read-order artifact expected from clock-before-voltage. The intermediate (1196 MHz, 1.25 V) was observed. Sampled evidence, not a hardware trace.

Four-worker SHA/zlib integrity: 1040 MHz 16647 iterations, 1196 MHz 18604, both with 0 errors (peak 71.5 °C at 1196). At 1300 MHz, four workers reached the 75 °C test guard in 16.8 s and were stopped. Two workers ran 5247 iterations with 0 errors (peak 64.5 °C). No voltage fault or fallback. The DT cpu-thermal trips are the BSP 110 °C passive / 120 °C critical, so the natural trip is NOT_TESTED under the new 1300-MHz ceiling. The cooling-device override passes.

## USB loaded transfer — FAIL, attributed

Wi-Fi observed before and after. Both runs (boots 1 and 3) lost USB in the first 1-MiB upload round: 0 of 10 successful. Classification is IRQ storm, `fault_reason=irq_overflow`, `rc=-75`, `irq_max_burst=513 > 512`. It is not a power-read transient, not reconnect timing and not a DMA bus error: `monitor_failures=0`, `reconnect_retries=0`, `dma_bus_errors=0×8`, `irq_unexplained=0`.

Fault snapshots: boot 1 L1 `0x182/0xf` (RX pending), `rx=2/1e`, EP1 RXCSR `0x0003` (RxPktRdy|FIFOFull, 512 B) with DMA channel 5 (`cntl=0x618`, EP1 RX) complete. Boot 3 L1 `0x108/0xf` (DMA pending), `DMA_INTR=0x20` (channel 5), EP1 RXCSR `0x2003` (DMAReqEnab + RxPktRdy + FIFOFull). Both are the host→device EP1 OUT bulk path under Inventra DMA. An RX completion/next-packet condition keeps re-asserting instead of being acknowledged and re-armed. The UI stayed alive and the transfer mode fell back to PIO. The fault is terminal by design and has no runtime recovery hook, so recovery was an ordinary reboot over Wi-Fi.

## SRAM diagnostics — PASS

Awake self-test: `result=pass`, sequences A=1/B=2, slot alternation, previous record preserved, reset stamp written and restored, ring verified, phys `0x10dc00` size `0x500`. One ordinary warm reboot: new boot ID, `previous_valid=1 previous_sequence=2 previous_stage=SELFTEST_B selftest_scratch=retained previous_ring=valid`. Retained records and the device callback ring were also valid after the RTC backstop reset (below).

## Charger and staged suspend — PASS

With USB attached the charger was `charging_active` (CONSTANT_CURRENT). A staged `devices` request produced `y2_charger_prepare_pm returns -16`, "not prepared for power transition", clean `suspend exit`, same boot, taint unchanged, no WARN, retained `failed_stage=DPM_PREPARED error=-16`, radios restored. The harness marked it FAIL only because the charger's prepare entry had scrolled out of the 24-entry ring. After the owner unplugged USB: `no_usb`, NO_SOURCE, no refusal.

| Stage (30-s RGU backstop armed) | Result |
| --- | --- |
| freezer (USB attached) | PASS, rc 0, same boot, taint 0, journal COMPLETE |
| devices | PASS |
| platform | PASS |
| processors | PASS, CPU3/2/1 SPM power-off result 0 and back up |
| core | PASS |

## Full RTC suspend — FAIL; exact boundary

Pre-flight: RTC wakeup enabled, PMIC EINT25 → RTC IRQ20 / keys IRQ5, SPM `SPM_CPU_SHUTDOWN_INFRA_RETAINED` not broken, backstop provider present. Alarm +30 s armed 16:18:37 UTC; `kernel_suspend` 16:18:44; RTC due ≈16:19:07. The device came back as a new boot; its kernel started ≈16:19:40, a reset ≈30 s after wake. This is the backstop period (`panic=0` would hang, not reboot). The reset cause register is not decoded (`not_observed`).

Retained previous record (valid, sequence 138): `reset_resume_entry=0x59325253` (the Y2 resume stamp, never observed in Fix01), SPM wake `0x20`, `cirq=0x3`, `boot_vector=0x8047ca20`, PCM `0x8495e000`/596, `wake_mask=0xfedfbfdb`, `rtc_enable=0x5`, last stage `DEVICES_RESUMING`, failed stage none, error 0. The callback ring (cycle 101 = this attempt) ends with balanced `phase=8` complete enter/leave pairs through the last device. **SPM entry, RTC wake, Boot-ROM resume vector, CPU context restore, syscore, secondaries and all device resume/complete callbacks happened.** The kernel then did not reach `Y2_PM_EXIT` within the 30-s backstop. Userspace never logged after resume and `y2-suspend` never wrote `RADIOS_RESTORING`.

The unmarked window is `resume_console` → `platform_resume_end` → `suspend_finish` (thaw, `PM_POST_SUSPEND` notifiers, console restore). No mark pings the backstop between `DEVICES_RESUMING` and `EXIT`. The exact stalled call inside that window is not established. The harness start step also misparsed `rtc-alarm`'s own JSON output and retried after the suspend had already launched (harness defect; no effect on the device path).

| Test | Status |
| --- | --- |
| RTC deep wake / same boot | FAIL: SPM return proven; backstop reset before PM exit |
| Power wake | NOT_TESTED: RTC full resume not established |
| Five RTC cycles | NOT_TESTED |
| Post-resume restoration | NOT_TESTED; boots 3/4 are clean boots, not resumes |
| Watchdog resets | one intended backstop reset (converted a stall into retained evidence) |

## C3 DORMANT — NOT_TESTED (not eligible)

`dormant_preflight`: `unmet=topology,frequency,domains,clocks,bus`. It needs one CPU, ≤747.5 MHz, domains `0xe0a` (CPUs, CONN, DISP) off, PERI blockers `0x21e8ffd` / INFRA `0xa0a0` clear, and `bus=0x0f`. The last shares SLIDLE's predicate. C3 stayed disabled (`disable=1`, `CPUIDLE_FLAG_OFF`); nothing was forced.

## Intelligent CPU workload matrix

Direct /proc and cpufreq/cpuidle deltas; CPU and C1 normalized to four-core capacity; OPP order 598/747.5/1040/1196/1300 MHz; voltage follows the OPP table per readback. Observer overhead is included. Per-core values are in `x-matrix/analysis.json`.

| Workload | CPU % | OPP % | Cores | C1/C2/C3 % | IRQ/s | Ctx/s | Max CPU/PMIC °C |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Screen-on idle (20 s) | 5.13 | 88.8/1.2/2.1/0.5/7.4 | 4 | 94.0/0/0 | 472 | 559 | 50.6/49.8 |
| Screen-off idle (330 s) | 2.71 | 85.1/2.5/2.6/1.0/8.8 | 1 | 22.0/0/0 | 171 | 355 | 50.2/48.1 |
| Interactive burst (15 s) | 5.61 | 0/94.3/1.5/0.7/3.5 | 4 | 92.7/0/0 | 603 | 759 | 51.2/50.4 |
| 44.1 kHz playback (25 s) | 10.53 | 89.0/0.6/1.3/0.8/8.3 | 4 | 88.6/0/0 | 744 | 906 | 51.4/49.2 |
| 24/96 → 48 kHz playback (25 s) | 11.20 | 89.3/0.7/1.4/0.6/8.1 | 4 | 87.5/0/0 | 720 | 873 | 52.5/49.8 |
| Heavy policy, crossfade 5000 ms (25 s) | 16.33 | 0/88.3/1.9/1.0/8.8 | 4 | 82.7/0/0 | 910 | 1012 | 53.6/52.7 |
| Scan 200 fixtures (20 s) | 5.95 | 86.2/1.6/1.3/0.6/10.3 | 4 | 93.3/0/0 | 511 | 719 | 53.2/50.4 |
| Wi-Fi 4 × 1 MiB each way (28 s) | 6.43 | 83.2/1.4/2.9/1.3/11.3 | 4 | 92.9/0/0 | 785 | 958 | 50.9/49.2 |
| USB transfer (45 s) | PARTIAL: transport lost in round 0; window mostly idle |  |  |  |  |  |  |
| 4-core load 1040 / 1196 (25 s) | ~100 | fixed | 4 | – | – | – | 64.6/58.6, 71.5/63.3 |

Playback ran with fixture silence; zero-XRUN/fidelity was not re-certified. Crossfade was set through the real UI and restored to 0. Playback leases keep all cores online by design.

## Cleanup and owner actions

Final boot `6bb70fad…`: identity unchanged, four CPUs, schedutil 598–1300 MHz, cooling 0, C3 disabled, crossfade 0, playback stopped, fixtures and scratch files removed, original three library tracks present. Wi-Fi associated, CONSYS calibrated with 0 errors, BT controller up, DSI connected, ALSA/GPU present, Reborn health `ok`, root/data/SD rw, ext4 errors 0, taint 0. The temporary Wi-Fi listener is gone. Device-side staged-run receipts remain in `/data/system/platform/fix02-*` and are copied to private evidence. Reborn's queue still lists the removed fixture entries.

Owner physical actions, exactly two:
  - Unplug USB (charging was active; required for devices+ stages).
  - Reconnect USB after the RTC backstop reset (Wi-Fi listener lost with the boot).

No Power press, shell command, log inspection or frequency selection was needed.

## Acceptance answers

| Question | Answer |
| --- | --- |
| Fix02 suitable as the normal Y2 CPU platform? | FAIL: deep suspend and loaded USB fail; awake CPU behavior is suitable |
| High stock OPPs usable? | PASS admission, readback, sampled ordering, integrity; natural thermal trip NOT_TESTED |
| SLIDLE materially works? | FAIL: 0 entries; one bus-DCM predicate after all clocks clear |
| Automatic parking works? | PASS 3→2→1, restore 0.63 s; wake attribution doubles hold |
| Deep suspend/resume works? | FAIL: SPM return proven; stall/reset after device resume |
| Power wake works? | NOT_TESTED |
| RTC wake works? | PARTIAL: RTC woke the SoC and resume vector ran; same-boot completion FAIL |
| USB reliable under loaded transfers? | FAIL: 0/10, EP1 RX DMA IRQ storm, reproducible |
| Intelligent CPU management behaving as designed? | PASS for leases, parking, low-OPP playback, 747.5 floors, scaling and thermal override; PARTIAL overall (no C2/C3; wake-hold attribution) |

## One coherent Fix03 correction batch

Scope: resume completion, bus-DCM baseline and EP1 RX DMA servicing. No CPU architecture change.
  - Resume completion. Mark and ping the backstop at every step from

`dpm_resume_end` to `Y2_PM_EXIT` (after resume, complete, `resume_console`, `platform_resume_end`, thaw and `PM_POST_SUSPEND`). Stamp ring entries with a monotonic ms value. Decode the RGU reset status into `boot.json`. Then take one RTC attempt to name the stalled call and fix that call only.
  - Bus DCM. Establish the source-backed baseline of TOPCKGEN+4 (Y2 reads

`0x0`, stock clears only bit 7 on exit). Reconcile the SLIDLE and deep-idle predicates with it, as PWRAP was reconciled, keeping the verified write and exact restore.
  - USB EP1 OUT. Align RX DMA completion, DMA_INTR acknowledgement and

RxPktRdy/DMAReqEnab re-arm for channel 5 with the MT6582/Inventra reference, using the two captured snapshots. Keep the storm guard terminal.
  - Coordinator and media. Exclude display/workload restores from

pressure-hold escalation. Key SD inventory on stable identity (device number/CID), not kernfs inode/ctime.

Harness corrections, which do not affect the device: navigation key code, separate parking and C2 verdicts, a warm reboot over the Wi-Fi fallback, the attribution scale, charger refusal checked from `failed_stage`/dmesg, `rtc-alarm` output captured, and no retry after a launch.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
