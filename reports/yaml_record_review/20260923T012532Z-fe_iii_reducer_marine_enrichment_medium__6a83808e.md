# YAML Record Review: Fe(III)-REDUCER MARINE ENRICHMENT MEDIUM

- Repository: CultureMech
- Record: data/merge_yaml/merged/fe_iii_reducer_marine_enrichment_medium__6a83808e.yaml
- Started UTC: 2026-09-23T01:25:32Z
- Finished UTC: 2026-09-23T01:25:44Z
- Verdict: needs curation

## Target

`data/merge_yaml/merged/fe_iii_reducer_marine_enrichment_medium__6a83808e.yaml` is the generated direct MediaDive/JCM J411 Fe(III)-REDUCER MARINE ENRICHMENT MEDIUM record. The maintained owner is `data/normalized_yaml/specialized/fe_iii_reducer_marine_enrichment_medium.yaml`.

The unsuffixed `data/merge_yaml/merged/fe_iii_reducer_marine_enrichment_medium.yaml` file is the TOGO M409 import for the same JCM GRMD 411 source.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/fe_iii_reducer_marine_enrichment_medium_6a83808e.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `mediadive.medium:J411` media term and pH 7.0 value identify the intended JCM GRMD 411 medium.

Most main salts are grounded to plausible CHEBI terms, and the BD-Difco yeast extract row is correctly ungrounded as an undefined extract. Sodium selenate still carries a deprecated `mediaingredientmech_term` link even though its primary CHEBI term is correct.

## Evidence

JCM GRMD 411 is a 1 L recipe containing 19 g/l NaCl, 9 g/l MgCl2.6H2O, 0.15 g/l MgSO4.7H2O, 0.3 g/l CaCl2.2H2O, 0.5 g/l KCl, 0.42 g/l KH2PO4, 0.1 g/l ammonium sulfate, 0.05 g/l NaBr, 0.02 g/l SrCl2.6H2O, 0.1 g/l BD-Difco yeast extract, 2.5 g/l NaHCO3, 0.02 g/l Na2SeO4, 100 mM poorly crystalline iron(III) oxide, 10 ml/l Trace vitamins, 10 ml/l Trace mineral solution, 0.044 g/l L-cysteine HCl H2O, and 0.26 g/l FeCl2.4H2O.

MediaDive J411 marks the main solution volume as 20 ml because the JCM preparation text gives 20 ml in a 120 ml serum bottle as an example vessel fill. JCM says the recipe is brought to 1.0 L before that distribution.

## Completeness

The generated record is not complete enough to reconstruct JCM 411. It preserves pH and most JCM preparation prose, but it inflates main-solution rows 50-fold, drops the Fe(III) oxide and Trace mineral solution additions, flattens Trace vitamins at stock strength, and omits the distilled-water basis.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Major | Main-solution masses were scaled against 20 ml instead of 1 L. | JCM lists 19 g/l NaCl, 9 g/l MgCl2.6H2O, and 2.5 g/l NaHCO3; the generated record stores 950, 450, and 125 g/l. The same 50x inflation affects all main gram rows. | Use the JCM 1 L recipe basis and keep the 20 ml serum-bottle volume only as vessel distribution guidance. |
| Major | Required Fe(III) oxide and Trace mineral additions are missing. | JCM adds 100 mM poorly crystalline iron(III) oxide and 10 ml/l Trace mineral solution; MediaDive includes both stock additions. Neither is present in the generated ingredient list. | Add explicit stock additions for Fe(III) oxide and Trace mineral solution, expanding or referencing their JCM source recipes. |
| Major | Trace vitamins are flattened into final ingredients at stock strength. | JCM adds 10 ml/l Trace vitamins; the generated record places all ten vitamin stock constituents directly under `ingredients` at their 1 L stock concentrations. | Keep Trace vitamins as a 10 ml/l stock addition with its recipe nested under that stock. |
| Minor | Distilled water is missing. | JCM instructs curators to add components to distilled water and bring the volume to 1.0 L. | Add distilled water as the final 1 L basis. |
| Minor | The duplicate TOGO import was not merged. | This record and `data/merge_yaml/merged/fe_iii_reducer_marine_enrichment_medium.yaml` both describe JCM GRMD 411. | Deduplicate these generated records after repairing both normalized owners. |

## Recommended Edits

1. Rework `data/normalized_yaml/specialized/fe_iii_reducer_marine_enrichment_medium.yaml` around the JCM 1 L basis.
2. Reduce all inflated gram-per-litre values back to their source masses per litre.
3. Add poorly crystalline iron(III) oxide at 100 mM and Trace mineral solution at 10 ml/l.
4. Nest Trace vitamins under a 10 ml/l addition instead of flattening its constituents.
5. Add the 1 L distilled-water basis and keep the 20 ml in 120 ml serum bottles detail only in preparation.
6. Deduplicate against TOGO M409 and regenerate.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated merge.
- Confirm NaCl is 19 g/l, not 950 g/l.
- Confirm MgCl2 x 6 H2O is 9 g/l, not 450 g/l.
- Confirm Fe(III) oxide, Trace mineral solution, and Trace vitamins are represented as stock additions.
- Confirm the TOGO and direct JCM imports collapse to one generated record after both sides are repaired.

## Additional Notes

None found.
