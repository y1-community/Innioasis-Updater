#!/usr/bin/env python3
"""Confirm the Edge helper modal gives the requested Keep instructions and
matches the Microsoft Edge flow described in the live web sources we read."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
GUIDE = "guide.html"
GUIDE_FIRMWARE = "firmware-guide.html"

MODAL_BLOCK = '<div id="edge-keep-modal" class="edge-keep-modal" hidden aria-hidden="true" role="dialog"'


def modal_html(page: str) -> str:
    body = Path(page).read_text("utf-8", "ignore")
    start = body.find(MODAL_BLOCK)
    if start == -1:
        return ""
    end = body.find("</div>", start)
    if end == -1:
        return body[start:]
    return body[start : end + 6]


def main() -> None:
    required = {
        "more options button": "More options button (…)",
        "select Keep": "Keep",
        "show more": "Show more",
        "down arrow next to Delete": "▼",
        "Windows 11 / 10 download panel": "Ctrl + J",
    }

    for page in (GUIDE, GUIDE_FIRMWARE):
        html = modal_html(page)
        if not html:
            raise SystemExit(f"{page} should contain the Edge keep modal block")
        for key, needle in required.items():
            if needle not in html:
                raise SystemExit(
                    f"{page} modal is missing the required instruction: {key!r}"
                )

    guide_html = modal_html(GUIDE)
    assert "More options button (…)" in guide_html
    assert "Keep" in guide_html
    assert "Show more" in guide_html
    assert "▼" in guide_html
    assert "Delete" in guide_html
    assert "Ctrl + J" in guide_html

    msg = (
        "OK: Edge modal instructs Windows 11 / 10 users to open the download panel, "
        "use the more options (...) button, select Keep, and if a second prompt appears, "
        "choose Show more, press the down arrow next to Delete, then Keep."
    )
    Path("_edge_instructions_stdout.txt").write_text(msg, "utf-8")
    print(msg)


if __name__ == "__main__":
    main()
