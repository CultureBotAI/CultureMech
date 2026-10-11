#!/usr/bin/env python3
"""Restore JCM973's two preparation stages using pinned TOGO/MediaDive evidence."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from pathlib import Path

import review_solution_concentration_evidence as runner
from repair_togo_first_pair_concentrations import amount_excerpt
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-jcm973-preparations"
CONTEXT_SHA = "86dff028638962f3766ee4b97586df8bcab635b831e9a1fb2423b7b43ca2c536"
ACTION = "RESTORED_JCM973_PREPARATION_STAGES_WITH_DATASET_EVIDENCE"
ORIGINAL = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=973"
STEP = (
    "Dissolve MgCl2 x 6H2O in distilled water and bring volume to 500.0 ml. "
    "Separately dissolve the remaining components in 500 ml distilled water and adjust pH to 7.0. "
    "For preparation of solid medium, add 20.0 g agar to the latter solution. "
    "Autoclave the two solutions separately and combine them after autoclaving."
)
ROWS = [
    ("NaCl", 43, 40.1, None),
    ("MgCl2 x 6 H2O", 79, 203, None),
    ("CaCl2 x 2 H2O", 7, 29.4, None),
    ("KCl", 61, 7.5, None),
    ("Yeast extract", 16, 1, "BD-Difco"),
    ("Casamino acids", 101, 1, "BD-Difco"),
    ("Starch", 199, 2, "soluble"),
]
TOGO_ROWS = [
    ("Distilled water", 1000, "ml"),
    ("NaCl", 40.1, "g"),
    ("CaCl2\u30fb2H2O", 29.4, "g"),
    ("MgCl2\u30fb6H2O", 203, "g"),
    ("KCl", 7.5, "g"),
    ("Soluble starch", 2, "g"),
    ("Yeast extract (BD-Difco)", 1, "g"),
    ("Casamino acids (BD-Difco)", 1, "g"),
]
MAGNESIUM = "JCM973 magnesium chloride preparation"
BASE = "JCM973 remaining-components preparation"
SCOPE = (
    "Source scope: the captured TOGO/MediaDive transcription of JCM973. The original JCM "
    "page returned 'Nothing found.' These datasets preserve the same recipe instructions; "
    "they are not independent experimental confirmations. No final-medium volume, "
    "density, post-autoclave volume, or DSMZ1468 equivalence is inferred."
)


def frozen():
    raw = (HERE / "inspected-context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    context = json.loads(raw)
    runner.require(
        [r["key"] for r in context["records"]] == ["M1023", "M1024", "medium", "solution"],
        "Inventory drift",
    )
    return context


def sources(context):
    result = {}
    for key, source in context["sources"].items():
        meta, raw = source["metadata"], source["raw"]
        url = (
            ORIGINAL
            if key == "original"
            else (
                "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=" + key
                if key.startswith("M")
                else "https://mediadive.dsmz.de/rest/"
                + ("medium/J973" if key == "medium" else "solution/4996")
            )
        )
        runner.require(
            meta["url"] == meta["response_url"] == url
            and meta["http_status"] == 200
            and runner.sha(raw.encode(meta["encoding"])) == meta["sha256"],
            "Capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
        if key == "original":
            runner.require(
                "Nothing found." in raw and "<TABLE" not in raw, "Original availability changed"
            )
            continue
        data = json.loads(raw)
        if key.startswith("M"):
            runner.require(
                data["meta"]
                == {
                    "gm": "http://togomedium.org/medium/" + key,
                    "name": "Halorhabdus Segorensis Medium",
                    "original_media_id": "JCM_M973" + ("-2" if key == "M1024" else ""),
                    "src_url": ORIGINAL,
                },
                "TOGO identity drift",
            )
            expected = list(TOGO_ROWS)
            if key == "M1024":
                expected.insert(6, ("agar", 20, "g"))
            runner.require(
                len(data["components"]) == 1
                and data["components"][0]["paragraph_index"] == 1
                and data["components"][0]["subcomponent_name"] == "main solution 1",
                "TOGO topology drift",
            )
            rows = data["components"][0]["items"]
            runner.require(
                [(r["component_name"], r["volume"], r["unit"]) for r in rows] == expected,
                "TOGO formulation drift",
            )
            step = STEP.replace("MgCl2 x 6H2O", "MgCl2\u30fb6H2O")
            runner.require(
                data["comments"] == [{"paragraph_index": 2, "comment": step}],
                "TOGO preparation drift",
            )
            result[key] = (rows, ["components", 0, "items"], step, ["comments", 0, "comment"])
        else:
            runner.require(data["status"] == 200 and data["count"] == 1, "API envelope drift")
            data = data["data"]
            base = ["data"]
            if key == "medium":
                runner.require(
                    data["medium"]["id"] == "J973"
                    and data["medium"]["name"] == "HALORHABDUS SEGORENSIS MEDIUM"
                    and data["medium"]["link"] == ORIGINAL
                    and data["medium"]["source"] == "JCM"
                    and len(data["solutions"]) == 1,
                    "MediaDive identity drift",
                )
                data = data["solutions"][0]
                base += ["solutions", 0]
            runner.require(
                data["id"] == 4996
                and data["name"] == "Main sol. J973"
                and data.get("volume") is None
                and [s["step"] for s in data["steps"]] == [STEP],
                "MediaDive preparation/volume drift",
            )
            runner.require(len(data["recipe"]) == len(ROWS), "MediaDive inventory drift")
            for i, (row, expected) in enumerate(zip(data["recipe"], ROWS, strict=True)):
                runner.require(
                    tuple(row.get(k) for k in ("compound", "compound_id", "amount", "attribute"))
                    == expected
                    and row["unit"] == "g"
                    and row["recipe_order"] == i + 1
                    and row["optional"] == 0
                    and all(
                        row.get(k) is None
                        for k in ("g_l", "mmol_l", "condition", "solution", "solution_id")
                    ),
                    "MediaDive amount/form drift",
                )
            result[key] = (data["recipe"], base + ["recipe"], STEP, base + ["steps", 0, "step"])
    return result


def build(before, key, timestamp):
    context = frozen()
    spec = next(r for r in context["records"] if r["key"] == key)
    runner.require(
        before == runner.load_yaml(spec["before_text"]) and before["id"] == spec["id"],
        "Unreviewed baseline",
    )
    cls, standalone = spec["target_class"], key == "solution"
    runner.require(
        runner.infer_target_class(before) == cls and not runner.errors(before, cls),
        "Baseline schema/class failure",
    )
    runner.require(
        not any(
            before.get(k)
            for k in ("solutions", "variants", "references", "evidence", "source_data")
        ),
        "Unreviewed topology/provenance",
    )
    checked = sources(context)
    rows, source_base, step, step_pointer = checked[key]
    src, meta = context["sources"][key]["raw"], context["sources"][key]["metadata"]
    togo = key.startswith("M")
    field = "composition" if standalone else "ingredients"
    local = before[field]
    name_key, amount_key = ("component_name", "volume") if togo else ("compound", "amount")
    runner.require(
        [n["preferred_term"] for n in local] == [r[name_key] for r in rows],
        "Ingredient identity/order drift",
    )
    expected_source = (
        "TOGO:" + key
        if togo
        else "mediadive.solution:4996" if standalone else "mediadive.medium:J973"
    )
    runner.require(
        (before["term"] if standalone else before["media_term"]["term"])["id"] == expected_source,
        "Local source accession drift",
    )
    runner.require(
        all(
            n["concentration"] == {"value": str(r[amount_key]), "unit": "G_PER_L"}
            for n, r in zip(local, rows, strict=True)
        ),
        "Old quantity drift",
    )
    if not standalone:
        runner.require(
            before["physical_state"] == ("SOLID_AGAR" if key == "M1024" else "LIQUID"),
            "Variant state drift",
        )
    if standalone:
        runner.require(before["preparation_notes"] == step, "Existing preparation drift")
    elif not togo:
        runner.require(
            before["preparation_steps"]
            == [{"step_number": 1, "action": "AUTOCLAVE", "description": step}],
            "Existing preparation drift",
        )

    after, claims = copy.deepcopy(before), []
    after[field] = []
    after["solutions"] = [
        {
            "preferred_term": MAGNESIUM,
            "composition": [],
            "notes": "Use the complete magnesium stock batch prepared to 0.5 L before autoclaving. This is its prepared batch volume, not a measured post-autoclave volume, working dose per liter, or final-medium volume. The actual volume added after autoclaving is unreported; no numeric working dose is asserted.",
            "preparation_notes": step.split(" Separately", 1)[0],
        },
        {
            "preferred_term": BASE,
            "composition": [],
            "notes": "Use the complete separately prepared remaining-components batch. The source specifies 500 ml water input, not a 500 ml final solution volume; no numeric stock working dose or final-medium concentration is inferred.",
            "preparation_notes": "Separately"
            + step.split(" Separately", 1)[1].split(" Autoclave", 1)[0],
        },
    ]
    root_pointer = ["source_data"] if standalone else []
    if standalone:
        after["source_data"] = {"origin": "MediaDive"}

    def claim(pointer, old_pointer, status, quote, locator, reason, evidence_pointer):
        old = runner.get_node(before, old_pointer) if old_pointer is not None else None
        parent = runner.get_node(after, pointer[:-1])
        new = parent.get(pointer[-1])
        explanation = f"{runner.field_name(pointer)}: {reason} {SCOPE} Locator={locator}; accessed={meta['accessed_at']}; capture SHA256={meta['sha256']}."
        entry = {
            "pointer": pointer,
            "old_pointer": old_pointer,
            "field": runner.field_name(pointer),
            "old_field": runner.field_name(old_pointer) if old_pointer else None,
            "ingredient": parent.get("preferred_term", "preparation"),
            "old": copy.deepcopy(old),
            "new": copy.deepcopy(new),
            "status": status,
            "reference": meta["url"],
            "snippet": quote,
            "locator": locator,
            "explanation": explanation,
            "evidence_pointer": evidence_pointer,
        }
        claims.append(entry)
        ev = runner.get_node(after, evidence_pointer).setdefault("evidence", [])
        if ev:
            runner.require(len(ev) == 1 and ev[0]["reference"] == meta["url"], "Evidence collision")
            ev[0]["explanation"] += "\n\nAdditional exact excerpt: " + quote + "\n" + explanation
        else:
            ev.append(
                {
                    "reference": meta["url"],
                    "supports": "SUPPORT",
                    "snippet": quote,
                    "explanation": explanation,
                }
            )

    makeup_note = "Distilled water is added as needed to make the magnesium stock up to 500.0 ml. This is a stock final-volume instruction, not 500 ml of water input. Its water amount remains unquantified."
    base_note = "Source input for the remaining-components preparation: 500 ml distilled water / 1000 ml per L = 0.5 L. This is not its final solution volume or the final-medium volume."
    base_water = copy.deepcopy(local[0]) if togo else {"preferred_term": "Distilled water"}
    base_water["concentration"] = {"value": "0.5", "unit": "L"}
    base_water["notes"] = (base_water.get("notes", "") + "\n\n" + base_note).strip()
    after["solutions"][1]["composition"].append(base_water)
    claim(
        ["solutions", 1, "composition", 0, "concentration"],
        [field, 0, "concentration"] if togo else None,
        "correct" if togo else "add",
        step,
        "$." + runner.field_name(step_pointer),
        base_note
        + (
            " The imported 1000 g/L water encoding conflates both preparation stages and is withdrawn."
            if togo
            else ""
        ),
        ["solutions", 1, "composition", 0],
    )

    for i, (old_node, row) in enumerate(zip(local, rows, strict=True)):
        if togo and i == 0:
            continue
        magnesium = i == (3 if togo else 1)
        si = 0 if magnesium else 1
        ci = len(after["solutions"][si]["composition"])
        pointer = ["solutions", si, "composition", ci]
        node = copy.deepcopy(old_node)
        after["solutions"][si]["composition"].append(node)
        source_pointer = source_base + [i]
        quote = amount_excerpt(src, source_pointer) if togo else json_excerpt(src, source_pointer)
        if magnesium:
            node["concentration"] = {"value": "406", "unit": "G_PER_L"}
            note = "Separate magnesium chloride hexahydrate stock before autoclaving: 203 g / (500.0 ml / 1000 ml per L) = 406 g/L. The former flattened 203 g/L was not a verified final-medium concentration. No final-medium concentration is calculated."
            status = "correct"
        else:
            del node["concentration"]
            note = f"Source amount: {row[amount_key]} g per remaining-components recipe batch, not per liter. The 500 ml quantity is water input, not final stock volume; the final mixed-medium volume is unreported. The former G_PER_L encoding is withdrawn."
            if not togo and row.get("attribute"):
                note += " Source material attribute: " + row["attribute"] + "."
            status = "remove_unsupported"
        node["notes"] = (node.get("notes", "") + "\n\n" + note).strip()
        reason = (
            note
            + f' Additional exact preparation excerpt: "{step}"; locator=$.'
            + runner.field_name(step_pointer)
            + "."
        )
        claim(
            pointer + ["concentration"],
            [field, i, "concentration"],
            status,
            quote,
            "$." + runner.field_name(source_pointer),
            reason,
            pointer,
        )

    mg_water = {"preferred_term": "Distilled water", "notes": makeup_note}
    after["solutions"][0]["composition"].append(mg_water)
    claim(
        ["solutions", 0, "composition", 1, "concentration"],
        None,
        "not_quantified",
        step,
        "$." + runner.field_name(step_pointer),
        makeup_note,
        ["solutions", 0, "composition", 1],
    )
    for si in (0, 1):
        stock = after["solutions"][si]
        claim(
            ["solutions", si, "concentration"],
            None,
            "not_quantified",
            step,
            "$." + runner.field_name(step_pointer),
            stock["notes"] + " " + stock["preparation_notes"],
            root_pointer,
        )
    if togo:
        after["preparation_steps"] = [
            {"step_number": 1, "action": "AUTOCLAVE", "description": step}
        ]
        claim(
            ["preparation_steps", 0, "description"],
            None,
            "add_stage",
            step,
            "$." + runner.field_name(step_pointer),
            "Restore the source's separate preparations, conditional agar instruction and separate autoclaving followed by combination. The existing liquid/solid state is preserved.",
            root_pointer,
        )
    if standalone:
        for c in runner.all_claims(before):
            if c["pointer"][0] == "ingredients":
                claims.append(
                    {
                        **c,
                        "old_pointer": c["pointer"] + ["concentration"],
                        "pointer": c["pointer"] + ["concentration"],
                        "new": c["old"],
                        "old_field": c["field"],
                        "explanation": "Legacy placeholder, not an actual source ingredient; preserved and unsupported.",
                    }
                )
    other = "medium" if togo else "M1023"
    other_source = context["sources"][other]
    other_step, other_pointer = checked[other][2:]
    runner.get_node(after, root_pointer)["evidence"].append(
        {
            "reference": other_source["metadata"]["url"],
            "supports": "SUPPORT",
            "snippet": other_step,
            "explanation": "Corroborates solutions[0] and solutions[1] preparation stages only. The same JCM973 transcription is preserved by another dataset; this does not independently establish the final-medium volume or validate a different formulation. Locator=$."
            + runner.field_name(other_pointer)
            + ". "
            + SCOPE,
        }
    )
    after["references"] = []
    for source_key in (key, other):
        source_meta = context["sources"][source_key]["metadata"]
        title = (
            "Halorhabdus Segorensis Medium"
            if source_key.startswith("M")
            else "HALORHABDUS SEGORENSIS MEDIUM" if source_key == "medium" else "Main sol. J973"
        )
        after["references"].append(
            {
                "reference": source_meta["url"],
                "title": title,
                "notes": f"source_type=dataset; discovery_mode=existing_record_reference; accessed_on={source_meta['accessed_at'][:10]}; capture_sha256={source_meta['sha256']}; original_recipe={ORIGINAL}. Original recipe page currently returns 'Nothing found.' Authors and publication year not supplied. Dataset-specific transcription, not a claim of original-page verification.",
            }
        )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source=meta["url"],
        notes="Restored two separately prepared JCM973 components from inspected dataset instructions. Rebased magnesium to its explicit 500 ml stock; withdrew unsupported mass-per-liter encodings while preserving exact batch masses. Kept makeup water unquantified and 500 ml base water separate. No final-medium volume, ontology IDs, physical-state changes or organism claims inferred. Historical provenance unchanged.",
        changes="; ".join(
            f"{c.get('old_field')} -> {c['field']}: {c['old']} -> {c['new']} ({c['status']})"
            for c in claims
        ),
    )
    runner.require(not runner.errors(after, cls), "Proposed schema failure")
    return after, claims


def process(root, plan_path, mode):
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    context = frozen()
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
            and plan["context_sha256"] == CONTEXT_SHA,
            "Plan drift",
        )
    records, pending = [], []
    for spec in context["records"]:
        path = root / spec["path"]
        runner.require(not path.is_symlink(), "Symlink target")
        current, before = path.read_bytes(), spec["before_text"].encode()
        runner.require(runner.sha(before) == spec["before_sha256"], "Baseline hash drift")
        after, claims = build(runner.load_yaml(before), spec["key"], plan["created_at"])
        output = runner.render(before.decode(), after)
        runner.require(current in (before, output), "Concurrent edit")
        records.append(
            {
                **spec,
                "action": ACTION,
                "after_text": output.decode(),
                "after_sha256": runner.sha(output),
                "claims": claims,
            }
        )
        pending.append((path, current, output))
    if mode != "preview":
        runner.require(records == plan["records"], "Frozen decision drift")
    plan["records"] = records
    runner.safe_targets(root, plan)
    runner.require(
        all(p.read_bytes() == c and not p.is_symlink() for p, c, _ in pending),
        "Concurrent edit before write",
    )
    if mode == "preview":
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


def reports(plan, applied):
    for r in plan["records"]:
        lines = [
            "# JCM973 Preparation Follow-Up",
            "",
            f"- Follow-up target: {r['path']}",
            f"- ID: {r['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {r['before_sha256']}",
            f"- Result SHA256: {r['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Hash-linked supplement to the existing exact-path report, not an additional unique review. All prior quantities, new water and stock quantities, and restored source preparation are covered. Unquantified stock/final-medium volumes remain unresolved. Source type=dataset; discovery=existing_record_reference; authors/year unknown. Baseline and proposed class-specific schema checks pass; see ../validation.json for wider gate results.",
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
        path = HERE / "records" / (r["key"] + ".md")
        path.parent.mkdir(exist_ok=True)
        path.write_text("\n".join(lines) + "\n")


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
        reports(plan, mode != "preview")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
