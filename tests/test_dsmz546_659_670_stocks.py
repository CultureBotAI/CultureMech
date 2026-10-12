"""Source/record guards and independent semantic checks for stock corrections."""

import copy
import importlib.util
import json
import subprocess

import pytest
import repair_dsmz546_659_670_stocks as repair

spec = importlib.util.spec_from_file_location("stock_stage_audit", repair.HERE / "audit.py")
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
PLAN = json.loads((repair.HERE / "plan.json").read_text())


@pytest.mark.parametrize("item", PLAN["records"], ids=lambda r: r["key"])
def test_frozen_preview_and_independent_inversion(item):
    before = repair.runner.load_yaml(item["before_text"])
    after, claims = repair.build(before, item["key"], PLAN["sources"], PLAN["created_at"])
    assert repair.runner.render(item["before_text"], after).decode() == item["after_text"]
    assert claims == item["claims"]
    audit.check(before, after, item, PLAN["sources"])


@pytest.mark.parametrize("key", tuple(repair.frozen()[0]))
def test_rejects_changed_baseline(key):
    before = copy.deepcopy(repair.frozen()[0][key]["snapshot"])
    field = "composition" if key.endswith("solution") else "ingredients"
    before[field][0]["concentration"]["value"] = "999"
    with pytest.raises(ValueError, match="baseline"):
        repair.build(before, key, PLAN["sources"], PLAN["created_at"])


def test_rejects_source_drift():
    sources = copy.deepcopy(PLAN["sources"])
    sources["659-medium"]["metadata"]["http_status"] = 404
    with pytest.raises(ValueError, match="source drift"):
        repair.check_sources(sources)


@pytest.mark.parametrize("key", ("659-medium", "659-solution", "659-komodo"))
def test_lactose_is_not_stock_strength(key):
    item = next(r for r in PLAN["records"] if r["key"] == key)
    doc = repair.runner.load_yaml(item["after_text"])
    field = "composition" if key.endswith("solution") else "ingredients"
    assert doc[field][7]["preferred_term"] == "Lactose"
    assert doc[field][7]["concentration"] == {"value": "8", "unit": "G_PER_L"}
    assert len(doc["solutions"]) == 1
    assert doc["solutions"][0]["composition"][0]["preferred_term"] == "CaCl2 x 2 H2O"


@pytest.mark.parametrize("mutation", ("dose", "stock_unit", "carrier", "history", "chemical"))
def test_independent_audit_rejects_unsafe_edits(mutation):
    item = next(r for r in PLAN["records"] if r["key"] == "670-medium")
    before, after = [repair.runner.load_yaml(item[k + "_text"]) for k in ("before", "after")]
    if mutation == "dose":
        after["solutions"][0]["concentration"]["unit"] = "ML_PER_L"
    elif mutation == "stock_unit":
        after["solutions"][0]["composition"][0]["concentration"]["unit"] = "PERCENT_V_V"
    elif mutation == "carrier":
        after["solutions"][0]["composition"][1]["concentration"] = {"value": "0.1", "unit": "MOLAR"}
    elif mutation == "history":
        after["curation_history"][0]["notes"] = "rewritten"
    else:
        after["ingredients"][0]["term"]["id"] = "CHEBI:15377"
    # Also alter the proposal: rejection must come from independent semantics,
    # not merely comparing the edited document against its frozen claim values.
    item = copy.deepcopy(item)
    for c in item["claims"]:
        c["new"] = copy.deepcopy(audit.get(after, c["pointer"]))
    with pytest.raises(AssertionError):
        audit.check(before, after, item, PLAN["sources"])


def fixture_repo(tmp_path):
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    for item in PLAN["records"]:
        path = tmp_path / item["path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(item["before_text"])
    subprocess.run(["git", "-C", str(tmp_path), "add", "data"], check=True)
    # apply/verify uses the frozen plan commit and does not require a fixture commit.
    plan = tmp_path / "plan.json"
    plan.write_text(json.dumps(PLAN))
    return plan


def test_apply_noop_and_readback(tmp_path):
    plan = fixture_repo(tmp_path)
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 9
    assert repair.process(tmp_path, plan, "apply")[1]["changed"] == 0
    assert repair.process(tmp_path, plan, "verify")[1]["already_applied"] == 9


def test_late_conflict_prevents_earlier_writes(tmp_path):
    plan = fixture_repo(tmp_path)
    last = tmp_path / PLAN["records"][-1]["path"]
    last.write_text(last.read_text() + "\n# concurrent change\n")
    with pytest.raises(ValueError, match="Concurrent edit"):
        repair.process(tmp_path, plan, "apply")
    assert (tmp_path / PLAN["records"][0]["path"]).read_text() == PLAN["records"][0]["before_text"]


def test_673_conflicts_are_not_targets():
    targets, _ = repair.frozen()
    assert len(targets) == 9 and all(not k.startswith("673") for k in targets)


def test_symlink_refused_before_writes(tmp_path):
    plan = fixture_repo(tmp_path)
    last = tmp_path / PLAN["records"][-1]["path"]
    original = last.with_suffix(".original")
    last.rename(original)
    last.symlink_to(original)
    with pytest.raises(ValueError, match="Symlink"):
        repair.process(tmp_path, plan, "apply")
    assert (tmp_path / PLAN["records"][0]["path"]).read_text() == PLAN["records"][0]["before_text"]


def test_builder_rejects_modified_source_amount():
    item = PLAN["records"][0]
    sources = copy.deepcopy(PLAN["sources"])
    sources[item["key"]]["raw"] = sources[item["key"]]["raw"].replace('"amount": 5', '"amount": 7')
    with pytest.raises(ValueError, match="source drift"):
        repair.build(
            repair.runner.load_yaml(item["before_text"]), item["key"], sources, PLAN["created_at"]
        )


def test_reports_cover_all_quantity_paths_and_supporting_excerpts(tmp_path, monkeypatch):
    monkeypatch.setattr(repair, "HERE", tmp_path)
    repair.report(PLAN, False)

    def quantities(node, pointer=()):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "concentration":
                    yield repair.runner.field_name([*pointer, key])
                elif key not in {"evidence", "references", "curation_history"}:
                    yield from quantities(value, (*pointer, key))
        elif isinstance(node, list):
            for index, value in enumerate(node):
                yield from quantities(value, (*pointer, index))

    for item in PLAN["records"]:
        text = (tmp_path / (item["key"] + "-followup.md")).read_text()
        assert text.count("- Follow-up target:") == 1 and "- Record:" not in text
        for field in quantities(repair.runner.load_yaml(item["after_text"])):
            assert "| " + field + " |" in text
        for c in item["claims"]:
            for quote in c["extra_excerpts"]:
                assert quote["locator"] in text
