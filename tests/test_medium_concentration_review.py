"""Receiving-medium identity, stock boundaries, evidence, and write safeguards."""

import copy
import json
import sys
from pathlib import Path

import pytest
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import fetch_medium_concentration_sources as fetcher
import review_medium_concentration_evidence as medium
import review_solution_concentration_evidence as runner


@pytest.fixture
def sample():
    link = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1.pdf"
    doc = {
        "id": "CultureMech:000111",
        "name": "example",
        "original_name": "Example",
        "category": "bacterial",
        "medium_type": "DEFINED",
        "physical_state": "LIQUID",
        "media_term": {
            "preferred_term": "DSMZ Medium 1",
            "term": {"id": "mediadive.medium:1", "label": "Example"},
        },
        "notes": f"Source: DSMZ | Link: {link}",
        "ingredients": [
            {
                "preferred_term": "NaCl",
                "term": {"id": "CHEBI:26710", "label": "sodium chloride"},
                "concentration": {"value": "2", "unit": "G_PER_L"},
            }
        ],
    }
    data = {
        "medium": {"id": 1, "name": "Example", "source": "DSMZ", "link": link},
        "solutions": [
            {
                "id": 1,
                "name": "Main sol. 1",
                "volume": 1000,
                "steps": [{"step": "Adjust pH to 7."}],
                "recipe": [
                    {
                        "compound": "NaCl",
                        "compound_id": 43,
                        "amount": 2,
                        "unit": "g",
                        "g_l": 2,
                        "optional": 0,
                    },
                    {
                        "compound": "Distilled water",
                        "compound_id": 4,
                        "amount": 1000,
                        "unit": "ml",
                        "optional": 0,
                    },
                ],
            }
        ],
    }
    return doc, data


def capture(data):
    raw = json.dumps({"status": 200, "count": 1, "data": data}, indent=4)
    url = fetcher.API + str(data["medium"]["id"])
    return raw, {
        "url": url,
        "response_url": url,
        "http_status": 200,
        "sha256": runner.sha(raw.encode()),
        "accessed_at": "2026-10-07T08:00:00+00:00",
    }


def review(doc, data):
    raw, meta = capture(data)
    return medium.review(doc, raw, meta, "2026-10-07T08:01:00+00:00")


def test_literal_path_extraction_with_equal_rows_and_escaped_keys():
    raw = '{ "x": [{"a": 1}, { "a": 1 }], "escaped\\"key": {"z": "quoted \\"word\\""}}'
    assert medium.json_excerpt(raw, ["x", 1]) == '{ "a": 1 }'
    assert json.loads(medium.json_excerpt(raw, ['escaped"key', "z"])) == 'quoted "word"'
    with pytest.raises(ValueError):
        medium.json_excerpt(raw, ["x", 2])


def test_main_medium_evidence_preserves_canonical_labels_and_reports_water(sample):
    doc, data = sample
    old = copy.deepcopy(doc)
    after, claims = review(doc, data)
    assert doc == old
    assert claims[0]["status"] == "evidence_only"
    assert claims[1]["ingredient"] == "Distilled water"
    assert claims[1]["status"] == claims[2]["status"] == "unsupported"
    assert after["ingredients"][0]["term"] == old["ingredients"][0]["term"]
    assert after["ingredients"][0]["concentration"] == old["ingredients"][0]["concentration"]
    assert not runner.errors(after, "MediaRecipe")
    assert claims[0]["snippet"] in capture(data)[0]
    assert "not an independently measured final volume" in claims[0]["explanation"]


def jcm_source(sample, mid="J1", link=None):
    doc, data = sample
    link = link or "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1"
    doc["media_term"]["term"]["id"] = f"mediadive.medium:{mid}"
    doc["notes"] = f"Source: JCM | Link: {link}"
    data["medium"].update(id=mid, source="JCM", link=link)
    data["solutions"][0]["name"] = f"Main sol. {mid}"
    return doc, data


def test_jcm_exact_accession_and_link_preserve_original_collection_provenance(sample):
    doc, data = jcm_source(sample)
    after, claims = review(doc, data)
    assert claims[0]["status"] == "evidence_only"
    assert claims[0]["reference"] == "https://mediadive.dsmz.de/rest/medium/J1"
    assert claims[0]["snippet"] in capture(data)[0]
    assert "Original recipe collection=JCM; GRMD accession=1;" in after["references"][0]["notes"]
    assert "dataset provider, not the original recipe collection" in after["references"][0]["notes"]
    assert after["ingredients"][0]["concentration"] == doc["ingredients"][0]["concentration"]
    assert not runner.errors(after, "MediaRecipe")


@pytest.mark.parametrize(
    "mid,link",
    [
        ("1", "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1"),
        ("C1", "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1"),
        ("J0", "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=0"),
        ("J1", "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=2"),
        ("J1", "http://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1"),
        ("J1", "https://example.org/cgi-bin/jcm/jcm_grmd?GRMD=1"),
        ("J1", "https://www.jcm.riken.jp@example.org/cgi-bin/jcm/jcm_grmd?GRMD=1"),
        ("J1", "https://www.jcm.riken.jp:443/cgi-bin/jcm/jcm_grmd?GRMD=1"),
        ("J1", "https://www.jcm.riken.jp/cgi-bin/jcm/other?GRMD=1"),
        ("J1", "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1&GRMD=2"),
        ("J1", "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1&extra=1"),
        ("J1", "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1&extra"),
        ("J1", "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1#other"),
    ],
)
def test_jcm_collection_link_and_accession_must_agree(sample, mid, link):
    doc, data = jcm_source(sample, mid, link)
    after, claims = review(doc, data)
    assert after == doc
    assert claims[0]["status"] == "conflict"
    assert "JCM accession does not match" in claims[0]["explanation"]
    assert all(c["new"] is None for c in claims)


@pytest.mark.parametrize("change", ["stock", "missing", "preparation", "collection"])
def test_jcm_allowance_does_not_bypass_other_source_guards(sample, change):
    doc, data = jcm_source(sample)
    if change == "stock":
        data["solutions"][0]["recipe"].append(
            {"solution_id": 42, "solution": "Stock", "amount": 1, "unit": "ml"}
        )
    elif change == "missing":
        data["solutions"][0].pop("recipe")
    elif change == "preparation":
        data["solutions"][0]["steps"].append({"step": "Do not combine both in one medium."})
    else:
        data["medium"]["source"] = "CCAP"
    after, claims = review(doc, data)
    assert after == doc
    assert claims[0]["status"] == "conflict"
    assert all(c["new"] is None for c in claims)


@pytest.mark.parametrize(
    "step",
    [
        "As energy source add either:",
        "AS ENERGY SOURCE\n ADD EITHER glucose or arginine.",
        "Do not combine both in one medium.",
        "For Ureaplasma add instead of Glucose or Arginine:",
    ],
)
def test_explicit_mutually_exclusive_branches_cannot_gain_unconditional_support(sample, step):
    doc, data = sample
    data["solutions"][0]["steps"].append({"step": step})
    after, claims = review(doc, data)
    assert after == doc
    assert claims[0]["status"] == "conflict"
    assert "Mutually exclusive ingredient branches" in claims[0]["explanation"]
    assert all(c["new"] is None for c in claims)


@pytest.mark.parametrize(
    "step",
    [
        "Add glucose from a sterile stock solution.",
        "For solid medium add agar.",
        "Use distilled water instead of tap water.",
    ],
)
def test_nonexclusive_preparation_does_not_trigger_branch_guard(sample, step):
    doc, data = sample
    data["solutions"][0]["steps"].append({"step": step})
    _, claims = review(doc, data)
    assert claims[0]["status"] == "evidence_only"


@pytest.mark.parametrize(
    "step",
    [
        "Add bicarbonate from a stock (e.g., add 1 ml stock solution per 9 ml medium).",
        "Mix 0.5 ml of stock solution with 4.5 ml of basal medium.",
        "ADD 1ML STOCK SOLUTION TO 9 ML MEDIUM.",
    ],
)
def test_explicit_mixing_ratio_requires_stage_review(sample, step):
    doc, data = sample
    data["solutions"][0]["steps"].append({"step": step})
    after, claims = review(doc, data)
    assert after == doc
    assert claims[0]["status"] == "conflict"
    assert "stock-to-medium mixing ratio" in claims[0]["explanation"]
    assert all(c["new"] is None for c in claims)


def test_main_volume_with_stock_addition_is_not_an_explicit_mixing_ratio(sample):
    doc, data = sample
    data["solutions"][0]["steps"].append(
        {"step": "Add 100 ml stock solution and make up the complete medium to 1000 ml."}
    )
    _, claims = review(doc, data)
    assert claims[0]["status"] == "evidence_only"


@pytest.mark.parametrize(
    "step",
    [
        "For agar media, do not add supplemental calcium.",
        "FOR AGAR MEDIA\n DO NOT ADD supplemental calcium.",
        "Agar (2%) medium should be prepared without Na2CO3.",
        "Agar medium should be prepared without NaCl.",
    ],
)
def test_agar_omission_cannot_support_solid_formulation(sample, step):
    doc, data = sample
    doc["physical_state"] = "SOLID_AGAR"
    data["solutions"][0]["steps"].append({"step": step})
    after, claims = review(doc, data)
    assert after == doc
    assert claims[0]["status"] == "conflict"
    assert "Agar-specific ingredient omission" in claims[0]["explanation"]
    assert all(c["new"] is None for c in claims)


@pytest.mark.parametrize(
    "state,step",
    [
        ("LIQUID", "For agar media, do not add supplemental calcium."),
        ("LIQUID", "Agar (2%) medium should be prepared without NaCl."),
        ("SOLID_AGAR", "Autoclave agar and NaCl separately, then combine."),
        ("SOLID_AGAR", "Prepare without NaCl, then add it after autoclaving."),
    ],
)
def test_agar_guard_does_not_reject_unaffected_state_or_separate_sterilization(sample, state, step):
    doc, data = sample
    doc["physical_state"] = state
    data["solutions"][0]["steps"].append({"step": step})
    _, claims = review(doc, data)
    assert claims[0]["status"] == "evidence_only"


@pytest.mark.parametrize(
    "step",
    [
        "Adjust pH by adding 100 ml/l 1M sterilized NaHCO3.",
        "Add 10 ML / L 0.5 M sodium carbonate.",
        "Add 2.5 ml/l\n1 M stock.",
    ],
)
def test_prose_molar_stock_dose_requires_basis_review(sample, step):
    doc, data = sample
    data["solutions"][0]["steps"].append({"step": step})
    after, claims = review(doc, data)
    assert after == doc
    assert claims[0]["status"] == "conflict"
    assert "Molar-stock doses" in claims[0]["explanation"]
    assert all(c["new"] is None for c in claims)


def test_alias_rows_cannot_gain_independent_amount_support(sample):
    doc, data = sample
    alias = copy.deepcopy(doc["ingredients"][0])
    alias["preferred_term"] = "Sodium chloride"
    doc["ingredients"].append(alias)
    row = copy.deepcopy(data["solutions"][0]["recipe"][0])
    row.update(compound="Sodium chloride", compound_id=999)
    data["solutions"][0]["recipe"].append(row)
    after, claims = review(doc, data)
    assert after == doc
    assert claims[0]["status"] == "conflict"
    assert "share a local chemical identifier" in claims[0]["explanation"]


def test_attributed_mixture_is_not_asserted_to_be_a_duplicate_from_ontology_id(sample):
    doc, data = sample
    mixture = copy.deepcopy(doc["ingredients"][0])
    mixture["preferred_term"] = "Saline mixture"
    doc["ingredients"].append(mixture)
    row = copy.deepcopy(data["solutions"][0]["recipe"][0])
    row.update(compound="Saline mixture", compound_id=999, attribute="brand")
    data["solutions"][0]["recipe"].append(row)
    after, claims = review(doc, data)
    assert claims[0]["status"] == "evidence_only"
    assert claims[1]["status"] == "unsupported"
    assert after["ingredients"][1] == mixture


@pytest.mark.parametrize(
    "change",
    [
        "id",
        "name",
        "link",
        "collection",
        "main_name",
        "hydrate",
        "missing",
        "extra",
        "duplicate",
        "stock",
        "nested_local",
        "upstream_id",
    ],
)
def test_identity_inventory_and_stock_conflicts_cannot_gain_support(sample, change):
    doc, data = sample
    source = data["solutions"][0]
    if change == "id":
        data["medium"]["id"] = 2
    elif change == "name":
        data["medium"]["name"] = "Another medium"
    elif change == "link":
        doc["notes"] = "Unrelated source"
    elif change == "collection":
        data["medium"]["source"] = "Different collection"
    elif change == "main_name":
        source["name"] = "Trace stock"
    elif change == "hydrate":
        source["recipe"][0]["compound"] = "NaCl x 2 H2O"
    elif change == "missing":
        source["recipe"].pop(0)
    elif change == "extra":
        source["recipe"].append(
            {
                "compound": "KCl",
                "compound_id": 2,
                "amount": 2,
                "unit": "g",
                "optional": 0,
            }
        )
    elif change == "duplicate":
        source["recipe"].append(copy.deepcopy(source["recipe"][0]))
    elif change == "stock":
        source["recipe"].append(
            {"solution_id": 42, "solution": "Trace stock", "amount": 1, "unit": "ml"}
        )
    elif change == "nested_local":
        doc["solutions"] = [
            {
                "preferred_term": "Stock",
                "concentration": {"value": "1", "unit": "L"},
                "composition": [{"preferred_term": "KCl"}],
            }
        ]
    else:
        doc["ingredients"][0]["term"]["id"] = "mediadive.compound:99"
    after, claims = review(doc, data)
    assert after == doc
    assert claims[0]["status"] == "conflict"
    assert all(c["new"] is None for c in claims)


@pytest.mark.parametrize(
    "change",
    [
        "optional",
        "attribute",
        "condition",
        "notes",
        "zero",
        "denominator",
        "no_steps",
        "no_volume",
        "percent",
        "nan",
    ],
)
def test_ambiguous_quantity_context_is_unchanged(sample, change):
    doc, data = sample
    source, row, node = (
        data["solutions"][0],
        data["solutions"][0]["recipe"][0],
        doc["ingredients"][0],
    )
    if change == "optional":
        row["optional"] = 1
    elif change == "attribute":
        row["attribute"] = "5% stock"
    elif change == "condition":
        row["condition"] = "if required"
    elif change == "notes":
        node["notes"] = "For a different dilution"
    elif change == "zero":
        row["amount"] = row["g_l"] = 0
    elif change == "denominator":
        node["concentration"]["per_volume"] = "per 100 mL"
    elif change == "no_steps":
        del source["steps"]
    elif change == "no_volume":
        del source["volume"]
    elif change == "percent":
        row["unit"] = "%"
    else:
        row["g_l"] = "NaN"
    after, claims = review(doc, data)
    assert after == doc
    assert claims[0]["status"] in {"unsupported", "conflict"}


def test_mass_conversion_missing_value_and_conflict(sample):
    doc, data = sample
    row = data["solutions"][0]["recipe"][0]
    row.update(amount=2000, unit="mg")
    del doc["ingredients"][0]["concentration"]
    after, claims = review(doc, data)
    assert claims[0]["status"] == "add"
    assert after["ingredients"][0]["concentration"] == {"value": "2", "unit": "G_PER_L"}
    doc["ingredients"][0]["concentration"] = {"value": "2000", "unit": "MG_PER_L"}
    assert review(doc, data)[1][0]["status"] == "evidence_only"
    row["g_l"] = 20
    assert review(doc, data)[1][0]["status"] == "conflict"
    row["g_l"] = 2
    doc["ingredients"][0]["concentration"]["value"] = "200"
    assert review(doc, data)[1][0]["status"] == "conflict"


@pytest.mark.parametrize("label", ["air-dried garden soil", "Dry cow-manure", "Soil extract"])
@pytest.mark.parametrize("step", ["Centrifuge the supernatant.", "Filter through cheesecloth."])
def test_extraction_input_is_not_supported_as_finished_medium(sample, label, step):
    doc, data = sample
    doc["ingredients"][0]["preferred_term"] = label
    source = data["solutions"][0]
    source["recipe"][0]["compound"] = label
    source["steps"] = [{"step": step}]
    after, claims = review(doc, data)
    assert after == doc
    assert claims[0]["status"] == "unsupported"
    assert "extract yield" in claims[0]["explanation"]


def test_separate_filter_sterilization_does_not_imply_extraction(sample):
    doc, data = sample
    data["solutions"][0]["steps"] = [{"step": "Filter sterilize the salt solution."}]
    after, claims = review(doc, data)
    assert claims[0]["status"] == "evidence_only"
    assert after["ingredients"][0]["concentration"] == doc["ingredients"][0]["concentration"]


def test_explicit_per_liter_unit_is_not_divided_twice(sample):
    doc, data = sample
    data["solutions"][0]["volume"] = 500
    data["solutions"][0]["recipe"][0]["unit"] = "g/l"
    assert review(doc, data)[1][0]["status"] == "evidence_only"
    data["solutions"][0]["recipe"][0]["unit"] = "g"
    assert review(doc, data)[1][0]["status"] == "conflict"


def test_solid_condition_must_match_state(sample):
    doc, data = sample
    data["solutions"][0]["recipe"][0]["condition"] = "for solid medium"
    doc["ingredients"][0]["notes"] = " (for solid medium)"
    assert review(doc, data)[1][0]["status"] == "unsupported"
    doc["physical_state"] = "SOLID_AGAR"
    assert review(doc, data)[1][0]["status"] == "evidence_only"


def test_variants_stocks_and_missing_amounts_are_in_inventory(sample):
    doc, _ = sample
    doc["variants"] = [{"name": "Supplemented", "modifications": ["Add 1 g KCl"]}]
    doc["variant_children"] = [
        {
            "path": "data/normalized_yaml/bacterial/child.yaml",
            "relationship": "SUPPLEMENTED_VARIANT",
        }
    ]
    doc["solutions"] = [
        {
            "preferred_term": "Stock",
            "concentration": {"value": "1", "unit": "L"},
            "composition": [{"preferred_term": "KCl"}],
        }
    ]
    fields = {c["field"] for c in medium.collect_claims(doc)}
    assert {
        "variants[0]",
        "variant_children[0]",
        "solutions[0].concentration",
        "solutions[0].composition[0].concentration",
    } <= fields
    del doc["solutions"][0]["concentration"]
    doc["solutions"][0]["concentration_candidates"] = [
        {"value": "1", "unit": "ML_PER_L", "basis": "TYPICAL_VALUE"}
    ]
    doc["parent_media"] = [{"path": "data/normalized_yaml/bacterial/parent.yaml"}]
    fields = {c["field"] for c in medium.collect_claims(doc)}
    assert {
        "solutions[0].concentration",
        "solutions[0].concentration_candidates",
        "parent_media[0]",
    } <= fields


def setup_batch(tmp_path, monkeypatch, sample, withholdings=()):
    doc, data = sample
    relative = "data/normalized_yaml/bacterial/example.yaml"
    path = tmp_path / relative
    path.parent.mkdir(parents=True)
    path.write_text(yaml.safe_dump(doc, sort_keys=False))
    cache = tmp_path / "cache"
    cache.mkdir()
    raw, meta = capture(data)
    (cache / "1.json").write_text(raw)
    (cache / "1.metadata.json").write_text(json.dumps(meta))
    item = {
        "path": relative,
        "id": doc["id"],
        "name": doc["original_name"],
        "medium_id": "1",
        "before_sha256": runner.sha(path.read_bytes()),
    }
    monkeypatch.setattr(
        runner.subprocess, "check_output", lambda *a, **k: (relative + "\0").encode()
    )
    medium.check_withholdings(tmp_path, [item], cache, list(withholdings))
    plan = runner.preview(tmp_path, [item], cache, "f" * 40, adapter=medium.adapter(withholdings))
    if withholdings:
        plan["withholdings"] = list(withholdings)
    assert not plan["records"][0]["failure"]
    return path, cache, plan


def withholding(sample, fields=None):
    doc, data = sample
    raw, meta = capture(data)
    return {
        "id": doc["id"],
        "medium_id": str(data["medium"]["id"]),
        "fields": fields or ["ingredients[0].concentration"],
        "reference": meta["url"],
        "source_sha256": runner.sha(raw.encode()),
        "source_pointer": ["data", "solutions", 0, "steps", 0, "step"],
        "snippet": "Adjust pH to 7.",
        "reason": "Fixture for a manual scientific-scope veto.",
    }


@pytest.mark.parametrize("fields", [["*"], ["ingredients[0].concentration"]])
def test_withholding_only_blocks_never_changes_quantities(sample, fields):
    doc, data = sample
    raw, meta = capture(data)
    decision = withholding(sample, fields)
    after, claims = medium.review(doc, raw, meta, "2026-10-07", withholdings=[decision])
    assert after == doc
    assert claims[0]["status"] == "conflict" and claims[0]["new"] is None
    assert claims[0]["snippet"] == decision["snippet"]
    assert claims[0]["locator"] == "$.data.solutions[0].steps[0].step"
    assert all(c["status"] not in runner.SUPPORTED for c in claims)


@pytest.mark.parametrize(
    "pointer",
    [["data", "solutions", 0, "volume"], ["data", "solutions", 0, "recipe", 0]],
)
def test_withholding_numeric_or_object_source_must_be_exact_fragment(sample, pointer):
    doc, data = sample
    raw, meta = capture(data)
    decision = withholding(sample)
    decision.update(source_pointer=pointer, snippet=medium.json_excerpt(raw, pointer))
    after, claims = medium.review(doc, raw, meta, "2026-10-07", withholdings=[decision])
    assert after == doc and claims[0]["status"] == "conflict"
    decision["snippet"] = decision["snippet"][:-1]
    with pytest.raises(ValueError, match="does not match"):
        medium.review(doc, raw, meta, "2026-10-07", withholdings=[decision])


@pytest.mark.parametrize(
    "damage",
    [
        "hash",
        "reference",
        "medium",
        "snippet",
        "pointer",
        "negative_index",
        "bool_index",
        "field",
        "empty_fields",
        "duplicate_field",
        "wildcard_mix",
        "extra",
        "reason",
        "overlap",
    ],
)
def test_bad_withholding_is_rejected(sample, damage):
    doc, data = sample
    decision = withholding(sample)
    if damage == "hash":
        decision["source_sha256"] = "a" * 64
    elif damage == "reference":
        decision["reference"] += "other"
    elif damage == "medium":
        decision["medium_id"] = "2"
    elif damage == "snippet":
        decision["snippet"] = "Unverified text"
    elif damage == "pointer":
        decision["source_pointer"] = ["data", "medium", "name"]
    elif damage in {"negative_index", "bool_index"}:
        decision["source_pointer"][2] = -1 if damage == "negative_index" else False
    elif damage == "field":
        decision["fields"] = ["ingredients[99].concentration"]
    elif damage == "empty_fields":
        decision["fields"] = []
    elif damage == "duplicate_field":
        decision["fields"] *= 2
    elif damage == "wildcard_mix":
        decision["fields"].append("*")
    elif damage == "extra":
        decision["new"] = {"value": "99", "unit": "G_PER_L"}
    elif damage == "reason":
        decision["reason"] = "  "
    decisions = [decision, copy.deepcopy(decision)] if damage == "overlap" else [decision]
    raw, meta = capture(data)
    with pytest.raises(ValueError):
        medium.review(doc, raw, meta, "2026-10-07", withholdings=decisions)


def test_partial_withholding_preview_apply_verify_noop_and_drift(tmp_path, monkeypatch, sample):
    doc, data = sample
    node = copy.deepcopy(doc["ingredients"][0])
    node.update(preferred_term="KCl", term={"id": "CHEBI:32588", "label": "potassium chloride"})
    doc["ingredients"].append(node)
    row = copy.deepcopy(data["solutions"][0]["recipe"][0])
    row.update(compound="KCl", compound_id=44)
    data["solutions"][0]["recipe"].insert(1, row)
    decisions = [withholding(sample)]
    path, cache, plan = setup_batch(tmp_path, monkeypatch, sample, decisions)
    adapter = medium.adapter(plan["withholdings"])
    before = path.read_bytes()
    with pytest.raises(ValueError, match="Preview claims changed"):
        runner.apply(tmp_path, plan, cache, adapter=medium.adapter())
    assert path.read_bytes() == before
    assert runner.apply(tmp_path, plan, cache, adapter=adapter)["changed"] == 1
    assert runner.verify(tmp_path, plan, cache, adapter=adapter)["verified_new_snippets"] == 1
    after = runner.load_yaml(path.read_bytes())
    assert after["ingredients"][0] == doc["ingredients"][0]
    assert len(after["ingredients"][1]["evidence"]) == 1
    assert runner.apply(tmp_path, plan, cache, adapter=adapter)["already_applied"] == 1
    medium.check_withholdings(tmp_path, plan["records"], cache, decisions)
    bad = copy.deepcopy(decisions)
    bad[0]["id"] = "CultureMech:999999"
    with pytest.raises(ValueError, match="exactly one selected"):
        medium.check_withholdings(tmp_path, plan["records"], cache, bad)


@pytest.mark.parametrize("flag", ["--apply", "--verify"])
def test_withholding_cli_override_is_refused(monkeypatch, flag):
    monkeypatch.setattr(
        sys,
        "argv",
        [
            "review",
            "--cache",
            "unused",
            "--plan",
            "unused",
            "--withholdings",
            "unused",
            flag,
        ],
    )
    with pytest.raises(ValueError, match="preview-only"):
        medium.main()


def test_preview_apply_readback_idempotence_and_report(tmp_path, monkeypatch, sample):
    path, cache, plan = setup_batch(tmp_path, monkeypatch, sample)
    assert runner.sha(path.read_bytes()) == plan["records"][0]["before_sha256"]
    assert plan["target_class"] == "MediaRecipe"
    assert runner.apply(tmp_path, plan, cache, adapter=medium.adapter())["changed"] == 1
    assert (
        runner.verify(tmp_path, plan, cache, adapter=medium.adapter())["verified_new_snippets"] == 1
    )
    result = path.read_bytes()
    assert runner.apply(tmp_path, plan, cache, adapter=medium.adapter()) == {
        "changed": 0,
        "already_applied": 1,
    }
    assert path.read_bytes() == result
    raw, meta = medium.read_capture(cache, "1")
    after, _ = medium.review(runner.load_yaml(result), raw, meta, plan["created_at"])
    assert after == runner.load_yaml(result)
    folder = tmp_path / "reports"
    runner.reports(
        folder,
        plan,
        True,
        source_api=medium.API,
        source_id_key="medium_id",
        title="Medium",
    )
    text = (folder / "bacterial/example.yaml.md").read_text()
    assert text.count("- Record:") == 1
    assert "# Medium Concentration Review:" in text
    assert f"- Source: {medium.API}1" in text


@pytest.mark.parametrize("damage", ["record", "source", "metadata", "plan", "target_class", "path"])
def test_drift_is_refused_before_write(tmp_path, monkeypatch, sample, damage):
    path, cache, plan = setup_batch(tmp_path, monkeypatch, sample)
    if damage == "record":
        path.write_text(path.read_text() + "# Concurrent change\n")
    elif damage == "source":
        (cache / "1.json").write_text("{}")
    elif damage == "metadata":
        meta = json.loads((cache / "1.metadata.json").read_text())
        meta["accessed_at"] = "2026-10-07T09:00:00+00:00"
        (cache / "1.metadata.json").write_text(json.dumps(meta))
    elif damage == "plan":
        plan["records"][0]["claims"][0]["new"]["value"] = "1000"
    elif damage == "target_class":
        plan["target_class"] = "SolutionRecipe"
    else:
        plan["records"][0]["path"] = "data/merge_yaml/merged/example.yaml"
    before = path.read_bytes()
    with pytest.raises((ValueError, KeyError)):
        runner.apply(tmp_path, plan, cache, adapter=medium.adapter())
    assert path.read_bytes() == before


@pytest.mark.parametrize("value", ["../1", "1/../2", "", "http://example.org"])
def test_source_identifier_traversal_refused(value):
    with pytest.raises(ValueError):
        fetcher.identifier(value)


def test_capture_origin_and_id_are_pinned(tmp_path, sample):
    _, data = sample
    raw, meta = capture(data)
    (tmp_path / "1.json").write_text(raw)
    meta["response_url"] = "https://example.org/1"
    (tmp_path / "1.metadata.json").write_text(json.dumps(meta))
    with pytest.raises(ValueError, match="URL"):
        fetcher.read_capture(tmp_path, "1")
    with pytest.raises(ValueError, match="Wrong source medium"):
        fetcher.check_payload(raw, "2")


@pytest.mark.parametrize("damage", [None, "amount", "snippet"])
def test_hash_linked_followup_cannot_hide_damage_to_accepted_claims(
    tmp_path, monkeypatch, sample, damage
):
    path, cache, plan = setup_batch(tmp_path, monkeypatch, sample)
    runner.apply(tmp_path, plan, cache, adapter=medium.adapter())
    before = path.read_text()
    doc = runner.load_yaml(before)
    doc["notes"] += " Separate later curation."
    if damage == "amount":
        doc["ingredients"][0]["concentration"]["value"] = "200"
    elif damage == "snippet":
        doc["ingredients"][0]["evidence"][0]["snippet"] = "Not from the source"
    path.write_bytes(runner.render(before, doc))
    item = plan["records"][0]
    successor = {
        "path": item["path"],
        "id": item["id"],
        "before_text": before,
        "before_sha256": item["after_sha256"],
        "after_sha256": runner.sha(path.read_bytes()),
    }
    with pytest.raises(ValueError, match="Result hash mismatch"):
        runner.verify(tmp_path, plan, cache, adapter=medium.adapter())
    if damage:
        with pytest.raises(ValueError, match="quantity|snippet"):
            runner.verify(tmp_path, plan, cache, [successor], adapter=medium.adapter())
    else:
        result = runner.verify(tmp_path, plan, cache, [successor], adapter=medium.adapter())
        assert result["superseded_record_hashes"] == 1
        assert result["verified_new_snippets"] == 1


@pytest.mark.parametrize("flags", [["--apply"], ["--verify", "--reports", "ignored"]])
def test_followup_cli_cannot_apply_or_rewrite_historical_reports(monkeypatch, flags):
    monkeypatch.setattr(
        sys,
        "argv",
        ["review", "--cache", "unused", "--plan", "unused", "--followup-plan", "unused"] + flags,
    )
    with pytest.raises(ValueError, match="without report rewriting"):
        medium.main()
