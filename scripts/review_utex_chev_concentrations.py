"""Preview guarded, source-pinned amount evidence for the nine CHEV recipes."""

import argparse
import collections
import copy
import json
import subprocess
from decimal import Decimal
from pathlib import Path

import review_solution_concentration_evidence as runner

from culturemech.curate.curation_event import now_iso, record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261009-utex-chev"
PLAN = HERE / "plan.json"
SOURCE_SHA = "725640b44dcc4267e06ca73b608c6b56affc8f09c2581b6554b8545399d4f251"
ACTION = "CURATED_UTEX_CHEV_BATCH_INPUTS_AND_SCOPED_EVIDENCE"
KEYS = {
    "chev-diatom-medium",
    "one-half-chev-diatom-medium",
    "one-third-chev-diatom-medium",
    "one-fifth-chev-diatom-medium",
    "two-thirds-chev-diatom-medium",
    "2x-chev-diatom-medium",
    "modified-chev-medium",
    "modified-2x-chev-medium",
    "modified-2x-chev-plus-soil-medium",
}
LIMITS = [
    "L quantities are absolute input volumes per single-tube preparation, not final "
    "concentrations. Vessel capacity and summed liquid inputs do not establish final volume.",
    "The three fixed drop counts retain unresolved legacy VARIABLE encodings; their "
    "new evidence supports notes only. No drop-volume estimate is introduced.",
    "Modified CHEV's 1 mg/12 mL versus 0.5 mM source discrepancy remains unresolved. "
    "Its new evidence supports the discrepancy note, not the retained molarity.",
    "Referenced F/2 composition, chemical mappings, preparation, growth conditions and "
    "relationships are preserved, not newly certified. No new taxa-media associations.",
]


def sources():
    raw = (HERE / "source-review.json").read_bytes()
    assert runner.sha(raw) == SOURCE_SHA, "Source review drift"
    source = json.loads(raw)
    records = {r["key"]: r for r in source["records"]}
    assert len(source["records"]) == 9 and set(records) == KEYS
    assert source["manual_pdf_pages_inspected"] == 9
    return source, records


def bibliography(record):
    return {
        "reference": record["url"],
        "title": record["title"],
        "notes": "source_type=culture_collection_page; discovery_mode=existing_record_reference; "
        "accessed_on=2026-10-09; named authors and web-page publication year not stated; "
        "publisher=UTEX Culture Collection of Algae; locator=recipe table and Directions; "
        f"html_sha256={record['capture_sha256']}; corroborating PDF={record['pdf']['url']}; "
        f"pdf_sha256={record['pdf']['pdf_sha256']}; PDF page 1 visually inspected. "
        "Evidence is claim-specific; unresolved drop encodings and the Modified CHEV "
        "magnesium-carbonate discrepancy are not certified.",
    }


def check_claims(before, record):
    claims = record["claims"]
    actual = runner.all_claims(before)
    assert [c["pointer"] for c in claims] == [c["pointer"] for c in actual]
    for claim in claims:
        node = runner.get_node(before, claim["pointer"])
        row = record["table"][claim["row_index"]]
        assert node["preferred_term"] == claim["ingredient"]
        assert node["concentration"] == claim["old"]
        assert node.get("notes") == claim["old_notes"]
        assert claim["evidence"]["reference"] == record["url"]
        assert claim["evidence"]["snippet"] in row
        if claim["status"] == "correct":
            amount, unit = row[2].split()
            assert unit in {"cc", "mL"}
            assert claim["new"] == {
                "value": format(Decimal(amount) / 1000, "f"),
                "unit": "L",
            }
            assert "per tube" in claim["new_notes"]
            assert "not a concentration" in claim["new_notes"]
        else:
            assert claim["new"] == claim["old"]
            if claim["status"] in {"conflict", "schema_gap"}:
                assert claim["evidence_scope"].startswith("notes only;")
            elif claim["status"] == "evidence_only":
                if record["key"] == "modified-2x-chev-medium":
                    assert "For 1 L Total" in record["prose_candidates"]
                    assert claim["new"] == {
                        "value": row[2].split()[0],
                        "unit": "ML_PER_L",
                    }
                else:
                    assert row[4] == "0.5 mM" and row[2] == "0.5 mg/12 mL"
                    assert claim["new"] == {"value": "0.5", "unit": "MILLIMOLAR"}
            else:
                raise AssertionError("Unreviewed claim status")


def event(before, record, timestamp):
    doc = copy.deepcopy(before)
    record_curation_event(
        doc,
        curator="codex",
        action=ACTION,
        source=record["url"],
        timestamp=timestamp,
        notes=" ".join(LIMITS),
        changes=json.dumps(
            [
                {
                    k: c[k]
                    for k in ("pointer", "ingredient", "old", "new", "status", "evidence_scope")
                }
                for c in record["claims"]
            ],
            sort_keys=True,
        ),
    )
    return doc["curation_history"][-1]


def transform(before, record, timestamp):
    check_claims(before, record)
    after = copy.deepcopy(before)
    for claim in record["claims"]:
        node = runner.get_node(after, claim["pointer"])
        node["concentration"] = copy.deepcopy(claim["new"])
        node["notes"] = claim["new_notes"]
        owner = runner.get_node(after, claim["evidence_pointer"])
        assert record["url"] not in {e["reference"] for e in owner.get("evidence", [])}
        owner.setdefault("evidence", []).append(copy.deepcopy(claim["evidence"]))
    indexes = [i for i, r in enumerate(after["references"]) if r["reference"] == record["url"]]
    assert len(indexes) == 1
    assert after["references"][indexes[0]] == {"reference": record["url"]}
    after["references"][indexes[0]] = bibliography(record)
    after["curation_history"].append(event(before, record, timestamp))
    return after


def check(before, after, item):
    _, records = sources()
    record = records[item["key"]]
    assert item["action"] == ACTION and item["target_class"] == "MediaRecipe"
    assert item["path"] == record["path"] and item["unresolved"] == LIMITS
    assert item["id"] == before["id"] == after["id"] == record["id"]
    assert item["before_text"] == record["before_text"]
    assert (
        runner.sha(item["before_text"].encode()) == item["before_sha256"] == record["before_sha256"]
    )
    assert runner.sha(item["after_text"].encode()) == item["after_sha256"]
    assert before == runner.load_yaml(item["before_text"])
    assert after == runner.load_yaml(item["after_text"])
    assert before["media_term"]["term"]["id"] == record["source_term"]
    assert item["claims"] == record["claims"], "Unreviewed claim change"
    check_claims(before, record)
    reverted = copy.deepcopy(after)
    for claim in record["claims"]:
        node = runner.get_node(reverted, claim["pointer"])
        old_node = runner.get_node(before, claim["pointer"])
        assert node["concentration"] == claim["new"], "Unreviewed quantity change"
        assert node["notes"] == claim["new_notes"], "Unreviewed note change"
        node["concentration"] = copy.deepcopy(claim["old"])
        node["notes"] = claim["old_notes"]
        owner = runner.get_node(reverted, claim["evidence_pointer"])
        old_owner = runner.get_node(before, claim["evidence_pointer"])
        assert owner["evidence"] == old_owner.get("evidence", []) + [claim["evidence"]]
        if "evidence" in old_owner:
            owner["evidence"] = copy.deepcopy(old_owner["evidence"])
        else:
            owner.pop("evidence")
        assert node == old_node, "Unreviewed ingredient or solution change"
    for i, old in enumerate(before["references"]):
        expected = bibliography(record) if old["reference"] == record["url"] else old
        assert reverted["references"][i] == expected, "Unreviewed bibliography change"
    assert len(reverted["references"]) == len(before["references"])
    reverted["references"] = copy.deepcopy(before["references"])
    added = reverted["curation_history"].pop()
    assert added == event(before, record, added["timestamp"]), "Unreviewed event change"
    assert reverted == before, "Unreviewed root change"
    return collections.Counter(
        new_evidence=len(record["claims"]),
        new_curation_history=1,
        bibliographic_entries_enriched=1,
        quantity_corrections=sum(c["old"] != c["new"] for c in record["claims"]),
        ingredient_context_notes_corrected=sum(
            c["old_notes"] != c["new_notes"] for c in record["claims"]
        ),
    )


def preview(root=ROOT):
    _, records = sources()
    plan = {
        "version": 1,
        "action": ACTION,
        "source_sha256": SOURCE_SHA,
        "created_at": now_iso(),
        "commit": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=root, text=True
        ).strip(),
        "records": [],
    }
    for key, record in records.items():
        raw = (root / record["path"]).read_bytes()
        assert runner.sha(raw) == record["before_sha256"], "Record drift"
        before = runner.load_yaml(raw)
        assert not validate_recipe(before, target_class="MediaRecipe")
        after = transform(before, record, plan["created_at"])
        assert not validate_recipe(after, target_class="MediaRecipe")
        output = runner.render(raw.decode(), after)
        item = {
            "key": key,
            "id": record["id"],
            "path": record["path"],
            "target_class": "MediaRecipe",
            "action": ACTION,
            "before_text": raw.decode(),
            "after_text": output.decode(),
            "before_sha256": runner.sha(raw),
            "after_sha256": runner.sha(output),
            "claims": record["claims"],
            "unresolved": LIMITS,
        }
        item["counts"] = dict(check(before, after, item))
        plan["records"].append(item)
    runner.safe_targets(root, plan)
    return plan


def safe_path(root, path):
    target = root / path
    parts = Path(path).parts
    assert target.resolve().is_relative_to(root / "data/normalized_yaml")
    assert not any(root.joinpath(*parts[:i]).is_symlink() for i in range(1, len(parts) + 1))
    return target


def apply(plan, root=ROOT, *, verify=False):
    root = root.resolve()
    assert plan["version"] == 1, "Unsupported plan version"
    assert plan["action"] == ACTION and plan["source_sha256"] == SOURCE_SHA
    assert len(plan["records"]) == 9 and {r["key"] for r in plan["records"]} == KEYS
    runner.safe_targets(root, plan)
    pending = []
    for item in plan["records"]:
        before, after = (runner.load_yaml(item[k]) for k in ("before_text", "after_text"))
        assert dict(check(before, after, item)) == item["counts"]
        assert not validate_recipe(after, target_class="MediaRecipe")
        target = safe_path(root, item["path"])
        raw = target.read_bytes()
        if runner.sha(raw) == item["after_sha256"]:
            continue
        assert not verify and runner.sha(raw) == item["before_sha256"], "Concurrent record edit"
        pending.append((target, raw, item["after_text"].encode()))
    for target, before, _ in pending:
        safe_path(root, target.relative_to(root))
        assert target.read_bytes() == before, "Concurrent edit during preflight"
    for target, before, after in pending:
        safe_path(root, target.relative_to(root))
        assert target.read_bytes() == before, "Concurrent edit during write"
        target.write_bytes(after)
        assert target.read_bytes() == after
    return {"changed": len(pending), "already_applied": 9 - len(pending)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=PLAN)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--verify", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.apply or args.verify:
        print(json.dumps(apply(json.loads(args.plan.read_text()), verify=args.verify)))
    else:
        assert not args.plan.exists(), "Refuse to overwrite preview"
        plan = preview()
        with args.plan.open("x") as stream:
            stream.write(json.dumps(plan, indent=2) + "\n")
        print(json.dumps({"reviewed": 9, "claim_rows": 34, "records_edited": 0}))


if __name__ == "__main__":
    main()
