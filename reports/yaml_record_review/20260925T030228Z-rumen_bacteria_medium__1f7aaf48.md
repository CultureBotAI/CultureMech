# YAML Record Review: rumen_bacteria_medium__1f7aaf48

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rumen_bacteria_medium__1f7aaf48.yaml`
- Started UTC: `2026-09-25T03:02:28Z`
- Finished UTC: `2026-09-25T03:02:49Z`
- Verdict: needs curation

## Target

Reviewed the generated merge record for `rumen_bacteria_medium__1f7aaf48`, a single-source merge of `data/normalized_yaml/bacterial/TOGO_M1093_Rumen_Bacteria_Medium.yaml`.

The target represents TOGO M1093, `Rumen Bacteria Medium`, imported from JCM M1029 with pH 6.8. The generated record carries the correct high-level source identity, but the import flattened TOGO's nested solution structure and promoted two milligram quantities to gram-per-liter concentrations.

## Validation

- Open schema validation: Passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: Passed; `scripts/validate_strict.py` exited 0 and wrote only the TSV header, so there were 0 strict error rows.
- Reference validation: Passed; `linkml-reference-validator` ran 0 checks and reported all checks passed.
- Term validation: Passed; `linkml-term-validator` exited 0 after the expected `eutils` / `pkg_resources` warning.
- Embedded `curation_history`: Not checked. `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

TOGO M1093 is the right identity for this generated record: the live TOGO payload identifies `http://togomedium.org/medium/M1093`, name `Rumen Bacteria Medium`, `original_media_id` `JCM_M1029`, source URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1029`, and pH `6.8`.

The original JCM `GRMD=1029` URL currently returns "Nothing found.", so TOGO's retained structured payload is the available source of record for this recipe. TOGO still preserves the parent main solution, a local `Mineral solution` subsection, and preparation comments for pH adjustment, a 100% CO2 gas atmosphere, boiling, anaerobic gassing, Hungate-tube distribution, autoclaving, and later addition of the carbohydrate, cysteine, and sodium sulfide sterile stocks.

An exact ignored-file-inclusive local check found the same `rumen_bacteria_medium` concept split across TOGO, JCM, MediaDive, and KOMODO source paths, including `data/merge_yaml/merged/RUMEN_BACTERIA_MEDIUM.yaml`, `data/merge_yaml/merged/rumen_bacteria_medium__b6ddc39f.yaml`, `data/normalized_yaml/bacterial/JCM_J1029_RUMEN_BACTERIA_MEDIUM.yaml`, `data/normalized_yaml/bacterial/KOMODO_330_RUMEN_BACTERIA_medium.yaml`, and `data/normalized_yaml/bacterial/rumen_bacteria_medium.yaml`. This TOGO M1093 record should be reconciled with those siblings after its stock-solution parsing is corrected.

## Evidence

The main TOGO M1093 solution lists `Distilled water` 960 ml, `Yeast extract` 0.5 g, `K2HPO4` 0.3 g, `Resazurin` 1 mg, `Na2S x 9 H2O` 0.25 g, `Na2CO3` 4 g, `Glycerol` 0.5 g, `Cellobiose` 0.5 g, `Maltose` 0.5 g, `Hemin` 1 mg, `Glucose` 0.5 g, `Starch, soluble` 0.5 g, `Trypticase peptone (BD-BBL)` 2 g, `L--Cysteine x HCl x H2O` 0.25 g, `Mineral solution (see below)` 38 ml, `VFA solution (see Medium [M124])` 3.1 ml, and `CO2`.

TOGO M1093 also lists a nested `Mineral solution` with `Distilled water` 1 L plus stock-strength `MgSO4 x 7 H2O` 2.5 g, `NaCl` 12 g, `CaCl2 x 2 H2O` 1.6 g, `KH2PO4` 6 g, and `(NH4)2SO4` 6 g.

TOGO M124 is a complete `Medium 10` record, not a standalone VFA stock record, but its `VFA solution` subsection is the cross-referenced VFA formulation. That subsection contains `DL-alpha-Methyl butyric acid`, `n-Butyric acid`, `Acetic acid`, `n-Valeric acid`, `iso-Valeric acid`, `iso-Butyric acid`, and `Propionic acid`.

## Completeness

The target preserves the primary simple ingredients from M1093 but drops or corrupts the two solution additions:

- `Mineral solution (see below)` is retained as an empty solution with `38 G_PER_L`, while the mineral stock's composition is flattened into the parent at stock strength.
- `VFA solution (see Medium [M124])` is retained as an empty solution with `3.1 G_PER_L`; the seven volatile fatty acid components from the referenced M124 subsection are absent.
- The 1 L mineral-stock water was merged with the 960 ml parent water to create `Distilled water` `961.0 G_PER_L`, which conflates parent medium volume with stock preparation volume.
- TOGO's pH and preparation text are absent, including the 100% CO2 atmosphere, five-minute boiling, pH 6.8 carbonate equilibration, Hungate-tube dispensing, and post-autoclave addition of anaerobically prepared carbohydrate, cysteine, and sodium sulfide stocks.

## Findings

- `needs curation`: Two milligram source quantities became gram-per-liter concentrations. TOGO has `Resazurin` 1 mg and `Hemin` 1 mg in the M1093 main solution, but the generated record has `Resazurin` `1 G_PER_L` and `Hemin` `1 G_PER_L`, a 1000x unit slip for each row.
- `needs curation`: The nested mineral stock was flattened into the parent recipe without applying its 38 ml addition volume. `MgSO4 x 7 H2O` 2.5 g/L, `NaCl` 12 g/L, `CaCl2 x 2 H2O` 1.6 g/L, `KH2PO4` 6 g/L, and `(NH4)2SO4` 6 g/L are stock-strength concentrations, not final parent-medium concentrations.
- `needs curation`: The importer merged unrelated water scopes. The main solution's 960 ml `Distilled water` and the Mineral solution's 1 L `Distilled water` became one parent ingredient, `961.0 G_PER_L`, losing the boundary between final medium water and stock-solution water.
- `needs curation`: The VFA stock was reduced to an empty `solutions` placeholder. TOGO M1093 adds 3.1 ml of the VFA solution cross-referenced to M124, and M124's VFA subsection enumerates seven volatile fatty acids, but none are represented in the generated recipe.
- `needs curation`: Volumetric solution additions are serialized as mass concentrations. `Mineral solution (see below)` and `VFA solution (see Medium [M124])` are parent-medium additions of 38 ml and 3.1 ml, but the generated `solutions` entries say `38 G_PER_L` and `3.1 G_PER_L`.
- `pass with minor issues`: Source identity and primary chemical grounding are otherwise plausible. The generated record points to TOGO M1093 / JCM M1029 and the hydrate terms for sodium sulfide nonahydrate, magnesium sulfate heptahydrate, calcium chloride dihydrate, and L-cysteine hydrochloride hydrate are consistent with the ingredient labels.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/TOGO_M1093_Rumen_Bacteria_Medium.yaml`, or the TOGO import logic that creates it, rather than hand-editing `data/merge_yaml/merged/rumen_bacteria_medium__1f7aaf48.yaml`.
- Convert `Resazurin` and `Hemin` from `1 mg` source amounts to 0.001 g/L-equivalent concentrations, or preserve the original `1 mg` source amount if the schema can represent source mass directly.
- Preserve the local `Mineral solution` as a nested solution with its own 1 L stock composition, and keep the parent addition as 38 ml. Do not merge the stock water into the parent water row.
- Resolve `VFA solution (see Medium [M124])` by importing the VFA subsection from TOGO M124 into a nested solution and retaining the parent addition as 3.1 ml.
- Add preparation and condition notes from the TOGO comments: final pH 6.8, 100% CO2, anaerobic handling, five-minute boiling, Hungate-tube dispensing, and the staged addition of Na2CO3, carbohydrate, cysteine, and sodium sulfide stocks.
- After TOGO M1093 is corrected, rerun the merge and compare it with the JCM, MediaDive, and KOMODO Rumen Bacteria Medium siblings for true duplicate or variant relationships.

## Follow-up Checks

- Rerun open schema, strict, reference, and term validation on `data/normalized_yaml/bacterial/TOGO_M1093_Rumen_Bacteria_Medium.yaml`.
- Regenerate `data/merge_yaml/merged/rumen_bacteria_medium__1f7aaf48.yaml` and verify that neither `Resazurin` nor `Hemin` remains at `1 G_PER_L`.
- Verify that the regenerated record has no empty `solutions` entries for Mineral solution or VFA solution.
- Verify that no parent ingredient retains the stock-strength mineral rows `2.5 G_PER_L`, `12 G_PER_L`, `1.6 G_PER_L`, `6 G_PER_L`, and `6 G_PER_L` from the 1 L Mineral solution.
- Run an exact ignored-file-inclusive search for `TOGO_M1093_Rumen_Bacteria_Medium`, `JCM_J1029_RUMEN_BACTERIA_MEDIUM`, `KOMODO_330_RUMEN_BACTERIA_medium`, and `rumen_bacteria_medium` before deleting or merging duplicate normalized sources.

## Additional Notes

The absence of `target_organisms` was not treated as a defect for this generated record review. No manual edits should be made under `data/merge_yaml/merged`; the generated output should change only after the normalized TOGO source or import logic is fixed and the merge is rerun.
