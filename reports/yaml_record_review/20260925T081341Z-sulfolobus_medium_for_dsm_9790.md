# YAML Record Review: Sulfolobus Medium (For DSM 9790)

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfolobus_medium_for_dsm_9790.yaml` (`CultureMech:008911`)
- Started UTC: `2026-09-25T08:13:41Z`
- Finished UTC: `2026-09-25T08:14:09Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfolobus_medium_for_dsm_9790.yaml` |
| Normalized sources | `data/normalized_yaml/archaea/sulfolobus_medium_for_dsm_9790.yaml`, `data/normalized_yaml/archaea/TOGO_M2385_Sulfolobus_Medium.yaml` |
| CultureMech ID | `CultureMech:008911` |
| Media term | `TOGO:M2323` |
| Original source | DSMZ Medium 88, Sulfolobus Medium, DSM 9790 variant |
| Merge fingerprint | `d1b577bef3fefc600d1dab9153d77440c9fde75ca728d2a8afac6abd9d0519ba` |
| Merged from | `TOGO_M2385_Sulfolobus_Medium`, `sulfolobus_medium_for_dsm_9790` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record carries the expected `CultureMech:008911` identifier and `TOGO:M2323` source term for the DSM 9790-specific DSMZ 88 variant. Exact gitignore-independent searches with `--no-ignore --hidden` for `CultureMech:008911`, `TOGO:M2323`, the merge fingerprint, `sulfolobus_medium_for_dsm_9790.yaml`, and `TOGO_M2385_Sulfolobus_Medium.yaml` found the two normalized source files and this generated merge as expected.

The merge grouping is not grounded against the current normalized sources. Generic TOGO M2385 has 1 g/L OXOID yeast extract, while the maintained TOGO M2323 source now has the DSMZ 88 DSM 9790 variant amount of 2 g/L yeast extract.

Hydrated salt groundings are partly plausible, but `MgSO4 x 7 H2O` still carries a generic magnesium sulfate legacy link, `VOSO4 x 2 H2O` still carries a legacy `MediaIngredientMech` term, and TOGO imports the DSMZ Allen-stock heptahydrate as generic `CoSO4`.

## Evidence

DSMZ 88 says DSM 9789 and DSM 9790 should use 2.00 g/L yeast extract and adjust the medium to pH 1.0 by using 300 ml 0.5 M H2SO4 plus 700 ml distilled water to dissolve the salts.

TOGO M2323 preserves the 2 g yeast-extract row and keeps Allen's trace-element solution as a 10 ml referenced solution with a separate 1 L stock. The generated YAML is stale: it still shows `1 G_PER_L` yeast extract, matching the generic TOGO M2385 source rather than M2323.

Both TOGO sources flatten Allen's trace-element stock into an empty `Allen's trace element solution` plus top-level stock components. In the generated record, milligram stock entries become final `G_PER_L` rows, and the basal and Allen-stock water rows have also been summed to `2000.0 G_PER_L`.

The generated record carries one `Picrophilus oshimae` target organism from a provenance review. That assertion is linked to the DSMZ DSM 9790 catalogue entry and survives validation.

## Completeness

The generated record is incomplete because it lacks the DSM 9790 pH 1.0 water/H2SO4 recipe, keeps the wrong yeast concentration, omits the DSMZ pH 2.0 basal salt-solution preparation, and flattens the Allen stock hierarchy.

`target_organisms` is present for DSM 9790 and is consistent with the named variant.

## Findings

- Generic TOGO M2385 and DSM 9790-specific TOGO M2323 are over-merged even though M2323 uses 2 g/L yeast extract and M2385 uses 1 g/L.
- The generated record is stale relative to the normalized M2323 source: it still has `1 G_PER_L` yeast extract instead of `2 G_PER_L`.
- The DSM 9790 pH 1.0 preparation using 300 ml 0.5 M H2SO4 plus 700 ml water is not encoded.
- The 10 ml Allen trace-element solution addition became an empty `G_PER_L` solution object.
- Allen-stock milligram quantities are present as top-level final-medium `G_PER_L` concentrations.
- The basal 1 L water and Allen stock 1 L water are summed into `2000.0 G_PER_L`.
- `H2SO4` and `HCl` are variable top-level ingredient rows instead of scoped pH-adjustment instructions.
- `CoSO4 x 7 H2O` was imported as generic `CoSO4`.

## Recommended Edits

- Repair `data/normalized_yaml/archaea/sulfolobus_medium_for_dsm_9790.yaml` or the TOGO import path, then regenerate `data/merge_yaml/merged/sulfolobus_medium_for_dsm_9790.yaml`.
- Split TOGO M2323 from generic TOGO M2385 because their yeast-extract concentrations and final pH preparations differ.
- Encode the DSM 9790 pH 1.0 preparation using 300 ml 0.5 M H2SO4 and 700 ml distilled water.
- Preserve Allen's trace-element solution as a nested 1 L stock added at 10 ml/L, with Allen-stock quantities and the 1 N HCl pH adjustment scoped to that stock.
- Keep the curated `Picrophilus oshimae` target organism when regenerating the merged YAML.
- Correct the CoSO4 hydrate loss and legacy `MgSO4 x 7 H2O` and `VOSO4 x 2 H2O` links while repairing the stock hierarchy.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `CultureMech:008911`, `TOGO:M2323`, `d1b577bef3fefc600d1dab9153d77440c9fde75ca728d2a8afac6abd9d0519ba`, `TOGO_M2385_Sulfolobus_Medium.yaml`, and `sulfolobus_medium_for_dsm_9790.yaml`.
- Confirm the regenerated DSM 9790 record has 2 g/L yeast extract and pH 1.0 and no longer claims TOGO M2385 as a source duplicate.

## Additional Notes

Empty optional fields that are unrelated to source-backed stock structure, DSM 9790 preparation, and target-organism evidence were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the maintained normalized TOGO sources and merge grouping.
