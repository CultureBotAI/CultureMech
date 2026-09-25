# YAML Record Review: ruminoclostridium_cellulolyticum_cm3_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/ruminoclostridium_cellulolyticum_cm3_medium.yaml`
- Started UTC: `2026-09-25T03:11:04Z`
- Finished UTC: `2026-09-25T03:11:04Z`
- Verdict: needs curation

## Target

Reviewed the generated merge record for `ruminoclostridium_cellulolyticum_cm3_medium`, a five-source merge of:

- `data/normalized_yaml/bacterial/KOMODO_520_CM3_medium.yaml`
- `data/normalized_yaml/bacterial/for_dsm_5974_and_dsm_17427.yaml`
- `data/normalized_yaml/bacterial/medium_520_modified_for_dsm_7093.yaml`
- `data/normalized_yaml/bacterial/medium_520_modified_for_dsm_9801.yaml`
- `data/normalized_yaml/bacterial/ruminoclostridium_cellulolyticum_cm3_medium.yaml`

The target is canonicalized to the DSMZ/MediaDive Medium 520 import for `RUMINOCLOSTRIDIUM CELLULOLYTICUM (CM3) MEDIUM`. It retains DSMZ preparation text, but it flattens the SL-10 trace-element stock into the parent and collapses multiple KOMODO strain-specific records as `SOURCE_DUPLICATE`s.

## Validation

- Open schema validation: Passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: Passed; `scripts/validate_strict.py` exited 0 and reported 0 total error rows.
- Reference validation: Passed; `linkml-reference-validator` ran 0 checks and reported all checks passed.
- Term validation: Passed; `linkml-term-validator` exited 0 after the expected `eutils` / `pkg_resources` warning.
- Embedded `curation_history`: Not checked. `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The canonical MediaDive identity is correct for the base recipe: DSMZ Medium 520 is `RUMINOCLOSTRIDIUM CELLULOLYTICUM (CM3) MEDIUM` with pH 7.2.

The merge is not fully identity-safe. KOMODO 520 is a duplicate of DSMZ Medium 520, but `For DSM 5974 and DSM 17427` and `MEDIUM 520 MODIFIED FOR DSM 9801` are strain-specific variants in DSMZ Medium 520's own PDF. That PDF says DSM 5974, DSM 9801, and DSM 17427 should use 5 g/L D-glucose as the substrate, receive 0.5 g/L additional `Na2S x 9 H2O` after autoclaving, and be adjusted to pH 6.8 - 7.0 if necessary.

`MEDIUM 520 MODIFIED FOR DSM 7093` also advertises itself as a KOMODO strain modification with pH 7.5, but the DSMZ Medium 520 PDF does not name DSM 7093. Treat that source as unresolved until the KOMODO source record is checked directly.

## Evidence

The live MediaDive 520 REST endpoint and the DSMZ Medium 520 PDF agree on the base main solution: final volume 1003 ml, 1.3 g `(NH4)2SO4`, 1.5 g `KH2PO4`, 2.9 g `K2HPO4 x 3 H2O`, 1.25 ml `FeSO4 x 7 H2O` solution, 1 ml `Trace element solution SL-10`, 2 g yeast extract, 0.5 ml 0.1% Sodium resazurin, 0.2 g `MgCl2 x 6 H2O`, 75 mg `CaCl2 x 2 H2O`, 6 g cellobiose, optional 10 g cellulose powder, 1.5 g `Na2CO3`, 0.5 g `L-Cysteine HCl x H2O`, and 1000 ml distilled water.

The same DSMZ source defines SL-10 as a separate 1 L stock with 10 ml 25% HCl, 1.5 g `FeCl2 x 4 H2O`, 70 mg `ZnCl2`, 100 mg `MnCl2 x 4 H2O`, 6 mg `H3BO3`, 190 mg `CoCl2 x 6 H2O`, 2 mg `CuCl2 x 2 H2O`, 24 mg `NiCl2 x 6 H2O`, 36 mg `Na2MoO4 x 2 H2O`, and 990 ml distilled water. The parent medium uses only 1 ml of that stock.

## Completeness

The generated record preserves the base DSMZ 520 solute concentrations and preparation steps well for direct main-solution masses and MediaDive-computed solution aliquots such as the acidified `FeSO4 x 7 H2O` and 0.1% resazurin additions.

It misses several source structures:

- SL-10 is flattened into parent ingredients at stock strength even though DSMZ Medium 520 uses only 1 ml of it per 1003 ml final medium.
- Both the 1000 ml main-solution water and 990 ml SL-10 stock water are absent.
- `Cellulose` is marked only in a note as optional, but remains a normal ingredient row in the base generated recipe.
- DSM 5974, DSM 9801, and DSM 17427 glucose/Na2S/pH variants are represented only as duplicate-source synonyms.

## Findings

- `needs curation`: The merge is a false source-duplicate collapse across strain-specific variants. DSMZ Medium 520 explicitly changes the substrate to 5 g/L D-glucose, adds a post-autoclave 0.5 g/L `Na2S x 9 H2O` supplement, and changes final pH handling to 6.8 - 7.0 for DSM 5974, DSM 9801, and DSM 17427; the generated record drops those modifications and keeps only base CM3 ingredients.
- `needs curation`: The 1 ml SL-10 trace-element addition was flattened at stock strength. Rows from `HCl` through `Na2MoO4 x 2 H2O` are the 1 L SL-10 recipe, not final parent-medium concentrations.
- `needs curation`: The `medium_520_modified_for_dsm_7093` merge is unresolved. It is named and keyed as a KOMODO-specific modified medium with pH 7.5, but the generated output gives it no distinct modification and DSMZ Medium 520 does not document DSM 7093.
- `needs curation`: Base and stock water are missing. MediaDive and the DSMZ PDF keep 1000 ml distilled water in the base main solution and 990 ml distilled water in SL-10.
- `pass with minor issues`: The base DSMZ 520 identity, pH 7.2, direct main-solute concentrations, acidified FeSO4 aliquot, resazurin aliquot, anaerobic preparation step, and SL-10 preparation text all match the MediaDive source for the canonical parent.

## Recommended Edits

- Do not hand-edit `data/merge_yaml/merged/ruminoclostridium_cellulolyticum_cm3_medium.yaml`; fix the normalized DSMZ/MediaDive and KOMODO inputs, then rerun the merge.
- Keep DSMZ Medium 520 and KOMODO Medium 520 as source duplicates of the base CM3 medium.
- Remodel `for_dsm_5974_and_dsm_17427` and `medium_520_modified_for_dsm_9801` as variants that replace the substrate with 5 g/L D-glucose, add 0.5 g/L `Na2S x 9 H2O` after autoclaving, and set pH 6.8 - 7.0.
- Check the KOMODO 520_7093 source before retaining, merging, or deleting `medium_520_modified_for_dsm_7093`; it should not remain a blind `SOURCE_DUPLICATE`.
- Preserve `Trace element solution SL-10` as a nested 1 L stock with a 1 ml parent addition instead of flattening its composition into parent ingredients.
- Preserve or explicitly suppress distilled-water rows consistently across the main solution and SL-10.

## Follow-up Checks

- Rerun open schema, strict, reference, and term validation on each edited normalized source file.
- Regenerate the CM3 merged YAML and verify that `HCl`, `FeCl2 x 4 H2O`, `ZnCl2`, `MnCl2 x 4 H2O`, `H3BO3`, `CoCl2 x 6 H2O`, `CuCl2 x 2 H2O`, `NiCl2 x 6 H2O`, and `Na2MoO4 x 2 H2O` are no longer direct stock-strength parent ingredients.
- Verify that the DSM 5974, DSM 17427, and DSM 9801 records no longer collapse into the base `merge_fingerprint`.
- Run an exact ignored-file-inclusive search for `KOMODO_520_CM3_medium`, `for_dsm_5974_and_dsm_17427`, `medium_520_modified_for_dsm_7093`, `medium_520_modified_for_dsm_9801`, and `ruminoclostridium_cellulolyticum_cm3_medium` before changing duplicate links.

## Additional Notes

Empty `target_organisms` were not treated as defects for this generated record review. The optional cellulose row should be revisited after variant modeling is available, because it is a substrate adaptation note rather than a universal base ingredient.
