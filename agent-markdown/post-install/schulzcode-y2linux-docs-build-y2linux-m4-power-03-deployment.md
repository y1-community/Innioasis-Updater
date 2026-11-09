---
title: "M4-POWER-03 — manual deployment and physical qualification - Innioasis Updater"
description: "M4-POWER-03 — manual deployment and physical qualification <!-- knowledge-base-scope: historical-build/deployment-receipt -- Historical record. The dates, candidate ident"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-build-y2linux-m4-power-03-deployment.html"
---

# M4-POWER-03 — manual deployment and physical qualification - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# M4-POWER-03 — manual deployment and physical qualification

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# M4-POWER-03 — manual deployment and physical qualification > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

Built and host-validated; M4 remains OPEN. No physical deployment was performed. The owner requested this focused M4 completion pass. M5 stays stopped.

Source: `16875c4acc813b54c781167883227cf289f4dfcd`. Kernel: `6.18.0-y2linux-m4-power-03`. Package: `/home/luca/Dokumente/Code/Y2Linux/out/y2linux-m4-power-03/`.````````

| Artifact | Bytes | SHA256 |
| --- | --- | --- |
| BOOTIMG.img | 5408768 | 66b6ecd5ef54da6f3ea07be2c9deda284d0a7636e9c6da4c5d72d84eca5fc010 |
| fallback/BOOTIMG-previous.img — POWER-02 | 5378048 | 1852dfc995953f86ef5c47349515e8d6f06478daa6c1a89efe0f223501c226c9 |

BOOTIMG changes; Y2ROOT and Y2DATA require no update or migration. The kernel, display module and current rescue executables are in BOOTIMG. Buildroot libraries/rootfs remain the retained Storage04/06 ABI. The retained packaged Y2ROOT identity is 536870912 bytes, SHA256 `814a5b2543931e01cee2eb6f641c3b6e02317bd6308d2d663aea78f618bd554f`; this is not a new live-root hash. Owner SSH authorization and data stay intact. The installed S20 USB workaround matches POWER-02 only and does not pin POWER-03.

The fallback restores the current bootable platform **with its known charging faults**. It is not a qualified charging or depleted-battery recovery solution. Older fallback images remain retained in their original packages.

## Changes and limits

[Full source decisions and retained-stock references](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm4-end-user-power.md%23power-03-correction-of-observed-failures--2026-09-15&anchor=power-03-correction-of-observed-failures--2026-09-15).

| Area | Candidate behavior; physical acceptance pending |
| --- | --- |
| PC SDP | 450 mA after a configured 500-mA allowance; 70 mA within a 100-mA allowance; inhibit below that during USB reset/suspend |
| CDP / DCP wall / detected Apple source | At most 650 mA, based on owned BC1.1 detection; no data enumeration needed |
| Unknown / nonstandard / unenumberated SDP | Conservative 70 mA, subject to the source policy |
| Low voltage | Below 3.2 V: at most 70 mA; up to 3.4 V: at most 450 mA; retain factory UVLO/ULC and presence protections |
| CV / normal stop | CV 4.175 V; stop engines on the first ADC sample at or above 4.175 V |
| Completion | A previously active cycle completes after six engine-off confirmations over 60 seconds at 4.110–<4.200 V. High voltage at insertion alone enters hold. This is conservative voltage-limited termination, without measured taper current or SOC |
| Recharge | Below 4.110 V continuously for 60 seconds; threshold noise restarts the interval. A completed cycle can start a new maintenance-cycle budget |
| Safety | The 4.2-V software guard stays fail-closed; exact stock 4.3-V battery OVP selector, enable/detector retained; first-fault registers retained before inhibit |
| Fault recovery | Verified physical removal, successful engine stop and safe recovered samples below the target; no clearing through manual auto, USB reset or voltage relaxation with cable attached |
| Watchdog / timers | One-second kernel service, four-second hardware watchdog; late service inhibits; stock 3-hour top-off / 24-hour total limits plus bounded precharge |
| Offline | Native activity/status display, no percentage; blank after eight seconds; brief Power shows status; two-second hold and release requests normal boot after three valid samples at least 3.4 V |
| Offline services | Charger/watchdog/input/display in RAM rescue; storage/audio probes gated. No Buildroot, SSH or ECM. Minimal listener-free ACM can obtain a PC charging allowance |
| Removal / shutdown | Offline removal requests PMIC hardware-off; plugged-in normal poweroff is expected to return through LK into offline mode. Actual behavior must be proved |
| Suspend | Existing exact-stock PCM CPU/cluster shutdown with infrastructure retained; s2idle fallback. Active charging blocks deep suspend to preserve watchdog service; screen-off charging continues |
| RTC | Correct stock 1968 epoch for time/alarm; reserved/spare fields preserved; RTC supplies boot time. The agent sets current UTC through normal APIs after deployment |
| Thermal | Scoped 32-bit thermal efuse reads, reject observed byte truncation; no default calibration or invented pack temperature |
| Frequency | 598 / 747.5 / 1040 MHz at the stock-proven 1.15 V; normal schedutil, offline powersave. No evidenced lower active voltage exists in retained Y2 tables |
| USB | Kernel runtime reference spans an attached session; release after detach; runtime resume before reentry. IRQ storm protection remains |

Host validation: 74 production/M4 tests passed, actual ARM rescue ABI and shell checks, emitted DT/config/memory/BOOTIMG validation, package validation and 12 package rejection cases. [Build receipt](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fbuild%2Fevidence%2Fy2linux-m4-power-03%2FREADME.md). These checks do not prove charging gain, temperature accuracy or physical suspend.

## Owner deployment — BOOTIMG only
  - Open the established SP Flash Tool and select the package's

`MT6582_BOOTIMG_only_scatter.txt`.
  - Choose Download Only. Select BOOTIMG → this package's `BOOTIMG.img`.

Every other row stays unchecked, including PRELOADER, LK/UBOOT, partition tables, recovery, ANDROID/Y2ROOT, USRDATA/Y2DATA and protected calibration. Do not use Format or Firmware Upgrade.
  - Perform the established manual connection/flash procedure and wait for SPFT

success. Disconnect the flashing cable and leave the Y2 off.
  - Connect a wall charger without pressing Power. Observe the charging display

and the eight-second timeout. Brief Power should show status again.
  - Hold Power for two seconds and release to request normal boot. This must

not auto-boot merely because charge voltage rises. Then connect the PC USB cable for the existing `root@10.42.0.1` SSH connection and report it running.

If the battery is too low for intentional boot, remain in attended offline charging. Do not repeatedly force normal boot. Kernel charge history is retained for retrieval after normal handover. Failure to gain voltage remains an M4 failure.

Fallback installation uses the same Download Only / BOOTIMG-only selection, choosing `fallback/BOOTIMG-previous.img`; root/data remain untouched.

Stop here for owner deployment. The following session starts only after the owner reports the candidate running. The agent performs commands over SSH; the owner handles cables, Power, audible/visible checks and available accessories.

## One coherent physical session
  - Identity and initial offline result. Verify release and complete BOOTIMG

image-length readback. Collect boot metadata, retained offline/charger logs, source policy, new fault snapshots and USB runtime state. Confirm no Buildroot or ECM before deliberate normal handover. Record actual animation/blanking. Save private raw evidence, boot ID, session/process identity and root/data sentinels with `tools/development/qualify-m4-power.sh begin`.
  - RTC and thermal before load. Inspect the corrected date, preserve existing

alarms, set/read host UTC using the helper's `rtc-set` phase. Reconcile fresh full-word thermal acquisition, idle values and ambient conditions. Compare CPU and PMIC response; do not proceed with load while values are implausible.
  - Sustained charging. Use a detached bounded recorder on Y2DATA while the

owner changes sources: PC, wall, power bank if available, removal/reconnect. Observe at least 10–15 minutes per available main source when still below termination voltage; verify useful gain, configured limits, source identity, watchdog, faults and no resets. At the upper voltage, follow real hold, termination and later recharge; do not clear faults or alter thresholds to simulate success. A charger source need not provide a USB host.
  - Frequency and cooling. Test all three OPPs for three rounds with bounded

load and readback, restoring schedutil afterward. Guard temperature and voltage throughout. Record actual thermal response and cpufreq cooling constraints; a separately commanded cooling state is a policy test, not an observed high-temperature event. Do not intentionally provoke a hardware overtemperature shutdown. Record WFI usage and screen-off charging behavior.
  - Sleep, two distinct wake sources. Verify charging-active suspend is safely

rejected. Run s2idle, then deep Power wake, then deep RTC wake. Detached helper phases allow a 15-second cable-removal window; no SSH command needs to stay connected. For deep require incremented entries and actual `cpu_resume` count, at least two seconds of PCM residency, unchanged boot ID/process, identical mounts/sentinels and no broken PCM state. RTC wake must occur after its intended alarm interval. USB reconnection after waking must return SSH. Repeat the deep pair to expose warm-context and transport failures.
  - Resume regression. Display/backlight, Power/volume/buttons/wheel, quiet

44.1-kHz ALSA/CS43131 playback, internal root/data writes and hashes, available external SD files, USB and charging state. The owner confirms visible/audible behavior and operates inputs; the agent captures events. Screen-off by itself must preserve active audio. No mounted-filesystem fsck or protected writes.
  - Reboot and hardware-off. Ordinary reboot must yield a new boot ID and

persistent RTC/data. Poweroff with the charger connected must enter offline charging, without normal services. Offline unplug must power off; reinsertion must return offline. With no charger, normal poweroff must stay off until an ordinary Power press starts a new boot. Use boot reason/session history and observed absence of spontaneous reboot; a black display alone does not pass. Record electrical off/current evidence if measuring equipment is available.
  - Low-battery recovery and completion. At an actually encountered low

battery, prove recovery in offline mode without Android and then deliberate normal boot. Do not force discharge past protection thresholds. If the physical voltage conditions for recovery or full/recharge have not occurred, those gates remain open. Neither synthetic tests nor an arbitrary short observation closes them. Retain bounded repeated cycles and inspect for crashes, stuck IRQs, storage errors and unexpected reboots.

Concrete failures lead to targeted corrections. There is no broad research or M5 implementation pass after deployment. M4 closes only after real acceptance; issue #30, roadmap, source/evidence commits and final artifact hashes then update together, with main pushed and the working tree clean.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
