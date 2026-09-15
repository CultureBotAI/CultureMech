"""Semantic adapter behavior, corpus boundaries, identity and atomic refusal."""

import copy
import hashlib
import json
from pathlib import Path

import pytest
import yaml

from culturemech import text_map_inputs as adapter

SOURCE = "data/normalized_yaml/bacterial/example.yaml"
RECORD = {
    "id": "CultureMech:000001",
    "name": "Example medium",
    "category": "bacterial",
    "description": "Grows anaerobic bacteria",
    "ingredients": [
        {"preferred_term": "Glucose", "concentration": {"value": "5", "unit": "G_PER_L"}}
    ],
}
LABEL_FIELD = "name"
PAGE = "normalized/000001.html"


def fixture_tree(root):
    for directory in adapter.RECORD_ROOTS:
        (root / directory).mkdir(parents=True, exist_ok=True)
    path = root / SOURCE
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(yaml.safe_dump(RECORD))
    if adapter.ADAPTER_VERSION.startswith("traitmech-"):
        parent = path.with_name("parent.yaml")
        parent.write_text(
            yaml.safe_dump(
                {
                    "identifier": "METPO:parent",
                    "label": "Resolved parent",
                    "trait_category": "ECOLOGY",
                }
            )
        )
    return path


def test_exact_contract_and_semantic_digest_ignores_provenance(tmp_path):
    path = fixture_tree(tmp_path)
    row = next(adapter.iter_inputs(tmp_path, records=[SOURCE]))
    assert set(row) == {
        "identifier",
        "label",
        "category",
        "page",
        "source_path",
        "text",
        "text_sha256",
        "adapter_version",
    }
    assert row["page"] == PAGE
    assert row["source_path"] == SOURCE
    assert row["text_sha256"] == hashlib.sha256(row["text"].encode("utf-8")).hexdigest()
    assert "REJECTED_SENTINEL" not in row["text"]
    record = copy.deepcopy(RECORD)
    record.update(
        {
            "curation_history": [{"notes": "PRIVATE_PROVENANCE_SENTINEL"}],
            "references": [{"reference": "PMID:999999"}],
            "evidence": [{"snippet": "PRIVATE_PROVENANCE_SENTINEL"}],
            "notes": "PRIVATE_PROVENANCE_SENTINEL",
        }
    )
    path.write_text(yaml.safe_dump(record))
    unchanged = next(adapter.iter_inputs(tmp_path, records=[SOURCE]))
    assert unchanged["text_sha256"] == row["text_sha256"]
    assert "PRIVATE_PROVENANCE_SENTINEL" not in unchanged["text"]
    record[LABEL_FIELD] = "A different biological entity"
    path.write_text(yaml.safe_dump(record))
    changed = next(adapter.iter_inputs(tmp_path, records=[SOURCE]))
    assert changed["text_sha256"] != row["text_sha256"]


def test_canary_and_full_keep_identical_semantics(tmp_path):
    fixture_tree(tmp_path)
    full = list(adapter.iter_inputs(tmp_path))
    subset = list(adapter.iter_inputs(tmp_path, records=[SOURCE]))
    assert subset[0] == next(row for row in full if row["source_path"] == SOURCE)
    if adapter.ADAPTER_VERSION.startswith("traitmech-"):
        assert "Resolved parent" in subset[0]["text"]
        assert "METPO:parent" not in subset[0]["text"]
    result = adapter.export_inputs(tmp_path, tmp_path / "records.jsonl", limit=1)
    assert result["records"] == 1 and result["scope"] == "subset"
    result = adapter.export_inputs(tmp_path, None)
    assert result["records"] == len(full) and result["scope"] == "full"


def test_atomic_failure_preserves_previous_output(tmp_path):
    path = fixture_tree(tmp_path)
    output = tmp_path / "records.jsonl"
    output.write_text("previous output")
    broken = path.with_name("zz_broken.yaml")
    broken.write_text("not: [valid YAML")
    with pytest.raises(yaml.YAMLError):
        adapter.export_inputs(tmp_path, output)
    assert output.read_text() == "previous output"
    assert not list(tmp_path.glob(".text-map-*"))


def test_selection_cannot_escape_or_repeat(tmp_path):
    fixture_tree(tmp_path)
    for selection in (["../outside.yaml"], [SOURCE, SOURCE]):
        with pytest.raises(ValueError):
            list(adapter.iter_inputs(tmp_path, records=selection))
    with pytest.raises(ValueError, match="positive"):
        list(adapter.iter_inputs(tmp_path, limit=0))


def test_symlinked_yaml_is_refused(tmp_path):
    path = fixture_tree(tmp_path)
    alias = path.with_name("alias.yaml")
    alias.symlink_to(path)
    with pytest.raises(ValueError, match="symlink"):
        list(adapter.iter_inputs(tmp_path))


def test_export_round_trip_and_map_sibling_route(tmp_path):
    from urllib.parse import urljoin

    fixture_tree(tmp_path)
    output = tmp_path / "output.jsonl"
    receipt = adapter.export_inputs(tmp_path, output, records=[SOURCE])
    row = json.loads(output.read_text())
    assert receipt["jsonl_sha256"] == hashlib.sha256(output.read_bytes()).hexdigest()
    assert Path(row["source_path"]).suffix == ".yaml"
    assert (
        urljoin("https://example.test/deployment/text-map/index.html", "../" + row["page"])
        == "https://example.test/deployment/" + PAGE
    )


def test_solution_components_and_scoped_targets_exclude_range_provenance():
    record = {
        "id": "CultureMech:123",
        "media_term": {"preferred_term": "Vitamin solution"},
        "composition": [
            {"preferred_term": "Biotin", "concentration": {"value": 1, "unit": "MG_PER_L"}}
        ],
        "ph_range": {"min": 6, "max": 7, "notes": "PROVENANCE_SENTINEL", "evidence": ["PMID:1"]},
        "target_organisms": [
            {"preferred_term": "Example organism", "scoped_to_variant": "low salt"}
        ],
    }
    text = adapter.semantic_text(record)
    assert "name: Vitamin solution" in text
    assert "solution component: Biotin" in text
    assert "concentration: 1 mg per l" in text
    assert "ph range min: 6" in text and "ph range max: 7" in text
    assert "target organism for variant low salt: Example organism" in text
    assert "PROVENANCE_SENTINEL" not in text and "PMID:1" not in text
