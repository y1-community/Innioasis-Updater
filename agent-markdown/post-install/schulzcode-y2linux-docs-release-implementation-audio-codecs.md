---
title: "Feature completion: wired audio and Classic Bluetooth - Innioasis Updater"
description: "Feature completion: wired audio and Classic Bluetooth <!-- knowledge-base-scope: historical-implementation-receipt; baseline02-sync 2026-10-03 -- Dated implementation rec"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-release-implementation-audio-codecs.html"
---

# Feature completion: wired audio and Classic Bluetooth - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Feature completion: wired audio and Classic Bluetooth

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Feature completion: wired audio and Classic Bluetooth

Dated implementation receipt. The campaign identities, test counts and pending actions below belong to the recorded source cut. The newest sealed integrated candidate is [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md). [UART01 hardware](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) now proves bounded C1/C2/C3. Baseline02 new-image/automatic cold boot and unrelated release gates remain open.

Implementation pass, 2026-10-02; Linux starting `9ac2c0b7018ce707ec15f8845daf58ce38ec18a0`, Reborn starting `eb64b8b`. This report covers priorities 5–7. No device configuration, flash, acoustic test or electrical measurement was performed. Qualification remains independent of source and software validation.

## 5–6: precision and native sample rates

Final: PARTIAL / BLOCKED_BY_HARDWARE_PROOF. F075/F076 remain NOT_IMPLEMENTED in the native kernel path. Existing direct output remains S16_LE, stereo, 44.1/48 kHz; 88.2→44.1 and 96→48 family conversion remains truthful. No exact evidence found establishes a safe wider DL1 fetch mode or native 88.2/96 rate code. This is an unresolved implementation prerequisite, not proof that MT6582 silicon cannot do it.

The exact [MT6582 BSP AFE header](https://android.googlesource.com/kernel/mediatek/+/53aba21e332b3864f26832fd9b35a0b372089c10/drivers/misc/mediatek/sound/mt6582/AudDrv_Afe.h) describes DL1 rate at DAC_CON1[3:0], mono selection at bit21, serial width at I2S bit1 and rates through 48 kHz. It does not establish the later-SoC `AFE_MEMIF_HD_MODE`/`AFE_CONN_24BIT` fields. The independent pinned Y2 donor (`artificery-dev/linux`, `53fb57bb99c916c24b65db5b7f9723be37f67826`) explicitly omits 24-bit paths/APLLs, but that donor comment alone is not a hardware limit determination. No MT8173/MT67xx constants were imported.

The retained Y2 HAL analysis, second-I2S report (`Y2Player/docs/Y2_AUDIO_PATH_PHASE4_SECOND_I2S.md`, private research repository), locates `Set2ndI2SOut` and `SetMemIfSampleRate`: stock CONN0=0x00400020, CON3=0x90b, with no wider DL1 fetch operation identified. [Current clock and board evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm3-audio-architecture.md) retains 26 MHz audio/audintbus muxes, 22.5792 MHz DAC crystal and CS43131 PLL-family handling. Linux6.18 CS43130-family driver accepts 88.2/96 and wide sample formats; the upstream DAC acceptance does not establish the SoC DMA/interconnect/clock path.

Current distinctions:

| Stage | Implemented contract |
| --- | --- |
| Source | Actual file metadata, including packed24 and high rates |
| Decoder/DSP | FFmpeg floating point; tested meaningful low bits |
| ALSA software | S16_LE; S24_LE valid24 in32; S32_LE signed32 mapping repaired |
| Y2 wired DMA | DL1 S16_LE stereo only |
| AFE route | I05/I06→O00/O01→CON3; no proven wider fetch mode |
| Serial slot | Programmed32 bits,64 BCLK/frame; independent capture pending |
| DAC payload | Current ALSA path contributes16 meaningful bits; no24-bit DAC claim |

Concrete fixes: Reborn's C membrane accepted enum S32 but its `pcm_format()` switch omitted S32 entirely. Valid observed S32 Bluetooth PCM therefore failed ALSA probing/opening. Added the real ALSA mapping, an exact-format null-sink open/write test and format candidates S32→S24→S16. ALSA negotiation now intersects access, format, stereo channels and rate in one constraint set; independent `test_*` calls previously could accept individually valid but mutually incompatible combinations. Strict observed Bluetooth contracts still never substitute formats; wired enablement profile remains the gate.

Low-bit proof now exercises packed24 WAV→FFmpeg decode→float DSP/limiter→S24/S32 packing at 44.1/48/88.2/96; samples ±1,±127,±255,±257 remain exact. Existing application volume tests preserve low bits at unity. This proves software precision, not native DAC precision.

Changes: Reborn `crates/reborn-audio/native/audio.c`, `crates/reborn-audio/src/native.rs`, `crates/reborn-media/src/native.rs`; Linux [audio_precision.py](https://github.com/schulzcode/y2linux/blob/HEAD/tools/host/audio_precision.py), [capture tests](https://github.com/schulzcode/y2linux/blob/HEAD/tests/test_audio_capture.py).

### Physical proof to add to the integrated harness
  - Record candidate hashes, boot ID, `y2-audio-contract`, ALSA hw_params and existing AFE state while the supported direct path is open. Preserve S16 baseline first. No `plughw`/implicit resampler may stand in for native acceptance.
  - Source-backed wider fetch and higher-rate programming must be resolved before enabling a new kernel mode. Needed evidence is an exact MT6582 register description/stock implementation establishing DMA fetch width and alignment, interconnect width, rate codes, generator/dividers and restoration ordering. Do not write candidate unknown register bits.
  - Generate fixtures once with `python3 tools/host/audio_precision.py <new-directory>`. Capture BCLK, LRCLK and SDATA at the established Y2 pads (GPIO43,44,46), with owner equipment and verified probe voltage. Retain original analyzer data, board/candidate/boot identity, measured MCLK, and capture configuration. I2S decoder must account for the one-bit delay, left/right order, slot width and signed payload alignment.
  - Normalize at least64 consecutive frames as CSV `time_s,left_s24,right_s24`; compare using `--verify-capture capture.csv --rate 44100 --first-frame N`. Checker rejects S16 truncation, channel/value mismatch and >1000ppm rate error; MATCH is only an offline capture match. It cannot authenticate hardware provenance or certify analog fidelity.
  - Once native modes are source-backed, repeat44.1→48→44.1,44.1→88.2,48→96,88.2→96,96→88.2 and high→low with close/reopen, muted safe level, ALSA params, AFE/DAC state and measured clocks. Nominal BCLK at64fs:2.8224/3.072/5.6448/6.144MHz. Verify duration/frame count, pitch, low bits, no stale PLL state, pops, channel swap or underruns. Unsupported modes must refuse and retain family fallback. This is one integrated harness lane, not a separate flash workflow.

## 7: Classic codec implementation

Final: PARTIAL / BLOCKED_BY_HARDWARE_PROOF and BLOCKED_BY_DISTRIBUTION for optional codecs. Private integration profile intentionally enables compiled AAC, aptX, aptX-HD and LDAC endpoints while `platform_qualified=false` and `distribution_approved=false`. SBC remains fallback. Existing explicit owner policy can disable experiments. Public package review remains separate; this does not grant public rights.

| Capability | Built / integrated / software proof | Enabled in private integration | Physical/distribution |
| --- | --- | --- | --- |
| SBC | Existing BlueALSA endpoint; encoder contract | Yes | Retain prior bounded SBC evidence; new candidate regression pending; OSS notices |
| SBC XQ/XQ+ | Real dual-channel44.1,16 blocks,8 subbands,loudness; observed bitpool38/47 gives452/551kbps | Quality preference, requires restart; ordinary SBC fallback when peer/mode differs | Peer audibility/load/coexistence pending; SBC quality policy, not another codec |
| AAC | FDK2.0.3 encoder, endpoint, PCM16, both44.1/48 offline LATM encode | Yes, experimental | Peer pending; FDK source/notice plus public patent/product review |
| aptX | libfreeaptx0.2.2; separate encode test, PCM24 packing | Yes, experimental | Peer pending; LGPL source/linkage obligations and unresolved product rights |
| aptX HD | Separate HD encode test and endpoint; PCM24 in32 observation | Yes, experimental | Separate peer proof pending; same library review, no Adaptive/Lossless claim |
| LDAC | libldac2.0.2.3 encoder/endpoint; S32 PCM | Yes, experimental | Peer/CPU/thermal pending; certification/distribution review unresolved |
| LDAC quality | Real44.1-family303/606/909;48-family330/660/990 | mobile/standard/high preference; next daemon start | Every peer quality/coexistence case pending |
| LDAC ABR | Real queue-driven ABR call; new actual encoder telemetry | Default on; selectable | Synthetic queue transitions proved; real RF adaptation pending |
| Auto | Compiled/runtime/mutual/distribution-or-private gates, prior observed codec, rejection history, fresh CPU PSI/Wi-Fi heavy transfer constraints | Available for eligible private endpoints | At most2 preferred attempts then SBC; no live flapping; peer/reconnect qualification pending |

BlueALSA5 quality is configured at daemon startup. `y2-platform codec-settings` exposes requested/effective settings and pending restart; setters persist validated choices durably and do not interrupt an active transport. Effective requires current-boot receipt plus a live matching daemon argv. Product UI consumes the typed platform contract. Actual negotiated codec remains a D-Bus observation, separate from preference/request/accepted selection. Raw remote advertisement stays unknown where GetCodecs supplies only mutual intersection.

The [BlueALSA patch](https://github.com/schulzcode/y2linux/blob/HEAD/buildroot/patches/bluez-alsa/0001-y2-observe-sbc-and-ldac-encoder-state.patch) exposes read-only `EncoderStats` on PCM1: active, bitrate, SBC bitpool, LDAC quality index, ABR enabled, adaptation count and errors. Atomic fields avoid locks, filesystem writes and D-Bus signals on the encoder thread. Active clears on cleanup. Platform reports XQ only for the actual negotiated mode plus observed bitpool; ABR-linked/enabled with zero transitions is never adaptation proof. Bitrate means encoder payload, not measured radio throughput. Other codecs retain unknown bitrate rather than fabricated measurements.

[Offline encoder contract](https://github.com/schulzcode/y2linux/blob/HEAD/tools/connectivity/codec-software-contract.c) opens no hardware and runs real libraries. ARM/QEMU results: SBC452/551; aptX512bytes and HD768bytes from512 input frames; AAC44.1/48 produces LATM; LDAC starts909/606/303 or990/660/330 and synthetic congestion produces respectively3/2/0 EQMID changes to303/330. This is deterministic encoder functionality, not RF, audible quality or target CPU-load evidence.

Changes: Linux codec manifest/source ledger, radio policy, capabilities, Bluetooth normalization, codec controls/observation, connectivity startup, Buildroot profile/package/patch installation, codec helper and radio-policy tests. Reborn audio files above plus `reborn-platform/{codecs,bluetooth}.rs`; Product UI/client work is recorded in the main pass report.

Remaining physical proof: per codec record daemon endpoints, mutual peer support, actual codec/PCM, encoder stats, audible output, CPU/load/temperature, reconnect and SBC fallback; run Wi-Fi idle/scan/transfer matrix. LDAC ABR must show real adaptation under observed link load, not just synthetic qualification. Pause/release PCM before selection; preserve sole reconnect ownership and uncertain-outcome marker. No LE Audio, aptX Adaptive or Lossless added.

### Source/distribution review

Reviewed primary [BlueALSA5 LDAC encoder](https://github.com/arkq/bluez-alsa/blob/v5.0.0/src/a2dp-ldac.c), pinned local SBC encoder/quality selector and corresponding library headers. [FDK NOTICE](https://github.com/mstorsjo/fdk-aac/blob/v2.0.3/NOTICE), [libfreeaptx COPYING](https://github.com/regularhunter/libfreeaptx/blob/0.2.2/COPYING) and [AOSP LDAC NOTICE](https://android.googlesource.com/platform/external/libldac/+/master/NOTICE) remain explicit source/notice/certification review inputs. No legal clearance was inferred. [Source ledger](https://github.com/schulzcode/y2linux/blob/HEAD/tools/production/codec-sources.json) records source URLs, exact hashes, license hashes, reviewed source and unresolved approval independently of technical enablement. Fresh legal-info must include the local BlueALSA modification and helper source.

### Targeted validation
  - Linux audio5 tests:4 pass,1 built-DT test deferred to integrated kernel build; capture test exercises12 valid/truncated/wrong-clock combinations.
  - Platform evidence3 pass; radio/codec policy7 pass; Bluetooth platform7 pass before final manifest extension.
  - Reborn audio8 and platform69 tests passed; new real low-bit decoder test passes8 format/rate cases. Final workspace fmt/clippy/test and ARM rebuild are integration gates.
  - Patched BlueALSA compiles ARM; QEMU `--version` returnsv5.0.0. Real optional-library contract passes12 printed codec/rate/quality cases, including actual software ABR movement.
  - No previous binary certifies the integration candidate; its clean build/ELF/package results belong to the final receipt.

Post-integration repair: first connection previously had no `codec_policy` until an explicit codec request, hiding the normal UI selector and LDAC settings. The Bluetooth worker now discovers eligibility read-only from current manager endpoints, peer mutual codecs and immutable build inventory. Discovery is cached for the observed transport epoch; disappearance/change invalidates it. A private D-Bus regression verifies that a playing stream exposes eligible choices without SelectCodec/Connect, and that stale peer choices disappear. Strict clippy passes. Saved-preference connection behavior and the SBC-only quality-row integration are covered by the Product lane.

Reliability/privacy closure: persistent codec history is platform-owned, event-only, sanitized to64 valid peer addresses and five known codec counters (maximum255), with a65536-byte publication limit. Unknown fields/events cannot produce unbounded writes; observed negotiation clears that codec's rejection count. The release scanner rejects the entire private Bluetooth state directory and diagnostics exclude peer identities/history. Invalid saved quality preferences now report a settings failure without hiding an independently observed live transport; mutation/startup still refuse invalid policy. Targeted history regression and all9 Bluetooth platform tests pass.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
