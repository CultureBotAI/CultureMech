"""Keep source binding coverage separate from release approval (#687)."""

import csv
import hashlib
import json

import pytest
import report_integration_handoff as report


def write_json(path, value):
    path.write_text(json.dumps(value), encoding="utf-8")
    return hashlib.sha256(path.read_bytes()).hexdigest()


@pytest.fixture
def handoff(tmp_path):
    bundle, intake, reviewed = (tmp_path / name for name in ("bundle", "intake", "reviewed"))
    for path in (bundle, intake, reviewed):
        path.mkdir()
    # A supported identity with context-only use must never become positive presence.
    records = [
        {
            "case_id": "positive",
            "disposition": "SUPPORTED",
            "positive_occurrences": "2",
            "context_only_mentions": "0",
            "held_source_mentions": "0",
            "change_action": "ADD",
        },
        {
            "case_id": "context",
            "disposition": "SUPPORTED",
            "positive_occurrences": "0",
            "context_only_mentions": "1",
            "held_source_mentions": "0",
            "change_action": "REMOVE",
        },
        {
            "case_id": "held",
            "disposition": "WITHHOLD",
            "positive_occurrences": "0",
            "context_only_mentions": "0",
            "held_source_mentions": "1",
            "change_action": "",
        },
    ]
    products = {}
    for name, subset in [
        ("binding-dispositions.tsv", records),
        ("supported-bindings.tsv", records[:2]),
        ("withheld-bindings.tsv", records[2:]),
    ]:
        with (reviewed / name).open("w", newline="") as stream:
            writer = csv.DictWriter(stream, fieldnames=list(records[0]), delimiter="\t")
            writer.writeheader()
            writer.writerows(subset)
        products[name] = report.fingerprint(reviewed / name)
    source = {
        "contract": "culturemech-direct-ingredients-v3",
        "integrated_release": False,
        "git": {"commit": "a" * 40},
        "products": {},
        "counts": {
            "occurrences": 2,
            "variant_context_only_mentions": 1,
            "variant_held_mentions": 1,
        },
    }
    pins = {"source": write_json(bundle / "manifest.json", source)}
    prepared = {
        "source_manifest_sha256": pins["source"],
        "source_contract": source["contract"],
        "source_producer_commit": source["git"]["commit"],
        "counts": {"cases": 3},
        "canonical_sssom": {"status": "historical_snapshot"},
    }
    pins["intake"] = write_json(intake / "intake.json", prepared)
    accepted = {
        "status": "REVIEWED_SOURCE_INTAKE",
        "source_manifest_sha256": pins["source"],
        "source_contract": source["contract"],
        "intake_sha256": pins["intake"],
        "files": products,
        "counts": {"SUPPORTED": 2, "WITHHOLD": 1},
        "canonical_sssom": prepared["canonical_sssom"],
    }
    pins["reviewed"] = write_json(reviewed / "reviewed-intake.json", accepted)
    return bundle, intake, reviewed, pins


def test_supported_context_never_becomes_positive_or_release_approval(handoff):
    result = report.audit(*handoff)
    assert result["integrated_release_ready"] is False
    assert result["binding_coverage"]["supported"]["positive_occurrences"] == 2
    assert result["binding_coverage"]["supported"]["context_only_mentions"] == 1
    assert result["binding_coverage"]["withheld"]["held_source_mentions"] == 1


def test_independent_manifest_pin_required(handoff):
    bundle, intake, reviewed, pins = handoff
    with pytest.raises(report.HandoffError, match="pin mismatch"):
        report.audit(bundle, intake, reviewed, {**pins, "source": "0" * 64})


def test_modified_supported_product_rejected(handoff):
    bundle, intake, reviewed, pins = handoff
    path = reviewed / "supported-bindings.tsv"
    path.write_text(path.read_text() + "\n")
    with pytest.raises(report.HandoffError, match="Product mismatch"):
        report.audit(bundle, intake, reviewed, pins)


def test_cross_intake_relationship_rejected_even_with_matching_manifest_pin(handoff):
    bundle, intake, reviewed, pins = handoff
    path = reviewed / "reviewed-intake.json"
    data = json.loads(path.read_text())
    data["intake_sha256"] = "0" * 64
    pins["reviewed"] = write_json(path, data)
    with pytest.raises(report.HandoffError, match="Prepared intake relationship"):
        report.audit(bundle, intake, reviewed, pins)


def test_duplicate_binding_cases_are_rejected():
    with pytest.raises(report.HandoffError, match="Duplicate"):
        report.keyed([{"case_id": "same"}, {"case_id": "same"}])


@pytest.mark.parametrize("count", ["-1", "1.5", "1e2", ""])
def test_counts_cannot_mask_excluded_or_negative_occurrences(count):
    with pytest.raises(report.HandoffError, match="Invalid count"):
        report.summarize([{"positive_occurrences": count}])
