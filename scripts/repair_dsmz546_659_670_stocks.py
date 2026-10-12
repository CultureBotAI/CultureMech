#!/usr/bin/env python3
"""Restore source-explicit stocks in nine pinned DSMZ/KOMODO/solution records."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from decimal import Decimal
from pathlib import Path

import review_solution_concentration_evidence as runner
from inventory_komodo_concentration_sources import MAPPING_URL
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "reports/ingredient_concentration_curation"
HERE = BASE / "20261007-dsmz546-659-670-stocks"
HANDOFF = BASE / "20261007-dsmz650-752-762-preparations/next-stock-candidates.json"
HANDOFF_SHA = "ef6371f014182148ddeb2589de7a3e07ec56f22a45ea1816eb5b5de144425f13"
COHORT = BASE / "20261007-komodo-media-2000-2500/plan.json"
COHORT_SHA = "f5827bda6e5f7caf5fdb9faddc5f36e3955ee048fa0a066cc40e04ff3e1c4823"
ACTION = "CORRECTED_DSMZ546_659_670_STOCK_STAGES"
SIDS = {"546": 1205, "659": 1390, "670": 1413}
DIRECT = {"546": 4, "659": 7, "670": 4}
WATER = {"546": 4, "659": 7, "670": 5}
STOCKS = {"546": (5, 6), "659": (9,), "670": (4,)}
PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium{}.pdf"


def frozen():
    raw, cohort_raw = HANDOFF.read_bytes(), COHORT.read_bytes()
    runner.require(runner.sha(raw) == HANDOFF_SHA, "Handoff drift")
    runner.require(runner.sha(cohort_raw) == COHORT_SHA, "Mapping cohort drift")
    handoff, cohort = json.loads(raw), json.loads(cohort_raw)
    targets, bundle = {}, {}
    for group in handoff["groups"]:
        mid = group["medium_id"]
        if mid not in SIDS:
            continue
        runner.require(group["solution_id"] == SIDS[mid], "Solution accession drift")
        for kind, record in zip(("komodo", "medium", "solution"), group["records"], strict=True):
            key = mid + "-" + kind
            targets[key] = {
                "path": record["path"],
                "id": record["id"],
                "before_sha256": record["sha256"],
                "snapshot": record["record"],
                "target_class": "SolutionRecipe" if kind == "solution" else "MediaRecipe",
            }
            source_kind = "solution" if kind == "solution" else "medium"
            bundle[key] = {
                "raw": group[source_kind + "_raw"],
                "metadata": group[source_kind + "_metadata"],
            }
            if kind == "komodo":
                mapped = next(r for r in cohort["records"] if r["path"] == record["path"])
                runner.require(
                    mapped["source_sha256"] == bundle[key]["metadata"]["sha256"],
                    "Mapping source drift",
                )
                bundle[key].update(
                    mapping=mapped["mapping"], mapping_metadata=cohort["mapping_source"]
                )
    runner.require(len(targets) == 9, "Incomplete target inventory")
    return targets, bundle


def check_sources(bundle):
    _, expected = frozen()
    runner.require(bundle == expected, "Pinned source drift")
    for mid, sid in SIDS.items():
        parsed = {}
        for kind in ("medium", "solution"):
            source = bundle[mid + "-" + kind]
            raw, meta = source["raw"], source["metadata"]
            url = f"https://mediadive.dsmz.de/rest/{kind}/" + (
                str(sid) if kind == "solution" else mid
            )
            runner.require(
                runner.sha(raw.encode()) == meta["sha256"]
                and meta["http_status"] == 200
                and meta["url"] == meta["response_url"] == url,
                "Invalid source capture",
            )
            data = json.loads(raw)["data"]
            if kind == "medium":
                runner.require(
                    data["medium"]["id"] == int(mid)
                    and data["medium"]["source"] == "DSMZ"
                    and data["medium"]["link"] == PDF.format(mid)
                    and len(data["solutions"]) == 1,
                    "Wrong medium formulation",
                )
                data = data["solutions"][0]
            runner.require(
                data["id"] == sid and data["name"] == "Main sol. " + mid and data["volume"] == 1000,
                "Wrong preparation identity/basis",
            )
            parsed[kind] = data

        def clean(row):
            return {k: v for k, v in row.items() if v is not None}

        runner.require(
            [clean(r) for r in parsed["solution"]["recipe"]] == parsed["medium"]["recipe"]
            and [r["step"] for r in parsed["solution"]["steps"]]
            == [r["step"] for r in parsed["medium"]["steps"]],
            "Paired sources disagree",
        )
        mapping = bundle[mid + "-komodo"]["mapping"]
        runner.require(
            mapping["medium_id"] == mapping["cells"][0] == mid
            and mapping["original_recipe"] == PDF.format(mid),
            "Wrong KOMODO mapping",
        )


def build(before, key, bundle, timestamp):
    targets, expected = frozen()
    runner.require(bundle == expected, "Pinned source drift")
    spec = targets[key]
    runner.require(
        before == spec["snapshot"] and not runner.errors(before, spec["target_class"]),
        "Unreviewed baseline",
    )
    mid, kind = key.split("-")
    solution = kind == "solution"
    field = "composition" if solution else "ingredients"
    source = bundle[key]
    raw, meta = source["raw"], source["metadata"]
    ref = meta["url"]
    base = ["data"] if solution else ["data", "solutions", 0]
    data = runner.get_node(json.loads(raw), base)
    rows, steps = data["recipe"], [s["step"] for s in data["steps"]]
    runner.require(
        not any(k in before for k in ("solutions", "source_data", "evidence")),
        "Unexpected topology",
    )
    old_rows = before[field]
    indices = (
        list(range(len(rows))) if solution else [i for i in range(len(rows)) if i != WATER[mid]]
    )
    runner.require(len(indices) == len(old_rows), "Inventory drift")
    old_index = {src: local for local, src in enumerate(indices)}
    for i, node in zip(indices, old_rows, strict=True):
        runner.require(
            node["preferred_term"] == rows[i]["compound"] and "notes" not in node,
            "Chemical/context drift",
        )
        if solution:
            runner.require(
                node["term"]["id"] == f"mediadive.compound:{rows[i]['compound_id']}",
                "Compound identity drift",
            )
        for e in node.get("evidence", []):
            runner.require(
                e["reference"] == ref and e["snippet"] == json_excerpt(raw, base + ["recipe", i]),
                "Old evidence drift",
            )
    after, claims = copy.deepcopy(before), []
    after[field] = []
    after["solutions"] = []
    eroot = ["source_data"] if solution else []
    if solution:
        after["source_data"] = {"origin": "MediaDive"}

    def claim(pointer, old_pointer, status, src, reason, ep, extra=()):
        claims.append(
            {
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
                "evidence_pointer": ep,
                "ingredient": runner.get_node(after, ep).get(
                    "preferred_term", before.get("name", before.get("preferred_term"))
                ),
                "extra_excerpts": [
                    {"snippet": json_excerpt(raw, p), "locator": "$." + runner.field_name(p)}
                    for p in extra
                ],
            }
        )

    for i in range(DIRECT[mid]):
        node = copy.deepcopy(old_rows[old_index[i]])
        runner.require(
            Decimal(node["concentration"]["value"]) == Decimal(str(rows[i]["g_l"]))
            and node["concentration"]["unit"] == "G_PER_L",
            "Direct amount drift",
        )
        node["notes"] = (
            f"Source batch input: {rows[i]['amount']} {rows[i]['unit']}. Retained g/L is the provider-declared nominal main-recipe rate "
            "(volume field 1000 ml), not a separately prepared base or stock concentration, or an independently measured final-volume concentration."
        )
        after[field].append(node)
        claim(
            [field, i, "concentration"],
            [field, old_index[i], "concentration"],
            "evidence_only",
            base + ["recipe", i],
            node["notes"],
            [field, i],
            (base + ["volume"],),
        )

    # Keep lactose as a source-explicit final-medium claim, not an invented stock strength.
    if mid == "659":
        node = copy.deepcopy(old_rows[old_index[8]])
        runner.require(
            node["concentration"] == {"value": "8", "unit": "G_PER_L"}, "Lactose amount drift"
        )
        node["notes"] = (
            "Final-medium lactose target: 8.0 g/L, added after autoclaving as a filter-sterilized solution. Stock strength and addition volume are unspecified; 8 g/L is not the stock concentration."
        )
        after[field].append(node)
        claim(
            [field, 7, "concentration"],
            [field, old_index[8], "concentration"],
            "evidence_only",
            base + ["recipe", 8],
            node["notes"],
            [field, 7],
            (base + ["steps", 0],),
        )

    wi = WATER[mid]
    water = (
        copy.deepcopy(old_rows[old_index[wi]])
        if solution
        else {
            "preferred_term": rows[wi]["compound"],
            "term": {
                "id": f"mediadive.compound:{rows[wi]['compound_id']}",
                "label": rows[wi]["compound"],
            },
        }
    )
    value = format(Decimal(str(rows[wi]["amount"])) / 1000, "f")
    water["concentration"] = {"value": value, "unit": "L"}
    water["notes"] = (
        "Distilled-water input to the base per recipe batch, not final medium volume or stock carrier volume."
    )
    wp = [field, len(after[field])]
    after[field].append(water)
    claim(
        wp + ["concentration"],
        [field, old_index[wi], "concentration"] if solution else None,
        "correct" if solution else "add",
        base + ["recipe", wi],
        water["notes"]
        + f" Convert {rows[wi]['amount']} ml / 1000 = {value} L; no density assumption.",
        wp,
    )

    for j, si in enumerate(STOCKS[mid]):
        node = copy.deepcopy(old_rows[old_index[si]])
        strength, unit = ("40", "PERCENT_W_V") if mid == "670" else ("1", "MOLAR")
        node["concentration"] = {"value": strength, "unit": unit}
        node["notes"] = (
            "Source-explicit stock strength, not a final-medium concentration. The former flattened value is replaced at the stock stage; no molecular-weight or density conversion is inferred."
        )
        dose = format(Decimal(str(rows[si]["amount"])) / 1000, "f")
        stock = {
            "preferred_term": node["preferred_term"] + " stock",
            "composition": [node],
            "concentration": {"value": dose, "unit": "L"},
            "source": ref,
            "notes": f"{rows[si]['amount']} ml stock addition per recipe batch, not per liter of an inferred final medium. Carrier amount and final-medium concentration are not inferred.",
        }
        after["solutions"].append(stock)
        p = ["solutions", j, "composition", 0]
        sp = base + ["steps", 1 if mid == "546" else 0]
        claim(
            p + ["concentration"],
            [field, old_index[si], "concentration"],
            "correct_stock_basis",
            base + ["recipe", si],
            node["notes"],
            p,
            (sp,),
        )
        claim(
            ["solutions", j, "concentration"],
            None,
            "add",
            base + ["recipe", si],
            stock["notes"]
            + f" Convert ml / 1000 = {dose} L. Descriptor is a curator label, not a new accession.",
            eroot,
            (sp,),
        )
        if mid == "670":
            carrier = {
                "preferred_term": "H2SO4",
                "notes": "Stock carrier is 0.2 N H2SO4; carrier amount is unspecified. Normality is retained as source text because no NORMAL unit exists in the concentration enum. This is distinct from the 4 N reagent used to adjust base pH.",
            }
            stock["composition"].append(carrier)
            claim(
                ["solutions", 0, "composition", 1, "notes"],
                None,
                "schema_gap",
                base + ["recipe", si],
                carrier["notes"],
                ["solutions", 0, "composition", 1],
                (sp,),
            )

    if mid == "670":
        acid = {
            "preferred_term": "H2SO4",
            "notes": "Use 4 N H2SO4 to adjust the base to pH 2.2 before autoclaving; addition amount is not quantified. Normality is retained as text, not converted to an unsupported concentration unit. This is not the 0.2 N iron-stock carrier.",
        }
        ap = [field, len(after[field])]
        after[field].append(acid)
        claim(ap + ["notes"], None, "not_quantified", base + ["steps", 0], acid["notes"], ap)

    if not solution:
        actions = {"546": ("ADJUST_PH", "HEAT"), "659": ("ADJUST_PH",), "670": ("DISSOLVE",)}[mid]
        after["preparation_steps"] = [
            {"step_number": i + 1, "action": action, "description": steps[i]}
            for i, action in enumerate(actions)
        ]
        claim(
            ["preparation_steps"],
            ["preparation_steps"] if "preparation_steps" in before else None,
            "correct_preparation" if "preparation_steps" in before else "add_preparation",
            base + ["steps"],
            "Retain the source's preparation stages verbatim. For 670, filter sterilization applies to the iron stock; static incubation is preserved in notes, not labeled MIX.",
            eroot,
        )
    after["notes"] = (
        before.get("notes", "")
        + "\n\nStock follow-up: quantities distinguish base-water inputs, stock strengths and batch doses; no measured final volume or new growth claim is inferred. Existing chemical mappings and variant links are retained, not independently validated."
    ).lstrip()
    if mid == "670":
        after["notes"] += (
            " "
            + steps[1]
            + " This correction covers the base formulation only; strain-specific alternatives require separate review."
        )
    claim(
        ["notes"],
        ["notes"] if "notes" in before else None,
        "clarify_scope",
        base + ["steps"],
        "Document preparation scope and source limitations; retain the complete static-incubation instruction for 670.",
        eroot,
    )

    groups = {}
    for c in claims:
        groups.setdefault(tuple(c["evidence_pointer"]), []).append(c)
    for pointer, group in groups.items():
        node = runner.get_node(after, pointer)
        existing = node.get("evidence", [])
        runner.require(len(existing) <= 1, "Unreviewed evidence list")
        explanation = (
            " ".join(
                f"{c['field']} ({c['status']}), locator={c['locator']}: {c['explanation']}"
                + (" Additional exact excerpt: " + c["snippet"] if i else "")
                + "".join(
                    f" Additional exact excerpt at {q['locator']}: {q['snippet']}"
                    for q in c["extra_excerpts"]
                )
                for i, c in enumerate(group)
            )
            + f" Retrieved {meta['accessed_at']}; response SHA256={meta['sha256']}."
        )
        if existing:
            runner.require(
                existing[0]["reference"] == ref and existing[0]["snippet"] == group[0]["snippet"],
                "Historical evidence conflict",
            )
            existing[0]["explanation"] = (
                explanation
                + " Historical explanation (retained with preparation scope clarified): "
                + existing[0]["explanation"]
            )
        else:
            node["evidence"] = [
                {
                    "reference": ref,
                    "supports": "SUPPORT",
                    "snippet": group[0]["snippet"],
                    "explanation": explanation,
                }
            ]
    if kind == "komodo":
        runner.require("references" not in before, "Unexpected KOMODO bibliography")
        mapping, mm = source["mapping"], source["mapping_metadata"]
        after["evidence"].append(
            {
                "reference": MAPPING_URL,
                "supports": "SUPPORT",
                "snippet": mapping["snippet"],
                "explanation": f"KOMODO {mid} maps to {PDF.format(mid)}. Mapping evidence establishes source identity only, not ingredient amounts. Retrieved {mm['accessed_at']}; response SHA256={mm['sha256']}.",
            }
        )
        name = json.loads(raw)["data"]["medium"]["name"]
        after["references"] = [
            {
                "reference": ref,
                "title": f"MediaDive medium {mid}: {name}",
                "notes": f"source_type=dataset; discovery_mode=cross_reference; accessed_on={meta['accessed_at'][:10]}; response_sha256={meta['sha256']}; original_recipe={PDF.format(mid)}; individual authors and publication year not supplied.",
            },
            {
                "reference": MAPPING_URL,
                "title": "KOMODO - the Known Media Database",
                "notes": f"source_type=dataset; discovery_mode=cross_reference; accessed_on={mm['accessed_at'][:10]}; response_sha256={mm['sha256']}; locator=medium row {mid}; identity mapping only; individual authors and publication year not supplied.",
            },
        ]
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source=ref,
        notes="Restored source-explicit stock strengths/doses and base-water inputs; prior excerpts, history and mappings preserved. No strain-variant or growth curation is claimed.",
        changes="; ".join(
            f"{c['field']}: {json.dumps(c['old'])} -> {json.dumps(c['new'])} ({c['status']})"
            for c in claims
        ),
    )
    runner.require(not runner.errors(after, spec["target_class"]), "Proposed schema failure")
    return after, claims


def process(root, plan_path, mode):
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    targets, bundle = frozen()
    check_sources(bundle)
    if mode == "preview":
        runner.require(not plan_path.exists(), "Refuse plan overwrite")
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
            and [r["key"] for r in plan["records"]] == list(targets),
            "Plan drift",
        )
    records, pending = [], []
    for i, (key, spec) in enumerate(targets.items()):
        path = root / spec["path"]
        runner.require(not path.is_symlink(), "Symlink target")
        current = path.read_bytes()
        before = current if mode == "preview" else plan["records"][i]["before_text"].encode()
        runner.require(runner.sha(before) == spec["before_sha256"], "Baseline hash drift")
        after, claims = build(runner.load_yaml(before), key, bundle, plan["created_at"])
        output = runner.render(before.decode(), after)
        runner.require(current in (before, output), "Concurrent edit")
        records.append(
            {
                **{k: v for k, v in spec.items() if k != "snapshot"},
                "key": key,
                "action": ACTION,
                "before_text": before.decode(),
                "after_text": output.decode(),
                "after_sha256": runner.sha(output),
                "source_sha256": bundle[key]["metadata"]["sha256"],
                "claims": claims,
                "claim_resolutions": [],
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
        "claims": sum(len(r["claims"]) for r in records),
    }


def report(plan, applied):
    for item in plan["records"]:
        lines = [
            "# Stock-Stage Follow-Up",
            "",
            f"- Follow-up target: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Hash-linked supplement to the existing exact-path review, not a second unique review. Baseline/proposed schema checks pass; wider validation is recorded separately.",
            "",
            "| Field | Ingredient | Old | New | Status | DOI/PURL | Exact snippet | Locator | Decision |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for c in item["claims"]:
            rendered = dict(c)
            rendered["snippet"] += "".join(
                f" Additional exact excerpt at {q['locator']}: {q['snippet']}"
                for q in c["extra_excerpts"]
            )
            lines.append(
                "| "
                + " | ".join(
                    runner.cell(rendered[k])
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
        if item["key"].endswith("solution"):
            lines.append(
                "| ingredients[0].concentration | Legacy source placeholder | variable / VARIABLE | variable / VARIABLE | unsupported | unknown | unknown | unknown | Preserved placeholder; not a verified amount. |"
            )
        for c in item["claims"]:
            if c["status"] not in {"schema_gap", "not_quantified"}:
                continue
            lines.append(
                "| "
                + " | ".join(
                    runner.cell(value)
                    for value in (
                        runner.field_name(c["pointer"][:-1] + ["concentration"]),
                        c["ingredient"],
                        None,
                        None,
                        c["status"],
                        c["reference"],
                        c["snippet"],
                        c["locator"],
                        c["explanation"],
                    )
                )
                + " |"
            )
        if item["key"].endswith("komodo"):
            source = plan["sources"][item["key"]]
            lines += [
                "",
                "## Source Identity",
                "",
                f"Mapping source: {MAPPING_URL}; row {source['mapping']['medium_id']}. This links the exact original recipe, not an amount claim.",
                "",
                "```html",
                source["mapping"]["snippet"],
                "```",
            ]
        if item["key"].startswith("659"):
            lines += [
                "",
                "Lactose stock strength and stock dose: unsupported/unquantified; the cited preparation supplies only the 8.0 g/L final-medium target. No separate stock quantity is asserted.",
            ]
        if item["key"].startswith("670"):
            lines += [
                "",
                "Acid normalities are source text (schema gap); both acid addition amounts remain unquantified. The 0.2 N carrier and 4 N pH reagent are distinct. Linked strain variants remain outside this base-formulation repair.",
            ]
        if item["key"].endswith("solution"):
            lines += [
                "",
                "Legacy ingredients[0].concentration remains variable / VARIABLE: unsupported placeholder, not a verified amount. The authoritative inventory is composition plus nested solutions.",
            ]
        lines += [
            "",
            "Source versions are pinned in plan.json. Unknown authors/year remain unknown. Copies of one recipe are not independent scientific confirmations.",
        ]
        (HERE / (item["key"] + "-followup.md")).write_text("\n".join(lines) + "\n")


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
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
