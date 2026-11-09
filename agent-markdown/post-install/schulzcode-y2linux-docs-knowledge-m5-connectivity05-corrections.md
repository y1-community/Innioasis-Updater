---
title: "CONNECTIVITY-05: frame the first WMT command over BTIF - Innioasis Updater"
description: "CONNECTIVITY-05: frame the first WMT command over BTIF <!-- knowledge-base-scope: retained-research-/-scoped-evidence -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-knowledge-m5-connectivity05-corrections.html"
---

# CONNECTIVITY-05: frame the first WMT command over BTIF - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# CONNECTIVITY-05: frame the first WMT command over BTIF

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# CONNECTIVITY-05: frame the first WMT command over BTIF > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../CURRENT_PLATFORM_STATE.md) for the latest physically observed result. 

CONNECTIVITY-04 completes this unit's MD calibration (`FS=841`, restore and shutdown successful), verifies the corrected EMI remap and reads CONN chip `6582`. It remains alive over 813 seconds, including a bounded runtime recovery, with the same boot ID and no observed Oops/panic. The first WMT register read times out after four seconds. All BTIF/DMA interrupt counters are zero; no Wi-Fi interface or usable BlueZ adapter exists. This does not establish radio readiness.

## Targeted correction

The native bootstrap sent the 20-byte WMT chip-read command directly to BTIF. Stock `wmt_core_stp_init` first selects BTIF mandatory STP mode (mode bit 3), enables it, and then reads the chip register. Despite its name, `wmt_core_reg_rw_raw` calls `wmt_core_tx` with bRawFlag=false. Donor `mtk_wcn_stp_send_data` sends a four-byte STP header and two-byte trailer even in mandatory mode; only sequence/ACK, header checksum and CRC are disabled. The required first packet is 26 bytes, not 20.

CONNECTIVITY-05 frames bootstrap requests accordingly and parses replies using their outer STP length. The inner WMT register-read length quirk remains limited to the outstanding register command. Mandatory-mode replies have no transport ACK. The existing negotiated full-mode CRC, ACK window and bounded retries stay active after the mode switch. No HCI traffic is accepted before that switch.

BTIF FIFO clear bits are explicitly released before DMA starts, matching the donor reset pulse convention. This is an initialization correction; it is not claimed as a separately proven cause of the physical timeout. A WMT timeout now records its opcode/mode and bounded BTIF/DMA control, occupancy and FIFO-pointer values before shutdown. No payload, calibration, address identity or DMA buffer address is logged. Clock ownership, I2C DMA channels and M4 policy are unchanged.

## Validation and scope

The regression executes the production STP send/receive functions: exact stock bootstrap bytes, every reply split, one-byte fragments, disabled checksum/CRC, the bounded register-event quirk, malformed frames, send failure, mandatory-to-full transition, full-mode CRC rejection and duplicate suppression. It rejects the previous bare-command implementation at the first wire-packet assertion.

Build a normal production BOOTIMG update retaining CONNECTIVITY-03 Y2ROOT and all Y2DATA. The fallback is CONNECTIVITY-04 with that same root; its bounded Linux stability is observed, but its radios remain unavailable. Do not recommend the crashing CONNECTIVITY-03 BOOTIMG as recovery. No new firmware acquisition, factory writes, memory layout change or broad milestone audit is involved.

After owner installation, first capture WMT versions/patch/calibration progress and interface availability. Continue the existing M5 qualification only as those gates pass. The new framing is source/test verified, not yet physically proven.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
