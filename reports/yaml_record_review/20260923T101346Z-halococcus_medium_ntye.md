# YAML Record Review: halococcus_medium_ntye

- Repository: CultureMech
- Record: `data/merge_yaml/merged/halococcus_medium_ntye.yaml`
- Started UTC: 2026-09-23T10:13:46Z
- Finished UTC: 2026-09-23T10:15:12Z
- Verdict: needs curation

## Target

Generated merged YAML for the direct MediaDive/DSMZ import of `HALOCOCCUS MEDIUM (NTYE)`, DSMZ medium 1549.

## Validation

- LinkML validation: passed for target class `MediaRecipe`.
- Strict validation: passed; `/private/tmp/halococcus_medium_ntye.strict.tsv` contained only the header row.
- Reference validation: passed with 0 checked references.
- Term validation: passed.
- Embedded history validation: Not checked; `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

- The record identity matches MediaDive `mediadive.medium:1549` and DSMZ medium 1549.
- An ignored-file-inclusive exact search for `mediadive.medium:1549` and the DSMZ 1549 PDF found only the expected normalized DSMZ source and this generated merged record.
- An ignored-file-inclusive exact search also found a separate repaired JCM 1324 file mentioning `JCM Medium J1324`; the current JCM 1324 page returns no composition and is not a current duplicate of DSMZ 1549.
- NaCl, MgSO4 x 7 H2O, and KCl are grounded to appropriate CHEBI terms.

## Evidence

- The DSMZ 1549 PDF and the MediaDive 1549 REST payload list NaCl 250 g, MgSO4 x 7 H2O 20 g, KCl 5 g, Tryptone 5 g, Yeast extract 3 g, Distilled water 1000 ml, and pH 7.2.
- The generated record preserves the three salt concentrations, Tryptone 5 g/L, Yeast extract 3 g/L, and `ph_value: 7.2`.
- MediaDive carries the tryptone attribute `BD 211921`, matching the DSMZ PDF text `Tryptone (BD 211921)`.

## Completeness

- Missing ingredient: distilled water at 1000 ml is explicit in both DSMZ and MediaDive but absent from the generated record.
- Missing qualifier: the `BD 211921` product qualifier for Tryptone was dropped.
- Preparation is weakly structured: the only generated preparation step is `MIX` with description `pH 7.2`, even though the scalar pH value already captures the pH target and any procedural entry should be an `ADJUST_PH` operation.

## Findings

1. The generated recipe omits the explicit `Distilled water 1000.0 ml` row. That changes a complete DSMZ formula into a partial solute-only formula.
2. The record loses the `BD 211921` qualifier on Tryptone, removing source-specific product information that distinguishes the undefined nitrogen source.
3. The pH line is misclassified as a `MIX` step. The value itself is correct, but the procedural representation should not describe `pH 7.2` as a mixing operation.

## Recommended Edits

- Add the distilled water solvent at the source amount using the repository's curated final-volume representation.
- Restore the `BD 211921` qualifier on Tryptone.
- Either remove the redundant preparation step or convert it to an `ADJUST_PH` step that states pH 7.2.

## Follow-up Checks

- Re-run LinkML, strict, reference, and term validation after curation.
- Compare the curated output against both the DSMZ PDF and the MediaDive 1549 REST payload to confirm no ingredient row was dropped.
- Re-run an ignored-file-inclusive exact search for `mediadive.medium:1549` and `DSMZ_Medium1549.pdf` after regeneration to confirm the normalized source and merged record remain the only DSMZ 1549 entries.

## Additional Notes

- Empty optional fields were not treated as defects.
- Exact local searches used `rg --no-ignore --hidden`, so ignored files were included.
