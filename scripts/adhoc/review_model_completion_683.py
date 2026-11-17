#!/usr/bin/env python3
"""Save independent review of #683 model-held claims, 2026-11-16.

Inputs: pinned proposal, recipe preimages and primary captures; output: exclusive
native review draft and verification receipt. No recipe writes/network requests.
Scientific judgments below record manual source reading, not automatic approval.
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
PROPOSAL = "conf/variant_ingredient_curation/completeness-model-683.json"
PIN = "548408377e4a75f000f779560647661533107b78199283df371ccda1680fde28"
JUDGMENTS = {
    "751": "Official liquid-medium instruction supplies phosphate masses, not an explicit final litre. SET_AMOUNT correctly retains 1.5 g KH2PO4 and 0.5 g K2HPO4 per batch.",
    "670": "Current official base table supplies 950 mL water before separately described ferrous stock/strain amendments. This input is not a final-volume denominator or the older archive's one-litre input.",
    "125": "Official instruction explicitly supplies 5 mL methanol or a methane-air atmosphere. The promoted amount preserves the methanol batch input without purity or final-volume assumptions.",
    "956": "Official post-sterilization alternatives specify final 0.5 percent methanol or 0.3 percent methylamine. Basis remains unspecified; no v/v or mass concentration is invented.",
    "119": "Official DSM2030/9575 instructions specify 2 bar overpressure and DSM25939/25945 specify 1 bar, after inoculation with 80:20 hydrogen/carbon dioxide. Events preserve strain, stage and gas context; no liquid dose is implied.",
    "hemiaulus": "Methods explicitly describe naturally dissolved nitrogen in fixed-N-free cultures. A held operation is appropriate: source presence does not establish deliberate nitrogen addition or a named fixed-nitrogen removal.",
    "fertilizer": "The primary abstract supports a named water-soluble fertilizer replacing TAP trace/macroelements. The named mixture input is defensible while exact product composition, dose and displaced chemicals remain held.",
    "teusink": "The source table's complete-formulation membership is not automatically converted into ingredient additions or removal operations. Existing discrete approved amounts are outside this follow-up assertion scope.",
    "tang": "Author manuscript page4 specifies the AA-S-18 supplement, 17 included amino acids at 25 micromolar each and three excluded amino acids. Named mixture input is supported. Exclusion from the supplement does not establish whole-culture absence or removal; exact DL forms are not inferred.",
    "pinchuk": "Methods explicitly name 10 mL each of two 10x stocks without a final-volume denominator. Literal inputs are retained, with stock-component correspondence to flattened parents held separately.",
    "bg11": "Captured phototrophic Methods support alternative ambient-air/2-percent-CO2 supplies at 0.5 vvm for ABC-009 in BG-11. This is distinct from the heterotrophic YM experiment; no gas fraction is encoded as a dissolved concentration.",
    "matsui": "Culture Methods distinguish high-CO2 and ambient-air aeration arms. The gas identity/stage is represented without mixing alternative arms or inventing aqueous concentration.",
    "kato": "Methods assign default 20 micromolar metal treatments to the specified strain arms and separately describe methane gas per tube or 20 mM methanol. The methane amount is a two-mL gas input into one tube batch; metal hydration, standard-state gas volume and simultaneous carbon supplies are not invented.",
    "kosch": "Printed page28 distinguishes final 80:20 hydrogen/carbon-dioxide headspace exchange at 1.5 bar from the earlier nitrogen/carbon-dioxide purge and chamber gas. The proposed events preserve that final-headspace scope.",
    "willard": "Culture Methods supports elemental sulfur at 10 g/L, separate species groups receiving 1 or 0.2 g/L yeast extract, and the sucrose/NZ-Amine arm. Vented bottles do not independently prove a removal of the local parent's sulfide or nitrogen.",
    "tsuji": "The publisher abstract directly contrasts supplied 5-percent and 0.04-percent carbon-dioxide air under low sodium; the lower-CO2 arm did not support growth. Both inputs can be recorded without a positive growth claim or invented full Methods.",
    "marine": "The primary-paper author copy, printed2730, states dilution of marine medium to half strength with water. The named diluent input is supported; an absolute water volume or complete constituent expansion is not inferred.",
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
    counts = {"append_changes": 0, "append_mentions": 0, "replace_changes": 0}
    for record in proposal["records"]:
        data = (ROOT / record["path"]).read_bytes()
        if sha(data) != record["expected_sha256"]:
            raise ValueError("Recipe preimage changed")
        recipe = yaml.safe_load(data)
        if recipe["id"] != record["recipe_id"]:
            raise ValueError("Recipe identity mismatch")
        for variant in record["variants"]:
            current = recipe["variants"][variant["variant_index"]]
            if current["name"] != variant["variant_name"]:
                raise ValueError("Variant identity mismatch")
            for kind in ("append_changes", "append_mentions", "replace_changes"):
                for item in variant.get(kind, []):
                    if kind == "replace_changes":
                        if current["ingredient_changes"][item["change_index"]] != item["expected"]:
                            raise ValueError("Amount promotion preimage mismatch")
                        promoted = copy.deepcopy(item["replacement"])
                        if "amount" not in promoted:
                            raise ValueError("Missing promoted quantity")
                        promoted.pop("amount")
                        if promoted != item["expected"]:
                            raise ValueError("Amount promotion changed other claims")
                        claim = item["replacement"]
                    else:
                        claim = item
                    if (
                        current["modifications"][claim["source_modification_index"]]
                        != claim["source_text"]
                    ):
                        raise ValueError("Source coordinate/text mismatch")
                    if (
                        kind == "append_mentions"
                        and claim["source_label"] not in claim["source_text"]
                    ):
                        raise ValueError("Held label is not literal")
                    counts[kind] += 1
                    inventory.append(
                        {
                            "recipe": record["path"],
                            "variant": variant["variant_index"],
                            "kind": kind,
                            "claim": claim,
                        }
                    )
        targets.append(
            {
                "target_id": record["recipe_id"],
                "path": record["path"],
                "label": recipe["name"],
                "kind": "maintained",
                "record_class": "MediaRecipe",
                "selector": "Only model-completion events, held mentions and six literal-amount promotions in the pinned proposal",
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
        len(targets) != 27
        or counts != {"append_changes": 47, "append_mentions": 19, "replace_changes": 6}
        or len({d["queue_row_number"] for d in proposal["dispositions"]}) != 37
    ):
        raise ValueError("Frozen scope mismatch")
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    target_path = directory / "targets.yaml"
    target_path.write_text(yaml.safe_dump({"targets": targets}, sort_keys=False), encoding="utf-8")
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        str(target_path.relative_to(ROOT)),
        "--input",
        PROPOSAL,
        "--input",
        str(Path(__file__).resolve().relative_to(ROOT)),
    ]
    evidence = []
    for source in proposal["source_inspections"]:
        data = (ROOT / source["path"]).read_bytes()
        if sha(data) != source["sha256"]:
            raise ValueError("Primary capture changed")
        input_path = source["path"]
        if not (ROOT / input_path).resolve().is_relative_to(ROOT):
            copied = directory / (source["key"] + Path(input_path).suffix)
            copied.write_bytes(data)
            if sha(copied.read_bytes()) != source["sha256"]:
                raise ValueError("Private evidence copy changed")
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
    for key, source in zip(("tsuji", "marine"), proposal["browser_inspections"], strict=True):
        evidence.append(
            {
                "evidence_id": key,
                "kind": "primary_source",
                "reference": source["reference"],
                "locator": source["locator"],
                "accessed_at": now,
                "support": "supports",
                "summary": JUDGMENTS[key] + " Browser inspection; no local capture hash claimed.",
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
        "recipes": 27,
        "queue_rows": 37,
        **counts,
        "only_amount_added_to_existing_six_events": True,
        "primary_captures": 15,
        "browser_only_primary_sources": 2,
        "native_inspect_exit_code": 0,
    }
    (directory / "verification.json").write_text(
        json.dumps(receipt, indent=2) + "\n", encoding="utf-8"
    )
    ids = [target["target_id"] for target in targets]
    evidence_ids = [item["evidence_id"] for item in evidence]
    review = {
        "schema_version": "1.0.0",
        "review_id": now.replace("-", "").replace(":", "") + "-model-completion-independent",
        "kind": "batch",
        "repository": "CultureBotAI/CultureMech",
        "title": "Independent review of model-completion events and field-specific holds",
        "started_at": now,
        "finished_at": now,
        "reviewer": {
            "identity": "codex-bundle-independent-scientific-reviewer",
            "kind": "agent",
            "independence": "independent",
            "independence_basis": "Reviewer did not author this follow-up proposal or its six amount promotions. Reviewer authored earlier extraction and MIM intake code and a distinct earlier bacterial cohort; this review is limited to the new proposal.",
        },
        "skill": "curate-yaml-record; review-ingredient-concentrations",
        "completion": "completed",
        "verdict": "pass_with_limitations",
        "scientific_review": True,
        "native_verdict": "The proposed 47 appended events, 19 field-specific holds and six literal-amount promotions agree with inspected sources; no new material finding.",
        "summary": "Gas phase, species/strain/alternative arms, literal batch and unspecified-percent bases, named stocks and negative mixture membership remain explicit. No whole-medium or successful-growth inference is approved.",
        "source": inspection["source"],
        "scope": {
            "description": "31 original model-held rows plus six existing-event amount promotions, covering 27 recipe preimages and 37 dispositions.",
            "selection": "Exact frozen proposal and source/recipe hash inventory.",
            "coverage": "partial",
            "population_size": 27,
            "reviewed_target_ids": ids,
            "exclusions": [
                {
                    "target": "Unrelated recipe assertions, full formulations and truth of unresolved held details",
                    "reason": "Only the enumerated proposal is assessed; held dimensions are retained rather than approved.",
                }
            ],
        },
        "targets": targets,
        "checks": [
            {
                "check_id": "frozen-inputs",
                "name": "Proposal, targets, sources and exact amount-only promotions",
                "status": "passed",
                "required": True,
                "summary": "All preimages/captures and source coordinates verified; six replacements add only amount, preserving existing identity, action, evidence and stage.",
                "target_ids": ids,
            },
            {
                "check_id": "scientific-claims",
                "name": "Independent source-family claim review",
                "status": "passed",
                "required": True,
                "summary": "Manual primary-source reading supports the bounded assertions and holds; gas supply is not liquid concentration, named mixture is not constituent identity, and alternative arms are not simultaneous.",
                "target_ids": ids,
                "evidence_ids": evidence_ids,
            },
        ],
        "evidence": evidence,
        "assessments": [
            {
                "assessment_id": "model-" + record["recipe_id"].replace(":", "-"),
                "area": "scope",
                "topic": "Proposed model completion and quantity representation",
                "outcome": "supported",
                "target_ids": [record["recipe_id"]],
                "evidence_ids": evidence_ids,
                "summary": "The enumerated proposal agrees with the source-family judgments and preserves uncertainty in separate held dimensions. Context-only dispositions add no invented ingredients.",
            }
            for record in proposal["records"]
        ],
        "findings": [],
        "actions": [],
        "limitations": [
            "Agent scientific review, not human approval or release approval.",
            "No recipes were mutated; native writer/export/schema gates remain separate.",
            "Tsuji evidence is the publisher abstract only; marine-paper text was inspected in an author copy. Neither browser-only source is assigned a fabricated capture hash.",
            "This review does not establish exact forms of unresolved salts/stocks, correspondence to flattened parents, or unreported final volumes.",
            "Gas events retain headspace/aeration stages; no liquid dose or physiological success is inferred.",
            "No-op record/variant envelopes may be omitted by the separate merger without changing these scientific decisions or disposition accounting.",
        ],
        "links": [
            "https://github.com/CultureBotAI/CultureMech/issues/683",
            "https://github.com/CultureBotAI/CultureMech/issues/760",
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
