#!/usr/bin/env python3
"""Offline regression tests for the V26 Flash Tool completion handoff."""

from __future__ import annotations

import ast
import queue
import time
import unittest
from pathlib import Path
from types import SimpleNamespace

from y2_public_delivery_v19 import DeliveryBlocked, evaluate_write_completion


ROOT = Path(__file__).resolve().parent
MIRRORED_SOURCES = (
    ROOT / "firmware_downloader.py",
    ROOT / "updater.py",
    ROOT / "test.py",
)


class FakeProcess:
    def __init__(self, polls):
        self._polls = iter(polls)
        self._last = None
        self.terminate_calls = 0

    def poll(self):
        try:
            self._last = next(self._polls)
        except StopIteration:
            pass
        return self._last

    def terminate(self):
        self.terminate_calls += 1


class FakeOutputQueue:
    EMPTY = object()

    def __init__(self, values):
        self._values = iter(values)

    def get(self, timeout):
        del timeout
        try:
            value = next(self._values)
        except StopIteration as exc:
            raise queue.Empty from exc
        if value is self.EMPTY:
            raise queue.Empty
        return value


def method_node(
    source: Path, name: str, class_name: str = "SPFlashToolWorker"
) -> ast.FunctionDef:
    tree = ast.parse(source.read_text(encoding="utf-8-sig"))
    owner = next(
        node
        for node in ast.walk(tree)
        if isinstance(node, ast.ClassDef) and node.name == class_name
    )
    return next(
        node
        for node in owner.body
        if isinstance(node, ast.FunctionDef) and node.name == name
    )


def exact_loop_code(source: Path, method_name: str):
    """Compile the real worker loop only; never import or launch the updater."""
    method = method_node(source, method_name)
    loop = next(node for node in ast.walk(method) if isinstance(node, ast.While))
    if method_name == "_run_flash_tool_once":
        prefix = []
        for node in loop.body:
            if (
                isinstance(node, ast.Assign)
                and any(isinstance(target, ast.Name) and target.id == "line"
                        for target in node.targets)
            ):
                break
            prefix.append(node)
        loop = ast.While(test=loop.test, body=prefix, orelse=[])
    module = ast.fix_missing_locations(ast.Module(body=[loop], type_ignores=[]))
    return compile(module, str(source), "exec")


def run_write_loop(outputs, polls, monotonic=None):
    process = FakeProcess(polls)
    clock = monotonic or time.monotonic
    scope = {
        "self": SimpleNamespace(should_stop=False),
        "process": process,
        "process_start_time": clock(),
        "process_timeout": 1800,
        "silent_print": lambda _message: None,
        "output_queue": FakeOutputQueue(outputs),
        "queue": queue,
        "time": SimpleNamespace(monotonic=clock),
        "stdout_eof": False,
        "exit_observed_at": None,
        "stdout_drain_timeout": 5.0,
        "termination_reason": "",
        "forced_termination": False,
    }
    exec(exact_loop_code(MIRRORED_SOURCES[0], "_run_flash_tool_once"), scope)
    return process, scope


def run_read_loop(outputs, polls, monotonic=None):
    process = FakeProcess(polls)
    clock = monotonic or time.monotonic
    emitted = []
    scope = {
        "self": SimpleNamespace(
            should_stop=False,
            status_updated=SimpleNamespace(emit=emitted.append),
        ),
        "process": process,
        "deadline": float("inf"),
        "output_queue": FakeOutputQueue(outputs),
        "queue": queue,
        "time": SimpleNamespace(monotonic=clock),
        "stdout_eof": False,
        "exit_observed_at": None,
        "drain_timeout": 5.0,
        "lines": [],
        "saw_search": False,
        "connect_text": "connect",
    }
    exec(exact_loop_code(MIRRORED_SOURCES[0], "_run_y2_read_process"), scope)
    return process, scope, emitted


class CompletionLoopTests(unittest.TestCase):
    def test_three_entry_sources_remain_byte_identical(self):
        payloads = [source.read_bytes() for source in MIRRORED_SOURCES]
        self.assertEqual(payloads[0], payloads[1])
        self.assertEqual(payloads[0], payloads[2])

    def test_write_loop_handles_eof_before_process_exit(self):
        process, scope = run_write_loop(
            [None, FakeOutputQueue.EMPTY],
            [None, None, 0, 0],
        )
        self.assertTrue(scope["stdout_eof"])
        self.assertEqual(scope["termination_reason"], "")
        self.assertFalse(scope["forced_termination"])
        self.assertEqual(process.terminate_calls, 0)

    def test_write_loop_handles_process_exit_before_eof(self):
        process, scope = run_write_loop(
            [FakeOutputQueue.EMPTY, None],
            [0, 0, 0, 0],
        )
        self.assertTrue(scope["stdout_eof"])
        self.assertEqual(scope["termination_reason"], "")
        self.assertFalse(scope["forced_termination"])
        self.assertEqual(process.terminate_calls, 0)

    def test_write_loop_timeout_is_explicitly_forced(self):
        ticks = iter((0.0, 1801.0))
        process, scope = run_write_loop(
            [FakeOutputQueue.EMPTY],
            [None, None],
            monotonic=lambda: next(ticks),
        )
        self.assertTrue(scope["forced_termination"])
        self.assertIn("timed out", scope["termination_reason"])
        self.assertEqual(process.terminate_calls, 1)

    def test_read_loop_handles_eof_before_process_exit(self):
        process, scope, _ = run_read_loop(
            [None, FakeOutputQueue.EMPTY],
            [None, None, 0, 0],
        )
        self.assertTrue(scope["stdout_eof"])
        self.assertEqual(process.terminate_calls, 0)

    def test_read_loop_drains_search_line_when_process_exits_first(self):
        process, scope, emitted = run_read_loop(
            ["Search usb\n", None],
            [0, 0, 0, 0],
        )
        self.assertTrue(scope["stdout_eof"])
        self.assertTrue(scope["saw_search"])
        self.assertEqual(scope["lines"], ["Search usb\n"])
        self.assertEqual(emitted, ["connect"])
        self.assertEqual(process.terminate_calls, 0)

    def test_forced_or_nonzero_write_cannot_pass_completion_contract(self):
        transcript = "Search usb\n100% of image data has been sent\nDownload Succeeded\nDisconnect!\n"
        with self.assertRaises(DeliveryBlocked):
            evaluate_write_completion(transcript, 0, False)
        with self.assertRaises(DeliveryBlocked):
            evaluate_write_completion(transcript, 1, True)
        self.assertEqual(
            evaluate_write_completion(transcript, 0, True)["status"],
            "PASS-WRITE-COMPLETED",
        )

    def test_y2_success_is_emitted_only_after_mandatory_readback(self):
        source = MIRRORED_SOURCES[0].read_text(encoding="utf-8-sig")
        run_node = method_node(MIRRORED_SOURCES[0], "run")
        run_text = ast.get_source_segment(source, run_node)
        self.assertIsNotNone(run_text)
        readback = run_text.index("self._run_y2_post_write_readback()")
        verified_success = run_text.index(
            "Firmware installed and sparse-aware five-range readback verified"
        )
        self.assertLess(readback, verified_success)

        write_node = method_node(MIRRORED_SOURCES[0], "_run_flash_tool_once")
        write_text = ast.get_source_segment(source, write_node)
        self.assertIsNotNone(write_text)
        self.assertEqual(
            write_text.count(
                "The firmware write finished, but verification is still required."
            ),
            2,
        )
        self.assertIn('"stdout_eof":stdout_eof', write_text)
        self.assertIn('"forced_termination":forced_termination', write_text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
