#!/usr/bin/env python3
"""Name the portable mirror on every firmware row in ``slidia_manifest.xml``.

The site only offers a portable package for a row that names one: the
``portable_zips`` attribute is what ``portable-zip-links.js`` and
``scripts/generate_backup_feeds.py`` read to find the repository that
repackages each release for Windows, macOS, Intel Linux and ARM64 Linux.

The central packager (``ryan-specter/inni-packager``) already derives the same
mirror name from the source repository, so enrolling a firmware is meant to be
one line:

    <package name="Rondo" repo="jarvissax/rondo" device="Y1" ... />

This script writes the attribute that line is missing, in place and in the
order the file already uses, so the site can swap the project's own rom ZIP for
the portable one as soon as the mirror has built it. It never touches a
commented-out row, an APK row, or a row that already names a mirror (including
the legacy ``portable_zip`` spelling). It is safe to run repeatedly: a run with
nothing to add changes no bytes.

Usage:
    python scripts/portable_manifest.py              # report what is missing
    python scripts/portable_manifest.py --apply      # write the attributes
    python scripts/portable_manifest.py --check      # exit 1 when a row is bare
    python scripts/portable_manifest.py --json out.json

The organisation that owns the mirrors is ``y1-community`` unless
``PORTABLE_MIRROR_ORG`` or ``--org`` says otherwise.
"""
from __future__ import annotations

import argparse
import json
import os
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "slidia_manifest.xml"
DEFAULT_ORG = (os.environ.get("PORTABLE_MIRROR_ORG") or "y1-community").strip()

ATTR_RE = re.compile(r'([A-Za-z_][\w.:-]*)\s*=\s*"([^"]*)"')
PACKAGE_RE = re.compile(r"<package\b[^>]*>")
#: Legacy spelling, still read by Updater CE and the site.
MIRROR_ATTRS = ("portable_zips", "portable_zip")


def comment_spans(text: str) -> list[tuple[int, int]]:
    """Character ranges covered by ``<!-- ... -->`` comments."""
    spans: list[tuple[int, int]] = []
    index = 0
    while True:
        start = text.find("<!--", index)
        if start == -1:
            break
        end = text.find("-->", start + 4)
        end = len(text) if end == -1 else end + 3
        spans.append((start, end))
        index = end
    return spans


def mask_comments(text: str) -> str:
    """The manifest with comments blanked, keeping every offset and newline.

    A commented-out row must never be edited, and a row's own ``<!--`` can sit
    on an earlier line, so the decision is made per character rather than per
    line.
    """
    chars = list(text)
    for start, end in comment_spans(text):
        for position in range(start, min(end, len(chars))):
            if chars[position] not in "\r\n":
                chars[position] = " "
    return "".join(chars)


def parse_entries(text: str) -> list[dict]:
    """Every *active* ``<package/>``: its line, raw tag and attributes."""
    entries: list[dict] = []
    masked = mask_comments(text)
    raw_lines = text.splitlines(keepends=True)
    masked_lines = masked.splitlines(keepends=True)
    for number, (raw, seen) in enumerate(zip(raw_lines, masked_lines), 1):
        match = PACKAGE_RE.search(seen)
        if not match:
            continue
        tag = raw[match.start():match.end()]
        attrs = {m.group(1): m.group(2) for m in ATTR_RE.finditer(tag)}
        entries.append({
            "line": number,
            "attributes": attrs,
            "tag": tag,
            "tag_start": match.start(),
            "text": raw,
        })
    return entries


def mirror_for(repo: str, org: str = DEFAULT_ORG) -> str:
    """``jarvissax/rondo`` -> ``y1-community/rondo-mirror``.

    The packager names a mirror after the source repository, not its owner, so
    two projects with the same product name in different organisations still
    land in one predictable place. This is the same rule the existing mirrors
    follow (``y1_launcher-mirror``, ``y2-rockbox-mirror``, ``koensayr-auto-mirror``).
    """
    _owner, _slash, product = (repo or "").strip().strip("/").partition("/")
    product = product.strip()
    if not product:
        return ""
    return "%s/%s-mirror" % (org.strip().strip("/"), product)


def plan(text: str, org: str = DEFAULT_ORG) -> list[dict]:
    """Rows that need a mirror attribute, with the line that would be written."""
    changes: list[dict] = []
    masked = mask_comments(text)
    raw_lines = text.splitlines(keepends=True)
    masked_lines = masked.splitlines(keepends=True)
    for number, (raw, seen) in enumerate(zip(raw_lines, masked_lines), 1):
        match = PACKAGE_RE.search(seen)
        if not match:
            continue
        start, end = match.span()
        tag = raw[start:end]
        attrs: dict[str, str] = {}
        positions: dict[str, tuple[int, int]] = {}
        for attr in ATTR_RE.finditer(tag):
            attrs[attr.group(1)] = attr.group(2)
            positions[attr.group(1)] = (attr.start(), attr.end())

        repo = (attrs.get("repo") or "").strip().strip("/")
        if not repo or "/" not in repo:
            continue
        if (attrs.get("type") or "").strip().lower() == "apk":
            continue
        name = attrs.get("name") or ""
        # The app-store placeholder row is not a firmware and has no releases.
        if re.search(r"please[- ]?(?:click|update)", name + " " + repo, re.I):
            continue

        mirror = mirror_for(repo, org)
        if not mirror:
            continue

        # A row that already names a mirror is left exactly as it is; an
        # attribute that is present but empty is filled instead of duplicated.
        existing = [key for key in MIRROR_ATTRS if key in attrs]
        if any(attrs[key].strip() for key in existing):
            continue
        filled_key = existing[0] if existing else ""

        if filled_key:
            empty = re.search(r'\b' + re.escape(filled_key) + r'\s*=\s*""', tag)
            if not empty:
                continue
            old = empty.group(0)
            new = '%s="%s"' % (filled_key, mirror)
            new_tag = tag[:empty.start()] + new + tag[empty.end():]
            new_line = raw[:start] + new_tag + raw[end:]
            changes.append({
                "line": number,
                "name": name,
                "repo": repo,
                "mirror": mirror,
                "action": "filled-empty",
                "before": old,
                "after": new,
                "text": new_line,
            })
            continue

        anchor = positions.get("repo")
        if not anchor:
            continue
        insert_at = start + anchor[1]
        addition = ' portable_zips="%s"' % mirror
        new_line = raw[:insert_at] + addition + raw[insert_at:]
        changes.append({
            "line": number,
            "name": name,
            "repo": repo,
            "mirror": mirror,
            "action": "added",
            "before": "",
            "after": 'portable_zips="%s"' % mirror,
            "text": new_line,
        })
    return changes


def repair(text: str, org: str = DEFAULT_ORG) -> tuple[str, list[dict]]:
    """The manifest text with every bare row naming its mirror."""
    changes = plan(text, org)
    if not changes:
        return text, []
    lines = text.splitlines(keepends=True)
    for change in changes:
        lines[change["line"] - 1] = change["text"]
    return "".join(lines), changes


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Name the portable mirror on every firmware row."
    )
    parser.add_argument("--apply", action="store_true", help="write the attributes")
    parser.add_argument("--check", action="store_true",
                        help="exit 1 when an active row has no mirror")
    parser.add_argument("--org", default=DEFAULT_ORG,
                        help="organisation that owns the mirrors (default: %s)" % DEFAULT_ORG)
    parser.add_argument("--manifest", default=str(MANIFEST),
                        help="manifest to read and edit (default: slidia_manifest.xml)")
    parser.add_argument("--json", default="", help="write the report here")
    args = parser.parse_args()

    path = pathlib.Path(args.manifest)
    if not path.exists():
        raise SystemExit("manifest not found: %s" % path)
    text = path.read_text(encoding="utf-8")
    updated, changes = repair(text, args.org)

    report = {
        "manifest": str(path),
        "org": args.org,
        "changed": bool(changes),
        "count": len(changes),
        "rows": [
            {key: change[key] for key in ("line", "name", "repo", "mirror", "action")}
            for change in changes
        ],
    }
    if args.json:
        pathlib.Path(args.json).write_text(json.dumps(report, indent=2) + "\n",
                                          encoding="utf-8")

    if not changes:
        print("Every active manifest row names a portable mirror.")
        return 0

    for change in changes:
        print("line %-3d %-28s %-36s -> %s (%s)"
              % (change["line"], change["name"][:28] or "(unnamed)",
                 change["repo"], change["mirror"], change["action"]))
    print("%d manifest row(s) need a portable mirror." % len(changes))

    if args.apply:
        path.write_text(updated, encoding="utf-8")
        print("Wrote %s." % path)
        return 0
    if args.check:
        return 1
    print("Run with --apply to write them.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
