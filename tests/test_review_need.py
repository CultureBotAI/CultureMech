"""Tests for the review-need scorer.

The scorer is the inverse of `prioritize_deep_research_candidates`: that one ranks
by expected research yield and hard-filters zero-ingredient records, so the
damaged tail is invisible to it. These tests pin the signals that surface that
tail, and — more importantly — pin that ordinary records score low, since a
ranking that flags everything ranks nothing.
"""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPO_ROOT / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


@pytest.fixture(scope="module")
def srn():
    return _load("score_review_need")


def _ing(name, grounded=True):
    d = {"preferred_term": name}
    if grounded:
        d["term"] = {"id": "CHEBI:12345"}
    return d


def _healthy():
    """A record with nothing wrong with it."""
    return {
        "name": "lb_broth",
        "original_name": "LB broth",
        "media_term": {"preferred_term": "DSMZ Medium 381"},
        "notes": "Source: DSMZ",
        "ph_value": 7.0,
        "ingredients": [_ing("Tryptone"), _ing("Yeast extract"), _ing("NaCl")],
    }


# --- the signals ----------------------------------------------------------


def test_a_healthy_record_scores_zero(srn):
    """The load-bearing test: a ranking that flags everything ranks nothing."""
    score, reasons = srn.score_record(_healthy())
    assert score == 0, reasons


def test_no_ingredients_scores_highest_single_signal(srn):
    doc = _healthy() | {"ingredients": []}
    score, reasons = srn.score_record(doc)
    assert "no ingredients" in "; ".join(reasons)
    assert score >= 30


def test_source_unavailable_empty_record_is_a_reviewed_endpoint(srn):
    doc = _healthy() | {
        "ingredients": [],
        "data_quality_flags": [
            "incomplete_composition",
            "source_information_unavailable",
        ],
    }

    score, reasons = srn.score_record(doc)

    assert score == 0, reasons
    assert srn.score_parsed([("bacterial/unavailable.yaml", doc)]) == []


def test_placeholder_ingredient_text_is_flagged(srn):
    doc = _healthy() | {"ingredients": [_ing("See source for composition", grounded=False)]}
    score, reasons = srn.score_record(doc)
    joined = "; ".join(reasons)
    assert "placeholder" in joined and "grounded" in joined


def test_unparsed_recipe_in_an_ingredient_name_is_flagged(srn):
    """The NBRC_1197 shape (#166): a whole composition block in one field."""
    doc = _healthy() | {
        "ingredients": [_ing("Substrates*10mMKH2PO40.85gNa2HPO4x7H2O4.9g(NH4)2SO40.5gMgSO4")]
    }
    _, reasons = srn.score_record(doc)
    assert "unparsed recipe" in "; ".join(reasons)


def test_ungrounded_ingredients_are_flagged(srn):
    doc = _healthy() | {"ingredients": [_ing("A", False), _ing("B", False), _ing("C", False)]}
    _, reasons = srn.score_record(doc)
    assert "no composition component is grounded" in "; ".join(reasons)


def test_partial_grounding_scores_less_than_none(srn):
    none_g = _healthy() | {
        "ingredients": [_ing("A", False), _ing("B", False), _ing("C", False), _ing("D", False)]
    }
    half_g = _healthy() | {
        "ingredients": [_ing("A", True), _ing("B", False), _ing("C", False), _ing("D", False)]
    }
    assert srn.score_record(none_g)[0] > srn.score_record(half_g)[0]


def test_solution_only_medium_is_not_treated_as_empty(srn):
    doc = _healthy() | {
        "ingredients": [],
        "solutions": [
            {
                "preferred_term": "Vitamin stock",
                "term": {"id": "mediadive.solution:7"},
            }
        ],
    }

    score, reasons = srn.score_record(doc)

    assert "no ingredients or solutions" not in reasons
    assert "no composition component is grounded" not in reasons
    assert score == 15


def test_medium_no_in_a_real_prepared_parent_name_is_not_placeholder_text(srn):
    doc = _healthy() | {
        "ingredients": [],
        "solutions": [
            {
                "preferred_term": "Gauze's Synthetic Medium NO. 1",
                "culturemech_term": {"id": "CultureMech:010138"},
            }
        ],
    }

    score, reasons = srn.score_record(doc)

    assert "placeholder ingredient text" not in reasons
    assert score == 15


def test_curated_sparse_delta_variant_is_not_suspiciously_small(srn):
    doc = _healthy() | {
        "ingredients": [],
        "solutions": [
            {
                "preferred_term": "ZMB ALS",
                "culturemech_term": {"id": "CultureMech:015792"},
            }
        ],
        "parent_media": {"id": "CultureMech:015792"},
        "variant_relationship": "OMITTED_COMPONENT_VARIANT",
        "data_quality_flags": ["ingredients_curated", "has_ontology_mappings"],
    }

    score, reasons = srn.score_record(doc)

    assert score == 0, reasons


def test_curated_opaque_commercial_product_is_not_regrounded_forever(srn):
    doc = _healthy() | {
        "ingredients": [
            {
                "preferred_term": "Opaque Medium (Supplier)",
                "concentration": {"value": "1000", "unit": "ML_PER_L"},
                "source": "Official recipe",
                "notes": "The official recipe names the product only.",
            },
        ],
        "data_quality_flags": ["ingredients_curated", "has_unmapped_ingredients"],
    }

    score, reasons = srn.score_record(doc)

    assert "no composition component is grounded" not in reasons
    assert score == 0, reasons


def test_inline_solution_composition_is_the_grounding_surface(srn):
    doc = _healthy() | {
        "ingredients": [],
        "solutions": [
            {
                "preferred_term": "Trace stock",
                "composition": [_ing("ZnSO4"), _ing("MnCl2"), _ing("CoCl2")],
            }
        ],
    }

    score, reasons = srn.score_record(doc)

    assert score == 0, reasons


def test_a_bare_strain_pointer_name_is_flagged(srn):
    doc = _healthy() | {"original_name": "For DSM 13514"}
    _, reasons = srn.score_record(doc)
    assert "identifies a strain" in "; ".join(reasons)


def test_a_curated_parent_linked_strain_pointer_variant_is_not_flagged(srn):
    doc = _healthy() | {
        "original_name": "For DSM 25939",
        "parent_media": {
            "path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml",
            "id": "CultureMech:001283",
        },
        "variant_relationship": "PH_VARIANT",
        "data_quality_flags": ["ingredients_curated", "has_ontology_mappings"],
    }

    score, reasons = srn.score_record(doc)

    assert score == 0, reasons


def test_a_source_duplicate_strain_pointer_name_is_still_flagged(srn):
    doc = _healthy() | {
        "original_name": "For DSM 25939",
        "parent_media": {
            "path": "data/normalized_yaml/bacterial/corn_meal_agar.yaml",
            "id": "CultureMech:001283",
        },
        "variant_relationship": "SOURCE_DUPLICATE",
        "data_quality_flags": ["ingredients_curated", "has_ontology_mappings"],
    }

    _, reasons = srn.score_record(doc)

    assert "identifies a strain" in "; ".join(reasons)


@pytest.mark.parametrize("name", ["BG11", "JM", "CH"])
def test_short_but_real_medium_names_are_not_flagged(srn, name):
    """BG11 and JM are real media. An earlier draft flagged short names and caught
    284 records, most of them legitimate — so name length is not used as a signal."""
    doc = _healthy() | {"original_name": name}
    _, reasons = srn.score_record(doc)
    assert not any("strain" in r or "name" in r for r in reasons), reasons


def test_missing_provenance_is_flagged(srn):
    doc = _healthy()
    del doc["media_term"]
    del doc["notes"]
    joined = "; ".join(srn.score_record(doc)[1])
    assert "media_term" in joined and "provenance" in joined


def test_structured_sources_are_enough_for_imported_source_provenance(srn):
    doc = _healthy()
    del doc["media_term"]
    del doc["ph_value"]
    doc["sources"] = [
        {
            "database": "CultureBotHT",
            "database_id": "DinoMM noCarbon",
            "url": "https://github.com/CultureBotAI/CultureBotHT",
        }
    ]

    score, reasons = srn.score_record(doc)

    assert score == 5
    assert reasons == ["no pH and no temperature"]
    assert srn.score_parsed([("bacterial/dinomm_nocarbon_highnutrient.yaml", doc)]) == []


def test_curated_legacy_source_url_unavailable_is_not_untraceable(srn):
    doc = _healthy()
    del doc["media_term"]
    doc["data_quality_flags"] = [
        "has_ontology_mappings",
        "ingredients_curated",
        "legacy_source_url_unavailable",
    ]

    score, reasons = srn.score_record(doc)

    assert score == 0, reasons


def test_missing_conditions_is_weighted_low(srn):
    """It fires on 51% of the corpus, so it must not dominate a rarer, worse signal."""
    no_cond = _healthy()
    del no_cond["ph_value"]
    cond_score = srn.score_record(no_cond)[0]
    worse = _healthy() | {"ingredients": []}
    assert cond_score < srn.score_record(worse)[0]


def test_signals_accumulate(srn):
    """A record that is wrong in several ways must outrank one wrong in a single way."""
    one = _healthy() | {"ingredients": []}
    many = {"name": "x", "original_name": "For DSM 999", "ingredients": []}
    assert srn.score_record(many)[0] > srn.score_record(one)[0]


# --- the corpus -----------------------------------------------------------


def _rank(srn, corpus):
    """Score the session-scoped corpus instead of re-reading it (#189)."""
    normalized = REPO_ROOT / "data" / "normalized_yaml"
    return srn.score_parsed([(str(p.relative_to(normalized)), d) for p, d in corpus])


def test_ranked_records_are_sorted_and_carry_reasons(srn, corpus):
    """The corpus-level check that the ranking means something when populated.

    This used to anchor on NBRC_1197, which #166 confirmed carried an unparsed
    recipe. That record was repaired in #299 — its composition was recovered from
    the preserved NBRC HTML. The last curated opaque-product endpoints now leave
    no severe rows, and a clean report is also a valid ranking state.

    What survives is the property that actually matters: every top-ranked record
    must have earned it.
    """
    rows = _rank(srn, corpus)
    for before, after in zip(rows, rows[1:], strict=False):
        assert before["score"] >= after["score"]
    for row in rows[:60]:
        assert row["reasons"], f"{row['file_path']} ranks top-60 with no reason given"


def test_most_of_the_corpus_is_not_flagged_as_severe(srn, corpus):
    """If a large share scored severe, the ranking would carry no information."""
    rows = _rank(srn, corpus)
    severe = [r for r in rows if r["score"] >= 50]
    assert len(severe) < 500, f"{len(severe)} records scored >=50; the weights are too loose"


def test_a_norm_level_signal_alone_does_not_qualify_a_record(srn, tmp_path):
    """#177: any non-zero score used to emit a row, so 4,332 records appeared in
    the report solely for lacking a pH value — a slot 51% of the corpus omits.

    That is the failure this whole scorer exists to avoid, one layer up: 60% of the
    corpus in a "needs review" file buries the 42 that are genuinely broken.
    Conditions refine the ranking among already-suspect records; they must not
    qualify one on their own.
    """
    import yaml as _yaml

    d = tmp_path / "bacterial"
    d.mkdir()
    healthy_but_no_conditions = {
        "id": "CultureMech:1",
        "name": "x",
        "original_name": "Nutrient Agar",
        "media_term": {"preferred_term": "DSMZ 1"},
        "notes": "Source: DSMZ",
        # 3 components: fewer would also trip the small-composition signal
        # and the record would no longer be conditions-only.
        "ingredients": [
            {"preferred_term": n, "term": {"id": "CHEBI:1"}}
            for n in ("Peptone", "Yeast extract", "NaCl")
        ],
    }
    (d / "a.yaml").write_text(_yaml.dump(healthy_but_no_conditions))

    score, reasons = srn.score_record(healthy_but_no_conditions)
    assert score > 0 and reasons == ["no pH and no temperature"], reasons
    assert srn.collect(tmp_path) == [], "a conditions-only record must not be emitted"


def test_conditions_still_contribute_when_something_else_is_wrong(srn, tmp_path):
    """The signal is a tiebreaker, not deleted — a suspect record missing
    conditions should outrank an otherwise identical one that has them."""
    import yaml as _yaml

    d = tmp_path / "bacterial"
    d.mkdir()
    broken = {
        "id": "CultureMech:2",
        "name": "y",
        "original_name": "Y",
        "media_term": {"preferred_term": "z"},
        "notes": "n",
        "ingredients": [],
    }
    (d / "b.yaml").write_text(_yaml.dump(broken))
    rows = srn.collect(tmp_path)
    assert len(rows) == 1
    assert "no pH and no temperature" in rows[0]["reasons"]
    assert rows[0]["score"] > srn.score_record(broken | {"ph_value": 7.0})[0]


def test_main_writes_lf_only_tsv(srn, tmp_path):
    import yaml as _yaml

    normalized = tmp_path / "normalized"
    normalized.mkdir()
    (normalized / "broken.yaml").write_text(
        _yaml.dump(
            {
                "id": "CultureMech:2",
                "name": "Broken",
                "original_name": "Broken",
                "ingredients": [],
            }
        ),
        encoding="utf-8",
    )
    out = tmp_path / "review_need_ranking.tsv"

    assert srn.main(["--normalized-dir", str(normalized), "--out", str(out)]) == 0

    data = out.read_bytes()
    assert b"\r\n" not in data
    assert data.startswith(b"score\tfile_path\trecord_id\tname\tn_components\treasons\n")
