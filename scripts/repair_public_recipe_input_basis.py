#!/usr/bin/env python3
"""Source-pinned P7/P10 input-basis repairs and concentration evidence."""

from __future__ import annotations

import argparse
import copy
import json
from decimal import Decimal
from pathlib import Path

import review_public_stock_concentrations as shared
from review_public_direct_concentrations import HTMLTree, content, nodes, one

from culturemech.curate.curation_event import record_curation_event

runner = shared.runner
ROOT = Path(__file__).resolve().parents[1]
ACTION = "CORRECTED_PUBLIC_RECIPE_INPUT_BASES_WITH_SCOPED_EVIDENCE"
ACCESSED = "2026-10-07"
BASE = "https://mediadive.dsmz.de/medium/"
SNAPSHOT = (
    ROOT / "reports/ingredient_concentration_curation/20261007-public-medium-source-pages.json"
)
SNAPSHOT_SHA = "9b1238f4c428109f538a733605e34f22b9b3e577f065cac40f6f417f54605078"
TARGETS = {
    "P7": {
        "path": "data/normalized_yaml/bacterial/n27_rhodospirillaceae_medium_modified.yaml",
        "id": "CultureMech:010437",
        "name": "n27_rhodospirillaceae_medium_modified",
        "before_sha256": "99897389da7999ecdedfe0f9f776bb85fe4b41840681fb95d5bd24377a9dceff",
        "semantic_sha256": "7df3a4db4a0a51eb427a0eb1aa2b948af183227ffb1a732d6b26cf1b491951bb",
        "source_sha256": "ce4a93ee29dbf3008a4bfcedd4962718c0bd6feb95b38b2d5dc5951ed2a29dcd",
        "main": "sol-24",
        "stock": "sol-25",
        "authors": "Lorenz",
        "year": 2023,
    },
    "P10": {
        "path": "data/normalized_yaml/bacterial/bekisolidmedium_hydrogenovibrio_crunogenus_quimiolitotrofo.yaml",
        "id": "CultureMech:010430",
        "name": "bekisolidmedium_hydrogenovibrio_crunogenus_quimiolitotrofo",
        "before_sha256": "f82eec97665fa4bc2e18e96039523b8e68e461835c03b659cbac986a4324a1fb",
        "semantic_sha256": "0881e0ff3f80d9951f1849cf2cc7ce5f15b0d8792c57c4da9b575460da7035bc",
        "source_sha256": "f57ebb12ab9b45cdb3a746764fcd9e0a228e1dab2346b2ade67db95b477456ad",
        "main": "sol-0",
        "stock": "sol-1",
        "authors": "Alvarez Maqueda Rafael Alejandro Uriel, Cleto Gutierrez Miriam Rebeka",
        "year": 2024,
    },
}


def sources(folder, mid):
    spec = TARGETS[mid]
    snapshot = SNAPSHOT.read_bytes()
    runner.require(runner.sha(snapshot) == SNAPSHOT_SHA, "Source snapshot drift")
    expected = one([r for r in json.loads(snapshot)["records"] if r["medium_id"] == mid])
    raw = (folder / f"{mid}-medium-page.html").read_bytes()
    runner.require(runner.sha(raw) == spec["source_sha256"], "Source hash drift")
    tree = HTMLTree(raw.decode()).root
    datasets = [json.loads(content(n)) for n in nodes(tree, "script", type="application/ld+json")]
    dataset = one([d for d in datasets if d.get("@type") == "Dataset"])
    runner.require(dataset == expected["dataset"], "Dataset identity drift")
    sections = [n for n in nodes(tree, "div") if "solution" in n["attrs"].get("class", "").split()]
    runner.require(
        {n["attrs"]["id"] for n in sections} == {spec["main"], spec["stock"]}
        and len(sections) == 2,
        "Unreviewed solution topology",
    )
    tables, excerpts = {}, []
    for section in sections:
        sid = section["attrs"]["id"]
        table = one(
            [
                t
                for t in nodes(section, "table")
                if "solution-table" in t["attrs"].get("class", "").split()
            ]
        )
        expected_table = one([t for t in expected["recipe_tables"] if t["container_id"] == sid])
        rows = nodes(table, "tr")
        actual_rows = [
            (
                [
                    content(c)
                    for c in r["children"]
                    if isinstance(c, dict) and c["tag"] in {"td", "th"}
                ],
                r["attrs"],
            )
            for r in rows
        ]
        runner.require(
            actual_rows == [(r["cells"], r["attributes"]) for r in expected_table["rows"]],
            "Table or preparation drift",
        )
        runner.require(actual_rows[0][0] == shared.HEADER, "Table column meanings changed")
        controls = nodes(section, "input", id="main-sol-vol")
        badges = [
            n for n in nodes(section, "span") if "volume" in n["attrs"].get("class", "").split()
        ]
        runner.require(
            [n["attrs"] for n in controls] == expected_table["main_volume_controls"],
            "Main scale drift",
        )
        runner.require(
            [n["attrs"] for n in badges] == expected_table["volume_badges"], "Stock volume drift"
        )
        if sid == spec["main"]:
            runner.require(
                one(controls)["attrs"]["data-volume"] == "1000", "Main scale not 1000 ml"
            )
            runner.require(
                [content(n) for n in nodes(section, "span", **{"class": "input-group-text"})]
                == ["ml"],
                "Scale unit drift",
            )
        else:
            badge = one(badges)
            runner.require(
                content(badge) == "1000"
                and badge["attrs"]["title"] == "Final volume of this solution",
                "Stock final-volume declaration missing",
            )
        tables[sid] = {attrs["id"]: cells for cells, attrs in actual_rows if "id" in attrs}
        excerpts.extend(" ".join(cells) for cells, _ in actual_rows)
    metadata = [[content(n) for n in nodes(row, "td")] for row in nodes(tree, "tr")]
    runner.require(
        all(r["cells"] in metadata for r in expected["metadata_rows"]),
        "Bibliography metadata drift",
    )
    author_key = "Creator:" if mid == "P7" else "Author(s):"
    runner.require([author_key, spec["authors"]] in metadata, "Author attribution changed")
    paragraphs = " ".join(content(p) for p in nodes(tree, "p"))
    runner.require(
        "we do not curate or test the media" in paragraphs
        and "no valid reference is given" in paragraphs,
        "Source qualification changed",
    )
    return {"tables": tables, "excerpts": excerpts, "dataset": dataset, "sha256": runner.sha(raw)}


def build(before, source, mid, timestamp):
    spec = TARGETS[mid]
    runner.require(
        shared.semantic_sha(before) == spec["semantic_sha256"], "Unreviewed baseline semantics"
    )
    runner.require(
        before["id"] == spec["id"]
        and before["media_term"]["term"]["id"] == "mediadive.medium:" + mid,
        "Record identity mismatch",
    )
    runner.require(not runner.errors(before, "MediaRecipe"), "Baseline schema failure")
    after, claims = copy.deepcopy(before), []
    reference = BASE + mid
    context = (
        f"Source: user-contributed MediaDive {mid} page, accessed {ACCESSED}, SHA256={source['sha256']}. "
        "HTML entities decoded and whitespace collapsed; no curated collection recipe, journal validation or growth claim is implied."
    )

    def row(sid, rid):
        return source["tables"][sid][f"recipe-{rid}"]

    def claim(pointer, old, new, status, snippet, locator, why, evidence_pointer):
        runner.require(
            any(snippet in excerpt for excerpt in source["excerpts"]), "Unverified exact snippet"
        )
        node = runner.get_node(after, pointer[:-1])
        claims.append(
            {
                "pointer": pointer,
                "field": runner.field_name(pointer),
                "ingredient": node.get("preferred_term", before["original_name"]),
                "old": copy.deepcopy(old),
                "new": copy.deepcopy(new),
                "status": status,
                "reference": reference,
                "snippet": snippet,
                "locator": locator,
                "evidence_pointer": evidence_pointer,
                "supports": "SUPPORT",
                "explanation": f"{runner.field_name(pointer)}: {why} {context}",
            }
        )

    def edit(pointer, new, status, snippet, locator, why, evidence_pointer=None):
        parent = runner.get_node(after, pointer[:-1])
        old = copy.deepcopy(parent.get(pointer[-1]))
        if new is None:
            parent.pop(pointer[-1], None)
        else:
            parent[pointer[-1]] = copy.deepcopy(new)
        claim(
            pointer,
            old,
            new,
            status,
            snippet,
            locator,
            why,
            pointer[:-1] if evidence_pointer is None else evidence_pointer,
        )

    def water(container, value, snippet, locator, note, label="Distilled water"):
        ingredients = runner.get_node(after, container)
        runner.require(
            not any(n["preferred_term"] in {"Water", "Distilled water"} for n in ingredients),
            "Water already represented",
        )
        node = {
            "preferred_term": label,
            "source": "MediaDive public Medium " + mid,
            "notes": note,
        }
        if value is not None:
            node["concentration"] = {"value": value, "unit": "L"}
        ingredients.append(node)
        pointer = container + [len(ingredients) - 1]
        claim(
            pointer + ["concentration"],
            None,
            node.get("concentration"),
            "add" if value else "not_quantified",
            snippet,
            locator,
            note,
            pointer,
        )

    main, stock = spec["main"], spec["stock"]
    main_ids = [0, 1, 2, 4, 5, 6, 7, 8] if mid == "P7" else [1, 3, 4, 5, 6, 9, 13]
    for index, rid in enumerate(main_ids):
        node = after["ingredients"][index]
        cells = row(main, rid)
        runner.require(
            cells[0] == node["preferred_term"]
            and Decimal(cells[3]) == Decimal(node["concentration"]["value"])
            and node["concentration"]["unit"] == "G_PER_L",
            "Main ingredient mismatch",
        )
        why = (
            "Retains only the dataset's explicitly displayed Conc. [g/L] rate. "
            "The recipe also lists 1000 ml water; this is not independent evidence that final physical volume is 1 L. "
            "No final-volume conversion or stock-contribution addition was performed."
        )
        edit(
            ["ingredients", index, "concentration"],
            node["concentration"],
            "evidence_only",
            " ".join(cells),
            f"{main} / recipe-{rid}; Conc. [g/L] column",
            why,
        )

    si = 2 if mid == "P7" else 0
    for index, node in enumerate(after["solutions"][si]["composition"]):
        cells = row(stock, index)
        runner.require(cells[0] == node["preferred_term"], "Stock chemical form mismatch")
        loc = f"{stock} / recipe-{index} and volume badge title 'Final volume of this solution', value 1000; page scale ml"
        amount = Decimal(cells[1])
        runner.require(
            node["concentration"] == {"value": format(amount.normalize(), "f"), "unit": "G_PER_L"},
            "Stock amount mismatch",
        )
        quote = " ".join(cells)
        why = f"Stock, not final medium: source mass {cells[1]} g / declared 1 L stock = {node['concentration']['value']} g/L. The badge is a dataset volume declaration, not a measured volume. No working dilution is inferred."
        if mid == "P10" and index == 3:
            runner.require(
                cells[2] == "" and cells[3:] == ["-", "-"], "Copper missing-unit context changed"
            )
            quote = "**CuSO4 x 5 H2O**: Pesar 0.05 g."
            loc += "; sol-0 preparation step 3, substep 3.6"
            why += " The table's empty unit is not interpreted as grams; the preparation explicitly provides 0.05 g of the same pentahydrate."
        else:
            runner.require(
                cells[2] == "g" and Decimal(cells[3]) == amount, "Unsupported stock unit/rate"
            )
        edit(
            ["solutions", si, "composition", index, "concentration"],
            node["concentration"],
            "evidence_only",
            quote,
            loc,
            why,
        )

    if mid == "P7":
        for pointer, rid in [
            (["ingredients", 8], 17),
            (["solutions", 0], 3),
            (["solutions", 1], 9),
            (["solutions", 2], 10),
        ]:
            cells = row(main, rid)
            runner.require(cells[2] == "ml", "Batch liquid unit mismatch")
            amount = format((Decimal(cells[1]) / 1000).normalize(), "f")
            note = f"Source input {cells[1]} ml per listed recipe batch, represented as {amount} L, not L/L. The listed 1000 ml water is not an explicit final-medium makeup instruction."
            ptr = [] if pointer[0] == "solutions" else pointer
            edit(
                pointer + ["concentration"],
                {"value": amount, "unit": "L"},
                "correct",
                " ".join(cells),
                f"{main} / recipe-{rid}",
                note,
                ptr,
            )
            prior_note = runner.get_node(after, pointer).get("notes", "")
            had_note = bool(prior_note)
            # Replace the SL-6 per-liter assertion; preserve other literal stock-input notes.
            if pointer == ["solutions", 2]:
                prior_note = ""
            edit(
                pointer + ["notes"],
                (prior_note + " " + note).strip(),
                "correct_context" if had_note else "add_context",
                " ".join(cells),
                f"{main} / recipe-{rid}",
                note,
                ptr,
            )
        for index, rid, note in [
            (
                0,
                3,
                "The source states 0.1% Fe(III) citrate in H2O without a mass/volume, mass/mass or volume/volume basis. Removed the unsupported 1 g/L assertion; no numeric percentage or final-medium concentration is inferred.",
            ),
            (
                1,
                9,
                "Source stock inputs are 10 mg Vitamin B12 in 100 ml H2O. This specifies solvent input, not final stock makeup. Removed the unsupported 0.1 g/L assertion; the 10 mg batch mass is retained here because no mass-only concentration unit exists in the schema.",
            ),
        ]:
            pointer = ["solutions", index, "composition", 0]
            quote, loc = " ".join(row(main, rid)), f"{main} / recipe-{rid} stock label"
            edit(pointer + ["concentration"], None, "correct", quote, loc, note)
            edit(pointer + ["notes"], note, "add_context", quote, loc, note)
        water(
            ["solutions", 0, "composition"],
            None,
            "0.1% in H2O",
            f"{main} / recipe-3",
            "Water is the stated stock solvent; its amount and the percent basis are unspecified. No water quantity is asserted.",
            label="Water",
        )
        water(
            ["solutions", 1, "composition"],
            "0.1",
            "10 mg in 100 ml H2O",
            f"{main} / recipe-9",
            "Stock solvent input: 100 ml H2O = 0.1 L for 10 mg B12; not final-stock volume or L/L. No concentration of B12 is derived.",
            label="Water",
        )
        water(
            ["solutions", 2, "composition"],
            "1",
            " ".join(row(stock, 7)),
            f"{stock} / recipe-7",
            "Reported water input: 1000 ml = 1 L per listed SL-6 stock batch; not L/L. The separate final-volume badge declares 1000 ml; the source does not specify a makeup procedure.",
        )
        water(
            ["ingredients"],
            "1",
            " ".join(row(main, 13)),
            f"{main} / recipe-13",
            "Reported water input: 1000 ml = 1 L per listed main recipe batch; not final-medium volume or L/L. The other listed liquid inputs total 6.9 ml; no 1006.9 ml final volume is inferred.",
        )
        new_note = "MediaDive public P7 lists main ingredients, three stocks and 1000 ml water. Retained g/L values are dataset-reported rates, not verified physical final-medium concentrations. Liquid doses are recorded as batch inputs. Iron-citrate percentage basis and B12 final stock volume are unresolved; no final-medium dilution is inferred."
        edit(
            ["notes"],
            new_note,
            "correct_context",
            " ".join(row(main, 13)),
            f"{main} / recipe-13 and all main table rows",
            new_note,
            [],
        )
    else:
        quote, loc = " ".join(row(main, 8)), f"{main} / recipe-8"
        note = "The inspected HTML reports Elemento traza as 'trace' with no unit or numerical dose. Removed the VARIABLE assertion: no fixed, zero or variable-range quantity is established. Stock concentrations are not final-medium trace concentrations."
        edit(["solutions", 0, "concentration"], None, "correct", quote, loc, note, [])
        edit(["solutions", 0, "notes"], note, "correct_context", quote, loc, note, [])
        note = "MediaDive public P10 reports main-ingredient rates in g/L, but preparation starts with 1 L water, not an explicit final-volume makeup. The trace-stock dose is undisclosed ('trace'); no numeric or VARIABLE dose and no final-medium trace dilution is asserted. Existing physical state and pH are unchanged."
        edit(["notes"], note, "correct_context", quote, loc, note, [])
        quote = "Medir 1 litro de agua destilada"
        water(
            ["ingredients"],
            "1",
            quote,
            "sol-0 preparation step 2, substep 2.1; sol-0 / recipe-0",
            "Preparation input: measure 1 liter distilled water = 1 L per base recipe batch, not L/L or final-medium makeup. Dissolved ingredients and the unspecified trace-stock dose are not subtracted or used to infer a final volume.",
        )
        note = "The dataset reports 4 g/L phosphate buffer but does not identify its salts or proportions in the inspected table/preparation. No component amounts, molarity or chemical grounding are inferred."
        edit(
            ["ingredients", 3, "notes"],
            note,
            "add_context",
            " ".join(row(main, 5)),
            f"{main} / recipe-5 and preparation step 2.5",
            note,
        )

    groups = {}
    for c in claims:
        groups.setdefault(tuple(c["evidence_pointer"]), []).append(c)
    for pointer, group in groups.items():
        evidence = runner.get_node(after, pointer).setdefault("evidence", [])
        runner.require(
            not any(e["reference"] == reference for e in evidence),
            "Existing evidence needs reconciliation",
        )
        evidence.append(
            {
                "reference": reference,
                "supports": "SUPPORT",
                "snippet": group[0]["snippet"],
                "explanation": " ".join(
                    c["explanation"] + f' Exact excerpt: "{c["snippet"]}"; locator={c["locator"]}.'
                    for c in group
                ),
            }
        )
    runner.require(
        not any(r["reference"] == reference for r in after["references"]),
        "Reference already present",
    )
    after["references"].append(
        {
            "reference": reference,
            "title": source["dataset"]["name"] + " - MediaDive public Medium " + mid,
            "authors": spec["authors"],
            "year": spec["year"],
            "notes": f"source_type=user_contributed_dataset_page; discovery_mode=existing_record_reference; accessed_on={ACCESSED}; publication year is the page year. Page states these user media are not curated or tested and no valid reference is given. No DOI or journal authorship invented; legacy bacmedia URL retained. capture_sha256={source['sha256']}.",
        }
    )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source=reference,
        changes="; ".join(
            f"{c['field']}: {json.dumps(c['old'], sort_keys=True)} -> {json.dumps(c['new'], sort_keys=True)} [{c['status']}]"
            for c in claims
        ),
        notes="Source-backed input and evidence repairs only. Preserved stable ID, chemical mappings, history, physical state, pH, preparation and variants. No inferred final volume, percent basis, stock dilution or growth association.",
    )
    runner.require(not runner.errors(after, "MediaRecipe"), "Proposed schema failure")
    runner.require(
        {c["field"] for c in runner.all_claims(before)} <= {c["field"] for c in claims},
        "Unreviewed concentration claim",
    )
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


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", required=True, type=Path)
    parser.add_argument("--plan", required=True, type=Path)
    parser.add_argument("--reports", type=Path)
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--dry-run", action="store_true")
    modes.add_argument("--apply", action="store_true")
    modes.add_argument("--verify", action="store_true")
    args = parser.parse_args()
    mode = "apply" if args.apply else "verify" if args.verify else "preview"
    plan, result = process(ROOT, args.source_dir, args.plan, mode)
    if args.reports:
        shared.report(args.reports, plan, mode != "preview")
    print(json.dumps(result, indent=2), flush=True)


if __name__ == "__main__":
    main()
