---
title: "Y2 suspend power optimization (POWER-FINAL-05 campaign) - Innioasis Updater"
description: "Y2 suspend power optimization POWER-FINAL-05 campaign Status: MORE WORK REQUIRED — phase 1 research, no device change. Started 2026-10-08 on branch codex/platform-v1-powe"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-suspend-power-optimization.html"
---

# Y2 suspend power optimization (POWER-FINAL-05 campaign) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 suspend power optimization (POWER-FINAL-05 campaign)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 suspend power optimization (POWER-FINAL-05 campaign)

Status: MORE_WORK_REQUIRED — phase 1 (research, no device change). Started 2026-10-08 on branch `codex/platform-v1-power-final-05` (from `27148be`). Nothing here has been built, flashed or changed on the device. Every statement is tagged [measured], [source] (exact-source backed, not yet observed on the Y2), [estimate] or [unknown]. SOC is voltage-derived and is never used as an energy measurement.

Correction (2026-10-09, POWER-FINAL-06 audit). Earlier text in this report (the §1 "PCM origin" line, §8, and the statements below that follow from them) says Y2Linux runs the 480-word `pcm_dpidle` program for full suspend. That is wrong. The `MT6582_d53dd75c_dpidle (480 words)` string comes from the runtime-idle (dormant C3) SPM sysfs line, not from system suspend. Full suspend already loads the vendor 597-word `pcm_suspend` (v34rc10, non-MT6333 variant, IM length 596, event vectors 26/55/99; `kernel/platform/spm-pcm.h`, `spm-suspend-policy.h`; `/sys/firmware/y2_pm/state` reports `pcm_length=596`). Re-verified on 2026-10-09: the 597 words are identical to the arrays in the pinned vendor `mt_spm_sleep.c` (`d53dd75c…`), SHA-256 `0ee71194bd3330512e1415c22080cea29942ec7124b77311cfd1bc2215c6ab94`, and the stock `spm_go_to_sleep` disassembly matches the vendor source. The actual difference from the vendor's default full suspend (`slp_cpu_pdn=1`, `slp_infra_pdn=1`, `slp_ck26m_on=0`; stock `.data` defaults 01 01 01 at `0xc09b1084` read from the retained FM kernel) is only `infra_pdn=false`: Y2Linux sets `CC_DISABLE_INFRA_PWR` (mode `SPM_CPU_SHUTDOWN_INFRA_RETAINED`) and does not port the stock post-wake `mtk_uart_restore` or any other INFRA-domain restore. The PCM program is not the lever; INFRA/DDRPHY power-down plus its restore path is. §8 and §21 below are corrected accordingly; the original wording remains in git history (POWER-FINAL-05 commits).

Naming note: the images in the request called "POWER-FINAL-04" are the repository's DEEPSLEEP-FINAL-04 (Linux `5e26757`).

## 1. Exact installed firmware

DEEPSLEEP-FINAL-04: Linux `5e267571d584da7fbe356d3161801ba15f87fa57`, Reborn `97ff8c357bab12319087740d7c97b5051e6588f5`, kernel `6.18.0-y2linux-platform-v1-deepsleep-final-04`, root v1.34, taint 0, SPM mode `SPM_CPU_SHUTDOWN_INFRA_RETAINED`, suspend PCM = vendor 597-word `pcm_suspend` (IM length 596; the runtime-idle line of the same sysfs file reports the separate 480-word `dpidle`), `system_sleep_abi=1`, `maintenance_seconds=600`. Verified read-only in archive 68 (helpers and Reborn byte-identical to the build). The device was unplugged for the overnight test when this phase started and was deliberately not contacted. [measured]

## 2. DEEPSLEEP-FINAL-04 evidence review (archives 72–73, raw journal)

Recomputed from `power-journal.jsonl` and `suspend-last.json` of archive 72: main sleep from BOOTTIME 1364.1 to 5188.7 (3824.6 s elapsed), product receipt `suspended_seconds=3805.25` (99.49%, confirmed). Six maintenance wakes: resumes at 1965.2, 2568.2, 3171.2, 3774.2, 4377.2, 4980.2; each followed by `suspend_maintenance_wake` 0.2 s later and re-entry 2.5 s after resume (1967.7 … 4982.7). Resume-to-resume spacing is exactly 603.0 s = 600.0 s timer + ~3.0 s overhead (~2.5 s awake plus entry/restore latency). SPM boot totals 9 entries / 9 resumes / 0 aborts / 0 restore failures. No unexplained wake: the extra 1.2 s entry at 1358.0 coincides with cable removal. [measured]

## 3. Measurement capabilities

On-device: BAT0 voltage (AUXADC BATSNS, 15-bit) and PMIC die temperature. `current_ua`, `charge_counter_uah`, `temperature_millicelsius` are `null` in `/run/y2/power.json`. [measured] The charger driver reads an `ISENSE` ADC channel, but the ADC driver documents it as "voltage only"; prior M4 work found ISENSE−BATSNS = −0.08 ± 1.6 mV with no calibrated current meaning. [measured, archive m4-adc] No coulomb counter / fuel gauge is exposed by the MT6323 port. **No on-device battery current measurement exists; no mA value may be claimed from software.**

## 4. Battery current sensor availability

NO (see §3). Programmed charge limits (450000 µA SDP etc.) are ceilings, not measurements.

## 5. Battery capacity evidence

`nominal_capacity_mAh` is `null` in the repository's power data; the owner does not know the pack label. [unknown] Budget below is a sensitivity table, not a claim about this pack.

## 6. MT6323 regulator inventory (from DT, kernel/dts/innioasis-y2.dts) [source]````````````````````

| Rail | Setting | Always-on | Consumers / note | Suspend question |
| --- | --- | --- | --- | --- |
| vproc | 1.15–1.25 V | yes | CPU DVFS (sole owner) | SPM/PWRAP sleep value not yet audited |
| vgp2-audio | 1.8 V | yes ("shared ownership not fully qualified") | feeds fixed GPIO "regulators" cs43131-en20 → en18 → en15 | stays enabled while DAC enables are low; analog supply never removed |
| vcn18, vcn28, vcn33_bt, vcn33_wifi | 1.8/2.8/3.3/3.3 V | no | connectivity (CONSYS, BT/Wi-Fi) | radios "off": rail state at suspend not yet read |
| ldo_vio18 | 1.8 V | yes | eMMC I/O | required |
| ldo_vmch / ldo_vmc | 3.3 V / 1.8–3.3 V | no | microSD | card power policy not yet audited |
| VCORE/VM/VIO28/VIBR/others | not described in DT | boot-inherited | loader state | inventory incomplete: needs read-only PMIC register dump |

Only DT-declared rails are listed; rails the loader enables and Linux never claims are [unknown] until a read-only snapshot is taken.

## 6a. Measured PMIC state (awake, archive 77–78, 2026-10-08) and vendor suspend golden table [measured + source]

Read-only snapshot on DEEPSLEEP-FINAL-04 (boot `aae0ddb3`, USB connected, screen off, Wi-Fi/BT in use) and a full read-only PMIC register dump (`/sys/kernel/debug/regmap/1000d000.pwrap/registers`, 2079 registers, 2 volatile between two dumps), decoded with the upstream MT6323 enable tables. This is the awake state; it is not the state during suspend.````

| Rail | Hardware enable / status (awake) | Linux claims it? | Note |
| --- | --- | --- | --- |
| VPROC, VSYS (bucks) | on / on | VPROC always-on | CPU and system supply |
| VTCXO 2.8 V | on / on | no (loader) | 26 MHz TCXO buffer; LP_SEL bit already set |
| VA 2.8 V | on / on | no (loader) | analog/AUXADC; LP_SEL not set |
| VIO28 2.8 V | on / on | no (loader) | peripheral I/O; LP_SEL not set |
| VUSB 3.3 V | on / on | no (loader) | USB PHY LDO; on while cable connected; unplugged state unknown |
| VMC / VMCH (SD I/O, SD VCC) | on / on | SD host | SD card powered; no cap-power-off-card |
| VEMC3V3 (eMMC VCC) | on / on | no (loader) | retained in suspend by patch 0029 |
| VM 1.2 V, VIO18 1.8 V, VRTC | on / on | VIO18 always-on | memory/I-O/RTC; required |
| VGP2 1.8 V | on / on | always-on | audio analog; DAC enables are low |
| VCN18, VCN33_WIFI (VCN33_BT hw bit) | on | connectivity driver | held only while Wi-Fi/BT is active: runtime_suspend → power_off() disables clock, SPM radio power and all four rails (core.c) |
| VCN28, VGP1/3, VCAM*, VIBR, VRF18, VSIM1/2, VPA | off | no | off |

The vendor kernel validates suspend against golden registers (`mt_power_gs_suspend.c`, `mt_power_gs_array.c`, `mt6323_power_gs_suspend_data`, 44 entries). Comparing them with the live awake dump: 25 of 44 differ. Expected (golden) in vendor suspend, but not so on the Y2 when awake: **VMC, VMCH, VEMC3V3 and VCN18 enable bits off (SD power, eMMC VCC and connectivity rail are removed in vendor suspend); LP_SEL bit0 set on VA, VIO28, VUSB, VM, VIO18** (low-power mode of the always-on LDOs); VPROC/VSYS sleep-voltage enables and control bits (`0x212`, `0x216`, `0x21c`, `0x230`, `0x256`, `0x310`); top-clock/OSC control (`0x4e`, `0x102`, `0x108`, `0x10e`, `0x120`). Data: `docs/validation/data/y2-pmic-suspend-golden-vs-awake-20261008.json`. The vendor sets these in `PMIC_INIT_SETTING_V1` (`pmic_mt6323.c`, chip ≥ E2, 20130604_0.85v); Y2Linux applies only the connectivity subset (`kernel/platform/connectivity/core.c: pmic_prepare()`). Whether each golden difference is already corrected by the Y2's own suspend path (e.g. regulator framework, SPM program) is unknown until the register state is read at suspend entry.

## 6b. Suspend-probe results (archives 79–81, 2026-10-08) [measured]

First real before/after-sleep PMIC capture on DEEPSLEEP-FINAL-04 (boot `aae0ddb3`): owner unplugged ~20:33 CEST, reconnected ~21:04; product receipt 1849.9 s suspended, 3 maintenance wakes, SPM 7 entries/7 resumes, aborts 0, taint 0. The probe (read-only) took 11 captures with no capture overlapping a suspend; each full PMIC dump takes 38 ms. Captures are the state ≈0.1–0.7 s before the freezer (`pre-entry`), 0.8 s after each maintenance wake, and at the first userspace instant after resume. They are not readings taken while the SoC sleeps.``````

| Rail / bit | pre-entry (quiesced, unplugged) | post-resume | Reading |
| --- | --- | --- | --- |
| VCN18, VCN33_WIFI, VCN33_BT (radios) | off | off | confirms the connectivity driver releases all rails before sleep |
| VMC, VMCH (SD I/O, SD VCC) | on | off (back on ~1 s later) | the SD card is powered off across suspend by the MMC core; the earlier static guess that it stays powered was wrong |
| VEMC3V3 (eMMC VCC) | on | on | retained by design (patch 0029); vendor suspend removes it |
| VA, VIO28, VUSB, VM, VIO18, VRTC, VTCXO, VGP2, VPROC, VSYS | on | on | VUSB is enabled with the cable removed; VUSB/VIO28/VA/VM/VIO18 have LP_SEL=0 |
| LP_SEL (bit 0) | only VTCXO set | same | vendor sets it on VA, VIO28, VUSB, VMC, VMCH, VEMC3V3, VM, VIO18 |
| VPROC/VSYS sleep-voltage enables (0x230, 0x256, …) | 0 | 0 | vendor golden expects 1 |

Registers that changed between `pre-entry` and `post-resume` (excluding 11 volatile counters/ADC registers): only `0x504`/`0x506` (SD rails) plus `0x13a` and `0x73a` (minor). The SPM sleep path does not visibly switch any PMIC low-power configuration bit: the vendor's static sleep configuration (LP_SEL, sleep voltages) is simply absent. Golden-table differences: 22 at pre-entry (down from 25 awake; the three connectivity rails now match), 20 at post-resume.

Interpretation limits: LP_SEL only lowers LDO quiescent current when the SoC releases its 26 MHz request (SRCLKENA) in sleep; whether the Y2's `pcm_suspend` program does is unknown. A different value at the instant of sleep cannot be excluded because the SPM could change and restore state, but the static configuration bits are not expected to be toggled.

## 7. SoC power-domain inventory

Not yet complete. Known from source/docs: SPM mode keeps INFRA/DDRPHY powered; CPU cores shut down; MFG is the only SPM power domain Linux models; thermal monitor, UART (26 MHz), GPT (13 MHz), PWRAP, AUXADC clocks are retained in awake runtime summaries. [source]

## 8. SPM suspend configuration — primary finding

Y2Linux runs the vendor `pcm_suspend` (597 words, v34rc10, non-MT6333) with `cpu_pdn=1, infra_pdn=0` (INFRA/DDRPHY power kept). **[source + measured: `spm-pcm.h` words identical to vendor, SHA-256 `0ee71194…6ab94`; state line `pcm_length=596`]** The runtime DORMANT (C3) idle uses the separate 480-word `pcm_dpidle` and is unrelated to full suspend. The exact vendor kernel (`android.googlesource.com/kernel/mediatek` @ `d53dd75c…`, `arch/arm/mach-mt6582/mt_spm_sleep.c`, `mt_sleep.c`) runs the same program with its defaults `slp_ck26m_on=0`, `slp_cpu_pdn=1`, `slp_infra_pdn=1`: `spm_go_to_sleep(cpu_pdn=1, infra_pdn=1)` = CPU shutdown, INFRA/DDRPHY power down, followed by `mtk_uart_restore()`. The only code difference is the `infra_pdn` argument: it clears `CC_DISABLE_INFRA_PWR` in `SPM_CLK_CON` (`spm_kick_pcm_to_run`) and selects the post-wake UART restore. [source; stock binary `spm_go_to_sleep`/`slp_will_infra_pdn` confirm the default `infra_pdn=1`] Y2's wake mask: see below. The vendor wake mask for suspend is `KP|EINT|CONN_WDT|CCIF_MD|CONN|USB_CD|THERM|SYSPWREQ|MD_WDT` (`SPM_BYPASS_SYSPWREQ=0` outside LDVT); Y2's entry mask is `0xfedfbfdb` (enabled bits 2, 5, 14, 21, 24 = KP, EINT, USB_CD, THERM, SYSPWREQ). [source + measured] Consequence: the largest unexamined electrical lever is whether the Y2 may safely run the same PCM with `infra_pdn=1` (INFRA/DDRPHY power-down with DRAM self-refresh handled by the program) together with the restore of whatever INFRA power-down resets (INFRACFG/PERICFG, UART). It is also the highest-risk change (DRAM retention, PWRAP/PMIC hand-off, resume vector). Not attempted. See §21–23.

## 9. DRAM retention

Linux relies on the SPM program for self-refresh; with INFRA/DDRPHY retained the DRAM path is the conservative one. Whether the PCM program puts DRAM in self-refresh and whether the DDRPHY could safely power down is vendor-program behaviour not yet traced instruction by instruction. Data integrity across 10 clean 04 suspends is empirical. [unknown for electrical state]

## 10. Clock / PLL / oscillator state

26 MHz crystal path and APSRC: vendor program toggles them via events (vec0/vec1 "26M wake/sleep", vec2/vec3 "APSRC wake/sleep"). Whether the `pcm_suspend` program actually switches the 26 MHz source off in the Y2's current configuration cannot be read during sleep. Needs the SPM wake/`R13` status and a PCM trace, or external measurement. [unknown]

## 11. DAC / audio power

PCM closed, codec/AFE runtime suspended, DAPM biases off, GPIO15/18/20 low (idle-bias fix present). `vgp2-audio` remains enabled (always-on, shared). Candidate: allow VGP2 to be disabled in suspend only if every consumer is proven; exact consumer list [unknown]. [measured for GPIO/DAPM, unknown for rail current]

## 12. Display / GPU power

Backlight `bl_power=4` in every dark sample; display pipeline and Lima idle state not yet audited for electrical shutdown.

## 13. Wi-Fi / Bluetooth power

`18070000.connectivity` is runtime-suspended at each maintenance wake [measured]; whether `vcn*` rails are actually disabled while suspended is [unknown] pending a read-only regulator snapshot.

## 14. USB PHY power

04 retains the prior USB clock lifecycle fix (bus clock off when disconnected, `monitor_parked=1`). PHY analog power unverified.

## 15. eMMC / SD power · 16. APT32F input power · 17. RTC / Power wake dependencies

Not yet audited. RTC and Power key are MT6323 children with `wakeup-source`; wake attribution is via PMIC child IRQ counters (archives 47/50/15). The APT32F wheel (I2C0 0x51, EINT 55) is interrupt-driven; its internal low-power mode is [unknown].

## 18. Ten-minute maintenance wake — root cause

Owner: the SPM PCM timer.`Y2_SPM_TIMER = 19660800 ticks = 600.000 s` at 32768 Hz, armed in `spm-suspend-policy.h` (`SPM_PCM_TIMER_VAL`), with a 630 s PCM watchdog; exposed as `maintenance_seconds=600`. It mirrors the vendor constant `SPM_WAKE_PERIOD 600 /* sec */` in `mt_spm_sleep.c`. The product helper uses that wake for a bounded battery safety check and then re-enters. Not the RTC, journal or a userspace timer. [source + measured]

## 19. Maintenance wake energy impact

Awake ~3.0 s per 603 s cycle (0.50% duty) [measured]. Awake current is [unknown]. Average added current = 3.0 s × I_awake / 603 s; for illustrative I_awake = 30 / 60 / 100 mA that is 0.15 / 0.30 / 0.50 mA [arithmetic on hypothetical inputs, not a measurement].

## 20. Power-budget breakdown and allowed average current

Average current allowed for ≤1 percentage point over the window, as a function of usable capacity C (1% = C/100):

| Usable capacity | 8 h | 12 h | 24 h |
| --- | --- | --- | --- |
| 400 mAh | 0.50 mA | 0.33 mA | 0.17 mA |
| 600 mAh | 0.75 mA | 0.50 mA | 0.25 mA |
| 800 mAh | 1.00 mA | 0.67 mA | 0.33 mA |
| 1000 mAh | 1.25 mA | 0.83 mA | 0.42 mA |
| 1500 mAh | 1.88 mA | 1.25 mA | 0.63 mA |

Plausibility, not a measurement: with INFRA/DDRPHY, the 26 MHz path and DRAM self-refresh retained, the achievable floor is [unknown]; reaching ≤1.25 mA average on a 1000 mAh pack would leave only ~0.75 mA for everything except wakes. Whether the target is physically reachable cannot be decided without a current measurement. Component breakdown: all rows [unknown] except maintenance duty (§19).

## 21. Optimization candidates, ranked (all unimplemented)

Revised ranking after the PMIC evidence (still unimplemented; every item needs a staged, backstopped test):
  - Evidence first: read the PMIC registers (read-only) at suspend entry and on resume, and compare to the vendor golden table. This tells

which of the 25 differences are real in suspend. Low risk.
  - SD card power in suspendalready off in suspend (probe, §6b).
  - PMIC static low-power configuration from `PMIC_INIT_SETTING_V1` (vendor), applied once at boot/probe: `LP_SEL` on VA, VIO28, VUSB, VMC, VMCH, VEMC3V3, VM, VIO18

(0x404/0x500/0x502/0x504/0x506/0x508/0x552/0x556 bit 0). Exact-source backed, absent today, no effect while the SoC requests 26 MHz. Needs a kernel/DT change (new image) and an owner-run before/after comparison; writes must be reviewed.

1b. VUSB while disconnected: LDO enabled with the cable removed. Verify in the vendor `usb20.c` whether the LDO is enabled only while a cable is present.
  - LDO LP_SEL bits (VA, VIO28, VUSB, VM, VIO18) from `PMIC_INIT_SETTING_V1`: standard MediaTek low-power-mode select, exact-source backed. Effect only

if SRCLKEN is deasserted in suspend (26 MHz request released) — not yet shown for the Y2's `pcm_suspend` program.
  - eMMC VCC (VEMC3V3) in suspend: vendor removes it with eMMC sleep; the Y2 deliberately retains it for reliability (patch 0029). High risk (root and data).
  - VPROC/VSYS sleep voltage (`VPROC_VSLEEP_EN`, `VOSEL_SLEEP=0x18`): reduces leakage; conflicts with the Y2's software-controlled DVFS (`VPROC_VOSEL_CTRL`). High risk.
  - Vendor `infra_pdn=1` (INFRA/DDRPHY power-down with the existing `pcm_suspend`), see §8: largest, riskiest.
  - Vendor `infra_pdn=1` (INFRA/DDRPHY power-down with the already-present `pcm_suspend`) — largest expected effect, highest risk; requires staged,

backstop-protected experiments and an exact-source port of the post-wake restore (UART and the INFRA-domain register blocks).
  - Read-only regulator/clock/SPM snapshot at suspend entry and on resume — needed first to find any rail left on (`vgp2`, `vcn*`,

SD rails). Low risk, informative.
  - VGP2 audio rail in suspend — disable only after a consumer audit; DAC GPIOs are already low.
  - Maintenance interval/work — lengthening 600 s is safe only if the battery-safety check and watchdog assumptions hold; saves at most

the §19 cost.
  - APT32F / USB PHY / SD power — need datasheet/firmware evidence before any change.

## 22. Changes implemented

POWER-FINAL-05 (source `837b614`, built, validated, sealed, not flashed): vendor `PMIC_INIT_SETTING_V1``LP_SEL` (bit 0) on VA 0x404, VIO28 0x500, VUSB 0x502, VM 0x552, VIO18 0x556: PMIC write whitelist extended by exactly those bits (`policy.h`), `kernel/platform/pmic-lowpower.c` applies them once ~10 s after boot on E2 silicon (CID ≥ 0x2023) with readback verification, `/sys/firmware/y2_pmic/lp_sel` (root) reverts/sets at run time. Expected effect: five golden-table differences close (22→17 at suspend entry); electrical benefit unmeasured. Owner-authorized. Tests: `tests/test_pmic_lowpower.py` (6), production suite 560 cases PASS.

Not implemented (see §23): storage-rail `LP_SEL` switch (blocked by the safety classifier, eMMC supply register), VUSB disable (vendor keeps it on), VGP2 off in suspend, VPROC/VSYS sleep voltage, eMMC supply removal, vendor `pcm_suspend`.

## 23. Changes rejected for safety

Any PMIC register write, rail disable, PCM/SPM change or oscillator change without an exact-source, staged and backstopped test design.

## 24–30. Before/after, same-boot, early-boot, Power, RTC, USB/charger, battery observations
  - Early-boot (6 min target): 04 passed an even earlier case (entry at 39.4 s, 551.8 s asleep, archives 74–75). [measured]
  - Power-button and RTC wake on 04: NOT TESTED yet (earlier 02 evidence only). USB wake: repeatedly observed (label `unknown`).
  - Battery: 71%→69% / 3.966→3.948 V over the one-hour run is provisional and includes post-charge relaxation. Not an energy result.
  - Overnight (≈8 h) unplugged drain test on 04: pending; it is the baseline for any later comparison.

## 31–32. Real current measurements / external measurement requirements

No real current measurement exists. An external measurement is required for any further quantitative optimization. Safe options need the owner's decision and must not involve improvised battery wiring or shorting; a USB power meter cannot see battery-only suspend current. A suitable method is a bench power supply or high-dynamic-range source-measure unit in place of the battery on a purpose-made, isolated connection made by someone qualified, with µA resolution and ≥1 kS/s capture to see the ~3 s wake bursts. Expected ranges are not stated because none are source-backed for this unit.

## 33. Regression tests · 34. Commits · 35. Candidate and hashes · 36. Remaining physical limits

No code was changed in this phase, so no new tests, commits (other than this report), candidate or hashes exist. Limits: no battery current sensing; unknown capacity; INFRA/DDRPHY retained by design; DRAM/26 MHz electrical state during sleep unobservable without external measurement.

## Next steps (proposed)
  - Finish the owner's overnight 04 drain test (baseline) and archive.
  - Read-only snapshot tool: regulator (`/sys/class/regulator`), clock summary, SPM/wake registers, runtime-PM states, captured just before

entry and immediately on resume (no claim about the in-between interval).
  - Trace which state the vendor `infra_pdn=1` path loses and restores (done in POWER-FINAL-06: only `mtk_uart_restore`; PERICFG/INFRACFG are INFRASYS-MTCMOS blocks per the manual) and design the staged experiment.
  - Owner decision on external current measurement.

## Candidate POWER-FINAL-05 (2026-10-08)

Folder `out/y2linux-platform-v1-power-final-candidate-05/` (own `OWNER-HANDOFF.md`, `SHA256SUMS` verified), symbols `…-candidate-05-symbols/`, worktrees `/home/luca/Dokumente/Code/worktrees/y2-power-final-05/`. Release `1.0.0-platform-v1-power-final-candidate.5`, root v1.35, kernel `6.18.0-y2linux-platform-v1-power-final-05`. BOOTIMG (7256064 B) `0137a855db96d8f94005333941495c4fdaa2f81c9eb653458b77e9c0fd044117`; Y2ROOT (536870912 B) `9175185fd577b759302337cc8d17f678fde3dc621525b90d45cf6cb370e99a4d`. Preserving scatter identical to 04; `fallback/` = sealed 04. Validation: container suite 560 PASS, 10 native packaging + 27 splash PASS, Reborn fmt/clippy/335 tests, QEMU, ELF 384/1411, package/privacy PASS. Physical: NOT_RUN.

## POWER-FINAL-05 first check (owner flashed; archives 82–84, 2026-10-08) [measured]

Boot `3cae62f2`, taint 0, `versions.json` = POWER-FINAL-05 / Linux `837b614` / root v1.35; installed Reborn `cc305fbf…1ac1` and the three PM helpers match the build byte-for-byte. dmesg: `y2-pmic-lp: LP_SEL set on VA/VIO28/VUSB/VM/VIO18 (CID=0x2023 err=0)` at 10.7 s. `/sys/firmware/y2_pmic/lp_sel`: `applied=1 error=0 VA=1 VIO28=1 VUSB=1 VM=1 VIO18=1`. Full read-only PMIC dump (2079 registers): LP_SEL bit 0 set on VA/VIO28/VUSB/VM/VIO18 (04: only VTCXO); vendor golden differences 25 → 20 awake, the five closed entries being 0x404/0x500/0x502/0x552/0x556; no regulator enable bit differs from the 04 baseline. ext4 errors 0, pstore empty, application healthy; the 04 product guard (`pending:false`) does not match the new identity. Charger: Not charging 89% / 4.085 V (provisional). Suspend behaviour on 05 is not yet tested; no power benefit is claimed.

## POWER-FINAL-05 suspend probe run (archives 85–87, 2026-10-08) [measured]

Owner unplugged 22:07 CEST, reconnected ~22:34. Same boot `3cae62f2`, taint 0, product receipt 1573.4 s suspended, 2 maintenance wakes, SPM 3 entries / 3 resumes / 0 aborts, PM `COMPLETE`, application restored. Probe: 8 captures, none overlapping a suspend, each full PMIC dump 35 ms.

| Check | 04 (archive 81) | 05 (archive 87) |
| --- | --- | --- |
| LP_SEL set at every capture | VTCXO only | VTCXO, VA, VIO28, VUSB, VM, VIO18 |
| Vendor golden differences at pre-entry | 22 | 17 |
| Golden differences at post-resume | 20 | 16 / 15 |
| Radios (VCN18/VCN33) at pre-entry | off | off |
| SD rails across suspend | on → off at resume | same |
| eMMC supply (VEMC3V3), VUSB, VGP2 | on | on |
| PMIC registers changed across a sleep (non-volatile) | 0x504, 0x506, 0x13a, 0x73a | 0x504, 0x13a, 0x52a, 0x73a (SD-rail/ADC state) |

The low-power select bits are unchanged across every sleep (not toggled by the SPM path), suspend/resume behaves exactly as on 04, and no rail enable differs from 04. Not shown: any current or SOC benefit. Still open: Power-button wake and RTC wake on 05, early-boot on 05, overnight A/B (bits set vs `echo 0 > /sys/firmware/y2_pmic/lp_sel`), an external current measurement.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
