# YAML Record Review: THERMOANAEROBACTER ETHANOLICUS MEDIUM
- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoanaerobacter_ethanolicus_medium__3d4166ac.yaml`
- Started UTC: `2026-09-25T09:36:00Z`
- Finished UTC: `2026-09-25T09:37:05Z`
- Verdict: needs curation

## Target
Generated MediaDive bacterial recipe `CultureMech:002583`, `thermoanaerobacter_ethanolicus_medium`, with medium term `mediadive.medium:J221` and label `THERMOANAEROBACTER ETHANOLICUS MEDIUM`.

It is a single-source merge of normalized source `thermoanaerobacter_ethanolicus_medium`, on merge fingerprint `3d4166ac5840ae4fbbee4a06e5ae21732183ca208d3bd758ae658bd4d5b8fe7b`.

## Validation
- LinkML schema validation: passed; `linkml-validate` reported `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file with 0 files containing errors and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported all checked references passed.
- Term validation: passed; `linkml-term-validator` reported `Validation passed`.
- Embedded `curation_history`: Not checked. The available history validator targets standalone `history/` entries rather than `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding
The record is correctly grounded to JCM Medium 221, `THERMOANAEROBACTER ETHANOLICUS MEDIUM`.

The same JCM 221 identity is still present in the TOGO import `TOGO:M214`, which is emitted as `data/merge_yaml/merged/THERMOANAEROBACTER_ETHANOLICUS_MEDIUM.yaml`. The MediaDive/JCM and TOGO/JCM branches therefore remain source-equivalent duplicates.

Most ingredient-level CHEBI terms are internally consistent, but the anhydrous or variably hydrated salts should be kept exactly as JCM specifies them during source normalization: `MnSO4 x n H2O`, `AlK(SO4)2`, `Na2SeO3`, and 0.2 N `NaOH` all occur inside stock recipes rather than as final medium ingredients.

## Evidence
JCM 221 and MediaDive J221 specify a 960 ml base medium containing KH2PO4, Na2HPO4 x 12 H2O, NH4Cl, MgCl2 x 6 H2O, yeast extract, glucose, resazurin, plus 0.5 ml Vitamin solution, 5 ml Wolfe's modified mineral elixir, and 40 ml Reducing solution.

The generated record promotes the Vitamin solution stock into top-level `G_PER_L` rows such as `Biotin` at `0.04`, `p-Aminobenzoic acid` at `0.1`, `Vitamin B12` at `0.002`, and `Pyridoxine hydrochloride` at `0.2`, even though only 0.5 ml of the 500 ml stock is added to the final recipe.

The generated record also promotes Wolfe's modified mineral elixir into top-level rows at its 1 L stock concentrations, including `Nitrilotriacetic acid` at `1.5 G_PER_L`, `MgSO4 x 7 H2O` at `3 G_PER_L`, and `NaCl` at `1 G_PER_L`, although the main JCM recipe adds only 5 ml of that stock.

The 40 ml Reducing solution is flattened into `NaOH` at `200 G_PER_L`, `Na2S x 9 H2O` at `12.5 G_PER_L`, and `L-Cysteine HCl x H2O` at `12.5 G_PER_L`. The JCM row is 200 ml of 0.2 N NaOH inside a 200 ml stock, not 200 g/L NaOH in the final medium.

## Completeness
The generated record preserves the main anaerobic preparation step, the vitamin cold-and-dark storage step, the mineral elixir pH adjustment, and the reducing-solution anaerobic autoclaving step.

The structural completeness defect is that these steps now describe stocks whose ingredients have already been collapsed into the final main solution, so the steps no longer line up with the represented ingredient hierarchy.

## Findings
1. Needs curation: Vitamin solution was flattened into top-level final ingredients at stock concentrations rather than being kept as a 0.5 ml stock addition.
2. Needs curation: Wolfe's modified mineral elixir was flattened into top-level final ingredients rather than being kept as a 5 ml stock addition.
3. Needs curation: Reducing solution was flattened into top-level final ingredients, including the chemically impossible `200 G_PER_L` direct `NaOH` row derived from 200 ml of 0.2 N NaOH.
4. Needs curation: the TOGO M214 JCM 221 branch remains an unmerged duplicate of this MediaDive/JCM branch.

## Recommended Edits
1. Normalize JCM 221 sources in `data/normalized_yaml`, not this generated merge file, so the main recipe keeps explicit additions of Vitamin solution, Wolfe's modified mineral elixir, and Reducing solution.
2. Represent 0.2 N NaOH as the solvent/base of the Reducing solution instead of converting its 200 ml volume to `200 G_PER_L`.
3. Merge `mediadive.medium:J221` and `TOGO:M214` by exact JCM source identity after the stock recipes are represented consistently.
4. Regenerate merge YAML only after source normalization, then confirm that the final record has the base 960 ml water row plus three stock additions rather than three flattened stock ingredient sets.

## Follow-up Checks
After source normalization and merge regeneration, re-run schema, strict, reference, and term validation.

Run an exact duplicate search with ignored files included for `mediadive.medium:J221`, `TOGO:M214`, and `jcm_grmd?GRMD=221` and confirm that JCM 221 regenerates as one canonical record.

## Additional Notes
Exact duplicate-source searches included ignored files.
