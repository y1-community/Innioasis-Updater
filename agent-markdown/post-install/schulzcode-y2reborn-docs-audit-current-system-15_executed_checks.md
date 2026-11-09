---
title: "Executed checks and provenance limits - Innioasis Updater"
description: "Executed checks and provenance limits <!-- knowledge-base-scope: historical-audit/review -- Historical record. The dates, candidate identity,"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2reborn-docs-audit-current-system-15_executed_checks.html"
---

# Executed checks and provenance limits - Innioasis Updater

[← All documentation](../post-install/index.html)

Post-install setup · Y2Reborn

# Executed checks and provenance limits

Documentation published by SchulzCode/Y2Reborn.

Instructions published by the project, shown here word for word.[All documentation →](../post-install/index.html)[All documentation](../post-install/index.html)

# Executed checks and provenance limits > **Historical record.** The dates, candidate identity, "current" claims, > next steps and permissions below belong to this recorded boundary. See > [current state](../../CURRENT_REBORN_STATE.md) for the latest physically observed result. 

Date: 2026-09-22. Repository HEADs are in [scope](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2FSchulzCode%2FY2Reborn%2Fblob%2Fmain%2Fdocs%2Faudit%2Fcurrent-system%2F00_SCOPE_AND_EVIDENCE.md). All tests were host-side; no SSH, USB-device command, flashing or power/radio operation was issued. No Cargo/kernel/Buildroot build was run. Test scripts used their own temporary directories; production source/configuration was not edited. Only this audit directory was added.

## Commands actually executed

Working directory: `/home/luca/Dokumente/Code/Y2Reborn` unless stated otherwise.`target/debug/deps/reborn-569a8d6f5e5b2b9d --list target/debug/deps/reborn_media-11cd456330717a75 --list timeout 35s target/debug/deps/reborn-569a8d6f5e5b2b9d --test-threads=1 --nocapture timeout 35s target/debug/deps/reborn_media-11cd456330717a75 --test-threads=1 timeout 35s target/debug/deps/reborn-569a8d6f5e5b2b9d --nocapture PYTHONDONTWRITEBYTECODE=1 python3 tests/tooling.py PYTHONDONTWRITEBYTECODE=1 timeout 60s python3 tests/host-daemon.py`

The following cached library binaries were each invoked with `timeout 40s target/debug/deps/<binary> --test-threads=1` in a shell loop:``````````````

| Binary | Passed | Failed |
| --- | --- | --- |
| reborn_core-7dcfc2228b127774 | 5 | 0 |
| reborn_library-c5234af8506b1a3f | 7 | 0 |
| reborn_ui-27d92cb4394b7256 | 10 | 0 |
| reborn_observability-65a42a3921a27cc5 | 13 | 0 |
| reborn_control-894d4af5df4fb32d | 5 | 0 |
| reborn_audio-610cef8b7603caee | 2 | 0 |
| reborn_platform-a0dab0805802cc10 | 21 | 0 |

Playback binary: 6/6 passed serially, then 6/6 passed in default parallel mode. Media binary: 14/14 passed. Thus 83 distinct cached Rust tests passed, with six playback tests repeated. Expected malformed-media/unknown-ALSA-device diagnostic output was not a test failure. Python tooling: 4/4. Host daemon output:`{"passed":true,"checks":20,"scanner_tracks":6,"incremental_reused":6,"malformed_files_skipped":1,"no_hardware_claim":true}`

Provenance limitation: these binaries pre-existed the audit. Observed dates range across earlier implementation steps; the main host executable was dated September 19 and the playback/UI test binaries September 20. They were not rebuilt or proven to correspond byte-for-byte to HEAD. Native host tests resolve host FFmpeg 9 libraries, whose enabled component set is broader than the pruned target build (`ldd` confirmed host `/usr/lib/libav*.so`). Passing host tests therefore cannot prove target packaging/minimal-component sufficiency. Current source was inspected independently and generated target configuration checked separately.

Working directory: `/home/luca/Dokumente/Code/Y2Linux`:`PYTHONDONTWRITEBYTECODE=1 python3 tools/production/verify-ffmpeg.py \ --buildroot-output out/y2linux-reborn-audio-final/buildroot`

Result: PASS generated FFmpeg configuration/library/ELF boundary. A subsequent exploratory `readelf` lookup in the newer reuse-only staging tree failed because that tree does not contain a full installed player. That is recorded as an inspection-path miss, not a target image validation failure. The retained full tree above was the appropriate input for this check.

Read-only image checks used `debugfs -R` without `-w` against `out/y2linux-reborn-ui-polish-02/Y2ROOT.img`: `cat /etc/y2linux/audio-qualified.json`, `cat /usr/share/reborn/dependencies.json`, `ls -l /usr/share/reborn`, and `ls -l /usr/lib/reborn`. Results: S16/44100 qualification profile, dependency inventory including stale font8x8 entry, top-level MIT LICENSE plus fixtures but no installed DejaVu notices in that directory, and a 25,824-byte media membrane present. No image was mounted writable or modified.

Read-only inspection also used Git status/log/show, rg, sed, stat, source/config reads and local ELF dependency inspection. Some exploratory paths did not exist (for example a `series` file where the repository uses `manifest.json`); those misses were resolved by file discovery and are not product defects. No unchanged ROM/recovery hash series was repeated.

## Final documentation verification

A local Node check validated all 16 Markdown documents, 296 local links, balanced code fences, table column consistency and 42 unique master finding IDs (32 corrective/uncertain/legacy findings plus 10 positive preservation findings). No link or table error remained. Both repositories' tracked and staged diffs were empty; the only worktree addition was `Y2Reborn/docs/audit/`. No commit was made. This documentation check does not add hardware or fresh-build evidence.

## Additional native diagnostic probes

These probes call the existing cached host C membrane with the inspected ABI through ctypes. They do not compile/edit production code or access ALSA/hardware. They are diagnostic experiments, not new production tests.

### Repeated decode/close

Library: `target/debug/build/reborn-media-86921348aad87dc5/out/libreborn_media.so`. Decode `assets/fixtures/tone.flac` to S16 stereo/44100, volume 100, RG/EQ off; close decoder and cancel context each iteration. Four phases of 250 iterations:

| Closed decoders | Output frames in this phase | Process maximum RSS, KiB |
| --- | --- | --- |
| 250 | 11,025,000 | 60,744 |
| 500 | 11,025,000 | 67,272 |
| 750 | 11,025,000 | 73,904 |
| 1000 | 11,025,000 | 80,256 |

Interpretation: persistent growth supports F01's independently identified frame ownership defect. `ru_maxrss` is a high-water mark, not a live-allocation profiler; this is not proof that every byte is attributable to that one leak and not an ARM memory budget. No sanitizer/profiler was run.

### Seek versus output samples

Same membrane/fixture, volume 100, no RG/EQ. Compare unseeked and `rb_media_seek(...,500)` before reading:

| Output rate | Unseeked frames | Frames after 500-ms seek | Expected remaining duration in frames | First reported time |
| --- | --- | --- | --- | --- |
| 48,000 | 48,000 | 24,448 | 24,000 | 500 ms |
| 44,100 | 44,100 | 22,461 | 22,050 | 500 ms |

The matching-rate result avoids attributing the whole discrepancy to a resampler. The first post-seek S16 sample was -73, versus 0 at the beginning of the unseeked 48-kHz decode. This is not a waveform characterization; the significant result is extra frames despite a correct-looking label. It matches source inspection: decoded pre-target samples are not explicitly trimmed.

A preliminary 40-ms seek on the 4096-frame `gapless-a.flac` specimen returned an error and failed the probe's assertion. That preliminary probe is not included among passed tests. The one-second fixture was then used for the successful measurement above. No production change was made to make any check pass.

The exact inline probe commands used follow, so these observations can be repeated with the same cached membrane or adapted in a separately authorized validation turn.

## Filter-negotiation probe

The same cached membrane was run with FFmpeg debug logging enabled. The initial unity/no-EQ run and the volume-35/+3-dB EQ run both showed these negotiated boundaries:`16/44100 FLAC: decoder s16 -> canonical fltp @44100 24/96000 FLAC: decoder s32 -> canonical fltp @96000 configured graph: aformat -> volume -> equalizer (fltp) -> auto_aresample: fltp -> dbl -> alimiter -> auto_aresample: dbl -> fltp -> graph sink final packed output requested: s16 @44100`

The initial metadata printer retained NUL padding in its JSON strings; the second command below strips that padding. This was diagnostic formatting only. Negotiation logs came from the actual graph; no production code changed. Both probes completed successfully. The exact second command follows:`PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY' import ctypes as C, resource, json p='target/debug/build/reborn-media-86921348aad87dc5/out/libreborn_media.so' l=C.CDLL(p) class Eq(C.Structure): _fields_=[('frequency',C.c_double),('gain',C.c_double),('q',C.c_double)] class Dsp(C.Structure): _fields_=[('replay_gain',C.c_int),('volume',C.c_uint32),('count',C.c_uint32),('eq',Eq*8),('crossfade',C.c_uint32)] l.rb_cancel_new.restype=C.c_void_p l.rb_cancel_free.argtypes=[C.c_void_p] l.rb_media_open.argtypes=[C.c_char_p,C.c_int,C.c_int,C.POINTER(Dsp),C.c_void_p,C.POINTER(C.c_void_p),C.c_void_p] l.rb_media_read.argtypes=[C.c_void_p,C.c_void_p,C.c_int,C.POINTER(C.c_uint64),C.POINTER(C.c_uint64),C.POINTER(C.c_int64)] l.rb_media_close.argtypes=[C.c_void_p] d=Dsp(); d.volume=35; d.count=1; d.eq[0]=Eq(1000,3,1) pcm=C.create_string_buffer(16384); meta=C.create_string_buffer(16384) packets=C.c_uint64(); frames=C.c_uint64(); position=C.c_int64() logs=[] CB=C.CFUNCTYPE(None,C.c_int,C.c_char_p) EN=C.CFUNCTYPE(C.c_int,C.c_int) def log(level,line): s=line.decode(errors='replace').strip() if 'fmt:' in s or 'sample_fmt:' in s or 'auto-inserting filter' in s: logs.append(s) callback=CB(log); enabled=EN(lambda level: 1) l.rb_media_logging.argtypes=[CB,EN] l.rb_media_logging(callback,enabled) results=[] for name in ('flac-16-44100.flac','flac-24-96000.flac'): logs.clear(); cancel=l.rb_cancel_new(); media=C.c_void_p() r=l.rb_media_open(('assets/fixtures/'+name).encode(),44100,1,C.byref(d),cancel,C.byref(media),meta) assert r==0,r formats={key:meta.raw[offset:offset+32].split(bytes([0]))[0].decode() for key,offset in [('source',2112),('decoder',2144),('canonical',2176),('final',2208)]} while True: r=l.rb_media_read(media,pcm,2048,C.byref(packets),C.byref(frames),C.byref(position)) assert r>=0,r if not r: break l.rb_media_close(media); l.rb_cancel_free(cancel) results.append({'fixture':name,'formats':formats,'negotiation':logs.copy()}) print(json.dumps(results,indent=2)) PY`

## Repeated decode / close command`PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY' import ctypes as C, resource, json p='target/debug/build/reborn-media-86921348aad87dc5/out/libreborn_media.so' l=C.CDLL(p) class Eq(C.Structure): _fields_=[('frequency',C.c_double),('gain',C.c_double),('q',C.c_double)] class Dsp(C.Structure): _fields_=[('replay_gain',C.c_int),('volume',C.c_uint32),('count',C.c_uint32),('eq',Eq*8),('crossfade',C.c_uint32)] l.rb_cancel_new.restype=C.c_void_p l.rb_cancel_free.argtypes=[C.c_void_p] l.rb_media_open.argtypes=[C.c_char_p,C.c_int,C.c_int,C.POINTER(Dsp),C.c_void_p,C.POINTER(C.c_void_p),C.c_void_p] l.rb_media_read.argtypes=[C.c_void_p,C.c_void_p,C.c_int,C.POINTER(C.c_uint64),C.POINTER(C.c_uint64),C.POINTER(C.c_int64)] l.rb_media_close.argtypes=[C.c_void_p] d=Dsp(); d.volume=100 pcm=C.create_string_buffer(16384); meta=C.create_string_buffer(16384) packets=C.c_uint64(); frames=C.c_uint64(); position=C.c_int64() results=[] for phase in range(4): total=0 for i in range(250): cancel=l.rb_cancel_new(); media=C.c_void_p() r=l.rb_media_open(b'assets/fixtures/tone.flac',44100,1,C.byref(d),cancel,C.byref(media),meta) assert r==0,r while True: r=l.rb_media_read(media,pcm,2048,C.byref(packets),C.byref(frames),C.byref(position)) assert r>=0,r if not r: break total+=r l.rb_media_close(media); l.rb_cancel_free(cancel) results.append({'closed_decoders':250*(phase+1),'phase_output_frames':total,'max_rss_kib':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}) print(json.dumps({'probe':'cached host C membrane; same one-second fixture; every context closed','library':p,'results':results},indent=2)) PY`

## Matching-rate seek command`PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY' import ctypes as C, resource, json p='target/debug/build/reborn-media-86921348aad87dc5/out/libreborn_media.so' l=C.CDLL(p) class Eq(C.Structure): _fields_=[('frequency',C.c_double),('gain',C.c_double),('q',C.c_double)] class Dsp(C.Structure): _fields_=[('replay_gain',C.c_int),('volume',C.c_uint32),('count',C.c_uint32),('eq',Eq*8),('crossfade',C.c_uint32)] l.rb_cancel_new.restype=C.c_void_p l.rb_cancel_free.argtypes=[C.c_void_p] l.rb_media_open.argtypes=[C.c_char_p,C.c_int,C.c_int,C.POINTER(Dsp),C.c_void_p,C.POINTER(C.c_void_p),C.c_void_p] l.rb_media_read.argtypes=[C.c_void_p,C.c_void_p,C.c_int,C.POINTER(C.c_uint64),C.POINTER(C.c_uint64),C.POINTER(C.c_int64)] l.rb_media_close.argtypes=[C.c_void_p] d=Dsp(); d.volume=100 pcm=C.create_string_buffer(16384); meta=C.create_string_buffer(16384) packets=C.c_uint64(); frames=C.c_uint64(); position=C.c_int64() l.rb_media_seek.argtypes=[C.c_void_p,C.c_int64] results=[] for seek_ms in (0,500): cancel=l.rb_cancel_new(); media=C.c_void_p() r=l.rb_media_open(b'assets/fixtures/tone.flac',48000,1,C.byref(d),cancel,C.byref(media),meta) assert r==0,r if seek_ms: assert l.rb_media_seek(media,seek_ms)==0 total=0; first=None while True: r=l.rb_media_read(media,pcm,2048,C.byref(packets),C.byref(frames),C.byref(position)) assert r>=0,r if not r: break if first is None: first={'sample_left':int.from_bytes(pcm.raw[:2],'little',signed=True),'reported_position_ms':position.value} total+=r l.rb_media_close(media); l.rb_cancel_free(cancel) results.append({'seek_ms':seek_ms,'total_frames':total,'first':first}) print(json.dumps({'probe':'cached host membrane; one-second 48kHz FLAC -> 48kHz; 500ms target','results':results},indent=2)) PY`

## Resampled seek command`PYTHONDONTWRITEBYTECODE=1 python3 - <<'PY' import ctypes as C, resource, json p='target/debug/build/reborn-media-86921348aad87dc5/out/libreborn_media.so' l=C.CDLL(p) class Eq(C.Structure): _fields_=[('frequency',C.c_double),('gain',C.c_double),('q',C.c_double)] class Dsp(C.Structure): _fields_=[('replay_gain',C.c_int),('volume',C.c_uint32),('count',C.c_uint32),('eq',Eq*8),('crossfade',C.c_uint32)] l.rb_cancel_new.restype=C.c_void_p l.rb_cancel_free.argtypes=[C.c_void_p] l.rb_media_open.argtypes=[C.c_char_p,C.c_int,C.c_int,C.POINTER(Dsp),C.c_void_p,C.POINTER(C.c_void_p),C.c_void_p] l.rb_media_read.argtypes=[C.c_void_p,C.c_void_p,C.c_int,C.POINTER(C.c_uint64),C.POINTER(C.c_uint64),C.POINTER(C.c_int64)] l.rb_media_close.argtypes=[C.c_void_p] d=Dsp(); d.volume=100 pcm=C.create_string_buffer(16384); meta=C.create_string_buffer(16384) packets=C.c_uint64(); frames=C.c_uint64(); position=C.c_int64() l.rb_media_seek.argtypes=[C.c_void_p,C.c_int64] results=[] for seek_ms in (0,500): cancel=l.rb_cancel_new(); media=C.c_void_p() r=l.rb_media_open(b'assets/fixtures/tone.flac',44100,1,C.byref(d),cancel,C.byref(media),meta) assert r==0,r if seek_ms: assert l.rb_media_seek(media,seek_ms)==0 total=0; first=None while True: r=l.rb_media_read(media,pcm,2048,C.byref(packets),C.byref(frames),C.byref(position)) assert r>=0,r if not r: break if first is None: first={'sample_left':int.from_bytes(pcm.raw[:2],'little',signed=True),'reported_position_ms':position.value} total+=r l.rb_media_close(media); l.rb_cancel_free(cancel) results.append({'seek_ms':seek_ms,'total_frames':total,'first':first}) print(json.dumps({'probe':'cached host membrane; one-second 48kHz FLAC -> 44.1kHz; 500ms target','results':results},indent=2)) PY`

These are Y2Reborn's own instructions, shown here word for word.

Published by the [SchulzCode/Y2Reborn](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn) project [[1]](https://innioasis.app/firmware_info.html?repo=SchulzCode%2FY2Reborn&software=schulzcode-y2reborn)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3ASchulzCode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
