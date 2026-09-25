# YAML Record Review: modified_cytophaga_agar

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_cytophaga_agar.yaml
- Started UTC: 2026-09-24T10:45:43Z
- Finished UTC: 2026-09-24T10:47:08Z
- Verdict: needs curation

## Target

Generated record `CultureMech:009366` for TOGO medium `M2820`, `modified cytophaga agar`.

The generated record merges `modified_cytophaga_agar` from `data/normalized_yaml/bacterial/modified_cytophaga_agar.yaml`. The generated YAML was compared with that maintained owner and the TOGO `M2820` API payload.

## Validation

- Open LinkML validation: passed with no issues found.
- Strict validation: passed with no error rows.
- Reference validation: passed with 0 reference checks.
- Term validation: passed.
- Embedded `curation_history`: Not checked: the available history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The generated record has the correct TOGO medium identity and retains the nine source ingredient labels.

All nine source rows are percentages tagged `(w/v)` in the TOGO payload, but the import stores the same numeric values as `G_PER_L`. That makes every concentration one tenth of the source value in grams per liter: for example 1.5% agar should become 15 g/L, not 1.5 g/L, and 0.06% tryptone should become 0.6 g/L, not 0.06 g/L.

## Evidence

TOGO `M2820` records modified cytophaga agar with 0.06% tryptone, 0.05% yeast extract, 0.02% beef extract, 0.02% sodium acetate, 0.05% anhydrous calcium chloride, 0.05% magnesium chloride, 0.05% potassium chloride, 1.5% agar, and 0.02% gelatin, all as weight/volume percentages at pH 7.5.

The generated YAML retains those ingredient labels but assigns the raw percentage numbers to grams per liter. It also omits pH 7.5 even though the TOGO metadata carries `ph: 7.5`.

The magnesium chloride row is additionally grounded as `CHEBI:86345` / magnesium dichloride hexahydrate, but the imported TOGO row says only `magnesium chloride`; the hexahydrate assignment is not source-backed in this API payload.

## Completeness

The generated record is complete for row count and for the TOGO medium identifier.

It is incomplete for concentration-unit normalization and pH. A curated owner should convert each `(w/v)` percentage to grams per liter and structure the TOGO pH value as preparation data.

## Findings

- High: All nine ingredient amounts are imported as grams per liter without converting the TOGO `(w/v)` percentages to grams per liter, underreporting every formula row by a factor of 10.
- Medium: TOGO pH 7.5 is absent from the generated YAML.
- Low: The magnesium chloride CHEBI assignment specifies a hexahydrate even though the source row does not specify hydration state.

## Recommended Edits

- Correct `data/normalized_yaml/bacterial/modified_cytophaga_agar.yaml` so 0.06% tryptone becomes `0.6` `G_PER_L`, each 0.05% row becomes `0.5` `G_PER_L`, each 0.02% row becomes `0.2` `G_PER_L`, and 1.5% agar becomes `15` `G_PER_L`.
- Add a pH 7.5 preparation datum or step derived from TOGO `M2820`.
- Reassess the magnesium chloride grounding unless a source outside the current TOGO payload justifies the hexahydrate-specific CHEBI term.
- Regenerate `data/merge_yaml/merged/modified_cytophaga_agar.yaml` after the maintained owner is repaired.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated YAML.
- Compare each regenerated amount against the TOGO `M2820` `(w/v)` rows after multiplying percentages by 10 to verify that the generated record now uses true grams-per-liter values.

## Additional Notes

None found.
