"""Independent source projection and adversarial tests for the medium436 preview."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_ruminococcus_albus_family as repair

spec = importlib.util.spec_from_file_location("ruminococcus_audit", repair.HERE / "audit.py")
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


def test_variant_preserves_base_rows_and_adds_both_explicit_supplements():
    base = {n["preferred_term"]: n.get("concentration") for n in DOCS["K436"][1]["ingredients"]}
    variant = DOCS["K436_18848"][1]
    rows = {n["preferred_term"]: n.get("concentration") for n in variant["ingredients"]}
    assert set(rows) - set(base) == {"maltose", "starch"}
    assert all(rows[k] == v for k, v in base.items())
    assert rows["maltose"] == rows["starch"] == {"value": "1.00", "unit": "G_PER_L"}
    assert base["K2HPO4"] is None and base["Resazurin"]["value"] == "9.99E-4"
    assert "ph_value" not in variant
    assert variant["variant_relationship"] == "STRAIN_SPECIFIC_VARIANT"


def test_original_and_togo_stages_keep_unknown_mass_denominators_and_percent_bases():
    for key in ("D436", "M694", "M2636"):
        after = DOCS[key][1]
        assert [s["concentration"] for s in after["solutions"]] == [
            {"value": "0.04", "unit": "L"},
            {"value": "0.04", "unit": "L"},
            {"value": "0.001", "unit": "L"},
        ]
        for path, node in audit.walk(after):
            if (
                not path
                or path[0] not in {"ingredients", "solutions"}
                or "concentration" not in node
            ):
                continue
            quantity = node["concentration"]
            assert quantity["unit"] == "L" or (
                key == "M2636"
                and node["preferred_term"] in {"Maltose", "Starch"}
                and quantity == {"value": "1", "unit": "G_PER_L"}
            )
        acids = after["solutions"][2]["composition"]
        assert len(acids) == 4
        assert sorted(n["concentration"]["value"] for n in acids) == [
            "0.01",
            "0.01",
            "0.01",
            "0.07",
        ]
    assert "term" not in DOCS["M2636"][1]["solutions"][1]


def test_prior_supported_entries_and_field_paths_are_unchanged():
    before, after = DOCS["S882"]
    old = [(i, n) for i, n in enumerate(before["composition"]) if n.get("evidence")]
    assert len(old) == 7
    assert all(after["composition"][i] == n for i, n in old)
    assert len(after["composition"]) == 11
    assert after["composition"][5]["concentration"] == {"value": "0.92", "unit": "L"}


def test_compared_or_inaccessible_records_are_not_silent_edit_targets():
    context, _ = repair.frozen()
    assert set(ITEMS) == repair.KEYS and not repair.UNCHANGED & ITEMS.keys()
    for record in context["records"]:
        allowed = {record["before_sha256"]}
        if record["key"] in ITEMS:
            allowed.add(ITEMS[record["key"]]["after_sha256"])
        assert repair.runner.sha((repair.ROOT / record["path"]).read_bytes()) in allowed


def test_source_hash_guard_rejects_rewritten_context(monkeypatch):
    old_sha = repair.CONTEXT_SHA
    monkeypatch.setattr(repair, "CONTEXT_SHA", "0" * 64)
    with pytest.raises(ValueError, match="Reviewed context drift"):
        repair.frozen()
    monkeypatch.setattr(repair, "CONTEXT_SHA", old_sha)
    monkeypatch.setattr(repair, "DECISIONS_SHA", "0" * 64)
    with pytest.raises(ValueError, match="Reviewed row decisions drift"):
        repair.frozen()


@pytest.mark.parametrize("key", ITEMS)
def test_rebuild_is_deterministic_without_modifying_baseline(key):
    before, expected = copy.deepcopy(DOCS[key])
    original = copy.deepcopy(before)
    after, claims, lineage = repair.build(before, key, PLAN["created_at"])
    assert before == original and after == expected
    assert claims == ITEMS[key]["claims"] and lineage == ITEMS[key]["lineage"]


@pytest.mark.parametrize("key", [k for k in ITEMS if k not in {"K436", "K436_18848"}])
def test_unrelated_parent_link_cannot_be_inserted(key):
    before, after = copy.deepcopy(DOCS[key])
    after["parent_media"] = {"id": "CultureMech:999999", "relationship": "SOURCE_DUPLICATE"}
    with pytest.raises(AssertionError):
        audit.check(before, after, ITEMS[key])


@pytest.mark.parametrize("key", [k for k in ITEMS if k not in {"K436", "D436"}])
def test_unrelated_child_link_cannot_be_inserted(key):
    before, after = copy.deepcopy(DOCS[key])
    after["variant_children"] = [{"id": "CultureMech:999999", "relationship": "SOURCE_DUPLICATE"}]
    with pytest.raises(AssertionError):
        audit.check(before, after, ITEMS[key])


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
    plan, context = fixture_repo(tmp_path, monkeypatch)
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 10
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 10
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    for item in context["records"]:
        if item["key"] in repair.UNCHANGED:
            assert (tmp_path / item["path"]).read_text() == item["before_text"]


@pytest.mark.parametrize("target", ["M2636", "K3037"])
def test_concurrent_edit_prevents_every_write(tmp_path, monkeypatch, target):
    plan, context = fixture_repo(tmp_path, monkeypatch)
    paths = {r["key"]: tmp_path / r["path"] for r in context["records"]}
    paths[target].write_text(paths[target].read_text() + "# concurrent edit\n")
    before = {k: p.read_bytes() for k, p in paths.items()}
    with pytest.raises(ValueError, match="Concurrent edit|Cohort baseline drift"):
        repair.process(tmp_path, plan, "apply")
    assert before == {k: p.read_bytes() for k, p in paths.items()}


@pytest.mark.parametrize("target", ["K436", "K3037"])
def test_symlink_prevents_every_write(tmp_path, monkeypatch, target):
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
