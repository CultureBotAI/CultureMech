# YAML Record Review: THERMOANAEROBACTER BROCKII MEDIUM
- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoanaerobacter_brockii_medium__4caf5a5c.yaml`
- Started UTC: `2026-09-25T09:34:37Z`
- Finished UTC: `2026-09-25T09:35:59Z`
- Verdict: needs curation

## Target
Generated MediaDive bacterial recipe `CultureMech:000913`, `thermoanaerobacter_brockii_medium`, with medium term `mediadive.medium:144` and label `THERMOANAEROBACTER BROCKII MEDIUM`.

It is a single-source merge of normalized source `thermoanaerobacter_brockii_medium`, on merge fingerprint `4caf5a5cbd2ad9204af533dab37ca447bbd9f909fbf4a3b4924977bbcdeffc16`.

## Validation
- LinkML schema validation: passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation: passed; `scripts/validate_strict.py` scanned 1 file with 0 files containing errors and 0 total error rows.
- Reference validation: passed; `linkml-reference-validator` checked 1 file and reported all checked references passed.
- Term validation: passed; `linkml-term-validator` reported `Validation passed`.
- Embedded `curation_history`: Not checked. The available history validator targets standalone `history/` entries rather than `MediaRecipe.curation_history` embedded in generated YAML.

## Identity and Grounding
The record is correctly grounded to MediaDive/DSMZ Medium 144, `THERMOANAEROBACTER BROCKII MEDIUM`.

The same DSMZ 144 PDF is also represented by TOGO source records `TOGO:M2729` and `TOGO:M2731`. At least `TOGO:M2729` is emitted as a separate generated duplicate, `data/merge_yaml/merged/THERMOANAEROBACTER_BROCKII_MEDIUM.yaml`, instead of merging with the MediaDive branch.

Reviewed ingredient-level CHEBI groundings are internally consistent on this generated branch; no stale generic hydrate grounding like the DSMZ 671 MgSO4 issue was found in the flattened list.

## Evidence
DSMZ Medium 144 and MediaDive medium 144 give one main solution containing NH4Cl, NaCl, MgCl2 x 6 H2O, KH2PO4, K2HPO4, 9 ml Trace element solution, 3 ml 0.1% FeSO4 x 7 H2O in 0.1 N H2SO4, yeast extract, trypticase peptone, 0.5 ml 0.1% sodium resazurin, 5 ml Wolin's vitamin solution, D-glucose, Na2S x 9 H2O, and distilled water.

The generated record flattened Trace element solution into top-level ingredient rows at the stock solution concentrations: `Nitrilotriacetic acid` at `12.8 G_PER_L`, `FeCl2 x 4 H2O` at `0.2 G_PER_L`, `MnCl2 x 4 H2O` at `0.1 G_PER_L`, `CoCl2 x 6 H2O` at `0.17 G_PER_L`, and the remaining trace components as direct final ingredients.

The stock `NaCl` row was merged with the true main-solution `NaCl`, raising final `NaCl` from `0.9 G_PER_L` plus a 9 ml stock contribution to `1.9 G_PER_L`.

Wolin's vitamin solution is added at 5 ml/L in DSMZ 144, but the generated record promotes its 1 L stock recipe into direct gram-per-liter rows such as `Biotin` at `0.002 G_PER_L`, `Pyridoxine hydrochloride` at `0.01 G_PER_L`, and `Vitamin B12` at `0.0001 G_PER_L`.

## Completeness
The MediaDive branch preserves the main DSMZ preparation step and the trace element stock pH adjustment step.

It omits two strain-specific DSMZ notes: DSM 3532 requires 10% NaCl under anaerobic conditions, and DSM 12299 omits D-glucose. These should be modeled as strain-specific notes or variants during source normalization.

## Findings
1. Needs curation: Trace element solution and Wolin's vitamin solution were flattened into direct top-level ingredients, so their internal stock concentrations are represented as final medium concentrations.
2. Needs curation: the stock `NaCl` and main-solution `NaCl` rows were merged, which changes the final NaCl concentration and hides the nested trace solution.
3. Needs curation: TOGO records for the same DSMZ 144 PDF remain unmerged from the MediaDive DSMZ 144 source identity.
4. Minor issue: the generated record is missing DSMZ strain-specific notes for DSM 3532 and DSM 12299.

## Recommended Edits
1. Normalize the MediaDive and TOGO DSMZ 144 source records, not the generated merge file, so the main recipe contains 9 ml/L Trace element solution and 5 ml/L Wolin's vitamin solution rather than the flattened contents of those stocks.
2. Preserve the 3 ml addition of FeSO4 x 7 H2O in 0.1 N H2SO4 as a stock addition or as a distinct annotated ingredient instead of conflating it with the trace stock.
3. Add exact source-identity merge handling so `mediadive.medium:144`, `TOGO:M2729`, and `TOGO:M2731` regenerate as one canonical DSMZ 144 record.
4. Retain the DSM 3532 and DSM 12299 strain-specific instructions in notes or variant metadata.

## Follow-up Checks
After source normalization and merge regeneration, re-run schema, strict, reference, and term validation.

Run an exact duplicate search with ignored files included for `mediadive.medium:144`, `TOGO:M2729`, `TOGO:M2731`, and `DSMZ_Medium144.pdf` and confirm that only the normalized inputs and one generated DSMZ 144 output remain.

## Additional Notes
Exact duplicate-source searches included ignored files. An initial `DSMZ_Medium144` prefix search was discarded because it also matched unrelated DSMZ 1440, 144a, 144b, and other neighboring medium numbers.
