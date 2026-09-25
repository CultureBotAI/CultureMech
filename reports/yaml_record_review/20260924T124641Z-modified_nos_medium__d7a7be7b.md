# YAML Record Review: modified_nos_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_nos_medium__d7a7be7b.yaml
- Started UTC: 2026-09-24T12:46:41Z
- Finished UTC: 2026-09-24T12:48:08Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:002503`, `modified_nos_medium`, generated from `data/normalized_yaml/bacterial/modified_nos_medium.yaml`.
- The record represents MediaDive `J144`, sourced from JCM `GRMD=144`, named `MODIFIED NOS MEDIUM`.
- The generated MediaDive record was compared with MediaDive `J144`, JCM `GRMD=144`, and the parallel TOGO `M135` import of the same JCM source.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` reported no issues.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` exited 0 after reporting 1 validated file and no failure diagnostics.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- MediaDive `J144`, TOGO `M135`, and JCM `GRMD=144` all identify the same Modified NOS Medium recipe.
- A gitignore-independent duplicate check with word-boundary-anchored JCM/TOGO/MediaDive identifiers found a parallel TOGO maintained record, `data/normalized_yaml/bacterial/TOGO_M135_Modified_NOS_Medium.yaml`, and a separate generated record, `data/merge_yaml/merged/MODIFIED_NOS_MEDIUM.yaml`, for the same JCM 144 source.
- `Heart Infusion Broth`, `Trypticase peptone`, `Yeast extract`, and `Rabbit serum` have no primary ontology grounding in this record.
- No inspected source payload identified a target organism for this medium.

## Evidence

- JCM lists a 94 ml basal formulation with Heart infusion broth, Trypticase peptone, Yeast extract, Sodium thioglycolate, L-Cysteine HCl x H2O, L-Asparagine, Glucose, and 0.1 ml 0.1 percent Resazurin solution.
- JCM then instructs boiling the medium while flushing with oxygen-free N2-H2-CO2 gas at 85:10:5, autoclaving anaerobically, cooling, and adding filter-sterilized 2.67 ml 7.5 percent NaHCO3 solution, 2.0 ml TPP/VFA mixture, and 2.0 ml heat-inactivated rabbit serum.
- The JCM TPP/VFA mixture is 1.5 ml 0.2 percent Thiamine pyrophosphate, 1.0 ml VFA solution, and 8.4 ml distilled water.
- The JCM VFA solution is 0.5 ml each of Isobutyric acid, 2-Methylbutyric acid, Isovaleric acid, and Valeric acid, plus 100 ml 0.1 N NaOH.
- MediaDive preserves `TPP/VFA mixture` and nested `VFA solution` as named stock solutions.

## Completeness

- Basal gram-scale ingredients and the JCM gas-exchange text are present.
- The Resazurin, NaHCO3, Rabbit serum, TPP/VFA mixture, Thiamine pyrophosphate, VFA solution, VFA acid, and NaOH milliliter additions are flattened into top-level grams-per-liter ingredients or omitted.
- 2-Methylbutyric acid is absent even though it is present in both JCM and MediaDive.
- The 94 ml basal distilled water and 8.4 ml TPP/VFA distilled water rows are absent.
- Tryptone, generic Yeast extract, and Sodium chloride rows from LB Medium were appended even though JCM `GRMD=144` and MediaDive `J144` do not list LB Medium as an ingredient.

## Findings

- Blocker: source milliliter solution additions are represented as final grams per liter. Examples include 0.1 ml Resazurin solution as `0.1` `G_PER_L`, 2.67 ml NaHCO3 solution as `2.67` `G_PER_L`, 2.0 ml Rabbit serum as `2` `G_PER_L`, 1.5 ml Thiamine pyrophosphate stock as `1.5` `G_PER_L`, and 100 ml 0.1 N NaOH inside the VFA stock as `100` `G_PER_L`.
- Blocker: the TPP/VFA mixture and nested VFA solution stock hierarchy is lost, so their members are top-level final ingredients rather than scoped stock components.
- Blocker: 0.5 ml 2-Methylbutyric acid is missing from the VFA solution.
- Major: 10 g/L Tryptone, 5 g/L generic Yeast extract, and 10 g/L Sodium chloride from LB Medium are appended without support from the JCM or MediaDive source.
- Major: the same JCM 144 medium is maintained and generated twice, once through MediaDive `J144` and once through TOGO `M135`.

## Recommended Edits

- Preserve Resazurin, NaHCO3, Rabbit serum, TPP/VFA mixture, Thiamine pyrophosphate, VFA solution, and 0.1 N NaOH as milliliter additions rather than gram-per-liter ingredients.
- Preserve TPP/VFA mixture and VFA solution as nested stock recipes with their source volumes and scoped distilled water.
- Add 2-Methylbutyric acid back to the VFA solution.
- Remove LB Medium constituent rows unless a maintained source actually contains an LB Medium commercial product.
- Merge or explicitly cross-link the TOGO `M135` and MediaDive `J144` maintained records before regeneration so JCM `GRMD=144` has one CultureMech identity.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting MediaDive solution flattening and the commercial-product enrichment.
- Recompare the regenerated record against MediaDive `J144` and JCM `GRMD=144`, including both solution scopes, all four VFA acids, the distilled-water rows, and the 85:10:5 gas mixture.
- Confirm that generated YAML no longer contains both `MODIFIED_NOS_MEDIUM.yaml` and `modified_nos_medium__d7a7be7b.yaml` as separate records for the same JCM recipe.

## Additional Notes

None found.
