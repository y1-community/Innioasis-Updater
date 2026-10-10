#!/usr/bin/env python3
"""Safety tests for model discovery and flash decisions. No Qt, no USB."""

import tempfile
import unittest
from pathlib import Path

import firmware_models as fm


ROOT = Path(__file__).resolve().parents[1]


def _scatter(chip, preloader, images):
    lines = [
        "- general: MTK_PLATFORM_CFG",
        "  info:",
        "    - config_version: V1.1.1",
        f"      platform: {chip}",
        "      project: test",
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


class FlashSafety(unittest.TestCase):
    def _payload(self, chip, preloader, extra_files=()):
        directory = Path(tempfile.mkdtemp())
        images = [("PRELOADER", preloader), ("UBOOT", "lk.bin")]
        (directory / f"{chip}_Android_scatter.txt").write_text(
            _scatter(chip, preloader, images), encoding="utf-8"
        )
        (directory / preloader).write_bytes(b"preloader-bytes")
        (directory / "lk.bin").write_bytes(b"lk")
        for name, data in extra_files:
            (directory / name).write_bytes(data)
        return directory

    def test_q5_generic_when_chip_preloader_and_name_agree(self):
        directory = self._payload("MT6580", "preloader_eastaeon80_wet_kk.bin")
        result = fm.assess_payload_dir(
            "Q5", directory, zip_name="rom_q5.zip", selected_model="Q5"
        )
        self.assertEqual(result.action, "generic")
        self.assertEqual(result.chip, "MT6580")
        self.assertEqual(result.preloader, "preloader_eastaeon80_wet_kk.bin")
        xml = fm.write_generic_spflash_xml(directory, "Q5")
        text = xml.read_text(encoding="utf-8")
        self.assertIn("<chip-name>MT6580</chip-name>", text)
        self.assertIn("preloader_eastaeon80_wet_kk.bin", text)
        self.assertNotIn("preloader_eastaeon82_wet_kk.bin", text)
        self.assertNotIn("preloader_g368_nyx.bin", text)

    def test_sr1_is_not_given_the_y2_preloader(self):
        directory = self._payload("MT6582", "preloader_j5052.bin")
        result = fm.assess_payload_dir(
            "SR1", directory, zip_name="rom_sr1.zip", selected_model="SR1"
        )
        self.assertEqual(result.action, "generic")
        self.assertEqual(result.preloader, "preloader_j5052.bin")

    def test_name_mismatch_refuses(self):
        directory = self._payload("MT6580", "preloader_eastaeon80_wet_kk.bin")
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
            "MT6580", "preloader_eastaeon80_wet_kk.bin",
            extra_files=(("boot-sign.img", b"sig"),),
        )
        result = fm.assess_payload_dir("Q5", signed, zip_name="rom_q5.zip", selected_model="Q5")
        self.assertEqual(result.action, "refuse")
        self.assertIn("signed_or_super", result.errors)

        super_dir = self._payload(
            "MT6580", "preloader_eastaeon80_wet_kk.bin",
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
            _scatter("MT6580", "preloader.bin", [("PRELOADER", "preloader.bin")]),
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
