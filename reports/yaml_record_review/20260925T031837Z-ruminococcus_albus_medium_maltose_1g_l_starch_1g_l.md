# YAML Record Review: ruminococcus_albus_medium_maltose_1g_l_starch_1g_l

- Repository: CultureMech
- Record: `data/merge_yaml/merged/ruminococcus_albus_medium_maltose_1g_l_starch_1g_l.yaml`
- Started UTC: `2026-09-25T03:18:37Z`
- Finished UTC: `2026-09-25T03:18:37Z`
- Verdict: needs curation

## Target

Reviewed the generated merge record for `ruminococcus_albus_medium_maltose_1g_l_starch_1g_l`, a single-source merge of `data/normalized_yaml/bacterial/ruminococcus_albus_medium_maltose_1g_l_starch_1g_l.yaml`.

The record represents TOGO Medium `M2636`, `Ruminococcus Albus Medium + maltose (1g/L), starch (1g/L)`, with DSMZ Medium 436 cited as the original URL. The source is the DSMZ 436 formula with 1 g starch and 1 g maltose added in the post-boil CO2 step.

## Validation

- Open schema validation: Passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation: Passed; `scripts/validate_strict.py` exited 0 and reported 0 total error rows.
- Reference validation: Passed; `linkml-reference-validator` ran 0 checks and reported all checks passed.
- Term validation: Passed; `linkml-term-validator` exited 0 after the expected `eutils` / `pkg_resources` warning.
- Embedded `curation_history`: Not checked. `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

The generated identity is correctly grounded to TOGO `M2636` and should remain distinct from the plain `RUMINOCOCCUS ALBUS MEDIUM` records because `M2636` adds 1 g starch and 1 g maltose. No false multi-source merge was found for this generated YAML.

## Evidence

TOGO `M2636` lists, in the main base recipe, 920 ml distilled water, 2 g Yeast extract, 1 mg Resazurin, 2 g Cellobiose, 3 g Glucose, 5 g Tryptone, 40 ml Mineral solution 1, 40 ml Mineral solution 2, and CO2. Its second main paragraph adds 4 g `Na2CO3`, 1 g Starch, 1 g Maltose, 500 mg `Cysteine-HCl x H2O`, 1 ml Fatty acid mixture, and N2.

The same TOGO payload defines Mineral solution 1 as 100 ml distilled water plus `K2HPO4` 0.6%; Mineral solution 2 as 100 ml distilled water plus `MgSO4 x 7 H2O` 0.25%, `NaCl` 1.2%, `KH2PO4` 0.6%, `(NH4)2SO4` 2%, and `CaCl2 x 7 H2O` 0.16%; and Fatty acid mixture as 70 ml distilled water plus 10 ml each of isovaleric acid, isobutyric acid, and 2-methylbutyric acid.

TOGO also carries pH 7.0 and the DSMZ instructions to boil and cool under CO2, add the second main paragraph under a gentle CO2 stream, adjust pH to 7.0, distribute under N2, sterilize, inoculate under CO2, and incubate at 37 C.

## Completeness

The generated record preserves the 2 g Yeast extract, 2 g Cellobiose, 3 g Glucose, 5 g Tryptone, 4 g `Na2CO3`, 1 g Starch, and 1 g Maltose rows from TOGO `M2636`.

It loses or corrupts these source details:

- The 1 mg Resazurin row is imported as `1 G_PER_L`.
- The 500 mg `Cysteine-HCl x H2O` row is imported as `500 G_PER_L`.
- Both 40 ml mineral-stock aliquots and the 1 ml fatty-acid aliquot are imported as gram-per-liter rows.
- The two mineral stocks are also flattened into direct parent ingredients at stock percent concentrations.
- The 70 ml fatty-acid-mixture water, both 100 ml mineral-stock water rows, and the 920 ml parent water are collapsed into `1190.0 G_PER_L`.
- The fatty-acid mixture drops 2-methylbutyric acid.
- pH 7.0 and the anaerobic preparation sequence are absent from structured fields.
- Unrelated LB Medium supplier metadata adds extra Tryptone, Yeast extract, and Sodium chloride rows.

## Findings

- `needs curation`: Two mass-unit conversions are off by 1000-fold. TOGO lists Resazurin as 1 mg and `Cysteine-HCl x H2O` as 500 mg, but the generated record reports `1 G_PER_L` and `500 G_PER_L`.
- `needs curation`: Parent aliquot volumes are represented as masses. The generated `solutions` array has 40 ml Mineral solution 1 and 40 ml Mineral solution 2 as `40 G_PER_L`, and the 1 ml Fatty acid mixture aliquot is represented as a direct `1 G_PER_L` ingredient.
- `needs curation`: The two mineral stocks are flattened at stock strength into the parent formula, so `K2HPO4`, `KH2PO4`, `(NH4)2SO4`, `NaCl`, `MgSO4 x 7 H2O`, and `CaCl2 x 7 H2O` are recorded as direct parent ingredients at their stock percentages.
- `needs curation`: Fatty acid mixture is incomplete. TOGO `M2636` includes 2-methylbutyric acid along with isobutyric and isovaleric acids, but the generated record has no 2-methylbutyric acid.
- `needs curation`: The water row merges 920 ml parent water, 100 ml from each mineral stock, and 70 ml from the fatty-acid stock into one `1190.0 G_PER_L` row, losing stock scope and changing volume into mass concentration.
- `needs curation`: A spurious LB Medium commercial-product expansion added unrelated `Tryptone` `10.0 G_PER_L`, `Yeast extract` `5.0 G_PER_L`, `Sodium chloride` `10.0 G_PER_L`, LB supplier catalogs, and an external LB preparation URL.
- `needs curation`: The record keeps neither the pH 7.0 target nor the DSMZ anaerobic sequence as structured preparation metadata.
- `needs curation`: `CaCl2 x 7 H2O` is grounded to CHEBI:3312, anhydrous calcium chloride. That identifier is too broad for the hydrate-labeled row and should either use a hydrate-specific term if one exists or be left ungrounded.
- `pass with minor issues`: The TOGO `M2636` identity, base DSMZ 436 formula relationship, direct 1 g starch and 1 g maltose additions, and direct gram amounts other than the mg-scale rows are otherwise plausible.

## Recommended Edits

- Do not hand-edit `data/merge_yaml/merged/ruminococcus_albus_medium_maltose_1g_l_starch_1g_l.yaml`; fix the TOGO `M2636` normalized source, then rerun the merge.
- Preserve Mineral solution 1, Mineral solution 2, and Fatty acid mixture as nested stocks with 40 ml, 40 ml, and 1 ml parent aliquots.
- Convert Resazurin 1 mg and `Cysteine-HCl x H2O` 500 mg without promoting those mg values to g/L.
- Keep the 920 ml parent water, the two 100 ml mineral-solution water rows, and the 70 ml fatty-acid-mixture water row in their source scopes.
- Restore 2-methylbutyric acid in the fatty-acid-mixture scope.
- Capture pH 7.0 and the anaerobic boil, CO2, N2, sterilization, inoculation, and 37 C incubation instructions where the schema permits.
- Remove the LB Medium note, supplier catalog blocks, `Tryptone` 10 g/L, `Yeast extract` 5 g/L, and `Sodium chloride` 10 g/L rows unless a real TOGO `M2636` source row supports them.
- Correct or remove the anhydrous calcium chloride grounding on `CaCl2 x 7 H2O`.

## Follow-up Checks

- Rerun open schema, strict, reference, and term validation on `data/normalized_yaml/bacterial/ruminococcus_albus_medium_maltose_1g_l_starch_1g_l.yaml`.
- Regenerate `data/merge_yaml/merged/ruminococcus_albus_medium_maltose_1g_l_starch_1g_l.yaml` and verify that the mineral-stock rows no longer appear as direct parent ingredients.
- Verify that 2-methylbutyric acid is present in the fatty-acid-mixture scope.
- Verify that the regenerated record has no `Resazurin` `1 G_PER_L`, no `Cysteine-HCl x H2O` `500 G_PER_L`, and no stock or fatty-acid aliquot represented as gram-per-liter mass.
- Run an exact ignored-file-inclusive search for `TOGO:M2636` and `ruminococcus_albus_medium_maltose_1g_l_starch_1g_l` before changing duplicate links.

## Additional Notes

The absence of `target_organisms` was not treated as a defect for this generated record review. The 1 g starch and 1 g maltose additions are present in TOGO `M2636` and should not be removed just because the cited DSMZ Medium 436 PDF is the plainer base medium.
