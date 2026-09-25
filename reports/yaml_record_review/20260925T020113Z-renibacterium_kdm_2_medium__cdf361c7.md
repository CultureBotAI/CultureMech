# YAML Record Review: renibacterium_kdm_2_medium__cdf361c7

- Repository: CultureMech
- Record: `data/merge_yaml/merged/renibacterium_kdm_2_medium__cdf361c7.yaml`
- Started UTC: 2026-09-25T01:59:50Z
- Finished UTC: 2026-09-25T02:01:13Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:009669` for TOGO Medium M322 / `TOGO:M322`, generated from `data/normalized_yaml/bacterial/TOGO_M322_Renibacterium_KDM-2_Medium.yaml`.

## Validation

- Open schema validation: passed with `No issues found`.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

TOGO M322 imports JCM Medium 327. Narrow ignored-inclusive searches found `id: TOGO:M322` in exactly the M322 owner and this generated target, and found the tab-delimited `TOGO:M322` manifest row without including neighboring M3220-series IDs.

## Evidence

JCM Medium 327 lists 10.0 g Bacto peptone (BD-Difco), 0.5 g yeast extract (BD-Difco), 1.0 g L-Cysteine.HCl.H2O, 15.0 g agar, 800 ml distilled water, and 200 ml fetal bovine serum. Its preparation note dissolves peptone, yeast extract, and cysteine in 800 ml distilled water, adjusts to pH 6.5 with NaOH, adds agar and heat, then cools after autoclaving and adds serum. TOGO M322 carries the same masses, volume amounts, pH 6.5, and preparation comment.

## Completeness

The generated record has the JCM ingredient set, but two volume rows are normalized as masses and the source pH/preparation evidence is missing.

## Findings

- The owner and generated target record `Distilled water` as `800 G_PER_L` and `Fetal bovine serum` as `200 G_PER_L`. JCM 327 and TOGO M322 state these two amounts in milliliters, not grams.
- The generated target lacks `ph_value: 6.5` even though TOGO M322 exposes pH 6.5 and the JCM preparation adjusts to that pH with NaOH.
- The generated target omits the JCM preparation logic: dissolve the peptone, yeast extract, and cysteine in water; adjust with NaOH; add agar and heat; autoclave; cool; then add serum.
- `L--Cysteine.HCl.H2O` should be normalized from the source's hydrate spelling without the doubled hyphen artifact.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/TOGO_M322_Renibacterium_KDM-2_Medium.yaml` so distilled water is 800 `ML_PER_L`, fetal bovine serum is 200 `ML_PER_L`, pH 6.5 is represented, and the JCM preparation note is structured.
- Normalize the cysteine hydrochloride hydrate label while retaining `CHEBI:91248`.
- Add a TOGO/JCM reference and a curation-history entry, then regenerate `data/merge_yaml/merged`.

## Follow-up Checks

- Confirm the regenerated target keeps the four mass rows unchanged: 10 g/L Bacto peptone, 0.5 g/L yeast extract, 1 g/L L-cysteine hydrochloride hydrate, and 15 g/L agar.
- Confirm the regenerated target has 800 ml/L distilled water, 200 ml/L fetal bovine serum, and pH 6.5.
- Re-run open schema, strict, reference, and term validation for the regenerated target.

## Additional Notes

NaOH is acceptable as a variable pH-adjuster because JCM 327 states the target pH but no final NaOH concentration.
