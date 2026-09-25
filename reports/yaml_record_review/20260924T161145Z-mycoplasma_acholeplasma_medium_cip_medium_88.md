# YAML Record Review: mycoplasma_acholeplasma_medium_cip_medium_88

- Repository: CultureMech
- Record: data/merge_yaml/merged/mycoplasma_acholeplasma_medium_cip_medium_88.yaml
- Started UTC: 2026-09-24T16:10:50Z
- Finished UTC: 2026-09-24T16:11:45Z
- Verdict: needs curation

## Target

Reviewed the generated MediaRecipe `CultureMech:000513` for
`mycoplasma_acholeplasma_medium_cip_medium_88`, a single-source DSMZ record
grounded to `mediadive.medium:1079`.

## Validation

Focused validation passed:

- LinkML `MediaRecipe` validation: passed; no issues found.
- Strict validation: passed with zero error rows in `/private/tmp/mycoplasma_acholeplasma_medium_cip_medium_88.strict.tsv`.
- Reference validation: passed with 0 checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in generated YAML.

## Identity and Grounding

The owner identity is direct and unambiguous: MediaDive medium 1079 is DSMZ
`MYCOPLASMA/ACHOLEPLASMA MEDIUM (CIP MEDIUM 88)`, and the generated record is a
single-source merge from the corresponding normalized DSMZ owner.

An exact ignored-inclusive search across `data/normalized_yaml`,
`data/merge_yaml/merged`, and top-level `data/*.tsv` files found this owner,
its generated YAML, and its MediaDive indexes; it did not find another active
recipe carrying `mediadive.medium:1079`.

## Evidence

MediaDive 1079 defines a 1000 ml main solution with:

- 17 g PPLO broth
- 100 ml 25% yeast extract stock, pH 7.0, autoclaved
- 20 ml 1% phenol red stock, pH 7.0, autoclaved
- 670 ml distilled water
- 210 ml sterile supplement

The 210 ml sterile supplement contains:

- 10 ml 50% glucose
- 200 ml horse serum
- 1 g ampicillin

DSMZ also gives pH 7.4-7.8. Its main-solution step says to add all components
except sterile supplement, adjust pH to 7.6 + 0.2, autoclave at 121 C for 15
minutes, and aseptically add sterile supplement. The sterile-supplement step
says to adjust pH to 7.0 + 0.2 and autoclave at 121 C for 15 minutes.

## Completeness

The generated record preserves the base DSMZ identity, pH range, six
non-water/non-solution ingredients, and both free-text preparation steps. It is
not complete as a recipe graph because it drops the 670 ml water row, drops the
210 ml sterile-supplement addition from the main solution, and flattens every
sterile-supplement ingredient into a top-level final-medium ingredient.

The flattened top-level quantities are a mixture of final and local stock
concentrations. `Glucose` is 5 g/L after 10 ml of 50% glucose stock is added to
the 1 L main solution, but `Ampicillin` is 4.7619 g/L in the 210 ml sterile
supplement, not in the final 1 L medium. `Horse serum` is a 200 ml liquid
addition to the 210 ml supplement but is modeled as `200 G_PER_L`.

## Findings

1. The main-solution `Distilled water` row is missing. DSMZ lists 670 ml of
   distilled water in `Main sol. 1079`.

2. The `Sterile supplement` row is missing as a nested 210 ml addition to the
   main solution. Its children were flattened into independent top-level
   ingredients.

3. `Ampicillin` has a stock-local concentration, `4.7619 G_PER_L`, as if 1 g
   were dissolved in the 210 ml supplement. In the final 1 L medium, that
   1 g supplement dose is not 4.7619 g/L.

4. `Horse serum` was converted from a 200 ml supplement ingredient to
   `200 G_PER_L`.

5. The Yeast extract, Phenol red, and Glucose rows no longer record their
   source stock percentages or stock volumes.

## Recommended Edits

Repair the normalized DSMZ owner before regenerating the merged recipe:

- Represent `Distilled water`, 670 ml, in the 1000 ml main solution.
- Represent `Sterile supplement`, 210 ml, as a nested main-solution addition
  with its own 210 ml recipe.
- Keep 200 ml `Horse serum` as a liquid addition inside that supplement.
- Keep `Ampicillin` as 1 g in the 210 ml supplement, not as a final 4.7619 g/L
  main-medium concentration.
- Preserve the source stock context for 100 ml of 25% yeast extract, 20 ml of
  1% phenol red, and 10 ml of 50% glucose.

## Follow-up Checks

- Regenerate the merged YAML and confirm DSMZ 1079 retains the main solution
  and sterile supplement as distinct layers.
- Re-run LinkML, strict, reference, and term validation on the regenerated
  record.
- Compare the regenerated ingredient tree against MediaDive medium 1079 to
  ensure the 670 ml water row and 210 ml supplement row are present.

## Additional Notes

None found.
