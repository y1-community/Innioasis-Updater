#!/usr/bin/env python3
"""Responsive audit harness for the Innioasis sites.

Drives the locally installed chrome-headless-shell over the DevTools protocol,
loads each page at a list of device viewports, and measures the things that
break on unusual screens (square handhelds, foldables, TV-sized monitors):

  * horizontal overflow           document wider than the viewport
  * dock height share             the bottom toolbar eating the viewport
  * donation goal line visible    it should stand down on cramped screens
  * content occlusion             footer copy hidden behind the dock
  * tap targets                   interactive dock items under 40 CSS px
  * cumulative layout shift       recorded from navigation start

Usage:
    python3 tools/responsive/audit.py --base https://innioasis.app --out .responsive/live
    python3 tools/responsive/audit.py --base http://localhost:8099 --out .responsive/local

The report is written as report.json plus report.md, with one screenshot per
device in shots/. Exit status is 1 when a page/device pair has a defect, so CI
can gate on it.
"""

from __future__ import annotations

import argparse
import base64
import json
import os
import shutil
import socket
import subprocess
import sys
import tempfile
import time
import urllib.request
from pathlib import Path

try:
    import websocket  # websocket-client
except ImportError:  # pragma: no cover - environment guard
    sys.exit("websocket-client is required: python3 -m pip install websocket-client")

CHROME_CANDIDATES = [
    os.path.expanduser(
        "~/Library/Caches/ms-playwright/chromium_headless_shell-1223/"
        "chrome-headless-shell-mac-arm64/chrome-headless-shell"
    ),
    "/usr/bin/google-chrome",
    "/usr/bin/chromium",
]

# width/height are CSS pixels at devicePixelRatio 1 unless dpr is set.
DEVICES = [
    {"name": "ikkomind-one", "label": "IkkoMind One", "width": 480, "height": 854, "mobile": True},
    {"name": "unihertz-pocket", "label": "Unihertz Pocket", "width": 480, "height": 854, "mobile": True},
    {"name": "unihertz-titan-2", "label": "Unihertz Titan 2", "width": 720, "height": 720, "mobile": True},
    {"name": "unihertz-elite", "label": "Unihertz Elite", "width": 480, "height": 480, "mobile": True},
    {"name": "unihertz-elite-pro", "label": "Unihertz Elite Pro", "width": 480, "height": 480, "mobile": True},
    {"name": "blackberry-passport", "label": "BlackBerry Passport", "width": 600, "height": 600, "mobile": True},
    {"name": "zflip-5", "label": "Galaxy Z Flip 5", "width": 412, "height": 850, "mobile": True},
    {"name": "zflip-6", "label": "Galaxy Z Flip 6", "width": 412, "height": 872, "mobile": True},
    {"name": "zfold-5-cover", "label": "Galaxy Z Fold 5 (cover)", "width": 344, "height": 882, "mobile": True},
    {"name": "zfold-5-inner", "label": "Galaxy Z Fold 5 (inner)", "width": 673, "height": 841, "mobile": True},
    {"name": "iphone-se", "label": "iPhone SE", "width": 375, "height": 667, "mobile": True},
    {"name": "iphone-16", "label": "iPhone 16", "width": 393, "height": 852, "mobile": True},
    {"name": "iphone-16-pro-max", "label": "iPhone 16 Pro Max", "width": 440, "height": 956, "mobile": True},
    {"name": "iphone-fold", "label": "iPhone foldable (Duo)", "width": 420, "height": 900, "mobile": True},
    {"name": "ipad-mini", "label": "iPad mini", "width": 744, "height": 1133, "mobile": True},
    {"name": "macbook-air-13", "label": "MacBook Air 13", "width": 1440, "height": 900},
    {"name": "macbook-pro-16", "label": "MacBook Pro 16", "width": 1728, "height": 1117},
    {"name": "fridge-portrait", "label": "Smart fridge (portrait)", "width": 800, "height": 1280, "mobile": True},
    {"name": "monitor-32-1440p", "label": '32" 1440p', "width": 2560, "height": 1440},
    {"name": "monitor-4k", "label": '32" 4K', "width": 3840, "height": 2160},
    {"name": "square-1440", "label": "Square 1440 (Passport-equivalent)", "width": 1440, "height": 1440},
    {"name": "iphone-safari-mini", "label": "iPhone Safari (320 window)", "width": 320, "height": 568, "mobile": True},
    {"name": "ipad-mini-landscape", "label": "iPad mini (landscape)", "width": 1133, "height": 744, "mobile": True},
    {"name": "monitor-ultrawide", "label": '34" ultrawide', "width": 3440, "height": 1440},
]

# Each entry may pin its own origin; the sites live on different hostnames.
PAGES = [
    {"name": "themes", "path": "/", "origin": "https://themes.innioasis.app", "goal": "gallery"},
    {"name": "firmware", "path": "/firmware.html", "origin": "https://innioasis.app", "goal": "archive"},
    {"name": "updater", "path": "/", "origin": "https://innioasis.app", "goal": "updater"},
]

# Installed before any page script so layout shifts are counted from the start.
CLS_SNIPPET = """
(() => {
  window.__auditCls = 0;
  window.__auditShifts = [];
  try {
    new PerformanceObserver((list) => {
      for (const entry of list.getEntries()) {
        if (!entry.hadRecentInput) {
          window.__auditCls += entry.value;
        window.__auditLastSources = (entry.sources || []).length;
          const nodes = (entry.sources || []).map((source) => {
            const el = source.node;
            if (!el || !el.tagName) return null;
            return el.tagName.toLowerCase() + (el.className && typeof el.className === 'string' ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.') : '');
          }).filter(Boolean);
          window.__auditShifts.push({value: Math.round(entry.value * 10000) / 10000, t: Math.round(entry.startTime), nodes: nodes.slice(0, 3), sources: (entry.sources || []).length});
        }
      }
    }).observe({type: 'layout-shift', buffered: true});
  } catch (error) {}
})();
"""

PROBE = r"""
(() => {
  const vw = window.innerWidth, vh = window.innerHeight;
  const doc = document.documentElement;
  const dock = document.querySelector('.y1-site-dock-wrap') || document.querySelector('#support-toolbar-container');
  const bar = document.querySelector('.y1-site-dock-bar') || dock;
  const dockHidden = !dock || getComputedStyle(dock).display === 'none' ||
    getComputedStyle(dock).visibility === 'hidden' || dock.getBoundingClientRect().height < 4;
  const dRect = dockHidden ? null : dock.getBoundingClientRect();
  const goal = document.querySelector('#y1-dock-secondary-line');
  const goalVisible = !!(goal && goal.getBoundingClientRect().height > 0 &&
    getComputedStyle(goal).display !== 'none' && !goal.hidden);

  const dockLinks = [...document.querySelectorAll(
    '#support-toolbar-container a, #support-toolbar-container button, #support-toolbar-container [role="button"]'
  )].filter((el) => {
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.height > 0;
  });
  const smallList = dockLinks.filter((el) => {
    const r = el.getBoundingClientRect();
    return r.height < 40 || r.width < 32;
  }).map((el) => {
    const r = el.getBoundingClientRect();
    return (el.tagName.toLowerCase() + '.' + String(el.className || '').trim().split(/\s+/).slice(0, 2).join('.')) +
      ' ' + Math.round(r.width) + 'x' + Math.round(r.height);
  }).slice(0, 4);
  const smallTargets = smallList.length;

  const footer = document.querySelector('#footer-root footer, footer.site-footer');
  let footerClip = null;
  if (footer && dRect) {
    const r = footer.getBoundingClientRect();
    footerClip = Math.round(Math.max(0, r.bottom - dRect.top));
  }

  const wide = [...document.querySelectorAll('body *')].filter((el) => {
    const r = el.getBoundingClientRect();
    return r.width > 0 && r.right > vw + 1 && getComputedStyle(el).position !== 'fixed';
  }).slice(0, 5).map((el) => ({
    tag: el.tagName.toLowerCase(),
    cls: typeof el.className === 'string' ? el.className.slice(0, 60) : '',
    right: Math.round(el.getBoundingClientRect().right)
  }));

  return {
    url: location.href,
    vw, vh,
    scrollWidth: Math.max(doc.scrollWidth, document.body ? document.body.scrollWidth : 0),
    overflowX: Math.max(doc.scrollWidth, document.body ? document.body.scrollWidth : 0) - vw,
    dockHeight: dRect ? Math.round(dRect.height) : 0,
    dockShare: dRect ? Math.round((dRect.height / vh) * 1000) / 1000 : 0,
    dockHidden,
    goalLineVisible: goalVisible,
    goalWeight: goal && goal.getBoundingClientRect().height > 0
      ? Math.round((goal.getBoundingClientRect().height / vh) * 1000) / 1000 : 0,
    footerClip,
    smallTargets,
    smallTargetList: smallList,
    density: (document.getElementById('support-toolbar-container') || {}).getAttribute
      ? document.getElementById('support-toolbar-container').getAttribute('data-dock-density') : null,
    controls: Object.fromEntries([
      ['donate', '[data-donate-open]'],
      ['privacy', '[data-privacy-open]'],
      ['language', '[data-locale-open]'],
      ['fontDown', '[data-font-down]'],
      ['fontUp', '[data-font-up]']
    ].map(([key, sel]) => {
      const el = document.querySelector(sel);
      if (!el) return [key, null];
      const r = el.getBoundingClientRect();
      return [key, r.width > 0 && r.height > 0];
    })),
    wideElements: wide,
    cls: Math.round((window.__auditCls || 0) * 10000) / 10000,
    landmarks: {
      header: !!document.querySelector('header, .lumen-header, #navShell'),
      main: !!document.querySelector('main, [role="main"]'),
      footer: !!footer
    },
    metaViewport: (document.querySelector('meta[name="viewport"]') || {}).content || null,
    docHeight: Math.round(Math.max(doc.scrollHeight, document.body ? document.body.scrollHeight : 0))
  };
})()
"""


def find_chrome() -> str:
    for path in CHROME_CANDIDATES:
        if os.path.exists(path):
            return path
    raise SystemExit("No Chrome/Chromium binary found")


def free_port() -> int:
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        return sock.getsockname()[1]


class CDP:
    def __init__(self, ws_url: str):
        self.ws = websocket.create_connection(ws_url, timeout=45)
        self.next_id = 0

    def send(self, method: str, **params):
        self.next_id += 1
        self.ws.send(json.dumps({"id": self.next_id, "method": method, "params": params}))
        while True:
            message = json.loads(self.ws.recv())
            if message.get("id") == self.next_id:
                if "error" in message:
                    raise RuntimeError(f"{method}: {message['error']}")
                return message.get("result", {})

    def close(self):
        self.ws.close()


def wait_for_json(url: str, timeout: float = 20.0):
    deadline = time.time() + timeout
    while time.time() < deadline:
        try:
            with urllib.request.urlopen(url, timeout=2) as response:
                return json.load(response)
        except Exception:
            time.sleep(0.2)
    raise RuntimeError(f"Chrome endpoint never answered: {url}")


def audit_page(cdp: CDP, url: str, device: dict, shot_path: Path | None) -> dict:
    cdp.send("Emulation.setDeviceMetricsOverride",
             width=device["width"], height=device["height"],
             deviceScaleFactor=device.get("dpr", 1), mobile=bool(device.get("mobile")))
    cdp.send("Emulation.setTouchEmulationEnabled", enabled=bool(device.get("mobile")), maxTouchPoints=5)
    if not getattr(cdp, "_cls_installed", False):
        cdp.send("Page.addScriptToEvaluateOnNewDocument", source=CLS_SNIPPET)
        cdp._cls_installed = True
    cdp.send("Page.navigate", url=url)
    # Wait for the load event, then give the dock injection and fonts a moment.
    deadline = time.time() + 25
    while time.time() < deadline:
        state = cdp.send("Runtime.evaluate", expression="document.readyState", returnByValue=True)
        if state.get("result", {}).get("value") == "complete":
            break
        time.sleep(0.2)
    time.sleep(1.6)
    if shot_path is not None:
        try:
            shot = cdp.send("Page.captureScreenshot", format="jpeg", quality=55, captureBeyondViewport=False)
            shot_path.write_bytes(base64.b64decode(shot["data"]))
        except Exception as error:  # screenshots are diagnostics, not the verdict
            shot_error = str(error)
    result = cdp.send("Runtime.evaluate", expression=PROBE, returnByValue=True, awaitPromise=True)
    data = result.get("result", {}).get("value") or {}
    data["clsTop"] = data.get("cls")
    # Scroll to the very end for the occlusion check. Smooth scrolling would
    # still be in flight, so force instant jumps and confirm the position.
    cdp.send("Runtime.evaluate", expression=(
        "document.documentElement.style.scrollBehavior='auto';"
        "document.body.style.scrollBehavior='auto';"
        "window.scrollTo(0, document.documentElement.scrollHeight);"), returnByValue=True)
    # The gallery streams cards while scrolling, so "are we at the bottom" is
    # not a stable question. What matters structurally is whether the space the
    # page reserves below its content covers the dock's footprint. If it does,
    # no footer can ever sit under the bar.
    occlusion = cdp.send("Runtime.evaluate", returnByValue=True, expression=r"""(() => {
      const footer = document.querySelector('#footer-root footer, footer.site-footer');
      const dock = document.querySelector('.y1-site-dock-wrap') || document.querySelector('#support-toolbar-container');
      if (!footer || !dock) return 0;
      const bar = dock.querySelector ? (dock.querySelector('.y1-site-dock-wrap') || dock) : dock;
      const r = bar.getBoundingClientRect();
      if (r.height < 4 || getComputedStyle(bar).display === 'none') return 0;
      const footprint = Math.round(innerHeight - r.top);
      const reserved = parseFloat(getComputedStyle(document.body).paddingBottom) || 0;
      return Math.max(0, footprint - Math.round(reserved));
    })()""")
    data["footerClip"] = occlusion.get("result", {}).get("value") or 0
    data["device"] = device["name"]
    data["deviceLabel"] = device["label"]
    if shot_path is not None:
        data["screenshot"] = str(shot_path)
    return data


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base", default="", help="Origin override, e.g. http://localhost:8099 (default: each page's live origin)")
    parser.add_argument("--out", default=".responsive/out")
    parser.add_argument("--pages", default="", help="Comma separated page names to limit the run")
    parser.add_argument("--devices", default="", help="Comma separated device names to limit the run")
    parser.add_argument("--no-shots", action="store_true")
    args = parser.parse_args()

    out_dir = Path(args.out)
    shots_dir = out_dir / "shots"
    shots_dir.mkdir(parents=True, exist_ok=True)

    pages = [p for p in PAGES if not args.pages or p["name"] in args.pages.split(",")]
    devices = [d for d in DEVICES if not args.devices or d["name"] in args.devices.split(",")]

    chrome = find_chrome()
    port = free_port()
    profile = tempfile.mkdtemp(prefix="responsive-audit-")
    process = subprocess.Popen(
        [chrome, f"--remote-debugging-port={port}", f"--user-data-dir={profile}",
         "--headless=new", "--hide-scrollbars", "--no-first-run", "--no-default-browser-check",
         "--remote-allow-origins=*",
         "--disable-gpu", "--force-color-profile=srgb", "about:blank"],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    results = []
    defects = []
    try:
        wait_for_json(f"http://127.0.0.1:{port}/json/version")
        target = wait_for_json(f"http://127.0.0.1:{port}/json/list")[0]
        cdp = CDP(target["webSocketDebuggerUrl"])
        cdp.send("Page.enable")
        cdp.send("Runtime.enable")
        for page in pages:
            # --base overrides every origin, which is how a local server run works.
            origin = args.base.rstrip("/") if args.base else page["origin"].rstrip("/")
            url = origin + page["path"]
            for device in devices:
                shot = None if args.no_shots else shots_dir / f"{page['name']}--{device['name']}.jpg"
                try:
                    row = audit_page(cdp, url, device, shot)
                except Exception as error:
                    row = {"device": device["name"], "deviceLabel": device["label"],
                           "url": url, "error": str(error)}
                row["page"] = page["name"]
                results.append(row)
                if "error" in row:
                    defects.append(f"{page['name']}/{device['name']}: probe failed: {row['error']}")
                    continue
                checks = []
                if row["overflowX"] > 1:
                    checks.append(f"horizontal overflow +{row['overflowX']}px")
                if row["dockShare"] > 0.22:
                    checks.append(f"dock takes {row['dockShare'] * 100:.0f}% of the viewport")
                if row["footerClip"] and row["footerClip"] > 2:
                    checks.append(f"footer hidden behind the dock by {row['footerClip']}px")
                if row["smallTargets"] > 0:
                    checks.append(f"{row['smallTargets']} dock targets under 40px")
                for control in ("donate", "privacy", "language"):
                    if row.get("controls", {}).get(control) is False:
                        checks.append(f"{control} control not reachable")
                expected_goal = row.get("density") == "full"
                if expected_goal and not row.get("goalLineVisible"):
                    checks.append(f"goal line missing on the {row.get('density')} tier")
                if not expected_goal and row.get("goalLineVisible"):
                    checks.append(f"goal line still shown on the {row.get('density')} tier")
                if row["cls"] > 0.05:
                    checks.append(f"CLS {row['cls']}")
                if checks:
                    defects.append(f"{page['name']}/{device['name']} ({device['width']}x{device['height']}): " + "; ".join(checks))
                print(f"{page['name']:9} {device['name']:20} {device['width']}x{device['height']:<5} "
                      f"overflow={row['overflowX']:>3} dock={row['dockHeight']:>3}px "
                      f"({row['dockShare'] * 100:>2.0f}%) goal={'on ' if row['goalLineVisible'] else 'off'} "
                      f"cls={row['cls']}", flush=True)
        cdp.close()
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()
        shutil.rmtree(profile, ignore_errors=True)

    (out_dir / "report.json").write_text(json.dumps({"base": args.base, "results": results}, indent=1))
    lines = [f"# Responsive audit: {args.base}", ""]
    lines.append(f"{len(results)} page/device combinations, {len(defects)} findings.")
    lines.append("")
    if defects:
        lines += ["## Findings", ""] + [f"- {item}" for item in defects] + [""]
    lines += ["## Matrix", "",
              "| page | device | viewport | overflow | dock | goal line | CLS |",
              "| --- | --- | --- | --- | --- | --- | --- |"]
    for row in results:
        if "error" in row:
            continue
        lines.append(
            f"| {row['page']} | {row['deviceLabel']} | {row['vw']}x{row['vh']} | {row['overflowX']}px | "
            f"{row['dockHeight']}px ({row['dockShare'] * 100:.0f}%) | "
            f"{'shown' if row['goalLineVisible'] else 'hidden'} | {row['cls']} |"
        )
    (out_dir / "report.md").write_text("\n".join(lines) + "\n")
    print(f"\n{len(defects)} findings -> {out_dir / 'report.md'}")
    return 1 if defects else 0


if __name__ == "__main__":
    raise SystemExit(main())
