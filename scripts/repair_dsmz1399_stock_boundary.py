#!/usr/bin/env python3
"""Preview/apply the source-verified DSMZ 1399 stock and drop-dose repair."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from decimal import Decimal
from pathlib import Path

import yaml
from fetch_solution_concentration_sources import read_capture
from repair_mediadive_stock_concentration_evidence import cell, exact_object, require, sha
from review_solution_concentration_evidence import field_name, render

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
MEDIUM_PATH = "data/normalized_yaml/archaea/DSMZ_1399_HALOPHILIC_MEDIUM.yaml"
STOCK_PATH = "data/normalized_yaml/bacterial/mediadive_2838_Total_Salts.yaml"
TARGETS = {
    MEDIUM_PATH: (
        "CultureMech:000252",
        "MediaRecipe",
        "fd3f20aadf89a81037ca0aa3b83c0791da7f930c27aa55b694a74a75db2911d5",
    ),
    STOCK_PATH: (
        "CultureMech:012117",
        "SolutionRecipe",
        "d8bd7590843678515ad808708d60fa995e0b8ec789a3b1f2c34ea8b6edfe27da",
    ),
}
MEDIUM = "https://mediadive.dsmz.de/rest/medium/1399"
STOCK = "https://mediadive.dsmz.de/rest/solution/2838"
PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1399.pdf"
HASHES = {
    MEDIUM: "692c728d98d3ba582110c22429da51aaa29ff7d6ea11d9fd8fe8a42c2a978e85",
    STOCK: "69a4694739caeb37e043ee8e7e63b187a9f4b9b66514a07707bc56e471f10a09",
    PDF: "c76a8a1d8c4e5da897b13caa810918454efc9258b0b78a433aa14032c3ed8d3e",
}
ACTION = "RESTORED_DSMZ1399_STOCK_BOUNDARY_AND_DROP_DOSE"
DROP_NOTE = (
    "Source dose: 9 drops of FeCl3 x 6 H2O solution (source attribute: 0,5 %) "
    "per prepared Total Salts stock batch. Percentage basis and drop volume are "
    "unspecified; no g/L, molarity, or mL conversion is asserted."
)


def captures(folder):
    raw = (folder / "medium-1399.json").read_bytes()
    require(sha(raw) == HASHES[MEDIUM], "Medium capture changed")
    require(sha((folder / "DSMZ_Medium1399.pdf").read_bytes()) == HASHES[PDF], "PDF changed")
    stock_raw, meta = read_capture(folder / "sources", 2838)
    require(meta["sha256"] == HASHES[STOCK], "Stock capture changed")
    payload = json.loads(raw)
    require(payload["status"] == 200 and payload["count"] == 1, "Wrong medium envelope")
    source = payload["data"]
    require(source["medium"]["id"] == 1399, "Wrong medium ID")
    require(source["medium"]["name"] == "HALOPHILIC MEDIUM", "Wrong medium name")
    require(
        source["medium"]["source"] == "DSMZ" and source["medium"]["link"] == PDF, "Wrong lineage"
    )
    require([s["id"] for s in source["solutions"]] == [2837, 2838], "Stock boundary drift")
    main, stock = source["solutions"]
    standalone = json.loads(stock_raw)["data"]
    require(main["volume"] == stock["volume"] == standalone["volume"] == 1000, "Volume drift")
    require(
        main["name"] == "Main sol. 1399" and stock["name"] == standalone["name"] == "Total Salts",
        "Name drift",
    )
    require(standalone["steps"] == [], "Unreviewed stock preparation")
    require(len(stock["recipe"]) == len(standalone["recipe"]) == 9, "Stock inventory drift")
    for embedded, row in zip(stock["recipe"], standalone["recipe"], strict=True):
        for key in (
            "compound_id",
            "compound",
            "amount",
            "unit",
            "g_l",
            "attribute",
            "condition",
            "optional",
            "solution_id",
        ):
            require(embedded.get(key) == row.get(key), f"Medium/stock disagree: {key}")
    return {MEDIUM: raw.decode(), STOCK: stock_raw}, main, stock


def claim(
    node, old_pointer, pointer, status, row, raw, locator, explanation, reference=MEDIUM, old=None
):
    quote = exact_object(raw, row)
    field = field_name(pointer + ["concentration"])
    explanation = (
        f"Concentration/formulation evidence for {field} ({node['preferred_term']}); "
        f"locator={locator}. {explanation} Retrieved 2026-10-07; "
        f"response SHA256={HASHES[reference]}. Original DSMZ 1399 PDF was visually checked: {PDF}; "
        "the PDF copyright year is not asserted as publication year."
    )
    return {
        "old_pointer": old_pointer,
        "pointer": pointer,
        "field": field,
        "ingredient": node["preferred_term"],
        "old": old,
        "new": copy.deepcopy(node.get("concentration")),
        "status": status,
        "reference": reference,
        "snippet": quote,
        "locator": locator,
        "explanation": explanation,
    }


def attach(node, item):
    require(
        not any(e["reference"] == item["reference"] for e in node.get("evidence", [])),
        "Existing evidence needs reconciliation",
    )
    node.setdefault("evidence", []).append(
        {
            "reference": item["reference"],
            "supports": "SUPPORT",
            "snippet": item["snippet"],
            "explanation": item["explanation"],
        }
    )


def mass_check(node, row):
    require(node["preferred_term"] == row["compound"], "Chemical form drift")
    require(row["unit"] == "g" and row["optional"] == 0, "Mass context drift")
    require(set(node["concentration"]) == {"value", "unit"}, "Local denominator drift")
    require(node["concentration"]["unit"] == "G_PER_L", "Local mass unit drift")
    require(
        Decimal(node["concentration"]["value"])
        == Decimal(str(row["amount"]))
        == Decimal(str(row["g_l"])),
        "Mass amount drift",
    )


def drop_check(node, row, old_unit):
    require(node["preferred_term"] == row["compound"] == "FeCl3 x 6 H2O", "Iron form drift")
    require(
        row["compound_id"] == 82 and row["amount"] == 9 and row["unit"] == "drops",
        "Drop dose drift",
    )
    require(row.get("attribute") == "0,5 %" and row["optional"] == 0, "Iron strength context drift")
    require(node["concentration"] == {"value": "9", "unit": old_unit}, "Local iron quantity drift")
    require(not node.get("notes"), "Existing iron notes need reconciliation")


def build(doc, path, sources, main, stock, timestamp):
    identifier, target_class, _ = TARGETS[path]
    require(doc["id"] == identifier, "Stable ID drift")
    require(not list(validate_recipe(doc, target_class=target_class)), "Baseline schema failure")
    after = copy.deepcopy(doc)
    raw = sources[MEDIUM]
    claims = []
    rows = stock["recipe"]
    require(
        [r["compound_id"] for r in rows] == [43, 79, 8, 7, 61, 353, 55, 82, 4],
        "Stock ingredient order drift",
    )
    if path == MEDIUM_PATH:
        require(
            doc["media_term"]["term"]["id"] == "mediadive.medium:1399" and PDF in doc["notes"],
            "Local lineage drift",
        )
        require(doc["physical_state"] == "SOLID_AGAR", "Agar formulation drift")
        require(
            len(doc["ingredients"]) == 12 and not doc.get("solutions") and not doc.get("variants"),
            "Local structure drift",
        )
        require(
            [r.get("compound_id", r.get("solution_id")) for r in main["recipe"]]
            == [316, 16, 5, 2838, 4, 3],
            "Main ingredient inventory drift",
        )
        dose = main["recipe"][3]
        require(
            dose
            == {
                "recipe_order": 4,
                "solution": "Total Salts",
                "solution_id": 2838,
                "amount": 666,
                "unit": "ml",
                "optional": 0,
            },
            "Stock dose drift",
        )
        require(
            len(main["steps"]) == 1
            and main["steps"][0]["step"] == doc["preparation_steps"][0]["description"],
            "Preparation drift",
        )
        after["ingredients"] = after["ingredients"][:4]
        for index, source_index in enumerate((0, 1, 2, 5)):
            node, row = after["ingredients"][index], main["recipe"][source_index]
            mass_check(node, row)
            context = ""
            if index == 0:
                require(
                    row.get("attribute") == "Difco" and not node.get("notes"), "Peptone grade drift"
                )
                node["notes"] = "Source material: Proteose peptone no. 3 (Difco)."
                context = "The source manufacturer/grade attribute Difco is retained in notes. "
            elif index == 3:
                require(row.get("condition") == "for solid medium", "Agar condition drift")
                context = "Applies to this record's SOLID_AGAR formulation; optional solidification is not asserted for liquid medium. "
            else:
                require(
                    not row.get("attribute") and not row.get("condition"), "Unreviewed mass context"
                )
            item = claim(
                node,
                ["ingredients", index],
                ["ingredients", index],
                "evidence_only",
                row,
                raw,
                f"$.data.solutions[0].recipe[{source_index}]",
                context
                + f"Existing {row['g_l']} g/L is explicitly reported. {row['amount']} g / (1000 ml / 1000 ml per L) = {row['g_l']} g/L. "
                "Exact final-volume instruction in $.data.solutions[0].steps[0].step: Make up to 1000.0 ml.",
                old=copy.deepcopy(node["concentration"]),
            )
            attach(node, item)
            claims.append(item)
        components = copy.deepcopy(doc["ingredients"][4:])
        after["solutions"] = [
            {
                "preferred_term": "Total Salts",
                "term": {"id": "mediadive.solution:2838", "label": "Total Salts"},
                "concentration": {"value": "0.666", "unit": "L"},
                "composition": components,
            }
        ]
        for index, node in enumerate(components):
            row = rows[index]
            old = copy.deepcopy(node["concentration"])
            if index < 7:
                mass_check(node, row)
                require(
                    not row.get("attribute") and not row.get("condition"), "Unreviewed salt context"
                )
                explanation = (
                    f"Moved from ingredients[{index + 4}] into stock 2838, explicitly linked in the receiving recipe. "
                    f"The unchanged {row['g_l']} g/L value is the provider-declared stock concentration: {row['amount']} g / (1000 ml / 1000 ml per L) = {row['g_l']} g/L. "
                    'Additional exact stock excerpt at $.data.solutions[1].volume: "volume": 1000. '
                    "This is not the concentration after adding 666 ml stock to the medium; no dilution is asserted."
                )
            else:
                drop_check(node, row, "G_PER_L")
                node.pop("concentration")
                node["notes"] = DROP_NOTE
                explanation = (
                    "Moved into the exact stock and removed unsupported 9 g/L. The source dose is retained in notes, not VARIABLE or a guessed conversion. "
                    + DROP_NOTE
                )
            item = claim(
                node,
                ["ingredients", index + 4],
                ["solutions", 0, "composition", index],
                "correct",
                row,
                raw,
                f"$.data.solutions[1].recipe[{index}]",
                explanation,
                old=old,
            )
            attach(node, item)
            claims.append(item)
        for pointer, row, source_index, expected in (
            (["ingredients", 4], main["recipe"][4], 0, 333),
            (["solutions", 0, "composition", 8], rows[8], 1, 1000),
        ):
            require(
                row["compound_id"] == 4
                and row["compound"] == "Distilled water"
                and row["amount"] == expected
                and row["unit"] == "ml"
                and row["optional"] == 0,
                "Water dose drift",
            )
            node = {
                "preferred_term": "Distilled water",
                "term": {"id": "mediadive.compound:4", "label": "Distilled water"},
                "concentration": {"value": str(Decimal(expected) / 1000), "unit": "L"},
            }
            item = claim(
                node,
                None,
                pointer,
                "add",
                row,
                raw,
                f"$.data.solutions[{source_index}].recipe[{4 if source_index == 0 else 8}]",
                f"Explicit {expected} ml water addition / 1000 = {Decimal(expected) / 1000} L per batch at this preparation stage. "
                "Not a percentage or receiving-medium concentration; the main recipe's separate make-up instruction is retained.",
            )
            attach(node, item)
            (after["ingredients"] if source_index == 0 else components).append(node)
            claims.append(item)
        item = claim(
            after["solutions"][0],
            None,
            ["solutions", 0],
            "add",
            dose,
            raw,
            "$.data.solutions[0].recipe[3]",
            "666 ml / 1000 = 0.666 L of stock 2838 per receiving batch. This dose establishes the stock boundary; salt entries in solutions[0].composition belong to this stock, not direct ingredients. "
            "The separate main-medium make-up instruction is retained; this is not an assumed per-liter dose.",
        )
        attach(after, item)
        claims.append(item)
    else:
        require(
            doc["term"] == {"id": "mediadive.solution:2838", "label": "Total Salts"},
            "Local stock identity drift",
        )
        require(len(doc["composition"]) == 9, "Local stock inventory drift")
        for index, node in enumerate(after["composition"]):
            row = rows[index]
            old = copy.deepcopy(node.get("concentration"))
            if index == 7:
                drop_check(node, row, "VARIABLE")
                node.pop("concentration")
                node["notes"] = DROP_NOTE
                item = claim(
                    node,
                    ["composition", index],
                    ["composition", index],
                    "correct",
                    row,
                    raw,
                    "$.data.solutions[1].recipe[7]",
                    "Removed ambiguous 9 VARIABLE; preserved exact source drop dose and strength attribute in notes. "
                    + DROP_NOTE,
                    old=old,
                )
                attach(node, item)
            else:
                evidence = [e for e in node.get("evidence", []) if e["reference"] == STOCK]
                require(
                    len(evidence) == 1 and evidence[0]["snippet"] in sources[STOCK],
                    "Earlier stock evidence lost",
                )
                item = {
                    "old_pointer": ["composition", index],
                    "pointer": ["composition", index],
                    "field": f"composition[{index}].concentration",
                    "ingredient": node["preferred_term"],
                    "old": old,
                    "new": copy.deepcopy(old),
                    "status": "verified",
                    "reference": STOCK,
                    "snippet": evidence[0]["snippet"],
                    "locator": f"$.data.recipe[{index}]",
                    "explanation": evidence[0]["explanation"],
                }
            claims.append(item)
        require(
            doc.get("ingredients")
            == [
                {
                    "preferred_term": "See source for composition",
                    "concentration": {"value": "variable", "unit": "VARIABLE"},
                }
            ],
            "Placeholder drift",
        )
        claims.append(
            {
                "old_pointer": ["ingredients", 0],
                "pointer": ["ingredients", 0],
                "field": "ingredients[0].concentration",
                "ingredient": "See source for composition",
                "old": doc["ingredients"][0]["concentration"],
                "new": doc["ingredients"][0]["concentration"],
                "status": "unsupported",
                "reference": None,
                "snippet": None,
                "locator": None,
                "explanation": "Legacy placeholder retained, not promoted to a concentration claim.",
            }
        )
    for reference, title, source_type in (
        (MEDIUM, "MediaDive 1399: HALOPHILIC MEDIUM", "dataset"),
        (PDF, "DSMZ 1399. HALOPHILIC MEDIUM", "culture_collection_page"),
    ):
        require(
            not any(r["reference"] == reference for r in after.get("references", [])),
            "Reference already present",
        )
        after.setdefault("references", []).append(
            {
                "reference": reference,
                "title": title,
                "notes": f"source_type={source_type}; discovery_mode=existing_record_reference; accessed_on=2026-10-07; source_organization=DSMZ; response_sha256={HASHES[reference]}; "
                "individual authors and publication year not established; PDF copyright date is not publication date.",
            }
        )
    changes = [c for c in claims if c["status"] in {"correct", "add", "evidence_only"}]
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source=f"{MEDIUM}; {STOCK}; {PDF}",
        notes="Exact medium/stock source identity and original PDF checked. Iron drop dose/percent attribute retained without conversion; percentage basis and drop volume remain unknown.",
        changes="; ".join(
            f"{c['old_pointer']} -> {c['field']}: {c['old']} -> {c['new']} ({c['status']})"
            for c in changes
        ),
    )
    require(not list(validate_recipe(after, target_class=target_class)), "Proposed schema failure")
    return after, claims


def reports(folder, plan, applied):
    folder.mkdir(parents=True, exist_ok=True)
    for item in plan["records"]:
        medium = item["path"] == MEDIUM_PATH
        lines = [
            "# DSMZ 1399 Stock-Boundary Review",
            "",
            f"- {'Record' if medium else 'Follow-up target'}: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: `{plan['commit']}`",
            f"- Before SHA256: `{item['before_sha256']}`",
            f"- Result SHA256: `{item['after_sha256']}`",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "The exact source PDF/JSON and preparation boundaries were inspected. Schema checks are not scientific proof. "
            "The drop unit is retained in notes; its volume and the percentage basis remain unknown. No final iron concentration is asserted.",
            "",
            "| Field | Old field | Ingredient | Old | New | Status | DOI/PURL | Exact snippet | Locator | Decision / calculation |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for c in item["claims"]:
            lines.append(
                "| "
                + " | ".join(
                    cell(c[k])
                    for k in (
                        "field",
                        "old_pointer",
                        "ingredient",
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
        if not medium:
            lines += [
                "",
                "This supplements the existing single per-record source-pass report; it is not another unique reviewed path.",
            ]
        lines += [
            "",
            "Baseline and proposed closed-schema checks passed. See the [batch validation](README.md#verification) "
            "for post-apply read-back, corpus checks, and unavailable external validators.",
        ]
        (folder / ("medium.md" if medium else "stock-followup.md")).write_text(
            "\n".join(lines) + "\n"
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--reports", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--verify", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    sources, main_source, stock = captures(args.source_dir)
    tracked = set(
        subprocess.check_output(["git", "ls-files", "-z", "data/normalized_yaml"], cwd=ROOT)
        .decode()
        .split("\0")
    )
    for path in TARGETS:
        require(path in tracked and not (ROOT / path).is_symlink(), "Non-exact or symlink target")
    if args.apply or args.verify:
        plan = json.loads(args.plan.read_text())
        require(
            plan["version"] == 1 and plan["action"] == ACTION and plan["source_hashes"] == HASHES,
            "Wrong plan",
        )
        require([r["path"] for r in plan["records"]] == list(TARGETS), "Wrong plan targets")
    else:
        require(not args.plan.exists(), "Do not overwrite reviewed plan")
        plan = {
            "version": 1,
            "action": ACTION,
            "source_hashes": HASHES,
            "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT)
            .decode()
            .strip(),
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "records": [],
        }
    pending, snippets, already = [], 0, 0
    for index, (path, (identifier, _, before_sha)) in enumerate(TARGETS.items()):
        current = (ROOT / path).read_bytes()
        before = (
            plan["records"][index]["before_text"].encode() if args.apply or args.verify else current
        )
        require(sha(before) == before_sha, "Unreviewed baseline")
        doc = yaml.load(before, Loader=yaml.CSafeLoader)
        after, claims = build(doc, path, sources, main_source, stock, plan["created_at"])
        output = render(before.decode(), after)
        item = {
            "path": path,
            "id": identifier,
            "before_sha256": before_sha,
            "before_text": before.decode(),
            "after_sha256": sha(output),
            "claims": claims,
        }
        if args.apply or args.verify:
            require(item == plan["records"][index], "Plan drift")
            require(current in (before, output), "Concurrent record edit")
            if current == output:
                already += 1
            else:
                require(not args.verify, "Not applied")
                pending.append((ROOT / path, current, output))
        else:
            plan["records"].append(item)
        for c in claims:
            if c["status"] in {"correct", "add", "evidence_only"}:
                require(c["snippet"] in sources[c["reference"]], "Inexact source snippet")
                snippets += 1
    for path, before, _ in pending:
        require(path.read_bytes() == before, "Concurrent edit before batch write")
    for path, before, output in pending:
        require(path.read_bytes() == before, "Concurrent edit during batch write")
        path.write_bytes(output)
    if not (args.apply or args.verify):
        args.plan.parent.mkdir(parents=True, exist_ok=True)
        args.plan.write_text(json.dumps(plan, indent=2) + "\n")
    if args.reports:
        reports(args.reports, plan, args.apply or args.verify)
    print(
        json.dumps(
            {
                "records": 2,
                "changed": len(pending),
                "already_applied": already,
                "new_evidence_entries": snippets,
                "mode": "verify" if args.verify else "apply" if args.apply else "preview",
            }
        )
    )


if __name__ == "__main__":
    main()
