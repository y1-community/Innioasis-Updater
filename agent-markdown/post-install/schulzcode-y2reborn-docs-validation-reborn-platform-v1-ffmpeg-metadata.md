---
title: "Reborn Platform 1.0: FFmpeg, metadata and library ingest - Innioasis Updater"
description: "Reborn Platform 1.0: FFmpeg, metadata and library ingest 2026-10-04. Verdict: PLATFORM V1 READY WITH LIMITATION for this software subpass. Metadata ingestion is substanti"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-validation-reborn-platform-v1-ffmpeg-metadata.html"
---

# Reborn Platform 1.0: FFmpeg, metadata and library ingest - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Reborn Platform 1.0: FFmpeg, metadata and library ingest

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Reborn Platform 1.0: FFmpeg, metadata and library ingest

2026-10-04. Verdict: PLATFORM_V1_READY_WITH_LIMITATION for this software subpass. Metadata ingestion is substantially faster, bounded and better tested. The new candidate has not been qualified on physical SD storage with concurrent playback; this receipt does not close the wider Platform 1.0 hardware gates.

Baseline: Reborn `b71b468860233faa0a42b8448ec5777fa952b8e3`; Linux worktree base `b5aea93`. Implementation: `a22107c53fc841f7f7e6e7767822ebec720bea99`, followed by `43a695c` for the sidecar-only collection-open correction. Work is isolated on `codex/platform-v1-ffmpeg-metadata`. No main-worktree edits, flash or push. Existing Luca author/committer identity was reused without changing Git settings.

[Compact measured evidence](https://github.com/SchulzCode/Y2Reborn/blob/main/docs/validation/evidence/platform-v1-ffmpeg-metadata.json) preserves samples, phases, RSS, component versions and fixture hashes. Raw local receipts are in ignored `out/media-pass/`. Admission and database-extension audits are in the paired [roadmap audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fplanning%2Froadmap-gap-audit.md). Retained [UART01](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Linux%2Fblob%2Fmain%2Fdocs%2Fvalidation%2FY2-CPU-C3-UART-PHYSICAL.md) hardware evidence identifies Linux `e9e8d63`, Reborn `b71b4688`, boot `fd955840-35d9-47db-83e0-ff47d6bb2d2b`, taint 0. It proves bounded installed playback/storage/CPU behavior, not this candidate's library throughput. The shared device lock was busy with the separate storage lane; this pass did not operate the physical device. That lane's owner-reported SDR104 results remain separate evidence.

Later receipt update: the storage owner supplied actual 1,000-file stock scanner receipts for Baseline02 on DATA and SD. They were read and summarized below, with original hashes in the compact evidence. This adds physical baseline evidence; the new metadata candidate still has no physical run.

## 1. Current metadata architecture and file-open trace

The architecture remains file → direct FFmpeg demux/decode/metadata → Reborn media abstractions → stereo float DSP → sink conversion → ALSA/BlueALSA. No FFmpeg CLI subprocess, replacement framework or production tag parser was introduced. The lazy shared media membrane remains process resident; each demux/decoder context has one owner and is closed by Rust `Drop`.````````

| Stage | Baseline | Current |
| --- | --- | --- |
| Discovery/filter | Directory queue, case-insensitive supported suffixes, pinned source root | Depth-first directory iterators, maximum depth 32; supported regular files only; symlinks skipped |
| Incremental identity | Whole-source map of complete track rows | At most 64 candidate stamps: source/path, size, nanosecond mtime, extractor revision |
| Changed-file initial open | Playback Decoder::open | Demux-only MediaFile::open; one regular-file descriptor, custom FFmpeg AVIO |
| avformat_open_input / detection | FFmpeg, 2 MiB probe budget | Same FFmpeg format detection and probe budget |
| avformat_find_stream_info | Always | Complete single-audio-stream header path skips it; otherwise normal bounded analysis |
| Codec/DSP setup during scan | Audio decoder, two resamplers, FLTP graph, packet/frame state | None; FLAC codec extradata initialization supplies channels/precision without decoding frames |
| Tags/properties | Shared with playback, some incorrect aliases/properties | One common extractor for inspection and playback |
| Artwork during scan | Attached picture could be decoded by stream analysis | Detection only; picture streams discarded during analysis; no thumbnail decode |
| DB publish | Batch 64; reused rows cloned/upserted/reindexed | Batch 64; reused rows update seen/deleted only; changed rows preserve ID at same source/path |
| Finish/removal | Source guards; wall-clock scan generation | Same guards plus strictly increasing generation; prune only complete, identity-consistent sources |
| Collection cover | Another complete playback open | Embedded cover: another lightweight inspection on a cache miss. Sidecar-only track: no media open |
| Playback | Separate decoder open | Separate decoder open, necessary for current codec/packet/seek state; artwork uses that same owner |

An unchanged incremental file has zero media opens and zero FFmpeg parses. A newly indexed file has one media open. If its embedded cover is subsequently requested, a collection-cache miss adds one lightweight open; playback adds its own necessary open. The four-entry collection pixel cache avoids repeat embedded decoding. No scanner stores encoded artwork or keeps thousands of demux contexts alive to avoid that occasional second open. Sidecar discovery and decoding are on demand. Each external image is opened once per decode attempt, with a size check before allocation.

The fast header path is admitted only for FLAC, WAV, AIFF, APE, WavPack, Ogg and MP4/M4A when there is one audio stream and usable rate, channels and duration. MP3, raw AAC, multiple audio streams and incomplete headers retain `avformat_find_stream_info` and `av_find_best_stream`. FFmpeg may decode limited audio during that fallback; it is not a whole-track decode. No lower probe or analysis limit was used to improve the benchmark. FFmpeg documents probing and analysis controls separately in [AVFormatContext](https://www.ffmpeg.org/doxygen/9.0/structAVFormatContext.html). The exact local FFmpeg 9.0.2 demuxer/decoder sources were also inspected.

## 2. Bugs found
  - Scans and collection covers paid for a complete playback/DSP initialization.
  - Stream analysis could unnecessarily decode attached pictures.
  - AIFF `AUTH` became FFmpeg's `author`, which the artist extractor ignored;

`albumartist` aliases were also missed.
  - Ordinals accepted negative/overflow/trailing-garbage input through unchecked

`strtoul`; bounded copies could split a valid UTF-8 code point.
  - ReplayGain peak values incorrectly accepted a `dB` suffix, and coded stream

ReplayGain side data was ignored.
  - `skip_manual` was set as an integer option although it is a `flags2` constant;

its result was ignored. Ogg Opus duration included its pre-skip.
  - Source sample-format labels described decoded containers such as `fltp`/`s32`

instead of encoded precision/PCM encoding.
  - Rapid scans could share a millisecond generation and fail to prune removed rows.
  - A file changed/replaced while extracting metadata could publish mixed revisions.
  - Old unchanged DB rows would retain corrected-but-stale metadata indefinitely.
  - External artwork had weaker dimension protection; sidecar names differed

between collection and playback and rejected mixed-case names.
  - Sidecar pixels cached by the music file's stamp stayed stale after a cover edit;

a corrupt disk pixel cache could be read into memory before checking its length.
  - Default FFmpeg filter-graph thread pools were created even without a slice-

threaded filter. Only the stereo equalizer benefits here.

## 3. Metadata correctness

Container tags take precedence; an absent/empty container value falls back to the selected stream. FFmpeg owns case/encoding/container normalization. Missing title remains empty at the media boundary and becomes the filename at ingestion. Repeated Vorbis values retain FFmpeg's deterministic `first;second` representation; the product does not guess a new artist-splitting convention.````````````````

| Field | Behavior / evidence |
| --- | --- |
| Title, artist, album | UTF-8-safe bounded copy; invalid bytes repaired deterministically by Rust; AIFF author fallback |
| Album artist | album_artist, then albumartist; Unicode FLAC/ID3/APE and existing MP4/Ogg assertions |
| Track, disc | Strict unsigned number or number/total; 3/12 → 3, 1/2 → 1; invalid/negative/overflow → 0 |
| Date/year, genre | Extracted as bounded raw strings, date then year; exposed in Metadata. Current Track/DB/UI does not persist these fields |
| Composer | No existing product field; intentionally not added |
| Duration | Selected stream time base preferred; container fallback; explicit Ogg Opus pre-skip removed; MP3 Xing and MP4 edit handling preserved |
| Codec/rate/channels | Encoded codec ID/name and codec parameters, constrained to supported audio limits; playback/header agreement tested |
| Source bits/format | PCM encoding, or raw/coded lossless precision; lossy unknown remains 0/unspecified, never “32-bit” because decoding is float |
| Decoder/DSP/sink | Separate fields; inspection leaves decoder/DSP/output fields empty; playback still reports decoder format, FLTP and negotiated packed sink |
| ReplayGain | Four independently validated fields; gain ±60 dB, peaks 0..16, finite only. Explicit valid tags precede coded side-data fallback |
| Embedded art | JPEG/PNG/WebP attached pictures with usable bounded packets; corrupt art can fail independently of audio metadata |
| External art | Shared case-insensitive cover/folder/album preference; regular files; corrupt candidate falls through |
| Delay/padding | Manual codec skip side data enabled correctly; existing sample-trim path retained; exact MP3/Opus/M4A frame counts asserted |

FLAC/ALAC/APE 24-bit or 16-bit precision is distinct from a 32-bit decoder container. WAV float32 really is a 32-bit float source and is labeled `pcm_f32le`; lossy AAC/MP3/Vorbis/Opus are unspecified precision. WavPack is labeled `lossless-N-bit`, avoiding an unsupported claim that its encoding is necessarily integer. Bitrate prefers the audio codec parameter and otherwise uses FFmpeg's container estimate; an unavailable estimate stays zero.

## 4. Performance bottlenecks

Native phase measurements found playback setup costing approximately 0.38–0.58 ms per short track, versus 0.06–0.15 ms for initial demux open. It dominated the old metadata path. For the sparse 180-second PCM WAV, stream analysis dominated: 17.74 ms and 720,940 bytes read, compared with no stream analysis and 65,580 bytes on the metadata header path. FFmpeg still reads beyond the initial WAV header to find supported trailing metadata; the implementation does not stop at an assumed 44-byte header.

Whole-row incremental DB rewriting and repeated library-count queries were the next demonstrated costs. The final 10k initial scan's median measured metadata work was about 0.83 seconds, DB request/transaction wait about 0.16 seconds, and total 1.08 seconds. An unchanged scan did no FFmpeg work; DB wait plus traversal dominated its 130 ms. These phase timers are nested: do not add FFmpeg open/probe time to metadata time. DB time includes channel wait and SQL, not only SQLite CPU time. Artwork time during library scanning is zero.

The 1,500-open concurrency experiment took 152/68/35 ms on the host for 1/2/4 metadata workers (QEMU exploratory run 821/393/200 ms). That experiment omits physical SD contention, playback and CPU policy. The product remains serial with a bounded DB pipeline; these figures do not establish the best worker count on a quad Cortex-A7. No desktop worker pool was added.

## 5. Memory bottlenecks and bounds

The old incremental map retained complete metadata strings for every indexed track, then cloned rows. It added about 10 MiB RSS for 10k rows. Directory queues could also grow with breadth. Both are replaced by bounded candidates and a depth-first iterator stack. The baseline filter pool amplified emulated ARM memory/thread overhead. Graphs without active EQ, including crossfade, now use one thread, and at most two for the slice-threaded stereo EQ.

| Resource | Current bound |
| --- | --- |
| Scan candidates, DB publish batch, identity results | 64 files/rows each; synchronous acknowledgment |
| Directory stack / supported files | 33 iterators / existing 250,000-file guard |
| Scanner request/result channels, DB commands | 1 / 2 / existing 32; no unbounded new task queue |
| Native FFmpeg allocation | 32 MiB per allocation, initialized once before workers regardless of logging setup |
| Header + analysis I/O | 32 MiB aggregate per open, including rereads; 10-second cancellation deadline; regular nonempty files only |
| Pending native PCM allocation | 32 MiB; normal playback releases only the header byte budget after initialization |
| Exported text | Existing 512-byte title/artist/album/album-artist buffers; date 128, genre 512; UTF-8 repair remains bounded |
| Encoded artwork | 16 MiB per image packet/file; max 16 streams per input |
| Decode dimensions | JPEG 16 Mi pixels with FFmpeg lowres up to 1/8; PNG/WebP 4 Mi pixels |
| UI pixels / collection cache | 160×160 RGBA = 100 KiB; four successful embedded covers = 400 KiB plus bounded replies |
| Sidecar candidates | At most 12 paths; no complete directory list retained |

PNG/WebP do not offer a reduced-resolution decoder here, so oversized images are refused rather than decoded fully. The JPEG 4000×4000 fixture reduces to 500×500 before scaling to the UI buffer. Its header dimensions are obtained through FFmpeg's MJPEG decoder with frames discarded, not a custom JPEG parser. The per-allocation limit is not a promise that the whole process consumes at most 32 MiB; measured process RSS includes FFmpeg mappings, SQLite and workers.

## 6. Changes made

`MediaFile` owns a demux-only native context and shares extraction/artwork functions with playback. Custom AVIO preserves FFmpeg detection while enforcing regular files, byte budget and cancellation, and closes its AVIO buffer and file exactly once. Attached images are excluded from analysis. Metadata and gapless fixes are listed above; DSP math and sink packing remain covered by the existing regression matrix.

Ingestion uses lean batched identity queries, moves extracted strings into changed rows, and only marks reused IDs seen. It checks dev/inode/size/mtime/ ctime after extraction and source identity before publishing/finishing. One bad file is logged and does not prevent later tracks being indexed. Existing conservative deletion behavior is preserved: a source with failures retains its old rows until a complete scan can safely prune.

The additive `metadata_revision INTEGER NOT NULL DEFAULT 0` column preserves SQLite schema/user_version 1 and row IDs. Old rows reparse once and successful rows record extractor revision 2. A malformed file cannot force every other track to reparse on subsequent scans. Rapid scan generations now increase strictly, including across reopening the database.

Collection and playback share sidecar selection. Only successful embedded pixels are cached against the track stamp; sidecars are checked anew on a new request. Playback validates cached pixel file length before reading it. A sidecar-only collection request skips opening the music file entirely.

## 7. Intentionally unchanged

FFmpeg 9.0.2, supported media/artwork matrix, probe/analyze budgets, the decoder/ float DSP/sink architecture, SQLite/WAL ownership, row identity, source UUID/ mount protections, rebuild behavior and bounded playback queues remain. No content hash is computed for every rescan. Identical content at two paths is two library entries; duplicate filenames on different media remain distinct. Renames/moves become a new source/path entry and prune the old path after a complete scan; queue ID preservation across moves is not an existing promise.

Playback still calls stream analysis: startup decoder state and correct trim/ seeking matter more than borrowing the scanner shortcut. A separate playback open is necessary. Source replacement, hotplug and DB recovery protections were already correct and retain their tests. No kernel, memory-layout, hardware, partition, firmware, networking, video, streaming or DRM scope was added.

## 8. Before/after metadata parse times and playback startup

Host x86_64, Rust 1.90.0, FFmpeg 9.0.2; 20 direct native owner initializations per fixture, both C builds `-Os`. Timer stops before owner close. Baseline C is the original `b71b468` implementation with timing instrumentation only. OS cache is uncontrolled; these are warm p50 latency measurements, not SD latency. All p95 values and I/O phases are in the compact evidence.

| Fixture | Before ms | After metadata ms | After playback open ms |
| --- | --- | --- | --- |
| FLAC 24/96 | 0.585 | 0.053 | 0.200 |
| MP3 | 0.664 | 0.139 | 0.307 |
| Raw AAC | 0.820 | 0.179 | 0.582 |
| M4A AAC | 0.775 | 0.056 | 0.591 |
| M4A ALAC | 0.624 | 0.054 | 0.338 |
| Vorbis | 0.843 | 0.080 | 0.446 |
| Opus | 0.702 | 0.071 | 0.223 |
| WAV PCM24 | 0.530 | 0.063 | 0.134 |
| WAV float32 | 0.569 | 0.048 | 0.211 |
| AIFF PCM24 | 0.498 | 0.049 | 0.122 |
| APE | 0.518 | 0.035 | 0.127 |
| WavPack | 0.814 | 0.046 | 0.432 |
| FLAC + JPEG / PNG / WebP | 0.716 / 0.718 / 0.688 | 0.063 / 0.062 / 0.061 | 0.283 / 0.189 / 0.276 |
| Sparse 180-second WAV | 18.306 | 0.085 | 18.200 |

Playback improvements come from bounded graph threads and avoiding picture analysis, not weaker format detection. The long WAV remains analysis-bound at playback open, intentionally. These measurements exclude sink negotiation, DAC/radio behavior and audible start latency. First lazy membrane load was about 21–35 ms in the benchmark processes and is visible in maxima; it is not repeated for every file.

Artwork after this pass: embedded JPEG/PNG/WebP warm p50 0.150/0.112/0.151 ms; 4000×4000 external JPEG p50 3.764 ms, max 4.022 ms, 10/10 successful decodes. Corrupt/oversized fixtures return errors without crashing. The standalone artwork benchmark process peaked at 47,464 KiB. No comparable pre-change large image decode receipt was collected, so no invented artwork speedup is claimed.

## 9. Before/after library scans

Same read-only 15-variant mixed corpus, fresh DB per initial scan, immediate unchanged rescan; three alternating before/after runs. The source scanner and DB are the product implementations, not a loop around a tag parser. The old host harness uses the old ABI/native library explicitly; the ARM archive's product source files match `b71b468` byte for byte. Corpus is synthetic and short: 1,000 files total 23,703,609 bytes, not music-sized SD bandwidth.

| Tracks | First before ms | First after ms | First files/s before → after | Incremental before → after ms |
| --- | --- | --- | --- | --- |
| 100 | 94 | 31 | 1,053 → 3,139 | 1 → 1 |
| 1,000 | 754 | 125 | 1,325 → 7,990 | 17 → 8 |
| 10,000 | 7,408 | 1,084 | 1,350 → 9,218 | 191 → 130 |

These are medians. The 10k first-scan ranges were 7,384–7,514 ms before and 1,084–1,102 ms after; incremental 189–195 and 122–135 ms. Earlier shared-host runs were noisier (after first scan 1.2–3.8 seconds); they were retained locally, not substituted into the alternating comparison. No global cache flushing or CPU/governor changes were performed.

Cortex-A7 user-mode QEMU, exact Baseline02 ARM libraries and four allowed host CPUs: 1,000-track median first scan 17,058 → 692 ms, unchanged 109 → 66 ms. First ranges: 16,259–19,382 → 687–705 ms. QEMU especially magnifies the original filter-thread setup cost. This validates ARM behavior and relative cost under emulation, not a physical Y2 speed estimate. Production scanning remains one worker. Every unchanged scan reused all files and recorded zero FFmpeg opens/analysis/I/O in the candidate metrics.

The independent storage lane then ran the exact stock ARM scanner harness (`16e64c9e…` SHA256) against the installed old media membrane, on both physical volumes in its own lock slot. Receipt identity: Linux `8584ccd85f052f351fe51650b2348c83ca894ed4`, Reborn `b71b4688`, Baseline02, kernel `6.18.0-y2linux-baseline-02`, rootfs `2025.02.18-platform-v1.21`, boot `27e6d684-3794-4490-95db-a489027cd4f4`; closing taint 0. These are single bounded runs of the same 1,000-file, 23,703,609-byte corpus:

| Physical stock baseline | Initial ms / files/s | Incremental ms | Initial / cumulative peak KiB |
| --- | --- | --- | --- |
| DATA, eMMC HS200 | 5,526 / 181.0 | 393 | 10,468 / 10,656 |
| SD, ext4 SDR104 | 5,495 / 182.0 | 401 | 10,580 / 10,936 |

Both initial scans indexed all 1,000 files with zero failures; both rescans reused all 1,000. Controller fault deltas were zero during write/fsync, read/SHA256 and scanning. Separate storage workload rates were DATA 1.731 MB/s write/fsync and 3.078 MB/s read/SHA256, SD 1.532/3.034 MB/s; those are small-file workload rates, not FFmpeg parse rates. Aggregate CPU busy during each initial+incremental scanner process was about 27%. Private scratch was cleaned and services/modes/settings left unchanged by that slot. The next device slot is reserved for suspend work; this lane did not acquire the device. Receipts originate in storage's ignored `out/platform-v1-storage/{emmc,sd}-corpus.json` and `corpus-restored.stdout`, copied immutably to this pass's ignored evidence. There is no physical candidate after-number, concurrency comparison or speedup extrapolation from these stock results.

## 10. Peak memory measured

Linux `/proc/self/status` VmHWM, maximum across each three-run group; KiB. The scan process includes libraries/DB/log worker but not the GUI or simultaneous playback. Incremental HWM is cumulative within the initial+rescan process.

| Tracks | Initial before → after KiB | Through incremental before → after KiB |
| --- | --- | --- |
| 100 | 54,432 → 51,112 | 54,536 → 51,136 |
| 1,000 | 55,388 → 52,488 | 56,368 → 52,496 |
| 10,000 | 56,808 → 53,716 | 66,488 → 53,720 |

At 10k, the measured process peak is about 64.9 → 52.5 MiB. Remaining modest growth includes SQLite page/cache state, not retained artwork blobs. QEMU 1k peak was 133,592 → 35,536 KiB; those values include emulator mappings and translated code and must not be described as physical ARM process RSS. No physical candidate peak RSS was measured. The later physical stock scanner peaks in section 9 are real ARM process measurements, still excluding the running GUI/whole-application memory. They must not be compared as an after-result to the host or QEMU figures.

## 11. Metadata edge cases covered

The [metadata fixture manifest](https://github.com/SchulzCode/Y2Reborn/blob/main/assets/fixtures/metadata/manifest.json) records 17 fixtures, sizes, hashes and generation provenance. Coverage includes FLAC comments, UTF-8/UTF-16 ID3v2, APE tags, WAV INFO, AIFF NAME/AUTH, existing MP4/M4A and Vorbis/Opus tags; Japanese/accented text, missing/empty tags, duplicate/multiple values, invalid UTF-8, long strings, track/total, multi-disc, negative/overflow ordinals, non-finite/malformed ReplayGain, four gain/peak fields, embedded JPEG/PNG/WebP, corrupt art, malicious declared lengths/dimensions, zero-length media, mixed-case sidecars and fallback after corrupt covers.

Deterministic fuzz-style tests exercise 99 truncation/header-XOR cases across nine formats. A generated 33 MiB multi-tag FLAC is refused by the aggregate I/O budget in both inspection and playback. Dimensions of 100,000×100,000 are rejected. Metadata and valid subsequent library tracks survive bad artwork/ media. Exact gapless output counts remain MP3 11,025, Opus 12,000 and M4A AAC 11,025 frames for their 250 ms fixtures. Source precision, duration and channel/ rate agreement are checked between inspection and playback.

Library tests cover same-path changes with stable ID, removal and move pruning, unchanged scans with a trigger forbidding metadata rewrites, a good+bad library, same-size/mtime replacement detection during extraction, source identity changes, incomplete traversal, SQL failures/ENOSPC and preserved prior rows. Migration removes the new column from a populated schema-1 fixture, reopens it, proves one-time old-row reparse and subsequent reuse even with an invalid neighbor.

## 12. Files changed
  - `crates/reborn-media/native/media.c`, `src/native.rs`, `src/lib.rs`: native

inspection/AVIO/ownership, extraction, image bounds, DSP thread caps, fixtures.
  - `crates/reborn-library/src/lib.rs`, `src/benchmark.rs`,

`examples/media_bench.rs`: bounded ingest, DB revision/generation, metrics and product-path benchmark.
  - `app/reborn/src/artwork.rs`, `playback.rs`: lightweight collection reads,

sidecar consistency, embedded-only cache and bounded pixel-cache reads.
  - `assets/fixtures/metadata/*`, fixture README: 17 fixtures plus manifest,

with original APE/WavPack media provenance retained.
  - `tools/build/metadata_fixtures.py`, `jpeg_fixture.c`, `media_bench.py`,

`media_qemu.py`, `media_sanitize.c`: reproducible fixture/benchmark/ownership tools.
  - This report, compact JSON, FFmpeg architecture page, documentation index/catalog.
  - Paired Linux `docs/planning/roadmap-gap-audit.md` and `platform-v1-roadmap.md`:

admission, cache-extension review and closing software-boundary audit only.

## 13. Validation and reproduction````````

| Check | Result |
| --- | --- |
| cargo fmt --all -- --check | PASS |
| cargo clippy --workspace --all-targets --locked -- -D warnings | PASS |
| cargo test --workspace --locked | PASS, 252 tests; media 32, library 30 |
| tools/build/cross.sh with exact Baseline02 Buildroot SDK | PASS, ARM workspace release, Cortex-A7 hardfloat |
| Fresh ARM media/library test binaries under QEMU | PASS, 32 + 30 tests |
| Fresh ARM daemon + control/media checks | PASS, six checks; decoder/database/library diagnostics explicitly assert passed |
| Native dependencies / runtime policy | PASS, FFmpeg 9.0.2 six-library ABI; required formats/decoders/filters; file protocol only |
| Native ASan/UBSan/LSan ownership stress | PASS, 26 fixture arguments × 20 iterations: inspect/art/read/cancel/close; no reported leak or invalid access |
| Python syntax / diff whitespace | PASS |
| Reborn documentation links/catalog | PASS, 59 pages / 572 local links |
| Physical new-candidate scan/concurrent playback | NOT_RUN |
| Physical stock 1k scan/reuse, DATA and SD | PASS, separate storage owner receipts; zero failures/controller fault deltas |

Runtime versions: avutil 61.1.102, avcodec/avformat 63.1.102, avfilter 12.1.102, swresample 7.1.102, swscale 10.1.102. ELF and runtime manifests agree. Production has no FFmpeg CLI, encoders/muxers, network or libavdevice. The sanitizer rebuild covers the membrane driver; FFmpeg shared dependencies were not themselves rebuilt with sanitizers. These tests are bounded malformed-input regression checks, not comprehensive fuzz qualification. The paired Linux documentation check finds one unchanged legacy Y2Player link whose sibling repository is absent from the isolated worktree layout; its original target exists. All new links resolve. No unrelated documentation was rewritten to accommodate that layout.`cargo build -p reborn-library --example media_bench --release --locked python3 tools/build/media_bench.py --output out/new-media-receipt --repeats 3 --long-wave target/release/examples/media_bench artwork assets/fixtures/metadata target/release/examples/media_bench parallel out/new-media-receipt/parse-fixtures python3 tools/build/metadata_fixtures.py # Caller supplies the exact production SDK; no device access. Y2_BUILDROOT_OUTPUT=/absolute/buildroot-output sh tools/build/cross.sh # Run inside an isolated environment providing qemu-arm and the ARM rootfs: python3 tools/build/media_qemu.py --sysroot /absolute/arm-rootfs \ --binaries target/armv7-unknown-linux-gnueabihf/release --scratch out/new-qemu-receipt`

The benchmark refuses existing scratch/output, reads media only and writes its own DB/logs. To reproduce baseline scans, archive `b71b468`, add the measurement example using its original `Decoder` metadata path and build against its matching membrane. Do not run a new Rust binary against an old native membrane or vice versa; the opaque private ABI changed and the pair must be built/packaged together.`cc -g -O1 -fsanitize=address,undefined -fno-omit-frame-pointer \ tools/build/media_sanitize.c -o /tmp/reborn-media-sanitize \ $(pkg-config --cflags --libs libavformat libavcodec libavutil libavfilter libswresample libswscale) -lm ASAN_OPTIONS=detect_leaks=1:halt_on_error=1 /tmp/reborn-media-sanitize \ assets/fixtures/tone.flac assets/fixtures/mp3.mp3 assets/fixtures/m4a-aac.m4a \ assets/fixtures/vorbis.ogg assets/fixtures/opus.opus assets/fixtures/wav-pcm24.wav \ assets/fixtures/aiff-pcm24.aiff assets/fixtures/ape-silence.ape \ assets/fixtures/wavpack-silence.wv assets/fixtures/metadata/*`

The 26-argument sanitizer receipt used the nine listed original formats plus the 17 fixture files, excluding `manifest.json` (the wildcard above also tests that unsupported JSON input fails cleanly). Large JPEG regeneration uses the direct-library encoder in `jpeg_fixture.c`; encoders remain host fixture tooling only. Fixture writers are not production tag parsers.

## 14. Commits

`a22107c` — Harden FFmpeg metadata and bound incremental library ingestion. `43a695c` — Skip media opens for sidecar-only collection artwork; explicitly assert QEMU diagnostic success. `bf1c50a` records the initial receipt and `0d692f2` the paired Linux audit. Following documentation commits reconcile the later physical stock receipts; their hashes are in the handoff. No push.

## 15. Remaining Platform 1.0 limitations
  - Physical SD scan latency, whole-application RAM and concurrent playback/scan

behavior of the new candidate remain unmeasured. QEMU and short synthetic files do not qualify those gates or SD failure/hotplug endurance.
  - Persistent incremental identity uses source/path/size/nanosecond mtime. An

intentional same-size rewrite preserving mtime between scans can remain cached; explicit rebuild reparses it. During-parse inode/ctime checks are stronger, but are not persisted as a new cross-platform identity scheme.
  - A bad file makes source deletion conservative, so removed old rows may remain

until a complete scan. Other valid tracks still ingest/reuse successfully.
  - Date/genre are extracted but not new DB browsing features; composer remains

unsupported. Some header-only lossless bitrate estimates stay unknown, and lossy source bit depth correctly stays unknown. Raw ADTS duration remains FFmpeg's bounded estimate when the format lacks a reliable total.
  - Existing browsing requests cap at 20,000 rows while the scanner guard is

250,000. This pass measures 10k ingestion, not 250k GUI usability. Content deduplication and move-stable queue IDs are not implemented.
  - Images beyond the byte/pixel policies, unusual >16-stream media, or metadata

requiring >32 MiB header/analysis reads are refused. Ordinary long music duration itself does not trigger that header budget.
  - App and native membrane require matched packaging. Full suspend, analog/high-

resolution audio, radio coexistence, battery and release/image qualification retain the independent roadmap gates; none are promoted by this receipt.

## 16. Verdict

PLATFORM_V1_READY_WITH_LIMITATION. This media software subpass is ready for integration and bounded physical qualification. Correctness/ownership and ARM regressions pass; 10k ingestion is about 6.8× faster, incremental work is lean, and scan memory no longer holds the library's complete raw metadata/art corpus. No substantial engine or database rewrite is justified by the measurements. The next evidence boundary is the matched candidate's guarded SD scan alongside playback, under the shared device lock; no hardware milestone is closed here.

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
