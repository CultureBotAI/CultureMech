# YAML Record Review: ruminoclostridium_cellulolyticum_cm3_medium__8685db78

- Repository: CultureMech
- Record: `data/merge_yaml/merged/ruminoclostridium_cellulolyticum_cm3_medium__8685db78.yaml`
- Started UTC: `2026-09-25T03:12:25Z`
- Finished UTC: `2026-09-25T03:12:25Z`
- Verdict: needs curation

## Target

Reviewed the generated merge record for `ruminoclostridium_cellulolyticum_cm3_medium__8685db78`, a single-source merge of `data/normalized_yaml/bacterial/TOGO_M2733_Ruminoclostridium_Cellulolyticum_CM3_Medium.yaml`.

The target represents TOGO M2733, `Ruminoclostridium Cellulolyticum (CM3) Medium`, whose upstream URL is DSMZ Medium 520. It is source-identical to the DSMZ/MediaDive Medium 520 record already present as `data/merge_yaml/merged/ruminoclostridium_cellulolyticum_cm3_medium.yaml`, but the TOGO import has unit slips and stock-flattening defects that gave it a different merge fingerprint.

## Validation

- Open schema validation: Passed; `linkml-validate` exited 0 with `No issues found`.
- Strict validation: Passed; `scripts/validate_strict.py` exited 0 and reported 0 total error rows.
- Reference validation: Passed; `linkml-reference-validator` ran 0 checks and reported all checks passed.
- Term validation: Passed; `linkml-term-validator` exited 0 after the expected `eutils` / `pkg_resources` warning.
- Embedded `curation_history`: Not checked. `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

TOGO M2733 is correctly grounded to DSMZ Medium 520. Its live payload identifies `http://togomedium.org/medium/M2733`, name `Ruminoclostridium Cellulolyticum (CM3) Medium`, source URL `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium520.pdf`, and pH `7.2`.

The generated record is split from the direct DSMZ/MediaDive 520 import because the TOGO path mishandles 75 mg calcium chloride, the 1 ml SL-10 stock addition, and several milligram SL-10 rows. Once fixed, TOGO M2733 should collapse with the base DSMZ 520 parent rather than remain a separate generated recipe.

## Evidence

The TOGO M2733 main solution lists 0.5 ml `Na-resazurin solution (0.1% w/v)`, 1000 ml distilled water, 2 g yeast extract, 75 mg `CaCl2 x 2 H2O`, 1.5 g `KH2PO4`, 0.2 g `MgCl2 x 6 H2O`, 1.3 g `(NH4)2SO4`, 1.5 g `Na2CO3`, 2.9 g `K2HPO4 x 3 H2O`, 6 g cellobiose, 1.25 ml `FeSO4 x 7 H2O solution (0.1% w/v in 0.1 N H2SO4)`, 0.5 g `L-Cysteine-HCl x H2O`, 1 ml `Trace element solution SL-10`, carbon dioxide gas, and nitrogen gas.

The TOGO M2733 `Trace element solution SL-10` subsection lists 990 ml distilled water, 36 mg `Na2MoO4 x 2 H2O`, 6 mg `H3BO3`, 100 mg `MnCl2 x 4 H2O`, 190 mg `CoCl2 x 6 H2O`, 24 mg `NiCl2 x 6 H2O`, 2 mg `CuCl2 x 2 H2O`, 70 mg `ZnCl2`, 10 ml `HCl (25%; 7.7 M)`, and 1.5 g `FeCl2 x 4 H2O`.

TOGO also retains DSMZ preparation comments that describe 80% N2 / 20% CO2 sparging, autoclaving, post-autoclave addition of magnesium chloride, calcium chloride, cellobiose, and carbonate stocks, cysteine addition before inoculation, pH adjustment to 7.2, optional adaptation to 10 g/L cellulose powder MN 301, and SL-10 preparation.

## Completeness

The generated record retains the DSMZ 520 identity, but loses or corrupts these source details:

- `CaCl2 x 2 H2O` 75 mg is stored as `75 G_PER_L`.
- `Na-resazurin solution`, `FeSO4 x 7 H2O solution`, and `Trace element solution SL-10` are empty solution placeholders with `G_PER_L` values copied from 0.5 ml, 1.25 ml, and 1 ml source aliquots.
- The SL-10 stock is flattened into the parent and its milligram masses are promoted to gram-per-liter values such as `CoCl2 x 6 H2O` `190 G_PER_L`, `MnCl2 x 4 H2O` `100 G_PER_L`, and `ZnCl2` `70 G_PER_L`.
- Main-solution and SL-10 waters are merged into one `Distilled water` `1990.0 G_PER_L` row.
- DSMZ preparation and optional-cellulose comments are absent.
- N2 and CO2 sparging gases are modeled as variable-concentration ingredients, not preparation conditions.

## Findings

- `needs curation`: The source 75 mg `CaCl2 x 2 H2O` row has a 1000x unit slip and appears as `75 G_PER_L`.
- `needs curation`: The 1 ml SL-10 stock addition was flattened into direct parent ingredients and every SL-10 milligram row was promoted to grams per liter. This is the cause of the generated `high_metal: true` flag.
- `needs curation`: Three solution aliquots were serialized as mass concentrations. DSMZ Medium 520 adds 0.5 ml Na-resazurin solution, 1.25 ml FeSO4 solution, and 1 ml SL-10; the generated `solutions` entries are empty and report `0.5 G_PER_L`, `1.25 G_PER_L`, and `1 G_PER_L`.
- `needs curation`: The generated record merges unrelated water scopes, summing the 1000 ml main-solution water with the 990 ml SL-10 stock water as `1990.0 G_PER_L`.
- `needs curation`: The imported preparation comments were dropped, including anaerobic gas composition, post-autoclave stock additions, cellobiose filtration, pH 7.2 adjustment, the optional 10 g/L cellulose adaptation, and SL-10 preparation.
- `pass with minor issues`: The gram-denominated base rows for yeast extract, phosphate, magnesium chloride, ammonium sulfate, carbonate, cellobiose, and cysteine match TOGO M2733, allowing for the TOGO path's source-mass style rather than MediaDive's 1003 ml final `g_l` normalization.

## Recommended Edits

- Fix `data/normalized_yaml/bacterial/TOGO_M2733_Ruminoclostridium_Cellulolyticum_CM3_Medium.yaml`, or the TOGO import logic that creates it, rather than hand-editing `data/merge_yaml/merged/ruminoclostridium_cellulolyticum_cm3_medium__8685db78.yaml`.
- Convert 75 mg `CaCl2 x 2 H2O` and the milligram SL-10 component rows to gram-scale stock concentrations, or preserve their source masses inside a nested SL-10 recipe.
- Preserve `Na-resazurin solution`, `FeSO4 x 7 H2O solution`, and `Trace element solution SL-10` as solution additions with milliliter parent aliquots.
- Keep the 1000 ml main water and 990 ml SL-10 water in their own scopes; do not merge them into one parent row.
- Convert the N2 and CO2 entries to preparation atmosphere metadata or suppress them as standalone ingredients if the gas concentrations cannot be represented.
- Carry the DSMZ preparation comments into `preparation_steps` and preserve the optional cellulose note.
- After TOGO M2733 is corrected, rerun the merge and compare it with the direct DSMZ/MediaDive 520 import for source-duplicate merging.

## Follow-up Checks

- Rerun open schema, strict, reference, and term validation on `data/normalized_yaml/bacterial/TOGO_M2733_Ruminoclostridium_Cellulolyticum_CM3_Medium.yaml`.
- Regenerate `data/merge_yaml/merged/ruminoclostridium_cellulolyticum_cm3_medium__8685db78.yaml` and verify that `CaCl2 x 2 H2O` is no longer `75 G_PER_L`.
- Verify that no SL-10 milligram stock row remains as a large direct parent ingredient and that `high_metal: true` is recalculated away unless another real high-metal source remains.
- Verify that the regenerated record has no empty solution entries for Na-resazurin, FeSO4, or SL-10.
- Run an exact ignored-file-inclusive search for `TOGO_M2733_Ruminoclostridium_Cellulolyticum_CM3_Medium`, `mediadive.medium:520`, and `ruminoclostridium_cellulolyticum_cm3_medium` before deduplicating normalized DSMZ 520 sources.

## Additional Notes

Empty `target_organisms` were not treated as defects for this generated record review. The Japanese `Properties: gas` label in the generated CO2 and N2 ingredient notes was not itself scored; those gas rows are a modeling issue because they came from atmosphere instructions.
