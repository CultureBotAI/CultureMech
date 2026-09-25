# YAML Record Review: NATRONOLIMNOBIUS AHT32 MEDIUM (A)

- Repository: CultureMech
- Record: data/merge_yaml/merged/natronolimnobius_aht32_medium_a__2198131f.yaml
- Started UTC: 2026-09-24T16:52:22Z
- Finished UTC: 2026-09-24T16:52:23Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:003235` for direct MediaDive/JCM J887, `NATRONOLIMNOBIUS AHT32 MEDIUM (A)`.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to MediaDive/JCM J887 for `NATRONOLIMNOBIUS AHT32 MEDIUM (A)`.

An exact repository search including ignored and hidden files for `TOGO:M928`, `CultureMech:010349`, `CultureMech:003235`, `GRMD=887`, `mediadive.medium:J887`, `JCM_M887`, and `natronolimnobius_aht32_medium_a` found this direct JCM generated record plus its normalized owner and an active TOGO M928 generated import of the same JCM medium.

`NiCl2 x 6 H2O` is grounded to generic nickel dichloride.

## Evidence

The recoverable MediaDive J887 record stores 190 g Na2CO3, 30 g NaHCO3, 16 g NaCl, and 2 g K2HPO4 in its `Basal minerals` recipe and places those same components before a 1.0 L basal-mineral preparation step.

The same provider record lists per-liter post-decant additions of 10 ml trace vitamins, 1 ml 4 M NH4Cl, 1 ml selenite-tungstate solution, 1 ml Trace element solution SL-4, 1 ml 1 M MgSO4, 0.2 ml 10% yeast extract, 20 ml 1 M sodium butyrate, and 20 ml 1 M sodium acetate.

MediaDive also represents Trace element solution SL-4 as a 1 L stock with 0.5 g EDTA, 0.2 g FeSO4 x 7 H2O, 100 ml Trace element solution SL-6, and 900 ml distilled water.

The generated record preserves the JCM preparation text about autoclaving, waiting three days, decanting, aseptic additions, and replacing the headspace with N2 containing 5% O2.

## Completeness

The generated record keeps only Selenite-tungstate solution as a solution wrapper, and that wrapper is empty.

Trace vitamins, NH4Cl, MgSO4, yeast extract, sodium butyrate, sodium acetate, and all SL-4 or SL-6 rows are flattened into direct ingredients.

## Findings

- Major: The basal Na2CO3, NaHCO3, NaCl, and K2HPO4 amounts were scaled against an internal 54 ml MediaDive stock volume, producing 3518.52, 555.556, 296.296, and 37.037 `G_PER_L` instead of the source 190, 30, 16, and 2 g in a 1 L basal recipe.
- Major: Per-liter milliliter stock additions were flattened into gram-per-liter ingredients, losing the 10 ml, 1 ml, 0.2 ml, and 20 ml final addition volumes and the 10%, 4 M, and 1 M stock strengths.
- Major: Trace element solution SL-4 was flattened into EDTA, FeSO4, and internal SL-6 ingredients; the source's 1 ml SL-4 addition, 100 ml SL-6 sub-stock addition, and 900 ml SL-4 water volume are absent.
- Major: Selenite-tungstate solution is an empty `Unknown solution`.
- Major: The direct JCM/MediaDive J887 owner is unlinked from the active TOGO M928 import for the same JCM medium.
- Minor: `NiCl2 x 6 H2O` is grounded to generic nickel dichloride.

## Recommended Edits

- In `data/normalized_yaml/archaea/natronolimnobius_aht32_medium_a.yaml`, restore basal mineral amounts as source masses in a 1 L basal preparation rather than concentrations normalized to 54 ml.
- Represent trace vitamins, 4 M NH4Cl, selenite-tungstate, SL-4, 1 M MgSO4, 10% yeast extract, 1 M sodium butyrate, and 1 M sodium acetate as post-decant milliliter additions.
- Preserve the nested SL-4 and SL-6 stock-solution boundary instead of flattening SL-6 salts into the final medium.
- Resolve the selenite-tungstate and trace-vitamin references to structured stock recipes or explicit internal media links.
- Link or collapse the direct JCM/MediaDive J887 owner with TOGO M928.
- Re-ground `NiCl2 x 6 H2O` to an exact hydrate term where one is available, or document it as unresolved.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/natronolimnobius_aht32_medium_a__2198131f.yaml` and verify Na2CO3, NaHCO3, NaCl, and K2HPO4 are no longer normalized to a 54 ml stock.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored and hidden files for `TOGO:M928`, `mediadive.medium:J887`, and `GRMD=887` to verify the duplicate source records are linked or collapsed.

## Additional Notes

The live JCM `GRMD=887` page returned `Nothing found`; this review used the inspected TOGO M928 and MediaDive J887 provider records as recoverable source views for that original JCM medium.
