#!/usr/bin/env python3
"""Package the author's bounded source-family review (#683, 2026-11-16).

Inputs: explicit proposal JSON, native target inspection, native preview receipt.
Outputs: new native target file or author-review draft for the repository saver.
Scientific judgments are the explicit row dispositions and scoped claims authored
after primary-source inspection, not an automatic scientific approval by this tool.
"""

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def targets(proposal):
    return [
        {
            "target_id": record["recipe_id"],
            "path": record["path"],
            "label": record["variants"][0]["variant_name"],
            "kind": "maintained",
            "record_class": "MediaRecipe",
            "selector": "Existing inline variant modification rows and proposed ingredient_changes only",
            "owner_paths": [
                {
                    "repository": "CultureBotAI/CultureMech",
                    "path": record["path"],
                    "role": "authoritative normalized recipe",
                }
            ],
        }
        for record in proposal["records"]
    ]


def draft(proposal, proposal_path, inspection_path, preview_path, review_id, started_at):
    inspection = json.loads(inspection_path.read_text())
    preview = json.loads(preview_path.read_text())
    if preview["mode"] != "preview" or preview["decision_sha256"] != sha(proposal_path):
        raise ValueError("preview does not bind exact proposal")
    for record in proposal["records"]:
        if sha(ROOT / record["path"]) != record["expected_sha256"]:
            raise ValueError("target changed since proposal inspection")
    finish = datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")
    review_id = finish.replace("-", "").replace(":", "") + "-" + review_id.split("-", 1)[-1]
    target_ids = [r["recipe_id"] for r in proposal["records"]]
    evidence = [
        {
            "evidence_id": "proposal",
            "kind": "record_content",
            "reference": str(proposal_path.relative_to(ROOT)),
            "locator": "records ingredient_changes and all 98 dispositions",
            "accessed_at": finish,
            "support": "supports",
            "summary": "Exact source-bound proposals with per-event names, actions, concentration units/basis, stage, old descriptors and source evidence; unresolved rows explicitly held.",
            "snapshot_sha256": sha(proposal_path),
        }
    ]
    inputs = [
        {"path": r["path"], "sha256": r["expected_sha256"], "role": "target"}
        for r in proposal["records"]
    ]
    for path, role in [
        (proposal_path, "author proposal"),
        (inspection_path, "native target inspection"),
        (preview_path, "native guarded preview"),
    ]:
        inputs.append({"path": str(path.relative_to(ROOT)), "sha256": sha(path), "role": role})
    reference_ids = {}
    for i, source in enumerate(proposal["source_inspection"]):
        eid = f"primary-{i + 1}"
        reference_ids[source["reference"]] = eid
        item = {
            "evidence_id": eid,
            "kind": "primary_source",
            "reference": source["reference"],
            "locator": source.get(
                "locator",
                "Methods and explicitly cited formulation tables; per-event evidence locators in proposal",
            ),
            "accessed_at": source.get("retrieved_at", finish).replace("+00:00", "Z"),
            "support": "supports",
            "summary": "Primary content read for the explicit variant-only claims. "
            + source.get(
                "access_limitation",
                "Capture bytes and extraction receipt retained; chemical identities are not established by retrieval.",
            ),
        }
        if "sha256" in source:
            item["snapshot_sha256"] = source["sha256"]
            receipt = ROOT / source["receipt"]
            source_path = next(receipt.parent.glob("source.*"))
            if sha(source_path) != source["sha256"]:
                raise ValueError("primary source capture drift")
            inputs.append(
                {
                    "path": str(source_path.relative_to(ROOT)),
                    "sha256": source["sha256"],
                    "role": "primary source",
                }
            )
        evidence.append(item)
    assessments = []
    for row in proposal["dispositions"]:
        record = next(r for r in proposal["records"] if r["recipe_id"] == row["recipe_id"])
        changes = [
            c
            for v in record["variants"]
            if v["variant_index"] == row["variant_index"]
            for c in v["ingredient_changes"]
            if c["source_modification_index"] == row["source_modification_index"]
        ]
        refs = sorted({reference_ids[e["reference"]] for c in changes for e in c["evidence"]})
        details = []
        for c in changes:
            dose = c["ingredient"].get("concentration")
            text = c["action"] + " " + c["ingredient"]["preferred_term"]
            if dose:
                text += " " + dose["value"] + " " + dose["unit"]
            if c.get("replaced_ingredient"):
                text += " (old descriptor: " + c["replaced_ingredient"]["preferred_term"] + ")"
            details.append(text + "; stage: " + c["stage"])
        status = row["status"]
        assessments.append(
            {
                "assessment_id": f"queue-row-{row['queue_row_number']}",
                "area": "scope",
                "topic": f"{row['recipe_id']} variants[{row['variant_index']}].modifications[{row['source_modification_index']}]",
                "outcome": "concern" if status.startswith("HELD") else "supported",
                "summary": row["reason"]
                + (
                    " Proposals: " + " | ".join(details)
                    if details
                    else " No new ingredient event proposed."
                ),
                "target_ids": [row["recipe_id"]],
                "evidence_ids": ["proposal", *refs],
                "dimensions": [
                    {
                        "name": "native_concentration_decision",
                        "value": (
                            "unsupported"
                            if status == "HELD_EVIDENCE"
                            else (
                                "schema_gap"
                                if status == "HELD_MODEL"
                                else "add" if changes else "evidence_only"
                            )
                        ),
                        "definition": "Decision for new structured variant events only; existing base doses and whole-record scientific status are not certified.",
                        "evidence_ids": ["proposal", *refs],
                    },
                    {
                        "name": "queue_disposition",
                        "value": status,
                        "definition": "Disposition of this exact assigned queue row; STRUCTURED may retain explicitly stated identity/form limitations.",
                        "evidence_ids": ["proposal"],
                    },
                ],
            }
        )
    return {
        "schema_version": "1.0.0",
        "review_id": review_id,
        "kind": "batch",
        "repository": "CultureBotAI/CultureMech",
        "title": "Author source review of 98 Carini, Jensen, Pinchuk and Tang variant rows",
        "started_at": started_at,
        "finished_at": finish,
        "reviewer": {
            "identity": "codex-variant-family-author",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "The reviewer authored these proposals and the schema extension. This is an explicitly non-independent scientific author check; a separate reviewer must clear application.",
        },
        "skill": "curate-yaml-record; review-ingredient-concentrations",
        "completion": "completed",
        "verdict": "needs_curation",
        "native_verdict": "182 supported source-scoped events proposed; 98 row dispositions complete, with unresolved stock/mixture/form gaps retained. Independent review and application remain pending.",
        "scientific_review": True,
        "summary": "Reviewed primary Methods and table contexts for this exact 21-record proposal. Preserved 2013/2014 assay differences, isotope labels, source-stated hydrate forms, literal B-vitamin labels, stage boundaries and unsupported-conversion holds. No whole-medium equivalence, growth outcome or ontology identity is certified.",
        "source": {
            "git_revision": inspection["source"]["git_revision"],
            "state": "working_tree",
            "inputs": inputs,
        },
        "scope": {
            "description": proposal["scope"],
            "selection": "Exact inventory membership of the four named planning groups; all 98 rows represented in proposal dispositions.",
            "coverage": "partial",
            "population_size": 21,
            "reviewed_target_ids": target_ids,
            "exclusions": [
                {
                    "target": "Base ingredients, global growth/taxonomy and unrelated record content",
                    "reason": "Read as context; not comprehensively revalidated or scientifically recertified.",
                },
                {
                    "target": "Remaining queue families and MIM/KGM mapping release",
                    "reason": "Outside this source-family review.",
                },
            ],
        },
        "targets": targets(proposal),
        "checks": [
            {
                "check_id": "native-inspect",
                "name": "Native target/input inspection",
                "status": "passed",
                "required": True,
                "summary": "Native inspector captured exact recipe and proposal inputs; current recipe hashes still match proposal preimages.",
                "target_ids": target_ids,
                "evidence_ids": ["proposal"],
            },
            {
                "check_id": "primary-claims",
                "name": "Author reading of primary methods and source-form claims",
                "status": "passed",
                "required": True,
                "summary": "Read captured primary content; visually inspected Carini 2014 p.5 and Tang manuscript p.4. Jensen ASM PDF text inspected through browser; local hash unavailable. Exact source ambiguity is retained rather than resolved by inference.",
                "target_ids": target_ids,
                "evidence_ids": [
                    i["evidence_id"] for i in evidence if i["kind"] == "primary_source"
                ],
            },
            {
                "check_id": "guarded-preview",
                "name": "Native guarded proposal preview",
                "status": "passed",
                "required": True,
                "summary": "21 records planned without writes; exact source-text binding and native schema/semantic validation passed for the proposals.",
                "target_ids": target_ids,
                "command": ".venv/bin/python scripts/curate_variant_ingredients.py conf/variant_ingredient_curation/carini-jensen-pinchuk-tang-683.json --receipt .temp/variant-683/family-sources/four-families-preview-v1.json",
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": ["proposal"],
            },
        ],
        "evidence": evidence,
        "assessments": assessments,
        "findings": [],
        "actions": [],
        "limitations": [
            "Author review is not independent or human approval. No recipe was changed by this agent.",
            "B-number vitamins remain source-level labels with molecular/salt forms unresolved; generic methionine, serine and P-substrate labels do not certify imported stereoisomers.",
            "Held rows preserve uncertain phosphite stoichiometry, Jensen hydration/form questions, Wolfe stock correspondence and Tang 17-amino-acid mixture correspondence. These are not claims of absent ingredients.",
            "Jensen primary PDF has no retained local byte hash because anonymous downloads failed; browser text was inspected. Tang evidence is the OSTI-hosted manuscript version, whose page includes author edits.",
            "The source-specific negative phosphate event refers to original AMS1 Table 1 phosphate, not a claim that each imported parent contains phosphate or that residual phosphate is zero.",
            "Independent proposal review, central guarded application, post-application export accounting and release gates remain separate.",
        ],
        "links": ["https://github.com/CultureBotAI/CultureMech/issues/683"],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["targets", "draft"])
    parser.add_argument("--proposal", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--inspection", type=Path)
    parser.add_argument("--preview", type=Path)
    parser.add_argument("--review-id")
    parser.add_argument("--started-at")
    args = parser.parse_args()
    proposal_path = args.proposal.resolve()
    proposal = json.loads(proposal_path.read_text())
    value = (
        {"targets": targets(proposal)}
        if args.mode == "targets"
        else draft(
            proposal,
            proposal_path,
            args.inspection.resolve(),
            args.preview.resolve(),
            args.review_id,
            args.started_at,
        )
    )
    with args.output.open("x", encoding="utf-8") as stream:
        yaml.safe_dump(json.loads(json.dumps(value)), stream, sort_keys=False, allow_unicode=True)


if __name__ == "__main__":
    main()
