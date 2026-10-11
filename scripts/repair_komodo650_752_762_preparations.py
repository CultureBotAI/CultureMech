#!/usr/bin/env python3
"""Restore source-explicit amounts and preparation stages for three KOMODO media."""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path

import review_public_stock_concentrations as shared
import review_solution_concentration_evidence as runner
from inventory_komodo_concentration_sources import MAPPING_URL
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261007-komodo650-752-762-preparations"
COHORT = HERE.parent / "20261007-komodo-media-2000-2500"
ACTION = "CORRECTED_KOMODO650_752_762_AMOUNTS_AND_PREPARATION_STAGES"
API = "https://mediadive.dsmz.de/rest/medium/"
PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium{}.pdf"
CONTEXT_SHA = "65c1b3085c5b2101fd274a184820f9de1dd1fa7f7f7d7d0068d6acb67b587934"
COHORT_SHA = "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823"
TARGETS = {
    "650": {
        "path": "data/normalized_yaml/bacterial/KOMODO_650_CENTENUM_medium.yaml",
        "id": "CultureMech:006227",
        "name": "centenum_medium",
        "before_sha256": "779aa4f42a64cc9e8d1935b7a1d82a59a569e6bee01f0accb54822f6840ae069",
    },
    "752": {
        "path": "data/normalized_yaml/bacterial/KOMODO_752_HALOMONAS_PANTELLERIENSE.yaml",
        "id": "CultureMech:006404",
        "name": "halomonas_pantelleriense",
        "before_sha256": "1678ab0baff860e2c2dcd9d0bcdf374f2ba8141f63be4db0d145b9bbbcfcdf8b",
    },
    "762": {
        "path": "data/normalized_yaml/bacterial/KOMODO_762_HALOMONAS_DESIDERATA_MEDIUM.yaml",
        "id": "CultureMech:006417",
        "name": "halomonas_desiderata_medium",
        "before_sha256": "909a9b718be107ee1ef2fc901bb2aee46a21e3714ebbed1157041546bc807c95",
    },
}


def sources(folder, mid):
    """Replay the already inspected, immutable source captures, not another YAML."""
    context = (folder / "inspected-candidate-context.json").read_bytes()
    cohort = (folder / "plan.json").read_bytes()
    runner.require(runner.sha(context) == CONTEXT_SHA, "Source context drift")
    runner.require(runner.sha(cohort) == COHORT_SHA, "Source mapping plan drift")
    entry = next(e for e in json.loads(context) if e["medium_id"] == mid)
    plan = json.loads(cohort)
    mapped = next(r for r in plan["records"] if r["path"] == TARGETS[mid]["path"])
    raw, meta = entry["source_raw"], entry["source_metadata"]
    runner.require(
        runner.sha(raw.encode()) == meta["sha256"] == mapped["source_sha256"]
        and meta["http_status"] == 200
        and meta["url"] == API + mid,
        "Source identity drift",
    )
    runner.require(
        entry["path"] == mapped["path"]
        and entry["before_sha256"] == TARGETS[mid]["before_sha256"]
        and mapped["mapping"]["medium_id"] == mid
        and mapped["mapping"]["original_recipe"] == PDF.format(mid),
        "Record/source mapping drift",
    )
    return {
        "raw": raw,
        "metadata": meta,
        "mapping": mapped["mapping"],
        "mapping_metadata": plan["mapping_source"],
        "sha256": meta["sha256"],
    }


def build(before, source, mid, timestamp):
    spec = TARGETS[mid]
    runner.require(
        before["id"] == spec["id"]
        and before["name"] == spec["name"]
        and before["media_term"]["term"]["id"] == "komodo.medium:" + mid
        and before["physical_state"] == "LIQUID"
        and not runner.errors(before, "MediaRecipe"),
        "Local identity/schema drift",
    )
    runner.require(
        not any(k in before for k in ("solutions", "preparation_steps", "evidence", "references")),
        "Unreviewed topology/provenance",
    )
    raw, ref = source["raw"], API + mid
    runner.require(runner.sha(raw.encode()) == source["sha256"], "Source hash drift")
    data = json.loads(raw)["data"]
    recipe = data["solutions"][0]
    runner.require(
        data["medium"]["id"] == int(mid)
        and data["medium"]["source"] == "DSMZ"
        and data["medium"]["link"] == PDF.format(mid)
        and len(data["solutions"]) == 1
        and recipe["volume"] == 1000,
        "Source recipe drift",
    )
    rows, steps = recipe["recipe"], [s["step"] for s in recipe["steps"]]
    count = {"650": 6, "752": 8, "762": 6}[mid]
    runner.require(len(before["ingredients"]) == count, "Local inventory drift")
    for node, row in zip(before["ingredients"], rows[:count], strict=True):
        runner.require(node["preferred_term"] == row["compound"], "Ingredient form drift")
        runner.require(
            not node.get("evidence") and "notes" not in node, "Existing claim needs reconciliation"
        )
    after, claims = copy.deepcopy(before), []
    base = ["data", "solutions", 0]

    def claim(
        pointer,
        old_pointer,
        status,
        source_pointer,
        reason,
        evidence_pointer,
        ingredient=None,
        extra=None,
    ):
        quote = json_excerpt(raw, source_pointer)
        runner.require(quote in raw, "Unverified excerpt")
        claims.append(
            {
                "pointer": pointer,
                "old_pointer": old_pointer,
                "field": runner.field_name(pointer),
                "old": copy.deepcopy(runner.get_node(before, old_pointer)) if old_pointer else None,
                "new": copy.deepcopy(runner.get_node(after, pointer)),
                "status": status,
                "reference": ref,
                "snippet": quote,
                "source_pointer": source_pointer,
                "locator": "$." + runner.field_name(source_pointer),
                "explanation": reason,
                "evidence_pointer": evidence_pointer,
                "ingredient": ingredient
                or runner.get_node(after, evidence_pointer).get("preferred_term", before["name"]),
                "extra_excerpts": (
                    []
                    if extra is None
                    else [
                        {
                            "snippet": json_excerpt(raw, extra),
                            "locator": "$." + runner.field_name(extra),
                        }
                    ]
                ),
            }
        )

    def water(pointer, value, source_pointer, reason):
        node = runner.get_node(after, pointer[:-1])
        node.append(
            {
                "preferred_term": "Distilled water",
                "term": {"id": "mediadive.compound:4", "label": "Distilled water"},
                "concentration": {"value": value, "unit": "L"},
                "notes": reason,
            }
        )
        claim(
            pointer + ["concentration"],
            None,
            "add",
            source_pointer,
            reason
            + " Convert ml to L by division by 1000. The source table identifies distilled water as compound 4; no final volume or density inferred.",
            pointer,
            "Distilled water",
            base + ["recipe", len(rows) - 1],
        )

    direct = {"650": 4, "752": 6, "762": 4}[mid]
    for i in range(direct):
        node = after["ingredients"][i]
        node["notes"] = (
            f"Source batch input: {rows[i]['amount']} {rows[i]['unit']}. Retained g/L is the provider's nominal main-recipe rate "
            "(volume field 1000 ml), not a measured final-medium concentration or a stock concentration."
        )
        claim(
            ["ingredients", i, "concentration"],
            ["ingredients", i, "concentration"],
            "evidence_only",
            base + ["recipe", i],
            node["notes"]
            + " Existing chemical mappings are preserved, not independently revalidated.",
            ["ingredients", i],
            extra=base + ["volume"],
        )

    if mid == "650":
        for i, value, unit, note in (
            (
                4,
                "1",
                "L",
                "1000 ml / 1000 = 1 L tap-water input per batch, not a mass concentration or measured final volume.",
            ),
            (
                5,
                "20",
                "MILLIMOLAR",
                "Source-explicit 20 mM pyruvate added after autoclaving. Replaces the imported mass conversion; no molecular weight, stock strength or stock dose is inferred.",
            ),
        ):
            node = after["ingredients"][i]
            node["concentration"] = {"value": value, "unit": unit}
            node["notes"] = note
            claim(
                ["ingredients", i, "concentration"],
                ["ingredients", i, "concentration"],
                "correct",
                base + ["recipe", i],
                note,
                ["ingredients", i],
                extra=base + ["steps", 1],
            )
        after["preparation_steps"] = [
            {"step_number": 1, "action": "ADJUST_PH", "description": steps[0]},
            {"step_number": 2, "action": "HEAT", "description": steps[1]},
        ]
    elif mid == "752":
        after["ingredients"] = after["ingredients"][:6]
        after["solutions"] = []
        for j, i in enumerate((6, 7)):
            node = copy.deepcopy(before["ingredients"][i])
            strength = "0.36" if j == 0 else "50"
            runner.require(
                rows[i]["attribute"] == strength + "g/l"
                and rows[i]["unit"] == "ml"
                and rows[i]["amount"] == 1,
                "Stock source drift",
            )
            node["concentration"] = {"value": strength, "unit": "G_PER_L"}
            node["notes"] = (
                "Source-explicit stock strength, not final-medium concentration; replaces the flattened 1 g/L encoding of a 1 ml stock dose."
            )
            after["solutions"].append(
                {
                    "preferred_term": node["preferred_term"] + " stock",
                    "composition": [node],
                    "concentration": {"value": "0.001", "unit": "L"},
                    "notes": "1 ml stock addition per source recipe batch; no final-medium volume, stock carrier amount or final-medium concentration inferred.",
                    "source": ref,
                }
            )
            pointer = ["solutions", j, "composition", 0]
            claim(
                pointer + ["concentration"],
                ["ingredients", i, "concentration"],
                "correct_stock_basis",
                base + ["recipe", i],
                node["notes"],
                pointer,
            )
            claim(
                ["solutions", j, "concentration"],
                None,
                "add",
                base + ["recipe", i],
                "1 ml / 1000 = 0.001 L absolute stock dose. Supports the stock descriptor name, source, and input-basis note. Chemical constituent retained at its source-explicit stock strength; no dilution calculation.",
                [],
                node["preferred_term"] + " stock",
            )
        water(
            ["ingredients", 6],
            "1",
            base + ["recipe", 8],
            "1000 ml distilled-water input per batch, not a measured final-medium volume.",
        )
        after["preparation_steps"] = [
            {
                "step_number": 1,
                "action": "MIX",
                "description": steps[0].split(" Agar (2%)")[0],
            }
        ]
    else:
        after["ingredients"] = after["ingredients"][:4]
        stock = {
            "preferred_term": "Separately sterilized carbonate preparation",
            "composition": copy.deepcopy(before["ingredients"][4:]),
            "preparation_notes": steps[0],
            "notes": "100 ml water is preparation input, not final stock volume or numeric stock addition dose. Stock strength and final-medium concentrations are unasserted. Separate sterilization method is not specified.",
            "source": ref,
        }
        after["solutions"] = [stock]
        for j, i in enumerate((4, 5)):
            node = stock["composition"][j]
            node.pop("concentration")
            node["notes"] = (
                f"Source batch input: {rows[i]['amount']} g {rows[i]['compound']} in the separately sterilized carbonate preparation. "
                "The flattened g/L rate is withdrawn at this stock stage; 100 ml water is not final stock volume. No stock or final-medium concentration is calculated."
            )
            pointer = ["solutions", 0, "composition", j]
            claim(
                pointer + ["notes"],
                ["ingredients", i, "concentration"],
                "withdraw",
                base + ["recipe", i],
                node["notes"],
                pointer,
                extra=base + ["steps", 0],
            )
        water(
            ["ingredients", 4],
            "0.9",
            base + ["steps", 0],
            "900 ml distilled-water input for the base, excluding the separate carbonate preparation; not a final volume.",
        )
        water(
            ["solutions", 0, "composition", 2],
            "0.1",
            base + ["steps", 0],
            "100 ml water input for the carbonate preparation, not a final stock volume or stock dose.",
        )
        for slot in ("preferred_term", "preparation_notes", "notes", "source"):
            claim(
                ["solutions", 0, slot],
                None,
                "restore_stock",
                base + ["steps", 0],
                "Restore the source's separate carbonate preparation. The descriptor name is a curator label, not a new source accession. Retain input masses without asserting 54 or 42 g/L stock strengths, a 0.1 L stock dose, or an unspecified sterilization method.",
                [],
                stock["preferred_term"],
            )
        after["preparation_steps"] = [{"step_number": 1, "action": "MIX", "description": steps[0]}]

    claim(
        ["preparation_steps"],
        None,
        "restore_preparation",
        base + ["steps"],
        "Restore the source instructions for this liquid formulation; "
        + (
            "the agar branch and its carbonate dose are excluded."
            if mid == "752"
            else "no additional sterilization parameters or final volumes inferred."
        ),
        [],
        "Preparation",
    )
    after["notes"] += (
        "\n\nConcentration follow-up: water volumes denote batch inputs, not final volume. "
        "Historical source-duplicate links and import annotations are preserved but not revalidated by this correction; linked records may still carry flattened quantities. "
        + (
            "Only the liquid preparation branch is represented; the source's agar/carbonate alternative is not applied here."
            if mid == "752"
            else "Preparation stages follow the cited source."
        )
    )
    claim(
        ["notes"],
        ["notes"],
        "clarify_scope",
        base + ["steps"],
        "Document the reviewed preparation scope and limitation of unchanged historical duplicate annotations; this does not validate linked formulations.",
        [],
        "Scope",
    )

    groups = {}
    for c in claims:
        groups.setdefault(tuple(c["evidence_pointer"]), []).append(c)
    for pointer, group in groups.items():
        explanation = " ".join(
            f"{c['field']} ({c['status']}), locator={c['locator']}: {c['explanation']}"
            + (" Additional exact excerpt: " + c["snippet"] if i else "")
            + "".join(
                f" Additional exact excerpt at {q['locator']}: {q['snippet']}"
                for q in c["extra_excerpts"]
            )
            for i, c in enumerate(group)
        )
        runner.get_node(after, pointer).setdefault("evidence", []).append(
            {
                "reference": ref,
                "supports": "SUPPORT",
                "snippet": group[0]["snippet"],
                "explanation": explanation
                + f" Retrieved {source['metadata']['accessed_at']}; response SHA256={source['sha256']}.",
            }
        )
    mapping = source["mapping_metadata"]
    after["evidence"].append(
        {
            "reference": MAPPING_URL,
            "supports": "SUPPORT",
            "snippet": source["mapping"]["snippet"],
            "explanation": f"Identity only: KOMODO {mid} maps to {PDF.format(mid)}. Locator=MediaList row {mid}. No quantity or growth inference. Retrieved {mapping['accessed_at']}; response SHA256={mapping['sha256']}.",
        }
    )
    after["references"] = [
        {
            "reference": url,
            "title": title,
            "notes": f"source_type={kind}; discovery_mode=cross_reference; accessed_on={meta['accessed_at'][:10]}; response_sha256={meta['sha256']}; individual authors and publication year not established. {note}",
        }
        for url, title, kind, meta, note in (
            (
                ref,
                f"MediaDive medium {mid}: {data['medium']['name']}",
                "dataset",
                source["metadata"],
                "Descriptive dataset title from the response's medium name, not an HTML document title.",
            ),
            (
                MAPPING_URL,
                "KOMODO - the Known Media Database",
                "web_page",
                mapping,
                "Document title verified in the captured HTML; mapping supports identity only.",
            ),
        )
    ]
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source=ref + "; " + MAPPING_URL,
        notes="Corrected source-explicit amounts and preparation stages. Exact excerpts accompany all changes; retained identity/history and linked records without propagating this formulation. No growth claim added.",
        changes="; ".join(
            f"{c['field']}: {json.dumps(c['old'])} -> {json.dumps(c['new'])} ({c['status']})"
            for c in claims
        ),
    )
    runner.require(not runner.errors(after, "MediaRecipe"), "Proposed schema failure")
    return after, claims


def process(root, folder, plan_path, mode):
    return shared.process(
        root,
        folder,
        plan_path,
        mode,
        targets=TARGETS,
        action=ACTION,
        source_reader=sources,
        builder=build,
    )


def report(folder, plan, applied):
    folder.mkdir(parents=True, exist_ok=True)
    for item in plan["records"]:
        lines = [
            "# Concentration And Preparation Follow-Up",
            "",
            f"- Follow-up target: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Hash-linked supplement to the existing exact-path report, not another unique review. All original concentration claims are accounted below. Baseline/proposed schema checks pass; wider checks are recorded in validation.json.",
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
        if item["medium_id"] == "762":
            context = sources(COHORT, "762")
            quote = json_excerpt(context["raw"], ["data", "solutions", 0, "steps", 0])
            for field in (
                "solutions[0].concentration",
                "solutions[0].composition[0].concentration",
                "solutions[0].composition[1].concentration",
            ):
                lines.append(
                    "| "
                    + " | ".join(
                        runner.cell(v)
                        for v in (
                            field,
                            "Carbonate preparation",
                            "see withdrawal rows",
                            None,
                            "unsupported",
                            API + "762",
                            quote,
                            "$.data.solutions[0].steps[0]",
                            "Input masses and water volume do not establish final stock volume, stock strength, or a numeric addition dose; deliberately unasserted.",
                        )
                    )
                    + " |"
                )
        lines += [
            "",
            "Remaining limits: no measured final-medium volume or independent ontology validation. Historical duplicate links require reconciliation. Dataset author/year unknown. No taxa-media association added.",
        ]
        if item["medium_id"] in {"752", "762"}:
            lines += [
                "",
                "Final-medium dilution concentrations remain unsupported; water inputs are not final volumes.",
            ]
        if item["medium_id"] == "762":
            lines += [
                "Carbonate stock strength and numeric addition volume: unsupported, deliberately unasserted. The source gives input masses and 100 ml water, not final stock volume."
            ]
        (folder / (item["medium_id"] + "-followup.md")).write_text("\n".join(lines) + "\n")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--source-dir", type=Path, default=COHORT)
    p.add_argument("--plan", type=Path, default=HERE / "plan.json")
    p.add_argument("--reports", type=Path)
    modes = p.add_mutually_exclusive_group()
    modes.add_argument("--dry-run", action="store_true")
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--verify", action="store_true")
    args = p.parse_args()
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    plan, result = process(ROOT, args.source_dir, args.plan, mode)
    if args.reports:
        report(args.reports, plan, mode != "preview")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
