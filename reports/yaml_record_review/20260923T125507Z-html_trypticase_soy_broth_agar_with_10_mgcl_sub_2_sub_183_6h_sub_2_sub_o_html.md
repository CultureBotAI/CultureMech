# YAML Record Review: TRYPTICASE Soy Broth Agar With 10% MgCl2 6H2O
- Repository: CultureMech
- Record: data/merge_yaml/merged/html_trypticase_soy_broth_agar_with_10_mgcl_sub_2_sub_183_6h_sub_2_sub_o_html.yaml
- Started UTC: 2026-09-23T12:54:10Z
- Finished UTC: 2026-09-23T12:55:07Z
- Verdict: needs curation

## Target

Reviewed the generated TOGO/JCM branch for TOGO Medium M487 and JCM Medium 486, `TRYPTICASE SOY BROTH AGAR WITH 10% MgCl2 6H2O`, at `data/merge_yaml/merged/html_trypticase_soy_broth_agar_with_10_mgcl_sub_2_sub_183_6h_sub_2_sub_o_html.yaml`. The maintained source is `data/normalized_yaml/bacterial/html_trypticase_soy_broth_agar_with_10_mgcl_sub_2_sub_183_6h_sub_2_sub_o_html.yaml`.

## Validation

- Open LinkML validation: passed for `MediaRecipe`.
- Strict validation: passed with zero error rows in `/private/tmp/html_trypticase_soy_broth_agar_with_10_mgcl_sub_2_sub_183_6h_sub_2_sub_o_html.strict.tsv`.
- Reference validation: passed with zero checks.
- Term validation: passed.
- Embedded history validation: Not checked: `just validate-history` validates standalone YAML files under `history/`, not embedded `MediaRecipe.curation_history` entries in generated merge artifacts.

## Identity and Grounding

The record's `TOGO:M487` accession and JCM Medium 486 URL identify the intended Trypticase Soy Broth agar with 10% MgCl2 hexahydrate recipe. Literal TOGO HTML markup leaked into `original_name`, `name`, and `media_term.term.label`, but the source ID still points to the correct JCM recipe.

## Evidence

JCM Medium 486 lists four recipe rows: 30 g Trypticase soy broth (BD-BBL), 100 g MgCl2 x 6 H2O, 20 g agar, and 1 L distilled water. It instructs users to adjust pH to 7.2 and carries the JCM default autoclave condition of 121 C for 15 min unless otherwise stated. TOGO M487 mirrors those rows and pH value.

The generated artifact preserves 100 g MgCl2 x 6 H2O and the source's 20 g agar row. It imports the explicit 1 L water row as `1 G_PER_L`, omits the 30 g Trypticase soy broth row, and adds inferred commercial TSB/TSA constituents with a second 15 g agar row.

## Completeness

The generated record is not complete enough to follow: it lacks the commercial base named by JCM, double-counts agar, and loses both pH 7.2 and default autoclave handling. The commercial-product overlay is cited to a Wikipedia page even though the notes claim a product specification, so those expanded subcomponents are not traceable to an inspected supplier source.

No `target_organisms`, growth metrics, or strain-specific growth evidence are asserted, so there are no over-scoped organism claims to review.

## Findings

- **major**: The source 30 g/L `Trypticase soy broth (BD-BBL)` component is missing as a direct recipe row.
- **major**: A second 15 g/L agar row was introduced from a Tryptic Soy Agar overlay even though JCM 486 already supplies 20 g/L agar separately.
- **major**: Inferred TSB/TSA subcomponents are mixed with source JCM ingredients without preserving that they are a decomposition of the 30 g/L commercial base rather than independent JCM rows.
- **major**: The explicit 1 L distilled-water row is represented as `1 G_PER_L`.
- **major**: Source pH 7.2 and the JCM default 121 C for 15 min autoclave instruction are absent.
- **minor**: Literal HTML tags leaked from TOGO into the medium label and slug instead of being normalized to a plain text formula.

## Recommended Edits

- In `data/normalized_yaml/bacterial/html_trypticase_soy_broth_agar_with_10_mgcl_sub_2_sub_183_6h_sub_2_sub_o_html.yaml`, restore `Trypticase soy broth (BD-BBL)` as a 30 g/L source ingredient.
- Remove the unsupported second 15 g/L agar row and keep the JCM 20 g/L agar row.
- If commercial TSB decomposition is retained, move it under an explicitly evidenced stock/composition object for the 30 g/L Trypticase soy broth component and replace the Wikipedia URL with inspected supplier documentation.
- Change distilled water from `1 G_PER_L` to 1 L or 1000 ml, add structured pH 7.2, add the default JCM autoclave step, and strip literal HTML tags from the label and slug.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation after regeneration.
- Re-open TOGO M487 and JCM Medium 486 to confirm the regenerated record has one commercial Trypticase soy broth component, one 20 g/L agar row, 100 g/L MgCl2 x 6 H2O, 1 L water, and pH 7.2.
- Run the repository's merge freshness audit after regenerating the TOGO/JCM branch.

## Additional Notes

None.
