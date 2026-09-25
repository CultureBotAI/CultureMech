# YAML Record Review: thermoproteus_neutrophilus_medium__9b901d75

- Repository: CultureMech
- Record: `data/merge_yaml/merged/thermoproteus_neutrophilus_medium__9b901d75.yaml`
- Started UTC: 2026-09-25T10:39:00Z
- Finished UTC: 2026-09-25T10:42:23Z
- Verdict: needs curation

## Target

- Reviewed generated TOGO M1633 record `CultureMech:008188`.
- Media term: `TOGO:M1633`, `Thermoproteus neutrophilus Medium`.
- Source claims in the record point to NBRC Medium 836.

## Validation

- Schema validation: passed with `linkml-validate`; no issues found.
- Strict validation: passed; `/private/tmp/thermoproteus_neutrophilus_medium__9b901d75.strict.tsv` was header-only with 1 line and 0 error rows.
- Reference validation: passed; 0 checks were configured for this record.
- Term validation: passed; only the known `eutils`/`pkg_resources` deprecation warning was emitted.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/` records, not `MediaRecipe.curation_history` blocks in merged YAML.

## Identity and Grounding

- NBRC Medium 836 identifies Thermoproteus neutrophilus Medium.
- TOGO M1633 cites `NBRC_M836` and imports the same formulation.
- NBRC 836 is a full expanded formula rather than the JCM 195 formula that references Modified Brock salt base.

## Evidence

- `/private/tmp/nbrc_836.html` lists the NBRC 836 ingredient table, including 1 L distilled water, trace salts at mg/L scale, 25 mg/L Na2S2O4, 0.5 mg/L resazurin, and the pH 6.5 H2/CO2 preparation.
- `/private/tmp/togo_M1633.json` preserves the same source quantities and comments from NBRC.
- Local duplicate detection was rerun with `rg --no-ignore --hidden` against exact TOGO M1633 and JCM 195 identifiers, so ignored generated indexes were included.

## Completeness

- The generated record includes all recognizable NBRC ingredient names.
- The source 1 L distilled-water row is normalized as 1 g/L.
- The source milligram rows are present as g/L values.
- The NBRC preparation text and pH 6.5 are absent from the generated record.

## Findings

- Resazurin 0.5 mg/L became 0.5 g/L.
- Sodium dithionite 25 mg/L became 25 g/L.
- Trace salts were imported at 1000x their source values, for example MnCl2 x 4 H2O 1.8 g/L instead of 0.0018 g/L and Na2B4O7 x 10 H2O 4.5 g/L instead of 0.0045 g/L.
- Distilled water is represented as 1 g/L instead of the source 1 L basis.
- Source H2/CO2 and N2 preparation gases became top-level variable gas ingredients.

## Recommended Edits

- Repair `data/normalized_yaml/archaea/TOGO_M1633_Thermoproteus_neutrophilus_Medium.yaml` so all mg rows are normalized to the correct g/L scale.
- Preserve the 1 L water basis and pH 6.5.
- Move gas-phase terms into preparation context and preserve the NBRC anaerobic preparation text.

## Follow-up Checks

- Rebuild the merged YAML and confirm no trace salts or sodium dithionite remain at g/L values copied directly from mg source rows.
- Re-run schema, strict, reference, and term validation on the regenerated NBRC 836 target.
- Re-run an exact ignored-inclusive search for `TOGO_M1633_Thermoproteus_neutrophilus_Medium`.

## Additional Notes

None found.
