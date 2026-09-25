# YAML Record Review: ppes_ii_agar_medium__e6eb967a

- Repository: CultureMech
- Record: data/merge_yaml/merged/ppes_ii_agar_medium__e6eb967a.yaml
- Started UTC: 2026-09-24T21:42:23Z
- Finished UTC: 2026-09-24T21:42:23Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:008972
- Name: ppes_ii_agar_medium
- Source import: TOGO M238 / JCM_M246
- Primary external ID: TOGO:M238
- Maintained input: data/normalized_yaml/bacterial/TOGO_M238_PPES-II_Agar_Medium.yaml

This generated record represents the TOGO import of PPES-II Agar Medium from JCM 246.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/ppes_ii_agar_medium__e6eb967a.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

TOGO M238 imports JCM_M246, and the TOGO API and JCM 246 page agree on the PPES-II Agar Medium formula: 2 g peptone, 1 g Proteose peptone No. 3, 1 g Soytone, 1 g yeast extract, 0.1 g EDTA-Fe(III), 15 g agar, 1 L artificial seawater, pH 7.8, and an artificial-seawater subrecipe containing NaCl, KCl, MgCl2 x 6 H2O, MgSO4 x 7 H2O, CaCl2 x 2 H2O, and 1 L distilled water.

The generated record is grounded to the right source but has the stale TOGO import shape: it emits `Artificial seawater (see below)` as `1 G_PER_L`, emits the subrecipe's 1 L distilled water as `1 G_PER_L`, flattens the artificial-seawater subrecipe into the main ingredient list, omits pH 7.8, and leaves EDTA-Fe(III) ungrounded.

Exact ignored-file searches across `data/normalized_yaml` and `data/merge_yaml` for `TOGO:M238`, `JCM_M246`, `GRMD=246`, `TOGO_M238_PPES-II_Agar_Medium`, and `ppes_ii_agar_medium__e6eb967a` found this TOGO M238 normalized input, this split generated record, and the separate direct JCM 246 `ppes_ii_agar_medium` generated record.

## Evidence

- TOGO M238 has a main solution with 1 L `Artificial seawater (see below)` and six non-seawater rows: peptone, Proteose peptone No. 3, Soytone, yeast extract, EDTA-Fe(III), and agar.
- TOGO M238 has a separate `Artificial seawater` subcomponent with 1 L distilled water plus 5.4 g MgSO4 x 7 H2O, 30 g NaCl, 1 g CaCl2 x 2 H2O, 10.8 g MgCl2 x 6 H2O, and 0.7 g KCl.
- JCM 246 lists the same main solution, artificial-seawater subcomponent, and pH 7.8 adjustment.

## Completeness

The generated record is incomplete and partially mis-normalized against JCM 246. It loses the artificial-seawater boundary, misstates two source 1 L rows as 1 G_PER_L, omits pH 7.8, and remains split from the cleaner direct JCM 246 / DSMZ 1075 duplicate cluster.

## Findings

1. Major: The main 1 L artificial seawater ingredient is imported as `1 G_PER_L` instead of a 1 L constituent medium or nested solution.
2. Major: The artificial-seawater subrecipe is flattened into the main ingredient list, including a 1 L distilled-water row represented as `1 G_PER_L`.
3. Major: The pH 7.8 source assertion is absent from the generated record.
4. Major: The same JCM 246 authority is emitted both here and in `data/merge_yaml/merged/ppes_ii_agar_medium.yaml`.
5. Minor: The EDTA-Fe(III) row lacks its available CHEBI grounding in this stale TOGO import.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M238_PPES-II_Agar_Medium.yaml` so the 1 L artificial seawater row points to a nested artificial-seawater solution and the nested 1 L distilled-water row is no longer `1 G_PER_L`.
- Add the pH 7.8 assertion and restore EDTA-Fe(III) grounding to CHEBI:30729 during TOGO M238 curation.
- Reconcile TOGO M238 with the direct JCM 246 / DSMZ 1075 PPES-II Agar duplicate cluster before regenerating.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after normalized curation and regeneration.
- Run exact ignored-file searches for `TOGO:M238`, `JCM_M246`, and `GRMD=246` to confirm JCM 246 is not emitted twice.
- Spot-check regenerated output for a 1 L artificial-seawater ingredient, pH 7.8, and a nested artificial-seawater solution with its own 1 L distilled-water carrier.

## Additional Notes

None found.
