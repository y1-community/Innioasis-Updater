---
title: "DEV-02 live platform qualification — 2026-09-10 - Innioasis Updater"
description: "DEV-02 live platform qualification — 2026-09-10 <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-y2linux-dev02-live-qualification.html"
---

# DEV-02 live platform qualification — 2026-09-10 - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# DEV-02 live platform qualification — 2026-09-10

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# DEV-02 live platform qualification — 2026-09-10 > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

The physical Y2 runs Buildroot successfully with expanded RAM, four CPUs, removable-SD root, native display and all tested controls. **USB reconnect fails: the first unplug removes both ACM and Ethernet, and reconnect does not enumerate.** The owner reports that USB works again only after restarting the Y2. No restart was initiated by the assistant. The owner subsequently restarted the Y2: USB/SSH returned at uptime33.32s, down from1595.34s, with the tmpfs token missing. This proves restart recovery, not reconnect continuity. The second cycle was not performed because the first was not clean.

M2's generic core/Buildroot foundation is substantially qualified. Keep #27/#28 open for the real reconnect blocker, not the superseded RAM/input/display/SD research sequence. The later platform phases remain ahead of application work.

## Evidence and identity

Complete command stdout/stderr and raw evdev bytes are retained in [the evidence directory](https://github.com/schulzcode/y2linux/blob/HEAD/docs/hardware-evidence/2026-09-10-dev02-live/). `SHA256SUMS` identifies the final files; `session.json` distinguishes owner observations from machine measurements. The source checkpoint is `a34a360`, with pre-existing uncommitted DEV-02 implementation preserved. No kernel build, BOOTIMG packaging/flash, eMMC write, raw physical-memory access or arbitrary debugfs register write occurred during this pass.

`uname` identifies `6.18.0-y2linux-dev02`; the live flattened DT SHA-256 is `57d774abaf2d410bbfbd5ec8956f7f3c4a35bf3120611fadb474cd51c12947e7`, matching the built DEV-02 DT. The entire flashed BOOTIMG was not read back. The installed userspace build ID and USB serial intentionally retain `Y2LINUX-DEV-01`.

## Physical result and failure classification

Classes: A working within the measured scope; B userspace/configuration; C driver/kernel work; D hardware acceptance requiring a subsequent kernel candidate test; E later platform work. An unavailable optional diagnostic is not proof that the underlying hardware failed.``````````

| Subsystem | Actual physical status / errors | Class | Another kernel flash? |
| --- | --- | --- | --- |
| Root/init | Buildroot 2025.02.17, BusyBox PID1 on ext4 /dev/mmcblk0p1; not rescue | A | No |
| Removable SD | Y2ROOT UUID 79324c69-6e75-4801-8000-000000000001, controller 11240000.mmc; file hashes and successful persistent userspace update/readback | A | No |
| SD operating mode | 13 MHz, one bit; 512 MiB ext4 inside a 119.1 GiB partition. Partition type byte remains 0x0b; actual filesystem is ext4. No resize/type rewrite attempted | A, deliberate development limits | No |
| Internal eMMC | mmc@11230000 disabled in live DT, no platform host/block/partition device; unmounted. No live CID is exposed to read | A protection | No |
| CPUs | Four online, CPU0–3; cross-CPU/timer interrupts advance, interrupt error count zero | A | No |
| RAM | MemTotal 954660 KiB; 256 MiB short allocator test passes; exhaustive run capped at 600 seconds | A bounded qualification | No |
| Buttons | Prev 105, Menu/Back 158, Next 106, Play/Pause 164, Select 28, Volume− 114, Volume+ 115, Power 116; balanced EV_KEY press/releases | A | No |
| Wheel/I2C | Both KEY_UP 103 and KEY_DOWN 108; 52 wheel IRQs and 52 I2C completions at the retained snapshot; no -110 regression | A | No |
| Display | Owner confirms white/red/green/blue plus checkerboard; active native DRM/fbcon. Standard fb0 unblank/readback works | A/B | No for visible output |
| Pattern diagnostic | Initial/live pattern checks match; later startup checks mismatch with the fbcon cursor active. Two cursor-hidden checks and the corrected helper pass; cursor handling fixed in userspace | B fixed | No |
| SSH/USB Ethernet | Root ED25519 authentication succeeded; usb0 10.42.0.1/24; host static USB profile fixed | A before detach; B host fixed | No for initial connection |
| USB reconnect | Host records disconnect at 21:32:50 CEST; owner reconnect does not produce enumeration, ACM, Ethernet or SSH | C likely / D requalification | Likely; exact device-side cause unobserved |
| CDC ACM | Enumerated during live boot. Initial LOG1 attempt hit host EACCES; scoped uaccess rule installed. After owner restart, LOG1 transfers61463bytes in12s with protocol header | A transfer / B host fixed | No for ACM transfer; reconnect still fails |
| PMIC/core buses | PWRAP/MFD/regulators, PMIC key, GPIO/EINT, I2C and SD consumers operate; USB presence power_supply reports ONLINE=1 before detach | A narrow core | No |
| Services/runtime | syslogd, klogd, observer, crond and Dropbear PID files point to live processes; rescue mount options and module-index mismatch fixed | A/B | No |
| Time/network/entropy | Wall clock starts in 1970, no RTC class; CRNG initialized at 153.97 seconds before key generation. No USB default route/DNS is intentionally configured | E; development limitations | No current core flash |
| Audio | Native ALSA/ASoC, AFE, CS43131, amplifier, routing and jack operation not qualified | E / M3 | Later integration |
| Power | Battery/charging/thermal, cpufreq/cpuidle, suspend/wake, shutdown/reboot unqualified; USB presence is not battery telemetry | E / M4 | Later integration |
| Radio and GPU | Wi-Fi/Bluetooth/firmware/calibration/BlueZ and GPU/lima not qualified | E / M5 and final platform | Later integration |

## Memory accounting and bounded test

The described bank is 992 MiB, `[0x80000000,0xbe000000)`. The 40 MiB loader guard, 1 MiB in-bank high reservation and 16 KiB low guard leave 973808 KiB = 950.984375 MiB before ordinary kernel reservations. Actual MemTotal is 954660 KiB = 932.28515625 MiB. The remaining difference is 19148 KiB (18.69921875 MiB), covering kernel/static and early allocation overhead, including memory-management structures. It is not missing addressable RAM and is not current userspace memory consumption. The boot log gives the early kernel/reserved breakdown; freed boot allocations make the later MemTotal differ from the early `Memory: ... available` value.

HighTotal is 228352 KiB. During allocator testing HighFree fell to 872 KiB and Mlocked reached 262144 KiB, corroborating substantial use of HIGHMEM through the normal allocator. MemAvailable stayed at least 656140 KiB in recorded samples. No `/dev/mem`, reserved range, physical address selection or swap was used.

`03-ram.txt` retains `memtester 256M 1`, periodic meminfo/dmesg, and deliberate termination at 600 seconds (exit 143). Address, random, arithmetic, sequence and solid-bit tests completed; the exhaustive block/bit-pattern suite did not finish. This is not a full-suite pass. To obtain a completed short qualification, `11-ram-short.txt` runs 256 MiB with mask `0xff`: stuck address plus random, XOR/SUB/MUL/DIV/OR/AND and sequential increment. All pass, memory is locked, and both helper and SSH return zero in about 39 seconds. No mismatch, OOM, oops/panic, allocation fault or memory corruption message was observed. This does not certify overnight stress, every RAM page or all inherited DMA.

## Display inspection

DSI-1 is connected/enabled with one 480×360 mode. CRTC 55 is enabled/active, plane 35 uses fb 56 allocated by fbcon, XRGB8888 (`XR24`), pitch 1920, GEM allocation 692224 bytes. fb0 maps 691200 visible bytes. The boot driver's safe diagnostics report GEM DMA and OVL scanout both `0x84900000`, match=1. The fbdev `smem_start` and generic GEM debug `start` report zero; those fields must not be interpreted as the live DMA address.

Boot vblank samples advance 18→86→154→221. Live IRQ/state snapshots were retained; no generic live vblank counter file exists in this build. fbcon vtcon1 is bound. Backlight reports brightness/actual/max 32. fb0 initially reports blank=4 while the DRM CRTC is active. Writing 0 through its supported sysfs interface succeeds; the explicit live pattern checksum matches `a40f4cc5` and the owner confirms physical visibility. Consoleblank is already zero; a timeout is not established as the original cause. A later startup-helper check mismatches with fbcon cursor active. Two checks with the cursor temporarily hidden pass, as does the revised startup helper. Cursor hiding/restoration now brackets the checksum in canonical S25y2-pattern. No new display kernel is required for this correction.

## USB failure and next evidence boundary

`reconnect-events.json` starts with uptime 1595.34 seconds and a tmpfs continuity token, then records physical USB removal. The host kernel records removal of device 22 and cdc_ether. After the owner confirms reconnect, no new Y2 USB device appears and repeated bounded SSH attempts time out. The owner says it works only after restarting. The owner then explicitly restarted the Y2. USB device23 and SSH return with uptime33.32s and the original tmpfs token missing; the monitor correctly rejects boot continuity. Its old parser puts the next uname line in the missing-token field, so that literal field is not a boot token; fixed parsing now emits MISSING. The470.29s host absence includes waiting and the owner restart, not a controlled 10-second successful reconnect. No second unplug cycle follows.

The exact running adapter in `kernel/usb/y2_musb.c` polls PMIC presence, detaches the MUSB controller and restores digital session inputs, then gates re-entry on power/clock/PHY/DMA state. A failed gate becomes terminal teardown. Host evidence localizes the problem before networking, but cannot distinguish a failed guard, disconnect callback/lifecycle failure, missing pullup or lost device execution. Existing fixtures substitute upstream callbacks and cannot prove this hardware path. Do not remove the safety guards or invent a register correction from the host timeout. A recovered device-side detach/reconnect log/status is the next smallest evidence boundary; a USB-focused integrated DEV-03 may then be justified. No BOOTIMG was prepared merely to add diagnostics missing from userspace.

## Reproducible userspace changes and remaining validation
  - S00y2-runtime remounts inherited `/run` with nosuid/nodev and explicitly chmods

its existing root inode to 0755; devpts is remounted gid=5/mode=620/ptmxmode=0666. The explicit chmod was added after live verification showed remount alone leaves `/run` at 1777. Final live mode is 0755.
  - S25y2-pattern explicitly unblanks fb0 before the development pattern. The

later checksum mismatch and subsequent cursor correction are retained above.
  - The already-built, hash-validated DEV-02 module archive updates `/display.ko`

and `/lib/modules/6.18.0-y2linux-dev02`, followed by depmod. modinfo now finds the matching vermagic; the active module was not unloaded/reloaded. The canonical post-build script already installs and indexes that exact version.
  - The comprehensive collector and completed bounded memory helper are installed

live and represented in the Buildroot overlay. Update manifests and live SHA-256 readbacks are retained. Runtime capture files/token in `/tmp` are test artifacts, not persistent configuration.
  - Host NetworkManager now persists the verified Y2 interface's `10.42.0.2/24`

address, MAC restriction and no-default-route policy. A Y2-specific udev uaccess rule is installed. Both have canonical helpers under tools/development; After the owner restart, the static profile reconnects automatically and the rule permits real ACM transfer; this does not turn the failed no-reboot test into a pass.
  - Next Buildroot configuration adds evtest, libdrm test utilities (modetest),

setterm, BusyBox timeout and a 2048-byte syslog input buffer. Current syslog truncates long kernel records at its 256-byte input limit; complete dmesg is retained independently. Those package changes were not rebuilt/deployed.

Real Buildroot defconfig resolution preserves all planned diagnostic selections. Targeted shell/Python syntax, archive hash/path checks and the existing removable root-selection rejection test pass. Live readbacks verify the applied module and runtime corrections. Whole-tree whitespace checking reports pre-existing patch context whitespace in `0008-mt6582-i2c.patch`; that unrelated work is preserved. The owner restart revalidates persistent Buildroot, runtime mount permissions, module indexing, key identity and automatic host network setup. No assistant reboot or controlled clean-shutdown test was performed. `/var/log` points into volatile `/tmp`, so old kernel logs cannot be recovered after restart. The new `y2-usb-record` helper is explicitly invoked, bounded to at most600seconds, checks removable Y2ROOT, and retains dmesg plus existing cached USB status on SD. Its five-second connected smoke test passes; it neither changes USB state nor starts automatically. A future targeted failure capture can use it without a new kernel.

## Roadmap decision

The satisfied narrow #22–26 research/bring-up issues are closed, with their remaining production/long-run concerns explicitly assigned to #29–32. Issues #27 and #28 remain open for USB reconnect recovery; optional physical UART #16 remains separate. After core reconnect qualification: M3 complete native audio; M4 full power; M5 Wi-Fi/Bluetooth; GPU/lima and final whole-platform qualification. Only then begin Y2PlayerNative. This newer owner gate supersedes the earlier wording that allowed the application workstream after only a wired-player vertical slice.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
