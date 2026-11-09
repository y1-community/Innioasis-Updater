---
title: "Hardware Final implementation-first continuation, 2026-09-27 - Innioasis Updater"
description: "Hardware Final implementation-first continuation, 2026-09-27 <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-hardware-final-handoff.html"
---

# Hardware Final implementation-first continuation, 2026-09-27 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Hardware Final implementation-first continuation, 2026-09-27

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Hardware Final implementation-first continuation, 2026-09-27 > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

The owner resumed Astra's `022e6ee` handoff with implementation before physical qualification. This continuation overrides the paused/measurement-first next steps below; Astra's completed evidence, failed experiments and source index are preserved verbatim as historical context. No full audit or new device session.

Current local branches contain SOC/low-battery/UI, UUID-less SD, automatic SDR fallback, schedutil/workload leases, guarded USB host/classes/NCM, slow idle, source-backed charger ceiling, Wi-Fi power policy/coexistence, experimental codec selection, native S16 48/family fallback, RTC alarm/sync and independent capability/configuration contracts. The volume and other Astra fixes remain.

One preserving candidate is built and software validated from Linux `067003f8988042a832181e935128ea93e26070a7` and Reborn `5b5d23b89952d88faf3155cf680ccce918f1b099`. Kernel `6.18.0-y2linux-hardware-final`; root `2025.02.18-platform-v1.5`. Exact images/configuration/source pair are bound by `out/y2linux-hardware-final-candidate/manifest.json`. No flash or push. Original Hardware02 remains the physical baseline. User docs and UI assets remain preserved outside the candidate checkout; preexisting Rust formatting was reproduced independently from committed source for strict fmt.

Read [implementation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-HARDWARE-FINAL.md), [truthful capability/default/fallback ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-HARDWARE-FINAL-CAPABILITIES.md) and [one later qualification campaign](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-HARDWARE-FINAL-QUALIFICATION.md). Native S32/88.2/96, runtime CPU power-down, NCM activation and successful deep suspend remain explicit technical gaps. Missing current/pack temperature stays unavailable. Software presence is never inferred from a qualification label.

## Completed software validation, 2026-09-27

Built pair: Linux `067003f8988042a832181e935128ea93e26070a7` / Reborn `5b5d23b89952d88faf3155cf680ccce918f1b099`. Kernel/config/DT and BOOTIMG memory/partition limits pass without extending any reservation. Buildroot ARM and Reborn ARM, 202 production tests, 189 Reborn workspace tests, fmt/strict Clippy, QEMU application/FFmpeg/ABI checks, installed ARM platform/SQLite/ALSA checks, and 382 ELF files / 1396 dependency edges pass. Signed update/preserving package and exact Hardware02 BOOTIMG/Y2ROOT fallback validation pass. Source inventory covers 105 selected packages and their pinned hashes.

Package includes source bundles, locked kernel/Buildroot archives, Buildroot source/license collection and qualification tools. Legal collection warnings for external-toolchain/local-package recipe metadata are retained, with local source and GPL text supplied separately. Optional codec certification/public distribution remains unapproved; this is a local owner package. Byte-identical rebuilds are not claimed. No device access, flash, push or physical/endurance qualification occurred.

The source pair above is the actual built pair. A later documentation-only commit records these results and is archived separately; it does not change firmware provenance. The engineering campaign remains open for the structured later phase.

## Astra handoff at 022e6ee (preserved)

# Hardware Final handoff — 2026-09-27

**PAUSED at the owner's request to reduce token use and continue with another model. Not complete. No final candidate was built, no flash occurred, nothing was pushed.** Resume from this file rather than repeating the initial audit. The owner subsequently confirmed: “the fix works tho” for the volume-key fix.

## Repositories and preserved work

Both repositories are on `hardware-final`, in their original directories: `/home/luca/Dokumente/Code/Y2Linux` and adjacent `Y2Reborn`. Implementation heads before this documentation commit: Linux `4a35658`, Reborn `47c545fea16dd347dd5c0feaf5a498de4312c04d`.

Pre-existing Linux modifications remain unstaged in roadmap-gap-audit.md, platform-v1-roadmap.md, PLATFORM-V1-PHYSICAL-QUALIFICATION.md and PLATFORM-V1-TELEMETRY-01.md. Do not commit or erase them accidentally. Their original patch is `out/hardware-final/preexisting-linux.patch`. Reborn's pre-existing asset pack deletions and untracked replacement pack/audit/docs remain untouched; `out/hardware-final/preexisting-reborn-status.txt` records them. No identity config was changed. Reborn lacks local identity config; commits used environment values from Y2Linux's existing configured Luca identity, matching prior Reborn history.

## Device at handoff

Original Hardware 02 restored and healthy, receipt21 plus final cleanup:
  - Linux `76bc8229580ec8d101008c5bad47419f2c110eae`, Reborn

`95747e0a36c7b27beb44b8cdd54feda1813f2f3a`, candidate.4.
  - Same boot `b93cda16-4e08-4ead-a74a-c85f4cccaa11`; taint0, CPUs0–3,

pm_test none, root/data/SD ext4 error counters0, quick health OK.
  - Both MMC qualification caps restored to25MHz; actual24,999,971Hz,

eMMC8-bit MMC high-speed and SD4-bit SD high-speed,3.3V.
  - Original `/usr/bin/reborn` SHA256

`8027f751c543b8548e6b6832994d7c0724a6276b068242f24a93beeae3f17938`. Temporary bind mount removed; original app restarted, stopped playback. The installed app therefore does not retain the volume repair after handoff.
  - Original BlueALSA daemon/supervisors restored after AAC experiment. No stopped

supervisor, temporary daemon, benchmark or campaign observer remains running.
  - Temporary `/run/y2-final-app`, `/run/y2-final-codecs` and generated listening

fixture under `/data/music/Y2-Hardware-Final-Qualification` removed. Library rescanned. No existing music deleted; ordinary test/library history persists.
  - Intentional persistent change retained: `/data/system/platform/rtc-policy.json`

enables existing NTP→RTC synchronization, grounded in successful receipt05 and earlier receipts50–52. No RTC retention/alarm claim.

USB SSH: pinned existing host key, `root@10.42.0.1`, owner identity file `/home/luca/.ssh/y2linux_ed25519`. Never print key bytes or bypass host checking. Owner has AirPods Pro2 and wired headphones, no USB meter. Wired listening was offered but not started before the stop request. No reboot/suspend/module load occurred in this campaign segment.

## Physical evidence and limits

Raw/private directory: `out/hardware-final/20260927T122702Z-hardware02/`. `out/hardware-final/active-run` points there; capture.py records command/stdout/ stderr/host UTC/exit status. SHA256SUMS seals completed receipts. Raw logs contain identifiers/private network information; do not publish them wholesale.
  - `00`,`01`: exact identity, broad census, CID/CSD, MMC error stats, power/IIO,

timer_list, interfaces/services. EXT_CSD still needs confirming through debugfs.
  - `02`,`03`: eMMC and SD13/25/50MHz cap sweep, guarded direct sequential/random

readback plus buffered/fsync/fdatasync/directory/metadata/SQLite workloads pass. Actual13MHz cap is about12.5MHz with this inherited clock source; report actual separately. First50MHz large-block eMMC read/write33.08/26.44MB/s; SD19.19/17.95.
  - `17`: three additional complete direct-readback repeats at50MHz per medium pass.

Some overlapped product audio testing: stable-load evidence, not isolated maxima. No source default-speed promotion yet; source and device default remain25MHz.
  - `18`: 1k and10k library+scan pass (5.90s/62.67s). **20k intentionally terminated

for handoff; workload FAILED/command_failed despite outer capture rc0.** The clock was restored to25MHz during its unfinished run; never certify it as a 50MHz result. `22` records termination. Rerun matched isolated library cases.
  - `06`: USB TCP RX38.35–38.79Mb/s with704–713 retransmits, TX46.31–46.57Mb/s

with0. DMA IRQ count stays6 despite large transfers: ECM actually falls back to PIO. Wi-Fi with AAC gives18.98–24.07Mb/s into Y2 and31.89–33.47Mb/s out. These are coexistence samples, not unloaded Wi-Fi ceiling or endurance.
  - `07`: idle app voluntary context switches/s: control98,audio99,Bluetooth51,

main65. Fixes below await post-fix idle A/B; no measured power-saving claim.
  - `05`: checked NTP then RTC write/read/tick pass. Prior RTC date was2022.
  - `08`–`11`: AirPods SBC stereoS16/44.1; owner clean both ears and working stem

Play/Pause. Private D-Bus trace captures actual MPRIS Play/Pause from BlueZ; metadata changes present. Next/Previous not qualified. Initial resume failed because the old selected track path was unavailable; dedicated fixture fixed the test setup, not a source change.
  - `12`: 100 one-millisecond sleeps/core, medians1.10–1.113ms;340.48s continuity

across low-counter rollover, raw/monotonic difference about1ppm; RTC340s. All four highres/nohz flags and idle_sleeps observed. Not external long drift.
  - `15`: temporary ARM FDK-AAC/BlueALSA5 bundle negotiates AAC,S16 stereo48k;

owner “clean no problems”, short playback/coexistence, no recorded XRUN or decode error. Volume presses still restarted old app during this experiment. Original daemon restored automatically. Not optional-codec endurance acceptance.
  - `16`:4→3→2→1→2→3→4 cores with per-core checked hash loads/idle and clockevents

pass; same boot, SPM broken0, taint0 and clean filesystems. No automatic policy.
  - `19`,`20d`: temporary fixed ARM Reborn. Automated20/0/30/10/25 volume changes

preserve playing state, generation2 and start count; owner confirms keys work. `20` failed only on diagnostic build label “development”; `20b` hit a transient not-yet-ready A2DP peer; `20c` reconnect and `20d` pass. Preserve failed attempts.
  - `04`: passive voltage/die-temperature trace under labelled workloads. Intentionally

stopped rc143 for handoff. Peak observed CPU67.5°C/PMIC~60.3°C; no pack temperature or net battery current inference. Start future stress cool with bounded stops.

## Committed implementation

Linux:
  - `e91fb1e`: power daemon deadline-based waiting replaces4Hz polling.
  - `bd48c13`: DMA allocation/programming/abort/failure counters (programmed bytes

explicitly not delivered bytes).
  - `7db74bc`: pinned private FDK-AAC2.0.3, libfreeaptx0.2.2 and LDAC2.0.2.3+ABR;

manifests/provenance/license limits. Default daemon keeps SBC, disables optional endpoints. `8e7799e` validates policy without invalidating historical fallback.
  - `dc9f22e`: truthful Wi-Fi control failure/latency telemetry.
  - `d46feaa`: real DMA alignment fix: standard RX no_skb_reserve quirk; conditional

aligned TX skb copy preserving metadata, allocation failure→existing PIO. Exact ARM checksum assembly tested for2mod4 headers under QEMU. Hardware pending.
  - `9bd1681`: exact-bin, sole-owner PWRAP/SPM/CCF DVFS; stock1196MHz/1.20V and

1300MHz/1.25V opt-in, default1040MHz QoS cap. No new generic PMIC write permission. `4a35658`: keep safe MAINPLL/2 fallback if ARMPLL mux restoration fails.
  - `45c7d42`,`78cf96a`: detailed power/idle evidence and exact gates.

Reborn:
  - `5d4ce0e`: block idle control listener instead of100Hz polling.
  - `f76f117`: idle audio waits for commands, preserving immediate command wake.
  - `1e93600`: observation failures no longer counted as Wi-Fi disconnect/reconnect.
  - `47c545f`: live volume after decoder DSP,5ms ramp, no reopen; partial-write,

mute→raise, queued PCM, signed formats, unity and exact frame-count tests.

Diagnostic ARM app SHA256 `d1bd0b55f4a733a19f5705f8461dcb6c9db4b713828394f84f1286b104f80e9a`, at `Y2Reborn/target/armv7-unknown-linux-gnueabihf/release/reborn`. It advertises “development”, built from the shared worktree with Hardware02 SDK; **not a final commit-certified release artifact**. Codec bundle and build logs: `out/hardware-final-codec-research/target-codec-bundle.tar.gz`.

## Validation completed and critical next work

Targeted Linux/USB/codec/network tests pass;22 relevant tests in final radio/USB run,9 Wi-Fi Rust tests,33 Reborn application tests, affected strict clippy and ARM application/codec builds. DVFS objects+DT compiled before the last mux fix; last fix host-tested only. Complete current-source kernel/DT/platform/Reborn workspace/fmt/strictclippy/ARM/Buildroot/QEMU/installed-ARM/FFmpeg/ALSA/package/ ELF/source/license/preserve-data/fallback boundary is NOT DONE.
  - Finish independent DVFS review before packaging. Reviewer found mux/divider

failure fixed in4a35658 but has not independently rechecked it. Check provenance in `out/hardware-final-power-source/`, voltage-readback mismatch containment, sleep/resume and all fault paths. In particular, current tests assume a failed voltage decrease retains old safe voltage; unexpected lower readback requires explicit assessment. Runtime path `/sys/module/cpu_dvfs/parameters/qualification_max_khz`; never raise installed Hardware02 voltage or claim new OPP physical acceptance.
  - Get persistent one-stage pm_test and Hardware02 first-overflow snapshot;

distinguish USB IRQ overflow from radio restoration timeout. No current suspend fix or successful same-boot deep/RTC wake. Only advance after verified recovery.
  - Wired48 product/screen-off/rate switches and live volume: runtime

`/etc/y2linux/audio-qualified.json` is reread per ALSA probe, allowing a temporary S16[44100,48000] profile without flashing. Restore after test; promote metadata only after evidence. No S24/S32/88.2/96 packing authorization.
  - Finish isolated storage/library/SFTP/USB/idle/frequency/load and recovery work.

New DMA alignment must be measured on final kernel; do not falsely compare old Hardware02 DMA label to true DMA. Keep exact Hardware02 fallback.
  - Optional codecs are compiled but normal endpoints disabled; UI preferences

only Auto/SBC. Auto still requires distribution/physical gates. Decide a truthful owner-private/manual mechanism if needed; do not turn short AAC listening into public-distribution or production Auto approval. AirPods cannot test aptX/LDAC.
  - SLIDLE: exact stock DCM WFI wrapper found, but need TOPCKGEN+4/PERICFG+0x18

read-only snapshot and eligibility/ownership review. Inherited I2C/APDMA/MSDC gates may prevent entry. No module prepared/loaded; do not remove protections just to make a counter advance. Deep idle additionally requires exact PCM, CIRQ/timer/clock/one-core/context handoffs; suspend PCM is not a substitute.
  - SOC/current/NTC/low-battery reserve/VBUS topology remain concrete physical

evidence gates. No meter available; no fabricated telemetry or threshold.
  - One consolidated final build and one owner install/qualification only after

independent work. Use `tools/production/system_update.py` with Hardware02 base and exact fallback, not package.py (which creates Y2DATA). No intermediate image is currently justified. Full8h endurance and OTA/rollback remain pending; destructive root OTA application needs explicit owner approval.

Full build requires clean reviewed source in both repos. Preserve unrelated user changes safely; do not silently commit them or reuse stale root binaries to pass. Existing SDK/build: `out/hardware02-worktrees/Y2Linux/out/hardware02-build/`. Prior packaging procedure: `out/hardware02-validation/assemble-package.py` and check-installed-arm-final.py. Final path remains `out/y2linux-hardware-final-candidate/`; it does not exist from this pass.

[Campaign](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-HARDWARE-FINAL.md), [capabilities](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-HARDWARE-FINAL-CAPABILITIES.md), [qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-HARDWARE-FINAL-QUALIFICATION.md) remain provisional ledgers.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
