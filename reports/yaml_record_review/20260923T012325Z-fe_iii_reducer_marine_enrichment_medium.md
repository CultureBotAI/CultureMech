# YAML Record Review: Fe(III)-Reducer Marine Enrichment Medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/fe_iii_reducer_marine_enrichment_medium.yaml
- Started UTC: 2026-09-23T01:23:25Z
- Finished UTC: 2026-09-23T01:23:25Z
- Verdict: needs curation

## Target

`data/merge_yaml/merged/fe_iii_reducer_marine_enrichment_medium.yaml` is the generated TOGO M409 Fe(III)-Reducer Marine Enrichment Medium record. The maintained owner is `data/normalized_yaml/bacterial/fe_iii_reducer_marine_enrichment_medium.yaml`.

The suffixed `data/merge_yaml/merged/fe_iii_reducer_marine_enrichment_medium__6a83808e.yaml` file is the direct MediaDive/JCM J411 import for the same source formula.

## Validation

- LinkML open schema: passed.
- Strict validator: passed with 0 error rows in `/private/tmp/fe_iii_reducer_marine_enrichment_medium.strict.tsv`.
- Reference validator: passed; 0 reference checks were applicable.
- Term validator: passed.
- Embedded history: Not checked; the history validator covers standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists.

## Identity and Grounding

The `TOGO:M409` media term and JCM GRMD 411 URL identify the intended Fe(III)-Reducer Marine Enrichment Medium source.

Most main-medium salts are grounded to plausible CHEBI terms. NiCl2.6H2O is grounded to anhydrous nickel dichloride, and the preparation-only FeCl3, NaOH, and trace-mineral constituents should not be final top-level medium ingredients at all.

## Evidence

JCM GRMD 411 specifies a 1 L basal marine medium with 19 g/l NaCl, 9 g/l MgCl2.6H2O, 0.15 g/l MgSO4.7H2O, 0.3 g/l CaCl2.2H2O, 0.5 g/l KCl, 0.42 g/l KH2PO4, 0.1 g/l ammonium sulfate, 0.05 g/l NaBr, 0.02 g/l SrCl2.6H2O, 0.1 g/l BD-Difco yeast extract, 2.5 g/l NaHCO3, 0.02 g/l Na2SeO4, 100 mM poorly crystalline iron(III) oxide, 10 ml/l Trace vitamins, 10 ml/l Trace mineral solution, 0.044 g/l L-cysteine HCl H2O, and 0.26 g/l FeCl2.4H2O.

JCM describes poorly crystalline iron(III) oxide as its own precipitated 0.67 M suspension made from 108 g FeCl3 per litre, 10 N NaOH, centrifugation, and repeated washing. It describes Trace mineral solution separately as Trace minerals of JCM Medium 151 supplemented per litre with 0.025 g Na2MoO4.2H2O, 0.024 g NiCl2.6H2O, and 0.025 g Na2WO4.2H2O.

## Completeness

The generated TOGO record is not complete enough to reconstruct JCM 411. It contains the major basal salts, but it sums unrelated basal and stock-preparation rows, drops the JCM anaerobic preparation procedure, stores gases as variable ingredients, keeps trace stocks as empty solution shells, and flattens Fe(III)-oxide and trace-mineral preparation reagents into the final `ingredients` list.

## Findings

| Severity | Finding | Evidence | Recommendation |
| --- | --- | --- | --- |
| Major | Basal rows were summed with unrelated stock-preparation ingredients. | JCM's basal recipe has 19 g NaCl, 0.15 g MgSO4.7H2O, and 0.3 g CaCl2.2H2O per litre. The owner records 20.0, 3.15, and 0.4 g/l because cleanup merged basal rows with 1.0 g NaCl, 3.0 g MgSO4.7H2O, and 0.1 g CaCl2.2H2O from Trace minerals of Medium 151. | Re-split the basal medium, Fe(III) oxide suspension, and Trace mineral stock into separate recipe scopes. |
| Major | Preparation reagents are top-level final-medium ingredients. | FeCl3 and NaOH are only used to prepare the Fe(III) oxide suspension; Na2MoO4, NiCl2, Na2WO4, and the Medium 151 trace salts are part of Trace mineral solution. The generated record lists all of them as final ingredients. | Move Fe(III)-oxide and trace-mineral constituents into nested preparation records or resolvable stock references. |
| Major | The Trace vitamins and Trace mineral additions have the wrong unit and no composition. | JCM adds 10 ml/l of each stock. The generated `solutions` rows are named `Unknown solution`, have empty `composition` lists, and use `10 G_PER_L`. | Represent both as 10 ml/l stock additions, expanding the Trace vitamins and Trace mineral recipes. |
| Major | Anaerobic preparation steps are absent. | JCM excludes L-cysteine and FeCl2 from the autoclaved base, sparges aliquots with H2-CO2, autoclaves concentrated L-cysteine and FeCl2 stocks under N2, adds them before inoculation, and pressurizes vessels to 100 kPa H2-CO2. The TOGO record has no `preparation_steps`. | Add the JCM procedure and move H2, CO2, and N2 out of bare variable ingredient rows. |
| Minor | The generated merge predates the owner-side duplicate-water repair. | The generated file stores Distilled water as `3.0 G_PER_L`, while the owner was repaired on 2026-09-02 to collapse three identical 1 L water rows to one `1.0 G_PER_L` row. | Regenerate after curation and change water to a 1 L basis. |
| Minor | The duplicate direct JCM import was not merged. | This record and `data/merge_yaml/merged/fe_iii_reducer_marine_enrichment_medium__6a83808e.yaml` both describe JCM GRMD 411. | Deduplicate the TOGO and direct JCM owners after both are repaired. |

## Recommended Edits

1. Rework `data/normalized_yaml/bacterial/fe_iii_reducer_marine_enrichment_medium.yaml` to split the basal medium from the Fe(III) oxide and Trace mineral stock recipes.
2. Restore basal NaCl, MgSO4.7H2O, and CaCl2.2H2O to 19.0, 0.15, and 0.3 g/l.
3. Change Trace vitamins and Trace mineral solution from empty `10 G_PER_L` solutions to 10 ml/l stock additions.
4. Move FeCl3, NaOH, KOH, and trace-mineral constituents into nested stock contexts.
5. Reground NiCl2.6H2O to the hexahydrate term.
6. Add pH 7.0 and the JCM anaerobic preparation sequence.
7. Deduplicate against the direct JCM J411 import and regenerate.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on the regenerated merge.
- Confirm basal NaCl, MgSO4.7H2O, and CaCl2.2H2O are no longer summed with trace-mineral stock constituents.
- Confirm the two 10 ml stock additions are not represented as `G_PER_L`.
- Confirm FeCl3 is only inside the Fe(III) oxide preparation.
- Confirm H2, CO2, and N2 are represented as process gases.

## Additional Notes

None found.
