#!/usr/bin/env python3
"""Manage advertising configuration, ads.txt, and Raptive readiness for Innioasis.app.

Usage:
    python3 scripts/manage_ads.py --status
    python3 scripts/manage_ads.py --enable-raptive <SITE_ID>
    python3 scripts/manage_ads.py --disable-raptive
    python3 scripts/manage_ads.py --append-ads-txt <SELLER_LINE>
    python3 scripts/manage_ads.py --validate-ads-txt
"""

from __future__ import annotations

import argparse
import os
import re
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
AD_MANAGER_PATH = os.path.join(ROOT, "ad-manager.js")
ADS_TXT_PATH = os.path.join(ROOT, "ads.txt")
SITE_INIT_PATH = os.path.join(ROOT, "site-init.js")
LUMEN_CSS_PATH = os.path.join(ROOT, "lumen.css")


def read_file(path: str) -> str:
    if not os.path.exists(path):
        return ""
    with open(path, "r", encoding="utf-8", errors="replace") as f:
        return f.read()


def write_file(path: str, content: str) -> None:
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)


def get_status() -> dict:
    manager_code = read_file(AD_MANAGER_PATH)
    ads_txt = read_file(ADS_TXT_PATH)
    lumen_css = read_file(LUMEN_CSS_PATH)

    raptive_id_match = re.search(r'raptiveSiteId:\s*["\']([^"\']*)["\']', manager_code)
    provider_match = re.search(r'provider:\s*["\']([^"\']*)["\']', manager_code)
    enabled_match = re.search(r'enabled:\s*(true|false)', manager_code)

    raptive_id = raptive_id_match.group(1) if raptive_id_match else ""
    provider = provider_match.group(1) if provider_match else "house"
    enabled = enabled_match.group(1) == "true" if enabled_match else False

    cls_safe = ".raptive-ad-container" in lumen_css and "min-height" in lumen_css
    ads_txt_exists = os.path.exists(ADS_TXT_PATH)
    ads_txt_lines = [line.strip() for line in ads_txt.splitlines() if line.strip() and not line.strip().startswith("#")]

    return {
        "enabled": enabled,
        "provider": provider,
        "raptive_site_id": raptive_id,
        "cls_safe": cls_safe,
        "ads_txt_exists": ads_txt_exists,
        "ads_txt_seller_records": len(ads_txt_lines),
    }


def enable_raptive(site_id: str) -> bool:
    if not os.path.exists(AD_MANAGER_PATH):
        print(f"Error: {AD_MANAGER_PATH} not found.")
        return False

    code = read_file(AD_MANAGER_PATH)
    code = re.sub(r'raptiveSiteId:\s*["\'][^"\']*["\']', f'raptiveSiteId: "{site_id}"', code)
    code = re.sub(r'provider:\s*["\'][^"\']*["\']', 'provider: "raptive"', code)
    code = re.sub(r'enabled:\s*(true|false)', 'enabled: true', code)
    write_file(AD_MANAGER_PATH, code)
    print(f"Successfully enabled Raptive with Site ID: {site_id}")
    return True


def disable_raptive() -> bool:
    if not os.path.exists(AD_MANAGER_PATH):
        return False
    code = read_file(AD_MANAGER_PATH)
    code = re.sub(r'enabled:\s*(true|false)', 'enabled: false', code)
    code = re.sub(r'provider:\s*["\'][^"\']*["\']', 'provider: "house"', code)
    write_file(AD_MANAGER_PATH, code)
    print("Disabled Raptive network ads (reverted to default house / dormant mode).")
    return True


def append_ads_txt(records: str) -> None:
    current = read_file(ADS_TXT_PATH)
    lines_to_add = [r.strip() for r in records.strip().splitlines() if r.strip()]
    existing_lines = set(current.splitlines())

    new_lines = [line for line in lines_to_add if line not in existing_lines]
    if not new_lines:
        print("All records already present in ads.txt.")
        return

    updated = current.rstrip() + "\n\n# Added via manage_ads.py\n" + "\n".join(new_lines) + "\n"
    write_file(ADS_TXT_PATH, updated)
    print(f"Appended {len(new_lines)} record(s) to ads.txt.")


def validate_ads_txt() -> bool:
    if not os.path.exists(ADS_TXT_PATH):
        print("ads.txt is missing!")
        return False

    content = read_file(ADS_TXT_PATH)
    valid_format = re.compile(r"^[\w\.\-]+,\s*[\w\.\-]+,\s*(DIRECT|RESELLER)(\s*,\s*[\w\.\-]+)?$", re.I)
    errors = []
    lines = content.splitlines()
    seller_count = 0

    for idx, line in enumerate(lines, start=1):
        clean = line.strip()
        if not clean or clean.startswith("#"):
            continue
        seller_count += 1
        if not valid_format.match(clean):
            errors.append(f"Line {idx}: Invalid ads.txt format -> '{clean}'")

    print(f"Total seller records found: {seller_count}")
    if errors:
        print("Validation errors encountered:")
        for err in errors:
            print(f"  - {err}")
        return False
    print("ads.txt syntax is valid.")
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--status", action="store_true", help="Print current ad framework status")
    parser.add_argument("--enable-raptive", metavar="SITE_ID", help="Activate Raptive with the given publisher site ID")
    parser.add_argument("--disable-raptive", action="store_true", help="Deactivate Raptive network ads")
    parser.add_argument("--append-ads-txt", metavar="RECORDS", help="Add ads.txt seller records")
    parser.add_argument("--validate-ads-txt", action="store_true", help="Validate syntax of ads.txt")

    args = parser.parse_args()

    if args.enable_raptive:
        enable_raptive(args.enable_raptive)
        return 0

    if args.disable_raptive:
        disable_raptive()
        return 0

    if args.append_ads_txt:
        append_ads_txt(args.append_ads_txt)
        return 0

    if args.validate_ads_txt:
        return 0 if validate_ads_txt() else 1

    # Default: status
    status = get_status()
    print("=========================================")
    print("       RAPTIVE AD SYSTEM STATUS          ")
    print("=========================================")
    print(f"  Ad System Enabled       : {status['enabled']}")
    print(f"  Active Provider         : {status['provider']}")
    print(f"  Raptive Site ID         : {status['raptive_site_id'] or '(not set)'}")
    print(f"  CLS Safety (CSS Contain): {'PASS' if status['cls_safe'] else 'FAIL'}")
    print(f"  ads.txt Present         : {'YES' if status['ads_txt_exists'] else 'NO'}")
    print(f"  Active Seller Records   : {status['ads_txt_seller_records']}")
    print("=========================================")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
