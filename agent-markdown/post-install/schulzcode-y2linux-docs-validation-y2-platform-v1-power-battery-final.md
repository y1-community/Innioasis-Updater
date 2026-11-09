---
title: "Y2 Platform 1.0 power / battery investigation - Innioasis Updater"
description: "Y2 Platform 1.0 power / battery investigation 2026-10-05. IN PROGRESS; MORE WORK REQUIRED. The corrected POWER01 pair is now owner-installed and its exact identity is ver"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-battery-final.html"
---

# Y2 Platform 1.0 power / battery investigation - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 Platform 1.0 power / battery investigation

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 Platform 1.0 power / battery investigation

2026-10-05. IN_PROGRESS; MORE_WORK_REQUIRED. The corrected POWER01 pair is now owner-installed and its exact identity is verified. The screen and controls work. All five staged PM tests passed, but one real RTC suspend failed in CS43131 cache replay and recovered by reboot. Full sleep is still gated; the software and endurance investigation is incomplete. See the Claude continuation handoff under `out/platform-v1-power-final/CLAUDE-HANDOFF.md` in the main workspace. The [machine report](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/data/y2-platform-v1-power-final.json) holds sanitized windows. Private raw incident, network and media evidence stays ignored and is not exported.

## 1. INSTALLED FIRMWARE IDENTITY

Current installed image after owner flash: POWER-FINAL-01, release `1.0.0-platform-v1-power-final-candidate.1`, kernel `6.18.0-y2linux-platform-v1-power-final-01`, root v1.27 / Buildroot 2025.02.18, Linux `fedc005ba68b3f5020a45258e38d641aa191b12a`, Reborn `ccf450ac1388228dbd859318a05e13adf667c9aa`, boot `69d8df3a-1b2d-4c1b-b26b-d744a7859f7a`, taint zero, sole loaded module mediatek_drm. Both SSH metadata and running kernel agree with the sealed candidate. These are metadata/source identities; no direct installed partition hash is claimed. The owner confirms normal redraw and controls. The captured boot has no display WARN/flip/commit timeout. Slots 5/6/7 now read `0x21e:0x48`, preparation flag one and error zero. C3 production policy is Enabled / budget -1; active PC charging correctly vetoes C3. SDP selects the unchanged 450 mA ceiling with fault zero; ECM/MTP is Ready. Radios are temporarily runtime-off for controlled windows; saved Wi-Fi on / Bluetooth off settings are preserved. Two initial PC windows crossed screen-on to screen-off and are kept as transitions, not matched steady idle evidence. Battery-only 60-second/five-minute collection completed on that boot. The failed real RTC test then recovered to boot `c884ae1c-a3b3-4291-8577-f89166a4a8a1`, also taint zero, with owner-confirmed working display and controls. That reboot is not same-boot suspend success.

The following table identifies the incident/before firmware, retained for forensic comparison:````````````````

| Item | Independently observed identity |
| --- | --- |
| Release | 1.0.0-platform-v1-usb-final-candidate.2 |
| Build | Y2LINUX-PLATFORM-V1-USB-FINAL-02 |
| Kernel | 6.18.0-y2linux-platform-v1-usb-final-02 |
| Linux source | 0cb779267ca90740853dc02695166d75f36faa29 |
| Reborn source | 2444e0f65811e688250a8cd069a57dd780b2d6d3 |
| Root / Buildroot | 2025.02.18-platform-v1.26 / 2025.02.18 |
| API / feature contract / DATA / layout | 1 / 2 / 1 / 1 |
| Battery profile / low-battery policy | 1 / 2 |
| Loaded modules | mediatek_drm; power, audio and radios are built in |

SSH identity, persisted boots and the USB worktree's `usb-validation-02` manifest agree. Fresh image hashes are BOOTIMG `4fea3d1e0fac307d7cb444d38d560e0cbc4f29d5c4e6be574247dc6833047382` and Y2ROOT `ab5a93da8a8642b587fd7eef50dbb76c2026825a90114145110e28b70c0587ce`. Main and older baseline labels do not identify this installed image. Both dedicated `codex/platform-v1-power-final` worktrees start at this exact pair. Yesterday's USB transport, lifecycle, FIFO, DMA and responder queue changes remain inherited. Manifest comparison and `git merge-base --is-ancestor` confirm both source ancestors. The USB worktree remains at `0cb7792`; its uncommitted host benchmark, lab and documentation work remains with the owner and changes no installed firmware source.

The 12-session campaign integrated CPU idle, suspend instrumentation/rollback, USB/MTP, charging, radio workers, storage, GPU/input, Reborn performance, precision observability, codecs and platform contracts. The installed USB02 descends from that integration and subsequent baseline. Historical qualified UART01 C3 is kept separate from current-image policy and endurance. Full resume was never promoted by staged PM or source availability. Requested release documents, the 233-feature matrix and newest subsystem reports were reconstructed before power modifications; missing parallel-session/changelog/baseline-integration filenames map to the actual final-session and baseline changelog records, not invented documents.

## 2. OVERNIGHT INCIDENT FORENSICS

The owner unplugged around 01:00, found the device dead around 09:00, and needed wall charging to power it on. The preceding UI value was 88%, not a measured full charge. Incident boot `6f2838c9-3b59-4320-b02f-1d02119a2359` records a declining battery voltage and an orderly `shutdown_complete`, with no unclean boot. The last retained low-voltage sample is 3.400268 V, monotonic 22449.233 seconds. This establishes a real voltage-floor shutdown, beyond a displayed 0%. It does not establish battery-protection cutoff or a genuinely full starting pack.

The retained maximum is 3.920141 V, `full=0`; no retained termination or sample above 4.1 V establishes full charge. Voltage declines from approximately 3.8 to 3.4 V over six hours. Wi-Fi was enabled and associated, playback was paused, and screen blanking was recorded. No full-system suspend occurred overnight. Exact nighttime clocks, process activity, radio retries and C3 residency were not journaled. Wall-clock/NTP jumps prevent assigning precise owner-local timestamps to all rows; use monotonic differences. The retained SDP / 2000 uA USB allocation is a source state, not pack current or proof contradicting physical cable removal.

The supported explanation is an incompletely evidenced starting charge followed by hours of awake runtime idle with Wi-Fi and known recurring userspace/input work. A concrete C3/PMIC slot defect also makes precharge reliability suspect, but the last night lacks a matching register trace. Its exact energy contribution cannot be retroactively measured. Battery degradation is not established.

A new bounded journal captures five-minute snapshots, coalesced state events, immediate shutdown/suspend transitions, voltage, charging, radio/USB/backlight, actual C1/C2/C3 counters, OPP counters, scheduler totals and runtime PM. It uses existing safety samples, adds no timer, rotates two 256 KiB files, and never lets write or lock failure disable battery protection.

## 3. BATTERY MEASUREMENT ARCHITECTURE

BAT0 voltage is a real MT6323 AUXADC measurement; absolute calibration has not been checked externally. SOC is an estimate from filtered voltage. No validated pack current, coulomb count or pack NTC temperature is exposed. BATSNS and ISENSE ADC channels exist, but this board's shunt topology, value and offset are unproven. Raw differential counts cannot be converted honestly to battery mA. PMIC die and CPU die temperatures are distinct from battery temperature. Nominal capacity is unknown; no repository label or verified stock capacity supplies a safe value.

## 4. CHARGER / MT6323 ARCHITECTURE

The built-in charger owns source classification, current-ceiling selection, checked regulation/protection fields, ADC checks, engine sequencing, watchdog, fault latching and voltage-limited hold/recharge. Its safety worker remains 1 Hz; the hardware watchdog is four seconds, with a 2500 ms late-service fault. USB provides an allocation, not measured current. Active charging holds a wake source. Autonomous DORMANT PCM requests bypass normal regmap write validation, so their PMIC-wrapper slots must point at VPROC before runtime C3 is admitted.

Primary field/sequence evidence is the pinned [MT6582 vendor source](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/), plus exact stock Y2 disassembly retained in [the charging contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-charging.md) and [sensor acquisition](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-battery-acquisition.md). The vendor net-current/coulomb methods are stubs; a charger differential estimate assumes a 68 milliohm shunt that has not been established on this Y2. Stock's constant 25 C public temperature is not a measured NTC. Protections were never experimentally bypassed or fault registers cleared to force charging.

## 5. SOC ALGORITHM

| Voltage, uV | Provisional percent |
| --- | --- |
| 3400000 | 0 |
| 3500000 | 5 |
| 3600000 | 10 |
| 3700000 | 25 |
| 3800000 | 45 |
| 3900000 | 65 |
| 4000000 | 80 |
| 4100000 | 95 |
| 4175000 | 100 |

The implementation filters over 30 seconds, requires 120 seconds of rest, uses a 15 mV deadband and 75 mV charging correction, and bounds movement to one percentage point per minute. Charger Full with at least 4.160 V permits 100%. There is no hard 88% cap in source; POWER01 subsequently displayed estimated 90%. Voltage sag, relaxation, temperature, aging and unknown capacity limit accuracy. The UI observation does not prove termination. SOC math is preserved pending calibrated evidence; changing percentages cannot fix drain. Reborn now reuses fresh same-boot protection-owner voltage, falling back to AUXADC when the record is stale, absent or invalid.

## 6. SAFE CHARGING LIMITS

| Source / condition | Existing validated configured maximum |
| --- | --- |
| SDP allocation at least 500 mA | 450 mA |
| SDP allocation 100–499 mA | 70 mA |
| SDP allocation below 100 mA | Inhibited |
| Detected DCP / CDP / eligible Apple source | 650 mA |
| Unknown eligible source | 70 mA |
| DCP deep-discharge / precharge | 450 mA |

CV stays 4.175 V, independent upper guard 4.2 V. Current, voltage, temperature and low-voltage limits were not raised or disabled. A programmed maximum is not measured actual charging or net battery current.

## 7. PC USB CHARGING

POWER01 superseding observation: SDP / 500 mA allocation / 450 mA ceiling, fault zero. Near the 4.175 V target, it stops into HOLD with `full=0`, relaxes to about 4.086–4.093 V, then restarts below the existing 4.110 V recharge threshold. Repeated cycles are observed, but actual current/taper and true termination are not established. Die temperature around 39–43 C is not pack temperature. Requalify near-full behavior after the idle DAC correction. The long numerical window below belongs to the earlier USB02 firmware.

Current boot reports SDP, 500 mA USB allocation, 450 mA selected, Charging and fault 0, with positive voltage trend and ECM/MTP available. This is a bounded charging pass, not proof of actual mA or near-full termination. The first wall fault stayed latched on PC reattachment until the one graceful diagnostic-module removal/recovery reboot. The 1800.312-second PC window gained 3.881469 → 3.937500 V, provisional SOC 47 → 58%, at the unchanged 450 mA ceiling with fault zero. CPU0 was online throughout; C1 52492 entries / 6.2767%, C2 205957 / 85.7193%, C3 zero. Recorded OPP residency was 90.605% at 598 MHz. IRQ rate was 164.046/s and context switches 368.132/s. The original components were restored. Two brief SSH read probes occurred; the frozen-display/C3-quarantined state prevents treating this as optimized battery-only endurance or a matched after-fix result.

## 8. WALL CHARGING

| Bounded wall window | First | Second |
| --- | --- | --- |
| Duration | 300.620 s | 300.299 s |
| Source / selected maximum | DCP / 650 mA | DCP / 650 mA |
| C3 policy | Active | Automatically quarantined after DRM WARN |
| Voltage | Fell after fault | 3.701513 → 3.740185 V |
| SOC | Not a full-charge proof | 8 → 13% |
| Outcome | Protection fault 0x80 | Charging throughout, fault 0 |

In the first window, `CHR_CON0=0x62` at monotonic 1610.374 s loses HV-enable, followed by verified charging inhibition. A matching read-only diagnostic module found wider regulation-field losses. Fault protection worked; it was never bypassed. The second test is a different boot and is an isolation observation, not matched post-fix proof. Detached wall operation showed no enumeration dependency or MUSB interrupt activity. Source current remains a configured ceiling.

## 9. CPU FREQUENCY

POWER01 battery-only B300: 94.6822% at 598 MHz, 0.7226% at 747.5 MHz, 1.2620% at 1040 MHz, 0.2797% at 1196 MHz and 3.0535% at 1300 MHz.

Governor `schedutil`; minimum 598000, maximum 1300000 kHz. Stats cover all five OPPs: 598000, 747500, 1040000, 1196000, 1300000. Quiet PC windows predominantly use 598 MHz. There is no evidence of a permanent overnight high-frequency/QoS lock. Window frequency deltas are in JSON. OPPs and the existing voltage floor are unchanged.

## 10. CORE PARKING

POWER01 B300 begins with cores 0–3 following heavy endpoint observation and ends with CPU0 only. B60 mostly remains WFI during that adaptive settling hold. This is not a fresh-boot policy disabling C3.

Natural hotplug parks secondaries after the existing adaptive post-burst hold. Observer work can restore demand and prolong this hold. The second wall window parked cores around 257/262/267 seconds. Endpoint online states and per-core wall denominators are retained; no arbitrary forced offline or IRQ-affinity policy was used.

## 11. C1

POWER01 B300 CPU0: 3657 entries, 83,248,116 us, 27.7221% wall time.

Real WFI entries occur in recorded windows. CPU0 in first wall window: 14426 entries, 83.5625% wall residency. Second: 7471 entries, 28.9026%. Per-core values and exact denominators are in JSON.

## 12. C2

POWER01 B300 CPU0: 3132 entries, 14,744,874 us, 4.9101% wall time.

SLIDLE works. First wall CPU0: 1246 entries, 1.5491%; second: 18690 entries, 64.4756%. Existing restore guards remain. C1/C2 remain usable while charging excludes C3; the charge watchdog does not require disabling C2.

## 13. C3

POWER01 supersedes the defect/readiness observations below: clean boot B300 records CPU0 9765 C3 entries and matching resumes, 188,118,874 us / 62.6446% wall residency. UART ACK succeeds for all 9765; restore failures and timeouts zero. The boot ID is unchanged and taint zero. Correct slots 5/6/7 are read back. This is runtime C3, not full-system suspend or endurance.

The first USB02 wall window physically records CPU0 2554 DORMANT entries and 11.7177% residency. Historical UART01 65.245% is a different image/workload. The former USB02 WARN boot records zero and remains quarantined.

The retained 480-word runtime PCM requests wrapper slots 5/6. USB02 normal CPU preparation initializes only slots 0–2; live slots 5–7 read **address 0, value 0**. Full-suspend preparation would populate them, but runtime C3 does not call it. These autonomous requests can address charger register 0 instead of VPROC. The candidate initializes and reads back slots 5–7 to the active VPROC bank with selector 72, retaining the verified 1.15 V floor. Failed preparation or voltage-owner checks close C3 admission. Source plus live readback proves the slot defect; no PMIC bus trace proves every observed register loss resulted from it. POWER01 proves slot initialization and bounded runtime C3 integrity; full charging, full suspend and endurance acceptance remain open.

## 14. C3 PRODUCTION POLICY

Post-owner POWER01: Enabled / budget -1 / state2 disable 0, taint zero, correct checked PMIC slots and readiness flag. Active PC charging correctly vetoes admission. B300 records 9765 matching unplugged entries/resumes and 62.6446% CPU0 residency. This is bounded runtime qualification, not endurance.

Installed USB02 fresh healthy boot: Enabled, budget -1, state2 disable 0. It is not the historical fresh-boot budget-zero configuration. The incident boot also logged startup Enabled. The later necessary reboot produced DRM WARN, taint 512, and Skipped / kernel_tainted_or_unknown / budget 0 / disable 1. That guard was respected. Candidate admission adds PMIC-slot readiness and active-charger/watchdog exclusion; all UART, timer, topology, CONSYS, USB, display, workload, deadline, context and CIRQ guards remain. Actual overnight residency is unknown because the prior journal lacked those counters.

## 15. CPUIDLE BLOCKERS

| Blocker | Owner | Actual idle behavior | Fix / expected behavior |
| --- | --- | --- | --- |
| USB clocks | MUSB, ECM, configfs | Required when PC configured; detached off / no IRQ | Preserve current lifecycle and USB data |
| CONN / APDMA / BTIF | Shared CONSYS | Wi-Fi enabled owns clocks; radio off releases them | No invented clock gate; measure radio matrix |
| Core topology | Hotplug coordinator | Adaptive post-burst hold | Preserve demand restoration |
| Display warning | First DRM takeover | POWER01 display/controls work; no captured warning, taint zero | Checked first-only inherited OVL stop; repeated resume remains open |
| Idle PMIC slots | PWRAP / SPM | POWER01 slots 5–7 initialized/read back, C3 returns | Retain verified active VPROC bank / 1.15 V |
| Active charge watchdog | Charger | Requires safe 1 Hz service | Explicit C3 exclusion; preserve C1/C2 |
| AFE / CS43131 | ALSA / codec | POWER01 PCM closed, AFE gated, codec active/Standby with five rail references | Y2-local idle-bias-off implemented but not installed/physically proved |
| eMMC / SD | MSDC / source observer | POWER01 clocks release; SD IRQ about 0.962/s; DT broken-cd polls | UUID cache installed; separate MMC poll ownership from source observer |
| UART | UART PIO / SPM | Existing request / ACK ownership | Preserve bounded qualified handoff |
| Input | APT32F, keypad, GPIO keys | Wheel/keypad IRQ quiet; navigation polls at 50 Hz | Do not guess unsupported EINT routing |

Unknown owner states remain unknown; source availability is not hardware proof.

## 16. WAKEUP SOURCES

A unique whole-CPU wakeups/s counter is unavailable. `wakeup_sources` covers system-suspend wake blockers, not every runtime idle exit. JSON separately keeps IRQ rates, context switches, per-thread CPU, cpuidle entry/residency deltas and available wakeup-source deltas. They are proxies, not battery mA or unique wakes.

## 17. IRQ OFFENDERS

Timer/IPI/scheduler activity dominates the retained short windows. Detached MUSB interrupts were zero; untouched wheel/I2C0/keypad and inactive AFE show no storm. JSON ranks per-window IRQ deltas. Hotplug can decrease per-core counters; these discontinuities become unknown rates, never negative/overflow event counts. POWER01 B300: 83.2847 IRQ/s and 149.7692 context switches/s; GPT 42.4182/s, SD 0.9624/s, eMMC 0.4529/s. Detached USB, AFE and untouched input hardware IRQs are zero. Architectural timer counter discontinuity during hotplug is reported unknown; the IRQ proxy must not be called unique CPU wakeups.

## 18. USERSPACE POLLING

POWER01 new offender: B300 global task births 0.9291/s. Bounded ptrace identifies the connectivity shell spawning `sleep 2` and periodic `cat`/ `readlink` health children. A production Python supervisor using netlink, pidfds and interruptible waits is implemented and targeted-tested; it is not installed. The bounded live monitor trial completed with original helpers/PIDs/hash restored, same boot, taint zero. Monitor context switches: 1.4588 → 0.03316/s; global task births: 1.7903 → 0.01658/s. IRQ 277.75 → 126.07/s and context 246.19 → 186.24/s are recorded observations, not isolated energy improvement: the trial parent used a timeout wait causing ~19.9 wakes/s in both windows, and SSH probes contaminated the before window. Repeat with a blocking parent and no probes. Production source remains unbuilt; no steady runtime replacement remains.

Matched component trials used PC-connected, radios-off, paused/dark 60-second windows on the same WARN boot. The table measures thread context switches, not uniquely attributable CPU wakeups or battery current.

| Offender | Before switches/s | Isolated after switches/s |
| --- | --- | --- |
| MTP receive thread | 49.7586 | 0 |
| Bluetooth reconnect main | 15.1216 | 0.1989 |
| Bluetooth reconnect GLib thread | 15.6356 | 0 |
| Reborn main | 20.1124 | Physical after measurement pending |

MTP now blocks on a signaled condition instead of 20 ms timeout polling, with all cancel/stop writers signaling under the same mutex. Bluetooth watches a private intent directory instead of unrelated `/run/y2/power.json` writes. The sole reconnect owner is preserved. SSH uses passive rtnetlink and signal wake descriptors, retaining its five-second readiness heartbeat and a 60-second stable-address backstop instead of one-second `ip` subprocesses. Address changes, child exit and shutdown still wake it immediately. No polling lab module ships.

## 19. REBORN IDLE

Before: main approximately 0.85% of one core / 20.11 switches/s; watchdog about 1.24%, with recurring source/voltage probes. The candidate waits up to one second when paused/dark, 250 ms for lit static UI, 50 ms while playing, and 34 ms while lit/dirty. Evdev, control and AVRCP descriptors wake it immediately; held keys retain 15 ms pacing. AVRCP blocks on bus/state/shutdown descriptors instead of 200 ms polling. UUID caching is bounded to four fresh mount/device/diskseq keys; card/CID/mount admission is still revalidated and failures are never cached. Same-boot protection samples younger than five seconds avoid duplicate AUXADC.

POWER01 superseding measurement: B300 main 0.9024% of one core / 2.3211 context switches/s; watchdog 0.3596% / 2.0180 switches/s. No continuous rendering is present with display/GPU suspended. Residual playback/audio, scanner and database timeout wakes still merit tracing. Current UUID caching includes the whole-disk diskseq when mounted device is a partition; a missing-partition- diskseq cache bug was investigated and ruled out, not patched.

The earlier temporary ARM Reborn trial hit the pre-existing stalled DRM commit and its RPC could not answer. There is no valid physical after window. The original binary was restored and hash verified. ARM and workspace tests do not qualify actual rendering, idle power or remote-command responsiveness on the device.

## 20. DISPLAY / GPU

Superseding post-owner POWER01 evidence: the owner confirms normal redraw and responsive controls after brief Power. Captured fresh boot has no display WARN/flip/commit timeout and taint zero. Bounded awake-to-dark windows show OVL, RDMA and GPU suspension after the normal timeout. Repeated wake and full-system resume remain separate tests. The following failure belongs to USB02.

The first healthy boot's dark state released scanout, Lima/MFG and backlight. The recovery boot warned in vblank, then timed out in flip/commit/mutex paths; the owner confirms black/frozen display even after brief Power. Taint 512 correctly quarantines C3. DSI probe parks the loader stream and the mutex owner clears membership, but installed OVL clock enable can leave loader EN=1, causing first configuration to skip its required reset. The candidate stops and verifies OVL and source layers only on first owned clock enable, then uses normal config/start. No subsequent live-plane reset, timing/PLL/rail change or warning suppression. Native clock/drop-write/non-Y2/subsequent-live-path tests pass; cold/warm physical boot repair has passed current owner visual/controls checks. Repeated blank/wake and full-system resume are distinct remaining qualification.

## 21. AUDIO / CS43131

POWER01 supersedes earlier suspended-codec snapshots: PCM is closed and AFE/I2S clocks are gated, but codec `1-0030` is runtime-active, DAPM Standby, with five codec rail references retained and GPIO15/18/20 asserted. Upstream CS43130/43131 components set `idle_bias_on=1`; exact pinned DAPM code traces Standby to held runtime PM. The unbuilt Y2 card fix sets the supported `snd_soc_dapm_set_idle_bias(..., false)` before initial sync. It preserves driver reset/cache/rail sequencing, stream references and disabled Headphone pin. Actual stop/start, rails, playback and resume after this fix remain untested. A skipped resume callback alone cannot prove the cache-replay stall repaired. No temporary audio lab module is installed; no direct rail forcing is used.

## 22. WI-FI

Incident Wi-Fi was enabled/associated and validly owned CONSYS. Nighttime scan, retry and IRQ counts were not retained. Runtime off releases these blockers. Campaign freshness, 30-second RSSI, inventory and DNS reuse are inherited. A historical FAST_PSP trial was reverted to CAM and cannot count as proven savings. Current default automatic policy has `automatic_standard=False`, so connected idle still requests CAM / power-save off. No setting was changed; compare bounded FAST_PSP and connectivity before changing a default. `iw` readback is host state, not proof of firmware sleep or measured energy. Enabled/disconnected/connected battery-only comparisons remain open; no guessed fullmac power mode, reconnect or keepalive changes were made.

Bounded ABA trial on POWER01 (CAM, FAST_PSP, CAM; 180 s each, screen off, paused, PC USB attached, same boot): 143.9 / 79.2 / 139.9 IRQ/s and 181.4 / 160.7 / 179.5 context switches/s. The charger phase differed in the middle window (4.168, 4.10, 4.165 V: charging versus HOLD relaxation) so that IRQ drop is not attributed to Wi-Fi power save; `y2-wifi` interrupts stayed 1.3 / 2.5 / 2.6 per second. FAST_PSP kept association with 0% gateway loss but raised ping to 15.5 ms mean, 100.8 ms maximum (CAM 2.1 ms mean). CPU0 stayed WFI-only because charger-active C3 is guarded. Policy file removed and CAM restored; no persistent change. Default stays CAM until an unplugged matched comparison exists.

## 23. BLUETOOTH

Off during isolated recorded windows, reconnect attempts/completions zero. The measured wake load was unrelated directory notifications, not a peer retry storm. The private intent directory reduces main to 0.199 switches/s and GLib to zero; the actual native fixture preserves intent response. On/disconnected/connected peer qualification remains open; an available headset is not assumed.

## 24. USB

Detached MUSB bus clock was off and its IRQ delta zero; the responder exits when unplugged. Its PC-only 50 Hz receive polling therefore cannot alone explain last night's disconnected drain. USB02 lifecycle, DMA/PIO, FIFO, ECM/MTP and 32 × 64 KiB queue are inherited. The isolated wait fix passed a real KDE desktop **16 MiB upload and download**, with device and returned SHA256 `84ebb5bc9e1e188628f3c87ff3c06906d45b775f2692555efc2be7deb7795696`. Only the owned test file was removed. ECM/SSH returned in the same boot with 450 mA selected and fault zero. Original responder was restored and hash verified. No competing desktop USB process was killed to force a libusb session.

POWER01 ECM/SSH and Ready/configured MTP state persist through the recovery reboot; restarts zero. A fresh host MTP attempt in the restricted execution session failed at `libusb_init` with `LIBUSB_ERROR_OTHER` before device access. The original host benchmark ignored that return and segfaulted; a temporary init-checked host copy localized the failure. This is not a measured firmware USB regression and not a passing new-image file round trip.

## 25. STORAGE

POWER01 B300 SD IRQ ~0.9624/s remains after UUID caching. The DT marks SD `broken-cd`; kernel MMC card polling is a separate leading owner to trace. Do not remove hot-insert support without established card-detect wiring.

Recurring UUID superblock probes every two seconds came from watchdog source observations. The candidate caches only the UUID using freshly read mount/device/ diskseq identity; it preserves CID, mount and no-follow checks. Failed probes are not cached. MSDC clocking, filesystem policy, database integrity and runtime PM are unchanged. The persistent power journal writes at five-minute cadence in steady state; no media rescan, forced cache drop or write suppression was added.

## 26. INPUT

APT32F is interrupt-driven, with an I2C read per valid data-ready IRQ. Untouched wheel interrupts are quiet. Keypad and PMIC Power are IRQ-driven. Five GPIO navigation buttons still use upstream `gpio-keys-polled` at 20 ms: a real **50 Hz runtime-idle limitation**. Current pinctrl supports only established EINT lines; exact navigation GPIO-to-EINT routing is not proven, and the pinned vendor GPIO map is empty. No guessed remux or slower/lost controls. Qualified full suspend would stop that runtime polling; held-key UI pacing remains responsive.

## 27. TIMERS / RTC

NO_HZ_IDLE and CPU_FREQ_STAT are enabled. GPT/local architectural timer/DORMANT handoff remain. Required charge safety remains 1 Hz. Optional 20 ms MTP receive, 50 ms dark UI, 200 ms AVRCP and Bluetooth shared-directory work are addressed in source. GPIO navigation at 50 Hz remains. The bounded audit collects endpoint IRQ/softirq/context/OPP/idle/process counters without tracing during its interval. Awake RTC alarm and full-suspend RTC wake are distinct acceptance gates.

## 28. FULL SYSTEM SUSPEND

POWER01 completes freezer/devices/platform/processors/core in the same boot with taint zero, clean filesystems, helper success and no deep-entry deltas. Exactly one real RTC12/backstop30 trial then FAILS: retained DEVICES_RESUMING, EINT wake0x20, PCM596, reset return0x59325253. Codec rails finish successfully after 2835 ms, access/reset and 2 ms delay finish, and trace stops at `cs_cache_begin` with no `cs_cache_done`. Recovery boot is c884ae1c, different from 69d8df3a. RTC versus Power child attribution is not recoverable from the shared EINT bit alone. No real Power test or automatic retry followed. Owner confirms usable display/controls after recovery. This is not successful same-boot resume and ordinary product sleep remains refused.

Unbuilt sleep-only retained breadcrumbs now bracket regcache map locking/sync and I2C clock, DMA, transfer and completion boundaries. Target is exact Y2 CS43131/controller; no new timeout, MMIO write, wake mask or polling. Root cause inside cache replay is still unknown. Next kernel must prove rails, playback restart, complete EXIT/restoration, actual residency and same-boot RTC/Power separately. Automatic sleep remains gated until those product checks pass.

Review finding after the failure: the codec supply enable took 2835 ms although the board defines three 50 ms startup delays (about 150 ms nominal), roughly 19 times longer. The PM journal also extends its backstop on every progress note, so the stall lasted at least the full 30 s with no further progress and no bounded I2C timeout fired. That points at timer or interrupt delivery after deep resume as well as the cache replay; it is unproven. Two sleep-only notes (`cs_jiffies_begin`, `cs_jiffies_done`) now record `jiffies` around the rail enable so the next retained ring distinguishes a stalled tick from slow regulators. They add no timer, MMIO access or runtime logging (patch 0030 regenerated; zero-fuzz result hash verified).

## 29. POWER-BUTTON POLICY

Owner reports paused Power says "not available" on recovery boot. The UI source requests guarded full sleep when paused; screen blank fallback on refusal has not been implemented or qualified. This user-visible behavior remains open. Paused short Power requests guarded full sleep; playing Power blanks, dark short Power wakes, long Power opens the shutdown confirmation. Screen-off currently cannot promise deep sleep. No unqualified five-/30-minute automatic suspend is activated. After repeated same-boot Power/ RTC success, add configurable paused-inactive sleep with playback, transfer, update, scanner and unsafe charging exclusions. This investigation continues through that gate after owner installation.

Source fallback (host-tested, not on hardware): when full sleep is refused only because it is not yet qualified, Reborn now turns the screen off after the refusal and the page says Power turned off the screen instead; charger, busy and other refusals are unchanged and nothing claims deep sleep.

## 30. LOW-BATTERY POLICY

Independent floor 3400000 uV; warning 3500000, recovery 3600000; five consecutive one-second samples and ten-second grace. SOC alone cannot force shutdown. The incident reached this actual voltage boundary and completed orderly shutdown. The new journal retains reason and voltage. No lowered floor or intentional protection cutoff/deep discharge was used.

## 31. BATTERY HEALTH EVIDENCE

Nominal/effective capacity is unknown and no pack-current integrator exists. A verified full charge followed by controlled safe load characterization has not been completed. There is no justified degradation diagnosis. Missing deep sleep and software defects are real, but the exact fraction of overnight energy explained is unknown. After software qualification, characterize normal idle/ playback with voltage, time, sag/relaxation and states, stopping before the existing safety floor. Do not deliberately exhaust the pack.

## 32. BEFORE / AFTER POWER MATRIX

The machine report retains thirteen sanitized windows, including POWER01 B60/B300, two screen transitions and the qualified-with-limitations supervisor trial pair, with raw hashes. The long PC charge window is reported separately from the 60-second component comparisons; its longer settling cannot be attributed to the candidate fixes.

| Same-boot PC comparison | Context switches/s | IRQ/s |
| --- | --- | --- |
| Original components | 383.11 | 259.87 |
| Only MTP wait fix | 289.54 | 211.70 |
| Only BT private intent fix; original MTP restored | 342.73 | 250.78 |

These are old-image matched component comparisons, not a combined candidate or measured battery current. POWER01 B300 is the new clean battery-only result: C1 27.7221%, C2 4.9101%, C3 62.6446%, IRQ 83.2847/s, context 149.7692/s, CPU0 at the final endpoint, 4.043627 → 4.036816 V, estimated SOC 83 → 83%. Observer/hotplug constraints remain explicit. The complete A–J matrix, playback, radio peer, corrected wall charging and longer battery-only endurance remain pending. B/E/G have bounded clean POWER01 battery-only evidence; full sleep J has staged passes and a failed real RTC test. Different-boot wall tests establish association, not an after-fix comparison.

## 33. LONG-IDLE RESULTS

Two five-minute wall windows completed: first faulted and voltage fell, second charged with C3 gated. POWER01 battery-only B300 completed, with −6811 uV direct ADC delta and unchanged estimated 83%; post-charge relaxation/noise and uncorrected idle DAC prevent calling this optimized endurance. Thirty-minute, two-hour and overnight battery-only tests remain NOT_RUN. B300 counter observer cost is about 0.594 CPU seconds / 300 seconds (~0.2% of one core), with roughly 1.85 CPU seconds of heavy descriptions outside the interval. A PC charging window is a separate workload. The audit uses approximately 0.62 CPU seconds of counter endpoint work in a 60-second interval (~1% of one core); approximately 1.8 CPU seconds of heavy state descriptions are outside the counter window. It performs no scheduled sampling during the declared interval. Longer intervals reduce endpoint bias. Five read-only device trials of the journal counter collector averaged 0.08886 CPU seconds per due row (0.0296% of one core at five-minute cadence), maximum encoded counter block 1847 bytes. This does not measure persistent-write latency. No service was replaced for this collector measurement.

## 34. CHANGES MADE

Checked runtime PCM idle slots and readiness; active-charge C3 exclusion; first mismatched protection-register diagnostics and correct callback context; source-change-only USB supply notification; first-only OVL takeover; signaled MTP receive wait; private Bluetooth intent watcher; passive SSH address monitor; bounded persistent power/idle journal; duplicate ADC reduction; Reborn workload-sensitive wait and AVRCP wake descriptor; identity-bound UUID cache; endpoint-only power audit with discontinuity and observer accounting. POWER01 is owner-installed. Further source-only fixes are Y2-local DAC idle bias, blocking connectivity supervisor, sleep-only cache/I2C retained trace and idle counter discontinuity handling. They are not yet built or installed. Reborn has no new source edits after ccf450. Main and yesterday's USB owner worktree remain untouched; the sealed POWER01 package is unchanged.

## 35. CHANGES REJECTED

No higher charging limits, lower voltage floor, forced protection-fault reset, fabricated current/coulomb/capacity, unsafe 1.05 V idle selector, guessed pinmux, forced core parking, taint bypass, unqualified autosuspend, wake-by-reboot success, high-frequency journal or battery blame. Stock live comparison may later use existing ADB; no original-firmware flash or SSH patch is required for this pass.

## 36. TESTS

Post-flash pending-source targeted suite: 40 pass, using `PYTHONPATH=tests python3 -m unittest tests.test_dev_i2c tests.test_pm_replay_trace tests.test_audio_idle tests.test_suspend_audio tests.test_power_audit tests.test_connectivity_supervisor tests.test_sleep_product tests.test_suspend_policy -v`. Actual pinned DAPM transition references, codec rollback, extracted I2C transfer, fd shutdown, helper crash/restart bounds and counter-reset handling are exercised. These are source tests, not a built or physically qualified second candidate. The broad build/validation results below apply to the sealed POWER01 only.

Affected CPU/charger suite: 72 pass. Extended targeted suite: 146 cases, 145 pass / one emitted-kernel opt-in skip. Real charger callback/worker: four pass after a review-caught context correction, with actual regmap identity checked. Journal: six pass, including cumulative counters only when a row is due; audit: two; display ownership: one; SSH/transfer: seven. MTP actual receive, cancel, filesystem/protocol and native Bluetooth event fixtures pass. Reborn `cargo fmt --all -- --check`, strict all-target workspace Clippy and 326 workspace tests pass. Prior failed receipts are retained and not called passes. The final fresh source-bound kernel/modules/config/DT/ABI and ARM build pass. The production profile has **498 cases: 487 pass, eleven locked-host dependency skips, all eleven covered by 59 passing native host cases**. Installed ARM/QEMU imports cover 34 platform modules; SQLite, OpenSSL, null ALSA constraints, Reborn defaults/library benchmark and codec contracts pass. ELF closure covers 384 files and 1411 dependency edges. Package/privacy, inventory, legal-info collector and source seal pass. The seal contains 451 source/license records and all successful validation exit receipts. Legal-info warnings remain explicit; public distribution is not asserted. Earlier cache-path/missing-input attempts are retained separately and are not final passing receipts. The exact pinned source archives were used; no parallel build output was substituted for the fresh rootfs. Inherited vendor Wi-Fi warnings are retained; this pass does not rewrite that driver.

## 37. COMMITS

Implementation Linux `bff021e7dc5dc57ed4fe0a3d1ac527a252e6c639`, charger-context correction `ffc1787e76c5b049e39ecbb8f4360c96322d60ea` and cumulative journal `447bc9b4aaab12d68b6f8a2e0c52ab71eef15352`; compiled Linux `fedc005ba68b3f5020a45258e38d641aa191b12a`; Reborn `ccf450ac1388228dbd859318a05e13adf667c9aa`. Full compiled source pair is recorded in candidate metadata; later documentation seal HEAD must not replace it. Configured Git identity is preserved; no model attribution or push.

## 38. CANDIDATE / HASHES IF BUILT

Owner installation complete: USB SSH confirms the exact POWER01 source pair and running kernel on boot `69d8df3a-1b2d-4c1b-b26b-d744a7859f7a`. The package remains sealed and unchanged. New physical evidence updates this continuation report outside the package; no flash or push was performed by the agent.

Sealed owner-local candidate. Canonical destination: `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-platform-v1-power-final-candidate/`. Build `Y2LINUX-PLATFORM-V1-POWER-FINAL-01`, kernel `6.18.0-y2linux-platform-v1-power-final-01`, root `2025.02.18-platform-v1.27`. One preserving BOOTIMG/Y2ROOT pair, no Y2DATA payload or reset. BOOTIMG (7239680 bytes): `716c686064764112310e0d1ef621d0308fafd4054650d57eb8b74d35e6fb2109`. Y2ROOT (536870912 bytes): `a23a03b8ee87492edca986b59e95b83ae41227204c7894a90df12245c822627d`. SHA256SUMS, manifest, source archives, validation receipts and OWNER-HANDOFF are included. The fallback is the exact installed USB02 BOOTIMG/Y2ROOT pair. Use SPFT Download Only / preserving scatter, BOOTIMG and ANDROID only; DATA and every other partition remain unselected. The owner flashes; the agent does not. After confirmation, verify installed identity and resume the pending matched matrix without restarting forensics.

Historical pre-POWER01 restoration on USB02 (not the current recovery boot): original Reborn, MTP, Bluetooth helper and Python module match backups; saved Wi-Fi on is restored at runtime; Bluetooth intent remains off; ECM/MTP Ready, charger fault zero, sole loaded module mediatek_drm. DRM taint/C3 quarantine remains, not bypassed. The supplied handoff contains the overnight procedure for use after five-/30- minute and two-hour acceptance, and repeated same-boot RTC/Power success.

Final verdict: MORE_WORK_REQUIRED. The software candidate is owner-installed; its display and source/PMIC-slot readiness are confirmed. Matched idle, charging, full resume and endurance qualification remain incomplete; continuation is recorded in the Claude handoff. No second power candidate has been built. No overnight solution or battery-health conclusion is asserted before those measurements.

Handoff restoration: boot c884ae1c, taint zero; original connectivity script and helper PIDs restored, Wi-Fi saved-on and runtime Online, Bluetooth saved-off and runtime Off, USB ECM/MTP Ready/configured with restarts zero, SDP450mA/fault zero. PM test none, RTC alarm empty, recovery backstop unarmed/not running/error zero. No new source fix is installed and no second power candidate exists.

## 39. POWER-FINAL-02 PHYSICAL QUALIFICATION

Installed and verified on boot `309681c4` (taint zero): release `1.0.0-platform-v1-power-final-candidate.2`, Linux `eb824a6`, Reborn `05af011`. Machine record: `docs/validation/data/y2-power-final-02-physical.json`. Private raw windows stay under `out/platform-v1-power-final/private/post-flash/F02-*`.

DAC idle bias: PASS. Idle and 3 s / 18 s after stopping playback: DAC GPIOs 15/18/20 low, `cs43131-en20/18/15` enable counts 0, DAPM bias Off, PCM closed, audio clocks off, AFE runtime suspended. During playback: GPIOs high, counts 1/2/1, bias On, PCM RUNNING, 517 AFE IRQs. Playback restarts cleanly. POWER01 held five rail references while paused.

Connectivity supervisor: PASS. Single thread, below 0.05 context switches/s over a 120 s window. Associated Wi-Fi idle 1.2-2.6 Wi-Fi IRQ/s. Bluetooth connected idle adds nothing measurable (168.8 ctx/s system, 0 reconnect attempts). Missing AP, measured with a runtime-only dummy network: wpa_supplicant scanned 11 times per minute with 7.2 Wi-Fi IRQ/s, indefinitely. `autoscan exponential:2:120` cut that to 5 scans per 150 s and 1.3 IRQ/s; the supervisor now applies it when the interface attaches (candidate 3). Missing Bluetooth peer was not testable (headphones were in range and connected).

Power button. Root cause of "not available": Reborn executed `/usr/bin/y2-platform`, which no production image installed (`/usr/sbin/y2-platform`), so every platform call failed. Fixed in Reborn source. With a temporary live symlink the fallback blanked the screen when sleep was refused as `physical_qualification_required`; it now also covers `charger_active`. A `restore_failed` receipt from a previous boot persists until the next sleep request.

CPU idle. C3 is enabled by normal policy (qualified CPU0 DORMANT, budget -1). Battery, dark, paused, radios off: 30 min = 74.4% C3 (65 808 entries), 17.5% C1, 3.8% C2, 71.9 IRQ/s, 136 ctx/s. 300 s window: 38.4% C3, 55.2% C1. **With Wi-Fi associated (CAM or FAST_PSP) C3 and C2 are 0%**: connectivity owns APDMA bit 11 and BTIF bit 20 (documented blockers), and 14 499 C3 / 17 796 C2 attempts per 300 s abort. This explains the overnight incident, where Wi-Fi was associated. Candidate 3 powers Wi-Fi down at runtime after five dark idle minutes on battery (saved preference untouched; wake restores). Wake offenders with radios off: polled navigation GPIO kworker 27 ctx/s, rcu_sched 8, mm_percpu_wq 6.6, charger worker 4.8, python daemons 2.2 each. Voltage slopes (1.84, 1.01 and 0.19 mV/min for CAM, FAST_PSP and radios-off) mix post-charge relaxation with load and are not current. FAST_PSP versus CAM cannot be separated electrically while both block C3; CAM stays default.

Full suspend: still FAIL, now precisely localised. Staged pm_test stages all pass. Real RTC12/backstop30 attempts (and a repeat with the SD host unbound) enter deep sleep, wake at the RTC time (SPM wake 0x20, PCM 596, reset-return stamp) and the kernel resumes every device and marks `DEVICES_RESUMED`, `CONSOLE_RESUMED`, `PLATFORM_ENDED`, `TASKS_THAWED` with `failed_stage` NONE and error 0. It never reaches `FILESYSTEMS_THAWED`; the 30 s backstop resets. The earlier codec cache-replay stall is not reproduced because the DAC is already down at suspend. The stall is in `suspend_finish()` after tasks thaw: a blocked `filesystems_thaw()` (storage I/O or `s_umount`) or a crash there. Candidate 3 adds a post-thaw sampler (suspender wchan, uninterruptible tasks, MMC IRQ counts at 3 s and 15 s), oops/panic notes and a ramoops reservation (DRAM retention across the warm reset is unproven). Power wake and repeat cycles wait for a same-boot resume.

Charging. PC USB: SDP, 450 mA programmed ceiling, HOLD near 4.175 V, fault 0, MTP and SSH configured; that is a configured ceiling, not measured current. Wall charging: not run. Verdict stays MORE_WORK_REQUIRED.

Baseline update (2026-10-06).`main` now integrates the parallel branches on top of POWER-FINAL-03 (03 wins on every collision). The flashable base is POWER-FINAL-04, behaviourally identical to 03: Linux `5aeba05`, Reborn `8cd365d`, BOOTIMG SHA256 `be0f4379531be4b8f94fd927adda18106fbad1a567665cb63d5807908095aea4`, Y2ROOT SHA256 `4fc765b931f85e0fee96c0b80c92592eca3a4f3f2a4e379d18abd71bc3978e64`, rollback = the installed POWER-FINAL-02 pair. The verdict is unchanged: MORE_WORK_REQUIRED (full suspend stalls after `TASKS_THAWED`; 04 carries the stall sampler, oops/panic notes and ramoops to locate it).

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
