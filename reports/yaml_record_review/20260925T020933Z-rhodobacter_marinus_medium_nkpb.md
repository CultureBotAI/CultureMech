# YAML Record Review: rhodobacter_marinus_medium_nkpb

- Repository: CultureMech
- Record: `data/merge_yaml/merged/rhodobacter_marinus_medium_nkpb.yaml`
- Started UTC: 2026-09-25T02:08:07Z
- Finished UTC: 2026-09-25T02:09:33Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:001141` for DSMZ Medium 1659 / `mediadive.medium:1659`, generated from `data/normalized_yaml/bacterial/rhodobacter_marinus_medium_nkpb.yaml`.

## Validation

- Open schema validation: passed with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

DSMZ Medium 1659 and MediaDive 1659 both identify this target as `RHODOBACTER MARINUS MEDIUM (NKPB)`. Exact ignored-inclusive searches for `mediadive.medium:1659` and `DSMZ_Medium1659` found the source ID/PDF URL only in the direct owner, this generated target, and the manifest row among the searched data paths.

## Evidence

DSMZ 1659 and MediaDive 1659 list the main medium as KH2PO4 0.60 g/L, K2HPO4 0.90 g/L, MgSO4 x 7H2O 0.20 g/L, FeSO4 x 7H2O 12 mg/L, Na2EDTA 20 mg/L, NH4Cl 1.25 g/L, NaCl 15 g/L, CaCl2 x 2H2O 75 mg/L, DL-malate 6 g/L, yeast extract 0.50 g/L, peptone 0.50 g/L, trace elements 1 ml/L, biotin 15 ug/L, and distilled water 1000 ml/L, with pH adjusted to 7.6 using NaOH. The trace-elements stock itself contains H3BO3 2.80 g, MnSO4 x H2O 2.10 g, Na2MoO4 x 2H2O 0.75 g, ZnSO4 x 7H2O 0.24 g, Cu(NO3)2 x 3H2O 0.04 g, and 1000 ml distilled water.

## Completeness

The generated target carries the pH and all scalar main-medium non-water amounts, but it omits the final water row and flattens the trace-elements stock into the final recipe.

## Findings

- The required `Trace elements` stock is missing as a 1 ml/L final-medium ingredient. Its five stock components are instead emitted as top-level final-medium ingredients at their stock concentrations, which overstates them 1000-fold relative to using 1 ml stock per liter.
- The main-medium `Distilled water` row of 1000 ml/L is missing entirely.
- The trace-elements stock has no nested representation, so its own 1000 ml distilled-water solvent is also missing.
- The `DL-Malate` row still carries legacy `mediaingredientmech_term: MediaIngredientMech:000619` despite having a CHEBI primary term and a June history note claiming legacy links were replaced.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/rhodobacter_marinus_medium_nkpb.yaml` so the main recipe has a 1 ml/L `Trace elements` stock row and 1000 ml/L distilled water.
- Move H3BO3, MnSO4 x H2O, Na2MoO4 x 2H2O, ZnSO4 x 7H2O, Cu(NO3)2 x 3H2O, and stock water into the `Trace elements` stock recipe instead of the final ingredient list.
- Replace the legacy DL-malate MediaIngredientMech field with a CHEBI-keyed field where available.
- Add a direct DSMZ reference and repair history, then regenerate `data/merge_yaml/merged`.

## Follow-up Checks

- Confirm the regenerated final medium has trace elements 1 ml/L and not the five trace-stock salts as top-level final ingredients.
- Confirm the regenerated target includes 1000 ml/L distilled water.
- Re-run open schema, strict, reference, and term validation for the regenerated target.

## Additional Notes

The main-medium mg and ug rows were normalized correctly: 12 mg/L FeSO4 x 7H2O, 20 mg/L Na2EDTA, 75 mg/L CaCl2 x 2H2O, and 15 ug/L biotin.
