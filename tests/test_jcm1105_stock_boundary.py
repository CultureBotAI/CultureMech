"""Original-source stage boundaries, exact quantities and guarded JCM 1105 repair."""

import copy
import html
import importlib.util
import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_jcm1105_stock_boundary as repair  # noqa: E402
from review_solution_concentration_evidence import get_node  # noqa: E402

HERE = ROOT / "reports/ingredient_concentration_curation/20261007-jcm1105-stock-boundary"


@pytest.fixture
def example(monkeypatch):
    plan = json.loads((HERE / "plan.json").read_text())

    def table(rows):
        return (
            "<table>"
            + "".join(
                "<tr>" + "".join("<td>" + html.escape(c) + "</td>" for c in row) + "</tr>"
                for row in rows
            )
            + "</table>"
        )

    # Synthetic HTML is only a parser fixture; actual source readback is separate.
    raw = (
        (
            "<html><head><title>Hidden</title></head><body><script>Hidden</script><p>"
            + html.escape(repair.HEADER)
            + "</p>"
            + table(repair.BASE_ROWS)
            + html.escape(repair.BRIDGE)
            + "<br>"
            + table([repair.STOCK_ROW])
            + html.escape(repair.PH)
            + "<br>"
            + html.escape(repair.FOOTER)
            + "</body></html>"
        )
        .replace("H2O", "H<sub>2</sub>O")
        .replace("Na2CO3", "Na<sub>2</sub>CO<sub>3</sub>")
    )
    monkeypatch.setattr(repair, "SOURCE_SHA", repair.sha(raw.encode()))
    return plan["records"][0]["before_text"], raw, plan["created_at"]


def test_complete_repair_and_evidence_scope(example):
    text, raw, timestamp = example
    before = repair.load_yaml(text)
    original = copy.deepcopy(before)
    after, claims = repair.build(before, raw, timestamp)
    assert before == original and len(claims) == 11
    assert after["ingredients"] == [] and len(after["solutions"]) == 2
    base, stock = after["solutions"]
    assert base["concentration"] == {"value": "1", "unit": "L"}
    assert stock["concentration"] == {"value": "0.010", "unit": "L"}
    assert [n["concentration"] for n in base["composition"]] == [
        {"value": v, "unit": "G_PER_L"} for v in ["10", "3", "1", "3", "100"]
    ]
    for index, node in enumerate(base["composition"]):
        old = before["ingredients"][index]
        assert {k: v for k, v in node.items() if k not in ("concentration", "evidence")} == {
            k: v for k, v in old.items() if k != "concentration"
        }
    carbonate = stock["composition"][0]
    assert "concentration" not in carbonate and "percentage basis" in carbonate["notes"]
    assert carbonate["preferred_term"] == "Na2CO3"
    assert after["physical_state"] == "LIQUID"
    assert not any(n["preferred_term"] == "Agar" for n in base["composition"])
    assert after["preparation_steps"][1:] == before["preparation_steps"][1:]
    assert after["preparation_steps"][0]["action"] == "AUTOCLAVE"
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["curation_history"][-1]["curator"] == "codex"
    for key in before.keys() - {"ingredients", "preparation_steps", "curation_history"}:
        assert after[key] == before[key]
    _, visible = repair.inspect_source(raw)
    assert "Hidden" not in visible
    for c in claims:
        if c["old_pointer"]:
            assert get_node(before, c["old_pointer"]) == c["old"]
        if c["status"] == "remove_unsupported":
            assert "concentration" not in get_node(after, c["pointer"][:-1])
        else:
            assert get_node(after, c["pointer"]) == c["new"]
        (evidence,) = get_node(after, c["evidence_pointer"])["evidence"]
        assert evidence["reference"] == c["reference"] == repair.URL
        assert evidence["supports"] == "SUPPORT" and c["snippet"] in visible
        assert c["snippet"] in evidence["snippet"] or c["snippet"] in evidence["explanation"]
        assert c["field"] in evidence["explanation"]
        assert repair.SOURCE_SHA in evidence["explanation"]
    assert len(after["references"]) == len(after["evidence"]) == 1


@pytest.mark.parametrize(
    "field",
    [
        "id",
        "ingredients",
        "preparation_steps",
        "physical_state",
        "ph_value",
        "media_term",
        "curation_history",
        "high_metal",
    ],
)
def test_local_context_drift_rejected(example, field):
    text, raw, timestamp = example
    doc = repair.load_yaml(text)
    doc.pop(field)
    with pytest.raises(ValueError, match="formulation drift"):
        repair.build(doc, raw, timestamp)


@pytest.mark.parametrize(
    "old,new",
    [
        ("<td>100.0</td>", "<td>101.0</td>"),
        ("<td>g</td>", "<td>ml</td>"),
        ("1.0 L", "0.1 L"),
        ("10% Na", "20% Na"),
        ("<td>10.0</td><td>ml</td>", "<td>1.0</td><td>ml</td>"),
        ("[1105]", "[1106]"),
        ("VIRGIBACILLUS MERV MEDIUM", "VIRGIBACILLUS MERV MEDIUM VARIANT"),
        ("3H<sub>2</sub>O", "2H<sub>2</sub>O"),
        ("After autoclaving", "Before autoclaving"),
        ("20.0 g/L agar", "2.0 g/L agar"),
        ("pH to 8.0", "pH to 9.0"),
        ("121\u00b0C", "100\u00b0C"),
        ("</table>", "</table><p>Omit the carbonate stock.</p>"),
        ("<table>", "<table><table>"),
    ],
)
def test_source_drift_rejected_even_with_recomputed_hash(example, monkeypatch, old, new):
    text, raw, timestamp = example
    assert old in raw
    raw = raw.replace(old, new)
    monkeypatch.setattr(repair, "SOURCE_SHA", repair.sha(raw.encode()))
    with pytest.raises(ValueError):
        repair.build(repair.load_yaml(text), raw, timestamp)


def test_missing_table_boundary_rejected(example, monkeypatch):
    text, raw, timestamp = example
    raw = raw.replace(
        "</table>" + html.escape(repair.BRIDGE) + "<br><table>", html.escape(repair.BRIDGE)
    )
    monkeypatch.setattr(repair, "SOURCE_SHA", repair.sha(raw.encode()))
    with pytest.raises(ValueError):
        repair.build(repair.load_yaml(text), raw, timestamp)


def test_wrong_capture_hash_rejected(example):
    text, raw, timestamp = example
    with pytest.raises(ValueError, match="source hash drift"):
        repair.build(repair.load_yaml(text), raw + " ", timestamp)


@pytest.fixture
def sandbox(example, tmp_path, monkeypatch):
    before, raw, _ = example
    target = tmp_path / repair.TARGET
    target.parent.mkdir(parents=True)
    target.write_text(before)
    (tmp_path / repair.SOURCE_FILE).write_text(raw)
    state = {"commit": "1" * 40, "tracked": repair.TARGET}

    def git(command, **kwargs):
        if command[1] == "ls-files":
            return (state["tracked"] + "\0").encode()
        assert command[1:3] == ["rev-parse", "HEAD"]
        return (state["commit"] + "\n").encode()

    monkeypatch.setattr(repair.subprocess, "check_output", git)
    return tmp_path, target, tmp_path / "plan.json", state


def test_preview_apply_verify_noop_and_unrelated_commit(sandbox):
    root, target, plan_path, state = sandbox
    original = target.read_bytes()
    plan, result = repair.process(root, root, plan_path, "preview")
    assert target.read_bytes() == original and result["changed"] == 0
    with pytest.raises(ValueError, match="Refuse to overwrite"):
        repair.process(root, root, plan_path, "preview")
    with pytest.raises(ValueError, match="not applied"):
        repair.process(root, root, plan_path, "verify")
    _, result = repair.process(root, root, plan_path, "apply")
    assert result["changed"] == 1 and target.read_text() == plan["records"][0]["after_text"]
    _, result = repair.process(root, root, plan_path, "apply")
    assert result["changed"] == 0 and result["already_applied"] == 1
    state["commit"] = "2" * 40
    _, result = repair.process(root, root, plan_path, "verify")
    assert result["already_applied"] == 1


@pytest.mark.parametrize("damage", ["target", "plan", "source", "case", "symlink"])
def test_apply_rejects_drift_without_writing(sandbox, damage):
    root, target, plan_path, state = sandbox
    repair.process(root, root, plan_path, "preview")
    if damage == "target":
        target.write_text(target.read_text() + "\n# Concurrent edit\n")
    elif damage == "plan":
        plan = json.loads(plan_path.read_text())
        plan["records"][0]["claims"][0]["new"]["value"] = "999"
        plan_path.write_text(json.dumps(plan))
    elif damage == "source":
        source = root / repair.SOURCE_FILE
        source.write_text(source.read_text().replace("1.0 L", "0.1 L"))
    elif damage == "case":
        state["tracked"] = repair.TARGET.upper()
    else:
        saved = root / "saved.yaml"
        target.rename(saved)
        target.symlink_to(saved)
    original = target.read_bytes()
    with pytest.raises(ValueError):
        repair.process(root, root, plan_path, "apply")
    assert target.read_bytes() == original


def test_applied_successor_preserves_historical_report():
    plan = json.loads((HERE / "plan.json").read_text())
    item = plan["records"][0]
    assert repair.sha((ROOT / repair.TARGET).read_bytes()) == item["after_sha256"]
    assert repair.sha(item["before_text"].encode()) == repair.BASELINE
    rows = (HERE / "J1105.md").read_text().splitlines()
    assert "- State: applied locally" in rows
    assert not any(r.startswith("- Record:") for r in rows)
    prior_plan = HERE.parent / "20261007-mediadive-media-3000-3319/plan.json"
    prior = next(
        r for r in json.loads(prior_plan.read_text())["records"] if r["path"] == repair.TARGET
    )
    assert prior["after_sha256"] == item["before_sha256"]
    assert not any(c["status"] in {"add", "correct", "evidence_only"} for c in prior["claims"])


@pytest.mark.parametrize(
    "damage",
    [
        None,
        "quantity",
        "unit",
        "stock_dose",
        "carbonate_quantity",
        "carbonate_notes",
        "label",
        "preparation",
        "quote",
        "scope",
        "reference",
        "ontology",
        "history",
        "root_ingredient",
        "ph",
    ],
)
def test_independent_inversion_rejects_unreviewed_changes(damage):
    spec = importlib.util.spec_from_file_location(
        "jcm1105_independent_diff", HERE.parent / "20261007-dsmz1399-stock-boundary/audit_diff.py"
    )
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    item = json.loads((HERE / "plan.json").read_text())["records"][0]
    before, after = map(repair.load_yaml, (item["before_text"], item["after_text"]))
    node = after["solutions"][0]["composition"][0]
    carbonate = after["solutions"][1]["composition"][0]
    if damage == "quantity":
        node["concentration"]["value"] = "1000"
    elif damage == "unit":
        node["concentration"]["unit"] = "ML_PER_L"
    elif damage == "stock_dose":
        after["solutions"][1]["concentration"]["unit"] = "ML_PER_L"
    elif damage == "carbonate_quantity":
        carbonate["concentration"] = {"value": "10", "unit": "PERCENT_W_V"}
    elif damage == "carbonate_notes":
        carbonate["notes"] = "Assume weight per volume."
    elif damage == "label":
        node["preferred_term"] = "Tryptone"
    elif damage == "preparation":
        after["solutions"][0]["preparation_notes"] = "Changed"
    elif damage == "quote":
        node["evidence"][0]["snippet"] = "Changed"
    elif damage == "scope":
        after["evidence"][0]["explanation"] = "Changed"
    elif damage == "reference":
        after["references"][0]["reference"] = "https://example.invalid/"
    elif damage == "ontology":
        node["term"] = {"id": "CHEBI:15377", "label": "water"}
    elif damage == "history":
        after["curation_history"][0]["curator"] = "Changed"
    elif damage == "root_ingredient":
        after["ingredients"].append(copy.deepcopy(before["ingredients"][0]))
    elif damage == "ph":
        after["ph_value"] = 7.0
    if damage:
        with pytest.raises(AssertionError):
            audit.invert_review(before, after, item)
    else:
        audit.invert_review(before, after, item)
        assert audit.counts["quantity_corrections"] == 5
        assert audit.counts["new_evidence"] == 7
        assert audit.counts["stock_nodes_relocated"] == 6
        assert audit.counts["unsupported_quantity_slots_removed"] == 1
        assert audit.counts["new_quantity_slots"] == 2
