---
title: "M2 USB ACM hardware results - Innioasis Updater"
description: "M2 USB ACM hardware results <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m2-usbacm-hardware-result.html"
---

# M2 USB ACM hardware results - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M2 USB ACM hardware results

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M2 USB ACM hardware results > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

## USBACM-03 kernel and PID1 capture confirmed

2026-09-09. The owner completed the privileged host capture into `out/m2-usbacm-03/capture-03/`. Start: 19:00:49.940090 UTC (21:00:49 CEST). The [review record](https://github.com/schulzcode/y2linux/blob/HEAD/docs/build/results/m2-usbacm-03-capture-review.json) verifies the raw file against the recorded length/SHA-256 and every chunk offset/time.````

| Evidence | Result |
| --- | --- |
| Header | Y2LOG1 M2-USBACM-03 |
| USB identity | 0525:a4a7, CDC ACM 02/02/01, host-reported 480 Mbit/s |
| Command / DTR | LOG1 sent; DTR asserted |
| Bytes / chunks | 11754 / 44; contiguous offsets |
| Raw SHA-256 | 24f7516ccb3ab76435b36ebca3a5459333f407ce36c4f4e3d6259fb6e97d5bac |
| Capture duration / exit | 45.048183896 seconds / 0 |
| First / last receive | 1.053460526 / 44.346827084 seconds after reader start |
| Kernel records | Sequence 0 through 77, contiguous |
| PID1 beats | Every beat 1 through 43; beat 1 also appears in startup replay |
| USB configured | First displayed at beat 4; US:6 RC:0 through beat 43 |
| USB IRQ / live DEVCTL | IRQ 43 through 101 while configured; D:99 |
| Protocol GAP/ERR / PID1 LAST ERR | None / NONE throughout |
| Steady heartbeat receive interval | Median 1.110116 seconds; 1.109511–1.110699 |

The `timeout` stop reason is the normal completion of the requested 45-second read window, not an enumeration or read failure: exit code 0, valid header and continuous bytes establish a successful bounded capture. It does not observe device deadline/teardown or BEAT 50. Keep the script's `hardware_qualified=false` field intact; this review establishes narrow facts without full qualification.

Retained kernel messages start with physical CPU0 boot and the exact release, then memory/clock setup, initramfs unpacking and `/init` launch. USB events show stage 2 at kernel timestamp 1.300853s, fresh valid supply/clock/USB snapshots at 4.162228s (CHR=0063), guarded session/unchanged sampled mode/trim values, g_serial ready and stage 6 at 4.693779s. The earlier “couldn't find an available UDC” message precedes the deliberately delayed controller registration; later binding/configuration and actual LOG1 transfer demonstrate that it did not prevent this capture. Cache-hierarchy detection and unselected kernel-memory protection warnings remain visible; this is not a production qualification.

CONFIRMED: one physical USB ACM transfer carries retained early kernel messages and ongoing native PID1 heartbeats without sequence gaps or reported relay errors in this window. The previous reader-access blocker is resolved for this owner-run capture. Host logging as a wider capability is PARTIAL pending repeatability, late-open/non-reading host, detach/reconnect and stability checks. No milestone closes; M1 remains complete, M2 active with blocked exit and #23/#27/#28 open. No new hardware/memory/production scope is activated.

Private copy of all three original files plus review: `evidence-private/20260909-m2-usbacm-result/capture-03/`. Association uses the build header, kernel release, USB manufacturer and retained candidate, not an independent flashed-byte readback. Power-on timing/restoration remain unreported.

## USBACM-03 host enumeration confirmed

Historical intermediate result; LOG1 uncertainty and the owner-run access blocker below are superseded by capture-03 above. Session access still needs its own check.

2026-09-09. The owner reports the Y2 appears in CachyOS and its screen shows connected. Host kernel journal entries at 20:47:51 and 20:50:05 CEST confirm high-speed USB enumeration on port 5-2 as `0525:a4a7`, product `Gadget Serial v2.4`, manufacturer `Linux 6.18.0-y2-m2-usbacm3 with musb-hdrc`. The host CDC ACM driver creates `ttyACM0` at interface `5-2:2.0`. The first event disconnects at 20:48:22. These are host USB events, not proof of two independent cold boots or qualified reconnect behavior. Exact power-on/cable timing, flashed hash and restoration are not independently established.

The first capture's “No matching CDC ACM device appeared” result was misleading as device evidence: the assistant ran it in a sandbox with a private `/dev` and no host USB nodes. An unsandboxed `lsusb` sees `0525:a4a7`. A second, unsandboxed capture matches the device but fails opening `/dev/ttyACM0` with EACCES. Host mode is `crw-rw---- root:uucp`; user luca is not in uucp and no user ACL grants access. Noninteractive sudo reports that a password is required. No host permission/group change was made. Keep both capture failure records as host execution failures, not evidence against enumeration.

CONFIRMED: USBACM-03 enumerates on the host with a CDC ACM tty. This also shows that this run progressed beyond the earlier sync-only refusal. **Still unproved:** LOG1 bytes, real kernel/PID1 log continuity, reader/reconnect/stability qualification and M2 exit. The next step is the same capture script with host device access and sufficient local permission, using the same BOOTIMG. No new firmware build is needed. A one-off `sudo python3 .../usb_log_capture.py` can be launched by the owner in a terminal using their local password.

Private journal and manifest: `evidence-private/20260909-m2-usbacm-result/``usbacm-03-host-usb.log` and `usbacm-03-host-manifest.json`. Capture failures: `out/m2-usbacm-03/capture-01/failure.json` and `capture-02/failure.json`.

## USBACM-02 result

2026-09-09. The owner supplies `out/m2-usbacm-02/debug.jpg`, reports the attach prompt appears, and explicitly confirms the error follows **before attaching USB**. BUILD and heading are M2-USBACM-02, Linux 6.18.0-y2-m2-usbacm2. Poll 5 fails at US:2 RC:-16 with PW:-16 V:0. WACS is `00200001>00200001`; gates are M:00 W:01 A:0000007F C:01 I:01. Cached PW:0/7, CLK:0/15, successful wake and the earlier PHY/trim values remain visible. BEAT 8 / FRAME 52, uptime/idle 8.00/8.19, timer IRQ 802, MemTotal 22096 kB and previous frame write 804 are visible. The uptime/idle pair is transcribed as shown, not timing qualification.

Private original: `evidence-private/20260909-m2-usbacm-result/debug-02.jpg`, 276888 bytes, SHA-256 `b02fa3168c4aca08df60f5446d9bb95b19e4d1c3e451cedc553b900a12364cdc`.

The failed word decodes to INIT_DONE=1, SYNC_IDLE=0, REQ=0, FSM=0, low data=0001. This establishes a sync-only pre-command refusal, not an active or stale WACS2 transaction and not an attachment/enumeration failure. Four prior worker polls completed; the fifth failed before issuing its first CID command. The duration/cause of sync activity and independent flashed hash/restoration remain unreported. This does not retrospectively prove USBACM-01 failed for the same bit; that candidate lacked the raw sample.

The source-reviewed localized fix, USBACM-03, waits at most 1000 x 10us for sync to become idle, checking initialized/no-request/FSM-idle on every sample. Commands still require the unchanged complete ready predicate. Busy/stale channel states stop immediately; timeout stops without command/retry/reset. The existing failed snapshot remains visible if the wait fails.

## Original USBACM-01 evidence

2026-09-09, implementation `c066d62`. The owner reports USB unplugged at power-on and no visible attachment prompt. One supplied photograph, `out/m2-usbacm-01/debug.jpg`, shows BUILD M2-USBACM-01 and Linux 6.18.0-y2-m2-usbacm1. The top M2-USBGUARD-01 heading is a stale literal in `kernel/diagnostic/text.h`; it does not identify a different running kernel.``

| Visible field | Value |
| --- | --- |
| USB stage / result / IRQ / live DEVCTL | 2 / -16 / 0 / unread |
| USB message / last error | USB STOP RC:-16 / USB LIVE -16 |
| Cached PWRAP result / valid | 0 / 7 |
| Cached clock result / valid | 0 / 15 |
| Live CHRDET / presence | unread / unknown (---- D:?) |
| Wake result / written / validity | 0 / 1 / 7F-FFF |
| PHY6a before / after | 04 / 00 |
| Post POWER / DEVCTL | 20 / 80 |
| Post PHY68..6e | 00 00 00 02 12 00 00 |
| PHY1a / 1d / 22 / 63 | 10 / 00 / 00 / 00 |
| PHY00 / 05 / 15 before-after | 6E/6E / 44/44 / 10/10 |
| BEAT / FRAME | 12 / 76 |
| Uptime / idle / timer IRQ CPU0 | 12.44 / 11.17 / 1246 |
| MemTotal / CPUs online | 22096 kB / 0 |
| Proc / sysfs / sleep / previous frame write | 0 / 0 / 0 / 804 |
| Watchdog / framebuffer | STOPPED / GUARD OK |

Private original and manifest: `evidence-private/20260909-m2-usbacm-result/`. Photo SHA-256: `11b37974afc8b9cb4affefdfb3213265eb09aa939e7076183514eba7a5aba982`. The photograph catches a READ MEMORY redraw with trailing older stage pixels; it does not establish a memory-read hang. Exact flashed hash, elapsed host time, later cable activity, restoration and any host capture are unreported.

## Source-backed localization and limit

Stage 2 is `Y2_USB_ATTACH`. Reaching it requires successful cached supply, clock and PHY-wake checks and successful persistent PWRAP/PHY resource claims. It excludes the earlier resource-claim `-EBUSY` branches at stage 1. `CHR:---- D:?` is set only after a failed live worker supply poll. Together with stage 2 and result -16, this localizes the stop to `y2_pwrap_probe()` during the cable-wait period, before controller registration or enumeration. It does not identify which poll failed or whether PID1 ever painted the attach text.

The PWRAP protocol returns -16 when its initial or pre-command WACS2 sample fails the existing idle predicate. That predicate requires init, sync-idle, no request and FSM idle. The failed sample is not exported in this candidate. Consequently sync activity, a request or stale completion cannot be distinguished from this photograph. Do not label the failure transient, blame a cable or weaken the predicate without the missing evidence. Cached PW:0/7 is the earlier successful snapshot, not the result of this later poll.

## Localized follow-up

M2-USBACM-02 retains the failed worker PWRAP snapshot before teardown and exports it under a separate lock through version 2 of the local live-status ABI (88 bytes, formerly 36). PID1 shows poll number, failed result/valid mask, full before/after WACS words and gate values (MUX/WRAP/channel/init low bytes, full arbitration). On this failure those rows replace CPU-online and mount status; the original PHY/wake rows remain visible. Initial CPU/mount results remain in PID1 history. The heading, BUILD, release and LOG1 identity are updated together.

All hardware transactions, poll/deadline limits, refusal rules, D08, CPU0, BOOTIMG packaging and recovery policy remain unchanged. This fixes missing failure evidence; it does not claim to fix the underlying busy state. Targeted worker/status and ARM PID1 fault tests, renderer/relay/PWRAP/session regression, one clean build and real-artifact/D08 checks apply. Next owner evidence is the complete new screen if the same refusal recurs, or the existing bounded capture if attachment/enumeration proceeds. No milestone or capability is promoted: M1 remains complete, M2 active with blocked exit, #23/#27/#28 open, M3 deferred.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
