# YAML Record Review: modified_nautilia_lithotrophica_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_nautilia_lithotrophica_medium__34d88830.yaml
- Started UTC: 2026-09-24T12:33:55Z
- Finished UTC: 2026-09-24T12:33:55Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:003094`, `modified_nautilia_lithotrophica_medium`, generated from `data/normalized_yaml/bacterial/modified_nautilia_lithotrophica_medium.yaml`.
- The record represents JCM Medium J751 / MediaDive `mediadive.medium:J751`, named `MODIFIED NAUTILIA LITHOTROPHICA MEDIUM`.
- The generated record was compared with the maintained MediaDive normalized record, JCM `GRMD=751`, MediaDive `J751`, and the parallel TOGO `M776` import of the same JCM source.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- MediaDive `J751`, JCM `GRMD=751`, and TOGO `M776` all identify the same Modified Nautilia Lithotrophica Medium source recipe.
- A gitignore-independent duplicate check for the exact normalized name and JCM/MediaDive identifiers found a second maintained record, `data/normalized_yaml/bacterial/TOGO_M776_Modified_Nautilia_Lithotrophica_Medium.yaml`, and a second generated record, `data/merge_yaml/merged/MODIFIED_NAUTILIA_LITHOTROPHICA_MEDIUM.yaml`.
- No inspected JCM, MediaDive, or TOGO source payload identified a target organism beyond the medium name.

## Evidence

- JCM 751 lists a 900 ml basal recipe with NaCl, NaNO3, NH4Cl, KCl, CaCl2 x 2 H2O, MgCl2 x 6 H2O, HEPES, resazurin, 10 ml Trace minerals, 1 ml Selenite-tungstate solution, 12 g sulfur powder, and distilled water.
- JCM then lists four post-autoclave additions to the 900 ml basal medium: 20 ml 15% Sodium formate solution, 50 ml 5% NaHCO3 solution, 10 ml Trace vitamins, and 20 ml 3% Na2S x 9 H2O solution.
- MediaDive `J751` preserves the 10 ml Trace minerals and 1 ml Selenite-tungstate solution additions as solution references and embeds their separate 1000 ml stock recipes.
- The generated record flattens both stock recipes into the top-level ingredient list at stock concentration.
- The generated record stores the four post-autoclave milliliter additions as `Sodium formate` `20` `G_PER_L`, `NaHCO3` `50` `G_PER_L`, `Trace vitamins` `10` `G_PER_L`, and `Na2S x 9 H2O` `20` `G_PER_L`.

## Completeness

- Basal salts, HEPES, resazurin, sulfur, and all post-autoclave additions are recognizable by name.
- The 10 ml Trace minerals and 1 ml Selenite-tungstate solution additions are missing as structured solution additions.
- The four post-autoclave milliliter additions are present only with incorrect gram-per-liter units.
- The 900 ml basal water row and the two 1000 ml stock-water rows are absent.
- Sulfur powder is grounded as `CHEBI:26833`, `sulfur atom`, instead of elemental sulfur.

## Findings

- Blocker: nested Trace minerals and Selenite-tungstate stock recipes are flattened into top-level ingredients at stock concentration. For example, NaOH, Na2SeO3 x 5 H2O, and Na2WO4 x 2 H2O are components of the 1 L Selenite-tungstate stock, not direct additions to the basal medium.
- Blocker: four post-autoclave volume additions are converted to grams per liter. The source has 20 ml of 15% Sodium formate solution, 50 ml of 5% NaHCO3 solution, 10 ml Trace vitamins, and 20 ml of 3% Na2S x 9 H2O solution, not direct `20`, `50`, `10`, and `20` `G_PER_L` rows.
- Major: duplicate merging sums basal components with Trace minerals stock components. The generated `NaCl` row is `25.728` g/L from `24.728 + 1.0`, and `CaCl2 x 2 H2O` is `0.42640900000000004` g/L from `0.326409 + 0.1`.
- Major: source water rows are omitted for the 900 ml basal recipe and both embedded 1 L stocks.
- Major: `Sulfur (powder)` is grounded to `CHEBI:26833` with label `sulfur atom`, but the source ingredient is elemental sulfur powder.
- Major: the same JCM 751 medium is maintained under two CultureMech IDs, `CultureMech:003094` for MediaDive and `CultureMech:010184` for TOGO, and it generates two separate merged YAML records.

## Recommended Edits

- Preserve Trace minerals and Selenite-tungstate solution as 10 ml and 1 ml solution additions with nested or linked stock recipes.
- Preserve Sodium formate, NaHCO3, Trace vitamins, and Na2S x 9 H2O as post-autoclave milliliter additions with their source stock strengths.
- Restrict duplicate ingredient merging to one solution scope so basal salts are not summed with Trace minerals stock components.
- Preserve source water rows for the 900 ml basal recipe and the nested stocks if water is in scope for structured recipes.
- Re-ground sulfur powder to elemental sulfur, for example `CHEBI:33403`, after confirming the preferred local grounding for source `Sulfur (powder)`.
- Merge or explicitly cross-link MediaDive `J751` and TOGO `M776` before regeneration so JCM `GRMD=751` has one CultureMech identity.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting nested-stock handling and post-autoclave solution units.
- Recompare the regenerated record against JCM `GRMD=751`, including the 10 ml Trace minerals row, 1 ml Selenite-tungstate row, and all four post-autoclave additions.
- Confirm that generated YAML no longer contains both `modified_nautilia_lithotrophica_medium__34d88830.yaml` and `MODIFIED_NAUTILIA_LITHOTROPHICA_MEDIUM.yaml` as separate records for the same JCM recipe.

## Additional Notes

None found.
