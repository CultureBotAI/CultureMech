#!/usr/bin/env python3
"""Prepare explicit residual-queue curation proposals for CultureMech #683.

2026-11-16. Input: verified planning inventory and source-bound decisions.
Output: private inspection summaries/proposals; never writes recipe YAML.
"""

from __future__ import annotations

import argparse
import copy
import difflib
import hashlib
import json
import re
import subprocess
import sys
import urllib.parse
import urllib.request
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
GROUPS = {"bacterial_remaining", "specialized_remaining"}

# These are explicit curator decisions after reading the cited source passages.
# They are not keyword extraction or a rule for unseen recipes.
SOURCES = {
    "spectrum": (
        "sources/2asw-spectrum-2023",
        "doi:10.1128/spectrum.00069-23",
        "Materials and Methods, Algal strains and cultivation conditions",
    ),
    "emami": (
        "sources/emami-2015",
        "doi:10.1038/srep10036",
        "Methods, culture conditions and bacterial interference experiment",
    ),
    "hiibel": (
        "remaining-sources/hiibel-2015",
        "doi:10.3389/fenrg.2015.00020",
        "Materials and Methods, Strains and media",
    ),
    "751": (
        "remaining-sources/dsmz-751",
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium751.pdf",
        "Page 1, liquid-medium instruction",
    ),
    "125": (
        "remaining-sources/dsmz-125",
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium125.pdf",
        "Page 1, preparation alternatives",
    ),
    "956": (
        "remaining-sources/dsmz-956",
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium956.pdf",
        "Page 1, final paragraph",
    ),
    "1021": (
        "remaining-sources/dsmz-1021",
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1021.pdf",
        "Page 1, Solution A hydrolysate alternatives",
    ),
    "829": (
        "remaining-sources/dsmz-829",
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium829.pdf",
        "Page 1, DSM 16661 and DSM 21157 prescription",
    ),
    "nbrc": (
        "remaining-sources/nbrc-1002",
        "https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1002",
        "Heterotrophic and autotrophic preparation alternatives",
    ),
    "blumer": (
        "remaining-sources/blumer-2010",
        "doi:10.1128/AEM.01400-10",
        "Materials and Methods, Bacterial strains and growth on sugar substrates",
    ),
    "teusink": (
        "remaining-sources/teusink-2005",
        "doi:10.1128/AEM.71.11.7253-7262.2005",
        "Table 1, concentration column and footnotes a-b",
    ),
    "wendisch": (
        "remaining-sources/wendisch-2000",
        "doi:10.1128/JB.182.11.3088-3096.2000",
        "Materials and Methods, cultivation conditions; separate Figure 1 caption",
    ),
    "kaminskyj": (
        "remaining-sources/kaminskyj-2001",
        "doi:10.4148/1941-4765.1175",
        "Page 26, Minimal Medium and 20 X Nitrate salts",
    ),
}
for _pmid in (10609610, 38194015, 12420179, 19826864, 15931519, 37088211, 35960254, 7520742):
    SOURCES[str(_pmid)] = (
        f"remaining-sources/abstract-{_pmid}",
        f"PMID:{_pmid}",
        "Primary article abstract indexed by Europe PMC; full methods not reviewed",
    )


def normalized(text: str) -> str:
    return " ".join(re.sub(r"<[^>]+>", "", text).split())


def source_context(key: str) -> dict:
    relative, reference, locator = SOURCES[key]
    directory = ROOT / ".temp/variant-683" / relative
    receipt = json.loads((directory / "receipt.json").read_text())
    source = next(directory.glob("source.*"))
    assert hashlib.sha256(source.read_bytes()).hexdigest() == receipt["sha256"]
    text = (directory / "inspection.txt").read_text()
    assert hashlib.sha256(text.encode()).hexdigest() == receipt["inspection_sha256"]
    return {
        "key": key,
        "path": str(source.relative_to(ROOT)),
        "reference": reference,
        "locator": locator,
        "sha256": receipt["sha256"],
        "url": receipt["url"],
        "accessed_at": receipt["retrieved_at"],
        "text": normalized(text),
    }


def prepare(inventory: dict, output: Path) -> None:
    rows = dict(assigned_rows(inventory))
    contexts = {key: source_context(key) for key in SOURCES}
    claims: dict[int, list[dict]] = {}
    decisions: dict[int, dict] = {}

    def disposition(numbers, status, reason):
        for number in numbers:
            assert number in rows and number not in decisions, number
            decisions[number] = {
                "queue_row_number": number,
                "status": status,
                "reason": reason,
                "assertion_count": 0,
            }

    def claim(
        number,
        action,
        label,
        source,
        quote,
        stage,
        value=None,
        unit=None,
        *,
        old=None,
        notes="",
        per_volume=None,
    ):
        row = rows[number]
        context = contexts[source]
        assert normalized(quote) in context["text"], (number, quote)
        ingredient = {"preferred_term": label}
        if value is not None:
            ingredient["concentration"] = {"value": value, "unit": unit}
            if per_volume:
                ingredient["concentration"]["per_volume"] = per_volume
        if notes:
            ingredient["notes"] = notes
        event = {
            "action": action,
            "ingredient": ingredient,
            "stage": stage,
            "source_modification_index": int(row["modification_index"]),
            "source_text": row["modification_text"],
            "evidence": [
                {
                    "reference": context["reference"],
                    "supports": "SUPPORT",
                    "snippet": quote,
                    "explanation": f"{context['locator']}. Supports only the named descriptor/event at the stated stage. {notes} Source inspected 2026-11-16; SHA256 {context['sha256']}. No parent formulation, growth, ontology identity, or missing dose is inferred.",
                }
            ],
        }
        if old:
            event["replaced_ingredient"] = {"preferred_term": old}
        claims.setdefault(number, []).append(event)

    claim(
        118,
        "SET_CONCENTRATION",
        "sodium chloride",
        "spectrum",
        "1.5 M NaCl",
        "reported 2ASW culture medium",
        "1.5",
        "MOLAR",
        notes="Reported medium concentration, not stock or amount added; complete basal formula remains unresolved.",
    )
    claim(
        120,
        "REPLACE",
        "sea salts",
        "hiibel",
        "33.6 g/L of sea salts",
        "modified 2ASW maintenance medium",
        "33.6",
        "G_PER_L",
        old="sodium chloride",
        notes="Undefined sea-salt mixture; no brand, constituent list or pure-NaCl equivalence inferred.",
    )
    claim(
        129,
        "ADD",
        "yeast extract",
        "38194015",
        "5 g/L yeast extract",
        "pH 6.5 MRS enrichment",
        "5",
        "G_PER_L",
        notes="Source-reported enrichment amount; do not calculate total yeast extract including basal MRS. Abstract evidence only.",
    )
    for number in (130, 317):
        claim(
            number,
            "ADD",
            "methanol",
            "125",
            "Add 5 ml methanol",
            "methanol preparation alternative",
            notes="Literal source dose: 5 mL per common basal batch. Final volume and purity unspecified. This alternative excludes methane-air incubation; no mL/L or percent conversion.",
        )
    for number in (136, 385):
        claim(
            number,
            "REMOVE",
            "corn meal agar",
            "751",
            "omit corn meal agar",
            "liquid SC preparation",
            notes="Removal of the named corn-meal-agar mixture; not positive ingredient presence. Phosphate batch changes remain separately held under issue 760.",
        )
    claim(
        140,
        "SET_CONCENTRATION",
        "sodium chloride",
        "7520742",
        "100 g of NaCl per liter",
        "reported isolation medium",
        "100",
        "G_PER_L",
        notes="The primary abstract states this medium concentration; it does not establish complete identity with the imported parent or certify growth at every salt level.",
    )
    for number in (142, 313):
        claim(
            number,
            "ADD",
            "methanol",
            "956",
            "final concentration of 0.5%",
            "post-sterilization methanol alternative",
            notes="Literal final-medium quantity: 0.5%, percentage basis unspecified. Not combined with methylamine; no w/v, w/w or v/v basis inferred.",
        )
    for number in (144, 315):
        claim(
            number,
            "ADD",
            "methylamine",
            "956",
            "final concentration of 0.3%",
            "post-sterilization methylamine alternative",
            notes="Literal final-medium quantity: 0.3%, percentage basis unspecified. Salt, hydration and purity unspecified; not combined with methanol.",
        )
    claim(
        188,
        "ADD",
        "iron(II) sulfate heptahydrate",
        "nbrc",
        "10 mg/l of FeSO4·7H2O",
        "heterotrophic medium preparation",
        "10",
        "MG_PER_L",
    )
    claim(
        189,
        "ADD",
        "yeast extract",
        "nbrc",
        "0.25 g/l",
        "heterotrophic post-autoclave sterile-stock addition",
        "0.25",
        "G_PER_L",
        notes="Final-medium concentration stated directly; stock concentration and dose not inferred.",
    )
    claim(
        190,
        "ADD",
        "iron(II) sulfate heptahydrate",
        "nbrc",
        "13.9 g/l of FeSO4·7H2O",
        "autotrophic medium preparation",
        "13.9",
        "G_PER_L",
    )
    claim(
        191,
        "ADD",
        "sulfuric acid",
        "nbrc",
        "pH to 1.7 with H2SO4",
        "autotrophic pH adjustment before autoclaving",
        notes="Titrant identity only; pH 1.7 is a target, not an acid dose. Strength and amount unspecified.",
    )
    claim(
        196,
        "ADD",
        "fetal bovine serum",
        "10609610",
        "10% fetal bovine serum",
        "Brucella-broth supplementation",
        notes="Primary abstract reports 10% serum; percentage basis unspecified and not inferred. Undefined mixture, no constituent identities expanded.",
    )
    claim(
        197,
        "ADD",
        "hydrogen peroxide",
        "10609610",
        "3.5 mM",
        "reported peroxide exposure arm",
        "3.5",
        "MILLIMOLAR",
        notes="One explicitly reported exposure level, not a recommended growth formulation or complete dose-response representation. Primary abstract only.",
    )
    claim(
        200,
        "ADD",
        "aluminum sulfate",
        "12420179",
        "300 mM aluminum sulfate",
        "reported 300 mM stress exposure",
        "300",
        "MILLIMOLAR",
        notes="Al2(SO4)3 identity as stated; hydration unspecified. Distinct from the 1 mM and 50 mM precultivation treatments; no whole-parent equivalence inferred.",
    )
    claim(
        202,
        "REPLACE",
        "hydrochloric acid",
        "emami",
        "pH 1.5 using hydrochloric acid",
        "AJS pH adjustment",
        old="sulfuric acid",
        notes="Replaces the canonical acidification instruction only. Strength and dose are unspecified; pH is not a concentration.",
    )
    for label, quote in (
        ("Trypticase", "Trypticase"),
        ("cysteine hydrochloride", "cysteine-HCl"),
        ("resazurin", "resazurin were not added"),
    ):
        claim(
            257,
            "REMOVE",
            label,
            "blumer",
            quote,
            "modified DSMZ 640 preparation",
            notes="Source explicitly omits this component. Cysteine-HCl hydration is unspecified; no mapped identity asserted.",
        )
    claim(
        258,
        "ADD",
        "sodium sulfide nonahydrate",
        "blumer",
        "Na2S·9H2O",
        "modified DSMZ 640 reducing-agent addition",
        notes="Source describes 10% [wt/vol] Na2S·9H2O stock added to a final concentration of 0.5%. Final percentage basis is not independently specified; do not substitute stock strength or infer a conversion. Carbon-source alternatives remain unexpanded.",
    )
    for number in (267, 339):
        claim(
            number,
            "SET_CONCENTRATION",
            "calcium D-pantothenate",
            "teusink",
            "Ca-(d)-(+)-pantothenate",
            "reported Table 1 medium composition",
            "0.001",
            "G_PER_L",
            notes="Direct Table 1 mass concentration, no molar conversion. The source's complete/minimal subset boundary remains as stated in the variant; other amounts are not certified.",
        )
    claim(
        340,
        "SET_CONCENTRATION",
        "D-biotin",
        "teusink",
        "d-Biotin",
        "reported Table 1 minimal-medium composition",
        "0.0025",
        "G_PER_L",
        notes="Direct Table 1 mass value; boldface minimal-subset membership verified in original HTML, not inferred from flattened text.",
    )
    for number in (269, 270):
        claim(
            number,
            "REPLACE",
            "sodium [1-13C]acetate",
            "wendisch",
            "10 g/liter",
            "13C-labeling experiment medium",
            "10",
            "G_PER_L",
            old="acetate",
            notes="Preserve sodium counterion and isotope position; no unspecified parent acetate identity or hydrate is equated. Table 2 nominal molarity is not a conversion.",
        )
    claim(
        270,
        "SET_CONCENTRATION",
        "unlabeled glucose",
        "wendisch",
        "10 g/liter each",
        "mixed-substrate 13C-labeling experiment medium",
        "10",
        "G_PER_L",
        notes="Glucose remains unlabeled in the acetate-labeling arm. Keep mass dose separate from Table 2 nominal 55 mM.",
    )
    claim(
        271,
        "SET_CONCENTRATION",
        "glucose",
        "wendisch",
        "35 mM glucose",
        "Figure 1 growth time-course medium",
        "35",
        "MILLIMOLAR",
        notes="Separate from isotope-labeling/Table 2 arm. The stated 120 mM acetate remains context, not a newly quantified substitution.",
    )
    claim(
        272,
        "REPLACE",
        "D-[5-13C]glucose",
        "wendisch",
        "20 g/liter",
        "glucose 13C-labeling experiment medium",
        "20",
        "G_PER_L",
        old="D-glucose",
        notes="Preserve the isotope position; Table 2 nominal 110 mM is not a curator conversion. Enrichment discrepancy elsewhere in the source remains unresolved.",
    )
    claim(
        279,
        "REMOVE",
        "growth-stimulating factors",
        "829",
        "Omit growth-stimulating factors",
        "DSM 16661 and DSM 21157 preparation",
        notes="Named stock mixture is removed, without expanding individual constituents. Separate 2-bar H2/CO2 headspace condition is not a liquid ingredient concentration.",
    )
    claim(
        280,
        "ADD",
        "silicate",
        "emami",
        "1.06 × 10−4 M silicate",
        "reported f/2 supplementation",
        "1.06e-4",
        "MOLAR",
        notes="Undefined silicate chemical form; no salt/hydrate/stock assigned. Stated supplement dose, not calculated total including basal silicate.",
    )
    claim(
        282,
        "ADD",
        "sodium nitrate",
        "emami",
        "29.4 mM NaNO3",
        "reported f/2 supplementation",
        "29.4",
        "MILLIMOLAR",
        notes="Stated supplement concentration; inclusion of basal nitrate is unresolved. pH 8 remains a condition.",
    )
    claim(
        284,
        "ADD",
        "penicillin G",
        "emami",
        "penicillin G",
        "antibiotic-treated f/2 culture",
        "200",
        "MICROG_PER_ML",
        notes="Source-literal 200 micrograms/mL, no conversion. No salt form or stock strength inferred; untreated comparator separate.",
    )
    claim(
        285,
        "ADD",
        "dihydrostreptomycin sulfate",
        "emami",
        "dihydrostreptomycin sulphate",
        "antibiotic-treated f/2 culture",
        "50",
        "MICROG_PER_ML",
        notes="Source-literal 50 micrograms/mL, no conversion. Not streptomycin; hydrate and stock strength unspecified.",
    )
    claim(
        287,
        "REPLACE",
        "2ASW vitamin solution",
        "hiibel",
        "vitamin solution from the 2ASW medium",
        "modified f/2 maintenance medium",
        old="f/2 vitamin solution",
        notes="Named mixture replacement only. Constituent identities, stock strength, addition volume and final concentrations remain unresolved; no reliance on the mismatched Gomord citation.",
    )
    claim(
        307,
        "REPLACE",
        "magnesium sulfate, anhydrous",
        "kaminskyj",
        "5.2 g if anhydrous",
        "20X nitrate stock preparation",
        "5.2",
        "G_PER_L",
        old="magnesium sulfate heptahydrate",
        per_volume="per liter of 20X nitrate stock, not final medium",
        notes="Source explicitly makes stock to 1 liter. Replaces 10.4 g/L heptahydrate in stock. The stock addition stays 50 mL/L; no final-medium conversion asserted.",
    )
    claim(
        308,
        "ADD",
        "agar",
        "kaminskyj",
        "add 18 g agar",
        "solid minimal-medium preparation before autoclaving",
        notes="Literal dose: 18 g added to the one-litre MM preparation. No separately established post-agar final volume or g/L value asserted; not the CM 15-g option.",
    )
    claim(
        310,
        "ADD",
        "Cr(VI)",
        "37088211",
        "10 mg",
        "reported B17316 Cr(VI) exposure",
        "10",
        "MG_PER_L",
        notes="Source-reported Cr(VI) mass concentration; administered chromate salt/counterion/hydration unspecified. Do not convert to mass of an assumed salt. Abstract evidence only.",
    )
    claim(
        383,
        "ADD",
        "L-phenylalanine",
        "19826864",
        "L-phenylalanine",
        "reported sole-nitrogen phototrophic formulation",
        notes="Ingredient identity and sole-nitrogen role only; dose and identities of any displaced basal nitrogen compounds are unresolved. No base-recipe materialization or inferred removals.",
    )
    claim(
        390,
        "REPLACE",
        "casein hydrolysate",
        "1021",
        "Casein hydrolysate",
        "Solution A batch preparation",
        old="lactalbumin hydrolysate",
        notes="Literal batch substitution: 8.10 g casein hydrolysate for 8.10 g lactalbumin hydrolysate, not both. Undefined hydrolysate mixture; serum addition and final volume not converted.",
    )
    claim(
        391,
        "REMOVE",
        "dextrose",
        "15931519",
        "tryptic soy broth without dextrose",
        "TSBWD basal preparation",
        notes="Explicit glucose/dextrose omission. No positive-presence descriptor is emitted for the removed ingredient.",
    )
    for label, stage in (
        ("soluble starch", "soluble-starch substrate arm"),
        ("maltose", "maltose substrate arm"),
    ):
        claim(
            392,
            "ADD",
            label,
            "15931519",
            label,
            stage,
            "0.5; 1.0",
            "PERCENT_W_V",
            notes="Two separate tested doses and mutually exclusive starch/maltose substrate arms, not simultaneous supplementation. Primary abstract explicitly states w/v; no full parent formulation certification.",
        )

    conditions = [
        122,
        125,
        126,
        127,
        128,
        131,
        132,
        133,
        135,
        139,
        141,
        143,
        145,
        195,
        198,
        199,
        201,
        203,
        228,
        230,
        231,
        232,
        233,
        234,
        235,
        236,
        259,
        265,
        266,
        274,
        276,
        277,
        278,
        281,
        283,
        286,
        288,
        289,
        304,
        305,
        306,
        309,
        311,
        314,
        316,
        318,
        319,
        320,
        380,
        381,
        382,
        384,
        388,
        393,
        394,
        396,
    ]
    disposition(
        conditions,
        "CONDITION_ONLY",
        "This row supplies organism, incubation, preparation, comparator, role or explicit uncertainty context rather than a new quantified ingredient change. Preserve the original prose; no gas-to-liquid concentration, base expansion, or new growth claim. Condition correctness is not independently certified by this disposition.",
    )
    # More precise context for rows that contain ingredient words without new events.
    for number in (304, 305):
        decisions[number][
            "reason"
        ] = "Primary abstract confirms acetate donor / fumarate acceptor roles, but this row states no addition, removal, replacement or changed quantity relative to the maintained formulation. Retain role context without inventing an ADD event."
    disposition(
        [119, 121],
        "HELD_EVIDENCE",
        "The row explicitly leaves basal formulation/brand/stock details unresolved. No additional ingredient identities or quantities can be inferred from it; the distinct supported source claim is proposed separately.",
    )
    disposition(
        [123, 312, 389],
        "HELD_EVIDENCE",
        "DSMZ 1021 specifies liquid-medium filtration but does not explicitly quantify or name an agar-change operation. No zero-agar amount or omission is invented.",
    )
    disposition(
        [124, 395],
        "HELD_EVIDENCE",
        "Only a named modified medium is specified; no explicit ingredient identity or dose occurs in this row. Primary formulation details require additional source inspection before decomposition.",
    )
    disposition(
        [134],
        "HELD_EVIDENCE",
        "Blood-species replacement and 50 g/L claim require independent reconciliation of DSMZ 693, the cited BacDive strain and the horse-blood parent; those primary recipe details were not reverified in this pass.",
    )
    disposition(
        [137, 138, 386, 387],
        "HELD_MODEL",
        "DSMZ 751 directly supports a changed phosphate mass per batch, not a demonstrated final concentration. SET_CONCENTRATION requires a valid concentration unit; absolute batch mass is not represented. Preserve original grams and hold under issue 760.",
    )
    disposition(
        [192, 193],
        "HELD_EVIDENCE",
        "The cited JCM/DSMZ recipe or ME19128 primary methods have not been independently inspected in this pass. Do not promote existing prose alone to a new evidence-backed descriptor.",
    )
    disposition(
        [194],
        "HELD_MODEL",
        "Methane versus methanol and calcium versus rare-earth chloride alternatives require arm-specific component identities and stage/dose evidence. A single combined ADD would falsely imply co-presence; preserve prose pending explicit alternatives.",
    )
    disposition(
        [218],
        "HELD_MODEL",
        "Half-strength whole-medium dilution is not an ingredient-specific change. No automatic expansion or multiplication of the parent recipe is authorized; retain the water/dilution formulation statement.",
    )
    disposition(
        [219],
        "HELD_EVIDENCE",
        "Assay-specific peptone and yeast-extract omissions require the cited primary methods; routine MB1/2 and carbon-assay formulations must stay separate. Source not reverified here.",
    )
    disposition(
        [227, 229],
        "HELD_EVIDENCE",
        "The Becking source's omission and full mass-basis recipe context were not independently reverified. Do not convert the parent/prose into new supported changes.",
    )
    disposition(
        [260, 261, 262, 263, 264],
        "HELD_EVIDENCE",
        "Shang 2013 primary formulation and separate substrate arms have not been independently inspected. Retain all listed forms, stock additions and preparation context without certifying them from local prose alone.",
    )
    disposition(
        [268, 341],
        "HELD_MODEL",
        "This row refers to a complete Table 1 formulation/subset and footnote components rather than enumerated changes. The bounded source review verifies specific vitamin doses separately; whole-table expansion and reconciliation of every imported chemical form remain out of scope.",
    )
    disposition(
        [273],
        "HELD_EVIDENCE",
        "The cited primary ATCC-1490 study was not independently inspected for explicit formate/fumarate omission; a named basal medium alone is insufficient to infer component absence.",
    )
    disposition(
        [275],
        "HELD_EVIDENCE",
        "The carbonate/CO2 buffering claim lacks a verified explicit carbonate species and dose; cited primary methods not reverified. Do not guess bicarbonate or add a gas as a liquid ingredient.",
    )
    for number, events in claims.items():
        assert number not in decisions
        decisions[number] = {
            "queue_row_number": number,
            "status": "STRUCTURED",
            "reason": "Explicit source-supported descriptor event(s) proposed; stage, exact existing source text and source evidence retained. Base recipe and unrelated claims are not certified.",
            "assertion_count": len(events),
        }
    for number in (130, 142, 144, 196, 258, 279, 287, 308, 313, 315, 317, 383, 390):
        decisions[number]["reason"] += (
            " PARTIAL: "
            + {
                130: "5 mL batch amount remains literal notes because no absolute-volume field exists.",
                142: "0.5% remains literal notes; percentage basis unspecified.",
                144: "0.3% remains literal notes; percentage basis unspecified.",
                196: "10% serum remains literal notes; percentage basis unspecified.",
                258: "Only sodium sulfide nonahydrate addition is represented, with stock/final percentage preserved in notes. Unspecified carbon-source increase and substrate alternatives remain unexpanded.",
                279: "Only the named stock removal is structured; 2-bar gas-mixture pressure remains prose context.",
                287: "Only named mixture replacement is structured; composition and dose remain unresolved.",
                308: "18-g preparation amount remains literal notes; no assumed post-addition final concentration.",
                313: "0.5% remains literal notes; percentage basis unspecified.",
                315: "0.3% remains literal notes; percentage basis unspecified.",
                317: "5 mL batch amount remains literal notes because no absolute-volume field exists.",
                383: "Only L-phenylalanine identity/role is represented; any displaced nitrogen ingredients and dose are unresolved.",
                390: "8.10-g batch amounts remain literal notes, with no final-volume conversion.",
            }[number]
        )
    assert set(decisions) == set(rows), sorted(set(rows) - set(decisions))
    records = {}
    for number, events in claims.items():
        row = rows[number]
        path = "data/normalized_yaml/" + row["source_path"]
        actual = (ROOT / path).read_bytes()
        assert hashlib.sha256(actual).hexdigest() == row["source_sha256"], path
        record = yaml.safe_load(actual)
        index = int(row["variant_index"])
        assert record["id"] == row["recipe_id"]
        assert record["variants"][index] == json.loads(row["variant_json"])
        target = records.setdefault(
            path,
            {
                "path": path,
                "recipe_id": row["recipe_id"],
                "expected_sha256": row["source_sha256"],
                "variants": {},
            },
        )
        variant = target["variants"].setdefault(
            index,
            {"variant_index": index, "variant_name": row["variant_name"], "ingredient_changes": []},
        )
        variant["ingredient_changes"].extend(copy.deepcopy(events))
    for record in records.values():
        record["variants"] = list(record["variants"].values())
    output.mkdir(parents=True, exist_ok=False)
    document = {
        "schema_version": 1,
        "issue": "https://github.com/CultureBotAI/CultureMech/issues/683",
        "scope": "Explicit bacterial_remaining and specialized_remaining decisions; partial source coverage, no recipe application",
        "source_inspections": [
            {k: v for k, v in item.items() if k != "text"} for item in contexts.values()
        ],
        "records": list(records.values()),
    }
    (output / "proposals.json").write_text(
        json.dumps(document, ensure_ascii=False, indent=2) + "\n"
    )
    (output / "dispositions.json").write_text(
        json.dumps(
            {
                "schema_version": 1,
                "assigned_rows": 126,
                "dispositions": [decisions[n] for n in sorted(decisions)],
            },
            ensure_ascii=False,
            indent=2,
        )
        + "\n"
    )
    targets = []
    for path in sorted({row["source_path"] for row in rows.values()}):
        selected = [(n, row) for n, row in rows.items() if row["source_path"] == path]
        first = selected[0][1]
        targets.append(
            {
                "target_id": first["recipe_id"],
                "path": "data/normalized_yaml/" + path,
                "label": path,
                "kind": "maintained",
                "selector": "Variant modification queue rows "
                + ", ".join(str(n) for n, _ in selected),
                "owner_paths": [
                    {
                        "repository": "CultureBotAI/CultureMech",
                        "path": "data/normalized_yaml/" + path,
                        "role": "authoritative normalized recipe",
                    }
                ],
            }
        )
    (output / "targets.yaml").write_text(yaml.safe_dump({"targets": targets}, sort_keys=False))
    counts = {
        status: sum(d["status"] == status for d in decisions.values())
        for status in sorted({d["status"] for d in decisions.values()})
    }
    print(
        json.dumps(
            {
                "output": str(output),
                "rows": len(decisions),
                "targets": len(targets),
                "proposed_records": len(records),
                "assertions": sum(map(len, claims.values())),
                "statuses": counts,
            },
            indent=2,
        )
    )


def validate_proposals(directory: Path) -> None:
    from culturemech.validation.write_validated import validate_recipe

    document = json.loads((directory / "proposals.json").read_text())
    observations = []
    for decision in document["records"]:
        raw = (ROOT / decision["path"]).read_bytes()
        assert hashlib.sha256(raw).hexdigest() == decision["expected_sha256"]
        record = yaml.safe_load(raw)
        baseline = yaml.safe_dump(
            record, sort_keys=False, allow_unicode=True, default_flow_style=False, width=80
        ).encode()
        for variant in decision["variants"]:
            destination = record["variants"][variant["variant_index"]]
            assert destination["name"] == variant["variant_name"] and not destination.get(
                "ingredient_changes"
            )
            destination["ingredient_changes"] = variant["ingredient_changes"]
        errors = validate_recipe(record)
        observations.append(
            {
                "path": decision["path"],
                "recipe_id": decision["recipe_id"],
                "errors": [error.message for error in errors],
                "native_presentation_unchanged": baseline == raw,
            }
        )
    result = {
        "records": observations,
        "schema_semantic_errors": sum(len(row["errors"]) for row in observations),
        "presentation_blocked": sum(
            not row["native_presentation_unchanged"] for row in observations
        ),
    }
    destination = directory / "validation.json"
    with destination.open("x") as stream:
        json.dump(result, stream, indent=2)
        stream.write("\n")
    print(json.dumps({key: value for key, value in result.items() if key != "records"}, indent=2))


def draft_review(directory: Path, inventory: dict) -> None:
    """Persist the curator's bounded judgments using native provenance inspection."""
    directory = directory.resolve()
    relative = str(directory.relative_to(ROOT))
    proposal = json.loads((directory / "proposals.json").read_text())
    dispositions = json.loads((directory / "dispositions.json").read_text())["dispositions"]
    validation = json.loads((directory / "validation.json").read_text())
    assert validation["schema_semantic_errors"] == 0
    contexts = proposal["source_inspections"]
    inputs = [
        relative + "/proposals.json",
        relative + "/dispositions.json",
        relative + "/validation.json",
        "src/culturemech/schema/culturemech.yaml",
    ] + [item["path"] for item in contexts]
    command = [
        sys.executable,
        "scripts/record_review.py",
        "inspect",
        "--targets",
        relative + "/targets.yaml",
    ]
    for path in inputs:
        command += ["--input", path]
    inspection = subprocess.run(command, cwd=ROOT, check=True, capture_output=True, text=True)
    (directory / "inspection.json").write_text(inspection.stdout)
    inspected = json.loads(inspection.stdout)
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rows = dict(assigned_rows(inventory))
    ids = [target["target_id"] for target in inspected["targets"]]
    evidence = [
        {
            "evidence_id": "queue",
            "kind": "record_content",
            "reference": relative + "/dispositions.json",
            "locator": "All 126 assigned queue rows; exact target selectors in targets.yaml",
            "accessed_at": now,
            "support": "context_only",
            "summary": "Every assigned row was read and classified. Condition-only classification is not external verification of those conditions; held claims remain unresolved.",
            "snapshot_sha256": hashlib.sha256(
                (directory / "dispositions.json").read_bytes()
            ).hexdigest(),
        },
        {
            "evidence_id": "proposal",
            "kind": "record_content",
            "reference": relative + "/proposals.json",
            "locator": "All 46 proposed events in 26 records",
            "accessed_at": now,
            "support": "supports",
            "summary": "Explicit curator decisions retain source coordinates, stage, evidence, original prose, and uncertainty; no recipe applied.",
            "snapshot_sha256": hashlib.sha256(
                (directory / "proposals.json").read_bytes()
            ).hexdigest(),
        },
        {
            "evidence_id": "validation",
            "kind": "validation",
            "reference": relative + "/validation.json",
            "locator": "26 proposed records, zero schema/semantic errors; nine presentation blockers",
            "accessed_at": now,
            "support": "supports",
            "summary": "Native validate_recipe accepted every proposed record. Separate byte comparison found nine files that the native writer would reformat, so a schema pass is not application permission.",
            "snapshot_sha256": hashlib.sha256(
                (directory / "validation.json").read_bytes()
            ).hexdigest(),
        },
    ]
    source_ids = {}
    for context in contexts:
        evidence_id = "source-" + context["key"]
        source_ids[context["reference"]] = evidence_id
        evidence.append(
            {
                "evidence_id": evidence_id,
                "kind": "primary_source",
                "reference": context["reference"],
                "locator": context["locator"],
                "accessed_at": context["accessed_at"].replace("+00:00", "Z"),
                "support": "supports",
                "summary": "Inspected the source passage used in the proposal; scope and quantity limits are retained separately for each event. Indexed abstracts are identified explicitly and do not establish unprinted methods.",
                "snapshot_sha256": context["sha256"],
            }
        )
    assertions = {}
    for record in proposal["records"]:
        for variant in record["variants"]:
            for event in variant["ingredient_changes"]:
                coordinate = (
                    record["recipe_id"],
                    variant["variant_index"],
                    event["source_modification_index"],
                )
                assertions.setdefault(coordinate, []).append(event)
    assessments = []
    for item in dispositions:
        row = rows[item["queue_row_number"]]
        coordinate = (row["recipe_id"], int(row["variant_index"]), int(row["modification_index"]))
        events = assertions.get(coordinate, [])
        assert len(events) == item["assertion_count"]
        evidence_ids = ["queue"]
        if events:
            evidence_ids += ["proposal"] + sorted(
                {source_ids[event["evidence"][0]["reference"]] for event in events}
            )
        assessments.append(
            {
                "assessment_id": "queue-row-" + str(item["queue_row_number"]),
                "area": "scope" if item["status"] == "CONDITION_ONLY" else "quantity",
                "topic": f"variants[{row['variant_index']}].modifications[{row['modification_index']}] — {item['status']}",
                "outcome": (
                    "supported"
                    if events
                    else ("not_applicable" if item["status"] == "CONDITION_ONLY" else "unknown")
                ),
                "summary": item["reason"],
                "target_ids": [row["recipe_id"]],
                "evidence_ids": evidence_ids,
                "details": row["modification_text"],
                "dimensions": [
                    {
                        "name": "queue_disposition",
                        "value": item["status"],
                        "definition": "Classification of the exact supplied modification row; STRUCTURED describes a proposal, not applied or released data.",
                        "evidence_ids": ["queue"],
                    },
                    {
                        "name": "proposed_assertion_count",
                        "value": str(item["assertion_count"]),
                        "definition": "Number of explicit descriptor-change events proposed for this row, before application or downstream identity resolution.",
                        "evidence_ids": evidence_ids,
                    },
                ],
            }
        )
    quantity_ids = sorted(
        {rows[n]["recipe_id"] for n in (130, 137, 138, 142, 144, 313, 315, 317, 386, 387)}
    )
    review = {
        "schema_version": "1.0.0",
        "review_id": stamp + "-variant-683-remaining-claims-preapply",
        "kind": "batch",
        "repository": inspected["repository"],
        "title": "Bacterial and specialized residual variant ingredient claims: bounded pre-application review",
        "started_at": "2026-11-16T21:13:00Z",
        "finished_at": now,
        "reviewer": {
            "identity": "codex",
            "kind": "agent",
            "independence": "self_review",
            "independence_basis": "The curator authored these explicit proposals and reviewed their primary-source basis; independent owner review and native application are still required.",
        },
        "skill": "curate-yaml-record; review-ingredient-concentrations",
        "completion": "partial",
        "verdict": "needs_curation",
        "scientific_review": True,
        "summary": "All 126 assigned rows across 41 recipes were triaged. Primary-source inspection supports 46 proposed events on 42 rows in 26 recipes; 56 rows are condition/context only, 20 are held for evidence and eight for representation. Several structured rows are explicitly partial. All 26 proposed records validate; nine presentation blockers prevent unreviewed application. No recipes changed and no whole-record, growth, MIM mapping or release certification.",
        "source": inspected["source"],
        "scope": {
            "description": "Exact bacterial_remaining (122) and specialized_remaining (4) queue rows; scientific assessment is limited to the proposed descriptor events and explicitly inspected primary passages.",
            "selection": "The planning inventory's two named groups, with each assigned queue row represented exactly once in dispositions and assessments.",
            "coverage": "partial",
            "population_size": 396,
            "reviewed_target_ids": ids,
            "exclusions": [
                {
                    "target": "Other 270 variant queue rows",
                    "reason": "Assigned to other source-family curators.",
                },
                {
                    "target": "Whole canonical recipes, growth/taxonomy assertions, inferred base application, expanded referenced stocks, and literature completeness",
                    "reason": "Not scientifically recertified by a bounded variant-claim pass.",
                },
                {
                    "target": "Unverified primary methods for held rows and condition correctness",
                    "reason": "Retain explicit held/context dispositions; classification does not certify existing source prose.",
                },
            ],
        },
        "targets": inspected["targets"],
        "checks": [
            {
                "check_id": "native-inspect",
                "name": "Native input-byte inspection",
                "status": "passed",
                "required": True,
                "summary": "Native inspector bound 41 target preimages, explicit proposals, dispositions, validation observations, schema and inspected source snapshots.",
                "target_ids": ids,
                "command": ".venv/bin/python scripts/adhoc/curate_variant_remaining_683.py --draft-review "
                + relative,
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": ["queue", "proposal"],
            },
            {
                "check_id": "native-proposals",
                "name": "Native proposed-record schema and semantic validation",
                "status": "passed",
                "required": True,
                "summary": "26 modified in-memory records passed validate_recipe with zero errors; no recipe YAML was written.",
                "target_ids": [record["recipe_id"] for record in proposal["records"]],
                "command": "env PYTHONPATH=src .venv/bin/python scripts/adhoc/curate_variant_remaining_683.py --validate-proposals "
                + relative,
                "exit_code": 0,
                "expected_exit_code": 0,
                "evidence_ids": ["validation"],
            },
            {
                "check_id": "application",
                "name": "Authoritative application and export acceptance",
                "status": "not_applicable",
                "required": False,
                "summary": "No application performed. Earlier all-record preview refused on existing KOMODO_125 presentation drift before any authoritative write; nine such records were enumerated separately.",
                "target_ids": ids,
                "evidence_ids": ["validation"],
            },
        ],
        "evidence": evidence,
        "assessments": assessments,
        "findings": [
            {
                "finding_id": "quantity-basis-gap",
                "issue_key": "variant-absolute-quantity-unspecified-percent-760",
                "category": "representation",
                "severity": "major",
                "status": "open",
                "certainty": "confirmed",
                "title": "Literal batch quantities and unspecified percentage bases lack a faithful structured representation",
                "description": "DSMZ 751 batch phosphate changes cannot truthfully satisfy SET_CONCENTRATION using g/L; DSMZ 125 methanol batch volume and DSMZ 956 unspecified-basis percentages remain literal notes. No false concentration basis was introduced. See issue 760 for the reusable model gap.",
                "target_ids": quantity_ids,
                "field_paths": ["variants[].ingredient_changes[].ingredient.concentration"],
                "evidence_ids": ["source-751", "source-125", "source-956", "proposal", "queue"],
                "owner_paths": [
                    {
                        "repository": inspected["repository"],
                        "path": "src/culturemech/schema/culturemech.yaml",
                        "role": "quantity model owner",
                    }
                ],
                "external_issues": ["https://github.com/CultureBotAI/CultureMech/issues/760"],
            }
        ],
        "actions": [
            {
                "action_id": "review-then-apply",
                "description": "Independently review proposed claims, resolve presentation boundaries, then centrally apply only approved records and verify exported event/ledger counts.",
                "finding_ids": [],
                "target_ids": ids,
                "ownership_note": "Normalized recipe owners and the #683 application owner; this curator has not applied data.",
                "acceptance_checks": [
                    "Exact primary-source/coordinate review",
                    "No unsupported quantity basis or inferred base composition",
                    "Native guarded application receipts and export verification",
                    "All 126 dispositions preserved including partial and held rows",
                ],
            }
        ],
        "limitations": [
            "This is partial scientific coverage of a 126-row assigned cohort, not completion of all catalog chemistry or curation.",
            "Condition-only rows are classified from their exact prose; conditions, taxa and growth are not newly certified.",
            "Primary indexed abstracts support only their explicit claims; full methods were not inspected for those sources.",
            "Nine source files fail the native writer's no-reformat guard; a schema-valid proposal is not an applied record.",
            "No new ontology IDs, solvent density, hydrate conversion, missing percentage basis, total basal concentrations, or automatic variant materialization is asserted.",
            "Source receipts and native review inputs are working-tree byte attestations, not external authentication or an integrated MIM/KGM release.",
        ],
        "links": [
            "https://github.com/CultureBotAI/CultureMech/issues/683",
            "https://github.com/CultureBotAI/CultureMech/issues/760",
        ],
    }
    content_name = "review-content-" + stamp + ".yaml"
    with (directory / content_name).open("x") as stream:
        # The native immutable-review contract prohibits YAML aliases.
        yaml.safe_dump(json.loads(json.dumps(review)), stream, sort_keys=False, allow_unicode=True)
    print(
        json.dumps(
            {"review_content": relative + "/" + content_name, "review_id": review["review_id"]}
        )
    )


def presentation_audit(output: Path) -> None:
    output = output.resolve()
    validation = json.loads(
        (ROOT / ".temp/variant-683/remaining-proposal-v2/validation.json").read_text()
    )
    extra = json.loads(
        (ROOT / "conf/variant_ingredient_curation/remaining-families-683.json").read_text()
    )
    paths = sorted(
        {row["path"] for row in validation["records"] if not row["native_presentation_unchanged"]}
        | {row["path"] for row in extra["records"]}
    )
    output.mkdir(parents=True, exist_ok=False)
    observations = []

    def ordered_nodes(node):
        if isinstance(node, yaml.ScalarNode):
            return ("scalar", node.tag, node.value)
        if isinstance(node, yaml.SequenceNode):
            return ("sequence", node.tag, tuple(ordered_nodes(item) for item in node.value))
        return (
            "mapping",
            node.tag,
            tuple((ordered_nodes(key), ordered_nodes(value)) for key, value in node.value),
        )

    for path in paths:
        before = (ROOT / path).read_bytes()
        document = yaml.safe_load(before)
        after = yaml.safe_dump(
            document, sort_keys=False, allow_unicode=True, default_flow_style=False, width=80
        ).encode()
        assert yaml.safe_load(after) == document
        assert ordered_nodes(yaml.compose(before)) == ordered_nodes(yaml.compose(after))
        diff = list(
            difflib.unified_diff(
                before.decode().splitlines(keepends=True),
                after.decode().splitlines(keepends=True),
                fromfile=path,
                tofile=path + " (native unchanged roundtrip)",
            )
        )
        diff_path = output / (Path(path).stem + ".diff")
        diff_path.write_text("".join(diff))
        before_tokens = list(yaml.scan(before))
        after_tokens = list(yaml.scan(after))
        observations.append(
            {
                "path": path,
                "before_sha256": hashlib.sha256(before).hexdigest(),
                "native_roundtrip_sha256": hashlib.sha256(after).hexdigest(),
                "semantic_equal": True,
                "ordered_yaml_nodes_and_tags_equal": True,
                "added_lines": sum(
                    line.startswith("+") and not line.startswith("+++") for line in diff
                ),
                "removed_lines": sum(
                    line.startswith("-") and not line.startswith("---") for line in diff
                ),
                "standalone_comment_lines": sum(
                    line.lstrip().startswith("#") for line in before.decode().splitlines()
                ),
                "explicit_tag_tokens": sum(
                    isinstance(token, yaml.tokens.TagToken) for token in before_tokens
                ),
                "scalar_styles_before": dict(
                    Counter(
                        str(token.style)
                        for token in before_tokens
                        if isinstance(token, yaml.tokens.ScalarToken)
                    )
                ),
                "scalar_styles_after": dict(
                    Counter(
                        str(token.style)
                        for token in after_tokens
                        if isinstance(token, yaml.tokens.ScalarToken)
                    )
                ),
                "diff": str(diff_path.relative_to(ROOT)),
            }
        )
    (output / "summary.json").write_text(json.dumps({"records": observations}, indent=2) + "\n")
    print(json.dumps(observations, indent=2))


def assigned_rows(inventory: dict) -> list[tuple[int, dict]]:
    numbers = sorted(
        number
        for group in inventory["planning_groups"]
        if group["name"] in GROUPS
        for number in group["queue_row_numbers"]
    )
    assert len(numbers) == len(set(numbers)) == 126
    return [(number, inventory["rows"][number - 1]) for number in numbers]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--inventory",
        type=Path,
        default=ROOT / ".temp/variant-683/planning-inventory-v2/inventory.json",
    )
    parser.add_argument("--capture-pmid")
    parser.add_argument("--prepare", type=Path)
    parser.add_argument("--validate-proposals", type=Path)
    parser.add_argument("--draft-review", type=Path)
    parser.add_argument("--presentation-audit", type=Path)
    args = parser.parse_args()
    if args.capture_pmid:
        pmid = args.capture_pmid
        if not pmid.isdigit():
            parser.error("PMID must be digits")
        directory = ROOT / ".temp/variant-683/remaining-sources" / ("abstract-" + pmid)
        if directory.exists():
            parser.error("capture destination exists")
        query = urllib.parse.urlencode(
            {"query": "EXT_ID:" + pmid + " AND SRC:MED", "format": "json", "resultType": "core"}
        )
        url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + query
        with urllib.request.urlopen(
            urllib.request.Request(url, headers={"User-Agent": "CultureMech-source-review/1.0"}),
            timeout=45,
        ) as response:
            raw = response.read()
        data = json.loads(raw)
        results = data["resultList"]["result"]
        assert len(results) == 1 and results[0]["id"] == pmid and results[0]["source"] == "MED"
        result = results[0]
        assert result.get("abstractText")
        directory.mkdir()
        (directory / "source.json").write_bytes(raw)
        inspection = result["title"] + "\n" + result["abstractText"] + "\n"
        (directory / "inspection.txt").write_text(inspection)
        receipt = {
            "url": url,
            "reference": "PMID:" + pmid,
            "retrieved_at": datetime.now(timezone.utc).isoformat(),
            "sha256": hashlib.sha256(raw).hexdigest(),
            "bytes": len(raw),
            "inspection_sha256": hashlib.sha256(inspection.encode()).hexdigest(),
            "limitation": "Primary article abstract indexed by Europe PMC; full methods not inspected.",
        }
        (directory / "receipt.json").write_text(json.dumps(receipt, indent=2) + "\n")
        print(json.dumps(receipt, indent=2))
        return
    if args.prepare:
        prepare(json.loads(args.inventory.read_text()), args.prepare)
        return
    if args.validate_proposals:
        validate_proposals(args.validate_proposals)
        return
    if args.draft_review:
        draft_review(args.draft_review, json.loads(args.inventory.read_text()))
        return
    if args.presentation_audit:
        presentation_audit(args.presentation_audit)
        return
    for number, row in assigned_rows(json.loads(args.inventory.read_text())):
        print(
            json.dumps(
                {
                    "row": number,
                    "path": row["source_path"],
                    "variant": row["variant_index"],
                    "name": row["variant_name"],
                    "index": row["modification_index"],
                    "text": row["modification_text"],
                    "references": sorted(
                        {
                            item["reference"]
                            for item in json.loads(row["variant_json"]).get("evidence", [])
                        }
                    ),
                },
                ensure_ascii=False,
            )
        )


if __name__ == "__main__":
    main()
