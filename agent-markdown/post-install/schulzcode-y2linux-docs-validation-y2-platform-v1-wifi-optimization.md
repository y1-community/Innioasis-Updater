---
title: "Y2 Platform 1.0 Wi-Fi optimization - Innioasis Updater"
description: "Y2 Platform 1.0 Wi-Fi optimization Date: 2026-10-04. Scope: Innioasis Y2, MT6582, MT6627-era CONSYS radio, approximately 1 GiB RAM. Isolated branches codex/platform-v1-wi"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-wifi-optimization.html"
---

# Y2 Platform 1.0 Wi-Fi optimization - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 Platform 1.0 Wi-Fi optimization

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 Platform 1.0 Wi-Fi optimization

Date: 2026-10-04. Scope: Innioasis Y2, MT6582, MT6627-era CONSYS radio, approximately 1 GiB RAM. Isolated branches `codex/platform-v1-wifi` in Y2Linux and Y2Reborn. No flash, push, parallel-branch merge or Bluetooth implementation change. Starting source: Linux `b5aea93`, Reborn `b71b468`.

## Architecture and evidence authority

The retained MT6582 vendor fullmac driver uses the owned AHB/DMA and CONSYS firmware/calibration path, exposes cfg80211/nl80211, and uses firmware AIS/scan/ roaming state machines. It is not a mac80211 softmac radio. Exact donor receipt: `kernel/platform/connectivity/wifi/reference.json`, commit `53fb57bb99c916c24b65db5b7f9723be37f67826`. No later MediaTek register layout is used. `CFG_TCP_IP_CHKSUM_OFFLOAD=0` remains unchanged; Linux computes the checksums that this firmware/transport could not offload correctly.

wpa_supplicant 2.12 owns WPA2 personal authentication and reconnect. The connectivity supervisor attaches wlan0 through nl80211 and uses a separate wpa_cli action monitor to own one epoch-scoped udhcpc lease. DHCP callbacks configure only wlan0 address/routes and `/run/y2/resolv.conf`; USB's fixed management address is independent. The readiness service publishes association, IP, default route and a successful bounded libc DNS probe separately. Reborn uses its own supplicant control socket and validates the platform readiness record. Explicit scans attach an event socket before requesting SCAN, reject duplicate active requests and finish only on a real scan-completion event. `SCAN_RESULTS` reads the cache; it does not start a scan. These distinctions follow the [supplicant control API](https://w1.fi/wpa_supplicant/devel/ctrl_iface_page.html) and [cfg80211 driver API](https://www.kernel.org/doc/html/latest/driver-api/80211/cfg80211.html).

The current release inventory identifies sealed Baseline02, compiled Linux `8584ccd85f052f351fe51650b2348c83ca894ed4` and Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`. Lock-protected USB SSH actually observed that image running: kernel `6.18.0-y2linux-baseline-02`, root v1.21, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0. This supersedes the old awaiting-installation statement for image identity. It does not independently close the Baseline02 CPU cold-boot or full-system-suspend qualification gates.

Retained physical authority: [ordinary DHCP/DNS/TCP and three TCP repeats](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FPLATFORM-V1-PHYSICAL-BRINGUP.md), [latest checked C1/C2/C3 returns](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md), and the [Baseline02 seal](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fvalidation%2FY2-BASELINE-02.md). Historical Wi-Fi TCP into Y2 is 45.15–45.60 Mb/s and out is 46.35–46.56 Mb/s. Those are measurements, not a proof of a practical hardware ceiling or a new measurement on this branch.

## Deficiencies and changes
  - Real control latency exceeds the observer deadline. Two bounded STATUS

queries succeeded in 1.4795 and 2.0809 seconds; two SIGNAL_POLL queries succeeded in 2.0793 and 2.0787 seconds. A power-save GET also took 2.0789 seconds. The platform's one-second STATUS deadline therefore reported `supplicant_unavailable` while association, lease, route and ordinary ping worked. Reborn's two-second observation deadline was also marginal. STATUS, observational PING and power-save GET now have three-second bounds. Mutation deadlines remain unchanged. Exact driver `get_station` queries link speed, RSSI and optional statistics through vendor OIDs; these can serialize control work. The source and timing explain the exposure, but do not prove the cause of each particular delayed reply. No guessed firmware fix is made.
  - DNS readiness inherited a previous lease's deadline. The old service set

the next probe 30 seconds ahead even when association was complete but DHCP had not yet supplied IP/route. A reconnect within that deadline inherited the delay. The new scheduler first requires usable IP/route and keys its deadline to epoch, peer and addresses. A new usable lease is probed immediately; unsuccessful probes on the same lease retain bounded retries. DNS proof now explicitly requires a nonempty current epoch, matching boot, peer/address and age; a route change during a probe invalidates the result.
  - Screen-off readiness slept through supplicant events. The existing

passive event monitor now supplies the readiness wait with its socket. Real events wake the service; acquisition/scan/handshake states have a one-second observation cadence. Settled idle retains the existing 3-second awake / 10-second dark cadence. Unknown queries do not enable fast polling.
  - RSSI polling duplicated slow firmware work. RSSI and its timestamp/query

result are cached for at most 30 seconds on the same boot/peer. An unknown association returns unknown RSSI. Actual counters and association still refresh normally; errors are not presented as signal loss or disconnects.
  - Unchanged power policy was resent to firmware every 30 seconds. GET checks

current cfg80211 state; SET occurs only when needed, or to establish policy after boot/association/interface recreation. Readback and retry behavior are retained. Diagnostics distinguish requested CAM/FAST_PSP and whether SET was applied. They remain provisional host state, not a firmware-sleep or electrical-current measurement.
  - Reborn repeatedly fetched unchanged lists. Association polling retains

its cadence. Scan and saved-network lists refresh on explicit operations, association/peer changes and every 30 seconds. Completed explicit scans keep their results and duplicate scan requests still issue only one SCAN.
  - Reborn could consume another peer's fresh Online record. Online now must

match the live completed association and address as well as record boot/age. Its diagnostic status also exposes association_id. Unmatched proof becomes unavailable, not a fabricated Online state.
  - Radio-off cleanup inflated raw disconnect actions. The physical toggle

increased `disconnected` twice while a direct disconnect increased it once. The supervisor explicitly repeats the DHCP action when removing an interface. The historical action count stays compatible, while new `real_disconnects` and `reconnects` count known link transitions and expose their start time. Initial/duplicate cleanup and unknown status never count as another real loss. These lifecycle counters are host-regression validated; the RAM readiness overlay does not replace the installed DHCP/action script.
  - Query failure totals were absent from platform readiness. The daemon now

retains a same-boot count of failed published status observations separately from the existing real CONNECTED/DISCONNECTED event counts. Existing Reborn association-transition logic already preserved unknown state correctly and was left intact. Failed queries never mutate DHCP epochs or link events.
  - Redacted diagnostics discarded useful Wi-Fi state. Fixed Wi-Fi states,

association/policy enums, query failures, link-transition counters, RSSI timestamps and interface error counters now survive the reviewed projection. Arbitrary strings, peer/IP identifiers and lease epochs remain private. A regression tests both retained observations and rejected private values.

## Power-save semantics and rejected changes

The exact vendor `mtk_cfg80211_set_power_mgmt` mapping is: disabled → CAM; enabled with timeout -1 → FAST_PSP; enabled with another timeout → MAX_PSP. The normal nl80211/iw switch supplies -1. MAX_PSP therefore is not a second safe product mode established by `iw ... power_save on`. No automatic strong screen-off mode is invented. Firmware sleep/current is not proved by iw's cfg80211 flag readback.

Product modes stay off, standard and automatic. Standard requests FAST_PSP. Automatic retains its conservative default CAM; explicitly qualified `automatic_standard=true` can request FAST_PSP and switch to CAM for the existing heavy-transfer hook. Default-on power saving is rejected until idle, latency, transfer, reconnect and Bluetooth playback coexistence have comparable physical evidence. Electrical battery savings require electrical measurements.

Also rejected: TX checksum offload, larger socket buffers without demonstrated window pressure, forced CPU frequency/core/clock changes, disabling required connectivity for an idle counter, changing DHCP lease renewal behavior without current failure evidence, speculative DMA/interrupt tuning, Bluetooth codec or reconnect work, and any claim of a radio/CPU ceiling based solely on a 65 Mb/s PHY report. The current live link reported single-stream HT20/65 Mb/s at approximately -49 to -53 dBm. Ordinary TCP near 45 Mb/s is plausible for that link, but a controlled rate/CPU/window/power comparison is needed to establish what actually limits it.

There is no configured product bgscan daemon or periodic user SCAN. The driver retains 2-second minimum/maximum WAIT_FOR_NEXT_SCAN constants. Inspection shows that state is conditional, not a healthy-associated timer; infrastructure no-candidate handling normally queues reconnect and returns to IDLE. Changing those constants without evidence that the affected path is active could slow recovery or change a different legacy mode, so they remain unchanged.

## Measurement method and before/after results

Hardware tools take nonblocking flock on `/tmp/y2-platform-v1-device.lock` before every USB SSH or LAN device request, including upload and cleanup. Busy ownership is left alone and retried while source/host work continues. No probe bypasses it. Raw local receipts and collectors live in `out/wifi-optimization/`; the tracked [sanitized receipt](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-wifi-optimization.json) includes snapshot deltas, stage timings, transfer hashes, artifact identity and raw-receipt SHA256 values. It omits SSIDs, radio addresses and bonds. The prepared after-runner copies Python sources under `/run` and restores the installed readiness daemon in a finally block. Its first preparation failed on unavailable BusyBox gzip/tar support before stopping any service; the archive was corrected to uncompressed USTAR. Two subsequent 15-minute retry windows could not acquire the lock. The RAM after-service was therefore NOT_RUN, and no rootfs or persistent policy was replaced. Reborn source changes are host/ARM validated separately; the application was not physically replaced.

Idle windows use two `/proc/stat`, `/proc/interrupts`, cpuidle and network counter snapshots around 20 seconds. Busy CPU is expressed as percent of one CPU, excluding idle/iowait; IRQ/s and context-switch/s are deltas. Per-state entry/time deltas are reported without equating every IRQ or context switch with a CPU wakeup. `wakeup_sources` covers registered wake sources, not all runtime CPU wakeups. USB management and charging are present, so this is not an unplugged battery measurement. Association/handshake/IP/DNS/platform-ready are separate observed stages; a missed fast stage is not assigned a fabricated time.

The baseline completed with the same boot and taint 0. Four cores were online at 1300 MHz in both baseline idle windows, unlike the earlier CPU0-only read-only admission. This shared-session environment must be carried into the after comparison; no core/frequency policy was forced by the Wi-Fi collector. The 20-second associated window had 14 Wi-Fi IRQs, 420 received bytes and no transmitted bytes, errors or drops. Most interrupts came from timers/IPIs; Wi-Fi was not the dominant source of idle IRQs in this window. TCP and file windows also had zero exposed interface errors/drops. Twenty small HTTP requests had a median of 6.961 ms and maximum of 17.251 ms. Each of the four 8 MiB transfers matched SHA256 `7d212b9c884f5c77896de960ae17cc341cda43b14d6a971f34ca29ebd4badf7f`. Aggregate CPU during the TCP window was 67.414% of one core; no CPU saturation or window ceiling was established. TCP read/write autotuning maxima were 5,724,160 / 4,194,304 bytes.

One iperf TX control connection reset on the second consecutive test. Preserve that FAIL; HTTP's successful TX hashes do not erase it. Bidirectional traffic was asymmetric, so it is not advertised as symmetrical simultaneous throughput. The temporary FAST_PSP sample began with `Power save: on` and ended with `off` after the installed automatic policy reapplied CAM; **that sample is invalid for a CAM-versus-PSP power comparison**. Default policy is not changed based on it.

The baseline is physical. After values below distinguish source regressions from physical NOT_RUN because the shared lock remained owned by storage, library and Reborn performance sessions. Those sessions were left alone. An isolated one-shot TX follow-up also found the lock busy; the iperf control reset remains unresolved. Retained throughput and CPU qualification are never relabeled as an after-result.

| Metric | Before | After |
| --- | --- | --- |
| STATUS successful latency | 1.4795 / 2.0809 s; exceeds old 1 s platform bound | 3 s bound; 2.1 s delayed-reply regression passes |
| Same-lease DNS retry interval | 30 s, also inherited by new leases and pre-IP association | 30 s only after usable lease; new lease starts immediately (regression) |
| Settled Reborn scan/saved list reads | 40/minute at 3 s cadence | 4/minute plus operations/association changes (source behavior) |
| Settled RSSI query frequency | Up to 20/minute awake; 6/minute dark, plus probe work | At most once per 30 s of matching published cache |
| Unchanged policy firmware SET | 2/minute | 0/minute once established; GET and generation recovery retained |
| Completed WPA2 association / IP / DNS / platform-ready | Reconnect 1: 2.545 / 4.379 / 24.322 / 32.241 s; reconnect 2: 0.829 / 2.676 / 21.131 / 29.051 s | NOT_RUN — shared device lock unavailable |
| Radio toggle → IP / DNS / platform-ready | 5.877 / 20.206 / 27.987 s | NOT_RUN — shared device lock unavailable |
| RX / TX / bidirectional TCP | Current RX 40.667 Mb/s; TX iperf control reset; bidirectional RX 41.513 + TX 3.916 Mb/s | NOT_RUN — shared device lock unavailable |
| Four checksummed 8 MiB HTTP transfers | RX 43.941–44.922 / TX 46.376–46.942 Mb/s, all hashes pass | NOT_RUN — shared device lock unavailable |
| Screen-off associated CAM CPU / IRQ/s / context-switch/s | 11.222% of one CPU / 289.23 / 382.73 | NOT_RUN — shared device lock unavailable |
| Screen-off radio off CPU / IRQ/s / context-switch/s | 9.905% of one CPU / 277.98 / 375.69 | NOT_RUN — shared device lock unavailable |
| Completed C1 idle cycles/s (proxy, all four CPUs) | Associated 258.497; off 251.950 | NOT_RUN — shared device lock unavailable |
| Explicit associated scan duration / CPU / IRQ | NOT_MEASURED; explicit scan completion is source-tested | NOT_RUN — shared device lock unavailable |
| Four-way handshake / radio-ready / UI-ready | Separate phase not captured; platform-ready is not UI-ready | NOT_MEASURED |
| AP loss / reboot → ready | NOT_RUN | NOT_RUN |
| Runtime CPU wakeups / electrical battery | NOT_MEASURED | NOT_MEASURED |

## C2/C3, screen-off and Bluetooth boundaries

Radio-associated firmware and required CONSYS/APDMA/BTIF ownership are real idle admission inputs. CPU source guards require quiet domains/clocks; an 802.11 power-save flag does not itself power off CONSYS or establish that those clocks can safely be released. The pass neither relaxes guards nor forces clock gates, core parking, dormant entry or full-system suspend. USB and any current playback also confound a radio-only idle comparison. Retained UART01 C2/C3 residency proves those states with its qualified radio-off topology, not associated Wi-Fi admission on this branch. Current baseline C2/C3 entry and residency deltas are zero both with Wi-Fi associated and off. The off preflight removes CONSYS/APDMA/BTIF blockers (domain mask 0xe02→0xe00, peripheral mask 0x102c00→0x400), while four-core topology, 1300 MHz and the remaining USB clock block admission. No conclusion that Wi-Fi alone prevents a qualified C2/C3 topology is drawn from these windows.

Source policy for stopped/local/Bluetooth playback and active file transfer retains connectivity; only stopped screen-off and active file transfers were physically measured here. Local-playback and Bluetooth-playback combinations are NOT_TESTED. Readiness observers now wake for events during screen-off; no new policy disables networking during music playback. Current Bluetooth observation before measurements: controller Powered=false, paired peer disconnected, no active PCM. The owner confirms the paired headset is unavailable for this pass; connected-idle and SBC coexistence are NOT_TESTED. They must be reported from an actual connected/running peer; firmware availability or an existing bond is insufficient. No Bluetooth-side change is included.

## Validation and delivery

Fresh Linux affected tests: Wi-Fi command completion, connectivity (including emitted pinned Baseline02 DT), radio policy, network/time, readiness/CPU service regressions and platform contract: 94 passed, 0 skipped. D08/BOOTIMG fixture checks: 5 passed. Diagnostic-export checks: 6 passed, including the new Wi-Fi retention/privacy regression. Python compilation and diff whitespace checks pass. The worktree uses the existing source cache read-only for tests. The initial missing-cache/dependency failures were resolved using that cache and existing pyelftools; no source or identity change was needed.

Fresh Reborn platform tests: 74 passed at the current receipt, including live delayed fake-supplicant replies, request-count/cache invalidation, scan completion/duplicate handling and association/readiness binding. Native build, ARMv7 platform-crate build against the existing target sysroot, rustfmt and clippy with warnings denied pass. These are crate checks, not a new full image build or physical acceptance of a replaced Reborn application.

Changed Linux implementation: `network.py`, `observe.py`, `radio_policy.py`, `service.py`, `diagnostics.py` and `diagnostic_fields.py` under `tools/platform/y2_platform/`. Regression files: `tests/test_platform_network_time.py`, `tests/test_radio_policy.py`, `tests/test_platform_contract.py`, `tests/test_diagnostic_export.py`. Changed Reborn implementation/tests: `crates/reborn-platform/src/wifi.rs`. Planning audit/roadmap, radio knowledge summary, this report and its sanitized evidence receipt record the boundary.

Implementation commits, local only:
  - Y2Linux `d408b28ac7513470a66d2b49a9ebbf3347e79d6a`: readiness, observer and policy fixes.
  - Y2Linux `61eecee1961c9243077388d196bd8113db626b5a`: real link-loss/reconnect counters separate from cleanup actions.
  - Y2Linux `2bd345a3eb2b35c30c3103dacd43cb9ed903fae7`: reuse RSSI within DNS rechecks.
  - Y2Linux `7056977dc534a655f0ca8d1a4c1f4353e8131d27`: retain reviewed Wi-Fi diagnostics with private values redacted.
  - Y2Reborn `2cdb9cce8df1b9a65a4f88f8cd39dd05f851093e`: inventory caching and current-link Online proof.

The closing documentation commit records its own scope in the branch log; it cannot contain its own commit hash. No main-worktree edits, push or merge. Existing configured identity is preserved, including passing the same configured Linux author/committer environment to the Reborn commit without changing config.

Verdict: source pass complete; Platform 1.0 physical acceptance PARTIAL. The current physical foundation reliably associates, leases, resolves DNS and transfers checksummed files at approximately the retained rate in this bounded LAN window. Genuine readiness latency, redundant observer/policy work and telemetry deficiencies are fixed with regressions; the working driver path is preserved. This does not prove a hardware ceiling, electrical savings or after performance. Required next boundary: reconcile the shared wait with USB, qualify this exact integrated service plus DHCP action handler/Reborn binary, and repeat readiness/idle/transfers under the lock. Then cover AP loss, cold-boot, screen/playback combinations, a stable CAM/FAST_PSP comparison and actual Bluetooth connected/SBC playback when a headset is available. Wider AP-loss/cold-boot/endurance/full-suspend/coexistence and battery coverage retain their actual gates. No milestone is promoted from source tests alone.

## Integration handoff

The independent USB workstream also edits the shared readiness service. Its control/signal wake must be reconciled with this branch's supplicant socket wait into one bounded wait mechanism. A clean textual merge alone does not prove both wake paths, shutdown and acquisition cadence. The integration coordinator's main-worktree plan identifies this as C01; this branch does not merge or redesign that parallel implementation. Its C18 diagnostic review is addressed here for fixed Wi-Fi fields only; Bluetooth/USB union and privacy checks still belong to integrated validation. Main-worktree coordination documents were read only, and their unrelated pending changes were left intact.

## Closing roadmap/gap audit

The scoped source boundary closes using the actual Baseline02 receipt above, not a deployment claim. GitHub #28/#31/#34 were refreshed read-only at closing and remain OPEN. The roadmap and knowledge summary preserve their CPU, connectivity, coexistence and wider release gates. No epic/milestone is closed. Main-worktree coordination changes belong to other sessions and are untouched. Both dedicated branches are delivered as local commits; the after-device constraint remains an explicit evidence limit.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
