# YAML Record Review: carboxydothermus_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/carboxydothermus_medium__2bd5ee0c.yaml
- Started UTC: 2026-09-22T03:49:00Z
- Finished UTC: 2026-09-22T03:53:22Z
- Verdict: needs curation

## Target

- Reviewed generated `MediaRecipe` `CultureMech:001639`, `carboxydothermus_medium`, in `data/merge_yaml/merged/carboxydothermus_medium__2bd5ee0c.yaml`.
- The record is generated from one maintained normalized owner, `data/normalized_yaml/bacterial/carboxydothermus_medium.yaml`, by the `2026-08-06` `merge_recipes.py` event on `merge_fingerprint: 2bd5ee0c6b66cd96df8371f0b78c019e035a55ad0acb89dee2cf490f63c7a679`.
- The asserted source identity is DSMZ/MediaDive Medium 507, `mediadive.medium:507`, `CARBOXYDOTHERMUS MEDIUM`, with the DSMZ PDF URL in `notes`.
- The record is a bacterial, liquid, semi-defined medium with pH range 6.8-7.0 and no explicit `target_organisms`, `growth_metrics`, evidence objects, or strain variants.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/carboxydothermus_medium__2bd5ee0c.yaml` | Passed: `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/carboxydothermus_medium__2bd5ee0c.yaml --out /private/tmp/carboxydothermus_medium__2bd5ee0c.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 total error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/carboxydothermus_medium__2bd5ee0c.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 1 file, 0 reference checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/carboxydothermus_medium__2bd5ee0c.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` | Not checked: `just validate-history` validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries. |

## Identity and Grounding

- DSMZ Medium 507 and the live MediaDive JSON identify medium `507` as `CARBOXYDOTHERMUS MEDIUM`; this agrees with `media_term.id`, `media_term.label`, `original_name`, the normalized owner name, and the import history note `Source: DSMZ, ID: 507`.
- `CultureMech:001639` resolves to `data/normalized_yaml/bacterial/carboxydothermus_medium.yaml` in `data/culturemech_id_registry.tsv`, `data/culturemech_recipe_catalog.tsv`, `data/normalized_yaml/recipe_index.json`, and `data/normalized_yaml/by_source_mediadive_index.json`.
- A gitignore-independent `rg --no-ignore --hidden` search for `CultureMech:001639`, `mediadive.medium:507`, `DSMZ_Medium507`, and the generated merge stem covered hidden and ignored files and found this ID's active normalized owner plus generated indexes, catalogs, reports, and downstream artifacts. I did not find a second active owner for `CultureMech:001639`.
- Most chemical groundings preserve the supplied hydrate state. The exception is `NiCl2 x 6 H2O`, which is grounded to anhydrous `CHEBI:34887` / `nickel dichloride` even though the supplied compound is nickel chloride hexahydrate; the packaged MIM label index includes the hydrate-specific `CHEBI:53542` identity.
- `Calcium D-(+)-pantothenate` is grounded to `CHEBI:31345`, but this row lacks the `mediaingredientmech_chebi_term` mirror that the MIM snapshot can provide for the exact label.

## Evidence

- The DSMZ PDF and MediaDive medium JSON support the main solution's direct compounds and amounts: KCl 0.33 g, MgCl2 x 6 H2O 0.52 g, CaCl2 x 2 H2O 0.29 g, NH4Cl 0.33 g, KH2PO4 0.33 g, 0.5 ml Sodium resazurin 0.1% w/v, NaHCO3 1 g, Yeast extract 0.05 g, and Distilled water 1000 ml.
- The same two sources support three stock additions to the main solution: 1 ml Trace element solution SL-11, 1 ml Wolin's vitamin solution (10x), and 20 ml Neutralized sulfide solution 3% w/v.
- The inspected sources do not support storing the SL-11 trace metals, Wolin vitamins, or sulfide-stock Na2S at stock strength as direct `ingredients` of the final medium. The direct record carries Na2-EDTA at `5.2 G_PER_L`, Biotin at `0.02 G_PER_L`, and Na2S x 9 H2O at `30 G_PER_L`, while MediaDive's final-composition endpoint calculates these at `0.00508806`, `0.0000195695`, and `0.587084 G_PER_L`, respectively.
- Preparation step 1 and the carbon monoxide pressurization step are supported by the main DSMZ recipe. Steps 3 and 4 are stock-solution preparation instructions for SL-11 and neutralized sulfide; they are source-backed text but attached to the wrong preparation boundary after stock flattening.

## Completeness

- The record is complete enough for source identity, pH, physical state, the import audit trail, and the main recipe's non-stock direct ingredients.
- The main medium is materially incomplete because `Distilled water 1000 ml` is absent and all three MediaDive stock additions are absent from `solutions`.
- Empty `target_organisms`, `growth_metrics`, and literature `references` are acceptable for this imported source recipe. DSMZ 507 is a formula source and does not itself report organism-specific growth evidence.
- The DSMZ 507 PDF includes DSM-strain modification notes for DSM 12326, DSM 19011, DSM 21830, DSM 22663, and DSM 23698; those are represented as neighboring normalized records and were not judged as part of this base `mediadive.medium:507` review.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The MediaDive importer flattened three stock solutions into final-medium direct ingredients and omitted the main `1000 ml` water row. | MediaDive 507 and the DSMZ PDF list SL-11, Wolin's vitamin solution, and neutralized sulfide as solution additions to the main recipe; the normalized owner instead has no `solutions` block and stores 20 non-water stock-composition rows directly under `ingredients` at stock concentrations. | `data/normalized_yaml/bacterial/carboxydothermus_medium.yaml`, or the MediaDive import transform if this pattern is source-owned and still reproducible. |
| major | Stock-solution preparation is attached to the medium rather than to its stock owners. | The EDTA/pH 6.0 instruction belongs to Trace element solution SL-11, and the N2/autoclave/pH 7 instruction belongs to Neutralized sulfide solution 3% w/v. In the reviewed record they appear as `preparation_steps` 3 and 4 after the main-medium autoclave and CO pressurization steps. | `data/normalized_yaml/bacterial/carboxydothermus_medium.yaml`, with stock-specific wording retained in `data/normalized_yaml/bacterial/mediadive_1474_Trace_element_solution_SL-11.yaml` and `data/normalized_yaml/bacterial/mediadive_34_Neutralized_sulfide_solution_3_w_v.yaml`. |
| minor | `NiCl2 x 6 H2O` is hydrate-specific in the source but points at an anhydrous nickel chloride term. | The source label includes six waters of hydration; the row uses `CHEBI:34887` / `nickel dichloride` rather than hydrate-specific `CHEBI:53542`. | The same normalized owner, or the upstream MediaDive compound-to-CHEBI resolver for compound 40. |
| minor | `Calcium D-(+)-pantothenate` is missing its CHEBI-keyed MediaIngredientMech mirror. | The ingredient has `term: CHEBI:31345` but no `mediaingredientmech_chebi_term`; the packaged `label_index.csv` maps the exact label to `CHEBI:31345` / `Calcium pantothenate`. | The same normalized owner, or the MIM enrichment backfill if this omission is importer-owned. |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/carboxydothermus_medium.yaml`, keep the eight direct main-recipe ingredients, add `Distilled water` as 1000 ml with a volume-appropriate unit, and remove the 20 trace/vitamin/sulfide rows that belong to stock recipes.
2. Add three `solutions` entries on the medium for `mediadive.solution:1474` Trace element solution SL-11 at 1 `ML_PER_L`, `mediadive.solution:5980` Wolin's vitamin solution (10x) at 1 `ML_PER_L`, and `mediadive.solution:34` Neutralized sulfide solution 3% (w/v) at 20 `ML_PER_L`.
3. Keep the main anoxic preparation and carbon monoxide pressurization instructions on the medium; leave the EDTA/FeCl2 order and neutralized-sulfide N2/autoclave instructions on the corresponding `SolutionRecipe` owners.
4. Replace the `NiCl2 x 6 H2O` row's primary and MIM CHEBI grounding with the hydrate-specific identity, or de-ground it if the resolver cannot yet safely emit `CHEBI:53542` for MediaDive compound 40.
5. Add a `mediaingredientmech_chebi_term` mirror for `Calcium D-(+)-pantothenate` once the direct row lives in the appropriate Wolin solution rather than the medium.
6. Append one focused `curation_history` event describing the stock-boundary reconstruction and ingredient grounding changes, then regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

- Rerun focused open-schema, strict, reference, and term validators against the normalized owner and its regenerated `data/merge_yaml/merged/carboxydothermus_medium__2bd5ee0c.yaml`.
- Rerun `just verify-merges` or the narrowest documented merge-freshness check to prove the regenerated merge reflects the normalized owner.
- Manually diff the regenerated record against DSMZ Medium 507 or MediaDive `/download/medium/507/json` to verify that main ingredients, the three stock additions, and stock-specific preparation boundaries are preserved.
- Re-check the rendered medium page after regeneration to ensure SL-11, Wolin's vitamin solution, and Neutralized sulfide solution render as stock links rather than overconcentrated final ingredients.

## Additional Notes

- MediaDive also exposes the final flattened composition at `/download/composition/507/json`; those final values confirm that the current stock rows are overconcentrated rather than pre-diluted.
- The existing normalized solution records for `mediadive.solution:1474`, `mediadive.solution:5980`, and `mediadive.solution:34` still need their imported water rows repaired from invalid `PERCENT_V_V` values to a volume representation. That is a related `SolutionRecipe` cleanup, not a reason to keep stock ingredients flattened in this `MediaRecipe`.
