# YAML Record Review: modified_methanohalophilus_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/modified_methanohalophilus_medium__b457469f.yaml
- Started UTC: 2026-09-24T12:19:28Z
- Finished UTC: 2026-09-24T12:19:28Z
- Verdict: needs curation

## Target

- Reviewed merged record `CultureMech:000289`, `modified_methanohalophilus_medium`, generated from `data/normalized_yaml/archaea/modified_methanohalophilus_medium.yaml`.
- The record represents JCM Medium J1218 / MediaDive `mediadive.medium:J1218`, named `MODIFIED METHANOHALOPHILUS MEDIUM`.
- The generated record was compared with the maintained MediaDive normalized record and with the JCM and TOGO source representations for JCM `GRMD=1218`.

## Validation

- LinkML open-schema validation: passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 1 file scanned, 0 files with errors, and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported 0 reference checks and no failures.
- Term validation: passed; `linkml-term-validator` exited 0 and printed `Validation passed`.
- Embedded `curation_history` entries were not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- MediaDive `J1218`, JCM `GRMD=1218`, and TOGO `M1307` all describe the same source recipe for Modified Methanohalophilus Medium.
- A gitignore-independent duplicate check for the exact normalized name and JCM/MediaDive identifiers found a second maintained record, `data/normalized_yaml/archaea/TOGO_M1307_Modified_Methanohalophilus_Medium.yaml`, and a second generated record, `data/merge_yaml/merged/MODIFIED_METHANOHALOPHILUS_MEDIUM.yaml`, for the same JCM medium.
- No inspected JCM, MediaDive, or TOGO source payload identified a target organism; the generated MediaDive record correspondingly has no target organism assertion.

## Evidence

- JCM lists the autoclaved base recipe as NaCl, KCl, MgCl2 x 6 H2O, CaCl2 x 2 H2O, NH4Cl, K2HPO4, 10 ml Trace minerals, 10 ml Trace vitamins, yeast extract, Trypticase peptone, resazurin, and 920 ml distilled water.
- JCM then instructs adding 50 ml of 8% NaHCO3 solution, 10 ml of 1.4% Coenzyme M solution, and 20 ml of 1 M Trimethylamine-HCl solution after cooling as filter-sterilized stocks, then adding 5 ml of 5% Na2S x 9 H2O solution per liter after distribution under N2:CO2.
- MediaDive `J1218` carries the same 10 ml Trace minerals and 10 ml Trace vitamins solution additions in its main `J1218` solution; the embedded Trace minerals stock has its own 1000 ml water context, and the Trace vitamins stock has its own 1000 ml water context.
- The generated MediaDive record flattens the Trace minerals and Trace vitamins stock recipes into top-level ingredients at their stock concentrations.
- The generated MediaDive record stores 50 ml NaHCO3, 10 ml Coenzyme M, 20 ml Trimethylamine-HCl, and 5 ml Na2S x 9 H2O as `50`, `10`, `20`, and `5` `G_PER_L`, losing the source stock percentages or molarity and the milliliter addition units.

## Completeness

- The base salts, yeast extract, Trypticase peptone, and resazurin are present.
- The 10 ml Trace minerals and 10 ml Trace vitamins additions are not preserved as first-class additions; their stock components are flattened into the top-level ingredient list.
- The four post-autoclave solution additions are present only as mis-typed compound concentrations, not as milliliter solution additions with their stock strengths.
- The 920 ml base-water row and the two 1000 ml stock-water rows are absent from the generated MediaDive record.
- The duplicate TOGO record keeps gas entries and empty solution cross-references instead of being reconciled with this MediaDive record.

## Findings

- Blocker: MediaDive solution additions are represented as grams per liter when the source gives milliliter additions of prepared stocks. The source has `50 ml` of `8% NaHCO3 solution`, `10 ml` of `1.4% Coenzyme M solution`, `20 ml` of `1 M Trimethylamine-HCl solution`, and `5 ml` of `5% Na2S x 9 H2O solution`; the generated record instead has `NaHCO3` at `50` `G_PER_L`, `Coenzyme M` at `10` `G_PER_L`, `Trimethylamine-HCl` at `20` `G_PER_L`, and `Na2S x 9 H2O` at `5` `G_PER_L`.
- Blocker: nested Trace minerals and Trace vitamins stocks are flattened into the main ingredient list at stock concentration. For example, 0.002 g/L biotin is the concentration inside the Trace vitamins liter stock, not a top-level concentration in a medium that uses only 10 ml of that stock.
- Major: duplicate consolidation sums compounds across main-medium and Trace minerals scopes. The generated `NaCl` value is `118.073` g/L from `117.073 + 1.0`, and the generated `CaCl2 x 2 H2O` value is `0.490244` g/L from `0.390244 + 0.1`; the second addend in each case belongs to the Trace minerals stock.
- Major: water rows are dropped for the main recipe and both nested stock solutions, making the three solution contexts less auditable.
- Major: the same JCM 1218 medium is maintained under two CultureMech IDs, `CultureMech:000289` for MediaDive and `CultureMech:007842` for TOGO, and it generates two separate merged YAML records.

## Recommended Edits

- Preserve `ml` stock additions from MediaDive as structured solutions, including the source stock strengths for 8% NaHCO3, 1.4% Coenzyme M, 1 M Trimethylamine-HCl, and 5% Na2S x 9 H2O.
- Preserve the 10 ml Trace minerals and 10 ml Trace vitamins additions as solution references or nested solution recipes rather than flattening their stock components at 1 L strength into the main ingredient array.
- Restrict duplicate compound merging to a single solution scope so base NaCl and CaCl2 x 2 H2O are not summed with Trace minerals stock components.
- Carry source water rows for the 920 ml base and the two 1000 ml stocks if structured water rows are in scope for curated recipes.
- Merge or explicitly cross-link the MediaDive `J1218` and TOGO `M1307` maintained records before regenerating so JCM `GRMD=1218` has one CultureMech identity.

## Follow-up Checks

- Re-run open-schema, strict, reference, and term validation after correcting the MediaDive import or normalized YAML.
- Diff the regenerated record against the JCM 1218 table to verify that gram quantities, milliliter additions, and stock labels are no longer conflated.
- Confirm that the generated merged directory contains one record for JCM `GRMD=1218` after MediaDive/TOGO de-duplication.

## Additional Notes

- The `high_metal: true` flag on the generated record may be downstream fallout from flattening Trace minerals into top-level ingredients; recompute derived flags after the stock boundaries are fixed.
