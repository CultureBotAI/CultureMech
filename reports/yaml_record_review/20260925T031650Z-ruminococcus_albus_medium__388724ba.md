# YAML Record Review: ruminococcus_albus_medium__388724ba

- Repository: CultureMech
- Record: `data/merge_yaml/merged/ruminococcus_albus_medium__388724ba.yaml`
- Started UTC: `2026-09-25T03:16:50Z`
- Finished UTC: `2026-09-25T03:16:50Z`
- Verdict: needs curation

## Target

Reviewed the generated merge record for `ruminococcus_albus_medium__388724ba`, a three-source merge of:

- `data/normalized_yaml/bacterial/KOMODO_436_RUMINOCOCCUS_ALBUS_medium.yaml`
- `data/normalized_yaml/bacterial/medium_436_modified_for_dsm_18848.yaml`
- `data/normalized_yaml/bacterial/ruminococcus_albus_medium.yaml`

The generated record is canonicalized to KOMODO Medium 436 and cites DSMZ Medium 436 as the ultimate source. It correctly merged the direct DSMZ/MediaDive 436 record with the KOMODO 436 mirror, but its formula still has mineral-stock flattening, a missing fatty-acid component, unrelated LB Medium rows, and an unresolved KOMODO `436_18848` child.

## Validation

- Open schema validation: Passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: Passed; `scripts/validate_strict.py` exited 0 and reported 0 total error rows.
- Reference validation: Passed; `linkml-reference-validator` ran 0 checks and reported all checks passed.
- Term validation: Passed; `linkml-term-validator` exited 0 after the expected `eutils` / `pkg_resources` warning.
- Embedded `curation_history`: Not checked. `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

DSMZ Medium 436 and KOMODO Medium 436 are true source duplicates of `RUMINOCOCCUS ALBUS MEDIUM`; local ignored-file-inclusive review data already records `data/normalized_yaml/bacterial/ruminococcus_albus_medium.yaml` with `data/normalized_yaml/bacterial/KOMODO_436_RUMINOCOCCUS_ALBUS_medium.yaml` as `SOURCE_DUPLICATE`.

The `medium_436_modified_for_dsm_18848` child is unresolved. It is a KOMODO `436_18848` source with a name that implies a strain-specific change for DSM 18848, but the normalized file has the same ingredient list as the base Medium 436 after `dsmz-resolver-v1.0` copied DSMZ Medium 436 over it. The DSMZ Medium 436 PDF does not mention DSM 18848, so this source needs direct KOMODO verification before it remains merged.

## Evidence

The DSMZ Medium 436 PDF lists Tryptone 5 g, Yeast extract 2 g, Glucose 3 g, Cellobiose 2 g, 40 ml Mineral solution 1, 40 ml Mineral solution 2, 1 mg Resazurin, and 920 ml distilled water. After boiling and cooling under CO2, it adds 4 g `Na2CO3`, 1 ml Fatty acid mixture, and 500 mg `Cysteine-HCl x H2O`, then adjusts pH to 7.0, distributes under N2, sterilizes, inoculates under CO2, and incubates at 37 C.

DSMZ defines Mineral solution 1 as `K2HPO4` 0.6%; Mineral solution 2 as `KH2PO4` 0.6%, `(NH4)2SO4` 2.0%, `NaCl` 1.2%, `MgSO4 x 7 H2O` 0.25%, and `CaCl2 x 7 H2O` 0.16%; and Fatty acid mixture as 10 ml isobutyric acid, 10 ml isovaleric acid, 10 ml 2-methylbutyric acid, and 70 ml distilled water.

## Completeness

The generated record preserves the base amounts for Tryptone, Yeast extract, Glucose, Cellobiose, Resazurin, `Na2CO3`, and cysteine, and it keeps DSMZ's pH 7.0.

It loses or corrupts these details:

- Mineral solution percentages are flattened at stock strength into the parent recipe.
- Fatty acid mixture loses 2-methylbutyric acid.
- The 920 ml parent water and 70 ml fatty-acid-mixture water are absent.
- The added LB Medium enrichment creates repeated Tryptone, Yeast extract, and NaCl rows.
- The `CaCl2 x 7 H2O` row is grounded to anhydrous calcium chloride.
- The `436_18848` child has no retained strain-specific modification.

## Findings

- `needs curation`: The two mineral stocks were flattened at stock strength. The parent uses 40 ml of each stock, but the generated record places `K2HPO4` 6 g/L, `KH2PO4` 6 g/L, `(NH4)2SO4` 20 g/L, `NaCl` 12 g/L, `MgSO4 x 7 H2O` 2.5 g/L, and `CaCl2 x 7 H2O` 1.6 g/L directly on the parent.
- `needs curation`: Fatty acid mixture is incomplete. DSMZ Medium 436 includes 2-methylbutyric acid alongside isobutyric and isovaleric acids, but the generated record has only two of those three acids and no 1 ml fatty-acid-mixture addition.
- `needs curation`: A spurious LB Medium commercial-product expansion added unrelated `Tryptone` `10.0 G_PER_L`, `Yeast extract` `5.0 G_PER_L`, `Sodium chloride` `10.0 G_PER_L`, and LB supplier notes.
- `needs curation`: The `medium_436_modified_for_dsm_18848` source should not be treated as a verified duplicate until its KOMODO 436_18848 source is checked; its name says it is modified, while its current local ingredient list is just a base-436 copy.
- `needs curation`: `CaCl2 x 7 H2O` is grounded to CHEBI:3312, anhydrous calcium chloride. That identifier is too broad for the hydrate-labeled row and should either use a hydrate-specific term if one exists or be left ungrounded.
- `pass with minor issues`: The DSMZ 436 / KOMODO 436 source identity, pH 7.0, main direct ingredient masses, resazurin conversion, cysteine conversion, and preparation steps are otherwise plausible.

## Recommended Edits

- Do not hand-edit `data/merge_yaml/merged/ruminococcus_albus_medium__388724ba.yaml`; fix the normalized DSMZ/MediaDive and KOMODO inputs, then rerun the merge.
- Preserve Mineral solution 1, Mineral solution 2, and Fatty acid mixture as nested stocks with 40 ml, 40 ml, and 1 ml parent aliquots.
- Restore 2-methylbutyric acid in the fatty-acid-mixture scope.
- Remove the LB Medium note, supplier catalog blocks, `Tryptone` 10 g/L, `Yeast extract` 5 g/L, and `Sodium chloride` 10 g/L rows unless a real DSMZ 436 source row supports them.
- Check KOMODO 436_18848 before keeping `medium_436_modified_for_dsm_18848` under Medium 436 as a duplicate or variant.
- Correct or remove the anhydrous calcium chloride grounding on `CaCl2 x 7 H2O`.

## Follow-up Checks

- Rerun open schema, strict, reference, and term validation on each edited normalized source file.
- Regenerate `data/merge_yaml/merged/ruminococcus_albus_medium__388724ba.yaml` and verify that the mineral-stock rows no longer appear at stock strength as direct parent ingredients.
- Verify that 2-methylbutyric acid is present in the fatty-acid-mixture scope.
- Verify that no regenerated Ruminococcus albus record contains the unsupported LB-only rows `Tryptone` 10 g/L, `Yeast extract` 5 g/L, or `Sodium chloride` 10 g/L.
- Run an exact ignored-file-inclusive search for `KOMODO_436_RUMINOCOCCUS_ALBUS_medium`, `medium_436_modified_for_dsm_18848`, and `ruminococcus_albus_medium` before changing duplicate links.

## Additional Notes

The absence of `target_organisms` was not treated as a defect for this generated record review. `CaCl2 x 7 H2O` appears exactly in the DSMZ Medium 436 PDF and should be checked chemically rather than "corrected" by assumption to a different hydrate.
