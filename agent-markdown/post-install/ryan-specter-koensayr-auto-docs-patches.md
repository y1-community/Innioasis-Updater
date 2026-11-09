---
title: "Patch Reference - Innioasis Updater"
description: "Patch Reference Byte-level reference for the patches currently shipped by this repo. Each section describes what the patch ships today offsets, before / after bytes, rati"
language: "en"
source: "https://innioasis.app/post-install/ryan-specter-koensayr-auto-docs-patches.html"
---

# Patch Reference - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y1&software=koensayr-y1)

Post-install setup · Koensayr · Y1

# Patch Reference

A Y1 custom Software maintained by the community.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y1&software=koensayr-y1)[Install guide](../guide.html?model=Y1&software=koensayr-y1)

# Patch Reference

Byte-level reference for the patches currently shipped by this repo. Each section describes what the patch ships today (offsets, before / after bytes, rationale, ICS status). For the commit-by-commit evolution that produced the current shape — including reverts, dead-end attempts, and the empirical evidence that motivated each behavior change — see [`INVESTIGATION.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FINVESTIGATION.md) and `git log`. Spec citations follow the discipline in [`BT-COMPLIANCE.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FBT-COMPLIANCE.md) §0.

## Patch ID Legend````````````````````````````````````````````````````````````````````````````````

| ID(s) | Binary | Site / effect |
| --- | --- | --- |
| V1, V2, V3, V4, V5, V6, V7, V8, S1, P_PN0, P1, M1, M2, M3, M4, M5, M6, M8, M10 | mtkbt | SDP shape (AVRCP 1.0→1.3, AVCTP 1.0→1.2, A2DP/AVDTP 1.0→1.3, sig 0x0c→0x02 alias, internal activeVersion 10→14 to route the dispatcher to the AVRCP 1.3 served record, drop AdditionalProtocolDescriptorList Browse-PSM advertisement (AVRCP 1.4 §8 Table 8.2 introduced; absent from AVRCP 1.3 §6 Table 6.2), clear stock GroupNavigation feature bit (Y1 doesn't implement the Group Navigation PASSTHROUGH PDUs), ServiceName-for-SupportedFeatures swap, dormant write of a 0x0102 ProviderName " " descriptor into an unused SDP-data gap (no entry slot currently references it — the AVRCP 1.3 TG record's 6-slot entry table is fully occupied by spec-mandatory + CT-compatibility-critical attributes), force-PASSTHROUGH-emit op_code dispatch, RegNotif INTERIM/CHANGED dispatch cmp constant widened from 1 to 0x0F so wire ctype matches the JNI trampoline's reasonCode plus a paired NOP of the hardcoded CHANGED-ctype write so the response builder's CHANGED branch becomes a pure pass-through for any non-0x0F AV/C ctype, three NOPs across the two outbound-frame builders that remove the chip-readiness list-contains check on each path + the chip-busy flag SET on the multi-frame path so the matching CHECK never trips, a code-cave trampoline in Path B that conditional-stores chan[+0x29] so outbound responses echo the inbound AV/C transId per AVRCP 1.3 §4.2.1 instead of clobbering to 0, and a NOP of the AVRCP_HandleA2DPInfo info=1 disconnect call so the AVCTP control channel survives AVDTP CLOSE/REOPEN cycles per AVRCP 1.3 §4 transport independence). |
| R1, T1, T2 stub, extended_T2, T4, T5, T_charset, T_battery, T_continuation, T6, T8, T9, U1 | libextavrcp_jni.so | Trampoline chain in _Z17saveRegEventSeqIdhh + LOAD #1 page-padding extension + uinput EV_REP NOP. Synthesises AVRCP 1.3 metadata responses directly from C, bypassing the no-op Java AVRCP TG. |
| F1, F2 | MtkBt.odex | getPreferVersion()=14 to unblock 1.3+ command dispatch through MtkBt's Java layer; disable() resets sPlayServiceInterface. |
| odex cardinality NOPs (×2) | MtkBt.odex | NOP the if-eqz v5 cardinality gates in BTAvrcpMusicAdapter.handleKeyMessage for events 0x02 (TRACK_CHANGED, sswitch_1a3) and 0x01 (PLAYBACK_STATUS_CHANGED, sswitch_18a) so the JNI natives fire on every metachanged / playstatechanged broadcast. Pairs with T5 / T9 in libextavrcp_jni.so. |
| A, B, C, E, H, H′, H″ | com.innioasis.y1*.apk | Smali edits: A/B/C for Artist→Album navigation; E for discrete PASSTHROUGH PLAY/PAUSE/STOP/NEXT/PREVIOUS routing per AV/C Panel Subunit Spec op_id table; H for foreground-activity propagation of KEYCODE_MEDIA_PLAY/PAUSE/STOP/NEXT/PREVIOUS; H′ for the same propagation in BasePlayerActivity (which overrides dispatchKeyEvent and bypasses BaseActivity); H″ adds a repeatCount > 0 → silent consume filter to both H and H′ so framework-synthesized key repeats from InputDispatcher::synthesizeKeyRepeatLocked don't trigger long-press FF/RW handlers. |
| AH1 | libaudio.a2dp.default.so | A2dpAudioStreamOut::standby_l cond-flip: beq 8684 → b 8684 at file offset 0x000086ab so silence-timeout standby skips a2dp_stop unconditionally. Keeps the AVDTP source stream alive across pauses; matches AVDTP 1.3 §8.14 / §8.15 expectation that PAUSED leaves the stream paused-but-up. |
| K1 | usr/keylayout/AVRCP.kl | Row 201 (KEY_PAUSECD) MEDIA_PLAY_PAUSE → MEDIA_PAUSE. Undoes stock AOSP's 2010-era coalescing of discrete PASSTHROUGH 0x46 PAUSE into the toggle keycode, restoring AVRCP 1.3 §4.6.1 + ICS Table 8 discrete-PAUSE semantics for CTs that send 0x46 (vs. 0x44 PLAY-as-toggle). Row 200 (KEY_PLAYCD → MEDIA_PLAY) unchanged. |
| su | /system/xbin/su | Setuid-root su binary installed by --root. |

## `patch_mtkbt.py`

Nine byte patches against stock `/system/bin/mtkbt`. Seven reshape the served SDP record so a peer CT engages with AVRCP 1.3 COMMANDs (per AVRCP 1.3 §6 Service Discovery Interoperability Requirements + ESR07 §2.1 / Erratum 4969 clarifying AVCTP version values), one reroutes inbound VENDOR_DEPENDENT frames into the JNI msg-519 emit path so the trampoline chain can respond, and one is a best-effort dispatch alias for AVDTP signal 0x0c.

The mtkbt daemon ships two physical AVRCP TG SDP record templates in `.data.rel.ro`. The internal `activeVersion` field selects which is served on the wire: stock = 10 (legacy 1.0 record), V6 → 14 (AVRCP 1.3 record). V1/V2/S1 patch the legacy record (kept for the fall-through path); V7/V8 patch the AVRCP 1.3 record (where V6 routes the daemon by default) so it conforms to AVRCP 1.3 §6 Table 6.2 SDP record shape — no AdditionalProtocolDescriptorList (a 1.4-introduced attribute per AVRCP 1.4 §8 Table 8.2), Group Navigation feature bit cleared (the bit exists in 1.3 §6 Table 6.2 but Y1 doesn't implement the Group Navigation PASSTHROUGH PDUs). P_PN0 writes a `0x0102 ProviderName " "` SDP descriptor into a previously-unused gap in the data area; the descriptor is currently dormant because the AVRCP 1.3 TG record's entry table is hard-capped at 6 slots, all occupied by spec-mandatory attributes. `0x0005 BrowseGroupList={PublicBrowseRoot}` is retained — empirically required by some CTs to take the full AVRCP-setup CT path rather than a passthrough-only fallback.

V1 — AVRCP 1.0 → 1.3 at file `0x0eba58` (1 byte): `0x00` → `0x03`. LSB of the served Group D ProfileDescList Version field.

V2 — AVCTP 1.0 → 1.2 at file `0x0eba6d` (1 byte): `0x00` → `0x02`. LSB of the served Group D ProtocolDescList AVCTP Version field.

V3 — A2DP 1.0 → 1.3 at file `0x0eb9f2` (1 byte): `0x00` → `0x03`. LSB of the served A2DP Source ProfileDescList Version field. Per A2DP 1.3 §5.3 Figure 5.1 the Mandatory version value is `0x0103`.

V4 — AVDTP 1.0 → 1.3 at file `0x0eba09` (1 byte): `0x00` → `0x03`. LSB of the served A2DP Source ProtocolDescList AVDTP Version field. Per A2DP 1.3 §5.3 the Mandatory AVDTP version is `0x0103`. Pairs with V3 — peers consult our advertised AVDTP version before GAVDP setup per A2DP §3.1, so both bumps ship together.

V5 — AVDTP sig 0x0c dispatch alias at file `0x0aa834` (2 bytes): halfword `0x0660` → `0x0083`.````````````

|  | bytes | TBH halfword | target |
| --- | --- | --- | --- |
| before | 60 06 | 0x0660 | 0xab4de (sig 0x0c stub — always returns BAD_LENGTH error) |
| after | 83 00 | 0x0083 | 0xaa924 (sig 0x02 GET_CAPABILITIES handler) |

Edits one entry of the AVDTP signal dispatcher's TBH jump table at file `0xaa81e`. Position 11 (`sig_id - 1` for sig 0x0c) is repointed from the stub at `0xab4de` to the full GET_CAPABILITIES handler at `0xaa924`.

This is a structural workaround, not a real GET_ALL_CAPABILITIES implementation — the response we emit is the sig 0x02 capability list, which per AVDTP 1.3 §8.8 is a wire-compatible subset of the sig 0x0c response (no extended Service Capabilities like DELAY_REPORTING / RECOVERY / MULTIPLEXING / HEADER_COMPRESSION). For an SBC-only Source this matches what we'd advertise anyway. Closes GAVDP 1.3 ICS Acceptor Table 5 row 9 on paper.

Wire-correct by decoupling: the response builder is `fcn.000ae418` (calls `L2CAP_SendData` at file `0xae58e`), and byte 1 of the response frame (sig_id) is read at `0xae480` from `txn->[0xe]` — the per-channel transaction state populated by the request parser at RX time. The dispatcher and per-signal handlers do not write `txn->[0xe]`. So a sig 0x0c request lands in the GET_CAPABILITIES handler post-V5, but the response frame still emits `sig_id=0x0c` matching the request. Payload is a V13 §8.8 subset valid for an SBC-only Source. Full walk-through in `INVESTIGATION.md`.

V6 — internal `activeVersion` 10 → 14 at file `0x10dca` (2 bytes):````````

|  | bytes | mnemonic |
| --- | --- | --- |
| before | 0a 23 | movs r3, #0xa |
| after | 0e 23 | movs r3, #0xe |

The stock activation handler at `fcn.00010d00` hardcodes the activeVersion field stored to the avrcp_state struct's `+0xb86` offset. The downstream SDP record builder at `fcn.00038ab8` reads this byte and dispatches: `v != 0xd && v != 0xe` → legacy AVRCP 1.0 served record (logs `AVRCP sdp 1.0 target role`); `v == 0xd || v == 0xe` → AVRCP 1.3 served record (logs `AVRCP sdp 1.3 target role`). V6 changes the immediate from 10 to 14 so the daemon takes the latter branch by default, aligning the served record with the version F1 surfaces to the Java layer.

V7 — `0x000d AdditionalProtocolDescList` → `0x0100 ServiceName` at file `0x0f9798` (12 bytes):````````````````````

|  | bytes | shape |
| --- | --- | --- |
| before | 0d 00 14 00 12 ba 0e 00 00 00 00 00 | attr=0x000d, len=0x14, ptr=0x0eba12 (→ AdditionalProtocolDescList: L2CAP / PSM 0x001b Browse + AVCTP) |
| after | 00 01 11 00 ce b9 0e 00 00 00 00 00 | attr=0x0100, len=0x11, ptr=0x0eb9ce (→ 25 0f "Advanced Audio0") |

The stock AVRCP 1.3 served record advertises attribute `0x000d AdditionalProtocolDescriptorList` carrying the AVRCP Browse PSM `0x001b`. AdditionalProtocolDescriptorList is introduced in AVRCP 1.4 §8 Table 8.2 (conditional on SupportedFeatures bit 6 "Supports browsing"); AVRCP 1.3 §6 Table 6.2 does not list it. V7 swaps this entry slot for a `0x0100 ServiceName` entry pointing at the same "Advanced Audio" string S1 reuses for the legacy record. Net wire effect: drops the Browse advertisement, restores ServiceName presence so the served record matches AVRCP 1.3 §6 Table 6.2 shape.

V8 — `SupportedFeatures` 0x0021 → 0x0001 at file `0x0eba4e` (1 byte):````

|  | byte | bits set |
| --- | --- | --- |
| before | 21 | bit 0 (Category 1: Player/Recorder) + bit 5 (Group Navigation) |
| after | 01 | bit 0 only |

LSB of the AVRCP 1.3 served record's SupportedFeatures `uint16` (byte stream `09 00 21` → `09 00 01` at `0x0eba4c`). AVRCP 1.3 §6 Table 6.2 defines bit 5 as "Group Navigation" (conditional on bit 0 Category 1 being set) with the note "the bits for supported categories are set to 1; others are set to 0." Y1's stock advertises bit 5 set but ships no Group Navigation PASSTHROUGH handler; V8 clears it so the advertised mask is 0x0001 (Category 1 only), matching what's actually implemented. Bits 6-15 are RFA in 1.3 Table 6.2; bit 6 became "Supports browsing" in AVRCP 1.4 §8 Table 8.2.

P_PN0 — write SDP TEXT_STR_8 " " at `0x0eb938` (4 bytes, dormant):````````

|  | bytes | shape |
| --- | --- | --- |
| before | 00 00 00 00 | (unused padding inside the SDP data area) |
| after | 25 02 20 00 | SDP TEXT_STR_8 ds + len=2 + ' ' + '0' |

Writes a `0x0102 ProviderName " "` SDP descriptor into a 36-byte zero-padded gap between two unrelated SDP data blocks. The descriptor is dormant — no entry slot in any record currently references it. The AVRCP 1.3 TG record's entry table is hard-capped at 6 slots, all currently occupied by spec-mandatory attributes including `0x0005 BrowseGroupList={PublicBrowseRoot}` (empirically required by some CTs to take the full AVRCP-setup path rather than a passthrough-only fallback). The descriptor bytes are left in place so they're ready if a non-destructive way to add a 7th entry slot is found in the future.

S1 — `0x0311 SupportedFeatures` → `0x0100 ServiceName` at file `0x0f97ec` (12 bytes):``````````````````

|  | bytes | shape |
| --- | --- | --- |
| before | 11 03 03 00 59 ba 0e 00 00 00 00 00 | attr=0x0311, len=3, ptr=0x0eba59 (→ uint16 0x0001) |
| after | 00 01 11 00 ce b9 0e 00 00 00 00 00 | attr=0x0100, len=0x11, ptr=0x0eb9ce (→ 25 0f "Advanced Audio0") |

Patches the same entry-slot swap on the legacy AVRCP 1.0 served record (the fall-through served when `activeVersion != 0xd && != 0xe`). Reuses the existing "Advanced Audio" SDP-encoded string from mtkbt's A2DP record. Cost: the legacy served record loses the `0x0311 SupportedFeatures` attribute. CTs in our test matrix engage with the record without it.

P1 — force PASSTHROUGH-emit branch at file `0x144e8` (2 bytes):````````

|  | bytes | mnemonic |
| --- | --- | --- |
| before | 30 2b | cmp r3, #0x30 |
| after | 1e e0 | b.n 0x14528 |

Replaces the first comparison in fn `0x144bc`'s op_code dispatch with an unconditional branch to the PASSTHROUGH-emit branch at `0x14528` (which ends with `bl 0x10404`, the function that emits msg 519 CMD_FRAME_IND to the JNI socket). Every AV/C frame flows through the emit path. Cost: VENDOR_DEPENDENT bytes get interpreted in PASSTHROUGH-shaped fields, so mtkbt's mid-stack response may be malformed — but the JNI trampoline chain takes over before that matters.

M1 — RegNotif INTERIM/CHANGED discriminator: cmp ctxt[8] against 0x0F at file `0x12230` (1 site, 2 bytes):``````````

| site | bytes (before → after) | mnemonic |
| --- | --- | --- |
| 0x12230 | 01 29 → 0f 29 | cmp r1, 1 → cmp r1, 0xF |

Stock mtkbt's RegNotif response packetFrame builder dispatch at fn `0x121d8` reads `ctxt[8]` and compares against `1` to choose between INTERIM (ctype `0x0F` at `0x12238`) and CHANGED (ctype `0x0D` at `0x12244`) branches. The JNI's `btmtk_avrcp_send_reg_notievent_*_rsp` helpers in `libextavrcp.so` marshal the reasonCode argument (REASON_INTERIM=`0x0F` / REASON_CHANGED=`0x0D`) into IPC payload byte 8 — verified by the `strb.w r7, [sp, #12]` encoding (bytes `8d f8 0c 70`) at the cardinality=0 path of every helper, where sp+12 maps to payload+8 (the helper's 40-byte buffer starts at sp+4). Stock mtkbt reads the correct byte but compares against `1`, so `0x0F` and `0x0D` both fail the cmp and the dispatch always lands on the CHANGED branch — wire ctype is `0x0D` for every RegNotif response regardless of which reasonCode the trampoline passes.

M1 widens the cmp constant from `1` to `0x0F`. After M1: `ctxt[8] == 0x0F` (T2 / extended_T2 / T8 first-response INTERIM arms) → INTERIM branch → wire ctype `0x0F` INTERIM. `ctxt[8] != 0x0F` (T5 / T9 edge emits, where r2 = REASON_CHANGED = `0x0D`) → CHANGED branch → wire ctype `0x0D` CHANGED. Spec-compliant per AVRCP 1.3 §5.4.2 (INTERIM on first response per registration, CHANGED on subsequent value updates without re-registration).

End-to-end byte chain: IPC msg=544 → `fcn.00067768` (sets ctxt ptr at msg+0x1c) → `fcn.000518ac` case 44 → `fcn.00012478` event_id tbb → per-event response builder → `fcn.000121d8` (M1 site at `0x12230`) → `fcn.00011894` strb ctype to packetFrame[0xb] → `fcn.0000f0bc` queue → `fcn.0000ef08` strb to wire `buf[0]`. Full radare2 trace in `docs/INVESTIGATION.md`.

M8 — Preserve AVCTP across AVDTP CLOSE: NOP info=1 disconnect at file `0xfa38` (1 site, 4 bytes):``````````

| site | bytes (before → after) | mnemonic |
| --- | --- | --- |
| 0xfa38 | 01 f0 a0 fb → 00 bf 00 bf | bl 0x1117c → nop ; nop |

`AVRCP_HandleA2DPInfo` (`fcn.0xf8e0`) is mtkbt's notification sink for A2DP stream-state changes. The `info_id == 1` path ("A2DP lost") logs `AVRCP: disconnect because a2dp is lost` and calls `fcn.0x1117c` — the AVRCP per-handle cleanup routine that emits `L2CAP DisconnectReq` on the AVCTP control channel + any remaining AVRCP-owned channels. The same routine is also called from the `info_id == 0` ("a2dp connected with other device") branch at `0xf9b8`; M8 only NOPs the info=1 site so multi-device A2DP collisions still tear AVRCP down appropriately.

Wire trigger:
  - CT sends AVDTP `CLOSE` (sig 0x08, ACP_SEID=1) on cid 0x42 — normal stream teardown per AVDTP 1.3 §8.14 (Stream Release / Close Stream Command).
  - mtkbt's AVDTP upper layer tears down PSM 0x19 L2CAP channels; `[AvdtpSigMgrConnCallback]AVDTP_CONN_EVENT_DISCONNECT stat:5` fires.
  - mtkbt calls `AVRCP_HandleA2DPInfo(1, 0)` — wrongly treating CLOSE as link loss rather than the normal stream-state transition.
  - Pre-M8: `info=1` path calls `fcn.0x1117c` which emits `DisconnectReq` for the AVCTP control channel.
  - CT then reconnects everything on the next AV/C command, issuing a fresh `GetCapabilities` that resets `g_avrcp_req_event_database` via `libextavrcp_jni.so`'s `clear_event_database` in `T1_extended`. The post-reset session has no per-event TIDs, so subsequent `T5` / `T9``CHANGED` emits go silent and the CT's UI freezes on stale metadata.

After M8, step 4 is a no-op; the AVCTP control channel survives the audio stream cycle. Spec basis: AVRCP 1.3 §4 states the AVCTP signaling channel for AVRCP is independent of any AVDTP audio channel — CTs are allowed to cycle audio without disturbing AVRCP. True ACL link loss (peer powered off / out of range) is still caught by the baseband link-supervision timeout independently of this software path, so the failure mode for genuine disconnection is preserved.

End-to-end RE walkthrough lives in `docs/INVESTIGATION.md`.

M6 — RegNotif CHANGED-branch ctype pass-through: NOP movs r1, 0xD at file `0x12244` (1 site, 2 bytes):``````````

| site | bytes (before → after) | mnemonic |
| --- | --- | --- |
| 0x12244 | 0d 21 → 00 bf | movs r1, 0xD → nop |

Companion to M1. After M1 widens the discriminator cmp from `cmp r1, 1` to `cmp r1, 0xF`, the response builder at `fcn.0x121d8` reads `ctxt[8]` and branches:
  - `ctxt[8] == 0x0F` → INTERIM branch → `movs r1, 0xF` at `0x12238` sets wire ctype `0x0F`
  - `ctxt[8] != 0x0F` → CHANGED branch → `movs r1, 0xD` at `0x12244` hardcodes wire ctype `0x0D`

M6 NOPs the `movs r1, 0xD` so the CHANGED branch retains whatever value `ctxt[8]` held from `ldrb r1, [r4, 8]` at `0x1222e`. Net wire behaviour:
  - `ctxt[8] == 0x0F` (INTERIM emit) → wire `0x0F` (unchanged from M1; M6's NOP is in the OTHER branch)
  - `ctxt[8] == 0x0D` (CHANGED emit) → wire `0x0D` (r1 retains 0x0D from `ldrb`; identical to stock CHANGED behaviour, only the instruction that produces it changed)
  - `ctxt[8] == any other valid AV/C ctype` → that value reaches the wire as AV/C ctype byte 0

Pure no-op for the existing 0x0F / 0x0D call sites in `_trampolines.py` (T2, extended_T2, T5, T8, T9, T_papp) and `libextavrcp.so`'s `reg_notievent_*_rsp` helpers. M6 only changes wire behaviour when a future caller deliberately passes a non-0x0F-and-non-0x0D AV/C ctype value via the helper's `reasonCode` argument.

End-to-end static verification of the chain (no ctype filtering anywhere downstream of `packetFrame[0xb]`) lives in `docs/INVESTIGATION.md`.

M2 — Outbound-frame drop bypass: NOP gate 1 list-contains check at file `0x6d06e` (1 site, 2 bytes):``````````

| site | bytes (before → after) | mnemonic |
| --- | --- | --- |
| 0x6d06e | 37 d0 → 00 bf | beq 0x6d0e0 → nop |

Stock `fcn.0x6d048` (outbound-frame builder reached from `fcn.0xf0bc → fcn.0xed50 → fcn.0x6d048 → fcn.0x6df20 → fcn.0xae5e4` for short-frame AVRCP responses under the L2CAP MTU — PSTAT, REACHED_END/START, batt status) calls `fcn.0x6ccdc` (doubly-linked-list contains check) against `g_active_conn_list` at `*(0xf99XX)`. If the conn isn't in the list, returns `0xd` and skips the wire-frame build; the caller (`fcn.0xf0bc`) treats this as success via `cmp r5, 2; bne 0xf208`.

M2 NOPs the `beq 0x6d0e0`, so the function unconditionally builds the wire frame and tail-calls `fcn.0x6df20`. The list state was a chip-readiness heuristic that empirically gated nothing measurable. The downstream send chain handles its own per-channel state, so removing this gate is safe; net wire-side delivery unchanged in observed captures, but the gate's removal eliminates one source of "did this CHANGED reach the wire?" ambiguity for future RE.

M3 — Chip-busy gate bypass: NOP set-busy-flag at file `0x6df42` (1 site, 4 bytes):``````````

| site | bytes (before → after) | mnemonic |
| --- | --- | --- |
| 0x6df42 | 84 f8 f2 00 → 00 bf 00 bf | strb.w r0, [r4, #0xf2] → nop; nop |

Stock `fcn.0x6df20` (second-stage outbound send, tail-called from M2's site) tests `ctx[0xf2]` (chip-write busy flag) at `0x6df3a`. If set, returns `0xb`. The flag is set at `0x6df42` just before the chip-send tail-call to `fcn.0xae5e4`, and cleared at `fcn.0x6d9b8:0x6da10` in the send-completion handler when the chip ACKs the write.

M3 NOPs ONE of two writers of `chan+0xf2`. The other writer (`fcn.0x6da50:0x6dda8`, fires when the inbound RegisterNotification callback returns CType=0x0F INTERIM) is preserved — some CTs' inbound state machines depend on it. Because the inbound-side writer is still active, M3 alone leaves the gate able to trip for sparse-re-registration CTs (CTs that register an event once at pair time then never re-register; `chan+0xf2` stays set indefinitely until L2CAP TX-complete events cycle the CLEAR sites in `fcn.0x6da50`, which only happens during sustained inbound traffic). M10 (below) completes the bypass by NOPping the GATE CHECK rather than the inbound SET.

M10 — Path A `chan+0xf2` GATE bypass: NOP cbnz at file `0x6df3a` (1 site, 2 bytes):``````````

| site | bytes (before → after) | mnemonic |
| --- | --- | --- |
| 0x6df3a | 53 b9 → 00 bf | cbnz r3, 0x6df52 → nop |

Companion to M3. Removes the gate CHECK rather than the SET. After M3+M10, `fcn.0x6df20` unconditionally proceeds to `fcn.0xae5e4` (L2CAP send); the read of `chan+0xf2` at `0x6df36` still happens but its result no longer controls flow.

Empirical motivation: on sparse-re-registration CTs (a single RegisterNotification at pair time, no re-registers for the remainder of the session), the inbound INTERIM at `0x6dda8` SETs `chan+0xf2` and nothing CLEARs it before the next outbound PSC CHANGED tries to ship. The CHECK at `0x6df3a` drops the response. M10 NOPs the CHECK so the gate becomes informational only; the inbound SET stays intact so well-behaved CTs that depend on it are unaffected.

Safety:
  - Race: mtkbt's IPC dispatcher is single-threaded; `fcn.0xae5e4` → `fcn.0xae418` → `fcn.0x7d204` → `mtk_bt_write` is synchronous. No concurrent Path A emits can race on chan state.
  - Ordering: L2CAP layer's per-channel TX queue at `chan+0x2c` (used by `fcn.0xae5e4` for back-to-back emits) handles ordering at the layer below.
  - Dead writers: 7 other writers of `chan+0xf2` continue to fire (verified exhaustive byte search: 8 writers total, 2 readers — both inside `fcn.0x6df20`, and only the read at `0x6df36` fed the cbnz). After M10, no code in mtkbt makes a flow decision based on the flag. The remaining writes are dead.
  - Spec: AVRCP 1.3 §5.4.2 requires the TG to send CHANGED responses; the gate's drop is not spec-mandated behaviour.

M4 — Outbound-frame drop bypass: NOP gate 1 list-contains check on twin builder at file `0x6d116` (1 site, 2 bytes):``````````

| site | bytes (before → after) | mnemonic |
| --- | --- | --- |
| 0x6d116 | 41 d0 → 00 bf | beq 0x6d19c → nop |

`fcn.0xf0bc` dispatches outbound AVRCP responses through two structurally-identical builders selected by IPC msg byte 9: `ldrb r3, [r6, #9]; cbz r3, 0xf186`. `r3 != 0` (multi-frame fragmented responses — `msg=540` GetElementAttributes STABLE `0x0C`) takes Path A via `fcn.0xed50 → fcn.0x6d048` (M2/M3-patched). `r3 == 0` (short single-PDU responses — `msg=544` RegNotif INTERIM `0x0F` / CHANGED `0x0D`) takes Path B via `fcn.0xef08 → fcn.0x6d0f0`. M2/M3 patch only Path A; before M4, Path B was unpatched.

`fcn.0x6d0f0` is byte-for-byte structurally identical to M2's `fcn.0x6d048`: same `fcn.0x6ccdc` list-contains check at `0x6d110`, same INTERIM/CHANGED discriminator at `0x6d11e`, same drop target `movs r0, 0xd; pop {r3, r4, r5, pc}` at `0x6d19c`. Unlike Path A on busy A2DP-heavy CTs, Path B's list-contains check fails on most invocations, dropping the majority of `msg=544` emits before the wire frame is built. Subscription-class CTs that depend on RegNotif INTERIM responses (ev=01 / 05 / 08 / 0A) then retry-storm on the AVRCP 1.3 §4.2.1 3 s timer until they disengage AVRCP TG. M4 NOPs the analogous `beq 0x6d19c` at `0x6d116`, so `fcn.0x6d0f0` unconditionally builds the wire frame and tail-calls `b.w 0xae5e4` (`L2CAP_SendData`). `fcn.0x6d0f0` skips `fcn.0x6df20` entirely, so M3's chip-busy SET has no analogue on Path B.

M5 — TID-echo skip-on-outbound cave: code-cave at `0xf3680` (4 sites, 6 + 24 + 4 + 4 bytes):``````````````````````````````````````

|  | offset | before | after |
| --- | --- | --- | --- |
| call site | 0x6d186 | 68 7b 84 f8 29 00 (ldrb r0, [r5, 0xd]; strb.w r0, [r4, 0x29]) | 86 f0 7b ba 00 bf (b.w 0xf3680; nop) |
| cave blob | 0xf3680 | 24 × 00 (LOAD #1 page padding) | 68 7b 00 28 00 bf 01 d0 84 f8 29 00 00 bf 00 bf 00 bf 00 bf 79 f7 7a bd (Thumb-2 M5 with cmp r0,0 discriminator + NOP padding + return) |
| LOAD #1 filesz | 0x84 | 6c 36 0f 00 (0xf366c) | 98 36 0f 00 (0xf3698) |
| LOAD #1 memsz | 0x88 | 6c 36 0f 00 (0xf366c) | 98 36 0f 00 (0xf3698) |

Path B at `0x6d186` writes `chan[+0x29]` from `packet[+0xd]`. The same site is reached from two callers: the INBOUND CMD chain (`fcn.0x11374 → fcn.0xed0a → Path B`), where `r5` points at the per-channel stash struct and `r5[+0xd]` is the inbound AV/C command's transId (latched by `fcn.0x11374:0x11436 strb.w sl, [r4, 0xba9]`); and the OUTBOUND RESPONSE chain (`fcn.0x11894 → fcn.0xf0bc → Path B`), where `r5` points at a freshly-allocated IPC packet and `packet[+0xd] = 0` unconditionally (`fcn.0x11894:0x11924-0x11927` writes `movs r6, 0; strb r6, [r4, 0xd]`). Unpatched Path B propagates the inbound transId on inbound calls but clobbers `chan[+0x29]` with 0 on outbound calls before the wire-frame builder `fcn.0xae418` reads it at `0xae448 ldrb r6, [r4, 0x15]`. Every Path B wire response then encodes byte 0 as `(0 << 4) + 4 + pkt[8]` per AVCTP 1.2 §6.1.1, i.e. transId=0 regardless of the originating command.

CTs that cycle AV/C transIds across the 0-15 range (`AVCTP 1.2 §6.1.1` transaction-label rotation, observed via `[AVRCP] transId:%d` btlog entries) see all their RegNotif INTERIM / CHANGED responses with TID=0, fail the `AVRCP 1.3 §4.2.1` command-response TID echo and `§6.7.2` subscription TID match, and retry-storm on the AVRCP 1.3 §4.2.1 3 s AVCTP retry timer until they disengage AVRCP TG. CTs that use transId=0 exclusively (no rotation) match accidentally and work pre-M5.

The cave places a conditional-store trampoline in the LOAD #1 page-padding region (same ELF-extension trick used by `patch_libextavrcp_jni.py` for its trampoline blob — extend the segment's filesz / memsz to claim previously-unmapped zero-padding bytes as R+E). The cave skips the outbound strb (preserving `fcn.0xf0bc:0xf1a8`'s prior write of `chan+0x39 = packet[+0xa] = msg[5]`) and lets the inbound strb fire (writing `chan+0x39 = packet[+0xd]` = inbound TID).

Discriminator: `cmp r0, 0` using the already-loaded `packet[+0xd]`. Outbound IPC packets have `packet[+0xd] = 0` (allocator-zeroed at `fcn.0x11894:0x11926` — `movs r6, 0; strb r6, [r4, 0xd]`). Inbound stash struct's `+0xd` is the inbound TID (nonzero in the common case). Empirically validated across CT sessions via the D2 cave's `M5dbg pd=NN` logs — `pd=0` correlates 1:1 with outbound IPC packets.

AVRCP 1.3 §4.2.1 strict TID echo correctness depends on the JNI side writing `conn[+0x11] = inbound CMD's TID` before every `*_rsp` builder call. RegNotif paths source the TID from `g_avrcp_req_event_database[event_id]`; non-RegNotif paths source it from the stack at `sp+0x171` via T4's prologue. See `patch_libextavrcp_jni.py` "AVRCP 1.3 §4.2.1 strict TID echo" section below. With those writes in place, `fcn.0xf0bc:0xf1a8` writes the correct TID into chan+0x39, and this cave preserves it across the outbound strb at `0x6d186`.

Cave disassembly (24 bytes at `0xf3680`):`0xf3680 68 7b ldrb r0, [r5, 0xd] ; load packet[+0xd] 0xf3682 00 28 cmp r0, 0 ; outbound = 0 (pd) 0xf3684 00 bf nop ; padding 0xf3686 01 d0 beq 0xf368c ; skip strb on outbound 0xf3688 84 f8 29 00 strb.w r0, [r4, 0x29] ; inbound: chan+0x39 = TID 0xf368c 00 bf 00 bf 2 × nop ; padding 0xf3690 00 bf 00 bf 2 × nop ; padding 0xf3694 79 f7 7a bd b.w 0x6d18c ; return into Path B`

Edge case: inbound CMDs with TID=0 fall into the outbound branch (skip strb). chan+0x39 isn't updated from the inbound. This doesn't affect wire echo because every outbound response goes through fcn.0xf0bc which rewrites chan+0x39 from packet[+0xa] = msg[5]. The inbound strb is therefore redundant in the working flow; it's kept for compatibility with any code path that reads chan+0x39 between an inbound CMD and the next outbound response.

The 8 bytes at `0xf368c..0xf3693` are NOP padding inside the 24-byte cave, reserved for future use without requiring a LOAD #1 filesz bump.

LOAD #1 filesz / memsz expand from `0xf366c` to `0xf3698` (a 44-byte extension — the cave at `0xf3680` is 24 bytes; the 20 bytes of preceding zero-padding `0xf366c..0xf3680` are absorbed harmlessly). No section headers are modified; the kernel ELF loader maps segments by program headers exclusively.

MD5s: Stock + current output MD5s are pinned in `patch_mtkbt.py`'s `STOCK_MD5` / `OUTPUT_MD5` / `OUTPUT_DEBUG_MD5` constants; the patcher prints them on every run and verifies the output against the pinned values.

## `patch_libextavrcp_jni.py`

The trampoline chain that synthesises AVRCP 1.3 responses directly from the JNI library, bypassing the no-op Java AVRCP TG. Patches into `_Z17saveRegEventSeqIdhh` (the JNI msg-519 receive function, body at file `0x5f0c`) and extends LOAD #1's filesz / memsz to map the page-alignment padding region as R+E for trampoline code.

`y1-track-info` access pattern. The trampolines lazy-init a single `mmap2(NULL, 4096, PROT_READ, MAP_SHARED)` of `/data/data/com.innioasis.y1/files/y1-track-info` via the shared `get_or_init_mmap` subroutine (caches the pointer in `.bss` at vaddr `0xd2cc`, retries on every miss). All per-trampoline reads call `read_track_info(dst, nbytes, slot_offset)` which (1) loads `file[0]` to pick the active slot, (2) byte-copies `nbytes` from `slot_base + slot_offset` into the caller's stack `file_buf`. All offsets below (`y1-track-info[N]` notation) refer to per-slot offsets within the 1104-byte active slot; the file-level wrapper (active_slot byte + 2 × slot, 2213 B total) is documented in [`BT-COMPLIANCE.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FBT-COMPLIANCE.md) §4.

### R1 — redirect at `0x6538` (4 bytes)``````````

|  | bytes | mnemonic |
| --- | --- | --- |
| before | 40 d1 09 25 | bne.n 0x65bc + movs r5, #9 |
| after | 00 f0 e6 fe | bl.w 0x7308 |

Diverts the size!=3 dispatch arm to T1 instead of falling into "unknow indication". Destroys the size==8 path's `movs r5, #9`, which is acceptable because mtkbt-as-1.0 never legitimately produces size==8 frames on this device.

### T1 — GetCapabilities (PDU 0x10) at `0x7308` (40 bytes)

Overwrites the unused JNI debug method `_Z33BluetoothAvrcpService_testparmnumP7_JNIEnvP8_jobjectaaaaaaaaaaaa` (~44 byte slot). Detects PDU 0x10, calls `btmtk_avrcp_send_get_capabilities_rsp` via PLT `0x35dc` with an 8-element `EventsSupported` array, branches to epilogue at `0x712a`. Fall-through (b.w `0x72d4`) bridges to T2.

Per AVRCP 1.3 §5.4.2 + ICS Table 7 row 11, GetCapabilities is mandatory for any TG advertising PASS THROUGH Cat 1 (which our V1 SDP does). Advertised set: `0x01` PLAYBACK_STATUS, `0x02` TRACK_CHANGED, `0x05` PLAYBACK_POS, `0x08` PLAYER_APPLICATION_SETTING_CHANGED, plus `0x09` NOW_PLAYING_CONTENT_CHANGED, `0x0a` AVAILABLE_PLAYERS_CHANGED, `0x0b` ADDRESSED_PLAYER_CHANGED, `0x0c` UIDS_CHANGED. The four 0x09..0x0c IDs come from AVRCP 1.4+; T1 advertises them and T8 INTERIM-acks each subscription, matching a reference 1.3-profile TG's observed behaviour. NowPlayingContentChanged (ev=0x09) is load-bearing: at least one CT in the test matrix uses NowPlayingContent CHANGED (not TrackChanged CHANGED) as its primary metadata-refresh trigger and falls back to a ~20 s polling cycle if that subscription is rejected. T5/T9 emit CHANGED for ev=0x09 on every track/play edge gated on `database[9] != 0`. Subscriptions for ev=0x0a/0x0b/0x0c are INTERIM-acked but never receive CHANGED (Y1 has no multi-player / UID-database semantics).

T1 also calls the shared `clear_event_database` subroutine on every GetCapabilities to zero `g_avrcp_req_event_database` (15 bytes at vaddr `0xd2b5`). GetCapabilities is the canonical CT-connection-boundary marker (every spec-conforming CT issues it as the first PDU on a new AVCTP channel), so this gives clean session-scope semantics: stale per-event subscription bytes from a previous CT's connection cannot leak into a fresh session.

AVRCP 1.3 §4.2.1 strict TID echo. Every AVRCP response Y1 emits must echo the inbound CMD's AVCTP transaction-label nibble. Response builders (`btmtk_avrcp_send_*_rsp` family in `libextavrcp.so`) read `conn[+0x11]` and pack it into outbound `msg[5]`; mtkbt's `fcn.0xf0bc:0xf1a8` then writes `msg[5]` into `chan+0x39` for the wire builder (`fcn.0xae418`). Whatever wrote `conn[+0x11]` last is the source of truth for the outbound TID.

Y1 writes `conn[+0x11]` at three call sites covering every PDU path:
  - RegNotif INTERIM/CHANGED (per-event database). libextavrcp_jni.so maintains a 15-byte global `g_avrcp_req_event_database` at vaddr `0xd2b5` (`.bss`) — one byte per event_id. extended_T2's `save_event_seq_id` writes `database[event_id] = seq_id + 1` on every inbound RegNotif CMD (the `+1` lets `0` unambiguously encode "not subscribed this session" even when the wire seq_id is 0). Every CHANGED / INTERIM emit site in extended_T2 / T5 / T8 / T9 calls the shared `restore_conn_tid` subroutine, which reads `database[event_id]` and writes `(value - 1) → conn[+0x11]`. The same nonzero byte doubles as the §5.4.2 subscription gate: T5 / T9 skip the CHANGED emit when `database[event_id] == 0`, suppressing unsolicited frames for events the CT didn't subscribe to in the current session.
  - Non-RegNotif PDUs (T4 universal entry).`T4`'s prologue does `ldrb.w r1, [sp, 0x171]; strb r1, [r5, 0x19]` — copying the inbound CMD's seq_id byte (at the empirically-verified pre-`SUB SP` offset) into `conn[+0x11]` (= `[r5, 0x19]` since `conn = r5 + 8`). T4 is the universal dispatcher reached via `extended_T2:b.w T4` for every PDU other than GetCap and RegNotif, so this single write covers GetEA (0x20), GetPlayStatus (0x30), InformCharset (0x17), InformBattery (0x18), PApp (0x11..0x16), and Continuation (0x40/0x41). One unconditional write per dispatched CMD, valid for the lifetime of the immediate response.
  - GetCapabilities (0x10). Response generated by `T1_extended` (in-blob, GetCap arm). Stock JNI writes `conn[+0x11] = inbound TID` before our R1 redirect at JNI vaddr `0x6538` takes effect, so no trampoline write is needed for this PDU.

The wire-emit chain (`conn[+0x11] → msg[5] → packet[+0xa] → chan+0x39 → AVCTP wire byte 0`) is invariant across all three paths. M5 cave at `patch_mtkbt.py:0xf36a0` provides per-frame diagnostic logs (`M5wire c39=NN`, `M5dbg p8/pd=NN`) but does not drive TID correctness — it harmlessly skips one redundant inbound-latch strb on outbound packets.

Session scope is enforced by `clear_event_database` at every T1 GetCapabilities entry — zeroing the 15-byte database in one 4-store sequence — so the gates are bound to the CT-connection boundary, not to process lifetime.

### T2 stub + extended_T2 — RegisterNotification (PDU 0x31) entry

T2 stub at `0x72d0` (8 bytes) overwrites `classInitNative` with `movs r0, #0; bx lr` (preserves the `return 0` contract; loses the debug logs) followed by `b.w extended_T2`. extended_T2 lives in the LOAD #1 padding region; on entry it unconditionally calls `save_event_seq_id` to write `database[event_id] = seq_id + 1` for every PDU=0x31 CMD reaching this path (replicating the stock `saveRegEventSeqId` write the trampoline path otherwise bypasses). For event 0x02 TRACK_CHANGED specifically it then:
  - Reads `y1-track-info[0..7]` (track_id) into a stack buffer.
  - Calls `restore_conn_tid` to write `database[2] - 1 → conn[+0x11]` so the response builder echoes the inbound TID.
  - Replies INTERIM via `reg_notievent_track_changed_rsp` (PLT `0x3384`) with `r1=0` (success), `r2=REASON_INTERIM` (`0x0f`), `r3=&selected_track_id` (8 zero bytes).

Other PDU / event combos fall through to T4 (PDU 0x20 → main, 0x17 → T_charset, 0x18 → T_battery, 0x30 → T6, 0x40 / 0x41 → T_continuation, 0x31+event≠0x02 → T8) before hitting the original "unknow indication" path.

`r1=0` matters: response builders dispatch on r1 — `r1==0` writes the spec-correct event payload (reasonCode + event_id + 8-byte Identifier memcpy per AVRCP 1.3 §5.4.2 Table 5.30); `r1!=0` writes a reject-shape frame. We pass `r1=0` everywhere.

Identifier payload = `0x0000000000000000` (8 zero bytes from the static `selected_track_id` data block in the trampoline blob). AVRCP 1.6 §6.7.2 Table 6.32 names this value "SELECTED" — "the currently playing track, no specific UID". This is also the strict AVRCP 1.6 §6.7.2 Table 6.32 reading ("Identifier shall always be set to 0x00…00" for TGs without Browseable Player UID support) and matches what a reference 1.3-as-TG implementation ships when no Now-Playing queue is in scope. Y1's served SDP record advertises AVRCP 1.3, so this is the spec-correct wire shape for the version we declare.

### T4 — GetElementAttributes (PDU 0x20) and universal non-RegNotif entry

In the LOAD #1 padding region, reached from extended_T2's `b.w T4` for every PDU other than 0x31 (RegNotif). T4's prologue writes `conn[+0x11] = sp[+0x171]` (the inbound CMD's TID byte) before any PDU dispatch — this is the universal §3.3.5 TID-echo write covering GetEA (0x20), GetPlayStatus (0x30), InformCharset (0x17), InformBattery (0x18), PApp (0x11..0x16), and Continuation (0x40/0x41). After the conn[+0x11] write, T4 dispatches on the PDU byte and branches via `b.w` to T_charset / T_battery / T6 / T_papp / T_continuation as appropriate, or executes the GetElementAttributes main body below for PDU 0x20.

The GetEA body implements the AVRCP 1.3 §5.3.1 Table 5.24 response contract: "If NumAttributes is set to zero, all attribute information shall be returned, else attribute information for the specified attribute IDs shall be returned by the TG."

T4 reads the inbound `NumAttributes` byte (caller's sp+394) and:
  - `NumAttributes == 0`: emits all seven supported attributes in canonical order (1..7) via a compile-time-unrolled loop.
  - `NumAttributes > 0`: emits each requested `AttributeID[i]` in the CT-specified order. For IDs in {0x01..0x07}, the value comes from the corresponding `y1-track-info` slot below. For any other ID (e.g. 0x08 — "Reserved" in 1.3, never supported), Y1 emits the attribute header with `AttributeValueLength=0` per AVRCP 1.3 §5.3.1 Table 5.24 "for attributes not supported by the TG, this field shall be sent with 0 length data".
````````````````

| attr_id | Name | Source slot in y1-track-info |
| --- | --- | --- |
| 0x01 | Title | [8..263] |
| 0x02 | Artist | [264..519] |
| 0x03 | Album | [520..775] |
| 0x04 | TrackNumber | [800..815] (UTF-8 ASCII decimal) |
| 0x05 | TotalNumberOfTracks | [816..831] (UTF-8 ASCII decimal) |
| 0x06 | Genre | [848..1103] |
| 0x07 | PlayingTime | [832..847] (UTF-8 ASCII decimal milliseconds) |

All values ship as UTF-8 (charset `0x006A`); a missing attribute is signalled by `AttributeValueLength=0`. Y1's emission of zero-length entries requires `patch_libextavrcp.py` E1 to land — the stock `libextavrcp.so` response builder otherwise drops such attributes on the floor (an AVRCP 1.3 §5.3.1 Table 5.24 violation in the stock code). The numeric attrs (4 / 5 / 7) are stored pre-formatted as ASCII strings by the music app's `TrackInfoWriter` rather than binary u16 / u32 with a Thumb-2 itoa, keeping the trampoline a uniform strlen+memcpy loop.

T4 also detects track-id edges (compares the active slot's `track_id` field from `y1-track-info` against the `.bss` trampoline-state block at `G_Y1_TRAMPOLINE_STATE + 0..7`) and emits a reactive CHANGED via `reg_notievent_track_changed_rsp` before the GetElementAttributes response, then writes the new track_id back to the `.bss` state.

Pre-check dispatch table: `0x20 → main`, `0x17 → T_charset`, `0x18 → T_battery`, `0x30 → T6`, `0x40 → T_continuation`, `0x41 → T_continuation`, `0x31+event≠0x02 → T8`, else fall through to "unknow indication".

### T5 — proactive track-edge CHANGED burst

In LOAD #1 padding. Entered via `b.w T5` from the patched first instruction of `notificationTrackChangedNative` at file offset `0x3bc0`:``````

|  | bytes | mnemonic |
| --- | --- | --- |
| before | 2D E9 F0 47 | stmdb sp!, {r4, r5, r6, r7, r8, r9, sl, lr} (function prologue) |
| after | [b.w T5 emitted by patcher] | branch to T5 trampoline |

T5 obtains the AVRCP per-conn struct via JNI helper at `0x36c0` (the same helper the stock native called), reads `y1-track-info` (active slot, 800 B via the mmap-backed `read_track_info` subroutine) and trampoline state (13 B via `read_state_block` from `.bss`), and on track-id divergence emits a track-edge CHANGED burst in this order:
  - `reg_notievent_pos_changed_rsp` (PLT `0x3360`, event 0x05 — Tbl 5.33) with `r1=0`, `r2=REASON_CHANGED`, `r3=REV(file[780..783])` (current position in host order — `duration_ms` on natural end, `0` on NEXT / PREV). Gated on `database[5] != 0`.
  - `reg_notievent_track_changed_rsp` (PLT `0x3384`, event 0x02 — Tbl 5.30) with `r1=0`, `r2=REASON_CHANGED` (`0x0d`), `r3=&selected_track_id` (8 zero bytes per §5.14.1 SELECTED). Gated on `database[2] != 0`.
  - `reg_notievent_now_playing_content_rsp` (PLT `0x330c`, event 0x09) with `r1=0`, `r2=REASON_CHANGED`. Gated on `database[9] != 0` (subscription armed by T8's INTERIM ack for ev=0x09). Some CTs use this as their primary metadata-refresh trigger.
  - `reg_notievent_reached_end_rsp` (PLT `0x3378`, event 0x03 — Tbl 5.31) only when`y1-track-info[793]` (the `previous_track_natural_end` flag set by `PlaybackStateBridge.onCompletion`) `== 1` AND `database[3] != 0`. Strict spec semantic: TRACK_REACHED_END fires on natural end, not on a skip.
  - `reg_notievent_reached_start_rsp` (PLT `0x336c`, event 0x04 — Tbl 5.32) with `r1=0`, `r2=REASON_CHANGED`. Gated on `database[4] != 0`.

Each emit site is preceded by a `restore_conn_tid` call (passing the matching event_id in r1) so the response builder sees `conn[+0x11] = database[event_id] - 1` — the inbound TID for that event_id. Then writes the new track_id back to state and returns `jboolean(1)`.

Emit ordering (PPC → TC → NPCC) matches a reference 1.3-as-TG implementation's observed wire order. Position reset arrives first so the CT zeroes the playhead before processing the identity change; TC arrives second so the CT registers the new track ID before NPCC's now-playing refresh hits. 0x03 / 0x04 are AVRCP 1.3 extensions Y1 supports if the CT subscribes (they're not advertised in the current `T1` event set, so `database[3]` / `database[4]` are typically `0` and these emits become no-ops).

Fired on every `com.android.music.metachanged` broadcast emitted by the music app (after the MtkBt.odex sswitch_1a3 cardinality NOP at 0x3c530 wakes the dispatch path). The remaining 196 bytes of the original native body are unreachable. T5's frame is 824 B (24 state mirror + 800 file_buf — the state-mirror region holds `last_*` change-detection bytes at `[0..12]` and is zero-padded across `[13..23]`).

### T_charset — InformDisplayableCharacterSet (PDU 0x17)

Branched from T4's pre-check on PDU 0x17. Restores lr canary + r0=conn and tail-jumps to UNKNOW_INDICATION (`0x65bc`), which emits an AV/C `NOT_IMPLEMENTED` reject. 12 bytes. Spec-permissible per AVRCP 1.3 §5.2.7 (Optional). Acking via `inform_charsetset_rsp` stalled at least one strict CT into a 3 s wait between 0x17 and the first RegisterNotification (apparently waiting for a follow-up notification that never came); reject lets the subscription burst land in <10 ms.

### T_battery — InformBatteryStatusOfCT (PDU 0x18)

Same shape as T_charset, calls `battery_status_rsp` via PLT `0x357c`. AVRCP 1.3 §5.2.8.

### T_continuation — RequestContinuingResponse (0x40) / AbortContinuingResponse (0x41)

Branched from T4's pre-check on PDU 0x40 or 0x41. Restores `lr` canary + `r0=conn` and tail-jumps to UNKNOW_INDICATION (the catch-all reject path that emits AV/C NOT_IMPLEMENTED via msg=520). Functionally identical to the catch-all fall-through but routed through an explicit dispatch in the pre-check so ICS Table 7 rows 31-32 read "shipped" rather than "fall-through".

AVRCP 1.3 §4.7.7 / §5.5: continuation is initiated by the TG setting `Packet Type=01` (start) in a response — the CT only sends 0x40 in reply to a fragmented response. `get_element_attributes_rsp` never sets the start-of-fragmentation flag, so a spec-conforming CT never sends 0x40. The trampoline body is 6 bytes (one `ldrh.w`, one `add.w`, one `b.w`).

§6.15.2 specifies AV/C INVALID_PARAMETER (status 0x05) as the spec-strict response when receiving 0x40 without prior fragmentation; NOT_IMPLEMENTED is a different but spec-acceptable AV/C reject for an unsupported PDU and is functionally indistinguishable to the CT (both are reject frames; the CT abandons the continuation flow either way).

### T6 — GetPlayStatus (PDU 0x30)

Branched from T4's pre-check on PDU 0x30. Reads `y1-track-info[776..795]` (4 BE u32 fields: duration_ms / position_at_state_change_ms / state_change_time_ms / playing_flag), byte-swaps the u32s to host order via Thumb-2 `REV`, and calls `btmtk_avrcp_send_get_playstatus_rsp` via PLT `0x3564` with `arg1=0` + `r2=duration_ms` + `r3=live_position_ms` + `sp[0]=play_status`. Outbound `msg_id=542`, 20-byte IPC frame.

Live position extrapolation: when `playing_flag == PLAYING` (the music app's `PlaybackStateBridge` maps `Static.setPlayValue`'s newValue 0/1/3/5 directly to AVRCP 1.3 §5.4.1 Table 5.26 PlayStatus bytes), T6 calls `clock_gettime(CLOCK_BOOTTIME, &timespec)` (NR=263, clk_id=7 — same monotonic source `TrackInfoWriter` stamps `mStateChangeTime` from), computes `now_ms = tv_sec * 1000 + tv_nsec / 1e6`, then `live_pos = saved_pos_ms + (now_ms - state_change_ms)`, passes that as r3. The nsec→ms division is done via magic-multiply (`(tv_nsec * 0x431BDE83) >> 50`, equivalent to high-half UMULL then >>18) — bit-exact for tv_nsec ∈ [0, 1e9). Both endpoints carry full ms precision on the wire, so the position the CT renders is exact relative to Y1's playhead, no per-state-edge ±1 s lurch. When STOPPED / PAUSED the position field stays at the saved freeze point. Implements AVRCP 1.3 §5.4.1 Table 5.26's `SongPosition` definition ("the current position of the playing in milliseconds elapsed"). `struct timespec` is stashed in unused outgoing-args slack at sp+8..15 inside the existing T6 frame (no frame growth).

ICS Table 7 row 21: GetPlayStatus is mandatory for any TG that ships GetElementAttributes Response (per ICS condition C.2). T6 closes that mandatory row.

### T_papp — PlayerApplicationSettings (PDUs 0x11..0x16)

Branched from T4's pre-check when the inbound PDU byte is in `[0x11..0x16]`. Per AVRCP 1.3 ICS Table 7 condition C.14, supporting any single PApp PDU makes the whole 7-row group (PDUs 0x11..0x16 + event 0x08) Mandatory — they ship together.

Y1 supports Repeat (id=2) + Shuffle (id=3); other AVRCP §5.2.1 attributes (Equalizer 0x01, Scan 0x04) aren't surfaced by the music app and aren't advertised. Six PDU dispatchers internal to T_papp + a paired event 0x08 INTERIM case in T8. Event 0x08 INTERIM (T8) and proactive CHANGED (T9) bind to live state via `y1-track-info[795..796]`, written by the music app's `PappStateBroadcaster` on every `musicRepeatMode` / `musicIsShuffle` SharedPreferences change. GetCurrent reads the same slot bytes via `read_track_info(slot_offset=795)` with a static OFF/OFF fallback on mmap failure. List / AttrText / ValueText return static-schema responses (these reflect the capabilities of the player rather than per-edge state).``````````````````````````````````````

| PDU | Builder PLT | Behavior |
| --- | --- | --- |
| 0x11 ListPlayerApplicationSettingAttributes | 0x35d0 | Returns [Repeat=2, Shuffle=3], n=2 |
| 0x12 ListPlayerApplicationSettingValues | 0x35c4 | Switches on inbound attr_id: Repeat → [1,2,3,4], Shuffle → [1,2,3], else reject |
| 0x13 GetCurrentPlayerApplicationSettingValue | 0x35b8 | Branches on inbound n per V13 §6.12 ("TG returns the value(s) of the setting(s) requested by the CT"). n==1: validate the requested attr_id (Repeat or Shuffle, else reject with status 0x05 INVALID_PARAMETER), read the matching live byte from y1-track-info[795..796], emit n=1 response. Other n: read both bytes, emit n=2 response (kept for permissive CTs). I/O failure falls back to 0x01 OFF for n=1 / [(Repeat, OFF), (Shuffle, OFF)] for n!=1. |
| 0x14 SetPlayerApplicationSettingValue | 0x3594 | Reads inbound (attr_id, value) pair from caller's sp+387/+388, writes 2 bytes to /data/data/com.innioasis.y1/files/y1-papp-set (atomic O_WRONLY |
| 0x15 GetPlayerApplicationSettingAttributeText | 0x35ac | Accumulator: emit "Repeat" (idx=0) then "Shuffle" (idx=1, total=2 → SendMessage) |
| 0x16 GetPlayerApplicationSettingValueText | 0x35a0 | Emits per-(attr_id, value_id) text via switch: Repeat 0x01/0x02/0x03 → "Off"/"Single Track"/"All Tracks"; Shuffle 0x01/0x02 → "Off"/"All Tracks". Unsupported pairs fall through with no response (peer times out / falls back). |

Per-builder calling-convention reference: [`ARCHITECTURE.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FARCHITECTURE.md) PApp builder table.

ICS Table 7 rows 12-15 (C.14 Mandatory if any), 16-17 (Optional), and 30 (event 0x08, Optional) — all closed by T_papp + the T8 event 0x08 INTERIM case.

### T8 — RegisterNotification dispatcher for events ≠ 0x02

In LOAD #1 padding. Branched from extended_T2's "PDU 0x31 + event ≠ 0x02" arm. Reads `y1-track-info` for events that need payloads (0x01 / 0x05), then dispatches on event_id and calls the matching `reg_notievent_*_rsp` PLT entry:``````````````````````````````````````

| event_id | name | PLT | payload |
| --- | --- | --- | --- |
| 0x01 | PLAYBACK_STATUS_CHANGED | 0x339c | play_status u8 (from y1-track-info[792]) |
| 0x03 | TRACK_REACHED_END | 0x3378 | (none) |
| 0x04 | TRACK_REACHED_START | 0x336c | (none) |
| 0x05 | PLAYBACK_POS_CHANGED | 0x3360 | position_ms u32 (from y1-track-info[780..783], REV-swapped) |
| 0x06 | BATT_STATUS_CHANGED | 0x3354 | battery_status u8 from y1-track-info[794] (real bucket from Intent.ACTION_BATTERY_CHANGED) |
| 0x07 | SYSTEM_STATUS_CHANGED | 0x3348 | canned 0x00 POWER_ON (intentional — while trampolines run the system is by definition POWER_ON; the canned value IS the real value) |
| 0x08 | PLAYER_APPLICATION_SETTING_CHANGED | 0x345c | n=2 + [(Repeat, repeat_avrcp), (Shuffle, shuffle_avrcp)] from y1-track-info[795..796] |
| 0x09 | NOW_PLAYING_CONTENT_CHANGED | 0x330c | INTERIM ack (empty payload). T5/T9 gate their CHANGED emit on database[9] != 0. |
| 0x0a | AVAILABLE_PLAYERS_CHANGED | 0x3324 | INTERIM ack (empty payload). No CHANGED — Y1 has one player. |
| 0x0b | ADDRESSED_PLAYER_CHANGED | 0x3330 | INTERIM ack (PlayerID=0, UidCounter=0). No CHANGED — single addressed player. |
| 0x0c | UIDS_CHANGED | 0x3318 | INTERIM ack (UidCounter=0). No CHANGED — no UID database. |

Events 0x01-0x08 cover AVRCP 1.3 §5.4.2 (Tbls 5.29/5.31/5.32/5.33/5.34/5.36/5.37); events 0x09-0x0c are AVRCP 1.4+ extensions advertised in T1 and INTERIM-acked here, mirroring a reference 1.3-profile TG's behaviour. Their response builders are already linked by `libextavrcp_jni.so` (PLT stubs present though stock JNI never invokes them). T5/T9 emit CHANGED for ev=0x09 on every track/play edge; ev=0x0a/0x0b/0x0c stay idle in steady state (Y1 has no multi-player / UID-database semantics).

All response builders share the calling convention `r0=conn`, `r1=0` (success), `r2=reasonCode` (where reasonCode is one of INTERIM `0x0F` / CHANGED `0x0D` / NOT_IMPLEMENTED `0x08`), `r3=event-specific u8/u16/u32`. Unknown event_ids beyond 0x0c fall through to "unknow indication" for the spec-correct NOT_IMPLEMENTED reject. T8 handles INTERIM for events 0x01/0x03/0x04/0x05/0x06/0x07/0x08; proactive CHANGED for events 0x01/0x05/0x06/0x08 lives in T9 (entered from `notificationPlayStatusChangedNative`) and for 0x02/0x03/0x04 in T5/extended_T2 (entered from `notificationTrackChangedNative` / extended_T2's PDU 0x31 + event 0x02 arm respectively). Each INTERIM call site is preceded by `restore_conn_tid` (event_id passed in r1) so the response builder echoes the inbound TID — the `save_event_seq_id` write at extended_T2's entry already populated `database[event_id]`. Event 0x07 is INTERIM-only — nothing on Y1 ever changes the SYSTEM_STATUS payload (see footnote in `docs/BT-COMPLIANCE.md` §2).

### T9 — proactive CHANGED on play-state / battery / papp / 1Hz position tick

T5's structural twin for events 0x01, 0x06, 0x05, 0x08, 0x09. Entered via `b.w T9` from the patched first instruction of `notificationPlayStatusChangedNative` at file offset `0x3c88`:````

|  | bytes | mnemonic |
| --- | --- | --- |
| before | 2D E9 F3 41 | function prologue |
| after | [b.w T9 emitted by patcher] | branch to T9 trampoline |

T9 reads `y1-track-info` into its file buffer (via `read_track_info` — active slot, mmap-served) and the trampoline state block (13 B via `read_state_block` from `.bss`), then runs five independent edge / cadence checks:
  - play_status: compare file[792] vs state[9] (`last_play_status`). On inequality, emit `reg_notievent_playback_rsp` via PLT `0x339c` with `r1=0`, `r2=REASON_CHANGED` (`0x0d`), `r3=play_status`. Gated on `database[1] != 0`. The same edge branch also emits `NowPlayingContentChanged` CHANGED alongside the play-status CHANGED, gated on `database[9] != 0`. Both emits use `restore_conn_tid` to echo the per-event TID. Update state[9].
  - battery_status: compare file[794] vs state[10] (`last_battery_status`). On inequality, emit `reg_notievent_battery_status_changed_rsp` via PLT `0x3354` with `r3=battery_status`. Gated on `database[6] != 0`. Update state[10].
  - papp settings: compare file[795]/file[796] (repeat_avrcp / shuffle_avrcp) vs state[11]/state[12]. On any inequality, emit `reg_notievent_player_appsettings_changed_rsp` via PLT `0x345c` with `r3=2`, `sp[0]=&papp_attr_ids` (=`[0x02, 0x03]`), `sp[4]=&file[795]`. Gated on `database[8] != 0`. Update state[11..12]. The values pointer is just `sp+T9_OFF_FILE_REPEAT` since file_buf already holds `[r, s]` contiguously at 795..796.
  - playback_pos: if file[792] == 1 (PLAYING), `clock_gettime(CLOCK_BOOTTIME, &timespec)` (NR=263, clk_id=7 via `svc 0`), compute `now_ms = tv_sec * 1000 + tv_nsec / 1e6` (nsec/1e6 via magic-multiply 0x431BDE83 then high-half >>18), then `live_pos = REV(file[780..783]) + (now_ms - REV(file[784..787]))` and emit `reg_notievent_pos_changed_rsp` via PLT `0x3360` with `r3=live_pos`. Gated on `database[5] != 0`. Same arithmetic T6 does for GetPlayStatus, so position parity is maintained between polled GetPlayStatus and notification CHANGED. Both endpoints (`state_change_time_ms` written by `TrackInfoWriter` from `SystemClock.elapsedRealtime()`; `now_ms` from `clock_gettime(CLOCK_BOOTTIME)`) carry full ms precision in the same monotonic-since-boot epoch, so subtraction is bit-exact. Fires on every `playstatechanged` broadcast while playing — the music app's 1 s position ticker drives the ~1 Hz cadence.

T9's frame is 840 B (8 outgoing-args at sp+0..7 + 24 state + 800 file_buf + 8 timespec).

If play, battery, or papp changed, the modified bytes are written back to .bss state at offset 9 (4 B: bytes 9..12) — these are `last_*` change-detection mirrors only and carry no subscription information; the position emit is independent and never dirties state. Fires on every `playstatechanged` broadcast (after the MtkBt.odex sswitch_18a cardinality NOP at 0x3c4fe wakes the dispatch path). Closes AVRCP 1.3 §5.4.2 Table 5.29's CHANGED requirement on event-0x01 subscribers, Table 5.34's on 0x06, Table 5.33's on 0x05, and Table 5.36's on 0x08.

`playstatechanged` is emitted whenever any of the following occurs:
  - play state edge (the music app's `PlayerService` fires `com.android.music.playstatechanged` directly per android.music standard)
  - battery bucket transition (level+plug bucket-mapped to the AVRCP §5.4.2 Tbl 5.35 enum)
  - `musicRepeatMode` / `musicIsShuffle` SharedPreferences change (the music app's `PappStateBroadcaster` writes `y1-track-info[795..796]` and triggers a `playstatechanged` relay)
  - 1 s position tick while playing

Stock MtkBt's battery dispatch chain via `BTAvrcpSystemListener.onBatteryStatusChange` is dead — `BTAvrcpMusicAdapter$2` overrides it with a log-only stub — so reusing `playstatechanged` as the trigger is the cheapest correct alternative, with `BATT_STATUS_NORMAL` retained only as the safe default for a short y1-track-info file (`stack_buf` is memset to zero before the read). The position emit deviates slightly from strict spec (we emit at our 1 s cadence rather than the CT-supplied `playback_interval`); this is a permissible floor since "shall be emitted at this interval" defines a maximum interval, not a minimum cadence — emitting more frequently over-serves rather than under-serves.

### U1 — disable kernel auto-repeat on the AVRCP `/dev/uinput` keyboard

At file `0x74e8` (4 bytes), inside `avrcp_input_init`:````````

|  | bytes | mnemonic |
| --- | --- | --- |
| before | fc f7 b4 e8 | blx ioctl@plt |
| after | 00 bf 00 bf | nop ; nop (Thumb-2) |

`avrcp_input_init` (real body at `0x73c8`, called from `BluetoothAvrcpService_activate_1req` and `wakeupListenerNative`) opens `/dev/uinput` at `0x73f2`, `strncpy`s the device name `"AVRCP"` (string at `0x828b`) into a `uinput_user_dev` struct, sets `id.bustype = BUS_BLUETOOTH (5)` at `0x749a`, and issues a four-call `UI_SET_EVBIT` sequence:````````````````````````

| Offset | Bytes | Decoded |
| --- | --- | --- |
| 0x74cc | 23 49 01 22 20 46 7e 44 fc f7 be e8 | UI_SET_EVBIT, EV_KEY (1) |
| 0x74d8 | 20 49 02 22 20 46 fc f7 ba e8 | UI_SET_EVBIT, EV_REL (2) (vendor typo, harmless) |
| 0x74e2 | 1e 49 14 22 20 46 fc f7 b4 e8 | UI_SET_EVBIT, EV_REP (0x14) ← U1 target |
| 0x74ec | 1b 49 00 22 20 46 fc f7 b0 e8 | UI_SET_EVBIT, EV_SYN (0) |

NOPing only the third call drops `EV_REP` from `dev->evbit` without disturbing the other event-class claims. Linux's `input_register_device()` calls `input_enable_softrepeat(dev, 250, 33)` only if `EV_REP` is set — by NOT claiming it, the kernel never schedules the soft-repeat timer for this device. Without auto-repeat, a dropped PASSTHROUGH RELEASE no longer drives a 25 Hz `KEY_xxx REPEAT` cascade against InputDispatcher → media-key broadcast → haptic feedback (the "vibration loop" symptom on strict CTs).

Spec-correct per AVRCP 1.3 §4.6.1 (PASS THROUGH command, defined in AV/C Panel Subunit Specification ref [2]): the CT is responsible for periodic re-send during a held button; the TG forwards one event per frame, not synthesizing extras at the input layer. Local Y1 hardware buttons are unaffected — they go through `mtk-kpd` (event0) / `mtk-tpd-kpd` (event3), not the patched AVRCP uinput device.

### LOAD #1 program-header surgery

The patcher writes the trampoline blob into LOAD #1's page-alignment padding (4020 zero bytes between LOAD #1's stock end at file `0xac54` and LOAD #2's start at `0xbc08`) and bumps LOAD #1's `p_filesz` and `p_memsz` to map the new code as R+E. The 4020-byte cap is a hard ceiling: the patcher asserts on overflow rather than silently truncating into LOAD #2's GOT. No other section / segment offsets shift; `.dynsym` / `.text` / `.rodata` / `.dynamic` / `.rel.plt` etc. all stay byte-identical. The patcher prints the exact post-patch LOAD #1 size on every run.

`g_avrcp_req_event_database` (15 bytes at vaddr `0xd2b5`) lives in pre-existing `.bss` padding — costs zero bytes in LOAD #1's budget because `.bss` is zero-filled at load time and `clear_event_database` re-zeros it on each CT-connection boundary anyway.

MD5s: Stock + current release/debug MD5s are pinned in `patch_libextavrcp_jni.py`'s `STOCK_MD5` / `OUTPUT_MD5` / `OUTPUT_DEBUG_MD5` constants; the patcher prints them on every run and verifies the output against the pinned values.

For the full architectural reference (data-path diagram, response-builder calling conventions, ELF program-header surgery details, code-cave inventory, msg-id taxonomy, Thumb-2 encoding gotchas), see [`ARCHITECTURE.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FARCHITECTURE.md).

## `patch_libextavrcp.py`

Single 2-byte Thumb-2 CBZ→NOP flip inside `btmtk_avrcp_send_get_element_attributes_rsp` (function entry at `0x2188`).

E1 at file `0x00002266` (2 bytes): `88 b3 → 00 bf` (CBZ r0, +0x62 → NOP T1). The function's per-attribute loop has a gate that skips the emit path when `(attr_id == 0) OR (strlen == 0)`, logging `"AVRCP send_get_element_attributes ignore empty attrib attri_id:%d strlen:%d"` instead of writing the attribute slot into the response buffer. The strlen-zero half of this gate is a deviation from AVRCP 1.3 §5.3.1 Table 5.24:

"For attributes not supported by the TG, this field shall be sent with 0 length data."

Patching the CBZ to a NOP makes execution fall through unconditionally to the emit path. Empty-value attributes are now emitted with `AttributeID + CharsetID + AttributeValueLength=0` (no value bytes), per spec. The attr_id=0 ("Not Used" per §26 Table 26.1) half of the gate also collapses, but `T4` in `libextavrcp_jni.so` never emits attr 0, so that side has no caller.

Strict CTs in the test matrix request a specific attribute set in their metadata-pane query (one such CT requests `[0x1, 0x2, 0x3, 0x6, 0x8, 0x7]`) and gate render on receiving every requested attribute back. Without E1, Y1 silently drops any whose value isn't set on its side, and the CT refuses to render. Lenient CTs were already rendering — they pick out what they recognize from the response.

MD5s: Stock `6442b137d3074e5ac9a654de83a4941a` → Output `1347e1b337879840ad2f66597836b05f`.

## `patch_mtkbt_odex.py`

Patches `MtkBt.odex` with four byte edits and recomputes the DEX adler32 checksum embedded in the ODEX header.

F1 at file `0x3e0ea` (1 byte): `0a → 0e`. `BTAvrcpProfile.getPreferVersion()` returns the BlueAngel-internal flag value 14 instead of 10. This is internal flag bookkeeping inside MtkBt's Java-side dispatcher — it unblocks 1.3+ command handling on a stack that was originally compiled for an earlier AVRCP version. The wire shape is unchanged; we ship AVRCP 1.3 PDUs only. See [`BT-COMPLIANCE.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FBT-COMPLIANCE.md) §1.

F2 at file `0x03f21a`: `BluetoothAvrcpService.disable()` resets `sPlayServiceInterface = false`. Fixes a BT-toggle bug where the service tears itself down prematurely on second activation because the flag is left stale across restarts.

Cardinality NOP — TRACK_CHANGED at file `0x03c530`: NOPs the `if-eqz v5, :cond_184` cardinality gate in `BTAvrcpMusicAdapter.handleKeyMessage`'s sswitch_1a3 (event 0x02 case). Java's `mRegisteredEvents` BitSet is permanently empty (Java-side AVRCP TG bookkeeping isn't updated by our trampolines), so without this NOP `notificationTrackChangedNative` is never invoked. With it, the native fires on every `metachanged` broadcast emitted by the music app and lands in T5 (libextavrcp_jni.so). Pairs with T5.

Cardinality NOP — PLAYBACK_STATUS_CHANGED at file `0x03c4fe`: same idiom for sswitch_18a (event 0x01 case). Without this, `notificationPlayStatusChangedNative` is never invoked. With it, the native fires on every `playstatechanged` broadcast and lands in T9. Pairs with T9.

MD5s: Stock `11566bc23001e78de64b5db355238175` → Output `00cc642742044286966cbb7b01135ca7`.

## `patch_libaudio_a2dp.py`

Single-byte cond-flip in `_ZN20android_audio_legacy18A2dpAudioInterface18A2dpAudioStreamOut9standby_lEv` (the AOSP A2DP HAL's standby path).

AH1 — `beq 8684 → b 8684` at file `0x000086ab` (1 byte): `0x0a` → `0xea`. ARM condition-code flip from `EQ` to `AL` (always). Forces standby_l's `if (mIsStreaming != 0) call a2dp_stop` guard to ALWAYS skip the call site. The instructions at 0x86ac-0x86b8 (`ldr r0, [r4,#40]; bl a2dp_stop@plt; mov r5, r0; b 8684`) become unreachable; standby still completes (`release_wake_lock`, `mStandby = 1`, return) but no AVDTP SUSPEND fires on the wire.

Why this site. AudioFlinger's silence-timeout (~3 s after the music app stops writing samples) calls `A2dpAudioStreamOut::standby` → `standby_l`, the only HAL-side path that calls `a2dp_stop`. NOPing that call leaves the AVDTP source stream alive while AudioFlinger thinks the HAL is in standby; the next `write()` after PLAYING resumes pushes samples into the same open AVDTP session. Per AVDTP 1.3 §8.14 / §8.15: PAUSED leaves the source stream paused-but-up; SUSPEND is reserved for explicit policy changes.

MD5s: Stock `0d909a0bcf7972d6e5d69a1704d35d1f` → Output `adbd98afeb5593f1ffe3b90acd0f2536`.

## `patch_avrcp_kl.py`

Single-line text edit to `/system/usr/keylayout/AVRCP.kl` — the keylayout file that maps Linux input keycodes from the AVRCP uinput device (`/dev/input/event4`, created by `libextavrcp_jni.so`'s `avrcp_input_init`) to Android keycodes consumed by the app layer.

K1 — row 201: `MEDIA_PLAY_PAUSE` → `MEDIA_PAUSE` at file offset `0x2ac` (35 bytes, length-preserving):````````````

|  | bytes (ASCII) | meaning |
| --- | --- | --- |
| before | key 201 MEDIA_PLAY_PAUSE WAKEn | Linux KEY_PAUSECD (201) → Android KEYCODE_MEDIA_PLAY_PAUSE (85, toggle) |
| after | key 201 MEDIA_PAUSE WAKEn | Linux KEY_PAUSECD (201) → Android KEYCODE_MEDIA_PAUSE (127, discrete) |

The stock file has the standard AOSP copyright header (2010); the `key 201 MEDIA_PLAY_PAUSE` mapping predates Android's discrete `KEYCODE_MEDIA_PAUSE` (127) and coalesces both `0x44 PLAY` and `0x46 PAUSE` PASSTHROUGH commands into the toggle key. AVRCP 1.3 §4.6.1 + ICS Table 8 define `PASSTHROUGH 0x46 PAUSE` as a DISCRETE Optional command distinct from `0x44 PLAY`; the AOSP coalescing is a spec deviation.

End-to-end flow post-K1. CTs that send PASSTHROUGH 0x46 PAUSE (rather than 0x44 PLAY-as-toggle):`PASSTHROUGH 0x46 PAUSE (CT → Y1, AV/C wire) → libextavrcp_jni.so avrcp_input_sendkey table @ 0xccec entry 2 → Linux KEY_PAUSECD (201) on /dev/input/event4 → AVRCP.kl row 201 (K1-patched) → Android KEYCODE_MEDIA_PAUSE (127) → BaseActivity.dispatchKeyEvent (Patch H: propagate for 127) → PlayControllerReceiver.onReceive → cond_pause_strict (Patch E: 127 → pause(0x12, true)) → PlayerService.pause(0x12, true) ← discrete pause, idempotent`

Row 200 (`KEY_PLAYCD → MEDIA_PLAY`) is unchanged. CTs that send `PASSTHROUGH 0x44 PLAY` (the older toggle convention) continue to route through `PlayControllerReceiver.cond_play_strict` (`if isPlaying: playOrPause() else play(true)` — discrete-with-toggle-fallback), preserving the existing toggle UX for those CTs.

MD5s: Stock `366670c4f944150bd657d9377839463a` (identical across firmware 3.0.2 and 3.0.7) → Output `dfd9afd58e94c38fc6f92592674b4ef1`. `KNOWN_AVRCP_KL_MD5S` in the patcher maps each known firmware build to its expected stock MD5; a future build that diverges (e.g. Innioasis ships an updated AVRCP.kl with a different layout) gets a clean MD5-mismatch report rather than silent miscompare.

## `patch_y1_apk.py`

Smali-level patches to the music app `com.innioasis.y1*.apk` via apktool. Four patches inside two DEX files (`classes.dex` + `classes2.dex`); the original `META-INF/` signature block is retained verbatim because PackageManager rejects an unsigned APK at boot even for system apps. Output to `output/com.innioasis.y1_<version>-patched.apk`. See the patcher's docstring for full DEX-level analysis (register layouts, instruction offsets, SQL query, etc.).

Patch A in `smali_classes2/com/innioasis/music/ArtistsActivity.smali` — `confirm()` artist-tap branch: replaces the in-place `switchSongSortType()` flat-song-list call with an Intent launching `AlbumsActivity` carrying the `artist_key` extra.

Patch B in `smali_classes2/com/innioasis/music/AlbumsActivity.smali` — `initView()`: rebuilds the method (`.locals 2 → .locals 8`) to read the `artist_key` extra and, if present, query `SongDao.getSongsByArtistSortByAlbum(artist)` and feed a deduplicated `ArrayList<String>` of album names through `AlbumListAdapter.setAlbums()`. If absent, falls through to the original `getAlbumListBySort()` path so the standalone Albums screen still works.

Patch C in `smali/com/innioasis/y1/database/Y1Repository.smali` (field decl): `private final songDao` → `public final songDao` so AlbumsActivity (different package) can `iget-object` it without an `IllegalAccessError`. The Kotlin-generated `access$getSongDao$p` exists but exhibits unreliable `NoSuchMethodError` on this device's old Dalvik (API 17).

Patch E in `smali_classes2/com/innioasis/y1/receiver/PlayControllerReceiver.smali` at `:cond_c` — splits the short-press `KEY_PLAY → playOrPause()` branch into six discrete arms per AVRCP 1.3 §4.6.1 (PASS THROUGH command, op codes defined in AV/C Panel Subunit Specification ref [2]; concrete frame example in AVRCP 1.3 §19.3 Appendix D) and ICS Table 8 (Cat 1 op_id status):``````````````````````````````````````````````````````````````

| keyCode | Source | Action | ICS Table 8 status |
| --- | --- | --- | --- |
| KEY_PLAY (85, KEYCODE_MEDIA_PLAY_PAUSE) | Legacy ACTION_MEDIA_BUTTON Intent (single physical play / pause key) | playOrPause()V (toggle) | n/a (toggle is a Y1-side abstraction) |
| KEYCODE_MEDIA_PLAY (0x7e = 126) | PASSTHROUGH 0x44 → Linux KEY_PLAYCD (200) → AVRCP.kl MEDIA_PLAY | play(Z)V with bool=true | item 19 — M (mandatory) |
| KEYCODE_MEDIA_PAUSE (0x7f = 127) | PASSTHROUGH 0x46 → Linux KEY_PAUSECD (201) → AVRCP.kl MEDIA_PLAY_PAUSE | pause(IZ)V with reason=0x12, flag=true | item 21 — O (optional) |
| KEYCODE_MEDIA_STOP (0x56 = 86) | PASSTHROUGH 0x45 → Linux KEY_STOPCD (166) → AVRCP.kl MEDIA_STOP | stop()V | item 20 — M (mandatory) |
| KEYCODE_MEDIA_NEXT (0x57 = 87) | PASSTHROUGH 0x4B → Linux KEY_NEXTSONG (163) → AVRCP.kl MEDIA_NEXT | nextSong()V | item 26 — O (optional) |
| KEYCODE_MEDIA_PREVIOUS (0x58 = 88) | PASSTHROUGH 0x4C → Linux KEY_PREVIOUSSONG (165) → AVRCP.kl MEDIA_PREVIOUS | prevSong()V | item 27 — O (optional) |

Each arm calls the corresponding `PlayerService` method per AV/C Panel Subunit Spec semantics. `play(true)` runs `Static.setPlayValue()` after `IjkMediaPlayer.start()` to propagate the resume edge to the rest of the app. `pause(0x12, true)` tags the discrete PASSTHROUGH path (existing stock pause-reason values span `0xc..0x11`). `nextSong()` / `prevSong()` are the discrete-track variants distinct from FAST_FORWARD (0x49) / REWIND (0x48); reached only via Patch H/H′'s propagation path. `playOrPause()` keeps the legacy single-physical-key toggle semantic.

Patched smali (apktool renames the user-defined labels `:cond_play_pause_toggle / :cond_play_strict / :cond_pause_strict / :cond_stop_strict / :cond_next_strict / :cond_prev_strict` to alphanumeric `:cond_X` on reassembly):`:cond_c [KeyMap.getKEY_PLAY()] if-eq v2, p1, :cond_play_pause_toggle # 85 → toggle const/16 p1, 0x7e if-eq v2, p1, :cond_play_strict # 126 → play(true) const/16 p1, 0x7f if-eq v2, p1, :cond_pause_strict # 127 → pause(0x12, true) const/16 p1, 0x56 if-eq v2, p1, :cond_stop_strict # 86 → stop() const/16 p1, 0x57 if-eq v2, p1, :cond_next_strict # 87 → nextSong() const/16 p1, 0x58 if-eq v2, p1, :cond_prev_strict # 88 → prevSong() goto :cond_e # no match → existing fall-through [six labeled arms, each ending in goto :goto_5]`

Uses scratch registers `v0` (bool / reason) and `v3` (flag) which are dead at this point in the `.locals 6``onReceive` method. The next/prev arms only need `p1` (PlayerService) and don't touch `v0` / `v3`. apktool optimizes the no-match `goto :cond_e` to `goto :goto_5` since stock's `:cond_e` sits immediately before `:goto_5` (same control flow).

Patch H in `smali/com/innioasis/y1/base/BaseActivity.smali` — propagate unhandled discrete media keys.

`BaseActivity.dispatchKeyEvent` is the foreground entry point for every music-app Activity (all extend `BaseActivity`). Stock returns `v0=1` (consumed) unconditionally, including for keycodes the activity doesn't handle — so `KEYCODE_MEDIA_PLAY` (126), `MEDIA_PAUSE` (127), `MEDIA_STOP` (86) never reach `PhoneFallbackEventHandler` → `AudioService` → `ACTION_MEDIA_BUTTON` → `PlayControllerReceiver`.

Patched: insert an early-return block after `move-result v2` gated on `keyCode ∈ {0x7e, 0x7f, 0x56, 0x57, 0x58}`. Check `KeyEvent.getRepeatCount()`: if `> 0` (framework-synthesized repeat — see Patch H″), silently consume (return TRUE); if `== 0` (genuine first press), return FALSE so the framework continues dispatch.`[stock through `move-result v2`] const/16 v3, 0x7e if-eq v2, v3, :patch_h_avrcp_key const/16 v3, 0x7f if-eq v2, v3, :patch_h_avrcp_key const/16 v3, 0x56 if-eq v2, v3, :patch_h_avrcp_key const/16 v3, 0x57 if-eq v2, v3, :patch_h_avrcp_key const/16 v3, 0x58 if-eq v2, v3, :patch_h_avrcp_key goto :patch_h_continue :patch_h_avrcp_key invoke-virtual {p1}, KeyEvent;->getRepeatCount()I move-result v3 if-eqz v3, :patch_h_propagate return v0 # repeat: consume silently (v0 is still 1 from method entry) :patch_h_propagate const/4 v0, 0x0 return v0 # first press: let the framework continue dispatch :patch_h_continue const/4 v3, 0x3 # original next instruction [stock continues unchanged]`

`v3` is reused as scratch then overwritten by the next instruction (or by the `getRepeatCount()` result); `v0` is set to 0 only on the propagate path which immediately returns. The patched method semantically becomes "for AVRCP-derived keycodes, propagate the first press to the framework media-button path and silently swallow framework-synthesized repeats; for everything else, behave exactly as stock."

Keycode set: `0x7e MEDIA_PLAY`, `0x7f MEDIA_PAUSE`, `0x56 MEDIA_STOP`, `0x57 MEDIA_NEXT`, `0x58 MEDIA_PREVIOUS`. Note: AVRCP.kl maps PASSTHROUGH 0x46 PAUSE → `KEY_PAUSECD` (201) → `KEYCODE_MEDIA_PLAY_PAUSE` (85), NOT MEDIA_PAUSE (127), so 0x7f comes from CTs that emit a discrete pause keycode (some Android-side AVRCP profile transformers do, on top of standard AV/C). 0x57 / 0x58 are added even though the activity's KeyMap.KEY_RIGHT / KEY_LEFT entries match them (87 / 88) because the existing `BasePlayerActivity` arms conflate AVRCP NEXT (op 0x4B) with hardware-wheel-RIGHT-LONG-press FF/scrub. AVRCP 1.3 §4.6.1 separates op 0x4B (NEXT) from op 0x49 (FAST_FORWARD); we honour that separation by routing 0x57 to the dedicated `nextSong()` arm in Patch E.

Side effect on hardware NEXT/PREV touch buttons (event2 mtk-tpd also emits keycodes 87/88): holding such a button no longer enters FF/RW; it produces a single nextSong()/prevSong() per tap. Matches the AVRCP-spec semantic but diverges from prior stock behaviour. The hardware scroll wheel uses different keycodes (KeyMap.KEY_UP=21 DPAD_LEFT, KEY_DOWN=22 DPAD_RIGHT) and is unaffected.

Upstream-compatibility note. This patch lives entirely inside the music app's APK. Other foreground apps installable on the device (e.g. Rockbox) extend `AppCompatActivity` directly and do not inherit from `com.innioasis.y1.base.BaseActivity`, so their AVRCP key handling is unaffected. The keylayout `/system/usr/keylayout/AVRCP.kl` stays stock — the kernel→`KeyEvent` mapping continues to deliver `KEYCODE_MEDIA_PLAY` (126) for op_id 0x44, which is the spec-correct keycode for any app that handles standard Android media keys.

Patch H′ in `smali_classes2/com/innioasis/y1/base/BasePlayerActivity.smali` — same propagation, applied to the music-player superclass.

`MusicPlayerActivity` and other player-screen activities extend `BasePlayerActivity`, which overrides `dispatchKeyEvent` and `return p1=1` unconditionally — `BaseActivity.dispatchKeyEvent` (Patch H) is unreachable from those screens. `BasePlayerActivity.onKeyUp` matches only `KeyMap` entries (KEY_LEFT=88, KEY_RIGHT=87, KEY_MENU=4, KEY_ENTER=66, KEY_PLAY=85), so discrete media keycodes 126/127/86 fall through and get silently consumed.

Patched: insert the same five-keycode early-return block at the top of `BasePlayerActivity.dispatchKeyEvent`, with the same `repeatCount > 0 → silent consume` filter as Patch H, before the `Intrinsics.checkNotNull` call (defensive null-safe ordering):`[method header + .locals 2] invoke-virtual {p1}, KeyEvent;->getKeyCode()I move-result v0 const/16 v1, 0x7e if-eq v0, v1, :patch_h2_avrcp_key const/16 v1, 0x7f if-eq v0, v1, :patch_h2_avrcp_key const/16 v1, 0x56 if-eq v0, v1, :patch_h2_avrcp_key const/16 v1, 0x57 if-eq v0, v1, :patch_h2_avrcp_key const/16 v1, 0x58 if-eq v0, v1, :patch_h2_avrcp_key goto :patch_h2_continue :patch_h2_avrcp_key invoke-virtual {p1}, KeyEvent;->getRepeatCount()I move-result v0 if-eqz v0, :patch_h2_propagate const/4 v0, 0x1 return v0 # repeat: consume silently :patch_h2_propagate const/4 v0, 0x0 return v0 # first press: let the framework continue dispatch :patch_h2_continue [stock method body resumes]`

`v0` and `v1` are the existing scratch locals (`.locals 2` covers both). Returning false from `BasePlayerActivity.dispatchKeyEvent` causes the framework to fall through to `PhoneFallbackEventHandler` → `AudioService` → `ACTION_MEDIA_BUTTON` broadcast, where `PlayControllerReceiver`'s Patch E discrete arms then fire. Returning true on a repeat is the no-action consume path.

Patch H″ — framework-synthetic-repeat filter, paired with NEXT/PREV keycode propagation. Logically a single change embedded in both Patch H and Patch H′.

Android 4.2.2's `InputDispatcher::synthesizeKeyRepeatLocked` synthesizes `KeyEvent` repeats independently of the kernel's `EV_REP` (which U1 patches off in `libextavrcp_jni.so:0x74e8`); for AVRCP-derived keycodes those synthetic repeats trigger `BasePlayerActivity.onKeyLongPress` at `repeatCount == 8` → music app enters FF/RW mode and stays stuck if the CT drops PASSTHROUGH RELEASE under subscribe load. H″ filters them: `getRepeatCount() > 0` → return TRUE (silent consume); `== 0` → propagate normally. Applies in both `BaseActivity` (Patch H) and `BasePlayerActivity` (Patch H′). The addition of `0x57` / `0x58` to the propagated keycode set is also part of H″.

Patch B3 — `com.koensayr.PappSetReceiver` for AVRCP-driven Repeat / Shuffle Sets.

BroadcastReceiver class registered dynamically from `Y1Application.onCreate`. Listens for two actions:````````````

| Action | Extra | Calls |
| --- | --- | --- |
| com.koensayr.y1.bridge.SET_REPEAT_MODE | value:I (Y1 enum 0/1/2 = OFF/ONE/ALL) | SharedPreferencesUtils.setMusicRepeatMode(I) |
| com.koensayr.y1.bridge.SET_IS_SHUFFLE | value:Z | SharedPreferencesUtils.setMusicIsShuffle(Z) |

Same setters the in-app Settings screen calls when the Y1 user toggles Repeat / Shuffle, so `PlayerService` re-reads SharedPreferences at the next track-end and the playback behavior changes without an app restart. Receiver class lives under `com.koensayr.*` to avoid collisions with the existing `com.innioasis.y1.*` tree. The live CT-Set consumer is B5's `PappSetFileObserver`; B3 stays in tree as a no-op safety net.

Patch B4 — `com.koensayr.PappStateBroadcaster` for Y1-side Repeat / Shuffle CHANGED relay.

`OnSharedPreferenceChangeListener` against the `"settings"` SharedPreferences (the same prefs file `SharedPreferencesUtils` reads/writes), registered from `Y1Application.onCreate`. Fires for any write to any key, filters to two:````

| Key | Maps to | AVRCP 1.3 Appendix F |
| --- | --- | --- |
| musicRepeatMode (int 0/1/2) | AVRCP repeat 0x01/0x02/0x03 (OFF/SINGLE/ALL) | attribute 0x02 |
| musicIsShuffle (boolean) | AVRCP shuffle 0x01/0x02 (OFF/ALL_TRACK) | attribute 0x03 |

On match, reads both live values via `SharedPreferencesUtils.INSTANCE.getMusicRepeatMode()` / `getMusicIsShuffle()`, maps to the AVRCP enum bytes, calls `TrackInfoWriter.setPapp(repeat, shuffle)` so the music-app `y1-track-info[795..796]` reflects the new state immediately, and fires `com.android.music.playstatechanged` so MtkBt's BluetoothAvrcpReceiver wakes T9 → AVRCP §5.4.2 Tbl 5.36 `PLAYER_APPLICATION_SETTING_CHANGED` CHANGED via PLT `0x345c`.

`Y1Application.onCreate` calls `sendNow()` once on registration so a fresh music-app start syncs the file + downstream state to actual SharedPreferences values. The broadcaster also stashes itself in a static `sInstance` field so the GC doesn't reclaim it (Android's SharedPreferences holds `OnSharedPreferenceChangeListener` instances by weak reference — without a strong rooting reference the listener stops firing after the next GC cycle).

Patch B5 — in-app `y1-track-info` production (`com.koensayr.y1.*` injected classes).

The music app is the canonical writer of the 2213-byte double-buffer `y1-track-info` schema (1-byte `active_slot` + 3 B pad + 2 × 1104-byte slots + 1 B pad) and the 2-byte `y1-papp-set` (initial create). Both files live in `/data/data/com.innioasis.y1/files/`. The trampoline chain in `libextavrcp_jni.so` reads `y1-track-info` via `mmap2` + active-slot dispatch (see [`patch_libextavrcp_jni.py`](#patch_libextavrcp_jnipy) preamble), accesses trampoline edge state via PC-relative loads from `.bss` at `G_Y1_TRAMPOLINE_STATE_VADDR = 0xd2d6` (zero syscalls), and writes `y1-papp-set` via `open + write + close` (rare — only on CT-initiated PApp Set).

Four new classes under `com/koensayr/y1/` (smali sources at `src/patches/inject/com/koensayr/y1/`, copied into `smali/` — the primary DEX — at patcher time, so they load with `Y1Application` itself; `smali_classes2/` would route through `MultiDex.install`'s cache at `/data/data/com.innioasis.y1/code_cache/secondary-dexes/` which survives `/system/app/` reflashes and stales out the new classes):``````````````````````````````````````````````````````````````````````````````````````````````````````````````````````

| Class | Role |
| --- | --- |
| trackinfo.TrackInfoWriter | Singleton state holder + double-buffer file writer (RandomAccessFile.seek+write, atomic single-byte active_slot flip, world-readable). Per-slot 1104-byte schema: audio_id at bytes 0..7 via `syntheticAudioId(path) = (path.hashCode() & 0xFFFFFFFFL) |
| playback.PlaybackStateBridge | Stateless static dispatcher. onPlayValue(II)V maps the music-app's Static.setPlayValue newValue (0/1/3/5) to the AVRCP §5.4.1 Tbl 5.26 byte (STOPPED/PLAYING/PAUSED) then calls TrackInfoWriter.wakePlayStateChanged() so T9 emits PLAYBACK_STATUS / POS CHANGED on the state edge. On the PLAYING edge it also starts PositionTicker; on PAUSED / STOPPED it stops it. onCompletion()V latches a natural-end signal; the next onPrepared()V consumes it into mPreviousTrackNaturalEnd, resets position+time, then calls wakeTrackChanged() + wakePlayStateChanged() so T5 emits TRACK_CHANGED / REACHED_END / REACHED_START and T9 emits PLAYBACK_POS CHANGED for the position reset. onError()V clears the latch. Reason-1 init-seed suppression: when the call's reason argument is exactly 1, onPlayValue returns immediately without touching any state. That reason value is emitted exclusively by MusicPlayerActivity.initView() line 288 (const/4 v4, 0x1 / setPlayValue(v4, v4)), which seeds Static.mPlayValue as the Activity reaches its first valid-music-list branch — purely to render the local play glyph. The same initView() body invoked pause$default(0xc, false, 2) ~9 ms earlier (pause$default with flags=0x2 forces the boolean to true → reaches PlayerService.pause(IZ)'s setPlayValue(3, 3) emit). Without this suppression the AVRCP wire would ship PSC CHANGED PAUSED → PSC CHANGED PLAYING in rapid succession and CTs would see the trailing PLAYING after a user PAUSE, refusing to flip their pause→play button glyph. Static.setPlayValue still updates mPlayValue after we return, so the on-device UI is unaffected. Track-change blip suppression: markTrackChange()V sets a 1s trackChangeDeadlineMs (on SystemClock.elapsedRealtime) — called from PlayerService.restartPlay(Z) / autoSwitch() / nextSong() / prevSong() entry prepends. While inside that window onPlayValue SUPPRESSES both setPlayStatus(2) AND wakePlayStateChanged() for newValue=3 (PAUSED) so the transient pause→play handshake inside restartPlay doesn't ship a spurious pstat=PAUSED CHANGED to the CT (which trips subscription-class CTs' rapid-state-change back-off heuristics). Both suppressions are required: without skipping setPlayStatus, an in-flight PositionTicker broadcast (queued ~1 s before the track-switch) reaches mtkbt AFTER file[792] has flipped to 2 and T9 emits pstat=2 regardless of whether our own wake fired. With both skipped, file[792] stays at the prior PLAYING value through the blip, in-flight T9 sees no edge, and the CT only learns about the new track via the subsequent TRACK_CHANGED CHANGED from wakeTrackChanged() (which is NEVER suppressed). The downstream PositionTicker start/stop is unaffected. |
| playback.PositionTicker | Runnable posted to a main-thread Handler every 1000 ms while playing. Each tick calls TrackInfoWriter.wakePlayStateChanged() so T9 emits PLAYBACK_POS_CHANGED CHANGED with the live-extrapolated position. Started from PlaybackStateBridge.onPlayValue on PLAYING edges, stopped on PAUSED / STOPPED. AVRCP 1.3 §5.4.2 Tbl 5.33 leaves the cadence to the TG; 1 s is the conventional minimum interval a 1.3 CT will display playhead at. |
| battery.BatteryReceiver | Intent.ACTION_BATTERY_CHANGED consumer. Bucket-maps to AVRCP §5.4.2 Tbl 5.35 (FULL_CHARGE / EXTERNAL / CRITICAL / WARNING / NORMAL). Sticky-broadcast value is processed at registration time so cold boot has a real bucket before the next CHANGED tick. |
| papp.PappSetFileObserver | FileObserver on /data/data/com.innioasis.y1/files/y1-papp-set (CLOSE_WRITE). T_papp 0x14 in libextavrcp_jni.so writes the file on every CT-initiated PApp Set; the observer reads the 2-byte (attr_id, value) tuple and calls SharedPreferencesUtils.setMusicRepeatMode / setMusicIsShuffle directly — no Intent hop. |

Existing-file edits (smali prepends, no logic replacement):``````````````````````````````````````````````````````````````````````````````

| File | Inject |
| --- | --- |
| smali_classes2/com/innioasis/y1/utils/Static.smali | Top of setPlayValue(II)V — invoke-static {p1, p2}, …PlaybackStateBridge;->onPlayValue(II)V. Single canonical state-edge entry; catches every play/pause/stop/resume regardless of UI foreground state. |
| smali/com/innioasis/y1/service/PlayerService.smali | Top of six listener lambdas (initPlayer$lambda-{10,11,12} IjkMediaPlayer Bilibili-IJK OnCompletion/OnPrepared/OnError; initPlayer2$lambda-{13,14,15} same for android.media.MediaPlayer) — each gets one invoke-static to the matching PlaybackStateBridge callback. Plus setCurrentPosition(J)V head (B5.2a) → PlaybackStateBridge.onSeek; toRestart()V 3 × setDataSource sites (B5.2b) → PlaybackStateBridge.onEarlyTrackChange (~100-500 ms early TRACK_CHANGED before prepareAsync completes); playerPrepared()V 2 × iput-boolean playerIsPrepared:=true sites (B5.2c) → PlaybackStateBridge.onPlayerPreparedTail (post-prepare flush so getDuration() is captured before broadcasting; without this, flushLocked from OnPreparedListener runs ~26 ms before the prepared flag flips and reports the previous track's stale duration); restartPlay(Z) / autoSwitch() / nextSong() / prevSong() heads (B5.2t) → PlaybackStateBridge.markTrackChange (sets the 1s deadline that suppresses the pause-blip pstat=PAUSED CHANGED emit during track-switch pause→play handshake). |
| smali/com/innioasis/y1/Y1Application.smali | onCreate:cond_3 block, between B3 and B4. Brings up TrackInfoWriter.init(Context) + PappSetFileObserver.start(Context) + BatteryReceiver.register(Context). Order matters: must run before B4's sendNow() so the cold-boot file write reflects live SharedPreferences Repeat/Shuffle, not the default OFF/OFF. |
| smali/com/koensayr/PappStateBroadcaster.smali (B4 product) | sendNow() tail — calls TrackInfoWriter.setPapp(repeat, shuffle) so the music-app file reflects the new state immediately, then fires com.android.music.playstatechanged so MtkBt's BluetoothAvrcpReceiver wakes T9 to emit PApp CHANGED on the wire. |
| smali/com/koensayr/y1/battery/BatteryReceiver.smali | onReceive tail — fires com.android.music.playstatechanged after each bucket transition so T9 reads the new file[794] and emits BATT_STATUS_CHANGED CHANGED. |

State sources, all read live from `PlayerService` accessors via `Y1Application.Companion.getPlayerService()`: `getPlayingMusic()`/`getPlayingSong()` for the current `Song` (title via `getSongName()`, plus `getArtist`/`getAlbum`/`getGenre`/`getPath`); `getDuration()`; `getMusicIndex()+1` for TrackNumber; `getMusicList().size()` for TotalNumberOfTracks. Position-at-state-change is captured at the `setPlayValue` edge with `SystemClock.elapsedRealtime()` for the lockstep clock the trampoline `T6` extrapolation expects.

Duration has a fallback path: `PlayerService.getDuration()` delegates to `IjkMediaPlayer/MediaPlayer.getDuration()` and throws between `setDataSource` and `OnPrepared`, so `flushLocked` gates on `getPlayerIsPrepared()`. The unprepared branch consults `getMmrDurationLocked(path, audio_id)` — a per-`audio_id` cache backed by `MediaMetadataRetriever.setDataSource(path).extractMetadata(METADATA_KEY_DURATION)` (synchronous container-header parse, no MediaPlayer dependency). This guarantees the first T4 `GetElementAttributes` response on every track skip carries a valid `attribute 0x07 PlayingTime`. AVRCP 1.3 has no `DURATION_CHANGED` event, so a CT that caches `dur=0` from a fresh-track T4 would keep it until the next track change — MMR closes that gap.

Patch B6 — AvrcpBinder smali (unused groundwork).

Two new classes routed to `smali_classes2/` (secondary DEX) because `classes.dex` sits at 99.7% of the 64K method cap after Patch B5:``````````````````````````````````

| Class | Role |
| --- | --- |
| avrcp.AvrcpBridgeService | Service shell. Not declared in the music APK manifest, so unreferenced at runtime. |
| avrcp.AvrcpBinder | Binder implementing IBTAvrcpMusic + IMediaPlaybackService onTransact in smali. Skips strictModePolicy + descriptor string and dispatches by transact code (descriptor mismatches across ROM variations have historically aborted registerCallback on enforceInterface). Codes implemented: 1 (registerCallback); 2 (unregisterCallback); 3 (regNotificationEvent — ACK true; returning false leaves MtkBt's mRegBit empty and notifyTrackChanged is dropped); 5 (getCapabilities — return [0x01, 0x02]); 6-13 (transport keys via sendMediaKey broadcast). Every other code: writeNoException + return true (ack-only). Not instantiated — Y1Bridge.apk hosts the live Binder MtkBt resolves to. The smali stays in tree so MtkBt.odex component-bind work doesn't have to recreate it. |

`--debug` instrumentation (gated on `KOENSAYR_DEBUG=1`; `apply.bash --debug` sets it). When enabled the patcher injects `Log.d("Y1Patch", …)` traces at every metadata-relevant entry point and inline value-bearing `_dbgKV(String key, long val)` / `_dbgLogTrampolineState(String tag)` calls at the diagnostic-critical sites. Nothing is added to release builds — helpers and call sites are gated in `patch_y1_apk.py` itself.````````````````````````````````````````````````````````````````````````

| Layer | Coverage |
| --- | --- |
| Stock smali entry traces | PlayControllerReceiver.onReceive; BaseActivity.dispatchKeyEvent + BasePlayerActivity.dispatchKeyEvent; PlayerService — play / pause / playOrPause / stop / nextSong / prevSong / restartPlay / playerPrepared / toRestart. |
| Inject-tree entry traces | TrackInfoWriter — init / setPlayStatus / onSeek / markCompletion / markError / onFreshTrackChange / onTrackEdge / setBattery / setPapp / flush / flushLocked / wakeTrackChanged / wakePlayStateChanged. PlaybackStateBridge — onPlayValue / onEarlyTrackChange / onPrepared / onPlayerPreparedTail / onCompletion / onSeek / onError. PositionTicker — start / stop / run. BatteryReceiver — register / onReceive. PappSetFileObserver — start / onEvent / dispatch. NowPlayingRefresher — onResume / onPause / refresh / run. |
| Inline value-bearing | TrackInfoWriter.onTrackEdge → onTE.old, onTE.new, onTE.EDGE_DETECTED. TrackInfoWriter.flushLocked → fL.id, fL.pos, fL.dur, fL.ps (audio_id, position-at-state-change, last-known-duration, AVRCP play-status). TrackInfoWriter.onSeek → onSeek.in, onSeek.SUPPRESSED.dtMs, onSeek.APPLIED.pos. TrackInfoWriter.setPlayStatus → sPS.from, sPS.to. PlaybackStateBridge.onPlayValue → oPV.newVal, oPV.reason. |

Tail with `adb logcat -s Y1Patch:*` to observe the metadata pipeline live; pipe to a file for post-test analysis.

Trampoline-side native debug instrumentation (`Y1T :` logcat tag). Both `patch_libextavrcp_jni.py` and `patch_mtkbt.py` (the latter only when M5 TID-echo verification is active) wire native `__android_log_print(INFO, "Y1T", ...)` calls into their respective binaries' wire-emit sites under `KOENSAYR_DEBUG=1`. These surface as `Y1T : <text>` lines in `adb logcat -s Y1T:*` and pair with the Y1Patch traces above for end-to-end visibility from Java broadcast → JNI trampoline emit → mtkbt IPC → AVCTP wire.``````````````````````````````````````````````````````````````````````````````````````

| Tag (format string) | Site | Value |
| --- | --- | --- |
| T1pdu=%02x | T4 dispatcher entry, immediately after ldrb PDU and before the cmp chain | inbound non-RegNotif AV/C CMD PDU ID. Covers GetCapabilities (0x10), PApp (0x11..0x16), InformDisplayableCharacterSet (0x17), InformBatteryStatusOfCT (0x18), GetElementAttributes (0x20), GetPlayStatus (0x30), Request/AbortContinuingResponse (0x40/0x41). RegisterNotification (0x31) is covered by T2reg. Absence of T1pdu=20 after a TRACK_CHANGED edge means the CT didn't re-fetch metadata — Identifier-change-detection failed CT-side. |
| T2reg ev=%02x | extended_T2 immediately after the PDU=0x31 check, before save_event_seq_id | confirms an inbound RegisterNotification(ev=N) CMD reached the JNI trampoline. Pairs with the outbound emit markers below to disambiguate "CT didn't subscribe to ev=N" (no T2reg ev=N) from "CT subscribed but our CHANGED gate skipped" (T2reg ev=N present, no matching T9ps / T9papp / T9pos). |
| T9ps | t9_play_status_changed before reg_notievent_playback_rsp | no-arg marker confirming PLAYBACK_STATUS_CHANGED CHANGED actually emitted. Absence after a play/pause edge means database[1] was 0. |
| T9papp | t9_papp_changed before reg_notievent_player_appsettings_changed_rsp | no-arg marker confirming PLAYER_APPLICATION_SETTING_CHANGED CHANGED actually emitted. Absence after a repeat/shuffle edge means database[8] was 0. |
| T9pos=%08x | t9_position_changed before reg_notievent_pos_changed_rsp | host-order u32 live_pos (ms) shipped on each PlaybackPositionChanged CHANGED. Sequence advancing across emits = wire-side position is live; sequence frozen or repeated = stale anchor or extrapolation broken. |
| M5wire c39=%02x | patch_mtkbt.py D1 cave at 0xf36a0, hooked from fcn.0xae418:0xae448 | byte at chan+0x39 immediately before mtkbt's AVCTP wire-frame builder encodes it as the outbound TL nibble. Fires once per outbound AVCTP frame (every RegNotif response). |
| M5dbg p8=%02x / M5dbg pd=%02x | patch_mtkbt.py D2 cave at 0xf3700, hooked from M5 cave tail at 0xf3694 | two values captured at M5 cave exit: packet[+8] (empirically 0xb8 outbound, 0xea inbound) and packet[+0xd] (the current discriminator — 0 outbound, inbound TID otherwise). Pair with M5wire c39 to verify the wire emits the per-event TID. |

Tail with `adb logcat -s Y1T:*`, or pipe through `tools/avrcp-wire-trace.py` for a timestamped pretty-print with optional `--tag` filter. Pair with `tools/btlog-parse.py --avrcp` on the simultaneously-captured `btlog.bin` for mtkbt internal log surfaces (`avctpCB`, `[AVCTP]`, `avrcp:` lines).

`AndroidManifest.xml` is NOT modified by the patcher. `com.innioasis.y1` declares `sharedUserId="android.uid.system"`, which constrains the package's signing key to the OEM platform key. Any change to AndroidManifest.xml bytes invalidates `META-INF/MANIFEST.MF`'s recorded SHA1-Digest, JarVerifier throws SecurityException, PackageParser logs "no certificates at entry AndroidManifest.xml; ignoring!", and PackageManager drops the package. JarVerifier doesn't digest-check classes.dex / classes2.dex / resources at scan time — that's why DEX-only modifications work. The intent-filter `<service>` MtkBt's `bindService` resolves to lives in Y1Bridge.apk's manifest, which is self-signed and unconstrained by the platform key requirement.

Apktool reassembly:`apktool d --no-res` decode → smali edits → `apktool b` reassemble (the post-DEX aapt step fails because resources weren't decoded, but DEX is already built by then; the script intentionally ignores the exit code). Patched DEX bytes are dropped into a copy of the original APK with `META-INF/` + `AndroidManifest.xml` preserved bit-exact.

Deployment:`adb root && adb remount && adb push <apk> /system/app/com.innioasis.y1/com.innioasis.y1.apk && adb reboot`. Do not use `adb install` — PackageManager rejects re-signed system app APKs.

## `src/su/` (root, v1.8.0+)

Source for a minimal setuid-root `su` binary installed at `/system/xbin/su` by the bash's `--root` flag. Replaces the historical adbd byte patches that broke ADB protocol on hardware (preserved diagnosis in [`INVESTIGATION.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FINVESTIGATION.md) §"adbd Root Patches (H1 / H2 / H3)").
  - `src/su/su.c` — direct ARM-EABI syscall implementation, no libc dependency. `setgid(0)` → `setuid(0)` → `execve("/system/bin/sh", ...)`. Three invocation forms: bare `su` (interactive root shell), `su -c "<cmd>"` (one-off), `su <prog> [args...]` (exec-passthrough).
  - `src/su/start.S` — ~10-line ARM Thumb-2 entry stub; extracts argc/argv/envp from the ELF process-start stack layout, calls `main`, exits via `__NR_exit`.
  - `src/su/Makefile` — cross-compile via `arm-linux-gnu-gcc`. `-nostdlib -ffreestanding -static -Os -mthumb -mfloat-abi=soft`; output ~900 bytes, statically linked, no `NEEDED` entries.

No supply chain beyond GCC + this source. No SuperSU/Magisk/phh-style binary imported; no manager APK; no whitelist. Trade-off: any process that can exec `/system/xbin/su` becomes root, which is acceptable for a single-user research device but not for a consumer ROM.

Build:`cd src/su && make` produces `src/su/build/su`. The bash references this prebuilt path; if missing, `--root` exits with a clear error pointing at `make`.

Deploy: the bash's `--root` flag does `install -m 06755 -o root -g root src/su/build/su /system/xbin/su` against the mounted system.img. Post-flash: `adb shell /system/xbin/su -c "id"` → `uid=0(root)`.

These are Koensayr's own instructions, shown here word for word.

Published by the [ryan-specter/koensayr-auto](https://innioasis.app/firmware.html?model=Y1&software=koensayr-y1) project [[1]](https://innioasis.app/firmware_info.html?repo=ryan-specter%2Fkoensayr-auto&software=koensayr-y1)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aryan-specter)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
