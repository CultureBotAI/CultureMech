# Next M142-Dependent Records

Triage only. None of these 98 receiving records was edited or counted as
reviewed by this capture. The J261/M253 cohort is separate.

## Frozen Inputs

- `next-m142-dependents-context.json`: full baseline YAML and 98 official
  receiving-source TOGO JSON responses, plus previously captured M142/JCM151.
  SHA256 `39372f9bc9386b16d45442f1ec055663688a1fe230d6b5d848bd2c76b1c2d668`.
- `next-m142-dependents-triage.json`: exact stock-node/source-row mapping and
  preparation/variant context; no numeric proposals.
  SHA256 `e71ac1b6dac2d465dc72bc23820096bd01fb7343332be8dd4e73f0d6ad821b84`.
- `next-m142-originals.json`: all 96 distinct referenced original JCM pages
  returned HTTP 200. Eighty contain recipe text; 16 say `Nothing found.`
  SHA256 `8b6efa967e5c9c5c4d11be140d7c9905e48f5f3b4effda1549514ad70889c5f7`.

Each source has its URL, response URL, access timestamp, encoding and raw
payload SHA256. All 98 baseline hashes were checked again after capture.
The initial dependency search included ignored and hidden files. Selection
uses exact tracked paths still outside current follow-up coverage; M253 is
excluded because its new curation is already reported.

## Source Mapping

All 101 named M142 stock references have exactly one matching receiving-source
row and an explicit `reference_media_id: M142`. Source amounts use 91 `ml`
and ten `L` entries, not mass units. This proves a unit problem in the old
records, but not a universal replacement dose or preparation stage.

- 83 rows occur in a `main solution 1` section: candidate batch-input repairs,
  still requiring the full preparation and every variant override to be read.
- 16 rows occur in nested/later sections: do not leave them as root inputs
  or assume their amount is per final liter.
- Two rows occur in a first section named `Solution A`, also requiring
  separate preparation scope.
- Twelve records have explicit base-medium variant instructions.
- Four have explicit volume-making instructions; those establish the volume
  at that stage, not automatically after all later supplements.
- Forty-four have per-liter wording, including the source typo `per litter`.
  Its association with a specific later table must be checked, not propagated
  across every stock or ingredient in the record.

These are textual triage flags, not an exhaustive semantic review. Read the
whole source and current YAML before applying; no reported absence of a flag
proves absence of a scientific condition.

## Verified Consequential Examples

The following original pages and corresponding TOGO tables were read after
capture; the other captures are review inputs, not asserted complete reviews.

- **M689 / JCM670:** the original main batch has 1 L water and direct masses.
  A later instruction adds FeCl2 stock 10 mL, trace-element stock 10 mL,
  M142 trace minerals **25 mL**, and vitamins 10 mL **per liter**. For that
  trace-mineral dose, `25 ML_PER_L` is supported, not `0.025 L` per batch.
  The receiving-source paragraph and table must accompany the amount evidence.
- **M933 / JCM892:** main medium receives 1 L modified synthetic seawater.
  That seawater stock receives 10 mL modified trace-mineral solution. The
  latter is made from **1 L M142 trace minerals** plus nickel and selenium
  additions. The 1 L M142 quantity is an internal stock input, not a medium
  dose. Preserve both nesting levels and additional constituents.
- **M196 / JCM203:** salt-base 1 L and trace minerals 10 mL are main batch
  inputs. The later 5% sulfide solution is **10 mL per liter**, and its percent
  basis remains unspecified. TOGO's main row repeats this later addition;
  do not double-count it. TOGO says `H2-CO4` in one preparation sentence while
  the original JCM page says `H2-CO2`: preserve/correct with explicit evidence,
  not an unrecorded typo replacement.
- **M197 / JCM204:** JCM203 variant with final yeast extract 0.2 g/L.
- **M198 / JCM205:** JCM203 variant with final yeast extract 0.5 g/L and
  sodium tungstate dihydrate 0.1 mg/L; explicitly omits citric acid. Do not
  infer that the parent has citric acid merely from the omission instruction.
- **M274:** TOGO accession `JCM_M280-2` points to original page 280. That
  page includes a conditional maltodextrin/sulfur-omission comment. The TOGO
  rows explicitly include maltodextrin 5 g/L and omit sulfur, but its copied
  preparation still adds sulfur: this is another override repair, not an
  exact base duplicate. Its FeSO4 heptahydrate row says 0.025 g while the
  original JCM280 table says 2.5 mg, a tenfold source-amount discrepancy.
  Preserve and adjudicate that discrepancy before asserting a concentration.
- **M1257:** accession `JCM_M1173-2` shares its original page with M1256;
  that page currently says `Nothing found.` Its TOGO rows include agar
  15 g/L and the solid-medium instruction, plus a separately listed 50% (v/v)
  methanol addition. Retain this explicit physical-state variant and known
  percent basis; do not infer a missing final preparation volume.

## Missing Original Pages

The following original accessions returned HTTP 200 but no recipe: JCM399,
400, 401, 688, 703, 728, 792, 856, 882, 955, 1042, 1159, 1173, 1278, 1279,
1297. They affect 17 receiving records because JCM1173 serves two wrappers.
Their TOGO captures remain available; do not claim original-source
corroboration for them or replace their formulations with neighboring recipes.

## Next Work

Use this inventory to drive a larger source-mapped cohort, retaining separate
handling for nested stocks, final-rate variants and later per-liter additions.
Review every ingredient and stock field of each selected record, including
unresolved fields; updating an M142 reference alone does not complete a record.
Preserve existing evidence and annotations, scope new evidence at the changed
node, preview and independently audit the full source projection, then apply
with identity/hash guards and append-only history. Reuse the M142 definitions
only where the receiving source explicitly references that stock.

The all-record goal remains active. Publication, citation-gate repairs,
stale merged outputs and the requested GitHub workflow remain unfinished.
