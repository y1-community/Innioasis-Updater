---
title: "Stock suspend reverse-engineering ledger (POWER-FINAL-16) - Innioasis Updater"
description: "Stock suspend reverse-engineering ledger POWER-FINAL-16 <!-- knowledge-base-scope: retained-research -- Target: the Y2's own stock FM kernel, evidence-private/20260908-ra"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-stock-suspend-re-ledger.html"
---

# Stock suspend reverse-engineering ledger (POWER-FINAL-16) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Stock suspend reverse-engineering ledger (POWER-FINAL-16)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Stock suspend reverse-engineering ledger (POWER-FINAL-16)

Target: the Y2's own stock FM kernel, `evidence-private/20260908-ram-map/fm-decompressed.bin` (base 0xc0008000), wrapped with its 54,692 kallsyms into `out/rea/fm-kernel.elf` (SHA-256 `329466b3…b6d003`, generator script kept in the session scratchpad and reproducible: one PT_LOAD at 0xc0008000 plus `.symtab` from `fm-symbols.json`). Analysed with REA 6.4 / Ghidra 12.1.2 default auto-analysis. Everything below is **static analysis of the shipped stock image** (pseudocode is Ghidra output, not source). Nothing here was observed running. Evidence IDs are REA session records from 2026-10-12.

Goal of 16: stock sleep parity, ≈0.1 points/h (≈1 % per night; ≈1.3 mA average on the stock 1300 mAh model). 15 measured ≈1.6 points/h (voltage-derived), i.e. roughly 20 mA average. Maintenance wakes are not the cause: 2.6 s awake per 1800 s (0.14 % duty, archive 109, boot e2952adf rows). The floor while suspended is the gap.

## Findings``````````````````````````````````````````````````````````````````````

| # | Question | Stock behaviour (address, Evidence) | Y2 Linux 15 | Status |
| --- | --- | --- | --- | --- |
| F1 | Does our SPM arming differ from stock? | spm_go_to_sleep(cpu_pdn, infra_pdn, pwake) 0xc0033b50 (ev_168f2760…); spm_kick_pcm_to_run 0xc003308c (ev_e1d13388…): SPM_CLK_CON bit14 set iff !cpu_pdn, bit15 (CC_DISABLE_INFRA_PWR) set iff !infra_pdn, then ` | 0x60(LOCK_INFRA_DCM, SRCLKENA_MASK); PCM_MAS_PAUSE_MASK=~0; PWR_IO_EN=0x81.spm_set_wakeup_event(ev_facc0b82…): timer default 0xfff0ffff, WAKEUP_EVENT_MASK=~wakesrc, 0x900&4 | 0xe00`. |
| F2 | What does stock do at screen-off to the display? | mtkfb_early_suspend 0xc0515f18 (ev_1f0e761f…): backlight 0, DISP_PrepareSuspend, release syncs, DISP_PanelEnable(0) (→ lcm_suspend), DISP_PowerEnable(0), DISP_PauseVsync(1), disp_path_clock_off. spm_mtcmos_ctrl_disp 0xc00350a8 (ev_59e40d65…) is called only from the clock manager (0xc003fa2c/0xc003fa4c, ev_c9c1613e…): off = INFRA TOPAXI_PROT_EN (0x10001220) bit1, wait PROT_STA1 (0x10001228) bit1, DIS_PWR_CON (0x1000623c) `&~0x1d | 0xf12`, wait PWR_STATUS/PWR_STATUS_S bit3 clear; on = reverse. | Only the MFG (GPU) domain is a genpd (spm.c). DIS is never powered off; 15's sleep rows show power=0x314c (bit3 DIS on while asleep). MMPLL/VENCPLL on at entry match this. |
| F3 | Does stock switch PLLs off explicitly at suspend? | clkmgr_early_suspend 0xc003f494 (ev_7ecdab45…) only logs CLK_CFG_0..3. PLL off follows clock reference counts (last user off). | PLLs on at entry (golden rows). | Answered: PLL-off is a consequence of releasing their users (DIS/MM, MSDC, audio), not a separate step. |
| F4 | DRAM at screen-off | mt_emifreq_early_suspend 0xc0038ef4 (ev_a810f583…): unless disabled, mt_h2l_dvfs_mempll() (DRAM PLL high → low). | No EMI/MEMPLL DVFS in Linux. | Gap G4, needs decoding of mt_h2l_dvfs_mempll (risky: DRAM timing). |
| F5 | PMIC at screen-off | pmic_early_suspend 0xc04b3a84 (ev_45809a69…): VREF18_ENB=0, CLKSQ_EN_AUX=1, AUD26M_DIV4 PDN=0, AUXADC SDM HW mode/clock settings. Separate from pmic_mt6323_suspend 0xc04b3dd4. | Not adopted (13 decision: would change ADC behaviour). | Known, re-evaluate with G5 (PMIC golden). |
| F6 | CONNSYS when Wi-Fi/BT off | mtk_wcn_consys_hw_pwr_off 0xc0564cd4 (ev_1aa5ca22…): consys_hw_reg_ctrl(0) + GPIO off. | PWR_STATUS bit1 (CONN) = 0 in 15 rows. | Answered: CONN already off. |
| F7 | Stock suspend hook inventory | Regex procedure search (ev_496e0cfe…): clkmgr, emifreq, mtkfb/disp, AudDrv (AudDrv_Suspend_Clk_Off), msdc, musb, mt_i2c, uart, gpio, kpd, thermal (mtktscpu_thermal_clock_off), battery, pmic, wcn. | — | Inventory only; each still to compare. |

| F8 | When does stock compare its golden table? | `slp_suspend_ops_prepare` 0xc0035ee4 calls `mt_power_gs_dump_suspend` only if a debug flag is set (`ev_44f0433f…`). | — | Answered: the golden table is MediaTek's reference checklist, not a recorded Y2 state. Rows are reached by stock mechanisms, never forced blindly. |

| F9 | Boot-time DCM | `mt_dcm_init` → `dcm_enable(0x1ff)` 0xc003c154 (assembly `ev_9054224d…`): CPU (0x10208000 bit12, MCUSYS+0x5c bit9), TOPCKGEN, IFR (INFRACFG 0x08/0x10/0x14/0x50/0x54/0x58, DRAMC+0x1dc bits 24/25), PER (PERICFG 0x50/0x54/0x58 + MSDC/USB/I2C local bits), SMI/DIS (MMSYS 0x120..0x134, LARB0+0x14, SMI+0x300) only while each domain is on. | Only SLIDLE bus DCM. | Implemented in 16 (`dcm-policy.h`): 10 golden rows. PERI DCMDBC follows stock code (0x80), not the checklist (0xf0). Peripheral-local bits not adopted. |

| F10 | Clock tables | Mux table `0xc09b17c8` (13 muxes, PDN bits, `clkmux_disable_op` sets PDN); PLL table `0xc09b1678` (6 PLLs; `mt_plls_init` sets MMPLL/VENCPLL refcount 1 for the display); `sdm_pll_disable_op` 0xc003f4dc / `sdm_pll_enable_op` 0xc0041c88 (assembly). | PLLs are read-only rate clocks in Y2 Linux; nothing ever switched one off. | Implemented in 16 as golden sleep entry (`golden-apply-policy.h`, `spm.golden_apply` bitmask, save/restore). MAINPLL/ARMPLL/AXI mux never touched. INFRA PMIC_WRAP (bit 23) kept on (SPM sleep PMIC access). |

| F11 | MD-side peripheral requests | Golden `PERI_PDN0_MD1_STA` = all gated; Y2 reads 0. No AP write found in stock (`gate_md1` writes 0xffffffff to an unresolved ccci block +0x14). | — | Answered on hardware 2026-10-12 (owner-authorised live test, 16 boot `0b0e8a77`, probe module `out/power-final-16-build/md1probe/`): layout MD1_SET 0x20 / MD1_CLR 0x28 / MD1_STA 0x30 confirmed (bit 0: 0→1→0); all 26 bits SET → STA 0x03ffffff for 200 ms with AP PDN0_STA unchanged (0x02ecf3fd), USB/SSH, Wi-Fi and charger alive; restored to 0. MD_MASK 0x38 = 3. 17: gate all MD1 requests at boot (switch). |

| F14 | Is the AP-side SPM setup the INFRA blocker? (17, 2026-10-13) | `spm_module_init` 0xc00328ec (`ev_e0004f2b…`): POWERON_CONFIG 0xb160001, POWER_ON_VAL0/1 0/0x15820, CLK_CON 0x200, PCM_SRC_REQ (0xb04) 2, wake mask ~0, ISR mask 0xf0c, SW_INT clear 0xf; `spm_go_to_normal` 0xc0032848 (`ev_d00fe860…`); `spm_go_to_sleep` 0xc0033b50 (`ev_168f2760…`): CLK_CON\|=SYSSETTLE_SEL, CLK_SETTLE 99, AP_STANBY_CON 0x180010, WFI_SEL 1, APMCU_PWRCTL 0; `slp_suspend_ops_enter` (`ev_1e5eb1d1…`) only calls it. `spm_is_md_sleep` 0xc0034250 (`ev_cdfa5bdd…`) = R13 bit 4 clear. | Write for write identical (`spm-suspend-policy.h`, probe). 17's R13 at wake 0xe8060000: MD (bit 4) and CONN (bit 1) SRCCLKENI clear; MD1 requests gated. | Answered: the SoC side matches stock completely; `last_lost=0x0` (PERICFG PDN0 keeps 0x2fcffff, reset value 0) proves INFRA stays powered. The remaining differences are PMIC-side (F15, F16). |

| F15 | PMIC golden fields (17) | All 15 differing rows mapped to stock `upmu_set_*` fields by decoding each setter's register/shift/mask from the image (`pmicmap.py`, session scratchpad): 0x102.0 `rg_clksq_en_aud` (stock 0, ours 1); 0x108 `drv_2m_ck_pdn`/`rtc_mclk_pdn`/`efuse_ck_pdn` (stock gated) and `accdet_ck_pdn` (stock 0 = clock running, ours 1 = gated: Linux already saves more here); 0x10e.5 `auxadc_ctl_ck_pdn`; 0x120.3/.7 `auxadc_sdm_sel_hw_mode`/`auxadc_sdm_ck_hw_mode` (bits 0/4/5 `srclken_en`, `srclken_hw_mode`, `osc_hw_mode` already stock); 0x04e.5/.7 `strup_auxadc_rstb_sw/sel`; 0x21c/0x310 `vproc/vpa_sfchg_fen/ren`; 0x230.8 `vproc_vsleep_en`, 0x256.8 `vsys_vsleep_en`; 0x508.14 `rg_vemc_3v3_en` (stock off); 0x70c.4 `rg_adacck_en` (stock 0, ours 1), .9 `rg_depop_vcm_en`; 0x776/0x778.15 `rg_vref18_enb(_md)` (stock 1). 0x216 has no named setter. | 16/17 capture these read-only every sleep (`pmic_golden`). | Mapped; next candidate's work list. |

| F16 | Who owns `rg_clksq_en_aud` in stock? | Callers (`ev_7bc2cf74…`): `AudDrv_probe`, `AudDrv_ANA_Clk_On/Off` 0xc0548de4/0xc0548d68 (refcount; 0 on the last analog-audio user, `ev_bf1811e9…`), `AudDrv_Suspend_Clk_On/Off` 0xc0548e40/0xc0548f1c (suspend: AFE `Afe_Set_Reg(0,0x4044,0x4044)`, `disable_clock(0xe2/0xe6)`, then `clksq_en_aud=0`, `ev_b8ec0172…`). | Never written by Linux (the PMIC allow-list for 0x102 is bits 6/11/15), so the bootloader's 1 stays all the time. | Gap: the PMIC's audio 26 MHz clock-square request is forced on in sleep. First candidate for the remaining always-on request. |

| F17 | INFRA bit 23 (PMIC_WRAP clock) in stock (18, 2026-10-13) | All 14 stock `mt6582_power_gs_*_data` checklists decoded from the image: INFRA_PDN_STA bit 23 is gated (1) in suspend (0x80bfe6), video_playback (0x81b0c4) and 3g_paging, ungated in idle/dpidle (0xb1e6), audio playback, connsys, 2G/TDD. A bit gated in an awake scenario means the AP's PMIC access does not depend on it. No stock `enable_clock/disable_clock` call passes its clock ID (32+23 = 55; scan of every BL to both, IDs 33/38/40/44 found), so stock gates it indirectly (clock-manager group, hardware or init state), not by a driver constant. `pwrap_suspend` 0xc039a6e8 only calls an optional hook, NULL in the image (`ev_b18e8c5b…`, struct 0xc09d092c+0x44). | Y2 deliberately keeps bit 23 on (`golden-apply-policy.h`: "SPM sleep firmware drives VPROC/LP_SEL through the wrapper"); it is the only INFRA gate still different at entry (ours 0xbfe6 vs 0x80bfe6). | Live test 2026-10-13 (owner-authorised, 18 boot `69ef8c26`, probe `out/power-final-18-build/infraprobe/`): one command with local IRQs off: INFRA_PDN_STA `0000a0a0` → SET bit 23 → `0080a0a0`; a WACS2 read of PMIC 0x100 (`kernel/diagnostic/pwrap.h`) then returned -EIO with the wrapper state register reading 0 (the whole wrapper register block is clock-gated for the AP; no bus hang); CLR bit 23 → `0000a0a0`, the same read returned CID 0x2023 again and the kernel's own PMIC driver kept working. Bit 23 is the AP's entire PMIC_WRAP clock. Stock's suspend checklist has it gated, so stock's AP does not touch the PMIC after that point and the identical PCM sleeps with it gated. 19 option: gate it as the very last write before the PCM kick (after every PMIC step and capture), ungate as the very first write after the CPU returns (before every PMIC/VPROC restore), behind a switch. |

| F12 | PMIC golden | `mt6323_power_gs_suspend_data` 0xc0757cd0, 44 rows. | Never compared at entry. | 16 captures it read-only at every sleep entry (`pwrap.pmic_golden`). |

| F13 | Fuel gauge | `fgauge_get_Q_max` 0x514 (1300 mAh), `fgauge_get_profile(25)` 0xc09d117c (95 rows, 4175 → 3400 mV), `r_profile` 0xc09d1d5c (191–326 mΩ). | Estimated 9-point curve. | Implemented in 16 (battery-profile.json, OAM charging correction, mAh estimate). |

## Gaps to close in 16 (ranked by expected sleep-current effect)
  - G1 DIS power domain + MM clocks off at screen-off (F2): add a DIS genpd with the exact stock sequence,

attach the display pipeline to it so DRM's disable powers it down, which also releases MMPLL/VENCPLL. Also the awake-dark power win the 15 handoff suspected ("Skipping unprepare" message).
  - G2 INFRA power-down never happens (`last_lost=0x0`): F1 rules out the SPM kick. Next: find what keeps

INFRA requested (SRCLKENA/26 MHz requesters, PCM `R7`/`SPM_PCM_SRC_REQ`, bus masters left on: DIS, MSDC, USB). Expected to follow partly from G1/G3.
  - G3 Golden-table rows: INFRA/PERI clock gates, PERI MD1, bus/peri DCM, CLK_CFG mux power-down, MSDCPLL

(eMMC/SD clock release at suspend), audio clocks (`AudDrv_Suspend_Clk_Off`), thermal clock off.
  - G4 DRAM low-power (F4): `mt_h2l_dvfs_mempll` and DRAMC+0x1dc golden row. Last, highest risk.
  - G5 PMIC golden (44 rows) and VEMC3V3/VGP2/panel deep standby/BAT_L interrupt (13 list).

## Non-power defects carried into 16
  - Defect B (USB TX dead after every wake): DMA-interrupt unmask (MUSB+0x200 bits 24..31) theory; first

read the full 32-bit value plus DMA channel registers, then re-arm in `y2_musb_enable`/`after_restore`.
  - Defect C (new, archive 109): with VBUS present but the host unconfigured/off (`udc=default`), sleep is

refused every 5 min (`charger_or_usb_active`) while the charger is `INHIBITED`/"Not charging": 75 % → 32 % in 6.3 h on a powered-off PC. Sleep policy must allow suspend when nothing charges and no host is configured.
  - Python 3.15 `/dev/kmsg` flush EINVAL (S03/S05), power-journal keeps only ≈4.5 h.

## Remaining-gap audit after 26 (2026-10-14, archive `20261014/124`)

Trigger: 26 night 10.3 h, 21/21 clean, whole-night ≈8.3 mA (least squares, first 2 h skipped). Owner asked whether this is stock parity. Static analysis of the stock image (REA/Ghidra 12.1.2 session 2026-10-14, plus literal/`movw`+`movt` scans of `fm-decompressed.bin`) and read-only live reads on 26 boot `8943a99a` (`live-reads/`, `golden-live.txt` in the archive). Nothing was written to the device.````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

| # | Question | Stock (address, Evidence) | Y2 26 | Status |
| --- | --- | --- | --- | --- |
| F18 | Who writes AP_PLL_CON1/CON2, MAINPLL_CON0 and CLK_CFG_0 (the SoC rows still different at entry)? | No code writes AP_PLL_CON1/2: the only 0xf0209004/8 references are the debug prints in slp_suspend_ops_enter (ev_2561cc4d…) and the golden tables; vendor clksq1_sw2hw() starts with return;. CLK_CFG_0 has no direct writer; the mux table 0xc09b17c8 (13 muxes) only lists MUX_MM there. | Same preloader/LK, same values. | Answered: checklist-only rows. Stock sleeps with the bootloader values too; not a gap. Remaining mux rows are the UART mux (kept on deliberately) and TOPCKGEN+4 bus DCM (idle-only). |
| F19 | Stock slp_suspend_ops_enter arguments | Flag block 0xc09b1084 = 01 01 01 00: cpu_pdn 1, infra_pdn 1, register dump 1 (stock prints AP_PLL/TOPCKGEN/INFRA/PERI/SPM registers as [SLP] … at every suspend). | SPM_CPU_SHUTDOWN_INFRA_PDN. | Answered: identical. No stock [SLP] log is archived; one would give stock's real sleep values. |
| F20 | VGP2 (CS43131 VA/VP/VCP 1.8 V) | Only owner is the CS43131 driver: hwPowerOn(6) in probe/cs43131_on/cs43131_late_resume, hwPowerDown(6,"CS_DAC") in cs43131_power_down_hw 0xc054b620 (ev_7b6992d2…), called from cs43131_early_suspend when not playing (ev_18a5a6f6…) and cs43131_off; LDO id 6 = VGP2 per pmic_ldo_enable (ev_d08d64ac…). Every hwPowerOn/Down caller scanned: no other VGP2 user. | DTS regulator-always-on ("shared ownership not qualified"); VGP2 stays on in sleep while the GPIO-switched VD/VL rails are off. | Gap A (confirmed, single owner). Stock order: EINT16 mask, GPIO15/18/20 low, then VGP2 off. Effect unmeasured (LDO quiescent + codec analog leakage). |
| F21 | VSYS buck sleep | Vendor PMIC_INIT (pmic_mt6323.c 3417–3424) and the image's init table: QI_VSYS_VSLEEP 2, VSYS_VOSEL_CTRL 1, VSYS_SFCHG_*, VSYS_TRANSTD 3, VSYS_VOSEL_TRANS_EN 1, VSYS_VSLEEP_EN 1; golden 0x256[8]=1. | Live: 0x238=0x0003 (RG_VSYS_SLP already 3), 0x23c=0, 0x242=0x0505, 0x256=0x0001, VOSEL=VOSEL_SLEEP=0x40 (2.2 V): VSYS stays in software mode, never enters its sleep mode. | Gap B. Same pattern as VPROC (13): apply inside the SPM enter, or as stock at init. |
| F22 | Panel suspend | GC9503V lcm_suspend 0xc04a24f4: 39-entry table 0xc09ff464 (72-byte rows): page f0 55 aa 52 08 00, c1 3f, 6c 60, b1 00, fa 7f 00 00 00, 6c 50, 28, 10, then 24 analog writes (c2 ce, c3 cd, c6 fc, c5 03, cd 64, c4 ff, c9 cd, f6 5a 87, fd aa aa 0a, fe 6a 0a, 78 2a aa, 92 17 08, 77 aa 2a, 76 aa aa, 84 00, 78 2b ba, 89 73, 88 3a, 85 b0, 76 eb aa, 94 80, 87 04 07 30, 93 27, af 02), then reset high, 50 ms. | gc9503v_unprepare: 28, 10, 120 ms, reset asserted (low). | Gap C. The vendor low-power register block is never sent, and reset is held in the opposite state. Effect unknown, possibly the largest single item (panel supply stays on in both). |
| F23 | VEMC3V3 (eMMC) | msdc_emmc_power(host, 0) 0xc04f265c (ev_2c81c7b5…, indirect caller): waits for DAT0 not busy, msdc_set_smt, msdc_ldo_power(0, 4 /*VEMC*/, 3300 mV). | On through sleep (overlay 0029 keeps the eMMC in TRAN without re-init). | Gap D (known, confirmed in code). Needs an eMMC suspend model with power-off + re-init (or sleep/awake). Storage risk. |
| F24 | Radios, SD, other LDOs at entry | Stock consys and msdc drop their LDOs; camera/SIM/VIBR LDOs unused. | PMIC capture at entry: VCN18/28/33, VMC, VMCH off; only 0x04e, 0x108[9], 0x120, 0x256, 0x310, 0x508, 0x70c[9] differ. | Answered: no gap apart from F21/F23 (0x04e/0x120 AUXADC modes and 0x310 VPA are negligible). |
| F25 | DRAM at suspend | mt_emifreq_early_suspend is screen-off DVFS; self-refresh in suspend is the PCM firmware's (same image). | — | Answered: no sleep-current effect. G4 is an awake-dark item only. |
| F26 | GPIO | mt_gpio_suspend is empty; GPIO sleep state = preloader defaults + driver changes. | Y2 pinctrl changes only I2C 84–87, MSDC1 124–129, I2S 43/44/46, LCM reset 112, EINT 25/55. No /dev/mem; a full register dump needs a probe (taints). | Low priority. |
| F27 | Hardware fuel gauge | fgauge_initialization/read_current/read_columb all return 0 (stubs): no coulomb counter on this board. | Voltage estimate only. | Measurement limit: stock's "≈1 % per night" is a smoothed voltage percentage, not a current. |

Measurement note (26 night). The filtered voltage slope falls through the night (h0–3 −10.6, h3–6 −4.3, h6–9 −1.2 mV/h; ±6 mV per-sample jitter), i.e. post-charge relaxation inflates the early hours. At ≈1.65 mAh/mV (stock curve near 3.93 V) the late-night drain is between ≈2 and ≈8 mA depending on the window. A fair stock comparison needs a start ≥4 h after charging and a ≥12 h run, or an external meter.

Ranked candidates for the next image: C panel suspend sequence (stock table + reset high), A VGP2 off when the DAC is idle (stock order), B VSYS sleep mode (stock init fields, inside the SPM enter like VPROC), D VEMC3V3 off (separate storage milestone). Each behind its own switch, one night per change if possible.

## Battery percentage: stock UI SOC vs Y2 (2026-10-14, 27 boot `5919b4fe`)

Owner report: on the charger the Y2 shows 100 %, after a restart about 80 %. Wanted: 100 % when really full, then 99, 98, 97 …``````````````````````````````````````````````````````````````

| # | Question | Stock (address, Evidence) | Y2 27 | Status |
| --- | --- | --- | --- | --- |
| F28 | Displayed vs estimated SOC | mt_battery_update_status 0xc039ff3c (ev_f1c32855…): BMT_status.UI_SOC (+0x54) is separate from SOC (+0x50). Charging, not full: UI capped at 99. Full: UI +1 per thread tick to 100, then battery_meter_reset 0xc039d14c (ev_47e859a0…) re-anchors the gauge at full (reset_parameter_dod_full(UI), Qmax aging update). Discharging: UI follows SOC only downward, −1 per 7 ticks (counter +0x178 == 6), never below 1. Every update set_rtc_spare_fg_value(UI). | One value: voltage curve, rate-limited (60 s/%), forced to 100 while the kernel says Full. | Gap: no separate display value, no full re-anchor. |
| F29 | Across a restart | dod_init 0xc039be10 (ev_07f4108c…): get_rtc_spare_fg_value (MT6323 RTC spare, ev_f83a7385…, written by set_rtc_spare_fg_value ≤100, ev_e0428c86…) is reused when it differs from the boot voltage SOC by < 40 points (charger/low-SOC cases aside). | Nothing persisted; first sample decides. | Gap (main cause of "≈80 % after restart"). |
| F30 | Boot voltage | oam_init 0xc039c114 (ev_5d947fb9…): command 9 = read_hw_ocv → get_hw_ocv 0xc04cae90 (ev_944044ab…): PMIC 0x724[14:0] (rg_adc_out_wakeup_pchr, latched at power-on before load) × 7200/32768 + 8 mV; if on a charger and far from the 5-s sample, the 5-s sample wins. | First sample under boot load. Live 27: 0x724 = 0xc813 → 4062 mV OCV, first sample 4002 mV → 87 % (OCV → ≈92 %). | Gap: boot sag ≈60–120 mV ≈ 5–15 points. |
| F31 | Full / top-off | BAT_ConstantCurrentModeAction/BAT_TopOffModeAction 0xc03a2208 (ev_f1442296…), batt_cust_data 0xc09d2d68 = {1, 4050, 150, …}: top-off above 4050 mV with hardware CV (stock CV request 4.2 V), Full after 6 × 10 s at ≤150 mA charging current or 10800 s; BAT_BatteryFullAction (ev_1e37b9de…); recharge below 4110 mV. | Stops at the first 4.175 V loaded sample (no taper; 4.2 V treated as fault since POWER-02), Full when the hold rests ≥4.07 V, recharge only below 4.00 V. Rests ≈4.09 V = 95 % on the stock curve; on the charger the Y2 runs from the battery down to 4.00 V (87 %) while showing 100 (live: Full, 4.04–4.05 V, 100 %). | Gap: never really full; 100 shown across an 87–95 % band. Changing CV/termination is a charger-safety milestone (valid charge-current measurement needed for the 150 mA taper). |
| F32 | Thread cadence | battery_kthread_hrtimer_init (ev_95907b4b…) 1 s timer; BAT thread period 10 s (top-off/CC add 10 s per call). | Platform sampling. | Display step ≈ −1 % per 70 s at most. |
| F33 | Current sense | fgauge_read_current/columb stubs (F27); stock OAM integrates a model current (OCV(DOD) − V)/R (oam_run 0xc039c37c, ev_eae29d1b…). | Same voltage model family (OAM while charging). | No coulomb counter on either. |

## Awake idle (C2 SLIDLE / C3 DORMANT) vs stock (2026-10-14, 29 boot `cac3e209`)

Live: only WFI is ever used awake; cpufreq residency is fine (≈89 % at 598 MHz). SLIDLE 0 entries (261 884 clock rejections: PERI bit 11 AP_DMA + bit 20 BTIF), DORMANT 0 entries in 305 100 attempts (`-EBUSY` at `domains`: SPM power bit 1 CONN on), with CPU0-only topology reached. No archive this session ever shows a DORMANT entry. The earlier CPU-idle qualification did reach 84 % SLIDLE / 65 % DORMANT residency, but only with screen off and radios off. Bluetooth is normally enabled on the owner's Y2 (rfkill bluetooth unblocked), so deep idle never happens in use.````````````````````````````````````````````````````````

| # | Question | Stock (address, Evidence) | Y2 | Status |
| --- | --- | --- | --- | --- |
| F34 | Stock deep-idle admission | dpidle_handler 0xc003cff0 (ev_838c0fdd…): enabled + early-suspend (screen off) + clkmgr_idle_can_enter 0xc0042fcc (ev_eaac1f04…, 10 group masks, MSDC via msdc_clk_status) + local-timer horizon ≥ 0x6590; then spm_go_to_dpidle. No power-domain check (CONN may be on). Masks (struct 0xc09b1548+0x10, vendor group order): PERI 0x02fe87fd (BTIF yes, AP_DMA no), INFRA 0xa080 (audio clock not required off), TOPCK 0, DISP0 0x7ffff, DISP1 0xf, IMAGE 0x3e1, MFG 1, AUDIO group 0, VDEC 1/1. | DORMANT also requires: CONN domain off, PERI AP_DMA + MSDC0–2 off (0x7800), INFRA audio (bit 5) off. | Ours is stricter in three places. |
| F35 | Stock slow idle | slidle_handler 0xc003d0e8 (ev_b49cd842…): mask PERI 0xf00800 (AP_DMA, BTIF, I2C0–2), bus DCM around WFI. | Same blockers (APDMA/BTIF/MSDC). | Equivalent. |
| F36 | Audio during deep idle | spm_dpidle_before_wfi (ev_f4060198…): bus DCM on, CLK_CFG_3 &= 0xf8ffffff (AUDINTBUS to 26 MHz), GPT3 deadline; spm_dpidle_after_wfi (ev_ed01d6f8…) restores CLK_CFG_3. Stock enters deep idle during screen-off playback. | Same CLK_CFG_3 handling, but INFRA audio bit 5 blocks entry, so never during playback. | Gap: screen-off playback never deep-idles. |
| F37 | Bluetooth idle | STP power saving: wmt_lib_ps_* 0xc03fca38–, stp_psm_* 0xc0401050–, BTIF deep-idle hooks btif_enter_dpidle 0xc03c122c / btif_exit_dpidle 0xc03c11ec, mtk_wcn_stp_dpidle_ctrl 0xc040814c, btif_clock_ctrl (ev_7a755ece…, BTIF + its DMA channels). When the BT link idles, consys sleeps and BTIF gates its clocks. | kernel/platform/connectivity/btif.c enables BTIF + DMA clocks at start and only disables at shutdown; no PSM. | Gap: enabled-but-idle Bluetooth blocks every deep idle. Implementing PSM is a protocol change. |
| F38 | Awake frequency | — | schedutil, CPU0-only when quiet; 598 MHz most of the time. | No gap. |

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
