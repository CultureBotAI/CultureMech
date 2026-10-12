"""Test diagnostics stay bounded; parallel timing and coverage stay complete."""

import importlib.util
import os
import subprocess
import sys
from pathlib import Path
from types import SimpleNamespace

import coverage
import pytest

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "tests/conftest.py"
RECEIPT = "culturemech_call_durations"


@pytest.fixture
def guard():
    spec = importlib.util.spec_from_file_location("isolated_budget", CONTRACT)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("char,count", [("x", 4096), ("\u00e9", 2048)])
def test_collection_accepts_ids_at_the_byte_limit(guard, char, count):
    markers = []
    item = SimpleNamespace(
        nodeid=char * count,
        path=Path(__file__),
        get_closest_marker=lambda name: None,
        fixturenames=(),
        add_marker=markers.append,
    )
    guard.pytest_collection_modifyitems([item])
    assert len(markers) == 1


@pytest.mark.parametrize("char,count", [("x", 4097), ("\u00e9", 2049)])
def test_collection_rejects_long_ids_without_echoing_them(guard, char, count):
    item = SimpleNamespace(nodeid=char * count, path=Path("oversized.py"))
    with pytest.raises(pytest.UsageError, match="exceeds 4096 UTF-8 bytes") as error:
        guard.pytest_collection_modifyitems([item])
    assert len(str(error.value)) < 200
    assert char * 100 not in str(error.value)


@pytest.mark.parametrize("compact", [False, True])
def test_real_collection_requires_compact_ids_but_keeps_large_payloads(tmp_path, compact):
    (tmp_path / "pytest.ini").write_text("[pytest]\nmarkers =\n    fast: isolated\n")
    (tmp_path / "conftest.py").write_text(CONTRACT.read_text())
    payload = 'pytest.param(b"x" * 5000, id="oversized-payload")' if compact else 'b"x" * 5000'
    (tmp_path / "test_payload.py").write_text(
        f'import pytest\n@pytest.mark.parametrize("payload", [{payload}])\n'
        "def test_payload(payload):\n    assert len(payload) == 5000\n"
    )
    env = {
        key: value
        for key, value in os.environ.items()
        if not key.startswith(("PYTEST_", "COV_CORE_", "COVERAGE_")) and key != "PYTHONPATH"
    }
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "-q", "--no-cov"],
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True,
        timeout=60,
    )
    output = result.stdout + result.stderr
    assert result.returncode == (0 if compact else 4)
    assert ("1 passed" if compact else "Test ID exceeds 4096 UTF-8 bytes") in output
    assert len(output) < 4096


def session(*, parallel=False, worker=False):
    config = SimpleNamespace(
        option=SimpleNamespace(numprocesses=2 if parallel else 0),
        pluginmanager=SimpleNamespace(hasplugin=lambda name: name == "xdist" and parallel),
    )
    if worker:
        config.workerinput = {}
        config.workeroutput = {}
    return SimpleNamespace(config=config, exitstatus=0)


def node(worker, receipt):
    return SimpleNamespace(gateway=SimpleNamespace(id=worker), workeroutput={RECEIPT: receipt})


def test_serial_budget_counts_only_calls_and_keeps_the_threshold(guard, capsys):
    assert guard.SLOW_TEST_BUDGET_S == 120 and guard.SLOW_TEST_ALLOWLIST == {}
    for when, seconds in (("setup", 999.0), ("call", 120.0), ("teardown", 999.0)):
        guard.pytest_runtest_logreport(
            SimpleNamespace(when=when, duration=seconds, nodeid="test_a")
        )
    result = session()
    guard.pytest_sessionfinish(result, 0)
    assert result.exitstatus == 0
    guard._call_durations["test_a"] = 120.001
    guard.pytest_sessionfinish(result, 0)
    assert result.exitstatus == 1 and "SLOW TESTS: 1" in capsys.readouterr().out


def test_worker_emits_a_copy_for_controller_enforcement(guard):
    guard._call_durations["test_a"] = 121.0
    result = session(parallel=True, worker=True)
    guard.pytest_sessionfinish(result, 0)
    guard._call_durations.clear()
    assert result.config.workeroutput[RECEIPT] == {"test_a": 121.0}


@pytest.mark.parametrize("seconds,expected", [(0.0, 0), (120.0, 0), (120.001, 1)])
def test_complete_parallel_receipts_enforce_the_same_budget(guard, seconds, expected):
    guard._call_durations.update({"test_a": seconds, "test_b": 0.01})
    for worker, receipt in (
        ("gw0", {"test_a": seconds}),
        ("gw1", {"test_b": 0.01}),
        ("gw2", {}),
    ):
        item = node(worker, receipt)
        guard.pytest_configure_node(item)
        guard.pytest_testnodedown(item, None)
    result = session(parallel=True)
    guard.pytest_sessionfinish(result, 0)
    assert result.exitstatus == expected


@pytest.mark.parametrize(
    "receipt",
    [
        None,
        [],
        {"": 1.0},
        {1: 1.0},
        {"a": True},
        {"a": 1},
        {"a": "1"},
        {"a": -1.0},
        {"a": float("nan")},
        {"a": float("inf")},
    ],
)
def test_malformed_receipts_fail_closed(guard, receipt, capsys):
    item = node("gw0", receipt)
    guard.pytest_configure_node(item)
    guard.pytest_testnodedown(item, None)
    result = session(parallel=True)
    guard.pytest_sessionfinish(result, 0)
    assert result.exitstatus == 1
    assert "SLOW-TEST BUDGET INCOMPLETE" in capsys.readouterr().out


@pytest.mark.parametrize(
    "defect", ["missing", "unknown", "duplicate_worker", "duplicate_test", "crash", "report"]
)
def test_incomplete_or_inconsistent_workers_fail_closed(guard, defect):
    first, second = node("gw0", {"a": 1.0}), node("gw1", {"b": 2.0})
    guard._call_durations.update({"a": 1.0, "b": 2.0})
    guard.pytest_configure_node(first)
    guard.pytest_configure_node(second)
    guard.pytest_testnodedown(first, None)
    if defect == "unknown":
        second.gateway.id = "unregistered"
    elif defect == "duplicate_test":
        second.workeroutput[RECEIPT]["a"] = 1.0
    elif defect == "report":
        guard._call_durations["b"] = 0.0
    if defect != "missing":
        guard.pytest_testnodedown(second, "crashed" if defect == "crash" else None)
    if defect == "duplicate_worker":
        guard.pytest_testnodedown(first, None)
    result = session(parallel=True)
    guard.pytest_sessionfinish(result, 0)
    assert result.exitstatus == 1


def test_crashed_worker_without_output_is_reported_not_an_attribute_error(guard):
    item = SimpleNamespace(gateway=SimpleNamespace(id="gw0"))
    guard.pytest_configure_node(item)
    guard.pytest_testnodedown(item, "crashed")
    with pytest.raises(ValueError, match="failed"):
        guard._parallel_durations()


def test_no_receipts_cannot_masquerade_as_a_parallel_pass(guard):
    with pytest.raises(ValueError, match="missing worker"):
        guard._parallel_durations()


def test_the_budget_does_not_reset_an_existing_failure(guard):
    result = session()
    result.exitstatus = 2
    guard.pytest_sessionfinish(result, 2)
    assert result.exitstatus == 2


def test_new_sessions_do_not_reuse_prior_timings(guard):
    guard._call_durations["a"] = 5.0
    guard._expected_workers.add("gw0")
    guard._worker_durations["gw0"] = {"a": 5.0}
    guard._worker_errors.append("broken")
    guard.pytest_sessionstart(session())
    assert not any(
        (
            guard._call_durations,
            guard._expected_workers,
            guard._worker_durations,
            guard._worker_errors,
        )
    )


def run_workers(tmp_path, *, scenario="pass", measure_coverage=False):
    (tmp_path / "pytest.ini").write_text("[pytest]\nmarkers =\n    fast: isolated\n")
    (tmp_path / "conftest.py").write_text(CONTRACT.read_text() + "\nSLOW_TEST_BUDGET_S = 0.05\n")
    (tmp_path / "probe.py").write_text(
        "def first():\n    return 1\n\ndef second():\n    return 2\n"
    )
    (tmp_path / "test_probe_a.py").write_text(
        "import probe\n\ndef test_a():\n    assert probe.first() == 1\n"
    )
    body = {
        "slow": "import time; time.sleep(0.1)",
        "crash": "import os; os._exit(7)",
    }.get(scenario, "assert probe.second() == 2")
    (tmp_path / "test_probe_b.py").write_text(f"import probe\n\ndef test_b():\n    {body}\n")
    if scenario in {"missing", "forged"}:
        mutation = (
            f"node.workeroutput.pop({RECEIPT!r}, None)"
            if scenario == "missing"
            else f"node.workeroutput[{RECEIPT!r}] = {{}}"
        )
        (tmp_path / "tamper.py").write_text(
            "import pytest\n@pytest.hookimpl(tryfirst=True)\n"
            f"def pytest_testnodedown(node, error):\n    {mutation}\n"
        )
    env = {
        key: value
        for key, value in os.environ.items()
        if not key.startswith(("PYTEST_", "COV_CORE_", "COVERAGE_")) and key != "PYTHONPATH"
    }
    env["COVERAGE_FILE"] = str(tmp_path / ".coverage")
    command = [
        sys.executable,
        "-m",
        "pytest",
        "-q",
        "-o",
        "addopts=",
        "-n",
        "2",
        "--dist=loadfile",
        "--max-worker-restart=0",
    ]
    if scenario in {"missing", "forged"}:
        command.extend(["-p", "tamper"])
    command.extend(
        [
            "--cov=probe",
            f"--cov-config={ROOT / 'pyproject.toml'}",
            "--cov-report=term",
            "--cov-fail-under=100",
        ]
        if measure_coverage
        else ["--no-cov"]
    )
    return subprocess.run(
        command, cwd=tmp_path, env=env, text=True, capture_output=True, timeout=60
    )


@pytest.mark.parametrize("scenario", ["pass", "slow", "missing", "forged", "crash"])
def test_real_workers_preserve_budget_and_receipt_failures(tmp_path, scenario):
    result = run_workers(tmp_path, scenario=scenario)
    output = result.stdout + result.stderr
    assert (result.returncode == 0) is (scenario == "pass"), output
    if scenario == "slow":
        assert "SLOW TESTS: 1" in output
    elif scenario != "pass":
        assert "SLOW-TEST BUDGET INCOMPLETE" in output
    else:
        assert "2 passed" in output
        assert "Validated call timings for 2 tests across 2 workers" in output


def test_real_workers_combine_complete_statement_coverage(tmp_path):
    result = run_workers(tmp_path, measure_coverage=True)
    assert result.returncode == 0, result.stdout + result.stderr
    data = coverage.CoverageData(basename=str(tmp_path / ".coverage"))
    data.read()
    assert set(data.lines(str((tmp_path / "probe.py").resolve()))) == {1, 2, 4, 5}
