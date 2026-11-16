#!/usr/bin/env python3
"""Prepare reviewed literal variant proposals for CultureMech #683, 2026-11-16.

Inputs: pinned planning inventory, unchanged normalized recipes, fresh primary
source receipts. Outputs: new proposal JSON and complete assigned-row dispositions.
The explicit scientific decisions below were authored after source inspection;
this is not an NLP extractor or identity resolver. It never writes recipe files.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from inspect_variant_family_context_683 import FAMILIES, inspect

ROOT = Path(__file__).resolve().parents[2]
C13 = "doi:10.1038/ismej.2012.122"
C14 = "doi:10.1038/ncomms5346"
J93 = "doi:10.1128/aem.59.12.4363-4366.1993"
P10 = "doi:10.1371/journal.pcbi.1000822"
T09 = "doi:10.1002/btpr.227"

# Literal Table 1 forms and final molar doses, not mass conversions.
HYDRATES = [
    (
        "Magnesium sulfate",
        "Magnesium sulfate heptahydrate",
        "2.8",
        "MILLIMOLAR",
        "MgSO4·7H2O2.8 mm",
    ),
    (
        "Calcium chloride anhydrous",
        "Calcium chloride dihydrate",
        "10",
        "MILLIMOLAR",
        "CaCl2·2H2O10 mm",
    ),
    ("Manganese chloride", "Manganese chloride tetrahydrate", "9", "NANOMOLAR", "MnCl2·4H2O9 nm"),
    ("Zinc sulfate", "Zinc sulfate heptahydrate", "800", "PICOMOLAR", "ZnSO4·7H2O800 pM"),
    ("Cobalt chloride", "Cobalt chloride hexahydrate", "500", "PICOMOLAR", "CoCl2·6H2O500 pM"),
    ("Sodium molybdate", "Sodium molybdate dihydrate", "300", "PICOMOLAR", "Na2MoO4·2H2O300 pM"),
    ("Nickel chloride", "Nickel chloride hexahydrate", "1", "NANOMOLAR", "NiCl2·6H2O1 nm"),
]
VITAMINS = [
    ("B1", "6", "MICROMOLAR", "B16 μm"),
    ("B3", "800", "NANOMOLAR", "B3800 nm"),
    ("B5", "425", "NANOMOLAR", "B5425 nm"),
    ("B6", "500", "NANOMOLAR", "B6500 nm"),
    ("B9", "4", "NANOMOLAR", "B94 nm"),
    ("B12", "700", "PICOMOLAR", "B12700 pM"),
    ("Myo-inositol", "6", "MICROMOLAR", "Myo-inositol6 μm"),
    ("4-Aminobenzoic acid", "60", "NANOMOLAR", "4-Aminobenzoic acid60 nm"),
]


def descriptor(name, value=None, unit=None, notes=None):
    item = {"preferred_term": name}
    if value is not None:
        item["concentration"] = {"value": value, "unit": unit}
    if notes:
        item["notes"] = notes
    return item


def event(row, action, ingredient, reference, quote, explanation, stage, old=None):
    result = {
        "action": action,
        "ingredient": ingredient,
        "stage": stage,
        "source_modification_index": row["modification_index"],
        "source_text": row["source_text"],
        "evidence": [
            {
                "reference": reference,
                "supports": "SUPPORT",
                "snippet": quote,
                "explanation": explanation
                + " Primary source inspected 2026-11-16; no ontology identity or mass conversion inferred.",
            }
        ],
    }
    if old:
        result["replaced_ingredient"] = descriptor(old)
    return result


def require_parent(record, name):
    matches = [i for i in record["ingredients"] if i["preferred_term"] == name]
    if len(matches) != 1:
        raise ValueError(f"expected one parent {name!r}: {record['path']}")
    return matches[0]


def carini(record, row):
    mi = row["modification_index"]
    is2014 = "Carini 2014" in record["variants"][row["variant_index"]]["name"]
    reference = C14 if is2014 else C13
    stage = (
        "2014 alternate-phosphorus utilization assay"
        if is2014
        else "2013 Table 3 glycine-substitution assay"
    )
    out = []

    def add(action, name, value, unit, quote, explanation, old=None, notes=None, ref=None):
        if old:
            require_parent(record, old)
        out.append(
            event(
                row,
                action,
                descriptor(name, value, unit, notes),
                ref or reference,
                quote,
                explanation,
                stage,
                old,
            )
        )

    if mi == 0:
        dose = "100" if is2014 else "50"
        require_parent(record, "Pyruvate")
        add(
            "SET_CONCENTRATION",
            "Pyruvate",
            dose,
            "MICROMOLAR",
            "pyruvate (50 μm)" if not is2014 else "pyruvate (100 µM)",
            "2013 Glycine substitution experiments / 2014 Methods Organism source, p.5. The 2014 PDF page was visually inspected because extracted text corrupts the micro symbol.",
        )
        add(
            "REPLACE",
            "Methionine",
            "5" if is2014 else "10",
            "MICROMOLAR",
            "methionine (10 μm)" if not is2014 else "methionine (5 µM)",
            "The same assay paragraph states the methionine dose without stereochemistry. The new descriptor deliberately does not certify the imported DL form.",
            old="DL-methionine",
            notes="Stereochemistry unspecified by the source; imported DL-methionine identity is not certified.",
        )
        if is2014:
            require_parent(record, "Glycine")
            add(
                "SET_CONCENTRATION",
                "Glycine",
                "5",
                "MICROMOLAR",
                "glycine (5 µM)",
                "2014 Methods Organism source, p.5, alternate-phosphorus assay; PDF page visually inspected.",
            )
    elif not is2014 and mi == 1:
        serine = "serine" in record["variants"][0]["name"].lower()
        old = "L-Serine" if serine else "Glycine"
        require_parent(record, old)
        add(
            "REPLACE" if serine else "SET_CONCENTRATION",
            "Serine" if serine else "Glycine",
            "25",
            "MICROMOLAR",
            "Each substitute was tested at a concentration of 25 μm",
            "2013 Glycine substitution experiments and Table 3: Serine is a listed substitute; Glycine is the positive control at the same stated 25 micromolar dose. No stereochemistry is supplied for serine.",
            old=old if serine else None,
            notes="Source serine stereochemistry is unspecified." if serine else None,
        )
    elif (is2014 and mi == 1) or (not is2014 and mi == 4):
        add(
            "REPLACE",
            "Iron(III) chloride hexahydrate",
            "1",
            "MICROMOLAR",
            "FeCl3 (1 μm)" if not is2014 else "FeCl3 (1 µM)",
            "Assay Methods overrides the basal iron dose with 1 micromolar FeCl3. Carini 2013 Table 1 specifies FeCl3·6H2O for AMS1; the basal 117 nM is not retained.",
            old="Iron(III) chloride",
            notes="Hydrate from the explicitly referenced AMS1 base formulation; dose from the assay Methods.",
        )
        (
            out[-1]["evidence"].append(
                {
                    "reference": C13,
                    "supports": "SUPPORT",
                    "snippet": "FeCl3·6H2O117 nm",
                    "explanation": "AMS1 Table 1 specifies the hexahydrate. This snippet supports form only; the separate assay Methods supplies the overriding 1 micromolar dose.",
                }
            )
            if is2014
            else None
        )
    elif (is2014 and mi == 2) or (not is2014 and mi == 5):
        for name, dose, unit, quote in VITAMINS:
            old = "Thiamine" if is2014 and name == "B1" else None
            add(
                "REPLACE" if old else "ADD",
                name,
                dose,
                unit,
                quote,
                "Carini 2013 Table 1, Vitamins, final-concentration column; the complete mixture is retained for the study assay. B-number labels are literal source designations, not an assertion of a particular vitamer/salt. The 2014 Methods repeats the same mixture.",
                old=old,
                notes=(
                    "Molecular and salt forms of B-number vitamin labels remain unspecified by this source."
                    if name.startswith("B")
                    else None
                ),
                ref=C13,
            )
        if not is2014:
            old = "4-Amino-5-hydroxymethyl-2-methylpyrimidine"
            require_parent(record, old)
            out.append(
                event(
                    row,
                    "REMOVE",
                    descriptor(old),
                    C13,
                    "B16 μm",
                    "Table 1 specifies B1 in its complete vitamin mixture, not the imported HMP substitute. Remove HMP only within this source-specific alternative vitamin formulation; do not assert universal HMP equivalence.",
                    stage,
                )
            )
        return (
            out,
            "STRUCTURED",
            "Partial: source-literal vitamin designations/doses structured; B7/biotin 4 nM already present and retained. Specific vitamers/salt forms remain unresolved; no B-number ontology identity assigned.",
        )
    elif (is2014 and mi == 3) or (not is2014 and mi in (2, 3)):
        subset = HYDRATES if is2014 else HYDRATES[:1] if mi == 2 else HYDRATES[1:]
        for old, name, dose, unit, quote in subset:
            add(
                "REPLACE",
                name,
                dose,
                unit,
                quote,
                "Carini 2013 AMS1 Table 1, explicit compound form and final concentration. Preserve stated molar dose, with no molecular-weight or mass conversion.",
                old=old,
                ref=C13,
            )
    elif is2014 and mi == 4:
        out.append(
            event(
                row,
                "REMOVE",
                descriptor("Sodium dihydrogen phosphate"),
                C14,
                "without added Pi",
                "2014 Methods Organism source omits added phosphate from the AMS1 assay base. This refers to phosphate of the original Table 1 AMS1 formulation, not a claim that the imported parent currently contains it or that residual phosphate is zero.",
                "2014 alternate-phosphorus assay base preparation",
            )
        )
    elif is2014 and mi == 5:
        selections = {
            "CultureMech:007386": ("Sodium Phosphite", None),
            "CultureMech:007388": ("D-Glucose 6-phosphate", "Glucose 6-phosphate"),
            "CultureMech:007389": ("D-Ribose 5-phosphate", "Ribose 5-phosphate"),
            "CultureMech:007390": ("Methylphosphonic acid", "Methylphosphonic acid"),
            "CultureMech:007391": ("2-Aminoethylphosphonate", "2-aminoethylphosphonic acid"),
            "CultureMech:007392": ("O-Phospho-L-serine", "Phosphoserine"),
        }
        old, name = selections[record["recipe_id"]]
        if name is None:
            return (
                [],
                "HELD_EVIDENCE",
                "The source prints phosphite as NaPHO3.5H2O; its stoichiometry is unresolved. Literal formula and 1 µM dose remain in prose; no corrected salt identity is asserted.",
            )
        require_parent(record, old)
        add(
            "SET_CONCENTRATION" if name == old else "REPLACE",
            name,
            "1.0",
            "MICROMOLAR",
            "1.0 µM " + ("MPn" if name == "Methylphosphonic acid" else name.lower()),
            "2014 Methods alternate-phosphorus experiment, p.5: each listed P source tested separately. Preserve source chemical label without certifying the imported stereoisomer or protonation state. The glucose Figure 1 label conflict is retained in source_text.",
            old=old if name != old else None,
            notes="Separate P-source assay, not a simultaneous mixture; unspecified stereochemistry/salt form remains unresolved.",
        )
    else:
        return (
            [],
            "CONDITION_ONLY",
            "Preparation order, gas sparging and pH context retained as prose. No dissolved-gas dose or new positive ingredient is inferred.",
        )
    return (
        out,
        "STRUCTURED",
        "Source-supported variant event(s); base ingredients/prose unchanged. Unspecified stereochemistry is retained explicitly without ontology assignment.",
    )


def other_family(family, record, row):
    mi = row["modification_index"]
    if family == "jensen_bl_source_family":
        if mi == 1:
            require_parent(record, "Pantothenate")
            return (
                [
                    event(
                        row,
                        "REPLACE",
                        descriptor(
                            "Calcium pantothenate",
                            notes="Table 1 gives 2 micromolar on a pantothenate basis; no calcium-salt molarity or calcium concentration is inferred.",
                        ),
                        J93,
                        "calcium pantothenate",
                        "p.4363 formulation paragraph identifies the calcium salt; Table 1 footnote b states 2 micromolar pantothenate. Read from the primary ASM PDF via browser; anonymous local download failed, so no local source hash is claimed.",
                        "BL medium vitamin-stock preparation",
                        "Pantothenate",
                    )
                ],
                "STRUCTURED",
                "Calcium salt identity retained without converting pantothenate-basis amount to salt molarity.",
            )
        if mi == 0:
            return (
                [],
                "CONDITION_ONLY",
                "Stock filtration pore size/order is preparation context, not an ingredient occurrence.",
            )
        if mi == 2:
            return (
                [],
                "HELD_EVIDENCE",
                "Nominal formulation retained; MgCl2 hydration and molybdate formula/hydration remain unresolved. No imported hydrate is certified.",
            )
        return (
            [],
            "ALREADY_STRUCTURED",
            "Existing treatment ingredient/dose retained; this row adds Table 3 context rather than a new variant ingredient. No growth claim revalidated.",
        )
    if family == "pinchuk_m1_source_family":
        if mi == 0:
            require_parent(record, "Dibasic sodium phosphate")
            return (
                [
                    event(
                        row,
                        "REPLACE",
                        descriptor("Sodium dihydrogen phosphate monohydrate", "4.35", "MILLIMOLAR"),
                        P10,
                        "4.35 mM NaH2PO4•H2O",
                        "Methods, Culture medium: modified M1 recipe explicitly supplies monobasic sodium phosphate monohydrate; replace the imported dibasic-phosphate descriptor only in this batch variant.",
                        "modified M1 batch culture",
                        "Dibasic sodium phosphate",
                    )
                ],
                "STRUCTURED",
                "Explicit phosphate-form replacement; no parent recipe equivalence inferred.",
            )
        if mi == 1:
            return (
                [],
                "HELD_MODEL",
                "Source names 10× Wolfe vitamin/mineral stock additions; correspondence to the parent's flattened stock components and final-volume basis are unresolved. Do not add stock components twice or invent individual replacements.",
            )
        require_parent(record, "PIPES")
        return (
            [],
            "ALREADY_STRUCTURED",
            "Batch PIPES 30 mM already present; pH and exclusion of chemostat/anaerobic treatments remain context. No chemostat Fe(III)-NTA or fumarate added.",
        )
    if family == "tang_tracer_source_family":
        if mi == 0:
            require_parent(record, "PIPES")
            return (
                [
                    event(
                        row,
                        "SET_CONCENTRATION",
                        descriptor("PIPES", "20", "MILLIMOLAR"),
                        T09,
                        "buffered with 20mM PIPES",
                        "Methods, p.4, isotope-tracer growth medium. This overrides the imported 10 mM for this variant only.",
                        "isotope-tracer growth assay",
                    )
                ],
                "STRUCTURED",
                "Literal study buffer concentration; no base mutation.",
            )
        if mi == 1:
            require_parent(record, "Sodium L-lactate")
            return (
                [
                    event(
                        row,
                        "REPLACE",
                        descriptor(
                            "[3-13C] sodium L-lactate",
                            "30",
                            "MILLIMOLAR",
                            "Source reports 98% for the supplied labeled reagent; no unlabeled-lactate ontology identity is inherited.",
                        ),
                        T09,
                        "[3-13C] sodium L-lactate",
                        "Methods, p.4: labeled lactate supplied at 30 mM in the growth medium. Isotope label and L stereochemistry preserved; no assumption about downstream isotope-resolved mapping.",
                        "isotope-tracer growth assay",
                        "Sodium L-lactate",
                    )
                ],
                "STRUCTURED",
                "Labeled substrate kept distinct from imported unlabeled sodium L-lactate.",
            )
        return (
            [],
            "HELD_MODEL",
            "AA-S-18 is a 17-component mixture at 25 µM each, not 25 µM mixture. Exact correspondence to flattened imported amino acids (including DL forms) remains unresolved; no duplicate mixture/individual presence or unsupported stereochemistry is asserted.",
        )
    raise ValueError(family)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    sources = []
    for directory, reference in [
        ("carini-2013-html", C13),
        ("carini-2014", C14),
        ("pinchuk-2010", P10),
        ("tang-2009", T09),
    ]:
        receipt_path = ROOT / ".temp/variant-683/family-sources" / directory / "receipt.json"
        receipt = json.loads(receipt_path.read_text())
        source_files = list(receipt_path.parent.glob("source.*"))
        if (
            len(source_files) != 1
            or hashlib.sha256(source_files[0].read_bytes()).hexdigest() != receipt["sha256"]
        ):
            raise ValueError(f"source capture differs from receipt: {directory}")
        receipt.pop(
            "response_url", None
        )  # Keep stable source URL; redirects remain in private receipt.
        sources.append(
            {"reference": reference, "receipt": str(receipt_path.relative_to(ROOT)), **receipt}
        )
    sources.append(
        {
            "reference": J93,
            "url": "https://journals.asm.org/doi/epdf/10.1128/aem.59.12.4363-4366.1993",
            "inspected_on": "2026-11-16",
            "locator": "pp.4363–4364, formulation paragraph, Table 1 footnote b, Table 3",
            "access_limitation": "Primary PDF text inspected with browser tool; anonymous local downloads failed (403/500). No local source hash available.",
        }
    )
    records, dispositions = [], []
    for family in sorted(FAMILIES):
        context = inspect(ROOT, args.inventory, family)
        for record in context["records"]:
            by_variant = {}
            for row in record["queue_rows"]:
                events, status, reason = (
                    carini(record, row)
                    if family == "carini_ams1_source_family"
                    else other_family(family, record, row)
                )
                by_variant.setdefault(row["variant_index"], []).extend(events)
                dispositions.append(
                    {
                        "queue_row_number": row["queue_row_number"],
                        "family": family,
                        "path": record["path"],
                        "recipe_id": record["recipe_id"],
                        "variant_index": row["variant_index"],
                        "source_modification_index": row["modification_index"],
                        "status": status,
                        "reason": reason,
                        "assertion_count": len(events),
                    }
                )
            variants = [
                {
                    "variant_index": vi,
                    "variant_name": record["variants"][vi]["name"],
                    "ingredient_changes": events,
                }
                for vi, events in by_variant.items()
                if events
            ]
            if variants:
                records.append(
                    {
                        "path": record["path"],
                        "recipe_id": record["recipe_id"],
                        "expected_sha256": record["sha256"],
                        "variants": variants,
                    }
                )
    dispositions.sort(key=lambda row: row["queue_row_number"])
    inventory = json.loads(args.inventory.read_text())
    expected = sorted(
        n
        for group in inventory["planning_groups"]
        if group["name"] in FAMILIES
        for n in group["queue_row_numbers"]
    )
    if [d["queue_row_number"] for d in dispositions] != expected or len(expected) != 98:
        raise ValueError("assigned-row disposition membership mismatch")
    result = {
        "schema_version": 1,
        "issue": "https://github.com/CultureBotAI/CultureMech/issues/683",
        "scope": "98 exact queue rows in Carini AMS1, Jensen BL, Pinchuk M1 and Tang tracer families; proposals only, no recipe application or whole-record certification.",
        "source_inspection": sources,
        "inventory_sha256": hashlib.sha256(args.inventory.read_bytes()).hexdigest(),
        "records": records,
        "dispositions": dispositions,
    }
    with args.output.open("x", encoding="utf-8") as stream:
        json.dump(result, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    print(
        json.dumps(
            {
                "output": str(args.output),
                "records": len(records),
                "queue_rows": len(dispositions),
                "assertions": sum(d["assertion_count"] for d in dispositions),
            }
        )
    )


if __name__ == "__main__":
    main()
