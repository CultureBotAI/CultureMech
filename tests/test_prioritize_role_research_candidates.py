"""Tests for scripts/prioritize_role_research_candidates.py — Step 7b prioritizer."""

from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path

import pytest
import yaml

_REPO_ROOT = Path(__file__).resolve().parent.parent
_SCRIPT_PATH = _REPO_ROOT / "scripts" / "prioritize_role_research_candidates.py"

_SPEC = importlib.util.spec_from_file_location("_prioritize", _SCRIPT_PATH)
_prio = importlib.util.module_from_spec(_SPEC)
sys.modules["_prioritize"] = _prio
_SPEC.loader.exec_module(_prio)  # type: ignore[union-attr]


def _make_mim_tree(tmp_path: Path, records: dict[str, dict]) -> Path:
    """Build a mini MediaIngredientMech tree with one YAML per record.

    `records` is `{path_relative_to_data_ingredients: doc}`.
    """
    mim = tmp_path / "mim"
    for rel_path, doc in records.items():
        target = mim / "data" / "ingredients" / rel_path
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(yaml.safe_dump(doc))
    return mim


# ---------------- _score_record ----------------


def test_score_zero_when_all_three_facets_full():
    doc = {
        "identifier": "CHEBI:17234",
        "mapping_status": "MAPPED",
        "occurrence_statistics": {"total_occurrences": 100},
        "nutritional_roles": [{"role": "CARBON_SOURCE"}],
        "physicochemical_roles": [{"role": "BUFFER"}],
        "cellular_metabolic_roles": [{"role": "SUBSTRATE"}],
    }
    score, breakdown = _prio._score_record(doc)
    assert score == 0.0
    assert breakdown["empty_facets"] == 0


def test_score_higher_for_more_facets_missing():
    base = {
        "identifier": "CHEBI:17234", "mapping_status": "MAPPED",
        "occurrence_statistics": {"total_occurrences": 100},
    }
    zero_full = dict(base)  # all 3 missing
    one_full = dict(base, nutritional_roles=[{"role": "X"}])  # 2 missing
    two_full = dict(base, nutritional_roles=[{"role": "X"}],
                    physicochemical_roles=[{"role": "Y"}])  # 1 missing
    s0, _ = _prio._score_record(zero_full)
    s1, _ = _prio._score_record(one_full)
    s2, _ = _prio._score_record(two_full)
    assert s0 > s1 > s2 > 0
    # 3× vs 2× vs 1× — linear in empty count.
    assert s0 == pytest.approx(3.0 * s2, rel=1e-3)


def test_score_occurrence_weighting_is_log10():
    """A 1638-occurrence ingredient (like glucose) should not swamp a 100-occurrence one."""
    doc_lo = {
        "identifier": "CHEBI:1", "mapping_status": "MAPPED",
        "occurrence_statistics": {"total_occurrences": 100},
    }
    doc_hi = {
        "identifier": "CHEBI:2", "mapping_status": "MAPPED",
        "occurrence_statistics": {"total_occurrences": 1638},
    }
    s_lo, _ = _prio._score_record(doc_lo)
    s_hi, _ = _prio._score_record(doc_hi)
    # Ratio should be log10(1639)/log10(101) ≈ 3.21/2.00 ≈ 1.60, not 16.4.
    ratio = s_hi / s_lo
    assert 1.2 < ratio < 2.0, f"expected log-scale ratio in (1.2, 2.0); got {ratio:.2f}"


def test_score_unmapped_downgrade():
    mapped = {
        "identifier": "CHEBI:17234", "mapping_status": "MAPPED",
        "occurrence_statistics": {"total_occurrences": 100},
    }
    unmapped = {
        "identifier": "CHEBI:17234", "mapping_status": "UNMAPPED",
        "occurrence_statistics": {"total_occurrences": 100},
    }
    s_m, _ = _prio._score_record(mapped)
    s_u, _ = _prio._score_record(unmapped)
    assert s_u == pytest.approx(0.3 * s_m, rel=1e-3)


def test_score_non_chebi_downgrade():
    chebi_grounded = {
        "identifier": "CHEBI:17234", "mapping_status": "MAPPED",
        "occurrence_statistics": {"total_occurrences": 100},
    }
    foodon_grounded = {
        "identifier": "MediaIngredientMech:00042", "mapping_status": "MAPPED",
        "ontology_mapping": {"ontology_id": "FOODON:03315720"},
        "occurrence_statistics": {"total_occurrences": 100},
    }
    s_c, _ = _prio._score_record(chebi_grounded)
    s_f, _ = _prio._score_record(foodon_grounded)
    assert s_f == pytest.approx(0.4 * s_c, rel=1e-3)


def test_score_ontology_mapping_chebi_lifts_multiplier():
    """A non-CHEBI identifier but CHEBI ontology_mapping still counts as CHEBI-grounded."""
    doc = {
        "identifier": "MediaIngredientMech:00042", "mapping_status": "MAPPED",
        "ontology_mapping": {"ontology_id": "CHEBI:17234"},
        "occurrence_statistics": {"total_occurrences": 100},
    }
    score, breakdown = _prio._score_record(doc)
    assert breakdown["chebi_mult"] == 1.0
    assert score > 0


def test_score_zero_when_no_occurrences():
    doc = {
        "identifier": "CHEBI:17234", "mapping_status": "MAPPED",
        "occurrence_statistics": {"total_occurrences": 0},
    }
    score, _ = _prio._score_record(doc)
    assert score == 0.0


# ---------------- collect_and_score ----------------


def test_collect_ranks_by_score(tmp_path):
    mim = _make_mim_tree(tmp_path, {
        "mapped/high.yaml": {
            "identifier": "CHEBI:1", "preferred_term": "high", "mapping_status": "MAPPED",
            "occurrence_statistics": {"total_occurrences": 1000},
        },  # all facets empty, high occurrence → high score
        "mapped/med.yaml": {
            "identifier": "CHEBI:2", "preferred_term": "med", "mapping_status": "MAPPED",
            "occurrence_statistics": {"total_occurrences": 50},
        },  # all empty, med occurrence
        "mapped/low.yaml": {
            "identifier": "CHEBI:3", "preferred_term": "low", "mapping_status": "MAPPED",
            "occurrence_statistics": {"total_occurrences": 5},
            "nutritional_roles": [{"role": "X"}],
            "physicochemical_roles": [{"role": "Y"}],
        },  # 1 facet empty, low occurrence
    })
    entries = _prio.collect_and_score(mim)
    assert [e["preferred_term"] for e in entries] == ["high", "med", "low"]


def test_collect_skips_fully_roled_ingredients(tmp_path):
    mim = _make_mim_tree(tmp_path, {
        "mapped/full.yaml": {
            "identifier": "CHEBI:1", "preferred_term": "full", "mapping_status": "MAPPED",
            "occurrence_statistics": {"total_occurrences": 100},
            "nutritional_roles": [{"role": "X"}],
            "physicochemical_roles": [{"role": "Y"}],
            "cellular_metabolic_roles": [{"role": "Z"}],
        },
        "mapped/gap.yaml": {
            "identifier": "CHEBI:2", "preferred_term": "gap", "mapping_status": "MAPPED",
            "occurrence_statistics": {"total_occurrences": 100},
        },
    })
    entries = _prio.collect_and_score(mim)
    assert len(entries) == 1
    assert entries[0]["preferred_term"] == "gap"


def test_collect_skips_zero_occurrence_ingredients(tmp_path):
    mim = _make_mim_tree(tmp_path, {
        "mapped/zero.yaml": {
            "identifier": "CHEBI:1", "preferred_term": "zero", "mapping_status": "MAPPED",
            "occurrence_statistics": {"total_occurrences": 0},
        },
        "mapped/one.yaml": {
            "identifier": "CHEBI:2", "preferred_term": "one", "mapping_status": "MAPPED",
            "occurrence_statistics": {"total_occurrences": 1},
        },
    })
    entries = _prio.collect_and_score(mim)
    assert [e["preferred_term"] for e in entries] == ["one"]


def test_collect_skips_already_researched(tmp_path):
    mim = _make_mim_tree(tmp_path, {
        "mapped/researched.yaml": {
            "identifier": "CHEBI:1", "preferred_term": "researched", "mapping_status": "MAPPED",
            "occurrence_statistics": {"total_occurrences": 100},
        },
        "mapped/fresh.yaml": {
            "identifier": "CHEBI:2", "preferred_term": "fresh", "mapping_status": "MAPPED",
            "occurrence_statistics": {"total_occurrences": 100},
        },
    })
    # Simulate a completed real run for `researched` (not a dry-run).
    roles_dir = mim / "research" / "ingredients" / "roles"
    roles_dir.mkdir(parents=True)
    (roles_dir / "researched-edison-literature-meta.yaml").write_text(yaml.safe_dump({
        "status": "complete", "task_id": "task_abc123",
    }))
    # And a dry-run for `fresh` — those don't count as researched.
    (roles_dir / "fresh-edison-literature-meta.yaml").write_text(yaml.safe_dump({
        "status": "dry-run", "task_id": None,
    }))

    entries = _prio.collect_and_score(mim)
    slugs = [e["slug"] for e in entries]
    assert "fresh" in slugs
    assert "researched" not in slugs


def test_collect_include_already_researched_flag(tmp_path):
    mim = _make_mim_tree(tmp_path, {
        "mapped/researched.yaml": {
            "identifier": "CHEBI:1", "preferred_term": "researched", "mapping_status": "MAPPED",
            "occurrence_statistics": {"total_occurrences": 100},
        },
    })
    roles_dir = mim / "research" / "ingredients" / "roles"
    roles_dir.mkdir(parents=True)
    (roles_dir / "researched-edison-literature-meta.yaml").write_text(yaml.safe_dump({
        "status": "complete", "task_id": "task_abc123",
    }))

    entries = _prio.collect_and_score(mim, include_already_researched=True)
    assert len(entries) == 1


# ---------------- batch entry shape ----------------


def test_batch_entry_carries_target_and_slug(tmp_path):
    mim = _make_mim_tree(tmp_path, {
        "mapped/L-cysteine.yaml": {
            "identifier": "CHEBI:17561", "preferred_term": "L-cysteine",
            "mapping_status": "MAPPED",
            "occurrence_statistics": {"total_occurrences": 100},
        },
    })
    entries = _prio.collect_and_score(mim)
    assert len(entries) == 1
    e = entries[0]
    assert e["slug"] == "L-cysteine"
    assert e["target"] == "data/ingredients/mapped/L-cysteine.yaml"
    assert e["identifier"] == "CHEBI:17561"
    assert e["preferred_term"] == "L-cysteine"
    assert "score" in e
    assert "score_breakdown" in e


# ---------------- CLI ----------------


def test_main_writes_output(tmp_path, capsys):
    mim = _make_mim_tree(tmp_path, {
        "mapped/L-cysteine.yaml": {
            "identifier": "CHEBI:17561", "preferred_term": "L-cysteine",
            "mapping_status": "MAPPED",
            "occurrence_statistics": {"total_occurrences": 100},
        },
    })
    out = tmp_path / "priority.json"
    rc = _prio.main(["--mim-repo", str(mim), "--out", str(out)])
    assert rc == 0
    data = json.loads(out.read_text())
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["slug"] == "L-cysteine"

    stdout = capsys.readouterr().out
    assert "Ranked 1 candidates" in stdout
    assert "Top 5:" in stdout
    assert "L-cysteine" in stdout


def test_main_top_cap(tmp_path):
    records = {
        f"mapped/rec_{i:03d}.yaml": {
            "identifier": f"CHEBI:{i:04d}", "preferred_term": f"rec_{i}",
            "mapping_status": "MAPPED",
            "occurrence_statistics": {"total_occurrences": 100 - i},
        }
        for i in range(10)
    }
    mim = _make_mim_tree(tmp_path, records)
    out = tmp_path / "priority.json"
    rc = _prio.main(["--mim-repo", str(mim), "--out", str(out), "--top", "3"])
    assert rc == 0
    data = json.loads(out.read_text())
    assert len(data) == 3
    # Sorted descending by occurrence weight.
    assert data[0]["preferred_term"] == "rec_0"


def test_main_errors_on_missing_mim_repo(tmp_path, capsys):
    out = tmp_path / "priority.json"
    with pytest.raises(SystemExit, match="MIM ingredients not found"):
        _prio.main(["--mim-repo", str(tmp_path / "nonexistent"), "--out", str(out)])
