# YAML Record Review: THERMINCOLA MEDIUM (CO)

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermincola_medium_co.yaml
- Started UTC: 2026-09-25T11:39:15Z
- Finished UTC: 2026-09-25T11:42:00Z
- Verdict: needs curation

## Target

- Generated YAML for DSMZ Medium 1028, THERMINCOLA MEDIUM (CO).
- The record was merged from `thermincola_medium_co`.
- The checked sources were the normalized DSMZ 1028 record, MediaDive 1028, DSMZ Medium 1028, and the separate KOMODO 1028 record.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; exited 0 with no diagnostics.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The source pointer is grounded to DSMZ/MediaDive Medium 1028.
- DSMZ 1028 is THERMINCOLA MEDIUM (CO) at pH 8.0.
- An exact `mediadive.medium:1028` and `komodo.medium:1028` search used `rg --no-ignore --hidden` scoped to `data`; it found this direct DSMZ 1028 record and the separate KOMODO 1028 record.

## Evidence

- DSMZ 1028 lists a 1003 ml main solution containing NH4Cl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, KCl, KH2PO4, 1 ml Wolfe's mineral elixir, Na-acetate, 0.5 ml 0.1% sodium resazurin, NaHCO3, Na2CO3, Na2S x 9 H2O, yeast extract, 2 ml Wolin's vitamin solution (10x), and 1000 ml distilled water.
- Wolfe's mineral elixir is a 1 L stock added at 1 ml/L and contains stock-strength salts including 30 g/L MgSO4 x 7 H2O, 5 g/L MnSO4 x H2O, 10 g/L NaCl, and 1 g/L CaCl2 x 2 H2O.
- Wolin's vitamin solution (10x) is a 1 L stock added at 2 ml/L.
- DSMZ 1028 gives pH 8.0 and the anoxic 100% N2, 100% carbon monoxide, autoclaving, filtration, and 1 N HCl adjustment instructions.

## Completeness

- pH 8.0 is present.
- DSMZ preparation steps are present.
- The 1000 ml distilled-water row is missing.
- Wolfe's mineral elixir and Wolin's vitamin solution (10x) are flattened at undiluted stock strength.

## Findings

- Wolfe's mineral elixir was expanded as if the entire stock liter were present, yielding rows such as 30 G_PER_L MgSO4 x 7 H2O, 5 G_PER_L MnSO4 x H2O, and 10 G_PER_L NaCl instead of applying a 1 ml/L dilution.
- The stock's 1 G_PER_L CaCl2 x 2 H2O row was summed with the main-medium CaCl2 row, producing 1.0997009 G_PER_L CaCl2.
- Wolin's vitamin solution was expanded at stock strength instead of at its 2 ml/L final addition.
- The direct DSMZ 1028 record remains separate from the KOMODO 1028 import of the same DSMZ source.

## Recommended Edits

- Regenerate DSMZ 1028 with Wolfe's mineral elixir and Wolin's vitamin solution retained as explicit stock additions, or expand them only after applying the 1 ml/L and 2 ml/L dilution factors.
- Keep the main-medium and Wolfe's mineral elixir CaCl2 rows in their own recipe scopes until stock dilution is applied.
- Preserve the 1000 ml distilled-water row.
- Merge or source-duplicate-link the corrected direct DSMZ 1028 and KOMODO 1028 records.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that corrected DSMZ 1028 no longer contains full-strength Wolfe's mineral elixir rows.

## Additional Notes

- None found.
