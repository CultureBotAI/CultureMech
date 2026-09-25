# YAML Record Review: methanocalculus_halotolerans_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/methanocalculus_halotolerans_medium__2e7ace4c.yaml`
- Started UTC: 2026-09-24T03:17:39Z
- Finished UTC: 2026-09-24T03:17:40Z
- Verdict: needs curation

## Target

- Stable ID: `CultureMech:002073`
- Label: `methanocalculus_halotolerans_medium`
- Category: `archaea`
- Maintained owner: `data/normalized_yaml/archaea/methanocalculus_halotolerans_medium.yaml`
- Source identity: MediaDive/DSMZ medium 905, `METHANOCALCULUS HALOTOLERANS MEDIUM`

## Validation

- Open schema: Passed; `linkml-validate` reported no issues.
- Strict validator: Passed; 1 file scanned, 0 files with errors, and 0 error rows.
- Reference validator: Passed; 0 reference checks were applicable.
- Term validator: Passed.
- Embedded history: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

- The generated record and its normalized owner are byte-equivalent at the reviewed scope, so the curation errors are present in the source-owned normalized YAML rather than introduced only during merge generation.
- `media_term` grounds the recipe to `mediadive.medium:905`, consistent with DSMZ medium 905.
- Exact ignored-file search for `mediadive.medium:905`, `DSMZ_Medium905.pdf`, `methanocalculus_halotolerans_medium`, and `CultureMech:002073` also found `data/normalized_yaml/archaea/KOMODO_905_METHANOCALCULUS_HALOTOLERANS_medium.yaml`, which appears to be a sibling record for the same DSMZ medium number and should be reviewed for deduplication or an explicit source-distinct rationale.
- Ingredient grounding is mostly specific for salts and reductants, but `Trypticase` is incorrectly grounded to `CHEBI:78018` / dodecylphosphocholine even though the MediaDive source compound is the peptone product `Trypticase BD BBL`.

## Evidence

- The DSMZ/MediaDive 905 source defines a 1010 ml final medium containing 10 ml of `Modified Wolin's mineral solution`.
- The 905 final recipe has 50 g NaCl, 0.6 g `CaCl2 x 2 H2O`, 3.2 g `MgCl2 x 6 H2O`, 2 g `NaHCO3`, 0.5 g each of Na-acetate, yeast extract, Trypticase, and `L-Cysteine HCl x H2O`, 0.3 g `Na2S x 9 H2O`, and 0.5 ml of 0.1% resazurin in 1000 ml water plus stock additions.
- The 10 ml `Modified Wolin's mineral solution` stock points to DSMZ/MediaDive solution 241, whose 1 L stock contains nitrilotriacetic acid, `MgSO4 x 7 H2O`, `MnSO4 x H2O`, NaCl, `FeSO4 x 7 H2O`, `CoSO4 x 7 H2O`, `CaCl2 x 2 H2O`, `ZnSO4 x 7 H2O`, `CuSO4 x 5 H2O`, `AlK(SO4)2 x 12 H2O`, `H3BO3`, `Na2MoO4 x 2 H2O`, `NiCl2 x 6 H2O`, `Na2SeO3 x 5 H2O`, and `Na2WO4 x 2 H2O`.
- The stock preparation first dissolves nitrilotriacetic acid, adjusts pH to 6.5 with KOH, adds minerals, and then adjusts the stock to pH 7.0 with KOH.

## Completeness

- The source has enough final-medium and stock-solution detail to encode the medium without unresolved amounts.
- Empty `target_organisms`, `growth_data`, and `protocols` are optional-field omissions, not review findings for this record.

## Findings

- Blocker: the 10 ml `Modified Wolin's mineral solution` addition is not represented as a structured stock solution. Every solution 241 compound was flattened into top-level `ingredients`, so stock membership and the exact 10 ml per 1010 ml dosing relationship are lost.
- Blocker: top-level duplicate merging sums incompatible concentrations from different solution scopes. NaCl combines the 50 g main-medium salt normalized to `49.505` g/L with the undiluted 1 g/L stock NaCl to produce `50.505` g/L, and `CaCl2 x 2 H2O` combines the 0.6 g main-medium salt normalized to `0.594059` g/L with the undiluted 0.1 g/L stock salt to produce `0.694059` g/L.
- Major: stock-only trace components are about 101-fold too concentrated if interpreted as final-medium concentrations. For example, nitrilotriacetic acid is recorded as `1.5` g/L and `MgSO4 x 7 H2O` as `3` g/L even though those are the 1 L stock concentrations for a 10 ml addition to a 1010 ml final medium.
- Major: the nitrilotriacetic acid and KOH preparation instructions belong to `Modified Wolin's mineral solution`, but the record scopes them as the main medium's `ADJUST_PH` preparation step.
- Major: `Trypticase` carries an unrelated small-molecule grounding to `CHEBI:78018` / dodecylphosphocholine.
- Minor: the separate KOMODO 905 record for the same DSMZ medium number should be compared with this MediaDive/DSMZ 905 record so the generated set does not publish avoidable duplicate recipe identities.

## Recommended Edits

- In `data/normalized_yaml/archaea/methanocalculus_halotolerans_medium.yaml`, replace the flattened Wolin solution rows with a structured `Modified Wolin's mineral solution` stock addition at 10 ml per 1010 ml final medium.
- Keep the DSMZ 905 main-medium salts at their final normalized concentrations and put NaCl 1 g/L and `CaCl2 x 2 H2O` 0.1 g/L under the Wolin stock, instead of summing those stock concentrations into the main recipe.
- Move nitrilotriacetic acid, sulfate, trace metal, selenite, and tungstate rows under the Wolin stock with their DSMZ/MediaDive solution 241 stock concentrations.
- Move the nitrilotriacetic-acid dissolution and pH adjustments into the Wolin stock preparation.
- Remove `CHEBI:78018` from `Trypticase` and either keep the curated `MediaIngredientMech:000263` grounding only or map it to a term that actually denotes trypticase/tryptone.
- Compare the KOMODO 905 sibling record and either merge it with this record or document why both generated records should remain distinct.

## Follow-up Checks

- Rerun open-schema, strict, reference, and term validation after nesting solution 241 so stock quantities remain machine-valid.
- Rebuild merged YAML and verify the generator no longer emits `Merged 2 duplicates` notes for NaCl or `CaCl2 x 2 H2O` in this record.
- Exact-search the regenerated merged output for `CHEBI:78018` scoped to this record and confirm no Trypticase row still points to dodecylphosphocholine.

## Additional Notes

None found.
