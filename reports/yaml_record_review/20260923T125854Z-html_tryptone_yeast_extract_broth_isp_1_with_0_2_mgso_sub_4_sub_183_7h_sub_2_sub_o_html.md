# YAML Record Review: TRYPTONE-Yeast Extract Broth (ISP-1) With 0.2% MgSO4 7H2O
- Repository: CultureMech
- Record: data/merge_yaml/merged/html_tryptone_yeast_extract_broth_isp_1_with_0_2_mgso_sub_4_sub_183_7h_sub_2_sub_o_html.yaml
- Started UTC: 2026-09-23T12:58:02Z
- Finished UTC: 2026-09-23T12:58:54Z
- Verdict: needs curation

## Target

Reviewed the generated TOGO/JCM branch for TOGO Medium M672 and JCM Medium 656, `TRYPTONE-YEAST EXTRACT BROTH (ISP-1) WITH 0.2% MgSO4 7H2O`, at `data/merge_yaml/merged/html_tryptone_yeast_extract_broth_isp_1_with_0_2_mgso_sub_4_sub_183_7h_sub_2_sub_o_html.yaml`. The maintained source is `data/normalized_yaml/bacterial/html_tryptone_yeast_extract_broth_isp_1_with_0_2_mgso_sub_4_sub_183_7h_sub_2_sub_o_html.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/html_tryptone_yeast_extract_broth_isp_1_with_0_2_mgso_sub_4_sub_183_7h_sub_2_sub_o_html.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record's `TOGO:M672` accession and JCM Medium 656 URL identify the intended ISP-1 derivative with added MgSO4 x 7 H2O. Literal TOGO HTML markup leaked into `original_name`, `name`, and `media_term.term.label`, but the source ID still points to the correct JCM recipe.

## Evidence

JCM Medium 656 lists 5 g Tryptone, 3 g yeast extract, 2 g MgSO4 x 7 H2O, and 1 L distilled water. It instructs users to adjust pH to 7.0 - 7.2, notes that premixed Tryptone-yeast extract broth is available from Becton Dickinson as ISP Medium 1, and says to add MgSO4 x 7 H2O before autoclaving. TOGO M672 mirrors the same amounts and notes.

## Completeness

The three non-water ingredients are present with source-supported concentrations and the MgSO4 heptahydrate row has appropriate CHEBI grounding. The generated artifact is missing structured pH, the note about the ISP Medium 1 premix, the instruction to add MgSO4 before autoclaving, and the default JCM autoclave step. The 1 L source water amount is present but has the wrong unit.

No `target_organisms`, growth metrics, or strain-specific growth evidence are asserted, so there are no over-scoped organism claims to review.

## Findings

- **major**: The explicit 1 L distilled-water row is represented as `1 G_PER_L`.
- **major**: The source pH range, 7.0 - 7.2, is absent.
- **major**: The source instruction to add MgSO4 x 7 H2O before autoclaving is absent.
- **major**: The JCM default 121 C for 15 min autoclave instruction is absent.
- **minor**: Literal HTML tags leaked from TOGO into the medium label and slug instead of being normalized to a plain text formula.

## Recommended Edits

- In `data/normalized_yaml/bacterial/html_tryptone_yeast_extract_broth_isp_1_with_0_2_mgso_sub_4_sub_183_7h_sub_2_sub_o_html.yaml`, change distilled water from `1 G_PER_L` to 1 L or 1000 ml.
- Add structured pH 7.0 - 7.2, the MgSO4-before-autoclaving preparation detail, and the default JCM autoclave step.
- Preserve the ISP Medium 1 premix note in source-grounded notes or preparation text.
- Strip literal `<html>` and `<sub>` tags from the label and slug before regenerating the merged artifact.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Re-open TOGO M672 and JCM Medium 656 to confirm the regenerated record has 5 g/L tryptone, 3 g/L yeast extract, 2 g/L MgSO4 x 7 H2O, 1 L water, pH 7.0 - 7.2, and the premix/autoclave notes.
- Run the repository's merge freshness audit after regenerating the TOGO/JCM branch.

## Additional Notes

None.
