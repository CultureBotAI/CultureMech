# YAML Record Review: rumen_bacteria_medium__b6ddc39f

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rumen_bacteria_medium__b6ddc39f.yaml`
- Started UTC: `2026-09-25T03:04:40Z`
- Finished UTC: `2026-09-25T03:04:57Z`
- Verdict: needs curation

## Target

Reviewed the generated merge record for `rumen_bacteria_medium__b6ddc39f`, a five-source merge of:

- `data/normalized_yaml/bacterial/KOMODO_330_RUMEN_BACTERIA_medium.yaml`
- `data/normalized_yaml/bacterial/KOMODO_704_BUTYRIVIBRIO_SP._medium.yaml`
- `data/normalized_yaml/bacterial/butyrivibrio_sp_medium.yaml`
- `data/normalized_yaml/bacterial/medium_330_modified_for_dsm_17630.yaml`
- `data/normalized_yaml/bacterial/rumen_bacteria_medium.yaml`

The generated record keeps the KOMODO Medium 330 identity, `RUMEN BACTERIA medium`, but it also absorbs DSMZ / MediaDive Medium 704, KOMODO Medium 704, and the KOMODO `330_17630` strain-specific medium.

## Validation

- Open schema validation: Passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: Passed; `scripts/validate_strict.py` exited 0 and reported 0 total error rows.
- Reference validation: Passed; `linkml-reference-validator` ran 0 checks and reported all checks passed.
- Term validation: Passed; `linkml-term-validator` exited 0 after the expected `eutils` / `pkg_resources` warning.
- Embedded `curation_history`: Not checked. `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The target's canonical identity, KOMODO Medium 330 / DSMZ Medium 330 `RUMEN BACTERIA MEDIUM`, is only one member of the merge. DSMZ Medium 330 and KOMODO Medium 330 are source duplicates of the same base medium. DSMZ Medium 704 and KOMODO Medium 704 are likewise source duplicates of each other, but Medium 704 is `BUTYRIVIBRIO SP. MEDIUM`, not a duplicate of Medium 330.

DSMZ Medium 330 also has a documented strain-specific modification for DSM 17630 and related strains: supplement the medium after autoclaving with sterile, anoxic rumen fluid at 30 ml/L. The KOMODO `330_17630` normalized file carries the same ingredient rows as the base Medium 330 because that rumen-fluid modification was dropped, so the `SOURCE_DUPLICATE` link to base 330 is only an artifact of an incomplete import.

The exact ignored-file-inclusive local proposal check found prior local evidence for the same split: `data/normalized_yaml/bacterial/rumen_bacteria_medium.yaml` with `KOMODO_330_RUMEN_BACTERIA_medium.yaml` was reviewed as `SOURCE_DUPLICATE`, `data/normalized_yaml/bacterial/butyrivibrio_sp_medium.yaml` with `KOMODO_704_BUTYRIVIBRIO_SP._medium.yaml` was reviewed as `SOURCE_DUPLICATE`, and the 330/704 cross-pair was proposed as a `CONCENTRATION_VARIANT`, not a source duplicate.

## Evidence

The DSMZ Medium 330 PDF and the live MediaDive 330 REST payload agree that the base medium adds 38 ml Mineral solution, 3.1 ml Volatile fatty acid mixture, 2 ml 0.05% w/v Haemin solution, 960 ml distilled water, and 0.5 g each of D-glucose, maltose, cellobiose, and soluble starch to a 1003 ml final volume.

The DSMZ Medium 704 PDF and the live MediaDive 704 REST payload agree that `BUTYRIVIBRIO SP. MEDIUM` is different: it adds 75 ml Mineral solution, 150 ml Clarified rumen fluid, 3.1 ml Volatile fatty acid mixture, 2 ml 0.05% w/v Haemin solution, 770 ml distilled water, 2 g yeast extract, and 1 g each of D-glucose, maltose, cellobiose, and soluble starch to a 1001 ml final volume.

Both DSMZ records define Mineral solution as a 1 L stock of `KH2PO4`, `NaCl`, `(NH4)2SO4`, `CaCl2 x 2 H2O`, and `MgSO4 x 7 H2O`; both define Volatile fatty acid mixture as a stock of acetic, propionic, butyric, n-valeric, iso-butyric, DL-2-methylbutyric, and iso-valeric acids; and both define Haemin solution as 50 mg haemin plus 1 ml 1 N NaOH made up to 100 ml and filter sterilized.

## Completeness

The generated record is missing several source-level distinctions:

- The five normalized inputs are collapsed into one parent instead of preserving Medium 330, Medium 330 modified for DSM 17630, and Medium 704 as distinct base/variant records.
- The Medium 704 `Clarified rumen fluid` 150 ml addition is completely absent.
- The DSM 17630 sterile anoxic rumen-fluid supplement, 30 ml/L after autoclaving, is absent.
- The DSMZ / MediaDive preparation steps are absent from the generated target because the KOMODO 330 source, which had no `preparation_steps`, became canonical.
- Mineral solution, Volatile fatty acid mixture, and Haemin solution are flattened into the parent at stock strength rather than represented as nested stock solutions with parent aliquot volumes.

## Findings

- `needs curation`: The merge is a false source-duplicate collapse across distinct DSMZ media. Medium 330 and Medium 704 differ by name, main-solution volume, 75 ml versus 38 ml Mineral solution, 150 ml Clarified rumen fluid, 770 ml versus 960 ml water, 2 g versus 0.5 g yeast extract, and doubled carbohydrate masses. The generated record hides Medium 704 under synonyms and keeps only the 330 concentrations.
- `needs curation`: The KOMODO `330_17630` child is not a true duplicate of Medium 330. DSMZ Medium 330 explicitly says DSM 17630 should receive a post-autoclave sterile anoxic rumen-fluid supplement at 30 ml/L, but that variant ingredient was dropped before the local `SOURCE_DUPLICATE` assignment.
- `needs curation`: Shared stock solutions are flattened at stock strength. Parent rows such as `NaCl` `12 G_PER_L`, `KH2PO4` `6 G_PER_L`, `Acetic acid` `573.182 G_PER_L`, `Propionic acid` `192.145 G_PER_L`, `Haemin` `0.5 G_PER_L`, and `NaOH` `1 G_PER_L` are recipes for Mineral, VFA, or Haemin stocks, not final parent-medium concentrations.
- `needs curation`: A spurious LB Medium commercial-product expansion added unrelated `Tryptone` `10.0 G_PER_L`, `Yeast extract` `5.0 G_PER_L`, and `Sodium chloride` `10.0 G_PER_L` rows, plus an LB supplier note and a laboratorynotes.com citation, to every normalized member of this merge. Those rows are not in DSMZ Media 330 or 704 and create repeated parent ingredients such as `Yeast extract` at both source-medium and LB concentrations.
- `needs curation`: The generated target lost available preparation details. The MediaDive 330 and 704 sources include anoxic CO2 sparging, carbonate equilibration to pH 6.8, Hungate or serum-vial dispensing, delayed sterile stock additions, and Haemin solution filter sterilization; the generated KOMODO-canonical record has no `preparation_steps`.
- `pass with minor issues`: The main 330 identity and several simple main-solution concentrations are plausible: `K2HPO4` 0.3 g/L, `Trypticase peptone` 2 g/L, `Yeast extract` 0.5 g/L, glycerol 0.5 g/L, carbohydrates 0.5 g/L, cysteine 0.25 g/L, and sodium sulfide 0.25 g/L match DSMZ Medium 330.

## Recommended Edits

- Do not hand-edit `data/merge_yaml/merged/rumen_bacteria_medium__b6ddc39f.yaml`; fix the normalized DSMZ/MediaDive and KOMODO inputs, then rerun the merge.
- Split the 330 and 704 source-duplicate pairs: keep DSMZ/MediaDive Medium 330 with KOMODO 330, keep DSMZ/MediaDive Medium 704 with KOMODO 704, and remove `SOURCE_DUPLICATE` linkage across those pairs.
- Rebuild `medium_330_modified_for_dsm_17630` as a Medium 330 variant that adds 30 ml/L sterile anoxic rumen fluid after autoclaving.
- Remove the unrelated LB Medium note, supplier catalog blocks, `Tryptone`, `Yeast extract` 5 g/L, and `Sodium chloride` 10 g/L rows from all five normalized inputs unless a real DSMZ 330/704 source row supports them.
- Preserve Mineral solution, Volatile fatty acid mixture, Haemin solution, and Clarified rumen fluid as nested solution or variant structures with their actual parent addition volumes.
- Prefer the MediaDive/DSMZ records over KOMODO-only records as canonical when they carry richer source steps and solution structure for the same DSMZ medium.

## Follow-up Checks

- Rerun open schema, strict, reference, and term validation on each edited normalized source file.
- Regenerate merged YAML and verify that Medium 330, Medium 704, and `medium_330_modified_for_dsm_17630` no longer collapse to one `merge_fingerprint`.
- Verify that no regenerated Rumen Bacteria or Butyrivibrio record contains the unsupported LB-only rows `Tryptone` 10 g/L, `Yeast extract` 5 g/L, or `Sodium chloride` 10 g/L.
- Verify that Mineral and VFA stock components are no longer present as stock-strength parent ingredients.
- Run an exact ignored-file-inclusive search for `KOMODO_330_RUMEN_BACTERIA_medium`, `KOMODO_704_BUTYRIVIBRIO_SP._medium`, `butyrivibrio_sp_medium`, and `medium_330_modified_for_dsm_17630` before deleting or changing the variant links.

## Additional Notes

The generated YAML uses schema-valid structures, so the blocker is a source-identity and transformation problem. Empty `target_organisms` were not treated as defects for this generated record review.
