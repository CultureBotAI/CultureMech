# YAML Record Review: DESULFOVIBRIO TUNISIENSIS MEDIUM

- Repository: CultureMech
- Record: `data/merge_yaml/merged/desulfovibrio_tunisiensis_medium__dd739510.yaml`
- Started UTC: 2026-09-22T21:04:06Z
- Finished UTC: 2026-09-22T21:04:06Z
- Verdict: needs curation

## Target

Reviewed generated merged record `CultureMech:003026` for `desulfovibrio_tunisiensis_medium`, a MediaDive import of JCM Medium J680.

## Validation

- Open LinkML validation: pass (`linkml-validate`, `MediaRecipe`, no issues found).
- Strict validation: pass (`scripts/validate_strict.py`, 0 error rows).
- Reference validation: pass (`linkml-reference-validator`, 0 checks).
- Term validation: pass (`linkml-term-validator`, labels enabled).
- Embedded `curation_history`: Not checked; the available history validator targets standalone files under `history/`.

## Identity and Grounding

The target is grounded to `mediadive.medium:J680`, `DESULFOVIBRIO TUNISIENSIS MEDIUM`, with JCM GRMD 680 in `notes`.

A gitignore-independent Tunisiensis lookup found this JCM J680 normalized source and a TOGO M699 companion that imports the same original JCM_M680 source. TOGO M699 currently generates separately as `data/merge_yaml/merged/DESULFOVIBRIO_TUNISIENSIS_MEDIUM.yaml`.

## Evidence

MediaDive J680 represents the main solution as 1000 ml water, basal salts, yeast extract, peptone, resazurin, 5 ml Trace minerals, 25 ml 8% NaHCO3, 10 ml L-Cysteine x HCl x H2O solution, and 8 ml 5% Na2S x 9 H2O.

Trace minerals is a separate 1000 ml stock with nitrilotriacetic acid, MgSO4 x 7 H2O, MnSO4 x n H2O, NaCl, FeSO4 x 7 H2O, CoSO4 x 7 H2O, CaCl2 x 2 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2, H3BO3, Na2MoO4 x 2 H2O, and water.

## Completeness

The target preserves the pH 7.2 and the broad JCM preparation text for boiling under N2, distributing under N2-CO2, autoclaving, and aseptically adding anaerobic stocks after autoclaving.

The composition is incomplete because the 5 ml Trace minerals stock was flattened into the top-level recipe, the 25 ml bicarbonate and 8 ml sulfide source-volume additions were copied as G/L ingredient rows, the 10 ml cysteine addition is an empty `Unknown solution` stub, and the water rows are absent.

## Findings

- High: The 5 ml Trace minerals addition was flattened. Trace stock ingredients are listed at 1000 ml stock strengths instead of inside a subordinate stock recipe.
- High: Trace stock NaCl and CaCl2 x 2 H2O were merged into the main NaCl and CaCl2 x 2 H2O rows, inflating those top-level rows with the stock-strength 1.0 and 0.1 G/L duplicate values.
- High: The 25 ml 8% NaHCO3 and 8 ml 5% Na2S x 9 H2O additions were copied as 25 and 8 G/L top-level ingredients.
- Medium: The 10 ml L-Cysteine x HCl x H2O solution addition is represented as an empty `Unknown solution` stub with a 10 G/L concentration.
- Medium: The 1000 ml main water row and 1000 ml Trace minerals water row are absent.
- Low: The Trace minerals preparation instruction was appended as a top-level preparation step instead of being scoped to the Trace minerals stock recipe.
- Medium: The exact TOGO M699 JCM_M680 companion remains split from the MediaDive J680 record.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/desulfovibrio_tunisiensis_medium.yaml` so JCM J680 has structured 5 ml Trace minerals, 25 ml 8% NaHCO3, 10 ml cysteine, and 8 ml 5% Na2S x 9 H2O additions.
- Move the Trace minerals recipe into a subordinate `solutions` entry with its 1000 ml water row and its pH 6.5-to-7.0 preparation note.
- Add the 1000 ml main water row and stop merging Trace minerals NaCl and CaCl2 x 2 H2O into the main solution.
- Repair `data/normalized_yaml/bacterial/TOGO_M699_Desulfovibrio_Tunisiensis_Medium.yaml` so it can reconcile with the curated JCM J680 import instead of generating as a split exact duplicate.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after normalized curation.
- Regenerate merged YAML and confirm the main J680 record contains source-volume additions for Trace minerals, bicarbonate, cysteine, and sulfide rather than copied stock strengths.
- Verify JCM M680 is no longer split across the MediaDive and TOGO generated records unless the two provider imports are deliberately retained as documented source duplicates.

## Additional Notes

None found.
