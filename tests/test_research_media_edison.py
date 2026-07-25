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


# --- skip-already-done guard (#117) ---------------------------------------


def _write_meta(out_dir: Path, slug: str, job_short: str, *, status: str, task_id: str) -> Path:
    """Write the meta yaml that run_one() would leave behind."""
    out_dir.mkdir(parents=True, exist_ok=True)
    path = out_dir / f"{slug}-edison-{job_short}-meta.yaml"
    body = f"slug: {slug}\nstatus: {status}\n"
    if task_id:
        body += f"task_id: {task_id}\n"
    path.write_text(body)
    return path


def test_has_existing_research_true_for_completed_run(rme, tmp_path):
    _write_meta(tmp_path, "lb_broth", "literature", status="success", task_id="abc123")
    assert rme.has_existing_research(tmp_path, "lb_broth", "literature") is True


def test_has_existing_research_false_for_dry_run_stub(rme, tmp_path):
    """A dry run costs nothing and produces no answer — it must not block a real run."""
    _write_meta(tmp_path, "lb_broth", "literature", status="dry-run", task_id="")
    assert rme.has_existing_research(tmp_path, "lb_broth", "literature") is False


def test_has_existing_research_false_without_task_id(rme, tmp_path):
    """Status set but no task_id means the submission never landed."""
    _write_meta(tmp_path, "lb_broth", "literature", status="success", task_id="")
    assert rme.has_existing_research(tmp_path, "lb_broth", "literature") is False


def test_has_existing_research_is_scoped_to_the_same_job(rme, tmp_path):
    """`--job literature-high` after `literature` is a different, deeper question."""
    _write_meta(tmp_path, "lb_broth", "literature", status="success", task_id="abc123")
    assert rme.has_existing_research(tmp_path, "lb_broth", "literature") is True
    assert rme.has_existing_research(tmp_path, "lb_broth", "literature-high") is False


def test_has_existing_research_false_when_out_dir_missing(rme, tmp_path):
    assert rme.has_existing_research(tmp_path / "nope", "lb_broth", "literature") is False


def test_has_existing_research_survives_corrupt_meta(rme, tmp_path):
    """A truncated/corrupt meta must not crash a batch — treat it as not-researched."""
    tmp_path.mkdir(parents=True, exist_ok=True)
    (tmp_path / "lb_broth-edison-literature-meta.yaml").write_text("status: [unclosed\n")
    assert rme.has_existing_research(tmp_path, "lb_broth", "literature") is False


def test_partition_already_researched_preserves_order(rme, tmp_path):
    data = tmp_path / "data"
    paths = [_make_recipe(data, f"medium_{i}") for i in range(4)]
    out_dir = tmp_path / "research"
    _write_meta(out_dir, "medium_1", "literature", status="success", task_id="t1")
    _write_meta(out_dir, "medium_3", "literature", status="success", task_id="t3")

    to_submit, already = rme.partition_already_researched(paths, out_dir, "literature")
    assert [p.stem for p in to_submit] == ["medium_0", "medium_2"]
    assert [p.stem for p in already] == ["medium_1", "medium_3"]


def test_partition_with_no_prior_runs_submits_everything(rme, tmp_path):
    data = tmp_path / "data"
    paths = [_make_recipe(data, f"medium_{i}") for i in range(3)]
    to_submit, already = rme.partition_already_researched(paths, tmp_path / "research", "literature")
    assert len(to_submit) == 3
    assert already == []


def _batch_of(tmp_path: Path, rel_paths: list[str]) -> Path:
    batch = tmp_path / "batch.json"
    batch.write_text(json.dumps(
        [{"recipe_name": Path(p).stem, "file_path": p} for p in rel_paths]
    ))
    return batch


# Four real corpus records — main() resolves batch entries against the live
# data/normalized_yaml/ tree, so these cannot be tmp_path fixtures.
_REAL = [
    "bacterial/tyl_medium.yaml",
    "bacterial/mediadive_4367_SL10_elements.yaml",
    "bacterial/mediadive_1448_Main_sol_697.yaml",
    "bacterial/mediadive_3695_Main_sol_J68.yaml",
]


def _submitted_slugs(capsys) -> list[str]:
    """Slugs the dry run reported it would submit."""
    out = capsys.readouterr().out
    return [line.split("] ")[1].split(" -> ")[0].split("/")[-1].removesuffix(".yaml")
            for line in out.splitlines() if line.startswith("[DRY RUN]")]


def test_limit_window_advances_instead_of_resubmitting(rme, tmp_path, capsys):
    """The #117 property: repeating `--limit 2` must walk forward.

    Before the guard, `--limit 2` always took batch entries 0-1, so a second run
    re-submitted (re-billed) the same two records and never reached entries 2-3.
    """
    out_dir = tmp_path / "research"
    batch = _batch_of(tmp_path, _REAL)
    argv = ["--batch", str(batch), "--out-dir", str(out_dir), "--limit", "2", "--dry-run"]

    assert rme.main(argv) == 0
    first = _submitted_slugs(capsys)
    assert len(first) == 2

    # Dry runs don't count as researched, so mark them completed as a real run would.
    for slug in first:
        _write_meta(out_dir, slug, "literature", status="success", task_id=f"t-{slug}")

    assert rme.main(argv) == 0
    second = _submitted_slugs(capsys)
    assert len(second) == 2
    assert set(first).isdisjoint(second), f"re-submitted {set(first) & set(second)}"


def test_force_resubmits_already_researched(rme, tmp_path, capsys):
    out_dir = tmp_path / "research"
    batch = _batch_of(tmp_path, _REAL[:2])
    base = ["--batch", str(batch), "--out-dir", str(out_dir), "--dry-run"]

    assert rme.main(base) == 0
    done = _submitted_slugs(capsys)
    for slug in done:
        _write_meta(out_dir, slug, "literature", status="success", task_id=f"t-{slug}")

    # Default: everything is skipped, exit 0, nothing submitted.
    assert rme.main(base) == 0
    assert _submitted_slugs(capsys) == []

    # --force: submitted again.
    assert rme.main(base + ["--force"]) == 0
    assert set(_submitted_slugs(capsys)) == set(done)


def test_single_target_is_skipped_when_already_researched(rme, tmp_path, capsys):
    out_dir = tmp_path / "research"
    argv = ["--target", "tyl_medium", "--out-dir", str(out_dir), "--dry-run"]

    assert rme.main(argv) == 0
    assert _submitted_slugs(capsys) == ["tyl_medium"]

    _write_meta(out_dir, "tyl_medium", "literature", status="success", task_id="t1")
    assert rme.main(argv) == 0
    assert _submitted_slugs(capsys) == []
