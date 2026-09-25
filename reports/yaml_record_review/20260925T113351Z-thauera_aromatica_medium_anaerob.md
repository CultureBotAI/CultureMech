# YAML Record Review: THAUERA AROMATICA MEDIUM (ANAEROB)

- Repository: CultureMech
- Record: data/merge_yaml/merged/thauera_aromatica_medium_anaerob.yaml
- Started UTC: 2026-09-25T11:29:01Z
- Finished UTC: 2026-09-25T11:33:51Z
- Verdict: needs curation

## Target

- Generated YAML for DSMZ Medium 855, THAUERA AROMATICA MEDIUM (ANAEROB).
- The record was merged from `thauera_aromatica_ar_1_medium`, `thauera_aromatica_ar_1_medium_anaerobic`, and `thauera_aromatica_medium_anaerob`.
- The checked sources were the normalized DSMZ 855 and KOMODO 855 records, MediaDive 855, and DSMZ Medium 855.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to DSMZ/MediaDive Medium 855.
- The two KOMODO inputs explicitly reference DSMZ Medium 855 through `mediadive.medium:855`; both carry the same ingredient and concentration signature as the direct MediaDive import and were correctly treated as source duplicates of DSMZ 855.
- An exact source-ID search used `rg --no-ignore --hidden` scoped to `data` and found the direct DSMZ 855 record plus the two KOMODO 855 duplicates that were merged into this record.

## Evidence

- DSMZ 855 defines a main medium from 952 ml Solution A, 10 ml Solution B, 10 ml Solution C, 30 ml Solution D, and 1 ml Solution E.
- Solution A contains the sulfate, phosphate, ammonium chloride, NaCl, MgCl2 x 6 H2O, KCl, CaCl2 x 2 H2O, 1 ml/L Trace element solution SL-10, 1 ml/L Selenite-tungstate solution, and 950 ml distilled water.
- Solution B contains 0.60 g 3,5-dihydroxybenzoic acid or Na-benzoate in 10 ml water; Solution C contains 0.60 g KNO3 in 10 ml water; Solution D contains 1.50 g Na2CO3 in 30 ml water; Solution E is 1 ml Wolin's vitamin solution (10x).
- DSMZ 855 gives pH 7.2 and anaerobic preparation under 80% N2 plus 20% CO2 and 100% N2 gas atmospheres, with an aerobic note to omit carbonate and KNO3.

## Completeness

- pH 7.2 is present.
- The DSMZ anaerobic and aerobic preparation notes are present.
- The nested stock structure is not present; stock-only concentrations from Solutions B to E, Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution are flattened into final ingredients.

## Findings

- 3,5-Dihydroxybenzoic acid and KNO3 are stored as 60 G_PER_L, which is the 0.60 g per 10 ml stock concentration rather than the final addition.
- Na2CO3 is stored as 50 G_PER_L, which is the 1.50 g per 30 ml Solution D concentration rather than the final addition.
- Trace element solution SL-10 and Selenite-tungstate solution are expanded at undiluted stock strength even though DSMZ 855 adds each stock at 1 ml/L through Solution A.
- Wolin's vitamin solution (10x) is expanded at stock strength even though DSMZ 855 adds 1 ml/L of the vitamin solution through Solution E.
- The merged KOMODO duplicate links are appropriate, but the shared source signature means all three upstream inputs need the same stock-structure fix.

## Recommended Edits

- Regenerate DSMZ 855 from the structured MediaDive solution tree rather than flattening stock solution `g_l` values into final `ingredients`.
- Keep Solutions A to E as explicit nested additions, or expand only after applying the 952 ml, 10 ml, 10 ml, 30 ml, and 1 ml dilution factors.
- Keep Trace element solution SL-10, Selenite-tungstate solution, and Wolin's vitamin solution as stock additions or expand them only after their 1 ml/L final dilution.
- Re-merge the DSMZ and KOMODO 855 records after their corrected ingredient signatures still match.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that the corrected DSMZ 855, KOMODO 855, and KOMODO 855.1 records still merge as source duplicates and no longer contain 60 G_PER_L organic acid or nitrate rows.

## Additional Notes

- None found.
