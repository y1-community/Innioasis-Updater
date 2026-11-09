---
title: "Implementation lane: Reborn product and battery - Innioasis Updater"
description: "Implementation lane: Reborn product and battery <!-- knowledge-base-scope: historical-implementation-receipt; baseline02-sync 2026-10-03 -- Dated implementation receipt."
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-release-implementation-reborn-power.html"
---

# Implementation lane: Reborn product and battery - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Implementation lane: Reborn product and battery

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Implementation lane: Reborn product and battery

Dated implementation receipt. The campaign identities, test counts and pending actions below belong to the recorded source cut. The newest sealed integrated candidate is [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md). [UART01 hardware](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) now proves bounded C1/C2/C3. Baseline02 new-image/automatic cold boot and unrelated release gates remain open.

Entry: Linux `9ac2c0b7018ce707ec15f8845daf58ce38ec18a0`, Reborn `eb64b8b21058eacb1ef183f7570cca8100cbbb46`. Existing dirty Linux documentation was preserved. No device writes, flash, push or Git identity changes occurred.

## Priority 8 — Product v2

Starting state: Product v2 and the new first-complete-frame splash handoff were already implemented. EQ existed in FFmpeg but had no product control; sleep had no typed UI contract; diagnostic export meant private state backup. Codec selection required `Stopped` although the ordinary UI only exposed Pause.

Implementation:
  - Audio → Equalizer uses existing DSP/limiter with five default bands,

±12 dB/1 dB wheel editing, Select apply, Back cancel and Reset to Flat. Existing custom bands are preserved up to the engine's eight-band limit. Reset Settings now rebuilds playback when disabling an active EQ.
  - Audio → Output Details exposes existing observed source bits/rate,

decoder/DSP precision and opened PCM format/rate through Diagnostics. No native high-resolution claim is inferred from source or container width.
  - System/Quick Settings → Sleep consumes typed `power.sleep` and

`y2-platform sleep request`, with explicit requested/refused/sleeping/ restoring/restored/restore-failed states. Active playback is refused with actionable wording. Ordinary deep sleep still returns `physical_qualification_required` from the platform; owner qualification retains its existing explicit path. Same-boot/kernel-completion checks protect a restored claim. Short Power still means screen off, preserving playback and volume controls.
  - Bluetooth presents preference separately from actual negotiated codec.

Paused/stopped playback permits selection; reconfiguration and the platform PCM lease still exclude active streams. SBC quality and LDAC quality/ABR controls reflect supported runtime settings; requested/effective settings and pending restart remain distinct. Quality labels include both LDAC rate families. CLI help and parser tests cover every viable Classic preference. Final integration review fixed initial read-only capability discovery (audio lane), saved-preference application once per observed peer connection, and SBC-only quality visibility. Selection waits for paused/stopped playback and a non-running PCM; PCM replacement cannot trigger repeated Auto selection. Accepted CLI preferences also persist to ordinary player settings.
  - Diagnostics exposes a separate redacted report export, immediately shows

its archive path/retrieval instructions, and labels state export private. Failed operations cannot display a successful export message. Opening the result retains the previous page/focus, so Back returns to Diagnostics.
  - Estimated SOC is named on the Battery page. Long modal lists now account for

description height, fixing focus rows outside the panel.
  - Ready-frame splash, shutdown save/audio stop/SQLite close/black frame/

backlight off/ack sequence and input duplicate/acceleration/direction-reset foundations remain unchanged and included in current software validation.

Files: Reborn `app/reborn/src/{main,ctl}.rs`, preview fixtures; `crates/reborn-core/src/{lib,platform}.rs`; platform `{client,power}.rs`; UI `{lib,pages,screens,components,diagnostics,tests}.rs`; `docs/ui/REBORN-FEATURE-COMPLETION.md` and platform boundary documentation. No additional direct Y2 filesystem/shell access exists outside reborn-platform.

Validation: final current-source fmt check and strict workspace clippy passed. The combined workspace passed 238 tests, zero failures/ignored, including codec discovery/history/reconnect and complete product regressions. A concurrent fork/CLOEXEC fixture race in the PCM lease test was corrected by using the same bounded reacquire wait already used earlier in that test; production lock semantics remain unchanged. Host preview generated 69 480×360 states; new EQ/picker/sleep/LDAC cases were visually inspected. Output is `Y2Reborn/out/feature-completion-previews/`; final logs are `Y2Reborn/out/feature-completion-final-{fmt,clippy,workspace}.log`.

Remaining physical proof: actual sleep restoration, new-control wheel and playback behavior on the panel, codec peers/qualities/ABR, audio output, boot/shutdown video and diagnostic retrieval in the one integrated run. Distribution: optional codec enablement is the private integration profile; product controls do not resolve redistribution/certification questions. Final lane state: PARTIAL / source implemented and software validated, with full sleep and high-resolution capabilities still platform/physical gates.

## Priority 4 — Battery/charging

Starting state already includes 70/450/650 mA source ceilings, 4.175 V CV, voltage-limited termination/hold/recharge, watchdog ownership, SOC estimate, warning/critical policy, and a debounced 3.4 V shutdown floor. Reborn already saves session, stops audio, closes SQLite and acknowledges the bounded platform shutdown; the coordinator syncs and requests ordinary init shutdown. These paths were reviewed and preserved rather than changing proven electrical policy without new evidence.

Exact source findings:
  - Retained Y2 `fgauge_read_current` at `0xc04caa04` and

`fgauge_read_columb` at `0xc04caa2c` return zero immediately and never fill the output pointer (20-byte functions). These are stubs, not zero measured current or a coulomb counter. Same functions in the exact MT6582 BSP also return STATUS_OK without producing data.
  - Stock temperature conversion assumes a 10 kohm NTC, 16.9 kohm pull-up,

27 kohm pull-down, 1.8 V. Stock public temperature is constant 25 C. Existing physical BATON raw10387–10388/570.6mV did not establish NTC wiring.
  - Stock charger-current computation subtracts ISENSE/BATSNS and assumes

68 milliohm. Existing paired read result (-0.081mV mean,1.638mV standard deviation with charging disabled) cannot validate resistance, channel offset, or net pack-current routing. It is not a calibrated current path.
  - Existing raw IIO BATON1/ISENSE/BATSNS and die thermal acquisition already

provide safe instrumentation. A PMIC die temperature is not pack temperature.

Primary sources freshly fetched: [MT6582 battery_meter_hal.c](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/power/mt6582/battery_meter_hal.c), [MT6323 AUXADC implementation](https://android.googlesource.com/kernel/mediatek/+/d53dd75c3ff77cac3f5be58fddfe660e94f94d64/drivers/misc/mediatek/power/mt6582/pmic_mt6323.c). Local copies under `out/feature-completion-battery-research/`, SHA256 respectively `f0abff44297fa5613cec5e8e74cd0bfe60b67348156e1df6bf36d5b5b453cc0c` and `196b4605c4d367189f6b7b4a6263d617c0c90dfade649020a4e7139acdf27a98`. Y2-specific retained evidence: [ADC result](https://github.com/schulzcode/y2linux/blob/HEAD/docs/hardware-evidence/2026-09-14-m4-adc/result.json), [stock reconstruction](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-battery-acquisition.md), [charger policy provenance](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-charging.md).

Implementation: truthful estimated-SOC presentation only; no fabricated sensor conversion or unproven register/voltage changes. Linux targeted validation: power contract 8 PASS, SOC 5 PASS, charger 4 PASS. Existing broader power/charger tests remain part of parent integrated validation.

Remaining exact blocker: pack/sense schematic or continuity/resistor evidence, reference current/temperature calibration and actual charge/discharge topology. The existing `tools/development/sample-battery-adc.sh` records bounded paired ADC observations; add its results to the integrated harness, not a separate flash workflow. Owner equipment is required to turn those voltages into proven pack current/temperature. Fuel gauge/coulomb support is not established, not proved physically impossible. No new image alone can establish wiring.

Final lane state: conservative charging/low-battery source retained and tested; measurement additions BLOCKED_BY_HARDWARE_PROOF. Full discharge reserve, charging/hold/recharge and low-voltage graceful shutdown remain physical proof.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
