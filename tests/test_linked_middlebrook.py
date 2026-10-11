"""Challenge source rates, alternatives, hemin scope, family links and guarded writes."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_linked_middlebrook as repair

spec = importlib.util.spec_from_file_location("linked_middlebrook_audit", repair.HERE / "audit.py")
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
def test_all_source_projections_and_original_quantity_accounting(key):
    item, before, expected = records(key)
    original = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == original and after == expected
    assert claims == item["claims"] and lineage == item["lineage"]
    assert audit.check(before, after, item)["old_quantity_slots"] >= 20


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "quantity",
        "omit",
        "extra",
        "mapping",
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
def test_independent_audit_rejects_corruption(key, mutation):
    item, before, after = records(key)
    node = after["ingredients"][0]
    if mutation == "quantity":
        node["concentration"] = {"value": "100", "unit": "G_PER_L"}
    elif mutation == "omit":
        after["ingredients"].pop()
    elif mutation == "extra":
        after["ingredients"].append(copy.deepcopy(node))
    elif mutation == "mapping":
        node["term"] = {"id": "CHEBI:123", "label": "invented"}
    elif mutation == "snippet":
        node["evidence"][0]["snippet"] = "fabricated quotation"
    elif mutation == "duplicate_evidence":
        after["evidence"].append(copy.deepcopy(after["evidence"][0]))
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif mutation == "claim":
        item["claims"].pop()
    elif mutation == "lineage":
        item["lineage"].pop()
    elif mutation == "title":
        after["references"][0]["title"] = "Another source"
    elif mutation == "year":
        after["references"][0]["year"] = 2008
    elif mutation == "old_value":
        item["claims"][0]["old"] = {"value": "1000", "unit": "G_PER_L"}
    elif mutation == "family":
        link = after["parent_media"] if "parent_media" in after else after["variant_children"][0]
        link["relationship"] = "SOURCE_DUPLICATE"
    else:
        after["notes"] = "Corrected."
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


def test_alternative_is_not_a_simultaneous_canonical_formulation():
    item, before, after = records("D645")
    assert [n["preferred_term"] for n in after["ingredients"]] == [
        "Bacto Middlebrook 7H10 agar",
        "Glycerol",
        "Distilled water",
    ]
    assert after["ingredients"][1]["concentration"] == {"value": "0.005", "unit": "L"}
    assert after["ingredients"][2]["concentration"] == {"value": "0.9", "unit": "L"}
    assert any("Distilled water 1000 ml" in v for v in after["variants"][0]["modifications"])
    after["variants"][0]["modifications"][
        0
    ] = "Add another 0.5 g ammonium sulfate to the commercial route."
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


def test_oadc_and_commercial_base_have_distinct_quantity_scopes():
    for key in ("D645", "D911"):
        _, _, after = records(key)
        stock = after["solutions"][-1]
        assert stock["concentration"] == {"value": "0.1", "unit": "L"}
        assert stock["composition"][1]["concentration"] == {"value": "50", "unit": "G_PER_L"}
        assert stock["composition"][3]["concentration"] == {"value": "0.04", "unit": "G_PER_L"}
    _, _, after = records("D911")
    assert "concentration" not in after["solutions"][0]
    assert all("concentration" not in n for n in after["solutions"][0]["composition"][:-1])


def test_hemin_is_not_converted_to_an_unsupported_molarity_or_naoh_dose():
    item, before, after = records("K645a")
    hemin = next(n for n in after["ingredients"] if n["preferred_term"] == "hemin")
    hemin["concentration"] = {"value": "60", "unit": "MICROMOLAR"}
    with pytest.raises(AssertionError):
        audit.check(before, after, item)
    item, before, after = records("K645a")
    sodium_hydroxide = next(n for n in after["ingredients"] if n["preferred_term"] == "NAOH")
    sodium_hydroxide["concentration"] = {"value": "0", "unit": "L"}
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


def test_genuine_casein_and_salt_are_not_removed_with_false_lb_nodes():
    for key in ("K911", "K911_44536"):
        _, _, after = records(key)
        nodes = {n["preferred_term"]: n for n in after["ingredients"]}
        assert nodes["Pancreatic digest of casein"]["concentration"] == {
            "value": "0.55",
            "unit": "G_PER_L",
        }
        assert nodes["NaCl"]["concentration"] == {"value": "0.42", "unit": "G_PER_L"}
        assert "Tryptone" not in nodes and "Yeast extract" not in nodes


def test_complete_family_forest_is_reciprocal_and_acyclic():
    docs = {item["path"]: repair.runner.load_yaml(item["after_text"]) for item in ITEMS.values()}
    parents = {p: doc["parent_media"]["path"] for p, doc in docs.items() if doc.get("parent_media")}
    assert len(parents) == 9
    for child, parent in parents.items():
        refs = [r for r in docs[parent]["variant_children"] if r["path"] == child]
        assert len(refs) == 1
        assert refs[0]["id"] == docs[child]["id"]
        assert refs[0]["relationship"] == docs[child]["parent_media"]["relationship"]
        seen = set()
        while child in parents:
            assert child not in seen
            seen.add(child)
            child = parents[child]


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
    original = [p.read_bytes() for p in targets]
    repair.process(tmp_path, plan, "preview")
    assert [p.read_bytes() for p in targets] == original
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 11
    current = [p.read_bytes() for p in targets]
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 11
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert [p.read_bytes() for p in targets] == current


def test_concurrent_edit_prevents_all_writes(tmp_path, monkeypatch):
    targets = fixture_repo(tmp_path, monkeypatch)
    plan = tmp_path / "plan.json"
    repair.process(tmp_path, plan, "preview")
    targets[-1].write_text(targets[-1].read_text() + "# concurrent change\n")
    current = [p.read_bytes() for p in targets]
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(tmp_path, plan, "apply")
    assert [p.read_bytes() for p in targets] == current
