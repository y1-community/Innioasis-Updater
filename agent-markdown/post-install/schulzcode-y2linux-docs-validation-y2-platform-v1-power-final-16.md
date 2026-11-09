---
title: "POWER-FINAL-16 — stock sleep parity from the Y2's own stock kernel (REA) - Innioasis Updater"
description: "POWER-FINAL-16 — stock sleep parity from the Y2's own stock kernel REA Status: INSTALLED, OVERNIGHT SLEEP CLEAN, ≈8.6 mA ASLEEP; tagged baseline-16 2026-10-13. Package ou"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-power-final-16.html"
---

# POWER-FINAL-16 — stock sleep parity from the Y2's own stock kernel (REA) - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# POWER-FINAL-16 — stock sleep parity from the Y2's own stock kernel (REA)

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# POWER-FINAL-16 — stock sleep parity from the Y2's own stock kernel (REA)

Status: INSTALLED, OVERNIGHT SLEEP CLEAN, ≈8.6 mA ASLEEP; tagged `baseline-16` (2026-10-13). Package `out/y2linux-platform-v1-power-final-candidate-16/` (fallback = 15), receipts `out/deep-sleep-final/build16-receipts/`. Identity: build `Y2LINUX-PLATFORM-V1-POWER-FINAL-16`, kernel `6.18.56-y2linux-platform-v1-power-final-16`, root `2026.08-platform-v1.46`, release `1.0.0-platform-v1-power-final-candidate.16`; Linux `a4e9c3b` on `main` (later commits: the two follow-ups below, tests and docs). Reborn unchanged (`f68e088`). BOOTIMG `2f1cd1c0091e2015afa2af6ffbd2f191f58090d3cbdc3b52f58a71ef5d6edebf`, Y2ROOT `bd4a12a07b39f21c9313d82069014891e1e1707ffee9eb532e04cece69a43d9f`.

Goal set by the owner: fix what was broken on 15 and reach the best possible deep sleep, stock parity of about 0.1 percentage points per hour (≈1 % per night, ≈1.3 mA on the stock 1300 mAh model). Every stock behaviour below was read from the Y2's own stock kernel with REA/Ghidra; the evidence and addresses are in the [stock suspend ledger](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fstock-suspend-re-ledger.md). Scope audit: "POWER-FINAL-16 stock sleep-parity scope audit" in the [roadmap gap audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

## What 16 changes````````````````

| Area | Change | Switch |
| --- | --- | --- |
| Defect B (USB dead after every wake, 13–15) | The MUSB DMA completion unmask (MAC+0x200) is re-armed whenever the interrupt gate reopens (reconnect, restore); full 32-bit diagnostics (dma_unmask_* in the y2-usb status). | — |
| Defect C (no sleep, no charge on a powered-off PC) | A standard PC port charges at the stock 450 mA whatever the gadget negotiated; sleep is admitted with a cable when no host has configured the gadget and nothing charges. | — |
| Display (DIS) power domain | Off at screen-off and during sleep with the exact stock MTCMOS sequence (spm_mtcmos_ctrl_disp); OVL/RDMA and the MMSYS clock provider drive it; the GPU domain is its child. Armed only once the UI has drawn its first frame. | dis_pdn |
| Stock DCM | Hardware dynamic clock gating as stock dcm_enable(0x1ff): CPU, TOPCKGEN, INFRA/bus, DRAMC and PERI at boot. | boot spm.dcm=0 |
| Golden sleep entry | At sleep entry, with every device suspended: MMPLL/VENCPLL/MSDCPLL/UNIVPLL off (stock PLL ops), mux power-down bits, unused PERI/INFRA clock gates; restored bit-exactly at wake. Never: MAINPLL/ARMPLL, the AXI mux, the console UART mux, PMIC_WRAP. | golden_apply bitmask 1/2/4/8 |
| Diagnostics | Read-only PMIC golden comparison (44 stock rows) and MD-side peripheral requests at every sleep entry. | — |
| Fuel gauge | Stock 25 °C battery profile (95 rows, 4175 → 3400 mV), stock internal-resistance correction while charging, Q_MAX 1300 mAh. Percentages read higher than on 15 (3.8 V: 54 % instead of 45 %). | — |
| Small fixes | Python 3.15 lost early boot log lines (/dev/kmsg EINVAL); the power journal keeps more than a day (8 MiB files). | — |

Owner switches live in `/data/system/platform/power-features.json`, for example `{"dis_pdn": false, "golden_apply": 3}`; they apply at the next start of the UI.

## Tests

Locked-container production suite: 676 cases, exit 0 (15: 664), including the busybox syntax check of the changed init scripts. Package validation, ELF closure (354 files), installed ARM (40 modules), privacy and inventory PASS. Host suite: no new failures against `main` (739 cases, same host-environment errors).

## Hardware results (2026-10-12, boot `0b0e8a77`)
  - First boot healthy, reset cause none. Display: screen off/on 5 times without a problem; the display domain powered

off and on 5/5 times with no failures after arming.
  - Wi-Fi, Bluetooth, MTP, SSH and audio up.
  - One unplugged sleep 15:32 → 16:08 (36 min, one maintenance wake), clean. USB worked after the wake — the first

time since 13. The unmask register still read `0000ff00` after the wake (not lost), so the cause of the fix is not yet proven; more wakes are needed.
  - Golden SoC rows differing at sleep entry: 26 → 11 (4 of the 11 are deliberate exceptions, see the ledger).

PMIC golden: 15 of 44 rows differ (first capture). INFRA still never loses power (`last_lost=0x0`).
  - The 36-min sleep gives no drain figure: it started right after charging, so the voltage relaxation dominates.
  - Live MD1 test (owner-authorised probe module): the AP may write PERICFG MD1_SET/CLR (0x20/0x28); gating all 26

modem-side requests leaves the AP untouched. 17 will gate them at boot.

## Overnight result (2026-10-12/13, boot `f871fd6a`)

Archive `out/deep-sleep-final/evidence/20261013/110-power16-overnight-return/` (read-only capture before anything else; the owner had restarted with hold-Power at 18:22, so the kernel was untainted, `tainted=0`).
  - Sleep: clean. Unplugged sleep 18:27 → owner's Power press 10:24 (≈16 h). 33 entries, 33 resumes, 0 aborts,

0 failures; 31 maintenance wakes every 1800 s, last wake `0x20` (Power). VPROC sleep voltage, USB PHY save-current and wheel sleep 33/33 without failures (wheel 2 retries per wake, as on 14/15). Display domain 35 off / 35 on.
  - USB after the morning replug: worked (enumerated 10:24:35, the archive itself was taken over USB SSH). Second

good wake on 16. `dma_unmask_lost=32` with `dma_intr_before=0000ff00` is the known false positive of 16's counter.
  - Drain ≈8.6 mA. 86 % → 74 % on the stock curve (≈0.75 points/h over the night). Least-squares fit of the

stock-curve remaining charge at the maintenance wakes, skipping the first 2 h of post-charge relaxation: 8.6 mA (8.5 mA when starting 1.5 h later). 15 was ≈10 mA (archive 108), stock ≈1.3 mA: about 14 % better, still ≈6–7× stock.
  - Why still high: INFRA never loses power (`last_lost=0x0`, `pdn0 0x2fcffff` unchanged on all 33 restores);

`PERI_PDN0_MD1_STA` is 0 at every entry (stock: all 26 modem-side requests gated); SoC golden 11/34 and PMIC golden 15/44 rows still differ, unchanged from the first capture.
  - Owner wake at 10:24: `kernel_resumed` 10:24:29 → `restoring_radios` 10:24:29 → `complete_result_0` 10:24:31.

## Found after the build (fixed in source for 17)
  - The MMSYS part of the DCM never reached 16: kernel overlays are cached by their manifest result hash, and the

edited 0011 patch kept the old hash. New test `test_overlay_hashes` re-applies every overlay.
  - The DMA unmask readback is in bits 15..8, so 16's `dma_unmask_lost` counter is a false positive.

## Not verified

Defect B over many more wakes (2 of 2 good so far), long-term stability of the golden sleep entry beyond one night.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
