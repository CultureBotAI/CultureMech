"""Independent source projection, provenance preservation and medium330 attacks."""

import copy
import importlib.util
import json
import subprocess
from decimal import Decimal

import pytest
import repair_rumen_bacteria_family as repair

spec = importlib.util.spec_from_file_location("rumen_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())
ITEMS = {r["key"]: r for r in PLAN["records"]}
DOCS = {
    k: (repair.runner.load_yaml(r["before_text"]), repair.runner.load_yaml(r["after_text"]))
    for k, r in ITEMS.items()
}


@pytest.mark.parametrize("key", ITEMS)
def test_independent_projection_covers_all_old_quantities_and_source_nodes(key):
    before, after = copy.deepcopy(DOCS[key])
    result = audit.check(before, after, ITEMS[key])
    assert result["source_nodes"] == len(ITEMS[key]["lineage"])
    assert result["old_quantity_slots"] == sum("concentration" in n for _, n in audit.walk(before))


@pytest.mark.parametrize(
    "key,path", [(k, row["pointer"]) for k, r in ITEMS.items() for row in r["lineage"]]
)
def test_each_source_node_rejects_invented_amount_even_after_rehash(key, path):
    item = copy.deepcopy(ITEMS[key])
    before, after = copy.deepcopy(DOCS[key])
    audit.get(after, path)["concentration"] = {"value": "876543", "unit": "G_PER_L"}
    # Forgery checks need valid YAML, not repeated production formatting.
    item["after_text"] = json.dumps(after, ensure_ascii=False)
    item["after_sha256"] = repair.runner.sha(item["after_text"].encode())
    with pytest.raises(AssertionError):
        audit.check(before, after, item)


@pytest.mark.parametrize("key", ITEMS)
def test_forgery_serialization_accepts_every_unchanged_record(key):
    item = copy.deepcopy(ITEMS[key])
    before, after = copy.deepcopy(DOCS[key])
    item["after_text"] = json.dumps(after, ensure_ascii=False)
    item["after_sha256"] = repair.runner.sha(item["after_text"].encode())
    assert repair.runner.load_yaml(item["after_text"]) == after
    assert audit.check(before, after, item)["source_nodes"] == len(item["lineage"])


@pytest.mark.parametrize("key", ITEMS)
@pytest.mark.parametrize(
    "mutation",
    [
        "omit",
        "extra",
        "grounding",
        "snippet",
        "history",
        "claim",
        "lineage",
        "title",
        "year",
        "old_value",
        "identity",
    ],
)
def test_provenance_and_formulation_corruption_is_rejected(key, mutation):
    item = copy.deepcopy(ITEMS[key])
    before, after = copy.deepcopy(DOCS[key])
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
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "rewritten history"
    elif mutation == "claim":
        item["claims"].pop()
    elif mutation == "lineage":
        item["lineage"].pop()
    elif mutation == "title":
        after["references"][0]["title"] = "Wrong recipe"
    elif mutation == "year":
        after["references"][0]["year"] = 2026
    elif mutation == "old_value":
        item["claims"][0]["old"] = "not the old value"
    else:
        after["id"] = "CultureMech:999999"
    with pytest.raises((AssertionError, KeyError, IndexError)):
        audit.check(before, after, item)


@pytest.mark.parametrize("key", ITEMS)
def test_rebuild_is_deterministic_without_modifying_baseline(key):
    before, expected = copy.deepcopy(DOCS[key])
    original = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == original and after == expected
    assert claims == ITEMS[key]["claims"] and lineage == ITEMS[key]["lineage"]


def test_variant_changes_sixteen_rates_and_adds_provider_rumen_fluid_not_density_conversion():
    base = {n["preferred_term"]: n.get("concentration") for n in DOCS["K330"][1]["ingredients"]}
    variant = DOCS["K330_17630"][1]
    rows = {n["preferred_term"]: n.get("concentration") for n in variant["ingredients"]}
    assert set(rows) - set(base) == {"rumen fluid"}
    assert sum(rows[k] != v for k, v in base.items()) == 16
    assert rows["rumen fluid"] == {"value": "29.13", "unit": "G_PER_L"}
    assert base["Resazurin"]["value"] == "9.99E-4" and rows["Resazurin"]["value"] == "9.70E-4"
    assert "ph_value" not in variant and "ph_range" not in variant
    assert variant["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"
    for key in ("K330", "K330_17630"):
        node = next(n for n in DOCS[key][1]["ingredients"] if n["preferred_term"] == "Resazurin")
        assert (
            not {"term", "chebi_term", "mediaingredientmech_chebi_term", "mediaingredientmech_term"}
            & node.keys()
        )
        assert "salt-specific grounding" in node["evidence"][0]["explanation"]


def test_original_nominal_denominator_is_not_sum_of_input_volumes():
    after = DOCS["D330"][1]
    masses = [
        n for n in after["ingredients"] if n.get("concentration", {}).get("unit") == "G_PER_L"
    ]
    assert len(masses) == 11
    assert (
        next(n for n in masses if n["preferred_term"] == "K2HPO4")["concentration"]["value"]
        == "0.299103"
    )
    assert all("1.003 L" in n["evidence"][0]["explanation"] for n in masses)
    assert "1003.6 ml" in after["notes"]
    mineral, acids, hemin = after["solutions"]
    assert [s["concentration"]["unit"] for s in after["solutions"]] == ["L"] * 3
    assert all("concentration" not in n for n in mineral["composition"][:5])
    assert all(n["concentration"]["unit"] == "L" for n in acids["composition"])
    assert "concentration" not in hemin["composition"][2]
    assert hemin["composition"][0]["concentration"] == {"value": "0.5", "unit": "G_PER_L"}
    assert "1 N" in hemin["composition"][1]["preferred_term"]


@pytest.mark.parametrize("key", ["DJ1029", "M1093"])
def test_unavailable_original_does_not_acquire_neighbor_denominator(key):
    after = DOCS[key][1]
    assert "Original JCM1029 is unavailable" in after["notes"]
    quantities = [
        n["concentration"]
        for p, n in audit.walk(after)
        if p and p[0] in {"ingredients", "solutions"} and "concentration" in n
    ]
    assert quantities and all(q["unit"] == "L" for q in quantities)
    assert len(after["solutions"]) == 2
    assert len(after["solutions"][1]["composition"]) == 7
    assert sum(
        Decimal(n["concentration"]["value"]) for n in after["solutions"][1]["composition"]
    ) == Decimal("0.031")


def test_togo_water_and_mg_inputs_are_not_collapsed_or_treated_as_grams():
    after = DOCS["M1093"][1]
    water = [n for n in after["ingredients"] if n["preferred_term"] == "Distilled water"]
    assert water[0]["concentration"] == {"value": "0.96", "unit": "L"}
    assert after["solutions"][0]["composition"][0]["concentration"] == {"value": "1", "unit": "L"}
    for label in ("Hemin", "Resazurin"):
        node = next(n for n in after["ingredients"] if n["preferred_term"] == label)
        assert "1 mg" in node["notes"] and "concentration" not in node
    assert len(after["ingredients"]) == 15


def test_thirteen_prior_evidence_entries_preserve_exact_paths_and_values():
    count = 0
    for key in ("S124", "S5080", "S607"):
        before, after = DOCS[key]
        for i, old in enumerate(before["composition"]):
            for j, evidence in enumerate(old.get("evidence", [])):
                assert after["composition"][i]["evidence"][j] == evidence
                assert after["composition"][i]["concentration"] == old["concentration"]
                count += 1
    assert count == 13
    assert len(DOCS["S607"][1]["composition"][0]["evidence"]) == 2
    assert (
        DOCS["S607"][1]["composition"][0]["evidence"][1]["reference"]
        == "https://mediadive.dsmz.de/rest/medium/330"
    )


@pytest.mark.parametrize("key", ["S3774", "S608"])
def test_all_seven_acid_inputs_are_volumes_not_percentages_or_density_estimates(key):
    assert len(DOCS[key][1]["composition"]) == 7
    assert all(n["concentration"]["unit"] == "L" for n in DOCS[key][1]["composition"])


def test_haemin_makeup_water_and_resazurin_stock_strength_stay_explicit():
    haemin = DOCS["S124"][1]["composition"]
    assert haemin[1]["concentration"] == {"value": "0.001", "unit": "L"}
    assert "1 N" in haemin[1]["notes"] and "concentration" not in haemin[2]
    resazurin = DOCS["S606"][1]["composition"][4]
    assert resazurin["concentration"] == {"value": "0.0005", "unit": "L"}
    assert "0.1% w/v" in resazurin["notes"]


@pytest.mark.parametrize("key", [k for k in ITEMS if k not in {"K330", "K330_17630"}])
def test_unrelated_parent_link_cannot_be_inserted(key):
    before, after = copy.deepcopy(DOCS[key])
    after["parent_media"] = {"id": "CultureMech:999999", "relationship": "SOURCE_DUPLICATE"}
    with pytest.raises(AssertionError):
        audit.check(before, after, ITEMS[key])


@pytest.mark.parametrize("key", [k for k in ITEMS if k not in {"K330", "D330"}])
def test_unrelated_child_link_cannot_be_inserted(key):
    before, after = copy.deepcopy(DOCS[key])
    after["variant_children"] = [{"id": "CultureMech:999999", "relationship": "SOURCE_DUPLICATE"}]
    with pytest.raises(AssertionError):
        audit.check(before, after, ITEMS[key])


def test_invalid_mode_is_rejected(tmp_path):
    with pytest.raises(ValueError, match="Invalid mode"):
        repair.process(tmp_path, tmp_path / "plan.json", "unknown")


@pytest.mark.parametrize("constant", ["CONTEXT_SHA", "PREPARATION_SHA"])
def test_capture_and_preparation_hashes_are_mandatory(monkeypatch, constant):
    monkeypatch.setattr(repair, constant, "0" * 64)
    with pytest.raises(ValueError, match="drift"):
        repair.frozen()


@pytest.mark.parametrize("target", ["DJ1029", "K3131"])
@pytest.mark.parametrize("mutation", ["concurrent", "symlink"])
def test_one_changed_or_linked_cohort_record_prevents_preview_writes(tmp_path, target, mutation):
    context, _ = repair.frozen()
    paths = {}
    for item in context["records"]:
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
        paths[item["key"]] = path
    if mutation == "concurrent":
        paths[target].write_text(paths[target].read_text() + "# concurrent edit\n")
    else:
        outside = tmp_path / "outside.yaml"
        outside.write_bytes(paths[target].read_bytes())
        paths[target].unlink()
        paths[target].symlink_to(outside)
    before = {k: p.read_bytes() for k, p in paths.items()}
    with pytest.raises(ValueError, match="baseline drift|Cohort symlink"):
        repair.process(tmp_path, tmp_path / "proposal.json")
    assert not (tmp_path / "proposal.json").exists()
    assert before == {k: p.read_bytes() for k, p in paths.items()}


def fixture_repo(tmp_path, monkeypatch):
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    context, _ = repair.frozen()
    for item in context["records"]:
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
        assert before == DOCS[key][0] and timestamp == PLAN["created_at"]
        return copy.deepcopy((DOCS[key][1], ITEMS[key]["claims"], ITEMS[key]["lineage"]))

    monkeypatch.setattr(repair, "build", builder)
    plan = tmp_path / "plan.json"
    plan.write_bytes((repair.HERE / "plan.json").read_bytes())
    return plan, context


def test_guarded_apply_readback_and_noop(tmp_path, monkeypatch):
    plan, _ = fixture_repo(tmp_path, monkeypatch)
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 13
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 13
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0


@pytest.mark.parametrize("target", ["DJ1029", "K3131"])
def test_concurrent_edit_prevents_every_application_write(tmp_path, monkeypatch, target):
    plan, context = fixture_repo(tmp_path, monkeypatch)
    paths = {r["key"]: tmp_path / r["path"] for r in context["records"]}
    paths[target].write_text(paths[target].read_text() + "# concurrent edit\n")
    before = {k: p.read_bytes() for k, p in paths.items()}
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(tmp_path, plan, "apply")
    assert before == {k: p.read_bytes() for k, p in paths.items()}


@pytest.mark.parametrize("target", ["K330", "K3131"])
def test_symlink_prevents_every_application_write(tmp_path, monkeypatch, target):
    plan, context = fixture_repo(tmp_path, monkeypatch)
    paths = {r["key"]: tmp_path / r["path"] for r in context["records"]}
    outside = tmp_path / "outside.yaml"
    outside.write_bytes(paths[target].read_bytes())
    paths[target].unlink()
    paths[target].symlink_to(outside)
    before = {k: p.read_bytes() for k, p in paths.items()}
    with pytest.raises(ValueError, match="symlink"):
        repair.process(tmp_path, plan, "apply")
    assert before == {k: p.read_bytes() for k, p in paths.items()}


def test_changed_plan_is_not_apply_authority(tmp_path, monkeypatch):
    plan, _ = fixture_repo(tmp_path, monkeypatch)
    changed = copy.deepcopy(PLAN)
    changed["records"].pop()
    plan.write_text(json.dumps(changed))
    with pytest.raises(ValueError, match="Unreviewed plan"):
        repair.process(tmp_path, plan, "apply")


def test_review_receipt_hash_cannot_be_bypassed(tmp_path, monkeypatch):
    plan, _ = fixture_repo(tmp_path, monkeypatch)
    monkeypatch.setattr(repair, "REVIEW_SHA", "0" * 64)
    with pytest.raises(ValueError, match="review receipt drift"):
        repair.process(tmp_path, plan, "apply")
