# YAML Record Review: Cyanobacteria Medium SWES (Seawater - Soil Extract - Salts)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/cyanobacteria_medium_swes_seawater_soil_extract_salts.yaml
- Started UTC: 2026-09-22T12:35:56Z
- Finished UTC: 2026-09-22T12:40:09Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:001260 |
| Name | cyanobacteria_medium_swes_seawater_soil_extract_salts |
| Source | DSMZ / MediaDive medium 1831 |
| Media term | mediadive.medium:1831, DSMZ Medium 1831 |
| Generated record | data/merge_yaml/merged/cyanobacteria_medium_swes_seawater_soil_extract_salts.yaml |
| Maintained medium input | data/normalized_yaml/bacterial/cyanobacteria_medium_swes_seawater_soil_extract_salts.yaml |
| Maintained solution inputs | data/normalized_yaml/bacterial/mediadive_6377_Micronutrient_Solution.yaml; data/normalized_yaml/bacterial/mediadive_5790_Preparation_of_soil_extract.yaml |

The merged record is a single-source generated copy of the normalized DSMZ /
MediaDive import. Future repairs belong in the normalized MediaDive medium and
solution inputs, or in the MediaDive solution import and merge logic that
converted raw volume additions into scalar concentration fields.

## Validation

| Check | Result |
|---|---|
| LinkML open-schema validation, `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/cyanobacteria_medium_swes_seawater_soil_extract_salts.yaml` | Passed |
| Closed-schema validation, `python scripts/validate_strict.py data/merge_yaml/merged/cyanobacteria_medium_swes_seawater_soil_extract_salts.yaml --out /private/tmp/cyanobacteria_medium_swes.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 error rows |
| Reference validation, `linkml-reference-validator validate data data/merge_yaml/merged/cyanobacteria_medium_swes_seawater_soil_extract_salts.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks |
| Term validation, `linkml-term-validator validate-data data/merge_yaml/merged/cyanobacteria_medium_swes_seawater_soil_extract_salts.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history validation | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` entries embedded in merged YAML |

The passing schema checks prove that the YAML shape is acceptable; they do not
prove the units or stock-solution arithmetic against DSMZ medium 1831.

## Identity and Grounding

The record identity is correct. `CultureMech:001260` names DSMZ / MediaDive
medium `1831`, "Cyanobacteria Medium SWES (Seawater - Soil Extract - Salts)",
and the live MediaDive JSON export for medium `1831` gives the same medium ID,
title, DSMZ source, complex-medium flag, and description for cultivation of
marine cyanobacteria and protists.

A gitignore-independent search with `rg --no-ignore --hidden` over
`data/normalized_yaml`, `data/raw`, and the generated target found one
normalized MediaRecipe with `mediadive.medium:1831`, this generated
MediaRecipe, the already-reviewed `1831a` sibling, and no raw `1831` capture
under `data/raw`.

The generated record keeps the DSMZ medium identity but does not preserve the
source solution graph. DSMZ/MediaDive main solution `6376` should contain raw
volume additions of nitrate, phosphate, and magnesium stock solutions,
Micronutrient Solution `6377`, Preparation of soil extract `5790`, and
filter-sterilized vitamin B12, with filtered natural seawater as the make-up
solvent. The generated YAML instead flattens the main solution, micronutrient
stock, and soil-extract stock into one top-level ingredient list.

## Evidence

The live DSMZ PDF for medium 1831 and MediaDive export for medium 1831 both
support these final-medium additions:

| Source component | Source amount | Record amount |
|---|---:|---:|
| Filtered natural seawater | make up final 1000 ml | preparation text only |
| KNO3, from a 19 g/L stock | 10.5 ml/L | 10.5 g/L |
| K2HPO4, from a 4.35 g/L stock | 4.6 ml/L | 4.6 g/L |
| MgSO4 x 7 H2O, from a 7.5 g/L stock | 2.7 ml/L | 2.7 g/L |
| Micronutrient Solution | 5 ml/L | flattened as stock constituents |
| Soil Extract | 30 ml/L | flattened as 300 g/L Garden soil |
| Vitamin B12, from a 0.02 g/L stock | 250 uL/L | 250 g/L |

The record therefore inflates several components by replacing the volume of a
stock solution with grams per liter of the stock ingredient. KNO3 should be
represented as 10.5 ml/L of 19 g/L stock, or 0.1995 g/L if deliberately
back-calculated; it is not 10.5 g/L. Vitamin B12 is 250 uL/L of 0.02 g/L
stock, or 0.000005 g/L if back-calculated; it is not 250 g/L.

The same error recurs in the micronutrient solution. MediaDive solution `6377`
contains 70 ml of 10 g/L FeSO4 x 7 H2O stock, 10 ml of 80 g/L
Na-EDTA x 2 H2O stock, 1 ml of 1 g/L ZnSO4 x 7 H2O stock, 2 ml of
0.76 g/L MnSO4 x 1 H2O stock, 5 ml of 2 g/L H3BO3 stock, 0.2 ml of
5 g/L Co(NO3)2 x 6 H2O stock, 5 ml of 0.2 g/L Na2 MoO4 x 2 H2O stock, and
20 uL of 0.25 g/L CuSO4 x 5 H2O stock made up to a one-liter micronutrient
stock. The generated record flattens the micronutrient stock into final medium
and records the raw 70, 10, 1, 2, 5, 0.2, 5, and 20 additions as `G_PER_L`;
the 20 uL copper addition is particularly wrong because both the stock boundary
and microliter unit are lost.

The soil-extract boundary is also lost. MediaDive solution `5790` is a 700 ml
preparation that starts from 300 ml Garden soil, and the main solution uses
30 ml/L of the resulting extract. The generated record records Garden soil
directly at 300 g/L in the final medium.

The direct DSMZ PDF and the live MediaDive export disagree on some soil-extract
details. DSMZ's PDF describes filling a one-liter Schott bottle one third with
garden or leaf soil and autoclaving the filtered supernatant before
refrigerated storage; the MediaDive export uses 300 ml garden soil, a 700 ml
make-up volume, PES filter sterilization, and storage at 4-10 deg C. That
conflict should be preserved as a source discrepancy until a curator chooses
the authoritative DSMZ representation.

## Completeness

- The record has no `references`, `source_data`, `target_organisms`,
  `growth_metrics`, structured solution references, or explicit source
  retrieval URL. Empty target-organism and growth-metric slots are acceptable
  because DSMZ medium 1831 is a recipe record, not a primary growth assay.
- The missing structured solution references are consequential: without them,
  a reader cannot distinguish final-medium additions from Micronutrient
  Solution or Preparation of soil extract preparation rows.
- The normalized companion solution files for MediaDive solution IDs `6377` and
  `5790` are present. The problem is not absent solution records, but an import
  representation that stores their volume rows as `PERCENT_V_V` and a merge
  projection that flattens them as final `G_PER_L` ingredients.
- No local raw `1831` capture was found by a gitignore-independent search over
  `data/raw`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Final-medium stock additions were imported as final grams per liter. | DSMZ/MediaDive list stock additions in `ml` or `uL` to a 1000 ml main solution; the merged record stores the same raw numeric values as `G_PER_L` for KNO3, K2HPO4, MgSO4 x 7 H2O, and vitamin B12. | `data/normalized_yaml/bacterial/cyanobacteria_medium_swes_seawater_soil_extract_salts.yaml` and the MediaDive importer |
| major | Micronutrient Solution `6377` was flattened into final-medium top-level ingredients and its raw ml/uL stock additions became `G_PER_L`. | MediaDive JSON has solution `6377` as a nested 5 ml/L addition; the merged YAML instead lists FeSO4, Na-EDTA, ZnSO4, MnSO4, H3BO3, Co(NO3)2, Na2 MoO4, and CuSO4 directly, with raw stock-preparation amounts. | `data/normalized_yaml/bacterial/mediadive_6377_Micronutrient_Solution.yaml` and solution merge logic |
| major | Preparation of soil extract `5790` was flattened into final-medium `Garden soil: 300 G_PER_L`. | The main solution uses 30 ml/L of soil extract, and the extract stock starts from soil made up to 700 ml; the final medium does not contain 300 g/L Garden soil. | `data/normalized_yaml/bacterial/mediadive_5790_Preparation_of_soil_extract.yaml`, the parent medium, and solution merge logic |
| major | Soil-extract preparation has an unresolved DSMZ-vs-MediaDive source conflict. | The current DSMZ PDF and MediaDive export use different wording and terminal sterilization/storage details for the soil-extract protocol. | MediaDive raw capture or source-transform provenance for medium 1831 |
| minor | The generated recipe has only generic DSMZ provenance. | The identity is recoverable from `mediadive.medium:1831` and import history, but there is no explicit `reference` or `source_data` entry naming the MediaDive or DSMZ retrieval URL. | `data/normalized_yaml/bacterial/cyanobacteria_medium_swes_seawater_soil_extract_salts.yaml` |

## Recommended Edits

1. Repair the MediaDive solution importer or normalized MediaDive inputs so
   solution rows keep their source units (`ml`, `uL`) and stock-solution
   boundaries instead of being normalized to `PERCENT_V_V` or projected as
   final `G_PER_L`.
2. Represent `Main sol. 1831` as the parent 1000 ml final solution with
   10.5 ml KNO3 stock, 4.6 ml K2HPO4 stock, 2.7 ml MgSO4 x 7 H2O stock,
   5 ml Micronutrient Solution `6377`, 30 ml Preparation of soil extract
   `5790`, and 250 uL filter-sterilized vitamin B12 stock, with filtered
   natural seawater as the make-up solvent.
3. Preserve `Micronutrient Solution *` as a one-liter nested solution with the
   eight DSMZ/MediaDive stock additions and the 20 uL CuSO4 x 5 H2O row,
   rather than flattening those ingredients into the final medium.
4. Preserve `Preparation of soil extract` as a separate 700 ml stock/preparation
   recipe and link the parent medium to 30 ml/L of the extract. Resolve the live
   DSMZ PDF vs MediaDive export difference before replacing the existing
   preparation text.
5. Add explicit source provenance for the DSMZ/MediaDive 1831 export used
   during the repair.
6. Regenerate `data/merge_yaml/merged/cyanobacteria_medium_swes_seawater_soil_extract_salts.yaml`
   after repairing the maintained inputs; do not edit the generated merge
   directly.

## Follow-up Checks

- Run open-schema, closed-schema, reference, and term validation on the repaired
  normalized MediaRecipe and the two involved SolutionRecipe files.
- Regenerate the merged record and verify that it either preserves structured
  solution references or computes any intended final concentrations from the
  source stock strengths dimensionally.
- Diff the regenerated record against MediaDive medium 1831 and DSMZ Medium
  1831, checking every ingredient amount, unit, stock concentration, solution
  volume, and preparation step.
- Re-run `rg --no-ignore --hidden` for `1831`, `mediadive.solution:6377`, and
  `mediadive.solution:5790` across `data/normalized_yaml` and `data/raw` after
  regeneration to ensure no stale split or flattened copy remains.

## Additional Notes

- MediaDive exports `Main sol. 1831` as the 1000 ml main solution with ID
  `6376`, but this repository has no split `mediadive_6376_Main_sol_1831.yaml`
  file analogous to the nested stock recipes.
- MediaDive `/download/composition/1831/json` leaves all g/L and mmol/L
  computed composition fields null for this medium, which is consistent with
  the stock-heavy recipe and further argues against projecting source volumes
  as direct final grams per liter.
