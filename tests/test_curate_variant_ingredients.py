"""Fail-closed application and replay of reviewed variant decisions (#683)."""

import copy
import hashlib
import json

import curate_variant_ingredients as curate
import pytest
import yaml


@pytest.fixture
def sample(tmp_path, monkeypatch):
    monkeypatch.setattr(curate, "validate_recipe", lambda record: [])
    monkeypatch.setattr(
        curate,
        "write_validated_recipe",
        lambda record, path: path.write_text(
            yaml.safe_dump(
                record, sort_keys=False, allow_unicode=True, default_flow_style=False, width=80
            )
        ),
    )
    relative = "data/normalized_yaml/algae/example.yaml"
    path = tmp_path / relative
    path.parent.mkdir(parents=True)
    record = {
        "id": "CultureMech:000001",
        "name": "example",
        "ingredients": [],
        "variants": [{"name": "exposure", "modifications": ["Add example compound."]}],
    }
    path.write_text(yaml.safe_dump(record, sort_keys=False))
    change = {
        "action": "ADD",
        "ingredient": {"preferred_term": "example compound"},
        "stage": "assay",
        "source_modification_index": 0,
        "source_text": "Add example compound.",
        "evidence": [
            {
                "reference": "https://example.org/protocol",
                "supports": "SUPPORT",
                "snippet": "Add example compound.",
                "explanation": "Synthetic fixture.",
            }
        ],
    }
    decision = {
        "path": relative,
        "recipe_id": record["id"],
        "expected_sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "variants": [
            {"variant_index": 0, "variant_name": "exposure", "ingredient_changes": [change]}
        ],
    }
    return tmp_path, path, decision


def save_decisions(root, records):
    path = root / "decisions.json"
    path.write_text(json.dumps({"schema_version": 1, "records": records}))
    return path


def test_preview_preserves_bytes_and_apply_keeps_parent_and_prose(sample):
    root, path, decision = sample
    before = path.read_bytes()
    decisions = save_decisions(root, [decision])
    assert curate.run(decisions, root=root)["records"][0]["status"] == "PLANNED"
    assert path.read_bytes() == before
    result = curate.run(decisions, root=root, apply=True)
    assert result["records"][0]["status"] == "APPLIED"
    after = yaml.safe_load(path.read_text())
    original = yaml.safe_load(before)
    assert after["ingredients"] == original["ingredients"]
    assert after["variants"][0]["modifications"] == original["variants"][0]["modifications"]
    assert after["variants"][0]["ingredient_changes"][0]["stage"] == "assay"
    assert len(after["curation_history"]) == 1
    applied_bytes = path.read_bytes()
    assert curate.run(decisions, root=root, apply=True)["records"][0]["status"] == "UNCHANGED"
    assert path.read_bytes() == applied_bytes


@pytest.mark.parametrize("trailing_newline", [True, False])
@pytest.mark.parametrize("history_first", [True, False])
def test_preserves_block_scalars_comments_and_multiple_variant_boundaries(
    sample, trailing_newline, history_first
):
    root, path, decision = sample
    history = "curation_history:\n  - action: OLD\n    notes: 'untouched history'\n"
    original = (
        "# source comment\nid: CultureMech:000001\nname: 'example β'\n"
        "ingredients: []\ndescription: |\n  Literal line one.\n  Literal line two.\n"
        + (history if history_first else "")
        + "variants:\n  - name: exposure\n    modifications:\n"
        "      - Add example compound.\n    notes: >-\n      Folded text\n      stays folded.\n"
        "  # next variant comment\n  - name: second\n    modifications:\n"
        "      - Add example compound.\n" + ("" if history_first else history)
    )
    if not trailing_newline:
        original = original.rstrip("\n")
    path.write_text(original)
    decision["expected_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    second = copy.deepcopy(decision["variants"][0])
    second.update(variant_index=1, variant_name="second")
    decision["variants"].append(second)
    before = yaml.safe_load(original)
    curate.run(save_decisions(root, [decision]), root=root, apply=True)
    after_text = path.read_text()
    # Every source line survives verbatim and in order, including quote style.
    position = 0
    for line in original.splitlines():
        position = after_text.index(line, position) + len(line)
    after = yaml.safe_load(after_text)
    for variant in after["variants"]:
        assert len(variant.pop("ingredient_changes")) == 1
    after["curation_history"].pop()
    assert after == before


def test_flow_variant_refused_before_write(sample):
    root, path, decision = sample
    record = yaml.safe_load(path.read_bytes())
    path.write_text(yaml.safe_dump(record, default_flow_style=True))
    decision["expected_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    before = path.read_bytes()
    with pytest.raises(ValueError, match="block-style"):
        curate.run(save_decisions(root, [decision]), root=root, apply=True)
    assert path.read_bytes() == before


def test_long_new_fragments_keep_native_canonical_record_canonical(sample):
    from record_io import dump_record

    root, path, decision = sample
    record = yaml.safe_load(path.read_bytes())
    record["notes"] = "An existing long note with source qualifications. " * 8
    path.write_text(dump_record(record))
    before = path.read_text()
    assert dump_record(yaml.safe_load(before)) == before
    decision["expected_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    change = decision["variants"][0]["ingredient_changes"][0]
    change["ingredient"]["notes"] = (
        "A new nested ingredient qualification with a long source description. " * 7
    )
    change["evidence"][0]["explanation"] = (
        "A long exact source explanation retains the experimental stage and dose basis. " * 9
    )
    curate.run(save_decisions(root, [decision]), root=root, apply=True)
    after = path.read_text()
    assert dump_record(yaml.safe_load(after)) == after
    assert yaml.safe_load(after)["notes"] == record["notes"]


def test_shared_alias_cannot_mutate_unselected_variant(sample):
    root, path, decision = sample
    path.write_text(
        "id: CultureMech:000001\nname: example\ningredients: []\nvariants:\n"
        "- &shared\n  name: exposure\n  modifications:\n  - Add example compound.\n"
        "- *shared\n"
    )
    decision["expected_sha256"] = hashlib.sha256(path.read_bytes()).hexdigest()
    before = path.read_bytes()
    with pytest.raises(ValueError, match="aliases and anchors"):
        curate.run(save_decisions(root, [decision]), root=root, apply=True)
    assert path.read_bytes() == before


def test_single_record_canary_retains_full_decision_hash(sample):
    root, path, decision = sample
    second = copy.deepcopy(decision)
    second["path"] = "data/normalized_yaml/algae/second.yaml"
    second_path = root / second["path"]
    second_path.write_bytes(path.read_bytes())
    before = second_path.read_bytes()
    decisions = save_decisions(root, [decision, second])
    with pytest.raises(ValueError, match="absent"):
        curate.run(decisions, root=root, apply=True, only_record="missing.yaml")
    result = curate.run(decisions, root=root, apply=True, only_record=decision["path"])
    assert len(result["records"]) == 1
    assert result["records"][0]["status"] == "APPLIED"
    assert second_path.read_bytes() == before
    event = yaml.safe_load(path.read_bytes())["curation_history"][-1]
    assert (
        json.loads(event["changes"])["decision_sha256"]
        == hashlib.sha256(decisions.read_bytes()).hexdigest()
    )


@pytest.mark.parametrize("fault", ["hash", "record", "variant", "source", "index"])
def test_stale_or_wrong_target_refused_without_write(sample, fault):
    root, path, original = sample
    decision = copy.deepcopy(original)
    if fault == "hash":
        decision["expected_sha256"] = "0" * 64
    elif fault == "record":
        decision["recipe_id"] = "CultureMech:999999"
    elif fault == "variant":
        decision["variants"][0]["variant_name"] = "different"
    elif fault == "source":
        decision["variants"][0]["ingredient_changes"][0]["source_text"] = "Different prose."
    else:
        decision["variants"][0]["ingredient_changes"][0]["source_modification_index"] = -1
    before = path.read_bytes()
    with pytest.raises(ValueError):
        curate.run(save_decisions(root, [decision]), root=root, apply=True)
    assert path.read_bytes() == before


def test_entire_batch_is_checked_before_first_write(sample):
    root, path, decision = sample
    second = copy.deepcopy(decision)
    second["path"] = "data/normalized_yaml/algae/second.yaml"
    (root / second["path"]).write_bytes(path.read_bytes())
    second["recipe_id"] = "CultureMech:999999"
    before = path.read_bytes()
    with pytest.raises(ValueError, match="identity mismatch"):
        curate.run(save_decisions(root, [decision, second]), root=root, apply=True)
    assert path.read_bytes() == before


def test_rejects_path_outside_authority_and_symlink(sample):
    root, path, decision = sample
    decision["path"] = "../../outside.yaml"
    with pytest.raises(ValueError, match="relative"):
        curate.run(save_decisions(root, [decision]), root=root, apply=True)
    link = path.with_name("link.yaml")
    link.symlink_to(path)
    decision["path"] = str(link.relative_to(root))
    with pytest.raises(ValueError, match="non-symlink"):
        curate.run(save_decisions(root, [decision]), root=root, apply=True)


def test_schema_failure_refuses_before_first_write(sample, monkeypatch):
    root, path, decision = sample

    class Error:
        message = "invalid structured variant"

    monkeypatch.setattr(curate, "validate_recipe", lambda record: [Error()])
    before = path.read_bytes()
    with pytest.raises(ValueError, match="fails validation"):
        curate.run(save_decisions(root, [decision]), root=root, apply=True)
    assert path.read_bytes() == before


def test_partial_native_write_cannot_damage_authoritative_record(sample, monkeypatch):
    root, path, decision = sample
    before = path.read_bytes()

    def interrupted_writer(record, destination):
        destination.write_text("id: truncated")
        raise OSError("simulated full disk")

    monkeypatch.setattr(curate, "write_validated_recipe", interrupted_writer)
    receipt = root / "receipt.json"
    with pytest.raises(curate.ApplyError):
        curate.run(save_decisions(root, [decision]), root=root, apply=True, receipt=receipt)
    assert path.read_bytes() == before
    assert json.loads(receipt.read_text())["state"] == "INCOMPLETE"
    assert not list(path.parent.glob(".variant-*.tmp"))


def test_later_drift_preserves_applied_and_unapplied_outcomes(sample, monkeypatch):
    root, path, decision = sample
    second = copy.deepcopy(decision)
    second["path"] = "data/normalized_yaml/algae/second.yaml"
    second_path = root / second["path"]
    second_path.write_bytes(path.read_bytes())
    writer = curate.write_validated_recipe
    calls = []

    def drift_after_first_stage(record, destination):
        writer(record, destination)
        calls.append(destination)
        if len(calls) == 1:
            second_path.write_text(second_path.read_text() + "# concurrent edit\n")

    monkeypatch.setattr(curate, "write_validated_recipe", drift_after_first_stage)
    receipt = root / "receipt.json"
    with pytest.raises(curate.ApplyError, match="changed after preview") as error:
        curate.run(save_decisions(root, [decision, second]), root=root, apply=True, receipt=receipt)
    persisted = json.loads(receipt.read_text())
    assert persisted == error.value.receipt
    assert persisted["records"][0]["status"] == "APPLIED"
    assert persisted["records"][1]["status"] == "APPLYING"
    assert (
        persisted["records"][0]["observed_sha256"] == hashlib.sha256(path.read_bytes()).hexdigest()
    )
    assert second_path.read_text().endswith("# concurrent edit\n")


def test_unusable_receipt_refuses_before_any_authoritative_write(sample):
    root, path, decision = sample
    before = path.read_bytes()
    blocker = root / "not-a-directory"
    blocker.write_text("reserved")
    with pytest.raises(OSError):
        curate.run(
            save_decisions(root, [decision]),
            root=root,
            apply=True,
            receipt=blocker / "receipt.json",
        )
    assert path.read_bytes() == before


def test_receipt_failure_after_replace_reports_actual_applied_state(sample, monkeypatch):
    root, path, decision = sample
    persist = curate.persist_receipt

    def fail_after_apply(destination, result):
        if result["records"][0]["status"] == "APPLIED":
            raise OSError("receipt disk failure")
        persist(destination, result)

    monkeypatch.setattr(curate, "persist_receipt", fail_after_apply)
    receipt = root / "receipt.json"
    with pytest.raises(curate.ApplyError) as error:
        curate.run(save_decisions(root, [decision]), root=root, apply=True, receipt=receipt)
    assert error.value.receipt["records"][0]["status"] == "APPLIED"
    saved = json.loads(receipt.read_text())["records"][0]
    assert saved["status"] == "APPLYING"
    assert saved["planned_after_sha256"] == hashlib.sha256(path.read_bytes()).hexdigest()
