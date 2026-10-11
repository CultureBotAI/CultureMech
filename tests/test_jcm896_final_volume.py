"""Offline recipe parsing, exact arithmetic, mutation guards, and successor checks."""

import html
import importlib.util
import json
import sys
from decimal import Decimal
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import repair_jcm896_final_volume as repair  # noqa: E402

HERE = ROOT / "reports/ingredient_concentration_curation/20261007-jcm896-final-volume"


@pytest.fixture
def example(monkeypatch):
    plan = json.loads((HERE / "plan.json").read_text())
    before = plan["records"][0]["before_text"]
    # Synthetic rendering fixture; live-source hash/readback is a separate CLI gate.
    rows = "".join(
        "<tr>" + "".join("<td>" + html.escape(c) + "</td>" for c in row) + "</tr>"
        for row in repair.ROWS
    )
    raw = (
        (
            "<html><head><title>Hidden title</title></head><body>"
            "<script>not visible</script><p>Search for medium no. = [896].</p>"
            "<p>896&nbsp; MODIFIED BSK MEDIUM</p><table>"
            + rows
            + "</table>"
            + repair.PREPARATION
            + "</body></html>"
        )
        .replace("NaHCO3", "NaHCO<sub>3</sub>")
        .replace("N-Acetyl-D-glucosamine", "<i>N</i>-Acetyl-D-glucosamine")
    )
    monkeypatch.setattr(repair, "SOURCE_SHA", repair.sha(raw.encode()))
    return before, raw, plan["created_at"]


def test_complete_repair_preserves_unrelated_fields_and_scopes_every_edit(example):
    text, raw, timestamp = example
    before = repair.load_yaml(text)
    after, claims = repair.build(before, raw, timestamp)
    assert len(claims) == 13 and len(after["ingredients"]) == 11
    expected = [
        "5.13699",
        "0.599315",
        "4.28082",
        "0.684932",
        "0.342466",
        "1.88356",
        "8.90411",
        "1.71233",
        "42.8082",
        "4.28082",
        "68.4932",
    ]
    for i, node in enumerate(after["ingredients"]):
        assert node["concentration"] == {
            "value": expected[i],
            "unit": "ML_PER_L" if i == 10 else "G_PER_L",
        }
        amount = Decimal(repair.ROWS[i][1])
        assert abs(Decimal(expected[i]) * Decimal("0.584") - amount) <= amount * Decimal("0.000005")
        assert len(node["evidence"]) == 1
        old = before["ingredients"][i]
        for key in old.keys() - {"concentration", "preferred_term"}:
            assert node[key] == old[key]
        assert node["preferred_term"] == (
            "TC Yeastolate (BD-Difco)" if i == 7 else old["preferred_term"]
        )
    assert after["preparation_steps"][0]["description"] == repair.PREPARATION
    assert len(after["evidence"]) == len(after["references"]) == 1
    assert after["curation_history"][:-1] == before["curation_history"]
    assert after["curation_history"][-1]["curator"] == "codex"
    for key in before.keys() - {"ingredients", "preparation_steps", "curation_history"}:
        assert after[key] == before[key]
    _, visible = repair.inspect_source(raw)
    assert "not visible" not in visible and "Hidden title" not in visible
    for c in claims:
        assert repair.get_node(before, c["pointer"]) == c["old"]
        assert repair.get_node(after, c["pointer"]) == c["new"]
        evidence = repair.get_node(after, c["evidence_pointer"])["evidence"]
        assert len(evidence) == 1 and evidence[0]["reference"] == repair.URL
        assert evidence[0]["snippet"] == c["snippet"] and c["snippet"] in visible
        assert c["field"] in evidence[0]["explanation"]
        assert repair.VOLUME_QUOTE in evidence[0]["explanation"]
        assert repair.SOURCE_SHA in evidence[0]["explanation"]
    assert before == repair.load_yaml(text)


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
        "notes",
    ],
)
def test_local_context_drift_is_rejected(example, field):
    text, raw, timestamp = example
    doc = repair.load_yaml(text)
    doc.pop(field)
    with pytest.raises(ValueError, match="formulation drift"):
        repair.build(doc, raw, timestamp)


@pytest.mark.parametrize(
    "old,new",
    [
        ("3.0", "3.1"),
        ("<td>g</td>", "<td>ml</td>"),
        ("584 ml", "5840 ml"),
        ("[896]", "[897]"),
        ("TC Yeastolate", "Yeast extract"),
        ("2H2O", "3H2O"),
        ("MODIFIED BSK MEDIUM", "MODIFIED BSK MEDIUM VARIANT"),
        ("0.22", "0.45"),
    ],
)
def test_changed_source_is_rejected_even_with_recomputed_hash(example, monkeypatch, old, new):
    text, raw, timestamp = example
    raw = raw.replace(old, new)
    monkeypatch.setattr(repair, "SOURCE_SHA", repair.sha(raw.encode()))
    with pytest.raises(ValueError):
        repair.build(repair.load_yaml(text), raw, timestamp)


def test_wrong_capture_hash_is_rejected(example):
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


def test_guarded_preview_apply_verify_noop_and_new_commit(sandbox):
    root, target, plan_path, state = sandbox
    original = target.read_bytes()
    plan, result = repair.process(root, root, plan_path, "preview")
    assert target.read_bytes() == original and result["changed"] == 0
    with pytest.raises(ValueError, match="Refuse to overwrite"):
        repair.process(root, root, plan_path, "preview")
    with pytest.raises(ValueError, match="not applied"):
        repair.process(root, root, plan_path, "verify")
    _, result = repair.process(root, root, plan_path, "apply")
    assert result["changed"] == 1
    assert target.read_text() == plan["records"][0]["after_text"]
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
        source.write_text(source.read_text().replace("584 ml", "40 ml"))
    elif damage == "case":
        state["tracked"] = repair.TARGET.upper()
    else:
        saved = root / "saved.yaml"
        target.rename(saved)
        target.symlink_to(saved)
    before = target.read_bytes()
    with pytest.raises(ValueError):
        repair.process(root, root, plan_path, "apply")
    assert target.read_bytes() == before


def test_applied_plan_is_a_complete_successor_not_a_second_record_report():
    plan = json.loads((HERE / "plan.json").read_text())
    item = plan["records"][0]
    assert repair.sha((ROOT / repair.TARGET).read_bytes()) == item["after_sha256"]
    assert repair.sha(item["before_text"].encode()) == repair.BASELINE
    assert repair.sha(item["after_text"].encode()) == item["after_sha256"]
    assert item["source_sha256"] == repair.SOURCE_SHA
    rows = (HERE / "J896.md").read_text().splitlines()
    assert "- State: applied locally" in rows
    assert not any(r.startswith("- Record:") for r in rows)
    original = ROOT / "reports/ingredient_concentration_curation/20261007-mediadive-media-2500-3000"
    cohort = json.loads((original / "plan.json").read_text())
    prior = next(r for r in cohort["records"] if r["path"] == repair.TARGET)
    assert prior["after_sha256"] == item["before_sha256"]
    assert all(c["status"] not in {"add", "correct", "evidence_only"} for c in prior["claims"])


@pytest.mark.parametrize(
    "damage",
    [
        None,
        "quantity",
        "unit",
        "label",
        "preparation",
        "quote",
        "scope",
        "reference",
        "ontology",
        "history",
    ],
)
def test_independent_diff_inversion_rejects_unreviewed_changes(damage):
    spec = importlib.util.spec_from_file_location(
        "jcm896_independent_diff",
        HERE.parent / "20261007-dsmz1399-stock-boundary/audit_diff.py",
    )
    audit = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(audit)
    item = json.loads((HERE / "plan.json").read_text())["records"][0]
    before, after = map(repair.load_yaml, (item["before_text"], item["after_text"]))
    node = after["ingredients"][0]
    if damage == "quantity":
        node["concentration"]["value"] = "75"
    elif damage == "unit":
        after["ingredients"][10]["concentration"]["unit"] = "G_PER_L"
    elif damage == "label":
        after["ingredients"][7]["preferred_term"] = "Yeast extract"
    elif damage == "preparation":
        after["preparation_steps"][0]["description"] = "Changed"
    elif damage == "quote":
        node["evidence"][0]["snippet"] = "Changed"
    elif damage == "scope":
        node["evidence"][0]["explanation"] = "Changed"
    elif damage == "reference":
        after["references"][0]["reference"] = "https://example.invalid/"
    elif damage == "ontology":
        node["term"]["id"] = "CHEBI:15377"
    elif damage == "history":
        after["curation_history"][0]["curator"] = "Changed"
    if damage:
        with pytest.raises(AssertionError):
            audit.invert_review(before, after, item)
    else:
        audit.invert_review(before, after, item)
        assert audit.counts["quantity_corrections"] == 11
        assert audit.counts["new_evidence"] == 12
        assert audit.counts["ingredient_labels_corrected"] == 1
        assert audit.counts["preparation_text_encodings_corrected"] == 1
