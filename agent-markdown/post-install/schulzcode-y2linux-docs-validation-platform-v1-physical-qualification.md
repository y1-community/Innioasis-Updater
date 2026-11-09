---
title: "Platform v1 physical qualification - Innioasis Updater"
description: "Platform v1 physical qualification <!-- knowledge-base-scope: scoped-validation-record -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-platform-v1-physical-qualification.html"
---

# Platform v1 physical qualification - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Platform v1 physical qualification

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Platform v1 physical qualification > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

## Owner-connected Wi-Fi check — 2026-09-25

**PARTIAL: Wi-Fi association, DHCP, default route, router and Internet-IP reachability PASS; DNS FAIL.** The owner connected to their router and explicitly requested this narrow check. It does not waive the retained Session A warning gate or complete Session C. Current coverage is A FAIL, B NOT_TESTED, C PARTIAL with the DNS failure below, D NOT_TESTED. No configuration, credentials, service, firmware or hardware policy was changed, and no throughput/reconnect test ran.

Installed identity is unchanged: Linux `814c2f3470566021c1a9c43037fd868de8b2df9c`, Reborn `155608393f6acfc6657f2f2e23cd07d0533479c6`, build `Y2LINUX-PLATFORM-V1-TELEMETRY-01`, rootfs `2025.02.18-platform-v1.2`, retained kernel `6.18.0-y2linux-platform-v1-candidate-01`. Boot ID remains `3194fa9d-2dee-4105-86f0-4021580bf8d0`. Full versions match before and after. Expected image hashes are the Telemetry 01 hashes below; no whole-image readback is claimed. Host timestamps, complete commands and raw results are private in `evidence-private/platform-v1-physical-qualification/20260925T154016Z-owner-wifi-check/`. The owner reports connecting to the router; no other manual observation was requested. The automatic checks below have no separate manual observation.``````````````````````````````````````````````````````

| Test / command | Measured result | Status | Evidence basename |
| --- | --- | --- | --- |
| y2-status system --json; capabilities; full health; dmesg -r before/after | Exact same candidate/boot; complete mandatory captures; remaining readiness/warning limits retained | PARTIAL | 01–04, 13–16, 20–23 receipts |
| wpa_cli -i wlan0 status | COMPLETED, WPA2-PSK/CCMP, 2422 MHz, 20 MHz channel | PASS (association only) | 06-wpa-status |
| ip -j -4 addr show dev wlan0; DHCP record | Address 192.168.123.136; matching lease, no DHCP error, 86400-second lease | PASS | 07-address, 09-dhcp-dns |
| ip -j -4 route show | Default via 192.168.123.1 on wlan0, metric 100 | PASS | 08-route |
| y2-platform network-check --peer 192.168.123.1 --seconds 5 | Refused with wifi_not_online; no throughput requested | FAIL (platform admission) | 10-platform-network-check |
| ping -I wlan0 -c 5 -W 2 192.168.123.1 | 5/5 replies, sample loss 0%; RTT min/avg/max 1.332/1.532/1.776 ms | PASS (bounded router reachability) | 11-router-ping |
| Isolated Python socket.getaddrinfo("pool.ntp.org", None, AF_INET) using configured resolver | EAI_AGAIN / temporary name-resolution failure after 2.026 s | FAIL | 12-dns-query |
| Same resolver query for example.com | EAI_AGAIN after 2.028 s | FAIL | 18-dns-second-host |
| ping -I wlan0 -c 3 -W 2 1.1.1.1 | 3/3 replies, sample loss 0%; RTT min/avg/max 11.528/11.846/12.275 ms | PASS (bounded Internet-IP reachability) | 19-internet-ip-ping |

DHCP supplied DNS server `192.168.123.1`; resolv.conf names that server. The platform's DNS probe also reports failure. These checks demonstrate working Wi-Fi/IP routing and a resolver-path failure; they do not isolate whether the cause is the router DNS service, DNS packet handling or resolver behavior on Y2. No alternate DNS server was configured. Native supplicant status succeeds while the platform observer still reports Starting/supplicant_unavailable, retaining the separate intermittent query/readiness problem. Online is not accepted without DNS. No speed, sustained loss, reconnect, TLS or endurance claim follows from these eight ping replies. The next focused diagnosis is the DNS path and readiness reporting; no new image has yet been shown necessary by this check.

Before/after kernel buffers each contain 67 priority 0–4 entries: the previous 14 plus 53 display log rate-limit notices accumulated before this connection check. No new critical Oops/panic/WARN-stack/ext4-I/O signature was found during the check. Existing warning and broader physical-acceptance gates remain open.

## Latest attempt: installed Telemetry 01 — 2026-09-25

Read-only follow-up on the same boot: `wpa_cli ping` returns PONG, status returns DISCONNECTED, and list_networks has zero network rows. No connection has been configured, so not_authenticated alone is not a demonstrated Wi-Fi defect. The three direct SSH queries took 2.08–2.12 s, while a subsequent on-device comparison using the installed command runner returned successfully in 0.118 s at a 1-second deadline and 0.012 s at 4 seconds. The observer's 1-second query deadline can miss slower responses, but this comparison did not reproduce a timeout or establish its cause. Closing health remains DEGRADED with supplicant_unavailable. No credentials, network selection or restart occurred.

Timer inspection shows four dummy per-CPU clockevents backed by the real `mtk-clkevt` periodic broadcast timer, broadcast mask `f`, 10,000,000 ns timer resolution, highres=0 and nohz=0. The retained candidate configuration has CONFIG_HZ=100 and CONFIG_HIGH_RES_TIMERS unset. This narrows the warning to the current periodic-timer limitation; it does not mean the Y2 has no working timer. Enabling high-resolution/tickless behavior or strict kernel RWX is a separate kernel validation scope. The original warning stop rule remains unchanged; continuing with named limitations requires explicit owner disposition, and software changes require a separately authorized repair pass.

Follow-up evidence: `evidence-private/platform-v1-physical-qualification/20260925T152936Z-readonly-triage/`. Before/after status/capabilities/health/dmesg and per-command receipts are retained. The `/proc/488/stack` read was unavailable; the later wchan was do_select. A single earlier D-state process snapshot does not establish a persistent hang. No new Session A workload or Session C test was activated by this diagnosis.

**Telemetry repairs PASS in this observed scope. Session A FAIL at the retained kernel-warning gate; B/C/D NOT_TESTED. No physical or endurance promotion.** The owner installed the corrective image, then authorized continuation of the original qualification. No source, firmware, service, radio or hardware-policy change was made by this retest. No reboot, rescue transition or workload started.

The exact installed metadata and nine file hashes match `out/y2linux-platform-v1-telemetry-01-candidate/`. New boot ID: `3194fa9d-2dee-4105-86f0-4021580bf8d0`. Identity:``````````````````````

| Field | Observed value |
| --- | --- |
| Y2Linux source | 814c2f3470566021c1a9c43037fd868de8b2df9c |
| Build / release | Y2LINUX-PLATFORM-V1-TELEMETRY-01 / 1.0.0-candidate.2 |
| Rootfs / Buildroot source marker | 2025.02.18-platform-v1.2 / VERSION=-g814c2f3 |
| Kernel | 6.18.0-y2linux-platform-v1-candidate-01 |
| Retained kernel/base source | d04b95aaff713edf943042d97a4c6134ca19fc24 |
| Reborn source / version | 155608393f6acfc6657f2f2e23cd07d0533479c6 / 0.1.0-ui-v1-candidate.1 |
| Expected local root SHA256 | 4a8e520946ad1aaa00df46e9f302463341e4408bba063f43728b8cb8f68bb092 |
| Expected unchanged BOOTIMG SHA256 | f7b4a950a0504a411ad72db0aac9398f04dc1ccabd6a6a0a3a7fdab198ca2622 |

Hash comparison covers the five replacement files and four Reborn ELFs; it is not whole installed-image readback. `uname -a` is the exact same kernel string recorded in the earlier attempt below. The saved owner-authorized host pin and existing login key still work; the prior independent-console-verification limitation remains. Host UTC below is authoritative: device wall time is still anchored to the September 23 build floor, NTP is not established and TLS readiness is false. RTC reads August 2022; no retention claim is made.

Private evidence (mode 0700, Git ignored): `evidence-private/platform-v1-physical-qualification/20260925T151959Z-telemetry01/`. Every command has UTC/arguments/exit/duration/raw-output receipts. The test register supplies full source/image identity, boot ID, observation, status and limits for every attempted test and remaining gate. The original run's sealed evidence is preserved separately. All rows below use the identity/boot above.``````````````````````````````````````````````````````````

| Host UTC | Command / observation | Measured result | Status | Evidence basename |
| --- | --- | --- | --- | --- |
| 15:20:36 | y2-status system --json | Valid exact-identity JSON; exit 0; 2.692 s including SSH | PASS | 01-system |
| 15:20:38 | y2-platform capabilities | Exit 0; 0.755 s; declarations captured | PASS (query) | 02-capabilities |
| 15:20:39 | y2-health --full --json | Valid JSON; 3.525 s; exit 1, FAILED for Wi-Fi not_authenticated; no exception | FAIL (readiness), PASS (dispatch repair) | 03-health-full |
| 15:20:43 | uname -a, boot ID, versions, build ID and os-release reads | Full metadata matches candidate; new boot ID | PASS | 04-uname through 07-release |
| 15:20:43 | dmesg -r | 14 kernel facility priority 0–4 entries; stop rule applies | FAIL (warning gate) | 08-dmesg |
| Owner reply on this boot | Look at screen and assess warmth; no control action | “Main menu visible; normal warmth” | PARTIAL | owner-observations.json |
| 15:22:27 | y2-platform collect --seconds 1 --interval 1 --warmup 0 --reborn --pss --workload session-a-stop-baseline | One passive sample; actual collector duration 2.852 s, SSH total 3.687 s; values below | PARTIAL | 09-stop-collection |
| 15:22:31 | sha256sum of five replacement files and four Reborn ELFs | All nine match; 4.595 s | PASS | 10-installed-hashes, installed-hash-comparison.json |
| 15:22:35 | y2-status system --json | Valid same-boot JSON; exit 0; 3.550 s | PASS | 11-post-system |
| 15:22:39 | y2-platform capabilities | Exit 0; 0.763 s | PASS (query) | 12-post-capabilities |
| 15:22:39 | y2-health --full --json | Valid JSON; exit 0; 3.576 s; DEGRADED, Wi-Fi supplicant_unavailable | PARTIAL | 13-post-health-full |
| 15:22:43 | dmesg -r | Same 14 kernel entries; no new warning class | FAIL (warning gate) | 14-post-dmesg, kernel-review.json |
| 15:22:43 | Boot/uptime/taint/normal_boot, Reborn proc identity, process/wakeup-source table, ext4 counters | Same boot, taint 0, normal_boot 1, both ext4 error counters 0; no leftover status/wakeup reader | PASS (narrow context) | 15-final-context |

The wakeup counter correctly reports null / `command_timeout` while BAT0 reports Charging and the charger wakeup source is active. The final process table contains no lingering counter reader or `pm_get_wakeup_count` wait. This proves the repaired observation path on this boot, not long-run collection. Health now reports actual readiness, including failures, instead of crashing. The Wi-Fi reason changes from `not_authenticated` to `supplicant_unavailable`; no service restart, password entry, AP test or radio action was performed. Its cause and end-to-end connectivity remain unqualified.

Both root and data are Ready, separate read-write ext4 mounts with the expected UUIDs and `11230000.mmc` controller. On this boot they enumerate as `/dev/mmcblk0p5` and `/dev/mmcblk0p7`; names changed with enumeration, controller and UUID identity did not. Boot fsck reports both clean. An SD device enumerates but `/media/sd` is unavailable; no mount/removal/benchmark was attempted.

Normal-boot markers show switch_root 9.740 s, first frame 62.785 s, and application_ready 70.058 s. Reborn PID 363, start ticks 2824 and `/usr/bin/reborn` match the first-frame record. Previous boot `083d4abb-a447-4ac6-a063-e8898c150bca` is recorded as orderly shutdown_complete, with previous-log tail metadata retained; this is not one of the three requested controlled reboot trials. Library readiness, rescue entry/return and all input/playback checks remain open.

Snapshot: CPU 48.800°C, PMIC 45.713°C; battery 4,024,072 µV. MemTotal 952,304 KiB, MemAvailable 865,868, LOWMEM 723,952, HIGHMEM 228,352, cache 56,684, slab 11,004. Reborn RSS 23,532 KiB, 16 threads; requested PSS remains null, not zero. Frequency time-in-state counters are 20,643 / 164 / 7,214 USER_HZ ticks at 598 / 747.5 / 1040 MHz. Per-core WFI cumulative time is approximately 249.569 / 249.092 / 256.292 / 250.001 seconds. These are mixed-boot counters, not idle/playback/scan workload utilization, power savings or endurance results. No governor/OPP/voltage change occurred. ALSA hw_params is `closed`; no sound or XRUN-under-playback result is inferred.

The 14 kernel entries repeat the previously reviewed timer/cache, LED-node, hardening, stock p8 clipping, regulator get_mode, Bluetooth feature quirk, Wi-Fi logging and rate-limit classes. Another 31 warning-priority lines have non-kernel facility (for example raw PRI 12) and are counted separately. No new Oops/panic/WARN-stack/ext4/I/O signature was found; taint remains zero. None of these observations waives the owner's kernel-warning stop rule. See the [source-backed warning review](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-TELEMETRY-01.md%23warning-review&anchor=warning-review).

### Latest requested result ledger

| Requested result | Current result |
| --- | --- |
| 1–2: Exact Linux and Reborn identities | Full identities above; metadata and nine file hashes match |
| 3–6: Sessions A / B / C / D | FAIL at warning gate / NOT_TESTED / NOT_TESTED / NOT_TESTED |
| 7–9: eMMC speeds, SD speeds, fsync p50/p95/p99 | NOT_TESTED |
| 10–11: SQLite 1k/10k/20k and Reborn 20k navigation | NOT_TESTED at each size |
| 12: Idle/playback/scan CPU | NOT_TESTED for each workload |
| 13: Frequency residency | PARTIAL: cumulative counters above, no workload interval |
| 14: Memory/RSS/PSS | PARTIAL: system/RSS/thread snapshot above; PSS unavailable |
| 15: CPU/PMIC temperatures | PARTIAL: 48.800°C / 45.713°C and normal-warmth report; no load/accuracy qualification |
| 16–20: Wi-Fi association, DHCP, DNS, throughput, reconnect | NOT_TESTED as controlled Session C tests; baseline Wi-Fi readiness failed/degraded |
| 21–26: Bluetooth pair/trust, SBC PCM/sound, reconnect, AVRCP, coexistence | NOT_TESTED; radio reported off |
| 27: USB/SSH/SFTP | PARTIAL: configured high-speed peripheral, saved-pin owner-key SSH and SFTP/USB-only readiness declaration; SFTP transaction and Wi-Fi/password exclusion probes NOT_TESTED |
| 28: Kernel/storage/audio warnings | 14 retained kernel messages; clean ext4 counters; no audio playback test |
| 29: Software fixes | Both telemetry repairs observed working; warning disposition and Wi-Fi readiness still need investigation; PSS remains unavailable |
| 30: Physical gates | Controlled reboots/rescue, library/input/audio, USB negative probes, B–D, endurance; E/F/G remain separately gated |
| 31: Acceptable as Platform v1 Core? | Not yet; Session A warning gate and incomplete required tests |
| 32: Recommended next work | Resolve the remaining warning/readiness gates before resuming Session A; no automatic rebuild, flash or policy change |

## Earlier attempt: original UI candidate

2026-09-25 UTC. Owner-supervised qualification of the already-installed `out/y2linux-reborn-ui-v1-candidate/`, clarified by the owner after the initial identity check found a different Reborn from the original plain Platform v1 package. The [owner test plan](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-OWNER-QUALIFICATION.md) and explicit no-flash/no-build/no-production-change limits remain authoritative.

Session A: FAIL; stopped at baseline. Sessions B/C/D: NOT_TESTED. Identity metadata and installed application hashes match the owner-clarified package. Two mandatory telemetry commands fail, and kernel warning/error-priority messages trigger the owner's Session A stop rule. No physical or endurance acceptance is declared. Sessions E/F/G and unattended long runs remain unstarted and separately gated. Recommended next step: corrective software work and warning review, then repeat Session A under the resulting exact identity.

Subsequent owner-authorized [telemetry repair](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-TELEMETRY-01.md) is complete at host/ARM/image scope. Its new candidate has not been installed. This physical record describes the original image and remains unchanged in result; software checks do not supersede its failures or missing physical tests.

## Identity

Authenticated identity read: 2026-09-25 14:23:49 UTC. Boot ID: `083d4abb-a447-4ac6-a063-e8898c150bca`.````````````````````

| Field | Observed |
| --- | --- |
| Kernel | 6.18.0-y2linux-platform-v1-candidate-01 |
| Y2Linux release/build | 1.0.0-candidate.1 / Y2LINUX-PLATFORM-V1-CANDIDATE-01 |
| Y2Linux source | d04b95aaff713edf943042d97a4c6134ca19fc24 |
| Reborn source | 155608393f6acfc6657f2f2e23cd07d0533479c6 |
| Reborn version/package | 0.1.0-ui-v1-candidate.1 / Y2LINUX-REBORN-UI-V1-CANDIDATE-01 |
| Rootfs | 2025.02.18-platform-v1.1; Buildroot 2025.02.18 |
| UI review metadata | 4fe236feaa986dccd014758a860554d18b94fbab |

All installed versions JSON fields equal the clarified package metadata. The original target expected Reborn `6c8aa128550ec80addd08ef3145e9d5a846ddf2e` / `0.1.0`; qualification stopped at that mismatch until the owner supplied the actual package path. Metadata matching is not installed-image readback.

Local integrity: plain Platform v1 package 1,112/1,112 checksums; clarified UI candidate 133/133. UI root SHA-256: `edcecfaae26b8102c071000b5d2e9e5f84626ad08e3ff5818b050174f301a044`. Required Platform v1 BOOTIMG SHA-256: `f7b4a950a0504a411ad72db0aac9398f04dc1ccabd6a6a0a3a7fdab198ca2622`. These are expected local image hashes, not measured whole installed images. All four installed application ELF SHA-256 values match this UI candidate's manifest: `reborn`, `rebornctl`, `reborn-bench`, and `libreborn_media.so`. Installed platform `cli.py` and `observe.py` hashes also match the inspected local source; no runtime replacement was made.

Exact `uname -a`:`Linux y2linux 6.18.0-y2linux-platform-v1-candidate-01 #1 SMP @1764542530 armv7l GNU/Linux`

## Evidence and preliminary results

Private directory (Git ignored, mode 0700):`evidence-private/platform-v1-physical-qualification/20260925T141911Z-owner/`

Per-command receipts retain host UTC, exact command/SSH arguments, exit status, elapsed time, stdout/stderr and limitations. `test-register.json` records each attempted or unexecuted test, exact source/image context, boot ID or its limits, timestamp, command, result, manual observation, status and evidence path. `test-register-original-preflight.json` preserves the original-target preflight. `SHA256SUMS` covers the final private evidence bundle.

The owner reports “i just see the main menu normal warm”. This confirms a visible main menu and subjective normal warmth only. No buttons, playback, screen cycling or cable action were requested. The annotation time is retained in `owner-observations.json`; an exact physical observation time was not supplied.

The initial failed SSH command obtained no boot ID. Later diagnostics are bracketed by the same authenticated boot ID through 14:36:05 UTC; the stalled status PID was identified in that boot. Device wall time was not verified and is not substituted for host UTC. No private-key contents, passwords, bond secrets, NVRAM or calibration were inspected or exported.``````````````````````

| Host UTC | Command / action | Measurement | Status | Evidence basename |
| --- | --- | --- | --- | --- |
| 14:19:11 | y2-status system --json through pinned SSH | SSH exit 255: stale host key; no command output | FAIL | 01-system |
| 14:21:30 | Host USB sysfs and ip route get 10.42.0.1 | ACM/ECM same USB parent, direct 10.42.0.2 route; reported USB speed 480 Mbit/s, not measured throughput | PARTIAL | host-usb-topology.json |
| 14:22:30 | Owner-authorized host-key update | Only Y2 host entry replaced, original retained; existing login key and strict checking preserved | PASS | host-trust-update.json |
| 14:22:30–14:23:20 | y2-status system --json | 50.050 s timeout; no stdout/stderr; host wrapper code 124 | FAIL | 11-system |
| 14:23:49 | uname -a; cat /proc/sys/kernel/random/boot_id; cat /etc/y2linux/versions.json; cat /etc/y2linux/build-id; cat /etc/os-release | Exit 0, 0.209 s; identity above; authenticated USB shell works | PASS | 18-ssh-identity-diagnostic |
| After owner clarification | Compare observed versions to UI candidate metadata | All fields equal; original mismatch retained | PASS | target-clarification.json |

The new host pin was accepted on explicit owner instruction with direct USB topology evidence; it was not independently read from a device console. Authenticated SSH alone does not prove password rejection, USB-only binding, Wi-Fi exclusion or SFTP readiness. The status timeout and health exception are diagnosed below; no silent software fix or service restart has been performed.

## Session A evidence and failures

All rows below use the exact UI candidate identity and boot ID above. The private receipt named in each row contains the complete command, timestamps, exit status and unabridged output. Manual observation is absent except for the display/warmth row. PASS applies only to the stated narrow observation.``````````````````````````````````````````````````````````````````

| Host UTC | Command / observation | Measured result | Status | Evidence basename |
| --- | --- | --- | --- | --- |
| 14:30:57–58 | timeout -s TERM -k 2 15 y2-platform capabilities | Exit 0; current capability declarations captured | PASS | 21-capabilities |
| 14:30:58 | timeout -s TERM -k 2 20 y2-health --full --json | Exit 1, 0.786 s; UnboundLocalError, no health JSON | FAIL | 22-health-full |
| 14:30:58–59 | dmesg -r | 171,210 bytes; warning/error-priority messages present | FAIL (warning gate) | 23-dmesg, kernel-review.json |
| 14:30:59 | Boot ID, uptime, taint, process and mount reads | Same boot; taint 0; distinct read-write root/data; stalled status query present | PARTIAL | 24-runtime-context |
| 14:32:48 | Status PID /proc state, FDs, wakeup-source table, platform source hashes | PID 1945 sleeping in pm_get_wakeup_count; FD 3 is /sys/power/wakeup_count; charger wakeup source active | FAIL (status command) | 25-stalled-status |
| 14:32:48–49 | Boot-stage, application-ready and boot-history JSON reads | Timings below; first-frame record carries current boot ID and Reborn PID/start ticks; prior UI boot marked orderly | PARTIAL | 26-boot-readiness |
| 14:32:49 | Mountinfo, controller sysfs, blkid -p, geometry, ext4 counters, df -k | Expected controller/UUIDs/geometry, separate read-write mounts; both error counters 0 | PASS (identity/current mounts) | 27-storage-identity |
| 14:32:49 | Thermal/power/radio sysfs, ALSA hw_params, meminfo | CPU 48.500°C; PMIC 46.298°C; memory snapshot below; PCM closed | PARTIAL | 28-safety-readings |
| 14:32:49–54 | Installed ELF sha256sum; timeout -s TERM -k 2 5 y2-audio-contract | Four matching ELF hashes; query exit 0, no PCM started; constraints below | PASS (hashes/query only) | 29-installed-elfs |
| Owner observation during this boot | Look at screen and assess case warmth without operating controls | Main menu visible; normally warm | PARTIAL (display/heat only) | owner-observations.json |
| 14:34:44 | Exact-identity cleanup of the orphaned diagnostic PID | SIGTERM only to PID 1945 after boot/start-ticks/cmdline/executable checks | PASS (collection cleanup) | 30-collector-cleanup |
| 14:34:44–49 | timeout -s TERM -k 2 5 y2-status system --json | No output; SSH invocation returns 255 after 5.217 s; subsequent independent SSH works | FAIL | 31-post-system |
| 14:36:03–04 | y2-platform capabilities | Exit 0; after-session capability capture | PASS | 32-post-capabilities |
| 14:36:04–05 | y2-health --full --json | Same exception, exit 1, 0.767 s | FAIL | 33-post-health |
| 14:36:05 | dmesg -r | 200,810 bytes; same 28 kernel priority 0–4 entries | FAIL (warning gate) | 34-post-dmesg, kernel-review.json |
| 14:36:05 | Boot ID, taint, uptime, process list and ext4 error counters | Same boot, taint 0, both error counters 0, no lingering status queries; SSH available | PASS (final context) | 35-post-context |

The required before/after baseline commands were attempted and preserved, but the baseline is incomplete because system status and health produced no valid JSON. Direct diagnostic reads are supplemental evidence, not replacements that make the failed public commands pass. Combined shell commands retain errors even when the last command exits 0: `/proc/1945/stack` was unavailable, and the queried `/run/y2/services.json` and `/data/reborn/logs/supervisor-last.json` did not exist. Those absent queried paths alone do not prove a failed production service.

### Confirmed telemetry defects
  - Health CLI dispatch fails. In

[cli.py](https://github.com/schulzcode/y2linux/blob/HEAD/tools/platform/y2_platform/cli.py), the `network-check` branch imports a local `check` inside `main()`. That shadows the module-level health function throughout `main()`. The health branch calls this unassigned local at line 197, producing the captured `UnboundLocalError`. Owning subsystem: platform CLI dispatch. This is independent of physical sensor health.
  - Status observation can block indefinitely.

[observe.py](https://github.com/schulzcode/y2linux/blob/HEAD/tools/platform/y2_platform/observe.py) reads `/sys/power/wakeup_count` synchronously in `cpu()`. The actual process was sleeping in `pm_get_wakeup_count` with that FD open. Kernel `wakeup_count_show` calls `pm_get_wakeup_count(..., true)`, which waits for active wakeup events to finish. The charger wakeup source was active. Owning subsystem: platform observation/bounding; this is not evidence that charger wake policy should be changed. Snapshot/collection paths sharing `cpu()` require review before dependable baseline or endurance collection. The original host timeout left its remote read process alive; that exact diagnostic process was cleaned up.

No production file, charger policy, wakeup source, service or kernel parameter was changed to bypass either defect. No software fix was implemented.

### Kernel findings and stop rule

The retained before/after buffers each contain **28 priority 0–4 kernel log entries**, including repeated rate-limiting notices. These are not 28 independent crashes. There are no retained `WARNING:` stack reports, Oops, kernel panic, `EXT4-fs error` or `I/O error` matches; taint remains 0. Severity-coded warnings still trigger the owner's stop condition. Relevant messages include:``````````````````

| Kernel message | Likely owning area / limitation |
| --- | --- |
| dummy_timer is not functional. (four entries) | Timer/clockevent configuration; boot-time warning, not a measured reset |
| cacheinfo: Unable to detect cache hierarchy for CPU 0 | CPU/cache description |
| mt6323-led: Failed to locate of_node [id: -1] | PMIC LED driver/device-tree lookup |
| Kernel memory protection not selected by kernel config. | Kernel configuration/hardening |
| mmcblk1: p8 size 4291225599 extends beyond EOD, truncated | Retained stock partition-layout clipping; not an observed ext4 corruption; no table change attempted |
| regulator VCAMA doesn't support get_mode; same for VRTC | Regulator capability/query handling |
| Bluetooth: hci0: broken local ext features page 2 | Bluetooth controller/feature compatibility; pairing/audio remain untested |
| MSDC/OVL/printk callbacks or lines suppressed | Diagnostic rate limiting; limits completeness of some log streams |
| <wifi> send Wi-Fi Start command at warning priority | Driver severity convention; not independently a failed association |

An early informational `Temperature check failed (-61)` precedes later readable CPU/PMIC temperatures; retain it without treating current thermometry as absent. Early ext4 orphan cleanup is followed by both filesystems reporting clean and zero current error counters. It is not counted as a new filesystem error. Charger log samples carry `fault=0x0`; this does not qualify charging. Radio snapshot reports `error=0 transport_errors=0 recoveries=0`; no packet-loss percentage or connection success is inferred.

No owner reboots, rescue transition, input cycle, playback, benchmark or radio test followed the warning review. Session A is incomplete and failed; no more-invasive session was started. No historical warning is silently waived.

### Narrow positive observations

Boot stages on the observed boot: initramfs 0.62 s; storage discovery 0.91 s; preflight 7.54 s; fsck 9.12–9.28 s; root/data mounted 9.65 s; switch_root 9.73 s; platform start 23.498 s; services-started marker 48.485 s; first-frame readiness record 57.785 s; application-ready stage 64.718 s. These are recorded monotonic boot times, not a new cold-boot timing experiment. Actual library-ready timing and full service health remain unverified. Historical orderly-shutdown records do not count as the requested three reboot tests.

Internal eMMC is on `11230000.mmc`, exposing 15,203,328 sectors. Y2ROOT is `/dev/mmcblk1p5`, UUID `79324c69-6e75-4801-8000-000000000101`, start 166,912, length 1,679,360 sectors. Y2DATA is `/dev/mmcblk1p7`, UUID `79324c69-6e75-4801-8000-000000000102`, start 2,104,320, length 1,638,400 sectors. Both are separate ext4 read-write mounts; `/data` also has `nosuid,nodev`. Boot fsck reports both clean; both current `errors_count` values are 0 before and after collection. Available space: root 360,592 KiB, data 730,824 KiB. This does not measure write durability, throughput or recovery under faults.

Instantaneous memory snapshot, KiB: MemTotal 952,304; MemAvailable 866,608; LowTotal 723,952; HighTotal 228,352; Cached 53,356; Slab 11,308. Reborn RSS/PSS, memory growth, workload CPU and frequency/WFI residency were not collected. CPU 48.500°C and PMIC 46.298°C are die-sensor snapshots, not pack temperature or a thermal-load qualification. Battery telemetry was 3,893,994 µV; configured current is not measured battery current or energy.

`y2-audio-contract` accepts S16 stereo 44.1-kHz constraints. It also reports direct 48-kHz constraints; the product-enabled profile remains **S16 stereo 44.1 kHz only**. S24/S32 and 88.2/96-kHz constraints are rejected. The command reports `pcm_started:false`; captured hw_params says `closed`. No playback, unsupported mode or listening test occurred.

## Requested result ledger``````

| # | Requested result | Finding |
| --- | --- | --- |
| 1 | Exact installed Y2Linux | d04b95aaff713edf943042d97a4c6134ca19fc24; release/kernel/build/rootfs above |
| 2 | Exact installed Reborn | 155608393f6acfc6657f2f2e23cd07d0533479c6, 0.1.0-ui-v1-candidate.1; metadata and four ELF hashes match owner-clarified package |
| 3 | Session A | FAIL, stopped during baseline; narrow observations above retained |
| 4 | Session B | NOT_TESTED |
| 5 | Session C | NOT_TESTED |
| 6 | Session D | NOT_TESTED |
| 7 | Actual internal eMMC speeds | NOT_TESTED; no MB/s or ops/s measurement |
| 8 | Actual SD speeds | NOT_TESTED; no SD benchmark or card-cycle action |
| 9 | fsync p50/p95/p99 | NOT_TESTED |
| 10 | SQLite 1k/10k/20k | NOT_TESTED at each size |
| 11 | Reborn 20k navigation | NOT_TESTED |
| 12 | Idle/playback/scan CPU | NOT_TESTED for each workload |
| 13 | Frequency residency | NOT_TESTED |
| 14 | Memory/RSS/PSS | PARTIAL: instantaneous system memory above; Reborn RSS/PSS and growth NOT_TESTED |
| 15 | CPU/PMIC temperatures | PARTIAL: 48.500°C / 46.298°C snapshot; owner says normally warm; no load/endurance qualification |
| 16 | Wi-Fi association | NOT_TESTED; an active radio/core is not association proof |
| 17 | DHCP | NOT_TESTED |
| 18 | DNS | NOT_TESTED |
| 19 | Wi-Fi throughput | NOT_TESTED |
| 20 | Wi-Fi reconnect | NOT_TESTED |
| 21 | Bluetooth pairing/trust | NOT_TESTED |
| 22 | Negotiated SBC PCM | NOT_TESTED |
| 23 | Audible SBC | NOT_TESTED |
| 24 | Bluetooth reconnect | NOT_TESTED |
| 25 | AVRCP | NOT_TESTED |
| 26 | Wi-Fi + SBC coexistence | NOT_TESTED |
| 27 | USB/SSH/SFTP | PARTIAL: ACM/ECM enumerate, pinned owner-key SSH works, service declares SFTP/USB-only binding; no SFTP transaction, password-refusal or Wi-Fi-side listener probe |
| 28 | Kernel/storage/audio warnings | Kernel messages listed above; no retained Oops/panic/ext4-I/O errors; audio playback warnings/XRUNs unmeasured |
| 29 | Software fixes needed | Health dispatch shadowing and blocking/unbounded status observation; review kernel warnings with owning subsystems; no repair performed |
| 30 | Remaining physical gates | Three reboots and rescue, service/library readiness, full input/display cycles, audible wired audio, USB/SFTP confinement, all B–D and endurance; E/F/G retain their separate gates |
| 31 | Acceptable as Platform v1 Core? | Not yet: mandatory baseline tools fail, warning stop rule triggered, and required sessions remain incomplete |
| 32 | Recommended next test/work | Corrective software work and explicit warning review, then repeat Session A with exact resulting versions; endurance, power, OTA and Reborn acceptance are not the next boundary |

Unexecuted checks have no command execution timestamp, measurement or manual observation. The private register enumerates these as NOT_TESTED, including all input/audio actions, all three reboots and rescue, storage/SD lifecycle, SQLite sizes, workload resource comparisons, Wi-Fi state/failure/reconnect/throughput cases and Bluetooth/SBC/AVRCP/coexistence cases. No short observation is used to infer endurance or electrical durability.

## Longer collections prepared, not started

Seven `ui-plan-*.json` records were generated locally using:`python3 tools/host/qualify.py capture --profile wired-8h \ --versions out/y2linux-reborn-ui-v1-candidate/metadata/versions.json`

Profiles: wired 8h; Bluetooth 8h; Wi-Fi + playback; Wi-Fi + Bluetooth; scan + playback; SD cycles; USB cycles. All report `network_contacted:false`. No `--run` was used. The original plain-candidate `plan-*.json` files remain historical and must not be used for this differing source pair.

Execution requires corrected/verified telemetry, relevant short sessions passed, an exact versions file for the actual resulting installed pair, explicit owner approval for duration/workload, a fresh private output directory, the existing owner private-key path and the verified/current host pin. The collector does not start a workload or operate hardware. Approval for an eight-hour run has not been requested because these prerequisites have not passed.

Wired requires observed S16 stereo 44.1-kHz media at an owner-selected safe volume. Bluetooth requires a known paired/trusted peer, actual negotiated SBC PCM and listening confirmation. Wi-Fi combinations require a controlled AP and throughput peer plus proven address/route/DNS. Scan requires a declared dataset and playback workload. SD/USB cycles require scheduled manual observations; request each removal/reinsert explicitly and use disposable media for surprise removal. Record media hashes, workload, observations, collection overhead, counter changes and gaps. Preserve the same stop conditions.

Only documentation and private host evidence were written in this repository. The host's Y2 public host-key pin was updated on owner instruction. On-device cleanup only terminated the exact query started by this qualification attempt; production code, services, hardware policy and protected data were not changed. The final process snapshot confirms no leftover status query. No build, flash, production test suite, reboot or long workload was run. Validation is limited to evidence consistency/hashes, local links and `git diff --check`.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
