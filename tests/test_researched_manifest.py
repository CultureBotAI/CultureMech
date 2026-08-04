"""Tests for the tracked researched-media manifest (#121).

The property under test is reproducibility: the priority reports must be a pure
function of TRACKED inputs (the corpus + the manifest), never of the gitignored
`research/media/` tree. Before this, regenerating on a different machine
reordered the entire top-10 and the diff was indistinguishable from a real data
change.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load(name: str):
    path = REPO_ROOT / "scripts" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def rmf():
    return _load("researched_manifest")


def _write_meta(research_dir: Path, stem: str, *, status: str, task_id: str,
                slug: str | None = None) -> Path:
    research_dir.mkdir(parents=True, exist_ok=True)
    path = research_dir / f"{stem}-meta.yaml"
    body = f"status: {status}\n"
    if task_id:
        body += f"task_id: {task_id}\n"
    if slug:
        body += f"slug: {slug}\n"
    path.write_text(body)
    return path


# --- scan_research_dir ----------------------------------------------------


def test_scan_picks_up_completed_runs(rmf, tmp_path):
    _write_meta(tmp_path, "lb_broth-edison-literature", status="success", task_id="t1")
    found = rmf.scan_research_dir(tmp_path)
    assert len(found) == 1
    assert found[0]["slug"] == "lb_broth"
    assert found[0]["job"] == "literature"
    assert found[0]["kind"] == "medium"


def test_scan_ignores_dry_runs_and_missing_task_ids(rmf, tmp_path):
    _write_meta(tmp_path, "a-edison-literature", status="dry-run", task_id="")
    _write_meta(tmp_path, "b-edison-literature", status="success", task_id="")
    assert rmf.scan_research_dir(tmp_path) == []


def test_scan_tags_phase2_organism_runs(rmf, tmp_path):
    """A per-organism follow-up is not the same as researching the medium."""
    _write_meta(tmp_path, "arch_medium-organism-archaeoglobus-fulgidus-edison-literature",
                status="success", task_id="t2")
    [entry] = rmf.scan_research_dir(tmp_path)
    assert entry["kind"] == "organism"
    assert entry["media_slug"] == "arch_medium"


def test_scan_missing_dir_is_empty(rmf, tmp_path):
    assert rmf.scan_research_dir(tmp_path / "nope") == []


def test_scan_survives_corrupt_meta(rmf, tmp_path):
    (tmp_path / "bad-edison-literature-meta.yaml").write_text("status: [unclosed\n")
    _write_meta(tmp_path, "good-edison-literature", status="success", task_id="t1")
    assert [e["slug"] for e in rmf.scan_research_dir(tmp_path)] == ["good"]


# --- researched_slugs -----------------------------------------------------


def test_researched_slugs_excludes_organism_entries(rmf, tmp_path):
    """The medium-level filter must not be tripped by a phase-2 run."""
    manifest = tmp_path / "m.json"
    rmf.write_manifest([
        {"slug": "lb_broth", "job": "literature", "task_id": "t1", "kind": "medium"},
        {"slug": "arch-organism-foo", "job": "literature", "task_id": "t2",
         "kind": "organism", "media_slug": "arch"},
    ], manifest)
    assert rmf.researched_slugs(manifest) == {"lb_broth"}


def test_researched_slugs_treats_untagged_entries_as_medium(rmf, tmp_path):
    """Back-compat: entries written before `kind` existed still filter."""
    manifest = tmp_path / "m.json"
    manifest.write_text(json.dumps({"entries": [{"slug": "lb_broth", "job": "literature"}]}))
    assert rmf.researched_slugs(manifest) == {"lb_broth"}


def test_missing_manifest_excludes_nothing(rmf, tmp_path):
    """A fresh clone with no manifest must still produce a usable ranking."""
    assert rmf.researched_slugs(tmp_path / "absent.json") == set()


def test_corrupt_manifest_excludes_nothing(rmf, tmp_path):
    manifest = tmp_path / "m.json"
    manifest.write_text("{not json")
    assert rmf.researched_slugs(manifest) == set()


# --- merge ----------------------------------------------------------------


def test_merge_is_a_union_and_never_drops_entries(rmf):
    """Each machine sees only its own research/; replace would delete others' work."""
    existing = [{"slug": "from_other_machine", "job": "literature", "task_id": "x", "kind": "medium"}]
    discovered = [{"slug": "local", "job": "literature", "task_id": "y", "kind": "medium"}]
    merged, added = rmf.merge_entries(existing, discovered)
    assert {e["slug"] for e in merged} == {"from_other_machine", "local"}
    assert [e["slug"] for e in added] == ["local"]


def test_merge_is_idempotent(rmf):
    entries = [{"slug": "a", "job": "literature", "task_id": "t", "kind": "medium"}]
    merged, added = rmf.merge_entries(entries, entries)
    assert merged == entries
    assert added == []


def test_merge_distinguishes_jobs_for_the_same_slug(rmf):
    existing = [{"slug": "a", "job": "literature", "task_id": "t1", "kind": "medium"}]
    discovered = [{"slug": "a", "job": "literature-high", "task_id": "t2", "kind": "medium"}]
    merged, added = rmf.merge_entries(existing, discovered)
    assert len(merged) == 2
    assert len(added) == 1


def test_written_manifest_is_sorted_for_stable_diffs(rmf, tmp_path):
    manifest = tmp_path / "m.json"
    rmf.write_manifest([
        {"slug": "zebra", "job": "literature", "task_id": "t2", "kind": "medium"},
        {"slug": "alpha", "job": "literature", "task_id": "t1", "kind": "medium"},
    ], manifest)
    doc = json.loads(manifest.read_text())
    assert [e["slug"] for e in doc["entries"]] == ["alpha", "zebra"]
    assert manifest.read_text().endswith("\n")


# --- the actual reproducibility property ----------------------------------


def test_prioritizer_output_does_not_depend_on_local_research_dir(tmp_path, monkeypatch):
    """The whole point of #121.

    `collect_records` must produce the same ranking whether or not a local
    `research/media/` tree exists. Previously it scanned that tree directly, so
    the committed reports encoded one machine's state.
    """
    pdrc = _load("prioritize_deep_research_candidates")

    manifest = tmp_path / "m.json"
    manifest.write_text(json.dumps({"entries": [
        {"slug": "tyl_medium", "job": "literature", "task_id": "t1", "kind": "medium"},
    ]}))
    researched = _load("researched_manifest").researched_slugs(manifest)

    first = pdrc.collect_records(researched)

    # Simulate a machine with a completely different local research/ tree by
    # pointing the module's research dir somewhere populated-but-irrelevant.
    other = tmp_path / "research_media"
    _write_meta(other, "thermus_medium-edison-literature", status="success", task_id="zzz")
    monkeypatch.setattr(pdrc.rmf, "DEFAULT_RESEARCH_DIR", other, raising=False)

    second = pdrc.collect_records(researched)

    assert [e["recipe_name"] for e in first] == [e["recipe_name"] for e in second]
    assert "tyl_medium" not in {e["recipe_name"] for e in first}


# --- axis classification vs growth research (#152) -------------------------
#
# Both run under job "literature" on the same slug and write the same
# `<slug>-edison-literature-meta.yaml` filename, so only the template
# distinguishes them. These pin that they stay distinct, because every failure
# mode here is silent: a shorter candidate list looks like progress.


def _meta(tmp_path, slug, template, task_id="t1"):
    d = tmp_path
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{slug}-edison-literature-meta.yaml").write_text(
        f"slug: {slug}\nstatus: success\ntask_id: {task_id}\ntemplate_path: {template}\n")
    return d


def test_axis_runs_are_tagged_axis_not_medium(tmp_path):
    rmf = _load("researched_manifest")
    d = _meta(tmp_path / "media_axis", "lb_broth", "templates/media_axis_classification.md")
    entries = rmf.scan_research_dir(d)
    assert [e["kind"] for e in entries] == ["axis"]


def test_growth_runs_are_still_tagged_medium(tmp_path):
    rmf = _load("researched_manifest")
    d = _meta(tmp_path / "media", "lb_broth", "templates/media_growth_research.md")
    assert [e["kind"] for e in rmf.scan_research_dir(d)] == ["medium"]


def test_axis_run_does_not_mark_a_medium_researched(tmp_path):
    """The load-bearing one: researched_slugs() feeds the prioritizer's
    already-researched filter, so tagging axis runs "medium" would drop every
    axis-classified record out of the growth-research queue."""
    rmf = _load("researched_manifest")
    d = _meta(tmp_path / "media_axis", "lb_broth", "templates/media_axis_classification.md")
    manifest = tmp_path / "m.json"
    rmf.write_manifest(rmf.scan_research_dir(d), manifest)
    assert rmf.researched_slugs(manifest) == set(), \
        "an axis run must not count as the medium having been researched"


def test_axis_and_growth_runs_for_one_slug_coexist(tmp_path):
    """Keyed on (slug, job) alone these collide and the union drops one."""
    rmf = _load("researched_manifest")
    axis = rmf.scan_research_dir(
        _meta(tmp_path / "media_axis", "lb_broth", "templates/media_axis_classification.md", "a1"))
    growth = rmf.scan_research_dir(
        _meta(tmp_path / "media", "lb_broth", "templates/media_growth_research.md", "g1"))
    merged, added = rmf.merge_entries(axis, growth)
    assert len(merged) == 2, f"growth run masked by the axis run: {merged}"
    assert {e["kind"] for e in merged} == {"axis", "medium"}
    assert len(added) == 1

    manifest = tmp_path / "m.json"
    rmf.write_manifest(merged, manifest)
    assert rmf.researched_slugs(manifest) == {"lb_broth"}


def test_legacy_entries_without_kind_do_not_re_add(tmp_path):
    """_entry_key gained a third element; legacy rows must keep their identity."""
    rmf = _load("researched_manifest")
    legacy = [{"slug": "lb_broth", "job": "literature", "task_id": "old"}]
    same = [{"slug": "lb_broth", "job": "literature", "task_id": "old", "kind": "medium"}]
    merged, added = rmf.merge_entries(legacy, same)
    assert added == [] and len(merged) == 1
