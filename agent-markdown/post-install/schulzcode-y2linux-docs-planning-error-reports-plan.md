---
title: "Error reports: opt-in reports from players to the maintainer - Innioasis Updater"
description: "Error reports: opt-in reports from players to the maintainer Status 2026-10-19: Beta 8.10 Baseline 105 ships opt-in uploads R7 done; before it Beta 8.8 shipped Save Repor"
language: "en"
source: "https://innioasis.app/post-install/schulzcode-y2linux-docs-planning-error-reports-plan.html"
---

# Error reports: opt-in reports from players to the maintainer - Innioasis Updater

[← Firmware Downloads](../firmware.html?model=Y2&software=reborn-y2linux-y2)

Post-install setup · Reborn (Y2Linux) · Y2

# Error reports: opt-in reports from players to the maintainer

Debian-based Linux with a fast clickwheel interface for the Innioasis Y2.

Instructions published by the project, shown here word for word.[Firmware Downloads →](../firmware.html?model=Y2&software=reborn-y2linux-y2)[Install guide](../guide.html?model=Y2&software=reborn-y2linux-y2)

# Error reports: opt-in reports from players to the maintainer

Status 2026-10-19: **Beta 8.10 (Baseline 105) ships opt-in uploads (R7 done); before it Beta 8.8 shipped Save Report. Earlier status follows.** Beta 8.9 (built, not published) asked only where. R3 (Worker, `fetch.py`, deploy README, upload key) and R4 (uploader, periodic check) are done and tested on `main`, unreleased; the receiver is option 1 (Worker + R2, pulled home). Next: the owner deploys the Worker (`tools/reports/README.md`), then R6 with a test build.** See "R3 and R4 done" at the end. Owner: "an error logger/reporter for users that they can opt in. It should send me everything about the error and device, no personal information, over Wi-Fi HTTPS", then "go with the Cloudflare Worker … get as much information as possible … not only kernel level, also everything that happens in Reborn". Audit row ERROR-REPORTS in [roadmap-gap-audit](https://innioasis.app/post_install.html?url=https%3A%2F%2Fgithub.com%2Fschulzcode%2Fy2linux%2Fblob%2FHEAD%2Fdocs%2Fplanning%2Froadmap-gap-audit.md).

## Decisions (owner, 2026-10-18)``

| Topic | Decision |
| --- | --- |
| Receiver | Cloudflare Worker + R2 at reports.schulzcode.dev (the domain is already on Cloudflare). The home server was checked and is well maintained, but it is home/Tailscale-only today, and opening Nginx Proxy Manager to the internet would expose every proxy host (none has an access list) and put the home IP into the firmware. |
| Content | Scrubbed raw logs: everything the player records (kernel, platform, recovery/update, Reborn), hardware IDs and live state, with personal data replaced (below). |
| Sending | Automatic + manual: an error queues a report that uploads in the background over Wi-Fi; Settings has Send Report Now. Only after the user opted in. |
| Linking | Random install ID, made on the player (never derived from a serial), shown in Settings and resettable. |
| Asking | One question after the update, then the switch in Settings (see Further decisions). |

## What a report contains

One gzip-compressed tar per report, `report.json` (index, identity, trigger, section sizes and scrub counts) plus one file per section. Budget 2 MiB compressed (8 MiB until the cost review of 2026-10-19; real reports ≈0.5 MB); a section that does not fit is cut from the oldest end and the cut is recorded.

### Identity and trigger
  - Report schema, report ID (random), install ID, trigger class and detail (see When), wall time (UTC) and uptime,

boot ID, boot count, UTC offset (not the zone name).
  - Release, update sequence, Y2Linux and Reborn commits, kernel and root filesystem versions, build ID; update state

(`/data/updates/state.json`: state, sequence, previous sequence, timings, failure).

### Hardware
  - SoC and CPU revision, RAM, panel (`panel_kind`, LK's `lcm=` token and `panel=`), stock bootloader identity (SHA-256

of LK and preloader regions: tells 3.2.0 from 3.2.1 units, #45/#46).
  - eMMC: name, manfid, oemid, PRV, firmware, date, size, EXT_CSD feature bytes and life/EOL. Not the CID serial.
  - SD card: manfid, oemid, name, date, size, bus mode. Not the CID serial.
  - MT6323 CID, CS43131 revision, APT32F firmware, CONSYS chip/HVR/FVR, input devices, partition table.
  - Battery and charger: voltage, current, the charger's raw readings (`baton_raw`, `isense_raw`, source), capacity,

temperatures, thermal zones.

### Kernel
  - The whole kernel ring buffer (`dmesg`, 1 MiB buffer), the persistent crash record of the previous boot

(`/sys/fs/pstore/*`), `/data/logs/system.log` and `system.log.0`.
  - Taint, warning count, `/proc` state: version, cmdline, meminfo, vmstat, loadavg, interrupts, softirqs, cpuinfo,

pressure; suspend statistics and wakeup sources; cpuidle and cpufreq statistics (time in state); regulator and clock summaries (debugfs); mounts and space; ext4 error counts; process list with RSS and CPU time.
  - Y2 driver status nodes already used by the platform: SPM, CIRQ, USB (`status`, `rxdiag`), MMC, connectivity

(`/sys/devices/platform/18070000.connectivity/status`), panel parameters, codec registers (`regmap` of 1-0030), `y2_boot`.

### Platform (Y2Linux services)
  - Health (`y2-platform health`), the existing allowlisted tester export (`diagnostics.py`), boot record

(`boot.json`, `previous-boot-evidence.json`, `/run/y2/boot-stages.jsonl`, `boot-trace.jsonl`), the retained per-boot archives (`/data/system/platform/retained/*.tar`).
  - Power: `power-journal.jsonl` and `sleep-diagnostics.jsonl` (last 1 MiB of each), `suspend-last.json`,

`product-sleep-guard.json`, `power-features.json`, `rtc-policy.json`, `time-last.json`, `battery-ui.json`.
  - Update and recovery: `/data/updates/*.json` (state, recovery-last, boot-check-last, download, last-check,

restart), `/data/logs/recovery-last.log`, `recovery-display.txt`, `/run/y2/update-*.json`.
  - Every runtime state file in `/run/y2` (`*.json`, `*.jsonl`, `*.log`: connectivity, wifi, dhcp, network,

coexistence, codec runtime, media and storage, MTP events, USB transfer, time, readiness, ssh), scrubbed.

### Reborn
  - All Reborn logs (`/data/reborn/logs/*.jsonl`: current, previous-1, previous-2, splash and startup, ≈2.1 MiB;

every subsystem: playback, alsa, audio, power, wifi, bluetooth, scanner, graphics, startup, …).
  - The last crash (`panic-last.json`) and the latest diagnostic bundles (`/data/reborn/diagnostics/*.tar.gz`).
  - Live state from the control socket: `rebornctl status`, `health`, `metrics`, `audio`, `snapshot`, `events`.
  - Settings from `session.json`, projected: every setting value, the queue length and position, the output kind,

the current track's technical data (codec, rate, bits, channels, duration, ReplayGain present), never titles, artists, paths, playlists or account data. Last.fm: only signed-in yes/no and queue counts.
  - Library statistics from `library.db`: counts per codec, sample rate, bit depth and source, scan errors by class,

database size and schema version. No names.

## What is never sent, and how

Two layers, both in one module (`tools/platform/y2_platform/report.py`, `scrub()`), applied to every byte of every section before it is written:
  - Known secrets of this player, collected at report time and replaced wherever they appear: saved Wi-Fi

network names and passphrases, the current BSSID, Bluetooth device names and addresses (paired and seen), the Last.fm user name and session key, the SSH key comment, the hostname, the player's own MAC and IP addresses. Exact-match is robust where a pattern is not (an SSID can be any text).
  - Patterns: MAC addresses (keep the first three bytes, the maker; mask the rest), IPv4/IPv6 (keep the class:

loopback, link-local, USB `10.42.0.x`, private, public), serial-like fields (CID, `serial`, `machine-id`), e-mail addresses, URLs (keep the host, drop path and query), paths below `/media` (keep the extension: `<media>/…/*.flac`).

Replacements are stable within one report (a keyed hash: `<ssid#3fa2c1>`, `3C:22:FB:<mac#9b01e2>`, with a random key per report that is never written), so a log still shows that the same network or device came back. `report.json` counts the replacements per class.

Not collected at all: `library.db` contents, `scrobbles.jsonl`, `lastfm.json`, Wi-Fi configuration, Bluetooth bond keys, SSH keys, `/data/system/dbus/machine-id`, entropy seed, artwork caches, any file below `/media`.

Tests: canary values (an SSID, a passphrase, a Bluetooth name, a Last.fm user, a MAC, an IP, a CID, a music path) are planted in every source of a synthetic player tree, a report is built, and none may appear in it. The same runs against a copy of real logs from the owner's player kept outside Git.

## When a report is made

Only with Error Reports on. At most one report per trigger class per boot, at most five a day; the queue holds three (oldest dropped).``````````````````

| Trigger | Detected by |
| --- | --- |
| Kernel crash on the previous boot | pstore record at boot |
| Kernel warning / taint | taint flags or warning count rising |
| Unclean restart, watchdog reset | previous-boot-evidence.json (no orderly shutdown, reset cause) |
| Reborn crash or restart by its supervisor | a new panic-last.json, supervisor restart count |
| A required Reborn worker or subsystem failed | Reborn health |
| Update failed or rolled back, recovery entered | /data/updates/state.json, recovery-last.json |
| Sleep failure (a failed resume, tasks that would not freeze, a driver error other than -EBUSY; not a sleep a wake event cancelled) | /sys/power/suspend_stats |
| Radio failure (the connectivity chip reports an error) | connectivity status error= (not wifi-failure.json: it is rewritten on every connection and names the network's answers) |
| Dark display (DSI register lag, no frame) | kernel log lines of the display driver |
| Storage error (ext4 errors, eMMC I/O errors, read-only remount; not a pulled SD card) | ext4 counters, kernel log |
| Manual | Send Report Now and Save Report, no topic (since 8.10 and 8.9: every report holds everything; --topic stays optional on the command line) |

A trigger collects at once (the logs are fresh) and queues the report; uploading waits for Wi-Fi and runs at low priority (the platform's NetworkTransfer workload class), never during an update and never below 15 % battery unless charging.

## Transport
  - `POST https://reports.schulzcode.dev/v1/report`, body = the tar.gz, headers: schema, install ID, report ID,

SHA-256 of the body. TLS 1.2+ with certificate checks (the same urllib/OpenSSL path as updates), no redirects.
  - A build-wide upload key in the header (it is public, inside the firmware; it only keeps random internet traffic

out). The real protection is the Worker's limits.
  - Retry with backoff (5 min, 15 min, 1 h, 3 h, then every 6 h; after a 429 the next UTC day), give up after 3 days;

a refused report is dropped. Settings shows the last report's state (waiting, sent, couldn't be sent).

## The Worker
  - `POST /v1/report` only. Checks: method, path, upload key, `Content-Length` ≤ 2 MiB, gzip magic, schema version,

install ID format, body SHA-256. Budget in a Durable Object (exact): 100 reports and 40 MiB a day for the whole service, 10 a day per install ID, 30 per network (IPv4 address or IPv6 /64). See "Cost review" at the end.
  - Stores `reports/YYYY-MM-DD/<install-id>/<report-id>.tar.gz` in a private R2 bucket with small metadata (schema,

release, trigger, size). It stores no IP address and has no read endpoint.
  - R2 lifecycle: delete after 180 days. Request logs off (`[observability] enabled = false`): they would hold IPs.
  - The maintainer reads with an R2 API token (S3 API): `tools/reports/fetch.py` downloads new reports to

`out/reports/` (or a scheduled pull to the home server).
  - Code in `tools/reports/worker/` (JavaScript, `wrangler.toml`, unit tests with `node --test`); the owner deploys it

with `wrangler deploy` in his Cloudflare account.

## Player settings and screens

Settings → About & Updates → Error Reports: the switch (off by default), What is sent (a short list and a link to the privacy note), the install ID with New ID, Send Report Now, and the last report's state (queued, sent with its ID, failed with the reason). Reborn talks to the platform through its existing client (`client::Reply`), like updates. State: `/data/system/platform/reports.json` (switch, install ID, counters), queue in `/data/system/platform/reports/`.

User documentation: `docs/ERROR-REPORTS.md` (what is sent, what never is, how to see and delete one's reports by install ID: a request on GitHub with the ID).

## Steps``````````

| Step | Content | Validation |
| --- | --- | --- |
| R1 | This plan, audit row | — |
| R2 | report.py: sources, sections, scrubber, budget, triggers, queue (platform) | Host tests with canaries, size bounds, every trigger, on a synthetic tree and on a private copy of real logs |
| R3 | Worker + fetch.py | node --test; owner deploys to reports.schulzcode.dev |
| R4 | Uploader and platform commands (`y2-platform report status | send |
| R5 | Reborn screens and client calls | Reborn tests, preview screenshots |
| R6 | Device test with a test build (owner's OK): manual report, a provoked Reborn crash, an update failure from the test bench, upload to the deployed Worker, owner downloads | Device |
| R7 | Release, docs/ERROR-REPORTS.md, readme | Release checks |

## Further decisions (owner, 2026-10-18: "yes to all")
  - Players ask once after updating to the release with error reports ("Help improve Y2Linux by sending error

reports?" Yes / No); the switch in Settings stays.
  - MAC addresses keep their maker part (first three bytes).
  - R2 keeps reports 180 days.

## R2 results (2026-10-18)
  - `tools/platform/y2_platform/report.py`, `y2-platform report status|enable|disable|new-id|send [--topic]|check`,

`tests/test_error_reports.py` (in the release gate): planted canaries in every source (Wi-Fi, Bluetooth paired and unpaired, Last.fm, SSH, eMMC/CPU/machine serials, volume ID, queue titles and paths, IPs, e-mail, URL token, a file on the never-read list) never appear; removing any scrub layer fails the test (mutation-checked). Evidence kept: panic text, Reborn events, MAC makers, the USB network, text after a music file, session settings, library counts, hardware IDs. Budget cut, queue limits and every trigger tested. Host suite 813 OK.
  - Known-secret matching is one prefix-tree regex (an alternation of 2000 titles took 4 s per 200 KB; now

0.1–0.2 s per MB on the PC).
  - Real data, owner's player (read-only, `/tmp` only, removed afterwards): a full report takes 33 s (nice 10),

5.7 MB raw → ≈390 KB compressed, 162 sections, nothing cut. Harvested: 1 network, 5 Bluetooth names, the Last.fm account, 5 serials, 184 queue strings. None of the owner's Wi-Fi name, Last.fm name, headphone address, eMMC serial, home IPs, song/artist names, music paths or SD volume serial appears. Found and fixed on the way: `ctx.glob` paths were re-rooted (Bluetooth names never harvested), the 128 KiB `ctx.json` limit hid the 311-song session, the SD volume serial in Reborn's media source, an SSH key comment ("Y2Linux") blanking the product name.
  - Remaining "@"/"luca" hits are FFmpeg's `[flac @ 0x…]` prefixes and the build host in the kernel/FFmpeg version

strings (the maintainer's, part of the firmware).
  - Next: R3 (Worker), R4 (uploader + periodic `check` in the platform service).

## Test build 96 on the owner's player (2026-10-18)

`1.0.0-beta.8.8`, sequence 6950, Linux `acec57c`, Reborn `ef9e805` (identity only); container suite 786 (the new tests run there too). Installed by stage + apply, ≈16 s, Acknowledged 6950. `y2-platform report status` → `enabled: null`; `enable` made an install ID and took the baseline (`check` then reported nothing, 0.7 s); `send --topic other` built and queued a manual report in 37 s, 409 KB, 163 sections, all 13 live commands OK; the leak search on it found none of the owner's secrets. Afterwards `reports.json` and the queue were removed (state back to "not asked") and `/data/ota-96` deleted. Not released.

## R5 screens, test builds 97–98 (2026-10-18)

Reborn `8ba33b3` (screens) and `fbecb77` (question timing): About & Updates > Error Reports (switch, What Is Sent, Send Report Now with seven topics, install ID with New ID, last report state), the one-time question ("Help Improve Y2Linux?" No Thanks / Send Reports, both recorded), previews 33b–33g; 542 Reborn tests, strict Clippy. Test build 97 (sequence 6951): the question only came when a platform screen (Settings) opened, and the test's own scripted presses answered it (reset afterwards). Fixed in test build 98 (sequence 6952, Linux `d9b19cb`): one platform observation 20 s after start on any screen, and the question waits for a lit screen, no other dialog and 5 s without a button press. On the owner's player the question appeared after the restart without opening Settings; the owner answered Send Reports (21:47:25 UTC) and opened the page: install ID shown, nothing queued. Not published. Known flaky, unrelated: Reborn `lastfm::tests::requests_carry_secrets_only_on_stdin_and_errors_classify` failed once under the parallel workspace run, passes alone and on rerun.

## R3 status and the open decision (2026-10-18, end of day)

Drafted, not tested, not deployed: `tools/reports/worker/src/index.js` (POST /v1/report only; upload key in an equal-time compare; schema, UUID install/report IDs, SHA-256 and trigger checked; ≤ 8 MiB read with a hard limit; gzip magic; body hash; KV limits 10 a day per install ID and 30 per salted daily address hash; duplicate report ID = 200; R2 key `reports/YYYY-MM-DD/<install>/<report>.tar.gz` with metadata; no read route; no IP stored) and `tools/reports/worker/wrangler.toml` (route `reports.schulzcode.dev`, R2 binding `REPORTS`, KV `RATES`, secrets `UPLOAD_KEY` and `RATE_SALT`).

Still to write in R3: `node --test` tests for the Worker (fake R2/KV), `tools/reports/fetch.py` (stdlib S3 SigV4 for R2: list and download new reports into `out/reports/` or onto the home server; test with the AWS SigV4 example vector), `tools/reports/README.md` (deploy: bucket, KV namespace, secrets, custom domain, 180-day lifecycle rule), the build-wide upload key.

Owner question, open: "can this worker live on my server?" A Worker always runs on Cloudflare. Options given:
  - Worker + R2, reports pulled to the home server by a script/n8n flow (recommended: only outgoing connections at

home, no home IP in the firmware, no disk filling from fake uploads; the drafted code fits).
  - The same receiver as a small container on the home server behind a Cloudflare Tunnel publishing only

`reports.schulzcode.dev` (no port forward, NPM not involved; uploads land at home, the server must be online, one more internet-facing service).
  - Port forward (advised against: every NPM proxy host would be exposed, home IP in the firmware).

The validation and limits are the same in 1 and 2; only the storage differs. Decide before finishing R3.

## Save to storage and speed, Beta 8.8 (2026-10-19)

Owner: "publish the next beta with what we have currently and export to storage feature either internal or sd card, we will do the worker afterwards", then "40-50 seconds is too long".
  - Save Report (`y2-platform report save --to internal|sd [--topic]`, Linux `190d713`, `d06c606`): the same

report, written to `Error Reports/y2linux-report-<local time>.tar.gz` at the MTP top level of the storage (Internal Storage is `/media/internal/music` in `umtprd.conf`; the first device run wrote to `/media/internal` and MTP did not show it). User-initiated, so no opt-in and nothing queued; the install ID only when reports are on. Real directories only (`O_NOFOLLOW`, same filesystem), written as `.part`, renamed, folder fsynced. `report status` adds `upload` (false) and `destinations`. Reports also hold `BAT0/charging_state` (#47).
  - Reborn (`6cca742`, `b6b6fbc`): Error Reports → Save Report → storage → topic. While `upload` is false only Save

Report and What Is Saved show; the switch, Send Report Now, the install ID and the one-time question come back when the platform reports `upload: true` (R4).
  - Speed (`be71b6d`): ≈47 s → ≈10 s. Profile on the player: 71 of 77 s in scrubbing, 354 000 `text()` calls on

JSON-lines values, 2.8 M `re.sub`; each pattern scans 2–3.5 MB/s on the Y2. Now JSON lines are scrubbed as one text (private keys' string values replaced in the text; private keys holding lists/objects and Bluetooth peers still value by value; known values also in JSON-escaped form), logs are cut at line ends into 256 KB pieces for 4 forked workers, tokens are keyed hashes, the live commands run during the scrub, `send`/`save` run at nice 10. On 6 973 real lines the text path equals the value path (tokens aside); no private value in five device reports.
  - Boot ID: a `/run/y2` record names it and it has an ext4 UUID's shape, so it was harvested as a volume serial;

it is discarded now.
  - Next: R3 (Worker tests, `fetch.py`, README, owner's receiver decision), R4 (uploader, periodic `report check`,

then `UPLOAD = True` in `report.py`, which brings the switch and question back in Reborn).

## R3 and R4 done (2026-10-19, `main`, unreleased)

Owner: "option 1, do all you can do also check the plan and code again with the changes we made".
  - Worker (`tools/reports/worker`): rate limits now count only valid reports (before, a broken upload the

player retried used up its day); request logs off; `package.json` and 11 `node --test` tests with a fake R2 and KV (storage key and metadata, duplicate report ID, no read route, exact key, every header check, gzip/length/hash, the 8 MiB cut-off without buffering, both daily limits, no address stored, 500 without details).
  - `fetch.py`: read-only S3 client for R2 (SigV4 in the standard library; three published AWS signing examples

match), downloads new reports to `<day>/<install>/<report>.tar.gz`, checks the Worker's SHA-256, refuses keys that are not report-shaped. 7 tests.
  - Upload key: `tools/reports/new_upload_key.py` writes `~/.local/share/y2linux/report-upload.json`; the release

build installs it as `/usr/share/y2linux/report-upload.json` (0600, like the Last.fm key). `report status` says `upload: true` only when the image has it, which replaces the planned `UPLOAD = True`: forks and builds before the Worker exists stay save-only.
  - Uploader (`report.upload`, `NetworkTransfer` workload, one at a time): opt-in, Wi-Fi online this boot, TLS

clock, no update, ≥ 15 % or charging; HTTPS with certificate checks, no proxy, no redirects; headers from the report's own `report.json`; outcomes `sent` / `failed` (retry) / `dropped` (refused or 3 days old) in `last`. `report send` tries at once; `report upload` and `report work` (checks + upload) added.
  - Service: `report work` in its own process 2 min after start, then every 15 min, sooner when a queued report

is due and Wi-Fi is online (at most every 5 min), stopped after 10 min. Nothing without the key and opt-in.
  - Trigger review against the owner's player: `wifi-failure.json` is rewritten on every Wi-Fi connection (it

exists on the player now with `error: null`): it would have sent a "radio problem" on every boot; dropped. `suspend_stats/fail` also counts sleeps a wake event cancelled (-EBUSY): now only failed resumes, freeze failures and other errors. Storage I/O errors only for the eMMC (a pulled SD card logs them too). Taint 0, `console-ramoops-0` without a crash line, no dark-display or storage lines on the player.
  - Reborn: "Report sent" after Send Report Now when it went out at once; "couldn't be sent" for a dropped one.
  - Tests: `tests/test_report_upload.py` (a local HTTPS receiver with a throwaway certificate: identity headers,

every wait condition, backoff, 429, refusal, expiry, redirect, untrusted certificate, damaged file, lock, the service schedule, the build step, the key maker, triggers/schema/size equal in Worker and player), `tests/test_report_fetch.py`, both in the release gate.
  - Next: the owner deploys (`tools/reports/README.md`, ≈15 min), then R6: a test build with the key, Send

Report Now on the owner's player, `fetch.py` downloads it, a provoked trigger. Then R7: user guide (`docs/ERROR-REPORTS.md` "Sending reports"), release.

## Deployed and cost review (2026-10-19)

The owner deployed the Worker (R2 bucket `y2linux-reports` in EEUR, Standard storage, private: no r2.dev URL, no custom domain), set the secrets and made a read-only R2 token for `fetch.py`. Checked from the PC: with the key and a broken body 400 `not_gzip`, a wrong key 403, GET 405, other paths 404; the token lists the bucket and a DELETE is refused (403). Found missing: the 180-day lifecycle rule (only Cloudflare's default multipart rule).

Owner: "check if its moste secure not only the code but also rate limiting, so that i dont rack up cost in any case? i have the free tier". Workers and Durable Objects on the Free plan fail past their limits; R2 bills past 10 GB-month and 1 M class A operations. The upload key is public (in every image), so an attacker with fresh install IDs and addresses was bounded only by the KV free tier (1 000 writes a day ≈ 333 reports × 8 MiB ≈ 2.6 GB a day; KV counters are also not atomic and read stale for up to a minute, so concurrent uploads could overshoot), and 8 MiB risked the Free plan's 10 ms CPU per request for the hash. Changes:
  - `Quota` Durable Object (SQLite, Free plan): one exact daily budget, 100 reports and 40 MiB for the whole

service (× 180 days ≈ 7 GiB < 10 GB), within it 10 per install ID and 30 per network; earlier days deleted. KV is no longer used (namespace `RATES` can be deleted). Duplicates are found with an R2 head (class B).
  - 2 MiB per report in the Worker and on the player (`report.BUDGET`; real reports ≈0.5 MB).
  - IPv6 per /64, since one connection gets a whole /64.
  - `preview_urls = false` besides `workers_dev = false`.
  - Owner steps added to `tools/reports/README.md`: the lifecycle rule (wrangler command), a WAF rate-limiting rule

(10 requests / 10 s per IP on the hostname, Free plan: one rule), a usage-based billing alert for R2 storage at 8 GB. Cost table in the README.
  - 14 Worker tests (new: budget under 150 concurrent uploads from new IDs and addresses, byte budget with

incompressible bodies, next-day reset, IPv6 grouping, nothing counted for refused or duplicate uploads).

## No topic, live progress, test build 103 (2026-10-19)

Owner: "i also dont wnat to choose a topic for the automatic upload, it should just do it. also i want like the update player page to see the progress of creatign the report and uploading it / saving ti to dc or internal".
  - No topic for Send Report Now (Reborn): `PlatformTask::ReportSend` without a topic, `Screen::ReportTopic` and

`ReportTopic` removed (skins: `report_topic` gone from the screen list); `y2-platform report send` runs without `--topic` (still accepted).
  - Live progress (platform `report.Progress`, `/run/y2/report-progress.json`, schema 1): `phase`

collect/scrub/pack/upload/save, `percent` of the whole run (collect 0–12, scrub 12–76 by bytes cleaned, pack 76–82, upload or save 82–100; upload by bytes sent through a streamed request body), `seconds_left` (from the elapsed time once ≥ 15 %), `bytes_done`/`bytes_total`; at most five writes a second, only for `send` and `save` (never for background reports), removed when the run ends. The scrub reports by bytes with `imap_unordered`.
  - Reborn: `client::report_progress` polled every 200 ms while the task runs (like the update download), drawn

like the update screen: steps Collect · Clean · Send (or Save), title per step, percent, gliding bar, detail ("260 of 504 KB", "Into the Error Reports folder."), time left. Previews 33f, 33l–33o. 545 tests.
  - Test build 103 (`1.0.0-beta.8.10`, sequence 7200, Linux `10b8cc7`, Reborn `bff7831`, 821 container tests,

upload key included): installed on the owner's player (Acknowledged, `upload: true`). The owner pressed Send Report Now: built in ≈10 s (503 KB), upload refused by DNS (`gaierror`): the router still served the "no such name" it had cached before the Worker existed (SOA minimum 1800 s); retried by the service afterwards. The topic and progress changes above came after build 103.

Test build 104 (`1.0.0-beta.8.10`, sequence 7300, Linux `7846476`, Reborn `cfac12b`, 825 container tests): no topic, live progress, the narrower display trigger. Installed (Acknowledged 7300). Send Report Now: made 15:13:36, in R2 15:13:48 (≈12 s, 523 KB, 166 sections, `topic: null`); the progress record removed afterwards. Leak search on the player for both received reports: 0 of 203 private values. The first automatic report (display_failure, 14:55, from build 103) was the boot-time DSI read lag after the restart through the recovery (the driver worked around it, the panel lit): the trigger now needs Reborn's first frame to be missing; the lag itself after a recovery restart is a finding for the display work. Afterwards: Send Report Now goes first and, once it is stored, takes the waiting reports along regardless of their retry time (the build-103 report waited 15 min in backoff behind it); the progress follows the new report only.

## R7: released in Beta 8.10 (2026-10-19)

Owner: "publish without it and answer the issue without it" (without a wall-charger test on build 105). Build 105 = `baseline-105`, sequence 7400, upload key included: players are asked once after updating. User guide section "Send reports over Wi-Fi". Still owed: Cloudflare WAF rate-limit rule and R2 billing alert (owner), the progress page checked by eye, the question on a player that never answered.

These are Reborn (Y2Linux)'s own instructions, shown here word for word.

Published by the [schulzcode/y2linux](https://innioasis.app/firmware.html?model=Y2&software=reborn-y2linux-y2) project [[1]](https://innioasis.app/firmware_info.html?repo=schulzcode%2Fy2linux&software=reborn-y2linux-y2)[[3]](https://github.com/y1-community/Innioasis-Updater/pulls?q=is%3Apr%20author%3Aschulzcode)

## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
