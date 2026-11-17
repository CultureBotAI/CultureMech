"""Guard reviewed completeness mutations and receipt replay (#683, #781–783).

2026-11-16. Synthetic recipes only; native validation and writer paths remain
enabled. Tests exercise actual persisted bytes rather than reported success.
"""

from __future__ import annotations

import copy
import json
import sys

import curate_variant_completeness as complete
import curate_variant_ingredients as writer
import pytest
import yaml

from culturemech.validation.write_validated import validate_recipe


@pytest.fixture
def sample(tmp_path):
    relative = "data/normalized_yaml/algae/completeness.yaml"
    path = tmp_path / relative
    path.parent.mkdir(parents=True)
    path.write_text(
        "# retained source comment\n"
        "id: CultureMech:000001\n"
        "name: 'Synthetic completeness fixture'\n"
        "physical_state: LIQUID\n"
        "description: |\n  Preserve this original line.\n  And this second line.\n"
        "ingredients:\n- preferred_term: water\n"
        "variants:\n- name: assay\n"
        "  description: Earlier assay description.\n"
        "  modifications:\n"
        "  - Set water input to 950 mL per batch.\n"
        "  - A salt hydrate is reported without a verified form.\n"
        "- name: untouched\n  modifications:\n  - Retain this unrelated variant.\n"
        "target_organisms:\n- preferred_term: Synthetic organism\n"
        "curation_history:\n- timestamp: '2026-11-16T00:00:00Z'\n"
        "  curator: fixture\n  action: created\n  notes: Preserve earlier evidence.\n"
    )
    record = yaml.safe_load(path.read_bytes())
    source, uncertain = record["variants"][0]["modifications"]
    change = {
        "action": "SET_AMOUNT",
        "ingredient": {"preferred_term": "water"},
        "amount": {
            "value": "950",
            "unit": "ML",
            "basis": "PER_BATCH",
            "basis_statement": "Literal batch input; final volume unspecified.",
        },
        "stage": "synthetic batch preparation",
        "source_modification_index": 0,
        "source_text": source,
        "evidence": [
            {
                "reference": "https://example.org/synthetic-completeness",
                "supports": "SUPPORT",
                "snippet": source,
                "explanation": "Synthetic exact batch statement, without volume conversion.",
            }
        ],
    }
    mention = {
        "source_label": "salt hydrate",
        "reported_action": "UNSPECIFIED",
        "stage": "unspecified in source",
        "source_modification_index": 1,
        "source_text": uncertain,
        "reason": "The reported salt form is not independently established.",
        "held_fields": ["IDENTITY_FORM"],
    }
    decision = {
        "path": relative,
        "recipe_id": record["id"],
        "expected_sha256": complete.digest(path.read_bytes()),
        "variants": [
            {
                "variant_index": 0,
                "variant_name": "assay",
                "append_changes": [change],
                "append_mentions": [mention],
            }
        ],
    }
    assert not validate_recipe(record)
    return tmp_path, path, decision


def decisions_file(root, records):
    path = root / "decisions.json"
    path.write_text(json.dumps({"schema_version": 1, "records": records}))
    return path


def run(root, decisions, receipt, *, apply=False):
    return writer.run(
        decisions, root=root, apply=apply, receipt=receipt, planner=complete.plan_record
    )


def invoke(monkeypatch, root, decisions, receipt, *, completed=None):
    monkeypatch.setattr(complete, "ROOT", root)
    args = ["curate_variant_completeness.py", str(decisions), "--apply", "--receipt", str(receipt)]
    if completed is not None:
        args += [
            "--completed-receipt",
            str(completed),
            "--expected-completed-receipt-sha256",
            complete.digest(completed.read_bytes()),
        ]
    monkeypatch.setattr(sys, "argv", args)
    return complete.main()


def assert_refused(call):
    try:
        result = call()
    except (ValueError, KeyError, TypeError, IndexError, writer.ApplyError):
        return
    except SystemExit as error:
        assert error.code != 0
        return
    assert isinstance(result, int) and result != 0, "mutation unexpectedly accepted"


def test_preview_and_native_apply_preserve_source_and_bind_one_history_event(sample):
    root, path, decision = sample
    original = path.read_bytes()
    before = yaml.safe_load(original)
    decisions = decisions_file(root, [decision])
    preview = run(root, decisions, root / "preview.json")
    assert preview["records"][0]["status"] == "PLANNED"
    assert path.read_bytes() == original
    result = run(root, decisions, root / "applied.json", apply=True)
    after_raw = path.read_bytes()
    after = yaml.safe_load(after_raw)
    assert result["state"] == "COMPLETE"
    row = result["records"][0]
    assert row["status"] == "APPLIED"
    assert row["before_text"].encode() == original
    assert row["after_text"].encode() == after_raw
    assert row["after_sha256"] == complete.digest(after_raw)
    assert not validate_recipe(after)
    assert after["ingredients"] == before["ingredients"]
    assert after["variants"][1] == before["variants"][1]
    assert after["curation_history"][:-1] == before["curation_history"]
    event = after["curation_history"][-1]
    assert event["action"] == complete.ACTION
    assert json.loads(event["changes"]) == {
        "decision_sha256": complete.digest(decisions.read_bytes()),
        "decision": decision,
    }
    assert after["variants"][0]["ingredient_changes"] == decision["variants"][0]["append_changes"]
    assert after["variants"][0]["ingredient_mentions"] == decision["variants"][0]["append_mentions"]
    offset = 0
    for line in original.decode().splitlines():
        offset = after_raw.decode().index(line, offset) + len(line)


@pytest.mark.parametrize("newline", [True, False])
def test_pinned_prose_and_scalar_correction_keep_other_source_bytes(sample, newline):
    root, path, decision = sample
    if not newline:
        path.write_bytes(path.read_bytes().rstrip(b"\n"))
    decision["expected_sha256"] = complete.digest(path.read_bytes())
    variant = decision["variants"][0]
    old = variant["append_changes"][0]["source_text"]
    replacement = "Set water input to 950 mL per batch; final volume is unspecified."
    variant["replace_modifications"] = [
        {"modification_index": 0, "expected": old, "replacement": replacement}
    ]
    variant["append_changes"][0]["source_text"] = replacement
    decision["field_replacements"] = [
        {
            "path": ["variants", 0, "description"],
            "expected": "Earlier assay description.",
            "replacement": "Corrected assay description.",
        }
    ]
    before = yaml.safe_load(path.read_bytes())
    run(root, decisions_file(root, [decision]), root / "applied.json", apply=True)
    after = yaml.safe_load(path.read_bytes())
    assert after["variants"][0]["modifications"][0] == replacement
    assert after["variants"][0]["ingredient_changes"][0]["source_text"] == replacement
    assert after["variants"][0]["description"] == "Corrected assay description."
    assert after["variants"][1] == before["variants"][1]
    assert (
        "description: |\n  Preserve this original line.\n  And this second line.\n"
        in path.read_text()
    )


@pytest.mark.parametrize("location", ["record", "variant", "replacement"])
def test_unknown_mutation_keys_refuse_before_any_write(sample, location):
    root, path, decision = sample
    if location == "record":
        decision["replace_ingredients"] = []
    elif location == "variant":
        decision["variants"][0]["append_mentons"] = decision["variants"][0].pop("append_mentions")
    else:
        decision["field_replacements"] = [
            {
                "path": ["variants", 0, "description"],
                "expected": "Earlier assay description.",
                "replacement": "Corrected description.",
                "ignore_beforeimage": True,
            }
        ]
    before = path.read_bytes()
    receipt = root / "must-not-complete.json"
    assert_refused(lambda: run(root, decisions_file(root, [decision]), receipt, apply=True))
    assert path.read_bytes() == before
    assert not receipt.exists()


@pytest.mark.parametrize(
    "mutation",
    ["stale_hash", "identity", "duplicate_variant", "source", "base_field", "grounded_hold"],
)
def test_invalid_decision_refuses_before_any_write(sample, mutation):
    root, path, decision = sample
    if mutation == "stale_hash":
        decision["expected_sha256"] = "0" * 64
    elif mutation == "identity":
        decision["recipe_id"] = "CultureMech:999999"
    elif mutation == "duplicate_variant":
        decision["variants"].append(copy.deepcopy(decision["variants"][0]))
    elif mutation == "source":
        decision["variants"][0]["append_changes"][0]["source_text"] += " unreviewed"
    elif mutation == "grounded_hold":
        decision["variants"][0]["append_mentions"][0]["term"] = {"id": "CHEBI:15377"}
    else:
        decision["field_replacements"] = [
            {"path": ["ingredients"], "expected": [{"preferred_term": "water"}], "replacement": []}
        ]
    before = path.read_bytes()
    receipt = root / "refused.json"
    assert_refused(lambda: run(root, decisions_file(root, [decision]), receipt, apply=True))
    assert path.read_bytes() == before
    assert not receipt.exists()


@pytest.mark.parametrize("retain_other", [False, True])
def test_exact_target_organism_removal_keeps_empty_or_remaining_list(sample, retain_other):
    root, path, decision = sample
    record = yaml.safe_load(path.read_bytes())
    if retain_other:
        record["target_organisms"].append({"preferred_term": "Other synthetic organism"})
        path.write_text(yaml.safe_dump(record, sort_keys=False))
    before = copy.deepcopy(record)
    decision["expected_sha256"] = complete.digest(path.read_bytes())
    decision["variants"] = []
    decision["field_replacements"] = [
        {
            "path": ["target_organisms"],
            "expected": record["target_organisms"],
            "replacement": record["target_organisms"][1:],
        }
    ]
    run(root, decisions_file(root, [decision]), root / "removed.json", apply=True)
    after = yaml.safe_load(path.read_bytes())
    assert after["target_organisms"] == before["target_organisms"][1:]
    assert after["variants"] == before["variants"]
    assert after["ingredients"] == before["ingredients"]
    assert after["curation_history"][:-1] == before["curation_history"]
    assert not validate_recipe(after)


def test_every_record_is_prevalidated_before_first_write(sample):
    root, path, decision = sample
    other = path.with_name("other.yaml")
    other.write_bytes(path.read_bytes().replace(b"CultureMech:000001", b"CultureMech:000002"))
    second = copy.deepcopy(decision)
    second.update(
        path=str(other.relative_to(root)), recipe_id="CultureMech:000002", expected_sha256="0" * 64
    )
    original = path.read_bytes(), other.read_bytes()
    receipt = root / "refused-batch.json"
    assert_refused(lambda: run(root, decisions_file(root, [decision, second]), receipt, apply=True))
    assert (path.read_bytes(), other.read_bytes()) == original
    assert not receipt.exists()


def test_native_writer_failure_retains_input_and_durable_incomplete_receipt(sample, monkeypatch):
    root, path, decision = sample
    before = path.read_bytes()

    def fail(record, destination):
        raise ValueError("synthetic native-writer rejection")

    monkeypatch.setattr(writer, "write_validated_recipe", fail)
    receipt = root / "incomplete.json"
    with pytest.raises(writer.ApplyError):
        run(root, decisions_file(root, [decision]), receipt, apply=True)
    assert path.read_bytes() == before
    saved = json.loads(receipt.read_bytes())
    assert saved["state"] == "INCOMPLETE"
    assert saved["records"][0]["observed_sha256"] == complete.digest(before)


def test_intervening_source_mutation_is_not_overwritten(sample, monkeypatch):
    root, path, decision = sample
    foreign = path.read_bytes() + b"# concurrent independent edit\n"
    original_writer = writer.write_validated_recipe

    def race(record, destination):
        original_writer(record, destination)
        path.write_bytes(foreign)

    monkeypatch.setattr(writer, "write_validated_recipe", race)
    receipt = root / "race.json"
    with pytest.raises(writer.ApplyError, match="changed after preview"):
        run(root, decisions_file(root, [decision]), receipt, apply=True)
    assert path.read_bytes() == foreign
    assert json.loads(receipt.read_bytes())["state"] == "INCOMPLETE"


def test_completed_replay_preserves_original_edge_through_multiple_receipts(sample, monkeypatch):
    root, path, decision = sample
    decisions = decisions_file(root, [decision])
    first = root / "first.json"
    assert invoke(monkeypatch, root, decisions, first) == 0
    before_replay = path.read_bytes()
    original_row = json.loads(first.read_bytes())["records"][0]
    previous = first
    for name in ("second.json", "third.json"):
        receipt = root / name
        assert invoke(monkeypatch, root, decisions, receipt, completed=previous) == 0
        saved = json.loads(receipt.read_bytes())
        assert saved["state"] == "COMPLETE"
        row = saved["records"][0]
        assert row["status"] == "UNCHANGED"
        for key in ("before_sha256", "after_sha256", "before_text", "after_text"):
            assert row[key] == original_row[key]
        assert path.read_bytes() == before_replay
        previous = receipt


def test_replay_cannot_certify_a_proposal_changed_between_validation_and_read(sample, monkeypatch):
    root, path, decision = sample
    decisions = decisions_file(root, [decision])
    first = root / "first.json"
    assert invoke(monkeypatch, root, decisions, first) == 0
    original_digest = complete.digest(decisions.read_bytes())
    after_apply = path.read_bytes()
    original_run = complete.run

    def race(*args, **kwargs):
        document = json.loads(decisions.read_bytes())
        document["records"][0]["variants"][0]["append_changes"][0][
            "stage"
        ] = "unapplied replacement stage"
        decisions.write_text(json.dumps(document))
        return original_run(*args, **kwargs)

    monkeypatch.setattr(complete, "run", race)
    receipt = root / "raced-replay.json"
    try:
        result = invoke(monkeypatch, root, decisions, receipt, completed=first)
    except (ValueError, KeyError, TypeError, writer.ApplyError):
        result = 1
    assert path.read_bytes() == after_apply
    if result == 0:
        # A single-read implementation may finish the original authenticated plan.
        assert json.loads(receipt.read_bytes())["decision_sha256"] == original_digest
    elif receipt.exists():
        assert json.loads(receipt.read_bytes()).get("state") != "COMPLETE"


def test_modified_completed_receipt_text_is_refused_even_with_its_new_digest(sample, monkeypatch):
    root, path, decision = sample
    decisions = decisions_file(root, [decision])
    first = root / "first.json"
    assert invoke(monkeypatch, root, decisions, first) == 0
    before = path.read_bytes()
    saved = json.loads(first.read_bytes())
    saved["records"][0]["after_text"] += "\n"
    first.write_text(json.dumps(saved))
    receipt = root / "forged.json"
    assert_refused(lambda: invoke(monkeypatch, root, decisions, receipt, completed=first))
    assert path.read_bytes() == before
    assert not receipt.exists()
