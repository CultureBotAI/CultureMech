#!/usr/bin/env python3
"""Restore source-pinned DSMZ 1157/1164 stock stages without assumed percent bases."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from decimal import Decimal
from pathlib import Path

import review_solution_concentration_evidence as runner
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-dsmz1157-1164-stocks"
CONTEXT_SHA = "746ca54df3fe06273c9d3a8e5ac2f784066460d0ae39d0fba8de499465cf9692"
ACTION = "CORRECTED_DSMZ1157_1164_STOCK_STAGES_AND_INPUTS"
SIDS = {"1157": 2323, "1164": 2333}
STEPS = {
    "1157": ["After autoclaving and cooling add: ", "Final pH 7.0"],
    "1164": ["Adjust to pH 7.2"],
}
QUOTES = {
    "1157": "Riboflavin (0.2 mg/ml) filter-sterilized 5.0 ml",
    "1164": "FeCl3 x 6 H2O (0.5%) 7 drops",
}
WATER_QUOTES = {"1157": "Distilled water 1000.0 ml", "1164": "Distilled water 1000.000 ml"}
ROWS = {
    "1157": [
        ("Peptone", 1, 2, "g", 2, None),
        ("Yeast extract", 16, 2, "g", 2, None),
        ("NH4Cl", 42, 0.5, "g", 0.5, None),
        ("Distilled water", 4, 1000, "ml", None, None),
        ("Riboflavin", 136, 5, "ml", None, "0.2 mg/ml, filter-sterilized"),
        ("Glucose", 5, 2, "ml", 1, "autoclaved, 50%"),
        ("MgSO4", 325, 1, "ml", 0.2, "autoclaved, 20%"),
        ("CaCl2", 81, 1, "ml", 0.1, "autoclaved, 10%"),
    ],
    "1164": [
        ("NaHCO3", 55, 0.166, "g", 0.166, None),
        ("NaBr", 353, 0.35, "g", 0.35, None),
        ("CaCl2 x 2 H2O", 7, 0.916, "g", 0.916, None),
        ("KCl", 61, 5, "g", 5, None),
        ("MgSO4 x 7 H2O", 8, 49.83, "g", 49.83, None),
        ("NaCl", 43, 195, "g", 195, None),
        ("FeCl3 x 6 H2O", 82, 7, "drops", None, "0.5 %"),
        ("Glucose", 5, 1, "g", 1, None),
        ("Proteose peptone", 208, 5, "g", 5, None),
        ("Yeast extract", 16, 5, "g", 5, None),
        ("Distilled water", 4, 1000, "ml", None, None),
    ],
}


def frozen():
    raw = (HERE / "inspected-context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    context = json.loads(raw)
    runner.require([g["medium_id"] for g in context["groups"]] == list(SIDS), "Wrong groups")
    targets = {}
    for group in context["groups"]:
        mid = group["medium_id"]
        runner.require(group["solution_id"] == SIDS[mid], "Solution mapping drift")
        runner.require(
            [r["kind"] for r in group["records"]] == ["komodo", "medium", "solution"],
            "Wrong record kinds",
        )
        for record in group["records"]:
            targets[mid + "-" + record["kind"]] = (record, group)
    return targets


def checked_source(group, kind):
    mid, sid = group["medium_id"], group["solution_id"]
    parsed = {}
    for source_kind, accession in (("medium", mid), ("solution", str(sid))):
        raw, meta = group[source_kind + "_raw"], group[source_kind + "_metadata"]
        reference = f"https://mediadive.dsmz.de/rest/{source_kind}/{accession}"
        runner.require(
            runner.sha(raw.encode()) == meta["sha256"]
            and meta["http_status"] == 200
            and meta["url"] == meta["response_url"] == reference,
            "Source capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        payload = json.loads(raw)
        runner.require(payload["status"] == 200 and payload["count"] == 1, "Source envelope drift")
        data = payload["data"]
        if source_kind == "medium":
            runner.require(
                data["medium"]["id"] == int(mid)
                and data["medium"]["source"] == "DSMZ"
                and data["medium"]["link"] == group["pdf"]["reference"]
                and len(data["solutions"]) == 1,
                "Wrong medium formulation",
            )
            data = data["solutions"][0]
        runner.require(
            data["id"] == sid
            and data["name"] == "Main sol. " + mid
            and data["volume"] == 1000
            and [s["step"] for s in data["steps"]] == STEPS[mid],
            "Preparation identity/context drift",
        )
        runner.require(len(data["recipe"]) == len(ROWS[mid]), "Source inventory drift")
        for i, (row, expected) in enumerate(zip(data["recipe"], ROWS[mid], strict=True)):
            runner.require(
                tuple(
                    row.get(k)
                    for k in ("compound", "compound_id", "amount", "unit", "g_l", "attribute")
                )
                == expected
                and row["recipe_order"] == i + 1
                and row["optional"] == 0
                and not any(row.get(k) for k in ("condition", "solution", "solution_id")),
                "Source amount/form drift",
            )
        parsed[source_kind] = data
    runner.require(
        [{k: v for k, v in r.items() if v is not None} for r in parsed["solution"]["recipe"]]
        == parsed["medium"]["recipe"],
        "Paired amount sources disagree",
    )
    pdf = group["pdf"]
    title = f"{mid}. " + json.loads(group["medium_raw"])["data"]["medium"]["name"]
    runner.require(
        pdf["http_status"] == 200
        and len(pdf["pages"]) == 1
        and all(q in pdf["pages"][0] for q in (title, QUOTES[mid], WATER_QUOTES[mid])),
        "PDF corroboration drift",
    )
    runner.require(
        group["mapping"]["medium_id"] == mid
        and group["mapping"]["original_recipe"] == pdf["reference"],
        "KOMODO mapping drift",
    )
    sk = "solution" if kind == "solution" else "medium"
    return parsed[sk], group[sk + "_raw"], group[sk + "_metadata"], title


def build(before, key, timestamp):
    record, group = frozen()[key]
    mid, kind = key.split("-")
    solution = kind == "solution"
    target_class = "SolutionRecipe" if solution else "MediaRecipe"
    runner.require(
        before == runner.load_yaml(record["before_text"]) and before["id"] == record["id"],
        "Unreviewed baseline",
    )
    runner.require(not runner.errors(before, target_class), "Baseline schema failure")
    data, raw, meta, title = checked_source(group, kind)
    field = "composition" if solution else "ingredients"
    nodes, rows = before[field], data["recipe"]
    wi = 3 if mid == "1157" else 10
    stock_rows = [4, 5, 6, 7] if mid == "1157" else [6]
    source_indices = (
        list(range(len(rows))) if solution else [i for i in range(len(rows)) if i != wi]
    )
    runner.require(
        [n["preferred_term"] for n in nodes] == [rows[i]["compound"] for i in source_indices],
        "Ingredient inventory drift",
    )
    runner.require(
        not before.get("solutions") and not before.get("variants"), "Unreviewed topology"
    )
    expected_id = (
        f"mediadive.solution:{SIDS[mid]}"
        if solution
        else f"{'komodo' if kind == 'komodo' else 'mediadive'}.medium:{mid}"
    )
    runner.require(
        (before["term"] if solution else before["media_term"]["term"])["id"] == expected_id,
        "Local source identity drift",
    )
    after = copy.deepcopy(before)
    after[field], after["solutions"] = [], []
    base = ["data"] if solution else ["data", "solutions", 0]
    root = ["source_data"] if solution else []
    if solution:
        runner.require("source_data" not in before, "Existing provenance needs reconciliation")
        after["source_data"] = {"origin": "MediaDive"}
    claims, resolutions = [], []

    def claim(pointer, old_pointer, status, source_pointer, reason, evidence_pointer, ingredient):
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
                "reference": meta["url"],
                "source_pointer": source_pointer,
                "snippet": json_excerpt(raw, source_pointer),
                "locator": "$." + runner.field_name(source_pointer),
                "explanation": reason,
                "evidence_pointer": evidence_pointer,
                "ingredient": ingredient,
            }
        )

    for ri in source_indices:
        if ri == wi or ri in stock_rows:
            continue
        oi, ni = source_indices.index(ri), len(after[field])
        node = copy.deepcopy(nodes[oi])
        runner.require(
            node["concentration"] == {"value": str(rows[ri]["g_l"]), "unit": "G_PER_L"}
            and "notes" not in node,
            "Basal amount drift",
        )
        note = f"Source batch input: {rows[ri]['amount']} g. Retained {rows[ri]['g_l']} g/L is the provider's nominal 1000 ml recipe rate, not a measured basal or final-medium concentration after stock additions."
        node["notes"] = note
        after[field].append(node)
        claim(
            [field, ni, "concentration"],
            [field, oi, "concentration"],
            "evidence_only",
            base + ["recipe", ri],
            note + " Supports the source-input note as well as the retained provider rate.",
            [field, ni],
            node["preferred_term"],
        )
        if oi != ni and node.get("evidence"):
            resolutions.append(
                {
                    "from_pointer": [field, oi],
                    "to_pointer": [field, ni],
                    "reference": meta["url"],
                    "disposition": "relocated",
                    "old_concentration": nodes[oi]["concentration"],
                    "new_field": runner.field_name([field, ni, "concentration"]),
                    "source_pointer": base + ["recipe", ri],
                    "source_snippet": claims[-1]["snippet"],
                    "reason": note,
                }
            )

    for si, ri in enumerate(stock_rows):
        oi = source_indices.index(ri)
        node = copy.deepcopy(nodes[oi])
        runner.require(
            "evidence" not in node and "notes" not in node, "Stock provenance needs reconciliation"
        )
        node.pop("concentration")
        if mid == "1157" and si == 0:
            node["concentration"] = {"value": "0.2", "unit": "MG_PER_ML"}
            node["notes"] = (
                "Source-explicit riboflavin stock strength: 0.2 mg/ml. The source's 5 ml is a stock addition volume, not 5 g/L or 5% v/v. No final-medium concentration is inferred."
            )
        else:
            percent = ["50%", "20%", "10%"][si - 1] if mid == "1157" else "0.5%"
            node["notes"] = (
                f"Source stock label: {percent}; percentage basis unspecified. The flattened recipe quantity is withdrawn at this stock stage. No mass/volume percentage basis, density, stock solvent or final-medium concentration is inferred."
            )
        stock = {
            "preferred_term": node["preferred_term"] + " stock",
            "composition": [node],
            "source": meta["url"],
        }
        if mid == "1157":
            dose = str(Decimal(str(rows[ri]["amount"])) / 1000)
            stock["concentration"] = {"value": dose, "unit": "L"}
            stock["notes"] = (
                f"Source batch dose: {rows[ri]['amount']} ml stock / 1000 ml per L = {dose} L. This is an input volume, not a dose per liter of measured final medium."
            )
            stock["preparation_notes"] = (
                ("Filter-sterilized" if si == 0 else "Autoclaved")
                + " stock; add after autoclaving and cooling the base. No temperature, duration, pore size or solvent specified."
            )
        else:
            stock["notes"] = (
                "Source batch dose: 7 drops of FeCl3 x 6 H2O stock labelled 0.5%. Drop volume and percentage basis are unspecified. Seven drops is not 7 g/L; no numeric volume, stock strength or final-medium concentration is inferred."
            )
        after["solutions"].append(stock)
        p = ["solutions", si, "composition", 0]
        claim(
            p + ["concentration" if "concentration" in node else "notes"],
            [field, oi, "concentration"],
            "correct",
            base + ["recipe", ri],
            node["notes"]
            + " Existing chemical mappings are preserved, not independently validated.",
            p,
            node["preferred_term"],
        )
        for slot in stock:
            if slot == "composition":
                continue
            reason = (
                stock["notes"]
                + " Stock descriptor is a curator label, not a new source identifier."
            )
            if slot == "preparation_notes":
                reason += (
                    " Additional exact preparation excerpt at $."
                    + runner.field_name(base + ["steps", 0])
                    + ": "
                    + json_excerpt(raw, base + ["steps", 0])
                )
            claim(
                ["solutions", si, slot],
                None,
                "add",
                base + ["recipe", ri],
                reason,
                root,
                stock["preferred_term"],
            )

    water = (
        copy.deepcopy(nodes[wi])
        if solution
        else {
            "preferred_term": "Distilled water",
            "term": {"id": "mediadive.compound:4", "label": "Distilled water"},
        }
    )
    water["concentration"] = {"value": "1", "unit": "L"}
    water["notes"] = (
        "Source batch input: 1000 ml distilled water = 1 L. This is not a volume percentage or a measured final-medium volume."
    )
    after[field].append(water)
    claim(
        [field, len(after[field]) - 1, "concentration"],
        [field, wi, "concentration"] if solution else None,
        "correct" if solution else "add",
        base + ["recipe", wi],
        water["notes"]
        + " Calculation: 1000 ml / 1000 ml per L = 1 L. Supports water identity and the input-basis note.",
        [field, len(after[field]) - 1],
        "Distilled water",
    )
    scope = "Stock stages and water inputs are explicit. Percentage bases, stock solvents and measured final volume are not supplied by these sources; no downstream dilution or growth claim is inferred. Existing chemical mappings and high_metal/other historical flags are retained but not validated by this concentration repair."
    after["notes"] = (before.get("notes", "") + "\n\n" + scope).lstrip()
    claim(
        ["notes"],
        ["notes"] if "notes" in before else None,
        "evidence_only",
        base + ["recipe", stock_rows[0]],
        scope,
        root,
        "Preparation scope",
    )
    if mid == "1164" and not solution:
        pointer = ["parent_media"] if kind == "komodo" else ["variant_children", 0]
        other = next(
            r for r in group["records"] if r["kind"] == ("medium" if kind == "komodo" else "komodo")
        )
        link = runner.get_node(after, pointer)
        runner.require(
            link["id"] == other["id"]
            and link["path"].replace("/bacterial/", "/archaea/") == other["path"],
            "Link target identity drift",
        )
        link["path"] = other["path"]
        claim(
            pointer + ["path"],
            pointer + ["path"],
            "correct",
            ["data", "medium"],
            f"Correct stale category path to exact tracked target {other['path']} with unchanged ID {other['id']}. Exact API/PDF and KOMODO original-recipe mapping establish source identity; the local path/ID is checked against the paired frozen record, not inferred from the external source.",
            root,
            "Source-duplicate link",
        )

    # One evidence entry per reference/container; retain historical quotations and explanations.
    groups = {}
    for c in claims:
        groups.setdefault(tuple(c["evidence_pointer"]), []).append(c)
    for pointer, group_claims in groups.items():
        target = runner.get_node(after, pointer)
        entries = [e for e in target.get("evidence", []) if e["reference"] == meta["url"]]
        runner.require(len(entries) <= 1, "Duplicate evidence")
        parts, quoted = [], set()
        for c in group_claims:
            part = f"{c['field']} ({c['status']}), locator={c['locator']}: {c['explanation']}"
            if c["snippet"] not in quoted:
                part += " Exact supporting excerpt: " + c["snippet"]
                quoted.add(c["snippet"])
            parts.append(part)
        explanation = " ".join(parts)
        explanation += f" Retrieved {meta['accessed_at']}; response SHA256={meta['sha256']}."
        if entries:
            runner.require(
                entries[0]["snippet"] == group_claims[0]["snippet"], "Historical quote drift"
            )
            entries[0]["explanation"] = (
                explanation
                + " Historical explanation (superseded where preparation scope differs): "
                + entries[0]["explanation"]
            )
        else:
            target.setdefault("evidence", []).append(
                {
                    "reference": meta["url"],
                    "supports": "SUPPORT",
                    "snippet": group_claims[0]["snippet"],
                    "explanation": explanation,
                }
            )
    pdf = group["pdf"]
    root_node = runner.get_node(after, root)
    root_node.setdefault("evidence", []).append(
        {
            "reference": pdf["reference"],
            "supports": "SUPPORT",
            "snippet": QUOTES[mid],
            "explanation": f"Original DSMZ recipe page 1 corroborates solutions[0] stock stage and batch dose, including {'0.2 mg/ml riboflavin strength' if mid == '1157' else 'seven drops and an unspecified 0.5% basis'}. Additional exact water-row excerpt: {WATER_QUOTES[mid]}. 1000 ml / 1000 ml per L = 1 L water input, not measured final volume. PDF SHA256={pdf['sha256']}; retrieved {pdf['accessed_at']}. Other stock rows are separately quoted from the linked API.",
        }
    )
    mapping = group["mapping_metadata"]
    if kind == "komodo":
        root_node["evidence"].append(
            {
                "reference": mapping["reference"],
                "supports": "SUPPORT",
                "snippet": group["mapping"]["snippet"],
                "explanation": f"Identity only: KOMODO {mid} maps to {pdf['reference']}; locator=MediaList row {mid}. No quantity or growth claim follows from this mapping. Retrieved {mapping['accessed_at']}; SHA256={mapping['sha256']}.",
            }
        )
    refs = [
        (
            meta["url"],
            data["name"] if solution else title.split(". ", 1)[1],
            "dataset",
            meta["accessed_at"],
            meta["sha256"],
        ),
        (pdf["reference"], title, "culture_collection_protocol", pdf["accessed_at"], pdf["sha256"]),
    ]
    if kind == "komodo":
        refs.append(
            (
                mapping["reference"],
                "KOMODO - the Known Media Database",
                "dataset",
                mapping["accessed_at"],
                mapping["sha256"],
            )
        )
    for url, ref_title, source_type, accessed, digest in refs:
        if any(r["reference"] == url for r in after.get("references", [])):
            continue
        after.setdefault("references", []).append(
            {
                "reference": url,
                "title": ref_title,
                "notes": f"source_type={source_type}; discovery_mode=cross_reference; accessed_on={accessed[:10]}; response_sha256={digest}; individual authors and publication year not specified; the 2008 PDF copyright notice is not treated as publication year.",
            }
        )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source="; ".join(r[0] for r in refs),
        notes="Restored stock boundaries, exact source doses and water input. Unspecified percentage bases/drop volume remain unresolved. Preserved prior history and snippets, chemical mappings and unrelated flags; corrected only verified stale link paths. No final-volume, growth or new variant inference.",
        changes="; ".join(
            f"{c['field']}: {json.dumps(c['old'])} -> {json.dumps(c['new'])} ({c['status']})"
            for c in claims
        ),
    )
    runner.require(not runner.errors(after, target_class), "Proposed schema failure")
    if solution:
        claims.append(
            {
                "pointer": ["ingredients", 0, "concentration"],
                "old_pointer": ["ingredients", 0, "concentration"],
                "field": "ingredients[0].concentration",
                "ingredient": "See source for composition",
                "old": before["ingredients"][0]["concentration"],
                "new": after["ingredients"][0]["concentration"],
                "status": "unsupported",
                "reference": None,
                "snippet": None,
                "locator": None,
                "explanation": "Legacy placeholder unchanged; not a verified ingredient amount.",
            }
        )
    return after, claims, resolutions


def process(root, plan_path, mode):
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    targets = frozen()
    if mode == "preview":
        runner.require(not plan_path.exists(), "Refuse plan overwrite")
        plan = {
            "version": 1,
            "action": ACTION,
            "context_sha256": CONTEXT_SHA,
            "commit": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=root, text=True
            ).strip(),
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
    else:
        plan = json.loads(plan_path.read_text())
        runner.require(
            plan["version"] == 1
            and plan["action"] == ACTION
            and plan["context_sha256"] == CONTEXT_SHA
            and [r["key"] for r in plan["records"]] == list(targets),
            "Plan drift",
        )
    records, pending = [], []
    for key, (spec, group) in targets.items():
        path = root / spec["path"]
        runner.require(not path.is_symlink(), "Symlink target")
        current, before = path.read_bytes(), spec["before_text"].encode()
        runner.require(runner.sha(before) == spec["before_sha256"], "Baseline hash drift")
        after, claims, resolutions = build(runner.load_yaml(before), key, plan["created_at"])
        output = runner.render(before.decode(), after)
        runner.require(current in (before, output), "Concurrent edit")
        sk = "solution" if spec["kind"] == "solution" else "medium"
        records.append(
            {
                **spec,
                "key": key,
                "action": ACTION,
                "target_class": "SolutionRecipe" if sk == "solution" else "MediaRecipe",
                "after_text": output.decode(),
                "after_sha256": runner.sha(output),
                "source_sha256": group[sk + "_metadata"]["sha256"],
                "claims": claims,
                "claim_resolutions": resolutions,
            }
        )
        pending.append((path, current, output))
    if mode != "preview":
        runner.require(records == plan["records"], "Frozen decisions drift")
    plan["records"] = records
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
        "records": len(records),
        "changed": sum(c != o for _, c, o in pending) if mode == "apply" else 0,
        "already_applied": sum(c == o for _, c, o in pending),
        "scoped_claims": sum(len(r["claims"]) for r in records),
    }


def report(plan, applied):
    for r in plan["records"]:
        lines = [
            "# Stock Stage Follow-Up",
            "",
            f"- Follow-up target: {r['path']}",
            f"- ID: {r['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {r['before_sha256']}",
            f"- Result SHA256: {r['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Hash-linked supplement to the original exact-path report, not an additional unique review. All prior concentration slots and new stock doses are covered. Missing stock strengths, percent bases and drop volume remain unresolved; no final-volume concentration is inferred. Schema checks pass; wider results belong in ../validation.json.",
            "",
            "| Field | Ingredient | Old | New | Status | DOI/PURL | Exact snippet | Locator | Decision |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for c in r["claims"]:
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
        p = HERE / "records" / (r["key"] + ".md")
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--plan", type=Path, default=HERE / "plan.json")
    parser.add_argument("--reports", action="store_true")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--dry-run", action="store_true")
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    plan, result = process(ROOT, args.plan, mode)
    if args.reports:
        report(plan, mode != "preview")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
