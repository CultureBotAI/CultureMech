#!/usr/bin/env python3
"""Prepare explicit decisions for five source families (#683; 2026-11-16).

Inputs: pinned prose inventory and independently inspected primary sources.
Output: guarded proposal and complete 55-row disposition ledger; no recipe writes.
DSMZ645/670 PDFs, Villasenor XML and Mattanovich XLS were captured in .temp;
Nordkvist Methods/Fig1 were read at the public PMC article (XML endpoint failed).
"""

import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
QUEUE_SHA = "dd5faea741da0a11e8eb86cad2976e8bf51d42884c601e96973eba61748330ca"
SOURCES = {
    "middlebrook": (
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium645.pdf",
        "e97e19295e3f61a6bcfaae355a2df1e9a4eb444f4b68177ad3b48b351d92932a",
    ),
    "dsm670": (
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium670.pdf",
        "e21dbc3f7c16cf301001aaa5ca4ca7aa57fb486cbccba0995c46e094946917ab",
    ),
    "villasenor": (
        "doi:10.1186/1471-2180-11-66",
        "0a6cc057afb3f2dfe558b722d9b34169150ff0bb03cd811a1f1d35837d02a06a",
    ),
    "mattanovich": (
        "doi:10.1186/1475-2859-8-29",
        "5a9895037d69eec142443c94b3a81ed40ff75e09a51c5c6f404c7c8e14b90bc8",
    ),
    "nordkvist": ("doi:10.1128/AEM.69.6.3462-3468.2003", None),
}


def change(
    source,
    label,
    action,
    stage,
    locator,
    *,
    value=None,
    unit=None,
    basis=None,
    notes="",
    old=None,
    snippet=None,
):
    descriptor = {"preferred_term": label}
    if notes:
        descriptor["notes"] = notes
    if value is not None:
        descriptor["concentration"] = {"value": value, "unit": unit}
        if basis:
            descriptor["concentration"]["per_volume"] = basis
    result = {
        "action": action,
        "ingredient": descriptor,
        "stage": stage,
        "evidence": [
            {
                "reference": SOURCES[source][0],
                "supports": "SUPPORT",
                "snippet": snippet or label,
                "explanation": locator + ". Primary source inspected 2026-11-16; "
                "supports this source-scoped variant assertion, not equivalence of the whole parent recipe.",
            }
        ],
    }
    if old:
        result["replaced_ingredient"] = {
            "preferred_term": old,
            "notes": "Displaced parent descriptor; not a positive variant ingredient.",
        }
    return result


def decisions():
    claims, statuses = {}, {}

    def put(
        number,
        values,
        status="STRUCTURED",
        reason="Source-supported named changes retained with their stage and literal quantity basis.",
    ):
        claims[number] = values
        statuses[number] = {
            "queue_row_number": number,
            "status": status,
            "reason": reason,
            "assertion_count": len(values),
        }

    # Alternative complete formulation: additions belong to the alternative route,
    # never to the commercial parent's ingredient set.
    components = [
        ("(NH4)2SO4", "0.5 g"),
        ("KH2PO4", "1.5 g"),
        ("Na2HPO4", "1.5 g"),
        ("Sodium citrate", "0.4 g"),
        ("MgSO4", "0.025 g"),
        ("CaCl2", "0.5 mg"),
        ("ZnSO4", "1 mg"),
        ("CuSO4", "1 mg"),
        ("L-Glutamic acid", "0.5 g"),
        ("Ferric ammonium citrate", "0.04 g"),
        ("Pyridoxine", "1 mg"),
        ("Biotin", "0.5 mg"),
        ("Malachite green", "0.25 mg"),
        ("Agar", "15 g"),
        ("Distilled water", "1000 ml"),
    ]
    for number, (label, amount) in enumerate(components, 321):
        put(
            number,
            [
                change(
                    "middlebrook",
                    label,
                    "ADD",
                    "from-scratch alternative to commercial 7H10 preparation",
                    "Page 1, alternative Bacto Middlebrook 7H10 table",
                    notes=f"Literal alternative preparation input: {amount}. Do not add to the commercial route "
                    "or infer final concentration/volume. Unstated salt/hydrate forms remain unresolved.",
                    snippet=(
                        "Na-citrate"
                        if label == "Sodium citrate"
                        else "Bacto agar" if label == "Agar" else label
                    ),
                )
            ],
        )
    put(
        336,
        [],
        "ALREADY_STRUCTURED",
        "The 1000 ml water input is represented by row335; remaining text is route/volume/pH context without a named titrant.",
    )

    # Current DSMZ670 versions remain separate from the historical parent.
    for number in (290, 294, 298, 301):
        put(
            number,
            [],
            "HELD_MODEL",
            "Water identity already exists in the parent. The change is an absolute950ml batch input versus1000ml, not a concentration; quantity-only representation gap #760. Do not encode it as added950ml or950ml/L.",
        )
    for number in (291, 295, 299, 302):
        put(
            number,
            [],
            "CONDITION_ONLY",
            "Autoclave/incubation conditions, with no additional named ingredient assertion.",
        )
    for number, strain in ((292, "9463"), (296, "9466")):
        put(
            number,
            [
                change(
                    "dsm670",
                    "FeSO4 x 7 H2O",
                    "REMOVE",
                    "current DSMZ670 strain-specific formulation",
                    "Page1, For DSM" + strain,
                    snippet="FeSO4",
                ),
                change(
                    "dsm670",
                    "powdered sulfur",
                    "ADD",
                    "sterilized sulfur addition before use",
                    "Page1, For DSM" + strain,
                    value="5.00",
                    unit="G_PER_L",
                    snippet="powdered sulfur",
                    notes="Steam in a boiling water bath for3hours on each of3successive days; this is a reported final-medium mass concentration.",
                ),
            ],
        )

    def acid(strength, ph, locator, stage="pH adjustment before autoclaving"):
        return change(
            "dsm670",
            "H2SO4",
            "ADD",
            stage,
            locator,
            snippet="H2SO4",
            notes=f"Titrant strength {strength}; adjust to pH{ph}. Fixed dose is unspecified; do not convert normality to molarity or a final-medium concentration.",
        )

    put(293, [acid("1 N", "3.5", "Page1, For DSM9463")])
    put(
        297,
        [
            acid("1 N", "3.0", "Page1, For DSM9466"),
            change(
                "dsm670",
                "yeast extract",
                "ADD",
                "sterile stock addition before use",
                "Page1, For DSM9466",
                value="0.20",
                unit="G_PER_L",
                notes="Reported final concentration; stock strength, dose and sterilization method are unspecified.",
            ),
        ],
    )
    put(
        300,
        [
            acid("1 N", "3.0", "Page1, For DSM9467"),
            change(
                "dsm670",
                "FeSO4 x 7 H2O",
                "REMOVE",
                "current DSMZ670 strain-specific formulation",
                "Page1, For DSM9467",
                snippet="FeSO4",
            ),
            change(
                "dsm670",
                "D-glucose",
                "ADD",
                "filter-sterilized stock addition before use",
                "Page1, For DSM9467",
                value="2.00",
                unit="G_PER_L",
                notes="Final concentration; stock strength and volume unspecified.",
            ),
            change(
                "dsm670",
                "yeast extract",
                "ADD",
                "filter-sterilized stock addition before use",
                "Page1, For DSM9467",
                value="0.1",
                unit="G_PER_L",
                notes="Final concentration; stock strength and volume unspecified.",
            ),
        ],
    )
    put(
        303,
        [
            acid("4 N", "1.6", "Page1, For DSM9468"),
            change(
                "dsm670",
                "FeSO4 x 7 H2O",
                "ADD",
                "ferrous sulfate stock preparation",
                "Page1, base table and preparation step1",
                value="40",
                unit="PERCENT_W_V",
                basis="stock solution, not final medium",
                snippet="40%",
                notes="50ml of this stock is added per recipe batch before use; no final-volume normalization. Filter sterilized under100%N2.",
            ),
            change(
                "dsm670",
                "H2SO4",
                "ADD",
                "ferrous sulfate stock solvent",
                "Page1, preparation step1",
                snippet="0.2 N",
                notes="Stock prepared with0.2N sulfuric acid; preserve normality without molar conversion. Gas atmosphere is context, not an extra liquid ingredient.",
            ),
        ],
        reason="Stock composition/titrant identities structured. The50ml per-batch stock addition remains exact notes, not a separately computed final concentration.",
    )

    # Villasenor final concentrations and preparation stages.
    for first in (350, 355):
        put(
            first,
            [
                change(
                    "villasenor",
                    label,
                    "SET_CONCENTRATION",
                    "separately filter-sterilized vitamin addition after base sterilization",
                    "Methods, Bacterial strains, media and growth conditions",
                    value="10",
                    unit="MICROG_PER_ML",
                    notes="Reported final culture concentration; no unreported salt form or parent molar-equivalence claim.",
                )
                for label in ("biotin", "thiamine")
            ],
        )
        put(
            first + 1,
            [
                change(
                    "villasenor",
                    "CaCl2 dihydrate",
                    "REPLACE",
                    "separately autoclaved calcium addition after base sterilization",
                    "Methods, medium formulation",
                    value="1.49",
                    unit="MILLIMOLAR",
                    old="Calcium chloride anhydrous",
                    snippet="CaCl2",
                    notes="Reported final concentration of the stated dihydrate; equal molarity does not establish equal supplied form.",
                ),
                change(
                    "villasenor",
                    "FeCl3 hexahydrate",
                    "REPLACE",
                    "filter-sterilized iron addition after base sterilization",
                    "Methods, medium formulation",
                    value="0.0184",
                    unit="MILLIMOLAR",
                    old="Iron(III) chloride",
                    snippet="FeCl3",
                    notes="Reported final concentration of stated hexahydrate; do not inherit the unspecified parent form.",
                ),
            ],
        )
        put(
            first + 2,
            [],
            "ALREADY_STRUCTURED",
            "Source confirms parent succinate10mM, NH4Cl10mM, K2HPO4 1.26mM and MgSO4 0.83mM. No new change or inferred counterion/hydrate; scoped source text remains intact.",
        )
        put(
            first + 3,
            [],
            "ALREADY_STRUCTURED",
            "Named components are represented in the parent and rows"
            + str(first)
            + "–"
            + str(first + 2)
            + ". This row supplies preparation sequence; new assertions already carry the relevant addition stages, with no generic filtration inherited.",
        )
    put(
        354,
        [
            change(
                "villasenor",
                "calcium pantothenate",
                "REMOVE",
                "MM formulation (without MMP supplement)",
                "Methods, distinction between MM and MMP",
                snippet="calcium pantothenate",
                notes="Explicit exclusion from MM, not a positive growth-medium occurrence or a claim that material was physically removed.",
            )
        ],
    )
    put(
        359,
        [
            change(
                "villasenor",
                "calcium pantothenate",
                "SET_CONCENTRATION",
                "MMP final formulation",
                "Methods, MMP formulation",
                value="1",
                unit="MICROMOLAR",
                notes="Source concentration of the calcium salt; not twice this amount and not a pantothenate-anion dose.",
            )
        ],
    )

    # Nordkvist: reactor, timed feed and preculture remain distinct.
    for number in (372, 375, 377):
        put(
            number,
            [
                change(
                    "nordkvist",
                    "MnSO4",
                    "REPLACE",
                    "microaerobic reactor medium preparation",
                    "Materials and Methods, Strain and growth conditions",
                    value="1.25e-5",
                    unit="G_PER_L",
                    old="Manganese chloride",
                    notes="Hydrate not specified; retain reported mass concentration without molar conversion.",
                )
            ],
        )
    for number in (373, 376, 378):
        put(
            number,
            [],
            "HELD_EVIDENCE",
            "Preculture has threefold phosphate relative to reactor, but exact reactor phosphate requires the full1995MS10base source. Retain scope without inferring quantities or normalizing parent values.",
        )
    put(
        374,
        [
            change(
                "nordkvist",
                "sodium acetate",
                "ADD",
                "timed addition after7h38min of microaerobic cultivation",
                "Figure1B caption",
                value="0.3",
                unit="G_PER_L",
                notes="Added during cultivation; not an initial-medium concentration or parent molar-equivalence claim.",
            )
        ],
    )
    put(
        379,
        [
            change(
                "nordkvist",
                "DL-6,8-thioctic acid",
                "REMOVE",
                "Figure1C microaerobic treatment formulation",
                "Figure1C caption",
                snippet="thioctic acid",
            ),
            change(
                "nordkvist",
                "sodium acetate",
                "SET_CONCENTRATION",
                "Figure1C microaerobic treatment formulation",
                "Figure1C caption",
                value="0.82",
                unit="G_PER_L",
                notes="Separate Figure1C formulation, not Figure1B timed feed and not certification of the parent's9.996mM conversion.",
            ),
        ],
    )

    # Mattanovich additional file3: chemostat and trace-stock columns inspected.
    put(
        220,
        [
            change(
                "mattanovich",
                "glucose monohydrate",
                "REPLACE",
                "chemostat medium preparation",
                "Additional file3, cellsA13–A14",
                value="50.0",
                unit="G_PER_L",
                old="Glycerol",
                snippet="glucose",
            )
        ],
    )
    put(
        221,
        [
            change(
                "mattanovich",
                "citric acid",
                "REPLACE",
                "chemostat medium preparation",
                "Additional file3, cellsA13,A15",
                value="0.9",
                unit="G_PER_L",
                old="Citrate",
            ),
            change(
                "mattanovich",
                "KCl",
                "SET_CONCENTRATION",
                "chemostat medium preparation",
                "Additional file3, cellsA13,A16",
                value="1.7",
                unit="G_PER_L",
            ),
            change(
                "mattanovich",
                "(NH4)2HPO4",
                "REPLACE",
                "chemostat medium preparation",
                "Additional file3, cellsA13,A17",
                value="4.35",
                unit="G_PER_L",
                old="Ammonium phosphate",
            ),
        ],
    )
    put(
        222,
        [
            change(
                "mattanovich",
                "CaCl2 dihydrate",
                "REPLACE",
                "chemostat medium preparation",
                "Additional file3, cellsA13,A18",
                value="0.01",
                unit="G_PER_L",
                old="Calcium chloride anhydrous",
                snippet="CaCl2",
            ),
            change(
                "mattanovich",
                "MgSO4 heptahydrate",
                "REPLACE",
                "chemostat medium preparation",
                "Additional file3, cellsA13,A19",
                value="0.65",
                unit="G_PER_L",
                old="Magnesium sulfate",
                snippet="MgSO4",
            ),
        ],
    )
    put(
        223,
        [
            change(
                "mattanovich",
                "biotin stock (0.2 g/L)",
                "REPLACE",
                "stock addition to chemostat medium",
                "Additional file3, cellsA13,A20",
                value="1",
                unit="ML_PER_L",
                old="Biotin",
                snippet="Biotin",
                notes="Literal0.2g/L biotin stock, added1ml per liter of chemostat medium. Mixture-level descriptor; no inferred final biotin molarity.",
            ),
            change(
                "mattanovich",
                "biotin",
                "ADD",
                "biotin stock preparation",
                "Additional file3, cellA20",
                value="0.2",
                unit="G_PER_L",
                basis="per liter of biotin stock, not final medium",
            ),
        ],
    )
    old_trace = [
        "Sulfate",
        "Boric acid",
        "Sodium molybdate",
        "Manganese sulfate",
        "Ferrous sulfate",
        "Cobalt chloride",
        "Cupric sulfate",
        "Zinc Chloride",
        "Sodium iodide",
    ]
    put(
        224,
        [
            change(
                "mattanovich",
                label,
                "REMOVE",
                "replacement of flattened parent trace entries by a stock addition",
                "Additional file3, A21 and A24–A33; parent descriptor comparison",
                snippet="stock solution",
                notes="Removed as a flattened final-medium entry; source stock constituents are retained separately at their stock-preparation stage.",
            )
            for label in old_trace
        ]
        + [
            change(
                "mattanovich",
                "trace-salts stock solution",
                "ADD",
                "stock addition to chemostat medium",
                "Additional file3, cellsA13,A21",
                value="1.6",
                unit="ML_PER_L",
                snippet="stock solution",
                notes="Stock dose, not concentrations of its individual constituents.",
            )
        ],
    )
    stock = [
        ("CuSO4 pentahydrate", "6.0", "CuSO4", "A25"),
        ("NaI", "0.08", "NaI", "A26"),
        ("MnSO4 monohydrate", "3.0", "MnSO4", "A27"),
        ("Na2MoO4 dihydrate", "0.2", "Na2MoO4", "A28"),
        ("H3BO3", "0.02", "H3BO3", "A29"),
        ("CoCl2", "0.5", "CoCl2", "A30"),
        ("ZnCl2", "20.0", "ZnCl2", "A31"),
        ("FeSO4 heptahydrate", "5.0", "FeSO4", "A32"),
    ]
    put(
        225,
        [
            change(
                "mattanovich",
                label,
                "ADD",
                "trace-salts stock preparation",
                "Additional file3, cellsA24," + cell,
                value=value,
                unit="G_PER_L",
                basis="per liter of trace-salts stock, not final medium",
                snippet=snippet,
                notes="Only the source-stated hydrate/form is retained; stock is added separately at1.6ml/L.",
            )
            for label, value, snippet, cell in stock
        ]
        + [
            change(
                "mattanovich",
                "H2SO4 (95–98% w/w)",
                "ADD",
                "trace-salts stock preparation",
                "Additional file3, cellsA24,A33",
                value="5",
                unit="ML_PER_L",
                basis="per liter of trace-salts stock, not final medium",
                snippet="H2SO4",
                notes="Source reagent strength95–98%w/w. No density, molar conversion or pure-acid final concentration inferred.",
            )
        ],
    )
    put(
        226,
        [
            change(
                "mattanovich",
                "HCl",
                "ADD",
                "initial chemostat medium pH adjustment",
                "Additional file3, cellA22",
                notes="25%HCl to pH5.0; percentage basis and fixed titrant volume unspecified.",
            ),
            change(
                "mattanovich",
                "ammonium hydroxide",
                "ADD",
                "chemostat pH control during cultivation",
                "Additional file3, cellA39",
                notes="25%ammonium hydroxide for pH5.0 control; percentage basis and delivered dose unspecified.",
            ),
        ],
    )
    return claims, statuses


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    inventory = json.loads(args.inventory.read_text())
    if inventory["summary"]["queue_sha256"] != QUEUE_SHA:
        raise ValueError("manual decisions belong to a different queue")
    claims, statuses = decisions()
    expected = (
        set(range(220, 227))
        | set(range(290, 304))
        | set(range(321, 337))
        | set(range(350, 360))
        | set(range(372, 380))
    )
    if set(statuses) != expected:
        raise ValueError("incomplete source-family disposition coverage")
    records, variants = {}, defaultdict(dict)
    for number, changes in sorted(claims.items()):
        if not changes:
            continue
        row = inventory["rows"][number - 1]
        path = "data/normalized_yaml/" + row["source_path"]
        if hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != row["source_sha256"]:
            raise ValueError("source changed: " + path)
        record = records.setdefault(
            path,
            {
                "path": path,
                "recipe_id": row["recipe_id"],
                "expected_sha256": row["source_sha256"],
                "variants": [],
            },
        )
        vi = int(row["variant_index"])
        if vi not in variants[path]:
            variant = {
                "variant_index": vi,
                "variant_name": row["variant_name"],
                "ingredient_changes": [],
            }
            variants[path][vi] = variant
            record["variants"].append(variant)
        for item in changes:
            item["source_modification_index"] = int(row["modification_index"])
            item["source_text"] = row["modification_text"]
            variants[path][vi]["ingredient_changes"].append(item)
    payload = {
        "schema_version": 1,
        "source_queue_sha256": QUEUE_SHA,
        "source_inspections": {
            key: {"reference": value[0], "sha256": value[1]} for key, value in SOURCES.items()
        },
        "records": list(records.values()),
        "dispositions": [statuses[number] for number in sorted(statuses)],
    }
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(payload, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    print(
        json.dumps(
            {
                "records": len(records),
                "rows": len(statuses),
                "assertions": sum(len(items) for items in claims.values()),
            }
        )
    )


if __name__ == "__main__":
    main()
