# YAML Record Review: Fe- and S-free basal medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/fe_and_s_free_basal_medium.yaml
- Started UTC: 2026-09-23T01:13:22Z
- Finished UTC: 2026-09-23T01:13:22Z
- Verdict: needs curation

## Target

`data/merge_yaml/merged/fe_and_s_free_basal_medium.yaml` is the generated TOGO M3265 Fe- and S-free basal medium record. The maintained owner is `data/normalized_yaml/bacterial/fe_and_s_free_basal_medium.yaml`.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/fe_and_s_free_basal_medium.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `TOGO:M3265` media term identifies the intended Fe- and S-free basal medium. The record does not import the TOGO pH 7.0 target as `ph_value`.

Most salt rows are grounded to plausible CHEBI terms. The CaCl2 and MgCl2 hydrate rows lack `mediaingredientmech_chebi_term` mirror links, but their primary CHEBI `term` values are correct.

## Evidence

TOGO M3265 lists the structured components NaCl, NH4Cl, CaCl2 x 2 H2O, MgCl2 x 6 H2O, KCl, NaHCO3, MQ H2O, 2 M HCl, 1 M NaOH, and N2. Its source comments add the missing basal salt K2HPO4 at 0.14 g/l.

The TOGO comments also describe preparation order: all basal components except NaHCO3 are dissolved in Milli-Q water and boiled for 15 minutes; the medium is sealed with a butyl rubber stopper and sparged with N2 over a heated, reduced copper column for 1 hour per litre; NaHCO3 is then added in an anaerobic chamber; and the final pH is adjusted to 7.00 with anoxic 2 M HCl or 1 M NaOH.

## Completeness

The generated record captures most structured salt quantities but is incomplete as a recipe. It omits K2HPO4, gives 1 L Milli-Q water the wrong unit, keeps HCl, NaOH, and N2 as bare variable ingredients, and drops the anaerobic boiling, sparging, bicarbonate-addition, and pH-adjustment procedure.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Major | K2HPO4 is missing. | The TOGO source comments include K2HPO4 at 0.14 g/l in the Fe- and S-free basal formula; the generated record has no phosphate ingredient. | Add K2HPO4 at the source concentration and ground it to dipotassium hydrogenphosphate. |
| Major | Critical anaerobic preparation steps are absent. | TOGO describes boiling all non-bicarbonate components, sealing, sparging with N2 over heated reduced copper for 1 hour per litre, anaerobic NaHCO3 addition, and pH 7.00 adjustment. The generated record has no `preparation_steps`. | Move N2, 2 M HCl, and 1 M NaOH into explicit degassing and pH-adjustment steps and preserve the bicarbonate addition order. |
| Minor | Milli-Q water has the wrong concentration unit. | TOGO lists `MQ H2O` as 1 L; the generated record stores it as `1 G_PER_L`. | Represent water as the 1 L basis rather than a gram-per-litre solute. |
| Minor | Source pH is not represented. | TOGO M3265 has pH 7.0 and the comment says to adjust the medium to pH 7.00. | Add `ph_value: 7.0` or equivalent pH metadata. |
| Minor | `medium_type` is too broad. | The source formula is inorganic salts, water, N2, and pH-adjustment solutions; no peptone, extract, serum, or other undefined complex ingredient is present. | Consider changing the type from `COMPLEX` to `DEFINED`. |

## Recommended Edits

1. Add the missing K2HPO4 row to `data/normalized_yaml/bacterial/fe_and_s_free_basal_medium.yaml`.
2. Correct MQ H2O from `1 G_PER_L` to a litre basis.
3. Add preparation steps for pre-bicarbonate boiling, N2 sparging over heated reduced copper, anaerobic NaHCO3 addition, and pH 7.00 adjustment.
4. Move 2 M HCl, 1 M NaOH, and N2 from bare variable ingredients into the relevant preparation-step reagent context if the schema can express that.
5. Add the pH 7.0 target and re-evaluate `medium_type`.
6. Regenerate `data/merge_yaml/merged/fe_and_s_free_basal_medium.yaml`.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated merge.
- Confirm K2HPO4 is present.
- Confirm Milli-Q water is not represented as `G_PER_L`.
- Confirm the record encodes the N2 sparging and delayed NaHCO3 addition steps.
- Confirm the record has pH 7.0 metadata.

## Additional Notes

None found.
