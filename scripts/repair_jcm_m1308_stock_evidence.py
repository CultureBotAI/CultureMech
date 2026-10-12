#!/usr/bin/env python3
"""Attach reviewed stock evidence to M1308 without inferring final-medium amounts."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from decimal import Decimal
from pathlib import Path

import yaml
from repair_mediadive_stock_concentration_evidence import exact_object, require, sha
from review_solution_concentration_evidence import render

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
TARGET = "data/normalized_yaml/bacterial/TOGO_M1308_Methylotroph_Medium.yaml"
BEFORE = "ad5cbfc18e740f41f3e3f601fdd67747f2d0af310bf9c5a79a8d92671f62e1f6"
ACTION = "CURATED_M1308_NESTED_STOCK_EVIDENCE"
JCM = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1219"
MEDIUM = "https://mediadive.dsmz.de/rest/medium/J1219"
SOURCES = {
    "J1219": "ec7bff0980d24724c1052f1e90796ca659808e61f3206a93b61376d2e1dbac67",
    "solution-3981": "f31ddb3c46606d262bb9d8fa48f9ea5d4bab81c8917dc35dce7a7f0da6369a23",
    "solution-3861": "c6829f83ad6e234909db1d65f45a27c24993e0280ff68c4d7355a8f6344335b9",
}
STOCKS = [
    (1, 3981, "Se/W solution (see Medium [M278])", [107, 249]),
    (
        2,
        3861,
        "Trace vitamins (see Medium [M190])",
        [46, 138, 519, 1207, 136, 139, 518, 18, 47, 368],
    ),
]


def captures(folder):
    result = {}
    for key, digest in SOURCES.items():
        raw = (folder / f"ingredient-mediadive-{key}-20261007.json").read_bytes()
        require(sha(raw) == digest, f"Source changed: {key}")
        payload = json.loads(raw)
        require(payload["status"] == 200 and payload["count"] == 1, "Bad source envelope")
        result[key] = (raw.decode(), payload["data"])
    return result


def build(doc, sources, timestamp):
    require(doc["id"] == "CultureMech:007843", "Wrong record ID")
    require(doc["media_term"]["term"]["id"] == "TOGO:M1308", "Wrong TOGO source")
    require(JCM in doc["notes"], "JCM lineage missing")
    after = copy.deepcopy(doc)
    medium_raw, medium = sources["J1219"]
    require(medium["medium"]["id"] == "J1219", "Wrong medium")
    require(medium["medium"]["source"] == "JCM", "Wrong collection")
    require(medium["medium"]["link"] == JCM, "Wrong original recipe link")
    main = [s for s in medium["solutions"] if s["id"] == 5347]
    require(len(main) == 1 and main[0]["name"] == "Main sol. J1219", "Wrong main solution")
    claims = []
    for stock_index, sid, name, ids in STOCKS:
        raw, source = sources[f"solution-{sid}"]
        stock = after["solutions"][stock_index]
        require(stock["preferred_term"] == name, "Wrong nested stock")
        require(stock["concentration"] == {"value": "0.01", "unit": "L"}, "Stock dose drift")
        require(source["id"] == sid and source["volume"] == 1000, "Stock identity/volume drift")
        require(source["steps"] == [], "Stock preparation changed")
        linked = [r for r in main[0]["recipe"] if r.get("solution_id") == sid]
        require(len(linked) == 1, "Ambiguous stock link")
        link = linked[0]
        require(
            link["solution"] == source["name"]
            and link["amount"] == 10
            and link["unit"] == "ml"
            and link["optional"] == 0
            and not link.get("condition")
            and not link.get("attribute"),
            "Stock linkage drift",
        )
        embedded = [s for s in medium["solutions"] if s["id"] == sid]
        require(len(embedded) == 1 and embedded[0]["volume"] == 1000, "Embedded stock drift")
        rows = source["recipe"][:-1]
        require([r["compound_id"] for r in rows] == ids, "Stock ingredient identity/order drift")
        require(source["recipe"][-1]["compound_id"] == 4, "Stock solvent row drift")
        require(len(stock["composition"]) == len(rows), "Nested composition drift")
        link_quote = exact_object(medium_raw, link)
        reference = f"https://mediadive.dsmz.de/rest/solution/{sid}"
        for index, (node, row) in enumerate(zip(stock["composition"], rows, strict=True)):
            require(node["preferred_term"] == row["compound"], "Chemical form/name drift")
            require(not node.get("evidence"), "Existing evidence requires reconciliation")
            require(
                row["optional"] == 0
                and not row["condition"]
                and not row["attribute"]
                and row["solution_id"] is None
                and row["unit"] == "mg",
                "Unreviewed stock context",
            )
            embedded_rows = [
                r for r in embedded[0]["recipe"] if r.get("compound_id") == row["compound_id"]
            ]
            require(len(embedded_rows) == 1, "Ambiguous embedded compound")
            for key in ("compound", "amount", "unit", "g_l", "optional"):
                require(embedded_rows[0][key] == row[key], "Medium/stock sources disagree")
            old = node["concentration"]
            concentration_mg = Decimal(str(row["g_l"])) * 1000
            require(
                set(old) == {"value", "unit"}
                and old["unit"] == "MG_PER_L"
                and Decimal(old["value"]) == concentration_mg == Decimal(str(row["amount"])),
                "Existing stock concentration conflicts with source",
            )
            field = f"solutions[{stock_index}].composition[{index}].concentration"
            snippet = exact_object(raw, row)
            explanation = (
                f"Concentration evidence for {field} ({node['preferred_term']}) within the stock. "
                f"MediaDive explicitly reports g_l={row['g_l']}; {row['g_l']} g/L * 1000 mg/g "
                f"= {concentration_mg} mg/L, matching the unchanged local value. "
                f"Cross-check: {row['amount']} mg / (1000 ml / 1000 ml per L) = {concentration_mg} mg/L. "
                f'Additional exact excerpt at $.data.volume: "volume": 1000. '
                f"Locator=$.data.recipe[{index}] (compound_id={row['compound_id']}); "
                f"response SHA256={SOURCES[f'solution-{sid}']}; accessed 2026-10-07. "
                "This supports provider-declared stock concentration, not an independently measured "
                "final volume, a dilution into the receiving medium, or either inline variant. "
                f"The exact receiving-recipe link is {MEDIUM}, $.data.solutions[0].recipe "
                f"where solution_id={sid}; additional exact excerpt: {link_quote}. "
                f"Medium response SHA256={SOURCES['J1219']}; it identifies original recipe {JCM}. "
                "JCM 1219's cross-reference and the linked JCM stock table were manually checked."
            )
            node["evidence"] = [
                {
                    "reference": reference,
                    "supports": "SUPPORT",
                    "snippet": snippet,
                    "explanation": explanation,
                }
            ]
            claims.append(
                {
                    "pointer": ["solutions", stock_index, "composition", index],
                    "field": field,
                    "ingredient": node["preferred_term"],
                    "old": copy.deepcopy(old),
                    "new": copy.deepcopy(old),
                    "status": "evidence_only",
                    "reference": reference,
                    "snippet": snippet,
                    "explanation": explanation,
                }
            )
        after["references"].append(
            {
                "reference": reference,
                "title": f"MediaDive solution {sid}: {source['name']}",
                "notes": "source_type=dataset; discovery_mode=cross_reference; accessed_on=2026-10-07; "
                f"source_organization=DSMZ; linked from JCM 1219; response_sha256={SOURCES[f'solution-{sid}']}; "
                "individual authors and publication year not supplied; stock concentrations only.",
            }
        )
    after["references"].append(
        {
            "reference": MEDIUM,
            "title": "MediaDive J1219: METHYLOTROPH MEDIUM",
            "notes": "source_type=dataset; discovery_mode=existing_record_reference; "
            "accessed_on=2026-10-07; source_organization=DSMZ/JCM; "
            f"response_sha256={SOURCES['J1219']}; source-to-stock linkage only; "
            "individual authors and publication year not supplied.",
        }
    )
    refs = [r["reference"] for r in after["references"]]
    require(len(refs) == len(set(refs)), "Duplicate bibliography reference")
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source="; ".join([MEDIUM] + list(dict.fromkeys(c["reference"] for c in claims))),
        notes="Twelve stock concentrations unchanged; exact stock and receiving-recipe evidence attached. "
        "Six main-medium denominator gaps and both variants remain unresolved.",
        changes="; ".join(f"{c['field']}: evidence_only; unchanged {c['old']}" for c in claims),
    )
    require(not list(validate_recipe(after, target_class="MediaRecipe")), "Closed-schema failure")
    return after, claims


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--verify", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    tracked = (
        subprocess.check_output(["git", "ls-files", "-z", TARGET], cwd=ROOT).decode().split("\0")
    )
    require(TARGET in tracked and not (ROOT / TARGET).is_symlink(), "Non-exact or symlink target")
    path = ROOT / TARGET
    raw = path.read_bytes()
    sources = captures(args.source_dir)
    if args.apply or args.verify:
        plan = json.loads(args.plan.read_text())
        require(plan["path"] == TARGET and plan["before_sha256"] == BEFORE, "Wrong plan")
        if sha(raw) == plan["after_sha256"]:
            doc = yaml.load(raw, Loader=yaml.CSafeLoader)
            require(
                not list(validate_recipe(doc, target_class="MediaRecipe")), "Post-schema failure"
            )
            for claim in plan["claims"]:
                node = doc
                for key in claim["pointer"]:
                    node = node[key]
                require(node["concentration"] == claim["old"], "Quantity changed")
                require(node["evidence"][0]["snippet"] == claim["snippet"], "Snippet changed")
                sid = claim["reference"].rsplit("/", 1)[1]
                require(claim["snippet"] in sources[f"solution-{sid}"][0], "Inexact source snippet")
            print(
                json.dumps(
                    {"changed": 0, "already_applied": 1, "verified_snippets": len(plan["claims"])}
                )
            )
            return
        require(not args.verify, "Result not applied")
    else:
        require(not args.plan.exists(), "Do not overwrite reviewed plan")
        plan = {
            "path": TARGET,
            "before_sha256": BEFORE,
            "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
    require(sha(raw) == BEFORE, "Concurrent record change")
    doc = yaml.load(raw, Loader=yaml.CSafeLoader)
    require(not list(validate_recipe(doc, target_class="MediaRecipe")), "Baseline schema failure")
    after, claims = build(doc, sources, plan["timestamp"])
    output = render(raw.decode(), after)
    if args.apply:
        require(claims == plan["claims"] and sha(output) == plan["after_sha256"], "Preview drift")
        require(path.read_bytes() == raw, "Concurrent edit before write")
        path.write_bytes(output)
    else:
        plan.update(after_sha256=sha(output), claims=claims, source_hashes=SOURCES)
        args.plan.parent.mkdir(parents=True, exist_ok=True)
        args.plan.write_text(json.dumps(plan, indent=2) + "\n")
    print(
        json.dumps(
            {"changed": int(args.apply), "evidence_only": len(claims), "quantity_corrections": 0}
        )
    )


if __name__ == "__main__":
    main()
