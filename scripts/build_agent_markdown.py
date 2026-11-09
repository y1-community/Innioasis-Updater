#!/usr/bin/env python3
"""Write a Markdown twin of every HTML page for agents and retrieval.

The HTML stays the page people and search engines open. These files are the
same words in a form an agent can read, in every language the site already
publishes. Each file ends with where to support the projects and where to
ask for help.

    python3 scripts/build_agent_markdown.py
    python3 scripts/build_agent_markdown.py --origin https://themes.innioasis.app
"""

from __future__ import annotations

import argparse
import os
import re
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", "node_modules", "dist", "agent-markdown", "__pycache__", ".cache"}
SKIP_FILES = {"analytics-handoff.html"}

SUPPORT = """
## Community support

This page is part of the Innioasis Community Projects.

Support the development at https://www.ko-fi.com/teamslide

Help from the developers of the community projects and the stock firmware for the players is at https://ko-fi.com/teamslide and on the Innioasis Community Discord: https://discord.gg/zHrT2zrcek
""".strip()

LANG_RE = re.compile(r"_([a-z]{2,3}(?:-[a-zA-Z0-9]{2,4})?)\.html$", re.I)


class MarkdownBody(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip = 0
        self.href: list[str | None] = []
        self.list_depth = 0
        self.in_cell = False
        self.cell: list[str] = []
        self.row: list[str] = []
        self.rows: list[list[str]] = []
        self.in_table = False

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript", "svg", "iframe"}:
            self.skip += 1
            return
        if self.skip:
            return
        if tag in {"h1", "h2", "h3", "h4"}:
            self.parts.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag == "p":
            self.parts.append("\n\n")
        elif tag == "br":
            self.parts.append("\n")
        elif tag == "li":
            self.parts.append("\n" + "  " * self.list_depth + "- ")
        elif tag in {"ul", "ol"}:
            self.list_depth += 1
        elif tag == "a":
            href = dict(attrs).get("href")
            self.href.append(href)
            self.parts.append("[")
        elif tag == "code":
            self.parts.append("`")
        elif tag == "table":
            self.in_table = True
            self.rows = []
        elif tag == "tr" and self.in_table:
            self.row = []
        elif tag in {"td", "th"} and self.in_table:
            self.in_cell = True
            self.cell = []
        elif tag == "img":
            alt = dict(attrs).get("alt") or ""
            if alt:
                self.parts.append(alt)

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript", "svg", "iframe"}:
            if self.skip:
                self.skip -= 1
            return
        if self.skip:
            return
        if tag in {"ul", "ol"} and self.list_depth:
            self.list_depth -= 1
            self.parts.append("\n")
        elif tag == "a" and self.href:
            href = self.href.pop()
            self.parts.append("](" + (href or "") + ")")
        elif tag == "code":
            self.parts.append("`")
        elif tag in {"td", "th"} and self.in_cell:
            self.row.append(re.sub(r"\s+", " ", "".join(self.cell)).strip())
            self.in_cell = False
        elif tag == "tr" and self.in_table:
            if any(self.row):
                self.rows.append(self.row)
        elif tag == "table" and self.in_table:
            self.parts.append("\n\n" + render_table(self.rows) + "\n")
            self.in_table = False

    def handle_data(self, data: str) -> None:
        if self.skip:
            return
        text = re.sub(r"\s+", " ", data)
        if not text.strip():
            return
        if self.in_cell:
            self.cell.append(text)
            return
        self.parts.append(text)


def render_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    width = max(len(row) for row in rows)
    padded = [row + [""] * (width - len(row)) for row in rows]
    lines = ["| " + " | ".join(cell.replace("|", "\\|") for cell in padded[0]) + " |"]
    lines.append("| " + " | ".join("---" for _ in range(width)) + " |")
    for row in padded[1:]:
        lines.append("| " + " | ".join(cell.replace("|", "\\|") for cell in row) + " |")
    return "\n".join(lines)


def meta(html: str, name: str) -> str:
    patterns = (
        rf'<meta[^>]*?(?:name|property)="{re.escape(name)}"[^>]*?content="([^"]*)"',
        rf'<meta[^>]*?content="([^"]*)"[^>]*?(?:name|property)="{re.escape(name)}"',
    )
    for pattern in patterns:
        match = re.search(pattern, html, re.I)
        if match:
            return re.sub(r"\s+", " ", match.group(1)).strip()
    return ""


def title_of(html: str) -> str:
    match = re.search(r"<title>(.*?)</title>", html, re.I | re.S)
    return re.sub(r"\s+", " ", match.group(1)).strip() if match else ""


def language_of(path: Path, html: str) -> str:
    named = LANG_RE.search(path.name)
    if named:
        return named.group(1)
    match = re.search(r'<html[^>]+lang=["\']([^"\']+)', html, re.I)
    return match.group(1) if match else "en"


def main_html(html: str) -> str:
    match = re.search(r"<main\b[^>]*>(.*)</main>", html, re.I | re.S)
    if match:
        return match.group(1)
    match = re.search(r"<body\b[^>]*>(.*)</body>", html, re.I | re.S)
    return match.group(1) if match else html


def to_markdown(html: str) -> str:
    parser = MarkdownBody()
    parser.feed(main_html(html))
    text = "".join(parser.parts)
    text = text.replace("]()", "")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def convert_tree(origin: str, out_dir: Path) -> int:
    written = 0
    index: list[str] = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [name for name in dirnames if name not in SKIP_DIRS]
        for filename in filenames:
            if not filename.lower().endswith(".html") or filename in SKIP_FILES:
                continue
            source = Path(dirpath) / filename
            html = source.read_text(encoding="utf-8", errors="replace")
            relative = source.relative_to(ROOT).with_suffix(".md")
            language = language_of(source, html)
            page_title = title_of(html) or source.stem
            description = meta(html, "description")
            url = origin.rstrip("/") + "/" + source.relative_to(ROOT).as_posix()
            body = to_markdown(html)
            def yaml(value: str) -> str:
                return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'

            document = (
                "---\n"
                f"title: {yaml(page_title)}\n"
                f"description: {yaml(description)}\n"
                f"language: {yaml(language)}\n"
                f"source: {yaml(url)}\n"
                "---\n\n"
                f"# {page_title}\n\n"
                f"{body}\n\n"
                f"{SUPPORT}\n"
            )
            target = out_dir / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(document, encoding="utf-8")
            index.append(f"- [{page_title}]({relative.as_posix()}) ({language})")
            written += 1
    index_body = (
        "# Agent Markdown\n\n"
        "One Markdown file for every HTML page on this site, in each published language. "
        "Open the HTML for the page people see. Read these when you need the words.\n\n"
        + SUPPORT
        + "\n\n"
        + "\n".join(sorted(index))
        + "\n"
    )
    (out_dir / "README.md").write_text(index_body, encoding="utf-8")
    return written


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--origin", default="https://innioasis.app")
    parser.add_argument("--out", default="agent-markdown")
    args = parser.parse_args()
    count = convert_tree(args.origin, ROOT / args.out)
    print(f"wrote {count} markdown pages to {args.out}")


if __name__ == "__main__":
    main()
