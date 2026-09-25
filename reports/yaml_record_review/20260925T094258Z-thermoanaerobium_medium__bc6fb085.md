# YAML Record Review: THERMOANAEROBIUM MEDIUM
- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoanaerobium_medium__bc6fb085.yaml`
- Started UTC: `2026-09-25T09:42:58Z`
- Finished UTC: `2026-09-25T09:43:50Z`
- Verdict: needs curation

## Target
Generated MediaDive bacterial recipe `CultureMech:003016`, `thermoanaerobium_medium`, with medium term `mediadive.medium:J671` and label `THERMOANAEROBIUM MEDIUM`.

It is a single-source generated record from normalized source `thermoanaerobium_medium`.

## Validation
- LinkML schema validation: passed; `linkml-validate` reported `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file with 0 files containing errors and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported all checked references passed.
- Term validation: passed; `linkml-term-validator` reported `Validation passed`.
- Embedded `curation_history`: Not checked. The available history validator targets standalone `history/` entries rather than `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding
The record is correctly grounded to JCM Medium 671, `THERMOANAEROBIUM MEDIUM`, through `mediadive.medium:J671`.

The same JCM 671 recipe is still emitted as the TOGO M690 branch `data/merge_yaml/merged/thermoanaerobium_medium__7979ea06.yaml`.

The reviewed MediaDive branch has internally consistent CHEBI groundings for hydrate salts and vitamin rows after normalization.

## Evidence
JCM 671 and MediaDive J671 define a 950 ml base with yeast extract, tryptone, NH4Cl, NaCl, MgCl2 x 6 H2O, KH2PO4, K2HPO4, 9 ml Trace element solution, 5 ml Trace vitamins, 3 mg FeSO4 x 7 H2O, 1 mg resazurin, plus post-autoclave 50 ml 10% glucose and 10 ml 5% Na2S x 9 H2O solution.

The MediaDive branch correctly represents the base 3 mg FeSO4 x 7 H2O and 1 mg resazurin as low final concentrations, but it flattens the 9 ml Trace element solution into top-level stock concentrations such as `Nitrilotriacetic acid` at `12.8 G_PER_L` and `FeCl2 x 4 H2O` at `0.2 G_PER_L`.

The trace stock `NaCl` row is merged with the base medium NaCl row, yielding `1.878906 G_PER_L` and erasing the distinction between the base solution and the 9 ml stock addition.

Trace vitamins are also flattened at stock concentrations: `Biotin` and `Folic acid` at `0.002 G_PER_L`, `Pyridoxine hydrochloride` at `0.01 G_PER_L`, and `Vitamin B12` at `0.0001 G_PER_L`.

Finally, the 50 ml 10% glucose and 10 ml 5% sulfide additions are emitted as `Glucose` at `50 G_PER_L` and `Na2S x 9 H2O` at `10 G_PER_L`, treating source volumes as final concentrations.

## Completeness
The MediaDive branch preserves the main JCM preparation steps: autoclaving the 950 ml base under N2, separately autoclaving glucose and sulfide under N2, adding those stocks, and readjusting final pH to 7.2 - 7.4 if needed.

The generated structure remains incomplete because the stocks named in those preparation steps do not exist as nested stock additions after flattening.

## Findings
1. Needs curation: Trace element solution was flattened into final ingredients and its NaCl row was merged with the base NaCl.
2. Needs curation: Trace vitamins were flattened into final ingredients at stock concentrations.
3. Needs curation: 10% Glucose solution and 5% Na2S x 9 H2O solution were converted from milliliter stock additions into `50 G_PER_L` and `10 G_PER_L` final rows.
4. Needs curation: TOGO M690 remains an unmerged JCM 671 duplicate branch.

## Recommended Edits
1. Normalize `thermoanaerobium_medium` in `data/normalized_yaml`, not the generated merge file, so the main recipe retains 9 ml Trace element solution, 5 ml Trace vitamins, 50 ml 10% Glucose solution, and 10 ml 5% Na2S x 9 H2O solution.
2. Prevent stock components from merging with base components before their stock addition factors are represented.
3. Merge `mediadive.medium:J671` and `TOGO:M690` by exact JCM 671 identity after the MediaDive and TOGO branches share the same nested-stock representation.

## Follow-up Checks
After source normalization and merge regeneration, re-run schema, strict, reference, and term validation.

Run an exact duplicate search with ignored files included for `mediadive.medium:J671`, `TOGO:M690`, and `jcm_grmd?GRMD=671` and confirm that JCM 671 regenerates as one canonical output with no top-level stock rows.

## Additional Notes
Exact duplicate-source searches included ignored files. A first pass that included exact normalized names was discarded for duplicate-source purposes because it also matched unrelated Thermoanaerobium branches outside JCM 671.
