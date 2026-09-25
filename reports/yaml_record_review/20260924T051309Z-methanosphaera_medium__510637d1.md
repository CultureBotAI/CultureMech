# YAML Record Review: methanosphaera_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/methanosphaera_medium__510637d1.yaml
- Started UTC: 2026-09-24T05:13:09Z
- Finished UTC: 2026-09-24T05:13:09Z
- Verdict: needs curation

## Target

Generated `MediaRecipe` `CultureMech:009728` for TOGO medium `M349`, "Methanosphaera Medium", imported from JCM medium 355.

## Validation

- LinkML open schema validation: Passed with "No issues found".
- Strict recipe validation: Passed; `/private/tmp/methanosphaera_medium_510637d1.strict.tsv` contained only the header row.
- Reference validation: Passed with 0 checks.
- Term validation: Passed.
- Embedded curation history: Not checked: the history validator targets standalone files under `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

- The TOGO and source JCM identities are preserved: TOGO `M349` maps to JCM GRMD 355, and the live JCM page still serves "METHANOSPHAERA MEDIUM".
- The main gram-scale rows are present and generally match JCM 355.
- The generated YAML has no `ph_value`, `ph_range`, or `preparation_steps` top-level keys; an exact `rg --no-ignore --hidden` check against this record returned no matches for those keys.

## Evidence

- JCM 355 lists a 900 ml distilled-water recipe containing 100 ml clarified rumen fluid, 2 g yeast extract, 2 g Trypticase peptone, 0.5 g sodium acetate, 0.5 g sodium formate, 10 ml trace minerals from Medium 151, 1 ml trace vitamins from Medium 197, 0.19 mg Na2SeO4, 0.7 mg NiCl2 x 6 H2O, 3 mg FeSO4 x 7 H2O, buffer salts, ammonium salts, 5 ml methanol, 1 mg resazurin, 0.875 g L-Cysteine HCl H2O, and 0.375 g Na2S x 9 H2O.
- JCM 355 instructs users to omit methanol, cysteine, and sulfide before boiling, cool under N2, add methanol, dispense under N2, autoclave, stand overnight, separately autoclave 5% cysteine and sulfide stocks under N2, replace the gas phase with 80:20 H2-CO2 before inoculation, add the reduced stocks aseptically and anaerobically, and pressurize inoculated bottles to 200 kPa H2-CO2.
- The source also defines clarified rumen fluid preparation by heating rumen content, centrifuging it, and using the supernatant.

## Completeness

- All major scalar ingredients are present.
- The trace-mineral and trace-vitamin stock additions are not structured.
- Unit-bearing source rows in mg and ml were converted to `G_PER_L` values.
- Preparation, gas handling, and clarified-rumen-fluid processing are absent.

## Findings

1. Major - Source mg rows are inflated to gram-per-liter entries. JCM 355 has 0.19 mg Na2SeO4, 0.7 mg NiCl2 x 6 H2O, 3 mg FeSO4 x 7 H2O, and 1 mg resazurin, but the generated concentrations are `0.19 G_PER_L`, `0.7 G_PER_L`, `3 G_PER_L`, and `1 G_PER_L`.
2. Major - Source ml rows are also serialized as gram-per-liter entries. The 5 ml methanol row and 100 ml clarified-rumen-fluid row became `5 G_PER_L` and `100 G_PER_L` instead of volume additions.
3. Major - Cross-medium stock additions are empty and use mass units. The JCM 151 trace minerals row and JCM 197 trace vitamins row should be 10 ml and 1 ml additions with structured stock references, but the generated `solutions` entries are empty `Unknown solution` stubs at `10 G_PER_L` and `1 G_PER_L`.
4. Major - The preparation sequence was dropped. The generated YAML loses the N2 boiling/cooling/dispensing sequence, overnight standing, separate 5% reducing-stock autoclaving, replacement with H2-CO2 gas, aseptic and anaerobic reducing-stock addition, and 200 kPa post-inoculation pressure.
5. Minor - Clarified rumen fluid was duplicated. The source has one 100 ml clarified-rumen-fluid ingredient and a prose preparation sentence; the generated record has that ingredient plus an extra variable `clarified rumen fluid` ingredient introduced from the prose.

## Recommended Edits

- Restore mg and ml source units for Na2SeO4, NiCl2 x 6 H2O, FeSO4 x 7 H2O, resazurin, methanol, and clarified rumen fluid.
- Represent the JCM 151 and JCM 197 rows as linked stock additions with 10 ml/l and 1 ml/l volumes.
- Restore the full JCM preparation paragraph, including N2 and H2-CO2 handling and the 200 kPa pressurization step.
- Keep clarified-rumen-fluid preparation as preparation text or a child solution note, not as a second variable ingredient.

## Follow-up Checks

- Re-run focused schema, strict, reference, and term validators on the regenerated merged YAML.
- Compare regenerated quantities against JCM 355 to confirm no milligram rows remain as `G_PER_L`.
- Confirm that only one clarified-rumen-fluid row remains.

## Additional Notes

The hydrate punctuation in TOGO source labels can be normalized for display, but those label artifacts are secondary to the row-unit drift and missing anaerobic preparation.
