# YAML Record Review: methanocaldococcus_leighii_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/methanocaldococcus_leighii_medium__0076a77f.yaml`
- Started UTC: 2026-09-24T03:23:57Z
- Finished UTC: 2026-09-24T03:23:57Z
- Verdict: needs curation

## Target

- Stable ID: `CultureMech:002380`
- Label: `methanocaldococcus_leighii_medium`
- Category: `archaea`
- Maintained owner: `data/normalized_yaml/archaea/methanocaldococcus_leighii_medium.yaml`
- Source identity: MediaDive/JCM medium J1211, `METHANOCALDOCOCCUS LEIGHII MEDIUM`

## Validation

- Open schema: Passed; `linkml-validate` reported no issues.
- Strict validator: Passed; 1 file scanned, 0 files with errors, and 0 error rows.
- Reference validator: Passed; 0 reference checks were applicable.
- Term validator: Passed.
- Embedded history: Not checked: the repository history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` embedded in merged YAML.

## Identity and Grounding

- `media_term` grounds the generated record to MediaDive/JCM `J1211`.
- Exact ignored-file search for `CultureMech:002380`, `mediadive.medium:J1211`, `mediadive.solution:5445`, and `methanocaldococcus_leighii_medium` confirmed a single direct JCM owner for this generated fingerprint.
- The same search found a separate TOGO M1298 import that also maps to original JCM M1211 and builds `data/merge_yaml/merged/METHANOCALDOCOCCUS_LEIGHII_MEDIUM.yaml`, so this direct JCM recipe is duplicated in generated output.
- `mediadive.solution:5445` also exists as `data/normalized_yaml/bacterial/mediadive_5445_Trace_mineral_solution.yaml`, but the generated J1211 record still carries only an empty `Unknown solution` stub for that stock.

## Evidence

- MediaDive J1211 encodes a main recipe with NaCl, magnesium salts, NH4Cl, KCl, K2HPO4, `CaCl2 x 2 H2O`, `FeSO4 x 7 H2O`, 10 ml trace-mineral solution, 10 ml trace vitamins, sodium acetate, PIPES, NaHCO3, 1 mg resazurin, 1000 ml water, and 10 ml of a 5% `Na2S x 9 H2O` solution.
- After a `Trace mineral solution` heading, the source lists 1 L of trace-mineral stock containing trisodium citrate, `MgSO4 x 7 H2O`, `MnSO4 x n H2O`, `CoSO4 x 7 H2O`, `ZnSO4 x 7 H2O`, `Na2MoO4 x 2 H2O`, `NiCl2 x 6 H2O`, `Na2SeO3`, `CuSO4 x 5 H2O`, `AlK(SO4)2`, H3BO3, `VOSO4 x n H2O`, `Na2WO4 x 2 H2O`, and water.
- MediaDive solution 3861 provides the separate `Trace vitamins` stock at 1 L stock concentrations.
- MediaDive solution 5445 is a named `Trace mineral solution` made from solution 3804 plus additional nickel, selenite, and tungstate rows.

## Completeness

- The live JCM URL now returns no formula, but MediaDive J1211 and solution 5445 preserve enough stock, vitamin, sulfide, and preparation detail to curate the record.
- Empty `target_organisms` and `growth_data` are optional-field omissions, not review findings for this record.

## Findings

- Blocker: the inline `Trace mineral solution` recipe was flattened into top-level final-medium ingredients. `Trisodium citrate x 2 H2O`, the 3 g/L stock `MgSO4 x 7 H2O`, `MnSO4 x n H2O`, trace metals, selenite, vanadyl sulfate, and tungstate belong under a child stock rather than `ingredients`.
- Blocker: the J1211 trace-vitamin stock was flattened into top-level ingredient rows at its 1 L stock concentrations, so all vitamin rows are about 100-fold too concentrated for the final medium.
- Blocker: the 10 ml 5% `Na2S x 9 H2O` post-autoclave solution is stored as a `Na2S x 9 H2O` top-level ingredient at `10` `G_PER_L`, turning a volume of reductant stock into an unsupported mass concentration.
- Major: `solutions[0]` keeps `mediadive.solution:5445` as `Unknown solution` with no `composition` and a `10` `G_PER_L` concentration, even though the MediaDive REST source and a standalone normalized solution record expose the stock identity and several component rows.
- Major: `MgSO4 x 7 H2O` is summed across main-medium and stock scopes. The final value `3.15271` g/L is a merge of `1.67488` and `1.47783`, where the second row was the trace-mineral stock's 3 g/L value divided through MediaDive's combined 2030 ml parsing artifact.
- Major: trace-mineral preparation leaked into the main-medium preparation sequence as a top-level `Trace mineral solution:` fragment followed by an `ADJUST_PH` step for trisodium citrate at pH 6.5.
- Minor: a separate TOGO M1298 generated record exists for the same original JCM M1211 source and should be reconciled after the direct JCM record is curated.

## Recommended Edits

- In `data/normalized_yaml/archaea/methanocaldococcus_leighii_medium.yaml`, replace the flattened trace-mineral rows with a structured `Trace mineral solution` stock and move its trisodium citrate, sulfate, trace metal, selenite, vanadyl sulfate, and tungstate rows under that stock.
- Replace the flattened trace-vitamin rows with a structured 10 ml `Trace vitamins` stock using the MediaDive 3861 stock composition.
- Encode `Na2S x 9 H2O` as a 10 ml addition of a 5% stock solution autoclaved and stored under N2, not as a 10 g/L final ingredient.
- Populate or link `mediadive.solution:5445` rather than leaving an empty `Unknown solution` in the generated J1211 record.
- Scope the trisodium-citrate pH 6.5 instructions to the trace-mineral solution and remove the orphaned top-level `Trace mineral solution:` preparation step.
- Reconcile this direct JCM J1211 record with the TOGO M1298 import after both source records represent the same stock hierarchy.

## Follow-up Checks

- Rerun open-schema, strict, reference, and term validation after restoring stock structure.
- Rebuild merged YAML and confirm `MgSO4 x 7 H2O` no longer contains a `Merged 2 duplicates` sum in the J1211 record.
- Confirm regenerated J1211 output has no `Unknown solution` entry for `mediadive.solution:5445`.
- Compare regenerated JCM J1211 and TOGO M1298 outputs and verify only one active canonical generated record remains for this source medium.

## Additional Notes

None found.
