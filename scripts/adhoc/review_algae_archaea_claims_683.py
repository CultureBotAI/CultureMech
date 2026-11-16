#!/usr/bin/env python3
"""Record independent review of 52 variant claims for #683/#763, 2026-11-16.

Inputs: frozen proposal, checkpoint proposal, authoritative recipes, primary captures.
Outputs: exclusive review draft, native inspection and bounded verification receipt.
No recipe writes or external requests. Scientific judgments below record the
reviewer's primary-source reading; the mechanical checks do not prove science.
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

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = "conf/variant_ingredient_curation/algae-archaea-683.json"
EXPECTED = "8918ca273b10dc6cce0292e504c741e0ec65b68c7feee2c65098180a8b3ed0f6"
BASE = "93d23e4415"
BEFORE = "b326ba81ebf38479e5d2e5b550a89bfa7c1d649edaf46603de7df3fbb14dcf5d"
JUDGMENTS = {
    "tsuji": "Table S1 establishes separate mM basal and micromolar trace-element headers. Sodium choices are discrete, including zero; 0.001 micromolar selenite is 1 nanomolar, not 10. Metasilicate is the nonahydrate. Trace sodium and unrelated basal components are not inferred from these events.",
    "spectrum": "Cultivation Methods supports reported 1.5 M NaCl. This does not establish full equivalence between the cited preparation and the local parent recipe.",
    "hiibel": "Maintenance-media Methods explicitly substitutes 33.6 g/L sea salts for NaCl and separately replaces the f/2 vitamin solution with the named 2ASW vitamin solution. Undefined mixtures are not expanded.",
    "synecho": "ASW Results and Figure 2 support 5 mM NH4Cl, 0.22 mM K2HPO4 and 20 mM HEPES-KOH at pH 7.8. These are the ASW experimental preparation, not BG11 preculture or an independently verified complete local parent recipe.",
    "tetraselmis": "Primary abstract supports the separate second-stage 4.41 mM NaNO3 repletion after the initial cultivation stage. The abstract does not establish all formulation details.",
    "spirulina": "Methods supports filtered effluent added at 1.5% v/v initially, a similar volume after three days and 3% of initial volume after six days. Sequential additions are not a 6% initial concentration; the undefined effluent is not expanded.",
    "fertilizer": "Primary abstract explicitly replaces Tris with HAc-NaAc. Buffer ratio, acetate form and dose remain unresolved; whole fertilizer-medium replacement is not accepted from this identity-only event.",
    "emami": "Culture and antibiotic-treatment Methods support HCl acidification, 1.06e-4 M silicate, 29.4 mM nitrate and separate penicillin G/dihydrostreptomycin sulfate treatment doses of 200/50 micrograms per mL. Stock strengths, unstated chemical forms and untreated controls are not inferred.",
    "bbmerds": "Official CCAP instructions specify 8:2 or 1:1 mixtures of the separately prepared media. The explicitly selected one-litre mixture normalization yields 800/200 or 500/500 mL; this is a stated arithmetic interpretation of the preparation ratio, not a measured chemical concentration or an addition atop a completed parent.",
    "f2si": "Official CCAP page 2 explicitly omits stock 5 and instead adds 0.1705 g sodium metasilicate nonahydrate per litre of medium. The replacement retains hydrate identity and excludes double counting of stock 5.",
    "reed": "The cultivation paragraph, not downstream protein assays, supports 20 mM each Tris/maleic acid, 22 mM DL-sodium lactate, 0.5 g/L yeast extract and 1 mM each sulfide/thiosulfate. Resazurin's literal 0.2% lacks a definitive final-dose basis and remains unconverted. Stored biomass under nitrogen does not establish culture sparging. Hartzell alternatives remain held.",
    "mayer": "The acetate-determination Methods paragraph supports 0.1% wt/vol yeast extract in its specified mixotrophic arm. A separate 0.05% experiment is not substituted or pooled.",
    "dsm119": "Official strain-specific instructions distinguish medium120 10x vitamins at 1 mL/L from medium141 vitamins at 10 mL/L, named hydrate removals, final g/L additions and literal 0.3 g batch additions without a per-litre basis. Glucose, acetate, sulfate, coenzyme M and rumen-fluid substitutions remain in their exact DSM strain/stage contexts; gases are not liquid doses.",
    "pyrococcus": "Primary abstract supports CF11 cellulose identity in serial adaptation, without a fabricated dose, constituent expansion or complete formulation equivalence.",
    "willard": "Low-sulfate Brock Methods supports replacing ammonium sulfate with 1.05 g/L NH4Cl. An unchanged basal magnesium-sulfate amount is not invented as a new event. Species-specific supplements and a different cited anaerobic preparation remain held.",
    "auernik": "Transcriptomics Methods separates 0.1% yeast-extract cultures, two of which receive approximately 7.5 g/L FeSO4 heptahydrate, from the SEM preparation using literal 0.1% FeS2 as sole energy source. The unspecified percent basis remains literal; approximation and alternative arms are preserved.",
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def without_quotes(document):
    result = copy.deepcopy(document)
    for record in result["records"]:
        for variant in record["variants"]:
            for change in variant["ingredient_changes"]:
                for evidence in change["evidence"]:
                    evidence.pop("snippet", None)
                    evidence.pop("explanation", None)
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", required=True, type=Path)
    args = parser.parse_args()
    directory = args.output_directory.resolve()
    directory.mkdir(parents=True, exist_ok=False)
    raw = (ROOT / PROPOSAL).read_bytes()
    if sha(raw) != EXPECTED:
        raise ValueError("frozen proposal changed")
    document = json.loads(raw)
    previous = subprocess.run(
        ["git", "show", BASE + ":" + PROPOSAL], cwd=ROOT, capture_output=True, check=True
    ).stdout
    if sha(previous) != BEFORE or without_quotes(json.loads(previous)) != without_quotes(document):
        raise ValueError("proposal repair changed non-quotation fields or historical input")
    targets = []
    count = 0
    for record in document["records"]:
        data = (ROOT / record["path"]).read_bytes()
        if sha(data) != record["expected_sha256"]:
            raise ValueError("target changed: " + record["path"])
        recipe = yaml.safe_load(data)
        if recipe["id"] != record["recipe_id"]:
            raise ValueError("record ID mismatch")
        for variant in record["variants"]:
            original = recipe["variants"][variant["variant_index"]]
            if original["name"] != variant["variant_name"]:
                raise ValueError("variant name mismatch")
            for change in variant["ingredient_changes"]:
                if (
                    original["modifications"][change["source_modification_index"]]
                    != change["source_text"]
                ):
                    raise ValueError("source text mismatch")
                count += 1
        targets.append(
            {
                "target_id": record["recipe_id"],
                "path": record["path"],
                "label": recipe["name"],
                "kind": "maintained",
                "record_class": "MediaRecipe",
                "selector": "Only proposed source-bound ingredient_changes in the frozen proposal",
                "owner_paths": [
                    {
                        "repository": "CultureBotAI/CultureMech",
                        "path": record["path"],
                        "role": "authoritative normalized recipe",
                    }
                ],
            }
        )
    dispositions = document["dispositions"]
    if count != 52 or len(targets) != 15 or len(dispositions) != 96:
        raise ValueError("frozen scope count mismatch")
    if len({row["queue_row_number"] for row in dispositions}) != 96:
        raise ValueError("duplicate disposition row")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    target_file = directory / "targets.yaml"
    target_file.write_text(yaml.safe_dump({"targets": targets}, sort_keys=False), encoding="utf-8")
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(target_file.relative_to(ROOT)),
        "--input",
        PROPOSAL,
        "--input",
        str(Path(__file__).resolve().relative_to(ROOT)),
    ]
    evidence = []
    references = {}
    for source in document["source_inspections"]:
        if sha((ROOT / source["path"]).read_bytes()) != source["sha256"]:
            raise ValueError("primary capture changed: " + source["key"])
        references[source["reference"]] = source["key"]
        command.extend(["--input", source["path"]])
        evidence.append(
            {
                "evidence_id": source["key"],
                "kind": "primary_source",
                "reference": source["reference"],
                "locator": source["locator"],
                "accessed_at": now,
                "support": "supports",
                "summary": JUDGMENTS[source["key"]],
                "snapshot_sha256": source["sha256"],
            }
        )
    result = subprocess.run(command, cwd=ROOT, check=True, capture_output=True, text=True)
    inspection = json.loads(result.stdout)
    (directory / "inspection.json").write_text(result.stdout, encoding="utf-8")
    receipt = {
        "proposal_sha256": EXPECTED,
        "previous_sha256": BEFORE,
        "only_quote_fields_changed": True,
        "assertions": count,
        "recipes": len(targets),
        "dispositions": len(dispositions),
        "primary_captures": len(evidence),
        "native_inspect_exit_code": result.returncode,
    }
    (directory / "verification.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8"
    )
    assessments = []
    for record in document["records"]:
        selected = sorted(
            {
                references[item["reference"]]
                for variant in record["variants"]
                for change in variant["ingredient_changes"]
                for item in change["evidence"]
            }
        )
        assessments.append(
            {
                "assessment_id": "claims-" + record["recipe_id"].replace(":", "-"),
                "area": "scope",
                "topic": "Bounded proposed ingredient identities, doses, actions and stages",
                "outcome": "supported",
                "target_ids": [record["recipe_id"]],
                "evidence_ids": selected,
                "summary": "The proposed events agree with the source-specific judgments above. Repaired exact excerpts and quoted table headings support numeric bases. This assessment excludes held claims and unrelated existing recipe assertions.",
            }
        )
    ids = [item["target_id"] for item in targets]
    review_id = now.replace("-", "").replace(":", "") + "-algae-archaea-independent-claims"
    review = {
        "schema_version": "1.0.0",
        "review_id": review_id,
        "kind": "batch",
        "repository": "CultureBotAI/CultureMech",
        "title": "Independent review of 52 algae and archaea variant ingredient claims",
        "started_at": now,
        "finished_at": now,
        "reviewer": {
            "identity": "codex-bundle-independent-scientific-reviewer",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Reviewer did not author this cohort's scientific proposal or quote repairs. Reviewer authored the native ingredient scanner and a different bacterial/specialized cohort; these surfaces are outside this scientific independence claim.",
        },
        "skill": "curate-yaml-record; review-ingredient-concentrations",
        "completion": "completed",
        "verdict": "pass_with_limitations",
        "scientific_review": True,
        "native_verdict": "All 52 proposed events are supported within their stated stages and evidence access limits. The #763 quantity/basis excerpt repairs are adequate for this frozen cohort; no held claim is promoted.",
        "summary": "Independent primary-source comparison supports the bounded scientific payload and revised quotations. Exact source and target hashes, coordinates and quote-only edit scope were checked separately. This does not certify all catalog chemistry, complete formulations or release readiness.",
        "source": inspection["source"],
        "scope": {
            "description": "52 proposed ingredient events in 15 recipes from a 96-row algae/archaea disposition cohort.",
            "selection": "Exact frozen proposal SHA256 recorded in this helper and native source inputs.",
            "coverage": "partial",
            "population_size": 15,
            "reviewed_target_ids": ids,
            "exclusions": [
                {
                    "target": "Held rows, condition-only rows and unrelated recipe content",
                    "reason": "No promotion of unavailable sources, undefined mixture constituents, gas operations, uncertain quantity bases or whole-formulation equivalence.",
                }
            ],
        },
        "targets": targets,
        "checks": [
            {
                "check_id": "frozen-inputs",
                "name": "Exact proposal, target, source and coordinate verification",
                "status": "passed",
                "required": True,
                "summary": "All 52 events, 15 target recipes, 96 unique dispositions and 16 primary captures verified; historical comparison permits only evidence snippet/explanation changes; native inspect exited zero.",
                "target_ids": ids,
            },
            {
                "check_id": "independent-claims",
                "name": "Primary source claims and quantitative excerpt review",
                "status": "passed",
                "required": True,
                "summary": "Separate read-only manual comparison supports the bounded claims and repaired quantity/basis quotations. Automated matching alone is not treated as scientific evidence.",
                "target_ids": ids,
                "evidence_ids": [item["evidence_id"] for item in evidence],
            },
        ],
        "evidence": evidence,
        "assessments": assessments,
        "findings": [],
        "actions": [],
        "limitations": [
            "Agent review of the proposed events, not human approval, whole-record certification or release approval.",
            "Native writer/corpus/export verification and MIM adoption remain separate acceptance gates.",
            "Abstract-only support is limited to explicit statements; detailed inaccessible methods are not reconstructed.",
            "Named mixtures are not expanded, uncertain percentage/batch bases stay literal, and alternative experimental arms are not summed.",
            "The 96-row disposition set is verified unchanged; this review does not certify scientific completeness of held or condition-only rows.",
        ],
        "links": [
            "https://github.com/CultureBotAI/CultureMech/issues/683",
            "https://github.com/CultureBotAI/CultureMech/issues/763",
            "https://github.com/CultureBotAI/CultureMech/issues/759",
        ],
    }
    draft = directory / "review.yaml"
    draft.write_text(
        yaml.safe_dump(json.loads(json.dumps(review)), sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    print(json.dumps({"review_id": review_id, "review": str(draft.relative_to(ROOT)), **receipt}))


if __name__ == "__main__":
    main()
