# YAML Record Review: Thermoanaerobium Medium
- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoanaerobium_medium__7979ea06.yaml`
- Started UTC: `2026-09-25T09:41:36Z`
- Finished UTC: `2026-09-25T09:42:57Z`
- Verdict: needs curation

## Target
Generated TOGO bacterial recipe `CultureMech:010096`, `thermoanaerobium_medium`, with medium term `TOGO:M690` and label `Thermoanaerobium Medium`.

It is a single-source generated record from `TOGO_M690_Thermoanaerobium_Medium`.

## Validation
- LinkML schema validation: passed; `linkml-validate` reported `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file with 0 files containing errors and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported all checked references passed.
- Term validation: passed; `linkml-term-validator` reported `Validation passed`.
- Embedded `curation_history`: Not checked. The available history validator targets standalone `history/` entries rather than `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding
The record correctly points to JCM Medium 671, `THERMOANAEROBIUM MEDIUM`, through `TOGO:M690`.

The same JCM 671 identity remains split into the MediaDive-generated branch `data/merge_yaml/merged/thermoanaerobium_medium__bc6fb085.yaml`, which carries `mediadive.medium:J671`.

Several hydrate ingredients in this TOGO branch use source spellings with a non-ASCII hydrate separator, but their primary CHEBI terms resolve to the expected hydrate chemicals. Some rows, such as `CoCl2 x 6 H2O`, retain a less specific primary term than the MediaDive branch.

## Evidence
JCM 671 and MediaDive J671 define a 950 ml base containing yeast extract, tryptone, NH4Cl, NaCl, MgCl2 x 6 H2O, KH2PO4, K2HPO4, 9 ml Trace element solution, 5 ml Trace vitamins, 3 mg FeSO4 x 7 H2O, and 1 mg resazurin. After autoclaving, 50 ml of 10% glucose and 10 ml of 5% Na2S x 9 H2O solution are added per 950 ml.

The generated TOGO branch converts the milligram base ingredients into grossly inflated final gram-per-liter rows: `Resazurin` is `1 G_PER_L` and `FeSO4 x 7 H2O` is `3 G_PER_L`.

The generated TOGO branch also flattens Trace element solution into the top-level recipe at stock concentrations, including `Nitrilotriacetic acid` at `12.8 G_PER_L`, `FeCl2 x 4 H2O` at `0.2 G_PER_L`, and `NaCl` at `1 G_PER_L`; that stock `NaCl` is merged with the base `NaCl` to yield `1.9 G_PER_L`.

The 10% glucose and 5% sulfide additions remain only as solution stubs with concentrations `50 G_PER_L` and `10 G_PER_L`, which are actually stock volumes in milliliters, not final gram-per-liter concentrations.

## Completeness
The TOGO branch lacks the structured JCM preparation steps for separately autoclaving 10% glucose and 5% sulfide stocks under N2 and readjusting the final pH to 7.2 - 7.4 with sterile NaOH as needed.

It also leaves the 5 ml Trace vitamins cross-reference to Medium 197 as an unresolved empty solution, while the MediaDive import expands that stock.

## Findings
1. Needs curation: 1 mg resazurin and 3 mg FeSO4 x 7 H2O were converted to `1 G_PER_L` and `3 G_PER_L`.
2. Needs curation: Trace element solution was flattened into the final recipe at stock concentrations, and its stock NaCl was merged into the base NaCl.
3. Needs curation: 10% Glucose solution and 5% Na2S x 9 H2O solution are represented with their milliliter addition volumes as `G_PER_L` values.
4. Needs curation: TOGO M690 and MediaDive J671 remain unmerged duplicate branches for the same JCM 671 source.
5. Minor issue: hydrate spelling and cobalt chloride grounding should be made consistent with the MediaDive branch during source normalization.

## Recommended Edits
1. Normalize `TOGO_M690_Thermoanaerobium_Medium` in `data/normalized_yaml`, not the generated merge file, so Trace element solution, Trace vitamins, 10% Glucose solution, and 5% Na2S x 9 H2O solution remain nested additions.
2. Preserve source milligram units for FeSO4 x 7 H2O and resazurin in the 950 ml base instead of promoting the source amounts to grams per liter.
3. Resolve the Trace vitamins cross-reference against JCM Medium 197 or leave it as a structured external stock reference instead of an empty `Unknown solution`.
4. Merge `TOGO:M690` and `mediadive.medium:J671` by exact JCM 671 source identity after both branches represent stocks consistently.

## Follow-up Checks
After source normalization and merge regeneration, re-run schema, strict, reference, and term validation.

Run an exact duplicate search with ignored files included for `TOGO:M690`, `mediadive.medium:J671`, and `jcm_grmd?GRMD=671` and confirm that JCM 671 regenerates as one canonical output.

## Additional Notes
Exact duplicate-source searches included ignored files. A first pass that included exact normalized names was discarded for duplicate-source purposes because it also matched unrelated Thermoanaerobium branches outside JCM 671.
