# Fourth Medium Pass: Source-Scope Findings

Four preliminary candidates are withheld, not repaired by this evidence-only
batch. Source API tables and preparation text were inspected, and each original
PDF below was downloaded and visually inspected in full on 2026-10-07 (one page
each). Discovery mode: existing record reference; source type: official
culture-collection recipe. Individual authors are not supplied. Footer copyright
years are not asserted as publication dates.

## DSMZ 1431: Carbonate Depends on Physical State

- Follow-up target: `data/normalized_yaml/archaea/alkalophilic_halophile_medium.yaml`
- ID: `CultureMech:000255`; local state: `SOLID_AGAR`.
- Source: [1431. ALKALOPHILIC HALOPHILE MEDIUM](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1431.pdf), page 1, preparation paragraph.
- Exact excerpt: "Agar (2%) medium should be prepared without Na2CO3".
- PDF SHA256: `b099bd697bec33fc11578ae2d6bae5b4b02148b370e5f6cc0972d3c3e650d514`.

The table's carbonate amount is not the agar preparation's carbonate dose. The
paragraph replaces that preparation with a variable volume of sterile carbonate
stock, adjusted to pH. The PDF supplies no explicit batch-water or final-volume
statement. Neither an unspecified percentage basis nor final concentration is
inferred. Nine preliminary evidence claims are withheld pending a source-backed
liquid/solid formulation repair; existing amounts are unchanged.

## DSMZ 1462: Agar Omits Supplemental Calcium

- Follow-up target: `data/normalized_yaml/bacterial/caulobacter_pye_medium.yaml`
- ID: `CultureMech:000928`; local state: `SOLID_AGAR`.
- Source: [1462: CAULOBACTER PYE MEDIUM](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1462.pdf), page 1, step 1.
- Exact excerpt: "For agar media, do not add supplemental calcium."
- PDF SHA256: `80e3039e10927cd0d93a550e94ab638801319668f81325e7959828d342bbc535`.

The current record combines agar with the table's calcium chloride amount despite
the explicit omission. Both preliminary claims are withheld; adding support to
the calcium amount would be false for this solid formulation. A later repair must
represent the liquid/agar distinction, not simply remove a number while leaving
unconditional calcium presence. No ingredient or concentration is changed here.

## DSMZ 1624: Base Volume Is Not Complete-Medium Volume

- Follow-up target: `data/normalized_yaml/bacterial/methylophaga_muralis_medium.yaml`
- ID: `CultureMech:001105`; local state: `LIQUID`.
- Source: [1624. METHYLOPHAGA MURALIS MEDIUM](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1624.pdf), page 1, table and preparation paragraph.
- Exact excerpt: "100 ml/l 1M sterilized NaHCO3 and 10 ml/l 1M sterilized".
- PDF SHA256: `5325458b4740df7658a738fab208e5b41e7b74a51e8bbf50f59cae989829804b`.

The table supplies an 890 mL mineral-base water amount. Later carbonate stocks
and methanol are specified only in prose; the current ingredients omit them.
API values normalized to 0.89 L cannot establish concentrations in the complete
medium. Four preliminary claims are withheld. Stock boundaries, addition doses,
physical-state branches, and the final-volume basis require repair; neither a
1 L nor 1.005 L final volume is asserted here.

## DSMZ 1641: Repeated Pyruvate Names

- Follow-up target: `data/normalized_yaml/bacterial/double_concentrated_830_0_06_sodium_pyruvate.yaml`
- ID: `CultureMech:001126`.
- Source: [1641. DOUBLE CONCENTRATED 830 + 0.06% SODIUM PYRUVATE](https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1641.pdf), page 1, ingredient table.
- Separate exact table excerpts: "Na-pyruvate" and "Sodium pyruvate".
- PDF SHA256: `d8051ee7cb3707a52247550d205d37dfc5bf119995344ed70c94597a47aab31c`.

Both source rows carry 0.60 g, as do their API rows; both local ingredients share
one sodium-pyruvate identifier. The original table really contains both rows, so
this is not merely an importer duplication. Eight preliminary claims are withheld
until the intended combined formulation is established. Do not choose between a
single 0.6 g amount and two additive amounts from the title or synonym matching.

## Guard Scope and Earlier Batches

The new guards identify these explicit preparation patterns and potential aliases;
they are not a general natural-language proof of formulation correctness. Tests
include liquid-state and separate-sterilization controls. The alias guard covers
unconditional, unattributed source rows; optional or branded rows already require
separate review and are not declared equivalent merely because of an ontology ID.

All 419 previously accepted medium records were checked against the new guards.
The preflight records the result. A broader shared-ID scan also found DSMZ 550:
its branded Czapek Dox agar mixture shares a local agar ID, but the source names
the mixture and added agar separately. The mixture had no newly accepted amount
claim. Its secondary identity mapping remains unresolved; prior scoped evidence
for the separately named ingredients is not rewritten or propagated to it.
