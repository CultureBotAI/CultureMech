# YAML Record Review: ruminococcus_albus_medium__11635e7b

- Repository: CultureMech
- Record: `data/merge_yaml/merged/ruminococcus_albus_medium__11635e7b.yaml`
- Started UTC: `2026-09-25T03:13:38Z`
- Finished UTC: `2026-09-25T03:13:38Z`
- Verdict: needs curation

## Target

Reviewed the generated merge record for `ruminococcus_albus_medium__11635e7b`, a single-source merge of `data/normalized_yaml/bacterial/TOGO_M694_Ruminococcus_Albus_Medium.yaml`.

The target represents TOGO M694, `Ruminococcus Albus Medium`, imported from JCM M675. The generated YAML keeps the source identity, but it flattens three nested stock solutions, promotes milligram quantities to grams per liter, drops a fatty-acid component, and carries an unrelated LB Medium commercial-product enrichment.

## Validation

- Open schema validation: Passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: Passed; `scripts/validate_strict.py` exited 0 and reported 0 total error rows.
- Reference validation: Passed; `linkml-reference-validator` ran 0 checks and reported all checks passed.
- Term validation: Passed; `linkml-term-validator` exited 0 after the expected `eutils` / `pkg_resources` warning.
- Embedded `curation_history`: Not checked. `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

TOGO M694 is the right upstream identity for this generated record: the live payload identifies `http://togomedium.org/medium/M694`, name `Ruminococcus Albus Medium`, `original_media_id` `JCM_M675`, source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=675`, and pH `7.0`.

An ignored-file-inclusive filename search found several sibling Ruminococcus albus records, including `data/normalized_yaml/bacterial/JCM_J675_RUMINOCOCCUS_ALBUS_MEDIUM.yaml`, `data/normalized_yaml/bacterial/KOMODO_436_RUMINOCOCCUS_ALBUS_medium.yaml`, `data/normalized_yaml/bacterial/ruminococcus_albus_medium.yaml`, and generated records `data/merge_yaml/merged/RUMINOCOCCUS_ALBUS_MEDIUM.yaml` and `data/merge_yaml/merged/ruminococcus_albus_medium__388724ba.yaml`. Those should be reconciled only after their formulas are compared against the JCM M675 and related source recipes.

## Evidence

The TOGO M694 main solution lists 920 ml distilled water, 1 mg Resazurin, 4 g `Na2CO3`, 2 g cellobiose, 3 g glucose, 2 g `Yeast extract (BD-Difco)`, 5 g `Tryptone (BD-Difco)`, 500 mg `L--cysteine x HCl x H2O`, 40 ml `Mineral solution 1`, 40 ml `Mineral solution 2`, 1 ml `fatty acid mixture`, and CO2 / N2 gas entries.

The same payload defines `Mineral solution 1` as 100 ml water plus 0.6 g `K2HPO4`, defines `Mineral solution 2` as 100 ml water plus 0.25 g `MgSO4 x 7 H2O`, 1.2 g `NaCl`, 0.16 g `CaCl2 x 2 H2O`, 0.6 g `KH2PO4`, and 2 g `(NH4)2SO4`, and defines `Fatty acid mixture` as 70 ml water with 10 ml each of isovaleric acid, isobutyric acid, and 2-methylbutyric acid.

TOGO also preserves preparation comments: boil and cool under CO2, then under CO2 add `Na2CO3`, fatty acid mixture, and L-cysteine; adjust pH to 7.0; distribute under N2; and autoclave.

## Completeness

The generated record retains most parent-medium gram quantities, but it loses or corrupts these source details:

- `Mineral solution 1` and `Mineral solution 2` survive only as empty solution placeholders with `40 G_PER_L`.
- The 1 ml fatty-acid mixture is not preserved as a solution, and 2-methylbutyric acid is absent.
- Main-solution, Mineral solution 1, Mineral solution 2, and fatty-acid-mixture water rows are merged into `Distilled water` `1190.0 G_PER_L`.
- Resazurin 1 mg and cysteine 500 mg are represented as `1 G_PER_L` and `500 G_PER_L`.
- Stock-strength mineral and fatty-acid rows are flattened directly into the parent.
- CO2 and N2 preparation gases are represented as variable-concentration ingredients.
- The pH and preparation comments are absent.
- Unrelated LB Medium rows and notes were appended.

## Findings

- `needs curation`: Two milligram source amounts have 1000x unit slips. TOGO lists 1 mg Resazurin and 500 mg `L--cysteine x HCl x H2O`, but the generated record has `1 G_PER_L` and `500 G_PER_L`.
- `needs curation`: Mineral solution 1, Mineral solution 2, and fatty acid mixture are flattened into the parent without their 40 ml, 40 ml, and 1 ml addition volumes. Their stock water was merged into parent water and their stock-strength minerals and acids became direct ingredients.
- `needs curation`: The fatty acid mixture lost 2-methylbutyric acid even though TOGO M694 lists it alongside isovaleric and isobutyric acids.
- `needs curation`: A spurious LB Medium commercial-product expansion added unrelated `Tryptone` `10.0 G_PER_L`, `Yeast extract` `5.0 G_PER_L`, `Sodium chloride` `10.0 G_PER_L`, and LB supplier notes to this Ruminococcus medium.
- `needs curation`: The generated record dropped pH 7.0 and preparation comments for CO2 boiling/cooling, CO2 addition of carbonate, fatty acids, and cysteine, N2 dispensing, and autoclaving, while turning CO2 and N2 into standalone ingredients.
- `pass with minor issues`: The high-level source identity and the main gram-denominated rows for carbonate, cellobiose, glucose, Difco yeast extract, and Difco tryptone are plausible relative to TOGO M694.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/TOGO_M694_Ruminococcus_Albus_Medium.yaml`, or the TOGO import/enrichment logic that creates it, rather than hand-editing `data/merge_yaml/merged/ruminococcus_albus_medium__11635e7b.yaml`.
- Convert Resazurin and cysteine from milligram source masses to gram-scale final quantities.
- Preserve Mineral solution 1, Mineral solution 2, and fatty acid mixture as nested stocks with 40 ml, 40 ml, and 1 ml parent aliquots.
- Restore the 2-methylbutyric acid member of the fatty-acid mixture.
- Remove the LB Medium note, supplier catalog blocks, `Tryptone` 10 g/L, `Yeast extract` 5 g/L, and `Sodium chloride` 10 g/L rows unless a real JCM M675 source row supports them.
- Carry TOGO's pH and preparation comments into structured preparation metadata and model CO2/N2 as preparation atmospheres rather than ingredients.
- After TOGO M694 is corrected, rerun the merge and compare it with the JCM/MediaDive and KOMODO Ruminococcus albus siblings for true duplicate or variant relationships.

## Follow-up Checks

- Rerun open schema, strict, reference, and term validation on `data/normalized_yaml/bacterial/TOGO_M694_Ruminococcus_Albus_Medium.yaml`.
- Regenerate `data/merge_yaml/merged/ruminococcus_albus_medium__11635e7b.yaml` and verify that `Resazurin` is no longer `1 G_PER_L` and cysteine is no longer `500 G_PER_L`.
- Verify that the regenerated record has no empty `solutions` entries for the two mineral solutions.
- Verify that 2-methylbutyric acid is present in the fatty-acid-mixture scope.
- Run an exact ignored-file-inclusive search for `TOGO_M694_Ruminococcus_Albus_Medium`, `JCM_J675_RUMINOCOCCUS_ALBUS_MEDIUM`, `KOMODO_436_RUMINOCOCCUS_ALBUS_medium`, and `ruminococcus_albus_medium` before deduplicating normalized sources.

## Additional Notes

The absence of `target_organisms` was not treated as a defect for this generated record review.
