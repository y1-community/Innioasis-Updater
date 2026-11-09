---
title: "M5-CONNECTIVITY-01 — manual deployment handoff - Innioasis Updater"
description: "M5-CONNECTIVITY-01 — manual deployment handoff <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-m5-connectivity-01-deployment.html"
---

# M5-CONNECTIVITY-01 — manual deployment handoff - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M5-CONNECTIVITY-01 — manual deployment handoff

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M5-CONNECTIVITY-01 — manual deployment handoff > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

**The integrated candidate is built and host-validated. M5 remains OPEN pending owner installation and physical qualification.** POWER-03 is the owner-accepted M4 baseline. No fresh entry audit, private partition reacquisition, physical flash or protected-partition write was performed.

## 1–5. Source, hardware and factory identity
  - Source commit:`022c701010c467904ab6025cd98535d3b861c771`. Kernel `6.18.0-y2linux-m5-connectivity-01`;

rootfs `2025.02.17-connectivity.1`. The evidence commit is the commit containing this receipt; it does not change the built source identity.
  - Controller: CONSYS_MT6582; Wi-Fi is MT6582 AHB fullmac. Bluetooth is

BTIF + AP_DMA → STP/WMT → standard HCI. One shared antenna. The older board has no useful FM reception; FM is unsupported and excluded from M5.
  - Silicon stepping: actual HVR/FVR remains a first-boot measurement.

The driver reads chip/HVR/FVR and accepts the inventoried E1/E2 HVR family `0x8a00`/`0x8a01`, with chip `0x6582`. No invented numeric PCB revision.
  - Factory mapping: read-only logical NVRAM `0x400000`/5 MiB,

PROTECT_F `0x900000`/10 MiB, PROTECT_S `0x1300000`/10 MiB. The first 4 MiB AP backup is empty; the tail is history receipts. BT LID 1/001 is 64 bytes; Wi-Fi LID 30/000 is 512 bytes; special LID 36 is PRODUCT_INFO. This unit's PROTECT_F provides ST33A004 (2060 bytes) and MP0D_000 (4); PROTECT_S provides ST33B004 (2060). They remain opaque MD factory records. Journal replay and generated calibration filesystem writes affect bounded RAM only. The native cold boot must satisfy the filesystem completion gate, shut MD1 down, and complete WMT calibration before radio use; physical success is still pending.
  - Addresses: use a valid firmware/controller address when present; reject

zero/multicast and the known generic BT default. Otherwise independent random local unicast addresses persist privately in `/data/connectivity`. Board defaults have their generic address fields erased. No release-wide identity, copied external calibration, private raw dump or protected write is used.

## 6–7. Firmware and provisioning
  - Firmware list, exact SHA256 and first-start loading order:
````````````````````

| Order | Filename | Bytes | SHA256 |
| --- | --- | --- | --- |
| 1 | modem_1_2g_n.img | 2424376 | 5059775975cbf6ab74c43978ca8f65d9a274b83585f456134e39b09f6dc7a4f1 |
| 2 | WMT_SOC.cfg | 80 | cea0a94b8a88e9c24e6835446ebc3106d7b100c3709ea98e8bb7368689c8a2b5 |
| 3 | mt6572_82_patch_e1_1_hdr.bin | 17476 | 96eb25489305bd472805db1da33bcc0acd37b5bb21cceda98d7e88ba1179ca37 |
| 4 | mt6572_82_patch_e1_0_hdr.bin | 33120 | fa3be4a92540296de512d64f56272746be10bdfa2db571c8ceada2d40cd616f0 |
| 5 | WIFI_RAM_CODE_MT6582 | 160368 | 4def37522e2bfd2d4b78e01bf9f567a37e3f67ab3d7b6646ffb317f5b2b49b82 |

Install directory: `/lib/firmware/mediatek/mt6582/`. Patch `_1` precedes `_0` by header sequence. After successful cold calibration, MD1 stays off for the rest of this Linux boot; warm CONN restart reloads volatile patches and function firmware. Wi-Fi RAM code loads when Wi-Fi starts. The build also installs address-free `WIFI.defaults` (512 bytes) and `BT.defaults` (64), with exact hashes in the [owner input receipt](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/evidence/y2linux-m5-connectivity-01/owner-firmware.json).
  - Provenance/legal status: the five files are from the owner's retained

Y2 v3.2.0_FM stock image and the two defaults from its hash-checked stock `libcustom_nvram.so`. Reuse the [completed inventory](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/evidence/m5-firmware-inventory.json). Vendor redistribution permission is not established. This is an explicit owner-local image. No blobs are committed/uploaded and no boot downloads occur.

## 8–20. Implemented production platform``````

| # | Area | Candidate behavior; physical acceptance pending |
| --- | --- | --- |
| 8 | Shared core | One CONSYS power/reset/recovery owner using existing CCF, SPM, PWRAP/regmap, regulators and reset framework; existing reserved RAM only. Bounded native MD IPC/filesystem calibration. |
| 9 | Wi-Fi | Linux 6.18 AHB fullmac port, cfg80211/nl80211 wlan0, rfkill, firmware/regulatory/power-save and shared recovery. No app-specific kernel API. |
| 10 | Bluetooth | Coherent AP_DMA TX/RX FIFOs, BTIF IRQs, reliable STP/WMT and standard hci0. Dedicated DMA windows and balanced clocks preserve I2C/audio ownership. |
| 11 | Buildroot | 2025.02.17, iw 6.9, signed regulatory database, D-Bus, BlueZ, BlueALSA, ALSA plugins, udhcpc/iproute2, TLS curl/CA certificates and iperf3. |
| 12 | Wi-Fi userspace | wpa_supplicant 2.12, nl80211/control socket/D-Bus; DHCP lifecycle follows association. Saved networks use private Y2DATA configuration. |
| 13 | BlueZ | 5.79, D-Bus 1.14.10, normal management/client/monitor/audio interfaces, dual-mode discovery from actual controller capabilities; bonds/trust persist. |
| 14 | Audio / AVRCP | BlueALSA 4.3.1, libsbc 2.0, A2DP Source and standard ALSA PCM/control. SBC is the selected codec. Bounded y2-a2dp-check exposes BlueZ/MPRIS controls and fixture metadata; no final player UI. |
| 15 | Expected Wi-Fi | 2.4 GHz b/g/n, single stream, HT20 station, open/WPA2-PSK. World regulatory default; persist the user's lawful country. HT40/AP/P2P/WPA3 unqualified; no 5 GHz/ac/ax/MIMO claims. |
| 16 | Expected Bluetooth | Classic discovery/pairing/bonds, A2DP Source/SBC, AVRCP controls/volume/metadata through BlueZ; automatic preferred trusted audio-device reconnect. Actual feature/version/profile interoperability requires physical tests. |
| 17 | EDR | No global Basic Rate restriction or feature masking. Test controller features, packet modes and credit progress; apply a narrow workaround only for a demonstrated failure. |
| 18 | BLE | BlueZ LE/GATT tools included; capability and scan/GATT qualification conditional on actual firmware reporting. No Bluetooth 5.x claim. |
| 19 | Coexistence | Own shared-antenna WMT configuration and co-clock, one function owner. Sustained Wi-Fi + SBC audio is a hard physical gate, still pending. |
| 20 | PM / recovery | Counted function references; both-off runtime power-down, bounded shared recovery, explicit radio-off full-suspend policy and preference restoration. Screen blanking leaves active audio/transfers alone; activity leases prevent deep suspend during work. Offline charging never activates radios. Active BT transport idle power still needs measurement. |

[Implementation details and source provenance](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm5-connectivity-implementation.md).

## 21–23. Candidate images and Y2DATA preservation
  - BOOTIMG changed. Package directory:

`/home/luca/Dokumente/Code/Y2Linux/out/y2linux-m5-connectivity-01/`.
  - Y2ROOT changed. Use both new images together:
````````````````

| Artifact, relative to the package directory | Bytes | SHA256 |
| --- | --- | --- |
| BOOTIMG.img | 6144000 | a24b257a795b8ffea198e57344f20a514f4fa5e7148572ac8331afed9e996a96 |
| Y2ROOT.img | 536870912 | add6b375d33dbfa3f36e505c9784c934c3b31e2073041f514dcd2db524408e67 |
| fallback/BOOTIMG.img | 5408768 | 66b6ecd5ef54da6f3ea07be2c9deda284d0a7636e9c6da4c5d72d84eca5fc010 |
| fallback/Y2ROOT.img | 536870912 | 814a5b2543931e01cee2eb6f641c3b6e02317bd6308d2d663aea78f618bd554f |

  - Y2DATA is preserved in place. No data image, formatting or schema reset.

First normal boot creates private network/Bluetooth/identity directories and bind mounts standard BlueZ/BlueALSA state paths. Existing media, settings, SSH authorization and host keys remain. Credentials/bonds are absent from immutable release inputs. BOOTIMG/Y2ROOT updates keep the existing schema-1 platform contract; the OTA updater itself is not implemented.

Host validation: 81 production/M4/connectivity tests, ARM executable/ plugin checks, emitted DT/config/BOOTIMG checks, clean ext4, verified firmware, and 16 package rejection cases. [Evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-m5-connectivity-01%2FREADME.md). These results do not prove calibration, radio operation, EDR, coexistence, reconnect, standby consumption or M4 resume behavior on this candidate.

## 24–25. Exact owner installation and fallback
  - Install manually:
`1. On the host, verify the complete package: ```sh cd /home/luca/Dokumente/Code/Y2Linux/out/y2linux-m5-connectivity-01 sha256sum -c SHA256SUMS ``` 2. Close other flash/serial tooling, shut down the Y2, and open the established working SP Flash Tool/Download Agent setup. 3. Load this directory's `MT6582_preserve_data_scatter.txt` and choose **Download Only**. Confirm exactly **BOOTIMG → BOOTIMG.img** and **ANDROID → Y2ROOT.img** are selected from this directory. Every other row, including USRDATA, PRELOADER/LK, partition tables and protected calibration, remains unchecked and has no payload mapping. Do not use Format or Firmware Upgrade. 4. Perform the established manual USB connection/download procedure and wait for success. Disconnect the flashing cable. Charger insertion should retain M4 offline charging; hold and release Power intentionally for normal boot. Connect the PC for existing `root@10.42.0.1` SSH access. 5. Report the candidate running. The assistant then performs the SSH tests; radio preferences initially default off and no AP password is packaged.`
  - Fallback: use `fallback/MT6582_preserve_data_scatter.txt`, Download Only,

with its POWER-03 BOOTIMG and previous Y2ROOT, selecting the same two rows. Their exact sizes/hashes are in the table above and SHA256SUMS. This restores the owner-accepted platform while preserving current Y2DATA.

## 26. One coherent physical qualification session
  - Follow the [nine-phase physical procedure](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm5-connectivity-implementation.md%23one-physical-qualification-session-after-owner-deployment&anchor=one-physical-qualification-session-after-owner-deployment):
`1. Verify candidate identity, same internal storage/data, baseline M4 health and private bounded logging; record actual silicon and calibration state. 2. Wi-Fi scan, legal country, WPA2, DHCP renewal, gateway/DNS/LAN/HTTPS, wrong password/forget/save, AP disappearance/return and saved reconnect. 3. Pair/trust multiple available audio categories; prove SBC, AVRCP controls, volume/metadata, peer off/on, local disconnect and screen-off playback. 4. Read EDR/LE capabilities and credit behavior; test BLE scan/GATT if supported with an available phone/accessory. Record unavailable categories honestly. 5. Sustained useful Wi-Fi transfer plus SBC playback, recording throughput, dropouts/retries/HCI errors/firmware resets and reconnect behavior. 6. Five radio toggle/reconnect cycles and controlled all-off recovery; verify shared power release and absence of unexpected reboot/controller wedge. 7. Active-work suspend inhibition, Power and RTC deep wakes with same boot ID and incrementing SPM counters, radio reconnect, display/input/wheel/ ALSA/eMMC/SD/USB/charging regression checks. 8. Reboot reconnect and persisted identities/networks/bonds, plus offline charging and intentional normal boot with radio absence in offline mode.`

Owner actions are limited to manual installation, available AP/peer setup, charger/Power handling and listening/visible confirmation. Commands run over SSH. Only concrete physical failures justify targeted corrections.

STOP for owner manual installation. M5 is NOT CLOSED.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
