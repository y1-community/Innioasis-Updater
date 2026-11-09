---
title: "Y2 Platform 1.0 full system suspend / resume - Innioasis Updater"
description: "Y2 Platform 1.0 full system suspend / resume Status: MORE WORK REQUIRED — source fixes implemented; physical full RTC resume FAILS on installed Baseline02. Work is isolat"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-suspend.html"
---

# Y2 Platform 1.0 full system suspend / resume - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 Platform 1.0 full system suspend / resume

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 Platform 1.0 full system suspend / resume

Status: MORE_WORK_REQUIRED — source fixes implemented; physical full RTC resume FAILS on installed Baseline02.

Work is isolated on `codex/platform-v1-suspend` in both repositories. Linux base `b5aea93`, Reborn base `b71b468`. No main-worktree edit, unrelated merge, push or flash. C1 WFI, C2 SLIDLE and C3 DORMANT entry/restore architecture are preserved. All device access uses the non-blocking `/tmp/y2-platform-v1-device.lock`.

## Starting hardware evidence and original failure

The 2026-10-04 locked reads identify installed Y2LINUX-BASELINE-02: Linux `8584ccd85f052f351fe51650b2348c83ca894ed4`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, kernel `6.18.0-y2linux-baseline-02`, root `2025.02.18-platform-v1.21`, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0. Battery reports Charging; current and previous SRAM suspend journals are invalid/empty, backstop inactive. These reads do not qualify this image's deep system suspend or cold-boot C3. Private receipt: `out/platform-v1-suspend/inspect-01/inspect.txt`.

[UART01 physical evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) independently proves repeated runtime C3 reset-and-return, not freezer/device/system suspend. The retained [Fix02 failure](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX02-PHYSICAL-QUALIFICATION.md%23full-rtc-suspend--fail-exact-boundary&anchor=full-rtc-suspend--fail-exact-boundary) entered full suspend, woke on RTC/SPM EINT (`0x20`), recorded reset dispatch `0x59325253`, restored CPU/syscore/secondaries and device callbacks, then stalled between `DEVICES_RESUMING` and kernel `EXIT`. Its RGU recovery was a **new boot, not successful resume**. That original stalled instruction remains unestablished. Current source already brackets device completion, console, thaw, PM_POST_SUSPEND and kernel exit; historical failure locations are not assumed current.

## Implemented corrections
  - Full system suspend now validates Linux's populated CPU0 context stash in its

finisher, before leaving coherency. It checks BIU readback, normal PCM pointer, length, UART request release, sleep timer/watchdog/power controls, local timer restore and CIRQ restore. Restore failures return an error, increment `suspend_restore_failures`, retain fault notes and quarantine the shared SPM owner. A real CPU reset return remains counted even if later restoration fails. Both entry refusal and successful wake unwind CPU/cluster/CIRQ ownership.
  - Linux can log a device resume callback error and still return zero from

`pm_suspend`. The existing journal previously retained such failures only in its small callback ring. It now preserves the first noirq/early/device resume error in its retained receipt, preventing a successful kernel exit from hiding a storage, USB, radio, graphics or audio restoration failure. Prepare refusal classification remains unchanged; no second tracing architecture is added.
  - Successful `pm_test` was indistinguishable from deep resume in the product

receipt. Receipts now capture the selected test mode. Deep restoration needs same boot, valid error-free kernel EXIT, the reset-vector stamp, full suspend PCM length 596 and a nonzero wake source. Staged success is recorded without advertising deep sleep or marking Reborn ready as a deep-resume result.
  - Reborn exposes `SleepRequested`, `SleepPreparing`, `SleepRefused`, `Sleeping`,

`Waking`, `Restored`, `RestoreFailed` through its typed platform boundary. The helper obtains explicit `sleep_prepare` acknowledgement: checkpoint queue and position, refuse playback/pending work, release ALSA and DRM scanout, blank display. Preparation blocks new input/transport/control mutations until unwind. `sleep_restore` restores scanout/backlight, renders a frame, reopens evdev queues and clears old press ages, queued wake edges, overflow state and wheel cadence. It runs on failed attempts too; status-socket liveness alone no longer proves application restoration.
  - A short Power gesture requests sleep when playback is paused/stopped; during

playback it blanks the display. An off-screen press wakes the display. A long hold opens the existing shutdown confirmation even with the screen off; its release cannot request sleep. Normal copy contains no SPM/CIRQ/stage names.
  - A one-shot resident qualification observer uses the existing SRAM receipt and

callback ring. Its coordinator can retain the checked shared device lease across separately reviewed one-shot trials. Host entry is never retried after a lost acknowledgement. It separates staged tests from actual entry/resume counter deltas, verifies boot, taint, positive suspend residence, child IRQ attribution, alarm clearing and ext4 error counts. No reset or flash command is present.
  - The present retained trace identifies an unmatched CS43131 resume callback.

The existing codec PM overlay now brackets force resume, regulator enable, access/reset delay, register-cache replay and XTAL mask restoration in the existing retained ring. Normal runtime audio does not emit these sleep notes. A separate verified source defect is corrected: after supply-disable refusal, restored rail references alone do not undo an earlier reset/partial rail cycle or the masked XTAL interrupt. Replay the cache and restore its interrupt mask without acquiring a second rail reference. Restore failure is reported; resume failure holds reset low when a reset GPIO exists, disables access, and records any supply-cleanup error. No AFE, clock, rail voltage or register-value change.

These are source/fault-injection results. The observed CS43131 callback stall is a confirmed boundary; its internal stalled instruction remains unknown. The rollback defect was found in source and is not claimed as the cause of that stall. The new source is not installed.

## Wake sources and charging policy

Power is the MT6323 key child IRQ (hardware child 5); RTC is child 20. Both feed PMIC EINT and SPM `WAKE_SRC_EINT`, not a dedicated Power/RTC SPM bit. The existing DT wake flags, child IRQ wake ownership, MFD late wake-mask ordering and CIRQ/GIC replay remain. Attribution uses same-boot serviced child IRQ deltas; the shared EINT bit alone is insufficient. RTC alarms are programmed/read back through the existing RTC API; the observer clears its own fallback alarm after wake or entry refusal. Awake-alarm delivery remains separate from suspend wake.

Active charging intentionally refuses device preparation with `-EBUSY`. The source documents the stock USB wake-lock rule and the need to service charging safety/watchdogs awake. No charger guard, PMIC protection or charging policy is bypassed. Battery operation and an independent observer are required for the later staged/full physical tests.

Exact MT6582 reference: [vendor SPM sleep source](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/arch/arm/mach-mt6582/mt_spm_sleep.c), retained under `out/cpu-c3-uart-research/` in the original repository. It uses SHUTDOWN_MODE for full suspend, DORMANT_MODE for runtime idle, and supports retained infrastructure/DDRPHY. No later-SoC register assumptions or arbitrary L2-retention changes are imported into full shutdown.

## Trace ownership

| Boundary | Existing evidence owner |
| --- | --- |
| Request / radio preparation / sync / return | y2-suspend, durable suspend-last.json |
| Freezer / device / late / noirq / CPU offline | patch 0060 stage marks; patch 0059 callback ring |
| PMIC wake masks / RTC armed | MT6323 MFD late callback snapshot |
| SPM / wake reason / context | spm.c, retained SRAM, full-entry/resume counters |
| Resume vector / cpu_resume | stackless resume-vector.S stamp then cpu_resume_arm |
| Syscore / noirq / early / device resume | kernel stage marks and callback phase ring |
| Console / PM notifier / thaw / exit | patch 0060 existing completion marks |
| Radio / Reborn / display/input restoration | helper receipt and explicit Reborn acknowledgement |

## Physical results

The owner reserved this continuous device window after the other sessions' tests and cleanup. The non-blocking coordinator lease is held throughout. Temporary Wi-Fi SSH on port 2222 uses the original authenticated host key; its owned listener survives CONSYS radio stop/start. Owner disconnects USB, and actual Discharging / USB presence 0 are confirmed before battery tests.

| Trial | Installed Baseline02 result |
| --- | --- |
| Freezer, charging | PASS; same boot, helper 0, COMPLETE/error 0, no SPM entry |
| Devices, charging | EXPECTED REFUSAL; DPM_PREPARED/-16; clean awake unwind, Wi-Fi returns, ext4 errors 0 |
| Devices / platform / processors / core, battery | PASS each; same boot, taint 0, COMPLETE/error 0; no deep entry; PM test reset to none |
| RTC awake alarm, 8 seconds | PASS; readback, one RTC child IRQ, automatic clear and explicit clear; SPM entries/resumes remain 0 |
| RTC full entry, 12-second alarm | FAIL; SPM EINT/reset-vector return, CS43131 resume callback never leaves, different-boot recovery with retained 30-second backstop |

The charging trial's generic success verdict is false because entry was refused; that is the intended charger safety result, not a failed unwind. Zero ext4 error counts alone do not prove resumed media I/O. Before full entry, owned 64-KiB files on data and SD were fsynced and read through aligned O_DIRECT/preadv; both match SHA256 `7daca2095d0438260fa849183dfc67faa459fdf4936e1bc91eec6b281b27e4c2`. Direct reads after reset recovery also match, with all ext4 errors 0. This proves preservation across the reset, not same-boot storage resume. Owned files are removed afterwards. Raw receipts are under `out/platform-v1-suspend/pm-*/`, `rtc-awake.json`, `storage-create.json` and `full-rtc-01/`. All these trials execute installed Baseline02/legacy helper, not this branch's new kernel guards or application acknowledgement protocol.

The recovered previous SRAM record is `sequence=175 stage=DEVICES_RESUMING`, `error=0 wake=0x20 pcm_length=596 reset_resume_entry=0x59325253`. Its callback ring is `cycle=138 last=7422 backstop_s=30`:`7406 phase=7 enter result=0 ms=10259443 device=0-0051 7407 phase=7 enter result=0 ms=10259443 device=1-0030 7408 phase=7 leave result=0 ms=10259443 device=0-0051 ... 7419 phase=7 enter result=0 ms=10259445 device=mmc0:0001 7420 phase=7 enter result=0 ms=10259445 device=mmc1:aaaa 7421 phase=7 leave result=0 ms=10259445 device=mmc0:0001 7422 phase=7 leave result=0 ms=10259445 device=mmc1:aaaa`

There is no leave for `1-0030` after its retained enter and no phase-8 completion or later stage. DTS maps this device to CS43131; the I2C1 controller resume already returned. **Do not infer that the codec returned because later parallel MMC callbacks returned.** The failure is inside the codec's system resume callback, which invokes runtime-force resume. Regulator work, reset delay, regcache/I2C and XTAL-mask update are separate remaining candidates, now individually marked in source. No particular inner call is claimed as the physical root cause.

Boot changes from `27e6d684-3794-4490-95db-a489027cd4f4` to `88b85fa3-2282-4d93-b0b8-818a105ddd0a`. This is reset recovery, not successful system resume. A watchdog timeout is consistent with the armed 30-second backstop and stopped callback; the decoded RGU reset cause was not captured and is not claimed as separately verified. The host launched exactly once, captured failure and stopped. A 12-second RTC alarm was requested and RTC interrupt enable is retained (`rtc_enable=0x5`); the wake is SPM EINT. Child-IRQ attribution and actual suspend residence are unavailable across the reset, so complete RTC wake remains unqualified. Power was left untouched. No Power trial or repeated cycles follow.

After owner USB reconnection, stock Reborn is running in the new boot with Mesa/Mali rendering available, USB SSH and Wi-Fi connected, original radio policies 1/0, root/data/SD writable, taint 0 and ext4 errors 0. These are recovery checks, not resume acceptance. PM test is none, backstop armed/running 0 and RTC alarm empty. The owned temporary observer/listener disappeared with /run at reboot; owned media fixtures are removed. The device lease is released normally to the master coordinator/performance session. No candidate/service replacement was performed. [Committed bounded evidence and raw-receipt hashes](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-suspend-2026-10-04.json).

| Coverage | Current full-suspend result |
| --- | --- |
| Power wake / clean input / backlight | NOT_RUN after failed RTC return |
| RTC awake alarm / RTC deep wake / clear | PASS awake / PARTIAL EINT+reset return, full resume FAIL / PASS awake clear; empty after recovery |
| Same-boot complete system resume | FAIL; boot changed |
| eMMC / SD / filesystem | Staged return PASS; full resume NOT_QUALIFIED; O_DIRECT data+SD hashes preserved after reset, ext4 errors 0 |
| USB | Staged return PASS; reattachment works after reset; full resume NOT_QUALIFIED |
| Wi-Fi / CONSYS | Staged quiesce/restore + authenticated observer PASS; full resume NOT_QUALIFIED |
| Bluetooth / BTIF | Initially disabled, policy preserved; active full restore NOT_RUN |
| GPU / Lima / DRM / display | Staged callbacks return; available after reset; full restore NOT_QUALIFIED |
| AFE / CS43131 / ALSA | CS43131 resume callback BLOCKED; audio full restore FAIL/NOT_QUALIFIED |
| Reborn | Restarted in new boot; same-process full restore NOT_PROVEN; new handshake native/QEMU PASS, physical NOT_RUN |
| Wheel / input / RTC timekeeping | Wheel callback returns; complete full restoration NOT_QUALIFIED |
| Five / ten mixed cycles / longer residence | NOT_RUN / NOT_RUN / NOT_RUN; first full trial failed |

No electrical standby measurement is available. Sleep-duration/CPU/IRQ/battery voltage/SOC observations are proxies only; no standby-current number is claimed. The failed trial loses its resident monotonic/BOOTTIME receipt at reset, so there is no measured full-suspend duration or valid same-boot CPU/IRQ/battery delta. The requested alarm delay is not substituted for a measured residence.

## Validation and limitations

Fresh production-config ARM kernel Image, zImage and modules build in the pinned host environment. Final kernel hashes and logs are under `out/platform-v1-suspend/`; build artifacts under `out/platform-v1-suspend-build/`. The 132-test targeted source run passes: 129 passed, three emitted-DTB checks skipped. Coverage includes suspend policy and failures, CPU/idle/timers/CIRQ, storage/MMC context, USB, connectivity/radio, GPU and audio. The later 23-test policy run passes, including two added charging/preparation-refusal checks. The five full-path/observer fault tests also pass after adding inherited-lease exclusion and inode checks. After the codec correction, 11 focused codec/full-path/ retained-journal tests pass, including real callback fault models for reset/cache replay, single rail-reference ownership, cache/XTAL/rail errors and quiet runtime tracing. A later audio/policy run has 13 tests: 12 pass and one emitted-DTB skip. The corrected Image/zImage/modules rebuild passes in the same isolated ARM build. Documentation link checking resolves this report/evidence and all Reborn links; its only failure is the pre-existing sibling Y2Player Phase4 link absent from this dedicated worktree. No unrelated documentation is changed. Final Image is 12,406,144 bytes, SHA256 `6edabf993aaa435f4def969064df26593c4ff24ce568ce5d8b9d47dbb5bea9b6`; zImage is 4,523,792 bytes, SHA256 `29dcb7c8e7773f48b504edfad1a1d67ff0aaccf484d4b58c791613e21ca8d2cb`. Reborn fmt and strict all-target Clippy pass; all 244 workspace tests pass with locked dependencies and isolated temporary paths. The ARM release build passes against the exact Baseline02 SDK; Reborn SHA256 is `afe9291a9412ca0f61a182ff5fad8b4e77f6ff1aaafac9269dbd153c4374c571`. Native and Cortex-A7 QEMU headless processes pass explicit prepare/checkpoint, prepared mutation refusal, restore/control admission and a second prepare/restore in the same process. QEMU uses the Baseline02 ARM runtime libraries. These are application IPC tests, not physical GPU/audio/input proof.

Wake-input reset is scheduled before fallible display restoration, so even a failed display restore discards the prior gesture before accepting input again.

The ordinary product request still preserves its existing physical-qualification refusal. It must not enable unqualified full suspend simply because runtime C3 works or these source tests pass. Installed Baseline02 cannot execute the new Reborn prepare/restore protocol without a coherent userspace update; new kernel checks likewise require owner installation, which this pass does not perform. Current installed-image evidence now narrows the blocker to CS43131 system resume. The exact inner stall and same-boot whole-device acceptance remain open. The next smallest physical boundary requires a coherent owner-installed candidate with the codec substep notes and new userspace handshake. This pass never flashes; no source-only correction or reboot recovery promotes the product gate.

Implementation commits:
  - Linux `69fa2c7`: checked full-suspend restoration, retained device resume errors,

explicit Reborn acknowledgement, one-shot observer and regression tests.
  - Linux `c73cd83`: charging and preparation failure policy.
  - Linux `50cc218`: temporary Wi-Fi observer port and verified host-key support.
  - Linux `7e10bdc`: retained coordinator lease across staged and wake trials.
  - Linux `a69bd50`: codec failed-suspend rollback and retained full-resume substeps.
  - Reborn `4544b1a`: typed preparation/restoration and Power/input semantics.
  - Reborn `f69c3c4`: discard wake input before fallible display restoration.
  - Reborn `c57a55f`: reopen evdev queues and clear overflow state after full resume.

Documentation/evidence commits preceding the physical receipt: Linux `e5b805e`, `c7086e8`, `5ed5e08`, `564710f`. The final physical receipt is committed after `a69bd50`; its revision is available from the branch log. No push or flash.

Both worktrees are ready for source review. This pass does not deliver a sealed BOOTIMG/rootfs pair or install one; the built kernel and Reborn ELF are host artifacts. A future coherent candidate must include the helper/platform modules and Reborn protocol together, then repeat this physical sequence from one RTC trial. The ordinary product gate remains refused until that proof exists.

## Changed files

Linux:
  - `kernel/platform/{spm.c,spm-suspend-policy.h,pm-journal.c}`
  - `kernel/patches/{0030-cs43130-system-pm.patch,manifest.json}`
  - `tools/platform/y2_platform/{cli.py,sleep.py,suspend_record.py}`
  - `buildroot/board/y2/production-overlay/usr/sbin/y2-suspend`
  - `tools/development/{qualify-platform-v1-suspend.py,suspend_platform_device.py}`
  - `tests/{test_cpu_fix03.py,test_platform_v1_suspend.py,test_sleep_product.py,test_suspend_policy.py,test_suspend_audio.py}`
  - `docs/validation/Y2-PLATFORM-V1-SUSPEND.md` and bounded JSON evidence
  - `docs/planning/{roadmap-gap-audit.md,platform-v1-roadmap.md}`
  - `docs/DOCUMENTATION_CATALOG.md`

Reborn:
  - `app/reborn/src/{main.rs,bin/reborn-preview.rs}`
  - `crates/reborn-control/src/lib.rs`
  - `crates/reborn-core/src/{lib.rs,platform.rs}`
  - `crates/reborn-platform/src/{client.rs,input.rs}`
  - `crates/reborn-ui/src/{lib.rs,pages.rs,tests.rs}`

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
