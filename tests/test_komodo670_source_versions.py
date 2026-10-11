"""Historical/current formulation separation, source guards and successive repair audits."""

import copy
import hashlib
import importlib.util
import json
import subprocess

import pytest
import repair_komodo670_source_versions as repair


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


audit = module("komodo670_version_audit", repair.HERE / "audit.py")
cumulative = module(
    "ingredient_cumulative_audit", repair.BASE / "20261007-dsmz1399-stock-boundary/audit_diff.py"
)
PLAN = json.loads((repair.HERE / "plan.json").read_text())


def item_for(key):
    item = copy.deepcopy(next(r for r in PLAN["records"] if r["key"] == key))
    return (
        item,
        repair.runner.load_yaml(item["before_text"]),
        repair.runner.load_yaml(item["after_text"]),
    )


@pytest.mark.parametrize("item", PLAN["records"], ids=lambda r: r["key"])
def test_frozen_build_and_independent_audit(item):
    before = repair.runner.load_yaml(item["before_text"])
    after, claims = repair.build(before, item["key"], PLAN["sources"], PLAN["created_at"])
    assert claims == item["claims"]
    assert repair.runner.render(item["before_text"], after).decode() == item["after_text"]
    audit.check(before, after, item, PLAN["sources"])


@pytest.mark.parametrize("key", (*repair.STRAINS, "parent"))
def test_baseline_guard(key):
    item, before, _ = item_for(key)
    before["ingredients"][0]["preferred_term"] = "wrong salt"
    with pytest.raises(ValueError, match="baseline"):
        repair.build(before, key, PLAN["sources"], PLAN["created_at"])


@pytest.mark.parametrize("key", ("bacdive4303", "current", "datacite4303", "9466"))
def test_source_guard(key):
    sources = copy.deepcopy(PLAN["sources"])
    sources[key]["unreviewed"] = True
    with pytest.raises(ValueError, match="source drift"):
        repair.check_sources(sources)


@pytest.mark.parametrize(
    "key,pointer,value",
    [
        ("9466", ["ph_value"], 3.0),
        ("9466", ["ingredients", 7, "concentration", "value"], "1"),
        ("9463", ["ingredients", 6, "concentration", "value"], "0.5"),
        ("9463", ["ingredients", 0, "concentration"], {"value": "2", "unit": "G_PER_L"}),
        ("9463", ["ingredients", 4, "concentration", "value"], "0.95"),
        ("9467", ["solutions", 0, "composition", 0, "preferred_term"], "D-glucose"),
        ("9467", ["solutions", 0, "composition", 0, "concentration", "unit"], "PERCENT_V_V"),
        (
            "9467",
            ["solutions", 1, "composition", 0, "concentration"],
            {"value": "1", "unit": "PERCENT_W_V"},
        ),
        ("9467", ["solutions", 0, "concentration"], {"value": "20", "unit": "ML_PER_L"}),
        ("9468", ["solutions", 0, "concentration", "per_volume"], "per liter of final medium"),
        ("9468", ["solutions", 0, "concentration", "unit"], "L"),
        (
            "9468",
            ["solutions", 0, "composition", 1, "concentration"],
            {"value": "0.1", "unit": "MOLAR"},
        ),
        ("9468", ["solutions", 0, "composition", 0, "term", "id"], "CHEBI:15377"),
        ("9466", ["medium_type"], "DEFINED"),
        ("parent", ["variant_children", 2, "relationship"], "PH_VARIANT"),
        ("9463", ["curation_history", 0, "notes"], "rewritten history"),
        ("9463", ["target_organisms"], [{"preferred_term": "invented growth association"}]),
    ],
)
def test_independent_audit_rejects_bad_scientific_proposals(key, pointer, value):
    item, before, after = item_for(key)
    repair.runner.get_node(after, pointer[:-1])[pointer[-1]] = value
    # Corrupt the proposal too so detection is independent of the mutator's frozen diff.
    for c in item["claims"]:
        if c["pointer"]:
            c["new"] = copy.deepcopy(repair.runner.get_node(after, c["pointer"]))
    with pytest.raises(AssertionError):
        audit.check(before, after, item, PLAN["sources"])


def fixture_repo(tmp_path):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    for item in PLAN["records"]:
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    subprocess.run(["git", "-C", str(tmp_path), "add", "data"], check=True)
    plan = tmp_path / "plan.json"
    plan.write_text(json.dumps(PLAN))
    return plan


def test_apply_noop_readback(tmp_path):
    plan = fixture_repo(tmp_path)
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 5
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 5


@pytest.mark.parametrize("kind", ("drift", "symlink", "case"))
def test_late_conflict_has_no_earlier_writes(tmp_path, kind):
    plan = fixture_repo(tmp_path)
    path = tmp_path / PLAN["records"][-1]["path"]
    if kind == "drift":
        path.write_text(path.read_text() + "\n# concurrent edit\n")
    elif kind == "symlink":
        destination = path.with_suffix(".original")
        path.rename(destination)
        path.symlink_to(destination)
    else:
        subprocess.run(
            ["git", "-C", str(tmp_path), "rm", "--cached", "--", PLAN["records"][-1]["path"]],
            check=True,
        )
    with pytest.raises(ValueError):
        repair.process(tmp_path, plan, "apply")
    assert (tmp_path / PLAN["records"][0]["path"]).read_text() == PLAN["records"][0]["before_text"]


def edge(before, after):
    return {
        "id": "CultureMech:000001",
        "before_text": before.decode(),
        "after_text": after.decode(),
        "before_sha256": hashlib.sha256(before).hexdigest(),
        "after_sha256": hashlib.sha256(after).hexdigest(),
    }


def test_chain_inverts_both_applied_successors(monkeypatch):
    a, b, c = (f"id: CultureMech:000001\nvalue: {i}\n".encode() for i in range(3))
    seen = []
    monkeypatch.setattr(
        cumulative,
        "invert_review",
        lambda before, after, item: seen.append((before["value"], after["value"])),
    )
    result = cumulative.invert_chain(c, [edge(a, b), edge(b, c)])
    assert seen == [(1, 2), (0, 1)] and result["value"] == 0


def test_legacy_hash_only_result_is_checked_against_live_bytes(monkeypatch):
    a, b = (f"id: CultureMech:000001\nvalue: {i}\n".encode() for i in range(2))
    item = edge(a, b)
    del item["after_text"]
    monkeypatch.setattr(cumulative, "invert_review", lambda *args: None)
    assert cumulative.invert_chain(b, [item])["value"] == 0
    with pytest.raises(AssertionError, match="Unapplied"):
        cumulative.invert_chain(b + b"# unreviewed\n", [item])


@pytest.mark.parametrize(
    "kind", ("unapplied", "duplicate", "disconnected", "identity", "hash", "cycle")
)
def test_chain_rejects_invalid_history(monkeypatch, kind):
    a, b, c, d = (f"id: CultureMech:000001\nvalue: {i}\n".encode() for i in range(4))
    monkeypatch.setattr(cumulative, "invert_review", lambda *args: None)
    items = [edge(a, b), edge(b, c)]
    raw = c
    if kind == "unapplied":
        raw = b
    elif kind == "duplicate":
        items.append(edge(a, c))
    elif kind == "disconnected":
        items.append(edge(a, d))
    elif kind == "identity":
        items[-1]["id"] = "CultureMech:999999"
    elif kind == "hash":
        items[-1]["before_text"] += "# drift"
    else:
        items = [edge(a, b), edge(b, a)]
        raw = a
    with pytest.raises(AssertionError):
        cumulative.invert_chain(raw, items)


def test_existing_parent_repair_also_inverts():
    item, _, _ = item_for("parent")
    prior = json.loads((repair.PREVIOUS / "plan.json").read_text())
    previous = next(r for r in prior["records"] if r["key"] == "670-komodo")
    cumulative.counts.clear()
    restored = cumulative.invert_chain(item["after_text"].encode(), [previous, item])
    assert restored == repair.runner.load_yaml(previous["before_text"])
    assert cumulative.counts["new_curation_history"] == 2


def test_report_quantity_coverage(tmp_path, monkeypatch):
    monkeypatch.setattr(repair, "HERE", tmp_path)
    repair.report(PLAN, False)
    for item in PLAN["records"]:
        text = (tmp_path / (item["key"] + "-followup.md")).read_text()
        assert text.count("- Follow-up target:") == 1 and "- Record:" not in text
        assert item["after_sha256"] in text
        for claim in item["claims"]:
            assert "| " + claim["field"] + " |" in text
        if item["key"] in {"9463", "9466"}:
            assert "| ingredients[6].concentration | Powdered sulfur |" in text
        if item["key"] == "9467":
            assert "| solutions[0].composition[0].concentration | Glucose |" in text
            assert "| solutions[1].composition[0].concentration | Yeast extract |" in text
            assert "| solutions[0].concentration | Archived glucose stock |" in text
        if item["key"] == "9468":
            assert "| solutions[0].concentration | Archived FeSO4 x 7 H2O stock |" in text
