# YAML Record Review: thiobacillus_ferrooxidans_medium_aph

- Repository: CultureMech
- Record: data/merge_yaml/merged/thiobacillus_ferrooxidans_medium_aph.yaml
- Started UTC: 2026-09-25T12:57:41Z
- Finished UTC: 2026-09-25T12:58:05Z
- Verdict: needs curation

## Target

- Generated YAML for the KOMODO 271 THIOBACILLUS FERROOXIDANS MEDIUM (APH) record enriched from DSMZ 271.
- The record was merged from `thiobacillus_ferrooxidans_medium_aph`.
- The checked sources were the local KOMODO 271 enrichment metadata, MediaDive 271, and DSMZ Medium 271.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to KOMODO 271, THIOBACILLUS FERROOXIDANS MEDIUM (APH).
- The notes map KOMODO 271 to DSMZ 271.
- DSMZ/MediaDive 271 identifies the exact DSMZ formulation as ACIDITHIOBACILLUS (APH) MEDIUM, and a separate exact DSMZ 271 normalized record exists as `acidithiobacillus_aph_medium`.

## Evidence

- DSMZ 271 lists 2 g (NH4)2SO4, 0.5 g K2HPO4, 0.5 g MgSO4 x 7 H2O, 0.1 g KCl, 0.02 g Ca(NO3)2 x 4 H2O, 8 g FeSO4 x 7 H2O, and 1000 ml distilled water.
- DSMZ 271 says to adjust to pH 2.0 with 10 N H2SO4 and sterilize by filtration.
- DSMZ 271 also documents an alternate split autoclaving path for the basal medium and ferrous sulfate, plus static incubation without shaking.

## Completeness

- The six non-water DSMZ 271 ingredients and pH 2.0 are present.
- The source water row is missing.
- The filter-sterilization instruction, alternate autoclaving instruction, nitrogen atmosphere detail for ferrous sulfate, and static incubation note are missing.

## Findings

- The record preserves the old KOMODO Thiobacillus label while its copied DSMZ 271 source is the direct Acidithiobacillus APH record already present in normalized YAML.
- The formulation is structurally valid but incomplete because no DSMZ 271 preparation instructions were imported.
- The 1000 ml distilled-water row from DSMZ 271 is omitted.

## Recommended Edits

- Reconcile or merge the KOMODO 271 record with the direct DSMZ 271 `acidithiobacillus_aph_medium` record.
- Preserve the DSMZ filtration route and the alternate basal/ferrous-sulfate autoclaving route as preparation steps.
- Restore the DSMZ water row.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Confirm whether the Thiobacillus ferrooxidans name should remain only as a legacy alias.
- Ensure DSMZ 271 strain-specific sulfur variants remain separate from this base APH formulation.

## Additional Notes

- None found.
