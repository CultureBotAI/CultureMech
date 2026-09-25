# YAML Record Review: sedimentisphaera_l21_hs_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/sedimentisphaera_l21_hs_medium.yaml
- Started UTC: 2026-09-25T05:01:57Z
- Finished UTC: 2026-09-25T05:01:57Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:001003`, `sedimentisphaera_l21_hs_medium`, from `data/merge_yaml/merged/sedimentisphaera_l21_hs_medium.yaml`.

The target record is a generated merge of MediaDive/DSMZ 1527 `SEDIMENTISPHAERA (L21 HS) MEDIUM` with MediaDive/DSMZ 1526a `KIRITIMATIELLA (L21 LS) MEDIUM`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record's primary identity is DSMZ Medium 1527, but `merged_from` also contains `kiritimatiella_l21_ls_medium`.

DSMZ 1527 and DSMZ 1526a are concentration variants and should not have been collapsed into one generated base record.

The merged output is especially inconsistent because it keeps the Sedimentisphaera L21 HS label while carrying lower-salt Kiritimatiella L21 LS NaCl, cysteine, and sulfide concentrations.

## Evidence

DSMZ 1527 lists 120 g NaCl, 0.30 g L-Cysteine HCl x H2O, 0.30 g Na2S x 9H2O, 10 ml Modified Wolin's mineral solution, 1 ml Wolin's vitamin solution (10x), and 1000 ml Distilled water, with pH 7.5.

The MediaDive 1527 API scales 120 g NaCl to 118.694 g/L in its 1011 ml main solution and then adds the 1 g/L NaCl from Modified Wolin's mineral solution when the stock is flattened, producing the expected high-salt merged artifact value of 119.694 g/L.

The normalized Kiritimatiella L21 LS source explicitly records Sedimentisphaera L21 HS as a concentration-variant child that raises NaCl from 60.3472 g/L to 119.694 g/L and lowers cysteine and sulfide from 0.49456 g/L to 0.296736 g/L.

## Completeness

The generated target still has the low-salt 60.3472 g/L NaCl and 0.49456 g/L cysteine/sulfide values.

The target flattens Modified Wolin's mineral solution and Wolin's vitamin solution into the parent ingredient list at stock strength.

NaCl and CaCl2 from Modified Wolin's mineral solution are summed with parent NaCl and CaCl2, hiding the stock boundary.

The 1000 ml Distilled water row is absent.

N2 and CO2 are present only in preparation prose, not as structured gas ingredients.

The Modified Wolin's mineral solution pH preparation note is attached to the parent recipe.

## Findings

The merge collapsed the DSMZ 1526a and DSMZ 1527 concentration variants into one record instead of preserving separate generated base records linked by a variant relationship.

The record labeled as `SEDIMENTISPHAERA (L21 HS) MEDIUM` carries low-salt Kiritimatiella values for the defining NaCl, cysteine, and sulfide axes.

The MediaDive import flattened linked stock solution ingredients into the final medium and summed duplicate NaCl/CaCl2 rows across parent and stock scopes.

The generated parent is missing water and has a stock-specific pH step.

## Recommended Edits

Keep DSMZ 1526a and DSMZ 1527 as separate normalized base records with an explicit concentration-variant relationship instead of merging them into one final YAML.

Repair the direct MediaDive/DSMZ 1527 source so the parent uses the high-salt NaCl, cysteine, and sulfide values from DSMZ 1527.

Move Modified Wolin's mineral solution and Wolin's vitamin solution into nested stock scopes with their source addition volumes.

Restore the 1000 ml Distilled water row and consider adding structured N2 and CO2 gas ingredients.

Regenerate the merge layer after the DSMZ 1526a and DSMZ 1527 normalized sources are repaired.

## Follow-up Checks

Confirm the regenerated `sedimentisphaera_l21_hs_medium` record has NaCl near 119.694 g/L and cysteine/sulfide near 0.296736 g/L if the importer continues to scale by MediaDive's 1011 ml final volume.

Confirm the regenerated Sedimentisphaera record no longer lists `kiritimatiella_l21_ls_medium` in `merged_from`.

Confirm the regenerated parent has no direct stock-strength rows such as 1.5 g/L Nitrilotriacetic acid or 0.02 g/L Biotin.

Confirm the generated parent has no preparation step that starts with `First dissolve nitrilotriacetic acid`.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
