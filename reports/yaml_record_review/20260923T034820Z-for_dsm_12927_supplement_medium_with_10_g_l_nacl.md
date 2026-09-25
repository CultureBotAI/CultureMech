# YAML Record Review: for_dsm_12927_supplement_medium_with_10_g_l_nacl

- Repository: CultureMech
- Record: data/merge_yaml/merged/for_dsm_12927_supplement_medium_with_10_g_l_nacl.yaml
- Started UTC: 2026-09-23T03:47:07Z
- Finished UTC: 2026-09-23T03:48:20Z
- Verdict: needs curation

## Target

- Reviewed generated MediaRecipe `CultureMech:006137` / `for_dsm_12927_supplement_medium_with_10_g_l_nacl`, the KOMODO Medium 63.1 variant for DSM 12927.
- Compared it with sibling KOMODO Medium 63 / `data/normalized_yaml/bacterial/KOMODO_63_DESULFOVIBRIO_medium.yaml`.
- Cross-checked both KOMODO sources against the DSMZ Medium 63 PDF and the MediaDive REST payload for medium 63.

## Validation

- LinkML open-schema validation: pass.
- Strict CultureMech validation: pass; `/private/tmp/for_dsm_12927_supplement_medium_with_10_g_l_nacl.strict.tsv` contains only its header row.
- LinkML reference validation: pass; 0 external reference checks.
- LinkML term validation: pass.
- Embedded curation history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding

- The KOMODO identity is internally coherent: `komodo.medium:63.1` and the record label both identify the DSM 12927 variant that should supplement DSMZ Medium 63 with 10 g/L NaCl.
- The generated record incorrectly treats KOMODO 63.1 as an exact duplicate of KOMODO 63 even though the 63.1 label encodes a strain-specific NaCl supplement.
- Defined small-molecule groundings are appropriate.
- Yeast extract is ungrounded; that is acceptable as a complex ingredient.
- The variable NaOH pH-adjuster row is grounded, but it is derived from pH-adjustment notes rather than a DSMZ ingredient-table row.

## Evidence

- DSMZ 63 and MediaDive 63 define DESULFOVIBRIO (POSTGATE) MEDIUM as 980 ml Solution A plus 10 ml Solution B plus 10 ml Solution C.
- Solution A contains 0.5 g K2HPO4, 1 g NH4Cl, 1 g Na2SO4, 0.1 g CaCl2 x 2 H2O, 2 g MgSO4 x 7 H2O, 2 g Na-DL-lactate, 1 g Yeast extract, and 0.5 ml of 0.1% Sodium resazurin in the final 1000 ml recipe.
- Solution B contributes 0.5 g FeSO4 x 7 H2O per final liter, and Solution C contributes 0.1 g Na-thioglycolate and 0.1 g Ascorbic acid per final liter.
- The generated record instead contains Solution A rows normalized to the 980 ml stock volume, plus Solution B and C components at 50 g/L and 10 g/L stock strengths.
- The generated 63.1 variant has no NaCl row even though its source label requires supplementing the medium with 10 g/L NaCl.
- The generated record has Na-pyruvate instead of the DSMZ Na-DL-lactate row.
- DSMZ 63 final pH is 6.8-7.0 after a pre-distribution adjustment to 7.8 with NaOH; the generated record keeps `ph_value: 7.8` and no `preparation_steps`.

## Completeness

- The generated record is not compositionally complete for the DSM 12927 variant because it is missing the 10 g/L NaCl supplement.
- Source subsolution boundaries and preparation instructions are absent.
- The generated record preserves the main phosphate/sulfate/salt composition only approximately because Solution A concentrations are relative to 980 ml instead of the final liter.

## Findings

- Needs curation: KOMODO 63.1 should not be collapsed as an exact duplicate of KOMODO 63; it should be a strain-specific variant with an added 10 g/L NaCl row.
- Needs curation: Solution B and C stock ingredients are overrepresented 100-fold.
- Needs curation: Solution A rows are inflated by the 980 ml stock-volume denominator instead of represented as final g/L in the completed 1 L medium.
- Needs curation: the DSMZ Na-DL-lactate row is represented as Na-pyruvate and should be checked against the original KOMODO import.
- Needs curation: `ph_value: 7.8` captures the pre-distribution pH adjustment and loses the DSMZ final pH range 6.8-7.0.
- Needs curation: all DSMZ instructions for Solution A/B/C combination, N2 sparging, suspended precipitate handling, autoclaving, and final pH adjustment are absent.

## Recommended Edits

- Repair the KOMODO 63 and 63.1 normalized records or DSMZ resolver so DSMZ Medium 63 remains a 3-solution recipe instead of top-level flattened stock ingredients.
- Represent KOMODO 63.1 as a strain-specific child that adds 10 g/L NaCl to the repaired DSMZ 63 base.
- Restore the DSMZ Na-DL-lactate row unless KOMODO has source-backed evidence for replacing lactate with pyruvate.
- Store final pH 6.8-7.0 for the base medium and preserve the pre-distribution pH 7.8 only in preparation text.
- Regenerate `data/merge_yaml/merged/for_dsm_12927_supplement_medium_with_10_g_l_nacl.yaml` after curation.

## Follow-up Checks

- After repair, rerun open-schema, strict, reference, and term validation on the generated KOMODO 63.1 YAML.
- Confirm the generated 63.1 record contains a 10 g/L NaCl supplement and no 50 g/L FeSO4 x 7 H2O, 10 g/L Na-thioglycolate, or 10 g/L Ascorbic acid rows.
- Confirm KOMODO 63 and 63.1 no longer collapse into an exact duplicate merge.
- Confirm embedded curation-history timestamps are parseable after regeneration.

## Additional Notes

- The generated file is derived data. The missing NaCl supplement, subsolution flattening, and pH/preparation issues are present in `data/normalized_yaml/bacterial/for_dsm_12927_supplement_medium_with_10_g_l_nacl.yaml` and should be fixed there or in the DSMZ resolver.
