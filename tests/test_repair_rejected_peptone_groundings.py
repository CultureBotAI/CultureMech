"""Rejected identities must disappear from source recipes and their exports (#484)."""

from __future__ import annotations

import copy
import hashlib
import importlib
import json
from types import SimpleNamespace

import pytest
import repair_rejected_peptone_groundings as repair
import yaml

from culturemech.export.kgx_export import ingredient_to_edge
from culturemech.ingredients.mim_label_index import resolve_ingredient

TIMESTAMP = "2026-09-21T00:00:00+00:00"


def _text(name="Trypticase", old="CHEBI:78018", *, solution=False):
    ingredient = {
        "preferred_term": name,
        "concentration": {"value": "2", "unit": "G_PER_L"},
        "term": {"id": old, "label": "rejected identity"},
    }
    if solution:
        ingredient["chebi_term"] = ingredient["term"]
        ingredient["term"] = {"id": "mediadive.compound:74", "label": name}
        ingredient["chebi_term"].update(confidence=0.7, match_type="corpus_consensus")
    doc = {
        "id": "CultureMech:999999",
        "composition" if solution else "ingredients": [ingredient],
        "curation_history": [{"timestamp": TIMESTAMP, "notes": f"Historical {old}"}],
        "notes": "keep original source notes",
    }
    return "# Keep this comment\n" + yaml.safe_dump(doc, sort_keys=False)


@pytest.mark.parametrize(
    "name,old,target,label",
    [
        ("Trypticase", "CHEBI:78018", "MICRO:0000175", "Trypticase peptone"),
        ("Bacto-tryptone", "CHEBI:78018", "MICRO:0000182", "tryptone"),
        ("Peptone", "FOODON:03302071", "MICRO:0000178", "peptone"),
    ],
)
def test_corrects_identity_preserves_history_and_is_idempotent(name, old, target, label):
    before = _text(name, old)
    after, changes = repair.repair_text(before, TIMESTAMP, repair.verify_mim())
    doc = yaml.safe_load(after)
    assert after.startswith("# Keep this comment\n")
    assert doc["ingredients"][0]["term"] == {"id": target, "label": label}
    assert doc["curation_history"][:-1] == yaml.safe_load(before)["curation_history"]
    assert doc["curation_history"][-1]["action"] == repair.ACTION
    assert doc["notes"] == "keep original source notes"
    assert changes[0]["json_pointer"] == "/ingredients/0/term/id"
    assert repair.repair_text(after, TIMESTAMP, repair.verify_mim()) == (after, [])


def test_solution_keeps_source_provenance_and_exports_micro():
    before = _text(solution=True)
    after, changes = repair.repair_text(before, TIMESTAMP, repair.verify_mim())
    original = yaml.safe_load(before)["composition"][0]
    row = yaml.safe_load(after)["composition"][0]
    expected = copy.deepcopy(original)
    del expected["chebi_term"]
    assert row == expected
    decision = resolve_ingredient(row)
    assert decision.source_compound_id == "mediadive.compound:74"
    assert decision.identifier == "MICRO:0000175"
    assert ingredient_to_edge("CultureMech:999999", row)["object"] == "MICRO:0000175"
    assert changes[0]["operation"] == "remove_chebi_term"


def test_same_id_on_a_different_substance_and_history_are_untouched():
    original = _text(name="Dodecylphosphocholine")
    assert repair.repair_text(original, TIMESTAMP, repair.verify_mim()) == (original, [])


def _shared_term_text():
    return """id: CultureMech:999999
ingredients:
- preferred_term: Dodecylphosphocholine
  term: &detergent
    id: CHEBI:78018
    label: dodecylphosphocholine
- preferred_term: Trypticase
  term: *detergent
"""


def test_shared_yaml_term_cannot_modify_an_unrelated_ingredient():
    with pytest.raises(ValueError, match="(?i)alias|shared"):
        repair.repair_text(_shared_term_text(), TIMESTAMP, repair.verify_mim())


def test_unrelated_aliases_are_preserved_while_the_term_is_corrected():
    before = """id: CultureMech:999999
ingredients:
- preferred_term: Trypticase
  concentration: &amount
    value: '2'
    unit: G_PER_L
  term:
    id: CHEBI:78018
    label: rejected identity
- preferred_term: NaCl
  concentration: *amount
notes: &original_note 'Preserve this quoted note' # and its comment
description: *original_note
"""
    after, changes = repair.repair_text(before, TIMESTAMP, repair.verify_mim())
    expected_original = before.replace("id: CHEBI:78018", "id: MICRO:0000175").replace(
        "label: rejected identity", "label: Trypticase peptone"
    )
    assert after.startswith(expected_original)
    assert len(changes) == 1
    doc = yaml.safe_load(after)
    assert doc["ingredients"][0]["concentration"] is doc["ingredients"][1]["concentration"]
    assert doc["ingredients"][1] == yaml.safe_load(before)["ingredients"][1]
    assert doc["notes"] == doc["description"] == "Preserve this quoted note"


def test_shared_history_sequence_cannot_receive_an_unreviewed_event():
    before = _text().replace("curation_history:\n", "curation_history: &history\n")
    before += "source_history_snapshot: *history\n"
    with pytest.raises(ValueError, match="(?i)alias|shared"):
        repair.repair_text(before, TIMESTAMP, repair.verify_mim())


def test_shared_id_scalar_cannot_change_a_separate_term():
    before = """id: CultureMech:999999
ingredients:
- preferred_term: Dodecylphosphocholine
  term:
    id: &detergent_id CHEBI:78018
    label: dodecylphosphocholine
- preferred_term: Trypticase
  term:
    id: *detergent_id
    label: rejected identity
"""
    with pytest.raises(ValueError, match="(?i)alias|shared"):
        repair.repair_text(before, TIMESTAMP, repair.verify_mim())


def test_shared_ingredient_ancestor_cannot_change_a_source_snapshot():
    before = """id: CultureMech:999999
ingredients:
- &ingredient
  preferred_term: Trypticase
  term:
    id: CHEBI:78018
    label: rejected identity
source_ingredient_snapshot: *ingredient
"""
    with pytest.raises(ValueError, match="(?i)alias|shared"):
        repair.repair_text(before, TIMESTAMP, repair.verify_mim())


def test_alias_in_later_record_aborts_before_writing_any_recipes(tmp_path):
    normalized = tmp_path / "normalized"
    normalized.mkdir()
    valid = normalized / "a_valid.yaml"
    shared = normalized / "z_shared.yaml"
    valid.write_text(_text())
    shared.write_text(_shared_term_text())
    originals = {path: path.read_bytes() for path in (valid, shared)}
    report = tmp_path / "audit.json"
    assert (
        repair.main(
            [
                "--normalized-dir",
                str(normalized),
                "--apply",
                "--report",
                str(report),
            ]
        )
        == 2
    )
    assert {path: path.read_bytes() for path in originals} == originals
    assert not report.exists()


def test_crlf_input_has_accurate_hashes_and_preserves_unrelated_bytes(tmp_path):
    normalized = tmp_path / "normalized"
    normalized.mkdir()
    path = normalized / "recipe.yaml"
    original = _text().replace("\n", "\r\n").encode("utf-8")
    path.write_bytes(original)
    report = tmp_path / "audit.json"
    assert (
        repair.main(
            [
                "--normalized-dir",
                str(normalized),
                "--apply",
                "--report",
                str(report),
            ]
        )
        == 0
    )
    after = path.read_bytes()
    audit = json.loads(report.read_text())
    assert audit["assignments"][0]["before_sha256"] == hashlib.sha256(original).hexdigest()
    assert audit["assignments"][0]["after_sha256"] == hashlib.sha256(after).hexdigest()
    assert after.startswith(b"# Keep this comment\r\n")
    assert b"notes: keep original source notes\r\n" in after


@pytest.mark.parametrize("mode", ["--dry-run", "--apply"])
@pytest.mark.parametrize("symlink", [False, True])
def test_report_cannot_overwrite_a_source_recipe(tmp_path, mode, symlink):
    normalized = tmp_path / "normalized"
    normalized.mkdir()
    path = normalized / "recipe.yaml"
    path.write_text(_text())
    original = path.read_bytes()
    report = path
    if symlink:
        report = tmp_path / "audit.json"
        report.symlink_to(path)
    assert (
        repair.main(
            [
                "--normalized-dir",
                str(normalized),
                mode,
                "--report",
                str(report),
            ]
        )
        == 2
    )
    assert path.read_bytes() == original


@pytest.mark.parametrize("mode", ["--dry-run", "--apply"])
@pytest.mark.parametrize("link_kind", ["source_symlink", "report_hardlink"])
def test_report_cannot_overwrite_a_linked_source_outside_the_input_directory(
    tmp_path, mode, link_kind
):
    normalized = tmp_path / "normalized"
    normalized.mkdir()
    source = normalized / "recipe.yaml"
    report = tmp_path / "audit.json"
    original = _text().encode("utf-8")
    if link_kind == "source_symlink":
        report.write_bytes(original)
        source.symlink_to(report)
    else:
        source.write_bytes(original)
        report.hardlink_to(source)
    assert repair.main(["--normalized-dir", str(normalized), mode, "--report", str(report)]) == 2
    assert source.read_bytes() == report.read_bytes() == original


def test_concurrent_edit_after_planning_aborts_before_other_recipe_writes(tmp_path, monkeypatch):
    first = tmp_path / "a_first.yaml"
    second = tmp_path / "b_second.yaml"
    original = _text().encode("utf-8")
    first.write_bytes(original)
    second.write_bytes(original)
    concurrent_edit = original + b"# A user's new note\n"
    real_repair = repair.repair_text
    planned = 0

    def edit_while_planning(text, timestamp, mim_pin):
        nonlocal planned
        result = real_repair(text, timestamp, mim_pin)
        planned += 1
        if planned == 2:
            first.write_bytes(concurrent_edit)
        return result

    monkeypatch.setattr(repair, "repair_text", edit_while_planning)
    assert repair.main(["--normalized-dir", str(tmp_path), "--apply"]) == 1
    assert first.read_bytes() == concurrent_edit
    assert second.read_bytes() == original


def test_missing_source_id_fails_before_writing(tmp_path):
    valid = tmp_path / "a_valid.yaml"
    valid.write_text(_text())
    valid_before = valid.read_bytes()
    doc = yaml.safe_load(_text(solution=True))
    del doc["composition"][0]["term"]
    path = tmp_path / "bad.yaml"
    path.write_text(yaml.safe_dump(doc))
    before = path.read_bytes()
    assert repair.main(["--normalized-dir", str(tmp_path), "--apply"]) == 2
    assert path.read_bytes() == before
    assert valid.read_bytes() == valid_before


def test_mim_drift_fails_before_any_recipe_is_written(tmp_path, monkeypatch):
    path = tmp_path / "recipe.yaml"
    path.write_text(_text())
    before = path.read_bytes()
    monkeypatch.setattr(
        repair,
        "get_default_mim_label_index",
        lambda: SimpleNamespace(
            resolve_label=lambda _label: SimpleNamespace(
                identifier="CHEBI:78018", mapping_status="MAPPED"
            )
        ),
    )
    assert repair.main(["--normalized-dir", str(tmp_path), "--apply"]) == 2
    assert path.read_bytes() == before


def test_preview_and_count_guard_write_nothing(tmp_path):
    path = tmp_path / "recipe.yaml"
    path.write_text(_text())
    before = path.read_bytes()
    assert repair.main(["--normalized-dir", str(tmp_path), "--dry-run"]) == 0
    assert path.read_bytes() == before
    assert repair.main(["--normalized-dir", str(tmp_path), "--expect-count", "109", "--apply"]) == 2
    assert path.read_bytes() == before
    assert repair.main(["--normalized-dir", str(tmp_path), "--expect-count", "1", "--apply"]) == 0
    assert yaml.safe_load(path.read_text())["ingredients"][0]["term"]["id"] == "MICRO:0000175"


def test_corpus_has_no_active_rejected_peptone_assignments(corpus):
    found = set()
    for path, doc in corpus:
        for field in ("ingredients", "composition"):
            for row in doc.get(field) or []:
                name = row.get("preferred_term")
                if name not in {"Trypticase", "Bacto-tryptone", "Peptone"}:
                    continue
                found.add(name)
                for slot in ("term", "chebi_term", "mediaingredientmech_chebi_term"):
                    assert (name, (row.get(slot) or {}).get("id")) not in repair.CORRECTIONS, path
    assert found == {"Trypticase", "Bacto-tryptone", "Peptone"}


@pytest.mark.parametrize("module_name", ["repair_komodo_642_score30", "repair_komodo_741_score30"])
def test_komodo_repair_templates_cannot_restore_green_kidney_bean(module_name):
    module = importlib.import_module(module_name)
    peptone = next(row for row in module.COMPONENTS if row.preferred_term == "Peptone")
    assert peptone.term == ("MICRO:0000178", "peptone")


def test_dsmz_repair_template_cannot_restore_green_kidney_bean():
    from repair_dsmz_1551_687_score15 import _dsmz_1551_ingredients

    peptone = next(row for row in _dsmz_1551_ingredients() if row["preferred_term"] == "Peptone")
    assert peptone["term"] == {"id": "MICRO:0000178", "label": "peptone"}


def test_unrelated_aliased_ingredients_are_unchanged():
    shared = {"id": "CHEBI:78018", "label": "dodecylphosphocholine"}
    text = yaml.safe_dump(
        {
            "id": "CultureMech:999999",
            "ingredients": [
                {"preferred_term": "Dodecylphosphocholine", "term": shared},
                {"preferred_term": "Detergent", "term": shared},
            ],
        }
    )
    assert "*id" in text
    assert repair.repair_text(text, TIMESTAMP, repair.verify_mim()) == (text, [])
