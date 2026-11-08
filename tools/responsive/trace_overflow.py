#!/usr/bin/env python3
"""Trace why an element is wider than the viewport.

Prints the element's inline style, its computed box, the ancestor chain with
widths, and every matched CSS rule that declares a sizing or layout property,
including the stylesheet it came from. This is the tool that answers "which
rule actually wins", rather than guessing at an override.

    python3 tools/responsive/trace_overflow.py \
        --url http://127.0.0.1:8099/ --width 393 --height 852 \
        --selector ".gallery-social-links"
"""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import audit  # noqa: E402  (sibling module, shared CDP client)


TRACE = r"""
((selector) => {
  const el = document.querySelector(selector);
  if (!el) return {error: 'selector not found: ' + selector};
  const out = {selector, matches: document.querySelectorAll(selector).length};
  out.inlineStyle = el.getAttribute('style') || '';
  const cs = getComputedStyle(el);
  const props = ['display', 'position', 'width', 'minWidth', 'maxWidth', 'flex', 'flexWrap',
                 'boxSizing', 'left', 'right', 'top', 'bottom', 'transform', 'overflowX',
                 'gridColumn', 'justifySelf', 'whiteSpace'];
  out.computed = {};
  props.forEach((p) => { out.computed[p] = cs[p]; });
  const r = el.getBoundingClientRect();
  out.rect = {left: Math.round(r.left), right: Math.round(r.right), width: Math.round(r.width)};
  out.viewport = {width: innerWidth, height: innerHeight};
  out.chain = [];
  let node = el;
  while (node && node !== document.documentElement) {
    const nr = node.getBoundingClientRect();
    const ncs = getComputedStyle(node);
    out.chain.push({
      node: node.tagName.toLowerCase() + (typeof node.className === 'string' && node.className ? '.' + node.className.trim().split(/\s+/).slice(0, 2).join('.') : ''),
      width: Math.round(nr.width),
      right: Math.round(nr.right),
      display: ncs.display,
      position: ncs.position,
      overflowX: ncs.overflowX
    });
    node = node.parentElement;
  }
  out.children = [...el.children].slice(0, 8).map((c) => {
    const cr = c.getBoundingClientRect();
    const ccs = getComputedStyle(c);
    return {
      node: c.tagName.toLowerCase() + (typeof c.className === 'string' && c.className ? '.' + c.className.trim().split(/\s+/).slice(0, 2).join('.') : ''),
      width: Math.round(cr.width),
      flex: ccs.flex,
      marginLeft: ccs.marginLeft
    };
  });
  return out;
})
"""

SIZING_PROPS = {
    "width", "min-width", "max-width", "height", "min-height", "flex", "flex-basis",
    "flex-wrap", "display", "position", "left", "right", "inset", "grid-template-columns",
    "grid-column", "justify-self", "padding", "padding-left", "padding-right",
    "margin", "margin-left", "overflow", "overflow-x", "white-space", "transform",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", required=True)
    parser.add_argument("--selector", required=True)
    parser.add_argument("--width", type=int, default=393)
    parser.add_argument("--height", type=int, default=852)
    parser.add_argument("--mobile", action="store_true", default=True)
    parser.add_argument("--wait", type=float, default=3.0)
    args = parser.parse_args()

    chrome = audit.find_chrome()
    port = audit.free_port()
    profile = tempfile.mkdtemp(prefix="trace-overflow-")
    process = subprocess.Popen(
        [chrome, f"--remote-debugging-port={port}", f"--user-data-dir={profile}",
         "--headless=new", "--hide-scrollbars", "--no-first-run", "--remote-allow-origins=*",
         "--disable-gpu", "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    try:
        audit.wait_for_json(f"http://127.0.0.1:{port}/json/version")
        target = audit.wait_for_json(f"http://127.0.0.1:{port}/json/list")[0]
        cdp = audit.CDP(target["webSocketDebuggerUrl"])
        cdp.send("Page.enable")
        cdp.send("Runtime.enable")
        cdp.send("DOM.enable")
        cdp.send("CSS.enable")
        cdp.send("Emulation.setDeviceMetricsOverride", width=args.width, height=args.height,
                 deviceScaleFactor=1, mobile=bool(args.mobile))
        cdp.send("Page.navigate", url=args.url)
        time.sleep(args.wait)

        result = cdp.send("Runtime.evaluate",
                          expression=f"({TRACE})({json.dumps(args.selector)})",
                          returnByValue=True)
        data = result.get("result", {}).get("value") or {}
        print(json.dumps(data, indent=1))

        document = cdp.send("DOM.getDocument", depth=-1)
        node = cdp.send("DOM.querySelector", nodeId=document["root"]["nodeId"], selector=args.selector)
        node_id = node.get("nodeId")
        if node_id:
            matched = cdp.send("CSS.getMatchedStylesForNode", nodeId=node_id)
            print("\n--- matched rules that size or position the element ---")
            for entry in matched.get("matchedCSSRules", []):
                rule = entry.get("rule", {})
                declarations = [
                    f"{p['name']}: {p['value']}"
                    for p in rule.get("style", {}).get("cssProperties", [])
                    if p.get("name") in SIZING_PROPS and p.get("value") and not p.get("parsedOk") is False
                ]
                if not declarations:
                    continue
                print(f"\n[{entry.get('matchingSelectors')}] {rule.get('selectorList', {}).get('text')}")
                print(f"  origin: {rule.get('origin')}  sheet: {rule.get('styleSheetId')}  "
                      f"media: {[m.get('text') for m in entry.get('rule', {}).get('media', [])]}")
                for declaration in declarations:
                    print("   ", declaration)
            inline = matched.get("inlineStyle", {}).get("cssProperties", [])
            if inline:
                print("\n--- inline style ---")
                for declaration in inline:
                    print("   ", f"{declaration.get('name')}: {declaration.get('value')}")
        else:
            print("DOM.querySelector found no node for", args.selector)
        cdp.close()
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
        shutil.rmtree(profile, ignore_errors=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
