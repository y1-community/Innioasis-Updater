---
title: "Platform power contract v1 - Innioasis Updater"
description: "Platform power contract v1 <!-- knowledge-base-scope: source-contract; baseline02-sync 2026-10-03 -- Baseline02 runtime idle and system suspend Baseline02 enables qualifi"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-architecture-platform-power-v1.html"
---

# Platform power contract v1 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Platform power contract v1

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Platform power contract v1

## Baseline02 runtime idle and system suspend

Baseline02 enables qualified CPU0 C3 automatically after boot through `S05y2-cpu-idle`. The kernel initially registers C3 disabled with budget 0. The once-per-boot service checks identity, taint and static SPM/CIRQ/timer/context foundations, sets budget -1, enables CPU0 state2 and reads both controls back. Failures roll back; CPU1–3 C3 remains disabled. Dynamic topology, frequency, screen/workload/radio/USB, clock/domain, future-deadline, UART ACK and restore fault guards remain intact. The service does not force parking or gate UART1.

`y2-platform cpu-idle-policy stop` disables C3 for the current boot and prevents another start from overriding that choice. Recovery boot options `y2.deep_idle=off` and `y2.cpu_safe=1` retain the safe fallback. Runtime C3 is separate from full system suspend.

`y2-platform status cpu` publishes `idle_completion.C3.boot_policy`, sourced from `/run/y2/cpu-idle-policy.json` (schema `org.y2linux.cpu-idle-policy/v1`). It carries boot ID, state, reasons and control readbacks; failed activation includes rollback errors. States are Enabled / Skipped / Failed / Disabled. Missing/stale evidence is not successful activation. A start runs once per boot, respects explicit owner controls and never overrides a later stop; this service adds no polling loop.

C1/C2/C3 are physically qualified on preceding UART01. Baseline02's new image and automatic cold boot remain NOT_RUN. Full system suspend is still disabled for ordinary use pending same-boot Power/RTC acceptance. Screen blanking allows runtime idle; it does not invoke full system suspend. See [Baseline02](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md), [UART01 hardware](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) and [current state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md).

## Shutdown and battery ownership

Normal `/sbin/poweroff`, `/sbin/reboot`, Reborn user requests and future update reboots enter `y2-platform shutdown poweroff|reboot --reason user|service|update`. A private Unix socket uses SO_PEERCRED. Only root may request a transition; only the recorded Reborn PID/start-time can acknowledge the current request UUID. There is one monotonic deadline, never extended by duplicate requests.

`/run/y2/shutdown.json` publishes schema, current boot ID, request ID, intent, reason, requested time, deadline, client identity and acknowledgement. Reborn checks every 250 ms, stops audio, checkpoints session, stops scanning, checkpoints WAL and closes the single database connection. Ready means those steps completed; a failed step reports Failed. A missing/failed acknowledgement cannot block the platform beyond the ten-second grace. The platform stops services (two bounded three-second calls), records the journal (one second per attempt), syncs (five seconds), then requests BusyBox init's standard shutdown (two seconds). No forced reboot syscall or charger/PMIC programming is introduced. Kernel uninterruptible I/O or final hardware poweroff cannot be guaranteed by a userspace deadline.

The dedicated supervised policy process runs independently of Reborn. Five short exits exhaust its restart budget. Its once-per-second heartbeat becomes Unavailable after five seconds; the status API never retains a stale Normal. Restart during the same boot resumes a pending intent at its original deadline; no intent is replayed across boots. Journal orderly_shutdown means orderly software preparation reached its final record, not observed hardware power loss.

Battery observation uses BAT0 voltage_now/present. USB presence is not assumed to supply positive net battery current. The **current shipped schema-2 policy is enabled but provisional**: critical/low/recover values are 3.4/3.5/3.6 V, five critical samples and ten-second grace. Its source text explicitly identifies a conservative stock-boundary floor, not a measured discharge curve. Provisional voltage-derived SOC is not calibrated pack current/capacity. A private `/data/system/platform/power-policy.json` can override the shipped policy; the loader accepts schema 1 or 2 with ordered voltage thresholds, critical_samples (1–60), grace_seconds (3–30) and an evidence reference/source. Schema 2 also validates ordered warning/critical/shutdown SOC values; SOC-triggered shutdown requires hardware or calibrated-estimate confidence. An evidence string is not software certification. Missing/invalid sensors report Unavailable. Debounce/ hysteresis implement Normal/Low/Critical/ShutdownPending; no charger limit changes. [Power evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fhardware-final-power-evidence.md) explains missing pack current, pack temperature and measured reserve qualification.

Owner qualification must establish pack identity, safe observation conditions, voltage sag under representative peak load, warning and shutdown reserve, sampling/debounce and recovery hysteresis. Test app acknowledgement, hung app, blocked database and sync failure first with synthetic host fixtures. Only then, under the separate owner-controlled power session, qualify selected thresholds, poweroff/reboot and the behavior of USB-connected low voltage. Do not discharge an unknown pack to infer a limit.

Suspend remains disabled for ordinary operation. See the explicit [hardware gates and existing scoped activity lease](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fplatform-v1-hardware-gates.md). The owner qualification helper requires `y2-suspend --owner-qualify`; this flag does not confer qualification. Screen blanking never invokes it.

## Historical physical note — 2026-09-28

2026-09-28 status: This page describes software behavior, with current hardware limits in [platform state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2FCURRENT_PLATFORM_STATE.md). Fix01's first devices-stage suspend request lost recovery; charger refusal was not truly exercised because BAT0 was Not charging. Full RTC/Power same-boot wake is NOT_TESTED. Do not read the contract below as a passed suspend qualification.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
