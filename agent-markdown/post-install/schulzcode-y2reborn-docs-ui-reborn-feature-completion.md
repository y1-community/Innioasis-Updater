---
title: "Product v2 feature-completion controls - Innioasis Updater"
description: "Product v2 feature-completion controls <!-- knowledge-base-scope: source-contract -- This pass extends Product v2. It does not claim physical sleep, codec or audio qualif"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-ui-reborn-feature-completion.html"
---

# Product v2 feature-completion controls - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Product v2 feature-completion controls

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Product v2 feature-completion controls

This pass extends Product v2. It does not claim physical sleep, codec or audio qualification. Current output capabilities still come from the platform.
  - Audio → Equalizer: enable the existing FFmpeg EQ/limiter, edit five broad

bands at 60/250/1000/4000/12000 Hz, or reset to flat. Each wheel detent changes the candidate gain by 1 dB, bounded to ±12 dB. Select applies; Back cancels. Values are persisted with the existing settings. Playback uses its existing transactional reconfiguration and rollback. Reset Settings now also removes an active EQ from the running pipeline.
  - Audio → Output Details: source codec/bits/rate, decoder/DSP precision and

the accepted PCM format/rate live in Diagnostics. The accepted PCM container is not proof of the DAC's meaningful payload bits.
  - System → Sleep and Quick Settings → Sleep: deliberate sleep is

distinct from a short Power press, which blanks the display while retaining playback. Playing/buffering refuses sleep with a Pause action explanation. The platform owns admission; current software refuses ordinary deep sleep until same-boot physical qualification is complete. Requested, refused, sleeping, restoring, restored and restore-failed are typed product states. A restored claim additionally needs same_boot=true and kernel_completed=true.
  - Bluetooth: codec preference and the observed device codec remain separate.

A paused player can now select a codec; there is no hidden requirement to use a command-line Stop action. Existing transport and PCM lease guards remain. Optional choices require the current enabled/mutual capability set, discovered read-only when the transport first appears. The saved preference is attempted once per observed connection after playback is paused/stopped; replacement PCM objects do not retrigger it. SBC-only peers still expose their quality setting. SBC quality and LDAC quality/Auto Rate controls use the platform's supported settings. Saved changes say restart required; Diagnostics distinguishes saved values from the current daemon's startup receipt. LDAC quality labels give both rate families: 303/330, 606/660, 909/990 kbps. ABR enabled is a control state, not evidence that adaptation has been observed.
  - Diagnostics → Export Diagnostic Report: creates the platform's redacted

shareable report, then opens Latest Result with its archive path and retrieval instruction. Export Player Data is explicitly a private backup.
  - Battery: voltage-derived percentage is labelled Estimated Charge.

No current, coulomb or battery temperature measurements are invented.

The ready-frame boot handoff and black-frame/backlight-off shutdown sequence from the entry source remain in use. The wheel's input duplicate suppression, acceleration and direction-reset logic is unchanged; the EQ picker uses the existing one-detent value policy. Long modal lists now compute visible rows from the actual description height so the focused row remains on screen.

Validation: `cargo fmt --all -- --check`, strict workspace clippy and 238 workspace tests passed, including API-boundary, shutdown and input tests. `reborn-preview` emits 69 deterministic native-resolution cases; the new EQ, long EQ picker, sleep refusal and LDAC settings cases were rendered and viewed. These fixtures are presentation validation, not observations from a device.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
