---
title: "CONNECTIVITY-10: complete Wi-Fi regulatory TX power requests - Innioasis Updater"
description: "CONNECTIVITY-10: complete Wi-Fi regulatory TX power requests <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate ide"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m5-connectivity10-corrections.html"
---

# CONNECTIVITY-10: complete Wi-Fi regulatory TX power requests - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# CONNECTIVITY-10: complete Wi-Fi regulatory TX power requests

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# CONNECTIVITY-10: complete Wi-Fi regulatory TX power requests > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

The own Y2 trace places the remaining -09 Wi-Fi failure after firmware ready, successful RF/baseband capability queries and the interface registration path. The regulatory notifier sends domain `0x13` and TX power `0x38` commands; TX credits return, but the power-setting OID times out and triggers recovery. [Physical evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-17-m5-wifi%2FREADME.md).

`wlanoidSetTxPower` marks `0x38` as an OID set without a firmware response and provides no done callback. `wlanProcessCommandQueue` completes successful no-response commands through that callback, then frees them. Consequently the waiting `kalIoctl` never receives success, although transmission succeeded.

Attach existing `nicCmdEventSetCommon` and `nicOidCmdTimeoutCommon` callbacks only to this producer. This repairs the driver completion contract; it adds no silicon workaround and requests no unsupported firmware acknowledgement. The payload, cfg80211 channel/power policy, command queue, transport and error checks stay unchanged. Two small lifecycle logs expose interface registration and regulatory failure without enabling the verbose legacy debug masks.

The new regression executes the actual producer, queue consumer, queue macros and callbacks, reproduces the missing completion, and checks successful TX, TX error, credit starvation/retry, timeout and non-OID behavior. Replaying the unmodified -09 producer fails its successful-completion assertion. All 16 targeted Wi-Fi/connectivity checks pass against the final emitted -10 artifacts.

The owner-installed CONNECTIVITY-10 BOOTIMG now verifies stable wlan0/cfg80211, successful scans, runtime restart and BlueZ power-on while Wi-Fi is active. Core errors/recoveries remain 0 and kernel taint is 0; no runtime correction or diagnostic module is needed. [Physical -10 result](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-17-m5-connectivity10%2FREADME.md). CONNECTIVITY-07 root/data and the verified -09 BOOTIMG fallback are retained. No network is configured, so association/DHCP/data traffic remain untested. M5 qualification remains open; both saved radio preferences stay off.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
