#!/usr/bin/env python3
"""Restore P4/P5 source stock boundaries, carriers and evidence without invented makeup doses."""

from __future__ import annotations

import argparse
import copy
import json
import re
from decimal import Decimal
from pathlib import Path

import review_public_stock_concentrations as shared
from review_public_direct_concentrations import HTMLTree, content, nodes, one

from culturemech.curate.curation_event import record_curation_event

runner = shared.runner
ROOT = Path(__file__).resolve().parents[1]
ACTION = "RESTORED_RS_STOCK_BOUNDARIES_CARRIERS_AND_SOURCE_CONFLICTS"
BASE = "https://mediadive.dsmz.de/medium/"
SNAPSHOT = (
    ROOT / "reports/ingredient_concentration_curation/20261007-public-medium-source-pages.json"
)
SNAPSHOT_SHA = "9b1238f4c428109f538a733605e34f22b9b3e577f065cac40f6f417f54605078"
ACCESSED = "2026-10-07"
NNM_NAME = "RS Medium - Non-Nutrient Medium (NNM) Component"
NNM_TERM = {"id": "CultureMech:010434", "label": NNM_NAME}
TARGETS = {
    "P4": {
        "path": "data/normalized_yaml/bacterial/rs_medium_non_nutrient_medium_nnm_component.yaml",
        "id": "CultureMech:010434",
        "name": "rs_medium_non_nutrient_medium_nnm_component",
        "before_sha256": "3cba8b91496a5b9ec18e2c6951a3e5a8529f93d6b9cbad09ee659b9c31353cc5",
        "semantic_sha256": "d886ad011dae18930842b59473c42db528c61e69a184c8c9880a32fc113ff1d1",
        "source_sha256": "c1b66217611ac37036f1550d0c3ade9bb6b4a9ef733f0547494547e574668a4b",
        "figure_sha256": "245e477ae6e3c0f514270e7e62fc4c000110c022ae18c153c7ec8ceb9f03e4a2",
        "volume": "1000",
    },
    "P5": {
        "path": "data/normalized_yaml/bacterial/rs_medium_nutrient_medium_nm_component.yaml",
        "id": "CultureMech:010435",
        "name": "rs_medium_nutrient_medium_nm_component",
        "before_sha256": "93211711e4f2891a3e86ff81e27515803735f1c90135826a1cca0743deae67b1",
        "semantic_sha256": "21988e1cebea21bfdd3fbd156cf0949260b6f7e7471766af88c752bc922e05f5",
        "source_sha256": "fe4448ec7332d8e7ec8313b49ffa8e03b0c26ca54522d83fa802a19bbb25f5c7",
        "figure_sha256": "e90144dbb695abd6ac4279e294fe7b6b8a1b3d28dce4a26346fd14d78aa28917",
        "volume": "150",
    },
}
P4_ROWS = [
    0,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
    15,
    16,
    18,
    19,
    20,
    21,
    22,
    23,
    24,
    25,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
]
P5_ROWS = {
    0: [0, 1, 2],
    1: [3, 4, 5, 6],
    2: list(range(7, 17)),
    4: [51, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36],
}
MEM = [
    [
        "6.32",
        "1.56",
        "2.10",
        "2.63",
        "2.62",
        "3.63",
        "0.76",
        "1.65",
        "2.38",
        "0.51",
        "1.80",
        "2.34",
    ],
    ["0.89", "0.75", "1.15", "1.50", "1.33", "1.47", "1.05"],
]


def num(value):
    return format(Decimal(value).normalize(), "f")


def sources(folder, mid):
    spec = TARGETS[mid]
    raw_snapshot = SNAPSHOT.read_bytes()
    runner.require(runner.sha(raw_snapshot) == SNAPSHOT_SHA, "Source inventory drift")
    snapshot = one([r for r in json.loads(raw_snapshot)["records"] if r["medium_id"] == mid])
    raw = (folder / f"{mid}-medium-page.html").read_bytes()
    runner.require(runner.sha(raw) == spec["source_sha256"], "Source page hash drift")
    figure = (folder / f"{mid}-preparation-figure.png").read_bytes()
    runner.require(runner.sha(figure) == spec["figure_sha256"], "Preparation figure drift")
    tree = HTMLTree(raw.decode()).root
    dataset = one(
        [
            json.loads(content(n))
            for n in nodes(tree, "script", type="application/ld+json")
            if json.loads(content(n)).get("@type") == "Dataset"
        ]
    )
    runner.require(dataset == snapshot["dataset"], "Dataset identity drift")
    sections = [n for n in nodes(tree, "div") if "solution" in n["attrs"].get("class", "").split()]
    section = one(sections)
    runner.require(section["attrs"]["id"] == "sol-0", "Unexpected source topology")
    table = one(
        [
            t
            for t in nodes(section, "table")
            if "solution-table" in t["attrs"].get("class", "").split()
        ]
    )
    parsed = [
        (
            [
                content(c)
                for c in tr["children"]
                if isinstance(c, dict) and c["tag"] in {"td", "th"}
            ],
            tr["attrs"],
        )
        for tr in nodes(table, "tr")
    ]
    expected = one(snapshot["recipe_tables"])
    runner.require(
        parsed == [(r["cells"], r["attributes"]) for r in expected["rows"]],
        "Recipe table/preparation drift",
    )
    runner.require(parsed[0][0] == shared.HEADER, "Source columns changed")
    controls = nodes(section, "input", id="main-sol-vol")
    runner.require(
        [n["attrs"] for n in controls] == expected["main_volume_controls"],
        "Source volume control drift",
    )
    runner.require(one(controls)["attrs"]["value"] == spec["volume"], "Wrong source scale")
    runner.require(
        [content(n) for n in nodes(section, "span", **{"class": "input-group-text"})] == ["ml"],
        "Volume unit changed",
    )
    metadata = [[content(c) for c in nodes(tr, "td")] for tr in nodes(tree, "tr")]
    runner.require(
        all(r["cells"] in metadata for r in snapshot["metadata_rows"]), "Source metadata drift"
    )
    paragraphs = " ".join(content(p) for p in nodes(tree, "p"))
    runner.require(
        "we do not curate or test the media" in paragraphs
        and "no valid reference is given" in paragraphs,
        "Dataset qualification changed",
    )
    rows = {
        int(attrs["id"].removeprefix("recipe-")): cells for cells, attrs in parsed if "id" in attrs
    }
    steps = {
        int(cells[0].split()[0]): cells[0]
        for cells, attrs in parsed
        if attrs.get("class") == "step-row"
    }
    return {
        "rows": rows,
        "steps": steps,
        "dataset": dataset,
        "text": [" ".join(cells) for cells, _ in parsed],
        "sha256": runner.sha(raw),
        "figure_sha256": runner.sha(figure),
    }


def build(before, source, mid, timestamp):
    spec = TARGETS[mid]
    runner.require(
        shared.semantic_sha(before) == spec["semantic_sha256"], "Unreviewed formulation drift"
    )
    runner.require(
        before["id"] == spec["id"]
        and before["media_term"]["term"]["id"] == "mediadive.medium:" + mid,
        "Wrong record identity",
    )
    runner.require(not runner.errors(before, "MediaRecipe"), "Baseline schema failure")
    after, claims = copy.deepcopy(before), []
    reference = BASE + mid
    rows, steps = source["rows"], source["steps"]

    def excerpt(text, locator):
        runner.require(any(text in block for block in source["text"]), "Unverified source excerpt")
        return {"snippet": text, "locator": locator}

    def row_quote(rid):
        return excerpt(" ".join(rows[rid]), f"sol-0 / recipe-{rid}; table headings={shared.HEADER}")

    def step_quote(step, text):
        runner.require(text in steps[step], "Wrong preparation-stage excerpt")
        return excerpt(text, f"sol-0 preparation step {step}")

    def claim(old_pointer, pointer, status, quotes, why, evidence_pointer=None):
        old = (
            None
            if old_pointer is None
            else runner.get_node(before, old_pointer[:-1]).get(old_pointer[-1])
        )
        node = runner.get_node(after, pointer[:-1])
        new = node.get(pointer[-1])
        old_field = None if old_pointer is None else runner.field_name(old_pointer)
        claims.append(
            {
                "old_pointer": old_pointer,
                "old_field": old_field,
                "pointer": pointer,
                "field": runner.field_name(pointer),
                "ingredient": node.get("preferred_term", before["original_name"]),
                "old": copy.deepcopy(old),
                "new": copy.deepcopy(new),
                "status": status,
                "reference": reference,
                **quotes[0],
                "extra_excerpts": quotes[1:],
                "explanation": f"{old_field or 'new input'} -> {runner.field_name(pointer)}: {why}",
                "evidence_pointer": pointer[:-1] if evidence_pointer is None else evidence_pointer,
                "supports": "SUPPORT",
            }
        )

    def solvent(pointer, nnm, quotes, note, purified=True):
        node = {
            "preferred_term": NNM_NAME if nnm else "Purified water" if purified else "Water",
            "source": "MediaDive public Medium " + mid,
            "notes": note,
        }
        if nnm:
            node["culturemech_term"] = copy.deepcopy(NNM_TERM)
        runner.get_node(after, pointer[:-1]).append(node)
        claim(None, pointer + ["concentration"], "not_quantified", quotes, note)

    if mid == "P4":
        after["ingredients"], after["solutions"] = [], []
        fill = step_quote(4, "Fill to a total volume of 1 liter with purified H2O.")
        prep = step_quote(2, "prepare stock solutions in H2O at the specified concentration")
        for index, rid in enumerate(P4_ROWS):
            original = before["ingredients"][index]
            cells = rows[rid]
            runner.require(
                cells[0].split(" (Stock solution")[0] == original["preferred_term"],
                "P4 chemical identity mismatch",
            )
            node = copy.deepcopy(original)
            oldp = ["ingredients", index, "concentration"]
            if cells[2] == "g/l":
                runner.require(
                    original["concentration"]["unit"] == "G_PER_L"
                    and Decimal(original["concentration"]["value"]) == Decimal(cells[1]),
                    "P4 direct amount mismatch",
                )
                pointer = ["ingredients", len(after["ingredients"])]
                after["ingredients"].append(node)
                claim(
                    oldp,
                    pointer + ["concentration"],
                    "evidence_only",
                    [row_quote(rid), fill],
                    "Source-explicit direct g/L rate with a separate 1 L final-makeup instruction; unchanged.",
                )
                continue
            runner.require(cells[2] in {"ml/l", "ul/l", "\u03bcl/l"}, "Unsupported P4 dose unit")
            dose = Decimal(cells[1]) / (1 if cells[2] == "ml/l" else 1000)
            strength = re.search(r"Stock solution ([0-9.]+)(mg|g)/(\d+)?ml", cells[0], re.I)
            if rid == 32:
                runner.require(
                    strength is None
                    and "10-15% TiCl3 basis" in cells[0]
                    and "1:1000000" in cells[0],
                    "TiCl3 dilution context changed",
                )
                runner.require(
                    original["concentration"] == {"value": "0.0013", "unit": "ML_PER_L"},
                    "TiCl3 legacy dose drift",
                )
                node.pop("concentration")
                why = "The legacy ingredient quantity was the diluted reagent's working dose, not TiCl3 solute concentration. Move it to the stock. Preserve 10-15% commercial strength and 1:1000000 dilution only as literal source context; no percent basis, density or TiCl3 mass amount is inferred."
            else:
                runner.require(strength is not None, "Unparsed stock strength")
                mass, unit, volume = strength.groups()
                stock_g_l = (
                    Decimal(mass)
                    * (1 if unit.lower() == "g" else Decimal("0.001"))
                    / (Decimal(volume or 1) / 1000)
                )
                legacy_g_l = (
                    Decimal(original["concentration"]["value"])
                    * {
                        "G_PER_L": Decimal(1),
                        "MG_PER_L": Decimal("0.001"),
                        "MICROG_PER_L": Decimal("0.000001"),
                    }[original["concentration"]["unit"]]
                )
                runner.require(
                    legacy_g_l == stock_g_l * dose / 1000,
                    "Prior P4 final concentration arithmetic conflict",
                )
                node["concentration"] = {"value": num(stock_g_l), "unit": "G_PER_L"}
                why = f"Restore the stock stage: {mass} {unit} / {volume or 1} ml = {num(stock_g_l)} g/L stock. Source addition {cells[1]} {cells[2]} = {num(dose)} ml/L. The previous final contribution {num(legacy_g_l)} g/L matches {num(stock_g_l)} * {num(dose)} / 1000; it was not a wrong numeric value but must not remain a duplicate direct ingredient."
            node["notes"] = why
            si = len(after["solutions"])
            stock = {
                "preferred_term": node["preferred_term"] + " stock",
                "concentration": {"value": num(dose), "unit": "ML_PER_L"},
                "notes": cells[0]
                + ". Prepared in H2O under source preparation step 2; dose applies to the 1 L NNM batch, not to preparation of this stock.",
                "composition": [node],
            }
            after["solutions"].append(stock)
            claim(
                oldp,
                ["solutions", si, "composition", 0, "concentration"],
                "relocate_stock",
                [row_quote(rid), prep, fill],
                why,
            )
            claim(
                oldp if rid == 32 else None,
                ["solutions", si, "concentration"],
                "add" if rid != 32 else "relocate_dose",
                [row_quote(rid), fill],
                f"Working stock addition: {cells[1]} {cells[2]} / {1 if cells[2] == 'ml/l' else 1000} = {num(dose)} ML_PER_L. No reagent density or solute percentage is inferred.",
                [],
            )
            solvent(
                ["solutions", si, "composition", 1],
                False,
                [prep, row_quote(rid)],
                "H2O is the source-named stock solvent. No solvent volume is given; do not equate stock volume with water input.",
                purified=False,
            )
        solvent(
            ["ingredients", len(after["ingredients"])],
            False,
            [fill],
            "Make up the combined NNM ingredients and stocks to a final 1 L with purified H2O. The amount of added water is not specified; no 1 L water dose is asserted.",
        )
        after["notes"] = (
            "RS NNM retains nine direct solute rates and now represents the 23 source-listed stocks separately. Final makeup is 1 L with purified water; stock water amounts are unspecified. Prior calculated final contributions are preserved in the claim audit, not duplicated as direct ingredients. TiCl3 commercial percentage basis and solute concentration remain unresolved."
        )
        claim(["notes"], ["notes"], "correct_context", [fill, prep], after["notes"], [])
    else:
        mix_doses = ["0.004", "0.030", "0.0107", "0.0109", "0.0107"]
        final_quote = step_quote(
            10,
            "Combine 4 ml of Mix solution 1 (Si and Fe+EDTA), 30 ml from Mix solution 2 (NO3-PO4), 10.7 ml from Mix solution 3 (Vitamins), 10.9 ml of Mix solution 4 (Amino Acids) and 10.7 ml of Mix solution 5 (Carbon sources).",
        )
        final_fill = step_quote(10, "Fill to 150 ml with NNM.")
        stock_phase = step_quote(
            2,
            "Single stocks are prepared either in purified H2O or in the Non-Nutrient Medium (NNM) component of RS Medium",
        )
        for mi in range(5):
            original_mix = before["solutions"][mi]
            mix = after["solutions"][mi]
            mix["composition"], mix["solutions"] = [], []
            mix["concentration"] = {"value": mix_doses[mi], "unit": "L"}
            mix["notes"] = (
                f"Prepare 50 ml of Mix solution {mi + 1} from the individually represented source stocks, then fill to volume with NNM; the makeup-fluid amount is not specified. Final NM assembly uses {num(Decimal(mix_doses[mi]) * 1000)} ml of this mix per 150 ml batch. Nested stock concentrations are stock stages, not duplicated direct contributions."
            )
            step = mi + 5
            fill = step_quote(step, "Fill to 50 ml with NNM.")
            if mi < 3:
                dose_quote = step_quote(
                    step,
                    (
                        "add 4.5 \u00b5l each from the single stocks of vitamins"
                        if mi == 2
                        else "add 2.27 ml each from the single stocks"
                    ),
                )
            elif mi == 3:
                dose_quote = step_quote(step, "Add 2.27 ml of the single stock of Glutamine.")
            else:
                dose_quote = step_quote(step, "Add 2.27 ml of each carbon source")
            claim(
                ["solutions", mi, "concentration"],
                ["solutions", mi, "concentration"],
                "correct",
                [final_quote, final_fill, fill],
                "Use the exact source batch volume in L, not a rounded ML_PER_L dose. Each mix has its own 50 ml preparation; no makeup-fluid subtraction is performed.",
                [],
            )

            def single(
                ci,
                rid,
                *,
                original_mix=original_mix,
                mix=mix,
                mi=mi,
                dose_quote=dose_quote,
                fill=fill,
            ):
                old = original_mix["composition"][ci]
                cells = rows[rid]
                label = old["preferred_term"]
                runner.require(
                    cells[0].startswith(label + " ("), "Single-stock chemical form mismatch"
                )
                runner.require(cells[2] in {"g/50ml", "g/ml"}, "Unreviewed single-stock unit")
                concentration = Decimal(cells[1]) / (
                    Decimal("0.05") if cells[2] == "g/50ml" else Decimal("0.001")
                )
                dose_l = Decimal("0.0000045") if mi == 2 else Decimal("0.00227")
                runner.require(
                    Decimal(old["concentration"]["value"])
                    == concentration * dose_l / Decimal("0.05")
                    and old["concentration"]["unit"] == "G_PER_L",
                    "Legacy mix-contribution mismatch",
                )
                node = copy.deepcopy(old)
                node["concentration"] = {"value": num(concentration), "unit": "G_PER_L"}
                why = f"Move {label} from a flattened mix contribution into its single stock. Source {cells[1]} {cells[2]} = {num(concentration)} g/L stock. {num(dose_l)} L stock / 0.05 L mix explains the former {old['concentration']['value']} g/L direct contribution. NNM carrier constituents, where present, are separate and not included in this solute-only rate."
                node["notes"] = why
                stock_index = len(mix["solutions"])
                pointer = ["solutions", mi, "solutions", stock_index]
                nested = {
                    "preferred_term": label + " single stock",
                    "concentration": {"value": num(dose_l), "unit": "L"},
                    "notes": cells[0] + f"; add {num(dose_l)} L per 50 ml mix batch, not L/L.",
                    "composition": [node],
                }
                mix["solutions"].append(nested)
                quotes = [row_quote(rid), dose_quote, fill]
                claim(
                    ["solutions", mi, "composition", ci, "concentration"],
                    pointer + ["composition", 0, "concentration"],
                    "relocate_stock",
                    quotes,
                    why,
                )
                claim(
                    None,
                    pointer + ["concentration"],
                    "add",
                    [dose_quote, row_quote(rid), fill],
                    nested["notes"],
                    [],
                )
                if "Single stock in NNM." in cells[0]:
                    nnm, solvent_quotes = True, [row_quote(rid), stock_phase]
                elif "Single stock in H2O." in cells[0]:
                    nnm, solvent_quotes = False, [row_quote(rid), stock_phase]
                elif rid in {33, 34}:
                    nnm = False
                    solvent_quotes = [
                        row_quote(rid),
                        step_quote(3 if rid == 33 else 4, "prepare the single stock in H2O."),
                        stock_phase,
                    ]
                else:
                    raise ValueError("Unreviewed stock solvent")
                solvent(
                    pointer + ["composition", 1],
                    nnm,
                    solvent_quotes,
                    "Source-named single-stock solvent/carrier. Its added volume is unspecified; do not subtract solute masses from a stock volume or assume the entire dose is pure solvent. NNM composition is linked to P4, not copied or omitted.",
                )

            for ci, original in enumerate(original_mix["composition"]):
                if original.get("culturemech_term") == NNM_TERM:
                    node = copy.deepcopy(original)
                    node.pop("concentration")
                    node["notes"] = (
                        "Fill this mix to 50 ml with NNM. The source specifies a final volume, not a fixed NNM amount; the former volume-subtraction rate is withdrawn. Additional NNM may enter through individual stocks and is represented there separately."
                    )
                    pointer = ["solutions", mi, "composition", len(mix["composition"])]
                    mix["composition"].append(node)
                    claim(
                        ["solutions", mi, "composition", ci, "concentration"],
                        pointer + ["concentration"],
                        "correct",
                        [fill],
                        node["notes"],
                    )
                elif mi == 3:
                    if ci == 19:
                        single(ci, 38)
                    elif ci in {0, 12}:
                        group = 0 if ci == 0 else 1
                        start, stop = (0, 12) if group == 0 else (12, 19)
                        dose_l = Decimal("0.00225") if group == 0 else Decimal("0.00227")
                        rid = 49 + group
                        runner.require(
                            rows[rid][2] == "ml" and Decimal(rows[rid][1]) / 1000 == dose_l,
                            "MEM working dose mismatch",
                        )
                        pointer = ["solutions", mi, "solutions", len(mix["solutions"])]
                        nested = {
                            "preferred_term": f"MEM {50 if group == 0 else 100}X Amino Acids solution (Sigma)",
                            "concentration": {"value": num(dose_l), "unit": "L"},
                            "notes": f"Source-described MEM formulation, not a current supplier specification. Add {num(dose_l)} L per 50 ml mix batch, not L/L. The source does not specify a solvent composition for this commercial stock; none is invented.",
                            "composition": [],
                        }
                        mix["solutions"].append(nested)
                        for offset, oi in enumerate(range(start, stop)):
                            old = original_mix["composition"][oi]
                            rate = MEM[group][offset]
                            q = step_quote(8, f"{old['preferred_term']} ({rate} g/L)")
                            runner.require(
                                Decimal(old["concentration"]["value"])
                                == Decimal(rate) * dose_l / Decimal("0.05"),
                                "MEM legacy dilution conflict",
                            )
                            node = copy.deepcopy(old)
                            node["concentration"] = {"value": rate, "unit": "G_PER_L"}
                            node["notes"] = (
                                "Stock concentration reported in the P5 MEM composition, not the diluted mix concentration and not inferred from the 50X/100X label."
                            )
                            nested["composition"].append(node)
                            claim(
                                ["solutions", mi, "composition", oi, "concentration"],
                                pointer + ["composition", offset, "concentration"],
                                "relocate_stock",
                                [q, row_quote(rid), fill],
                                f"Preserve the source MEM stage at {rate} g/L. Prior mix contribution {old['concentration']['value']} g/L = {rate} * {num(dose_l)} / 0.05; remove that duplicate direct contribution.",
                            )
                        claim(
                            None,
                            pointer + ["concentration"],
                            "add",
                            [row_quote(rid), fill],
                            nested["notes"],
                            [],
                        )
                elif mi == 4 and ci == 0:
                    pointer = ["solutions", mi, "composition", len(mix["composition"])]
                    node = copy.deepcopy(original)
                    mix["composition"].append(node)
                    quote = step_quote(9, "add 45 \u00b5l of Glycerol from Sigma (1.26 g/mL).")
                    runner.require(
                        Decimal(original["concentration"]["value"])
                        == Decimal("45") / 1000 * Decimal("1.26") / Decimal("0.05"),
                        "Glycerol arithmetic mismatch",
                    )
                    claim(
                        ["solutions", mi, "composition", ci, "concentration"],
                        pointer + ["concentration"],
                        "evidence_only",
                        [row_quote(51), quote, fill],
                        "The source itself supplies 1.26 g/ml: 45 ul / 1000 * 1.26 g/ml / 0.05 L = 1.134 g/L in Mix 5, unchanged. No external density estimate is used.",
                    )
                elif mi == 4 and ci in {12, 14}:
                    rid, other = (29, "L-mannose") if ci == 12 else (31, "Xylan")
                    pointer = ["solutions", mi, "composition", len(mix["composition"])]
                    node = copy.deepcopy(original)
                    node.pop("concentration")
                    node["notes"] = (
                        f"Source identity conflict: the single-stock table names {original['preferred_term']}, but Mix 5 preparation names {other}. The prior calculated mix concentration is withdrawn; no amount or alternative identity is selected. Existing chemical annotation identifies the table label only, not confirmed presence of that reagent in the prepared mix."
                    )
                    node["data_quality_flags"] = ["source_identity_conflict"]
                    mix["composition"].append(node)
                    claim(
                        ["solutions", mi, "composition", ci, "concentration"],
                        pointer + ["concentration"],
                        "correct",
                        [row_quote(rid), step_quote(9, other)],
                        node["notes"],
                    )
                else:
                    single(ci, P5_ROWS[mi][ci])
        makeup = after["solutions"][5]
        makeup.pop("concentration")
        makeup["notes"] = (
            "Fill the combined five mixes to a final 150 ml with NNM. The makeup amount is unspecified; the former 558 ml/L subtraction-derived dose is withdrawn. NNM also enters through individual stocks and mix makeup, without an invented total NNM fraction."
        )
        claim(
            ["solutions", 5, "concentration"],
            ["solutions", 5, "concentration"],
            "correct",
            [final_quote, final_fill],
            makeup["notes"],
            [],
        )
        after["notes"] = (
            "RS NM preserves five 50 ml mix stages and the final 150 ml assembly. Individual source stocks, their NNM or water carriers, and exact batch additions are now explicit. Makeup-fluid quantities are unquantified rather than inferred by volume subtraction. Mix 5 has unresolved D-Mannose/L-mannose and D-Xylose/Xylan conflicts; neither alternative nor its dose is selected. No complete final-medium composition is claimed while these conflicts remain."
        )
        claim(
            ["notes"],
            ["notes"],
            "correct_context",
            [stock_phase, final_fill, step_quote(9, "L-mannose"), step_quote(9, "Xylan")],
            after["notes"],
            [],
        )

    groups = {}
    for c in claims:
        groups.setdefault(tuple(c["evidence_pointer"]), []).append(c)
    context = f"User-contributed MediaDive {mid} page, accessed {ACCESSED}; source_type=user_contributed_dataset_page; page_sha256={source['sha256']}; figure_sha256={source['figure_sha256']}. Numeric evidence is the page text, not OCR of the inspected diagram. No journal validation or growth claim is implied."
    for pointer, group in groups.items():
        evidence = runner.get_node(after, pointer).setdefault("evidence", [])
        runner.require(
            not any(e["reference"] == reference for e in evidence),
            "Existing evidence needs reconciliation",
        )
        explanation = []
        for c in group:
            explanation.append(c["explanation"])
            for q in [c, *c["extra_excerpts"]]:
                explanation.append(f'Exact excerpt: "{q["snippet"]}"; locator={q["locator"]}.')
        evidence.append(
            {
                "reference": reference,
                "supports": "SUPPORT",
                "snippet": group[0]["snippet"],
                "explanation": " ".join(explanation) + " " + context,
            }
        )
    after["references"].append(
        {
            "reference": reference,
            "title": source["dataset"]["name"] + " - MediaDive public Medium " + mid,
            "authors": "Cristiana Sigona, Daniel J. Richter",
            "year": 2023,
            "notes": f"source_type=user_contributed_dataset_page; discovery_mode=existing_record_reference; accessed_on={ACCESSED}; page published=2023-06-30, modified={'2025-07-10' if mid == 'P4' else '2025-10-07'}. The page states user media are not curated/tested and no valid reference is given. Legacy bacmedia URL retained; no DOI invented. {context}",
        }
    )
    record_curation_event(
        after,
        curator="codex",
        action=ACTION,
        timestamp=timestamp,
        source=reference,
        changes="; ".join(
            f"{c['old_field'] or 'new input'} -> {c['field']}: {json.dumps(c['old'], sort_keys=True)} -> {json.dumps(c['new'], sort_keys=True)} [{c['status']}]"
            for c in claims
        ),
        notes="Restored source preparation stages without double-counting final and stock solutes. Preserved permanent ID, names, prior history, mappings, physical state, pH, salinity, preparation and variants. Unknown makeup amounts and source identity conflicts remain explicit.",
    )
    runner.require(not runner.errors(after, "MediaRecipe"), "Proposed schema failure")
    runner.require(
        {c["field"] for c in runner.all_claims(before)} <= {c["old_field"] for c in claims},
        "Unreviewed baseline claim",
    )
    runner.require(
        {c["field"] for c in runner.all_claims(after)} <= {c["field"] for c in claims},
        "Unreviewed result claim",
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


def report(folder, plan, applied):
    for item in plan["records"]:
        lines = [
            f"# RS Stock Boundary Review: {item['name']}",
            "",
            f"- Record: {item['path']}",
            f"- ID: {item['id']}",
            f"- Reviewed commit: `{plan['commit']}`",
            f"- State: {'applied locally' if applied else 'preview'}",
            f"- Before SHA256: `{item['before_sha256']}`",
            f"- Result SHA256: `{item['after_sha256']}`",
            f"- Source page SHA256: `{item['source_sha256']}`",
            "",
            "All original and resulting concentration claims are accounted below. "
            "Relocation rebases a concentration to its source stock stage; it is not "
            "a claim that the former calculated contribution was numerically wrong. "
            "Unknown makeup amounts, TiCl3 strength basis, and P5 identity conflicts "
            "are not resolved by schema validity. Source pages are user-contributed, "
            "not journal validation. See ../README.md and ../validation.json for "
            "scope, independent audit and terminal validation. No growth claims added.",
            "",
            "| Old field | Result field | Ingredient | Old | New | Status | DOI/PURL | "
            "Exact excerpts with separate locators | Decision | Action |",
            "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |",
        ]
        for c in item["claims"]:
            excerpts = " ; ".join(
                f'"{q["snippet"]}" [locator: {q["locator"]}]' for q in [c, *c["extra_excerpts"]]
            )
            values = [
                c["old_field"] or "new input",
                c["field"],
                c["ingredient"],
                c["old"],
                c["new"],
                c["status"],
                c["reference"],
                excerpts,
                c["explanation"],
                "applied" if applied else "preview",
            ]
            lines.append("| " + " | ".join(runner.cell(v) for v in values) + " |")
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
