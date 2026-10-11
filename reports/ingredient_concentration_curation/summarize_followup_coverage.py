"""Inventory current follow-up coverage; report presence is not scientific verification."""

import argparse
import collections
import datetime
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
REPORTS = ROOT / "reports/ingredient_concentration_curation"
DRIVER = ROOT / "reports/ingredient_concentration_review/20261005T175229Z/review_driver.py"
sys.path.insert(0, str(ROOT / "scripts"))
from review_solution_concentration_evidence import followup_result_hash  # noqa: E402


def report_inventory(tracked, reports=REPORTS):
    """Count canonical reports; retain explicitly marked previews as separate evidence."""
    reviewed, previews = set(), []
    for path in sorted(reports.rglob("*.md")):
        raw = path.read_bytes()
        lines = raw.decode().splitlines()
        targets = [
            line.removeprefix("- Record: ") for line in lines if line.startswith("- Record:")
        ]
        if not targets:
            continue
        assert len(targets) == 1 and targets[0] in tracked, str(path)
        if any(line.lower().startswith("- state: preview") for line in lines):
            previews.append(
                {
                    "report": str(path.relative_to(ROOT) if path.is_relative_to(ROOT) else path),
                    "target": targets[0],
                    "sha256": hashlib.sha256(raw).hexdigest(),
                }
            )
            continue
        assert targets[0] not in reviewed, str(path)
        reviewed.add(targets[0])
    return reviewed, previews


def summarize(followup_plans=()):
    if Path.cwd() != ROOT:
        raise ValueError("Run from the repository root")
    spec = importlib.util.spec_from_file_location("concentration_review_inventory", DRIVER)
    driver = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(driver)
    tracked = {
        p
        for p in subprocess.check_output(
            ["git", "ls-files", "-z", "data/normalized_yaml"], cwd=ROOT
        )
        .decode()
        .split("\0")
        if p.endswith(".yaml")
    }
    successors = [r for p in followup_plans for r in json.loads(p.read_text())["records"]]
    for record in successors:
        assert record["path"] in tracked, record["path"]
        expected, _ = followup_result_hash(record, successors)
        assert hashlib.sha256((ROOT / record["path"]).read_bytes()).hexdigest() == expected
    reviewed, previews = report_inventory(tracked)
    source_plans = (
        sorted(REPORTS.glob("20261007-mediadive-solutions-*/plan.json"))
        + sorted(REPORTS.glob("20261007-mediadive-media-*/plan.json"))
        + sorted(REPORTS.glob("20261007-komodo-media-*/plan.json"))
    )
    for path in source_plans:
        for record in json.loads(path.read_text())["records"]:
            assert not record["failure"], record["path"]
            expected, _ = followup_result_hash(record, successors)
            assert hashlib.sha256((ROOT / record["path"]).read_bytes()).hexdigest() == expected
    pending = []
    prefixes = collections.Counter()
    kinds = collections.Counter()
    for relative in sorted(tracked - reviewed):
        raw = (ROOT / relative).read_bytes()
        doc = yaml.load(raw, Loader=yaml.CSafeLoader)
        claims, _ = driver.collect_claims(doc)
        source = ((doc.get("media_term") or {}).get("term") or {}).get("id")
        if source is None:
            source = (doc.get("term") or {}).get("id")
        prefix = source.split(":", 1)[0] if isinstance(source, str) else "UNSPECIFIED"
        prefixes[prefix] += 1
        claim_kinds = collections.Counter(c["kind"] for c in claims)
        kinds.update(claim_kinds)
        pending.append(
            {
                "path": relative,
                "id": doc["id"],
                "sha256": hashlib.sha256(raw).hexdigest(),
                "source_term": source,
                "claim_rows": len(claims),
                "claim_kinds": dict(claim_kinds),
                "evidence_states": dict(collections.Counter(c["evidence_state"] for c in claims)),
            }
        )
    assert len(reviewed) + len(pending) == len(tracked)
    return {
        "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT).decode().strip(),
        "scope_note": "Exact tracked normalized paths outside reports/ingredient_concentration_curation; "
        "not a claim that those records have never been reviewed. Follow-up report presence does not "
        "mean all claims are verified. Evidence-state counts are structural candidates, not source checks. "
        "Source prefixes are literal identifiers, not inferred collection equivalences.",
        "tracked_normalized_records": len(tracked),
        "followup_unique_records": len(reviewed),
        "excluded_preview_reports": previews,
        "outside_this_followup": len(pending),
        "explicit_followup_plans": [
            str(p.relative_to(ROOT) if p.is_absolute() else p) for p in followup_plans
        ],
        "pending_source_prefixes": dict(prefixes),
        "pending_claim_kinds": dict(kinds),
        "pending_records": pending,
    }


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, required=True)
    parser.add_argument("--followup-plan", type=Path, action="append", default=[])
    args = parser.parse_args()
    if args.out.exists():
        raise ValueError("Refuse to overwrite a coverage snapshot")
    result = summarize(args.followup_plan)
    args.out.write_text(json.dumps(result, indent=2) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "pending_records"}, indent=2))
