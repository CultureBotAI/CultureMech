#!/usr/bin/env python3
"""Repair the DSMZ and standalone-source counterparts without losing prior evidence."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from pathlib import Path

import repair_komodo650_752_762_preparations as komodo
import review_solution_concentration_evidence as runner
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261007-dsmz650-752-762-preparations"
ACTION = "CORRECTED_DSMZ650_752_762_MEDIUM_AND_SOLUTION_PREPARATIONS"
HANDOFF_SHA = "d1494456978169922593f952f6da9b3fc23d1b2c0717de5e8eedcaa90414a7fa"
SOURCE_SHA = "4fb9643748006517ff91951569feb1771bb216e6f1abdcc3c10e2095344e0e6a"
SIDS = {"650": 1378, "752": 1538, "762": 1552}
TARGETS = {
    "650-medium": (
        "centenum_medium.yaml",
        "001789",
        "d8c501c37e916fb861b62c77c493876dfafa59fe761a616daa197459a3fea6ac",
    ),
    "752-medium": (
        "halomonas_pantelleriense.yaml",
        "001885",
        "2bbbac8fa6fdcc582e8cc82a76af94448a9876e322c5c825e674c8734b6ac1c4",
    ),
    "762-medium": (
        "halomonas_desiderata_medium.yaml",
        "001895",
        "fcf45b15b4d75ac232ff9e456456c24f7527e29dbf4777d2804fe25aa578e643",
    ),
    "650-solution": (
        "mediadive_1378_Main_sol_650.yaml",
        "010862",
        "c9431668ac31b5df76ddfd635d2dfc0a27d02d3b0eff0cad9ab719cc513d080c",
    ),
    "752-solution": (
        "mediadive_1538_Main_sol_752.yaml",
        "011004",
        "68120fed50ac88772d242bfaa940bdd4badff873cb9facd53696c106d5fcb068",
    ),
    "762-solution": (
        "mediadive_1552_Main_sol_762.yaml",
        "011014",
        "2d102f0853122a9cb1c9543c91c115a22a6314633102ebe5a20ef778252f3457",
    ),
}
TARGETS = {
    key: {
        "path": "data/normalized_yaml/bacterial/" + file,
        "id": "CultureMech:" + rid,
        "before_sha256": digest,
        "target_class": "SolutionRecipe" if key.endswith("solution") else "MediaRecipe",
    }
    for key, (file, rid, digest) in TARGETS.items()
}


def sources():
    records = (komodo.HERE / "related-record-handoff.json").read_bytes()
    captures = (komodo.HERE / "related-source-handoff.json").read_bytes()
    runner.require(
        runner.sha(records) == HANDOFF_SHA and runner.sha(captures) == SOURCE_SHA,
        "Frozen handoff drift",
    )
    source_rows = json.loads(captures)["sources"]
    bundle = {}
    for mid, sid in SIDS.items():
        old = next(r for r in source_rows if r["medium_id"] == mid)
        medium = komodo.sources(komodo.COHORT, mid)
        runner.require(
            old["solution_id"] == sid and old["medium_metadata"] == medium["metadata"],
            "Paired source identity drift",
        )
        bundle[mid + "-medium"] = {"raw": medium["raw"], "metadata": medium["metadata"]}
        bundle[mid + "-solution"] = {
            "raw": old["solution_raw"],
            "metadata": old["solution_metadata"],
        }
    check_sources(bundle)
    return bundle


def check_sources(bundle):
    captured = json.loads((komodo.HERE / "related-source-handoff.json").read_text())
    runner.require(set(bundle) == set(TARGETS), "Wrong sources")
    for mid, sid in SIDS.items():
        item = next(r for r in captured["sources"] if r["medium_id"] == mid)
        for kind, expected in (
            ("medium", item["medium_metadata"]),
            ("solution", item["solution_metadata"]),
        ):
            s = bundle[mid + "-" + kind]
            runner.require(
                s["metadata"] == expected
                and runner.sha(s["raw"].encode()) == expected["sha256"]
                and expected["http_status"] == 200,
                "Source hash/metadata drift",
            )
            expected_ref = (
                "https://mediadive.dsmz.de/rest/"
                + kind
                + "/"
                + (mid if kind == "medium" else str(sid))
            )
            runner.require(expected["url"] == expected_ref, "Source URL drift")
        main = json.loads(bundle[mid + "-medium"]["raw"])["data"]
        sol = json.loads(bundle[mid + "-solution"]["raw"])["data"]
        runner.require(
            main["medium"]["id"] == int(mid)
            and main["medium"]["source"] == "DSMZ"
            and main["medium"]["link"] == komodo.PDF.format(mid)
            and len(main["solutions"]) == 1,
            "Medium identity drift",
        )
        m = main["solutions"][0]
        runner.require(
            sol["id"] == m["id"] == sid
            and sol["name"] == m["name"] == "Main sol. " + mid
            and sol["volume"] == m["volume"] == 1000,
            "Recipe basis drift",
        )
        runner.require(
            [{k: v for k, v in r.items() if v is not None} for r in sol["recipe"]] == m["recipe"]
            and [s["step"] for s in sol["steps"]] == [s["step"] for s in m["steps"]],
            "Paired source formulation drift",
        )


def build(before, key, bundle, timestamp):
    check_sources(bundle)
    spec = TARGETS[key]
    mid, kind = key.split("-")
    solution = kind == "solution"
    field = "composition" if solution else "ingredients"
    raw, meta = bundle[key]["raw"], bundle[key]["metadata"]
    ref = meta["url"]
    base = ["data"] if solution else ["data", "solutions", 0]
    data = runner.get_node(json.loads(raw), base)
    rows, steps = data["recipe"], [s["step"] for s in data["steps"]]
    old_rows = before[field]
    expected_term = (
        ("mediadive.solution:" + str(SIDS[mid])) if solution else "mediadive.medium:" + mid
    )
    runner.require(
        before["id"] == spec["id"] and not runner.errors(before, spec["target_class"]),
        "Record identity/schema drift",
    )
    runner.require(
        (before["term"] if solution else before["media_term"]["term"])["id"] == expected_term,
        "Local source drift",
    )
    runner.require(
        not any(k in before for k in ("solutions", "source_data", "evidence")),
        "Unreviewed topology",
    )
    runner.require(solution or before["physical_state"] == "LIQUID", "Unexpected physical state")
    expected_count = len(rows) if solution else {"650": 6, "752": 8, "762": 6}[mid]
    runner.require(len(old_rows) == expected_count, "Local inventory drift")
    for i, node in enumerate(old_rows):
        runner.require(
            node["preferred_term"] == rows[i]["compound"] and "notes" not in node,
            "Local chemical/context drift",
        )
        if solution:
            runner.require(
                node["term"]["id"] == "mediadive.compound:" + str(rows[i]["compound_id"]),
                "Compound accession drift",
            )
        for e in node.get("evidence", []):
            runner.require(
                e["reference"] == ref and e["snippet"] == json_excerpt(raw, base + ["recipe", i]),
                "Existing evidence drift",
            )
    runner.require(
        len(before["references"]) == 1 and before["references"][0]["reference"] == ref,
        "Bibliography drift",
    )
    if solution:
        runner.require(
            before["preparation_notes"] == "\n".join(steps), "Existing preparation drift"
        )
    else:
        runner.require(
            [p["description"] for p in before["preparation_steps"]] == steps,
            "Existing preparation drift",
        )
    after, claims, resolutions = copy.deepcopy(before), [], []
    evidence_root = ["source_data"] if solution else []
    if solution:
        after["source_data"] = {"origin": "MediaDive"}

    def claim(pointer, old_pointer, status, src, reason, evidence_pointer, extra=None):
        c = {
            "pointer": pointer,
            "old_pointer": old_pointer,
            "field": runner.field_name(pointer),
            "old": copy.deepcopy(runner.get_node(before, old_pointer)) if old_pointer else None,
            "new": copy.deepcopy(runner.get_node(after, pointer)),
            "status": status,
            "reference": ref,
            "source_pointer": src,
            "snippet": json_excerpt(raw, src),
            "locator": "$." + runner.field_name(src),
            "explanation": reason,
            "evidence_pointer": evidence_pointer,
            "ingredient": runner.get_node(after, evidence_pointer).get(
                "preferred_term", before.get("name", before.get("preferred_term"))
            ),
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
        claims.append(c)
        return c

    def water(pointer, value, reason, old_index=None, step=False):
        node = (
            copy.deepcopy(old_rows[old_index])
            if old_index is not None
            else {
                "preferred_term": "Distilled water",
                "term": {"id": "mediadive.compound:4", "label": "Distilled water"},
            }
        )
        node["concentration"] = {"value": value, "unit": "L"}
        node["notes"] = reason
        runner.get_node(after, pointer[:-1]).append(node)
        claim(
            pointer + ["concentration"],
            [field, old_index, "concentration"] if old_index is not None else None,
            "correct" if old_index is not None else "add",
            base + (["steps", 0] if step else ["recipe", len(rows) - 1]),
            reason
            + " Convert ml to L by division by 1000; no density or final-volume assumption. The source identifies distilled water as compound 4.",
            pointer,
            base + ["recipe", len(rows) - 1] if step else None,
        )

    direct = {"650": 4, "752": 6, "762": 4}[mid]
    for i in range(direct):
        node = after[field][i]
        node["notes"] = (
            f"Source input: {rows[i]['amount']} {rows[i]['unit']}. Retained g/L is the provider-declared nominal main-recipe rate "
            "(volume field 1000 ml), not a concentration in a separately prepared base, a separate stock, or a measured final-medium volume."
        )
        claim(
            [field, i, "notes"],
            None,
            "clarify_scope",
            base + ["recipe", i],
            node["notes"],
            [field, i],
            base + ["volume"],
        )

    if mid == "650":
        for i, value, unit, note in (
            (
                4,
                "1",
                "L",
                "1000 ml / 1000 = 1 L tap-water input per batch, not a mass concentration, percentage or measured final volume.",
            ),
            (
                5,
                "20",
                "MILLIMOLAR",
                "Source-explicit 20 mM pyruvate added after autoclaving; no molecular-weight conversion or unspecified stock dose inferred.",
            ),
        ):
            node = after[field][i]
            node["concentration"] = {"value": value, "unit": unit}
            node["notes"] = note
            claim(
                [field, i, "concentration"],
                [field, i, "concentration"],
                "correct",
                base + ["recipe", i],
                note,
                [field, i],
                base + ["steps", 1],
            )
        # Existing verbatim instructions already distinguish the late pyruvate addition.
    elif mid == "752":
        after[field] = after[field][:6]
        after["solutions"] = []
        for j, i in enumerate((6, 7)):
            node = copy.deepcopy(old_rows[i])
            value = "0.36" if j == 0 else "50"
            runner.require(
                rows[i]["attribute"] == value + "g/l"
                and rows[i]["unit"] == "ml"
                and rows[i]["amount"] == 1,
                "Stock amount drift",
            )
            node["concentration"] = {"value": value, "unit": "G_PER_L"}
            node["notes"] = (
                "Source-explicit stock strength, not a final-medium concentration. Replaces the flattened encoding of a 1 ml stock dose."
            )
            after["solutions"].append(
                {
                    "preferred_term": node["preferred_term"] + " stock",
                    "composition": [node],
                    "concentration": {"value": "0.001", "unit": "L"},
                    "source": ref,
                    "notes": "1 ml stock addition per source recipe batch, not per liter of an inferred final medium. Carrier amount and final-medium concentration remain unspecified.",
                }
            )
            pointer = ["solutions", j, "composition", 0]
            claim(
                pointer + ["concentration"],
                [field, i, "concentration"],
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
                "1 ml / 1000 = 0.001 L absolute stock addition. Supports the source-linked stock descriptor and dose note; no final-volume dilution inferred.",
                evidence_root,
            )
        water(
            [field, 6],
            "1",
            "1000 ml distilled-water input per batch, not a measured final volume.",
            8 if solution else None,
        )
        if not solution:
            after["preparation_steps"] = [
                {
                    "step_number": 1,
                    "action": "MIX",
                    "description": "Liquid medium may be prepared by adding all components together.",
                }
            ]
            runner.require(
                after["preparation_steps"][0]["description"] in steps[0], "Liquid branch drift"
            )
            claim(
                ["preparation_steps"],
                ["preparation_steps"],
                "correct_preparation",
                base + ["steps", 0],
                "Apply only the source's liquid branch to this LIQUID medium. Do not autoclave or add carbonate according to the distinct agar alternative.",
                evidence_root,
            )
    else:
        after[field] = after[field][:4]
        stock = {
            "preferred_term": "Separately sterilized carbonate preparation",
            "composition": copy.deepcopy(old_rows[4:6]),
            "preparation_notes": steps[0],
            "source": ref,
            "notes": "100 ml water is input, not final stock volume or a numeric stock addition dose. Neither stock strength nor final-medium concentration is inferred; the separate sterilization method is unspecified.",
        }
        after["solutions"] = [stock]
        for j, i in enumerate((4, 5)):
            node = stock["composition"][j]
            node.pop("concentration")
            node["notes"] = (
                f"Source batch input: {rows[i]['amount']} g {rows[i]['compound']} in the separately sterilized carbonate preparation. "
                "The former flattened g/L rate is withdrawn at this stock stage. The 100 ml water input does not establish final stock volume or a numeric stock dose."
            )
            pointer = ["solutions", 0, "composition", j]
            reason = "Withdraw the earlier flattened concentration interpretation at the separate carbonate preparation stage; retain the source batch mass."
            c = claim(
                pointer + ["notes"],
                [field, i, "concentration"],
                "withdraw",
                base + ["recipe", i],
                reason + " " + node["notes"],
                pointer,
                base + ["steps", 0],
            )
            resolutions.append(
                {
                    "from_pointer": [field, i],
                    "to_pointer": pointer,
                    "reference": ref,
                    "disposition": "withdrawn",
                    "old_concentration": copy.deepcopy(old_rows[i]["concentration"]),
                    "new_field": c["field"],
                    "source_pointer": base + ["steps", 0],
                    "source_snippet": json_excerpt(raw, base + ["steps", 0]),
                    "reason": reason,
                }
            )
        water(
            [field, 4],
            "0.9",
            "900 ml distilled-water input for the base, separate from carbonate preparation water; not a final volume.",
            6 if solution else None,
            True,
        )
        water(
            ["solutions", 0, "composition", 2],
            "0.1",
            "100 ml water input for the separate carbonate preparation, not final stock volume or stock dose.",
            step=True,
        )
        for slot in ("preferred_term", "preparation_notes", "notes", "source"):
            claim(
                ["solutions", 0, slot],
                None,
                "restore_stock",
                base + ["steps", 0],
                "Restore the source's separate carbonate preparation without assuming 54/42 g/L strengths, 0.1 L stock dose, or a sterilization method. Descriptor name is a curator label, not a new accession.",
                evidence_root,
            )
        if not solution:
            after["preparation_steps"][0]["action"] = "MIX"
            claim(
                ["preparation_steps"],
                ["preparation_steps"],
                "correct_preparation",
                base + ["steps", 0],
                "Keep the full verbatim instruction; do not label the entire combined recipe as autoclaved together. The base is autoclaved, the carbonates sterilized separately and added after cooling.",
                evidence_root,
            )

    after["notes"] = (
        before.get("notes", "")
        + "\n\nPreparation follow-up: water volumes are batch inputs, not measured final volumes. "
        "Original chemical mappings, history and source links are retained, not independently revalidated. "
        + (
            "The standalone recipe retains both conditional liquid/agar instructions; the agar alternative is not a simultaneous extra addition."
            if solution and mid == "752"
            else "Preparation follows the cited source; no dose into another receiving medium is inferred."
        )
    ).lstrip()
    claim(
        ["notes"],
        ["notes"] if "notes" in before else None,
        "clarify_scope",
        base + ["steps"],
        "Document preparation scope, retained conditional instructions, and input-versus-final-volume limitation. No growth or chemical remapping claim is added.",
        evidence_root,
    )
    groups = {}
    for c in claims:
        groups.setdefault(tuple(c["evidence_pointer"]), []).append(c)
    for pointer, group in groups.items():
        node = runner.get_node(after, pointer)
        entries = [e for e in node.get("evidence", []) if e["reference"] == ref]
        runner.require(len(entries) <= 1, "Duplicate reference evidence")
        explanation = " ".join(
            f"{c['field']} ({c['status']}), locator={c['locator']}: {c['explanation']}"
            + (" Additional exact excerpt: " + c["snippet"] if i else "")
            + "".join(
                f" Additional exact excerpt at {q['locator']}: {q['snippet']}"
                for q in c["extra_excerpts"]
            )
            for i, c in enumerate(group)
        )
        explanation += f" Retrieved {meta['accessed_at']}; response SHA256={meta['sha256']}."
        if entries:
            runner.require(entries[0]["snippet"] == group[0]["snippet"], "Historical excerpt drift")
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
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source=ref,
        notes="Corrected source-explicit amounts and preparation stages; original excerpts and history retained. Earlier carbonate concentration claims explicitly withdrawn and replaced by scoped input-mass evidence. No new growth claim or chemical grounding.",
        changes="; ".join(
            f"{c['field']}: {json.dumps(c['old'])} -> {json.dumps(c['new'])} ({c['status']})"
            for c in claims
        ),
    )
    runner.require(not runner.errors(after, spec["target_class"]), "Proposed schema failure")
    return after, claims, resolutions


def process(root, bundle, plan_path, mode):
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    check_sources(bundle)
    if mode == "preview":
        runner.require(not plan_path.exists(), "Refuse to overwrite reviewed plan")
        plan = {
            "version": 1,
            "action": ACTION,
            "commit": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=root, text=True
            ).strip(),
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "sources": bundle,
        }
    else:
        plan = json.loads(plan_path.read_text())
        runner.require(
            plan["version"] == 1
            and plan["action"] == ACTION
            and plan["sources"] == bundle
            and [r["key"] for r in plan["records"]] == list(TARGETS),
            "Frozen plan/source drift",
        )
    records, pending = [], []
    for i, (key, spec) in enumerate(TARGETS.items()):
        path = root / spec["path"]
        runner.require(not path.is_symlink(), "Symlink target")
        current = path.read_bytes()
        before = current if mode == "preview" else plan["records"][i]["before_text"].encode()
        runner.require(runner.sha(before) == spec["before_sha256"], "Baseline hash drift")
        after, claims, resolutions = build(
            runner.load_yaml(before), key, bundle, plan["created_at"]
        )
        output = runner.render(before.decode(), after)
        runner.require(current in (before, output), "Concurrent edit")
        records.append(
            {
                **spec,
                "key": key,
                "action": ACTION,
                "before_text": before.decode(),
                "after_text": output.decode(),
                "after_sha256": runner.sha(output),
                "source_sha256": bundle[key]["metadata"]["sha256"],
                "claims": claims,
                "claim_resolutions": resolutions,
            }
        )
        pending.append((path, current, output))
    if mode != "preview":
        runner.require(records == plan["records"], "Frozen plan/decision drift")
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
        "claims": sum(len(r["claims"]) for r in records),
    }


def report(plan, applied, directory=HERE):
    directory.mkdir(parents=True, exist_ok=True)
    for item in plan["records"]:
        lines = [
            "# DSMZ Preparation Follow-Up",
            "",
            f"- Follow-up target: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Hash-linked supplement to the existing exact-path report, not a new unique review. Existing excerpts and history are retained; withdrawn concentrations are explicitly scoped to source input masses. Baseline/proposed schema checks pass; terminal wider checks are in validation.json.",
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
        after = runner.load_yaml(item["after_text"])
        field = "composition" if item["key"].endswith("solution") else "ingredients"
        for c in item["claims"]:
            if c["pointer"][:1] != [field] or c["pointer"][-1] != "notes":
                continue
            pointer = c["pointer"][:-1] + ["concentration"]
            value = runner.get_node(after, pointer)
            lines.append(
                "| "
                + " | ".join(
                    runner.cell(v)
                    for v in (
                        runner.field_name(pointer),
                        c["ingredient"],
                        value,
                        value,
                        "verified",
                        c["reference"],
                        c["snippet"],
                        c["locator"],
                        "Unchanged provider-declared nominal recipe rate only. " + c["explanation"],
                    )
                )
                + " |"
            )
        if item["key"].startswith("762"):
            c = next(c for c in item["claims"] if c["status"] == "restore_stock")
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
                            "Carbonate stock",
                            "see withdrawal rows",
                            None,
                            "unsupported",
                            c["reference"],
                            c["snippet"],
                            c["locator"],
                            "Water input is not final stock volume or numeric addition dose; no fixed concentration asserted.",
                        )
                    )
                    + " |"
                )
        if item["key"].endswith("solution"):
            lines.append(
                "| ingredients[0].concentration | Legacy source placeholder | variable / VARIABLE | variable / VARIABLE | unsupported | unknown | unknown | unknown | Preserved historical placeholder; not a verified ingredient amount. |"
            )
        lines += [
            "",
            "No final-medium volume, receiving-medium dose, ontology identity, author/year, or growth association is inferred. Source copies are not independent scientific confirmations.",
        ]
        (directory / (item["key"] + "-followup.md")).write_text("\n".join(lines) + "\n")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--plan", type=Path, default=HERE / "plan.json")
    p.add_argument("--reports", action="store_true")
    modes = p.add_mutually_exclusive_group()
    modes.add_argument("--dry-run", action="store_true")
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--verify", action="store_true")
    args = p.parse_args()
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    plan, result = process(ROOT, sources(), args.plan, mode)
    if args.reports:
        report(plan, mode != "preview")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
