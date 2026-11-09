---
title: "Actual system architecture - Innioasis Updater"
description: "Actual system architecture <!-- knowledge-base-scope: historical-audit/review -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-audit-current-system-02_system_architecture.html"
---

# Actual system architecture - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Actual system architecture

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Actual system architecture > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

Source authorities and commits are in [scope](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F00_SCOPE_AND_EVIDENCE.md). Arrows below describe existing ownership/data flow, not a proposed product.

## Boot and persistent storage`MT6582 Boot ROM -> retained stock preloader (DRAM/platform assumptions) -> retained stock LK -> BOOTIMG: Android boot header + Linux 6.18 + DT + rescue initramfs -> /init: proc/sys/dev/run/tmp, platform and display preparation +-> forced rescue / failed storage or compatibility checks | -> RAM-resident recovery/diagnostic environment +-> charger-only/low-battery gate -> offline-charge program | (no normal Y2ROOT/Reborn/radio startup) `-> identify internal eMMC by controller, geometry, label, UUID -> read-only noload root preflight and compatibility checks -> e2fsck -p; unacceptable result -> rescue -> mount Y2ROOT rw + Y2DATA rw,nosuid,nodev -> expose BOOTIMG-owned modules from /run/y2/modules -> switch_root -> BusyBox init / rcS -> platform/data setup -> Reborn supervisor -> USB/display/system logging/D-Bus/radio/SSH services`

`Y2ROOT` reuses stock ANDROID; `Y2DATA` reuses USRDATA. The tested addressing contract distinguishes scatter coordinates from native eMMC coordinates. Linux's Y2-specific stock-logical translation is essential; it is not generic eMMC behavior. Preloader/LK/partition tables/NVRAM/calibration are not update targets. `Y2DATA.img` is an initialization seed, not an update payload. A/B slots and automatic rollback are not implemented.

Evidence: [production init](https://github.com/SchulzCode/Y2Linux/blob/main/initramfs/production/init), [layout](https://github.com/SchulzCode/Y2Linux/blob/main/tools/production/layout.py), [package](https://github.com/SchulzCode/Y2Linux/blob/main/tools/production/package.py), [storage translation patch](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/patches/0023-y2-stock-emmc-capacity.patch), [data startup](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/board/y2/production-overlay/etc/init.d/S02y2-data).

## Hardware ownership map`Linux 6.18 + canonical Y2 DT + hashed patch/overlay manifest | +-- clocks/pinctrl/EINT/PWRAP -> MT6323 MFD/regmap | +-- regulators / ADC / charger power_supply / PMIC keys / RTC / poweroff +-- SPM -> CPU hotplug/suspend + MFG generic power domain +-- cpufreq-dt / CPU cooling -> fixed-voltage OPPs +-- thermal + efuse calibration -> CPU and PMIC die observations +-- DRM mediatek -> OVL/RDMA/COLOR/DSI/PHY -> panel/backlight +-- Lima -> Mali-400 MP2 -> Mesa render node -> PRIME/display scanout +-- input -> navigation/keypad/PMIC keys/APT32F wheel -> evdev +-- MSDC -> internal eMMC / external SD -> ext4/vfat +-- USB PHY/MUSB gadget -> ACM + USB Ethernet; PHY also owns charger detection +-- ALSA/ASoC -> MT6582 AFE DL1 -> I2S -> CS43131 -> headphone pins `-- one CONSYS parent -> rails/reset/BTIF-DMA/STP/WMT/firmware/calibration +-- fullmac Wi-Fi port -> cfg80211 -> wlan0 `-- standard HCI -> BlueZ`

Canonical files: [DT](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/dts/innioasis-y2.dts), [platform drivers](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2), [audio drivers](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2), [patch manifest](https://github.com/SchulzCode/Y2Linux/blob/main/kernel/patches/manifest.json). The production DTS includes the common DTS; there is not an independent second hardware design. Low-level register constants often originate in vendor/donor evidence; their named policy wrappers improve reviewability but do not independently validate electrical assumptions.

Memory intent is 0x3e000000 bytes in DT (992 MiB), minus reserved regions, kernel and other allocations—not a freely available 1 GiB heap. The historical LK gap is reserved, as is connectivity-owned high memory. HIGHMEM, a 3G/1G split, 100-Hz tick and NO_HZ_IDLE are configured; CMA is disabled. The audit does not propose changing these boundaries.

## Processes, services and persistence`BusyBox init +-- S00 runtime / S01 platform / S02 persistent data +-- S05reborn -> reborn-supervise -> reborn | (bounded rapid-crash budget; delayed restarts) +-- splash helper -> explicit KMS handoff to Reborn +-- syslogd -> bounded /data/logs/system.log +-- D-Bus system bus +-- bluetoothd +-- S41 connectivity supervisor | +-- factory provider -> root-only runtime calibration material | +-- calibration helper <-> kernel /dev/y2-calibration | +-- wpa_supplicant global/interface control | | -> wpa_cli events -> udhcpc -> IP/routes/resolver configuration | +-- bluealsad (A2DP source; SBC in inspected build) | `-- y2-bt-reconnect (preferred paired+trusted audio sink policy) `-- Dropbear: key-only root SSH bound to USB Ethernet 10.42.0.1:22 /data +-- Reborn state/library/cache/logs/diagnostics (under app data root) +-- music directory +-- network config + enable preference +-- Bluetooth bonds/preference `-- owner SSH authorization + generated host keys /run: transient sockets, locks, driver/service observations and radio logs /media/sd: explicit y2-media-managed removable music source`

Evidence: [Reborn packaging and services](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2), [connectivity service](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/board/y2/production-overlay/usr/libexec/y2/connectivity), [SSH configuration](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/board/y2/overlay/etc/default/dropbear), [media mount helper](https://github.com/SchulzCode/Y2Linux/blob/main/buildroot/board/y2/production-overlay/usr/sbin/y2-media).

Reborn starts before optional radios; workers must tolerate unavailable providers. Screen blanking is not deep suspend. `y2-suspend` independently enforces activity/radio policy; playback/radio activity leases prevent inappropriate suspend. There is no evidence that merely sleeping the UI implements a complete battery standby policy.

## Reborn state and data flow`evdev -> InputManager -> normalized controls -> ActionRouter -> Action | control socket -> enumerated commands --------------------------+ v main/UI thread: Runtime owns AppModel + Ui + graphics + service handles Ui::action(&mut AppModel, ...) -> Effect -> Runtime::effect service events -------------> AppModel::apply / Runtime handlers Ui::draw(&AppModel, ...) ----> quads -> native GLES renderer -> KMS (draw does not own hardware or perform service IO) Runtime -> scanner worker -> FFmpeg metadata -> DB command queue (32) -> SQLite worker/connection -> paged query reply Runtime -> decode worker -> bounded PCM stream -> audio worker -> AudioSink Runtime -> Wi-Fi worker -> supplicant control + rfkill/preference Runtime -> BT worker -> BlueZ/BlueALSA D-Bus + pairing agent Runtime -> diagnostics worker -> bounded tests/bundles all -> Observer -> bounded event/metric state + bounded logger worker`

The model is the UI/session authority, but not yet the sole playback authority: the decode worker owns a copied upcoming-track list. This is actual architectural drift, not a second intentional queue service. UI navigation mutates AppModel directly while returning effects; this is not a fully pure reducer architecture, and need not become one. The useful boundary is that presentation does not own device/DB/decoder handles.

Production sources: [runtime](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/main.rs), [playback](https://github.com/SchulzCode/Y2Reborn/blob/main/app/reborn/src/playback.rs), [model](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-core/src/lib.rs), [library](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-library/src/lib.rs), [UI](https://github.com/SchulzCode/Y2Reborn/blob/main/crates/reborn-ui/src/lib.rs).

## Actual audio and graphics dependencies`file -> FFmpeg demux/decode -> swresample to stereo FLTP at source rate -> avfilter volume/RG + optional EQ + always limiter (limiter negotiates packed double internally; back to FLTP) -> swresample to job output rate / packed S16 or S32 -> optional crossfade window conversions/mix -> audio worker +-- wired ALSA hw:Y2Audio -> S16-only AFE -> 32-bit I2S slots -> DAC `-- BlueALSA ALSA PCM -> bluealsad SBC -> BlueZ -> HCI -> headphones quads + bitmap font/icon atlas + 160x160 artwork -> GLES2 textures/draws -> EGL/GBM front buffer -> DRM FB/pageflip -> panel scanout`

The S32 transport representation is not proof of 32-bit precision. A 32-bit slot is not a 32-bit sample. Bluetooth does share the main processed PCM, but has additional BlueALSA encoding/transport buffering and a separately negotiated PCM rate. See [audio](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F05_AUDIO_AUDIT.md).

## Production build authority and legacy

`tools/production/build.py` orchestrates the pinned kernel inputs, Buildroot external tree, board overlays, sibling Reborn source, owner firmware inputs, image construction and package validation. Reborn's `tools/build/cross.sh` consumes the Buildroot SDK with locked/vendored Cargo dependencies. Reborn's local packaging and preview helpers are not substitutes for the system image build.

First-boot/development configurations, Y2PlayerNative manifest placeholders, old UI packs/previews and historical milestone reports are legacy/reference material. Some recovery/development tools still matter; do not delete them solely because they are old. The native Wi-Fi vendor-derived core remains production code despite its legacy shape. The separation between these categories needs better documentation, not wholesale relocation of the repositories.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
