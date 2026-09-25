# YAML Record Review: HALANAEROBIUM HYDROGENIFORMANS MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/halanaerobium_hydrogeniformans_medium__4da99b2d.yaml
- Started UTC: 2026-09-23T08:43:25Z
- Finished UTC: 2026-09-23T08:44:27Z
- Verdict: needs curation

## Target

- Reviewed generated YAML for `HALANAEROBIUM HYDROGENIFORMANS MEDIUM`.
- Stable ID: `CultureMech:002377`.
- Primary source in generated record: direct JCM/MediaDive `mediadive.medium:J1209`.
- Merge fingerprint: `4da99b2dd10f8cac2a0991c9f6ee108afc02c46c0a8890646a1dbccfc5d6f1bd`.

## Validation

- LinkML validation against `src/culturemech/schema/culturemech.yaml`, target class `MediaRecipe`: pass.
- Strict validation with `scripts/validate_strict.py`: pass, 0 error rows in `/private/tmp/halanaerobium_hydrogeniformans_medium_4da99b2d.strict.tsv`.
- LinkML reference validation: pass, 0 checked references.
- LinkML term validation with `conf/oak_config.yaml`: pass.
- Embedded `curation_history`: Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

- The generated record is the direct JCM/MediaDive import for JCM medium 1209.
- An exact `rg --no-ignore --hidden` search for `JCM_M1209`, `GRMD=1209`, and `mediadive.medium:J1209` found the direct JCM/MediaDive source plus a source-equivalent Togo `M1296` / `JCM_M1209` import in `data/merge_yaml` and `data/normalized_yaml`.
- The direct MediaDive import and the Togo import remain split into two generated records even though both point to the same live JCM recipe.

## Evidence

- The live JCM `GRMD=1209` recipe defines Solution A as 70 g NaCl, 40 g Na2CO3, and 500 ml water; Solution B as 6.3 g K2HPO4, 10 ml basal salts solution, 10 ml trace minerals from JCM medium 151, and 380 ml water.
- JCM then instructs autoclaving Solution A and Solution B separately under N2, combining them, adding 10 ml of 10 percent yeast extract solution and 100 ml of 25 percent glycerin solution, distributing anaerobically under N2, and finally adding per liter 12 ml of 5 percent L-cysteine HCl x H2O solution and 15 ml of 5 percent Na2S x 9 H2O solution.
- The generated direct MediaDive record omits the JCM 100 ml glycerin-solution addition, represents 10 percent yeast extract, 5 percent L-cysteine, and 5 percent Na2S stocks as 10 g/L top-level ingredients, and uses MediaDive's 10 ml volumes for both reducer stocks instead of JCM's 12 ml and 15 ml final additions.
- Basal salts and trace-minerals rows are flattened at their stock concentrations, then duplicate NaCl, MnSO4 x n H2O, CaCl2 x 2 H2O, and FeSO4 x 7 H2O rows are summed across unrelated solution contexts.
- The Togo `M1296` import is not a clean replacement: it preserves the JCM glycerin solution as a child solution, but imports basal-salts milligram rows as gram-per-liter top-level ingredients and models N2 gas as a variable chemical ingredient.

## Completeness

- The 100 ml 25 percent glycerin addition from the JCM recipe is missing from the generated direct JCM/MediaDive record.
- Solution structure is only partly represented: `Basal salts solution` appears as a separate solution reference, but its composition and the trace-minerals stock are also flattened into top-level ingredients.
- The direct generated record has no final pH value; none was provided by the JCM page or MediaDive REST medium metadata.
- `Yeast extract` is ungrounded, and `MnSO4 x n H2O` lacks a MediaIngredientMech ChEBI link.

## Findings

- Major: Required JCM glycerin solution is absent.
- Major: Basal salts and trace-minerals stocks are flattened at stock strength rather than being kept as 10 ml stock additions or converted to final concentrations.
- Major: Reducing-agent stock additions are misrepresented as 10 g/L each and lose JCM's distinct 12 ml L-cysteine and 15 ml Na2S addition volumes.
- Major: Duplicate-ingredient cleanup summed salts across separate basal and trace-mineral contexts.
- Minor: The direct JCM/MediaDive import remains split from the source-equivalent Togo `M1296` record.

## Recommended Edits

- Recurate JCM 1209 as a staged anaerobic recipe with Solution A, Solution B, the 10 percent yeast extract addition, the 25 percent glycerin addition, and the per-liter cysteine and sulfide additions.
- Stop flattening basal salts and trace-minerals stock compositions into the top-level medium unless their stock aliquots are converted to final concentrations.
- Stop summing same-named salts across nested solution contexts.
- Add source-equivalence handling so direct `mediadive.medium:J1209` and `TOGO:M1296` / `JCM_M1209` merge into one generated record after both source imports are corrected.

## Follow-up Checks

- After recuration, verify that the generated record includes the 25 percent glycerin stock, keeps the 12 ml and 15 ml reducer additions distinct, and has no `Merged 2 duplicates` ingredient notes.

## Additional Notes

- None found.
