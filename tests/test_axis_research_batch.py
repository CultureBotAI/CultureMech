"""Tests for the axis-classification batch sampler.

Every property here fails SILENTLY if it regresses. A batch drawn from one
stratum, or with duplicates, or shorter than requested, still runs to completion
and still reports fill rates — it just answers a different question than the one
asked. Nothing errors, so only these tests can catch it.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def sarb():
    return _load("sample_axis_research_batch")


@pytest.fixture
def corpus(tmp_path):
    """A synthetic corpus with all four strata represented."""
    d = tmp_path / "bacterial"
    d.mkdir(parents=True)
    for i in range(12):
        (d / f"semi_{i}.yaml").write_text(yaml.dump(
            {"id": f"CultureMech:1{i:03d}", "name": f"semi_{i}",
             "composition_type": "SEMI_DEFINED"}))
    for i in range(12):
        (d / f"lb_broth_{i}.yaml").write_text(yaml.dump(
            {"id": f"CultureMech:2{i:03d}", "name": f"lb_broth_{i}",
             "original_name": f"LB broth {i}"}))
    for i in range(12):
        (d / f"plain_{i}.yaml").write_text(yaml.dump(
            {"id": f"CultureMech:3{i:03d}", "name": f"plain_{i}",
             "original_name": f"Obscure medium {i}"}))
    return tmp_path


def _run(sarb, corpus, tmp_path, size, ranking=None, seed=7):
    out = tmp_path / f"batch_{size}_{seed}.json"
    rank = tmp_path / f"rank_{seed}.json"
    rank.write_text(json.dumps(ranking or []))
    rc = sarb.main(["--normalized-dir", str(corpus), "--out", str(out),
                    "--ranking", str(rank), "--size", str(size), "--seed", str(seed)])
    assert rc == 0
    return json.loads(out.read_text())


# --- the load-bearing property ---------------------------------------------


def test_every_prefix_is_stratified(sarb, corpus, tmp_path):
    """The whole basis for probing with --limit N and generalising the result.

    The runner researches in file order and --limit takes the first N, so if the
    strata were concatenated instead of interleaved, a 25-record probe would draw
    all 25 from one stratum — completing normally and reporting fill rates for a
    sample that represents nothing.
    """
    batch = _run(sarb, corpus, tmp_path, 12)
    for n in (4, 8, 12):
        strata = {r["stratum"] for r in batch[:n]}
        assert len(strata) >= 3, f"prefix of {n} covers only {strata}"


def test_strata_are_disjoint(sarb, corpus, tmp_path):
    batch = _run(sarb, corpus, tmp_path, 12)
    paths = [r["file_path"] for r in batch]
    assert len(paths) == len(set(paths)), "a record was drawn into two strata"


def test_size_is_honoured_when_not_divisible_by_stratum_count(sarb, corpus, tmp_path):
    """#185: `per = size // len(strata)` floored the remainder away, so --size 25
    returned 24 while reporting success — a silent cap."""
    for size in (4, 5, 6, 7, 9):
        batch = _run(sarb, corpus, tmp_path, size)
        assert len(batch) == size, f"asked {size}, got {len(batch)}"


def test_seed_is_deterministic(sarb, corpus, tmp_path):
    """A rerun after a partial failure must research the same records, not a new
    set — otherwise the completed runs are orphaned and re-billed."""
    a = _run(sarb, corpus, tmp_path, 8, seed=99)
    b = _run(sarb, corpus, tmp_path, 8, seed=99)
    assert [r["file_path"] for r in a] == [r["file_path"] for r in b]


def test_different_seeds_draw_differently(sarb, corpus, tmp_path):
    a = _run(sarb, corpus, tmp_path, 8, seed=1)
    b = _run(sarb, corpus, tmp_path, 8, seed=2)
    assert [r["file_path"] for r in a] != [r["file_path"] for r in b]


def test_every_entry_carries_the_fields_the_runner_needs(sarb, corpus, tmp_path):
    for row in _run(sarb, corpus, tmp_path, 8):
        assert row["recipe_name"] and row["file_path"] and row["stratum"]
        assert "culturemech_id" in row


def test_an_undersized_stratum_is_absorbed_not_dropped(sarb, corpus, tmp_path):
    """DEEP_RESEARCH holds only 99 records corpus-wide, so an exhausted stratum is
    the normal case. Its unused quota goes to strata with room, rather than
    shortening the batch."""
    batch = _run(sarb, corpus, tmp_path, 30)
    assert len(batch) == 30, f"undersized stratum shortened the batch to {len(batch)}"


def test_a_corpus_smaller_than_size_says_so(sarb, corpus, tmp_path, capsys):
    """The only shortfall `allocate` cannot absorb. Silence here would read as
    full coverage of a --size that was never met."""
    batch = _run(sarb, corpus, tmp_path, 500)
    assert len(batch) == 36, len(batch)
    assert "NOTE" in capsys.readouterr().err


def test_well_known_stratum_recognises_well_known_media(sarb, corpus, tmp_path):
    """Without this stratum the run yields classifications nobody can grade."""
    batch = _run(sarb, corpus, tmp_path, 12)
    wk = [r for r in batch if r["stratum"] == "WELL_KNOWN"]
    assert wk and all("lb_broth" in r["recipe_name"] for r in wk)


def test_semi_defined_wins_over_well_known_when_a_record_is_both(sarb, tmp_path):
    """Strata are assigned in priority order; the docstring promises disjointness."""
    d = tmp_path / "c" / "bacterial"
    d.mkdir(parents=True)
    (d / "lb.yaml").write_text(yaml.dump(
        {"id": "CultureMech:1", "name": "lb_broth", "original_name": "LB broth",
         "composition_type": "SEMI_DEFINED"}))
    strata = sarb.assign_strata(sarb.load_media(tmp_path / "c"), set(), tmp_path / "c")
    assert len(strata["SEMI_DEFINED"]) == 1 and not strata["WELL_KNOWN"]


# --- the tracked artifact (#186) -------------------------------------------


def test_committed_batch_paths_still_resolve():
    """The batch is a tracked derived artifact holding paths into the corpus, and
    records do move — 629 were recategorised in #114.

    This rots quietly: the runner's tiered resolver (#173) falls back to filename
    and name, so a moved record still resolves and the batch looks healthy. A
    deleted or renamed one fails only at submission time, partway into a run of
    several hours.
    """
    batch_path = (REPO_ROOT / "data" / "import_tracking" / "reports"
                  / "axis_research_batch.json")
    if not batch_path.is_file():
        pytest.skip("batch artifact not present")
    normalized = REPO_ROOT / "data" / "normalized_yaml"
    missing = [r["file_path"] for r in json.loads(batch_path.read_text())
               if not (normalized / r["file_path"]).is_file()]
    assert not missing, (
        f"{len(missing)} batch entries no longer resolve, e.g. {missing[:5]}. "
        "Re-run `just sample-axis-research-batch` — but note that re-drawing "
        "orphans any completed runs against the old batch.")


def test_allocate_redistributes_an_exhausted_stratum(sarb):
    """DEEP_RESEARCH holds 99 records against OTHER's 9,730, so an exhausted
    stratum is the normal case. Its unused quota must go somewhere."""
    cap = {"SEMI_DEFINED": 612, "DEEP_RESEARCH": 99, "WELL_KNOWN": 653, "OTHER": 9730}
    for size in (25, 200, 500, 1000):
        q = sarb.allocate(size, cap)
        assert sum(q.values()) == size, f"size {size} -> {sum(q.values())}: {q}"
        assert all(q[k] <= cap[k] for k in cap), q


def test_allocate_caps_at_total_capacity(sarb):
    q = sarb.allocate(10_000, {"a": 3, "b": 4})
    assert sum(q.values()) == 7


def test_allocate_handles_empty_strata(sarb):
    q = sarb.allocate(6, {"a": 0, "b": 10})
    assert q == {"a": 0, "b": 6}
