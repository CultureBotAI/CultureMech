#!/usr/bin/env python3
"""Prepare manually source-reviewed UTEX ingredient proposals (#683; 2026-11-16).

Inputs: exact preserved prose inventory; authoritative normalized recipe bytes.
Output: explicit guarded decision JSON. Does not edit recipes or infer identities.
Source pages were inspected through the public web reader on 2026-11-16; direct
curl returned HTTP429. Short quotations and exact locators remain in each claim.
"""

import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QUEUE_SHA = "dd5faea741da0a11e8eb86cad2976e8bf51d42884c601e96973eba61748330ca"
URL = "https://utex.org/products/"


def claim(label, stage, notes, page, snippet, locator, concentration=None):
    ingredient = {"preferred_term": label, "notes": notes}
    if concentration:
        ingredient["concentration"] = concentration
    return {
        "action": "ADD",
        "ingredient": ingredient,
        "stage": stage,
        "evidence": [
            {
                "reference": URL + page,
                "supports": "SUPPORT",
                "snippet": snippet,
                "explanation": locator + "; primary UTEX collection page inspected 2026-11-16. "
                "This ingredient occurrence is scoped to the optional variant, not a change to the liquid parent.",
            }
        ],
    }


def reviewed_claims():
    claims = {}
    for number, slug in [
        (1, "one-half"),
        (2, "one-third"),
        (3, "one-fourth"),
        (4, "one-fifth"),
        (73, None),
    ]:
        page = (slug + "-" if slug else "") + "soil-plus-seawater-medium"
        claims[number] = [
            claim(
                "calcium carbonate",
                "optional carbonate addition before steaming",
                "Literal source batch input: 1 mg in the 200 mL recipe. No measured final-volume "
                "concentration is inferred. Fisher catalog C 64; optional formulation only.",
                page,
                "1 mg" if slug else "1 mg/200 mL of Seawater",
                "Recipe table, optional CaCO3 row; Directions, 200 mL total",
            )
        ]
    for number, page, amount, basis, snippet in [
        (25, "euglena-medium", "15 g", "1 L prepared liquid", "add 15 g of agar"),
        (34, "j-medium", "12.5 g", "1 L prepared liquid", "add 12.5 g of agar"),
        (35, "malt-medium", "7.5 g", "batch starting with 500 mL dH2O", "add 7.5 g of agar"),
        (36, "polytomella-medium", "15 g", "1 L prepared liquid", "add 15 grams of agar"),
        (
            44,
            "trebouxia-medium",
            "15 g",
            "liquid made up to 1 L with Bristol Medium",
            "add 15 g of agar",
        ),
        (
            45,
            "volvocacean-medium",
            "10.0 g",
            "800 mL Waris plus 200 mL Euglena medium",
            "add 10.0 grams of agar",
        ),
    ]:
        concentration = None
        if number == 34:
            concentration = {
                "value": "1.25",
                "unit": "PERCENT_W_V",
                "per_volume": "source-designated optional agar formulation",
            }
        claims[number] = [
            claim(
                "agar",
                "optional agar addition before autoclaving",
                f"Literal batch input: {amount} agar added to {basis}; do not mix. "
                "Retain this preparation basis without inferring a measured volume after agar addition.",
                page,
                snippet,
                "Directions, optional agar instruction",
                concentration,
            )
        ]
    for first, page in [
        (56, "bg-11-1-plus-0-point-36-percent-nacl-medium"),
        (59, "bg-11-plus-1-percent-nacl-medium"),
    ]:
        claims[first] = [
            claim(
                "NaCl",
                "saline liquid portion before separate autoclaving",
                "Use this formulation's NaCl while preparing the 500 mL liquid portion. "
                "The modification does not restate a dose; do not interpret a stock concentration.",
                page,
                "Add NaCl",
                "Agar media, step 2",
            ),
            claim(
                "dH2O",
                "liquid portion makeup before separate autoclaving",
                "Make the supplemented liquid portion up to 500 mL with dH2O; "
                "500 mL is the portion volume, not an independently specified water dose.",
                page,
                "bring total volume to 500 mL",
                "Agar media, step 2",
            ),
        ]
        claims[first + 1] = [
            claim(
                "agar",
                "separate agar portion before autoclaving",
                "Literal input: 15 g agar to 500 mL dH2O in a separate container. "
                "The two portions are combined later; no final concentration is inferred.",
                page,
                "15 g of agar",
                "Agar media, step 3",
            ),
            claim(
                "dH2O",
                "separate agar portion before autoclaving",
                "Literal input: 500 mL dH2O for the separate agar portion. "
                "This is a preparation input, not a final-volume water fraction.",
                page,
                "500 mL of dH",
                "Agar media, step 3; water notation dH2O",
            ),
        ]
        claims[first + 2] = [
            claim(
                "sodium thiosulfate",
                "sterile addition to cooled agar portion before combining",
                "Dose, stock strength and hydrate form are not specified on this salt-variant page. "
                "Do not import a dose from the linked base formulation.",
                page,
                "sterile Sodium Thiosulfate",
                "Agar media, step 6",
            )
        ]
    return claims


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    inventory = json.loads(args.inventory.read_text())
    if inventory["summary"]["queue_sha256"] != QUEUE_SHA:
        raise ValueError("manual decisions belong to a different queue")
    records, variants = {}, defaultdict(dict)
    dispositions = []
    for number, changes in reviewed_claims().items():
        row = inventory["rows"][number - 1]
        path = "data/normalized_yaml/" + row["source_path"]
        if hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != row["source_sha256"]:
            raise ValueError("source changed: " + path)
        record = records.setdefault(
            path,
            {
                "path": path,
                "recipe_id": row["recipe_id"],
                "expected_sha256": row["source_sha256"],
                "variants": [],
            },
        )
        vi = int(row["variant_index"])
        if vi not in variants[path]:
            variant = {
                "variant_index": vi,
                "variant_name": row["variant_name"],
                "ingredient_changes": [],
            }
            variants[path][vi] = variant
            record["variants"].append(variant)
        for change in changes:
            change["source_modification_index"] = int(row["modification_index"])
            change["source_text"] = row["modification_text"]
            variants[path][vi]["ingredient_changes"].append(change)
        dispositions.append(
            {
                "queue_row_number": number,
                "status": "STRUCTURED",
                "reason": "Named inputs retained with literal preparation basis and optional variant scope.",
                "assertion_count": len(changes),
            }
        )
    payload = {
        "schema_version": 1,
        "source_queue_sha256": QUEUE_SHA,
        "scope": "UTEX optional preparations; claim-scoped agent review, not whole-record human certification",
        "records": sorted(records.values(), key=lambda item: item["path"]),
        "dispositions": sorted(dispositions, key=lambda item: item["queue_row_number"]),
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(payload, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    print(
        json.dumps(
            {
                "records": len(records),
                "rows": len(dispositions),
                "assertions": sum(row["assertion_count"] for row in dispositions),
            }
        )
    )


if __name__ == "__main__":
    main()
