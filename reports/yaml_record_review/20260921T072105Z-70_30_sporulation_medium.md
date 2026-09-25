# YAML Record Review: 70_30_sporulation_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/70_30_sporulation_medium.yaml
- Started UTC: 2026-09-21T07:19:28Z
- Finished UTC: 2026-09-21T07:21:05Z
- Verdict: needs curation

## Target

- Reviewed generated record `data/merge_yaml/merged/70_30_sporulation_medium.yaml`.
- Stable identifier: `CultureMech:001277`.
- Source identity asserted by the record: DSMZ / MediaDive `1874`, `70:30 sporulation medium`.
- The generated record was merged from one owner, `70_30_sporulation_medium.yaml`, on fingerprint `f15e228388e94a9331203cf5325e44125bf32bda627ab256141ff18d026822a3`.
- Current authoritative owner: `data/normalized_yaml/bacterial/70_30_sporulation_medium.yaml`.

## Validation

- PASS: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/70_30_sporulation_medium.yaml`
- PASS: `scripts/validate_strict.py data/merge_yaml/merged/70_30_sporulation_medium.yaml`
- PASS: `linkml-reference-validator validate data data/merge_yaml/merged/70_30_sporulation_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe`
- PASS: `linkml-term-validator validate-data data/merge_yaml/merged/70_30_sporulation_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml`
- Not checked: embedded `MediaRecipe.curation_history` entries; the documented history validator targets standalone files under `history/`.

## Identity and Grounding

- The DSMZ / MediaDive identity is coherent: `mediadive.medium:1874`, original name `70:30 sporulation medium`, and the current MediaDive record all identify DSMZ medium 1874.
- A gitignore-independent exact search with a digit boundary for `mediadive.medium:1874` found only one active normalized owner and its generated merge.
- A gitignore-independent exact search for `10.1371/journal.pgen.1003660` found only this active owner and its generated merge.
- The DOI reference resolves to the PLoS Genetics article "Global Analysis of the Sporulation Pathway of Clostridium difficile", which is a plausible literature source for this sporulation medium.

## Evidence

- MediaDive / BacMedia lists the main solution as 63 g `Bacto peptone`, 3.5 g `Proteose peptone`, 0.7 g ammonium sulfate, 1.06 g Tris base, 11.1 g Brain Heart Infusion broth, 1.5 g yeast extract, and 15 g agar per litre.
- The same source lists a separate `L-Cysteine 10% w/v` solution containing 10 g L-cysteine and adds only 3 ml of that stock to the main solution.
- The source preparation says to autoclave the main solution at 121 degrees C for 15 minutes, add the cysteine stock after cooling to about 65 degrees C, store plates at 4 degrees C for up to 1 week, and filter the cysteine stock through a 0.22 um filter.

## Completeness

- The generated target preserves the four direct salts/buffers/carbon-free solids, yeast extract, and agar from the main solution.
- The generated target decomposes the 11.1 g/L Brain Heart Infusion broth source row into supplier constituents, but those constituent masses are not scaled to an 11.1 g/L amount of the commercial product.
- The generated target does not preserve Brain Heart Infusion broth itself as an ingredient and does not model `L-Cysteine 10% w/v` as a stock solution.

## Findings

- BLOCKER: Brain Heart Infusion broth is represented with unscaled supplier-formulation rows. The source adds 11.1 g/L of the commercial broth, but the generated record emits full dehydrated-medium constituent amounts such as proteose peptone 10.0 g/L, dextrose 2.0 g/L, sodium chloride 5.0 g/L, and disodium phosphate 2.5 g/L.
- BLOCKER: the L-cysteine concentration is flattened from the stock solution instead of the final medium. `3 ml` of a `10% w/v` stock contributes about 0.3 g/L L-cysteine to a 1 L recipe, not 100 g/L.
- MINOR: the stock-solution filter-sterilization step is emitted after plate storage, so the target loses the nesting and ordering that connect 0.22 um filtration to the cysteine stock before addition.
- MINOR: the BHI `supplier_catalog.product_url` values point to a third-party Microbe Notes page rather than a Difco/BD product-specification URL for catalog `237500`.

## Recommended Edits

- In `data/normalized_yaml/bacterial/70_30_sporulation_medium.yaml`, restore a source-faithful 11.1 g/L `Brain Heart Infusion broth` row or scale any optional BHI constituent rows to the 11.1 g/L amount actually used in DSMZ medium 1874.
- Represent `L-Cysteine 10% w/v` as a separate 100 g/L stock solution and represent the final addition as 3 ml/L, or otherwise store the final L-cysteine amount as approximately 0.3 g/L.
- Keep the cysteine 0.22 um filtration instruction attached to the stock solution, before the 3 ml addition to cooled medium.
- Replace the Microbe Notes supplier URL with authoritative Difco/BD catalog provenance, or move the third-party page out of `supplier_catalog` into secondary notes.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after the BHI and cysteine concentration fixes.
- Re-run an exact `mediadive.medium:1874` source search with a digit boundary; the DSMZ medium 1874 identity should still resolve to this single generated record.
- Recompute the merge fingerprint and confirm that the page generated for DSMZ Medium 1874 no longer reports L-cysteine at 100 g/L final concentration.

## Additional Notes

- The current record is structurally valid YAML, but two stock/commercial-product flattening choices produce concentrations that do not match the MediaDive source recipe.
