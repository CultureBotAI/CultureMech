#!/usr/bin/env python3
"""Record bounded root55/UTEX quotation-repair review, 2026-11-16, #683/#763.

Inputs: frozen proposals, prior independent review and primary captures.
Output: native inspection and new review draft; no recipe or proposal writes.
Root authored the scientific payload, another agent repaired evidence excerpts;
this is explicitly a self-review supplement to the independent claim review.
"""

import argparse
import copy
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml
from review_variant_family_proposals_683 import targets

ROOT = Path(__file__).resolve().parents[2]
OLD = "reviews/structured/20261116T212755Z-root55-utex-independent-claims/review.yaml"
PINS = {
    "remaining-families-683.json": "575937e6b9739016d8b43f48ea23efba290d69a3445c311bc95223991cc18049",
    "utex-optional-683.json": "053b2ac82a0c3681d84f53714b129366f2e7b2f9f2d8da1acc6b72c471491e88",
}


def scientific_payload(value):
    result = copy.deepcopy(value)
    for record in result["records"]:
        for variant in record["variants"]:
            for change in variant["ingredient_changes"]:
                for evidence in change["evidence"]:
                    evidence.pop("snippet", None)
                    evidence.pop("explanation", None)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", type=Path, required=True)
    args = parser.parse_args()
    directory = args.output_directory.resolve()
    directory.mkdir(parents=True, exist_ok=False)
    prior = yaml.safe_load((ROOT / OLD).read_text())
    selected = []
    inputs = [OLD]
    for name, expected in PINS.items():
        path = "conf/variant_ingredient_curation/" + name
        raw = (ROOT / path).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == expected
        after = json.loads(raw)
        before = json.loads(
            subprocess.check_output(["git", "show", "93d23e4415:" + path], cwd=ROOT)
        )
        assert scientific_payload(before) == scientific_payload(after)
        selected.extend(targets(after))
        inputs.append(path)
        for record in after["records"]:
            assert (
                hashlib.sha256((ROOT / record["path"]).read_bytes()).hexdigest()
                == record["expected_sha256"]
            )
    target_file = directory / "targets.yaml"
    target_file.write_text(yaml.safe_dump({"targets": selected}, sort_keys=False))
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(target_file.relative_to(ROOT)),
    ]
    for path in inputs:
        command.extend(["--input", path])
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True, check=True)
    (directory / "inspection.json").write_text(result.stdout)
    inspection = json.loads(result.stdout)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    review_id = now.replace("-", "").replace(":", "") + "-root55-utex-quantity-repair"
    ids = [target["target_id"] for target in selected]
    summary = "Reviewed all changed excerpts against the already inspected primary sources: Mattanovich XLS exact cells and stock/header bases; DSMZ645 table amounts; DSMZ670 strain-specific quantities and titrant strengths; Villasenor final vitamin/hydrate amounts; Nordkvist distinct timed and initial acetate treatments; UTEX optional agar/batch directions. The evidence repair adds exact quantity and separately located basis excerpts without changing scientific payload or source coordinates."
    review = {
        "schema_version": "1.0.0",
        "review_id": review_id,
        "kind": "batch",
        "repository": "CultureBotAI/CultureMech",
        "title": "Follow-up review of root55 and UTEX quantitative evidence repairs",
        "started_at": now,
        "finished_at": now,
        "reviewer": {
            "identity": "codex-root-quantity-repair-reviewer",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "Root authored original scientific payload; another agent authored this evidence-only repair. This bounded follow-up does not replace the prior independent scientific review, retained and pinned as an input.",
        },
        "skill": "review-ingredient-concentrations; curate-yaml-record",
        "completion": "completed",
        "verdict": "pass_with_limitations",
        "scientific_review": True,
        "native_verdict": "Issue763 evidence finding is addressed for these95 unchanged events; prior independent claim review remains applicable to the unchanged scientific payload.",
        "summary": summary,
        "source": inspection["source"],
        "scope": {
            "description": "Evidence-only corrections in24 recipes/95 events; original independent review retained.",
            "selection": "Two exact proposal hashes in the retained helper and checkpoint93d23e originals.",
            "coverage": "partial",
            "population_size": 24,
            "reviewed_target_ids": ids,
            "exclusions": [
                {
                    "target": "Whole-record scientific certification and held rows",
                    "reason": "Bounded follow-up of accepted events' excerpts only.",
                }
            ],
        },
        "targets": selected,
        "checks": [
            {
                "check_id": "repair-scope",
                "name": "Only excerpts and explanation fields changed",
                "status": "passed",
                "required": True,
                "summary": "Compared against committed checkpoint; identities, actions, doses, stages, exact source text and dispositions unchanged.",
                "target_ids": ids,
            },
            {
                "check_id": "source-reading",
                "name": "Manual source comparison of repaired excerpts",
                "status": "passed",
                "required": True,
                "summary": summary,
                "target_ids": ids,
                "evidence_ids": [e["evidence_id"] for e in prior["evidence"]],
            },
        ],
        "evidence": prior["evidence"],
        "assessments": [
            {
                "assessment_id": "quantity-excerpts",
                "area": "scope",
                "topic": "Exact quantity/unit/basis support",
                "outcome": "supported",
                "summary": summary,
                "target_ids": ids,
                "evidence_ids": [e["evidence_id"] for e in prior["evidence"]],
            }
        ],
        "findings": [],
        "actions": [],
        "limitations": [
            "Self-review follow-up; initial scientific review by another agent is separately preserved.",
            "No whole-recipe approval, unsupported dose conversion, universal base membership or held-claim clearance.",
            "Native application, whole-catalog audit and MIM adoption remain separate gates.",
        ],
        "links": [
            "https://github.com/CultureBotAI/CultureMech/issues/763",
            "https://github.com/CultureBotAI/CultureMech/pull/764",
        ],
    }
    (directory / "review.yaml").write_text(
        yaml.safe_dump(json.loads(json.dumps(review)), sort_keys=False, allow_unicode=True)
    )
    print(
        json.dumps(
            {"review_id": review_id, "review": str((directory / "review.yaml").relative_to(ROOT))}
        )
    )


if __name__ == "__main__":
    main()
