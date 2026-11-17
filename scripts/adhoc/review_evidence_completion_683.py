#!/usr/bin/env python3
"""Persist independent scientific review of the #683 evidence proposal, 2026-11-16.

Inputs: hash-pinned proposal, recipe preimages and inspected primary captures.
Outputs: exclusive native review draft, inspection and claim/mention inventory.
No recipe writes or network calls. Judgments record manual source reading;
hash and coordinate checks alone do not establish scientific correctness.
"""

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = "conf/variant_ingredient_curation/completeness-evidence-683.json"
PIN = "85f718233396d14a3bac3165694a76db4bc1bb9a1ac35923a78b1ac65b600d4b"
JUDGMENTS = {
    "matsui": "Culture and transformation Methods support the named half-strength Guillard mixture and plate-specific agar; no absolute mixture concentration or agar dose is invented.",
    "kato": "Methods explicitly omit CaCl2 from the basal trace solution, with separate later metal supplementation. The REMOVE is stock-stage scoped, not universal calcium absence.",
    "jcm": "The official 1219 recipe gives 15 g agar per listed preparation, 970 mL water plus stock and later additions, without a final-volume adjustment. The batch amount avoids unsupported g/L.",
    "shang": "Methods list components per litre of distilled-water input; amounts and hydrate forms agree. Separate xylan, xylose and glucose arms remain distinct. No final-volume denominator or exact ferrous replacement is invented.",
    "kosch": "Printed pages 27–28 distinguish one-litre SME stock from the half-SME preparation, later sulfide solution and bottle-specific sulfur. Stock SrCl2/KI amounts, bicarbonate batch mass, sulfide hydration range and uncalibrated spatula are retained.",
    "blood": "The official DSMZ693 recipe supports sheep-blood identity and an unspecified-basis 5 percent statement. It does not justify a mass-concentration conversion.",
    "bacdive": "The exact strain page links medium693 and reports sheep blood at 50 g/L. This database assertion is distinct from DSMZ's unspecified percent; the proposal supports identity while retaining the quantity conflict.",
    "sakai": "Dissertation sections 3.2.3.3 and 3.3.2.3 support nonahydrate, resazurin, yeast extract, separate sulfur/no-sulfur arms, 110 kPa and 65 C. The result is no anaerobic growth after four weeks. Removing that variant's positive growth target is justified; headspace gases remain phase-scoped holds.",
    "ohanlon": "Methods explicitly distinguish plain ATCC1490 strains from B. ureolyticus in supplemented1490 with formate/fumarate. Scoped omission relative to the supplemented parent is supported; exact salts and zero concentrations are not inferred.",
    "ms10": "The accessible publisher abstract does not resolve the exact reactor phosphate salt/dose. Retaining a field-specific hold is appropriate; the ratio does not establish absolute composition.",
    "tsuji": "Table S1 supplies separate basal mM and trace micromolar headings. The 0.001 micromolar selenite value is 1 nanomolar; sodium metasilicate nonahydrate is 0.1 mM. The explicit arithmetic and form are correct.",
    "willard": "Culture Methods names concentrated HCl and species-specific temperatures/pH. It does not support H2SO4 as an interchangeable alternative in this formulation.",
    "carini": "Page5 image supports nominal 1.0 micromolar phosphite while printing an unresolved salt formula. Keeping the nominal dose separate from the exact-form hold avoids correcting stoichiometry by assumption. Vitamin-label doses remain distinct from unknown vitamer/salt identities.",
    "jensen": "Publisher PDF Table1 supports nominal MgCl2 at 0.52 mM in BL and the named BL treatment variants. It does not specify its hydrate; the unusual printed molybdate formula does not justify promoting the parent's tetrahydrate.",
    "marine": "The primary paper author copy, printed2730, explicitly uses MB1/2 without peptone/yeast extract for single-carbon-source assay plates. Routine MB1/2 remains distinct. These negative descriptors are not positive occurrences.",
    "holds": "Remaining claims retain literal named labels with precise source, quantity, identity, operation or phase limits. Inaccessible Hartzell/Brierley/Johnston details are not approved. Existing independently supported occurrences are not demoted by a separate form/quantity hold; no gas concentration, mixture expansion, missing-as-zero or whole-medium equivalence is inferred.",
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", type=Path, required=True)
    args = parser.parse_args()
    directory = args.output_directory.resolve()
    directory.mkdir(parents=True, exist_ok=False)
    raw = (ROOT / PROPOSAL).read_bytes()
    if sha(raw) != PIN:
        raise ValueError("Frozen proposal changed")
    proposal = json.loads(raw)
    targets, inventory = [], []
    counts = {"changes": 0, "mentions": 0, "corrections": 0, "field_replacements": 0}
    for record in proposal["records"]:
        data = (ROOT / record["path"]).read_bytes()
        if sha(data) != record["expected_sha256"]:
            raise ValueError("Recipe preimage changed: " + record["path"])
        recipe = yaml.safe_load(data)
        if recipe["id"] != record["recipe_id"]:
            raise ValueError("Recipe identity mismatch")
        for field in record.get("field_replacements", []):
            value = recipe
            for key in field["path"]:
                value = value[key]
            if value != field["expected"]:
                raise ValueError("Field correction preimage mismatch")
            counts["field_replacements"] += 1
        for variant in record["variants"]:
            current = recipe["variants"][variant["variant_index"]]
            if current["name"] != variant["variant_name"]:
                raise ValueError("Variant mismatch")
            modifications = list(current["modifications"])
            for replacement in variant.get("replace_modifications", []):
                index = replacement["modification_index"]
                if modifications[index] != replacement["expected"]:
                    raise ValueError("Modification preimage mismatch")
                modifications[index] = replacement["replacement"]
                counts["corrections"] += 1
            for field, kind in (("append_changes", "changes"), ("append_mentions", "mentions")):
                for item in variant.get(field, []):
                    if modifications[item["source_modification_index"]] != item["source_text"]:
                        raise ValueError("Source coordinate/text mismatch")
                    if kind == "mentions" and item["source_label"] not in item["source_text"]:
                        raise ValueError("Held label is not literal")
                    counts[kind] += 1
                    inventory.append(
                        {
                            "recipe": record["path"],
                            "variant": variant["variant_index"],
                            "kind": kind,
                            "claim": item,
                        }
                    )
        targets.append(
            {
                "target_id": record["recipe_id"],
                "path": record["path"],
                "label": recipe["name"],
                "kind": "maintained",
                "record_class": "MediaRecipe",
                "selector": "Only additions and exact field/prose corrections in the pinned evidence-completion proposal",
                "owner_paths": [
                    {
                        "repository": "CultureBotAI/CultureMech",
                        "path": record["path"],
                        "role": "authoritative normalized recipe",
                    }
                ],
            }
        )
    if (
        len(targets) != 36
        or counts["changes"] != 43
        or counts["mentions"] != 111
        or len({d["queue_row_number"] for d in proposal["dispositions"]}) != 60
    ):
        raise ValueError("Frozen scientific scope count mismatch")
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
    for source in proposal["source_inspections"]:
        source_bytes = (ROOT / source["path"]).read_bytes()
        if sha(source_bytes) != source["sha256"]:
            raise ValueError("Primary capture changed: " + source["key"])
        input_path = source["path"]
        if not (ROOT / input_path).resolve().is_relative_to(ROOT):
            copied = directory / (source["key"] + Path(input_path).suffix)
            copied.write_bytes(source_bytes)
            if sha(copied.read_bytes()) != source["sha256"]:
                raise ValueError("Private evidence copy changed")
            input_path = str(copied.relative_to(ROOT))
        command.extend(["--input", input_path])
        evidence.append(
            {
                "evidence_id": source["key"],
                "kind": "primary_source" if source["key"] != "bacdive" else "database",
                "reference": source["reference"],
                "locator": source["locator"],
                "accessed_at": now,
                "support": "supports",
                "summary": JUDGMENTS[source["key"]],
                "snapshot_sha256": source["sha256"],
            }
        )
    for key, source in zip(("jensen", "marine"), proposal["browser_inspections"], strict=True):
        evidence.append(
            {
                "evidence_id": key,
                "kind": "primary_source",
                "reference": source["reference"],
                "locator": source["locator"],
                "accessed_at": now,
                "support": "supports",
                "summary": JUDGMENTS[key]
                + " Browser-only inspection; no downloaded capture hash claimed.",
            }
        )
    evidence.append(
        {
            "evidence_id": "holds",
            "kind": "record_content",
            "reference": PROPOSAL,
            "accessed_at": now,
            "support": "supports",
            "summary": JUDGMENTS["holds"],
        }
    )
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    if result.returncode:
        raise ValueError("Native inspect failed: " + result.stderr)
    inspection = json.loads(result.stdout)
    (directory / "inspection.json").write_text(result.stdout, encoding="utf-8")
    (directory / "inventory.json").write_text(
        json.dumps(inventory, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    receipt = {
        "proposal_sha256": PIN,
        "recipes": len(targets),
        "queue_rows": 60,
        **counts,
        "primary_captures": len(proposal["source_inspections"]),
        "browser_only_primary_sources": 2,
        "native_inspect_exit_code": result.returncode,
    }
    (directory / "verification.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8"
    )
    ids = [target["target_id"] for target in targets]
    evidence_ids = [item["evidence_id"] for item in evidence]
    review = {
        "schema_version": "1.0.0",
        "review_id": now.replace("-", "").replace(":", "") + "-evidence-completion-independent",
        "kind": "batch",
        "repository": "CultureBotAI/CultureMech",
        "title": "Independent review of 43 supported events and 111 field-specific held mentions",
        "started_at": now,
        "finished_at": now,
        "reviewer": {
            "identity": "codex-bundle-independent-scientific-reviewer",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Reviewer did not author this proposal or follow-up scientific corrections. Reviewer authored prior extraction and MIM intake code and a different earlier curation cohort, outside this scientific independence claim.",
        },
        "skill": "curate-yaml-record; review-ingredient-concentrations",
        "completion": "completed",
        "verdict": "pass_with_limitations",
        "scientific_review": True,
        "native_verdict": "The bounded supported additions and explicit held dimensions agree with the inspected sources; no new material finding.",
        "summary": "Source preparation stages, quantities, exact forms, negative experimental result and held dimensions were inspected independently. This proposal does not certify complete recipes or erase unresolved source claims.",
        "source": inspection["source"],
        "scope": {
            "description": "60 queue rows, 36 recipe preimages, 43 supported events, 111 held mentions and the enumerated prose/field corrections.",
            "selection": "Exact frozen proposal hash and all recipe/source inputs recorded by native inspection.",
            "coverage": "partial",
            "population_size": 36,
            "reviewed_target_ids": ids,
            "exclusions": [
                {
                    "target": "Unrelated recipe assertions and unresolved held claim truth",
                    "reason": "The hold is reviewed as appropriate; inaccessible source details are not certified.",
                }
            ],
        },
        "targets": targets,
        "checks": [
            {
                "check_id": "frozen-inputs",
                "name": "Proposal, preimage, capture and coordinate checks",
                "status": "passed",
                "required": True,
                "summary": "Pinned proposal and all 36 preimages/13 source captures verified; 43 events and 111 mentions bind their exact resulting source text.",
                "target_ids": ids,
            },
            {
                "check_id": "scientific-claims",
                "name": "Independent primary-source scientific comparison",
                "status": "passed",
                "required": True,
                "summary": "Manual review of source family claims, amounts, forms, stage boundaries and explicit holds; two browser-only primary sources are identified separately.",
                "target_ids": ids,
                "evidence_ids": evidence_ids,
            },
        ],
        "evidence": evidence,
        "assessments": [
            {
                "assessment_id": "bounded-" + record["recipe_id"].replace(":", "-"),
                "area": "scope",
                "topic": "Proposed variant events, field-specific holds and exact corrections",
                "outcome": "supported",
                "target_ids": [record["recipe_id"]],
                "evidence_ids": evidence_ids,
                "summary": "Supported events and field corrections are source-scoped as recorded in the evidence judgments. Held mentions retain uncertainty without asserting identity or ingredient presence; unrelated recipe content is outside this assessment.",
            }
            for record in proposal["records"]
        ],
        "findings": [],
        "actions": [],
        "limitations": [
            "Agent review, not human approval or release approval.",
            "No recipe mutation was performed. Native writer, schema/export gates and MIM scientific binding review remain separate.",
            "Inaccessible primary claims remain withheld, rather than treated as verified absence or falsehood.",
            "Jensen and marine-paper full content was inspected through browser; no local snapshot hash is claimed for those two sources.",
            "Stock components, water-input/batch amounts and experimental arms remain separate; uncertain formulas, vitamer/salt identities and quantities are not resolved by familiar labels.",
            "Growth-test ingredients do not imply successful growth; the Sakai negative result and target removal are retained explicitly.",
        ],
        "links": [
            "https://github.com/CultureBotAI/CultureMech/issues/683",
            "https://github.com/CultureBotAI/CultureMech/issues/759",
            "https://github.com/CultureBotAI/CultureMech/issues/762",
            "https://github.com/CultureBotAI/CultureMech/issues/776",
            "https://github.com/CultureBotAI/CultureMech/issues/777",
            "https://github.com/CultureBotAI/CultureMech/issues/778",
            "https://github.com/CultureBotAI/CultureMech/issues/779",
        ],
    }
    draft = directory / "review.yaml"
    draft.write_text(
        yaml.safe_dump(json.loads(json.dumps(review)), sort_keys=False, allow_unicode=True),
        encoding="utf-8",
    )
    print(json.dumps({"review": str(draft.relative_to(ROOT)), **receipt}))


if __name__ == "__main__":
    main()
