# YAML Record Review: THERMOANAEROBACTER MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoanaerobacter_medium__c53d0378.yaml
- Started UTC: 2026-09-25T11:45:33Z
- Finished UTC: 2026-09-25T11:49:17Z
- Verdict: needs curation

## Target

- Generated YAML for DSMZ Medium 61, THERMOANAEROBACTER MEDIUM.
- The record was merged from `clostridium_thermohydrosulfuricum_medium`, `for_dsm_8686_and_dsm_8690`, and `thermoanaerobacter_medium`.
- The checked sources were the normalized DSMZ 61, KOMODO 61, and KOMODO 61.1 records, MediaDive 61, and DSMZ Medium 61.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to DSMZ/MediaDive Medium 61.
- The KOMODO 61 record references the same DSMZ Medium 61 formulation through `mediadive.medium:61`.
- The KOMODO 61.1 record is for DSM 8686 and DSM 8690 and uses the DSMZ 61 instruction to replace sucrose with D-xylose and adjust pH to 5.2.

## Evidence

- DSMZ 61 lists 10 g Tryptone, 2 g Yeast extract, 0.5 ml 0.1% w/v Sodium resazurin, 0.2 g FeSO4 x 7 H2O, 10 g Sucrose, 0.2 g Na2SO3, 0.08 g Na2S2O3 x 5 H2O, and 1000 ml Distilled water.
- DSMZ 61 gives a pH range of 6.8-7.5 and a 100% N2 anaerobic preparation.
- DSMZ 61 separately instructs that DSM 8686 and DSM 8690 should replace sucrose with 10 g/L D-xylose and adjust pH to 5.2.

## Completeness

- The 6.8-7.5 pH range is present on the canonical DSMZ 61 formulation.
- The DSMZ preparation text is present.
- The main 1000 ml distilled-water row is missing.
- The DSMZ 61.1 xylose/pH-5.2 child is merged as a source duplicate rather than retained as a variant.

## Findings

- The direct DSMZ 61 recipe dropped its 1000 ml Distilled water row.
- The DSMZ 61.1 KOMODO child was merged as a `SOURCE_DUPLICATE` even though the source changes the substrate from sucrose to D-xylose and changes pH from 6.8-7.5 to 5.2 for DSM 8686 and DSM 8690.
- The generated canonical record does not preserve the D-xylose substitution needed by the DSM 8686 and DSM 8690 variant.

## Recommended Edits

- Preserve the DSMZ 61 1000 ml distilled-water row in the direct source record.
- Keep KOMODO 61 as the source duplicate of DSMZ/MediaDive 61.
- Re-link KOMODO 61.1 as a DSMZ 61 variant that replaces 10 G_PER_L sucrose with 10 G_PER_L D-xylose and sets pH 5.2.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that the corrected canonical record still carries sucrose while the DSM 8686 and DSM 8690 variant carries D-xylose and pH 5.2.

## Additional Notes

- None found.
