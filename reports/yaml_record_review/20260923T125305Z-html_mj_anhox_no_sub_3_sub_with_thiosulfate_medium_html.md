# YAML Record Review: MJ/Anhox-NO3 With Thiosulfate Medium
- Repository: CultureMech
- Record: data/merge_yaml/merged/html_mj_anhox_no_sub_3_sub_with_thiosulfate_medium_html.yaml
- Started UTC: 2026-09-23T12:51:48Z
- Finished UTC: 2026-09-23T12:53:05Z
- Verdict: needs curation

## Target

Reviewed the generated TOGO/JCM branch for TOGO Medium M320 and JCM Medium 325, `MJ/ANHOX-NO3 WITH THIOSULFATE MEDIUM`, at `data/merge_yaml/merged/html_mj_anhox_no_sub_3_sub_with_thiosulfate_medium_html.yaml`. The maintained source is `data/normalized_yaml/bacterial/html_mj_anhox_no_sub_3_sub_with_thiosulfate_medium_html.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/html_mj_anhox_no_sub_3_sub_with_thiosulfate_medium_html.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The `TOGO:M320` accession and JCM Medium 325 URL identify the intended MJ/ANHOX nitrate medium with thiosulfate. Literal TOGO HTML markup leaked into `original_name`, `name`, and `media_term.term.label`, but the source ID still points to the correct JCM recipe.

## Evidence

JCM Medium 325 lists 0.05 g NH4Cl, 0.6 g Na2SiO3, 0.85 g NaNO3, 2.48 g Na2S2O3 x 5 H2O, 2 g NaHCO3, 1 ml Trace vitamins, 100 ml MJ(-N) synthetic seawater, and 900 ml distilled water. It instructs dispensing the medium under an H2-CO2 4:1 gas stream, sealing the vessels, autoclaving, adjusting pH to 7.5 if necessary, and pressurizing inoculated bottles to 200 kPa H2-CO2 4:1 after inoculation.

The generated record preserves the five direct gram-scale solutes. It converts the 900 ml distilled-water row to `900 G_PER_L`, converts the 1 ml and 100 ml cross-referenced media to empty `G_PER_L` solutions, and represents H2 and CO2 as variable ingredients rather than as the preparation atmosphere.

## Completeness

The generated artifact is missing pH 7.5, the anaerobic H2-CO2 dispensing and pressurization instructions, the default JCM autoclave step as a structured operation, and usable references to the M190 Trace vitamins and M260 MJ(-N) synthetic seawater recipes.

No `target_organisms`, growth metrics, or strain-specific growth evidence are asserted, so there are no over-scoped organism claims to review.

## Findings

- **major**: The explicit 900 ml distilled-water row is represented as `900 G_PER_L`.
- **major**: The 1 ml Trace vitamins cross-reference and 100 ml MJ(-N) synthetic seawater cross-reference are represented as empty gram-per-liter solutions.
- **major**: The H2-CO2 gas mixture was promoted to two variable-concentration ingredients instead of an anaerobic atmosphere and bottle-pressurization condition.
- **major**: pH 7.5 and the source distribution, sealing, autoclave, pH-adjustment, and 200 kPa pressurization instructions are absent.
- **minor**: Literal HTML tags leaked from TOGO into the medium label and slug instead of being normalized to a plain `MJ/ANHOX-NO3 With Thiosulfate Medium` name.

## Recommended Edits

- In `data/normalized_yaml/bacterial/html_mj_anhox_no_sub_3_sub_with_thiosulfate_medium_html.yaml`, change distilled water from `900 G_PER_L` to 900 ml per liter.
- Model Trace vitamins and MJ(-N) synthetic seawater as 1 ml and 100 ml cross-referenced additions, with resolvable links to the M190 and M260 source recipes rather than empty unknown solutions.
- Move H2 and CO2 out of `ingredients` and into atmosphere/preparation text preserving the 4:1 gas mixture and 200 kPa post-inoculation pressure.
- Add structured pH 7.5 and the JCM 325 preparation sequence.
- Strip literal `<html>` and `<sub>` tags from the label and slug before regenerating the merged artifact.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Re-open JCM 325, TOGO M320, TOGO M190, and TOGO M260 to confirm all direct rows and cross-referenced additions are regenerated with volume semantics.
- Run the repository's merge freshness audit after regenerating the TOGO/JCM branch.

## Additional Notes

None.
