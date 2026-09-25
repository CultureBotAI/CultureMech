# YAML Record Review: THERMINCOLA medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/thermincola_medium.yaml
- Started UTC: 2026-09-25T11:34:05Z
- Finished UTC: 2026-09-25T11:38:53Z
- Verdict: needs curation

## Target

- Generated YAML for KOMODO Medium 1028, THERMINCOLA medium.
- The record was merged from `thermincola_medium`.
- The checked sources were the normalized KOMODO 1028 record, MediaDive 1028, DSMZ Medium 1028, and the separately generated direct DSMZ 1028 record.

## Validation

- Schema validation: Passed; no issues found.
- Strict validation: Passed; exited 0 and wrote a header-only TSV with 0 error rows.
- Reference validation: Passed; 0 checks, all passed.
- Term validation: Passed; validation passed after the known `eutils`/`pkg_resources` warning.
- Embedded history validation: Not checked; the repository history validator targets standalone `history/` entries rather than merged `MediaRecipe.curation_history` arrays.

## Identity and Grounding

- The source pointer is grounded to KOMODO 1028, and the notes point to DSMZ Medium 1028 through `mediadive.medium:1028`.
- DSMZ/MediaDive Medium 1028 is THERMINCOLA MEDIUM (CO) at pH 8.0.
- The direct DSMZ/MediaDive 1028 import exists separately as `thermincola_medium_co` instead of being merged or duplicate-linked with this KOMODO 1028 record.

## Evidence

- DSMZ 1028 lists a 1003 ml main solution with major rows for NH4Cl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, KCl, KH2PO4, 1 ml Wolfe's mineral elixir, Na-acetate, 0.5 ml 0.1% sodium resazurin, NaHCO3, Na2CO3, Na2S x 9 H2O, yeast extract, 2 ml Wolin's vitamin solution (10x), and 1000 ml distilled water.
- Wolfe's mineral elixir is a 1 L stock added at 1 ml/L; it contains 1 g/L CaCl2 x 2 H2O and other salts such as 30 g/L MgSO4 x 7 H2O, 5 g/L MnSO4 x H2O, and 10 g/L NaCl at stock strength.
- Wolin's vitamin solution (10x) is a 1 L stock added at 2 ml/L.
- DSMZ 1028 instructs anoxic preparation under 100% N2 and 100% carbon monoxide, filter-sterilized yeast extract and vitamin stocks, pH 8.0 adjustment with sterile anoxic 1 N HCl, and an optional extra 0.30 g/L sodium sulfide if the autoclaved medium remains pink.

## Completeness

- pH 8.0 is present.
- The 1000 ml distilled-water row is missing.
- DSMZ preparation steps are missing.
- Wolfe's mineral elixir and Wolin's vitamin solution (10x) are flattened at undiluted stock strength.

## Findings

- Wolfe's mineral elixir was expanded as if the full 1 L stock were present in the final liter; examples include 30 G_PER_L MgSO4 x 7 H2O, 5 G_PER_L MnSO4 x H2O, and 10 G_PER_L NaCl instead of 1 ml/L of the stock.
- The 1 g/L CaCl2 x 2 H2O stock concentration from Wolfe's mineral elixir was summed with the 0.0997009 G_PER_L main-medium CaCl2 row, producing an impossible 1.0997009 G_PER_L CaCl2 row.
- Wolin's vitamin solution was expanded at undiluted stock strength even though DSMZ 1028 adds 2 ml/L.
- The 1000 ml Distilled water row and DSMZ 1028 anoxic preparation instructions are missing.
- The KOMODO 1028 and direct DSMZ/MediaDive 1028 records remain separate even though they point to the same DSMZ source.

## Recommended Edits

- Regenerate KOMODO 1028 with Wolfe's mineral elixir and Wolin's vitamin solution retained as stock additions, or expand them only after applying their 1 ml/L and 2 ml/L final dilutions.
- Keep the main-medium CaCl2 x 2 H2O row separate from the CaCl2 row inside Wolfe's mineral elixir until stock dilution is applied.
- Preserve the DSMZ 1028 distilled-water row and preparation steps.
- Merge or explicitly duplicate-link the corrected KOMODO 1028 record with the direct DSMZ/MediaDive 1028 import.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Verify that no corrected DSMZ 1028 record still contains 30 G_PER_L MgSO4 x 7 H2O or a summed 1.0997009 G_PER_L CaCl2 row.

## Additional Notes

- None found.
