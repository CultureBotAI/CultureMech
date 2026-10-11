"""Primary protocol stage arithmetic, evidence and guarded application."""

import copy
import json
import subprocess
from decimal import Decimal

import pytest
import repair_kaminskyj_stocks as repair


@pytest.fixture
def plan():
    return json.loads(repair.PLAN.read_text())


def docs(plan):
    item = plan["records"][0]
    return (
        repair.runner.load_yaml(item["before_text"]),
        repair.runner.load_yaml(item["after_text"]),
        item,
    )


def rehash(item, doc):
    item["after_text"] = repair.runner.render(item["before_text"], doc).decode()
    item["after_sha256"] = repair.runner.sha(item["after_text"].encode())


def test_recipe_quantities_and_independent_dilutions(plan):
    before, after, item = docs(plan)
    assert repair.check(before, after, item) == item["counts"]
    stocks = after["solutions"]
    assert [n["concentration"]["value"] for n in stocks[:3]] == ["50", "1", "1"]
    nitrate = [
        Decimal(n["concentration"]["value"]) * Decimal("0.050") for n in stocks[0]["composition"]
    ]
    assert nitrate == list(map(Decimal, ["6", "0.520", "0.520", "1.520"]))
    trace = [
        Decimal(n["concentration"]["value"]) * Decimal("0.001")
        for n in stocks[1]["composition"][:8]
    ]
    assert trace == list(
        map(Decimal, ["0.022", "0.011", "0.005", "0.005", "0.0017", "0.0016", "0.0015", "0.050"])
    )
    assert after["ingredients"][0]["concentration"] == {"value": "10", "unit": "G_PER_L"}
    assert "concentration" not in stocks[2]["composition"][0]
    assert "concentration" not in stocks[3]
    assert "concentration" not in stocks[1]["composition"][-1]
    assert "concentration" not in after["ingredients"][1]
    assert stocks[3]["composition"][0]["concentration"] == {"value": "1", "unit": "MOLAR"}
    assert after["ph_value"] == 6.5
    assert after["preparation_steps"][-1]["action"] == "AUTOCLAVE"
    assert after["physical_state"] == "LIQUID"
    assert len(item["claims"]) == 23


def test_provenance_and_supplied_forms(plan):
    before, after, item = docs(plan)
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after.get("target_organisms") == before.get("target_organisms")
    assert after["solutions"][0]["composition"][2]["term"]["id"] == "CHEBI:31795"
    assert "term" not in after["solutions"][1]["composition"][7]
    refs = after["references"]
    assert {r["reference"] for r in refs} == {repair.source()["url"], "doi:10.4148/1941-4765.1175"}
    assert all(r["year"] == 2001 and r["authors"] == "Susan G. W. Kaminskyj" for r in refs)
    assert all(
        c["evidence"]["snippet"] and c["evidence"]["reference"] == refs[0]["reference"]
        for c in item["claims"]
    )


@pytest.mark.parametrize("spec", repair.SPECS)
def test_each_rehashed_ingredient_quantity_forgery_rejected(plan, spec):
    before, after, item = docs(plan)
    node = repair.at(after, spec[3])
    node["concentration"] = {"value": "999", "unit": "G_PER_L"}
    rehash(item, after)
    item["claims"] = repair.claims(before, after)
    with pytest.raises(AssertionError):
        repair.check(before, after, item)


@pytest.mark.parametrize(
    "kind",
    [
        "dose",
        "stock_as_final",
        "initial_water_as_final",
        "thiamine_percent",
        "koh_zero",
        "naoh_fixed_dose",
        "water_fixed_dose",
        "anhydrous_identity",
        "mim_identity",
        "extra_salt",
        "missing_stock",
        "order",
        "snippet",
        "explanation",
        "history",
        "category",
        "variants",
        "temperature",
        "filtration",
        "doi",
        "per_volume",
    ],
)
def test_semantic_forgery_rejected_even_with_refreshed_claims(plan, kind):
    before, after, item = docs(plan)
    stocks = after["solutions"]
    if kind == "dose":
        stocks[0]["concentration"]["value"] = "1"
    elif kind == "stock_as_final":
        stocks[0]["composition"][0]["concentration"]["value"] = "6"
    elif kind == "initial_water_as_final":
        stocks[1]["composition"][0]["concentration"]["value"] = str(
            Decimal("2.2") / Decimal("0.060")
        )
    elif kind == "thiamine_percent":
        stocks[2]["composition"][0]["concentration"] = {"value": "1", "unit": "PERCENT_W_V"}
    elif kind == "koh_zero":
        stocks[1]["composition"][-1]["concentration"] = {"value": "0", "unit": "G_PER_L"}
    elif kind == "naoh_fixed_dose":
        stocks[3]["concentration"] = {"value": "1", "unit": "ML_PER_L"}
    elif kind == "water_fixed_dose":
        after["ingredients"][1]["concentration"] = {"value": "1000", "unit": "ML_PER_L"}
    elif kind in {"anhydrous_identity", "mim_identity"}:
        key = "term" if kind == "anhydrous_identity" else "mediaingredientmech_chebi_term"
        stocks[0]["composition"][2][key] = {"id": "CHEBI:32599", "label": "magnesium sulfate"}
    elif kind == "extra_salt":
        after["ingredients"].append(copy.deepcopy(stocks[0]["composition"][0]))
    elif kind == "missing_stock":
        stocks.pop()
    elif kind == "order":
        stocks[1]["composition"].reverse()
    elif kind in {"snippet", "explanation"}:
        stocks[0]["composition"][0]["evidence"][0][kind] = "Invented claim"
    elif kind == "history":
        after["curation_history"][0]["curator"] = "different"
    elif kind == "category":
        after["category"] = "fungal"
    elif kind == "variants":
        after["variants"][1]["modifications"] = ["Add 15 g agar"]
    elif kind == "temperature":
        after["preparation_steps"][-1]["temperature"] = "121 C"
    elif kind == "filtration":
        after["preparation_steps"][-1]["action"] = "FILTER_STERILIZE"
    elif kind == "doi":
        after["references"][1]["reference"] = "doi:10.1234/invented"
    else:
        stocks[1]["composition"][0]["concentration"]["per_volume"] = "100 mL"
    rehash(item, after)
    if kind not in {"missing_stock"}:
        item["claims"] = repair.claims(before, after)
    with pytest.raises((AssertionError, IndexError, KeyError)):
        repair.check(before, after, item)


def make_repo(tmp_path, plan, monkeypatch):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    target = tmp_path / repair.PATH
    target.parent.mkdir(parents=True)
    target.write_text(plan["records"][0]["before_text"])
    subprocess.run(["git", "add", "data"], cwd=tmp_path, check=True)
    monkeypatch.setattr(repair, "validate_recipe", lambda *a, **k: [])
    return target


def test_apply_readback_noop(plan, tmp_path, monkeypatch):
    target = make_repo(tmp_path, plan, monkeypatch)
    assert repair.apply(plan, tmp_path) == {"changed": 1, "already_applied": 0}
    assert repair.apply(plan, tmp_path) == {"changed": 0, "already_applied": 1}
    assert repair.apply(plan, tmp_path, verify=True) == {"changed": 0, "already_applied": 1}
    assert target.read_text() == plan["records"][0]["after_text"]


@pytest.mark.parametrize(
    "kind",
    [
        "drift",
        "duplicate",
        "outside",
        "symlink",
        "ancestor_symlink",
        "verify_before_apply",
        "source",
        "version",
        "counts",
        "class",
        "invalid_shape",
    ],
)
def test_guard_rejects_without_writing(plan, tmp_path, monkeypatch, kind):
    target = make_repo(tmp_path, plan, monkeypatch)
    if kind == "drift":
        target.write_text(target.read_text() + "\n# concurrent edit\n")
    elif kind == "duplicate":
        plan["records"].append(copy.deepcopy(plan["records"][0]))
    elif kind == "outside":
        plan["records"][0]["path"] = "../outside.yaml"
    elif kind == "symlink":
        saved = tmp_path / "saved.yaml"
        target.rename(saved)
        target.symlink_to(saved)
    elif kind == "ancestor_symlink":
        parent = target.parent
        saved = tmp_path / "saved-dir"
        parent.rename(saved)
        parent.symlink_to(saved, target_is_directory=True)
    elif kind == "source":
        plan["source_sha256"] = "0" * 64
    elif kind == "version":
        plan["version"] = 999
    elif kind == "counts":
        plan["records"][0]["counts"]["new_evidence"] = 21
    elif kind == "class":
        plan["records"][0]["target_class"] = "SolutionRecipe"
    elif kind == "invalid_shape":
        monkeypatch.setattr(repair, "validate_recipe", lambda *a, **k: ["test rejection"])
    original = target.read_bytes()
    with pytest.raises((AssertionError, ValueError)):
        repair.apply(plan, tmp_path, verify=kind == "verify_before_apply")
    assert target.read_bytes() == original
