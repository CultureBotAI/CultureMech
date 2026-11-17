#!/usr/bin/env python3
"""Prepare manual model-held decisions for #683 (2026-11-16).

Inputs: pinned queue, prior coverage, base recipe bytes, inspected primary captures.
Output: exact-preimage proposal for 31 model rows and six quantity upgrades.
Never applies recipes; no chemical identity is inferred from name matching.
"""

from __future__ import annotations

import argparse
import copy
import csv
import json
from collections import Counter
from pathlib import Path

from prepare_evidence_completion_683 import (
    BASE,
    NEW,
    OLD,
    PRIOR_SOURCES,
    QUEUE_SHA,
    ROOT,
    SOURCES,
    Proposal,
    amount,
    conc,
    digest,
)

# Paths are relative to the prior capture directory except explicit new captures.
CAPTURES = {
    "751": (
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium751.pdf",
        "remaining-sources/dsmz-751/source.pdf",
        "721e0310d250ea6eab5d453f063b9452b48b8368ad53fa9384cb54434d2e59fb",
        "Page 1 liquid-medium instruction",
    ),
    "670": (
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium670.pdf",
        "sources/dsmz-670/source.pdf",
        "e21dbc3f7c16cf301001aaa5ca4ca7aa57fb486cbccba0995c46e094946917ab",
        "Page 1 base table and strain preparations",
    ),
    "125": (
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium125.pdf",
        "remaining-sources/dsmz-125/source.pdf",
        "e107edb0e43f303bc124e81ef0430f07fde07eb9efbcf1cea9c35e3a2190ad8f",
        "Page 1 carbon alternatives",
    ),
    "956": (
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium956.pdf",
        "remaining-sources/dsmz-956/source.pdf",
        "156fe7f9a826c658bf690c9c892ba7d137848d397f55cf93568c4c3145374f39",
        "Page 1 post-sterilization alternatives",
    ),
    "119": (
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium119.pdf",
        "sources/dsmz-119/source.pdf",
        "65295918764de4ed5b73ce773ab4057a7183ecf8bfd7fff0d02393d901b41a2a",
        "Strain-specific post-inoculation gas instructions",
    ),
    "hemiaulus": (
        "PMID:33083143",
        "sources/hemiaulus-2020/source.xml",
        "b2b891255be3531171e9479c4d8744724632f3b4e3f89573664273774d4f47e9",
        "Methods: naturally dissolved N2",
    ),
    "fertilizer": (
        "PMID:40484141",
        "sources/tap-fertilizer-2025/metadata.json",
        "3f738652b616e23152d9ce0740fc5f05ebabd63716e5a17cdc5482b56643d375",
        "Primary abstract only",
    ),
    "teusink": (
        "doi:10.1128/AEM.71.11.7253-7262.2005",
        "remaining-sources/teusink-2005/source.html",
        "3b4288d316e061cdad56879cb8a30c2cccff1fe3361eb0be71778d49c9dbef91",
        "Table 1 headings and footnotes",
    ),
    "tang": (
        "doi:10.1002/btpr.227",
        "family-sources/tang-2009/source.pdf",
        "ebbab61739c7a8c63213c57e0258f20822d165ef8188e23455ff8495689eb4be",
        "Author manuscript page 4",
    ),
    "pinchuk": (
        "doi:10.1371/journal.pcbi.1000822",
        "family-sources/pinchuk-2010/source.xml",
        "9fc877d8ff8e5822a2abf7e00ef5395d11cba3da89281ba3c2038e1c14de6d81",
        "Methods: Bacterial Strains and Growth Media",
    ),
    "bg11": (
        "PMID:34584038",
        "new:bg11-2021/source.xml",
        "669d11703f04dc008905d7ac0b78c5963585ff556d92fb0229ae63323634a697",
        "Methods: phototrophic BG-11 gas supply",
    ),
}
for _key in ("matsui", "kato", "kosch"):
    _ref, _path, _sha, _locator = SOURCES[_key]
    CAPTURES[_key] = (_ref, "new:" + _path, _sha, _locator)
CAPTURES["willard"] = PRIOR_SOURCES["willard"]


def ev(key, snippet, explanation, support="SUPPORT"):
    return {
        "reference": CAPTURES[key][0],
        "supports": support,
        "snippet": snippet,
        "explanation": explanation,
    }


def prepare(p):
    p.dispose(
        15,
        "CONTEXT_ONLY",
        "Whole modified-medium reference contains no named ingredient change. Primary Methods identify modified YBCII; no parent equivalence or unnamed removal is inferred.",
    )
    p.mention(
        17,
        "N2",
        "Primary Methods explicitly describe naturally dissolved N2, not deliberate supplementation. Presence as a nitrogen source is supported; no ADD operation or administered dose is asserted.",
        ["OPERATION"],
        stage="Hemiaulus fixed-N-free culture; naturally dissolved nitrogen",
        items=[
            ev(
                "hemiaulus",
                "recognizing that dissolved N2 will be abundant as an N source for diazotrophs",
                "Methods define no added organic or inorganic nitrogen; environmental dissolved-gas context is not a preparation addition.",
            )
        ],
    )
    p.dispose(
        17,
        "PARTIALLY_STRUCTURED",
        "Natural dissolved N2 retained as a field-specific mention; absent fixed nitrogen does not identify a particular removed chemical.",
    )
    gas_note = "Gas supply only; no liquid concentration or simultaneous use of alternative gas arms is implied."
    for label, stage in (
        ("CO2", "Matsui2018 high-CO2 aeration arm; 1% v/v CO2"),
        ("ambient air", "Matsui2018 ambient-air aeration arm; 0.04% v/v CO2"),
    ):
        p.change(
            30,
            "ADD",
            label,
            stage,
            [
                ev(
                    "matsui",
                    "constant aeration with 1% (v/v) CO2 (high CO2-grown cells) or ambient air containing 0.04% (v/v) CO2 (air-grown cells)",
                    "Cells and Culture Conditions; separate experimental arms.",
                )
            ],
            notes=gas_note,
        )
    p.dispose(
        30,
        "STRUCTURED",
        "Explicit gas supplies represented at aeration stages without liquid units.",
    )
    for percentage in ("5%", "0.04%"):
        p.change(
            33,
            "ADD",
            "CO2",
            "Tsuji2021 low-sodium aeration arm with " + percentage + " CO2 in air",
            [
                {
                    "reference": "DOI:10.1007/s10126-021-10037-4",
                    "supports": "SUPPORT",
                    "snippet": "aeration with air containing 5% CO2, but not with the air containing 0.04% CO2",
                    "explanation": "Publisher primary abstract inspected 2026-11-16. Low-sodium comparison names two supplied gas conditions with different growth outcomes. Input event makes no growth assertion or liquid-concentration claim. Full Methods inaccessible.",
                }
            ],
            notes=gas_note,
        )
    p.dispose(
        33,
        "STRUCTURED",
        "Primary abstract verifies gas treatments; negative growth in the low-CO2 arm is not reclassified as positive growth.",
    )
    p.change(
        41,
        "ADD",
        "water-soluble fertilizer",
        "Ab-WSF formulation; named fertilizer input",
        [
            ev(
                "fertilizer",
                "the trace and macroelements in TAP were replaced by water-soluble fertilizer (WSF)",
                "Primary abstract verifies mixture use, but does not enumerate displaced chemicals, product composition or dose.",
            )
        ],
    )
    p.mention(
        41,
        "water-soluble fertilizer",
        "Named fertilizer presence is supported independently. Exact product/formulation and dose are unavailable in the inspected abstract.",
        ["IDENTITY_FORM", "QUANTITY"],
        "ADD",
        "Ab-WSF formulation",
    )
    p.mention(
        41,
        "TAP trace and macroelements",
        "Source reports group replacement, but no precise displaced chemical list was inspected. No unlisted removal or component equivalence inferred.",
        ["IDENTITY_FORM", "OPERATION"],
        "REPLACE",
        "Ab-WSF formulation",
    )
    p.dispose(
        41,
        "PARTIALLY_STRUCTURED",
        "Named fertilizer input supported; component-set replacement and composition retained separately.",
    )
    for label, stage in (
        ("air", "ABC-009 BG-11 ambient-air phototrophic arm"),
        ("CO2", "ABC-009 BG-11 2% CO2 phototrophic arm"),
    ):
        p.change(
            55,
            "ADD",
            label,
            stage,
            [
                ev(
                    "bg11",
                    "ambient air or 2% CO2 was supplied at the rate of 0.5 vvm",
                    "Phototrophic Methods specify alternative supplied gases. Flow and gas fraction are not dissolved concentrations.",
                )
            ],
            notes=gas_note,
        )
    p.dispose(55, "STRUCTURED", "Both supplied gas arms verified in captured primary Methods.")
    for label in ("H2", "CO2"):
        p.change(
            85,
            "ADD",
            label,
            "Koschnitzki2017 final serum-bottle headspace exchange; H2/CO2 80:20 v/v, 1.5 bar",
            [
                ev(
                    "kosch",
                    "H2/CO2 (80:20, v/v) at 1.5 bar",
                    "Printed page 28: evacuation/gas exchange repeated three times; final pressure 1.5 bar per bottle. Distinct from N2/CO2 purge and N2/H2 chamber atmosphere.",
                )
            ],
            notes="Final preparation headspace only; no liquid concentration or unreported pressure-reference convention.",
        )
    p.dispose(
        85, "STRUCTURED", "Final-headspace gases supported; pH and temperature remain contextual."
    )
    for n, strain, pressure in (
        (89, "2030", "2"),
        (95, "9575", "2"),
        (99, "25939", "1"),
        (100, "25945", "1"),
    ):
        for label in ("H2", "CO2"):
            p.change(
                n,
                "ADD",
                label,
                f"DSM {strain} post-inoculation headspace; 80% H2/20% CO2, {pressure} bar overpressure",
                [
                    ev(
                        "119",
                        "80% H2 and 20% CO2",
                        f"Official instruction for DSM {strain}: sterile gas supplied after inoculation at {pressure} bar overpressure. Gas composition is not a liquid dose.",
                    )
                ],
                notes="Source ratio and overpressure belong to this strain-specific post-inoculation stage.",
            )
        p.dispose(
            n,
            "STRUCTURED",
            "Strain-specific gas additions verified without dissolved-concentration inference.",
        )
    stage = "Willard2024 low-sulfate DSM-88 aerobic cultures"
    p.change(
        108,
        "SET_CONCENTRATION",
        "elemental sulfur",
        stage,
        [
            ev(
                "willard",
                "Cultures were supplemented with 10 g/L of elemental sulfur.",
                "Source concentration in aerobic study medium; not a claim of a difference from every parent amount.",
            )
        ],
        conc("10", "G_PER_L"),
    )
    for value, species in (
        (
            "1",
            "A. brierleyi DSM1651, M. hakonensis HO1-1, M. prunae RON 12/II, M. sedula DSM5348, S. ohwakuensis TA-1 and S. tokodaii str.7",
        ),
        ("0.2", "S. metallicus DSM6482 and S. tepidarius IC-007"),
    ):
        p.change(
            108,
            "SET_CONCENTRATION",
            "yeast extract",
            stage + "; species arm: " + species,
            [
                ev(
                    "willard",
                    value + " g/L yeast extract",
                    "Species-specific paragraph identifies this group: "
                    + species
                    + ". Alternatives are not combined.",
                )
            ],
            conc(value, "G_PER_L"),
        )
    for label, value in (("sucrose", "2"), ("NZ-Amine", "1")):
        p.change(
            108,
            "ADD",
            label,
            stage + "; S. acidocaldarius MW001 and S. solfataricus P2 arm",
            [
                ev(
                    "willard",
                    "2 g/L sucrose and 1 g/L NZ-Amine",
                    "Exact supplement for S. acidocaldarius MW001 and S. solfataricus P2; no transfer to yeast-extract arms or full-formulation recertification.",
                )
            ],
            conc(value, "G_PER_L"),
        )
    p.dispose(
        108,
        "STRUCTURED",
        "Aggregate prose decomposed into explicit species-specific stages, not one simultaneous universal recipe.",
    )
    for label in ("Na2S", "N2"):
        p.mention(
            109,
            label,
            "Aerobic vented-bottle conditions verified. Source does not explicitly document removal of this local parent's ingredient; absence from a source list is not an observed removal.",
            ["OPERATION", "SOURCE_CLAIM"],
            "REMOVE",
            stage,
            items=[
                ev(
                    "willard",
                    "glass serum bottles vented with foam stoppers",
                    "Aeration context only; does not assert chemical removal.",
                    "PARTIAL",
                )
            ],
        )
    p.dispose(
        109,
        "PARTIALLY_STRUCTURED",
        "Both claimed omissions retained as withheld operations; aerobic setup remains context.",
    )
    for n, label, value in (
        (137, "KH2PO4", "1.5"),
        (138, "K2HPO4", "0.5"),
        (386, "KH2PO4", "1.5"),
        (387, "K2HPO4", "0.5"),
    ):
        p.change(
            n,
            "SET_AMOUNT",
            label,
            "DSMZ751 liquid-medium preparation batch",
            [
                ev(
                    "751",
                    "KH2PO4, 1.5 g and K2HPO4, 0.5 g",
                    "Page 1 liquid-medium instruction. Water plus added stocks is a batch recipe, not an established final litre.",
                )
            ],
            amount=amount(
                value,
                "G",
                "Literal grams in DSMZ751 liquid preparation batch; final volume unspecified.",
            ),
        )
        p.dispose(
            n,
            "STRUCTURED",
            "Exact batch mass represented with SET_AMOUNT; no concentration conversion.",
        )
    for label, strain in (
        ("CaCl2", "M. sporium DSM17706T"),
        ("YCl3", "Y-b3"),
        ("LaCl3", "La-a12"),
        ("CeCl3", "Ce-a6"),
    ):
        p.change(
            194,
            "ADD",
            label,
            "Kato2020 post-autoclave default metal supplementation; " + strain + " arm",
            [
                ev(
                    "kato",
                    "CaCl2 and REE chlorides (final concentration of 20 μM each, unless otherwise stated)",
                    "Methods assign CaCl2, YCl3, LaCl3 and CeCl3 to M. sporium DSM17706T and Y-b3, La-a12 and Ce-a6 respectively. Default not imposed on dose-response, no-metal or mixed-metal experiments. Hydration unspecified.",
                )
            ],
            conc("20", "MICROMOLAR"),
        )
    p.change(
        194,
        "ADD",
        "methane",
        "Kato2020 methane headspace alternative; one 26-mL tube with 5 mL basal medium",
        [
            ev(
                "kato",
                "methane (2 mL tube–1)",
                "2 mL gas aliquot per tube, not dissolved concentration or standard-state volume. Methanol is an alternative.",
            )
        ],
        amount=amount(
            "2",
            "ML",
            "One source culture-tube batch: 2 mL methane gas input; not per litre liquid.",
        ),
    )
    p.change(
        194,
        "ADD",
        "methanol",
        "Kato2020 methanol carbon-source alternative",
        [
            ev(
                "kato",
                "methanol (20‍ ‍mM)",
                "Methods alternative to methane; Unicode spacing retained from source. No simultaneous methane/methanol culture asserted.",
            )
        ],
        conc("20", "MILLIMOLAR"),
    )
    p.dispose(
        194,
        "STRUCTURED",
        "Default metal/strain arms and alternative carbon supplies represented separately.",
    )
    p.change(
        218,
        "ADD",
        "water",
        "Marteinsson2010 MB1/2 whole-medium dilution",
        [
            {
                "reference": "doi:10.1099/ijs.0.012724-0",
                "supports": "SUPPORT",
                "snippet": "diluted to half strength with water",
                "explanation": "Primary-paper copy page 2730 inspected in browser 2026-11-16. Diluent input supported; relative half-strength establishes no absolute water amount or component concentration. Local capture unavailable.",
            }
        ],
        notes="Whole-medium dilution only; medium name is not expanded into newly resolved chemicals.",
    )
    p.dispose(
        218,
        "STRUCTURED",
        "Water diluent represented without treating medium name as a chemical or calculating doses.",
    )
    for n in (268, 341):
        p.dispose(
            n,
            "CONTEXT_ONLY",
            "Table-membership instruction names no individual ingredient. Pyridox-x is explicitly an omission-experiment label, not a chemical. Existing source-specific dose events remain; no automatic full-table normalization or inferred parent equivalence.",
        )
    for n in (290, 294, 298, 301):
        p.change(
            n,
            "SET_AMOUNT",
            "distilled water",
            "DSMZ670 current source base-batch input before strain-specific additions",
            [
                ev(
                    "670",
                    "Distilled water 950.00 ml",
                    "Page 1 base table, whitespace normalized. Separate ferrous-sulfate stock and strain-specific omissions do not make water input a final-medium volume.",
                )
            ],
            amount=amount(
                "950",
                "ML",
                "Current DSMZ670 table input per preparation batch; not a final-volume assertion.",
            ),
        )
        p.dispose(
            n,
            "STRUCTURED",
            "950 mL batch input retained without using archive 1000 mL as a denominator.",
        )
    for n in (344, 347):
        p.change(
            n,
            "ADD",
            "AA-S-18 amino acid mixture",
            "Tang2009 defined-rich supplement; separate from unsupplemented minimal-medium arm",
            [
                ev(
                    "tang",
                    "a standard amino acid mix (containing 17 unlabeled amino acids, without tryptophan, glutamine, and asparagine, Cat#AA-S-18, Sigma, USA)",
                    "Manuscript page 4. Named commercial mixture supported, no inferred 17 precise stereochemical forms. Separate dose sentence: 'a final concentration of 25 µM for each amino acid', not a mixture molarity.",
                )
            ],
            notes="25 micromolar per included amino acid; no bulk-mixture molarity or individual stereochemical assignment.",
        )
        for label in ("tryptophan", "glutamine", "asparagine"):
            p.mention(
                n,
                label,
                "Source excludes this label from AA-S-18 supplement. Negative mixture membership is not an observed removal step or proof of whole-culture absence.",
                ["OPERATION"],
                "REMOVE",
                "Tang2009 AA-S-18 supplement membership only",
                items=[
                    ev(
                        "tang",
                        "without tryptophan, glutamine, and asparagine",
                        "Page 4 exclusion from supplement, not whole-medium removal.",
                        "PARTIAL",
                    )
                ],
            )
        for label in ("DL-serine", "DL-tyrosine"):
            p.mention(
                n,
                label,
                "Generic mixture description does not certify these local stereochemical forms. Named-mixture presence and per-member dose do not resolve identities.",
                ["IDENTITY_FORM"],
                stage="Tang2009 AA-S-18 member normalization",
            )
        p.dispose(
            n,
            "PARTIALLY_STRUCTURED",
            "Named mixture supported; exact negative membership and stereochemical uncertainties retained.",
        )
    for n in (361, 364, 367, 370):
        for label in ("10x Wolfe's vitamin solution", "10x mineral solution"):
            p.change(
                n,
                "ADD",
                label,
                "Pinchuk2010 modified-M1 source preparation; named stock input",
                [
                    ev(
                        "pinchuk",
                        "10 ml each of 10× Wolfe's vitamin solution and 10× mineral solution",
                        "Methods preparation input; no final volume supplied, so not mL/L. Named stocks are not a second addition of all flattened parent chemicals.",
                    )
                ],
                amount=amount(
                    "10",
                    "ML",
                    "Literal 10 mL of this 10x stock per source-described preparation; final volume unspecified.",
                ),
                notes="Source input only; correspondence to parent's flattened ingredients remains withheld.",
            )
        p.mention(
            n,
            "Wolfe vitamin/mineral stocks",
            "Named stocks and 10 mL inputs supported. Component forms and correspondence to flattened parent remain unresolved; no component double-counting or replacement authorized.",
            ["IDENTITY_FORM", "OPERATION"],
            stage="Pinchuk2010 source stocks versus flattened parent",
        )
        p.dispose(
            n,
            "PARTIALLY_STRUCTURED",
            "Named stock inputs separated from unresolved component equivalence.",
        )
    for n, key, value, unit, basis in (
        (130, "125", "5", "ML", "PER_BATCH"),
        (317, "125", "5", "ML", "PER_BATCH"),
        (142, "956", "0.5", "PERCENT", "UNSPECIFIED_PERCENT"),
        (313, "956", "0.5", "PERCENT", "UNSPECIFIED_PERCENT"),
        (144, "956", "0.3", "PERCENT", "UNSPECIFIED_PERCENT"),
        (315, "956", "0.3", "PERCENT", "UNSPECIFIED_PERCENT"),
    ):
        row, _, target, variant = p.target(n)
        matches = [
            (i, c)
            for i, c in enumerate(variant.get("ingredient_changes", []))
            if c["source_modification_index"] == int(row["modification_index"])
        ]
        if len(matches) != 1:
            raise ValueError("Expected one existing source event for amount promotion")
        index, old = matches[0]
        new = copy.deepcopy(old)
        if "amount" in old or "concentration" in old["ingredient"]:
            raise ValueError("Existing event already has structured quantity")
        statement = (
            "Literal 5 mL methanol input per DSMZ125 basal batch; no final volume or purity inferred."
            if key == "125"
            else "Literal final-medium percentage from DSMZ956; mass/volume, volume/volume and mass/mass basis unspecified."
        )
        new["amount"] = {"value": value, "unit": unit, "basis": basis, "basis_statement": statement}
        target.setdefault("replace_changes", []).append(
            {"change_index": index, "expected": copy.deepcopy(old), "replacement": new}
        )
        p.dispose(
            n,
            "STRUCTURED",
            "Existing event preserved; source-literal quantity promoted from notes to amount without denominator inference.",
        )


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue", type=Path, required=True)
    parser.add_argument("--coverage", type=Path, required=True)
    parser.add_argument("--prior-worktree", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.output.exists() or digest(args.queue.read_bytes()) != QUEUE_SHA:
        raise ValueError("Output must be new and original queue hash must match")
    csv.field_size_limit(16 * 1024 * 1024)
    with args.queue.open(newline="") as stream:
        rows = list(csv.DictReader(stream, delimiter="\t"))
    with args.coverage.open(newline="") as stream:
        coverage = {int(r["queue_row_number"]): r for r in csv.DictReader(stream, delimiter="\t")}
    p = Proposal(rows, coverage)
    prepare(p)
    expected = {n for n, r in coverage.items() if r["status"] == "HELD_MODEL"} | {
        130,
        317,
        142,
        313,
        144,
        315,
    }
    if set(p.dispositions) != expected or len(rows) != 396:
        raise ValueError("31 model-held and six quantity-promotion scope mismatch")
    inspections = []
    for key, (reference, path, expected_hash, locator) in CAPTURES.items():
        source = (
            ROOT / NEW / path[4:] if path.startswith("new:") else args.prior_worktree / OLD / path
        )
        if digest(source.read_bytes()) != expected_hash:
            raise ValueError("Inspected source drift: " + key)
        inspections.append(
            {
                "key": key,
                "reference": reference,
                "path": str(source.relative_to(ROOT)) if source.is_absolute() else str(source),
                "sha256": expected_hash,
                "locator": locator,
            }
        )
    payload = {
        "schema_version": 1,
        "base_commit": BASE,
        "source_queue_sha256": QUEUE_SHA,
        "scope": "31 model-held rows and six existing-event literal-amount upgrades; named gas/mixture stages separated, unresolved identity/operation dimensions held. No recipe applies.",
        "source_inspections": inspections,
        "browser_inspections": [
            {
                "reference": "DOI:10.1007/s10126-021-10037-4",
                "url": "https://link.springer.com/article/10.1007/s10126-021-10037-4",
                "locator": "Primary abstract only",
                "sha256": None,
            },
            {
                "reference": "doi:10.1099/ijs.0.012724-0",
                "url": "https://www.academia.edu/165327461/",
                "locator": "Primary paper page 2730",
                "sha256": None,
            },
        ],
        "records": sorted(p.records.values(), key=lambda r: r["path"]),
        "dispositions": [p.dispositions[n] for n in sorted(p.dispositions)],
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")
    print(
        json.dumps(
            {
                "path": str(args.output),
                "sha256": digest(args.output.read_bytes()),
                "records": len(payload["records"]),
                "rows": len(payload["dispositions"]),
                "statuses": dict(Counter(d["status"] for d in payload["dispositions"])),
                "append_changes": sum(d["append_assertion_count"] for d in payload["dispositions"]),
                "append_mentions": sum(d["append_mention_count"] for d in payload["dispositions"]),
                "replace_changes": 6,
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
