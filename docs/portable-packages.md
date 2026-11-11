# Portable packages: the one-line contract

A project publishes one ROM ZIP. The archive offers the reader a build for
their own computer: the same ROM beside the flashing tool for Windows, macOS,
Intel Linux or ARM64 Linux. Those builds live in a mirror repository, one per
source project, and the site only finds them through `slidia_manifest.xml`.

## Enrolling a firmware

Add its line to `slidia_manifest.xml`:

```xml
<package name="Rondo" repo="jarvissax/rondo" device="Y1" url="https://github.com/jarvissax/rondo" type="img" handler="Custom Firmware" />
```

That is the whole job. Within half an hour the `Portable packages for every
listed firmware` workflow writes the mirror the row is missing:

```xml
<package name="Rondo" repo="jarvissax/rondo" portable_zips="y1-community/rondo-mirror" device="Y1" ... />
```

and asks `y1-community/rondo-mirror` to rebuild. Changing the `repo` in an
existing line is the same case: the mirror attribute stays, the audit sees that
the new source's releases are not in the mirror's index, and the mirror is asked
to package them again.

The name is derived, never hand-written: `<product>-mirror` in
`y1-community`, where `<product>` is the repository name without its owner. This
is the rule the existing mirrors already follow (`y1_launcher-mirror`,
`y2-rockbox-mirror`, `koensayr-auto-mirror`). A row that already names a mirror,
including the legacy `portable_zip` spelling, is left untouched. So is a
commented-out row, an APK row, and anything not in `slidia_manifest.xml` at all.

## What runs, and when

| Workflow | Runs | Does |
| --- | --- | --- |
| `portable-packages.yml` (this repo) | On a manifest change, on `repository_dispatch`, every 30 minutes, manually | Adds the missing mirror attribute and commits it; audits every listed firmware against its mirror; dispatches the mirrors that are behind |
| `ryan-specter/inni-packager` `onboard.yml` | Every 15 minutes | Its own manifest/source/seed watcher: creates a mirror repository that does not exist yet, then dispatches it |
| `<product>-mirror` `mirror.yml` | Hourly, plus `repository_dispatch` of `firmware-release` or `portable-seed` | Builds the per-platform packages, uploads them to its releases, commits `index.json` |

The two watchers are deliberate. The packager's is the one that can create a
repository and seed its config; this repository's is the one that owns
`slidia_manifest.xml` and knows what the website needs. Both are idempotent, so
running them on top of each other only costs a skipped pass.

The site itself needs no further step: `portable-zip-links.js` reads the
mirror's `index.json` at click time, and `scripts/generate_backup_feeds.py`
folds the same index into `feeds/firmware-releases.json` on the hourly
`generate-doc-pages.yml` run that a manifest push already triggers.

## What counts as being behind

`scripts/portable_audit.py` reports a firmware when:

- a release tag in the source has a firmware ZIP that the mirror's index does
  not list at all (`release`);
- a tag the mirror already processed has a ZIP added since (`asset-platforms`);
- a listed ZIP is missing one of the platforms the mirror actually publishes
  for that kind of file (`asset-platforms`). A mirror's `index.json` declares
  Windows on ARM and the legacy bundle whether or not it builds them, so the
  audit measures what it ships, not what it advertises: a release that drops a
  platform the mirror normally includes is a gap, a platform it never includes
  is not;
- the row names a mirror that does not exist yet (`mirror-missing`);
- the mirror's `index.json` was generated before the newest release of the
  flash-tool seed (`y1-community/updater-ce-neo`), so every package predates the
  tool it is supposed to bundle (`portable-seed`).

A ZIP that is not a firmware package is ignored: `sources`, `legal-info`,
checksums and the mirror's own `-windows.zip`-style names. A release with no
firmware ZIP (an APK-only or notes-only release) is not a gap.

## Running it locally

```bash
# What would the manifest repair change?
python scripts/portable_manifest.py

# Who is behind? Reads feeds/<owner>/<repo>/releases.json, no API quota used.
python scripts/portable_audit.py --report /tmp/portable-audit.json

# Ask the mirrors to rebuild (needs a token that can write to them).
GH_TOKEN=... python scripts/portable_audit.py --dispatch --dry-run
GH_TOKEN=... python scripts/portable_audit.py --dispatch
```

The audit exits 0 even when a mirror is behind, because a fresh release is
normally behind for a few minutes. Pass `--strict` in a check that should fail
instead.

## When it says "about to be prepared"

`portable-zip-links.js` shows that message, and keeps the project's own ZIP
hidden, only when it read a mirror index and found no build for this computer.
A mirror that is behind therefore looks unfinished rather than broken. If a
release stays in that state for more than a couple of runs, the audit report
names the reason: a missing mirror, an unreadable index, or the exact tag and
platform that never arrived.
