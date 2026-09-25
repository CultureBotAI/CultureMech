# YAML Record Review: Sulfolobus Medium (Anaerobic) (For DSM 2162)

- Repository: `/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CultureMech`
- Record: `data/merge_yaml/merged/sulfolobus_medium_anaerobic_for_dsm_2162.yaml` (`CultureMech:009226`)
- Started UTC: `2026-09-25T08:08:51Z`
- Finished UTC: `2026-09-25T08:09:23Z`
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Generated YAML | `data/merge_yaml/merged/sulfolobus_medium_anaerobic_for_dsm_2162.yaml` |
| Normalized source | `data/normalized_yaml/archaea/sulfolobus_medium_anaerobic_for_dsm_2162.yaml` |
| CultureMech ID | `CultureMech:009226` |
| Media term | `TOGO:M2670` |
| Original source | DSMZ Medium 88a, Sulfolobus Medium (Anaerobic), DSM 2162 variant |
| Merge fingerprint | `82009a0150729ff2738b730b008973a397435a1bb796cc2babd06d719490be0f` |
| Merged from | `sulfolobus_medium_anaerobic_for_dsm_2162` |

## Validation

| Check | Result |
| --- | --- |
| LinkML schema | Passed; `linkml-validate` reported `No issues found` for the generated YAML. |
| Strict validator | Passed; `scripts/validate_strict.py` reported 1 file, 0 total errors. |
| Reference validator | Failed; `linkml-reference-validator` reported 2 validation issues in evidence snippets. |
| Term validator | Passed; `linkml-term-validator` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` embedded in generated YAML. |

## Identity and Grounding

The generated record has the expected `CultureMech:009226` identifier and `TOGO:M2670` source term for the DSM 2162-specific DSMZ 88a variant. Exact gitignore-independent searches with `--no-ignore --hidden` for `CultureMech:009226`, `TOGO:M2670`, the exact merge fingerprint, and `sulfolobus_medium_anaerobic_for_dsm_2162.yaml` found this normalized source and generated singleton as the only direct recipe records.

The main variant identity is recoverable from TOGO M2670 and DSMZ 88a, but the generated YAML does not encode the source pH. TOGO M2670 exposes `ph: 5.5`, and DSMZ 88a says DSM 2161 and DSM 2162 should use 1.00 g/L yeast extract and adjust the medium to pH 5.5.

Simple salt groundings are partly plausible, but `MgSO4 x 7 H2O` still carries a generic magnesium sulfate legacy link, `VOSO4 x 2 H2O` still carries a legacy `MediaIngredientMech` term, and the TOGO payload imports the DSMZ Allen-stock heptahydrate as generic `CoSO4`.

## Evidence

TOGO M2670 uses the DSMZ 88a main solution with 1000 ml water, 1.3 g ammonium sulfate, 0.28 g KH2PO4, 0.25 g MgSO4 x 7 H2O, 0.07 g CaCl2 x 2 H2O, 0.02 g FeCl3 x 6 H2O, 10 g sulfur powder, 1 g OXOID yeast extract, 0.5 g Na2S x 9 H2O, 10 ml Allen trace-element solution, 1 N H2SO4, and 100% N2.

TOGO M2670 preserves Allen's trace-element solution separately as a 1 L stock with milligram quantities and 1 N HCl. The generated YAML flattens those milligram stock rows into top-level final `G_PER_L` ingredients, including `450 G_PER_L` Na2B4O7 x 10 H2O, `180 G_PER_L` MnCl2 x 4 H2O, `22 G_PER_L` ZnSO4 x 7 H2O, and `1 G_PER_L` CoSO4.

TOGO also keeps the DSMZ 88a procedural comments: adjust the salt solution to pH 4.0 with 1 N H2SO4, sparge with 100% N2, dispense under N2 into sulfur-containing anoxic vessels, sterilize for 1 to 2 hours on each of 3 successive days in a boiling-water bath, add sterile anoxic yeast-extract and sulfide stocks, adjust to pH 4.0 if necessary before inoculation, and use the pH 5.5 DSM 2162 modification. The generated YAML has no `preparation_steps`.

The generated record carries six `target_organisms` and two variants from the normalized source. The organism explanations are intentionally scoped to variants and say the aerobic Willard 2024 records are not verified on the anaerobic parent, but reference validation fails because one `doi:10.1128/mbio.01033-24` snippet is absent from the available abstract and no cached content is available for `doi:10.1099/ijsem.0.001881`.

## Completeness

The generated record is incomplete because the pH 5.5 DSM 2162 variant setting, the anaerobic pH 4.0 preparation context, N2 sparging and dispensing, sulfur-in-vessel handling, separate yeast-extract and sulfide stocks, three-day boiling-water sterilization, and Allen stock hierarchy are absent or flattened.

`target_organisms` is present and scoped to media variants. The variant scoping avoids asserting direct growth on TOGO M2670, but its evidence snippets need repair before the citations are mechanically supported.

## Findings

- The source-backed DSM 2162 `ph: 5.5` value is absent from the generated record.
- The generated singleton is stale relative to the normalized source: basal and Allen stock water are summed to `2000.0 G_PER_L`, while the normalized source has already been repaired to `1000.0 G_PER_L`.
- The 10 ml Allen trace-element addition became an empty `G_PER_L` solution object, and Allen-stock milligram quantities were promoted to top-level `G_PER_L` rows.
- The generated record omits all DSMZ 88a and DSM 2162-specific preparation comments.
- `1 N H2SO4`, `N2 gas`, and `1 N HCl` are variable top-level ingredient rows instead of pH-adjustment, gas-atmosphere, and stock-adjustment instructions.
- Reference validation fails for the stored Willard 2024 and Sakai 2017 snippets.
- `CoSO4 x 7 H2O` was imported as generic `CoSO4`.

## Recommended Edits

- Repair `data/normalized_yaml/archaea/sulfolobus_medium_anaerobic_for_dsm_2162.yaml` or the TOGO import path, then regenerate `data/merge_yaml/merged/sulfolobus_medium_anaerobic_for_dsm_2162.yaml`.
- Encode DSM 2162's pH 5.5 setting explicitly while retaining the DSMZ 88a anaerobic handling steps needed to build the variant.
- Preserve Allen's trace-element solution as a nested 1 L stock added at 10 ml/L, with Allen-stock quantities and the 1 N HCl pH adjustment scoped to that stock.
- Recast 1 N H2SO4 and 100% N2 as procedural requirements rather than final ingredient defaults.
- Refresh the two evidence snippets so `linkml-reference-validator` can find them in cached reference content, or replace them with snippets from available source text.
- Correct the CoSO4 hydrate loss and legacy `MgSO4 x 7 H2O` and `VOSO4 x 2 H2O` links while repairing the stock hierarchy.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regenerating the merged YAML.
- Re-run exact gitignore-independent searches for `CultureMech:009226`, `TOGO:M2670`, `82009a0150729ff2738b730b008973a397435a1bb796cc2babd06d719490be0f`, and `sulfolobus_medium_anaerobic_for_dsm_2162.yaml`.
- Confirm the regenerated record has pH 5.5, the 1 g/L yeast extract variant amount, and stock-scoped Allen trace quantities.

## Additional Notes

Empty optional fields that are unrelated to stock hierarchy, DSM 2162 pH, and evidence snippets were not treated as defects.

The generated YAML should not be hand-edited. The review findings target the maintained normalized TOGO source, evidence curation, and the stock-aware generation path.
