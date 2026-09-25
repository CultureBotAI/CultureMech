# YAML Record Review: Sulfolobus Medium (Anaerobic)

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfolobus_medium_anaerobic.yaml` (`CultureMech:008970`)
- Started UTC: `2026-09-25T08:06:34Z`
- Finished UTC: `2026-09-25T08:07:02Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfolobus_medium_anaerobic.yaml` |
| Normalized source | `data/normalized_yaml/archaea/sulfolobus_medium_anaerobic.yaml` |
| CultureMech ID | `CultureMech:008970` |
| Media term | `TOGO:M2387` |
| Original source | DSMZ Medium 88a, Sulfolobus Medium (Anaerobic) |
| Merge fingerprint | `c03016f0bf37e3be697158242759072d87c44c374d5d1fe9ea7734ced20c3168` |
| Merged from | `sulfolobus_medium_anaerobic` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Passed; `linkml-reference-validator` reported 1 file, 0 checks, all passed. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected `CultureMech:008970` identifier and `TOGO:M2387` media term for DSMZ Medium 88a. Exact gitignore-independent searches with `--no-ignore --hidden` for `CultureMech:008970`, `TOGO:M2387`, and the merge fingerprint found this TOGO source and generated singleton as the only direct owner of the stable identifier, source term, and fingerprint.

An exact gitignore-independent search for `sulfolobus_medium_anaerobic.yaml` also found that the same source file is included in `data/merge_yaml/merged/sulfolobus_medium_anaerobic__101bcc40.yaml`. That means the generated tree currently has two outputs claiming the same normalized source.

The main salt groundings are partly plausible, but `MgSO4 x 7 H2O` still carries a generic magnesium sulfate legacy link, `VOSO4 x 2 H2O` still carries a legacy `MediaIngredientMech` term, and `CoSO4` loses the `x 7 H2O` hydrate state present in DSMZ Medium 88a.

## Evidence

DSMZ 88a contains 1.3 g ammonium sulfate, 0.28 g KH2PO4, 0.25 g MgSO4 x 7 H2O, 0.07 g CaCl2 x 2 H2O, 0.02 g FeCl3 x 6 H2O, 10 ml Allen trace-element solution, 10 g sulfur powder, 0.5 g OXOID yeast extract, 0.5 g Na2S x 9 H2O, and 1000 ml distilled water.

The TOGO M2387 payload preserves the main solution in paragraph 1, stores the Allen trace-element solution as a 10 ml referenced component, and stores the 1 L Allen stock separately in paragraph 5 with milligram quantities for Na2MoO4 x 2 H2O, MnCl2 x 4 H2O, ZnSO4 x 7 H2O, CuCl2 x 2 H2O, VOSO4 x 2 H2O, Na2B4O7 x 10 H2O, and CoSO4.

DSMZ 88a also instructs the curator to adjust the salt solution to pH 4.0 with 1 N H2SO4, sparge the medium with 100% N2, dispense under the same gas into anoxic Hungate tubes or serum vials containing sulfur, sterilize by heating the vessels in boiling water for 1 to 2 hours on each of 3 successive days, add yeast extract and sulfide from sterile anoxic stock solutions prepared under 100% N2, and check and adjust pH to 4.0 before inoculation.

The generated YAML flattens the Allen stock into the main ingredient list, promotes milligram stock entries to final `G_PER_L` quantities such as `450 G_PER_L` Na2B4O7 x 10 H2O and `180 G_PER_L` MnCl2 x 4 H2O, sums the basal and Allen-stock water to `2000.0 G_PER_L`, and retains only an empty `Allen's trace element solution` in `solutions`.

## Completeness

The generated record is incomplete because it lacks the 10 ml/L Allen stock hierarchy, the pH 4.0 medium setting, sulfur-in-vessel handling, 100% N2 sparging and dispensing, three-day boiling-water sterilization, and separate sterile anoxic yeast-extract and sodium sulfide stocks.

`target_organisms` is absent. DSMZ 88a lists strain-specific use notes for DSM 2161 and DSM 2162 but does not assert growth observations, so no growth target was inferred.

## Findings

- The generated singleton is stale or duplicated: `sulfolobus_medium_anaerobic.yaml` is also folded into `sulfolobus_medium_anaerobic__101bcc40.yaml`.
- The basal 1 L water and Allen stock 1 L water are summed into `2000.0 G_PER_L`, while the normalized source has since been repaired back to a single `1000.0 G_PER_L` water row.
- The 10 ml Allen trace-element solution addition became an empty `G_PER_L` solution object.
- Allen stock milligram quantities are present as top-level final-medium `G_PER_L` concentrations.
- DSMZ 88a pH 4.0 and anaerobic preparation requirements are absent.
- `H2SO4`, `N2`, and `HCl` are variable top-level rows instead of pH-adjustment and gas-atmosphere instructions.
- `CoSO4 x 7 H2O` was imported as generic `CoSO4`.

## Recommended Edits

- Repair `data/normalized_yaml/archaea/sulfolobus_medium_anaerobic.yaml` or the TOGO import path, then regenerate `data/merge_yaml/merged/sulfolobus_medium_anaerobic.yaml`.
- Ensure each normalized source appears in only one generated merge output; either remove the stale singleton during generation or exclude this source from the suffixed duplicate cluster.
- Keep Allen's trace-element solution as a nested 1 L stock added at 10 ml/L, with the Allen stock's milligram quantities and pH 2 HCl adjustment scoped to the stock.
- Add pH 4.0, 1 N H2SO4, 100% N2 sparging, anoxic dispensing into sulfur-containing vessels, three successive boiling-water sterilization cycles, and separate sterile anoxic yeast-extract and sodium sulfide stock steps.
- Correct the CoSO4 hydrate loss and legacy `MgSO4 x 7 H2O` and `VOSO4 x 2 H2O` links while repairing the stock hierarchy.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `CultureMech:008970`, `TOGO:M2387`, `c03016f0bf37e3be697158242759072d87c44c374d5d1fe9ea7734ced20c3168`, and `sulfolobus_medium_anaerobic.yaml`.
- Verify that only one generated record names `data/normalized_yaml/archaea/sulfolobus_medium_anaerobic.yaml` as a source.

## Additional Notes

Empty optional fields that are unrelated to source-backed growth evidence and anaerobic stock reconstruction were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the maintained normalized TOGO source, the TOGO stock importer, and stale merge-output cleanup.
