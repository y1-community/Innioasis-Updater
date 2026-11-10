#!/usr/bin/env python3
"""Queue GA4's traffic_type=internal for Singaporean 1366x1366 clients.

Google Analytics 4 has no resolution rule for internal traffic: the built-in
definition in the property settings matches IP addresses only. A page can
still send the documented ``traffic_type`` event parameter, so this script
queues that value in ``dataLayer`` before the GTM container loads. GA4 then
reports those sessions with ``traffic_type=internal``, and the property's
Internal Traffic data filter can label or exclude them.

"Singaporean" comes from the Asia/Singapore time zone or an -SG browser
locale. 1366x1366 is not a resolution real hardware reports, so the pair is
treated as the preview-scraper bot farm rather than customers.

    python3 scripts/inject_internal_traffic.py
    python3 scripts/inject_internal_traffic.py --root ../InnioasisY1Themes
    python3 scripts/inject_internal_traffic.py --check
"""

from __future__ import annotations

import argparse
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SKIP_DIRS = {".git", "node_modules", "dist", "_site", ".cache", ".coord", ".github", "__pycache__"}

GTM_TAG = re.compile(
    r"""<script\b[^>]*\bsrc=["']https://www\.googletagmanager\.com/(?:gtm\.js|gtag/js)[^"']*["'][^>]*>\s*</script>""",
    re.I,
)
MARKER = "innioasis-internal-traffic"
EXISTING = re.compile(r"<script>\s*\n\s*// " + MARKER + r"[\s\S]*?</script>\n?")

SNIPPET = """<script>
  // innioasis-internal-traffic: label Singaporean 1366x1366 clients as internal.
  (function () {
    try {
      var zone = "";
      try {
        zone = Intl.DateTimeFormat().resolvedOptions().timeZone || "";
      } catch (error) {
        zone = "";
      }
      var languages = navigator.languages || [navigator.language || ""];
      var singapore = String(zone).toLowerCase() === "asia/singapore";
      for (var i = 0; !singapore && i < languages.length; i += 1) {
        singapore = /-sg$/i.test(String(languages[i]));
      }
      var view = window.screen || window;
      if (!singapore || view.width !== 1366 || view.height !== 1366) return;
      window.dataLayer = window.dataLayer || [];
      if (typeof window.gtag === "function") {
        window.gtag("set", { traffic_type: "internal" });
      }
      window.dataLayer.push({ traffic_type: "internal" });
      // The container owns the page_view tag, so the queued value only applies
      // to later events. Stamp the collect request itself so the page_view
      // carries traffic_type too.
      function stamp(url) {
        var text = String(url);
        if (text.indexOf("google-analytics.com") === -1 || text.indexOf("/g/collect") === -1) return url;
        if (/([?&])tt=/.test(text)) return url;
        return text + (text.indexOf("?") === -1 ? "?" : "&") + "tt=internal";
      }
      if (navigator.sendBeacon) {
        var beacon = navigator.sendBeacon.bind(navigator);
        navigator.sendBeacon = function (url, data) { return beacon(stamp(url), data); };
      }
      var open = XMLHttpRequest.prototype.open;
      XMLHttpRequest.prototype.open = function () {
        var args = Array.prototype.slice.call(arguments);
        args[1] = stamp(args[1]);
        return open.apply(this, args);
      };
      var fetchOriginal = window.fetch;
      if (fetchOriginal) {
        window.fetch = function (input) {
          if (typeof input === "string") return fetchOriginal.call(this, stamp(input));
          return fetchOriginal.apply(this, arguments);
        };
      }
    } catch (error) {}
  })();
</script>
"""


def pages(root: str):
    for base, dirs, files in os.walk(root):
        dirs[:] = [name for name in dirs if name not in SKIP_DIRS]
        for name in files:
            if name.startswith("support_toolbar"):
                continue
            if name.lower().endswith((".html", ".htm")):
                yield os.path.join(base, name)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", default=ROOT, help="Repository root to process")
    parser.add_argument("--check", action="store_true", help="Report pages without the current snippet, change nothing")
    args = parser.parse_args()

    root = os.path.abspath(args.root)
    total = inserted = updated = current = missing = 0
    examples = []

    for path in pages(root):
        total += 1
        with open(path, "r", encoding="utf-8", errors="replace") as handle:
            markup = handle.read()
        if MARKER in markup:
            if SNIPPET in markup:
                current += 1
                continue
            if args.check:
                updated += 1
                continue
            updated_markup, count = EXISTING.subn(lambda _match: SNIPPET, markup, count=1)
            if count != 1:
                missing += 1
                if len(examples) < 10:
                    examples.append(os.path.relpath(path, root))
                continue
            with open(path, "w", encoding="utf-8", newline="\n") as handle:
                handle.write(updated_markup)
            updated += 1
            continue
        tag = GTM_TAG.search(markup)
        if not tag:
            missing += 1
            if len(examples) < 10:
                examples.append(os.path.relpath(path, root))
            continue
        if args.check:
            inserted += 1
            continue
        updated_markup = markup[: tag.start()] + SNIPPET + markup[tag.start() :]
        with open(path, "w", encoding="utf-8", newline="\n") as handle:
            handle.write(updated_markup)
        inserted += 1

    print(f"Pages scanned           : {total}")
    print(f"Snippet current         : {current}")
    print(f"Snippet rewritten       : {updated}{' (would rewrite)' if args.check else ''}")
    print(f"Snippet inserted        : {inserted}{' (would insert)' if args.check else ''}")
    print(f"Pages without a GTM tag : {missing}")
    for example in examples:
        print(f"  unhandled: {example}")

    if args.check and (updated or inserted or missing):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
