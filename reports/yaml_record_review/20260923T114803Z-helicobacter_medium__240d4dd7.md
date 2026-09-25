# YAML Record Review: Helicobacter Medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/helicobacter_medium__240d4dd7.yaml
- Started UTC: 2026-09-23T11:47:20Z
- Finished UTC: 2026-09-23T11:48:03Z
- Verdict: needs curation

## Target

Reviewed the generated Togo M1402 branch for JCM 1305, `Helicobacter Medium`, at `data/merge_yaml/merged/helicobacter_medium__240d4dd7.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/helicobacter_medium__240d4dd7.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is grounded to `TOGO:M1402`, which imports `JCM_M1305`. JCM Medium 1305 is `HELICOBACTER MEDIUM`, so the Togo wrapper is linked to the intended JCM formulation.

## Evidence

Togo M1402 and JCM 1305 describe an 80 ml Brucella broth base containing 2.8 g Brucella broth and 80 ml distilled water. After autoclaving, the base is cooled to 50 C, acidified aseptically with 135 microliter concentrated HCl, then supplemented with 20 ml heat-inactivated fetal bovine serum, 2 ml Vitox, 0.4 ml Skirrow supplement, and 100 microliter amphotericin B in 5 mg/ml DMSO. The source also gives stable-culture conditions: 5 ml broth in a 25 cm2 polystyrene flask at 37 C under 5% O2 and 12% CO2 with shaking at 50 rpm.

The generated record lists the six imported Togo components, but it converts every milliliter and microliter addition into `G_PER_L` without scaling the 80 ml source batch to one liter. It omits the concentrated HCl addition and all preparation and incubation conditions.

## Completeness

The generated artifact is stale relative to `data/normalized_yaml/bacterial/TOGO_M1402_Helicobacter_Medium.yaml`. That normalized record scales all source rows 10x to a one-liter basis, keeps HCl as a 1.35 ml/L aseptic addition, represents the late FBS, Vitox, Skirrow, and amphotericin stock additions in ml/L, and records the 37 C microaerophilic shaking incubation.

## Findings

- Source rows measured in milliliters or microliters were imported as grams per liter.
- The 80 ml JCM source batch was not scaled to one liter; Brucella broth should be 28 g/L, not 2.8 g/L.
- The 135 microliter concentrated-HCl addition is missing.
- Post-autoclave aseptic addition order is absent, so antimicrobial and serum stocks are indistinguishable from base ingredients.
- The 37 C, 5% O2, 12% CO2, 50 rpm, 25 cm2 flask incubation conditions are absent.
- The Togo wrapper remains a separate generated branch from the direct JCM 1305 branch.

## Recommended Edits

- Regenerate the merged artifact from the repaired Togo M1402 normalized source.
- Preserve the 10x-normalized units: Brucella broth 28 g/L, distilled water 800 ml/L, HCl 1.35 ml/L, fetal bovine serum 200 ml/L, Vitox 20 ml/L, Skirrow supplement 4 ml/L, and amphotericin B stock 1 ml/L.
- Preserve the autoclave, 50 C cooling, aseptic additions, and microaerophilic shaking incubation details.
- Merge or alias the Togo M1402 branch with the direct JCM 1305 branch after both are regenerated.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation on the regenerated artifact.
- Confirm the regenerated artifact has no `G_PER_L` concentrations on source rows whose JCM unit is `ml` or `microliter`.

## Additional Notes

None.
