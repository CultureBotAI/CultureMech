"""Cohort and coverage boundaries from independent review (#785–787, 2026-11-16).

Synthetic source/queue fixtures exercise this accounting layer. Capsule inversion
and the immutable production queue contract have separate exact-evidence tests.
"""

from __future__ import annotations

import copy
import json

import audit_variant_completeness_successor as capsule
import audit_variant_ingredient_successor as earlier
import pytest
import yaml
from adhoc import audit_variant_completeness_683 as audit

from tests import test_curate_variant_completeness as updater_tests
from tests.test_curate_variant_completeness import run

sample = updater_tests.sample


def save(path, document):
    path.write_text(json.dumps(document))
    return str(path), audit.digest(path.read_bytes())


def disposition(number, status="STRUCTURED"):
    return {
        "queue_row_number": number,
        "status": status,
        "reason": "Synthetic reviewed source classification.",
    }


def cohorts(sample):
    root, _, decision = sample
    left, right = copy.deepcopy(decision), copy.deepcopy(decision)
    del left["variants"][0]["append_mentions"]
    del right["variants"][0]["append_changes"]
    first = {"schema_version": 1, "records": [left], "dispositions": [disposition(1)]}
    second = {
        "schema_version": 1,
        "records": [right],
        "dispositions": [disposition(2, "HELD_EVIDENCE")],
    }
    return root, first, second


def test_merge_preserves_both_cohorts_without_touching_recipe(sample, monkeypatch):
    root, first, second = cohorts(sample)
    monkeypatch.setattr(audit, "ROOT", root)
    before = sample[1].read_bytes()
    inputs = [save(root / "first.json", first), save(root / "second.json", second)]
    output = root / "merged.json"
    receipt = audit.merge(inputs, output)
    merged = json.loads(output.read_bytes())
    assert receipt["records"] == 1 and receipt["dispositions"] == 2
    assert (
        merged["records"][0]["variants"][0]["append_changes"]
        == first["records"][0]["variants"][0]["append_changes"]
    )
    assert (
        merged["records"][0]["variants"][0]["append_mentions"]
        == second["records"][0]["variants"][0]["append_mentions"]
    )
    assert [row["queue_row_number"] for row in merged["dispositions"]] == [1, 2]
    assert sample[1].read_bytes() == before


def test_unknown_instruction_in_second_shared_record_is_not_discarded(sample, monkeypatch):
    root, first, second = cohorts(sample)
    monkeypatch.setattr(audit, "ROOT", root)
    second["records"][0]["replace_ingredients"] = []
    inputs = [save(root / "first.json", first), save(root / "second.json", second)]
    output = root / "must-not-publish.json"
    with pytest.raises(ValueError):
        audit.merge(inputs, output)
    assert not output.exists()


def test_duplicate_records_inside_one_cohort_are_not_cross_cohort_composition(sample, monkeypatch):
    root, first, second = cohorts(sample)
    monkeypatch.setattr(audit, "ROOT", root)
    first["records"] += second["records"]
    first["dispositions"] += second["dispositions"]
    output = root / "must-not-publish.json"
    with pytest.raises(ValueError):
        audit.merge([save(root / "duplicate.json", first)], output)
    assert not output.exists()


@pytest.mark.parametrize("kind", ["absolute", "parent_components"])
def test_merger_requires_authoritative_canonical_recipe_paths(sample, monkeypatch, kind):
    root, first, _ = cohorts(sample)
    monkeypatch.setattr(audit, "ROOT", root)
    first["records"][0]["path"] = (
        str(sample[1])
        if kind == "absolute"
        else "data/normalized_yaml/algae/../algae/completeness.yaml"
    )
    output = root / "unsafe.json"
    with pytest.raises(ValueError):
        audit.merge([save(root / "source.json", first)], output)
    assert not output.exists()


def test_disposition_only_decision_stays_in_ledger_without_empty_mutation(sample, monkeypatch):
    root, _, decision = sample
    monkeypatch.setattr(audit, "ROOT", root)
    decision["variants"] = []
    document = {
        "schema_version": 1,
        "records": [decision],
        "dispositions": [disposition(1, "CONTEXT_ONLY")],
    }
    output = root / "context-only.json"
    audit.merge([save(root / "source.json", document)], output)
    merged = json.loads(output.read_bytes())
    assert merged["records"] == []
    assert merged["dispositions"] == document["dispositions"]


@pytest.fixture
def audited(sample, monkeypatch, request):
    root, path, decision = sample
    status = getattr(request, "param", "STRUCTURED")
    mode = status
    if mode in {"VALID_PARTIAL", "PARTIAL_MENTIONS_ONLY", "STRUCTURED_MENTIONS_ONLY"}:
        status = "STRUCTURED" if mode == "STRUCTURED_MENTIONS_ONLY" else "PARTIALLY_STRUCTURED"
        decision["variants"][0]["append_mentions"].append(
            {
                "source_label": "water",
                "reported_action": "SET_CONCENTRATION",
                "stage": "synthetic batch preparation",
                "source_modification_index": 0,
                "source_text": decision["variants"][0]["append_changes"][0]["source_text"],
                "reason": "Final concentration is withheld; the literal batch amount remains supported.",
                "held_fields": ["QUANTITY"],
            }
        )
    if mode in {"PARTIAL_MENTIONS_ONLY", "STRUCTURED_MENTIONS_ONLY", "EMPTY_PARTIAL"}:
        del decision["variants"][0]["append_changes"]
    if mode == "EMPTY_PARTIAL":
        status = "PARTIALLY_STRUCTURED"
    before = path.read_bytes()
    original = yaml.safe_load(before)
    rows = []
    for index, source in enumerate(original["variants"][0]["modifications"]):
        rows.append(
            {
                "record_path": decision["path"],
                "source_path": "algae/completeness.yaml",
                "source_sha256": audit.digest(before),
                "recipe_id": decision["recipe_id"],
                "variant_index": 0,
                "variant_name": "assay",
                "modification_index": index,
                "modification_text": source,
            }
        )
    statuses = [disposition(1, status), disposition(2, "HELD_EVIDENCE")]
    document = {"schema_version": 1, "records": [decision], "dispositions": statuses}
    proposal = root / "applied-proposal.json"
    _, pin = save(proposal, document)
    run(root, proposal, root / "apply.json", apply=True)
    after = path.read_bytes()
    prior = root / "conf/variant_ingredient_curation/synthetic-prior.json"
    prior.parent.mkdir(parents=True)
    prior.write_text(json.dumps({"dispositions": statuses}))
    queue = root / "queue.tsv"
    queue.write_text("Synthetic queue fixture; immutable queue parser is tested separately.\n")
    monkeypatch.setattr(audit, "ROOT", root)
    monkeypatch.setattr(audit, "PRIOR", ("synthetic-prior",))
    monkeypatch.setattr(audit, "read_queue", lambda raw: (copy.deepcopy(rows), {}))
    monkeypatch.setattr(
        capsule,
        "retained_evidence",
        lambda: (
            {decision["path"]: {}},
            {decision["path"]: decision},
            {"decisions": {"sha256": pin}},
        ),
    )

    def restored(raw, relative):
        assert relative == decision["path"] and raw == after
        return before

    monkeypatch.setattr(earlier, "restore_before", restored)
    return root, queue, proposal, pin, prior


def test_audit_accounts_supported_and_withheld_rows_separately(audited):
    root, queue, proposal, pin, _ = audited
    output = root / "coverage"
    summary = audit.audit(queue, proposal, pin, output)
    assert summary["result"] == "PASS"
    assert summary["queue_rows"] == 2 and summary["queue_recipes"] == 1
    assert summary["applied_assertions"] == 1 and summary["held_mentions"] == 1
    assert summary["dispositions"] == {"STRUCTURED": 1, "WITHHELD_NAMED_CLAIMS": 1}
    assert json.loads((output / "summary.json").read_bytes())["reviewed_proposal_sha256"] == pin


def test_unapplied_pinned_proposal_cannot_label_another_capsules_coverage(audited):
    root, queue, proposal, _, _ = audited
    other = json.loads(proposal.read_bytes())
    other["records"][0]["variants"][0]["append_changes"][0]["stage"] = "Unapplied proposal stage"
    alternative = root / "alternative.json"
    _, pin = save(alternative, other)
    output = root / "must-not-publish"
    with pytest.raises(ValueError, match="authenticated applied"):
        audit.audit(queue, alternative, pin, output)
    assert not output.exists()


@pytest.mark.parametrize("audited", ["VALID_PARTIAL"], indirect=True)
def test_supported_amount_with_withheld_concentration_remains_partial(audited):
    root, queue, proposal, pin, _ = audited
    summary = audit.audit(queue, proposal, pin, root / "coverage")
    assert summary["applied_assertions"] == 1
    assert summary["held_mentions"] == 2
    assert summary["dispositions"] == {"PARTIALLY_STRUCTURED": 1, "WITHHELD_NAMED_CLAIMS": 1}


@pytest.mark.parametrize("audited", ["PARTIAL_MENTIONS_ONLY"], indirect=True)
def test_partial_disposition_can_retain_only_mentions_without_inventing_an_event(audited):
    """A supported field plus a remaining hold need not establish ADD/SET (#790)."""
    root, queue, proposal, pin, _ = audited
    summary = audit.audit(queue, proposal, pin, root / "coverage")
    assert summary["applied_assertions"] == 0
    assert summary["held_mentions"] == 2
    assert summary["changes_by_action"] == {}
    assert summary["dispositions"] == {"WITHHELD_NAMED_CLAIMS": 2}


@pytest.mark.parametrize("audited", ["EMPTY_PARTIAL", "STRUCTURED_MENTIONS_ONLY"], indirect=True)
def test_empty_partial_and_promotion_of_mentions_to_structured_events_are_refused(audited):
    root, queue, proposal, pin, _ = audited
    output = root / "must-not-publish"
    with pytest.raises(ValueError):
        audit.audit(queue, proposal, pin, output)
    assert not output.exists()


@pytest.mark.parametrize(
    "audited", ["HELD_EVIDENCE", "HELD_MODEL", "PARTIALLY_STRUCTURED", "INVENTED"], indirect=True
)
def test_existing_positive_change_cannot_erase_explicit_hold_or_invalid_status(audited):
    root, queue, proposal, pin, _ = audited
    output = root / "must-not-publish"
    with pytest.raises(ValueError):
        audit.audit(queue, proposal, pin, output)
    assert not output.exists()


@pytest.mark.parametrize("source", ["queue", "proposal", "prior"])
def test_inputs_changed_during_audit_refuse_before_publication(audited, monkeypatch, source):
    root, queue, proposal, pin, prior = audited
    original_validate = audit.validate_recipe
    changed = {"queue": queue, "proposal": proposal, "prior": prior}[source]

    def race(record):
        result = original_validate(record)
        changed.write_bytes(changed.read_bytes() + b"\n")
        return result

    monkeypatch.setattr(audit, "validate_recipe", race)
    output = root / "must-not-publish"
    with pytest.raises(ValueError, match="changed during coverage audit"):
        audit.audit(queue, proposal, pin, output)
    assert not output.exists()
