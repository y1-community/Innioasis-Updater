#!/usr/bin/env python3
from __future__ import annotations

from pathlib import Path

GUIDE = "guide.html"
GUIDE_FIRMWARE = "firmware-guide.html"

OLD_MODAL_ID = 'id="edge-keep-modal"'
OLD_HINT_TEXT = 'Need the file after Edge blocked it?'

results: dict[str, list[str]] = {
    "old_modal_removed": [],
    "old_hint_removed": [],
    "new_modal_present": [],
    "new_screenshot_link_present": [],
}


def check(page: str, body: str) -> None:
    if OLD_MODAL_ID in body:
        results["old_modal_removed"].append(page)
    if OLD_HINT_TEXT in body:
        results["old_hint_removed"].append(page)
    if 'id="edge-keep-screenshot-modal"' not in body:
        results["new_modal_present"].append(page)
    if 'class="lumen-edge-help-link"' not in body:
        results["new_screenshot_link_present"].append(page)


for page in (GUIDE, GUIDE_FIRMWARE):
    check(page, Path(page).read_text("utf-8", "ignore"))

failed = False
for key, pages in results.items():
    if pages:
        failed = True
        print(f"FAIL {key}: {', '.join(pages)}")
if not failed:
    print("OK: old Edge modal replaced with screenshot-based modal in both guide pages.")
