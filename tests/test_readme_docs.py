from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "update_readme_stats.py"
SPEC = importlib.util.spec_from_file_location("update_readme_stats", SCRIPT)
assert SPEC and SPEC.loader
update_readme_stats = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(update_readme_stats)


def test_readme_corpus_statistics_are_fresh() -> None:
    result = subprocess.run(
        [sys.executable, str(SCRIPT), "--check"],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stdout + result.stderr


def test_stats_replacement_is_deterministic(tmp_path: Path) -> None:
    normalized = tmp_path / "normalized"
    merged = tmp_path / "merged"
    (normalized / "bacterial").mkdir(parents=True)
    (normalized / "algae").mkdir()
    merged.mkdir()
    (normalized / "bacterial" / "a.yaml").touch()
    (normalized / "algae" / "b.yaml").touch()
    (merged / "one.yaml").touch()

    block = update_readme_stats.render_stats(normalized, merged)
    original = f"before\n{update_readme_stats.BEGIN}\nstale\n{update_readme_stats.END}\nafter\n"
    updated = update_readme_stats.replace_stats(original, block)

    assert "**2 normalized records** and **1 merged records**" in updated
    assert updated == update_readme_stats.replace_stats(updated, block)


def test_current_docs_use_repository_paths_and_current_axes() -> None:
    quick_start = (ROOT / "docs" / "QUICK_START.md").read_text()
    contributing = (ROOT / "docs" / "CONTRIBUTING.md").read_text()
    combined = quick_start + contributing

    assert "data/normalized_yaml/" in combined
    assert all(
        axis in combined for axis in ("composition_type", "nutritional_class", "functional_role")
    )
    assert "3-layer" not in combined and "three-tier" not in combined


def test_documented_local_commands_and_example_path_exist() -> None:
    result = subprocess.run(
        ["just", "--summary"], cwd=ROOT, check=True, capture_output=True, text=True
    )
    recipes = set(result.stdout.split())
    for recipe in (
        "validate-schema",
        "validate-terms",
        "validate-references",
        "gen-page",
        "build-browser",
        "gen-pages",
        "gen-media-pages",
        "test-fast",
        "test-corpus",
        "test-integration",
        "validate-strict",
        "assign-ids-check",
    ):
        assert recipe in recipes
    assert (ROOT / "data" / "normalized_yaml" / "bacterial" / "lb_medium.yaml").is_file()


@pytest.fixture
def stats_inputs(tmp_path: Path) -> dict[str, Path]:
    normalized = tmp_path / "normalized"
    merged = tmp_path / "merged"
    (normalized / "bacterial" / "nested").mkdir(parents=True)
    (normalized / "algae").mkdir()
    (normalized / "empty").mkdir()
    merged.mkdir()
    (normalized / "bacterial" / "nested" / "one.yaml").touch()
    (normalized / "algae" / "two.yaml").touch()
    (merged / "canonical.yaml").touch()
    readme = tmp_path / "README.md"
    landing = tmp_path / "index.html"
    for path in (readme, landing):
        path.write_text(
            f"preserve before\n{update_readme_stats.BEGIN}\nstale\n"
            f"{update_readme_stats.END}\npreserve after\n"
        )
    return {"readme": readme, "landing": landing, "normalized": normalized, "merged": merged}


def run_stats(paths: dict[str, Path], *extra: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            sys.executable,
            str(SCRIPT),
            "--readme",
            str(paths["readme"]),
            "--landing",
            str(paths["landing"]),
            "--normalized-dir",
            str(paths["normalized"]),
            "--merged-dir",
            str(paths["merged"]),
            *extra,
        ],
        check=False,
        capture_output=True,
        text=True,
    )


def test_stale_landing_fails_check_without_writes(stats_inputs: dict[str, Path]) -> None:
    paths = stats_inputs
    block = update_readme_stats.render_stats(paths["normalized"], paths["merged"])
    paths["readme"].write_text(
        update_readme_stats.replace_stats(paths["readme"].read_text(), block)
    )
    before = {key: paths[key].read_bytes() for key in ("readme", "landing")}

    checked = run_stats(paths, "--check")

    assert checked.returncode == 1
    assert str(paths["landing"]) in checked.stdout
    assert all(paths[key].read_bytes() == value for key, value in before.items())


def test_both_statistics_outputs_follow_corpus_and_are_idempotent(
    stats_inputs: dict[str, Path],
) -> None:
    paths = stats_inputs
    (paths["normalized"] / "bacterial" / "third.yaml").touch()
    (paths["merged"] / "second.yaml").touch()

    updated = run_stats(paths)

    assert updated.returncode == 0, updated.stderr
    readme, landing = paths["readme"].read_text(), paths["landing"].read_text()
    assert "**3 normalized records** and **2 merged records**" in readme
    assert "<b>3</b><span>normalized records</span>" in landing
    assert "<b>2</b><span>merged records</span>" in landing
    assert "<b>2</b><span>populated categories</span>" in landing
    for text in (readme, landing):
        assert text.startswith("preserve before\n") and text.endswith("preserve after\n")
    before = {
        key: (paths[key].read_bytes(), paths[key].stat().st_mtime_ns)
        for key in ("readme", "landing")
    }
    assert run_stats(paths).returncode == 0
    assert run_stats(paths, "--check").returncode == 0
    assert all(
        (paths[key].read_bytes(), paths[key].stat().st_mtime_ns) == value
        for key, value in before.items()
    )


@pytest.mark.parametrize("broken", ("readme", "landing"))
@pytest.mark.parametrize(
    "malformed",
    (
        f"{update_readme_stats.BEGIN}\nmissing end",
        f"{update_readme_stats.END}\n{update_readme_stats.BEGIN}",
        f"{update_readme_stats.BEGIN}\n{update_readme_stats.BEGIN}\n{update_readme_stats.END}",
    ),
)
def test_malformed_marker_prevents_any_output_write(
    stats_inputs: dict[str, Path],
    broken: str,
    malformed: str,
) -> None:
    paths = stats_inputs
    paths[broken].write_text(malformed)
    before = {key: paths[key].read_bytes() for key in ("readme", "landing")}

    updated = run_stats(paths)

    assert updated.returncode == 2
    assert "corpus-stats" in updated.stderr
    assert all(paths[key].read_bytes() == value for key, value in before.items())


def test_missing_corpus_directory_prevents_any_output_write(
    stats_inputs: dict[str, Path],
) -> None:
    paths = dict(stats_inputs)
    paths["merged"] = paths["merged"] / "missing"
    before = {key: paths[key].read_bytes() for key in ("readme", "landing")}

    updated = run_stats(paths)

    assert updated.returncode == 2
    assert "Corpus directory does not exist" in updated.stderr
    assert all(paths[key].read_bytes() == value for key, value in before.items())


def test_custom_readme_only_invocation_preserves_default_landing(
    stats_inputs: dict[str, Path],
    tmp_path: Path,
) -> None:
    copied_root = tmp_path / "other-checkout"
    (copied_root / "scripts").mkdir(parents=True)
    (copied_root / "app").mkdir()
    copied_script = copied_root / "scripts" / SCRIPT.name
    copied_script.write_text(SCRIPT.read_text())
    default_landing = copied_root / "app" / "index.html"
    default_landing.write_text("Leave this unrelated landing page alone.\n")
    paths = stats_inputs

    result = subprocess.run(
        [
            sys.executable,
            str(copied_script),
            "--readme",
            str(paths["readme"]),
            "--normalized-dir",
            str(paths["normalized"]),
            "--merged-dir",
            str(paths["merged"]),
        ],
        check=False,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stderr
    assert "**2 normalized records** and **1 merged records**" in paths["readme"].read_text()
    assert default_landing.read_text() == "Leave this unrelated landing page alone.\n"
