#!/usr/bin/env python3
"""Source-pinned P2 evidence and P8 original-methods stock corrections."""

from __future__ import annotations

import argparse
import copy
import datetime
import json
import subprocess
from collections import Counter
from decimal import Decimal
from pathlib import Path

import review_solution_concentration_evidence as runner
from review_public_direct_concentrations import HTMLTree, content, nodes, one

from culturemech.curate.curation_event import record_curation_event

ROOT = Path(__file__).resolve().parents[1]
ACTION = "CURATED_PUBLIC_STOCK_CONCENTRATIONS_FROM_SCOPED_SOURCES"
ACCESSED = "2026-10-07"
BASE = "https://mediadive.dsmz.de/medium/"
DOI = "doi:10.1007/s11104-022-05822-6"
PDF_URL = "https://hal.inrae.fr/hal-04370677v1/file/Submitted_version_LM.pdf"
PDF_FILE = "P8-P9-HAL-submitted.pdf"
PDF_SHA = "2788ca1a054d5ff67f02af146db31e0735153886d9c5de54c0c607629a9c9f1c"
METHOD_SHA = "4aa363d18e41ceac96d5a3183d7060ef76a036c2e76e55e4e46209faf33f3cea"
TITLE = (
    "Soil microbiota promotes early developmental stages of Phelipanche ramosa L. Pomel "
    "during plant parasitism on Brassica napus L."
)
AUTHORS = (
    "Lisa Martinez; Jean-Bernard Pouvreau; Gregory Montiel; Christophe Jestin; "
    "Philippe Delavault; Philippe Simier; Lucie Poulin"
)
P2_HANDOFF = ROOT / "reports/ingredient_concentration_curation/20261007-p2-claim-handoff.json"
P2_HANDOFF_SHA = "dc1057468dc6ac60335fa29cdf8e1ad76fc96dd71227bb4c2961e1b9b84ec9b5"
TARGETS = {
    "P2": {
        "path": "data/normalized_yaml/bacterial/taiyang_medium_no_9_prototype.yaml",
        "id": "CultureMech:010432",
        "name": "taiyang_medium_no_9_prototype",
        "title": "Taiyang Medium No.9 (prototype)",
        "before_sha256": "6f0af5cbde2378df09c65c04e464faad031284e475f67fd857a98d42ab9534c1",
        "semantic_sha256": "a6d29774cd22a24bc2ce0206f57f73aa08943829eca54e4cd8ca4bbad8a8c108",
        "source_sha256": "b8081b72d9351bd6e873c6c77484baccd7c01a39cd6bd4cd557ec3568e6eff85",
        "containers": {"sol-0": 16, "sol-124": 3, "sol-660": 10},
    },
    "P8": {
        "path": "data/normalized_yaml/bacterial/m9_sng_medium.yaml",
        "id": "CultureMech:010438",
        "name": "m9_sng_medium",
        "title": "M9-SNG medium",
        "before_sha256": "250cc259402cfc6454d35f34240ff492d027b548fee1773ac6f5b238f08d1af4",
        "semantic_sha256": "22863295b395bd30d26542a41baf5736a3b790c7bbac69fe3f30d05845df8987",
        "source_sha256": "6730f629992bfb0c3e536c4a535361b85415212a4717b3c81f930606c4461c39",
        "containers": {"sol-0": 4, "sol-NaN": 4},
    },
}
HEADER = ["Compound", "Amount", "Unit", "Conc. [g/L]", "Conc. [mM]"]
WATER_QUOTE = "make up to 100 ml with distilled water"
WATER_NOTES = (
    "Make up the haemin stock to 100 ml with distilled water after dissolving 50 mg "
    "haemin in 1 ml 1 N NaOH. The added water amount is not fixed at 100 ml; no "
    "numeric water concentration or volume is asserted."
)
P8_DOSES = [
    ("MgSO4 stock", "0.002", "2 mL of 24.65 g.L-1 MgSO4"),
    ("CaCl2 stock", "0.000010", "10 \u00b5L of 14.7 g.L-1 CaCl2"),
    ("Sinigrin stock", "0.002", "2 mL of 10 g.L-1 SNG"),
    ("M9 stock", "0.002", "2 mL of M9 solution"),
]
P8_COMPONENTS = [
    (0, 0, "MgSO4", "24.65", "24.65 g.L-1 MgSO4"),
    (1, 0, "CaCl2", "14.7", "14.7 g.L-1 CaCl2"),
    (2, 0, "Sinigrin", "10", "10 g.L-1 SNG"),
    (3, 0, "Na2HPO4", "64", "64 g.L-1 Na2HPO4"),
    (3, 1, "KH2PO4", "15", "15 g.L-1 KH2PO4"),
    (3, 2, "NaCl", "2.5", "2.5 g.L-1 NaCl"),
    (3, 3, "NH4Cl", "5", "5 g.L-1 NH4Cl"),
]


def semantic_sha(doc):
    return runner.sha(
        json.dumps(doc, sort_keys=True, ensure_ascii=True, separators=(",", ":")).encode()
    )


def read_page(raw, mid):
    spec = TARGETS[mid]
    runner.require(runner.sha(raw) == spec["source_sha256"], "Public page hash drift")
    tree = HTMLTree(raw.decode()).root
    datasets = [json.loads(content(n)) for n in nodes(tree, "script", type="application/ld+json")]
    dataset = one([d for d in datasets if d.get("@type") == "Dataset"])
    runner.require(
        dataset["identifier"]["value"] == mid
        and dataset["name"] == spec["title"]
        and dataset["url"] == BASE + mid,
        "Wrong dataset identity",
    )
    sections = [n for n in nodes(tree, "div") if "solution" in n["attrs"].get("class", "").split()]
    runner.require(
        {n["attrs"]["id"] for n in sections} == set(spec["containers"])
        and len(sections) == len(spec["containers"]),
        "Unreviewed stock topology",
    )
    tables, text = {}, []
    for section in sections:
        table = one(
            [
                t
                for t in nodes(section, "table")
                if "solution-table" in t["attrs"].get("class", "").split()
            ]
        )
        rows = nodes(table, "tr")
        runner.require([content(n) for n in nodes(rows[0], "th")] == HEADER, "Column meaning drift")
        data, steps = {}, []
        for row in rows[1:]:
            cells = [content(n) for n in nodes(row, "td")]
            text.append(" ".join(cells))
            if row["attrs"].get("class") == "step-row":
                steps.append(one(cells))
                continue
            rid = row["attrs"].get("id")
            runner.require(rid and rid not in data and len(cells) == 5, "Ambiguous ingredient row")
            data[rid] = {"cells": cells, "links": [n["attrs"]["href"] for n in nodes(row, "a")]}
        sid = section["attrs"]["id"]
        runner.require(len(data) == spec["containers"][sid], "Source membership drift")
        tables[sid] = {"rows": data, "steps": steps}
    main = one([n for n in sections if n["attrs"]["id"] == "sol-0"])
    scale = one(nodes(main, "input", id="main-sol-vol"))["attrs"]
    expected = "1000" if mid == "P2" else "6.1"
    runner.require(scale["value"] == scale["data-volume"] == expected, "Recipe control changed")
    runner.require(
        [content(n) for n in nodes(main, "span", **{"class": "input-group-text"})] == ["ml"],
        "Recipe control unit changed",
    )
    metadata = [[content(n) for n in nodes(row, "td")] for row in nodes(tree, "tr")]
    paragraphs = [content(n) for n in nodes(tree, "p")]
    text.extend(paragraphs)
    text.extend(" ".join(row) for row in metadata)
    return tables, metadata, "\n".join(text)


def read_article(path):
    from pypdf import PdfReader

    runner.require(runner.sha(path.read_bytes()) == PDF_SHA, "Author manuscript hash drift")
    reader = PdfReader(path)
    runner.require(len(reader.pages) == 42, "Manuscript page count drift")
    cover = " ".join(reader.pages[0].extract_text().split())
    title_page = " ".join(reader.pages[1].extract_text().split())
    method = " ".join(reader.pages[10].extract_text().split())
    runner.require(
        "hal-04370677v1" in cover
        and DOI.removeprefix("doi:") in cover
        and "December 8th" in title_page
        and "2022" in title_page,
        "Wrong manuscript provenance",
    )
    runner.require(runner.sha(method.encode()) == METHOD_SHA, "Method extraction/context drift")
    for quote in [
        *[r[-1] for r in P8_DOSES],
        *[r[-1] for r in P8_COMPONENTS],
        "10 mL of M9-sinigrin medium",
        "SNG; Sinigrin hydrate",
    ]:
        runner.require(quote in method, "Method quote missing")
    return method


def sources(folder, mid):
    tables, metadata, page = read_page((folder / f"{mid}-medium-page.html").read_bytes(), mid)
    docs = {BASE + mid: page}
    hashes = {f"{mid}-medium-page.html": TARGETS[mid]["source_sha256"]}
    if mid == "P8":
        docs[DOI] = read_article(folder / PDF_FILE)
        hashes[PDF_FILE] = PDF_SHA
    return {
        "tables": tables,
        "metadata": metadata,
        "docs": docs,
        "hashes": hashes,
        "sha256": runner.sha(json.dumps(hashes, sort_keys=True).encode()),
    }


def build(before, source, mid, timestamp):
    spec = TARGETS[mid]
    runner.require(
        semantic_sha(before) == spec["semantic_sha256"], "Unreviewed local formulation drift"
    )
    runner.require(not runner.errors(before, "MediaRecipe"), "Baseline schema failure")
    after, claims = copy.deepcopy(before), []
    context = (
        f"Accessed {ACCESSED}; captures={json.dumps(source['hashes'], sort_keys=True)}. "
        "Quotes decode HTML entities or PDF text glyphs and collapse whitespace. "
        "No chemical grounding, growth, density or unspecified percentage basis is inferred."
    )

    def claim(
        pointer,
        old,
        new,
        status,
        ref,
        snippet,
        locator,
        explanation,
        evidence_pointer,
        support="SUPPORT",
    ):
        runner.require(snippet in source["docs"][ref], "Unverified source excerpt")
        claims.append(
            {
                "pointer": pointer,
                "field": runner.field_name(pointer),
                "ingredient": runner.get_node(after, pointer[:-1]).get(
                    "preferred_term", before["original_name"]
                ),
                "old": copy.deepcopy(old),
                "new": copy.deepcopy(new),
                "status": status,
                "reference": ref,
                "snippet": snippet,
                "locator": locator,
                "evidence_pointer": evidence_pointer,
                "supports": support,
                "explanation": f"{runner.field_name(pointer)}: {explanation} {context}",
            }
        )

    if mid == "P2":
        raw = P2_HANDOFF.read_bytes()
        runner.require(runner.sha(raw) == P2_HANDOFF_SHA, "Reviewed P2 claim map drift")
        handoff = json.loads(raw)
        current = {c["field"]: c for c in runner.all_claims(before)}
        runner.require(
            len(current) == 28 and set(current) == {c["field"] for c in handoff["claims"]},
            "P2 claim coverage drift",
        )
        runner.require(before["physical_state"] == "SOLID_AGAR", "Agar condition changed")
        runner.require(
            "we do not curate or test the media" in source["docs"][BASE + mid]
            and "no valid reference is given" in source["docs"][BASE + mid],
            "Prototype disclaimer changed",
        )
        step = one(source["tables"]["sol-124"]["steps"])
        runner.require(
            WATER_QUOTE in step and "Dissolve 50 mg haemin in 1 ml 1 N NaOH" in step,
            "Haemin makeup changed",
        )
        for h in handoff["claims"]:
            c = current[h["field"]]
            runner.require(
                c["old"] == h["old"] == h["proposed"] and c["ingredient"] == h["ingredient"],
                "P2 local claim drift",
            )
            sid, rid = h["locator"].split(" / ")
            row = source["tables"][sid]["rows"][rid]["cells"]
            runner.require(" ".join(row) == h["snippet"], "P2 source row drift")
            label = (
                row[0]
                .removesuffix(" (filtrate sterilization)")
                .removesuffix(" (for solid plate medium)")
            )
            runner.require(label.lower() == c["ingredient"].lower(), "P2 row identity mismatch")
            value = Decimal(row[1])
            if row[2] == "mg/l":
                value /= 1000
            elif sid == "sol-124":
                value = value / (1000 if row[2] == "mg" else 1) / Decimal("0.100")
            runner.require(value == Decimal(c["old"]["value"]), "P2 arithmetic mismatch")
            scope = (
                h["calculation"] + " User-contributed, untested formulation; not journal evidence."
            )
            if sid == "sol-124":
                scope += (
                    f' Additional exact preparation excerpt: "{step}"; locator=sol-124 preparation.'
                )
            claim(
                c["pointer"] + ["concentration"],
                c["old"],
                c["old"],
                "evidence_only",
                BASE + mid,
                h["snippet"],
                h["locator"],
                scope,
                [] if len(c["pointer"]) == 2 and c["pointer"][0] == "solutions" else c["pointer"],
            )
        water = {
            "preferred_term": "Distilled water",
            "source": "MediaDive public Medium P2",
            "notes": WATER_NOTES,
        }
        after["solutions"][1]["composition"].append(water)
        claim(
            ["solutions", 1, "composition", 2, "concentration"],
            None,
            None,
            "not_quantified",
            BASE + mid,
            WATER_QUOTE,
            "sol-124 preparation",
            "Adds the omitted makeup-water ingredient and scoped notes; water concentration remains absent. "
            + WATER_NOTES,
            ["solutions", 1, "composition", 2],
        )
        runner.require(
            ["Author(s):", "Taiyang Jin"] in source["metadata"]
            and ["Published:", "21.06.23"] in source["metadata"],
            "P2 bibliography drift",
        )
        page_authors, year = "Taiyang Jin", 2023
    else:
        runner.require(
            before["physical_state"] == "LIQUID" and not before["ingredients"],
            "P8 base topology drift",
        )
        loc = "HAL v1 author manuscript, PDF page 11 (printed 10), lines 303-308"
        for si, ci, label, value, quote in P8_COMPONENTS:
            pointer = ["solutions", si, "composition", ci]
            node = runner.get_node(after, pointer)
            runner.require(node["preferred_term"] == label, "P8 stock ingredient identity drift")
            old = copy.deepcopy(node["concentration"])
            node["concentration"] = {"value": value, "unit": "G_PER_L"}
            claim(
                pointer + ["concentration"],
                old,
                node["concentration"],
                "correct" if old != node["concentration"] else "evidence_only",
                DOI,
                quote,
                loc,
                f"Directly reported stock strength for {label}, not final-medium concentration. "
                + (
                    'SNG is explicitly identified by the additional exact excerpt "SNG; Sinigrin hydrate" at the same locator. '
                    if label == "Sinigrin"
                    else ""
                ),
                pointer,
            )
        for si, (label, value, quote) in enumerate(P8_DOSES):
            node = after["solutions"][si]
            runner.require(node["preferred_term"] == label, "P8 dose order drift")
            old = copy.deepcopy(node["concentration"])
            node["concentration"] = {"value": value, "unit": "L"}
            dose = "10 microliters / 1000000 = 0.000010 L" if si == 1 else "2 ml / 1000 = 0.002 L"
            scope = f"{dose} per recipe batch. Replaces a rate derived from the unverified 6.1 ml page control with the article's explicit addition amount. Not a per-liter working concentration or final-medium dilution."
            claim(
                ["solutions", si, "concentration"],
                old,
                node["concentration"],
                "correct",
                DOI,
                quote,
                loc,
                scope,
                [],
            )
            old_note = node["notes"]
            node["notes"] = (
                f"Add {value} L of {label} per recipe batch. The L unit is a batch amount, not L/L. The manuscript describes 10 ml cultures; no fixed water makeup amount is inferred."
            )
            if si == 3:
                node[
                    "notes"
                ] += " The page-scoped M9 anchor is malformed NaN; no global solution accession is assigned."
            claim(
                ["solutions", si, "notes"],
                old_note,
                node["notes"],
                "correct_context",
                DOI,
                quote,
                loc,
                scope + ' Additional exact culture-scale excerpt: "10 mL of M9-sinigrin medium".',
                [],
            )
        for si, ci, note, quote in [
            (
                2,
                0,
                "The manuscript identifies SNG as sinigrin hydrate, without a hydration number. The 10 g/L value is the reagent stock strength; no molar conversion is asserted.",
                "SNG; Sinigrin hydrate",
            ),
            (
                3,
                1,
                "The DOI-linked author manuscript specifies 15 g/L KH2PO4 in M9 5X. The public P8 table instead reports 51.0 g/L; that conflicting dataset amount is retained as counterevidence, not adopted as a separate supported variant.",
                "15 g.L-1 KH2PO4",
            ),
        ]:
            ptr = ["solutions", si, "composition", ci]
            node = runner.get_node(after, ptr)
            old = node.get("notes")
            node["notes"] = note
            claim(ptr + ["notes"], old, note, "add_context", DOI, quote, loc, note, ptr)
        ptr = ["solutions", 3, "composition", 1]
        node = runner.get_node(after, ptr)
        old_source = node["source"]
        node["source"] = DOI
        claim(
            ptr + ["source"],
            old_source,
            DOI,
            "correct_source",
            DOI,
            "15 g.L-1 KH2PO4",
            loc,
            "The corrected value is attributed to the inspected article, not the disagreeing dataset row.",
            ptr,
        )
        row = source["tables"]["sol-NaN"]["rows"]["recipe-1"]["cells"]
        runner.require(
            row == ["KH2PO4", "51.0", "g/l", "51", "374.766"], "P8 counterevidence drift"
        )
        claim(
            ptr + ["concentration"],
            runner.get_node(before, ptr)["concentration"],
            node["concentration"],
            "conflicting_source",
            BASE + mid,
            " ".join(row),
            "sol-NaN / recipe-1",
            "Dataset row disagrees with the curated 15 g/L article amount. Original methods take precedence for the DOI-linked formulation. The discrepancy is explicit, not averaged or promoted to a new variant.",
            ptr,
            "REFUTE",
        )
        old_note = after["notes"]
        after[
            "notes"
        ] += " Curation now uses the DOI-linked HAL v1 manuscript for stock amounts and batch additions. The public page's 6.1 ml dose denominator is not retained; no final-medium component dilution or fixed makeup-water amount is inferred."
        claim(
            ["notes"],
            old_note,
            after["notes"],
            "correct_context",
            DOI,
            "10 mL of M9-sinigrin medium",
            loc,
            "Distinguishes the article's declared culture scale from the page control; keeps literal input doses without inventing a water amount.",
            [],
        )
        ref = after["references"][0]
        runner.require(
            ref == {"reference": DOI.removeprefix("doi:")}, "Unexpected existing DOI metadata"
        )
        ref.update(
            reference=DOI,
            title=TITLE,
            authors=AUTHORS,
            year=2023,
            notes=f"source_type=journal_article; discovery_mode=manual_web_search; accessed_on={ACCESSED}; version=HAL v1 author manuscript; full_text={PDF_URL}; deposit=2024-01-16; online publication=2022-12-08, volume year=2023. Methods page 11 (printed 10) visually inspected. Publisher methods and supplements were not inspected. Legacy bare DOI normalized, not a new publication.",
        )
        runner.require(["Published:", "09.01.24"] in source["metadata"], "P8 page year drift")
        page_authors = one(
            [r[1] for r in source["metadata"] if len(r) == 2 and r[0] == "Author(s):"]
        )
        year = 2024

    # One evidence item per reference/container, retaining each separately located quote.
    groups = {}
    for c in claims:
        groups.setdefault((tuple(c["evidence_pointer"]), c["reference"], c["supports"]), []).append(
            c
        )
    for (ptr, ref, support), group in groups.items():
        node = runner.get_node(after, ptr)
        evidence = node.setdefault("evidence", [])
        runner.require(
            not any(e["reference"] == ref for e in evidence),
            "Existing evidence needs reconciliation",
        )
        evidence.append(
            {
                "reference": ref,
                "supports": support,
                "snippet": group[0]["snippet"],
                "explanation": " ".join(
                    c["explanation"] + f' Exact excerpt: "{c["snippet"]}"; locator={c["locator"]}.'
                    for c in group
                ),
            }
        )
    runner.require(
        not any(r["reference"] == BASE + mid for r in after["references"]),
        "Page reference already present",
    )
    after["references"].append(
        {
            "reference": BASE + mid,
            "title": f"{spec['title']} - MediaDive public Medium {mid}",
            "authors": page_authors,
            "year": year,
            "notes": f"source_type=user_contributed_dataset_page; discovery_mode=existing_record_reference; accessed_on={ACCESSED}; year is the dataset-page publication year, not the journal year; legacy bacmedia reference retained. "
            + (
                "Untested prototype; no valid journal reference supplied."
                if mid == "P2"
                else "Retained as explicit counterevidence for the KH2PO4 stock conflict, not supporting the corrected amount."
            ),
        }
    )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source="; ".join(source["docs"]),
        changes="; ".join(
            f"{c['field']}: {json.dumps(c['old'], sort_keys=True)} -> {json.dumps(c['new'], sort_keys=True)} [{c['status']}]"
            for c in claims
        ),
        notes="Preserved stable ID, original history, ontology annotations, physical state, pH, preparation and variants. "
        + (
            "Added scoped evidence and unquantified haemin-stock makeup water; all existing amounts unchanged. "
            if mid == "P2"
            else "Corrected article-backed stock amounts/doses, notes and source attribution; normalized/enriched the existing DOI citation and preserved dataset counterevidence. "
        )
        + "No new growth associations or IDs.",
    )
    runner.require(not runner.errors(after, "MediaRecipe"), "Proposed schema failure")
    return after, claims


def process(
    root, folder, plan_path, mode, *, targets=None, action=None, source_reader=None, builder=None
):
    targets = TARGETS if targets is None else targets
    action = ACTION if action is None else action
    source_reader = sources if source_reader is None else source_reader
    builder = build if builder is None else builder
    runner.require(mode in {"preview", "apply", "verify"}, "Invalid mode")
    if mode == "preview":
        runner.require(not plan_path.exists(), "Refuse to overwrite a reviewed plan")
        plan = {
            "version": 1,
            "action": action,
            "target_class": "MediaRecipe",
            "commit": subprocess.check_output(
                ["git", "rev-parse", "HEAD"], cwd=root, text=True
            ).strip(),
            "created_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        }
        old_items = None
    else:
        plan = json.loads(plan_path.read_text())
        runner.require(
            plan["version"] == 1
            and plan["action"] == action
            and plan["target_class"] == "MediaRecipe",
            "Wrong plan",
        )
        old_items = plan["records"]
        runner.require(
            [r["medium_id"] for r in old_items] == list(targets), "Wrong reviewed targets"
        )
    items, pending = [], []
    for index, (mid, spec) in enumerate(targets.items()):
        path = root / spec["path"]
        runner.require(not path.is_symlink(), "Symlink target refused")
        current = path.read_bytes()
        before = current if old_items is None else old_items[index]["before_text"].encode()
        runner.require(runner.sha(before) == spec["before_sha256"], "Unreviewed baseline drift")
        source = source_reader(folder, mid)
        after, claims = builder(runner.load_yaml(before), source, mid, plan["created_at"])
        output = runner.render(before.decode(), after)
        runner.require(current in (before, output), "Concurrent edit")
        item = {
            "path": spec["path"],
            "id": spec["id"],
            "name": spec["name"],
            "medium_id": mid,
            "action": action,
            "before_text": before.decode(),
            "after_text": output.decode(),
            "before_sha256": runner.sha(before),
            "after_sha256": runner.sha(output),
            "source_sha256": source["sha256"],
            "source_accessed_at": ACCESSED,
            "claims": claims,
        }
        items.append(item)
        pending.append((path, current, output))
    if old_items is not None:
        runner.require(items == old_items, "Frozen plan/source/decision drift")
    plan["records"] = items
    runner.safe_targets(root, plan)
    for path, current, _ in pending:
        runner.require(
            path.read_bytes() == current and not path.is_symlink(), "Concurrent edit before write"
        )
    if mode == "preview":
        plan_path.parent.mkdir(parents=True, exist_ok=True)
        plan_path.write_text(json.dumps(plan, indent=2) + "\n")
    else:
        for path, current, output in pending:
            runner.require(
                path.read_bytes() == current and not path.is_symlink(),
                "Concurrent edit during apply",
            )
            if mode == "apply" and current != output:
                path.write_bytes(output)
            runner.require(path.read_bytes() == output, "Result not applied or differs")
    return plan, {
        "mode": mode,
        "records": len(items),
        "changed": sum(c != o for _, c, o in pending) if mode == "apply" else 0,
        "already_applied": sum(c == o for _, c, o in pending),
        "claims": dict(Counter(c["status"] for item in items for c in item["claims"])),
    }


def report(folder, plan, applied):
    for item in plan["records"]:
        lines = [
            f"# Public Stock Concentration Review: {item['name']}",
            "",
            f"- Record: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: `{plan['commit']}`",
            f"- State: {'applied locally' if applied else 'preview'}",
            f"- Before SHA256: `{item['before_sha256']}`",
            f"- Result SHA256: `{item['after_sha256']}`",
            f"- Source bundle SHA256: `{item['source_sha256']}`",
            "",
            "All ingredient and stock concentration claims, including unquantified water and conflicting evidence, are accounted below. Baseline/proposed schema checks pass. Wider terminal results and source limitations are in ../validation.json and ../README.md. No growth claims were added.",
            "",
            "| Field | Ingredient | Old | New | Status | DOI/PURL | Exact snippet | Locator | Decision | Action |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
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
                + (" | applied |" if applied else " | preview |")
            )
        path = folder / "records" / (item["name"] + ".md")
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text("\n".join(lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--plan", type=Path, required=True)
    parser.add_argument("--reports", type=Path)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--dry-run", action="store_true")
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    plan, result = process(ROOT, args.source_dir, args.plan, mode)
    if args.reports:
        report(args.reports, plan, mode != "preview")
    print(json.dumps(result, indent=2), flush=True)


if __name__ == "__main__":
    main()
