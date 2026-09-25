# YAML Record Review: Natronolimnobius AHT32 Medium (A)

- Repository: CultureMech
- Record: data/merge_yaml/merged/natronolimnobius_aht32_medium_a.yaml
- Started UTC: 2026-09-24T16:51:18Z
- Finished UTC: 2026-09-24T16:51:19Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:010349` for TOGO M928, a JCM M887 import of `Natronolimnobius AHT32 Medium (A)`.

## Validation

Open schema validation passed with no issues.

Strict validation passed with 0 errors; the strict TSV contained only the header row.

Reference validation passed with 0 checks.

Term validation passed.

Embedded `curation_history` was not checked: `just validate-history` validates the standalone `history/` tree, not `MediaRecipe.curation_history` inside merged generated YAML.

## Identity and Grounding

The record is grounded to TOGO M928 for original media ID `JCM_M887`.

An exact repository search including ignored and hidden files for `TOGO:M928`, `CultureMech:010349`, `CultureMech:003235`, `GRMD=887`, `mediadive.medium:J887`, `JCM_M887`, and `natronolimnobius_aht32_medium_a` found this TOGO M928 generated record plus its normalized owner and an active direct MediaDive/JCM J887 owner for the same medium.

The gas row for nitrogen is grounded to dinitrogen, but the source atmosphere is N2 containing 5% O2 by volume, not separate variable-concentration final-medium ingredients. The oxygen row is ungrounded.

## Evidence

The TOGO M928 payload identifies a `Basal minerals` block containing 1 L distilled water, 16 g NaCl, 2 g K2HPO4, 30 g NaHCO3, and 190 g Na2CO3.

The recoverable TOGO and MediaDive J887 provider records agree that the per-liter post-decant additions are 0.2 ml 10% yeast extract solution, 1 ml 4 M NH4Cl, 1 ml 1 M MgSO4, 10 ml trace vitamins, 1 ml selenite-tungstate solution, 1 ml Trace element solution SL-4, 20 ml 1 M sodium butyrate, and 20 ml 1 M sodium acetate.

The imported source instructs autoclaving the basal solution, letting it stand for three days, decanting the clear solution into another sterile bottle, aseptically adding the post-decant solutions, distributing the medium into culture vessels, replacing the gas phase with N2 containing 5% O2 by volume, and closing with butyl rubber stoppers.

## Completeness

The generated record lacks all preparation steps, including the stand-and-decant boundary that separates basal minerals from later additions.

Every post-decant solution in the TOGO record is either an empty `Unknown solution` or a milliliter addition stored as `G_PER_L`.

Trace vitamins, selenite-tungstate solution, and SL-4 trace element solution are preserved only as text references to M190, M431, and M335, not as resolvable stock recipes.

## Findings

- Major: The 1 L basal water row is mis-unitized as `1 G_PER_L`.
- Major: The 0.2 ml, 1 ml, 10 ml, and 20 ml post-decant stock additions are stored as `G_PER_L` concentrations rather than final addition volumes.
- Major: All six solution wrappers are empty and named `Unknown solution`, so the record loses 10% yeast extract, 4 M NH4Cl, 1 M MgSO4, trace vitamins, selenite-tungstate, and SL-4 stock composition or reference boundaries.
- Major: The basal autoclave, three-day stand, decant, aseptic-addition, N2 plus 5% O2 headspace, and butyl-rubber-stopper instructions are absent.
- Major: TOGO M928 remains unlinked from the active direct JCM/MediaDive J887 record for the same medium.
- Minor: Oxygen gas is ungrounded and both gases are modeled as variable ingredients rather than an atmosphere condition.

## Recommended Edits

- In `data/normalized_yaml/archaea/TOGO_M928_Natronolimnobius_AHT32_Medium_A.yaml`, convert the basal water row to a 1 L preparation volume.
- Represent each post-decant milliliter addition as a solution addition, preserving 10%, 4 M, 1 M, M190, M431, and M335 stock identities.
- Resolve M190, M431, and M335 to structured stock recipes or explicit internal media links.
- Add the JCM preparation sequence: basal autoclaving, three-day standing, decanting, aseptic additions, N2 plus 5% O2 headspace replacement, and closure with butyl rubber stoppers.
- Replace the nitrogen and oxygen ingredient rows with a scoped atmosphere condition.
- Link or collapse TOGO M928 with the direct JCM/MediaDive J887 owner.

## Follow-up Checks

- Regenerate `data/merge_yaml/merged/natronolimnobius_aht32_medium_a.yaml` and verify all post-decant additions remain milliliter volumes.
- Re-run open schema, strict, reference, and term validation after curation.
- Search including ignored and hidden files for `TOGO:M928`, `mediadive.medium:J887`, and `GRMD=887` to verify the direct and TOGO JCM imports are linked or collapsed.

## Additional Notes

The live JCM `GRMD=887` page returned `Nothing found`; this review used the inspected TOGO M928 and MediaDive J887 provider records as recoverable source views for that original JCM medium.
