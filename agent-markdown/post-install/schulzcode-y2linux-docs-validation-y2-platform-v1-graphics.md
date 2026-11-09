---
title: "Y2 Platform 1.0 GPU, display and graphics power pass - Innioasis Updater"
description: "Y2 Platform 1.0 GPU, display and graphics power pass Date: 2026-10-04. Isolated branch codex/platform-v1-graphics in both repositories. Linux base b5aea93 ; Reborn base b"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-validation-y2-platform-v1-graphics.html"
---

# Y2 Platform 1.0 GPU, display and graphics power pass - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Y2 Platform 1.0 GPU, display and graphics power pass

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Y2 Platform 1.0 GPU, display and graphics power pass

Date: 2026-10-04. Isolated branch `codex/platform-v1-graphics` in both repositories. Linux base `b5aea93`; Reborn base `b71b4688`. No main edits, push, flash or full system-suspend experiment. Admission follows the [standing audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md%23platform-10-graphics-pass-admission--2026-10-04&anchor=platform-10-graphics-pass-admission--2026-10-04).

## Architecture preserved

Mali-400 MP2 uses Linux Lima and the existing MFG genpd/CCF owners. Mesa Lima/kmsro renders GLES2 into GBM linear XRGB8888 buffers allocated by the Mediatek KMS device and shared through PRIME. EGL presents at native 480x360. There is no CPU framebuffer copy in product presentation. Reborn retains its shader program, quad VBO, shared font atlas, icons and two artwork texture handles. Framebuffer IDs attach to GBM buffers and are reused. A single outstanding page flip completes before the old front buffer is released; the wait is bounded to three seconds. The ordinary render path has no `glFinish`, readback or per-frame framebuffer allocation. Its explicit graphics self-test uses a small temporary FBO/readback for correctness only.

Runtime PM retains Lima's 200-ms autosuspend and initial-reference balancing. SPM owns the MFG domain sequence; userspace does not gate GPU/display clocks or alter PLLs, voltages, OPPs, reserved memory or CPU idle policy. Lima exposes `pm_runtime_force_suspend`/`pm_runtime_force_resume`; callback availability is separate from physical system-resume qualification, owned by another session.

## Redraw and scanout audit

The base main loop renders only with `dirty.render`, while the screen is on, at least 34 ms after its previous frame. The boot dissolve deliberately retains dirty state until its bounded transition completes. Input, notices, playback, artwork and visible platform changes can invalidate the UI. A static frame is retained for KMS scanout between invalidations. Full-frame composition on actual damage is preserved: this pass has no measured case for tiled damage tracking, extra framebuffers or a new compositor. The base renderer does repeat texture binds, uniform-location lookups and one draw call for each quad. Measured renderer CPU below supports the performance pass's existing batching work; this branch does not independently change that shared renderer.

The awake loop polls every 15 ms; screen-off polls every 50 ms. These are CPU wakeups, not necessarily GPU submissions. Audio/platform/control workers have independent lifetimes. C1/C2/C3 remain qualified only to their retained UART01 scope; remote observation and attached USB/radios can themselves prevent C3.

Fresh observations under the graphics session's exclusive non-blocking lock used installed Y2LINUX-BASELINE-02, compiled Linux `8584ccd8`, running Reborn `b71b4688`, kernel `6.18.0-y2linux-baseline-02`, root `2025.02.18-platform-v1.21`, release `1.0.0-baseline-candidate.2`, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0. The renderer reports Mesa 24.0.9 / Mali400 / GLES2 / EGL 1.4. Native XR24 480x360 scanout and Reborn framebuffer ownership were read back from DRM state.

| Product scenario | Duration | Frames | GPU runtime active / suspended | Reborn process CPU |
| --- | --- | --- | --- | --- |
| Paused Home, no injected input | 20.138 s | 25 (1.24 FPS) | 4,148 / 15,986 ms | 7.00% |
| Screen off, paused | 20.191 s | 0 | 0 / 20,191 ms | 5.65% |
| Home after blank/wake | 10.138 s | 15 (1.48 FPS) | 2,482 / 7,657 ms | 7.20% |
| Songs selection, 100 injected wheel events | 14.779 s | 113 (7.65 FPS) | 14,673 / 105 ms | 10.56% |

CPU is aggregate process time, including workers, as a percentage of one core. Runtime-active residence includes the 200-ms autosuspend delay; **20.6% active residence on static Home is not 20.6% GPU execution utilization**. The static redraw problem is independently reproduced on the stock application. Reborn's last-frame metric includes presentation wait and cannot measure CPU rendering alone. The last Songs frame took 8.568 ms wall time; missed-frame and context-loss counters did not increase in any measured window. This installed library has only three tracks: these wheel actions qualify selection/redraw responsiveness, not an overflowing large-list scroll or physical button-to-photon latency.

The parallel Reborn performance pass has a same-day hardware receipt from installed Baseline02 (`8584ccd8` / `b71b4688`, boot `27e6d684-3794-4490-95db-a489027cd4f4`, taint 0), using its instrumented base Reborn build and then restoring installed `b71b4688`. It observed **13 frames in 10.09 seconds** on both paused Home and paused Now Playing, with main-thread CPU 4.16% / 4.56%; screen-off produced zero frames in 10.08 seconds. These are the performance session's measurements, not fresh graphics-session readings. They establish a redundant-invalidation problem despite the dirty-render gate: base Wi-Fi/Bluetooth observations mark rendering dirty even when their visible view has not changed. That session already owns the corresponding event-loop, radio invalidation and renderer optimization changes. This branch does not duplicate or prematurely integrate its uncommitted work. Integration and its physical before/after results are a dependency of the final static-UI verdict. Raw peer receipt: `../Y2Reborn/out/performance/before/device/receipt.json` in the `platform-v1-reborn-performance` worktree pair.

The peer's instrumented native-render trace also supplies separate CPU and KMS wait measurements for its 10k-track product fixture: Songs has 1,072 frames, median renderer CPU 5.729 ms / nearest-rank p95 6.149 ms, median GL submission 4.333 ms and median presentation wait 11.872 ms. Home has 56 frames, median renderer CPU 7.469 ms / p95 11.728 ms. Instrumentation changes and the larger fixture distinguish these from this pass's stock-process percentages. The performance owner rejected that exploratory run's injected-input/playback latency due to observer/queue defects; only its rendering and idle observations are used here. [Peer baseline summary](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-graphics/peer-baseline.json) records binary/trace hashes and all screen aggregates. Renderer batching and poll scheduling remain that session's changes and acceptance responsibility. This pass's stock scanout/PM receipt does not qualify the performance candidate's changed `graphics.c`, shaders or batching path.

Earlier retained [GPU-01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fhardware-evidence%2F2026-09-18-gpu01%2FREADME.md) proves static EGL content with unchanged GPU active time and job IRQ counters, MFG off and runtime suspended over a five-second observation. Its 120-second workload produced 30.00 FPS, median 9.272 ms/p95 16.191 ms submit-to-present, 3.36% application CPU and CPU/PMIC peaks 49.6/48.637°C. That workload and image are historical; these figures are not new Reborn measurements or GPU-only time.

## Artwork: demonstrated cost and localized correction

Artwork already leaves the decoder as 160x160 RGBA (102,400 bytes). Decode runs outside the UI thread. The collection worker caches at most four outputs (409,600 pixel bytes), keyed by source/file revision/mount identity; stale route completions are ignored. Original full-size decoded frames are temporary, but JPEG conversion previously decoded the complete source before shrinking. The two GL texture handles persist; `glTexImage2D` defines their fixed-size contents when artwork arrives. Texture upload and eviction policy are unchanged because no measured upload bottleneck justified a new cache or GL mechanism.

Same generated 4096x4096 JPEG, twelve decode/scale calls per separate process, same `-O2` build and host FFmpeg n9.0.2, x86_64 Linux:``

| Measure | Base b71b4688 | Changed source | Difference |
| --- | --- | --- | --- |
| Median process CPU per decode/scale | 15.014719 ms | 3.992294 ms | 73.41% reduction |
| Peak process RSS | 76,396 KiB | 51,712 KiB | 24,684 KiB less |
| RGBA output | 102,400 bytes | 102,400 bytes | same dimensions |

RSS includes the executable/FFmpeg runtime; CPU time is decode plus scale, not texture upload, GPU time, device latency or battery energy. The simple color-block fixture establishes a real avoidable allocation/CPU cost, not performance for every album image.

The same fixture was then measured on the Y2, using one temporary Cortex-A7 helper and separate processes loading the installed native library or the new ARM library from `/run`. The stock Reborn application was not replaced. Twelve decodes per process, with CLOCK_PROCESS_CPUTIME_ID and getrusage, give:``

| On-device measure | Installed b71b4688 | Reduced JPEG decode |
| --- | --- | --- |
| Initial-order median decode/scale CPU | 491.569 ms | 75.555 ms |
| Initial-order peak process RSS | 30,044 KiB | 9,296 KiB |
| Reverse-order median decode/scale CPU | 492.637 ms | 75.332 ms |
| Reverse-order peak process RSS | 29,920 KiB | 9,320 KiB |

The reverse-order check starts and ends at the observed 1.3-GHz CPU frequency for both variants, confirming **84.71% lower CPU time and 20,600 KiB lower peak RSS**. Normal DVFS is retained; endpoint frequency reads do not prove every instant's clock. Both outputs are opaque 160x160 and their sampled pixels agree. This is artwork CPU/memory evidence, not a GL upload, playback transition, battery or GPU benchmark. A small 160x160 host JPEG remains byte-identical; median decode changes from 0.0512 to 0.0575 ms in the narrow host check.

A generated FLAC containing the same large JPEG also passes the changed native module's decoder-open/artwork path: twelve calls average 0.713 ms CPU for opening and 4.010 ms for artwork conversion, peak process RSS 47,348 KiB. This separate host check uses a different executable, so its RSS is not a before/after comparison. It provides no evidence for changing the existing metadata path.

Reborn commit `a2df691edfbb105a164e2f5f574b158ec5f81e6c` asks FFmpeg's MJPEG decoder to read parameters with `AVDISCARD_ALL`, then chooses its supported reduced IDCT while both decoded edges remain at least the requested side. Baseline/extended/progressive DCT profiles are eligible; small covers and unsupported profiles/decoders retain normal decoding. The FFmpeg decoder supplies parameter-only decoding; the selected reduction is bounded by `codec->max_lowres`. The pinned ARM build and actual decoding checks pass on the tested membrane. External images now use the same 16-Mipixel and one-decoder-thread limits as embedded artwork. Existing 16-MiB file and 32-MiB individual-allocation bounds remain. PNG/WebP still use their normal bounded decoder; no speculative alternative image decoder or lossy asset conversion is introduced.

The exact Baseline02 ARM SDK uses FFmpeg 9.0.2, verified from staging `libavutil/ffversion.h`, the `ffmpeg-9.0.2` build source and the target `libavutil.so` version string. The header predates this pass's ARM build. The earlier draft's 9.0.1 label was a documentation error. The [physical summary](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-graphics/physical.json) binds the tested changed native membrane and helper to their SHA-256 hashes. The device helper loaded installed FFmpeg dependencies but did not independently query their runtime version; no per-device library-version/hash identity is invented from the SDK. Installed Baseline02 identity and successful native execution are the physical scope. A Cortex-A7 QEMU execution of the changed membrane decodes the 4096x4096 fixture to correct opaque 160x160 pixels. Its timing/RSS are emulation measurements and are not device claims.

## Screen off, backlight and wake

Source preserves the existing transactional sequence: turn the backlight off, wait for any pending flip, disable the owned CRTC/bridge, retain GBM/EGL/current buffer, and set screen-off state. Rendering is suppressed while off. Wake restores the owned CRTC/mode/buffer before unblank; failed transitions roll back. Brightness maps the 10–100% product range to the driver's actual maximum using rounded-up nonzero levels. This pass does not alter the backlight range or panel power sequencing without a measured problem.

The fresh screen-off window reads CRTC enable/active 0/0, backlight `bl_power=4` and `actual_brightness=0`, unchanged OVL/DSI interrupt totals, Lima suspended and MFG `off-0`. DSI engine/digital, OVL, RDMA, SMI and GPU core clocks have zero enable count. The GPU core's configured rate remains 500.5 MHz when gated. Screen-on reads active native 480x360 scanout; 1,307 OVL interrupts over the 20.138-second static window are panel refresh, separate from the 25 UI frames. There is no evidence justifying a refresh-mode or panel self-refresh change.

Five off/on cycles restore native scanout and the retained context, with zero context losses. Graphics FBO/readback self-tests pass before and after the wake workload. Driver brightness readback passes at 10/50/100%: raw/actual 4/4, 16/16 and 32/32 against max 32. The original brightness and paused Home with screen off were verified after all tests, installed build and boot unchanged, taint 0. Temporary decoder files were removed and the shared lock released. Actual electrical display savings and absence of visible white flash were not measured remotely. Long-off content updates and forced EGL context loss are not qualified by these five retention cycles.

CPU0 WFI accumulates 19.524 s awake and 19.445 s off during the corresponding windows. C2/C3 accumulate no entries; the SPM dormant guard reports `topology` rejection with no restore failures. This SSH/attached-observer condition neither extends nor overturns retained UART01 C1/C2/C3 qualification. No CPU idle policy, secondary-core parking or UART ownership is changed by this pass. Off-process CPU remains 5.65%, so zero rendering does not establish whole-system deep idle.

The short Songs workload reads CPU 54.3→54.8°C and PMIC 52.146→52.731°C, after earlier sessions had already warmed the device. The separate large-image decoder benchmark reaches a sampled CPU 57.8°C. These are bounded observations without a cooled baseline, electrical measurement or thermal-endurance qualification.

## Product v2 boot and shutdown ownership

The early native splash retains DRM master and the boot frame/progress until Reborn has rendered a complete first frame. The explicit READY/RELEASED exchange allows Reborn to take master and modeset that frame; PRESENTED acknowledges successful scanout before the splash process retires its buffers. DRM-master release precedes Reborn's modeset. Reborn discards the retired splash's old CRTC buffer reference and runs its bounded dissolve. Protocol failures and disconnections preserve/reclaim splash ownership. Pixel tests compare the splash and Reborn handoff frame, progress phases and generated mark.

The installed boot's retained `/run/reborn-splash/events.jsonl` was read under the lock: splash visible 489 ms; progress reaches system-ready 24,960 ms; graphics-ready 25,346 ms; READY 25,423 ms; DRM splash released 25,453 ms; PRESENTED 25,466 ms, all recorded handoff errno values zero. These are real current-boot receipts, not a fresh cold boot initiated by this pass. They prove successful ownership/protocol progress; source/pixel tests cover the dissolve, while actual visual smoothness and absence of white flash remain unobserved.

On shutdown Reborn presents the closing transition, saves state and closes audio/database, presents black, waits one refresh, blanks the backlight and acknowledges. It retains the dark DRM buffer until exit. The platform also blanks before terminating an unacknowledged/hung Reborn, preventing a lit restored console buffer on that fallback path. Host tests cover both orders. Fresh physical cold-boot/shutdown visual timing and white-flash observation remain separate gates; no reboot/poweroff is needed for a source-only claim.

## Validation and evidence````

| Check | Result |
| --- | --- |
| Linux GPU, display, splash, power, runtime idle and shutdown contract | PASS, 68 tests |
| Cargo formatting | PASS |
| Strict workspace/all-targets clippy (-D warnings) | PASS |
| Reborn workspace tests | PASS, 238 tests |
| Native C membrane -Wall -Wextra -Werror | PASS |
| Generated artwork regression | PASS, 10 scenarios |
| ARM workspace release build, offline/locked, Cortex-A7 | PASS |
| Changed ARM membrane under Cortex-A7 QEMU | PASS, artwork correctness |
| Fresh physical GPU/display/runtime-PM/product scenarios | PASS for bounded screen-off, wake, brightness and selection; static redraw GAP |
| Native ARM artwork before/after on Y2 | PASS, 84.71% CPU reduction in reverse-order check |
| Full system suspend / electrical power / long thermal endurance | Outside this pass; no new qualification |

Artwork regression covers small/big/rectangular baseline and progressive JPEG, ordinary PNG/WebP, a valid 25-Mpixel PNG rejection and truncated JPEG. Small JPEG and ordinary PNG/WebP output match the base byte-for-byte. Existing workspace tests cover embedded PNG/JPEG/WebP artwork and subsequent audio decoding. `Y2Reborn/tests/artwork.py --library <built-libreborn_media.so> [--baseline <base-lib>]` regenerates the additional synthetic host inputs using Pillow in a temporary directory; no extra product assets/dependencies are installed.

Initial Linux test invocations found an old GPU-02 DT artifact incompatible with current mappings, missing host QEMU, and absolute cache symlinks unavailable inside the isolated environment. Those are retained test-environment failures, not ignored passes. Final execution uses the retained Baseline02 emitted DT and a locked-environment QEMU wrapper, with native DRM/Pillow on the host: 68 pass, zero skips. No kernel rebuild or repeated unchanged ROM/recovery provenance.

The first extra device harness completed the wheel workload but failed while formatting a nonexistent library track-count key; its finally block blanked and removed scratch. The corrected run supplies the reported wheel/decoder receipt. Home restoration was subsequently verified after explicitly waking before navigation. A regex escaping error omitted GPU job IRQ names from the timed snapshots: this pass claims no GPU-job IRQ deltas. Runtime-PM timers, DRM/OVL interrupts and MMU fault counters were captured; the limitation is recorded in the [physical summary](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-graphics/physical.json).

Raw local receipts: each worktree's `out/platform-v1-graphics/`; Linux `linux-final-tests.log`, device harness and lock attempts; Reborn `artwork-before.json`, `artwork-after.json`, `artwork-regression.json`, `reborn-final-tests.log`, `fmt.log`, `clippy.log`, `arm-build.log`, `arm-artwork.json`; Linux `device.jsonl`, `device-extra.jsonl`, `device-art-reverse.jsonl` and `device-restored.json`. Compact durable receipts are [software](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-graphics/software.json), [physical](https://github.com/schulzcode/y2linux/blob/HEAD/docs/validation/evidence/platform-v1-graphics/physical.json) and the peer baseline above. Raw `out/` directories are ignored build/evidence scratch, not new production images.

## Changes, preserved scope and verdict

Reborn changes: `crates/reborn-media/native/media.c`, `tests/artwork.py`. Linux changes: `docs/validation/Y2-PLATFORM-V1-GRAPHICS.md`, `docs/validation/evidence/platform-v1-graphics/{software,physical,peer-baseline}.json`, `docs/planning/roadmap-gap-audit.md`, `docs/planning/platform-v1-roadmap.md`, `docs/knowledge/gpu-platform.md`. Reborn's local commit is `a2df691edfbb105a164e2f5f574b158ec5f81e6c`; Linux's local receipt commit is on `codex/platform-v1-graphics`. No GPU, DRM, panel, backlight, splash or CPU idle driver/policy changes. No cosmetic redesign, new renderer, cache architecture, synthetic 3D benchmark, flash, push, installed application replacement or main modification.

Master integration identified overlapping reduced-JPEG work in the independent FFmpeg/media commits `a22107c` and `43a695c`. Select one bounded decoder path when integrating and retain that pass's aggregate-I/O and cancellation guards. This branch's measured native membrane is an isolated candidate; its decoder figures do not qualify a later combined native ABI or different implementation.

**Artwork improvement and bounded awake/off/wake graphics behavior PASS. Platform 1.0 graphics acceptance remains PARTIAL:** the installed app still redraws static UI, and the separate performance correction must be integrated and accepted before a no-unnecessary-redraw verdict. Driver/scanout/backlight architecture is intentionally preserved on positive evidence. Physical system resume, visible boot/shutdown/white-flash acceptance, full product artwork transitions, large-list interaction, electrical savings and endurance retain their explicit gates. This pass closes no release or system-suspend milestone. #34 remains OPEN with its independent full-resume gate; #28/#31 remain OPEN.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
