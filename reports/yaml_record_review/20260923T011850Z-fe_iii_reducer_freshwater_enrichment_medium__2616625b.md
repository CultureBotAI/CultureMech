# YAML Record Review: Fe(III)-REDUCER FRESHWATER ENRICHMENT MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/fe_iii_reducer_freshwater_enrichment_medium__2616625b.yaml
- Started UTC: 2026-09-23T01:18:50Z
- Finished UTC: 2026-09-23T01:19:04Z
- Verdict: needs curation

## Target

`data/merge_yaml/merged/fe_iii_reducer_freshwater_enrichment_medium__2616625b.yaml` is the generated direct MediaDive/JCM J412 Fe(III)-REDUCER FRESHWATER ENRICHMENT MEDIUM record. The maintained owner is `data/normalized_yaml/bacterial/fe_iii_reducer_freshwater_enrichment_medium.yaml`.

The unsuffixed `data/merge_yaml/merged/fe_iii_reducer_freshwater_enrichment_medium.yaml` file is the TOGO M410 import for the same JCM GRMD 412 source.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/fe_iii_reducer_freshwater_enrichment_medium_2616625b.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `mediadive.medium:J412` media term, pH 7.0 value, and defined-medium metadata all identify the intended JCM GRMD 412 medium.

The main salts and vitamins are mostly grounded to plausible CHEBI terms. Sodium selenate still carries a deprecated `mediaingredientmech_term` link even though its primary CHEBI term is correct.

## Evidence

JCM GRMD 412 is a 1 L recipe containing 100 mM poorly crystalline iron(III) oxide, 0.33 g/l each MgCl2.6H2O, CaCl2.2H2O, KCl, and KH2PO4, 0.25 g/l NH4Cl, 2.5 g/l NaHCO3, 18.9 mg/l Na2SeO4, 10 ml/l Trace vitamins, 10 ml/l Trace mineral solution, 0.044 g/l L-cysteine HCl H2O, and 0.26 g/l FeCl2.4H2O.

MediaDive J412 marks the main solution volume as 20 ml because the preparation text gives 20 ml in a 120 ml serum bottle as an example vessel fill. JCM says the recipe is brought to 1.0 L before that distribution.

## Completeness

The generated record is not complete enough to reconstruct JCM 412. It preserves the JCM preparation prose, pH, and many CHEBI mappings, but most main-medium concentrations are inflated 50-fold, Trace vitamins are flattened at stock strength, and the Fe(III) oxide and Trace mineral solution additions are absent from `ingredients`.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Major | Main-solution masses were scaled against 20 ml instead of 1 L. | JCM lists 0.33 g/l MgCl2.6H2O, CaCl2.2H2O, KCl, and KH2PO4; the generated record stores each at `16.5 G_PER_L`. The same 50x inflation affects NH4Cl, NaHCO3, Na2SeO4, L-cysteine, and FeCl2. | Use the JCM 1 L recipe basis and keep the 20 ml serum-bottle volume only as vessel distribution guidance. |
| Major | Required Fe(III) oxide and Trace mineral additions are missing. | JCM adds 100 mM poorly crystalline iron(III) oxide and 10 ml/l Trace mineral solution; MediaDive includes both stock additions. Neither is present in the generated ingredient list. | Add explicit stock additions for Fe(III) oxide and Trace mineral solution, expanding or referencing their JCM source recipes. |
| Major | Trace vitamins are flattened into final ingredients at stock strength. | JCM adds 10 ml/l Trace vitamins; the generated file places all ten vitamin stock constituents directly under `ingredients` at their 1 L stock concentrations. | Keep Trace vitamins as a 10 ml/l stock addition with its recipe nested under that stock. |
| Minor | Distilled water is missing. | JCM instructs curators to add components to distilled water and bring the volume to 1.0 L. | Add distilled water as the final 1 L basis. |
| Minor | The duplicate TOGO import was not merged. | This record and `data/merge_yaml/merged/fe_iii_reducer_freshwater_enrichment_medium.yaml` both describe JCM GRMD 412. | Deduplicate these generated records after repairing both normalized owners. |

## Recommended Edits

1. Rework `data/normalized_yaml/bacterial/fe_iii_reducer_freshwater_enrichment_medium.yaml` around the JCM 1 L basis.
2. Reduce the inflated gram-per-litre values back to their source masses per litre.
3. Add poorly crystalline iron(III) oxide at 100 mM and Trace mineral solution at 10 ml/l.
4. Nest Trace vitamins under a 10 ml/l addition instead of flattening its constituents.
5. Add distilled water and keep the 20 ml in 120 ml serum bottles detail only in preparation.
6. Deduplicate against TOGO M410 and regenerate.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated merge.
- Confirm MgCl2 x 6 H2O, CaCl2 x 2 H2O, KCl, and KH2PO4 are each 0.33 g/l, not 16.5 g/l.
- Confirm NaHCO3 is 2.5 g/l, not 125 g/l.
- Confirm Na2SeO4 is 18.9 mg/l or 0.0189 g/l.
- Confirm Fe(III) oxide, Trace mineral solution, and Trace vitamins are represented as stock additions.

## Additional Notes

None found.
