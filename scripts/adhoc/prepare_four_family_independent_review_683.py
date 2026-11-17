#!/usr/bin/env python3
"""Package independent review of four-family variant claims (2026-11-16, #683).

Inputs: frozen proposal, pinned inventory, native inspection, filed finding URL.
Outputs: targets/proof or native review content; no recipe or proposal edits.
Scientific source assessment is manual; this helper verifies snapshot/accounting.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
EXPECTED = "786ae063209accd3c3ad1e67bd2043e0ff0a4e94703e6b5d8a55b0d073d1b32c"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--decision", type=Path, required=True)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--inspection", type=Path)
    parser.add_argument("--issue-url")
    args = parser.parse_args()
    if hashlib.sha256(args.decision.read_bytes()).hexdigest() != EXPECTED:
        raise ValueError("review requires the frozen candidate")
    payload = json.loads(args.decision.read_text())
    inventory = json.loads(args.inventory.read_text())
    row_by_coordinate = {
        (item["recipe_id"], int(item["variant_index"]), int(item["modification_index"])): (n, item)
        for n, item in enumerate(inventory["rows"], 1)
    }
    expected_rows = set()
    for group in inventory["planning_groups"]:
        if group["name"] in {
            "carini_ams1_source_family",
            "jensen_bl_source_family",
            "pinchuk_m1_source_family",
            "tang_tracer_source_family",
        }:
            expected_rows.update(group["queue_row_numbers"])
    observed_rows = [row["queue_row_number"] for row in payload["dispositions"]]
    if len(observed_rows) != len(set(observed_rows)) or set(observed_rows) != expected_rows:
        raise ValueError("disposition membership mismatch")
    counts = Counter()
    targets = []
    for record in payload["records"]:
        raw = (ROOT / record["path"]).read_bytes()
        if hashlib.sha256(raw).hexdigest() != record["expected_sha256"]:
            raise ValueError("record drift:" + record["path"])
        document = yaml.safe_load(raw)
        if document["id"] != record["recipe_id"]:
            raise ValueError("recipe identity mismatch")
        targets.append(
            {
                "target_id": record["recipe_id"],
                "path": record["path"],
                "label": document["name"],
                "kind": "maintained",
                "record_class": "MediaRecipe",
                "selector": "Exact proposed variant ingredient_changes and assigned queue dispositions only",
                "owner_paths": [
                    {
                        "repository": "CultureBotAI/CultureMech",
                        "path": record["path"],
                        "role": "authoritative normalized recipe",
                    }
                ],
            }
        )
        for variant in record["variants"]:
            vi = variant["variant_index"]
            original = document["variants"][vi]
            if original["name"] != variant["variant_name"]:
                raise ValueError("variant identity mismatch")
            for change in variant["ingredient_changes"]:
                mi = change["source_modification_index"]
                number, row = row_by_coordinate[(record["recipe_id"], vi, mi)]
                if (
                    change["source_text"] != original["modifications"][mi]
                    or change["source_text"] != row["modification_text"]
                ):
                    raise ValueError("source text mismatch")
                if number not in expected_rows:
                    raise ValueError("assertion outside assigned scope")
                counts[number] += 1
    for row in payload["dispositions"]:
        if row["assertion_count"] != counts[row["queue_row_number"]]:
            raise ValueError("assertion count mismatch")
    if not args.inspection:
        result = {"targets": targets}
    else:
        if not args.issue_url:
            parser.error("--issue-url required for review content")
        inspection = json.loads(args.inspection.read_text())
        source = inspection["source"]
        ids = [target["target_id"] for target in targets]
        now = "2026-11-16T21:25:00Z"
        evidence = [
            {
                "evidence_id": "proposal",
                "kind": "record_content",
                "reference": str(args.decision),
                "accessed_at": now,
                "support": "partial",
                "snapshot_sha256": EXPECTED,
                "summary": "Frozen98-row proposal:182assertions, explicit holds and zero base/prose mutations. Manual independent review plus exact-coordinate/accounting checks.",
            }
        ]
        for name, filename, reference, locator, summary in [
            (
                "carini-2013-html",
                "source.html",
                "doi:10.1038/ismej.2012.122",
                "Table1; Glycine substitution experiments; Table3",
                "Read exact AMS1 forms/doses and assay amendments. Literal B-number labels and unspecified stereochemistry remain explicit; no ontology IDs inferred.",
            ),
            (
                "carini-2014",
                "source.pdf",
                "doi:10.1038/ncomms5346",
                "Page5, Methods Organism source and Cultivation details",
                "Visually inspected original page5 to disambiguate micro symbols corrupted by text extraction. Assay doses and alternate-P compounds match; phosphite formula held.",
            ),
            (
                "pinchuk-2010",
                "source.xml",
                "doi:10.1371/journal.pcbi.1000822",
                "Methods, Culture medium",
                "Verified4.35mM NaH2PO4.H2O and batch/chemostat separation; unresolved Wolfe stocks remain held.",
            ),
            (
                "tang-2009",
                "source.pdf",
                "doi:10.1002/btpr.227",
                "Author manuscript page4, Materials and Methods",
                "Visually inspected labeled sodium L-lactate30mM and PIPES20mM; holds preserve17-component mixture ambiguity. Quantitative quote defect remains filed.",
            ),
        ]:
            path = ".temp/variant-683/family-sources/" + name + "/" + filename
            digest = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
            receipt = json.loads((ROOT / path).with_name("receipt.json").read_text())
            if digest != receipt["sha256"]:
                raise ValueError("source capture drift")
            source["inputs"].append(
                {"path": path, "sha256": digest, "role": "independently inspected primary source"}
            )
            evidence.append(
                {
                    "evidence_id": name,
                    "kind": "primary_source",
                    "reference": reference,
                    "locator": locator,
                    "accessed_at": now,
                    "support": "supports",
                    "summary": summary,
                    "snapshot_sha256": digest,
                }
            )
        evidence.append(
            {
                "evidence_id": "jensen",
                "kind": "primary_source",
                "reference": "https://journals.asm.org/doi/epdf/10.1128/aem.59.12.4363-4366.1993",
                "locator": "Pages4363–4364: formulation paragraph, Table1 footnote b, Table3",
                "accessed_at": now,
                "support": "supports",
                "summary": "Independently read primary PDF via web tool. Calcium pantothenate identity and2micromolar pantothenate basis are supported; no local source hash claimed. Unresolved salt forms remain held.",
            }
        )
        families = [
            (
                "carini",
                "Carini assay stages and chemical forms",
                ids[:8],
                ["carini-2013-html", "carini-2014"],
            ),
            (
                "jensen",
                "Jensen calcium pantothenate and unresolved stock forms",
                ids[8:13],
                ["jensen"],
            ),
            (
                "pinchuk",
                "Pinchuk monobasic monohydrate and batch context",
                ids[13:17],
                ["pinchuk-2010"],
            ),
            ("tang", "Tang isotope/stereochemistry and doses", ids[17:], ["tang-2009"]),
        ]
        assessments = [
            {
                "assessment_id": key,
                "area": "quantity",
                "topic": title,
                "outcome": "supported",
                "summary": "Proposed identities/doses agree with the cited primary material within their explicit assay scope. This is not certification of parent ingredients, full variant composition or downstream mapping. Quantitative evidence quotations require the separate filed correction.",
                "target_ids": subset,
                "evidence_ids": ["proposal"] + refs,
            }
            for key, title, subset, refs in families
        ]
        assessments.append(
            {
                "assessment_id": "accounting",
                "area": "provenance",
                "topic": "Complete98-row disposition and exact182assertion bindings",
                "outcome": "supported",
                "summary": "Verified unique assigned row membership, source hashes, recipe/variant names, exact modification text and per-row assertion counts across all21records. Held rows are not positive occurrences.",
                "target_ids": ids,
                "evidence_ids": ["proposal"],
            }
        )
        finding = {
            "finding_id": "quantified-quotes",
            "issue_key": "variant-quantified-evidence-quotes",
            "category": "evidence",
            "severity": "minor",
            "status": "open",
            "certainty": "confirmed",
            "title": "Quantified Tang/Jensen evidence quotations omit the amount/basis",
            "description": "All4Tang labeled-lactate replacement snippets quote only the chemical label, while concentration30mM is asserted. All5Jensen calcium-pantothenate snippets omit the2micromolar pantothenate-basis amount retained in notes. Actual primary sources support these values; evidence snippets must preserve them explicitly for the concentration-review contract.",
            "target_ids": ids[8:13] + ids[17:],
            "field_paths": ["variants[].ingredient_changes[].evidence[].snippet"],
            "evidence_ids": ["proposal", "tang-2009", "jensen"],
            "ownership_note": "The proposal builder owns these evidence snippets; recipes remain unapplied.",
            "external_issues": [args.issue_url],
        }
        result = {
            "schema_version": "1.0.0",
            "review_id": "20261116T212500Z-four-family-independent-claims",
            "kind": "batch",
            "repository": "CultureBotAI/CultureMech",
            "title": "Independent pre-application review of Carini, Jensen, Pinchuk and Tang variant claims",
            "started_at": "2026-11-16T21:23:00Z",
            "finished_at": now,
            "reviewer": {
                "identity": "codex-independent-reviewer",
                "kind": "agent",
                "independence": "independent",
                "independence_basis": "This reviewer did not author the four-family decision/builder or edit its recipes. Independently read primary captures/PDF images and the Jensen primary PDF, reviewed all unique scientific claims and exact repeated-record bindings.",
            },
            "skill": "curate-yaml-record; review-ingredient-concentrations",
            "completion": "completed",
            "verdict": "needs_curation",
            "native_verdict": "Source-supported182assertions require the filed quantitative-evidence-quotation correction before guarded application; held rows remain held.",
            "scientific_review": True,
            "summary": "No incorrect proposed dose/form found in the reviewed scope. A concrete evidence-contract defect affects quantified Tang and Jensen snippets. Full recipe, taxonomic/growth claims and release readiness are not recertified.",
            "source": source,
            "scope": {
                "description": "Exact182proposed ingredient assertions plus98row dispositions across21records; claim-level independent assessment, not whole-record scientific recertification.",
                "selection": "Four assigned source families in frozen proposal SHA256" + EXPECTED,
                "coverage": "partial",
                "population_size": 21,
                "reviewed_target_ids": ids,
                "exclusions": [
                    {
                        "target": "Other record fields and unproposed/held claims",
                        "reason": "Outside bounded proposed-claim verification; holds remain explicit.",
                    },
                    {
                        "target": "Application/export and MIM/KGM release",
                        "reason": "No mutation or release acceptance in this review.",
                    },
                ],
            },
            "targets": targets,
            "checks": [
                {
                    "check_id": "native-inspection",
                    "name": "Native snapshot and exact binding verification",
                    "status": "passed",
                    "required": True,
                    "summary": "Native inspector captured exact proposal/schema/target bytes; this helper independently verified all98assignedrows and182assertion coordinates/counts without recipe mutation.",
                    "target_ids": ids,
                    "evidence_ids": ["proposal"],
                    "command": "record_review.py inspect plus prepare_four_family_independent_review_683.py snapshot/accounting verification",
                    "exit_code": 0,
                    "expected_exit_code": 0,
                }
            ],
            "evidence": evidence,
            "assessments": assessments,
            "findings": [finding],
            "actions": [
                {
                    "action_id": "repair-quotes",
                    "description": "Add exact primary amount/unit and explicit basis excerpts to the affected evidence items, keeping assertions/scientific scope unchanged, then independently re-review the frozen repair.",
                    "finding_ids": ["quantified-quotes"],
                    "target_ids": ids[8:13] + ids[17:],
                    "ownership_note": "Proposal author owns evidence-only repair.",
                    "acceptance_checks": [
                        "Tang quote contains30mM tied to labeled growth substrate, distinct from20mM PIPES.",
                        "Jensen evidence preserves2micromolar pantothenate basis without asserting2micromolar calcium salt.",
                        "No dose/form/stage change, source drift or held-row promotion.",
                    ],
                }
            ],
            "limitations": [
                "Jensen primary PDF inspected through web reader; local downloads unavailable and no local hash invented.",
                "Source-supported values do not resolve held phosphite stoichiometry, Jensen hydrate/molybdate ambiguity, Wolfe-stock correspondence or amino-acid-mixture mapping.",
                "Repeated occurrences remain separate record-level events; no ontology identity, full parent equivalence or human REVIEWED status granted.",
                "Native preview was reported by author; this reviewer did not rerun application/tests or mutate records.",
            ],
            "links": [args.issue_url],
        }
    with args.output.open("x") as stream:
        yaml.dump(result, stream, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True)
    print(
        json.dumps(
            {
                "targets": len(targets),
                "rows": len(observed_rows),
                "assertions": sum(counts.values()),
                "output": str(args.output),
            }
        )
    )


if __name__ == "__main__":
    main()
