#!/usr/bin/env python3
"""Find released firmware that has no portable package for every platform.

A portable package only exists once the mirror has built it, and the site
shows "This download is being prepared" until then. That is the right message
for a fresh release, but it should never be the answer a day later, and a new
flash-tool seed has to reach the mirrors even when no project published
anything.

This script is the check that closes that gap. For every firmware row in
``slidia_manifest.xml`` it compares the source repository's releases with the
mirror's ``index.json``:

* a release tag the mirror has not processed at all;
* a ZIP added to a tag the mirror already processed;
* a package missing for one of the platform keys the mirror declares;
* a mirror that does not exist yet, for a row that was just added;
* an ``index.json`` generated before the flash-tool seed's newest release.

Release data comes from the generated backup feeds (``feeds/<owner>/<repo>/
releases.json``) when they exist, so a run costs no GitHub API quota; fall back
to the API with ``--refresh``.

Usage:
    python scripts/portable_audit.py                        # report only
    python scripts/portable_audit.py --report out.json --summary "$GITHUB_STEP_SUMMARY"
    python scripts/portable_audit.py --dispatch             # ask the mirrors to rebuild
    python scripts/portable_audit.py --dispatch --dry-run    # say what it would ask
    python scripts/portable_audit.py --strict               # exit 1 when anything is behind

``--dispatch`` posts ``repository_dispatch`` events the mirror workflow listens
for: ``firmware-release`` for a source that is behind, ``portable-seed`` when
only the flash tool changed. It needs a token that can write to the mirror
repositories (``GH_TOKEN``); without one the run reports the gaps and says who
would have been asked. The central packager watcher still picks the work up on
its own schedule, so a missing token delays packages rather than losing them.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import pathlib
import subprocess
import sys
import time
import urllib.error
import urllib.request

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
import portable_manifest as pm  # noqa: E402

MANIFEST = ROOT / "slidia_manifest.xml"
FEEDS = ROOT / "feeds"
CACHE = ROOT / ".cache" / "portable-audit"
API = "https://api.github.com"
RAW_INDEX = "https://raw.githubusercontent.com/%s/%s/index.json"
DEFAULT_SEED_REPO = "y1-community/updater-ce-neo"

#: The site's own firmware naming convention: the project's ROM ZIP.
ROM_NAME_RE = re.compile(r"^rom.*\.zip$", re.I)
NOT_A_PACKAGE_RE = re.compile(r"sources?|legal-info|sha256|checksums?|mirror", re.I)
PLATFORM_SUFFIX_RE = re.compile(
    r"-(?:windows(?:-arm64|-legacy)?|macos|linux(?:-arm64|-legacy)?)\.zip$", re.I)
#: An app-store placeholder row, not a firmware. The site and the packager both
#: skip it, so the audit must not ask for a package it can never have.
PLACEHOLDER_RE = re.compile(r"please[- ]?(?:click|update)", re.I)


def now() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def token() -> str:
    for name in ("GH_TOKEN", "GITHUB_TOKEN"):
        value = (os.environ.get(name) or "").strip()
        if value:
            return value
    return ""


def is_zip(name: str) -> bool:
    """Whether this release asset is a ZIP a mirror could repack."""
    value = str(name or "").strip()
    if not value or NOT_A_PACKAGE_RE.search(value) or PLATFORM_SUFFIX_RE.search(value):
        return False
    return value.lower().endswith(".zip")


def shape(name: str) -> str:
    """An asset name with its version numbers removed.

    ``Y2Linux-1.0.0-beta.8.8-first-install.zip`` and its next beta share one
    shape, so a project that names every build differently is still recognised
    as packaging the same thing. ``system.zip`` has no numbers and keeps its
    own shape, which is how the Y2Player system images stay out of the audit
    while Y2Linux's first-install archives stay in.
    """
    return re.sub(r"\d+", "#", str(name or "").lower())


def http_json(url: str, token_value: str = "", cache_minutes: int = 0):
    """GET JSON, optionally through a short disk cache. Returns (payload, error)."""
    cached = None
    digest = hashlib.sha1(url.encode("utf-8")).hexdigest()
    if cache_minutes:
        CACHE.mkdir(parents=True, exist_ok=True)
        cached = CACHE / ("%s.json" % digest)
        if cached.exists() and (time.time() - cached.stat().st_mtime) < cache_minutes * 60:
            try:
                return json.loads(cached.read_text(encoding="utf-8")), ""
            except (OSError, json.JSONDecodeError):
                pass
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "innioasis-portable-audit",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token_value:
        headers["Authorization"] = "Bearer " + token_value
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.loads(response.read().decode("utf-8", "replace"))
    except urllib.error.HTTPError as error:
        if cached is not None and cached.exists():
            try:
                return json.loads(cached.read_text(encoding="utf-8")), "HTTP %d" % error.code
            except (OSError, json.JSONDecodeError):
                pass
        return None, "HTTP %d" % error.code
    except Exception as error:  # noqa: BLE001 - a missing feed is not fatal
        return None, str(error)
    if cached is not None:
        try:
            cached.write_text(json.dumps(payload), encoding="utf-8")
        except OSError:
            pass
    return payload, ""


def feed_releases(repo: str) -> list[dict] | None:
    path = FEEDS / repo.lower() / "releases.json"
    if not path.exists():
        return None
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return payload if isinstance(payload, list) else None


def github_releases(repo: str, token_value: str) -> list[dict] | None:
    collected: list[dict] = []
    for page in range(1, 4):
        payload, error = http_json(
            "%s/repos/%s/releases?per_page=100&page=%d" % (API, repo, page),
            token_value, cache_minutes=15)
        if error or not isinstance(payload, list):
            break
        collected.extend(entry for entry in payload if isinstance(entry, dict))
        if len(payload) < 100:
            break
    return collected or None


def releases_for(repo: str, token_value: str, refresh: bool) -> tuple[list[dict] | None, str]:
    """A repository's releases, from the local feed first."""
    if not refresh:
        cached = feed_releases(repo)
        if cached is not None:
            return cached, "feed"
    payload = github_releases(repo, token_value)
    if payload is None and not refresh:
        cached = feed_releases(repo)
        if cached is not None:
            return cached, "feed"
    if payload is None:
        return None, "unreadable"
    return payload, "api"


def mirror_index(mirror: str) -> tuple[dict | None, str]:
    """The mirror's ``index.json``; the packager commits it on every run."""
    for branch in ("main", "master"):
        url = RAW_INDEX % (mirror, branch)
        payload, error = http_json(url, cache_minutes=10)
        if isinstance(payload, dict) and payload:
            return payload, ""
        if error in ("HTTP 404",):
            continue
        if error:
            return None, error
    return None, "missing"


def releases_of(releases: list[dict]) -> list[dict]:
    return [rel for rel in releases
            if isinstance(rel, dict) and not rel.get("draft") and rel.get("tag_name")]


def package_map(index: dict) -> dict[str, dict[str, set[str]]]:
    """tag -> source asset (lowercase) -> platform keys the mirror published."""
    mapping: dict[str, dict[str, set[str]]] = {}
    for release in index.get("releases") or []:
        if not isinstance(release, dict):
            continue
        tag = str(release.get("tag") or release.get("tag_name") or "").strip()
        if not tag:
            continue
        assets = mapping.setdefault(tag, {})
        for asset in release.get("assets") or []:
            if not isinstance(asset, dict):
                continue
            source = str(asset.get("source_asset") or asset.get("name") or "").strip().lower()
            platform = str(asset.get("platform") or "").strip()
            if source:
                assets.setdefault(source, set()).add(platform)
    return mapping


def audit_row(source: str, mirrors: list[str], token_value: str,
              refresh: bool, seed_repo: str, seed_releases: list[dict] | None) -> dict:
    releases, origin = releases_for(source, token_value, refresh)
    if releases is None:
        return {"source_repo": source, "mirrors": mirrors, "state": "unknown-source",
                "error": "release list unreadable", "gaps": []}

    source_releases = releases_of(releases)
    wanted: dict[str, list[str]] = {}
    for release in source_releases:
        assets = [str(asset.get("name") or "") for asset in release.get("assets") or []
                  if isinstance(asset, dict) and is_zip(asset.get("name"))]
        if assets:
            wanted[str(release.get("tag_name")).strip()] = assets

    if not wanted:
        return {"source_repo": source, "mirrors": mirrors, "state": "nothing-to-package",
                "releases": origin, "gaps": []}

    result: dict = {
        "source_repo": source,
        "mirrors": mirrors,
        "state": "ok",
        "releases": origin,
        "tags_needing_package": len(wanted),
        "gaps": [],
        "mirror_states": {},
        "dispatch": "none",
    }

    seed_newest = ""
    for release in seed_releases or []:
        published = str(release.get("published_at") or "")
        if published > seed_newest:
            seed_newest = published

    for mirror in mirrors:
        index, error = mirror_index(mirror)
        if index is None:
            state = "mirror-missing" if error == "missing" else "index-unreadable"
            result["mirror_states"][mirror] = {"state": state, "error": error}
            if state == "mirror-missing":
                result["gaps"].append({
                    "kind": "mirror-missing",
                    "mirror": mirror,
                    "detail": "the mirror repository or its index.json does not exist yet",
                })
                result["state"] = "behind"
            continue

        declared = {str(entry.get("key") or "") for entry in index.get("platforms") or []
                    if isinstance(entry, dict) and entry.get("key")}
        published = package_map(index)
        mirror_gaps: list[dict] = []

        # What this mirror actually publishes, per source asset shape. A mirror
        # may declare Windows on ARM and the legacy bundle without ever
        # building them, and demanding them for every release would report a
        # permanent backlog nobody can clear. The package that exists is the
        # contract; a delivery that drops a platform it normally ships is not.
        shapes: dict[str, set[str]] = {}
        for tag_assets in published.values():
            for name, platforms in tag_assets.items():
                shapes.setdefault(shape(name), set()).update(platforms)
        observed = set().union(*shapes.values()) if shapes else set()
        expected = observed or declared

        def required_platforms(asset: str) -> set[str]:
            return shapes.get(shape(asset)) or expected

        for tag, assets in sorted(wanted.items()):
            required_assets = [name for name in assets
                               if ROM_NAME_RE.match(name) or shape(name) in shapes]
            if not required_assets:
                # A release that carries only something the mirror never
                # packages (Y2Player's system images) is not behind.
                continue
            entry = published.get(tag)
            if entry is None:
                mirror_gaps.append({
                    "kind": "release",
                    "mirror": mirror,
                    "tag": tag,
                    "assets": required_assets,
                    "missing_platforms": sorted(expected),
                })
                continue
            for asset in required_assets:
                have = entry.get(asset.lower(), set())
                missing = sorted(required_platforms(asset) - have)
                if missing:
                    mirror_gaps.append({
                        "kind": "asset-platforms",
                        "mirror": mirror,
                        "tag": tag,
                        "asset": asset,
                        "missing_platforms": missing,
                        "reason": "asset not in the mirror" if not have else "platform package missing",
                    })

        generated_at = str(index.get("generated_at") or "")
        seed_repo_for_mirror = str(index.get("updater_repo") or seed_repo)
        seed_stale = bool(seed_newest and generated_at and seed_newest > generated_at
                          and seed_repo_for_mirror.lower() == seed_repo.lower())

        result["mirror_states"][mirror] = {
            "state": "behind" if mirror_gaps else "ok",
            "releases_indexed": len(published),
            "platforms": sorted(declared),
            "generated_at": generated_at,
            "seed": "stale" if seed_stale else "current",
        }
        if mirror_gaps:
            result["gaps"].extend(mirror_gaps)
            result["state"] = "behind"
            result["dispatch"] = "firmware-release"
        elif seed_stale:
            result["mirror_states"][mirror]["state"] = "seed-stale"
            result["state"] = "behind" if result["state"] == "behind" else "seed-stale"
            if result["dispatch"] == "none":
                result["dispatch"] = "portable-seed"

    return result


def dispatch(mirror: str, event_type: str, reason: str, dry_run: bool) -> dict:
    if dry_run:
        return {"mirror": mirror, "event": event_type, "result": "dry-run"}
    command = [
        "gh", "api", "-X", "POST", "repos/%s/dispatches" % mirror,
        "-f", "event_type=%s" % event_type,
        "-f", "client_payload[reason]=%s" % reason[:200],
    ]
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired) as error:
        return {"mirror": mirror, "event": event_type, "result": "error",
                "error": str(error)[:300]}
    if result.returncode == 0:
        return {"mirror": mirror, "event": event_type, "result": "dispatched"}
    detail = (result.stderr or result.stdout or "").strip().replace("\n", " ")
    return {"mirror": mirror, "event": event_type, "result": "error",
            "error": detail[:300]}


def summarize(rows: list[dict], dispatch_log: list[dict]) -> str:
    lines = ["## Portable packages", ""]
    behind = [row for row in rows if row.get("state") in ("behind", "seed-stale")]
    unknown = [row for row in rows if row.get("state") == "unknown-source"]
    if not behind and not unknown:
        lines.append("Every listed firmware has a portable package for every platform "
                     "its mirror publishes.")
        return "\n".join(lines) + "\n"

    if behind:
        lines += ["| Firmware | Source | State | Missing |", "| --- | --- | --- | --- |"]
        for row in behind:
            missing = []
            for gap in row.get("gaps") or []:
                if gap["kind"] == "mirror-missing":
                    missing.append("mirror not created")
                elif gap["kind"] == "release":
                    missing.append("%s (no package)" % gap["tag"])
                else:
                    missing.append("%s %s: %s" % (gap["tag"], gap["asset"],
                                                  ", ".join(gap["missing_platforms"])))
            lines.append("| %s | %s | %s | %s |" % (
                row["source_repo"].split("/")[-1], row["source_repo"],
                row.get("state"), "; ".join(missing[:4]) or "seed only"))
    if unknown:
        lines += ["", "Could not read releases for: " +
                  ", ".join("`%s`" % row["source_repo"] for row in unknown)]
    if dispatch_log:
        lines += ["", "| Mirror | Event | Result |", "| --- | --- | --- |"]
        for entry in dispatch_log:
            lines.append("| `%s` | `%s` | %s |" % (
                entry["mirror"], entry["event"],
                entry.get("error") or entry["result"]))
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Check every manifest firmware for portable packages.")
    parser.add_argument("--manifest", default=str(MANIFEST))
    parser.add_argument("--seed-repo", default=DEFAULT_SEED_REPO,
                        help="repository whose releases are the portable app seed")
    parser.add_argument("--only", default="", help="comma separated source repositories")
    parser.add_argument("--refresh", action="store_true",
                        help="read the GitHub API instead of the local feeds")
    parser.add_argument("--dispatch", action="store_true",
                        help="ask behind mirrors to rebuild")
    parser.add_argument("--dry-run", action="store_true",
                        help="report the dispatch calls without making them")
    parser.add_argument("--report", default="portable-audit.json",
                        help="write the JSON report here (default: portable-audit.json)")
    parser.add_argument("--summary", default="",
                        help="append a Markdown summary here (e.g. $GITHUB_STEP_SUMMARY)")
    parser.add_argument("--strict", action="store_true",
                        help="exit 1 when any firmware is behind")
    args = parser.parse_args()

    text = pathlib.Path(args.manifest).read_text(encoding="utf-8")
    entries = pm.parse_entries(text)
    wanted = {item.strip().lower() for item in args.only.split(",") if item.strip()}

    rows: list[dict] = []
    seen: set[tuple[str, tuple[str, ...]]] = set()
    for entry in entries:
        attrs = entry["attributes"]
        source = (attrs.get("repo") or "").strip().strip("/")
        if not source or (attrs.get("type") or "").strip().lower() == "apk":
            continue
        if PLACEHOLDER_RE.search(source) or PLACEHOLDER_RE.search(attrs.get("name") or ""):
            continue
        mirrors = [value.strip() for key in pm.MIRROR_ATTRS
                   for value in re.split(r"[\s,]+", attrs.get(key) or "")
                   if value.strip()]
        if not mirrors:
            print("  ! %s has no portable mirror; run scripts/portable_manifest.py --apply"
                  % source, file=sys.stderr)
            continue
        key = (source.lower(), tuple(sorted(mirror.lower() for mirror in mirrors)))
        if key in seen:
            continue
        if wanted and source.lower() not in wanted and not any(
                mirror.lower() in wanted for mirror in mirrors):
            continue
        seen.add(key)
        rows.append({"source_repo": source, "mirrors": mirrors})

    token_value = token()
    seed_releases, _seed_origin = releases_for(args.seed_repo, token_value, args.refresh)

    audited: list[dict] = []
    for row in rows:
        result = audit_row(row["source_repo"], row["mirrors"], token_value,
                           args.refresh, args.seed_repo, seed_releases)
        audited.append(result)
        print("  %-9s %-38s %s" % (
            result.get("state"),
            result["source_repo"],
            ", ".join(sorted({gap.get("tag") or gap["kind"]
                              for gap in result.get("gaps") or []}))[:70]))

    dispatch_log: list[dict] = []
    if args.dispatch:
        for row in audited:
            if row.get("dispatch") in ("none", None) or row.get("state") not in ("behind", "seed-stale"):
                continue
            for mirror in row["mirrors"]:
                state = (row.get("mirror_states") or {}).get(mirror) or {}
                if state.get("state") not in ("behind", "seed-stale"):
                    continue
                event = "firmware-release" if state["state"] == "behind" else "portable-seed"
                dispatch_log.append(dispatch(mirror, event, row["source_repo"], args.dry_run))
        for entry in dispatch_log:
            print("  dispatch %-34s %-16s %s"
                  % (entry["mirror"], entry["event"],
                     entry.get("error") or entry["result"]))
        if not dispatch_log:
            print("  nothing to dispatch: every mirror is current.")

    report = {
        "generated_at": now(),
        "seed_repo": args.seed_repo,
        "rows": audited,
        "dispatched": dispatch_log,
        "behind": [row["source_repo"] for row in audited
                   if row.get("state") in ("behind", "seed-stale")],
    }
    if args.report:
        pathlib.Path(args.report).write_text(
            json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if args.summary:
        with open(args.summary, "a", encoding="utf-8") as handle:
            handle.write(summarize(audited, dispatch_log))

    behind = report["behind"]
    print("%d firmware row(s) checked, %d behind." % (len(audited), len(behind)))
    if args.strict and behind:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
