#!/usr/bin/env python3
"""Restore reviewed, exact-source stock boundaries; default to a frozen preview."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from decimal import Decimal
from pathlib import Path

from fetch_medium_concentration_sources import API, read_capture
from fetch_solution_concentration_sources import load_yaml
from repair_mediadive_stock_concentration_evidence import cell, require, sha
from review_medium_concentration_evidence import json_excerpt
from review_solution_concentration_evidence import field_name, get_node, render, rounded_equal

from culturemech.curate.curation_event import record_curation_event
from culturemech.validation.write_validated import validate_recipe

ROOT = Path(__file__).resolve().parents[1]
ORIGINAL = Path(
    "reports/ingredient_concentration_curation/20261007-mediadive-media-0000-0500/plan.json"
)
ORIGINAL_SHA = "1ada7bec3dbf8c0a4bb2e448ab02750c2cfd126352f8488695ed34cf2a821f5c"
ACTION = "RESTORED_REVIEWED_MEDIUM_STOCK_BOUNDARIES"
PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium{}.pdf"
PDF_HASHES = {
    "79": "fa30638235b7c7bbe3ebf995ae0ad6cff524802e887d2750d5ce520a41f13984",
    "98": "ed72f0832f306618c096dd2458e9d07cfd0799b58240476727b5a4984d6551ed",
    "129": "0cc96a482ddf12da286edde02e76d510b4d92ff9e9e42eb3133a6f440b442fff",
    "260": "ab78dd71cbd8d2d91832258c3cda9ccde3c6344d87b1ac791892c257691bf291",
    "261": "abea799d50da431e0446e012179e4ef6144c6f239cc8db830e33abafbcf33596",
    "369": "cb7da859a785ac99638a2590b988241221a2b035de782e05785182d565c24ade",
    "452": "e0cc3cb64fcf765793ff9064a8de060201aa4a3f020881546f58094216f6426e",
    "27": "e9c7d7ca3bfea7e2300e746a51320e5b47b4f6aa2237abe840b01471af25d9a9",
}
CHAINS = {
    "79": ["79"],
    "98": ["98"],
    "129": ["129"],
    "260": ["260", "27"],
    "261": ["261", "260", "27"],
    "369": ["369", "261", "260", "27"],
    "452": ["452"],
}
DSMZ13_PDF_SHA = "5de6bdfb00d6a166c335f5df44f780408884678ecc130a5474eb7a5d80c59c95"


def decimal(value):
    require(not isinstance(value, bool), "Boolean is not an amount")
    result = Decimal(str(value))
    require(result.is_finite() and result > 0, "Nonpositive/nonfinite source amount")
    return result


def litres(value):
    return format((decimal(value) / 1000).normalize(), "f")


def build(doc, raw, metadata, mid, timestamp, *, chains=None, pdf_hashes=None):
    """Only an exact, unique, one-level source tree is eligible for this batch."""
    chains = CHAINS if chains is None else chains
    pdf_hashes = PDF_HASHES if pdf_hashes is None else pdf_hashes
    require(mid in chains, "Unreviewed source")
    require(not list(validate_recipe(doc, target_class="MediaRecipe")), "Baseline schema failure")
    data = json.loads(raw)["data"]
    medium, sources = data["medium"], data["solutions"]
    require(str(medium["id"]) == mid and medium["source"] == "DSMZ", "Source identity drift")
    require(medium["link"] == PDF.format(mid), "Source lineage drift")
    require(
        doc["media_term"]["term"] == {"id": "mediadive.medium:" + mid, "label": medium["name"]},
        "Local source identity drift",
    )
    require(
        doc["original_name"] == medium["name"] and medium["link"] in doc["notes"],
        "Local name/link drift",
    )
    require(
        not doc.get("solutions") and not doc.get("variants"), "Unreviewed local stocks/variants"
    )
    require(len(sources) > 1 and sources[0]["name"] == "Main sol. " + mid, "Main recipe drift")
    ids = [s["id"] for s in sources]
    require(len(set(ids)) == len(ids), "Repeated or cyclic stock identity")
    edges = [(ri, r) for ri, r in enumerate(sources[0]["recipe"]) if r.get("solution_id")]
    require([r["solution_id"] for _, r in edges] == ids[1:], "Shared/nested/orphan stock graph")
    after = copy.deepcopy(doc)
    after["ingredients"], after["solutions"] = [], []
    claims, used = [], []
    reference = API + mid

    def claim(pointer, old_pointer, status, source_pointer, evidence_pointer, explanation):
        claims.append(
            {
                "pointer": pointer,
                "old_pointer": old_pointer,
                "field": field_name(pointer),
                "old": (
                    copy.deepcopy(get_node(doc, old_pointer)) if old_pointer is not None else None
                ),
                "new": copy.deepcopy(get_node(after, pointer)),
                "status": status,
                "reference": reference,
                "snippet": json_excerpt(raw, source_pointer),
                "source_pointer": source_pointer,
                "locator": "$." + field_name(source_pointer),
                "evidence_pointer": evidence_pointer,
                "explanation": explanation,
            }
        )

    for si, source in enumerate(sources):
        require(
            isinstance(source.get("recipe"), list) and source["recipe"],
            "Missing source composition",
        )
        volume = decimal(source["volume"])
        require(isinstance(source.get("steps", []), list), "Malformed source steps")
        parent = ["ingredients"] if si == 0 else ["solutions", si - 1, "composition"]
        if si:
            ri, edge = edges[si - 1]
            require(
                edge["solution"] == source["name"] and edge["unit"] == "ml", "Stock name/unit drift"
            )
            require(
                edge.get("optional") == 0
                and not edge.get("condition")
                and not edge.get("attribute"),
                "Conditional stock dose",
            )
            after["solutions"].append(
                {
                    "preferred_term": source["name"],
                    "term": {"id": f"mediadive.solution:{source['id']}", "label": source["name"]},
                    "concentration": {"value": litres(edge["amount"]), "unit": "L"},
                    "composition": [],
                }
            )
            claim(
                ["solutions", si - 1, "concentration"],
                None,
                "add",
                ["data", "solutions", 0, "recipe", ri],
                [],
                f"Explicit {edge['amount']} ml / 1000 ml per L = {litres(edge['amount'])} L per receiving batch. The exact solution_id establishes this stock boundary; no final-volume dilution or dose from another medium is inferred.",
            )
        components = get_node(after, parent)
        for ri, row in enumerate(source["recipe"]):
            if row.get("solution_id"):
                require(si == 0 and not row.get("compound_id"), "Nested/ambiguous stock row")
                continue
            require(row.get("compound_id") and row.get("compound"), "Unidentified source row")
            require(
                row.get("optional") == 0 and not row.get("attribute"),
                "Conditional/attribute source row",
            )
            condition = row.get("condition")
            require(
                not condition
                or (condition == "for solid medium" and doc["physical_state"] == "SOLID_AGAR"),
                "Unreviewed physical-state condition",
            )
            pointer = parent + [len(components)]
            source_pointer = ["data", "solutions", si, "recipe", ri]
            if (row["compound_id"], row["compound"]) in {(4, "Distilled water"), (754, "Water")}:
                require(
                    row["unit"] == "ml" and not condition and row.get("g_l") is None,
                    "Ambiguous water amount",
                )
                components.append(
                    {
                        "preferred_term": row["compound"],
                        "term": {
                            "id": f"mediadive.compound:{row['compound_id']}",
                            "label": row["compound"],
                        },
                        "concentration": {"value": litres(row["amount"]), "unit": "L"},
                    }
                )
                claim(
                    pointer + ["concentration"],
                    None,
                    "add",
                    source_pointer,
                    pointer,
                    f"Explicit {row['amount']} ml water / 1000 ml per L = {litres(row['amount'])} L in this preparation batch. This is an addition amount, not a claim of final volume, stock strength, or percent basis.",
                )
                continue
            index = len(used)
            require(index < len(doc["ingredients"]), "Source has extra ingredient")
            node = doc["ingredients"][index]
            require(
                node["preferred_term"] == row["compound"] and row["compound"] not in used,
                "Ingredient inventory/order/form ambiguity",
            )
            require(
                not node.get("evidence"), "Existing ingredient evidence needs scope reconciliation"
            )
            require(
                node.get("notes", "").strip() == ("(for solid medium)" if condition else ""),
                "Unreviewed ingredient notes",
            )
            unit = row["unit"]
            require(unit in {"g", "mg", "g/l"}, "Unreviewed source unit")
            amount, rate = decimal(row["amount"]), decimal(row["g_l"])
            computed = (
                amount
                if unit == "g/l"
                else amount * (Decimal("0.001") if unit == "mg" else 1) / (volume / 1000)
            )
            require(rounded_equal(computed, rate), "Source rate arithmetic conflict")
            require(
                set(node["concentration"]) == {"value", "unit"}
                and node["concentration"]["unit"] == "G_PER_L"
                and decimal(node["concentration"]["value"]) == rate,
                "Local amount/basis drift",
            )
            used.append(row["compound"])
            components.append(copy.deepcopy(node))
            text = (
                f"Source solution {source['id']} ({source['name']}) explicitly reports g_l={row['g_l']}. "
                f"Arithmetic check: {row['amount']} {unit}; provider volume {source['volume']} ml; computed {computed} g/L. "
                f"Additional exact value at $.data.solutions[{si}].volume (ml): {json_excerpt(raw, ['data', 'solutions', si, 'volume'])}. "
                "The numeric value and chemical mappings are preserved. This supports the provider-declared preparation concentration, not an independently measured final volume or downstream dilution."
            )
            if si:
                text += f" Relocated from ingredients[{index}] into the explicitly linked stock; it is not a direct receiving-medium concentration."
            if row["compound"] in {"Potato", "air-dried garden soil", "Na2CO3"} and mid in {
                "98",
                "129",
            }:
                text += " This is the input loading for extract preparation, not a measured dissolved concentration after sieving/settling/centrifugation; the exact extraction instructions are preserved in preparation_notes."
            if condition:
                text += " The source's solid-medium condition is preserved and applies to the existing SOLID_AGAR record."
            claim(
                pointer + ["concentration"],
                ["ingredients", index, "concentration"],
                "relocate" if si else "evidence_only",
                source_pointer,
                pointer,
                text,
            )
    require(len(used) == len(doc["ingredients"]), "Unmatched local ingredient")
    # An explicit empty direct list is valid when all source ingredients are stocks.
    if not after["ingredients"]:
        from culturemech.merge.fingerprint import RecipeFingerprinter

        require(
            RecipeFingerprinter().fingerprint(after), "Stock-only recipe cannot be fingerprinted"
        )
    steps = [step["step"] for s in sources for step in s.get("steps", [])]
    require(
        [s["description"] for s in doc.get("preparation_steps", [])] == steps,
        "Preparation text/inventory drift",
    )
    require(
        [s["step_number"] for s in doc.get("preparation_steps", [])]
        == list(range(1, len(steps) + 1)),
        "Preparation order drift",
    )
    offset = len(sources[0].get("steps", []))
    main_steps = doc.get("preparation_steps", [])[:offset]
    if main_steps:
        after["preparation_steps"] = copy.deepcopy(main_steps)
    else:
        after.pop("preparation_steps", None)
    for si, source in enumerate(sources[1:], 1):
        n = len(source.get("steps", []))
        if n:
            pointer = ["solutions", si - 1, "preparation_notes"]
            after["solutions"][si - 1]["preparation_notes"] = "\n\n".join(
                s["step"] for s in source["steps"]
            )
            claim(
                pointer,
                None,
                "correct_stage",
                ["data", "solutions", si, "steps"],
                [],
                f"Move the exact texts from preparation_steps[{offset}:{offset+n}] into this stock's preparation stage. The receiving recipe's own remaining steps are unchanged; no new procedure is inferred.",
            )
            claims[-1].update(
                old=copy.deepcopy(doc["preparation_steps"][offset : offset + n]),
                old_field=f"preparation_steps[{offset}:{offset+n}]",
            )
        offset += n
    grouped = {}
    for c in claims:
        grouped.setdefault(tuple(c["evidence_pointer"]), []).append(c)
    for pointer, group in grouped.items():
        node = get_node(after, pointer)
        require(
            not any(e["reference"] == reference for e in node.get("evidence", [])),
            "Same-reference evidence collision",
        )
        texts = [
            f"{c['field']} ({c['status']}), locator={c['locator']}: {c['explanation']}"
            + (f" Additional exact excerpt: {c['snippet']}" if i else "")
            for i, c in enumerate(group)
        ]
        texts.append(
            f"Source retrieved {metadata['accessed_at']}; response SHA256={metadata['sha256']}. Original DSMZ PDF recipe chain visually cross-checked: {', '.join(chains[mid])}. Secondary ontology mappings and parent/variant relationships were preserved, not validated by this amount evidence."
        )
        node.setdefault("evidence", []).append(
            {
                "reference": reference,
                "supports": "SUPPORT",
                "snippet": group[0]["snippet"],
                "explanation": " ".join(texts),
            }
        )
    refs = [(reference, f"MediaDive medium {mid}: {medium['name']}", "dataset", metadata["sha256"])]
    refs += [
        (
            PDF.format(p),
            f"DSMZ medium {p}: official recipe",
            "culture_collection_page",
            pdf_hashes[p],
        )
        for p in chains[mid]
    ]
    for ref, title, kind, digest in refs:
        require(
            not any(r["reference"] == ref for r in after.get("references", [])),
            "Existing bibliography needs reconciliation",
        )
        after.setdefault("references", []).append(
            {
                "reference": ref,
                "title": title,
                "notes": f"source_type={kind}; discovery_mode=existing_record_reference; source_organization=DSMZ; accessed_on=2026-10-07; response_sha256={digest}; individual authors and publication year not established. PDF copyright is not a publication date.",
            }
        )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        source="; ".join(r[0] for r in refs),
        timestamp=timestamp,
        notes="Exact source graph, complete ingredient inventory, amounts, and original PDF recipe chain checked. Numeric concentrations and chemical mappings preserved; stock doses and water are explicit batch amounts. No final-medium stock dilution inferred. Parent/variant relationships remain separately unreviewed.",
        changes="; ".join(
            f"{c.get('old_field', c['old_pointer'])} -> {c['field']}: {c['old']} -> {c['new']} ({c['status']})"
            for c in claims
        ),
    )
    require(not list(validate_recipe(after, target_class="MediaRecipe")), "Proposed schema failure")
    return after, claims


def process(root, source_dir, plan_path, mode, *, cohort="stock-boundaries"):
    require(cohort in {"stock-boundaries", "dsmz13"}, "Unreviewed cohort")
    chains = CHAINS if cohort == "stock-boundaries" else {"13": ["13"]}
    pdf_hashes = PDF_HASHES if cohort == "stock-boundaries" else {"13": DSMZ13_PDF_SHA}
    original_raw = (root / ORIGINAL).read_bytes()
    require(sha(original_raw) == ORIGINAL_SHA, "Original review plan changed")
    selected = [r for r in json.loads(original_raw)["records"] if r["medium_id"] in chains]
    require(len(selected) == len(chains), "Duplicate/missing reviewed target")
    tracked = set(
        subprocess.check_output(["git", "ls-files", "-z", "data/normalized_yaml"], cwd=root)
        .decode()
        .split("\0")
    )
    if mode == "preview":
        require(not plan_path.exists(), "Do not overwrite a reviewed plan")
        plan = {
            "version": 1,
            "action": ACTION,
            "commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root)
            .decode()
            .strip(),
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
            "original_plan_sha256": ORIGINAL_SHA,
            "pdf_hashes": pdf_hashes,
            "records": [],
        }
    else:
        plan = json.loads(plan_path.read_text())
        require(
            plan["version"] == 1
            and plan["action"] == ACTION
            and plan["original_plan_sha256"] == ORIGINAL_SHA
            and plan["pdf_hashes"] == pdf_hashes,
            "Wrong plan",
        )
        require(
            [r["path"] for r in plan["records"]] == [r["path"] for r in selected],
            "Plan target drift",
        )
    for mid, digest in pdf_hashes.items():
        require(
            sha((source_dir / f"DSMZ_Medium{mid}.pdf").read_bytes()) == digest,
            "PDF capture changed",
        )
    writes, rebuilt = [], []
    for i, original in enumerate(selected):
        path, mid = root / original["path"], original["medium_id"]
        require(original["path"] in tracked and not path.is_symlink(), "Non-exact/symlink target")
        current = path.read_bytes()
        before = current if mode == "preview" else plan["records"][i]["before_text"].encode()
        require(
            sha(before) == original["before_sha256"] == original["after_sha256"],
            "Unreviewed baseline",
        )
        raw, meta = read_capture(source_dir / "sources", mid)
        require(meta["sha256"] == original["source_sha256"], "Reviewed source capture drift")
        doc = load_yaml(before)
        require(doc["id"] == original["id"], "Stable ID drift")
        after, claims = build(
            doc, raw, meta, mid, plan["created_at"], chains=chains, pdf_hashes=pdf_hashes
        )
        output = render(before.decode(), after)
        item = {
            "path": original["path"],
            "id": original["id"],
            "medium_id": mid,
            "before_text": before.decode(),
            "before_sha256": sha(before),
            "after_sha256": sha(output),
            "source_sha256": meta["sha256"],
            "source_accessed_at": meta["accessed_at"],
            "claims": claims,
        }
        rebuilt.append(item)
        require(current in (before, output), "Concurrent record edit")
        require(mode != "verify" or current == output, "Repair not applied")
        for c in claims:
            require(c["snippet"] == json_excerpt(raw, c["source_pointer"]), "Inexact excerpt")
            entries = [
                e
                for e in get_node(after, c["evidence_pointer"])["evidence"]
                if e["reference"] == c["reference"]
            ]
            require(
                len(entries) == 1 and c["field"] in entries[0]["explanation"], "Lost claim scope"
            )
            require(
                c["snippet"] == entries[0]["snippet"] or c["snippet"] in entries[0]["explanation"],
                "Lost snippet",
            )
        writes.append((path, current, output))
    if mode == "preview":
        plan["records"] = rebuilt
        plan_path.parent.mkdir(parents=True, exist_ok=True)
        plan_path.write_text(json.dumps(plan, indent=2) + "\n")
    else:
        require(rebuilt == plan["records"], "Plan decision/source metadata drift")
        # Validate every record before the first write; partial reruns are idempotent.
        for path, current, output in writes:
            require(path.read_bytes() == current, "Concurrent edit before write")
            if mode == "apply" and current != output:
                path.write_bytes(output)
            require(path.read_bytes() == output, "Persisted result differs")
    return plan, {
        "mode": mode,
        "records": len(writes),
        "changed": sum(a != b for _, a, b in writes) if mode == "apply" else 0,
        "already_applied": sum(a == b for _, a, b in writes),
        "scoped_claims": sum(len(r["claims"]) for r in rebuilt),
        "new_evidence_entries": sum(
            len({tuple(c["evidence_pointer"]) for c in r["claims"]}) for r in rebuilt
        ),
    }


def reports(folder, plan, applied):
    folder.mkdir(parents=True, exist_ok=True)
    for item in plan["records"]:
        lines = [
            "# Stock Boundary Follow-Up",
            "",
            f"- Follow-up target: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: `{plan['commit']}`",
            f"- Before SHA256: `{item['before_sha256']}`",
            f"- Result SHA256: `{item['after_sha256']}`",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "This supplements the existing per-record report, not a new unique reviewed path. Original unsupported findings remain historical; parent/variant and secondary identity mappings remain unreviewed.",
            "",
            "| Field | Old field | Old | New | Status | DOI/PURL | Exact snippet | Locator | Decision |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for c in item["claims"]:
            row = dict(
                c,
                old_field=c.get(
                    "old_field", field_name(c["old_pointer"]) if c["old_pointer"] else None
                ),
            )
            lines.append(
                "| "
                + " | ".join(
                    cell(row.get(k))
                    for k in (
                        "field",
                        "old_field",
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
        lines += ["", "See README.md and validation.json for verification and remaining gaps.", ""]
        (folder / f"{item['medium_id']}.md").write_text("\n".join(lines))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--reports", type=Path)
    parser.add_argument(
        "--cohort", choices=["stock-boundaries", "dsmz13"], default="stock-boundaries"
    )
    flags = parser.add_mutually_exclusive_group()
    flags.add_argument("--apply", action="store_true")
    flags.add_argument("--verify", action="store_true")
    flags.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    plan, outcome = process(ROOT, args.source_dir, args.plan, mode, cohort=args.cohort)
    if args.reports:
        reports(args.reports, plan, mode != "preview")
    print(json.dumps(outcome), flush=True)


if __name__ == "__main__":
    main()
