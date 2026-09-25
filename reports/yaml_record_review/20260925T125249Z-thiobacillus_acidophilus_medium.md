# YAML Record Review: thiobacillus_acidophilus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thiobacillus_acidophilus_medium.yaml
- Started UTC: 2026-09-25T12:54:01Z
- Finished UTC: 2026-09-25T12:54:25Z
- Verdict: needs curation

## Target

- Generated YAML for the KOMODO 108 THIOBACILLUS ACIDOPHILUS MEDIUM record enriched from DSMZ 108.
- The record was merged from `thiobacillus_acidophilus_medium`.
- The checked sources were the local KOMODO 108 enrichment metadata, MediaDive 108, and DSMZ Medium 108.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical media term is grounded to KOMODO 108, THIOBACILLUS ACIDOPHILUS MEDIUM.
- The record notes point KOMODO 108 at DSMZ Medium 108.
- DSMZ/MediaDive 108 identifies that source as ACIDIPHILIUM ACIDOPHILUM MEDIUM, not THIOBACILLUS ACIDOPHILUS MEDIUM.

## Evidence

- DSMZ 108 lists 3 g (NH4)2SO4, 0.5 g KH2PO4, 1 g MgSO4 x 7 H2O, 0.1 g KCl, 18 mg Ca(NO3)2 x 4 H2O, 0.01 ml 0.1% FeSO4 x 7 H2O in 0.1 N H2SO4, optional 15 g agar for solid medium, 10 g D-glucose, and 1000 ml distilled water.
- DSMZ 108 says the liquid pH should be adjusted to 3.5 with H2SO4.
- DSMZ 108 says the solid pH should be adjusted to 4.5 with H2SO4 after autoclaving and says glucose should be sterilized separately.

## Completeness

- The DSMZ 108 ingredient formula is mostly present, including optional agar and 10 g/L D-glucose.
- The source water row is missing.
- The separate glucose sterilization and solid-medium pH instruction are missing.
- `physical_state` is `SOLID_AGAR`, but the single `ph_value` of 3.5 is the DSMZ liquid-medium pH.

## Findings

- The record identity is inconsistent: KOMODO 108 and the record name use the Thiobacillus label, but the DSMZ 108 formulation copied into the record is Acidiphilium acidophilum medium.
- The pH is ambiguous because the generated solid-agar record carries the DSMZ liquid pH instead of the DSMZ solid-medium pH of 4.5.
- The glucose sterilization instruction is omitted.
- The 1000 ml distilled-water row from DSMZ 108 is omitted.

## Recommended Edits

- Reconcile the KOMODO 108 identity with DSMZ 108 before treating the DSMZ formulation as evidence for `thiobacillus_acidophilus_medium`.
- If DSMZ 108 is retained, rename or alias the record around ACIDIPHILIUM ACIDOPHILUM MEDIUM with source evidence for any legacy Thiobacillus synonym.
- Represent liquid and solid conditions as separate variants or otherwise preserve their distinct pH values.
- Add the separate-glucose-sterilization instruction and the DSMZ water row.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Compare the exact KOMODO 108 row with DSMZ 108 to decide whether the KOMODO source name is obsolete, wrong, or intentionally mapped.
- Verify that optional agar does not force the liquid DSMZ recipe into a single solid-only record.

## Additional Notes

- None found.
