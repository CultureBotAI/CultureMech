# YAML Record Review: halomonas_magadiensis_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halomonas_magadiensis_medium.yaml`
- Started UTC: 2026-09-23T10:35:08Z
- Finished UTC: 2026-09-23T10:36:00Z
- Verdict: needs curation

## Target

Generated merged YAML rooted on KOMODO medium 971, `HALOMONAS MAGADIENSIS medium`, after merging DSMZ 971, DSMZ 785, DSMZ 1060, and KOMODO variants.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed with 0 error rows.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The top-level record claims KOMODO `komodo.medium:971` identity and DSMZ medium 971 provenance.
- An ignored-file-inclusive exact search for `mediadive.medium:971`, `mediadive.medium:785`, `mediadive.medium:1060`, `komodo.medium:971`, `komodo.medium:785`, and the two DSM-specific KOMODO variant IDs found all seven merged source records.
- The simple chemical groundings on glucose, KH2PO4, MgSO4 x 7 H2O, NaCl, Na2CO3, and agar are appropriate.
- Peptone and yeast extract are correctly ungrounded as complex undefined ingredients.

## Evidence

- DSMZ 971 has pH 10.0, 40 g/L NaCl, 10 g/L Na2CO3, and 20 g/L agar, with NaCl and Na2CO3 autoclaved separately and added to the organic components at 60 C.
- DSMZ 785 has pH 9.6 with the same glucose/peptone/yeast extract/KH2PO4/MgSO4/NaCl/Na2CO3 base quantities, but its 15 g agar row is optional in MediaDive.
- DSMZ 1060 is pH 8.1 and is assembled by separately autoclaving 700 ml Solution A and 300 ml Solution B; it uses 20 g NaCl and 1 g Na2CO3, not the DSMZ 971/785 amounts.

## Completeness

- Missing water: the generated merged record has no distilled-water row from any source.
- Missing DSMZ 971 preparation: the KOMODO-rooted record lost the NaCl/Na2CO3 separate-autoclaving and 60 C mixing instruction present in the direct DSMZ 971 parent.
- Missing variant distinctions: DSMZ 785 and DSMZ 1060 differ in pH, agar, salt concentration, or preparation topology but were merged as source duplicates.

## Findings

1. Distinct DSMZ media were incorrectly merged. DSMZ 971, 785, and 1060 are not source duplicates because they differ at least in pH, NaCl amount, Na2CO3 amount, agar amount, and/or solution structure.
2. The generated record combines a DSMZ 971 identity and pH with a DSMZ 785 agar row. For DSMZ 971, agar is 20 g/L and required; the generated row is 15 g/L and marked optional.
3. DSMZ 1060 was collapsed into this recipe even though it uses a 700 ml / 300 ml two-solution protocol and final 20 g/L NaCl plus 1 g/L Na2CO3.
4. Direct DSMZ 971 preparation semantics were lost when the KOMODO record was used as the canonical merge root.

## Recommended Edits

- Split DSMZ 971, DSMZ 785, and DSMZ 1060 back into separate records or explicit variants, not `SOURCE_DUPLICATE` synonyms.
- Restore DSMZ 971 with 20 g/L required agar and its NaCl/Na2CO3 separate-autoclaving preparation step.
- Restore DSMZ 785 with pH 9.6 and optional 15 g agar.
- Restore DSMZ 1060 with its 700 ml Solution A / 300 ml Solution B structure, pH 8.1, and lower NaCl/Na2CO3 amounts.
- Keep KOMODO 971 and KOMODO 785 only as source duplicates of their exact DSMZ parents.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Verify that `mediadive.medium:971`, `mediadive.medium:785`, and `mediadive.medium:1060` no longer share one merge fingerprint.
- Re-run exact ignored-file-inclusive searches for the three DSMZ IDs and both KOMODO variant IDs after regeneration.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
