# YAML Record Review: de_man_rogosa_sharpe_mrs_broth_biokar_diagnostic

- Repository: CultureMech
- Record: data/merge_yaml/merged/de_man_rogosa_sharpe_mrs_broth_biokar_diagnostic.yaml
- Started UTC: 2026-09-22T13:52:58Z
- Finished UTC: 2026-09-22T13:55:37Z
- Verdict: needs curation

## Target

Reviewed generated record `data/merge_yaml/merged/de_man_rogosa_sharpe_mrs_broth_biokar_diagnostic.yaml` with generated identifier `CultureMech:008813`, media term `TOGO:M2225`, original name `De Man-Rogosa-Sharpe (MRS) broth (Biokar Diagnostic)`, category `bacterial`, and one merged source, `de_man_rogosa_sharpe_mrs_broth_biokar_diagnostic`.

## Validation

- LinkML open-schema validation: passed.
- Strict validation: passed with 0 error rows in `/private/tmp/de_man_rogosa_sharpe_mrs_broth_biokar_diagnostic.strict.tsv`.
- Reference validation: passed with 0 references checked.
- Term validation: passed.
- Embedded curation history: not checked; `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` blocks.

## Identity and Grounding

TOGO M2225 is the Biokar Diagnostic MRS broth product recipe. The formula is 55.3 g De Man-Rogosa-Sharpe broth in 1 L distilled water, with ready-to-use pH 6.4 +/- 0.2 at 25 C and anaerobic 24 h cultivation at 37 C described in the source comment.

An exact gitignore-independent search for `M2225`, `Biokar Diagnostic`, and `de_man_rogosa_sharpe_mrs_broth_biokar_diagnostic` across normalized YAML, merged YAML, and prior YAML record reviews found the maintained source and this generated target for M2225; it also found `TOGO_M2495_Man-Rogosa-Sharpe_MRS_broth.yaml`, a related but separate Biokar product record.

## Evidence

The TOGO API reports `ph` `6.4 +/- 0.2`, `Distilled water` at 1 L, and `De Man-Rogosa-Sharpe (MRS) broth (Biokar Diagnostic)` at 55.3 g. Its source comment states the bacteria were grown under anaerobic Gaspak H2/CO2 conditions for 24 h at 37 C.

## Completeness

The generated target keeps the 55.3 g/L powder row but stores the 1 L water row as `1 G_PER_L` and omits the pH range, temperature, anaerobic cultivation condition, preparation text, explicit source reference, and 2026-09-10 repair from the maintained normalized source.

## Findings

1. **The solvent row has the wrong unit.** TOGO M2225 lists one liter of distilled water; the generated record stores it as `1 G_PER_L`.

2. **The pH range is missing.** TOGO gives ready-to-use pH 6.4 +/- 0.2, and the maintained source stores `ph_range` 6.2-6.6, but the generated output has no pH field.

3. **The generated output omits source condition metadata and the repair.** The current normalized owner has a 2026-09-10 repair, `temperature_value: 37.0`, and a preparation step for anaerobic 24 h cultivation at 37 C. The generated record is still the pre-repair import.

## Recommended Edits

- Regenerate this record from `data/normalized_yaml/bacterial/de_man_rogosa_sharpe_mrs_broth_biokar_diagnostic.yaml`.
- Confirm distilled water becomes `1000 ML_PER_L`, the Biokar powder remains `55.3 G_PER_L`, and the pH 6.2-6.6 range is present.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Compare the Biokar M2225 record with TOGO M2495 only for shared commercial-product handling; do not merge them without source evidence because M2225 records 55.3 g/L powder and M2495 is a different TOGO source.

## Additional Notes

The review used gitignore-independent `rg --no-ignore --hidden` searches for `M2225`, `Biokar Diagnostic`, and `de_man_rogosa_sharpe_mrs_broth_biokar_diagnostic`, so ignored files were included in the duplicate/source scan.
