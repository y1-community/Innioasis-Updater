#!/usr/bin/env python3
"""Offline regression tests for the V26 Flash Tool completion handoff."""

from __future__ import annotations

import ast
import datetime
import json
import os
import queue
import tempfile
import threading
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


class FakeSignal:
    def __init__(self, events=None, name=None):
        self.events = events
        self.name = name
        self.values = []

    def emit(self, *values):
        self.values.append(values)
        if self.events is not None:
            self.events.append((self.name, *values))


class FakeFlashProcess:
    def __init__(self, lines, exit_code=0):
        self.pid = 4242
        self._lines = list(lines)
        self._planned_exit = exit_code
        self._exit_code = None
        self.terminate_calls = 0
        self.kill_calls = 0
        self.stdout = self

    def __iter__(self):
        for line in self._lines:
            yield line
        self._exit_code = self._planned_exit

    def poll(self):
        return self._exit_code

    def wait(self, timeout=None):
        del timeout
        if self._exit_code is None:
            self._exit_code = self._planned_exit
        return self._exit_code

    def terminate(self):
        self.terminate_calls += 1
        self._exit_code = -15

    def kill(self):
        self.kill_calls += 1
        self._exit_code = -9


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


def production_method(name: str, globals_: dict):
    node = method_node(MIRRORED_SOURCES[0], name)
    module = ast.fix_missing_locations(ast.Module(body=[node], type_ignores=[]))
    scope = dict(globals_)
    exec(compile(module, str(MIRRORED_SOURCES[0]), "exec"), scope)
    return scope[name]


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
        "connect_prompt_emitted": False,
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

    def test_read_loop_suppresses_prompt_when_process_exits_first(self):
        process, scope, emitted = run_read_loop(
            ["Search usb\n", None],
            [0, 0, 0, 0],
        )
        self.assertTrue(scope["stdout_eof"])
        self.assertTrue(scope["saw_search"])
        self.assertEqual(scope["lines"], ["Search usb\n"])
        self.assertFalse(scope["connect_prompt_emitted"])
        self.assertEqual(emitted, [])
        self.assertEqual(process.terminate_calls, 0)

    def test_read_loop_prompts_only_while_process_is_live(self):
        process, scope, emitted = run_read_loop(
            ["Search usb\n", None],
            [None, None, 0, 0],
        )
        self.assertTrue(scope["connect_prompt_emitted"])
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

    def _run_orchestration(self, *, readback_error=None, write_result=None):
        events = []
        completed = FakeSignal(events, "completed")
        enabled = FakeSignal(events, "enabled")
        worker = SimpleNamespace(
            device_model="Y2",
            device_label="Innioasis Y2",
            should_stop=False,
            spflash_completed=completed,
            enable_update_button=enabled,
            status_updated=FakeSignal(events, "status"),
            show_please_wait_image=FakeSignal(),
            show_try_again_dialog=FakeSignal(),
        )
        worker._run_y2_prewrite_identity_probe = lambda: events.append(("prewrite",))

        attempts = []
        def write_once(attempt, maximum):
            attempts.append((attempt, maximum))
            events.append(("write",))
            if isinstance(write_result, Exception):
                raise write_result
            return write_result or {"ok": True, "completed": True}
        worker._run_flash_tool_once = write_once
        worker._sync_device_label = lambda: events.append(("sync",))
        def readback():
            events.append(("readback",))
            if readback_error:
                raise readback_error
            return {"status": "PASS"}
        worker._run_y2_post_write_readback = readback

        run = production_method("run", {
            "is_y2_model": lambda _model: True,
            "is_y1_model": lambda _model: False,
            "is_linux_platform": lambda: False,
            "is_windows_platform": lambda: True,
            "stop_install_competitor_processes": lambda **_kw: 0,
            "silent_print": lambda *_values: None,
            "time": time,
            "LINUX_FLASH_SELF_HEAL_MAX_ATTEMPTS": 3,
        })
        run(worker)
        return events, attempts, completed

    def test_complete_run_enters_readback_before_success(self):
        events, attempts, completed = self._run_orchestration()
        names = [event[0] for event in events]
        self.assertEqual(attempts, [(1, 1)])
        self.assertLess(names.index("write"), names.index("readback"))
        success_index = next(
            i for i, event in enumerate(events)
            if event[0] == "completed" and event[1] is True
        )
        self.assertLess(names.index("readback"), success_index)
        self.assertEqual(completed.values[-1][0], True)

    def test_readback_rejection_blocks_success_and_retry(self):
        events, attempts, completed = self._run_orchestration(
            readback_error=RuntimeError("sparse verification mismatch")
        )
        self.assertEqual(attempts, [(1, 1)])
        self.assertFalse(any(values[0] is True for values in completed.values))
        self.assertEqual(completed.values[-1][0], False)
        self.assertIn("failed closed", completed.values[-1][1])

    def test_write_exception_blocks_readback_success_and_retry(self):
        events, attempts, completed = self._run_orchestration(
            write_result=OSError("completion evidence write failed")
        )
        self.assertEqual(attempts, [(1, 1)])
        self.assertNotIn("readback", [event[0] for event in events])
        self.assertFalse(any(values[0] is True for values in completed.values))

    def test_failed_write_result_is_not_retried_for_y2(self):
        events, attempts, completed = self._run_orchestration(
            write_result={
                "ok": False,
                "completed": False,
                "reached_search_usb": True,
                "com_port_open_fail": False,
                "message": "cancelled or timed out",
            }
        )
        self.assertEqual(attempts, [(1, 1)])
        self.assertNotIn("readback", [event[0] for event in events])
        self.assertFalse(any(values[0] is True for values in completed.values))

    def test_physical_disconnect_requires_positive_acknowledgement(self):
        method = production_method("_require_y2_physical_disconnect", {
            "threading": threading,
            "time": time,
            "RuntimeError": RuntimeError,
        })
        def signal(accepted):
            class Confirm:
                @staticmethod
                def emit(_purpose, token):
                    token["accepted"] = accepted
                    token["event"].set()
            return Confirm()
        accepted_worker = SimpleNamespace(
            should_stop=False,
            request_y2_physical_disconnect=signal(True),
        )
        method(accepted_worker, "test checkpoint", timeout=1)
        refused_worker = SimpleNamespace(
            should_stop=False,
            request_y2_physical_disconnect=signal(False),
        )
        with self.assertRaisesRegex(RuntimeError, "cancelled"):
            method(refused_worker, "test checkpoint", timeout=1)

    def test_source_contains_two_separate_disconnect_checkpoints(self):
        source = MIRRORED_SOURCES[0].read_text(encoding="utf-8-sig")
        self.assertEqual(
            source.count("self._require_y2_physical_disconnect("),
            2,
        )
        self.assertNotIn("Y2 disconnect confirmed", source)

    def test_complete_write_worker_creates_positive_completion_evidence(self):
        transcript = [
            "Search usb\n",
            "Downloading\n",
            "100% of image data has been sent\n",
            "Download Succeeded\n",
            "Disconnect!\n",
        ]
        process = FakeFlashProcess(transcript)
        with tempfile.TemporaryDirectory(prefix="v27-full-worker-") as td:
            app_dir = Path(td)
            worker = SimpleNamespace(
                should_stop=False,
                device_model="Y2",
                device_label="Innioasis Y2",
                app_dir=app_dir,
                spflash_working_dir=app_dir,
                spflash_command=["fake-flash-tool"],
                requested_com_port=None,
                y2_launch_snapshot=object(),
                _build_runtime_command=lambda: (["fake-flash-tool"], None, []),
                status_updated=FakeSignal(),
                show_please_wait_image=FakeSignal(),
                show_initsteps_image=FakeSignal(),
                show_installing_image=FakeSignal(),
                show_installed_image=FakeSignal(),
                disable_update_button=FakeSignal(),
            )
            method = production_method("_run_flash_tool_once", {
                "is_linux_platform": lambda: False,
                "is_y2_model": lambda _model: True,
                "assert_y2_snapshot": lambda _snapshot: None,
                "subprocess": SimpleNamespace(
                    PIPE=object(), STDOUT=object(), Popen=lambda *_a, **_kw: process
                ),
                "threading": threading,
                "queue": queue,
                "time": time,
                "datetime": datetime.datetime,
                "json": json,
                "os": os,
                "silent_print": lambda *_values: None,
                "sp_flash_tool_process_env": lambda _app: {},
                "spflash_connect_status_text": lambda *_a, **_kw: "connect",
                "spflash_success_status_text": lambda *_a, **_kw: "success",
                "describe_mediatek_ports": lambda _ports: "none",
                "stop_sp_flash_tool_processes": lambda **_kw: 0,
                "evaluate_y2_write_completion": evaluate_write_completion,
                "FLASH_TOOL_LINUX_LOG_DIR_NAME": "SP_FT_Logs",
            })
            result = method(worker, 1, 1)
            evidence_path = app_dir / "Y2-write-completion.json"
            self.assertTrue(result["ok"])
            self.assertTrue(evidence_path.is_file())
            evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
            self.assertEqual(evidence["status"], "PASS-WRITE-COMPLETED")
            self.assertEqual(evidence["exit_code"], 0)
            self.assertTrue(evidence["natural_completion"])
            self.assertTrue(evidence["stdout_eof"])
            self.assertFalse(evidence["forced_termination"])
            self.assertFalse(evidence["retry_performed"])

    def test_complete_write_worker_evidence_failure_propagates(self):
        process = FakeFlashProcess([
            "Search usb\n",
            "Downloading\n",
            "100% of image data has been sent\n",
            "Download Succeeded\n",
            "Disconnect!\n",
        ])
        with tempfile.TemporaryDirectory(prefix="v27-evidence-fail-") as td:
            missing_app_dir = Path(td) / "missing"
            working_dir = Path(td)
            worker = SimpleNamespace(
                should_stop=False,
                device_model="Y2",
                device_label="Innioasis Y2",
                app_dir=missing_app_dir,
                spflash_working_dir=working_dir,
                spflash_command=["fake-flash-tool"],
                requested_com_port=None,
                y2_launch_snapshot=object(),
                _build_runtime_command=lambda: (["fake-flash-tool"], None, []),
                status_updated=FakeSignal(),
                show_please_wait_image=FakeSignal(),
                show_initsteps_image=FakeSignal(),
                show_installing_image=FakeSignal(),
                show_installed_image=FakeSignal(),
                disable_update_button=FakeSignal(),
            )
            method = production_method("_run_flash_tool_once", {
                "is_linux_platform": lambda: False,
                "is_y2_model": lambda _model: True,
                "assert_y2_snapshot": lambda _snapshot: None,
                "subprocess": SimpleNamespace(
                    PIPE=object(), STDOUT=object(), Popen=lambda *_a, **_kw: process
                ),
                "threading": threading,
                "queue": queue,
                "time": time,
                "datetime": datetime.datetime,
                "json": json,
                "os": os,
                "silent_print": lambda *_values: None,
                "sp_flash_tool_process_env": lambda _app: {},
                "spflash_connect_status_text": lambda *_a, **_kw: "connect",
                "spflash_success_status_text": lambda *_a, **_kw: "success",
                "describe_mediatek_ports": lambda _ports: "none",
                "stop_sp_flash_tool_processes": lambda **_kw: 0,
                "evaluate_y2_write_completion": evaluate_write_completion,
                "FLASH_TOOL_LINUX_LOG_DIR_NAME": "SP_FT_Logs",
            })
            with self.assertRaises(FileNotFoundError):
                method(worker, 1, 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
