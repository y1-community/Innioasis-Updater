---
title: "POWER-FINAL-06 bring-up candidate — INFRASYS/DDRPHY power-down in full suspend - Innioasis Updater"
description: "POWER-FINAL-06 bring-up candidate — INFRASYS/DDRPHY power-down in full suspend Status: PRODUCTION-CODE-READY is not claimed. This is a bring-up candidate. Source + offlin"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-06-bringup.html"
---

# POWER-FINAL-06 bring-up candidate — INFRASYS/DDRPHY power-down in full suspend - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-06 bring-up candidate — INFRASYS/DDRPHY power-down in full suspend

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-06 bring-up candidate — INFRASYS/DDRPHY power-down in full suspend

Status: PRODUCTION-CODE-READY is not claimed. This is a bring-up candidate. Source + offline qualification only. Physical status: NOT_RUN (owner flashes; the agent never flashes). Readiness: MORE_WORK_REQUIRED.

Identity: Linux `c1ef37a6f6338b3abe7fcb4f2aa505b6fb861075` (branch `codex/platform-v1-power-final-06`, from 05 `280b612`), Reborn `97ff8c357bab12319087740d7c97b5051e6588f5` (unchanged), kernel `6.18.0-y2linux-platform-v1-power-final-06`, root `2025.02.18-platform-v1.36`, release `1.0.0-platform-v1-power-final-candidate.6`, build `Y2LINUX-PLATFORM-V1-POWER-FINAL-06`. BOOTIMG `64a916282b383116fb5d323fe60f5fbf638ae966291ce20827617fd23147869f`, Y2ROOT `e1c0bcd3dc200c3fa2179d65ab18ba1358c46fc4b6fe0b2740f7f44f6c23e4be`.

## Why this image exists

05 measured about 2.1 battery points per hour while 99.5 % suspended (voltage-derived, indicative only). The owner recalls about 1 percent per night on the stock firmware. The 05 report claimed Y2Linux ran the 480-word `pcm_dpidle` for full suspend; that was wrong. It already runs the vendor 597-word `pcm_suspend` (identical words, SHA-256 `0ee71194…6ab94`) and differs from the stock kernel in exactly one argument: `infra_pdn` (stock default 1, read from the retained FM kernel at `0xc09b1084`). With `infra_pdn=1` the PCM also removes INFRASYS and DDRPHY power.

## What changed (relative to 05)
  - INFRA power-down (`kernel/platform/infra-pdn*.{h,c}`, `spm-suspend-policy.h`, `spm.c`): the arm function takes `infra_pdn`

and verifies `SPM_CLK_CON` reads back accordingly. PERICFG (RST0/1, PDN0 via SET/CLR/STA, DCM, CKSEL, AXI/AHB limiters, USB wake, UART clock source) is saved before the PCM is armed and written back immediately after `cpu_suspend()` returns, only for registers that changed, then verified. INFRACFG TOPAXI is read-only. Source: MT6582 manual 2.3.2 (INFRASYS MTCMOS domain = INFRACFG + PERICFG), stock `spm_go_to_sleep`/`spm_kick_pcm_to_run`/`mtk_uart_restore` disassembly.
  - Safety: a failed or unverifiable restore pins the boot to the proven retained mode (`-EIO`, SPM broken, product guard

quarantines); a boot whose predecessor ended on the new `INFRA_PDN_ENTRY` journal stage starts retained; the 30 s RGU backstop and the PCM watchdog wake are unchanged; `/sys/firmware/y2_infra/mode` is the explicit owner switch.
  - UART:`8250_mtk` re-arms `UART_SLEEP_EN` after system resume (power-down resets the UART; the next sleep's UART-ack handshake needs it).
  - USB (Defect 1): MUSB L1INTM keeps only TX/RX/USBCOM/DMA; an unowned PHY level interrupt (the overnight `l1=800/f00`

POWERDWN case) is masked at its source instead of storming into the terminal guard.
  - USB/Wi-Fi (Defect 2): a terminal USB stop parks the controller instead of unregistering `musb-hdrc`. Unregistering freed the gadget

device that `usb0` references as `dev.parent`; the next netlink query crashed in `strlen(NULL)` (the Oops stack contains `"usb0"`).
  - Docs: 05 report corrected; `docs/architecture/deep-suspend.md` added.

Not changed: PCM words, wake mask, PMIC rails and whitelist, eMMC/SD handling, Reborn, runtime idle C1/C2/C3.

## Offline qualification (receipts in the package's `validation/`)
  - Image built from `c1ef37a`; the locked-container production suite then passed in full (581 cases, exit 0) on `a9f9b0e`, which differs from the

build commit only in `tests/test_cpu_final.py` (a USB restore fixture needed the new L1 helper; the first run at `c1ef37a` stopped there, and `tests.sh` aborts at the first failing module, so the suite was re-run complete) and a dev-tool pin. 25 packaging-host and 27 native splash cases PASS.
  - New regression tests, verified to fail on the old source where applicable: `tests/test_usb_l1.py` (3), `tests/test_infra_pdn.py` (5), extended

`test_power_policy` (INFRA arm + CLK_CON readback refusal), `test_suspend_cpu_pm` (save → arm → restore ordering, abort and failure paths).
  - Preserving package, fallback pair (sealed 05), manifest/rootfs/privacy checks PASS; ELF closure 384 files / 1411 edges, no build RPATHs; installed-ARM contracts PASS.
  - The new strings (`Y2INFRA`, `INFRA_PDN_ENTRY`, `previous_boot_died_in_infra_pdn`, `Y2USB masked unowned L1`, `suspend_pcm_origin`) are present in the built kernel image.
  - Reborn is unchanged at `97ff8c3`; its fmt/Clippy/test/QEMU receipts from 05 are not repeated (see `validation/reborn-NOT-RERUN.md`).
  - Physical behaviour: NOT_RUN.

## What to check after the owner flashes (agent, read-only first)
  - Identity/taint/boot id; `dmesg`: `Y2INFRA: mode=powerdown fallback=0 reason=none`.
  - `cat /sys/firmware/y2_infra/state` and `diff` before any sleep: `saves=0`, `ready=1`.
  - One normal automatic suspend cycle (unplug, dark, paused). Success means: same boot, `Y2SPM: suspend result=0`,

`Y2INFRA: restore result=0 lost=... pdn0 ...->0x0`, `restore_failures=0`, `fallback=0`, journal COMPLETE. * `pdn0_woke=0x0` with `last_lost` containing the PDN0 bit proves INFRASYS really lost power; the drain comparison is meaningful. * `last_lost=0` after a long sleep means INFRA did not power down; investigate `CC_DISABLE_INFRA_PWR` and `PWR_STATUS` bit 6 (0x40).
  - Decision tree on failure: backstop reset (about 30 s before SPM) or device that never wakes (hold Power ≥ 10 s). Next boot reports

`reason=previous_boot_died_in_infra_pdn` or product guard `pending:true`; archive with `capture-return.py` first, then `echo retained > /sys/firmware/y2_infra/mode` to compare with the 05 behaviour.
  - Then: repeated cycles and maintenance wakes (600 s), USB cable wake and re-enumeration, Wi-Fi/BT restore, `ip link` clean,

eMMC/SD health, and an overnight drain compared with the 05 baseline (about 2.1 points/h, voltage-derived).

## Known limits

No current sensor and no external measurement; DRAM/26 MHz/INFRA power state are unobservable during sleep. The first power-down is the experiment: PERICFG is the documented lost state, but peripheral register state is deliberately not read or restored by the platform (vendor parity); if a driver fails to re-initialise, the first hardware cycle will show which one.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
