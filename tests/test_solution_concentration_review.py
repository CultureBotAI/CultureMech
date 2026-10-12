"""Source integrity, arithmetic, scope, and whole-batch write guards."""

import copy
import json
import sys
from decimal import Decimal
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import fetch_solution_concentration_sources as fetcher
import review_solution_concentration_evidence as reviewer


@pytest.fixture
def sample():
    salt = {
        "compound": "NaCl",
        "compound_id": 43,
        "amount": 1,
        "unit": "g",
        "g_l": 40,
        "optional": 0,
        "condition": None,
        "attribute": None,
    }
    water = {
        "compound": "Distilled water",
        "compound_id": 4,
        "amount": 25,
        "unit": "ml",
        "g_l": None,
        "optional": 0,
        "condition": None,
        "attribute": None,
    }
    source = {
        "id": 100,
        "name": "Example solution",
        "volume": 25,
        "recipe": [salt, water],
        "steps": [],
    }
    doc = {
        "id": "CultureMech:000111",
        "preferred_term": source["name"],
        "term": {"id": "mediadive.solution:100", "label": source["name"]},
        "composition": [
            {
                "preferred_term": row["compound"],
                "term": {
                    "id": f"mediadive.compound:{row['compound_id']}",
                    "label": row["compound"],
                },
                "concentration": {
                    "value": "40" if i == 0 else "1000.0",
                    "unit": "G_PER_L" if i == 0 else "PERCENT_V_V",
                },
            }
            for i, row in enumerate(source["recipe"])
        ],
        "ingredients": [
            {
                "preferred_term": "See source for composition",
                "concentration": {"value": "variable", "unit": "VARIABLE"},
            }
        ],
        "curation_history": [
            {"timestamp": "2026-01-01T00:00:00Z", "curator": "prior", "action": "import"}
        ],
    }
    return doc, source


def capture(source):
    raw = json.dumps({"status": 200, "count": 1, "data": source}, indent=4)
    meta = {
        "url": fetcher.API + str(source["id"]),
        "response_url": fetcher.API + str(source["id"]),
        "http_status": 200,
        "sha256": reviewer.sha(raw.encode()),
        "accessed_at": "2026-10-07T08:00:00+00:00",
    }
    return raw, meta


def run_review(doc, source):
    raw, meta = capture(source)
    return reviewer.review(doc, raw, meta, "2026-10-07T08:01:00+00:00")


def test_provider_concentration_and_batch_water_amount(sample):
    doc, source = sample
    old = copy.deepcopy(doc)
    after, claims = run_review(doc, source)
    assert doc == old
    assert [c["status"] for c in claims] == ["evidence_only", "correct", "unsupported"]
    assert after["composition"][0]["concentration"] == doc["composition"][0]["concentration"]
    assert after["composition"][1]["concentration"] == {"value": "0.025", "unit": "L"}
    assert after["curation_history"][:-1] == doc["curation_history"]
    assert not reviewer.errors(after)
    raw, _ = capture(source)
    for node in after["composition"]:
        assert node["evidence"][0]["snippet"] in raw


@pytest.mark.parametrize("attribute", ["25%", "10 mM", "SIGMA"])
def test_stock_strength_or_material_attribute_is_not_dropped(sample, attribute):
    doc, source = sample
    source["recipe"][0]["attribute"] = attribute
    after, claims = run_review(doc, source)
    assert claims[0]["status"] == "unsupported"
    assert after["composition"][0] == doc["composition"][0]


@pytest.mark.parametrize(
    "key,value", [("optional", 1), ("optional", None), ("condition", "strain-specific")]
)
def test_optional_and_conditional_rows_are_not_promoted(sample, key, value):
    doc, source = sample
    source["recipe"][0][key] = value
    after, claims = run_review(doc, source)
    assert claims[0]["status"] == "unsupported"
    assert after["composition"][0] == doc["composition"][0]


def test_water_make_up_instruction_requires_review(sample):
    doc, source = sample
    source["steps"] = [{"step": "Finally make up to 25 ml."}]
    after, claims = run_review(doc, source)
    assert claims[1]["new"] is None
    assert "manual water review" in claims[1]["explanation"]
    assert after["composition"][1] == doc["composition"][1]


@pytest.mark.parametrize("steps", ["missing", None, {}, ""])
def test_missing_preparation_metadata_is_not_an_empty_step_list(sample, steps):
    doc, source = sample
    if steps == "missing":
        del source["steps"]
    else:
        source["steps"] = steps
    after, claims = run_review(doc, source)
    assert claims[1]["status"] == "unsupported"
    assert claims[1]["new"] is None
    assert "missing or malformed" in claims[1]["explanation"]
    assert after["composition"][1] == doc["composition"][1]


def test_local_preparation_context_is_not_overridden(sample):
    doc, source = sample
    doc["preparation_notes"] = "Make up to volume after adding the concentrate."
    after, claims = run_review(doc, source)
    assert claims[1]["new"] is None
    assert after["composition"][1] == doc["composition"][1]
    doc["preparation_notes"] = "Original volume: 25 mL"
    _, claims = run_review(doc, source)
    assert claims[1]["status"] == "correct"


@pytest.mark.parametrize("change", ["name", "id", "extra", "missing"])
def test_source_formulation_drift_blocks_mutation(sample, change):
    doc, source = sample
    if change == "name":
        source["name"] = "Other solution"
    elif change == "id":
        source["id"] = 101
    elif change == "extra":
        source["recipe"].append({"compound": "Extra", "compound_id": 99, "amount": 1, "unit": "g"})
    else:
        source["recipe"].pop()
    after, claims = run_review(doc, source)
    assert after == doc
    assert all(c["new"] is None for c in claims)


def test_hydrate_label_mismatch_does_not_gain_evidence(sample):
    doc, source = sample
    source["recipe"][0]["compound"] = "NaCl x 2 H2O"
    after, claims = run_review(doc, source)
    assert claims[0]["status"] == "conflict"
    assert after["composition"][0] == doc["composition"][0]


def test_missing_concentration_can_be_added_but_conflicting_mass_cannot(sample):
    doc, source = sample
    del doc["composition"][0]["concentration"]
    after, claims = run_review(doc, source)
    assert claims[0]["status"] == "add"
    assert after["composition"][0]["concentration"] == {"value": "40", "unit": "G_PER_L"}
    doc["composition"][0]["concentration"] = {"value": "1", "unit": "G_PER_L"}
    after, claims = run_review(doc, source)
    assert claims[0]["new"] is None
    assert after["composition"][0] == doc["composition"][0]


def test_rounding_is_not_permission_for_unit_errors():
    assert reviewer.rounded_equal(Decimal("0.1") / 3, Decimal("0.0333333"))
    assert not reviewer.rounded_equal(Decimal("0.1") / 3, Decimal("0.00333333"))
    assert not reviewer.rounded_equal(Decimal("10.4"), Decimal("10"))


def test_source_zero_is_reported_but_not_mistaken_for_fixed_quantity(sample):
    doc, source = sample
    source["recipe"][0].update(amount=0, g_l=0)
    del doc["composition"][0]["concentration"]
    after, claims = run_review(doc, source)
    assert claims[0]["status"] == "unsupported"
    assert "concentration" not in after["composition"][0]


@pytest.mark.parametrize(
    "key,value", [("amount", None), ("amount", -1), ("amount", "NaN"), ("g_l", None), ("g_l", 4)]
)
def test_bad_source_arithmetic_is_not_endorsed(sample, key, value):
    doc, source = sample
    source["recipe"][0][key] = value
    after, claims = run_review(doc, source)
    assert claims[0]["new"] is None
    assert after["composition"][0] == doc["composition"][0]


def test_nested_source_stock_is_reported_not_flattened(sample):
    doc, source = sample
    source["recipe"].append(
        {"solution": "Trace stock", "solution_id": 42, "amount": 1, "unit": "ml"}
    )
    after, claims = run_review(doc, source)
    assert claims[-1]["field"] == "source.recipe[2]"
    assert claims[-1]["new"] is None
    assert "solutions" not in after
    assert len(after["composition"]) == 2


def test_nested_record_claims_and_cycle_detection(sample):
    doc, _ = sample
    doc["solutions"] = [
        {
            "preferred_term": "Nested",
            "concentration": {"value": "1", "unit": "L"},
            "composition": [{"preferred_term": "Missing amount"}],
        }
    ]
    fields = {c["field"] for c in reviewer.all_claims(doc)}
    assert "solutions[0].concentration" in fields
    assert "solutions[0].composition[0].concentration" in fields
    doc["loop"] = doc
    with pytest.raises(ValueError, match="Cyclic"):
        reviewer.all_claims(doc)


def setup_batch(tmp_path, monkeypatch, sample):
    doc, source = sample
    relative = "data/normalized_yaml/bacterial/example.yaml"
    path = tmp_path / relative
    path.parent.mkdir(parents=True)
    path.write_text(yaml.safe_dump(doc, sort_keys=False))
    cache = tmp_path / "cache"
    cache.mkdir()
    raw, meta = capture(source)
    (cache / "100.json").write_text(raw)
    (cache / "100.metadata.json").write_text(json.dumps(meta))
    item = {
        "path": relative,
        "id": doc["id"],
        "name": source["name"],
        "solution_id": 100,
        "before_sha256": reviewer.sha(path.read_bytes()),
    }
    monkeypatch.setattr(
        reviewer.subprocess, "check_output", lambda *a, **k: (relative + "\0").encode()
    )
    plan = reviewer.preview(tmp_path, [item], cache, "f" * 40)
    return path, cache, plan


def test_preview_apply_verify_and_idempotence(tmp_path, monkeypatch, sample):
    path, cache, plan = setup_batch(tmp_path, monkeypatch, sample)
    assert reviewer.sha(path.read_bytes()) == plan["records"][0]["before_sha256"]
    assert reviewer.apply(tmp_path, plan, cache)["changed"] == 1
    assert reviewer.verify(tmp_path, plan, cache)["verified_new_snippets"] == 2
    result = path.read_bytes()
    assert reviewer.apply(tmp_path, plan, cache) == {"changed": 0, "already_applied": 1}
    assert path.read_bytes() == result


def test_solution_curation_does_not_call_medium_fingerprinter(tmp_path, monkeypatch, sample):
    def forbidden(*args):
        raise AssertionError("A standalone solution cannot use a medium fingerprint")

    monkeypatch.setattr(reviewer.RecipeFingerprinter, "fingerprint", forbidden)
    path, cache, plan = setup_batch(tmp_path, monkeypatch, sample)
    item = plan["records"][0]
    assert item["failure"] is None
    assert item["merge_fingerprint_scope"] == "outside_medium_scope"
    assert reviewer.apply(tmp_path, plan, cache)["changed"] == 1
    assert reviewer.verify(tmp_path, plan, cache)["verified_new_snippets"] == 2


def test_preview_refuses_root_class_drift(tmp_path, monkeypatch, sample):
    review = reviewer.review

    def broken_review(*args):
        after, claims = review(*args)
        after["term"]["id"] = "mediadive.medium:100"
        return after, claims

    monkeypatch.setattr(reviewer, "review", broken_review)
    path, _, plan = setup_batch(tmp_path, monkeypatch, sample)
    item = plan["records"][0]
    assert item["failure"] == "Root record class changed or does not match review scope"
    assert item["before_sha256"] == item["after_sha256"] == reviewer.sha(path.read_bytes())


@pytest.mark.parametrize("damage", [None, "amount", "snippet"])
def test_explicit_followup_cannot_hide_damage_to_earlier_supported_claims(
    tmp_path, monkeypatch, sample, damage
):
    path, cache, plan = setup_batch(tmp_path, monkeypatch, sample)
    reviewer.apply(tmp_path, plan, cache)
    before = path.read_text()
    doc = reviewer.load_yaml(before)
    doc["notes"] = "Separate later curation"
    if damage == "amount":
        doc["composition"][0]["concentration"]["value"] = "400"
    elif damage == "snippet":
        doc["composition"][0]["evidence"][0]["snippet"] = "Not from source"
    path.write_bytes(reviewer.render(before, doc))
    item = plan["records"][0]
    successor = {
        "path": item["path"],
        "id": item["id"],
        "before_text": before,
        "before_sha256": item["after_sha256"],
        "after_sha256": reviewer.sha(path.read_bytes()),
    }
    with pytest.raises(ValueError, match="Result hash mismatch"):
        reviewer.verify(tmp_path, plan, cache)
    if damage:
        with pytest.raises(ValueError, match="quantity|snippet"):
            reviewer.verify(tmp_path, plan, cache, [successor])
    else:
        assert reviewer.verify(tmp_path, plan, cache, [successor]) == {
            "checked_record_hashes": 1,
            "verified_new_snippets": 2,
            "superseded_record_hashes": 1,
        }


def test_report_heading_does_not_rewrite_source_name(tmp_path, monkeypatch, sample):
    doc, source = sample
    source["name"] += " "
    doc["preferred_term"] = doc["term"]["label"] = source["name"]
    path, _, plan = setup_batch(tmp_path, monkeypatch, sample)
    before = path.read_bytes()
    folder = tmp_path / "reports"
    reviewer.reports(folder, plan, False)
    lines = (folder / "bacterial/example.yaml.md").read_text().splitlines()
    assert lines[0] == "# Solution Concentration Review: Example solution"
    assert plan["records"][0]["name"] == "Example solution "
    assert path.read_bytes() == before


@pytest.mark.parametrize("identity_conflict", [False, True])
def test_solution_without_legacy_ingredients_is_not_an_operational_failure(
    tmp_path, monkeypatch, sample, identity_conflict
):
    doc, _ = sample
    del doc["ingredients"]
    if identity_conflict:
        doc["composition"][0]["term"] = {"id": "CHEBI:26710", "label": "sodium chloride"}
    path, cache, plan = setup_batch(tmp_path, monkeypatch, sample)
    item = plan["records"][0]
    assert item["failure"] is None
    assert not item["baseline_errors"] and not item["post_errors"]
    assert item["merge_fingerprint_unchanged"]
    assert reviewer.apply(tmp_path, plan, cache)["changed"] == int(not identity_conflict)
    assert reviewer.verify(tmp_path, plan, cache)["verified_new_snippets"] == (
        0 if identity_conflict else 2
    )
    assert "ingredients" not in reviewer.load_yaml(path.read_bytes())


@pytest.mark.parametrize("key", ["ingredients", "solutions"])
def test_preview_still_refuses_changes_to_merge_input_fields(tmp_path, monkeypatch, sample, key):
    review = reviewer.review

    def broken_review(*args):
        after, claims = review(*args)
        after[key] = [{"preferred_term": "Unexpected new component"}]
        return after, claims

    monkeypatch.setattr(reviewer, "review", broken_review)
    path, _, plan = setup_batch(tmp_path, monkeypatch, sample)
    item = plan["records"][0]
    assert item["failure"] == "Merge input fields changed"
    assert item["before_sha256"] == item["after_sha256"] == reviewer.sha(path.read_bytes())


@pytest.mark.parametrize("change", ["record", "source", "plan", "path"])
def test_drift_refused_before_writes(tmp_path, monkeypatch, sample, change):
    path, cache, plan = setup_batch(tmp_path, monkeypatch, sample)
    if change == "record":
        path.write_text(path.read_text() + "# User note\n")
    elif change == "source":
        (cache / "100.json").write_text("{}")
    elif change == "plan":
        plan["records"][0]["claims"][0]["new"]["value"] = "999"
    else:
        plan["records"][0]["path"] = "data/merge_yaml/merged/example.yaml"
    original = path.read_bytes()
    with pytest.raises((ValueError, KeyError)):
        reviewer.apply(tmp_path, plan, cache)
    assert path.read_bytes() == original


def test_fetch_uses_pinned_origin_and_does_not_trust_cache_name(tmp_path, sample):
    _, source = sample
    raw, meta = capture(source)
    (tmp_path / "100.json").write_text(raw)
    meta["response_url"] = "https://example.org/unrelated"
    (tmp_path / "100.metadata.json").write_text(json.dumps(meta))
    with pytest.raises(ValueError, match="URL"):
        fetcher.read_capture(tmp_path, 100)


def test_fetch_failure_is_not_reported_complete(tmp_path, monkeypatch):
    monkeypatch.setattr(
        fetcher, "fetch_one", lambda *a, **k: (_ for _ in ()).throw(OSError("unavailable"))
    )
    monkeypatch.setattr(fetcher.time, "sleep", lambda _: None)
    records = [{"solution_id": n, "path": str(n)} for n in range(5)]
    result = fetcher.fetch(records, tmp_path)
    assert result["failed"] == 3
    assert result["processed"] == 3
    assert not result["complete"]
