---
title: "Power evidence and reporting discrepancy - Innioasis Updater"
description: "Power evidence and reporting discrepancy <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-power.html"
---

# Power evidence and reporting discrepancy - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Power evidence and reporting discrepancy

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Power evidence and reporting discrepancy > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

2026-09-10: [additional evidence](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Freverse-engineering-audit.md) explains the donor wrapper-IRQ omission as an unresolved storm workaround, separate from PMIC EINT25. Final donor DT includes an MFD despite older minimal-PMIC prose. VGP2 brownout is a useful M3 supply lead; charging settings and inherited rail enables do not resolve our telemetry/calibration gaps. One USB/regmap owner first.

Date: 2026-09-08. Related tasks: Y2E-101/105. Status: power baseline incomplete.

CONFIRMED historical observation: `pmic_mt6323`, battery and battery-meter platform nodes in the verified 2026-07-29 snapshot. Current CPU topology and `/proc/meminfo` were captured, but governor/idle/power behavior was not measured.

CONFIRMED current observation: `dumpsys battery` in `20260908-stock/battery.stdout` returns conflicting repeated fields: status 5 and 4, present true and false, level 100 and 50. It also reports USB powered, voltage 4237 and temperature 250. Do not select one duplicate or promote these service values into validated physical battery voltage/temperature/charge state. The cause could be service modification or reporting logic; it has not been established.

UNKNOWN: trusted power_supply values/units, gauge/charger identity and calibration, battery health, safe charging limits, thermal sensor mapping, cpufreq/cpuidle, runtime PM, suspend/resume and wake sources. The service anomaly blocks a trustworthy recovery-power precondition, not all passive research.

Next proof: inspect the source of duplicated framework output and narrowly selected standard power_supply metadata without changing charge, suspend, governor or display state. Do not read arbitrary vendor debug/register files merely because they are exposed under sysfs.

## M2 USB supply prerequisite — 2026-09-09

Source/binary CONFIRMED: FM uses AP PWRAP WACS2 at physical `0x1000d000` to read MT6323 CID (`0x0100`) and VUSB (`0x0502`); the latter's software enable is bit 14 and reported enable bit 15. The USB init requests fixed 3.3 V VUSB. This is an internal USB supply and does not establish host VBUS sourcing. [Exact locators, guards and candidate contract](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-pwrap-probe.md).

Hardware status remains UNKNOWN after normal Linux handoff. One bounded identity/status candidate is specified to use only inherited initialization and PMIC read commands, never rail/charger writes. It must refuse a missing/busy transport and mismatched chip identity. Full PWRAP provider initialization, shared input/display/SD rail ownership and battery/charger telemetry remain open under #23; the conflicting Android battery fields above remain unresolved. There is no evidence that a VUSB enable report measures actual supply voltage or satisfies the basic battery/charger reporting required for M2 exit.

## Returned M2-PWRAP-01 hardware evidence

[Owner photographs](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-pwrap-hardware-result.md) confirm RC=0/VALID=3, CID=0x2023, VUSB=0xc000 and continued execution through BEAT 50. This resolves the narrow inherited AP read-transport/VUSB-enable observation for this boot. It is one cached snapshot, not repeated sampling, voltage measurement or battery telemetry. Earlier pending/unknown statements describe the original handoff. Next: [read-only USB clock handoff snapshot](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-clock-probe.md), with the source-identified timer IRQ-name parser correction. USB ownership remains blocked.

## Clock hardware result and next USB prerequisite — 2026-09-09

The [clock trial](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-clock-hardware-result.md) confirms another successful PWRAP CID/VUSB snapshot and enabled inherited USB clocks, with no reported errors through BEAT 50. Supply voltage, consumer regulator control and battery/charger telemetry remain unqualified. [Next read-only USB state probe](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-state-probe.md) preserves the inherited rail/PLL state; it makes no PMIC/clock/calibration write.

## USB state result / bounded PHY wake — 2026-09-09

[Returned USB-state photos](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-usb-state-hardware-result.md) confirm all 21 MAC/digital-PHY/DMA reads, disconnected B-device state, eight zero DMA controls, PHY force_suspendm=1/value=0 and BEAT 50 without errors. This is one cached snapshot, not DMA ownership or a USB enumeration result. The next [guarded PHY wake](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fknowledge%2Fm2-phy-wake-probe.md) checks remaining mode controls and conditionally clears only the suspend-force bit. Calibration/analog controls, clocks, VBUS forcing, controller connection and DMA remain unchanged. The candidate must stop for owner testing; full USB/clock-provider/PHY/VBUS/FIFO/IRQ/ DMA contract, host logging and M2 exit remain unqualified.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
