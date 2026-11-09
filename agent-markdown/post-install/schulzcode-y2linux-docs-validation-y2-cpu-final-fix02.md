---
title: "CPU Final Fix 02 implementation and candidate receipt - Innioasis Updater"
description: "CPU Final Fix 02 implementation and candidate receipt <!-- knowledge-base-scope: historical-validation-receipt; baseline02-sync 2026-10-03 -- Historical exact-image recei"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-cpu-final-fix02.html"
---

# CPU Final Fix 02 implementation and candidate receipt - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# CPU Final Fix 02 implementation and candidate receipt

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# CPU Final Fix 02 implementation and candidate receipt

Historical exact-image receipt. This report retains its named Fix image and dated result. It does not describe Baseline02 or negate the newer bounded UART01 C1/C2/C3 passes. See [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) and [latest CPU-idle hardware proof](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md).

Owner-authorized correction of the remaining real-device failures recorded by the [Fix01 physical qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md). This pass changes software, produces one preserving candidate and does not access or flash a Y2. It does not restart the CPU architecture: GPT6/GPT4/PPI29, CNTFRQ, highres/NO_HZ, hotplug, 598/747.5/1040 MHz, schedutil, the eight workload classes, interactive boost/expiry, thermal authority, WFI, bounded playback and CONSYS isolated retry are unchanged and kept as regression requirements. Software tests are not physical passes. Research provenance is in the [Fix02 source ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX02-SOURCES.md); the next run is prepared in [Fix02 physical qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX02-PHYSICAL-QUALIFICATION.md).

Starting Linux `0b8f810926c09510773eb76d1bf967a136b00f08`; starting Reborn `6ddc553dd69a0158c9121df959ef135c50814a13`. Both trees were clean.

## 1. MSDC runtime clock ownership (SLIDLE blocker 0x3000)

Root cause. Patch `0009-y2-msdc-readonly.patch` returned early from `msdc_runtime_suspend()`/`msdc_runtime_resume()` for every Y2 host under `CONFIG_Y2_POWER`. The comment described s2idle retention, but these are the ordinary runtime callbacks, so a host that runtime PM reported as `suspended` never released `hclk`/`source_cg` (the same PERI MSDC0/MSDC1 CG, bits 12/13). That is exactly the physically observed state: runtime suspended, enable count 2, blocker mask `0x3000` with radios off.

The bypass also hid a second problem: upstream `msdc_save_reg/restore_reg` touch `PATCH_BIT2` (0xb8), `PAD_DS/CMD_TUNE` (0x188/0x18c), `EMMC50_CFG0/3` and `SDC_FIFO_CFG`, none of which exist in the pinned MT6582 `mt_sd.h` register map.

Correction. Runtime PM and system sleep share one Y2 owner (`y2_msdc_runtime_suspend/resume`). Suspend refuses (`-EBUSY`, runtime core retries at the next autosuspend expiry) for a pending request, `DMA_CFG` busy, `SDC_STS` SDC/CMD busy, FIFO RX/TX data, or an unserviced enabled interrupt. When idle it saves the MT6582-defined image (CFG, IOCON, INTEN, SDC_CFG, PATCH_BIT0/1, PAD_CTL0..2, PAD_TUNE, DAT_RDDLY0/1), selects `MSDC_CFG` MS mode and releases the PERI CG, the exact stock `msdc_clksrc_onoff` order. Resume ungates, waits 10 µs, verifies every retained register, restores and re-verifies any lost one, rewrites SD/MMC mode with the saved divider (never replaying RST) and waits for CKSTB. A failure leaves the clock enabled and reports; it never re-gates a live host. No card command, reset, rail, pinctrl or re-initialization is issued; `0029` still retains card power and addressing across system sleep (no CMD5/poweroff notify/reinit). Since the host is almost always runtime-gated when system sleep starts, "system sleep retention" is card and register-image retention, not an ungated controller. Card detect on Y2 is `broken-cd` polling with no internal CD register access, so no register is read while gated.

`y2_runtime_pm` exposes gated/suspends/resumes/retained/restored/last mismatch, error and refusals by reason; it never touches a gated controller.

## 2. Automatic parking and SLIDLE reachability

Root causes (source attribution of the recurring bursts).``````````

| Source | Class | Evidence / change |
| --- | --- | --- |
| Readiness service started a full Python interpreter (y2-platform media reconcile) every 3 s, plus space --cleanup and update health-ack every 30 s | Avoidable periodic work | Start-up of CPython on a Cortex-A7 is exactly the quarter-second, ≤31 %, 1040-MHz (iowait/util) burst pattern. Reconcile is now started only when its own no-op condition is false (SD inventory changed or retry pending, checked in-process from sysfs). While dark the loop runs every 10 s (Reborn's network.json limit is 15 s) and maintenance every 300 s once update health is settled (30 s while pending, so the 180-s health deadline is unaffected). |
| Coordinator reset its window on any single 250-ms sample >10 % and on every cpufreq PRECHANGE >598 MHz | Wrong policy (harmless transients treated as demand) | Replaced by sustained measurement, below. |
| Coordinator's own 250-ms timer | Observer overhead | Now deferrable: an idle CPU is not woken to observe idleness. |
| Reborn main loop: 15-ms wake while the screen is off (~66/s) | Avoidable wake-ups | 50 ms while the screen is off; input still wakes promptly; audio/decode/control run on their own threads. |
| SD broken-cd polling (1 Hz CMD13), power daemon 1-Hz battery sample, Reborn 1-s playback lease renewal, 2-s supply read, Wi-Fi 3-s status, AVRCP 3-s refresh | Legitimate | Kept. Each is short; MSDC1 now re-gates 50 ms after each poll. |
| Test observer SSH/sampling | Observer overhead | The Fix02 harness is silent during its 240-s window and attributes CPU per process between two samples. |

Coordinator.`system-idle-policy.h` measures a time-weighted busy average in milli-cores (τ 30 s, park only at ≤400 = 10 % of four cores) and the time fraction above 598 MHz (≤25 %). Short bursts and single 1040-MHz raises now only move the averages. One second of per-core saturation (≥85 %) is real demand. Screen, workload lease, timer admission, disable and explicit input/display/workload demand still reset immediately. Parking remains one CPU per 5 s, CPU3→CPU2→CPU1, after the 60-s restore hold and a 30-s quiet window; workload and display restores stay synchronous before acknowledgement; manual offlines are never claimed. A pressure restore soon after parking doubles the hold (60→960 s cap); ten stable parked minutes return it to 60 s, bounding oscillation. Frequency raises are counted, not treated as demand. The `state` parameter reports averages, quiet/longest window, hold and every reset by reason.

SLIDLE refusals are attributed separately (topology, lock, clock blocker, bus state) with per-bit blocker counts and the last mask read with one CPU online, so "mask 0 with four CPUs" can no longer be mistaken for idle clocks.

C3. Unchanged and still experimental/default off (`CPUIDLE_FLAG_OFF`). `dormant_preflight` now evaluates, read-only and in entry order, the same topology, frequency, timer, CIRQ, SPM domain and PERI/INFRA/bus clock prerequisites and lists every unmet one.

## 3. High OPP / PWRAP readiness

Actual register interpretation. The Fix01 predicate required `MUX_SEL(+0x00)=0`, `WRAP_EN(+0x04)=1` and `HIPRIO_ARB_EN(+0x50)=0x1ff`. The retained Y2 preloader `pwrap_init` does write 0x1ff (Thumb `movw r1,#0x1ff; str r1,[r5]`at file offset 0xc954,`r5` loaded from literal 0x1000d050). The pinned MT6582 BSP defines only seven arbiter channels (MDINF bit0, WACS0..2 bits1..3, DVFSINF bit4, STAUPD bit5, GPSINF bit6); bits 7/8 are not implemented and read back as zero. The M2-PWRAP-01 physical screen photographed exactly `MUX:0 WRAP:1 WACS:1 INIT:1 ARB:0000007F` on this board. The predicate therefore compared a readback with the written value and could never pass: it was a wrong register interpretation, not a different initialization stage or missing stock state (the stock kernel never writes HIPRIO_ARB_EN).

Correction.`pwrap-readiness-policy.h` requires wrapper mux, enabled wrapper, no readback bits outside the implemented 7-bit field, DVFSINF and WACS2 enabled, and the complete preloader field (0x7f); each refusal has a name. It gates admission and is rechecked before every SPM voltage request (a change after admission is `-EIO`/fault). `pwrap_readiness` exposes live and last-admission MUX/WRAP/ARB, WACS2 enable/init/rdata and all eight DVFS slots, read-only (no WACS2 FSM or PMIC access). Bin validation, active-bank detection, NI feedback, voltage-before-frequency increases, frequency-before-voltage decreases, settle/readback, rollback, 1040-MHz fallback and thermal authority are unchanged. High OPP support is software-ready: on this board state the existing automatic admission can now reach 1196 MHz @ 1.20 V and 1300 MHz @ 1.25 V; physical voltage-changing DVFS remains NOT_TESTED until the next run.

## 4. Suspend diagnostics and recoverability

Diagnostic failure root cause. After the Fix01 staged request, both SRAM slots were invalid (valid=0, sequence=0). That outcome is equally explained by a journal that never wrote, by the owner's restart being a PMIC power cycle (which cannot retain SRAM), or by loader overwrite; the durable file ended at the coarse userspace `kernel_suspend`. Nothing had ever proven the SRAM path awake, and recovery required the owner because a hang had no warm-reset path.

SRAM journal design. Unchanged slots A/B (0x0010dc00/0x0010dc80, magic written last, checksum, wrapping sequence) and Boot-ROM stamp (0x0010dd00). The claimed window grows to 0x0010dc00..0x0010e0ff, inside the stock RAM-console allocation (proven by `mt_map_io`/`ram_console_early_init`). A scan of the retained FM preloader and LK finds references only to 0x0010f000.. and the preloader's RAM-console guard (which mutates only on magic 0x43474244); 0x0010dc00..0x0010e0ff is referenced by neither. New content: a self-test scratch area and a 24-entry device-callback ring (sequence written last).

Awake validation (`/sys/firmware/y2_pm/selftest`, write `run`): serialized with system sleep; marks SELFTEST_A and SELFTEST_B and reads every word back through a second, independent `ioremap` of the same physical SRAM; checks checksum, sequence +1, slot alternation and that the previous record survives; writes and restores the reset stamp; verifies the ring; writes a sequence-derived scratch pattern; refuses a RAM-console magic in slot 0. The next boot reports (`retention`) whether SELFTEST_B and the scratch pattern survived: one ordinary warm reboot proves electrical retention without entering suspend. The harness only reboots with `--allow-warm-reboot`.

Earlier breadcrumbs. HELPER_REQUEST (helper, before radio quiesce), SUSPEND_REQUEST, FILESYSTEM_SYNCED, TASKS_FROZEN, PLATFORM_BEGIN, DPM_PREPARE_BEGIN, DPM_PREPARED, DEVICES_SUSPENDED, LATE_SUSPENDED, NOIRQ_SUSPENDED, SECONDARIES_DISABLING/OFF, SYSCORE_SUSPENDED, PLATFORM_ENTER, then the existing CIRQ/PCM/context/SPM entry/return/restore marks, TEST_RETURN and EXIT. The first failing stage and error are kept.

Device-callback trace.`dpm_run_callback`, prepare and complete record enter/leave, phase and result with the device name (tail-preserving, 20 bytes) in the ring for every device (charger, MUSB, MMC, CONSYS, BT, DRM, GPU, AFE/ CS43131, RTC, input included). Raw MMIO word stores only; no logging in noirq. `devices` and `devices_previous` show this and the previous boot's trail.

Recoverable staged tests. An owner-armed one-shot backstop (`backstop_s`, 10..30 s) starts the RGU watchdog at `pm_suspend` entry, is pinged on stage progress and stopped at exit. Staged pm_test runs are covered through every phase; a full sleep pauses it only around SPM entry and restarts it after return. Expiry uses the same RGU reset path as Linux `reboot`, so a stall becomes a warm reset that keeps the journal instead of a hang needing an owner power cycle. It is refused while userspace owns `/dev/watchdog` and is invisible to the watchdog core (upstream suspend/resume never touch it).

Charger. The kernel already refuses only while the charger engine is active (or failed to stop); USB-online HOLD/"Not charging" legitimately proceeds. `charger_state.classify` separates USB present, charging active, charger hold and not charging; refusal is expected (and verified from the retained prepare result `-16` on the charger device) only when active.

SPM/wake. RTC, Power key/PMIC EINT25, CIRQ, wake mask, CPU0 vector and context restoration were re-reviewed and are unchanged: no new evidence shows a defect, and the failed staged request never reached SPM. The next failure will now name the first boundary.

## 5. USB loaded-transfer failure

Findings. Every `y2_usb_fail()` was terminal until reboot and none recorded which of nine sites fired. Two are not transport faults: a single failed PMIC/PWRAP sample in the 250-ms supply monitor, and any write-free reconnect preflight refusal right after a VBUS/CHRDET dip (plausible with charging plus 1040-MHz load) tore USB down permanently while the UI stayed usable — matching the Fix01 observation. A DMA bus error or IRQ storm is also terminal by design. Because the observer died with USB, the actual site is not established.

Correction. The monitor needs one second of consecutive failed samples; a write-free reconnect refusal is retried for ten seconds while the cable is present. Refusals after a session write, DMA bus errors and IRQ storms remain terminal (no stale interrupt loop). The first terminal fault freezes its reason and a read-only snapshot (L1/USB/TX/RX status+masks, POWER, DEVCTL, FADDR, per-endpoint CSR/RXCOUNT with INDEX restored, DMA INTR and all eight channel control/address/count) for the independent Wi-Fi observer, and notes the reason in the retained ring. Counters add peak per-jiffy IRQ burst, unexplained IRQs, per-channel bus errors, tolerance retries and runtime-PM state. Inventra DMA (not disabled), `y2.usb_dma=off`/allocation PIO fallback and the USB SSH recovery architecture are unchanged. If a DMA bus error is captured next run, its snapshot identifies channel, endpoint and address for a targeted fix; the stock MT6582 DMA IRQ path matches upstream's spurious-IRQ recovery, so no divergence was imported blindly.

## Tests added

`tests/test_cpu_fix02.py` executes the real driver functions on host models: MSDC busy reasons/gate/retain/restore/failure unwind and root/SD safety invariants; PWRAP operands, admission, feedback mismatch, failed SPM request, fault latch, wrapper change after admission, slot tampering and transition ordering/rollback/thermal cap; coordinator parking order under the measured background, lease/display/demand restore, hysteresis, pressure escalation bound and sustained-load refusal; screen-off background gating; journal self-test success and injected failures, stage progression, torn ring entries, backstop lifecycle; USB tolerance and attribution; charger classification; harness evaluation helpers and plan safety. Existing Fix01, slow-idle, USB-failure and USB-reconnect fixtures were updated to the new contracts.

## Final software receipt

| Identity | Commit/version |
| --- | --- |
| Starting Linux / Reborn | 0b8f810926c09510773eb76d1bf967a136b00f08 / 6ddc553dd69a0158c9121df959ef135c50814a13 |
| Built Linux runtime | 1a1a6693dcd82f62daecd4c1491ef512823a86c5 |
| Built Reborn | 77cf83e09a18f82a867040e72d35b6e70b26fa85 |
| Kernel / root | 6.18.0-y2linux-cpu-final-fix02 / 2025.02.18-platform-v1.8 |
| Release / build | 1.0.0-cpu-final-fix02-candidate.1 / Y2LINUX-CPU-FINAL-FIX02 |

A later documentation commit seals this receipt; it changes no built kernel or userspace (recorded in the candidate's `sources/campaign-docs-commit.txt`). Git identity/configuration and the authenticated account are unchanged; no model attribution; no push.

| Fresh check (isolated checkouts at the built commits) | Result |
| --- | --- |
| Kernel/config/modules, production DT, BOOTIMG/memory bounds (artifact validation) | PASS; BOOTIMG 7196672 bytes |
| Targeted ARM W=1 of every changed object (pm-journal, usb, spm, clocks, system-idle, pwrap, mtk-sd, mtk_wdt, PM core, suspend) | PASS, no warnings |
| Production/platform/CPU regressions (incl. test_cpu_fix02) | 241 tests: 238 PASS, 3 explicit native-dependency skips |
| Native dependency tests on the packaging host | 12 PASS, no skips |
| Reborn workspace | 193 PASS; cargo fmt and strict Clippy all-targets -D warnings PASS |
| Buildroot ARM, Reborn ARM and QEMU | PASS |
| Installed ARM (Python modules, SQLite/OpenSSL, Reborn, ALSA) | PASS, 26 modules |
| ELF dependency closure | 382 ARM ELF files / 1396 edges PASS; no build RPATH |
| FFmpeg/ALSA | fresh FFmpeg feature contract and ALSA constraints PASS |
| Locked source/release inventory, legal-info | 105 packages hash-verified; legal-info collected with existing recipe-metadata limits |
| Recovery options and automatic-admission fault containment | PASS |
| Preserving package / fallback | PASS clean ext4 and on-image identity, BOOTIMG/Y2ROOT only, no Y2DATA payload, exact Hardware02 fallback |
| Qualification harness offline | plan-only default, --wifi-host required, evaluation helpers PASS |
| Documentation links/catalog | 0 problems |

Host-only modules needing `elftools` and a stale local GPU artifact were compared against the starting commit; they are environment-only and pass in the isolated production run.

Candidate: /home/luca/Dokumente/Code/Y2Linux/out/y2linux-cpu-final-fix02-candidate/

| Payload | SHA256 |
| --- | --- |
| BOOTIMG.img | a621e270038356056ec21cb332a6592a18373e075e4df8a1f32beaca3b8fdd5e |
| Y2ROOT.img | 5010d839766f52ebce9934f07ee6e4189c3318eacc460021f156a92b9ea27835 |
| fallback/BOOTIMG.img | b2a2c3bcb7cc7783828882e447e8b867453cb5b65846ce63577076b1ca4afeea |
| fallback/Y2ROOT.img | 63dbd0a198cd86e847c10ed163fd14b2cbe269595fa1988c99ac8393160bb547 |

Fallback is the accepted Hardware02 pair (Linux 76bc8229, Reborn 95747e0a, kernel 6.18.0-y2linux-hardware-02, root 2025.02.18-platform-v1.4), identical to the Fix01 fallback. No preloader/LK/NVRAM/PROTECT/calibration/factory/data payload. No device access, flash or push occurred.

Owner next action: verify SHA256SUMS, install only BOOTIMG and ANDROID/Y2ROOT with `MT6582_preserve_data_scatter.txt` through the existing preserving workflow, then run `python3 tools/development/qualify-cpu-fix02.py --run --host y2 --wifi-host OWNER_WIFI_ALIAS` (optionally `--allow-warm-reboot`).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
