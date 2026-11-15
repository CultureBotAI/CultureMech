#!/usr/bin/env python3
"""Transcribe the scoped record07 assessment into an unsaved review draft.

Provenance date: 2026-11-15.
Context: CultureMech #749 (DSMZ876 needs-curation findings) and #752 (publish
executed helpers and exact historical sources, including superseded versions).

Required inputs: no CLI arguments. Run against the retained checkout and
.temp/batch079-scientific-20261114 artifacts: successful record07 inspect/check
and MIM receipts with their streams, claim-inventory.json, chemical assessment
and OLS catalog/raw inputs, DSMZ876 captures, peer review and all source paths
bound by the inspection. The helper selects the latest successful matching
receipt labels and verifies the inspected current input hashes; PyYAML is needed.
Outputs: an exclusively created record07/review.yaml and a console draft/ID
summary. It does not execute validators, save a native bundle or edit recipes.

Replay limits: embedded findings are frozen manual decisions, not new research.
Existing output prevents a direct rerun. The first executed predecessor emitted
YAML aliases and its validation failed; the retained NoAliasDumper successor
produced the later draft. Historical versions and receipts remain authoritative
for those events. Current headers/formatting do not restamp immutable review
inputs. Earlier bundle-only publication wording in draft text is historical;
#752 and the provenance README describe the superseding publication scope.
"""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
RUN = ROOT / ".temp" / "batch079-scientific-20261114"
CHEM = RUN / "record07" / "chemical-identity-tsb-20261115T075834261194Z"
TARGET = "CultureMech:002034"
ISSUE = "https://github.com/CultureBotAI/CultureMech/issues/749"


class NoAliasDumper(yaml.SafeDumper):
    def ignore_aliases(self, data):
        return True


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def receipt(label: str) -> tuple[Path, dict]:
    paths = sorted(RUN.glob(f"*-{label}.json"))
    selected = [(p, json.loads(p.read_text())) for p in paths]
    return next((p, d) for p, d in reversed(selected) if d.get("exit") == 0)


def main() -> None:
    inspected_path, inspected_receipt = receipt("record07-inspect-final")
    inspected = json.loads((ROOT / inspected_receipt["stdout"]).read_text())
    for item in inspected["source"]["inputs"]:
        assert digest(ROOT / item["path"]) == item["sha256"], item["path"]
    owners = inspected["targets"][0]["owner_paths"]
    inventory = json.loads((RUN / "record07" / "claim-inventory.json").read_text())
    chemical = json.loads((CHEM / "chemical-identity-assessment.json").read_text())
    catalog = json.loads((CHEM / "ols-capture-catalog.json").read_text())
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    review_id = (
        datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-batch079-record07-desulfothermus"
    )
    evidence = [
        {
            "evidence_id": "E-record",
            "kind": "record_content",
            "reference": inspected["targets"][0]["path"],
            "accessed_at": now,
            "support": "context_only",
            "summary": "Complete generated YAML and both complete maintained owners read; input hashes verified. Generated37 root ingredients/no solutions; each owner31 root ingredients and10 nested components.",
            "snapshot_sha256": next(
                x["sha256"] for x in inspected["source"]["inputs"] if x["role"] == "target"
            ),
        },
        {
            "evidence_id": "E-primary",
            "kind": "primary_source",
            "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium876.pdf",
            "locator": "Pages1–2: basal recipe, preparation and four separate stock tables",
            "accessed_at": "2026-11-15T07:58:11Z",
            "support": "partial",
            "summary": "Official formulation distinguishes basal ingredients, SL-10, selenite/tungstate and two vitamin stocks; supports anoxic preparation, pH and optional fatty-acid supplementation.",
            "snapshot_sha256": digest(RUN / "record07" / "DSMZ_Medium876.pdf"),
        },
        {
            "evidence_id": "E-structured",
            "kind": "database",
            "reference": "https://mediadive.dsmz.de/download/medium/876/json",
            "locator": "solutions1815,595,777,5980,1038; full separate recipe tables",
            "accessed_at": "2026-11-15T07:58:08Z",
            "support": "partial",
            "summary": "Provider records1005mL main volume and1000mL stocks. Twelve main rates match local values; stock rates must retain their separate solution context. Provider conversion is not independent proof of percentage basis or chemical grounding.",
            "snapshot_sha256": digest(RUN / "record07" / "medium876.json"),
        },
        {
            "evidence_id": "E-flattened",
            "kind": "database",
            "reference": "https://mediadive.dsmz.de/download/composition/876/json",
            "locator": "Pyridoxine hydrochloride row compared with both primary vitamin stocks",
            "accessed_at": "2026-11-15T07:58:08Z",
            "support": "refutes",
            "summary": "Flattened pyridoxine0.000298507g/L captures only the0.3g/L stock contribution at1mL/1005mL, although the other stock also supplies0.1g/L at1mL/1005mL. This endpoint is not an authoritative total oracle.",
            "snapshot_sha256": digest(RUN / "record07" / "composition876.json"),
        },
        {
            "evidence_id": "E-119",
            "kind": "primary_source",
            "reference": "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium119.pdf",
            "locator": "Fatty acid mixture subsection, pages2–3 only",
            "accessed_at": now,
            "support": "supports",
            "summary": "The referenced mixture is a separate preparation. Existing optional1%v/v prose correctly transfers this mixture only; no medium119 basal recipe, organism claims or gas conditions are transferred.",
        },
        {
            "evidence_id": "E-mim",
            "kind": "record_content",
            "reference": "src/culturemech/data/mediaingredientmech/label_index.csv",
            "locator": "Pinned metadata; exact label rows retained in input snapshot",
            "accessed_at": now,
            "support": "context_only",
            "summary": "Snapshot6643131b0f12ab40b66f98135245fca04027e0e9 passes native integrity check. Nickel exact-label rows include a rejected preferred row and mapped synonym, both53542; sodium-resazurin synonym maps8806. Resolver policy and chemical truth are separate.",
            "snapshot_sha256": digest(
                ROOT / "src/culturemech/data/mediaingredientmech/label_index.csv"
            ),
        },
        {
            "evidence_id": "E-peer",
            "kind": "prior_review",
            "reference": ".temp/batch079-scientific-20261114/peer-review-record07.md",
            "accessed_at": now,
            "support": "context_only",
            "summary": "Independent source peer supplied by coordinating root; current input and primary citations rechecked by the author before adopting findings.",
            "snapshot_sha256": digest(RUN / "peer-review-record07.md"),
        },
        {
            "evidence_id": "E-generator",
            "kind": "record_content",
            "reference": "src/culturemech/merge/formulation.py",
            "accessed_at": now,
            "support": "context_only",
            "summary": "Current generator requires exact formulation assertions, including stocks, notes and conditions. Historical ingredient-set grouping is not permission to force the two differing owners into one regenerated target.",
        },
    ]
    for item in catalog:
        term = item["exact_terms"][0]
        evidence.append(
            {
                "evidence_id": "E-" + item["id"].replace(":", "-"),
                "kind": "authority",
                "reference": item["url"],
                "locator": term["obo_id"] + ": exact active OLS/ChEBI term",
                "accessed_at": item["started_at"],
                "support": "context_only",
                "summary": term["label"]
                + "; formula="
                + str(term["annotation"].get("generalized_empirical_formula"))
                + "; active="
                + str(not term["is_obsolete"]),
                "snapshot_sha256": item["sha256"],
            }
        )
    checks = []
    for label, name, note in [
        ("record07-schema", "Native schema", "Open-schema structure only."),
        (
            "record07-strict",
            "Native strict schema",
            "One file, schema layer, zero errors; not a whole-repository QC sweep.",
        ),
        (
            "record07-terms",
            "Native term validator",
            "Configured bound slots only; chemical term slots are not fully bound and this does not establish supplied-form identity.",
        ),
        (
            "record07-references",
            "Native reference validator",
            "ZERO evidence assertions checked; no evidence completeness or scientific approval implied.",
        ),
        (
            "mim-index",
            "Packaged MIM snapshot integrity",
            "Byte/hash/row/contract integrity only; no external chemical proof.",
        ),
    ]:
        path, record = receipt(label)
        checks.append(
            {
                "check_id": "C-" + label,
                "name": name,
                "status": "passed",
                "required": True,
                "target_ids": [TARGET],
                "exit_code": record["exit"],
                "command": " ".join(record["argv"]),
                "summary": note,
                "scope_note": "Actual output, timing and exit retained at "
                + str(path.relative_to(ROOT)),
            }
        )
    checks.extend(
        [
            {
                "check_id": "C-inspect",
                "name": "Native input inspection",
                "status": "passed",
                "required": True,
                "exit_code": 0,
                "target_ids": [TARGET],
                "summary": "Native inspect captured every final local assessment input; original inputs rechecked without recipe changes.",
                "scope_note": str(inspected_path.relative_to(ROOT)),
            },
            {
                "check_id": "C-science",
                "name": "Primary-source scientific assessment",
                "status": "failed",
                "required": True,
                "target_ids": [TARGET],
                "summary": "Assessment completed and found critical stock representation and exact-form defects; failed scientific acceptance is retained as needs_curation.",
                "evidence_ids": [
                    "E-record",
                    "E-primary",
                    "E-structured",
                    "E-CHEBI-34887",
                    "E-CHEBI-53542",
                    "E-CHEBI-8806",
                ],
            },
            {
                "check_id": "C-history",
                "name": "Read-only history and ownership review",
                "status": "passed",
                "required": True,
                "target_ids": [TARGET],
                "summary": "Historical provenance and maintained/generated boundaries read; no history edited or native scientific status promoted. Native validate-history targets separate session HistoryRecords, not these embedded event arrays.",
                "evidence_ids": ["E-record", "E-generator"],
            },
            {
                "check_id": "C-komodo",
                "name": "Exact KOMODO recipe retrieval",
                "status": "unavailable",
                "required": False,
                "target_ids": [TARGET],
                "summary": "Exact servlet routes failed in bounded peer source review; no usable independent KOMODO formulation recovered. This is an unresolved source-identity finding, not an inferred equality.",
                "scope_note": "DSMZ876 and the imported-owner history establish the conflict; unverified KOMODO equivalence remains an explicit limitation.",
            },
        ]
    )
    assessments = []

    def assess(key, area, topic, outcome, summary, refs, details=None):
        item = {
            "assessment_id": key,
            "area": area,
            "topic": topic,
            "outcome": outcome,
            "summary": summary,
            "target_ids": [TARGET],
            "evidence_ids": refs,
        }
        if details:
            item["details"] = details
        assessments.append(item)

    assess(
        "A-identity",
        "identity",
        "Exact generated target and maintained sources",
        "concern",
        "CultureMech:002034 explicitly denotes DSMZ876. KOMODO876/TD3 is a distinct maintained owner with unresolved source-equivalence and atmosphere claims; historical89%-of37 counterevidence is not a current identity measurement.",
        ["E-record", "E-primary", "E-structured", "E-generator"],
    )
    assess(
        "A-main",
        "quantity",
        "All twelve basal component rates and volume basis",
        "supported",
        "The first twelve local rates match the structured main solution's explicit1005mL normalization. They are evidence_only decisions pending claim-level linkage, not instructions to replace them using1000mL water.",
        ["E-record", "E-structured"],
    )
    details = []
    for path, rows in inventory.items():
        details.append(path)
        for row in rows:
            ing = row["ingredient"]
            rate = ing.get("concentration", {})
            field = row["field"]
            sources = row["source_occurrences"]
            if field.startswith("ingredients[") and int(field.split("[")[1].split("]")[0]) < 12:
                decision = "evidence_only: main-rate supported on provider1005mL basis"
            elif field.startswith("solutions["):
                decision = "evidence_only for named stock-strength component; stock completeness and receiving dose still concern"
            else:
                decision = "correct representation: stock-strength/root placement or summed separate stocks; no new final concentration asserted"
            locators = ", ".join(
                str(x["solution_id"])
                + ":"
                + str(x.get("g_l"))
                + "g/L-stock-or-main/"
                + str(x["volume_ml"])
                + "mL-batch"
                for x in sources
            )
            details.append(
                f"{field}; {ing['preferred_term']}; retained={rate.get('value')} {rate.get('unit')}; {decision}; source={locators}"
            )
    assess(
        "A-amounts",
        "quantity",
        "Every direct and nested ingredient amount",
        "concern",
        "Reviewed37 generated root rows and41 rows in each owner, including10 existing nested components per owner. Correct stock placement before deriving final amounts; preserve distinct vitamin additions. No quantity or source field was changed.",
        ["E-record", "E-primary", "E-structured", "E-flattened"],
        "\n".join(details),
    )
    assess(
        "A-dose",
        "quantity",
        "Stock-addition basis and conversion limits",
        "concern",
        "DSM owner asserts three1mL/L additions; provider describes1mL per1005mL batch, with2mL selenium/tungsten stock. HCl2.5g/L is provider stock data, not independently derivable from an unspecified25% basis. Retain exact batch and stock context; no density assumption or averaged vitamin total.",
        ["E-record", "E-primary", "E-structured", "E-flattened"],
    )
    chem_details = []
    for row in chemical["assessments"]:
        chem_details.append(
            row["id"]
            + "; "
            + ", ".join(row["local_names"])
            + "; "
            + row["status"]
            + "; "
            + row["reason"]
        )
    assess(
        "A-chemistry",
        "grounding",
        "Every asserted chemical identifier and supplied form",
        "concern",
        "35 unique asserted ChEBI IDs across232 primary/secondary slots are active. Two exact-form mismatches remain: nickel hexahydrate and sodium resazurin.29 named identities are compatible; B12 breadth, lipoic stereochemistry, HCl solution context and generic calcium-pantothenate specificity retain explicit limits.",
        ["E-mim"] + ["E-" + x["id"].replace(":", "-") for x in catalog],
        "\n".join(chem_details),
    )
    assess(
        "A-preparation",
        "scope",
        "Preparation, pH, gas and optional supplement",
        "concern",
        "Main anoxic protocol, vitamin filtration and pH6.7–6.9 are source-supported. SL-10 makeup text belongs to the stock, while KOMODO aerobic wording conflicts with DSMZ. Optional1%v/v fatty-acid-mixture prose is correctly scoped to medium119's mixture only.",
        ["E-record", "E-primary", "E-119"],
    )
    assess(
        "A-classification",
        "identity",
        "Composition and physical-state classification",
        "supported",
        "Source describes a defined liquid formulation; existing DEFINED/DEFINED/LIQUID classification is supported. Empty optional growth/storage fields are not filled by inference.",
        ["E-record", "E-structured"],
    )
    assess(
        "A-growth",
        "evidence",
        "Organism and cultivation claims",
        "supported",
        "No strain-specific structured growth claim is asserted by this target. Generic cultivation context and optional stimulation note are recipe-source statements only; no optimality, species-wide growth or medium119 organism claim is inferred.",
        ["E-record", "E-primary", "E-119"],
    )
    assess(
        "A-provenance",
        "provenance",
        "Evidence linkage, history and generated freshness",
        "concern",
        "Each complete YAML lacks evidence entries; source URLs/history remain provenance leads. Existing nesting repairs are credited. GeneratedAugust6 content predates theirAugust7/15 nesting events, and current exact-formulation merge rules require source-boundary decisions before regeneration.",
        ["E-record", "E-primary", "E-generator"],
    )
    findings = []

    def finding(key, category, severity, title, description, paths, refs):
        findings.append(
            {
                "finding_id": key,
                "issue_key": "batch079-record07-" + key.lower(),
                "category": category,
                "severity": severity,
                "status": "open",
                "certainty": "confirmed",
                "title": title,
                "description": description,
                "target_ids": [TARGET],
                "field_paths": paths,
                "evidence_ids": refs,
                "owner_paths": owners,
                "rule_id": "CultureMech.single-record-checklist." + category,
                "native_severity": severity,
                "normalization_reason": "Severity follows concrete scientific impact, not a linkage percentage or validator score.",
                "external_issues": [ISSUE],
            }
        )

    finding(
        "F-stock",
        "representation",
        "blocker",
        "Stock formulations appear as basal ingredients",
        "Both owners leave trace, selenium/tungsten and vitamin components at root stock strengths. SL-10/vitamin nesting is incomplete and no selenium/tungsten container exists within these fully read files. This changes the formulation a reader would prepare; maintain separate stocks, supplied forms, addition amounts and source basis.",
        ["ingredients", "solutions"],
        ["E-record", "E-primary", "E-structured"],
    )
    finding(
        "F-stale",
        "ownership",
        "blocker",
        "Generated target drops existing normalized nesting repairs",
        "The generated target retains37 root ingredients and no solutions, including summed pyridoxine0.4, nicotinic acid0.25, B120.101 and PABA0.13G_PER_L. Each current owner has31 root plus10 nested components. Do not overwrite owners with this stale product or force differing formulations into one current merge group.",
        ["ingredients", "solutions", "merged_from", "curation_history"],
        ["E-record", "E-generator", "E-primary"],
    )
    finding(
        "F-nickel",
        "grounding",
        "major",
        "Hexahydrate supplied as anhydrous nickel chloride",
        "Generated ingredients[19] and both owners' ingredients[18] use34887 in primary and secondary term slots.53542 explicitly represents six waters. Exact MIM rows have different mapped/rejected roles; preserve resolver policy and attach chemical evidence through authoritative inputs.",
        ["ingredients[19].term", "ingredients[19].mediaingredientmech_chebi_term"],
        ["E-record", "E-CHEBI-34887", "E-CHEBI-53542", "E-mim"],
    )
    finding(
        "F-resazurin",
        "grounding",
        "major",
        "Sodium resazurin uses an identifier without sodium",
        "All three files' ingredients[7].term map the explicitly supplied sodium salt to8806, whose formula has no sodium. A repeated MIM synonym mapping is not independent chemical verification. Replacement identity remains unresolved; no substitute ID is invented.",
        ["ingredients[7].term"],
        ["E-record", "E-primary", "E-CHEBI-8806", "E-mim"],
    )
    finding(
        "F-preparation",
        "scope",
        "major",
        "Conflicting atmosphere and misplaced stock preparation",
        "KOMODO notes assert aerobic conditions while the associated DSMZ formulation is anoxic. Exact KOMODO equivalence is not established. Separately, DSM and generated preparation_steps[2] contain SL-10 makeup text at main-medium scope. Preserve distinctions among main80%N2/20%CO2, selected100%N2 stocks and vitamin filtration.",
        ["preparation_steps[2]", "parent_media", "merged_from"],
        ["E-record", "E-primary", "E-structured"],
    )
    finding(
        "F-linkage",
        "evidence",
        "minor",
        "Formulation support lacks narrow evidence links",
        "The complete three YAML files contain no evidence entries. Native references consequently inspect zero assertions. Attach evidence to each corrected claim, retaining source/version/stock basis and existing history; no missing optional property is inferred false.",
        ["evidence", "ingredients", "solutions"],
        ["E-record", "E-primary"],
    )
    actions = [
        {
            "action_id": "ACT-owners",
            "description": "Resolve source equivalence, stock boundaries/doses, preparation scoping and narrow evidence in the two maintained owners; keep exact quantities unsupported by sources unresolved. Current observations are retained as follow-up rather than a forced repair.",
            "finding_ids": ["F-stock", "F-preparation", "F-linkage"],
            "target_ids": [TARGET],
            "owner_paths": owners,
            "acceptance_checks": [
                "Compare every direct and nested component with primary stock tables, preserving1005mL provider basis and independent stock strengths.",
                "Use round-trip source edits with closed-schema validation and append-only substantive curation events.",
                "Rerun native schema, strict, term and reference checks on changed owners; manually verify PURL/table claims.",
            ],
        },
        {
            "action_id": "ACT-grounding",
            "description": "Correct only exact verified chemical forms in authoritative inputs after checking packaged resolver behavior; resolve or explicitly withhold sodium-resazurin replacement and narrower stereochemical claims.",
            "finding_ids": ["F-nickel", "F-resazurin"],
            "target_ids": [TARGET],
            "owner_paths": owners,
            "acceptance_checks": [
                "Recheck ChEBI formula/hydration/charge/stereochemistry against exact supplied source forms.",
                "Keep MIM snapshot immutable and use its maintained resolver; do not bypass rejected/ambiguous decisions.",
                "Validate changed owner terms and source-linked evidence without claiming configured term validation covers all chemical slots.",
            ],
        },
        {
            "action_id": "ACT-regenerate",
            "description": "After owner decisions, regenerate only the defensible scoped target group through maintained merge code, preserving IDs and all historical receipts. If owners split under exact-formulation rules, review the ID/lifecycle impact rather than forcing the historical merge.",
            "finding_ids": ["F-stale"],
            "target_ids": [TARGET],
            "owner_paths": owners,
            "depends_on": ["ACT-owners", "ACT-grounding"],
            "generator": "python -m culturemech.merge.merge_recipes with explicitly staged owner set",
            "acceptance_checks": [
                "Preview grouping/names/IDs; never use --limit as a target selector.",
                "Run native output validation, verify-merges and audit-merge-freshness at their documented scopes; record pre-existing corpus drift separately.",
                "Independent scientific review confirms stock/preparation/identity preservation before considering a passing assessment.",
            ],
        },
    ]
    review = {
        "schema_version": "1.0.0",
        "review_id": review_id,
        "kind": "record",
        "repository": "CultureBotAI/CultureMech",
        "title": "Recovered batch079 record07: DSMZ876 scientific assessment",
        "started_at": "2026-11-15T07:56:56Z",
        "finished_at": now,
        "reviewer": {
            "identity": "Codex recovery reviewer",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Reviewer did not author or alter the existing scientific inputs. Independent source and chemical peer contributions were checked against current bytes and inspected authorities. This is not human approval.",
        },
        "skill": ".claude/skills/review-yaml-record/SKILL.md",
        "completion": "completed",
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "Completed bounded assessment of one generated record with both maintained owners as context. Source tables confirm stock/root representation defects, stale generated content, two chemical-form mismatches and unresolved preparation/source scope. Native diagnostic passes do not change this verdict. No scientific record was edited.",
        "source": inspected["source"],
        "scope": {
            "description": "Record07 only: full generated target and its two maintained owners, every ingredient/stock entry, preparation, source provenance and chemical IDs.",
            "selection": "Recovered batch079 selection identifies CultureMech:002034; exact paths and IDs checked.",
            "coverage": "full",
            "population_size": 1,
            "reviewed_target_ids": [TARGET],
            "exclusions": [
                {
                    "target": "batch079 records01–06 and09",
                    "reason": "Historical receipts preserved, not reassessed or claimed complete.",
                },
                {
                    "target": "batch079 records08 and10",
                    "reason": "Deferred until this canary is validated, saved and verified.",
                },
                {
                    "target": "PR692, variant queue, catalog-wide repair and KG-Microbe workflow work",
                    "reason": "Separate scopes; this report makes no release/admission decision.",
                },
            ],
        },
        "targets": inspected["targets"],
        "checks": checks,
        "evidence": evidence,
        "assessments": assessments,
        "findings": findings,
        "actions": actions,
        "limitations": [
            "Completed assessment means the declared record was reviewed, not scientifically approved: two blocker and three major findings remain open.",
            "Exact KOMODO source formulation is inaccessible in the bounded search. DSM association and historical copied composition do not prove source equivalence.",
            "No scientific inputs were corrected or regenerated. Source-equivalence, dose basis and current formulation grouping require a separately verified correction; follow-up is filed in issue749.",
            "Native references checked zero evidence assertions; configured term checks do not independently validate every chemical supplied form.",
            "B12 is a broad class; lipoic stereochemistry and generic calcium-pantothenate specificity are not made more precise than their sources. HCl percentage basis/density is not invented.",
            "Raw primary captures, runtime logs and peer records are retained under ignored .temp with input hashes, not published as reusable source corpora. Working-tree hashes attest examined bytes; Git base remains dda27db.",
            "The broader history/ID/product/corpus and merge-freshness gates are not claimed executed by this read-only scientific assessment; no source/ID/product mutation required those gates in this canary.",
        ],
        "notes": [
            "Initial native inspect failed because a metadata filename was mistyped; the failed receipt is preserved and the corrected/final native inspections succeeded.",
            "The original approval rejections were superseded by direct user continuation approval before environment setup; no bypass was used.",
            "Optional medium119 supplementation is retained as supported prose, not a missing mandatory component.",
        ],
        "links": [
            ISSUE,
            "https://github.com/CultureBotAI/CultureMech/issues/150",
            "https://github.com/CultureBotAI/CultureMech/issues/278",
        ],
        "tags": ["batch079", "record07", "needs_curation", "source_review"],
    }
    destination = RUN / "record07" / "review.yaml"
    with destination.open("x") as handle:
        yaml.dump(
            review, handle, Dumper=NoAliasDumper, sort_keys=False, allow_unicode=True, width=100
        )
    print(
        json.dumps(
            {
                "draft": str(destination.relative_to(ROOT)),
                "review_id": review_id,
                "findings": len(findings),
            }
        )
    )


if __name__ == "__main__":
    main()
