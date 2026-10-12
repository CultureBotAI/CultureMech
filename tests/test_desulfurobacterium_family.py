"""Source-boundary, evidence preservation and guarded-writer tests for medium 829."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_desulfurobacterium_family as repair

from culturemech.merge.fingerprint import RecipeFingerprinter
from culturemech.merge.formulation import formulation_content
from culturemech.merge.matcher import RecipeMatcher
from culturemech.merge.merger import RecipeMerger
from culturemech.validation.write_validated import infer_target_class

spec = importlib.util.spec_from_file_location("medium829_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads(repair.PLAN_PATH.read_text())
ITEMS = {r["key"]: r for r in PLAN["records"]}
DOCS = {
    k: (repair.runner.load_yaml(r["before_text"]), repair.runner.load_yaml(r["after_text"]))
    for k, r in ITEMS.items()
}


def records(key):
    return copy.deepcopy((ITEMS[key], *DOCS[key]))


@pytest.mark.parametrize("key", ITEMS)
def test_independent_source_projection_accounts_for_every_old_quantity_and_new_node(key):
    item, before, after = records(key)
    result = audit.check(before, after, item)
    assert result["source_nodes"] == len(item["lineage"])
    assert result["old_quantity_slots"] == sum("concentration" in n for _, n in audit.walk(before))


@pytest.mark.parametrize(
    "key,path", [(key, row["pointer"]) for key, item in ITEMS.items() for row in item["lineage"]]
)
def test_every_source_node_rejects_an_invented_quantity(key, path):
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
        "identity",
    ],
)
def test_corrupt_formulation_evidence_or_accounting_is_rejected(key, mutation):
    item, before, after = records(key)
    field = "composition" if key == "S1680" else "ingredients"
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


@pytest.mark.parametrize("key", ["K829.1", "K829.2", "K829.3", "K829_16661"])
def test_list_index_candidates_are_archived_without_promoting_inferred_doses(key):
    item, before, after = records(key)
    candidates = [c for c in item["claims"] if c["kind"] == "old_candidate_accounted"]
    assert len(candidates) == 2 and "solutions" not in after
    for claim in candidates:
        assert claim["old"] == audit.get(before, claim["old_pointer"])
        assert claim["old"]["basis"] == "CROSS_MEDIUM_INFERENCE"
    candidates[0]["old"] = None
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


def test_genuine_yeast_is_preserved_but_false_lb_is_removed():
    after = DOCS["D829b"][1]
    yeast = [n for n in after["ingredients"] if n["preferred_term"] == "Yeast extract"]
    assert len(yeast) == 1 and yeast[0]["concentration"] == {"value": "0.497512", "unit": "G_PER_L"}
    assert not any(
        "LB Medium" in n.get("supplier_catalog", {}).get("supplier_name", "")
        for _, n in audit.walk(after)
    )
    assert "110" not in after["preparation_steps"][0]["description"]
    assert "2 bar" in after["preparation_steps"][1]["description"]


def stock(key, name):
    return next(n for n in DOCS[key][1]["solutions"] if n["preferred_term"] == name)


def test_dithionite_carriers_remain_distinct_with_strength_and_receiving_dose():
    current = stock("D829", "Na-dithionite solution (5% w/v)")
    togo = stock("M2587", "Na-dithionite solution (5% w/v)")
    assert current["concentration"] == togo["concentration"] == {"value": "0.001", "unit": "L"}
    nodes = {n["preferred_term"]: n for n in current["composition"]}
    assert (
        nodes["NaOH"]["concentration"] == {"value": "0.0005", "unit": "L"}
        and "1 N" in nodes["NaOH"]["notes"]
    )
    assert nodes["Na2S2O4"]["concentration"] == {"value": "5", "unit": "PERCENT_W_V"}
    nodes = {n["preferred_term"]: n for n in togo["composition"]}
    assert "NaOH" not in nodes and "50 g" in nodes["NaHCO3"]["notes"]
    assert "concentration" not in nodes["NaHCO3"]
    assert nodes["Distilled water"]["concentration"] == {"value": "1", "unit": "L"}
    assert nodes["Na2S2O4"]["concentration"] == {"value": "5", "unit": "PERCENT_W_V"}


def test_no_denominator_is_invented_from_water_or_vessel_size():
    after = DOCS["D829a"][1]
    assert all(
        "concentration" not in n
        for n in after["ingredients"]
        if n["preferred_term"] != "Distilled water"
    )
    sulfide = stock("D829a", "Neutralized sulfide solution 3% (w/v)")
    assert sulfide["concentration"] == {"value": "0.02", "unit": "L"}
    assert sulfide["composition"][0]["concentration"] == {"value": "3", "unit": "PERCENT_W_V"}
    assert "concentration" not in sulfide["composition"][-1]
    assert "2 M" in sulfide["composition"][-1]["notes"]
    for key in ("D829", "D829b"):
        growth = stock(key, "Growth-stimulating factors")
        assert [n["preferred_term"] for n in growth["composition"][-2:]] == [
            "Distilled water",
            "NaOH",
        ]
        assert all(
            "concentration" not in n
            for n in growth["composition"]
            if n["preferred_term"] != "Distilled water"
        )


@pytest.mark.parametrize("key", ["D829c", "D829d"])
def test_wolin_b12_is_one_mg_not_the_seven_vitamin_recipe(key):
    vitamins = stock(key, "Wolin's vitamin solution (10x)")
    b12 = next(n for n in vitamins["composition"] if n["preferred_term"] == "Vitamin B12")
    assert "1 mg" in b12["notes"] and "concentration" not in b12
    assert vitamins["concentration"] == {"value": "0.001", "unit": "L"}
    minerals = stock(key, "Modified Wolin's mineral solution")
    assert (
        minerals["composition"][-1]["preferred_term"] == "KOH"
        and "concentration" not in minerals["composition"][-1]
    )


def test_solution_shape_and_semantic_stock_marker_are_not_conflated():
    before, after = DOCS["S1680"]
    assert after["composition"][:6] == before["composition"][:6]
    assert after["references"][0]["title"] == "Growth-stimulating factors"
    titles = [c for c in ITEMS["S1680"]["claims"] if c["kind"] == "bibliographic_title"]
    assert len(titles) == 1 and titles[0]["old"] == before["references"][0]["title"]
    assert infer_target_class(after) == "SolutionRecipe" and "source_data" not in after
    assert after["composition"][6]["concentration"] == {"value": "1", "unit": "L"}
    with pytest.raises(ValueError, match="SolutionRecipe"):
        RecipeFingerprinter().fingerprint(after)
    komodo = DOCS["K2027"][1]
    assert infer_target_class(komodo) == "MediaRecipe" and komodo["record_kind"] == "SOLUTION"
    assert formulation_content(komodo)["record_kind"] == "SOLUTION"
    unmarked = copy.deepcopy(komodo)
    del unmarked["record_kind"]
    assert formulation_content(komodo) != formulation_content(unmarked)


def test_repaired_source_versions_merge_without_losing_scoped_claims(tmp_path):
    paths = []
    for key, item in ITEMS.items():
        path = tmp_path / (key + ".yaml")
        path.write_text(item["after_text"])
        paths.append(path)
    matcher = RecipeMatcher()
    groups = matcher.group_formulations(paths)
    assert matcher._last_skip_stats["excluded_solutions"] == 1
    assert len(groups) == 13
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
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 14
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 14
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
    context["sources"]["K829"]["raw"] += "changed"
    with pytest.raises(ValueError, match="Capture drift"):
        repair.sources(context)
