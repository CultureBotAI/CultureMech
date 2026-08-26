"""Offline contracts for CultureMech's claw-authoritative vendored gate."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path
from types import ModuleType

import pytest
import yaml

ROOT = Path(__file__).resolve().parent.parent
CHECKER_PATH = ROOT / "scripts" / "check_vendored_sync.py"
LAUNCHER_PATH = ROOT / "scripts" / "check_vendored_sync.sh"
WORKFLOW_PATH = ROOT / ".github" / "workflows" / "vendored-sync.yaml"
PIN_PATH = ROOT / "scripts" / ".vendored_canon_ref"


def _load_checker() -> ModuleType:
    """Load the standalone vendored checker without requiring a package install."""

    name = "culturemech_vendored_sync_checker"
    spec = importlib.util.spec_from_file_location(name, CHECKER_PATH)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    # dataclasses resolves postponed annotations through sys.modules.
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def checker() -> ModuleType:
    return _load_checker()


def _workflow_run_block() -> str:
    workflow = yaml.safe_load(WORKFLOW_PATH.read_text())
    return workflow["jobs"]["vendored-sync"]["steps"][1]["run"]


def test_checker_uses_only_the_pinned_public_claw_manifest(checker: ModuleType) -> None:
    pin = PIN_PATH.read_text().strip()

    assert checker.CANONICAL_REPOSITORY == "CultureBotAI/culturebotai-claw"
    assert checker.CANONICAL_MANIFEST_PATH == (
        "src/kg_microbe_governance/vendored_artifacts.json"
    )
    assert checker.DEFAULT_PIN_PATH == "scripts/.vendored_canon_ref"
    assert len(pin) == 40 and all(character in "0123456789abcdef" for character in pin)
    assert checker.raw_url(pin, checker.CANONICAL_MANIFEST_PATH) == (
        "https://raw.githubusercontent.com/CultureBotAI/culturebotai-claw/"
        f"{pin}/src/kg_microbe_governance/vendored_artifacts.json"
    )


def test_launcher_and_unfiltered_workflow_invoke_the_full_manifest_checker() -> None:
    launcher = LAUNCHER_PATH.read_text()
    workflow = yaml.safe_load(WORKFLOW_PATH.read_text())
    triggers = workflow.get("on", workflow.get(True))
    concurrency = workflow["concurrency"]
    run = _workflow_run_block()

    assert 'exec python3 -I "${SCRIPT_DIR}/check_vendored_sync.py" "$@"' in launcher
    assert "FILES=(" not in launcher
    assert "MAPPED=(" not in launcher
    assert all("paths" not in (config or {}) for config in triggers.values())
    assert workflow["jobs"]["vendored-sync"]["timeout-minutes"] == 5
    assert "github.run_id" in concurrency["group"]
    assert concurrency["cancel-in-progress"] == "${{ github.event_name == 'pull_request' }}"
    assert run.count("bash scripts/check_vendored_sync.sh || status=$?") == 1
    assert "--repository" not in run


@pytest.mark.parametrize(
    ("outcome", "expected"),
    [
        ((14, ()), 0),
        ((14, ("DRIFT: governed artifact",)), 1),
    ],
)
def test_checker_main_maps_complete_check_results_to_exit_status(
    checker: ModuleType,
    monkeypatch: pytest.MonkeyPatch,
    capsys: pytest.CaptureFixture[str],
    outcome: tuple[int, tuple[str, ...]],
    expected: int,
) -> None:
    monkeypatch.setattr(checker, "check_repository", lambda *_args, **_kwargs: outcome)

    assert checker.main(["--root", str(ROOT), "--repository", "culturemech"]) == expected
    output = capsys.readouterr()
    if expected == 0:
        assert "OK: 14 governed artifacts" in output.out
    else:
        assert "DRIFT: governed artifact" in output.err


@pytest.mark.parametrize(
    ("error_name", "expected"),
    [
        ("CanonicalFetchError", 1),
        ("GovernanceError", 2),
    ],
)
def test_checker_main_preserves_retryable_and_precondition_exit_semantics(
    checker: ModuleType,
    monkeypatch: pytest.MonkeyPatch,
    error_name: str,
    expected: int,
) -> None:
    error_type = getattr(checker, error_name)

    def fail(*_args: object, **_kwargs: object) -> None:
        raise error_type("offline fixture failure")

    monkeypatch.setattr(checker, "check_repository", fail)
    assert checker.main(["--root", str(ROOT)]) == expected


def test_workflow_retries_exit_one_but_not_exit_two(tmp_path: Path) -> None:
    """Execute the CI shell block with offline stand-ins for checker and sleep."""

    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    attempts = tmp_path / "attempts"
    fake_bash = fake_bin / "bash"
    fake_bash.write_text(
        "#!/bin/sh\n"
        "count=0\n"
        "if [ -f \"$TEST_ATTEMPTS\" ]; then count=$(cat \"$TEST_ATTEMPTS\"); fi\n"
        "printf '%s' \"$((count + 1))\" > \"$TEST_ATTEMPTS\"\n"
        "case \"$TEST_CHECKER_SEQUENCE:$count\" in\n"
        "  1,1,0:0) exit 1 ;;\n"
        "  1,1,0:1) exit 1 ;;\n"
        "  1,1,0:2) exit 0 ;;\n"
        "  2:0) exit 2 ;;\n"
        "  *) exit 99 ;;\n"
        "esac\n"
    )
    fake_bash.chmod(0o755)
    fake_sleep = fake_bin / "sleep"
    fake_sleep.write_text("#!/bin/sh\nexit 0\n")
    fake_sleep.chmod(0o755)

    environment = {
        "PATH": f"{fake_bin}:/usr/bin:/bin",
        "TEST_ATTEMPTS": str(attempts),
        "TEST_CHECKER_SEQUENCE": "1,1,0",
    }
    retryable = subprocess.run(
        ["/bin/bash", "-c", _workflow_run_block()],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    assert retryable.returncode == 0, retryable.stdout + retryable.stderr
    assert attempts.read_text() == "3"

    attempts.unlink()
    environment["TEST_CHECKER_SEQUENCE"] = "2"
    precondition = subprocess.run(
        ["/bin/bash", "-c", _workflow_run_block()],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    assert precondition.returncode == 2
    assert attempts.read_text() == "1"

    attempts.unlink()
    environment["TEST_CHECKER_SEQUENCE"] = "99"
    unexpected = subprocess.run(
        ["/bin/bash", "-c", _workflow_run_block()],
        cwd=ROOT,
        env=environment,
        capture_output=True,
        text=True,
        check=False,
    )
    assert unexpected.returncode == 99
    assert attempts.read_text() == "1"
    assert "unexpected exit 99" in unexpected.stderr
