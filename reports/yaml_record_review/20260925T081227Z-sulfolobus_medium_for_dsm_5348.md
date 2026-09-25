# YAML Record Review: Sulfolobus Medium (For DSM 5348)

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfolobus_medium_for_dsm_5348.yaml` (`CultureMech:008908`)
- Started UTC: `2026-09-25T08:12:27Z`
- Finished UTC: `2026-09-25T08:12:55Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfolobus_medium_for_dsm_5348.yaml` |
| Normalized source | `data/normalized_yaml/archaea/sulfolobus_medium_for_dsm_5348.yaml` |
| CultureMech ID | `CultureMech:008908` |
| Media term | `TOGO:M2320` |
| Original source | DSMZ Medium 88, Sulfolobus Medium, DSM 5348 variant |
| Merge fingerprint | `aae03af8e120a54326cabb0d97a644380aaf20e60b83921e92d550b9182c8dc0` |
| Merged from | `sulfolobus_medium_for_dsm_5348` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Failed; `linkml-reference-validator` reported 1 validation issue in a `doi:10.1128/AEM.02019-07` evidence snippet. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected `CultureMech:008908` identifier and `TOGO:M2320` source term for the DSM 5348-specific DSMZ 88 variant. Exact gitignore-independent searches with `--no-ignore --hidden` for `CultureMech:008908`, `TOGO:M2320`, the exact merge fingerprint, and `sulfolobus_medium_for_dsm_5348.yaml` found this normalized source and generated singleton as the only direct recipe records.

The source row set is recognizable: TOGO M2320 uses the DSMZ 88 salt base, omits yeast extract, and adds 0.5 g/L powdered sulfur plus 20 g/L sulfide ore. Hydrated salt groundings are partly plausible, but `MgSO4 x 7 H2O` still carries a generic magnesium sulfate legacy link, `VOSO4 x 2 H2O` still carries a legacy `MediaIngredientMech` term, and the TOGO payload imports the DSMZ Allen-stock heptahydrate as generic `CoSO4`.

## Evidence

DSMZ 88 says the DSM 5348 variant should omit yeast extract, add 0.50 g/L powdered sulfur and 20.00 g/L sulfide ore such as pyrite, sterilize sulfur separately by steaming for 3 hours on each of 3 successive days, sterilize ore by heating at 150 C overnight, and add sulfur and ore aseptically to the autoclaved medium.

TOGO M2320 preserves that wrapper over the DSMZ 88 salt base and keeps Allen's trace-element solution as a 10 ml referenced solution with a separate 1 L stock. The generated YAML flattens the Allen stock into top-level ingredients, turns stock milligram quantities into final `G_PER_L` rows such as `450 G_PER_L` Na2B4O7 x 10 H2O and `180 G_PER_L` MnCl2 x 4 H2O, and turns the Allen stock pH adjuster into a top-level `HCl` ingredient.

The generated record carries two target organisms and one supplemented variant from the normalized source. Reference validation fails for the Auernik 2008 `Metallosphaera sedula` snippet because the configured cache only exposes the abstract for `doi:10.1128/AEM.02019-07`.

## Completeness

The generated record is incomplete because the DSMZ salt-solution pH 2.0 preparation, separate sterilization of sulfur and sulfide ore, aseptic addition, Allen stock hierarchy, and Allen stock pH adjustment are absent or flattened.

`target_organisms` is present and scoped to direct or variant evidence, but the failed Auernik 2008 snippet needs repair before the DSM 5348 evidence is mechanically supported.

## Findings

- The generated singleton is stale relative to the normalized source: basal and Allen stock water are summed to `2000.0 G_PER_L`, while the normalized source has already been repaired to `1000.0 G_PER_L`.
- The 10 ml Allen trace-element solution addition became an empty `G_PER_L` solution object.
- Allen-stock milligram quantities are present as top-level final-medium `G_PER_L` concentrations.
- Sulfur steaming, ore dry-heat sterilization, and aseptic sulfur/ore addition are absent.
- The DSMZ salt-solution pH 2.0 step with 10 N H2SO4 and the Allen-stock pH 2 step with 1 N HCl became variable top-level acid ingredients.
- Reference validation fails for the Auernik 2008 snippet.
- `CoSO4 x 7 H2O` was imported as generic `CoSO4`.

## Recommended Edits

- Repair `data/normalized_yaml/archaea/sulfolobus_medium_for_dsm_5348.yaml` or the TOGO import path, then regenerate `data/merge_yaml/merged/sulfolobus_medium_for_dsm_5348.yaml`.
- Preserve Allen's trace-element solution as a nested 1 L stock added at 10 ml/L, and keep HCl scoped to that stock.
- Add preparation steps for pH 2.0 salt-solution adjustment, sulfur steaming on three successive days, sulfide ore heating at 150 C overnight, and aseptic sulfur and ore addition.
- Keep powdered sulfur and sulfide ore as DSM 5348 additions while continuing to omit yeast extract.
- Refresh the Auernik 2008 snippet so `linkml-reference-validator` can find it in cached reference content, or replace it with a snippet from available source text.
- Correct the CoSO4 hydrate loss and legacy `MgSO4 x 7 H2O` and `VOSO4 x 2 H2O` links while repairing the stock hierarchy.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `CultureMech:008908`, `TOGO:M2320`, `aae03af8e120a54326cabb0d97a644380aaf20e60b83921e92d550b9182c8dc0`, and `sulfolobus_medium_for_dsm_5348.yaml`.
- Verify that the regenerated record retains the curated target organisms and media variant while clearing the Auernik 2008 snippet failure.

## Additional Notes

Empty optional fields that are unrelated to source-backed stock structure, DSM 5348 preparation, and evidence snippets were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the maintained normalized TOGO source, evidence curation, and the stock-aware generation path.
