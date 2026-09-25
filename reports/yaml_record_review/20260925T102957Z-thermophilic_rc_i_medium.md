# YAML Record Review: thermophilic_rc_i_medium

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermophilic_rc_i_medium.yaml`
- Started UTC: 2026-09-25T10:24:00Z
- Finished UTC: 2026-09-25T10:29:57Z
- Verdict: needs curation

## Target

- Reviewed generated TOGO/NBRC M1850 record `CultureMech:008425`.
- Media term: `TOGO:M1850`, `Thermophilic RC-I medium`.
- Source claims in the record point to NBRC Medium 1086 and `https://www.nite.go.jp/nbrc/catalogue/NBRCMediumDetailServlet?NO=1086`.

## Validation

- Schema validation: passed with `linkml-validate`; no issues found.
- Strict validation: passed; `/private/tmp/thermophilic_rc_i_medium.strict.tsv` was header-only with 1 line and 0 error rows.
- Reference validation: passed; 0 checks were configured for this record.
- Term validation: passed; only the known `eutils`/`pkg_resources` deprecation warning was emitted.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged YAML.

## Identity and Grounding

- The NBRC Medium 1086 page identifies the recipe as Thermophilic RC-I medium.
- The generated TOGO/NBRC target is stale relative to the repaired `data/normalized_yaml/bacterial/NBRC_1091.yaml` source, whose 2026-09-11 `RESOLVED_NBRC_1091_SCORE15` history entry records grounding of the recovered NBRC Medium 1086 formula.
- The repaired normalized record keeps the main medium, Trace elements solution, and Vitamin solution nested with the source addition volumes of 2 ml/L and 10 ml/L.

## Evidence

- `/private/tmp/nbrc_1086.html` contains the NBRC Medium 1086 main ingredients, instructions, Trace elements solution, and Vitamin solution.
- The source main medium uses 0.5 mg/L resazurin, 1 L distilled water, 2 ml/L Trace elements solution, and 10 ml/L Vitamin solution.
- The Trace elements stock includes 1 L distilled water plus gram-per-liter mineral stock rows, while the Vitamin solution includes mg/L vitamin rows; neither stock is intended to be flattened into the basal medium at its stock concentration.
- Local duplicate detection was run with `rg --no-ignore --hidden` against `data/normalized_yaml` and `data/merge_yaml/merged`, so ignored generated indexes were included in the source search.

## Completeness

- The generated merge has every recognizable NBRC stock row, but it flattens them into the top-level ingredient list.
- The two source stock additions are preserved only as generated `Unknown solution` placeholders with units `G_PER_L` instead of `ML_PER_L`.
- The repaired `NBRC_1091.yaml` normalized source already has the stock hierarchy and source units needed to regenerate a better merge.

## Findings

- Water was summed across the basal recipe and both stocks, producing one top-level `Distilled water` row at 3.0 g/L instead of the basal 1 L plus two nested 1 L stock waters.
- The source 0.5 mg/L resazurin row became 0.5 g/L.
- Trace stock minerals, the trace-stock NaOH pH adjustment, and all Vitamin solution rows were flattened into top-level medium ingredients.
- The Vitamin solution mg/L entries were imported as g/L values, for example biotin 2 g/L and Vitamin B12 0.01 g/L.
- Basal CaCl2 x 2 H2O at 0.1 g/L and trace-stock CaCl2 x 2 H2O at 0.018 g/L were summed into one 0.118 g/L top-level ingredient even though they belong to different compartments.

## Recommended Edits

- Regenerate `thermophilic_rc_i_medium` from the repaired `data/normalized_yaml/bacterial/NBRC_1091.yaml` source rather than from the stale flattened TOGO/NBRC normalized state.
- Keep Trace elements solution and Vitamin solution as nested stock solutions with 2 ml/L and 10 ml/L additions in the main medium.
- Preserve the source units for 0.5 mg/L resazurin and mg/L vitamin stock rows.
- Keep NaOH inside the Trace elements solution preparation context rather than as a variable top-level basal ingredient.

## Follow-up Checks

- Rebuild the merged YAML and confirm that `Trace elements solution` and `Vitamin solution` remain nested, with no vitamin rows in the top-level ingredient list.
- Re-run schema, strict, reference, and term validation on the regenerated record.
- Re-run an exact ignored-inclusive search for `NBRC_1091` and NBRC Medium 1086 to verify no stale flattened NBRC 1086 target remains.

## Additional Notes

None found.
