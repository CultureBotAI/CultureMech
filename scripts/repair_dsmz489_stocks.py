#!/usr/bin/env python3
"""Restore medium 489 stock boundaries using pinned original-source evidence."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from pathlib import Path

import review_solution_concentration_evidence as runner
from fetch_medium_concentration_sources import read_capture as read_medium
from fetch_solution_concentration_sources import read_capture as read_solution
from inventory_komodo_concentration_sources import MAPPING_URL, read_mapping
from repair_dsmz111_preparation import MAPPING_META
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261007-dsmz489-stocks"
HANDOFF = HERE.parent / "20261007-dsmz467-469-inputs/next-medium489-handoff.json"
ACTION = "CORRECTED_DSMZ489_STOCK_BOUNDARIES_AND_WATER_INPUT"
API = "https://mediadive.dsmz.de/rest/"
PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium489.pdf"
PDF_HASH = "87e33303ba52375124cb2a58bd6ca8ee1827872562b37c0040775d120ba306ba"
HASHES = {
    API + "medium/489": "5e3a6ed7c5e1fece0f2c6852a18238f8e4413b9215893cdc23a69e6a77fbfff3",
    API + "solution/995": "b4fa8a5e53d05cefbbc31f9e28e52a398afdaad599e2d57b76b1c90bb42d0607",
}
STEP = (
    "Dissolve ingredients (except cysteine and sulfide), adjust pH to 7.0, "
    "bring medium to the boil, then cool to room temperature under 100% N2 gas. "
    "Dispense under same gas atmosphere into anoxic Hungate-type tubes or serum vials and autoclave. "
    "After sterilization add cysteine and sulfide from sterile anoxic stock solutions prepared under 100% N2 gas."
)
STOCK_STEP = STEP[STEP.index("After sterilization") :]
ROWS = [
    ("K2HPO4", 10, 0.22, "g", 0.22),
    ("KH2PO4", 11, 0.22, "g", 0.22),
    ("NaCl", 43, 0.45, "g", 0.45),
    ("(NH4)2SO4", 27, 0.45, "g", 0.45),
    ("CaCl2 x 2 H2O", 7, 0.06, "g", 0.06),
    ("MgSO4 x 7 H2O", 8, 0.09, "g", 0.09),
    ("Yeast extract", 16, 5, "g", 5),
    ("Xylan", 508, 5, "g", 5),
    ("Sodium resazurin", 1852, 0.5, "ml", 0.0005),
    ("L-Cysteine HCl x H2O", 770, 0.15, "g", 0.15),
    ("Na2S x 9 H2O", 54, 0.15, "g", 0.15),
    ("Distilled water", 4, 1000, "ml", None),
]
TARGETS = {
    key: {
        "path": "data/normalized_yaml/bacterial/" + name,
        "id": "CultureMech:" + rid,
        "before_sha256": digest,
        "target_class": "SolutionRecipe" if key == "solution" else "MediaRecipe",
    }
    for key, name, rid, digest in [
        (
            "dsmz",
            "lacrimispora_medium.yaml",
            "001616",
            "aea5b2c691d99f7fea32edbb4509870cbefcad9203f04554d1a5d51e35c14c53",
        ),
        (
            "komodo",
            "KOMODO_489_CLOSTRIDIUM_AEROTOLERANS_medium.yaml",
            "005614",
            "8143ecd9d9c6551c5b0612f80ad7340a478acca6472d07b3998db27ed0ada0b6",
        ),
        (
            "solution",
            "mediadive_995_Main_sol_489.yaml",
            "015327",
            "33bec52d778e4ed281738685fee81817854c65ddc0c8810938412f9e1b978e39",
        ),
    ]
}


def reference_for(key):
    return API + ("solution/995" if key == "solution" else "medium/489")


def read_sources(medium_cache, solution_cache, mapping, pdf_path):
    sources = {}
    for ref, (raw, meta) in zip(
        HASHES, (read_medium(medium_cache, "489"), read_solution(solution_cache, 995)), strict=True
    ):
        sources[ref] = {"raw": raw, "metadata": meta}
    handoff = json.loads(HANDOFF.read_text())
    sources["pdf"] = handoff["pdf"]
    sources["mapping"] = read_mapping(mapping, MAPPING_META)["489"]
    sources["mapping_metadata"] = copy.deepcopy(MAPPING_META)
    runner.require(runner.sha(pdf_path.read_bytes()) == PDF_HASH, "PDF byte drift")
    check_sources(sources)
    return sources


def check_sources(sources):
    for ref, digest in HASHES.items():
        source = sources[ref]
        runner.require(
            runner.sha(source["raw"].encode()) == digest == source["metadata"]["sha256"]
            and source["metadata"]["url"] == ref
            and source["metadata"]["http_status"] == 200,
            "API source drift",
        )
        data = json.loads(source["raw"])["data"]
        if ref.endswith("medium/489"):
            runner.require(
                data["medium"]["id"] == 489
                and data["medium"]["name"] == "LACRIMISPORA MEDIUM"
                and data["medium"]["source"] == "DSMZ"
                and data["medium"]["link"] == PDF
                and len(data["solutions"]) == 1,
                "Medium identity drift",
            )
            data = data["solutions"][0]
        runner.require(
            data["id"] == 995
            and data["name"] == "Main sol. 489"
            and data["volume"] == 1000
            and len(data["recipe"]) == 12
            and [s["step"] for s in data["steps"]] == [STEP],
            "Recipe/preparation drift",
        )
        for i, (row, expected) in enumerate(zip(data["recipe"], ROWS, strict=True)):
            runner.require(
                tuple(row.get(k) for k in ("compound", "compound_id", "amount", "unit", "g_l"))
                == expected
                and row["recipe_order"] == i + 1
                and row["optional"] == 0
                and row.get("attribute") == ("0.1% w/v" if i == 8 else None)
                and not any(row.get(k) for k in ("condition", "solution", "solution_id")),
                "Ingredient/form/amount drift",
            )
    mapping, pdf = sources["mapping"], sources["pdf"]
    runner.require(
        sources["mapping_metadata"] == MAPPING_META
        and mapping["medium_id"] == "489"
        and mapping["original_recipe"] == PDF
        and mapping["cells"][:2] == ["489", "CLOSTRIDIUM AEROTOLERANS medium"]
        and PDF.replace("https:", "http:") in mapping["snippet"],
        "Mapping drift",
    )
    runner.require(
        pdf["reference"] == PDF
        and pdf["pdf_sha256"] == PDF_HASH
        and pdf["http_status"] == 200
        and pdf["pages"] == 1
        and all(
            quote in pdf["extracted_text"]
            for quote in (
                "Sodium resazurin (0.1% w/v) 0.50 ml",
                "Distilled water 1000.00 ml",
                "L-Cysteine HCl x H2O 0.15 g",
                "Na2S x 9 H2O 0.15 g",
                "sterilization add cysteine and sulfide from sterile anoxic stock solutions prepared under\n100% N2 gas.",
            )
        ),
        "PDF source drift",
    )


def build(before, key, sources, timestamp):
    spec = TARGETS[key]
    solution = key == "solution"
    field = "composition" if solution else "ingredients"
    ref = reference_for(key)
    raw = sources[ref]["raw"]
    base = ["data"] if solution else ["data", "solutions", 0]
    runner.require(
        before["id"] == spec["id"] and not runner.errors(before, spec["target_class"]),
        "Record/schema drift",
    )
    runner.require(
        not before.get("solutions") and not before.get("variants"), "Unreviewed topology"
    )
    expected_id = (
        "mediadive.solution:995"
        if solution
        else ("komodo" if key == "komodo" else "mediadive") + ".medium:489"
    )
    runner.require(
        (before["term"] if solution else before["media_term"]["term"])["id"] == expected_id,
        "Local source drift",
    )
    nodes = before[field]
    runner.require(len(nodes) == (12 if solution else 11), "Local inventory drift")
    for i, node in enumerate(nodes):
        runner.require(
            node["preferred_term"] == ROWS[i][0]
            and node["concentration"]
            == {
                "value": "1000" if i == 11 else str(ROWS[i][4]),
                "unit": "PERCENT_V_V" if i == 11 else "G_PER_L",
            }
            and "notes" not in node,
            "Local ingredient/amount drift",
        )
    after = copy.deepcopy(before)
    after[field] = after[field][:8]
    after["solutions"] = []
    evidence_root = ["source_data"] if solution else []
    if solution:
        runner.require("source_data" not in before, "Existing provenance needs reconciliation")
        after["source_data"] = {"origin": "MediaDive"}
    claims, resolutions = [], []

    def claim(
        pointer, old_pointer, status, source_pointer, explanation, evidence_pointer, ingredient
    ):
        claims.append(
            {
                "pointer": pointer,
                "old_pointer": old_pointer,
                "field": runner.field_name(pointer),
                "old": (
                    copy.deepcopy(runner.get_node(before, old_pointer))
                    if old_pointer is not None
                    else None
                ),
                "new": copy.deepcopy(runner.get_node(after, pointer)),
                "status": status,
                "reference": ref,
                "source_pointer": source_pointer,
                "snippet": json_excerpt(raw, source_pointer),
                "locator": "$." + runner.field_name(source_pointer),
                "explanation": explanation,
                "evidence_pointer": evidence_pointer,
                "ingredient": ingredient,
            }
        )

    # Basal rates remain explicitly provider-nominal, not measured final-volume rates.
    for i, node in enumerate(after[field]):
        node["notes"] = (
            f"Source batch input: {ROWS[i][2]} g. Retained {ROWS[i][4]} g/L is the provider's nominal 1000 ml recipe rate, "
            "not a measured basal or final-medium concentration after stock additions."
        )
        claim(
            [field, i, "concentration"],
            [field, i, "concentration"],
            "evidence_only",
            base + ["recipe", i],
            node["notes"],
            [field, i],
            node["preferred_term"],
        )
    for si, i in enumerate((8, 9, 10)):
        node = copy.deepcopy(nodes[i])
        old = node.pop("concentration")
        if si == 0:
            node["concentration"] = {"value": "0.1", "unit": "PERCENT_W_V"}
            node["notes"] = (
                "Source-explicit 0.1% w/v stock strength. The former 0.0005 g/L recipe rate is not the stock concentration. Existing resazurin ontology mapping is retained, not independently validated as the sodium salt."
            )
        else:
            node["notes"] = (
                "Source batch requirement: 0.15 g supplied from a sterile anoxic stock prepared under 100% N2, added after sterilization. Stock strength, final stock volume, solvent identity and numeric stock dose are unspecified; the former 0.15 g/L flattened rate is withdrawn at this preparation stage."
            )
        stock = {
            "preferred_term": (
                "Sodium resazurin stock (0.1% w/v)"
                if si == 0
                else node["preferred_term"] + " sterile anoxic stock"
            ),
            "composition": [node],
            "source": ref,
            "notes": (
                "0.50 ml stock input per source recipe batch, not per liter of measured final medium. No solvent identity is inferred."
                if si == 0
                else node["notes"]
            ),
        }
        if si == 0:
            stock["concentration"] = {"value": "0.0005", "unit": "L"}
        else:
            stock["preparation_notes"] = STOCK_STEP
        after["solutions"].append(stock)
        pointer = ["solutions", si, "composition", 0]
        reason = (
            node["notes"]
            + " Additional exact preparation excerpt: "
            + json_excerpt(raw, base + ["steps", 0])
        )
        claim(
            pointer + ["concentration" if si == 0 else "notes"],
            [field, i, "concentration"],
            "correct_stage" if si == 0 else "withdraw",
            base + ["recipe", i],
            reason,
            pointer,
            node["preferred_term"],
        )
        if nodes[i].get("evidence"):
            resolutions.append(
                {
                    "from_pointer": [field, i],
                    "to_pointer": pointer,
                    "reference": ref,
                    "disposition": "withdrawn",
                    "old_concentration": old,
                    "new_field": runner.field_name(pointer + ["notes"]),
                    "source_pointer": base + ["steps", 0],
                    "source_snippet": json_excerpt(raw, base + ["steps", 0]),
                    "reason": node["notes"],
                }
            )
        for slot in stock:
            if slot == "composition":
                continue
            claim(
                ["solutions", si, slot],
                None,
                "restore_stock",
                base + (["recipe", i] if si == 0 else ["steps", 0]),
                stock["notes"]
                + (
                    " 0.50 ml / 1000 ml per L = 0.0005 L batch dose."
                    if si == 0
                    else " Source input mass is quoted separately on the ingredient. Descriptor is a curator label, not a new identifier."
                ),
                evidence_root,
                stock["preferred_term"],
            )
    water = (
        copy.deepcopy(nodes[11])
        if solution
        else {
            "preferred_term": "Distilled water",
            "term": {"id": "mediadive.compound:4", "label": "Distilled water"},
        }
    )
    water["concentration"] = {"value": "1", "unit": "L"}
    water["notes"] = (
        "1000 ml distilled-water input per source batch, not a volume percentage or measured final medium volume."
    )
    after[field].append(water)
    claim(
        [field, 8, "concentration"],
        [field, 11, "concentration"] if solution else None,
        "correct" if solution else "add",
        base + ["recipe", 11],
        "1000 ml / 1000 ml per L = 1 L input; supports the water identity and input-basis note, not final volume.",
        [field, 8],
        "Distilled water",
    )
    after["notes"] = (
        before.get("notes", "")
        + "\n\nPreparation scope: cysteine and sulfide are added after sterilization from sterile anoxic stocks prepared under 100% N2. Their 0.15 g batch inputs do not establish stock strengths or addition volumes. Resazurin is a 0.1% w/v stock added at 0.50 ml per batch. Water is a 1000 ml input; final-medium volume and final concentrations are not inferred. Historical annotations, including any aerobic flag, are not verified incubation or growth evidence; the source establishes anoxic preparation. Chemical mappings and variant links are retained, not independently revalidated."
    ).lstrip()
    claim(
        ["notes"],
        ["notes"] if "notes" in before else None,
        "correct_scope",
        base + ["steps", 0],
        "Preparation context; ingredient-row excerpts separately support quantities. Historical aerobic annotation is retained as import provenance, not endorsed as preparation or growth evidence.",
        evidence_root,
        "Preparation scope",
    )
    if key == "komodo":
        runner.require(
            "preparation_steps" not in before, "Existing preparation needs reconciliation"
        )
        after["preparation_steps"] = [{"step_number": 1, "action": "DISSOLVE", "description": STEP}]
        claim(
            ["preparation_steps"],
            None,
            "restore_preparation",
            base + ["steps", 0],
            "Verbatim source preparation; action names opening instruction. No temperature, duration, filter pore size or incubation atmosphere added.",
            evidence_root,
            "Preparation",
        )
    else:
        actual_step = (
            before["preparation_notes"]
            if solution
            else before["preparation_steps"][0]["description"]
        )
        runner.require(actual_step == STEP, "Local preparation drift")
    groups = {}
    for c in claims:
        groups.setdefault(tuple(c["evidence_pointer"]), []).append(c)
    for pointer, group in groups.items():
        node = runner.get_node(after, pointer)
        entries = [e for e in node.get("evidence", []) if e["reference"] == ref]
        runner.require(len(entries) <= 1, "Duplicate evidence")
        explanation = " ".join(
            f"{c['field']} ({c['status']}), locator={c['locator']}: {c['explanation']}"
            + (
                " Additional exact excerpt: " + c["snippet"]
                if n and c["snippet"] != group[0]["snippet"]
                else ""
            )
            for n, c in enumerate(group)
        )
        explanation += f" Retrieved {sources[ref]['metadata']['accessed_at']}; response SHA256={HASHES[ref]}. Chemical mappings are not independently validated."
        if entries:
            runner.require(entries[0]["snippet"] == group[0]["snippet"], "Historical quote drift")
            entries[0]["explanation"] = (
                explanation
                + " Historical explanation (superseded where preparation scope differs): "
                + entries[0]["explanation"]
            )
        else:
            node.setdefault("evidence", []).append(
                {
                    "reference": ref,
                    "supports": "SUPPORT",
                    "snippet": group[0]["snippet"],
                    "explanation": explanation,
                }
            )
    root = runner.get_node(after, evidence_root)
    root.setdefault("evidence", []).append(
        {
            "reference": PDF,
            "supports": "SUPPORT",
            "snippet": "Sodium resazurin (0.1% w/v) 0.50 ml",
            "explanation": f"Original recipe page 1 confirms solutions[0] stock strength and batch dose. Additional exact water-row excerpt: Distilled water 1000.00 ml. Input water does not establish final volume. PDF SHA256={PDF_HASH}; retrieved {sources['pdf']['accessed_at']}. Preparation and reducer-mass claims are separately supported by the API excerpts.",
        }
    )
    if key == "komodo":
        root["evidence"].append(
            {
                "reference": MAPPING_URL,
                "supports": "SUPPORT",
                "snippet": sources["mapping"]["snippet"],
                "explanation": f"Identity only: KOMODO 489 maps to {PDF}; locator=MediaList row 489. Historical medium name retained. No concentration or growth claim follows from the mapping. Retrieved {MAPPING_META['accessed_at']}; SHA256={MAPPING_META['sha256']}.",
            }
        )
    refs = [
        (
            ref,
            (
                "MediaDive solution 995: Main sol. 489"
                if solution
                else "MediaDive medium 489: LACRIMISPORA MEDIUM"
            ),
            "dataset",
            sources[ref]["metadata"]["accessed_at"],
            HASHES[ref],
        ),
        (
            PDF,
            "489: LACRIMISPORA MEDIUM",
            "culture_collection_page",
            sources["pdf"]["accessed_at"],
            PDF_HASH,
        ),
    ]
    if key == "komodo":
        refs.append(
            (
                MAPPING_URL,
                "KOMODO media list: original-recipe mappings",
                "dataset",
                MAPPING_META["accessed_at"],
                MAPPING_META["sha256"],
            )
        )
    for url, title, stype, accessed, digest in refs:
        if any(r["reference"] == url for r in after.get("references", [])):
            continue
        after.setdefault("references", []).append(
            {
                "reference": url,
                "title": title,
                "notes": f"source_type={stype}; discovery_mode={'cross_reference' if key == 'komodo' else 'existing_record_reference'}; accessed_on={accessed[:10]}; response_sha256={digest}; individual authors and publication year not established; PDF copyright year is not a publication year.",
            }
        )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source="; ".join(r[0] for r in refs),
        notes="Restored explicit resazurin stock strength/dose and separate post-sterilization reducing stocks. Corrected/restored water input. Preserved history, exact previous snippets, mappings and variants; no unknown stock strength, solvent, final volume or growth association inferred.",
        changes="; ".join(
            f"{c['field']}: {json.dumps(c['old'])} -> {json.dumps(c['new'])} ({c['status']})"
            for c in claims
        ),
    )
    runner.require(not runner.errors(after, spec["target_class"]), "Proposed schema failure")
    return after, claims, resolutions


def process(root, sources, plan_path, mode):
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    check_sources(sources)
    if mode == "preview":
        runner.require(not plan_path.exists(), "Refuse to overwrite reviewed plan")
        plan = {
            "version": 1,
            "action": ACTION,
            "commit": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=root, text=True
            ).strip(),
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "sources": sources,
        }
    else:
        plan = json.loads(plan_path.read_text())
        runner.require(
            plan["version"] == 1
            and plan["action"] == ACTION
            and plan["sources"] == sources
            and [r["key"] for r in plan["records"]] == list(TARGETS),
            "Frozen plan/source drift",
        )
    items, pending = [], []
    for i, (key, spec) in enumerate(TARGETS.items()):
        path = root / spec["path"]
        runner.require(not path.is_symlink(), "Symlink target")
        current = path.read_bytes()
        before = current if mode == "preview" else plan["records"][i]["before_text"].encode()
        runner.require(runner.sha(before) == spec["before_sha256"], "Baseline hash drift")
        after, claims, resolutions = build(
            runner.load_yaml(before), key, sources, plan["created_at"]
        )
        output = runner.render(before.decode(), after)
        runner.require(current in (before, output), "Concurrent edit")
        items.append(
            {
                **spec,
                "key": key,
                "action": ACTION,
                "before_text": before.decode(),
                "after_text": output.decode(),
                "after_sha256": runner.sha(output),
                "source_sha256": HASHES[reference_for(key)],
                "claims": claims,
                "claim_resolutions": resolutions,
            }
        )
        pending.append((path, current, output))
    if mode != "preview":
        runner.require(items == plan["records"], "Frozen plan/decision drift")
    plan["records"] = items
    runner.safe_targets(root, plan)
    runner.require(
        all(p.read_bytes() == c and not p.is_symlink() for p, c, _ in pending),
        "Concurrent edit before write",
    )
    if mode == "preview":
        plan_path.parent.mkdir(parents=True, exist_ok=True)
        plan_path.write_text(json.dumps(plan, indent=2) + "\n")
    else:
        for path, current, output in pending:
            runner.require(
                path.read_bytes() == current and not path.is_symlink(),
                "Concurrent edit during write",
            )
            if mode == "apply" and current != output:
                path.write_bytes(output)
            runner.require(path.read_bytes() == output, "Result not applied")
    return plan, {
        "mode": mode,
        "records": len(items),
        "changed": sum(c != o for _, c, o in pending) if mode == "apply" else 0,
        "already_applied": sum(c == o for _, c, o in pending),
        "scoped_claims": sum(len(r["claims"]) for r in items),
    }


def report(folder, plan, applied):
    folder.mkdir(parents=True, exist_ok=True)
    for item in plan["records"]:
        lines = [
            "# Medium 489 Stock Follow-Up",
            "",
            f"- Follow-up target: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview; not applied'}",
            "",
            "Hash-linked supplement to the existing exact-path report, not a new unique reviewed path. Unchanged IDs, mappings, prior snippets/history and variant links are retained. The independent preflight inverts the complete record. Validation results are in baseline.json and, after applying, validation.json.",
            "",
            "| Field | Ingredient | Old | New | Status | DOI/PURL | Exact snippet | Locator | Decision |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for c in item["claims"]:
            lines.append(
                "| "
                + " | ".join(
                    runner.cell(c[k])
                    for k in (
                        "field",
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
        for si in (1, 2):
            for slot in (
                f"solutions[{si}].concentration",
                f"solutions[{si}].composition[0].concentration",
            ):
                lines.append(
                    "| "
                    + " | ".join(
                        runner.cell(v)
                        for v in (
                            slot,
                            "Reducing stock dose/strength",
                            "flattened rate; see withdrawal row",
                            None,
                            "unsupported",
                            reference_for(item["key"]),
                            STOCK_STEP,
                            "steps[0]",
                            "No numeric stock dose, stock volume or strength specified. Source batch mass retained in notes, not used to invent a stock rate.",
                        )
                    )
                    + " |"
                )
        if item["key"] == "solution":
            lines.append(
                "| ingredients[0].concentration | Legacy placeholder | variable / VARIABLE | variable / VARIABLE | unsupported | unknown | unknown | unknown | Preserved import placeholder, not verified composition. |"
            )
        lines += [
            "",
            "Original PDF confirms resazurin strength/dose and water input: " + PDF,
            "Individual authors and publication year remain unknown; copyright is not publication year. Existing resazurin CHEBI mapping has not been validated as a sodium-salt identifier. No final-medium concentration, solvent identity or growth association is inferred.",
        ]
        (folder / (item["key"] + "-followup.md")).write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("medium-cache", "solution-cache", "mapping", "pdf-path", "plan"):
        parser.add_argument("--" + name, type=Path, required=True)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--verify", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    parser.add_argument("--reports", type=Path)
    args = parser.parse_args()
    sources = read_sources(args.medium_cache, args.solution_cache, args.mapping, args.pdf_path)
    plan, outcome = process(
        ROOT, sources, args.plan, "apply" if args.apply else "verify" if args.verify else "preview"
    )
    if args.reports:
        report(args.reports, plan, args.apply or args.verify)
    print(json.dumps(outcome, indent=2))


if __name__ == "__main__":
    main()
