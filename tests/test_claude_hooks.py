import os
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
PRE_HOOKS = [ROOT / ".claude" / "hooks" / name for name in ("pre-edit", "pre-commit")]


def _run(hook: Path, orchestration_root: Path | None = None, checker_exit: int = 0):
    env = os.environ.copy()
    env.pop("KG_MICROBE_ORCHESTRATION_ROOT", None)
    if orchestration_root is not None:
        env["KG_MICROBE_ORCHESTRATION_ROOT"] = str(orchestration_root)
        env["CHECKER_EXIT"] = str(checker_exit)
    return subprocess.run(
        ["bash", str(hook)],
        cwd=ROOT,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )


def _orchestration_root(path: Path) -> Path:
    scripts = path / "scripts"
    scripts.mkdir(parents=True)
    (scripts / "check_lock.py").write_text(
        "import os, sys\nsys.exit(int(os.environ.get('CHECKER_EXIT', '0')))\n"
    )
    return path


@pytest.mark.parametrize("hook", PRE_HOOKS)
def test_pre_hook_is_explicitly_disabled_without_configuration(hook: Path) -> None:
    result = _run(hook)

    assert result.returncode == 0
    assert "disabled" in result.stderr


@pytest.mark.parametrize("hook", PRE_HOOKS)
@pytest.mark.parametrize("checker_exit, expected", [(0, 0), (1, 1), (7, 2)])
def test_enabled_pre_hook_handles_all_checker_results(
    tmp_path: Path, hook: Path, checker_exit: int, expected: int
) -> None:
    root = _orchestration_root(tmp_path / "orchestration")

    result = _run(hook, root, checker_exit)

    assert result.returncode == expected
    if checker_exit not in (0, 1):
        assert "blocking" in result.stderr


@pytest.mark.parametrize("hook", PRE_HOOKS)
def test_enabled_pre_hook_fails_closed_when_checker_is_missing(tmp_path: Path, hook: Path) -> None:
    root = tmp_path / "orchestration"
    root.mkdir()

    result = _run(hook, root)

    assert result.returncode == 2
    assert "checker not found" in result.stderr


@pytest.mark.parametrize("name", ["post-edit", "post-commit"])
def test_post_hooks_have_explicit_disabled_and_configured_modes(tmp_path: Path, name: str) -> None:
    hook = ROOT / ".claude" / "hooks" / name
    disabled = _run(hook)
    assert disabled.returncode == 0
    assert "disabled" in disabled.stderr

    root = tmp_path / "orchestration"
    configured_without_status = _run(hook, root)
    assert configured_without_status.returncode == 2

    (root / "status").mkdir(parents=True)
    configured = _run(hook, root)
    assert configured.returncode == 0
    status = (root / "status" / "culturemech_claude_status.yaml").read_text()
    assert "status:" in status
