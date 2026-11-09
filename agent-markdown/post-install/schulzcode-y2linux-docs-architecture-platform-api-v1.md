---
title: "Platform API v1 - Innioasis Updater"
description: "Platform API v1 <!-- knowledge-base-scope: source-contract; baseline02-sync 2026-10-03 -- Baseline02 additive CPU-idle interface API v1 remains unchanged; clients ignore"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-architecture-platform-api-v1.html"
---

# Platform API v1 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Platform API v1

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Platform API v1

## Baseline02 additive CPU-idle interface

API v1 remains unchanged; clients ignore unknown added keys. `y2-platform cpu-idle-policy start|stop` selects the existing qualified CPU0 C3 controls. Boot init calls start once; stop quarantines C3 for the current boot and prevents another start from overriding the owner. It does not change C1/C2, force topology/frequency or bypass entry guards.

`y2-platform status cpu` adds `idle_completion.C3.boot_policy`, read from `/run/y2/cpu-idle-policy.json`, schema `org.y2linux.cpu-idle-policy/v1`. It reports boot ID, policy, Enabled / Skipped / Failed / Disabled, reasons, budget/state readbacks and rollback errors when present. Absent evidence is not successful activation. Capabilities may enable qualified DORMANT policy while current-image physical qualification remains false: preceding UART01 proves the architecture, Baseline02 automatic cold boot is NOT_RUN.

The qualification harness explicitly arms the existing RGU backstop for bounded C3 trials; ordinary status collection does not arm it. Full system suspend is a separate gate. [Power ownership](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fplatform-power-v1.md), [Baseline02 receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md), [UART01 hardware](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md). > **Source-contract scope.** This page describes software ownership and > interface behavior. See [current state](../CURRENT_PLATFORM_STATE.md) for the exact latest image > and physical limits; implemented or enabled does not mean qualified. 

The machine interface is `y2-status --json` (or `y2-platform status`), `y2-health --json`, and `y2-platform capabilities`. JSON is the default; the `--json` flag is accepted for explicit clients. Schema names carry `/v1`. Unknown added keys must be ignored. Missing measurements are `null`, empty collections mean no interfaces observed, and neither implies a measured zero. `y2-status cpu|memory|thermal|power|storage|wifi|bluetooth|system|audio|usb|readiness` selects one section while retaining record identity. Rescue keeps a separate minimal shell status tool, usable without Y2ROOT or Python.

Each record includes UTC wall timestamp, monotonic nanoseconds, boot ID, Linux commit, Reborn commit when packaged, kernel, rootfs release, build ID, workload, parameters, units, result, failure and evidence level. Wall time is not trusted merely because it is formatted as UTC. Source identity comes from the installed build receipt. Observation does not promote a release's evidence level.

CPU times, frequency and idle residency, IRQs, context switches, VM and block counters are cumulative. `--interval 0.1` through `10` samples CPU deltas; without an interval utilization is null. Guests are not double-counted. Counter reversal or a newly online core has no utilization sample. PSS is opt-in: `y2-status memory --pid PID --pss`. KiB, kHz, microseconds, microvolts, microamps and millicelsius are identified in the response. Charge limits are configured values, never inferred net battery current, SOC or pack temperature.

Storage reports one exact mount, controller, UUID, boot-scoped mount generation and filesystem space. A surviving mountpoint is not a source. Missing block identity, stacked mounts, a mismatched internal UUID, read-only mounts and missing statvfs are distinct errors. Clients must recheck UUID and generation before destructive reconciliation. Free-space policy is Normal / LowSpace / CriticalSpace / ReadOnlyRisk / Failed / Unavailable. Low is below max(96 MiB, 10%); critical is below max(32 MiB, 5%) or no free inodes. These are software capacity reserves, not qualified capacity/performance claims. This interface does not automatically delete any files.

Readiness is Ready / Starting / Degraded / Failed / Unavailable. Wi-Fi's detailed state separately reports Off / Starting / Scanning / Associating / Authenticated / AcquiringIP / Online / Failed. Online requires authentication, an address, default route and a successful DNS probe younger than 120 seconds, on the same boot, address and association. Configured DNS servers and a live PID cannot establish Online. Connection owners are wpa_supplicant (Wi-Fi association) and `y2-radiod` (Bluetooth and both radios' power, [radio-daemon.md](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Farchitecture%2Fradio-daemon.md)). Unavailable Bluetooth observation remains explicit until the D-Bus observer is installed; codec requests must never be interpreted as negotiated output.

Capabilities distinguish implemented, enabled and qualified. Enabled radio preferences are resolved at query time. Physical evidence for an older narrow profile is named separately; current image qualification is false until the owner supplies matching evidence. Driver support does not enable USB host, deeper idle, optional codecs, high-resolution audio, low-battery thresholds or automatic BOOTIMG updates.

`y2-health` checks identity, space, filesystem error counters, nodes, sensors, USB and service readiness. It returns OK / DEGRADED / FAILED / UNAVAILABLE with per-check reasons; exit 1 means a failed check. `--full` adds bounded ALSA and KMS capability queries; it does not play audio, change display modes, connect radios or invoke physical actions. Additional explicit scratch tests use the benchmark contract. Interface presence is a narrow observation, not physical qualification.

Boot stages retain initramfs, discovery, preflight, fsck, mounts and switch_root timing in `/run/y2/boot-stages.jsonl`. A durable, bounded eight-boot journal in `/data/system/platform/boot.json` retains identity, count, last stage, previous boot ID and orderly-shutdown marker. Three unclean predecessors recommend recovery; no automatic reboot follows. An unclean record does not distinguish power loss, panic, reset or removal of power. Watchdog sysfs and pstore inventory are observations only; no AP watchdog is armed and no RAM region is reserved. Failures before validated writable data cannot be promised persistent retention.

The interpreter uses only the standard library; no pip or network packages are installed. Files are size-bounded, PID requests capped at 32, and subprocesses have output caps and deadlines. A kernel task stuck in uninterruptible I/O cannot be made time-bounded by a userspace timeout. Full status is an on-demand tool, not a high-frequency polling daemon; benchmark records include collection cost.

`--reborn --pss` observes the current service PID/start-time and bounded Reborn metrics; collection follows restarts as separate memory series. Boot evidence is captured before the current logger starts. Status contains only previous-log metadata/hashes, while `y2-platform boot-evidence` is private owner retrieval. Kernel taint and actual CONSYS status are observations; no kernel warning count or packet-loss number is synthesized from log text or application XRUNs.

The [owner qualification plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-OWNER-QUALIFICATION.md) uses `tools/host/qualify.py`: local plan by default, explicit readonly USB collection, exact source-pair matching, bounded gaps and no automatic hardware actions. Capture completion and qualification acceptance are separate states.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
