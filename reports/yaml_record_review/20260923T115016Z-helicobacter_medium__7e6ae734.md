# YAML Record Review: HELICOBACTER MEDIUM
- Repository: CultureMech
- Record: data/merge_yaml/merged/helicobacter_medium__7e6ae734.yaml
- Started UTC: 2026-09-23T11:48:56Z
- Finished UTC: 2026-09-23T11:50:16Z
- Verdict: needs curation

## Target

Reviewed the generated direct DSMZ branch for DSMZ Medium 1279, `HELICOBACTER MEDIUM`, at `data/merge_yaml/merged/helicobacter_medium__7e6ae734.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/helicobacter_medium__7e6ae734.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record is grounded to `mediadive.medium:1279`, which is DSMZ Medium 1279 `HELICOBACTER MEDIUM` at pH 5.0. It is distinct from the JCM 1305 Helicobacter Medium branch; DSMZ 1279 is an 80 ml Hungate-tube recipe with per-tube aseptic additions and sterile air.

## Evidence

The DSMZ PDF and MediaDive 1279 both list 2.8 g Brucella Broth in 80 ml demineralized water. The recipe then adjusts that base to pH 5.0 with HCl, makes it anoxic under N2/CO2, dispenses 8 ml portions into Hungate tubes, autoclaves, and adds 2.00 ml heat-inactivated fetal bovine serum, 0.06 ml Vitox, 0.02 ml Skirrow supplement, and 0.02 ml amphotericin per tube before adding 1 ml sterile air to each tube.

The generated record keeps the correct six named components and the three source preparation sentences, but every liquid addition is typed as `G_PER_L`. The 80 ml water row is `80 G_PER_L`, and the per-tube serum, Vitox, Skirrow, and amphotericin additions are also expressed as grams per liter instead of scoped milliliter additions.

## Completeness

The record retains the pH and major workflow text, but it does not represent the Hungate-tube batch structure. The 80 ml base, 8 ml tube distribution, post-autoclave additions to each tube, and 1 ml sterile-air addition are only prose and are inconsistent with the top-level `G_PER_L` concentrations.

## Findings

- `Demineralized water` is imported as `80 G_PER_L`; the source lists 80 ml in the base.
- `Fetal bovine serum`, `Vitox`, `Skirrow supplement`, and `Amphotericin` are imported as grams per liter despite source units of ml per Hungate tube.
- The post-autoclave additions are per-tube supplements, not ingredients to be mixed into the original 80 ml base.
- The `Add aseptically to each tube:` preparation step has no structured association with the four supplement rows that follow it.
- The normalized source has repaired MediaDive compound grounding but still needs a unit and per-tube scoping curation pass.

## Recommended Edits

- Curate `data/normalized_yaml/bacterial/helicobacter_medium.yaml` so the 80 ml base and per-tube aseptic additions retain milliliter units and their Hungate-tube scope.
- Keep Brucella Broth normalized to 35 g/L only within the 80 ml base.
- Represent the pH 5.0 HCl adjustment, N2/CO2 anoxic handling, 8 ml dispensing, autoclaving, aseptic additions, and 1 ml sterile-air addition as ordered preparation steps tied to the relevant ingredient groups.
- Regenerate the merged artifact after the normalized source is repaired.

## Follow-up Checks

- Confirm the regenerated DSMZ 1279 record has no `G_PER_L` units on rows whose DSMZ source unit is `ml`.
- Re-run open schema, strict, reference, and term validation after regeneration.

## Additional Notes

None.
