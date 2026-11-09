---
title: "Y2 wired high-resolution PCM completion - Innioasis Updater"
description: "Y2 wired high-resolution PCM completion Session 3 — all-playback-route study live AFE experiments Status: concluded. Final verdict: ALL MT6582 WIDE PLAYBACK PATHS PROVEN"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-highres-audio-completion.html"
---

# Y2 wired high-resolution PCM completion - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 wired high-resolution PCM completion

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 wired high-resolution PCM completion

## Session 3 — all-playback-route study (live AFE experiments)

Status: **concluded. Final verdict: `ALL_MT6582_WIDE_PLAYBACK_PATHS_PROVEN_IMPOSSIBLE` for the Y2 wired path: at most 16 meaningful bits reach the CS43131.** The earlier sections of this file (the withdrawn DL1-monitor argument and the first report) are historical; the measurements below replace them. Everything below was measured on the physical Y2 (Linux 6.18.0-y2linux-platform-v1-baseline-01) with the whitelisted, snapshot/restore lab module [`tools/development/afe-lab`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Ftools%2Fdevelopment%2Fafe-lab%2FREADME.md). Machine-readable log of every register write, readback and restore: [`afe-lab-experiments-session3.jsonl`](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/highres-audio-completion/afe-lab-experiments-session3.jsonl) (`afe-lab-experiments-session3.jsonl`, 473 records; timestamp, kernel, register, mask, original, request, readback, restore readback, PM usage, DAC_CON0, I2S_CON3, IRQ status, abort flag). After every experiment `restore_all` returned all touched registers to their original values (restore readbacks verified) and the AFE returned to runtime suspend; reboot clears the (non-unloadable) module.

### Experiments``````````````````

| ID | Hypothesis | Path / registers | Modification | Readback / observation | Restored | Result and implication |
| --- | --- | --- | --- | --- | --- | --- |
| E1a | Later-SoC AFE_CONN_24BIT (0x6C) exists on MT6582 | 0x6C, 19-bit mask, initial 0 | single-bit toggle of every candidate bit, restore after each | no bit changes | yes | Absent (fixed zero). |
| E1b | AFE_MEMIF_MSB (0xCC), CONN5 (0x5C), CONN6 (0xBC) exist | 24/16/16-bit masks, initial 0 | same | no bit changes | yes | Absent. |
| E1c | Second-DL1/VUL memif (0x340–0x358), HDMI memif/conn (0x370–0x390) exist | base/end/conn/con0 candidate masks, initial 0 | same | no bit changes | yes | Absent (later-SoC blocks not implemented). |
| E1d | MEMIF_MINLEN/MAXLEN | 0x3D0 / 0x3D4, initial 0x11111111 | per-bit toggle | MINLEN fixed; every MAXLEN nibble bit writable | yes | MAXLEN is a real burst-length control, not a format control. |
| E1e | AFE_MEMIF_PBUF_SIZE bits [19:16] are an HD fetch format (later-SoC meaning) | 0x3D8 bits 7:0, 23:16, initial 0xFF0000FF | per-bit toggle; then DL2→AWB with each of bits 16–19 set | all writable; AWB data and DL2 monitor identical for every value | yes | They are DL_ULTRA_TH as the manual says; no fetch-format effect. |
| E2a | DL2 is a usable second playback memif | DL2 base/end, DAC_CON0.DL2_ON, DAC_CON1.DL2_MODE, CONN2 (I07→O05, I08→O06), AWB | DL2 stereo 48 kHz pattern L=1234,1235,ffff,8000 | AWB words bit-exact; AFE_MEMIF_MON1 = L/R 16-bit; 4 bytes/frame | yes | DL2 is an independent 16-bit-per-channel memif; routable to O05/O06 (and per Table 53-1 to O00/O01). |
| E2b | Gain/adder nodes keep >16 bits | GAIN1 in = I07+I08 (DL2 L+R = 0x7000), gain 0.5 → I10 → O05 | — | AWB L = 0xF000 (0xE000 wrapped at 16 bits, halved) | yes | The gain-input adder is 16-bit modular; no headroom. |
| E2c | Main interconnect output saturates at 16 bits | I05 (DL1 L) + I07 (DL2 L), both 0x7000 → O05 | — | AWB L = 0x7FFF | yes | The output node clamps at 16 bits. |
| E2d | Main adder keeps wider internal headroom | I05 + I07 (0x7000 each) + I10 (gain 1.0 of DL1 R = −0x7000) → O05 | — | AWB L = 0x7000 (not sequentially-saturated 0x0FFF) | yes | The output adder accumulates wider than 16 bits internally but delivers a 16-bit saturated output. Sub-LSB precision is not observable through AWB. |
| E3 | Production wire format, 48 kHz | read-only GPIO43/44/46 pad sampling during production S16 playback | none | pins identified (GPIO43 BCLK, 44 LRCK, 46 DATA); 3.07 MHz BCLK is under-sampled by the 425 ns/read sampler | n/a | Not decodable at 44.1/48 kHz; superseded by the slow lab-driven stream below. |

Stock Y2 evidence (re-checked): the primary output profile is `AUDIO_FORMAT_PCM_16_BIT`, 44.1 kHz; `SetHiFiDACStatus` is an unsupported stub; stock DL1 used the 16 KiB AFE SRAM window at `0x11224000` (16-bit PCM); stock programs the CS43131 ASP for 24-bit reception only.

### Serializer-pad measurement (`i2s_capture`)

A dedicated, one-shot, self-restoring lab operation drives a bounded stream from a DL1 and/or DL2 ring through programmed AFE routing into the real I2S serializer (`AFE_I2S_CON3`: I2S format, 32-bit slots, 8 / 11.025 / 12 kHz documented rate codes) and samples GPIO43 (BCLK), GPIO44 (LRCK) and GPIO46 (DATA) by polling the GPIO input register from the kernel. The generic write guard is unchanged. The operation refuses unless armed, no stream/PM reference exists (so no ALSA stream, Reborn playback or other lab experiment is active), DL1/DL2/AWB/I2S are idle and the kernel identity matches; it always disables I2S/memifs, restores and verifies every register it touched, frees DMA and releases clocks before returning. The headphone switch stayed off and no ALSA stream was open (DAPM powers the amplifier only for streams), so nothing was played acoustically. All 32 recorded runs (plus the in-kernel log of every run) ended with `restore_ok=1`, I2S and memifs off, no IRQ status, AFE runtime-suspended.

Decoder: [`i2s_decode.py`](https://github.com/schulzcode/y2linux/blob/HEAD/tools/development/afe-lab/i2s_decode.py) latches DATA/LRCK from the last sample before each rising BCLK edge (BCLK is the reference), finds I2S slots from LRCK transitions (MSB one BCLK after the change) and reproduces the full 32-bit slot per channel. Raw captures: [`i2s-captures/*.bin.gz`](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/highres-audio-completion/i2s-captures/), per-capture records: [`i2s-capture-records.jsonl`](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/highres-audio-completion/i2s-capture-records.jsonl).

Sampler validation (required before interpreting anything). At 8 kHz the stream has 4.6 samples per BCLK (3–5 min/max), LRCK spacing exactly 32 BCLK, actual frame rate 8.0 kHz. Control fixture A (`0x0000, 0x0001, 0x1234, 0x7fff, 0x8000, 0xffff, 0xa5c3, 0x5a3c` and complements) decodes with **0 mismatches over 443 frame pairs on DL1 and 441 on DL2**; 11.025 and 12 kHz also decode with 0 mismatches (3.1–3.2 samples/bit). 16 kHz (2.4 samples/bit) is below the sampler's reliable limit and is treated as inconclusive, not as evidence.````````````````````````````

| ID | Fixture (routing → pad) | Pad result | Meaning |
| --- | --- | --- | --- |
| A | DL1 → O00/O01 and DL2 → O00/O01, S16 test values | slot = value << 16; low 16 bits 0x0000 in every frame; 0 mismatches | Wire format: 16 payload bits MSB-first in a 32-bit I2S slot, 16 zero bits. |
| B1 | O00 = (L>>1)+(R>>1), O01 = L>>1 (right-shift paths), 16-frame rotating pattern | all 429 frames match "exact sum of halves, then round-half-up to an integer" (1,1→1, 3,3→3, 0x1235,0x1235→0x1235); low 16 bits always 0 | The adder retains at least one sub-LSB bit, but the node is rounded to 16 bits before the serializer. |
| B2/G | gain 0.5 (20-bit gain, target = current) on L/R, alone and mixed with shift paths, DC inputs | gain alone: round(0.5·x); gain+shift: exact sum then round (3,3→3, 0x7fff→0x7fff); low 16 bits 0 | Gain output also carries a fraction internally, but it never reaches the pad. |
| C1 | DL1 L + DL2 L = 0x7000 + 0x7000 | 0x7fff | Output clamps to 16 bits at the pad. |
| C2 | DL1 L + DL2 L + gain(DL1 R = −0x7000) | 0x7000 | Internal accumulation is wider than 16 bits, the pad still gets the 16-bit result. |
| D | DL2 source, shift+gain DC fixtures | same exact-then-round behavior; low 16 bits 0 | DL2 is not different from DL1 at the serializer. |
| N | all AFE_CONN0..4/gain connections 0 with both memifs streaming non-zero data; positive control with routing on | pad silent (0x00000000 slots) / data visible | No memif→serializer bypass; the serializer is fed only through the 16-bit interconnect outputs. |
| R | control and shift fixtures at 11.025 and 12 kHz, DL1 and DL2 | identical results; 0 mismatches; low 16 bits 0 | Result is not specific to 8 kHz. |

The required 24-bit test (two inputs with the same upper 16 bits that differ below that boundary) cannot even be formed in the source memifs (16 bits per channel). The adder's sub-LSB bits were created with shifts and gains as the nearest possible approximation; across B1/B2/G/D the serialized slots differ only through the rounded 16-bit result, never in bits 15:0.

### Final architectural check (no bypass)
  - **Complete playback-memif inventory (manual chapter 53 and the exact MT6582

BSP `AudDrv_Afe.h`)**: DL1 and DL2 are the only memory-read playback interfaces. AWB, VUL and MOD_PCM/DAI are write/capture interfaces. Both playback memifs are 16 bits per channel with no format/width field (E1a–E2a).
  - Later-SoC wide fields (`AFE_CONN_24BIT`, `AFE_MEMIF_MSB`, extra DL1 data

memif, HDMI/IEC memif registers, PBUF HD bits): absent or ineffective (E1).
  - Interconnect: gain/summing nodes may carry internal fractions/headroom, but

every output node (AWB observed; serializer pad observed) is a 16-bit rounded/clamped value (E2, B, C).
  - Serializer sources: only interconnect outputs (N). The ASRC blocks

(`0x500–0x570`) belong to the I2S/PCM input interfaces and are not memory playback paths. The internal-DAC route (O03/O04 → DL SRC → PMIC) does not feed the CS43131.
  - Stock Y2: PCM16 primary profile, `SetHiFiDACStatus` unsupported, DL1 16-bit.

The CS43131 ASP is configured for 24-bit reception, which is only a receiver setting.
  - CS43131: supports wider PCM reception, but receives a 32-bit slot whose

low 16 bits are zero from every tested route; no DAC-side limitation is claimed and none is relevant.

Residual limits (stated, not hidden): the pad was decoded at 8, 11.025 and 12 kHz (the polling sampler cannot resolve 44.1/48 kHz BCLK); analog output was not measured. The serializer and interconnect are rate-independent hardware, the DL memifs have no format control at any rate, and the decoded wire format matches the installed S16 readback, so no rate-dependent wide mode is expected. An optional external logic-analyzer capture at 44.1/48 kHz would only confirm this; the procedure is in the owner handoff below.

### Route table (final)

| Route | Memory interface / width | Internal AFE | I2S route / payload | Linux implementation | Live result |
| --- | --- | --- | --- | --- | --- |
| DL1 → I05/I06 → O00/O01 → I2S_CON3 | DL1 ring, 4 B/frame, 16 b/channel, no format field | internal fractions possible, output rounded/clamped to 16 b | 32-bit slots, 16 MSB-aligned payload bits, low 16 = 0 (measured) | production | works, S16 maximum |
| DL2 → I07/I08 → O00/O01 → I2S_CON3 | DL2 ring (0x50/54/58), 4 B/frame, 16 b/channel | same | same (measured) | none (lab only; no product benefit) | pad identical to DL1 |
| DL1+DL2 split recombined in the fabric | two 16-bit memifs | exact accumulation, output rounded to 16 b | pad clamps/rounds to 16 b (measured, B/C) | none | cannot exceed 16 b |
| Later-SoC HD fetch / CONN_24BIT / MEMIF_MSB / DL1_D2 / HDMI / IEC memifs | — | — | — | — | absent (E1) |
| Direct memif → serializer bypass | — | — | — | — | none (N) |
| Internal DAC route O03/O04 → DL SRC → PMIC | not the CS43131 path | — | — | — | out of scope |

### Consequences
  - Keep S16_LE 44.1/48 as the maximum wired output; **do not add S24/S32

masks** (they would be fake: the extra bits cannot reach the DAC).
  - Reborn's software S24/S32 conversion remains correct for other sinks; for the

wired sink the single final conversion is S16. Quality improvement within 16 bits is limited to the conversion step itself (rounding/dither), not transport.
  - The lab module and decoder are development tools only; reboot removes the module.

No candidate or flash is required.

### Owner handoff (optional external confirmation)

If an external check is wanted: probe GPIO43 (BCLK), GPIO44 (LRCK), GPIO46 (DATA) of the second I2S output at the CS43131 side (voltage level not established in source/board evidence here; measure with a probe/analyzer threshold appropriate for the measured logic high). Play a constant S16 pattern (for example both channels `0x1235`) at 44.1 or 48 kHz. Expect BCLK = 64 × LRCK (2.8224 / 3.072 MHz), I2S format (MSB one BCLK after the LRCK edge), 32-bit slots, first 16 bits the sample, last 16 bits zero. Decoder settings: I2S, 32-bit word, MSB first, left = LRCK low. Any non-zero bit in slot bits 15:0 would contradict this record.

## Evidence correction: hardware impossibility is not established

Historical (Session 2). Superseded by the Session 3 measurements above, which establish the 16-meaningful-bit limit from direct serializer-pad evidence and a complete route inventory rather than from the DL1 monitor register.

The previous HARDWARE_PROVEN_UNSUPPORTED verdict is withdrawn. The manual defines two 16-bit fields in a DL1 monitor register. That definition does not, by itself, specify the full internal data bus width in every possible mode. Finding no documented wider fetch selector strengthens the case for a narrow documented interface, but does not prove that all silicon modes or alternative routes are incapable of wider PCM. The earlier conclusion exceeded the evidence.

Current findings: installed playback is S16 throughout ALSA/DMA; software24 packing preserves the tested low bits; CS43131 accepts wider PCM; MT6582 I2S has 16/32-bit serialization. No complete meaningful24/32 hardware path has been established. Neither owner Outcome A nor Outcome B has been met. 24-bit feasibility remains open. True32 also encounters the independently verified binary32 DSP precision loss. No unsupported register write or format enablement is authorized by this correction.

The initial report below is retained as a historical record of the tests and the withdrawn interpretation. Its register values, bytes, source hashes and measurements remain evidence; statements deriving a universal DL1 precision ceiling from MON0 must not be treated as proven hardware capability.

## Initial report — hardware-limit interpretation superseded

Owner task: establish and implement the strongest real MT6582 → DL1 → AFE → second I2S → CS43131 PCM path. **Outcome B: HARDWARE_PROVEN_UNSUPPORTED on the DL1 path for both meaningful 24-bit and meaningful 32-bit PCM.**

The decisive new evidence is the **complete 2798-page MT6582 Functional Specification v0.91**, rather than a technical brief or a later-SoC driver. It documents two 16-bit DL1 output channels. The suspected HD fetch bits actually belong to a prefetch threshold. Wider I2S serialization and a wider DAC receiver do not change this memory-interface boundary. The independent maximum precision of every internal AFE gain block is not claimed here.

This report supersedes the unresolved hardware question in [the earlier precision pass](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-HIGHRES-AUDIO.md). Its evidence and corrections remain historical, including existing software 24-bit packing and true-32 loss detection. No unsupported format mask, guessed register programming, clock forcing, flash or push was performed.

## Evidence classifications

| Label | Meaning in this record |
| --- | --- |
| PROVEN_SOURCE | Exact MT6582 register/interface contract, selected implementation and CS43131 specification. |
| IMPLEMENTED | Read-only kernel/DMA observer, conservative fixtures, native conversion probe and evidence tests. Wider native PCM is not implemented. |
| SOFTWARE_VALIDATED | Actual ARM decode/DSP/packing bytes, existing precision/negotiation tests, production ARM/kernel/config/DT/ABI and relevant tests passed. |
| PHYSICALLY_OBSERVED | Connected Y2 PCM parameters, coherent DMA bytes, instantaneous DL1 output monitor, AFE/I2S and physical DAC register readback, bounded CPU measurements. |
| EXTERNAL_CAPTURE_STILL_REQUIRED | Independent serial bit/padding/clock and analog measurements. No logic analyzer, analog capture or ALSA capture endpoint was available. No wider physical success is claimed. |

Raw scoped observations are in [physical.json](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/highres-audio-completion/physical.json), fixture identities in [fixtures.json](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/highres-audio-completion/fixtures.json), research identities in [sources.json](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/highres-audio-completion/sources.json), and checks in [software.json](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/highres-audio-completion/software.json). Source-bound readback is stronger than ALSA acceptance alone, but is not an external measurement of the pins. The precision-limit conclusion uses the documented complete DL1 contract, not a claimed physical wide-bit capture.

## 1. Original bottleneck and selected source

Installed Baseline01 exposes S16_LE stereo at 44.1/48 kHz. Reborn consequently quantizes the float graph to S16 before ALSA. Direct wide playback is rejected; `plughw` accepts wide files by converting them to S16. This software loss point is distinct from the underlying fixed-width DL1 interface.

Both original repositories were inspected with status, HEAD, log80, branch and worktree inventory. The newest integrated Baseline-final descendants selected were Linux `3f35bc68e7537bffe356f145dcb35837c9d2e9a6` and Reborn `2444e0f65811e688250a8cd069a57dd780b2d6d3`, not the older documentation starting commits. Work uses isolated paired `codex/highres-audio-completion` branches under `/home/luca/Dokumente/Code/worktrees/highres-audio-completion/`. Existing owner checkouts and dirty documentation were preserved.

The installed image identifies Linux `98daf3f0220f4a1580bb4893094ee9f0e02362a5`, Reborn `9cd12baeeb70b204e08299bd4c91c8c35604c304`, kernel `6.18.0-y2linux-platform-v1-baseline-01`, root `2025.02.18-platform-v1.24`, FFmpeg 9.0.2. Selected and installed native media, audio, playback and live-volume sources compare identically. The current image's older `pcm_contract` maximum remains null; the temporary observer and this report provide the newly established hardware conclusion.

## 2–4. Exact MT6582 DL1, interconnect and I2S

Primary hardware source: MediaTek-authored [MT6582 Functional Specification v0.91, complete public mirror](https://disk.yandex.com/d/b2Sy4Y4xFJXYjQ). The archive and PDF hashes are pinned in sources.json; the PDF was extracted, text-searched and the route table visually inspected. Only audio chapter 53 was used for this conclusion.

| Contract | Exact address / section / printed page | Result |
| --- | --- | --- |
| DL1 channel outputs | AFE_MEMIF_MON0, 0x112200d0; p2741 | Right bits 31:16, left bits 15:0. Each documented channel output is 16 bits. |
| DL1 control | AFE_DAC_CON1, 0x11220014; pp2716–18 | Bit21 selects mono/stereo; bits3:0 select rate. No width selector. |
| DMA ring | 0x11220040/44/48; pp2734–35 | Byte addresses; base aligned to eight bytes, inclusive end low bits7. Production driver uses stricter 16-byte alignment. |
| Prefetch | AFE_MEMIF_PBUF_SIZE, 0x112203d8; p2768 | Bits19:16 are DL_ULTRA_TH; low 2 bits choose a 16/32/64/128-byte buffer. Neither is sample width. |
| Wired route | Figure53-1 / Table53-1, pp2706–07; AFE_CONN0 pp2719–22 | I05/I06 → O00/O01, bits 5/22. Optional one-bit right shifts are separate controls. |
| Serializer | AFE_I2S_CON3, 0x1122004c; pp2735–36 | WLEN bit 1 selects 16/32-bit words. Format bit 3 selects I2S. |
| Output rates | §53.2 p2705; DL1/I2S rate fields | Documented master playback rates8–48 kHz, including44.1/48. |

PROVEN_SOURCE: the entire chapter's register map contains no DL1 wide fetch mode or compatible AFE_CONN_24BIT field. In particular, importing later MediaTek HD programming into bits 17:16 would change DL_ULTRA_TH. Offset0x6c was not treated as a safe undocumented wide control.

DL1 feeds the wired route as two signed 16-bit channels. Wider words supplied to its ordinary packed ring would change channel/frame interpretation; they would not establish 24-bit samples. No change of DMA stride or ALSA container can create the missing per-channel fetch/output representation. The complete map also documents DL2's channel monitor as two 16-bit outputs (p2742), rather than an alternate wide downlink. Gain coefficient precision and I2S input width do not define a wider CPU-memory fetch interface.

The AFE fabric's independent maximum width is not explicitly specified for all routes. For the required I05/I06 route it receives DL1's 16-bit values; no source-backed wide connection switch exists. This is the scoped interconnect conclusion, not a claim that every gain block is16-bit. Second I2S can serialize32-bit words, but the current DL1 source contributes only16 meaningful bits. The distinction between word/slot width and payload precision is essential.

Exact [MT6582 BSP definitions](https://android.googlesource.com/kernel/mediatek/+/53aba21e332b3864f26832fd9b35a0b372089c10/drivers/misc/mediatek/sound/mt6582/AudDrv_Afe.h) and [ring implementation](https://android.googlesource.com/kernel/mediatek/+/53aba21e332b3864f26832fd9b35a0b372089c10/drivers/misc/mediatek/sound/mt6582/AudDrv_Kernel.c) corroborate the addresses and controls. Additional exact-MT6582 vendor trees were examined with their actual defconfig/Kconfig selection. Their unselected mixed-SoC `sound/soc` HD code does not establish MT6582 compatibility; the complete register contract now positively identifies the field collision.

88.2/96 kHz were not enabled: documented output rate codes stop at48 kHz, the direct endpoint rejects both, and there is no admitted higher-rate clock contract. Real 24/96 FLAC decoding and resampling to48 was measured below.

## 5–6. CS43131 and original Y2 behavior

PROVEN_SOURCE:[Cirrus CS43131 DS1155F2](https://statics.cirrus.com/pubs/proDatasheet/CS43131_DS1155F2.pdf), §4.9, §7.1.8 and §7.3.22–24, supports8/16/24/32-bit PCM reception and I2S/left/right-justified/TDM arrangements. PCM rate capability extends beyond the admitted MT6582 output rates. Slot timing, channel location and received word length are separate settings. The [Linux6.18 codec implementation](https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/tree/sound/soc/codecs/cs43130.c?h=v6.18) sets ASP word and channel size from `params_width`, separately from the rate×64-derived32-bit slots. No DAC-side16-bit hardware limitation was found.

Retained stock Y2 HAL SHA256 `5c5162f6a68f7db57febd050ee88cc886779dcce5948937149d6cd211eb0e6de`: `SetMemIfFetchFormatPerSample` and `SetoutputConnectionFormat` alias ELF VA 0x31138. Targeted8-byte disassembly returns -38/ENOSYS. Confidence HIGH for this function behavior; it alone would not prove silicon impossibility. Exact-MT6582 open HAL functions likewise return unsupported operations and report16-bit fetch. Details and binary provenance are retained in the earlier report; unrelated code and unchanged ROM/recovery were not re-audited.

Stock route reconstruction uses `Set2ndI2SOut` VA0x61c14 and enable VA0x62838, second-I2S pins43/44/46 and CONN0=0x00400020. Stock DAC initialization selects a24-bit ASP receiver, while the feeding PCM implementation uses16-bit words. A receiver setting is not proof of24-bit source transport. Current Linux correctly selects16-bit ASP reception for its S16 PCM parameters.

## 7–9. Final formats and status

| Native format | Container | Meaningful payload | Physical result |
| --- | --- | --- | --- |
| S16_LE, stereo 44.1/48 | 16 | 16 | Running parameters, DMA, DL1 monitor, I2S/DAC readback PASS. External serial/analog precision measurement not performed. |
| S24_LE / S24_3LE | 32 /24 | 24 requested | Not exposed; hardware DL1 precision limit. |
| S32_LE carrying24 | 32 | 24 requested | Software packing verified; native physical path unsupported. |
| True S32_LE | 32 | 32 requested | DL1 unsupported; binary32 DSP is also insufficient for arbitrary full 32 source precision. |

True 24: HARDWARE_PROVEN_UNSUPPORTED.True 32: HARDWARE_PROVEN_UNSUPPORTED. Both statuses apply to the specified CPU-memory/DL1 wired route. No `32_CONTAINER_24_MEANINGFUL` physical working claim is made.

No native S24/S32 masks were added. Reborn already queries intersected ALSA format/rate/channel constraints and the enabled platform PCM contract, rather than choosing a container from the source file alone. Its existing direct-S16 fallback remains accurate and audible playback pacing remains unchanged.

## 10. Conversion map and low-bit results

Source anchors are relative to the selected paired repositories. All PCM integers below use little endian on Y2, signed two's complement, stereo L/R.``````````````````

| Stage and source anchor | Representation, scaling, packing and loss |
| --- | --- |
| FFmpeg decoder → media.c:1241 canonical_swr | PCM16 decodes S16; PCM24/32 decodes S32. PCM24 is Q31 left-aligned with low 8 zero; normalized by2^31. FLTP uses separate4-byte L/R planes and binary32 precision. No early S16 conversion is imposed on wide sources. |
| media.c:643 make_filter_graph | Canonical stereo FLTP; ReplayGain/headroom, optional EQ, limiter limit.98 without auto-level, optional transitions. Float operations/resampling change samples. Ordinary playback delegates live user gain to VolumeRamp. |
| media.c:246,613,1246 format/output_swr | Negotiated S16:2bytes/sample,4/frame, scale2^15, saturation; installed stereo NEON path packs high Q31 halves, discarding low 16. S32:4bytes/sample,8/frame, scale2^31, saturation. No explicit dither selected. |
| media.c:285–307 S24 packing | S32 scratch → nearest/ties-even divide256 → clamp; low 3 little-endian bytes in4-byte ALSA S24_LE container, padding byte0. Signed bit 23 determines sign; zero padding is not positive-only PCM. |
| media.c:316 / float acrossfade | Transition working S32/Q31 → float graph → S32, followed by final integer narrowing. Existing integer S32→S16 conversion uses nearest/ties-even and clamp; it differs from ordinary FLTP→S16 stereo NEON. |
| Rust queue / volume.rs:37 | Queue copies PCM bytes. Gain=(volume/100)^2 with5ms ramp; non-unity f64 multiply, nearest ties-away rounding, clamp and repack. Settled unity copies bytes, silence emits zeros. Only accepted frames advance gain/queue state. This remains an additional integer quantization at non-unity gain. |
| native audio.c / snd_pcm_writei | Direct hw endpoint; interleaved frames passed without plug conversion. ALSA copy → coherent managed DMA ring, S16 bytes[Llo,Lhi,Rlo,Rhi],4/frame. |
| mt6582-afe.c:128,210,263 | Byte-addressed DL1 ring, stereo/rate controls, routeI05/I06→O00/O01, second-I2S32-bit words; hardware pointer wrap converted from byte address to S16 stereo frames. |
| y2-cs43131.c:19, upstream cs43130 | Serial clock rate×64; separate receiver word 16/channel 16, locations0/32, I2S one-bit delay. DAC conversion follows reception; analog low-bit measurement unavailable. |

The actual ARM [FFmpeg stereo FLTP→S16 NEON implementation](https://github.com/FFmpeg/FFmpeg/blob/n9.0.2/libswresample/arm/audio_convert_neon.S) uses Q31 conversion plus high-half packing (`vsri`), unlike its rounded packed-float converter (`vqrshrn`). Live results confirmed this distinction. The earlier generic “round” description is corrected here. No costly dither or unrelated volume redesign was introduced into a hardware-limited task.

SOFTWARE_VALIDATED / PHYSICALLY_OBSERVED: conservative8-second fixtures peak below -60dBFS. The24-bit positives0x1200/01/7f/ff share their upper16bits; the32-bit positives0x120000/01/7f/ff share their upper24bits. Signed negative partners and the four-frame R offset discriminate channel/sign errors.

On the actual ARM native probe, neutral24→S24 preserved all signed fixture values;24→S32 preserved them shifted8 with low 8 zero. On each of six actual Reborn playback cases, the first 256 DMA bytes matched the final native S16 probe bytes exactly at unity live gain. Wide low-bit differences collapsed before ALSA at S16 conversion. This proves the location of loss in the installed software path, not wider DAC reception.

Low-amplitude32 fixtures do not establish arbitrary full 32 preservation: their values fit within float significand precision. Existing high-amplitude full 32 fixtures such as0x23450001/02 demonstrate the independent S32→FLTP low-bit collapse. Exact24 preservation is established only for the neutral, same-rate fixture graph; EQ, gain, limiter and resampling legitimately change values and round their computations.

## 11–15. Live ALSA, DMA, AFE, I2S and DAC

PHYSICALLY_OBSERVED:`/proc/asound/cards` lists card0 Y2Audio; `/proc/asound/pcm` lists one Y2 Headphone Playback stream and no capture. `aplay -l/-L`, constraint intersections and running hw_params are retained. Direct endpoint accepts only stereo S16_LE at44.1/48. Packed24, S24_LE and S32_LE, plus88.2/96 intersections, were rejected.

| Observation | Value |
| --- | --- |
| ALSA access/subformat | RW_INTERLEAVED and MMAP_INTERLEAVED; STD/MSBITS_MAX |
| Constraints | Period128–32768frames /512–131072bytes; buffer256–65536frames /1024–262144bytes; periods2–256;16-byte alignment |
| aplay direct16 | 44.1: period 5512/buffer 22048;48:6000/24000frames |
| aplay direct24/32 | Rejected; no wide DMA configuration |
| aplay plug16/24/32 | All completed; physical hw_params remained S16, including wide inputs |
| Six Reborn runs | S16_LE,44.1/48,2channels, period 512/buffer 4096; DMA 16384bytes |
| DL1 fetch/ring | Packed signed stereo16,4bytes/frame; current/end/base byte addresses observed;32-bit address mask is not sample width |
| DL1 MON0 examples | 0x0012ffee and0x0014ffec on16 sources;0x0012ffed /0xffed0012 on24 sources after S16 conversion |
| AFE | DAC_CON0=0x3003; DAC_CON1 rate9/a, stereo; CONN0=0x00400020; PBUF=0xff0000ff |
| Second I2S | CON3=0x90b /0xa0b; I2S, WLEN32, enabled; expected64BCLK/frame and16-bit source payload |
| CS43131 identification | DEVID bytes43/13/10 |
| DAC rate/width | SP_SRATE=1/2; SP_BITSIZE=0x06 has ASP[1:0]=2→16bit (independent XSP field differs); CH1/2_SZ_EN=0x05/0x0d has width16 |
| DAC slot/frame | LRCK_HIGH=0x1f / PERIOD=0x3f →32/64clocks; channel locations0/32; CLOCK_CONF=0x0c, FRAME_CONF=0x02→I2S delay |

MON0 and ring snapshots are instantaneous, not mutually clock-synchronized. Readback used `regmap_read_bypassed` with existing active runtime-PM references, so codec cache defaults were not substituted for live hardware observations. No loopback endpoint was found. External BCLK/LRCK/padding and analog output were not measured; they are explicitly EXTERNAL_CAPTURE_STILL_REQUIRED.

## 16. CPU overhead on the connected Cortex-A7

Existing native precision-bench ran five5-second FLAC decodes per case, with real FFmpeg9.0.2 and process CPU time divided by rendered audio time. Figures are percent of one core, not percent of all four cores. DSP-on adds three EQ bands and gain 73; both modes retain the limiter. No ALSA output is opened by this benchmark. S24/S32 are software conversion measurements only.

| Source / output rate / DSP | S16 | S24_LE | S32_LE container |
| --- | --- | --- | --- |
| 16/44.1 →44.1, off | 1.754% | 2.164% | 2.046% |
| 16/44.1 →44.1, on | 2.743% | 3.262% | 3.009% |
| 24/48 →48, off | 2.048% | 2.507% | 2.348% |
| 24/48 →48, on | 3.110% | 3.625% | 3.430% |
| 24/96 →48, off | 6.253% | 6.732% | 6.519% |
| 24/96 →48, on | 8.192% | 8.623% | 8.470% |

Software wider packing adds at most about0.54 percentage points here. Short headless Reborn S16 runs sampled approximately4.29–5.39% of one core including control/observation overhead. These are bounded headroom measurements, not endurance or real hardware-wide playback qualification.

## 17. Regressions and device cleanup

All six Reborn cases had zero xruns, recoveries, playback, decode and filter errors. Source precision reporting and44.1↔48 transitions were observed. Full workspace playback/media/volume/ReplayGain/limiter/EQ/gapless/crossfade tests passed. Their individual production hardware scenarios were not all repeated; no product audio/radio/runtime-PM implementation changed.

The owner requested that Baseline01 CPU qualification finish. Its lease was respected; exclusive `/tmp/y2-platform-v1-device.lock` was then held throughout the audio session. Temporary headless Reborn used a separate test DB, socket and controlled music directory. Production library files were preserved. Actual Reborn opens its hardware mixer at -24dB; fixtures remain below -60dBFS, so the bounded test level stayed below -84dBFS. Format changes were muted.

I initially missed `CONFIG_MODULE_UNLOAD=n` before loading the matching GPL read-only observer. Normal removal was unavailable. A normal reboot removed both observer versions; nothing was flashed. Pre-session boot `9d4d0245-f1f0-45ef-abc9-f43234ae30de` changed to `3bbea37e-e6ae-41e0-bcca-c81bb836fe64`, with the same installed source/image identity. Temporary process, helpers, libraries and music were removed; PCM is closed, Master restored to -60dB and headphones off. Taint512 existed before these audio tests, rose to4608 for the out-of-tree modules, and returned to512 after reboot. No new audio fault is attributed to that preexisting bit. The observer README now requires the unload preflight. The device lease was released after cleanup verification.

## 18–21. Changes, checks, sources and commits

Implemented changes: matching read-only [observer](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Ftools%2Fdevelopment%2Faudio-observer%2FREADME.md), conservative `audio_precision.py --live-safe` fixtures, retained-observation tests, Reborn `tools/build/precision-probe.c`, and truthful scoped roadmap/platform inventory records. No built-in audio behavior changed and no unsupported capability is exposed. Existing Git identity/account were preserved; no push occurred.````````````````````````````

| Repository | Files changed |
| --- | --- |
| Y2Linux diagnostics | tools/development/audio-observer/Makefile, y2_audio_observer.c, README.md; tools/host/audio_precision.py; tests/test_highres_observations.py |
| Y2Linux evidence | This report; docs/validation/evidence/highres-audio-completion/{physical,fixtures,sources,software}.json; superseding note in Y2-PLATFORM-V1-HIGHRES-AUDIO.md |
| Y2Linux records | docs/planning/{roadmap-gap-audit,platform-v1-roadmap}.md; docs/release/Y2-PLATFORM-V1-MASTER.md; Y2-COMMUNITY-BETA-FEATURE-AUDIT.md; Y2-COMMUNITY-BETA-FEATURES.json (F075 only); docs/validation/platform-v1-capabilities.json (three precision rows only) |
| Y2Reborn | tools/build/precision-probe.c; docs/validation/REBORN-Y2-WIRED-PRECISION-COMPLETION.md |

SOFTWARE_VALIDATED:
  - Reborn `cargo fmt --all -- --check`, strict workspace Clippy,

`cargo test --workspace --locked` (324 passed), production ARM build.
  - Strict-warning ARM probe build, 18 native probe cases on the Y2 and

QEMU Cortex-A7 S24 bytes matching the live result.
  - Exact-config observer/v2 module builds; full 6.18 kernel zImage/modules/DTBs

build, production config check, fresh production Y2 DT.
  - Audio/clock/ALSA precision contract tests 6/6, ABI 2/2,

production tests 22/22, audio suspend unwind 1/1, new fixture/DMA tests 4/4.
  - Existing S16/S24/S32 packing, sign, clipping, rounding, full 32-bit loss,

negotiation/fallback, source/output reporting and transition tests are included in the workspace suite. JSON and diff checks accompany this record.

Production DT validation used `innioasis-y2-production.dts`; an initial wrong base-DT invocation was corrected before the reported pass. Host ABI validation uses the retained environment's pyelftools. QEMU was invoked directly as its static PIE executable, rather than through an incompatible host loader. Packaging validation is N/A: no changed built-in/product image or candidate was produced. Unchanged ROM/recovery provenance was not repeated.

Research includes the full exact-SoC manual, MT6582 BSP, selected vendor defconfigs, exact HAL unsupported functions, retained stock Y2 disassembly, official CS43131 specification, Linux6.18 codec and ARM FFmpeg9.0.2 conversion. Exact revisions, hashes and page/function references are in sources.json. The mirrored MediaTek PDF itself is not redistributed in this repository.

Changes are committed locally on paired `codex/highres-audio-completion` branches. Reborn diagnostic/documentation commit: `43db7a93af825b8d28b93c49a50d51283d9c38f7`. The commit containing this file is the Linux source/evidence record; its resulting ID is given in the owner handoff. No self-hash is embedded into a file that would change that hash.

## 22–25. Candidate and owner action

Candidate path: not built. BOOTIMG SHA256: N/A. Y2ROOT SHA256: N/A. No owner flash is required for this conclusion. The current native S16 path remains the strongest documented CPU-memory/DL1 representation. There is no source-backed wider implementation to place in a candidate.

An external I2S capture could independently verify existing16-bit alignment and padding, but cannot supply missing DL1 fetch bits. A different external digital source or different hardware transport would be a different path, outside this task's specified DL1 chain. Wider DAC capability alone is not a software solution for this fixed-width interface.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
