# YAML Record Review: de_man_rogosa_sharpe_broths_supplemented_with_0_05_l_cysteine_hcl

- Repository: CultureMech
- Record: data/merge_yaml/merged/de_man_rogosa_sharpe_broths_supplemented_with_0_05_l_cysteine_hcl.yaml
- Started UTC: 2026-09-22T13:47:25Z
- Finished UTC: 2026-09-22T13:50:21Z
- Verdict: needs curation

## Target

Reviewed generated record `data/merge_yaml/merged/de_man_rogosa_sharpe_broths_supplemented_with_0_05_l_cysteine_hcl.yaml` with generated identifier `CultureMech:009351`, media term `TOGO:M2803`, original name `de Man-Rogosa-Sharpe broths supplemented with 0.05% l-cysteine . HCl`, category `bacterial`, and one merged source, `de_man_rogosa_sharpe_broths_supplemented_with_0_05_l_cysteine_hcl`.

## Validation

- LinkML open-schema validation: passed.
- Strict validation: passed with 0 error rows in `/private/tmp/de_man_rogosa_sharpe_broths_supplemented_with_0_05_l_cysteine_hcl.strict.tsv`.
- Reference validation: passed with 0 references checked.
- Term validation: passed.
- Embedded curation history: not checked; `just validate-history` targets standalone files under `history/`, not `MediaRecipe.curation_history` blocks.

## Identity and Grounding

TOGO M2803 describes Difco MRS broth supplemented with 0.05% final-concentration L-cysteine HCl for bifidobacterial cultivation at 37 C under anaerobic BBL Anaerobic system conditions.

The generated identity is correct, but the generated formula is stale relative to the repaired maintained source. `data/normalized_yaml/bacterial/de_man_rogosa_sharpe_broths_supplemented_with_0_05_l_cysteine_hcl.yaml` now records the Difco base as 1000 ml/L of `CultureMech:009062`, the cysteine as the added supplement, the 37 C anaerobic incubation conditions, explicit M2803 reference, and `SUPPLEMENTED_VARIANT` parentage.

An exact gitignore-independent search for `M2803` and `de_man_rogosa_sharpe_broths_supplemented_with_0_05_l_cysteine_hcl` across normalized YAML, merged YAML, and prior YAML record reviews found only the maintained source, its TOGO M2489 parent link, and this generated target.

## Evidence

The TOGO API lists two final rows: `MRS broth (Difco)` at 1 L and `L-cysteine . HCl` at 0.05%. Its source comment specifies that the 0.05% L-cysteine HCl is the final concentration and that cultures were grown at 37 C under anaerobic BBL Anaerobic system conditions.

## Completeness

The generated target has both source rows but keeps the imported default for the base broth, `1 G_PER_L`, instead of preserving the 1 L prepared-base volume. It also lacks the September 2026 curation that grounded L-cysteine HCl, linked the Difco MRS broth parent, captured the 37 C anaerobic cultivation condition, and stored a real reference.

## Findings

1. **The base Difco broth has the wrong unit.** TOGO M2803 lists `MRS broth (Difco)` as 1 L of prepared base medium; the generated YAML represents it as `1 G_PER_L`.

2. **The generated output is stale relative to the repaired normalized source.** The generated file predates the 2026-09-08 repair that changed the base to `1000 ML_PER_L`, linked it to `CultureMech:009062`, added `SUPPLEMENTED_VARIANT` parent metadata, grounded L-cysteine hydrochloride to `CHEBI:91247`, and added the M2803 reference.

3. **Growth-condition metadata is missing.** The TOGO source comment records routine cultivation at 37 C under anaerobic BBL Anaerobic system conditions; the maintained source now stores `temperature_value: 37.0` and `incubation_atmosphere: ANAEROBIC`, but the generated record omits them.

## Recommended Edits

- Regenerate this record from `data/normalized_yaml/bacterial/de_man_rogosa_sharpe_broths_supplemented_with_0_05_l_cysteine_hcl.yaml`.
- Confirm the regenerated output keeps the Difco MRS broth as `1000 ML_PER_L` of `CultureMech:009062` and keeps L-cysteine HCl as a 0.05% final supplement.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation after regeneration.
- Confirm the generated record includes the M2803 reference and the 37 C anaerobic conditions.

## Additional Notes

The review used gitignore-independent `rg --no-ignore --hidden` searches for `M2803` and `de_man_rogosa_sharpe_broths_supplemented_with_0_05_l_cysteine_hcl`, so ignored files were included in the duplicate/source scan.
