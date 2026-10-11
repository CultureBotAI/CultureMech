"""Exact-source OTEB scope, independent tampering checks and guarded writes."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_oteb_family as repair

from culturemech.merge.formulation import formulation_content
from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merger import RecipeMerger
from culturemech.validation.write_validated import infer_target_class

spec = importlib.util.spec_from_file_location("oteb_audit", repair.HERE / "audit.py")
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
def test_source_projection_accounts_for_every_old_quantity_and_source_node(key):
    item, before, after = records(key)
    result = audit.check(before, after, item)
    assert result["source_nodes"] == len(item["lineage"])
    assert result["old_quantity_slots"] == sum("concentration" in n for _, n in audit.walk(before))


@pytest.mark.parametrize(
    "key,path", [(key, row["pointer"]) for key, item in ITEMS.items() for row in item["lineage"]]
)
def test_each_node_rejects_an_invented_quantity_even_after_rehashing(key, path):
    item, before, after = records(key)
    audit.get(after, path)["concentration"] = {"value": "987654", "unit": "G_PER_L"}
    item["after_text"] = repair.runner.render(item["before_text"], after).decode()
    item["after_sha256"] = repair.runner.sha(item["after_text"].encode())
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
        "identity",
    ],
)
def test_corrupt_formulation_evidence_or_accounting_is_rejected(key, mutation):
    item, before, after = records(key)
    field = "composition" if key.startswith("S") else "ingredients"
    first = after[field][0]
    if mutation == "omit":
        after[field].pop()
    elif mutation == "extra":
        after[field].append(copy.deepcopy(first))
    elif mutation == "grounding":
        first["term"] = {"id": "CHEBI:123", "label": "invented"}
    elif mutation == "snippet":
        first["evidence"][0]["snippet"] = "invented source quotation"
    elif mutation == "duplicate_evidence":
        first["evidence"].append(copy.deepcopy(first["evidence"][0]))
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "rewritten history"
    elif mutation == "claim":
        item["claims"].pop()
    elif mutation == "lineage":
        item["lineage"].pop()
    elif mutation == "title":
        after["references"][0]["title"] = "Wrong source"
    elif mutation == "year":
        after["references"][0]["year"] = 2025
    elif mutation == "old_value":
        item["claims"][0]["old"] = "not the reviewed prior value"
    else:
        after["id"] = "CultureMech:999999"
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


def test_duplicate_maltose_is_retained_without_deduplication_or_summing():
    original = DOCS["D1245"][1]["solutions"][1]["composition"]
    maltose = [n for n in original if n["preferred_term"] == "Maltose"]
    assert len(maltose) == 2 and all(
        "8.0 g per preparation" in n["notes"] and "concentration" not in n for n in maltose
    )
    stock = [n for n in DOCS["S5688"][1]["composition"] if n["preferred_term"] == "Maltose"]
    assert len(stock) == 2 and all(
        n["concentration"] == {"value": "8", "unit": "G_PER_L"} for n in stock
    )
    for key, value in (("K1245", "1.60"), ("K6000", "16.00")):
        rows = [n for n in DOCS[key][1]["ingredients"] if n["preferred_term"] == "Maltose"]
        assert len(rows) == 1 and rows[0]["concentration"] == {"value": value, "unit": "G_PER_L"}


def test_serum_variant_retains_both_source_rows_and_does_not_substitute():
    base = DOCS["K1245"][1]
    variant = DOCS["K1245_18691"][1]
    a = {n["preferred_term"]: n.get("concentration") for n in base["ingredients"]}
    b = {n["preferred_term"]: n.get("concentration") for n in variant["ingredients"]}
    assert set(b) - set(a) == {"fetal bovine serum"}
    assert all(b[k] == v for k, v in a.items())
    assert b["Calf Serum"] == {"value": "99.70", "unit": "G_PER_L"}
    assert b["fetal bovine serum"] == {"value": "100.00", "unit": "G_PER_L"}
    assert "ph_range" not in variant
    assert variant["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"
    assert base["variant_children"][0]["relationship"] == variant["variant_relationship"]
    original = [n for n in DOCS["D1245"][1]["ingredients"] if "Serum" in n["preferred_term"]]
    assert len(original) == 1 and original[0]["preferred_term"] == "Calf Serum, inactivated"
    assert original[0]["concentration"] == {"value": "0.1", "unit": "L"}
    assert "Identity conflict" in original[0]["notes"]


def test_original_input_volumes_do_not_become_concentrations_or_mass():
    after = DOCS["D1245"][1]
    nodes = {n["preferred_term"]: n for n in after["ingredients"]}
    assert "concentration" not in nodes["Proteose peptone no. 2"]
    assert nodes["Acetic acid"]["concentration"] == {"value": "0.0016", "unit": "L"}
    assert nodes["Distilled water"]["concentration"] == {"value": "0.8", "unit": "L"}
    vitamin, sugar = after["solutions"]
    assert vitamin["concentration"] == {"value": "0.0001", "unit": "L"}
    assert "concentration" not in vitamin["composition"][0]
    assert "1%" in vitamin["composition"][0]["notes"]
    assert sugar["concentration"] == {"value": "0.1", "unit": "L"}
    assert sugar["composition"][-1]["concentration"] == {"value": "1", "unit": "L"}
    assert "750.0" in sugar["composition"][-2]["notes"]
    assert "preparation_steps" not in after
    assert "1003.1" in after["notes"] and "25 C is a measurement condition" in after["notes"]


@pytest.mark.parametrize("key,count", [("S2474", 6), ("S5688", 9)])
def test_prior_qualified_evidence_is_preserved_exactly(key, count):
    before, after = DOCS[key]
    prior = [(i, e) for i, n in enumerate(before["composition"]) for e in n.get("evidence", [])]
    assert len(prior) == count
    for i, evidence in prior:
        assert evidence in after["composition"][i]["evidence"]
        assert before["composition"][i]["concentration"] == after["composition"][i]["concentration"]
    assert infer_target_class(after) == "SolutionRecipe"
    assert "source_data" not in after and "evidence" not in after


def test_standalone_sugar_input_has_its_own_evidence_and_exact_stock_identity():
    node = DOCS["S2474"][1]["composition"][17]
    assert node["culturemech_term"]["id"] == DOCS["S5688"][1]["id"]
    assert node["concentration"] == {"value": "0.1", "unit": "L"}
    assert '"solution_id": 5688' in node["evidence"][0]["snippet"]
    assert (
        DOCS["S2474"][1]["composition"][3]["chebi_term"]
        == DOCS["S2474"][0]["composition"][3]["chebi_term"]
    )


def test_provider_nulls_and_conflicting_thiamine_alias_are_not_resolved_by_guessing():
    for key in ("K1245", "K1245_18691", "K6000"):
        nodes = {n["preferred_term"]: n for n in DOCS[key][1]["ingredients"]}
        assert "concentration" not in nodes["Distilled Water"]
        assert "Thiamine-HCl" in nodes["Thiamine Pyrophosphate"]["notes"]
        assert "term" not in nodes["Thiamine Pyrophosphate"]
        if key != "K6000":
            assert "concentration" not in nodes["Vitamin K1"]
            assert "concentration" not in nodes["Acetic Acid"]
    stock = DOCS["K6000"][1]
    assert infer_target_class(stock) == "MediaRecipe" and stock["record_kind"] == "SOLUTION"
    assert formulation_content(stock)["record_kind"] == "SOLUTION"


def test_merge_preview_retains_distinct_source_formulations_and_claims(tmp_path):
    paths = []
    for key, item in ITEMS.items():
        path = tmp_path / (key + ".yaml")
        path.write_text(item["after_text"])
        paths.append(path)
    matcher = RecipeMatcher()
    groups = matcher.group_formulations(paths)
    assert matcher._last_skip_stats["excluded_solutions"] == 2
    assert len(groups) == 4
    for paths in groups.values():
        assert len(paths) == 1
        merged = RecipeMerger().merge_group(paths)
        source = DOCS[paths[0].stem][1]
        assert all(merged[key] == value for key, value in source.items())


@pytest.mark.parametrize("key", ITEMS)
def test_rebuild_is_deterministic_and_does_not_mutate_baseline(key):
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

    def builder(before, key, timestamp):
        assert timestamp == PLAN["created_at"] and before == DOCS[key][0]
        return copy.deepcopy((DOCS[key][1], ITEMS[key]["claims"], ITEMS[key]["lineage"]))

    monkeypatch.setattr(repair, "build", builder)
    plan = tmp_path / "plan.json"
    plan.write_text(json.dumps(PLAN))
    return plan


def test_guarded_apply_readback_and_noop(tmp_path, monkeypatch):
    plan = fixture_repo(tmp_path, monkeypatch)
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 6
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 6
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0


def test_late_concurrent_edit_prevents_first_write(tmp_path, monkeypatch):
    plan = fixture_repo(tmp_path, monkeypatch)
    paths = [tmp_path / r["path"] for r in ITEMS.values()]
    paths[-1].write_text(paths[-1].read_text() + "# concurrent change\n")
    before = [p.read_bytes() for p in paths]
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(tmp_path, plan, "apply")
    assert [p.read_bytes() for p in paths] == before


def test_symlink_prevents_batch_write(tmp_path, monkeypatch):
    plan = fixture_repo(tmp_path, monkeypatch)
    path = tmp_path / next(iter(ITEMS.values()))["path"]
    target = tmp_path / "outside.yaml"
    target.write_bytes(path.read_bytes())
    path.unlink()
    path.symlink_to(target)
    with pytest.raises(ValueError, match="symlink"):
        repair.process(tmp_path, plan, "apply")


def test_capture_change_is_rejected():
    context = repair.frozen()
    context["sources"]["K1245"]["raw"] += "changed"
    with pytest.raises(ValueError, match="Source capture drift"):
        repair.sources(context)
