# YAML Record Review: THERMOACETOGENIUM MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermoacetogenium_medium__be581d8a.yaml
- Started UTC: 2026-09-25T11:39:15Z
- Finished UTC: 2026-09-25T11:42:01Z
- Verdict: needs curation

## Target

- Generated YAML for DSMZ Medium 880, THERMOACETOGENIUM MEDIUM.
- The record was merged from `thermoacetogenium_medium` and `thermoacetogenium_phaeum_medium`.
- The checked sources were the normalized DSMZ 880 and KOMODO 880 records, MediaDive 880, and DSMZ Medium 880.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The canonical source pointer is grounded to DSMZ/MediaDive Medium 880.
- The KOMODO 880 child explicitly references DSMZ Medium 880 through `mediadive.medium:880` and was correctly treated as a duplicate of the direct DSMZ 880 import.
- An exact `mediadive.medium:880` and `komodo.medium:880` search used `rg --no-ignore --hidden` scoped to `data`; it found the direct DSMZ 880 and KOMODO 880 source records merged here.

## Evidence

- DSMZ 880 lists a 1008 ml main solution with KH2PO4, NaCl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, NH4Cl, 1 ml Trace element solution SL-11, 1 ml Selenite-tungstate solution, 0.5 ml 0.1% sodium resazurin, KHCO3, L-Cysteine HCl x H2O, 6 ml 50% vol/vol methanol, 1 ml Wolin's vitamin solution (10x), Na2S x 9 H2O, and 1000 ml distilled water.
- Trace element solution SL-11 and Selenite-tungstate solution are independent 1 L stocks added to the main medium at 1 ml/L.
- Wolin's vitamin solution (10x) is another 1 L stock added at 1 ml/L.
- DSMZ 880 gives pH 7.0 to 7.2 and detailed 80% N2 plus 20% CO2, autoclaving, post-autoclave methanol/vitamin/sulfide addition, filtration, and stock preparation instructions.

## Completeness

- The pH range 7.0 to 7.2 is present.
- DSMZ preparation steps are present.
- The 1000 ml distilled-water row is missing.
- Trace element solution SL-11, Selenite-tungstate solution, and Wolin's vitamin solution are flattened at undiluted stock strength.

## Findings

- Trace element solution SL-11 was expanded at stock strength, including 5.2 G_PER_L Na2-EDTA x 2 H2O and 1.5 G_PER_L FeCl2 x 4 H2O, instead of the 1 ml/L final dilution.
- Selenite-tungstate solution was expanded at stock strength even though DSMZ 880 adds it at 1 ml/L.
- Wolin's vitamin solution (10x) was expanded at stock strength even though DSMZ 880 adds it at 1 ml/L.
- The 1000 ml main-medium Distilled water row is missing.
- The DSMZ and KOMODO 880 merge is appropriate only after both sources share a corrected structured stock model.

## Recommended Edits

- Regenerate DSMZ 880 from the structured MediaDive solution tree, preserving Trace element solution SL-11, Selenite-tungstate solution, and Wolin's vitamin solution as 1 ml/L stock additions.
- Expand stock components only after applying their 1 ml/L dilution factors.
- Preserve the main 1000 ml distilled-water row.
- Re-merge the direct DSMZ and KOMODO 880 records after their corrected ingredient signatures still match.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that corrected DSMZ 880 no longer contains undiluted 5.2 G_PER_L EDTA or 1.5 G_PER_L FeCl2 rows from Trace element solution SL-11.

## Additional Notes

- None found.
