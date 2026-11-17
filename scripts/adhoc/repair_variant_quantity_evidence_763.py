#!/usr/bin/env python3
"""Strengthen already reviewed variant evidence excerpts (#763, 2026-11-16).

Inputs: three pinned #683 proposals and inspected primary-source excerpts/cells.
Outputs: new before/after snapshots and receipt; optional canonical proposal writes.
Only evidence snippets/explanations may change. Scientific payloads, source text,
quantities, stages, membership and dispositions are asserted unchanged.
"""

import argparse
import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PINS = {
    "carini-jensen-pinchuk-tang-683.json": "786ae063209accd3c3ad1e67bd2043e0ff0a4e94703e6b5d8a55b0d073d1b32c",
    "remaining-families-683.json": "bdbfd610071cb3e1983a627ea30e799c2c5a786bddcba52fab2f31958d2d992f",
    "utex-optional-683.json": "d56794675b4a8a3a1bcbceed428f16d734bf624c7331d89e175020c804ec539f",
}


def without_evidence(proposal):
    value = copy.deepcopy(proposal)
    for record in value["records"]:
        for variant in record["variants"]:
            for change in variant["ingredient_changes"]:
                change.pop("evidence")
    return value


def improve(change, snippet, context):
    evidence = change["evidence"][0]
    evidence["snippet"] = snippet
    evidence["explanation"] += (
        " " + context + " Exact excerpt clarification for issue763; scientific payload unchanged."
    )


def root_family(record, change, cells):
    label = change["ingredient"]["preferred_term"]
    mi = change["source_modification_index"]
    name = Path(record["path"]).stem
    if name.startswith("batch_medium"):
        mapping = {
            "glucose monohydrate": "A14",
            "citric acid": "A15",
            "KCl": "A16",
            "(NH4)2HPO4": "A17",
            "CaCl2 dihydrate": "A18",
            "MgSO4 heptahydrate": "A19",
            "biotin stock (0.2 g/L)": "A20",
            "biotin": "A20",
            "trace-salts stock solution": "A21",
            "CuSO4 pentahydrate": "A25",
            "NaI": "A26",
            "MnSO4 monohydrate": "A27",
            "Na2MoO4 dihydrate": "A28",
            "H3BO3": "A29",
            "CoCl2": "A30",
            "ZnCl2": "A31",
            "FeSO4 heptahydrate": "A32",
            "H2SO4 (95–98% w/w)": "A33",
            "HCl": "A22",
            "ammonium hydroxide": "A39",
        }
        if change["action"] == "REMOVE":
            improve(
                change,
                cells["A21"].strip(),
                'Additional file3, A13 header: "'
                + cells["A13"]
                + '". The nine old flattened descriptors are replaced as a group by this stock addition; constituent identities/stock concentrations are separately supported by A24–A33. This is not physical absence from the stock.',
            )
            return
        cell = mapping[label]
        header = (
            "A24"
            if cell in {"A25", "A26", "A27", "A28", "A29", "A30", "A31", "A32", "A33"}
            else "A13"
        )
        context = f'Additional file3 {cell}; separately located {header} header: "{cells[header]}".'
        if cell == "A20":
            context += " Parenthetical 0.2 g L-1 is the biotin stock strength; 1 mL is the stock volume added per liter of chemostat medium."
        if cell == "A39":
            context = 'Additional file3 A39 within the section headed A35 "Chemostat parameters". Percentage basis is not supplied.'
        improve(change, cells[cell].strip(), context)
    elif name == "middlebrook_medium":
        # Exact source-table amounts; whitespace between columns is normalized.
        rows = [
            ("(NH4)2SO4", "0.500 g"),
            ("KH2PO4", "1.500 g"),
            ("Na2HPO4", "1.500 g"),
            ("Na-citrate", "0.400 g"),
            ("MgSO4", "0.025 g"),
            ("CaCl2", "0.500 mg"),
            ("ZnSO4", "1.000 mg"),
            ("CuSO4", "1.000 mg"),
            ("L-Glutamic acid", "0.500 g"),
            ("Ferric ammonium citrate", "0.040 g"),
            ("Pyridoxine", "1.000 mg"),
            ("Biotin", "0.500 mg"),
            ("Malachite green", "0.250 mg"),
            ("Bacto agar", "15.000 g"),
            ("Distilled water", "1000.000 ml"),
        ]
        term, amount = rows[mi]
        improve(
            change,
            term + " " + amount,
            'DSMZ645 p.1 alternative table headed "Bacto Middlebrook 7H10 agar:"; row columns transcribed with whitespace normalized. These are batch input amounts; the water row is an input, not a separately measured final volume.',
        )
    elif name.startswith("for_dsm"):
        if label == "powdered sulfur":
            improve(
                change,
                "add 5.00 g/l of powdered sulfur",
                "DSMZ670 p.1, matching strain-specific prescription. The immediately following steaming instruction concerns sulfur sterilization.",
            )
        elif label == "yeast extract":
            dose = change["ingredient"]["concentration"]["value"]
            improve(
                change,
                dose + " g/l of yeast" if dose == "0.20" else "0.1 g/l yeast extract",
                "DSMZ670 p.1, matching DSM9466/9467 prescription; line wrapping normalized. Yeast extract is a final-medium addition supplied from a sterile stock, whose concentration is not specified.",
            )
        elif label == "D-glucose":
            improve(
                change,
                "add 2.00 g/l D-glucose",
                "DSMZ670 p.1, DSM9467. The subsequent clause specifies filter-sterilized stock solutions.",
            )
        elif label == "H2SO4":
            if "solvent" in change["stage"]:
                improve(
                    change,
                    "prepared with 0.2 N H2SO4",
                    "DSMZ670 p.1 preparation step1, ferrous-sulfate stock solvent; normality is retained without conversion.",
                )
            else:
                ph, strength = {
                    "for_dsm_9463": ("3.5", "1"),
                    "for_dsm_9466": ("3.0", "1"),
                    "for_dsm_9467": ("3.0", "1"),
                    "for_dsm_9468": ("1.6", "4"),
                }[name]
                improve(
                    change,
                    f"Adjust pH to {ph} with {strength} N H2SO4 prior to autoclaving",
                    "DSMZ670 p.1, matching strain prescription. Titrant strength and target pH do not supply a fixed acid dose.",
                )
        elif change["action"] == "REMOVE":
            improve(
                change,
                "omit FeSO4 x 7 H2O from the medium",
                "DSMZ670 p.1, matching DSM9463/9466/9467 prescription; line wrapping normalized.",
            )
        else:
            improve(
                change,
                "40% (w/v) stock solution",
                'DSMZ670 p.1 step1; separate exact solvent excerpt: "prepared with 0.2 N H2SO4". Table stock-volume column states "50.00 ml"; the batch water input is 950.00 ml. No further final-volume normalization is asserted.',
            )
    elif name.startswith(("mm_biotin", "mmp_biotin")):
        quotes = {
            "biotin": "10 μg ml-1 biotin",
            "thiamine": "10 μg ml-1 thiamine",
            "CaCl2 dihydrate": "1.49 mM CaCl2 2H2O (autoclaved separately)",
            "FeCl3 hexahydrate": "0.0184 mM FeCl3 6H2O (filter sterilized)",
            "calcium pantothenate": "MMP contains the same components plus 1 μM calcium pantothenate",
        }
        improve(
            change,
            quotes[label],
            'Villasenor Methods, Bacterial strains/media/growth conditions. Separate basis statement: "After sterilization the following components were added to the final concentration indicated". MM lacks the separate MMP addition; no physical removal or doubled calcium-salt dose is implied.',
        )
    elif name.startswith("ms10"):
        if label == "MnSO4":
            improve(
                change,
                "MnSO4 (1.25 × 10−5 g · liter−1)",
                "Nordkvist original ASM Methods, Strain and growth conditions; subscripts/superscripts rendered in plain text. Hydration not specified. This supplement applies to the defined MS10 culture medium.",
            )
        elif change["action"] == "REMOVE":
            improve(
                change,
                "without dl-6,8-thioctic acid",
                "Nordkvist Figure1C caption and Table2 heading; source explicitly excludes this component from the modified treatment.",
            )
        elif change["action"] == "ADD":
            improve(
                change,
                "0.3 g of sodium acetate liter−1 was added after 7 h 38 min",
                "Nordkvist Figure1B caption. This is a timed addition during cultivation, not an initial concentration; superscript exponent rendered in plain text.",
            )
        else:
            improve(
                change,
                "with 0.82 g of sodium acetate liter−1",
                "Nordkvist Figure1C caption; separate treatment without dl-6,8-thioctic acid, not the timed Figure1B addition.",
            )
    else:
        raise ValueError("unreviewed root-family record")


def four_families(change):
    ref = change["evidence"][0]["reference"]
    if ref == "doi:10.1002/btpr.227" and change["action"] == "REPLACE":
        improve(
            change,
            "minimal medium (30mM, pH=7, buffered with 20mM PIPES)",
            'Tang OSTI-hosted manuscript, p.4 Methods. Separate exact substrate excerpt: "[3-13C] sodium L-lactate". The immediately preceding substrate name binds this 30mM dose to labeled lactate; isotope-position typography rendered as plain text.',
        )
    elif ref == "doi:10.1128/aem.59.12.4363-4366.1993":
        improve(
            change,
            "calcium pantothenate",
            'Jensen p.4363 Table1 footnote b gives the separate amount excerpt "2 μM pantothenate" (micro-unit typography normalized from PDF extraction). This is the pantothenate basis, not 2 μM calcium salt; no calcium dose or salt-molarity conversion is inferred. The formulation paragraph supplies the calcium-salt identity.',
        )


def utex(change):
    label = change["ingredient"]["preferred_term"]
    evidence = change["evidence"][0]
    url = evidence["reference"]
    if "j-medium" in url:
        improve(
            change,
            "For 1.25% agar medium add 12.5 g of agar",
            'Directions step2; separate preceding instruction: "Bring total volume to 1 L with dH2O". Source designates the optional agar percentage and pairs a mass with this volume; no post-addition volume measurement is claimed. Water subscript rendered as plain text.',
        )
    elif "soil-plus-seawater" in url:
        improve(
            change,
            evidence["snippet"],
            'Separate Directions header: "For 200 mL Total"; table identifies optional CaCO3. The quoted 1 mg is a batch input; the source table molarity is not adopted.',
        )
    elif label == "agar" and "bg-11" in url:
        improve(
            change,
            "add 15 g of agar to 500 mL of dH2O",
            "Agar-media step3, separately autoclaved agar portion; water subscript rendered as plain text. Combining portions occurs in step7, not in this quoted stock-preparation step.",
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-directory", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    directory = args.output_directory.resolve()
    directory.mkdir(parents=True, exist_ok=False)
    cells_file = ROOT / ".temp/variant-683/sources/mattanovich-2009/s3-cells.json"
    if (
        hashlib.sha256(cells_file.read_bytes()).hexdigest()
        != "59c545161499cb11bfc37cd3a62ee163ef8dc2737330d6bbce7597681cc96971"
    ):
        raise ValueError("reviewed Mattanovich cell extraction changed")
    workbook = cells_file.parent / "verified-s3.xls"
    if (
        hashlib.sha256(workbook.read_bytes()).hexdigest()
        != "5a9895037d69eec142443c94b3a81ed40ff75e09a51c5c6f404c7c8e14b90bc8"
    ):
        raise ValueError("reviewed Mattanovich workbook changed")
    cells = json.loads(cells_file.read_text())["sheets"][0]["cells"]
    results, writes = [], []
    for name, expected in PINS.items():
        path = ROOT / "conf/variant_ingredient_curation" / name
        raw = path.read_bytes()
        if hashlib.sha256(raw).hexdigest() != expected:
            raise ValueError("proposal drift: " + name)
        original = json.loads(raw)
        corrected = copy.deepcopy(original)
        changed = 0
        for record in corrected["records"]:
            for variant in record["variants"]:
                for change in variant["ingredient_changes"]:
                    before = copy.deepcopy(change["evidence"])
                    if name.startswith("remaining"):
                        root_family(record, change, cells)
                    elif name.startswith("carini"):
                        four_families(change)
                    else:
                        utex(change)
                    changed += change["evidence"] != before
        if without_evidence(original) != without_evidence(corrected):
            raise ValueError("non-evidence payload changed")
        after = (json.dumps(corrected, indent=2, ensure_ascii=False) + "\n").encode()
        (directory / (name + ".before")).write_bytes(raw)
        (directory / (name + ".after")).write_bytes(after)
        results.append(
            {
                "path": str(path.relative_to(ROOT)),
                "before_sha256": expected,
                "after_sha256": hashlib.sha256(after).hexdigest(),
                "events_with_evidence_changed": changed,
                "non_evidence_payload_equal": True,
            }
        )
        writes.append((path, after))
    if args.apply:
        for path, after in writes:
            path.write_bytes(after)
    receipt = {
        "issue": 763,
        "mode": "apply" if args.apply else "preview",
        "records": results,
        "source_cells_sha256": hashlib.sha256(cells_file.read_bytes()).hexdigest(),
    }
    (directory / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
    print(json.dumps(receipt, indent=2))


if __name__ == "__main__":
    main()
