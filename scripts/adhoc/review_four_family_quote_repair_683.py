#!/usr/bin/env python3
"""Package independent #763/#766 follow-up evidence (2026-11-16).

Inputs: original immutable review, frozen repaired proposal, native inspection.
Output: new native review content; no recipe/proposal/previous-review writes.
Source readings are manual; this helper checks quote-only scope and family IDs.
"""

import argparse
import copy
import datetime
import hashlib
import json
from pathlib import Path

import yaml
from verify_variant_quote_repair_683 import without_quotations

ROOT = Path(__file__).resolve().parents[2]
OLD = "786ae063209accd3c3ad1e67bd2043e0ff0a4e94703e6b5d8a55b0d073d1b32c"
NEW = "311cb0ca79971c03b8a2a334da32709c3be1315c8cf63cb1dc51b31f85200317"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def family(path):
    stem = Path(path).stem
    if "AMS1" in stem or stem.startswith("ams1"):
        return "carini"
    if stem.startswith("bl_medium"):
        return "jensen"
    if "tang_et_al" in stem:
        return "tang"
    if stem.startswith("modified_m1"):
        return "pinchuk"
    raise ValueError("unrecognized family: " + path)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--before", type=Path, required=True)
    parser.add_argument("--after", type=Path, required=True)
    parser.add_argument("--prior-review", type=Path, required=True)
    parser.add_argument("--inspection", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    before_raw, after_raw = args.before.read_bytes(), args.after.read_bytes()
    if (
        hashlib.sha256(before_raw).hexdigest() != OLD
        or hashlib.sha256(after_raw).hexdigest() != NEW
    ):
        raise ValueError("candidate hash mismatch")
    before, after = json.loads(before_raw), json.loads(after_raw)
    if without_quotations(before) != without_quotations(after):
        raise ValueError("non-quotation change")
    result = yaml.safe_load(args.prior_review.read_text())
    prior_id = result["review_id"]
    inspection = json.loads(args.inspection.read_text())
    source = copy.deepcopy(inspection["source"])
    if not any(item["sha256"] == NEW for item in source["inputs"]):
        raise ValueError("native inspection does not bind candidate")
    for item in source["inputs"]:
        if hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest() != item["sha256"]:
            raise ValueError("native inspected input changed")
    for item in result["source"]["inputs"]:
        if item["role"] == "independently inspected primary source":
            if hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest() != item["sha256"]:
                raise ValueError("primary source changed")
            source["inputs"].append(item)
    families = {name: [] for name in ("carini", "jensen", "pinchuk", "tang")}
    for record in after["records"]:
        families[family(record["path"])].append(record["recipe_id"])
    if {k: len(v) for k, v in families.items()} != {
        "carini": 8,
        "jensen": 5,
        "pinchuk": 4,
        "tang": 4,
    }:
        raise ValueError("family membership mismatch")
    now = datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0)
    timestamp = now.isoformat().replace("+00:00", "Z")
    result.update(
        review_id=now.strftime("%Y%m%dT%H%M%SZ") + "-four-family-quote-followup",
        title="Independent quotation repair follow-up",
        started_at=timestamp,
        finished_at=timestamp,
        verdict="pass_with_limitations",
        native_verdict="Exact frozen182-assertion proposal cleared for guarded application; existing held claims remain held.",
        summary="Nine quantified evidence items now preserve literal amounts and bases. Scientific payload,98dispositions and all source bindings are unchanged. Prior family target associations were separately confirmed correct; the alleged mismatch was a rejected false positive. No whole-record/human/release certification.",
        source=source,
    )
    result["reviewer"][
        "independence_basis"
    ] = "This reviewer authored neither proposal nor quotation repair and changed no recipes. Independently reread the9changed evidence items against Tang source page4 and Jensen primary PDF page4363, confirmed quote-only change, and mapped family IDs from exact recipe paths. The prior review is retained unchanged."
    result["scope"]["selection"] = (
        "Frozen repaired proposal SHA256" + NEW + "; previous review " + prior_id
    )
    for evidence in result["evidence"]:
        if evidence["evidence_id"] == "proposal":
            evidence.update(
                snapshot_sha256=NEW,
                accessed_at=timestamp,
                support="supports",
                summary="Exact repaired proposal; only quotation/explanation fields differ from the independently reviewed original.",
            )
        elif evidence["evidence_id"] == "tang-2009":
            evidence["summary"] = (
                "Rechecked Methods p.4:30mM labeled sodium L-lactate, separate20mM PIPES. Repaired snippet and separate isotope quotation preserve substrate/dose context."
            )
            evidence["accessed_at"] = timestamp
        elif evidence["evidence_id"] == "jensen":
            evidence["summary"] = (
                "Fresh primary PDF read confirms calcium-salt identity in formulation paragraph and2micromolar pantothenate in Table1 footnote b. Repair quotes the pantothenate basis without asserting calcium-salt molarity; typography normalization explicit, no local source hash claimed."
            )
            evidence["accessed_at"] = timestamp
    for assessment in result["assessments"]:
        key = assessment["assessment_id"]
        if key in families:
            if assessment["target_ids"] != families[key]:
                raise ValueError("prior family association differs")
            assessment["summary"] = (
                "Prior scientific assessment retained for unchanged assertions; explicit filename-based membership independently confirms the prior target associations. Quantified quotation repair is now independently verified; held forms/stocks/mixtures remain excluded."
            )
    quote = result["findings"][0]
    quote.update(
        status="resolved",
        target_ids=families["jensen"] + families["tang"],
        description="Four Tang items now quote30mM medium and separately identify isotope-labeled sodium L-lactate. Five Jensen items add the exact2micromolar pantothenate-basis excerpt. Independent primary-source rereading confirms the repair with unchanged scientific payload.",
        disposition_reason="Nine source-grounded repairs inspected on the exact frozen candidate; unchanged scientific payload verified.",
        previous_occurrences=[
            {
                "repository": "CultureBotAI/CultureMech",
                "review_id": prior_id,
                "finding_id": "quantified-quotes",
            }
        ],
    )
    quote["ownership_note"] = (
        "This finding is resolved for the exact repaired proposal; parent issue763 also covers other cohorts."
    )
    result["assessments"].append(
        {
            "assessment_id": "family-target-associations",
            "area": "provenance",
            "outcome": "supported",
            "topic": "Rejected allegation of incorrect Tang/Pinchuk target associations",
            "summary": "Reviewer initially inferred family order from the native inspector's sorted source inputs rather than the saved review's target order. Inspection of actual saved assessment and finding IDs confirmed correct associations. Explicit filename mapping here reproduces those same IDs. Original review remains untouched. Issue766 was a false positive and is closed as not planned; no scientific or review data repair needed.",
            "target_ids": families["pinchuk"] + families["tang"],
            "evidence_ids": ["proposal"],
        }
    )
    result["actions"] = []
    result["checks"] = [
        {
            "check_id": "followup-snapshot",
            "name": "Native inspection and quotation-only comparison",
            "status": "passed",
            "required": True,
            "summary": "Exact candidate/prior review/targets bound by fresh native inspection; source captures rehashed; comparison excludes only snippet/explanation and all other fields match. Explicit filename membership is8Carini,5Jensen,4Pinchuk,4Tang.",
            "target_ids": [target["target_id"] for target in result["targets"]],
            "evidence_ids": ["proposal"],
            "command": "record_review.py inspect; review_four_family_quote_repair_683.py",
            "exit_code": 0,
            "expected_exit_code": 0,
        }
    ]
    result["links"] = [
        "https://github.com/CultureBotAI/CultureMech/issues/763",
        "https://github.com/CultureBotAI/CultureMech/issues/766",
    ]
    result["limitations"].append(
        "This follow-up resolves the quote finding for this proposal and rejects the association allegation; it does not close global issue763 or authorize merge/release."
    )
    with args.output.open("x", encoding="utf-8") as stream:
        yaml.dump(result, stream, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True)
    print(
        json.dumps(
            {
                "review_id": result["review_id"],
                "candidate_sha256": NEW,
                "families": families,
                "output": str(args.output),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
