---
title: "Connectivity audit - Innioasis Updater"
description: "Connectivity audit <!-- knowledge-base-scope: historical-audit/review -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-audit-current-system-06_connectivity_audit.html"
---

# Connectivity audit - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Connectivity audit

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Connectivity audit > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

## Shared hardware authority

IMPLEMENTED / HIGH; limited physical functions VERIFIED. The native stack has one CONSYS kernel owner for shared rails, reset, SPM domains, BTIF/DMA, STP/WMT commands, firmware and calibration. Wi-Fi is exposed through cfg80211; Bluetooth through HCI/BlueZ. Reborn is not running a second vendor hardware-control stack.

Evidence: [CONSYS core](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/connectivity/core.c), [firmware](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/platform/connectivity/firmware.c), [Wi-Fi integration](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2), [factory provider](https://github.com/SchulzCode/Y2Linux/blob/main/tools/connectivity/factory.c), [calibration helper](https://github.com/SchulzCode/Y2Linux/blob/main/tools/connectivity/calibration.c). Firmware size/SHA checks precede controller use. The factory handoff accepts an exact bounded record size through a root-only interface; source calibration is read rather than silently replaced with a generic MAC/calibration block. Sensitive runtime files are private and private memory/core-dump handling is deliberate. Keep these safeguards.

Shared recovery has serialization, error counters, bounded automatic attempts and explicit manual recovery conditions. The empty legacy Wi-Fi `glResetInit/glResetUninit` functions are compatibility stubs because recovery moved to the parent; they do not mean recovery is entirely absent. The vendor-derived Wi-Fi core remains a maintenance burden, and its whole command/DMA/concurrency surface was not formally verified by this review. UNKNOWN: recovery correctness under simultaneous real audio and network traffic, RF interference and controller loss.

## Wi-Fi path: F18`Reborn Wifi command worker -> rfkill + /data/network/enabled -> wpa_supplicant Unix control socket + separate attached event socket -> nl80211/cfg80211 -> native MT6582 fullmac port -> CONSYS firmware supplicant connection event -> wpa_cli event helper -> udhcpc -> address/routes/resolver configuration`

The [Reborn adapter](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-platform/src/wifi.rs) has bounded scan startup/completion deadlines, bounded/deduplicated results, separate scan-event monitoring, explicit Off/Starting/scanning state, saved-network operations and input escaping. Its fake-supplicant tests exercise asynchronous progression and malformed/error responses, not merely a success return. The [platform service](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/board/y2/production-overlay/usr/libexec/y2/connectivity) attaches interfaces and supervises supplicant/calibration/BlueALSA. [wpa-event](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/board/y2/production-overlay/usr/libexec/y2/wpa-event) drives DHCP. These are useful pieces to keep.

What is incomplete:
  - `connect()` is WPA-PSK password based: SSID 1–32 bytes and password 8–63 bytes, `key_mgmt WPA-PSK`. Open-network connection is not implemented by this function even if scans display an open network. WPA3/enterprise/captive portals are not promised requirements; explicitly define the supported subset.
  - ADD/SET/SELECT/SAVE succeeds before association/DHCP/DNS succeeds. There is no comparable end-to-end connection deadline and rollback policy to the robust scan state machine. Wrong password, lost AP and DHCP failure need distinct states.
  - Supplicant `COMPLETED` is a link/authentication state, not proof of DNS or useful IP traffic. UI “connected” must not be used as the acceptance criterion. A saved-network diagnostic that checks IP still does not prove DNS/data transfer.
  - App and platform both participate in radio preference/recovery policy. Direct rfkill is an appropriate Linux interface, but retries, requested state and actual recovery need a single documented contract rather than layered optimistic statuses.
  - cfg80211 regulatory/channel/power constraints are propagated into the fullmac protocol. This is better than transplanting another product's country table; it is not RF/regulatory certification.

### What is physically proven

[CONNECTIVITY-10](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fhardware-evidence%2F2026-09-17-m5-connectivity10%2FREADME.md) records wlan0 registration, scans returning 23 then 12 BSS entries, clean off/on cycles and simultaneous Bluetooth adapter power with core functions 0x9, zero observed transport errors. It explicitly says there were no saved network blocks and that association/authentication/DHCP/DNS/transfer were untested.

A later [Reborn inspection](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Fvalidation%2F2026-09-18-radio-inspection.md) records 28 Wi-Fi scan results through the deployed older Reborn build, and identified real status/UI defects subsequently addressed in source. This is stronger than a standalone `iw` scan, but still not a network connection test. The current scan-UI correction report leaves manual viewing/peer tests pending.

Conclusion: PARTIAL / HIGH. Scan/adapter bring-up is physically evidenced; complete Wi-Fi operation is UNKNOWN. Required physical qualification: WPA2 join with correct/incorrect credentials, DHCP timeout, DNS lookup and bidirectional transfer, saved reconnect after reboot/AP loss, radio off/on, suspend/resume if offered, and sustained coexistence with SBC playback. No credentials need to enter public logs to prove those outcomes.

## Bluetooth, pairing and reconnect: F19`Reborn BlueZ worker + pairing agent -> system D-Bus -> bluetoothd -> HCI -> shared CONSYS/STP/WMT transport processed PCM -> BlueALSA ALSA PCM -> bluealsa A2DP-source encoder -> BlueZ transport -> HCI controller -> remote audio sink`

[bluetooth.rs](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-platform/src/bluetooth.rs) uses ObjectManager, a DisplayYesNo agent, explicit confirmation, bounded discovery and asynchronous device operations. It rejects unsupported legacy PIN requests instead of inventing a PIN. Playback rate selects the exact device, transport direction and negotiated 44.1/48-kHz PCM; tests reject unavailable/wrong-peer/unsupported-rate objects. Bond files persist through the platform's private BlueZ storage.

The [reconnect helper](https://github.com/SchulzCode/Y2Linux/blob/main/tools/connectivity/reconnect.c) has a sensible single preferred audio-device policy and bounded retries. BlueZ's built-in reconnect policy is disabled to avoid two autonomous retry owners. However, the helper requires a paired Trusted sink. Reborn issues Pair/Connect/Disconnect/Remove operations but contains no `Trusted` property assignment/control. Pairing alone does not establish that helper precondition. A manually trusted device may work; the end-to-end UI onboarding/reconnect path is PARTIAL, not demonstrated. Confirm with a fresh bond rather than reusing an owner-configured headset.

Reborn has no `MediaPlayer1`/`RegisterPlayer` implementation or corresponding AVRCP action/metadata service. BlueZ having AVRCP code does not connect remote play/pause/next commands to AppModel. This application integration is MISSING / HIGH. It need not block a wired-only alpha, but cannot be advertised as working headset control.

Operations are tracked with timeouts and errors, but whole-bus/service restarts, peer disconnection during writes and output fallback are not qualified. Output switching uses the same playback rebuild/lifecycle mechanisms reviewed in F02, not a seamless handover. The app reads the BlueALSA PCM rate/channels/direction; its baseline S16 choice is appropriate to the current narrow SBC path, not a future proof of arbitrary codec/PCM negotiation.

## Actually built Bluetooth codecs

Inspected source: Buildroot BlueALSA 4.3.1 generated `config.h` and build sources in `out/y2linux-reborn-audio-final/buildroot/build/bluez-alsa-4.3.1`; BlueZ 5.79. The service launches `bluealsa -p a2dp-source`. SBC is built as the mandatory codec. Optional enable macros for AAC, aptX, aptX HD, LDAC, MPEG/MP3 and mSBC are undefined. The later [focused codec audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Farchitecture%2Fbluetooth-codecs.md) confirms the v4.3.1 executable name, advertised controller EDR features, codec/library distinctions and the proposed Auto policy; upstream v5 uses `bluealsad`.

| Codec | Enabled in inspected image build? | Reborn/Y2 peer qualification |
| --- | --- | --- |
| SBC | Yes | UNKNOWN: no retained actual A2DP listening/transport run identified |
| AAC | No | Not qualified; FFmpeg AAC file decoding is unrelated |
| aptX | No | Not qualified |
| aptX HD | No | Not qualified |
| LDAC | No | Not qualified |

Do not describe these optional codecs as “supported today” merely because upstream BlueALSA supports them. Adding them is new codec/CPU/distribution scope, not a bug fix authorized by this audit.

## Actual Bluetooth evidence and target

Historical adapter power/discovery and service availability exist. The Reborn physical scan report found zero discoverable peers, not a successful pairing or audio connection. The native HCI path is therefore more than a stub, but pairing, bonding, preferred reconnect, A2DP transport, audible playback, remote controls and sustained radio coexistence remain distinct unclosed evidence items.

CURRENT: native adapters, orchestration, UI commands and shared PCM-to-BlueALSA path. TARGET: reliable narrowly specified WPA2/SBC operation with truthful link/IP/audio states, one reconnect policy, and tested recovery. GAP: peer/network proof plus trust/AVRCP integration; optional codec expansion is not on the critical path. Before claiming Bluetooth as a release feature, use at least a fresh paired headset and a second interoperability peer, test disconnect/range loss/reboot and wired switching, then run Wi-Fi traffic concurrently. This is a proposed qualification plan, not permission to activate radios or change bonds now.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
