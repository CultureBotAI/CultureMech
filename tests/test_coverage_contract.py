"""Collector changes must retain real line measurement and the coverage floor."""

import os
import subprocess
import sys
from pathlib import Path

import coverage
import pytest

CONFIG = Path(__file__).resolve().parents[1] / "pyproject.toml"


def test_statement_coverage_configuration_preserves_the_publication_gate(monkeypatch):
    monkeypatch.delenv("COVERAGE_CORE", raising=False)
    cov = coverage.Coverage(config_file=str(CONFIG))
    assert cov.get_option("run:core") == "sysmon"
    assert cov.get_option("run:branch") is False
    assert cov.get_option("run:plugins") == []
    assert cov.get_option("run:dynamic_context") is None
    assert cov.get_option("run:omit") == ["src/culturemech/schema/culturemech_dataclasses.py"]
    assert cov.get_option("report:fail_under") == 17


@pytest.mark.parametrize("execute_body", [False, True])
def test_configured_collector_measures_lines_and_enforces_floor(tmp_path, execute_body):
    probe = tmp_path / "probe.py"
    lines = ["def measured():"] + [f"    value = {number}" for number in range(100)]
    if execute_body:
        lines.append("measured()")
    probe.write_text("\n".join(lines) + "\n")
    data_file = tmp_path / ".coverage"
    env = dict(os.environ)
    for key in ("COVERAGE_CORE", "COVERAGE_PROCESS_START", "COVERAGE_RCFILE"):
        env.pop(key, None)
    env["COVERAGE_FILE"] = str(data_file)
    command = [sys.executable, "-m", "coverage"]
    measured = subprocess.run(
        command + ["run", f"--rcfile={CONFIG}", f"--source={tmp_path}", str(probe)],
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True,
        check=True,
    )
    assert "no-data-collected" not in measured.stderr
    if sys.version_info >= (3, 12):
        assert "no-sysmon" not in measured.stderr
    data = coverage.CoverageData(basename=str(data_file))
    data.read()
    assert data.measured_files() == {str(probe)}
    expected = set(range(1, len(lines) + 1)) if execute_body else {1}
    assert set(data.lines(str(probe))) == expected
    report = subprocess.run(
        command + ["report", f"--rcfile={CONFIG}"],
        cwd=tmp_path,
        env=env,
        capture_output=True,
        text=True,
    )
    assert report.returncode == (0 if execute_body else 2), report.stdout + report.stderr
    assert ("Coverage failure" in report.stdout) is not execute_body
