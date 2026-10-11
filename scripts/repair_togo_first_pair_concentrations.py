#!/usr/bin/env python3
"""Review four pinned TOGO records; apply only corroborated JCM 954 input repairs."""

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
from review_public_direct_concentrations import HTMLTree, content, nodes, one

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-togo-first-pairs"
CONTEXT_SHA = "2add08d00b64bfa065f7a2a456e5c24111e8cfb4ffa22b66a1f27213ca170f92"
ACTION = "CORRECTED_TOGO_JCM954_INPUT_VOLUMES_AND_STOCK_STRENGTH"
MIDS = ["M1001", "M1002", "M1023", "M1024"]
JCM = "https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD="
API = "https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id="
AGAR = "For preparation of solid medium, add 20.0 g/L agar."
COOL = "Autoclave and, after cooling, add the following solutions (*filter-sterilized or autoclaved) to the medium."
JCM_ROWS = [
    ["MDS salt water (see Medium No. 574)", "767.0", "ml"],
    ["Yeast extract", "1.0", "g"],
    ["Fish peptone (Fluka)", "0.25", "g"],
    ["Sodium formate", "0.25", "g"],
    ["Sodium acetate", "0.25", "g"],
    ["Sodium lactate", "0.25", "g"],
    ["Sodium pyruvate", "0.25", "g"],
    ["Distilled water", "233.0", "ml"],
    ["1 M NH4Cl solution*", "5.0", "ml"],
    ["Potassium phosphate buffer (see Medium No. 574)", "2.0", "ml"],
]


def frozen():
    raw = (HERE / "inspected-context.json").read_bytes()
    runner.require(runner.sha(raw) == CONTEXT_SHA, "Inspected context drift")
    context = json.loads(raw)
    runner.require([r["key"] for r in context["records"]] == MIDS, "Wrong inventory")
    return context


def checked_source(context, mid):
    jcm = "954" if mid in MIDS[:2] else "973"
    sources = context["sources"]
    for key, url in [(mid, API + mid), ("JCM" + jcm, JCM + jcm)]:
        source = sources[key]
        meta = source["metadata"]
        runner.require(
            runner.sha(source["raw"].encode(meta["encoding"])) == meta["sha256"]
            and meta["url"] == meta["response_url"] == url
            and meta["http_status"] == 200,
            "Source capture drift",
        )
        datetime.datetime.fromisoformat(meta["accessed_at"])
    data = json.loads(sources[mid]["raw"])
    runner.require(
        data["meta"]["gm"] == "http://togomedium.org/medium/" + mid
        and data["meta"]["src_url"] == JCM + jcm
        and data["meta"]["original_media_id"]
        == "JCM_M" + jcm + ("-2" if mid in {"M1002", "M1024"} else ""),
        "Wrong source formulation",
    )
    tree = HTMLTree(sources["JCM" + jcm]["raw"]).root
    runner.require(content(one(nodes(tree, "title"))) == "Medium data", "Page title drift")
    if jcm == "954":
        rows = [[content(n) for n in nodes(row, "td")] for row in nodes(tree, "tr")]
        runner.require(rows == JCM_ROWS, "JCM table drift")
        page = content(one(nodes(tree, "body")))
        runner.require(
            "954 NEUTRAL OLIGOTROPHIC HALOARCHAEAL MEDIUM NO.3" in page
            and AGAR in page
            and COOL in page,
            "Preparation context drift",
        )
    else:
        runner.require(
            "Nothing found." in content(one(nodes(tree, "body"))) and not nodes(tree, "tr"),
            "JCM973 source status changed; revisit deferred decisions",
        )
    return data


def build(before, mid, timestamp):
    context = frozen()
    spec = one([r for r in context["records"] if r["key"] == mid])
    runner.require(before == runner.load_yaml(spec["before_text"]), "Unreviewed baseline")
    runner.require(not runner.errors(before, "MediaRecipe"), "Baseline schema failure")
    data = checked_source(context, mid)
    runner.require(
        before["id"] == spec["id"]
        and before["original_name"] == data["meta"]["name"]
        and before["media_term"]["term"]["id"] == "TOGO:" + mid
        and before["physical_state"] == ("SOLID_AGAR" if mid in {"M1002", "M1024"} else "LIQUID")
        and not before.get("variants"),
        "Record identity/topology drift",
    )
    after = copy.deepcopy(before)
    raw, meta = context["sources"][mid]["raw"], context["sources"][mid]["metadata"]
    claims = runner.all_claims(before)
    source_items = [
        (["components", si, "items", ri], row)
        for si, section in enumerate(data["components"])
        for ri, row in enumerate(section["items"])
    ]
    runner.require(len(source_items) == len(claims), "Source/local inventory differs")
    for claim in claims:
        pointer, name = claim["pointer"], claim["ingredient"]
        source_pointer, row = one([p for p in source_items if p[1]["component_name"] == name])
        runner.require(
            claim["old"] == {"value": str(row["volume"]), "unit": "G_PER_L"},
            "Unreviewed local quantity",
        )
        quote = amount_excerpt(raw, source_pointer)
        claim.update(
            new=copy.deepcopy(claim["old"]),
            reference=meta["url"],
            snippet=quote,
            source_pointer=source_pointer,
            locator="$." + runner.field_name(source_pointer),
            action_taken="unchanged",
        )
        if mid in MIDS[2:]:
            claim["explanation"] = (
                "Deferred: the original JCM973 page returns 'Nothing found.' TOGO's table "
                "is not a final-volume concentration: its preparation makes the magnesium "
                "solution up to 500 ml and dissolves the remaining components in 500 ml water, "
                "then autoclaves separately. Even agar is 20 g, not 20 g/L. The tabulated "
                "1000 ml water does not establish an exact water input or final mixed volume. "
                "A preparation-aware repair and original-source recovery remain necessary. "
                "TOGO $.comments[0].comment: " + data["comments"][0]["comment"]
            )
            continue
        node = runner.get_node(after, pointer)
        jcm_name = {
            "MDS salt water (see Medium [M578])": JCM_ROWS[0][0],
            "Potassium phosphate buffer (see Medium [M578])": JCM_ROWS[-1][0],
        }.get(name, name)
        if name == "agar":
            runner.require(mid == "M1002" and row["unit"] == "g/L", "Agar variant mismatch")
            primary_quote, primary_locator = AGAR, "Preparation paragraph after table 1"
            note = (
                "JCM954 explicitly specifies 20.0 g/L agar for the solid-medium preparation only."
            )
            claim.update(status="evidence_only", action_taken="added concentration evidence")
        else:
            primary_row = one([r for r in JCM_ROWS if r[0] == jcm_name])
            runner.require(
                Decimal(primary_row[1]) == Decimal(str(row["volume"]))
                and primary_row[2] == row["unit"],
                "TOGO/JCM amount conflict",
            )
            primary_quote = " ".join(primary_row)
            primary_locator = "Recipe table row: " + primary_row[0]
            if row["unit"] == "ml":
                value = format(Decimal(str(row["volume"])) / Decimal(1000), "f")
                node["concentration"] = {"value": value, "unit": "L"}
                note = (
                    f"Source batch input: {row['volume']} ml = {value} L. "
                    "This is an input volume, not g/L, ml/L, or a final-medium volume. "
                    "No density or final-volume assumption is made."
                )
                if pointer[0] == "solutions" and pointer[1] in {1, 2}:
                    note += (
                        " Add after autoclaving and cooling; stock strength is distinct from dose."
                    )
                claim.update(
                    status="correct",
                    new=copy.deepcopy(node["concentration"]),
                    action_taken="corrected batch volume",
                )
            else:
                runner.require(row["unit"] == "g", "Unreviewed source unit")
                note = (
                    f"JCM954 specifies {primary_row[1]} g per recipe batch for this component. "
                    "The existing G_PER_L value is retained but remains unverified: 767 ml "
                    "MDS salt water plus 233 ml water precede post-autoclave additions of "
                    "5 ml ammonium chloride stock and 2 ml phosphate buffer; no final "
                    "make-up volume is specified. The evidence supports this batch-mass "
                    "note only, not the retained final-medium concentration."
                )
                claim["action_taken"] = "added batch-mass note/evidence; concentration unchanged"
        node["notes"] = node.get("notes", "") + "\n\n" + note
        claim.update(explanation=note, primary_quote=primary_quote, primary_locator=primary_locator)
        evidence_pointer = [] if pointer[0] == "solutions" else pointer
        claim["evidence_pointer"] = evidence_pointer
        evidence_node = runner.get_node(after, evidence_pointer)
        scoped = f"{claim['field']} ({name}): {note}"
        if pointer[0] == "solutions":
            scoped += f' Separate JCM954 preparation excerpt: "{COOL}".'
        for reference, snippet, explanation in [
            (
                meta["url"],
                quote,
                scoped
                + f" Locator={claim['locator']}; source SHA256={meta['sha256']}; accessed={meta['accessed_at']}.",
            ),
            (
                JCM + "954",
                primary_quote,
                scoped
                + " Original-source locator="
                + primary_locator
                + ". "
                + "Capture SHA256="
                + context["sources"]["JCM954"]["metadata"]["sha256"]
                + "; accessed="
                + context["sources"]["JCM954"]["metadata"]["accessed_at"]
                + ".",
            ),
        ]:
            add_evidence(evidence_node, reference, snippet, explanation)

    if mid in MIDS[:2]:
        stock = after["solutions"][1]
        runner.require(stock["composition"] == [], "Unreviewed stock contents")
        pointer = ["solutions", 1, "composition", 0]
        field = runner.field_name(pointer + ["concentration"])
        note = "Explicit 1 M NH4Cl stock strength, not its final-medium concentration. The batch addition remains 5 ml; no final dilution is calculated."
        stock["composition"] = [
            {
                "preferred_term": "NH4Cl",
                "concentration": {"value": "1", "unit": "MOLAR"},
                "notes": note,
            }
        ]
        source_pointer = ["components", 1, "items", 0]
        quote = amount_excerpt(raw, source_pointer, strength=True)
        stock_row = data["components"][1]["items"][0]
        runner.require(
            stock_row["conc_value"] == 1 and stock_row["conc_unit"] == "M", "Stock strength drift"
        )
        explanation = (
            field
            + ": "
            + note
            + " Locator=$.components[1].items[0]; original JCM954 table 2 row 1."
        )
        add_evidence(stock["composition"][0], meta["url"], quote, explanation)
        add_evidence(stock["composition"][0], JCM + "954", " ".join(JCM_ROWS[8]), explanation)
        claims.append(
            {
                "pointer": pointer,
                "field": field,
                "ingredient": "NH4Cl",
                "old": None,
                "new": {"value": "1", "unit": "MOLAR"},
                "status": "add",
                "reference": meta["url"],
                "snippet": quote,
                "source_pointer": source_pointer,
                "locator": "$.components[1].items[0]",
                "primary_quote": " ".join(JCM_ROWS[8]),
                "primary_locator": "Recipe table 2 row 1",
                "explanation": note,
                "evidence_pointer": pointer,
                "action_taken": "added explicit stock composition strength",
            }
        )
        runner.require(
            "references" not in before and "evidence" not in before,
            "Existing root provenance requires reconciliation",
        )
        after["references"] = [
            {
                "reference": meta["url"],
                "title": data["meta"]["name"],
                "notes": f"source_type=dataset; discovery_mode=existing_record_reference; accessed_on={meta['accessed_at'][:10]}; accession={mid}; original_accession={data['meta']['original_media_id']}; response_sha256={meta['sha256']}. Authors and publication year not supplied.",
            },
            {
                "reference": JCM + "954",
                "title": "Medium data",
                "notes": "source_type=culture_collection_page; discovery_mode=cross_reference; accessed_on="
                + context["sources"]["JCM954"]["metadata"]["accessed_at"][:10]
                + "; recipe=954 NEUTRAL OLIGOTROPHIC HALOARCHAEAL MEDIUM NO.3. Authors and publication year not supplied; site copyright year is not a publication year.",
            },
        ]
        record_curation_event(
            after,
            curator="codex",
            action=ACTION,
            timestamp=timestamp,
            source=JCM + "954",
            changes="; ".join(
                f"{c['field']}: {c['old']} -> {c['new']} ({c['action_taken']})" for c in claims
            ),
            notes="Source-pinned TOGO/JCM954 pair. Corrected four batch-volume units; added explicit NH4Cl stock strength. Batch-mass notes do not validate retained G_PER_L values. No inferred final volume, organism claims, chemical mappings, or historical events changed.",
        )
    runner.require(not runner.errors(after, "MediaRecipe"), "Proposed schema failure")
    return after, claims


def amount_excerpt(raw, pointer, strength=False):
    """Quote only the consecutive identity/amount fields of the pinned JSON row."""
    obj = json_excerpt(raw, pointer)
    row = json.loads(obj)
    fields = ["component_name", "volume", "unit"]
    if strength:
        fields += ["conc_value", "conc_unit"]
    runner.require(list(row)[: len(fields)] == fields, "Source field order drift")
    excerpt = "\n".join(obj.splitlines()[1 : 1 + len(fields)])
    runner.require(
        json.loads("{" + excerpt.rstrip().removesuffix(",") + "}") == {k: row[k] for k in fields}
        and excerpt in raw,
        "Amount excerpt is not exact or complete",
    )
    return excerpt


def add_evidence(node, reference, snippet, explanation):
    entries = node.setdefault("evidence", [])
    existing = [e for e in entries if e["reference"] == reference]
    runner.require(len(existing) < 2, "Duplicate reference")
    if existing:
        existing[0]["explanation"] += (
            "\n\nAdditional exact excerpt: " + snippet + "\n" + explanation
        )
    else:
        entries.append(
            {
                "reference": reference,
                "supports": "SUPPORT",
                "snippet": snippet,
                "explanation": explanation,
            }
        )


def process(root, plan_path, mode, successors=()):
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    runner.require(not successors or mode == "verify", "Follow-ups are verify-only")
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
    followed = 0
    for spec in context["records"]:
        path = root / spec["path"]
        runner.require(not path.is_symlink(), "Symlink target")
        current, before = path.read_bytes(), spec["before_text"].encode()
        runner.require(runner.sha(before) == spec["before_sha256"], "Baseline hash drift")
        after, claims = build(runner.load_yaml(before), spec["key"], plan["created_at"])
        output = (
            before if after == runner.load_yaml(before) else runner.render(before.decode(), after)
        )
        records.append(
            {
                **spec,
                "action": ACTION,
                "after_text": output.decode(),
                "after_sha256": runner.sha(output),
                "claims": claims,
            }
        )
        if successors and current != output:
            runner.require(
                before == output and all(c["status"] == "unsupported" for c in claims),
                "Only unchanged unsupported historical records allow follow-ups",
            )
            expected, depth = runner.followup_result_hash(records[-1], successors)
            runner.require(depth > 0 and runner.sha(current) == expected, "Follow-up result drift")
            runner.require(
                not runner.errors(runner.load_yaml(current), spec["target_class"]),
                "Follow-up schema failure",
            )
            output = current
            followed += 1
        runner.require(current in (before, output), "Concurrent edit")
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
        "already_applied_or_unchanged": sum(c == o for _, c, o in pending),
        "claims": len([c for r in records for c in r["claims"]]),
        "followed_records": followed,
    }


def report(plan, applied):
    for r in plan["records"]:
        lines = [
            "# TOGO Concentration Review",
            "",
            f"- Record: {r['path']}",
            f"- ID: {r['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {r['before_sha256']}",
            f"- Result SHA256: {r['after_sha256']}",
            f"- State: {'applied/reviewed locally' if applied else 'preview'}",
            "- Source type: TOGO dataset; JCM culture collection page; discovery: existing_record_reference/cross_reference; accessed 2026-10-08; publication authors/year unknown.",
            "",
            "One row per existing concentration plus new stock strength. Baseline/proposed schema checks pass. Unsupported concentrations remain unverified, including where a batch-mass note was added. JCM973 is unavailable at its cited page and has a preparation/table conflict; no edits applied to that pair. See ../validation.json for wider checks, and ../inspected-context.json for source captures and all preparation text.",
            "",
            "| Field | Ingredient | Old | New | Status | DOI/PURL | Exact snippet | Locator | Decision | Action |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
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
                        "action_taken",
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
    parser.add_argument("--followup-plan", type=Path, action="append", default=[])
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--dry-run", action="store_true")
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    runner.require(
        not args.followup_plan or (args.verify and not args.reports),
        "Follow-ups require verify-only without reports",
    )
    successors = [r for p in args.followup_plan for r in json.loads(p.read_text())["records"]]
    plan, result = process(ROOT, args.plan, mode, successors)
    if args.reports:
        report(plan, mode != "preview")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
