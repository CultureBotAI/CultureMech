"""Consolidation must neither invent a formulation nor discard its evidence."""

import json
import sys
from copy import deepcopy

import pytest
import yaml

from culturemech.merge import merge_recipes as cli
from culturemech.merge.formulation import FormulationFingerprinter, merge_formulation_evidence
from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merger import RecipeMerger


def medium():
    return {
        "name": "Synthetic medium",
        "ingredients": [
            {"preferred_term": "Salt", "concentration": {"value": "1", "unit": "G_PER_L"}}
        ],
        "solutions": [
            {
                "preferred_term": "Stock",
                "culturemech_term": {"id": "CultureMech:000001", "label": "Synthetic stock"},
                "concentration": {"value": "1", "unit": "ML_PER_L"},
                "composition": [],
            }
        ],
    }


def write_records(tmp_path, records):
    paths = []
    for i, record in enumerate(records):
        path = tmp_path / f"recipe{i}.yaml"
        path.write_text(yaml.safe_dump(record), encoding="utf-8")
        paths.append(path)
    return paths


@pytest.mark.parametrize("difference", ["amount", "stock"])
@pytest.mark.parametrize("supply_candidate_fingerprint", [False, True])
def test_candidate_similarity_cannot_authorize_merge(
    tmp_path, difference, supply_candidate_fingerprint
):
    left = medium()
    right = deepcopy(left)
    if difference == "amount":
        right["ingredients"][0]["concentration"]["value"] = "2"
    else:
        right["solutions"][0]["culturemech_term"]["id"] = "CultureMech:000002"
    paths = write_records(tmp_path, [left, right])
    groups = RecipeMatcher().group_recipes(paths)
    assert list(groups.values()) == [paths]
    fingerprint = next(iter(groups)) if supply_candidate_fingerprint else None
    before = [p.read_bytes() for p in paths]
    with pytest.raises(ValueError, match="formulation"):
        RecipeMerger().merge_group(paths, fingerprint=fingerprint)
    assert [p.read_bytes() for p in paths] == before


def test_exact_merge_keeps_every_evidence_location_and_root_provenance(tmp_path):
    records = [medium(), medium()]
    for i, record in enumerate(records):
        evidence = {
            "reference": f"https://example.org/source/{i}",
            "snippet": f"Synthetic quote {i}",
        }
        record["evidence"] = [evidence]
        record["references"] = [{"reference": evidence["reference"], "title": f"Source {i}"}]
        record["curation_history"] = [
            {"timestamp": f"2026-01-0{i + 1}", "curator": "test", "action": "Source checked"}
        ]
        record["ingredients"][0]["evidence"] = [evidence]
        record["solutions"][0]["composition"] = [
            {"preferred_term": "Stock salt", "evidence": [evidence]}
        ]
        record["solutions"][0]["solutions"] = [
            {
                "preferred_term": "Nested stock",
                "composition": [{"preferred_term": "Nested salt", "evidence": [evidence]}],
            }
        ]
    paths = write_records(tmp_path, records)
    merged = RecipeMerger().merge_group(paths)
    for record in records:
        for field in ("evidence", "references", "curation_history"):
            assert all(entry in merged[field] for entry in record[field])
        assert record["evidence"][0] in merged["ingredients"][0]["evidence"]
        assert record["evidence"][0] in merged["solutions"][0]["composition"][0]["evidence"]
        assert (
            record["evidence"][0]
            in merged["solutions"][0]["solutions"][0]["composition"][0]["evidence"]
        )
    assert (
        merged["ingredients"][0]["concentration"] == records[0]["ingredients"][0]["concentration"]
    )


def test_merger_does_not_mutate_loaded_records(tmp_path, monkeypatch):
    records = [medium(), medium()]
    records[0]["curation_history"] = [{"curator": "test", "action": "Original"}]
    before = deepcopy(records)
    paths = write_records(tmp_path, records)
    merger = RecipeMerger()
    monkeypatch.setattr(merger, "_load_recipe", lambda path: records[paths.index(path)])
    merger.merge_group(paths)
    assert records == before


@pytest.mark.parametrize(
    "field,value",
    [
        ("concentration", {"value": "2", "unit": "G_PER_L"}),
        ("concentration", {"value": "1", "unit": "ML_PER_L"}),
        ("concentration", {"value": "1", "unit": "G_PER_L", "per_volume": "500 ml"}),
        ("concentration", {"value": "0", "unit": "G_PER_L"}),
        ("notes", "Source mass, not a final-volume concentration"),
        ("term", {"id": "CHEBI:12345"}),
        ("chemical_formula", "Synthetic hydrate identity"),
        ("future_scientific_field", "Must not be silently discarded"),
    ],
)
def test_all_ingredient_assertions_remain_significant(field, value):
    left = medium()
    right = deepcopy(left)
    right["ingredients"][0][field] = value
    fingerprinter = FormulationFingerprinter()
    assert fingerprinter.fingerprint(left) != fingerprinter.fingerprint(right)
    with pytest.raises(ValueError, match="formulation"):
        merge_formulation_evidence([left, right])


@pytest.mark.parametrize(
    "field,value",
    [
        ("ph_value", 7.0),
        ("temperature_value", 37),
        ("physical_state", "SOLID"),
        ("notes", "Use a different source version"),
        ("preparation_steps", [{"description": "Boil"}]),
        ("import_metadata", {"source_id": "different"}),
        ("source_data", {"source": "different"}),
        ("variant_modifications", ["Supplement added"]),
        ("target_organisms", [{"preferred_term": "Synthetic"}]),
    ],
)
def test_root_context_is_not_dropped(field, value):
    left = medium()
    right = deepcopy(left)
    right[field] = value
    assert FormulationFingerprinter().fingerprint(left) != FormulationFingerprinter().fingerprint(
        right
    )


def test_nested_stock_stage_and_missing_amount_are_significant():
    left = medium()
    left["solutions"][0]["composition"] = deepcopy(left["ingredients"])
    right = deepcopy(left)
    del right["solutions"][0]["composition"][0]["concentration"]
    assert FormulationFingerprinter().fingerprint(left) != FormulationFingerprinter().fingerprint(
        right
    )
    right = deepcopy(left)
    right["ingredients"] += right["solutions"][0].pop("composition")
    assert FormulationFingerprinter().fingerprint(left) != FormulationFingerprinter().fingerprint(
        right
    )


def test_order_is_preserved_to_keep_evidence_index_references_valid():
    left = medium()
    left["ingredients"].append({"preferred_term": "Second ingredient"})
    right = deepcopy(left)
    right["ingredients"].reverse()
    with pytest.raises(ValueError, match="formulation"):
        merge_formulation_evidence([left, right])


def test_hydrate_names_remain_significant_even_with_shared_grounding():
    left = medium()
    left["ingredients"][0].update(preferred_term="Salt.2H2O", term={"id": "CHEBI:12345"})
    right = deepcopy(left)
    right["ingredients"][0]["preferred_term"] = "Salt.7H2O"
    assert FormulationFingerprinter().fingerprint(left) != FormulationFingerprinter().fingerprint(
        right
    )


def test_identical_evidence_is_not_duplicated_and_distinct_quotes_survive():
    left = medium()
    left["ingredients"][0]["evidence"] = [
        {"reference": "https://example.org", "snippet": "Quote A"}
    ]
    right = deepcopy(left)
    right["ingredients"][0]["evidence"].append(
        {"reference": "https://example.org", "snippet": "Quote B"}
    )
    result = merge_formulation_evidence([left, right, left])
    assert result["ingredients"][0]["evidence"] == right["ingredients"][0]["evidence"]
    result["ingredients"][0]["evidence"][0]["snippet"] = "Result mutation"
    assert left["ingredients"][0]["evidence"][0]["snippet"] == "Quote A"


@pytest.mark.parametrize("field", ["evidence", "references", "curation_history", "sources"])
def test_malformed_provenance_is_rejected(field):
    record = medium()
    record[field] = {"not": "a list"}
    with pytest.raises(ValueError, match="must be a list"):
        FormulationFingerprinter().fingerprint(record)


def test_cycles_are_rejected_but_shared_aliases_are_valid():
    record = medium()
    record["solutions"].append(record["solutions"][0])
    assert FormulationFingerprinter().fingerprint(record)
    record["extra_context"] = record
    with pytest.raises(ValueError, match="Cyclic"):
        FormulationFingerprinter().fingerprint(record)


def test_file_signature_does_not_rewrite_literal_escape_sequences(tmp_path):
    record = medium()
    record["notes"] = r"Literal source text \x41"
    path = write_records(tmp_path, [record])[0]
    fp = FormulationFingerprinter()
    assert fp.fingerprint_file(path) == fp.fingerprint(record)


def test_supplied_fingerprint_is_not_trusted(tmp_path):
    paths = write_records(tmp_path, [medium()])
    with pytest.raises(ValueError, match="fingerprint"):
        RecipeMerger().merge_group(paths, fingerprint="unverified")


def test_cli_splits_variants_and_preserves_exact_duplicate_evidence(tmp_path, monkeypatch):
    inputs = tmp_path / "normalized" / "bacterial"
    inputs.mkdir(parents=True)
    records = [medium(), medium(), medium()]
    records[1]["ingredients"][0]["evidence"] = [
        {"reference": "https://example.org", "snippet": "Synthetic"}
    ]
    records[2]["solutions"][0]["concentration"]["value"] = "2"
    paths = write_records(inputs, records)
    matcher = RecipeMatcher()
    assert len(matcher.group_recipes(paths)) == 1
    assert sorted(map(len, matcher.group_formulations(paths).values())) == [1, 2]
    outputs, stats = tmp_path / "merged", tmp_path / "stats.json"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "merge_recipes",
            "--normalized-dir",
            str(inputs.parent),
            "--output-dir",
            str(outputs),
            "--stats-file",
            str(stats),
        ],
    )
    assert cli.main() == 0
    docs = [yaml.safe_load(path.read_text()) for path in outputs.glob("*.yaml")]
    assert len(docs) == 2
    assert sorted(len(doc["merged_from"]) for doc in docs) == [1, 2]
    duplicate = next(doc for doc in docs if len(doc["merged_from"]) == 2)
    assert duplicate["ingredients"][0]["evidence"] == records[1]["ingredients"][0]["evidence"]
    assert json.loads(stats.read_text())["merge_errors"] == []


@pytest.mark.parametrize("bad_input", ["provenance", "stock", "yaml", "missing", "no_ingredients"])
def test_formulation_scan_aborts_before_any_cli_output(tmp_path, monkeypatch, bad_input):
    inputs = tmp_path / "normalized" / "bacterial"
    inputs.mkdir(parents=True)
    records = [medium(), medium()]
    if bad_input == "provenance":
        records[1]["evidence"] = {"not": "a list"}
    elif bad_input == "stock":
        records[1]["solutions"] = "not a list"
    elif bad_input == "no_ingredients":
        records[1].pop("ingredients")
    paths = write_records(inputs, records)
    if bad_input == "yaml":
        paths[1].write_text("ingredients: [", encoding="utf-8")
    elif bad_input == "missing":
        paths[1].unlink()
        monkeypatch.setattr(cli, "find_all_recipes", lambda _: paths)
    outputs, stats = tmp_path / "merged", tmp_path / "stats.json"
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "merge_recipes",
            "--normalized-dir",
            str(inputs.parent),
            "--output-dir",
            str(outputs),
            "--stats-file",
            str(stats),
        ],
    )
    with pytest.raises(ValueError, match="formulation"):
        cli.main()
    assert not outputs.exists()
    assert not stats.exists()


def test_empty_but_well_formed_medium_is_reported_as_unfingerprintable(tmp_path):
    paths = write_records(tmp_path, [{"name": "Unquantified", "ingredients": []}, medium()])
    matcher = RecipeMatcher()
    assert list(matcher.group_formulations(paths).values()) == [[paths[1]]]
    assert matcher._last_skip_stats["skipped_error"] == 1
