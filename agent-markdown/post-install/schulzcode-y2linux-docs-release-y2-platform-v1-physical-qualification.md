---
title: "One Platform 1.0 integrated physical qualification campaign - Innioasis Updater"
description: "One Platform 1.0 integrated physical qualification campaign Installed Baseline01 follow-up 2026-10-04: the owner restarted during an overlong intentional USB-off C3 topol"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-release-y2-platform-v1-physical-qualification.html"
---

# One Platform 1.0 integrated physical qualification campaign - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# One Platform 1.0 integrated physical qualification campaign

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# One Platform 1.0 integrated physical qualification campaign

Installed Baseline01 follow-up (2026-10-04): the owner restarted during an overlong intentional USB-off C3 topology wait. C1/hotplug/OPPs/C2 and bounded post-C2 storage pass; C3 remains unqualified with no recorded armed/entered cycle. Recovered boot has a DRM WARNING and correctly refuses automatic C3. Owner also reports earlier post-flash USB reconnect problems. See the [physical receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-PLATFORM-V1-BASELINE-PHYSICAL.md). Do not repeat the campaign before exclusive USB/boot diagnosis resolves these gates. The host helper now waits for parking while USB remains attached; offline topology/admission waits are bounded and a 180-second userspace alarm restores USB after timeout, without weakening the kernel's real-entry backstop.

Host harness correction after Baseline01 installation (2026-10-04): CPU-idle qualification waits for Reborn's normal automatic display timeout when playback is stopped. Short Power now requests full-system sleep in that state and must not be used as a screen-blank control. The initial gesture run stopped safely before C2/C3 and retained its failure receipt. The corrected host-only helper does not change owner settings or installed firmware, and leaves timeout-disabled configurations as a bounded stop requiring owner observation. The normal short Power gesture remains the awake-from-screen-off test. Full Power wake and RTC wake remain separate staged qualification gates.

At software seal the baseline starts SOFTWARE_VALIDATED / INTEGRATED_PHYSICAL_NOT_RUN. Endurance and electrical battery benefit are NOT_RUN. The owner flashes; this software verification session accessed no device. The later installed-image receipt above controls current physical state. Source, capability and historical physical evidence have separate identities. [Baseline](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Frelease%2FY2-PLATFORM-V1-BASELINE.md).

## Installation and first smoke gate

Use the canonical owner candidate and its `MT6582_preserve_data_scatter.txt`. SP Flash Tool: Download Only; BOOTIMG and ANDROID/Y2ROOT only. USRDATA/Y2DATA, preloader, LK, NVRAM, PROTECT, calibration, factory, tables and every other row stay unselected. No data image is supplied. Retain the matching UART01 fallback.

MTP and Developer both include ECM. Connect the existing USB network and owner Wi-Fi. The retained pinned SSH config has aliases `y2` (10.42.0.1) and `y2-owner-wifi` (192.168.123.136). If DHCP has changed, correct that alias to the address observed on this same device, retaining its pinned host key and existing owner identity. A stale address must stop, never bypass host-key checking. No private key or Wi-Fi secret is included in the candidate.

Run exactly this first command after boot:`python3 /home/luca/Dokumente/Code/worktrees/platform-v1-baseline-final/Y2Linux/tools/development/qualify-platform-v1-integration.py \ --run --cpu --smoke-only \ --package /home/luca/Dokumente/Code/Y2Linux/out/y2linux-platform-v1-baseline-candidate \ --ssh-config /home/luca/Dokumente/Code/Y2Linux/out/cpu-final-fix01-physical-qualification/20260927T205514Z/ssh-config \ --host y2 --wifi-host y2-owner-wifi \ --output /home/luca/Dokumente/Code/Y2Linux/out/platform-v1-physical/baseline-01-smoke`

The coordinator holds one nonblocking shared device lease. It checks full source pair, kernel/root/build identity, same boot and taint zero, then reads dmesg, Reborn process, expected ROOT/DATA geometry, ext4 labels/UUIDs and idle boot policy. It asks seven explicit observations: wheel, display, mounted storage, basic listening, Wi-Fi, USB and battery. Play and stop one local track; leave playback stopped for CPU tests. A missing/no observation stops before any child. Only after this short gate does the guarded CPU child exercise actual C1/C2/C3, parking/timers/hotplug and all five OPPs. This invocation ends there. No MTP stress or full-system suspend is launched by `--smoke-only`.

The CPU lane includes a single guarded context-loss return, then twenty cycles and bounded normal policy; preflights and stop conditions remain. This is the existing protected CPU acceptance, not an unrestricted write loop. Preserve its before/after counters and exact installed boot identity. If static admission leaves DORMANT disabled, inspect the refusal rather than force-enable it.

## One campaign, staged acceptance

Use the same coordinator and package for subsequent attended stages, with fresh output subdirectories under `out/platform-v1-physical/`. Repeated smoke/identity gates are intentional. `--cpu` and independent pinned Wi-Fi are required before transfer/suspend actions. Child operations launch once and are never retried by an alternate SSH path. Read-only status can recover through Wi-Fi. A process exit zero requires its actual passing receipt; the overall capture remains PENDING_EVIDENCE_REVIEW until equipment and owner observations are reviewed.````

| Area | Required integrated observations | Acceptance limit / safe operation |
| --- | --- | --- |
| A. Boot / identity / recovery | Exact image pair, cold boot, service/Reborn readiness, same ROOT/DATA geometry, no BUG/Oops; preserving fallback/update procedure | Recovery image identity and preservation validated offline; physical recovery/update only with owner participation |
| B. CPU | C1/C2/C3 entries/time/restore, natural parking/demand return, timers/GPT4/GPT6/CIRQ/UART ACK, hotplug, 598/747.5/1040/1196/1300 MHz before and after wake | Existing guarded CPU helper; do not exceed OPPs, bypass battery/clock/USB guards or infer full suspend from C3 |
| C. Storage | eMMC/SD negotiated mode/rate, runtime PM, owned fsynced scratch hashes, ext4 counters; FAT/exFAT only on existing owner media; absent/reinsert/different-card identity | No formatting, repartitioning or clock forcing; different-card/eject waits for owner, finished scanner/player and no active transfer |
| D. USB | Actual desktop MTP enumeration, large and many small owned files, create/rename/delete, reconnect/disconnect and SHA256 readback; SD root release | --usb sftp --volumes internal sd provides ECM integrity only. MTP uses --usb mtp --volumes internal --mtp-uri <actual Internal Storage URI>; one matching volume per real URI. Never export raw blocks or system roots |
| E. Connectivity | Wi-Fi Online/route/DNS freshness, AP loss/reconnect, screen-off; real Bluetooth headset, observed negotiated codec/PCM generation, reconnect and Wi-Fi/BT coexistence during transfer/playback | No headset or AP action means NOT_RUN. Preference/compiled codec is never negotiated transport evidence |
| F. Audio | Supported format decode/seek/pause/stop, wired S16 stereo 44.1/48 kHz listening and XRUNs; actual BT PCM/codec | S24/S32 conversion is software support. Wider native modes remain refused until AFE/I2S bit/clock evidence admits them. S32 container does not prove 32 meaningful bits |
| G. Reborn / display / controls | Actual performance, static frame counts, off/wake GPU/KMS PM, artwork replacement, metadata, DB/no-op scans, media/USB/sleep races; counted detents/buttons, boot/splash and shutdown | Synthetic latency is separate from physical IRQ/photon timing. Inspect slow cold layout/startup, render order/blend and explicit source rejection. One frame owner; no normal capture/readback |
| H. Power / battery | C1/C2/C3 idle, voltage/SOC and elapsed windows, charging status/refusal, warnings/shutdown, representative screen-off idle | Record actual sensor availability. Never infer electrical savings or runtime from C-state residency; use owner profile and safe charge levels |
| I. Full system suspend | Separate staged freezer/devices/platform/processors/core; one Power wake; independently one RTC wake; same-boot COMPLETE/EXIT and full restoration | Existing Baseline02 RTC FAIL remains open. No loops or overnight full suspend. Product deep sleep stays refused until qualified evidence |
| J. Recovery / update / diagnostics | Preserving workflow, UART01 fallback identity, private-state-safe diagnostic archive and source/notices inventory | Public firmware/codec rights and collector gaps remain a separate release axis; no protected-partition writes |

The coordinator's retained machine lane letters predate this table (its C is full suspend, D combines storage/USB, H is display/input and I is power). Use named flags and these acceptance areas when reviewing evidence, rather than assuming a successful automated lane closes every requirement.

## Suspend: Power and RTC are separate tests

First run the coordinator with `--cpu --suspend-stage inspect`; review blockers and current battery/charging state. Then, in separate attended invocations, qualify each of `freezer`, `devices`, `platform`, `processors`, `core`. Reuse exact installed-pair and boot gates. Staged PM success and awake RTC IRQ delivery do not prove full suspend.

After staged acceptance, one coordinator invocation with `--cpu`, independent Wi-Fi, `--suspend-stage none --wake-source power` tests Power. Press Power during the announced suspended window before the 30-second RTC backstop. If the alarm wakes the device instead, Power remains FAIL/NOT_PROVEN. A separate invocation with `--suspend-stage none --wake-source rtc` tests the armed 30-second RTC. Leave Power untouched for that trial. The child requires the selected actual PMIC IRQ delta, same boot, full PCM 596/reset 0x59325253, COMPLETE/EXIT without error, restored state/counters and an acknowledged Reborn prepare/restore cycle. Clear alarm/pm_test afterward and verify kernel, audio, display, controls, USB, storage and radios. A watchdog reboot is a failure even if all mounts recover.

Baseline02's single 12-second RTC trial watchdog-rebooted while retained journal reported DEVICES_RESUMING. Wake 0x20 and a CS43131 1-0030 resume entry without leave narrow diagnosis; the stalled internal instruction is UNKNOWN. The new rollback repair, checked restores and substep telemetry are not a demonstrated fix for that physical stall. Power success must never close RTC.

## Battery / standby observation

After attended smoke/CPU and charging safety acceptance, prepare screen-off, no playback, Wi-Fi and Bluetooth off. Before switching off the observation transport, save exact identity/boot, monotonic time, voltage/SOC/temperature, charge state, per-state idle entries/time and restore failures, `/proc/interrupts` and available wakeup counters in the campaign's private H directory. Record the owner conditions, charger absent/present and actual current-sensor availability. Disconnect USB, leave idle for 30–60 minutes, reconnect and save the same fields. Label transport/display transitions as measurement overhead; radio-off windows cannot be continuously observed over Wi-Fi. Compare deltas and elapsed time on the same boot. A missing current sensor stays unavailable.

Optionally repeat with radios idle, recording associated AP/peer condition privately. The existing `tools/host/qualify.py capture` passive collector can capture timed snapshots, but its SSH activity is a measurement workload and it does not create the owner condition or prove energy benefit. Review its default offline plan/profile before use. An owner-run overnight radio-off idle window is appropriate only after attended safety acceptance; retain beginning/end voltage/SOC/duration/idle/IRQ data and all anomalies. No unattended full-suspend or low-battery exhaustion test is prepared.

## Stop and restoration rules

Stop on image mismatch, unexpected reboot, taint, BUG/Oops, failed/missing receipt, restore failure, timer/clock/UART/PWRAP/DVFS error, thermal/battery warning, storage error/hash mismatch, stalled mount or unavailable independent Wi-Fi. Preserve the failure directory. Do not replay a mutating command after a transport timeout. Leave no alarm/pm_test/temporary override; require restored normal topology/OPP, stopped scratch activity and normal player/storage/radio state. If restoration cannot be established, stop for owner recovery with the matching fallback. No hardware failure is waived by a software test.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
