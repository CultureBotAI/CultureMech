# YAML Record Review: de_man_rogosa_and_sharpe_mrs_broth_sigma

- Repository: CultureMech
- Record: data/merge_yaml/merged/de_man_rogosa_and_sharpe_mrs_broth_sigma.yaml
- Started UTC: 2026-09-22T13:44:40Z
- Finished UTC: 2026-09-22T13:47:25Z
- Verdict: needs curation

## Target

Reviewed generated record `data/merge_yaml/merged/de_man_rogosa_and_sharpe_mrs_broth_sigma.yaml` with generated identifier `CultureMech:009412`, media term `TOGO:M2878`, original name `de Man, Rogosa, and Sharpe (MRS) broth (Sigma)`, category `bacterial`, and one merged source, `de_man_rogosa_and_sharpe_mrs_broth_sigma`.

## Validation

- LinkML open-schema validation: passed.
- Strict validation: passed with 0 error rows in `/private/tmp/de_man_rogosa_and_sharpe_mrs_broth_sigma.strict.tsv`.
- Reference validation: passed with 0 references checked.
- Term validation: passed.
- Embedded curation history: not checked; `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` blocks.

## Identity and Grounding

TOGO M2878 is a TOGO-authored recipe for de Man, Rogosa, and Sharpe broth made from a Sigma commercial powder. The final medium is 51 g `MRS broth (Sigma)` dissolved in 1 L distilled water. TOGO also gives a second `MRS broth (Sigma)` table that decomposes the dehydrated powder into magnesium sulfate heptahydrate, yeast extract, dipotassium hydrogen phosphate, manganous sulfate tetrahydrate, triammonium citrate, sodium acetate trihydrate, glucose, meat extract, and peptone.

An exact gitignore-independent search for `M2878` and `de_man_rogosa_and_sharpe_mrs_broth_sigma` across normalized YAML, merged YAML, and prior YAML record reviews found only the maintained source and this generated target.

## Evidence

The TOGO API reports one final-medium table with `Distilled water` 1 L and `MRS broth (Sigma)` 51 g, then a separate `MRS broth (Sigma)` subcomponent table whose rows sum the commercial powder formula. That source structure distinguishes the final commercial-product addition from the powder's internal composition.

## Completeness

The generated record captures all numeric rows from the TOGO response, but it does not preserve their hierarchy. It stores 51 g/L of MRS broth powder and then repeats every constituent of that powder as a separate top-level final-medium ingredient. It also converts the 1 L water row to `1 G_PER_L`.

## Findings

1. **The commercial powder was double-counted.** The final recipe uses 51 g MRS broth powder per 1 L, and the later TOGO table describes that powder's composition. The generated record flattened both layers into one ingredient list, so peptone, glucose, meat extract, salts, and buffers are represented as additional final-medium masses on top of the 51 g/L powder.

2. **The water row has the wrong unit.** TOGO M2878 lists 1 L distilled water; the generated record stores the same numeric value as `1 G_PER_L`.

3. **The Sigma powder lacks structure.** The internal `MRS broth (Sigma)` composition should be a nested stock/product composition or an explanatory annotation tied to the commercial powder, not unrelated sibling ingredients in the final medium.

## Recommended Edits

- Rebuild the record with a final recipe of 51 g/L `MRS broth (Sigma)` into 1 L distilled water.
- Preserve the dehydrated MRS broth composition as nested product composition or product metadata instead of adding it to the top-level ingredient list.
- Store distilled water with a volume unit, not `G_PER_L`.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after editing and regenerating the merged YAML.
- Check the adjacent MRS broth records for the same final-powder-versus-internal-composition flattening, because this source-family is likely to repeat the same importer mistake.

## Additional Notes

The review used gitignore-independent `rg --no-ignore --hidden` searches for `M2878` and `de_man_rogosa_and_sharpe_mrs_broth_sigma`, so ignored files were included in the duplicate/source scan.
