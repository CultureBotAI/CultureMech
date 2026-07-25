"""Tests for duplicate handling in the deep-research ranking (#127).

The ranking showed `thermus_medium` 12 times in its top rows, which looked like
import duplicates. It is not: those are 12 distinct TOGO media that share a name,
with different ingredient counts (24/23/12/24/13/...) and different CultureMech
ids. Across the corpus, 1613 name-collision groups hold genuinely different
recipes and only 800 are exact repeats.

So the fix collapses only EXACT repeats and makes the rest identifiable, rather
than deduplicating on the ingredient fingerprint — which would merge media that
differ in the ingredient that defines them.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))
sys.path.insert(0, str(REPO_ROOT / "src"))


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


@pytest.fixture(scope="module")
def pdrc():
    return _load("prioritize_deep_research_candidates")


def _ing(ident, value, unit="G_PER_L"):
    return {"term": {"id": ident}, "concentration": {"value": value, "unit": unit}}


def _entry(pdrc, name, doc, score=50.0, path=None):
    return {
        "recipe_name": name,
        "file_path": path or f"bacterial/{name}.yaml",
        "id": f"CultureMech:{abs(hash(path or name)) % 999999:06d}",
        "score": score,
        "_identity": pdrc.strict_identity_key(doc),
    }


# --- strict_identity_key --------------------------------------------------


def test_identity_distinguishes_concentration(pdrc):
    """The case that rules out reusing the merge fingerprint.

    Pfennig's Medium I *with salt* exists at 10 and 30 G_PER_L NaCl under one
    name. Same ingredient set, so identical fingerprints — but the salt is the
    point of the medium.
    """
    a = {"ingredients": [_ing("CHEBI:26710", "10")]}
    b = {"ingredients": [_ing("CHEBI:26710", "30")]}
    assert pdrc.strict_identity_key(a) != pdrc.strict_identity_key(b)


def test_identity_distinguishes_unit(pdrc):
    a = {"ingredients": [_ing("CHEBI:26710", "1", "G_PER_L")]}
    b = {"ingredients": [_ing("CHEBI:26710", "1", "MG_PER_L")]}
    assert pdrc.strict_identity_key(a) != pdrc.strict_identity_key(b)


def test_identity_ignores_ingredient_order(pdrc):
    a = {"ingredients": [_ing("CHEBI:1", "1"), _ing("CHEBI:2", "2")]}
    b = {"ingredients": [_ing("CHEBI:2", "2"), _ing("CHEBI:1", "1")]}
    assert pdrc.strict_identity_key(a) == pdrc.strict_identity_key(b)


def test_identity_survives_malformed_ingredients(pdrc):
    doc = {"ingredients": [_ing("CHEBI:1", "1"), "not-a-dict", None]}
    assert pdrc.strict_identity_key(doc) == (("CHEBI:1", "1", "G_PER_L"),)


def test_identity_falls_back_to_preferred_term(pdrc):
    doc = {"ingredients": [{"preferred_term": "Yeast extract",
                            "concentration": {"value": "5", "unit": "G_PER_L"}}]}
    assert pdrc.strict_identity_key(doc) == (("Yeast extract", "5", "G_PER_L"),)


def test_fingerprint_would_have_merged_what_we_keep_apart(pdrc):
    """Pins WHY the merge fingerprint is not reused here.

    If the fingerprint ever becomes concentration-aware this test fails, and the
    two equivalences should be reconciled rather than left to diverge silently.
    """
    from culturemech.merge.fingerprint import RecipeFingerprinter

    fp = RecipeFingerprinter()
    a = {"name": "x", "ingredients": [_ing("CHEBI:26710", "10")]}
    b = {"name": "x", "ingredients": [_ing("CHEBI:26710", "30")]}
    assert fp.fingerprint(a) == fp.fingerprint(b)          # concentration-blind
    assert pdrc.strict_identity_key(a) != pdrc.strict_identity_key(b)  # we are not


# --- collapse_identical_records -------------------------------------------


def test_exact_duplicates_collapse_to_highest_score(pdrc):
    doc = {"ingredients": [_ing("CHEBI:1", "1")]}
    entries = [
        _entry(pdrc, "lb", doc, score=40.0, path="bacterial/lb_a.yaml"),
        _entry(pdrc, "lb", doc, score=90.0, path="bacterial/lb_b.yaml"),
    ]
    kept = pdrc.collapse_identical_records(entries)
    assert len(kept) == 1
    assert kept[0]["file_path"] == "bacterial/lb_b.yaml"
    assert kept[0]["identical_records"] == ["bacterial/lb_a.yaml"]
    assert kept[0]["identical_record_count"] == 1


def test_same_name_different_composition_are_all_kept(pdrc):
    """The thermus_medium case — distinct media, must not be collapsed."""
    entries = [
        _entry(pdrc, "thermus", {"ingredients": [_ing("CHEBI:1", "1")]}, path="bacterial/t1.yaml"),
        _entry(pdrc, "thermus", {"ingredients": [_ing("CHEBI:1", "2")]}, path="bacterial/t2.yaml"),
        _entry(pdrc, "thermus", {"ingredients": [_ing("CHEBI:2", "1")]}, path="bacterial/t3.yaml"),
    ]
    kept = pdrc.collapse_identical_records(entries)
    assert len(kept) == 3
    assert all(e["name_collision_count"] == 3 for e in kept)
    assert not any("identical_records" in e for e in kept)


def test_distinct_names_are_not_flagged(pdrc):
    doc = {"ingredients": [_ing("CHEBI:1", "1")]}
    entries = [_entry(pdrc, "a", doc, path="bacterial/a.yaml"),
               _entry(pdrc, "b", doc, path="bacterial/b.yaml")]
    kept = pdrc.collapse_identical_records(entries)
    assert len(kept) == 2  # same composition, different name -> both kept
    assert not any("name_collision_count" in e for e in kept)


def test_collapse_is_sorted_by_score(pdrc):
    doc = {"ingredients": [_ing("CHEBI:1", "1")]}
    entries = [
        _entry(pdrc, "a", doc, score=10.0, path="bacterial/a.yaml"),
        _entry(pdrc, "b", doc, score=99.0, path="bacterial/b.yaml"),
        _entry(pdrc, "c", doc, score=50.0, path="bacterial/c.yaml"),
    ]
    kept = pdrc.collapse_identical_records(entries)
    assert [e["score"] for e in kept] == [99.0, 50.0, 10.0]


def test_identity_key_is_removed_from_output(pdrc):
    """`_identity` is an internal grouping key and must not reach the report."""
    doc = {"ingredients": [_ing("CHEBI:1", "1")]}
    kept = pdrc.collapse_identical_records([_entry(pdrc, "a", doc)])
    assert "_identity" not in kept[0]


# --- corpus-level ---------------------------------------------------------


def test_ranking_has_no_exact_duplicate_records(pdrc):
    """End-to-end: no two ranked entries share a name AND a composition."""
    entries = pdrc.collect_records(set())
    seen: set[tuple] = set()
    normalized = REPO_ROOT / "data" / "normalized_yaml"
    for e in entries:
        doc = pdrc.load_yaml(normalized / e["file_path"])
        if not doc:
            continue
        key = (e["recipe_name"], pdrc.strict_identity_key(doc))
        assert key not in seen, f"exact duplicate survived: {e['file_path']}"
        seen.add(key)


def test_every_ranked_entry_carries_an_id(pdrc):
    """recipe_name is not an identity key; the id is what disambiguates."""
    entries = pdrc.collect_records(set())
    missing = [e["file_path"] for e in entries if not e.get("id")][:5]
    assert not missing, f"entries without an id: {missing}"
