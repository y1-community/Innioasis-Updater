#!/usr/bin/env python3
"""Safety tests for model discovery and flash decisions. No Qt, no USB."""

import tempfile
import unittest
from pathlib import Path

import firmware_models as fm


ROOT = Path(__file__).resolve().parents[1]


def _scatter(chip, preloader, images, project="test"):
    lines = [
        "- general: MTK_PLATFORM_CFG",
        "  info:",
        "    - config_version: V1.1.1",
        f"      platform: {chip}",
        f"      project: {project}",
        "      storage: EMMC",
        "",
    ]
    for index, (name, filename) in enumerate(images):
        lines.extend(
            [
                f"- partition_index: SYS{index}",
                f"  partition_name: {name}",
                f"  file_name: {filename}",
                "  is_download: true",
                "  linear_start_addr: 0x0",
                "  physical_start_addr: 0x0",
                "  partition_size: 0x1000",
                "  region: EMMC_USER",
                "",
            ]
        )
    return "\n".join(lines)


class ModelNames(unittest.TestCase):
    def test_explicit_rom_names_do_not_collapse_into_y1_y2_a5(self):
        self.assertEqual(fm.model_from_zip_name("rom_q5.zip"), "Q5")
        self.assertEqual(fm.model_from_zip_name("https://example/rom_g5.zip"), "G5")
        self.assertEqual(fm.model_from_zip_name("rom_sr1.zip"), "SR1")
        self.assertEqual(fm.model_from_zip_name("rom_r1.zip"), "R1")
        self.assertEqual(fm.model_from_zip_name("rom_g1.zip"), "G1")
        self.assertIsNone(fm.model_from_zip_name("rom.zip"))
        self.assertIsNone(fm.model_from_zip_name("rom_type_b.zip"))
        self.assertIsNone(fm.model_from_zip_name("rom_240p.zip"))
        self.assertEqual(fm.model_from_zip_name("rom_y2.zip"), "Y2")
        self.assertEqual(fm.model_from_zip_name("rom_a5.zip"), "A5")

    def test_classify_keeps_legacy_y1_and_y2_assets(self):
        self.assertEqual(fm.classify_rom_asset("rom.zip"), "dual")
        self.assertEqual(fm.classify_rom_asset("rom_y2.zip"), "Y2")
        self.assertEqual(fm.classify_rom_asset("rom_q5.zip"), "Q5")
        self.assertNotEqual(fm.classify_rom_asset("rom_g5.zip"), "A5")
        self.assertNotEqual(fm.classify_rom_asset("rom_sr1.zip"), "Y2")
        self.assertNotEqual(fm.classify_rom_asset("rom_r1.zip"), "Y1")

    def test_variant_filter_never_offers_another_models_zip(self):
        repo = "y1-community/y1-stock-rom"
        self.assertTrue(fm.variant_matches("dual", "Y1", "Y1", repo))
        self.assertTrue(fm.variant_matches("Y2", "Y2", "Y2", repo))
        self.assertFalse(fm.variant_matches("dual", "Y2", "Y2", repo))
        self.assertFalse(fm.variant_matches("Q5", "Y1", "Y1", repo))
        self.assertFalse(fm.variant_matches("Y2", "Q5", "Q5", "y1-community/q5-stock-rom"))
        self.assertTrue(fm.variant_matches("Q5", "Q5", "Q5", "y1-community/q5-stock-rom"))
        self.assertFalse(fm.variant_matches("dual", "Q5", "Q5", "y1-community/q5-stock-rom"))
        self.assertFalse(fm.variant_matches("G5", "G1", "G1", "y1-community/g1-stock-rom"))

    def test_default_model_stays_y1_when_more_devices_exist(self):
        self.assertEqual(fm.preferred_default_model(["G1", "Q5", "Y1", "Y2"]), "Y1")
        self.assertEqual(fm.preferred_default_model(["G5", "Q3"]), "G5")

    def test_regional_tags_stay_distinguishable(self):
        self.assertEqual(fm.stock_release_variant("3.27-en"), ("3.27", "English"))
        self.assertEqual(fm.stock_release_variant("3.28-de"), ("3.28", "German"))
        self.assertEqual(fm.stock_release_variant("5.02-es"), ("5.02", "Spanish"))
        self.assertEqual(fm.stock_release_variant("3.03-multi"), ("3.03", "Multi-language"))
        self.assertEqual(fm.stock_release_variant("5.01-en-wm"), ("5.01", "English · WM"))
        self.assertEqual(fm.stock_release_variant("6.01-en-wm"), ("6.01", "English · WM"))
        self.assertEqual(fm.stock_release_variant("1.11"), ("1.11", ""))
        self.assertEqual(fm.stock_release_variant("1.48"), ("1.48", ""))
        self.assertEqual(fm.stock_release_variant("2.05"), ("2.05", ""))
        self.assertIsNone(fm.stock_release_variant("Stable-v0.3-ipod-theme-compatible"))
        self.assertIn("S2", fm.release_variant_warning("G1", "5.01-en-wm"))
        self.assertIn("S4", fm.release_variant_warning("G3", "6.01-en-wm"))
        self.assertEqual(fm.release_variant_warning("G1", "3.03-multi"), "")
        self.assertEqual(fm.release_variant_warning("Q5", "3.27-en"), "")
        self.assertLess(fm.G5_PUBLISHED_ZIP_BYTES, fm.GITHUB_MAX_ASSET_BYTES)


class FlashSafety(unittest.TestCase):
    def _payload(self, chip, preloader, extra_files=(), scatter_name=None, project="test"):
        directory = Path(tempfile.mkdtemp())
        images = [("PRELOADER", preloader), ("UBOOT", "lk.bin")]
        (directory / (scatter_name or f"{chip}_Android_scatter.txt")).write_text(
            _scatter(chip, preloader, images, project=project), encoding="utf-8"
        )
        (directory / preloader).write_bytes(b"preloader-bytes")
        (directory / "lk.bin").write_bytes(b"lk")
        for name, data in extra_files:
            (directory / name).write_bytes(data)
        return directory

    def test_q5_uses_mt6582_platform_even_when_the_filename_says_mt6580(self):
        directory = self._payload(
            "MT6582",
            "preloader_eastaeon80_wet_kk.bin",
            scatter_name="MT6580_Android_scatter.txt",
        )
        result = fm.assess_payload_dir(
            "Q5", directory, zip_name="rom_q5.zip", selected_model="Q5"
        )
        self.assertEqual(result.action, "generic")
        self.assertEqual(result.chip, "MT6582")
        self.assertEqual(result.scatter_name, "MT6580_Android_scatter.txt")
        self.assertEqual(result.preloader, "preloader_eastaeon80_wet_kk.bin")
        self.assertIn("not the Y2 partition layout", result.message)
        xml = fm.write_generic_spflash_xml(directory, "Q5")
        text = xml.read_text(encoding="utf-8")
        self.assertIn("<chip-name>MT6582</chip-name>", text)
        self.assertIn("MT6580_Android_scatter.txt", text)
        self.assertIn("preloader_eastaeon80_wet_kk.bin", text)
        self.assertNotIn("preloader_eastaeon82_wet_kk.bin", text)
        self.assertNotIn("preloader_g368_nyx.bin", text)

    def test_q3_accepts_q3e_identity_and_q5_refuses_it(self):
        q3 = self._payload(
            "MT6582",
            "preloader_eastaeon80_wet_kk.bin",
            scatter_name="MT6580_Android_scatter.txt",
            project="Q3E",
        )
        result = fm.assess_payload_dir("Q3", q3, zip_name="rom_q3.zip", selected_model="Q3")
        self.assertEqual(result.action, "generic")
        self.assertIn("Q3E", result.message)
        q5 = self._payload(
            "MT6582",
            "preloader_eastaeon80_wet_kk.bin",
            scatter_name="MT6580_Android_scatter.txt",
            project="Q3E",
        )
        refused = fm.assess_payload_dir("Q5", q5, zip_name="rom_q5.zip", selected_model="Q5")
        self.assertEqual(refused.action, "refuse")
        self.assertIn("model_mismatch", refused.errors)

    def test_sr1_is_not_given_the_y2_preloader(self):
        directory = self._payload("MT6582", "preloader_j5052.bin")
        result = fm.assess_payload_dir(
            "SR1", directory, zip_name="rom_sr1.zip", selected_model="SR1"
        )
        self.assertEqual(result.action, "generic")
        self.assertEqual(result.preloader, "preloader_j5052.bin")

    def test_name_mismatch_refuses(self):
        directory = self._payload(
            "MT6582", "preloader_eastaeon80_wet_kk.bin",
            scatter_name="MT6580_Android_scatter.txt",
        )
        result = fm.assess_payload_dir(
            "Q5", directory, zip_name="rom_q3.zip", selected_model="Q5"
        )
        self.assertEqual(result.action, "refuse")
        self.assertIn("model_mismatch", result.errors)

    def test_chip_mismatch_refuses(self):
        directory = self._payload("MT6753", "preloader_k53v1_64_bsp.bin")
        result = fm.assess_payload_dir(
            "Q5", directory, zip_name="rom_q5.zip", selected_model="Q5"
        )
        self.assertEqual(result.action, "refuse")
        self.assertIn("chip_mismatch", result.errors)

    def test_signed_and_super_images_refuse(self):
        signed = self._payload(
            "MT6582", "preloader_eastaeon80_wet_kk.bin",
            scatter_name="MT6580_Android_scatter.txt",
            extra_files=(("boot-sign.img", b"sig"),),
        )
        result = fm.assess_payload_dir("Q5", signed, zip_name="rom_q5.zip", selected_model="Q5")
        self.assertEqual(result.action, "refuse")
        self.assertIn("signed_or_super", result.errors)

        super_dir = self._payload(
            "MT6582", "preloader_eastaeon80_wet_kk.bin",
            scatter_name="MT6580_Android_scatter.txt",
            extra_files=(("super.img", b"super"),),
        )
        result = fm.assess_payload_dir("Q3", super_dir, zip_name="rom_q3.zip", selected_model="Q3")
        self.assertEqual(result.action, "refuse")

    def test_download_only_models_never_flash(self):
        for model in ("G1", "G3", "G5", "A5"):
            result = fm.assess_named_package(model, zip_name=f"rom_{model.lower()}.zip")
            self.assertEqual(result.action, "download_only", model)
            self.assertIn("not supported yet", result.message)

    def test_nested_scatter_is_refused(self):
        directory = Path(tempfile.mkdtemp())
        inner = directory / "MX2"
        inner.mkdir()
        (inner / "MT6580_Android_scatter.txt").write_text(
            _scatter("MT6582", "preloader.bin", [("PRELOADER", "preloader.bin")]),
            encoding="utf-8",
        )
        result = fm.assess_payload_dir("Q5", directory, zip_name="rom_q5.zip", selected_model="Q5")
        self.assertEqual(result.action, "refuse")
        self.assertIn("scatter_missing", result.errors)

    def test_manifest_lists_new_stock_models_without_dropping_y1_y2(self):
        text = (ROOT / "slidia_manifest.xml").read_text(encoding="utf-8")
        devices = fm.devices_in_manifest(text)
        for model in ("Y1", "Y2", *fm.STOCK_MANIFEST_MODELS):
            self.assertIn(model, devices)
        self.assertIn('repo="y1-community/y1-ata-rom"', text)
        self.assertIn('url="https://github.com/y1-community/y1-linux-rom"', text)


if __name__ == "__main__":
    unittest.main()
