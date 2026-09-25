# YAML Record Review: selenomonas_ruminantium_medium__edc0c0c8

- Repository: CultureMech
- Record: data/merge_yaml/merged/selenomonas_ruminantium_medium__edc0c0c8.yaml
- Started UTC: 2026-09-25T05:09:34Z
- Finished UTC: 2026-09-25T05:09:34Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:009195`, `selenomonas_ruminantium_medium`, from `data/merge_yaml/merged/selenomonas_ruminantium_medium__edc0c0c8.yaml`.

The target record is a TOGO Medium M2638 import that cites DSMZ Medium 181 as its original source.

## Validation

The generated record passed open LinkML validation, strict validation, reference validation, and term validation.

Strict validation wrote only the TSV header, so it reported 0 strict rows.

Embedded `curation_history` was not checked because the repository history validator targets standalone `history/` files rather than `MediaRecipe.curation_history` entries in merged YAML.

## Identity and Grounding

The record is correctly grounded to TOGO Medium M2638 and DSMZ Medium 181.

The TOGO source is a same-source duplicate of the direct MediaDive DSMZ 181 / KOMODO Medium 181 generated record.

The `selenomonas_wg_medium` files found by exact name inspection are different records and were not treated as duplicates of DSMZ 181.

## Evidence

DSMZ Medium 181 and TOGO Medium M2638 list 1 g/L Glucose, 5 g/L Trypticase (BBL), 1 g/L KH2PO4, 4 g/L Na-acetate, 2 g/L Yeast extract, 0.1 ml/L n-Valeric acid, 1 mg/L Resazurin, 4 g/L Na2CO3, 0.5 g/L Cysteine-HCl x H2O, and 1000 ml/L Distilled water.

Both source views specify pH 7.0 and a 100% CO2 gas atmosphere.

## Completeness

The generated record has the expected 2 g/L Yeast extract, 1 g/L KH2PO4, 4 g/L Na-acetate, 4 g/L Na2CO3, 1 g/L Glucose, 5 g/L Trypticase (BBL), and 0.5 g/L Cysteine-HCl x H2O rows.

The generated record keeps the source CO2 atmosphere as a structured variable gas ingredient.

The TOGO 1000 ml Distilled water row is represented as 1000 g/L Distilled water.

The TOGO 1 mg Resazurin row is represented as 1 g/L Resazurin instead of 0.001 g/L.

The TOGO 0.1 ml n-Valeric acid row is represented as 0.1 g/L n-Valeric acid instead of 0.1 ml/L.

The TOGO and DSMZ pH 7.0 value is absent.

## Findings

Several source units were normalized incorrectly: ml water, mg Resazurin, and ml n-Valeric acid were all converted to `G_PER_L`.

The missing pH makes the TOGO-derived record less complete than its source.

The TOGO branch remains separate from the existing direct DSMZ/KOMODO DSMZ Medium 181 source duplicate because the source unit defects and structured CO2 row change its merge fingerprint.

## Recommended Edits

Repair `data/normalized_yaml/bacterial/TOGO_M2638_Selenomonas_Ruminantium_Medium.yaml` so Distilled water is 1000 ml/L, Resazurin is 0.001 g/L, and n-Valeric acid is 0.1 ml/L.

Add the pH 7.0 source value to the TOGO normalized source.

After the TOGO M2638 source is corrected, merge or suppress it as a source duplicate of the direct DSMZ Medium 181 record while preserving the explicit 100% CO2 gas atmosphere from TOGO.

Regenerate the merged YAML after the normalized source is repaired.

## Follow-up Checks

Confirm the regenerated TOGO M2638 record no longer has 1000 g/L Distilled water, 1 g/L Resazurin, or 0.1 g/L n-Valeric acid.

Confirm the corrected TOGO branch fingerprints as a same-source duplicate of DSMZ Medium 181 or has an explicit duplicate relationship to the DSMZ/KOMODO branch.

Confirm pH 7.0 and the 100% CO2 atmosphere remain visible after duplicate collapse.

## Additional Notes

Empty optional evidence and organism fields were not treated as defects in this generated record.
