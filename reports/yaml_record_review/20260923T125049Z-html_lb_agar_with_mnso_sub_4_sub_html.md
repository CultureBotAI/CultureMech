# YAML Record Review: LB Agar With MnSO4
- Repository: CultureMech
- Record: data/merge_yaml/merged/html_lb_agar_with_mnso_sub_4_sub_html.yaml
- Started UTC: 2026-09-23T12:49:59Z
- Finished UTC: 2026-09-23T12:50:49Z
- Verdict: needs curation

## Target

Reviewed the generated TOGO/JCM branch for TOGO Medium M1105 and JCM Medium 1040, `LB AGAR WITH MnSO4`, at `data/merge_yaml/merged/html_lb_agar_with_mnso_sub_4_sub_html.yaml`. The maintained source is `data/normalized_yaml/bacterial/html_lb_agar_with_mnso_sub_4_sub_html.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/html_lb_agar_with_mnso_sub_4_sub_html.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record's `TOGO:M1105` accession and original JCM Medium 1040 URL identify `LB AGAR WITH MnSO4`. TOGO's medium name includes literal HTML markup around the MnSO4 subscript, and the importer preserved that markup in `original_name`, `media_term.term.label`, and the normalized slug.

## Evidence

JCM Medium 1040 lists 10 g Tryptone, 5 g yeast extract, 10 g NaCl, 10 mg MnSO4 x H2O, 15 g agar, and 1 L distilled water, followed by a pH adjustment to 7.0. It also carries the JCM default instruction to autoclave at 121 C for 15 min unless otherwise stated. TOGO M1105 mirrors those amounts and reports pH 7.0.

The generated record preserves the tryptone, yeast extract, NaCl, and agar amounts. It imports 1 L distilled water as `1 G_PER_L` and imports the 10 mg MnSO4 x H2O row as `10 G_PER_L` instead of 0.01 g/L.

## Completeness

The generated artifact is missing structured `ph_value`, the pH-adjustment step, and the default JCM autoclave step. Empty organism and growth-evidence slots are acceptable because neither inspected medium recipe makes a strain-specific growth claim.

## Findings

- **major**: The 10 mg MnSO4 x H2O row is represented as `10 G_PER_L`, a 1000-fold unit error.
- **major**: The explicit 1 L distilled-water row is represented as `1 G_PER_L`.
- **major**: Source pH 7.0 and the `Adjust pH to 7.0` instruction are absent.
- **major**: The JCM default 121 C for 15 min autoclave instruction is absent.
- **minor**: Literal HTML tags leaked from TOGO into the medium label and slug instead of being normalized to a plain `LB Agar With MnSO4` name.

## Recommended Edits

- In `data/normalized_yaml/bacterial/html_lb_agar_with_mnso_sub_4_sub_html.yaml`, convert MnSO4 x H2O from 10 mg per liter to `0.01 G_PER_L` or an equivalent mg/L representation.
- Change the distilled-water concentration from `1 G_PER_L` to an explicit 1 L or 1000 ml water volume.
- Strip the literal TOGO `<html>` and `<sub>` tags from `original_name`, `name`, and `media_term.term.label`, preserving the formula text as `MnSO4`.
- Add structured pH 7.0, an `ADJUST_PH` step, and the default JCM autoclave step.
- Regenerate the merged artifact from the corrected normalized source.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Re-open TOGO M1105 and JCM Medium 1040 to confirm MnSO4 amount, water volume, pH, label cleanup, and default autoclave handling.
- Run the repository's merge freshness audit after regenerating the TOGO/JCM branch.

## Additional Notes

None.
