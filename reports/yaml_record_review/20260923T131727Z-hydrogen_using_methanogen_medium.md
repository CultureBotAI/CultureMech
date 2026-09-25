# YAML Record Review: Hydrogen-using methanogen medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/hydrogen_using_methanogen_medium.yaml
- Started UTC: 2026-09-23T13:16:23Z
- Finished UTC: 2026-09-23T13:17:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| ID | CultureMech:008308 |
| Name | hydrogen_using_methanogen_medium |
| Original name | Hydrogen-using methanogen medium |
| Class | MediaRecipe |
| Category | archaea |
| Medium type | COMPLEX |
| Composition type | UNDEFINED |
| Physical state | LIQUID |
| Source identity | TOGO Medium M1745; original source NBRC Medium 955 |
| Generated path reviewed | data/merge_yaml/merged/hydrogen_using_methanogen_medium.yaml |
| Maintained owner | data/normalized_yaml/archaea/hydrogen_using_methanogen_medium.yaml |

This review targeted the generated merged record. It is produced from
`data/normalized_yaml/archaea/hydrogen_using_methanogen_medium.yaml`;
future fixes should update that normalized source, any repeated TOGO import
logic that created the same stock-solution flattening, and then regenerate
`data/merge_yaml/merged/`.

## Validation

| Check | Result |
|---|---|
| Open LinkML validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/hydrogen_using_methanogen_medium.yaml` | Passed; no issues found. |
| Strict validation, `python scripts/validate_strict.py data/merge_yaml/merged/hydrogen_using_methanogen_medium.yaml --out /private/tmp/hydrogen_using_methanogen_medium.strict.tsv --workers 1 --quiet` | Passed; the TSV contained the header and zero ERROR rows. |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/hydrogen_using_methanogen_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with zero reference checks. |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/hydrogen_using_methanogen_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the documented `just validate-history` entry point validates standalone YAML under `history/`, not embedded MediaRecipe history arrays. |

The focused validators used Python 3.11 and the offline uv cache because the
project-level uv solve attempts to build `llvmlite==0.46.0` under Python 3.13
and currently fails in setuptools before reaching these data checks.

## Identity and Grounding

- The record identity is resolved and singular: `CultureMech:008308` names
  `hydrogen_using_methanogen_medium`, and the `media_term` is `TOGO:M1745`
  with label Hydrogen-using methanogen medium.
- The `notes` field ties TOGO M1745 to NBRC Medium 955, and the live TOGO
  payload for M1745 is the same NBRC formulation.
- A gitignore-independent slug search over `data/normalized_yaml`,
  `data/merge_yaml/merged`, and `reports/import_tracking` found this record's
  maintained normalized input and TOGO-owned plausibility rows for
  `CultureMech:008308`.
- A gitignore-independent exact-title search over `data/raw/togo` and
  `data/raw/nbrc` found only raw-data README scaffolding and no checked-in
  source payload for this medium.
- The ingredient-level CHEBI grounding is mixed. The main medium's hydrated
  `MgSO4 x 7H2O`, `CaCl2 x 2H2O`, `Na2S x 9H2O`, and
  `Fe(NH4)2(SO4)2 x 6H2O` rows are grounded to exact hydrated terms, and
  several trace/vitamin rows are exact. `CoCl2 x 6H2O` and `NiCl2 x 6H2O`
  are grounded to generic cobalt dichloride and nickel dichloride even though
  the inspected stock recipe specifies the hexahydrates; `Ca-pantothenate` is
  grounded to pantothenate rather than the calcium salt.

## Evidence

- The source identity is supported by the inspected TOGO M1745/NBRC 955
  formulation.
- The main soluble ingredients and gram-per-liter rows match the source for
  magnesium sulfate heptahydrate, calcium chloride dihydrate, potassium
  dihydrogen phosphate, ammonium chloride, magnesium chloride hexahydrate,
  sodium sulfide nonahydrate, potassium chloride, sodium bicarbonate, sodium
  acetate, yeast extract, cysteine-HCl, and Hipolypepton.
- The record keeps pH-adjustment and headspace gases as variable ingredients,
  but the reviewed YAML has no structured preparation context stating that
  NaOH adjusts the premix to pH 6.5, the vessels are dispensed under H2/CO2
  80/20, separate cysteine-HCl and sulfide solutions are autoclaved under N2,
  vitamin and 8% sodium bicarbonate solutions are filter-sterilized and added
  anaerobically, inoculated vessels are pressurized to 150 kPa with H2/CO2,
  and the final pH is adjusted to 6.8-7.0.
- The two source stock solutions are not evidence for final-medium trace and
  vitamin ingredients at their stock concentrations. TOGO M1745 adds 10 ml of
  `Trace elements solution*` and 10 ml of `Vitamin solution**` per liter of
  final medium; the generated YAML also emits every member of those 1 L stock
  recipes as a top-level final-medium ingredient.
- The synthetic solution links are not supported by the inspected TOGO source.
  The local TOGO stocks are M1745-specific `Trace elements solution*` and
  `Vitamin solution**`; the generated `mediadive.solution:6129` and
  `mediadive.solution:6241` CURIEs point to same-label MediaDive stock records
  rather than the local M1745 stock definitions.

## Completeness

- The reviewed YAML lacks the source preparation protocol and therefore drops
  the anaerobic dispensing, gas ratios, gas pressure, pH-adjustment points,
  sterilization boundaries, and post-autoclave addition instructions needed to
  make NBRC 955.
- The stock-solution structure is incomplete. The source has one final medium,
  one trace-elements stock, and one vitamin stock; the record has two empty
  stock references plus flattened, undiluted stock members as final-medium
  ingredients.
- Concentrations from milligram source rows are incomplete or dimensionally
  wrong: resazurin is 1 mg/L in the final medium but appears as 1 g/L,
  ferrous ammonium sulfate hexahydrate is 2 mg/L but appears as 2 g/L, and the
  vitamin stock's mg/L rows appear as g/L final-medium rows before applying
  the 10 ml/L dilution.
- Duplicate merging crossed stock/final boundaries. The generated water row is
  `3.0 G_PER_L` after combining water from the final medium, trace stock, and
  vitamin stock; calcium chloride dihydrate is `0.24000000000000002 G_PER_L`
  after summing the 0.14 g/L final row with the 0.1 g/L undiluted trace-stock
  row.
- A gitignore-independent exact-title search covered `data/raw/togo` and
  `data/raw/nbrc` and did not find a checked-in raw NBRC/TOGO response that
  could document the payload version used for the current import.
- Empty optional fields such as synonyms, organisms, and external literature
  references are not defects for this imported source recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | M1745 local stock solutions are flattened into top-level final-medium ingredients at stock strength. | TOGO M1745 adds 10 ml each of `Trace elements solution*` and `Vitamin solution**`, but the YAML lists their member compounds as direct ingredients and leaves two empty `solutions` references. | `data/normalized_yaml/archaea/hydrogen_using_methanogen_medium.yaml`; repeated flattening should also be traced in the TOGO import or solution migration path. |
| Major | Several source milligram quantities are represented as grams per liter. | The TOGO final medium has resazurin at 1 mg and ferrous ammonium sulfate hexahydrate at 2 mg per liter, while the YAML records 1 and 2 `G_PER_L`. Vitamin stock rows such as biotin 2 mg and pyridoxine-HCl 10 mg are likewise emitted as 2 and 10 `G_PER_L` rows after stock flattening. | `data/normalized_yaml/archaea/hydrogen_using_methanogen_medium.yaml`; the TOGO quantity/unit conversion should be audited for `mg` rows. |
| Major | Duplicate merging combines chemically identical rows across incompatible solution boundaries. | Water from three 1 L recipes became a single `3.0 G_PER_L` ingredient, and final calcium chloride dihydrate plus undiluted trace-stock calcium chloride dihydrate became `0.24000000000000002 G_PER_L`. | `data/normalized_yaml/archaea/hydrogen_using_methanogen_medium.yaml`; generated duplicate cleanup and merge scripts should preserve final-medium and local-stock scope. |
| Major | The two `solutions` CURIEs are unsupported for this source. | M1745 defines local TOGO trace and vitamin stocks; it does not cite `mediadive.solution:6129` or `mediadive.solution:6241`. | `data/normalized_yaml/archaea/hydrogen_using_methanogen_medium.yaml` and the solution migrator that assigned generic MediaDive same-label links. |
| Major | Preparation evidence is omitted. | The inspected source includes anaerobic H2/CO2 dispensing, N2 handling of reducing-agent stocks, filter sterilization of vitamin and bicarbonate stocks, 150 kPa H2/CO2 pressurization, and pH adjustments; none are represented in the YAML. | `data/normalized_yaml/archaea/hydrogen_using_methanogen_medium.yaml`; TOGO/NBRC importer needs a structured home for comments. |
| Minor | Some ingredient groundings lose exact hydrated or salt form. | The source labels are `CoCl2 x 6H2O`, `NiCl2 x 6H2O`, and `Ca-pantothenate`, while the YAML grounds them to generic cobalt dichloride, generic nickel dichloride, and pantothenate. | `data/normalized_yaml/archaea/hydrogen_using_methanogen_medium.yaml`; CHEBI enrichment mappings for hydrate and calcium pantothenate labels should be reviewed. |

## Recommended Edits

1. Rebuild the source-owned M1745 normalized record so final-medium
   ingredients contain only the NBRC 955 main recipe rows plus two stock
   additions: 10 ml/L `Trace elements solution*` and 10 ml/L
   `Vitamin solution**`.
2. Represent the local trace-elements and vitamin solution compositions as
   nested source-specific stock solutions, preserving their 1 L water rows,
   mg and g units, and the trace-stock instruction to dissolve NTA, adjust to
   pH 6.5 with NaOH, then add minerals to final pH 7.0.
3. Correct the milligram unit slips for final-medium resazurin and ferrous
   ammonium sulfate hexahydrate, and for every vitamin-stock milligram row
   after the stock boundary is restored.
4. Remove the unsupported `mediadive.solution:6129` and
   `mediadive.solution:6241` references unless a future source-specific
   reconciliation proves those MediaDive solutions are exact equivalents of
   TOGO M1745's local stocks.
5. Capture the NBRC preparation comments in the normalized record, including
   pH 6.5 before dispensing, H2/CO2 80/20 anaerobic dispensing, separate
   reducing-agent autoclaving under N2, filter sterilization of vitamin and 8%
   sodium bicarbonate stocks, anaerobic post-autoclave additions, 150 kPa
   H2/CO2 after inoculation, and final pH 6.8-7.0.
6. Re-ground hydrated cobalt chloride and nickel chloride, and re-check
   calcium pantothenate, against exact CHEBI terms where available.
7. Rerun the merge recipe generator so
   `data/merge_yaml/merged/hydrogen_using_methanogen_medium.yaml` is derived
   from the corrected normalized record rather than patched directly.

## Follow-up Checks

- Rerun open LinkML, strict, reference, and term validation for the regenerated
  merged record.
- Manually compare every final-medium row and every member of both local
  stocks against TOGO M1745/NBRC 955; the stock members should not appear as
  direct final-medium ingredients unless represented as nested stock members.
- Verify the regenerated `solutions` entries use source-specific identifiers
  or unresolved local labels for the M1745 stocks instead of generic
  same-label MediaDive solution CURIEs.
- Inspect `reports/import_tracking/plausibility.tsv` for
  `CultureMech:008308`; its current unit-slip flags cover resazurin, vitamin
  rows, and the trace-stock ferric chloride row, but they did not flag the
  final-medium ferrous ammonium sulfate 2 mg to 2 g/L unit slip.
- Re-run the duplicate merge step on this record and verify water, calcium
  chloride dihydrate, and NaOH are not merged across final-medium,
  trace-stock, and vitamin-stock scopes.

## Additional Notes

- The generated record and maintained normalized input already differ on the
  water row: the normalized input still collapses three 1 L waters to
  `1.0 G_PER_L`, while the merged output rewrites the same row to `3.0`.
  Both forms are artifacts of losing the source stock boundaries.
- No raw TOGO or NBRC response is checked in under `data/raw/togo` or
  `data/raw/nbrc`; the local raw directories only contain README scaffolding.
