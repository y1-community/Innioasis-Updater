#!/usr/bin/env python3
"""
Multi-provider free no-auth translation engine.
Implements the exact fallback cascade from updater-ce-neo / Updater CE 2.5:
  1. Google clients5 (Chrome dictionary endpoint)
  2. Google GTX (Single public translate endpoint)
  3. MyMemory fallback API
"""

import json
import logging
import ssl
import time
import urllib.parse
import urllib.request
from typing import Dict, List, Optional, Sequence

logger = logging.getLogger(__name__)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    ),
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}

def _translate_via_google_clients5(text: str, target_lang: str, timeout: float = 10.0) -> Optional[str]:
    url = (
        "https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl="
        + urllib.parse.quote(target_lang)
    )
    req = urllib.request.Request(
        url,
        data=urllib.parse.urlencode({"q": text}).encode("utf-8"),
        headers=HEADERS,
        method="POST",
    )
    ctx = ssl._create_unverified_context()
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        if resp.status != 200:
            return None
        payload = json.loads(resp.read().decode("utf-8"))
        if isinstance(payload, list) and payload:
            first = payload[0]
            if isinstance(first, list) and first:
                return str(first[0]).strip()
            if isinstance(first, str):
                return first.strip()
    return None

def _translate_via_google_gtx(text: str, target_lang: str, timeout: float = 10.0) -> Optional[str]:
    query = urllib.parse.urlencode(
        {"client": "gtx", "sl": "auto", "tl": target_lang, "dt": "t", "q": text}
    )
    url = f"https://translate.googleapis.com/translate_a/single?{query}"
    req = urllib.request.Request(url, headers={"User-Agent": HEADERS["User-Agent"]})
    ctx = ssl._create_unverified_context()
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        if resp.status != 200:
            return None
        payload = json.loads(resp.read().decode("utf-8"))
        if isinstance(payload, list) and payload and isinstance(payload[0], list):
            parts = [seg[0] for seg in payload[0] if isinstance(seg, list) and seg and seg[0]]
            return "".join(parts).strip()
    return None

def _translate_via_mymemory(text: str, target_lang: str, timeout: float = 10.0) -> Optional[str]:
    query = urllib.parse.urlencode({"q": text, "langpair": f"en|{target_lang}"})
    url = f"https://api.mymemory.translated.net/get?{query}"
    req = urllib.request.Request(url, headers={"User-Agent": HEADERS["User-Agent"]})
    ctx = ssl._create_unverified_context()
    with urllib.request.urlopen(req, timeout=timeout, context=ctx) as resp:
        if resp.status != 200:
            return None
        payload = json.loads(resp.read().decode("utf-8"))
        matches = payload.get("responseData", {}).get("translatedText")
        if matches:
            return matches.strip()
    return None

def translate_single(text: str, target_lang: str) -> Optional[str]:
    if not text.strip():
        return text
    # Chain providers
    for name, fn in [
        ("google_clients5", _translate_via_google_clients5),
        ("google_gtx", _translate_via_google_gtx),
        ("mymemory", _translate_via_mymemory)
    ]:
        try:
            res = fn(text, target_lang)
            if res:
                return res
        except Exception:
            continue
    return None

if __name__ == "__main__":
    import sys
    lang = sys.argv[1] if len(sys.argv) > 1 else "es"
    txt = sys.argv[2] if len(sys.argv) > 2 else "Innioasis Updater CE Release Notes"
    print(f"Translating to {lang}:")
    print(translate_single(txt, lang))
