#!/usr/bin/env python3
from pathlib import Path

css = Path("lumen.css").read_text("utf-8", "ignore")

required = [
    ".lumen-edge-help-link {",
    "display: inline-flex;",
    ".lumen-edge-help-link img {",
    "width: 100%;",
    "@media (min-width: 760px) {",
    ".lumen-edge-help-link img {",
    "width: 64px;",
]

missing = [item for item in required if item not in css]
if missing:
    raise SystemExit("lumen.css is missing: " + ", ".join(missing))

print("OK: lumen.css includes the screenshot-link styles.")
