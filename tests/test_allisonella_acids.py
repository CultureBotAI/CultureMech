"""Challenge Allisonella stock scopes, source identities, evidence and guarded writes."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_allisonella_acids as repair

spec = importlib.util.spec_from_file_location("allisonella_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())
ITEMS = {r["key"]: r for r in PLAN["records"]}


def records(key):
    item = copy.deepcopy(ITEMS[key])
    return (
        item,
        repair.runner.load_yaml(item["before_text"]),
        repair.runner.load_yaml(item["after_text"]),
    )


@pytest.mark.parametrize("key", ITEMS)
def test_builder_matches_independent_source_projection(key):
    item, before, expected = records(key)
    original = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == original and after == expected
    assert claims == item["claims"] and lineage == item["lineage"]
    assert audit.check(before, after, item)["old_quantity_slots"] == 21


@pytest.mark.parametrize(
    "key,path", [(key, row["pointer"]) for key, item in ITEMS.items() for row in item["lineage"]]
)
def test_every_source_node_rejects_unreviewed_quantity(key, path):
    item, before, after = records(key)
    audit.get(after, path)["concentration"] = {"value": "87654321", "unit": "G_PER_L"}
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "omit",
        "extra",
        "grounding",
        "snippet",
        "duplicate_evidence",
        "history",
        "claim",
        "lineage",
        "title",
        "year",
        "old_value",
        "family",
        "provenance",
    ],
)
def test_independent_audit_rejects_claim_and_identity_corruption(key, mutation):
    item, before, after = records(key)
    if mutation == "omit":
        after["ingredients"].pop()
    elif mutation == "extra":
        after["ingredients"].append(copy.deepcopy(after["ingredients"][0]))
    elif mutation == "grounding":
        after["ingredients"][0]["term"] = {"id": "CHEBI:123", "label": "invented"}
    elif mutation == "snippet":
        after["ingredients"][0]["evidence"][0]["snippet"] = "invented quotation"
    elif mutation == "duplicate_evidence":
        after["evidence"].append(copy.deepcopy(after["evidence"][0]))
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif mutation == "claim":
        item["claims"].pop()
    elif mutation == "lineage":
        item["lineage"].pop()
    elif mutation == "title":
        after["references"][0]["title"] = "Different recipe"
    elif mutation == "year":
        after["references"][0]["year"] = 2022
    elif mutation == "old_value":
        item["claims"][0]["old"] = {"value": "0", "unit": "L"}
    elif mutation == "family":
        ref = after["parent_media"] if key == "K1006" else after["variant_children"][0]
        ref["relationship"] = "SOURCE_DUPLICATE"
    else:
        after["notes"] = "Corrected"
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


def test_acid_liquid_inputs_are_not_final_medium_rates():
    _, _, after = records("D1006")
    stock = after["solutions"][1]
    assert stock["concentration"] == {"value": "0.0031", "unit": "L"}
    assert [n["concentration"] for n in stock["composition"]] == [
        {"value": value, "unit": "L"}
        for value in ("0.5485", "0.1935", "0.129", "0.03225", "0.03225", "0.03225", "0.03225")
    ]
    assert stock["composition"][5]["preferred_term"] == "DL-2-Methylbutyric acid"
    assert all("concentration" not in n for n in after["ingredients"][:-1])
    assert after["ingredients"][-1]["concentration"] == {"value": "1", "unit": "L"}


def test_resazurin_stock_strength_and_dose_are_not_interchanged():
    item, before, after = records("D1006")
    stock = after["solutions"][0]
    assert stock["concentration"] == {"value": "0.0005", "unit": "L"}
    assert stock["composition"][0]["concentration"] == {"value": "0.1", "unit": "PERCENT_W_V"}
    stock["composition"][0]["concentration"]["unit"] = "G_PER_L"
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


@pytest.mark.parametrize("label", ["Cysteine-HCl x H2O", "Resazurin"])
def test_unverified_copied_chemical_forms_are_not_reintroduced(label):
    item, before, after = records("K1006")
    node = next(n for n in after["ingredients"] if n["preferred_term"] == label)
    assert not any(k in node for k in ("term", "mediaingredientmech_chebi_term"))
    archived = [c for c in item["claims"] if c["kind"] == "copied_identity_archived"]
    assert len(archived) == 1 and archived[0]["old"] == before["ingredients"]
    node["term"] = {"id": "CHEBI:91248", "label": "L-cysteine hydrochloride hydrate"}
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


def test_false_lb_removed_without_removing_genuine_components():
    for key in ITEMS:
        _, _, after = records(key)
        names = {n["preferred_term"] for n in after["ingredients"]}
        assert {"Yeast extract", "NaCl"} <= names
        assert ("Trypticase" if key == "K1006" else "Trypticase peptone") in names
        assert "Tryptone" not in names and "Sodium chloride" not in names


def test_pdf_quantity_rows_exclude_headings_and_reject_duplicate_amounts():
    _, before, _ = records("D1006")
    review = repair.Review(before, "D1006")
    quote = review.pdf_row("Volatile fatty acid mixture")
    assert "3.10" in quote and quote.endswith("ml")
    review.texts["DSMZ1006"] += "\n" + quote
    with pytest.raises(ValueError, match="Ambiguous PDF row"):
        review.pdf_row("Volatile fatty acid mixture")


def test_source_hash_guard_rejects_changed_capture():
    context = repair.frozen()
    context["sources"]["K1006"]["raw"] += "changed"
    with pytest.raises(ValueError, match="Source capture drift"):
        repair.sources(context)


def fixture_repo(tmp_path, monkeypatch):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    targets = []
    for item in ITEMS.values():
        target = tmp_path / item["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(item["before_text"])
        targets.append(target)
    subprocess.run(["git", "add", "data"], cwd=tmp_path, check=True)
    original = subprocess.check_output
    monkeypatch.setattr(
        subprocess,
        "check_output",
        lambda args, **kwargs: (
            PLAN["commit"] + "\n"
            if args == ["git", "rev-parse", "HEAD"]
            else original(args, **kwargs)
        ),
    )
    return targets


def test_preview_apply_readback_and_noop(tmp_path, monkeypatch):
    targets = fixture_repo(tmp_path, monkeypatch)
    plan = tmp_path / "plan.json"
    before = [p.read_bytes() for p in targets]
    repair.process(tmp_path, plan, "preview")
    assert [p.read_bytes() for p in targets] == before
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 2
    current = [p.read_bytes() for p in targets]
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 2
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert [p.read_bytes() for p in targets] == current


def test_concurrent_edit_blocks_both_writes(tmp_path, monkeypatch):
    targets = fixture_repo(tmp_path, monkeypatch)
    plan = tmp_path / "plan.json"
    repair.process(tmp_path, plan, "preview")
    targets[-1].write_text(targets[-1].read_text() + "# concurrent change\n")
    before = [p.read_bytes() for p in targets]
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(tmp_path, plan, "apply")
    assert [p.read_bytes() for p in targets] == before
