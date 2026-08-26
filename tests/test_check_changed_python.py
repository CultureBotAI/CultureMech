import importlib.util
import subprocess
from pathlib import Path

ROOT = Path(__file__).parents[1]
SCRIPT = ROOT / "scripts" / "check_changed_python.py"
SPEC = importlib.util.spec_from_file_location("check_changed_python", SCRIPT)
assert SPEC and SPEC.loader
check_changed_python = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(check_changed_python)


def test_changed_python_filter_excludes_generated_deleted_and_non_python(tmp_path: Path) -> None:
    existing = "src/culturemech/cli.py"
    generated = "src/culturemech/schema/culturemech_dataclasses.py"
    governed = "scripts/check_vendored_sync.py"

    assert check_changed_python.select_python_files(
        [
            existing,
            existing,
            generated,
            governed,
            "README.md",
            "scripts/does_not_exist.py",
        ]
    ) == [existing]


def test_changed_paths_disables_rename_detection(monkeypatch) -> None:
    calls = []

    def fake_run(command, **kwargs):
        calls.append((command, kwargs))
        return subprocess.CompletedProcess(command, 0, stdout="src/culturemech/cli.py\n", stderr="")

    monkeypatch.setattr(check_changed_python.subprocess, "run", fake_run)

    assert check_changed_python.changed_paths("origin/main") == ["src/culturemech/cli.py"]
    assert "--no-renames" in calls[0][0]
