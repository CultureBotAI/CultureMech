# YAML Record Review: gbs_salts_medium_for_rhodothermus__063a13f7

- Repository: CultureMech
- Record: data/merge_yaml/merged/gbs_salts_medium_for_rhodothermus__063a13f7.yaml
- Started UTC: 2026-09-23T05:40:46Z
- Finished UTC: 2026-09-23T05:41:39Z
- Verdict: needs curation

## Target

Generated CultureMech:002432 is the direct MediaDive/JCM record for JCM J1266, "GBS SALTS MEDIUM FOR RHODOTHERMUS".

## Validation

`linkml-validate` passed against `MediaRecipe`.

`scripts/validate_strict.py` passed with 0 error rows.

`linkml-reference-validator` passed with 0 checks.

`linkml-term-validator` passed.

Embedded `curation_history` entries were not checked: the available history validator targets standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The direct MediaDive/JCM identity and `mediadive.medium:J1266` grounding are valid, but TOGO M1362 is another normalized import of the same JCM_M1266 source and was not merged into this generated record.

All expanded mineral-solution constituents have good primary CHEBI groundings, but the generated record should not expose them as final-medium ingredients at their stock concentrations.

Yeast extract and peptone are ungrounded undefined stock additives.

## Evidence

The live JCM GRMD 1266 URL currently returns "Nothing found", but both MediaDive J1266 and TOGO M1362 archive the same JCM_M1266 recipe.

The main recipe contains NaH2PO4, NaCl, NH4Cl, MgSO4 x 7H2O, CaCl2 x 2H2O, KCl, Na2SO4, 5 ml Mineral solution, 1 L distilled water, 10 ml 10% yeast extract, and 10 ml 10% peptone, then instructs adjustment to pH 7.5, autoclaving, and aseptic addition of the autoclaved solutions.

MediaDive preserves Mineral solution as a separate 1 L stock containing EDTA, FeSO4 x 7H2O, MnCl2 x 4H2O, ZnSO4 x 7H2O, CoCl2 x 6H2O, CuCl2 x 2H2O, Na2MoO4 x 2H2O, H3BO3, and distilled water. Its stock steps adjust pH to 6.0 with KOH and keep the butyl-stopper pretreatment note.

## Completeness

The generated record preserves pH 7.5, the main autoclave/addition instruction, the Mineral solution pH 6.0 step, and the butyl-stopper pretreatment comment.

It does not preserve the 5 ml/L Mineral solution stock row, the 10 ml/L 10% yeast extract stock row, the 10 ml/L 10% peptone stock row, or the main and Mineral solution final-volume water rows.

The equivalent TOGO M1362 evidence is absent from `merged_from`, and the TOGO record carries the original source amounts while this MediaDive record carries 1025 ml final-volume normalized amounts.

## Findings

- Major: The 5 ml/L Mineral solution stock was flattened into direct final-medium EDTA, FeSO4 x 7H2O, MnCl2 x 4H2O, ZnSO4 x 7H2O, CoCl2 x 6H2O, CuCl2 x 2H2O, Na2MoO4 x 2H2O, and H3BO3 rows at undiluted stock concentrations.
- Major: The 10 ml 10% yeast extract addition was converted to 10 g/L yeast extract instead of a 10 ml/L stock addition or 1 g/L final yeast extract.
- Major: The 10 ml 10% peptone addition was converted to 10 g/L peptone instead of a 10 ml/L stock addition or 1 g/L final peptone.
- Major: Main and Mineral solution 1 L distilled-water rows were dropped instead of being retained as final-volume context for their respective solutions.
- Minor: The equivalent TOGO M1362 JCM import remains a separate normalized record and is not represented in `merged_from`.

## Recommended Edits

- Keep Mineral solution as a 5 ml/L stock addition or pre-dilute its constituent rows by 5 ml/L.
- Represent 10% yeast extract and 10% peptone as 10 ml/L stock additions or 1 g/L final undefined components.
- Preserve separate final-volume context for the main medium and Mineral solution stock.
- Merge or cross-link the MediaDive J1266 and TOGO M1362 records for the same JCM_M1266 recipe.

## Follow-up Checks

- Confirm that Mineral solution trace metals are no longer present at stock concentrations in regenerated final-medium output.
- Confirm that yeast extract and peptone are not 10 g/L in regenerated J1266 output unless a source explicitly provides those final concentrations.
- Re-run strict, reference, term, and LinkML validation after regenerating the record.

## Additional Notes

JCM GRMD 1266 was checked directly and returned "Nothing found"; the review therefore relies on the MediaDive REST payload and TOGO M1362 archival import for the underlying JCM_M1266 recipe.
