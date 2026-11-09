---
title: "Roadmap gap audit - Innioasis Updater"
description: "Roadmap gap audit POWER-FINAL-06 INFRASYS power-down bring-up admission — 2026-10-09 Standing milestone-boundary audit before materially changing hardware/memory scope, u"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-roadmap-gap-audit.html"
---

# Roadmap gap audit - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Roadmap gap audit

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Roadmap gap audit

## POWER-FINAL-06 INFRASYS power-down bring-up admission — 2026-10-09

Standing milestone-boundary audit before materially changing hardware/memory scope, using real hardware evidence only. Reviewed: the 05 overnight archive 88 (38,052.5 s of 38,234.6 s suspended, 64 cycles, resume 2.2 s, SOC 88%→66% voltage-derived, about 2.1 points/h, with a terminal `Y2USB IRQ overflow` at 01:34 and a kernel Oops at the first Wi-Fi restore) and the 9 h idle archive 89 (boot `65d3b0c9`, taint 0, 31,230 s of 32,679 s in SPM sleep, 51 maintenance wakes, no USB overflow, no Oops, single run; SOC about 2.2 points/h). The owner recalls stock at about 1 percent per night; no stock baseline has been measured on this unit.

Corrections admitted: full suspend already runs the vendor 597-word `pcm_suspend` (words identical to vendor `mt_spm_sleep.c` d53dd75c, SHA-256 `0ee71194…6ab94`; stock `slp_infra_pdn` defaults to 1 in the retained FM kernel). The 05 report's "480-word dpidle" statement was the runtime-idle line and is corrected on the 06 branch. The real difference is `infra_pdn=false` plus a missing post-wake restore. The Wi-Fi Oops is explained by the 01:34 terminal USB stop: `platform_device_unregister(musb-hdrc)` freed the gadget device that the ECM netdev `usb0` references as `dev.parent` (the stack carries `"usb0"`), so the first later netlink query crashed.

Scope change admitted for source work and offline qualification only: vendor `infra_pdn=1` (INFRASYS and DDRPHY MTCMOS power-down) with an exact-source restore of PERICFG and a read-only INFRACFG report; MUSB L1 interrupt ownership; park-not-unregister on a terminal USB stop; UART sleep re-arm. Bounds retained: the PCM and wake mask are unchanged, the 30 s RGU backstop is kept, any unverifiable restore or a previous boot that ended on the new `INFRA_PDN_ENTRY` journal stage pins the boot to the proven INFRA-retained mode, and `/sys/firmware/y2_infra/mode` is the explicit owner switch. The agent does not flash; no PMIC rail, eMMC supply, storage or DRAM setting is changed; nothing is claimed about drain.

Coverage table: the full suspend/power row stays PARTIAL and MORE_WORK_REQUIRED; physical status of the bring-up candidate is NOT_RUN. New physical gates: first INFRA power-down cycle (restore verified, DRAM and all drivers healthy), repeated cycles and maintenance wakes, USB cable wake and re-enumeration, Wi-Fi/BT restore, an overnight drain compared with the 05 baseline of about 2.1 points/h. No milestone is promoted or closed; the production cleanup phase follows only after hardware qualification.

## Deep-sleep continuation admission — 2026-10-07

### Clean corrective-image physical admission

05 hardware evidence refresh, 2026-10-08: scope unchanged for memory layout and production scope; one PMIC write-allowlist extension (bit 0 of VA/VIO28/VUSB/VM/VIO18) with explicit owner approval and a runtime revert. Owner flashed POWER-FINAL-05 (Linux `837b614`). Archive 82–84: identity, taint 0, `lp_sel applied=1`, Reborn/helper hashes match, ext4 0. Archive 85–87 (before/after-sleep probe): 1573.4 s suspended, 2 maintenance wakes, SPM 3/3, aborts 0, golden PMIC differences at suspend entry 22→17, connectivity and SD rails off in suspend, eMMC VCC/VUSB/VGP2 on. #28/#34 suspend: PARTIAL unchanged (reliability), electrical minimum still UNKNOWN (no current measurement, capacity unknown). Open: overnight/8 h drain, Power/RTC wake and early-boot on 05, vendor `pcm_suspend`, display/poweroff gaps. No milestone promotion. Linux provenance `837b614`.

04 hardware evidence refresh, 2026-10-08: scope unchanged (no memory-layout, hardware or production-scope change; retained SRAM region and ring size untouched). Owner flashed DEEPSLEEP-FINAL-04 (diagnostic successor; Linux `5e26757`, Reborn `97ff8c3`). Archive68 verified identity, taint 0, helper/Reborn hashes and ext4 counters; the old 03 guard is identity-mismatched. Normal-policy owner trials: archives 70-71 (469.27 s, same boot) and 72-73 (one hour: 3805.25 s suspended, six dark maintenance wakes re-entered, SPM 9/9, aborts 0, restore failures 0, taint 0). Coverage: #28/#34 suspend PARTIAL improves (clean repeated residence on 04) but the intermittent pre-SPM stall is unresolved (diagnostic change may have shifted timing); Power/RTC wake on 04, formal 30-min/2-h gates, overnight drain, warm-start display, user poweroff and cold-C3/electrical remain open; SOC is provisional (71%→69% includes post-charge relaxation). No milestone promotion. Next smallest gap: early-boot stall-window test after owner reboot, then overnight drain. Reborn source/ROM/recovery provenance is unchanged; Linux provenance is `5e26757`.

03 late analysis (documentation/source only), 2026-10-08: no new hardware evidence. Re-reading archives65/66 against exact03 `drivers/base/power/main.c` and `pm-journal.c` shows the retained ring records only devices that have PM callbacks, so the recurring pre-SPM stop (always after a returned `11008000.i2c`) lies in an unrecorded wait, and the reset followed about half a minute later. Prepared a local diagnostic successor source (per-device `WAIT`/`LOCK` records and a built-in device-phase sampler); unit tests, existing journal/suspend suites and a production config cross-compile pass. Not built, flashed or deployed: a planning/source row is not hardware authorization. Hardware/memory/production scope is unchanged (the retained SRAM region and ring size are not modified), no milestone is promoted and source/ROM/recovery provenance is not repeated. Next gate: owner decision on building and installing the diagnostic successor.

03 evening evidence refresh, 2026-10-08: host-lease-protected read-only archive67 preserves first return, pstore/PM, persistent journal and health after the owner's roughly seven-hour absence. Boot81dce40c ended with an orderly `reason:user` poweroff at approximately09:55:39 CEST; the current bootad0d5416 began about16 seconds later. Those times use host-anchored BOOTTIME because device wall time is unreliable. This is a separate event from the earlier unclean reset. The03 guard still names failed boot0132fb21 and remains pending. Current SPM entries/resumes0/0,421 guard refusals before cable return, and matching BOOTTIME/MONOTONIC growth show no whole-system sleep on this boot. CPU0 runtime DORMANT continues without recorded restore failure. The device journal's provisional battery estimate falls57%→32% in about7.0h unplugged, with ADC 3.862→3.736V; connected at17:00 it reports Charging31% and no charger errors. The previous boot's63% versus new boot57% crosses poweroff and load changes; do not treat that difference as measured off-state consumption. No calibrated capacity or pack current is available.

Installed03 hashes match archive65; taint0, responsive paused player, PCM closed, radios/scan off, ext4 errors/warnings0 and configured USB remain confirmed. The first return's pstore contains `Power down`, consistent with the orderly ledger. No build, flash, deployment, reboot, guard clear, forced sleep or new trial was performed. This adds physical evidence without changing hardware/memory/production scope or promoting a milestone. Admission remains MORE_WORK_REQUIRED: resolve the recurring pre-SPM failure, then qualify controlled30-minute/two-hour/endurance and independent reliability/electrical gaps. Source/ROM/recovery provenance is unchanged.

03 morning evidence refresh, 2026-10-08: the owner reports approximately six hours unplugged, about88% at removal and55% in the morning, and confirms no manual restart after installation. Read-only, host-lease-protected archive `out/deep-sleep-final/evidence/20261008/66-image03-morning-return/` preserves the first SSH state, retained PM/pstore export and persistent logs before any further inspection. Exact03 sources/helpers remain unchanged. Boot changed from0132fb21 to81dce40c; the boot ledger marks the preceding shutdown unclean.

Coverage changes from03 suspend NOT_RUN to FAILED automatic suspend attempt: the old boot requested kernel suspend at BOOTTIME398.407s; retained sequence8 stops at DPM_PREPARED, with successful callback records through11008000.i2c at398.638s. No completed SPM interval or return survives. The owner-uninitiated reboot has no reported RGU reset cause and no retained panic; neither the exact failing callback nor watchdog causation is established. The new boot records SPM0/0 and380 `sleep_recovery_required` refusals over roughly6.44h. Its matching 03 guard remains pending and is preserved. This repeats the known device-phase failure pattern on03; earlier02 successful returns remain narrow historical evidence, not reliability acceptance.

Battery #16/#27/#28: pre-cable journal confirms88% and55%, with entry ADC 4.092187V and final Discharging sample3.821484V. The last dark sample was 56%/3.846972V; the55% endpoint is screen-on. SOC is provisional; the approximate 33-point drop is not a measured capacity/current or battery-health finding. CPU/idle #28/#34: runtime CPU0 DORMANT now has807610 entries/resumes and zero restore failures on this03 battery boot, distinct from full-system suspend; complete cold-C3/electrical qualification remains PARTIAL. Display/audio/radios/ storage #29/#31/#32: morning application responds, playback paused, PCM closed, scan/radios off, taint0, ext4 errors/warnings0. Existing warm-display and poweroff defects, controlled30-minute/two-hour/endurance, charging/electrical and #33 release gates remain open; historical#30 is unchanged.

This is an evidence refresh within the active investigation, with no milestone activation/closure or hardware/memory/production expansion. No build, flash, deployment, guard clear, forced sleep or new trial occurred. The roadmap and [overnight report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-DEEP-SLEEP-FINAL.md%2332-overnight-result--2026-10-08&anchor=32-overnight-result--2026-10-08) record the failed observation. Next smallest gap is the recurring pre-SPM device-suspend failure, before any repeat endurance acceptance. Device wall time was reset to build_floor and is not established; use per-boot counters and host capture times. Unchanged source/ROM/recovery provenance was not repeated.

03 installation evidence refresh, 2026-10-08: archive65 records the owner flash and requested quick SSH check on boot0132fb21..., taint0. Exact paired sources, kernel/root identity and installed Reborn/three helper hashes match03. First display frame, application status, configured USB, active fault-free charging and three zero ext4 error counters are CONFIRMED for this boot. The production synthetic-USB wake removal is present; physical cable/battery wake remains. No blocking operation owner, applicable quarantine, test/alarm or backstop is active. No device mutation or agent flash occurred.

Coverage is SOFTWARE_VALIDATED / INSTALLATION_SANITY_PASS, with03 full suspend and endurance NOT_RUN (SPM0/0 while cable-attached). The owner's exploratory night remains distinct from controlled qualification; preserve entry/endpoints and morning evidence before any reboot. This narrow evidence update neither activates/closes a milestone nor changes hardware/production scope. Existing issue mappings and independent device-stage, warm-display, poweroff, C3, SOC/charging/electrical and longer endurance gaps are unchanged.

Successor03 software closing review: source `cfb7e098eae60918f47d7b330445bf66e9d61817` plus Reborn97ff8c3 builds the coherent rootv1.33 pair.578 platform cases pass (541 container + ten native dependency + 27 native splash),335 Reborn tests plus fmt/strict Clippy, fresh ARM build, kernel/config/DT/module ABI/QEMU, installed tools and ELF closure384/1411 pass. Both ext4 images and the preserving package validate; no Y2DATA payload. The first splash test failed only because native libdrm/Pillow were unavailable inside the kernel container; its full27 cases pass on the packaging host, and the corrected profile completes. Source and image receipts stay linked.

Coverage becomes SOFTWARE_VALIDATED / PHYSICAL_NOT_RUN for03. All narrow02 physical results retain their source identity. The unresolved device-stage, warm-display, poweroff, cold C3, charging/SOC, electrical floor and long-duration gaps remain; no issue/milestone/readiness promotion. Owner alone installs03, then exact identity/boot/USB/charging verification precedes sleep observation. The planned overnight enablement on02 never occurred; archive64 is the latest read-only preservation, not a sleep start. Preserve02 and matching symbols, publish only the new03 folder, and record the owner's actual overnight choice after installation. Any morning result must prove its sleep time and endpoints.

Successor03 build boundary, 2026-10-08: the owner now explicitly requests new flashable images containing all completed fixes. This supersedes enabling tonight's observation on02: archive64 completed, but the guard was never cleared and no overnight collector/alarm/entry was armed. Preserve that distinction in the handoff. Installed identity and all hardware evidence remain02 plus its recorded live corrections, not03.

Admit one coherent BOOTIMG/Y2ROOT candidate03, rootv1.33, paired with Reborn `97ff8c357bab12319087740d7c97b5051e6588f5`. Include committed single-write PM, synthetic USB wake, maintenance handshake, endpoint/journal and splash/renderer recovery changes. Preserve voltage/SOC curves, charger ceilings, protection, partition layout and Y2DATA. Failed/untracked reset diagnostics are excluded. Use isolated paired worktrees and reusable verified caches; retain immutable02 images and matching build/symbols. No agent flash or release promotion.

Coverage/gap audit: real PM and Power/RTC same-boot returns, normal inactivity and one maintenance re-entry are CONFIRMED only for their recorded sources. 03 as a combined image is SOFTWARE_PENDING / PHYSICAL_NOT_RUN until its checks. The candidate needs the complete production profile including new regression modules, Reborn fmt/strict Clippy/workspace tests/ARM, kernel/config/DT/modules/ ABI/QEMU and package/preservation/privacy checks. Intermittent devices, warm display root cause, poweroff, cold C3, endurance, SOC/charging and electrical floor remain open; all existing issue mappings and other classifications stay unchanged. After owner flash, verify exact identity and USB/charging before any physical sleep observation. A new image does not convert old tests into new-image qualification or waive longer endurance requirements.

Owner-requested overnight observation, 2026-10-08: after the stop checkpoint, the owner explicitly chose to leave the Y2 unplugged for the rest of the night and inspect it in the morning. This supersedes the parked runtime-idle plan for that observation only. Archive64 rechecks the same boot, taint0, COMPLETE667, idle backstop and empty RTC alarm before any change. The accepted live source remains0ba99f5 plus3929026 and the runtime synthetic USB wake correction; the local maintenance correction remains undeployed.

Admit clearing the diagnostic between-test quarantine under both operation locks, with durable before/after identity and battery records, so ordinary Reborn inactivity can request full suspend after unplugging. Preserve all playback/transfer/update/maintenance inhibitors, ten-minute battery checks, low-voltage/thermal protection and the existing entry/resume backstop. No forced entry, new helper loop, diagnostic module, alarm, source deployment or firmware change. Existing event journaling records actual entry/maintenance/ resume; host SSH stops before unplugging. A failed/reset path remains evidence, not success; do not automatically clear a subsequent failure quarantine.

This is an exploratory owner observation, not a waiver or completion of the thirty-minute/two-hour qualification sequence. One dark maintenance re-entry is physically confirmed; intermittent devices/display/poweroff defects and the latent maintenance race remain open. Coverage classifications and issue/release status below are unchanged. Morning must preserve evidence before mutations and calculate actual suspended residence, all awake gaps and valid battery endpoints; an unplugged night alone does not establish that suspend persisted all night.

Session stop review, 2026-10-08: the owner requested an early finish and reconnected USB. Archive62 retains trial61 on unchanged02 plus the recorded overlays/runtime wake correction: 600.004089355 + 343.159606934 seconds of actual suspend, same boot `f567b2c3...`, taint0, SPM8→10, COMPLETE667/error0, application restored and ext4 errors0. One automatic maintenance return kept the display dark and connectivity suspended and then re-entered successfully. USB insertion ended the second interval; the helper's wake label is unknown, while cable/CHRDET evidence and unchanged Power/RTC counts identify the owner interruption. It is not a thirty-minute pass or usable terminal drain endpoint.

Coverage refresh: maintenance with dark/radio-off re-entry becomes CONFIRMED narrowly for this live configuration. Thirty-minute/120-minute/overnight acceptance, SOC/charging, electrical minimum and cold-battery C3 remain PARTIAL. The latent host-reproduced wake-count race was not observed in this trial. Original intermittent device-stage reset, warm-start display and poweroff defects remain open. All other coverage rows and existing issue mappings below are unchanged; no milestone, issue or release is closed.

Archive63 verifies no collector/helper remains, both operation locks are free, RTC alarm empty, recovery backstop idle, pm_test none and persistent quarantine restored. Reborn answers, USB is configured and charging has no reported fault. The host device lease is released. The owner's stop request supersedes all earlier instructions to continue the current trial tonight. On resumption, recheck live identity/state, deploy the reviewed maintenance fix with backups, qualify the exact corrected source in a short product trial, then repeat30 minutes before admitting longer endurance. No additional test, source deployment, reboot, candidate build, flash or charging-policy change at this closing boundary.

During unchanged trial61, a host regression reproduces an independent maintenance race: a normal BAT0 event during the2-second safety interval makes the reused count stale, so the next atomic store refuses re-entry. Local-only d43b592 refreshes that count afterward while retaining Power/RTC IRQ comparison, all safety admission and the late-event store guard;27 affected tests pass. This is a localized source correction within existing product policy, not a hardware/memory expansion. It is not deployed and must not be attributed to61. Archive62 now confirms the first maintenance re-entry succeeded; its later owner interruption is independent of this race. Qualify the corrected source before extending endurance. Release gates below stay unchanged.

Archive59, 2026-10-08: the narrow USB wake correction passes the actual normal product path on boot `f567b2c3...`, taint0. Live maintenance owner7356 refuses entry, then its release atBOOTTIME3895.063 is followed by automatic kernel entry3916.070. One203.051331-second SPM interval returns through RTC IRQ7→8, Power12→12, COMPLETE573, Reborn restored, all three ext4 error counters0. SPM entries/resumes7→8, restore failures0. No hidden retry or direct test-helper suspend call. USB reconnect and Charging work afterward; the six physical wake owners remain enabled. Base02 plus recorded0ba99f5 userspace and runtime-only USB wake changes must remain distinct from a clean successor image.

Coverage refresh: ordinary inactivity, owned maintenance/USB inhibition and complete product restoration become CONFIRMED narrowly for that overlay/policy. Power/RTC and earlier staged/kernel/storage/audio results retain their scope. Cold-battery C3,600-second maintenance returns,30/120-minute/overnight drain, SOC/charging and electrical minimum remain PARTIAL. Original intermittent device-stage reset, warm-start display and poweroff defects remain open; all other CPU/peripheral, memory/recovery/calibration/security/time/host rows and existing #16/#27–#34 issue mappings retain their prior classifications. No milestone, release or remote issue closure.

The earlier30-minute admission deployed tested3929026 receipt/journal changes in archive60 under operation locks with old-byte backup and overlay ledger; archive62 preserves first entry ADC across maintenance cycles and completed results at the existing journal cadence. The next observer must separately retain a fresh post-resume battery-owner sample: the immediate kernel-return receipt can still contain the pre-sleep SOC sample. Require at least1800 actual SPM seconds, dark/radio-off600-second maintenance returns, one terminal RTC wake, same boot, normal application restoration and no new integrity errors. Stop on first failure and re-establish quarantine. No SSH in the battery window. The existing backstop, PCM watchdog, battery reserve and charger limits stay intact. Two-hour admission depends on this result; no new image or flash is authorized by this audit.

Archive56 narrows the next product failure: unbuffered source0ba99f5 removes the close-time replay, but each of three normal automatic requests returns EBUSY during device suspend; SPM stays7/7 and taint0. The only wake-source `wakeup_count` increasing is synthetic `y2-usb-input`,2→8; hardware PM wake IRQ is absent for these refusals. Driver `y2_usb_set_power()` unconditionally calls `power_supply_changed()` during MUSB PM, which activates the default wake source. The explicit owner helper never armed wakeup_count, explaining that path's passes without proving this product handshake. No Power/RTC failure or reset is inferred from these pre-SPM refusals.

Admit a narrow causal runtime test: disable wake capability only on the software `y2-usb-input` power-supply child. Verify the physical charger/CHRDET, RTC and Power wake owners remain enabled; preserve notifications/current allocation and all charging/voltage protections. Corresponding source uses the standard `power_supply_config.no_wakeup_source` flag. No diagnostic module or raw MMIO. Repeat the bounded automatic-policy test before any longer interval. Keep a runtime-policy ledger separate from base02 and the Python overlay. Original intermittent devices and warm-display failures remain unresolved; all other coverage/issue states above retain their classification. The collector's error cleanup also raced a later normal helper's guard clear; both live locks now protect restored quarantine. Fix collector cleanup ownership before repeating.

Product boundary, archive53, 2026-10-08 local: clean02 boot `f567b2c3...` refuses automatic entry for live owner `maintenance:4694/python3`. After lock release it requests full PM normally. Kernel logs show an early-wake refusal, then an immediate second entry and RTC return: 6507253 ticks (198.585602 s), SPM7/7, taint0, no reset. The helper nevertheless records `kernel_suspend_refused`, result2 and RADIOS_RESTORING470; its application restoration runs, but no successful product completion is recorded. The observer fails and re-establishes quarantine. This is not a product-policy pass.

Installed Python3.12.14 and host fixtures reproduce the exact mechanism: `Path.write_text('mem\n')` buffers a sysfs command, retries the failed flush on close, and propagates the original EBUSY after the repeated write succeeds. Admit a localized unbuffered, single-write correction to product PM controls, real Python-I/O error/short-write regressions, then a backed-up userspace-only deployment and bounded repeat of the same automatic-policy test. Preserve the sealed02 image/source identity and explicitly record the live overlay. No kernel/module/voltage/partition changes or new candidate per hypothesis.

Coverage refresh: named maintenance/USB refusal and automatic request are CONFIRMED narrowly; complete product restoration remains PHYSICAL_FAIL pending this correction. Clean Power/RTC kernel returns remain CONFIRMED narrowly, original intermittent device-stage reset and warm-start display remain PARTIAL/ PHYSICAL_FAIL. Runtime C3, charging/SOC, electrical minimum and longer endurance remain PARTIAL. All other CPU/peripheral, memory, recovery, calibration, security/time/host coverage and existing #16/#27–#34 mappings are unchanged; no milestone or remote issue is closed. Next gate is corrected automatic PM, before longer endurance.

Clean repetition boundary, archive50: on the same untainted `f567b2c3...` boot, three RTC30 trials, a second Power trial and RTC310 all pass. SPM totals6 entries/ 6 resumes, aborts/restore failures0, COMPLETE408. Clean wake coverage is now Power2/2 and RTC4/4. Final305.200562 s residence has one expected RTC wake, automatic alarm disarm and no unexpected wake; ADC4.057031→4.052416 V, SOC89→89. The unchanged voltage-derived percentage is not an overnight drain pass. The existing infrastructure-retention/electrical and longer-endurance limits stay.

Admit one bounded normal-product automatic-policy test after preserving50. Use the installed helper and normal Reborn inactivity path, a real maintenance flock held beyond the60-second timeout, then release it; RTC300 bounds wake. Clearing the diagnostic quarantine is authorized only for this reviewed clean boot/test, with renewed quarantine after return. The observer must not directly write /sys/power/state or invoke owner-qualified suspend. Verify USB and named maintenance refusal, no SPM entry while inhibited, normal automatic entry after release, RTC/same-boot/taint-zero restoration. This advances the next product gate; it does not waive the original intermittent device/reset or warm-display failures. Other coverage rows and existing issue status remain unchanged; no new image, voltage/current, memory or storage scope is added.

Clean Power boundary, 2026-10-08 local: archive47 on exact02 boot `f567b2c3...` passes all five PM stages and one real Power return with taint zero, no modules, SPM entries/resumes 1/1, aborts/restore failures zero and COMPLETE seq163. Hardware residence is 1243558 ticks = 37.950378418 s; Power IRQ 6→8, RTC 0→0, fallback alarm cleared. Archive48 verifies five seconds of advancing PCM, closed PCM after pause, unchanged zero ext4 errors, and 262144-byte fsync/hash checks on internal and SD storage. The quick health read immediately after resume reports Wi-Fi not authenticated during reconnect; do not label that snapshot an all-services pass. Owner confirms the normal player screen.

Coverage refresh: clean staged PM and one Power/CPU-context/storage/audio/display return become CONFIRMED narrowly on02; repeated Power, clean RTC, automatic policy/inhibitors, cold-battery C3, long endurance and electrical minimum remain PARTIAL. Original intermittent device-stage reset and warm-start display fault remain PHYSICAL_FAIL/PARTIAL; no assumed causal correction or issue closure. Other CPU/peripheral, memory/recovery/calibration/security/time/host coverage and existing issue mapping retain their prior status. Admit three RTC30 trials, one scheduled Power/RTC300 trial and one RTC310 measurement requiring at least 300 actual SPM seconds, stopping at the first failure. Keep quarantine and the 30-second PM backstop; no module, electrical, image or partition change.

Owner hardware restart restores exact 02 on boot `f567b2c3-97eb-42e2-8c24-ffca801be25c`, taint zero, only the normal DRM module, and advancing startup vblank 17/87/154/222. Archive `45b-clean-hardware-return/` preserves identity, power, retained state and logs; the owner confirms the normal player screen. This permits the previously admitted clean five-stage sequence and one bounded Power-wake trial, with a 300-second RTC fallback and existing 30-second PM backstop. No observer or display recovery module is loaded. All coverage rows retain their prior status: diagnostic RTC progress does not close the intermittent devices failure, warm-start display fault, clean wake, product policy or endurance gates. Product sleep remains quarantined pending the actual clean return.

Latest diagnostic `34-device-wait-normal-return/` returns from freezer on `e6b85337...` but application restoration fails with graphics presentation -EPROTO. Devices is never reached; no outstanding kernel task is sampled. Initial display vblank timeout precedes the probe, and the splash handoff then retries after losing ownership. Source also shows the purported one-time renderer recreation repeating on each failed frame. Admit ordinary display service recovery and targeted source fixes for this observed failure path; no raw register writes, protection changes, production PM acceptance or new candidate per hypothesis. Display/app recovery stays PHYSICAL_FAIL/PARTIAL; all other coverage and existing issue mappings above/below are unchanged. The original DPM_PREPARED wait remains open, not attributed to a transient UART/SRCU stack captured during a passing diagnostic. Next gate is a working display followed by bounded localization of that wait.

Normal owner off/on after terminating the failed splash does not recover frame IRQs (`35-display-recovery.json`); Reborn has been stopped to end its retry loop. Admit a matching active-display observer using pinned MT6582 register offsets, read-only MMIO and balanced references to already enabled clocks/domain. It refuses inactive/off states and has no background worker, reset, DMA or raw register write. This is diagnostic localization, not a power-domain scope expansion or proof of the hardware cause. Preserve all same-boot evidence.

Archive `36-display-observer-complete/` localizes the no-vblank endpoint: OVL flow 0x280f8d00, FSM 0x100 (`h_wait_w_rst` in pinned vendor ddp_debug.c), unchanged across 35 samples; SMI GREQ zero. Re-review all coverage groups: display/reset stays PARTIAL/PHYSICAL_FAIL; current PM is diagnostic only and the original device wait remains unresolved. CPU, peripherals, battery, memory/recovery/calibration/security/time/host gates and issue mappings remain unchanged. Admit one source-matched, bounded OVL-only recovery diagnostic after normal DRM master disables scanout. Require OVL/RDMA/DSI/mutex stopped and exact vendor SMI idle operands before any reset; preserve every unrelated reset bit. The pinned BSP uses MMSYS 0x138 bit 8 after failed OVL soft reset; LCM reset 0x13c is distinct and must not change. Compile and exercise refusal/timeout/ preservation paths before loading. No live DMA reset, domain collapse, voltage, protected storage or firmware write is authorized. Recover frame IRQs and working UI on the same boot before accepting this narrow causal correction.

That recovery diagnostic loses USB/Wi-Fi before returning. The last host output is the durable evidence directory, not a reset result. Normal KMS disable and an additional read-only capture precede module loading; all remain possible stopping points until recovered checkpoints localize the failure. USB replug does not recover transport. Admit the necessary owner hardware restart after complete pre-test archive `36-display-observer-complete/`; recover pstore and the diagnostic directory first. No recovery backstop was armed for this test; require one before any subsequent potentially blocking hardware diagnostic. No gate advances; no production reset code or new image is admitted by this failed trial. The separately observed application readiness/retry bugs remain eligible for targeted fixes and native regression checks.

Owner restart returns exact 02 on boot `22bd28fa-62ed-4e1e-afe4-0e6c6e209ac7`, uptime 46.41 s, taint zero, normal frame IRQs and Charging at 4.131518 V. Archive `38-display-hang-reboot-return/` recovers `kms-blank.json` (success after 31.015 s) and `parked.json` (DRM runtime inactive); no module-return checkpoint exists. Thus KMS disable completed and the failure is later, during the recovery-module call, but its first completed hardware operation remains unknown. Pstore contains only the old freezer sample; SRAM is invalid after the owner reset. Do not repeat the recovery module. With display restored, return to the already admitted bounded freezer→devices stack diagnostic on this initially clean boot; existing 30-second PM backstop is required. This diagnostic taint cannot establish clean-image qualification. Other coverage rows, issue mapping and original clean DPM_PREPARED failure remain unchanged.

Archive `40-device-wait-clean-display-return/` returns freezer and devices on that same boot with COMPLETE seq34, no new warning taint or filesystem errors, and working frame completion after both stages. The observer samples no blocked tasks; this does not explain or erase the earlier intermittent hang. Two devices-only diagnostic runs have now returned. Admit all five staged checks and, only if every non-taint check passes, one real 30-second RTC trial with the same exact stack observer and existing backstop. This tests the installed built-in context fix and retains the original failure as an open reliability gate. Explicit diagnostic metadata and unchanged failing clean verdict prevent confusing observer results with production qualification. No PM callback, hardware policy, electrical or firmware mutation is involved. Product sleep remains quarantined; no endurance or release promotion is admitted yet.

Archive `42-observed-stages-rtc-return/`: all five stages and real RTC wake return on boot `22bd28fa...`, observer taint4096 unchanged, COMPLETE seq197. Built-in SPM entries/resumes 1/1, aborts/restore failures zero, wake0x20 with RTC IRQ attribution, 803768 ticks (24.529052734 s), alarm auto-cleared, ext4 errors zero and application restored. Unlike the earlier 04 context-suppression module, this observer only captures task stacks; the installed built-in context path is exercised. This advances only the narrow diagnostic PM/RTC evidence. The original intermittent device failure and warm-display fault remain open; every other coverage row and issue status is unchanged. Archive precedes a normal service reboot specifically to remove the non-unloadable observer. Admit clean identity/taint/display verification, then staged PM and one RTC trial without modules. No endurance or product-quarantine release yet.

The service reboot itself reproduces the earlier warm-start display failure: archive `44-clean-reboot-display-fault/`, boot `7c416e45...`, vblank timeout at 1.026018 s with no diagnostic modules and taint512. The retained journal correctly preserves the previous successful RTC COMPLETE seq197. Do not run qualification on that warned boot or clear taint. Owner hardware restart is requested after archive; next verify clean startup then staged Power wake. Warm-display reliability stays PHYSICAL_FAIL; the source-tested application recovery changes do not fix that driver cause. No release/coverage gate closes.

Physical result: freezer PASS, then devices FAIL by reset. Boot `f350d9dd...` changes to `e1df409f-ab3c-4f0c-b094-7a81d1b142bf`; real suspend/Power trial was never reached. Archive `28b-clean-power-recovered/` preserves retained stage DPM_PREPARED, callback ring ending in successful `11008000.i2c` at 463.348 s, after codec/storage completion. The ring alone does not identify the outstanding task. Backstop was 30 s; RGU raw zero cannot independently attribute reset cause. No current pstore entries survived. Owner's normal screen observation was on the new boot and is not wake proof. This reproduces the earlier unlocalized device-phase problem on clean 02; USB/charging recover after reboot.

Coverage refresh: full PM and clean wake remain PHYSICAL_FAIL/PARTIAL, with all other rows and existing issue mappings unchanged. Admit one diagnostic `pm_test=devices` repeat with a source-matched, read-only blocked-task module, normal UART/display console PM, the existing RAM console and recovery backstop. It changes no MMIO, context ownership, freezer, reservation or protection. Archive before loading; external-module taint is diagnostic only. No real entry or next candidate is admitted until the outstanding wait is identified.

The verbose-entry diagnostic returns on `e1df409f...` (`30-device-wait-return/`), but only captures a transient UART resume/SRCU wait, not the earlier hang. Refine the observer to retain normal entry loglevel and raise verbosity only when the four-second capture fires; exclude idle workers from its bounded task list. Archive `31-before-probe-reboot/` precedes the service reboot needed to replace a non-unloadable module. New boot `e6b85337...` has preexisting WARN taint 512 from DRM startup vblank timeouts (1.026 s and 31.954 s), with subsequent Reborn readiness and screen-off; archive `32-probe-reboot-return/`. Display warm-boot qualification is now explicitly PHYSICAL_FAIL/PARTIAL; retain this separate defect. No clean claim or production admission is possible. Admit the same bounded freezer→devices diagnostic on this explicitly warned boot with expected combined taint 4608, captured before module loading, to localize the outstanding PM wait. No warning/taint is cleared or hidden and the product's refusal guard remains intact. All other coverage gates unchanged.

Owner-installed DEEPSLEEP-FINAL-02 is verified over USB SSH: Linux `5a32683`, Reborn `5a9f758`, root v1.32, boot `f350d9dd-5126-4d89-b8f0-9f09cb1603f7`, initial uptime 46.24 s and taint zero. Archive `26-successor02-initial/` includes the saved 01 export (boot `44c73d7b...`, exact Linux `0c9b78c`) and persistent stage-2/-EIO USB failure logs. On 02 USB is configured, clock gates/restores 1/1, failures zero; charger recognizes SDP and BAT0 is Charging with the unchanged 450000 uA programmed ceiling. This confirms the narrow USB/charging correction, not charge termination, capacity or measured current.

Refresh every sealing-table coverage row: boot/identity/diagnostic retention and USB enumeration/charging advance to CONFIRMED narrowly on 02; CPU/C3 cold-battery, PM/CIRQ/Power/RTC, display/input/audio/storage restoration, radios, product inhibitors, battery/endurance and electrical minimum remain PARTIAL. Physical UART remains UNKNOWN, host/VBUS PHYSICAL_GATE, memory/recovery/security/time/ calibration gates and FM exclusion unchanged. Earlier device-phase wait and poweroff defect stay open. Existing issue mapping/status is unchanged; no closure or milestone promotion is justified by restored transport.

Admit five staged PM checks followed by one bounded Power-wake attempt, with RTC fallback and the existing 30-second recovery backstop. Use normal console PM, no modules, exact source/boot guards, a live maintenance lock and durable product quarantine. Archive before entry, stop on any failure and require a same-boot, taint-zero return; only then admit repetition/RTC/product/endurance. No electrical, memory, partition or firmware change is made at this boundary.

### First successor USB regression and correction admission

Owner installed DEEPSLEEP-FINAL-01 and reports normal Reborn/Wi-Fi operation, but no USB enumeration or charging. Host observes only preloader during flash, then no normal gadget. USB SSH fails. Exact running metadata cannot yet be read; the owner has saved the on-device diagnostic export before a possible reboot. Host evidence is `25-successor-usb-enumeration/`. No suspend test is admitted. Wi-Fi alone cannot recover SSH because production binds its listener to USB.

Source/native cross-owner reproduction identifies an omitted clock handoff: the new childless gate runs before `y2_ccf_usb_claim()`, which previously existed only in MUSB initialization. CCF deliberately refuses to disable an inherited loader clock; gate readback therefore returns -EIO and terminally stops USB. BC1.1 then cannot acquire the PHY, explaining the associated charging symptom. The integrated actual-probe/actual-CCF regression fails on sealed 01. Earlier tests mocked clock-disable as always gating and missed that ownership state. Admit the narrow fix: claim the inherited clock only after the existing verified idle-DMA/digital-recovery preflight and successful PHY mapping, before scheduling the first worker. Failed/partial recovery must retain loader protection. No register sequence, safety mask, charging limit or retry bypass changes.

Every coverage group in the sealing table below retains its classification, except successor USB/charging now has an explicit PHYSICAL FAIL, and successor boot/UI has owner-observed narrow evidence without SSH identity. Full PM, clean wake, cold-battery C3, automatic policy, endurance, electrical minimum, earlier device-phase wait and poweroff remain open. #16/#27/#28/#29/ #31/#32/#33/#34 remain open; historical #30 does not qualify this work. Preserve the failed 01 image/manifest/symbols as evidence. A tested corrective successor is justified by this reproduced regression, not a speculative image per hypothesis. Full candidate checks and coherent new identity precede another owner installation. Preserve Y2DATA, diagnostic export and persistent logs; no autonomous flash, fallback reset, raw storage operation or release promotion.

Correction sealing refresh: Linux `5a32683f1ae9493c6a37bd18af3d131afb04d450` / unchanged Reborn `5a9f7586dd8d80ab5afc16c6a9a7e853e7469aeb` now builds DEEPSLEEP-FINAL-02/root v1.32. 25 targeted tests pass, including the actual CCF/probe regression that fails on 01. Full candidate boundary passes 543 unique production cases (533 container + ten host dependency cases), kernel/config/DT/ modules/QEMU/ARM/ELF and preserving package checks. Every coverage row retains the classifications above: new USB/charging fix still PHYSICAL_PENDING, no clean sleep acceptance. Admit owner-only corrective installation after the saved diagnostic export; retrieve 01's persistent logs/export first on restored SSH, then verify 02 USB/charging before PM. Preserve failed 01 and exact 04 fallback, all data/protected partitions and electrical limits. No issue closure.

### Successor sealing and owner-installation boundary

Read-only issue refresh at the sealing boundary keeps #16/#27/#28/#29/#31/ #32/#33/#34 OPEN and #30 CLOSED; no remote write or closure is warranted. Owner/blueprint scope remains real same-boot sleep with truthful voltage/SOC, preserved Y2DATA/protected partitions and owner-only flashing. Frozen source: Linux `0c9b78c7903182861b84e7d90a536bd30fca295a`, Reborn `5a9f7586dd8d80ab5afc16c6a9a7e853e7469aeb`. Later documentation is not compiled identity. Full build/profile/package checks pass: 542 unique production cases, 332 Reborn workspace cases, strict formatting/Clippy, ARM/kernel/config/DT/ modules/ABI/QEMU and preserving package validation. Exact seven existing 04 firmware inputs were recovered and inventory-verified; no calibration expansion.

Fresh physical archive `24-endurance30-repeat-return/` on installed 04 boot `404ef43c...` adds four RTC returns: 1811.835 s suspended in 1847.315 s elapsed, four expected wakes/no unexpected wakes, 4.050439→4.013964 V, SOC 86→86 with the old elapsed-time defect. Total 14 same-boot diagnostic kernel returns (12 RTC/1 Power/1 USB); external-module taint excludes clean qualification. Every standing coverage group is refreshed here; historical evidence and accepted risks remain separately scoped, with no permanent production waiver:

| Coverage / existing tracking | Current classification and next gate |
| --- | --- |
| Boot/PID1/root/data, diagnostics, SMP; #28/#33 | CONFIRMED installed 04 identity, persistent archive and same-boot diagnostic continuity; PARTIAL successor cold boot/clean identity. |
| CPU/OPP/C1/C2/C3, timers, clocks/PWRAP/pinctrl/I2C; #28 | CONFIRMED narrow retained tests and 56.72% diagnostic C3 after USB detach; PARTIAL successor cold-battery USB veto correction and load/hotplug regression. |
| Watchdog/reset, poweroff, full PM/CIRQ/GIC/wake; #28/#30/#34 | PARTIAL: duplicate context overwrite localized and bounded diagnostic correction repeats. Earlier device-phase wait remains unlocalized; separate user-poweroff panic remains. Clean built-in Power/RTC/repetition required. |
| Display/GPU/backlight, input/Power; #28/#34 | CONFIRMED narrow paused/dark and owner-observed Power return; PARTIAL repeated clean resume, automatic policy and input polling. |
| eMMC/SD/filesystems/layout; #28/#33 | CONFIRMED bounded synced readback after resume and zero ext4 errors; PARTIAL clean successor/endurance/card matrix. No storage layout/raw write change. |
| AFE/I2S/DMA/codec/headphones/analog; #29 | CONFIRMED bounded closed idle PCM/rails and resumed PCM advancement; PARTIAL clean successor/repeated/endurance/precision gates. |
| Battery/charger/thermal/electrical; #28/#30 | PARTIAL: actual voltage decline, provisional SOC, no pack current/capacity/NTC. Reporting fixes tested; full charge/termination and multi-hour consumption unmeasured. Infrastructure/DDRPHY remain retained. |
| USB networking/MTP, host/VBUS; #27/#28/#31/#33 | PARTIAL: 04 reconnect works; new cold-battery gating/event monitor software-validated only. Host/VBUS PHYSICAL_GATE unchanged. |
| Wi-Fi/Bluetooth/firmware/calibration; #31 | PARTIAL: off during trials, firmware provenance preserved; clean resume/on/peer/coexistence gates unchanged. |
| Physical UART/crash capture; #16/#28 | Physical UART UNKNOWN; retained PM and early pstore capture PARTIAL because SRAM is warm-reset-only and prior ramoops has corruption. |
| RAM/recovery/update/rollback/security/services/non-root; #28/#32/#33 | PARTIAL existing gates unchanged. No memory/reservation/partition expansion, backup or recovery waiver. Exact 04 fallback preserved. |
| RTC/time/entropy/identity/privacy; #28/#31/#32 | RTC same-boot delivery/auto-disarm CONFIRMED narrowly on diagnostic 04; PARTIAL clean image/time validity. Use host UTC/BOOTTIME; private logs stay local. |
| FM | CONFIRMED existing scope exclusion. |

Admit sealing one DEEPSLEEP-FINAL-01/root v1.31 BOOTIMG/Y2ROOT candidate and requesting the owner's installation with the preserving scatter. Classification PARTIALLY READY, not release readiness or a <=1% result. The running collection is archived before this boundary. The next smallest gate is clean installed identity/taint zero, staged PM, repeated Power/RTC and automatic/inhibitor checks; then 5/30-minute, two-hour and overnight voltage/residence. Do not load 04 modules on the new kernel or reuse a harness that requires diagnostic taint. No flash, issue closure, push, destructive cleanup or broader hardware authorization.

### Suspend-aware battery observation correction

Before extending the frozen production source, re-reviewed the standing coverage groups against archive `22-endurance30-return/`. Two RTC segments add 595.849 and 595.286 seconds of same-boot sleep, both with the alarm disabled before harness cleanup. USB insertion interrupts the third segment after 487.924 s; all ten actual returns on this boot complete, but the 30-minute drain gate is still incomplete. The repeat has identical scope and protections. CPU/PM/wake/ peripheral/endurance classifications remain PARTIAL for the successor; all other coverage, owner, issue, recovery and release gates above/below are unchanged.

Fresh voltage falls across the two completed RTC segments while daemon SOC stays 86. Source proves SOC receives CLOCK_MONOTONIC, which excludes suspension, and additionally caps an observation interval at 60 seconds. Admit the narrow reporting correction to elapsed BOOTTIME for the existing voltage filter and existing per-minute rate limit, with physical-time regression cases. Do not alter the voltage curve, offsets, rate, thresholds, charge/current/voltage limits, hardware confidence or shutdown grace clock. This makes actual loss visible; it is not electrical improvement and cannot satisfy the overnight target. Update the same unsealed candidate source, rebuild affected artifacts and run the complete final profile before sealing. No second hypothesis candidate, device deployment, flash or readiness promotion is authorized by this audit.

### Coherent successor build admission

Refreshed against current owner scope, newest 04 handoff, source diff and retained hardware before the packaging boundary. Identity/boot/data evidence remains CONFIRMED narrowly; CPU/C1/C2/C3/timers/PWRAP/clocks/USB are PARTIAL for the new image despite native/ARM checks and 56.72% current diagnostic C3. PM/CIRQ/GIC/RTC/ Power are PARTIAL: seven real same-boot returns on corrected-context 04, one attributed Power, five-minute residence, external taint, and an earlier intermittent device-phase wait. Display/input/storage/audio have narrow post- resume functional proof, not endurance acceptance. Battery/charger/thermal and SOC remain PARTIAL: voltage-based estimate, no pack current/capacity/NTC, actual runtime loss and a separately reproduced stale post-resume UI observation. Radios/calibration, physical UART (UNKNOWN), memory/recovery/update/security/ services, time/identity/privacy, host/VBUS (PHYSICAL_GATE), and FM exclusion keep all previous gates. #16/#27/#28/#29/#31/#32/#33/#34 remain open; closed #30 does not qualify this work. No remote closure or external message is warranted.

Admit one source-frozen paired build, identity DEEPSLEEP-FINAL-01/root v1.31, with the coherent CPU-context/CIRQ, filesystem-freeze selection, USB idle, evidence, product ownership/maintenance and Reborn DB/freshness fixes. The software checks precede sealing: full production CPU/PM/peripheral/profile, config/DT/modules/ABI/QEMU/package checks and Reborn fmt/strict clippy/workspace/ ARM. New source currently passes the targeted platform suites and Reborn's 332 workspace tests; final checks bind the committed source pair. This is PARTIALLY READY for building, not physical/release acceptance.

Each product entry also owns the existing bounded one-shot 30-second PM backstop, paused during real SPM sleep; resets remain failures and quarantine the attempt. Bounded wake-count reads refuse a stuck active wake source instead of indefinitely blocking before PM. Protections and electrical limits unchanged.

Use isolated source worktrees so physical evidence and roadmap updates cannot change the compiled identity while building. Seal only BOOTIMG/ANDROID (Y2ROOT), with the established preserving scatter, manifests/hashes and owner handoff; no Y2DATA image or flash. The installed 04 hardware session remains intact. Clean built-in Power/RTC/repeated/auto-sleep and longer endurance still require owner installation and physical evidence. The ongoing segmented 30-minute trial cannot qualify the new image in advance.

### Thirty-minute retained baseline and segmented-suspend admission

`20-idle30-return/` completes 1800.282 s of undisturbed runtime idle on `404ef43c...`: CPU0 C3 56.721%, fresh 4.062963→4.030664 V, SOC 91→85, 77.296 interrupts/s and 136.314 context switches/s. USB/radios absent, screen off, paused, no scanner; diagnostic taint explicit. No full suspend requested. Every standing coverage row retains the classifications below; this advances runtime observation only, not battery capacity/current or deep-sleep endurance.

Admit 1800 s accumulated real suspension using separately bounded <=600-second RTC segments, stopping on the first failure. The installed helper restores the screen between segments, so all awake gaps and RTC wakes must be reported. Pre-cleanup RTC state is captured to separate driver auto-disarm from harness cleanup. No protection, voltage, timer horizon, memory, partition or firmware change. The 2-hour trial depends on reviewing this result. #28/#29/#31/#32/#33/ #34 remain open; no release or owner-flash gate is waived.

### Product sleep implementation and longer observation admission

Archive `17-five-minute-return/` adds a seventh same-boot corrected-context return: six RTC and one Power, six with normal console PM. The latest actual SPM residence is 305.849609375 s, fresh voltage 3.983422→3.950244 V, SOC 76→76, RTC +1/Power +0, COMPLETE/error 0, no ext4 errors. External-module taint and recent-charge relaxation prevent clean release or overnight-drain claims.

Re-reviewed every standing coverage group below: no broader hardware, battery, thermal, charging, RAM, recovery, radio, USB, security or release gate changes. Full PM/Power/RTC stay PARTIAL pending clean successor and repeated Power; the earlier device-phase wait remains open. Admit the missing 30-minute runtime observation with diagnostic taint explicit and no SSH during its counter window.

Admit implementation of the normal delayed product policy with kernel ABI capability, process-owned critical-operation locks, explicit Reborn DB barrier, wakeup-count handshake, persistent failed-attempt quarantine and evidence. Retain the established 600-second PCM wake and 630-second backstop: attributable maintenance returns can sample battery and re-enter with the display/radios still asleep; Power/RTC/other wake fully restores the application. This does not extend blind battery sampling intervals, alter protection or promote the image. Long tests must report accumulated suspend duration and every maintenance wake. Installed 04 remains guarded; one coherent candidate and owner flash are still required for built-in source qualification. No flash or issue closure.

### Admission to bounded suspend-drain measurement

Fresh `15-power-return/` preserves boot `404ef43c...`, six successful actual SPM returns, no abort/restore failure, COMPLETE/error 0, Power child IRQ 24→26 and RTC unchanged at 5. Owner observes normal display return. Five earlier complete RTC wakes include four with normal console suspension. The matching external diagnostic still causes taint 4096; no clean kernel qualification or production readiness is inferred. The immediately preceding early USB reconnect was correctly refused at device prepare and is not a suspend/wake result.

Re-reviewed every coverage group in the table below against these new archives: boot/identity/evidence and narrow storage/audio restoration remain CONFIRMED; CPU/timers/CIRQ/GIC/Power/RTC/full-PM advance to repeatable diagnostic behavior but remain PARTIAL for the new kernel and the earlier intermittent device-phase wait. Display/input have owner Power-return evidence, repeated functional coverage remains PARTIAL. USB cold-boot gating/event changes remain software validated only; radios/firmware, thermal/charging/battery, UART, memory/recovery, update/security/services, time/privacy, host/VBUS and FM keep their prior gates. Existing #28/#29/#31/#32/#33/#34 stay open; historical #30 closure is not a qualification claim. No new hardware/memory/partition or voltage/current scope.

Admit source preparation of the product sleep contract: an explicit database queue barrier after scanner/background quiescence, followed by process-owned operation exclusions. The measured idle database/scanner polling is retained as a separate optimization target; active-work watchdog coverage must survive any blocking-worker change. This admission does not enable automatic suspend on installed 04 or declare an untested successor qualified. Tests must exercise real queued work/transaction refusal and operation ownership, not only strings.

Admit one 310-second RTC trial after battery-only settling, with the same guarded helper, normal console PM, raw voltage/SOC and unchanged protections. Five minutes is a short diagnostic drain observation, not overnight acceptance. Longer observation, repeated Power cycles, clean successor and automatic product sleep remain separate gates. No flash, issue closure or release promotion.

### Current physical suspend failure and upstream correction

The following RTC-only diagnostic on 04 also resets, but its verbose retained console proves duplicate CPU PM entry/exit around SPM. Core syscore PM already owns the context; the platform's second save occurs after CIRQ masks device SPIs and overwrites GIC's sole saved bitmap. Admit the call-site ownership fix and ordered CIRQ replay, with native abort/restore tests and ARM compilation. The matching opt-in diagnostic changes only the nested notification delivery; it retains the first save/final restore and records external-module taint. No hardware register experiment, memory change or new image is involved. All coverage groups below retain their current gates, including Power/RTC, same-boot restoration, peripherals, endurance and release. Product automatic sleep is not enabled on the strength of a source diagnosis.

The first suppressed-nesting comparison reset in the preliminary device phase, before reaching CPU PM: DPM_PREPARED, last ring callback I2C returned success, boot changed to `404ef43c...`. This leaves the context correction untested on hardware. Admit standard console-suspend debugging for the next bounded trial to expose the blocked task; its UART/power effect excludes drain qualification.

The next comparison yields the first complete same-boot real RTC return on `404ef43c...`: original GIC masks restored, COMPLETE/error 0, RTC child IRQ, Reborn return, internal/SD synced readback and PCM playback/stop all observed. This is narrow CONFIRMED diagnostic behavior, with taint 4096 and console debugging, not clean release qualification. All standing coverage groups retain the table's scope and gates; this new evidence advances full PM/RTC from failure-only to PARTIAL. The earlier device-phase wait is unresolved. Admit bounded repeated RTC/Power and five-minute collection with normal UART PM and RAM-only delayed stack retention. Product automatic sleep, clean successor qualification and long endurance remain dependent. No issue/milestone closure.

Boundary review after the first current real entry: all five PM stages pass on clean 04 boot `dbcb3854...`. Real suspend has reset-resume stamp 0x59325253, suspend PCM length 596, devices resumed, then TASKS_THAWED with no following filesystem-thaw or deferred sampler mark. Boot changes to `697282e9...`; this is a failure, not resume. Early-boot PM/pstore archive now has physical proof. The clean five-minute battery window enters C3 55.82% after USB detach, unlike the retained cold battery boot with bit-10 USB veto and zero entries.

The exact installed Linux 6.18.0 also contains the upstream filesystem-freeze selection inversion: value 0 freezes ordinary filesystems. Admit the narrowly scoped, upstream-authored one-line correction (222047f68e / stable b107196729f) with executable policy tests and ARM compilation. It changes no voltage, storage layout, PM hardware ownership or memory reservation. Its relationship to the live stall is still a hypothesis until the bounded stack/timer diagnostic and controlled comparison; no auto-suspend admission follows from source alone.

Re-audit of every coverage group in the standing table below: boot/evidence, CPU/C1/C2/C3/timers, watchdog/reset, input/display/GPU, storage/filesystems, audio/analog, battery/charging/thermal, USB/host, radios/firmware, UART, RAM/recovery/update/security/services, RTC/time/identity and FM retain their listed classification and individual gates. Updated narrow evidence is clean staged PM, post-USB C3 and early retained capture. Full PM, Power/RTC same-boot, electrical/endurance and release remain PARTIAL; physical UART remains UNKNOWN, host remains PHYSICAL_GATE, FM excluded. No issue closure, source-identity reset, candidate build or flash is authorized by this audit itself.

Owner explicitly authorizes retained-evidence recovery, controlled battery-only idle, staged PM and bounded full suspend, matching diagnostics and fixes. No autonomous flash, protected-partition write, voltage/current limit change or protection bypass is authorized. Work starts from integrated POWER-FINAL-04, Linux `5aeba051c428451483402e5874dcf8222afca259`, Reborn `8cd365da5f3454c8e3189df1434b966edbd06575`; current main documentation HEAD `3e562e7` has no subsequent installed implementation. The newest authority is [NEXT-SESSION-HANDOFF](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FNEXT-SESSION-HANDOFF.md), consumed in full; its cleanup job is outside this investigation. Earlier release reports retain historical scope.

Fresh locked SSH proves installed 04/root v1.30, boot `dbcb3854-d028-4882-94aa-cc86b5af091e`, taint zero. Initial uptime 638.83 s. Persistent logs and journals are archived before mutation under ignored `out/deep-sleep-final/evidence/20261007/00-initial/`. Pstore was unmounted; mounting it recovered two ramoops files, including a partly corrupted prior user-poweroff failure/panic. SRAM PM state/ring is absent. The retained long 04 boot has zero C3 entries despite Enabled/budget -1, substantial C2, real declining voltage and a later low-battery shutdown. Exact matching to the owner's six-hour 88-to-30 observation is still being reconstructed; do not substitute the older POWER01 incident. Product requests unconditionally refuse full suspend until qualification; no auto-suspend implementation exists.

All standing coverage rows are refreshed below; grouped rows retain their individual historical evidence and do not promote broader qualification:

| Coverage | Classification / remaining gate |
| --- | --- |
| Boot/PID1/root/data, diagnostics, SMP | CONFIRMED narrow current 04 boot/SSH; PARTIAL repeated cold boot/coherency/release (#28/#33). |
| CPU/OPP/C1/C2/C3, timers, clocks/PWRAP/pinctrl/I2C | CONFIRMED retained bounded UART01 and 02 tests; PARTIAL current 04 C3 regression: enabled but no entries, PERI blocker 0x400 in retained battery rows (#28). |
| Watchdog/reset, poweroff, runtime PM/full suspend/wake | PARTIAL; retained 02 stops after TASKS_THAWED before FILESYSTEMS_THAWED. Current 04 sampler not yet exercised; recovered poweroff panic is a separate defect (#28/#30/#34). |
| Display/GPU/backlight, wheel/navigation/Power | CONFIRMED bounded awake/dark behavior; PARTIAL full-resume/physical Power wake and input polling (#28/#34). |
| eMMC/SD, filesystems and development/production layout | CONFIRMED retained bounded integrity/PM; PARTIAL full-resume I/O and endurance (#28/#33). No raw write or layout change. |
| Native AFE/I2S/DMA/CS43131/headphones/analog | CONFIRMED retained 02 idle-rail fix and narrow S16 playback; PARTIAL exact 04 verification/full resume (#29). |
| Battery/charger/thermal/electrical | PARTIAL; real voltage decline, provisional SOC, no validated pack current/capacity/NTC. Existing safety limits preserved (#28/#30). |
| USB developer logs/network/MTP, host/VBUS | PARTIAL; current configured ECM/SSH works, battery-side USB clock suspected; host/VBUS remains PHYSICAL_GATE (#27/#28/#31/#33). |
| Wi-Fi/Bluetooth, firmware/calibration | PARTIAL; current radio core powered off, saved intent preserved; on/peer/coexistence qualification retained separately (#31). |
| Physical UART/crash capture | UNKNOWN physical UART; PARTIAL ramoops retention with visible bit corruption; SRAM only warm-reset retention (#16/#28). |
| RAM/reservations, recovery, update/rollback/security, services/non-root | PARTIAL existing gates unchanged; no architecture/memory expansion or backup waiver (#28/#32/#33). |
| RTC/time, entropy, identity/privacy | PARTIAL: current wall clock is build-floor, RTC 2022; use boot IDs/monotonic intervals. Raw logs stay private (#28/#31/#32). |
| FM | CONFIRMED existing board scope exclusion. |

GitHub read-only refresh: #16/#27/#28/#29/#31/#32/#33/#34 OPEN, #30 CLOSED. Closed #30 does not establish reliable suspend. No remote status mutation or release promotion is warranted. Admission is PARTIALLY READY: preserve evidence, reproduce 04 clean idle, then stage PM and use its existing sampler for one bounded real entry. Same-boot Power and RTC restoration must precede product auto-suspend and long suspend-drain qualification. See the [deep-sleep investigation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-DEEP-SLEEP-FINAL.md).

## POWER-FINAL-04 integrated baseline — 2026-10-06

`main` now contains POWER-FINAL-03 plus the eleven parallel Platform 1.0 handoff branches and the high-resolution research branch, merged one at a time with 03 winning every collision (code lines each branch added were searched in the result; almost all were already present in adapted form). The merge added only research tools, tests and documentation, so the image is behaviourally identical to 03. POWER-FINAL-04 (Linux `5aeba05`, Reborn `8cd365d`, BOOTIMG `be0f4379…aea4`, Y2ROOT `4fc765b9…8e64`, fallback = the installed POWER-FINAL-02 pair) is the single base to flash and continue from. Production profile 515 cases, 10 skips, 0 failures. Coverage #28-#34 stay PARTIAL; full suspend still fails at the post-thaw stall; no readiness promotion, flash or push.

## USB candidate handoff boundary — 2026-10-04

One preserving USB candidate is sealed at out/y2linux-platform-v1-usb-candidate/. Compiled Linux08019df / Reborn51d477b; BOOTIMG SHA256 b1b9dc1ec000159cb9d9c75327ab6d60aa32f29ffe476ab8450f7850e76fc9c4, Y2ROOT SHA256 cf0a4eccbd30cb556bb28d3ca7d145a8a75e968e24b1fbaf70d31b3dcaed9c52. Package/root/checksum validation and449-record source/license seal pass. The qualification harness adds checked user-partition/SD admission, every before/after hash, process CPU/RSS and actual frequency diagnostics; its6 native guards pass. Later docs/harness revision is explicitly separate from the compiled source pair.

Every standing coverage row retains the preceding software-sealing admission: CONFIRMED bounded UART01 boot/core/display/input/storage/audio/CPU/C1/C2/C3; CONFIRMED retained Baseline02 installed identity only, boot27e6d684…/taint0; PARTIAL new-image/cold-boot/full-suspend/endurance, USB/radio/desktop/performance, power/thermal/electrical/firmware/calibration/backlight/watchdog/wake and RAM/ recovery/update/security/services/time/identity/privacy/release gates (#27/#28/#29/#31/#32/#33/#34); UART crash capture UNKNOWN, host/VBUS PHYSICAL_GATE, FM excluded. MTP adds no block export or protected/memory/charging policy change. USB platform remains MORE_WORK_REQUIRED; all issues stay OPEN remotely.

Shared-lock refusals leave current speed, BEFORE/AFTER throughput and transfer CPU/IRQ/memory unmeasured. No new hardware result is inferred from software checks. Next exact action: owner Download Only of BOOTIMG and ANDROID/Y2ROOT while preserving Y2DATA/protected partitions, then the attached locked transfer harness and desktop/ ten-session/mid-copy/eject/library/playback/PIO acceptance. No flash or push; owner main/parallel subsystem work stays untouched. Full [USB report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-USB.md) and [structured evidence](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-usb.json) retain the scope.

## USB software-qualified candidate sealing admission — 2026-10-04

The source pair Linux 08019df44c8a7fbc249fc49a5a41f7ac906429ba / Reborn 51d477b2f30edfc90418d8d0c3fa5fad8de6f581 builds fresh kernel6.18.0-y2linux-platform-v1-usb, rootv1.22, release1.0.0-usb-candidate.1. 411 production checks (406 pass/5 minimal-host dependency skips with separate 27 filesystem/GIO and3 ALSA checks), 79 focused tests,240 Reborn tests/fmt/clippy, ARM/Cortex-A7/QEMU, config/DT/modules/ ABI/dependencies/inventory/legal checks pass. Final harness guards pass before packaging. No flash/push or physical promotion; detailed [USB report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-USB.md).

Every coverage row is refreshed: boot/display/input/storage/audio/CPU/timers/ clocks/C1/C2/C3 remain CONFIRMED only within retained UART01 bounded proof; installed Baseline02 identity is CONFIRMED by another locked session’s saved receipt, boot27e6d684…/taint0; USB product implementation is SOFTWARE_VALIDATED but USB/desktop/large-transfer/PIO-disabling/ten-session acceptance is PARTIAL #27/#28/#31/#33. Radio/firmware/calibration/thermal/battery/charger/backlight/ watchdog/wake and new-image cold boot/full suspend/endurance remain PARTIAL #28/#29/#31. RAM/reservations/recovery/update/security/services/time/identity/ privacy/release remain PARTIAL #28/#32/#33 with unchanged memory/protected-data contracts; measured MTP memory remains missing. UART crash capture UNKNOWN, host/VBUS PHYSICAL_GATE, FM excluded. Existing issues stay OPEN remotely.

Three further scratch-baseline attempts remain NOT_RUN_DEVICE_LOCK_BUSY. No USB speed, throughput, transfer CPU/IRQ or host discovery result is invented. Proceed to seal only BOOTIMG/Y2ROOT with accepted UART01 fallback, source/legal archives, evidence and the single guarded qualification harness. Y2DATA and all protected partitions remain preserved. Subsequent qualification-only docs/harness revisions are separate from compiled identity. After owner installation, exact-image host/file/library/eject/performance acceptance is the next smallest blocker; verdict MORE_WORK_REQUIRED. Parallel owner-main integration work remains untouched.

## USB candidate freeze: latest retained installed identity — 2026-10-04

The parallel integration review provides a newer retained locked hardware observation: installed Baseline02, Linux 8584ccd8 / Reborn b71b4688, rootv1.21, boot 27e6d684-3794-4490-95db-a489027cd4f4, taint0. The saved Bluetooth identity receipt hash eb2fd0f0377e25c5a848b6aa02e9cabe3bf6af4a2089ed146670d36f6999f07d matches its evidence inventory. USB work still cannot obtain the physical lock; this is retained evidence, not direct new USB observation or CPU cold-boot proof.

Every coverage row in the preceding admission remains unchanged in classification: boot/display/input/storage/audio and C1/C2/C3 retain bounded UART01 CONFIRMED proof; Baseline02 installed identity is CONFIRMED while new cold-boot/full-suspend/ endurance remain PARTIAL #28; USB/radio/desktop/performance remain PARTIAL #27/#28/#31/#33; firmware/calibration/power/electrical/thermal/wake and security/ services/time/RAM/recovery/update/production remain PARTIAL #28/#29/#32/#33; UART crash capture UNKNOWN, host/VBUS PHYSICAL_GATE, FM excluded. The 64 MiB responder bound and unchanged protected partition/memory/charger policy persist.

The first ARM attempt exposed legacy g_cdc module linkage to unexported boot policy symbols; production now uses only configfs for both selections. The kernel build passes. Supervisor restart/unbind and parent-death FD release, and correct space/read-only error receipts are included before final candidate freeze. Resume the same fresh build workspace for the coherent source pair; publish only one final preserving candidate after all software checks. Parallel owner-main planning edits were read for evidence and remain untouched/unmerged. No flash/push/closure.

## USB MTP architecture and candidate-build admission — 2026-10-04

The owner-authorized desktop pass selects MTP + ECM, with disconnected-session ACM + ECM for advanced use. Kernel/root scope changes are now explicit: configfs/ FunctionFS, a bounded pinned C responder, Linux-only user-file views and a narrow PIO progress fix. No MSC, block handoff, filesystem migration, FIFO/memory layout, charging-current or radio-policy change. The [USB report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-USB.md) records rejected alternatives and host/product limits. Source/native tests cover actual responder transfers/descriptors and data-integrity failures; software verification precedes one fresh ARM/package candidate.

All standing coverage rows are refreshed against retained UART01 Linux e9e8d63 / Reborn b71b4688, boot fd955840-35d9-47db-83e0-ff47d6bb2d2b, taint0; fresh access remains refused by the shared nonblocking device lock. The retained receipt remains real hardware authority; new protocol/speed/throughput/host behavior is NOT_RUN.

| Coverage | Classification / remaining gate |
| --- | --- |
| Boot/PID1/internal root, SMP, diagnostics/display/input, eMMC/SD, AFE/headphones | CONFIRMED retained bounded behavior; exact new root/kernel regression remains PHYSICAL_NOT_RUN. |
| CPU/timers/clocks/C1/C2/C3 | CONFIRMED bounded UART01; candidate automatic cold boot/full suspend/endurance remain PARTIAL #28. |
| USB logs/network/transfer and desktop discovery | PARTIAL #27/#28/#31/#33; safe MTP software implementation/tested descriptors, physical composite/desktop/throughput acceptance missing. |
| Wi-Fi/BT/firmware/calibration/thermal/battery/charger/backlight/watchdog/wake | PARTIAL retained scope #28/#29/#31; no new electrical/radio/deep-suspend claim. |
| RAM/reservations/recovery/update/security/services/time/identity/privacy | PARTIAL existing release gates #28/#32/#33; 64 MiB MTP address-space bound added, measured RAM and release qualification pending; memory/reservation map unchanged. |
| Physical UART crash capture; host/VBUS; FM | UNKNOWN crash capture; host/VBUS PHYSICAL_GATE; FM excluded. |

Existing issues remain OPEN and unchanged remotely; no milestone closes. The next smallest boundary is one fresh kernel/Buildroot/Reborn ARM candidate and config/DT/ modules/ABI/source/legal/package checks, only BOOTIMG/Y2ROOT with Y2DATA preserved. Then owner installation enables exact-image desktop, ten-session and integrity/ performance harness acceptance. No flash or push is authorized for this agent.

## USB desktop file-transfer activation audit — 2026-10-04

Owner explicitly authorizes implementation/research/performance and a single preserving candidate on `codex/platform-v1-usb`; no flash or push. Entry source Linux `b5aea93` / Reborn `b71b4688`, isolated sibling worktrees. GitHub #27/#28/#31/ #32/#33/#34 refreshed read-only and remain OPEN; this local branch does not alter parallel work or remote milestone status.

Real hardware authority is retained UART01 Linux `e9e8d63` / Reborn `b71b4688`, boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b`, taint 0: [physical receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md). Fresh access was refused by the shared nonblocking `/tmp/y2-platform-v1-device.lock`; availability is retried in bounded batches. No new physical result is inferred.

| Coverage (all standing rows reviewed) | Classification / boundary |
| --- | --- |
| Boot/PID1/internal root, SMP, diagnostic/display/input, internal eMMC/SD, AFE/headphones | CONFIRMED within retained bounded receipts; new transfer candidate remains untested. No hardware, partition or memory changes authorized by this audit. |
| CPU/timers/clocks/runtime idle | CONFIRMED bounded C1/C2/C3 UART01; Baseline02 cold boot and full-system suspend remain separate PARTIAL gates (#28). |
| USB logs/network/file transfer | PARTIAL (#27/#28/#33). Existing ACM+ECM plus owner-key SFTP has bounded 1 MiB hash proof; no desktop storage function or current throughput proof. Current progress-aware DMA guard is retained pending source/live audit. |
| Radio, firmware/calibration, thermal/battery/charger/backlight/watchdog/wake | PARTIAL in their retained scope (#29/#31/#28); no new radio/electrical/charging claim or current-limit change. |
| RAM/reservations/recovery/update/security/services/time/identity/privacy | PARTIAL in existing release gates (#28/#32/#33); unchanged protected-data/recovery provenance carries forward. |
| Physical UART early-crash capture; host/VBUS; FM | UNKNOWN UART capture; host/VBUS PHYSICAL_GATE; FM remains excluded on this board. |
| Desktop discovery/consumer transfer | MISSING: evaluate MSC, MTP, composite and existing SFTP from current ext4/private-data layout before selecting. Linux desktop plus Windows/macOS requirements and new-image evidence are mandatory limitations. |

Next smallest boundary: choose a file-safe protocol with protected partition exclusion and current endpoint budget; implement typed product/library integration, automated failure tests and bounded current-image scratch baselines. New kernel/ root changes require coherent implementation and one ARM/package candidate before owner installation. Y2DATA is preserved, never reformatted and never concurrently mounted as host block storage. No milestone closure or physical-ready verdict.

## POWER-FINAL-02 pre-candidate audit — 2026-10-05

Evidence since the full-sleep failure, all on installed POWER01 boot c884ae1c with taint zero: the codec rail enable took 2835 ms against a nominal 150 ms, suggesting post-resume timer/interrupt delay in addition to the unresolved cache replay (two `jiffies` notes added, sleep-only). A bounded ABA Wi-Fi comparison (CAM/FAST_PSP/CAM, 180 s, PC USB attached) is confounded by charger phase and shows no `y2-wifi` IRQ change; FAST_PSP raised gateway latency to 100.8 ms maximum, so the CAM default stays. Source changes pending (unbuilt on hardware): DAC idle bias, blocking connectivity supervisor (with child-reaping fix), sleep-only breadcrumbs, audit reset handling, Power screen-off fallback when sleep is gated. Scope is not widened: no new hardware subsystem, memory or production claim. Coverage #28-#34 remain PARTIAL; no readiness promotion, flash, push or issue closure. Candidate-02 needs an owner flash to validate rails, supervisor and the breadcrumbs.

Candidate-02 built and sealed from clean commits (Linux `eb824a6`, Reborn `05af011`, which contain POWER01 `fedc005`/`ccf450a` and USB02 `0cb7792`/`2444e0f`): BOOTIMG `79f0925f...b307`, Y2ROOT `93c1bf99...f147`, preserving scatter identical to POWER01, fallback = the POWER01 pair. Container production profile 511 cases (10 skips, 0 failures), Reborn fmt/clippy/tests, installed ARM 35 modules, ELF 384 files/1411 edges, package/inventory/legal-info pass. Unsigned; no physical acceptance. Docs commit after this seal is not compiled source.

## POWER01 full RTC cache-replay failure — 2026-10-05

The admitted resident sequence completed freezer/devices/platform/processors/core on boot 69d8df3a with valid same-boot, clean filesystem/taint, helper return and zero deep-entry deltas. Exactly one real RTC12/backstop30 trial then reached SPM EINT wake0x20, PCM596, reset return0x59325253 and DEVICES_RESUMING. The codec trace completes supply enable (2835 ms), access/reset and 2 ms delay, and stops at cs_cache_begin without cs_cache_done. Recovery is boot c884ae1c, taint zero, not successful full resume. No automatic retry or Power trial follows.

This narrows the former unmatched codec callback to regcache_sync, not yet its mutex, traversal, I2C clock, DMA or completion instruction. Admit sleep-only retained breadcrumbs at that register-cache lock/traversal and existing I2C clock/transfer/completion boundaries, restricted to this Y2 codec/controller. No new timer, MMIO write, timeout change, arbitrary power control, wake mask, voltage or USB alteration. Keep the board-local idle-bias correction separate from the unexplained full-reset replay stall; a skipped callback cannot alone prove safe subsequent playback. Next owner image must validate idle rails, playback restore and same-boot RTC/Power independently. Coverage #28/#29/#30/ #31/#32/#33/#34 remains PARTIAL; full sleep FAIL, ordinary autosuspend refused. Recovered image identity/source and preserved DATA/USB remain POWER01. Canonical POWER01 seal is unchanged. No flash, push, issue/milestone closure or battery hardware blame follows this diagnosis.

## POWER01 idle audio and supervisor boundary — 2026-10-05

The owner confirms working display and controls on boot 69d8df3a, taint zero. Detached paused/dark/radios-off 300.295 s has 9765 matching DORMANT returns, 62.6446% CPU0 C3, 27.7221% C1, 4.9101% C2 and zero UART/clock restore failures. Direct voltage 4.043627 to 4.036816 V / estimated SOC 83 to 83 is short-window evidence, not endurance or pack current. GPU/display/AFE/CONSYS/MUSB are suspended; the closed PCM's CS43131 remains runtime-active, DAPM Standby, five codec supply references held. Exact Linux 6.18 DAPM source traces this to the codec's upstream idle_bias_on policy. Admit Y2 card-local idle-bias-off using the supported DAPM API, before the core's initial sync, preserving managed PM order, normal stream references, safe disabled headphone pin and existing checked rail/cache callbacks. No direct rail writes, forced runtime suspend, volume change or generic codec policy change. Target stop/start, rails, playback and full-resume remain gates.

Global task births are approximately 0.929/s and SD IRQs 0.962/s. The legacy connectivity shell polls netdev existence every two seconds and spawns sleep and health-check cat/readlink children; bounded ptrace identification precedes a netlink-driven supervisor replacement. Keep single Bluetooth reconnect ownership, calibration exclusivity, wpa action hooks, restart limits and saved radio intent. Do not infer electrical savings from task/IRQ counts. Input GPIO navigation's 50 Hz timer remains hardware-routing-unproved; do not guess EINT or slow input. Current full-suspend entries remain zero; staged tests then one backstopped real trial are still required, ordinary automatic suspend remains refused.

Coverage #28/#29/#30/#31/#32/#33/#34 remains PARTIAL. No milestone/issue closure, new electrical limits, USB transport, partition/memory scope, flash or push. POWER01 package stays sealed; any further built-in repair requires a distinct source-bound candidate after coherent fixes and affected validation.

## POWER01 post-owner-install physical admission — 2026-10-05

The owner installed the reviewed preserving pair and explicitly requested continued checks. Locked USB SSH identifies POWER-FINAL-01, Linux `fedc005ba68b3f5020a45258e38d641aa191b12a`, Reborn `ccf450ac1388228dbd859318a05e13adf667c9aa`, kernel `6.18.0-y2linux-platform-v1-power-final-01`, root v1.27, boot `69d8df3a-1b2d-4c1b-b26b-d744a7859f7a`, taint zero. PWRAP runtime idle slots 5/6/7 read `0x21e:0x48`, readiness one, error zero; the previously zero-address runtime PCM slot defect is corrected on installed hardware. C3 production policy Enabled/budget -1, with active PC charging correctly vetoing entry. USB ECM/MTP is Ready/configured; SDP 500 mA allocation selects the existing 450 mA ceiling, Charging/fault zero, 4.075488 V at the bounded read. No display WARN/flip timeout appears in the captured fresh boot; owner visual confirmation and repeated blank/wake are pending. Sole loaded module is mediatek_drm. Private evidence: ignored `out/platform-v1-power-final/private/post-flash/`.

| Coverage / existing gates | Current classification | Next evidence boundary |
| --- | --- | --- |
| Boot/source/DATA/USB #16/#27/#31/#34 | Exact source pair and ECM/MTP CONFIRMED, preserving package previously validated | Application/display response, real desktop transfer/hash, retained DATA smoke |
| C1/C2/C3, PMIC, DVFS #30 | Correct slots and policy CONFIRMED, warning-free boot; active charge veto works | Matched PC and unplugged 60-second/five-minute windows, actual C3 restoration/residency |
| Display/audio/storage/input #28/#29/#33 | Driver/source availability and fresh boot scanout; full product qualification PARTIAL | Physical controls, rendering/blank/wake, paused/audio device clocks, playback |
| Battery/radios/journal #30/#31/#32 | Safe existing charging and voltage observed; calibrated current/capacity/NTC unknown | PC/wall source/near-full, radio states, cumulative journal, safe longer battery-only windows |
| Full sleep/endurance/release #30/#34 | Previous RTC failure remains OPEN; new-image NOT_RUN | Staged PM first; one bounded backstopped real trial only after prerequisites; same-boot RTC and Power separately |

Admission is PARTIALLY READY for the already authorized bounded physical power pass. No battery-health verdict, milestone closure, electrical/memory change, forced guard bypass or production autosuspend promotion follows from this read. Existing issue statuses remain open. Continue the existing investigation without repeating unchanged source/ROM/recovery provenance. Update evidence after each real boundary; keep main and the owner's USB worktree unchanged.

## Power candidate owner handoff — 2026-10-05

Standing boundary audit repeated before the canonical preserving handoff. Actual installed hardware remains USB02 Linux `0cb7792` / Reborn `2444e0f`, current boot `e043cb75-9d76-4967-b3a6-1a3396a17dd9`, taint 512. The owner confirms the display remains black/frozen after short Power. The incident had a real 3.400268 V orderly shutdown and no proved full starting charge. The final 1800.312 s PC window gained 3.881469 → 3.937500 V / estimated SOC 47 → 58%, source SDP, 450 mA selected, fault zero, CPU0 online, C2 85.7193%, C3 quarantined. Original Reborn/MTP/Bluetooth components and saved Wi-Fi state are restored; ECM/MTP Ready. Raw evidence stays private; seven sanitized windows are retained in [the final power report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-POWER-BATTERY-FINAL.md).

| Coverage / existing gate | Classification at this boundary | Remaining qualification |
| --- | --- | --- |
| Boot, DATA, memory, recovery / #16, #27, #34 | Existing observed geometry retained; new package SOFTWARE_VALIDATED | Owner preserving BOOTIMG/ANDROID install, no-SD and DATA preservation smoke; no memory or partition change |
| CPU, DVFS, C1/C2 / #30 | CONFIRMED bounded old-image behavior; new source built | Warning-free new-image OPP, parking and matching idle checks |
| Runtime C3 / #30 | Concrete zero PMIC-slot defect FIXED_IN_SOURCE; first wall C3 entered; current WARN quarantine respected | New-image slot readback, real battery-only C3 entries/residency and repeat wake integrity |
| Display/GPU / #29, #33 | Owner-visible failure on current boot; first OVL takeover correction SOFTWARE_VALIDATED | Cold/warm display, controls, blank/wake and clean taint on installed pair |
| Full suspend / #30 | PARTIAL, historical RTC FAIL; no same-boot product qualification | Staged PM then separate RTC/Power same-boot wake and subsystem restoration; automatic sleep stays gated |
| Battery/charging / #30 | Real voltage, independent floor, bounded PC/wall gain; current ceiling is not measured current | Near-full hold/recharge, source transitions, controlled safe battery-only endurance; capacity/NTC/shunt unproven |
| USB / #31 | Yesterday's USB02 foundation retained; new isolated receive wait passes 16 MiB desktop round trip | Exact combined candidate desktop/SSH/source/reconnect checks; no transport rollback |
| Radios / #31 | BT off-state notification load reduced in matched live trial; Wi-Fi saved on restored | Disconnected/connected radio matrix and available peer tests; no phantom EINT or power-save claim |
| Audio/storage/input / #28, #29, #31, #33 | Bounded old-image idle states retained; UUID/ADC wait fixes SOFTWARE_VALIDATED | Playback/idle/resume integrity; legitimate 50 Hz GPIO navigation polling remains until routing is proved |
| Diagnostics/journal / #28, #32 | Bounded machine audit and 300 s journal implemented; counter collector measured 0.08886 CPU s/row | Observe actual next-night counters/shutdown reason; no per-second logging or current fiction |
| Release/endurance | SOFTWARE_VALIDATED / PHYSICAL_NOT_RUN for POWER01 | Five-/30-minute, two-hour, then overnight; no Platform 1.0, battery-health or public readiness promotion |

Compiled source is Linux `fedc005ba68b3f5020a45258e38d641aa191b12a` / Reborn `ccf450ac1388228dbd859318a05e13adf667c9aa`. Kernel/modules/config/DT/ABI, 498 production cases (487 pass, eleven locked-host dependency skips all covered by 59 passing native cases), 326 Rust tests, formatting/strict Clippy, installed ARM/QEMU, ELF closure, package/privacy/inventory and source seal pass. Canonical candidate is `out/y2linux-platform-v1-power-final-candidate/`; only BOOTIMG and ANDROID are selected, no DATA payload. Source/license records retain legal-info limitations and owner-local distribution. A later documentation commit does not replace compiled identity. Main and the owner's USB worktree remain unchanged.

Readiness is MORE_WORK_REQUIRED / OWNER_INSTALLATION_NEXT, not milestone closure. No flash, push, external issue mutation, new electrical limit, memory, calibration, recovery or unqualified product autosuspend is authorized by this planning record. The owner already authorized preparation and ongoing physical qualification; only owner installation of the reviewed kernel/root pair is the next external dependency. After confirmation, continue existing measurements, not a new investigation. Current open issues remain open; no GitHub status is promoted without physical acceptance.

## Power candidate build admission — 2026-10-05

Repeat the standing audit before packaging the owner's single preserving power candidate. Fresh locked SSH still identifies installed USB02, boot e043cb75, taint 512, C3 safely Skipped. PC SDP charging remains active at the existing 450 mA ceiling, fault zero, 3.880371 V; original Reborn has been restored. The owner confirms the screen remains frozen after a short Power wake. Current display failure prevents valid target UI, full sleep and endurance qualification; it does not justify bypassing warning or charger safeguards.

| Coverage / existing issue | Evidence and remaining gate |
| --- | --- |
| Battery/charging / #28, #32 | Real overnight 3.400268 V orderly shutdown; original full charge unproved. Detached DCP charging fault with C3 active, five-minute charging PASS with C3 quarantined. Slots 5–7 read as zero and the exact PCM requests 5/6: checked VPROC initialization and charger guard are implemented, target proof remains pending. Limits, capacity and sensor uncertainty stay. |
| CPU/display / #28, #30, #34 | Fresh kernel/modules and 72 affected native CPU/charger cases PASS. First OVL ownership repair passes actual-function fault tests; no owner-installed display/C3 acceptance yet. No OPP, voltage floor, clock masks or memory change. |
| USB/radios/Reborn / #29, #31–#34 | Matched MTP wait 49.76→0 context switches/s and Bluetooth helper approximately 15→0.20/s. MTP 16 MiB upload/download hashes PASS. Reborn full 326 tests, fmt and strict Clippy PASS; new live UI measurements blocked by the inherited DRM failure. Preserve yesterday's USB receive ring/DMA/FIFO/lifecycle and single Bluetooth reconnect owner. |
| Journal/diagnostics / #28, #32 | Five-minute bounded journal and endpoint-only machine audit implemented, observer cost reported separately. No new high-frequency production timer. |
| Full suspend/endurance/release / #16, #27–#34 | Power/RTC same-boot full resume, complete A–J matrix and 30-minute/two-hour endurance remain NOT_RUN on the corrected image. Ordinary full sleep stays refused. No physical/public readiness or issue closure. |

Proceed with the fresh source-bound kernel/DT/modules/ABI, ARM rootfs, production, QEMU and package gates. Deliver BOOTIMG and Y2ROOT only, preserving Y2DATA, fallback and protected partitions. Existing issue states remain open as recorded in admission; no external status change is warranted. The next hardware boundary is owner installation followed by identity/smoke before the same power matrix. Classification: PARTIALLY READY, software candidate preparation authorized; physical power-platform acceptance remains open. No flash, push or main merge.

## Runtime PCM / PMIC-wrapper slot defect — 2026-10-05

Standing audit repeated before the shared CPU/PMIC initialization boundary. The physical USB02 PWRAP readback has slots0/1/2=21e:58/50/48 but slots5/6/7=0:0. The exact unchanged480-word d53dd75c DORMANT PCM contains a request to 10006604 using e2200006/e2200005: the same AP-DVFS slot register used by the normal CPU-voltage request. Exact MT6582 vendor cpufreq initializes all eight addresses to VPROC and identifies slots5/6/7 as SPM idle/sleep. Our driver only initializes those slots in full-suspend prepare; ordinary runtime C3 has never called that prepare. Therefore its autonomous requests can address PMIC CHR_CON0 at zero, bypassing the software regmap write guard and clearing protections/ engine state. This is a concrete source/hardware-readback defect, not a measured PMIC bus trace; the relation to the observed full charger-regulation reset still needs post-fix hardware confirmation.

Admit initialization and readback of slots5/6/7 during existing checked CPU-DVFS prepare, to the verified active VPROC bank and existing1.15V floor only. Never adopt vendor1.05V sleep, flip selector mode, alter arbitration, allow arbitrary PMIC writes, add OPPs or change charger limits. Runtime C3 must fail closed until those slots are initialized; source-bound C1/C2/UART/timer/CIRQ restore remains. Keep conservative active-charger DORMANT veto until charging interaction is qualified. Exact worker/wrapper native fault tests, fresh kernel/ABI/package checks and owner-installed C3/charging proof remain separate gates. Update #28/ #30/#32 coverage as PARTIAL, no issue closure/public readiness/flash/push.

## First display ownership boundary — 2026-10-05

Real USB02 reboot e043cb75 emits first vblank WARN at1.025s, repeated mutex/ commit timeouts, and taint512 gates C3. Good preceding boot e416d48c had live frame IRQs and taint0. Current source parks inherited DSI before DRM binds, clears inherited mutex membership, but never stops inherited OVL before first configuration. OVL config deliberately skips reset when EN remains1 to avoid the documented enabled-reset/SOF deadlock. This leaves the loader's enabled OVL/FIFO state in the first Linux modeset. Admit one localized first-clock ownership fix: with DSI already parked, mask stale OVL IRQs, stop inherited OVL/layers, verify off, then let normal Linux config/start own the pipeline. No live-frame reset, panel timing/rail/PLL change, warning suppression or C3 guard bypass. Native real-function tests and fresh kernel/module build precede one owner candidate; actual warm/cold boot and warning-free C3 remain unproved. This is a source ownership defect and proposed repair, not yet a proved cause of every display failure. The owner subsequently confirmed a frozen screen after a short Power wake, establishing visible failure in this boot. Existing #28/#32/#34 remain open; Platform1.0 PARTIAL. USB/DATA/recovery are preserved.

## Charging/C3 isolation boundary — 2026-10-05

Repeated the standing real-hardware gap audit before changing runtime DORMANT admission. On exact USB02 boot e416d48c, the detached DCP five-minute window started Charging/650000 uA and developed protection fault0x80, loss of HV enable and charger regulation fields, then stopped charging; voltage declined. A fresh boot e043cb75 automatically quarantined C3 after DRM vblank WARN/taint512. With that guard respected, detached DCP charged throughout300.299s:3.701513→3.740185V, no fault, C2 residency64.48%, C3zero. Different boots prevent a definitive C3 causality claim. The next conservative implementation boundary excludes runtime DORMANT while the charger/watchdog requires the AP awake, preserving C1/C2 and all source-backed limits/protections. No PMIC field/voltage/arbitration write is expanded. The exact PMIC-reset mechanism and DRM warm-boot failure remain open; we will retain first failed register evidence instead of clearing a fault.

Full sleep remains unqualified/product-refused; no automatic sleep promotion. Five-minute evidence is not endurance, battery health or electrical current. Yesterday's USB descriptors, queued receive/DMA/FIFO and single lifecycle owner remain unchanged. Platform1.0 PARTIAL; no memory/layout/OPP/DATA changes, flash, push, public promotion or issue closure. Next: affected charger/CPU native tests, matched userspace trials, kernel build, then coherent owner installation if needed.

## Installed USB02 power investigation admission — 2026-10-05

Owner authorizes power forensics, implementation and bounded live experiments, one coherent preserving candidate if needed, no flash/push. The shared nonblocking lease was acquired before SSH. Current and prior overnight source pair is Linux 0cb779267ca90740853dc02695166d75f36faa29 / Reborn 2444e0f65811e688250a8cd069a57dd780b2d6d3: USB-FINAL-02, kernel USB02, root v1.26. Dedicated power worktrees start at this installed pair and retain both the twelve-session integration and yesterday's receive/FIFO/reconnect/MTP/ECM and charging allocation fixes. Main and its preexisting dirty documentation stay.

| Coverage / existing issue | Current real hardware evidence and limit | Next boundary |
| --- | --- | --- |
| Incident / #28/#32 | Prior boot 6f2838c9 records orderly shutdown_complete after voltage reaches 3.400268 V. Retained rows peak at 3.920141 V, full=0. Owner saw 88%; actual preceding full termination is unproved. Clock adjustments require monotonic durations. | Persistent low-rate power journal and separate charge/SOC evidence. No inferred current or battery blame. |
| CPU / #28, historical #30 | Current boot enables C3 budget -1. Quiet PC/Wi-Fi-connected 60.63 s: C1 89.16%, C2/C3 zero; CONN/APDMA/BTIF/USB ownership blocks. Observer uses 1.225 CPU s at endpoints. | Radio-off/detached 60 s and 5 min windows with improved observer accounting, original guards retained. |
| Polling / #31/#32/#34 | MTP io_thread 49.71 switches/s; Reborn main 20.65/s; reconnect main 19.18/s despite BT Off. | Fix source of timed waits and unrelated filesystem notifications, regression-test cancellation, reconnect, transfer, input and shutdown. |
| Charging / #28/#32 | PC SDP actively charging, programmed 450 mA, fault=0, positive voltage trend. Overnight 2 mA USB allowance is neither active charging nor measured pack current. | Preserve current validated 70/450/650 mA and 4.175 V limits; physical wall/full/source tests. |
| Suspend / #28/#32/#34 | Campaign codec/restore fixes present; ordinary deep sleep remains gated. Previous Baseline02 RTC resume FAIL remains history. | Staged PM then one backstopped exact-image real trial; same boot/complete restoration before policy promotion. |
| Storage/USB/audio/display/input | USB02 is authoritative; previous bounded receipts do not qualify new behavior. | Preserve partition/data/native S16/CPU/scanout/USB contracts; targeted source and matched live tests. |
| Endurance/distribution | Optimized 30 min/2 h/overnight and electrical/pack capacity unmeasured. | Safe increasing duration; product status PARTIAL, no milestone/public-release promotion. |

Read-only GitHub refresh retains #16/#27/#28/#29/#31/#32/#33/#34 OPEN. Existing bookmarks cover this task; no external mutation is requested. This admission does not change memory, OPP, charging protections, protected data or recovery.

## Baseline01 physical pause / USB observation boundary — 2026-10-04

Standing audit repeated on actual installed-image receipts before closing this partial test boundary. Compiled Linux98daf3f/Reborn9cd12bae and sealed images are unchanged. Original boot ef2c8f2f/taint0 passes owner/machine smoke, C1 on all four cores, 18 hotplug transitions, all five guarded OPPs/PWRAP readbacks and natural CPU0-only parking/C2 (4,857 entries,85.4572% in60.05534s,restore faults0). Eight fsynced128KiB hash rounds each on DATA/SD after C2 pass. These are bounded CONFIRMED successes, not integrated acceptance or electrical benefit.

| Coverage / retained issue | New real evidence / next smallest boundary |
| --- | --- |
| CPU/idle/timer/parking; #28/#30 | C3 PARTIAL/NOT_QUALIFIED: deliberate USB-off topology wait lasted too long; last durable record budget0/entries0/no armed cycle. Owner confirms restart to recover USB, so changed boot is not proof of C3 crash. Preserve UART01 exact-image C1/C2/C3. Host-only parking-before-detach and180s alarm/cleanup correction passes30 affected tests; no hardware replay. |
| USB/storage/recovery; #27/#28/#33 | Owner reports pre-test post-flash disconnects. Host DHCP profile did not fit static ECM/new interface; verified MAC/static-IP/autoconnect saved and return observed. Physical USB/MTP reconnect remains PARTIAL. No descriptor error in captured host interval. Diagnose exclusively after audio lane finishes. |
| Graphics/boot/policy; #28/#34 | Recovered boot9d4d0245 logs DRM vblank WARNING/flip/commit timeout; C3 policy Skipped/kernel_tainted_or_unknown. Current taint/restore observation awaits lease. Never bypass that safety gate. |
| Full sleep/radios/audio/endurance/distribution; #16/#29/#31/#32/#33 | Baseline02 RTC FAIL remains; new-image Power and RTC independently NOT_RUN. Separate wired-audio lane owns device; no claim about its result. Radio peer/coexistence, MTP, battery/electrical/endurance and firmware/codec/source/collector gates remain open. |

Owner prioritizes finishing the wired-audio test before further USB diagnosis. This session respects its shared lease and makes no device command while held. No new CPU/suspend/transfer stress, production/hardware/memory/OPP/layout change, flash, push, main/public promotion or issue closure. All233feature IDs and retained issue states stay fixed. No unchanged ROM/stock/recovery provenance campaign is repeated. Next stage is partially ready for read-only USB/boot observation once the audio lease is released; integrated acceptance is blocked on those gates. [Physical receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-BASELINE-PHYSICAL.md) and private owner out/platform-v1-physical/baseline-01-smoke-03 retain evidence.[ ## Wired precision evidence correction 

The standing boundary review is repeated for the owner's clarification about physical impossibility. No hardware operation or image change is made. The same retained Baseline01 register/DMA results prove the tested S16 path; exact software24 bytes remain validated. The manual defines two16-bit MON0 fields, not an explicit all-mode internal bus-width maximum. The previous inference from monitor width plus an absent documented fetch selector is insufficient for owner Outcome B. That closure and HARDWARE_PROVEN_UNSUPPORTED verdict are withdrawn; neither A nor B is established. The former boundary below is historical, with its raw measurements retained.

Coverage now separates PROVEN_SOURCE monitor/control definitions, PHYSICALLY_OBSERVED installed S16, SOFTWARE_VALIDATED24 packing, and UNKNOWN wider-memory/AFE transport. I2S/DAC wider reception remains source-backed. Next evidence must establish actual fetch/output representation and a viable route or an explicit exclusion, rather than treating a monitor field as the bus contract. F075 hardware condition returns to pending decision. Original hardware safety restrictions and audio-only scope persist; no new source controls, candidate, flash, radio audit or remote milestone change is admitted. See [the corrected report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-HIGHRES-AUDIO-COMPLETION.md).[ ## Wired high-resolution completion boundary — 2026-10-04 

The standing review is repeated for the owner's one wired-precision task, using the connected Baseline01 rather than promoting unrelated milestones. Selected Linux3f35bc68/Reborn2444e0f6 remain the newest integrated Baseline-final pair; isolated branches preserve the original checkouts. Real installed Linux98daf3f0/Reborn9cd12bae, rootv1.24/kernelBaseline01 were verified before and after the conservative locked audio session. No image was flashed.

| Changed coverage | Closing classification and remaining limit |
| --- | --- |
| DL1 wide fetch | PROVEN_SOURCE hardware-limited16: complete exact MT6582 specification documents two16-bit outputs, no wide fetch selector; PBUF[19:16] is a threshold. |
| I05/I06→O00/O01 | PROVEN_SOURCE route receives16-bit DL1 values; PHYSICALLY_OBSERVED CONN0=0x00400020. Independent width of every AFE internal block is not claimed. |
| Second I2S | PROVEN_SOURCE16/32-word serializer; PHYSICALLY_OBSERVED32-word configuration, not24/32 meaningful DL1 payload. |
| CS43131 | PROVEN_SOURCE16/24/32 receiver; PHYSICALLY_OBSERVED ASP/channel16 and32-bit slots,44.1/48. |
| Decode/DSP/packing | SOFTWARE_VALIDATED exact signed24 in S24/S32 software outputs; full32 FLTP loss remains. Six live S16 ring snapshots match native conversion byte-for-byte. |
| Native formats/rates | PHYSICALLY_OBSERVED S16 stereo44.1/48; direct24/32 rejected, plug downconverts. Wider precision HARDWARE_PROVEN_UNSUPPORTED on DL1;88.2/96 not enabled without a matching clock/rate contract. |
| Device safety/cleanup | Temporary test process/data removed; both observers removed by normal reboot because unloading is disabled; same image, PCM closed, -60dB/headphone off, preexisting taint512 restored, lease released. |
| Physical bit capture | EXTERNAL_CAPTURE_STILL_REQUIRED for independent serial/analog measurements. No wider physical PASS or endurance qualification. |

The previous unknown-width evidence gate is resolved by the complete exact-SoC contract, not by the driver's S16 mask. Outcome B applies to the specified DL1 chain. Native feature F075 remains unimplemented and physically unqualified, but its hardware-conditional admission decision is now explicit. Existing audio issue #29 and remote milestone states remain for owner review; no remote closure or public/platform-wide qualification is performed. The next scoped owner step is review of [the completion record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-HIGHRES-AUDIO-COMPLETION.md), not flashing another S16 image. Existing release/endurance and unrelated subsystem gates are preserved without auditing them again. Source/evidence handoff is READY; no wider native candidate has a supported implementation.[ ## Wired high-resolution completion admission — 2026-10-04T18:56:50.640168+00:00 

The owner authorizes one task: meaningful wired PCM precision on the physical MT6582/CS43131 Y2, with exact-SoC research, conservative live playback, matching read-only diagnostics and one coherent preserving candidate if needed. No flash, push, radio work or unrelated audit. This instruction narrows the standing audit to the changed audio coverage and supersedes the earlier stop at unknown width. Existing audio issue #29 remains open; no remote mutation or milestone closure.

Newest integrated source selected after inspecting both repository histories, branches and worktrees: Linux 3f35bc68e7537bffe356f145dcb35837c9d2e9a6 (Baseline-final descendant of integration de9f26d) and Reborn 2444e0f65811e688250a8cd069a57dd780b2d6d3 (descendant of 9cd12ba). Implementation uses isolated paired codex/highres-audio-completion branches. Original checkouts and their existing documentation changes are preserved.

Initial read-only device identity: kernel 6.18.0-y2linux-platform-v1-baseline-01, root 2025.02.18-platform-v1.24, compiled Linux 98daf3f0220f4a1580bb4893094ee9f0e02362a5, Reborn 9cd12baeeb70b204e08299bd4c91c8c35604c304, boot ef2c8f2f-56d9-418a-b8a8-2dfd329d0973, taint 0. PCM was closed, Master -60 dB/headphone off, native single stereo playback endpoint. Source proves current S16 44.1/48 policy, not a silicon precision ceiling. Current Reborn decode/DSP is FLTP; full32 source low bits can collapse before packing. The prior precision pass's source/stock stub/codec evidence is retained without repeating unchanged ROM/recovery provenance.

| Changed coverage | Classification | Required next evidence |
| --- | --- | --- |
| Native DL1 fetch and packing | UNKNOWN above16; current16 IMPLEMENTED | Exact MT6582 register/packing contract; vendor build selection must prove SoC applicability |
| AFE I05/I06→O00/O01 width | UNKNOWN above16 | Exact wide-field evidence or explicit physical limit |
| Second I2S | 32-slot setting PROVEN_SOURCE; meaningful wide payload UNKNOWN | Payload alignment and width independent of slots |
| CS43131 | 16/24/32 receiver PROVEN_SOURCE | Running word/channel readback during admitted playback |
| Software precision | 24 packing SOFTWARE_VALIDATED in prior integrated pass; arbitrary32 FLTP loss established | Sink/gain/DMA byte comparisons and actual capability negotiation |
| Live qualification | PARTIAL initial identity only | Shared lock is held by another active qualification; acquire before any further device access/test |

Scope readiness: READY for independent exact-SoC research; live work waits for exclusive device access. No register guessing, undocumented clock/power writes, raw sectors, data migration or layout change is admitted. Candidate sealing requires a repeated audio-only boundary audit and relevant broad build/package checks. Physical low-bit success remains unclaimed until observed.

## Baseline01 installed physical admission — 2026-10-04

Owner reports newest preserving firmware installed and authorizes its tests. Read-only pinned USB admission at 18:35 UTC verifies compiled Linux `98daf3f0220f4a1580bb4893094ee9f0e02362a5` / Reborn `9cd12baeeb70b204e08299bd4c91c8c35604c304`, kernel `6.18.0-y2linux-platform-v1-baseline-01`, root `2025.02.18-platform-v1.24`, boot `ef2c8f2f-56d9-418a-b8a8-2dfd329d0973`, taint 0. Standing audit repeated before activating exact-image physical qualification; all 233 feature IDs, source selection, protected partitions, memory and OPP scope, fallback and open issue gates remain unchanged. Owner confirms wheel, display, audible local track and normal battery display, playback now stopped. Root/DATA/SD ext4 and Wi-Fi COMPLETED/DNS are observed Ready. C1 counters advance; C3 boot policy Enabled/-1/disable0 is now observed on the integrated boot, but C2/C3 entry/restore and after-full-resume remain unqualified. Current screen/radio/USB/topology guards correctly report unmet prerequisites.

Retained UART01 C1/C2/C3 remains historical exact-image evidence. Baseline02 RTC watchdog FAIL remains open; persisted sleep restore_failed refers to old boot 27e6d684, not a new trial. Power and RTC full wake are separate NOT_RUN on this image. Battery 4.039 V/estimated 88%, no current sensor: no battery-life claim. Storage/USB desktop, Bluetooth peer, audio fidelity/rates, graphics/input counted controls, endurance and current-image recovery still require scoped tests. Firmware/codec redistribution, source/notices and collector gaps remain open; owner-local testing does not qualify public distribution or close issues.

Next smallest boundary: smoke geometry/kernel/owner gate, then guarded CPU foundation under the shared nonblocking lease and independent pinned Wi-Fi. Stop mutation on identity/boot/taint/restore/storage failure. Broader USB/suspend follows only a passing gate; no flash, reboot loop, push or main promotion. Private admission and campaign receipts: owner `out/platform-v1-physical/`. Readiness: PHYSICAL_QUALIFICATION_IN_PROGRESS, overall acceptance PARTIAL.

## Independent baseline final closure check — 2026-10-04

+ +Before ending the software-seal boundary, retained real hardware and owner scope +were reviewed again against the canonical copy. No hardware evidence changed: +UART01 C1/C2/C3 is source-bound CONFIRMED, integrated physical/endurance remains +NOT_RUN, Baseline02 RTC FAIL stays open, Power/RTC and electrical benefit remain +separate PARTIAL/UNKNOWN gates. All 233 IDs, active issue states, hardware/memory/ +OPP/DATA scope and distribution limits remain as in the preceding audit. No new +build, flash or unchanged ROM/recovery provenance audit is needed for this +receipt-only documentation update. Canonical software/package/source/checksum +verification PASS; next step remains owner-preserving flash and one smoke-first +campaign. No main, public release or physical milestone is promoted. +

## Independent baseline software seal / physical handoff audit — 2026-10-04

Standing boundary audit repeated before canonical baseline promotion, using actual retained hardware receipts rather than integrated source claims. Selected owner source, C01–C34 dispositions and the 233-feature scope remain unchanged. Final compiled pair Linux `98daf3f0220f4a1580bb4893094ee9f0e02362a5` / Reborn `9cd12baeeb70b204e08299bd4c91c8c35604c304` is CONFIRMED by fresh clean build and software/package tests: 475 cases (465 passed, ten native-covered skips), 324 Reborn, 384 ELF files/1411 edges, 106 packages. No runtime correction or expanded hardware, memory, OPP, partition, battery or production subsystem scope was admitted.

Retained real hardware: UART01 e9e8d63/b71b4688, same boot fd955840…/taint 0, C1 WORKING, C2 84.3473%/zero clock restores failed, C3 21 guarded context-loss returns plus 3624 normal entries, total 3647 matching returns/ACK/CIRQ/timer restores and zero faults. Sixteen foundation source files/three idle functions directly match that physical implementation. Automatic new-image policy remains PARTIAL until cold boot and guarded runtime observation. Baseline02 boot 27→88 RTC watchdog recovery is FAIL: DEVICES_RESUMING/wake 0x20/PCM 596/reset 0x59325253, CS43131 resume entry without leave; inner stall UNKNOWN. Power and RTC are separately NOT_RUN on the final baseline. New rollback/substep source is not physical fix evidence. Ordinary product full sleep remains guarded.

Storage/radio/JPEG/DB/performance evidence retains exact earlier image/binary scope; integrated USB desktop, peer/coexistence, controls, wider AFE, recovery, endurance and battery/electrical benefit are PARTIAL / NOT_RUN or UNKNOWN. Firmware/optional codec rights and source/collector limitations remain PARTIAL; public release is NOT_READY, owner-local qualification proceeds separately. Retained issue snapshot #16/#27/#28/#29/#31/#32/#33/#34 OPEN; #30 historical CLOSED does not close full sleep. No remote issue or milestone was changed. No ROM, stock/recovery/source provenance campaign or device connection was repeated.

Next smallest boundary: seal one owner-directory preserving baseline and let the owner flash BOOTIMG+ANDROID only, then run the smoke-first single campaign. Verdict READY_FOR_PLATFORM_V1_PHYSICAL_QUALIFICATION, not physically qualified. No main merge, flash, push or milestone closure. Source/software CONFIRMED; integrated hardware/endurance/public distribution remain open.

## Independent baseline finalization admission — 2026-10-04

Owner authorizes verification/reconciliation, fresh build/software qualification and one preserving owner-local baseline. No device access, flash, main merge, push or public release. Standing audit repeated before finalization/production identity change, using retained real hardware evidence. All eleven paired merge bases equal Linux b5aea937/Reborn b71b4688. Master compiled4c72466/dd73dcc; later tips are documentation-only. Owner dirt and all histories are preserved.

| Coverage / existing issues | Evidence classification / next smallest boundary |
| --- | --- |
| CPU/idle/timers/hotplug/DVFS/PWRAP; #28/#30 | CONFIRMED UART01 e9e8d63/b71 sameboot/taint0: C1 working,C2 84.3473%,C3 65.2450%,3647 reset/resumes,restore faults0.16source files and3idle functions byte-compared with physical source. Integrated cold boot/idle PARTIAL. Preserve qualified once-per-boot CPU0 policy/dynamic guards. |
| Full suspend; #28/#30/#32 | PARTIAL. Baseline02 RTC FAIL: boot27→88 watchdog recovery,DEVICES_RESUMING/wake0x20/PCM596/reset59325253,unmatched CS43131 resume entry7407. New rollback repair/substep notes are not a demonstrated RTC-stall fix. Power/RTC independently NOT_RUN on new source. |
| Storage/USB; #27/#33 | CONFIRMED bounded old modes/hashes/1k scans; selected source has sole Linux filesystem writer. Integrated MTP/replacement/endurance PARTIAL. |
| Radios/audio/media/library; #29/#31/#32/#33 | CONFIRMED software/scoped old metrics; changed BT/peer/coexistence/wider AFE PARTIAL/UNKNOWN. Native S16 stereo44.1/48 only;50k DB measured,250k ceiling unqualified. |
| GPU/input/performance; #28/#34 | CONFIRMED temporary binary/JPEG scope; integrated counted controls/renderer PARTIAL. Preserve scanout/runtimePM. |
| Battery/charging/recovery; #16/#27/#28/#32 | PARTIAL. Safeguards retained; electrical/battery-life/overnight/current-image recovery NOT_RUN. Residency is not battery gain. |
| Distribution/source/notices; #16/#32/#33 | PARTIAL. Firmware/codec permissions and collector/toolchain/local-package limitations unresolved. Owner-local qualification proceeds separately. |

All233feature IDs/layout/OPPs/memory/protectedDATA/calibration scope stays fixed. C01–C34 source dispositions checked against blobs/diffs/contracts. Final identity and smoke-gated single coordinator with separate Power/RTC are needed. Retained issue snapshot: #16/#27/#28/#29/#31/#32/#33/#34 OPEN; #30 historical CLOSED, never full-sleep acceptance. No issue/milestone changed or closed. Next: fresh independent build/package/software, then owner flash and exact-image hardware. Finalization PARTIALLY_READY; no integrated physical promotion.

## Platform 1.0 software exit / physical qualification preparation — 2026-10-04

Repeated standing milestone-boundary audit at 2026-10-04T16:54:14.264292+00:00, before crossing the software-candidate boundary. Explicit owner Platform 1.0 requirements, all233 feature IDs, all eleven frozen paired sources, accepted/rejected C01–C34 changes, all eight current open GitHub issues and actual source-bound hardware receipts are reconciled. Source and software are CONFIRMED; integrated hardware, endurance and distribution remain PARTIAL / NOT_RUN, with conditional wide AFE/audio and peer/backend questions UNKNOWN. No production waiver or milestone closure follows from the software exit.

Exact compiled pair: Linux `4c72466f2f27ddf9f0ca18ba8ddc4d89c52599d2` / Reborn `dd73dcc3243045cd33e319dda2f76918ed37ea31`. Kernel `6.18.0-y2linux-platform-v1-integration-01`, root `2025.02.18-platform-v1.23`. One sealed candidate: `/home/luca/Dokumente/Code/worktrees/platform-v1-integration/Y2Linux/out/y2linux-platform-v1-integration-candidate`. BOOTIMG SHA256 `d2dec1a517a596861adb69b4c9aaab51e68d5caf46712a99dbd8607e9d8fbb06`; Y2ROOT SHA256 `cd3c077fd6c4882c82b7c67c42266f5f0ddc04828ddc2af111434740153bd1dc`. Identity comes from the new manifest, not later documentation HEAD. This audit reads the seal/receipts and does not build, flash, access hardware or repeat unchanged source/stock/recovery provenance.

| Coverage / issue | Real evidence and present gap | Boundary decision |
| --- | --- | --- |
| CPU/idle/timers/hotplug/DVFS; #28/#30 | CONFIRMED bounded UART01: all4 C1, C2 84.3473%, C3 65.2450%,3647 checked returns/zero restore faults/sameboot. Fifteen registered foundation files plus SPM dormant/idle-arm/idle-restore functions byte-preserved. Fresh ARM/config/DT/modules/ABI/software PASS. Integrated cold boot/C3 NOT_RUN. | Protect foundation; exact-RC before/after-sleep regression required. Historical#30 closure is not full-sleep acceptance. |
| Full suspend/product restore; #28/#30/#32 | PARTIAL. Baseline02 boot27 full RTC FAIL, recovered boot88/taint0, retained DEVICES_RESUMING/wake0x20/PCM596/reset59325253, unmatched CS43131 1-0030 phase7. New checked codec/SPM restore and worker ACK guards software PASS; never installed. | No ordinary deep-sleep promotion. One staged/backstopped source-bound trial after owner installation/review; stop on unexpected reboot. |
| Storage/filesystems/USB; #27/#33 | CONFIRMED scoped Baseline02 SD SDR104/direct hash/runtime-PM observations; six private DB trials and fsynced integrity evidence remain exact-scope. New MTP/configfs/PIO/confinement source and software PASS. Real desktop MTP/different-card/newRC NOT_RUN. | Linux sole filesystem writer; no raw block export. PreserveDATA/SD geometry. F134 MTP required; mass-storage/RNDIS absent. |
| Wi-Fi/BT/codec/precision/audio; #29/#31 | PARTIAL. Old Wi-Fi throughput/readiness and S16/44.1/48 observations retained; optimized BT worker never ran with a peer. Q31/S24/S32 conversion software PASS is not wider native AFE output. | Real AP/headset/codec/coexistence/listening remain gates. Native S16-only enablement; wider fetch/I2S/analog evidence conditional. |
| Media/library/DB; #32/#33 | CONFIRMED exact9.0.2 ARM/QEMU parser policy, schema1 TEMP scan/revision/CID/admission/privacy/fault tests. Source-bound50k native benchmark includes ingest/prune regressions;250k is capacity ceiling, not qualified capacity. | One scanner/catalog/worker; retained queues refuse stale cards; zero-FD4-cover cache cannot block eject. Integrated scan/playback/USB/sleep races remain physical gates. |
| Graphics/input/performance; #28/#34 | CONFIRMED bounded temporary069415a ARM evidence on boot88 with stock/data restored;600/6,912,000 pixel-channel differences (near-equivalence), synthetic input excludes mechanical latency. New runtime/input/capture/sleep source324tests/fmt/Clippy PASS. | Preserve DRM/Lima/scanout foundation. Exact-RC counted input/display/latency checks required; no new refresh-rate or cold-boot claim. |
| Battery/charging/boot/shutdown/update/recovery; #16/#27/#28/#32 | PARTIAL. Awake/refusal/recovery evidence retained; no electrical/endurance/newRC full-return qualification. Matching UART01 fallback is sealed separately and preserving scatter selects onlyBOOTIMG/ANDROID. | One owner install and one integratedA–J campaign; existingDATA/protected partitions/stock recovery remain intact. |
| Composition/source/notices/privacy/distribution; #32/#33 | CONFIRMED fresh106-package inventory,384ELFs/1411edges,449source/license records, checksums/root/private-state PASS. Owner firmware redistribution and AAC/aptX/aptX-HD/LDAC approvals unresolved; collector/toolchain/local-license limitations retained, MTP GPL3+ source/notices reviewed as delivery not legal clearance. | Owner-local candidate only; no public distribution waiver. Corresponding-source/notices/permission review remains required. |

All active GitHub issues were refreshed read-only at16:43UTC: #16/#27/#28/#29/ #31/#32/#33/#34 OPEN; #30 historicalCLOSED since2026-09-15. Those states remain appropriate because their physical/product/distribution gates are open. No remote issue mutation, new bookmark or closure is warranted. Existing source- bound failures are preserved. Memory/layout/OPP/protected-data scope is unchanged; the bounded48KiB render cache and4 pixel covers do not enlarge hardware admission. Next phase readiness: READY_FOR_PLATFORM_V1_PHYSICAL_QUALIFICATION as an owner-local software candidate; complete Platform 1.0 remains PARTIAL.

## Platform 1.0 production composition boundary — 2026-10-04

Before creating the integrated release candidate, the master repeats the [standing milestone boundary review](#standing-milestone-boundary-rule). The233-feature target, owner Platform1.0 direction, all eleven frozen paired handoffs, protected Linuxb5aea937/Rebornb71b4688 foundations and C01–C30 are compared with the retained hardware receipts.15:40 read-only discovery confirms all22 owner heads unchanged/clean/stable; isolated integration branches alone contain the selected composition. Source/software readiness is complete for localized units: Reborn324 tests/fmt/strict Clippy and Linux focused contracts pass. Fresh pinned9.0.2 ARM/kernel/DT/modules/ABI/production/package/source/privacy qualification is the next software boundary; no integrated image exists yet.

| Coverage | Current hardware evidence and production gap |
| --- | --- |
| CPU/timers/topology/idle | UART01 exact e9e8d63/b71, bootfd955840/taint0: all-core C1; C2 84.3473%; C3 3,647 checked returns,65.2450%,zero restore failures/same boot. Baseline02 boot88 readback enables automatic C3; exact-RC cold boot/residency and after-full-resume regression remain. |
| Full suspend/power | Baseline02 compiled8584ccd/b71 full RTC trial FAIL: warm recovery to88b85fa3, unmatched CS43131 1-0030 resume entry7407, no COMPLETE/EXIT. Same scratch hashes/ext4 errors0 prove recovery, not resume. New codec rollback/notes, SPM restoration and product quiescence are source/software only; ordinary unqualified full sleep refuses. Charging/offline/electrical/endurance gates remain. |
| Storage/filesystems/USB | Baseline02 passive MMC/SD tuning, DATA+SD1k scans and fsynced scratch hashes are bounded physical passes; same-card reinsertion diskseq2→3 observed. Different-card/FAT/exFAT/absent-boot/desktop/endurance are open. New configfs/MTP exposes files through the sole Linux filesystem owner, never raw writable blocks; sealed USB080 candidate is separate/uninstalled. MTP hardware/Windows/macOS/GNOME/KDE matrix must qualify the integrated image. |
| Radios/codecs | New event-driven Bluetooth and bounded Wi-Fi readiness/power policy have software evidence; Baseline02 Wi-Fi HTTP/DNS and old worker overhead are retained. Real headset/active PCM/reconnect/coexistence, codec hardware and new-policy target execution remain. No old receipt qualifies the new binaries. |
| Wired/highres/media | Native S16 stereo44.1/48 is the proven hardware contract;24/32 and88.2/96 remain conditional on unproven AFE/I2S payload. Software low-bit packing, FD/custom-AVIO metadata, checked JPEG reduction and media limits pass. Physical fidelity/bit capture/formats/endurance remain. |
| DB/Reborn/graphics/input | Baseline02 private native1k/10k/50k DB comparisons and temporary performance069415a binarySHA7871ec67 show bounded improvements, with ingest/prune/cold-list and original two-sample Play/Pause regressions retained. Supplemental32-event replay improves tails; stock/policy/data restored on boot88/taint0. New integration claim/worker/input contracts have software checks; exact-RC UI/controls/KMS/audio/source/eject regressions remain. The input owner's120-second physical window contained zero events, not a counted-button pass. |
| Boot/install/update/recovery | Preserve stock loaders, D08/MMC layouts, data schema1, BOOTIMG+ANDROID preserving update allowlist, independent recovery and paired fallback. No owner tree/main mutation, flash or push. Exact new release identity and package closure must be built/verified before an owner install step is concrete. |
| Release/distribution | One source-bound personalized integration candidate is authorized after composition/software gates. Owner-local firmware remains without established redistribution permission; optional private codecs remain conditional; MTP adds its pinned GPL3+ source/notices obligation. No public release, signing/channel/rollback or endurance gate is waived. |

Production scope now composes the already authorized subsystem implementations: configfs MTP/developer fallback and GPL3+ dependency, sole Linux filesystem owner, ABI/status unions, DB TEMP protocol/revision2, precision membrane, render batching, measured wired pacing and shared suspend gates. F134 must explicitly distinguish implemented MTP from unimplemented mass-storage/RNDIS within its retained feature ID. Layout/reservations/OPPs/physical highres ceilings and private data scope do not expand. Four artwork pixel caches own immutable claims and zero cached file FDs;49152-byte native vertex batch is bounded. Existing queue20k/session8MiB and catalog250k limits remain;50k is the largest native qualification, while250001 SQL-only fixture checks rejection and is no hardware/RSS qualification.

Roadmap/source admission advances to fresh integrated software qualification, with product readiness PARTIAL. Existing #16/#27/#28/#29/#31/#32/#33/#34 are open in the retained GitHub read; historical #30 closure is not a full-sleep pass. No epic/milestone is activated or closed by this composition, so no issue mutation or new hardware authorization is implied. The audit itself is documentation/evidence only: it neither builds/flashes nor repeats unchanged ROM/SPFT/recovery/source provenance. The separately authorized candidate build will run the broad qualification appropriate to production packaging.

## Platform 1.0 integration activation boundary — 2026-10-04

The master reviews all eleven final paired handoffs at immutable observation 20261004T142419.143470Z: every owner tree is clean/stable and retains Linux b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c / Reborn b71b468860233faa0a42b8448ec5777fa952b8e3. Reborn main7f9df397 omits the scanout-release foundation. Source integration is READY_TO_INTEGRATE into new isolated codex/platform-v1-integration branches, as explicitly requested by the owner; no main merge, push or flash. Source selection and complete observed refs, paths, commits, diffs, tests and candidate identities are in the [master status](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-INTEGRATION-STATUS.md) and [C01–C30 plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-INTEGRATION-PLAN.md). Coherent source units enter with immediate targeted validation; shared changes are composed semantically. The weaker performance Bluetooth polling hunk is superseded by the Bluetooth owner's event worker. No owner branch/worktree/index is modified.

This boundary compares the unchanged233-feature product target, explicit owner decisions, repository changes, existing issues and actual retained hardware receipts. It closes no milestone. Firmware, private calibration, protected partitions/Y2DATA, matched fallback/recovery and memory map remain under their established scope; native wider audio stays disabled pending proof.

| Coverage / existing gate | Classification and evidence applicability | Next smallest boundary |
| --- | --- | --- |
| CPU, five OPPs, timers/hotplug, C1/C2/C3; #28/#30 | CONFIRMED bounded UART01: C2 84.3473%, C3 65.2450%,3,647 returns/same boot/zero restore faults. Installed Baseline02 automatic C3 readback Enabled/-1/disable0 is observed, not new-image/cold-boot/endurance qualification. | Preserve all idle/UART/timer/dynamic guards and shared restoration; fresh integrated kernel/config/DT/modules/ABI and current-image C-state regression. |
| Full suspend/resume, power; #30/#32/#34 | FAIL for installed Baseline02 one-shot full RTC resume. Boot27e6d684 changes to88b85fa3; retained DEVICES_RESUMING/wake0x20/PCM596/resetstamp59325253 has no complete/exit and unmatched CS43131 1-0030 resume entry. Decoded RGU reset cause/RTC-child attribution not retained. New suspend/codec rollback notes are software validated, PHYSICAL_NOT_RUN. | Compose handshake/input/source quiescence, retain ordinary sleep qualification refusal, then one exact-RC same-boot campaign. Reboot direct scratch hashes/ext4 errors0 prove recovery only. |
| Storage/filesystems/USB; #27/#28/#33 | CONFIRMED bounded old Baseline02 mode/read/hash/reinsert and stock1k scan receipts; new claims/FD pinning/MTP code software validated, PHYSICAL_NOT_RUN. USB08019df subsystem image is uninstalled and not master RC. | One diskseq/mount/CID authority, pinned regular file/sidecar lifetime including collection art C30, durable USB generation/eject and targeted native confinement/filesystem tests. |
| Wi-Fi/Bluetooth/codecs; #31 | PARTIAL. Baseline02 throughput/readiness/off-worker observations retained; changed policy/event worker and real peer codecs/coexistence lack final-image physical evidence. No headset currently available. | Union socket/control wake, diagnostics/status contracts and owner workers; exact-RC association/transfer/peer qualification later. |
| Wired precision/FFmpeg/library; #29/#33 | PARTIAL. Native S16 stereo44.1/48 remains admitted; software meaningful-bit fixtures, media parsing and DB scan/durability pass separately. Native50k DB benchmark measured on private Baseline02 scratch;250k catalog capacity not physically qualified. | One paired C/Rust ABI, DB-owned TEMP scan protocol plus metadata_revision, safe legacy UUID/CID upgrade and queue refusal; compose precision/FD-pinned playback/ALSA pacing. |
| Graphics/input/Reborn responsiveness; #34/#28 | CONFIRMED bounded owner app069415a temporary ARM SHA7871ec67 on Baseline02 boot88/taint0: playing87.95→11.21% one core/audio82.63→5.11%, wheel59.93→17.52ms, supplemental16resume/pause p95 improvements; stock/data/policy restored, no hard kill/xruns. Ten pixel captures near-equivalent600/6,912,000channels max5/255, not byte identity; synthetic evdev excludes mechanical timing. Counted physical input remains NOT_RUN. | One event loop/watchdog/catalog/art worker; canonical kernel_mono_us/input cancellation/Power shutdown confirmation, stale observation/sleep guards and integrated rendering regression. |
| Battery/charging/boot/shutdown/update/recovery; #16/#27/#28/#32 | PARTIAL. Existing policy/fallback and bounded awake/charging refusal evidence retained. No integrated image, full-resume/representative endurance/electrical acceptance yet. | Preserve rescue/developer observer, intent/checkpoint and low-battery control; fresh broad software/package then exact-RC physical conditions. |
| Distribution/source/notices/privacy; #16/#32/#33 | PARTIAL. Existing owner-local verified radio provision is available; redistribution permission remains unestablished, private calibration excluded and codec/source collector limits persist. New MTP GPL3+ dependencies must be inventoried. | One freshly built source-bound candidate; complete installed dependency/capability/source/notices/private-state and paired fallback checks. No release permission follows from a clean merge. |

Issue state from the retained read-only2026-10-04 refresh: #16/#27/#28/#29/#31/ #32/#33/#34 OPEN; historical#30 CLOSED since2026-09-15. No external epic/status change is warranted at this source activation boundary; historical#30 closure cannot qualify the later failed physical full resume. No new bookmark is needed. No external issue/comment mutation is performed. The integration phase is PARTIALLY READY for software work; physical/endurance/distribution remain gates. This audit itself builds/flashes nothing and does not repeat unchanged source, ROM or recovery provenance. A fresh broad build/package qualification is required after the selected source pair is integrated, before sealing one RC.

## Platform 1.0 parallel integration observation — 2026-10-04

Owner authorizes master integration review of all independent sessions, followed by dedicated integration branches only after selected owners finish. This is the documentation/observation boundary, not subsystem implementation, integration activation, a new hardware campaign or milestone closure. Linux foundation is `b5aea937a3b8e3e8ec398f8cb2e04656b8a53f8c`; Reborn foundation is `b71b468860233faa0a42b8448ec5777fa952b8e3`. Reborn `main` is still `7f9df397ab3809d52e2f1073ca93a305246e0c3a`; its missing scanout-release commit must be preserved in the integration foundation. Eleven paired subsystem trees are discovered; historical candidate trees and missing `/tmp` registrations remain separate. No owner worktree or Git ref is changed by this review.

Real evidence is the retained [UART01 receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md), the [Baseline02 seal](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md), and the newly written Bluetooth/Wi-Fi owner receipts in their independent worktrees, indexed by the [master status](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-INTEGRATION-STATUS.md). Those new locked observations identify installed Baseline02, compiled Linux `8584ccd8` / Reborn `b71b4688`, root v1.21, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0. This supersedes the older awaiting-installation identity statement only. It is not a fresh master device read, automatic cold-boot/C3 qualification, or acceptance of changed binaries.

| Coverage / existing gate | Classification and next boundary |
| --- | --- |
| CPU/timers/C1/C2/C3; #28/#30 | CONFIRMED in bounded UART01 scope: C2 84.3473%, C3 65.2450%, 3,647 checked returns, same boot and zero restore failures. Preserve exact guards, timer/UART/clock/context ownership, boot policy and five OPPs. Current integrated-image and endurance acceptance remain PARTIAL. |
| Storage/USB/connectivity; #27/#28/#31/#33 | PARTIAL. Live filesystem identity, USB MTP/export/eject, Wi-Fi wake loop and Bluetooth observer changes overlap; reconcile contracts and repeat affected tests on a frozen source pair. Actual peer audio remains unqualified; owner reports no headset currently available. |
| Audio/media/database/graphics/input; #29/#32/#34 | PARTIAL. Four branches change native media code; two independently replace incremental scanning; input and suspend change the same Power router. Stronger final evidence and owner-specific responsibility must decide semantic integration. |
| Full system sleep/power; #30/#32/#34 | PARTIAL. Suspend changes shared SPM code and Reborn wake/prepare contracts; protect idle restoration. Full same-boot RTC/Power wake, electrical battery evidence and endurance remain independent gates. |
| Release/distribution/security; #16/#32/#33 | PARTIAL. No integrated candidate exists. Existing source/notices, owner firmware, private calibration and optional codec distribution restrictions persist; preserve-data/fallback/recovery are mandatory. |

Existing owner receipts report #28/#31/#34 OPEN after read-only refresh. The master has made no external status update and closes no epic. Refresh this audit and the roadmap again immediately before actual integration, any material scope change, candidate sealing and qualification/release boundaries. The next smallest blocker is reproducible final owner handoffs plus semantic reconciliation, not a general CPU redesign. See [integration plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-INTEGRATION-PLAN.md) and [master](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-MASTER.md). This review builds/flashes nothing and does not repeat unchanged source/ROM/recovery provenance.

Later owner RTC full-sleep evidence on the same installed Baseline02 is FAIL: watchdog recovery changes boot `27e6d684` to `88b85fa3-2282-4d93-b0b8-818a105ddd0a`, taint 0; retained journal stops at DEVICES_RESUMING (wake 0x20, full PCM 596, reset stamp 0x59325253), with no complete/exit proof. Direct scratch hashes and zero ext4 counters after reboot prove recovery only. New suspend source was not installed. Preserve prior UART01 C1/C2/C3 evidence; full resume and automatic C3 remain separate gates. Master archives the raw failure receipts offline and neither repeats the trial nor closes any milestone. Review the source-bound owner handoff before integration.

Read-only GitHub refresh on 2026-10-04 confirms #16/#27/#28/#29/#31/#32/#33/#34 OPEN and historical #30 CLOSED since 2026-09-15. That planning closure does not qualify physical full resume; the new failed RTC receipt keeps this release gate open. No external issue state or comment was changed by master.

## Storage Platform 1.0 closing audit — 2026-10-04

This boundary reviews the owner's isolated storage pass before local handoff. Actual installed Baseline02 is Linux `8584ccd85f052f351fe51650b2348c83ca894ed4`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0. Final locked hardware receipts record clean scratch cleanup, mounted ext4 SD at SDR104, eMMC HS200, both clocks gated, zero PM mismatch/error and unchanged transport fault counters. The non-blocking lease was released normally before the reserved suspend lane; that lane's later qualification is separate from this pass. New source remains uninstalled: Linux implementation `2a603c1`, Reborn source identity `ee1c25a` and playback/sidecar guard `f726ae4`. Affected Reborn app38/platform77/library28/ media22 plus architecture guards, denied-warning Clippy and pinned ARM build pass; final ARM ELF/dependency and QEMU pinned image pixels pass as emulation. See the [storage report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-STORAGE.md) and [compact physical/software receipt](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-storage-20261004.json).

| Coverage / existing gate | Closing classification and smallest remaining boundary |
| --- | --- |
| eMMC / #28, #33 | CONFIRMED bounded HS200 read/write/fsync/SHA/PM. Direct read 98.717 MB/s, guarded write 26.800; retain HS200. Mounted-root DDR52/HS52 renegotiation and repeated cold boots remain untested. |
| SD / #28, #33 | CONFIRMED bounded one-card SDR104/DDR50/SDR50/HS, 4 GiB top-rung direct reads without CRC/timeouts; retain current ladder. Candidate3 failures remain historical, superseded only for installed later pads/card selection and this card. Card/temperature/endurance matrix remains PARTIAL. |
| Filesystems/media / #32, #33 | CONFIRMED installed ext4 fsync/hash/eject/same-card reinsert and host scratch FAT32 Unicode/dirty-bit refusal/ext4/exFAT no-write checks. Paired stable claims/CID sources, dirty-mount gate and pinned playback admission are software-tested. Different-card/FAT/exFAT/large-file target acceptance remains PARTIAL. |
| Music/scanning / #29, #32, #33 | CONFIRMED stock 1,000-file physical corpus on both volumes: all hashes match, initial scans 5.526/5.495 s, all incremental rows reused, zero failures/controller deltas. New app/native source guard still requires matching deployment and target acceptance; SQLite ownership remains separate. |
| CPU idle / #28, #34 | CONFIRMED storage clock gating/retention and clear MSDC blocker bits; retain UART01 actual C2/C3/hash evidence. This USB/radio four-core boot has no new C2/C3 entries; intended-workload regression remains PARTIAL. No masks weakened. |
| Suspend/power / #30, #34 | PARTIAL in this storage pass; no full sleep, electrical durability or power-loss claim. Reserved independent suspend lane owns its actual results. |
| Release/security/boot/USB/radio/GPU / #16, #27–#29, #31–#34 | Existing scope retained; localized tests/config/DT/modules/ABI/offline BOOTIMG pass. No new paired release installation or broader acceptance, backup/calibration waiver or unchanged ROM/recovery recapture. |

Fresh read-only GitHub refresh keeps #16/#27/#28/#29/#31/#32/#33/#34 OPEN and #30 CLOSED. No status mutation or milestone closure is warranted. Existing recovery/fallback, Y2DATA/protected partition, memory, supplies and firmware obligations remain unchanged. Final classification is PARTIALLY READY: local source/report handoff is ready, general Platform 1.0 qualification is not. Next boundary is paired Linux/Reborn/native integration with explicit source-key migration/media admission, then owner-supported repeated/absent boot, second-card and physical filesystem matrix. Do not infer hardware authorization from this planning row. No flash, push, autoformat, raw write or mounted-media reset.

## Storage playback-source guard audit — 2026-10-04

Final paired-source review finds C19's saved queue contains old Track snapshots, and `Runtime::load` checks only whether a pathname exists. SourceChanged pauses an unavailable current track, but a later manual resume or queued decoder can reopen a same-named file on a different card. The validated CID-qualified source must be checked at decoder admission, with pinned source directory and regular file descriptors so mountpoint/file-entry replacement cannot redirect the open. Reject symlinks and subordinate mounts while walking relative components; retain the pins through native close. Extension-free file-FD header probing requires direct-versus-pinned metadata/PCM tests across all valid fixtures; sidecar admission uses the same regular-file and pinned-parent boundary. Review found the local artwork loader selects codecs by suffix, so extension-free sidecar FDs need a bounded 12-byte JPEG/PNG/RIFF-WebP signature fallback. Preserve existing named-file behavior, image limits, codecs/protocols and native ABI; validate identical direct/pinned pixels and affected native tests. The app must ship its matching native media library; old installed binaries remain unchanged.

This is within the owner's storage coordination for playback/media replacement and #32/#33; it does not change SQLite, FFmpeg/native ABI, DSP, sink configuration, MMC modes or memory/idle policy. Installed physical hotplug remains bounded old- source evidence; the new paired guard requires host fault tests, app/platform checks and ARM build, then later target acceptance. No old queues are rebound to unproven cards. Update the [storage report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-STORAGE.md) before closing this review; no broader release/milestone acceptance is inferred.

## Storage removable-mount gate audit — 2026-10-04

A source review during the authorized filesystem pass found that `y2-media mount` identifies the card but does not run the existing read-only checker. The owned-host FAT32 test proves that a dirty clean-unmount bit produces a nonzero `fsck.fat -n` result without changing the image. Current physical media is clean ext4, with successful explicit `e2fsck -f -n` and remove/reinsert; no dirty user media is created. Adopt a bounded read-only preflight before SD mounts, reject checker faults/timeouts/source changes, and leave automatic repair/formatting disabled. Internal root/data boot gates stay unchanged.

This is a localized production-admission change within #32/#33, not hardware, memory or filesystem-format expansion. Read-only checks may delay mounts or refuse media requiring journal recovery; that availability limit must remain visible. Existing MT6582 modes, fallback, runtime PM and C2/C3 guards remain unchanged. Paired claim/source-ID changes still require Linux/Reborn integration; new source is software-tested, not installed by this pass. Proceed with focused media/checker tests and update [the receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-STORAGE.md).

## Storage Platform 1.0 optimization admission — 2026-10-04

Owner requests an isolated storage/filesystem pass from Linux `b5aea93` and Reborn `b71b4688` on `codex/platform-v1-storage`; no main-worktree edits, flash or push. This narrow review precedes implementation and physical measurement. Retained hardware authority: candidate3's 200 MHz SD data CRCs and clean bounded 100 MHz reads ([SD characterization](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-SD-SDR104-DIAG.md)); UART01's clean eMMC/SD SHA256 after real C2/C3 returns ([physical receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md)). Candidate4's stock pad/card-driver changes are included in current source, but its original receipt is software-only. A read-only identity probe saw Baseline02 running at HS200 and SDR104 with zero counters, boot `27e6d684-3794-4490-95db-a489027cd4f4`; the lock acquisition raced another session, so no qualification is claimed from that probe and all further physical access requires the non-blocking device lock.

| Coverage / existing gate | Admission classification and next evidence |
| --- | --- |
| eMMC / #28, #33 | CONFIRMED bounded HS200 negotiation/readback and post-idle integrity; PARTIAL sustained writes/fsync/performance/repeated boot |
| SD / #28, #33 | PARTIAL: older 200 MHz CRC failures retained; candidate4/later pad and driver selection must be reconciled before choosing a production ceiling |
| Filesystems/media / #32, #33 | PARTIAL ext4 physical evidence, FAT/exFAT source support; inode/ctime mount claims disagree with stable diskseq inventory and require a paired Reborn fix |
| CPU idle / #28, #34 | CONFIRMED bounded C1/C2/C3 UART01; preserve every blocker mask; collect passive storage regression on installed Baseline02 |
| Suspend/endurance/release / #30, #32, #34 | PARTIAL; full sleep/repeated boot/card matrix/endurance remain independent physical gates |

Read-only GitHub refresh: #16/#27/#28/#29/#31/#32/#33/#34 OPEN, #30 CLOSED; no external status mutation or milestone closure. Preserve storage addressing, Y2DATA, recovery/backup/calibration obligations, exact fallback, memory map, regulators and idle guards. No raw writes, autoformat, mounted-media reset or SQLite optimization. Proceed with the smallest justified source fixes, targeted regressions and safe scratch measurement; owner is available for SD interaction. Final decisions and unobserved gates belong in [the storage report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-STORAGE.md).

## Wi-Fi optimization source closing audit — 2026-10-04

Scoped source pass closes on Linux `7056977` / Reborn `2cdb9cc`; physical acceptance remains PARTIAL, with no phase/milestone promotion. Latest Wi-Fi-owned device receipt is Baseline02 boot `27e6d684…`, taint 0 before/after baseline. GitHub #28/#31/#34 refreshed read-only at closing, all OPEN. Exact results and sanitized receipt: [Wi-Fi optimization](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-WIFI-OPTIMIZATION.md).

| Coverage | Classification | Evidence / next boundary |
| --- | --- | --- |
| WPA2, lease, route, DNS and local TCP/file integrity, #31 | CONFIRMED, bounded baseline | Association 0.829–2.545 s, IP 2.676–5.877 s; platform-ready 27.987–32.241 s. HTTP RX 43.941–44.922 / TX 46.376–46.942 Mb/s, four 8 MiB hashes pass. One iperf TX control reset retained. |
| Readiness and truthful telemetry, #31 | Source regressions CONFIRMED; physical after PARTIAL | New-lease DNS scheduling, event wake, measured observation deadlines, redundant RSSI/list/policy reduction, current-peer Online proof and reviewed diagnostics fixed. 94 Linux + 6 diagnostic + 5 layout checks; 74 Reborn platform tests and native/ARM builds pass. |
| Idle power, C1/C2/C3, #28/#31 | PARTIAL, current comparison; retained CPU scope unchanged | Screen-off associated/off CPU 11.222/9.905% of one core, IRQ 289.23/277.98 per second; four cores/1300 MHz/USB confound admission. C2/C3 zero in both windows. Exact wakeups/electrical power not measured; no guards or clock/frequency policy changed. |
| Scanning, power save and playback/coexistence, #31 | PARTIAL / NOT_TESTED | Explicit scan source tests pass; physical scan absent. Temporary PSP sample changed back to CAM and is invalid. Owner's headset unavailable; connected/SBC and local-playback combinations untested. Conservative automatic CAM retained. |
| Integrated Platform 1.0 acceptance | PARTIAL | Two 15-minute after retry windows could not acquire the shared device lock; no RAM after-service ran. Shared USB/Wi-Fi service wait needs C01 reconciliation. No driver/checksum changes, flash, push, merge, main-worktree edits or release qualification. |

Next smallest boundary is an available lock for the exact integrated readiness, DHCP action and Reborn after sweep, preserving USB control wake and supplicant socket wake. Isolate the iperf reset, then AP-loss/cold-boot/power/coexistence coverage. No source-test result substitutes for those physical gates. Retained recovery, memory, packaging, calibration and distribution boundaries stand.

## Wi-Fi Platform 1.0 optimization admission — 2026-10-04

Owner authorizes isolated `codex/platform-v1-wifi` worktrees, bounded shared-lock Wi-Fi tests, localized fixes and regression checks; no flash, push, parallel branch merge, memory/partition change or Bluetooth redesign. Starting source: Linux `b5aea93`, Reborn `b71b468`. Read-only USB SSH under nonblocking `/tmp/y2-platform-v1-device.lock` observes installed Baseline02, kernel `6.18.0-y2linux-baseline-02`, compiled Linux `8584ccd`, Reborn `b71b468`, root v1.21, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0. This supersedes the earlier awaiting-installation statement for identity only; this read does not qualify all Baseline02 cold-boot or CPU gates. Current lease, route and DNS are ready, automatic policy requests CAM/off, screen is blank. Release inventory agrees with compiled source. GitHub #28/#31/#34 refreshed read-only, all OPEN; no remote status mutation or milestone closure.

| Coverage | Classification | Evidence / remaining boundary |
| --- | --- | --- |
| Wi-Fi/WPA2/IP/DNS/TCP, #31 | CONFIRMED, bounded retained transfers; PARTIAL, optimization | Retained receive 45.15–45.60 / transmit 46.35–46.56 Mb/s; disabled checksum offload preserved. Measure current idle/readiness/transfer behavior before selecting fixes. |
| CPU C1/C2/C3, #28 | CONFIRMED, retained UART01 scope; PARTIAL, current-image admission | Existing checked returns carry forward; inspect current radio blockers without relaxing guards or initiating dormant trials. |
| Screen off and coexistence, #31/#34 | PARTIAL | Existing awake/display behavior retained; Wi-Fi idle/power-save and actual peer/SBC coverage require bounded evidence. |
| Release/endurance/electrical power | PARTIAL | No current optimization acceptance, battery savings or practical hardware ceiling claimed. Full suspend, endurance and distribution retain independent gates. |

Next smallest boundary: capture current baseline and exact power-mode semantics, fix only demonstrated polling/readiness deficiencies, then repeat affected tests and bounded measurements with reversible RAM-only tools. Association, DHCP, route and successful DNS remain separate; unknown status never becomes a real disconnect. See [optimization report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-WIFI-OPTIMIZATION.md) for the eventual closing receipt. Existing recovery, calibration, source and ROM provenance is unchanged and is not recaptured.

## Bluetooth optimization admission — 2026-10-04

Owner explicitly authorizes the Bluetooth implementation/research pass in isolated `codex/platform-v1-bluetooth` worktrees from Linux `b5aea93` / Reborn `b71b468`. Read-only locked SSH identifies installed Baseline02, Linux `8584ccd8`, Reborn `b71b4688`, kernel `6.18.0-y2linux-baseline-02`, root v1.21, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0. This supersedes the *installed identity* in the older UART01 receipt; it does not constitute the separate Baseline02 cold-boot/C3 qualification. Retained UART01 C1/C2/C3 evidence remains bounded to its own image/boot. No headset is available, as confirmed by the owner.

F102/F103/F104 and #31 remain PARTIAL: the controller/BlueZ/BlueALSA are observable; peer pairing, audio, reconnect and endurance cannot be promoted by this pass. F105/F108/F229 retain peer/audio/coexistence evidence gates. #28/#31/#34 remain OPEN on read-only GitHub refresh. Idle measurement with Bluetooth off shows 50.37 Reborn Bluetooth thread context switches/s and repeated 2s BlueZ snapshots; these justify localized event/wakeup fixes, not a new kernel power architecture.

Proceed with signal-based observation, bounded-intent/recovery fixes, private-bus regressions, ARM userspace builds and temporary, restored runtime tests only when the nonblocking shared device lock is held. Preserve one reconnect owner and FFmpeg → shared DSP → final sink conversion → BlueALSA. No memory, firmware, calibration, protected storage, image packaging, flash, push, merge, release or milestone closure. The next acceptance boundary remains actual peer/audio and coexistence measurements on the final integrated artifact. Findings and final classification: [Bluetooth optimization receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-BLUETOOTH-OPTIMIZATION.md).

## Bluetooth optimization closing evidence — 2026-10-04

The [implementation receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-BLUETOOTH-OPTIMIZATION.md) records Baseline02 same-boot locked radio/idle samples, zero CONSYS/BTIF idle IRQ increments and zero transport errors/recoveries. Software fixes remove 20ms Reborn polling/2s enumeration, eliminate the committed-intent 30s delay, preserve bond/owner/uncertainty correctness and repair observed discovery JSON. Native private-bus/ARM contracts and 238 Reborn tests/fmt/clippy pass. No changed binary ran on the Y2: the shared lock remained occupied on subsequent attempts.

Controller/idle behavior remains narrow CONFIRMED/PARTIAL; F103/F104/F105/F108/ F229 and M5 #31 remain PARTIAL or UNTESTED at their peer/audio/endurance boundary. No headset is available. Source improvements are not physical CPU/battery or reconnect results; Baseline02 automatic C3 cold boot is not qualified by this pass. Recommendation is MORE_WORK_REQUIRED, with matched changed-binary idle and actual peer/SBC/screen-off/coexistence testing as the next boundary. No milestone/epic closure or release promotion; #28/#31/#34 remain OPEN. Hardware/memory/firmware/ calibration/protected-data/package scope is unchanged; no flash/push or repeat of unchanged ROM/recovery provenance.

## Wired precision source boundary — 2026-10-04

Source-only review correction: the complete diagram now includes live VolumeRamp after FFmpeg integer packing, with f64 gain and a second nearest/ties-away integer quantizer. Unity-volume low-bit fixture proof is not proof for non-unity gain; the membrane CPU benchmark excludes that live gain and ALSA pacing. Exact accepted frames alone advance ramp/offset, including zero/partial writes. This correction uses retained source/tests, does not repeat builds or device access, changes no implementation/policy or hardware admission, and keeps all coverage gates below.

The isolated completion pass reaches MORE_HARDWARE_EVIDENCE_REQUIRED, not a high-resolution milestone closure. Exact MT6582 BSP, retained Y2 HAL/kernel and CS43131 receiver research are reconciled in the [precision report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-HIGHRES-AUDIO.md). Latest available locked hardware read identifies installed Baseline02 Linux 8584ccd8 / Reborn b71b4688, boot27e6d684-3794-4490-95db-a489027cd4f4, taint0, direct S16 44100/48000 constraints and suspended idle AFE. Later non-blocking device-lock attempts remain unavailable; fresh playback and A7 CPU measurements are NOT_RUN. No substitute physical result is inferred.

| Coverage / existing epic | Reconciled evidence | Next boundary |
| --- | --- | --- |
| Wired audio; #29 | CONFIRMED admitted S16 scope / PARTIAL wider precision; stock fetch/connection width APIs are ENOSYS, DAC independently accepts32 | Exact MT6582 wide fetch/interconnect programming, then low-bit I2S capture; source and compiled diagnostics are not installed hardware proof. |
| CPU/timers/idle/storage; #28/#33 | CONFIRMED retained bounded scope / PARTIAL broader qualification | Preserve architecture/memory/storage; collect locked A7 audio CPU costs when available. |
| Bluetooth/Wi-Fi/USB; #31/#27 | PARTIAL, concurrent isolated owners | No branch integration or radio qualification promotion. |
| GPU/display; #34 | CONFIRMED awake scope / PARTIAL full suspend | Preserve existing policy; no screen-off audio or full-resume claim from this pass. |
| Production/release; #16/#32 | PARTIAL | Localized config/DT/module/ABI/package-source checks pass; no new installed/sealed release or milestone closure. |

Software24 WAV/FLAC low bits survive final S24/S32 buffers at44100/48000; general full32 input loses bits in FLTP. Saturating ties-even narrowing and truthful kernel/platform diagnostics are implemented. Six audio/clock/DT tests, 19 localized source checks,241 Reborn workspace tests, fmt/clippy, ARM build, 32 ARM media/ALSA QEMU tests and16 ARM ALSA query intersections pass. Issues #16/#27/#28/#29/#31/#32/#33/#34 were refreshed read-only and remain OPEN; the evidence warrants no remote status change. Source handoff is ready, native wider admission remains blocked by exact silicon evidence. Backup/calibration, protected storage, power and release gates retain their existing obligations. No flash, push, merge, MMIO write, source/ROM rehash or production-scope expansion.

## Wired precision completion admission — 2026-10-04

Owner explicitly authorizes isolated source implementation, exact MT6582/stock research and bounded locked physical audio tests; no flash, push or merge. Linux starts at b5aea93, Reborn at b71b468, on dedicated `codex/platform-v1-highres-audio` worktrees. Read-only device admission under `/tmp/y2-platform-v1-device.lock` observes installed Baseline02 kernel, boot 27e6d684-3794-4490-95db-a489027cd4f4, taint 0 and idle Y2Audio. Exact direct constraint intersections admit only S16_LE stereo 44100/48000; S24_LE/S32_LE and 88200/96000 are rejected. This is driver admission evidence, not silicon maximum or low-bit proof. Raw receipt: out/highres-audio/validation/device-admission.txt. Retained UART01 and native headphone evidence remains authoritative for its bounded tests; new-image general CPU qualification is outside this pass.

| Coverage | Classification | Boundary |
| --- | --- | --- |
| Native wired audio; #29 | CONFIRMED S16 narrow scope / PARTIAL wider precision | Exact DL1/interconnect evidence must precede wider register or ALSA enablement. |
| CPU/timers/idle/storage; #28/#33 | CONFIRMED retained bounded scope / PARTIAL wider qualification | Preserve architecture, memory and partition layout. |
| Bluetooth/Wi-Fi/USB; #31 | PARTIAL | Concurrent isolated sessions own radio changes; no branch integration. |
| GPU/display; #34 | CONFIRMED awake scope / PARTIAL full suspend | Preserve existing screen/runtime-PM behavior. |
| Production/release; #32 | PARTIAL | No release or milestone closure; source/ROM/recovery provenance unchanged. |

Open issues #16/#27/#28/#29/#31/#32/#33/#34 refreshed read-only. No remote status change is warranted or authorized. High-resolution implementation is ready only after exact fetch/packing/interconnect documentation or stock programming establishes every meaningful bit. If unavailable, retain the safe S16 contract and publish the unresolved hardware boundary without claiming a 16-bit silicon ceiling. Next: exact vendor source and targeted stock analysis, software low-bit fixtures, truthful diagnostics and locked baseline tests.

Bounded S16 test admission: a second locked read verifies the installed Linux 8584ccd85f052f351fe51650b2348c83ca894ed4 / Reborn b71b468, same Baseline02 boot/taint 0, suspended AFE, no PCM owner and headphone disabled at -60 dB. Exact stock HAL width/fetch functions return -ENOSYS; mixed-tree ASoC wide fields are unselected by its MT6582 defconfig and lack compatibility proof. No wider mode is admitted. New kernel diagnostics and S24 software rounding are host/ARM compiled, not installed. Ready for bounded existing S16 DMA/rate/runtime-PM observation and offline three-format A7 CPU measurements under one non-blocking device lock. No source/memory/production scope expansion.

## Media stock physical receipt reconciliation — 2026-10-04

Before closing this documentation addendum, repeat the boundary review with the new real-hardware receipts supplied by the separate storage owner. This lane reads retained files only; no device access, build, flash, source change or repeat of unchanged ROM/recovery provenance. The owner's next device slot is reserved for suspend qualification, and is not taken by the media lane.

The storage receipts identify Baseline02 Linux `8584ccd8`, Reborn `b71b4688`, kernel `6.18.0-y2linux-baseline-02`, rootfs `2025.02.18-platform-v1.21`, boot `27e6d684-3794-4490-95db-a489027cd4f4`, closing taint 0. Stock scanner harness SHA256 `16e64c9ebd4139b0324a39d15e6d1bfdb57986f926e3e013d4a55c6db36400f0` uses the installed old media membrane and an isolated DB. One 1000-file mixed-corpus run per volume: DATA/HS200 initial 5526 ms, incremental 393 ms, peak 10656 KiB; SD/ext4/SDR104 initial 5495 ms, incremental 401 ms, peak 10936 KiB. Each initial scan indexes 1000/zero failures; each rescan reuses all
  - Storage controller fault deltas remain zero during write/fsync, read/SHA

and scans; known scratch is cleaned. Original receipts are private storage `out/platform-v1-storage/{emmc,sd}-corpus.json` and `corpus-restored.stdout`, with hashes and summaries in the [media receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FREBORN-PLATFORM-V1-FFMPEG-METADATA.md).

This supersedes “physical stock mixed scan unmeasured,” not the candidate's NOT_RUN gate. #29/#32/#33 now have CONFIRMED bounded physical stock scan/reuse evidence and CONFIRMED candidate software evidence; new-candidate physical scan/concurrent playback remains UNTESTED. The prior closing review's other coverage rows, eight OPEN epics, backup/calibration/fallback obligations and independent audio/radio/core/release gates carry forward. No epic closure, production waiver or hardware scope promotion. Software integration remains READY_WITH_LIMITATION; the smallest next gap is the matched candidate's SD and concurrent playback receipt after the reserved device work. Existing planning does not authorize installation or flash.

## FFmpeg, metadata and library software closing review — 2026-10-04

Repeat the standing boundary review before closing this owner-authorized software subpass. Reborn `a22107c` + `43a695c` on the isolated media branch preserve the direct FFmpeg/float-DSP/sink architecture and add bounded inspection, correct extraction, bounded artwork and lean incremental ingestion. Linux changes are planning documentation only. The [media receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FREBORN-PLATFORM-V1-FFMPEG-METADATA.md) and checked-in measurements distinguish host/ARM/QEMU results from hardware. The blueprint and owner scope exclude flash, push, production installation, kernel/partition/memory-layout changes and interference with parallel radio/audio work. The app and its extended private native ABI must be built/packaged together.

Real-hardware evidence remains retained [UART01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md): Linux `e9e8d63`, Reborn `b71b4688`, boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b`, taint 0, bounded playback/storage and C1/C2/C3. [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) supplies the exact software SDK used here; its retained document is not this candidate's cold-boot receipt. Device-lock admission was nonblocking and busy; this lane performed no device operation. The parallel storage owner's SDR104 report is separate, not media-candidate throughput qualification. No unchanged ROM/recovery/source provenance is repeated.

| Coverage / existing epic | Classification at this boundary | Evidence / next smallest gap |
| --- | --- | --- |
| Boot/observation/USB, #16/#27/#28 | CONFIRMED bounded retained scope; PARTIAL production acceptance | Carry UART01 boot/logging and recovery controls; no new image or protected-area operation |
| CPU/timers/memory/core platform, #28 | CONFIRMED bounded retained C1/C2/C3; PARTIAL wider power/endurance | No memory layout or kernel change; full suspend, wake and electrical measurements retain their gates |
| Audio, #29 | CONFIRMED retained bounded playback; PARTIAL physical candidate acceptance | Fresh decoder/float DSP/sink fixtures pass; analog/native high-rate work belongs to its lane |
| Metadata/artwork/ingest, #29/#32 | CONFIRMED software scope; PARTIAL physical workload | 252 host tests, ARM build, 32+30 QEMU tests, six fresh daemon checks, malformed fixtures and native sanitizer ownership stress pass |
| Large-library scan/RAM, #32/#33 | CONFIRMED measured host/ARM-emulation scope; UNTESTED candidate physical SD | Host 10k median initial 7408→1084 ms, incremental 191→130 ms, peak 66488→53720 KiB; QEMU is not hardware timing/RAM |
| Storage/source lifecycle, #33 | CONFIRMED software guards; PARTIAL physical candidate workload | Existing source UUID/mount checks, SQL failure/recovery and complete-source pruning retained; size/mtime identity limitations explicit |
| Wi-Fi/Bluetooth, #31 | PARTIAL, independent owner lane | No new radio availability/coexistence/endurance claim from media tests |
| GPU/display/input, #34/#28 | CONFIRMED retained awake/bounded scope; PARTIAL resume/endurance | Artwork runs on its existing worker; no display/input driver or physical visual claim |
| Updates/security/release, #32/#33 | PARTIAL | Native local-only policy and matched ABI checks pass; installed-image/recovery/calibration/backups and public release gates remain independent |

All active issues #16/#27/#28/#29/#31/#32/#33/#34 were refreshed read-only and remain OPEN. No external epic closure or production waiver is appropriate. The next software phase is READY for integration with explicit limitations; the next hardware boundary is PARTIALLY READY, requiring a matched candidate, guarded SD scan and concurrent playback under the shared lock. No planning epic is hardware authorization. Existing backup/calibration/fallback and protected storage obligations carry forward. Verdict: PLATFORM_V1_READY_WITH_LIMITATION for this software subpass, not whole-platform milestone acceptance. Updating the audit/roadmap closes the software evidence task only; this documentation review itself performs no build, flash or hardware test.

## Metadata cache revision boundary — 2026-10-04

The media pass found that existing indexed rows otherwise retain the old AIFF artist mapping, album-artist alias behavior and Opus duration after extractor corrections. Before this localized database extension, repeat the standing review against retained [UART01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) and [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) evidence. Hardware coverage and image identities remain as recorded in this pass's admission; new code is host/ARM/QEMU qualified only. The shared physical device lock is busy with separate storage qualification, so no physical access occurs here. The owner's parallel SDR104 result is separate evidence, not a measured media-pass result.

Add one default-zero per-file extractor revision column, retaining public SQLite schema/user_version 1 and all existing row IDs/columns. Old rows reparse once; successful rows record the revision, and malformed rows cannot force the rest of the source to reparse forever. No raw artwork/tag corpus is stored, no SQLite architecture replacement, data reset, hardware, memory-layout, partition or package change is authorized or performed. The owner explicitly authorized metadata correctness and incremental ingestion; this is necessary cache invalidation within that scope. Validate migration, one-time reparse and subsequent reuse, alongside the requested final software checks. #29/#32 remain PARTIAL for media acceptance pending the final receipt; #16/#27/#28/#31/#33/#34 retain their independent OPEN gates after read-only refresh. No external status mutation, release waiver, provenance repetition, flash or push.

## FFmpeg, metadata and library pass admission — 2026-10-04

Owner explicitly authorizes the Reborn Platform 1.0 media pass in isolated `codex/platform-v1-ffmpeg-metadata` worktrees. Entry source: Reborn `b71b4688`, Linux `b5aea93`. Preserve file → FFmpeg → media abstractions → float DSP → sink conversion; no engine replacement, kernel/hardware/partition change, flash or push. Parallel radio and wired-audio work remains separate.

Retained [UART01 real hardware evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) identifies Linux `e9e8d63`, Reborn `b71b4688`, boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b`, taint 0. It proves bounded playback, storage and C1/C2/C3 behavior; it does not measure large-library metadata throughput. [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) provides ARM/QEMU/software evidence, not new-image cold-boot acceptance. GitHub #29 and #32 refreshed read-only: OPEN; stale historical issue text does not supersede retained newer hardware receipts. No external issue status change is authorized or needed for this software subpass.

| Coverage / gate | Classification | Next evidence boundary |
| --- | --- | --- |
| Direct FFmpeg local playback, #29 | CONFIRMED, bounded installed scope | Preserve decoder/DSP behavior; fixture and ARM/QEMU regressions |
| Metadata correctness, artwork, ingest, #29/#32 | PARTIAL, existing source and narrow fixtures | Measure current actual scan; repair demonstrated bugs and bound resource use |
| Large-library throughput and RAM, #32 | UNTESTED for this pass | Reproducible 100/1k/10k host mixed fixtures and representative ARM checks |
| Physical SD scan performance, #29/#32 | UNTESTED | Optional bounded device test only with nonblocking shared lock; QEMU is not hardware timing |
| Release/cold boot/suspend/battery, #28/#31/#34 | PARTIAL, independent gates | Carry existing limitations; no milestone closure or production waiver |

The software pass is ready to proceed. The smallest blocker is missing measured metadata/scan evidence, not hardware authorization from a planning epic. Existing backup/calibration/fallback, memory layout and production obligations remain. This documentation audit performs no build/device test or provenance repetition.

## Library/database bounded native Y2 closure — 2026-10-04

This closing review supersedes only the earlier library target NOT_RUN label. Actual installed Baseline02 is Linux `8584ccd85f052f351fe51650b2348c83ca894ed4`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, kernel `6.18.0-y2linux-baseline-02`, root `2025.02.18-platform-v1.21`, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0. MemTotal 951824 KiB; Y2DATA rw ext4/eMMC. All six private native before/after runs (1k/10k/50k) preserve boot, taint and exact mount generation. The read-only observer after optimized scan 14 reads ext4 errors_count 0 on DATA, SD and root. Driver exits 0 after descriptor-relative owned DATA/SD fixture and temporary binary cleanup; shared device lock released normally. Installed app/database and storage modes are unchanged. No flash, push, service change or production database replacement.

The 50k fixture uses 25k files on DATA + 25k on SD, all SQLite databases on DATA; capacity admission includes bytes/inodes/reserves. The stock filesystem inode limit prevents a safe single-volume 50k fixture; no resize/format is authorized. 1k/10k use only DATA. 50k after artifact is Reborn `c161404`; before is archived `b71b468` production code with current benchmark-only adapters. Transfers are SHA256-verified; checked-in sanitized results retain artifact identity and all median/p95/worst samples. See [Reborn evidence/report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FREBORN-PLATFORM-V1-LIBRARY-DB.md). The target lacks `/proc/self/io`; target write bytes are unavailable, not zero.

| Coverage / existing epic | Classification | Evidence and next boundary |
| --- | --- | --- |
| SQLite/library; #32 | CONFIRMED, bounded host + native Y2 through 50k | Native unchanged scan 25.47 → 3.85 s, mixed 25.73 → 3.87 s, complete catalog 8.64 → 1.00 s. Songs 64-row page 1.79 → 1.59 ms. Initial ingest 17.53 → 18.53 s and prune 85.50 → 155.21 ms regress and are retained. |
| Memory/navigation; #32/#34 | CONFIRMED process footprint and cached model; PARTIAL rendered UI | Native 50k peak 49.72 → 38.68 MiB, DB 21.617 → 20.457 MiB; no-op scan preserves resident/cache identity. Cold Songs row construction remains ~179 ms, queue 20k ~131 ms; actual frame/simultaneous playback gate remains separate. |
| Transactions/durability/media; #28/#32/#33 | CONFIRMED host fault behavior; PARTIAL electrical/paired identity integration | 251 workspace tests/fmt/Clippy and production Cortex-A7 ARM build pass. Real SQLite FULL, killed transaction, restart, migration/row/media faults retain usable library. Schema v1/indexes, WAL/NORMAL, 64-row writes and single worker preserved. Storage SourceID/playback guard and FFmpeg revision must integrate separately. |
| Storage/installation; #28/#33 | CONFIRMED narrow mounted scratch behavior; PARTIAL endurance/power loss | Root/DATA/SD errors 0 and same boot/mount checks; no production changes or physical removal during this DB run. Electrical power loss, endurance and install/rollback gates unchanged. |
| CPU/radio/audio/GPU/release; #28/#29/#31/#34 | PARTIAL, independent gates unchanged | This userspace benchmark does not qualify Baseline02 whole-image/cold boot, CPU/suspend, audio codecs, radio restoration, rendered frames, battery or release. Retained UART01 hardware authority remains scoped to its original receipt. |

All active issues/epics refreshed read-only 2026-10-04: #16/#27/#28/#29/#31/#32/#33/#34 remain OPEN. Existing coverage owners and retained failures remain; no external issue or milestone status is changed. Protected partitions, hardware/memory layout, recovery/calibration and standing installation decisions are unchanged. No unchanged ROM/recovery provenance, package or kernel checks are repeated.

The localized library/database pass is ready for source integration, with measured regressions and current 20k queue/8 MiB session limits explicit. The next smallest boundary is combining the separate storage and FFmpeg commits, resolving source ownership/reuse revision interactions, then targeted integration checks. This is not whole Platform 1.0 closure or authorization for flash/push.

## Library 50k split-fixture admission — 2026-10-04

Locked read-only admission confirms installed Baseline02: Linux `8584ccd85f052f351fe51650b2348c83ca894ed4`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, kernel `6.18.0-y2linux-baseline-02`, root `2025.02.18-platform-v1.21`, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0. Y2DATA is rw ext4 on mmcblk0p7, 770.6 MiB, errors_count 0; RAM MemTotal 951824 KiB. Standalone private before/after 1k and 10k library runs pass. This is not full Baseline02 cold-boot/CPU/platform qualification.

The first 50k-file attempt failed with remote status 1 and cleaned its owned scratch; that wrapper failed to retain stderr, so its exact failing syscall is unknown. The storage owner reports only ~51071 free Y2DATA inodes and ~31982 on the current 512 MiB SD ext4 filesystem. 50k files plus ~2084 release directories cannot safely fit on either filesystem. Do not resize/format/mount/remap anything. This is a fixture capacity boundary, not permission to change production storage.

Proceed, after the queued live session releases the same device lock, with a bounded 50k collection split into 25k new private files on Y2DATA and 25k on SD. Keep all SQLite databases on Y2DATA. Pin both scratch directory descriptors, check bytes/inodes/reserve and mount/boot identity, clean only newly owned dirs. No existing media, installed app/DB, SD mode, services or hardware controls change. The separate storage physical sequence is finished and restored SDR104/HS200. Core media-removal/identity fault qualification remains separate; fixture sources are synthetic and benchmark exact mount generation is checked by the parent. The Reborn report must label this two-source layout and missing target I/O counters (`/proc/self/io` is absent), rather than claiming zero flash writes. Existing #28/#31/#32/#34 remain OPEN; no whole-platform acceptance is promoted.

## Library/database host validation boundary — 2026-10-04

Repeat the admission audit before recording this local software result. Reborn `b0b114e` implements bounded fingerprint/presence scans and coherent keyset catalog loads; `9152005` preserves instrumentation-only baseline reproduction, `eca41fc` covers UUID-less CID compatibility. Schema v1, persistent indexes, WAL/NORMAL, 64-row write transactions, single worker, protected/data/memory-layout and installed images remain unchanged. The cache target is explicit 2 MiB; no new RAM layout.

Retained real hardware authority remains UART01 Linux `e9e8d63` / Reborn `b71b468`, boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b`, taint 0. No new-image or physical performance pass is inferred from host timing. Baseline02 cold-boot qualification remains PHYSICAL_NOT_RUN. #28/#31/#32/#34 refreshed read-only again 2026-10-04: all OPEN; no external milestone/epic changes or new issue required.

| Coverage | Classification | Result / next boundary |
| --- | --- | --- |
| Reborn SQLite/library; #32 | CONFIRMED host software, PARTIAL target performance | 100/1k/10k/50k actual schema/scanner fixtures, 250 workspace tests/fmt/Clippy and Cortex-A7 ARM build pass; 50k rescan 1185→189 ms, catalog 399→40 ms, peak process RSS 168→113 MiB on host |
| Durability/media; #28/#32 | CONFIRMED host fault behavior, PARTIAL electrical/physical | Real SQLite FULL, killed transaction, restart before prune, migration/row/media faults retain usable records; no electrical power-loss or physical SD qualification here |
| Y2DATA/storage | CONFIRMED retained UART01 bounded scope; target DB benchmark NOT_RUN | Parallel storage session retains device lock during owner removal/reinsert confirmation; do not remove its lock or touch its SD state |
| Release/suspend/endurance; #28/#31/#34 | PARTIAL, unchanged | Exact-image/new-boot, full suspend, wider endurance, battery and release gates remain separate |

The [Reborn pass record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FREBORN-PLATFORM-V1-LIBRARY-DB.md) and checked-in host samples retain median/p95/worst and observed regressions. The next smallest gate is locked scratch-only Y2DATA before/after timing/memory, without flash, production database or installed binary replacement. Source-ID producer changes belong to storage; library accepts legacy, UUID-less CID and UUID+CID IDs without auto-rebinding old queue snapshots to unproven cards. No unchanged ROM/recovery/source provenance, package or kernel qualification is repeated. This records software readiness, not whole Platform 1.0 closure.

## Library/database performance pass admission — 2026-10-04

Owner authorizes isolated host profiling and bounded scratch-only Y2 tests for Reborn SQLite/library Platform 1.0. Reborn base `b71b468860233faa0a42b8448ec5777fa952b8e3`; Linux base `b5aea93`. Separate `codex/platform-v1-library-db` worktrees preserve main trees. FFmpeg metadata parsing belongs to another session. No flash, push, production database replacement, kernel change or milestone closure is authorized.

Retained real hardware authority is [UART01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md): Linux `e9e8d63`, Reborn `b71b468`, boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b`, taint 0, bounded C1/C2/C3 and storage integrity pass. Baseline02 new-image/cold-boot qualification remains PHYSICAL_NOT_RUN. GitHub #28/#31/#32/#34 refreshed read-only 2026-10-04: all OPEN. No external status changes are needed for this localized pass.

| Coverage | Classification | Next evidence boundary |
| --- | --- | --- |
| Library/schema/query behavior; #32 | PARTIAL | Reproducible 100/1k/10k/50k host workloads, scan faults and ARM build; locked scratch Y2 timings where available |
| Y2DATA/eMMC/storage; #28/#32 | CONFIRMED bounded UART01; PARTIAL endurance/power-loss | Preserve ext4 data and volume identity contracts; no destructive durability experiments |
| Memory/navigation | PARTIAL | Remove scan-wide duplicate metadata; measure 50k catalog/queue peak and bounded worker requests |
| Platform/release; #28/#31/#34 | PARTIAL | Full suspend, wider endurance, electrical battery and new-image gates unchanged |

Proceed with measured local library improvements within the existing worker and schema. Application memory is measured, not new RAM-layout authorization. Future physical runs acquire `/tmp/y2-platform-v1-device.lock`; no unchanged source/ROM/ recovery provenance is repeated. Closing report must distinguish host/ARM evidence from real-device and whole-platform qualification.

## Platform 1.0 graphics evidence boundary — 2026-10-04

Before completing the isolated graphics pass, this review compares the owner scope, unchanged Lima/Mesa/DRM foundation, Reborn commit `a2df691e`, the parallel performance work, current issues and fresh locked hardware evidence. The [receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-GRAPHICS.md) and [physical summary](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-graphics/physical.json) identify installed Baseline02: Linux `8584ccd8`, running Reborn `b71b4688`, kernel `6.18.0-y2linux-baseline-02`, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0. The changed ARM decoder ran only as a temporary helper/library in `/run`; stock Reborn, original brightness and paused Home/screen-off were restored, scratch removed and the lock released. No flash, main edit, push, image rebuild, memory/layout expansion or full-system suspend trial occurred.

| Coverage | Classification | Evidence and next boundary |
| --- | --- | --- |
| Mali-400 MP2, Lima/Mesa, GBM/EGL/GLES2 and 480x360 KMS; #34 | CONFIRMED, bounded current awake scope | Native scanout ownership and two graphics readback tests pass; foundation preserved. |
| GPU runtime PM / screen-off display activity; #34 | CONFIRMED, bounded current off scope | 20.191 s off: zero frames/active GPU ms, MFG off, CRTC disabled, display/GPU enable counts zero, OVL/DSI IRQ totals unchanged. No electrical-power claim. |
| Static UI / runtime CPU cost; #34 and performance pass | PARTIAL, demonstrated gap | Stock paused Home presents 25 frames/20.138 s, GPU active residence 4.148 s, process CPU 7.00%; off CPU remains 5.65%. Performance owns event-loop/radio/renderer correction; combined acceptance is next. |
| Artwork dimensions/decode/memory; #34 | CONFIRMED, generated JPEG fixture scope | Reverse-order ARM check: 492.637→75.332 ms median CPU, peak RSS 29,920→9,320 KiB, unchanged 160x160 output; host regressions and 238 workspace tests pass. No GL-upload or full transition timing claim. |
| Backlight / retained-context wake; #34 | CONFIRMED, bounded readback scope | Five cycles, zero context loss, active native scanout restored, 10/50/100% readback 4/16/32. Optical flash and long-off state changes retain separate gates. |
| Product v2 boot / shutdown; #34 | PARTIAL | Same-boot splash log records READY→RELEASED→PRESENTED with errno 0; 26 splash tests plus shutdown/power contracts pass. No new cold boot, optical dissolve or poweroff observation. |
| CPU C1/C2/C3; #28 | CONFIRMED, retained UART01 scope | This SSH-attached sample has WFI entries and no C2/C3 entries; SPM rejects dormant topology. No policy change or new deep-idle qualification. |
| Full system suspend / context restore; #28/#31/#34 | PARTIAL, other session | Driver callbacks preserved; do not duplicate system-suspend work. |
| Electrical / endurance / release | PARTIAL | Activity/RSS/CPU counters and short warm-device temperatures are not watts, battery life or release acceptance. |

GitHub #28/#31/#34 were refreshed read-only at this boundary and remain OPEN; no milestone/epic closure or remote write is warranted. GPU-job IRQ deltas were not captured due to a harness regex defect; this does not erase the independent runtime-PM/scanout evidence or promote missing measurements. Native C warnings, 68 Linux tests, 238 Reborn tests, fmt, strict clippy and ARM release build pass. The graphics decoder candidate is ready for source review within its bounded scope; master integration must select one reduced-JPEG implementation alongside the FFmpeg/media pass and preserve its aggregate-I/O and cancellation guards; Platform 1.0 graphics acceptance remains PARTIAL pending integration and qualification of the performance-owned static-redraw correction and the separate visual/full-resume gates. Update the roadmap before any such boundary; planning issues authorize no further hardware or production scope.

## Platform 1.0 graphics pass admission — 2026-10-04

Owner requests an evidence-led GPU/display/power pass in isolated `codex/platform-v1-graphics` worktrees (Linux base `b5aea93`, Reborn `b71b4688`). No main edits, push, flash, memory/layout change or full-system suspend trial is authorized. Live access requires the shared non-blocking `/tmp/y2-platform-v1-device.lock`; admission attempts found it busy, so no device command ran. The retained UART01 and GPU-01 receipts supply real hardware evidence while fresh observation awaits exclusive access.[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-18-gpu01%2FREADME.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-REBORN-PRODUCT-UI-V2.md)

| Coverage | Classification | Evidence / next boundary |
| --- | --- | --- |
| Mali-400 MP2, Lima/Mesa, GBM/EGL/GLES2, 480x360 KMS | CONFIRMED, retained awake scope | GPU-01: correct rendering, 30 FPS, static GPU runtime suspend. Preserve architecture, clocks and PM policy. |
| C1/C2/C3 and screen/workload restoration | CONFIRMED, bounded UART01 scope | UART01; this pass does not alter CPU idle or repeat dormant trials. |
| Current Reborn static redraw, scrolling, artwork and blank/wake | PARTIAL | Source has dirty rendering and owned-CRTC sleep; collect exact running identity, counters and bounded product scenarios before claiming fresh physical success. |
| Product v2 splash/dissolve/shutdown | PARTIAL | Product v2 source/pixel/protocol evidence; retained receipts do not replace fresh visible cold-boot/shutdown observation. |
| Graphics full system-suspend/context restore | PARTIAL | Lima force-suspend/resume hooks exist; another session owns same-boot system-suspend qualification. No duplicate experiment. |
| Electrical savings / endurance / release | PARTIAL | Activity counters are not battery watts; no milestone or public-release acceptance. |

GitHub #28/#31/#34 refreshed read-only and remain OPEN. #34's historical pre-Reborn text is superseded by the current repository and UART01 receipts; its full-resume gate remains open. Refreshed OPEN statuses preserve the independent gates; no issue/milestone closure is warranted. Proceed with source audit, localized host checks and locked runtime measurements; implement only demonstrated graphics defects. Next smallest evidence boundary is an exclusive current-product observation. Results and remaining gaps belong in [the graphics receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-GRAPHICS.md).

Same-day peer evidence subsequently identifies installed Baseline02 `8584ccd8`/Reborn `b71b4688`, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0. The instrumented Reborn performance baseline shows 13 frames/10.09s on paused Home/Now Playing and zero screen-off frames; it restores installed `b71b4688`. Static invalidation is therefore a demonstrated gap, already being corrected by that parallel pass. Do not duplicate its renderer/event-loop work; final graphics acceptance depends on integration and physical after evidence. The local graphics branch separately reduces a measured full-size JPEG decode cost, with 68 Linux/238 Reborn tests, strict lint and ARM checks. At this intermediate point live graphics observation still awaited the lock, held by storage after the performance and Wi-Fi windows. The evidence boundary above supersedes that access status with fresh bounded results; release, full-resume and visual gates remain open.

## Reborn performance pass closing boundary — 2026-10-04

The owner-authorized, isolated application pass is complete for its measured Product v2 scenarios. Preserved baseline `b71b4688` plus instrumentation and candidate `069415a4207c00f0a32a3a2ac00602ddea29a895` run on the same real Baseline02 boot `88b85fa3-2282-4d93-b0b8-818a105ddd0a`, taint 0. Candidate ARM SHA-256 is `7871ec67f6678c7f522b1b84da0f1e53ab1646e89bc6abb6b7eafe10c02286c7`. The independent suspend recovery prompted a fresh matched comparison; old-boot results remain historical. No suspend trial is performed by this pass.

Evidence origin: synthetic supported evdev records/kernel timestamps, real 480x360 GLES2/KMS frames, disposable 10k SQL/UI fixtures, 16 collection trips, 1,000 wheel steps, four warm starts, playback/idle windows, cover sequences, native write-size probes and a supplemental 16 resume/16 pause replay per binary. See the [Reborn report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FREBORN-PLATFORM-V1-PERFORMANCE.md), [matched summary](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/reborn-platform-v1-performance/summary.json), [controls](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/reborn-platform-v1-performance/play-pause.json) and [restoration](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/reborn-platform-v1-performance/restoration.json). Mechanical/IRQ/debounce-to-photon, analog response, electrical power, peer radios and cold-boot improvement are not claimed. Live input uses three owner-library tracks/private PCM queue; 10k SQL/layout/GPU stress is a separate fixture.``

| Coverage / dependency | Classification | Evidence and remaining boundary |
| --- | --- | --- |
| Product v2, rendering/input; #34/#28 | CONFIRMED, bounded application scope | Wheel KMS p95 59.93→17.52 ms; Now Playing 77.61→17.15 ms; all 1,000 single steps match. Frame CPU p95 5.09–9.94→1.65–2.82 ms. Ten captures differ in 0.0087% of channels, max 5/255: bounded near-equivalence, not bit identity. Physical detent/IRQ/debounce/endurance remain separate. |
| Library/storage/artwork; #33 | CONFIRMED fixture behavior; PARTIAL wider library | 10k SQL/UI/GPU, collection Select/Back, bounded 160px/four-cover cache and missing/corrupt handling pass. A 10k single-album stress layout still takes 34.36 ms; no before/after claim for that new extreme fixture. Deep folders, large-queue persistence, media epochs and storage-owner pinning retain integration gates. |
| Application idle / C states; #28/#34 | CONFIRMED application reduction; PARTIAL current C2/C3/power | Home CPU 4.96→1.88%, switches 133.44→47.23/s; Home/paused Now Playing/Settings produce zero sampled static redraws. Screen-off CPU 4.25→2.87%. C1 progresses; C2/C3 remain zero under connected USB/radio guards. C3 policy stays Enabled/-1/disable0; electrical/full-suspend evidence is separate. |
| Wired audio / controls; #29 | CONFIRMED bounded S16/48k; PARTIAL wider audio | Whole-app playing CPU 87.95→11.21%, audio thread 82.63→5.11%; tiny partial-write churn is measured and fixed with one bounded readiness wait. Supplemental resume KMS p95 43.98→22.55 ms, pause 64.70→38.50 ms. Seek/reopen/pause/resume/stop and active SIGTERM exit 317.28 ms pass with zero XRUN/audio errors. Host null/fault tests preserve S16/S24/S32 counts; high-resolution/analog/peer audio remain separate. |
| Radios; #31 | CONFIRMED off-worker observation scope; PARTIAL peers | Redraws follow changed views; powered-off wait reduces wakes. Queued power-on can take 100 ms and is not hardware-qualified. Reconcile this local timeout hunk with the independent event-worker implementation before combined qualification. |
| Startup/splash; #16/#27/#28/#34 | CONFIRMED warm-start scope; PARTIAL cold boot | Four starts: first KMS p95 228.74→210.28 ms, first interactive 779→499 ms. Existing Product v2 handoff/frame count remains. Lazy platform connect does not block these screens; no unexercised API or new cold-boot latency is invented. |
| Production/recovery/full suspend; #28/#32 | CONFIRMED scope preservation; PARTIAL release | Installed /usr/bin/reborn b71, original paused/screen-off state and three tracks restored; same boot/taint0, rw root/data/SD with zero ext4 errors, original governor/C3 policy. Independent full-resume failure remains a release blocker. No production package, partitions, memory map, flash or push changes. |

Reborn source is `b8c05db` plus `069415a`; fmt, strict workspace/all-target Clippy, 243 workspace tests, exact ARM workspace build, 1k/10k/20k host fixtures and targeted native/scripted controls pass. Physical leases are released normally; owned device scratch is removed and raw host evidence retained privately. Read-only refresh keeps #16/#27/#28/#29/#31/#32/#33/#34 OPEN. No remote issue or milestone mutation is performed; scoped application acceptance closes no epic.

The next boundary is isolated cross-owner source integration, PARTIALLY READY, followed by relevant combined qualification. Preserve fresh storage/FD authority, source-epoch and suspend-prepare/inflight-result invalidation when composing the off-thread observations, and the strict audio/radio transport contracts when composing wired pacing. Use the radio owner's event worker for its superseded timeout hunk. Full resume, peer/analog/electrical evidence and release remain independent gates. This closing audit changes documentation only; unchanged source/ROM/recovery provenance is not repeated and no image is built or flashed.

## Reborn performance matched-run readmission — 2026-10-04

An independent suspend trial recovered through a watchdog reboot. Its owner checked direct storage hashes/ext4 integrity, restored the installed service and released the device lease. This performance pass then acquired the nonblocking lock and independently observed boot `88b85fa3-2282-4d93-b0b8-818a105ddd0a`, taint 0, unchanged Baseline02 Linux `8584ccd8` / Reborn `b71b4688`, paused playback, screen off and three library tracks. Root/data/SD remain mounted rw with all three ext4 error counters zero. CPU0 C3 is Enabled/budget -1/disable 0, coordinator enabled and schedutil 598000–1300000; pm_test is none.

The installed-source and production-scope admission below remains unchanged. Earlier performance measurements belong to boot `27e6d684`; rerun the preserved baseline executable before exact candidate `b8c05db` on this new boot for a matched comparison. Suspend remains PARTIAL with the independent failed full resume gate; this pass authorizes no further deep trial. Read-only refresh keeps #16/#27/#28/#29/#31/#32/#33/#34 OPEN. No source/ROM/recovery provenance, build image, flash, push or policy change is needed. The next boundary is the reversible baseline/candidate measurement and restoration receipt, followed by the closing gap audit. Evidence: Reborn `out/performance/admission-newboot.json`.

The matched UI candidate passes its bounded boot88 scenarios. A further audio write-size probe using the exact gain code and normal S16/48k/512-period/4096- buffer sink reproduces over 10k tiny partial writes/s and roughly one core of CPU. A bounded capacity wait reduces that probe to 131 writes and about 30 ms CPU per second. This supports a localized Reborn ALSA readiness fix under the existing authorization, with unchanged formats/buffers/gain/leases/frame accounting. Validate its wait/recovery/control behavior, then repeat the exact candidate playback and performance receipt before the closing audit. This is not high-resolution/analog/peer-Bluetooth or production package authorization.

## Reborn performance pass admission — 2026-10-04

Owner authorizes measurement and localized Reborn responsiveness fixes on branch `codex/platform-v1-reborn-performance`, preserving Product v2. Fresh read-only USB SSH under `/tmp/y2-platform-v1-device.lock` observes installed Y2LINUX-BASELINE-02, Linux `8584ccd8`, Reborn `b71b4688`, kernel `6.18.0-y2linux-baseline-02`, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0, and automatic qualified CPU0 C3 policy Enabled/budget -1/disable 0. This supersedes installation-pending information only for device identity and boot-policy observation; it does not substitute for full Baseline02 qualification. Retained UART01 C1/C2/C3 evidence remains scoped to its tested image.

| Coverage / existing dependency | Classification | Next boundary |
| --- | --- | --- |
| Product v2 UI, GPU #34 | PARTIAL | Measure 480x360 frame submission/presentation, navigation, wheel and artwork on installed hardware; preserve pixels and KMS ownership. |
| Library/storage #33 | PARTIAL | Disposable 10k-track SQL and UI fixtures; distinguish fixture timings from owner-library/cold-storage results. |
| CPU idle #28/#34 | CONFIRMED bounded UART01; PARTIAL current-image | Measure Reborn CPU/context switches and redraws under current guards; do not change C1/C2/C3 policy. |
| Audio/radios #29/#31 | PARTIAL | Bounded playback/control regressions; audible response and external peer behavior require direct observation. |
| Startup/splash #28/#34 | PARTIAL | Installed first-frame log 446 ms from process entry; boot application-ready 41.343 s. Measure app restart separately from cold boot. |

Read-only GitHub refresh confirms #16/#27/#28/#29/#31/#32/#33/#34 OPEN. No remote status mutation, milestone closure, build image, flash, push, memory reservation, partition or production package change is authorized by this pass. Temporary executable/fixture runs are reversible hardware measurements; retain and restore the installed service and owner data. Next smallest boundary is a measured baseline before any optimization. Source/ROM/recovery provenance is unchanged and is not repeated. Report belongs in Reborn `docs/validation/REBORN-PLATFORM-V1-PERFORMANCE.md`.

## Platform 1.0 input pass end boundary — 2026-10-04

Owner instruction “come to an end” terminates further device waiting after source validation and one bounded read-only hardware observation. This boundary closes the work session, not input acceptance or a Platform 1.0 milestone. Reborn `e51a335`, Linux `95ed509`: fmt/strict Clippy,257 workspace tests (37 input/40 UI), ARM build and5 targeted Linux tests pass. Candidate userspace is built and hashed, never installed/executed. Kernel/DT/images remain unchanged.

Fresh hardware identity is Baseline02 compiled Linux8584ccd8/Rebornb71b468, boot27e6d684-3794-4490-95db-a489027cd4f4,taint0. The120.289s observer recorded 0events; owner operation was not confirmed before window end. Subsequent wheel/I2C0/Power/keypad IRQ deltas0, but four cores remained online and dormant entry rejected topology; C2/C3 counts0. Retained UART01 proves bounded older C1/C2/C3 behavior, not this unexecuted input candidate. Helper removed, original service/binary untouched, lock normally released; input reservation cancelled.

| Coverage / dependency | Final classification | Remaining gate |
| --- | --- | --- |
| APT32F/filter/cadence, #28 | CONFIRMED retained218 pulses; PARTIAL physical accuracy | 100CW/100CCW counted detents, measured bounce and owner feel |
| Reborn timing/recovery, #28 | CONFIRMED deterministic software; PARTIAL hardware | All buttons>=20 presses; holds/repeats/reopen/drop acceptance |
| Action/state/frame, #34 | IMPLEMENTED bounded diagnostics; NOT_MEASURED current latency | Candidate kernel->state/page-flip median/p95/worst; physical origin separate |
| Input idle/C1/C2/C3, #28 | CONFIRMED zero input IRQ delta in bounded snapshots; PARTIAL candidate compatibility | Qualified topology and per-process wake attribution;50Hz navigation poll retained |
| Power/full suspend, #28 | CONFIRMED software gesture/reset contract; PARTIAL physical wake | Suspend-owner integration and actual wake suppression |
| Product v2 physical UX | CONFIRMED host navigation invariants; PARTIAL owner acceptance | Every screen, large lists, audio volume and human feel |

Verdict MORE_WORK_REQUIRED. Existing issue/epic states are retained from the read-only admission snapshot (#28/#34 OPEN); no remote status write or milestone promotion. Source handoff is ready; the next smallest blocker is an owner-counted physical window and candidate runtime tracing. No new hardware, memory, protected-data or production scope is authorized by this closure. Full fixes, exact artifacts and acceptance limits: [input report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-INPUT.md).

## Platform 1.0 input software candidate boundary — 2026-10-04

The admitted input-only source pass is software complete: Reborn `e51a335`, Linux tooling `99087ba` (kernel/DT unchanged), 257 workspace tests including 37 input and40 UI tests, fmt/strict Clippy, ARM Cortex-A7 release build and 5 targeted Linux input tests pass. The userspace candidate is sealed under `out/platform-v1-input-candidate/`; no BOOTIMG/Y2ROOT image, flash or push. After owner-requested waiting, the lock admitted one bounded read-only window. Baseline02 boot `27e6d684-3794-4490-95db-a489027cd4f4`, compiled Linux `8584ccd8` / Reborn `b71b468`, taint0: 120.289s with zero evdev records (owner replied after capture); subsequent wheel/I2C0/Power/keypad IRQ deltas all0. Current four-core topology rejected dormant entry; C2/C3 counts0. No policy or installed binary changed. Helper removed and lock released for storage. This is not physical acceptance or cold-boot/CPU qualification.

Fresh analysis of retained physical DEV02/GPU01 raw records finds218 wheel press/release pairs; zero same-direction gaps <8ms; minimum active gap30.957ms. No counted hand detents or latency data exist in those captures. Retain the 8ms filter and acceleration tiers. Existing UART01 C1/C2/C3 receipts remain hardware authority; no CPU/radio/poll policy or full-suspend subsystem change.

| Coverage / dependency | Classification | Remaining gate |
| --- | --- | --- |
| APT32F/I2C/evdev, #28 | CONFIRMED retained pulse behavior; PARTIAL counted/current behavior | 100CW+100CCW counted detents and button counts |
| Reborn timing/recovery, #28 | CONFIRMED deterministic software; PARTIAL physical | Candidate holds/rebind/drop/wake and human feel |
| Input->state/frame, #34 | PARTIAL | New bounded microsecond trace on candidate; physical median/p95/worst pending |
| Input idle/C1/C2/C3, #28 | CONFIRMED retained whole-system scope; PARTIAL new input measurement | Zero idle wheel/I2C0/Power/keypad IRQ delta observed; per-process timers/candidate C2/C3 pending;20ms navigation poll retained |
| Power/full suspend, #28 | PARTIAL | Typed gesture/reset contract provided; platform-owned full wake qualification |
| Product v2 controls | CONFIRMED software invariants; PARTIAL physical UX | Screen/list/volume listening and owner acceptance |

Existing epics remain OPEN; no status/milestone promotion or remote write. [Input report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-INPUT.md) records bugs, exclusions, exact candidate identity and physical owner protocol. Next smallest boundary is a free device window and installed-identity/capture; no new hardware, memory, protected-data or recovery provenance scope is admitted.

## Platform 1.0 input pass admission — 2026-10-04

Owner explicitly authorizes implementation, optimization and bounded physical input observation in isolated `codex/platform-v1-input` worktrees, based on Linux `b5aea93` and Reborn `b71b468`. No flash, push, main-worktree changes or full system-suspend implementation is authorized. The shared nonblocking device lock was busy on first attempt; no live access occurred.

Retained UART01 hardware evidence remains authoritative for bounded C1/C2/C3: Linux `e9e8d63`, Reborn `b71b468`, boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b`, taint 0, 3,647 checked C3 returns. Retained DEV02 and GPU01 evdev captures show APT32F press/release wheel records and all eight physical controls; they do not prove counted slow-detent accuracy, current-image bounce, presentation latency or human feel. Baseline02 new-image qualification remains PHYSICAL_NOT_RUN.

| Coverage / dependency | Classification | Next evidence boundary |
| --- | --- | --- |
| APT32F IRQ/I2C/evdev, #28 | PARTIAL | Current installed identity, bounded capture and detent counters; preserve IRQ-only driver unless evidence requires change |
| Reborn timing/actions/recovery, #28 | PARTIAL | Deterministic failure/timestamp/hold tests, targeted fixes, workspace checks and ARM build |
| Display/presentation latency, #34 | PARTIAL | Correlated input/state/frame timestamps; physical actuation origin requires owner or external measurement |
| C1/C2/C3 input compatibility, #28 | CONFIRMED bounded retained CPU scope; PARTIAL input scope | Observe untouched input IRQ/poll activity without changing CPU/radio policy |
| Power/full suspend, #28 | PARTIAL | Typed Power and screen-state ownership here; full suspend belongs to another session |
| Product v2 physical UX | PARTIAL | Counted detents/buttons, screen-off/wake and owner feel test on installed candidate |

GitHub #28/#34 refreshed read-only: OPEN. No remote issue mutation or milestone closure; parallel sessions retain their ownership. Product v2 global controls, fine-control contexts and long-list acceleration remain the authority. Proceed with source mapping and deterministic reproduction while retrying the device lock. Recovery/protected partitions, memory, ROM provenance and production scope are unchanged. Admission is PARTIALLY READY: software work authorized, hardware counts and candidate acceptance pending. See [the input validation record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-INPUT.md).

## Full suspend failed-return boundary and codec correction — 2026-10-04

Verdict MORE_WORK_REQUIRED. The installed Baseline02 one-shot 12-second RTC trial records SPM EINT `0x20`, full PCM length 596 and reset-vector stamp `0x59325253`, but no COMPLETE/EXIT. Previous journal sequence 175 stops at DEVICES_RESUMING; phase-7 enter 7407 for CS43131 `1-0030` has no matching leave through final sequence 7422. Wheel and both MMC callbacks do leave; their parallel progress does not prove codec completion. The inner codec stall is unknown. Boot changes from `27e6d684-3794-4490-95db-a489027cd4f4` to `88b85fa3-2282-4d93-b0b8-818a105ddd0a`, with a retained 30-second backstop. This is failed return/reset recovery, never successful resume; decoded RGU cause was not captured. Power and repeated entries are stopped after this first trial.

| Coverage | Current classification / remaining boundary |
| --- | --- |
| CPU/idle/timers; #28 | CONFIRMED bounded UART01 runtime; Baseline02 staged PM PASS, full CPU reset return observed, whole-device completion FAIL |
| Power/suspend; #30 | PARTIAL; charger refusal/awake RTC PASS; same-boot RTC/Power and repetition unqualified. Epic externally CLOSED does not close this evidence gate |
| Storage/USB/radio; #28/#31 | PARTIAL full resume; stages return, O_DIRECT data+SD preserved across reset/errors 0, USB/Wi-Fi usable after reboot; active BT full restore NOT_RUN |
| GPU/display/audio; #34/#29 | PARTIAL full resume; CS43131 callback is the present blocker; new boot graphics availability is recovery evidence |
| Reborn/product | IMPLEMENTED typed prepare/restore and Power behavior; native/QEMU tests PASS, new physical protocol NOT_RUN; ordinary deep-sleep gate retained |

A narrowly scoped codec PM source correction replays cached state/XTAL mask after supply-disable refusal without double rail references, and records force/rail/ delay/cache/XTAL substeps in the existing retained ring. It does not claim to fix the unidentified inner stall. Eleven focused fault/PM trace tests and a corrected isolated ARM Image/zImage/modules build PASS; audio/policy has 12 pass + one DTB skip. Prior 244 Reborn workspace tests/fmt/Clippy/ARM proof remains unchanged. No AFE/high-resolution audio, C1/C2/C3, voltage, clock, memory or protected scope change. New source is uninstalled; no flash/push/merge/issue update or milestone closure. Fixtures/listener cleaned, pm_test none/backstop 0/alarm empty, stock software/policies preserved, lease released normally to performance. Next is a coherent owner-installed instrumented candidate, then one checked RTC return, Power wake and full subsystem/cycle qualification only after success. [Exact report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-SUSPEND.md) and [bounded evidence](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-suspend-2026-10-04.json).

## Full suspend physical entry boundary — 2026-10-04

The retained device lease now admits installed Baseline02 Linux `8584ccd8` / Reborn `b71b4688`, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0. Freezer on USB and battery devices/platform/processors/core PM tests PASS: helper return, kernel COMPLETE/error 0, unchanged boot, zero ext4 errors and no SPM entry. Charging devices test intentionally refuses at DPM_PREPARED with `-EBUSY` and returns awake; its guard is preserved. One awake RTC alarm delivers one child IRQ and clears; it does not prove suspend wake. Wi-Fi observation survives radio quiesce/restore. Owner disconnects USB; actual Discharging and USB presence 0 are verified before battery tests.

Read-only issue refresh: #28/#31/#34 OPEN; #30 CLOSED since 2026-09-15 despite its retained checklist. This pass changes no issue status and cannot infer full-suspend acceptance from that administrative closure. Runtime C3 evidence remains separate. Full Power/RTC wake, same-boot deep return, actual subsystem restoration and repetition are still NOT_RUN. Source kernel guards and the new Reborn protocol are built/tested but not installed; installed-image tests cannot qualify their execution. No milestone closes, charger bypass, register change, flash, push, protected-partition or memory-layout change is admitted. Next is one short RTC full trial with existing one-shot backstop and retained journaling; any failed checked return stops subsequent entry trials pending diagnosis. Raw receipts: `out/platform-v1-suspend/pm-*-battery/`, `pm-freezer-charging/`, `pm-devices-charging/`, `rtc-awake.json`. [Full implementation and qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-SUSPEND.md).

## Platform 1.0 full suspend implementation admission — 2026-10-04

Owner explicitly authorizes implementation and bounded whole-device qualification on dedicated `codex/platform-v1-suspend` worktrees (Linux base b5aea93, Reborn b71b468), with no flash or push. A non-blocking shared device lock governs every physical operation. First locked read observes Baseline02 kernel, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0, active charging and no current retained suspend journal. Installed source identity needs a complete receipt; this new image does not inherit blanket physical qualification from UART01.

Retained UART01 evidence proves C1/C2/C3 in its bounded runtime scope. Retained Fix02 evidence proves SPM/RTC/reset-vector/CPU/device return followed by a stall before kernel EXIT and watchdog recovery, not successful same-boot resume. Current staged PM, Power/RTC wake and all full-suspend subsystem restoration remain PARTIAL/NOT_RUN. Existing #28/#30/#31/#34 and production gates remain open; no external issue change or milestone closure. Preserve C1/C2/C3, exact MT6582 PCM and register contracts, charger refusal, storage and memory layout. Next: trace the installed image, run safe staged PM before one RTC and one Power wake, then bounded mixed cycles only after checked same-boot restoration. Source work continues while the shared device lock or charging prevents physical entry. See [implementation receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-SUSPEND.md).

## Baseline02 source integration into main — 2026-10-03

The owner authorizes merging and publishing the current Baseline02 source and documentation on `main`. Admission compares remote `main` at `131ee4621cd583c955182f994adac5a594fb823f` with `cpu-idle-completion` at `acb5bb3e8fb3a0cdc07a6d31fc64b6e83118ccbc`: the former is an ancestor, the working tree is clean, and integration can fast-forward without source reconciliation. This review precedes that operation.

Hardware authority remains the retained [UART01 physical receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md): Linux `e9e8d63f9c94232c2b6627881e0967583e202dac`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b`, taint 0. C1/C2/C3 pass their bounded scope; 21 guarded C3 trials and 3,647 final checked returns preserve timer/context/CIRQ/clock/media integrity. The [sealed Baseline02 receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) records compiled Linux `8584ccd85f052f351fe51650b2348c83ca894ed4`, fresh software/package checks and automatic qualified CPU0 C3 policy. Its new-image/cold-boot hardware qualification remains PHYSICAL_NOT_RUN; publishing source does not change that.

| Coverage | Classification | Evidence and remaining boundary |
| --- | --- | --- |
| CPU/timers/idle/storage; #28 | CONFIRMED, bounded UART01 scope; PARTIAL, new-image acceptance | Bounded UART01 hardware qualified; Baseline02 software validated. Owner installation and exact-image/cold-boot qualification remain next. |
| Radio/USB; #31 | PARTIAL | Bounded UART01 observer/transfer regression passes; peer codecs, coexistence, full-suspend restoration and endurance retain separate gates. |
| GPU/display; #34 | CONFIRMED, awake scope; PARTIAL, full resume | Existing awake rendering/runtime-PM evidence carries forward; full system-suspend restoration remains separate. |
| Release/power | PARTIAL | Full system suspend, electrical battery measurements, wider endurance and public distribution remain open; no milestone acceptance is promoted. |

GitHub #28/#31/#34 were refreshed read-only and remain OPEN. Source integration is ready; the next hardware boundary still requires owner-preserving installation and the existing guarded harness. BOOTIMG/Y2ROOT bytes, Y2DATA, protected partitions, memory layout and runtime policy are unchanged by this merge. No build, flash or repeat of unchanged ROM/recovery provenance is required. The roadmap records the same boundary before integration; the later documentation revision is not the source revision compiled into the sealed images.

## Baseline02 documentation synchronization — 2026-10-03

This is a documentation-only boundary review using the already retained Baseline02 seal and UART01 hardware receipt; no build, flash, device test, remote issue update or repeat of unchanged ROM/recovery provenance occurs. The [current state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md), [Baseline02 receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md) and [UART01 physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) govern the current source/runtime distinction.

The C1/C2/C3 implementation and bounded UART01 hardware gates are closed. UART1 ownership and the exact MT6582 sleep ACK no longer block C3. Baseline02 is sealed and software-tested from Linux `8584ccd85f052f351fe51650b2348c83ca894ed4` and Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`. Owner-selected once-per-boot automatic CPU0 C3 policy is included, with unchanged dynamic guards. New-image/cold-boot physical qualification remains PHYSICAL_NOT_RUN.

Next CPU boundary: owner-preserving Baseline02 installation, exact identity and automatic boot-policy proof, guarded first C3 reset-and-return plus 20 cycles, then runtime/wake/storage regression. No C1/C2 redesign or generic CPU audit is needed. Full system suspend/Power+RTC wake, wider endurance/thermal conditions, electrical battery measurement, native high-resolution audio and public release permissions retain their independent gates. Planning epics #28/#31/#34 remain open; this documentation review does not close or authorize their remaining work.

## Historical roadmap and boundary reviews

The following text retains earlier dated decisions and results. Its “current”, “next” and candidate labels belong to those sessions; the Baseline02 summary above takes precedence. Historical failures and seal-time NOT_RUN receipts remain evidence for their exact images.

# Y2Linux roadmap and gap audit

## Baseline02 sealed candidate boundary — 2026-10-03

Y2LINUX-BASELINE-02 is built, software-validated and sealed. Compiled Linux `8584ccd85f052f351fe51650b2348c83ca894ed4` / Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`; kernel6.18.0-y2linux-baseline-02, rootv1.21, release1.0.0-baseline-candidate.2. Fresh kernel/Buildroot/Reborn ARM, config/DT/modules/ABI,391 production tests, 125 focused source tests,27 native filesystem/GIO and3 ALSA tests,238 Reborn tests/fmt/lint, Cortex-A7 QEMU, installed ARM tools, ELF/dependencies, legal/source collection and preserving package validation pass. Five minimal-environment checks skip dependencies separately covered by the native/ARM checks. Final package: `out/y2linux-baseline-02-candidate/`; receipts: `out/baseline-02-validation/final-seal.json`. Source/current-main inclusion and preserved implementation are recorded in preserved-architecture.json.

Owner-selected C3 startup now selects budget-1/CPU0 enable once after static foundations pass. Live ARM control/readback and isolated fault tests pass; manual stop/recovery overrides and all dynamic kernel guards remain intact. New-image cold-boot and physical qualification NOT_RUN until owner flashes. Closing read-only SSH still verifies installed UART01e9e8d63, unchanged boot fd955840-35d9-47db-83e0-ff47d6bb2d2b, taint0,3647 actual C3 returns, no timeout/ context/clock restore fault. C1/C2 and C3 entry/restore implementation are preserved; SPM comment/localversion and userspace boot admission differ.

Only BOOTIMG and ANDROID/Y2ROOT are payloads. Y2DATA and protected partitions remain preserved. Exact UART01 rollback pair remains in fallback/; source/license archives and fresh validation/harness are attached. No flash/push or milestone closure. #28/#31/#34 stay OPEN; full suspend, additional wakes, endurance and electrical battery evidence remain separate gaps. Six owner documentation edits remain preserved. Next boundary: owner-controlled Download Only of the two new images, then exact-identity/automatic-boot-policy and guarded physical harness. [Baseline02 handoff record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md).

## Baseline02 automatic C3 policy source check — 2026-10-03

The owner-selected once-per-boot CPU0 policy passes isolated foundation, identity, manual ownership, readback/rollback, failed receipt and stop tests. Live ARM execution on installed UART01 also passes: quarantined budget0/state-disabled then budget-1/CPU0 enable readbacks, repeated-start refusal, same boot/taint0. Original already-qualified runtime controls are restored and owned /run test files removed. This verifies the control transaction on the existing image; new Baseline02 cold-boot execution is still NOT_RUN. C1/C2 and kernel admission/ UART ACK/context/clock/timer/restore logic are unchanged. Only the SPM explanatory comment changes. The harness now verifies the actual automatic boot receipt and controls before altering qualification policy. Freeze this coherent source pair, then build fresh kernel/Buildroot/Reborn ARM and preserve-data package. No flash, push, milestone closure or protected/memory/data change. Raw control receipt: `out/baseline-02-validation/live-policy-control.json`.

## Baseline02 qualified C3 boot-policy admission — 2026-10-03

Owner selects Enable qualified C3 automatically for this new baseline. This supersedes the default-off packaging choice in the admission below, not its hardware evidence. Same installed UART01 source/boot,3647 real C3 returns and clean checked restores underpin the decision. Add a once-per-boot userspace policy using existing CPU0 cpuidle disable and SPM budget controls. Kernel starts quarantined, then normal startup verifies identity and static context/timer/CIRQ/ SPM foundations before budget-1/CPU0 enable. Leave dynamic screen/workload/ radio/USB/topology/OPP/deadline/clock/UART ACK guards intact. No forced parking, frequency/radio change or clock gate. Retain y2.deep_idle=off/CPU-safe recovery and manual stop; repeated service startup must not undo an owner's disable.

Targeted isolated fault tests and a bounded live policy-control/readback test precede source freeze. Then one final fresh integrated baseline build and full candidate checks. The interrupted default-off draft produced no package; it is not a delivered candidate. New persistent cold-boot behavior remains NOT_RUN until owner installs Baseline02. Full suspend/endurance/electrical evidence and #28/#31/#34 dependencies remain OPEN; no new hardware/memory/partition scope, flash or push. Current boundary receipts: `out/baseline-02-validation/`.

## Baseline02 integrated candidate admission — 2026-10-03

Owner requests a fresh integrated baseline after UART01 physical qualification. Read-only authorized SSH reconfirms installed Linuxe9e8d63/Rebornb71b4688, kernel `6.18.0-y2linux-cpu-c3-uart-01`, rootv1.20, unchanged boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b`, taint0. C3 still has3647 real entries/resumes/successes/UART ACKs, zero timeout/context/clock/CIRQ failures. The completed foundation and21 bounded C3 trials plus60s runtime observation remain authoritative; see [UART01 physical evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md). This is a packaging boundary, not a general CPU audit or new hardware phase.

Prepare one fresh BOOTIMG/Y2ROOT baseline from current committed Linux and Rebornb71b4688, retaining all integrated storage/USB/audio/power/radio/product work and current UART C3 architecture. Fresh kernel, Buildroot/Reborn ARM, production regressions, QEMU/ELF/config/DT/module/ABI and data-preserving package checks are required. Preserve Y2DATA, protected partitions, guarded five OPPs, C1/C2 and default-off C3 policy; include latest guarded qualification harness. New image physical qualification remains NOT_RUN until owner installation. Fallback is the unchanged physically qualified UART01 BOOTIMG/Y2ROOT pair.

#28/#31/#34 remain OPEN: persistent C3 boot policy, full-system suspend, additional wake sources, endurance and electrical battery evidence are distinct unclosed coverage. No memory/layout/data-schema change, flash, push or public redistribution authorization. Six preexisting owner documentation edits remain separate. Boundary receipts: `out/baseline-02-validation/`; [new baseline record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md).

## UART01 C3 hardware closing audit — 2026-10-03

C1 WORKING; C2 WORKING; C3 WORKING_AND_REPEATEDLY_OBSERVED on installed Linuxe9e8d63/Rebornb71b4688, kernel `6.18.0-y2linux-cpu-c3-uart-01`, rootv1.20, unchanged boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b`, taint0. Fresh physical foundation checks pass: four-core C1,18 normal hotplug transitions, all five OPPs, GPT6/GPT4/PPI29/13MHz/highres/NO_HZ, natural owned parking, C2+6971 entries/+50.654676s in60.054881s (84.35%), zero clock restore failures. C3 proves21 budget1/RGU/SRAM checked reset returns, then+3624 normal-policy entries/+39.204662s in60.088344s (65.25%). Final entries=resumes=successes= UART attempts=ACKs=CIRQ transactions/flushes=timer saves/restores=3647. No UART timeout, restore/context/clock/media/IRQ fault or reboot. eMMC/SD, five OPPs, screen/workload/playback, USB and Wi-Fi postwake regressions pass.

UART1 remains clocked: conditional exact MT6582 PIO ownership and global SPM request/ACK resolve admission without forced gating. No kernel/image changes after installation; locally committed c8ae170 fixes observer fsync sequencing and accounts safe guard refusals separately from actual entries. 33 targeted tests pass. Original failed observer verdicts are retained and independently rechecked against stronger UART/SRAM/context/media guards. Authoritative joined proof: `out/cpu-c3-uart-physical/20261003T183259Z-uart01/final-verdict.json`; [hardware record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md).

F027/F028/F030 may advance to this bounded same-boot physical qualification. The UART C3 blocker is closed. No new flash is required. C3 is intentionally runtime-enabled/budget-1 for THIS BOOT, RGU disarmed and original radios, screen, schedutil598–1300MHz and coordinator restored. Fresh boot still uses image default-off/budget0; no persistent default-on policy is claimed or changed. Full system suspend, new wake-source coverage, endurance, electrical battery measurement and other #28/#31/#34 dependencies remain OPEN. No general milestone closure, memory/partition/protected-data change, flash or push. Six preexisting owner documentation edits remain preserved separately.

## UART01 physical trial admission — 2026-10-03

Owner confirms the new candidate installed and authorizes the prepared hardware qualification. Read-only SSH verifies Linuxe9e8d63/Rebornb71b4688, kernel `6.18.0-y2linux-cpu-c3-uart-01`, rootv1.20/buildY2LINUX-CPU-C3-UART-01, boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b`, taint0. Checkout55db6d3 is a later receipt, not installed source. C3 remains disabled/budget0 and actual dormant/ UART handshake counters0. UART0 sleep enable1 and UART1 conditional deferred bit0x20000 are now physically observed. UART1 is no longer a mandatory gate prerequisite; global SPM ACK and context return remain unobserved. Current normal Wi-Fi/USB/1300MHz adds legitimate dynamic blockers, not a new settled UART diagnosis. Existing candidate02 C1/C2 qualification stays authoritative until regression checks on this image complete. Raw evidence: `out/cpu-c3-uart-physical/20261003T183259Z-uart01/`.

Dependencies #28/#31/#34 stay OPEN; no milestone closure or hardware-limit claim. Proceed with normal C1/C2/timer/hotplug/storage/five-OPP regressions, then natural quiet CPU0/low OPP/radios-off/USB-detached topology. One budget1 RGU/SRAM/timer-wake trial must show real request/ACK and checked same-boot return before20 further bounded cycles. Failure disables C3 and stops trials; observe the precise stage, retain independent regressions and fix that cause. Stop paused playback through the existing authorized owner control. No forced UART gate, arbitrary MMIO/probe, memory/partition change, flash or push; preserve six preexisting owner documentation edits. No general CPU redesign, full-system suspend or electrical battery claim is authorized by this narrow trial.

The installed UART01 regression pass now proves four-core C1, natural parking, C2 +6,971 entries/+50,654,676us over60.0549s with zero restore failures, all five OPPs, hotplug, timers, eMMC/inserted SD, screen/workload/playback and USB/Wi-Fi integrity. Same boot/taint0, no filesystem/IRQ faults. Its first C3 window stopped at legitimate MSDC0 bit12 (0x1000), not UART1: the harness fsynced its durable arm receipt after the clean preflight, waking eMMC. Actual UART requests/ACK attempts, CIRQ transactions, CPU context entries and returns all remain0. Therefore this is an observer sequencing defect, not a failed deep-idle experiment. Preserve the kernel/storage guard. Targeted harness fix saves before a read-only two-second stable admission window, checking the real MMC gates, all exposed prerequisites and owned physical CPU0 topology; no storage writes occur between that window and enabling C3. A C3-only continuation requires the exact clean same-boot regression receipt and zero actual UART/CPU entries both in that receipt and on-device immediately before mutation. Any real UART/context refusal stops repeats; first checked entry must still precede 20 further cycles. Thirty targeted harness/CPU/UART tests pass. Scope remains unchanged; dependencies stay open pending real hardware ACK/context results.

UART01 FIRST REAL DORMANT RETURN is now physically proved on the same boot. Corrected observer sequencing reached global UART request/ACK1, exact POWER1 0x15820→0x15821→0x15820, R13 ACK0x8140000, one CPU entry/resume/success, 8,065us SPM/9,363us cpuidle residency, GPT wake0x10, CIRQ clone/flush1/1 and local timer context save/restore1/1. SRAM records UART_REQUEST→UART_ACK→ DORMANT_CONTEXT→DORMANT_FINISH→DORMANT_RETURN→DORMANT_COMPLETE with actual reset-resume assembly marker0x59325253; no restore/context/media/IRQ fault, taint0 and unchanged fd955840 boot. The harness incorrectly rejected the otherwise successful trial because spm.c counts every admission before the budget check: +3 admissions included +2 safe -EACCES budget refusals after the single physical entry. Fix measurement to require EXACTLY one physical entry/ return/success/ACK, account all extra admissions as aborts, require final budget refusal and every original restore guard plus SRAM reset marker. Original raw FAIL receipt remains intact; independent first-entry recheck is attached. 33 targeted tests pass. Continue ONLY20 further budget1 guarded cycles after rechecking the same-boot first-entry and original regression receipt hashes; no retry of any actual hardware failure. C3 stays disabled/budget0 between trials. Full repeatability/policy qualification and dependency closure remain pending; no kernel build or image changes are needed for these harness fixes.

Repeatability now physically proves18 UART ACKs/CPU reset entries/resumes/ successes on unchanged fd955840 boot, positive residency and zero UART/CIRQ/ timer/clock/context/media faults. Sixteen further cycles passed directly; cycle17 also genuinely succeeded, but the checker overrequired the LAST admission to be budget-refused when its two safe guard refusals preceded the successful entry. Correct verdict permits last resumed/result0 as well as budget/-EACCES, still accounting every refusal and requiring exactly one new physical entry/ACK/checked reset return and every restore. Independently rechecked all18 raw cycles (original FAIL receipts retained with their SHA256). Continue only the remaining3 bounded cycles, then near-deadline fallback and 60s normal-policy residency. Any real failure still stops; ordinary policy may stay enabled for THIS BOOT only after all21 checked cycles and postwake regressions pass. Fresh boots retain image default-off/budget0; no persistent policy/image/default-on change is implied. No general CPU or suspend milestone closure; release claims may advance only to the actual bounded idle evidence.

## C3 UART sealed candidate boundary — 2026-10-03

Exact MT6582 PIO-owner admission/global UART request-ACK integration is fixed; C1/C2 and all unrelated clock/context/timer/OPP architecture are preserved. Candidate `out/y2linux-cpu-c3-uart-candidate/` at Linuxe9e8d63/Rebornb71b4688 is freshly built/sealed. Production375/source109/native host/Reborn238 tests, ARM/QEMU/config/DT/modules/ABI/ELF and preserving package checks pass; five minimal-host dependency skips have separate native/ARM coverage. Sources and collector limitations are attached; package remains owner-local.

Fresh closing SSH still verifies installed candidate02/unchanged boot, C3 disabled/budget0/entries0; C1/C2 working evidence remains authoritative. C3 has never entered. #28/#31/#34 and CPU idle acceptance remain open until owner-installed UART01 gives real ACK and bounded same-boot context/timer wake. No hardware-limit proof, full suspend/electrical battery claim, protected data change, flash/push or milestone closure. Owner alone installs BOOTIMG+Y2ROOT with the preserving scatter; harness is ready for first entry then20 further cycles. Six preexisting owner doc edits remain separate. Exact source, hashes, checks and owner action are in [the C3 UART handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART.md).

## C3 UART software freeze audit — 2026-10-03

Targeted stock-contract implementation and100 focused tests are complete. Installed candidate02/source/boot and actual C1/C2 results remain unchanged; C3 has never entered. The copied default UART1 mask lacked stock PIO-owner integration. Conditional UART1 sleep adoption, exact MT6582 console driver sleep capability, bounded global SPM ACK/refusal, checked unwind, retained stages and first-entry/20-further-cycle harness replace that missing contract. All unrelated clock guards, C1/C2/timers/parking/OPPs/media architecture remain. Exact source/ownership/unknown RTL limits are documented in [the C3 UART record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART.md).

Before production handoff, build one fresh kernel/Buildroot/Reborn ARM pair and validate config/DT/modules/ABI, regressions, ELF/QEMU and preserving package. Candidate scope is BOOTIMG+Y2ROOT at `out/y2linux-cpu-c3-uart-candidate/`, API1/data/layout unchanged, no protected payload, no flash/push. No hardware promotion: #28/#31/#34 and CPU completion remain open pending real ACK and bounded same-boot DORMANT wake after owner installation. No new general audit, ROM/recovery provenance pass, electrical measurement or full suspend claim.

## C3 UART stock-contract admission — 2026-10-03

Owner narrows work to the candidate02 UART1 C3 blocker. Preserve physically working C1/C2 and their architecture; do not conduct another general CPU audit. Fresh targeted SSH verifies installeddb0234e/b71b4688, kernelidle-02/rootv1.19, buildY2LINUX-CPU-IDLE-COMPLETION-02, same boot `f155196b-64d4-45a4-88b3-27755a1a8926`. UART1 remains clocked with IRQ/DMA/LSR0; actual dormant calls0, C3 disabled/budget0. Restored normal radio/OPP policy legitimately adds other current preflight reasons; the prior settled receipt still isolates UART1 alone. Expected prior diagnostic taint4096 is retained. New read-only admission: `out/cpu-c3-uart-physical/20261003T164546Z/`.

Exact MT6582 d53dd75c `mt_idle` default PERI mask includes UART1 bit17; `mtk_uart_startup` enables DPIDLE for non-DMA ports and enables UART_SLEEP_EN, while DMA ports remain blocked. The global SPM R7 request/R13 ACK follows PCM fetch and precedes PCM register/power/run/WFI programming. Existing Y2Linux has the handshake but lacks UART's conditional mask/sleep-owner integration. Therefore merely dropping bit17 is unauthorized by the hardware evidence. The next implementation boundary is conditional PIO sleep adoption with bounded ACK/refusal, exact unwind and diagnostics, preserving all unrelated blockers, CCF ownership, C1/C2 and existing timer/context/CIRQ safeguards. No forced gate, FIFO/data/baud/reset writes, invented PCM, memory/partition expansion or live C3 trial on the old kernel. Normal console ownership must provide its sleep capability as required by the same global handshake.

Existing #28/#31/#34 clock/idle dependencies remain open; CPU completion is not closed or hardware-impossible. User authorizes one fresh preserving candidate `out/y2linux-cpu-c3-uart-candidate/`, BOOTIMG+Y2ROOT only, with owner-only flash and no push. Software validation and a prepared first-entry/20-cycle harness must precede handoff; physical DORMANT success remains unobserved until then. Unchanged ROM/recovery provenance, protected data and six owner doc edits stay separate. Full-system suspend/electrical battery benefit remain outside scope.

## Candidate02 physical closing audit — 2026-10-03

Owner-installed candidate02 is verified at Linuxdb0234e/Rebornb71b4688, kernelcpu-idle-02/rootv1.19/releasecandidate.2, unchanged boot `f155196b-64d4-45a4-88b3-27755a1a8926`. Repo HEAD at admission76567e5 is a later receipt, not the installed source. Fresh raw SSH/source/issue evidence: `out/cpu-idle-completion-physical/20261003T144857Z-candidate02/`. Blueprint/owner scope remains real C1/C2/C3 with no fake guards/counters, no flash/push and unchanged memory/partition/recovery contracts. The existing #16/#27/#28/#29/#31/#32/#33/#34 refresh remains OPEN; no epic is activated/closed.

| Dependency / coverage | Candidate02 actual evidence | Boundary |
| --- | --- | --- |
| C1/GPT6/GPT4/PPI29/highres/NO_HZ, #28 | All four states/wakes/residency, timer continuity and13MHz readbacks pass | Preserve working architecture |
| C2/parking/MMC, #28/#33 | Natural CPU0/owner0xe;6772entries/50.669913s in60.048084s (84.38%); restores0; both media integrity/errors pass | Working narrow behavior; SD absent/electrical energy unobserved |
| Hotplug/DVFS/display/USB/radios, #27/#29/#31/#34 | 18 exact physical hotplug transitions, five OPPs, screen/playback/USB and independent Wi-Fi observer pass | Carry qualified regressions; radio endurance/actual failover not claimed |
| C3/retained clock owner, #28/#31/#34 | SPI0 released; settled CPU0/747.5MHz/both power copies clear; only UART1 PERI0x20000 fails; actual dormant calls0 | Blocked; close exact UART ownership before bounded dormant trial |
| Dormant context/CIRQ/GPT4/cache/coherency | Static readiness/software checks only; first/repeated deep wake not exercised | Unqualified; no hardware-limit proof |
| Full-system suspend/electrical battery/other release gates | Prior failures/missing measurements retained | No promotion or waiver |

Main qualification/settled preflight taint0. Two bounded exact-kernel probes then record UART1 reset/sleep/IRQ/DMA/LSR0, DLL1/DLH0, exact LCR restore and balanced CCF refs; they do not prove safe gating. Expected out-of-tree taint4096 remains truthfully until owner reboot, with no resident probes or new critical errors. No C3 trial under diagnostic scope. Final same-boot controls: C3 off, budget0/RGU disarmed, schedutil598000–1300000/coordinatorY, USB device, original screen/radio policy restored, ext4/MMCerrors0, temporary observers/files removed. Playback stays stopped because its initial paused fixture was already deleted.

The harness now waits for normal parking again after synced storage, checks owner and both power copies for20s, and keeps progress saves sparse. Fresh locked CPU90+slow-idle/suspend8+workload2 cases pass;19 native probe guard cases pass. No production kernel/root changes or new image; sealed02 hashes still match. Preserve the six preexisting owner documentation edits and unchanged provenance. The physical pass is complete, but CPU idle completion/release acceptance is blocked by UART1, not closed. Current candidate02 receipt supersedes its historical NOT_RUN/owner-flash instruction below. See [physical record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION-PHYSICAL.md) and [source/harness record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION.md).

## Candidate02 bounded UART1 divisor snapshot admission — 2026-10-03 15:34 UTC

The first nonresident exact-kernel probe retains UART1 gate0 before/after normal CCF borrow/release, reset0/0, sleep0, FCR_RD0, ACTIVE_EN0, IRQ/DMA0, LSR0; source-pinned non-destructive operands are captured in the current physical run. This disproves a held PERI reset or enabled sleep-control explanation; it does not establish transmitter-idle or a hardware limit. Same installed pair/boot, C3 disabled/budget0, expected external-module taint4096, no resident probe.

The next existing-UART observation uses the exact MT6582 BSP `mtk_uart_save`/`mtk_uart_cal_baud` LCR.DLAB select/read DLL+DLH/restore sequence. It changes only the saved register-bank selector and checks its restoration; never writes baud, FIFO, data, IRQ, DMA, GPIO, or reset. Host disables the normal coordinator, waits for all four cores, and switches radios off through their owners; both physical power copies must have MD/CONN off. Module requires CPU0, all four cores, UART1 already clocked, LCR0, and IRQ/DMA disabled before its bounded IRQ-disabled bank transaction. This excludes concurrent unused-clock handoff (its worker requires enabled coordinator/one core). Unknown/live/banked states are skipped. Exact ARM build and11 actual-function guard/cleanup tests pass; module returns EAGAIN and is not resident. The existing expected4096 taint is retained truthfully. Radio/coordinator settings restore in finally. No C3 entry, guard relaxation, live-media reset, memory/partition change, flash/push, external milestone activation/closure, or unrelated release promotion. Raw evidence remains `out/cpu-idle-completion-physical/20261003T144857Z-candidate02/`; #28/#31/#34 remain the clock-owner dependencies.

## Candidate02 UART1 read-only diagnostic admission — 2026-10-03 15:20 UTC

Fresh settled preflight in boot `f155196b-64d4-45a4-88b3-27755a1a8926` at Linuxdb0234e/Rebornb71b4688 proves CPU0-only, owner0xe, both secondary power copies0, domains0,747.5MHz, CIRQ/timer/context/PCM prerequisites available; only `clocks` fails, PERI0x00020000/UART1. SPI0 is correctly released. LCR/IER/ DMA/LSR remain0 after repeated clocked rechecks. No C3 call occurs. Supported USB/radio/DVFS/screen/coordinator settings restore, same boot/taint0/ext4errors0; new live admission verifies C3 disabled/budget0/backstop0 and exact installed pair.

The existing #28/#31/#34 clock-owner dependency needs UART reset/sleep operands, which the installed handoff diagnostic does not expose. A bounded, source-pinned read-only kernel probe is admitted for this existing subsystem. It accepts only the exact Y2 CCF UART1 handle and fixed MT6582 register windows, requires its gate already on, borrows/releases through normal CCF, skips alternate banks and live IRQ/DMA LSR, and never writes UART/GPIO/IRQ/DMA/reset controls. All eight actual probe guard/ref-cleanup fault cases and its exact installed-kernel ARM build pass. It returns EAGAIN after cleanup, leaves no resident module, and truthfully leaves the expected external-module taint until the next owner boot. Qualification results obtained beforehand retain their original taint0 receipt. No C3 entry will be attempted under this diagnostic scope. This is not production activation, hardware-limit proof, a blocker-mask relaxation, memory/partition expansion, flash/push, or an unrelated release closure. Full-system suspend remains excluded. Raw source/build/fault/live receipts stay in the candidate02 physical session.

## Candidate02 post-flash hardware admission — 2026-10-03 14:50 UTC

Owner reports installing the sealed follow-up02 and requests physical tests. Fresh authenticated USB SSH verifies Linux `db0234e7519c559031da6f427869ab683ffe0f3c`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, kernel `6.18.0-y2linux-cpu-idle-02`, root `2025.02.18-platform-v1.19`, release `1.0.0-cpu-idle-completion-candidate.2`, and boot `f155196b-64d4-45a4-88b3-27755a1a8926`. All manifest identity checks match; taint0 and mounted ext4 error counts0. Raw commands/exit codes/timestamps: `out/cpu-idle-completion-physical/20261003T144857Z-candidate02/`. Read-only issue refresh retains #16/#27/#28/#29/#31/#32/#33/#34 OPEN.

| Dependency | Current hardware admission | Required fresh result |
| --- | --- | --- |
| C1/timers, #28 | All four 13MHz timers admitted, C1 registered; prior01 physical pass retained | Four-core residency/wake and GPT6/GPT4/PPI29/highres/NO_HZ continuity |
| C2/parking/storage, #28/#33 | C2 registered; current Wi-Fi APDMA/BTIF clocks legitimately block; both MMC hosts gated/error0 | Normal radio policy/quiet parking, useful residency, exact restore, integrity |
| C3/clock owners, #28/#31/#34 | SPI0 quiet/released, UART1 retained with LSR0; C3 disabled/budget0, actual entries0 | Guarded late handoff and individual preflight; only then one bounded wake, 20 only after success |
| DVFS/display/USB/radios, #27/#29/#31/#34 | Guarded1300MHz ceiling and display handoff preserved | All five OPPs, screen/playback, USB and independent Wi-Fi regressions |
| Full-system suspend/electrical battery/other release gates | Separate failures or missing evidence retained | Excluded; no unsupported promotion |

The prepared durable device-side runner uses supported owners and restores screen/radio/DVFS/coordinator settings. Playback state is recorded before normal stop. It does not force busy UART/DMA/IRQ gates, weaken masks, reset live media, perform userspace MMIO, flash, push, change memory/partition scope, or close external milestones. C3 remains disabled on any failed prerequisite or wake; normal enablement requires repeated physical success and remaining regressions. The physical phase is admitted, not accepted. Preserve owner documentation edits and the sealed packages; unchanged ROM/recovery provenance needs no recapture.

## CPU idle hardware closing / candidate02 owner-flash boundary — 2026-10-03

Fresh final SSH receipt after build/sealing retains installed01 Linux3dfb5f5/ Rebornb71b4688, boot `e0eb2f36-7c1f-4007-99e2-81d2eae047d4`, taint0, mounted ext4 errors0. Screen off, Wi-Fi online/Bluetooth off, USB device, original DVFS/ coordinator restored; C3 disabled/budget0; temporary observer removed. Active issues#16/#27/#28/#29/#31/#32/#33/#34 refresh read-only and remain OPEN.

| Dependency | Installed01 actual evidence | Follow-up02 boundary |
| --- | --- | --- |
| C1/GPT6/GPT4/PPI29/highres/NO_HZ, #28 | Four-core WFI/wake/timer continuity passes, failures0 | Preserve; candidate02 repeat |
| C2/parking/MMC, #28/#33 | 7040entries/49.674049s of60.047965s; restores0, both media integrity/errors pass | Preserve; candidate02 repeat |
| Display/USB/demand/OPPs, #27/#29/#34 | Screen/playback/five OPPs/USB/Wi-Fi passes; clocks release normally | Candidate02 affected regressions |
| C3/clock owners, #28/#31/#34 | UART1/SPI0 PERI0x02020000 preflight reject; no actual entry | Source-correct checks and guarded late handoff/operands; actual guards/wake unknown until owner flash |
| Full-system suspend/electrical battery/other release gates | Prior failures or missing evidence retained | No promotion or external closure |

Candidate02 source db0234e/b71b4688 is freshly built and sealed, kernelcpu-idle-02/ rootv1.19. CPU owner/fault100, production366 with native skips covered, Reborn238/ fmt/clippy, fresh ARM kernel/root, config/DT/modules/ABI, QEMU/dependencies/ inventory/legal-info and preserving/root/source/checksum checks pass. C3 category SOFTWARE_READY_NEEDS_NEW_FLASH means ready for bounded qualification, not proof both clocks clear. One guarded entry and then19 more only on first success remain mandatory. Latest package:`out/y2linux-cpu-idle-completion-02-candidate/`; installed01 package remains unchanged. No reused root image; all affected/local ARM components rebuilt after final source cutoff. Exact Hardware02 fallback, Y2DATA/protected partitions, memory ABI and unchanged ROM/recovery provenance remain preserved. No unsafe MMIO/IRQ/DMA/reset forcing, guard-mask reduction, flash/push or unrelated release closure. Owner-controlled installation is the remaining boundary; see [source/hashes/action](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION.md) and [physical result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION-PHYSICAL.md).

## CPU idle candidate hardware result and follow-up admission — 2026-10-03

Fresh candidate01 run at Linux3dfb5f5/Rebornb71b4688, boot `e0eb2f36-7c1f-4007-99e2-81d2eae047d4`, completes with CPU idle acceptance FAIL: C1 passes all four cores; natural parking reaches CPU0/owner0xe; C2 adds 7,040 entries and49.674049s/60.047965s (82.72%), restore failures0. Both mounted media pass16 fsynced checksum cycles each across the two storage phases, ext4 counts0. Three hotplug cycles, all five OPPs before/after preflight, screen wake, real playback and bidirectional USB/independent Wi-Fi integrity pass. Same boot, taint0, owner screen/radio/DVFS/coordinator restored; C3 off/budget0/backstop0.

C3 is not physically working: preflight rejects PERI0x02020000, exact UART1 bit17 and SPI0 bit25, after normal radio-off/USB-role-none, CPU0-only topology, 747.5MHz cap and an armed RGU backstop. Every other reported static predicate passes; no actual cpu_suspend call occurs. Boot warnings and CCF summary show both retained, zero references, no Linux consumer. Installed diagnostics omit raw handoff operands; do not infer UART's exact busy field or fake C3 success.

Pinned exact MT6582 d53/3be93a68/krillin SPI source identifies STATUS1[0]=1 as idle; the installed predicate instead accepts0/rejects1. UART platform source identifies DMA_EN bit2 as timeout-counter metadata, unlike RX/TX bits0/1. Correct those source-backed decisions, retain unknown/live engines, capture read-only clocked handoff operands, and preserve aliased UART banks. Partial NAND/PWM handoff must retain its gate without aborting the shared CCF provider. No blocker masks, timer/context/PCM/CIRQ/OPP algorithms or memory ABI change.

The unused-clock owner also rechecks retained UART1–3/SPI0 through the existing CPU0-only, screen-off, lease-free deferrable worker, only with both radios physically off. It borrows/releases through CCF, keeps IRQ/DMA/unknown engines, never reads gated or aliased windows, avoids live UART clear-on-read LSR, and quarantines a failed gate readback. A transient loader operation no longer pins its clock forever. No new timer, coordinator-policy/hysteresis change or reset. Native fault tests cover real refs, still-busy engines, unavailable domains, unclocked skips, allocation/borrow and gate-readback failures.

Existing#28/#31/#34 track this next owner dependency; all refreshed issues remain OPEN. The original autonomous completion instruction authorizes safe source fixes and one coherent follow-up preserving candidate. Candidate02 gets a fresh kernel/root build and affected/full production verification; no reused root image, no flash/push, no external closure, no unrelated qualification claim. Current candidate01 hardware evidence stays attached to its actual source pair; candidate02 will remain physically unqualified until owner flash. Full-system suspend and electrical battery improvement remain separate unresolved gates. [Physical record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION-PHYSICAL.md), private raw `out/cpu-idle-completion-physical/20261003T130848Z-candidate/`.

## CPU idle candidate physical admission — 2026-10-03 13:13 UTC

Owner reports installing the sealed CPU idle BOOTIMG/Y2ROOT and explicitly requests hardware qualification. Fresh authorized USB SSH verifies actual Linux3dfb5f5/Rebornb71b4688, kernel6.18.0-y2linux-cpu-idle-01, root2025.02.18-platform-v1.18/releasecpu-idle-completion-candidate.1, boot `e0eb2f36-7c1f-4007-99e2-81d2eae047d4`, taint0; all identity axes match the candidate manifest. Raw admission/status/health/dmesg/timer/IRQ receipts: `out/cpu-idle-completion-physical/20261003T130848Z-candidate/`. Active issues#16/#27/#28/#29/#31/#32/#33/#34 are refreshed read-only; remain OPEN.

| Coverage/dependency | Real current evidence | Qualification boundary |
| --- | --- | --- |
| GPT6/GPT4/PPI29/highres/NO_HZ | Admitted13MHz/per-core errors0, no critical dmesg lines | Fresh bounded continuity and four-core wake |
| C1/C2/parking | Registered; natural CPU0/secondary bits0, prior baseline passes historical | Fresh counters/residency/restore and supported hotplug |
| Display/INFRA owner fixes | Current screen off: DISP0/1 blockers0, INFRA blockers0 | Screen restore/playback/USB regressions |
| C3 | Disabled, real entries0; current frequency/radio/USB/PERI/policy guards reject | Resolve through real supported owners; one RGU-backed entry only after prerequisites, then20 only on success |
| Storage/DVFS/thermal | Mounted eMMC/SD ext4 counts0, temperatures42.8–42.9°C | Fsynced integrity/runtime PM/all five OPP readbacks |
| Full system suspend/unrelated release gates | Historical failures and unqualified scope retained | Excluded from this CPU qualification; no promotion |

Pause/session state is recorded before normal playback stop. This pass uses the prepared durable device-side SSH harness with independent Wi-Fi observation, supported radio/USB/CPU controls, normal-policy parking, failure quarantine and owner-setting restoration. Ordinary C3 is retained only after repeated bounded success and the remaining regressions. No guards are weakened, no userspace MMIO or live-media reset, no flash/push, no memory/partition/calibration change, no unchanged ROM/recovery recapture or external milestone closure. The physical phase is admitted; acceptance is pending fresh evidence. Preserve the preexisting owner documentation edits and exact Hardware02 fallback.

## CPU idle owner-flash boundary — 2026-10-03 11:07 UTC

Repeated standing gap audit uses final current-boot receipts21–23 and read-only GitHub receipt24, alongside the complete CPU evidence and the fresh committed build pair. Installed baseline remains Linux131ee462/Reborn7f9df397, boot cee326c1-a5b0-447a-8eb0-dc3f39f7e2c2, taint0. C1 is WORKING on all four cores. Natural CPU0 parking plus C2 adds7182 entries/50.763741s in60.404076s; controlled 30-second enabled/disabled/re-enabled windows add25.023/0/25.016s SLIDLE, respectively. eMMC/inserted SD ext4 errors remain0. Owner screen/radio/DVFS/USB policy is restored; the temporary owned Wi-Fi observer is stopped.

| Coverage/dependency | Current classification | Next boundary |
| --- | --- | --- |
| C1/timer foundation, #28 | WORKING on installed baseline; frozen algorithm | Candidate regression through single automated SSH harness |
| C2/parking/MMC, #28/#33 | WORKING after legitimate quiet/pressure hold; storage integrity/restore pass | Preserve guards; qualify unchanged paths with new clock owners |
| C3/clock/context/CIRQ, #28/#31/#34 | SOFTWARE_READY_NEEDS_NEW_FLASH; no real entry observed | Owner installs one preserving candidate; one guarded entry, then20 only after success |
| Active DVFS/hotplug, #28/#29 | WORKING in bounded baseline tests, all five OPPs/three cycles | Candidate pre/post-dormant voltage/topology/thermal regression |
| Display/USB owner dependencies, #34/#27 | SOURCE_IMPLEMENTED and SOFTWARE_VALIDATED; baseline USB0 leak observed | Real screen-off clock release and USB runtime restore after owner flash |
| Full-system suspend, audio/radio/GPU/storage ceiling/endurance | Prior narrow evidence and unresolved gates retained | No unrelated closure or promotion from CPU idle evidence |

Fresh clean paired source 3dfb5f5/b71b4688 produces kernel6.18.0-y2linux-cpu-idle-01 and root2025.02.18-platform-v1.18. Kernel/config/DT/modules/ABI, fresh Buildroot/ Reborn ARM, production regression364 cases (five locked-host prerequisites covered by25 packaging-host cases), Reborn238 host cases/clippy/fmt, installed ARM/QEMU,383 ELF files/1403 dependency edges and release inventory/legal-info complete. Software evidence is not current-candidate hardware acceptance. Preserving-package/root/composition/checksum validation and final hash seal pass; owner-flash handoff is ready. No reuse-userspace.

Active issues#16/#27/#28/#29/#31/#32/#33/#34 remain OPEN; no external status is changed. CPU work maps to existing#28, owner dependencies to#27/#31/#33/#34. The next phase is software-ready, physically unqualified until owner flash. Recovery/fallback uses the exact Hardware02 BOOTIMG/Y2ROOT pair. Memory, ROM/ recovery provenance, partition layout, factory/calibration protection and Y2DATA preservation remain unchanged. No hardware limitation is inferred from an untested prerequisite. No milestone is closed, no default-on C3 patch, no flash or push. See [implementation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION.md) and [physical record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION-PHYSICAL.md).

## CPU idle completion admission — 2026-10-03

### CPU idle dependency audit — 2026-10-03 08:05 UTC

Current-boot receipts04–11 now physically close C1 and C2 on the installed baseline: four-core WFI counters/residency and timer continuity pass; natural parking reaches owner0xe/CPU0; C2 adds7182 entries and50.763741 seconds residency in60.404075502 seconds (84.0%), with restore failures0. Eight uncached, fsynced SHA256 cycles per eMMC/SD medium pass in each radio-off run, ext4 counts0. Three hotplug cycles and all five guarded OPPs pass. C3 remains unentered. Live screen-off still owns OVL/RDMA/COLOR/DSI and32-kHz mutex references; inherited AFE clocks remain enabled with zero references. This new evidence supersedes the admission's pending C1/C2 observations, not unrelated gates.

Exact d53dd75c/3be93a68 MT6582 `dpidle_condition_mask` requires DISP0 0x7ffff and DISP1 0xf clock quiescence, rather than unconditional DISP-domain power-off. CPU completion therefore includes the existing Reborn DRM master's screen-sleep lifecycle, balanced shared display/audio clock ownership, and read-only checks for safely retiring inactive loader clocks. Active or unknown engines remain blockers. This dependency is within the owner's explicit CPU clock/wake scope; it authorizes no new display feature, arbitrary power-domain shutdown, DMA reset, MMIO userspace access, memory layout, partition, flash or push. Existing GPU and radio ownership and active performance ceiling remain required regressions.

Owner explicitly authorizes an autonomous CPU/idle implementation and physical qualification pass on installed `y2linux-baseline-candidate`, with one fresh `y2linux-cpu-idle-completion-candidate` preserving BOOTIMG/Y2ROOT package. Only the owner flashes; no push, protected-partition or Y2DATA payload is admitted.

Read-only SSH verifies Linux `131ee4621cd583c955182f994adac5a594fb823f`, Reborn `7f9df397ab3809d52e2f1073ca93a305246e0c3a`, kernel `6.18.0-y2linux-baseline-01`, root `2025.02.18-platform-v1.17`, release `1.0.0-baseline-candidate.1`, boot `cee326c1-a5b0-447a-8eb0-dc3f39f7e2c2`, taint0, matching the sealed package. This supersedes installed Candidate4 identity only; retained Fix02 passes/failures remain historical evidence. Private receipts: `out/cpu-idle-completion-physical/20261003T074026Z/`.

Initial current coverage: GPT6/GPT4/PPI29/CNTFRQ13MHz/highres/NO_HZ admitted; all five guarded OPPs admitted; CPU0-only coordinator-owned topology observed. C1 registered/enabled with accumulated residency, fresh continuity qualification pending. C2 registered/enabled but entries0, live APDMA/BTIF blockers while Wi-Fi runs; bus rejection0 and MMC runtime gating intact. C3 registered/default-off, entries0; current frequency, domains and clocks reject its read-only preflight. No new idle-state pass is claimed. Existing storage tuning remains Candidate4.

GitHub active issues refreshed read-only: #16/#27/#28/#29/#31/#32/#33/#34 OPEN; CPU/timers/idle map to #28 and storage/radio/GPU interactions to #33/#31/#34. Their older descriptions do not override current source or hardware receipts. No external issue or milestone is closed or changed. Every unrelated hardware, audio/distribution/endurance gate retains its existing classification.

Scope: characterize C1 then freeze its proven architecture; decode/fix actual C2 clock/device ownership; resolve every source-backed C3 topology/deadline/CIRQ/PCM/ context prerequisite, without masking blockers or undocumented register writes. Bounded existing runtime controls and workload/storage/network regression tests are authorized, with safe abort and state restoration. First C3 entry requires all real prerequisites; no repeated hammering of a failed deep path. Preserve GPT6/GPT4/PPI29, schedutil/QoS/thermal, hotplug, all guarded OPPs, exact memory/ partition layout and Hardware02 fallback. Full system-suspend acceptance remains a separate gate. Coherent source fixes and fresh software/package qualification precede owner flash and current-candidate physical acceptance.

Track implementation and physical results in [CPU idle completion](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION.md) and [physical qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-IDLE-COMPLETION-PHYSICAL.md).

### USB clock dependency audit — 2026-10-03

Current-boot receipt12 uses supported USB role `none` over the verified Wi-Fi observer. MUSB changes active ->suspended and returns active on restoring `device`; same boot, no source/partition changes. PERI USB0 bit10 nevertheless remains active in the exact C3 blocker mask. Source confirms the glue adopts that gate without a CCF consumer. The MT6582 d53 USB PHY's usb_enable_clock explicitly owns MT_CG_PERI_USB0 through enable_clock/disable_clock.

This CPU completion boundary now admits a balanced USB0 CCF consumer and MUSB runtime save/gate/enable/restore hooks, preserving attached sessions, DMA/IRQ refusal, PHY sequencing and ordinary role-based detach/reconnect. No blocker bit is removed. Only the existing controller is modeled; no host, VBUS, PHY-retune, power-domain, memory, partition or flash scope is added. Fresh USB regressions and same-boot role recovery are required. The next C3 harness may intentionally release USB through the existing role interface while its durable device-side job runs, then restore transport. Radios and USB may both legitimately prevent C3 until their owners have quiesced.

### CPU idle source/build boundary audit — 2026-10-03

Fresh same-boot receipts04/10/11/12/16/17 now establish four-core C1, useful C2, physical secondary hotplug, all five OPPs, the USB0 ownership leak, actual44.1-kHz playback with PlaybackNormal demand/all-core restoration and screen-off/on userspace transitions. Taint0; mounted eMMC/SD errors0; C3 has not entered. The source pass preserves the working timer/C1/C2/MMC/DVFS/parking algorithms and repairs the exact C3 clock/context/deadline/CIRQ/PCM prerequisites. Targeted native fault tests and fresh Reborn host/clippy checks pass; full fresh software and package qualification is next. This crosses a software build boundary only: no new hardware/memory/partition scope, milestone closure, flash or push. All unrelated full-suspend/storage-ceiling/audio/distribution gates remain open. One coherent CPU idle preserving candidate and its automated20-cycle harness are the next deliverables. CPU hardware completion remains pending owner flash.

## Integration build boundary — 2026-10-02

Handoff closure: fresh source `02eb735` / `72e94b2` is now sealed as `Y2LINUX-FEATURE-COMPLETION-01`,350 production and238 Reborn tests passed, ARM/QEMU/package checks passed. READY FOR HARDWARE DECISION RUN only. Installed Candidate4 and retained Fix02 physical evidence below are unchanged; no new physical qualification, public distribution or milestone closure.

The read-only connected-device receipt establishes installed Candidate4 Linux `dcbd7d1` / Reborn `b92d312`, boot `159f7c81-ab89-4440-bc89-df827dd8bc34`, taint0. Current storage negotiates HS200/SDR104 near200MHz; this narrow idle observation is not endurance acceptance. PM records are invalid/no-attempt; C2 has no observed entries and C3 remains disabled. Fix02 remains the broad physical qualification, with full-resume/C2/loaded-USB failures unresolved physically.

The authorized fresh build uses Linux `02eb735` and Reborn `72e94b2`, including source-backed tuning recovery, truthful PM evidence, codec integration, Productv2 and tester/release safety. No partition/memory/voltage scope expansion, physical qualification or milestone closure. Only one preserving owner-local integration candidate is admitted; all existing hardware and public-distribution gates remain. No flash or push. The implementation pass records final software/build outcomes.

## Feature completion implementation admission — 2026-10-02

The owner now explicitly authorizes the ten-lane implementation campaign and one fresh preserving candidate; the earlier planning-only limit is superseded. Starting Linux `9ac2c0b7018ce707ec15f8845daf58ce38ec18a0`, Reborn `eb64b8b21058eacb1ef183f7570cca8100cbbb46`. Existing dirty planning documentation is preserved. The 233-feature inventory remains the work queue; no fresh broad audit or unchanged ROM/recovery provenance acquisition is substituted for implementation.

Standing boundary review uses the retained Fix02 real hardware result (awake timers/OPPs/parking/MMC/staged PM pass; full resume, C2 and loaded USB fail), candidate3 storage measurements (200 MHz CRCs, bounded 100 MHz read pass), and candidate4 source/304-test receipt (not hardware acceptance). Boot polish source is newer than the planning snapshot; its build is unfinished, not a sealed receipt. GitHub #16/#27/#28/#29/#31/#32/#33/#34 refreshed read-only and remain OPEN. Every existing coverage classification is carried forward: no new physical pass or milestone closure follows from this activation. Scope maps platform to #27/#28/#33, audio/radio to #29/#31, product/release to #16/#32/#34.

No memory-map, partition, voltage or clock-limit change is admitted. Preserve BOOTIMG/Y2ROOT-only installation, Y2DATA and exact Hardware02 fallback. Current SSH identity is attempted read-only; absence of access does not invalidate retained evidence. Parallel source lanes continue across independent blockers. Source-ready changes require targeted tests, then fresh integrated software/build/package checks. Hardware acceptance and public redistribution remain separate gates. No flashing, push, destructive device operation or external issue mutation. Track findings in [the implementation pass](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-COMMUNITY-BETA-IMPLEMENTATION-PASS.md).

## Community beta planning audit — 2026-10-02

Later owner decision supersedes the initial minimal-subset proposal: the first community beta must be polished and feature-complete. [Master factual audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-COMMUNITY-BETA-FEATURE-AUDIT.md), [three-pass/seven-day plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-COMMUNITY-BETA-PLAN.md), and [233-row inventory](https://github.com/schulzcode/y2linux/blob/HEAD/docs/release/Y2-COMMUNITY-BETA-FEATURES.json) preserve implementation/evidence while91 old C/D rows become required or hardware-conditional. This is a documentation-only planning boundary, not hardware/memory/production implementation authorization or milestone closure.

Retained hardware basis: Fix02 awake CPU/timer/DVFS/MMC and staged PM passes, loaded USB/full-resume failures; candidate3 reported200MHz SD CRCs and bounded100MHz read pass. Current Linux `e2dd583` records candidate4 built from `dcbd7d1`,304 software tests PASS, not flashed; Reborn `b92d312` unchanged. Candidate3 is latest reported installed; no new live device observation or unchanged ROM/recovery provenance acquisition. Exact AFE fetch/rate evidence, C3 entry, final same-boot wake, optional codec peer/load evidence and public distribution remain open.

Source, owner target and retained physical evidence now require native meaningful24-bit/rates where supported, viable Classic codecs, C2/conditional C3, full sleep/wake, admitted1196/1300MHz, highest robust storage, DMA USB, battery/charging and polished Productv2. Fallback existence does not close these features. New independent product/maturity/distribution axes replace old priority meanings; unresolved required features delay release rather than silently reverting scope. Three coherent passes precede one integrated RC and qualification/endurance.

Existing issue context remains the prior read-only snapshot #16/#27/#28/#29/#31/#32/#33/#34; not refreshed or mutated during this reclassification. Map platform completion to #27/#28/#33 and retained M4#30 physical gates, audio/Bluetooth to #29/#31, product/release to #16/#32/#34. Historical M4 closure is not new physical acceptance. Before later implementation/hardware admission, reconcile current issue state and affected boundaries separately; this plan authorizes none. No external milestone, issue, Git identity or source was changed.

Current reading order, 2026-10-01: The [Fix03 implementation boundary](#cpu-final-fix03-implementation-boundary--2026-10-01), the [Fix02 physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX02-PHYSICAL-QUALIFICATION.md) and [current platform state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md) supersede older candidate admission/"next" text below for today's acceptance. The Fix02 physical report is the authoritative hardware result until Fix03 receipts exist. The [knowledge-base maintenance receipt](#knowledge-base-reconciliation--2026-09-28) changes navigation and source/physical summaries only; it does not open a hardware, memory, production or milestone boundary. Older audit entries remain in their original sequence for evidence and permission history.

## CPU Final Fix03 implementation boundary — 2026-10-01

The owner activates the single Fix03 correction batch planned by the Fix02 physical run (2026-09-29, private evidence `out/cpu-final-fix02-physical-qualification/20260929T152328Z/`, 460 sealed files). The standing audit is repeated narrowly from that real-hardware evidence. There is no new hardware subsystem. The retained-SRAM window, DRAM layout and boot partitions are unchanged, and production scope remains the same preserve-data BOOTIMG/Y2ROOT pair with the exact Hardware02 fallback. This activates implementation and one candidate, not hardware acceptance, a flash or an external milestone closure. Starting Linux `19ab970` / Reborn `77cf83e`. Open issues refreshed read-only: #16/#27/#28/#29/#31/#32/#33/#34 OPEN; M4 #30 is closed, and its remaining physical gates are tracked here and in the Fix02 report.``````````````````````````````````

| Coverage / owner | Fix02 physical evidence | Fix03 scope (nothing broader) |
| --- | --- | --- |
| Full suspend, M4 #30 | SPM wake 0x20, resume stamp, every device complete; reset 30 s later before Y2_PM_EXIT | Mark and ping the backstop after dpm_resume_end, console resume, platform_resume_end, thaw and PM_POST_SUSPEND; ms stamps and stage entries in the retained ring; RGU status decoded into boot.json. The next RTC attempt names the stalled call. The call is fixed only after that. |
| SLIDLE, M4 #30 | Clock mask 0 radios-off; slow_reject_bus 0 → 20809; TOPCKGEN+4 reads 0x0 | Accept the source-backed bus-DCM baseline {0x00 reset default, 0x0f after stock bus_dcm_disable}; keep the verified 0x8f write and exact restore; same predicate for deep idle and the read-only preflight |
| Loaded USB, M2 #28 / M5 #31 | 0/10, irq_overflow at 513 per 10-ms jiffy; ISR, DMA-IRQ and DMA-program counts match one interrupt per packet event | Progress-aware storm guard: count only interrupts without new DMA programming, plus a hard per-jiffy ceiling above the HS bulk maximum; still terminal |
| Coordinator / SD / DVFS label | Wake render burst doubled the hold; drop_caches remounted /media/sd; admission_error=1 is success | A display/workload/input restore right after a pressure restore undoes that escalation; SD inventory keyed on dev_t, diskseq and CID; admission reports 0 on success |

Preserved as regression requirements: all Fix02 physical passes (timers, highres/NO_HZ, hotplug, QoS, thermal authority, WFI, MMC gating, parking, 1196/1300-MHz DVFS, SRAM self-test/retention, staged PM, charger refusal). C3 stays default off. The screen-off frequency ceiling and the BSP 110/120 °C trips are recorded as owner decisions, not defects, and are not changed. The next physical gate is a regression run, SLIDLE radios-off, USB 10 × 1 MiB, then RTC → Power → 5 cycles. Ready for implementation; hardware acceptance is still blocked on that owner run.

## CPU Final Fix02 implementation boundary — 2026-09-28

The owner activates the single coherent Fix02 correction planned by the Fix01 closing boundary, using that real-hardware evidence. The standing audit is repeated narrowly: scope is unchanged hardware (no new subsystem), unchanged memory contract and the same preserve-data BOOTIMG/Y2ROOT production scope; it activates implementation and one candidate, not hardware acceptance or an external milestone closure. Starting Linux `0b8f810` / Reborn `6ddc553`.

| Coverage / owner | Fix02 software change | Remaining physical gate |
| --- | --- | --- |
| Deeper CPU idle, M4 #30 | MSDC runtime early return removed; MT6582-only register image verified across PERI CG gating; SLIDLE refusal attribution; read-only C3 prerequisites | gating, C2 entries/residency, C3 stays default off |
| Coordinator, M4 #30 | sustained time-weighted quiet, 1-s saturation demand, escalating hold; readiness-service Python spawn per 3 s removed; Reborn screen-off loop 50 ms | parking 3→2→1 and restore on the device |
| High-bin voltage, M4 #30 | PWRAP predicate reconciled: preloader writes 0x1ff, 7-bit arbiter reads 0x7f (M2-PWRAP-01 photo); raw operands exposed | 1196/1300 MHz voltage readback |
| PM/wake, M4 #30 | awake SRAM self-test and retention report, earlier stages, device-callback ring, owner-armed RGU warm-reset backstop, charger classification | staged, RTC and Power same-boot wake |
| Transport, M2 #28 / M5 #31 | terminal USB fault attribution with snapshot; 1-s supply and 10-s write-free reconnect tolerance; DMA/PIO fallbacks unchanged | repeated loaded transfers with Wi-Fi observer |

Receipt: [Fix02 implementation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX02.md), [source ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX02-SOURCES.md) and the prepared [physical qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX02-PHYSICAL-QUALIFICATION.md). Preserved: timers/highres/NO_HZ, hotplug, conservative OPPs, schedutil, eight QoS classes, thermal authority, WFI, bounded playback and CONSYS isolated retry. No flash or push. The owner run on 2026-09-29 passed timers/QoS, MMC gating, parking, 1196/1300-MHz DVFS, SRAM retention and staged PM, and failed SLIDLE (bus-DCM predicate), full RTC resume completion and loaded USB upload; M4/M5/M6 gates remain open.

## CPU Final Fix 01 implementation admission — 2026-09-27

Owner authorizes one focused correction and one preserving candidate, no flash or push. Starting source Linux `aadcaa40a486cda555c859f131a2dcdb664b2233`, Reborn `afcf9ffa1bc45073e97520d592c0284ce73fefcf`. The authoritative physical pair is Linux `ff586df` / Reborn `afcf9ff`, kernel6.18.0-y2linux-cpu-final, root2025.02.18-platform-v1.6. Evidence is the completed [physical qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-PHYSICAL-QUALIFICATION.md) and private receipts20260927T161145Z; no new device access is needed for admission. Open GitHub inventory refreshed read-only: #16/#27/#28/#29/#31/#32/#33/#34 remain OPEN.

| Coverage / existing issue | Physical evidence and authorized correction |
| --- | --- |
| CPU/timer/idle #28/#34 | GPT6 preflight FAIL, legacy/dummy highres0/nohz0; lower OPPs/hotplug/WFI PASS. Fix inherited ownership, precise predicates, GPT4/PPI29 lifecycle; preserve fallback. SLIDLE blocker0xe07800 and single-CPU topology require source-backed clock lifecycle/coordinator correction, not deleted guards. |
| DVFS/thermal #28/#34 | bin0 identified,216=0/21e=48/1.15V; high admission-95. Reconcile software versus hardware selector with exact stock evidence; preserve sequencing, readback/fault/thermal ceilings. |
| Reborn/QoS/audio #29/#32 | Kernel leases/thermal and bounded no-XRUN playback PASS; fragmented app writes EINVAL. Fix one complete payload and producer/lifetime integration; no application MHz policy. |
| Suspend/USB/radio #27/#31/#34 | Battery freezer/devices/platform/processors/core PASS, USB quiescent restore and isolated CONSYS retry PASS. Full RTC nonreturn FAIL; preserve those paths, repair wake/context and persist unsafe-interval stage diagnostics. Charging refusal remains, PM unwind WARN must be corrected. |
| Storage/recovery/security #16/#28/#32/#33 | Recovery after owner restart has clean filesystems/new boot; no reset cause. Exact known-good fallback remains immutable; BOOTIMG/Y2ROOT only, no Y2DATA/protected/loader writes or memory reservation changes. |
| Acceptance #32/#34 | READY for focused implementation and complete current-source candidate validation. Hardware success remains pending one owner-controlled Fix01 qualification; automatic deep suspend/C3 gates remain. |

Retained-diagnostic memory audit: exact stock `mt_map_io` descriptor maps physical0x00100000/64KiB and `ram_console_early_init` reserves 0x0010dc00..0x0010f7ff for reset-retained console evidence. Fix01 uses only260 bytes of this existing, otherwise unowned SRAM allocation. No DRAM carveout, ROM/LK/preloader, PMIC spare or boot-mode field changes. Two checksum slots and a stackless resume stamp are paired with filesystem receipts outside noirq. Reset retention remains an explicit next-device check; cold power cannot retain SRAM. This narrowly scoped diagnostic owner is admitted, not a new memory plan.

Candidate-build boundary audit: the same physical evidence remains authoritative. Retained Y2 preloader/LK now identifies legitimate GPT4 control0x31 as the old combined admission conflict; stock PMIC initialization explains216 mode0 versus stock kernel mode1. All seven0xe07800 owners are decoded; balanced CCF and a slow system-idle coordinator preserve real blockers. Full entry gains stock SRAM stages, exact wake/vector checks and balanced charger refusal unwind. Focused current-source tests pass (70 tests, one native-dependency case deferred to the full host profile); Reborn192 tests/fmt/strict Clippy pass. Admit one fresh kernel, Buildroot/ARM/Reborn and broad software/package qualification from isolated clean commits. Preserve exact accepted Hardware02 fallback. No physical success, C3 activation, automatic full-suspend promotion or new hardware scope is inferred.

Candidate seal admission: the same physical failure/pass inventory remains the hardware authority. Fresh code Linux0de6e95/Reborn36db186 passes kernel/config/ DT/modules/ARM ABI, fresh Buildroot/ARM and Reborn ARM,215 locked regressions (218 total;3 native cases covered by12 fresh host tests),192 Reborn tests/fmt/ strict Clippy, installed ARM benchmark,382 ELF files/1396 dependency edges, 105 pinned source packages and license collection. New runtime objects passW=1 without warnings. Admit the single preserving package seal after successful package/ext4/on-image validation; exact Hardware02 fallback hashes remain b2a2c3bc/63dbd0a1. No highres/SLIDLE/high-OPP/full-wake electrical acceptance is inferred. Host SSH qualification tools check same boot/taint, actual serviced wake IRQs, bounded playback and USB/WLAN round-trip hashes; no device execution here.

Closing software boundary: preserving package/ext4/on-image validation now PASS; BOOTIMG82b38fd3/Y2ROOT26aa01ce are the single Fix01 payload pair. Close the focused software implementation/candidate qualification scope, retain full physical acceptance pending owner installation and one prioritized SSH run. Exact initial user diffs and roadmap text are preserved; no flash/push/device access or identity configuration changes. Existing conservative/hardware qualifications stand alone.

Unrelated user documentation/assets are retained. Source/ROM/recovery provenance is unchanged and is not reacquired. This admission does not reopen architecture, qualify high OPPs/full wake, or authorize a planning epic as hardware work.

## CPU Final physical qualification boundary — 2026-09-27

Standing boundary audit uses the fresh physical report and private receipts under `out/cpu-final-physical-qualification/20260927T161145Z/`, not software-test claims. Exact installed Linux ff586df/Reborn afcf9ff and all declared release fields match. Original boot18248d38-f426-4090-add7-a99a7a3a067d; after the first full RTC sleep failed to return and lost recovery, owner restart yields 2aff9ecf-dac0-4479-913e-46dc343964d0. Fresh recovery taint0, root/data/SD rw/error0, all4 online, schedutil598–1040MHz, C3 disabled, no alarm/pm_test/load left.

| Coverage / existing issues | Real result / remaining production gap |
| --- | --- |
| CPU/timer/idle #28/#34 | Lower OPP/hotplug/WFI bounded PASS. GPT6/GPT4/PPI29 boot admission FAIL; highres/NO_HZ inactive; C2 blocked0xe07800, C3/deadline/CIRQ replay unqualified. |
| Power/DVFS/thermal #30/#34 | PMIC216=0 blocks hardware-selector admission, high bins gated; lower stock voltage/readback PASS; thermal cooling cap overrides QoS. No voltage-transition/high-bin electrical qualification. |
| Workload/Reborn #29/#32/#34 | Kernel leases/expiry/thermal interaction PASS; actual Reborn partial formatted device writes getEINVAL, semantic hints FAIL. |
| Suspend/USB/radio #27/#31/#34 | Freezer and battery devices/platform/processors/core PASS; quiescent MUSB4suspends/8restores, no IRQ storm. Core radio mandatory-STP timeout isolated and second boot succeeds. Full RTC suspend FAIL/nonreturn, no same-boot wake. Attached charging.prepare refusal unwind WARN remains. |
| Audio/GPU/display #29/#32 | Silent44.1/24-96 resampled native playback no XRUN; screen-off GPU gating and staged DSI restoration observed. Full post-resume/audio/peer quality unqualified. |
| Storage/recovery/security #16/#28/#32/#33 | Recovery SSH and clean filesystem checks PASS after restart; no panic/reset cause retained. Original media/protected regions preserved, only owned fixtures removed. Recovery boot options present, not reboot-qualified individually. |
| Acceptance/production #32/#34 | Observation sweep complete subject to owner stop rule for recovery loss; candidate NOT accepted as normal CPU Final. One prioritized coherent fix batch documented; no blanket production capability/epic promotion. |

[Physical result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-PHYSICAL-QUALIFICATION.md) distinguishes implementation, observed runtime and qualification. Scope did not add hardware, memory layout, package/loader writes or calibration acquisition. Unchanged ROM, recovery and release provenance is not repeated. Existing external inventory was refreshed read-only at activation; cited issues remain open, no external mutation.

Decision: close this first observation sweep, keep automatic suspend/C3 at existing qualification/default-off gates, preserve successful runtime fallbacks and pursue the documented single CPU Final Fix Batch separately. Loss of USB/Wi-Fi recovery stopped further full-suspend/C3/stress testing; owner restart is not a wake pass. No implementation edits, builds, flashes, commits/pushes or identity changes in this physical sweep. Documentation-only closure requires targeted diff/evidence validation, not a kernel build or another unchanged hardware campaign.

## CPU Final physical qualification activation — 2026-09-27

Owner confirms CPU Final already flashed and explicitly authorizes one autonomous, bounded real-device sweep, including hotplug, admitted OPPs, workload/idle tests, staged suspend and guarded RTC/Power wake. No implementation source changes, build, flash, protected-region access, calibration acquisition or data reset. Pinned USB SSH receipt `00-identity-boot` under `out/cpu-final-physical-qualification/20260927T161145Z/` verifies Linux `ff586dfff2b5e7abd28af339c055375307308f1f`, Reborn `afcf9ffa1bc45073e97520d592c0284ce73fefcf`, kernel `6.18.0-y2linux-cpu-final`, root `2025.02.18-platform-v1.6`, release `1.0.0-cpu-final-candidate.1`, API1 and boot `18248d38-f426-4090-add7-a99a7a3a067d`. Taint0; root/data/SD rw, all ext4 error counters0. CPU55C/PMIC53.315C at admission.

| Coverage / existing issue | Real admission evidence / next boundary |
| --- | --- |
| CPU/timer/idle #28/#34 | Exact candidate boot observed; GPT6 boot preflight rejects, legacy timer/dummy events selected, highres/nohz inactive. Preserve fallback and continue independent runtime tests. C2 enabled with busy aborts; C3 default off. |
| DVFS/thermal/power #30/#34 | Bin0 admitted as silicon, automatic voltage admission returns -95, ceiling1040MHz, voltage1.15V, no voltage fault. Exercise admitted lower OPPs only; no manual high-bin override/overheating. |
| USB/radio/suspend #27/#31/#34 | SSH works; CIRQ ready but never entered. Historical USB overflow/WMT failure remains until tested. Guard staged suspend, reconnect automatically; stop whole sweep only for owner's severe safety/recovery conditions. |
| Audio/GPU/display/Reborn #29/#32 | Preserve native device/app ownership. Use supported controls and existing fixtures; physical observations requested only when unavoidable. |
| Storage/recovery/security #16/#28/#32/#33 | Clean rw filesystem admission; preserve all user data/keys/protected regions and exact accepted fallback. No root/package/loader writes. |
| Qualification/production #32/#34 | ACTIVE for this exact candidate, no blanket capability promotion/epic closure. Capture commands/outputs/status/timing/identity privately; record PASS/FAIL/PARTIAL/NOT_TESTED separately from implementation. |

Continuation receipt20: freezer PASS, devices refused at charger.prepare with -16 while charging, then PM unwind WARN/taint512; same boot and clean filesystems, USB/CPU/controller restoration retained. No MUSB/SPM entry occurred in this test. The charger has an explicit source-backed active-USB sleep guard; do not bypass it. Owner's battery/RTC/Power qualification now needs the unavoidable physical USB unplug, with private persistent local logs, RTC recovery alarms, local thermal/ filesystem/boot guards and Wi-Fi status observation. Abort further suspend stages on any failed local stage; USB replug is the recovery/log retrieval path. No source change, charger override or new electrical assumption. This is within the owner's explicit testing authorization. External inventory refreshed read-only: existing #16/#27/#28/#29/#31/#32/#33/#34 remain OPEN.

Decision: READY for independent bounded physical tests with existing timer and OPP fallbacks active. Timer/high-bin failures are observations, not a reason to stop the whole sweep. End audit will use collected results and propose one fix batch if needed. Existing external epics remain open; no external mutation.

## CPU Final candidate boundary — 2026-09-27

Owner's concentrated implementation scope is complete at the source/candidate boundary: Linux `ff586df`, Reborn `afcf9ff`. Exact original Hardware02 `76bc822` / `95747e0`, boot prefix `b93cda16`, remains the retained real-hardware baseline. Hardware Final handoff receipts12/16 prove four local timers, highres/NO_HZ, GPT6 rollover and checked hotplug; older receipt49 proves CPU3/2/1 restoration but records USB overflow and mandatory-STP radio timeout. CPU Final corrects those software paths without replacing the historical failed result. No device was accessed. ROM/recovery/calibration provenance and reserved memory are unchanged; no repeat acquisition or physical qualification campaign applies. Fresh complete software validation uses the exact pair above; existing unrelated worktree documentation/assets stay outside the candidate source checkout.

| Coverage / existing issues | Refreshed classification and boundary decision |
| --- | --- |
| Boot/recovery/security #16/#28/#32 | NARROW PHYSICAL PASS retained; CPU recovery options IMPLEMENTED/HOST TESTED. Loader and protected areas unchanged, exact accepted Hardware02 pair retained as fallback. New boot is independently unqualified. |
| Storage/filesystems #28/#33 | Retained narrow unit results unchanged. BOOTIMG/Y2ROOT-only scatter, no USRDATA image, no Y2DATA reset or schema change. Local package validation is the final preservation gate. |
| CPU/timers/idle #28/#34 | IMPLEMENTED/HOST TESTED: GPT6 stable counter, PPI29 per-CPU events, GPT4 Linux broadcast, highres/NO_HZ lifecycle, CNTFRQ/CPU PM context, automatic preflight SLIDLE, distinct stock dormant PCM/CIRQ/GIC/coherency. Dormant is experimental/default off, CPU0 with others physically off; stricter media/clock preflight stays binding. |
| DVFS/thermal/power #30/#34 | IMPLEMENTED/HOST TESTED: exact bin0/voltage admission, transition ordering/rollback, schedutil, expiring QoS/boosts and thermal maximum authority. Unknown bins/faults retain conservative stock OPPs. Battery/current/pack-sensor limitations unchanged. |
| USB #27/#32 | IMPLEMENTED/HOST TESTED: system gadget disconnect/DMA refusal, sampled stale W1C cleanup, endpoint-before-gate restore, preserved runtime/live-DMA completion status and terminal fault masks. No new physical resume or VBUS qualification. |
| Suspend/Power/RTC #30/#34 | IMPLEMENTED/HOST TESTED: CIRQ bracket, Linux CPU/cluster context, normal PCM reinstall, Power/RTC wake masks, helper stage/error restoration. Full same-boot resume remains independently unqualified; explicit existing qualification interface remains default. |
| GPU/display/input/memory #28/#34 | Working GPU01 corrections/reservations preserved. CPU low-power preflight honors domain/clock ownership; no forced peripheral clock loss, no memory reclaim or new physical load claim. |
| Audio/DAC #29 | Existing ALSA/AFE/CS43131 PM/volume ownership retained; QoS latency leases bound heavy playback and thermal remains authoritative. New suspend audio quality and unrelated wider native transport remain unqualified. |
| Wi-Fi/BT/codecs #31 | IMPLEMENTED/HOST TESTED: one isolated controller boot retry after complete power/DMA/rail/clock teardown; firmware/interface readiness before success, radio errors propagate. y2-bt-reconnect remains sole automatic reconnect owner; prior peer/codec qualifications unchanged. |
| Reborn/library/platform #32/#33 | IMPLEMENTED/HOST TESTED: scoped artwork workload, independent coalesced interaction lease, immediate screen-off release, semantic API with crash/expiry cleanup. Host tests/fmt/strict Clippy and fresh ARM build/QEMU are release-facing software gates. |
| Packaging/updates/endurance #32/#33 | One preserving candidate, exact fallback and source/license/validation handoff; no flash/push or OTA application. Existing open epics #16/#27/#28/#29/#31/#32/#33/#34 stay open; no hardware milestone or qualification promotion. |

Decision: READY for the single CPU Final software-candidate handoff. Fresh build/release checks and local package/data/exact-fallback validation all pass. The package is `out/y2linux-cpu-final-candidate/`; its receipts identify the built pair. Implementation, admission and physical qualification are separate flags. No new hardware authorization, measurements or successful suspend receipt is inferred.

## CPU Final implementation admission — 2026-09-27

Owner explicitly authorizes a concentrated CPU/timer/DVFS/idle/suspend implementation and one preserving candidate; no flash/push or new physical campaign. Entry Linux `0b0e3e0`, Reborn `5b5d23b`; unrelated documentation/assets remain preserved. Real receipts from Hardware02 (`76bc822` / `95747e0`, boot `b93cda16`) remain the hardware baseline: four local clockevents, highres/NO_HZ on four cores, GPT6 rollover continuity, checked 1–4-core hotplug, clean filesystems and taint0. Historical processor-stage secondary restoration passed; devices-stage USB overflow and radio timeout are failures requiring implementation corrections, not qualification. Unchanged ROM/recovery/source provenance is retained without repeating acquisition.

| Coverage / owner | Boundary decision |
| --- | --- |
| CPU/timer/idle #28/#34 | IMPLEMENTED/PARTIAL: finish dormant CPU context, runtime PCM, CIRQ and GPT broadcast integration; use distinct timer owners and Linux CPU PM. |
| DVFS/thermal #30/#34 | Source-backed stock bin0 and voltage sequencing already present; automatic supported-bin admission and fault/recovery policy within stock limits authorized. |
| Suspend/radio/USB/audio/GPU #27/#29/#30/#31 | Preserve GPU01 and device ownership; correct restoration ordering using retained failure receipts. Physical same-boot wake remains independently unqualified. |
| Boot/storage/memory/recovery #16/#28/#32/#33 | Preserve loader, reserved memory, Y2DATA and protected partitions. Single BOOTIMG/Y2ROOT candidate plus exact Hardware02 fallback; no hardware operation. |
| Qualification/release | Build/tests/package validate software only. No epic closure, external status promotion or claim of new hardware success. |

READY for CPU Final implementation under explicit owner direction. Retained physical evidence supplies the audit; absence of new hardware confirmation does not prevent independent source implementation. Architecture/package changes get full final software validation. The prior qualification-first sequencing is superseded for this pass; hardware qualifications remain separate flags.

## Hardware Final campaign activation — 2026-09-27

Owner explicitly combines Hardware 03–05 into one engineering campaign and one final preserving candidate. This supersedes the sequential batch/flash plan. Entry source Linux `c53963b`, Reborn `95747e0`; pre-existing documentation and asset changes are retained separately. Private receipt `00-identity-census` in `out/hardware-final/20260927T122702Z-hardware02/` verifies installed Linux `76bc822` / Reborn `95747e0`, Hardware 02 candidate.4, boot `b93cda16-4e08-4ead-a74a-c85f4cccaa11`. Pinned USB SSH works; taint 0, root/data/SD ext4 counters 0, quick health OK. GitHub open inventory refreshed: #16/#27/#28/#29/#31/#32/#33/#34 remain open; historical #30 is not a broad pass. Unchanged ROM/recovery/source provenance is not repeated.

| Coverage / issues | Evidence and admission |
| --- | --- |
| Boot/recovery/security #16/#28/#32 | Hardware 02 exact metadata and clean boot observed. Preserve installed pair/fallback, keys, loaders, protected partitions and Y2DATA. OTA apply still requires explicit owner approval. |
| eMMC/SD/filesystems #28/#33 | Real IOS 8/4-bit high-speed SDR, actual 24,999,971 Hz at 3.3 V; requested 50 MHz differs from capped actual rate. Admit bounded 13/25/50 controls and guarded scratch measurements; no DDR/UHS claim. |
| USB #27/#32 | Inventra DMA active, six DMA IRQs, zero DMA errors at census; not a throughput qualification. Compare separated RAM/storage transfers and retain PIO boot fallback. Host VBUS remains evidence gated. |
| CPU/timer/idle #28/#34 | Four arch_sys_timer clockevents, arch_sys_counter clocksource, GPT6 13 MHz calibration logged. Continuity/hotplug/effective NO_HZ, voltage sequencing and deeper states still need evidence. |
| GPU/display/input/memory #28/#34 | Health observes render/display/input; retained stock-backed 500.5 MHz and reservations unchanged. Current load/power/memory/endurance still open. |
| Battery/charging/low battery #30/#34 | Current sensors observed; historical limits/ADC evidence retained. No measured current/SOC/pack temperature or calibrated shutdown reserve. Source and load-curve investigation authorized; no guessed values. |
| Suspend/RTC #30/#34 | pm_test none; earlier USB overflow/radio restore failures remain unsuperseded. One persistent stage plus recovery verification before advancing; Power/RTC same-boot wake unqualified. |
| Audio/DAC #29 | Hardware 02 carries native ALSA sink fix. S16/44.1 and short 48 kHz historical results retained; current product listening/endurance, wider DL1, clocks and DAC topology require evidence. |
| Wi-Fi/BT/codecs #31 | Current health OK; prior checked DNS/TCP/SBC narrow passes retained. Full peer/AVRCP/coexistence/optional-codec qualification and distribution review remain open. |
| Library/OTA/endurance #32/#33 | Existing matched 1k/10k/20k baselines retained. Rerun at measured final storage setting. Root install/rollback and long workloads not qualified by health. |
| Build/package | One current-source host/ARM/Buildroot/image validation boundary after accumulated corrections. No candidate built at activation; no stale binaries certify new source. |

Decision: **READY for coordinated census, independent source investigation and evidence-backed implementation**, not hardware closure. All independent work continues after ordinary subsystem failures. An intermediate image is allowed only for an identified physical kernel dependency that blocks remaining work; record why existing source/host/QEMU evidence cannot answer it. Final package is `out/y2linux-hardware-final-candidate/`, BOOTIMG + Y2ROOT only, with one owner installation/qualification boundary. Current electrical and physical gates stay binding. No issue is closed or external status promoted by this audit.

## Hardware 02 candidate handoff — 2026-09-26

This is the candidate/admission boundary for the owner's existing hardware ceiling authorization. Installed Physical 01 remains Linux `198fa7c` / Reborn `feb530f`. Recovered receipts 49–52, all earlier matched benchmarks, source `76bc822` / Reborn `95747e0`, exact image hashes, final release checks and the open issue inventory support this review. No source/ROM/SPFT provenance is repeated where unchanged. The recovered evidence explicitly supersedes the lost SSH stream; no platform closure or electrical waiver follows from it.

| Coverage / issues | Classification and decision |
| --- | --- |
| Boot/recovery/security #16/#28/#32 | NARROW PHYSICAL PASS: fresh owner Power Menu reboot restores pinned USB SSH, exact old image identity, taint 0 and clean root/data/SD counters. New package has the exact Physical 01 pair as fallback. IMAGE VALIDATED; new boot/recovery remains PHYSICAL PENDING. |
| eMMC/SD/filesystems #28/#33 | NARROW PHYSICAL PASS: 8/4-bit 13 MHz, repeated checked data and durable workloads. IMPLEMENTED/HOST TESTED: source-backed 25 MHz initial SDR cap, 13/25/50 MHz bounded controls, crystal fallback, failed-clock restoration and fatal pre-I/O rejection. Faster modes/card lifecycle need actual-unit measurements; preserve protected regions. |
| Library/application #32/#33 | NARROW PHYSICAL PASS: matched 1k/10k/20k counts/integrity and query gains, with measured index write/scan costs. No new library optimization. Candidate app/1k ARM scan checks pass; interactive envelope and endurance open. |
| USB device/host #27/#32 | IMPLEMENTED/HOST TESTED: Inventra DMA and fault teardown, first-overflow snapshot, PIO boot/allocation fallback. Existing PIO throughput measured; devices pm_test exposed overflow. DMA speed/PM/reconnect remain PHYSICAL PENDING. NCM compatibility research does not qualify a gadget. VBUS topology/current limit unknown: powered host BLOCKED. |
| CPU/core/timer/idle #28/#34 | NARROW PHYSICAL PASS: existing OPPs, manual 1–4 core cycles, CPU3/2/1 processor-stage return, isolated GPT6/PPI29 counter/IRQ diagnostic. Integrated local timer/highres/NO_HZ HOST BUILT, physical continuity/hotplug pending. Higher stock OPPs await regulator transition contract; deeper SPM states remain PLANNED. |
| GPU/display/input/memory #28/#34 | NARROW PHYSICAL PASS: responsive menu/input, 500.5 MHz GPU and screen-off runtime suspend. Memory/layout/DMA compile and release checks pass without reservation changes. Load, pressure, PM and endurance pending. |
| Charging/battery/low battery #30/#34 | PARTIAL: configured SDP charging and voltage observed; meter unavailable. Measured current/energy, pack calibration, SOC, thresholds/reserve remain EVIDENCE GATED. No unsupported current or percentage introduced. |
| Suspend/RTC/time #30/#34 | PARTIAL/FAILED RESTORE: freezer/devices/platform/processors return, but USB overflow and radio timeout invalidate full resume. Helper now propagates restore failure; no root-cause fix claim. RTC UTC write/read/ticking pass after synchronized network time; prior automatic writes were gated. Reboot/full-power retention, alarm and core/SPM wake remain PHYSICAL PENDING. |
| Audio/DAC #29 | NARROW PHYSICAL PASS: S16 44.1/48 direct and switching; fixed temporary Reborn SBC playback owner-confirmed. Paired root includes tested sink contract repair. Long native-48 qualification, true DL1 24-bit/high rates and DAC topology/features remain PLANNED/EVIDENCE GATED. |
| Wi-Fi/BT/codecs #31 | NARROW PHYSICAL PASS: checked DNS/TCP/NTP, current bond/SBC and owner Reborn play/pause. Transient supplicant observer timeout remains (receipt 50 DEGRADED despite passing DNS). Pair/reconnect/endurance/coexistence and compiled/negotiated optional codecs remain PHYSICAL PENDING. |
| OTA/firmware/endurance #31/#32/#33 | IMPLEMENTED, PHYSICAL PENDING: root signed-update/rollback path; no automatic BOOTIMG changes. Exact owner firmware inventory unchanged, redistribution unestablished. Broken-app experiment still requires controlled owner approval. No full endurance or final ceiling freeze. |
| Packaging/validation #28/#32/#33 | IMAGE VALIDATED: 170 passing locked tests plus three native-dependency skips covered on host; 180 Reborn tests; eight ARM app checks, installed modules/SQLite/null-ALSA/1k scan and three ARM SFTP cases. D08/BOOTIMG/root/modules/DT/layout/fallback/protected-storage checks pass. Source/license/inventory records retained; byte-identical userspace reproduction not claimed. |

Decision: READY for one owner-performed preserving Hardware 02 flash once the packaged checksum inventory is checked. [Concrete artifact and hashes](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-HARDWARE-02.md) define the scope. User data remains in place and the exact old pair is available for recovery. Post-install identity/regression precedes clock/performance promotion. Suspend runs one persistent stage at a time with explicit radio, storage, display and host recovery checks. Ordinary failures are retained and diagnosed; actual corruption, unsafe electrical/thermal behavior or recovery loss stops the affected experiment. Final platform acceptance remains PARTIAL.

## Hardware Batch 2 build admission — 2026-09-26

The owner continues the entire capability-ceiling campaign. Fresh private receipts `17`, `26`–`45`, owner listening/control replies, current source diff and a fresh GitHub inventory refresh every coverage area below. Installed Physical 01 remains Linux `198fa7c` / Reborn `feb530f`; host base is `cc73853`. The temporary app and timer modules were removed. Normal reboot `39`–`41` returned the original binaries, taint 0, eight/four-bit 13 MHz buses, clean ext4 counters and checked DNS on boot `b3d92d70-521e-41d7-bca7-69b4badf00c1`. The initial lost SSH stream was interpreted as a devices-stage nonreturn. Receipt 49 corrects that interpretation: persistent freezer/devices/platform/ processors end records all exist on the same boot, taint 0; CPU3/2/1 power-off and restart succeed. USB's interrupt-burst guard terminates access after devices (-75), and WMT/radio restore times out (-110) after processors. The old helper masks restore failure. There is no core/SPM-entry receipt. Owner Power Menu reboot with fresh splash restores pinned USB SSH on `fffb5ac5`, unchanged Physical 01, taint 0, pm_test none, four CPUs, clean root/data/SD counters and quick health OK. First attempted restart was not proven by boot identity. This update retains the same batch boundary, adds diagnostic failure context and corrects helper failure reporting; no speculative hardware fix is admitted.

| Coverage / issues | Evidence and current decision |
| --- | --- |
| Boot/recovery/security #16/#28/#32 | Regression and normal reboot passed before devices-stage failure. Preserve the installed fallback and pinned SSH identity. Recovery is verified by receipt 49. Further suspend needs one persisted stage at a time, explicit subsystem/host recovery checks and failure diagnosis; host build/validation continues. |
| eMMC/SD/filesystems #28/#33 | Widths and guarded read/write/fsync/metadata pass with zero errors. Exact LK selects MSDC source 1; stock host source is 200 MHz and inherited MSDCPLL is ~400 MHz. Source admits only SDR high speed at 3.3 V, default 25 MHz cap, deliberate 13/25/50 MHz host-owned steps and legacy/crystal boot fallback. Faster modes remain unmeasured; normal card-capability fallback is retained, automatic CRC downshift is not claimed. |
| Library/application #32/#33 | Isolated matched old/new binaries at 1k/10k/20k pass counts/integrity. Wider bus reduces large commit tails; queries reduce 20k page p50 93.435→2.080 ms on the same bus. New indexes increase population/scan cost. No additional library optimization or final envelope claim. |
| USB device/host #27/#32 | Three TCP repeats and separated verified 16 MiB SFTP runs recorded. Exact stock integrated DMA/IRQ layout supports implementation using upstream Inventra and 32-bit DMA addressing. Allocation/boot PIO fallback, error teardown and counters are required; no physical DMA result yet. Connector/VBUS switch/current limit remain unknown: powered host/UAC BLOCKED. |
| CPU/core/timer/idle #28/#34 | Exact unit selects stock table 0, but 1196/1300 MHz require 1.20/1.25 V and an established regulator/SPM transition contract. Existing OPPs stay. Manual 1–4-core cycles pass. GPT6 counter measured 12,999,956–13,000,027 Hz and all 12 PPI29 one-shots delivered; probe restores controls. Integrate GPT6 through its existing owner, guard ARM timer registration, retain GPT fallback. Effective NO_HZ, long counter continuity, hotplug and idle residency remain post-install gates; no deeper SPM state added. |
| GPU/display/input/RAM #28/#34 | Menu/input and 500.5 MHz GPU baseline remain; screen-off runtime suspend observed. No GPU clock change or memory-reservation reclamation. New DMA/timer integration requires broader memory/layout/build checks and physical load/PM regression. |
| Charging/battery/low battery #30/#34 | Existing SDP 450 mA configuration and voltage/CV cycling observed. No external meter; input/pack current, pack temperature, positive energy balance, SOC and shutdown reserve remain unqualified. No charger-limit, fabricated percentage or low-battery enablement. |
| Suspend/RTC/time #30/#34 | NTP and freezer pass; recovered devices/platform/processors return, including CPU3/2/1 restart. USB overflow and radio timeout prevent full restore. Core/deep tests have no receipt. Propagate restore errors and capture first USB-overflow status before another one-stage test. Power/RTC same-boot wake and retention remain open. |
| Audio/CS43131 #29 | Direct S16 44.1/48 and switching owner-confirmed clean. A real native ALSA metadata omission rejected valid Reborn sinks; regression reproduces it, seven tests pass after repair. Temporary fixed ARM app played clean SBC >3 minutes. Product native-48 endurance, true DL1 24-bit packing/high rates and DAC load/IRQ features remain distinct gates. |
| Wi-Fi/Bluetooth/codecs #31 | Checked DNS/NTP/TCP and boot reconnect pass; owner confirms Reborn AirPods audio and play/pause after the sink fix. The retained trace captured no incoming AVRCP command, so owner and trace evidence are distinguished. Fresh pairing, reconnect/endurance/coexistence and actual optional encoders remain open; SBC fallback retained. |
| Firmware/OTA/endurance #31/#32/#33 | Existing owner provision/calibration and recovery provenance remain unchanged. No missing result is inferred from historical closed #30. Signed root install/readback/health/rollback and controlled broken-app approval remain pending; no automatic BOOTIMG update or platform freeze. |

Decision: READY for one coherent Hardware Batch 2 host build and validation of storage SDR steps, USB DMA, local timer/NO_HZ and the measured Reborn sink repair, USB failure observation and truthful suspend-helper status. Recovery is now verified; physical admission remains PARTIAL until a concrete validated artifact and its safe fallback are available; owner performs one manual flash. The new paths are candidates, not qualified ceilings. Broader release checks apply because timer and DMA ownership change. Preserve unrelated worktree edits. No guessed fix for the suspend failure is admitted by this review.

## GPT6/local-timer diagnostic boundary — 2026-09-26

The complete baseline/coverage audit immediately below remains current for all unchanged subsystems. Fresh receipts `17`, `26`–`32` add matched library tests, same-boot recovery/clean filesystems, a localized Reborn playback fix and actual CPU/timer reads. The read-only observer deliberately failed init and left no module; this boot now has documented O taint (4096). Normal reboot and zero-taint verification are required; no new kernel fault is inferred from O alone.

| Coverage / issues | Refreshed decision |
| --- | --- |
| CPU #28/#34 | Retained ATAG devinfo3 low2=2, devinfo15 bits30:28=0 select exact stock table 0: 1300 MHz/1.25 V, 1196 MHz/1.20 V, existing three at 1.15 V. Voltage/regulator/SPM transition contract remains required; no OPP activation. |
| Timer/idle/suspend #34 | CNTFRQ=0 and physical counter delta=0 on all cores in three 53–60 ms observations. Stock starts GPT6 as the CP15 system counter; installed upstream driver starts GPT1/2 only. A bare architectural-timer DT/Kconfig enable would be incorrect. |
| Application/audio/radio #29/#31 | ALSA constructor omitted the returned PCM name, causing valid playback rejection. Regression reproduces it; seven audio tests pass after metadata repair with contract checks retained. Temporary RAM-mounted ARM app plays SBC over three minutes with zero XRUN/recovery/decode/playback errors. No incoming AVRCP command in this trace; control acceptance stays open. Original app/session restoration recorded separately. |
| Storage/application #32/#33 | All matched 1k/10k/20k integrity/count checks pass. Wider-bus commit gains and query gains separate; new indexes have measurable write/scan cost. No errors or clock increases. |
| USB/host, GPU/display/input, RAM #27/#28/#32/#34 | Prior partial results retained. No DMA/role/VBUS/PLL or reservation changes. Powered host remains blocked by missing electrical evidence. |
| Power/battery, RTC, firmware/security, OTA/recovery/endurance #30–#34 | Prior gates retained, including no external meter, no current/SOC inference, staged suspend, physical OTA rollback and long runs. No missing physical result is inferred from diagnostics. |

Exact stock `mt_gpt_init` at `c001d83c`, extract SHA-256 `bac9c513d975dbda913dc76b7aae60f077f043bc50a12784412615e42a3f9809`, starts GPT6 free-running. Pinned MT6582 BSP `mt_gpt.c` confirms GPT6/13 MHz/DIV1. Decision: READY for `tools/development/y2-local-timer-probe.c`, a bounded test on this exact kernel. It refuses an existing PPI29 mapping, enabled CNTP, or non-idle GPT6/its interrupt. It starts only source-backed GPT6, checks three counter-rate samples per CPU against 13 MHz, then requests PPI29 and tests three one-shot deliveries per core. GPT1/2 remain Linux timekeepers. Waits are bounded; the handler immediately masks/stops CNTP. Original timer compare/control and GPT6 control/clock are restored, IRQ resources freed, and init deliberately fails. The previously unused counter advances; it is not reset or made a Linux clocksource. No voltage, PLL, storage, VBUS, PMIC or power-state register changes. This is diagnostic evidence, not NO_HZ/suspend/deep-idle acceptance. Failure stops the affected experiment while independent work continues. Hardware Batch 2 remains PARTIALLY READY pending these results, integration and fallback tests.

## Physical 01 baseline and ceiling diagnostics boundary — 2026-09-26

Refresh from the same exact Physical 01 identity/boot as the entry below, private receipts `00`–`16`, owner listening/card/menu replies and the unchanged open issue inventory. Linux worktree still preserves pre-existing documentation edits and Reborn's unrelated asset/document changes. The initial regression gate passes; Physical 01 is the working baseline. No final platform or subsystem ceiling is declared. [Current report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-HARDWARE-CEILING.md).

| Coverage / issue | Refreshed decision |
| --- | --- |
| Boot/recovery/protected storage #16/#28/#32/#33 | READY for bounded diagnostics: exact installed metadata, same boot, pinned USB SSH, taint 0 and all three ext4 error counters 0. No partition/protected-area or recovery-policy change. Reboot/rescue/OTA cycles still pending. |
| eMMC/SD/filesystems #28/#33 | Width regression passes: IOS 8/4 at 13 MHz legacy, verified direct/random I/O, three SD passes, full guarded fsync/metadata/readback. Clean replacement card confirmed. Old suspect FAT card remains isolated; multi-card/removal/faster-mode acceptance pending. |
| SQLite/application/storage #32/#33 | Exact 1k/10k/20k counts/quick checks pass, browse p50 ~2.08 ms; matched old/new binary comparison running serially to separate query cost and transport gains. No new library optimization before these measurements. |
| CPU/core/idle/clocks/RAM #28/#34 | Manual 4→3→2→1→2→3→4 hotplug and checked hash load succeed; same boot, SPM broken=0, final four online. Current OPPs/reservations unchanged. Local clockevents remain dummy; no tickless/deeper-idle acceptance. |
| Display/GPU/input #28/#34 | Owner menu visible, Mali400 active and 500.5 MHz source retained; screen-off runtime suspended. Full UI/PM/thermal endurance pending. |
| Charging/battery/low battery #30 | Configured 450 mA under 500 mA SDP allocation; voltage and die temperatures observed, no current/SOC/pack-temperature inference. Owner has no external meter. Pack evidence/charge balance and shutdown reserve remain gates. |
| Suspend/RTC/time #30/#34 | NTP now synchronizes through ordinary checked Wi-Fi. Correct core masks pass manual hotplug; pm_test, SPM entry, same-boot Power/RTC wake, restoration and retention remain unqualified. |
| Wired/precision/CS43131 #29 | Owner confirms clean S16 44.1/48 one-minute tests and switches, no reported XRUN. Longer Reborn/native-48 profile, true DL1 packing, high rates and codec IRQ/load features remain distinct gates. |
| Wi-Fi/Bluetooth/codecs #31 | WPA2/DHCP/DNS/NTP and 45–47 Mb/s TCP work. Bonded/trusted SBC PCM produces clean owner-confirmed tones. Fixture AVRCP fails; trace Reborn's addressed player next. Fresh pair/reconnect/coexistence/codecs still pending. |
| USB device/host #27/#32 | ECM/PIO TCP ~40 Mb/s receive/~47 transmit; reproducible upload retransmissions open. DMA source review proceeds; no DMA, role or VBUS activation yet. Unknown VBUS switch/current limit continues to block powered host operation. |
| Firmware/security/updates/endurance #31/#32/#33 | Existing owner calibration/provisioning, SSH identity and fallback retained. No repeated unchanged provenance acquisition, no keys/bonds in public evidence. Signed root apply/rollback, broken-app approval and long runs remain open. |

Next diagnostic admission: a short GPL module built against this exact installed kernel may read the architectural physical counter/control/frequency on each core and only the five relevant CPU-bin bits from the already reserved LK ATAG page. Userspace timer access traps; this is why a privileged observation is needed. It writes no timer, clock, power, MMIO or loader state, and deliberately returns `-EAGAIN` so it leaves no resident module. As in the earlier GPU-bin inspection, external-module loading sets taint O (4096); preserve the clean baseline receipt, label that diagnostic boot explicitly and verify a fresh normal boot afterwards. This is not timer interrupt/wake acceptance, a voltage increase or permission to guess efuse addresses. A timer interrupt experiment requires its own bounded restore/cleanup review after these reads.

Decision: READY for the bounded observation and existing supported-state qualification; PARTIALLY READY for Hardware Batch 2. Final batch admission still requires exact clock/timing/DMA/timer contracts, conservative fallback and targeted failure tests. No production image build or flash is implied by this diagnostic boundary.

## Hardware capability ceiling entry — 2026-09-26

The owner authorizes a platform-wide evidence-backed ceiling campaign, broad investigation before rebuilding, coherent hardware batches and physical tests. This supersedes incremental feature admission and the earlier headphone deferral. It does not authorize guessed overclock/overvoltage, unknown VBUS activation, reserved-memory reclamation or fabricated audio/SOC capability. Owner performs manual flashes; deliberately broken app OTA retains explicit owner approval.

Fresh pinned USB SSH at 18:42 UTC identifies installed Physical 01 exactly: Linux `198fa7cfd54a93826b54e3c0c4fab4d32e84acec`, Reborn `feb530fae2cdf785c764d619e8df22798c8e524c`, candidate.3, kernel `6.18.0-y2linux-platform-v1-physical-01`, boot `4991ba2c-0571-4649-9f7c-9e0318abb952`. Complete versions JSON matches the candidate metadata; no whole installed-image readback is claimed. Local heads are Linux `cc73853` and Reborn `feb530f`; existing unrelated worktree edits stay intact. Private receipts: `out/platform-v1-hardware-ceiling/20260926T184237Z-physical01/`. Read-only GitHub inventory confirms #16/#27–#29/#31–#34 OPEN, historical #30 CLOSED. That historical state is not physical power acceptance.

| Coverage / issue owner | Fresh evidence and next boundary |
| --- | --- |
| Boot/rescue/protected storage #16/#28/#32/#33 | PARTIAL: exact candidate boots, authenticated USB SSH works, fsck stages complete and root/data mount rw. Existing fallback retained; current rescue/reboot/rollback cycles pending. No protected-area or geometry changes. |
| Kernel/RAM/DMA #28/#34 | PARTIAL: taint 0, ~930 MiB usable RAM, HIGHMEM retained, Reborn PSS now readable (21359 KiB at this observation). No panic/Oops or transfer-corruption signature. Pressure/endurance pending; reservations unchanged. |
| eMMC #28/#33 | PARTIAL: actual IOS eight bits, 13 MHz, legacy, 3.3 V; root/data ext4 error counters 0. Repeat exact guarded direct-I/O, metadata and library workloads before any higher-clock experiment. EXT_CSD/controller/stock-clock evidence must support subsequent steps. |
| SD #33 | PARTIAL: present SD128 card, four bits/13 MHz/legacy, mounted ext4 with error counter 0. This differs from the isolated bad FAT card; owner confirmation/clean-card provenance and lifecycle still pending. No card repair/reformat. |
| Library/SQLite #32/#33 | PARTIAL: compiled index/scanner fixes installed; exact 1k/10k/20k rerun pending. Isolate bus and query effects where matched evidence permits; no further speculative optimization. |
| CPU/core/idle/clocks #28/#30/#34 | PARTIAL: four cores online, 598/747.5/1040 MHz available, dummy local clockevents and broadcast IPIs persist. Stock timer/OPP/binning/voltage review precedes activation; no unsupported voltage increase. |
| Display/GPU/input #28/#34 | PARTIAL: current Reborn first-frame record and GPU/display queries pass. Physical menu/input confirmation, source-backed GPU ceiling and workload/runtime-PM measurements pending. |
| Charging/battery/thermal #30 | PARTIAL: SDP allocation 500 mA, configured charge current 450 mA, ~4.08–4.10 V, currently Not charging; CPU/PMIC 47.1/46.883°C at entry. External meter requested; no measured pack current, SOC, pack temperature or low-battery reserve. Diagnose before changing limits. |
| Suspend/RTC/time #30/#34 | PARTIAL: RTC query works; current per-CPU clockevent gap and historical CPU3 shutdown/resume issue retained. Controlled pm_test, same-boot resume and Power/RTC wake required; no guessed SPM sequence. |
| Wired/precision audio #29 | PARTIAL: ALSA query succeeds; closed PCM and truthful unavailable jack telemetry. Owner listening and longer 44.1/48 regression pending; DL1 packing/clock evidence required before S32/preserved-24/high rates. |
| Wi-Fi #31 | PARTIAL: address/default route present but current status says supplicant_unavailable. Diagnose current control interface and test ordinary checked DNS/TCP before acceptance of PHY-001. No checksum-bypass diagnostic as acceptance. |
| Bluetooth/codecs/coexistence #31 | PARTIAL: controller powered, peer not bonded/connected, SBC only. Physical stable SBC precedes expanded codecs and Auto policy. Owner peer availability requested. |
| USB device/host #27/#32 | PARTIAL: high-speed peripheral SSH works. Separate RAM/storage TCP/SFTP measurements and source-backed DMA review next. Host role/VBUS remains BLOCKED_BY_EVIDENCE until switch/current-limit/wiring proof. |
| Firmware/calibration/security #31/#32 | Existing private provisioning and SSH identity retained; no renewed acquisition or secret publication. No provenance repetition absent a relevant change. |
| OTA/maintenance/endurance #32/#33 | PARTIAL: candidate installed by owner, retained data and recovery package; no physical signed-root apply/ack/rollback acceptance or long-run freeze. Storage/power/core prerequisite gates remain. |

Decision: READY for regression measurements and broad source investigation; PARTIALLY READY for Hardware Batch 2 selection. Physical 01 is not yet promoted as a complete baseline. Ordinary subsystem failures do not stop independent work. Corruption, dangerous electrical/thermal behavior and lost recovery stop the affected experiment; unstable storage prohibits clock escalation. Group supported storage/USB/timer/telemetry changes only after evidence review, then build and validate one coherent candidate with fallback before owner flashing.

## Physical Fix Batch 1 packaging boundary — 2026-09-26

Real-device receipts 49–56 refresh the admission audit below. The installed Telemetry 01 boot remains `09de0586-278c-4d37-a68f-17ac9952740c`; taint and both internal ext4 error counters remain zero. CPU/PMIC readings at the last check are 55.4/52.731°C, battery 4.028 V and Charging, ALSA closed. USB SSH remains usable. Full health still correctly reports Wi-Fi DNS degradation; controller presence is not SBC acceptance. Owner postponed further AirPods actions and the pairable window is closed. This admits packaging, not physical acceptance.````

| Coverage | Boundary disposition |
| --- | --- |
| Boot/recovery, firmware, protected storage | Exact current root-overlay fallback verified against its original BOOTIMG; new kernel/rescue/DT/BOOTIMG checks pass. No device installation, partition geometry or protected-area operation. Fresh physical boot/recovery remains mandatory. |
| eMMC/SD/filesystems | Width-only 8/4-bit implementation retains 13 MHz/3.3 V/legacy; baseline direct-I/O hashes and internal error checks pass. SD remains removed/unrepaired; clean-card lifecycle and serial-less identity remain separate gates. |
| SQLite/library | Real 1k/10k/20k baseline and exact-query A/B justify indexes; full current application tests pass. New candidate scan/WAL/durable-write retest pending. Actual settings/database export passes archive hashes and SQLite integrity; no reset performed. |
| CPU/idle/RAM/DMA | Nine bounded decoder suites pass across all three existing OPP caps, with residency proving the caps; original schedutil/max restored. No topology, voltage, DMA, reservation or timer/SPM change. PSS/advice facilities are compiled; sustained app workloads and growth remain unqualified. |
| Display/GPU/input/wired/high-resolution audio | Menu/normal warmth and short stereo 44.1/48 listening evidence retained. No new listening claim. 24/96 decoding passes; preserved-24 output/clock/IRQ evidence remains missing. |
| Charging/battery/thermal | Rising observed voltage supports charging observation only; no measured current, pack temperature, SOC or shutdown reserve. No limits/trips/threshold changes. Meter and supervised load/curve work pending. |
| Suspend/RTC/time/watchdog | No suspend or watchdog experiment. RTC tick evidence retained, network time blocked by DNS. Same-boot Power/RTC wake and power-cycle retention require controlled physical sessions. |
| Wi-Fi/Bluetooth/codecs | Checksum, bonding/connect/error/UI fixes compiled; early/root signed regulatory bytes aligned. Neither Online nor SBC/AVRCP/reconnect/coexistence is accepted before physical regression. Optional codecs remain off. |
| USB device/host | Existing bidirectional SFTP hash/throughput evidence retained; cable/PC cycles pending. No role or VBUS activation; connector/switch/current evidence still required. |
| Updates/maintenance/endurance | Export measured; destructive reset, root OTA apply/rollback, repeated reboot, SD cycles and long power/endurance remain gated. No automatic BOOTIMG update. |
| Source/release | Final build pair: Linux 198fa7c, Reborn feb530f; 179 host application tests and native fallback fixture pass. ARM/QEMU/production/package/license receipts must accompany the candidate, with environment exclusions stated explicitly. Existing unrelated documentation/assets remain preserved. |

Decision: package the coherent batch with exact fallback and source identities; request owner installation only after final checks and hashes exist. Do not close Platform v1, change issue acceptance or carry old physical passes onto new code.

## Physical Fix Batch 1 admission — 2026-09-26

Batch refinement from receipts 49–52: include the Bluetooth UI's false Connected→Paired inference in the existing radio repair. Owner deferred the next headphone session; Pairable was explicitly closed. The fallback packaging path must bind the physically running Telemetry 01 root-overlay receipt to its unchanged original BOOTIMG, while retaining the full release's geometry and data contract. Exact image/version/filesystem checks and rejection tests now cover this extension. These are within the admitted batch, with no additional hardware activation or milestone closure; artifact and physical gates remain.

Owner authority is the complete physical bring-up request, including coherent kernel/platform/application fixes and later manual installation. Repository heads remain Linux `e88d044` and Reborn `9125788`; installed Telemetry 01 identity and boot are unchanged from the entry audit. Private receipts `00`–`45` and the [physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-PHYSICAL-BRINGUP.md) supply this review. Existing unrelated dirty documentation/assets remain preserved. No milestone or issue closure is warranted; the existing #16/#27–#29/#31–#34 owners remain.

| Coverage | Refreshed hardware evidence / remaining boundary |
| --- | --- |
| Boot/recovery, firmware, protected storage (#16/#28/#31/#33) | PARTIAL: same boot and pinned SSH throughout; internal ext4 errors 0/0 and taint 0. Existing paired fallback must accompany the candidate. No loader, calibration, NVRAM, protected-area or partition-layout change. |
| eMMC/buses (#28/#33) | PARTIAL: verified O_DIRECT throughput 1.25–1.60 MB/s at one-bit 13 MHz. Exact retained stock Y2 platform data proves MSDC0 eight data pins and MSDC1 four; stock and current SDC_CFG width encodings agree. Admit width-only 8/4-bit software change at the existing 13 MHz/3.3 V/legacy timing. Standard MMC EXT_CSD read comparison/fallback remains mandatory; no clock/voltage/DDR expansion. Physical acceptance is pending. |
| SD/filesystems (#33) | PARTIAL: real FAT32 card has zero serial, no blkid UUID, dirty flag and inconsistent label metadata. Global stop was honored; owner removed the unmounted card, internal checks then allowed resumption. Card remains gated. Stable serial-less identity and clean-card lifecycle are subsequent implementation/physical work, not a pass. |
| SQLite/library (#32/#33) | PARTIAL: actual ARM 1k/10k/20k scans, queries, WAL/checkpoint/reopen and RSS measured; quick_check passes. Exact 20k query/index A/B reproduces sorting cost and substantial improvement with unchanged results. Admit measured indexing/predicate changes; preserve schema compatibility and measure write cost. |
| RAM/DMA/SMP/telemetry (#16/#28/#34) | PARTIAL: no observed OOM/corruption; PSS unavailable from missing PROC_PAGE_MONITOR. Admit this observation facility and ADVISE_SYSCALLS, required by the failed real benchmark. Reservations, DMA ownership and CPU topology remain unchanged. |
| CPU/idle/display/GPU/input (#28/#34) | PARTIAL: four cores, three OPPs, screen-off GPU suspend and WFI residency measured. Stock local timer PPI29 is a lead, not proof of current firmware routing/rate. Deeper idle and local-timer activation remain BLOCKED_BY_EVIDENCE; no invented clockevent/SPM sequence. |
| Charging/battery/thermal (#30) | PARTIAL: observed charging voltage gain and normal owner-reported warmth; die temperatures roughly 50–57°C in measured workloads. No pack-current/temperature/SOC calibration or controlled charge/discharge curve. Existing limits and disabled shutdown thresholds remain; meter/pack evidence and supervised physical tests required. |
| Suspend/RTC/time (#30/#34) | PARTIAL: RTC reads/ticks but is dated 2022; system time uses the release floor. NTP blocked by Wi-Fi DNS. Prior CPU3 ACK failure/correction still requires controlled same-boot resume, power-key and later RTC wake. No suspend activation in this batch. |
| Wired/high-resolution audio (#29) | PARTIAL: owner hears six clean alternating S16/44.1/48-kHz stereo tones, correct hw_params and no XRUN. Jack telemetry lacks codec IRQ and is not physically truthful. Long playback, IRQ routing, preserved-24 and high-rate clock evidence remain gates. |
| Wi-Fi/Bluetooth/codecs (#31) | PARTIAL: WPA2/DHCP/route/ping pass; DNS succeeds only in a diagnostic that bypasses the falsely advertised TX checksum offload. Admit software-checksum fix. AirPods ACL appears, but no bond/PCM; trace and exact kernel code expose non-bondable authentication, and Reborn omits Connect after Pair. Admit bounded pairable lifecycle, verified bond and explicit connect sequencing. Sole automatic reconnect owner remains y2-bt-reconnect. SBC/AVRCP/coexistence and all optional codecs remain physical gates. |
| USB device/host (#27/#32) | PARTIAL: 129 SFTP files pass both-direction hashes; durable 64-MiB upload 1.327 MB/s, warm-cache download 5.727 MB/s. Cable/PC cycles pending. Host role/VBUS remains BLOCKED_BY_EVIDENCE. |
| Userspace/shutdown/OTA/reset/endurance (#32/#33) | PARTIAL: short independent workloads are measured. No real root-update/rollback, full reset, shutdown reserve or endurance acceptance. Safe package/backup checks precede separately approved destructive/update/power sessions. |

Decision: READY for coherent source implementation and host/ARM validation; PARTIALLY READY for candidate qualification after fresh packaging audit and owner installation. First batch addresses measured transport, observation and application faults together. It does not require completion of gated SD, battery, suspend, USB-host or precision-audio work before repairing the usable baseline. No generic stock platform or speculative register value substitutes for Y2 evidence. Recovery and broad physical regression remain candidate exit gates.

## Complete physical bring-up campaign entry — 2026-09-26

The owner explicitly authorizes a broad physical census, source diagnosis and coherent software/kernel fixes, candidate builds and repeated qualification. This supersedes the September 25 passive/fail-fast scope: ordinary warnings and individual subsystem failures are recorded while independent work continues. Global stops are unsafe kernel panic/Oops, filesystem corruption, protected partition access, uncontrolled repeated reboot, dangerous charger/battery/heat, lost recovery, or destructive writes outside dedicated test areas. Manual flashes, OTA apply/rollback experiments, card swaps/surprise removal, full-user reset and long unattended power/suspend work retain the owner's explicit action gates.

Entry repository heads: Linux `e88d0444d7365ffc539f013bdb4f3177160bf8e9`, Reborn `912578848f3094dd276d8cdb6e030c8ae10f71a9`. Existing Linux documentation edits and Reborn asset deletions/untracked review/assets are preserved. Git identity, authenticated account and remote issue status are unchanged. Read-only tracker inventory still reports #16/#27/#28/#29/#31/#32/#33/#34 OPEN, historical #30 CLOSED.

Fresh authenticated USB evidence at 14:31–14:33 UTC binds this campaign to Telemetry 01: Linux userspace `814c2f3`, kernel/base `d04b95a`, Reborn `1556083`, release `1.0.0-candidate.2`, rootfs `2025.02.18-platform-v1.2`, API 1, boot `09de0586-278c-4d37-a68f-17ac9952740c`. Complete versions metadata matches `out/y2linux-platform-v1-telemetry-01-candidate/`, not the older original package named in the brief. Both comparisons are retained; the current installed candidate is the expressly requested target. Whole installed images were not read back. Strict existing SSH pin/login key remain in use.

Re-read retained Storage06, GPU-01, CONNECTIVITY-10 and USB reconnect receipts, the September 23 review/capability/owner ledgers and September 25 physical results. Refresh the full coverage matrix before admitting workloads:

| Coverage / owner | Evidence at entry and remaining boundary |
| --- | --- |
| Boot/rescue #16/#28/#32 | PARTIAL: current normal boot, first-frame record and USB shell; prior manual recovery evidence. Current rescue rehearsal/repeated boots pending. |
| Kernel/diagnostics #16/#28 | PARTIAL: taint 0, no retained panic/Oops/WARN-stack or ext4 I/O corruption signature; ordinary warnings need classification, not global stop. |
| RAM/DMA/SMP #28/#34 | PARTIAL: prior four-core/short allocator evidence; current pressure/PSS/growth and timer behavior to measure. Reservations unchanged. |
| Clocks/buses/reset #28 | PARTIAL: current probes; constrained MSDC and dummy local timers need source/hardware correlation. No speculative timing or SPM changes. |
| Display/GPU/input #28/#34 | PARTIAL: earlier Lima/input/runtime-PM pass, current first-frame process; owner view/input and workload/resume regression pending. |
| Internal storage #28/#33 | PARTIAL: separate rw root/data, ext4 errors 0/0. Safe scratch measurements and bus evidence next. |
| Removable SD #33 | PARTIAL: controller implementation; current health not mounted. Card identity/lifecycle/filesystem performance pending. |
| SQLite/library #32/#33 | PARTIAL: host/ARM software contracts; 1k/10k/20k target measurement next. |
| Power/charging/SOC #30 | PARTIAL: current Charging, 3.854 V, configured 450 mA on SDP; retained voltage gain is not measured pack current. Pack/thermal/SOC evidence missing. |
| CPU/idle/thermal #28/#30 | PARTIAL: WFI/three OPP implementation; fresh CPU/PMIC 54.4/50.391°C snapshot, no operating-envelope claim. Deeper idle BLOCKED_BY_EVIDENCE. |
| Suspend/wake/RTC #30/#34 | PARTIAL: prior GPU-01 failed same-boot resume, later mask fix unqualified; staged supervised tests follow recovery prerequisites. Clock currently wrong. |
| Wired audio #29 | PARTIAL: old S16/44.1 pass; current native query works. S16/48 physical gate; S32/preserved-24/high rates BLOCKED_BY_EVIDENCE. |
| Wi-Fi #31 | PARTIAL: previous WPA/IP/routing pass; fresh dns_unavailable. Diagnose all layers alongside unrelated tests. |
| Bluetooth/codecs #31 | PARTIAL: adapter/software available, currently off. Pair/SBC/AVRCP/coexistence physical gates; optional codecs follow stable SBC individually. |
| Firmware/calibration #31 | Existing private provisioning retained; no reacquisition, protected reads or exported secrets. |
| USB device/host #27/#32 | PARTIAL: current pinned SSH works; SFTP/throughput/reconnect pending. Host role/VBUS BLOCKED_BY_EVIDENCE. |
| Time/entropy/telemetry #28/#32 | PARTIAL: status/full-health now return; device wall time inaccurate. Collection cost, DNS/NTP and truthful capability version need review. |
| Userspace/shutdown/update/reset #32/#33 | PARTIAL: implemented contracts; no OTA apply/full reset. Backup, scratch-only maintenance, normal shutdown and rescue precede explicit update approval. |
| Release/endurance #32/#33 | PARTIAL: exact installed software identity; no integrated physical/endurance acceptance. Build coherent measured fixes, preserve existing recovery artifacts. |

Decision: READY for the broad bounded census and dedicated scratch benchmarks; PARTIALLY READY for physical actions as prerequisites and owner responses arrive. No hardware gate is promoted and no new electrical limit is authorized. Raw private evidence: `out/platform-v1-physical-bringup/20260926T143142Z-census/`. The [campaign report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-PHYSICAL-BRINGUP.md) and [master issues](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-PHYSICAL-ISSUES.md) own ongoing results. Re-audit before candidate packaging, new hardware implementation and closure.

## Owner-requested Wi-Fi connection check — 2026-09-25

Result, same Telemetry 01 boot `3194fa9d-2dee-4105-86f0-4021580bf8d0`: direct supplicant COMPLETED/WPA2-PSK, matching DHCP address and wlan0 default route, 5/5 router ping replies (1.532 ms mean) and 3/3 Internet-IP replies (11.846 ms mean). Both configured-resolver lookups, pool.ntp.org and example.com, fail with EAI_AGAIN; the platform's DNS probe also fails. The native control query succeeds while the observer intermittently reports supplicant_unavailable. Refine Wi-Fi coverage to PARTIAL with actual association/DHCP/routing/IP evidence; DNS FAIL, full Online/Session C acceptance absent, no throughput/reconnect/endurance claim. Source/image, hardware policy and all other physical gates stay unchanged. Private evidence: `20260925T154016Z-owner-wifi-check`. Next narrow blocker is DNS-path and status-query diagnosis, not an assumed need to reflash.

The owner now reports connecting to their router and explicitly requests a narrow Wi-Fi check. Verify unchanged Telemetry 01 identity, association, address, default route and DNS, with bounded router reachability if the platform admits it. This does not restart the full Session C plan or waive Session A's retained kernel-warning gate. No network credentials, service/radio configuration, throughput/reconnect workload, source or hardware policy is changed. Existing physical coverage remains as recorded until fresh observations support a limited update; retain before/after baseline and private command receipts.

## Telemetry 01 physical baseline stop — 2026-09-25

Subsequent read-only diagnosis, same boot, privately retained under `20260925T152936Z-readonly-triage`: supplicant answers PONG/DISCONNECTED and has zero configured networks. No authentication failure is established without a configured network. Intermittent query delay versus the observer's one-second deadline remains unresolved; two explicit deadline probes both succeeded. Timer state confirms periodic MediaTek broadcast to four dummy local devices, 10 ms resolution and no active highres/nohz mode, consistent with HZ=100 and HIGH_RES_TIMERS unset in the retained kernel config. Do not change timer or hardening scope solely to silence a warning. The next decision is a separately authorized correction pass or explicit disposition of named known limitations before short tests; the existing stop rule and session results stay in force.

Fresh USB SSH evidence, 15:20:36–15:22:44 UTC, boot `3194fa9d-2dee-4105-86f0-4021580bf8d0`: complete installed versions and all five replacement/four Reborn ELF hashes match Telemetry 01, Linux source `814c2f3` / Reborn `1556083`. Source identity is corrected; retained kernel remains d04b95a. Status now returns (2.692/3.550 s including SSH); full health returns valid JSON (3.525/3.576 s), preserving FAILED/DEGRADED Wi-Fi readiness. A passive platform collection reports null/command_timeout for wakeup_count while Charging; the final process table has no leftover reader. Both targeted repairs pass in this narrow physical observation; this is not whole-platform physical qualification.

The kernel repeats 14 warning/error-priority entries from the already reviewed classes. No new Oops/panic/WARN-stack/ext4-I/O signature; taint 0, both ext4 error counters 0. The original warning stop rule still applies: A FAIL, B–D NOT_TESTED. No reboot/rescue/workload, service/radio action, code change, flash or hardware policy modification was performed. Wi-Fi changes from not_authenticated to supplicant_unavailable; do not infer a connected network or silently restart it.

Coverage refresh: root/data identities and separate rw mounts pass narrowly; normal_boot=1 and first-frame process identity match; owner sees main menu and reports normal warmth. CPU/PMIC snapshot 48.800/45.713°C, Reborn RSS 23,532 KiB / 16 threads, PSS unavailable, cumulative frequency/WFI counters retained without workload qualification. Boot/rescue, memory/DMA/SMP, buses/clocks/reset, display/input, SD/eMMC, power/thermal/idle/suspend, audio/radios/calibration, USB, time/entropy, userspace/shutdown, update/backup and release retain all earlier PARTIAL/UNKNOWN/BLOCKED_BY_EVIDENCE/DEFERRED limits. No milestone or issue status changes; existing owners remain as recorded in the preceding audit.

The [current physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-PHYSICAL-QUALIFICATION.md) and private `20260925T151959Z-telemetry01` receipts retain both baselines, manual observation, exact commands, identities, hashes and limitations. Next smallest boundary is warning disposition and Wi-Fi readiness investigation, then resuming Session A under its explicit stop rules. No physical gate is promoted; E/F/G and unattended endurance remain separately controlled.

## Telemetry 01 physical re-entry — 2026-09-25

The owner reports installing the corrective root candidate and resumes the original supervised qualification scope. Expected source is `814c2f3` with Reborn `1556083`; running identity must match the candidate before testing. Re-read the owner plan, preceding failed physical run, repair/warning review, and candidate handoff. All coverage rows and issue ownership retain the prior physical gates until fresh evidence changes a narrow observation. Begin with the mandatory status/capabilities/full-health baseline and kernel capture; stop on mismatch or the existing fault/warning rules. No automatic exception is granted for a previously classified warning. No build, source change, flashing, hardware policy, long run, or Session E/F/G action is part of this physical re-entry. Update this audit and the report with the actual boot and results before crossing to another session.

## Platform v1 telemetry candidate handoff — 2026-09-25

Close only the owner-authorized corrective software/package pass. Source `814c2f3470566021c1a9c43037fd868de8b2df9c` fixes health dispatch and bounds the wakeup reader; 67 host and 5 packaged ARM/QEMU tests pass. The fresh preserving root in `out/y2linux-platform-v1-telemetry-01-candidate/` has SHA256 `4a8e520946ad1aaa00df46e9f302463341e4408bba063f43728b8cb8f68bb092`. Five expected files changed; whole-tree bytes/links/modes and image ownership/flags checks, clean e2fsck, root-only scatter/geometry, unchanged BOOTIMG requirement, unchanged Reborn ELFs and exact original UI fallback pass. The [repair report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-TELEMETRY-01.md) retains test limitations and source-backed warning classification. No kernel warning was suppressed.

Re-audit against the physical stop boot below and retained Storage06, GPU-01, CONNECTIVITY-10 and USB evidence. Every freeze coverage row keeps its physical classification: boot/rescue, memory/DMA/SMP, buses/clocks/reset, display/input, SD/eMMC, power/thermal/idle/suspend, audio/radios/calibration, USB, time/entropy, userspace/shutdown and update/backup/release remain PARTIAL with their existing UNKNOWN/BLOCKED_BY_EVIDENCE/DEFERRED extensions. No new device evidence was collected. The installed source remains d04b95a / Reborn 1556083, Session A FAIL, B–D NOT_TESTED; no PHYSICALLY_QUALIFIED or endurance promotion.

Existing issue ownership and status stay unchanged: #16/#27/#28/#29/#31/#32/#33/ #34 OPEN and historical #30 CLOSED, with later adverse evidence retained. No remote mutation, hardware/memory scope change, calibration acquisition or repeat of unchanged ROM provenance. Next boundary remains separately authorized installation and Session A, with the owner's warning/fault stop rules intact. Timer/cache and hardening review are open; E/F/G and unattended runs remain gated.

## Platform v1 telemetry repair entry — 2026-09-25

The owner now authorizes the proposed corrective software pass and a new candidate, with flashing still prohibited. Reuse the physical stop evidence below: CLI health dispatch crashes; the status reader blocks in pm_get_wakeup_count while charging; warnings remain explicitly unwaived. The current installed pair and every hardware coverage classification remain unchanged. No device access, hardware-policy change or new hardware subsystem is needed for this repair. The existing issue inventory and ownership remain valid.

Scope: correct CLI name resolution, bound the wakeup-counter query and report unavailable data honestly, add focused regressions exercising the real failure boundaries, review warning origins, and prepare a fresh preserving root-only candidate from the exact UI candidate. Retain the unchanged Reborn binaries, BOOTIMG requirement, Y2DATA and hardware policy. Record the corrected platform source/root identity distinctly. Validate host and packaged ARM Python behavior, exact image changes, filesystem, scatter and fallback before handoff. Re-audit at candidate closure; no physical gate is promoted by host/emulated checks.

## Platform v1 physical qualification stop — 2026-09-25

Session A FAIL; B/C/D NOT_TESTED. No milestone closure or physical promotion. The owner clarified the installed UI candidate after the initial plain-candidate source mismatch. Its exact Linux/Reborn metadata matches the entry record below, and all four installed Reborn ELF hashes match the UI candidate manifest. Boot ID `083d4abb-a447-4ac6-a063-e8898c150bca` remained unchanged through the final 14:36:05 UTC evidence capture. No firmware/code/policy change or reboot occurred.

Fresh narrow evidence: internal eMMC on `11230000.mmc`, expected Y2ROOT/Y2DATA UUIDs/geometry, distinct read-write mounts, clean boot fsck and zero ext4 error counters. Boot stages record switch_root 9.73 s, first frame 57.785 s and application_ready 64.718 s. The owner sees the main menu and reports normal warmth. One snapshot reads CPU 48.500°C / PMIC 46.298°C. USB owner-key SSH remains available. These observations do not establish repeated boot, library readiness, input/audio operation, durability, performance, radio connections or endurance.

Two installed-platform defects prevent the mandatory baseline: CLI-local `network_check.check` shadows health's `check`, raising UnboundLocalError; and the observer reads `/sys/power/wakeup_count` synchronously, blocking in `pm_get_wakeup_count` with a charger wakeup source active. Source hashes match the inspected repository files. No charger/wakeup-policy change is justified. The exact orphaned diagnostic query was stopped after its evidence was saved; final process inspection finds no leftover query. No production service was restarted, source fixed or replacement installed.

Before/after dmesg retains 28 warning/error-priority entries, including repeated rate-limit notices, timer/cache descriptions, the PMIC LED node lookup, memory-protection configuration, retained p8 clipping, regulator get_mode and Bluetooth extended-feature messages. These are not 28 independent faults. No retained WARN stack/Oops/panic/ext4-I/O error is found; taint stays 0. The owner's kernel-warning rule still stops Session A without silently exempting historical warnings. Detailed owning areas and all limitations are in the [physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-PHYSICAL-QUALIFICATION.md).

Refresh every freeze-matrix area from this evidence: boot/storage/display/USB gain the narrow observations above but remain PARTIAL; telemetry/readiness now has observed failures. RAM/DMA/SMP, buses/clocks/reset, input, power/idle/suspend, audio, SD, radios/calibration, time/entropy, updates/backup and release retain all prior untested/blocked boundaries. No reserved-memory, hardware, production or protected-data scope changes. Fresh read-only GitHub inventory retains #16/#27/#28/#29/#31/#32/#33/#34 OPEN and #30 CLOSED; no remote mutation.

Next smallest blocker: separate corrective software work for telemetry plus source-backed review of the recorded warning classes, then repeat Session A on the exact resulting installed pair. This qualification request does not itself authorize implementing, rebuilding or installing fixes. Session B–D workloads, endurance and separately controlled E/F/G do not advance. Seven passive long-run plans are prepared locally with the clarified identity; none was executed. No unchanged source/ROM/calibration provenance or build was repeated.

## Platform v1 physical qualification entry — 2026-09-25

The owner authorizes supervised Sessions A–D with no flash, rebuild, production code change, protected-data write or hardware-policy change. Following an exact identity mismatch against the original Platform v1 package, the owner clarified that the installed/intended package is `out/y2linux-reborn-ui-v1-candidate/`. Bind this run to its versions file; preserve the original mismatch as evidence. Long runs and Sessions E/F/G remain separately gated.

Fresh authenticated USB identity at 14:23:49 UTC, boot `083d4abb-a447-4ac6-a063-e8898c150bca`, matches that package's complete versions metadata: Platform v1 Linux `d04b95aaff713edf943042d97a4c6134ca19fc24`, Reborn `155608393f6acfc6657f2f2e23cd07d0533479c6`, kernel `6.18.0-y2linux-platform-v1-candidate-01`, rootfs `2025.02.18-platform-v1.1`. Local package checksums pass 133/133; installed whole-image hashes were not read. The owner authorized updating the stale host-key pin after a direct USB topology check; strict checking and the existing owner login key are retained. The trust record explicitly states that the fingerprint was not independently read from a device console.

Re-read Storage06, GPU-01, CONNECTIVITY-10 and USB reconnect hardware receipts and every September 23 freeze coverage row. Boot/rescue, kernel, RAM/DMA/SMP, buses/clocks/reset, display/input, SD/eMMC, power/thermal/idle/suspend, audio, radios/calibration, USB, time/entropy, userspace/shutdown, update/backup and release retain their physical gates. Fresh enumeration and metadata reads do not promote a subsystem. No unchanged ROM/calibration acquisition or build was repeated. Existing issue ownership remains; no milestone or remote status changes.

Entry limitation: `y2-status system --json` timed out after 50.050 seconds with no output, while a simple authenticated identity query subsequently succeeded. Obtain the required baseline and diagnose this observation before workloads or reboot/recovery tests. Stop on the owner's fault conditions. No source fix or workaround is authorized merely to pass a test. The [physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-PHYSICAL-QUALIFICATION.md) and private receipts retain exact commands, identities and limits. Repository review head: `d6811ffed028e73d90a8b146e576310319734187`. No physical acceptance is declared.

## Reborn UI v1 software candidate handoff — 2026-09-24

Boundary: close the owner-authorized application implementation and preserving candidate work, without accepting Platform v1 hardware or authorizing installation. Reborn compiled source is `155608393f6acfc6657f2f2e23cd07d0533479c6`; the platform inside the image remains `d04b95aaff713edf943042d97a4c6134ca19fc24` with the existing Platform v1 kernel/rootfs. Linux changes for this task are these audits only.

Re-read the actual Storage06 identity/internal-boot receipt, GPU-01 native 480×360 Lima/S16/input results and failed same-boot deep resume, CONNECTIVITY-10 adapter/scan-only result, and two old-policy USB reconnect observations linked below. No new hardware evidence, device access, ROM provenance repetition or physical test occurred. Refresh every coverage row in the freeze matrix: all remain PARTIAL, with existing UNKNOWN/BLOCKED_BY_EVIDENCE/DEFERRED extensions. Boot/rescue, memory/DMA/SMP, clocks/reset/watchdog, display/input/wake, SD/eMMC, power/thermal/idle/suspend, wired audio/radios/calibration, USB, clock/entropy, userspace/shutdown, update/reset/export and release retain their exact prior gates. The 4 MiB font atlas and bounded art allocations add application measurement work; they do not change platform memory ownership or establish target resource limits.

Fresh software receipts: 177 Rust tests (29 UI), warning-free all-target Clippy, format checks, 54 relevant Platform v1 regressions, 20 host daemon checks, eight packaged ARM userspace QEMU checks, 1k/10k/20k host and ARM-emulated library runs, 69 native-size reviewed previews, and a fresh Cortex-A7 ARMv7 hard-float build. ELF/GLES/media dependencies, embedded assets/provenance, exact root readback, ext4 checks, unchanged critical platform files and ANDROID-only selection pass. These establish HOST_TESTED/ARM_BUILT/IMAGE_VALIDATED only.

Candidate: `out/y2linux-reborn-ui-v1-candidate/`; root SHA-256 `edcecfaae26b8102c071000b5d2e9e5f84626ad08e3ff5818b050174f301a044`. An exact previous root is retained in `fallback/`. No BOOTIMG or Y2DATA payload, erase/format instruction, protected partition or calibration operation is included. The required already-installed Platform v1 BOOTIMG remains SHA-256 `f7b4a950a0504a411ad72db0aac9398f04dc1ccabd6a6a0a3a7fdab198ca2622`.

Readonly GitHub reconciliation still finds #16/#27/#28/#29/#31/#32/#33/#34 OPEN and historical #30 CLOSED; no remote mutation or milestone promotion is warranted. Backup/calibration/recovery/trusted-power prerequisites and development-key limits remain. Next smallest boundary is owner Session A with the exact root/BOOT pair, physical UI legibility/focus/wake, RSS/PSS and audio coexistence, followed by relevant B–G sessions. Reset execution remains the platform's authenticated stopped-service maintenance flow. Decision: **software candidate ready for owner-controlled review; physical qualification pending**. No flash, push, or platform feature expansion.

## Reborn UI v1 candidate build admission — 2026-09-24

Reconcile the owner UI brief with the implemented application, the activation and graphics-memory audits, the retained Storage06/GPU-01/CONNECTIVITY-10/USB results, and the Platform v1 capability/owner-qualification ledgers. Every hardware coverage row remains PARTIAL with its existing blocked/deferred extensions; issue statuses and backup/calibration/trusted-power prerequisites remain unchanged. No new physical observation or qualification is claimed.

UI-specific and full Rust workspace host checks pass; the 54 relevant Platform v1 contract, Bluetooth, network/time, power, update, transfer, storage and reset regressions pass. Native 480×360 previews have received repeated visual review. These admit the next software step, not a release or hardware acceptance.

Decision: ready for a fresh ARMv7 application build using the existing Platform v1 SDK, then a preserving application-only root candidate if all checks pass. Reuse the exact manifest-verified Platform v1 root and required BOOTIMG; replace only application ELFs and application release metadata. Retain platform source, rootfs and kernel identities, recording the UI package identity separately. No kernel/Buildroot/DT/boot/hardware policy rebuild or extension is required. Select ANDROID/Y2ROOT only; include neither BOOTIMG nor Y2DATA payload, and retain an exact root fallback. Inspect ELF dependencies, media ABI, image contents, filesystem, scatter selection and artifact hashes before declaring a candidate. Owner review still requires the exact Platform v1 BOOTIMG as a prerequisite.

## Reborn UI v1 bounded graphics memory review — 2026-09-24

Before further artwork integration and candidate production, repeat the activation coverage audit above the frozen platform boundary. Re-read the retained GPU-01 480×360 Lima/input/wired evidence and Storage06 internal-boot evidence: neither qualifies the new UI font footprint or collection-art decoding on this candidate. The remaining radio, USB, power, suspend and update evidence limits in the activation matrix remain unchanged; no new hardware evidence was collected.

The application uses one shared 1024×1024 RGBA font texture (4 MiB), replacing two small ASCII atlases, to provide readable proportional Latin/Greek/Cyrillic text and bounded replacement glyphs. A separate 160×160 collection-art texture (100 KiB), a bounded four-entry decoded-art cache (400 KiB) and one bounded worker are permitted within the owner-authorized application rebuild. No RAM reservation, DMA, kernel, graphics-driver or platform memory policy changes. This is application allocation scope only. Decoding must remain off the UI thread, responses must be matched to route/source identity, and no music-sized textures or unbounded caches are permitted.

Decision: proceed with these explicit bounded application allocations, retain all hardware epics and qualification gates, and measure target RSS/PSS, input latency and audio underruns during owner review. Host tests and previews are not target memory/thermal/endurance qualification. Audit again at packaging.

## Reborn UI v1 application activation — 2026-09-24

Starting pair: Linux `8959c3439a2305934151141c7346c455460e0be7` / Reborn `5bab207ae662dafe31544fe5948f68e702ea33fa`. The owner explicitly requests the complete application UI candidate on Platform v1, local commits and preserving packaging, with no flashing. This later decision authorizes application work before physical Platform v1 acceptance; it does not accept those hardware gates or authorize platform expansion.

Re-read the retained Storage06, GPU-01, CONNECTIVITY-10 and USB reconnect owner evidence linked in the freeze audit below. Storage06 establishes old-image internal identity/boot/SSH; GPU-01 establishes 480×360 Lima, balanced input and S16/44.1 audio under bounded load, with failed same-boot deep resume; radio scans establish adapters, not association or peer audio; two USB workaround reconnects are narrow old-policy evidence. No new device access or evidence is claimed. The Platform v1 completion/capability/owner ledgers and actual Reborn source are the application contract; older Reborn audit proposals are superseded only by source-backed correctness and Platform v1 implementations.

Every coverage row in the freeze matrix below was reviewed: boot/rescue, kernel, RAM/DMA/SMP, clocks/regulators, reset/watchdog, display/GPU, wheel/Power, SD, eMMC/layout, power/charging/thermal, CPU/idle, suspend, wired audio, radios, firmware/calibration, USB, clock/entropy, userspace/shutdown, update/reset/export, and build/release remain PARTIAL, with the exact existing UNKNOWN, BLOCKED_BY_EVIDENCE and DEFERRED extensions retained. UI changes can add IMPLEMENTED/HOST_TESTED/ARM_BUILT/IMAGE_VALIDATED application evidence only. No memory reservation, hardware policy, calibration, encoder or partition change.

Readonly GitHub inventory confirms #16/#27/#28/#29/#31/#32/#33/#34 OPEN; #30's narrow historical acceptance remains CLOSED with the later adverse suspend evidence preserved. No issue or milestone qualification status changes, remote messages or new epics are needed for this local application task. Existing backup/calibration/trusted-power conditions remain owner prerequisites for later physical work. Unchanged ROM/recovery provenance is not repeated.

Decision: ready for bounded application implementation. Keep semantic input, AppModel/effects/workers, actual platform observations, GLES dirty rendering and queue occurrence identities. Audit again before candidate packaging/closure. The next physical boundary remains owner Session A, then relevant B–G on exact candidate hashes. A UI screenshot is not physical or endurance qualification.

## Platform v1 software freeze boundary — 2026-09-23 UTC

Final built pair: Linux `d04b95aaff713edf943042d97a4c6134ca19fc24` / Reborn `6c8aa128550ec80addd08ef3145e9d5a846ddf2e`. This review precedes the software candidate declaration. The owner's completion request permits a v1 with explicit unavailable hardware features; it supersedes older all-features phase ordering, without turning an old experiment into production acceptance.

Re-read the actual [Storage06 owner result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-13-storage06-owner%2FREADME.md), [GPU-01 result and failed same-boot resume](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-18-gpu01%2FREADME.md), [CONNECTIVITY-10 adapter/scan result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-17-m5-connectivity10%2FREADME.md) and [two USB workaround reconnects](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-15-usb-reconnect%2FREADME.md). Their original image/source identities and limits remain authoritative. No new physical evidence, repeated ROM provenance, device access or flash occurred. The already-present USB PM reference correction was preserved, not duplicated.

Current source passed kernel/config/ABI/artifact, Buildroot ARM, Reborn ARM, FFmpeg/ELF, 64 host platform cases, 56 locked platform cases (two dependency skips covered by separate host/ARM checks), 68 production, 39 subsystem and eight QEMU userspace checks. Reborn's unchanged final source passed 155 host tests, formatting and strict all-target clippy. Seven actual ARM updater fault tests, three installed SFTP protocol cases, installed ARM Python/ALSA/default-settings/ 1k library checks, full production ARM signed-payload verification and bad signature refusal passed. The preserve-data package and root ext4 contents pass. These are IMPLEMENTED/HOST_TESTED/ARM_BUILT/IMAGE_VALIDATED evidence only.

This table refreshes every coverage area; the older matrices below are history. PARTIAL means candidate physical or endurance qualification remains open.

| Coverage | Current classification and next boundary | Tracking |
| --- | --- | --- |
| Boot, native PID1, rescue, root handover | PARTIAL: guarded layout/fsck/ABI and rescue retained; current software/image checks pass. Storage06's 8.729 s handover is old-image evidence; exact candidate boot/rescue next. | #28/#32/#33 |
| Kernel stability and maintenance | PARTIAL: source-bound checks and bounded boot/crash records; repeated boot/soak still physical. | #28/#32 |
| RAM, reserved/DMA ownership and SMP | PARTIAL: existing four-core/LOWMEM/HIGHMEM map retained; no reserved-memory reclamation. Measurement/growth tools added; target pressure/endurance remains. | #28 |
| Clocks, resets, pinctrl/GPIO/IRQ, I2C/PWRAP/regulators | PARTIAL: existing Linux ownership preserved; no new voltage or electrical sequence. Existing narrow transport proof does not qualify all power transitions. | #28/#29/#30 |
| AP reset/watchdog and early UART/panic retention | PARTIAL/UNKNOWN: bounded previous-boot evidence is implemented; AP watchdog recovery is disabled, exact retained reset cause/pstore/UART remains unproved. Charger watchdog is separate. | #16/#28/#32 |
| Display, framebuffer, backlight, DRM/KMS/Lima | PARTIAL: GPU-01's narrow rendering/runtime-PM proof retained; candidate first-frame readiness is truthful. Current UI/panel/recovery and longer runs await owner. | #28/#34 |
| Wheel/buttons/evdev, Power key and wake | PARTIAL: prior balanced events retained; candidate interaction and wake remain separate, no touchscreen claim. | #28/#30/#34 |
| SD and ext4/FAT/exFAT | PARTIAL: implemented generation/UUID/controller-instance lifecycle, safe removal/error handling and scratch tools; old SD boot proof is not hotplug/full-card/endurance proof. | #28/#33 |
| Internal eMMC and root/data layout | PARTIAL: original geometry/identity preserved; reserves, SQLite faults and signed offline root recovery implemented. Physical write tails/electrical durability remain. | #28/#32/#33 |
| PMIC, battery, charging and thermal | PARTIAL: voltage/source/configured limits and die sensors exposed. No guessed pack temperature/current/SOC or new charger setting; thresholds, reserve and current charging envelope require evidence. | #28/#30 |
| CPU OPP/governor/tick/idle | PARTIAL: existing 598/747.5/1040 MHz fixed-voltage/WFI policy retained; counters/workload tools added. No deeper-idle/SPM/voltage experiment. | #28/#30 |
| Runtime PM, suspend/resume and RTC wake | PARTIAL: prior normal GPU runtime PM retained; failed same-boot deep resume and later unqualified CPU mask correction preserved. Deep suspend defaults off; leases/query tools do not prove resume. | #30/#34 |
| AFE/ASoC/ALSA/I2S and CS43131 analog path | PARTIAL: S16 stereo 44.1 baseline; direct 48 constraints exist but product profile stays 44.1. S24/S32/24-bit precision/88.2/96 and advanced analog policy remain evidence-gated. | #29 |
| Wi-Fi, Bluetooth and coexistence | PARTIAL: full readiness/DHCP/DNS, single reconnect ownership, SBC/PCM/AVRCP and qualified Auto foundations implemented. Actual association/peer audio/coexistence remains physical; optional encoders deferred. | #31 |
| Firmware, per-device calibration and FM | PARTIAL/explicit exclusion: matched owner firmware hashes retained, redistribution not established; no protected calibration write. FM remains unsupported on this board. | #31/#32 |
| USB device, transfer and host role | PARTIAL: USB-bound owner SSH/SFTP, reserve/hash publication and protocol faults pass; current reconnect/PC sleep/throughput needs qualification. Host/OTG/VBUS/UAC host unavailable pending board proof. | #27/#28/#32 |
| RTC, time, entropy, identity and private diagnostics | PARTIAL: standard NTP/clock/CRNG/persistent-seed contracts implemented; RTC retention/wake and real boot timing remain physical. No fabricated reset cause or authenticated-time claim. | #28/#30/#32 |
| Production userspace, shutdown and privilege | PARTIAL: bounded independent shutdown, maintenance holds and service readiness implemented. Most services/app remain root; broad privilege separation deferred. | #28/#32 |
| Update, rollback, recovery, reset and backup | PARTIAL: signed root-only staging/offline verified backup/write/readback/restore and boot-health timeout implemented; scoped reset/export pass faults. BOOTIMG stays manual/non-atomic; electrical update recovery remains physical. | #32/#33 |
| Build, security and release | PARTIAL: exact paired sources, source/hash/license inventory, ARM/image validation and owner sessions ready. Development trust only; byte-identical reproducibility, production key deployment and product endurance are not established. | #32/#33 |

Readonly GitHub inventory still has #16/#27/#28/#29/#31/#32/#33/#34 OPEN and #30 CLOSED. The prior narrow M4 acceptance is preserved alongside later adverse evidence. No milestone closure, remote comment, account/identity change or push is needed or performed for this local software freeze. Unresolved owner backup, calibration retention and trusted-power requirements still apply before physical maintenance; no repeated acquisition is implied by this documentation audit.

Decision: ready for Y2Linux Platform v1 Candidate software freeze, partially ready for owner qualification, not a physically qualified release. Core contracts are implemented and validated; excluded capabilities stay explicit. The next smallest boundary is owner Session A on the exact hashes, followed by B–D and separately controlled E/G. Session F's wider formats remain blocked until complete AFE/clock evidence. After the advertised core is physically accepted, return general development to Reborn and keep Y2Linux in maintenance. Any later hardware, memory or production-scope extension requires another standing audit.

## Platform v1 release/endurance implementation boundary — 2026-09-23

At Linux `648fbea` / Reborn `41214d0`, phases 1–7 have implemented software contracts or explicit evidence gates. The fresh USB/update pair `1c2451e` / `f4b83b7` passed kernel/ARM/image/FFmpeg checks, production suites, eight QEMU userspace checks, seven ARM updater fault cases and the actual ARM SFTP protocol fault check. New maintenance/evidence code still awaits the final fresh build.

Re-read Storage06's authenticated identity/fsck/handover receipt, GPU-01's narrow rendering/S16 result and failed same-boot resume, CONNECTIVITY-10's scan/adapter receipt, and the two earlier USB workaround cycles. None supplies candidate physical, network connection, SBC, electrical update or endurance qualification. The later USB PM fix already exists; no duplicate fix is needed. Original ROM, calibration and recovery provenance is unchanged and is not repeated.

All coverage remains explicit: boot/rescue/crash; RAM/SMP/reservations; clock, regulator and interrupt ownership; eMMC/SD; display/GPU/input; wired audio; battery/thermal/RTC/idle/suspend; Wi-Fi/Bluetooth; USB; time/security; update and build/release. Optional codecs, deeper idle, high-resolution AFE, AP watchdog recovery and host VBUS do not have sufficient implementation/qualification proof. No speculative hardware change is warranted. #16/#27/#28/#29/#31/#32/ #33/#34 remain open; #30's prior narrow acceptance remains distinct. No tracker mutation or hardware authorization is inferred.

Phase 8 is ready for software: integrated passive endurance orchestration, source/footprint/security inventory, exact-source fresh qualification and a preserve-data candidate package. Physical sessions A–G remain owner-controlled. Freeze requires a second boundary audit and passing final receipts; it is not already declared. Automatic BOOTIMG OTA, production signing authority, battery thresholds and deep suspend remain excluded or gated. No flash or real device connection occurs during this work.

## Platform v1 low-power/audio evidence boundary — 2026-09-23

Linux `df7d3a8` / Reborn `41214d0`: signed root-only rescue and scoped maintenance are implemented and host tested. The fresh USB/update build at `1c2451e` / `f4b83b7` is in progress; subsequent reset/export source has no ARM receipt yet. No physical work occurred. Re-read the exact GPU-01 rendering/audio and adverse suspend receipt: clean S16/44.1 audio is narrow evidence; same-boot resume failed, and later CPU3 mask correction has source/host evidence, not a physical pass.

All coverage rows remain accounted for: boot/rescue/crash, RAM/reservations/SMP, clocks/interrupts/regulators, eMMC/SD, display/input/GPU, wired audio, power/thermal/ RTC/idle/suspend, radios, USB, time/security and release. Software updates now have authenticated offline recovery foundations, not electrical durability proof. #16/#27/#28/#29/#31/#32/#33/#34 stay open; the earlier narrow #30 acceptance is preserved. No remote issue changes or new hardware authorization are inferred.

Phase 7 may inspect pinned MT6582/Y2/vendor and upstream sources, add safe observation/qualification tools, and change a driver only where complete packing, clock/power and board evidence support it. The known WFI-only idle state is not permission to copy a donor SPM program. Existing corrected suspend remains an owner-controlled PHYSICAL_GATE. A 32-bit I2S slot is not 24/32-bit DMA precision; S32/rate masks must remain closed unless the entire fetch/interconnect/clock path is established. No reserved memory, voltage, trip point or VBUS change. The next independent work is exact source-backed feasibility plus qualification fixtures, then integrated release/endurance hardening and current-source builds.

## Platform v1 signed recovery implementation boundary — 2026-09-23

Linux `ba3ac58` / Reborn `87a46cb`: USB owner transfer has focused host fault coverage; the earlier pair `1f54bd0` / `87a46cb` completed a fresh ARM build, with production/QEMU checks in progress. USB changes are not covered by that build. No new physical evidence exists. Re-read Storage06's owner identity, fsck/handover and SSH receipt and CONNECTIVITY-10's adapter/scan receipt: neither proves update interruption, root write durability, network readiness or SBC.

The full coverage matrix retains its physical classifications and limitations: boot/rescue/reset, memory/reservations/SMP, clocks/regulators/interrupts, storage/SD, display/input/GPU, audio, battery/thermal/RTC/idle/suspend, radios, USB, time/security and release. Software USB authentication/reserve/atomic publication advances; host role/VBUS remains gated. No protected partition, reserved memory, charger, SPM or regulator scope changes. Existing open #16/#27/#28/#29/#31/#32/#33/#34 and accepted narrow #30 remain; no remote changes.

Phase 6 proceeds under the owner's explicit software authorization: signed root-only staging, a small independently trusted rescue verifier/writer, verified previous-root backup, readback and bounded boot-health acknowledgement. Rescue size budgets stay unchanged. Private signing material stays off-device/outside repositories. Key rotation/revocation must account for the immutable BOOTIMG trust store; automatic BOOTIMG replacement remains excluded. Host file faults and current-source ARM/image validation precede offering a candidate. Electrical interruption, rescue access and rollback are PHYSICAL_GATE. No real device is contacted, and no documentation or build receipt supplies hardware authorization.

## Platform v1 USB and recovery software activation — 2026-09-23

Boundary: Linux codec/reconnect sources follow `f2db217`; Reborn follows `7892115`. The fresh phase-3 pair `ea50d53` / `ce55f89` passed kernel/ARM, production/platform/subsystem suites and eight QEMU userspace checks. New Bluetooth observer/reconnect/AVRCP/Auto code has focused host evidence, with its own paired ARM build pending. Optional encoders are unbuilt/distribution-gated.

Re-read USB POWER-02's own two reconnect records and CONNECTIVITY-10's own adapter/scan receipt. The former is a runtime-PM workaround result, not proof of the later already-present session-reference source fix; the latter still has no network association or paired audio evidence. Storage06's narrow verified root/data identity and rescue access do not qualify interrupted updates. No new physical results are inferred from software builds.

All coverage rows remain accounted for: boot/rescue/reset, RAM/reservations/SMP, clocks/regulators/interrupts, storage/SD, display/input/GPU, audio, power/thermal/ RTC/idle/suspend, radios/firmware, USB, updates/security/time and releases. Their retained physical evidence and gates are unchanged. No controller/PHY/VBUS, charger, memory, SPM or protected-partition change is authorized. #16/#27/#28/ #29/#31/#32/#33/#34 stay open, prior #30 acceptance stays narrow; no remote tracker changes. Roadmap entries 5–6 now proceed as software under owner scope.

USB work is authenticated USB-interface-only file transfer and bounded standard protocol tooling. Host role/VBUS stays PHYSICAL_GATE until board wiring/current proof. Rescue work may add signed root-only staging/offline install/readback, health acknowledgement/restore, scoped reset and backup. BOOTIMG remains manual: single-slot rescue replacement cannot be made atomic by software policy. Fake files/devices must cover interrupted writes before any installation is offered. No active mounted root write, ordinary Y2DATA replacement, calibration access or physical qualification is included. Builds/packages retain explicit evidence levels and exact source identities; software progress does not close milestones.

## Platform v1 Bluetooth software activation — 2026-09-23

Boundary source Linux `80dc891`, Reborn `ce55f89`. Phase-2 Linux `5049761` / Reborn `17dd464` built kernel/ARM/rootfs; installed QEMU app checks and the actual 1k library/scanner/UI benchmark passed. The production suite stopped on the host-only shim's off64_t portability error; `44cf4ac` fixes it, rerun pending. Phase-3 shutdown/network/time/media changes have focused host evidence; Reborn workspace tests passed. They await their own ARM build, not inherited proof.

All September 23 coverage rows remain physically unchanged: core boot/rescue, identity/storage, RAM/SMP/reservations, clocks/regulators/IRQs, display/input, S16 wired audio, USB, power/thermal/idle/suspend, radios, firmware, updates, security/time/entropy and recovery retain their narrow prior evidence or gaps. The software advances are now independent shutdown/media policy, truthful IP/DNS readiness, clock strategy and per-device entropy persistence. No new voltage, PMIC, reserved-memory or hardware scope is introduced.

Re-read own CONNECTIVITY-10 summary: adapter power and simultaneous Wi-Fi scan passed, but zero saved networks and no paired peer/SBC data were tested. The codec audit is a design source, not hardware authorization. Current source supersedes its older findings: BlueZ 5.87/BlueALSA 5.0.0/libsbc 2.2 are pinned; Reborn already sets Trusted after successful owner-initiated pairing, observes Format/Rate and invalidates transport generations. Do not reimplement those fixes.

Next software boundary under #31/#29/#32 is typed D-Bus observation, bounded single-owner reconnect coordination, Reborn AVRCP semantic actions and codec Auto eligibility. Production Auto requires build/runtime/remote/distribution AND qualification gates; current integrated SBC qualification is absent. Optional encoders can be researched and built in explicit experimental profiles where source/license evidence permits, never advertised as qualified. AAC patent, aptX trademark/library and LDAC certification/distribution limits remain separate from source availability. LE Audio/ISO, Adaptive/Lossless stay unsupported.

#16/#27/#28/#29/#31/#32/#33/#34 remain open; accepted #30 is preserved. No remote milestone closure/update is warranted by these software-only increments. Physical pairing/SBC/reconnect/AVRCP/coexistence and codec qualification remain PHYSICAL_GATE; continue authorized software work and exact qualification preparation.

## Platform v1 power/time/network software activation — 2026-09-23

Boundary source: Linux `9f347cf`, Reborn `17dd464`. Observation ARM/QEMU receipts are for `82da3f9` / `d9ba054`; subsequent SD/space/library/resource code has host evidence and awaits the next paired build. The 22 platform and focused Reborn tests cover the new software contracts. No hardware acceptance is added.

Coverage is refreshed against all rows of the September 23 evidence ledger: boot/rescue and identity, RAM/SMP/reservations, clocks/IRQ/regulator ownership, display/input, audio, USB, eMMC/SD, power/thermal/idle, radios, firmware, updates, security/time/entropy and recovery retain their physical classifications. The only advances are software observation, mount claims/space policy, exFAT tooling, benchmarks, resource logging and reduced Reborn navigation allocation. Kernel SD support is source-only until rebuilt. No memory/electrical scope changes.

Re-read CONNECTIVITY-10's own interface/scan result (no saved network, WPA/IP/DNS or peer audio test), GPU-01 owner audio/input observations and retained charging state (450 mA is a programmed limit, not battery current). Later low-voltage charger source remains unqualified; historical wrong RTC date and deep-resume failure remain adverse evidence. M4 #30 owner acceptance is preserved. Issue ownership remains #28/#30/#31/#32/#33, with #16 early evidence and #27 USB open; no remote tracker mutation or new physical milestone is appropriate.

Phase 3 is ready for software: a UI-independent bounded shutdown handshake, disabled-by-default threshold mechanism, sane-clock/TLS readiness and standard NTP, and one DHCP/DNS lifecycle under the existing supplicant owner. No charge limit, RTC register algorithm, SPM sequence or battery cutoff is invented. Thresholds/reserve, RTC retention, poweroff/reboot, association/DHCP/DNS and reconnect remain PHYSICAL_GATE. Proceed with software and fake-environment failure tests; physical sessions remain owner-controlled.

## Platform v1 storage/measurement activation — 2026-09-23

Before phase 2, source `6c9b991` has 24 passing targeted telemetry, handover and splash tests; its fresh kernel/Buildroot build is running against unchanged sources. Isolated local worktrees keep later implementation out of that receipt. No physical evidence changed: Storage06 remains narrow mount/readback proof; DEV-02's memory test and GPU-01's audio/render trace are not storage benchmarks. The same open #16/#27/#28/#29/#31/#32/#33/#34 and accepted #30 apply. No remote status transition is warranted. All entry coverage rows and exclusions remain.

Phase 2 is ready for software work: descriptor-relative scratch-only I/O, space reserves and disposable-cache policy, SD mount identity/generation, read-only filesystem checks and Reborn's real SQLite/scanner measurements. Linux 6.18 already includes exFAT; pinned Buildroot supplies GPL exfatprogs. Enabling this maintained filesystem does not change controller clocks, voltages, partitioning or recovery policy. Card/media-loss/durability/performance are PHYSICAL_GATE. No automatic filesystem repair or user music deletion. Measurement tools do not authorize their unattended use on the Y2. Software benchmark results will distinguish cache state, process crashes and actual electrical durability. High-resolution audio and deeper idle research remain separate evidence gates.

## Platform v1 completion entry — 2026-09-23

The owner now authorizes a major software completion pass, including kernel changes only where evidence supports them, focused local commits and fresh candidate builds. No physical Y2 activity is authorized. Entry heads are Linux `5f6b446` and Reborn `d9ba054`; supplied uncommitted review documents are preserved in the [completion ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-COMPLETION.md). Current source and later correctness closure supersede older repaired findings.

The real-device evidence is unchanged: Storage06 proves narrow internal boot and identities; GPU-01 proves narrow rendering/runtime PM and S16 stereo 44.1 kHz, but records failed deep resume; CONNECTIVITY-10 proves scans and simultaneous adapter power, not IP or A2DP; POWER-02's two USB reconnects used a workaround. The subsequent session PM-reference fix already exists and will not be duplicated. No current-source physical or endurance acceptance is inferred. Prior M4 owner acceptance is retained without extending it to the later charger revision.

| Coverage / issue | Boundary decision |
| --- | --- |
| Boot/recovery/diagnostics #16/#28/#32/#33 | Software telemetry, health, boot stages/history and bounded readiness may proceed; reset registers/retained panic and whole-system watchdog need evidence. |
| Memory/CPU #28 | Observe existing HIGHMEM, reservations, fixed-voltage OPPs and WFI; no reserved-memory reclamation, voltage scaling or guessed SPM programming. |
| Storage/SD #33 | Implement identity/generation, space policy and scratch/SQLite tooling; no raw-device benchmarks, music deletion or repartition. |
| Display/input/GPU #34 | Preserve current DRM/Lima/evdev; same-boot deep wake remains PHYSICAL_GATE. |
| Battery/thermal/RTC #30/#28 | Implement mechanisms and truthful die telemetry; low-battery thresholds and charging acceptance remain PHYSICAL_GATE. |
| Wired audio #29 | Qualified product profile stays S16/44.1; packing/clock evidence precedes any wider-format implementation, and physical precision proof remains mandatory. |
| Wi-Fi/Bluetooth #31 | Finish service readiness and application integration; one reconnect owner; codec provenance/distribution and physical eligibility stay explicit. |
| USB #27/#28 | Productize USB-only authenticated transfer; retain PM fix; unknown host VBUS/role wiring remains PHYSICAL_GATE. |
| Updates/security #32/#33 | Signed, staged, rescue-assisted Y2ROOT implementation may proceed; no mounted-root writes or automatic BOOTIMG replacement. |
| Calibration/firmware/FM | Owner-provided provisioning and protected exclusions retained; no new calibration access or FM scope. |
| Build/release/endurance #32/#33 | Fresh current-source software/ARM/image checks and exact owner qualification package; no physical closure. |

Read-only tracker inventory still shows #16/#27/#28/#29/#31/#32/#33/#34 open and #30 closed. No milestone/epic status change is justified; remote writes are outside this local implementation pass. The [software roadmap](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Fplatform-v1-roadmap.md) is updated before activation. Phase 1 is ready for software implementation; later phases advance in dependency order. Physical gates stop only their own workstreams. No unchanged ROM/recovery provenance is repeated.

## Whole-platform owner review — 2026-09-23

The documentation-only [current platform review](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md) and [evidence ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Fplatform-review-evidence-2026-09-23.md) reassess boot, recovery/updates, storage/SQLite, CPU/RAM, thermal/battery/power, suspend, connectivity/USB, diagnostics, endurance and release maintenance as shared application contracts. Reviewed heads are Y2Linux `5f6b446` and Y2Reborn `d9ba054` (packaged Reborn code `dde3c53`). Existing physical receipts were read first; current source and the candidate metadata were then inspected. No new physical observation, test, build or unchanged ROM/recovery revalidation occurred.

Retained Storage06/DEV-02, GPU-01, CONNECTIVITY-10 and older Reborn observations support narrow internal boot, core/input/display, wired audio, GPU runtime PM and radio discovery. The latest candidate remains physically unqualified. Deep resume, current charging-policy measurements, complete network/audio services, storage performance/durability and integrated endurance remain open. Current USB session-PM ownership and Reborn receipt/storage/trust fixes are recognized as implemented; their presence does not establish physical closure.

GitHub was read: #16/#27/#28/#29/#31/#32/#33/#34 remain open and #30 closed. Storage milestone 3 remains active; M4 owner acceptance is preserved alongside the later power/suspend evidence limits. No tracker or milestone state changes. Protected storage, reserved RAM, firmware/calibration ownership, manual deployment and existing recovery limits remain authoritative.

The proposed order is observable/recoverable reference platform, durable storage and resource budgets, qualified power lifecycle, complete connectivity, then maintainable releases and recoverable updates/OTA. These are recommendations under existing epics, not phase activation or hardware/implementation authority. The next proposed work is shared telemetry, storage/SQLite characterization and the normal-runtime low-battery contract. Any implementation or physical milestone boundary must repeat this audit with its exact scope and hardware evidence.

## Reborn software-correctness candidate boundary — 2026-09-23

This repeat audit precedes packaging the focused Reborn correctness closure as an owner-controlled physical-qualification candidate. The reviewed code heads are Y2Linux `df1bccf` and Y2Reborn `dde3c53`; neither repository contains uncommitted product-source changes at this point. The Y2Reborn worktree's pre-existing untracked `docs/audit/`, `docs/review/`, and `docs/architecture/bluetooth-codecs.md` remain user-owned and untouched. The software closure log is [`LUNA-CORRECTNESS-CLOSURE-01.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FLUNA-CORRECTNESS-CLOSURE-01.md).

No new physical evidence is claimed or sought: the device was not accessed. The latest retained device evidence remains the 2026-09-18 GPU-01 receipt and 2026-09-17 CONNECTIVITY-10 receipt below. GPU-01 supports narrow Mali-400/Lima rendering, S16 stereo 44.1-kHz wired playback and bounded Wi-Fi scan/radio coexistence; it records a failed deep-suspend attempt, so GPU #34 stays open. CONNECTIVITY-10 supports Wi-Fi discovery and concurrent adapter power only; association, DHCP/DNS, Bluetooth pairing/A2DP and sustained coexistence remain untested. Neither receipt qualifies this Reborn revision, its corrected PCM conversion, sink failures, scan behavior, Bluetooth transport epoch, or the candidate package. Software and QEMU evidence below cannot replace those owner-run checks.

The GitHub issue state was read on 2026-09-23: #16, #27, #28, #29, #31, #32, #33 and #34 are open; #30 is closed. Storage / Installation milestone 3 remains active under #33. No issue, milestone, or physical gate is closed by this candidate. The existing platform phase dependencies and protected-storage, backup/calibration, recovery, power and radio limits are unchanged.

| Coverage row | Current evidence and remaining boundary |
| --- | --- |
| Boot, core and memory | Existing narrow production boot remains the recorded baseline; the closure changes no kernel, memory reservation, preloader or LK. Broader stability remains #28. |
| Internal/removable storage and recovery | Existing internal root/data identity is retained; SD mount identity now gates Reborn pruning in software. Physical SD removal/reinsert and broader recovery remain #33. |
| Display and GPU | GPU-01's narrow rendering result is retained; deep resume is still failed/unqualified under #34. No display/GPU changes here. |
| Buttons, wheel and input | Prior device event capture remains evidence only for physical event delivery. R8 cancellation is host-tested; current Reborn hardware mapping/hold behavior still needs owner qualification. |
| Power, RTC and charging | M4 #30 is closed per the issue tracker; GPU-01's failed same-session suspend remains a separate open #34 gate. No policy or hardware changes here. |
| Wired audio | Only the recorded S16 stereo 44.1-kHz physical result is accepted. R2's S24-in-32 behavior is software-tested and does not authorize higher-resolution output. |
| USB/SSH | Existing pinned USB path remains; reconnect issue #27 is open. This pass does not change USB ownership. |
| Wi-Fi | Scan/interface startup remains the narrow physical result. WPA association, DHCP, DNS, reconnect and sustained operation remain open under #31. |
| Bluetooth | Adapter power is the narrow retained result. Pairing/SBC playback/reconnect/coexistence are unqualified under #31; R9 transport epoch invalidation is software evidence only and plug-hidden negotiated-format verification remains partial. |
| Firmware, calibration and identity | Existing owner-supplied files are hash-verified for this offline build. No new firmware, calibration, NVRAM or protected-storage access occurred. |
| GPU/power interactions | No candidate test qualifies suspend, charging, thermal behavior or deep resume; issue #34 stays open. |
| FM and unrequested features | Existing board exclusion remains. USB Audio, high-resolution wired output, optional codecs, OTA/A-B, exFAT and UI redesign remain out of scope. |
| Updates, security and privacy | The generated update preserves Y2DATA and selects only approved system partitions; broader recovery/update contract remains #32/#33. |

The candidate boundary is software-ready for owner review only once the fresh ARM build, runtime/component checks and preserving-package validations listed in the closure log pass. It does not activate or close a platform milestone. The next smallest evidence boundary is manual installation of the exact hash-verified preserving candidate, followed by the ordered owner qualification checklist in the closure log. Power/charging/suspend remains a separate safety-scoped activity. No GitHub status transition is warranted.

## Reborn software correctness closure entry — 2026-09-22

This entry records the owner-authorized, software-only correctness closure boundary before implementation. Entry revisions are Y2Linux `8e5b53bc9fb934e1f668b9e7e9e34f0fc5e4130e` and Y2Reborn `8a1443daa25419834c800a7f9d707e66f80e0f90`. Y2Linux was clean; Y2Reborn had pre-existing untracked `docs/audit/`, `docs/review/`, and `docs/architecture/bluetooth-codecs.md`, which are retained. The latest independent source review is Y2Reborn `docs/review/CURRENT_PROJECT_STATE.md` and `LUNA_STABILIZATION_REVIEW.md`; it recommends keeping this base and lists R1–R10 as the finite software correction scope. This user instruction now authorizes that scope and targeted tests; it does not authorize physical work or a platform milestone closure.

The latest retained real-device evidence remains from the earlier GPU-01 and CONNECTIVITY-10 boots, not these revisions. GPU-01 records Mali-400/Lima rendering and clean wired stereo `S16_LE` 44.1-kHz playback during its bounded workload, while its deep-suspend trial failed and GPU #34 remains open. CONNECTIVITY-10 records Wi-Fi scans and concurrent adapter power with no core errors; association, DHCP, DNS, Bluetooth pairing/A2DP, and sustained radio coexistence remain unqualified. M4 has owner acceptance recorded, not a new charging/thermal series. Storage #33 still lacks the remaining owner physical acceptance. No physical result is inferred for current Reborn, the current userspace stack, Bluetooth audio, current sink reconfiguration, or these software fixes.

The current open platform issues were read from the repository's issue tracker: #27, #28, #29, #31, #32, #33, and #34 remain open, as does #16. Their existing platform scopes and gates are unchanged. This pass introduces no kernel, memory, partition, charger, suspend, radio-policy, or audio-hardware change; stock preloader/LK, protected storage, Y2DATA preservation, and platform ownership remain as reviewed. There is no reason to repeat unchanged ROM, recovery, or physical provenance checks.

Authorized next boundary: correct Reborn R1–R10 at their software failure boundaries, add targeted host tests, record partial/physical limitations, and prepare an exact preserving candidate only if all required fresh software, ARM, FFmpeg, and package checks pass. Stop before physical qualification. The next hardware step remains owner-controlled use of that exact candidate, with power/charging/suspend separately scoped; no platform milestone is closed by this implementation or a successful build.

## Reborn startup-latency inspection — 2026-09-18

This audit is repeated before a targeted production startup correction using the owner-installed audio candidate and current real-device evidence. Read-only SSH identifies the running boot as Linux `6.18.0-y2linux-gpu-02`, with Mali400 EGL/GLES active and the current FFmpeg runtime reporting `9.0.1`. The retained boot trace shows the splash visible at `0.828 s` and released/presented at `52.047/52.060 s`; Y2ROOT completes its handoff at `12.246 s`.

The Reborn session trace and `/proc` task start times localize the delay: the process is created near `19.5 s`, its first application log appears near `41.0 s`, and the first frame is presented near `52.1 s`. The cold process startup is currently coupled to direct FFmpeg shared-library loading before `main`; Reborn then spends about `3.5 s` reaching the scan worker and `6.2 s` creating the GPU context. The SD card also reports a dirty FAT volume and remains an independent storage-health issue.

This authorizes a bounded Reborn/Y2Linux startup optimization: keep FFmpeg as the only decode/DSP implementation, load its shared media membrane after the UI process is alive, retain bounded worker behavior, and add phase timing to the existing diagnostics. The implementation boundary also starts Reborn after `S02y2-data` and before optional radio/network services, whose Reborn workers already retry until their providers appear, and opens the GPU context before the library scan while the splash retains KMS ownership until the first frame. It does not authorize flashing, protected or calibration writes, Y2DATA replacement, hardware qualification, or changes to the physical audio sink profile. Existing GPU, radio, storage, power and audio qualification gaps remain open.

## Reborn audio-stack architecture boundary — 2026-09-18

This audit is repeated before the requested production audio architecture change. The latest retained real-device evidence is `docs/hardware-evidence/2026-09-18-gpu01/audio.txt` and its README: the owner-confirmed wired CS43131 path is clean for stereo `S16_LE` at 44.1 kHz, with no XRUNs during the GPU workload. That evidence does not qualify `S32_LE`, 48/88.2/96 kHz, Bluetooth A2DP playback, or high-resolution analog output. The retained audio architecture also records the driver-side 8–48 kHz rate table and 32-bit slots as source/driver evidence, not physical acceptance.

The requested Reborn change is authorized as a host/cross-build application and rootfs implementation boundary. Y2Reborn owns one FFmpeg 9.0.1 decode, libavfilter DSP, and libswresample conversion pipeline; Y2Linux owns the pinned Buildroot component set, runtime verification, ALSA capability probe, and production packaging. The software qualification profile therefore starts with the physically evidenced wired rate and refuses to advertise unqualified sink combinations. S32 transport and additional rates remain pending until the owner manually installs the candidate and captures real `Y2Audio` ALSA hardware capabilities and playback results. Bluetooth remains a separate physical gate, but must consume the same processed PCM stream in source.

Required exit evidence for this boundary is a committed pair of source trees, actual FFmpeg 9.0.1 library/version and component manifests from the built rootfs, deterministic source/DSP/gapless fixtures, host and ARM-emulated tests, rootfs/package preservation checks, and a manual-install receipt. No BOOTIMG, protected/calibration partition, or Y2DATA write is authorized by this audit. The next physical action is owner installation and qualification of the candidate; no physical success is claimed by host or emulated tests.

## Reborn audio production-candidate qualification boundary — 2026-09-18

This standing audit is repeated before closing the requested audio-stack implementation boundary. The real-device evidence is unchanged: the retained GPU-01 receipt confirms clean wired CS43131 playback only for stereo `S16_LE` at 44.1 kHz under the recorded workload. It does not qualify `S32_LE`, 48/88.2/96 kHz, Bluetooth A2DP, or high-resolution analog output. The MT6582 driver's 32-bit slot and rate-table evidence remains implementation evidence, not physical acceptance.

The candidate now has the required committed Y2Linux/Y2Reborn source pair, actual FFmpeg 9.0.1 build and runtime manifests, deterministic format/artwork/ corruption/gapless fixtures, host workspace tests, ARM-emulated runtime checks, rootfs preservation validation, and a preserving manual-install package. The software boundary is therefore ready for owner review. The candidate's audio profile prefers `S32_LE` and source-native rates, but the shipped qualification profile activates only the physically evidenced `S16_LE`/44.1 kHz wired combination and logs an explicit fallback for unqualified sink combinations.

This closes the offline implementation and packaging boundary only. Manual installation and real-device qualification remain the next owner action; S32 transport, additional rates, Bluetooth playback, and CPU/RAM measurements on MT6582 remain open. No flash, protected/calibration partition write, Y2DATA overwrite, or hardware acceptance is inferred from this candidate.

## Reborn radio scan UI correction — 2026-09-18

Following the installed splash inspection, the owner reports that pressing Scan in either radio screen shows no progress or devices. The observed on/off/scan events and source confirm that Scan did not enable an off radio, Wi-Fi lacked completion state, and neither radio rendered discovery progress. This authorizes a targeted application correction and root-only candidate, not a radio-driver, kernel, splash, charging or platform redesign. Existing splash BOOTIMG and exact installed splash root fallback are preserved; stop for owner installation.

Implement explicit bounded worker scan state, radio activation on Scan, results and empty/error feedback, screen-local radio status, and suppression of repeated Select activation while a key is held. SSH radio commands must use the same workers as the UI for subsequent qualification. Host mock supplicant/private D-Bus tests must distinguish progress, completion, errors and power-off; they do not establish physical pairing or association. No software is installed over SSH and no live radio configuration changes are needed for this source fix.

The [root-only candidate](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Freborn-radio-ui-01-deployment.md) is now built from Reborn `a8ae8b6` / integration `640ecb8`: 64 Rust tests, 20 host daemon checks, four tooling tests, eight ARM application/shell checks and Clippy pass. Offline Buildroot and raw rootfs comparisons pass; exactly five application/identity files change, used root space increases 52 KiB, and the splash BOOTIMG remains byte-identical. The installed splash root is the exact root-only fallback. STOP for owner manual installation, then qualify the actual UI-worker commands over SSH before requesting visible scan/peer confirmation. Physical success for this correction, association/pairing and broader Baseline 01 gates remain open.

## Reborn splash installed and radio inspection — 2026-09-18

The owner reports the manually flashed startup update works and requests SSH inspection because Reborn displays radio unavailability. No new install, reboot, pairing, network connection or milestone expansion is authorized by this report. The [splash receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Freborn-splash-01-deployment.md) retains matched BOOTIMG/root/fallback hashes and the unchanged kernel/display/charging evidence.

SSH confirms installed Reborn `6209f48`, root `Y2LINUX-REBORN-SPLASH-01`, Mali400, and explicit splash release/presentation at boot 49.448/49.456 seconds. All ten safe application baseline checks pass. Both radio services are present but both radios start off. Explicit bounded Reborn scan tests pass: Wi-Fi finds 28 networks; Bluetooth powers/discovers successfully with no discoverable peer; BlueALSA is available. Tests restore prior radio state. Same boot/session, no new radio or GPU-context errors and zero kernel connectivity errors/recoveries.

Reborn conflates disabled Wi-Fi with unavailable and writes its error into a global UI notice that persists on the Bluetooth screen. This is an application status defect, not evidence that the underlying radio stack failed. Capture is in Y2Reborn `docs/validation/2026-09-18-radio-inspection.md`. No radio/UI fix was installed during this inspection. Association/DHCP, pairing/A2DP, charging and suspend acceptance remain pending; GPU #34/M5 #31 and full Baseline 01 stay open.

## Reborn splash-only boundary — 2026-09-18

The owner reports deployed REBORN-BASELINE-01 working and authorizes only startup UX: retain the stock logo, hide panel console, show a lightweight loading screen, and explicitly hand display ownership to the first Reborn frame. Read-only SSH confirms root marker Y2LINUX-REBORN-BASELINE-01, source 77e6732, Mali400/EGL and overall health ok. This is not acceptance of previously pending audio/radio/ suspend gates and does not authorize Reborn 02.

Live boot evidence makes a BOOTIMG initramfs change necessary: framebuffer console attaches at 0.745889s; switch_root occurs at 9.213802s. Y2ROOT alone cannot hide that interval. Preserve the exact GPU-02 kernel, display module, charging program, boot arguments, partition geometry, firmware and Y2DATA. Change only early normal boot display policy/helper, matching root splash integration, and the DT initrd end address required by the new archive size. Charging remains in its existing initramfs path. No live install, reboot or display takeover during development.

The candidate must prove unchanged kernel/module/charging bytes, bounded protocol and timeout recovery, offline cross build, root/initramfs consistency, D08/BOOTIMG bounds and exact Baseline-01 fallback. Stop for owner manual installation, then qualify actual visible boot/handoff. Existing GPU #34/M5 #31 gates remain open.

## Reborn Baseline 01 implementation boundary — 2026-09-18

The owner now explicitly requests native Reborn implementation, Buildroot integration, host/cross validation and a manual-install handoff. This supersedes the older Reborn implementation exclusion; it does not close GPU #34 or M5 #31. Entry is platform `16b2fb8`, Reborn `93454b5`. The initial SSH attempt timed out. The owner subsequently reports GPU-02 installed and connects USB. Read-only SSH using the retained September 15 host-key pin confirms Linux 6.18.0-y2linux-gpu-02, Y2LINUX-GPU-02, Y2Audio, evdev names, DRM nodes and power/backlight classes. Reborn retains the capture in docs/validation/evidence/platform-entry.txt. No suspend, radio connection or playback qualification is inferred from inspection.

| Coverage | Current evidence and remaining qualification |
| --- | --- |
| Boot/SMP/RAM/core buses | Narrow production boot confirmed; preserve memory exclusions; broader stability pending (#28). |
| Internal/SD storage and recovery | Y2ROOT/Y2DATA confirmed; SD uses explicit y2-media mount policy; Reborn hotplug pending (#33). Recovery/factory inputs unchanged. |
| Display/GPU | 480x360 Mediatek KMS + Lima/GBM/EGL/GLES confirmed in GPU-01; GPU-02 resume unqualified (#34). |
| Input | Evdev wheel/buttons confirmed; application mapping/overlap pending (#24/#34). |
| Power/RTC/charging | M4 owner accepted; CPU ACK correction built in GPU-02, same-session resume still pending (#30/#34). No live suspend authorized by this implementation step. |
| Wired audio | S16 stereo 44.1 kHz CS43131 confirmed; Reborn/FFmpeg path pending (#29). |
| USB/SSH | Pinned owner SSH and live GPU-02 interface inventory confirmed (#27). |
| Wi-Fi | Scans/radio startup confirmed; association/DHCP/reconnect pending (#31). |
| Bluetooth | BlueZ adapter and concurrent radio power confirmed; pairing/A2DP/BlueALSA pending (#31). |
| Firmware/calibration/identity | Existing owner provisioning retained; no new acquisition or protected writes (#31). |
| FM | Board exclusion retained. |
| Updates/security/privacy | Existing owner SSH and manual installation retained; no OTA/M6 expansion (#32). |

Reborn implementation is authorized; physical acceptance is pending. The next boundary is a tested application/rootfs candidate with exact provenance and a manual owner installation. BOOTIMG and known fallbacks must be preserved unless an independently justified platform correction becomes necessary. Public remote issue changes are deferred to an authorized publishing step; local audit is updated here. No physical success is claimed by host or emulated tests.

The [REBORN-BASELINE-01 candidate](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Freborn-baseline-01-deployment.md) now passes 50 Rust tests, 20 daemon checks, 3 tooling tests, 8 ARM runtime/shell checks and the retained 94 platform regressions. An offline production rootfs build and root-only preservation checks pass. Reborn source `77e6732`, integration `08b0e7d`; BOOTIMG is byte-unchanged and fallback is the exact GPU-02 root. Read-only live BlueALSA ObjectManager inspection succeeds with no peer PCM present. This closes the first implementation/build boundary only. STOP for owner installation; Reborn, GPU resume and M5 physical qualification remain open.

## GPU-01 physical result and targeted GPU-02 correction — 2026-09-18

Owner-deployed `7c43557` proves Mali-400 MP2 r1p1, mainline Lima render node, Mesa 24.0.9 hardware EGL 1.4/GLES 2.0, visible native 480x360 PRIME/KMS rendering, 30.00 FPS at 3.36% CPU, static runtime/domain off, application termination recovery, clean wired audio and GPU + Wi-Fi scans/concurrent Bluetooth power with zero radio errors/recoveries. [Physical receipts](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-18-gpu01%2FREADME.md).

GPU #34 remains OPEN; NOT READY TO BEGIN REBORN. Actual sleep qualification finds an all-off radio-status formatting refusal, then a failed same-session wake. A retained bounded `pm_test=core` trace localizes CPU3 power-off timeout: status clears bit 9 while code waits for bit 13. Actual retained Y2 stock and pinned GPL source prove CPU1/2/3 masks 0x800/0x400/0x200 and combined 0xe00. GPU-02 corrects those ACK/boot/entry tests and the radio zero-format matcher. The [integrated GPU-02 package](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-gpu-02-deployment.md) is now built from `7e318af`, with 94 tests, nine package rejection cases and exact emitted root/DT checks passing. STOP for owner manual deployment; no assistant flash. No PCM, voltage, frequency, GPU/display/radio architecture or memory change.

This updates only the observed gap inside the authorized GPU qualification; it is not a new M5 entry audit or a milestone closure. M4 remains the owner-accepted foundation, with this pre-existing CPU-mask defect now recorded as a targeted residual exposed by GPU qualification. Live fault containment leaves CPUs 0–2 online, SPM broken=1 and prevents another sleep attempt on that boot; charging, storage and radios remain operational. Requalification must use the owner-installed corrected candidate, not an attempted runtime kernel patch.

Remaining: same-session deep RTC/Power wake, retained-context and fresh rendering, no-client suspend, display/backlight/offline-charge regression, strict input and animation overlap, and targeted post-resume state. M5 connection/peer/audio and sustained/full traffic coexistence stay pending by owner choice. Reborn, M6/OTA and unrelated milestone residuals remain out of scope.

## GPU-01 candidate — 2026-09-18

Implementation and host validation are complete for the authorized GPU scope: source `7c43557a38fac6bbdb0ab5628cffe131ebda6360`, Linux 6.18 Lima, Mesa 24.0.9 Lima/kmsro, existing KMS, owned CCF/SPM runtime power and standard GBM/EGL/GLES. Own hardware/stock evidence identifies Mali-400 MP2 and the 500.5-MHz MMPLL branch, including this unit's retained devinfo selector flag. Silicon revision and every physical graphics acceptance gate remain pending.

[GPU-01 deployment receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-gpu-01-deployment.md): one integrated BOOTIMG/Y2ROOT package, preserved Y2DATA and RAM exclusions, exact known fallback pair, 92 passing regression tests, nine preservation rejection cases, emitted DT validation and ARM/root checks. Stop for owner deployment; no assistant flash. GPU #34 stays OPEN; not yet ready to begin Reborn. M4/CONNECTIVITY-10 remain the physical baseline and remaining M5 connection/audio tests stay pending. This is implementation progress within the already reviewed scope below, not a new M5 audit or a physical milestone closure.

## GPU activation boundary — 2026-09-18

Owner authorization explicitly activates production GPU implementation alongside pending M5 qualification. This is the GPU scope review required by the standing rule, not another M5 entry audit. Entry: clean `c70ff07`; current native CONNECTIVITY-10 hardware evidence overrides every older startup-blocked row. The [retained GPU inspection](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-18-gpu-contract%2FREADME.md) records the live hardware contract; the [GPU-02 receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-gpu-02-deployment.md) retains the subsequent correction and manual-deployment boundary. No builds, flashes, radio operations, new protected-data acquisition or repeated provenance checks occur in this review.

All coverage areas below were reviewed. This table supersedes the historical September 15 matrix where statuses differ; unchanged residuals are retained.[](https://github.com/SchulzCode/Y2Linux/issues/34)

| Coverage | Current classification and evidence / next gap | Tracking |
| --- | --- | --- |
| Boot, PID1, SMP, core buses, RAM | CONFIRMED narrow production boot; PARTIAL broader stability. CONNECTIVITY-10 live, 952480 KiB; identical exclusions. No RAM expansion. | #28 |
| Internal/removable storage, root/data | Internal boot and persistent data CONFIRMED; broader storage/recovery qualification PARTIAL and unchanged. BOOTIMG/Y2ROOT may change; Y2DATA preserved. | #33 |
| Display, panel, backlight | Visible existing DRM/KMS and 480x360 panel CONFIRMED. GPU sharing, page flips and resume with GPU UNTESTED. Keep the same display owner. | #25/#28; GPU |
| Wheel/navigation/volume/Power | Existing balanced events CONFIRMED; response during GPU workloads UNTESTED. | #24/#28; GPU |
| M4 PMIC, charging/watchdog, thermal, CPU DVFS/idle, suspend/wake/RTC | POWER-03 owner-accepted, #30 CLOSED. Latest CPU/PMIC readings plausible; no new suspend/charging stress claimed. Preserve protection and run targeted GPU coexistence checks. No separate GPU sensor identified. | #30; GPU |
| Wired audio and analog routing | Clean S16/44.1-kHz headphones CONFIRMED. Other retained M3 residuals remain PARTIAL; GPU/audio coexistence UNTESTED. | #29; GPU |
| USB/SSH and physical UART | Current pinned USB SSH CONFIRMED. Broader reconnect PARTIAL; physical UART UNKNOWN. Do not reopen unrelated work. | #27/#28/#16 |
| Wi-Fi | wlan0/cfg80211, scans, disable/re-enable CONFIRMED at CONNECTIVITY-10. WPA2/DHCP/DNS/data and saved-network reconnect UNTESTED; owner elects pending. | #31 |
| Bluetooth | Standard BlueZ power-on with Wi-Fi CONFIRMED. Peer pairing/SBC/AVRCP/reconnect and sustained coexistence UNTESTED; owner elects pending. | #31 |
| Firmware, calibration and identity | Working native factory reader, BTIF/AP_DMA, controller 6582/8a01/8a00 and WMT startup CONFIRMED. Preserve private inputs/identities; no reacquisition. | #31 |
| GPU | Own stock GP + two PP resources/IRQs CONFIRMED; donor reports Mali-400 MP2 Lima. Silicon revision, production Lima/EGL/GLES, runtime PM and rendering UNTESTED. Implement through existing ownership. | GPU #34 |
| FM | CONFIRMED board exclusion, unchanged. | #31 |
| Recovery/backups, updates/security, privacy/non-root lifecycle | PARTIAL with retained gaps; no OTA/security scope expansion. Existing recovery remains owner's operation. | M0/#32/#33 |

Ready for authorized GPU implementation; not physically qualified. M5 stays open but is no longer an implementation gate for GPU. One integrated candidate must include exact artifacts, fallback pair and a coherent qualification sequence. Reborn starts only after the GPU acceptance decision; Reborn and M6 are excluded from this session. No diagnostic Mali stack, Android EGL, second display owner, raw-MMIO userspace or permanent GPU power-on is authorized as the product path.

## CONNECTIVITY-10 physical Wi-Fi result — 2026-09-17

Owner-installed -10 exposes stable wlan0/cfg80211, and two scans return 23 and 12 BSS entries. Runtime Wi-Fi restart and BlueZ power-on with Wi-Fi active succeed. Core/transport errors and recoveries remain 0, kernel taint is 0, and no diagnostic module or runtime correction is used. [Physical result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-17-m5-connectivity10%2FREADME.md).

The missing completion callback on regulatory TX power command `0x38` was the exact -09 blocker. Its targeted correction is now physically verified. The [installed BOOTIMG and -09 fallback](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-m5-connectivity-10-deployment.md) retain -07 root/data, Bluetooth fixes and M4. Both radios and saved preferences are returned off. No network is configured; association/DHCP/data and broader Bluetooth/coexistence qualification remain open. M5 #31 is ACTIVE / WI-FI AND BLUETOOTH ADAPTERS VERIFIED / CONNECTION AND RADIO QUALIFICATION OPEN. This remains an interface checkpoint within M5, with no major boundary crossed.

## Wi-Fi exact regulatory failure / CONNECTIVITY-10 correction — 2026-09-17

Targeted -09 SSH diagnostics show Wi-Fi firmware ready and successful RF/BB capability queries. The exact failure is the regulatory TX power OID (`0x38`): successful transmission frees the no-response command without completing its waiter because the producer omits its callback. The subsequent timeout causes EIO recovery and interface teardown. [Physical evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-17-m5-wifi%2FREADME.md).

[CONNECTIVITY-10](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm5-connectivity10-corrections.md) supplies that command's standard completion callbacks, with unchanged wire format, power policy and transport. Sixteen targeted checks pass, including old-source failure replay. Build BOOTIMG-only, retain -07 root/data and working -09 Bluetooth fallback, then verify after manual owner installation. No new hardware/memory scope or major milestone transition. M5 #31 remains ACTIVE / BLUETOOTH ADAPTER VERIFIED / WI-FI OID CORRECTION / QUALIFICATION OPEN. Both radio preferences remain off; BlueZ power-on/off is rechecked after diagnostic cleanup. Accepted M4 remains intact.

## CONNECTIVITY-09 physical result / permanent BlueZ adapter — 2026-09-17

Owner-installed -09 reaches standard hci0/BlueZ on normal boot. Both patch downloads/resets, the 630-byte RF calibration result and HCI initialization succeed. Standard runtime BlueZ power-on/off works with zero core errors, transport errors or recoveries. No diagnostic module or runtime correction is used; kernel taint is 0. [Physical result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-17-m5-connectivity09%2FREADME.md).

The original EPROTO was rejection of the successful RF result. The later `0x1004` page-2/status-`0x30` defect is corrected only for `6582/8a01/8a00` using the existing Linux quirk and verified page limit. The [-08 trace and controlled test](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-17-m5-connectivity08%2FREADME.md) remain the causal evidence. Its Wi-Fi test reached function enable and Wi-Fi Start but recovered with EIO before wlan0; that exact next failure remains open.

CONNECTIVITY-09 is installed from `f55fff4`, BOOTIMG 6150144 bytes, SHA256 `200346dff20ea1ffe769278bc8c52a19402d850a380c2054f6e93d1ef167de7a`. Fifteen targeted checks and emitted artifact/package checks pass. [Deployment receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-m5-connectivity-09-deployment.md). Retain -07 root/data and -08 BOOTIMG fallback. Both radios and saved preferences are returned off. Accepted M4 is intact; pairing/audio/coexistence remain open. M5 #31 is ACTIVE / BLUETOOTH ADAPTER VERIFIED / WI-FI STARTUP FAILURE / QUALIFICATION OPEN. No major milestone transition or broad audit is implied. Installation-pending descriptions below are historical.

## CONNECTIVITY-07 exact protocol failure / CONNECTIVITY-08 correction — 2026-09-17

Live SSH identifies MT6582/HVR `8a01`/FVR `8a00`. A stopped-buffer snapshot proves full STP negotiation, both patch downloads and both resets succeed. The next RF calibration event is 630 bytes with valid checksum/CRC and success status; the native 256-byte reply limit rejects it as EPROTO. This supersedes the provider/TX-pending descriptions below. Factory acquisition, DMA/IRQ and identification are settled and are not repeated.

[Physical evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-17-m5-protocol%2FREADME.md) and [the scoped correction](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm5-connectivity08-corrections.md) preserve strict framing/status checks and accept only this controller's extended RF result during its matching command. Build CONNECTIVITY-08 BOOTIMG-only, retain CONNECTIVITY-07 root/data and its BOOTIMG fallback, then use the established manual installation boundary before live BlueZ/cfg80211 checks. M5 #31 stays ACTIVE / PROTOCOL CORRECTION / PHYSICALLY UNQUALIFIED. M4 remains accepted. No milestone transition, RAM/platform expansion, GPU/Reborn or broad audit.

CONNECTIVITY-08 is now built from `8b18ca3`: BOOTIMG 6150144 bytes, SHA256 `5b8e333cdb9fff7bf314abf905ad11a7f26d23e8dab4fd4a4cf78a0bd58b0d78`. Fourteen targeted connectivity checks, original-failure replay, emitted artifact and BOOTIMG-only package validation pass. [Ready manual handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-m5-connectivity-08-deployment.md). New hardware progress remains pending installation; no radio readiness is inferred.

## CONNECTIVITY-06 physical result / mounted-eMMC correction — 2026-09-16

Internal eMMC is mmcblk1 on this owner-installed boot. Root/data work; the provider's hardcoded mmcblk0 fails before activation. TX rearm is not physically exercised yet. [Evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-m5-connectivity-06%2FREADME.md). CONNECTIVITY-07 identifies the mounted root/data parent and retains strict MMC, partition, node and geometry checks. Rebuild the production helper/Y2ROOT with Y2DATA preserved. M5 remains ACTIVE / PROVIDER STARTUP FAILURE / UNQUALIFIED. No protected writes, memory/platform expansion or repeated entry audit.

## CONNECTIVITY-05 physical result / CONNECTIVITY-06 correction — 2026-09-16

Owner-installed CONNECTIVITY-05 completes MD calibration and stays responsive, but its first WMT command leaves two trailer bytes in TX DMA; no TX IRQ is serviced. [Physical result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-16-m5-connectivity05%2FREADME.md). CONNECTIVITY-06 restores the stock per-transfer IRQ rearm/submission order, verified by a regression reproducing that exact stall. It is a BOOTIMG-only correction retaining root/data, memory layout and accepted M4. M5 #31 remains ACTIVE / TRANSPORT STARTUP FAILURE / PHYSICALLY UNQUALIFIED. No entry audit is repeated.

## CONNECTIVITY-04 physical result — 2026-09-16

The owner installed `ac833c8`. SSH confirms CONNECTIVITY-04 kernel, retained CONNECTIVITY-03 root, successful MD completion (`FS=841`) and verified CONN remap/chip ID `6582`. Linux stays responsive through 813 seconds with the same boot ID and no observed Oops/panic, including one bounded runtime recovery. The first WMT command times out; no usable Wi-Fi/BlueZ adapter exists. [Physical evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-16-m5-connectivity04%2FREADME.md) and [85 build checks / 14 package rejection cases](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-m5-connectivity-04%2FREADME.md).

M5 #31 remains ACTIVE / WMT STARTUP TIMEOUT / PHYSICALLY UNQUALIFIED. The next correction uses mandatory STP framing from the first BTIF command, as stock requires. Preserve the remap fix, corrected helper, M4, Y2ROOT and Y2DATA. No scope/memory expansion or repeated entry audit.

## CONNECTIVITY-03 startup crash — 2026-09-16

Early SSH verifies CONNECTIVITY-03 kernel/root and the corrected calibration helper. This unit now completes the MD gate: `stage=2 FS=841 restore=1 open=0 result=0 poweroff=0`. Immediately afterward the owner observes kernel faults on idle CPUs in interrupt processing, and SSH stops responding. This is not a connectivity pass; #31 remains open. CONNECTIVITY-03 is not a working rollback.

Stock FM disassembly confirms a wrong native CONN EMI register offset: INFRACFG + `0x1310` instead of `0x310`. The targeted [CONNECTIVITY-04 correction](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm5-connectivity04-corrections.md) fixes the offset and requires readback before CONN power-on. Build a production BOOTIMG retaining the corrected CONNECTIVITY-03 root and Y2DATA. No RAM/layout expansion, factory write, M4 redesign or repeated entry audit. Physical crash elimination and the remaining radio qualification are still required.

## CONNECTIVITY-02 physical result — 2026-09-16

The owner installed the targeted BOOTIMG correction (`dd84462`). SSH confirms 53 completed calibration FS exchanges (previously zero), followed by an MD_EX firmware exception before readiness. MD shutdown reports success; Wi-Fi and BlueZ remain unavailable. The early regulatory-data error is fixed. Internal mounts/USB SSH work; PC charging shows fault 0 and voltage-hold recovery. [Physical evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-16-m5-connectivity02%2FREADME.md) and [build checks](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-m5-connectivity-02%2FREADME.md). M5 stays ACTIVE / FIRMWARE EXCEPTION / PHYSICALLY UNQUALIFIED. The next work is exception/FS-response diagnosis, not a broad entry audit or M4 redesign. The image is already installed; earlier awaiting-installation text below is history.

## First M5 physical inspection — 2026-09-16

The owner installed CONNECTIVITY-01. Read-only SSH confirms the M5 kernel/root markers, internal p5/p7 mounts and wired SSH. Radio initialization fails at the MD calibration handshake (`stage=1 FS=0 result=-71`), with successful reported MD shutdown and no usable BlueZ adapter or Wi-Fi interface. Early regulatory database loading also precedes rootfs availability; the clock is unset (2022). [Physical snapshot and limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-16-m5-connectivity01%2FREADME.md). M5 remains ACTIVE / STARTUP FAILURE / PHYSICALLY UNQUALIFIED. Make targeted corrections from these observations, then continue the coherent qualification. No new broad audit or M4 redesign is called for by this inspection.

## M5 candidate handoff — 2026-09-16

CONNECTIVITY-01 is built from `022c701010c467904ab6025cd98535d3b861c771`. The integrated kernel/rootfs passed 81 production/M4/connectivity tests, eight isolated ARM userspace checks, emitted memory/DT/BOOTIMG validation, rootfs validation and 16 package rejection cases. The preserving package contains new BOOTIMG/Y2ROOT and the accepted POWER-03/previous-root fallback; there is no Y2DATA payload. No assistant deployment or protected write occurred.

[Complete manual handoff, image hashes and physical procedure](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-m5-connectivity-01-deployment.md). M5 #31 is ACTIVE / AWAITING OWNER INSTALLATION / PHYSICALLY UNQUALIFIED. Stop for manual installation, then perform one coherent SSH qualification. Silicon stepping, own calibration completion, radio functionality, EDR/BLE, coexistence, recovery and M4 regression remain physical gates. FM is excluded on this older board. This is a build/implementation update using the completed entry audit below, not another broad entry audit or a milestone closure.

## M5 implementation authorized — 2026-09-15

The owner reports that POWER-03 works and explicitly accepts M4, then requests M5 implementation. This is owner acceptance, not a new agent-run measurement series. It supersedes the pending-deployment/M4-only instructions below. POWER-03 (`16875c4`, BOOTIMG SHA256 `66b6ecd5ef54da6f3ea07be2c9deda284d0a7636e9c6da4c5d72d84eca5fc010`) is the accepted power-platform baseline and M5 fallback.

Use the completed entry audit at `67cbe8f` without repeating it, as explicitly directed by the owner. M5 #31 is ACTIVE / IMPLEMENTING; native radio behavior is not yet physically qualified. Implement factory-data decoding, one shared connectivity owner, AHB Wi-Fi, BTIF/STP/HCI and persistent standard userspace. Preserve M4, the RAM exclusions, protected partitions and Y2DATA. Build one integrated BOOTIMG/Y2ROOT candidate and stop for manual owner installation. Older-board FM, GPU, Y2PlayerNative and OTA implementation remain out of scope.

Native implementation now includes the shared CONSYS/MD calibration owner, BTIF/AP_DMA/STP/HCI, cfg80211 AHB fullmac, read-only factory provider, verified owner firmware loading, standard Wi-Fi/BlueZ/BlueALSA userspace, persistent preferences and a preserving BOOTIMG+Y2ROOT package. See the [implementation and qualification contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm5-connectivity-implementation.md). Source/host checks do not satisfy physical M5 gates; #31 stays open for the manual candidate deployment and coherent physical session. The accepted M4 image remains the fallback; no new M4 physical measurements are claimed.

## Focused M4 completion — 2026-09-15

The owner's latest direction supersedes M5 implementation scope: **finish M4, do not start M5**. The completed entry audit below is retained; no broad audit is repeated. Entry `67cbe8f` is clean. Targeted SSH still finds the same voltage fault with the battery now about 3.74 V. The existing SPM, storage, audio and minimal offline architecture remain the production foundation.

[POWER-03 source corrections](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-end-user-power.md%23power-03-correction-of-observed-failures--2026-09-15&anchor=power-03-correction-of-observed-failures--2026-09-15) address charge cutoff/hold, the stock OVP setting, first-fault evidence, RTC epoch, word-width thermal efuse acquisition and MUSB runtime ownership. POWER-03 is built from `16875c4` and passes 74 production/M4 tests, ARM rescue checks, package validation and 12 rejection cases. The [BOOTIMG-only handoff](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-m4-power-03-deployment.md) now stops for owner manual deployment. M4 #30 remains ACTIVE/PARTIAL; the full physical exit criteria remain open. No memory/layout/current ceiling expansion, guessed DVFS voltage, protected write or radio implementation.

## M5 fresh-session entry audit — 2026-09-15

Entry audited; integrated M5 implementation/deployment BLOCKED. The owner authorizes a complete production Wi-Fi/Bluetooth audio platform on the current internal-root architecture, with manual deployment only. That supersedes issue #31's deferred planning wording. The requested qualified M4 foundation is not established: charging/offline/deep-suspend/RTC/thermal gates remain substantial.

Entry HEAD `bbbbbf20e96860089b015c19501b7d39638c5419` equalled origin/main, with prior POWER-02 USB/evidence changes, now preserved in `ef285f1`. Read current history/handoff, all eight open issue summaries, relevant epic bodies, current DT/config/BOOTIMG, Buildroot, power/audio/data architecture, stock ramdisk/firmware, own stock radio metadata and pinned donor/RE evidence. Reassessed every coverage row below; settled M1/M2/M3 work remains intact.

[Fresh authenticated hardware evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-15-m5-entry%2FREADME.md) confirms complete image-length POWER-02 BOOTIMG identity, internal p5/p7 ext4 read-write, owner-key SSH, four CPUs and Y2Audio. Strict host-key access matched the exact previously retained September 14 fingerprint; default trust/account settings were unchanged. MUSB is `on/active` with the preserved workaround.

New material failure: at uptime 747.328296 s charging reached 4.200073 V and latched `Y2_FAULT_VOLTAGE=0x8`; it remains off at the fresh inspection. Source explains the 4.2-V software guard, not the analog cause or the separate September 14 OVP `0x10`. SPM has entries=0/resumes=0 on this boot; RTC reports 2082 and thermal accuracy is unresolved. #30 stays ACTIVE/PARTIAL. The earlier short no-fault interval and pending-deployment wording do not override this. The power platform is preserved, not rebuilt under M5.

[The connectivity audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm5-connectivity-entry.md) records own CONSYS_MT6582/BTIF/DMA/IRQ evidence, older-board FM exclusion, five-file stock firmware hashes/header order, AHB Wi-Fi and STP/HCI architecture, userspace, Y2DATA ownership and hard qualification gates. Own NVRAM/PROTECT_F/PROTECT_S were read with bounded normal block reads after identity/geometry checks. Raw data and identifying hashes stay private. Record decoding, actual silicon HVR/FVR and valid addresses remain unproved; external calibration cannot fill that gap. No native radio operation is inferred from source metadata.

Next: resolve #30's charging/qualification failure within M4; reconcile own controller/calibration for #31 before an integrated candidate. No M5 kernel, DT or rootfs change, build, flash, radio enable, protected write or power-state change. No new issue shell or closure. Existing RAM exclusions, storage layout, M3 residuals, recovery and later gates remain. Host firmware extraction reused established ROM provenance; no unchanged full source/ROM/recovery audit.

## Charging-test USB blocker — 2026-09-15

At `bbbbbf2` with the existing September 14 evidence edits preserved, the owner requests a focused fix for the first cable reconnect because it prevents M4 wall-charger observation. Current POWER-02 SSH samples show PC charging active, fault=0 and about 4.13–4.15 V; this narrow result does not resolve the earlier OVP failure or qualify wall charging. Two inspected boots have different uptime histories, and the wall-session log was lost across reboot. An owner-operated five-second removal/reconnect again leaves the Y2 absent from host USB while the owner reports it remains powered on. The saved device log subsequently confirms successful re-entry followed by an IRQ-storm shutdown (`-EOVERFLOW`, -75), rather than a PHY admission failure.

Reviewed every coverage row, current source/retained hardware evidence, and the eight open issues #16/#27–33. The existing #27/#28 reconnect gap now blocks #30; this is a localized repair within the documented M4 test-blocker exception, not a new milestone, hardware subsystem or expanded charging policy. A bounded recorder now saves existing USB/charging diagnostics to production Y2DATA so a required restart need not erase the failure. A standard MUSB `power/control=on` workaround then passes two physical reconnects on one boot, including a DCP wall session of 12.96 seconds with no charging fault. The exact POWER-02 startup workaround is installed and its readback matches source; a fresh boot of that startup edit is not tested. This is a tested workaround, not a kernel fix or full reconnect/charging qualification. Extra idle power is unmeasured. See [the hardware result and limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-15-usb-reconnect%2FREADME.md). All other coverage classifications and phase gates retain their prior limits; M4 stays ACTIVE/PARTIAL. No unchanged source/ROM/recovery audit or broad qualification is repeated.

2026-09-14 post-deployment read-only result at repository `bbbbbf2`: [M4-POWER-02 charging fault](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-14-m4-power02-charge-fault%2FREADME.md). The owner reports wall-charge animation without recovery, then stock recharge and Linux reinstall. USB/SSH identify POWER-02; no physical BOOTIMG hash was taken. In the current normal PC-connected boot, SDP/500-mA allocation works, but 450-mA charging stops after about one second with latched OVP fault 0x10. The earlier wall session is not retained. This supersedes pending-deployment statements, not the limits of prior acceptance. M4 #30 remains ACTIVE/PARTIAL; the next blocker is the first OVP trigger and stock/Linux protection settings, before further charging qualification. Other power, thermal, storage and later phase gates are unchanged. This inspection makes no milestone transition or hardware-scope expansion; no build, flash or device-state write was performed.

2026-09-14 candidate boundary review: M4-POWER-02 from `83d475e` passes 72 production/M4 checks, ARM rescue ABI and package identity/rejection checks. BOOTIMG is 5378048 bytes, SHA256 `1852dfc995953f86ef5c47349515e8d6f06478daa6c1a89efe0f223501c226c9`. The [manual qualification sequence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-m4-power-02-deployment.md) and verified prior charging-kernel fallback are prepared. Reconsidered every M4 exit row against the latest failed 70-mA baseline, source reconstruction and new host results: all new charging/offline/deep-suspend/RTC/poweroff physical gates remain open. Root/data layout, calibration and stock loaders remain unchanged. No M4 closure or M5 activation follows from this candidate.

2026-09-14 implementation audit addendum: actual FM Y2 CPU-domain shutdown, restart-vector ownership and upstream 32-bit ext4 inode initialization are now reconciled in [the active M4 contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-end-user-power.md%23cpu-domain-and-suspend-integration-audit-before-implementation&anchor=cpu-domain-and-suspend-integration-audit-before-implementation). The owner-confirmed device is off; the 70-mA net-gain baseline failed. CPU hotplug, deep suspend and the new charging policy remain unqualified. This authorizes no milestone closure or M5 activation; the current owner request supplies the production hardware scope.

Original audit date: 2026-09-09. Documentation/planning only. No implementation, build, BOOTIMG creation, device access or flash. Repository baseline `00b4afa`; GitHub issues #1–#27 and M0/M1 inspected before adding five deferred epics #28–#32. Y2PlayerNative has no open application issues and its checked-in content remains blueprint/planning material; no native platform readiness is inferred from that.

## M4 end-user completion scope — 2026-09-14

Fresh-session audit at local `aacb9a5`, clean at entry, five commits ahead of the remotely verified `444e7ed`. Re-read the handoff, M4 code/docs and retained stock/ADC/charging evidence, all open issue summaries and epic bodies. The owner's physically observed active M4-CHARGE-01 test supersedes the older inhibited/pending-deployment statements below. The live USB device independently identifies that release; the owner confirmed the changed host key and strictly pinned SSH observation succeeded. The same-boot 70-mA trace then demonstrated falling voltage until the 3.4-V guard stopped charging. The owner switched the Y2 off. This supersedes the initial active-charge report; it is no gain pass.

The owner explicitly authorizes one coherent production completion and physical qualification pass, including stock-evidenced normal charging currents, PC/wall/power-bank source detection, low-battery recovery, **offline charging in the production rescue/initramfs**, deep suspend/same-session resume, device restore, RTC, reboot and actual poweroff. Offline charging includes timed native UI, status versus deliberate Power-on, removal-to-off, and poweroff-with-charger returning offline. This supersedes the earlier fixed-70-mA, configured-host-only scope and the former allowance to close M4 with merely bounded charging.

Reassessed every coverage row: internal root/data, Linux/SSH and the M3 audio foundation remain confirmed within their retained limits; active charging is owner-confirmed but energy gain and final source policies remain unqualified. Thermal/frequency/RTC/PM implementations are not physical acceptance. Deep SPM, offline-charge routing and early recovery require integrated physical acceptance. No memory or storage-layout expansion, loader/calibration changes, M5 activation, or broader qualification claim follows from this audit. #30 remains ACTIVE/PARTIAL; #29 residuals, #33 wider qualification, #27 reconnect and M0/M6 risks remain.

The [current scope and physical exit matrix](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-end-user-power.md) is authoritative over historical checkpoints below. First observe the installed 70-mA/4.175-V profile without changing current, finish source/live investigation, then build one integrated candidate with preserved fallback. Hardware closure requires the complete owner acceptance, including offline charging and genuine deep standby. Percent/current/pack-Celsius may be explicit optional follow-ups under the owner's conditions; the hard power gates may not.

## M4 integrated power activation — 2026-09-13

### Stock-equivalent charging scope — 2026-09-14

The owner now explicitly authorizes reconstructing the actual stock Y2 charging contract and implementing one conservative production candidate at 70 mA / 4.175 V. This supersedes treating missing BATON Celsius as an unconditional gate: an evidenced alternative stock hardware-protection architecture may support charging, while BAT0/temp and current/SOC remain unavailable. It does not authorize disabling or guessing protections, higher current/CV, live charging before the candidate, or assistant flashing.

Entry `d1ac549` is clean. SSH confirms the installed M4-ADC-01, BAT0 present / Not charging, USB online and 3441137 uV at uptime 1243.93 s. The prior 120-sample sensor result is retained, not repeated. Reconsidered all coverage rows and phase gates against this owner correction, current production source, retained stock binary/BSP and all eight open GitHub issues (fresh read, no state change). M4 #30 stays ACTIVE/PARTIAL; M3/storage residuals, deferred USB reconnect and M5/M6/player gates are unchanged. No memory or storage-layout expansion.

The next implementation gate is the real stock charger enable/watchdog, OVP/thermal/presence, USB input and bounded termination contract. Production code must check the preserved protections, fail closed on critical faults, coordinate USB/PM lifecycle and retain the shared PWRAP/MFD owner. Build one BOOTIMG-only charging candidate if that contract is established; physical charging success remains pending the owner's manual deployment and monitored voltage-trend/removal/reconnect test.

Stock reconciliation now establishes the CID2023 PMIC thermal-shutdown init, explicit BATON hot-detector disable, charger enable/WDT sequence, 4050 mV stock top-off threshold, 3 h/24 h budgets and 4110 mV recharge. Production code implements fixed 70 mA/4.175 V, configured USB budget gating, checked hardware protections, fault inhibition, manual standard power_supply policy and PM ordering. The latest inherited battery OVP selector remains unchanged. No pack temperature, measured current or SOC is claimed. [Contract and limitations](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-charging.md).

Reconsidered the coverage matrix before creating the integrated candidate: charging under load, cable reconnect, physical protection behavior, CHRDET wake, off-state insertion and recovery below the conservative 3.4 V start floor remain unqualified. Source and fault-injection tests do not advance those hardware gates. M4 remains ACTIVE/PARTIAL; no new milestone, memory/storage scope or player work.

The final M4-CHARGE-01 candidate is built from `53aa9a6`, reusing Storage06 userspace with one kernel compilation/header correction and no diagnostic image series. Fourteen targeted checks, actual DT/config/layout/rescue ABI and final BOOTIMG-only package validation pass. [Build receipt and hashes](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-m4-charge-01%2FREADME.md). No hardware acceptance status changes: the next boundary is owner manual flash and an attended 70 mA voltage-trend, removal/reconnect and PM regression session.

### ADC owner boot and charging gate — 2026-09-14

Source `bbd0664dcbc1190a5e16e3b3f5889f2154cb04fd` builds one production Y2LINUX-M4-ADC-01 update with unchanged charging inhibition. The owner manually booted it before the packaging handoff. Authenticated SSH confirms the release, all four CPUs, internal p5/p7 and the added IIO channels. A clean kernel build, eight targeted production checks and DT/config/BOOTIMG/package validation pass; root/data are reused. [Artifact receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-m4-adc-01%2FREADME.md).

Reconsidered the coverage matrix and phase gates against this new physical checkpoint and today's existing issue audit. 120 bounded samples plus the owner's normal-handling observation establish raw BATON1/ISENSE acquisition, but no resolved BATON temperature response. Both pack-temperature conversion and sense-resistor/current calibration remain unvalidated. Charging stays blocked at pack thermometry; no production charging policy or final charging candidate is claimed. [Measurements and exact next gate](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-battery-acquisition.md%23owner-deployed-adc-result--same-day&anchor=owner-deployed-adc-result--same-day).

M4 #30 remains ACTIVE/PARTIAL, matching the existing open GitHub epic (read again after the samples); no milestone/epic state transition is required. No closure, new phase, radio/player scope, storage-layout or memory expansion follows. Display/ASoC/PM implementations are unchanged; broader physical qualification and existing ext4 boot warnings remain tracked. The next sensor experiment can use the installed ADC kernel; no further diagnostic image is required to collect readings. The agent did not flash, enable charging, change current/CV/protections, or suspend/reboot/poweroff.

### Charging completion entry — 2026-09-14

Owner explicitly requests one conservative production charging completion pass, with BATON/ISENSE acquisition initially inhibited and a manual BOOTIMG boundary. Current local HEAD is `444e7ed`, clean at entry. Fresh SSH confirms the already owner-deployed `6.18.0-y2linux-m4-01`, continuing uptime, BAT0 present/Not charging, USB ONLINE=1 and configured 70 mA / 4.175 V. The preceding same-device battery audit establishes the raw BATON1/channel 5 and ISENSE/channel 6 paths, but neither had a ready result. Stock compiled NTC/current constants are hypotheses requiring physical validation; PMIC die calibration does not calibrate the pack.

Reconsidered every coverage row below against the current owner scope, current M4 source, retained M2/M3/Storage06 evidence, live M4 bindings/DT/logs and all eight active GitHub issues (#16/#27–33, read 2026-09-14). #30 remains ACTIVE/PARTIAL; #33 wider storage and #29 audio residuals remain open. No phase closes, no radio or player starts, and unchanged provenance/recovery/stress gaps stay open. Current M4 boot, BAT0 and die telemetry supersede the earlier pending-deployment description; suspend, physical poweroff and whole-platform qualification are not inferred from those reads.

The immediate acquisition blocker is concrete: M4-01's built-in PWRAP policy admits only request bits 3/7 at 0x076e (`0x88`), and the ADC driver exposes only those channels. BATON1/ISENSE need bits 5/6. A loadable consumer would still be rejected by that same transport guard. PWRAP has no unbind operation, regmap debugfs is read-only, and KEXEC/KPROBES are disabled. No raw WACS client, guard patching or live kernel memory modification is authorized as a substitute.

The source change is the same production ADC owner exposing BATON1 and ISENSE raw/scale channels with scoped request permissions and propagated conversion errors. Charging enable and all current/CV/watchdog/protection writes remain prohibited until the physical temperature and policy prerequisites are established. This is a prerequisite, not a completed charging implementation. A production BOOTIMG-only sensor update, Y2LINUX-M4-ADC-01, is the minimum supported deployment needed to obtain that evidence. It keeps charging inhibited and is explicitly not Y2LINUX-M4-CHARGE-01. The owner's single final charging-candidate objective cannot be completed on the current guarded boot without this prerequisite. No assistant flash or live kernel patch is performed. The physical NTC connection/conversion is the first unresolved charging gate; input-budget/protection/termination qualification follows it.

[The exact-device evidence, implemented channels and smallest experiment](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-battery-acquisition.md) record this bounded change. Source/transport failure checks and the actual ARM ADC object compile pass before packaging; emitted configuration/DT/BOOTIMG checks apply to the sensor update. Existing M4 physical acceptance remains open.

### Candidate boundary re-audit — 2026-09-14

Reconciled the coverage matrix and milestone gates again before handing off Y2LINUX-M4-01. There is no new physical M4 result: the latest actual hardware remains the authenticated Storage06 baseline and retained M2/M3 evidence. Source commit `f2d2ac641ee67cd94cd2c57c9f5201b6e78841fc` builds one integrated 5355520-byte BOOTIMG. 66 final regressions, ARM ABI/shell checks, emitted DT/config/memory/BOOTIMG validation and 12 package rejection cases pass. [Build evidence and limitations](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-m4-01%2FREADME.md) · [Owner deployment and qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-m4-01-deployment.md).

The implemented power scope uses standard frameworks; battery pack temperature, measured current, capacity and full-charge determination remain unsupported. Charging is inhibited and inherited limits/protection retained. Safe shared OPPs, calibrated die zones, WFI/s2idle, Power/RTC wake and RTC/reset/poweroff are candidate capabilities, not physical acceptance. Current internal p5/p7, M3 startup fix, input/display/USB/audio and Buildroot contracts remain the regression baseline; no root/data update is packaged. Storage06 is the fallback.

M4 #30 stays ACTIVE/PARTIAL, every physical checkbox open. #33 wider storage, #29 narrow M3 residuals, #28 broader stability, #27 deferred reconnect, M0 backup/recovery/calibration residuals and M5/M6/application deferrals retain their prior status. No memory expansion, boot-chain/table/calibration change, new radio or application scope. Stop for the owner's manual BOOTIMG deployment; do not cross into physical PM qualification until that deployment is reported.

### Entry audit

Owner explicitly authorizes a complete generic power-platform implementation, one integrated candidate and read-only live SSH inspection, then STOP for manual BOOTIMG deployment. Entry is local `ae5819f`, ten commits ahead of origin/main. Fresh authenticated SSH confirms Storage06, four CPUs, MemTotal 954376 KiB, internal p5 root/p7 data and no SD block device. The owner explicitly confirmed preserving that current layout; the initial SD-root wording is superseded.

Reviewed the tracked source/config/DT/Buildroot/build/test inventory, local Git history, all open issues #16/#27–33, Storage06 boot/SSH evidence, M2 core evidence, M3 results and the complete coverage matrix below. GitHub's Storage03/SD-root headers are stale compared with local hardware evidence. Canonical ALSA retains the tested period-notification fix `137b3f2`; no solved audio path is repeated. M3's remaining 48 kHz/LR/repeat and wider storage acceptance stay open, but the owner now authorizes M4 progression. Reconnect #27 remains explicitly deferred.

[Current observations and architecture](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-power-platform.md). Only USB presence is currently a power_supply; thermal, cpufreq, cpuidle, RTC and suspend interfaces are absent. Regulator/clock summaries report inherited VPROC 1.15 V and ARMPLL 1.04 GHz. Source-reviewed, bounded regmap reads show charging disabled, configured 70 mA/4.175 V and enabled PMIC thermal calibration; these are not measured battery current or a validated charging policy.

M4 #30 ACTIVE, entry PARTIAL / ready for implementation. One shared PWRAP owner, upstream MFD/regulator/RTC/reset/PM frameworks, checked ADC/thermal and charging semantics, safe OPPs/WFI and suspend-to-idle are the coherent scope. Unknown calibration/pack/OPP facts restrict the affected feature; they do not justify fabricated telemetry or aggressive settings. No hardware success is inferred from compiling. M1 complete, M2 narrow successes, all unchanged coverage rows, M0 backup/recovery/calibration residuals, M5/M6 gates and application deferral are retained. No physical flash or protected-partition write.

## Storage06 owner boot and SSH correction entry — 2026-09-13

### Completed owner flash and authenticated acceptance

At source `dcb7f45fd7fbe0adffc10195239f8df934491c8b`, the corrected initial Y2DATA package passed exact existing-public-key validation, ext4 integrity/identity, actual ARM blkid and eleven isolated package rejection checks. The owner then reported the new image flashed. [Authenticated SSH evidence](https://github.com/schulzcode/y2linux/blob/HEAD/docs/hardware-evidence/2026-09-13-storage06-owner/ssh-result.json) confirms the requested identity now works, both internal filesystems mount read-write, p5/p7 retain exact stock geometry, and no removable SD block device is present. A complete 5193728-byte BOOTIMG read matches the Storage06 package SHA256; all three 512-byte stock table hashes match. Buildroot handover on this boot is at 8.728982 seconds. The live public-key file matches the local `.pub` exactly. No private-key contents were inspected, copied, packaged or committed. The regenerated server key required replacing the host's stale 10.42.0.1 public known_hosts entry with the verified new key. The normal SSH invocation then succeeds; strict host-key checks and all other saved host entries are preserved.

Reassessed every coverage row and phase gate against this new physical result, the earlier ACM/readback/source evidence, the retained firmware/data package checks and today's existing #16/#27–33 snapshot. Internal boot, normal block reads and owner-key SSH are confirmed. Automatic root journal recovery and a new persistent server host key are observed; deliberate scratch-write, protected-region write, stress and power-fail qualification were not attempted. The two synthetic ext4 inode warnings remain recorded; filesystem checks finish cleanly. No table or existing Y2ROOT rewrite, alternate hardware path or further kernel build occurred in the SSH correction.

[The deployed artifacts and limits](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-production-v1-r6-deployment.md) replace the pending manual-flash boundary below. This integrated pass is done; no further flash is required. #33 stays ACTIVE for its wider qualification, so its existing GitHub/milestone status needs no transition and no GitHub write was made. M1/M2 history, narrow M3 audio, deferred reconnect, backup/calibration gaps, M4/M5 not started, M6 planned and application deferral remain unchanged. No later phase starts automatically. The pre-initialization entry follows.

The owner has already flashed Storage06, reports that it works, and requests SSH access/correction in this same production pass. The host observes Linux 6.18.0-y2linux-storage06 over USB ECM/ACM. After assigning10.42.0.2/24 to the active USB connection, Dropbear at10.42.0.1 rejects the explicitly selected existing owner key with `Permission denied (publickey)`. This establishes normal root/service progression beyond the former rescue blocker; full authenticated runtime/storage acceptance is still pending. The renewed ACL allowed [ACM capture](https://github.com/schulzcode/y2linux/blob/HEAD/docs/hardware-evidence/2026-09-13-storage06-owner/result.json): sector0/EBRs55aa, exact partition sizes, root/data mounted ext4rw and switch_root at7.878653s. Four CPUs,954376KiB RAM, no removable block device in the snapshot. No authenticated scratch-write or repeat/stress acceptance yet.

Read-only comparison proves that the original Y2DATA template contains a different public key. The owner explicitly selects ~/.ssh/y2linux_ed25519.pub, forbids reading/copying/packaging the corresponding private key, and confirms that only initial system state exists on Y2DATA. Prepare a corrected data-initialization template/profile; keep the successful BOOTIMG and existing Y2ROOT. No new kernel, DT, transport, console or alternate hardware path is required. Authorization stays in persistent Y2DATA, so ordinary system updates preserve it. This explicit data initialization replaces initial state and lets per-device host keys be generated again; it is never a normal preserving update or OTA action.

Reassessed all coverage rows and phase gates against this owner result, USB/TCP evidence, the completed54-test/ARM/BOOTIMG checks and the current #16/#27–33 snapshot. Internal boot is newly observed; authenticated reads/bounded-write acceptance remains pending. #33 remains ACTIVE; M1/M2 history, narrow M3 audio, M4/M5 not started, M6 planned, deferred reconnect, backup/calibration gaps and application deferral remain unchanged. The next boundary is one manual USRDATA-only initialization, then SSH using the owner's existing identity.

## Stock address compatibility correction entry — 2026-09-13

Entry revision `d7ee4f2`. The owner's corrected readback completed at 21:10:43 CEST: all six samples match, including Storage05's BOOTIMG control, the complete stock MBR/EBRs and both flashed ext4 identity prefixes. [Evidence and limits](https://github.com/schulzcode/y2linux/blob/HEAD/docs/hardware-evidence/2026-09-13-storage05-owner/readback-corrected-analysis.json). The independently retained actual FM kernel binary, unlike the public donor source previously reviewed, adds `(0x1400000 - other_hardware_capacity)/512` to user-area block commands. DA reports 0x880000 bytes of other hardware areas, so the missing translation is 23552 sectors, with a 15203328-sector stock disk view. [Source proof and production correction](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fstorage06-addressing-correction.md). This supersedes the missing-sector-evidence blocker and the assumption that the public donor's zero offset describes this device. Tables must not be repaired.

Reassessed every coverage row against the new readback, actual stock binary, Storage05 ACM/failure photo, historical DEV-02/AUDIO-02, current owner scope and all eight open GitHub issues (#16/#27–33, read again today). Physical internal boot remains failed; no capability is promoted from offline evidence. #33 and milestone 3 already say ACTIVE/manual acceptance pending; no GitHub status change is needed. M1/M2 historical core success, narrow M3 44.1-kHz audio, deferred reconnect, backup/calibration gaps, M4/M5 not started, M6 planned and application deferral retain their classifications and gates.

The owner-authorized integrated production pass now has concrete evidence for one corrected BOOTIMG: restore the stock logical-to-native address translation and visible capacity, enforce the same logical write spans before translation, preserve real EXT_CSD bytes, and reuse the installed root/data images. No DT, hardware/memory scope, separate diagnostic path, table write or next-phase activation. The next blocker is validation of that correction, followed by one owner manual BOOTIMG-only flash/no-SD boot; hardware acceptance remains pending.

## Storage05 readback observation update — 2026-09-13

The owner completed the prepared 13824-byte batch at 21:00:03 CEST. The [retained result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-13-storage05-owner%2FREADME.md) shows that the assistant supplied physical offsets to a tool path operating in legacy global DA mode (`NUTL_ADDR_LOGICAL`, `EMMC_PART_UNKNOWN=0`). All six intended-prefix checks fail; the supposed Y2ROOT prefix exactly matches stock SEC_RO at its global address. The BOOTIMG identity gate fails. This establishes an acquisition-coordinate error, not intended table corruption or a Linux offset defect. Current internal boot is still failed and ext4 contents on the device remain unqualified.

The next smallest blocker is the same six samples at the [corrected addresses for the observed mode](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fstorage05-readback.md). Original bytes and logs are retained privately. No firmware build, source/DT change, assistant device operation, GUI change, table repair, scope change or milestone transition occurred. #33 stays ACTIVE and later gates are unchanged. This is an observation update, not new hardware or repair authorization.

## Storage05 ACM observation update — 2026-09-13

Owner-established host access now permits [Storage05 LOG1 capture](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-13-storage05-owner%2FREADME.md). 578653 bytes retain contiguous kernel sequences 0–2735. The production eMMC host reports sector addressing, 15269888 sectors and PART_CONFIG=0x48 (user-area access), then CMD18 sector 0/signature0000 with successful SBC/R1. No eMMC guard rejection or reported transport error occurs in this interval; rescue fails at 40.853244 seconds. Internal-root/write acceptance stays failed; physical MBR contents are still unverified. This supersedes host-absence/access-pending statements below.

Existing LOG1 cannot supply raw sectors. The already identified independent read-only evidence boundary is now a concrete [six-sample SPFT Readback plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fstorage05-readback.md), 13824 bytes including a known BOOTIMG address control and ext4 identity samples. It is prepared only. No readback, firmware build, physical assistant block write, reboot, flash, table repair, architecture change or milestone transition occurred. All coverage classifications, #33 ACTIVE and later gates remain unchanged. This is an observation update, not new hardware or repair authorization.

## Storage05 owner result boundary — 2026-09-13

The [owner's Storage05 photo](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-13-storage05-owner%2FREADME.md) arrived after building the single candidate and supersedes the pending-flash boundary below. Reassessed all coverage rows against it: CMD18 sector0 still returns signature0000 with4096 reported bytes, SBC8/00000900 and R1=00000900; normal internal root/data boot fails. Software SBC sequencing alone did not correct the physical problem. No metadata corruption, on-device ext4 integrity or whole-image readback is established. No physical status is promoted.

Source/ARM defects and offline results stand, with their limits retained. #33 and its existing GitHub status remain ACTIVE; every later gate is unchanged. The next smallest blocker is independent read-only sector evidence, with address semantics checked against a known-content control. Host currently has no Y2 USB/ACM/network device; the owner was asked to connect the running rescue for existing LOG1 logs. This does not authorize table repairs or a speculative second candidate. No further firmware build, physical assistant write or phase activation.

## Storage05 manual BOOTIMG boundary — 2026-09-13

Reassessed every coverage row against the same owner-observed Storage04 ACM capture, retained working SD AUDIO-02, current owner scope and open #16/#27–33. No newer physical result exists. The single [Storage05 production candidate](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-production-v1-r5-deployment.md) is built from `5401007791dc2d915c95baac31e91fd062c8edc0`. Source/ARM execution reproduces broken one-block CMD25 encoding, falsely successful DMA fault handling and the fatal rescue `set -i`. The exact physical cause of sector-zero `0000` remains unproved; neither table corruption nor an AutoCMD23 silicon defect is established. Explicit software SBC, corrected error handling and the valid exec handover are the integrated production correction, awaiting hardware acceptance.

52 regression tests, actual ARM ABI/shell checks, kernel/module/archive/layout validation, ext4 identity/integrity and BOOTIMG manifest/bounds/hash checks pass. Eight isolated package mutation cases are refused. The 71-node hardware DT and reservations match Storage04 except calculated initrd-end; kernel configuration differs only in LOCALVERSION. Exact stock MBR/EBR geometry, root/data bytes, runtime write spans, module ownership and y2-platform-v1 stay unchanged. No root/data build, new diagnostic firmware, physical assistant write or SPFT operation occurred. Unchanged ROM/recovery provenance was not repeated.

#33/milestone 3 stays ACTIVE, as already recorded on GitHub; no status update or new epic is needed. Native internal read/write and no-SD Buildroot acceptance are still pending. M1/M2 historical core results, narrow M3 44.1-kHz audio and every later power/radio/GPU/reconnect/stability/application gate retain their status. The next boundary is one owner manual BOOTIMG-only flash and one no-SD boot. Fallback restores the observed Storage04 rescue/ACM, not a working internal root. Stop here; no further build or phase activation follows this documentation audit.

## Integrated production MMC correction entry — 2026-09-13

Owner authorizes one production fix pass and one candidate, stopping before a manual flash. Entry source is `37e4a3f` plus the retained live-evidence/build-input changes already in the workspace. Reassessed every coverage row below against the [Storage04 ACM capture](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-13-storage04-live%2FREADME.md), the last working SD-backed AUDIO-02, current source, and open GitHub issues #16/#27–33 (read again today). #33/milestone 3 remains ACTIVE; the GitHub status already matches. M1/M2 historical successes and M3's narrow 44.1-kHz result stand; all power/radio/GPU/reconnect/stability/application gates remain unchanged.

Storage04 identifies 15269888 sectors, four CPUs and 954380 KiB RAM, but returns sector-zero signature `0000`, exports no partitions and stays in rescue. This is not proof of erased tables. ACM is absent at this pass's host inspection; its existing LOG1 protocol provides logs, not arbitrary remote block reads. No new physical write or new diagnostic firmware is authorized or performed.

The next boundary is a BOOTIMG-only production correction: audit the actual MMC request/response/DMA path, retain normal bounded root/data writes and all protected regions, execute the stock parser against the retained tables, and check the existing ext4 identities and internal-only rescue handover. Preserve layout 1, the exact stock ANDROID/USRDATA geometry, existing root/data bytes, DT hardware, module ownership and y2-platform-v1. No parser replacement or MBR/EBR rewrite without evidence. Offline tests must distinguish reproduced source defects from the still-unverified physical cause. Re-audit at the manual-candidate boundary.

## Storage04 live observation — 2026-09-13

Read-only [hardware inspection](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-13-storage04-live%2FREADME.md) after the owner's r4 flash establishes Linux storage04, CPUs 0–3, MemTotal 954380 KiB, initial USB composite enumeration and bounded ACM LOG1 reception. Internal MMC is detected at 15269888 sectors, but no partitions are exported. The driver observes sector-zero signature `0000`; rescue explicitly reports missing/invalid internal root/data at 41.163161 seconds. Normal Buildroot/SSH and internal-root/data acceptance remain blocked. Actual table bytes/addressing are not independently read back; do not infer physical erasure or authorize table repair from this signature alone. USB Ethernet and reconnect remain unqualified.

Owner attributes the earlier off-state failure to an empty battery. Available telemetry reports USB ONLINE only; no battery voltage or charging measurement. Charging management remains absent. Storage #33 remains ACTIVE and later gates remain unchanged. This is an observation update, not a milestone-boundary audit, scope expansion, implementation authorization or M4 activation. It supersedes older pending-flash/no-USB statements for the observed Storage04 boot.

## Single production platform correction audit — 2026-09-13

Owner manual Storage03 flash completed, but the newest rescue photograph shows missing internal Y2ROOT/Y2DATA, no partition rows, USB preflight -19, zero polls, and recovery written=0. This supersedes the pending-flash entry below. Linux and rescue/display run; normal internal Buildroot and USB are not qualified. Cable-dependent/off-state response was reported before Storage03 too. Battery voltage is unknown; Y2Linux has no implemented/qualified charging manager.

Rechecked the coverage matrix against this result, DIAG01, Storage02, and retained AUDIO-02 results. Storage #33 remains ACTIVE. M1/M2 and clean S16/44.1-kHz audio stand as historical physical results; 48 kHz, repeat/LR, USB reconnect, stability, power and radios retain their gaps. No M4/M5/application activation or closure.

The owner explicitly authorizes replacing parallel bring-up hardware modes with one production platform. Active drivers, DT and root resolver must be shared by normal/rescue/diagnostic userspace. Preserve permanent hardware support and bounded write protection; remove identity-only MMC and unplugged USB semantics. Execute the upstream partition parser against retained stock metadata before considering any compatibility change. Do not rewrite tables or infer current raw-media contents from factory files. Instrument failures through production interfaces rather than another diagnostic firmware. Keep layout/data schema 1, OTA architecture and protected boundaries unchanged. Build a uniquely named successor to the already-flashed Storage03, validate the integrated package, and stop for manual owner flashing. BOOTIMG will own the matching DRM module and stage it in RAM for normal /lib/modules access. The rootfs gains only platform startup/status tools, removing the current exact-kernel module dependency from future rootfs updates. This changes packaging ownership, not the DRM driver or storage geometry; validate module ABI, archive, handover and release contracts. No physical assistant writes or SPFT execution.

## Storage03 complete manual boundary — 2026-09-13

The [complete Storage03 package](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-production-v1-r3-deployment.md) is built from 4845860 and passes 33 regression tests plus a linked ARM USB test, ARM userspace/reader/filesystem checks and full image/layout/package validation. Partition layout 1, data schema 1 and root/data runtime write ranges are retained. No further hardware evidence is available; this remains a correction candidate, not physical acceptance. The truncated rejected MMC command and off-state power entry cause remain unproven. No protected/table writes, physical assistant operation, OTA/player work, M4/M5 activation or milestone closure occurred. Storage remains ACTIVE and stops for owner manual SPFT Download Only operation.

## Storage03 correction scope — 2026-09-13

Latest owner DIAG01 photos confirm internal MMC, nonremovable, 15269888 sectors, no exported partitions, rejected storage commands, and USB PREFLIGHT -19 with zero polls and initial CHRDET=007b. The display truncates the command/argument; no specific rejected opcode is established. Owner reports cable-dependent power entry and apparent SD-dependent progress, and cannot provide more device data.

Correct the production storage request boundary and cable-present PHY startup; keep stock loader/table/calibration untouched and the same root/data write ranges. Quiet expected empty-slot console traffic and retain useful rescue status. This is authorized production correction, not M4 power/charging qualification or a new full USB milestone. No evidence yet attributes off-state power entry to a specific image; do not claim a software or physical fix without acceptance. Build a complete three-payload candidate with targeted request/PHY fault tests and full production package validation. Owner remains the only physical writer. Storage stays ACTIVE; later milestones and M3 qualification remain unchanged.

## DIAG01 manual observation boundary — 2026-09-13

The [BOOTIMG-only diagnostic](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-storage-diag-01-deployment.md) passed seven targeted tests and ARM/newc/DT/D08/BOOTIMG/selection/hash checks. The exact Storage02 kernel/module and all hardware/write policies are unchanged. Owner photos establish failed internal-root discovery and Linux display; host still has no Linux USB capture. Hardware coverage and later gates remain as in the preceding audit; no new root/USB success is established by offline tests. Storage stays ACTIVE and pauses at the owner manual diagnostic flash boundary. No assistant physical write or SPFT execution. Do not start later milestones.

## Storage02 diagnostic BOOTIMG preparation — 2026-09-13

A later owner startup/USB attachment still yields no Linux USB enumeration. The established unplugged-start sequence alone has not restored observation; its actual device-side USB status is unknown. Repeated button/cable trials are not useful without additional evidence. The rescue photo confirms failed internal root/data discovery, not its cause.

Prepare a bounded BOOTIMG-only diagnostic with the exact Storage02 kernel, module, controller configuration and command guard. Replace only rescue PID1 with an unmounted-filesystem observation loop and reduce console verbosity so empty removable-slot warnings cannot bury status. Display cached USB diagnostics, internal block geometry, approved root/data signatures and relevant driver logs. No root/data rewrite, filesystem repair, new hardware controls, changed write allowlist, OTA implementation or physical assistant operation. Owner flashes.

Storage stays ACTIVE; no internal-root/USB acceptance or milestone closure. M3 physical results and later power/radio/GPU/reconnect/stability/app gates remain unchanged. Targeted new reader/ARM/shell/DT/newc/D08/BOOTIMG/selection checks are required before the manual diagnostic boundary. No repeated ROM provenance or M1/M2/M3 bring-up is justified.

## Storage02 rescue failure observation — 2026-09-13

Latest owner photos establish Linux display with no SD, then rescue's aggregate missing/invalid internal root/data failure with SD present. Full internal-root boot has failed this attempt; recovery PID1 remains alive. USB remains unobserved. Source review recovers the existing boot-unplugged / attach-after-startup contract and corrects the assistant's incompatible cable-present startup instructions. See [rescue evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-13-storage02-owner-flash%2Frescue-console.md). No milestone closure or new hardware scope; storage remains active and every later milestone retains its prior gate. Next work is read-only ACM observation.

## Storage02 owner transfer result — 2026-09-13

[New physical/operator evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-13-storage02-owner-flash%2FREADME.md): SPFT Download Only transfer completed successfully. Owner reports response after holding Power + Volume Up following a black start. No SD and connected USB are confirmed. Resulting boot stage is unspecified; host sees brief preloader appearances but no Linux USB/ACM/Ethernet. This qualifies the raw transport past its earlier failure, not internal boot or protected-byte integrity. Storage #33 remains ACTIVE; no milestone boundary is crossed. All remaining hardware acceptance and later M4/M5/platform/application gates are unchanged. No code change, build, assistant flash or repeat bring-up is warranted without identifying the current running state. See the handoff for pending observations.

## Storage02 manual retry boundary audit — 2026-09-13

Source/build `c2db4893b79eca25458b6adc318232c80dd99872` produces the [corrected raw-image package and full checklist](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-production-v1-r2-deployment.md). 26 regression tests, ARM ABI/ALSA/shell checks, kernel/DT/BOOTIMG, filesystem, stock geometry, manifest/hash validation and synthetic readback rejection pass. The isolated scatter test now carries the hash-checked original fixture.

Reassessed the coverage matrix against the newer owner failure: BOOTIMG transfer completed; ANDROID failed; USRDATA was not reached. This supersedes any statement below that AUDIO-02 is necessarily still deployed. No native eMMC filesystem, no-SD boot, protected preservation or rescue-negative physical acceptance exists. M3's clean 44.1 kHz and remaining 48 kHz/LR/repeat gaps are unchanged. Power, radios, GPU, USB reconnect, stability and whole-platform gates remain unchanged.

Production Storage v1/#33 remains ACTIVE, awaiting manual retry and physical qualification. All stock boundaries, restoration sources and protected write exclusions remain unchanged; no further source/ROM/recovery audit is justified. Use only out/y2linux-production-v1-r2, including its new BOOTIMG. Before/after readbacks taken only after the failure cannot prove the prior attempt preserved all protected bytes. No assistant flash or physical write was performed. M4/M5 and Y2PlayerNative remain deferred. Stop at this owner operation boundary.

## Storage flash failure / transport correction audit — 2026-09-13

[Owner flash evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-13-storage-flash-failure%2FREADME.md) supersedes the package-ready state below: BOOTIMG transfer checksum passes, ANDROID sparse transfer fails3154, USRDATA not reached. Selected MT6582 DA's parser rejects FILL chunks. First package is withdrawn from retry use. Physical acceptance remains pending; all other hardware coverage rows retain their prior limits. No kernel/root boot success or protected-byte readback is established.

DA physical user capacity differs from historical Android exported capacity; update exact capacity checks for both observed views without reclaiming the tail or changing a partition boundary. Normal write spans remain ANDROID/USRDATA only. Use raw ext4 transport to define every byte without the unsupported sparse path. #33 remains active; M3/M4/M5 and platform/app gates unchanged. This is a bounded failure correction with targeted storage/packaging/BOOTIMG validation, not a repeat of M1/M2/M3 bring-up. Owner alone performs the retry; no assistant flash.

## Production Storage v1 manual-package boundary audit — 2026-09-13

Implementation/build commit `f2ef297a81cc0229155ba5d96f1955bdd230f11d` now yields the [complete manual deployment package/checklist](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-production-v1-deployment.md). Re-reviewed every coverage row against the live AUDIO-02 entry, retained DEV-02/ M3 results, current open issues#16/#27–33, stock table/scatter and recovery sources. 24 regression tests, kernel/DT/BOOTIMG checks, root/data filesystem integrity, manifest/scatter/sparse/hash checks and synthetic readback rejection pass. No new production hardware result or protected-data readback is claimed.

Production Storage / Installation v1 ACTIVE / manual owner operation pending ([#33](https://github.com/SchulzCode/Y2Linux/issues/33), GitHub milestone3). Internal root/data implementation is ready for its first manual test, not closure. M3 remains open with clean44.1kHz;48kHz/LR/repeat remain pending. eMMC is disabled in the currently deployed kernel. Live MemTotal954384KiB/four CPUs/SD/ALSA are confirmed; current no-SD/internal-write/rescue-negative acceptance is absent. All other hardware gaps remain unchanged and tracked. M4 follows storage, then M5, remaining GPU/USB reconnect/stability, final qualification, then native app.

Overwritten-partition FM factory sources are available/hashed; personal Android state and independent recovery retention remain explicit operator choices/steps. Before/after bounded protected/table readbacks and actual address verification belong to the owner manual boundary. The assistant has performed no eMMC write, SPFT operation, kernel deployment, OTA updater or Y2PlayerNative implementation.

## Production Storage v1 activation audit — 2026-09-13

Authoritative current scope, superseding the historical phase order below. Baseline `1583360`; all current open GitHub issues #16 and #27–32 reviewed. Every coverage row below was reassessed against retained DEV-02 and AUDIO-02 physical results, the stock 21-entry map, current source/config and owner direction. [Read-only live entry](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-13-production-entry%2FREADME.md) confirms AUDIO-02, four CPUs, MemTotal954384KiB, SD root and ALSA; eMMC remains disabled in current DT. M1/M2 narrow successes, M3 clean44.1kHz and all power/radio/GPU/USB reconnect gaps remain unchanged. 48kHz, L/R and repeated playback remain pending; M3 stays open.

Production Storage / Installation v1 ACTIVE, inserted after current M3 work and before M4 by explicit owner authorization. Ready for offline implementation and package validation; physical acceptance pending manual owner deployment. [Partition audit and exact classification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fproduction-storage-v1.md) select stock ANDROID for Y2ROOT and USRDATA for Y2DATA. No repartition, protected write, live eMMC write, SPFT execution, updater or native app implementation.

Coverage changes: internal eMMC remains PARTIAL (native identity exists; native block/mount/write not yet qualified); internal rootfs/data, release manifest, rescue, installer/update contract become ACTIVE implementation scope. Buildroot remains canonical. Recovery retains verified stock FM sources for overwritten partitions, with personal Android-data backup and independent retention explicit operator obligations. No full-ROM backup or provenance repeat is imposed. All other matrix statuses and tracked gaps were reviewed and remain unchanged.

Sequence: current M3 acceptance remains open → Production Storage v1/manual no-SD acceptance → M4#30 power → M5#31 radios → remaining platform GPU/lima, USB reconnect#27 and stability#28 → whole-platform qualification → Y2PlayerNative. #32 continues broader lifecycle/security ownership; [storage #33](https://github.com/SchulzCode/Y2Linux/issues/33) tracks this bounded activation. Audit again at package/manual-deployment boundary; do not call installation successful until physical acceptance is retained.

## Current session-close audit — 2026-09-10

This was the authoritative session-close status; dated candidate/activation sections below are historical. Reconciled owner reports, source commits, retained core and AUDIO-02 logs/build metadata, and current GitHub#22–32. Every coverage row was reviewed: the audio, PCM/rootfs tools and phase rows change below; remaining power/radio/GPU/production gaps keep their prior scope. No new phase is activated, closed or implemented tonight. No build, flash or device change in this audit.
  - M1 COMPLETE. Linux6.18 and native boot objectives achieved.
  - M2 core/Buildroot qualified for progression. #22–26 confirmed closed;

four CPUs, bounded RAM pass, writable SD/SSH, display/input and buses remain proven. #27 reconnect stays open/deferred under#28. Initial ACM/ECM/SSH and owner startup/restart recovery work; do not label that cable reconnect success.
  - M3 ACTIVE / NEAR COMPLETION. AUDIO-02 `8f93e44` contains startup fix

`137b3f2`, is owner-deployed and has clean S16 stereo44.1kHz headphones. 3.13s/130IRQs/advancing ALSA pointers and owner "perfect, no clicking!" support the fix. Persistent ALSA tools are installed on SD. Remaining small checks: 48kHz, explicit L/R, stop/restart/repeat and associated noise/reset/XRUN checks. Do not redeploy the already validated fix or rediscover AFE/CON3/CS43131/VGP2.
  - M4 NOT STARTED. Next after M3 short qualification and a boundary audit:

battery/charging/thermal/DVFS/idle/suspend/wake/reboot/poweroff.
  - M5 NOT STARTED. Wi-Fi/Bluetooth remains later; no native app starts.

GPU/lima and final reusable-platform qualification still precede Y2PlayerNative.

DEV-02 measured MemTotal954660KiB; AUDIO-01 measured954384KiB with its larger kernel. Do not turn either into954MiB or invent a fresh AUDIO-02 /proc/meminfo measurement: AUDIO-02 retains the same bank/reservations and comparable boot memory log, while this closeout performs no device inventory. Physical bank is 992MiB; exclusions leave about951MiB before kernel/page metadata reservations.

[Current physical audio result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm3-audio-01-live-result.md) · [Core qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md) · [AUDIO-02 qualification procedure](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-m3-audio-02-deployment.md).

Native24/32-bit and higher rates are not implemented.32-bit I2S slots carry16-bit PCM. These are later enhancements; amp/speaker identity/output, jack and precision clock checks remain separately tracked under#29, not grounds to reopen the basic headphone proof. Before M3 core closure explicitly retain those subpath gaps and re-audit before M4; clean one-run audio alone is not full milestone completion.

## M3-AUDIO-01 manual-deployment boundary — 2026-09-10

[Integrated result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-m3-audio-01-result.md) now passes offline build, thirteen targeted tests, resolved audio/rail DT, expanded RAM/BOOTIMG and rootfs checks. Reconciled every coverage row against the same physical DEV-02 baseline and owner authorization: no new audio hardware result exists. Core acceptance stands, #27/#28 reconnect remains deferred, #29 M3 stays active/open; M4/M5/GPU/final-platform gates and Y2PlayerNative deferral remain unchanged. The owner next updates removable SD content and manually flashes BOOTIMG only. No assistant flash/reboot, internal-storage write or repeat M2 pass occurred.

## M3 activation audit — 2026-09-10

The owner explicitly authorizes one integrated native-audio implementation/build and manual BOOTIMG deployment, using physical DEV-02 as the baseline (checkpoint `d76e57f`). This supersedes the reconnect prerequisite below. M2 core/Buildroot is substantially qualified; #27 and #28 retain USB reconnect for later whole-platform qualification. Do not repeat reconnect experiments or reopen satisfied #22–26.

Reconciled the coverage matrix and current open issue snapshot with the retained [physical pass](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md) and a narrow SSH entry check. Four CPUs, 954660 KiB MemTotal, bounded 256 MiB RAM pass, writable SD Buildroot, protected eMMC, initial SSH/ECM/ACM, visible display, wheel/buttons and PMIC/core buses retain their physical acceptance. Audio remains UNTESTED; VGP2's live selector is 2.5 V with no consumer and must be constrained to 1.8 V before DAC operation. No sound card exists in DEV-02. No new power/radio/GPU acceptance exists.

M3 ACTIVE (#29): ALSA/ASoC DL1 DMA/IRQ -> second I2S CON3 -> upstream CS43131, regulator-owned power and controlled headphone playback. Speaker identity/routing, jack reporting and higher rates remain separately qualified subpaths. One clean kernel build, one audio-equipped Buildroot build, relevant static/DMA/config/DT checks and current layout/BOOTIMG validation. Stop for owner BOOTIMG-only flash; no internal storage, loader, calibration or partition writes. M3 remains open until real clean headphone playback, repeated start/stop and rate tests succeed.

M4 power, M5 connectivity, GPU/lima and final whole-system qualification remain subsequent platform gates. Y2PlayerNative remains deferred. Unchanged provenance, recovery research and M2 qualification are not repeated.

## DEV-02 live qualification boundary audit — 2026-09-10

Owner-authorized complete live pass on physical Linux `6.18.0-y2linux-dev02`, source checkpoint `a34a360` plus preserved DEV-02 working changes. Live DT hash matches DEV-02; full flashed BOOTIMG was not read back. Reassessed every coverage row, current #16/#22–32, retained baseline, raw evdev, RAM tests, DRM/sysfs and host disconnect evidence. [Complete report and evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-dev02-live-qualification.md).

Buildroot PID1 runs on writable removable Y2ROOT, four CPUs online, MemTotal 954660 KiB. The completed 256 MiB allocator test passes; a separate exhaustive run was capped at 600 seconds without observed memory errors. All eight buttons and both wheel directions produce evdev events; wheel/I2C IRQs agree and no transport timeout remains. Owner confirms native display pattern after standard fb0 unblank. Internal eMMC is disabled and unexposed. PMIC/core buses, initial ACM enumeration, key-authenticated SSH and USB Ethernet work.

USB reconnect FAILED. The host sees removal, then no enumeration after owner reconnect. The owner reports USB works only after restarting; no post-reconnect uptime/continuity measurement exists. Do not perform the second cycle or close M2. The generic core/Buildroot foundation is substantially qualified, with the real #27/#28 reconnect blocker replacing the old research sequence. A later shared-framebuffer checksum mismatch is corrected by hiding/restoring the cursor; visible display acceptance and independent allocator-test success stand.

Safe runtime/module/config changes are represented in canonical Buildroot/host sources and retained readbacks. Missing evtest/modetest and longer syslog records are configured for the next userspace build, without triggering a rebuild. Close satisfied #22–26 narrow slices; retain long-run/DMA, full power, routing, production and final platform concerns under #29–32. Optional physical UART #16 remains separate, not an M2 closure prerequisite. No new kernel/BOOTIMG, flash, assistant-initiated reboot, internal storage access or unchanged provenance qualification occurred.

M1 COMPLETE; M2 ACTIVE solely around remaining real qualification/fixes, chiefly USB re-entry. M3 audio is the next platform phase once that foundation is usable; M4 full power and M5 connectivity follow with shared dependencies. GPU/lima and final whole-system qualification precede Y2PlayerNative under the owner's new explicit platform-first gate. No later hardware phase is activated by this audit. After the failed reconnect the owner restarted the device; SSH returns at33.32s with the old tmpfs token missing, confirming a new boot. Runtime fixes persist and actual ACM capture now works after the host rule. A bounded SD recorder is installed/tested so a future failure log can survive loss of USB. A USB-focused DEV-03 requires device-side failure evidence and a justified change; host absence alone does not identify which guard/callback failed.

## DEV-02 root handoff / wheel correction audit — 2026-09-10

Owner's new photograph confirms SD partition mmcblk0p1, ext4 recovery, exact Y2ROOT UUID, writable remount and handoff attempt. PID1 then dies by SIGILL (exitcode4) at23.723s. Visible fbcon remains positive. SD block/filesystem access now has physical evidence; Buildroot init/SSH do not. The raw fault PC is absent. All other coverage rows retain their latest evidence and open gaps; no milestone closes, M2 stays active. No loader/partition/internal-eMMC write or new hardware subsystem is authorized. Preserve the observed RAM/display/SD configuration.

DEV-02 combines standard ARM userspace Thumb/signal and kuser compatibility, framebuffer device-node availability, userspace fault reporting/preflight, and an evidence-backed MT6582 I2C combined-message correction. v6.18 selects WRRD only with auto_restart, but MT6582 uses the older non-auto-restart compatible; DEV-01 logs op1/transactions2 with only one byte of completed TX DMA. Restore combined WRRD for this exact compatible and test the controller-level selection, without changing APT32F packet framing or adding retries.

Use one new kernel build, existing pinned Buildroot binaries, targeted regression checks and fresh actual layout/BOOTIMG validation. Keep the already written SD rootfs usable; the new DRM module loads from rescue before switching. A later SSH module-index refresh can bring the SD module directory to the new kernel. Stop at owner BOOTIMG-only flashing, then collect all independent failures again.

## DEV-01 retained rescue/RAM/display checkpoint — 2026-09-10

[Capture-02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-development-hardware-result.md) now retains all 704 kernel records, visible-console supporting scanout/vblank state, four CPUs, MemTotal954668KiB and HighTotal228352KiB. RAM/HIGHMEM visibility is physically observed; stress and full DMA containment remain open. Wheel remains regressed with ten I2C timeouts; the test-pattern tool cannot open/query fb0. Rescue fallback is confirmed without Y2ROOT; SD boot/ECM traffic/SSH/reconnect remain unqualified. M2 ACTIVE/exit incomplete, later gates unchanged. Transfer the existing rootfs to the owner's Mac, identify its removable card, then prepare exact manual commands. No hardware scope expansion or new build is needed for this transfer.

## DEV-01 owner-visible console update — 2026-09-10

The owner reports a visible Linux console after manually flashing DEV-01; SD rootfs is not installed. Host USB descriptors independently identify Linux 6.18.0-y2linux-dev01 and composite ACM+ECM enumeration. This is positive visible output, superseding the prior black-screen outcome for this boot; display remains PARTIAL pending broader qualification. [Evidence and host access limitation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fy2linux-development-hardware-result.md).

No new RAM, wheel, SD-root, network, SSH or reconnect success is inferred. M1 COMPLETE; M2 ACTIVE/exit incomplete, later phases unchanged. Continue the already authorized removable-SD preparation after exact host device identification; no assistant write or guessed disk target. The existing DEV-01 BOOTIMG can remain.

## Y2LINUX-DEV-01 manual-deployment boundary audit — 2026-09-10

Offline implementation and the combined candidate are now built and validated: [DEV-01 result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-dev-01-result.md), [memory reconciliation](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fdevelopment-memory.md). Rechecked every hardware coverage row against the retained BASELINE-03 capture and owner observations. No newer physical capture exists, so **no physical classification or milestone exit is promoted**. M1 COMPLETE; M2 ACTIVE/exit incomplete; audio/application, radio, product PM/security and later milestones retain their gaps and owners.

The owner-specified ED25519 public key is packaged; no host private key was accessed. Kernel/module, large-memory DT, rescue archive, actual pinned Buildroot, ext4/tar content and key policy pass offline validation. Rootfs/ECM/SSH now have built implementations; their physical state remains untested. SD writes and BOOTIMG flashing remain owner-only. Next action is one manual deployment and combined visible-display, wheel, RAM, SD, persistent USB/network/SSH collection. No unchanged ROM/recovery provenance or duplicate clean build was repeated.

## Y2LINUX-DEV-01 integration scope audit — 2026-09-10

Fresh-session local baseline 2efcdc1, clean main; current open issues #16, #22–32 agree with the local BASELINE-03 checkpoint. Reviewed all coverage rows, retained capture-02 (102314 bytes, all 606 kernel records, 180 seconds), source and artifact metadata. No new hardware success is claimed. Owner confirms an earlier wheel-working integrated baseline; its exact artifact identity is not established in the retained canonical captures. Treat current eight -110 reads as an integration regression and preserve register-zero repeated-start framing.

The owner now explicitly authorizes one integrated development candidate: post-modeset display fixes/diagnostics at 480x360; wheel transport correction; large RAM with explicit reservations and HIGHMEM; pinned ARMv7 hard-float glibc Buildroot; removable-SD ext4 LABEL=Y2ROOT; rescue initramfs; persistent ACM+ECM; key-only Dropbear. This supersedes D08 as the final target, identity-only SD and temporary USB disconnect deadlines. Internal eMMC remains protected; no assistant flash, SD write, loader/partition/calibration/Android write is authorized.

Every physical coverage classification below remains unchanged. Display remains PARTIAL with failed visible output despite successful DRM initialization. Wheel remains PARTIAL with working historical owner observation and current transport regression. RAM, removable SD and USB are PARTIAL; Buildroot/rootfs/SSH are PLANNED pending implementation/build and then physical qualification. SMP and buttons retain their narrow successes. All power/thermal, audio, radio, recovery, production security, time/entropy and application gaps retain their existing owners and limitations. M1 COMPLETE; M2 ACTIVE/exit incomplete; M3/application and later product phases are not activated. Existing #22–28 own this work; #30 retains sustained-workload/power qualification and #32 production policy.

Proceed offline together, preserving attribution/identity and unchanged donor, ROM and recovery provenance. One clean kernel tree, one pinned Buildroot build, changed-subsystem tests and full new memory/layout/BOOTIMG/rootfs validation. Record exact artifact hashes and remaining physical tests. Stop for owner manual SD identification/write and BOOTIMG-only deployment. Permanent USB observation is a development capability, not sustained power/thermal qualification. Re-audit before milestone closure using the subsequently collected real hardware results.

## BASELINE-03 hardware evidence update — 2026-09-10

Owner capture-02 restores complete kernel/PID1 observation for180seconds, including successful live-PHY adoption, DSI park, cold Linux PHY initialization, DRM/fb0 registration and module return0. The owner still sees black: visible display acceptance remains failed. Four CPUs and existing navigation/volume/power input operate. Wheel EINT55 now fires, but eight I2C reads time out with no controller completion IRQ; transport debugging replaces the previous unobserved-wheel gap. [Retained result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-baseline-hardware-result.md%23latest-baseline-03-logs-the-display-handoff-screen-remains-black&anchor=latest-baseline-03-logs-the-display-handoff-screen-remains-black).

Next combined source iteration: diagnose actual display output and wheel I2C completion, include standard runtime state/failure diagnostics and repair snapshot line framing. Preserve the working single USB writer. No guessed rate/rail/panel changes, repeated per-register images or milestone promotion. M1 COMPLETE; M2 ACTIVE, exit incomplete. D08, storage/PMIC firewalls, owner300s limit and later milestone exclusions remain. This is an evidence/documentation update, not a new build, hardware scope authorization or five-minute/reconnect qualification.

## BASELINE-03 observation and packaging review — 2026-09-10

BASELINE-02 owner reports grey/black after LK. The retained 180-second capture identifies baseline2 at high-speed ACM, sends LOG1, but receives zero bytes (exit2, no protocol header). No kernel/PID1 execution point or display failure instruction is established. This is a regression of observation, not display success. All newly tested BASELINE-01 results remain historical, not silently revalidated for BASELINE-02.

Same M2 hardware scope, revised initramfs packaging/startup: compile the MediaTek DRM aggregate as the sole loadable module, with required DRM helpers built in. Package the exact module with PID1 in the existing bounded RAM-only initramfs. Start it once through finit_module in a separate child after LOG1 is active; PID1 must never wait synchronously for display probing. Keep PID1 on CPU0 and the load child on previously observed CPU1 using normal scheduler affinity; this reduces local CPU starvation, not global bus/lockup risk. Kernel/driver logs still use the unchanged /dev/kmsg-to-CDC relay, without competing USB writers. Repair unpowered DSI host-transfer access and add phase messages. No guessed panel/clock/rail changes or extra per-register image.

Audit module dependencies, ABI/exports and exact initramfs membership, include module bytes in the D08 unpacked-file/layout accounting, test child errors and nonblocking reap, then one clean combined build/package. No second reproducibility build or unchanged ROM/recovery/source-tree hashing. D08, protected partitions, PMIC/storage write firewalls, five-minute owner limit and M3/M4/M5 gates remain. M1 COMPLETE; M2 ACTIVE; stop at BASELINE-03 for manual owner BOOTIMG flash.

## M2 integrated hardware checkpoint — 2026-09-10

[BASELINE-01 physical results](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-baseline-hardware-result.md): two complete initial kernel captures confirm four CPUs, shared PWRAP/MFD/regulator probes, all five navigation channels, both volume keys, PMIC power key through EINT25, and native microSD/eMMC identity. DSI rejects the inherited PLL before handoff; wheel rotation has no captured IRQ/transfer/events. These are partial core results, not M2 closure. M1 COMPLETE, M2 ACTIVE; M3/M4/M5 gates unchanged.

Continue one combined source iteration: repair live-PHY adoption and capture window defaults; retain D08, PMIC/storage write firewalls, USB logging, the 295-second USB deadline and owner 300-second limit. The five-minute disconnect report is consistent with the deadline but not captured in the 45-second files. No memory/rail/production scope expansion or independent per-register flash.

## M2-BASELINE-01 integration authorization — 2026-09-10

Baseline 4dde305 (clean main). The owner explicitly supersedes per-register and per-driver flash gates with one coherent offline Linux 6.18 core integration. Reviewed canonical config/DT/PID1/USB, retained USBACM-03 and D08 evidence, the 36-commit donor and additional history against every coverage row below. No new hardware result exists: M1 COMPLETE, M2 ACTIVE/exit incomplete, M3 gated, M4/M5 deferred. No coverage status is promoted by compiling a driver.

Implemented at entry: CPU0/GIC/GPT, early stopped AP watchdog, guarded LK text, PIO CDC ACM with kernel/PID1 relay, offline USBACM-04 lifecycle and polled navigation GPIOs. CCF/pinctrl/EINT/I2C/wheel/PMIC MFD/regulators/keypad/DRM/MMC/SMP are documentation or donor source only. The two previous offline candidates no longer require separate flashes before the combined baseline.

Integrate evidenced controller contracts together; preserve normal probe errors and deferral. Remove USB's dependence on display ownership and competing PWRAP access. Review RAM in the same pass; retain D08 if the LK heap/live DMA ownership boundary still prevents a defensible larger interval. Storage must enforce no writes at the kernel boundary. No charger policy, audio, radio, GPU applications, rootfs installation, protected partition, loader or calibration changes.

The 60-second experiment limit is superseded only for this candidate by a maximum five-minute owner test from power-on. Proven early AP watchdog stop, Linux/PID1 and USB observation plus retained BOOTIMG recovery justify observing idle core probes longer. This does not qualify thermal/charging policy or permit stress: no CPU load test, charging experiment or automatic reboot. USB/PID1 must remain observable within that interval; early stop on abnormal warmth, repeated faults or lost observation. End with the existing manual BOOTIMG restoration.

One combined source/config/DT review, one clean build (repair errors in that build if necessary), shared-provider tests and final layout/package validation. No duplicate reproducibility build or unchanged ROM/source/recovery audits. Stop at the resulting BOOTIMG for the owner's flash; classify the complete live log and fix independent failures together in the next source iteration. M2 closure still requires the standing strict milestone audit and real exit evidence.

## Additional reverse-engineering evidence — 2026-09-10

Baseline e4a0a81. Reviewed the blueprint, current issues #1–32 (open #16/#22–32), every coverage row, canonical source and retained physical results against the [additional research](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md). External f96d4c7 pins our existing donor 53fb57bb. Missing private captures and stale historical statements are identified in the research matrix.

Every hardware classification remains unchanged. USBACM-03 remains the 11,754-byte kernel/PID1 capture. USBACM-04 and M2-INPUT-01 have offline validation only; host inventory found no Y2 attached. M1 stays complete, M2 active/exit incomplete, M3 gated, M4/M5 deferred beyond shared M2 prerequisites. D08, the rootfs/application plan, recovery rules and older-board FM exclusion remain. No new boot, build, flash or unchanged provenance requalification occurred.

The implementation strategy advances where evidence is stronger:
  - #24/#28: validate the navigation candidate, then adapt EINT/I2C/AP-DMA/wheel

and keypad by dependency. Upstream 6.18 already fixes the donor's PMIC single-key null-pointer problem.
  - #23/#28: one WACS2 owner shared with USB; distinguish the wrapper IRQ storm

from PMIC EINT25. Derive CCF/pin/rail contracts; absent PLL probe files cannot validate approximate donor rates.
  - #25: use the later 480×360 correction, cold PHY/reset findings and live-pipeline

failure history. v6.18 already protects the OVL address from PITCH_MSB writes; port remaining variant differences instead of redundant 6.12 fixes.
  - #22 still needs loader/DMA/lowmem ownership despite main-bank agreement.

The modem/HYP collision reinforces high exclusions. #26 can validate reported MSDC operation after clocks/pins/rails/DMA; there is no local native read result.
  - #29 retains CON3/VGP2-brownout evidence for M3; #30 retains separate charger/AP

watchdogs and unresolved thermal/DVFS/suspend limits. #31 retains cold radio calibration and failed EDR experiments; #32 retains address-space/recovery pitfalls. No later phase is activated.

Execution remains navigation/USB evidence → corrected shared providers and useful RAM reconciliation → wheel/power, display and storage/rootfs → real M2 stability and exit audit. The research report specifies the next provider contract. Existing issues absorb the findings; no new issue/milestone fan-out. Physical flashes remain owner-performed; protected partitions/calibration are untouched.

## M2 activation audit — 2026-09-09

### Donor adoption and GPIO input scope — baseline 8ebc800

2026-09-09. The owner authorizes donor-assisted Linux 6.18 implementation, build/test/Git/GitHub and live host logs, with manual owner BOOTIMG flashes. Reviewed the complete 364-file/36-commit donor inventory, local blueprint M2/M3 and later gates, current GitHub issues #1–32, canonical config/DT/source and retained stock/RAM/Linux evidence. [Subsystem audit and dependencies](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fdonor-audit.md). No new physical result: USBACM-03 remains the 11,754-byte kernel/PID1 success; USBACM-04 robustness remains pending. Host USB is accessible outside the sandbox; no Y2 was attached at this inspection. Identity/recovery/provenance is unchanged.

Every coverage row below was reconsidered. Hardware status stays unchanged except that other navigation buttons now have a concrete PLANNED evdev slice; source availability does not promote hardware readiness. The former "common providers not established" blocker now has substantial donor contracts to correct/forward-port. SMP, CCF, EINT, PMIC, input, display, storage, audio, radio and haptic source availability is detailed in the separate reuse matrix. Thermal/DVFS/idle, full memory/DMA ownership and production/recovery gaps remain. FM reception is inapplicable to the owner's older board; retain donor knowledge only for other revisions. M1 complete, M2 active/exit blocked, M3/app deferred. All M2 rootfs/display/input/storage/observation/battery criteria still apply.

Supersede the rigid #27→#22→#23→#24→#25→#26 order. Keep USB robustness open and preserve both USB candidates; use GPIO navigation→upstream gpio-keys-polled→ evdev→USB as the first coherent slice under #24/#28. D08 stays unchanged. The five inherited input lines can be sampled without EINT, I2C DMA, supply, clock or pinmux writes. Refuse output-configured lines. Poll at 20 ms through the input core; bounded userspace evdev capture must preserve USB/heartbeat. This is real input integration, not a hardware-success claim. General pinctrl, EINT, wheel rotation, keypad and PMIC power key remain subsequent dependencies.

Next combine corrected CCF/PWRAP/GPIO/EINT/I2C foundations by consumer dependency; reconcile a useful large RAM expansion under #22 instead of arbitrary tiny increments. DRM/panel/backlight and removable storage/rootfs follow their actual rail/clock/DMA requirements. Retain donor AFE/codec knowledge for M3, with radio work deferred. Planning-only wording in old issue bodies is superseded only by the owner's explicit implementation scope; it never authorizes device flashes.

New input subsystem qualification: one clean build, full existing offline suite, GPIO range/refusal and ARM evdev/relay cases, linked access review, resolved config/DT and D08/BOOTIMG checks. No memory architecture change or repeated ROM, source or recovery provenance. Stop at the validated candidate for the owner's physical test. Source/license attribution remains with each reused piece; donorSource stays immutable and outside versioned implementation.

[M2-INPUT-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-input-01-result.md) is now offline validated: one clean kernel build, corrected PID1/package after a caught parser defect, 29 build-suite and 12 observation tests, emitted GPIO loads/refusal review and current D08/BOOTIMG checks. Candidate 1,204,224 bytes, SHA-256 `05c6f33d7fadb75c9bc5d8cc4a23aed1a5dcc79cf6b4fe735ce9006906290d37`. Stop at this owner-flash boundary; no input/USB hardware classification advances.

### Current scope review — one bounded USB reconnect, baseline 7ee780a

2026-09-09. The owner explicitly authorizes completing #27 robustness before #22 → #23 → #24 → #25 → #26 → M2 boot/stability qualification and closure audit. Reviewed the current repository, open #16/#22–#32, #27 acceptance and #28 epic, the existing blueprint/coverage matrix and USBACM-03 capture/source/build evidence. The successful baseline is now pushed; its 67 retained implementation/test/tool files match the build snapshot. No repeated source/ROM/recovery provenance audit.

Every coverage row below is re-evaluated and retains its classification: narrow kernel/PID1 logging CONFIRMED inside overall USB PARTIAL; boot, RAM, display, power, recovery and later product gaps remain with their existing issue owners. M1 stays complete; M2 active with blocked exit; M3 and application work deferred. No optional exit criterion or D11 experimental limitation becomes a production waiver. The existing backup/calibration and full DMA ownership gaps remain open.

USBACM-03 stops permanently at first detach, so it cannot satisfy the requested reconnect criterion unchanged. Develop USBACM-04 using the already-owned PIO controller: on first sampled CHRDET loss remove SOFTCONN, notify upstream gadget disconnect and restore only the existing saved digital PHY session inputs; retain the controller and PID1 history while unplugged. Permit one restart only after fresh supply/clock, passive digital PHY, zero DMA controls and unchanged mode/trim checks, using the same guarded session writes and upstream controller start. A second detach, any failed guard or the original 50-second deadline is terminal. PID1 heartbeat and the 60-second owner limit remain unchanged.

This is a localized lifecycle extension of the proven subsystem, not new USB, DMA, memory, boot packaging, rail or production ownership. Targeted transition, relay/ARM PID1, host capture, linked and D08/BOOTIMG checks plus one clean build apply. Qualification still needs the physical combined delayed-open/no-reader/ disconnect/offline-heartbeat/reconnect/replay test; do not close #27 from fixtures. The real host sees Y2 at 5-2, ttyACM0, 0525:a4a7 with the USBACM-03 manufacturer; this session lacks tty permissions, independently of sandbox visibility.

[USBACM-04 is now ready for the owner test](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbacm-04-result.md). One clean build, 16 targeted methods and eight host observation/orchestration methods pass; 34 ARM PID1, eight worker and 29 lifecycle/guard scenarios are included. Current D08/BOOTIMG and focused emitted-ARM checks pass. Candidate: 1,161,216 bytes, SHA-256 `ecdce008c34998dce03e1b5dd88b0c78c3015e5865b93d4ba609f6cbf134f365`. No physical robustness run occurred and no capability classification is promoted. Stop at this BOOTIMG for the owner flash/cable test; #27 remains open.

### Previous checkpoint — first kernel/PID1 USB capture succeeds

2026-09-09, USBACM-03 retained candidate/source identity. The owner-run [capture-03](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usbacm-hardware-result.md%23usbacm-03-kernel-and-pid1-capture-confirmed&anchor=usbacm-03-kernel-and-pid1-capture-confirmed) contains 11754 verified bytes over a 45-second reader window: exact LOG1 build header, contiguous kernel sequence 0–77, every PID1 beat 1–43, US:6 RC:0 from beat 4 and increasing IRQs. No relay GAP/ERR or PID1 error appears. The normal reader timeout exits 0. The prior host-permission blocker is resolved for this run; this is the first captured log result, not just enumeration.

Update the USB coverage row to PARTIAL: narrow kernel/PID1 logging is confirmed, while repeatability, late-open/non-reading host, detach/reconnect and stability remain unqualified under #27/#28. All other coverage classifications and owners remain unchanged; no boot/memory/power or M2 exit criterion is promoted by this capture. M1 complete, M2 active/exit blocked, M3/application deferred. This is an evidence review within the existing experiment: no milestone closure, new hardware scope, build or flash. Repeat the standing full audit before activating a different scope or closing the milestone/qualification boundary.

### Previous checkpoint — USBACM-03 enumerates; host capture access blocked

2026-09-09. [Host journal](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usbacm-hardware-result.md%23usbacm-03-host-enumeration-confirmed&anchor=usbacm-03-host-enumeration-confirmed) and owner report confirm high-speed 0525:a4a7, the USBACM-03 kernel identity and CDC ACM ttyACM0. The former capture timeout came from the assistant's isolated `/dev`; an unsandboxed run matches the device but gets EACCES because the host account lacks tty permission. Neither error disproves enumeration. No LOG1 payload was captured. The next step is the same image and script with owner-authorized host access, not a new hardware change or build.

Narrow enumeration is now evidenced. Overall host logging remains BLOCKED on reader access and log-content proof; other coverage statuses and owners remain unchanged. No milestone activation/closure, memory/production scope change or reconnect/boot-repeatability qualification is inferred. M1 complete, M2 active with blocked exit, #23/#27/#28 open, M3/application deferred.

### Previous checkpoint — USBACM-02 sync-only refusal

2026-09-09, `c066d62` plus the retained USBACM-02 source snapshot. The owner reports the attach prompt now appears, followed by an error before attachment. The [new photo](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usbacm-hardware-result.md%23usbacm-02-result&anchor=usbacm-02-result) shows poll 5, US:2 RC:-16, WACS2 `00200001` at entry/failure, valid mask zero, and passing wrapper gates. Init is set, request is clear and FSM is idle; only sync-idle is absent. The snapshot does not establish how long this lasts. No controller registration or enumeration occurred. Wake/clock evidence remains confirmed within the prior narrow scope; USB BLOCKED, boot/memory/power PARTIAL, all other coverage classifications and issue owners unchanged. M1 stays complete, M2 active with blocked exit, M3/application work deferred.

The next localized fix is a bounded, read-only pre-command wait for sync only in M2-USBACM-03. Retained MT6582 definitions identify bit 20 separately from channel FSM/request; vendor `wait_for_sync`/`wait_for_idle_and_sync` explicitly poll this condition. Require init/no-request/FSM-idle on every sample, retain the full existing ready predicate before any command, and stop immediately on stale/active/invalid channel states. Limit each wait to 1000 ten-microsecond delays; no transaction retry, stale acknowledgement, wrapper reset, new register, PMIC write, memory map or packaging scope. This repairs single-sample rejection within the active PWRAP/USB contract; it does not authorize channel recovery or promote hardware readiness. Targeted protocol/fault, worker/ARM PID1, linked access and one clean BOOTIMG/D08 validation apply before the owner test.

[M2-USBACM-03](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbacm-03-result.md) now passes one clean build, 15 targeted methods plus four host-capture methods and linked/D08/package review. The new protocol cases cover sync settling and failure at all four pre-command gates. Image: 1,159,168 bytes, SHA-256 `20c7f01ad97832def704523897fb5ec08cbfacd560558bbd3989b4f4426f734a`. Hardware sync recovery/enumeration remains untested; no capability is promoted.

### Previous checkpoint — USBACM cable-wait poll refusal

2026-09-09, baseline `c066d62`. The owner reports unplugged startup and supplies [one M2-USBACM-01 photo](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usbacm-hardware-result.md): cached power/clock and PHY wake succeed, US:2 RC:-16 with invalid live CHRDET stops the worker before controller registration. BEAT 12 and MemTotal 22096 kB are visible; there is no enumeration/logging success or identified repeatability result. The raw failed WACS2 sample was discarded, so the particular idle-gate cause remains unknown. The earlier CHRDET/wake evidence is retained.

The localized next candidate, M2-USBACM-02, preserves that failed sample and corrects the stale screen heading. No hardware access, guard, memory map, packaging or production scope changes; targeted validation applies. This is an evidence-display repair within the active experiment, not a milestone boundary or authority to recover a busy/stale channel. Coverage classifications and owners remain unchanged: USB BLOCKED, boot/memory/power PARTIAL, M1 complete, M2 exit blocked, M3/application and other input/display/media/thermal gaps deferred to their existing gates. Stop at the validated candidate for owner testing.

[M2-USBACM-02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbacm-02-result.md) now passes one clean build, 15 targeted methods and four host-capture methods, including 33 ARM PID1 paths and real-artifact/D08 checks. Candidate is 1,159,168 bytes, SHA-256 `4ff741513ef842fca28e6fd8cd08829c9c8c9d2e3e160da70552e06166460e20`. It awaits the failed-poll screen or bounded enumeration evidence; no busy-state recovery or new hardware success is claimed.

### Combined USB ownership scope review — baseline d9c2c98

2026-09-09. The owner explicitly replaces the register-by-register handoff with one guarded candidate targeting enumeration and kernel/PID1 logs. USBGUARD-01 remains an untested fallback; there is no new physical result. Reviewed the blueprint M2/exit and later gates, current open #16/#22–#32, this coverage matrix, the CHRDET and PHY-wake reports and current implementation. All capability classifications remain unchanged: M1 complete; M2 active, exit blocked; host USB logging blocked pending implementation and hardware proof. Boot/memory/power remain partial; input, standard display, media/rootfs, thermal/battery and all later-phase gaps retain their existing owners. No milestone criterion waived.

Authorize development of one experimental vertical slice under #23/#27: source-reviewed MT6582 controller/PHY ownership, peripheral-only PIO MUSB, one standard g_serial ACM function and bounded kernel/PID1 log relay. Use the observed passive handoff as a runtime gate, initially booting without USB and requesting attachment only after successful preflight. The unobserved complete connected-start save-current state is not normalized by guessing. Refuse unknown clock/supply/PHY/DMA states and preserve the screen at every stage. Resolve each write/IRQ/FIFO contract from retained FM/LK and pinned Linux/vendor source before implementing it; combine resolved stages within the candidate, not hardware claims.

This is first controller/IRQ/FIFO ownership and requires broader qualification: production guard/fault tests, actual ARM relay/syscall tests, full existing offline suite, linked access review, resolved config/DT and D08/BOOTIMG checks. One clean candidate build, no duplicate reproducibility or unchanged source/ROM/ recovery audit. Keep D08/CPU0, watchdog stop, framebuffer fallback and original loader/partition/calibration boundaries. No USB DMA, host VBUS supply, analog calibration rewrite, M3/audio or application work. Stop at validated BOOTIMG for owner physical test; successful enumeration cannot be promised offline.

[M2-USBACM-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbacm-01-result.md) is now the immediate next owner test: one clean build, full offline suite plus ARM relay/linked syscall and host capture checks, unchanged D08 bounds and valid BOOTIMG. It attempts enumeration and logging in one unplugged-start/late-attach boot. Implementation has advanced; USB hardware status remains BLOCKED pending that evidence. No milestone or capability is promoted from the build. First-detach/reconnect qualification and connected-start recovery remain outstanding; the original #27 criteria stand.

### Previous checkpoint — CHRDET confirmed, connected-start guard refusal

Baseline `de1a6d0`, 2026-09-09. [Three owner photos](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-chrdet-hardware-result.md) show CHRDET 007B/1 with USB attached at startup and 0001/0 without it. PWRAP, clock and initial USB snapshots succeed. The connected boot reaches BEAT 10 but refuses wake before writing (6a=BE, W0, V00/000); no-USB photos show successful wake and BEAT 11/46. Same-boot chronology of the no-USB pair is not explicit. The connected screen's zero wake fields are unread, not hardware values.

Narrow PMIC charger detection advances to CONFIRMED. Broader power/boot/memory remain PARTIAL and host USB logging BLOCKED. Current #22–#32 tracking and the coverage matrix retain their remaining gaps: no input/display/media/rootfs, thermal or later-phase capability advances from these photos. M1 stays complete, M2 active with blocked exit, M3 and Y2PlayerNative deferred; no criterion waived.

The next localized step is [M2-USBGUARD-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-guard-diagnostic.md), preserving the already-captured raw USB state on early guard refusal and marking unread data. Hardware access/guards, 260-byte ABI, D08, DMA, loader, calibration, recovery and packaging policies are unchanged. This is a presentation fix within the active prerequisite, not a new subsystem or milestone boundary. Targeted tests and one clean build with D08/BOOTIMG checks apply. Stop at the candidate for connected-start owner photos before selecting a recovery/session write.

[M2-USBGUARD-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbguard-01-result.md) now passes one clean build, all 15 selected methods (26 ARM PID1 and 49 PHY-wake scenarios), linked probe comparison and D08/BOOTIMG checks. Candidate: 1,097,728 bytes, SHA-256 `e4078583ab53bd7e6388c94a357023fe8a7504ccc5a7499341cf72287ecd19b5`. It awaits the connected-start owner test; no new hardware result is inferred.

### Previous checkpoint — PHY wake confirmed, baseline 305f8f9

The owner-confirmed [same-boot USB-connected pair](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-phy-wake-hardware-result.md) shows BEAT 10→49, IRQ 1134→5463, MemTotal 22208 kB, no reported error, the guarded 6a 04→00 write and unchanged sampled trims. The earlier conflicting pair remains retained with unresolved chronology. Full PHY readiness/session detection is still unproved: POWER20/DEV80 remain after release with the cable attached.

Reconsidered the coverage matrix and current open #22–#32: narrow PHY release advances to CONFIRMED; boot qualification/memory/power remain PARTIAL, USB logging BLOCKED, and input/display/media/rootfs/thermal and later-phase gaps unchanged. No optional criterion waived, M1 reopened or M3 work started. The next localized step is [one PMIC CHRDET status read](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-chrdet-probe.md) through the proven PWRAP transport, addressing only the cable/session prerequisite. It adds no new PMIC/analog/VBUS/MAC/DMA write, changes no memory/packaging policy and uses targeted validation. Stop at the next BOOTIMG for owner test. Existing recovery, stock loader, partition and calibration boundaries remain unchanged.

[M2-CHRDET-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-chrdet-01-result.md) passes one clean build and all 18 selected methods plus linked transaction and D08/BOOTIMG checks. Candidate: 1,097,728 bytes, SHA-256 `e511fb89e45326673183f426a4bdd3b6ca708c25bf3e6ceecfc4a67478aa9660`. It awaits owner test; no physical charger-presence result is claimed yet.

### Latest scope review — PHY suspend release, baseline 726d38d

[USB-state photos](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-state-hardware-result.md) confirm all 21 reads, BEAT 11→50 without errors, MemTotal 22204 kB, disconnected B-device MAC, eight zero DMA controls, inherited IRQ enables and PHY force_suspendm=1/value=0. Current active issues and every coverage row were reconsidered against owner/ blueprint requirements. Narrow MAC/PHY read access is CONFIRMED; the controller contract/host logging remain BLOCKED. Memory, boot qualification and power stay PARTIAL; input/display/media/rootfs/thermal/battery and later-phase gaps remain. No optional exit criterion is waived; M1 stays complete and M3 deferred.

The smallest functional next step is [M2-PHYWAKE-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-phy-wake-probe.md): read/check remaining PHY mode controls, then conditionally clear only 6a bit2, as corroborated by FM/LK. Require disconnected B-device and zero DMA, preserve calibration and all analog/VBUS settings, inspect readback without retry. This adds one bounded PHY control write, not UDC/DMA ownership or calibration policy. Full existing offline checks plus emitted access review apply; stop at BOOTIMG for owner test. Recovery/loader/partition boundaries and D08 are unchanged.

[M2-PHYWAKE-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-phywake-01-result.md) now passes one clean build, 21 top-level and four observation test methods plus linked-write/layout review. Candidate: 1,097,728 bytes, SHA-256 `d68c8fbc56721c7aa1fda5b3e321a9aff5876661aac857505864e28d8924793a`. It awaits owner test; no successful PHY release is claimed yet.

### Latest scope review — USB state observation, baseline 23d09db

The [returned clock-probe photographs](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-clock-hardware-result.md) show no errors, BEAT 15→50, IRQ 1689→5574, MemTotal 22208 kB, successful PWRAP/VUSB reads, USB0 ungated, USB mux selector 1 enabled and PLL USB reference enabled with power on/isolation off. Reconsidered every coverage row below, current open issues and owner/blueprint requirements: only narrow clock-read and timer-reporting facts advance. Core clocks/pins/IRQ/power stay incomplete; boot/memory remain PARTIAL, USB logging BLOCKED. Input, standard display, media, rootfs, thermal/battery and later milestone gates are unchanged. No optional feature is waived, no M1 reopening and no M3 work.

Next scope: a single cached read-only MAC/digital-PHY/DMA-control snapshot under strict observed supply/clock guards. This is first access to those register windows, requiring source/FM/LK width/side-effect review, fault tests and the full existing offline suite plus D08/package validation. No interrupt status, FIFO, endpoint index, analog trim/calibration, clock or controller writes; no DMA ownership change. [Contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-state-probe.md). Stop at the new BOOTIMG for owner test. Keep all existing recovery boundaries; no repeated unchanged source/ROM/recovery audit is needed.

[M2-USBSTATE-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbstate-01-result.md) now passes one clean build, 20 full build-suite methods and four observation-tool methods. Candidate: 1,095,680 bytes, SHA-256 `8c1f701b61a1adb70b1377071e6cb885cda989a422fd75d626cd5c7da5bdb5e7`. It awaits the owner test; no MAC/PHY hardware result is inferred.

### Original activation review

Baseline `ebeed72`, clean `main`; current GitHub #1–#32, open M0 and closed M1 reviewed against the local blueprint and retained hardware result. The owner now explicitly authorizes autonomous M2 research/implementation/builds and normal Git/GitHub operations, with a stop at each hardware-testable BOOTIMG and before any physical-device modification. This supersedes the earlier planning-session restrictions and queued research order; it does not establish any hardware fact.

**M2 is ACTIVE, entry PARTIAL; exit BLOCKED on unimplemented/unverified core interfaces.** M1 stays complete. All coverage rows below were reconsidered: their capability classifications and evidence limits remain unchanged because no newer physical result exists. M2's phase status changes from PLANNED to ACTIVE; #22–#27 remain open, and #27's controller gate is still BLOCKED. The working owner-reported version is 6.18.0-y2-m1; exact flashed SHA-256, MemTotal, repetition and timing are not supplied. The retained time32 candidate identity is recorded in [the M1 result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm1-runtime-hardware-result.md), not promoted to an identified hardware trial.

Execution priority: (1) #27 USB contract and only #23's needed VUSB/PWRAP/clock prerequisite; (2) one logging implementation/trial if that contract permits it; (3) RAM adequacy and #22's bounded expansion decision; (4) #24 input; (5) #25 standard display handoff; (6) #26 read-only removable media and recoverable stage-appropriate rootfs; (7) identified repeatability/stability and M2 exit audit. RAM expansion, UART wiring, full SMP and full power-framework implementation are not prerequisites for USB research. Reorder subsequent work only on evidence. The smallest current blocker is the FM-normal-handoff USB PHY/clock/VUSB/DMA contract; inspect those exact functions before selecting a runtime change.

D08, CPU0, stopped AP watchdog and guarded framebuffer remain the default. Stock preloader/LK, partition tables and calibration remain protected. Existing SPFT/FM recovery evidence is retained without another provenance/recovery audit; M0 backup/installed-lineage and inherited-DMA uncertainties remain residual risks, not production waivers. New subsystem ownership must be justified separately. No M3 audio or Y2PlayerNative implementation starts before real M2 exit evidence. No optional feature has been waived merely to reach today's target.

### Current execution checkpoint

[M2-PWRAP-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-pwrap-01-result.md) is offline validated, 1,093,632 bytes, SHA-256 `c51102c861d65d39f5af2425ed73e9c1ba21d8adaae1b016f450a58630946ac0`. The owner has now supplied [two physical photographs](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-pwrap-hardware-result.md): PWRAP RC=0/VALID=3, CID=0x2023, VUSB=0xc000, BEAT 18→50 and MemTotal 22208 kB. The cached PWRAP/VUSB result is confirmed on this boot; exact flashed hash, host timing and restoration remain unreported. Timer -61 is a source-identified IRQ-name parser mismatch. #23/#27 and M2 remain open.

Scope review at `c6709cc`: the next localized candidate corrects IRQ parsing and reads four exact USB clock handoff registers; no clock/PHY/USB controller/PMIC write or DMA ownership change is added. [Contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-clock-probe.md). All coverage rows were reconsidered against these photographs: boot stability, memory and power remain PARTIAL (now with measured MemTotal and one successful PWRAP read path); USB remains BLOCKED on its lower-level ownership contract. Other input/display/storage/rootfs/thermal/battery gaps and later-phase gates are unchanged. Preserve D08, CPU0, screen/watchdog and established recovery policy.

[M2-USBCLK-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fm2-usbclk-01-result.md) is now offline validated and awaits the owner test: 1,093,632 bytes, SHA-256 `602080eb199f3a4be30082ee114dfeb97ef414e10d8ad4acf5d239f2096cd6ec`. One clean build and 19 targeted validation methods pass; no device action occurred.

### First prerequisite scope review

The focused [PWRAP/VUSB probe contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-pwrap-probe.md) now resolves one implementable #23 step using FM/LK and pinned upstream/vendor source. This adds bounded AP PMIC read transactions to a candidate, with no PMIC register writes or USB ownership. Power remains PARTIAL and USB remains BLOCKED pending physical state evidence and the remaining PHY/clock/DMA contract. D08 and all other coverage classifications remain unchanged. Basic battery/charger reporting also remains an M2 exit gap from the blueprint; VUSB status cannot satisfy it.

## Blueprint assessment and authority

The [Y2Linux/Y2PlayerNative blueprint](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2PlayerNative%2Fblob%2Fmain%2FYY2PlayerNativeBlueprint.md) still covers the project's direction adequately: upstream 6.18, standard Linux interfaces, native Rust/C application, native audio before central player work, power/connectivity/product gates and rolling-wave planning. This audit reviewed the local blueprint, the actual Y2Linux code/config/DT and retained build reports, current issues, and the stock evidence indexed in [evidence-index.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fevidence-index.md). Local blueprint snapshot SHA-256: `f9850e35ed790008cbb125001cf166848c7dd1c11c580d41299ecbe311add95e`. No repeated provenance audit or new driver investigation was performed. Source applicability is not hardware success; Android behavior is a reference, not the native implementation.

Important reconciliations:
  - Blueprint example task IDs are illustrative. Existing Y2E/Y2B IDs and results

remain authoritative; do not create duplicate tasks with those sample IDs.
  - The owner superseded the original role split with direct M1 implementation.

That authorization is not a standing permission to execute a planning epic.
  - The owner accepted specific first-boot risks under D11. M1 core success does

not retroactively certify all M0 backups/lineage/DMA questions. M0 remains open; proven same-device SPFT recovery must not be repeatedly rediscovered.
  - M1 core is achieved, as explicitly reported by the owner. Blueprint M1

wording about reproducible boots/stability is broader than the retained report: boot identity/repetition/timing/stress evidence remains PARTIAL and is tracked under Y2H-300. Do not reopen the achieved core or claim release qualification.
  - New recurring milestone audits and the fast-iteration validation policy below

supplement the blueprint. They are not permission for a full build on a documentation-only day.

## Classification key

One primary status describes the scoped area, not every fact in it:
  - CONFIRMED: the stated narrow result is directly evidenced; scope matters.
  - PARTIAL: useful evidence or execution exists, but the platform capability

or its qualification is incomplete.
  - PLANNED: a bounded next task exists; it has not been implemented/validated.
  - UNKNOWN: the required contract/capability is not established; an epic is a

reminder, not enough evidence to upgrade this to a resolved plan.
  - BLOCKED: a specific missing prerequisite prevents the stated next capability.

Hardware-fact labels in older knowledge documents (including INFERRED/DISPROVEN) remain unchanged. An epic does not turn unknown hardware into confirmed support.

## Coverage matrix

Reassessed at the September 15 M5 entry audit using fresh authenticated POWER-02 evidence, current sources and retained milestone results. All rows were reviewed; unchanged rows retain their stated limits. Driver/interface availability and external research do not imply consumer qualification.[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm1-runtime-hardware-result.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-15-usb-reconnect%2FREADME.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fdonor-audit.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm3-audio-01-live-result.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Frecovery.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Ffirst-experiment-result.md)

| Area | Status | Actual evidence / remaining gap | Durable tracking |
| --- | --- | --- | --- |
| Physical Linux + initramfs + native PID1 | CONFIRMED | Storage06 switches from rescue to internal Buildroot at 8.728982s and authenticates owner-key SSH with no SD block device. Earlier DEV-02 removable-root and M1 results remain historical. | Closed M1 / #20–21; core stays achieved; #33 internal storage. |
| Boot/kernel stability and maintenance | PARTIAL | POWER-02 full image-length readback matches; internal boot and SSH work. Two retained reconnects pass with runtime PM held on. Charging failures and broader boot/cycle/stress/maintenance qualification remain. | #28/#30/#32. |
| RAM and reserved/DMA ownership | PARTIAL | 992 MiB bank with exclusions; physical MemTotal954660KiB and HighTotal228352KiB. Completed 256MiB short allocator test passes, substantial HIGHMEM consumed. Full-suite run capped600s; every-page/long-run/inherited-DMA containment is not proved. Narrow expansion #22 satisfied. | #22; #28. Owner-authorized development qualification. |
| SMP | CONFIRMED | Four CPUs online on DEV-02 with advancing cross-CPU/timer IPIs and no interrupt errors; full coherency/PM stress is a later qualification scope. | #28; optional for first wired player. |
| Clocks, resets, pinctrl/GPIO/IRQ and I2C | PARTIAL | DEV-02 CCF/PWRAP/MFD/regulator/core consumers operate; wheel has52IRQ/52I2C completions and both directions, no timeout. Exact full clock rates/unused orphan gates and future consumer reset/rail ownership remain #29/#30 prerequisites. | #23/#24/#28; research. |
| Watchdog and controlled reset | PARTIAL | POWER-02 charger watchdog serviced 646 times before voltage-fault inhibition. AP_RGU reset, RTC poweroff and offline routing are implemented; controlled reboot/off/wake acceptance remains open. | #28/#30; no new transition test. |
| On-device diagnostic channel | CONFIRMED | DEV-02 native fbcon and owner-confirmed visible color/checkerboard pattern; supported unblank succeeds. Cursor handling fixes a later shared-buffer checksum mismatch without a kernel change. | #20–21; result. |
| Developer host logs / USB | PARTIAL; reconnect workaround tested | Storage06/POWER-02 ACM and owner-key SSH over ECM work. POWER-02's first reconnect reproduces an IRQ-storm shutdown (-75). Keeping MUSB runtime PM active passes two physical reconnects on one boot, including wall-source charging; the scoped startup change is installed. Kernel correction with automatic runtime PM, fresh-boot validation of the startup edit, broader reconnect and power qualification remain open. Result. | #27, #23, #28; #30 charging blocker; #33 owner SSH. |
| Physical UART / early crash capture | UNKNOWN | UART0 candidate exists; no pad/level/wire capture. Ramoops retention/reader is unproved. USB cannot log hangs before its initialization. | Existing #16; broader crash/debug policy #32. |
| Display/controller/panel | CONFIRMED | DEV-02 DSI-1 connected, CRTC55 active, framebuffer56 XR24 480x360/pitch1920, fbcon bound, safe GEM/OVL address match and owner-confirmed pattern. Blank state corrected through sysfs; broader modes/power sequencing remain later. | #25/#28; research. |
| Backlight | PARTIAL | DEV-02 brightness/actual/max32 with physically visible panel; native brightness range, PWM/rail transitions and suspend sequencing remain #30. | #25/#23; #28/#30. |
| Wheel/select input | CONFIRMED | DEV-02 raw evdev has balanced Select and both wheel KEY_UP/KEY_DOWN directions;52wheelIRQ/52I2C completions. Supersedes DEV-01 -110 transport regression. | #24/#28; research. |
| Other buttons/power-key/touch/wake | PARTIAL | All five navigation keys, both volume keys and brief Power have balanced DEV-02 evdev events. No redesign; wake/suspend remains M4 and no touchscreen claim. | #24/#28 and #30; donor audit. |
| Removable SD | CONFIRMED | DEV-02 SD128 on11240000.mmc at13MHz/one bit; ext4 Y2ROOT boots Buildroot, reads files, accepts verified userspace updates and sync.512MiB filesystem retained; throughput/hotplug/card-removal/power-fail qualification later. | #26/#28; research. |
| Internal eMMC | PARTIAL; internal boot CONFIRMED | Storage06 authenticated reads confirm 15203328 logical sectors, exact p5/p7 geometry, stock MBR/EBR hashes and complete BOOTIMG hash. Offset 23552 restores normal reads; internal ext4 root/data mount rw and Buildroot starts without an SD block device. Owner SSH now works. Deliberate bounded-write/repeat/stress qualification remains. Two synthetic ext4 buddy-cache inode warnings remain; both filesystem checks report clean. | #33 storage; #28/#32. |
| Development rootfs and filesystem/data layout | CONFIRMED within observed scope | Current production Buildroot uses internal ext4 Y2ROOT/Y2DATA and BOOTIMG-owned modules. Earlier removable-root results remain history. Live USB startup differs additively from the retained root image. Preserving updates/data remain the production contract. | #28/#32/#33. |
| PMIC/battery/charger telemetry | PARTIAL; current charging failure | POWER-02 stops at 4.200073 V with latched voltage fault 0x8. Earlier OVP 0x10 is separate/unresolved. Brief DCP result is not sustained/full/offline acceptance. Pack thermometry, measured current and SOC remain unavailable. | #30; fresh M5-entry evidence above. |
| Thermal sensors/protection | PARTIAL | Fresh CPU about 14.7 C and PMIC about 46.9 C preserve the accuracy discrepancy. Own-efuse conversions and software trips exist; physical cooling/protection and absolute accuracy remain unqualified. Neither reading is pack temperature. | #30/#28. |
| cpufreq/voltage/OPP and cpuidle | PARTIAL | POWER-02 source offers 598/747.5/1040 MHz at the retained 1.15-V constraint, with WFI fallback. Fresh current frequency is 598 MHz. Repeated OPP/load/cooling and consumption acceptance remain; no voltage-scaling claim. | #30/#28. |
| Runtime PM/suspend/resume/wake | PARTIAL | POWER-02 exposes s2idle/deep and integrated SPM/CPU context. Fresh entries=0/resumes=0; same-session deep restore, intended wake and consumption remain unqualified. USB on/active workaround has unmeasured idle-power cost. | #30; integrates #28/#29/#31. |
| MT6582 AFE/ASoC/I2S/DMA | CONFIRMED narrow S16/44.1k path | AUDIO-02 DL1/CON3/IRQ/ALSA pointer progress and clean headphones; startup fix137b3f2 is deployed/tested. 48kHz, L/R and repeated stop/start remain;24/32-bit/higher rates unimplemented. Result. | #29; shared resources #23/#28/#30. |
| CS43131 / headphone / amplifier / speaker routing | PARTIAL; basic headphones CONFIRMED | Own CS43131 revisionA1 operates through upstream ASoC, VGP2=1.8V, ordered20/18/15 enables; clean44.1kHz audible headphones. SpeakerGPIO8 stays low; amplifier identity/output, jack reporting and precision clock validation separate/unqualified. | #29 with #23/#30. |
| Wi-Fi | PARTIAL evidence; no native interface | Own stock CONSYS_MT6582/mt-wifi metadata and matched firmware inventory; donor uses AHB HIF, not SDIO. Native driver, exact stepping/calibration/regulatory handling and end-user WPA2/network/reconnect/coexistence tests remain. | #31 entry audit; #30 prerequisite. |
| Bluetooth | PARTIAL evidence; no native HCI | Own stock BTIF/DMA/wake IRQs corroborate transport. External full cold calibration/A2DP and matching generic modem firmware reduce uncertainty. Own HVR/FVR, calibration/addresses, BlueZ/audio/reconnect/EDR/BLE/coexistence remain unqualified. | #31; #29 audio, #30 PM. |
| Firmware and per-device calibration | PARTIAL | Five own-stock files have exact hashes/headers and patch order; redistribution grant and controller compatibility not established. Own protected copies obtained read-only and retained privately; record mapping and valid addresses unproved. | #31/#32; no blobs/private data distributed. |
| FM where physically supported | CONFIRMED scope exclusion on this board | Owner identifies older board without usable reception; earlier own FM driver reported 0x6627 but reception failed. FM reception is unsupported here and not an M5 gate. Later populated revisions need independent evidence. | Conditional #31/M16 reference only. |
| Recovery and safe acquisition | PARTIAL | Owner-proven SPFT/FM history plus documented BOOTIMG-only Android restoration. Exact current image/per-device backups, consistency and independent retention remain incomplete. Recovery, actual trial. | Open M0; #32 owns continuing production/recovery coverage. |
| Updates / rollback / production security | PARTIAL | V1 release manifest, component versions, allowlists, per-owner SSH provisioning and staged rescue update/installer contract implemented. No OTA/signature implementation; no automatic torn-BOOTIMG rollback, unchanged LK supplies no new verified boot. | #33 architecture/package; #32 future lifecycle/security. |
| Production rootfs / services / non-root app contract | PARTIAL | Fresh POWER-02 inventory confirms internal p5/p7 read-write, owner-key SSH and no SD block device. Wider write/recovery/non-root lifecycle remain. Radio services are absent; future mutable configuration/bonds belong in Y2DATA. | #33/#32; radio services #31. |
| Time/RTC, entropy, identity and diagnostic privacy | PARTIAL | POWER-02 RTC exists but reports 2082; persistence/alarm/deep wake unqualified. SSH uses the retained reinstall pin and persistent owner authorization. Radio addresses/calibration remain private and unvalidated. No invented time/entropy/identity defaults. | #30/#31/#32. |

## Gaps found and minimum additions

The blueprint already names the major phases; the repository had only M0/M1 GitHub milestones and narrow #22–#27 follow-ups. Audio, product PM, connectivity and production lifecycle had no durable epic owner. Common clock/pinctrl/I2C, watchdog/reset, eMMC/rootfs, firmware selection/redistribution/calibration and conditional FM could otherwise fall between the narrow issues.

Five deferred planning epics now retain these gaps. No detailed children or new GitHub milestone shells are needed today:[](https://github.com/SchulzCode/Y2Linux/issues/28)[](https://github.com/SchulzCode/Y2Linux/issues/29)[](https://github.com/SchulzCode/Y2Linux/issues/30)[](https://github.com/SchulzCode/Y2Linux/issues/31)[](https://github.com/SchulzCode/Y2Linux/issues/32)

| Blueprint phase | Tracking epic | Current phase status / dependency |
| --- | --- | --- |
| M0 Evidence & Recovery | Existing open milestone 1 | PARTIAL; owner-accepted experimental exceptions are documented, not a full pass. |
| M1 First Boot | Existing closed milestone 2 | CONFIRMED core; broader stability qualification moves into #28. |
| M2 Core Hardware | Y2H-300 #28 | Core/Buildroot qualified for M3 progression; #22–26 satisfied. USB reconnect #27 stays open under #28 for later whole-platform qualification. |
| M3 Native Audio | Y2A-300 #29 | ACTIVE / NEAR COMPLETION; clean native S16/44.1kHz headphones. Notification fix deployed/tested. Remaining48kHz, L/R, stop/restart/repeat; #27 deferred. |
| Production Storage / Installation v1 | #33 storage activation (2026-09-13); #32 lifecycle | ACTIVE; internal root/data boot, stock block reads and owner-key SSH confirmed after manual flash. Wider write/stress/recovery qualification remains. |
| M4 Power Viability | Y2P-400 #30 | ACTIVE/PARTIAL; charging failure. POWER-02 deployed and hash verified; voltage fault 0x8 now stops charging. Earlier OVP and full/offline/deep-suspend/RTC/thermal acceptance remain open. Preserve implementation; no M4 rewrite under M5. |
| M5 Connectivity | Y2N-500 #31 | ENTRY AUDITED / BLOCKED; owner authorizes the end-user platform, but current M4 charging/qualification and own silicon/calibration mapping prevent integrated implementation/deployment. No native radios yet. |
| M6 Production Y2Linux | Y2R-600 #32 | PLANNED; storage/recovery/PM gates and later M18–20 platform release obligations. |
| M7–M20 application/product phases | Existing blueprint, no native backlog added | NOT STARTED; Y2PlayerNative waits for reusable Linux platform and final qualification. |

M4 numbering is not permission to defer basic thermal/power safety until after audio. M5 radio-specific power measurements depend on radio operation, so these phases have shared gates rather than a rigid all-or-nothing serial chain. M6 rootfs contracts can mature with M2 without prematurely choosing production OTA. The original next-five order is retained as history. Current owner direction defers #27 while finishing small M3 acceptance; it does not waive reconnect from final platform qualification.

## When Y2PlayerNative can become the serious workstream

The owner's 2026-09-10 platform-first instruction supersedes the earlier wired-player-only gate. First qualify the reusable general-purpose Y2 platform: M2 core/Buildroot including reliable development reconnect; M3 native ALSA/ASoC, MT6582 AFE, CS43131, amplifier, headphone/speaker routing and jack detection; M4 battery/charging/thermal, cpufreq/cpuidle, suspend/resume/wake and controlled shutdown/reboot; M5 Wi-Fi/Bluetooth with own firmware/calibration, BlueZ, reconnect/coexistence. Then complete GPU/lima and final whole-system qualification. Only after that does Y2PlayerNative implementation begin. #29–32 retain these gates; no application or later hardware phase starts in this live audit.

## Standing milestone-boundary rule

**At every major milestone boundary, repeat this gap audit and update the roadmap from real hardware evidence before proceeding.** Apply it before phase activation, exit/closure or a material change in hardware/memory/production scope. Root `AGENTS.md` links this rule so it remains visible in future sessions.

The boundary review must:
  - Compare current blueprint/owner decisions, repository changes, all active

issues/epics, retained validation and actual hardware results. Record date, revision, tested artifact identity when known, evidence origin and limitations.
  - Refresh every coverage row using this classification vocabulary. Separate

working narrow behavior, untested driver availability and planned work. Preserve older failures/history with explicit superseding notes; do not invent missing timings, hashes, firmware selection or hardware success.
  - Reconcile dependency/phase gates, accepted risks, unresolved backup/calibration

requirements and the next smallest blocker. An experiment's accepted risk is not a permanent production waiver. Honor all later explicit owner decisions.
  - Link each material gap to an existing issue/epic; add only a missing high-level

bookmark when necessary. Decompose only the next evidence boundary. Record whether the next phase is ready, partially ready or blocked and why.
  - Update this audit, relevant knowledge pages, roadmap and GitHub milestone/epic

status before proceeding. Hardware authorization remains separate.

An audit is a planning/evidence review, not an automatic test run. Future small localized code changes use one clean build, affected tests, D08/layout/BOOTIMG checks and final size/hash. Architecture/memory/packaging changes, new hardware subsystems, milestone qualification and release candidates use the appropriate full verification boundary. Do not rehash the unchanged entire source tree or redo ROM/SPFT provenance without relevant cause. A documentation-only request never triggers a build or hardware operation to fill a missing audit datum.

## CPU Final Fix01 physical admission — 2026-09-27

Owner authorizes the already-flashed Fix01 physical sweep, including bounded CPU/timer/QoS/idle/DVFS stress and guarded C3/full suspend. USB SSH reads match Linux0de6e951/Reborn36db1869, kernel6.18.0-y2linux-cpu-final-fix01, root2025.02.18-platform-v1.7, bootd3f4d265-ced8-4b53-8037-84637d765a89, taint0. Previous CPU Final qualification remains the authoritative before-state: conservative OPPs/hotplug/WFI/staged suspend/data/audio work; timer/app leases, SLIDLE/high voltage admission and full RTC resume fail. Software Fix01 receipt is not physical acceptance. Coverage gates remain unpromoted until this sweep. Existing recovery/fallback/protected partition and memory contracts unchanged. Proceed with existing SSH harness and targeted supplementation; ordinary failures retain independent testing, safety/integrity loss stops risky testing. No source patches, builds, flashing, push, external epic closure or architecture research. Private evidence: out/cpu-final-fix01-physical-qualification/.

## CPU Final Fix01 physical closing boundary — 2026-09-27

Owner-authorized already-flashed qualification is complete at the safe observation boundary; normal CPU platform acceptance FAILS. Installed source identity is Linux `0de6e951b438bf0f2d701e23e476d2b2405ba3c6` / Reborn `36db1869c6bab1ad2d00b7d8e7807ea6ef5b3803`, kernel `6.18.0-y2linux-cpu-final-fix01`, root `2025.02.18-platform-v1.7`. Host HEADs remain Linux `a5598918` / Reborn `36db1869`; no implementation changes, build, flash, push or commit in this pass. Existing user work/identity remain intact.

The [physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md) and restricted `out/cpu-final-fix01-physical-qualification/20260927T205514Z/` retain command receipts, measurements, both immediate recovery captures and owner confirmation. Three boot IDs are d3f4d265-ced8-4b53-8037-84637d765a89, 1807c573-b7c2-469e-9a16-5645b4d25ecb and 81e422f3-43cd-4ad6-877f-692eb1191b36. Owner Power once and two manual restarts are distinct; second restart follows USB loss with UI alive, not a spontaneous SoC reboot. Ordinary defects retained independent testing after safe recovery.

| Coverage / existing owner | Updated real-device state | Next gate |
| --- | --- | --- |
| CPU timer/performance, M4 #30 | PASS GPT6/GPT4/PPI29, actual highres/NO_HZ, eight real QoS classes, lower OPPs, hotplug, WFI, thermal priority | preserve these narrow successes |
| Deeper CPU idle, M4 #30 | FAIL C2 entry, PARTIAL coordinator, C3 NOT_TESTED | MSDC0/MSDC1 runtime clocks stay enabled; separate retention from runtime gate, qualify sustained inactivity |
| High-bin voltage, M4 #30 | software VOSEL recognition PASS; high admission FAIL at pwrap_readiness | expose exact raw predicate then correct real board contract, no bypass |
| PM/wake, M4 #30 | devices request FAIL, later staged/full RTC/Power NOT_TESTED | prove early journal safety/retention; durable kernel_suspend only, invalid SRAM cannot identify SPM boundary |
| Native audio, M3 #29 | PASS bounded 44.1 and 24/96->48, zero XRUN/decode/filter errors | no promotion of perceptual quality, blend transition or full resume |
| Transport, M2 #28/#27 and M5 #31 | Wi-Fi bounded hashes PASS; USB first hash PASS then transport loss; CONSYS single isolated retry PASS | capture loaded USB IRQ/DMA/carrier and independent recovery before restart |
| Storage/runtime, M6 #32 | final rw root/data/SD, errors 0, taint 0 | failed interval/full restoration still unqualified; accepted preserve-data/fallback/protected partitions unchanged |
| Telemetry, existing platform scope | timer states useful; SRAM invalid and health supplicant discrepancy retained | diagnostic availability is not a hardware pass |

Roadmap and capability ledger now reflect these observations. Earlier software completion and previous candidate staged successes are historical, not Fix01 physical acceptance. Root-cause confidence differs: MMC runtime early returns are source-backed; PWRAP predicate group is exact but operand unknown; staged PM and USB failing instructions remain unknown. Do not claim full PCM or CPU-vector causation from invalid SRAM. No charging-refusal certification: USB online did not mean BAT0 actively charging in this run.

Next boundary is the single coherent Fix02 correction plan in the report, covering PM diagnostic safety/readiness, PWRAP ownership, MMC runtime clocks and coordinator reachability, and loaded USB recovery. It preserves now-working timers/QoS/conservative/audio/radio retry, does not expand hardware or memory scope, and does not activate another architecture review. M4/M5/M6 release gates remain blocked/partial; no external epic/milestone was closed or modified. No new issues are needed for these already tracked gaps. Backup/calibration, protected storage, exact fallback and existing production obligations remain unchanged; this audit does not redo ROM/source recovery provenance.

## Knowledge-base reconciliation — 2026-09-28

This is a documentation-only evidence/gap audit, using the already completed [Fix01 real-device report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md). No new hardware test, architecture review, package build, flash, protected-state access, source/ROM/recovery provenance acquisition, milestone activation or scope promotion occurred. At entry both `main` trees were clean and synced: Y2Linux `a605c884aed7705a93293299628ef95d5f0219f8`, Y2Reborn `b5d1f4f985ffcbb14da013e7d56c098285496b46`. Exact running candidate remains Linux `0de6e95` / Reborn `36db186`, kernel `6.18.0-y2linux-cpu-final-fix01`, root `2025.02.18-platform-v1.7`; Git HEADs are not image identities.

The platform and Reborn entry pages had still presented Platform v1 or Hardware Final as current. This reconciliation updates both READMEs/current-state pages, the capability/evidence navigation and selected power, audio, radio, timer, idle, DVFS and USB summaries. It indexes all first-party Markdown pages and adds scope notices to historical records. It repairs a local link into ignored private `out/` without deleting the historical reference, and retains original physical/build captures and candidate/fallback images. The newer source configuration is explicit: 44.1/48 S16 enablement, a provisional enabled schema-2 low-voltage policy, and optional codec compilation with normal-runtime endpoints disabled. None is elevated to blanket physical qualification.

| Coverage / existing gate | Current decision from real evidence |
| --- | --- |
| CPU timer/QoS and lower OPPs, #28/#30/#34 | Narrow PASS; preserve GPT6/GPT4/PPI29, highres/NO_HZ, eight real leases, hotplug/WFI, thermal priority |
| Deeper idle and voltage, #30/#34 | C2 entry FAIL; coordinator PARTIAL; high-bin admission FAIL at PWRAP readiness; voltage transitions/C3 NOT_TESTED |
| Suspend/wake, #30/#34 | devices attempt FAIL; invalid SRAM prevents exact boundary; other staged/full RTC/Power wake NOT_TESTED |
| Audio/Reborn and radio, #29/#31/#32 | bounded wired fixtures, producer leases, Wi-Fi hashes and CONSYS retry PASS; peer audio, full resume, fidelity/endurance NOT_TESTED |
| USB/recovery/storage, #27/#28/#32/#33 | first small USB hash PASS then loaded connection loss; recovered root/data/SD rw and ext4 error 0; exact failed-interval cause unavailable |
| Production/security, #16/#32/#33 | immutable fallback/preserve-data contract and private owner assets remain; no release, OTA, production trust or milestone promotion |

The one coherent Fix02 plan remains PM diagnostic safety, genuine PWRAP readiness, MMC runtime clock ownership/system-idle reachability and loaded USB recovery. It is not implementation authorization from a planning document. Existing epics/gates remain open at their previously recorded status; no issue was created or externally changed. Current-state pages and complete catalogs are the first reading point; older task permissions/"ready" claims remain dated.

## Bluetooth optimization admission — 2026-10-04

Owner explicitly authorizes the Bluetooth implementation/research pass in isolated `codex/platform-v1-bluetooth` worktrees from Linux `b5aea93` / Reborn `b71b468`. Read-only locked SSH identifies installed Baseline02, Linux `8584ccd8`, Reborn `b71b4688`, kernel `6.18.0-y2linux-baseline-02`, root v1.21, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0. This supersedes the *installed identity* in the older UART01 receipt; it does not constitute the separate Baseline02 cold-boot/C3 qualification. Retained UART01 C1/C2/C3 evidence remains bounded to its own image/boot. No headset is available, as confirmed by the owner.

F102/F103/F104 and #31 remain PARTIAL: the controller/BlueZ/BlueALSA are observable; peer pairing, audio, reconnect and endurance cannot be promoted by this pass. F105/F108/F229 retain peer/audio/coexistence evidence gates. #28/#31/#34 remain OPEN on read-only GitHub refresh. Idle measurement with Bluetooth off shows 50.37 Reborn Bluetooth thread context switches/s and repeated 2s BlueZ snapshots; these justify localized event/wakeup fixes, not a new kernel power architecture.

Proceed with signal-based observation, bounded-intent/recovery fixes, private-bus regressions, ARM userspace builds and temporary, restored runtime tests only when the nonblocking shared device lock is held. Preserve one reconnect owner and FFmpeg → shared DSP → final sink conversion → BlueALSA. No memory, firmware, calibration, protected storage, image packaging, flash, push, merge, release or milestone closure. The next acceptance boundary remains actual peer/audio and coexistence measurements on the final integrated artifact. Findings and final classification: [Bluetooth optimization receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-BLUETOOTH-OPTIMIZATION.md).

## Platform 1.0 graphics pass admission — 2026-10-04

Owner requests an evidence-led GPU/display/power pass in isolated `codex/platform-v1-graphics` worktrees (Linux base `b5aea93`, Reborn `b71b4688`). No main edits, push, flash, memory/layout change or full-system suspend trial is authorized. Live access requires the shared non-blocking `/tmp/y2-platform-v1-device.lock`; admission attempts found it busy, so no device command ran. The retained UART01 and GPU-01 receipts supply real hardware evidence while fresh observation awaits exclusive access.[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-18-gpu01%2FREADME.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md)[](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-REBORN-PRODUCT-UI-V2.md)

| Coverage | Classification | Evidence / next boundary |
| --- | --- | --- |
| Mali-400 MP2, Lima/Mesa, GBM/EGL/GLES2, 480x360 KMS | CONFIRMED, retained awake scope | GPU-01: correct rendering, 30 FPS, static GPU runtime suspend. Preserve architecture, clocks and PM policy. |
| C1/C2/C3 and screen/workload restoration | CONFIRMED, bounded UART01 scope | UART01; this pass does not alter CPU idle or repeat dormant trials. |
| Current Reborn static redraw, scrolling, artwork and blank/wake | PARTIAL | Source has dirty rendering and owned-CRTC sleep; collect exact running identity, counters and bounded product scenarios before claiming fresh physical success. |
| Product v2 splash/dissolve/shutdown | PARTIAL | Product v2 source/pixel/protocol evidence; retained receipts do not replace fresh visible cold-boot/shutdown observation. |
| Graphics full system-suspend/context restore | PARTIAL | Lima force-suspend/resume hooks exist; another session owns same-boot system-suspend qualification. No duplicate experiment. |
| Electrical savings / endurance / release | PARTIAL | Activity counters are not battery watts; no milestone or public-release acceptance. |

GitHub #28/#31/#34 refreshed read-only and remain OPEN. #34's historical pre-Reborn text is superseded by the current repository and UART01 receipts; its full-resume gate remains open. Refreshed OPEN statuses preserve the independent gates; no issue/milestone closure is warranted. Proceed with source audit, localized host checks and locked runtime measurements; implement only demonstrated graphics defects. Next smallest evidence boundary is an exclusive current-product observation. Results and remaining gaps belong in [the graphics receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-GRAPHICS.md).

Same-day peer evidence subsequently identifies installed Baseline02 `8584ccd8`/Reborn `b71b4688`, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0. The instrumented Reborn performance baseline shows 13 frames/10.09s on paused Home/Now Playing and zero screen-off frames; it restores installed `b71b4688`. Static invalidation is therefore a demonstrated gap, already being corrected by that parallel pass. Do not duplicate its renderer/event-loop work; final graphics acceptance depends on integration and physical after evidence. The local graphics branch separately reduces a measured full-size JPEG decode cost, with 68 Linux/238 Reborn tests, strict lint and ARM checks. At this intermediate point live graphics observation still awaited the lock, held by storage after the performance and Wi-Fi windows. The evidence boundary above supersedes that access status with fresh bounded results; release, full-resume and visual gates remain open.

## Wired precision completion admission — 2026-10-04

Owner explicitly authorizes isolated source implementation, exact MT6582/stock research and bounded locked physical audio tests; no flash, push or merge. Linux starts at b5aea93, Reborn at b71b468, on dedicated `codex/platform-v1-highres-audio` worktrees. Read-only device admission under `/tmp/y2-platform-v1-device.lock` observes installed Baseline02 kernel, boot 27e6d684-3794-4490-95db-a489027cd4f4, taint 0 and idle Y2Audio. Exact direct constraint intersections admit only S16_LE stereo 44100/48000; S24_LE/S32_LE and 88200/96000 are rejected. This is driver admission evidence, not silicon maximum or low-bit proof. Raw receipt: out/highres-audio/validation/device-admission.txt. Retained UART01 and native headphone evidence remains authoritative for its bounded tests; new-image general CPU qualification is outside this pass.

| Coverage | Classification | Boundary |
| --- | --- | --- |
| Native wired audio; #29 | CONFIRMED S16 narrow scope / PARTIAL wider precision | Exact DL1/interconnect evidence must precede wider register or ALSA enablement. |
| CPU/timers/idle/storage; #28/#33 | CONFIRMED retained bounded scope / PARTIAL wider qualification | Preserve architecture, memory and partition layout. |
| Bluetooth/Wi-Fi/USB; #31 | PARTIAL | Concurrent isolated sessions own radio changes; no branch integration. |
| GPU/display; #34 | CONFIRMED awake scope / PARTIAL full suspend | Preserve existing screen/runtime-PM behavior. |
| Production/release; #32 | PARTIAL | No release or milestone closure; source/ROM/recovery provenance unchanged. |

Open issues #16/#27/#28/#29/#31/#32/#33/#34 refreshed read-only. No remote status change is warranted or authorized. High-resolution implementation is ready only after exact fetch/packing/interconnect documentation or stock programming establishes every meaningful bit. If unavailable, retain the safe S16 contract and publish the unresolved hardware boundary without claiming a 16-bit silicon ceiling. Next: exact vendor source and targeted stock analysis, software low-bit fixtures, truthful diagnostics and locked baseline tests.

Bounded S16 test admission: a second locked read verifies the installed Linux 8584ccd85f052f351fe51650b2348c83ca894ed4 / Reborn b71b468, same Baseline02 boot/taint 0, suspended AFE, no PCM owner and headphone disabled at -60 dB. Exact stock HAL width/fetch functions return -ENOSYS; mixed-tree ASoC wide fields are unselected by its MT6582 defconfig and lack compatibility proof. No wider mode is admitted. New kernel diagnostics and S24 software rounding are host/ARM compiled, not installed. Ready for bounded existing S16 DMA/rate/runtime-PM observation and offline three-format A7 CPU measurements under one non-blocking device lock. No source/memory/production scope expansion.

## Platform 1.0 input pass admission — 2026-10-04

Owner explicitly authorizes implementation, optimization and bounded physical input observation in isolated `codex/platform-v1-input` worktrees, based on Linux `b5aea93` and Reborn `b71b468`. No flash, push, main-worktree changes or full system-suspend implementation is authorized. The shared nonblocking device lock was busy on first attempt; no live access occurred.

Retained UART01 hardware evidence remains authoritative for bounded C1/C2/C3: Linux `e9e8d63`, Reborn `b71b468`, boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b`, taint 0, 3,647 checked C3 returns. Retained DEV02 and GPU01 evdev captures show APT32F press/release wheel records and all eight physical controls; they do not prove counted slow-detent accuracy, current-image bounce, presentation latency or human feel. Baseline02 new-image qualification remains PHYSICAL_NOT_RUN.

| Coverage / dependency | Classification | Next evidence boundary |
| --- | --- | --- |
| APT32F IRQ/I2C/evdev, #28 | PARTIAL | Current installed identity, bounded capture and detent counters; preserve IRQ-only driver unless evidence requires change |
| Reborn timing/actions/recovery, #28 | PARTIAL | Deterministic failure/timestamp/hold tests, targeted fixes, workspace checks and ARM build |
| Display/presentation latency, #34 | PARTIAL | Correlated input/state/frame timestamps; physical actuation origin requires owner or external measurement |
| C1/C2/C3 input compatibility, #28 | CONFIRMED bounded retained CPU scope; PARTIAL input scope | Observe untouched input IRQ/poll activity without changing CPU/radio policy |
| Power/full suspend, #28 | PARTIAL | Typed Power and screen-state ownership here; full suspend belongs to another session |
| Product v2 physical UX | PARTIAL | Counted detents/buttons, screen-off/wake and owner feel test on installed candidate |

GitHub #28/#34 refreshed read-only: OPEN. No remote issue mutation or milestone closure; parallel sessions retain their ownership. Product v2 global controls, fine-control contexts and long-list acceleration remain the authority. Proceed with source mapping and deterministic reproduction while retrying the device lock. Recovery/protected partitions, memory, ROM provenance and production scope are unchanged. Admission is PARTIALLY READY: software work authorized, hardware counts and candidate acceptance pending. See [the input validation record](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-INPUT.md).

## Storage Platform 1.0 optimization admission — 2026-10-04

Owner requests an isolated storage/filesystem pass from Linux `b5aea93` and Reborn `b71b4688` on `codex/platform-v1-storage`; no main-worktree edits, flash or push. This narrow review precedes implementation and physical measurement. Retained hardware authority: candidate3's 200 MHz SD data CRCs and clean bounded 100 MHz reads ([SD characterization](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-SD-SDR104-DIAG.md)); UART01's clean eMMC/SD SHA256 after real C2/C3 returns ([physical receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md)). Candidate4's stock pad/card-driver changes are included in current source, but its original receipt is software-only. A read-only identity probe saw Baseline02 running at HS200 and SDR104 with zero counters, boot `27e6d684-3794-4490-95db-a489027cd4f4`; the lock acquisition raced another session, so no qualification is claimed from that probe and all further physical access requires the non-blocking device lock.

| Coverage / existing gate | Admission classification and next evidence |
| --- | --- |
| eMMC / #28, #33 | CONFIRMED bounded HS200 negotiation/readback and post-idle integrity; PARTIAL sustained writes/fsync/performance/repeated boot |
| SD / #28, #33 | PARTIAL: older 200 MHz CRC failures retained; candidate4/later pad and driver selection must be reconciled before choosing a production ceiling |
| Filesystems/media / #32, #33 | PARTIAL ext4 physical evidence, FAT/exFAT source support; inode/ctime mount claims disagree with stable diskseq inventory and require a paired Reborn fix |
| CPU idle / #28, #34 | CONFIRMED bounded C1/C2/C3 UART01; preserve every blocker mask; collect passive storage regression on installed Baseline02 |
| Suspend/endurance/release / #30, #32, #34 | PARTIAL; full sleep/repeated boot/card matrix/endurance remain independent physical gates |

Read-only GitHub refresh: #16/#27/#28/#29/#31/#32/#33/#34 OPEN, #30 CLOSED; no external status mutation or milestone closure. Preserve storage addressing, Y2DATA, recovery/backup/calibration obligations, exact fallback, memory map, regulators and idle guards. No raw writes, autoformat, mounted-media reset or SQLite optimization. Proceed with the smallest justified source fixes, targeted regressions and safe scratch measurement; owner is available for SD interaction. Final decisions and unobserved gates belong in [the storage report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-STORAGE.md).

## Storage Platform 1.0 closing audit — 2026-10-04

This boundary reviews the owner's isolated storage pass before local handoff. Actual installed Baseline02 is Linux `8584ccd85f052f351fe51650b2348c83ca894ed4`, Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0. Final locked hardware receipts record clean scratch cleanup, mounted ext4 SD at SDR104, eMMC HS200, both clocks gated, zero PM mismatch/error and unchanged transport fault counters. The non-blocking lease was released normally before the reserved suspend lane; that lane's later qualification is separate from this pass. New source remains uninstalled: Linux implementation `2a603c1`, Reborn source identity `ee1c25a` and playback/sidecar guard `f726ae4`. Affected Reborn app38/platform77/library28/ media22 plus architecture guards, denied-warning Clippy and pinned ARM build pass; final ARM ELF/dependency and QEMU pinned image pixels pass as emulation. See the [storage report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-STORAGE.md) and [compact physical/software receipt](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-storage-20261004.json).

| Coverage / existing gate | Closing classification and smallest remaining boundary |
| --- | --- |
| eMMC / #28, #33 | CONFIRMED bounded HS200 read/write/fsync/SHA/PM. Direct read 98.717 MB/s, guarded write 26.800; retain HS200. Mounted-root DDR52/HS52 renegotiation and repeated cold boots remain untested. |
| SD / #28, #33 | CONFIRMED bounded one-card SDR104/DDR50/SDR50/HS, 4 GiB top-rung direct reads without CRC/timeouts; retain current ladder. Candidate3 failures remain historical, superseded only for installed later pads/card selection and this card. Card/temperature/endurance matrix remains PARTIAL. |
| Filesystems/media / #32, #33 | CONFIRMED installed ext4 fsync/hash/eject/same-card reinsert and host scratch FAT32 Unicode/dirty-bit refusal/ext4/exFAT no-write checks. Paired stable claims/CID sources, dirty-mount gate and pinned playback admission are software-tested. Different-card/FAT/exFAT/large-file target acceptance remains PARTIAL. |
| Music/scanning / #29, #32, #33 | CONFIRMED stock 1,000-file physical corpus on both volumes: all hashes match, initial scans 5.526/5.495 s, all incremental rows reused, zero failures/controller deltas. New app/native source guard still requires matching deployment and target acceptance; SQLite ownership remains separate. |
| CPU idle / #28, #34 | CONFIRMED storage clock gating/retention and clear MSDC blocker bits; retain UART01 actual C2/C3/hash evidence. This USB/radio four-core boot has no new C2/C3 entries; intended-workload regression remains PARTIAL. No masks weakened. |
| Suspend/power / #30, #34 | PARTIAL in this storage pass; no full sleep, electrical durability or power-loss claim. Reserved independent suspend lane owns its actual results. |
| Release/security/boot/USB/radio/GPU / #16, #27–#29, #31–#34 | Existing scope retained; localized tests/config/DT/modules/ABI/offline BOOTIMG pass. No new paired release installation or broader acceptance, backup/calibration waiver or unchanged ROM/recovery recapture. |

Fresh read-only GitHub refresh keeps #16/#27/#28/#29/#31/#32/#33/#34 OPEN and #30 CLOSED. No status mutation or milestone closure is warranted. Existing recovery/fallback, Y2DATA/protected partition, memory, supplies and firmware obligations remain unchanged. Final classification is PARTIALLY READY: local source/report handoff is ready, general Platform 1.0 qualification is not. Next boundary is paired Linux/Reborn/native integration with explicit source-key migration/media admission, then owner-supported repeated/absent boot, second-card and physical filesystem matrix. Do not infer hardware authorization from this planning row. No flash, push, autoformat, raw write or mounted-media reset.

## Storage removable-mount gate audit — 2026-10-04

A source review during the authorized filesystem pass found that `y2-media mount` identifies the card but does not run the existing read-only checker. The owned-host FAT32 test proves that a dirty clean-unmount bit produces a nonzero `fsck.fat -n` result without changing the image. Current physical media is clean ext4, with successful explicit `e2fsck -f -n` and remove/reinsert; no dirty user media is created. Adopt a bounded read-only preflight before SD mounts, reject checker faults/timeouts/source changes, and leave automatic repair/formatting disabled. Internal root/data boot gates stay unchanged.

This is a localized production-admission change within #32/#33, not hardware, memory or filesystem-format expansion. Read-only checks may delay mounts or refuse media requiring journal recovery; that availability limit must remain visible. Existing MT6582 modes, fallback, runtime PM and C2/C3 guards remain unchanged. Paired claim/source-ID changes still require Linux/Reborn integration; new source is software-tested, not installed by this pass. Proceed with focused media/checker tests and update [the receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-STORAGE.md).

## POWER-FINAL-07 charging hardware-scope audit — 2026-10-10

Boundary: a material change in hardware production scope (charge current above the physically exercised 450/650 mA selectors). Repeated before source changes, per the standing rule. No build, flash or device write is performed by this audit. Owner authorization for the work is the 2026-10-10 POWER-FINAL-07 instruction; it does not authorize flashing or unqualified high current.

Baseline: POWER-FINAL-06 bring-up source (Linux `c1ef37a`, branch `codex/platform-v1-power-final-06` tip `bd7e54d`, Reborn `97ff8c3`). The owner flashed 06 on 2026-10-10; a read-only health capture (`out/deep-sleep-final/evidence/20261010/90-power06-first-check/`, boot `bed8cebd`, taint 0, ext4 errors 0, `Y2INFRA mode=powerdown fallback=0`) shows the charger healthy at the 450 mA selector (SDP, 500 mA budget, BAT 8% 3.67 V, constant-current, die 36.9 C, watchdog pets advancing, no fault). Deep-sleep qualification of 06 remains physical NOT_RUN; charging changes are kept independent of it and are not claimed as integrated.````````````````````````

| Row | Classification | Evidence and limit |
| --- | --- | --- |
| Stock CS_VTH selector table | CONFIRMED (offline) | 16 entries at 0xc07572f8 (units 0.01 mA) = 1600…70 mA, identical to BSP CS_VTH_PMIC. Selectors 15/12/10 already hardware-exercised. |
| Stock per-source request | CONFIRMED (offline) | select_charging_curret0xc03a1d88: type1 500, type2/6 650, type3/4 1100, type5 800, type7 500, else 70 mA. Detection stores only types 1,3,2,5,4 (Apple signature is type5). |
| Linux policy | WORKING narrow | 70/450/650 only; DCP/CDP/Apple 650, nonstandard 70, SDP 450 from allocation. Duplicate selector tables in power-math.h, source-policy.h, policy.h. |
| Charge current measurement | PARTIAL | ISENSE−BATSNS drop is 98.3 mV (16 CC samples, 450 mA) and 139.6 mV (2 samples, 650 mA DCP), flat over 3.70–4.17 V, offset ~2 mV at zero current: 0.21 ohm-equivalent. BSP CUST_R_SENSE is 200 mohm for the internal linear charger (68 only for external FAN5405/BQ24158); the stock Y2 binary compiles 68. Absolute mA unvalidated (+6% vs 200 mohm). |
| Pack rating / capacity | UNKNOWN | No cell label/datasheet in evidence; stock model constants 1300 mAh (Y2 binary), 1728 mAh (reference header); web sources show only other Innioasis models at 1250–1500 mAh. A charge C-rate cannot be derived. |
| Pack temperature | UNAVAILABLE | No NTC (stock force_get_tbat returns literal 25); only PMIC die (36–46 C at 450 mA incl. system load). MT6323 is a linear charger: dissipation scales with (Vchr−Vbat)·I. |
| Faults 0x8 / 0x80 | EXPLAINED | 0x8 = battery sample ≥4.2 V safety (POWER-02 waited above the CV target; fixed by first-sample termination). 0x80 = protection-register expectation mismatch: after 1521 watchdog pets (about 38 min) at 70 mA CHR_CON0 read 0x62 where y2_charge_protections() requires bit0 (VCDT_HV_EN) set (0x63 pattern); the fail-closed inhibit worked, what cleared bit0 is NOT established (stock has a charger_hv_detect_sw_workaround thread that toggles it). |
| USB data + charging | WORKING (historical) | Composite gadget unchanged by this scope; DCP/CDP detection does not require the gadget. |

Gate decision: implement the full verified selector table, the stock source-request policy, a single policy function and die-temperature derating; default charge ceiling stays 650 mA until a cell charge rating or independent current/temperature evidence exists. Selectors above the stock maximum (1200–1600 mA, never requested by stock) are rejected at the PMIC write boundary. Raising the ceiling above 650 mA is a root-only, volatile, logged qualification action, not shipped behavior. Readiness for the next boundary: PARTIALLY READY (implementation yes; high-current activation blocked on cell rating).

## POWER-FINAL-08 internal-storage hardware-scope audit — 2026-10-10

Boundary: a material change in hardware/production scope: the eMMC host write allow-list gains the stock FAT partition (p8), and that partition is reformatted. Repeated before source changes, per the standing rule. This audit builds and flashes nothing. Owner authorization (2026-10-10): extend the write guard to p8, replace the stock FAT filesystem with ext4 `Y2MEDIA`, and migrate then delete the old `/data/music` originals once hash-verified. Flashing remains the owner's.

Baseline: POWER-FINAL-07 (Linux `551baad`, branch `codex/platform-v1-power-final-07`), installed image is POWER-FINAL-06. Evidence: `out/deep-sleep-final/evidence/20261010/{91,92,93}-*`.````````````````````````````````

| Row | Classification | Evidence and limit |
| --- | --- | --- |
| eMMC geometry | CONFIRMED | mmcblk0 15203328 sectors (7423 MiB); p5 Y2ROOT 1679360, p7 Y2DATA 1638400 at 2104320, p8 stock runtime FAT 11460608 at 3742720 (5596 MiB), directly after USRDATA and ending at the exposed disk end. Hidden prefix/tail, BOOTIMG, NVRAM, PROTECT, SEC_RO, SECCFG, BMTPOOL, CACHE stay outside every write span. |
| Stock p8 contents | CONFIRMED | vfat serial 3F93-07E6, 541 files / 31 MB (stock Music, Y2Player, Themes, Android folders, screenshots); fsck.fat -n reports only a stale dirty bit. File-level backup retained (93-stock-fat-partition-backup/p8-contents.tar, 20.4 MB). |
| Why MTP showed 808 MB / 511 MB | EXPLAINED | Internal Storage was a folder (/data/music) on the 800 MiB Y2DATA that also holds state and logs; the SD filesystem was a 512 MiB copy of a root image on a 121 GiB partition. SD reformatted 2026-10-10 (125.7 GB over MTP, hashes verified). |
| Write guard | CHANGE | One added span [3742720, Y2_EMMC_DISK_SECTORS); tests pin ANDROID, USRDATA, p8 and the exact native extents sector by sector, and that a write straddling spans is refused. |
| Y2Media identity | DEFINED | ext4, label Y2MEDIA, UUID ...0103, geometry-checked; mounted only on exact match at /media/internal after e2fsck -p; never boot-critical. Provisioning is explicit and names the stock serial. |
| Library / MTP / SFTP / upload | CHANGE | Internal Storage = /media/internal/music; Reborn follows the platform's Ready record and falls back to /data/music before provisioning. Factory reset does NOT erase Y2Media music (listed as preserved). |
| Wear / power loss | UNKNOWN | ext4 on eMMC with journal; unclean power loss repaired by e2fsck -p at mount. No endurance measurement. |
| Physical | NOT_RUN | Nothing above is installed. Provisioning runs only after the owner flashes and only on the exact serial. |

Readiness for the next boundary: PARTIALLY READY (source and offline tests; physical provisioning pending flash).

## POWER-FINAL-10 Reborn UI v3 scope audit — 2026-10-10

Boundary: a material change in production scope (what the owner sees and presses) and a bounded change in graphics-memory scope: Reborn Product UI v3 replaces the v2 interface, the early boot splash and the shutdown screens, and changes what the Power button does. Repeated before source changes, per the standing rule. This audit builds and flashes nothing, and the owner asked for this redesign to be built as candidate 10. **No kernel, driver, partition, power or radio code changes in this candidate**; it is POWER-FINAL-09 plus Reborn 0.3.0.

Baseline: POWER-FINAL-09 is installed and checked (evidence `out/deep-sleep-final/evidence/20261010/94-power09-first-check`: clean first boot, taint 0, MTP roots `/media/internal/music` and `/media/sd`, Reborn playing from Y2Media).````````````````

| Row | Classification | Evidence and limit |
| --- | --- | --- |
| GPU path | UNCHANGED shader, NEW textures | The fragment program is still texture × tint. New: three 1024-wide glyph pages and one 512-wide shape/icon page uploaded as GL_LUMINANCE_ALPHA (1 byte/texel in the binary), a 1024×512 RGBA thumbnail atlas and 5 draw-state combinations. A host harness renders all 62 preview frames through the production GL code on Mesa and matches the Python rasteriser (mean difference < 1.5/255). Mali-400 behaviour of luminance-alpha and non-power-of-two textures is standard GLES2 but NOT_RUN on the device. |
| Memory | CHANGE, bounded | UI textures grow from about 4.4 MB to about 9 MB (fonts 5.9 MB, masks 1.5 MB, thumbnails 2.1 MB, artwork 0.2 MB) against MemTotal 951824 KiB. Frame lists fall from up to ~1800 quads to a few hundred in about 40 batches. Resident set not yet measured on a flashed image. |
| Storage | CHANGE, bounded | A cover cache of at most 1500 files (about 55 MB) under /data/reborn/cache, written atomically, emptied by Clear cache; Y2Data is 800 MiB shared with settings, logs and the library database. Disk-full falls back to no cache (placeholders and decode on demand). |
| CPU | CHANGE, unmeasured | Cover decoding runs on a background worker under the existing artwork-decode workload hint, one cover at a time, only for covers on screen; it replaces the old single-slot collection-art worker. No measurement yet. |
| Power button | CHANGE | A short press still turns the screen off or on (or sleeps when paused). A hold no longer opens a confirmation sheet: at the existing 650 ms long-press a ring fills over 1.2 s and turning off happens at about 1.85 s from the press; release cancels (Action::PowerHoldCancel). The shutdown request, grace period and acknowledgement path are unchanged. There is no Quick Settings or Power menu any more. |
| Shutdown timeline | UNKNOWN | User shutdowns have a 10 s grace and low-battery shutdowns a 3 s grace. The normal animation is 74 frames at 34 ms (about 2.5 s) around the real save; the low-battery farewell is 30 frames (about 1.0 s). If Reborn does not acknowledge, the platform's deadline still fires and blanks the panel. On-device timing NOT_RUN. |
| Early splash | CHANGE, tested | reborn-splash-mark.h is regenerated from Reborn's boot layout; the hand-off frame, every progress frame and the failure screen are pixel-identical to Reborn's own frames (27 splash tests pass), including the new hard-edged leading dot. The failure screen now reads Couldn't start / Hold Power for 10 seconds, then turn it on again. |
| Removed from the normal UI | CHANGE | Diagnostics, maintenance, codec/LDAC tuning, update internals, song info and jump to letter move to a service menu opened by seven taps on Version in About & Updates. SSH and rebornctl are unchanged. |
| Licensing | CHANGE | Open Sans (SIL OFL 1.1) glyph data is compiled into the Reborn binary; the licence text is installed at /usr/share/reborn/OpenSans-OFL.txt and named in the package licence. No font file is installed. |
| Open first-boot failure | UNRESOLVED, unrelated | The 08 first boot showed the splash failure screen once; it did not recur on 09. This candidate does not change that path but its new failure text must be read on the device if it recurs. |
| Physical | NOT_RUN | Nothing above is observed on hardware. |

Gate decision: build candidate 10 as 09 plus Reborn 0.3.0; keep the platform untouched; the owner flashes and reports what the screens look like. The first on-device check after flashing is read-only: identity, taint, Reborn memory and CPU, thumbnail cache growth, then the owner's visual review. Readiness for the next boundary: PARTIALLY READY (source, host and splash tests; physical review pending flash).

## POWER-FINAL-11 remaining-screens scope audit — 2026-10-10

Boundary: a change to a power-adjacent production component: the rescue-environment charger's display (`tools/production/offline-charge.c`) is redrawn, and Reborn gains system screens that react to USB, Bluetooth, battery and update state. Repeated before source changes, per the standing rule. This audit builds and flashes nothing. The owner asked for the screens left out of candidate 10. Candidate 11 is 10 plus those screens; no kernel, driver, partition or radio code changes.``````

| Row | Classification | Evidence and limit |
| --- | --- | --- |
| Charger decision logic | UNCHANGED | power_event, safe_boot_sample, the 3.4 V gate, the 2 s hold, sampling, unplug-wins and every write are untouched; the existing two charger tests still pass. Only draw() changed. |
| Charger display | CHANGE, host-tested | The 5×7 block alphabet and moving blocks are replaced by images rendered from Reborn's quads (ring and bolt, Charging / Charged / Charging paused, three hint lines) plus a ring segment drawn procedurally with integer 3×3 coverage (no libm, no allocation). New tests render real frames into a memory framebuffer and check the sweep, the full and paused ring, text presence and bounds. On-device NOT_RUN. |
| State-of-charge claims | UNCHANGED, deliberate | The design showed a percentage and "about 1 h 10 min to full". Neither is shown: the percentage is a provisional voltage estimate and time-to-full is not computed anywhere. The ring only sweeps (activity) and closes when the status is Full. Copy is tested to contain no digits or "%". |
| Charger binary size | CHANGE, small | About 30 KB of image data in the initramfs charger. |
| Computer screen | CHANGE | Shown when the platform reports the transfer service Ready or Copying and the state has been observed; Back dismisses it, volume and transport still work; it returns on a new connection. It only reads the existing USB state. |
| Update download | CHANGE | A sweeping ring replaces a static page; no progress figure is claimed (none exists in the model). |
| Battery warning | CHANGE | A dialog once per level (Low, Critical); shutdown behaviour and the platform's low-battery policy are unchanged. |
| Physical | NOT_RUN | Nothing above is observed on hardware. |

Gate decision: build candidate 11 as 10 plus these screens. Offline-charging behaviour must be observed by the owner (unplug, replug while off, Power hold) after flashing; the fallback pair (10) is in the package. Readiness for the next boundary: PARTIALLY READY.

## POWER-FINAL-12 suspend-ordering and charge-completion scope audit — 2026-10-11

Boundary: two power-adjacent production changes after real hardware evidence from candidate 11 (flashed, owner-run unplugged sleep at 23:07, retained logs read afterwards). Repeated before source changes; this audit builds and flashes nothing. The display-recovery experiments in the main repo are not part of 12.````````````````````````````

| Row | Classification | Evidence and limit |
| --- | --- | --- |
| Deep-sleep device-phase stall | CHANGE, unproven | The retained Y2_DPM_STALL dump (/sys/fs/pstore/console-ramoops-0, round 1 and 2) shows exactly two uninterruptible tasks: the suspending python3 and one async worker, both in dpm_wait_fn under dpm_wait_for_subordinate. No task is blocked in synchronize_irq, an I2C transfer or any driver. The previous hypothesis (APT32F disable_irq against its own threaded handler) is not supported; the wheel driver is unchanged. The I2C bus numbers also swap between boots (this boot 11007000.i2c is i2c-1). 12 turns async device suspend off by default (kernel/power/main.c, overlay 0067), so the 6.18 parent/child async scheduling cannot be waited on; /sys/power/pm_async can re-enable it. Whether this removes the stall is only knowable from repeated sleeps. |
| Charge completion | CHANGE, host-tested | The system log shows the charger stopping at 4.175 V under load and the pack resting at 4.09-4.10 V; the 4.11 V recharge rule then restarted charging every ~70 s with full=0, all day. Full is now declared when a completing hold rests at or above 4.07 V for six samples; otherwise charging resumes; a maintenance cycle starts below 4.00 V. The 4.175 V stop, 4.2 V fault, current, timers and all protections are untouched, and the pack is charged no higher than before. |
| Battery percentage | CHANGE, host-tested | Full now reads 100% from 4.0 V up (it required 4.16 V, which this charger never leaves the pack at). After unplugging, the existing rate limit lets the estimate fall to the voltage curve (about 94% at 4.09 V) at 1% per minute; the curve itself is unchanged. |
| Wi-Fi, display, storage, USB, radio | UNCHANGED | No source change. |
| Physical | NOT_RUN | Nothing above is observed on hardware. |

Gate decision: build candidate 12 as 11 plus these two changes. After the owner flashes: read the charger state while plugged in (expect `Full` within a few minutes at ~4.09 V) and run repeated unplug sleeps. Stall rate before 12 is unknown, so one passing sleep does not prove the fix. Readiness for the next boundary: PARTIALLY READY.

## POWER-FINAL-13 stock suspend power-parity scope audit — 2026-10-11

Boundary: a material hardware-scope change (PMIC sleep voltage, storage-rail low-power mode, USB PHY power-down, wheel controller sleep) after real evidence from candidate 12: the first full night of synchronous suspend (archive 97: 34 kernel suspends, 33 clean maintenance wakes, no stall, ~2.2 points/h voltage-derived) and the stuck second boot (archive 98: every sleep refused for 4.2 h, 78% to 56%). Repeated before source changes; this audit builds and flashes nothing. The owner asked for the golden-master table and the most power-optimal deep sleep (target ~0.1 points/h, the owner's recollection of stock at about 1% per night). Reference: the Y2's own stock FM kernel (`evidence-private/20260908-ram-map/fm-decompressed.bin` + `fm-symbols.json`), not a generic vendor tree.``````````````````````````````````````

| Row | Classification | Evidence and limit |
| --- | --- | --- |
| Sleep guard (Defect A) | CHANGE, host-tested | The reconnect daemon holds /run/y2/bt-operation.lock after a Power wake; bluetooth-power off refused, result 1 left product-sleep-guard.json pending, and admission matched it by build identity, so sleep was refused across reboots (archive 98). Radio quiesce now retries within 25 s; the guard is cleared whenever the kernel was not entered and only a record with kernel_entry quarantines. |
| PMIC golden master | RESEARCH | Stock PMIC_INIT_SETTING_V1 (0xc04b81f8, E2) decoded field by field (~80 writes); 55 differ from the live 12 PMIC dump (archive 99). Stock mt6323_power_gs_suspend_data / mt6582_power_gs_suspend_data extracted. Data: docs/validation/data/y2-stock-suspend-golden-20261011.json. |
| VPROC sleep voltage | CHANGE, host-tested, highest electrical risk | Stock drops VPROC (CPU and SoC core) to 0.85 V via VOSEL_SLEEP when the SPM releases SRCLKEN; Y2 kept 1.15 V in software mode. 13 applies the eight stock fields only inside ->enter() around the PCM sleep, presets VOSEL_ON to the live selector, verifies the voltage is unchanged after the mode switch and restores every word (mode bit first) before the normal PCM returns. Non-fatal; pwrap.vproc_sleep switch. |
| Storage LDO LP_SEL | CHANGE, host-tested | VMC, VMCH and VEMC3V3 get the stock LP_SEL bit (stock additionally removes VEMC3V3 in suspend; 13 does not). Enables stay unwritable; /sys/firmware/y2_pmic/lp_sel reverts. |
| USB PHY save-current | CHANGE, host-tested | Stock usb_phy_savecurrent (0xc04d98f0) runs whenever no cable is attached; Y2 only ever ran the recover half at boot. 13 applies the exact stock sequence in the y2-usb parent's noirq suspend (no cable, no session) and writes every byte back in recover order on resume; phy_savecurrent switch and counters. |
| APT32F wheel sleep | CHANGE, host-tested | Stock tpd_suspend/tpd_resume (0xc04a41c0/0xc04a3088): reg5=1 for firmware 1..19 (this unit reads 0x01), resume pulses GPIO56 reset then reg5=0. Y2 left the controller scanning. GPIO56 is admitted to the pin allowlist with the latch preset high. sleep switch. |
| Maintenance wake | CHANGE | 600 s to 1800 s (stock uses a dynamic battery-meter period); PCM watchdog stays timer + 30 s. |
| SoC golden diagnostic | NEW, read-only | golden attribute on the SPM device: 34 stock golden rows (TOPCKGEN, INFRA/PERI clock gates, DRAMC, APMIXED PLLs) captured at every suspend entry. Decides the next step (PLL hardware control, DIS/MMSYS, clock gates) from evidence. |
| Not changed | UNCHANGED | eMMC supply removal, VGP2/DAC rail, panel deep-standby table, PLL/MTCMOS ownership, VSYS, AUXADC clocking/trims (would shift battery readings), PMIC low-battery interrupt, Reborn. |
| Physical | NOT_RUN | Nothing above is observed on hardware; no current measurement exists, so no mA or points/h claim. |

Gate decision: build candidate 13 as 12 plus these changes, each with a runtime switch for an A/B night. After the owner flashes: read `golden`, `vproc_sleep_state`, `phy_savecurrent`, the wheel `sleep` attribute and `y2_infra/state` after one unplugged 30-min sleep, then an overnight drain against 12's ~2.2 points/h. Readiness for the next boundary: PARTIALLY READY.

## POWER-FINAL-14 persistent sleep and USB diagnostics scope audit — 2026-10-11

Boundary: a diagnostics-only change after real evidence from 13. 13 was flashed and slept correctly once (archive 104: 12,104 s suspended, 6 maintenance wakes, Power wake, `complete_result_0`). The USB-after-wake defect (Defect B) then reproduced twice. The first time was at 18:39: the gadget was configured, but the host received 0 bytes. The second time was at 20:56: the host received 0 bytes and MTP also returned no storage, while the Y2's earlier Wi-Fi address still answered ping (not confirmed to be the Y2). Each time, the only recovery was a hold-Power restart. That restart erased every in-memory counter that 13 was built to report (`vproc_sleep_state`, `phy_savecurrent`, wheel `sleep`, `y2_infra/state`, the `golden` capture at sleep entry). The boot's syslog (two 256 KiB files) did not keep the night either. Without these values neither 13 nor Defect B can be judged. Repeated before source changes; this audit builds and flashes nothing.``````````````````

| Row | Classification | Evidence and limit |
| --- | --- | --- |
| Sleep feature counters | CHANGE, host-tested | At kernel suspend, kernel resume, maintenance wake, radio restore and completion/failure, the platform appends one bounded row to /data/system/platform/sleep-diagnostics.jsonl (2 × 2 MiB, private, fsync): the 13 switches and counters, y2_infra/state, the SPM state and golden (entry column), the USB/network snapshot, and a filtered kernel-log tail. Read-only sysfs; a failure never blocks or delays sleep. |
| USB/network snapshot | CHANGE, host-tested | UDC state, configfs gadget binding, usb0 operstate/carrier/IPv4 (from /proc/net/fib_trie), interface counters, the y2-usb controller summary and whether umtprd/dropbear run. Added compactly to every power-journal row, and written to the diagnostics file when the UDC state changes plus once 30 s later (at most one row per 10 s). This catches the moment a cable is plugged in after a wake. |
| Wi-Fi owner shell | NOT CHANGED, by design | SSH stays bound to usb0. A shell on the wireless network is outside the security scope. The persisted rows replace the need for it. |
| Kernel, drivers, sleep policy, Reborn | UNCHANGED | Only the identity string changes in the kernel. |
| Physical | NOT_RUN | Nothing above has been observed on hardware. |

Gate decision: build candidate 14 as 13 plus these diagnostics. After the owner flashes, repeat the unplugged sleep. If USB is dead after the wake, restart by holding Power and read the previous boot's rows from `/data/system/platform/sleep-diagnostics.jsonl` and `power-journal.jsonl`. Then decide the Defect B fix and the golden-based power step. Readiness for the next boundary: PARTIALLY READY.

## POWER-FINAL-15 dependency-update scope audit — 2026-10-11

Boundary: the owner asked for every software component on its newest upstream release, except Linux, which stays on the 6.18 long-term line. This is a material packaging/toolchain change with no functional goal of its own. Evidence for the gap: the 2026-10-11 version survey (release-monitoring.org, kernel.org, buildroot.org, Bootlin). The kernel is 6.18.0, 56 stable releases behind. The Buildroot 2025.02 line ended with 2025.02.18. Mesa is 24.0.9 and the Bootlin toolchain is 2024.05-1. Built on 14 (persistent diagnostics), which is flashed but not yet sleep-tested. Repeated before source changes; this audit builds and flashes nothing.````````

| Row | Classification | Plan and risk |
| --- | --- | --- |
| Linux | CHANGE | 6.18.0 → 6.18.56 (newest 6.18.y). Every overlay in kernel/patches must apply and the audited-source list is re-recorded for 6.18.56. Risk: stable backports touching MTK/MUSB/DRM/ASoC code that our overlays also change. |
| Buildroot | CHANGE | 2025.02.18 (line ended) → 2026.08 (newest release, not LTS). Already brings most packages to the newest version. The defconfig and external packages must be ported. |
| Packages beyond 2026.08 | CHANGE | OpenSSL 4.0.3 (major API change), Python 3.15.0 (released this month; cross-build patches), Mesa 26.2.4 (Lima), GLib 2.90.1, OpenSSH 10.6p1, util-linux 2.42.4, iproute2 7.2.0, SQLite 3.54.0, expat 2.9.0, exfatprogs 1.4.3, fdk-aac 3.0.0, iperf3 3.22, json-c 0.19, pcre2 10.49, procps-ng 4.0.7, strace 7.2, CA certificates; the existing pins are kept (BlueZ 5.87, SBC 2.2, bluez-alsa 5.0.0, Dropbear, FFmpeg 9.0.2, wireless-regdb). Each pin is hash-checked in modernize_buildroot.py. |
| Toolchains | CHANGE | Bootlin armv7-eabihf glibc stable 2025.08-1 (in 2026.08) → 2026.08-1. Rust 1.90.0 → 1.99.0 (Reborn, with any new strict-Clippy findings fixed). Kernel build sandbox: Alpine 3.22.1 → 3.24 with its LLVM/Clang. |
| Rust crates (Reborn vendor/) | NOT CHANGED | They are pinned by Cargo.lock. Major crate updates change APIs and are a separate step. |
| Behaviour | UNCHANGED by intent | No platform, sleep or UI change. Any change forced by a new API is recorded with the commit that makes it. |
| Physical | NOT_RUN | GPU (Mesa/Lima), audio, Bluetooth, Wi-Fi, USB/MTP, SSH and sleep all need re-checking on the device. |

Gate decision: build 15 as 14 plus these updates, as one candidate. If a component's newest release cannot be built or breaks a test, report it and keep the newest version that works, rather than patching around it silently. After the owner flashes: read-only check, then the 13/14 sleep test, then display, audio, Bluetooth, Wi-Fi, MTP and SSH. Readiness for the next boundary: PARTIALLY READY.

## POWER-FINAL-16 stock sleep-parity scope audit — 2026-10-12

Boundary: the owner set the goal for 16: fix what is broken on 15 and reach the best possible deep sleep, ≈0.1 points/h (stock parity, ≈1 % per night), completing the golden table, using REA for the stock analysis. Hardware evidence: 15 flashed 2026-10-12 00:33 (boot `e2952adf`, kernel `6.18.56-y2linux-platform-v1-power-final-15`, build `be1aac2`); overnight archive 108 (16/16 clean sleeps, ≈1.6 points/h voltage-derived, Defect B) and afternoon archive 109 (boot `bbea610d`; 6.3 h awake on a powered-off PC's port without sleeping or charging, then one clean 14-min sleep and Defect B again; owner hold-Power restart → boot `ff5243d9`, healthy). Stock analysis: `docs/knowledge/stock-suspend-re-ledger.md` (REA/Ghidra on the Y2's own FM kernel). Repeated before source changes; this audit builds and flashes nothing.````````````````````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| Suspend floor | GAP, measured indirectly | ≈1.6 points/h asleep vs target ≈0.1 (≈20 mA vs ≈1.3 mA on the 1300 mAh stock model). Maintenance wakes cost 0.14 % duty (2.6 s per 1800 s), so the floor while suspended dominates. No current sensor; every figure is voltage-derived. |
| SPM arming | MATCHES STOCK | REA F1: our y2_spm_suspend_arm sets the same SPM_CLK_CON/PCM bits as stock spm_kick_pcm_to_run. INFRA last_lost=0x0 must come from active requesters, not the kick. |
| Display power domain (G1) | GAP, planned | REA F2: stock powers DIS off at screen-off (mtkfb_early_suspend → disp_path_clock_off → clock manager → spm_mtcmos_ctrl_disp). Y2 never does; sleep rows show DIS on (power=0x314c). Plan: DIS genpd with the exact stock sequence, attached to the display pipeline; releases MMPLL/VENCPLL. Risk: display is the first physical risk (dark panel → hold Power, fallback 15). |
| INFRA power-down (G2) | GAP, investigation | Identify what keeps INFRA requested after G1 (SRCLKENA requesters, MSDC/USB bus masters). Read-only first. |
| Golden rows (G3) | GAP, staged | 26/34 SoC rows differ at entry (unchanged 14→15). One group per candidate with a runtime switch: INFRA/PERI gates + PERI MD1, DCM, CLK_CFG mux PD, MSDC/audio/thermal clocks. |
| DRAM (G4) | GAP, last | Stock lowers MEMPLL at screen-off (mt_h2l_dvfs_mempll); DRAMC+0x1dc golden row. Highest risk; only after G1–G3. |
| PMIC golden (G5) | GAP | 44 PMIC rows, VEMC3V3/VGP2, panel deep standby, BAT_L interrupt instead of timer wakes. Read-only comparison needs the probe (owner consent). |
| Defect B (USB after wake) | DEFECT, reproduced 3× | Diagnostics first (full MUSB+0x200 and DMA channel registers), then re-arm the DMA unmask after restore; host test. |
| Defect C (no sleep, no charge on unconfigured VBUS) | DEFECT, new | Archive 109: udc=default, charger INHIBITED, 106 refusals charger_or_usb_active, 75 %→32 %. Sleep policy must admit suspend when no host is configured and nothing charges. |
| Minor | DEFECT | Python 3.15 /dev/kmsg flush EINVAL; power journal keeps ≈4.5 h only. |
| Physical | NOT_RUN | Nothing above is changed or observed on hardware yet. |

Gate decision: 16 is a staged milestone. Candidate 16a: Defect B diagnostics+fix, Defect C, minor fixes and G1 (DIS domain) behind a runtime switch, plus read-only INFRA-requester diagnostics. Then G3 groups and G4/G5 in later candidates, each with an A/B night. No live register or sysfs writes without the owner's OK. Readiness for the next boundary: PARTIALLY READY (G1 and the defects are specified; G2/G4 need more analysis).

## POWER-FINAL-17 sleep-floor and wake-latency scope audit — 2026-10-13

Boundary: the owner set the goal for 17: stock sleep parity, ≈0.1 points/h (≈1.3 mA), with deep suspend and resume working every time; and on 2026-10-13 asked for a faster wake (screen first, radios restored afterwards). Hardware evidence: 16 installed 2026-10-12 (kernel `6.18.56-y2linux-platform-v1-power-final-16`, build `a4e9c3b`), first checks on boot `0b0e8a77`, overnight archive 110 (boot `f871fd6a`, taint 0): 16 h unplugged, 33/33 clean sleeps, USB worked after the replug, drain ≈8.6 mA on the stock curve (least-squares on the maintenance-wake estimates after 2 h of post-charge relaxation). Published as tag `baseline-16`. This audit builds and flashes nothing.````````````````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| Suspend floor | GAP, measured indirectly | ≈8.6 mA vs ≈1.3 mA stock (15: ≈10 mA). No current sensor; voltage-derived on the stock fuel-gauge curve. |
| MD1 requests (ledger F11) | GAP, ready | PERI_PDN0_MD1_STA=0 at all 33 entries, stock golden all gated. AP write proven harmless live on 16. 17: gate at application_ready (spm.md1_gate, owner switch md1_gate), re-check at every sleep entry, readback in state. Main suspect for INFRA never powering down. |
| INFRA power-down | GAP, investigation | last_lost=0x0 on all 33 restores. Re-read after the MD1 gate; if still 0, the remaining requesters (SRCLKENA, PCM R13 bits, MD_MASK 0x38 = 3). |
| MMSYS DCM, DMA-unmask readback | FIXED IN SOURCE (d1953fa), not built | Rides along in 17. |
| PMIC golden (15/44), SoC golden (11/34) | GAP, staged | Unchanged on the night; next candidates after the MD1 night, one group per A/B night. |
| Wake latency | GAP, measured | Archive 110 morning wake (kernel clock): SPM return 217.92 → PM: suspend exit 218.15 → kernel_resumed record 218.47 → radios 218.88–220.50 → Reborn sleep_restore and DSI modeset ≈220.45. The screen waited ≈1.9 s for Wi-Fi/Bluetooth firmware and calibration. 17: the helper asks Reborn to restore the screen before the radios; the completion record reuses that acknowledgement (a failed early restore is retried as before). Expected screen ≈1 s after Power. Further steps (panel deep standby, leaner resume records) after measuring 17. |
| Defect B | WATCH | 2/2 good wakes on 16; cause of the fix still unproven. |
| Physical | NOT_RUN | Nothing above is observed on 17 hardware yet. |

Gate decision: 17 = MD1 gate + screen-first wake + the two 16 follow-ups, each behind a switch or with the old order as fallback (`{"md1_gate": false}`). Then one A/B night against 16's ≈8.6 mA. Readiness: READY for the 17 build; PMIC/SoC golden writes stay planned.

## POWER-FINAL-18 PMIC suspend-field scope audit — 2026-10-13

Boundary: the owner asked for 18 with every PMIC change proposed after the INFRA requester analysis (ledger F14–F16). Hardware evidence: 17 installed (boot `de37f6bc`, archives 111/112): first boot healthy, an 18-min sleep clean, modem requests gated, INFRA still retained (`last_lost=0x0`); 16's night ≈8.6 mA (archive 110). REA on the stock kernel: the SoC/SPM side is stock-identical; all 15 differing PMIC golden rows are mapped to stock fields. 17's overnight drain is not measured yet, so 18 is not an A/B against 17 alone. This audit builds and flashes nothing.````````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| PMIC audio clocks | GAP, ready | rg_clksq_en_aud (0x102[0]) stays 1 in Linux (bootloader value, never written); stock clears it with no analog audio user and in AudDrv_Suspend_Clk_Off. rg_adacck_en (0x70c[4]) 1 vs stock 0. 18: stock value inside the SPM enter, exact restore before resume (group 1). Audio uses the external CS43131 over I2S; check playback after every wake. |
| Unused PMIC clocks | GAP, ready | 0x108 drv_2m/rtc_mclk/efuse clock PDN, 0x10e auxadc_ctl clock PDN: gated in stock suspend (group 2). |
| VREF18 | GAP, ready | 0x776/0x778 rg_vref18_enb(_md) 1 in stock (pmic_early_suspend). Group 4. |
| Headset-detect clock | NOT A GAP | 0x108[9]: Linux already gates it; stock keeps it running. Not changed. |
| VEMC3V3 off | BLOCKED | Overlay 0029 retains the root eMMC powered in TRAN state across suspend (no CMD5, no re-initialisation; the storage firewall blocks the commands a re-init needs). Cutting its supply would break the next root access. Needs an eMMC suspend-model change first; separate storage work with data risk. |
| VPROC sleep rows | ALREADY DONE | 0x212/0x216/0x21c/0x230 are set by 13's VPROC step after the capture; 18 moves the PMIC capture after both steps so the golden comparison shows the real sleep state. |
| AUXADC hw modes, VSYS/VPA sleep, depop VCM | NOT ADOPTED | Battery readings / unclear benefit; kept for later. |
| Refusal reason | DIAGNOSTICS GAP | 17 lost the reason of two refused requests; the journal now keeps suspend.reason/error. |

Gate decision: 18 = PMIC groups 1/2/4 behind `pwrap.pmic_sleep` (owner switch `pmic_sleep`, default 7) + journal reason. Readiness: READY for the build; physical risk is low (every write is restored before any device resumes; a failed write undoes itself and sleep continues unchanged).

## POWER-FINAL-19 PMIC_WRAP clock gate scope audit — 2026-10-13

Boundary: after 18's 1-h sleep (archive 114: PMIC fields applied/restored 3/3, PMIC golden 15 → 7, INFRA still retained) the only INFRA gate still different at sleep entry is bit 23, the AP's PMIC_WRAP clock (ledger F17). Stock gates it in suspend (and in awake video playback). Owner-authorised live test on 18 (boot `69ef8c26`): gating it makes the AP-side wrapper read as 0 (WACS2 -EIO), no bus hang, fully reversible. The owner asked for 19 right away; 18's overnight drain is postponed. This audit builds and flashes nothing.``````````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| PMIC_WRAP clock in sleep | GAP, ready | Gate INFRA_PDN_SET bit 23 after the last AP PMIC access in y2_spm_enter (after VPROC/PMIC steps and the PMIC capture), right before y2_spm_suspend_arm; ungate (CLR, verified, 3 tries) right after cpu_suspend returns (after the backstop re-arm, before the INFRA restore) and again on the arm-failure path, both before any PMIC/VPROC restore. Switch spm.pwrap_gate, owner switch pwrap_gate (default on). Never takes over a gate it did not set. |
| Risk | ACCEPTED (owner) | If the PCM itself needed the AP-gated wrapper, a sleep could stall; the 30-s RGU backstop resets, the night's persistent rows record it, {"pwrap_gate": false} or the 18 fallback recover. Stock sleeps with the same PCM and this clock gated. |
| INFRA power-down | GAP | The key read after 19's first sleep: last_lost. |
| Physical | NOT_RUN | 18's boot is tainted by the probe; hold-Power restart before any sleep. |

Gate decision: 19 = PMIC_WRAP clock gate for the PCM sleep only. Readiness: READY for the build.

## POWER-FINAL-20 UART1 clock reclaim scope audit — 2026-10-13

Boundary: 19's 47-min sleep (archive 116): the PMIC_WRAP gate worked 2/2 and INFRA_PDN_STA at the kick equals the stock golden exactly, yet INFRA stays retained (`last_lost=0x0`). The only peripheral gate still different from stock at sleep entry is PERI_PDN0 bit 17, UART1 (ours 0x2fcffff vs 0x2feffff). The owner asked for 20 with this before the next tests. This audit builds and flashes nothing.````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| UART1 clock | GAP, ready | No Linux owner (no DT node). Boot handoff (clocks.unused_handoff, 19): lcr=0 ier=0 lsr=0x0 dma=0 reason=tx_not_drained retained=1 — the all-zero register set of a never-initialised UART failed the THRE/TEMT check; UART2/3 read the normal 0x60 and were gated. Stock gates UART1 in every scenario checklist (idle, deep idle, suspend). 20: an all-zero LCR/IER/DMA/LSR set counts as never initialised and the clock is reclaimed by CCF unused-clock handling like UART2/3; any non-zero field keeps the old rule. Every UART1 register read in the kernel is already conditional on its clock being on. |
| Side effect | EXPECTED | The deep-idle owner check reported UART1_sleep_unknown for the same reason; with UART1 gated it no longer applies. |
| INFRA power-down | GAP | Read last_lost after the first 20 sleep. If still 0 with every SoC clock gate at stock, question the premise (stock restores only the UART after INFRA power-down) and rely on the measured drain. |

Gate decision: 20 = UART1 reclaim. Readiness: READY for the build.

## POWER-FINAL-21 quiet display power transitions scope audit — 2026-10-13

Boundary: owner report on 20: the startup sometimes flashes colours; after the shutdown animation the panel turns white or shows colours. Analysis (no device writes): the panel driver linked the backlight to DRM (`drm_panel_of_backlight`), so every pipeline enable called `backlight_enable()` and reset `bl_power` to on. At shutdown Reborn ends on a black frame with the light off and is killed; when its DRM file closes, the core restores the stale fbdev buffer and enables the pipeline, which re-lit the panel over white/console content (the platform's `bl_power=4` can land before that close: a race, hence "sometimes"). At boot the splash's first `SetCrtc` fully re-initialises the DSI link (`modeset: PHY/clocks ready, initialize DSI`, ≈0.48 s) while LK's picture is lit. Reborn already owns the backlight explicitly (screen sleep/wake, shutdown), the offline charger writes `brightness` itself. This audit builds and flashes nothing.````````````````````

| Row | Classification | Plan |
| --- | --- | --- |
| DRM-coupled backlight | DEFECT | Drop drm_panel_of_backlight; the backlight is owned only by explicit bl_power/brightness writers. |
| Lit panel during power-off | DEFECT | y2-backlight.shutdown switches all four ISINKs off (0x356[3:0]=0) in device_shutdown. |
| Boot modeset with lit panel | DEFECT (probable) | Splash: bl_power=4 immediately before its SetCrtc, bl_power=0 after two vblanks, unconditionally (a failed modeset never stays dark). LK's own panel init cannot be changed. |
| Sleep/power | UNCHANGED | 21 = 20 + these three; sleep tests can run on 21. |

Gate decision: READY for the build.

## POWER-FINAL-22 DSI hand-over backlight scope audit — 2026-10-13

Boundary: owner on 21: the white/colour screen after shutdown is gone; the colour flash between the bootloader logo and the Reborn splash remains. 21's boot log (archive 118, boot `a0c4d60e`): DSI hand-over "park video" at 0.489 s (LK's stream stops), Linux's first DSI modeset from the fbdev client at 0.532 s, the splash's first frame at 0.642 s. The lit panel has no video stream for ≈40 ms; 21's splash-side darkening came after the modeset and could not help. This audit builds and flashes nothing.``````

| Row | Classification | Plan |
| --- | --- | --- |
| Hand-over with lit panel | DEFECT | mtk_dsi overlay 0017: before "park video", switch the panel's backlight (DT backlight phandle) off; relight 50 ms after the first Linux atomic_enable, with a 3-s fallback and a devm release that relights on unbind/probe failure. Only if it was lit. |
| Splash darkening (21) | KEPT | Harmless; covers a splash-first modeset. |

Gate decision: READY for the build (overlay hash regenerated with `refresh-overlays.py`).

## POWER-FINAL-23 Reborn Cover Flow and Genres scope audit — 2026-10-13

Boundary: owner request: Cover Flow for albums ("people really want a cover flow"), highly optimised (smooth scrolling, an animation opening the album), and Genre in the main list. Owner decisions: Albums opens Cover Flow with a Grid option in Settings → Display; Genre → Albums (headed by All Songs) → Songs. Reborn-only change; the platform image is 22 unchanged. This audit builds and flashes nothing.``````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| Genre data | NEW | reborn-media already parsed the genre tag; the library now stores it (additive column, METADATA_REVISION 3 → every older row re-reads its tags once on the next scan, no rebuild). |
| Navigation | NEW | Home/Music: Genres (seven home rows; spacing follows the count). Genre → Albums (genre: filter, All Songs first) → Album/Songs; untagged songs as No Genre. |
| Renderer | EXTENDED | Quad.warp: perspective-correct quadrilaterals with per-corner tints (texture2DProj, q from the diagonal intersection). Boxes render bit-identically to 22 (host GLES harness, max difference 0); all 77 preview screens match the reference rasteriser. |
| Cover Flow | NEW | Projected 3D covers with reflections, time-based glide (≈0.4 s to rest), centre cover at 160 px from the artwork worker once at rest, flight into/out of the album page (300 ms). |
| Device performance | NOT_RUN | Frame times on the Mali-400 must be measured (graphics_frame_time_ms gauges, screen capture). |

Gate decision: READY for the build.

## POWER-FINAL-25 Reborn Cover Flow frame rate and card hygiene scope audit — 2026-10-13

Boundary: handoff items 1 and 2, owner-approved: Cover Flow toward the panel's rate, sub-minute album lengths, and a scanner that ignores macOS card metadata. Reborn-only change (`ed6a8cb`); the platform image is 24 unchanged apart from the release identity. This audit builds nothing and flashes nothing.````````````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| Frame pacing | CORRECTED | 24 measured 27 fps median / 31 max: the render gate still required 34 ms between frame starts, so presentation (synchronous page flip) landed on every 2nd/3rd vblank. While Cover Flow glides or the cover flies, the gap is 12 ms and the vblank paces frames; spinners and fades keep 34 ms. |
| CPU during the glide | EXTENDED | The existing Interactive lease (750 MHz floor, 250 ms) is renewed while gliding. No kernel workload policy change. |
| Per-frame work | REDUCED | Host profile, 3000 tracks: ui.draw 0.033 ms/frame, two thirds the album detail line (all-track scan); now cached per album and library. |
| Album length | CORRECTED | Albums under a minute show m:ss instead of "0 min". |
| Scanner | CORRECTED | ._* AppleDouble files and .Spotlight-V100/.fseventsd/.Trashes/.TemporaryItems are skipped; 11 such files on the owner's card made every scan incomplete and blocked pruning. Test covers an unreadable .Spotlight-V100. |
| Device performance | NOT_RUN | Re-measure with the 40-s metrics sampler and a capture after the flash. |

Gate decision: READY for the build.

## POWER-FINAL-26 Reborn Bluetooth codec auto-selection scope audit — 2026-10-13

Boundary: owner request: enable every implemented Bluetooth codec so automatic negotiation selects the best one. Reborn-only change (`1c9edd4`); the platform image is 25 unchanged apart from the release identity. The platform already starts BlueALSA with AAC, aptX, aptX-HD and LDAC (`/run/y2/codec-runtime.json`, owner-private integration profile). This audit builds nothing and flashes nothing.``````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| Runtime codec discovery | CORRECTED | Live on 25: org.bluealsa.Manager1.Codecs = A2DP-source:SBC/AAC/aptX/aptX-HD/LDAC; Reborn stripped only a2dp-source:, so every codec (SBC included) was runtime_enabled=false, policy Failed: no_eligible_codec…, codec row hidden. Prefix now case-insensitive. |
| Default preference | CHANGED | Auto (ranking LDAC → aptX-HD → aptX → AAC, SBC fallback, only mutually usable codecs, only while the PCM is idle). Saved SBC from before codec revision 1 migrates to Auto once. |
| Peer evidence | OBSERVED | AirPods Pro: mutual SBC and AAC; BlueZ had negotiated AAC by itself. Auto should request AAC. |
| aptX / aptX-HD / LDAC on a real peer | NOT_RUN | Needs headphones that advertise them. |

Gate decision: READY for the build.

## POWER-FINAL-27 stock sleep-parity gaps C, A, B scope audit — 2026-10-14

Boundary: owner request after the 26 night (archive `20261014/124`, 21/21 clean, ≈8.3 mA whole-night, relaxation-limited) and the read-only remaining-gap audit (ledger F18–F27): build 27 with gaps C (panel), A (VGP2) and B (VSYS). Gap D (VEMC3V3) stays out (storage model). Platform-only change; Reborn unchanged (`1c9edd4`). Each change has its own switch whose kernel default is 26's behaviour and which `power_features` arms at `application_ready`; the owner disables one with `/data/system/platform/power-features.json`. This audit builds the image; it does not flash it (the owner flashes).````````````````````````````````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| C Panel power-down | CHANGED (switch panel_stock_suspend, /sys/module/panel/parameters/stock_suspend) | Stock GC9503V lcm_suspend 0xc04a24f4, table 0xc09ff464: vendor pre-sequence, display off, sleep-in, 25 analog writes, then reset high 50 ms. 26: display off, sleep-in, reset low. Any DCS failure falls back to 26's sequence; prepare() still pulses reset and replays the full init. Risk: display wake; checked by every screen-on. |
| A VGP2 | CHANGED (switch vgp2_idle_off, /sys/module/y2_cs43131/parameters/vgp2_idle_off) | Stock: CS43131 is VGP2's only user; cs43131_power_down_hw drops GPIO15/18/20 then hwPowerDown(VGP2). DTS regulator-always-on removed; the card holds one reference unless the switch is set; the codec's runtime PM (upstream, unchanged) then disables VA/VP/VCP and VD/VL when idle. Risk: audio start after idle; checked by playback. DTB validator updated. |
| B VSYS buck | CHANGED (pmic_sleep group 8, default mask 7 → 0xf) | Stock PMIC_INIT (vendor pmic_mt6323.c 3417–3424, image init table): QI_VSYS_VSLEEP 2, VSYS_VOSEL_CTRL 1, slew rates, VSYS_TRANSTD 3, VOSEL_TRANS_EN 1, VSYS_VSLEEP_EN 1. Applied inside the SPM enter with the other PMIC sleep fields, mode bit last, restored exactly (mode bit first) before any resume. Only while VSYS is in software mode with VOSEL = VOSEL_ON = VOSEL_SLEEP = readback (live: all 0x40, 2.2 V), otherwise refused and counted (vsys_refusals); every VSYS selector stays unwritable, so the voltage never changes. PMIC write policy admits only these mode/slew bits (13 had kept VSYS closed; owner go 2026-10-14). Effect size unknown. |
| D VEMC3V3 | NOT_CHANGED | Needs eMMC power-off/re-init; separate milestone. |
| Effect on drain | NOT_RUN | No coulomb counter on this board (stock fgauge_read_* stubs). Night test should start ≥4 h after charging and run ≥12 h; per-gap A/B nights with the switches if the owner wants attribution. |

Gate decision: READY for the build.

## POWER-FINAL-28 stock battery percentage and top-off scope audit — 2026-10-14

Boundary: owner report on 27: on the charger the Y2 shows 100 %, after a restart about 80 %; wanted 100 % when really full, then 99, 98, 97 …, with REA. Owner chose the full scope including stock-style charging (2026-10-14). Analysis: ledger F28–F33 (`docs/knowledge/stock-suspend-re-ledger.md`), live 27 boot `5919b4fe` (read-only). Platform only; Reborn unchanged (`1c9edd4`). This audit builds the image; the owner flashes. **Charging change: materially changes charging behaviour (hardware scope) — the voltage ceiling, 4.2 V guard and every protection are unchanged.**``````````````````````````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| Top-off (finish stage) | CHANGED (charger-policy.h, mt6323-charger.c) | Stock: top-off at hardware CV until (ISENSE − BATSNS + offset) × 1000 / 68 ≤ 150 mA for 6 × 10 s (a 10.2-mV net sense drop) or 3 h. Y2 26: stops at the first 4.175 V sample (POWER-02 tripped the 4.2 V guard while charging on at full current against CV), rests ≈4.09 V (95 % on the stock curve). 28: the first 4.175 V sample at the normal current steps the cycle to the existing 70 mA selector; at 70 mA the cycle completes at 4.175 V or on the stock 10.2-mV taper rule (raw drop minus the measured zero-current offset). Target 4.175 V, hardware CV selector 30, 4.2 V fault guard, 3 h CV / 24 h / precharge timers, watchdog, OVP, thermal ladder: unchanged. Unknown current keeps 26 behaviour. |
| Recharge | CHANGED | Stock 4.110 V. 28: below min(4.110 V, last Full rest − 30 mV), never below 26's 4.00 V, so the 70-s loop (rest below 4.11 V) cannot return. |
| Boot OCV | NEW, read-only | BAT0 voltage_ocv = PMIC 0x724 latched at power-on (stock get_hw_ocv: raw × 7200/32768 + 8 mV, bit 15 ready), read once at probe. Live 27: 4062 mV vs 4002 mV first loaded sample. |
| Displayed percentage | CHANGED (battery.py, power.py) | Stock UI SOC: separate display value; charging shows at most 99 until Full; Full counts up 1 per 10 s to 100 and re-anchors (100 = the Full rest voltage's curve value); after Full 100 is held through maintenance holds/recharges until unplug; unplugged it only follows the estimate down (existing 60 s/point limit). The estimate itself (and remaining_uah_estimate) is unchanged; the display is estimate × 100 / anchor. |
| Restart | NEW | Stock keeps UI SOC in an RTC spare register and reuses it within 40 points (dod_init). 28: /data/system/platform/battery-ui.json (written durably on change), reused within 40 points of the boot estimate, which uses the power-on OCV unless a charger moved it by 31+ points (oam_init). |
| Effect | NOT_RUN | Needs one full charge on the device (charging_state finish/taper_samples/full_rest_uv, rest voltage after Full), then unplug/restart observations. |

Gate decision: READY for the build.

## POWER-FINAL-29 finish-stage and discharge-estimate corrections scope audit — 2026-10-14

Boundary: first device run of 28 (archive `20261014/126`, boots `8f43c71e`, `129e5611`). Owner-approved battery milestone continues (full scope chosen 2026-10-14). Platform only; Reborn unchanged (`1c9edd4`). Builds the image; the owner flashes.``````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| 28 works | OBSERVED | Power-on OCV start (89 % vs ≈81 % from the loaded sample); restart restored the saved display; finish stage entered at 4.175 V after 15 min at 450 mA, no fault; VSYS/pmic_sleep (27) 1/1 with last_changed 0x3ff. |
| 70 mA finish stalls | DEFECT → CORRECTED | At 70 mA the pack fell back to 4.09 V and stayed flat (ISENSE est. ≈90 mA; screen off, idle, awake on USB): the awake Y2 consumes about what 70 mA supplies; the 3-h top-off budget would have ended the cycle as a timeout fault. 29: steps 450/650 → 200 → 70 mA at successive 4.175 V samples; at 70 mA no 5 mV rise in 10 min completes the cycle (Full still needs the ≥4.07 V rest); the 3-h top-off budget completes a finishing cycle as stock BAT_TopOffModeAction does (total 24 h and precharge timeouts stay faults). 200 mA is a stock CS_VTH selector already admitted; target, guard and protections unchanged. |
| Display drift on battery | DEFECT → CORRECTED | 28 showed 89 → 85 within 3.5 min awake: the estimate moved toward the loaded-voltage SOC (≈50 mV, 4–5 points low under load). 29: on battery with continuous samples (≤60 s apart) the estimate follows stock oam_run: model current (OCV(SOC) − V)/R(V) integrated against Q_MAX 1300 mAh; after longer gaps (suspend; stock integrates raw-monotonic time) the rested voltage is used as before. The display stays down-only on battery. |

Gate decision: READY for the build.

## POWER-FINAL-30 database and file I/O performance pass scope audit — 2026-10-14

Boundary: owner request: a performance pass on the database and file reads/writes. Measured read-only on 29 (boot `cac3e209`) plus scratch-file timings under `/data/perf-probe` (removed) and page-cache drops. Platform-only kernel change; Reborn unchanged (`1c9edd4`). Builds the image; the owner flashes.``````````````````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| Library database | NO_CHANGE | 317 tracks, 393 KB, WAL + synchronous=NORMAL, keyset pages and covering indexes: query latency 2.7 ms; open+migrations+quick_check ≈56 ms, initial catalog ≈70 ms at start-up. |
| Warm rescan | NO_CHANGE | 311 reused files in ≈200 ms (db_us ≈120 ms in 5 probe transactions). Small absolute cost. |
| Session saves | NO_CHANGE | session.json (9 KB) atomic write with file + directory fsync: median 7.9 ms (1.0 ms without fsync) on the eMMC, only on user actions; durability kept. |
| Cold SD directory reads | DEFECT → CORRECTED | Start-up scan 6975 ms for 311 unchanged files (db_us 176 ms, no decoding); reproduced without boot load after a page-cache drop (7011 ms). find /media/sd -type d cold 7955 ms (118 dirs), warm 38 ms; raw card 85 MB/s sequential, 0.4 ms per scattered 4 KiB. One cold listdir = ~200 read requests of one 512-byte sector, 0 merged, ~50 ms. Cause: exfat_dir_readahead() (fs/exfat/dir.c) submits the 128 KiB cluster's 256 sectors unplugged; exfat_load_bitmap() already plugs its readahead. Fix: overlay 0068-exfat-dir-readahead-plug.patch adds blk_start_plug/blk_finish_plug around the loop (read path only; no format, write or mount-option change). Also helps MTP and folder browsing on the SD card. |

| FAT32 and ext4 cards | CORRECTED (owner: users bring every format) | `fat_dir_readahead()` (fs/fat/dir.c) has the same unplugged per-sector cluster readahead (FAT32 cards: 32 KiB clusters, 64 reads per cold directory); the FAT-table readahead in `fatent.c` already plugs: overlay `0069-fat-dir-readahead-plug.patch`. ext4 listings are already batched by block-device readahead (`ext4_readdir`); `ext4_bread_batch()` (directory lookups) submitted unplugged: overlay `0070-ext4-bread-batch-plug.patch`. Read path only. |

| Access-time writes | CHANGED | SD (all formats) and the internal Y2Media partition mounted `relatime`: the first read of each song per day wrote an access time to the card. Now `noatime`. |

| Pre-mount read-only check | NO_CHANGE | `fsck.exfat -n` on the owner's card: 315 ms cold (exfatprogs reads in large blocks). |

| FFmpeg decode pipeline | MEASURED | Owner follow-up: decoding performance. Stage benchmark built with the product toolchain against the image's FFmpeg (decode → canonical FLTP → `aformat`+`alimiter` graph → S16 output; wired output negotiates the source rate, S16, period 512 / buffer 4096), at 1.2–1.3 GHz, % of one core: 320k MP3 decode 1.3 / full pipeline 2.5; CD FLAC 0.9 / 2.1; 24/96 FLAC 2.1 / 4.6; AAC 256k 0.9 / 2.0. `alimiter` alone ≈ half of the pipeline; 3 EQ bands +0.8–1.7; resampling to 48 kHz +1.1–2.0. Decoders need no change. |

| Always-on limiter | CHANGED (Reborn `f08cf93`) | The player decodes at neutral user gain; the graph can only raise a peak with an active EQ band or a positive net gain (ReplayGain without a peak tag; with one the headroom already caps it at −0.1 dBFS). The limiter is now built only then: pipeline 2.5 → 1.5 % (MP3), 4.6 → 2.4 % (24/96), and loud masters are no longer limited above −0.18 dBFS. The output conversion saturates (tested). |

| ALSA period | NO_CHANGE | 512 frames (≈86 wakeups/s); user volume is applied at write time, so a larger buffer would delay volume changes. |

Gate decision: READY for the build.

## POWER-FINAL-31 metadata formats and folder-first artwork scope audit — 2026-10-14

Boundary: owner request: a pass on metadata decoding and supported formats; artwork from the album folder first, the embedded picture only when the folder has none. Reborn change (`0892bf2`); platform as 30 plus the release identity. Builds the image; the owner flashes.````````````````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| Formats (image FFmpeg 9.0.2) | MEASURED | Demuxers: aac, aiff, ape, flac, mov, mp3, ogg, wav, wv. Audio decoders: aac, alac, ape, flac, mp3/mp3float, opus, vorbis, wavpack, pcm s16/s24/s32/f32 (le/be). Image decoders: mjpeg, png, webp (+vp8). No image or network demuxer. |
| Extensions | EXTENDED | Library adds .m4b, .oga, .aifc (already demuxed/decoded). .mp4 stays out: a music video has no audio-only stream and would mark every scan incomplete. Not supported (would need new FFmpeg components): DSD (.dsf/.dff), WMA, ALAC-in-CAF, TAK, Musepack. |
| Tags | EXTENDED | FFmpeg's normalised keys for ID3v2, Vorbis comments, MP4 atoms and APEv2: title, artist (AIFF author), album, album artist (album_artist/albumartist, now also ALBUM ARTIST with a space as foobar2000 writes it), date/year, genre, track/disc, ReplayGain. METADATA_REVISION 3 → 4: every row re-reads its tags once. |
| Embedded artwork | NO_CHANGE | Attached pictures (ID3 APIC, FLAC PICTURE, MP4 covr, Ogg METADATA_BLOCK_PICTURE, APEv2) in JPEG/PNG/WebP up to 16 MiB. |
| Artwork order | CHANGED | Was embedded first, folder fallback (thumbnail worker and playback). Now the folder cover first, embedded only when the folder has none. Folder names by priority (any case, jpg/jpeg/png/webp): cover, folder, front, album, albumart, artwork; then Windows Media Player AlbumArt_{GUID}_Large / AlbumArtSmall; finally the only image in the folder. macOS ._* never counts. Thumbnail cache renamed (thumb2-), old files removed once, so existing thumbnails follow the new order. Playback's embedded-picture cache stays embedded-only. |
| Disc subfolders (Album/CD1/) | NOT_CHANGED | A cover one level up would need the pinned-storage sidecar API to open the parent directory; left for a later change. |

Gate decision: READY for the build.

## POWER-FINAL-32 deep idle during screen-off playback scope audit — 2026-10-14

Boundary: owner request: awake idle power pass with REA (ledger F34–F38); owner go for change 1 (deep idle during screen-off playback) and a wired screen-off playback test. Platform-only kernel/userspace change; Reborn as 31 (`0892bf2`). Builds the image; the owner flashes and tests.````````````````````````````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| Deep idle with the audio clock on | CHANGED (switch deep_idle_audio, /sys/module/clocks/parameters/deep_idle_audio, kernel default off, power_features arms it) | Stock dpidle_handler / clkmgr_idle_can_enter masks: INFRA 0xa080, AUDIO group unchecked; spm_dpidle_before_wfi moves only AUDINTBUS to 26 MHz and restores it. Y2 31 added INFRA bit 5 (AFE clock), so screen-off playback never deep-idled. 32 drops bit 5 when the switch is on; every other stock mask, MSDC, display, UART, topology, OPP and screen rule unchanged. deep_audio_entries counts admissions with the AFE clock on; sleep rows record both. |
| Risk | OPEN, device test | Audio DMA continues on the 26 MHz AUDINTBUS during the PCM program; underruns would show in Reborn's audio_xruns and be audible. Test: wired, screen off, Bluetooth off, ≈30 min; compare SPM dormant_entries/dormant_residency_us, SLIDLE entries, deep_audio_entries, audio_xruns. Off switch: {"deep_idle_audio": false}. |
| Bluetooth enabled-but-idle | NOT_CHANGED | Needs STP PSM + BTIF clock gating (stock stp_psm_*, btif_enter_dpidle); separate change after this test. |

Gate decision: READY for the build.

## POWER-FINAL-33 Reborn skins (themes) scope audit — 2026-10-14

Boundary: owner request: themes that give Reborn a totally different look (example: a classic click-wheel player), switchable in Reborn and addable on the device; the current UI stays the untouched default; steps 1 (engine, format, Classic proof) and 2 (every screen part, fonts from TTF, Settings picker, install from storage). Reborn change (`cfd21df` vendor, `e4b175b` skins); platform as 32 plus installing the shipped skins and the release identity. Builds the image; the owner flashes and tests. Steps 3 (web editor) and 4 (polish) not in scope.``````````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| Default look | NO_CHANGE (host-verified) | Without a skin screens::draw runs the old path; every reborn-preview state is byte-identical to Reborn 0892bf2 except Display (new Theme row). The skin texture slot is a 1×1 texel until a skin is chosen. |
| Renderer | CHANGED | Texture slot 8 = skin atlas (≤1024×1024 RGBA, uploaded on choice, released on Reborn, re-uploaded after a renderer restart); quads validated against its size. One extra texture name, no new shader. |
| Pictures | CHANGED | rb_media_image_file reuses the FFmpeg mjpeg/png/webp decoders at the picture's own size (≤480×360, bounded file read, no image demuxer, no network). |
| Skin files | NEW | Shipped: /usr/share/reborn/skins/classic (skin.json, 7 small PNGs, Open Sans Bold/Regular/SemiBold TTF + OFL). User: Themes/ (any case) in the internal music root (MTP Internal Storage) and the SD card root. Every named file must canonicalize inside its skin folder; size limits per file. The UI crate does no I/O (architecture guard); the app reads. |
| Settings | CHANGED | Settings.theme (serde default empty = Reborn), Settings → Display → Theme picker (rescans on open), live switch; a refused skin keeps the current look and says why; a missing skin at start falls back for the session; Reset settings returns to Reborn. Control op theme / `rebornctl theme [ID |
| Risk | OPEN, device test | Load time and memory on the Y2 (atlas ≤4 MiB RAM + texture), Lima texture upload, MTP folder copy, SD-hosted skin, live switch from the picker, sleep/wake with a skin active. |

Gate decision: READY for the build.

## POWER-FINAL-34 shipped skins, battery level, skin engine additions scope audit — 2026-10-14

Boundary: owner: "ship them all" (the 14 example skins tried on 33) and the battery-level fix. Reborn `116f942` (battery), `9a9c250` (font `charset`, `case: lower`, example skins), `5b69ef5` (all skins in `skins/`); platform as 33 plus the release identity. Builds the image; the owner flashes.``````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| Battery level in Reborn | FIXED | Since 29 the platform reports source: stock_oam; Reborn accepted only fuel_gauge/hybrid/voltage_estimate and showed no level (empty battery in Classic, no number in Reborn's look). Seen on the 33 device capture. |
| Shipped skins | CHANGED | /usr/share/reborn/skins: Classic + Nano Glass, Walkman, Terminal, Winamp, Paper, Big Type, Cassette, Neon Night, Zune, Mini Silver/Pink/Blue/Green/Gold (3.1 MB; Latin subsets of Open Sans/Noto, OFL texts in each skin and in legal-info). 13 of them loaded on the 33 device in 87–119 ms; Zune needs the 34 engine. |
| Skin engine | CHANGED | Font charset: ascii (large display fonts fit the atlas), text case: lower. Default look unchanged. |
| User copies | NOTE | The 13 trial copies in Internal Storage Themes/ are hidden by the shipped skins of the same name; the owner may delete them. |

Gate decision: READY for the build.

## OTA-35 full over-the-air updates through a Y2 recovery image scope audit — 2026-10-15

Boundary: owner request: users on Wi-Fi search for updates on the Y2 and install a full update (Y2Linux kernel, rescue, root and Reborn) without a computer; flashing the RECOVERY partition for this is approved. Owner decisions (2026-10-15, "yes to all"): (1) the device powers off and the user presses Power to enter the installer, and again to start the new system, while the warm-reboot display defect is fixed separately; (2) releases are hosted as GitHub Release assets of SchulzCode/Y2Linux; (3) installing needs the charger or at least 50 % battery; (4) an automatic daily check that only shows that an update is available, never installs; (5) the stock Android recovery is replaced by a Y2 recovery image after a backup. Material production-scope change: new device-side write windows (RECOVERY, MISC message block, BOOTIMG from recovery only) and a new SPFT row (RECOVERY).

Read-only evidence (archive `20261015/128-ota-entry-baseline`, device on 34, boot ID in the archive): installed LK (UBOOT `0x1d20000`, first 242440 bytes) is byte-identical to the analysed FM `lk.bin` (`bb1a93b4…964a`), so the static LK findings apply: `boot_mode_select` honours the MISC bootloader command `boot-recovery` and the RTC PDN1 recovery flag, has no recovery key, and checks both before charging mode. BOOTIMG prefix equals candidate 34 (`ee80a82c…c30c`). RECOVERY holds an intact stock Android recovery (`RECOVERY` ramdisk label, kernel lineage `b026b285…`, OriginalFirmware, not FM; region hash `b3389226…be26`), saved with UBOOT, BOOTIMG and MISC as `emmc-readback/*.bin`. MISC's Android message area (first 2 KiB) is all zero; LK's `ENV_v1` block at MISC+0x20000 is not touched by this work. Our kernel ignores LK's command line (`ATAG_DTB_COMPAT=n`) and takes `bootargs`/`initrd-end` from its own appended DTB, so a recovery image carries its own DTB. LK's boot mode is visible at `/sys/firmware/y2_boot/metadata`.``````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| Recovery entry | NEW, PHYSICAL_GATE | Normal system writes the 2 KiB MISC message (boot-recovery) only after checking that RECOVERY holds a Y2 recovery image; LK then loads RECOVERY on the next power-on. The request stays set until the installer's work is verified, so power loss re-enters recovery. RTC flag not used (lifetime unmeasured). |
| Y2 recovery image | NEW | Same zImage, own DTB (y2.recovery=1, own initrd end), ramdisk labelled RECOVERY, boot-image name Y2Recovery; initramfs = production rescue plus installer and progress screen. Fits the 16 MiB RECOVERY span. |
| eMMC write policy | CHANGED | storage-policy.h: kernel from BOOTIMG may write RECOVERY and the MISC message; kernel from RECOVERY may write BOOTIMG and the MISC message; neither writes its own image. ANDROID/USRDATA/FAT unchanged; everything else stays read-only. |
| Update contract | CHANGED | Manifest schema 2: BOOTIMG + Y2ROOT (+ optional RECOVERY) payloads; the kernel is no longer required to match. The installer backs up both and rolls back both. Schema-1 root-only rescue installation is retired (no device ever installed one). |
| Download | CHANGED | Default channel GitHub Releases; HTTPS redirects only to an allowlist; authenticity from the Ed25519 signature; payload hashes pinned by the signed manifest. |
| Reborn | CHANGED | Software Update page wording for power-off install, daily check result, battery gate. |
| Warm reboot display | OPEN (separate) | Software reboot leaves the panel dark (since 11). Not needed for OTA v1 (cold power-on only). |
| Hang before rescue | ACCEPTED RISK | LK has no try-once boot: a BOOTIMG that hangs before its initramfs runs needs SP Flash Tool. Mitigation: OTA BOOTIMGs are byte-identical to computer-flashed and checked candidates. |

Gate decision: READY for source work and a candidate build. Physical steps (flash RECOVERY with SPFT, first recovery entry, first OTA) remain the owner's; the agent never flashes.

## POWER-FINAL-44 dark recovery screen (DSI register reads lag) scope audit — 2026-10-16

Boundary: the 43 install with the owner's restart switch ran end to end without a Power press (53 s, health `Acknowledged`), the restart into the new system was lit, but the recovery's progress screen stayed dark (owner: "only the update display did not show with usb connected"). Read-only evidence: the recovery's kernel log on Y2DATA (`/data/logs/recovery-last.log`) and archive `20261016/143` (42 cold start with USB plugged in, dark, early hand-over at 0.49 s, display snapshot). No hardware or memory scope change; display driver and recovery script only.``````````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| Dark recovery screen | NEW (distinct from the restart wedge fixed in 43) | Both dark boots read the whole DSI register file shifted by one word (each read returns the previous read's data: vactive reads PSCTRL's 0x305a0, ld0 reads LCC). 143's snapshot vs the lit restart 147 differs in DSI only (77 words) plus one CPU-PLL bit; SMI larb0 idle, MMSYS gates, PHY, mutex identical. Real CON_CTRL reads 0 (DSI_EN lost): every mtk_dsi_mask() stored a neighbour's value. 144 (42 restart, the larb0 wedge) reads DSI correctly, so this is a second, intermittent failure mode; USB enumeration is not concurrent (5 s in 143). |
| Fix (44) | CHANGED | mtk_dsi_poweron() reads PSCTRL then VACT_NL after the timing setup; if VACT_NL is not the mode's vactive it power-cycles PHY and DSI clocks and repeats the setup (at most 3 times, logged). The hand-over logs the same read-back of LK's timing, to show whether the lag is inherited. The recovery saves y2_display_snapshot as /data/logs/recovery-display.txt. |
| Cause | OPEN | Why the register port lags is unknown (no vendor reference found yet). The retry is a mitigation that only runs when the lag is measured. |

Gate decision: READY for a candidate (44) delivered over the air; checked by the next restart-entered recovery (install or probe) with the owner's OK.

## OTA-46 update space guarantee and restart by default scope audit — 2026-10-16

Boundary: owner request after 45 (installed over the air, archive `20261016/149`): "does the update process also have a cleanup, so that we can guarantee there is always enough space for users to update?", then "build 46 with the cleanup … tag release … update this without cable … just wifi from git". No hardware or memory scope change; update manager, recovery script and Reborn's Software Update page. Publishing the first GitHub release is the owner's explicit instruction.````````````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| Cancelled package | GAP → CHANGED | 45 staging failed update_data_space_reserve: a cancelled package (57 MiB) stays in pending and counts against the check (package + root/4 + 96 MiB ≈ 281 MiB). Cancel and every new download now delete it first. |
| Full Y2DATA | GAP → CHANGED | No cleanup existed; the owner's player had 330 MiB of test logs. Before refusing, the update manager removes disposable data one entry at a time (/data/logs except the live and last-installer logs, rotated platform journals, finished qualification runs), first for the manifest, then for the payloads. Music, settings, library and rollback copies are never touched. |
| Rollback copies | CHANGED | The recovery deletes the previous copies before writing the new ones; the space check counts them as free. A failed backup ends Failed, which never restores. |
| Refusal | CHANGED | download.json carries needed_bytes; Reborn names the MB and says music is not affected (the old text asked to remove music, which is on another partition). |
| Restart | CHANGED | Restart into the recovery and back is the default (lit on 43 restart, 45 OTA); restart.json{"mode": "poweroff"} is the override. Low battery in the recovery always turns off (a restart would loop). Reborn: Restart and Install. |

Gate decision: READY for candidate 46, published as a GitHub release and installed over Wi-Fi from the channel.

## POWER-FINAL-47 DSI register read lag: display DCM scope audit — 2026-10-16

Boundary: 46 installed over Wi-Fi from the release (archive `20261016/150`, Acknowledged), but its recovery screen stayed dark. Its log narrows the read lag: at the hand-over LK's DSI registers read correctly (`vact=00000168`); at Linux's first modeset, 42 ms later, every read lags, and 44's three DSI clock/PHY power cycles did not clear it. In that window the mutex's first prepare applies MMSYS DCM, including group 1 (DSI engine/digital, DPI). Stock calls `dcm_enable` only from `mt_dcm_init` (and sysfs), when its display already streams; `bus_dcm_*` only around idle. Every lagged boot (143, 43's recovery, 150) is after POWER-FINAL-16 introduced the DCM; the older dark restarts read the DSI correctly. Not proven causal (no clean A/B yet).````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| DSI/DPI DCM | CHANGED | Group 1 keeps DCM off (0x1400012c/0x14000130 = 0xf, clear register untouched). Group 0 and SMI DCM unchanged. No power cost: with the screen on the DSI streams continuously, with it off DIS is powered down. |
| Evidence | CHANGED | Hand-over and read-back lines print the group-1 DCM register (dcm1=). |
| Probe | CHANGED | update probe-recovery follows the restart setting, so restart-entered recovery screens can be repeated without an install (the A/B test). |

Gate decision: READY for candidate 47; device qualification by repeated restart-entered recovery probes with the owner's OK.

## OTA-48 download screen: progress, speed, completion scope audit — 2026-10-16

Boundary: owner after downloading 47 over Wi-Fi: "rework the download screen … the animation is very laggy and it does not show progress and does not take the user back / says download is finished … show progress and download speed". Read-only evidence from that download (pending files and journal times): manifest 19:30:17, payloads done 19:30:35 (58.7 MB, ≈3.3 MB/s), queued 19:30:59 — 24 s of two full decoding checks (`check`, then `queue`) with nothing new on screen. Reborn: the platform refresh is skipped while any platform task runs (`busy.is_none()`), so the percentage never moved; the stage reply showed nothing; the spinner is a 48-step ring at the calm frame rate. No hardware or memory scope change.````````

| Row | Classification | Evidence and plan |
| --- | --- | --- |
| Live progress | CHANGED | /run/y2/update-progress.json (RAM, ≤4/s: bytes, 4-s speed, seconds left, phase) and /run/y2/update-check-progress from the queue's decoding check; per-MiB durable journal writes removed. |
| Check | CHANGED | One decoding check (the queue's; it keeps refusing a wrong-slot boot image) instead of check + queue: about 12 s less. |
| Priority | CHANGED | Download and check run at nice 10. |
| Reborn | CHANGED | Download screen: step, percentage, gliding bar, MB of MB, speed, time left; check step with its own bar; at the end the page turns to Ready to Install and a notice says so wherever the owner is. |

Gate decision: READY for candidate 48. The new screen first shows when 48 downloads the next release.

## RELEASE-49 firmware-free public images, one-time radio firmware from the owner's copy scope audit — 2026-10-16

Boundary: owner: "for release 49 … provide all the images in the release, so other developers have the one time flash setup", plus a written explanation of the recovery and why RECOVERY must be flashed once. Found while preparing it: `Y2ROOT` (and the OTA `rootfs.ext4.gz` of releases 46–48) contained the proprietary MediaTek radio firmware in `/lib/firmware/mediatek/mt6582` (Wi-Fi RAM code, Bluetooth patches, modem image, WMT config, two derived defaults); the readme forbids redistributing images that contain it, the build records `redistribution_permission_established: false`, and the owner has no permission. Owner decision 2026-10-16: remove those assets (done: 46–48 now carry no system image, notes added; firmware was never in Git) and make releases firmware-free with this install flow: flash the public images, then copy `system.img` from the Innioasis package into the player's `Firmware` folder over USB; the player extracts and checks the five files itself.``````````````````````

| Row | Classification | Plan |
| --- | --- | --- |
| Root image | CHANGED | No owner firmware in any image; /lib/firmware/mediatek/mt6582 is a link to /data/firmware/mt6582 (Y2DATA). Seal check: no firmware file in root or initramfs. |
| Existing players | NEW | The 49+ recovery copies the reviewed files from the old root to Y2DATA before it writes the new root (hash-checked); nothing for the owner to do. |
| New players | NEW | The platform watches Firmware/system.img on the MTP storages, reads the Android sparse ext4 image itself, checks the five files against the reviewed inventory (SHA-256), derives the two defaults like provision.py, installs them, deletes the copy and starts the radios. Reborn says what to do while the firmware is missing. |
| Public package | NEW | First-install package without the owner's SSH key (developers personalize Y2DATA with first_owner.py); release 49 carries it plus the OTA files. |
| Contributions | CHANGED | Merge Y2Linux #38 (cs43130 on-demand load measurement, two driver fixes; reviewed, builds, 718 OK) and Y2Reborn #6–#8. |
| Codecs | CHANGED | The public-distribution gate (privacy.public_distribution) also blocked AAC, aptX, aptX HD and LDAC. Owner decision 2026-10-16: public images carry SBC, AAC from fdk-aac-free 2.0.3 (Red Hat's stripped FDK, AAC-LC only, as Fedora ships after legal review; upstream wtaymans/fdk-aac-strippedstripped5, Ubuntu's pinned release tarball) and LDAC; aptX/aptX HD only in owner-private builds (build.py --public disables BR2_PACKAGE_Y2_CODEC_APTX). Codec inventory profile public; gate passes only that set. |

Gate decision: READY for candidate 49; publish only after the firmware migration and the copy flow work on the owner's player.

## BETA-1 (Baseline 50) first public beta: milestone gap audit — 2026-10-16

Boundary: owner: "push baseline 50 as the first beta release of Y2Linux/Reborn with all images needed and update all docs and the readme". Crossing from developer preview to a public beta is a milestone boundary (standing rule). Hardware evidence used (no new flash or device write for this audit): 49 installed over Wi-Fi from its public release (archive `20261016/153`: recovery kept the radio firmware, radios up from `/data/firmware`, recovery screen lit), the Firmware-drive install on the owner's player (archive 154), restart and restart-entered recovery (43–48, archives 147–151: five probes lit), over-the-air installs 37/38/45/46/47/48/49, sleep nights on 16 and 26 (≈8.6 / 8.3 mA).``````

| Area | State for a beta | Evidence / gap |
| --- | --- | --- |
| Install | READY | Public first-install package (49): one SP Flash Tool pass incl. the Y2 recovery image; radio firmware from the owner's system.img on the Firmware drive (owner-tested 49). Gap: the full path from stock on a second, untouched player has not been run. |
| Updates | READY | Signed GitHub releases, Wi-Fi check/download/install with restart, backup and rollback (≥ 8 device installs). Fixes since 49: a cancel no longer hides a newer release (Reborn 476e281); the firmware watcher re-checks and restarts the radios reliably (Linux d1f1195). |
| Display | READY with known rare issue | Restart fixed (43); DSI read lag still occurs (2 of 5 restart entries) but no longer darkens the screen (47). |
| Audio / Bluetooth | READY with gaps | Wired playback daily. Public codecs SBC, AAC (fdk-aac-free), LDAC; AAC with the owner's AirPods not yet confirmed; saved headphones not always reconnected after a wake. |
| Power | KNOWN GAP | Sleep ≈8.3 mA vs stock ≈1.3 mA; 27/32 measures not yet measured overnight. Beta notes say so. |
| USB | READY with gap | MTP/charging fixes; USB after deep-sleep wake not confirmed over many wakes. |
| Distribution | READY | No MediaTek firmware in any image; public codec gate; GPL sources (legal-info + Linux archive) attached. |

Gate decision: READY for Y2Linux 1.0.0-beta.1 / Reborn 1.0.0-beta.1 (Baseline 50, update sequence 5000) as a public beta with the gaps above stated in the release notes and readmes. Not a final 1.0: power parity, AAC confirmation and a second-device install remain.

## BETA-2 (Baseline 51) Bluetooth/Wi-Fi fixes: milestone gap audit — 2026-10-15

Boundary: owner: "fix everything, also add a automatic output reconission … do a full build and release as 51", version `1.0.0-beta.2`, "publish directly, i want to update only over ota in the future". A public release is a milestone boundary (standing rule). Hardware evidence used (read-only, no device write): archive `20261016/155` (Beta 1 overnight and morning wake), the live Beta 1 player on 2026-10-15 over USB SSH (AirPods Pro connected, AAC 44.1 kHz negotiated, reconnect `Connected`, 41 processes/min with the screen dark, DNS probe every 30 s), and the BTIF timeout lines of every archived system log (4 of 4 with RX `flag=0 valid>0`).````

| Area | State for Beta 2 | Evidence / gap |
| --- | --- | --- |
| Radio transport | FIX BUILT, device check owed | BTIF RX race reproduced by a host test that fails on Beta 1's handler; fix acknowledges first and drains until stable. Count radio-start timeouts over many wakes after the OTA install. |
| Bluetooth reconnect | FIX BUILT, device check owed | 10 s client deadline vs ~18 s BlueZ answer → Inhibited (155, 26 nights). Now 45 s, and 5.12 s page timeout from the HCI driver (logs the replaced value). Check: AirPods away at wake → not Inhibited; connect when taken out. |
| Audio output | NEW, device check owed | Reborn routes to Bluetooth headphones once per connection; jack otherwise; no jack detection on this board. |
| Wi-Fi | READY | No real link drops on 2026-10-15 (all disconnects were sleep). DNS re-check 5 min. Open: 7.5–22 s to Online after a wake; power save stays off (owner decision). |
| Power, display, USB, install | unchanged from BETA-1 | Sleep ≈9.4 mA (155) vs stock ≈1.3; wake_event_in_progress race open. |
| Distribution | READY | --public, no MediaTek firmware in any image, legal-info and Linux sources attached. |

Gate decision: READY for Y2Linux 1.0.0-beta.2 / Reborn 1.0.0-beta.2 (Baseline 51, update sequence 5100) as a public beta, published before its device check at the owner's request; the owed checks are listed in the [Beta 2 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-2.md). Next evidence boundary: the first OTA install of 51 on the owner's player. Not a final 1.0.

## BETA-3 (Baseline 52) Bluetooth quality and stability: milestone gap audit — 2026-10-15

Boundary: owner: "work on the bluetooth quality and stability improvements", then "publish this as beta 3 and new tag". Evidence (read-only, Beta 2 player with AirPods Pro): AAC 44.1 kHz at BlueALSA's 220 kbit/s CBR while the AirPods advertise VBR up to 256 kbit/s; a 60-s HCI capture at close range (median ack 46 ms, max 78 ms, ≤ 4 in flight); encoder ≈9 % of one core; WMT coexistence setting identical to stock; the controller's page timeout already 5.12 s. One live BlueALSA restart with test options was undone by the connectivity supervisor; a second was refused by the session's safety check (no further device writes).````

| Area | State for Beta 3 | Evidence / gap |
| --- | --- | --- |
| AAC quality | BUILT, device check owed | Afterburner, peer rate capped to one packet per frame; host-tested arithmetic; listening comparison owed. |
| AAC stability | BUILT, device check owed | Adaptive CBR rate (patch 0002) host-tested; range/Wi-Fi-load test with aac_abr_level owed. |
| SBC XQ | READY (owner choice) | Ungated; default unchanged. |
| Coexistence | NO CHANGE NEEDED | Stock shared-antenna setting already sent. |
| Power, display, USB, install | unchanged from BETA-2 | Sleep ≈9.4 mA vs ≈1.3 mA stock. |
| Distribution | READY | --public, firmware scan clean, sources attached or linked. |

Gate decision: READY for Y2Linux 1.0.0-beta.3 / Reborn 1.0.0-beta.3 (Baseline 52, update sequence 5200) as a public beta at the owner's request; next evidence boundary: the owner's OTA install and an AirPods listening/range check.

## BETA-4 (Baseline 53) internet radio: milestone gap audit — 2026-10-15

Boundary: owner: FM radio and internet radio for Beta 4, internet radio first; "yes publish so i can update and see on the device". A public release is a milestone boundary. Internet radio adds no hardware subsystem: it uses Wi-Fi, the existing decoder and `curl`. FM radio (MT6627 in the CONSYS combo; firmware from the owner's `system.img`; indirect audio path per the Y2Player 2.5 evidence) is a new hardware subsystem and gets its own audit before implementation.````

| Area | State for Beta 4 | Evidence / gap |
| --- | --- | --- |
| Internet radio | BUILT, device check owed | Host tests incl. reconnect through real curl; live directory + two real stations decoded on the host; player curl HTTPS verified. |
| Decoder security | UNCHANGED | FFmpeg --disable-network, file-only protocols; streams arrive through a pipe. |
| Bluetooth | unchanged from BETA-3 | Range hardware-limited (stock too); A/B tests (Wi-Fi off, Standard AAC) owed. |
| FM radio | NOT STARTED | New hardware subsystem: audit, owner-approved device experiments. |
| Power, display, USB, install | unchanged | Sleep ≈9.4 mA. |

Gate decision: READY for Y2Linux 1.0.0-beta.4 / Reborn 1.0.0-beta.4 (Baseline 53, sequence 5300) as a public beta; next evidence boundary: the owner's OTA install and radio use on the device.

## BETA-4.1 (Baseline 54) radio and Wi-Fi fixes: milestone gap audit — 2026-10-15

Boundary: owner, after installing Beta 4: "playback command queue full", Wi-Fi shown as unavailable after screen-off or sleep until restarted (radio and updates), "do 4.1". A public release is a milestone boundary. No hardware, memory or production scope change: fixes in Reborn's radio/Wi-Fi status handling and the platform's TLS clock check.````

| Area | State for Beta 4.1 | Evidence / gap |
| --- | --- | --- |
| Internet radio | FIXED, device check owed | Stop deadlock reproduced by a host test (hangs without the fix); Beta 4 Reborn log and zombie curl on the player. |
| Wi-Fi status | FIXED, device check owed | network.json ages up to 12.0 s measured with the screen dark (limit was 15 s); three owner Wi-Fi restarts after screen-off in the Reborn log. |
| Update clock | FIXED, device check owed | Monotonic-vs-wall comparison fails after any suspend over 60 s; host test simulates one hour asleep. |
| Bluetooth after wake | OPEN | Owner suspicion; no log evidence yet. |
| FM radio | NOT STARTED | Beta 5, own audit first. |
| Power, display, USB, install | unchanged | Sleep ≈9.4 mA. |

Gate decision: READY for Y2Linux 1.0.0-beta.4.1 / Reborn 1.0.0-beta.4.1 (Baseline 54, sequence 5350) as a public beta at the owner's request; next evidence boundary: the owner's OTA install and the device checks in the Beta 4.1 report.

## BETA-5 (Baseline 55) keyboard, search and UI pass: milestone gap audit — 2026-10-15

Boundary: owner: a full-screen button keyboard for every text entry and a UI pass, "push as beta 5". A public release is a milestone boundary. No hardware, memory, platform or production scope change: Reborn UI and input routing only (the platform image changes only by the Reborn package and the release identity). FM radio moves to Beta 6.

| Area | State for Beta 5 | Evidence / gap |
| --- | --- | --- |
| Keyboard and button routing | BUILT, device check owed | Host tests for layout, movement, pages, limits and router keyboard mode (held buttons, keyboard closed while held); previews in Reborn's look and skins. Repeat speed and comfort need the owner's hands. |
| Library search | BUILT, device check owed | Matching tests (word beginnings, accents, articles, offline tracks); previews. |
| UI pass | DONE on host | 95 preview states reviewed; capitalization, toast placement, power hold, password title fixed. |
| Beta 4.1 fixes | device check owed | Radio stop, Wi-Fi after screen-off, update after sleep. |
| FM radio | NOT STARTED | Beta 6, own audit first. |
| Power, display, USB, install | unchanged | Sleep ≈9.4 mA. |

Gate decision: READY for Y2Linux 1.0.0-beta.5 / Reborn 1.0.0-beta.5 (Baseline 55, sequence 5450) as a public beta at the owner's request; next evidence boundary: the owner's OTA install and the device checks in the Beta 5 report.

## BETA-5.1 (Baseline 56) live search and radio section: milestone gap audit — 2026-10-15

Boundary: owner: live search with a performance pass, a premium radio section with logos and details, A-to-Z with each country's top 10 on top; "yes" to publishing. A public release is a milestone boundary. No hardware, memory-model or platform change: Reborn only, plus a native image function in Reborn's media library (`rb_media_logo_file`, same decoders and bounds as covers) and outbound logo downloads by the player's existing `curl` (≤300 kB, http(s) only).``

| Area | State for Beta 5.1 | Evidence / gap |
| --- | --- | --- |
| Live search and index | BUILT, device check owed | 20 000-song host benchmark; tests for navigation into results. |
| Radio section and logos | BUILT, device check owed | Real directory logos tiled on the host (21/24); image built with the new native symbol verified in libreborn_media.so. |
| Logo downloads | NEW network use | Bounded size/time, http(s) only, cached; decoded by the existing image decoders. |
| FM radio | NOT STARTED | Beta 6, own audit first. |
| Power, display, USB, install | unchanged | Sleep ≈9.4 mA. |

Gate decision: READY for Y2Linux 1.0.0-beta.5.1 / Reborn 1.0.0-beta.5.1 (Baseline 56, sequence 5500) as a public beta at the owner's request; next evidence boundary: the owner's OTA install and the device checks in the Beta 5.1 report.

## BETA-6 (Baseline 57) playlists, pause in place, seeking: milestone gap audit — 2026-10-15

Boundary: owner: a playlist section ("yes" to publish as Beta 6), instant pause/resume and the seek error fixed. A public release is a milestone boundary. No hardware, memory-model or platform change; Reborn only. New: Reborn writes playlist files on Internal Storage and the SD card (atomic, only on the owner's edits) and holds an open, paused audio device for up to 3 minutes after Pause (released before sleep).

| Area | State for Beta 6 | Evidence / gap |
| --- | --- | --- |
| Playlists | BUILT, device check owed | Host tests (encodings, paths, edits, worker, UI); previews; 20k-entry benchmark. |
| Pause in place | BUILT, device check owed | Engine test: held pause writes nothing, never reopens; image contains the code. Whether the wired codec pauses itself shows in the log. |
| Seeking | BUILT, device check owed | Coalesced; no restart during a pending one. |
| Power while paused | WATCH | A held pause keeps the device open ≤3 min, released before sleep. |
| FM radio | NOT STARTED | Beta 7, own audit first. |

Gate decision: READY for Y2Linux 1.0.0-beta.6 / Reborn 1.0.0-beta.6 (Baseline 57, sequence 5600) as a public beta at the owner's request; next evidence boundary: the owner's OTA install and the Beta 6 report's device checks.

## BETA-6.1 (Baseline 58) Beta 6 fixes: milestone gap audit — 2026-10-16

Boundary: owner: Bluetooth resume silent and "Couldn't complete that" on skipping after Beta 6; Y2Reborn issue #15 / PR #14 ("yes do both and publish as beta 6.1"). A public release is a milestone boundary. No hardware, memory-model or platform change; Reborn only. New: a Bluetooth pause drains instead of pausing the PCM; a complete scan of an SD card marks its pre-CID rows deleted (database rows only, never files).``

| Area | State for Beta 6.1 | Evidence / gap |
| --- | --- | --- |
| Bluetooth pause/resume | BUILT, device check owed | Device log of the silent resume; drain/prepare path not yet heard on the device. |
| Skipping while starting | BUILT, device check owed | Runtime path has no host harness; device test. |
| SD duplicates (#15) | BUILT, host-tested | a_card_scanned_under_its_cid_id_retires_its_pre_cid_copy; owner's database has 2 such rows. |
| Playlist matching (#14) | MERGED | PR test plus existing matcher tests. |
| FM radio | NOT STARTED | Beta 7, own audit first. |

Gate decision: READY for Y2Linux 1.0.0-beta.6.1 / Reborn 1.0.0-beta.6.1 (Baseline 58, sequence 5650) as a public beta at the owner's request; next evidence boundary: the owner's OTA install and the Beta 6.1 report's device checks.

## BETA-6.2 (Baseline 59) clock, skins, Bunny Bow: milestone gap audit — 2026-10-16

Boundary: owner: PR #10 clock fitting all skins, optimised; skins updated for the day's screens; a cute pixel skin; "yes publish". A public release is a milestone boundary. No hardware, memory-model or platform change; Reborn and its skins, plus a licence entry in the Reborn package. New: one redraw per minute while the screen is on (no new wakeups).

| Area | State for Beta 6.2 | Evidence / gap |
| --- | --- | --- |
| Clock and Time Zone | BUILT, device check owed | Host tests (zones parse, DST, picker, status bar); per-minute caches measured on the host. |
| Skins for the newer screens | BUILT, device check owed | Previews of all 16 skins; Reborn's own look pixel-identical (110/110); shipped-skin test. |
| Bunny Bow | BUILT, device check owed | Loads without warnings (contrast included); previews; OFL font licence in legal-info. |
| Power | WATCH | One frame per minute with the screen on; none with it off. |
| FM radio | NOT STARTED | Beta 7, own audit first. |

Gate decision: READY for Y2Linux 1.0.0-beta.6.2 / Reborn 1.0.0-beta.6.2 (Baseline 59, sequence 5700) as a public beta at the owner's request; next evidence boundary: the owner's OTA install and the Beta 6.2 report's device checks.

## BETA-6.3 (Baseline 60) sleep while paused: milestone gap audit — 2026-10-16

Boundary: owner: Power while paused stayed awake ("finishing another task"); "yes" to publish. A public release is a milestone boundary. No hardware, memory-model or platform change; one Reborn runtime change (a held pause is released before a sleep request) and one log event.``

| Area | State for Beta 6.3 | Evidence / gap |
| --- | --- | --- |
| Sleep while paused | BUILT, device check owed | Device journal: four refusals activity_operation:808/reborn; cause in the report; runtime path has no host harness. |
| Pause in place | UNCHANGED otherwise | Still instant within 3 minutes; after a sleep request Play restarts at the same place. |
| FM radio | NOT STARTED | Beta 7, own audit first. |

Gate decision: READY for Y2Linux 1.0.0-beta.6.3 / Reborn 1.0.0-beta.6.3 (Baseline 60, sequence 5750) as a public beta at the owner's request; next evidence boundary: the owner's OTA install and the Beta 6.3 report's device checks.

## UI-V4 (Reborn Product UI v4) one strict system: milestone activation audit — 2026-10-16

Boundary: owner: since playlists, search and radio the UI "looks kind full", the default look is "still a little rough"; make it consistent, for listeners rather than developers, removing what users do not need. Activating a milestone is a boundary. Planning only: no build, flash or hardware experiment; no platform, memory-model or hardware-scope change. Evidence: device capture on Beta 6.3 (`baseline-59-2-gb20404c` running, Settings, matches the host render) and all 92 interactive `reborn-preview` states from Reborn `0ab9953`. Plan and owner decisions: [Reborn Product UI v4](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fui%2FREBORN-PRODUCT-UI-V4.md).``

| Area | State | Evidence / gap |
| --- | --- | --- |
| Visual consistency | PLANNED | Three focus styles, four button styles, cover accent outside Now Playing, four empty-state forms; rules fixed in the plan. |
| Home / navigation | PLANNED | Ten Home items; owner chose a Music submenu with a Home Menu pinning setting. Skins need a music layout. |
| Content trims, hints | PLANNED | Developer facts (codec, bitrate, ranks, free space) and permanent hint lines leave lists; hold menus name the actions. |
| Beta 6.x device checks | OWED | Unchanged; the Beta 6.3 report's checks still stand. |
| FM radio | NOT STARTED | Beta 7 moves behind UI v4; its own audit first. |

Gate decision: UI v4 ACTIVE at phase 0 (spec, preview fixture titles, "before" previews); phase 1 (components and tokens) is ready to start. Each phase ships as its own beta after host previews; next evidence boundary: the device walk-through with screen capture while the owner presses the buttons.

## BETA-7 (Baseline 61) UI v4 and two platform fixes: milestone gap audit — 2026-10-16

Boundary: owner: "commit everything and start the release build" after UI v4 phases 1–3 ("we do a new build after all ui work is finished"). A release is a milestone boundary. No hardware-scope or memory-model change: Reborn presentation only, plus a kernel resume callback (`thermal.c`) and a retry in the platform's sleep helper.``

| Area | State for Beta 7 | Evidence / gap |
| --- | --- | --- |
| UI v4 | BUILT, device tour owed | Phases 1–3 on the host: 479 tests, previews of 114 states and 16 skins by eye. Phase 4 = the owner's on-device tour with screen capture. |
| CPU thermal after sleep | BUILT, device check owed | Archive 156: zone disabled at 06:43 after INFRA power-down wiped the monitor; resume re-programs it. Check thermal_zone1 after a night. |
| Sleep refusal by BAT0 | BUILT, device check owed | Archive 156 10:31 and archive 155 06:38; bounded fresh-count retry with the Power/RTC/cable checks repeated; 3 host tests. |
| Overnight drain | MEASURED on 6.3 | ≈7.8 mA, 14 h; stock ≈1.3 mA remains the open gap. |
| FM radio | NOT STARTED | Now Beta 8; its own audit first. |

Gate decision: READY for Y2Linux 1.0.0-beta.7 / Reborn 1.0.0-beta.7 (Baseline 61, sequence 5800) once the build's checks pass; publishing waits for the owner's word. Next evidence boundary: the owner's OTA install and the device checks of the Beta 7 report.

## BETA-7.1 (Baseline 62) one-step update, USB screen, automatic time zone: milestone gap audit — 2026-10-16

Boundary: owner requests on Beta 7 (time zone list, late/missing and leavable USB screen, late update answers, a one-step update); "publish it when the build is done". A release is a milestone boundary. No hardware-scope or memory-model change: Reborn behaviour plus a SIGTERM path in the platform's download. New outward traffic: the automatic time zone asks ipapi.co (fallback ipwho.is) once per Wi-Fi network (owner decision), default only where no zone was chosen.````

| Area | State for Beta 7.1 | Evidence / gap |
| --- | --- | --- |
| USB screen latency/lock | BUILT, device check owed | Cause found on the device (status refreshed only on Settings screens; platform already Ready); live sysfs + RAM receipt every 0.5 s; lock with developer switch. Platform-side time from plug to Ready still unmeasured. |
| Update flow | BUILT, device check owed | Check answer at once; one-step run with up-front charge rule; Cancel via SIGTERM before the commit point (host test). The first real one-step run needs the next release (Beta 8). |
| Automatic time zone | BUILT, device check owed | Lookup validated against the zone table; country picker from tz tables. |
| UI v4 tour, thermal, sleep retry | OWED | From Beta 7. |
| FM radio | NOT STARTED | Beta 8; its own audit first. |

Gate decision: READY for Y2Linux 1.0.0-beta.7.1 / Reborn 1.0.0-beta.7.1 (Baseline 62, sequence 5850) as a public beta at the owner's request; next evidence boundary: the owner's OTA install and the Beta 7.1 report's device checks.

## BETA-7.2 (Baseline 63) motion and the Now Playing wave: milestone gap audit — 2026-10-16

Boundary: owner: more animation at 60 fps and a wave progress bar; "publish it when the build is done". A release is a milestone boundary. No hardware-scope or memory-model change: Reborn drawing only. Power note: Now Playing redraws continuously while playing and visible (Interactive lease); every other motion ends within ≈0.2 s.``

| Area | State for Beta 7.2 | Evidence / gap |
| --- | --- | --- |
| UI motion | BUILT, device fps owed | Host tests and mid-animation captures; frame rate on the Mali-400/CPU path to be sampled (graphics_frames). |
| Now Playing wave | BUILT, device fps and battery check owed | Continuous redraw while playing and visible. |
| Beta 7.1 / 7 checks | OWED | Unchanged. |
| FM radio | NOT STARTED | Beta 8; its own audit first. |

Gate decision: READY for Y2Linux 1.0.0-beta.7.2 / Reborn 1.0.0-beta.7.2 (Baseline 63, sequence 5900) as a public beta at the owner's request; next evidence boundary: the owner's OTA install and a frame-rate sample on the device.

## BETA-7.3 (Baseline 64) USB message instead of a screen: milestone gap audit — 2026-10-16

Boundary: owner: the locked computer screen blocked the player (and the 7.2 frame-rate measurement); "push a new version" with a message and a USB symbol instead. A release is a milestone boundary; Reborn presentation only. Supersedes Beta 7.1's lock decision (owner).

| Area | State for Beta 7.3 | Evidence / gap |
| --- | --- | --- |
| USB indication | BUILT, device check owed | Message + status-bar symbol; lock, dismiss state and developer switch removed; host tests. |
| Beta 7.2 motion fps | OWED | Sampling becomes possible with the cable in. |
| FM radio | NOT STARTED | Beta 8. |

Gate decision: READY for Y2Linux 1.0.0-beta.7.3 / Reborn 1.0.0-beta.7.3 (Baseline 64, sequence 5950) as a public beta at the owner's request; next evidence boundary: OTA install, then the 7.2 frame-rate sample.

## BETA-7.4 (Baseline 65) status-bar messages, cooler wave: milestone gap audit — 2026-10-16

Boundary: owner chose message placement C ("c") and the wave change; a release is a milestone boundary. Reborn only; no hardware or memory-model change. Thermal note recorded: no regression under the same conditions; the wave's CPU lease removed.

| Area | State for Beta 7.4 | Evidence / gap |
| --- | --- | --- |
| Messages | BUILT, device look owed | Rendered A/B/C; host tests. |
| Now Playing heat | BUILT, device check owed | 598 MHz expected while the wave plays; temperature over ten minutes on battery. |
| Motion fps | MEASURED (7.3) | 62 fps median while moving, 0 missed; Songs list sample owed. |
| FM radio | NOT STARTED | Beta 8. |

Gate decision: READY for Y2Linux 1.0.0-beta.7.4 / Reborn 1.0.0-beta.7.4 (Baseline 65, sequence 6000) as a public beta; next evidence boundary: the Now Playing clock/temperature check on battery.

## BETA-7.5 (Baseline 66) larger status bar, Skin in Settings: milestone gap audit — 2026-10-16

Boundary: owner chose status bar layout C, a Home header, Skin as its own Settings place and asked for the release; a release is a milestone boundary. Reborn only; no hardware, kernel or memory-model change. Real-hardware evidence unchanged since BETA-7.4 (7.3 fps sample, 7.4 temperatures); nothing here depends on new hardware behaviour.````

| Area | State for Beta 7.5 | Evidence / gap |
| --- | --- | --- |
| Status bar / Home header | BUILT, device look owed | Four rendered variants, owner chose C; host tests, previews, three skins. |
| Skin place | BUILT, device check owed | Settings fits seven rows; Display without scrolling; Skins and Themes folders read. |
| Now Playing heat | BUILT (7.4), device check owed | 598 MHz expected while the wave plays. |
| FM radio | NOT STARTED | Beta 8. |

Gate decision: READY for Y2Linux 1.0.0-beta.7.5 / Reborn 1.0.0-beta.7.5 (Baseline 66, sequence 6050) as a public beta at the owner's request; next evidence boundary: the device look at the new bar.

## BETA-7.6 (Baseline 67) smooth update screens: milestone gap audit — 2026-10-16

Boundary: owner reported low fps on the update download screen and asked for the release. Reborn only; no hardware, kernel, update-format or memory-model change (the platform's download is unchanged, nice 10). Real-hardware evidence unchanged since BETA-7.4.

| Area | State for Beta 7.6 | Evidence / gap |
| --- | --- | --- |
| Update screens | BUILT, device fps owed | Cause found in code (calm rate ≤ 29 fps); host tests; seen on the update after 7.6. |
| Status bar / Skin (7.5) | BUILT, device look owed | Previews. |
| Now Playing heat (7.4) | BUILT, device check owed | 598 MHz expected. |
| FM radio | NOT STARTED | Beta 8. |

Gate decision: READY for Y2Linux 1.0.0-beta.7.6 / Reborn 1.0.0-beta.7.6 (Baseline 67, sequence 6100) as a public beta at the owner's request; next evidence boundary: frame rate during the next OTA download.

## LASTFM scrobbling: milestone gap audit — 2026-10-16

Boundary: owner: Last.fm scrobbling from the player, on `main`, released separately from FM (FM stays on `beta8-fm`). No new hardware subsystem: a Reborn feature on the existing Wi-Fi/curl path; the only Y2Linux changes are release plumbing for the app key file and its privacy check. Plan, decisions and security: [LASTFM-SCROBBLE-PLAN](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FLASTFM-SCROBBLE-PLAN.md). Real-hardware evidence unchanged since BETA-7.6 (device on 1.0.0-beta.7.6).``

| Area | State | Evidence / gap |
| --- | --- | --- |
| Scrobble rules, queue, log | NOT STARTED → phase 1 | Playback events (TrackStarted/Boundary/Ended/Position) and tags exist in Reborn. |
| Last.fm client | NOT STARTED | curl HTTPS proven by internet radio; no MD5 yet. |
| Sign-in UI | NOT STARTED | Keyboard exists; QR encoder missing. |
| App API account | OWED (owner) | Key file outside git, see plan. |
| FM radio | ON BRANCH beta8-fm | Device test owed (BETA-8-FM rows). |

Gate decision: phase 1 READY (host only); live Last.fm runs wait for the owner's API account; a release waits for the owner's device check and word.

## LASTFM implementation boundary — 2026-10-16

Boundary: phases 1–3 of [LASTFM-SCROBBLE-PLAN](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FLASTFM-SCROBBLE-PLAN.md) on `main` (Reborn 60bea96 + Y2Linux release plumbing). Host evidence only; no image built, nothing installed.

| Area | State | Evidence / gap |
| --- | --- | --- |
| Counting rules, queue, log, clock | BUILT, host-tested | Unit tests: thresholds, pause, seek, repeat, gapless, untagged, unknown clock, torn queue line. |
| Last.fm client | BUILT, stand-in tested | MD5 RFC 1321 vectors, signature, no secret in argv, error classes, batches, stale drop. Live run owed. |
| Settings → Last.fm, QR | BUILT, host-tested | UI tests (password never drawn or printed), zbar decodes the encoder and the rendered page. |
| App key handling | BUILT, host-tested | 0600 checks, exact format, privacy names; key file from the owner still OWED. |
| Device | NOT_RUN | Real scrobbles, offline queue across sleep, sending after Wi-Fi returns. |

Gate decision: ready for a test build once the owner's key file exists; a release from `main` follows the device check and the owner's word. FM stays on `beta8-fm`.

## BETA-7.7 (Baseline 70) Last.fm scrobbling: milestone gap audit — 2026-10-16

Boundary: owner: "i want to install with ota so publish this". A public release is a milestone boundary. Reborn feature plus release plumbing for the app key; no hardware, kernel, update-format or memory-model change. Real-hardware evidence unchanged since BETA-7.6; FM radio stays on `beta8-fm`.

| Area | State for Beta 7.7 | Evidence / gap |
| --- | --- | --- |
| Last.fm scrobbling | BUILT, device check owed | 509 Reborn tests, key pair confirmed by Last.fm, key in image root 0600. |
| Secrets | BUILT | Session only on Y2DATA; privacy check refuses session/queue/log in images. |
| Update screens (7.6) | BUILT, device fps owed | Seen on this update's download. |
| FM radio | ON BRANCH | Device test owed (BETA-8-FM rows). |

Gate decision: READY for Y2Linux 1.0.0-beta.7.7 / Reborn 1.0.0-beta.7.7 (Baseline 70, sequence 6150) as a public beta at the owner's request; next evidence boundary: the owner's OTA install, QR sign-in and first real scrobble.

## BETA-7.8 (Baseline 71) Last.fm fixes: milestone gap audit — 2026-10-16

Boundary: owner: "yes" (release the fixes), "do 7.8". A public release is a milestone boundary. Reborn fixes only; no hardware, kernel, update-format or memory-model change. Real-hardware evidence: Beta 7.7 on the owner's player (QR sign-in, first real scrobble on last.fm; Now Playing lost after a pause; Last.fm events missing from the log).

| Area | State for Beta 7.8 | Evidence / gap |
| --- | --- | --- |
| Last.fm scrobbling | DEVICE-CONFIRMED (7.7), fixes BUILT | Real scrobble on last.fm; 512 Reborn tests incl. Now Playing decision, error-6 split, log guard. |
| Offline queue across sleep | NOT_RUN on device | Needs the player unplugged (ChargerActive refuses sleep). |
| Log | FIXED | radio/clock/platform/lastfm/scrobble events recorded again. |
| FM radio | ON BRANCH | Device test owed (BETA-8-FM rows). |

Gate decision: READY for Y2Linux 1.0.0-beta.7.8 / Reborn 1.0.0-beta.7.8 (Baseline 71, sequence 6200) as a public beta at the owner's request; next evidence boundary: Now Playing after a pause and the offline test on the owner's player.

## STORAGE-SETUP (Beta 7.9 candidate) automatic Internal Storage: milestone gap audit — 2026-10-16

Boundary: owner: automatic Internal Storage for every player ("i want everybody to have the exact same storage layout"), plus issues #39 and #44. Materially changes storage for every user (erases the stock FAT p8 in cases 1–2 or on request), so this audit precedes any implementation. Plan: [INTERNAL-STORAGE-SETUP-PLAN](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FINTERNAL-STORAGE-SETUP-PLAN.md).````````

| Area | State | Real-hardware evidence / gap |
| --- | --- | --- |
| Y2MEDIA layout | PROVEN on one player | Owner's p8 read 2026-10-16: ext4, Y2MEDIA, UUID …0103, start 3742720, 11 460 608 sectors, created by provision 2026-10-10. Pinned mkfs.ext4 reproduces its features/inodes/blocks on the host. |
| Stock p8 contents | ONE SAMPLE | Backup 20261010/93: 541 files, 31 MB (Themes, test files, empty Android folders); dirty bit only. Other users' contents unknown (case 3 covers large libraries). |
| Y2DATA headroom | MEASURED | Owner 644 MB free (54 MB staged update); fresh image 197 214 free 4 KiB blocks; reporter 585.8 MB. |
| Firmware image sizes | MEASURED | Innioasis v3.2.0 system.img sparse 518 MB (two copies); reporter's raw copy 859 826 928 B ≈ ANDROID partition. |
| Update health window | SOURCE | update.health_ack: 180 s from first call, rollback after → setup never on a PendingHealth boot. |
| Automatic setup, resume, Old Storage, Reborn UI | NOT BUILT | Host tests planned; device end-to-end on the owner's player after recreating the stock FAT from the backup (owner authorisation for p8 writes). |
| #44 SD dirty bit | BUILT on main | Linux 3110f3a, Reborn b023daf; host + real dosfstools tests. |

Gate decision: PLAN ACCEPTED FOR IMPLEMENTATION once the owner approves the plan; release only after the device end-to-end run (case 2 at least) and the owner's word.

## BETA-7.9 (Baseline 72) Internal Storage for every player, #39, #44: milestone gap audit — 2026-10-17

Boundary: owner: "plan is ok … update the code build and publish, and i update OTA and we see". Public release crossing the STORAGE-SETUP boundary (row above). Real-hardware evidence: owner's player prepared with the stock FAT restored from the 2026-10-10 backup (hash-identical), Internal Storage backed up twice.

| Area | State for Beta 7.9 | Evidence / gap |
| --- | --- | --- |
| Automatic Internal Storage | BUILT, device run owed | 792 host tests incl. resume/refusals (mutation-checked), real mkfs layout; files verified inside Y2ROOT. |
| Radio firmware location (#39) | BUILT | Host tests; device: not needed on the owner's player (firmware present). |
| SD dirty bit (#44) | BUILT | Real dosfstools tests. |
| FM radio | ON BRANCH | Device test owed. |

Gate decision: READY for Y2Linux 1.0.0-beta.7.9 / Reborn 1.0.0-beta.7.9 (Baseline 72, sequence 6250) at the owner's request; next evidence: the owner's OTA install and restart (case 2 on real hardware).

## BETA-7.10 (Baseline 73) USB file operations pass: milestone gap audit — 2026-10-17

Boundary: owner: "copying, moving and deleting files when connected over usb [should] work without errors and dont crash the player or hang … it should work for windows, mac and linux, please all fixes together". USB transfer subsystem change (kernel musb + MTP responder) and a public release. Real-hardware evidence: Beta 7.9 oops on the owner's player (pstore, decoded to ZERO_SIZE_PTR), Beta 7.9 storage setup confirmed on hardware.

| Area | State for Beta 7.10 | Evidence / gap |
| --- | --- | --- |
| ZLP DMA oops | FIXED | Root cause from registers + disassembly; musb skips mapping zero-length requests. Device confirmation owed (stress tool). |
| MoveObject / CopyObject | BUILT | Real responder protocol tests incl. between storages, read-only, refusals; mutation-checked. Windows Explorer run owed. |
| Internal Storage setup (7.9) | DEVICE-CONFIRMED | Owner's player, 509 files hash-identical, layout identical. |
| FM radio | ON BRANCH | Device test owed. |

Gate decision: READY for Y2Linux 1.0.0-beta.7.10 / Reborn 1.0.0-beta.7.10 (Baseline 73, sequence 6300) at the owner's word; next evidence: `mtp-file-ops` on the owner's player, then Windows Explorer and a macOS MTP app.

## USB-RX-DMA multi-packet receive DMA: milestone gap audit — 2026-10-17

Boundary: owner: "i would like to do multi packet and fix the kernel". Kernel USB driver change in the area where receive DMA once lost data. Plan: [USB-RX-DMA-MODE1-PLAN](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FUSB-RX-DMA-MODE1-PLAN.md).``

| Area | State | Real-hardware evidence / gap |
| --- | --- | --- |
| Upload ceiling | MEASURED | 8.7–10.3 MB/s up vs 37.7 down (Beta 7.10, owner's player); RX all PIO (dma_rx_programs=0). |
| Ceiling cause | PROVEN | One core 96–100 % busy at ≈21–24 k interrupts/s regardless of core (live affinity test, restored). |
| Storage headroom | MEASURED (candidate 11) | eMMC write 30 MiB/s, SD 26 MiB/s. |
| Mode-1 RX DMA | NOT BUILT | Stock MTK reference (REA) owed; device integrity tests owed. |

Gate decision: plan for owner review; implementation only after approval; default on only after the device tests.

**Update 2026-10-17 (same day, owner: "please investigate and look if you can get the fast usb upload working"; owner approved the test install and then "on by default"):**``````````````````

| Area | State | Real-hardware evidence / gap |
| --- | --- | --- |
| Stock reference (REA) | DONE | fm-kernel.elf (Linux 3.4.67) rxstate: mode 1 only for short_not_ok, AUTOCLEAR → DMAENAB → DMAMODE pulse, else mode 0 per packet; pause/resume/residue are stubs. No vendor MTP mode-1 path to copy. |
| Mode-1 RX DMA | BUILT, ON BY DEFAULT in test build 7.11 seq 6352 (not published) | Linux 1f86b4f, b49afaa, 049df5c, 10ec3eb; installed over SSH (local signed OTA). |
| Throughput | MEASURED | 1 GiB Internal 29.6 MB/s (was ~10), 512 MiB SD 23.3 MB/s, ECM 10–14 MB/s (6–8); ≈1 450 musb IRQ/s (was ≈22 000), CPU ≈80 % idle. |
| Integrity | PASS | SHA-256 on every byte: 20 boundary sizes × 2 storages, 100 random sizes, libmtp suite 26/26 (twice), 1.5 GB soak, 300 MB ECM; 0 kicks, 0 fallbacks, 0 DMA errors. |
| Defect found | FIXED | RXCOUNT falls while the engine unloads a packet; one sample looked short and cut a 64 MiB upload (seq 6350). Two agreeing samples now required. |
| Off switch | PASS | rx_dma=0: dma_rx_programs unchanged over 240 MB (mapped requests go to PIO, not mode 0). |
| Owner checks | OWED | Cable pulled mid-upload, sleep/wake with it on, Dolphin and Windows Explorer copies. |

Gate decision: default on in the test build on the owner's player; release (label 74) after the owner checks.

## BETA-7.11 (Baseline 74) faster uploads: milestone gap audit — 2026-10-17

Boundary: owner: "Dolphin copies work, publish it as beta 7.11". Kernel USB receive path change (USB-RX-DMA above) and a public release. Real-hardware evidence: test builds 6350–6352 on the owner's player.``

| Area | State for Beta 7.11 | Evidence / gap |
| --- | --- | --- |
| Multi-packet receive DMA | DEVICE-CONFIRMED, default on | 29.6 MB/s Internal, 23.3 MB/s SD, every byte hashed; libmtp suite 26/26; off switch PIO only. |
| Dolphin | OWNER-CONFIRMED | Owner: "Dolphin copies work". |
| Cable pull, sleep/wake, Windows Explorer | OWED | Not run with this path; rx_dma=0 restores Beta 7.10 behaviour. |
| FM radio | ON BRANCH | Device test owed. |

Gate decision: READY for Y2Linux 1.0.0-beta.7.11 / Reborn 1.0.0-beta.7.11 (Baseline 74, sequence 6352) at the owner's word (given).

## BETA-8.0 (Baseline 75) 1.0 review fixes: milestone gap audit — 2026-10-18

Boundary: owner: "fix it all and publish a new release beta 8.0", after the 1.0 readiness audit and code review ([V1-RELEASE-READINESS](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FV1-RELEASE-READINESS.md), [V1-CODE-REVIEW](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FV1-CODE-REVIEW.md)). Changes in the update health rule, the library scanner, SD admission, the USB receive fallback, the recovery image and the release assets. Real-hardware evidence: OTA install of 6400 on the owner's player.````````

| Area | State for Beta 8.0 | Evidence / gap |
| --- | --- | --- |
| Update health (B3, R7) | DEVICE-CONFIRMED | 6352 → 6400 acknowledged at ≈67 s; healthy: true with a broken file on Internal Storage. |
| Library unreadable files (B3, B4) | DEVICE-CONFIRMED | unreadable: 1, no library error; pruning covered by host tests. |
| SD reconcile (B5) | HOST-TESTED | Background process, tree kill on timeout; large-card device test owed. |
| Receive DMA fallback (B6) | HOST-TESTED | Normal path unchanged on the device (256 MiB hashed, counters consistent, m1_fallback 0); the fallback itself never fires in tests. |
| Recovery stuck power-off (B8) | FIXTURE-TESTED | Not provoked on the device. |
| Session recovery (B7) | HOST-TESTED |  |
| Toolchain sources (A7) | DONE | Y2Linux-sources-toolchain-f7cda4c7d213.tar, archives match Buildroot's pins. |
| Standby drain (A1, #42), external install/build (A2), owed device checks (A8, A9, A11) | OPEN | Unchanged; block a 1.0 label. |
| FM radio | ON BRANCH | Moves to a later beta number. |

Gate decision: READY for Y2Linux 1.0.0-beta.8.0 / Reborn 1.0.0-beta.8.0 (Baseline 75, sequence 6400) at the owner's word.

## BETA-8.1 (Baseline 86) panel power-down: milestone gap audit — 2026-10-18

Boundary: owner: "answer the issues ... and publish beta 8.1". Display driver behaviour change (#45) and a newly found hardware variant (two panel types). Real-hardware evidence: test builds 6450–6463 on the owner's player (ST7701S).``````

| Area | State for Beta 8.1 | Evidence / gap |
| --- | --- | --- |
| Panel identification | DEVICE-CONFIRMED (ST7701S) | 0xa1 = 88 on every boot, LK lcm=0/lcm=1 both handled |
| ST7701S power-down + stock init | DEVICE-CONFIRMED | 6456: two power-downs, two full inits, picture normal |
| GC9503V power-down + init | OFF BY DEFAULT | Stock packet types not yet run on hardware; reporter asked to test (#45) |
| Sleep drain effect | OWED | One overnight sleep on battery |
| FM radio | ON BRANCH |  |

Gate decision: READY for Y2Linux 1.0.0-beta.8.1 (Baseline 86, sequence 6463) at the owner's word (given).

## BETA-8.2 (Baseline 88) faster updates: milestone gap audit — 2026-10-18

Boundary: owner: "yes update all the docs and publish the build". Installer architecture change (payload layout, four threads, a new rollback-copy source) in the update core and recovery. Real-hardware evidence: test builds 87 (6500) and 88 (6501) installed by OTA on the owner's player.``````

| Area | State for Beta 8.2 | Evidence / gap |
| --- | --- | --- |
| Segmented root payload | DEVICE-CONFIRMED | Queued by Beta 8.1's core; decoded on four threads by the new recovery |
| Four-core backup / readback | DEVICE-CONFIRMED | 8.1 → 6500: backup 12.5 s, check 3.9 s, acknowledged |
| Kept package as rollback copy | DEVICE-CONFIRMED (install) | 6500 → 6501: backup 1.8 s, source: package, acknowledged |
| Rollback from a kept package | DEVICE-CONFIRMED (after publishing) | Owner rollback 6501 → 6500 from the kept package: 12.2 s in the recovery, RolledBack, healthy |
| Space | CHECKED | /data/updates ≈ 87 MB; kept package removed last by the cleanup |
| Sleep drain with panel power-down | OWED (from 8.1) | One overnight sleep on battery (#42) |
| FM radio | ON BRANCH |  |

Gate decision: READY for Y2Linux 1.0.0-beta.8.2 (Baseline 88, sequence 6501) at the owner's word (given).

## BETA-8.3 (Baseline 89) time left on the update screens: milestone gap audit — 2026-10-18

Boundary: owner: "build the latest and publish, but don't update the player". Installer progress and estimate, parallel hashing in the recovery, a Reborn screen text. Real-hardware evidence: the Beta 8.2 phase measurements and the owner rollback on the player (models); the 8.3 build itself has not run on a player.``

| Area | State for Beta 8.3 | Evidence / gap |
| --- | --- | --- |
| Time plan and seconds left | HOST-TESTED | Step lines carry left=, falling; models match 8.2 device phases (23.7/23.6 s, 11.7/12.2 s) |
| Recovery screen countdown | BUILT, NOT ON DEVICE | Compiled into RECOVERY; the owner's OTA shows it |
| Parallel verify hashing | HOST-TESTED | 34 update tests, ThreadSanitizer, AddressSanitizer/UBSan |
| Reborn check-step seconds | HOST-TESTED | Parser test; older cores keep the old text |
| Sleep drain with panel power-down | OWED (from 8.1) | One overnight sleep on battery (#42) |
| FM radio | ON BRANCH |  |

Gate decision: READY for Y2Linux 1.0.0-beta.8.3 (Baseline 89, sequence 6600) at the owner's word (given), with the device check owed through the owner's own OTA.

## BETA-8.4 (Baseline 90) dark display after a restart: milestone gap audit — 2026-10-18

Boundary: owner: "publish, I do OTA". Display restart path (kernel restart handler) after the 8.3 OTA rolled back on a dark display. Real-hardware evidence: the four restarts out of the recovery on the owner's player on 2026-10-18 (three lit with the SMI hold, one dark without it); the 8.4 build itself has not run on a player.````

| Area | State for Beta 8.4 | Evidence / gap |
| --- | --- | --- |
| Cause of the dark restart | FOUND (logs) | No SMI hold at probe, SMI gates 1 left closed, larb0 stat=1 greq=1, DSI reads lag after |
| Restart handler (42) back | HOST-TESTED | tests.test_display_domain; owed: restarts on the player |
| Why only some restarts close the gate | UNKNOWN | Handler reopens it on every restart |
| Sleep drain with panel power-down | OWED (from 8.1) | One overnight sleep on battery (#42) |
| FM radio | ON BRANCH |  |

Gate decision: READY for Y2Linux 1.0.0-beta.8.4 (Baseline 90, sequence 6700) at the owner's word (given), with the device check owed through the owner's own OTA.

## HP-LEVEL-EQ headphone output level and calibration: milestone gap audit — 2026-10-18

Boundary: owner (after an email about stock bass rolloff and "output gain switching with impedance"): a headphone output level setting, a parametric equalizer with AutoEQ import, optional DAC filter settings and a measurement plan. New user-facing control of the analog output stage (hearing safety) and a packaging change (two FFmpeg filters). Real-hardware evidence: regmap debugfs reads on the owner's player and the REA of the stock kernel (2026-10-18); nothing measured acoustically or electrically.``````

| Area | State | Real-hardware evidence / gap |
| --- | --- | --- |
| Output level today | READ ON DEVICE | HP_OUT_CTL_1 = 0x30 (1.73 Vrms full scale), CLASS_H 0x1E, Master pinned at −24 dB by Reborn → ≈0.11 Vrms at full volume |
| Stock level | REA | Vendor cs43131_apply_out_fs: headphones 0x10 (1.0 Vrms), CLASS_H never written (reset 0x1E); top volume step −3 dB → ≈0.71 Vrms |
| Full-scale voltages | DATASHEET | DS1155F2 HP_OUT_CTL_1 OUT_FS 00/01/10/11 = 0.5/1.0/1.41/1.73 Vrms; change only while PDN_HP is set; HV_EN = 1 specified for ≥ 600 Ω and VP ≥ 3.3 V |
| Load measurement | IN KERNEL SINCE BASELINE 49 (c852008), UNUSED | y2_hp/hpload_measure, board offset 102 Ω; no jack detection (#11/#12 parked) |
| Level control, parametric EQ, DAC filter settings | NOT BUILT | Host tests first (C harness for the codec logic, Reborn tests) |
| Stock bass rolloff | UNKNOWN | Same DAC filter registers; Android processing or analog — needs a measurement (plan for the emailer) |
| Real output, noise, frequency response per level and load | NOT MEASURED | 16/32/300 Ω loads with an audio interface |

Gate decision: implementation and host tests may proceed. A test build on the player and any release need the owner's word; the level default and the Master pin change loudness, so the owner listens before a release.

## BETA-8.5 (Baseline 93) headphone level, profiles, DAC filter: milestone gap audit — 2026-10-18

Boundary: owner: "publish it as beta 8.5". Headphone output stage control (kernel), a new default level, the Master change, shipped AutoEq data and two FFmpeg filters (packaging). Real-hardware evidence: test builds 91–93 (6750–6752) on the owner's player; 93 is this release.

| Area | State for Beta 8.5 | Evidence / gap |
| --- | --- | --- |
| Level control and default Low | DEVICE-TESTED | Registers per level; deferral while live; applied at power-up |
| Loudness at Low | BY DESIGN | −0.26 dB vs 8.4 (datasheet ratio); owner listening owed |
| Headphone profiles, 47 shipped | DEVICE-TESTED | Graph with shelves and preamp on ARM; refusal of a broken file (owner) |
| DAC filter | DEVICE-TESTED (register) | PCM_FILT_OPT 0xC2 for Slow phase compensated; sound not compared |
| Settings screens, fade after a raise, sleep with a level | OWED | Need the buttons / USB unplugged |
| Output voltage, noise, response per load | NOT MEASURED | Plan in HEADPHONE-OUTPUT.md |

Gate decision: READY for Y2Linux 1.0.0-beta.8.5 (Baseline 93, sequence 6752) at the owner's word (given).

## AUDIO-REVIEW-8.5 audio playback review after Beta 8.5: milestone gap audit — 2026-10-18

Boundary: owner asked for a review of audio playback (bugs, races, hearing safety, battery, tests) and then "do it all". Localized fixes in the codec overlay (0030) and Reborn; one battery-policy change (an equalizer no longer takes the PlaybackHeavy workload class) and a small loudness change (six shipped profiles 0.1–0.4 dB lower). No hardware, memory or packaging scope change. Real-hardware evidence: Beta 8.5 device results (test builds 91–93); everything below is host-tested only.``````````````

| Area | State | Evidence / gap |
| --- | --- | --- |
| OUT_FS while PDN_HP clear | FIXED (host) | y2_hp_level_set checked PDN_HP and wrote outside DAPM's lock (a stream starting in between); now under the card's DAPM mutex. hpload_measure refuses an open stream and holds DAPM. C harness asserts the lock; mutations caught; W=1 compile clean |
| Loudness without a fade | FIXED (host) | Fade carries over a reopened sink, volume up keeps fading, louder sound settings fade in, held pause released on any sound change |
| Profile clip safety | FIXED (host) | Preamp covers 44.1–384 kHz source rates; limiter holds a +6 dB ReplayGain full profile at S24/S16 (new fixture) |
| Shipped profile list | FIXED (host) | License file no longer listed as a profile |
| Battery with a profile | CHANGED, NOT MEASURED | One graph thread (host −20…−43 % CPU, bit-identical); no PlaybackHeavy floor/latency for EQ. Device CPU and mA owed |
| Settings screens, fades, sleep with a level | DEVICE-TESTED (test build 94, sequence 6800) except sleep | Profile list, dsp_rise_fade, pause_released, no restart for the same level, level_raise_fade → fade_continued after Next, registers per level, hpload_measure EBUSY while playing |
| Battery with a profile (device) | PARTLY MEASURED | Floor 747.5 → 598 MHz, ≥16 % fewer decode-thread cycles, half the idle entries; deep idle blocked by audio either way; mA owed |

Gate decision: host work complete (Linux host suite 805 OK, Reborn 539 tests, fmt, strict Clippy); test build 94 on the owner's player passed the checks above. A release needs the owner's word.

## BETA-8.6 (Baseline 94) audio playback review: milestone gap audit — 2026-10-18

Boundary: owner: "publish as a new update, once you deem this good". The AUDIO-REVIEW-8.5 fixes as a release; no hardware, memory or packaging scope change beyond a new test fixture (not shipped). Real-hardware evidence: test build 94 (sequence 6800) on the owner's player, identical to this release.````````

| Area | State for Beta 8.6 | Evidence / gap |
| --- | --- | --- |
| Level write under DAPM, hpload refusal | DEVICE-TESTED (behaviour) | Registers per level, EBUSY while playing; the race itself is not triggerable |
| Fades, held pause, same level | DEVICE-TESTED | dsp_rise_fade, fade_continued, pause_released, no restart |
| Profile list, hi-res preamp | DEVICE-TESTED | No license entry; AirPods Pro −6.1 dB in the graph |
| CPU with a profile | DEVICE-MEASURED | Floor 598 MHz (was 747.5), ≥16 % fewer decode cycles; current not measured |
| Sleep with a level, DAC filter by ear, output measurement | OWED | As in 8.5 |

Gate decision: READY for Y2Linux 1.0.0-beta.8.6 (Baseline 94, sequence 6800) at the owner's word (given).

## BETA-8.7 (Baseline 95) GC9503V identification: milestone gap audit — 2026-10-18

Boundary: owner: "publish the release also so i can update from OTA". One localized kernel parser change (`boot-policy.h`) for the second panel type; no hardware, memory or packaging scope change.``

| Area | State for Beta 8.7 | Evidence / gap |
| --- | --- | --- |
| LK panel naming | REA (stock v3.2.0 LK) | List order, fallback and GC9503V compare decoded; reporter's 3.2.1 LK hash requested |
| ST7701S players | UNCHANGED PATH | Parser keeps lcm=1-st7701; host tests |
| GC9503V players | IDENTIFIED, POWER-DOWN OPT-IN | Reporter's test owed (#45) |

Gate decision: READY for Y2Linux 1.0.0-beta.8.7 (Baseline 95, sequence 6900) at the owner's word (given).

## ERROR-REPORTS opt-in error reporting: milestone gap audit — 2026-10-18

Boundary: owner: an opt-in error reporter that sends "everything about the error and device, no personal information" over Wi-Fi HTTPS; receiver Cloudflare Worker + R2 (owner's choice after the home-server review). New subsystem: a network upload of device data, so privacy is the gating risk. Plan: [ERROR-REPORTS-PLAN](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FERROR-REPORTS-PLAN.md). Real-hardware evidence: a read-only inventory of the owner's player (log and state files, sizes, personal-data counts: kernel log 2 MACs and 4 serial lines, Reborn log 3 IPs, no titles, paths, SSIDs or account names).``

| Area | State | Evidence / gap |
| --- | --- | --- |
| Data sources | INVENTORIED | Kernel, pstore, platform journals, /run/y2, update/recovery, Reborn logs/state/control socket |
| Scrubbing | DESIGNED | Known-secret replacement + patterns; canary tests required before any upload code ships |
| Receiver | DESIGNED | Worker + R2; owner deploys; no read endpoint |
| Player UI, triggers, uploader | NOT BUILT | Steps R2–R6 |

Gate decision: implementation may proceed on the host (R2–R5). A test build on the player, deploying the Worker and any release need the owner's word. Nothing uploads by default (opt-in only).

## BETA-8.8 (Baseline 101) error reports saved to storage: milestone gap audit — 2026-10-19

Boundary: owner: "publish the next beta with what we have currently and export to storage feature either internal or sd card, we will do the worker afterwards", then "40-50 seconds is too long". The ERROR-REPORTS collector and screens reach users without any network path: a report is only written to storage the owner chose. No kernel, hardware, memory or packaging scope change.``

| Area | State for Beta 8.8 | Evidence / gap |
| --- | --- | --- |
| Save to storage | SHIPPED | Player: ext4 Internal Storage and exFAT SD written, both listed over MTP, MTP copy hash equal; FAT32 card and Reborn screens on the player owed |
| Privacy | CHECKED ON REAL DATA | The player's 199 private values absent from every report; canary and mutation tests; text path = value path on 6 973 real lines |
| Speed | ≈47 s → ≈10 s | Profiled on the player; 4 workers at nice 10 |
| Upload, automatic triggers | NOT SHIPPED | Switch and question hidden while upload is false; R3/R4 next |

Gate decision: READY for Y2Linux 1.0.0-beta.8.8 (Baseline 101, sequence 7000) at the owner's word (given).

## BETA-8.9 (label 102, not published) Save Report without a topic: milestone gap audit — 2026-10-19

Boundary: owner asked whether exporting everything would be better than choosing a topic, then "yes no topic" and "push and build a new release". The topic never selected report content (`report.py``_build` collects the same sections for every topic). Reborn screen flow only; no kernel, platform code, hardware, memory or packaging scope change.

| Area | State for Beta 8.9 | Evidence / gap |
| --- | --- | --- |
| Save Report flow | SHIPPED | Storage → saved; host test and preview 33i; not run on the player (8.8's platform command was) |
| Send Report Now topics | UNCHANGED, HIDDEN | Kept for the uploader (R4), where the topic is the only owner description |
| Everything else | As BETA-8.8 | Upload, FAT32/full card, #42, #45, #47 open |

Gate decision: built and installed on the owner's player (Acknowledged 7100, Save Report used); **not published**: the owner continued R3/R4 on `main` instead, so the next release is a new build.

## BETA-8.10 (Baseline 105) charging fix and error reports over Wi-Fi: milestone gap audit — 2026-10-19

Boundary: owner: "publish without it and answer the issue without it". Kernel charger policy change (inherited PMIC charger settings replaced instead of refused, #47), the platform uploader and a public receiver. No memory, partition or packaging scope change; the upload key ships in the image (public by design).

| Area | State for Beta 8.10 | Evidence / gap |
| --- | --- | --- |
| Charging start (#47) | FIXED IN CODE | Reporter's report: CV selector 31 refused (fault 0x80, -EIO); every CV/input OVP/battery OVP state tested on the host; not reproduced on a player; reporter's confirmation owed |
| Wall-charger charging | NOT RECHECKED on 8.10 | PC port charges on 105 |
| Uploads | SHIPPED | Owner's player: Send Report Now → R2 in ≈12 s, automatic report delivered, 0/203 private values |
| Receiver cost | BOUNDED | Durable Object budget 100 reports / 40 MiB a day, 2 MiB each, 180-day expiry ≈ 7 GiB < 10 GB free; WAF rule and billing alert owed |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.10 (Baseline 105, sequence 7400).

## BETA-8.11 (Baseline 106) Internal Storage setup on a low battery: milestone gap audit — 2026-10-20

Boundary: owner: "do fix 1 and 2 and publish as 8.11" after user report 20261019-153610. Platform battery gate of the automatic storage setup and one Reborn status line. No kernel, memory, partition or packaging scope change.``````````````

| Area | State for Beta 8.11 | Evidence / gap |
| --- | --- | --- |
| Setup battery gate | FIXED IN CODE | Report: every start on battery at 3.54–3.59 V voltage_now < 3.7 V → battery_low; now 25 % from voltage_ocv (plan value); host tests with the report's values |
| Storage screen reason | FIXED IN CODE | Pending reason was dropped; now Connect a charger and restart; preview checked |
| Setup on a stock-FAT player above 25 % | NOT CHECKED ON A PLAYER | Owner's player already has Y2MEDIA |
| Leftover system.img after the radio firmware is installed | OPEN (minor) | radiofw.scan returns at installed() before looking at the folders; second user report, no log |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.11 (Baseline 106, sequence 7500).

## BETA-8.12 (Baseline 108) crash loop, codec clock, sleep prepare and report fixes: milestone gap audit — 2026-10-20

Boundary: owner: "fix it all and build a point release … install on my player and check … publish it" after issues #48/#49 and 16 uploaded reports. Reborn parsing and crash isolation, one kernel codec overlay, two kernel platform fixes (suspend notifier order, loader-display hold), platform sleep guard, report collection, supervisor screen. No memory, partition or packaging scope change. Hardware evidence: test build 107 on the maintainer's player.````````

| Area | State for Beta 8.12 | Evidence / gap |
| --- | --- | --- |
| Playlist crash loop (#49) | FIXED, CHECKED ON A PLAYER | 3 players' playlists.rs:223 panics; 107 started with crash-trigger M3U files on the SD card, lists shown, no panic |
| Panic isolation | FIXED IN CODE | isolated() test with the real hook; per file in playlists, covers, scanner |
| Silent audio after EQ (#48) | FIXED IN CODE, PARTLY CHECKED | XTAL timeout in report; register-model test; 25 reopens on 107 clean, crystal source confirmed; slow crystal not reproducible here |
| Suspend prepare -EPERM | FIXED IN CODE | notifier order from linux-6.18 kernel/cpu.c; not checked (player on USB) |
| Sleep quarantine after a prepare refusal | FIXED IN CODE | host tests; retry after 120 s |
| Dark display after a recovery restart | FIXED IN CODE (cause from one report) | hold line present on 107; intermittent, GC9503V restarts owed |
| Report collection | FIXED, CHECKED ON A PLAYER | /proc and debugfs present, leak check 0/44; codec glob only host-tested (108) |
| Couldn't Start screen | FIXED IN CODE | supervisor tests against a fake tree; not shown on a player |
| Build 108 on a player | NOT INSTALLED | classifier refused the install; differs from 107 by the report glob and sequence |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.12 (Baseline 108, sequence 7601).

## BETA-8.13 (Baseline 110) MTP track listing, Wi-Fi connect and boot log: milestone gap audit — 2026-10-20

Boundary: owner: "fix all of this, publish 8.13 and mark all of these reports as solved" after five uploaded reports and two user messages. One userspace responder overlay (umtprd reads Reborn's library read-only), one Wi-Fi driver call, one boot script line, maintainer report tools. No memory, partition or packaging scope change. Hardware evidence: build 110 on the maintainer's player.````````

| Area | State for Beta 8.13 | Evidence / gap |
| --- | --- | --- |
| Songs in Strawberry / libmtp clients | FIXED, CHECKED ON A PLAYER | mtp-tracks 0 (8.12) → 311 = files = library rows, all tagged; Strawberry itself not run |
| MTP Name = tag title | OWNER DECISION | Windows Explorer display not checked |
| Wi-Fi connect dropped (sme.c:845) | FIXED, CHECKED ON A PLAYER | boot connect + 3 reconnects, no warning; the original race is intermittent |
| Boot Errno 22 | FIXED, CHECKED ON A PLAYER | none in dmesg on 109 and 110 |
| Pause/resume silence | FIXED IN 8.12, CHECKED ON A PLAYER | 25 s and 3.5 min wired pauses with sound on 8.12 |
| Report intake | DONE | timer + REVIEWED.md ledger on the maintainer PC |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.13 (Baseline 110, sequence 7701).

## BETA-8.14 (Baseline 111) shuffle, seek, genre Shuffle, titles and eMMC zero-out: milestone gap audit — 2026-10-20

Boundary: owner: "build 8.14 with 1–4 and publish it" after user requests (shuffle, seek, genre Shuffle, long titles) and report bf017f02. Reborn playback/UI changes and one MSDC card quirk. No memory, partition or packaging scope change. Hardware evidence: build 111 on the maintainer's player.

| Area | State for Beta 8.14 | Evidence / gap |
| --- | --- | --- |
| Shuffle order | FIXED, CHECKED ON A PLAYER | seed tests (orders differ, uniform first song); owner: two shuffles differ |
| Held seek | FIXED, CHECKED ON A PLAYER | schedule test; owner: feels right; first tuning |
| Genre Shuffle row | DONE, CHECKED ON A PLAYER | UI test plays the genre's songs shuffled |
| Long title on Home | FIXED, CHECKED ON A PLAYER | fitted to 200 px |
| eMMC zero-out as erase | FIXED, CHECKED ON A PLAYER | write_zeroes_max_bytes 0; the setup itself not re-run |
| Japanese/CJK text, USB DAC, video | PLANNED / GATED | CJK next (audit before work); USB DAC needs the VBUS hardware check; video not for 1.0 |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.14 (Baseline 111, sequence 7800).

## BETA-8.15 (Baseline 112) CJK text, update check after a wake and codec retry: milestone gap audit — 2026-10-20

Boundary: owner: "fix this for 8.15 and also add japanese but dont put it on my player, i want to update with OTA". Packaging scope grows by one font package (16.5 MB in the root filesystem, ~361 MiB free after); Reborn gains a runtime glyph page (1 MiB CPU + 2 MiB GPU, only once CJK text appears); platform update check and Bluetooth worker behaviour. No partition, kernel or memory-layout change. Hardware evidence: none for this build (owner installs by OTA).

| Area | State for Beta 8.15 | Evidence / gap |
| --- | --- | --- |
| Japanese/Chinese/Korean text | IMPLEMENTED, HOST-CHECKED | 12 preview states, host GLES compare; Lima and A7 speed unmeasured |
| Update check after a wake | FIXED IN CODE | host tests (mutation-checked); on a player after the owner's OTA |
| Codec choice while connecting | FIXED IN CODE | classification test; on a player with headphones owed |
| Build 112 on a player | NOT INSTALLED BEFORE PUBLISH | owner's OTA is the first install; health check rolls back a failing Reborn |
| USB DAC, video | GATED / NOT FOR 1.0 | unchanged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.15 (Baseline 112, sequence 7900).

## BETA-8.16 (Baseline 113) large libraries: milestone gap audit — 2026-10-20

Boundary: owner: multi-core scanning before 8.16 "so the user can test that directly", after report 9765e1e7 (28 600 songs). Reborn queue limit and windowing, one scanner SQL statement, parallel tag reading (≤ 3 threads, nice 10, inside the existing LibraryScan lease). No kernel, partition or packaging change; memory per queue drops (5 000 songs).

| Area | State for Beta 8.16 | Evidence / gap |
| --- | --- | --- |
| All Songs / Shuffle on 28 600 songs | FIXED IN CODE | window and restore-trim tests; not run on a large library |
| Rescan with no changes | FIXED IN CODE | query plan read on a player's library; host benchmark 700×; player timing owed |
| Tag reading on new files | FIXED IN CODE | order/isolation test with real fixtures; host 3.3×; SD-bound share on the player unmeasured |
| Build 113 on a player | NOT INSTALLED BEFORE PUBLISH | owner OTA; health check rolls back a failing Reborn |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.16 (Baseline 113, sequence 8000).

## BETA-8.17 (Baseline 114) user reports and #51: milestone gap audit — 2026-10-21

Boundary: owner: fix every open finding from the new reports, Reddit posts and #51 on top of 8.16, publish as 8.17; HLS radio and an on-device SD repair deferred. Kernel overlays 0030 (codec crystal lifetime, rail cycle) and 0017 (DSI double read on a persistent lag), a new BlueALSA patch (SBC bitpool steps), platform and Reborn fixes. No partition or memory-layout change.

| Area | State for Beta 8.17 | Evidence / gap |
| --- | --- | --- |
| #51 headphone crystal | FIXED IN CODE | register-model test (restart, retry, rail cycle, rails left off); not run on a player; crystal power while the codec is active unmeasured |
| SD admission (F12) | FIXED IN CODE | fsck.fat 4.2 outputs from host images; real-image test |
| Bluetooth disconnect/search/connect (F20, F21, F14) | FIXED IN CODE | Reborn unit tests, native fake-BlueZ test of the page cancel; page cancel on real BlueZ unconfirmed |
| SBC bitpool steps (F22) | FIXED IN CODE | host decision tests, ARM compile; no stuttering sink tested |
| F13 Wi-Fi after wake, F17 dark wake, F18 early sleep | DIAGNOSTICS / MITIGATION | causes unproven; new evidence fields in reports |
| Build 114 on a player | NOT INSTALLED BEFORE PUBLISH | owner OTA; health check rolls back a failing Reborn |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.17 (Baseline 114, sequence 8100).

## BETA-8.19 (Baseline 118) audiobooks, sharper covers, Customize: milestone gap audit — 2026-10-21

Boundary: owner: sharper covers and a Customize page (wrap-around lists, screen-off buttons) — built as test 8.18, never published — then audiobooks end to end (Y2Player assessed, not copied) with speed and a sleep timer, published as 8.19. Packaging/memory changes: FFmpeg gains the `atempo` filter (defconfig, `verify-ffmpeg.py`, Reborn qemu lists); Reborn's per-allocation FFmpeg ceiling 32 → 128 MiB (a long M4B's frame index), large MP4s scanned one at a time; the thumbnail atlas grows to 2048×1024 (≈8 MB of video memory). No kernel, partition or session-schema change (`state/books.json` is new and separate).````

| Area | State for Beta 8.19 | Evidence / gap |
| --- | --- | --- |
| Audiobooks (detection, list, page, chapters, progress, rewind, finished) | IMPLEMENTED, DEVICE-CHECKED | test books on the owner's player (builds 117/118); real libraries owed |
| Speed (atempo) | IMPLEMENTED, DEVICE-CHECKED | atempo=1.50 in the chain, position rate measured; by ear owed |
| Sleep timer | IMPLEMENTED, DEVICE-CHECKED | end of chapter on the player; the timed fade owed |
| Long M4B (10.5 h) | FIXED, DEVICE-CHECKED | RSS 92 MB (155 MB peak) of 928 MB; seek 2.8 s (reopen); in-file seek later |
| Covers 180/128, levels, crop, cache | IMPLEMENTED, DEVICE-INSTALLED | GLES 165/165; Mali-400 look checked on screenshots only |
| Customize, When Screen Off, headset grace | IMPLEMENTED, HOST-CHECKED | router and UI tests; holds not injectable |
| Car AVRCP metadata | OPEN | capture running on the owner's player |
| Build 118 on a player | INSTALLED BEFORE PUBLISH | owner's player, Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.19 (Baseline 118, sequence 8302).

## BETA-8.20 (Baseline 119) headphone crystal (#52): milestone gap audit — 2026-10-22

Boundary: owner: fix GitHub #52 and publish 8.20, installed and tested on the owner's player first. Kernel change limited to the CS43131 overlay (0030: crystal bias after a failure, sysfs) and Reborn's open deadline; reports gain one sysfs file. No packaging, memory, partition or schema change. Hardware evidence: the #52 reports (one player, a marginal crystal) and the owner's player (build 119).````````

| Area | State for Beta 8.20 | Evidence / gap |
| --- | --- | --- |
| Crystal bias 15 µA after a failed start or a stop | IMPLEMENTED, HOST-CHECKED, DEVICE-CHECKED (forced) | register model test; owner's player with boost: CRYSTAL_SET=02, all playback steps pass |
| Stock bias on healthy players | DEVICE-CHECKED | owner's player: every start first try, boosted=0 |
| Reborn open deadline 5 s | IMPLEMENTED, HOST-CHECKED | Reborn tests; the slow path only on the affected player |
| #52 on the affected player | OWED | reporter's next report (y2_hp/xtal) |
| Build 119 on a player | INSTALLED BEFORE PUBLISH | owner's player, Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.20 (Baseline 119, sequence 8400).

## BETA-8.21 (Baseline 120) headphone crystal run as stock (#52, #54): milestone gap audit — 2026-10-22

Boundary: owner: do 8.21 and publish, installed and tested on the owner's player first. Kernel change limited to the CS43131 overlay (0030: crystal lifetime and wait, codec autosuspend, sysfs fields). No packaging, memory, partition, schema or Reborn code change (identity only). Hardware evidence: #52 reports on 8.20 (15 µA fails), the #54 report (second player, never plays; plays on stock), the stock kernel's codec driver (REA/objdump), the owner's player (build 120).``````

| Area | State for Beta 8.21 | Evidence / gap |
| --- | --- | --- |
| Crystal starts with the codec, stops only with the rails | IMPLEMENTED, HOST-CHECKED, DEVICE-CHECKED | register model + PM tests; owner's player: every power-up ready=1, no stop outside runtime suspend |
| Stream uses an unconfirmed crystal after 1 s (stock path) | IMPLEMENTED, HOST-CHECKED | model with a 5-s crystal; not reachable on the owner's player (crystal ready at once) |
| Codec autosuspend 5 s | DEVICE-CHECKED | stop 8 s → suspended; skips keep the codec active |
| 48 kHz (PLL) from a powered-down codec | DEVICE-CHECKED | owner's player |
| #52 / #54 on the affected players | OWED | reporters' next reports (y2_hp/xtal unconfirmed=) |
| #53 clock without Wi-Fi | DIAGNOSED, NOT CHANGED | owner decision pending |
| Build 120 on a player | INSTALLED BEFORE PUBLISH | owner's player, Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.21 (Baseline 120, sequence 8500).

## BETA-8.22 (Baseline 121) report fixes F23–F32 and #53: milestone gap audit — 2026-10-22

Boundary: owner: plan and implement all fixes from the 2026-10-22 report review in the next beta, installed and tested on the owner's player first. Changes: initramfs/recovery (stage trail, health evidence, display off before restart), kernel config `CONFIG_PSTORE_PMSG` and a `pmsg-size` inside the existing ramoops reservation (no memory map change; DTB validator updated), overlay 0014 (log rate), Wi-Fi driver remove path, platform (sleep lease, taint, Wi-Fi evidence, download record, clock), Reborn (sink retry, Bluetooth marker/Pair, pre-open, Date & Time). No partition, schema or packaging change. Hardware evidence: fourteen user reports (8.10–8.20) and the owner's player (test builds 8600–8603).````

| Area | State for Beta 8.22 | Evidence / gap |
| --- | --- | --- |
| F23 health-boot evidence (pmsg, health files, console/panic until confirmed) | IMPLEMENTED, DEVICE-CHECKED | owner's player: health file with trail; settings restored; normal-boot trail |
| F23 recovery display off before restart | IMPLEMENTED, DEVICE-CHECKED (no regression) | four OTA installs acknowledged on boot 1; cause on GC9503V unproven |
| F24 activity lease released before the radio restore; busy retry | IMPLEMENTED, HOST-CHECKED | sleep needs USB off; owed |
| F25 / F28 Bluetooth | IMPLEMENTED, HOST-CHECKED | failure cases owed |
| F26 WARN-only taint / F27 Wi-Fi remove | IMPLEMENTED, HOST-CHECKED / DEVICE-CHECKED | F27: Wi-Fi off while Online, no WARN |
| F29 / F30 | DEVICE-CHECKED | 0 bursts after 50 skips; 1 scanout line per boot |
| F31 Wi-Fi evidence | IMPLEMENTED, HOST-CHECKED | failure case owed |
| F32 interrupted download | IMPLEMENTED, DEVICE-CHECKED | stale record → download_interrupted |
| #53 manual clock | IMPLEMENTED, DEVICE-CHECKED (platform) | set, refusal, NTP step-back, shutdown save; page by hand owed |
| #52/#54 crystal lifecycle as stock | IMPLEMENTED, DEVICE-CHECKED (owner's healthy crystal) | 15/15 playback, ready_ms=10 cold; reporters owed |
| Build 121 on a player | INSTALLED BEFORE PUBLISH | seq 8607, Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.22 (Baseline 121, sequence 8607).

## BETA-8.23 (Baseline 122) recovery watchdog (F34) and DAC power as stock (#52, #54): milestone gap audit — 2026-10-22

Boundary: owner: stop the "Step 1 of 4" install freeze from needing a forced restart; model the headphone DAC's power as close to stock as possible ("do it all now"); install and test on the owner's player, then publish. Changes: initramfs recovery (watchdog keeper, pmsg trail, previous-boot evidence), update core (progress to pmsg), overlay 0030 (stock power-up, `y2_hp/hold`), DT DAC rail delays (validator updated), Reborn (kept wired sink, DAC hold, F33 update task queue). No memory map, partition, schema or packaging change. Hardware evidence: #52/#54 reports on 8.22 and the owner's player (test builds 8700–8705).````````

| Area | State for Beta 8.23 | Evidence / gap |
| --- | --- | --- |
| F34 recovery watchdog + evidence | IMPLEMENTED, DEVICE-CHECKED | starved keeper resets (boot_reason=4); 8703–8705 restarted by themselves; freeze cause unproven |
| Initramfs command coverage | HOST-CHECKED | test: every command init/recovery/storage run exists in the initramfs |
| #54 stock power-up (XTAL+PLL+CLKOUT, EXT 20 ms later, rail burst) | IMPLEMENTED, DEVICE-CHECKED (owner's healthy crystal) | PWDN_CTL=f0, SYS_CLK_CTL_1=04, ready_ms=30 after boot; reporters owed |
| #52 kept wired output across same-format tracks | IMPLEMENTED, DEVICE-CHECKED | 17/17 reuses in the skip block, 96 per session, no kernel line; click check by ear owed |
| DAC hold while the screen is on | IMPLEMENTED, DEVICE-CHECKED (screen on/off) | released at screen-off, codec down after 141–160 s; real sleep/wake and power-off with this build owed; battery cost unmeasured |
| F33 update task queue (Reborn) | IMPLEMENTED, HOST-CHECKED | — |
| Build 122 on a player | INSTALLED BEFORE PUBLISH | seq 8705, Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.23 (Baseline 122, sequence 8705).

## BETA-8.24 (Baseline 123) no codec PLL, 44.1 kHz as stock (#52): milestone gap audit — 2026-10-23

Boundary: owner: implement the three #52 measures (no PLL, cold start after a restart, self-healing) and publish 8.24. Changes: AFE rate list (44.1 kHz only), overlay 0030 (refuse non-crystal rates, power cycle after a crystal error, cold start at probe, sysfs fields), platform capabilities (enabled/driver/sink rates), Reborn (`WIRED_RATE`, wired plan and reuse rule simplified). No memory map, partition, schema or packaging change. Hardware evidence: #52 report on 8.23 (all failures at 48 kHz), stock `audio_policy.conf`, the owner's player (build 123).````

| Area | State for Beta 8.24 | Evidence / gap |
| --- | --- | --- |
| Wired output 44.1 kHz only, no PLL | IMPLEMENTED, DEVICE-CHECKED | 48/96 kHz play at 44100 Hz, crystal selected; reporters owed |
| One open sink across rates | DEVICE-CHECKED | sink_reused +50, sink_reopened 0 |
| Power cycle after a crystal error | IMPLEMENTED, HOST-CHECKED | register model; not triggerable on the owner's player |
| Cold start at probe | IMPLEMENTED, DEVICE-CHECKED (not triggered) | restarts already reset VGP2; safety net only |
| Build 123 on a player | INSTALLED BEFORE PUBLISH | seq 8800, Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.24 (Baseline 123, sequence 8800).

## BETA-8.25 (Baseline 124) crystal start as stock with retries (#52, #54): milestone gap audit — 2026-10-23

Boundary: owner: implement Fable's plan from the #52/#54 handoff, install on the owner's player, publish 8.25. Changes: overlay 0030 only (crystal start with the chip powered except the headphone amplifier, three tries with rail cycles, a first-stream cold start, module test switches, sysfs fields) and its tests. No memory map, partition, schema, packaging or Reborn code change. Hardware evidence: #52 and #54 reports on 8.24 (XTAL_ERR at power-up), stock RE, the owner's player (builds 8900 and 8901).

| Area | State for Beta 8.25 | Evidence / gap |
| --- | --- | --- |
| Crystal start with the chip powered | IMPLEMENTED, DEVICE-CHECKED | owner: 10/10 first-try starts; reporters owed |
| Amplifier kept down during the start | DEVICE-CHECKED | static at screen wake with it on (8900), none without (8901) |
| Power-up retries / first-stream cold start | IMPLEMENTED, HOST-CHECKED | register model, mutation-checked; never needed on the owner's player |
| Build 124 on a player | INSTALLED BEFORE PUBLISH | seq 8901, Acknowledged |

## BETA-8.26 (Baseline 125) report fixes F35–F41: milestone gap audit — 2026-10-23

Boundary: owner: fix the findings of the 2026-10-23 review of twelve uploaded reports and publish; owner chose 450 mA for nonstandard chargers (F38) and a device run before publishing. Changes: platform Python (battery start, low-battery rule, shutdown trail, Wi-Fi and SD evidence, report scrubbing), `y2-radio`, the Wi-Fi driver's roam indication and the nonstandard charger ceiling. No memory map, partition, schema, packaging or Reborn code change. Hardware evidence: the twelve reports, the owner's player (F37 reproduced on 8.25, then 8.26).````

| Area | State for Beta 8.26 | Evidence / gap |
| --- | --- | --- |
| F36 start on a charger after a low-battery power-off | IMPLEMENTED, HOST-CHECKED | report values replayed; restore path device-checked; a drained battery not reproduced |
| F37 Wi-Fi rfkill after a sleep with Wi-Fi off | IMPLEMENTED, DEVICE-CHECKED | reproduced on 8.25 (phy4 soft=1), fixed on 8.26 (phy1 soft=0, COMPLETED) |
| F38 nonstandard chargers 450 mA | IMPLEMENTED, HOST-CHECKED | not qualified on a nonstandard charger (owner decision) |
| F39 shutdown trail, 3-s stage writes | IMPLEMENTED, DEVICE-CHECKED | trail in the next boot's capture; the stalled update restart's cause stays open |
| F35 roam BSS entry | IMPLEMENTED, BUILT | the re-association could not be forced |
| F12/F13/F41 report evidence | IMPLEMENTED, HOST-CHECKED | F41 seen in a saved device report |
| Build 125 on a player | INSTALLED BEFORE PUBLISH | seq 9000, Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.26 (Baseline 125, sequence 9000).

## BETA-8.27 (Baseline 126) SD cards: read-only fallback, repair, protection (F12): milestone gap audit — 2026-10-23

Boundary: owner: "do all phases with user confirmation in 2" (plan after report 29ed4ccb). Changes: platform `media.py` (admission classes, read-only fallback, repair, protected mount with write windows), status, reports, the firmware import, the USB service; Reborn SD states, Repair SD Card, playlist write windows. No kernel, memory map, partition, schema or packaging change. Hardware evidence: report 29ed4ccb, host reproduction of interrupted writes, the owner's player (exFAT card).````

| Area | State for Beta 8.27 | Evidence / gap |
| --- | --- | --- |
| Interrupted-write leftovers admitted | IMPLEMENTED, HOST-CHECKED | real fsck.fat 4.2 lines; same lines on the player |
| Damaged card plays read-only | IMPLEMENTED, HOST-CHECKED | not run on a damaged card in a player |
| Repair SD Card | IMPLEMENTED, HOST-CHECKED | fsck.fat -a -w on damaged images on the player; the full flow not run on a damaged card |
| Protected card + write windows | IMPLEMENTED, DEVICE-CHECKED | ro 4 s after unplug, clean, rw on replug, playback and sleep while ro |
| Build 126 on a player | INSTALLED BEFORE PUBLISH | seq 9100, Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.27 (Baseline 126, sequence 9100).

## BETA-8.28 (Baseline 127) Wi-Fi wrong password (Y2Reborn #20): milestone gap audit — 2026-10-23

Boundary: owner: "do the fix and publish the new version" after the #20 analysis. Changes: platform Wi-Fi failure record and state (`network.py`, `observe.py`); Reborn Wi-Fi worker join, Wi-Fi page, keyboard return, diagnostics. No kernel, memory map, partition, schema or packaging change. Hardware evidence: #20, report a19646dd, the owner's player (reproduced on 8.27, checked on 8.28).``````

| Area | State for Beta 8.28 | Evidence / gap |
| --- | --- | --- |
| Wrong password reported by the platform | IMPLEMENTED, DEVICE-CHECKED | Failed / wrong_credentials with the failed network id |
| Join tried before it is saved | IMPLEMENTED, DEVICE-CHECKED | wifi-join-wrong: WrongPassword 5.8 s, nothing left; wifi-join: Joined |
| Keyboard return, rows, Change Password | IMPLEMENTED, HOST-CHECKED | UI test and preview; not typed on the device |
| Saved network whose password changed | IMPLEMENTED, HOST-CHECKED | the owner's password cannot be restored after such a test |
| Build 127 on a player | INSTALLED BEFORE PUBLISH | seq 9200, Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.28 (Baseline 127, sequence 9200).

## BETA-8.29 (Baseline 128) charging without PMIC die calibration: milestone gap audit — 2026-10-24

Boundary: owner: "do the fixes, I want +10 here, and publish a new version so my user can update" after the analysis of reports 09888d70/8fc8eea6/ba0bb428 (install 047f2c1a). Changes: `kernel/platform/power-math.h` (`y2_pmic_calibrate` nominal case) and `mt6323-adc.c` (flag, zone, boot log). No memory map, partition, schema, packaging or Reborn change. Hardware evidence: the three reports (charger `fault=0x3`, `die calibration=0`); the stock nominal is from `mtk_ts_pmic.c``pmic_cali_prepare()` (BSP `d53dd75c3ff7`).

| Area | State for Beta 8.29 | Evidence / gap |
| --- | --- | --- |
| Die sensor without calibration fuse | IMPLEMENTED, HOST-CHECKED | stock nominal + 10 °C; unit test; not run on an affected player |
| Calibrated players | UNCHANGED, HOST-CHECKED | same conversion at the own fuses; container suite 879 OK |
| Build 128 on a player | NOT INSTALLED BEFORE PUBLISH | SSH to the owner's player not available in this session; the owner's player is calibrated |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.29 (Baseline 128, sequence 9300).

## BETA-8.30 (Baseline 129) GitHub triage fixes: milestone gap audit — 2026-10-24

Boundary: owner: "do 58, do 55 and also look for other places in reborn with the same problem, do 4 with the previous song, do bluetooth absolute volume, assess but don't implement 59", then "Publish Beta 8.30" and "make the GC9503V power-down default + close #42". Changes: Reborn queue membership and Songs order (`track_matches`, `filtered_indices`, `play_index`), Previous restart, AVRCP absolute volume (BlueZ `MediaTransport1.Volume`, Reborn settings `wired_volume`/`bluetooth_absolute_volume`), two-line toasts; Linux recovery-screen text and `CONFIRMED_PANELS`. No kernel, memory map, partition, data schema or packaging change. Hardware evidence for the GC9503V default: #45 (8.7, normal picture through screen-off cycles and deep sleep) and #42 (≈1.9 mA overnight).````````

| Area | State for Beta 8.30 | Evidence / gap |
| --- | --- | --- |
| Music queues without audiobooks (#58), Songs order (Y2Reborn #21) | IMPLEMENTED, HOST-CHECKED | UI test music_queues_skip_audiobooks_and_songs_play_in_list_order |
| Previous restarts the song (Y2Reborn #21) | IMPLEMENTED, DEVICE-CHECKED | 3/3 on the owner's player after the seek-target fix (Reborn 44481c3) |
| Bluetooth absolute volume (Y2Reborn #22) | IMPLEMENTED, HOST-CHECKED | level/takeover unit test; not run with real headphones (none at hand); reporter confirmation owed |
| Recovery text (#55), Reborn toasts | IMPLEMENTED, HOST-CHECKED | test_recovery_screen_lines_fit_its_28_columns; toast test + preview 44b; 16 toasts were cut |
| GC9503V panel power-down default (#42/#45) | ENABLED BY DEFAULT | confirmed on a GC9503V player by its owner; the owner's player is ST7701S (unchanged) |
| SD filesystems (#59) | ASSESSED, NOT IMPLEMENTED | ext4 supported; f2fs possible later, btrfs not planned (answer on #59) |
| Build 129 on a player | INSTALLED BEFORE PUBLISH | seq 9401 Acknowledged; one hung start after the update restart (F39 family, before boot.json), healthy after a power cycle |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.30 (Baseline 129, sequence 9401).

## BETA-8.31 (Baseline 130) left/right balance: milestone gap audit — 2026-10-24

Boundary: owner: "can you also make this addition to the sound settings" (a user's left/right balance request), then "Release as Beta 8.31". Change: Reborn only (`settings.balance`, sink gain per channel, Balance page, Sound layout). No kernel, memory map, partition, data schema or packaging change.

| Area | State for Beta 8.31 | Evidence / gap |
| --- | --- | --- |
| Balance setting | IMPLEMENTED, HOST- AND DEVICE-CHECKED | unit + UI tests; set and saved through button events on the owner's player, playback without xruns; not listened to |
| Build 130 on a player | INSTALLED BEFORE PUBLISH | seq 9500, Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.31 (Baseline 130, sequence 9500).

## BETA-8.33 (Baseline 134) search page and queue redesign: milestone gap audit — 2026-10-24

Boundary: owner: plan and "do the whole revamp" of the search page, then a queue assessment and "do the whole plan", each installed for testing; then "can you publish a new baseline". Changes: Reborn (search page, queue model and Up Next, playback engine's upcoming list, session schema 3, `rebornctl action`) and the platform's settings reset and installed-arm check for schema 3. No kernel, memory map, partition or packaging change.``

| Area | State for Beta 8.33 | Evidence / gap |
| --- | --- | --- |
| Search page | IMPLEMENTED, HOST- AND DEVICE-CHECKED | UI tests, previews 70–71e, device walk-through on builds 131/132 |
| Queue model, Up Next, Select Songs, group actions | IMPLEMENTED, HOST- AND DEVICE-CHECKED | core/UI tests, engine test; device through rebornctl action on 133/134; holds by hand open |
| No restart on queue edits | IMPLEMENTED, HOST- AND DEVICE-CHECKED | engine test; device: generation unchanged, gapless next |
| Session schema 3 | IMPLEMENTED, DEVICE-CHECKED | 8.31 session read on 133, schema-3 restore on 134; rollback to < 8.33 keeps settings, empties the queue |
| Build 134 on a player | INSTALLED BEFORE PUBLISH | seq 9702, Acknowledged, healthy, 0 warnings |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.33 (Baseline 134, sequence 9702).

## BETA-8.34 (Baseline 135) MTP hang fix: milestone gap audit — 2026-10-24

Boundary: user report #61 (MTP hangs in Dolphin, the player disconnects); owner: "can you check on that?", then publish. Change: one uMTP patch (`0006-y2-mtp-events-never-block`) and its protocol test. No kernel, Reborn, memory map, partition, data schema or packaging change.

| Area | State for Beta 8.34 | Evidence / gap |
| --- | --- | --- |
| MTP events vs requests | FIXED, HOST- AND DEVICE-CHECKED | protocol test (hung before the fix); KDE reconnect, 3 storage swaps, 20 MB copies on the owner's player; Windows/macOS not tried |
| Build 135 on a player | INSTALLED BEFORE PUBLISH | seq 9802, Acknowledged, healthy |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.34 (Baseline 135, sequence 9802).

## BETA-8.35 (Baseline 136) headphone drive: milestone gap audit — 2026-10-25

Boundary: user report F45 (FiiO FH7 IEM too quiet at High); owner: plan, then "follow your plan" without a meter, "keep as is and publish". Change: Reborn only (Master per level, dB volume scale, safe-volume warning, migration). No kernel, platform, memory map, partition or packaging change; session schema unchanged (additive settings fields).

| Area | State for Beta 8.35 | Evidence / gap |
| --- | --- | --- |
| Level gain staging (HP-LEVEL-EQ) | CHANGED, HOST- AND DEVICE-CHECKED | Master −9/−6/0 dB live on the owner's player; output not measured with a meter |
| Hearing safety | NEW, HOST- AND PARTLY DEVICE-CHECKED | warning + agreement on device; 20-h lapse, BT-return cap and restart cap host-tested only |
| Volume migration | DEVICE-CHECKED | 80 → 76 at Low on the owner's player |
| Build 136 on a player | INSTALLED BEFORE PUBLISH | seq 9902, Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.35 (Baseline 136, sequence 9902).

## BETA-8.36 (Baseline 138) issue fixes and menu order: milestone gap audit — 2026-10-25

Boundary: owner: assess all open GitHub issues in the code, fix, test on the player, then "do the implementation and redesign of the UI as proposed", consistent everywhere. Change: Reborn (fixes, menus, Customize, filters, skin engine `label_end`) and `reborn-supervise` (report on Couldn't Start). No kernel, platform API, memory map, partition or packaging change; settings gain two defaulted fields, session schema unchanged.

| Area | State for Beta 8.36 | Evidence / gap |
| --- | --- | --- |
| Issue bugs #43, #60, #32, #40 | FIXED, HOST- AND DEVICE-CHECKED | tests fail without the fixes; owner's player with tagged test files |
| Couldn't Start report | NEW, HOST- AND DEVICE-CHECKED | forced failures on the owner's player; report copied over MTP |
| Menu order, Customize, genre albums, Album Artists, wheel seek, audiobook Cover Flow | NEW, HOST- AND DEVICE-CHECKED | consistency test; previews 09b, 17g, 17h, 51c, b2; device walk-through |
| Haptics (#28) | NOT STARTED | needs a vibration-motor driver (PMIC VIBR): new hardware subsystem, own evidence first |
| Build 138 on a player | INSTALLED BEFORE PUBLISH | seq 10050, Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.36 (Baseline 138, sequence 10050).

## BETA-8.37 (Baseline 144) sleep timer, search, scrolling: milestone gap audit — 2026-10-25

Boundary: owner requests (#29 "build it with your list", #44 "do it all as proposed", the playlist focus and "headers stay, scroll only the list everywhere"). Change: Reborn only (UI, skins, icon sheet). No kernel, platform, memory map, partition, packaging, session or settings change.``

| Area | State for Beta 8.37 | Evidence / gap |
| --- | --- | --- |
| Sleep timer picker, skins' {sleep} | NEW, HOST- AND DEVICE-CHECKED | picker, hours, redraw while paused, Classic |
| Search Back / empty start / playlists / See All | NEW, HOST- AND DEVICE-CHECKED | owner library and SD playlists |
| Scrolling (headers stay, lists scroll) | CHANGED, HOST- AND DEVICE-CHECKED | tests; owner checked on device |
| Build 144 on a player | INSTALLED BEFORE PUBLISH | seq 10200, Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.37 (Baseline 144, sequence 10200).

## BETA-8.38 (Baseline 146) Bluetooth pause and live wave: milestone gap audit — 2026-10-25

Boundary: user report 73547e56 (F43, AirPods Pro 2) and the owner's wave request ("all of A, the live wave, not a real visualizer yet"), "publish". Change: Reborn only (pause path, wave drawing, audio-thread meter). No kernel, platform, memory map, partition, packaging, session or settings change.

| Area | State for Beta 8.38 | Evidence / gap |
| --- | --- | --- |
| Bluetooth pause/resume (F43) | CHANGED, EVIDENCE-BASED | report timelines; ear confirmation by the reporter owed |
| Wave anti-aliasing and levels | NEW, HOST- AND DEVICE-CHECKED | meter tests; previews; device frames, ≈1.7 ms CPU a frame |
| Build 146 on a player | INSTALLED BEFORE PUBLISH | seq 10310, Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.38 (Baseline 146, sequence 10310).

## BETA-8.39 (Baseline 153) Folders, Shuffle Albums, playlist Sort, 120 000 songs: milestone gap audit — 2026-10-26

Boundary: a Reddit user report (512 GB card, 33 000 → 120 000 MP3s, folder-first) and the owner's "do all phases then test on the player, also 120k library", then "yes do all of it" (publish). Change: Reborn only (library views, queue shuffle, playlist worker, caches). No kernel, platform, memory map, partition or packaging change; settings gain two fields read with defaults.

| Area | State for Beta 8.39 | Evidence / gap |
| --- | --- | --- |
| Folders by file name, folder play order | NEW, HOST- AND DEVICE-CHECKED | UI tests; previews; Clubland order and Next on the player |
| Shuffle Off / Songs / Albums | NEW, HOST- AND DEVICE-CHECKED | core tests; Now Playing step and queue on the player |
| Playlist Sort | NEW, HOST- AND DEVICE-CHECKED | UI tests; on the player, kept across a restart |
| 120 000-song library | MEASURED ON THE PLAYER | performance traces before/after; real-size files 500 only; not listened to |
| Build 153 on a player | INSTALLED BEFORE PUBLISH | seq 10470, Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.39 (Baseline 153, sequence 10470).

## BETA-8.40 (Baseline 154) power off on a charger: milestone gap audit — 2026-10-27

Boundary: user report 149a9d81 (install 02f46e9f: "will not charge while the power is off", ledger F46) and the owner's "do the fix for our software and push as 8.40". Change: kernel power-off path only (charger driver sys-off handler, charger DT node gains an RGU reference). No platform userspace, Reborn, memory map, partition or packaging change.````````````

| Area | State for Beta 8.40 | Evidence / gap |
| --- | --- | --- |
| Power off with a charger (F46) | CHANGED, STOCK-DERIVED, DEVICE-CHECKED | REA of the FM kernel (mt_power_off, arch_reset, wdt_arch_reset), preloader boot-reason strings and LK (is_force_boot, kernel_power_off_charging_detection); host test; owner player mode=8 reason=3, unplug switches off |
| Power off without a charger | UNCHANGED | handler returns before any write; BBPU power-off as before |
| Build 154 on a player | INSTALLED AFTER PUBLISH | owner's instruction; seq 10500, Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.40 (Baseline 154, sequence 10500).

## HAPTICS (#28) vibration motor: entry gap audit — 2026-10-27

Boundary: owner: research the internal speaker and haptics with REA and the stock sources, then "start with haptics". New hardware subsystem (MT6323 VIBR LDO as a force-feedback input), so this entry precedes the code. Evidence: REA of the stock FM kernel (`vib_mod_init`, `vibr_power_set`, `vibrator_enable`, `dct_pmic_VIBR_enable/sel`, cust `{50 ms, 9, 5}`), the golden comparison row `vibr_ther_shen_en` and upstream `mt6323-regulator` (`docs/planning/SPEAKER-HAPTICS-PLAN.md`). No device evidence yet: the motor has never run under Linux.``````

| Area | State before the change | Plan / gap |
| --- | --- | --- |
| VIBR rail | NOT DECLARED; writes refused by the PWRAP policy | ldo_vibr 1.8..2.8 V; policy admits 0x542 enable + thermal bit, 0x544 selectors 3..5 only (stock 2.8 V is the ceiling) |
| VIBR thermal shutdown | MISMATCH vs stock (golden row) | set once at boot by pmic-lowpower, never cleared (transport guard) |
| Motor driver | NOT BUILT | upstream regulator-haptic (CONFIG_INPUT_REGULATOR_HAPTIC), suspend switches it off |
| Reborn | NO HAPTICS | Customize > Haptics Off/Light/Strong (default Off); one 30 ms tick per handled wheel step/button on a lit screen, ≥45 ms apart |
| Device checks | OWED | motor runs; Light/Strong felt; fast spin responsive; rail off after sleep; overnight drain unchanged |

Gate decision: ready for a host build and an owner-installed test build; not release-qualified until the device checks pass. Speaker (no issue yet) stays planning only.

## SPEAKER (internal speaker) entry gap audit — 2026-10-27

Boundary: owner: "keep stock [haptics] for now and work on the speaker now". New hardware subsystem (AW87559 / OCA72559 amplifier on I2C1 0x58 behind the CS43131, GPIO8 enable) and jack detection. Evidence: REA of the stock FM kernel (`aw87559_on/off`, `Sound_Speaker_Turnon/off`, `cs43131_apply_route`, `cs43131_apply_out_fs`, `cs43131_refresh_volume_for_route`, `cs43131_hp_work_callback`, `cs43131_early_suspend`, `cs43131_power_down_hw`), the donor driver (tables identical to stock), the player's own regmap (detector cached 0xC4, never read; "Headphone Jack" never reported) and `docs/planning/SPEAKER-HAPTICS-PLAN.md`. The speaker has never played under Linux.````

| Area | State before | Plan / gap |
| --- | --- | --- |
| Amplifier | GPIO8 hogged low, no driver | donor aw87559.c (stock tables, timings); registers even without an answer so the headphones never depend on it |
| Route | headphones only | codec writes stock speaker route at HP power-up from the card's Speaker pin: PCM path 0x05, ASP ch2 left slot, OUT_FS 1.73 Vrms |
| Exclusivity | — | one pin on turns the other off; switching under a running stream refused (speaker level into earphones); speaker refused while the detector reads a plug |
| Jack detection | none (no codec IRQ; EINT16 would break the #52 crystal polling) | 200 ms HP_STATUS poll only while the codec is powered (stock detects only then too); plug turns the speaker off at once; __pm_runtime_put_autosuspend so the poll never keeps the DAC up |
| Reborn | — | jack via "Y2Audio Headphone" SW events; Output > Speaker (on); mono (L+R)/2 downmix (DAC plays the left slot only); Master −3 dB (stock top); plug moves to headphones, unplug pauses |
| Device checks | OWED | amp chip ID; detector bit live; audible, no pop; plug/unplug while playing and paused; screen-off playback; sleep and drain unchanged |

Gate decision: ready for a host build and an owner-installed test build together with the haptics change; not release-qualified until the device checks pass.

## BETA-8.41 (Baseline 159) internal speaker and haptic feedback: milestone gap audit — 2026-10-27

Boundary: the HAPTICS (#28) and SPEAKER entry audits above, test builds 155–158 on the owner's player, then the owner's "do the build and publish it". Change: kernel (VIBR rail and policy, regulator-haptic, AW87559 driver, card Speaker pin and exclusivity, codec speaker route and jack poll in overlay 0030, DT, validator) and Reborn (haptics, jack, speaker output, mono gain, `rebornctl jack`). No memory map, partition or packaging change; settings gain `haptics` and `speaker` read with defaults.````

| Area | State for Beta 8.41 | Evidence / gap |
| --- | --- | --- |
| Haptics (#28) | NEW, STOCK-DERIVED, DEVICE-CHECKED | motor felt at Light/Strong (155); 60 ms stock tick per press chosen by the owner; overnight drain owed |
| Speaker | NEW, STOCK-DERIVED, DEVICE-CHECKED | OCA72559 answers; stock route registers live; owner heard it; long listening and drain owed |
| Headphone detection | NEW, DEVICE-CHECKED | real plugs 1 → 0 → 1, kernel speaker-off on plug while playing; detection only while the codec is powered (as stock) |
| Output paths | DEVICE-CHECKED (simulated jack via rebornctl jack) | nine paths on 158, all as intended; "Starting" hang of 157 fixed |
| Build 159 on a player | NOT INSTALLED BEFORE PUBLISH | test build 158 (same code apart from rebornctl jack flag parsing) installed |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.41 (Baseline 159, sequence 10700).

## BETA-8.42 SD admission in the background (F49) and Reborn quick scan: entry audit — 2026-10-27

Boundary: report `d32f8f3c` (8.41, 1 TB exFAT, 71 400 songs) and the owner's "implement the fix" / "implement the folder mtime skip too", committed without a build ("commit but don't publish yet"). Change: platform SD admission (`media.py`, `service.py`, `observe.py`, `cli.py`) and Reborn's library walk. No kernel, memory map, partition or packaging change; Reborn's database gains two additive tables (schema version unchanged).````````````

| Area | State before | Plan / gap |
| --- | --- | --- |
| SD admission check | one fsck -n with 60 s, timeout = read-only + Repair | 20 s for FAT32/exFAT, then mounted read-only as checking and checked by media verify (30 min, no lock); ext4 unchanged (60 s, refused on failure) |
| Writes during the check | — | refused (card_being_checked); USB gets its window on the tick after the pass |
| Repair | offered for a timeout | only for findings or a background check that never ends |
| Sleep during the check | — | a failed check read across a sleep is no verdict and runs again |
| Restart scan | every folder read (62–70 s for 70 500 files on exFAT) | unchanged folders skipped while exFAT/ext4 free space is unchanged; FAT32 and Scan for Music read every folder |
| Missed by the quick scan | — | edits on a computer that change neither folder time nor free space (most tag edits) until Scan for Music |
| Device checks | OWED | slow card plays at once, checking → protected, MTP writable after the pass, sleep and card pull during the check; restart scan timing before/after |

Gate decision: ready for an owner-installed test build (label 162); not release-qualified until the device checks pass.

## BETA-8.42 (Baseline 163) sleep, SD admission, report fixes: milestone gap audit — 2026-10-28

Boundary: the BETA-8.42 entry audit above, the review of 40 error reports (findings F50–F57), issues #62/#63, test builds 160–162 on the owner's player, then the owner's "do a build now and publish". Change: kernel (UART pad in sleep, DSI restart and read policy, connectivity IRQ, last power-off handler and `watchdog_powers_off`, PMIC power status), kernel config `CONFIG_LOG_BUF_SHIFT` 19 (Image 1.6 MiB under the D08 12 MiB cap instead of 5.4 KiB over; the 1 MiB log is allocated from `log_buf_len=1M`, no other memory map change), initramfs (partition wait, recovery watchdog), platform (shutdown steps, SD admission, Wi-Fi heal, battery, sleep floor, factory provider), Reborn (sleep, quick scan, lost Bluetooth peer, Wi-Fi reasons, held Power, EACCES). No partition or packaging change.

| Area | State for Beta 8.42 | Evidence / gap |
| --- | --- | --- |
| Sleep (F47/F48) | DEVICE-CHECKED | 17.3 h asleep on 161 (≈2 mA estimate), no kernel refusal |
| Shutdown (F39/F50) | DEVICE-CHECKED (restart only) | full pmsg trail on 162; watchdog power-off and a real stall not exercised |
| SD admission (F49), quick scan | HOST-TESTED | slow card and restart timing owed |
| #62 empty PROTECT | HOST-TESTED | reporter's player owed (modem defaults, range) |
| Wi-Fi heal, battery, held Power, lost peer | HOST-TESTED | device checks listed in the Beta 8.42 report |
| Dark start (F17) | DEVICE-CHECKED (no false restart) | a dark start not reproduced |
| F56 | DIAGNOSTICS ONLY | cause open |
| Build 163 on a player | NOT INSTALLED BEFORE PUBLISH | test build 162 (same code apart from #62 and the sequence) installed and Acknowledged |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.42 (Baseline 163, sequence 10900).

## BETA-8.43 (Baseline 164) Y2Reborn issue fixes: milestone gap audit — 2026-10-28

Boundary: triage of the 25 open Y2Reborn issues against 8.42, the owner's "do the bugs and quick wins, build 8.43", test build 164 on the owner's player, then "publish and answer the issues". Change: Reborn only (search exit, album-artist unification on the library thread, Home visibility, queue origin, skin gradient recolour, album order, letter steps, unplug toast, haptic ticks). No kernel, memory map, partition or packaging change; settings and session gain fields read with defaults.

| Area | State for Beta 8.43 | Evidence / gap |
| --- | --- | --- |
| Home visibility, Album Order, unplug message, Go to fallback | DEVICE-CHECKED (over SSH, screenshots) | Radio hidden and shown again on the owner's player |
| Search exit, letter steps, haptics, shelf, Go to source | HOST-TESTED | by hand on a player owed |
| Build 164 on a player | INSTALLED, Acknowledged | published images are build 164 |

Gate decision: published at the owner's word as Y2Linux 1.0.0-beta.8.43 (Baseline 164, sequence 11000).

## PLATFORM-RUST phase 1 (Rust dispatcher for `/usr/sbin/y2-platform`): entry audit — 2026-10-28

Boundary: the owner's "go ahead with phase 1" after Phase 0 of the [platform port plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FPLATFORM-RUST-PORT-PLAN.md) and the owner decisions of the same night (contract crate in Y2Linux, Reborn carries a stamped copy; known defects ported 1:1 and fixed after Phase 6). Hardware evidence: the Phase 0 measurements on test build 165 (owner's player, plan §7), boot stages of 165 and of the previous 8.43 boot (pmsg trail). Limitations: the idle window was 9 min and the playing window 10 min, awake current is not measurable on the charger, and no overnight drain on 165 exists (owner: not possible yet), so the Python drain baseline is still the 161 estimate (≈2 mA).

Change: packaging/architecture. A new Cargo workspace `platform/` (`y2p-core`, `y2p-contract`, `y2-platform`, vendored serde/serde_json/libc/ryu at Reborn's pins, Rust 1.99.0) and Buildroot package `y2-platform`; the Rust binary replaces the shell wrapper at `/usr/sbin/y2-platform` and, in this phase, hands every subcommand to `/usr/bin/python3 -I /usr/lib/y2-platform/main.py` by `exec` (same PID, argv, environment, stdio). Python, its modules and every other script are installed as before. Reborn gains `crates/y2p-contract` (copy) and uses its schema names. No kernel, device tree, memory map, partition, recovery or update-format change.````````````

| Area | State before | Phase 1 / gap |
| --- | --- | --- |
| /usr/sbin/y2-platform | shell exec python3 … | Rust exec of the same command; host tests: argv/env/stdin/PID/exit code identical, 16 differential cases Rust vs Python identical |
| Exec cost per call | sh start + Python | Rust start + Python (≈ the same; the CPU win starts in phase 2) |
| Image | 130 MB tree | +0.4 MB (one binary) |
| Contract types | hand-written strings on both sides | y2p-contract (schema names, boot stage/record, health, capabilities, status envelope, error record) checked against Python goldens; release.py build refuses a differing Reborn copy |
| 165 device checks (sleep cycles, overnight, power-off holding Power, update restart) | OWED | still owed; 166 stacks on 165 |
| Device checks for phase 1 | — | DEVICE-CHECKED on test build 166 (below) |

Gate decision: ready for an owner-installed test build (label 166, sequence above 11100); not release-qualified.

Device result, test build 166 (Linux `10f884c`, Reborn `bd96685`, sequence 11110, rootfs v1.208; owner's player): staged OTA from 165 → health boot `1520bf4a`Acknowledged; `/usr/sbin/y2-platform` is the 302 KB ARM ELF, the four daemons run with the same command lines, supervisor logs empty, taint 0. Exit codes and shapes as before (error record exit 1, argparse exit 2 naming `main.py`); the dispatcher adds 4–22 ms per call (`capabilities` 0.541 s, 165's wrapper 0.547 s). Restart on 166 (`shutdown reboot --reason user`): pmsg `execute` → `init_reboot ok`in 2.57 s, watchdog and long-press reset ok, orderly, warm; boot`8f497227` platform_start 8.72 s, application_ready 44.44 s (a plain restart; the 12.5/48.6 s of Phase 0 were first boots after an update). Settings and About & Updates show their platform data. One sleep cycle unplugged (owner): 261.6 s asleep, same boot, `complete_result_0`, radios restored. Still owed: overnight on the dispatcher (and 165's power-off with Power held). Phase 2 admitted for source work and host tests; its device checks follow on the next test build. Phase 2 (the first Rust subcommands) is admitted only after 166's device checks pass; the overnight drain on the dispatcher build is owed before phase 5 (power) at the latest and is recommended before phase 2's CPU comparison. No milestone is promoted or closed.

## PLATFORM-RUST phase 2 part 1 (short commands in Rust): entry audit — 2026-10-28

Boundary: the owner's "ok do phase 2" after the phase 1 device check on test build 166 (above). Change: `capabilities`, `sleep status`, `time`, `time-remember`, `ntp-event`, `boot-stage` (incl. the `application_ready` power features and the panel record/hint), `codec-runtime`, `wifi-event`, `dhcp-event`, `cpu-idle-policy` run in Rust for their exact argument forms (platform/CONTRACT.md "Ported to Rust"); all else still runs in Python. These sit in the boot path (S03y2-platform, reborn-boot-services, S05y2-cpu-idle, connectivity), the shutdown path (`boot-stage shutdown_*`, `time-remember`), the Wi-Fi path (wpa-event, udhcpc) and ntpd's callback. No kernel, memory map, partition or packaging change beyond the binary.

| Area | Evidence | Gap |
| --- | --- | --- |
| Behaviour | 62 differential cases Rust = Python (records, files, modes, subprocess requests, errors, fallbacks) | fixture only |
| Boot stages, power features, cpu idle, codec arguments | — | OWED on test build 167: same records as 166, boot timing |
| Shutdown trail (F39/F50 timing) | 166: journal_pending 0.54 s, time_remember 0.54 s, journal_complete 0.59 s | OWED: restart on 167 |
| Wi-Fi events | — | OWED: association/DHCP on 167 (owner's Wi-Fi is on) |
| Overnight drain | none on the dispatcher yet | owed |

Gate decision: ready for an owner-installed test build (label 167, sequence 11120); not release-qualified. Part 2 (`status`, `health`, `boot-evidence`, `network-check`) continues as source work.

Test build 167 did not carry phase 2 part 1 (found on the player: Rust and Python took the same 0.54 s per call; `/usr/sbin/y2-platform` was byte-identical to 166's, and `out/build/buildroot/build/y2-platform-1` still held phase 1's source). Cause: the package version was a fixed `1`, so the resumed build reused the old build folder. Fix: `Y2_PLATFORM_VERSION` is the git tree of `platform/` (a build fails without one), and `release.py` prunes older `y2-platform-*` folders. 167's device result is therefore phase 1 again (Acknowledged, records identical to 166, restart orderly); the part 1 device check moves to test build 168 (sequence 11130).

Device result, test build 168 (Linux `cf86abc`, sequence 11130; `/usr/sbin/y2-platform` 634 KB, new hash): staged OTA → health boot Acknowledged, taint 0. Ported commands on the player: `capabilities` 15 ms, `sleep status`8 ms,`time`8 ms,`time-remember`17 ms,`codec-runtime` 9 ms (Python 527–541 ms each). Boot records as 166's (power features, CPU idle `Enabled`, BlueALSA arguments); Rust `dhcp-event` took the real lease (`Authenticated`), Rust `ntp-event` wrote time.json. Restart: `execute` → `init_reboot ok` in 1.20 s (166: 2.57 s; journal_pending 0.02 s, time_remember 0.01 s, journal_complete 0.02 s, each 0.54–0.59 s before), orderly; plain boot platform_start 8.23 s, services_started 22.06 s, application_ready 40.59 s (166: 8.72/23.75/44.44). Owner (2026-10-28): continue until all phases are done and Python is removed; the owner runs the hardware tests.

## PLATFORM-RUST phases 2–6 (whole platform in Rust, no Python on the player): entry audit — 2026-10-29

Boundary: the owner's "continue till all phases are done and python is removed" and "i want a full implementation"; the owner runs the hardware tests. Hardware evidence so far: test builds 166 (dispatcher) and 168 (short commands in Rust: calls 8–17 ms, restart trail 1.20 s, boot 3.9 s sooner). Change: **packaging and architecture** — every subcommand, the four daemons, the sleep helper and the platform scripts run in the Rust `y2-platform` (groups in plan §5a, merged on `main`); the dispatcher parses arguments as argparse did; the image has no Python (`BR2_PACKAGE_PYTHON3*` removed, post-build links the programme names to `y2-platform` and refuses an image with Python); validators updated. No kernel, device tree, memory map, partition or recovery change.

| Area | Host evidence | Device gap (owner) |
| --- | --- | --- |
| Every command | differential cases per group, Rust = Python (stdout, exit, files, subprocess requests), argparse corpus 5 700 | OWED on test build 169 |
| Daemons (power, service, connectivity, ssh) | tick cases, live socket test (power) | boot, idle CPU/RSS vs Phase 0, Wi-Fi/BT, USB MTP/SSH |
| Sleep, battery, charging, shutdown | product-sleep and power cases | 10 sleep/wake cycles, two overnight runs, low battery to power-off, charger plug/unplug, power-off on a charger, update restart |
| Storage, update, reports | cases incl. archives, scrubber, update stage/apply | SD insert/remove/repair, OTA + rollback, report save/send |
| Image | — | Python gone (≈21 MB), y2-platform size |

Known host-test issue: two product-sleep differential cases are timing-sensitive under load (Python against Python too); they pass when run alone. Gate decision: ready for an owner-installed test build (label 169, sequence 11140, `release.py build --clean`: Buildroot does not remove a disabled package from the target); not release-qualified until the owner's device checks above pass.

Device result, test build 169 (Linux `5640949`, Reborn `dc38c55`, sequence 11140; first build failed on the 32-bit ARM target, fixed with the 64-bit file interfaces and time widths; the second on the argparse generator in the container and the y2-status link in `validate.py`): staged OTA from 168 → health boot **Acknowledged by the Rust `update health-ack`**; no `/usr/bin/python3`, no `/usr/lib/y2-platform`; the four daemons are `/usr/sbin/y2-platform <daemon>`: 15.2 MB RSS / 4.6 MB PSS together (Python 58.4 / 35.0), idle CPU 19.6 s/h with Wi-Fi on (Python 91.8 s/h, Wi-Fi off); taint 0, supervisor logs empty. Restart: every shutdown step in order, `execute` → `init_reboot ok` 0.46 s (Python 2.57 s), watchdog and long-press reset ok; boot application_ready 36.8 s (Python 44.4 s plain, 48.6 s after an update; this update boot 37.6 s). Reborn's About & Updates shows its platform data. Root tree 111 MB (130). Owed to the owner: sleep cycles, two overnight runs, low battery to power-off, charger plug/unplug (also asleep), power-off on a charger, SD insert/remove/repair, Internal Storage, an OTA from 169 and a rollback, error report save/send, MTP/SSH, Wi-Fi join/wrong password, Bluetooth.

## PLATFORM-RUST after the port: carried defects fixed, Rust-only tests (test build 170): entry audit — 2026-10-29

Boundary: the owner's "start fixing the defects … i want to have the newest build installed on my player and no python should be in that build … going forward, we only have the rust code", and (later) "just put it on the player and then review and see what works". Hardware evidence so far: test build 169 (the Rust platform, no Python on the player; Acknowledged, daemons 15.2 MB RSS, idle 19.6 s/h, restart trail 0.46 s, boot 36.8 s). The owner's hardware checks on 169 are not done yet; 170 replaces it on the player and carries them. Change: behaviour fixes in the platform (the ten defects carried 1:1, CONTRACT.md table: SFTP root on Internal Storage, `media status`/`media write` exit codes, busy update lock, rollback battery gate before the core, auto-check skip reasons, `firmware scan` exit code, battery fuel-gauge sample, expired SD write window, DHCP renew keeping dns.json; Reborn: a message for `update_in_progress`) and test/tooling only elsewhere: the Python reference platform (`tools/platform`) is deleted, its ≈630 unit tests are Rust tests (608 Rust tests in all), the Python-vs-Rust harness is a golden suite against the Rust binary (1 063 goldens recorded from Python, 22 re-recorded for the fixes), host tools moved to tools/host and tools/production, the release's firmware-free check reads the stock radio files with the Rust reader (same seven files byte for byte). Port bug found by the test port: `media::change_card` ran grow for an unknown action (unreachable from the CLI; fixed). No kernel, device tree, memory map, partition, recovery or package-set change (the image already had no Python).

| Area | Host evidence | Device gap (owner) |
| --- | --- | --- |
| Fixed defects | a Rust test each, golden diffs reviewed | SFTP opens Internal Storage; SD write window closes after use; Wi-Fi stays Online across a DHCP renew |
| Update (Rust stage/apply never ran on a player: 169 was installed by 168's Python update) | update unit/golden cases | the 169 → 170 OTA itself, then an OTA and a rollback from 170 |
| Sleep, battery, charging, shutdown | suspend/power Rust tests, goldens | sleep/wake cycles, two overnight runs, low battery to power-off, charger plug/unplug, power-off on a charger |
| Storage, reports, MTP/SSH, Wi-Fi, Bluetooth | group Rust tests, goldens | SD insert/remove/repair, report save/send (curl), MTP copy, SSH/SFTP, Wi-Fi join and wrong password, BT headphones |

Host: `tools/development/host-tests.sh` 577 OK (1:40, was 7:43 with the Python comparison), `cargo test` 608 OK (repeated runs), clippy clean, armv7 check clean. Gate decision: ready for an owner-installed test build (label 170, sequence 11150); not release-qualified until the owner's device checks above pass. The code-quality refactor is planned separately ([PLATFORM-RUST-REFACTOR-PLAN.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FPLATFORM-RUST-REFACTOR-PLAN.md)) and starts only after these checks.

Device result (2026-10-29, owner's player, from 169 by staged OTA):`update stage --package` (Rust, first time on a player) Queued sequence 11150 in 8.8 s, `update apply` restarted into the installer, Acknowledged by the Rust health-ack 86 s after apply; boot platform_start 6.63 s, services_started 20.06 s, application_ready 37.67 s; the four daemons 3.4–4.4 MB RSS each; no Python in /usr/bin. Fixed defects visible on the player: SFTP opens `/media/internal/music` (real SFTP session), `update auto-check` prints `{"result": "skipped", "reason": "not_due"}`, `media status` exits 0. The owner's hardware checks above are still owed.

## PLATFORM-RUST refactor (ported Python → idiomatic Rust, test build 171): entry audit — 2026-10-29

Boundary: the owner's "just do the refactoring plan now and after you are finished install via ota" ([plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FPLATFORM-RUST-REFACTOR-PLAN.md), decisions recorded there). Hardware evidence: test build 170 on the owner's player (first Rust OTA, Acknowledged, SFTP fix confirmed); the owner's hardware checks on 170 are **not done — they move to 171, with 170 as the comparison point. Change: architecture of the platform code** (one shared core, one JSON model, test injection instead of seams, typed records, module splits) with three deliberate behaviour changes (argparse replaced; crash paths → refusal records; same-lease DHCP renew is a no-op), all visible as golden diffs. Contract fixed points (plan §3) unchanged: Reborn's JSON fields and failure strings, the compact records scripts grep, persistent /data formats, multicall names, stdout JSON formatting. No kernel, device tree, memory map, partition, recovery or package-set change. Gate: host suite + cargo tests + goldens green, then test build 171 by OTA; not release-qualified until the owner's checks pass on it.

Device result (2026-10-29 evening, owner's player, from 170 by staged OTA): test build 171 (sequence 11160, the refactored platform: one shared core, typed records, split modules, cli.rs parser, refusal records instead of tracebacks, same-lease DHCP renew without `ip` commands) staged by 170's Rust update, applied 20:15:35, Acknowledged by 171's health-ack 20:17:01 (86 s); boot platform_start 6.52 s, services_started 19.85 s, application_ready 37.45 s; daemons 3.4–4.5 MB RSS each; the daily update check reached the server over Wi-Fi; SFTP root Internal Storage; help says y2-platform, an abbreviated option is refused (exit 2). Host evidence before the build: cargo test, clippy, armv7 check, golden suite, host suite 576 OK, byte comparison against the pre-wave-2 build: every difference is a deliberately re-recorded golden. The owner's hardware checks (PLATFORM-RUST-PORT-HANDOFF.md §6 A) are owed on 171; 170 (sequence 11150) is the comparison point.

Test build 172 (2026-10-29, the refactor's quick wins, PLATFORM-RUST-REFACTOR-PLAN.md): no behaviour change intended (byte comparison against 171 at every step, host suite OK, build container 549 tests). On the owner's player from 171 by staged OTA: applied 21:33:53, Acknowledged 21:35:19 (86 s), application_ready 37.51 s; the four daemons 3.3–4.5 MB RSS; `status wifi` and the connectivity daemon's network.json agree (Online, DNS ready, −52 dBm: one Wi-Fi observer now); clock TLS-ready from NTP; SFTP root Internal Storage; codec-runtime arguments as before. The owner's hardware checks (PLATFORM-RUST-PORT-HANDOFF.md §6 A) are owed on 172; 171 and 170 are the comparison points.

Test build 173 (2026-10-29, duplication pass and idle gains, PLATFORM-RUST-REFACTOR-PLAN.md): byte comparison against 171 at every step (0 differences), host suite 576 OK, platform tests 5 clean runs. On the owner's player from 172 by staged OTA: applied 21:52:47, Acknowledged 21:54:18 (≈91 s), application_ready 40.3 s; `status wifi` equal to `wpa_cli status`/`ip -j -4 addr|route`/`signal_poll` (Online, BSSID, address, default route text, −37 dBm), supplicant query 0.48 ms; ssh.json Ready; `rebornctl metrics` 0.01 s, `status --reborn` +10 ms over `status`. Idle, screen off (bl_power 4), charging, 300 s window from 6 min uptime: Reborn 19.0 s/h (172: 45.0; main thread 9.4 from 24.6, watchdog 3.4 from 14.4), process starts 33.6/min (172: ≈140), power-daemon 8.9, service-daemon 10.2, ssh-daemon 1.9, connectivity-daemon 0.1 s/h (172: 7.8/7.8/2.1/0.0, measured later after boot; within the window's noise and boot-time work, not a regression shown). power.json is still rewritten every second (10 inodes in 10 s): the intended change test sees the raw ADC voltage change each sample. Idle process starts after start-up ≈10/min (PID counter over 60 s), mostly kernel workers.

Test builds 174 and 175 (2026-10-30, the refactor plan's next pass P1–P9): every step byte-identical against 171 except deliberately re-recorded call lists (a volume probed alone: transfer commit blkid 8 → 4; the service daemon's space policy in process: 31 service goldens lose the `y2-platform space --cleanup` child; diagnostics export one snapshot), host suite 576 OK. On the owner's player by staged OTA: 174 (seq 11190) Acknowledged, Wi-Fi power policy Ready with the nl80211 readback equal to `iw` (off/off), usb0 10.42.0.1/24 equal to `ip`, Wi-Fi Online, storage.json written by the service daemon, SSH Ready, health OK (Bluetooth UNAVAILABLE: radio off). power.json was still written every second on 174 (the estimate's own figures flicker near a step); 175 (seq 11200, applied 01:20:18, Acknowledged by 01:22:59) leaves them out of the change test: 10 writes in 20 s. Idle on 174, screen off, charging, 300 s at 5–10 min uptime: power-daemon 7.3, service-daemon 7.7, ssh-daemon 1.9, connectivity 0.1, Reborn 14.4 s/h (main 6.0, watchdog 2.4). Owed: a long-uptime idle measurement on 175, the owner's dark-wake checks (Power, USB plug, Bluetooth Play, automatic sleep on battery), handoff §6 A. Owed: the owner's dark-wake checks (Power, USB plug, Bluetooth Play, automatic sleep on battery) and PLATFORM-RUST-PORT-HANDOFF.md §6 A.

Test build 176 (2026-10-30 night, PLATFORM-RUST-NEXT-AGENT-HANDOFF.md §4 A–F, one agent, owner asleep): every step byte-identical against the 175 code (tools/development/platform-gate.sh, baseline from 2e68d63e, no golden re-recorded), host suite 576 OK. Staged on the owner's player from 175 (Queued, seq 11210) and applied 03:48:30 (host clock); the host saw the usual sequence (preloader twice, then the Y2 gadget at 03:49:23, MTP + ECM) but the USB network never carried a packet: host cdc_ether transmit timeouts 03:49:29–03:50:00, rx 0 packets, ARP for 10.42.0.1 FAILED, SSH "No route to host" at +4.5, +6, +11 min and after re-activating the host's NM connection. MTP from the host (KDE KIO) listed "Internal Storage" and "SD Card": the player's userspace and the USB service run; only usb0 on the player is down or has no address (S20y2-usb sets 10.42.0.1 once, when usb0 first appears). Update state (Acknowledged or not) and the device check could not be read. Owner's rule for this case: write down and stop — no further install, no 177, no idle measurement. Owed (owner): look at the player's screen / Software Update page; replug the USB cable (a new enumeration) and check `ip addr show usb0` and `update status` on 176; if 176 is at fault, the commits after 2e68d63e are the suspects (none touches usb0 or S20y2-usb directly; the USB tick's views became a typed struct in 82503b14). 176 afterwards (2026-10-30 morning): the owner replugged the cable at 07:34; usb0 answered at once and 176 was Acknowledged (seq 11210, 6fd3e065, no reboot since the install, uptime 3:48). Cause class, from both kernels: on the player usb0 had 10.42.0.1/24 from 10.7 s (`Y2NET: usb0 … ready`), so the address script was fine; on the host cdc_ether logged `NETDEV WATCHDOG: transmit queue 0 timed out` 11 times (03:49:29–05:00:11), i.e. the gadget's bulk-OUT (ECM) endpoint took no packet from the host until the re-enumeration. The gadget was not rebound in between (one host register 03:49:23, the next 07:34:25). This is the only transmit timeout in the host's journal (kept since 2026-10-26), across ≈10 OTA/restart enumerations on 10-29/30 including 175; 177's OTA right after came back clean. The controller counters for the whole boot show no fault (dma_errors 0, m1_fallback 0, nuke 0, restart_flush 0, storm guard and unexplained IRQs 0); the 40-event `rxdiag` ring held only post-replug traffic. 176's diff touches only the MTP view types, not the configfs/ECM setup. Verdict: a one-off ECM OUT stall after an OTA boot, cause not found; if it repeats, read `/sys/devices/platform/11200000.usb/rxdiag` and `status`before replugging (the ring is overwritten by the new traffic). Device check on 176: all OK (health OK, Bluetooth UNAVAILABLE: radio off). Idle on 176, screen off, charging, 300 s at 231 min uptime: power-daemon 6.2, service 7.7, ssh 2.0, connectivity 0.1, Reborn 14.5 s/h (main 6.0, wifi 3.0, watchdog 2.3, avrcp 1.3).

Test build 177 (2026-10-30 morning): 176 + the SD inventory/USB tick skipping the 11 eMMC entries after one readlink (979f124b, 3d2bd3b0) and the power daemon's pread of BAT0 from kept descriptors (db11884f); host suite 576 OK. Staged from 176 (seq 11220, 9f708af2), applied 07:46:49, Acknowledged at the first check ≈3 min later; host re-enumeration 07:47:47, no transmit timeout. Device check all OK (power.json 11 writes in 20 s at 2.5 min uptime). strace, screen off: the power daemon ≈29 calls per sample (175: ≈46) with 4 preads/s; a dark service pass runs every 10 s at ≈560 calls with 73 readlinks, the eMMC entries one readlink each (18/pass); left in a pass: the SD card's sysfs path resolved component by component 4× (36 readlinks), media-mount.json read 4×, mountinfo 3×. Idle, screen off, battery Full (not charging, unlike 174/176), 300 s at 30.6 min uptime, measured with builtins only (no forks of its own but one sleep): power-daemon 4.1, service-daemon 4.9, ssh-daemon 2.0, connectivity 0.2, Reborn 12.5 s/h (main 5.9, watchdog 2.0, wifi 1.4, avrcp 1.2); process starts 3.0/min (15 in 300 s). Owed: the owner's dark-wake checks, the hands-on event-source checks for handoff §4 I, PLATFORM-RUST-PORT-HANDOFF.md §6 A.

Test build 178 (2026-10-30 late morning; handoff §4 item 9, J3, C, E, F, Reborn 764b024): every step byte-identical against 177's code (platform-gate.sh, baseline from 0e2d066a, no golden re-recorded), host suite 576 OK. Changes: wlan0's 24 traffic counters from one RTM_GETLINK dump (IFLA_STATS64) instead of 24 files per service pass; `y2p_core::sys::real_path` (O_PATH + /proc/self/fd: 3 calls instead of ~13 readlinks per sysfs block path); the application_ready boot stage within a pass of Reborn's first frame once no update waits for health (a plain restart recorded it on the next 30-s maintenance pass: 177's update boot had the first frame at 23.4 s, the stage at 40.2 s); typed status sections power, cpu, idle completion, wifi, storage. Reborn 764b024: after a `charger_or_usb_active` refusal automatic sleep waits while the battery shows a cable (strace on 177, dark on USB: one `y2-platform sleep request` a minute, the only steady process start). On the player by staged OTA: seq 11230, Acknowledged, USB clean; device check OK; `status wifi` counters equal the sysfs files; SD volume Ready through real_path. Idle, screen off, battery Full, 300 s from 30.8 min (builtins-only script): power-daemon 4.1, service-daemon 4.2 (177: 4.9), ssh 1.8, connectivity 0.1, Reborn 13.9 s/h. Reborn's sleep requests on USB: at 123, 1291, 1351, 2450 s instead of every minute; the leaks came from BAT0 reading "Not charging" while the charger holds a full battery (shown as on battery) → Reborn 68af9ac holds on a cable flag (Charging, Full, Not charging). Remaining process starts are event-driven: Wi-Fi idle power-down/up (wpa_cli -g interface_add/remove, ip flush ×4, udhcpc, wpa-event/dhcp-event/wifi-event), the report check (blkid, report work, rebornctl health, dmesg), ntpd's periodic hwclock.

Boot profile (177's update boot, J3): initramfs 0.44 s; storage discovery → rescue_update 6.2 s is the update boot only (e2fsck of Y2DATA + boot-check; a plain restart skips it, platform_start ≈ 8.7 s there); rcS 8.75–9.69 s; S90reborn 9.69 → 22.68 s = boot-gate waiting for the radios (factory records ≈10 s, calibration, then radio-activate: the connectivity driver's `pmic_prepare` has a fixed `msleep(5000)` after the PMIC connectivity settings, then the MD1 calibration boot ends 20.75 s (FS=841 requests served from RAM), WMT patches and RF calibration to 21.4 s, Wi-Fi up 22.6 s); Reborn's first frame 23.4 s. Owner decisions: (a) do the PMIC settings at probe time (normal boot) so the 5 s settle overlaps the boot instead of following S41 (a kernel timing change); (b) let Reborn start before the radios and show Wi-Fi/Bluetooth coming up (boot-gate's design choice).

Test build 179 (2026-10-30, handoff §4 E/F/D/G, Reborn 68af9ac): byte-identical against 177's code (gate OK each), host suite 576 OK. Root::is_this_boot for the record checks (and one setup_status), one sys::poll with each caller's rounding, signal_wake! restores errno, no unsafe in power/unix.rs and suspend/helper/kernel.rs (sys bind_unix/listen/peer_credentials/nanosleep/real timer), the power journal's sleep status is sleep::product, typed status system section, Bluetooth normalize and reset execute split into steps, update health-ack asks Reborn's control socket (observation::reborn_control) instead of starting rebornctl. On the player by staged OTA from 178: seq 11240, Acknowledged by health-ack through Reborn's control socket (no rebornctl process), USB clean (re-enumerated 49 s after the apply); device check OK (health: Bluetooth UNAVAILABLE, radio off); `status system` and `status bluetooth` answer (Bluetooth: radio_off at the adapter step, as before). Update boot: first frame 20.5 s, application_ready 37.4 s (health-ack's, as designed for an update boot). Owed: idle on 179 after ≥ 30 min, Reborn's sleep requests on the cable over an hour (68af9ac), the owner's checks.

Test build 180 (2026-10-30 afternoon; PLATFORM-RUST-IDIOMATIC-PLAN.md P0–P4, owner: byte identity dropped): semantic gate (goldens, record-compat against the last release, Reborn's contract test) OK at every commit, host suite 576 OK. One serde JSON writer (compact records and answers; the SD media identity digest keeps Python's encoding), one argument reading (`cli::given`), records read with Rust types instead of Python comparisons outside the critical code (which keeps Python's number rules explicitly), Bluetooth section typed; Reborn e45604e (charger hold, contract test). On the player by staged OTA from 179: seq 11250, Acknowledged, USB clean; device check OK (compact JSON throughout; the check's greps accept both spellings); ntpd started by S43's new grep (time source ntp); Reborn logged no platform warning or error; `report status` still prints through reports' own Py writer (P6). 179's idle (battery Full, 30.8 min): power 4.2, service 4.6, ssh 1.9, Reborn 14.2 s/h; Reborn's sleep refusals on the cable: 1 in 37 min (68af9ac).

BETA-9.0 (2026-10-30, owner: "make a build and publish it as beta 9.0"): release `1.0.0-beta.9.0`, sequence 11400, root `2026.08-platform-v1.212`, label/tag 186 (`baseline-186`). Content since Beta 8.43 (`baseline-164`): the platform in Rust (port 165–171, refactor 172–179, idiomatic plan P0–P7 and finishing Q1–Q5 180–185), Reborn's dark idle and charger hold, the fixes listed in the [Beta 9.0 report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-LINUX-1.0-BETA-9.0.md) (written for owners). Gate OK on the release commit (formatting, clippy, armv7, host tests, goldens, record-compat against 185, Reborn contract); Reborn workspace 738 tests (its architecture guard caught a device path in the shared contract crate, moved back into the platform). The owner's hardware round on 184/185 (overnight sleep, low-battery shutdown, SD repair/format, reset) was not done before publishing; the report's Known issues say so.

## RADIO-V2 (one radio daemon for Bluetooth and the shared core): entry audit — 2026-11-03

Boundary: architecture change of a hardware subsystem (Bluetooth control moves from five owners to one daemon, `y2-radiod`; the sleep helper's radio steps and Wi-Fi power go through it). Owner request 2026-11-03: "a complete new reimplementation built on reliability … without losing the codecs and bitrates", then "do the full implementation in one step, build and install on my Y2". Plan: [BLUETOOTH-REIMPLEMENTATION-PLAN.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2FBLUETOOTH-REIMPLEMENTATION-PLAN.md).

Evidence (date, revision, origin, limits): Y2Linux b8e78d3f / Y2Reborn 6fd259c (Beta 9.2.16, baseline-207); field reports 0400eb78 (583b7c23 58e1456e a74ed186), 5692dd73 (962aac6c 46fcbe24) and 11-01..03 others; ledger F64 (library emptied by a Bluetooth rollback, proven in code), F65 (wake reconnect race), F63 corrected (encoder ABR shows the air-time shortfall). No hardware measurement was taken for this audit (the player was not reachable); the plan's P0 measurements (air-time matrix, timing table, keep-alive, stock coex REA) are not done and the first build uses the existing measured constants (page timeout 5.12 s, power-on ≈1.6 s warm, Start up to 6 s).

Coverage: kernel connectivity driver, firmware, BlueZ 5.87, BlueALSA 5.0.0 and its patches: kept (no field failure starts there). Replaced: `y2-bt-reconnect`, `bluetooth-power`, the intent file and the operation/PCM locks, the codec-uncertain marker, Reborn's D-Bus worker. Wi-Fi association (wpa_supplicant, Reborn's join/scan, the F52/F53 heals) is not rewritten in this step (plan §7, P7); its power, the F60 restart and the wake order go through the daemon.

Readiness: implementation ready; owner authorised build and install on the owner's player. Risks accepted by the owner: no P0 measurements first, no v1/v2 switch on the device (rollback = the installer's kept previous package). Hardware authorization covers the owner's player only; publishing is a separate decision.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
