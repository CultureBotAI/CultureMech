#!/usr/bin/env python3
"""Correct ingredient groundings that point at the wrong chemical species (#256).

Why this matters more than an ordinary grounding tidy-up
--------------------------------------------------------
kg-microbe resolves an ingredient with
``best_primary([chebi_id, culturemech_term_id, mim_id, ...])``. ``culturemech_term_id``
is populated from OUR ``term.id`` and outranks ``mim_id``, so a wrong id here overrides
MediaIngredientMech's correct one downstream and no MIM-side fix can reach it
(MediaIngredientMech#138). Our ``mediaingredientmech_chebi_term`` cannot catch it either
— it is a self-link to our own ``term.id`` in 119,577 of 120,131 rows.

Scope: groundings where the record's OWN evidence contradicts the id, plus a small
curator-approved set of high-frequency disagreements where MediaIngredientMech's
published exactMatch settles the intended identity. The latter set is checked against
the live sibling-repository SSSOM before any corpus edit, so SSSOM drift aborts the run.

  ``Magnesium Sulfate Heptahydrate`` -> CHEBI:86463
      CHEBI:86463 is *potassium aluminium sulfate*. The rows carry
      ``label: magnesium sulfate heptahydrate``, ``CAS: 10034-99-8`` and ``MW: 246.47``,
      all of which are magnesium sulfate heptahydrate = CHEBI:31795. Every other name on
      CHEBI:86463 (``AlK(SO4)2``, ``Aluminum potassium sulfate``, ``KAl(SO4)2``) is
      correct and is left alone; the two sets share no record, so this is a bad id
      rather than a row-alignment slip.

  glucose -> CHEBI:42758
      CHEBI:42758 is *aldehydo-D-glucose*, the open-chain aldehyde tautomer (a fraction
      of a percent of glucose in solution). A medium calling for glucose means the
      ordinary sugar. Bare ``Glucose`` -> CHEBI:17234 (glucose); the explicitly-D names
      and ``Dextrose`` -> CHEBI:17634 (D-glucose).

Both replacement ids are the ones MediaIngredientMech already asserts, so the fix also
removes ~850 rows of divergence rather than trading one disagreement for another.

Usage::

    just fix-wrong-groundings                  # dry run, prints every change
    just fix-wrong-groundings --limit 1 --apply   # canary one record
    just fix-wrong-groundings --apply          # fan out
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

import yaml
from audit_mim_sssom_divergence import DEFAULT_SSSOM, load_sssom, normalize_name

REPO = Path(__file__).resolve().parent.parent
NORMALIZED = REPO / "data" / "normalized_yaml"

# These formerly deferred #256 decisions are now adjudicated by the primary identity
# source requested by the media-content review: MIM's published skos:exactMatch rows.
# validate_mim_reconciliations() checks every asserted target id AND ontology label
# against that SSSOM before main() scans or writes the corpus.
MIM_EXACT_CORRECTIONS: dict[tuple[str, str], tuple[str, str]] = {
    ("CHEBI:72699", "(NH4)3 citrate"): ("CHEBI:63037", "triammonium citrate"),
    ("CHEBI:17439", "Vitamin B12"): ("CHEBI:176843", "vitamin B12"),
    ("CHEBI:64755", "EDTA"): ("CHEBI:4735", "ethylenediaminetetraacetic acid"),
    ("CHEBI:26948", "Thiamine"): ("CHEBI:18385", "thiamine(1+)"),
    ("CHEBI:26948", "thiamine"): ("CHEBI:18385", "thiamine(1+)"),
    ("CHEBI:30769", "Citrate"): ("CHEBI:16947", "citrate(3-)"),
    ("CHEBI:53258", "Citric acid"): ("CHEBI:30769", "citric acid"),
    ("CHEBI:46983", "D-Arabinose"): ("CHEBI:17108", "D-arabinose"),
    ("CHEBI:48095", "D-Fructose"): ("CHEBI:15824", "D-fructose"),
    ("CHEBI:37675", "D-Mannose"): ("CHEBI:16024", "D-mannose"),
    ("CHEBI:42106", "DL-Dithiothreitol"): ("CHEBI:18320", "1,4-dithiothreitol"),
    ("CHEBI:53001", "NiSO4 x 7 H2O"): ("CHEBI:53504", "nickel sulfate heptahydrate"),
    ("CHEBI:64243", "Sodium glutamate monohydrate"): (
        "CHEBI:232425",
        "monosodium L-glutamate hydrate",
    ),
    ("CHEBI:85248", "Starch"): ("CHEBI:28017", "starch"),
    ("CHEBI:85248", "Starch "): ("CHEBI:28017", "starch"),
    ("CHEBI:150970", "DL-mevalonic acid"): ("CHEBI:25351", "mevalonic acid"),
    ("CHEBI:15356", "L-Cysteine"): ("CHEBI:17561", "L-cysteine"),
    ("CHEBI:53558", "L-Lysine HCl"): ("CHEBI:53633", "L-lysine hydrochloride"),
    ("CHEBI:29988", "Na glutamate"): ("CHEBI:64220", "monosodium glutamate"),
    ("CHEBI:29988", "Na-glutamate"): ("CHEBI:64220", "monosodium glutamate"),
}

# Exact names/formulas that settle hydration, salt identity, or stereochemistry even
# where MIM has only a close/synonym mapping (or no subject row). Every target label
# below was checked against OAK sqlite:obo:chebi on 2026-08-25. These remain keyed on
# both source id and preferred_term; an anhydrous name on the same id never moves.
NAME_SETTLED_CORRECTIONS: dict[tuple[str, str], tuple[str, str]] = {
    ("CHEBI:35696", "CoCl2 x 6 H2O"): ("CHEBI:53503", "cobalt chloride hexahydrate"),
    ("CHEBI:34683", "Na2HPO4 x 2 H2O"): ("CHEBI:91258", "disodium hydrogenphosphate dihydrate"),
    ("CHEBI:3312", "Calcium chloride dihydrate"): ("CHEBI:86158", "calcium chloride dihydrate"),
    ("CHEBI:6636", "Magnesium chloride hexahydrate"): (
        "CHEBI:86345",
        "magnesium dichloride hexahydrate",
    ),
    ("CHEBI:32599", "Magnesium Sulfate Heptahydrate"): (
        "CHEBI:31795",
        "magnesium sulfate heptahydrate",
    ),
    ("CHEBI:32599", "Magnesium sulfate heptahydrate"): (
        "CHEBI:31795",
        "magnesium sulfate heptahydrate",
    ),
    ("CHEBI:86360", "MnSO4 x 4 H2O"): ("CHEBI:86358", "manganese(II) sulfate tetrahydrate"),
    ("CHEBI:86360", "MnSO4 x 5 H2O"): ("CHEBI:131524", "manganese(II) sulfate pentahydrate"),
    ("CHEBI:33146", "VOSO4 x 2 H2O"): ("CHEBI:87009", "vanadyl sulfate dihydrate"),
    ("CHEBI:33146", "VOSO4 x 5 H2O"): ("CHEBI:132758", "vanadyl sulfate pentahydrate"),
    ("CHEBI:87014", "VOSO4 x 5 H2O"): ("CHEBI:132758", "vanadyl sulfate pentahydrate"),
    ("CHEBI:30066", "Na-thioglycolate"): ("CHEBI:86481", "sodium thioglycolate"),
    ("CHEBI:17968", "Na-butyrate"): ("CHEBI:64103", "sodium butyrate"),
    ("CHEBI:30924", "Na-tartrate"): ("CHEBI:63017", "sodium L-tartrate"),
    ("CHEBI:63036", "Dipotassium phosphate"): ("CHEBI:131527", "dipotassium hydrogen phosphate"),
}

# (current wrong id, exact preferred_term) -> (correct id, correct label)
# Keyed on NAME AND ID together: the same wrong id also carries correctly-grounded
# names, and rewriting by id alone would corrupt them.
CORRECTIONS: dict[tuple[str, str], tuple[str, str]] = {
    **MIM_EXACT_CORRECTIONS,
    **NAME_SETTLED_CORRECTIONS,
    ("CHEBI:86463", "Magnesium Sulfate Heptahydrate"): (
        "CHEBI:31795",
        "magnesium sulfate heptahydrate",
    ),
    ("CHEBI:42758", "Glucose"): ("CHEBI:17234", "glucose"),
    ("CHEBI:42758", "glucose"): ("CHEBI:17234", "glucose"),
    ("CHEBI:42758", "D-Glucose"): ("CHEBI:17634", "D-glucose"),
    ("CHEBI:42758", "D-glucose"): ("CHEBI:17634", "D-glucose"),
    ("CHEBI:42758", "D(+)-Glucose"): ("CHEBI:17634", "D-glucose"),
    ("CHEBI:42758", "Dextrose"): ("CHEBI:17634", "D-glucose"),
    # Fructose is an unrelated sugar. MIM's reviewed D-glucose mapping carries both
    # spellings as synonyms, and ChEBI identifies CHEBI:17634 as D-glucose.
    ("CHEBI:15824", "D(+)-Glucose"): ("CHEBI:17634", "D-glucose"),
    ("CHEBI:15824", "Dextrose"): ("CHEBI:17634", "D-glucose"),
    # PABA (#260, reported from MediaIngredientMech#138). CHEBI:194474 is
    # 4-ammoniobenzoate, the zwitterion. Every one of these rows carries
    # `CAS: 150-13-0` in its own notes, which is the neutral acid = CHEBI:30753, and
    # every one has an EMPTY term.label, so nothing on the record ever asserted the
    # zwitterion. MIM independently grounds the name to the acid across 1,968
    # occurrences.
    ("CHEBI:194474", "4-Aminobenzoic acid"): ("CHEBI:30753", "4-aminobenzoic acid"),
    ("CHEBI:194474", "p-Amino Benzoic Acid"): ("CHEBI:30753", "4-aminobenzoic acid"),
    ("CHEBI:194474", "p-amino benzoic acid"): ("CHEBI:30753", "4-aminobenzoic acid"),
    # Cysteine-HCl -> CHEBI:52891, which is `QSY9 succinimidyl ester(1+)` -- a
    # fluorescence quencher dye, not an amino acid at all. The same string is already
    # grounded to CHEBI:91247 (L-cysteine hydrochloride) in 40 other rows, and the name
    # carries no hydrate marker, so the anhydrous HCl salt is the target.
    ("CHEBI:52891", "Cysteine-HCl"): ("CHEBI:91247", "L-cysteine hydrochloride"),
    ("CHEBI:52891", "cysteine-HCl"): ("CHEBI:91247", "L-cysteine hydrochloride"),
    # Names that spell out HCl AND a hydrate, grounded to CHEBI:17561 (plain
    # L-cysteine) -- neither the salt nor the hydrate. The corpus already uses
    # CHEBI:91248 (L-cysteine hydrochloride hydrate) for this substance in 1,901 rows,
    # so this is the corpus disagreeing with itself, not a judgement call.
    ("CHEBI:17561", "L-Cysteine-HCl x H2O"): ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    ("CHEBI:17561", "Cysteine-HCl x H2O"): ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    ("CHEBI:17561", "Cysteine-HCl\u00b7H2O"): ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    ("CHEBI:17561", "L-cysteine-HCL x H2O"): ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    ("CHEBI:17561", "L-Cysteine-HCl\u00b7H2O"): ("CHEBI:91248", "L-cysteine hydrochloride hydrate"),
    # --- #258: one ingredient name, several ids ---------------------------------
    # 63 names in the corpus are grounded more than one way (13,657 rows). The ones
    # below are those where the NAME ITSELF settles it: it spells out a hydrate the id
    # does not have, or names a salt where the id is the bare ion. Names that do NOT
    # specify a hydrate keep the anhydrous id -- `Na2MoO4` and `Sodium molybdate` stay
    # on CHEBI:75215, only the `2 H2O` spellings move -- so this is keyed on the exact
    # string, never on the id alone.
    # Deliberately excluded: `Vitamin B12` (cyanocobalamin vs the vitamer class, the
    # judgement call #256 defers), `Maltose` (generic vs alpha anomer), and the CaCl2 /
    # MgSO4 / MgCl2 rows naming hydrates that do not exist (`MgCl2 x 7 H2O`).
    # sodium molybdate DIhydrate
    ("CHEBI:75215", "Na2MoO4\u00b72H2O"): ("CHEBI:75213", "sodium molybdate dihydrate"),
    ("CHEBI:75215", "Na2MoO4 x 2 H2O"): ("CHEBI:75213", "sodium molybdate dihydrate"),
    ("CHEBI:75215", "Na2MoO4\u30fb2H2O"): ("CHEBI:75213", "sodium molybdate dihydrate"),
    ("CHEBI:75215", "Na2MoO4 . 2H2O"): ("CHEBI:75213", "sodium molybdate dihydrate"),
    # cobalt(2+) sulfate HEPTAhydrate -- here the MAJORITY was wrong: 1,161 rows named
    # `CoSO4 x 7 H2O` sat on the anhydrous id and only 5 on the heptahydrate.
    ("CHEBI:53470", "CoSO4 x 7 H2O"): ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    ("CHEBI:53470", "CoSO4\u00b77H2O"): ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    ("CHEBI:53470", "CoSO4\u30fb7H2O"): ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    ("CHEBI:53470", "CoSO4 . 7H2O"): ("CHEBI:91244", "cobalt(2+) sulfate heptahydrate"),
    # magnesium sulfate HEPTAhydrate
    ("CHEBI:32599", "MgSO4\u00b77H2O"): ("CHEBI:31795", "magnesium sulfate heptahydrate"),
    # disodium selenite PENTAhydrate
    ("CHEBI:48843", "Na2SeO3 x 5 H2O"): ("CHEBI:131361", "disodium selenite pentahydrate"),
    ("CHEBI:48843", "Na2SeO3\u30fb5H2O"): ("CHEBI:131361", "disodium selenite pentahydrate"),
    ("CHEBI:48843", "Na2SeO3\u00b75H2O"): ("CHEBI:131361", "disodium selenite pentahydrate"),
    ("CHEBI:48843", "Na2SeO3.5H2O"): ("CHEBI:131361", "disodium selenite pentahydrate"),
    # iron(2+) sulfate HEPTAhydrate
    ("CHEBI:75832", "FeSO4 x 7H2O"): ("CHEBI:75836", "iron(2+) sulfate heptahydrate"),
    ("CHEBI:75832", "Iron (II) sulfate heptahydrate"): (
        "CHEBI:75836",
        "iron(2+) sulfate heptahydrate",
    ),
    # magnesium dichloride HEXAhydrate
    ("CHEBI:6636", "MgCl2 x 6 H2O"): ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    ("CHEBI:6636", "MgCl2x 6 H2O"): ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    ("CHEBI:6636", "MgCl2 x 6H2O"): ("CHEBI:86345", "magnesium dichloride hexahydrate"),
    # `Starch` grounded to gellan gum is declared in MIM_EXACT_CORRECTIONS above.
    # Rows actually named `Gelrite` / `Gellan Gum` stay on CHEBI:85248, correctly.
    # KNO3 is the salt, CHEBI:17632 is the bare nitrate ION.
    ("CHEBI:17632", "KNO3"): ("CHEBI:63043", "potassium nitrate"),
    # zwitterion ids for names that state the neutral compound
    ("CHEBI:57305", "Glycine"): ("CHEBI:15428", "glycine"),
    ("CHEBI:35235", "L-Cysteine"): ("CHEBI:17561", "L-cysteine"),
    # the tri-anion vs the neutral salt
    ("CHEBI:4991", "Fe(III) citrate"): ("CHEBI:144421", "iron(III) citrate"),
    # Dextrose IS D-glucose, by definition. It was split three ways.
    ("CHEBI:17234", "Dextrose"): ("CHEBI:17634", "D-glucose"),
    ("CHEBI:4167", "Dextrose"): ("CHEBI:17634", "D-glucose"),
    # `Sodium citrate` with no hydrate marker, sitting on the dihydrate. The rows that
    # DO say dihydrate stay on CHEBI:32142.
    ("CHEBI:32142", "Sodium citrate"): ("CHEBI:53258", "sodium citrate"),
    ("CHEBI:32142", "Sodium Citrate"): ("CHEBI:53258", "sodium citrate"),
    ("CHEBI:32142", "sodium citrate"): ("CHEBI:53258", "sodium citrate"),
    # one stray row against the 470-row majority
    ("FOODON:03420180", "Pancreatic digest of casein"): ("MICRO:0000182", "tryptone"),
    # --- #259: hydration mismatches the LABEL DRIFT was hiding ---------------------
    # Found by comparing each ingredient's NAME against its grounded term's real CHEBI
    # label. #258-class errors in spellings that sweep missed -- and they matter here
    # because refilling term.label from the ontology would have made the label agree
    # with the wrong id, destroying the only visible signal that it was wrong.
    ("CHEBI:64734", "Na2-EDTA x 2 H2O"): ("CHEBI:64758", "EDTA disodium salt dihydrate"),
    ("CHEBI:64734", "Na-EDTA x 2 H2O"): ("CHEBI:64758", "EDTA disodium salt dihydrate"),
    ("CHEBI:64734", "Na2-EDTA\u00b72H2O"): ("CHEBI:64758", "EDTA disodium salt dihydrate"),
    # Found by the standing hydration check added for #278 -- it lives in a solution
    # record's top-level `composition:`, which the one-off scan for #275 never reached.
    ("CHEBI:64734", "Disodium EDTA dihydrate"): ("CHEBI:64758", "EDTA disodium salt dihydrate"),
    ("CHEBI:87014", "VOSO4 x 2 H2O"): ("CHEBI:87009", "vanadyl sulfate dihydrate"),
    ("CHEBI:75215", "Na2MoO4 \u00b7 2H2O"): ("CHEBI:75213", "sodium molybdate dihydrate"),
    ("CHEBI:75215", "Na2MoO4 x 2H2O"): ("CHEBI:75213", "sodium molybdate dihydrate"),
    ("CHEBI:75215", "Na2MoO4. 2H2O"): ("CHEBI:75213", "sodium molybdate dihydrate"),
    ("CHEBI:76208", "Sodium sulfide nonahydrate"): ("CHEBI:76209", "sodium sulfide nonahydrate"),
    ("CHEBI:63675", "Sodium succinate dibasic hexahydrate"): (
        "CHEBI:63686",
        "sodium succinate hexahydrate",
    ),
    # NOT fixed: `FeSO4 x 6 H2O` / `x 5 H2O` (18 rows) and `VOSO4 x 5 H2O` -- CHEBI has
    # no term for those hydrates, and they are likelier transcription errors for the
    # heptahydrate than real formulations. Left for curation.
    # --- #276 item 2: a racemate is not its L-enantiomer -------------------------
    # A DL- name grounded to the single-enantiomer term. Most DL- names in the corpus
    # are already correct -- `DL-methionine` -> `methionine`, `DL-Malic acid` ->
    # `malic acid` are stereo-UNSPECIFIED and fine -- so only these two move.
    ("CHEBI:17895", "DL-Tyrosine"): ("CHEBI:18186", "tyrosine"),
    ("CHEBI:16857", "DL-threonine"): ("CHEBI:26986", "threonine"),
    # --- #276/#278: found by the element-mismatch detector -----------------------
    # Each of these is grounded to a term whose ChEBI FORMULA lacks an element the
    # ingredient's own name demands. Four name a completely different substance --
    # ninhydrin for manganese sulfate, a peptide for sodium tungstate, organics for
    # sodium sulfide and cobalt nitrate -- which is the class that keeps recurring
    # (CHEBI:52891 the dye, CHEBI:86463 potassium aluminium sulfate).
    ("CHEBI:85357", "Sodium sulfide nonahydrate"): ("CHEBI:76209", "sodium sulfide nonahydrate"),
    ("CHEBI:85357", "Sodium sulfide"): ("CHEBI:76208", "sodium sulfide (anhydrous)"),
    ("CHEBI:78038", "Co(NO ) .6H O"): ("CHEBI:86214", "cobalt dinitrate hexahydrate"),
    ("CHEBI:86374", "Manganese sulfate monohydrate"): (
        "CHEBI:86364",
        "manganese(II) sulfate monohydrate",
    ),
    ("CHEBI:48854", "H2SeO3"): ("CHEBI:26642", "selenous acid"),
    ("CHEBI:86311", "Na WO .2H O"): ("CHEBI:63939", "sodium tungstate dihydrate"),
    ("CHEBI:29033", "Iron(II) sulfate"): ("CHEBI:75832", "iron(2+) sulfate (anhydrous)"),
    # Remaining internal splits whose minority id names an unrelated entity. These
    # targets are independently supported by real ChEBI labels and MIM reviewed rows
    # (direct mappings or asserted synonyms/CAS evidence), never by majority vote.
    ("CHEBI:83760", "D-Trehalose dihydrate"): ("CHEBI:232797", "trehalose dihydrate"),
    ("CHEBI:73605", "KF"): ("CHEBI:66872", "potassium fluoride"),
    ("CHEBI:10642", "m-Inositol"): ("CHEBI:17268", "myo-inositol"),
    ("CHEBI:166917", "m-Inositol"): ("CHEBI:17268", "myo-inositol"),
}

# Full-corpus pre-state reference counts measured immediately before this migration.
# A correction can be wholly present (expected) or wholly absent (already migrated).
# Any intermediate count indicates corpus drift or a partial prior write and aborts a
# full default-directory run before files are changed. Counts are serialized id
# references, not expanded ingredient rows: fifteen records reuse a YAML anchor for a
# second Vitamin B12 row, so changing one anchor definition intentionally fixes both.
EXPECTED_REFERENCE_COUNTS: dict[tuple[str, str, str], int] = {
    ("Vitamin B12", "CHEBI:17439", "CHEBI:176843"): 3976,
    ("EDTA", "CHEBI:64755", "CHEBI:4735"): 1008,
    ("Thiamine", "CHEBI:26948", "CHEBI:18385"): 149,
    ("thiamine", "CHEBI:26948", "CHEBI:18385"): 2,
    ("Citrate", "CHEBI:30769", "CHEBI:16947"): 63,
    ("NiSO4 x 7 H2O", "CHEBI:53001", "CHEBI:53504"): 15,
    ("Sodium glutamate monohydrate", "CHEBI:64243", "CHEBI:232425"): 28,
    ("Starch", "CHEBI:85248", "CHEBI:28017"): 0,
    ("Starch ", "CHEBI:85248", "CHEBI:28017"): 2,
    ("DL-mevalonic acid", "CHEBI:150970", "CHEBI:25351"): 5,
    ("D(+)-Glucose", "CHEBI:15824", "CHEBI:17634"): 13,
    ("Dextrose", "CHEBI:15824", "CHEBI:17634"): 16,
    ("D-Trehalose dihydrate", "CHEBI:83760", "CHEBI:232797"): 1,
    ("KF", "CHEBI:73605", "CHEBI:66872"): 3,
    ("m-Inositol", "CHEBI:10642", "CHEBI:17268"): 20,
    ("m-Inositol", "CHEBI:166917", "CHEBI:17268"): 1,
    ("(NH4)3 citrate", "CHEBI:72699", "CHEBI:63037"): 4,
    ("Citric acid", "CHEBI:53258", "CHEBI:30769"): 54,
    ("D-Arabinose", "CHEBI:46983", "CHEBI:17108"): 4,
    ("D-Fructose", "CHEBI:48095", "CHEBI:15824"): 9,
    ("D-Mannose", "CHEBI:37675", "CHEBI:16024"): 4,
    ("DL-Dithiothreitol", "CHEBI:42106", "CHEBI:18320"): 1,
    ("L-Cysteine", "CHEBI:15356", "CHEBI:17561"): 14,
    ("L-Lysine HCl", "CHEBI:53558", "CHEBI:53633"): 2,
    ("Na-glutamate", "CHEBI:29988", "CHEBI:64220"): 4,
    ("CoCl2 x 6 H2O", "CHEBI:35696", "CHEBI:53503"): 4905,
    ("Na2HPO4 x 2 H2O", "CHEBI:34683", "CHEBI:91258"): 523,
    ("Calcium chloride dihydrate", "CHEBI:3312", "CHEBI:86158"): 4,
    ("Magnesium chloride hexahydrate", "CHEBI:6636", "CHEBI:86345"): 4,
    ("Magnesium sulfate heptahydrate", "CHEBI:32599", "CHEBI:31795"): 4,
    ("MnSO4 x 4 H2O", "CHEBI:86360", "CHEBI:86358"): 12,
    ("MnSO4 x 5 H2O", "CHEBI:86360", "CHEBI:131524"): 2,
    ("VOSO4 x 2 H2O", "CHEBI:33146", "CHEBI:87009"): 9,
    ("VOSO4 x 5 H2O", "CHEBI:33146", "CHEBI:132758"): 3,
    ("VOSO4 x 5 H2O", "CHEBI:87014", "CHEBI:132758"): 1,
    ("Na-thioglycolate", "CHEBI:30066", "CHEBI:86481"): 4,
    ("Na-butyrate", "CHEBI:17968", "CHEBI:64103"): 1,
    ("Na-tartrate", "CHEBI:30924", "CHEBI:63017"): 2,
    ("Dipotassium phosphate", "CHEBI:63036", "CHEBI:131527"): 2,
}


PREFERRED = re.compile(r"^\s*-?\s*preferred_term:\s*(.+?)\s*$")
ID_LINE = re.compile(r"^(\s*)id:\s*(\S+)\s*$")
LABEL_LINE = re.compile(r"^(\s*)label:\s*")


def _unquote(s: str) -> str:
    if len(s) >= 2 and s[0] == s[-1] and s[0] in "'\"":
        return s[1:-1].replace("''", "'") if s[0] == "'" else s[1:-1]
    return s


def validate_mim_reconciliations(sssom_path: Path) -> str:
    """Return the MIM version after proving every exact reconciliation still holds."""
    mappings, version = load_sssom(sssom_path)
    errors: list[str] = []
    for (_old_id, name), expected in sorted(MIM_EXACT_CORRECTIONS.items()):
        observed = mappings.get(normalize_name(name))
        if observed != expected:
            errors.append(f"{name!r}: expected {expected!r}, found {observed!r}")
    if errors:
        raise ValueError(
            "MIM SSSOM no longer supports the approved exactMatch corrections:\n  "
            + "\n  ".join(errors)
        )
    return version


def validate_reference_counts(tally: Counter[tuple[str, str, str]]) -> None:
    """Reject partial or unexpectedly broadened full-corpus migrations."""
    errors: list[str] = []
    for key, expected in EXPECTED_REFERENCE_COUNTS.items():
        observed = tally.get(key, 0)
        if observed not in {0, expected}:
            errors.append(
                f"{key[0]!r} {key[1]} -> {key[2]}: " f"expected 0 or {expected}, found {observed}"
            )
    if errors:
        raise ValueError(
            "Grounding migration count guard failed; no files were written:\n  "
            + "\n  ".join(errors)
        )


def fix_text(text: str) -> tuple[str, list[tuple[str, str, str]]]:
    """Rewrite only the id/label lines that need it, leaving the file otherwise byte-identical.

    A YAML round-trip was the obvious implementation and the wrong one: re-dumping
    reflows every long `notes:` string in the record, so a one-id change arrives as a
    67-line diff and the real edit is invisible in review. This walks lines instead.

    Correction is keyed on the enclosing ingredient's `preferred_term` AND the id, never
    the id alone — CHEBI:86463 is also carried, correctly, by `AlK(SO4)2`. Both the
    `term` block and a `mediaingredientmech_chebi_term` self-link move together; leaving
    the latter on the old id would turn a stale field into a contradictory one.
    """
    lines = text.splitlines(keepends=True)
    out = list(lines)
    changes: list[tuple[str, str, str]] = []
    name = ""
    pending: tuple[str, str] | None = None  # (indent, new_label) for the next label line
    for n, line in enumerate(lines):
        m = PREFERRED.match(line)
        if m:
            name = _unquote(m.group(1))
            pending = None
            continue
        mi = ID_LINE.match(line)
        if mi:
            repl = CORRECTIONS.get((mi.group(2), name))
            pending = None
            if repl:
                new_id, new_label = repl
                out[n] = f"{mi.group(1)}id: {new_id}\n"
                changes.append((name, mi.group(2), new_id))
                pending = (mi.group(1), new_label)
            continue
        if pending:
            ml = LABEL_LINE.match(line)
            if ml and ml.group(1) == pending[0]:
                out[n] = f"{pending[0]}label: {pending[1]}\n"
            pending = None
    return "".join(out), changes


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--apply", action="store_true", help="Write the corpus. Default is a dry run.")
    ap.add_argument("--limit", type=int, default=0, help="Stop after N changed records (canary).")
    ap.add_argument("--yaml-dir", type=Path, default=NORMALIZED)
    ap.add_argument(
        "--sssom",
        type=Path,
        default=DEFAULT_SSSOM,
        help="MIM ingredient SSSOM used to verify exact reconciliations.",
    )
    ap.add_argument(
        "--summary-only",
        action="store_true",
        help="Suppress per-reference output; retain validation and totals.",
    )
    args = ap.parse_args(argv)

    try:
        mim_version = validate_mim_reconciliations(args.sssom)
    except (OSError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    print(
        f"Verified {len(MIM_EXACT_CORRECTIONS)} approved corrections against "
        f"MIM SSSOM {mim_version}."
    )

    tally: Counter[tuple[str, str, str]] = Counter()
    pending: list[tuple[Path, str, list[tuple[str, str, str]]]] = []
    for path in sorted(args.yaml_dir.resolve().rglob("*.yaml")):
        try:
            text = path.read_text(errors="replace")
        except OSError:
            continue
        # Cheap prefilter — the vast majority of records carry neither wrong id.
        if not any(bad in text for bad in {k[0] for k in CORRECTIONS}):
            continue
        new_text, changes = fix_text(text)
        if not changes:
            continue
        # Re-parse defensively: a line-level edit must still leave valid YAML.
        try:
            yaml.safe_load(new_text)
        except yaml.YAMLError as exc:
            print(
                f"  SKIP {path.relative_to(REPO)} — edit would break YAML: {exc}", file=sys.stderr
            )
            continue
        pending.append((path, new_text, changes))
        tally.update(changes)
        if args.limit and len(pending) >= args.limit:
            break

    if not args.limit and args.yaml_dir.resolve() == NORMALIZED.resolve():
        try:
            validate_reference_counts(tally)
        except ValueError as exc:
            print(f"ERROR: {exc}", file=sys.stderr)
            return 2

    # Deliberately write only after SSSOM and count validation: a failed guard must
    # leave the corpus byte-identical, not half-migrated.
    for path, new_text, changes in pending:
        try:
            rel = path.relative_to(REPO)
        except ValueError:
            rel = path  # --yaml-dir may be relative or outside the repo
        if not args.summary_only:
            for name, old, new in changes:
                print(f"  {rel}: {name!r} {old} -> {new}")
        if args.apply:
            path.write_text(new_text)

    print(
        f"\n{'Corrected' if args.apply else 'Would correct'} "
        f"{sum(tally.values())} term reference(s) in {len(pending)} record(s):"
    )
    for (name, old, new), n in tally.most_common():
        print(f"  {n:5d}x  {name!r}  {old} -> {new}")
    if not args.apply:
        print("\nDry run — nothing written. Re-run with --apply.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
