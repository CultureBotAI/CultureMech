# YAML Record Review: sphaerotilus_natans_subspec_sulfidivorans_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/sphaerotilus_natans_subspec_sulfidivorans_medium.yaml
- Started UTC: 2026-09-25T06:05:50Z
- Finished UTC: 2026-09-25T06:07:16Z
- Verdict: needs curation

## Target

Generated merged YAML for DSMZ 1664, Sphaerotilus natans subspec. sulfidivorans medium, merged with DSMZ 1664a, Modified Sphaerotilus natans ssp. sulfidivorans medium.

## Validation

- LinkML open validation: Passed; `linkml-validate` reported no issues.
- Strict validation: Passed; `/private/tmp/sphaerotilus_natans_subspec_sulfidivorans_medium.strict.tsv` contained only the header row.
- Reference validation: Passed; the reference validator ran 0 checks and reported no failures.
- Term validation: Passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` entries embedded in merged YAML.

## Identity and Grounding

The generated record incorrectly treats DSMZ 1664a as a source duplicate of DSMZ 1664. DSMZ 1664a is a modified recipe with doubled ammonium, phosphate, magnesium, calcium, iron, lactate, peptone, and thiosulfate values relative to the MediaDive 1664 REST payload, plus 50 ul trace/vitamin additions rather than 25 ul additions.

The current DSMZ 1664 PDF also no longer matches the MediaDive 1664 REST payload or the normalized `sphaerotilus_natans_subspec_sulfidivorans_medium.yaml` branch. The PDF lists NaCl, Na2SO4, no Na-lactate, no peptone, and a 25 ml SLM addition, while the REST/YAML representation lists Na-lactate and peptone and lacks NaCl and Na2SO4.

## Evidence

MediaDive 1664 lists the 1664 main solution with 0.3 g (NH4)Cl, 9 mg KH2PO4, 22 mg K2HPO4, 35 mg Na2HPO4 x 7 H2O, 23 mg MgSO4 x 7 H2O, 28 mg CaCl2, 0.25 mg FeCl3 x 6 H2O, 200 mg Na-lactate, 500 mg peptone, 1 g Na2S2SO3, 25 ul Trace element solution, 1000 ml distilled water, and 25 ul Standard vitamin solution.

MediaDive 1664a lists doubled main-solution values for those same MediaDive 1664 main ingredients and doubles the trace/vitamin additions to 50 ul each. The trace-element stock and Standard vitamin solution are separate stock recipes shared by both variants.

The current DSMZ 1664 PDF instead lists 3.62 g NaCl, 0.05 g Na2SO4, no Na-lactate, no peptone, and a post-sterilization 25 ml SLM addition. The current DSMZ 1664a PDF matches the modified MediaDive 1664a basal recipe and lists a 50 ul SLM.155 addition.

## Completeness

The generated record is neither a valid DSMZ 1664 recipe nor a valid DSMZ 1664a recipe. It keeps the 1664a main-solution amounts under the 1664 identity, flattens the shared trace-element and vitamin stock recipes into final `G_PER_L` rows, omits main-solution distilled water, omits trace and vitamin stock water, and drops the 25 ul versus 50 ul stock-addition distinction.

## Findings

- Critical: DSMZ 1664 and DSMZ 1664a are distinct variants and should not be merged as source duplicates.
- Critical: the generated canonical record uses 1664a's doubled main-solution values while retaining the DSMZ 1664 identity.
- Critical: the generated ingredient list flattens Trace element solution and Standard vitamin solution at stock strength instead of preserving 25 ul or 50 ul additions to the main solution.
- Critical: current DSMZ 1664 PDF evidence conflicts with the MediaDive 1664 import; the normalized DSMZ 1664 branch needs source reconciliation before regeneration.
- Major: 1000 ml distilled water rows are missing from the main, trace, and vitamin solutions.

## Recommended Edits

- Split `data/normalized_yaml/bacterial/sphaerotilus_natans_subspec_sulfidivorans_medium.yaml` and `data/normalized_yaml/bacterial/modified_sphaerotilus_natans_ssp_sulfidivorans_medium.yaml` into separate generated records.
- Recurate DSMZ 1664 against the current DSMZ Medium 1664 PDF, resolving the conflict between the PDF and MediaDive 1664 REST payload before regeneration.
- Model DSMZ 1664a as a modified variant with its own doubled main-solution values and 50 ul stock additions.
- Preserve Trace element solution and Standard vitamin solution as stock additions, including their own distilled-water rows.

## Follow-up Checks

- Re-run open, strict, reference, and term validation on the regenerated DSMZ 1664 and 1664a records.
- Confirm no regenerated final-medium ingredient list contains stock-strength trace metals or stock-strength vitamins as direct final `G_PER_L` rows.
- Confirm DSMZ 1664 does not include the DSMZ 1664a doubled main-solution concentrations.

## Additional Notes

None found.
