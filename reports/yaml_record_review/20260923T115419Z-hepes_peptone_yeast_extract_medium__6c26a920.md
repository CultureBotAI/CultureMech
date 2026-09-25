# YAML Record Review: HEPES PEPTONE-YEAST EXTRACT MEDIUM
- Repository: CultureMech
- Record: data/merge_yaml/merged/hepes_peptone_yeast_extract_medium__6c26a920.yaml
- Started UTC: 2026-09-23T11:53:37Z
- Finished UTC: 2026-09-23T11:54:19Z
- Verdict: needs curation

## Target

Reviewed the generated direct JCM branch for JCM 764, `HEPES PEPTONE-YEAST EXTRACT MEDIUM`, at `data/merge_yaml/merged/hepes_peptone_yeast_extract_medium__6c26a920.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/hepes_peptone_yeast_extract_medium__6c26a920.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is grounded to `mediadive.medium:J764`, matching the JCM 764 recipe. It is a direct MediaDive import of the same JCM formulation that Togo M791 wraps in `data/merge_yaml/merged/hepes_peptone_yeast_extract_medium.yaml`.

## Evidence

JCM 764 lists a 1 L HEPES peptone-yeast extract base with 1 ml trace elements from JCM/Togo M631, 1 ml of 0.2% ferrous ammonium sulfate in 0.037% HCl, and 1 L distilled water. After pH 7.25 adjustment, autoclaving, and cooling, it adds 10 ml filter-sterilized trace vitamins from JCM/Togo M190. MediaDive expands the M631 trace-elements stock and the M190 trace-vitamins stock into separate solution recipes.

The generated record omits the 1 L distilled water, turns the 1 ml ferrous ammonium sulfate stock into `1 G_PER_L`, and moves all trace-elements and trace-vitamins stock ingredients into the top-level final medium at stock strength.

## Completeness

The direct branch preserves more of MediaDive's nested detail than the Togo branch, but it does so in the wrong scope. Stock-recipe ingredients appear as final-medium ingredients, stock-preparation text appears as a main-medium preparation step, and the source's post-autoclave addition of 10 ml trace vitamins is not tied to the vitamin stock rows.

## Findings

- The final medium is missing the 1 L distilled-water row.
- The 1 ml ferrous ammonium sulfate/HCl solution is represented as `1 G_PER_L`.
- The M631 trace-elements stock is added at 1 ml per final medium, but its ingredients are flattened at their stock g/L concentrations.
- The M190 trace-vitamins stock is added at 10 ml per final medium, but its ingredients are flattened at their stock g/L concentrations.
- `First dissolve EDTA x 2Na and adjust pH to 8.0 with KOH. Then add the minerals.` is a trace-elements stock-preparation instruction, not a top-level final-medium pH step.
- The direct JCM and Togo wrapper branches for JCM 764 remain split into separate generated records.

## Recommended Edits

- Curate the direct JCM normalized source to keep M631 and M190 as nested stock solutions or to convert their ingredients to final-medium concentrations after applying the 1 ml and 10 ml addition volumes.
- Restore the 1 L distilled-water row.
- Keep the 0.2% ferrous ammonium sulfate row as a 1 ml solution addition instead of a mass concentration.
- Scope the EDTA/KOH pH 8.0 preparation text to the trace-elements stock.
- Merge or alias the direct JCM 764 and Togo M791 branches after both are corrected.

## Follow-up Checks

- Confirm the regenerated final medium has no full-strength trace-element or trace-vitamin stock rows as top-level final-medium ingredients.
- Re-run open schema, strict, reference, and term validation after regeneration.

## Additional Notes

None.
