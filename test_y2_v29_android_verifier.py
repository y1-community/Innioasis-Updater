#!/usr/bin/env python3
"""Regression tests for bounded ext4 bookkeeping after a Y2 write."""

from __future__ import annotations

import struct
import tempfile
import unittest
from pathlib import Path

from y2_update_only_guard import GuardError, verify_sparse_aware_android


ANDROID_SIZE = 0x33400000
BLOCK_SIZE = 4096
MUTABLE_CTIME_EXTRA_FIELDS = (0x57A84, 0x57B84, 0x61A84)


def build_sparse_fixture(root: Path, unexpected_offset: int | None = None) -> tuple[Path, Path]:
    """Create a tiny sparse input and a logically full-size sparse readback."""
    sparse = root / "system.img"
    readback = root / "ANDROID.img"
    first_raw_block = min(MUTABLE_CTIME_EXTRA_FIELDS) // BLOCK_SIZE
    last_raw_block = max(MUTABLE_CTIME_EXTRA_FIELDS) // BLOCK_SIZE
    raw_blocks = last_raw_block - first_raw_block + 1
    trailing_blocks = ANDROID_SIZE // BLOCK_SIZE - first_raw_block - raw_blocks
    header = struct.pack(
        "<I4H4I", 0xED26FF3A, 1, 0, 28, 12, BLOCK_SIZE,
        ANDROID_SIZE // BLOCK_SIZE, 3, 0,
    )
    chunks = (
        struct.pack("<2H2I", 0xCAC3, 0, first_raw_block, 12)
        + struct.pack("<2H2I", 0xCAC1, 0, raw_blocks, 12 + raw_blocks * BLOCK_SIZE)
        + bytes(raw_blocks * BLOCK_SIZE)
        + struct.pack("<2H2I", 0xCAC3, 0, trailing_blocks, 12)
    )
    sparse.write_bytes(header + chunks)

    with readback.open("wb") as output:
        output.truncate(ANDROID_SIZE)
        output.seek(1080)
        output.write(b"\x53\xef")
        for offset in MUTABLE_CTIME_EXTRA_FIELDS:
            output.seek(offset)
            output.write(bytes.fromhex("08f646a9"))
        if unexpected_offset is not None:
            output.seek(unexpected_offset)
            output.write(b"\x01")
    return sparse, readback


class AndroidVerifierTests(unittest.TestCase):
    def test_accepts_complete_known_ctime_extra_fields(self):
        with tempfile.TemporaryDirectory() as folder:
            sparse, readback = build_sparse_fixture(Path(folder))
            result = verify_sparse_aware_android(sparse, readback)
        expected = {
            offset + byte
            for offset in MUTABLE_CTIME_EXTRA_FIELDS
            for byte in range(4)
        }
        self.assertEqual(set(result["allowed_ext4_changed_offsets"]), expected)
        self.assertEqual(result["allowed_ext4_changed_byte_count"], 12)

    def test_rejects_adjacent_unapproved_change(self):
        with tempfile.TemporaryDirectory() as folder:
            sparse, readback = build_sparse_fixture(Path(folder), 0x57A88)
            with self.assertRaisesRegex(GuardError, "0x57a88"):
                verify_sparse_aware_android(sparse, readback)


if __name__ == "__main__":
    unittest.main()
