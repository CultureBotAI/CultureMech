# YAML Record Review: mitsuhashi_maramorosch_m_m_medium

- Repository: CultureMech
- Record: data/merge_yaml/merged/mitsuhashi_maramorosch_m_m_medium.yaml
- Started UTC: 2026-09-24T07:31:54Z
- Finished UTC: 2026-09-24T07:32:39Z
- Verdict: needs curation

## Target

- Generated record: `CultureMech:008873`
- Generated name: `mitsuhashi_maramorosch_m_m_medium`
- Generated source file: `data/merge_yaml/merged/mitsuhashi_maramorosch_m_m_medium.yaml`
- Normalized owner: `data/normalized_yaml/bacterial/mitsuhashi_maramorosch_m_m_medium.yaml`
- Upstream source: TOGO Medium `M2287`, `Mitsuhashi-Maramorosch (M&M) medium`

## Validation

- Open LinkML validation passed: `No issues found`.
- Strict validation passed with 0 ERROR rows in `/private/tmp/mitsuhashi_maramorosch_m_m_medium.strict.tsv`.
- Reference validation passed with 0 checks.
- Term validation passed.
- Embedded `curation_history` was not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The generated record identity is aligned with TOGO `M2287`.
- The `media_term` points to `TOGO:M2287` with label `Mitsuhashi-Maramorosch (M&M) medium`.
- `D (+) glucose`, `yeast extract`, and `heat-inactivated fetal bovine serum` are ungrounded in the actual M2287 portion of the formula.
- `lactalbumin hydrolysate`, present in TOGO M2287, is absent from the generated YAML.
- Three generated rows have supplier metadata for LB Medium (Luria-Bertani, Miller formulation), which is unrelated to Mitsuhashi-Maramorosch medium.

## Evidence

- TOGO `M2287` lists eleven ingredients: 1 L distilled water, 5.0 g/L yeast extract, 120 mM NaCl, 22 mM `D (+) glucose`, 2.7 mM KCl, 1.4 mM NaHCO3, 1 mM CaCl2, 0.2 mM MgCl2, 1.3 mM NaH2PO4, 5% heat-inactivated fetal bovine serum, and 6.5 g/L lactalbumin hydrolysate.
- The TOGO source comment describes pure Sodalis cultures maintained in vitro at 25 C in Mitsuhashi-Maramorosch medium supplemented with 5% heat-inactivated fetal bovine serum.
- The generated YAML preserves ten of the eleven TOGO ingredients and drops only `lactalbumin hydrolysate`.
- The generated YAML appends `Tryptone` 10 g/L, a second `Yeast extract` 5 g/L, and a second `Sodium chloride` 10 g/L from an LB Miller product note.

## Completeness

- The source 6.5 g/L lactalbumin hydrolysate row is missing.
- The generated record does not preserve the 25 C Sodalis maintenance context.
- The 5% fetal bovine serum source unit is represented as `PERCENT_W_V`, but the TOGO source string only says 5%, so weight/volume is an unsupported assumption.
- The normalized owner has the same LB Miller contamination as the generated record, so this needs a source YAML edit before regeneration.

## Findings

- High: `lactalbumin hydrolysate` at 6.5 g/L is omitted from the record even though it is part of TOGO `M2287`.
- High: The record contains three LB Miller rows, `Tryptone`, `Yeast extract`, and `Sodium chloride`, that are not in the TOGO M2287 formula.
- High: The added LB Miller `Yeast extract` and `Sodium chloride` rows duplicate real M2287 rows with different units, changing the recipe composition.
- Medium: Fetal bovine serum was imported as `PERCENT_W_V` even though the TOGO source does not state a weight/volume percent.
- Medium: 25 C and the Sodalis source context are missing.
- Low: Three authentic M2287 ingredients are ungrounded.

## Recommended Edits

- Remove the LB Medium supplier-catalog enrichment from `data/normalized_yaml/bacterial/mitsuhashi_maramorosch_m_m_medium.yaml`.
- Restore `lactalbumin hydrolysate` at 6.5 g/L with its TOGO role and source label.
- Keep exactly one yeast extract row and exactly one sodium chloride row, with the TOGO M2287 concentrations.
- Change the fetal bovine serum unit to a schema representation that does not overstate weight/volume unless source evidence for weight/volume is found.
- Add the 25 C Sodalis maintenance context if the model has a suitable source-context field.
- Re-run the merge after editing the normalized record.

## Follow-up Checks

- Re-fetch TOGO `M2287` and verify the curated output contains all eleven TOGO ingredients and no LB Miller constituents.
- Confirm the curated record has no `laboratorynotes.com` or `Luria-Bertani` source text.
- Re-run open LinkML, strict, reference, and term validation after regenerating the merged record.
- The normalized-owner lookup used `rg --no-ignore --hidden`; repeat ignored-file-inclusive checks for exact owner and duplicate source paths after the edit.

## Additional Notes

- None found.
