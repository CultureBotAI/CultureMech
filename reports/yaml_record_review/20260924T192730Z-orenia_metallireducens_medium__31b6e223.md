# YAML Record Review: ORENIA METALLIREDUCENS MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/orenia_metallireducens_medium__31b6e223.yaml
- Started UTC: 2026-09-24T19:26:26Z
- Finished UTC: 2026-09-24T19:27:30Z
- Verdict: needs curation

## Target

Reviewed `CultureMech:002316`, the generated direct JCM `orenia_metallireducens_medium` record merged from `data/normalized_yaml/bacterial/orenia_metallireducens_medium.yaml`.

## Validation

Passed LinkML validation against `MediaRecipe` with no issues reported.

Passed strict validation; the TSV contained only the header row.

Passed LinkML reference validation with zero reference checks.

Passed LinkML term validation.

Embedded `curation_history` validation was not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` blocks in generated YAML.

## Identity and Grounding

The identity is grounded to JCM Medium 1143, ORENIA METALLIREDUCENS MEDIUM, and preserves `media_term.term.id: mediadive.medium:J1143`.

An ignored-inclusive exact search for `mediadive.medium:J1143`, `GRMD=1143`, `TOGO:M1225`, and `orenia_metallireducens_medium` under `data/merge_yaml` and `data/normalized_yaml` found this direct JCM owner and a separate TOGO M1225 generated duplicate at `data/merge_yaml/merged/ORENIA_METALLIREDUCENS_MEDIUM.yaml`.

## Evidence

The fetched JCM 1143 page lists base salts, yeast extract, 1 ml FeCl2 solution, 1 ml trace element solution, 1 ml trace vitamins, 1 ml selenite-tungstate solution, 1 mg resazurin, 5 ml phosphate buffer, and 1 L distilled water. It then adds 2 g NaHCO3 and 0.031 g L-Cysteine HCl x H2O at about 50 C under N2-CO2, autoclaves under that gas, and adds 10 ml 1.0 M glucose, 20 ml 0.25 M ferric citrate, 5 ml 1.88 M CaCl2 x 2 H2O, and 0.5 ml 5% Na2S x 9 H2O after cooling.

TOGO M1225 points to the same JCM 1143 source URL and preserves the same major recipe blocks, including the phosphate buffer made from 12.5 g KH2PO4, 20 g K2HPO4, and 1 L distilled water.

## Completeness

The generated record includes the base salts, 50 C NaHCO3/cysteine additions, post-autoclave glucose/ferric citrate/CaCl2/Na2S additions, and the imported stock solution ingredients.

The preparation text is incomplete but still preserves the main heat, N2-CO2, distribution, and post-autoclave addition phases.

Target organisms are absent. This is not a defect for the fetched JCM and TOGO medium definitions.

## Findings

- The generated record flattens distinct scopes and sums duplicate labels. It adds the base 0.35 g KH2PO4 to the 12.5 g/L phosphate-buffer stock as `12.835249 G_PER_L`, and it adds the base CaCl2 row to the 1.88 M CaCl2 stock as `5.0478927 G_PER_L`.
- Solution aliquots are emitted as gram-per-liter final ingredients. The JCM post-autoclave rows are 10 ml 1.0 M glucose, 20 ml 0.25 M ferric citrate, 5 ml 1.88 M CaCl2 x 2 H2O, and 0.5 ml 5% Na2S x 9 H2O, but the generated YAML reports `Glucose` as `10 G_PER_L`, `Ferric citrate` as `20 G_PER_L`, `CaCl2 x 2 H2O` as part of a 5 g/L sum, and `Na2S x 9 H2O` as `0.5 G_PER_L`.
- The base 1 L distilled water row and the 1 L phosphate-buffer water row are absent from the direct JCM generated record.
- FeCl2, trace element, trace vitamin, and selenite-tungstate component concentrations are stock concentrations imported from referenced JCM media, not final-medium concentrations for the 1 ml additions in JCM 1143.
- `HCl` from the FeCl2/trace stock and `NaOH` from the selenite-tungstate stock are flattened as final top-level medium ingredients.
- TOGO M1225 is a duplicate import of the same JCM 1143 recipe, but it generated separately as `data/merge_yaml/merged/ORENIA_METALLIREDUCENS_MEDIUM.yaml`.

## Recommended Edits

- Recurate `data/normalized_yaml/bacterial/orenia_metallireducens_medium.yaml` with explicit referenced stock solutions, phosphate buffer, 50 C additions, and post-autoclave solution aliquots rather than a flat final ingredient list.
- Restore the base 1 L water and phosphate-buffer 1 L water rows in their proper scopes.
- Keep glucose, ferric citrate, CaCl2, and sulfide as post-autoclave solution additions with their molarity or percent concentrations.
- Merge the TOGO M1225 normalized owner into the same source-duplicate group after repairing both branches.
- Regenerate `data/merge_yaml/merged/orenia_metallireducens_medium__31b6e223.yaml` and `data/merge_yaml/merged/ORENIA_METALLIREDUCENS_MEDIUM.yaml` after the normalized repairs.

## Follow-up Checks

- Rerun open-schema, strict, reference, and term validation on the regenerated Orenia Metallireducens records.
- Recheck JCM 1143 and TOGO M1225 after regeneration to confirm the N2-CO2 handling, 50 C additions, phosphate buffer, post-autoclave stocks, water rows, and referenced FeCl2/trace/vitamin stocks are correctly scoped.

## Additional Notes

None found.
