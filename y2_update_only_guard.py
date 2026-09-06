"""Fail-closed Y2 Class A update-only plan builder (no device access)."""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import struct
from pathlib import Path
from xml.etree import ElementTree as ET

ALLOWED = {
    "UBOOT": (8, "lk.bin", 0x03120000, 0x00060000),
    "BOOTIMG": (9, "boot.img", 0x03180000, 0x01000000),
    "RECOVERY": (10, "recovery.img", 0x04180000, 0x01000000),
    "LOGO": (13, "logo.bin", 0x05800000, 0x00300000),
    "ANDROID": (16, "system.img", 0x06580000, 0x33400000),
}
EXPECTED_MEMBERS = {v[1] for v in ALLOWED.values()} | {
    "MT6582_Android_scatter.txt", "UPDATE-MANIFEST.json", "SHA256SUMS.txt"
}
LAUNCH_XML = "Y2-Beta2-DOWNLOAD-ONLY.xml"
LAUNCH_PLAN = "windows-update-only-plan.json"
ACTIVE_LAUNCH_FILES = {"MT6582_Android_scatter.txt"} | {v[1] for v in ALLOWED.values()}
FORBIDDEN = (
    "formatall", "format-download", "combo-format", "firmware-upgrade",
    "preloader", "mbr", "ebr1", "ebr2", "pro_info", "nvram", "protect_f",
    "protect_s", "seccfg", "sec_ro", "misc", "cache", "userdata", "fat", "bmtpool",
)
TRUSTED = {
    "source": "2cf163bdc0e29faf1c16e117c2bb95fcfe875f03af5849870db80d78a4271f99",
    "candidate": "409ddb4d2d18111fb8c3ab619f10f04b916b6b2a3fc04d1d38011324563f326a",
    "scatter": "dc2f0769ed4697fe16846fab092a2d7fd91f6ea117957c9ec4b8ef5eca83e658",
    "manifest": "4edbf375093a279e7bbedb2eef7fd6b86a1dbee241bd5004f261f5d6b2bdaa1a",
    "checksums": "c540467b15f112cdc299d30648f331162a1a633e87bf6aed630f0a74349d9abd",
    "lk.bin": "bd001af26174188ab34bb908b5b99e2bc128aa71299905c27353c67bb84d9664",
    "boot.img": "9272587463fb05c7076d8c67fac793e579638d5ccb558d19a353e283e664632b",
    "recovery.img": "43c3de3d605f00868ff29055f1c3a368c91b2c6c9897c11442775924bebdfed7",
    "logo.bin": "b1d37ff6c4b4868fe62fb97e662fba768699d0c27219e2199ee816bf643a1a2d",
    "system.img": "3c2370134a533389dba76b6e26eda1d6296a695e73969492a2fc0530014983de",
    "system.raw": "805ed8a23e1df13867c5ee789117ca90c6680779d20dd8884ad413ddd98fb00c",
    "flash_tool": "8aa16765f811f9b665dd1dc110f68081a4bcd8efa19832cb49b23cfd031881df",
    "da": "4729b77976508708a541039a807f3203f68a37e91ebbc832ac7db70b4ea6d832",
    "storage_setting": "ee26162cd2eb07653e9bf3f81711f64b2eba615f7bbc4a8970fdd954b66bb918",
}
TRUSTED_SIZES = {
    "candidate": 361774260, "flash_tool": 10514944, "da": 12945664,
    "storage_setting": 44932,
    "scatter": 7673, "manifest": 3578, "checksums": 472,
    "lk.bin": 242440, "boot.img": 5804032, "recovery.img": 5793792,
    "logo.bin": 114955, "system.img": 522197348,
}
MBR_PROBE_START = 0x01400000
MBR_PROBE_LENGTH = 0x200
MBR_PROBE_SHA256 = "4be9c92be18ba4169d4b050e18811c6650eab27a487f1c67f4a49efa01cd32a1"


class GuardError(RuntimeError):
    pass


# ext4 fields observed changing normally across the physically qualified V16/V17
# and V28 Windows write/readbacks. V28 completed three previously partial
# four-byte inode ctime_extra fields at 0x57A84, 0x57B84, and 0x61A84; every
# filesystem path and file content still matched. Differences outside these
# bytes or sparse DONT_CARE chunks fail closed. Offsets are in expanded ANDROID.
ANDROID_EXT4_MUTABLE_OFFSETS = frozenset((1068,1069,1070,1071,1072,1073,1074,1075,
    1076,1088,1089,1090,1091,1376,1400,4124,4125,4126,4127,4156,4157,4158,4159,
    4188,4189,4190,4191,4220,4221,4222,4223,4252,4253,4254,4255,4284,4285,4286,
    4287,4316,4317,4318,4319,358912,358914,358915,358924,358925,358926,358927,
    358936,358937,359044,359045,359046,359047,359168,359180,359181,359182,359183,
    359300,359301,359302,359303,399872,399884,399885,399886,399887,399896,399897,
    400004,400005,400006,400007,2162715))


def verify_sparse_aware_android(sparse_path: Path, readback_path: Path) -> dict:
    """Compare every written sparse byte, ignore DONT_CARE, and bound ext4 churn."""
    sparse_path = require_ordinary_file(sparse_path, "sparse system image")
    readback_path = require_ordinary_file(readback_path, "ANDROID readback")
    if readback_path.stat().st_size != 0x33400000:
        raise GuardError("ANDROID readback size changed")
    differences = []
    compared = ignored = position = 0
    with sparse_path.open("rb") as src, readback_path.open("rb") as actual:
        header = src.read(28)
        magic, major, minor, file_hdr, chunk_hdr, block, total_blocks, chunks, checksum = struct.unpack("<I4H4I", header)
        if magic != 0xED26FF3A or major != 1 or file_hdr < 28 or chunk_hdr < 12:
            raise GuardError("Malformed Android sparse header")
        src.seek(file_hdr)
        for _ in range(chunks):
            kind, reserved, count, total = struct.unpack("<2H2I", src.read(chunk_hdr)); payload = total-chunk_hdr; raw=count*block
            if kind == 0xCAC1:
                expected=src.read(payload); got=actual.read(raw)
            elif kind == 0xCAC2:
                pattern=src.read(4); expected=(pattern*((raw+3)//4))[:raw]; got=actual.read(raw)
            elif kind == 0xCAC3:
                src.read(payload); actual.seek(raw,1); ignored += raw; position += raw; continue
            elif kind == 0xCAC4:
                src.read(payload); continue
            else: raise GuardError("Unknown sparse chunk")
            if len(expected)!=raw or len(got)!=raw: raise GuardError("Sparse/readback truncation")
            for i,(a,b) in enumerate(zip(expected,got)):
                if a!=b:
                    offset=position+i
                    if offset not in ANDROID_EXT4_MUTABLE_OFFSETS: raise GuardError(f"ANDROID written byte changed at 0x{offset:x}")
                    differences.append(offset)
            compared += raw; position += raw
    with readback_path.open("rb") as f: f.seek(1080); magic=f.read(2)
    if magic != b'\x53\xef': raise GuardError("ANDROID readback is not the expected ext4 filesystem")
    return {"status":"PASS","read_size":readback_path.stat().st_size,"written_bytes_compared":compared,
            "dont_care_bytes_ignored":ignored,"allowed_ext4_changed_offsets":differences,
            "allowed_ext4_changed_byte_count":len(differences)}


def verify_post_write_readbacks(report: dict, readback_dir: Path) -> dict:
    """Verify four exact images plus sparse-aware ANDROID; exactly five outputs."""
    readback_dir=Path(readback_dir).resolve(); expected={p["name"]+".img" for p in report["plan"]}
    if {p.name for p in readback_dir.iterdir() if p.is_file()} != expected: raise GuardError("Readback inventory differs")
    results=[]
    for p in report["plan"]:
        out=require_ordinary_file(readback_dir/(p["name"]+".img"),p["name"]+" readback")
        aligned=(p["write_size"]+0x1ff)&~0x1ff
        if out.stat().st_size!=aligned: raise GuardError("Readback size changed: "+p["name"])
        if p["name"]=="ANDROID": result=verify_sparse_aware_android(Path(report["app_dir"])/p["file"],out)
        else:
            h=hashlib.sha256()
            with out.open('rb') as f:
                remaining=p["write_size"]
                while remaining:
                    data=f.read(min(1024*1024,remaining));h.update(data);remaining-=len(data)
            if h.hexdigest()!=p["payload_sha256"]: raise GuardError("Readback prefix mismatch: "+p["name"])
            result={"status":"PASS","verified_length":p["write_size"],"sha256":h.hexdigest(),"alignment_extra":aligned-p["write_size"]}
        results.append({"partition":p["name"],**result})
    return {"schema":1,"status":"PASS","sparse_aware_android":True,"results":results}


def must_block_generic_tool(app_dir: Path, ui_model: str | None) -> bool:
    """Disk evidence wins over stale/unknown UI state for unguarded routes."""
    model = (ui_model or "").upper()
    scatter = Path(app_dir) / "MT6582_Android_scatter.txt"
    disk_y2 = False
    if scatter.is_file():
        text = scatter.read_text(encoding="utf-8", errors="replace")
        disk_y2 = "platform: MT6582" in text or "project: eastaeon82_wet_kk" in text
    return disk_y2 or "Y2" in model or not model


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def require_ordinary_file(path: Path, label: str) -> Path:
    path = Path(path)
    try:
        info = path.lstat()
    except OSError as exc:
        raise GuardError(f"Missing {label}: {path}") from exc
    reparse = bool(getattr(info, "st_file_attributes", 0) & getattr(os, "FILE_ATTRIBUTE_REPARSE_POINT", 0x400))
    if path.is_symlink() or reparse or not path.is_file():
        raise GuardError(f"{label} must be an ordinary file, not a symlink/reparse point: {path}")
    return path


def audit_storage_setting_bytes(data: bytes) -> None:
    if len(data) != TRUSTED_SIZES["storage_setting"] or hashlib.sha256(data).hexdigest() != TRUSTED["storage_setting"]:
        raise GuardError("storage_setting.xml identity changed")
    try:
        root = ET.fromstring(data)
    except ET.ParseError as exc:
        raise GuardError(f"storage_setting.xml is invalid: {exc}") from exc
    if root.tag != "storage-setting":
        raise GuardError("storage_setting.xml root must be storage-setting")
    platforms = [p for p in root.findall("platform") if p.attrib.get("name", "").strip() == "MT6582"]
    if len(platforms) != 1:
        raise GuardError("storage_setting.xml must contain exactly one MT6582 platform")
    emmc = platforms[0].find("emmc")
    expected = {"type-name":"EMMC", "is-support":"true",
        "hw-storage-type":"HW_STORAGE_EMMC", "mem-storage-type":"HW_MEM_EMMC",
        "storage-addressing-type":"16"}
    if emmc is None or any(emmc.attrib.get(k, "").strip() != v for k, v in expected.items()):
        raise GuardError("MT6582 EMMC storage settings changed")


def validate_storage_setting(path: Path) -> dict:
    path = require_ordinary_file(path, "storage_setting.xml")
    data = path.read_bytes()
    audit_storage_setting_bytes(data)
    return {"size": len(data), "sha256": hashlib.sha256(data).hexdigest()}


def require_exact_launch_inventory(app_dir: Path) -> None:
    """Refuse any untrusted firmware material in Flash Tool's application cwd.

    This legacy build needs its shipped DLL/config files in the cwd, so the
    directory cannot contain *only* firmware.  The active firmware set can and
    must still be exact.  Manufacturer support inputs (the pinned DA and the
    shipped *_def/MT6572 scatter templates) are not selectable ROM payloads.
    """
    app_dir = Path(app_dir).resolve()
    if not app_dir.is_dir() or app_dir.is_symlink():
        raise GuardError(f"Flash Tool working directory is missing or substituted: {app_dir}")
    validate_storage_setting(app_dir / "storage_setting.xml")
    permitted_support = {
        "mtk_allinone_da.bin", "mt6582_android_scatter_def.txt",
        "mt6572_android_scatter.txt", "mt6572_android_scatter_def.txt",
    }
    active = set()
    extras = []
    firmware_suffixes = {".img", ".bin"}
    for item in app_dir.iterdir():
        lower = item.name.lower()
        looks_like_firmware = (item.suffix.lower() in firmware_suffixes
                               or ("scatter" in lower and item.suffix.lower() == ".txt"))
        if not looks_like_firmware:
            continue
        if lower in permitted_support:
            require_ordinary_file(item, "pinned Flash Tool support input")
            continue
        if item.name in ACTIVE_LAUNCH_FILES:
            require_ordinary_file(item, "active launch firmware")
            active.add(item.name)
        else:
            extras.append(item.name)
    if active != ACTIVE_LAUNCH_FILES or extras:
        raise GuardError(f"Active firmware inventory differs: extra={sorted(extras)} missing={sorted(ACTIVE_LAUNCH_FILES-active)}")


def prepare_application_launch_dir(source_stage: Path, app_dir: Path, candidate: Path,
                                   flash_tool: Path, da: Path, log_dir: Path) -> tuple[dict, Path, Path]:
    """Materialize the exact six active inputs into the legacy tool cwd."""
    source_stage, app_dir = Path(source_stage).resolve(), Path(app_dir).resolve()
    if Path(flash_tool).resolve().parent != app_dir or Path(da).resolve().parent != app_dir:
        raise GuardError("Flash Tool and DA must remain in the pinned application directory")
    validate_storage_setting(app_dir / "storage_setting.xml")
    source_report = validate_stage(source_stage, candidate)
    # Metadata is copied too so the materialized bytes can be independently
    # revalidated; only the scatter and five images are active firmware.
    for name in EXPECTED_MEMBERS:
        source = require_ordinary_file(source_stage / name, "validated staging input")
        destination = app_dir / name
        if destination.exists():
            require_ordinary_file(destination, "existing launch input")
            if destination.stat().st_size != source.stat().st_size or sha256(destination) != sha256(source):
                raise GuardError(f"Stale same-named launch file must be removed explicitly: {destination}")
        else:
            shutil.copyfile(source, destination)
    report = validate_stage(app_dir, candidate)
    if plan_document(report) != plan_document(source_report):
        raise GuardError("Application launch stage differs from the validated extraction")
    plan = write_plan(report, app_dir / LAUNCH_PLAN)
    xml = build_download_only_xml(app_dir, candidate, flash_tool, da,
                                  app_dir / LAUNCH_XML, log_dir,
                                  validated_report=report)
    require_exact_launch_inventory(app_dir)
    return report, xml, plan


def validate_candidate_archive(candidate_archive: Path | str | None) -> Path:
    """Return the exact absolute candidate, refusing basename reconstruction."""
    if candidate_archive is None:
        raise GuardError("Accepted candidate archive path is missing")
    candidate = Path(candidate_archive)
    if not candidate.is_absolute():
        raise GuardError("Candidate archive path must be absolute; basenames are refused")
    try:
        candidate = candidate.resolve(strict=True)
    except OSError as exc:
        raise GuardError("Accepted candidate archive was moved or deleted") from exc
    require_ordinary_file(candidate, "candidate archive")
    if candidate.stat().st_size != TRUSTED_SIZES["candidate"] or sha256(candidate) != TRUSTED["candidate"]:
        raise GuardError("Accepted candidate archive identity is missing or changed")
    return candidate


def validate_stage_light(app_dir: Path, candidate_archive: Path | str | None) -> Path:
    """Cheap GUI-thread gate; the worker repeats full validation before launch."""
    candidate = validate_candidate_archive(candidate_archive)
    app_dir = Path(app_dir).resolve()
    missing = sorted(name for name in EXPECTED_MEMBERS if not (app_dir / name).is_file())
    if missing:
        raise GuardError(f"Missing Class A files: {missing}")
    forbidden_names = {"preloader_eastaeon82_wet_kk.bin", "mbr", "ebr1", "ebr2", "secro.img", "cache.img", "userdata.img"}
    dangerous = sorted(p.name for p in app_dir.iterdir() if p.is_file() and p.name.lower() in forbidden_names)
    if dangerous:
        raise GuardError("Class A stage contains stale forbidden payloads; clean the staging directory and re-extract: " + ", ".join(dangerous))
    return candidate


def parse_scatter(path: Path) -> tuple[str, str, list[dict]]:
    text = path.read_text(encoding="utf-8", errors="strict")
    platform = re.search(r"(?m)^\s*platform:\s*(\S+)", text)
    project = re.search(r"(?m)^\s*project:\s*(\S+)", text)
    parts = []
    for block in re.split(r"(?m)^-\s*partition_index:\s*", text)[1:]:
        def field(name: str) -> str:
            m = re.search(rf"(?m)^\s*{re.escape(name)}:\s*(\S+)", block)
            return m.group(1) if m else ""
        idx = re.match(r"SYS(\d+)", block)
        parts.append({
            "index": int(idx.group(1)) if idx else -1,
            "name": field("partition_name"), "file": field("file_name"),
            "download": field("is_download").lower() == "true",
            "start": int(field("linear_start_addr") or "0", 0),
            "capacity": int(field("partition_size") or "0", 0),
            "region": field("region"), "storage": field("storage"),
        })
    return platform.group(1) if platform else "", project.group(1) if project else "", parts


def sparse_raw_identity(path: Path) -> tuple[int, str]:
    """Fully decode Android sparse chunks into a streaming raw SHA-256."""
    h = hashlib.sha256()
    with path.open("rb") as f:
        header = f.read(28)
        if len(header) != 28:
            raise GuardError("Truncated sparse header")
        magic, major, _, file_hdr, chunk_hdr, block, total_blocks, total_chunks, _ = struct.unpack("<IHHHHIIII", header)
        if magic != 0xED26FF3A or major != 1 or file_hdr < 28 or chunk_hdr < 12 or block <= 0:
            raise GuardError("Invalid sparse header")
        if file_hdr > 28 and len(f.read(file_hdr - 28)) != file_hdr - 28:
            raise GuardError("Truncated extended sparse header")
        blocks_seen = 0
        zero = b"\0" * (1024 * 1024)
        for _ in range(total_chunks):
            ch = f.read(chunk_hdr)
            if len(ch) != chunk_hdr:
                raise GuardError("Truncated sparse chunk header")
            kind, _, chunks, total_size = struct.unpack_from("<HHII", ch)
            raw_bytes = chunks * block
            data_bytes = total_size - chunk_hdr
            if kind == 0xCAC1:
                if data_bytes != raw_bytes:
                    raise GuardError("Malformed RAW sparse chunk")
                remaining = raw_bytes
                while remaining:
                    data = f.read(min(1024 * 1024, remaining))
                    if not data:
                        raise GuardError("Truncated RAW sparse chunk")
                    h.update(data); remaining -= len(data)
            elif kind == 0xCAC2:
                fill = f.read(4)
                if data_bytes != 4 or len(fill) != 4:
                    raise GuardError("Malformed FILL sparse chunk")
                pattern = fill * (len(zero) // 4)
                remaining = raw_bytes
                while remaining:
                    data = pattern[:min(len(pattern), remaining)]; h.update(data); remaining -= len(data)
            elif kind == 0xCAC3:
                if data_bytes != 0:
                    raise GuardError("Malformed DONT_CARE sparse chunk")
                remaining = raw_bytes
                while remaining:
                    data = zero[:min(len(zero), remaining)]; h.update(data); remaining -= len(data)
            elif kind == 0xCAC4:
                if data_bytes != 4 or len(f.read(4)) != 4:
                    raise GuardError("Malformed CRC sparse chunk")
                raw_bytes = 0
            else:
                raise GuardError(f"Unknown sparse chunk 0x{kind:04x}")
            blocks_seen += chunks
        if blocks_seen != total_blocks or f.read(1):
            raise GuardError("Sparse block count or trailing bytes mismatch")
    return total_blocks * block, h.hexdigest()


def validate_stage(app_dir: Path, candidate_archive: Path | None = None) -> dict:
    app_dir = Path(app_dir).resolve()
    candidate_archive = validate_candidate_archive(candidate_archive)
    missing = sorted(name for name in EXPECTED_MEMBERS if not (app_dir / name).is_file())
    if missing:
        raise GuardError(f"Missing Class A files: {missing}")
    dangerous = sorted(p.name for p in app_dir.iterdir() if p.is_file() and p.name.lower() in {
        "preloader_eastaeon82_wet_kk.bin", "mbr", "ebr1", "ebr2", "secro.img", "cache.img", "userdata.img"
    })
    if dangerous:
        raise GuardError(f"Class A stage contains forbidden payloads: {dangerous}")
    if sha256(app_dir / "UPDATE-MANIFEST.json") != TRUSTED["manifest"] or sha256(app_dir / "SHA256SUMS.txt") != TRUSTED["checksums"]:
        raise GuardError("Trusted manifest/checksum identity changed")
    manifest = json.loads((app_dir / "UPDATE-MANIFEST.json").read_text(encoding="utf-8"))
    if manifest.get("status") != "PRODUCTION RELEASE - CLASS A UPDATE ONLY":
        raise GuardError("Candidate is not the reviewed production Class A release")
    if manifest.get("source", {}).get("sha256", "").lower() != TRUSTED["source"]:
        raise GuardError("Accepted source identity changed")
    contract = manifest.get("installer_contract", {})
    if contract.get("class") != "state-preserving update-only" or contract.get("format_all_permitted") is not False or contract.get("erase_omitted_partitions_permitted") is not False or contract.get("post_write_verification_required") is not True:
        raise GuardError("Manifest does not declare the required Class A contract")
    files = manifest.get("files", {})
    if set(files) != EXPECTED_MEMBERS - {"UPDATE-MANIFEST.json", "SHA256SUMS.txt"}:
        raise GuardError("Manifest file allowlist differs from the Class A contract")
    for name, record in files.items():
        path = app_dir / name
        trusted_hash = TRUSTED["scatter"] if name == "MT6582_Android_scatter.txt" else TRUSTED.get(name)
        if path.stat().st_size != record.get("size") or sha256(path) != trusted_hash or str(record.get("sha256", "")).lower() != trusted_hash:
            raise GuardError(f"Hash/size mismatch: {name}")
    if sha256(app_dir / "MT6582_Android_scatter.txt") != TRUSTED["scatter"]:
        raise GuardError("Trusted scatter identity changed")
    platform, project, parts = parse_scatter(app_dir / "MT6582_Android_scatter.txt")
    if (platform, project) != ("MT6582", "eastaeon82_wet_kk"):
        raise GuardError(f"Wrong scatter identity: {platform}/{project}")
    enabled = {p["name"]: p for p in parts if p["download"]}
    if set(enabled) != set(ALLOWED):
        raise GuardError(f"Enabled partition set differs: {sorted(enabled)}")
    plan = []
    for name, (index, filename, start, capacity) in ALLOWED.items():
        part = enabled[name]
        if (part["index"], part["file"], part["start"], part["capacity"], part["region"], part["storage"]) != (index, filename, start, capacity, "EMMC_USER", "HW_STORAGE_EMMC"):
            raise GuardError(f"Scatter contract mismatch: {name}")
        if name == "ANDROID":
            write_size, raw_hash = sparse_raw_identity(app_dir / filename)
            if (write_size, raw_hash) != (0x33400000, TRUSTED["system.raw"]):
                raise GuardError("Decoded Android identity changed")
        else:
            write_size, raw_hash = (app_dir / filename).stat().st_size, TRUSTED[filename]
        if not write_size or write_size > part["capacity"]:
            raise GuardError(f"Image exceeds target bounds: {name}")
        plan.append({**part, "write_size": write_size, "payload_sha256": TRUSTED[filename], "expected_readback_sha256": raw_hash})
    return {"app_dir": str(app_dir), "candidate_archive": str(candidate_archive), "plan": plan, "manifest": manifest}


def build_download_only_xml(app_dir: Path, candidate_archive: Path, flash_tool: Path, download_agent: Path, output: Path, log_dir: Path, com_port: str = "", validated_report: dict | None = None) -> Path:
    if sha256(Path(flash_tool)) != TRUSTED["flash_tool"] or sha256(Path(download_agent)) != TRUSTED["da"]:
        raise GuardError("Flash Tool or Download Agent identity changed")
    if validated_report is not None:
        candidate = validate_candidate_archive(candidate_archive)
        if (Path(validated_report.get("app_dir", "")).resolve() != Path(app_dir).resolve()
                or validated_report.get("candidate_archive") != str(candidate)):
            raise GuardError("Cached validation report is not bound to these launch inputs")
        report = validated_report
    else:
        report = validate_stage(app_dir, candidate_archive)
    app_dir, output = Path(app_dir).resolve(), Path(output).resolve()
    root = ET.Element("flashtool-config", {"version": "2.0"})
    general = ET.SubElement(root, "general")
    fixed_cwd = Path(flash_tool).resolve().parent == app_dir and Path(download_agent).resolve().parent == app_dir
    # Production uses cwd-bound basenames. External-tool paths remain available
    # only to the portable offline auditor/tests; the production preparer above
    # refuses that topology.
    da_value = Path(download_agent).name if fixed_cwd else str(Path(download_agent).resolve())
    scatter_value = "MT6582_Android_scatter.txt" if fixed_cwd else str(app_dir / "MT6582_Android_scatter.txt")
    for tag, value in (("chip-name", "MT6582"), ("storage-type", "EMMC"), ("download-agent", da_value), ("scatter", scatter_value), ("authentication", ""), ("certification", "")):
        ET.SubElement(general, tag).text = value
    rom_list = ET.SubElement(general, "rom-list")
    for p in report["plan"]:
        ET.SubElement(rom_list, "rom", {"index": str(p["index"]), "enable": "true"}).text = p["file"]
    ET.SubElement(general, "connection", {"type": "BromUSB", "high-speed": "true", "power": "AutoDetect", "da_log_level": "Info", "da_log_channel": "UART", "timeout-count": "3600000", "com-port": com_port})
    ET.SubElement(general, "checksum-level").text = "usb"
    if fixed_cwd:
        if Path(log_dir).resolve() != (app_dir / "SP_FT_Logs").resolve():
            raise GuardError("Flash Tool log directory must be SP_FT_Logs in the pinned working directory")
        (app_dir / "SP_FT_Logs").mkdir(exist_ok=True)
        log_value = "SP_FT_Logs"
    else:
        log_value = str(Path(log_dir).resolve())
    ET.SubElement(general, "log-info", {"log_on": "true", "log_path": log_value, "clean_hours": "720"})
    commands = ET.SubElement(root, "commands")
    ET.SubElement(ET.SubElement(commands, "download-only"), "da-download-all")
    ET.indent(root, space="  ")
    output.write_bytes(b'<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="utf-8") + b"\n")
    audit_download_only_xml(output, report, download_agent, log_dir)
    return output


def plan_document(report: dict) -> dict:
    plan = {"schema": 2, "status": "OFFLINE-VALIDATED-NOT-WRITTEN", "write_plan": []}
    for p in report["plan"]:
        plan["write_plan"].append({
            "partition": p["name"], "index": p["index"], "file": p["file"],
            "storage_region": "EMMC_USER", "part_id": 8,
            "address_mode": "NUTL_ADDR_LOGICAL",
            "logical_start": p["start"], "logical_start_hex": f'0x{p["start"]:x}',
            "capacity": p["capacity"], "write_size": p["write_size"],
            "payload_sha256": p["payload_sha256"],
            "expected_readback_sha256": p["expected_readback_sha256"],
        })
    return plan


def write_plan(report: dict, path: Path) -> Path:
    plan = plan_document(report)
    Path(path).write_text(json.dumps(plan, indent=2) + "\n", encoding="utf-8", newline="\n")
    return Path(path)


def build_readback_xml(report: dict, output: Path, download_agent: Path, readback_dir: Path, log_dir: Path) -> Path:
    root = ET.Element("flashtool-config", {"version": "2.0"}); general = ET.SubElement(root, "general")
    for tag, value in (("chip-name","MT6582"),("storage-type","EMMC"),("download-agent",str(Path(download_agent).resolve())),("scatter",str(Path(report["app_dir"])/"MT6582_Android_scatter.txt")),("authentication",""),("certification","")):
        ET.SubElement(general, tag).text=value
    ET.SubElement(general,"rom-list"); ET.SubElement(general,"connection",{"type":"BromUSB","high-speed":"true","power":"AutoDetect","da_log_level":"Info","da_log_channel":"UART","timeout-count":"3600000","com-port":""}); ET.SubElement(general,"checksum-level").text="usb"; ET.SubElement(general,"log-info",{"log_on":"true","log_path":str(Path(log_dir).resolve()),"clean_hours":"720"})
    readback=ET.SubElement(ET.SubElement(root,"commands"),"readback"); ET.SubElement(readback,"physical-readback",{"is-physical-readback":"false"}); items=ET.SubElement(readback,"readback-list")
    for i,p in enumerate(report["plan"]):
        read_length = (p["write_size"] + 0x1ff) & ~0x1ff
        ET.SubElement(items,"readback-rom-item",{"readback-index":str(i),"readback-enable":"true","part-id":"8","start-address":f'0x{p["start"]:x}',"readback-length":f'0x{read_length:x}',"readback-flag":"NUTL_READ_PAGE_ONLY","addr-flag":"NUTL_ADDR_LOGICAL"}).text=str((Path(readback_dir)/(p["name"]+".img")).resolve())
    ET.indent(root,space="  "); Path(output).write_bytes(b'<?xml version="1.0" encoding="UTF-8"?>\n'+ET.tostring(root,encoding="utf-8")+b'\n')
    audit_readback_xml(output, report, download_agent, Path(report["app_dir"])/"MT6582_Android_scatter.txt", log_dir, readback_dir)
    return Path(output)


def build_mbr_read_only_probe_xml(output: Path, download_agent: Path,
                                  scatter: Path, readback_output: Path,
                                  log_dir: Path) -> Path:
    """Build the single-sector qualification probe; this never executes it."""
    download_agent = require_ordinary_file(download_agent, "probe Download Agent").resolve()
    scatter = require_ordinary_file(scatter, "probe scatter").resolve()
    if (sha256(download_agent) != TRUSTED["da"]
            or sha256(scatter) != TRUSTED["scatter"]):
        raise GuardError("Probe DA or scatter identity changed")
    validate_storage_setting(download_agent.parent / "storage_setting.xml")
    output = Path(output).resolve()
    readback_output = Path(readback_output).resolve()
    log_dir = Path(log_dir).resolve()
    if readback_output.name != "MBR.bin" or readback_output.parent == output.parent:
        raise GuardError("Probe output must be MBR.bin in a separate fresh evidence directory")
    root = ET.Element("flashtool-config", {"version": "2.0"})
    general = ET.SubElement(root, "general")
    for tag, value in (("chip-name", "MT6582"), ("storage-type", "EMMC"),
                       ("download-agent", str(download_agent)),
                       ("scatter", str(scatter)), ("authentication", ""),
                       ("certification", "")):
        ET.SubElement(general, tag).text = value
    ET.SubElement(general, "rom-list")
    ET.SubElement(general, "connection", {"type":"BromUSB", "high-speed":"true",
        "power":"AutoDetect", "da_log_level":"Info", "da_log_channel":"UART",
        "timeout-count":"3600000", "com-port":""})
    ET.SubElement(general, "checksum-level").text = "usb"
    ET.SubElement(general, "log-info", {"log_on":"true", "log_path":str(log_dir), "clean_hours":"720"})
    readback = ET.SubElement(ET.SubElement(root, "commands"), "readback")
    ET.SubElement(readback, "physical-readback", {"is-physical-readback":"false"})
    items = ET.SubElement(readback, "readback-list")
    ET.SubElement(items, "readback-rom-item", {"readback-index":"0",
        "readback-enable":"true", "part-id":"8", "start-address":f"0x{MBR_PROBE_START:x}",
        "readback-length":f"0x{MBR_PROBE_LENGTH:x}",
        "readback-flag":"NUTL_READ_PAGE_ONLY", "addr-flag":"NUTL_ADDR_LOGICAL"}).text = str(readback_output)
    ET.indent(root, space="  ")
    output.write_bytes(b'<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="utf-8") + b"\n")
    audit_mbr_read_only_probe_xml(output, download_agent, scatter, readback_output, log_dir)
    return output


def mbr_probe_plan_document(readback_output: Path) -> dict:
    return {"schema":1, "status":"OFFLINE-AUDITED-NOT-EXECUTED",
        "command":"readback", "storage_region":"EMMC_USER", "part_id":8,
        "address_mode":"NUTL_ADDR_LOGICAL",
        "start":MBR_PROBE_START, "start_hex":"0x01400000",
        "length":MBR_PROBE_LENGTH, "length_hex":"0x200",
        "output":str(Path(readback_output).resolve()),
        "expected_sha256":MBR_PROBE_SHA256.upper(), "enabled_rom_entries":0,
        "download_permitted":False, "format_permitted":False,
        "erase_permitted":False}


def audit_mbr_probe_plan_bytes(data: bytes, readback_output: Path) -> None:
    try:
        actual = json.loads(data.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise GuardError(f"MBR probe plan is unreadable: {exc}") from exc
    if actual != mbr_probe_plan_document(readback_output):
        raise GuardError("MBR probe plan differs from exact trusted contract")


def audit_mbr_probe_plan(path: Path, readback_output: Path) -> None:
    path = require_ordinary_file(path, "MBR read-only probe plan")
    audit_mbr_probe_plan_bytes(path.read_bytes(), readback_output)


def audit_mbr_read_only_probe_xml_bytes(data: bytes, download_agent: Path,
                                        scatter: Path, readback_output: Path,
                                        log_dir: Path) -> None:
    try:
        text = data.decode("utf-8")
    except UnicodeError as exc:
        raise GuardError(f"Probe XML is unreadable: {exc}") from exc
    lower = text.lower()
    for token in ("download-only", "da-download", "format", "erase", "firmware-upgrade"):
        if token in lower:
            raise GuardError(f"Write-capable token in read-only probe: {token}")
    root = parse_download_only_xml_bytes(data)
    if root.tag != "flashtool-config" or root.attrib != {"version":"2.0"}:
        raise GuardError("Probe XML root changed")
    roms = root.findall("./general/rom-list/rom")
    if roms:
        raise GuardError("Read-only probe must contain no ROM entries")
    commands = root.find("commands")
    if commands is None or [node.tag for node in commands] != ["readback"]:
        raise GuardError("Probe command must be readback only")
    physical = commands.find("./readback/physical-readback")
    if physical is None or physical.attrib != {"is-physical-readback":"false"}:
        raise GuardError("Probe must use logical addressing")
    items = commands.findall("./readback/readback-list/readback-rom-item")
    expected_attrs = {"readback-index":"0", "readback-enable":"true",
        "part-id":"8",
        "start-address":"0x1400000", "readback-length":"0x200",
        "readback-flag":"NUTL_READ_PAGE_ONLY", "addr-flag":"NUTL_ADDR_LOGICAL"}
    if len(items) != 1 or items[0].attrib != expected_attrs:
        raise GuardError("Probe readback range or mode changed")
    if (items[0].text or "") != str(Path(readback_output).resolve()):
        raise GuardError("Probe output path changed")
    expected_text = {"chip-name":"MT6582", "storage-type":"EMMC",
        "download-agent":str(Path(download_agent).resolve()),
        "scatter":str(Path(scatter).resolve()), "checksum-level":"usb"}
    for tag, value in expected_text.items():
        if root.findtext("./general/" + tag) != value:
            raise GuardError(f"Probe field changed: {tag}")
    conn = root.find("./general/connection")
    expected_conn = {"type":"BromUSB", "high-speed":"true", "power":"AutoDetect",
        "da_log_level":"Info", "da_log_channel":"UART", "timeout-count":"3600000", "com-port":""}
    if conn is None or conn.attrib != expected_conn:
        raise GuardError("Probe connection changed")
    log = root.find("./general/log-info")
    if log is None or log.attrib != {"log_on":"true", "log_path":str(Path(log_dir).resolve()), "clean_hours":"720"}:
        raise GuardError("Probe log path changed")


def audit_mbr_read_only_probe_xml(path: Path, download_agent: Path,
                                  scatter: Path, readback_output: Path,
                                  log_dir: Path) -> None:
    path = require_ordinary_file(path, "MBR read-only probe XML")
    audit_mbr_read_only_probe_xml_bytes(path.read_bytes(), download_agent,
                                        scatter, readback_output, log_dir)


def snapshot_inputs(app_dir: Path, candidate: Path, flash_tool: Path, da: Path,
                    xml: Path, plan: Path, validated_report: dict,
                    working_dir: Path | None = None) -> dict:
    """Create a launch snapshot only while every input still matches trust."""
    app_dir = Path(app_dir).resolve()
    working_dir = Path(working_dir or app_dir).resolve()
    if working_dir != app_dir or Path(xml).resolve().parent != app_dir or Path(plan).resolve().parent != app_dir:
        raise GuardError("Launch working, scatter, XML and plan directories must be identical")
    require_exact_launch_inventory(app_dir)
    candidate = validate_candidate_archive(candidate)
    if (Path(validated_report.get("app_dir", "")).resolve() != app_dir
            or validated_report.get("candidate_archive") != str(candidate)):
        raise GuardError("Validated report is no longer bound to this stage/candidate")
    expected = {
        Path(flash_tool): (TRUSTED_SIZES["flash_tool"], TRUSTED["flash_tool"]),
        Path(da): (TRUSTED_SIZES["da"], TRUSTED["da"]),
        app_dir/"storage_setting.xml": (TRUSTED_SIZES["storage_setting"], TRUSTED["storage_setting"]),
        app_dir/"MT6582_Android_scatter.txt": (TRUSTED_SIZES["scatter"], TRUSTED["scatter"]),
        app_dir/"UPDATE-MANIFEST.json": (TRUSTED_SIZES["manifest"], TRUSTED["manifest"]),
        app_dir/"SHA256SUMS.txt": (TRUSTED_SIZES["checksums"], TRUSTED["checksums"]),
    }
    for name in ("lk.bin", "boot.img", "recovery.img", "logo.bin", "system.img"):
        expected[app_dir/name] = (TRUSTED_SIZES[name], TRUSTED[name])
    identities = {}
    candidate_key = str(require_ordinary_file(candidate, "candidate archive").resolve())
    identities[candidate_key] = {"size": TRUSTED_SIZES["candidate"], "sha256": TRUSTED["candidate"]}
    for path, (size, digest) in expected.items():
        path = require_ordinary_file(path, "trusted launch input")
        actual_size, actual_hash = path.stat().st_size, sha256(path)
        if (actual_size, actual_hash) != (size, digest):
            raise GuardError(f"Trusted input changed between validation and snapshot: {path}")
        identities[str(path.resolve())] = {"size": actual_size, "sha256": actual_hash}
    # Read each generated control exactly once. The semantic audit and the
    # recorded identity are deliberately derived from these same bytes; a later
    # pathname read can never become the snapshot baseline.
    plan_path = require_ordinary_file(plan, "generated launch plan")
    xml_path = require_ordinary_file(xml, "download XML")
    try:
        plan_bytes = plan_path.read_bytes()
        xml_bytes = xml_path.read_bytes()
    except OSError as exc:
        raise GuardError(f"Generated launch control is unreadable: {exc}") from exc
    audit_plan_bytes(plan_bytes, validated_report)
    xml_root = parse_download_only_xml_bytes(xml_bytes)
    log = xml_root.find("./general/log-info")
    if log is None or not log.attrib.get("log_path"):
        raise GuardError("Download XML log path is missing")
    audit_download_only_xml_bytes(xml_bytes, validated_report, da, Path(log.attrib["log_path"]))
    identities[str(xml_path.resolve())] = {"size": len(xml_bytes), "sha256": hashlib.sha256(xml_bytes).hexdigest()}
    identities[str(plan_path.resolve())] = {"size": len(plan_bytes), "sha256": hashlib.sha256(plan_bytes).hexdigest()}
    return identities


def assert_snapshot(snapshot: dict) -> None:
    for name, identity in snapshot.items():
        path = Path(name)
        if (not require_ordinary_file(path, "snapshotted input")
                or path.stat().st_size != identity["size"] or sha256(path) != identity["sha256"]):
            raise GuardError(f"Validated input changed before launch: {name}")


class UpdateCompletionGate:
    """Prevents a download-only result from being reported as installation success."""
    def __init__(self):
        self.download_complete = False
        self.readback_verified = False

    def record_download(self, succeeded: bool) -> None:
        if not succeeded:
            raise GuardError("Download failed")
        self.download_complete = True

    def record_readback(self, succeeded: bool) -> None:
        if not self.download_complete or not succeeded:
            raise GuardError("Complete verified readback is required")
        self.readback_verified = True

    def installation_succeeded(self) -> bool:
        if not (self.download_complete and self.readback_verified):
            raise GuardError("Updater success is blocked until readback verification passes")
        return True


def parse_download_only_xml_bytes(data: bytes) -> ET.Element:
    try:
        text = data.decode("utf-8")
        return ET.fromstring(text)
    except (UnicodeError, ET.ParseError) as exc:
        raise GuardError(f"Active XML is unreadable: {exc}") from exc


def audit_download_only_xml_bytes(data: bytes, report: dict | None = None, download_agent: Path | None = None, log_dir: Path | None = None) -> None:
    try:
        text = data.decode("utf-8")
    except UnicodeError as exc:
        raise GuardError(f"Active XML is unreadable: {exc}") from exc
    lower = text.lower()
    for token in FORBIDDEN:
        if token in lower:
            raise GuardError(f"Forbidden token in active XML: {token}")
    root = parse_download_only_xml_bytes(data)
    commands = root.find("commands")
    if commands is None or [c.tag for c in commands] != ["download-only"] or commands.find("download-only/da-download-all") is None:
        raise GuardError("Active XML is not exactly Download Only")
    roms = root.findall("./general/rom-list/rom")
    actual = [(int(r.attrib.get("index", "-1")), r.text or "") for r in roms if r.attrib.get("enable") == "true"]
    if report is not None:
        expected = [(v[0], v[1]) for v in ALLOWED.values()]
    else:
        expected = [(v[0], v[1]) for v in ALLOWED.values()]
    if actual != expected:
        raise GuardError(f"Active XML ROM list differs: {actual}")
    if report is not None:
        scatter = root.findtext("./general/scatter")
        expected_scatter = ("MT6582_Android_scatter.txt" if download_agent is not None
                            and Path(download_agent).resolve().parent == Path(report["app_dir"]).resolve()
                            else str((Path(report["app_dir"]) / "MT6582_Android_scatter.txt").resolve()))
        if scatter != expected_scatter:
            raise GuardError("Active XML scatter was substituted")
    required = {
        "./general/chip-name": "MT6582", "./general/storage-type": "EMMC",
        "./general/checksum-level": "usb",
    }
    for xpath, value in required.items():
        if root.findtext(xpath) != value:
            raise GuardError(f"Active XML field changed: {xpath}")
    conn = root.find("./general/connection")
    expected_conn = {"type":"BromUSB","high-speed":"true","power":"AutoDetect","da_log_level":"Info","da_log_channel":"UART","timeout-count":"3600000","com-port":""}
    if conn is None or conn.attrib != expected_conn:
        raise GuardError("Active XML connection changed")
    if download_agent is not None:
        expected_da = (Path(download_agent).name if Path(download_agent).resolve().parent == Path(report["app_dir"]).resolve()
                       else str(Path(download_agent).resolve()))
        if root.findtext("./general/download-agent", "") != expected_da:
            raise GuardError("Active XML DA path changed")
    log = root.find("./general/log-info")
    production_cwd = (report is not None and download_agent is not None
                      and Path(download_agent).resolve().parent == Path(report["app_dir"]).resolve())
    expected_log = {"log_on":"true", "log_path":"SP_FT_Logs" if production_cwd else (str(Path(log_dir).resolve()) if log_dir is not None else log.attrib.get("log_path", "")), "clean_hours":"720"}
    if log is None or log.attrib != expected_log:
        raise GuardError("Active XML log settings changed")


def audit_download_only_xml(path: Path, report: dict | None = None, download_agent: Path | None = None, log_dir: Path | None = None) -> None:
    path = require_ordinary_file(path, "download XML")
    audit_download_only_xml_bytes(path.read_bytes(), report, download_agent, log_dir)


def audit_plan_bytes(data: bytes, report: dict) -> None:
    try:
        actual = json.loads(data.decode("utf-8"))
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise GuardError(f"Plan is unreadable: {exc}") from exc
    if actual != plan_document(report):
        raise GuardError("Plan differs from the trusted generated plan")


def audit_plan(path: Path, report: dict) -> None:
    path = require_ordinary_file(path, "generated launch plan")
    audit_plan_bytes(path.read_bytes(), report)


def audit_readback_xml(path: Path, report: dict, download_agent: Path, scatter: Path,
                       log_dir: Path, readback_dir: Path) -> None:
    root = ET.parse(path).getroot()
    if root.tag != "flashtool-config" or root.attrib != {"version": "2.0"}:
        raise GuardError("Readback XML root changed")
    expected_text = {
        "chip-name": "MT6582", "storage-type": "EMMC",
        "download-agent": str(Path(download_agent).resolve()),
        "scatter": str(Path(scatter).resolve()), "authentication": "",
        "certification": "", "checksum-level": "usb",
    }
    general = root.find("general")
    if general is None or [c.tag for c in general] != [
        "chip-name", "storage-type", "download-agent", "scatter",
        "authentication", "certification", "rom-list", "connection",
        "checksum-level", "log-info",
    ]:
        raise GuardError("Readback XML general section changed")
    for tag, expected in expected_text.items():
        if (general.findtext(tag) or "") != expected:
            raise GuardError(f"Readback XML field changed: {tag}")
    rom_list = general.find("rom-list")
    if rom_list is None or list(rom_list):
        raise GuardError("Readback XML ROM list must be empty")
    conn = general.find("connection")
    expected_conn = {"type":"BromUSB","high-speed":"true","power":"AutoDetect","da_log_level":"Info","da_log_channel":"UART","timeout-count":"3600000","com-port":""}
    if conn is None or conn.attrib != expected_conn:
        raise GuardError("Readback XML connection changed")
    log = general.find("log-info")
    expected_log = {"log_on":"true", "log_path":str(Path(log_dir).resolve()), "clean_hours":"720"}
    if log is None or log.attrib != expected_log:
        raise GuardError("Readback XML log settings changed")
    commands = root.find("commands")
    if commands is None or [c.tag for c in commands] != ["readback"]:
        raise GuardError("Readback XML command changed")
    readback = commands.find("readback")
    physical = readback.find("physical-readback") if readback is not None else None
    items_parent = readback.find("readback-list") if readback is not None else None
    if physical is None or physical.attrib != {"is-physical-readback":"false"} or items_parent is None:
        raise GuardError("Readback mode changed")
    items = list(items_parent)
    if len(items) != len(report["plan"]):
        raise GuardError("Readback item count changed")
    for index, (item, part) in enumerate(zip(items, report["plan"])):
        expected_attrib = {
            "readback-index": str(index), "readback-enable": "true",
            "part-id": "8",
            "start-address": f'0x{part["start"]:x}',
            "readback-length": f'0x{((part["write_size"] + 0x1ff) & ~0x1ff):x}',
            "readback-flag": "NUTL_READ_PAGE_ONLY",
            "addr-flag": "NUTL_ADDR_LOGICAL",
        }
        expected_output = (Path(readback_dir) / (part["name"] + ".img")).resolve()
        if item.tag != "readback-rom-item" or item.attrib != expected_attrib:
            raise GuardError(f"Readback geometry/flags changed: {part['name']}")
        if Path(item.text or "").resolve() != expected_output:
            raise GuardError(f"Readback output path changed: {part['name']}")
