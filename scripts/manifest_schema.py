#!/usr/bin/env python3
"""Model, brand and package-name rules for ``slidia_manifest.xml``.

The manifest has always named one model per line::

    <package name="Rondo" repo="jarvissax/rondo" device="Y1" ... />

A row may now name every model it serves, and a package name for each of
them, without repeating the repository::

    <package name="Reborn" repo="schulzcode/y2linux"
             devices="Y1,Y2,G5" package_name_y1="rom.zip"
             package_name_y2="rom_y2.zip" package_name_g5="rom_g5.zip" ... />

``device`` keeps working exactly as before, so an old row needs no change and
the app can read both shapes. A model entry may carry its brand
(``Timmkoo/Q3`` or ``Timmkoo:Q3``) so two brands that share a model number
stay apart. Nothing here is a fixed list of models: a model the manifest
gains later is read from the row itself.

Package name resolution, most specific first:

    1. package_name_<brand>_<model>_type_<a|b>
    2. package_name_<model>_type_<a|b>
    3. package_name_<brand>_<model>
    4. package_name_<model>
    5. package_name
    6. the historic default: rom.zip on the Y1, rom_<model>.zip elsewhere

Attribute names are matched without case, so ``package_name_A5`` and
``package_name_a5`` are the same declaration.
"""
from __future__ import annotations

import re

SPLIT_RE = re.compile(r"[\s,;]+")
KEY_CLEAN_RE = re.compile(r"[^a-z0-9]+")


def _key(value: str) -> str:
    return KEY_CLEAN_RE.sub("_", str(value or "").lower()).strip("_")


def device_specs(attributes: dict) -> list[dict]:
    """Every model a row covers, with the brand that qualifies it.

    ``devices`` wins over ``device`` when both are present, so a row can be
    migrated one attribute at a time. Entries are de-duplicated, keeping the
    order the row lists them in.
    """
    values = {str(key).lower(): str(value or "").strip() for key, value in (attributes or {}).items()}
    raw = values.get("devices") or values.get("device") or ""
    row_brand = values.get("brand") or ""
    specs: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for entry in SPLIT_RE.split(raw):
        entry = entry.strip()
        if not entry:
            continue
        brand = row_brand
        model = entry
        if "/" in entry or ":" in entry:
            head, _, tail = entry.replace(":", "/").partition("/")
            brand = head.strip()
            model = tail.strip()
        model = model.upper()
        if not model:
            continue
        key = (brand.lower(), model)
        if key in seen:
            continue
        seen.add(key)
        specs.append({"brand": brand, "model": model})
    return specs


def device_types(attributes: dict) -> dict:
    """Hardware types a row declares, from ``type_a_asset`` / ``type_b_asset``."""
    values = {str(key).lower(): str(value or "") for key, value in (attributes or {}).items()}
    return {
        "A": bool(values.get("type_a_asset", "").strip()),
        "B": bool(values.get("type_b_asset", "").strip()),
    }


def default_package_name(model: str) -> str:
    """The asset name the app assumes when a row names none."""
    value = str(model or "").upper()
    if not value or value == "Y1":
        return "rom.zip"
    return "rom_%s.zip" % value.lower()


def declared_package_name(attributes: dict, model: str, brand: str = "", device_type: str = "") -> str:
    """The package name a row declares for one model, or ``""``.

    Returning ``""`` rather than the default lets a caller keep a value it
    already has instead of overwriting it with an assumption.
    """
    values = {str(key).lower(): str(value or "").strip() for key, value in (attributes or {}).items()}
    model_key = _key(model)
    brand_key = _key(brand)
    type_key = re.sub(r"^type_?", "", str(device_type or "").lower())
    candidates: list[str] = []
    if type_key and brand_key:
        candidates.append("package_name_%s_%s_type_%s" % (brand_key, model_key, type_key))
    if type_key:
        candidates.append("package_name_%s_type_%s" % (model_key, type_key))
    if brand_key:
        candidates.append("package_name_%s_%s" % (brand_key, model_key))
    candidates.append("package_name_%s" % model_key)
    candidates.append("package_name")
    for key in candidates:
        value = values.get(key) or ""
        if value:
            return value
    return ""


def package_name_for(attributes: dict, model: str, brand: str = "", device_type: str = "") -> str:
    """The ROM asset name for one model of a row, default included."""
    return declared_package_name(attributes, model, brand, device_type) or default_package_name(model)


def expand_packages(rows: list[dict]) -> list[dict]:
    """One copy of each manifest row per model it serves.

    The copy keeps every attribute the row had, so callers that read
    ``icon``, ``post_install`` or ``portable_zips`` need no change; ``device``
    becomes that model, ``brand`` becomes its brand, and ``package_name`` is
    the name declared for that model when the row declares one.
    """
    expanded: list[dict] = []
    for row in rows or []:
        specs = device_specs(row)
        if not specs:
            expanded.append(row)
            continue
        for spec in specs:
            copy = dict(row)
            copy["device"] = spec["model"]
            if spec.get("brand"):
                copy["brand"] = spec["brand"]
            declared = declared_package_name(row, spec["model"], copy.get("brand", ""))
            if declared:
                copy["package_name"] = declared
            expanded.append(copy)
    return expanded


def package_names(attributes: dict, model: str, brand: str = "") -> dict:
    """Both package names a row can carry for one model.

    ``{"package": <name>, "type_b": <name or "">}``. A row that names no Type B
    package keeps ``""`` there, so a caller never invents one.
    """
    return {
        "package": package_name_for(attributes, model, brand),
        "type_b": declared_package_name(attributes, model, brand, "b"),
    }
