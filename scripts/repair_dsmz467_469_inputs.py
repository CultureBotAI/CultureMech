#!/usr/bin/env python3
"""Correct DSMZ 467 water inputs and restore DSMZ 469's filtered preparations."""

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
HERE = ROOT / "reports/ingredient_concentration_curation/20261007-dsmz467-469-inputs"
ACTION = "CORRECTED_DSMZ467_WATER_AND_DSMZ469_FILTERED_PREPARATIONS"
API = "https://mediadive.dsmz.de/rest/"
PDF = "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium{}.pdf"
HASHES = {
    API + "medium/467": "4cc8a7f8e8222c810dac9ca0f528d2e87025d890a2157de4d378bab51dd733e5",
    API + "medium/469": "5ca531fbbc4074a41bcbf759e584098a0a62205ce8cbbc20d1c06801955e2833",
    API + "solution/959": "477ac5c777599917f9fd0edc4cc4b019960f0a22c7bbb92164498e1f69b18404",
    API + "solution/961": "565cb49820743b205bf491e01a4f4c2dfdec8dfddf95ff5b873d6b07b0e47e3a",
}
PDF_HASHES = {
    "467": "31ad0e734637e5aa1086a814056ce5e3baecd59847eaedf24db0e91ccc89e8f6",
    "469": "a7da4f0650bedfcb0c353fe9ae83fd885641a14ed6565b62a6655db099855531",
}
STOCK_STEP = (
    "Add catalase and MgSO4 to 10 ml of distilled water each, and sterilize separately by filtration. "
    "Cool down autoclaved main solution to 50\u00b0C, and aseptically add catalase and MgSO4 solution."
)
STEP = "Adjust pH to 7.0. " + STOCK_STEP
ROWS = {
    "467": [
        ("Glucose", 5, 1, "g", "1"),
        ("Peptone", 1, 7.5, "g", "7.5"),
        ("Meat extract", 2, 5, "g", "5"),
        ("Yeast extract", 16, 2.5, "g", "2.5"),
        ("Casamino acids", 101, 2.5, "g", "2.5"),
        ("NaCl", 43, 5, "g", "5"),
        ("Tap water", 322, 1000, "ml", None),
    ],
    "469": [
        ("Yeast extract", 16, 5, "g", "5"),
        ("Malt extract", 116, 5, "g", "5"),
        ("K2HPO4", 10, 5.7, "g", "5.7"),
        ("MgSO4 x 7 H2O", 8, 0.2, "g", "0.2"),
        ("NH4H2PO4", 413, 1.2, "g", "1.2"),
        ("Catalase", 270, 60, "mg", "0.06"),
        ("Distilled water", 4, 980, "ml", None),
    ],
}
TARGETS = {
    "467-dsmz": (
        "ottow_medium.yaml",
        "001596",
        "419bd6d459a42237cd15ef710a3b84a6a75ddf4dca1cfca15ef06a7d40e00c95",
    ),
    "467-komodo": (
        "KOMODO_467_OTTOW_medium.yaml",
        "005580",
        "d53641e052d6ae8237d90a97e3b55d381d64cc0e806dba0583b4fed46830ace4",
    ),
    "467-solution": (
        "mediadive_959_Main_sol_467.yaml",
        "015296",
        "10d11f00b86ce7aa499ba6c3aa53a33c0b9060c6ed9e319c5675ca6e9903ae5b",
    ),
    "469-dsmz": (
        "ym_catalase_medium.yaml",
        "001598",
        "c3bddf0c73d78980ecda88d38bdd9552ce0deef4fee9314f551f484fdf835e4c",
    ),
    "469-komodo": (
        "KOMODO_469_YM-CATALASE_medium.yaml",
        "005582",
        "880a392bff5f4a81984f5ae45400fb1b121cfe1c97a2a186f3a07b26b360eace",
    ),
    "469-solution": (
        "mediadive_961_Main_sol_469.yaml",
        "015299",
        "d34f0dd73e4a1c6c005398e5af0c2f458591de059ed474f5ce0db94ca482a2f9",
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


def reference_for(key):
    mid, kind = key.split("-")
    return API + ("solution/" + str(int(mid) + 492) if kind == "solution" else "medium/" + mid)


def read_sources(medium_cache, solution_cache, mapping, pdf_dir):
    sources = {}
    for ref in HASHES:
        kind, sid = ref.removeprefix(API).split("/")
        raw, meta = (
            read_solution(solution_cache, int(sid))
            if kind == "solution"
            else read_medium(medium_cache, sid)
        )
        sources[ref] = {"raw": raw, "metadata": meta}
    rows = read_mapping(mapping, MAPPING_META)
    sources["mapping"] = {mid: rows[mid] for mid in ROWS}
    sources["mapping_metadata"] = copy.deepcopy(MAPPING_META)
    captured = json.loads(
        (
            HERE.parent / "20261007-komodo-media-1500-2000/original-source-crosschecks.json"
        ).read_text()
    )
    sources["pdfs"] = {s["medium_id"]: s for s in captured["sources"] if s["medium_id"] in ROWS}
    for mid, digest in PDF_HASHES.items():
        runner.require(
            runner.sha((pdf_dir / f"komodo-2000-pdf-{mid}.pdf").read_bytes()) == digest,
            "PDF capture hash drift",
        )
    check_sources(sources)
    return sources


def check_sources(sources):
    for ref, digest in HASHES.items():
        source = sources[ref]
        runner.require(
            runner.sha(source["raw"].encode()) == digest == source["metadata"]["sha256"],
            "Source hash drift",
        )
        runner.require(
            source["metadata"]["url"] == ref and source["metadata"]["http_status"] == 200,
            "Source identity drift",
        )
        kind, sid = ref.removeprefix(API).split("/")
        mid = str(int(sid) - 492) if kind == "solution" else sid
        data = json.loads(source["raw"])["data"]
        name = "OTTOW MEDIUM" if mid == "467" else "YM-CATALASE MEDIUM"
        if kind == "medium":
            runner.require(
                data["medium"]["id"] == int(mid)
                and data["medium"]["name"] == name
                and data["medium"]["source"] == "DSMZ"
                and data["medium"]["link"] == PDF.format(mid)
                and len(data["solutions"]) == 1,
                "Medium identity drift",
            )
            data = data["solutions"][0]
        runner.require(
            data["id"] == int(mid) + 492
            and data["name"] == "Main sol. " + mid
            and data["volume"] == 1000
            and len(data["recipe"]) == 7,
            "Recipe basis drift",
        )
        runner.require(
            [s["step"] for s in data["steps"]] == ["Adjust pH to 8.5." if mid == "467" else STEP],
            "Preparation drift",
        )
        for i, (row, expected) in enumerate(zip(data["recipe"], ROWS[mid], strict=True)):
            runner.require(
                [
                    row["compound"],
                    row["compound_id"],
                    row["amount"],
                    row["unit"],
                    None if row.get("g_l") is None else str(row["g_l"]),
                ]
                == list(expected)
                and row["recipe_order"] == i + 1
                and row["optional"] == 0
                and not any(row.get(k) for k in ("condition", "solution", "solution_id"))
                and row.get("attribute") == ("Sigma C-10" if mid == "469" and i == 5 else None),
                "Source ingredient/form/amount drift",
            )
    for mid in ROWS:
        mapping = sources["mapping"][mid]
        runner.require(
            mapping["medium_id"] == mid
            and mapping["original_recipe"] == PDF.format(mid)
            and mapping["cells"][:2]
            == [mid, "OTTOW medium" if mid == "467" else "YM-CATALASE medium"],
            "Mapping identity drift",
        )
        pdf = sources["pdfs"][mid]
        runner.require(
            pdf["reference"] == PDF.format(mid)
            and pdf["pdf_sha256"] == PDF_HASHES[mid]
            and pdf["pages"] == 1
            and pdf["http_status"] == 200,
            "PDF identity drift",
        )
        for quote in (
            ["Tap water 1000.0 ml"]
            if mid == "467"
            else [
                "Distilled water 1000.0 ml",
                "Catalase and MgSO4 are sterilized separately by filtration.",
            ]
        ):
            runner.require(quote in pdf["extracted_text"], "PDF excerpt drift")


def build(before, key, sources, timestamp):
    check_sources(sources)
    spec = TARGETS[key]
    mid, kind = key.split("-")
    is_solution = kind == "solution"
    field = "composition" if is_solution else "ingredients"
    ref = reference_for(key)
    raw = sources[ref]["raw"]
    base = ["data"] if is_solution else ["data", "solutions", 0]
    step_pointer = base + ["steps", 0]
    step_quote = json_excerpt(raw, step_pointer)
    runner.require(
        before["id"] == spec["id"] and not runner.errors(before, spec["target_class"]),
        "Record identity/schema drift",
    )
    runner.require(
        not before.get("solutions") and not before.get("variants"), "Unreviewed topology"
    )
    term = before["term"] if is_solution else before["media_term"]["term"]
    expected_id = (
        "mediadive.solution:" + str(int(mid) + 492)
        if is_solution
        else ("komodo" if kind == "komodo" else "mediadive") + ".medium:" + mid
    )
    runner.require(term["id"] == expected_id, "Local source drift")
    rows = before[field]
    runner.require(
        len(rows) == (6 if mid == "469" and not is_solution else 7), "Local inventory drift"
    )
    for node, row in zip(rows[:6], ROWS[mid][:6], strict=True):
        runner.require(
            node["preferred_term"] == row[0]
            and node["concentration"] == {"value": row[4], "unit": "G_PER_L"}
            and "notes" not in node,
            "Local ingredient/amount drift",
        )
    if len(rows) == 7:
        runner.require(
            rows[-1]["preferred_term"] == ROWS[mid][-1][0]
            and rows[-1]["concentration"]
            == {"value": str(ROWS[mid][-1][2]), "unit": "PERCENT_V_V" if is_solution else "G_PER_L"}
            and not rows[-1].get("evidence")
            and "notes" not in rows[-1],
            "Local water drift",
        )
    after = copy.deepcopy(before)
    claims, resolutions = [], []
    evidence_root = ["source_data"] if is_solution else []

    def claim(pointer, old_pointer, status, source_pointer, reason, evidence_pointer, ingredient):
        item = {
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
            "explanation": reason,
            "evidence_pointer": evidence_pointer,
            "ingredient": ingredient,
        }
        claims.append(item)
        return item

    if mid == "469":
        after[field] = [after[field][i] for i in (0, 1, 2, 4)] + (
            after[field][6:] if is_solution else []
        )
        after["solutions"] = []
        if is_solution:
            runner.require("source_data" not in after, "Existing provenance needs reconciliation")
            after["source_data"] = {"origin": "MediaDive"}
        for stock_index, old_index in enumerate((3, 5)):
            node = copy.deepcopy(rows[old_index])
            node.pop("concentration")
            amount = (
                "0.2 g MgSO4 x 7 H2O"
                if old_index == 3
                else "60 mg catalase (source attribute: Sigma C-10)"
            )
            node["notes"] = (
                f"Source batch input: {amount}, added to 10 ml distilled water and sterilized separately by filtration. "
                "The former flattened g/L slot is withdrawn at this separate preparation stage. "
                "No stock strength or final-medium concentration is asserted; final stock and medium volumes are unspecified."
            )
            stock = {
                "preferred_term": "Separately filtered "
                + ("magnesium sulfate" if old_index == 3 else "catalase")
                + " preparation",
                "composition": [node],
                "preparation_notes": STOCK_STEP,
                "notes": "The 10 ml is distilled-water input for this preparation, not final stock volume or a numeric addition dose. The two ingredients are filtered separately, not together. No filter pore size is specified.",
                "source": ref,
            }
            after["solutions"].append(stock)
            water = {
                "preferred_term": "Distilled water",
                "term": {"id": "mediadive.compound:4", "label": "Distilled water"},
                "concentration": {"value": "0.01", "unit": "L"},
                "notes": "10 ml distilled-water input for this separately filtered preparation; not a measured final stock volume.",
            }
            stock["composition"].append(water)
            claim(
                ["solutions", stock_index, "composition", 1, "concentration"],
                None,
                "add",
                step_pointer,
                "10 ml / 1000 ml per L = 0.01 L water input. Supports the water label and input-basis note; the source recipe identifies distilled water as compound 4. No density, final volume or per-liter dose is inferred.",
                ["solutions", stock_index, "composition", 1],
                "Distilled water",
            )
            for slot in ("preferred_term", "preparation_notes", "notes", "source"):
                claim(
                    ["solutions", stock_index, slot],
                    None,
                    "restore_stock",
                    step_pointer,
                    "Separate filtered preparation; the descriptor name is a curator label, not a new accession. The shared verbatim instruction distinguishes the two separately prepared stocks.",
                    evidence_root,
                    stock["preferred_term"],
                )
        for old_index in range(6):
            stock_index = {3: 0, 5: 1}.get(old_index)
            pointer = (
                ["solutions", stock_index, "composition", 0]
                if stock_index is not None
                else [field, (0, 1, 2, 4).index(old_index)]
            )
            node = runner.get_node(after, pointer)
            if stock_index is None:
                node["notes"] = (
                    f"Source input: {ROWS[mid][old_index][2]} g. The retained {ROWS[mid][old_index][4]} g/L "
                    "is the provider-reported nominal main-recipe rate (volume field 1000 ml), not a concentration in the 980 ml basal preparation or a measured final-medium concentration."
                )
            reason = (
                "Withdraw the flattened rate and retain the mass input at its separate filtration stage."
                if stock_index is not None
                else "Retain the provider-reported nominal recipe rate, with explicit stage limitation and current field scope."
            )
            c = claim(
                pointer + ["notes" if stock_index is not None else "concentration"],
                [field, old_index, "concentration"],
                "withdraw" if stock_index is not None else "evidence_only",
                base + ["recipe", old_index],
                reason + " " + node["notes"],
                pointer,
                node["preferred_term"],
            )
            c["explanation"] += (
                " Additional exact preparation excerpt at $."
                + runner.field_name(step_pointer)
                + ": "
                + step_quote
            )
            c["extra_excerpts"] = [
                {"snippet": step_quote, "locator": "$." + runner.field_name(step_pointer)}
            ]
            if rows[old_index].get("evidence"):
                resolutions.append(
                    {
                        "from_pointer": [field, old_index],
                        "to_pointer": pointer,
                        "reference": ref,
                        "disposition": "withdrawn" if stock_index is not None else "relocated",
                        "old_concentration": copy.deepcopy(rows[old_index]["concentration"]),
                        "new_field": c["field"],
                        "source_pointer": step_pointer,
                        "source_snippet": step_quote,
                        "reason": reason,
                    }
                )
        after["notes"] = (
            before.get("notes", "")
            + "\n\nPreparation scope: this record follows the MediaDive API allocation of 980 ml distilled water in the base and 10 ml for each separately filtered stock. "
            "The original DSMZ PDF lists 1000 ml distilled water without that allocation; it confirms separate filtration but does not independently specify 980/10/10. "
            "The API's nominal 1000 ml volume field and water-input sum are not measured final volumes. Stock strengths and numeric stock addition doses remain unasserted. "
            "Historical import annotations and ontology mappings are retained, not revalidated."
        ).lstrip()
        claim(
            ["notes"],
            ["notes"] if "notes" in before else None,
            "correct_scope",
            step_pointer,
            "API-specific preparation context; the water table is independently quoted on its node. Original-PDF detail difference is documented by separate PDF evidence.",
            evidence_root,
            "Preparation scope",
        )
        if kind != "solution":
            expected = (
                []
                if kind == "komodo"
                else [{"step_number": 1, "action": "AUTOCLAVE", "description": STEP}]
            )
            runner.require(
                before.get("preparation_steps", []) == expected, "Local preparation drift"
            )
            after["preparation_steps"] = [
                {"step_number": 1, "action": "ADJUST_PH", "description": STEP}
            ]
            claim(
                ["preparation_steps"],
                ["preparation_steps"] if expected else None,
                "correct_scope" if expected else "restore_preparation",
                step_pointer,
                "Retain the verbatim source instruction; the action names the opening pH adjustment, not autoclaving the filtered supplements. No pore size or autoclaving temperature/time is added.",
                evidence_root,
                "Preparation",
            )
        else:
            runner.require(before["preparation_notes"] == STEP, "Local preparation drift")

    if mid == "469" and not is_solution:
        after[field].append(
            {
                "preferred_term": "Distilled water",
                "term": {"id": "mediadive.compound:4", "label": "Distilled water"},
            }
        )
    water = after[field][-1]
    water["concentration"] = {"value": "1" if mid == "467" else "0.98", "unit": "L"}
    water["notes"] = (
        "1000 ml tap-water input per recipe batch; not a mass concentration, percentage, or measured final volume."
        if mid == "467"
        else "980 ml distilled-water input in the API main recipe, separate from 10 ml in each filtered stock; not a measured final volume. The PDF lists 1000 ml without this allocation."
    )
    water_pointer = [field, len(after[field]) - 1]
    claim(
        water_pointer + ["concentration"],
        [field, 6, "concentration"] if len(rows) == 7 else None,
        "correct" if len(rows) == 7 else "add",
        base + ["recipe", 6],
        f"{ROWS[mid][-1][2]} ml / 1000 ml per L = {water['concentration']['value']} L water input per batch. Supports the water label and input-basis note; no density, percentage or final-volume assumption.",
        water_pointer,
        water["preferred_term"],
    )
    grouped = {}
    for c in claims:
        grouped.setdefault(tuple(c["evidence_pointer"]), []).append(c)
    for pointer, group in grouped.items():
        node = runner.get_node(after, pointer)
        entries = [e for e in node.get("evidence", []) if e["reference"] == ref]
        runner.require(len(entries) <= 1, "Duplicate evidence")
        explanation = " ".join(
            f"{c['field']} ({c['status']}), locator={c['locator']}: {c['explanation']}"
            + (
                f" Additional exact excerpt: {c['snippet']}"
                if i and c["snippet"] != group[0]["snippet"]
                else ""
            )
            for i, c in enumerate(group)
        )
        explanation += f" Retrieved {sources[ref]['metadata']['accessed_at']}; response SHA256={HASHES[ref]}. Existing chemical mappings unchanged, not independently validated."
        if entries:
            runner.require(entries[0]["snippet"] == group[0]["snippet"], "Historical quote drift")
            entries[0]["explanation"] = (
                explanation
                + " Historical explanation (superseded where stage/scope differs): "
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
    pdf_node = water if mid == "467" else runner.get_node(after, evidence_root)
    pdf_node.setdefault("evidence", []).append(
        {
            "reference": PDF.format(mid),
            "supports": "SUPPORT",
            "snippet": (
                "Tap water 1000.0 ml"
                if mid == "467"
                else "Catalase and MgSO4 are sterilized separately by filtration."
            ),
            "explanation": (
                (
                    f"{runner.field_name(water_pointer)}.concentration and notes: page 1 water row independently confirms 1000 ml = 1 L input, not mass, percentage or final volume."
                )
                if mid == "467"
                else "notes and solutions[0:2].preparation_notes: page 1 confirms separate filtration. Additional exact page 1 water-row excerpt: Distilled water 1000.0 ml. Unlike the API, this PDF does not partition that water into base and stocks; the API allocation is explicitly attributed, not inferred from this PDF."
            )
            + f" Retrieved {sources['pdfs'][mid]['accessed_at']}; PDF SHA256={PDF_HASHES[mid]}.",
        }
    )
    if kind == "komodo" and mid == "469":
        after.setdefault("evidence", []).append(
            {
                "reference": MAPPING_URL,
                "supports": "SUPPORT",
                "snippet": sources["mapping"][mid]["snippet"],
                "explanation": f"Identity only: KOMODO {mid} maps to {PDF.format(mid)}; locator=MediaList row {mid}. No amount or growth claim comes from this mapping. Retrieved {MAPPING_META['accessed_at']}; response SHA256={MAPPING_META['sha256']}.",
            }
        )
    refs = [
        (
            ref,
            f"MediaDive {'solution ' + str(int(mid) + 492) if is_solution else 'medium ' + mid}: {'OTTOW MEDIUM' if mid == '467' else 'YM-CATALASE MEDIUM'}",
            "dataset",
            sources[ref]["metadata"]["accessed_at"],
            HASHES[ref],
        ),
        (
            PDF.format(mid),
            f"DSMZ {mid}. {'OTTOW MEDIUM' if mid == '467' else 'YM-CATALASE MEDIUM'}",
            "culture_collection_page",
            sources["pdfs"][mid]["accessed_at"],
            PDF_HASHES[mid],
        ),
    ]
    if kind == "komodo":
        refs.append(
            (
                MAPPING_URL,
                "KOMODO media list: original-recipe mappings",
                "dataset",
                MAPPING_META["accessed_at"],
                MAPPING_META["sha256"],
            )
        )
    for url, title, source_type, accessed, digest in refs:
        if any(r["reference"] == url for r in after.get("references", [])):
            continue
        after.setdefault("references", []).append(
            {
                "reference": url,
                "title": title,
                "notes": f"source_type={source_type}; discovery_mode={'cross_reference' if kind == 'komodo' else 'existing_record_reference'}; accessed_on={accessed[:10]}; response_sha256={digest}; individual authors and publication year not established. PDF copyright year is not a publication date. API-specific details are not silently attributed to the PDF.",
            }
        )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source="; ".join([ref, PDF.format(mid)] + ([MAPPING_URL] if kind == "komodo" else [])),
        notes="Corrected source water input units; for medium 469 restored separate filtered preparations and withdrew unsupported stock-rate interpretations. Preserved earlier history, snippets, mappings and variant links. API/PDF preparation-detail difference remains explicit; no growth association added.",
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
    for item in plan["records"]:
        lines = [
            "# Water Input And Preparation Follow-Up",
            "",
            f"- Follow-up target: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: {plan['commit']}",
            f"- Before SHA256: {item['before_sha256']}",
            f"- Result SHA256: {item['after_sha256']}",
            f"- State: {'applied locally' if applied else 'preview'}",
            "",
            "Hash-linked supplement to the existing exact-path report; no new unique reviewed path. All unchanged fields, historical evidence and variant links are retained. Baseline/proposed strict schema checks pass; wider checks are in validation.json.",
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
        before = runner.load_yaml(item["before_text"])
        field = "composition" if item["key"].endswith("solution") else "ingredients"
        if item["key"].startswith("467"):
            for i, node in enumerate(before[field][:6]):
                e = node["evidence"][0]
                lines.append(
                    "| "
                    + " | ".join(
                        runner.cell(v)
                        for v in (
                            f"{field}[{i}].concentration",
                            node["preferred_term"],
                            node["concentration"],
                            node["concentration"],
                            "verified",
                            e["reference"],
                            e["snippet"],
                            f"recipe[{i}]",
                            "Unchanged provider-reported nominal recipe rate; not proof of measured final volume.",
                        )
                    )
                    + " |"
                )
        else:
            for i in range(2):
                for slot in (
                    f"solutions[{i}].concentration",
                    f"solutions[{i}].composition[0].concentration",
                ):
                    lines.append(
                        "| "
                        + " | ".join(
                            runner.cell(v)
                            for v in (
                                slot,
                                "Stock dose/strength",
                                "see withdrawn input row",
                                None,
                                "unsupported",
                                reference_for(item["key"]),
                                STEP,
                                "steps[0]",
                                "Water input is not final stock volume or numeric working dose; left unasserted.",
                            )
                        )
                        + " |"
                    )
        if item["key"].endswith("solution"):
            lines.append(
                "| ingredients[0].concentration | Legacy placeholder | variable / VARIABLE | variable / VARIABLE | unsupported | unknown | unknown | unknown | Preserved import placeholder, not verified composition. |"
            )
        lines += [
            "",
            "Source copies are not independent scientific confirmations. No final-medium volume or new growth association is inferred. PDF authors/year remain unknown, not guessed.",
        ]
        folder.mkdir(parents=True, exist_ok=True)
        (folder / (item["key"] + "-followup.md")).write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("medium-cache", "solution-cache", "mapping", "pdf-dir", "plan"):
        parser.add_argument("--" + name, type=Path, required=True)
    parser.add_argument("--reports", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--verify", action="store_true")
    mode.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    sources = read_sources(args.medium_cache, args.solution_cache, args.mapping, args.pdf_dir)
    plan, outcome = process(
        ROOT, sources, args.plan, "apply" if args.apply else "verify" if args.verify else "preview"
    )
    if args.reports:
        report(args.reports, plan, args.apply or args.verify)
    print(json.dumps(outcome, indent=2))


if __name__ == "__main__":
    main()
