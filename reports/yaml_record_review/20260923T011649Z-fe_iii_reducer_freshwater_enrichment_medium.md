# YAML Record Review: Fe(III)-Reducer Freshwater Enrichment Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/fe_iii_reducer_freshwater_enrichment_medium.yaml
- Started UTC: 2026-09-23T01:16:49Z
- Finished UTC: 2026-09-23T01:17:08Z
- Verdict: needs curation

## Target

`data/merge_yaml/merged/fe_iii_reducer_freshwater_enrichment_medium.yaml` is the generated TOGO M410 Fe(III)-Reducer Freshwater Enrichment Medium record. The maintained owner is `data/normalized_yaml/bacterial/TOGO_M410_Fe_III_-Reducer_Freshwater_Enrichment_Medium.yaml`.

The suffixed `data/merge_yaml/merged/fe_iii_reducer_freshwater_enrichment_medium__2616625b.yaml` file is the direct MediaDive/JCM J412 import for the same source formula.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/fe_iii_reducer_freshwater_enrichment_medium.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `TOGO:M410` media term and JCM GRMD 412 URL identify the intended Fe(III)-Reducer Freshwater Enrichment Medium source.

The primary CHEBI terms for the small salts, sodium selenate, and L-cysteine hydrochloride hydrate are plausible. The gas terms are grounded correctly but are preparation gases, not variable-concentration medium ingredients.

## Evidence

TOGO M410 and JCM GRMD 412 specify a 1 L medium containing poorly crystalline iron(III) oxide at 100 mM, 0.33 g/l each MgCl2.6H2O, CaCl2.2H2O, KCl, and KH2PO4, 0.25 g/l NH4Cl, 2.5 g/l NaHCO3, 18.9 mg/l Na2SeO4, 10 ml/l Trace vitamins, 10 ml/l Trace mineral solution, 0.044 g/l L-cysteine HCl H2O, and 0.26 g/l FeCl2.4H2O.

The source preparation excludes L-cysteine HCl H2O and FeCl2.4H2O from the autoclaved basal medium, sparges 20 ml aliquots in 120 ml serum bottles with H2-CO2 gas, separately autoclaves 100- or 200-fold concentrated L-cysteine and FeCl2 stocks under N2, then adds those sterile stocks before inoculation and pressurizes vessels to 100 kPa H2-CO2.

## Completeness

The generated TOGO record contains the basal gram quantities, but it is not complete enough to reconstruct the anaerobic medium. Sodium selenate is 1000-fold too high, the two 10 ml referenced stock additions have the wrong unit and empty compositions, the iron(III) oxide cross-reference is not expanded, 1 L distilled water is represented as `1 G_PER_L`, and the gas handling is encoded only as bare variable ingredients.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Major | Sodium selenate has the wrong unit. | TOGO and JCM list 18.9 mg/l Na2SeO4; the generated record stores `18.9 G_PER_L`. | Change the amount to 18.9 mg/l or 0.0189 g/l. |
| Major | Referenced trace solutions are empty and have the wrong addition units. | TOGO M410 adds 10 ml Trace vitamins from M190 and 10 ml Trace mineral solution from M409; the generated `solutions` rows have empty `composition` lists and `10 G_PER_L`. | Model these as 10 ml/l stock additions and expand or explicitly reference the M190 and M409 recipes. |
| Major | The anaerobic preparation sequence is missing. | JCM excludes L-cysteine and FeCl2 from the autoclaved basal medium, sparges H2-CO2, separately autoclaves concentrated L-cysteine and FeCl2 stocks under N2, and adds them before inoculation. The generated record has no `preparation_steps`. | Add preparation steps and move H2, CO2, and N2 into the gas contexts they control. |
| Minor | Distilled water has the wrong unit. | TOGO lists 1 L distilled water; the generated record stores it as `1 G_PER_L`. | Represent water as the 1 L basis. |
| Minor | The duplicate direct JCM import was not merged. | TOGO M410 and MediaDive J412 describe JCM GRMD 412 but generated into separate records. | Deduplicate these records after repairing the TOGO and direct JCM owners. |
| Minor | `medium_type` is too broad. | The source formula is fully chemically defined apart from prepared Fe(III) oxide and trace stocks; MediaDive marks J412 as not complex. | Consider changing the TOGO owner to `medium_type: DEFINED` and `composition_type: DEFINED`. |

## Recommended Edits

1. Rework `data/normalized_yaml/bacterial/TOGO_M410_Fe_III_-Reducer_Freshwater_Enrichment_Medium.yaml` to preserve the JCM 412 main-solution structure.
2. Correct Na2SeO4 from grams to milligrams.
3. Replace empty Trace vitamins, Trace mineral solution, and poorly crystalline iron(III) oxide solution stubs with expanded or resolvable stock references.
4. Move H2, CO2, and N2 into preparation-step gas handling.
5. Add the missing JCM preparation steps.
6. Correct distilled water and defined-medium metadata, then regenerate.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated merge.
- Confirm Na2SeO4 is not `18.9 G_PER_L`.
- Confirm the two 10 ml additions are no longer `G_PER_L`.
- Confirm L-cysteine and FeCl2 are explicitly post-autoclave stock additions.
- Confirm the TOGO and direct JCM imports collapse to one generated record after both sides are repaired.

## Additional Notes

None found.
