"""Tests for scripts/research_media_edison.py batch resolution + slug helpers.

Focus is the resolution logic that bridges the priority-list JSON
(``recipe_name`` + ``file_path``) to actual YAML paths under
``data/normalized_yaml/``. The corpus drifts as files are renamed
(snake_case migration, orphan-page cleanups), so the resolver has
to:

1. prefer ``data/normalized_yaml/<file_path>`` verbatim when the
   candidate looks like a relative path;
2. fall back to slug-style matching when the path-style lookup
   misses;
3. skip entries that resolve to nothing (without crashing the run).
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load_module():
    """Load research_media_edison.py without going through the package
    (the script lives in scripts/, not under src/)."""
    path = REPO_ROOT / "scripts" / "research_media_edison.py"
    spec = importlib.util.spec_from_file_location("research_media_edison", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules["research_media_edison"] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def rme():
    return _load_module()


def _make_recipe(category_dir: Path, name: str, recipe_id: str = "CultureMech:099999") -> Path:
    """Drop a minimal MediaRecipe YAML under tmp data dir."""
    category_dir.mkdir(parents=True, exist_ok=True)
    path = category_dir / f"{name}.yaml"
    path.write_text(
        f"id: {recipe_id}\n"
        f"name: {name}\n"
        "category: bacterial\n"
        "physical_state: LIQUID\n"
        "medium_type: COMPLEX\n"
    )
    return path


def test_load_batch_targets_returns_candidate_lists(rme, tmp_path):
    batch = tmp_path / "edison_batch.json"
    batch.write_text(json.dumps([
        {"recipe_name": "alpha_medium",
         "file_path": "bacterial/ALPHA_MEDIUM.yaml"},
        {"recipe_name": "beta_medium"},                              # no file_path
        {"file_path": "bacterial/GAMMA_MEDIUM.yaml"},                # no recipe_name
        {},                                                          # empty entry, skipped
    ]))
    candidates = rme.load_batch_targets(batch)
    # 3 of 4 entries yield at least one candidate.
    assert len(candidates) == 3
    # Order within each candidate list: recipe_name first, file_path second.
    assert candidates[0] == ["alpha_medium", "bacterial/ALPHA_MEDIUM.yaml"]
    assert candidates[1] == ["beta_medium"]
    assert candidates[2] == ["bacterial/GAMMA_MEDIUM.yaml"]


def test_load_batch_targets_rejects_non_list(rme, tmp_path):
    batch = tmp_path / "bad.json"
    batch.write_text(json.dumps({"not": "a list"}))
    with pytest.raises(SystemExit):
        rme.load_batch_targets(batch)


def test_short_job_uses_hyphens(rme):
    """CLI alias and filename suffix should match: literature-high, not _high."""
    from edison_client import JobNames

    assert rme._short_job(JobNames.LITERATURE) == "literature"
    assert rme._short_job(JobNames.LITERATURE_HIGH) == "literature-high"
    assert rme._short_job(JobNames.PHOENIX) == "phoenix"


def test_slug_for_uses_yaml_stem(rme, tmp_path):
    """Output filename should be human-readable (stem), not the numeric CURIE local part.

    Output paths from research_media.py's DRC variant use the stem;
    keep parity so users can sort/find research outputs by recipe name.
    """
    recipe = _make_recipe(tmp_path / "data" / "normalized_yaml" / "bacterial",
                          "luria_bertani_lb_medium",
                          recipe_id="CultureMech:009674")
    assert rme.slug_for(recipe) == "luria_bertani_lb_medium"


def test_display_path_safe_when_outside_repo(rme, tmp_path):
    """`Path.relative_to(REPO_ROOT)` raises when path is outside; the
    display helper must fall through to an absolute string instead."""
    outside = tmp_path / "elsewhere" / "out.md"
    out = rme._display_path(outside)
    # Either the absolute path or something relative — never raises.
    assert str(outside) in out or outside.name in out


def test_resolve_job_known_aliases(rme):
    from edison_client import JobNames

    assert rme.resolve_job("literature") is JobNames.LITERATURE
    assert rme.resolve_job("paperqa") is JobNames.LITERATURE
    assert rme.resolve_job("literature-high") is JobNames.LITERATURE_HIGH
    assert rme.resolve_job("paperqa-high") is JobNames.LITERATURE_HIGH


def test_resolve_job_unknown_raises(rme):
    with pytest.raises(SystemExit, match="Unknown --job"):
        rme.resolve_job("not-a-real-job")
