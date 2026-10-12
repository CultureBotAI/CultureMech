"""Adversarial tests of all nineteen medium-119 formulations and stock boundaries."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_methanobacterium_family as repair

spec = importlib.util.spec_from_file_location("medium119_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())
ITEMS = {r["key"]: r for r in PLAN["records"]}
DOCS = {
    k: (repair.runner.load_yaml(r["before_text"]), repair.runner.load_yaml(r["after_text"]))
    for k, r in ITEMS.items()
}


def records(key):
    return copy.deepcopy((ITEMS[key], *DOCS[key]))


@pytest.mark.parametrize("key", ITEMS)
def test_independent_projection_accounts_for_every_old_slot_and_source_node(key):
    item, before, after = records(key)
    result = audit.check(before, after, item)
    assert result["old_quantity_slots"] == len(before["ingredients"])
    assert result["source_nodes"] == len(item["lineage"])


@pytest.mark.parametrize(
    "key,path", [(key, row["pointer"]) for key, item in ITEMS.items() for row in item["lineage"]]
)
def test_every_source_node_rejects_wrong_quantity(key, path):
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
        "source_identity",
    ],
)
def test_corrupted_identity_evidence_or_accounting_is_rejected(key, mutation):
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
        after["references"][0]["title"] = "Different source"
    elif mutation == "year":
        after["references"][0]["year"] = 2022
    elif mutation == "old_value":
        item["claims"][0]["old"] = {"value": "0", "unit": "L"}
    else:
        after["media_term"]["term"]["id"] = "mediadive.medium:119b"
        if key == "D119b":
            after["media_term"]["term"]["id"] = "mediadive.medium:119"
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize("key", ["D119", "D119a", "D119b", "D119c"])
def test_acid_carrier_and_stock_strength_are_not_final_medium_masses(key):
    _, _, after = records(key)
    stocks = {s["preferred_term"]: s for s in after["solutions"]}
    fatty = stocks["Fatty acid mixture"]
    assert fatty["concentration"] == {"value": "0.02", "unit": "L"}
    assert [n["concentration"] for n in fatty["composition"]] == [
        {"value": value, "unit": "L"} for value in ("0.023", "0.027", "0.027", "0.027", "0.896")
    ]
    iron = stocks["FeSO4 x 7 H2O solution (0.1% w/v)"]
    assert iron["concentration"] == {"value": "0.002", "unit": "L"}
    assert iron["composition"][0]["concentration"] == {"value": "0.1", "unit": "PERCENT_W_V"}
    assert iron["composition"][1]["concentration"] == {"value": "1", "unit": "L"}
    assert "0.1 N" in iron["composition"][1]["notes"]
    assert "freshly prepared" in iron["preparation_notes"]


def test_only_original_119_has_verified_basal_final_volume():
    for key in ("D119", "D119a", "D119b", "D119c"):
        _, _, after = records(key)
        nodes = {n["preferred_term"]: n for n in after["ingredients"]}
        if key == "D119":
            assert nodes["KH2PO4"]["concentration"] == {"value": "0.498504", "unit": "G_PER_L"}
            assert nodes["Yeast extract"]["concentration"] == {
                "value": "0.997009",
                "unit": "G_PER_L",
            }
        else:
            assert "concentration" not in nodes["KH2PO4"]
            assert "concentration" not in nodes["Yeast extract"]
        for stock in after["solutions"]:
            if stock["preferred_term"] == "Sludge fluid":
                assert "concentration" not in stock["composition"][0]
                assert "4 g" in stock["composition"][0]["notes"]
                assert stock["concentration"] == {"value": "0.05", "unit": "L"}


def test_methanol_stock_is_not_neat_methanol_or_density_derived_mass():
    _, _, after = records("D119b")
    stock = next(s for s in after["solutions"] if s["preferred_term"] == "Methanol (15% v/v)")
    assert stock["concentration"] == {"value": "0.01", "unit": "L"}
    assert stock["composition"][0]["concentration"] == {"value": "15", "unit": "PERCENT_V_V"}
    assert "Methanol" not in {n["preferred_term"] for n in after["ingredients"]}


@pytest.mark.parametrize(
    "key,label,value",
    [
        ("K119_11975", "NH4Cl", "10.40"),
        ("K119_11977", "NH4Cl", "10.40"),
        ("K119_6216", "Na-acetate", "3.99"),
        ("K119_7256", "rumen fluid", "200.00"),
        ("K119_3468", "methanol", "5.00"),
        ("K119.1", "Trypticase Peptone", "1.96"),
    ],
)
def test_provider_variants_keep_literal_rates_not_neighbor_recipe_values(key, label, value):
    _, _, after = records(key)
    node = next(n for n in after["ingredients"] if n["preferred_term"] == label)
    assert node["concentration"] == {"value": value, "unit": "G_PER_L"}


def test_both_directions_of_every_family_link_use_exact_current_paths():
    docs = {d[1]["id"]: d[1] for d in DOCS.values()}
    paths = {r["id"]: r["path"] for r in ITEMS.values()}
    for doc in docs.values():
        for child in doc.get("variant_children", []):
            parent = docs[child["id"]]["parent_media"]
            assert parent["id"] == doc["id"]
            assert parent["path"] == paths[doc["id"]]
            assert child["path"] == paths[child["id"]]
            assert parent["relationship"] == child["relationship"] != "SOURCE_DUPLICATE"
        if "parent_media" in doc:
            parent = docs[doc["parent_media"]["id"]]
            assert doc["id"] in {c["id"] for c in parent["variant_children"]}


@pytest.mark.parametrize("key", ITEMS)
def test_rebuild_is_deterministic_and_does_not_change_baseline(key):
    item, before, expected = records(key)
    original = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == original and after == expected
    assert claims == item["claims"] and lineage == item["lineage"]


def fixture_repo(tmp_path, monkeypatch):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    for item in ITEMS.values():
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
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

    # Real deterministic builders are checked above; exercise the write protocol
    # with those frozen decisions without repeating expensive PDF/schema reads.
    def builder(before, key, timestamp):
        assert timestamp == PLAN["created_at"] and before == DOCS[key][0]
        return copy.deepcopy((DOCS[key][1], ITEMS[key]["claims"], ITEMS[key]["lineage"]))

    monkeypatch.setattr(repair, "build", builder)
    path = tmp_path / "plan.json"
    path.write_text(json.dumps(PLAN))
    return path


def test_guarded_apply_readback_and_noop(tmp_path, monkeypatch):
    plan = fixture_repo(tmp_path, monkeypatch)
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 19
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 19
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0


def test_concurrent_edit_rejects_whole_batch_before_first_write(tmp_path, monkeypatch):
    plan = fixture_repo(tmp_path, monkeypatch)
    paths = [tmp_path / r["path"] for r in ITEMS.values()]
    paths[-1].write_text(paths[-1].read_text() + "# concurrent change\n")
    before = [p.read_bytes() for p in paths]
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(tmp_path, plan, "apply")
    assert [p.read_bytes() for p in paths] == before


def test_changed_capture_is_rejected():
    context = repair.frozen()
    context["sources"]["K119"]["raw"] += "changed"
    with pytest.raises(ValueError, match="Source capture drift"):
        repair.sources(context)
