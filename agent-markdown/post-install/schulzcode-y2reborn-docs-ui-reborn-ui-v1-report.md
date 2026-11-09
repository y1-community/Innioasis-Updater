---
title: "Reborn UI v1 implementation and candidate report - Innioasis Updater"
description: "Reborn UI v1 implementation and candidate report Historical software receipt. Its unchanged candidate identities and owner-review status refer to that UI build. A later i"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-ui-reborn-ui-v1-report.html"
---

# Reborn UI v1 implementation and candidate report - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn UI v1 implementation and candidate report

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn UI v1 implementation and candidate report

Historical software receipt. Its unchanged candidate identities and owner-review status refer to that UI build. A later installed Fix01 image physically exercised real wheel/workload paths, but no separate visual, accessibility or analog playback acceptance was made. See [current application state](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2FCURRENT_REBORN_STATE.md) and the [Fix01 physical report](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-CPU-FINAL-FIX01-PHYSICAL-QUALIFICATION.md).

Status: software candidate ready for owner-controlled physical review. No device access, flash, push, history rewrite, identity change or platform implementation change occurred. Existing user documentation, untracked design/review material and historical asset-pack deletions remain outside these commits.

## 1–4. Repository and compiled identities``````````````

| Identity | Commit |
| --- | --- |
| 1. Starting Y2Linux | 8959c3439a2305934151141c7346c455460e0be7 |
| 2. Starting Y2Reborn | 5bab207ae662dafe31544fe5948f68e702ea33fa |
| 3. Final Y2Linux review HEAD | d6811ffed028e73d90a8b146e576310319734187 |
| 4. Final Y2Reborn review HEAD | Recorded in the sealed candidate metadata/final-heads.json and REPORT.md |
| Reborn compiled into this candidate | 155608393f6acfc6657f2f2e23cd07d0533479c6 |
| Platform source compiled into the retained base | d04b95aaff713edf943042d97a4c6134ca19fc24 |

The sealed candidate's `metadata/final-heads.json` records both final review HEADs. The tracked report cannot embed the hash of its own reporting commit; its sealed copy at `REPORT.md` resolves that identity. Documentation after the compiled commit does not alter application inputs. Kernel, rootfs release and platform build IDs remain those of the existing Platform v1 candidate, not the current documentation HEAD. About shows friendly releases before advanced IDs.

## 5–9. Architecture, navigation, physical input, focus and design

5. Architecture: AppModel → production UI → existing semantic Action → Effect → bounded service/runtime worker → observed result. Theme, components, catalog, platform presentation, navigation/modal state and artwork worker have distinct responsibilities. UI performs no ALSA/SQLite/BlueZ/sysfs/OTA writes. Platform JSON observation and fixed-argument operations use separate workers; live data is not persisted. The renderer retains GLES/DRM/GBM and dirty rendering.

6. Navigation: Home → Music / Now Playing / Queue / Connectivity / Settings. Music → Albums / Artists / Songs / Folders / Scan. Settings → Audio / Playback / Library / Connectivity / Storage / Display / Power / System. System → About / Update / Backup / Maintenance / Date & Time / Diagnostics. Detail views and context menus preserve collection/filter/focus/scroll on Back. The complete screen/focus/parent/child/context/empty-state map is in `REBORN-UI-V1-NAVIGATION.md`.

7. Input: wheel traverses the single focus path with existing acceleration; Select opens/toggles/accepts; long Select opens context or submits password; Back closes/restores parent; long Back returns Home outside overlays. Play/Pause, Previous/Next and Volume remain global; long Previous/Next emits existing ±30 s seek actions. Long Play opens Now Playing outside a focus trap. Power preserves the existing blank/wake and long-press menu policy. No second key mapper or touch interaction was added. Confirmed root apply/restore temporarily suppresses conflicting navigation/power/transport actions; wake and Volume remain available.

8. Focus: exactly one warm outline on interactive screens, enabled rows only, deterministic wheel order, modal traps and restored background focus. Screen-off wheel/Select/Back cannot move hidden focus. Boot and install preparation are intentionally noninteractive. Playing uses a triangle/state label; selected values and enabled/disabled states are distinct from focus.

9. Visual system: the complete extracted Simple asset pack was read, and all eight native references studied; no historical Android/old-player visual authority was used. Native layouts adapt the palette and minimal mood rather than paste PNGs. One theme owns #090B0D background, neutral panels, #F2F0EB text, #E7C98B accent, #FFE2A4 2 px focus and #201C16 focus fill. Type roles are 26/20/18/15/14/12 px; 16 px margins, 28 px status, 46 px rows on a 48 px pitch, five visible rows and 164 px Now Playing art. Licensed official DejaVu 2.37 glyphs and pack-derived monochrome SVG icons are pre-rasterized. Provenance and license files are retained.

## 10–14. Screen inventory and platform scope

10. Implemented: Startup, Home/Music, Albums/Album, Artists/Artist/Artist Albums, Songs, Folders, Letter Index, Now Playing, Queue, track/collection/queue contexts, Track Info, Quick Settings, Connectivity, Wi-Fi/network details/password/errors, Bluetooth/device pairing/codec/audio detail, PC Transfer; Settings/Audio/Playback/ Library/Display/Power/System/Storage/Date & Time/About/build IDs; Update/details/ result/confirmation, Backup/Export, six maintenance scopes; Diagnostics/Health/ Capabilities/CPU & Memory/Thermal & Power/Storage/Network/Bluetooth/Audio/USB/Update/ Boot & Services/Checks; full-value view, notices/volume, power and confirmation menus. Empty, long-data, loading, disabled, unavailable and failure variants share the same components. The preview manifest enumerates 69 representative states.

11. Replaced/removed: old screen composition, scattered styling, dense ASCII presentation, Now Playing wheel-volume behavior and flat system/settings discovery were replaced. Dead or unsupported normal controls are omitted. No decorative lock screen persists while the panel is off. No fake favorite, brightness, gain, filter, Airplane Mode, DND or ineffective EQ switch was added.

12. Capabilities exposed: current Wi-Fi readiness/IP/DNS, BlueZ peers and actual BlueALSA PCM/codec, wired output facts, storage/SD/space state, charging/voltage/source, clock trust, USB-only authenticated SFTP, signed root updater, backup/export, health and safe bounded checks. Capability implementation/enabled/qualification fields remain independent and are readable through Diagnostics.

13. Diagnostics exposed: Health; Capabilities; CPU cores/frequency/load; memory total/available/Reborn RSS/PSS/cache/slab; CPU/PMIC die/cooling; storage; Wi-Fi stage/IP/route/DNS/signal/traffic; Bluetooth peer/trust/reconnect/PCM; source, processing and sink audio; USB/cable/address/SFTP; update/journal/sequence/result; boot history/clean shutdown/stage and service readiness. Unknown reset reason, OTA key ID or USB activity stays unavailable when the API supplies no observation.

14. Gated/hidden: deep suspend/deeper idle, USB Host/OTG/UAC, S24/S32/preserved 24-bit and 88.2/96 kHz internal output, optional Bluetooth AAC/aptX/aptX HD/LDAC, advanced CS43131 controls, automatic BOOTIMG OTA and unsupported battery metrics. Diagnostics may name these with truthful unavailable/not-built/disabled/pending states. No platform driver, power, partition, Buildroot or OTA architecture changed.

## 15–25. Product behavior

15. Music: readable wheel lists, collection art/count/duration, track-specific contexts, separate artist album list, parent-preserving folders, fast title ordering and letter jumps. Missing metadata falls back to filename/Unknown. Partial scans retain validated music and show an incomplete status. Empty collections offer Scan instead of inactive playback actions. Durable favorites are unavailable in the model.

16. Now Playing: large real embedded/sidecar art, readable title/artist/album, elapsed/remaining and actual playback state. One wheel path: Options → Queue → Audio Info. Hardware transport indicators are informational. Technical source/sink facts live in Audio Info, not an invented main-screen output specification.

17. Queue: ordered occurrences, durations, Now Playing/Up Next/Played and repeat/shuffle. Context Play Now/Remove/future Move Up/Down/confirmed Clear Future uses QueueEntryId so duplicates remain distinct. Current removal and invalid moves are disabled. No drag handles.

18. Wi-Fi: Off/Starting/Scanning/Associating/Authenticated/Acquiring IP/Online/ Failed are distinct. Saved networks merge with current scans; signal/security and errors are readable. Open/WPA-PSK connections use the service and a physical rotary password editor; unsupported WEP/EAP/SAE-only networks are disabled. Authentication alone never becomes Online. Secrets are not rendered in plaintext.

19. Bluetooth: adapter and discovered/paired/connected peers, Pair/Connect/ Disconnect/Forget, named pairing confirmation with Cancel initially selected, connected-peer output selection and actual failure states. Existing AVRCP actions feed the same model and UI as local controls.

20. Codec: stored preference is separate from negotiated Active Codec. SBC is the built baseline; stopped playback and a connected audio peer are required for preference application. Auto is disabled without qualified eligible inventory. Active codec, PCM format/rate/channels are prominent in Bluetooth Audio. No optional codec is advertised as a production choice.

21. USB: PC Transfer explains authenticated USB-only SFTP, cable/ECM-derived state, readiness/address/key requirement, unavailable activity metrics and Storage. It explicitly excludes Wi-Fi exposure and never displays private authentication.

22. Storage: real internal/root/SD state, filesystem and used/free information, MiB below 1 GiB, clear missing/removed SD and low-space guidance. Advanced scratch benchmarks are separated and confirmed; no user-music benchmark writes.

23. Power: real charging/voltage/source and low-battery-policy observation. No SOC, runtime estimate, current or battery-temperature fiction. The status bar uses an uncalibrated icon and charging mark without a fabricated fill/percentage.

24. OTA: current release/journal/network, signed check/stage, verification state, queued install readiness, explicit install/restart and restore confirmation, previous result and advanced detail. State comes from the platform worker; no fake percentage or BOOTIMG promise. Busy install/restore traps conflicting actions and failure unlocks the route. This candidate is a preserving root-image review package, not a newly signed update-channel release.

25. Diagnostics: an advanced, readable hierarchy with full-value drill-down and 10-second observation refresh while relevant. Health refresh, passive Network Check, confirmed 16 MiB/64-operation scratch Storage Benchmark and 1k scratch Library Benchmark use platform tools. No suspend/power/VBUS/OTA-failure experiments. Maintenance distinguishes all six reset scopes and their consequences, but execution requires the platform's authenticated USB stopped-service plan/digest flow. Starting a destructive reset from a running UI would violate that current contract.

## 26–28. Performance, memory and text

26. Performance: only visible rows are formatted; catalog identities are cached. Wheel steps do not clone every Track or rebuild the whole library. Navigation avoids transactional full-model copies; necessary playback transactions preserve existing engine semantics. Expensive art decode and platform/radio operations stay off the UI thread. No blur, continuous menu animation or constant marquee. Now Playing's position redraw is bounded to visible seconds; expired notices redraw once.

27. Memory/rendering: one 1024×1024 RGBA font texture (4 MiB), 192×160 icon atlas, bounded 160×160 artwork textures (100 KiB each), four-image collection cache (400 KiB) and one bounded art worker/channel. These are allocation bounds, not a claim that total RSS increases by only those amounts. Embedded atlas data, GPU storage and renderer/library allocations all need physical RSS/PSS review. Existing GLES and render-on-damage remain; no runtime SVG/font engine was introduced.

28. Text: proportional measured ellipsis, wrapped detail/dialog text, bounded 1024-character processing and checked atlas indices. The 1001-glyph set supports Latin/extended Latin, Greek, Cyrillic and useful punctuation. Unsupported scripts, combining/shaping cases and CJK use bounded replacement glyphs; no atlas overrun. The letter index uses A–Z and `#`, not locale-aware collation. No constant marquee.

## 29–33. Fresh validation

29. Added tests: full-route wheel reachability/single focus/Back restoration, modal trapping and global controls, screen-off policy, QueueEntryId context identity, update confirmation/live gating/conflict lock, unavailable codec/radio states, source-vs-sink/power/clock truth, storage/SD/USB errors, long Unicode bounds, password/pairing globals, letter jumps after library replacement, notice expiry, transient-state persistence, empty collection recovery, artwork source/mount identity, platform JSON/deadline/error handling, partial-scan daemon behavior and safe package selection/atlas provenance/native preview size.

30. Results:`cargo fmt --all -- --check` PASS; `cargo clippy --workspace --all-targets --locked`PASS without warnings;`cargo test --workspace --locked` 177 PASS, including 29 UI tests. Relevant Linux contract/Bluetooth/network-time/ power/update/transfer/storage/maintenance regressions: 54 PASS. Existing tooling: 4 PASS. New UI/package tests: 4 PASS. Fresh host daemon: 20 checks PASS. All logs are copied into candidate `validation/`; no physical success is inferred.

31. Preview: fresh host renderer produced 69 individual 480×360 images and a native-scale contact sheet. All important screens/states were visually inspected through three passes; final additions and changed layouts were inspected again. Focus counts are asserted in the production draw fixtures. The sample album art is preview-only and absent from the installed player ELF/root.

32. ARM: clean target directory with the exact existing Platform v1 Buildroot SDK, Cortex-A7/NEON/hard-float, locked offline workspace release build PASS. Installed ELF32 ARM binaries and dynamic dependencies PASS. The packaged root's loader/control/decoder/database/library/security checks PASS (eight QEMU checks). Host and packaged ARM-emulated 1k/10k/20k library/128-wheel-action runs all pass SQLite quick-check. Timings are host/emulation evidence, not physical performance.

33. Package: exact manifest-verified base, app/media/control/benchmark ELF replacement, app version/provenance/license overlay only. Kernel, platform services, capabilities, init and updater remain unchanged. Image readback matches installed inputs, ext4 checks pass, Y2ROOT UUID/512 MiB geometry remains. GLES/GBM/DRM dependencies are present; FFmpeg remains lazy via the native bridge. Preview executable, sample music art, software rasterizer, replacement user state and owner SSH material are excluded. Only ANDROID is selected, with exact base-root fallback and no BOOTIMG payload. Final source bundles, receipts, metadata and SHA256SUMS are provided.

## 34–38. Commits, deliverables and hashes

34. Local commits: Linux has activation, bounded-memory, candidate-admission and handoff audits only. Reborn has the core native UI/Platform binding, partial-scan/SOC correction, capability/PCM/letter hardening, empty collection recovery, Clippy cleanup, readable capability labels, preserving packager/tests, 69 previews/docs and final handoff report. Exact ranges/titles are sealed in `metadata/local-commits.json`. No commits were pushed and the configured/existing author identity was preserved.

35. Previews:`docs/ui/previews/v1/`, including `contact-sheet.png`, individual native PNGs, README and hash/review manifest.

36. Documents:`docs/ui/REBORN-UI-V1.md`, `REBORN-UI-V1-NAVIGATION.md`, `REBORN-UI-V1-QUALIFICATION.md`, this report and preview provenance. Linux roadmap and gap audit record every application boundary without promoting hardware gates.

37. Candidate:`/home/luca/Dokumente/Code/Y2Linux/out/y2linux-reborn-ui-v1-candidate/`. The initial superseded package is separately retained as `...-candidate-initial/`. Fresh build tree: `.../out/y2linux-reborn-ui-v1-build-sealed/`.

38. SHA-256:``````````````

| Artifact | SHA-256 |
| --- | --- |
| Y2ROOT.img | edcecfaae26b8102c071000b5d2e9e5f84626ad08e3ff5818b050174f301a044 |
| fallback/Y2ROOT.img | 970330d24f6a0bddb0cb685d37232b298566c5cd7025a45990566f03c3f66fa3 |
| Required installed Platform v1 BOOTIMG | f7b4a950a0504a411ad72db0aac9398f04dc1ccabd6a6a0a3a7fdab198ca2622 |
| usr/bin/reborn | 2ff167a511f14fc8e3ac9e08b46ce3c8112788059363d25f5bbc84c27c7f9521 |
| usr/bin/rebornctl | bbabf8df84f48b21bab860e1cfc84f33098cd755d769d365d80b3370b58bc30c |
| usr/bin/reborn-bench | a4af4e2f8cabd52d64a44abf3baaf8d99b66225014b2543448b12956463fc653 |
| usr/lib/reborn/libreborn_media.so | 2e5813fad9977b18b2792756fb0ad4953a97aa56ccc2d449808817e34a20fce8 |

The required BOOTIMG is a compatibility prerequisite, not an included/selected payload. `SHA256SUMS` covers every sealed candidate file; `manifest.json` records image geometry, ELF identities, replaced files and preserved platform identities.

## 39–40. Remaining limits and physical qualification

39. Remaining UI limits: unsupported scripts use a safe replacement glyph; password entry supports the existing ASCII WPA-PSK contract; no durable favorites, brightness API, useful configurable EQ or decorative lock view exists. Reset scopes are informative owner-maintenance flows rather than unsafe in-app reset execution. OTA key ID and active USB transfer counts are unavailable unless the platform actually exposes them. Unknown services/clock/power remain explicit. Collection index building and existing transactional playback/queue work can scale with collection size; wheel navigation itself is cached. Precise target memory, rendering, input latency, audio coexistence and endurance are unqualified.

40. Owner review required: exact root/BOOT identities and recovery prerequisites, physical legibility/contrast/focus, all wheel/Back/context paths, real artwork and long metadata, large libraries and queue occurrences, screen off/wake and global transport/volume, Wi-Fi DHCP/DNS/error transitions, Bluetooth pairing/SBC/PCM/AVRCP, USB transfer/reconnect, SD/storage/low-space, OTA and recovery observation, every advanced diagnostic and safe action. Use `REBORN-UI-V1-QUALIFICATION.md` with the Platform v1 owner sessions. No screenshot or emulated success closes those gates.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
