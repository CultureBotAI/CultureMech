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


# Restated deliberately, not read from `check_changed_python.VENDORED_FROM_CLAW`.
# The first version of this test iterated that constant, so deleting an entry
# shrank both the gate and the assertion and the test passed either way -- the
# tautology #286 describes, confirmed by mutation. Two literals that must agree
# is a weaker contract than deriving the set from claw's manifest (#437), but it
# is one that fails when only one side is edited.
EXPECTED_VENDORED_PYTHON = {
    "scripts/_edison_capture.py",
    "scripts/check_vendored_sync.py",
    "scripts/chem_formula.py",
    "scripts/deep_research_contract.py",
    "scripts/validate_id_label_correspondence.py",
    "tests/test_curation_timestamp_schema.py",
    "tests/test_id_label_empty_adapter.py",
    "tests/test_id_label_plausibility.py",
    "tests/test_id_label_unknown_prefix.py",
    "tests/test_provider_triage_contract.py",
    "tests/test_skill_frontmatter.py",
}


def test_the_gate_excludes_exactly_the_vendored_python_files() -> None:
    """#437. This gate requires a changed Python file to be ruff-clean and
    black-formatted here; `check_vendored_sync` requires a vendored artifact to
    be byte-identical to claw's canonical copy. A vendored file that changes
    satisfies both only by coincidence, and re-vendoring
    `validate_id_label_correspondence.py` ended it -- three findings under this
    configuration, in a file this repository must not edit.
    """
    assert check_changed_python.VENDORED_FROM_CLAW == EXPECTED_VENDORED_PYTHON


def test_every_vendored_python_file_exists_and_is_not_selected() -> None:
    """A listed path that no longer exists protects nothing; a listed path that
    is still selected is the bug itself."""
    missing = sorted(p for p in EXPECTED_VENDORED_PYTHON if not (ROOT / p).is_file())
    assert not missing, f"listed as vendored but absent: {missing}"

    selected = check_changed_python.select_python_files(sorted(EXPECTED_VENDORED_PYTHON))
    assert selected == [], (
        f"{selected} are vendored from claw and byte-identical to it by "
        f"contract, so this gate cannot ask for them to be reformatted"
    )


def test_the_vendored_exclusion_does_not_swallow_hand_written_scripts() -> None:
    """An exclusion wide enough to cover the gate's actual job would pass for
    the wrong reason."""
    hand_written = "scripts/export_kgx.py"
    assert (ROOT / hand_written).is_file()
    assert check_changed_python.select_python_files([hand_written]) == [hand_written]
