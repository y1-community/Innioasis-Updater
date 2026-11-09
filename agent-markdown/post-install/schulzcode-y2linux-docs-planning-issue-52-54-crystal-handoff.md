---
title: "#52 / #54 — CS43131 crystal does not start on Y2Linux (handoff, 2026-10-23) - Innioasis Updater"
description: "52 / 54 — CS43131 crystal does not start on Y2Linux handoff, 2026-10-23 Everything below was verified by reading reports, source and the stock kernel binary. Do not re-de"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-issue-52-54-crystal-handoff.html"
---

# #52 / #54 — CS43131 crystal does not start on Y2Linux (handoff, 2026-10-23) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# #52 / #54 — CS43131 crystal does not start on Y2Linux (handoff, 2026-10-23)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# #52 / #54 — CS43131 crystal does not start on Y2Linux (handoff, 2026-10-23)

Everything below was verified by reading reports, source and the stock kernel binary. Do not re-derive it; build on it.

## The problem in one paragraph

Two users' players (install IDs `2813306c` = GitHub #48/#51/#52, `0400eb78` = #54) play headphone audio on the stock ROM, but on Y2Linux the CS43131 DAC's **22.5792 MHz crystal does not start**: the DAC's status shows `XTAL_ERR` and never `XTAL_RDY`, the DAC has no clock, and playback is silent while the UI shows the song playing. The owner's player (and about 20 other installs) never shows this: `ready_ms=30 errors=0`. On 8.24 both affected players fail right at power-up after a fresh boot, with nothing played yet. It is a systematic difference between stock and us that only some units are sensitive to, not something stored on the device: a clean SP Flash Tool install of 8.24 fails the same way.

## Hardware / wiring (from DT and stock RE)
  - DAC: CS43131 rev A1 on I2C1 addr 0x30 (bus shows as `0-0030` or `1-0030` depending on boot).

No IRQ line in our DT (status polled); no reset GPIO in our DT. Stock does not drive a reset pin either.
  - Supplies (`kernel/dts/innioasis-y2.dts` ~l.134–157, 349–357, 383–390):

VA/VP/VCP = PMIC LDO VGP2 1.8 V (`vgp2-audio`); VD = GPIO18-enabled rail; VL = GPIO15-enabled rail; GPIO20 enables a third rail. Modeled as fixed regulators chained VGP2 → GPIO20 → GPIO18 → GPIO15, startup delays 0/0/50 ms. GPIO rail voltages are nominal (not measured).
  - At every boot the regulator core logs `vgp2-audio: Bringing 2500000uV into 1800000-1800000uV`

(selector is at the 2.5 V reset value before we set 1.8 V). `cold_start=0` = VGP2 was off at probe.
  - SoC I2S pins GPIO43 (BCK), 44 (WS), 46 (data) are muxed by our pinctrl at ≈0.28 s, i.e.

before the DAC rails come on at ≈0.52–0.60 s (DAC probe). Not yet compared with stock. The SoC is I2S master (codec ASP slave: ASP_CLOCK_CONF 0x40018 = 0x0C, same as stock).
  - GPIO8 (amp enable?) is held output-low by us. Its stock use is unresolved.
  - Stock writes PMIC ABB/AUDTOP registers (MT6323 analog audio) that we do not reproduce

(`docs/knowledge/m3-audio-architecture.md`, "Source limit" row). Their relevance is unknown.

## Stock behaviour (RE of `out/rea/fm-kernel.elf`, `llvm-objdump -d --triple=armv7a`)````````````````````````````````````````````

| Function | Address | What it does |
| --- | --- | --- |
| cs43131_i2c_probe | 0xc054c310 | hwPowerOn(6 /*VGP2*/, 0x708 /*1800 mV*/); GPIO20 mode0/out/1; GPIO18 same; GPIO15 same; msleep(50); read 0x10000 (ID); cs43131_hw_init; EINT16 register; … |
| cs43131_hw_init | 0xc054c164 | PWDN_CTL(0x20000)=0x00 (everything on incl. XTAL, PLL, CLKOUT, ASP, XSP, HP); msleep(20); SYS_CLK_CTL_1(0x10006)=0x04 (MCLK=EXT crystal, 22.5792); 0x1000B=1; 0x1000C=5; 0x40018=0x0C; 0x50000=0; 0x50001=0; 0x90000=2; route/volume; PWDN_CTL=0 again; HP_DETECT(0xD0000)=0xCA; INT_MASK_1(0xF0010)=0x9F (XTAL_RDY/ERR masked); msleep(12). Never reads XTAL_RDY/XTAL_ERR, never writes CRYSTAL_SET (0x20052 stays 0x04 = 12.5 µA reset value). |
| cs43131_on (per stream) | 0xc054c648 | If powered-down flag: hwPowerOn(6,1800), GPIO20/18/15 = 1, msleep(50), hw_init. Then GPIO15=1, msleep(2), 0x10010=0x99, 0x80032=0x20, PWDN &= 0xAF (HP+ASP on), msleep(15), 0x80032=0, 0x10010=0, route, clear interrupts. |
| cs43131_off | 0xc054c7a0 | PWDN \|= 0x10 (HP down), poll 0xF0000 bit0 up to 4×10 ms, PWDN \|= 0x40 (ASP down). Crystal stays on. Powers down fully only if a power-down was deferred. |
| cs43131_power_down_hw | 0xc054b620 | EINT16 mask; GPIO15=0, GPIO18=0, GPIO20=0; hwPowerDown(6). |
| cs43131_early_suspend | 0xc054bed0 | Screen off: if not playing, power_down_hw now, else defer to cs43131_off. |
| cs43131_late_resume | 0xc054c284 | Screen on: full power-on + hw_init (as in cs43131_on). |

So stock re-powers the DAC and restarts the crystal at every screen-off → screen-on while idle. Stock `system.img``/etc/audio_policy.conf`: primary output 44100 Hz only, so stock never uses the codec PLL.

## Our implementation (Linux 6.18 upstream `cs43130.c` + overlay `kernel/patches/0030-cs43130-system-pm.patch`)

Line numbers are in the patch file.
  - `y2_xtal_power_on` (l.83): CRYSTAL_SET bias (DT `cirrus,xtal-ibias = <2>` → 0x04, same as stock),

read INT_STATUS_1 to clear it, PWDN_CTL clears XTAL+PLL+CLKOUT (ASP/XSP/HP/DSPIF stay down, so idle PWDN=0xF0, while stock idle is 0x00 and later 0x50), `msleep(20)`, unmask XTAL_RDY, read INT_STATUS_1 once (counts `errors`, sets `ready`/`ready_ms`), re-mask RDY, SYS_CLK_CTL_1 = EXT/22.5792. Called at the end of probe (l.1046) and in runtime resume after `regcache_sync` (l.1193).
  - `y2_xtal_start` (l.178), run under clk_mutex at stream start (`cs43130_change_clksrc`):

if ready or assumed → read status; on XTAL_ERR → `y2_codec_cycle` (l.163: runtime suspend, rails off 500 ms, runtime resume). Otherwise wait (RDY unmasked, poll every 20 ms) until the crystal has run 1000 ms (`Y2_XTAL_WAIT_MS`), then use it anyway ("assumed", `unconfirmed++`) and log `XTAL not ready … used as stock does`.
  - Runtime PM: autosuspend 120 s (l.1047). The `y2_hp/hold` pm_runtime reference keeps the DAC on while

the screen is on (Reborn sets it). Runtime suspend = PDN_XTAL/PLL, MCLK→RCO, rails off. System sleep = `pm_runtime_force_suspend/resume`.
  - INT_MASK_1 = 0x97 (XTAL_ERR unmasked, as upstream) vs stock 0x9F.
  - 8.24: AFE/codec 44.1 kHz only (no PLL); `y2_codec_cycle` on XTAL_ERR; probe cold start if rails were on.
  - Sysfs: `/sys/bus/i2c/devices/*-0030/y2_hp/xtal` →

`running= ready= ready_ms= unconfirmed= errors= boosted= cycles= cold_start=`.
  - Register dump of the #52 unit on 8.24 (`debugfs/regmap/1-0030/registers`) equals the owner's apart from

power state: 0x10006=04, 0x1000B=01, 0x1000C=05, 0x1000D=00, 0x20000=f0, 0x20052=04, 0x40018=0c, 0x90000=02.

### Known gap in the 8.24 self-repair

The power cycle only runs when the crystal was ready/assumed earlier. The first stream after boot takes the wait-then-assume path instead, and the 20-ms read at power-up already cleared the sticky XTAL_ERR. On both 8.24 reports `cycles=0`. Open question: do masked status bits latch? If XTAL_RDY does not latch while masked, an RDY that came after the 20-ms read is never seen, and "not ready" can be a false negative. XTAL_ERR is unmasked, so it is real.

## Evidence timeline (ledger: `UserReports/REVIEWED.md`, rows for 2813306c / 0400eb78)``````````````````````

| Build | Unit | Result |
| --- | --- | --- |
| 8.11–8.16 | #52 | XTAL_READY -110 on reopen (upstream stopped the crystal at every hw_free, waited 100 ms) |
| 8.19 | #52 | every open: XTAL not ready … status1=08 (XTAL_ERR); 1 of 9 rail cycles recovered |
| 8.20 (15 µA bias) | #52, #54 | still fails; #54 never plays (16 opens, all XTAL_ERR); works after a 3-h rest on #52 |
| 8.21 (crystal from power-up, used after 1 s) | #52 | ready at power-up, then XTAL_ERR (status1=49) at track starts while skipping; after a restart never ready, PLL_READY -110 |
| 8.21 | #54 | never ready, silent |
| 8.22 | #54 | XTAL not ready 45930 ms status1=48, then status1=69 / 48 while running |
| 8.23 (stock DAC power-up, hold) | #52 | OTA boot: ready 30 ms, ≈4.5 min fine, then failures, all at 48 kHz opens (PLL_READY -110 → XTAL_ERR) |
| 8.24 (no PLL), clean flash | #52 | boot 1: first stream at 146 s: XTAL not ready 146230 ms, status1=48 → silent. Restart, boot 2: ready=0 errors=1 with nothing played (ERR at the 20-ms read) |
| 8.24 | #54 | first stream at 61 s: XTAL not ready 60800 ms, status1=48, ready=0 errors=1 cycles=0 → silent |
| stock ROM | #52 | reporter: rapid skipping, no problem |
| 8.24 | owner | ready_ms=30 errors=0; hundreds of skips fine |

status1 bits: 0x40 HP_PLUG, 0x20 HP_UNPLUG, 0x10 XTAL_RDY, 0x08 XTAL_ERR, 0x04 PLL_RDY, 0x01 (unknown, seen with 0x49).

Wrong theories already ruled out: marginal crystal needing more bias (15 µA no help); crystal stopped between streams (8.21 keeps it on); 48 kHz/PLL (8.24 no PLL, still fails); stored state on the device (clean flash fails); warm restart not cutting VGP2 (VGP2 is at its reset value and off at probe); a system sleep before the first stream in the #52 8.24 boot (boottime = monotonic = 169 s, the syslog jump is the Wi-Fi clock step).

## Untested differences from stock (candidates)
  - I2S pins driven before the DAC has power: our pinctrl muxes GPIO43/44/46 at 0.28 s, the rails

come on at ≈0.55 s; the AFE may also leave the pins driven while the DAC is runtime-suspended. Back-powering through I/O pins can stop a clean power-on reset. Stock's pin mux timing is unknown.
  - Idle power state: stock runs PWDN=0x00 (ASP, XSP, DSPIF, HP on) from hw_init on; we keep

0xF0 (only XTAL/PLL/CLKOUT on). The crystal starts with a different digital load and state.
  - I2C traffic during crystal start: we read INT_STATUS_1 at 20 ms and poll every 20 ms; stock

never reads it. INT_MASK_1 0x97 vs 0x9F.
  - Re-power frequency: stock restarts the crystal at every idle screen wake. We hold the DAC while

the screen is on and then for 120 s, so a bad start persists (but the 8.24 restart failed too).
  - PMIC analog audio (ABB/AUDTOP) and GPIO8 writes that stock makes and we don't.
  - Upstream component probe / `regcache_sync` writes between rails-on and crystal power-on, which stock

doesn't do (HP detect, HP level, defaults).

## Files
  - Overlay: `kernel/patches/0030-cs43130-system-pm.patch` (edit method: patch a copy of

`.cache/sources/linux-6.18`, then `tools/build/refresh-overlays.py <tree>`).
  - Tests: `PYTHONPATH=.:tests:tools/platform python3 -m unittest tests.test_codec_clock`.
  - DT: `kernel/dts/innioasis-y2.dts`; pinctrl `kernel/platform/pinctrl.c`; AFE `kernel/audio/mt6582-afe.c`.
  - Stock kernel ELF: `out/rea/fm-kernel.elf` (symbols present: `cs43131_*`, `hwPowerOn`, `mt_set_gpio_*`).
  - Reports (local, not in git): `UserReports/y2linux-report-20261022-230113.tar.gz` (#52, 8.24);

`UserReports/reports_2026-10-22_0400eb78-…_768b0d04-….tar.gz` (#54, 8.24). Inside each: `commands/dmesg.txt`, `files/data/logs/system.log` (previous boots), `files/sys/bus/i2c/devices/1-0030/y2_hp/xtal`, `files/sys/kernel/debug/regmap/1-0030/registers`.
  - Owner's player (healthy, 8.24) over SSH: `ssh -F /dev/null -o HostKeyAlias=y2linux-production-v1 -i ~/.ssh/y2linux_ed25519 root@10.42.0.1`

(read-only checks allowed; register writes need the owner's explicit OK). The owner's player cannot reproduce the failure.
  - Release flow: `tools/production/release.py` (next label 124, sequence > 8800).

## Fable analysis

Written 2026-10-23 from the handoff above plus a bounded check of `out/rea/fm-kernel.elf`, `kernel/platform/pinctrl.c`, `kernel/audio/mt6582-afe.c`, `kernel/dts/innioasis-y2.dts`, `kernel/patches/0030-cs43130-system-pm.patch`, upstream `cs43130.c/.h` (6.18) and one read-only look at the owner's boot log. Nothing was built, flashed or written to a device.

### New facts (verified)
  - Stock never touches the I2S pins. Every `mt_set_gpio_mode/dir/out` caller in the stock kernel

was decoded by argument (MediaTek passes `pin | 0x80000000`). GPIO43/44/46 appear in none of them. `cs43131_i2c_probe` (0xc054c344–0xc054c3a4) only sets GPIO20, 18, 15 to mode 0 / output / 1, in that order; the second block at 0xc054c554–0xc054c5b4 is the ID-mismatch error path (drives them low, `hwPowerDown(6)`). `cs43131_power_down_hw` writes 15, 18, 20 low. `mt_gpio_probe` (0xc03907f8) applies no default pin table; the I2S mux therefore comes from LK on both ROMs.
  - Our pinctrl inherits LK's mux (`pinctrl.c` function `i2s-lk`: it refuses to probe if the mux is

0 and never writes it). Owner's log: `pin43 mode=4, pin44 mode=4, pin46 mode=3`, printed at 0.28 s but set by LK before the kernel. The 0.28 s in the handoff is the log line, not a mux change.
  - Our AFE drives nothing while idle.`mt6582-afe.c`: `AFE_I2S_CON3.I2S_ON` is set only in

`prepare` and cleared in `shutdown`, `AFE_ON` is cleared in runtime suspend; probe ends with `pm_runtime_idle`. A codec cycle in `y2_xtal_start` runs from `hw_params`, before the AFE `prepare`, so BCK/WS/DATA are static while the rails are off. Same state as stock's `AudDrv_I2S_Clk_Off` idle.
  - GPIO8 is the speaker-amplifier enable. Stock `aw87559_i2c_probe` (0xc054ab50–0xc054abe4),

`aw87559_on/off` and `Speaker_Init`/`Sound_Speaker_Turnon` are its only users; the probe leaves it mode 0 / output / low. Our hog (output low) matches stock. Candidate 5's GPIO8 half is closed.
  - VGP2 is programmed the same way. Stock `hwPowerOn(6, 1800)` → `dct_pmic_VGP2_sel(1800)` →

`upmu_set_rg_vgp2_vosel(3)` and `dct_pmic_VGP2_enable(1)` → `upmu_set_rg_vgp2_en(1)`; nothing else. Ours writes the same two fields (`policy.h`: DIGLDO_CON8 enable, DIGLDO_CON29 selector).
  - Upstream reset value of PWDN_CTL is 0xFE (`cs43130_reg_defaults`). Our power-on

`regmap_write_bits(PWDN_CTL, XTAL|PLL|CLKOUT, 0)` therefore produces 0xF0: ASP, XSP, DSPIF and HP stay powered down while the crystal is asked to start. Stock writes 0x00.
  - At the instant the crystal fails, the only on-chip differences from stock are: (a) PWDN_CTL 0xF0

vs 0x00; (b) one CRYSTAL_SET write (same value 0x04 as reset) and one INT_STATUS_1 read in the microseconds before PDN_XTAL clears, plus the mask-toggle/read at 20 ms. Everything else we do differently (component probe, HP detect, HP level, load measurement, INT_MASK 0x97, PAD_INT_CFG, PMIC audio writes we lack) comes after the 20-ms read that already shows XTAL_ERR on both affected units (8.24 boot 2 of #52, #54). Those later differences cannot be the cause of the power-up failure, whatever else they do.

### Do masked CS43131 status bits latch?

Yes, as far as our own evidence goes. INT_MASK_1 = 0x97 masks bits 7, 4, 2, 1, 0. The affected units reported `status1=49` (8.21, #52) and `69` (8.22, #54): both contain bit 0, which is masked, and were read while the RDY bit was masked. Upstream's IRQ thread also reads every INT_STATUS register and interprets all bits regardless of the mask registers. So the mask gates the INT pin only; the status bits set and stay set until read. Consequence: the "XTAL not ready 146230 ms" first-stream result is a genuine negative, not a missed RDY. (The datasheet itself was not available in the repo; this is inferred from logs + upstream, not quoted from Cirrus.)

### Ranked hypotheses
  - Partial power-up (PWDN_CTL = 0xF0) vs stock's full power-up (0x00) when the crystal starts.

For: it is the only chip-visible difference present at the failure instant (see above); stock starts the crystal with every block (HP amp + charge pump, ASP, XSP, DSPIF) already powered, and only later powers HP/ASP down (`cs43131_off`, idle 0x50) and up again per stream without the crystal ever stopping. If the oscillator's bias/reference or its ready/error detector shares a domain with one of those blocks, a marginal crystal starts reliably only under full power. The 8.21/8.23 boots of #52 (ready at 30 ms, then failures later) show the start is probabilistic on these units, which fits a margin effect better than a hard fault. Against: no datasheet statement ties XTAL start-up to those blocks; the owner's unit starts either way; nothing explains why the crystal later stops (status 0x49 while running) except the same margin. Test (one build, no reflash between tries): module parameter `y2_xtal_full_power` (default 1) plus a sysfs trigger `y2_hp/cycle` (see patch plan). On an affected unit, with nothing playing: `echo 0 > /sys/module/snd_soc_cs43130/parameters/y2_xtal_full_power; for i in $(seq 10); do echo 1 > …/y2_hp/cycle; cat …/y2_hp/xtal; done` then the same with `1`. If `ready=1` appears in ≥9/10 starts with `1` and ≤2/10 with `0`, this hypothesis is proven; equal rates refute it. Even with the retry alone enabled, `tries=` in the sysfs line shows how often a cold start was needed.
  - **Marginal crystal / supply margin on these two units, exposed by anything short of stock's

exact start.** For: 15 µA did not help, 3-h rest did (temperature), starts succeed sometimes. Against: explains why only two units, not why stock is fine; it is the "unit" half of hypothesis 1, not an alternative. Test: the same cycle loop at cold and warm device temperature; the success rate difference is the measurement.
  - I2C traffic around the start (candidate 3).For: stock is silent on the bus for 20 ms after

the PWDN write; we write CRYSTAL_SET + read INT_STATUS_1 just before it and toggle the mask at 20 ms. Against: ERR is already latched when the 20-ms read happens, so that read cannot be the cause; the pre-start write/read are microseconds of 400-kHz traffic on pins unrelated to XTI/XTO. Low. Test: build variant that drops the pre-start CRYSTAL_SET write and status read (`y2_xtal_quiet_start=1`); compare the cycle-loop success rate.
  - Re-power frequency (candidate 4). Not a cause of the boot failure (8.24 fails before any

stream). It only decides how often a bad start gets another chance; the retry in the patch plan replaces it. Test: none needed beyond the retry counters.
  - I2S pins driven before/without DAC power (candidate 1).Ruled out by the facts above: same

LK mux on both ROMs, no kernel mux write on either, our AFE output off while idle, codec cycle runs before `prepare`. Only remaining variant: LK pull-ups on 43/44/46 back-powering VL while the rails are off, but that is identical under stock. Test, if ever wanted:`pin43/44/46 pull` values from the `before pin…` dmesg line, compared with a stock boot log.
  - Component-probe writes (candidate 6), PMIC analog audio (candidate 5). Occur after the

failure instant; cannot cause the power-up ERR. Candidate 2's idle value (0xF0 after the start) and 48-kHz/PLL were already excluded or are covered by hypothesis 1. Not worth reverse-engineering AUDTOP for this issue.

### Patch plan for `kernel/patches/0030-cs43130-system-pm.patch`

Edit method as in Files: patch a copy of `.cache/sources/linux-6.18`, then `tools/build/refresh-overlays.py <tree>`. No DT, pinctrl or AFE change is needed. All new code goes next to the existing `y2_xtal_*` helpers (patch l.43–231) and in `cs43130_runtime_resume` / `cs43130_i2c_probe`. Keep 44.1 kHz-only, keep idle 0xF0 after the start, keep the 120-s autosuspend.
  - Constants and state (next to `Y2_XTAL_WAIT_MS`, l.43):

`Y2_XTAL_START_MS 100` (per attempt: owner is ready at 30 ms, upstream waited 100), `Y2_XTAL_TRIES 3` (power-up attempts per power-on), `Y2_XTAL_STREAM_CYCLES 1` (extra cold start a stream may add). New counters `y2_xtal_tries` (attempts in the last power-on), `y2_xtal_start_ms` (ms from the final PDN_XTAL clear to RDY), `y2_xtal_stream_cycles`. Module params `y2_xtal_full_power` (bool, default true) and `y2_xtal_quiet_start` (bool, default false), `module_param(..., 0644)` so the reporter can flip them without a rebuild.
  - `y2_xtal_attempt(cs43130)` (new, replaces the body of `y2_xtal_power_on` l.83–128):
    - unless `y2_xtal_quiet_start`: write CRYSTAL_SET bias and read INT_STATUS_1 as today;
    - `regmap_read(PWDN_CTL, &keep)` (cache value, holds DAPM's HP/ASP/XSP/DSPIF bits);
    - if `y2_xtal_full_power`: `regmap_write(PWDN_CTL, 0x00)` (stock `hw_init`); else

`regmap_write_bits(PWDN_CTL, XTAL|PLL|CLKOUT, 0)` (today's 0xF0);
    - set `y2_xtal_on = true`, `ready = assumed = false`, `on_since = jiffies`;
    - unmask XTAL_RDY, then `regmap_read_poll_timeout(INT_STATUS_1, st, st & (RDY|ERR), 20000,

Y2_XTAL_START_MS*1000)` (first read at 20 ms as today), re-mask RDY;
    - restore the non-clock bits: `regmap_write(PWDN_CTL, (keep & 0xF0))` (DAPM state back, clock

bits stay 0) — stock keeps 0x00 but the idle value is not the hypothesis under test;
    - result: RDY seen → `ready = true`, `ready_ms/start_ms = ran`, return 0; ERR seen → `errors++`,

return -EIO; timeout → return -ETIMEDOUT. Always count `y2_xtal_tries++`.

  - `y2_rails_cycle(cs43130)` (new, no recursion):`cs43130_runtime_suspend(dev)` (masks ERR,

cache-only, PDN_XTAL/PLL set, RCO, rails off) → `msleep(Y2_CODEC_OFF_MS)` → `regulator_bulk_enable` → `cs43130_restore_cache` (both already exist; factor the first half of `cs43130_runtime_resume` into `y2_codec_up()` and call it from both). Returns the enable/restore error.
  - `y2_xtal_power_on(cs43130, select)` becomes the loop:

`for (i = 0; i < Y2_XTAL_TRIES; i++) { ret = y2_xtal_attempt(); if (!ret) break; if (i + 1 == Y2_XTAL_TRIES) break; dev_warn("XTAL start %d/%d failed (%d), cold start", …); if (y2_rails_cycle()) break; }`then, as today, if`select`: SYS_CLK_CTL_1 = EXT/22.5792, `mclk_int_src = EXT`, `pll_bypass = true`. The crystal is selected even after three failures (stock behaviour, nothing is lost). Return `ret` for logging; callers ignore it. Callers unchanged: probe (l.~1046, `y2_xtal_power_on(cs43130, true)`) and `cs43130_runtime_resume` (`y2_codec_up()` then `y2_xtal_power_on(true)`). `y2_xtal_start` keeps calling `y2_xtal_power_on(cs43130, false)` when `!y2_xtal_on`; the loop then also runs there.
  - `y2_codec_cycle` (l.163) = `y2_rails_cycle()` + `y2_xtal_power_on(cs43130, true)`;

`cycles++` and the existing warning. Still called from `y2_xtal_start` on a running ERR.
  - First stream, `y2_xtal_start` (l.178), the 8.24 gap: when neither ready nor assumed:
    - read INT_STATUS_1 once; if ERR → `errors++`, `y2_codec_cycle()`; if ready now, return;
    - otherwise wait as today, but poll for `RDY|ERR` (change the condition in `y2_xtal_wait`, l.145,

and return -EIO on ERR) with the remaining budget `Y2_XTAL_WAIT_MS - ran`;
    - on ERR or timeout, if `y2_xtal_stream_cycles < Y2_XTAL_STREAM_CYCLES` for this power-on →

`y2_xtal_stream_cycles++`, `y2_codec_cycle()`; if ready now, return;
    - finally `assumed = true`, `unconfirmed++`, `y2_xtal_report()` as today. Reset

`y2_xtal_stream_cycles` in `y2_xtal_attempt`. Bound per boot: at most `Y2_XTAL_TRIES` + `Y2_XTAL_STREAM_CYCLES` + running-ERR cycles, each ≤ 0.5 s + 3×0.1 s, so the worst first stream adds ≈ 2.5 s, never a loop.

  - Sysfs (`y2_hp_group`, l.~960): extend the `xtal` line with `tries=%u start_ms=%u

stream_cycles=%u full_power=%d quiet=%d`; add a write-only`cycle`attribute: under`clk_mutex`, refuse with -EBUSY if `clk_req`, else `y2_codec_cycle()`; this is the reporter's test loop.
  - Tests: extend `tests/test_codec_clock.py` (`CodecClock`) with: attempt order (bias, status

read, PWDN 0x00, poll, restore DAPM bits); three failed attempts produce exactly two rails cycles and still select EXT; ERR at the first stream cycles once and then assumes; `y2_xtal_full_power=0` writes 0xF0 instead of 0x00. Run: `PYTHONPATH=.:tests:tools/platform python3 -m unittest tests.test_codec_clock`.

Expected log on an affected unit with the fix: `XTAL start 1/3 failed (-5), cold start` once or twice, then `ready=1 tries=2`; on the owner's unit `tries=1 start_ms≈30`, unchanged behaviour. If `ready=0 tries=3` persists on the reporters' units with `full_power=1`, hypothesis 1 is refuted and the next candidates are the supply margin (VGP2 under load, GPIO rails' real voltages) rather than anything in the register sequence.

## Implementation (2026-10-23, uncommitted, not built into a release)

Fable's patch plan, implemented in `kernel/patches/0030-cs43130-system-pm.patch` and `tests/test_codec_clock.py`, with these changes to the plan:
  - `y2_xtal_stream_cycles` is reset in `cs43130_runtime_resume` (a real power-up), not in

`y2_xtal_attempt`: every cold start runs an attempt, so resetting it there would let one stream cycle forever. Worst case per stream: 3 + 3 starts, never a loop (tested).
  - The cycle trigger is `echo cycle > y2_hp/xtal` (next to the existing `boost`), not a new attribute.

It wakes the codec, refuses with -EBUSY while a stream holds the clock, and runs one cold start.
  - `y2_xtal_wait` now unmasks/re-masks XTAL_RDY itself, stops on RDY or ERR, and counts ERR.
  - After a start, PWDN's upper four bits go back to DAPM's cached value (`keep & 0xf0`).

Reporter test (one build): with nothing playing, `P=/sys/module/snd_soc_cs43130/parameters; X=$(ls /sys/bus/i2c/devices/*-0030/y2_hp/xtal)`, `echo 0 > $P/y2_xtal_full_power; for i in $(seq 10); do echo cycle > $X; cat $X; done`, then the same with `1`. Compare `tries=` / `ready=`. Also `y2_xtal_quiet_start` (candidate 3).

Checks: `tests.test_codec_clock` OK. Mutations caught: TRIES 1, STREAM_CYCLES 0, start with 0xF0. `make W=1 sound/soc/codecs/cs43130.o` has no warnings. Owed on the owner's player: `tries=1`, `start_ms` ≈ 30, and no click from the brief full-chip power-up (HP amp included) at boot or screen wake.

Published as Beta 8.25 (baseline-124, sequence 8901), with one change after the owner's listening test: the full-chip start (`PWDN_CTL=0`) made static in the headphones at screen wake (amplifier powered outside its DAPM sequence). The start now writes `0x10` (everything but the headphone amplifier); `y2_xtal_start_hp=1` restores the exact stock `0x00` for a reporter test. Report: `docs/validation/Y2-LINUX-1.0-BETA-8.25.md`.

Outcome (2026-10-23): both reporters confirmed 8.25 and closed #52 and #54. The #54 unit's report (5f909e65) shows `ready=1 ready_ms=30 tries=1 errors=0 cycles=0 cold_start=0 stream_cycles=0 full_power=1 start_hp=0` on its first 8.25 boot: the chip-powered start without the headphone amplifier (`PWDN_CTL=0x10`) brought up a crystal that flagged XTAL_ERR at every power-up on 8.22 and 8.24; no retry, rail cycle or first-stream cold start ran. #52's reporter confirmed in text ("couldn't break it", also after a restart and screen off) without a report. Conclusion: the CS43131 crystal oscillator needs the chip's analog/digital blocks powered to start reliably on some units; the clock-only power-up Y2Linux used since the first codec driver was the cause. Candidates 2 and 3 (`start_hp`, `quiet`) were not needed. Report: `docs/validation/Y2-LINUX-1.0-BETA-8.25.md`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
