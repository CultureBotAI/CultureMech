# YAML Record Review: modified_picrophilus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_picrophilus_medium__2e13d4cd.yaml
- Started UTC: 2026-09-24T12:51:33Z
- Finished UTC: 2026-09-24T12:52:22Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:002433`, `modified_picrophilus_medium`, generated from `data/normalized_yaml/archaea/modified_picrophilus_medium.yaml`.
- The record represents MediaDive `J1267`, sourced from JCM `GRMD=1267`, named `MODIFIED PICROPHILUS MEDIUM`.
- The generated MediaDive record was compared with MediaDive `J1267`, JCM `GRMD=1267`, and the parallel TOGO `M1363` import of the same JCM source.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` reported no issues.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` exited 0 with no diagnostics.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- MediaDive `J1267`, TOGO `M1363`, and JCM `GRMD=1267` all identify the same Modified Picrophilus Medium recipe.
- A gitignore-independent exact search for the JCM/MediaDive identifiers found a parallel TOGO maintained record, `data/normalized_yaml/archaea/TOGO_M1363_Modified_Picrophilus_Medium.yaml`, and a separate generated record, `data/merge_yaml/merged/MODIFIED_PICROPHILUS_MEDIUM.yaml`, for the same JCM 1267 source.
- `Fe2(SO4)3`, `Tryptone`, `Yeast extract`, and `MnSO4 x n H2O` have no CHEBI or local MIM grounding in this generated record.
- No inspected source payload identified a target organism for this medium.

## Evidence

- JCM lists a basal medium with 0.2 g ammonium sulfate, 0.5 g MgSO4 x 7 H2O, 0.25 g CaCl2 x 2 H2O, and 1 L distilled water.
- JCM instructs adjusting pH to 2.0-2.5 with H2SO4 and autoclaving before filter-sterilized additions of 11.1 ml 10 percent Tryptone solution, 11.1 ml 10 percent Yeast extract solution, 88.8 ml 10 percent Fe2(SO4)3 solution in 0.01 N H2SO4, 2 ml Wolfe's mineral elixir, and 2 ml Vitamin solution.
- JCM's local Vitamin solution contains 50 mg Vitamin B12, 50 mg DL-Calcium pantothenate, 50 mg Riboflavin, 10 mg Pyridoxine-HCl, 20 mg Biotin, 20 mg Folic acid, 25 mg Nicotinic acid, 25 mg Nicotine amide, 50 mg Lipoic acid, 50 mg p-Aminobenzoic acid, 50 mg Thiamine-HCl, and 1 L distilled water.
- MediaDive expands Wolfe's mineral elixir as a 1 L stock containing 14 mineral salts, including 30 g MgSO4 x 7 H2O and 1 g CaCl2 x 2 H2O.

## Completeness

- Basal ammonium sulfate, MgSO4 x 7 H2O, and CaCl2 x 2 H2O are present.
- The 10 percent Tryptone, Yeast extract, and Fe2(SO4)3 additions are flattened as final grams-per-liter rows.
- The local Vitamin solution and Wolfe's mineral elixir are flattened into top-level rows with stock concentrations instead of being scoped under stock recipes.
- Wolfe's mineral elixir MgSO4 x 7 H2O and CaCl2 x 2 H2O stock rows are merged with the basal MgSO4 x 7 H2O and CaCl2 x 2 H2O rows.
- Neither the basal 1 L water nor the Vitamin solution 1 L water is represented.

## Findings

- Blocker: stock and post-autoclave additions are flattened as final ingredients. The source adds 11.1 ml 10 percent Tryptone solution, 11.1 ml 10 percent Yeast extract solution, 88.8 ml 10 percent Fe2(SO4)3 solution, 2 ml Vitamin solution, and 2 ml Wolfe's mineral elixir, but the generated record lists their stock members as top-level `G_PER_L` rows.
- Blocker: the Wolfe's mineral elixir MgSO4 x 7 H2O and CaCl2 x 2 H2O stock rows are merged with the basal MgSO4 and CaCl2 rows, producing `30.44843` and `1.224215` `G_PER_L` rows that mix final basal concentrations with stock-strength Wolfe's rows.
- Blocker: local Vitamin solution components are stock concentrations that are not scaled by the 2 ml addition. For example, 50 mg Vitamin B12 in 1 L Vitamin solution becomes `0.05` `G_PER_L` in the final medium.
- Major: the same JCM 1267 medium is maintained and generated twice, once through MediaDive `J1267` and once through TOGO `M1363`.

## Recommended Edits

- Preserve 10 percent Tryptone, 10 percent Yeast extract, 10 percent Fe2(SO4)3, Vitamin solution, and Wolfe's mineral elixir as source milliliter additions or scale their contents to final concentrations with provenance intact.
- Keep Wolfe's MgSO4 x 7 H2O and CaCl2 x 2 H2O rows scoped under the Wolfe's mineral elixir stock so they cannot merge with the basal salts.
- Preserve the local Vitamin solution as a stock recipe with its own 1 L water row.
- Merge or explicitly cross-link the TOGO `M1363` and MediaDive `J1267` maintained records before regeneration so JCM `GRMD=1267` has one CultureMech identity.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting MediaDive solution flattening.
- Recompare the regenerated record against MediaDive `J1267` and JCM `GRMD=1267`, including all five filter-sterilized additions, the local Vitamin solution, and Wolfe's mineral elixir.
- Confirm that generated YAML no longer contains both `MODIFIED_PICROPHILUS_MEDIUM.yaml` and `modified_picrophilus_medium__2e13d4cd.yaml` as separate records for the same JCM recipe.

## Additional Notes

None found.
