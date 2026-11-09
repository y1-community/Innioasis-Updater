---
title: "Bluetooth profile-stack spec compliance - Innioasis Updater"
description: "Bluetooth profile-stack spec compliance Current spec compliance state across the Bluetooth profile stack the Y1 talks to peer Controllers CTs over. AVRCP 1.3 is the prima"
language: "en"
source: "https://innioasis.app/post-install/ryan-specter-koensayr-auto-docs-bt-compliance.html"
---

# Bluetooth profile-stack spec compliance - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y1&software=koensayr-y1)

Post-install setup · Koensayr · Y1

# Bluetooth profile-stack spec compliance

A Y1 custom Software maintained by the community.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y1&software=koensayr-y1)[Install guide](../guide.html?model=Y1&software=koensayr-y1)

# Bluetooth profile-stack spec compliance

Current spec compliance state across the Bluetooth profile stack the Y1 talks to peer Controllers (CTs) over. AVRCP 1.3 is the primary target — full ICS Table 7 scorecard with M/O accounting in §2 — because that's where most of the Y1's stock behaviour was non-conformant. Adjacent profiles (A2DP, AVDTP, AVCTP, GAVDP) are in scope when their behaviour bleeds into AVRCP-level CT interop, with targeted fixes per §9 rather than full per-profile compliance scoreboards. Per-CT empirical observations behind each design choice live in [`INVESTIGATION.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FINVESTIGATION.md) "Hardware test history per CT".

For why we have a proxy at all, the current trampoline chain shape, and the calling conventions of the response builders we use, see [`ARCHITECTURE.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FARCHITECTURE.md). For per-patch byte-level reference, see [`PATCHES.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FPATCHES.md).

## 0. Spec target + citation discipline

Primary wire protocol target: AVRCP 1.3 (V13, adopted 16 April 2007), with ESR07 errata applied. AVCTP 1.2 paired per §6 SDP record. Canonical PDFs live under `docs/spec/<PROFILE>/` (gitignored — Bluetooth SIG copyright disallows redistribution; download from [https://www.bluetooth.com/specifications/specs/](https://www.bluetooth.com/specifications/specs/)):

AVRCP 1.3 (primary):
  - `docs/spec/AVRCP 1.3/AVRCP_SPEC_V13.pdf` — base spec, 93 pages.
  - `docs/spec/AVRCP 1.3/ESR07_ESR_V10.pdf` — Errata Service Release 07 (2013-12-03); §2.1 contains Erratum 4969 (SDP record AVCTP version clarification, the only formal 1.3 erratum); §2.2 carries supplementary clarifications that resolve printed typos in 1.3 wire-format tables (e.g., the 8-byte `Identifier` sentinel form for TRACK_CHANGED).
  - `docs/spec/AVRCP 1.3/AVRCP.ICS.p17.pdf` — Implementation Conformance Statement Proforma, revision p17 (2024-07-01, TCRL.2024-1, 25 pages). Authoritative TG/CT feature M/O matrix with conditional logic. Used to anchor the scorecard in §2 below.
  - `docs/spec/AVRCP 1.3/AVRCP.IXIT.1.6.0.pdf` — IXIT proforma. Companion to ICS; defines per-implementation values a tester needs (timer values, parameter ranges, declared PASSTHROUGH op_id support).

AVCTP 1.2 (paired, §6 + ESR07 §2.1 / Erratum 4969):
  - `docs/spec/AVCTP 1.2/AVCTP_SPEC_V12.pdf` — base spec.
  - `docs/spec/AVCTP 1.2/AVCTP.ICS.p10.pdf` — ICS proforma.
  - `docs/spec/AVCTP 1.2/AVCTP.TS.p12.pdf` — Test Specification.

A2DP / AVDTP / GAVDP triad (audio path, §9 references):
  - `docs/spec/A2DP 1.3/A2DP_SPEC_V13.pdf` + `ESR08_V1.0.0.pdf`.
  - `docs/spec/AVDTP 1.3/AVDTP_SPEC_V13.pdf` + `AVDTP.ICS.p14.pdf` + `AVDTP.TS.p23.pdf` + `Erratum_23224_Update_Conformance_Section.pdf`.
  - `docs/spec/GAVDP 1.3/GAVDP_SPEC_V13.pdf` + `GAVDP.ICS.p12.pdf` + `GAVDP.TS_.p8.pdf` + `Erratum_23224_Update_Conformance_Section.pdf`.

Per ICS §1.2 Table 2b, AVRCP 1.3 was deprecated 2023-02-01 and is scheduled for withdrawal 2027-02-01. We're patching a 2012 firmware that was originally qualified against AVRCP 1.0; the deprecation schedule does not block us from shipping.

Citation hygiene rule. Cite by PDU name + AVRCP 1.3 section number verified against the spec PDF's table-of-contents. Where a behavior comes from AV/C Panel Subunit Spec (PASS THROUGH op codes / press-release semantics), cite as `AVRCP 1.3 §4.6.1 (defined in AV/C Panel Subunit Spec, ref [2])`. Where the spec text contains a printed typo, cite ESR07's clarification: `AVRCP 1.3 §X.Y + ESR07 §2.2`. Section numbers must appear in the spec PDF's table of contents — anything else is a citation error. Adjacent-profile citations follow the same shape: `A2DP 1.3 §X.Y`, `AVDTP 1.3 §X.Y`, `AVCTP 1.2 §X.Y`, `GAVDP 1.3 §X.Y`.

## 1. Current coverage state

AVRCP 1.3 (primary target). The goal is AVRCP 1.3 spec-completeness so any spec-compliant 1.3+ controller renders our metadata. Scope is the latest revision of the AVRCP 1.3 spec (V13 + ESR07). Anything outside that revision is out of scope for the AVRCP scoreboard.

The one carry-out from outside the 1.3 spec proper is `MtkBt.odex` patch F1's BlueAngel-internal `getPreferVersion()` value — internal flag bookkeeping inside MtkBt's Java-side dispatcher that unblocks 1.3+ command handling on a stack that was originally compiled against AVRCP 1.0. F1 sets the flag and unblocks 1.3 dispatch; nothing in our wire shape is changed by it.

Lower BT profile stack (adjacent). A2DP, AVDTP, AVCTP, GAVDP fixes are filed in §9. Goal: spec-completeness where tractable on this hardware (every Optional row we can implement, not just observed-deviation fixes). Each entry in §9 has motivation, scope, and a verification path.

Closed: every Mandatory row of ICS Table 7, plus every Optional row.

PlayerApplicationSettings (PDUs 0x11-0x16 + event 0x08, ICS Table 7 rows 12-17 + 30).`T_papp` dispatches PDUs 0x11-0x16 internally; T8 emits event 0x08 INTERIM, T9 emits proactive CHANGED on edge. Set loop (CT→Y1): `T_papp 0x14` validates the inbound `(attr_id, value)` against the supported set, writes the pair to `/data/data/com.innioasis.y1/files/y1-papp-set`, ACKs with success; the music app's `PappSetFileObserver` consumes the CLOSE_WRITE, translates AVRCP→Y1 enum, and calls `SharedPreferencesUtils.setMusicRepeatMode/setMusicIsShuffle` directly. CHANGED loop (Y1→CT): Patch B4's `com.koensayr.PappStateBroadcaster` registers as `OnSharedPreferenceChangeListener` against the `"settings"` SharedPreferences, calls `TrackInfoWriter.setPapp(repeat, shuffle)` to update `y1-track-info[795..796]`, and triggers a `playstatechanged` wake whenever `musicRepeatMode` or `musicIsShuffle` flips (covering both CT-driven Sets and Y1-UI toggles uniformly). T9's edge detector then emits `reg_notievent_player_appsettings_changed_rsp` (PLT `0x345c`) with REASON_CHANGED. T8 0x08 INTERIM and T9 papp CHANGED both read live `[795..796]` so a fresh CT subscribe sees actual current state.

## 2. Coverage matrix — current vs spec

Anchored against ICS Table 7 (Target Features) in `docs/spec/AVRCP 1.3/AVRCP.ICS.p17.pdf` §1.5, which is the canonical M/O determination. M/O status is conditional on what other features the TG claims; the ICS encodes the conditionals explicitly. PDU = "PDU ID" byte at AV/C body offset +4. AVRCP 1.3 V13 spec sections in `docs/spec/AVRCP 1.3/AVRCP_SPEC_V13.pdf`.

Our claims that drive the conditionals: PASS THROUGH Cat 1 (V1 SDP record, ICS Table 7 item 7), GetElementAttributes Response (T4, item 20). Combining these:``````````````````````````

| ICS Table 7 row | PDU / Capability | Spec § | ICS Status (this proj) | Currently shipped | Gap |
| --- | --- | --- | --- | --- | --- |
| 2 | Accepting connection establishment (control) | §4.1.1 | M | ✓ (mtkbt) | — |
| 3-4 | Connection release | §4.1.2 | M | ✓ (mtkbt) | — |
| 5 | Receiving UNIT INFO | §4.1.3 | M | ✓ (mtkbt) | — |
| 6 | Receiving SUBUNIT INFO | §4.1.3 | M | ✓ (mtkbt) | — |
| 7 | Receiving PASS THROUGH cat 1 | §4.1.3 | M (C.1: at least one cat) | ✓ (mtkbt + Patch E) | — |
| 8 | Receiving PASS THROUGH cat 2 | §4.1.3 | C.1: not required (cat 1 satisfies) | not claimed | — |
| 9 | Receiving PASS THROUGH cat 3 | §4.1.3 | C.1: not required | not claimed | — |
| 10 | Receiving PASS THROUGH cat 4 | §4.1.3 | C.1: not required | not claimed | — |
| 11 | GetCapabilities Response (PDU 0x10) | §5.1.1 | M (C.3: M IF cat 1) | ✓ T1 | — |
| 12-15 | List / Get / Set PApp Settings (0x11–0x14) | §5.2.1–5.2.4 | C.14: M to support none or all | ✓ T_papp (Repeat + Shuffle, OFF/OFF; Set rejects 0x06 INTERNAL_ERROR — see §1) | — |
| 16-17 | PApp Setting Attribute / Value Text (0x15-0x16) | §5.2.5-5.2.6 | O | ✓ T_papp (UTF-8 "Repeat" / "Shuffle" / "Off") | — |
| 18 | InformDisplayableCharacterSet (PDU 0x17) | §5.2.7 | O | ✓ T_charset (NOT_IMPLEMENTED reject; spec-permissible for Optional PDU) | — |
| 19 | InformBatteryStatusOfCT (PDU 0x18) | §5.2.8 | O | ✓ T_battery | — |
| 20 | GetElementAttributes (PDU 0x20) | §5.3.1 | M (C.3: M IF cat 1) | ✓ T4 (all 7 Appendix E attrs: Title / Artist / Album / TrackNumber / TotalNumberOfTracks / Genre / PlayingTime, single packed frame) | — |
| 21 | GetPlayStatus (PDU 0x30) | §5.4.1 | M (C.2: M IF GetElementAttributes Response) | ✓ T6 with live position via clock_gettime(CLOCK_BOOTTIME) | — |
| 22 | RegisterNotification (PDU 0x31) | §5.4.2 | M (C.12: M IF cat 1) | ✓ T2 / extended_T2 / T8 | — |
| 23 | Notify EVENT_PLAYBACK_STATUS_CHANGED | §5.4.2 Tbl 5.29 | M (C.4: M IF GetElementAttributes + RegisterNotification) | ✓ T8 INTERIM + T9 CHANGED on edge | — |
| 24 | Notify EVENT_TRACK_CHANGED | §5.4.2 Tbl 5.30 | M (C.4) | ✓ extended_T2 INTERIM + T5 CHANGED on edge | — |
| 25 | Notify EVENT_TRACK_REACHED_END | §5.4.2 Tbl 5.31 | O | ✓ T8 INTERIM + T5 CHANGED-on-edge (gated on natural-end flag set by music app's PlaybackStateBridge.onCompletion) | — |
| 26 | Notify EVENT_TRACK_REACHED_START | §5.4.2 Tbl 5.32 | O | ✓ T8 INTERIM + T5 CHANGED-on-edge (unconditional on every track edge) | — |
| 27 | Notify EVENT_PLAYBACK_POS_CHANGED | §5.4.2 Tbl 5.33 | O | ✓ T8 INTERIM + T9 CHANGED at 1 s cadence while playing (1 s tick fires playstatechanged; T9 live-extrapolates position via clock_gettime(CLOCK_BOOTTIME)) | — |
| 28 | Notify EVENT_BATT_STATUS_CHANGED | §5.4.2 Tbl 5.34 | O | ✓ T8 INTERIM reads y1-track-info[794] (real bucket from Intent.ACTION_BATTERY_CHANGED) + T9 CHANGED-on-edge piggybacked on playstatechanged broadcast | — |
| 29 | Notify EVENT_SYSTEM_STATUS_CHANGED | §5.4.2 Tbl 5.36 | O | ✓ T8 INTERIM with 0x00 POWER_ON (canned IS the real value while trampolines run — see footnote†) | — |
| 30 | Notify EVENT_PLAYER_APPLICATION_SETTING_CHANGED | §5.4.2 Tbl 5.37 | O | ✓ T8 INTERIM + T9 proactive CHANGED, both reading live (Repeat, Shuffle) from y1-track-info[795..796] (Patch B4 PappStateBroadcaster → TrackInfoWriter.setPapp + playstatechanged → T9 edge detect) | — |
| 31-32 | Continuation (PDUs 0x40/0x41) | §5.5 | C.2: M IF GetElementAttributes Response | ✓ T_continuation explicit dispatch in T4 pre-check → AV/C NOT_IMPLEMENTED reject via UNKNOW_INDICATION path (msg=520) | — |
| 65 | Discoverable Mode | §12.1 | M | ✓ (mtkbt) | — |
| 66 | PASSTHROUGH operation supporting Press and Hold | §4.1.3 | O | ✓ (mtkbt + U1 disables kernel auto-repeat on AVRCP uinput) | — |

Mandatory rows: all hit. Optional rows: all hit. ICS Table 7 (Target Features) is fully covered.

† Event 0x07 SYSTEM_STATUS_CHANGED — INTERIM-only is intentional. While trampolines execute, the system is by definition POWER_ON; UNPLUGGED is for accessory / dock contexts that don't apply to the Y1; POWER_OFF is unobservable from inside a process that can no longer emit responses. The canned `0x00 POWER_ON` value IS the real value, so there is no edge to fire CHANGED on.

INTERIM vs. CHANGED notation reminder. AVRCP 1.3 §5.4.2 splits each event subscription into two response shapes: an immediate INTERIM carrying the current value at registration time, and an asynchronous CHANGED when the relevant condition fires. Mandatory rows 23 and 24 ship both halves. Optional rows 25 / 26 / 27 / 28 also ship both halves with real-data CHANGED-on-edge. Row 29 SYSTEM_STATUS_CHANGED ships INTERIM only (see footnote above).

ICS Table 8 (Cat 1 PASSTHROUGH op_ids — mandatory subset):``````

| op_id | Operation | ICS status | Currently shipped |
| --- | --- | --- | --- |
| 0x44 | Play (item 19) | M | ✓ Patch E → play(true) |
| 0x45 | Stop (item 20) | M | ✓ Patch E → stop()V |
| 0x46 | Pause (item 21) | O | ✓ Patch E → pause(0x12, true) |
| 0x48 | Rewind (item 23) | O | partial (mtkbt fftimer + Y1 long-press) |
| 0x49 | Fast forward (item 24) | O | partial |
| 0x4B | Forward / next track (item 26) | O | ✓ |
| 0x4C | Backward / prev track (item 27) | O | ✓ |

Mandatory cat 1 op_ids: both hit (PLAY + STOP).

### Notification events (PDU 0x31 sub-dispatch, AVRCP 1.3 §5.4.2 Tables 5.29–5.37)

The advertised set in the GetCapabilities response (T1's `EventsSupported` array) determines what a CT can register for. We advertise eight events: `{0x01, 0x02, 0x05, 0x08, 0x09, 0x0a, 0x0b, 0x0c}`. Events 0x03, 0x04, 0x06, 0x07 are not advertised; T8 / T5 / T9 still handle them if a permissive CT subscribes anyway.

Subscription gating + §5.4.2 CHANGED cadence: every inbound `RegisterNotification` CMD writes `g_avrcp_req_event_database[event_id] = seq_id + 1` (vaddr `0xd2b5`, `.bss`, 15 bytes — one byte per event_id). A nonzero byte means "subscribed in this session" and "this is the inbound AVCTP TID to echo on the matching CHANGED." T5 / T9 read the table at every CHANGED emit site and skip when the byte is zero. The table is zeroed by `clear_event_database` on every T1 GetCapabilities so a fresh CT-connection cannot inherit stale subscriptions from a previous CT. Within a session, CHANGED emits are continuous — the gate is not cleared after emit — letting Y1's per-edge / per-tick wire cadence match the music app's broadcast rate rather than each CT's individual re-`RegisterNotification` cadence. M1 widens the cmp constant in mtkbt's RegNotif response dispatch (`fcn.0x121d8` at `0x12230`) from 1 to `0x0F`, so the dispatcher routes the JNI's reasonCode byte (IPC offset 8 = `ctxt[8]`) to the matching wire ctype: INTERIM (`0x0F`) for first-response arms, CHANGED (`0x0D`) for edge emits.

AVRCP 1.3 §4.2.1 strict TID echo on non-RegNotif PDUs: every response Y1 emits must echo the inbound CMD's AVCTP transaction label. For RegNotif INTERIM/CHANGED the database mechanism above supplies the TID. For non-RegNotif responses (GetEA / GetPlayStatus / Charset / Battery / PApp / Continuation), T4's prologue writes `conn[+0x11] = sp[+0x171]` (the inbound CMD's seq_id at the empirically-verified pre-`SUB SP` stack offset). All response builders read `conn[+0x11]` and pack it into the outbound AVCTP TL via the wire-emit chain `conn[+0x11] → msg[5] → packet[+0xa] → chan+0x39 → wire byte 0`. The same chain serves GetCapabilities responses via stock JNI's pre-R1 path, which writes `conn[+0x11]` before our hijack takes effect.````````````

| event_id | Name | Spec § | INTERIM | CHANGED on edge |
| --- | --- | --- | --- | --- |
| 0x01 | PLAYBACK_STATUS_CHANGED | §5.4.2 Tbl 5.29 | ✓ T8 | ✓ T9 on play/pause edge (gated on database[1] != 0) |
| 0x02 | TRACK_CHANGED | §5.4.2 Tbl 5.30 | ✓ extended_T2 | ✓ T5 on track edge (gated on database[2] != 0) |
| 0x05 | PLAYBACK_POS_CHANGED | §5.4.2 Tbl 5.33 | ✓ T8 | ✓ T9 at ~1Hz while playing + T5 on track edge (gated on database[5] != 0) |
| 0x08 | PLAYER_APPLICATION_SETTING_CHANGED | §5.4.2 Tbl 5.37 | ✓ T8 (reads y1-track-info[795..796]) | ✓ T9 on Repeat/Shuffle edge (gated on database[8] != 0) |
| 0x09 | NOW_PLAYING_CONTENT_CHANGED | 1.4+ event ID | ✓ T8 (zero/empty payload) | ✓ T5 on track edge + T9 on play/pause edge (gated on database[9] != 0) |
| 0x0a | AVAILABLE_PLAYERS_CHANGED | 1.4+ event ID | ✓ T8 (zero/empty payload) | n/a (Y1 has one player) |
| 0x0b | ADDRESSED_PLAYER_CHANGED | 1.4+ event ID | ✓ T8 (PlayerID=0, UidCtr=0) | n/a (Y1 has one player) |
| 0x0c | UIDS_CHANGED | 1.4+ event ID | ✓ T8 (UidCtr=0) | n/a (Y1 has no UID database) |

## 3. Binary discovery — what's already mapped

`objdump -dRT` against the stock libraries (byte-identical between v3.0.2 and v3.0.7) was the entire discovery pass for what response-builder primitives we have to call. Result: every PDU and every event has both:
  - A function in `libextavrcp.so` (e.g. `<btmtk_avrcp_send_get_playstatus_rsp>: 0x2354`)
  - A PLT stub in `libextavrcp_jni.so` (e.g. `<btmtk_avrcp_send_get_playstatus_rsp@plt>: 0x3564`)

Full PLT inventory (from `libextavrcp_jni.so` md5 `fd2ce74db9389980b55bccf3d8f15660`, what each trampoline would `blx`):````````````````````````````````````````````````````````````````````````````````````````````````

| PDU / event | Response builder | PLT @ | libextavrcp.so body @ |
| --- | --- | --- | --- |
| Currently used by shipped trampolines |  |  |  |
| 0x10 GetCapabilities | get_capabilities_rsp | 0x35dc | 0x1dac |
| 0x17 InformDisplayableCharacterSet | (T_charset rejects via UNKNOW_INDICATION; ACK builder inform_charsetset_rsp at PLT 0x3588 / body 0x2138 is no longer called) | — | — |
| 0x18 InformBatteryStatusOfCT | battery_status_rsp | 0x357c | 0x2160 |
| 0x20 GetElementAttributes | get_element_attributes_rsp | 0x3570 | 0x2188 |
| 0x30 GetPlayStatus | get_playstatus_rsp | 0x3564 | 0x2354 |
| 0x31 event 0x01 | reg_notievent_playback_rsp | 0x339c | 0x23f0 |
| 0x31 event 0x02 | reg_notievent_track_changed_rsp | 0x3384 | 0x2458 |
| 0x31 event 0x03 | reg_notievent_reached_end_rsp | 0x3378 | 0x24c8 |
| 0x31 event 0x04 | reg_notievent_reached_start_rsp | 0x336c | 0x2528 |
| 0x31 event 0x05 | reg_notievent_pos_changed_rsp | 0x3360 | 0x2588 |
| 0x31 event 0x06 | reg_notievent_battery_status_changed_rsp | 0x3354 | 0x25f0 |
| 0x31 event 0x07 | reg_notievent_system_status_changed_rsp | 0x3348 | 0x2658 |
| 0x31 event 0x09 | reg_notievent_now_playing_content_changed_rsp | 0x330c | 0x26c0 |
| 0x31 event 0x0a | reg_notievent_availplayers_changed_rsp | 0x3324 | 0x27b0 |
| 0x31 event 0x0b | reg_notievent_addredplayer_changed_rsp | 0x3330 | 0x2810 |
| 0x31 event 0x0c | reg_notievent_uids_changed_rsp | 0x3318 | 0x2880 |
| (default reject for unknown PDU including 0x40/0x41) | pass_through_rsp | 0x3624 | n/a (in libextavrcp.so too — reached via UNKNOW_INDICATION fall-through) |
| PlayerApplicationSettings (T_papp + T8 event 0x08) |  |  |  |
| 0x11 | list_player_attrs_rsp | 0x35d0 | 0x1e24 |
| 0x12 | list_player_values_rsp | 0x35c4 | 0x1e74 |
| 0x13 | get_curplayer_value_rsp | 0x35b8 | 0x1ed0 |
| 0x14 | set_player_value_rsp | 0x3594 | 0x1f2e |
| 0x15 | get_player_attr_text_rsp | 0x35ac | 0x1f58 |
| 0x16 | get_player_value_text_value_rsp | 0x35a0 | 0x203c |
| 0x31 event 0x08 | reg_notievent_player_appsettings_changed_rsp | 0x345c | 0x2720 |

No new PLT discovery needed. All builders linked at stock and exercised by the trampoline chain. Calling-convention reference: [`ARCHITECTURE.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FARCHITECTURE.md) PApp builder table.

### Code-cave budget

LOAD #1 padding budget: 4020 bytes total (`0xac54..0xbc08`). The patcher computes the assembled trampoline blob size at build time and prints it on every run; release builds currently land in the low 3 kB range, debug builds (`KOENSAYR_DEBUG=1`) ~150 B larger from the spliced `__android_log_print` calls. The patcher asserts on overflow before it can corrupt LOAD #2's `.data` / `.got`.

If we ever do exhaust LOAD #1 padding, the fallback is to extend the same trick to the LOAD #2 padding region by bumping LOAD #2's `p_filesz`/`p_memsz`.

## 4. y1-track-info schema (cumulative)

File-level wrapper:``````

| File offset | Size | Contents |
| --- | --- | --- |
| 0 | 1 B | active_slot — single-byte indicator (0 or 1). Reader's atomic load → dispatch. Writer's atomic store after slot fill flips this. |
| 1..3 | 3 B | RFA padding (4-B align slot[0]). |
| 4..1107 | 1104 B | slot[0] — 1104-byte schema below (in-place when active_slot == 0 on read, fresh write target when active_slot == 1). |
| 1108..2211 | 1104 B | slot[1] — second copy. |
| 2212 | 1 B | RFA padding. |

Total file: 2213 B. Reader (`libextavrcp_jni.so` trampolines via `get_or_init_mmap` + `read_track_info`) memory-maps the file once per process, reads `file[0]` per emit to pick the slot, byte-copies the 1104-byte payload (or any sub-range via `slot_offset`) into the trampoline's stack `file_buf`. Writer (`TrackInfoWriter.flushLocked`) writes the inactive slot via `RandomAccessFile.seek+write`, then atomically flips `file[0]` to point at the just-written slot — readers never observe a torn slot.

Per-slot schema (offsets relative to the active slot's start):````````````````````````````````````````````````````````````

| Offset | Field | Size | Status | Source |
| --- | --- | --- | --- | --- |
| 0..7 | track_id (synthetic) | 8 | shipped | Song.getId() or syntheticAudioId(path) fallback (read live from PlayerService.getCurrentSong() in TrackInfoWriter.flushLocked) |
| 8..263 | Title | 256 | shipped | Song.getName() (read live from PlayerService.getCurrentSong()) |
| 264..519 | Artist | 256 | shipped | Song.getArtist() (read live from PlayerService.getCurrentSong()) |
| 520..775 | Album | 256 | shipped | Song.getAlbum() (read live from PlayerService.getCurrentSong()) |
| 776..779 | duration_ms (BE u32) | 4 | shipped | Song.getDuration() (read live from PlayerService.getCurrentSong()) |
| 780..783 | position_at_state_change_ms (BE u32) | 4 | shipped | TrackInfoWriter.mPositionAtStateChange |
| 784..787 | state_change_time_ms (BE u32) | 4 | shipped | TrackInfoWriter.mStateChangeTime (CLOCK_BOOTTIME ms-since-boot, full ms precision; T6 / T9 live-position extrapolation. tv_nsec/1e6 computed in-trampoline via magic-multiply) |
| 788..791 | reserved | 4 | — | (pad) |
| 792 | playing_flag | 1 | shipped | TrackInfoWriter.mPlayStatus (3-valued AVRCP §5.4.1 Tbl 5.26 enum: 0=STOPPED, 1=PLAYING, 2=PAUSED — set by PlaybackStateBridge.onPlayValue hooking Static.setPlayValue newValue 0/1/3/5) |
| 793 | previous_track_natural_end | 1 | shipped | TrackInfoWriter.mPreviousTrackNaturalEnd (T5 gate for AVRCP §5.4.2 Tbl 5.31 TRACK_REACHED_END CHANGED) |
| 794 | battery_status | 1 | shipped | TrackInfoWriter.mBatteryStatus (T8 INTERIM + T9 CHANGED-on-edge for AVRCP §5.4.2 Tbl 5.34 BATT_STATUS_CHANGED) |
| 795 | repeat_avrcp | 1 | shipped | TrackInfoWriter.mRepeatAvrcp (AVRCP 1.3 Appendix F attribute 0x02 enum; written by PappSetFileObserver on y1-papp-set writes; T8 0x08 INTERIM + T9 papp CHANGED-on-edge read this byte) |
| 796 | shuffle_avrcp | 1 | shipped | TrackInfoWriter.mShuffleAvrcp (AVRCP 1.3 Appendix F attribute 0x03 enum; same write/read pipeline as 795) |
| 797..799 | reserved | 3 | — | available for future PApp attribute additions (Equalizer / Scan if a Y1 release ever surfaces them) |
| 800..815 | TrackNumber (UTF-8 ASCII decimal) | 16 | shipped | MediaStore.Audio.Media.TRACK % 1000 / parsed from METADATA_KEY_CD_TRACK_NUMBER |
| 816..831 | TotalNumberOfTracks (UTF-8 ASCII decimal) | 16 | shipped | count(*) WHERE ALBUM_ID=? / parsed from CD_TRACK_NUMBER "n/total" |
| 832..847 | PlayingTime (UTF-8 ASCII decimal ms) | 16 | shipped | derived from duration_ms |
| 848..1103 | Genre (UTF-8) | 256 | shipped | MediaStore.Audio.Genres / METADATA_KEY_GENRE |

Total slot size: 1104 B. Per-slot schema is append-only; we never relocate existing fields. The file-level wrapper (1 B `active_slot` + 3 B pad + 2 × 1104 B slots + 1 B pad = 2213 B) keeps reader / writer race-free without `tmpfile + rename`.

The numeric AVRCP 1.3 Appendix E attrs (4 / 5 / 7) are stored pre-formatted as ASCII decimal strings rather than binary u16 / u32 with a Thumb-2 itoa, keeping the T4 trampoline a uniform strlen+memcpy loop.

Trampoline edge state lives in `libextavrcp_jni.so``.bss` at `G_Y1_TRAMPOLINE_STATE_VADDR = 0xd2d6` (13 B): bytes 0..7 = last_seen track_id (T5 / T4 edge detect), byte 8 = unused (was last RegNotif transId; per-event TIDs now live in `g_avrcp_req_event_database`), byte 9 = last_play_status (T9), byte 10 = last_battery_status (T9), byte 11 = last_repeat_avrcp (T9 papp), byte 12 = last_shuffle_avrcp (T9 papp). Zero-init at process load (same scope as `g_avrcp_req_event_database`).

## 5. PlayerApplicationSettings — response-builder discovery

Discovery work that will be required before trampolines for PDUs 0x11-0x16 + event 0x08 can be written:``````````````````````````````

| Function | libextavrcp.so @ | Notes |
| --- | --- | --- |
| list_player_attrs_rsp | 0x1e24 | PDU 0x11 — return list of supported attribute IDs |
| list_player_values_rsp | 0x1e74 | PDU 0x12 — return allowed values for one attribute |
| get_curplayer_value_rsp | 0x1ed0 | PDU 0x13 — return current values for the requested attribute IDs |
| set_player_value_rsp | 0x1f2e | PDU 0x14 — accept new value (also requires a write path that mutates Y1's SharedPreferences from a different process) |
| get_player_attr_text_rsp | 0x1f58 | PDU 0x15 — return UTF-8 attribute label text |
| get_player_value_text_value_rsp | 0x203c | PDU 0x16 — return UTF-8 value label text |
| reg_notievent_player_appsettings_changed_rsp | 0x2720 | event 0x08 — proactive CHANGED on shuffle / repeat edges |

Recipe per function: see [`ARCHITECTURE.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FARCHITECTURE.md) §"Adding a new PDU handler". The argument shape must be confirmed via disassembly, not inferred from arg name — the OEM names don't always match semantics (see the worked example on `get_element_attributes_rsp`).

Sub-PDU detail (informative):
  - 0x11 ListPlayerAppSettingAttrs — return 2 attrs: 0x02 (Repeat), 0x03 (Shuffle). 1.3 also defines 0x01 EqualizerStatus and 0x04 ScanStatus, both optional; skip.
  - 0x12 ListPlayerAppSettingValues for attr=0x02 → 4 values (off / single / all / group). For attr=0x03 → 3 values (off / all / group).
  - 0x13 GetCurrentPlayerAppSettingValue — read shuffle_flag / repeat_mode from y1-track-info, return.
  - 0x14 SetPlayerAppSettingValue — controller sending us shuffle / repeat. Forward as a broadcast that the music app receives → setSharedPref → broadcast loops back to us.
  - 0x15/0x16 — text labels for attribute and value names. Static strings ("Repeat", "Off", etc.) shippable in LOAD #1 padding.

Plus: proactive CHANGED on shuffle / repeat changes via event 0x08, fed by the same broadcast receivers.

## 6. Test / verification strategy

Per change: a hardware capture against at least three CTs covering different policy postures. Test-matrix CT roster + per-CT empirical observations live in [`INVESTIGATION.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FINVESTIGATION.md) "Hardware test history per CT". Recommended posture spread:
  - Permissive CT — polls metadata regardless of CHANGED edges; most forgiving baseline.
  - High-subscribe-rate CT — subscribes to TRACK_CHANGED at high frequency (regression check for AVCTP-saturation symptoms).
  - Strict CT — gates metadata refresh on charset acknowledgement and real CHANGED edges.
  - Polling CT — uses GetPlayStatus polling rather than RegisterNotification subscriptions (regression check for T6 / live position).
  - (stretch) An iOS / WearOS CT — different polling pattern again.

For each CT, capture btlog+logcat with:`./tools/dual-capture.sh /work/logs/dual-<ct>-<run>/`

and verify:
  - No new NACKs. msg=520 NOT_IMPLEMENTED count should drop to zero (or stay at zero).
  - Expected msg=N response sizes. Each PDU has a known wire-shape; its outbound IPC frame size should be deterministic.
  - EventsSupported announcement. T1's GetCapabilities response advertises every event the current build can satisfy; CT either subscribes or it doesn't, but it shouldn't subscribe to events we can't satisfy and then NACK.
  - Battery footprint. dmesg-after wake-lock count and `getprop` battery stats should not regress.

The btlog parser (`tools/btlog-parse.py`) gives us full HCI command/event visibility. Any AVCTP-level NACK or rejection will surface there as a `result:` field on the relevant CNF.

## 7. Risk register (when extending)``````````````[``](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FINVESTIGATION.md)``````

| Risk | Likelihood | Mitigation |
| --- | --- | --- |
| New PDU response builder has an arg convention not derivable from disassembly alone | Medium | Bisect via JNI in-tree caller (most builders are called by stock JNI somewhere even if Java stack never reaches them). Failing that, ship a no-op trampoline that returns NOT_IMPLEMENTED and watch CT behavior to confirm the CT was actually probing for that PDU. |
| The 1 s PLAYBACK_POS_CHANGED cadence creates wakeup pressure | Low | T9's position-emit block runs only when file[792]==PLAYING and is driven by a 1 s Handler.postDelayed loop that's cancelled the moment playback pauses or stops. No timer fires while idle. Strict CTs subscribed for a longer interval are over-served (spec-permissible — shall be emitted at this interval defines a max-interval ceiling, not a min cadence floor). |
| LOAD #1 extension exhausts page-padding | Very low | 4020-byte cap is hard-asserted in the patcher; build fails before it can corrupt LOAD #2's GOT. Fallback: extend LOAD #2 padding. |
| Trampoline blob shifts every PLT call beyond range | Low (Thumb b.w covers ±16 MB; trampolines and PLT are <0x10000 apart) | Verify bl.w/b.w reach in _thumb2asm.py self-test for each new emit site. |
| AVRCP version negotiation: F1 patch sets MtkBt-internal version flag but our wire-shape PDU set is 1.3 | Low | F1 only flips the BlueAngel-internal flag to unblock 1.3+ command dispatch through MtkBt's Java layer. SDP record advertises AVRCP 1.3 (V1 patch) / AVCTP 1.2 (V2 patch). Per AVRCP 1.3 §6 (Service Discovery Interoperability Requirements) + ESR07 §2.1 / Erratum 4969, the served version is what CTs key against, and they negotiate a 1.3 dialogue — which is what we implement. |
| Continuation PDU 0x40/0x41 traffic from a CT (would require stateful re-emit) | Low — TG never fragments | T_continuation emits NOT_IMPLEMENTED, which is spec-acceptable. If a CT ever issues 0x40, upgrade to a stateful re-emitter. |
| AVCTP saturation under a CT subscribe storm drops PASSTHROUGH key-release frames; the music app then interprets the held key as a long-press, calls startFastForward()/startRewind(), and the lambda thread runs forever | Medium (high-subscribe-rate CT classes have been observed driving this — see INVESTIGATION.md for per-CT empirical context) | U1: NOP UI_SET_EVBIT(EV_REP) at libextavrcp_jni.so:0x74e8 so the kernel's evdev soft-repeat timer never fires on the AVRCP virtual keyboard. Without auto-repeat, a dropped PASSTHROUGH RELEASE can no longer drive the held-key cascade; the music app sees one event per actual PRESS frame the CT sends. Spec-correct per AVRCP 1.3 §4.6.1 + AV/C Panel Subunit Spec (CT periodic re-send during held button). |

## 8. Out of scope (and why)

Anything outside the AVRCP 1.3 spec proper (V13 + ESR07) is out of scope for this project. See §1 above.

## 9. Lower BT profile stack

AVRCP 1.3 sits on top of AVCTP, which rides L2CAP. A2DP rides AVDTP, signalled by GAVDP. All four lower profiles live in `mtkbt` (BlueAngel internal stack — see [`ARCHITECTURE.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FARCHITECTURE.md) "Lower BT profile stack").

Scope. Spec-completeness where tractable on this hardware — every Optional row we can implement, not just observed-deviation fixes. Per the [`feedback_y1_upstream_spec_compliance`] memory rule, fixes go at the spec-deviation layer, not via AVRCP-level workarounds. Subsections are organised per-issue with the affected profile noted in the heading.

### 9.1 AVRCP META CONTINUING_RESPONSE (PDUs 0x40 / 0x41) — AVRCP / AVCTP — DEFERRED

Spec. AVRCP 1.3 §5.5: when a TG response exceeds CT buffer / AVCTP MTU, TG sends `packet_type=01 START`; CT responds with PDU 0x40 (Continuing) or 0x41 (Abort). ICS Table 7 rows 31-32: Mandatory if GetElementAttributes Response is supported (C.2).

Current state.`T_continuation` rejects 0x40 / 0x41 with AV/C NOT_IMPLEMENTED via the UNKNOW_INDICATION fallback. Counted as ✓ in §2 because the OEM `_send_get_element_attributes_rsp` packs into a 644 B buffer and emits a single non-fragmented frame — TG never sets `packet_type=01`, so a spec-conforming CT never sends 0x40.

Why deferred. A stateful re-emitter is only meaningful after the OEM `_send_get_element_attributes_rsp` is replaced by a manual META builder that fragments at AVRCP layer (i.e., the TG actually sets `packet_type=01`). Until that bypass lands, the re-emitter is dead code. Cheaper INVALID_PARAMETER (status 0x05 per AVRCP 1.3 §5.7.1 Table 5.41) reject hits a binary-shape barrier: `libextavrcp.so` exposes no META REJECTED builder, and changing the existing `cmd_frame_ind_rsp` arg shape carries regression risk for every unhandled-PDU path with no observable wire-shape benefit (CT can't tell the two reject codes apart).

Plan when revisited. Replace T4's `_send_get_element_attributes_rsp` call with a manual META builder that paginates at AVRCP layer (set `packet_type=01` on first fragment, cache the rest in a per-conn state struct in the trampoline blob region). Upgrade T_continuation: on 0x40 emit next chunk with `packet_type=02/03`; on 0x41 drop state. ~3 days; needs `AVRCP_SendMessage` (libextavrcp.so:0x18ec) IPC shape disassembly.

### 9.2 AVRCP playback state ↔ AVDTP source state coupling — A2DP / AVDTP — SHIPPED

Spec. AVDTP 1.3 §8.14 / §8.15: when AVRCP TG signals PAUSED, the A2DP source should keep the stream paused (NOT torn down); resume without renegotiation on PLAYING. SUSPEND is reserved for explicit policy changes (phone call routing, etc.), not for normal pause / silence handling.

Stock deviation. AudioFlinger's silence-timeout (~3 s after the music app stops writing samples) hits `libaudio.a2dp.default.so::A2dpAudioStreamOut::standby_l`, which calls `a2dp_stop` unconditionally → AVDTP SUSPEND on the wire. Peer CTs that aggressively close + reopen their A2DP sink on SUSPEND cycle once per pause-of-≥3 s, producing burst-on-resume audio and playhead drift.

Current state.`patch_libaudio_a2dp.py` patches `standby_l` at file offset `0x000086ab` (1 byte: ARM cond `0x0a` EQ → `0xea` AL). The `beq` that conditionally branched past `a2dp_stop` is now an unconditional `b`, making the call site unreachable. AudioFlinger's silence-timeout still completes the standby (releases the wake lock, sets `mStandby = 1`), but the AVDTP stream stays alive; the next `write()` after PLAYING resumes pushes samples into the same session.

Verification. Capture btlog around a pause: zero `[A2DP] a2dp_stop. is_streaming:1` lines, peer A2DP sink doesn't cycle, audio resumes clean.

Sibling-path note (close_l → a2dp_cleanup).`libaudio.a2dp.default.so` has one other teardown PLT call: `bl sym.imp.a2dp_cleanup` at file `0x8a00` inside `A2dpAudioStreamOut::close_l` (`0x89cc`). `close_l` is reached from `close()` (`0x8a4c`) and `setBluetoothEnabled(false)` (`0x8b58`). AH1 doesn't cover this path because AudioFlinger doesn't call `close()` during normal pause cycles, only on policy / focus / device-routing transitions. If a future capture surfaces `close_l` firing during a pause, the corresponding fix is a sibling byte-flip at file `0x89e0` (`beq 0x8a0c` EQ → AL, mirroring AH1's shape).

### 9.3 Per-attribute 511-byte hard cap in `…send_get_element_attributes_rsp` — AVRCP — SHIPPED

Spec. AVRCP 1.3 §5.3.1 Table 5.24 places no per-attribute byte cap. TG fragments via §5.5 if the total response exceeds AVCTP MTU.

OEM TG deviation.`libextavrcp.so:0x2188` (`btmtk_avrcp_send_get_element_attributes_rsp`) enforces a 511-byte per-attribute hard cap; on overflow it emits `[BT][AVRCP][ERR] too large attr_index:%d` and drops the attribute silently.

Current state. The music app's `TrackInfoWriter.putUtf8Padded` caps each string attribute at 240 bytes before it lands in `y1-track-info`. The cap is well below the OEM 511 hard cap so even after multi-byte UTF-8 expansion at the CT side the attribute survives. Truncation is codepoint-safe — if the chosen byte position would split a multi-byte codepoint, the helper walks back to the codepoint boundary so a strict CT never sees a malformed UTF-8 sequence (AVRCP 1.3 §5.3.1 Table 5.24 CharacterSet=0x6A). Numeric attributes (TrackNumber 4, TotalNumber 5, PlayingTime 7) are bounded to a 15-byte ASCII slot and unaffected.

Optional follow-up. Bypass `…send_get_element_attributes_rsp` entirely and build the GetElementAttributes response wire frame directly in the trampoline, using the full §5.5 fragmentation flow from §9.1 above. Removes the 511 cap as a constraint. ~3 days if paired with §9.1 (no value as a standalone change — 240 B already fits everything we'd realistically ship).

### 9.4 AVCTP MTU negotiation discoverability — AVCTP — NO ACTION

Spec. AVCTP 1.2 §5: each side independently advertises its MTU during L2CAP CONFIG; the smaller value wins. AVRCP 1.3 §6 specifies the AVCTP version pairing only.

Current state. mtkbt advertises `AVRCP_MAX_PACKET_LEN:512` regardless of peer capability. Captured logs show `(10+u2MtuPayload) <= 512` enforcement. Most peers agree to 512; some negotiate higher in L2CAP CONFIG but we cap at 512.

Compliance plan. Not a deviation worth fixing — 512 is the standard L2CAP signaling MTU. Filed here for completeness; revisit if a CT ever requests >512 and degrades on the cap.

### 9.5 GAVDP / AVDTP codec advertisement — GAVDP / AVDTP / A2DP — RESOLVED (closed by §9.11)

Spec. AVDTP 1.3 §8.6 (DISCOVER): TG should respond with all locally-supported SEPs. A2DP 1.3 §4.2 Table 4.1: SBC Mandatory; AAC / MP3 / ATRAC Optional.

Resolution. SBC-only is fully spec-compliant for an A2DP 1.3 Source — every non-SBC codec is Optional. No spec obligation to add codec coverage. See §9.11 for the A2DP 1.3 audit.

### 9.6 AVCTP subscribe-storm mitigation (U1) — AVCTP — SHIPPED

`U1` (`libextavrcp_jni.so:0x74e8` NOPs `UI_SET_EVBIT(EV_REP)`) defangs kernel-side auto-repeat on the AVRCP virtual keyboard, preventing held-key cascades when a subscribe-storming CT drops PASSTHROUGH RELEASEs. Risk-register context in §7. Patch H″ (in `com.innioasis.y1.apk`) handles the framework-side equivalent (`InputDispatcher::synthesizeKeyRepeatLocked` repeats).

### 9.7 SDP AVCTP version correction (V2) — AVCTP — SHIPPED

`V2` (`mtkbt 0x0eba6d`: SDP AVCTP version `0x00 → 0x02`) corrects the served record from advertising AVCTP 1.0 to AVCTP 1.2, the version paired with AVRCP 1.3 per AVRCP 1.3 §6 + ESR07 §2.1 / Erratum 4969. Byte detail in [`PATCHES.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FPATCHES.md).

### 9.8 AVDTP DELAY_REPORT (sig_id 0x0d) — AVDTP — RESOLVED (closed by §9.12)

Spec. AVDTP 1.3 §8.19 Delay Reporting. AVDTP 1.3 ICS Table 14 row 6 = Optional for the Source role.

Resolution. Optional at AVDTP 1.3 — mtkbt's lack of a 0x0d handler is spec-permissible as long as we don't advertise the Delay Reporting service capability in our SEP capabilities response (we don't). Inbound 0x0d hits the General Reject path (Mandatory per §8.18, present in mtkbt). See §9.12 for the AVDTP 1.3 audit.

### 9.9 Remaining workstream order

§9.2 / §9.3 / §9.5 / §9.6 / §9.7 / §9.8 shipped or resolved-no-action. Active queue:
  - §9.1 stateful T_continuation: needs either (a) the OEM `_send_get_element_attributes_rsp` replaced by a manual AVRCP META builder (so TG ever sets `packet_type=01`), or (b) `cmd_frame_ind_rsp` arg-shape disassembly to upgrade NOT_IMPLEMENTED to INVALID_PARAMETER.
  - Hardware verification of the bidirectional PApp loop on a peer CT. Round trip: Y1-UI Repeat/Shuffle toggle → SharedPreferences write → `PappStateBroadcaster.onSharedPreferenceChanged` → `TrackInfoWriter.setPapp` writes `y1-track-info[795..796]` + `playstatechanged` wake → MtkBt `notificationPlayStatusChangedNative` → T9 papp block → `reg_notievent_player_appsettings_changed_rsp` REASON_CHANGED on the wire. logcat checkpoints: `Y1Application` registers `PappStateBroadcaster`; CT subscribers of event 0x08 see CHANGED frames following the Y1-UI edge.
  - §9.10-§9.14 ICS-scoreboard pass: complete. AVCTP and the audio-triad audits done. GAVDP Acceptor Table 5 row 9 (GET_ALL_CAPABILITIES) closed by V5 — a 2-byte TBH jump-table alias routing sig 0x0c through the sig 0x02 handler.

### 9.10 AVCTP 1.2 ICS audit — AVCTP — VERIFIED

Anchored against `docs/spec/AVCTP 1.2/AVCTP.ICS.p10.pdf` Table 3 (Target Features). Per Table 0, AVCTP 1.0 / 1.2 / 1.3 are all deprecated 2022-02-01 + withdrawn 2023-02-01; only AVCTP 1.4 is in current SIG qualification scope. We target 1.2 because that's the version paired with AVRCP 1.3 per AVRCP 1.3 §6 + ESR07 §2.1 / Erratum 4969 — same shipping-window argument as AVRCP 1.3 (deprecated 2023-02-01 / withdrawn 2027-02-01).````

| ICS Table 3 row | Capability | Status | Y1 |
| --- | --- | --- | --- |
| 1 | Message fragmentation | O | ✓ — mtkbt outbound path implements pkt_type 0/1/2/3 (SINGLE/START/CONTINUE/END) per ARCHITECTURE.md §"AVCTP packet types" |
| 2 | Transaction label management | M | ✓ — transId routed from conn[17] into every response builder; stamping into byte 5 of IPC frame is the response-builder's responsibility (cross-ref ARCHITECTURE.md cross-profile coupling table item 4) |
| 3 | Packet type field management | M | ✓ — pkt_type written by the AVCTP-layer fragmentation logic (SINGLE for the GetElementAttributes 644 B body; fragmentation untriggered at our advertised attribute sizes) |
| 4 | Message type field management | M | ✓ — RESPONSE / COMMAND distinction set per AV/C body type; mtkbt's response builders write the correct type bit |
| 5 | PID field management | M | ✓ — AVRCP TG PID=0x110E served correctly per the AVRCP record's ProfileDescList; AVCTP layer uses this PID for routing |
| 6 | IPID field management | M | ✓ — Invalid Profile Identifier handling delegated to mtkbt's AVCTP layer |
| 7 | Message information management | M | ✓ — AV/C body parsing + response synthesis lives in the trampoline chain (see ARCHITECTURE.md §"Trampoline chain") |
| 8-13 | Event registration / connect / disconnect / send variants | O | mtkbt provides the connect / disconnect / send paths used by the JNI bridge; event-registration optional and not separately exposed |
| 14 | Multiple AVCTP channel establishment | O — Controller-only row | n/a (TG row table doesn't include this) |

All Mandatory rows covered. Optional row 1 (fragmentation) shipped for completeness; remaining Optional rows (8-13) are CT/TG event-registration APIs not exercised by our stack.

Static AVCTP version-byte multiplicity. Three AVCTP version sites in mtkbt's static SDP-record region; V2 patches the only one consulted at runtime. Per the SDP attribute table at vaddr `0xfa700`, only one served AVRCP TG record references AVCTP — the served-record entries (file offset `0xf97c0..0xf9808`) include attr 0x0004 ProtocolDescriptorList (containing the V2-patched site at `0xeba6d`) but not attr 0x000d AdditionalProtocolDescriptorList. The unpatched sites `0xeba25` and `0xeba37` are dead bytes in unselected template records.

### 9.11 A2DP 1.3 ICS audit — A2DP — SHIPPED (PARTIAL — see §9.5 / §9.8)

Anchored against `docs/spec/A2DP 1.3/A2DP_SPEC_V13.pdf`. There is no separate A2DP ICS proforma in the SIG release; conformance requirements live in the spec body itself.

Application Layer (§3 Table 3.1):

| Item | Feature | SRC | SNK | Y1 |
| --- | --- | --- | --- | --- |
| 1 | Audio Streaming | M | M | ✓ Y1 implements SRC role; SBC stream over AVDTP |

Audio Codec Interoperability (§4.2 Table 4.1):``````````

| Codec | Status | Y1 |
| --- | --- | --- |
| SBC | M | ✓ encoder present (libmtkbtextadpa2dp.so exports sbc_pack_frame, sbc_proto_4_40_fx, sbc_proto_8_80_fx, sbc_calculate_bits, etc.) |
| MPEG-1,2 Audio | O | not advertised, not present |
| MPEG-2,4 AAC | O | not advertised, not present |
| ATRAC family | O | not advertised, not present |

GAVDP layer rejects non-SBC SEPs at `GavdpAvdtpEventCallback` per ARCHITECTURE.md §"Codec scope". Spec-permissible (§4.2.4 codec interop is conditional on Optional codec support, none claimed).

SDP Source Service Record (§5.3 Figure 5.1):``````````````````

| Attribute | Spec status | Spec value (1.3) | Y1 served value | Gap |
| --- | --- | --- | --- | --- |
| Service Class ID List → Audio Source (UUID 0x110A) | M | UUID | ✓ (sdptool confirms handle 0x10002 advertises Audio Source) | — |
| ProtocolDescriptorList → L2CAP / AVDTP, AVDTP version | M | 0x0103 | 0x0100 (AVDTP 1.0) | 1 byte at file 0xeba09 |
| BluetoothProfileDescriptorList → AdvancedAudioDistribution (UUID 0x110D), version | M | 0x0103 | 0x0100 (A2DP 1.0) | 1 byte at file 0xeb9f2 |
| SupportedFeatures (Source bitmap: bit 0 Player / 1 Microphone / 2 Tuner / 3 Mixer) | O | bit 0 = 1 (Player) | not advertised (stock A2DP record omits attr 0x0311) | none required (Optional) |
| Provider Name / Service Name | O | text | "Advanced Audio" served as Service Name (sdptool confirms) | — |

Gaps to A2DP 1.3 conformance:
  - Advertised AVDTP version in A2DP record's ProtoDescList is `0x0100` instead of spec-mandated `0x0103` — file offset `0xeba09`, single-byte patch.
  - Advertised A2DP version in BluetoothProfileDescriptorList is `0x0100` instead of spec-mandated `0x0103` — file offset `0xeb9f2`, single-byte patch.
  - Both must move together — asymmetric advertisement is invalid. The bumps imply AVDTP 1.3 feature support (DELAY_REPORT per A2DP 1.3 §1.4.1.2; GET_ALL_CAPABILITIES per GAVDP 1.3 Table 5 row 9 once A2DP 1.3 §1.2 inherits it).

A2DP §3.1: peers consult advertised AVDTP version before GAVDP_ConnectionEstablishment. Per §9.12 AVDTP-1.3 features are Optional at the AVDTP layer; per §9.13 GAVDP 1.3 raises GET_ALL_CAPABILITIES to Mandatory at the Acceptor layer.

Shipped: V3 + V4 + V5. V3/V4 bump A2DP/AVDTP advertisement to 1.3. V5 is a 2-byte TBH jump-table alias routing sig 0x0c through the sig 0x02 GET_CAPABILITIES handler — per AVDTP 1.3 §8.8, the sig 0x02 response is a wire-compatible subset of the sig 0x0c response, sufficient for an SBC-only Source.

### 9.12 AVDTP 1.3 ICS audit — AVDTP — VERIFIED, GAP = ADVERTISED VERSION

Anchored against `docs/spec/AVDTP 1.3/AVDTP.ICS.p14.pdf`. Per Table 14a (Versions, Source), AVDTP 1.0 / 1.2 are deprecated/withdrawn; AVDTP 1.3 is the only currently-Mandatory version. Same shipping-window argument as AVRCP / AVCTP.

Source role capabilities (Table 14):``

| Item | Capability | Status | Y1 |
| --- | --- | --- | --- |
| 1 | Basic transport service support | M | ✓ — A2DP audio streams over AVDTP through libmtka2dp.so ↔ mtkbt internal A2DP source state machine ↔ AVDTP MEDIA on the wire |
| 2 | Reporting service support | O | not advertised in SEP capabilities, no handler |
| 3 | Recovery service support | O | not advertised, no handler |
| 4 | Multiplexing service support | O | not advertised, no handler |
| 5 | Robust header compression service support | O | not advertised, no handler |
| 6 | Delay Reporting | O | not advertised in SEP capabilities; sig_id 0x0d DELAYREPORT reaches General Reject (§8.18 fallback) — see "Handler verification" below |

Acceptor capabilities (Source role) — Table 8 Signaling Message Format:

| Item | Capability | Status | Y1 |
| --- | --- | --- | --- |
| 1 | Transaction Label | M | ✓ |
| 2 | Packet type | M | ✓ |
| 3 | Message type | M | ✓ |
| 4 | Signal identifier | M | ✓ |

Tables 9-12 (Stream Discovery, Establishment, Suspension, Release, Security) — every row Optional. We implement Stream Discover (DISCOVER), Stream Get Capabilities (GET_CAPABILITIES), Set Configuration, Get Configuration, Open Stream, Start Stream, Suspend, Close, Abort responses (per ARCHITECTURE.md §"AVDTP signal codes" — sig 0x01..0x0b documented in mtkbt strings).

Table 13 (Message Fragmentation) item 1 = M: ✓ (mtkbt's AVDTP layer implements fragmentation, same code path as AVCTP layer per §8.3).

Table 16 (Message Error Handling): Reporting Capability Error (M) ✓ via `[AVDTP_EVENT_GET_CAP_CNF]try another SEP` in `GavdpAvdtpEventCallback`; General Reject Response Includes Signal ID (M) ✓ via §8.18 fallback path.

Handler verification for AVDTP 1.3 additions (sig_id 0x0c GET_ALL_CAPABILITIES + 0x0d DELAYREPORT):

The AVDTP signal dispatcher at file `0xaa72c` (full disassembly in `INVESTIGATION.md`) has a TBH jump table at `0xaa81e` with explicit entries for both sig 0x0c (target `0xab4de`) and sig 0x0d (target `0xab540`). Sig 0x0d DELAYREPORT has substantive handler logic. Sig 0x0c GET_ALL_CAPABILITIES is a stub at `0xab4de` that always falls through to the BAD_LENGTH error path — peer receives an error response, not a General Reject.

V5 patches the jump-table entry for sig 0x0c to redirect to the sig 0x02 GET_CAPABILITIES handler at `0xaa924`. This is a structural workaround, not a real handler — but per AVDTP 1.3 §8.8 the sig 0x02 response is a wire-compatible subset of the sig 0x0c response, which suffices for an SBC-only Source.

Compliance verdict.````

| Aspect | Status |
| --- | --- |
| All Mandatory rows of Tables 8 / 13 / 16 (Source-role Acceptor) covered | ✓ |
| All advertised SEP capabilities backed by working handlers (SBC + Basic transport service) | ✓ |
| AVDTP 1.3 Optional features (Delay Reporting, Reporting / Recovery / Multiplexing services) | not advertised, not implemented — spec-permissible |
| Advertised AVDTP version in SDP record | 0x0100 (AVDTP 1.0) — gap; spec target 0x0103 |

Gap: the static AVDTP version byte at file offset `0xeba09` is `0x00` instead of `0x03`. Standalone fix would be a single-byte patch (V4-style: 0x00 → 0x03). However, the bump implies A2DP 1.3 conformance (peers consult our AVDTP version per A2DP §3.1), which transitively implies GAVDP 1.3 conformance (per A2DP 1.3 §1.2 profile dependency), which has a strict-conformance gap on sig 0x0c GET_ALL_CAPABILITIES — see §9.13 for the full picture. Bump decision deferred to §9.11 user-approval point.

This partially resolves the §9.5 / §9.8 open investigations — the codec-advertisement question is closed (SBC-only at A2DP 1.3 is spec-permissible since AAC/MP3/ATRAC are Optional). The DELAY_REPORT question is closed at the AVDTP-1.3-Optional-feature level (we don't advertise it in our SEP capabilities, so the missing handler is not a deviation). The GET_ALL_CAPABILITIES question survives and feeds the §9.13 GAVDP-layer Mandatory-row analysis.

### 9.13 GAVDP 1.3 ICS audit — GAVDP — VERIFIED, GAP = SIG 0x0C HANDLER

Anchored against `docs/spec/GAVDP 1.3/GAVDP.ICS.p12.pdf`. Per Tables 2a / 3a, GAVDP 1.0 / 1.2 are deprecated/withdrawn; GAVDP 1.3 is the only currently-Mandatory version. GAVDP isn't separately advertised in any SDP record (UUID 0x1203 hits in mtkbt's static SDP region are part of the HFP / HSP records, not GAVDP); A2DP 1.3 §1.2 makes A2DP-1.3 conformance imply GAVDP-1.3 conformance.

Acceptor capabilities (Table 3 — our role since peers initiate):``````````````````

| Item | Feature | Status | Y1 |
| --- | --- | --- | --- |
| 1 | Connection Establishment | M | ✓ — peer-initiated AVDTP connection accepted |
| 2 | Transfer Control – Suspend | O | response handled per btmtk_a2dp_send_stream_pause_req (_handle_stream_suspend_ind/_cnf) |
| 3 | Transfer Control – Change Parameters | O | RECONFIGURE response present in mtkbt sig table |
| 4 | Start Streaming | M | ✓ — _handle_stream_start_ind/_cnf |
| 5 | Connection Release | M | ✓ — _handle_stream_close_ind/_cnf |
| 6 | Signaling Control – Abort | M | ✓ — _handle_stream_abort_ind/_cnf |
| 7 | Security Control | O | not implemented; peers don't issue Content Security Control commands in our test matrix |
| 8 | Delay Reporting | O | not implemented (matches §9.12) |

Acceptor AVDTP procedures (Table 5):

| Item | Feature | Status | Y1 |
| --- | --- | --- | --- |
| 1 | Stream discover response | M | ✓ — DISCOVER (sig 0x01) |
| 2 | Stream get capabilities response | M | ✓ — GET_CAPABILITIES (sig 0x02) |
| 3 | Set configuration response | M | ✓ — SET_CONFIGURATION (sig 0x03) |
| 4 | Open stream response | M | ✓ — OPEN (sig 0x06) |
| 5 | Start stream response | M | ✓ — START (sig 0x07) |
| 6 | Close stream response | M | ✓ — CLOSE (sig 0x08) |
| 7 | General reject message | M | ✓ — §8.18 fallback path |
| 8 | Abort stream response | M | ✓ — ABORT (sig 0x0a) |
| 9 | Stream get all capabilities response | M | ✗ — sig 0x0c hits General Reject; no real handler |

Item 9 is the gap. AVDTP 1.3 ICS Table 10 row 6 says it's Optional at the AVDTP layer; GAVDP 1.3 ICS Table 5 row 9 raises it to Mandatory at the GAVDP-Acceptor layer with Inter-Layer Dependency `AVDTP 10/6 OR AVDTP 10b/6` (Source row OR Sink row).

Interop reality vs ICS-strict reading. Stock without V5: a peer that issues sig 0x0c receives an AVDTP General Reject per §8.18 (Mandatory, present). Well-behaved peers fall back to plain sig 0x02 GET_CAPABILITIES, which we honor. The ICS gap is paper-only at the conformance level, not a functional interop break.

Verdict. GAVDP 1.3 conformance is strict-conformant on every Mandatory row except Acceptor Table 5 row 9 (sig 0x0c GET_ALL_CAPABILITIES response). The gap survives whether or not we bump §9.11 / §9.12 advertised versions — the only difference is whether we claim GAVDP 1.3 (by virtue of A2DP 1.3 dependency, which inherits AVDTP 1.3 dependency). At current 1.0 advertisement, we don't claim GAVDP 1.3 conformance; the gap exists but isn't load-bearing.

Implementation cost for a real 0x0c handler: disassembly of mtkbt's existing GET_CAPABILITIES (sig 0x02) response builder + extension to emit the Get All Capabilities response shape (GET_CAPABILITIES response + Reporting Service / Recovery Service / Multiplexing Service / Robust Header Compression / Delay Reporting service capabilities, all advertised as "not supported"). Not currently in scope.

### 9.14 Lower-BT-stack gap analysis — synthesis

Combining §9.10 (AVCTP) + §9.11 (A2DP) + §9.12 (AVDTP) + §9.13 (GAVDP):

| Profile | Stock advertises | Spec target | M-row gaps | Patch needed | Status |
| --- | --- | --- | --- | --- | --- |
| AVRCP | 1.0 | 1.3 | none | V1 (0xeba58 0x00→0x03) | ✓ shipped |
| AVCTP | 1.0 (signaling) | 1.2 (paired with AVRCP 1.3) | none | V2 (0xeba6d 0x00→0x02) | ✓ shipped |
| A2DP | 1.0 | 1.3 (era-correct) | inherits GAVDP gap on sig 0x0c (closed by V5) | V3 (0xeb9f2 0x00→0x03) | ✓ shipped |
| AVDTP | 1.0 | 1.3 (paired with A2DP 1.3) | none at AVDTP layer; sig 0x0c is Optional here | V4 (0xeba09 0x00→0x03) | ✓ shipped |
| GAVDP | not separately advertised; piggybacks AVDTP version | 1.3 (transitive) | Table 5 row 9 (sig 0x0c GET_ALL_CAPABILITIES response, Mandatory at GAVDP-Acceptor) | V5 (TBH jump-table alias at 0xaa834) | ✓ shipped |

Status: Option C shipped — V3 + V4 + V5 landed together. V3 + V4 bump A2DP/AVDTP advertisement to 1.3; V5 is the structural workaround for sig 0x0c — it aliases the dispatcher's TBH jump-table entry from the BAD_LENGTH stub at `0xab4de` to the existing GET_CAPABILITIES handler at `0xaa924`. Per AVDTP 1.3 §8.8 the sig 0x02 response is a wire-compatible subset of the sig 0x0c response (no extended Service Capabilities), which is exactly what our SBC-only Source advertises anyway.

V5 is wire-correct by decoupling. The AVDTP wire-frame TX site is `fcn.000ae418` (calls `L2CAP_SendData` at file offset `0xae58e`). Byte 1 of the response frame (sig_id) is read at `0xae480` from `txn->[0xe]`, where `txn = *(channel + 0x10)` is the per-channel transaction state populated by the request parser at signal-RX time. The dispatcher (TBH at `0xaa81e`) and per-signal handlers (e.g. `0xaa924`) do not write `txn->[0xe]`. When a peer issues sig 0x0c the parser stores 0x0c in `txn->[0xe]`, V5 routes dispatch through the GET_CAPABILITIES handler, the handler updates state, and `fcn.000ae418` reads `txn->[0xe]=0x0c` and emits a response with `sig_id=0x0c`. Full walk-through in `INVESTIGATION.md`.

`patch_mtkbt.py``OUTPUT_MD5` reflects V1+V2+V3+V4+V5+S1+P1.

## 10. See also
  - [`ARCHITECTURE.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FARCHITECTURE.md) — proxy architecture and existing trampoline chain.
  - [`PATCHES.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FPATCHES.md) — per-patch byte detail.
  - [`INVESTIGATION.md`](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fryan-specter%2Fkoensayr-auto%2Fblob%2FHEAD%2Fdocs%2FINVESTIGATION.md) — historical investigation including binary discovery passes and the empirical history that produced each shipped behavior.
  - `src/patches/_trampolines.py` — current trampoline blob assembler.
  - `src/patches/_thumb2asm.py` — Thumb-2 mini-assembler.

These are Koensayr's own instructions, shown here word for word.

Published by the [ryan-specter/koensayr-auto](https://innioasis.app/firmware.html?model=Y1&software=koensayr-y1) project [[1]](https://innioasis.app/firmware_info.html?repo=ryan-specter%2Fkoensayr-auto&software=koensayr-y1)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aryan-specter)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
