"""Adversarial fixtures for the retained concentration-audit driver."""

import copy
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
DRIVER = ROOT / "reports/ingredient_concentration_review/20261005T175229Z/review_driver.py"
spec = importlib.util.spec_from_file_location("concentration_review_driver", DRIVER)
driver = importlib.util.module_from_spec(spec)
spec.loader.exec_module(driver)


@pytest.fixture
def snapshot(tmp_path):
    doc = {
        "id": "CultureMech:000001",
        "ingredients": [
            {
                "preferred_term": "Sodium chloride",
                "concentration": {"value": "1", "unit": "G_PER_L"},
            }
        ],
    }
    row = {
        "path": "data/fixtures/recipe.yaml",
        "id": doc["id"],
        "sha256": hashlib.sha256(b"fixture").hexdigest(),
        "layer": "normalized",
        "record_kind": "MEDIUM",
        "claims": driver.collect_claims(doc)[0],
    }
    (tmp_path / "inventory.jsonl").write_text(json.dumps(row) + "\n")
    (tmp_path / "run.json").write_text(json.dumps({"commit": "fixture", "records": 1}))
    return tmp_path, row


def test_no_validation_marker_is_pending(snapshot):
    out, _ = snapshot
    driver.render(out)
    assert (
        "Closed-schema validation not yet finalized"
        in next((out / "records").rglob("*.md")).read_text()
    )


@pytest.mark.parametrize("marker", [{}, {"status": "failed", "exit_code": 1, "files_scanned": 0}])
def test_invalid_validation_marker_cannot_claim_zero_errors(snapshot, marker):
    out, _ = snapshot
    (out / "validation_complete.json").write_text(json.dumps(marker))
    with pytest.raises(ValueError, match="validation"):
        driver.render(out)
    assert not (out / "manifest.tsv").exists()


def source_check(row):
    claim = row["claims"][0]
    return {
        "path": row["path"],
        "field": claim["field"],
        "expected_record_id": row["id"],
        "expected_record_sha256": row["sha256"],
        "expected_ingredient": claim["ingredient"],
        "expected_identity": claim["identity"],
        "expected_old": claim["old"],
        "status": "evidence_only",
        "source_check": "inspected_amount_and_basis",
        "reference": "https://example.org/recipe",
        "snippet": "Sodium chloride 1 g/L",
        "locator": "ingredient table",
        "explanation": "Exact formulation and final volume inspected.",
    }


@pytest.mark.parametrize(
    "field",
    [
        "expected_record_id",
        "expected_record_sha256",
        "expected_ingredient",
        "expected_identity",
        "expected_old",
    ],
)
def test_source_check_rejects_wrong_identity_or_snapshot(snapshot, field):
    out, row = snapshot
    check = source_check(row)
    check[field] = "different"
    (out / "source_checks.json").write_text(json.dumps([check]))
    with pytest.raises(ValueError, match="Source check"):
        driver.render(out)
    assert not (out / "manifest.tsv").exists()


@pytest.mark.parametrize("mutation", ["duplicate", "unmatched", "missing_guard", "missing_snippet"])
def test_source_checks_are_not_silently_dropped(snapshot, mutation):
    out, row = snapshot
    checks = [source_check(row)]
    if mutation == "duplicate":
        checks.append(copy.deepcopy(checks[0]))
    elif mutation == "unmatched":
        checks[0]["field"] = "ingredients[99].concentration"
    elif mutation == "missing_guard":
        del checks[0]["expected_record_sha256"]
    else:
        del checks[0]["snippet"]
    (out / "source_checks.json").write_text(json.dumps(checks))
    with pytest.raises(ValueError, match="Source check"):
        driver.render(out)
    assert not (out / "manifest.tsv").exists()


def test_guarded_source_check_is_rendered(snapshot):
    out, row = snapshot
    (out / "source_checks.json").write_text(json.dumps([source_check(row)]))
    driver.render(out)
    report = next((out / "records").rglob("*.md")).read_text()
    assert "Source-checked claim rows: 1/1" in report
    assert "Sodium chloride 1 g/L" in report


def test_scan_returns_failure_for_unreadable_record(tmp_path, monkeypatch):
    path = tmp_path / "bad.yaml"
    path.write_text("not a mapping\n")
    monkeypatch.setattr(driver, "ROOT", tmp_path)
    monkeypatch.setattr(
        driver.subprocess,
        "check_output",
        lambda cmd, **kwargs: "bad.yaml\0" if "ls-files" in cmd else "fixture\n",
    )
    out = tmp_path / "audit"
    with pytest.raises(SystemExit) as exc:
        driver.scan(out)
    assert exc.value.code != 0
    assert json.loads((out / "run.json").read_text())["status"] == "failed"


def bind_validation(out, row):
    report = out / "strict_validation.tsv"
    report.write_text("file\tmessage\n")
    marker = {
        "status": "passed",
        "exit_code": 0,
        "files_scanned": 1,
        "files_with_errors": 0,
        "error_rows": 0,
        "snapshot_sha256": driver.snapshot_sha256([row]),
        "schema_sha256": hashlib.sha256(driver.SCHEMA_PATH.read_bytes()).hexdigest(),
        "report_sha256": hashlib.sha256(report.read_bytes()).hexdigest(),
    }
    (out / "validation_complete.json").write_text(json.dumps(marker))
    return marker


def test_bound_validation_can_finalize(snapshot):
    out, row = snapshot
    bind_validation(out, row)
    driver.render(out)
    assert "0 closed-schema errors" in next((out / "records").rglob("*.md")).read_text()


@pytest.mark.parametrize(
    "field", ["files_scanned", "schema_sha256", "snapshot_sha256", "report_sha256"]
)
def test_validation_rejects_stale_binding(snapshot, field):
    out, row = snapshot
    marker = bind_validation(out, row)
    marker[field] = "stale"
    (out / "validation_complete.json").write_text(json.dumps(marker))
    with pytest.raises(ValueError, match="validation"):
        driver.render(out)
    assert not (out / "manifest.tsv").exists()


@pytest.mark.parametrize("contents", ["", "file\tmessage\nrecipe.yaml\terror\n"])
def test_bound_report_must_have_header_and_zero_errors(snapshot, contents):
    out, row = snapshot
    marker = bind_validation(out, row)
    report = out / "strict_validation.tsv"
    report.write_text(contents)
    marker["report_sha256"] = hashlib.sha256(report.read_bytes()).hexdigest()
    (out / "validation_complete.json").write_text(json.dumps(marker))
    with pytest.raises(ValueError, match="validation report"):
        driver.render(out)


@pytest.mark.parametrize(
    "mutation", ["empty", "duplicate", "parse_error", "failed_run", "wrong_count", "both_formats"]
)
def test_failed_or_ambiguous_inventory_cannot_render(snapshot, mutation):
    out, row = snapshot
    inventory = out / "inventory.jsonl"
    if mutation == "empty":
        inventory.write_text("")
    elif mutation == "duplicate":
        inventory.write_text(inventory.read_text() * 2)
    elif mutation == "parse_error":
        row["parse_error"] = "bad record"
        inventory.write_text(json.dumps(row) + "\n")
    elif mutation == "both_formats":
        (out / "inventory.jsonl.gz").touch()
    else:
        meta = json.loads((out / "run.json").read_text())
        meta["status" if mutation == "failed_run" else "records"] = "failed"
        (out / "run.json").write_text(json.dumps(meta))
    with pytest.raises(ValueError, match="inventory"):
        driver.render(out)
    assert not (out / "manifest.tsv").exists()


def test_coverage_guard_is_active_under_optimized_python(snapshot):
    out, row = snapshot
    bind_validation(out, row)
    driver.render(out)
    (out / "manifest.tsv").write_text("record\treport\tsha256\n")
    code = (
        f"import sys; sys.path.insert(0, {str(DRIVER.parent)!r}); "
        "from pathlib import Path; from verify_coverage import verify; "
        f"verify(Path({str(out)!r}), Path({str(out)!r}), {{{row['path']!r}}})"
    )
    result = subprocess.run([sys.executable, "-O", "-c", code], capture_output=True, text=True)
    assert result.returncode != 0
    assert "Record counts differ" in result.stderr


def test_successful_scan_observes_upstream(tmp_path, monkeypatch):
    (tmp_path / "recipe.yaml").write_text("id: CultureMech:000001\n")
    monkeypatch.setattr(driver, "ROOT", tmp_path)
    monkeypatch.setattr(
        driver.subprocess,
        "check_output",
        lambda cmd, **kwargs: "recipe.yaml\0" if "ls-files" in cmd else "observed-ref\n",
    )
    out = tmp_path / "audit"
    driver.scan(out)
    meta = json.loads((out / "run.json").read_text())
    assert meta["status"] == "complete"
    assert meta["upstream_main_observed"] == "observed-ref"


def test_scan_refuses_existing_compressed_inventory(tmp_path, monkeypatch):
    monkeypatch.setattr(driver.subprocess, "check_output", lambda *args, **kwargs: "")
    (tmp_path / "inventory.jsonl.gz").touch()
    with pytest.raises(SystemExit, match="overwrite"):
        driver.scan(tmp_path)
