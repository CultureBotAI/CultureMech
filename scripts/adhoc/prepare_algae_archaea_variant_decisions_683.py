#!/usr/bin/env python3
"""Prepare manual algae/archaea variant decisions for #683 (2026-11-16).

Inputs: pinned 396-row inventory, current recipe bytes, inspected primary captures.
Outputs: exclusive decision JSON and native review targets; no recipe mutation.
All selections below are manual claim-level decisions, not extracted identities.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
QUEUE_SHA = "dd5faea741da0a11e8eb86cad2976e8bf51d42884c601e96973eba61748330ca"
SOURCE = {
    "tsuji": (
        "doi:10.1007/s10126-021-10037-4",
        "tsuji-2021-table-s1",
        "Table S1, component rows and sodium footnotes",
    ),
    "spectrum": (
        "doi:10.1128/spectrum.00069-23",
        "2asw-spectrum-2023",
        "Materials and Methods, algal strains and cultivation",
    ),
    "hiibel": (
        "doi:10.3389/fenrg.2015.00020",
        "hiibel-2015",
        "Materials and Methods, microalgal strains and maintenance media",
    ),
    "synecho": (
        "doi:10.3389/fmicb.2015.00326",
        "synechocystis-2015",
        "Results, ASW nitrogen/phosphorus additions and Figure 2 buffered condition",
    ),
    "tetraselmis": (
        "doi:10.1016/j.biortech.2017.04.008",
        "tetraselmis-2017",
        "Primary article abstract, second-stage N repletion",
    ),
    "spirulina": (
        "doi:10.1007/s00449-016-1726-2",
        "spirulina-2017",
        "Materials and methods, filtered effluent preparation and timed additions",
    ),
    "fertilizer": (
        "doi:10.1016/j.biortech.2025.132777",
        "tap-fertilizer-2025",
        "Primary article abstract, HAc-NaAc replacement of Tris",
    ),
    "emami": (
        "doi:10.1038/srep10036",
        "emami-2015",
        "Methods, culture conditions and bacterial-community antibiotic experiment",
    ),
    "bbmerds": (
        "https://www.ccap.ac.uk/wp-content/uploads/MR_BB_MErds.pdf",
        "ccap-bb-merds",
        "Page 1, 8:2 or 1:1 mixture; named BB and MErds recipes",
    ),
    "f2si": (
        "https://www.ccap.ac.uk/wp-content/uploads/MR_f2Si.pdf",
        "ccap-f2-si",
        "Page 2, f/2 + Si Modified, direct addition replacing stock 5",
    ),
    "reed": (
        "doi:10.1128/jb.183.24.7007-7016.2001",
        "reed-2001-html",
        "Materials and Methods, Archaeoglobus growth and harvest",
    ),
    "mayer": (
        "doi:10.1128/JB.06130-11",
        "mayer-2012-html",
        "Materials and Methods, acetate determination; separate 0.05% passage retained as a limit",
    ),
    "dsm119": (
        "https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium119.pdf",
        "dsmz-119",
        "Pages 1–2, exact DSM strain-specific instructions",
    ),
    "pyrococcus": (
        "doi:10.1128/AEM.01366-10",
        "pyrococcus-2011",
        "Primary article abstract, serial adaptation on CF11 cellulose",
    ),
    "willard": (
        "doi:10.1128/mbio.01033-24",
        "willard-2024",
        "Materials and Methods, low-sulfate Brock's salts and species-specific supplements",
    ),
    "auernik": (
        "doi:10.1128/AEM.02019-07",
        "auernik-2008-html",
        "Materials and Methods, transcriptomics versus scanning-electron-microscopy cultures",
    ),
}


def claim(
    label, source, snippet, stage, *, action="ADD", amount=None, unit=None, old=None, notes=""
):
    ref, _, locator = SOURCE[source]
    ingredient = {"preferred_term": label}
    if amount is not None:
        ingredient["concentration"] = {"value": str(amount), "unit": unit}
    if notes:
        ingredient["notes"] = notes
    result = {
        "action": action,
        "ingredient": ingredient,
        "stage": stage,
        "evidence": [
            {
                "reference": ref,
                "supports": "SUPPORT",
                "snippet": snippet,
                "explanation": locator + "; primary source inspected 2026-11-16. " + notes,
            }
        ],
        "notes": "A scoped change event, not a fully expanded variant or a parent-formulation amendment. No chemical identifier is inferred.",
    }
    if old:
        result["replaced_ingredient"] = {"preferred_term": old}
    return result


def decisions():
    output = {}

    def row(number, status, reason, *claims):
        if number in output:
            raise ValueError(f"duplicate manual row {number}")
        output[number] = {"status": status, "reason": reason, "claims": list(claims)}

    def condition(numbers, reason):
        for number in numbers:
            row(number, "CONDITION_ONLY", reason)

    def held(numbers, status, reason):
        for number in numbers:
            row(number, status, reason)

    held(
        [5, 6, 28],
        "HELD_EVIDENCE",
        "Matsui2018 primary metadata/abstract captured, but formulation/agar methods not verified; no Guillard-stock expansion or agar assertion promoted.",
    )
    condition(
        [7, 10, 29],
        "Culture conditions or acclimation only; atmospheric context is not converted to a liquid ingredient or concentration.",
    )
    held(
        [8],
        "HELD_EVIDENCE",
        "Source TableS1 gives Na2SeO3 0.001 micromolar=1nM and Na2SiO3.9H2O 0.1mM. Existing row says10nM; held for correction/review under issue759. PDF SHA2561cc2581bf2363ea89d31f170ae398b94d1125c647cc1c655a54417e6c73aac98.",
    )
    for number in [9, 32]:
        row(
            number,
            "STRUCTURED",
            "Source defines separate NaCl settings in modified artificial seawater, not total sodium.",
            claim(
                "NaCl",
                "tsuji",
                "0, 10, 20, 50, 200, or 423",
                "separate sodium-response modified F/2ASW formulations",
                action="SET_CONCENTRATION",
                amount="0; 10; 20; 50; 200; 423",
                unit="MILLIMOLAR",
                notes="Discrete alternative NaCl settings; zero means no NaCl addition. These are not summed or treated as a continuous dose. Trace salts contribute background sodium; no total sodium concentration or universal parent equivalence asserted.",
            ),
        )
    row(
        11,
        "STRUCTURED",
        "Explicit study medium concentration; no inferred amount added.",
        claim(
            "NaCl",
            "spectrum",
            "1.5 M NaCl",
            "study-specific D. salina CCAP19/18 cultivation in 2ASW",
            action="SET_CONCENTRATION",
            amount="1.5",
            unit="MOLAR",
            notes="Source states medium concentration, not stock strength or a dose increment; other constituents and parent equivalence remain unresolved.",
        ),
    )
    condition(
        [12, 14],
        "Uncertainty/interpretation guard for the adjacent claim; no additional input or identity asserted.",
    )
    row(
        13,
        "STRUCTURED",
        "Mixture-level replacement, without chemical expansion.",
        claim(
            "sea salts",
            "hiibel",
            "33.6",
            "modified 2ASW maintenance medium for the study's Dunaliella cultures",
            action="REPLACE",
            old="NaCl",
            amount="33.6",
            unit="G_PER_L",
            notes="Undefined sea-salt mixture replaces NaCl. No salt-product identity, constituent expansion, NaCl-equivalent molarity or parent seawater equivalence is claimed.",
        ),
    )
    held(
        [15],
        "HELD_MODEL",
        "Modified base medium alone does not identify an ingredient change; actual primary methods describe modified fixed-N-free YBCII, whose full equivalence to this parent is not established.",
    )
    condition([16, 18], "Organism/base-medium context, without an asserted ingredient change.")
    held(
        [17],
        "HELD_MODEL",
        "Primary Hemiaulus methods define no added organic/inorganic nitrogen and naturally dissolved N2. Do not invent a particular removed salt or deliberate N2 dose from this statement.",
    )
    row(
        19,
        "STRUCTURED",
        "Primary Results resolves the stated N and P sources at their study-specific concentrations.",
        claim(
            "NH4Cl",
            "synecho",
            "5 mM NH4Cl",
            "nitrogen-and-phosphorus-supplemented Marine Art SF-1 ASW",
            amount="5",
            unit="MILLIMOLAR",
            notes="Names resolved from the primary Results, not guessed from generic nitrogen/phosphorus prose. Does not certify equivalence to the local UTEX artificial-seawater parent.",
        ),
        claim(
            "K2HPO4",
            "synecho",
            "0.22 mM K2HPO4",
            "nitrogen-and-phosphorus-supplemented Marine Art SF-1 ASW",
            amount="0.22",
            unit="MILLIMOLAR",
            notes="Explicit phosphorus source; no hydrate or other phosphate identity inferred.",
        ),
    )
    row(
        20,
        "STRUCTURED",
        "Retain the buffer as the reported HEPES-KOH preparation.",
        claim(
            "HEPES-KOH buffer",
            "synecho",
            "20 mM HEPES",
            "buffered ASW with nitrogen and phosphorus sources, pH7.8 buffer",
            amount="20",
            unit="MILLIMOLAR",
            notes="The source calls the preparation HEPES-KOH. No separate KOH dose, chemical salt form or buffer-component stoichiometry inferred.",
        ),
    )
    condition(
        [26], "First-stage culture duration and base-medium use, without a new ingredient claim."
    )
    row(
        27,
        "STRUCTURED",
        "Primary abstract supports the second-stage repletion concentration only.",
        claim(
            "NaNO3",
            "tetraselmis",
            "4.41mM",
            "three-day nitrogen-replete second stage after seven-day F/2 culture",
            action="SET_CONCENTRATION",
            amount="4.41",
            unit="MILLIMOLAR",
            notes="Primary abstract was inspected; full Methods unavailable. This is the second-stage reported condition, not an amount to add to the first stage or a universal F/2 concentration.",
        ),
    )
    held(
        [30, 33, 55],
        "HELD_MODEL",
        "Gas-supply/aeration condition retained literally. No liquid concentration or ingredient addition inferred; exact gas-phase representation requires separate admission policy.",
    )
    row(
        31,
        "STRUCTURED",
        "Correct sibling matches TableS1; preserve full-formulation context.",
        claim(
            "sodium selenite",
            "tsuji",
            "0.001",
            "complete modified F/2ASW formulation, TableS1",
            action="SET_CONCENTRATION",
            amount="1",
            unit="NANOMOLAR",
            notes="TableS1 trace-element heading is micromolar:0.001micromolar×1000=1nanomolar. Not10nM and not an increment atop canonical F/2.",
        ),
        claim(
            "sodium metasilicate nonahydrate",
            "tsuji",
            "0.1",
            "complete modified F/2ASW formulation, TableS1",
            action="SET_CONCENTRATION",
            amount="0.1",
            unit="MILLIMOLAR",
            notes="Na2SiO3.9H2O under basal seawater components(mM). Hydrate specified by the source. No full parent equivalence or additional salt mass inferred.",
        ),
    )
    row(
        37,
        "STRUCTURED",
        "Undefined effluent input retained; timed feed stays in notes rather than one initial dose.",
        claim(
            "filtered biogas-process effluent",
            "spirulina",
            "filtered effluent",
            "effluent-based alternative Spirulina culture with sequential nutrient feeding",
            notes="Primary Methods: filtered plant-residue digester effluent in carbonate buffer;1.5%(v/v) at start, a similar volume after3days,3% of initial volume after6days. These sequential additions must not become a6% initial concentration. No constituent expansion or assertion that all canonical Spirulina ingredients remain present.",
        ),
    )
    condition(
        [38, 39, 43], "Comparison, coculture or process mode only; no new ingredient assertion."
    )
    row(
        40,
        "ALREADY_STRUCTURED",
        "The parent explicitly represents NH4Cl in Beijerinck's solution and acetic acid in Tris Acetate Stock Solution. TAP2024 Methods confirms their medium roles but does not make this row a new supplement. No parent/study dose-equivalence claim.",
    )
    held(
        [41],
        "HELD_MODEL",
        "Primary abstract supports a water-soluble-fertilizer replacement, but the replaced trace/macroelement group is not a resolved single ingredient. Hold component-set replacement and product identity; do not invent fertilizer constituents.",
    )
    row(
        42,
        "STRUCTURED",
        "Abstract-supported preparation-level buffer replacement; quantities unresolved.",
        claim(
            "HAc-NaAc buffer",
            "fertilizer",
            "HAc-NaAc",
            "Ab-WSF medium pH-balancing formulation",
            action="REPLACE",
            old="Tris",
            notes="Primary abstract explicitly says HAc-NaAc replaces Tris. Keep the source abbreviation at mixture level; no acetate salt hydration, buffer ratio, dose, final concentration or full TAP-equivalence inferred.",
        ),
    )
    row(
        46,
        "STRUCTURED",
        "Study-specific acid differs from parent CCAP acid; no dose inferred.",
        claim(
            "hydrochloric acid",
            "emami",
            "acidified to pH 1.5 using hydrochloric acid",
            "AJS study cultivation pH adjustment to1.5",
            action="REPLACE",
            old="sulfuric acid",
            notes="Emami Methods names HCl; separately inspected CCAP AJS page1 names concentrated H2SO4. No HCl strength/volume or replacement arithmetic. Other recipe details remain unresolved.",
        ),
    )
    condition([47], "Explicit formulation uncertainty limits the adjacent acid claim.")
    for number, bb, merds in [(48, "800", "200"), (49, "500", "500")]:
        row(
            number,
            "STRUCTURED",
            "Source-defined alternative blend of prepared media; no constituent expansion.",
            claim(
                "Bold's Basal Medium (BB)",
                "bbmerds",
                "8:2 mixture or 1:1 mixture",
                "preparation of the selected BB:MErds blend before autoclaving",
                amount=bb,
                unit="ML_PER_L",
                notes=f"Selected source ratio gives{bb}mL prepared BB and{merds}mL prepared MErds per1L mixture. These are source recipe inputs, not additional volumes atop an already completed parent medium; other ratio is separate.",
            ),
            claim(
                "MErds medium",
                "bbmerds",
                "8:2 mixture or 1:1 mixture",
                "preparation of the selected BB:MErds blend before autoclaving",
                amount=merds,
                unit="ML_PER_L",
                notes="Prepared modified Foyns Erdschreiber medium, retained as a named mixture without expanding stock constituents.",
            ),
        )
    row(
        50,
        "ALREADY_STRUCTURED",
        "Nitrate-bearing NaNO3 already occurs in the parent BG11 ingredients. This qualitative nitrate-replete row does not specify an additional dose or change; no study/formula equivalence inferred.",
    )
    condition(
        [51, 52, 53, 54],
        "Comparator medium, organism, measurement method or photoautotrophy context. BG110 is a separately named comparator, not an omission asserted for the nitrate-replete variant.",
    )
    row(
        62,
        "STRUCTURED",
        "Source names silicate but no salt or hydrate.",
        claim(
            "silicate",
            "emami",
            "1.06",
            "Isochrysis galbana study-specific f/2 supplementation",
            amount="1.06e-4",
            unit="MOLAR",
            notes="Preserve reported supplement concentration. No sodium salt, hydrate, stock composition, total silicate including base, or local f/2+Si equivalence inferred.",
        ),
    )
    condition(
        [63, 65, 68, 70, 71],
        "Explicit uncertainty/comparator boundary; no additional ingredient assertion.",
    )
    row(
        64,
        "STRUCTURED",
        "Source-reported nitrate supplement, not calculated total nitrate.",
        claim(
            "NaNO3",
            "emami",
            "29.4 mM NaNO3",
            "A. platensis study-specific f/2 supplementation, pH8",
            amount="29.4",
            unit="MILLIMOLAR",
            notes="Source does not resolve whether the stated supplement includes background nitrate. No total concentration or stock form inferred.",
        ),
    )
    row(
        66,
        "STRUCTURED",
        "Literal microgram/mL dose retained in notes; no unsupported enum or silent conversion.",
        claim(
            "penicillin G",
            "emami",
            "penicillin G",
            "antibiotic-treated D. polymorpha f/2 cultures",
            notes="Reported treatment dose200micrograms/mL. Unreported salt form and stock strength remain unresolved. Untreated control and later marine-agar bacterial assay are separate.",
        ),
    )
    row(
        67,
        "STRUCTURED",
        "Correct antibiotic and source salt retained.",
        claim(
            "dihydrostreptomycin sulphate",
            "emami",
            "dihydrostreptomycin sulphate",
            "antibiotic-treated D. polymorpha f/2 cultures",
            notes="Reported treatment dose50micrograms/mL, preserved literally without silent unit conversion. Not streptomycin; no hydrate or stock concentration inferred.",
        ),
    )
    row(
        69,
        "STRUCTURED",
        "Named vitamin preparations retained without fabricated constituents.",
        claim(
            "2ASW vitamin solution",
            "hiibel",
            "vitamin solution from the 2ASW medium",
            "modified f/2 maintenance medium for study Nannochloropsis cultures",
            action="REPLACE",
            old="original f/2 vitamin solution",
            notes="Source reports replacement and additional vitamin components but supplies no identities, dose or composition. Mismatched Gomord citation cannot fill these gaps; no claim of equivalence to a local stock.",
        ),
    )
    row(
        72,
        "STRUCTURED",
        "Direct solid replaces stock5; no double counting of stock and its solute.",
        claim(
            "sodium metasilicate nonahydrate",
            "f2si",
            "0.1705 g",
            "CCAP f/2+Si Modified direct-addition preparation",
            action="REPLACE",
            old="stock 5 sodium metasilicate solution",
            amount="0.1705",
            unit="G_PER_L",
            notes="Page2 says omit stock5 and instead add Na2SiO3.9H2O directly per litre. Parent stock5 composition is not separately added; no hydrate conversion.",
        ),
    )
    held(
        [74, 78],
        "HELD_EVIDENCE",
        "Hartzell1999 full stock/trace formulation not inspected. Reed2001 names basal salts/trace minerals without verifying these quantities/forms; preserve prose without promoting stock identities or doses.",
    )
    for number, reason, specs in [
        (
            75,
            "Only Reed2001 alternative buffer is structured; Hartzell PIPES preparation remains held for its primary source.",
            [("Tris", "20", "MILLIMOLAR"), ("maleic acid", "20", "MILLIMOLAR")],
        ),
        (
            76,
            "Only Reed2001 DL-sodium-lactate concentration structured; Hartzell30% stock7mL/L preparation remains held.",
            [("DL-sodium lactate", "22", "MILLIMOLAR")],
        ),
        (
            77,
            "Only Reed2001 yeast-extract condition structured; Wolfe-vitamin replacement belongs to unresolved Hartzell alternative.",
            [("yeast extract", "0.5", "G_PER_L")],
        ),
        (
            79,
            "Only Reed2001 final reductant concentrations structured; Hartzell combined-stock preparation remains held.",
            [("Na2S", "1", "MILLIMOLAR"), ("Na2S2O3", "1", "MILLIMOLAR")],
        ),
    ]:
        row(
            number,
            "STRUCTURED",
            reason,
            *[
                claim(
                    label,
                    "reed",
                    "STL",
                    "Reed2001 modified STL cultivation of A. fulgidus",
                    amount=value,
                    unit=unit,
                    notes=reason
                    + " Do not combine with Hartzell formulation or infer unspecified hydrate.",
                )
                for label, value, unit in specs
            ],
        )
    row(
        80,
        "STRUCTURED",
        "Resazurin identity supported by Reed; Hartzell N2-sparging assertion remains held and temperatures are conditions.",
        claim(
            "resazurin",
            "reed",
            "resazurin",
            "Reed2001 modified STL reduction indicator",
            notes="Source says0.2% resazurin was added without an unambiguous final-dose basis/stock volume; no concentration promoted. Stored biomass underN2 is not evidence of culture sparging.",
        ),
    )
    held(
        [81, 82, 83, 84],
        "HELD_EVIDENCE",
        "Koschnitzki2017 thesis formulation not independently inspected in this pass; quoted local evidence alone does not verify stock composition, sodium-sulfide hydration or added-versus-parent status.",
    )
    held(
        [85],
        "HELD_MODEL",
        "Headspace pressure/ratio and temperature/pH remain explicit prose; thesis evidence and gas-phase ingredient admission unresolved.",
    )
    row(
        86,
        "STRUCTURED",
        "0.1% condition is supported in acetate-determination passage; other0.05% experiment stays separate.",
        claim(
            "yeast extract",
            "mayer",
            "0.1% [wt/vol] yeast extract",
            "I. hospitalis mixotrophic culture for acetate determination",
            amount="0.1",
            unit="PERCENT_W_V",
            notes="Source also reports0.05% for a separate ACS-dependence/acetate-uptake setup. Do not generalize0.1% across every experiment or combine the two doses.",
        ),
    )
    row(
        87,
        "STRUCTURED",
        "Three supplements and two explicit omissions scoped to the listed DSM strains.",
        claim(
            "Wolin's vitamin solution (10x)",
            "dsm119",
            "1 ml/l Wolin's vitamin solution",
            "listed DSM strains after autoclaving from sterile anoxic stocks",
            amount="1",
            unit="ML_PER_L",
            notes="Named10x solution refers to medium120; constituent composition not expanded.",
        ),
        claim(
            "DL-dithiothreitol",
            "dsm119",
            "0.30",
            "listed DSM strains after autoclaving from sterile anoxic stocks",
            amount="0.30",
            unit="G_PER_L",
        ),
        claim(
            "2-mercaptoethanesulfonic acid (coenzyme M)",
            "dsm119",
            "0.15 g/l coenzyme M",
            "listed DSM strains after autoclaving from sterile anoxic stocks",
            amount="0.15",
            unit="G_PER_L",
            notes="Acid identity explicit; no sodium salt inferred.",
        ),
        claim(
            "Na2S x 9 H2O",
            "dsm119",
            "Omit Na2S",
            "listed DSM strain-specific omitted reductant",
            action="REMOVE",
        ),
        claim(
            "L-Cysteine HCl x H2O",
            "dsm119",
            "L-Cysteine HCl x H2O",
            "listed DSM strain-specific omitted reductant",
            action="REMOVE",
        ),
    )
    condition([88, 90, 101, 102], "pH condition only; no named titrant or dose invented.")
    held(
        [89, 95, 99, 100],
        "HELD_MODEL",
        "Primary DSMZ recipe verifies the gas mixture/pressure but it is a post-inoculation headspace operation; preserve literal context pending explicit gas-occurrence admission, not a liquid ingredient concentration.",
    )
    row(
        91,
        "STRUCTURED",
        "Explicit post-autoclave supplement for DSM5522.",
        claim(
            "D-glucose",
            "dsm119",
            "5.0 g/l D-glucose",
            "DSM5522 after autoclaving from sterile anoxic stock",
            amount="5.0",
            unit="G_PER_L",
        ),
    )
    row(
        92,
        "STRUCTURED",
        "Set reported amount; do not add3g/L to the prior amount.",
        claim(
            "Na-acetate",
            "dsm119",
            "3.00 g/l",
            "DSM6216 strain-specific medium formulation",
            action="SET_CONCENTRATION",
            amount="3.00",
            unit="G_PER_L",
            notes="Source gives no hydrate; value replaces the baseline amount rather than adding an increment.",
        ),
    )
    row(
        93,
        "STRUCTURED",
        "Explicit sulfate supplement for DSM7057.",
        claim(
            "Na2SO4",
            "dsm119",
            "2.00 g/l Na2SO4",
            "DSM7057 strain-specific supplementation",
            amount="2.00",
            unit="G_PER_L",
            notes="No hydrate inferred.",
        ),
    )
    for number, strains in [(94, "DSM7095 and DSM28100"), (96, "DSM15163")]:
        row(
            number,
            "STRUCTURED",
            "Literal0.3g supplement and explicit omitted nonahydrate; pH context retained.",
            claim(
                "DL-dithiothreitol",
                "dsm119",
                "0.3 g DL-Dithiothreitol",
                strains + " strain-specific supplementation",
                notes="Literal source amount0.3g; the strain note does not repeat a per-litre basis, so no concentration is inferred from the recipe volume.",
            ),
            claim(
                "Na2S x 9 H2O",
                "dsm119",
                "Omit Na2S",
                strains + " omitted reductant",
                action="REMOVE",
            ),
        )
    row(
        97,
        "STRUCTURED",
        "Replacement and two supplements kept separate; no stock expansion.",
        claim(
            "clarified rumen fluid",
            "dsm119",
            "same volume of clarified rumen fluid",
            "DSM16632 strain-specific fluid replacement",
            action="REPLACE",
            old="sludge fluid",
            notes="Same-volume replacement specified; no independently inferred density or final concentration. Medium1310 preparation remains a named-mixture reference.",
        ),
        claim(
            "Trypticase peptone",
            "dsm119",
            "2.00 g/l Trypticase peptone",
            "DSM16632 strain-specific supplement",
            amount="2.00",
            unit="G_PER_L",
        ),
        claim(
            "Wolin's vitamin solution",
            "dsm119",
            "10.00 ml/l",
            "DSM16632 strain-specific supplement",
            amount="10.00",
            unit="ML_PER_L",
            notes="Source refers to medium141; not assumed equal to the10x medium120 preparation in another strain variant.",
        ),
    )
    row(
        98,
        "STRUCTURED",
        "CoenzymeM supplement structured; separately named1bar gas operation remains held under gas-phase admission.",
        claim(
            "2-mercaptoethanesulfonic acid (coenzyme M)",
            "dsm119",
            "0.10 g/l",
            "DSM25824 after autoclaving from sterile filtered anoxic stock",
            amount="0.10",
            unit="G_PER_L",
            notes="Gas mixture/pressure is a separate post-inoculation condition, not a liquid ingredient dose.",
        ),
    )
    condition(
        [103, 104, 105],
        "Growth phase, organism or serial-adaptation context, without a new ingredient assertion.",
    )
    row(
        106,
        "STRUCTURED",
        "Primary abstract verifies CF11-cellulose substrate identity only.",
        claim(
            "CF11 cellulose",
            "pyrococcus",
            "CF11 cellulose",
            "serially adapted P. furiosus growth-substrate condition",
            notes="Primary abstract inspected; full formulation and dose not verified. Do not infer cellulose concentration, replace a particular baseline substrate or certify parent-medium equivalence.",
        ),
    )
    row(
        107,
        "STRUCTURED",
        "NH4Cl substitution is supported; vague MgSO4 reduction/replacement remains unpromoted.",
        claim(
            "NH4Cl",
            "willard",
            "1.05 g/L (NH4)Cl",
            "Willard2024 low-sulfate Brock's salts aerobic formulation",
            action="REPLACE",
            old="(NH4)2SO4",
            amount="1.05",
            unit="G_PER_L",
            notes="Primary formulation names NH4Cl; local anaerobic parent names ammonium sulfate. Primary MgSO4.7H2O concentration equals0.25g/L already in this parent, so no unsupported MgSO4 reduction/substitution event is emitted.",
        ),
    )
    held(
        [108],
        "HELD_MODEL",
        "Sulfur10g/L and some yeast extract are already in parent; primary source has distinct species-specific0.2g/L/1g/L yeast, sucrose/NZ-Amine and other supplements. Keep this aggregate row held until separate alternative recipe scopes are explicit, not one simultaneous recipe.",
    )
    held(
        [109],
        "HELD_MODEL",
        "Aerobic foam-stopper condition is verified, but source does not explicitly state removal events for this local parent's Na2S/N2. Do not transform absence from a source list into an unqualified omission assertion.",
    )
    held(
        [110],
        "HELD_EVIDENCE",
        "Willard2024 Methods states concentrated HCl only; existing H2SO4-or-HCl alternative is not supported by the cited source. Preserve hold pending prose correction/review.",
    )
    held(
        [111, 112, 113, 114],
        "HELD_EVIDENCE",
        "Sakai2017 primary metadata/abstract describes aerobic sulfur-inhibited S.acidiphilus, whereas this variant asserts anaerobic MBSY/H2-CO2 and optional sulfur. Full Methods not inspected, so formulation/dose/source linkage remains held, not certified or corrected from abstract alone.",
    )
    condition([115], "Base-medium, pH, temperature and oxygen context only.")
    row(
        116,
        "STRUCTURED",
        "Yeast-extract condition verified; tryptone alternative remains held for source evidence.",
        claim(
            "yeast extract",
            "auernik",
            "0.1% yeast extract",
            "M.sedula DSM5348 transcriptomic culture on DSMZ88",
            notes="Source states0.1% without an explicit percent basis in the inspected passage; retain the literal amount here, do not infer w/v. The row's tryptone alternative was not verified and is not structured.",
        ),
    )
    row(
        117,
        "STRUCTURED",
        "Two distinct experiments retained with explicit stages, not simultaneous interchangeable supplements.",
        claim(
            "FeSO4.7H2O",
            "auernik",
            "7.5 g/liter",
            "M.sedula transcriptomic cultures: iron-supplemented yeast-extract arm before inoculation",
            amount="7.5",
            unit="G_PER_L",
            notes="Approximately7.5g/L; preserve approximation. Two of four yeast-extract cultures received iron; no universal addition.",
        ),
        claim(
            "FeS2 (pyrite)",
            "auernik",
            "0.1% FeS2",
            "M.sedula scanning-electron-microscopy cultures on minimal salts medium",
            notes="Different experimental preparation from the transcriptomics DSMZ88+yeast+iron arm. Literal0.1% sole-energy-source input; percent basis not specified, no concentration enum or parent equivalence inferred.",
        ),
    )
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--inventory", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--targets", type=Path, required=True)
    args = parser.parse_args()
    inventory = json.loads(args.inventory.read_text())
    if inventory["summary"]["queue_sha256"] != QUEUE_SHA:
        raise ValueError("manual decisions belong to a different queue")
    selected = decisions()
    expected = set()
    for group in inventory["planning_groups"]:
        if group["name"] in {"algae_remaining", "archaea_remaining"}:
            expected.update(group["queue_row_numbers"])
    if set(selected) != expected:
        raise ValueError(
            f"row coverage mismatch: missing{sorted(expected-set(selected))}; extra{sorted(set(selected)-expected)}"
        )
    records, variants, targets, dispositions = {}, {}, {}, []
    for number, decision in sorted(selected.items()):
        item = inventory["rows"][number - 1]
        path = "data/normalized_yaml/" + item["source_path"]
        if hashlib.sha256((ROOT / path).read_bytes()).hexdigest() != item["source_sha256"]:
            raise ValueError("source changed:" + path)
        targets[path] = {
            "target_id": item["recipe_id"],
            "path": path,
            "label": item["source_path"],
            "kind": "maintained",
            "record_class": "MediaRecipe",
            "selector": "Assigned exact variant modification rows and proposed ingredient_changes only; not whole-record recertification",
        }
        changes = decision["claims"]
        if changes:
            record = records.setdefault(
                path,
                {
                    "path": path,
                    "recipe_id": item["recipe_id"],
                    "expected_sha256": item["source_sha256"],
                    "variants": [],
                },
            )
            vi = int(item["variant_index"])
            key = (path, vi)
            if key not in variants:
                variants[key] = {
                    "variant_index": vi,
                    "variant_name": item["variant_name"],
                    "ingredient_changes": [],
                }
                record["variants"].append(variants[key])
            for change in changes:
                change["source_modification_index"] = int(item["modification_index"])
                change["source_text"] = item["modification_text"]
                variants[key]["ingredient_changes"].append(change)
        dispositions.append(
            {
                "queue_row_number": number,
                "status": decision["status"],
                "reason": decision["reason"],
                "assertion_count": len(changes),
                "recipe_id": item["recipe_id"],
                "source_path": path,
                "source_sha256": item["source_sha256"],
                "variant_index": int(item["variant_index"]),
                "modification_index": int(item["modification_index"]),
                "source_text": item["modification_text"],
            }
        )
    sources = []
    for key, (reference, folder, locator) in SOURCE.items():
        directory = ROOT / ".temp/variant-683/sources" / folder
        receipt = json.loads((directory / "receipt.json").read_text())
        source_files = sorted(directory.glob("source.*"))
        source_file = source_files[0] if source_files else directory / "metadata.json"
        digest = hashlib.sha256(source_file.read_bytes()).hexdigest()
        recorded = receipt.get("sha256") if source_files else receipt["metadata_sha256"]
        if digest != recorded:
            raise ValueError("source receipt mismatch:" + folder)
        sources.append(
            {
                "key": key,
                "reference": reference,
                "path": str(source_file.relative_to(ROOT)),
                "sha256": digest,
                "locator": locator,
                "access_scope": (
                    "full primary source" if source_files else "primary abstract/metadata only"
                ),
            }
        )
    payload = {
        "schema_version": 1,
        "source_queue_sha256": QUEUE_SHA,
        "scope": "All96assigned algae/archaea rows explicitly disposed; only listed source-supported assertions proposed. Partial rows retain unresolved portions in reason. No recipe edits, ontology IDs, human REVIEWED status or full-record/release certification.",
        "source_inspections": sources,
        "records": list(records.values()),
        "dispositions": dispositions,
        "limitations": [
            "Gas-phase operations remain held pending admission policy.",
            "Named media/stock/undefined mixtures are not chemically expanded.",
            "Sources inaccessible or ambiguous are held; condition-only is a literal-row disposition, not ingredient absence in the full methods.",
            "Independent review and guarded application remain required.",
        ],
    }
    for path in [args.output, args.targets]:
        if path.exists():
            raise ValueError("refusing overwrite:" + str(path))
        path.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("x") as stream:
        json.dump(payload, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    with args.targets.open("x") as stream:
        yaml.safe_dump({"targets": list(targets.values())}, stream, sort_keys=False)
    print(
        json.dumps(
            {
                "records_with_assertions": len(records),
                "target_records": len(targets),
                "rows": len(dispositions),
                "assertions": sum(item["assertion_count"] for item in dispositions),
                "dispositions": dict(Counter(item["status"] for item in dispositions)),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
