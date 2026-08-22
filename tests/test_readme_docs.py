from __future__ import annotations

import importlib.util
import subprocess
import sys
from pathlib import Path

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
