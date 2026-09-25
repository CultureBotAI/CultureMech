# YAML Record Review: rhodobacter_thiocapsa_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rhodobacter_thiocapsa_medium.yaml`
- Started UTC: 2026-09-25T02:08:55Z
- Finished UTC: 2026-09-25T02:11:45Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:003935` for KOMODO Medium 1197 / `komodo.medium:1197`, merged from the KOMODO base record, two KOMODO strain-specific records, and the direct DSMZ Medium 1197 owner.

## Validation

- Open schema validation: passed with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

KOMODO 1197 explicitly cites DSMZ Medium 1197, and an exact ignored-inclusive rerun using YAML-line and TSV-field patterns isolated `komodo.medium:1197` from the neighboring `komodo.medium:1197.1` and `.2` strain-variant IDs. The source-duplicate link to the direct `mediadive.medium:1197` owner is valid at the base-medium level.

## Evidence

DSMZ Medium 1197 and MediaDive 1197 list the main medium as 0.4 g/L yeast extract, 3.0 g/L sodium pyruvate, 0.5 g/L KH2PO4, 0.5 g/L MgCl2 x 6H2O, 0.4 g/L NaCl, 0.6 g/L NH4Cl, 0.05 g/L CaCl2 x 2H2O, 1 ml/L vitamin B12 stock at 2 mg/L, 1 ml/L Trace element solution SL7, and 1000 ml/L distilled water, with pH 7.2 and N2 gassing. The SL7 stock itself contains 1 ml 25% HCl, 70 mg ZnCl2, 100 mg MnCl2 x 4H2O, 60 mg H3BO3, 200 mg CoCl2 x 6H2O, 20 mg CuCl2 x 2H2O, 20 mg NiCl2 x 6H2O, 40 mg Na2MoO4 x 2H2O, and 1000 ml distilled water per liter of stock. DSMZ also lists strain-specific modifications for DSM 18774 and DSM 19780 below the base recipe.

## Completeness

The generated target emits 16 gram-per-liter ingredients, but the source base medium has 10 final-medium rows; vitamin B12 and SL7 are stock additions, not final gram-per-liter salts.

## Findings

- `Vitamin B12` is represented as `1 G_PER_L`, but DSMZ 1197 lists 1 ml/L of a 2 mg/L filter-sterilized vitamin B12 stock.
- `HCl`, `ZnCl2`, `MnCl2 x 4 H2O`, `H3BO3`, `CoCl2 x 6 H2O`, `CuCl2 x 2 H2O`, `NiCl2 x 6 H2O`, and `Na2MoO4 x 2 H2O` are emitted as top-level final-medium ingredients at their SL7 stock concentrations. The final medium should contain 1 ml/L of the SL7 stock, with these components nested under that stock.
- The required 1000 ml/L `Distilled water` row from the DSMZ 1197 main medium is missing.
- The generated variant topology is stale relative to `data/normalized_yaml/bacterial/KOMODO_1197_RHODOBACTER_THIOCAPSA_medium.yaml`: `for_dsm_18774` and `for_dsm_19780` now have `STRAIN_SPECIFIC_VARIANT` relationships, but the generated target still marks them as source duplicates and merges them into the base.

## Recommended Edits

- Repair both the KOMODO 1197 owner and the direct `rhodobacter_thiocapsa_medium.yaml` owner so the main recipe has 1 ml/L vitamin B12 stock, 1 ml/L Trace element solution SL7, and 1000 ml/L distilled water.
- Move the SL7 components and stock water into a nested stock recipe.
- Regenerate `data/merge_yaml/merged` so 1197.1 and 1197.2 are emitted as strain-specific variants rather than duplicate synonyms.

## Follow-up Checks

- Confirm the regenerated base medium has the DSMZ 1197 ten-row final recipe, not 16 flattened stock components.
- Confirm `for_dsm_18774` and `for_dsm_19780` are no longer merged into the base as source duplicates.
- Re-run open schema, strict, reference, and term validation for the regenerated base and variant targets.

## Additional Notes

The source-duplicate relationship between KOMODO 1197 and the direct DSMZ 1197 owner is valid; the stock topology within those owners is not.
