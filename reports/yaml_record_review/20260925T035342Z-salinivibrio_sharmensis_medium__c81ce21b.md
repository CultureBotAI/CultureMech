# YAML Record Review: salinivibrio_sharmensis_medium__c81ce21b

- Repository: CultureMech
- Record: data/merge_yaml/merged/salinivibrio_sharmensis_medium__c81ce21b.yaml
- Started UTC: 2026-09-25T03:53:42Z
- Finished UTC: 2026-09-25T03:53:42Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:000927`, `salinivibrio_sharmensis_medium`, from `data/merge_yaml/merged/salinivibrio_sharmensis_medium__c81ce21b.yaml`.

The record is a single-source DSMZ/MediaDive 1461 import for `SALINIVIBRIO SHARMENSIS MEDIUM`.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to DSMZ Medium 1461.

The formulation is the same Salinivibrio sharmensis medium also represented by TOGO M1028 / JCM_M975-2, but the two generated records did not merge because the TOGO and DSMZ import paths made different stock-handling errors.

## Evidence

DSMZ Medium 1461 lists 100 g NaCl, 3 g Tri-Na citrate, 1 g MgSO4 x 7 H2O, 2 g KCl, 3 g Na2CO3, 1 ml of 0.36 g/L MnCl2 x 4 H2O stock, 1 ml of 50 g/L FeSO4 x 7 H2O stock, 10 g yeast extract, and 1000 ml distilled water.

The DSMZ source sets final pH to 9.0 and says Na2CO3 is added from a sterilized stock after the autoclaved medium has cooled; 20 g/L agar may be added for solid medium.

The MediaDive REST record preserves the MnCl2 and FeSO4 rows as 1 ml aliquots with stock-strength attributes.

## Completeness

The major salts, yeast extract, Na2CO3 final contribution, agar row, pH, and preparation text are present.

The distilled-water row is absent, and the MnCl2 and FeSO4 stock aliquots were not converted into their final gram-per-liter contributions.

## Findings

`MnCl2 x 4 H2O` is modeled as 1 g/L, but DSMZ specifies 1 ml/L of a 0.36 g/L stock. The final contribution is 0.00036 g/L.

`FeSO4 x 7 H2O` is modeled as 1 g/L, but DSMZ specifies 1 ml/L of a 50 g/L stock. The final contribution is 0.05 g/L.

The generated record is a duplicate split from the TOGO M1028 Salinivibrio sharmensis record. Both represent the same medium and should collapse after the TOGO milligram and Na2CO3 stock issues and this DSMZ stock-aliquot issue are repaired.

The 1000 ml distilled-water row from DSMZ is absent from the generated record.

## Recommended Edits

Represent the MnCl2 x 4 H2O and FeSO4 x 7 H2O rows as 1 ml/L stock aliquots or flatten them to 0.00036 g/L and 0.05 g/L respectively.

Preserve the DSMZ water and Na2CO3 stock-handling notes through normalization.

Regenerate the merge layer after repairing DSMZ 1461 and TOGO M1028 so the duplicate Salinivibrio sharmensis generated records can merge.

## Follow-up Checks

After regeneration, confirm the DSMZ-derived record has no 1 g/L MnCl2 or FeSO4 rows.

Confirm only one generated `salinivibrio_sharmensis_medium` record remains and that it retains DSMZ 1461 plus TOGO M1028 provenance.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
