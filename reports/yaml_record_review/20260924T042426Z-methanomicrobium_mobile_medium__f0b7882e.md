# YAML Record Review: Methanomicrobium Mobile Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanomicrobium_mobile_medium__f0b7882e.yaml
- Started UTC: 2026-09-24T04:23:03Z
- Finished UTC: 2026-09-24T04:24:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:009157 |
| Name | methanomicrobium_mobile_medium |
| Original name | Methanomicrobium Mobile Medium |
| Category | archaea |
| Media term | TOGO:M258 |
| Source | TOGO M258 / JCM M266 |
| Generated path reviewed | data/merge_yaml/merged/methanomicrobium_mobile_medium__f0b7882e.yaml |
| Canonical owner | data/normalized_yaml/archaea/TOGO_M258_Methanomicrobium_Mobile_Medium.yaml |

The reviewed file is a generated merge of one TOGO owner. It preserves JCM
Medium 266 identity, but the owner is contaminated with unsupported LB Medium
constituents and has the local rumen-fluid and fatty-acid stock rows flattened
into the final medium.

## Validation

| Check | Result |
|---|---|
| Open LinkML schema | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanomicrobium_mobile_medium__f0b7882e.yaml` exited 0 with no diagnostics. |
| Strict validator | Passed; `scripts/validate_strict.py data/merge_yaml/merged/methanomicrobium_mobile_medium__f0b7882e.yaml --out /private/tmp/methanomicrobium_mobile_medium__f0b7882e.strict.tsv --workers 1 --quiet` reported 0 error rows. |
| Reference validator | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/methanomicrobium_mobile_medium__f0b7882e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` performed 0 reference checks and passed. |
| Term validator | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/methanomicrobium_mobile_medium__f0b7882e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/` YAML, not embedded `MediaRecipe.curation_history` entries in merged records. |

## Identity and Grounding

- **The source identity is correct.** TOGO M258 and the live JCM `GRMD=266`
  page both identify the recipe as `METHANOMICROBIUM MOBILE MEDIUM`.
- **Three ingredient rows are from an unrelated LB decomposition.** Tryptone,
  a generic 5 g/L Yeast extract row, and a generic 10 g/L Sodium chloride row
  are marked as constituents of LB Medium and are not in TOGO M258 or JCM 266.
- **The M258-local stocks are not represented.** Rumen fluid and the fatty-acid
  mixture are local subrecipes in JCM 266; the YAML hoists some of their rows
  into top-level ingredients and leaves a duplicate variable rumen-fluid row.
- **Shared JCM stocks are only empty placeholders.** The 10 ml Trace minerals
  and Trace vitamins additions are carried as empty `Unknown solution` entries
  with `G_PER_L` units.
- **Source units are partly broken.** CaCl2 x 2H2O and FeSO4 x 7H2O are mg
  rows in the source, but appear as 8 and 2 `G_PER_L`.

## Evidence

### Supported by inspected sources

- TOGO M258 and JCM 266 support 300 ml clarified rumen fluid, 660 ml distilled
  water, MgSO4 x 7H2O, NaCl, 8 mg CaCl2 x 2H2O, KH2PO4, K2HPO4, 1 mg
  resazurin, Na2S x 9H2O, 2 mg FeSO4 x 7H2O, NaHCO3, ammonium sulfate, 1 g
  Yeast extract from BD-Difco, 1 g Trypticase peptone from BD-BBL, 0.5 g
  L-Cysteine HCl H2O, 10 ml trace minerals, 10 ml trace vitamins, and 20 ml
  fatty-acid mixture.
- TOGO M258 supports the rumen-fluid stock recipe and the fatty-acid stock made
  with 20 ml water, 0.5 g each of valeric acid, isovaleric acid,
  2-Methylbutyric acid, and isobutyric acid, then adjusted to pH 7.5 with
  concentrated NaOH.
- JCM 266 supports the current stock references for trace minerals and trace
  vitamins as JCM Medium 151 and JCM Medium 197, while the TOGO snapshot
  preserves the corresponding TOGO reference IDs M142 and M190.
- JCM 266 supports the anaerobic preparation: mix without NaHCO3, cysteine, and
  sulfide; adjust pH to 6.5; boil briefly; cool under H2-CO2 80:20; add
  NaHCO3; dispense under the same gas; seal with butyl stoppers; autoclave;
  stand overnight; separately autoclave 5 percent cysteine and sulfide stocks
  under N2; aseptically and anaerobically add them before inoculation; and
  pressurize inoculated bottles to 200 kPa H2-CO2 80:20.

### Unsupported or over-scoped in the YAML

- The LB-derived Tryptone, generic Yeast extract, and 10 g/L Sodium chloride
  rows are unsupported by TOGO M258 and JCM 266.
- 8 mg CaCl2 x 2H2O, 2 mg FeSO4 x 7H2O, 1 mg resazurin, 300 ml rumen fluid,
  20 ml fatty-acid mixture, 20 ml fatty-acid water, and both 10 ml shared stock
  additions are represented as `G_PER_L`.
- The source 660 ml main-solution water and 20 ml fatty-acid stock water are
  collapsed to one 680 `G_PER_L` top-level water row.
- The fatty-acid mixture is flattened; 2-Methylbutyric acid is missing
  entirely.
- Preparation instructions are absent even though both TOGO and JCM preserve
  the anaerobic main-medium steps, rumen-fluid handling, and fatty-acid pH
  adjustment.

## Completeness

- **Unsupported LB constituents must be removed.** JCM 266 uses 1 g/L
  Trypticase peptone and 1 g/L Yeast extract; it does not call for LB Medium,
  Tryptone, a generic extra 5 g/L Yeast extract, or a generic extra 10 g/L
  Sodium chloride.
- **Three stock/subrecipes are incomplete.** Rumen fluid, fatty-acid mixture,
  Trace minerals, and Trace vitamins need scoped additions rather than flattened
  or empty top-level rows.
- **One fatty acid is missing.** The source fatty-acid mixture contains
  2-Methylbutyric acid in addition to valeric, isovaleric, and isobutyric acid.
- **Preparation is missing.** The record does not represent anaerobic gas,
  butyl-stopper sealing, separate cysteine and sulfide stocks, overnight
  standing, inoculation overpressure, rumen-fluid processing, or the fatty-acid
  pH 7.5 adjustment.
- **Bounded local search.** A gitignore-independent search for
  `TOGO_M258_Methanomicrobium_Mobile_Medium`, `JCM_M266`, and
  `Methanomicrobium Mobile Medium` under `data/normalized_yaml` and
  `data/merge_yaml/merged` found only this maintained owner, generated indexes,
  and the reviewed generated record.
- Empty target-organism and growth-evidence sections are not defects for this
  provider recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Three LB Medium constituent rows were appended without source support. | TOGO M258 and JCM 266 do not list LB Medium or its Tryptone, generic Yeast extract, and 10 g/L NaCl constituents. | `data/normalized_yaml/archaea/TOGO_M258_Methanomicrobium_Mobile_Medium.yaml` |
| Major | Several source amounts use the wrong unit dimension. | CaCl2 x 2H2O is 8 mg, FeSO4 x 7H2O is 2 mg, resazurin is 1 mg, rumen fluid is 300 ml, fatty-acid mixture is 20 ml, and shared stocks are 10 ml; the YAML records those amounts as `G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M258_Methanomicrobium_Mobile_Medium.yaml` and import unit handling |
| Major | Rumen fluid and fatty-acid mixture topology was lost. | The source has a local rumen-fluid preparation and a local 20 ml fatty-acid stock addition; the YAML flattens stock rows and collapses main water with fatty-acid water. | `data/normalized_yaml/archaea/TOGO_M258_Methanomicrobium_Mobile_Medium.yaml` and solution migration |
| Major | 2-Methylbutyric acid is missing from the fatty-acid mixture. | JCM 266 and TOGO M258 include 0.5 g 2-Methylbutyric acid in the fatty-acid mixture; the YAML only retains valeric, isovaleric, and isobutyric acid. | `data/normalized_yaml/archaea/TOGO_M258_Methanomicrobium_Mobile_Medium.yaml` |
| Major | Trace minerals and vitamins are empty addition placeholders. | The source adds 10 ml of each referenced stock, but the YAML has empty `Unknown solution` entries with `10 G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M258_Methanomicrobium_Mobile_Medium.yaml` |
| Major | JCM preparation instructions are absent. | TOGO and JCM both preserve staged anaerobic preparation, separate reducer stocks, rumen-fluid preparation, fatty-acid pH adjustment, and post-inoculation H2-CO2 overpressure; the YAML has no `preparation_steps`. | `data/normalized_yaml/archaea/TOGO_M258_Methanomicrobium_Mobile_Medium.yaml` |

## Recommended Edits

1. Remove the unsupported LB Medium constituent rows and their supplier
   metadata from the TOGO M258 owner.
2. Restore source units for the mg rows, ml stock additions, and 660 ml main
   water.
3. Rebuild local `Rumen fluid, clarified` and `Fatty acid mixture` subrecipes
   instead of flattening them into top-level ingredients.
4. Add 2-Methylbutyric acid to the fatty-acid mixture.
5. Expand or correctly link Trace minerals from TOGO M142 and Trace vitamins
   from TOGO M190, preserving the 10 ml addition volumes.
6. Add the JCM anaerobic preparation, reducer-stock preparation, rumen-fluid
   preparation, fatty-acid pH adjustment, and 200 kPa H2-CO2 pressurization
   instructions.

## Follow-up Checks

- Re-run schema, strict, term, and reference validation on
  `data/normalized_yaml/archaea/TOGO_M258_Methanomicrobium_Mobile_Medium.yaml`
  and the regenerated merged record.
- Manually compare the regenerated YAML with TOGO M258 and JCM 266 to confirm
  no LB Medium constituents remain and all stock additions stay scoped.
- Confirm generated output contains no `Unknown solution` placeholders for
  Trace minerals or Trace vitamins.

## Additional Notes

- The same short medium name also appears in DSMZ/MediaDive, JCM/MediaDive, and
  KOMODO-derived records. This report is scoped to the TOGO M258 / JCM M266
  generated output.
