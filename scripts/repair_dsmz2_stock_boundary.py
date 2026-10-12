#!/usr/bin/env python3
"""Guarded source-backed restoration of DSMZ 2's DSMZ 1 base and preparation stage."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from pathlib import Path

from fetch_medium_concentration_sources import API, read_capture
from fetch_solution_concentration_sources import load_yaml
from repair_mediadive_stock_concentration_evidence import cell, require, sha
from review_medium_concentration_evidence import json_excerpt
from review_solution_concentration_evidence import field_name, get_node, render

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
TARGET = "data/normalized_yaml/bacterial/bacillus_pasteurii_medium.yaml"
IDENTIFIER = "CultureMech:001399"
BASELINE = "5012a43264d5ada50e60cd988cb7deac3c0830e88d1ce1a6b32c8307b6deaa6a"
ACTION = "RESTORED_DSMZ2_BASE_MEDIUM_AND_PREPARATION_STAGE"
MEDIUM = API + "2"
BASE = API + "1"
PDFS = {i: f"https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium{i}.pdf" for i in (1, 2)}
HASHES = {
    MEDIUM: "e0812b7c4942b14a6de12c5d21195eb8cadbcad1965e5364657a61291f0f61ea",
    BASE: "96b8496db5025086f2407d1e2e2738ad74250909ec172a4a76c42ca22a96e319",
    PDFS[1]: "95916f2ec73cf9a2d87acccb06e39eb6eb38f282b63cea53b6f5ad6441adaf7f",
    PDFS[2]: "2216960d2564bff726b3b45c9f4a3e5d84d5a549cff3bb548c74a118de1e56c9",
}


def captures(folder):
    raws, metadata = {}, {}
    for mid in (1, 2):
        reference = API + str(mid)
        raws[reference], metadata[reference] = read_capture(folder / "sources", str(mid))
        require(metadata[reference]["sha256"] == HASHES[reference], "API capture changed")
        require(
            sha((folder / f"DSMZ_Medium{mid}.pdf").read_bytes()) == HASHES[PDFS[mid]], "PDF changed"
        )
    return raws, metadata


def build(doc, raws, metadata, timestamp):
    require(doc["id"] == IDENTIFIER, "Stable ID drift")
    require(not list(validate_recipe(doc, target_class="MediaRecipe")), "Baseline schema failure")
    data = json.loads(raws[MEDIUM])["data"]
    base_data = json.loads(raws[BASE])["data"]
    for source, mid, name in (
        (data, 2, "BACILLUS PASTEURII MEDIUM"),
        (base_data, 1, "NUTRIENT AGAR"),
    ):
        require(
            source["medium"]["id"] == mid and source["medium"]["name"] == name,
            "Source identity drift",
        )
        require(
            source["medium"]["source"] == "DSMZ" and source["medium"]["link"] == PDFS[mid],
            "Source lineage drift",
        )
    require([s["id"] for s in data["solutions"]] == [4, 1], "Source stock topology drift")
    require(len(base_data["solutions"]) == 1, "Base formulation drift")
    main, stock = data["solutions"]
    require(
        stock == base_data["solutions"][0], "Receiving-medium base differs from exact base recipe"
    )
    require(
        main["name"] == "Main sol. 2" and stock["name"] == "Main sol. 1",
        "Source solution name drift",
    )
    require(main["volume"] == stock["volume"] == 1000, "Provider volume drift")
    require(
        doc["media_term"]["term"] == {"id": "mediadive.medium:2", "label": data["medium"]["name"]},
        "Local lineage drift",
    )
    require(
        doc["original_name"] == data["medium"]["name"] and PDFS[2] in doc["notes"],
        "Local source name/link drift",
    )
    require(doc["physical_state"] == "SOLID_AGAR", "Agar formulation drift")
    require(not doc.get("solutions") and not doc.get("variants"), "Unreviewed local structure")
    require(
        [n["preferred_term"] for n in doc["ingredients"]]
        == ["Urea", "Peptone", "Meat extract", "Agar"],
        "Local ingredient order/form drift",
    )
    require(
        len(main["recipe"]) == 2 and [r["compound_id"] for r in stock["recipe"]] == [1, 2, 3, 4],
        "Source ingredient inventory drift",
    )
    dose = main["recipe"][0]
    require(
        dose
        == {
            "recipe_order": 1,
            "solution": "Main sol. 1",
            "solution_id": 1,
            "amount": 1000,
            "unit": "ml",
            "optional": 0,
        },
        "Base dose drift",
    )
    require(len(main["steps"]) == len(stock["steps"]) == 2, "Source preparation inventory drift")
    descriptions = [s["step"] for s in main["steps"] + stock["steps"]]
    require(
        [s["description"] for s in doc["preparation_steps"]] == descriptions,
        "Local preparation text drift",
    )
    require(
        [s["step_number"] for s in doc["preparation_steps"]] == [1, 2, 3, 4],
        "Local preparation order drift",
    )
    require(
        [s["action"] for s in doc["preparation_steps"]] == ["ADJUST_PH", "MIX", "ADJUST_PH", "MIX"],
        "Local preparation action drift",
    )
    require(
        descriptions[0]
        == "To medium 1 add 20 g/l urea before autoclaving. Do not adjust pH; pH raises to about 8 due to heat degraded urea.",
        "Main preparation drift",
    )
    require(
        descriptions[1] == "For sporulation enhancement add 10 mg/l MnSO4 x H2O.",
        "Conditional supplement drift",
    )
    require(descriptions[2] == "Adjust pH to 7.0.", "Base pH instruction drift")
    require(
        descriptions[3]
        == "For Bacillus strains the addition of 10.0 mg MnSO4 x H2O is recommended for sporulation.",
        "Base supplement context drift",
    )

    after = copy.deepcopy(doc)
    after["ingredients"] = after["ingredients"][:1]
    components = copy.deepcopy(doc["ingredients"][1:])
    after["solutions"] = [
        {
            "preferred_term": stock["name"],
            "term": {"id": "mediadive.solution:1", "label": stock["name"]},
            "composition": components,
            "concentration": {"value": "1", "unit": "L"},
            "preparation_notes": "\n\n".join(descriptions[2:]),
        }
    ]
    after["preparation_steps"] = after["preparation_steps"][:2]
    after["preparation_steps"][0]["action"] = "MIX"
    claims = []

    def add_claim(pointer, old_pointer, status, source_pointer, explanation, evidence_pointer):
        snippet = json_excerpt(raws[MEDIUM], source_pointer)
        item = {
            "pointer": pointer,
            "old_pointer": old_pointer,
            "field": field_name(pointer),
            "status": status,
            "old": copy.deepcopy(get_node(doc, old_pointer)) if old_pointer is not None else None,
            "new": copy.deepcopy(get_node(after, pointer)),
            "reference": MEDIUM,
            "snippet": snippet,
            "locator": "$." + field_name(source_pointer),
            "source_pointer": source_pointer,
            "evidence_pointer": evidence_pointer,
            "explanation": explanation,
        }
        claims.append(item)
        return item

    for index, row in enumerate([main["recipe"][1]] + stock["recipe"][:3]):
        node = after["ingredients"][0] if index == 0 else components[index - 1]
        require(node["preferred_term"] == row["compound"], "Chemical form drift")
        require(row["optional"] == 0 and not row.get("attribute"), "Conditional/attribute drift")
        require(
            row.get("condition") == ("for solid medium" if index == 3 else None),
            "Agar condition drift",
        )
        require(row["compound_id"] == [339, 1, 2, 3][index], "Compound ID drift")
        require(row["unit"] == ("g/l" if index == 0 else "g"), "Source mass unit drift")
        require(row["amount"] == row["g_l"] == [20, 5, 3, 15][index], "Source mass amount drift")
        require(
            node["concentration"] == {"value": str(row["g_l"]), "unit": "G_PER_L"},
            "Local concentration drift",
        )
        parent = ["ingredients", 0] if index == 0 else ["solutions", 0, "composition", index - 1]
        source_pointer = (
            ["data", "solutions", 0, "recipe", 1]
            if index == 0
            else ["data", "solutions", 1, "recipe", index - 1]
        )
        explanation = (
            "The source explicitly states 20 g/l urea; no additional volume division is performed."
            if index == 0
            else f"Relocated from ingredients[{index}] into the explicitly linked DSMZ 1 base (solution 1), not inferred from a shared name. "
            f"The unchanged {row['g_l']} g/L is the provider-declared base concentration: {row['amount']} g / (1000 ml / 1000 ml per L). "
            "Additional exact value at $.data.solutions[1].volume (ml): 1000. "
            "No independently measured receiving-medium final volume or dilution is asserted."
        )
        if index == 3:
            explanation += " Source condition 'for solid medium' applies to this record's SOLID_AGAR state; the original note is preserved."
        add_claim(
            parent + ["concentration"],
            ["ingredients", index, "concentration"],
            "evidence_only" if index == 0 else "relocate",
            source_pointer,
            explanation,
            parent,
        )
    water_row = stock["recipe"][3]
    require(
        water_row
        == {
            "recipe_order": 4,
            "compound": "Distilled water",
            "compound_id": 4,
            "amount": 1000,
            "unit": "ml",
            "optional": 0,
        },
        "Base water dose drift",
    )
    components.append(
        {
            "preferred_term": "Distilled water",
            "term": {"id": "mediadive.compound:4", "label": "Distilled water"},
            "concentration": {"value": "1", "unit": "L"},
        }
    )
    add_claim(
        ["solutions", 0, "composition", 3, "concentration"],
        None,
        "add",
        ["data", "solutions", 1, "recipe", 3],
        "Explicit 1000 ml water / 1000 ml per L = 1 L per prepared base batch. This is a batch addition, not an inferred final volume or percentage.",
        ["solutions", 0, "composition", 3],
    )
    add_claim(
        ["solutions", 0, "concentration"],
        None,
        "add",
        ["data", "solutions", 0, "recipe", 0],
        "Explicit 1000 ml of Main sol. 1 / 1000 ml per L = 1 L per receiving batch. This source link establishes the base boundary and its three relocated ingredients; it is not a stock dose inferred from another medium.",
        [],
    )
    add_claim(
        ["preparation_steps", 0, "action"],
        ["preparation_steps", 0, "action"],
        "correct_stage",
        ["data", "solutions", 0, "steps", 0],
        "The operation adds urea and explicitly prohibits pH adjustment at this stage. MIX replaces the misleading ADJUST_PH action; the original description and conditional sporulation instruction remain unchanged.",
        [],
    )
    add_claim(
        ["solutions", 0, "preparation_notes"],
        None,
        "correct_stage",
        ["data", "solutions", 1, "steps"],
        "The exact texts formerly at preparation_steps[2:4] belong to preparation of base solution 1. They are moved verbatim into this stock's preparation_notes and removed from the main procedure, so base pH adjustment is not applied after the urea instruction. The conditional Bacillus supplement remains conditional prose, not a mandatory ingredient.",
        [],
    )
    claims[-1]["old"] = copy.deepcopy(doc["preparation_steps"][2:])
    claims[-1]["old_field"] = "preparation_steps[2:4]"

    grouped = {}
    for claim in claims:
        grouped.setdefault(tuple(claim["evidence_pointer"]), []).append(claim)
    for pointer, group in grouped.items():
        node = get_node(after, pointer)
        require(
            not any(e["reference"] == MEDIUM for e in node.get("evidence", [])),
            "Existing same-source evidence needs reconciliation",
        )
        explanations = []
        for index, claim in enumerate(group):
            text = f"{claim['field']} ({claim['status']}), locator={claim['locator']}: {claim['explanation']}"
            if index:
                text += f" Additional exact excerpt: {claim['snippet']}"
            explanations.append(text)
        explanations.append(
            f"Source retrieved {metadata[MEDIUM]['accessed_at']}; response SHA256={HASHES[MEDIUM]}. Exact base source independently cross-checked at {BASE} (SHA256={HASHES[BASE]}). Original DSMZ 1 and 2 PDFs visually checked. Secondary chemical mappings were preserved, not revalidated."
        )
        node.setdefault("evidence", []).append(
            {
                "reference": MEDIUM,
                "supports": "SUPPORT",
                "snippet": group[0]["snippet"],
                "explanation": " ".join(explanations),
            }
        )
    for reference, title, kind in (
        (MEDIUM, "MediaDive medium 2: BACILLUS PASTEURII MEDIUM", "dataset"),
        (BASE, "MediaDive medium 1: NUTRIENT AGAR", "dataset"),
        (PDFS[2], "DSMZ 2. BACILLUS PASTEURII MEDIUM", "culture_collection_page"),
        (PDFS[1], "DSMZ 1. NUTRIENT AGAR", "culture_collection_page"),
    ):
        require(
            not any(r["reference"] == reference for r in after.get("references", [])),
            "Existing bibliography needs reconciliation",
        )
        after.setdefault("references", []).append(
            {
                "reference": reference,
                "title": title,
                "notes": f"source_type={kind}; discovery_mode=existing_record_reference; source_organization=DSMZ; accessed_on=2026-10-07; response_sha256={HASHES[reference]}; individual authors and publication year not established; PDF copyright year is not a publication date.",
            }
        )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        source="; ".join(HASHES),
        timestamp=timestamp,
        notes="Exact source identity, base recipe, original PDFs, and preparation-stage instructions verified. Three ingredients relocated with their identifiers and amounts preserved; two explicit batch-volume slots added. Conditional sporulation supplement not promoted to a mandatory ingredient.",
        changes="; ".join(
            f"{c.get('old_field', c['old_pointer'])} -> {c['field']}: {c['old']} -> {c['new']} ({c['status']})"
            for c in claims
        ),
    )
    require(not list(validate_recipe(after, target_class="MediaRecipe")), "Proposed schema failure")
    return after, claims


def process(root, folder, plan_path, mode):
    raws, metadata = captures(folder)
    tracked = set(
        subprocess.check_output(["git", "ls-files", "-z", "data/normalized_yaml"], cwd=root)
        .decode()
        .split("\0")
    )
    target = root / TARGET
    require(TARGET in tracked and not target.is_symlink(), "Non-exact/symlink target")
    current = target.read_bytes()
    if mode == "preview":
        require(not plan_path.exists(), "Do not overwrite a reviewed plan")
        before = current
        plan = {
            "version": 1,
            "action": ACTION,
            "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root)
            .decode()
            .strip(),
            "source_hashes": HASHES,
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "records": [],
        }
    else:
        plan = json.loads(plan_path.read_text())
        require(
            plan["version"] == 1 and plan["action"] == ACTION and plan["source_hashes"] == HASHES,
            "Wrong plan",
        )
        require(
            len(plan["records"]) == 1 and plan["records"][0]["path"] == TARGET, "Wrong plan target"
        )
        before = plan["records"][0]["before_text"].encode()
    require(sha(before) == BASELINE, "Unreviewed baseline")
    after, claims = build(load_yaml(before), raws, metadata, plan["created_at"])
    output = render(before.decode(), after)
    item = {
        "path": TARGET,
        "id": IDENTIFIER,
        "before_text": before.decode(),
        "before_sha256": sha(before),
        "after_sha256": sha(output),
        "claims": claims,
    }
    changed = already = 0
    if mode == "preview":
        plan["records"].append(item)
        plan_path.parent.mkdir(parents=True, exist_ok=True)
        plan_path.write_text(json.dumps(plan, indent=2) + "\n")
    else:
        require(item == plan["records"][0], "Plan/source decision drift")
        require(current in (before, output), "Concurrent record edit")
        if current == output:
            already = 1
        else:
            require(mode == "apply", "Repair not applied")
            require(target.read_bytes() == before, "Concurrent edit before write")
            target.write_bytes(output)
            changed = 1
        require(target.read_bytes() == output, "Persisted result differs")
    for claim in claims:
        require(
            claim["snippet"] == json_excerpt(raws[MEDIUM], claim["source_pointer"]),
            "Inexact source excerpt",
        )
        node = get_node(after, claim["evidence_pointer"])
        entries = [e for e in node["evidence"] if e["reference"] == MEDIUM]
        require(
            len(entries) == 1 and claim["field"] in entries[0]["explanation"],
            "Claim scope/evidence lost",
        )
        require(
            claim["snippet"] == entries[0]["snippet"]
            or claim["snippet"] in entries[0]["explanation"],
            "Supporting excerpt lost",
        )
    return plan, {
        "mode": mode,
        "changed": changed,
        "already_applied": already,
        "scoped_claims": len(claims),
        "new_evidence_entries": len({tuple(c["evidence_pointer"]) for c in claims}),
    }


def report(folder, plan, applied):
    item = plan["records"][0]
    lines = [
        "# DSMZ 2 Base-Medium Follow-Up",
        "",
        f"- Follow-up target: {TARGET}",
        f"- ID: {IDENTIFIER}",
        f"- Reviewed commit: `{plan['commit']}`",
        f"- Before SHA256: `{item['before_sha256']}`",
        f"- Result SHA256: `{item['after_sha256']}`",
        f"- State: {'applied locally' if applied else 'preview'}",
        "",
        "This supplements the existing single per-record source-pass report; it is not a new unique reviewed path.",
        "",
        "| Field | Old field | Old | New | Status | DOI/PURL | Exact snippet | Locator | Decision |",
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for c in item["claims"]:
        row = dict(
            c,
            old_field=c.get(
                "old_field", field_name(c["old_pointer"]) if c["old_pointer"] is not None else None
            ),
        )
        lines.append(
            "| "
            + " | ".join(
                cell(row.get(k))
                for k in (
                    "field",
                    "old_field",
                    "old",
                    "new",
                    "status",
                    "reference",
                    "snippet",
                    "locator",
                    "explanation",
                )
            )
            + " |"
        )
    lines += [
        "",
        "The conditional manganese sporulation supplement remains explicit source prose, not a mandatory base ingredient or a newly created variant. No receiving-medium final-volume assumption or new growth claim was introduced.",
        "",
        "See README.md for validation, remaining scope, and merge findings.",
    ]
    folder.mkdir(parents=True, exist_ok=True)
    (folder / "followup.md").write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--reports", type=Path)
    flags = parser.add_mutually_exclusive_group()
    flags.add_argument("--apply", action="store_true")
    flags.add_argument("--verify", action="store_true")
    flags.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    plan, outcome = process(ROOT, args.source_dir, args.plan, mode)
    if args.reports:
        report(args.reports, plan, mode != "preview")
    print(json.dumps(outcome), flush=True)


if __name__ == "__main__":
    main()
