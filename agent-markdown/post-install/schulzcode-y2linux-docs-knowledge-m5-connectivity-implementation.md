---
title: "M5 production connectivity candidate - Innioasis Updater"
description: "M5 production connectivity candidate <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m5-connectivity-implementation.html"
---

# M5 production connectivity candidate - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M5 production connectivity candidate

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M5 production connectivity candidate > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Implementation continues from owner-accepted M4 POWER-03 and the completed entry audit `67cbe8f1df439a25eb542fc5c6f35fc57b758430`. This document describes the implementation and deployment contract. **No native radio result is yet physically qualified. M5 remains open.** The source commit and finished image identities belong in the package manifest and deployment receipt.

## Hardware and ownership``````````````````

| Item | Implemented contract / evidence limit |
| --- | --- |
| Platform | CONSYS_MT6582; MCU chip register must report 0x6582. |
| Stepping | WMT reads HVR/FVR. Accept stock patch header family 0x8a00 and HVR E1 0x8a00 / E2 0x8a01; this unit's live stepping remains to be read. |
| Board | Owner identifies the older Y2 with no useful FM reception hardware. No fabricated numeric PCB revision. FM remains unsupported on this board. |
| Wi-Fi | MT6582 AHB fullmac, MCU/HIF protocol from the pinned MediaTek GPL source. The legacy MT6628 compile symbol selects that protocol; it is not a claim of a separate MT6628 chip or SDIO wiring. |
| Bluetooth | BTIF + dedicated AP_DMA TX/RX FIFOs, STP/WMT channel multiplexing, standard Linux HCI. |
| RF | This product's WMT setting selects one shared antenna and co-clock. VCN18, VCN28 and the two VCN33 function controls use existing PWRAP/regmap and regulators. |
| Memory | Existing high exclusion only: CONN EMI 0xbdf00000/1 MiB, MD ROM 0xbe000000/22 MiB, MD shared memory 0xbf600000/0x1c4000. Linux RAM boundaries do not expand. |
| IRQs | BTIF SPI 50; TX/RX DMA 71/72; wake 185; CCIF 100 (stock absolute IRQ 132); Wi-Fi 184. DT verifies the fixed resources. |

`kernel/platform/connectivity/core.c` is the shared power/reset/recovery owner. The existing CCF owns shared clock, remap and bus-protection registers; SPM owns CONN/MD1 domain transitions under its existing lock. The upstream MT6582 watchdog reset controller supplies CONN reset. BTIF maps only its two DMA channel windows, leaving I2C/audio and the shared AP_DMA clock owner intact.

## Factory records and identity

The production provider opens the established logical `/dev/mmcblk0` interface read-only. It reads NVRAM at `0x400000`/5 MiB, PROTECT_F at `0x900000`/10 MiB and PROTECT_S at `0x1300000`/10 MiB. The existing 23,552-sector translation is already implemented by the storage driver and is not applied a second time.

The acquired unit's first 4 MiB NVRAM backup is empty. Its nonzero tail contains `NVM_HistoryLog` recovery receipts, not saved Wi-Fi or Bluetooth records. The exact stock `libcustom_nvram.so` table maps BT_Addr to LID 1/version 001/64 bytes and WIFI to LID 30/version 000/512 bytes. The separate special-LID descriptor is LID 36 PRODUCT_INFO; it is not a second radio-record container.

PROTECT_F supplies `md/ST33A004` (2060 bytes) and `md/MP0D_000` (4 bytes); PROTECT_S supplies `md/ST33B004` (2060 bytes). These remain opaque factory MD records, not asserted to be a decoded RF trim table. The provider replays an ext4 journal only into bounded anonymous RAM, seals that copy read-only, and exports just the three records into root-only `/run/y2/factory`. Neither the source partition nor its journal is opened for writing. Unknown/nonempty AP backup formats fail closed rather than being replaced with defaults.

The Wi-Fi and Bluetooth board defaults come from this product's verified stock reader, with default addresses erased during provisioning. They contain no other unit's records. A valid firmware/controller address takes precedence; Bluetooth rejects the known generic stock default. Otherwise independently generated, locally administered unicast addresses persist as six private bytes in `/data/connectivity/{wifi-address,bluetooth-address}`. No release-wide address, partition identifier, raw calibration or pairing key is committed. Protecting Y2DATA preserves a fallback identity and its bonds across updates.

## Firmware and cold boot

The five firmware filenames, provenance, SHA256 values and compatibility notes remain in the [completed inventory](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/evidence/m5-firmware-inventory.json). They are installed under `/lib/firmware/mediatek/mt6582/`. On the first radio startup in a Linux boot, the loading order is:
  - `modem_1_2g_n.img`: bounded MD1 filesystem/calibration startup, then MD1 off.
  - `WMT_SOC.cfg`: shared antenna/co-clock policy is validated before WMT boot.
  - `mt6572_82_patch_e1_1_hdr.bin`: patch header sequence 1.
  - `mt6572_82_patch_e1_0_hdr.bin`: patch header sequence 2.
  - `WIFI_RAM_CODE_MT6582`: Wi-Fi function startup, two firmware image sections.

The build additionally installs address-free `WIFI.defaults` and `BT.defaults`, extracted by `tools/connectivity/provision.py` from the hash-checked stock reader. Build provisioning verifies all seven files. Kernel `request_firmware()` loads only the five reviewed names and verifies their size and SHA256 before transporting bytes. There is no boot-time download.

Redistribution permission for these vendor inputs is not established. This candidate is an explicit owner-local image, not a public firmware release. Public source contains the provisioning tool and hashes, not the blobs or private factory data. A later release must resolve permission or require the owner to provision/extract the same inputs.

Cold calibration uses a newly constructed stock-compatible CCCI runtime and a bounded filesystem service: five validated mailboxes, 4096 requests maximum, 5-second response deadlines, 90-second overall deadline, 16 MiB RAM filesystem quota, and an exclusive root-only service descriptor. Filesystem paths are virtual and cannot access the host filesystem. Writes affect RAM shadows only. No external `fs.bin`, `smem.bin`, response replay or other unit's private data is used. MD records seed the stock X/Y virtual roots; generated records are owned by this boot's firmware lifecycle.

The completion gate requires the normal boot handshake, successful restore query and read/close exchanges, no outstanding file handles/mailbox, and five seconds of quiescence. Both MD1 power-off acknowledgements must follow. WMT's own RF calibration command must then succeed. Physical validation must record the actual exchange count and radio behavior; neither a counter nor boot-ready alone proves successful calibration. The historical approximately 592-record run is behavioral evidence, not a replay file or invented measurement here.

There is one narrowly bounded inherited-state exception: if MD1 is powered but all four remaps, boot-enable and CCIF control/busy/pending are zero, the never-started LK domain can be reset/isolated and powered off despite the known missing bus-protection ACK. Live firmware shutdown never uses that exception. A failed live shutdown leaves radios unavailable and vetoes deep suspend while Linux still owns that MD lifecycle.

## Native interfaces and userspace``````````````````

| Component | Candidate configuration |
| --- | --- |
| Wi-Fi driver | cfg80211/nl80211/netdev wlan0; AHB PIO, bounded firmware/OID requests, shared recovery, rfkill enable/disable. |
| Initial Wi-Fi capability | 2.4 GHz b/g/n, one spatial stream, HT20 station, open/WPA2-PSK baseline. HT40/AP/P2P/WPA3 are not advertised as qualified. No 5 GHz/ac/ax. WPA3 cannot be added (Y2Linux #91, 2026-11-05): the gen2 driver hands the whole connection to the firmware (mtk_cfg80211_connect only, no auth/assoc/external-auth ops), whose auth modes are open, shared, WPA and WPA2 (PSK or 802.1X, wlan_oid.hENUM_PARAM_AUTH_MODE_T), and PMF is compiled out (CFG_SUPPORT_802_11W 0); SAE and Enhanced Open (OWE) need both. WPA2/WPA3 mixed networks join with WPA2-PSK; Reborn names WPA3-only, login (802.1X) and WEP networks in their rows. |
| Regulatory | Linux signed regulatory database, initial world domain, firmware channel list and power ceilings derived from cfg80211. Passive-only initiation channels are conservatively excluded. User selects a lawful country in persisted supplicant configuration; no country is inferred from another board. |
| Wi-Fi userspace | Buildroot 2025.02.17, wpa_supplicant 2.12 (nl80211, control socket and D-Bus), iw 6.9, BusyBox udhcpc, iproute2, curl/TLS/CA certificates, iperf3. |
| Bluetooth kernel | Standard HCI (hci0), H4 fragmentation over reliable STP, bounded retries and coherent AP_DMA FIFOs. Linux retains HCI credit accounting. |
| BlueZ | 5.79 with D-Bus 1.14.10, management/client/monitor tools and audio plugin; dual-mode policy, feature discovery from the controller. No fabricated version/LE bits. |
| Audio | BlueALSA 4.3.1, A2DP Source, libsbc 2.0, ALSA PCM/control plugins. No desktop audio server or proprietary codec. SBC is the only selected A2DP codec. |
| AVRCP | BlueZ Media/MPRIS player API plus BlueALSA volume control. y2-a2dp-check is a bounded PCM fixture client with Play/Pause/Stop/Next/Previous and metadata; Next/Previous restart the fixture with a track counter. It is not Y2PlayerNative. |
| Reconnect | A small policy service remembers a successfully connected, paired, trusted A2DP sink. Device1.ConnectProfile performs retries with bounded timeout/backoff; a passive Linux management socket distinguishes local disconnect/authentication failure from a disappearing peer. Local disconnect is respected until explicit connection or radio re-enable. Optional profiles are not auto-connected. |
| EDR | No Basic Rate restriction or controller feature masking. Record features, packet mode and credits physically; scope any later workaround to demonstrated failure. |
| BLE | BlueZ GATT client/server tools are available; expose and qualify LE only if this controller actually reports support. |

Settings use native wpa_supplicant control/D-Bus and BlueZ D-Bus for scan, connect, pairing, trust, forget and status. `y2-radio` persists radio preference and invokes normal rfkill/BlueZ controls. Root-only connectivity state lives in:
  - `/data/network/wpa_supplicant.conf`: saved networks, credentials and country;

mode 0600, `update_config=1`, no image credentials.
  - `/data/bluetooth/bluez` bound to `/var/lib/bluetooth`: bonds, trust and aliases.
  - `/data/bluetooth/bluealsa` bound to `/var/lib/bluealsa`: audio preferences.
  - `/data/bluetooth/preferred-audio`: private preferred-peer identity.
  - `/data/connectivity`: fallback radio identities.
  - `/data/system/dbus`: generated machine identity, retained across updates.

No-data/no-peer conditions do not block normal boot. The service starts in the background; helper restarts are rate-limited. Wired SSH remains available. Firmware errors report unavailability. Recovery drains consumers, stops IRQ/ DMA, isolates the shared domain and reloads; automatic retries are bounded to three per five minutes. An explicit off/on operation can request another safe recovery. A wedged DMA channel is reset only after remote isolation; the shared AP_DMA controller is never reset. Stuck isolation/power acknowledgements remain errors rather than permission to access live buffers.

## Power and coexistence

Both functions use counted references to the same core. When both references close, runtime PM powers the core down after one second; warm restart retains the successful MD calibration lifecycle for this Linux boot and reloads volatile CONN/BT/Wi-Fi state. Wi-Fi uses firmware power save while connected. Transport clock/rail behavior and warm calibration retention still need physical proof.

`y2-suspend` implements explicit full-suspend radio-off policy and restores saved radio preferences after same-session resume. Active work holds a shared `/run/y2/activity.lock` lease (`y2-radio-hold command ...`); full suspend requires an exclusive lease. The A2DP fixture client holds the lease while playing and releases it while paused. Future players/downloaders must follow this contract. Screen blanking does not change radio, audio or active-work references. Kernel suspend also rejects active functions or an unfinished owned MD lifecycle.

Initramfs offline charging never starts these userspace services, provides factory data or activates radios. Existing charger, RTC, thermal, DVFS, storage, display, input, audio and USB implementations remain the M4 baseline.

Coexistence uses the product's shared-antenna WMT configuration and common function owner. Sustained Wi-Fi traffic alongside SBC audio is a required physical gate; configuration presence is not a coexistence pass.

## Owner installation

The preserving package contains BOOTIMG + Y2ROOT and a separate fallback to the selected previous kernel/root pair. Its manifest records exact versions, source and image identities. It contains no Y2DATA image.
  - On the host, verify the package's `SHA256SUMS`.
  - Close any other serial/flash tooling, power the Y2 down, and open the

established SP Flash Tool setup with the same known-good Download Agent.
  - Load the package's `MT6582_preserve_data_scatter.txt`, choose Download Only,

and confirm exactly BOOTIMG → BOOTIMG.img and ANDROID → Y2ROOT.img. Keep USRDATA, PRELOADER, partition tables and every protected row unchecked. Do not use Format or Firmware Upgrade.
  - Perform the download manually using the established Y2 USB connection

procedure. After success, unplug/reconnect as appropriate. A charger-insertion boot should remain M4 offline charging; hold/release Power intentionally for normal Linux boot. Then report the candidate running.
  - Fallback uses `fallback/MT6582_preserve_data_scatter.txt` with its BOOTIMG and

Y2ROOT, Download Only, the same two selected rows, preserving current Y2DATA.

The assistant does not flash, format, deploy over SSH or write calibration.

## One physical qualification session after owner deployment

The assistant operates SSH and normal tools, saves private raw captures outside Git, and publishes only redacted results. Owner actions are limited to charger/ peer handling, password/pairing interaction, listening and wake-button actions.
  - Establish source/kernel/root versions, boot ID, mounts and Y2DATA continuity;

check the accepted charger/RTC/thermal/audio baseline and absence of boot crashes. Start private dmesg, btmon and network logs with bounded sizes.
  - Enable radios; record HCR/HVR/FVR, firmware hash verification, actual MD FS

completion/stop and WMT calibration; verify per-unit address choice privately. Check `iw phy`, regulatory policy and BlueZ/HCI reported capabilities.
  - Wi-Fi: scan, select the owner's WPA2 AP, provision its password without

logging it, obtain/renew DHCP, verify gateway/DNS/LAN/HTTPS; test wrong password, forget/save, hidden SSID if available, disconnect/reconnect and AP loss/return.
  - Bluetooth: pair/trust at least two available audio device categories, record

actual negotiated SBC, play the bounded fixture, test AVRCP controls/volume/ metadata and screen-off playback. Test peer off/on, reconnect and local disconnect. Record unavailable device categories explicitly.
  - If LE is reported, scan a suitable phone/accessory and exercise harmless GATT

reads/writes where available. No purchase required and no invented capability.
  - Run useful sustained LAN Wi-Fi transfer with SBC playback for at least ten

minutes; record throughput, real TX retries/failures, audible dropouts, HCI credit progress, controller/transport errors and resets. Investigate EDR only from this firmware/controller's observed traffic.
  - Repeat five radio disable/enable and reconnect cycles; verify clocks/rails

release, no unexpected reboot and bounded recovery. Exercise a controlled all-radios-off recovery through the production recovery interface.
  - Test active-work suspend inhibition, screen-off transfer/audio, paused/full

deep suspend with Power and RTC wakes, same boot ID, increasing SPM counters, reconnection and display/input/wheel/ALSA/eMMC/SD/USB/charging continuity.
  - Reboot once; verify root/data checks and saved network/bond/audio reconnect.

Check offline charging, intentional power-on and radio absence in offline mode with the owner. Record power policy/residency limits honestly.

Only concrete failures justify targeted fixes and a replacement candidate. M5 closes after these end-user gates pass, not when interfaces first appear.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
