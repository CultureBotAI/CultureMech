"""A KGX node is keyed on the record's permanent id, never on its name (#438).

Node emission dedupes on id, so the name-keyed ids the export used until #438
collapsed every record sharing a name into one node with merged edges — 3,181
media and 4,787 solution records on the 2026-09-09 corpus. The 4,784 MediaDive
solution records carry ``preferred_term`` and no ``name`` at all, so they
sanitized to the empty string and emitted no node while their ``has_part``
edges still pointed at ``culturemech:``.

Kept free of corpus paths on purpose: conftest tiers a module by substring, and
these cases need no records.
"""

from __future__ import annotations

import pytest

from culturemech.export.kgx_export import (
    RECORDS_DIR_ENV,
    _solution_record_index,
    is_solution_record,
    nested_solution_target,
    nodes,
    record_label,
    record_node_id,
    transform,
)

MEDIUM = {
    "id": "CultureMech:900101",
    "name": "Defined freshwater medium (CoSO4)",
    "medium_type": "DEFINED",
    "ingredients": [{"preferred_term": "Glucose", "term": {"id": "CHEBI:17234"}}],
}
# The #392 shape: a second record whose name sanitizes to the same string.
TWIN = {**MEDIUM, "id": "CultureMech:900102"}

# The MediaDive solution-record shape: preferred_term, no name, upstream term id.
SOLUTION = {
    "id": "CultureMech:900103",
    "preferred_term": "SL10 elements",
    "term": {"id": "mediadive.solution:4367"},
    "composition": [{"preferred_term": "ZnSO4", "term": {"id": "CHEBI:32312"}}],
}


def _record_node(record):
    by_id = {n["id"]: n for n in nodes(record)}
    return by_id[record_node_id(record)]


def test_the_node_id_is_the_record_id():
    assert record_node_id(MEDIUM) == "CultureMech:900101"
    assert _record_node(MEDIUM)["id"] == "CultureMech:900101"


def test_records_sharing_a_name_keep_distinct_nodes_and_edges():
    """The collapse: same name, different records, one node before #438."""
    assert record_node_id(MEDIUM) != record_node_id(TWIN)
    subjects = {e["subject"] for e in transform(MEDIUM)} | {e["subject"] for e in transform(TWIN)}
    assert subjects == {"CultureMech:900101", "CultureMech:900102"}


def test_a_solution_record_with_no_name_gets_a_node_labelled_by_preferred_term():
    node = _record_node(SOLUTION)
    assert node["name"] == "SL10 elements"
    assert node["category"] == ["biolink:ChemicalMixture"]


def test_a_solution_record_is_recognised_by_either_explicit_signal():
    assert is_solution_record(SOLUTION)
    assert is_solution_record({"id": "CultureMech:900104", "name": "x", "record_kind": "SOLUTION"})
    assert not is_solution_record(MEDIUM)


def test_a_medium_is_a_growth_medium_not_a_bare_mixture():
    assert "biolink:GrowthMedium" in _record_node(MEDIUM)["category"]


def test_label_falls_back_from_name_to_preferred_term():
    assert record_label(MEDIUM) == "Defined freshwater medium (CoSO4)"
    assert record_label(SOLUTION) == "SL10 elements"


@pytest.mark.parametrize("bad", [{}, {"id": ""}, {"id": "   "}, {"name": "LB"}])
def test_a_record_without_an_id_is_an_error_not_a_name_keyed_node(bad):
    """Falling back to the name would quietly reinstate the collapse."""
    with pytest.raises(ValueError, match="no id"):
        record_node_id(bad)
    with pytest.raises(ValueError):
        list(nodes(bad))
    with pytest.raises(ValueError):
        list(transform(bad))


# The curated `record_kind: SOLUTION` shape (#175): MediaRecipe fields, no name.
CURATED_SOLUTION = {
    "id": "CultureMech:900105",
    "preferred_term": "Trace salt solution",
    "record_kind": "SOLUTION",
    "ingredients": [{"preferred_term": "ZnSO4", "term": {"id": "CHEBI:32312"}}],
}


def test_edges_from_a_solution_record_use_its_id_not_the_empty_local_id():
    subjects = {e["subject"] for e in transform(CURATED_SOLUTION)}
    assert subjects == {"CultureMech:900105"}
    assert _record_node(CURATED_SOLUTION)["category"] == ["biolink:ChemicalMixture"]


def test_a_solution_record_gets_no_medium_type_node_or_edge():
    """202 solution records carry a medium_type; it is a medium's attribute (#442)."""
    typed = {**CURATED_SOLUTION, "medium_type": "DEFINED"}
    assert not any(n["id"].startswith("CultureMech:medium_type_") for n in nodes(typed))
    assert not any(e["predicate"] == "biolink:has_attribute" for e in transform(typed))
    # and a medium with the same field still gets both
    assert any(n["id"] == "CultureMech:medium_type_DEFINED" for n in nodes(MEDIUM))
    assert any(e["predicate"] == "biolink:has_attribute" for e in transform(MEDIUM))


def test_a_solution_record_emits_its_top_level_composition():
    """The SolutionRecipe shape keeps reagents in `composition`, not `ingredients`;
    until #442 transform() never walked it and 4,784 records emitted no has_part."""
    # The object goes through the MIM resolver (ZnSO4 publishes as CHEBI:35176), so
    # assert the edge and its identity class rather than the record's own id.
    objects = [e["object"] for e in transform(SOLUTION) if e["predicate"] == "biolink:has_part"]
    assert len(objects) == 1 and objects[0].startswith("CHEBI:")
    assert all(e["subject"] == "CultureMech:900103" for e in transform(SOLUTION))


def test_everything_the_export_mints_shares_one_prefix():
    """Records carry CultureMech:NNNNNN; auxiliary nodes used a lower-cased twin of
    that prefix until #440, which no consumer treats as the same namespace."""
    full = {
        **MEDIUM,
        "physical_state": "LIQUID",
        "applications": ["Canary use"],
        "solutions": [{"preferred_term": "Trace Elements", "composition": []}],
        "variants": [{"name": "Canary agar"}],
    }
    minted = {n["id"] for n in nodes(full)}
    minted |= {
        end
        for e in transform(full)
        for end in (e["subject"], e["object"])
        if ":" in end and end.split(":", 1)[0].lower() == "culturemech"
    }
    assert len(minted) >= 6, minted
    assert all(i.startswith("CultureMech:") for i in minted), sorted(minted)


def test_quantified_edges_carry_value_and_unit_as_typed_fields():
    """#445: the quantity travels as two fields, the value string as written and the
    unit enum token, beside the joined qualifier; unquantified edges carry neither."""
    record = {
        **MEDIUM,
        "ingredients": [
            {
                "preferred_term": "Glucose",
                "term": {"id": "CHEBI:17234"},
                "concentration": {"value": "5e-05", "unit": "MOLAR"},
            },
            {"preferred_term": "Agar", "term": {"id": "CHEBI:2509"}},
        ],
    }
    by_obj = {e["object"]: e for e in transform(record) if e["predicate"] == "biolink:has_part"}
    q = next(e for o, e in by_obj.items() if e.get("value"))
    assert (q["value"], q["unit"]) == ("5e-05", "MOLAR")
    assert any(x["qualifier_value"] == "5e-05 MOLAR" for x in q["qualifiers"])
    bare = next(e for o, e in by_obj.items() if not e.get("value"))
    assert bare["unit"] is None and not bare.get("qualifiers")


@pytest.mark.parametrize("raw", ["variable", "-", "0.01 g per vessel"])
def test_a_value_that_is_not_a_number_keeps_the_qualifier_but_no_typed_pair(raw):
    """The typed pair is for arithmetic; 3,598 corpus rows carry a non-numeric
    value and MediaDive's column is numeric, so those keep only the string."""
    record = {
        **MEDIUM,
        "ingredients": [
            {
                "preferred_term": "Glucose",
                "term": {"id": "CHEBI:17234"},
                "concentration": {"value": raw, "unit": "G_PER_L"},
            },
        ],
    }
    edge = next(e for e in transform(record) if e["predicate"] == "biolink:has_part")
    assert edge["value"] is None and edge["unit"] is None
    assert edge["qualifiers"][0]["qualifier_value"] == f"{raw} G_PER_L"


# --- nested solutions (#441) -------------------------------------------------

VITAMINS_A = {
    "preferred_term": "Vitamin solution",
    "concentration": {"value": "1", "unit": "ML_PER_L"},
    "composition": [{"preferred_term": "Biotin", "term": {"id": "CHEBI:15956"}}],
}
VITAMINS_B = {
    "preferred_term": "Vitamin solution",
    "concentration": {"value": "1", "unit": "ML_PER_L"},
    "composition": [{"preferred_term": "Thiamine", "term": {"id": "CHEBI:18385"}}],
}


def _with_solutions(record_id, *solutions):
    return {
        "id": record_id,
        "name": "Canary",
        "medium_type": "DEFINED",
        "solutions": list(solutions),
    }


def test_two_nested_solutions_with_one_name_and_different_reagents_are_different_nodes():
    """The union node: `Vitamin solution` carried 15 compositions under one id."""
    a, _ = nested_solution_target(VITAMINS_A)
    b, _ = nested_solution_target(VITAMINS_B)
    assert a != b
    assert a.startswith("CultureMech:solution_Vitamin_solution_") and b.startswith(
        "CultureMech:solution_Vitamin_solution_"
    )


def test_one_stock_shared_by_two_media_is_one_node():
    """Same name, same reagents: one stock, one node, one composition (#312)."""
    a, _ = nested_solution_target(VITAMINS_A)
    b, _ = nested_solution_target(dict(VITAMINS_A))
    assert a == b


def test_footnote_marked_names_are_kept_apart_when_their_reagents_differ():
    """MediaDive's `Vitamin solution*` and `**` are two stocks; the sanitizer drops
    the asterisks, so the composition has to keep them apart."""
    star = {**VITAMINS_A, "preferred_term": "Vitamin solution*"}
    star2 = {**VITAMINS_B, "preferred_term": "Vitamin solution**"}
    assert nested_solution_target(star)[0] != nested_solution_target(star2)[0]


def test_a_nested_solution_naming_a_record_links_to_it_and_mints_nothing():
    ref = {
        "preferred_term": "SES",
        "culturemech_term": {"id": "CultureMech:000130", "label": "SES"},
    }
    record = _with_solutions("CultureMech:900201", ref)
    assert nested_solution_target(ref) == ("CultureMech:000130", False)
    assert not any(n["id"].startswith("CultureMech:solution_") for n in nodes(record))
    link = [e for e in transform(record) if e["object"] == "CultureMech:000130"]
    assert len(link) == 1 and link[0]["subject"] == "CultureMech:900201"


def test_an_upstream_solution_id_resolves_to_the_record_that_carries_it(tmp_path, monkeypatch):
    """The 1,228 `mediadive.solution:` references; none carries a composition of
    its own, so the record's exported composition (#442) is the depth."""
    records = tmp_path / "bacterial"
    records.mkdir()
    (records / "sol.yaml").write_text(
        "id: CultureMech:900301\npreferred_term: SL10 elements\nterm:\n  id: mediadive.solution:4367\n"
        "  label: SL10 elements\ncomposition:\n- preferred_term: ZnSO4\n  term:\n    id: CHEBI:32312\n"
    )
    monkeypatch.setenv(RECORDS_DIR_ENV, str(tmp_path))
    _solution_record_index.cache_clear()
    try:
        ref = {"preferred_term": "SL10 elements", "term": {"id": "mediadive.solution:4367"}}
        assert nested_solution_target(ref) == ("CultureMech:900301", False)
        record = _with_solutions("CultureMech:900302", ref)
        assert not any(n["id"].startswith("CultureMech:solution_") for n in nodes(record))
        objects = [e["object"] for e in transform(record) if e["subject"] == "CultureMech:900302"]
        assert "CultureMech:900301" in objects
        # and an id the index does not know is minted as before
        unknown = {"preferred_term": "Other", "term": {"id": "mediadive.solution:1"}}
        assert nested_solution_target(unknown)[1] is True
    finally:
        _solution_record_index.cache_clear()


def test_without_a_records_dir_the_index_is_empty_and_everything_is_minted(monkeypatch):
    monkeypatch.delenv(RECORDS_DIR_ENV, raising=False)
    _solution_record_index.cache_clear()
    try:
        assert _solution_record_index() == {}
        ref = {"preferred_term": "SL10 elements", "term": {"id": "mediadive.solution:4367"}}
        assert nested_solution_target(ref)[1] is True
    finally:
        _solution_record_index.cache_clear()


def test_a_minted_nested_solution_still_exports_its_composition():
    record = _with_solutions("CultureMech:900401", VITAMINS_A)
    target, minted = nested_solution_target(VITAMINS_A)
    assert minted
    assert any(n["id"] == target for n in nodes(record))
    assert any(
        e["subject"] == target and e["predicate"] == "biolink:has_part" for e in transform(record)
    )
