---
title: "Bluetooth codecs: current capability audit and proposed Auto policy - Innioasis Updater"
description: "Bluetooth codecs: current capability audit and proposed Auto policy Bluetooth control optimization — 2026-10-04 The isolated Platform 1.0 Bluetooth pass preserves FFmpeg"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-architecture-bluetooth-codecs.html"
---

# Bluetooth codecs: current capability audit and proposed Auto policy - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Bluetooth codecs: current capability audit and proposed Auto policy

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Bluetooth codecs: current capability audit and proposed Auto policy

## Bluetooth control optimization — 2026-10-04

The isolated Platform 1.0 Bluetooth pass preserves FFmpeg decode, shared DSP, one negotiated sink conversion and BlueALSA encoding. Reborn now refreshes Bluetooth observations on relevant D-Bus signals and user commands, with a 30s reconciliation backstop, instead of a 20ms worker timer and 2s enumeration. A bounded notified command queue wakes descriptor-based waiting immediately. Pairing/discovery deadlines and transport invalidation remain active while idle; BlueZ owner return recreates the pairing agent. Codec capabilities remain cached by transport epoch, requested and negotiated codec remain separate, and Reborn adds no reconnect loop or encoder. Source validation covers idle wake behavior, command responsiveness, stale PCM removal and owner/agent recovery. Physical peer audio, optional codec CPU and coexistence remain separate gates; the owner has no headset available for this pass. Full receipt is in the sibling Y2Linux repository at `docs/validation/Y2-PLATFORM-V1-BLUETOOTH-OPTIMIZATION.md`.

Historical audit/design at its 2026-09-22 revisions. Later Hardware Final source/ARM work compiled a private optional-encoder profile and implemented a gated Auto control, while normal radio launch keeps optional endpoints disabled. This supersedes the audit's "no source/binary integration" statement **only for the later candidate**. Fix01 physically demonstrates a bounded CONSYS retry, not peer codec audio. [Current application state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2FCURRENT_REBORN_STATE.md), [current platform contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Farchitecture%2Fplatform-bluetooth-v1.md), and [later codec source work](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-HARDWARE-FINAL-RADIO-AUDIO.md) separate those scopes. The recommendation below is not implementation authority.

Date: 2026-09-22. Scope: Y2Linux and Y2Reborn as one product.

**Status: AUDIT / DESIGN ONLY. No codec enabled, production code changed, image built, device accessed, or device flashed during this review. Auto is a proposal, not an implemented feature.** Material physical and distribution uncertainties trigger the user's stop condition for implementation.

Audited revisions:
  - Y2Linux: `be7e64c5dd5c6bdfe39c35e8fbd70e6b4b2c4717`.
  - Y2Reborn: `011884b7ef13187171225f252c213afeeb6da851`.

The existing broad [system audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F01_EXECUTIVE_SUMMARY.md) remains relevant. This focused review additionally inspected the retained raw HCI feature/version/buffer-size responses, version-specific BlueALSA/BlueZ source, generated configuration, linked dependencies and current upstream codec/licensing sources. [Evidence, executed checks and qualification plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fbluetooth-codecs%2F2026-09-22-evidence-and-tests.md) give reproducible inspection locations and explicitly unexecuted test cases.

## 1. Decision

Keep the native Linux HCI + BlueZ + BlueALSA architecture and the single Reborn decode/DSP pipeline. Do not replace it with another audio server or put codec encoders in Reborn.

The current image provides SBC only, with BlueALSA's normal high-quality SBC setting. It does not provide AAC, aptX, aptX HD or LDAC A2DP encoding. Even SBC headphone playback is not physically qualified by the retained evidence. Adapter bring-up and discovery are different achievements.

Recommended initial release codec set: **SBC, including ordinary high-quality operation and a conservative fallback**. This is a recommendation after qualification, not permission to label today's Bluetooth production-ready. Next candidates: AAC, aptX/aptX HD and LDAC, individually gated by library provenance/licensing, target builds, CPU budget, interoperability and coexistence. SBC XQ is useful to investigate; it is not a separate codec or an unconditional safe fallback. LDAC 990/909 kbps and 88.2/96-kHz operation stay experimental.

Five findings determine the next work:
  - Establish fresh-bond SBC playback, reconnect and sustained Wi-Fi coexistence

on this Y2 before claiming a multi-codec product.
  - Add truthful typed capability/negotiated-format observation before selection.

Today's adapter ignores BlueALSA `Format` and requests S16 for Bluetooth.
  - Keep one connection-retry owner. The existing platform reconnect helper

requires `Trusted`, which Reborn's pairing path does not establish.
  - Resolve distribution gates. Radio firmware permission is unestablished;

FDK-AAC explicitly grants no patent license; LDAC's AOSP NOTICE requests product certification. aptX library choices have materially different terms.
  - Do not promise per-device LDAC quality control or live bitrate reporting from

stock BlueALSA 4.3.1. Those interfaces do not exist in the inspected version.

### Evidence vocabulary

`VERIFIED` = implementation plus meaningful matching validation; `IMPLEMENTED` = code exists, runtime/physical proof incomplete; `PARTIAL` = only part exists; `WEAK` = architectural/quality concerns; `MISSING` = no meaningful implementation; `UNKNOWN` = inadequate evidence; `DEPRECATED / DEAD` = obsolete path. Confidence is HIGH, MEDIUM or LOW. `PROPOSED` below labels design, not another evidence grade.

| Area | Classification | Confidence | Meaning |
| --- | --- | --- | --- |
| MT6582 identity, advertised BT version/EDR features | VERIFIED | HIGH | Own retained HCI/WMT responses, not marketing specifications |
| Native transport and adapter power | VERIFIED, narrowly | HIGH | Physical bring-up; no sustained audio implication |
| SBC build and service configuration | VERIFIED | HIGH | Recipe, generated config and ELF dependencies agree |
| Shared DSP to Bluetooth PCM | IMPLEMENTED | HIGH | Real source path and host tests; no retained headphone listening proof |
| Fresh pairing/bonding/reconnect end-to-end | PARTIAL | HIGH | Code exists; trust contract and physical evidence incomplete |
| Actual connected headphone codec capabilities | UNKNOWN | HIGH | No connected peer/PCM in retained inspection |
| SBC/AAC/aptX/HD/LDAC real-time and RF qualification | UNKNOWN | HIGH | No appropriate target measurements found |
| Auto selection, bounded codec fallback, device reliability cache | MISSING | HIGH | Current adapter observes a codec string; no codec policy engine |
| Per-transport LDAC quality ceiling/live bitrate API | MISSING in 4.3.1 | HIGH | Global options/encoder state, not PCM D-Bus properties |

## 2. Hardware: what is actually established````````````````````

| Property | Finding and limit |
| --- | --- |
| Controller | Integrated CONSYS_MT6582, WMT chip 0x6582, HVR 0x8a01, FVR 0x8a00; this is the observed E2/E1-ROM combination, not an external USB or Qualcomm controller |
| HCI/LMP | Both report Bluetooth 4.0, code 0x06, revision/subversion 0; manufacturer MediaTek 70 |
| Classic capability | Feature bytes bf 3e 8d fe db ff 5b 87: BR/EDR, ACL 2 Mbps and 3 Mbps EDR, 3-/5-slot EDR packets, AFH central/peripheral and Secure Simple Pairing advertised |
| LE | LE and simultaneous LE/BR-EDR are advertised. LE data is not qualified. This is not LE Audio capability |
| Controller buffering | Read Buffer Size: ACL payload MTU 1021 bytes, 4 ACL packet credits; this is not the negotiated A2DP/L2CAP MTU or proof of four independent streams |
| AP transport | Reborn/BlueALSA → Linux Bluetooth/L2CAP/HCI → native H4 framing → STP BT channel → BTIF with AP_DMA → CONSYS firmware/radio |
| Shared ownership | Kernel CONSYS parent owns power/reset/calibration/recovery. Wi-Fi uses AHB HIF, not the BT audio PCM transport; radios nevertheless share power/co-clock/coexistence resources |
| Antenna | Own WMT_SOC.cfg has coex_wmt_ant_mode=1, co_clock_flag=1; source interprets shared-antenna arbitration. Physical RF wiring, isolation and PTA performance are not measured |
| Controller quirk | Exact chip/HVR/FVR guard applies HCI_QUIRK_BROKEN_LOCAL_EXT_FEATURES_PAGE_2. It does not mask EDR/LE capabilities or force Basic Rate |
| Sustainable throughput | UNKNOWN. Advertising 3 Mbps is not 3 Mbps of usable A2DP payload, and says nothing about losses with Wi-Fi traffic |

Sources: [HCI driver](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/connectivity/hci.c), [core](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/connectivity/core.c), [BTIF](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/connectivity/btif.c), [STP](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/connectivity/stp.c), [bounded protocol](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/connectivity/protocol.h), [own controller summary](https://github.com/SchulzCode/Y2Linux/blob/main/docs/hardware-evidence/2026-09-17-m5-connectivity08/adapter-result.json), [durable quirk validation](https://github.com/SchulzCode/Y2Linux/blob/main/docs/hardware-evidence/2026-09-17-m5-connectivity09/adapter-result.json). Sanitized raw-response fields and their exact private-source line locations are in the companion evidence document; no addresses, keys or calibration are copied.

### Firmware and controller limitations

The checked firmware set includes `mt6572_82_patch_e1_0_hdr.bin`, `mt6572_82_patch_e1_1_hdr.bin`, `WMT_SOC.cfg`, Wi-Fi's `WIFI_RAM_CODE_MT6582`, and `modem_1_2g_n.img` for cold RF calibration. This is a shared bootstrap, not five Bluetooth codecs or an Android audio-offload engine. [Firmware checks](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/connectivity/firmware.c) and [inventory](https://github.com/SchulzCode/Y2Linux/blob/main/docs/knowledge/evidence/m5-firmware-inventory.json) identify exact owner-supplied files; every relevant redistribution permission is still recorded as unestablished. Preserve private calibration and existing firmware validation; never transplant another unit's records.

The controller transports encoded Classic A2DP packets. SBC, AAC, aptX, aptX HD, LDAC and applicable vendor A2DP codecs can be software encoders on the AP; ordinary aptX/HD do not intrinsically require a Qualcomm Bluetooth controller. They still require a matching remote endpoint, encoder, sufficient CPU and RF budget. A stock firmware command named "codec" in `hci.c::setup` is not evidence of AP A2DP encoder offload.

LE Audio/LC3 over CIS/BIS requires LE Isochronous Channels introduced in Core 5.2. This controller's 4.0 interface and current driver do not supply that path. Newer BlueZ libraries or an LC3 library cannot add it. [Bluetooth SIG LE Audio FAQ](https://www.bluetooth.com/media/le-audio/le-audio-faqs/). LC3plus over a vendor Classic A2DP endpoint is a separate possibility, and HFP LC3-SWB is a voice profile, not LE Audio or a stereo-music upgrade.

Four ACL credits and the driver's 128-packet software queue/7-frame STP window are relevant latency/backpressure constraints, not a measured bitrate ceiling. Encoded payload alone at 330/660/990 kbps is approximately 41/83/124 kB/s, before RTP/L2CAP/HCI/STP overhead, air retransmissions and antenna sharing. Wi-Fi scans with Bluetooth merely powered do not validate any of these sustained loads. Historical donor Basic Rate workarounds are not this unit's qualified policy.

## 3. Actual software and build state````````````

| Component | Audited production input / retained build |
| --- | --- |
| Buildroot | 2025.02.17, Cortex-A7 ARMv7 hard-float target |
| BlueZ | 5.79; generated config.h agrees with recipe |
| BlueALSA | 4.3.1, generated version v4.3.1 |
| SBC library | 2.0, selected automatically by BlueALSA package |
| FFmpeg | 9.0.1 media decoding/DSP; no A2DP encoders enabled there |
| Daemon name | /usr/bin/bluealsa, not bluealsad in this version |
| Service arguments | -p a2dp-source --loglevel=warning, both initial launch and supervised restart |
| A2DP codec enabled | SBC; default sbc_quality = SBC_QUALITY_HIGH |
| Disabled optional codecs | AAC, aptX, aptX HD, LDAC, FastStream, LC3plus, Opus, MPEG/MP3; mSBC/LC3-SWB also not enabled |

Evidence: [production defconfig](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/configs/y2_production_defconfig), [input lock](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/inputs.lock.json), [service](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/board/y2/production-overlay/usr/libexec/y2/connectivity). The companion ledger identifies the ignored retained build tree and exact generated files. Its ARM executable links `libsbc.so.1` and no optional codec library; configuration/source inspection also excludes static optional codecs. This does not establish which image is currently installed on a powered device.

The pinned Buildroot recipe couples codecs to independently selected packages: FDK-AAC → `--enable-aac`; libopenaptx → both aptX variants; libopus → Opus; LAME → MP3 encoder. These are explicit recipe branches, **not compiler autodetection**, but adding an unrelated library can broaden Bluetooth capability. FDK-AAC and libopenaptx are not selected today. There is no existing LDAC, libfreeaptx, LC3plus or LHDC production package in this Buildroot tree.

Upstream 5.0.0, dated 2026-08-27, adds LHDC v3 and changes executable names, PCM rate property names and other interfaces. It also fixes Android-Opus configuration. Do not paste its manual into a 4.3.1 integration or upgrade it incidentally while enabling a codec. [Upstream release notes](https://raw.githubusercontent.com/arkq/bluez-alsa/master/NEWS.md).

### BlueZ versus BlueALSA

BlueZ handles discovery, bonds, profile signaling and transport setup. It does not become an AAC/LDAC encoder because audio plugins are enabled. BlueALSA registers local A2DP endpoints, configures the remote transport, encodes PCM and writes acquired transport file descriptors. The per-packet audio data is not passed through a D-Bus method or copied through the `bluetoothd` process.`CONTROL UI -> Action/Effect -> Reborn Bluetooth worker -> system D-Bus | | | | bluetoothd bluealsa | bonds/SEP PCM/encoder +------ typed status/events -------+ DATA FFmpeg decode -> shared DSP -> final PCM conversion -> ALSA BlueALSA plug-in -> PCM pipe -> bluealsa encoder/RTP -> acquired L2CAP transport fd -> Linux HCI -> native BTIF/STP/CONSYS -> headphones RECOVERY OWNERS CONSYS kernel: shared-radio failures platform helper: connection retries Reborn Bluetooth service (proposed): codec attempts / audio-state coordination`

## 4. Codec capability matrix

This table is deliberately wider than the recommended set. Bitrates are nominal encoded payload operating points, not measured Y2 maxima. Every Y2 sustained maximum, encoder CPU percentage and incremental RSS is currently UNKNOWN. CPU/memory categories are architecture-based estimates (LOW confidence), not benchmarks. ARM "plausible" is source portability, not a successful Y2 build.

| Codec | Transport | Local encoder available | BlueALSA support | ARMv7 | Remote compatibility | Nominal bitrate / Y2 practical max | Input rates, kHz | CPU / memory estimate | Wi-Fi risk | License status | Y2 recommendation |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| SBC normal/high | Classic A2DP mandatory | libsbc 2.0, built | 4.3.1, enabled | Built ARM ELF | Required A2DP baseline | Usually ~328 at 44.1, ~345 at 48 for HQ; peer bitpool can lower it; max UNKNOWN | 16/32/44.1/48; Reborn accepts last two | Low; small streaming state | Lowest baseline, not immune | LGPL-2.1+ library | SHIP candidate, mandatory last codec; qualify first |
| SBC XQ / XQ+ | Same SBC endpoint, dual-channel quality modes | Same libsbc | 4.3.1 contains both; not activated | Same build | Must accept configuration; real interoperability required | ~452 / ~551 at 44.1 in this version; max UNKNOWN | 44.1 for these implementations | Low–moderate; small | Medium/high | Same library; no separate XQ license | EXPERIMENTAL per-device modes, not global default |
| AAC-LC | Classic optional A2DP | FDK-AAC; Buildroot 2.0.3 available, not built | 4.3.1 optional | Explicit Buildroot ARM support; Y2 build untested | Valuable Apple/Beats and other AAC sinks; inspect actual peer | Current upstream default target 220; proposed test 256, peer/config/MTU limited; max UNKNOWN | Code advertises 8–96; initial product restrict 44.1/48 | Moderate/high; encoder working state, afterburner increases both | Lower payload, CPU/bursts still matter | FDK terms/source delivery; no patent grant | EXPERIMENTAL → SHIP candidate after legal/CPU/peer gates |
| aptX | Classic vendor A2DP | libfreeaptx, libopenaptx, AOSP source | 4.3.1 optional; disabled | Portable C/Buildroot recipe; untested here | Many aptX sinks, never infer from Adaptive branding | 352.8 / 384 at 44.1/48; max UNKNOWN | 16/32/44.1/48 | Low–moderate; small fixed state | Low/medium | Library choice significant; see §6 | EXPERIMENTAL → SHIP candidate, especially CPU-limited peers |
| aptX HD | Classic vendor A2DP | Same families, HD encoder | 4.3.1 optional; disabled | Plausible; untested here | Explicit HD endpoint required | 529.2 / 576 at 44.1/48; max UNKNOWN | Code offers 16/32/44.1/48; initial 44.1/48 | Low–moderate; small fixed state | Medium/high fixed payload | Same licensing review, distinct codec | EXPERIMENTAL → SHIP candidate after 24-bit sink/EDR tests |
| LDAC | Classic vendor A2DP | Sony AOSP libldac encoder + ABR; Linux ldacBT packaging | 4.3.1 optional; disabled | Portable source, no Y2 package/build yet | Sony and other explicit LDAC sinks | 303/606/909 at 44.1-family, 330/660/990 at 48-family; max UNKNOWN | 44.1/48/88.2/96 in 4.3.1 | Moderate, higher-rate risk; bounded frames + library state | High at 990; ABR helps but proves nothing | Apache-2.0 plus product certification NOTICE | EXPERIMENTAL; ≤606/660 candidate after gates, high mode stays opt-in |
| LHDC | Classic vendor A2DP | Current integration needs binary lhdcBT encoder/decoder | Not 4.3.1; 5.0.0 v3 support; v2/v5 encode paths reject | Compatible glibc ARMv7 binary/provenance UNKNOWN | Specific LHDC generation/endpoint, limited value without a test peer | v3 ceilings 400/500/900 in source; max UNKNOWN | v3 44.1/48/96 | UNKNOWN / UNKNOWN | High at upper modes | Binary redistribution and vendor terms unresolved | DO NOT SHIP now; not inherently impossible on BR/EDR |
| LC3plus HR | Classic vendor A2DP, not LE Audio | ETSI/Fraunhofer reference library | 4.3.1 optional; disabled | Fixed/floating source plausible; untested | Niche matching LC3plus HR sinks, not arbitrary LC3 earbuds | BlueALSA default 396.8; other rates require library/peer limits; max UNKNOWN | 48/96 in this integration | Moderate estimate; query state/scratch sizes | Depends on bitrate | ETSI source terms; no implicit patent license | DO NOT SHIP initial product; little demonstrated peer value |
| MPEG/MP3 | Classic optional MPEG A2DP | LAME encoder; mpg123 is decoder, not source encoder | 4.3.1 optional; disabled | Existing Buildroot package, untested Y2 encoder | Optional and not a dependable modern baseline | MP3 up to 320, profile/mode dependent; max UNKNOWN | 16/22.05/24/32/44.1/48 advertised | Moderate/high; encoder buffers | Modest payload | LAME LGPL library, exact build/license review | DO NOT SHIP initial product; no passthrough advantage after DSP |
| Opus, Android A2DP variant | Classic vendor extension | libopus | 4.3.1 optional, 5.0 fixes config; disabled | ARM-supporting library, untested here | Matching Android extension, not all Opus players/headsets | 4.3.1 sets 128 kbps/channel, 256 stereo; max UNKNOWN | 48 | Moderate at complexity 5; bounded state | Modest payload, unqualified | BSD-style plus published patent grants | DO NOT SHIP initial product; interoperability/work ratio poor |
| FastStream | Classic vendor bidirectional A2DP | libsbc | 4.3.1 optional; disabled | Same library plausible | Specialized compatible duplex headsets/adapters | ~200–220 music + ~72 voice; max UNKNOWN | Music 44.1/48; backchannel 16 | Low + second direction; small | Additional backchannel airtime | libsbc terms; vendor/profile review | DO NOT SHIP music-only product; no quality upgrade |
| aptX Low Latency / TWS variants | Classic vendor extensions | Codec-name constants are not implementations | No implemented matching source SEP in inspected 4.3.1/5.0 set | Not established | Specific peer extensions | Not a Y2 operating point | Not negotiated here | UNKNOWN | UNKNOWN | Vendor/IP review | DO NOT SHIP; plain aptX is not LL/TWS support |
| aptX Adaptive | Proprietary Classic-audio ecosystem | No usable encoder integration established for this stack | No source SEP implementation | No deployable path established | Matching licensed implementation on both ends | Product/version dependent; no Y2 operating point | Not negotiated here | UNKNOWN | UNKNOWN | Proprietary ecosystem/licensing | DO NOT SHIP / not realistically implementable in current stack |
| aptX Lossless | Qualcomm Adaptive/Snapdragon Sound ecosystem | No usable Y2 implementation | No source SEP implementation | No deployable path established | Appropriate Snapdragon Sound peers/source required | No Y2 operating point | Not negotiated here | UNKNOWN | Very high throughput requirement | Proprietary system/qualification | DO NOT SHIP / platform limited; not an aptX HD switch |
| LC3 LE Audio / Auracast | LE ISO CIS/BIS, not Classic A2DP | Software LC3 exists, insufficient | No current Y2 path | Library build irrelevant to missing transport | LE Audio peer not enough | N/A on Y2 | N/A on Y2 | Not applicable | Not applicable | Separate spec/library terms | IMPOSSIBLE / HARDWARE LIMITED on present controller path |

Sources for the matrix: retained `src/a2dp-{sbc,aac,aptx,aptx-hd,ldac,lc3plus,mpeg,opus,faststream}.c` and `codec-sbc.c` in the pinned build; [versioned upstream source tree](https://github.com/arkq/bluez-alsa/tree/v4.3.1/src); [LHDC v5.0.0 source](https://raw.githubusercontent.com/arkq/bluez-alsa/v5.0.0/src/a2dp-lhdc.c); [current integration prerequisites](https://github.com/arkq/bluez-alsa/wiki/Installation-from-source). The legal sources are separated in §6. Apple's [AAC description](https://support.apple.com/en-us/118295) supports the AAC ecosystem rationale, not an assertion that a particular peer advertised it to this Y2.

Other recognizable codec IDs, PipeWire Opus variants, Samsung proprietary codecs, ATRAC, MPEG-D/USAC and HFP voice codecs must not become UI choices merely because a header names them. `a2dp-codecs.c` has names for more codecs than `a2dp.c` has actual encoder endpoints. ASHA/G.722 in newer BlueALSA is a separate hearing-aid profile, not this A2DP-headphone project. Neither ASHA nor LC3-SWB justifies claiming LE Audio.

## 5. Important codec-specific conclusions

### SBC is a useful quality baseline

The service already defaults to high, not a deliberately poor mode. BlueALSA chooses bitpool inside peer limits. In 4.3.1, XQ requests dual channel, 44.1 kHz, 16 blocks, 8 subbands, loudness allocation, bitpool 38; XQ+ uses 47. These yield approximately 452 and 551 kbps. An older release-note number is not the current algorithm. XQ source initialization restricts advertised frequency and channel mode globally. Do not use `--sbc-quality=xq` as a casual production default: that changes the mandatory fallback's compatibility surface.

Model `codec=Sbc` and `quality=Xq` separately. A headset does not advertise an "SBC XQ codec". Check the legal SBC configuration and actual peer behavior; never exceed the peer's bitpool or use `NonConformant=true` for Auto. A lower bitpool fallback can be proposed inside negotiated bounds; if a peer cannot support the chosen setting, skip it, do not force it.

### AAC: useful, but select the encoder deliberately

The inspected implementation uses FDK-AAC, not FFmpeg's AAC decoder or native AAC encoder. Initial product policy should use AAC-LC, stereo 44.1/48 kHz, conformant transport, and a measured target such as 256 kbps clipped to remote limits. That target is a proposal; today's optional-code default would be 220 kbps, with afterburner off. Keep afterburner an engineering benchmark variable, not another ordinary user setting. It improves analysis at extra CPU/memory cost. Do not enable `--aac-true-bps` or nonconformant fragmentation as a quality shortcut. FDK's actual negotiated profile/rate/VBR behavior must be observed.

### aptX families are not interchangeable

Classic aptX and aptX HD have viable software implementations. The stock Buildroot dependency is libopenaptx 0.2.1, GPL-3.0+, not LGPL. libfreeaptx is the LGPL-2.1+ fork supported by BlueALSA's `--with-libfreeaptx` option; adding it requires a deliberate pinned package. Official AOSP also contains Apache-2.0 aptX/HD encoder source, but it is not a drop-in package/API selected by the current recipe. Do not build a new adapter only to avoid understanding existing library/license choices.

Do not ship `arkq/openaptx`'s reverse-engineered/proprietary archive variants by default; its own README carries a binary-distribution warning. Do not generalize that warning to mean all aptX encoders are equally licensed or prohibited. Adaptive and Lossless are different technologies, absent from this encoder integration. Qualcomm describes Lossless as an Adaptive/Snapdragon Sound capability. Their exclusion is an implementation/platform/licensing conclusion, not a claim that all vendor Classic codecs require Bluetooth 5.2. [Qualcomm Lossless description](https://www.qualcomm.com/news/releases/2021/09/qualcomm-adds-bluetooth-lossless-audio-technology-snapdragon-sound).

### LDAC: adaptive does not mean "safe at 990"

Sony's AOSP encoder plus ABR is the relevant source-side implementation. The Linux packaging supplies `ldacBT-enc` and `ldacBT-abr`; an LDAC decoder is not needed to transmit to headphones. BlueALSA 4.3.1 advertises 44.1/48/88.2/96 kHz, and initializes its encoder with S32 PCM. This is not a promise of lossless 32-bit reproduction. A codec capability is not the selected rate: LDAC does not imply 96 kHz.

Public fixed operating points are 330/660/990 kbps in the 48-kHz family and 303/606/909 in the 44.1-kHz family. ABR can traverse additional intermediate quality levels: the inspected AOSP ABR table includes 492/396 kbps at 96 kHz. Do not implement a three-value "measured bitrate" enum. [Sony overview](https://www.sony.net/Products/LDAC/), [AOSP ABR source](https://android.googlesource.com/platform/external/libldac/+/refs/heads/main/abr/src/ldacBT_abr.c).

In the pinned encoder thread, ABR observes local transport socket queue depth and blocking writes, not actual over-air packet-loss percentage or headphone buffer health. Its thresholds are 6/4/2 queue units. `--ldac-quality=standard` sets the starting encoder mode; adding `--ldac-abr` does not establish a documented 660-kbps ceiling. ABR may increase quality again. Neither the selected LDAC capability blob nor `PCM1.CodecConfiguration` contains current ABR bitrate.

Consequently:
  - Stock 4.3.1 experimental testing can use one fixed daemon-wide quality, or

uncapped ABR while explicitly treating all its reachable levels as experimental.
  - Production Auto must not claim a capped adaptive mode without an enforceable,

tested per-transport ceiling and actual mode feedback.
  - Stock API fallback can change codec after closing/reopening PCM. It cannot

honestly implement the complete per-device runtime LDAC quality ladder.
  - Do not restart the global daemon on every underrun to simulate quality control.

This would disturb connection ownership and all PCM objects.
  - Do not display `660 kbps` as live fact merely because Standard was requested.

## 6. Licensing and redistribution gates

Owner decision for public releases (2026-10-16, Y2Linux Baseline 49). Public images and the public over-the-air updates carry SBC, AAC and LDAC; aptX and aptX HD stay in owner-private builds (`tools/production/build.py --public` leaves libfreeaptx out). AAC comes from fdk-aac-free 2.0.3: Red Hat's stripped FDK library (AAC-LC only; the HE-AAC SBR/PS parts are removed), upstream `gitlab.freedesktop.org/wtaymans/fdk-aac-stripped` (branch `stripped5`), the version Fedora ships after its legal review concluded it is no longer encumbered by AAC patents; A2DP uses AAC-LC. LDAC is Sony's Apache-2.0 code; its NOTICE asks for certification for product use, so Reborn claims no certification and shows no logos. The codec inventory (`/etc/y2linux/bluetooth-codecs.json`, profile `public`) marks exactly these three as approved, and public packaging refuses anything else. This is the owner's decision, not a legal opinion.

This is an engineering distribution audit, not a legal clearance. Copyright permission, patent scope, brand/logo use, product certification and firmware redistribution are different questions. A free source download settles none of the others automatically. Review the intended countries and whether Reborn is distributed as source, a binary firmware image, or hardware.

| Dependency / source | Identified terms | Required release action |
| --- | --- | --- |
| BlueALSA 4.3.1 | MIT | Preserve copyright/license; include actual version and modifications in SBOM |
| BlueZ 5.79 | GPL-2.0+ programs, LGPL-2.1+ libraries per Buildroot | Corresponding-source/license obligations for shipped components |
| libsbc 2.0 | LGPL-2.1+ library; optional tools separately GPL | Supply notices, corresponding library source/modifications and compliant relinking arrangement; do not mislabel tools |
| FDK-AAC 2.0.3 | Custom FDK license, binary/source redistribution conditions, complete source available free of charge, no patent license | Evaluate AAC patent authorization/territory; preserve NOTICE and modifications; no presumed coverage from old Android firmware |
| libopenaptx 0.2.1 | GPL-3.0+ | Deliberate linked-work compliance review; do not accidentally combine with FDK in a daemon without license-compatibility review |
| libfreeaptx | LGPL-2.1+ source fork | Prefer evaluating this maintained-interface route; pin audited revision, source/relink compliance, separate patent/trademark assessment |
| Official AOSP aptX / HD encoders | Apache-2.0 source headers, including its defined contributor patent grant | Audit selected source provenance and grant scope; different license/API from libopenaptx, no automatic BlueALSA integration or branding certification |
| Sony AOSP libldac / Linux ldacBT | Apache-2.0 copyright license; AOSP NOTICE requests certification for product use | Retain license/NOTICE; clarify applicability to public Linux firmware and product claims with qualified advice/Sony before public enablement; do not imply a decoder license is required for this source-only path |
| LC3plus reference | ETSI IPR-policy copyright notice, no implied patent license | Obtain applicable terms; Fraunhofer offers licensing and describes a high-resolution-encoder-only royalty exception in an older overview—verify scope/current agreement, do not assume universal free use |
| LHDC libraries | Binary dependencies in upstream integration; redistributable ARMv7 package not established | Do not add blobs without source/provenance, ABI, security and redistribution review |
| libopus | BSD-style license and separately published royalty-free patent grants with conditions | Preserve license/patent notices; matching wire format/peer remains a separate technical gate |
| LAME | LGPL library; exact configured components matter | Preserve terms/source, check build composition; not enough user value to add now |
| MTK firmware / board configuration | Owner extraction with permission explicitly unestablished | No public blob bundling until rights established; document lawful owner-supplied provisioning if that remains the model |

Primary legal sources: [FDK NOTICE](https://raw.githubusercontent.com/mstorsjo/fdk-aac/master/NOTICE), [libopenaptx COPYING](https://raw.githubusercontent.com/pali/libopenaptx/master/COPYING), [libfreeaptx source/license](https://github.com/regularhunter/libfreeaptx), [AOSP aptX encoder](https://android.googlesource.com/platform/packages/modules/Bluetooth/+/refs/heads/main/system/embdrv/encoder_for_aptx/src/aptXbtenc.c), [AOSP aptX HD encoder](https://android.googlesource.com/platform/packages/modules/Bluetooth/+/refs/heads/main/system/embdrv/encoder_for_aptxhd/src/aptXHDbtenc.c), [openaptx warning](https://github.com/arkq/openaptx), [ldacBT license](https://raw.githubusercontent.com/EHfive/ldacBT/master/LICENSE), [LDAC certification NOTICE](https://android.googlesource.com/platform/external/libldac/+/2efdd91222c4c5f929335f34cbc3b576343cf1d2/NOTICE), [Sony certification/contact entry](https://www.sony.co.jp/en/Products/LDAC/aosp/), [LC3plus header terms](https://raw.githubusercontent.com/arkq/LC3plus/master/src/fixed_point/lc3plus.h), [Fraunhofer licensing](https://www.iis.fraunhofer.de/en/ff/amm/communication/lc3/lc3-lc3plus-licensing.html), [older LC3plus royalty overview](https://www.iis.fraunhofer.de/content/dam/iis/en/img/ff/Audio/patent-lizenz/Fraunhofer-LC3plus-Licensing.pdf), [Opus grants](https://opus-codec.org/license/), [LAME license guidance](https://lame.sourceforge.io/license.txt).

Do not use LDAC/aptX/Hi-Res logos or claim certification based solely on a successful encode. Sony's public page distinguishes free source implementation from sink licensing, while its NOTICE still asks for certification. That tension requires a product-specific answer, not a blanket assertion that Linux encoding is forbidden or automatically certified. Likewise, do not declare aptX patents expired everywhere without jurisdiction-specific evidence.

## 7. PCM and precision contract

### Current, inspected path`16-bit FLAC -> FFmpeg s16 ----+ +-> stereo FLTP at source rate 24/96 FLAC -> FFmpeg s32 ----+ -> shared volume/ReplayGain/EQ/limiter -> FFmpeg final swresample -> packed S16, 44.1 or 48 kHz requested for BT -> ALSA "bluealsa:" plug wrapper -> BlueALSA SBC S16 encoder -> A2DP`

[media.c](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-media/native/media.c) creates `canonical_swr` with the decoder rate on both sides and FLTP output; `output_swr` performs final sink-rate/format adaptation. [Bluetooth status](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-platform/src/bluetooth.rs) matches exact connected peer, `A2DP-source`, `mode=sink`, stereo 44.1/48 kHz. [ALSA adapter](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-audio/src/native.rs) chooses S16 whenever output is Bluetooth. It does not select based on `PCM1.Format`.

The shipped ALSA `bluealsa` definition is itself a `type plug` wrapper, not necessarily a conversion-free raw PCM. Current rate matching reduces accidental resampling for SBC, but a future wider-format codec could silently receive an S16-derived signal converted again by ALSA. Inspect the slave's negotiated format; accepting an application S32 buffer through `plug` is not precision proof.

FLTP is 32-bit IEEE floating point, approximately 24 significant binary bits, not 32-bit integer precision. S32 buffers in parts of playback/crossfade do not change that. Preserve the common DSP's existing precision; a future wider DSP decision is separate work, not a Bluetooth codec change. The existing broad [audio audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F05_AUDIO_AUDIT.md) also records unresolved gapless/transition/limiter/lifecycle concerns. This review does not certify those features merely because the user asks that they not regress.

### Negotiated final format, not codec-name inference``````````````````

| Codec integration in 4.3.1 | BlueALSA PCM input | Channels / rates | Reborn adaptation needed |
| --- | --- | --- | --- |
| SBC, AAC, aptX, MPEG, Android Opus | S16_LE, property 0x8210 | SBC/AAC can negotiate mono/stereo; aptX stereo; Opus mono/stereo; supported rates in matrix | Final float → S16 only at sink; explicitly tested dither/rounding policy |
| aptX HD, LC3plus | S24_LE in a 4-byte container, 0x8418 (S24_4LE in BlueALSA naming) | HD stereo; LC3plus mono/stereo; intersect actual rates | Add correct signed 24-in-32 packing/ALSA format; not packed 3-byte S24 and not S32 amplitude layout |
| LDAC | S32_LE, 0x8420; encoder called with LDACBT_SMPL_FMT_S32 | Mono/dual/stereo in capabilities; initial product stereo at 44.1/48 | Final float → S32 at boundary; do not first narrow to S16 |
| FastStream | S16 music + separate S16 mono voice PCM | 44.1/48 music, 16 voice | Not selected for product; never mistake backchannel for playback |
| LHDC v3, upstream 5.0 only | Version-specific 16/24-bit configuration and 32-bit internal buffers | Stereo, 44.1/48/96 | Out of initial scope; inspect actual future PCM Format, not a v4 assumption |

The AAC capability helpers also recognize 5.1/7.1 channel configurations for applicable profiles. They are not an invitation to add surround output: Reborn's canonical/player contract is stereo, and initial codec selection must request and validate two channels explicitly.

A future `SinkSpec` must contain actual format, physical and valid bit widths, rate, channel layout, device identity and transport generation. Always validate properties after selection and again at open. Handle unknown values as a failed candidate, not an implicit S16 conversion.

Use one final sink converter. Prefer exact source rate **within an already qualified common set** when starting a new audio session; otherwise 44.1-family sources → 44.1, 48-family sources → 48, then an available qualified alternative. Do not upsample 44.1 to 96 for a logo. Start with 44.1/48 for Auto even on LDAC; 24/96 is downsampled once at the sink boundary until separately qualified. Do not reconfigure the Bluetooth rate at every track boundary: keep it stable through gapless/crossfade and let the final converter handle source changes.

Volume ownership also needs an explicit contract. BlueALSA 4.3.1 defaults to software attenuation and persists volume state; Reborn already applies volume in its shared DSP. Establish a controlled neutral encoder-side gain or a clearly defined remote-volume arrangement, with quiet-level physical testing. Never force a headset to maximum volume just to simplify gain accounting. Do not let independent persisted attenuation or AVRCP events create two volume authorities.

## 8. Production negotiation architecture — PROPOSED

### Responsibilities and typed state`AppModel: Auto/manual intent, output choice, playback intent | Action/Effect BluetoothService (existing worker extended, one bounded coordinator) +-- BlueZ adapter: paired device + remote SEP capability observations +-- BlueALSA adapter: local runtime inventory + usable codec intersection +-- pure CodecPolicy: ordered eligible candidates, no I/O +-- negotiation state machine: bounded attempts and generation checks +-- bounded DeviceProfileStore: preferences / compact stability evidence | SinkReady(actual format, transport generation) Playback owner: stop/quiesce/open/resume the SAME media pipeline | service events AppModel -> UI and rebornctl: preference distinct from actual negotiated state`

No generic plugin architecture, per-codec service threads, new DSP or external policy daemon is needed. Wire strings are decoded once inside the BlueALSA adapter; arbitrary strings do not propagate through application policy.

Illustrative types, not implementation:`Codec = Sbc | Aac | Aptx | AptxHd | Ldac ObservedCodec = Known(Codec) | Unknown { standard_id, vendor_id, vendor_codec_id } Preference = Auto | Prefer(Codec) // manual means preference + safe fallback SbcQuality = NormalHigh | Conservative | Xq | XqPlus LdacQuality = Adaptive { ceiling } | Fixed(Connection | Standard | High) CapabilityState = Unknown | Observed { connection_epoch, endpoints } Stability = Unproven | StableInContext | Suspect | SuppressedForSession CodecState { compiled_local, runtime_enabled_local, advertised_remote, mutually_usable, requested_preference, policy_choice, negotiation_attempt, negotiated: Option<ActualPcmAndCodec>, requested_quality, observed_quality: Option<QualityObservation>, fallback_reason, fallback_count, stability, bluez_owner_epoch, bluealsa_owner_epoch, connection_epoch, sink_epoch }`

SBC XQ is a quality mode. Unknown advertised codecs may appear in diagnostics, not in the selectable menu. Per-device codec preferences belong in the service profile store; global default Auto belongs in app settings. Do not persist a second authoritative copy in AppModel.

### Version-specific discovery and selection
  - Read `org.bluealsa.Manager1` at `/org/bluealsa`: `Version`, `Profiles`,

`Codecs`. Filter `A2DP-source:` entries (actual D-Bus spelling, not the lowercase command-line profile argument). This is the enabled daemon inventory, not a full compiled-library inventory. Compare against a generated firmware codec manifest to identify disabled/missing/mismatched capabilities.
  - Subscribe to BlueZ ObjectManager and property changes for the selected

`Device1`. After profile discovery, enumerate its remote`org.bluez.MediaEndpoint1` sink objects. Read `UUID`, `Codec`, `Capabilities`, `Device`; parse vendor IDs from bounded codec blobs where necessary. In 5.79 source these properties are exported without a separate `Vendor` property, despite newer/general documentation discussing one.
  - Read BlueALSA ObjectManager PCMs, matching exact device, `A2DP-source` and

`Mode=sink`. Call that PCM's `GetCodecs()`, signature `a{sa{sv}}`. In 4.3.1 its `Capabilities`, `SupportedChannels`, `SupportedSampling` are already intersected with enabled local capabilities. Do not label this result a complete list of all codecs advertised by the headphones.
  - Unknown/missing SEP discovery is `Unknown`, not `remote supports only SBC`.

Existing actually negotiated SBC can remain a safe baseline when complete inventory is unavailable. A2DP UUID alone says nothing about optional codecs.
  - Compute a candidate. Ask playback to quiesce/close the old PCM first. Call

`SelectCodec(name, {Channels: byte, Sampling: uint32})` in 4.3.1. Use a validated codec configuration only where policy genuinely needs it; never disable conformance checks. In 5.0 the rate key is `Rate`, requiring an explicit version adapter, not speculative support.
  - A successful method return means accepted request, not proven audio. Observe

new/current `PCM1.Codec`, `CodecConfiguration`, `Format`, `Channels`, `Sampling`, then open exact PCM and confirm `Running` plus write progress. Reconfiguration can destroy/recreate PCM objects. Reject stale generation callbacks even if an object path is reused.
  - Report requested, policy-selected and negotiated values separately. If the

remote/stack instead establishes SBC, observe and validate SBC; never report the requested LDAC as active. Clear active state on owner/transport loss.

The 4.3.1 `GetCodecs` implementation deduplicates equal codec IDs and picks the first matching remote SEP for selection. Different endpoints with the same codec can have different capabilities. Keep raw remote observations separately; do not invent a union configuration that no individual endpoint accepts. If the adapter cannot select the desired endpoint safely, skip that candidate. This needs real multi-SEP fixtures and peer tests.

Sources: local `bluealsa-iface.xml`, `bluealsa-dbus.c::{ba_variant_populate_remote_sep, bluealsa_pcm_get_codecs,bluealsa_pcm_select_codec}`,`doc/org.bluealsa.PCM1.7.rst`, BlueZ `profiles/audio/a2dp.c::register_remote_sep` and [versioned BlueZ API](https://raw.githubusercontent.com/bluez/bluez/5.79/doc/org.bluez.MediaEndpoint.rst). Reborn must not register competing endpoints, acquire BlueALSA's media fd, run `bluetoothctl` parsers, or send vendor HCI commands to select a codec.

### Quality-control gap: honest implementation boundary

Codec/rate selection and actual-format observation are possible with existing standard interfaces. Per-device live LDAC quality/ABR ceilings, current bitrate and structured encoder-error/queue metrics are not available in stock 4.3.1. Do not invent D-Bus properties and write UI against them as if they existed.

For the full target, prefer a small reviewed/upstreamable **BlueALSA transport extension**, with validated per-PCM quality request, allowed ceiling, actual encoder mode/bitrate and aggregated errors. Keep ABR inside the encoder owner; Reborn supplies limits and policy, not per-packet decisions. A namespaced API must be feature-detected and versioned. Its implementation/locking/error-path review is separate future work. Newer 5.0 documentation alone does not supply this quality API either.

Without that extension, ship only behavior the stock interface can support: codec choice and bounded codec fallback; one fixed LDAC daemon quality in an explicit experimental image; `observed_bitrate=null` where not known. Do not advertise the complete adaptive-quality UX yet.

## 9. Auto policy — deterministic proposal, not an asserted quality ranking

### Eligibility precedes ranking`compiled ∩ runtime-enabled ∩ actually mutually usable ∩ distribution-approved ∩ platform-qualified-for-context ∩ supported PCM formats/rates ∩ acceptable resource budget minus session failures and per-device/context exclusions -> ranked candidates, always preserving conformant SBC fallback`

No legal/qualification waiver is inferred from manual mode. Laboratory firmware may have a visibly experimental allowlist; production Auto must not select it. On today's reviewed image the effective list is SBC only. No headphone profile has been supplied or observed in this audit.

Future initial policy profiles below apply **only after the named codec/mode passes all gates**. They express engineering tradeoffs, not a claim that AAC always sounds better than aptX or LDAC always sounds better than SBC.

| Context | Exact initial candidate order |
| --- | --- |
| First connection, no per-device history | Qualified SBC High baseline for this first session; observe device/transport. Do not silently experiment on a public user |
| Known peer, normal CPU budget, Wi-Fi off or qualified idle coexistence | LDAC capped Adaptive Standard (≤606/660) → aptX HD → AAC-LC target 256 → aptX → SBC High → SBC Conservative |
| Active Wi-Fi traffic or repeated scans, no strong peer coex result | AAC-LC target 256 → aptX → SBC High → SBC Conservative. Exclude HD/LDAC until their active-coexistence profile is qualified |
| Active Wi-Fi, peer has specific stable capped-LDAC coex record | LDAC capped Adaptive Standard → AAC-LC → aptX → SBC High → SBC Conservative; omit aptX HD unless separately coex-qualified, then place it after LDAC |
| Measured encoding/CPU pressure | If aptX is measured cheaper and qualified for this peer/context: aptX → SBC High → SBC Conservative; otherwise SBC High → SBC Conservative. Exclude AAC/LDAC/HD until their measured budget passes |
| User preference for an eligible codec | Requested codec/mode first; on failure remove failed candidate and use the relevant Auto list; publish explicit fallback reason |

The CPU-pressure row's aptX qualification does not prove reduced load just from the name; if no measurements establish a benefit, the row reduces to SBC High → Conservative. CPU budget is a filter, not an excuse to continuously switch a working codec. Existing stable sessions stay in place unless meaningful failure thresholds are crossed.

Why these defaults: capped LDAC offers a plausible wider-input quality path without automatically targeting 990; HD offers 24-bit input at moderate fixed payload; FDK AAC provides useful compatibility and lower payload if CPU allows; aptX is a plausible lower-cost alternative. Standard high-quality SBC is a serious fallback. Under congestion, payload and measured stability outrank codec branding. All ordering is revisioned and can be changed by qualification results.

For a peer offering SBC/AAC/LDAC, the first unknown session therefore uses SBC; after a compatible baseline and approved codec qualification, normal-context order is capped LDAC → AAC → SBC High → Conservative. That differs intentionally from blindly choosing 990 on first contact. During experimental qualification, an explicit laboratory profile may start with capped LDAC to exercise that path.

Precisely, persist `baseline_observed` after the 30-minute stable SBC observation defined below. At the next connection session, this permits the ranked list of already release-qualified optional codecs; do not interrupt the baseline session to upgrade. A known-good optional codec may lead the list when higher choices are unproven on that peer. A successful SBC baseline alone does not permanently pin Auto to SBC: only failures, exclusions or resource/context gates do that. This is deterministic device learning, not in-session exploration.

LDAC Connection Priority can be attempted once as a downgrade from capped Standard after persistent congestion; if it remains unstable, use the remaining Auto list. Do not assert that 303/330 is always acoustically preferable to well-encoded AAC. If AAC is already proven for this device/context, prefer that proven AAC fallback over introducing an unproven low-LDAC setting.

### Stickiness, source format and coexistence
  - Keep a demonstrated working choice for the session. Device history may promote

a stable choice above an unproven higher-ranked choice, but never restore a codec excluded by the new firmware's legal/hardware allowlist.
  - Treat Wi-Fi Off, ConnectedIdle, ActiveTraffic, Scanning and Unknown separately.

Current code does not expose a complete traffic-load classifier. Proposed classification uses existing scan state plus low-rate byte-counter deltas, not permanent packet capture. Unknown uses the conservative context.
  - Proposed active threshold: ≥128 kbit/s combined Wi-Fi traffic averaged over

10 s, or ≥2 scans in 60 s. Hold that context 60 s after the last qualifying event. These are initial testable policy constants, not measured RF limits.
  - One scan or Wi-Fi becoming connected must not interrupt healthy playback.

At most lower an available ABR ceiling; change codec only for meaningful instability or the next session. Never automatically turn Wi-Fi off.
  - Choose qualified source-family rate at session start, then hold it across

track changes. A 16-bit source does not require wider output, and a 24-bit source does not justify an unqualified RF mode.
  - No automatic 990/909 or 96-kHz promotion in the initial production policy.

Manual High remains experimental until separately qualified. Do not show a setting that the daemon cannot actually apply and verify.

## 10. Fallback state machine — PROPOSED`Disconnected -> AwaitProfile/Capabilities -> SelectCandidate -> Selecting ^ | | | failed/timeout v new connection <------- next candidate AwaitActualPCM | validate / open v RunningUnproven | stable observation v RunningStable | repeated failure v Exhausted <- no candidates <- Quiesce / Downgrade`

All deadlines use monotonic time. Key state by daemon-owner and connection generation; stale completion cannot reopen a previous device or revive playback after Stop. No busy wait, no per-packet logs, no hidden reconnect loop.

### Initial limits and observable causes

| Condition | Proposed response / threshold |
| --- | --- |
| Unsupported codec/configuration, malformed capabilities, unknown PCM format | Reject candidate immediately; record typed reason; no same-candidate automatic retry |
| SelectCodec timeout / transport startup failure | 5 s method deadline, 10 s actual-PCM/open deadline, within 45 s overall negotiation budget; try next candidate |
| Explicit encoder initialization failure | Candidate fails immediately; current API may expose only failed startup, so use that honest reason unless structured encoder signal exists |
| D-Bus service temporarily restarting | At most one same-candidate retry after owner reappears, with fresh epoch/inventory; 2 s backoff; counts within total attempt budget |
| One recoverable XRUN / transient write delay | Recover locally, record; no codec switch or persistent failure penalty |
| ≥3 distinct transport-attributed starvation/XRUN episodes in 60 s | Mark suspect; after 2 s settling allowance, bounded quiesce and downgrade. Coalesce symptoms within 2 s into one episode |
| Fatal transport write failure / PCM loss while device remains connected | Attempt next allowed candidate once resources are closed; do not wait for a cooldown on a dead stream |
| ≥2 unexplained disconnects within 120 s, each within 10 s of codec startup | Suppress candidate for session; next connection uses remaining candidates; exclude intentional disconnect/headphone power-off evidence |
| SD removal, decoder error, producer queue empty | Media/source failure, not codec evidence; pause/report through playback; no codec downgrade penalty |
| Wi-Fi scan, low RSSI, CPU spike, or no packet-loss telemetry | Not sufficient on its own to blame a codec |
| User Stop / Disconnect / radio Off / Forget | Cancel all codec timers and pending work; no automatic resume or re-pair |
| No usable candidate / SBC fails | Pause with one actionable "Bluetooth audio unavailable" state; no silent speaker playback and no repeated popups |

Stock Reborn cannot currently attribute all these events: it lacks structured BlueALSA encoder errors/queue telemetry and currently samples only a few PCM properties. Do not implement the threshold by scraping warning text or calling every decoder underrun a radio failure. Missing telemetry remains unknown.

### Bounded retries and no flapping
  - Construct at most six distinct codec/mode candidates, including SBC High and

Conservative. An LDAC Connection downgrade consumes a candidate slot; if adding it would exceed six after a congestion failure, remove fixed-rate aptX HD first, then aptX if AAC is already proven in that context. Never remove both SBC fallback modes to make room for optional experiments.
  - Each candidate gets one selection attempt per fallback session, except the

single service-restart retry above; the visited set survives rapid connection- epoch changes as described below. Maximum seven selection attempts across the fallback session. Initial startup and each later recovery episode have a 45-s deadline; entering recovery does not reset the session's candidate/attempt budget. Reserve the final 15 s for a conformant SBC startup: by 30 s stop launching optional candidates and select the untried SBC baseline. Conservative SBC is attempted if budget remains after a prompt High failure. Quiesce/reconciliation time is inside the same budget, not an unbounded prelude.
  - A D-Bus client timeout does not cancel the remote method. Never issue competing

SelectCodec calls while an earlier operation can still reconfigure the stream. Reconcile actual transport state/epochs after a bounded settling wait; accept a verified safe SBC transport or terminate as exhausted if safe serialization cannot be established. Ignore stale replies and do not extend the deadline.
  - While audio still works, no policy-driven codec reconfiguration more often

than once per 60 s. Same-transport ABR reduction may occur sooner; ABR remains inside BlueALSA with a fixed maximum. A fatal stream can fall through without waiting 60 s, but only to an untried candidate.
  - A failed codec/mode is not automatically promoted again in this session.

Track changes, scans and repeated UI refreshes do not reset the failure set.
  - Reconnects within five minutes retain the fallback session and attempt set.

A session ends after five minutes disconnected, explicit Forget, or a deliberate advanced "Retry preferred" operation. Reboot preserves the compact failure history, rather than immediately repeating a known bad high mode.
  - Ordinary reconnect to a previously successful, not failed/suppressed

current codec may reopen its newly observed PCM once per connection epoch, without another SelectCodec or promotion. This is a separate resume transition, not an opportunity to retry failed candidates. Revalidate format/gates and preserve paused intent. If the stack negotiates an allowed lower fallback, observe it honestly instead of immediately forcing the old higher codec. A failed resume enters the remaining fallback list; repeated reconnects are bounded by the connection-owner contract below.
  - A user-requested Retry creates a fresh bounded budget; it cannot race with an

existing negotiation. Background upgrade probing is excluded from version one.
  - Persistent two-failure evidence suppresses that codec/context for the next

three connection sessions; a user can explicitly retry. Count sessions rather than trusting Y2's currently unreliable wall clock. A software/capability fingerprint change marks history stale rather than treating it as permanent.

For a finite ordered candidate vector `C`, record each attempt in a monotone visited set `V`; automatic fallback always chooses from `C \ V`, never removes an element from `V`, and never upgrades. Thus one session cannot oscillate LDAC → SBC → LDAC. Resuming the current nonfailed codec is not a promotion or a fresh fallback selection. This is a design invariant, not a proved property of today's nonexistent Auto implementation; test vectors are in the companion file.

### Connection retry and audio recovery must not fight

[Y2 reconnect helper](https://github.com/SchulzCode/Y2Linux/blob/main/tools/connectivity/reconnect.c) is already the preferred-device connection owner; BlueZ built-in reconnect is disabled. It makes bounded-rate requests but can keep trying once per minute indefinitely. Do not add another independent Device1.Connect loop inside CodecPolicy.

The full design needs a narrow coordination contract: codec reconfiguration, intentional disconnect and exhausted-audio recovery can inhibit helper retries; only the connection owner performs bounded profile reconnect requests. An exhausted codec session stays exhausted even if the current helper reconnects the link. Reconnection alone does not reset codec attempts. A transient app-only lease must expire safely on crash; explicit user radio/disconnect intent must remain authoritative. This contract is currently missing and blocks a claim of complete end-to-end bounded fallback.

Initial proposed connection-owner limit: at most two automatic profile reconnect requests for one unexpected loss, 10-s request deadline, 2-s backoff and a 25-s total recovery budget. These limits are separate from the codec-selection budget and are not implemented by today's helper. Do not overlap requests after a client timeout; reconcile a late remote completion or stop. Exhaustion waits for explicit user Connect or a genuinely new peer-initiated connection, not a once-per-minute timer forever. Known user/headphone-off intent bypasses automatic retries. Qualify these deadlines with real devices before adoption.

Fresh pairing also must explicitly establish the user's approved trust policy. Do not trust every discovered device. The helper requires paired + trusted + AudioSink; Reborn's current pairing code does not set Trusted. Qualify fresh onboarding without preconfigured owner bonds.

### Playback continuity and volume safety

Close/quiesce the old sink before reconfiguration, invalidate old PCM jobs, then open the observed new sink. Preserve queue identity, track, user pause state, DSP settings and logical position. Hold only a bounded amount of canonical PCM; do not decode minutes ahead during negotiations. Reconfigure the final converter, not the decoder/DSP authority. Do not replay stale old-rate buffers.

Codec changes in Classic A2DP are not guaranteed sample-continuous. A short audible gap may be unavoidable; no claim of seamless fallback. Do not guess exact heard position from bytes merely queued to Bluetooth. Use the existing playback clock/delay contract and expose interruption diagnostics. Rate changes at ordinary queue boundaries should be avoided so gapless is not unnecessarily broken. Existing `Runtime::load` probe-before-worker-stop behavior and sink generation/cancellation tests deserve attention before expanding this path.

On genuine peer disappearance preserve paused intent; never start wired output automatically at an unsafe volume. Current core changes Bluetooth output to Wired and pauses on `BluetoothDisconnected`; deliberate codec reconfiguration must not be mistaken for this user-visible unplug event.

## 11. Bounded per-device persistence — PROPOSED

Store under Reborn's existing private state root, not BlueZ's bond/key files. One versioned atomic JSON record set, maximum 32 paired devices, **six codec entries/device**, two qualification contexts (quiet/congested), saturating small counters. Evict forgotten/unpaired entries first, then least recently used.

Fields: schema/policy revision; private paired-device identity; capability and firmware/encoder fingerprints; optional manual preference; last stable codec/rate/quality ceiling per context; stable-session count; capped failure count; `baseline_observed`; remaining suppressed-session count; latest bounded reason code. Do not store packet histories, media titles, SSIDs, bond keys or raw calibration. Unknown vendor capability blobs need not be persisted.

An initial stable observation means 30 minutes of progressing playback without codec-attributed faults in the recorded context. It permits a device-history hint, not product qualification. High-quality mode history must be based on observed mode, not just requested mode. Do not manufacture "highest stable 660" while ABR feedback is unavailable.

Write on changed preference, a new stable milestone, or session termination; coalesce automatic writes to at most once per five minutes, skip unchanged content, and flush a pending summary during orderly shutdown. Atomic temporary file + rename + appropriate file/directory sync; no per-packet/XRUN writes. Corrupt/unsupported schema resets learning to Unknown/Auto safely, without removing bonds or inventing negotiated codec state. Migration must preserve an unsupported manual preference as unavailable, not silently relabel it active.

## 12. Observability and UI — PROPOSED

Use the existing bounded event ring/structured logger, not another telemetry system. Events: inventory ready/mismatch, remote capability snapshot, candidate selection, attempt started/completed/timed out, actual codec/format changed, quality ceiling changed, transport lost/restored, fallback and exhausted. Fields include device pseudonym, session/sink epochs, correlation ID, codec, rate/channels/format, request vs observation, bounded reason code and elapsed time. Aggregate underruns/blocked writes periodically; never log audio packets. Logs stay in RAM by default; diagnostic persistence is deliberate and bounded.

Packet loss is `null/not_observable` unless an actual reliable source supplies it. Local `TIOCOUTQ`, RSSI and ALSA underruns are not packet-loss percentage. Protect Bluetooth MACs/device names in exported bundles; no bond keys, passkeys or raw SDP/HCI payload capture by default.

The following command/schema is not implemented today:`rebornctl bluetooth status --json`

Illustrative hypothetical state, not a captured Y2 result:`{ "schema": 1, "device": "paired-device-1", "local_enabled": ["sbc", "aac", "ldac"], "remote_capabilities_state": "observed", "remote_codecs": ["sbc", "aac", "ldac"], "mutually_usable": ["sbc", "aac", "ldac"], "preference": "auto", "policy_choice": "ldac", "negotiated": {"codec": "aac", "rate_hz": 48000, "channels": 2, "format": "s16le"}, "requested_quality": null, "observed_bitrate_bps": null, "stability": "suppressed_ldac_for_session", "fallback_count": 1, "latest_fallback_reason": "transport_start_timeout" }`

Actual current tools are `rebornctl status --json`, `audio --json`, logs/events, and radio on/off/scan. The parser currently rejects `bluetooth status`; do not present the proposed command as an installation check that already works.

Normal UI: Codec: Auto and Active: SBC/AAC/LDAC, from observed state only. Display "Negotiating" or "Unavailable" when appropriate. If bitrate is not observable, use "LDAC · Adaptive" only when adaptive mode itself is confirmed; otherwise simply "LDAC". Never synthesize a live kbps value from preferences.

Manual menu includes only compiled, runtime-enabled, release-approved codecs. Show an unsupported-on-this-headphone choice disabled with explanation, or reject it without disturbing working playback. If a previously saved preference is unavailable, preserve it as an unavailable preference and visibly show the actual fallback in Audio Info. Manual means "prefer", not "lie about strict success". Keep ordinary fallback quiet—no popup. Show one warning only when no usable Bluetooth audio connection can be established. Advanced diagnostics may explain why Auto chose differently.

## 13. Build changes required later, not made here``````

| Candidate | Required deliberate integration |
| --- | --- |
| SBC policy | Preserve libsbc and mandatory SBC; explicit normal quality/role; add inventory/format observation and tests. Do not globally constrain fallback to XQ |
| AAC | Select pinned FDK-AAC and legal assets; explicit --enable-aac; approved LC/profile/bitrate settings; verify ARM ELF dependencies and encoder behavior |
| aptX/HD | Prefer evaluating a pinned libfreeaptx package with --with-libfreeaptx --enable-aptx --enable-aptx-hd; adjust existing recipe branch so libopenaptx is not simultaneously selected; preserve source/license hashes |
| LDAC | Add pinned source-side libldac/ldacBT encoder+ABR package, hashes/licenses/NOTICE and --enable-ldac; no decoder binary dependency; explicit daemon codec enablement and qualification-gated mode |
| XQ | No new codec library; needs safe per-transport quality/config policy, baseline fallback preserved and real peer tests |
| MPEG/Opus/FastStream/LC3plus | Keep disabled despite independently installed decoder libraries; no user-value case strong enough for initial release |
| LHDC / BlueALSA 5.0 | Separate upgrade/ABI/binary-license project, not prerequisite for sensible SBC/AAC/aptX/LDAC policy |

Explicitly enumerate approved configure enables/disables and runtime codecs; never use `--all-codecs`. In 4.3.1 some optional codecs are not runtime-enabled by default even if compiled: check Manager1.Codecs rather than assuming library presence. Generate a read-only codec manifest from actual configured outputs, not hand-written marketing metadata. Record encoder versions, options, license status, quality profile and qualification ID with the firmware artifact.

Cross-build assertions must reject unexpected encoders, format adapters, missing source/license files and disagreement among manifest, configure output, ELF dependencies and runtime inventory. No downloads at playback time. No broad FFmpeg encoder enablement; file AAC/MP3/Opus decoding remains independent.

## 14. Qualification, release categories and next sequence

The full [test and physical matrix](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fbluetooth-codecs%2F2026-09-22-evidence-and-tests.md) covers remote capabilities, CPU/memory/thermal/battery, four Wi-Fi states, LDAC fixed/adaptive modes, lifecycle/failure injection and precision checks. All physical codec qualification remains outstanding; host policy tests cannot prove radio, CPU, battery or headphone behavior.

| Category | Decision |
| --- | --- |
| SHIP recommendation, after baseline qualification and distribution review | SBC with normal high quality and conservative fallback. Current public Bluetooth release qualification: none |
| EXPERIMENTAL, qualify one at a time | AAC, aptX, aptX HD, LDAC 303/330 and 606/660, capped adaptive when interface exists; SBC XQ. AAC/aptX/HD may graduate after gates |
| EXPERIMENTAL, lower priority / never initial Auto | LDAC 909/990, LDAC 88.2/96 kHz, SBC XQ+; higher radio/CPU/interoperability exposure |
| DO NOT SHIP initial Reborn | LHDC, LC3plus, MPEG/MP3 A2DP, Android/PipeWire Opus extensions, FastStream, aptX LL/TWS; low proven value or major integration/distribution gaps |
| Not realistically supported by present product stack | aptX Adaptive/Lossless; no suitable encoder/transport integration and proprietary ecosystem requirements |
| IMPOSSIBLE / HARDWARE LIMITED on present controller interface | Standard LE Audio/LC3 CIS/BIS and Auracast |

Proposed correction sequence:
  - Close SBC baseline evidence and the pairing/trust/reconnect ownership gap.

Refresh the Y2Linux standing milestone audit with actual evidence before any production-scope expansion; this document does not activate a milestone.
  - Add typed observations and exact PCM-format contract; expose truthful existing

SBC state. Add fake-bus stale-generation/malformed/unsupported tests.
  - Add the pure policy plus bounded negotiation coordinator, SBC conservative

fallback and compact persistence. Prove no flapping/exhaustion behavior.
  - Resolve exact dependency/distribution decisions; qualify optional codecs one

at a time, starting with the actual owner's available headphone capabilities. AAC is high user value; aptX is an attractive lower-CPU comparison; measure.
  - Only then add LDAC quality extension/capability telemetry if the platform

results justify it. Keep a small codec menu and one pipeline.
  - Produce a candidate through the existing production packaging workflow, with

explicit codec manifest/source/legal payload and test identities. Stop for owner-controlled physical installation/qualification—never touch protected partitions or calibration as part of codec work.

**No implementation, commits, new production artifact or installation occurred in this audit.** The next useful external input is real headphone capability and baseline playback evidence, not permission to enable every encoder.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
