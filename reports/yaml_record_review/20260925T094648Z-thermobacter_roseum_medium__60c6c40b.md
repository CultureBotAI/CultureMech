# YAML Record Review: THERMOBACTER ROSEUM MEDIUM
- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermobacter_roseum_medium__60c6c40b.yaml`
- Started UTC: `2026-09-25T09:46:48Z`
- Finished UTC: `2026-09-25T09:48:01Z`
- Verdict: needs curation

## Target
Generated MediaDive bacterial recipe `CultureMech:003247`, `thermobacter_roseum_medium`, with medium term `mediadive.medium:J899` and label `THERMOBACTER ROSEUM MEDIUM`.

It is a single-source generated record from normalized source `thermobacter_roseum_medium`.

## Validation
- LinkML schema validation: passed; `linkml-validate` reported `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file with 0 files containing errors and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported all checked references passed.
- Term validation: passed; `linkml-term-validator` reported `Validation passed`.
- Embedded `curation_history`: Not checked. The available history validator targets standalone `history/` entries rather than `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding
The record is correctly grounded to JCM Medium 899, `THERMOBACTER ROSEUM MEDIUM`, through `mediadive.medium:J899`.

The same JCM 899 source URL is still present in the TOGO M940 branch emitted as `data/merge_yaml/merged/THERMOBACTER_ROSEUM_MEDIUM.yaml`.

One stale legacy grounding remains: `Na2SeO4` has the correct primary `term` `CHEBI:77775` but still carries `mediaingredientmech_term: MediaIngredientMech:000198` instead of a `mediaingredientmech_chebi_term`.

## Evidence
JCM 899 and MediaDive J899 define a main solution with KH2PO4, NH4Cl, NaCl, MgCl2 x 6 H2O, KCl, CaCl2 x 2 H2O, NaHCO3, 1 mg resazurin, yeast extract, and water. After autoclaving under N2, the source adds 1 ml Vitamin solution, 1 ml Trace element solution, and 6 ml of 5% Na2S x 9 H2O.

The generated MediaDive branch keeps the base milligram resazurin as a low final concentration, but it converts the 6 ml sulfide stock addition into a direct `Na2S x 9 H2O` row at `6 G_PER_L`.

The generated branch flattens the 1 ml Vitamin solution into top-level final ingredients at stock concentrations, including `p-Aminobenzoic acid`, `Biotin`, `Nicotinic acid`, `DL-Calcium pantothenate`, `Pyridoxine hydrochloride`, and `Vitamin B12`.

It also flattens the 1 ml Trace element solution into top-level final ingredients at stock concentrations, including ferrous ammonium sulfate, cobalt chloride, ammonium nickel sulfate, sodium molybdate, sodium tungstate, zinc sulfate, copper chloride, sodium selenate, boric acid, and manganese chloride.

## Completeness
The generated MediaDive branch preserves the main JCM preparation instructions and final pH check.

The TOGO M940 branch for the same JCM source should not be merged as-is because its vitamin milligram values have been promoted to whole gram-per-liter rows and its 1 L stock waters have been merged into the final water row.

## Findings
1. Needs curation: Vitamin solution was flattened into top-level final ingredients at 1 L stock concentrations.
2. Needs curation: Trace element solution was flattened into top-level final ingredients at 1 L stock concentrations.
3. Needs curation: 6 ml of 5% Na2S x 9 H2O was converted to `6 G_PER_L` final sodium sulfide nonahydrate.
4. Needs curation: TOGO M940 remains an unmerged duplicate branch for the same JCM 899 source.
5. Minor issue: `Na2SeO4` still has a stale `mediaingredientmech_term` instead of a CHEBI-keyed `mediaingredientmech_chebi_term`.

## Recommended Edits
1. Normalize the MediaDive and TOGO JCM 899 source records, not the generated merge files, so Vitamin solution, Trace element solution, and 5% Na2S x 9 H2O remain separate post-autoclave stock additions.
2. Preserve source milligram units inside the vitamin and trace stocks before scaling them by their 1 ml/L final additions.
3. Convert the stale `Na2SeO4` MediaIngredientMech link to the CHEBI-keyed form during source cleanup.
4. Merge `mediadive.medium:J899` with the TOGO M940 import by exact JCM 899 source identity after both branches represent stocks consistently.

## Follow-up Checks
After source normalization and merge regeneration, re-run schema, strict, reference, and term validation.

Run an exact duplicate search with ignored files included for `mediadive.medium:J899`, `TOGO_M940_Thermobacter_Roseum_Medium`, and `jcm_grmd?GRMD=899` and confirm that JCM 899 regenerates as one canonical output with nested vitamin, trace, and sulfide stocks.

## Additional Notes
Exact duplicate-source searches included ignored files.
