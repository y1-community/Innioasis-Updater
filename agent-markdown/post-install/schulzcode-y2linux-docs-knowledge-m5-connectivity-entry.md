---
title: "M5 connectivity entry audit — 2026-09-15 - Innioasis Updater"
description: "M5 connectivity entry audit — 2026-09-15 <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m5-connectivity-entry.html"
---

# M5 connectivity entry audit — 2026-09-15 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M5 connectivity entry audit — 2026-09-15

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M5 connectivity entry audit — 2026-09-15 > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

M5 entry audit completed; integrated implementation/deployment blocked. The owner's connectivity scope is authorized. Its prerequisite of an intact, qualified M4 platform is not established: the installed POWER-02 has a current latched charging failure, and deep suspend, offline charging, RTC and thermal acceptance remain open. These are substantial gates, not one small residual test. M4 is not rebuilt under M5. Neither issue #30 nor #31 can close.

[Fresh hardware evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-15-m5-entry%2FREADME.md) · [Roadmap](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md) · [Subsequent POWER-03 correction and qualification](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fy2linux-m4-power-03-deployment.md).

## Actual entry state

The fresh session started at `bbbbbf20e96860089b015c19501b7d39638c5419` on `main`, then equal to `origin/main`. Existing POWER-02 USB workaround, recorder and September 14–15 evidence changes were present. They were reviewed and checkpointed as `ef285f1`; the USB startup code was preserved byte-for-byte. The old September 13 session handoff and issue #31's SD-root entry are historical.````````````````````````````````

| Component | Current evidence |
| --- | --- |
| Production BOOTIMG | Source 83d475ef71a3dd84f6e3cc483a7637b13520e4f7, Linux 6.18.0-y2linux-m4-power-02. Complete image-length readback matches the retained image. |
| Internal system/data | Live ext4 /dev/mmcblk0p5 at /, p7 at /data, both read-write; exact stock logical geometry checked. No SD block device in this inventory. Layout/data schema 1 remains. |
| Charging | PC charging reached the 4.2-V software ceiling at uptime 747.328296 s, latched Y2_FAULT_VOLTAGE=0x8, and remains inactive at the fresh inspection. Earlier September 14 OVP 0x10 is a separate unresolved event. No fault clear or limit change. |
| USB/SSH | Exact previously retained host fingerprint matched before strict SSH with a private temporary pin. Default known_hosts unchanged. MUSB remains on/active; installed startup hash matches ef285f1. Two earlier same-boot reconnects remain the qualified extent. |
| Suspend | freeze mem, s2idle [deep]; SPM reports entries=0 resumes=0 aborts=0 broken=0 on this boot. Availability is not physical qualification. |
| RTC/thermal/DVFS | RTC reports 2082-07-31. CPU about 14.7°C versus PMIC about 46.9°C, still unqualified. Four CPUs online, current frequency 598 MHz. No frequency or wake test was performed. |
| Native audio | Y2Audio exists. Retained clean S16/44.1-kHz headphone result stands; no new playback, 48-kHz/channel/repeat or speaker acceptance. |
| Native connectivity | Only lo and usb0; no HCI class. Built kernel disables wireless, Bluetooth, rfkill and firmware loader. Buildroot disables BlueZ, BlueALSA, D-Bus, iw and wpa_supplicant. |

The current power owner remains the production PWRAP/regmap/MFD and its charger, ADC, thermal, RTC and regulator consumers. The existing SPM driver owns the stock-matched suspend PCM, CPU context and wake policy. Charging retains watchdog service and vetoes suspend while active. Rescue handles offline charging before normal storage/audio startup. Connectivity must consume these owners and the normal-boot gate; it must not add another SPM/PWRAP owner.

M3 remains ASoC/ALSA DL1 → second I²S → upstream CS43131, with VGP2 at 1.8 V and ordered GPIO20/18/15 rail enables. AP_DMA is shared with I²C. Existing CCF ownership and headphone behavior must survive BTIF DMA and radio power cycling.

## Hardware identity: distinguish observations from reference````````````````````````````````````

| Item | Evidence and conclusion |
| --- | --- |
| Product/board | Owner identifies the older Y2 without useful FM reception. Stock product family is eastaeon82_wet_kk; no numeric PCB revision has been read. |
| Digital connectivity | Own retained stock properties name CONSYS_MT6582, module postfix _consys_mt6582, platform MT6582; current native DT/product agrees on MT6582. This identifies the integrated family. |
| Analog/FM identity | Own August 1–2 Y2Player report records FM driver getchipid=0x6627 and hardware-version tuple [26151,0,0,0,0]. This is a driver-reported identity, not a newly read analog-die revision. |
| Silicon stepping | Unconfirmed for this controller. Android ro.mediatek.chip_ver=S01 is a build property. Patch header 8a00 is firmware metadata. Neither establishes the running HVR/FVR. Donor table accepts HVR 0x8a00/E1 and 0x8a01/E2; both select the E1 patch family. |
| Bluetooth transport | Own stock snapshot has mtk_btif, IRQ82, TX-DMA IRQ103, RX-DMA IRQ104 and active IRQ217 BTIF_WAKEUP_IRQ. This corroborates BTIF with AP_DMA. WMT manages functions; STP multiplexes transport; HCI belongs above the BT channel. |
| Wi-Fi transport | Own stock platform has mt-wifi. Donor MT6582 fullmac uses AHB HIF at 0x180f0000, GIC SPI184 (vendor IRQ216), not an SDIO function. Own native HIF/chip capability response remains missing. |
| UART/SDIO | Retained init's ttyMT2 comment and commented SDIO module declarations are generic stock setup. They do not override the actual BTIF evidence or establish a wired UART/SDIO radio. Production MMC nodes both retain no-sdio. |
| Shared antenna | Own stock WMT_SOC.cfg sets coex_wmt_ant_mode=1; donor interprets 1 as a shared antenna with arbitration. Physical RF wiring/PTA performance is not measured. |
| FM | FM reception unsupported on this board revision. Owner statement agrees with the earlier failed reception work. No M5 FM driver, tuning or reception tests. Later populated boards need their own conditional description and evidence. |

Own stock observations are retained in sibling Y2Player's `out/hardware-snapshots/2026-07-29_004316/{identity/getprop.txt,hardware/proc-interrupts.txt,hardware/platform-devices.txt}` and `docs/FM_RADIO_FEASIBILITY.md`. Only non-identifying selected fields are retained in this audit. No other player's hardware result is relabelled as ours.

### Resources to reconcile before a driver can own them

The following is a donor/source map, not a claim that Linux 6.18 has probed it:````````````````````````````````

| Resource | Reference | Required production ownership |
| --- | --- | --- |
| CONSYS registers | MCU 0x18070000, TOP 0x180b0000 | One connectivity-core device; guarded access only while powered. |
| Power/reset | SPM CONN +0x280, AP_RGU CONSYS reset, infracfg bus protection/remap | Share the existing framework owners with serialized field-level control and checked unwind. No overlapping uncoordinated MMIO drivers. |
| BTIF | 0x1100c000; SPI50 | Transport below STP/HCI; bounded receive/transmit and error recovery. |
| BTIF DMA | AP_DMA 0x11000000, TX +0x780, RX +0x800; SPI71/72 | Proper DMA allocations, IRQ lifecycle and references to the already shared AP_DMA clock. |
| CONN wake | SPI185, vendor IRQ217 | Core-owned wake IRQ; explicit suspend policy, no accidental new wake source. |
| Wi-Fi | AHB HIF 0x180f0000, SPI184 | cfg80211/nl80211 and normal netdev; shared core references. |
| Supplies | MT6323 VCN18, VCN28, VCN33_BT, VCN33_WIFI | Regulator consumers through existing MFD/regmap. Reconcile board need and exact HW-control masks before extending the PWRAP allowlist. |
| Clocks | CONNMCU, BTIF, AP_DMA; stock co_clock_flag=1 | CCF and shared 26-MHz clock policy; preserve I²C/audio clocks and M4 oscillator/suspend behavior. |
| Reserved RAM | Current exclusions [0x81800000,0x84000000) and [0xbdf00000,0xc0000000) | Preserve all exclusions. Donor CONSYS 1 MiB at 0xbdf00000 differs from stock-inferred 0xbfa00000; choose only after remap/ownership reconciliation. |
| MD1 calibration boot | External ROM window 0xbe000000/22 MiB, shared memory 0xbf600000/0x1c4000 | These lie within the existing high exclusion. Their presence is not permission to reuse live firmware state or to change RAM policy. A bounded kernel-owned CCIF/firmware lifecycle is still needed. |

## Firmware inventory and supply policy

Five relevant files were extracted on the host from the owner's retained `Y2Player/y2_v3.2.0_FM-20260813/system.img`, `/etc/firmware/`. The sparse image was expanded into an ignored private regular file and read with `debugfs` without `-w`. Existing source-ROM provenance was reused, not re-audited.

[Machine-readable inventory, exact SHA256 and patch metadata](https://github.com/schulzcode/y2linux/blob/HEAD/docs/knowledge/evidence/m5-firmware-inventory.json). This is an inventory, not an approved release payload or proof of firmware selection on the physical controller. No redistribution grant has been established for any of these vendor files; none is committed or packaged.``````````````````````````

| Filename | Bytes | Function / compatibility evidence | Loading position | Proposed system path after validation |
| --- | --- | --- | --- | --- |
| WMT_SOC.cfg | 80 | Board clock/coexistence parameters; own stock co-clock/shared-antenna settings | Parse before core initialization; validate supported keys | /lib/firmware/mediatek/mt6582/WMT_SOC.cfg |
| modem_1_2g_n.img | 2424376 | MT6582 2G MD1 firmware; exact hash matches the historical cold-calibration experiment | Complete required calibration startup and verify MD1 off before exposing radios | /lib/firmware/mediatek/mt6582/modem_1_2g_n.img |
| mt6572_82_patch_e1_1_hdr.bin | 17476 | WMT ROM-v1 patch family; header HW/FW 8a00 | Patch 1 of 2, wire address bytes 00 00 0e f0 | /lib/firmware/mediatek/mt6582/mt6572_82_patch_e1_1_hdr.bin |
| mt6572_82_patch_e1_0_hdr.bin | 33120 | Same family/build as patch 1 | Patch 2 of 2, wire address bytes 00 00 06 00 | /lib/firmware/mediatek/mt6582/mt6572_82_patch_e1_0_hdr.bin |
| WIFI_RAM_CODE_MT6582 | 160368 | Matching stock name and donor MT6582 firmware request; actual firmware capability response absent | Wi-Fi function initialization after shared core/calibration readiness | /lib/firmware/mediatek/mt6582/WIFI_RAM_CODE_MT6582 |

Patch byte 24 encodes total count in its high nibble and order in its low nibble: `_1` has `0x21`, `_0` has `0x22`. Never sort by filename for download. The remaining WMT reset/configuration handshake must follow the validated controller protocol; this table is not a complete executable boot sequence.

Normal boot must use local `request_firmware()` inputs. Provision required vendor files through explicit owner extraction/supply with checked size/hash, headers and compatible controller revision. Missing or incompatible firmware must leave radios unavailable while the player boots. Do not silently fetch blobs, infer a redistribution license from a GPL driver, include unrelated WIFI variants/FM blobs, or take calibration from an external fixture.

## Own calibration and address ownership

Strict authenticated read-only inspection now establishes:
  - Current Y2DATA has no `/data/nvram`, `/data/network` or `/data/bluetooth`.

The original Android `/data/nvram` tree is not present in this Linux layout.
  - The exact POWER-02 image, MMC host `11230000`, MMC type, disk length and p5/p7

geometry were checked before bounded reads in stock logical disk coordinates. The driver performs the existing 23552-sector translation; do not add it twice.
  - Own NVRAM: start `0x00400000`, length `0x00500000`; own PROTECT_F:

`0x00900000`/`0x00a00000`; own PROTECT_S: `0x01300000`/`0x00a00000`. Reads used `dd if=...` only. Their bytes and per-device hashes remain private under `evidence-private/20260915-m5-entry/`, mode 0600 in a private directory.
  - PROTECT_F/S are ext filesystems with small `/md` record sets. They were

inspected on host copies without mounting or replaying a journal. NVRAM is nonempty binary data with no observed literal APCFG/WIFI/BT_Addr path names. This does not prove those records are absent, corrupt, or recoverable.

The backup container/LID mapping, versions, checksums and effective calibration selection still need decoding. Generic firmware, board RF/power tables, unit-specific calibration and addresses must remain separate. The public donor Wi-Fi reader expects Android `/data/nvram/APCFG/APRDEB/WIFI` and also contains a write path; those APIs are not suitable for protected production calibration.

The eventual production reader should expose only validated, required records through a read-only provider/consumer contract. Fail radio initialization on missing mandatory RF data; never fabricate calibration or modify protected partitions. Any volatile firmware filesystem writes require explicit protocol semantics and must never become factory-data writes.

Neither a valid Wi-Fi MAC nor a valid Bluetooth address is established yet. Do not use donor defaults, one release-wide address, or addresses from these private captures in public logs. First validate factory identity and the controller's address behavior. Any necessary generated identity needs a supported programming path and persistent per-unit storage; this audit does not select such a fallback. Public receipts contain no calibration bytes, MAC/address values, pairing keys, credentials or per-device calibration hashes.

## Historical calibration and donor code decisions

The pinned reverse-engineering source remains `f96d4c7dddbcafeb31919fe1fbe2dab99c4bd641`; donor kernel remains `53fb57bb99c916c24b65db5b7f9723be37f67826`. Existing [reverse-engineering audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md) remains authoritative about evidence origin and missing private inputs.

Its cold result required 592 ordered filesystem operations plus an independent restore query, settling after boot-ready, and verified MD1 shutdown. Power-only and boot-ready-only attempts failed. The exact generic modem firmware matches our stock file, but its `smem.bin`/`fs.bin` contain another unit's state. They are not a production filesystem service and cannot supply this Y2's calibration. No external bootstrap/MMIO script was executed.

Direct donor import would also bring:
  - Overlapping plain mappings of SPM/infracfg and global singleton state.
  - AP_DMA clock handling which deliberately leaks the clock reference to avoid

breaking its older I²C integration.
  - Android-path NVRAM reads/writes, debug overrides and permissive fallback paths.
  - Hard-coded Bluetooth radio-calibration command payloads that log success even

after command errors; no own-data provenance for those values.
  - A controller-wide Basic Rate default, LE command-bitmap adjustments and an

E2 extended-feature quirk, none verified on this unit.

Port only needed protocol/hardware behavior into Linux 6.18 with proper lifetimes, locking, checked failures and one core owner. Keep the current M4 power architecture and common production DT. No second radio driver or raw-MMIO userspace bootstrap is introduced.

## Userspace and future settings contract

Current pinned Buildroot is 2025.02.17, BusyBox init, Bootlin ARMv7 hard-float/glibc 2024.05-1. Its package recipes offer BlueZ 5.79, wpa_supplicant 2.12, and BlueALSA 4.3.1. These are available recipe versions, not installed or finally selected M5 release versions. Before a candidate, review the applicable LTS package fixes and pin the selected source. The [Buildroot 2025.02 LTS line](https://buildroot.org/lts.html) has a three-year support policy; that alone is not a security audit of each bundled package.

The production design to implement after entry dependencies are resolved is:``````````

| Consumer function | Standard interface / service | Persistent state |
| --- | --- | --- |
| Wi-Fi radio/scan/connect/forget/status | cfg80211/nl80211, wpa_supplicant control/D-Bus, rfkill; iw for qualification | /data/network, directories 0700 and credentials/config 0600 |
| IP/DNS/reconnect | Bounded BusyBox DHCP lifecycle bound to association events; preserve USB networking independently | Saved network priorities/security and user-selected country; leases/runtime sockets in /run |
| Bluetooth discovery/pair/trust/connect/remove/status | Kernel HCI, BlueZ org.bluez D-Bus and management APIs; bounded pairing agent | Standard /var/lib/bluetooth persisted through /data/bluetooth, private permissions |
| A2DP Source | ALSA PCM → BlueALSA → BlueZ Media transport → HCI | Per-device preferences only; SBC baseline, no optional codec required |
| AVRCP/metadata | BlueZ Media1 player registration with a standard MPRIS player object | Aliases/preferences in Y2DATA; future player supplies real metadata/controls |
| LE/GATT/battery | BlueZ standard interfaces, only for capabilities actually reported and verified | Bonds on Y2DATA; battery exposed only when reported |

[BlueALSA's versioned daemon documentation](https://github.com/arkq/bluez-alsa/blob/v5.0.0/doc/bluealsad.8.rst) supports the lightweight ALSA bridge evaluation. BlueZ's [Media API](https://bluez.readthedocs.io/en/latest/media-api/) supplies endpoint and player registration. Installing an audio bridge alone does not implement player commands/metadata or prove headset compatibility. A bounded qualification client can exercise that contract without implementing Y2PlayerNative.

Rootfs updates may add directories and standard bind mounts/symlinks after validated Y2DATA mount, but must preserve existing data and refuse unsafe paths. No USRDATA image is required for an additive M5 migration. BOOTIMG continues to own kernel/modules, Y2ROOT owns userspace/approved firmware, Y2DATA owns secrets and user state. No OTA updater or UI is implemented.

Initial Wi-Fi target is station mode, 2.4-GHz b/g/n and HT20, **pending actual firmware/cfg80211 capability and regulatory validation**. HT40, AP/P2P and WPA3 are conditional extras; donor 802.11w is disabled, so SAE/PMF cannot be promised. No 5-GHz/ac/ax/MIMO claim. Use WPA2-PSK and normal secure defaults, regulatory database/country intersection and the unit's correct power tables.

Initial Bluetooth target is Classic discovery/bonding/reconnect and A2DP Source/SBC/AVRCP. BLE capability/version is unqualified. Start EDR investigation without importing the donor restriction; record controller features, packet modes and credits. Any required Basic Rate fallback must match the affected controller/firmware/behavior and remain explicitly documented.

## PM, coexistence and recovery contract still to implement

One serialized core owns OFF → power/firmware/calibration → READY and bounded failure cleanup/restart. Wi-Fi and Bluetooth hold function/runtime references; the last inactive function permits supported power-down. Failed calibration never publishes a usable interface. Error recovery must stop consumers, drain DMA/IRQs, reset/reload and restore the standard interfaces without a reflash. Warm restart is a distinct hardware requirement, not an assumed consequence of cold success. Interrupted calibration and subsequent restart need explicit tests.

Preserve stock-evidenced coexistence configuration and qualify simultaneous Wi-Fi traffic plus A2DP. Do not force separate-antenna mode or disable one radio to hide arbitration failures. Screen blanking is independent of system suspend: active A2DP/download work retains the required runtime references and prevents deep suspension of the active path; paused/idle operation releases them. Initial full-suspend policy must explicitly quiesce radios and reconnect on resume unless retained-link/wake behavior has physical proof. Offline-charge mode starts no radio driver activity, firmware calibration or radio userspace.

## Required deployment and qualification boundary

No BOOTIMG/Y2ROOT M5 candidate was built. There are no M5 install instructions or request to flash. Preserve POWER-02 and its fallback; M5 entry remains blocked by M4 charging/qualification and unresolved own controller/calibration mapping.

When those dependencies are resolved, build one integrated production candidate and provide all 26 owner-requested deployment fields: commit, controller/revision, firmware/license/hash/order, calibration/addresses, kernel/userspace/BlueZ/audio choices, capabilities/EDR/BLE/coexistence/PM, changed components, exact images and fallback hashes, preserving install steps and one-session acceptance plan. Then stop for the owner's manual SPFT/deployment. Assistant flashing remains prohibited. After the owner reports it running, execute one coherent session:
  - Wi-Fi: real scan, WPA2, DHCP/gateway/DNS, LAN/internet, saved networks,

wrong password, AP loss/return, renewal, reboot, radio toggle and resume.
  - Bluetooth: multiple available device categories, discovery/pair/bonds,

SBC A2DP, negotiated codec, controls/volume/metadata, reconnect, power cycles, range loss/return, reboot and screen-off playback.
  - BLE: capability query and, if supported with available hardware, scan/GATT

and a harmless characteristic test. No invented BLE version/capability.
  - Coexistence: sustained useful Wi-Fi transfer while A2DP plays; record

throughput, dropouts, retransmissions, HCI/firmware faults and recovery.
  - PM/stability: bounded repeated radio/reconnect/suspend/reboot cycles,

explicit idle/full-suspend policy, recovery and persistent state, with M4 regression checks. Observe errors/memory growth and retain private traces.

Optional WPA3, HT40/AP/P2P, extra profiles/codecs and battery display may remain scoped limitations. Core Wi-Fi, A2DP/SBC/AVRCP, reconnect, coexistence, privacy, recovery, persistence and M4 preservation are hard gates. FM is excluded on this board. GPU/lima, applications and Y2PlayerNative remain later work.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
