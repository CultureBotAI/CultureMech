# YAML Record Review: salinivibrio_sharmensis_medium__04c2c5de

- Repository: CultureMech
- Record: data/merge_yaml/merged/salinivibrio_sharmensis_medium__04c2c5de.yaml
- Started UTC: 2026-09-25T03:52:23Z
- Finished UTC: 2026-09-25T03:52:23Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:007542`, `salinivibrio_sharmensis_medium`, from `data/merge_yaml/merged/salinivibrio_sharmensis_medium__04c2c5de.yaml`.

The record is a single-source TOGO M1028 import with JCM_M975-2 listed as TOGO's original source.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to TOGO M1028, `Salinivibrio Sharmensis Medium`, and the preserved JCM_M975-2 / JCM 975 source URL.

The live JCM 975 page confirms this is `SALINIVIBRIO SHARMENSIS MEDIUM`.

## Evidence

JCM 975 lists 100 g NaCl, 3 g trisodium citrate, 1 g MgSO4 x 7 H2O, 2 g KCl, 0.36 mg MnCl2 x 4 H2O, 0.05 g FeSO4 x 7 H2O, and 10 g yeast extract in the base medium, then instructs bringing the volume to 970 ml with distilled water.

JCM 975 says to add 20 g/L agar for solid medium, autoclave and cool to 50 - 60C for agar medium, add 30 ml of separately autoclaved 10% w/v Na2CO3 solution, and check that the final pH is around 9.0.

TOGO M1028 preserves the same final pH, ingredients, 970 ml water volume, 30 ml Na2CO3 stock, and preparation comments.

## Completeness

The base ingredients, agar, and 970 ml distilled-water row are present.

The pH 9.0 value and preparation comments are missing from the structured generated recipe, and the 10% w/v Na2CO3 solution appears as an empty `Unknown solution` with a `30 G_PER_L` concentration instead of a stock composition and 30 ml aliquot.

## Findings

`MnCl2 x 4 H2O` is 1000x too high: JCM and TOGO specify 0.36 mg, while the generated row is 0.36 g/L.

The 30 ml post-autoclave 10% w/v Na2CO3 aliquot is not modeled correctly. It should either be represented as a 10% stock added at 30 ml/L or as the corresponding 3 g/L final Na2CO3 contribution.

The generated record drops the source pH 9.0 and the preparation instructions for 970 ml make-up water, agar handling, cooling, separate Na2CO3 autoclaving, and final pH checking.

The 970 ml distilled-water source row is represented as `970 G_PER_L`, which preserves the row but not the source volume unit.

## Recommended Edits

Repair the TOGO M1028 normalized file so `MnCl2 x 4 H2O` is `0.00036 G_PER_L` if flattened, or 0.36 mg before final unit conversion.

Model the 10% w/v Na2CO3 solution as a separate stock with a 30 ml aliquot added after autoclaving.

Add the pH 9.0 target and preparation steps from TOGO/JCM before regenerating the merged YAML.

## Follow-up Checks

After regeneration, confirm the record has no `Unknown solution`, the manganese row is no longer 0.36 g/L, and the Na2CO3 addition remains traceable to the 30 ml 10% w/v stock.

Validate the regenerated record with schema, strict, reference, and term validation.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
