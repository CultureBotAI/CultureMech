"""End-to-end tests for the KGX TSV export (#294).

`tests/test_kgx_export.py` covers the pure `transform()` function, which is why
three defects survived in the surrounding pipeline for as long as they did:

1. `just kgx-export` ran `uv run koza` without `--extra koza`, and passed a
   Python file where koza 2.x expects a configuration YAML. It had never run.
2. It asked for `-f jsonl`, so no TSV pair was ever produced.
3. The transform emitted edges only, so all six `culturemech:`-minted id shapes
   were dangling references.

Running it once surfaced a fourth, worse defect: biolink's
`Association.qualifiers` is `list[str] | None`, so `Association(**edge_dict)`
raised for every qualified edge and the wrapper swallowed it with a `print`. A
249-record canary produced **10** edges instead of 1,937.

These tests therefore drive the real koza runner over fixture records and assert
on the files on disk. They are the only coverage of the path that actually ships.
"""
from __future__ import annotations

import csv
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "scripts"))

pytest.importorskip("koza", reason="koza is an optional extra; run with --extra koza")

from culturemech.export.kgx_export import (  # noqa: E402
    _QUALIFIER_COLUMNS,
    Edge,
    nodes,
    to_edge,
    transform,
)

RECORD = {
    "name": "Canary Medium",
    "medium_type": "COMPLEX",
    "physical_state": "LIQUID",
    "applications": ["Microbial cultivation"],
    "ingredients": [
        {
            "preferred_term": "Glucose",
            "term": {"id": "CHEBI:17234"},
            "concentration": {"value": "10", "unit": "G_PER_L"},
            "nutritional_roles": ["CARBON_SOURCE"],
        }
    ],
    "target_organisms": [
        {"preferred_term": "Escherichia coli", "term": {"id": "NCBITaxon:562"},
         "strain": "K-12"}
    ],
    "solutions": [
        {"preferred_term": "Trace Elements",
         "concentration": {"value": "1", "unit": "ML_PER_L"},
         "composition": [{"preferred_term": "ZnSO4", "term": {"id": "CHEBI:32312"}}]}
    ],
    "variants": [{"name": "Canary Medium agar"}],
}

DEFINED_RECORD = {"name": "Defined Canary", "medium_type": "DEFINED",
                  "physical_state": "LIQUID"}


# --- qualifier flattening -------------------------------------------------


def test_every_qualifier_type_the_transform_emits_has_a_column():
    """The defect that dropped 99% of edges, in its general form.

    A qualifier type with no column is data the TSV cannot carry. Scanning the
    transform's real output beats hand-listing types, because the failure mode is
    someone adding a qualifier and not noticing this table.
    """
    emitted = {
        q["qualifier_type_id"]
        for record in (RECORD, DEFINED_RECORD)
        for edge in transform(record)
        for q in edge.get("qualifiers") or []
    }
    assert emitted, "fixture must exercise qualifiers or this test proves nothing"
    assert emitted <= set(_QUALIFIER_COLUMNS), (
        f"no TSV column for {emitted - set(_QUALIFIER_COLUMNS)}"
    )


def test_qualifier_values_survive_the_conversion_to_a_row():
    edge = next(
        e for e in transform(RECORD)
        if e["object"] == "CHEBI:17234" and e["predicate"] == "biolink:has_part"
    )
    row = to_edge(edge)
    assert row.concentration == "10 G_PER_L"
    assert row.role == "CARBON_SOURCE"


def test_an_unknown_qualifier_type_is_dropped_not_misfiled():
    row = to_edge({
        "id": "urn:uuid:x", "subject": "a", "predicate": "p", "object": "b",
        "qualifiers": [{"qualifier_type_id": "biolink:invented",
                        "qualifier_value": "v"}],
    })
    assert row.concentration is None and row.role is None


def test_edge_is_not_a_biolink_association():
    """Pins why. `Association.qualifiers` is `list[str] | None`, so routing these
    dicts through it raises and — with the old except-and-print — dropped the
    edge silently."""
    from biolink_model.datamodel.pydanticmodel_v2 import Association

    with pytest.raises(Exception):
        Association(
            id="urn:uuid:x", subject="a", predicate="p", object="b",
            qualifiers=[{"qualifier_type_id": "biolink:concentration",
                         "qualifier_value": "10 G_PER_L"}],
        )
    assert isinstance(to_edge(next(iter(transform(RECORD)))), Edge)


# --- node declaration -----------------------------------------------------


def test_medium_and_type_categories_follow_the_consumer():
    """kg-microbe fixes these in transform_utils/constants.py; a medium node the
    loader does not recognise is worse than no node."""
    by_id = {n["id"]: n for n in nodes(RECORD)}
    assert by_id["culturemech:Canary_Medium"]["category"] == [
        "biolink:GrowthMedium", "biolink:ComplexMolecularMixture"
    ]
    assert by_id["culturemech:medium_type_COMPLEX"]["category"] == [
        "biolink:ComplexMolecularMixture"
    ]

    defined = {n["id"]: n for n in nodes(DEFINED_RECORD)}
    assert defined["culturemech:Defined_Canary"]["category"] == [
        "biolink:GrowthMedium", "biolink:ChemicalMixture"
    ]
    assert defined["culturemech:medium_type_DEFINED"]["category"] == [
        "biolink:ChemicalMixture"
    ]


def test_a_medium_type_outside_the_table_falls_back_rather_than_guessing():
    """BUFFER and NEGATIVE_CONTROL assert nothing about composition."""
    buffer_nodes = {n["id"]: n for n in nodes({"name": "B", "medium_type": "BUFFER"})}
    assert buffer_nodes["culturemech:B"]["category"] == ["biolink:GrowthMedium"]
    assert buffer_nodes["culturemech:medium_type_BUFFER"]["category"] == [
        "biolink:ChemicalMixture"
    ]


def test_only_minted_ids_get_nodes():
    """Ontology terms come from KG-Microbe's ontology ingests, which carry the
    authoritative labels. Minting name-less rows for them here would put a
    competing node into the merge."""
    ids = {n["id"] for n in nodes(RECORD)}
    assert all(i.startswith("culturemech:") for i in ids)
    assert not any(i.startswith(("CHEBI:", "NCBITaxon:")) for i in ids)


def test_ids_survive_kozas_asymmetric_sanitization():
    r'''The two dangling references the full-corpus run produced.

    `TOGO_M1572_Ekho_Lake_Strains_Medium.yaml` carries the solution name
    `Mineral salt solution* (\"Hutner/Cohen-Bazire\")` — the backslash-quotes are
    literal in the record. Koza's `trim()` strips the two-character sequence `\"`
    from every edge column, but `TSVWriter.write_row` restores a node's `id` from
    the raw record and bypasses that, so the same solution was spelled two ways:

        node: culturemech:solution_Mineral_salt_solution*_\"Hutner_Cohen-Bazire\"
        edge: culturemech:solution_Mineral_salt_solution*_Hutner_Cohen-Bazire

    Stripping the characters at the source makes both sides agree no matter what
    koza does downstream.
    '''
    from culturemech.export.kgx_export import _create_solution_id, _sanitize_id

    assert _sanitize_id(r'Mineral salt solution* (\"Hutner/Cohen-Bazire\")') == (
        "Mineral_salt_solution_Hutner_Cohen-Bazire"
    )
    for char in '\\"*()':
        assert char not in _create_solution_id(f'R2A Broth {char}DAIGO{char}')

    # Dropping a character must not leave a doubled or trailing separator behind.
    assert _sanitize_id("Test (variant)") == "Test_variant"
    assert _sanitize_id("A  /  B") == "A_B"

    # The colon is the CURIE delimiter, so a name carrying one produced a
    # two-colon id that any consumer splitting on `:` reads wrongly. 19 in the
    # corpus, e.g. `Solution A:` -> `culturemech:solution_Solution_A:`.
    assert _create_solution_id("Solution A:") == "culturemech:solution_Solution_A"
    assert _create_solution_id("Solution A:").count(":") == 1
    # Mapped to `_`, not dropped, so two words are not welded together.
    assert _sanitize_id("growth on sulfate:Add 13.9 g") == "growth_on_sulfate_Add_13.9_g"

    # And the medium id goes through the same sanitizer as the solution id --
    # before the fix it only replaced spaces, so a quoted medium name would drift
    # exactly the same way.
    quoted = {n["id"] for n in nodes({'name': r'Foo \"Bar\"', "medium_type": "COMPLEX"})}
    edge_subjects = {
        e["subject"] for e in transform({'name': r'Foo \"Bar\"', "medium_type": "COMPLEX"})
    }
    assert edge_subjects <= quoted


def test_a_record_with_no_name_mints_nothing():
    """`culturemech:` alone would be a garbage node bound to every unnamed record."""
    assert list(nodes({"medium_type": "COMPLEX"})) == []


# --- the koza path, end to end -------------------------------------------


@pytest.fixture
def exported(tmp_path: Path) -> tuple[list[dict], list[dict]]:
    """Run the real koza runner over fixture records; return (nodes, edges)."""
    import export_kgx
    import yaml

    records_dir = tmp_path / "records" / "canary"
    records_dir.mkdir(parents=True)
    for i, record in enumerate((RECORD, DEFINED_RECORD)):
        (records_dir / f"record_{i}.yaml").write_text(yaml.safe_dump(record))

    out = tmp_path / "out"
    export_kgx.run(tmp_path / "records", out)

    def read(kind: str) -> list[dict]:
        with (out / f"culturemech_{kind}.tsv").open() as fh:
            return list(csv.DictReader(fh, delimiter="\t"))

    return read("nodes"), read("edges")


# Two media referencing ONE stock solution — the #312 shape. On the real corpus
# `Seven vitamins solution` is referenced by 178 media.
SHARED_SOLUTION = {
    "preferred_term": "Seven vitamins solution",
    "concentration": {"value": "1", "unit": "ML_PER_L"},
    "composition": [
        {"preferred_term": "Biotin", "term": {"id": "CHEBI:15956"}},
        {"preferred_term": "Nicotinic acid", "term": {"id": "CHEBI:15940"}},
    ],
}


@pytest.fixture
def exported_shared(tmp_path: Path) -> tuple[list[dict], list[dict]]:
    """Two media that reference the same stock solution."""
    import export_kgx
    import yaml

    records_dir = tmp_path / "records" / "canary"
    records_dir.mkdir(parents=True)
    for i, name in enumerate(("Medium One", "Medium Two")):
        (records_dir / f"record_{i}.yaml").write_text(yaml.safe_dump({
            "name": name, "medium_type": "COMPLEX",
            "solutions": [SHARED_SOLUTION],
        }))

    out = tmp_path / "out"
    export_kgx.run(tmp_path / "records", out)

    def read(kind: str) -> list[dict]:
        with (out / f"culturemech_{kind}.tsv").open() as fh:
            return list(csv.DictReader(fh, delimiter="\t"))

    return read("nodes"), read("edges")


def test_the_export_writes_a_node_and_edge_tsv_pair(exported):
    node_rows, edge_rows = exported
    assert node_rows and edge_rows


def test_no_culturemech_id_in_the_edges_dangles(exported):
    """The #294 acceptance criterion. Verified on the real corpus too: the
    249-record algae canary produced 259 nodes and 259 referenced ids, 0 dangling
    and 0 unused."""
    node_rows, edge_rows = exported
    declared = {n["id"] for n in node_rows}
    referenced = {
        end for e in edge_rows for end in (e["subject"], e["object"])
        if end.startswith("culturemech:")
    }
    assert referenced - declared == set()


def test_ontology_ids_are_referenced_but_not_declared(exported):
    node_rows, edge_rows = exported
    declared = {n["id"] for n in node_rows}
    referenced = {end for e in edge_rows for end in (e["subject"], e["object"])}
    external = {r for r in referenced if not r.startswith("culturemech:")}
    assert external, "fixture must reference ontology terms"
    assert external & declared == set()


def test_qualified_edges_reach_the_tsv(exported):
    """The regression guard: before the fix this file held 10 rows for 249
    records, because every qualified edge raised and was swallowed."""
    _node_rows, edge_rows = exported
    assert any(e["concentration"] for e in edge_rows)
    assert any(e["role"] for e in edge_rows)
    assert any(e["strain"] for e in edge_rows)


def test_shared_edges_are_written_once(exported_shared):
    """A stock solution's composition belongs to the solution, not to each medium.

    `transform()` walks every record's `solutions[]`, so a shared solution
    re-emitted its whole composition once per referencing medium. `Seven vitamins
    solution` is referenced by 178 media, so each of its `has_part` edges appeared
    178 times — 45,464 surplus rows, 23% of the file (#312).

    Every collision was an exact duplicate triple, so keeping the first loses
    nothing: on the real corpus, distinct edges before and after are both 153,372.

    Uses `exported_shared` deliberately. Against the plain `exported` fixture this
    assertion is vacuous — those two records share no solution, so no duplicate
    can arise and the test passes with the dedup removed. Verified by reverting
    the fix: only the shared-solution fixtures fail.
    """
    _node_rows, edge_rows = exported_shared
    ids = [e["id"] for e in edge_rows]
    assert len(ids) == len(set(ids)), "duplicate edge id in the edges file"

    triples = [(e["subject"], e["predicate"], e["object"]) for e in edge_rows]
    assert len(triples) == len(set(triples))
    # ...and the id really is a function of the triple, which is what makes
    # deduplicating on the id safe.
    assert len(set(ids)) == len(set(triples))


def test_a_solution_shared_by_two_media_emits_its_composition_once(exported_shared):
    """The #312 shape itself, not just the absence of duplicates."""
    _node_rows, edge_rows = exported_shared
    composition = [e for e in edge_rows
                   if e["subject"].startswith("culturemech:solution_")
                   and e["predicate"] == "biolink:has_part"]
    assert composition, "fixture must reference a shared solution"
    assert len(composition) == len({e["id"] for e in composition})
    # Both media still get their own medium -> solution edge: that one IS
    # per-medium and must not be collapsed.
    to_solution = [e for e in edge_rows
                   if e["object"].startswith("culturemech:solution_")
                   and e["predicate"] == "biolink:has_part"]
    assert len(to_solution) == 2, to_solution


def test_shared_nodes_are_written_once(exported):
    """Both fixture records are LIQUID. Without run-scoped dedup, a shared node
    would appear once per record — 8,850 rows for medium_type_COMPLEX alone."""
    node_rows, _edge_rows = exported
    ids = [n["id"] for n in node_rows]
    assert len(ids) == len(set(ids))
    assert "culturemech:state_liquid" in ids


def test_a_second_run_in_the_same_process_repeats_the_output(tmp_path):
    """The node-dedup set is run-scoped, so a second run must not come up empty.

    This pins the *invariant*, not the mechanism. Today it holds because koza
    loads the transform with `spec_from_file_location` "without touching
    sys.modules", giving each run a fresh module and a fresh set — so the
    driver's old `reset_node_dedup()` call was clearing an unrelated copy of the
    module and protecting nothing. If koza ever caches transform modules, this
    test fails and `reset_node_dedup()` becomes the fix.
    """
    import yaml

    import export_kgx

    records_dir = tmp_path / "records" / "canary"
    records_dir.mkdir(parents=True)
    (records_dir / "a.yaml").write_text(yaml.safe_dump(RECORD))

    first = export_kgx.run(tmp_path / "records", tmp_path / "out1")
    second = export_kgx.run(tmp_path / "records", tmp_path / "out2")

    assert first == second
    assert first[0] > 0
    assert (tmp_path / "out1" / "culturemech_nodes.tsv").read_text() == (
        tmp_path / "out2" / "culturemech_nodes.tsv"
    ).read_text()


def test_an_empty_corpus_fails_loudly(tmp_path):
    """A silent empty export is the failure mode #294 was about."""
    import export_kgx

    (tmp_path / "records" / "empty").mkdir(parents=True)
    with pytest.raises(SystemExit, match="No record YAMLs"):
        export_kgx.run(tmp_path / "records", tmp_path / "out")
