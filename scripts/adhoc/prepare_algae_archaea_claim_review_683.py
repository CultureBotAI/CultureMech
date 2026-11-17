#!/usr/bin/env python3
"""Package the manual claim review of the 96-row proposal (2026-11-16, #683).

Inputs: the frozen decision JSON and native inspect result; primary captures.
Output: native review content for record_review.py validate/save. No recipe edits.
Packaging only: scientific decisions were manually made in the proposal builder.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--decision", type=Path, required=True)
    parser.add_argument("--inspection", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    decision = json.loads(args.decision.read_text())
    inspection = json.loads(args.inspection.read_text())
    observed = "2026-11-16T21:20:22Z"
    targets = inspection["targets"]
    for target in targets:
        target["owner_paths"] = [
            {
                "repository": "CultureBotAI/CultureMech",
                "path": target["path"],
                "role": "authoritative normalized recipe",
            }
        ]
    ids = [target["target_id"] for target in targets]
    owners = {target["target_id"]: target["owner_paths"] for target in targets}
    source = inspection["source"]
    proposal_hash = hashlib.sha256(args.decision.read_bytes()).hexdigest()
    if proposal_hash != "b326ba81ebf38479e5d2e5b550a89bfa7c1d649edaf46603de7df3fbb14dcf5d":
        raise ValueError("review belongs to a different frozen proposal")
    evidence = [
        {
            "evidence_id": "proposal",
            "kind": "record_content",
            "reference": str(args.decision),
            "accessed_at": observed,
            "support": "partial",
            "snapshot_sha256": proposal_hash,
            "summary": "All96assigned rows accounted, including37rows with52proposed assertions,29context-only,2already represented and28held. Mixed rows retain held portions explicitly; not96approved ingredient rows.",
        }
    ]
    evidence_by_ref = {}
    for item in decision["source_inspections"]:
        digest = hashlib.sha256((ROOT / item["path"]).read_bytes()).hexdigest()
        if digest != item["sha256"]:
            raise ValueError("primary source drift:" + item["path"])
        source["inputs"].append(
            {"path": item["path"], "sha256": digest, "role": item["access_scope"]}
        )
        evidence.append(
            {
                "evidence_id": item["key"],
                "kind": "primary_source",
                "reference": item["reference"],
                "locator": item["locator"],
                "accessed_at": observed,
                "support": "partial",
                "summary": "Inspected for the limited claim(s) and exclusions stated in the proposal; "
                + item["access_scope"]
                + ". Does not establish full parent-formulation equivalence.",
                "snapshot_sha256": digest,
            }
        )
        evidence_by_ref[item["reference"]] = item["key"]
    for folder, file, name, description in [
        (
            "ccap-ajs",
            "source.pdf",
            "ajs-parent",
            "CCAP AJS page1 specifies concentrated sulfuric acid; used only as the old side of the study acid replacement.",
        ),
        (
            "tap-coculture-2024",
            "source.xml",
            "tap-context",
            "Methods2.3/2.4 gives TAP ammonium chloride and acetic acid context; not a new supplement in the queue row.",
        ),
        (
            "hemiaulus-2020",
            "source.xml",
            "hemiaulus-context",
            "Methods distinguishes modified fixed-N-free YBCII and naturally dissolved N2; no specific nitrogen-removal or added-gas assertion promoted.",
        ),
        (
            "sakai-2017",
            "metadata.json",
            "sakai-limit",
            "Primary abstract describes aerobic sulfur-inhibited organism; fullMethods not inspected, so the anaerobic variant's formula linkage remains held.",
        ),
    ]:
        path = ".temp/variant-683/sources/" + folder + "/" + file
        digest = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
        source["inputs"].append(
            {"path": path, "sha256": digest, "role": "bounded counterevidence/context"}
        )
        evidence.append(
            {
                "evidence_id": name,
                "kind": "primary_source",
                "reference": path,
                "accessed_at": observed,
                "support": "context_only",
                "summary": description,
                "snapshot_sha256": digest,
            }
        )
    claims = {}
    for record in decision["records"]:
        for variant in record["variants"]:
            for change in variant["ingredient_changes"]:
                key = (
                    record["recipe_id"],
                    variant["variant_index"],
                    change["source_modification_index"],
                )
                claims.setdefault(key, []).append(change)
    assessments = []
    for row in decision["dispositions"]:
        key = (row["recipe_id"], row["variant_index"], row["modification_index"])
        references = {
            item["reference"] for claim in claims.get(key, []) for item in claim["evidence"]
        }
        linked = [evidence_by_ref[ref] for ref in sorted(references)]
        outcome = "unknown" if row["status"].startswith("HELD_") else "supported"
        assessments.append(
            {
                "assessment_id": f"queue-{row['queue_row_number']}",
                "area": "scope",
                "topic": f"Queue row {row['queue_row_number']}: {row['status']}",
                "outcome": outcome,
                "summary": row["reason"],
                "target_ids": [row["recipe_id"]],
                "evidence_ids": ["proposal"] + linked,
                "details": "Exact preserved modification: " + row["source_text"],
            }
        )
    findings = []
    actions = []
    for number, target, field, key, issue, title, description in [
        (
            8,
            "CultureMech:000038",
            "variants[1].modifications[0]",
            "tsuji",
            759,
            "Selenite dose conflicts with primary TableS1",
            "Existing10nM conflicts with source0.001micromolar=1nM. Source also specifies sodium metasilicate nonahydrate. The row is held; no incorrect assertion proposed.",
        ),
        (
            110,
            "CultureMech:009226",
            "variants[0].modifications[3]",
            "willard",
            762,
            "Acid alternative not supported by cited aerobic formulation",
            "Source specifies concentrated HCl, whereas existing prose permits H2SO4 or HCl. The row is held; parent acid is not automatically a study-variant acid.",
        ),
    ]:
        fid = f"row-{number}-source-conflict"
        findings.append(
            {
                "finding_id": fid,
                "issue_key": f"culturemech-{issue}",
                "category": "evidence",
                "severity": "major",
                "status": "open",
                "certainty": "confirmed",
                "title": title,
                "description": description,
                "target_ids": [target],
                "field_paths": [field],
                "evidence_ids": ["proposal", key],
                "owner_paths": owners[target],
                "external_issues": [f"https://github.com/CultureBotAI/CultureMech/issues/{issue}"],
            }
        )
        actions.append(
            {
                "action_id": f"resolve-{number}",
                "description": "Correct only source-supported prose in a separately reviewed change; regenerate the exact text/hash binding before admission.",
                "finding_ids": [fid],
                "target_ids": [target],
                "owner_paths": owners[target],
                "acceptance_checks": [
                    "Inspect primary source in full relevant context; preserve stage/form/dose limits.",
                    "Append actual curation history and obtain independent review.",
                    "Rebind queue occurrence; held row is not silently treated as reviewed.",
                ],
            }
        )
    review = {
        "schema_version": "1.0.0",
        "review_id": "20261116T212022Z-algae-archaea-variant-claims",
        "kind": "batch",
        "repository": "CultureBotAI/CultureMech",
        "title": "Author claim review and complete disposition of96algal/archaeal variant rows",
        "started_at": "2026-11-16T21:12:16Z",
        "finished_at": observed,
        "reviewer": {
            "identity": "codex-source-curator",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "This agent authored the proposed assertions after reading primary sources. This record documents source reasoning and holds, not independent review; a separate reviewer must assess the proposal.",
        },
        "skill": "curate-yaml-record; review-ingredient-concentrations",
        "completion": "completed",
        "verdict": "needs_curation",
        "native_verdict": "52bounded assertions are proposed for independent review;96row curation is not fully cleared because source conflicts and explicit evidence/model holds remain.",
        "scientific_review": True,
        "summary": "The proposal preserves every assigned row and scopes supported assertions to primary-source preparation/experiment context. Two confirmed pre-existing source conflicts are filed and held. No recipe was changed and no whole-record, human REVIEWED or release status is granted.",
        "source": source,
        "scope": {
            "description": "Claim-level review of96literal queue rows across17recipes, including52proposed assertions and explicit holds. Read assigned variants/source passages and relevant parent context; not a complete scientific review of all17records.",
            "selection": "algae_remaining52 and archaea_remaining44 in the pinned396-row inventory",
            "coverage": "partial",
            "population_size": 17,
            "reviewed_target_ids": ids,
            "exclusions": [
                {
                    "target": "Other parent ingredients, quantities, taxonomy, growth claims and historical curation",
                    "reason": "Not recertified by this claim-level pass.",
                },
                {
                    "target": "Other300queue rows and MIM/KGM release",
                    "reason": "Separate curators and downstream review; no integration acceptance claimed.",
                },
            ],
        },
        "targets": targets,
        "checks": [
            {
                "check_id": "native-inspection",
                "name": "Native recipe and proposal snapshot",
                "status": "passed",
                "required": True,
                "summary": "record_review.py inspect captured17target hashes, decision, schema and builder; primary capture hashes separately verified against receipts.",
                "target_ids": ids,
                "command": ".venv/bin/python scripts/record_review.py inspect --targets .temp/variant-683/algae-archaea-targets.yaml --input conf/variant_ingredient_curation/algae-archaea-683.json --input src/culturemech/schema/culturemech.yaml --input scripts/adhoc/prepare_algae_archaea_variant_decisions_683.py",
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": ["proposal"],
            },
            {
                "check_id": "application",
                "name": "Guarded application and downstream export",
                "status": "not_applicable",
                "required": False,
                "target_ids": ids,
                "summary": "Pre-application review only; no recipe/application/export tests were run by this reviewer.",
            },
        ],
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": actions,
        "limitations": [
            "Authored decisions require independent review; this self-review does not replace it.",
            "28rows remain wholly held, and several structured rows retain explicitly held portions.96dispositions do not mean96scientifically approved rows.",
            "Ingredient identity is kept literal or mixture-level without new ontology IDs; gases, unresolved stocks and alternative recipe scopes are not forced into positive liquid occurrences.",
            "Some support is primary abstract only; exact scope is recorded. Formulation equality, unreported doses/forms and all parent claims remain unresolved.",
            "No recipe mutation, human REVIEWED status, MIM admission, KGM rebuild or integrated release approval is granted.",
        ],
        "links": [
            "https://github.com/CultureBotAI/CultureMech/issues/759",
            "https://github.com/CultureBotAI/CultureMech/issues/762",
        ],
    }
    with args.output.open("x") as stream:
        yaml.dump(review, stream, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True)
    print(
        json.dumps(
            {
                "review_content": str(args.output),
                "targets": len(targets),
                "assessments": len(assessments),
                "findings": len(findings),
            }
        )
    )


if __name__ == "__main__":
    main()
