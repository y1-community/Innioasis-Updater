#!/usr/bin/env python3
"""Onboarding script tests. They use a fake gh client and never touch GitHub."""

import base64
import json
import tempfile
import unittest
import zipfile
from pathlib import Path

import firmware_models as fm

# scripts/, not tools/: the repo already has mtkclient's Tools/ directory,
# and those two names collide on a case-insensitive checkout.
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import onboard_stock_firmware as onboard


class Result:
    def __init__(self, code, out="", err=""):
        self.returncode = code
        self.stdout = out
        self.stderr = err


class FakeGh:
    def __init__(self):
        self.calls = []
        self.repos = set()
        self.files = {}
        self.releases = {}

    def run(self, args, check=True, input_text=None):
        self.calls.append(list(args))
        if args[:2] == ["repo", "view"]:
            repo = args[2]
            if repo in self.repos:
                return Result(0, '{"name":"ok"}')
            return Result(1, "", "not found") if not check else None
        if args[:2] == ["repo", "create"]:
            self.repos.add(args[2])
            return Result(0)
        if args[:2] == ["api", "--method"]:
            path = args[3]
            payload = json.loads(input_text)
            self.files[path] = base64.b64decode(payload["content"]).decode("utf-8")
            return Result(0)
        if args[0] == "api":
            path = args[1]
            if path not in self.files:
                return Result(1, "", "404")
            content = base64.b64encode(self.files[path].encode("utf-8")).decode("ascii")
            return Result(0, json.dumps({"content": content, "sha": "abc"}))
        if args[:2] == ["release", "view"]:
            repo = args[args.index("--repo") + 1]
            key = (repo, args[2])
            if key not in self.releases:
                return Result(1, "", "missing")
            assets = [{"name": name, "size": size} for name, size in self.releases[key].items()]
            return Result(0, json.dumps({"assets": assets}))
        if args[:2] == ["release", "create"]:
            repo = args[args.index("--repo") + 1]
            self.releases[(repo, args[2])] = {}
            return Result(0)
        if args[:2] == ["release", "upload"]:
            repo = args[args.index("--repo") + 1]
            tag = args[2]
            bucket = self.releases.setdefault((repo, tag), {})
            for arg in args[3:]:
                if arg.startswith("--"):
                    continue
                path = Path(arg)
                if path.is_file():
                    bucket[path.name] = path.stat().st_size
            return Result(0)
        if check:
            raise AssertionError(f"unexpected gh {' '.join(args)}")
        return Result(1, "", "unexpected")


def _source_zip(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(path, "w") as archive:
        archive.writestr("MX2/MT6580_Android_scatter.txt", "platform: MT6582\n")
        archive.writestr("MX2/preloader_eastaeon80_wet_kk.bin", b"pre")
        archive.writestr("MX2/lk.bin", b"lk")
        archive.writestr("MX2/pad.bin", b"A" * 8000)
        archive.writestr("__MACOSX/._junk", b"junk")
        archive.writestr(".DS_Store", b"store")


class RepackAndManifest(unittest.TestCase):
    def test_repack_flattens_strips_junk_and_uses_max_deflate(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            source = tmp / "vendor.zip"
            _source_zip(source)
            dest = tmp / "rom_q5.zip"
            onboard.repack_firmware(source, dest)
            with zipfile.ZipFile(dest) as archive:
                names = set(archive.namelist())
                self.assertIn("MT6580_Android_scatter.txt", names)
                self.assertIn("preloader_eastaeon80_wet_kk.bin", names)
                self.assertIn("pad.bin", names)
                self.assertFalse(any(name.startswith("__MACOSX") or name.endswith(".DS_Store") for name in names))
                self.assertFalse(any("/" in name for name in names))
                pad = archive.getinfo("pad.bin")
                self.assertEqual(pad.compress_type, zipfile.ZIP_DEFLATED)
                self.assertEqual(pad.extra, b"")
                self.assertLess(pad.compress_size, pad.file_size)
            self.assertLess(dest.stat().st_size, fm.GITHUB_MAX_ASSET_BYTES)

    def test_github_limit_rejects_an_oversized_asset(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "rom_g5.zip"
            path.write_bytes(b"too-big")
            original = fm.GITHUB_MAX_ASSET_BYTES
            fm.GITHUB_MAX_ASSET_BYTES = 4
            try:
                with self.assertRaises(onboard.OnboardError):
                    onboard.assert_under_github_limit(path)
            finally:
                fm.GITHUB_MAX_ASSET_BYTES = original

    def test_manifest_upsert_is_idempotent_and_keeps_other_lines(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = Path(tmp) / "slidia_manifest.xml"
            manifest.write_text(
                '<?xml version="1.0"?>\n<slidia>\n'
                '  <package name="Original Software" repo="y1-community/y1-stock-rom" '
                'device="Y1" url="https://github.com/y1-community/y1-stock-rom" '
                'type="img" handler="Custom Firmware" />\n'
                '  <package name="Linux for Y1 (Dev)" repo="y1-community/y1-ata-rom" '
                'device="Y1" url="https://github.com/y1-community/y1-linux-rom" '
                'type="img" handler="Custom Firmware" />\n'
                "</slidia>\n",
                encoding="utf-8",
            )
            self.assertEqual(onboard.upsert_manifest(manifest, "Q5"), "added")
            text = manifest.read_text(encoding="utf-8")
            self.assertIn('device="Y1"', text)
            self.assertIn("y1-linux-rom", text)
            self.assertEqual(text.count('device="Q5"'), 1)
            self.assertEqual(onboard.upsert_manifest(manifest, "Q5"), "unchanged")
            self.assertEqual(manifest.read_text(encoding="utf-8").count('device="Q5"'), 1)


class ApplyIsIdempotent(unittest.TestCase):
    def _args(self, tmp, manifest):
        source = Path(tmp) / "in.zip"
        _source_zip(source)
        image = Path(tmp) / "updater.jpg"
        image.write_bytes(b"jpg")
        return [
            "--model", "Q5",
            "--tag", "3.27-en",
            "--title", "System Software 3.27 for Timmkoo Q5",
            "--notes", "English build.",
            "--source", str(source),
            "--image", str(image),
            "--manifest", str(manifest),
            "--output", str(Path(tmp) / "rom_q5.zip"),
            "--org", "y1-community",
        ]

    def test_dry_run_does_not_call_gh_or_edit_the_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = Path(tmp) / "slidia_manifest.xml"
            manifest.write_text("<slidia>\n</slidia>\n", encoding="utf-8")
            before = manifest.read_text(encoding="utf-8")
            gh = FakeGh()
            report = onboard.run(self._args(tmp, manifest), gh=gh)
            self.assertFalse(report["apply"])
            self.assertEqual(report["manifest"], "not-written")
            self.assertEqual(gh.calls, [])
            self.assertEqual(manifest.read_text(encoding="utf-8"), before)
            self.assertTrue(Path(report["zip"]).is_file())

    def test_apply_twice_does_not_duplicate_the_release_or_manifest(self):
        with tempfile.TemporaryDirectory() as tmp:
            manifest = Path(tmp) / "slidia_manifest.xml"
            manifest.write_text("<slidia>\n</slidia>\n", encoding="utf-8")
            gh = FakeGh()
            first = onboard.run(self._args(tmp, manifest) + ["--apply"], gh=gh)
            second = onboard.run(self._args(tmp, manifest) + ["--apply"], gh=gh)
            self.assertIn("created", first["steps"])
            self.assertIn("manifest:added", first["steps"])
            self.assertIn("exists", second["steps"])
            self.assertIn("manifest:unchanged", second["steps"])
            self.assertEqual(manifest.read_text(encoding="utf-8").count('device="Q5"'), 1)
            creates = [call for call in gh.calls if call[:2] == ["release", "create"]]
            self.assertEqual(len(creates), 1)
            self.assertIn("y1-community/q5-stock-rom", gh.repos)


if __name__ == "__main__":
    unittest.main()
