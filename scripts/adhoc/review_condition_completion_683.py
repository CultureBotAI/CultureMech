#!/usr/bin/env python3
"""Record independent #683/#788 condition-row review, 2026-11-16.

Inputs: pinned proposal, original queue, recipe preimages and primary captures.
Outputs: exclusive readable inventory, verification and native review draft.
No scientific record mutation or network requests; source judgments are manual.
"""

import argparse
import csv
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
PROPOSAL = "conf/variant_ingredient_curation/completeness-conditions-683.json"
PIN = "888fbb82de4b8148a10b46a8c07f80a8460f0ccbaa571586d52f2d1d6a7a3a24"
JUDGMENTS = {
    "matsui": "Methods supports distinct high-CO2 and ambient-air aeration arms. This proposal concerns a different recipe coordinate from the prior model cohort; gas input is not a dissolved dose.",
    "125": "Official medium125 describes methane-air incubation at4:1 as an alternative to methanol addition. Ratio and input stage are retained without gas volume/pressure assumptions.",
    "kato": "The already-reviewed metal and carbon-source treatments remain linked, avoiding duplicate positive events. Condition notes do not alter default versus dose-response scopes.",
    "carini": "Media preparation explicitly orders CO2 sparging after autoclaving, then air sparging, then vitamin/organic additions. Establishing a bicarbonate buffer does not identify a directly added bicarbonate salt or measured final species concentration.",
    "blumer": "The modified DSMZ640 sugar-substrate Methods specify nitrogen headspace for the50mL culture. This is the exact Blumer-Schuette variant0, distinct from the same recipe's Shang variant1.",
    "11801": "Full source describes active ambient-air bubbling in the multi-cultivator. The supplied gas context is distinct from shaker-flask incubation; no dissolved dose or new growth-success assertion is inferred.",
    "11802": "Figure-associated full text supports the1-percent CO2 multi-cultivator arm with bubbling. Other CO2/shaker arms are not silently combined.",
    "nostoc": "The primary abstract distinguishes nitrate-present BG11 from nitrate-absent BG110. Comparator membership is held as operation/form uncertainty rather than an inferred removal from the nitrate-replete variant.",
    "mrs": "The primary abstract supports oxygen-condition comparisons but does not establish a gas-delivery procedure or dose. A field-specific operation/quantity hold is appropriate.",
}


def sha(data):
    return hashlib.sha256(data).hexdigest()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path, required=True)
    parser.add_argument("--output-directory", type=Path, required=True)
    args = parser.parse_args()
    directory = args.output_directory.resolve()
    directory.mkdir(parents=True, exist_ok=False)
    raw = (ROOT / PROPOSAL).read_bytes()
    if sha(raw) != PIN:
        raise ValueError("Frozen proposal changed")
    proposal = json.loads(raw)
    queue_bytes = args.queue.read_bytes()
    if sha(queue_bytes) != proposal["source_queue_sha256"]:
        raise ValueError("Original queue pin mismatch")
    with args.queue.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    targets, counts, recipes = [], {"changes": 0, "mentions": 0}, {}
    for record in proposal["records"]:
        data = (ROOT / record["path"]).read_bytes()
        if sha(data) != record["expected_sha256"]:
            raise ValueError("Recipe preimage changed")
        recipe = yaml.safe_load(data)
        recipes[record["path"]] = recipe
        if recipe["id"] != record["recipe_id"]:
            raise ValueError("Recipe identity mismatch")
        for variant in record["variants"]:
            current = recipe["variants"][variant["variant_index"]]
            if current["name"] != variant["variant_name"]:
                raise ValueError("Variant identity mismatch")
            for field, key in (("append_changes", "changes"), ("append_mentions", "mentions")):
                for claim in variant.get(field, []):
                    if (
                        current["modifications"][claim["source_modification_index"]]
                        != claim["source_text"]
                    ):
                        raise ValueError("Claim source coordinate/text mismatch")
                    if key == "mentions" and claim["source_label"] not in claim["source_text"]:
                        raise ValueError("Held label is not literal")
                    counts[key] += 1
        targets.append(
            {
                "target_id": recipe["id"],
                "path": record["path"],
                "label": recipe["name"],
                "kind": "maintained",
                "record_class": "MediaRecipe",
                "selector": "Only condition-row source inputs, holds and coverage dispositions in the frozen proposal",
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
        len(targets) != 58
        or counts != {"changes": 25, "mentions": 8}
        or len({item["queue_row_number"] for item in proposal["dispositions"]}) != 104
    ):
        raise ValueError("Frozen scope mismatch")
    readable = []
    for decision in proposal["dispositions"]:
        row = rows[decision["queue_row_number"] - 1]
        path = "data/normalized_yaml/" + row["source_path"]
        recipe = recipes[path]
        variant = recipe["variants"][int(row["variant_index"])]
        if variant["modifications"][int(row["modification_index"])] != row["modification_text"]:
            raise ValueError("Original queue coordinate drift")
        readable.append(
            f"{decision['queue_row_number']} | {decision['status']} | {row['source_path']} | {row['modification_text']}"
        )
        for link in decision.get("coverage_links", []):
            if "queue_row_number" in link:
                linked = rows[link["queue_row_number"] - 1]
                if linked["source_path"] != row["source_path"]:
                    raise ValueError("Coverage link crosses recipe")
                readable.append(
                    f"  linked {link['queue_row_number']} variant {linked['variant_index']}: {linked['modification_text']}"
                )
            else:
                pointer = link["field_path"]
                if not pointer.startswith("ingredients[") or not pointer.endswith("]"):
                    raise ValueError("Unexpected base link")
                if (
                    recipe["ingredients"][int(pointer[12:-1])]["preferred_term"]
                    != link["preferred_term"]
                ):
                    raise ValueError("Base ingredient link mismatch")
    (directory / "scope.txt").write_text("\n".join(readable) + "\n", encoding="utf-8")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    targets_path = directory / "targets.yaml"
    targets_path.write_text(yaml.safe_dump({"targets": targets}, sort_keys=False), encoding="utf-8")
    queue_path = directory / "original-review-queue.tsv"
    queue_path.write_bytes(queue_bytes)
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(targets_path.relative_to(ROOT)),
        "--input",
        PROPOSAL,
        "--input",
        str(Path(__file__).resolve().relative_to(ROOT)),
        "--input",
        str(queue_path.relative_to(ROOT)),
    ]
    evidence = []
    for source in proposal["source_inspections"]:
        data = (ROOT / source["path"]).read_bytes()
        if sha(data) != source["sha256"]:
            raise ValueError("Source capture changed")
        input_path = source["path"]
        if not (ROOT / input_path).resolve().is_relative_to(ROOT):
            copied = directory / (source["key"] + Path(input_path).suffix)
            copied.write_bytes(data)
            if sha(copied.read_bytes()) != source["sha256"]:
                raise ValueError("Private source copy changed")
            input_path = str(copied.relative_to(ROOT))
        command.extend(["--input", input_path])
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
    evidence.append(
        {
            "evidence_id": "context-accounting",
            "kind": "record_content",
            "reference": PROPOSAL,
            "accessed_at": now,
            "support": "supports",
            "summary": "All104 original condition rows were re-read. Named residual sodium, nitrate, total-silicate, oxygen and bicarbonate claims remain held at their exact unresolved dimensions. Existing/base occurrence links avoid duplicate inputs; ordinary temperature/pH/role/whole-medium conditions do not invent unnamed chemical additions.",
        }
    )
    result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
    if result.returncode:
        raise ValueError("Native inspect failed: " + result.stderr)
    inspection = json.loads(result.stdout)
    (directory / "inspection.json").write_text(result.stdout, encoding="utf-8")
    receipt = {
        "proposal_sha256": PIN,
        "queue_sha256": sha(queue_bytes),
        "recipes": 58,
        "dispositions": 104,
        **counts,
        "primary_captures": 9,
        "native_inspect_exit_code": 0,
    }
    (directory / "verification.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8"
    )
    ids = [target["target_id"] for target in targets]
    evidence_ids = [item["evidence_id"] for item in evidence]
    review = {
        "schema_version": "1.0.0",
        "review_id": now.replace("-", "").replace(":", "") + "-condition-completion-independent",
        "kind": "batch",
        "repository": "CultureBotAI/CultureMech",
        "title": "Independent review of104 condition-row ingredient dispositions",
        "started_at": now,
        "finished_at": now,
        "reviewer": {
            "identity": "codex-bundle-independent-scientific-reviewer",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Reviewer did not author this condition-completion proposal. Reviewer authored prior extraction and MIM intake code and a distinct earlier curation cohort; this review is limited to the new proposal.",
        },
        "skill": "curate-yaml-record; review-ingredient-concentrations",
        "completion": "completed",
        "verdict": "pass_with_limitations",
        "scientific_review": True,
        "native_verdict": "The25 source-stage gas events,8 field-specific holds and all104 condition dispositions are appropriate within their stated scope; no new material finding.",
        "summary": "Ordered gas operations and alternative/variant context are retained. Existing/base ingredient links prevent duplication. Held dimensions and ordinary conditions remain explicit without falsely certifying whole recipes.",
        "source": inspection["source"],
        "scope": {
            "description": "104 original condition rows across58 recipe preimages, including25 appended events and8 held mentions.",
            "selection": "Exact frozen proposal, original queue and all source/recipe pins.",
            "coverage": "partial",
            "population_size": 58,
            "reviewed_target_ids": ids,
            "exclusions": [
                {
                    "target": "Unrelated record content and truth of unresolved condition/growth claims",
                    "reason": "This is ingredient-disposition coverage, not whole-condition or whole-medium recertification.",
                }
            ],
        },
        "targets": targets,
        "checks": [
            {
                "check_id": "pins-and-links",
                "name": "Exact proposal, queue, source and coverage links",
                "status": "passed",
                "required": True,
                "summary": "All preimages/captures verified, all104 rows bind exact source coordinates, links resolve in the same recipe with explicit alternative-variant context, and base ingredient links resolve exactly.",
                "target_ids": ids,
            },
            {
                "check_id": "science",
                "name": "Independent source and condition-disposition reading",
                "status": "passed",
                "required": True,
                "summary": "Manual reading supports the bounded gas stages and retained holds; no supplied gas is assigned a dissolved concentration and no comparator or mixture inference is promoted.",
                "target_ids": ids,
                "evidence_ids": evidence_ids,
            },
        ],
        "evidence": evidence,
        "assessments": [
            {
                "assessment_id": "condition-" + target["target_id"].replace(":", "-"),
                "area": "scope",
                "topic": "Condition-row ingredient coverage and source-stage operations",
                "outcome": "supported",
                "target_ids": [target["target_id"]],
                "evidence_ids": evidence_ids,
                "summary": "Proposed inputs and holds agree with source-family judgments; other condition text remains contextual and unrecertified. No-op envelopes add no ingredient assertions.",
            }
            for target in targets
        ],
        "findings": [],
        "actions": [],
        "limitations": [
            "Agent review, not human approval or release approval.",
            "No scientific records were mutated. Writer, schema, aggregate and MIM mapping gates remain separate.",
            "Nostoc/MRS support is limited to the inspected primary abstracts. Unavailable detailed preacclimation or oxygen procedures remain held.",
            "Ingredient-role links do not independently certify base ontology identities, doses or growth claims.",
            "Gas-supply stages are not liquid concentrations; alternative arms and ordered sparging are not combined.",
            "No-op envelopes may be filtered by the merger while every disposition remains accounted for.",
        ],
        "links": [
            "https://github.com/CultureBotAI/CultureMech/issues/683",
            "https://github.com/CultureBotAI/CultureMech/issues/788",
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
