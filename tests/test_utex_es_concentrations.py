"""Guard source-specific ES amounts, nested stocks, chemical forms and provenance."""

import collections
import copy
import json
import subprocess

import pytest
import review_utex_es_concentrations as repair


@pytest.fixture(scope="module")
def frozen_plan():
    return json.loads(repair.PLAN.read_text())


@pytest.fixture
def plan(frozen_plan):
    return copy.deepcopy(frozen_plan)


@pytest.fixture(params=sorted(repair.KEYS))
def reviewed(frozen_plan, request):
    item = copy.deepcopy(next(r for r in frozen_plan["records"] if r["key"] == request.param))
    return tuple(repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text")) + (item,)


def rehash(item, after):
    item["after_text"] = json.dumps(after, ensure_ascii=False)
    item["after_sha256"] = repair.runner.sha(item["after_text"].encode())


def test_inventory_and_counts(frozen_plan):
    counts = collections.Counter()
    for item in frozen_plan["records"]:
        counts.update(item["counts"])
    assert sum(len(r["claims"]) for r in frozen_plan["records"]) == 124
    assert counts == {
        "new_evidence": 134,
        "new_curation_history": 6,
        "stock_nodes_relocated": 20,
        "stock_dose_basis_corrections": 20,
        "new_references": 26,
        "bibliographic_entries_enriched": 30,
        "quantity_corrections": 8,
        "unsupported_quantity_slots_removed": 24,
        "ingredient_context_notes_corrected": 48,
        "unsupported_primary_identities_removed": 4,
        "unsupported_secondary_identities_removed": 4,
        "ingredient_labels_corrected": 12,
        "ingredient_identities_corrected": 8,
        "relationship_dose_descriptions_corrected": 9,
    }


def test_every_claim_and_identity_is_scoped(reviewed):
    before, after, item = reviewed
    source, records = repair.sources()
    record = records[item["key"]]
    assert dict(repair.check(before, after, item)) == item["counts"]
    assert [c["pointer"] for c in item["claims"]] == [
        c["pointer"] for c in repair.runner.all_claims(before)
    ]
    assert {tuple(c["proposed_pointer"]) for c in item["claims"]} == {
        tuple(c["pointer"]) for c in repair.runner.all_claims(after)
    }
    for claim in item["claims"]:
        node = repair.runner.get_node(after, claim["proposed_pointer"])
        assert node.get("concentration") == claim["new"]
        assert claim["snippet"] in source["sources"][claim["reference"]]["text"]
        if claim["new"] is None:
            assert "concentration" not in node and node["notes"]
        if claim.get("identity_corrected") == "unsupported-identifiers-removed":
            assert "term" not in node and "mediaingredientmech_chebi_term" not in node
            assert "pentahydrate" in node["preferred_term"]
            assert "13408-09-8" in node["notes"]
    for addition in record["evidence_additions"]:
        node = repair.runner.get_node(after, addition["pointer"])
        assert addition["evidence"] in node["evidence"]
        assert len({e["reference"] for e in node["evidence"]}) == len(node["evidence"])
    for field in (
        "id",
        "name",
        "target_organisms",
        "variants",
        "physical_state",
        "preparation_steps",
    ):
        assert before.get(field) == after.get(field)
    assert before["curation_history"] == after["curation_history"][:-1]


def test_receiving_stages_are_not_flattened(reviewed):
    before, after, item = reviewed
    assert len(after["solutions"]) == 1
    enrichment = after["solutions"][0]
    if len(before["solutions"]) == 6:
        assert after["ingredients"][0]["concentration"] == {"value": "1", "unit": "L"}
        assert enrichment["concentration"]["unit"] == "L"
        assert [s["concentration"] for s in enrichment["solutions"]] == [
            {"value": "162.5", "unit": "ML_PER_L"},
            {"value": "162.5", "unit": "ML_PER_L"},
            {"value": "1.5", "unit": "ML_PER_L"},
            {"value": "1.5", "unit": "ML_PER_L"},
            {"value": "1.5", "unit": "ML_PER_L"},
        ]
        assert all(
            "concentration" not in stock["composition"][0]
            for stock in [enrichment] + enrichment["solutions"]
        )
        assert all("evidence" not in stock for stock in [enrichment] + enrichment["solutions"])
    else:
        assert "solutions" not in enrichment
        assert enrichment["concentration"] == before["solutions"][0]["concentration"]
        assert after["ingredients"][0]["concentration"] == before["ingredients"][0]["concentration"]
        if item["key"] == "two-thirds-enriched-seawater-medium":
            assert enrichment["concentration"]["value"] == "665"


def test_json_equivalence(reviewed):
    before, after, item = reviewed
    rehash(item, after)
    assert dict(repair.check(before, after, item)) == item["counts"]


def test_dilution_explanations_do_not_cross_formulations(frozen_plan):
    for key, expected, excluded in (
        ("one-half-enriched-seawater-medium", "500/500", "665/335"),
        ("two-thirds-enriched-seawater-medium", "665/335", "500/500"),
    ):
        item = next(r for r in frozen_plan["records"] if r["key"] == key)
        record = repair.sources()[1][key]
        texts = [c["explanation"] for c in item["claims"]]
        texts += [e["evidence"]["explanation"] for e in record["evidence_additions"]]
        assert all(expected in text and excluded not in text for text in texts)


@pytest.mark.parametrize(
    "field,value", [("value", "999"), ("unit", "MOLAR"), ("per_volume", "per 1 L final")]
)
def test_all_quantity_claims_reject_forgery(reviewed, field, value):
    before, after, item = reviewed
    for claim in item["claims"]:
        changed, forged = copy.deepcopy(after), copy.deepcopy(item)
        node = repair.runner.get_node(changed, claim["proposed_pointer"])
        node.setdefault("concentration", {"value": "1000", "unit": "ML_PER_L"})[field] = value
        rehash(forged, changed)
        with pytest.raises(AssertionError):
            repair.check(before, changed, forged)


@pytest.mark.parametrize("field", ["snippet", "reference", "supports", "explanation"])
def test_every_new_evidence_rejects_forgery(reviewed, field):
    before, after, item = reviewed
    record = repair.sources()[1][item["key"]]
    for addition in record["evidence_additions"]:
        changed, forged = copy.deepcopy(after), copy.deepcopy(item)
        evidence = repair.runner.get_node(changed, addition["pointer"])["evidence"]
        index = evidence.index(addition["evidence"])
        evidence[index][field] = "forged"
        rehash(forged, changed)
        with pytest.raises(AssertionError):
            repair.check(before, changed, forged)


@pytest.mark.parametrize(
    "kind",
    [
        "identity",
        "notes",
        "history",
        "event",
        "bibliography",
        "relationship",
        "order",
        "claim",
        "unresolved",
        "new_taxon",
        "root",
    ],
)
def test_other_changes_reject_forgery(reviewed, kind):
    before, after, item = reviewed
    if kind == "identity":
        after["ingredients"][0]["term"] = {"id": "CHEBI:999999", "label": "forged"}
    elif kind == "notes":
        after["ingredients"][0]["notes"] = "forged"
    elif kind == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    elif kind == "event":
        after["curation_history"][-1]["curator"] = "someone else"
    elif kind == "bibliography":
        after["references"][1]["year"] = 2026
    elif kind == "relationship":
        after["parent_media"] = {"id": "CultureMech:999999"}
    elif kind == "order":
        after["ingredients"].append(copy.deepcopy(after["ingredients"][0]))
    elif kind == "claim":
        item["claims"][0]["status"] = "verified"
    elif kind == "unresolved":
        item["unresolved"] = []
    elif kind == "new_taxon":
        after.setdefault("target_organisms", []).append({"preferred_term": "invented"})
    else:
        after["invented"] = True
    rehash(item, after)
    with pytest.raises(AssertionError):
        repair.check(before, after, item)


@pytest.mark.parametrize("kind", ["flatten", "duplicate", "reorder", "restore_identity"])
def test_stock_and_glycerophosphate_regressions(plan, kind):
    item = next(r for r in plan["records"] if r["key"] == "enriched-seawater-medium")
    before, after = (repair.runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
    stock = after["solutions"][0]
    if kind == "flatten":
        after["solutions"].extend(stock.pop("solutions"))
    elif kind == "duplicate":
        after["solutions"].append(copy.deepcopy(stock["solutions"][0]))
    elif kind == "reorder":
        stock["solutions"].reverse()
    else:
        stock["composition"][2]["term"] = {"id": "CHEBI:15978", "label": "sn-glycerol 3-phosphate"}
    rehash(item, after)
    with pytest.raises((AssertionError, KeyError, IndexError)):
        repair.check(before, after, item)


def make_repo(tmp_path, plan, monkeypatch):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    for item in plan["records"]:
        target = tmp_path / item["path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(item["before_text"])
    subprocess.run(["git", "add", "data"], cwd=tmp_path, check=True)
    monkeypatch.setattr(repair, "validate_recipe", lambda *a, **k: [])
    return tmp_path


def test_apply_readback_noop(plan, tmp_path, monkeypatch):
    root = make_repo(tmp_path, plan, monkeypatch)
    assert repair.apply(plan, root) == {"changed": 6, "already_applied": 0}
    assert repair.apply(plan, root) == {"changed": 0, "already_applied": 6}
    assert repair.apply(plan, root, verify=True) == {"changed": 0, "already_applied": 6}


@pytest.mark.parametrize(
    "kind",
    [
        "late_drift",
        "duplicate",
        "outside",
        "symlink",
        "source",
        "version",
        "case",
        "counts",
        "verify_before_apply",
    ],
)
def test_failed_preflight_writes_nothing(plan, tmp_path, monkeypatch, kind):
    root = make_repo(tmp_path, plan, monkeypatch)
    original = {r["path"]: (root / r["path"]).read_bytes() for r in plan["records"]}
    last = plan["records"][-1]
    if kind == "late_drift":
        target = root / last["path"]
        target.write_bytes(target.read_bytes() + b"\n# concurrent edit\n")
        original[last["path"]] = target.read_bytes()
    elif kind == "duplicate":
        plan["records"][-1] = copy.deepcopy(plan["records"][0])
    elif kind == "outside":
        last["path"] = "../../outside.yaml"
    elif kind == "symlink":
        target = root / last["path"]
        saved = root / "elsewhere.yaml"
        target.rename(saved)
        target.symlink_to(saved)
    elif kind == "source":
        plan["source_sha256"] = "0" * 64
    elif kind == "version":
        plan["version"] = 999
    elif kind == "case":
        last["path"] = last["path"].replace("algae", "ALGAE")
    elif kind == "counts":
        last["counts"]["new_evidence"] = 999
    with pytest.raises((AssertionError, ValueError)):
        repair.apply(plan, root, verify=kind == "verify_before_apply")
    assert all((root / path).read_bytes() == raw for path, raw in original.items())
