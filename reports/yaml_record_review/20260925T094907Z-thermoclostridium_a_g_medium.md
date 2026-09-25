# YAML Record Review: Thermoclostridium A-G Medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoclostridium_a_g_medium.yaml`
- Started UTC: `2026-09-25T09:49:07Z`
- Finished UTC: `2026-09-25T09:50:09Z`
- Verdict: needs curation

## Target
Generated TOGO bacterial recipe `CultureMech:009307`, `thermoclostridium_a_g_medium`, with medium term `TOGO:M2756`.

It is a single-source generated record from the TOGO import for DSMZ Medium 326.

## Validation
- LinkML schema validation: passed; `linkml-validate` reported `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file with 0 files containing errors and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported all checked references passed.
- Term validation: passed; `linkml-term-validator` reported `Validation passed`.
- Embedded `curation_history`: Not checked. The available history validator targets standalone `history/` entries rather than `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding
The record correctly points to DSMZ Medium 326 through TOGO M2756 and `DSMZ_Medium326.pdf`.

The same DSMZ 326 recipe is present in `data/merge_yaml/merged/thermoclostridium_a_g_medium__441f8294.yaml`, the MediaDive branch for `mediadive.medium:326`.

CHEBI groundings generally match the inflated ingredient strings, but the generated `high_metal: true` flag is a symptom of stock-parsing failure rather than a true property of the DSMZ recipe.

## Evidence
DSMZ Medium 326 and MediaDive medium 326 specify direct main-solution rows for KH2PO4, MgCl2 x 6 H2O, 12 mg CoCl2 x 6 H2O, 1 ml Trace element solution SL-10, yeast extract, trypticase peptone, resazurin, carbonate, sucrose, 1 ml Wolin's vitamin solution 10x, cysteine, sulfide, and water.

The TOGO branch flattens SL-10 into the top-level ingredient list and treats its milligram rows as grams. `CoCl2 x 6 H2O` is emitted as `202.0 G_PER_L` after merging a misparsed `12.0` main row with a misparsed `190.0` stock row; `ZnCl2`, `MnCl2 x 4 H2O`, `NiCl2 x 6 H2O`, `Na2MoO4 x 2 H2O`, `H3BO3`, and `CuCl2 x 2 H2O` are likewise inflated.

The TOGO branch also converts the 10 ml 25% HCl row inside SL-10 into a top-level `HCl (25%; 7.7 M)` row at `10 G_PER_L`, instead of retaining that acid as part of the 1 L SL-10 stock recipe.

Wolin's vitamin solution 10x is flattened into top-level final rows and its source milligram values are emitted as gram-per-liter values, such as `Biotin` at `2 G_PER_L`, `Pyridoxine-HCl` at `10 G_PER_L`, and `Vitamin B12` at `0.1 G_PER_L`.

Stock waters were merged into the main water row, producing `2990.0 G_PER_L` from 1000 ml main water, 990 ml SL-10 water, and 1000 ml vitamin stock water.

## Completeness
The generated TOGO branch omits the DSMZ structured preparation step describing anoxic N2/CO2 sparging, separate sterile carbonate, sucrose, vitamin, cysteine, and sulfide stock additions, and final pH adjustment.

The solution stubs for SL-10 and Vitamin solution point to MediaDive stock IDs but have no nested composition while those stock ingredients also appear at the top level.

## Findings
1. Needs curation: Trace element solution SL-10 was flattened and its milligram rows were promoted to gram-per-liter final ingredients.
2. Needs curation: Wolin's vitamin solution 10x was flattened and its milligram rows were promoted to gram-per-liter final ingredients.
3. Needs curation: main and stock waters were merged into `2990.0 G_PER_L`.
4. Needs curation: TOGO M2756 remains an unmerged duplicate of the MediaDive DSMZ 326 branch.

## Recommended Edits
1. Normalize the TOGO and MediaDive DSMZ 326 source records, not the generated merge files, so the main recipe keeps 1 ml/L SL-10 and 1 ml/L Wolin's vitamin solution 10x as nested stock additions.
2. Keep 25% HCl scoped to SL-10 and preserve milligram units inside both stock recipes.
3. Preserve the DSMZ anoxic stock-addition preparation instructions.
4. Merge `TOGO:M2756` and `mediadive.medium:326` by exact DSMZ 326 source identity once both branches represent stock solutions consistently.

## Follow-up Checks
After source normalization and merge regeneration, re-run schema, strict, reference, and term validation.

Run an exact duplicate search with ignored files included for `TOGO:M2756`, `mediadive.medium:326`, and `DSMZ_Medium326.pdf` and confirm that DSMZ 326 regenerates as one canonical output.

## Additional Notes
Exact duplicate-source searches included ignored files.
