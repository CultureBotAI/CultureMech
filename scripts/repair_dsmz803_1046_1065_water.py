#!/usr/bin/env python3
"""Correct nine source-pinned water inputs without inferring final volume."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from pathlib import Path

import review_solution_concentration_evidence as runner
from review_medium_concentration_evidence import json_excerpt

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
HERE = ROOT / "reports/ingredient_concentration_curation/20261008-dsmz803-1046-1065-water"
CONTEXT_SHA = "8ec4c3dae8b5a3a0ee707c6ee2757ae7bbf4f41984e15f270697afa21eb03d5b"
ACTION = "CORRECTED_DSMZ803_1046_1065_WATER_INPUT_UNITS"
SIDS = {"803": 1634, "1046": 2114, "1065": 2155}
STEPS = {"803": "pH 7.1.", "1046": "adjust pH 5.6", "1065": "Adjust pH to 7.2"}
QUOTES = {
    "803": "Tap water 1000.00 ml",
    "1046": "Tap water 1000.0 ml",
    "1065": "Sea water 1000.0 ml",
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
            and [s["step"] for s in data["steps"]] == [STEPS[mid]],
            "Preparation identity/context drift",
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
        and title in pdf["pages"][0]
        and QUOTES[mid] in pdf["pages"][0],
        "PDF corroboration drift",
    )
    mapping = group["mapping"]
    runner.require(
        mapping["medium_id"] == mid and mapping["original_recipe"] == pdf["reference"],
        "KOMODO mapping drift",
    )
    source_kind = "solution" if kind == "solution" else "medium"
    return parsed[source_kind], group[source_kind + "_raw"], group[source_kind + "_metadata"], title


def build(before, key, timestamp):
    record, group = frozen()[key]
    mid, kind = key.split("-")
    target_class = "SolutionRecipe" if kind == "solution" else "MediaRecipe"
    runner.require(
        before == runner.load_yaml(record["before_text"]) and before["id"] == record["id"],
        "Unreviewed baseline",
    )
    runner.require(not runner.errors(before, target_class), "Baseline schema failure")
    data, raw, meta, title = checked_source(group, kind)
    container = "composition" if kind == "solution" else "ingredients"
    nodes, rows = before[container], data["recipe"]
    runner.require(
        [n["preferred_term"] for n in nodes] == [r["compound"] for r in rows],
        "Ingredient inventory drift",
    )
    if kind == "solution":
        runner.require(
            before["term"]["id"] == f"mediadive.solution:{SIDS[mid]}"
            and before["preferred_term"] == data["name"]
            and before["preparation_notes"] == STEPS[mid],
            "Solution identity drift",
        )
        runner.require(
            all(
                n["term"]
                == {"id": f"mediadive.compound:{r['compound_id']}", "label": r["compound"]}
                for n, r in zip(nodes, rows, strict=True)
            ),
            "Source compound identity drift",
        )
    else:
        prefix = "komodo" if kind == "komodo" else "mediadive"
        runner.require(
            before["media_term"]["term"]["id"] == f"{prefix}.medium:{mid}", "Medium identity drift"
        )
    wi = {"803": 8, "1046": 2, "1065": 5}[mid]
    water, row = nodes[wi], rows[wi]
    label = "Sea water" if mid == "1065" else "Tap water"
    old = {"value": "1000", "unit": "PERCENT_V_V" if kind == "solution" else "G_PER_L"}
    runner.require(
        row["compound"] == label
        and row["compound_id"] == (286 if mid == "1065" else 322)
        and row["amount"] == 1000
        and row["unit"] == "ml"
        and row["optional"] == 0
        and all(not row.get(k) for k in ("condition", "attribute", "g_l", "mmol_l", "solution_id")),
        "Unreviewed water row",
    )
    runner.require(
        water["concentration"] == old and "notes" not in water and "evidence" not in water,
        "Water baseline drift",
    )
    after = copy.deepcopy(before)
    pointer = [container, wi]
    field = runner.field_name(pointer + ["concentration"])
    source_pointer = (["data"] if kind == "solution" else ["data", "solutions", 0]) + ["recipe", wi]
    quote = json_excerpt(raw, source_pointer)
    locator = "$." + runner.field_name(source_pointer)
    note = f"Source batch input: 1000 ml {label.lower()} = 1 L. This is an input volume, not a mass concentration, volume percentage or measured final-medium volume. No density or final-volume assumption is made."
    explanation = f"{field} ({label}): {note} Calculation: 1000 ml / 1000 ml per L = 1 L. Locator={locator}. Preparation context: {STEPS[mid]} Existing non-water amounts and chemical mappings are preserved, not newly validated by this water evidence. Retrieved {meta['accessed_at']}; response SHA256={meta['sha256']}."
    target = after[container][wi]
    target["concentration"] = {"value": "1", "unit": "L"}
    target["notes"] = note
    pdf = group["pdf"]
    target["evidence"] = [
        {
            "reference": meta["url"],
            "supports": "SUPPORT",
            "snippet": quote,
            "explanation": explanation,
        },
        {
            "reference": pdf["reference"],
            "supports": "SUPPORT",
            "snippet": QUOTES[mid],
            "explanation": f"{field} ({label}): original DSMZ recipe {mid}, page 1, water row. {note} Calculation: 1000 ml / 1000 ml per L = 1 L. The medium API explicitly links this recipe and solution {SIDS[mid]}; this is not an inference from a similar medium name. Retrieved {pdf['accessed_at']}; PDF SHA256={pdf['sha256']}.",
        },
    ]
    refs = after["references"]
    runner.require(
        sum(r["reference"] == meta["url"] for r in refs) == 1
        and not any(r["reference"] == pdf["reference"] for r in refs),
        "Reference needs reconciliation",
    )
    refs.append(
        {
            "reference": pdf["reference"],
            "title": title,
            "notes": f"source_type=culture_collection_protocol; discovery_mode=cross_reference; source_organization=DSMZ; accessed_on={pdf['accessed_at'][:10]}; locator=page 1, water row; PDF SHA256={pdf['sha256']}. Linked by the exact MediaDive medium record and verified KOMODO original-recipe mapping. Individual authors and publication year are not specified; the 2007 copyright notice is not treated as publication year.",
        }
    )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source=pdf["reference"],
        changes=f"{field}: 1000 {old['unit']} -> 1 L source batch input (1000 ml / 1000); added water-input note, two source snippets and original-recipe reference.",
        notes="Original DSMZ PDF and exact linked API recipe independently inspected. Preserved prior evidence/history, identifiers, non-water amounts, preparation, chemical mappings and parent/variant links. No final-volume, density, stock dilution or growth inference.",
    )
    claims = []
    for c in runner.all_claims(before):
        c = copy.deepcopy(c)
        if c["pointer"] == pointer:
            c.update(
                status="correct",
                new=target["concentration"],
                reference=meta["url"],
                snippet=quote,
                locator=locator,
                explanation=explanation,
                corroboration=target["evidence"][1],
                source_pointer=source_pointer,
            )
        else:
            n = runner.get_node(before, c["pointer"])
            entries = [e for e in n.get("evidence", []) if e["reference"] == meta["url"]]
            if entries:
                runner.require(
                    len(entries) == 1 and entries[0]["snippet"] in raw,
                    "Prior evidence/source drift",
                )
                e = entries[0]
                c.update(
                    status="verified",
                    new=c["old"],
                    reference=e["reference"],
                    snippet=e["snippet"],
                    locator="Existing evidence explanation",
                    explanation="Unchanged; existing source-scoped amount evidence retained. "
                    + e["explanation"],
                )
            else:
                c.update(
                    status="unsupported",
                    new=c["old"],
                    reference=None,
                    snippet=None,
                    locator=None,
                    explanation="Legacy placeholder remains unsupported and unchanged; not an ingredient amount.",
                )
        claims.append(c)
    runner.require(sum(c["status"] == "correct" for c in claims) == 1, "Wrong edit scope")
    runner.require(not runner.errors(after, target_class), "Proposed schema failure")
    return after, claims


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
        after, claims = build(runner.load_yaml(before), key, plan["created_at"])
        output = runner.render(before.decode(), after)
        runner.require(current in (before, output), "Concurrent edit")
        kind = spec["kind"]
        source_kind = "solution" if kind == "solution" else "medium"
        records.append(
            {
                **spec,
                "key": key,
                "action": ACTION,
                "target_class": "SolutionRecipe" if kind == "solution" else "MediaRecipe",
                "after_text": output.decode(),
                "after_sha256": runner.sha(output),
                "source_sha256": group[source_kind + "_metadata"]["sha256"],
                "claims": claims,
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
        "quantity_corrections": 9,
    }


def report(plan, applied):
    for r in plan["records"]:
        lines = [
            "# Water Input Follow-Up",
            "",
            f"- Follow-up target: {r['path']}",
            f"- ID: {r['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {r['before_sha256']}",
            f"- Result SHA256: {r['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Hash-linked supplement to the original exact-path report, not another unique review. All concentration slots are listed; only the water input changes. Schema checks pass; wider results are in ../validation.json.",
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
        for c in r["claims"]:
            if c.get("corroboration"):
                e = c["corroboration"]
                lines += [
                    "",
                    f"Original PDF corroboration: {e['reference']}",
                    "",
                    f"> {e['snippet']}",
                    "",
                    e["explanation"],
                    "",
                ]
        path = HERE / "records" / (r["key"] + ".md")
        path.parent.mkdir(parents=True, exist_ok=True)
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
        report(plan, mode != "preview")
    print(json.dumps(result), flush=True)


if __name__ == "__main__":
    main()
