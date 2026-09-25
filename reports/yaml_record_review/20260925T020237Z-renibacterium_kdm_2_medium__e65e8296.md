# YAML Record Review: renibacterium_kdm_2_medium__e65e8296

- Repository: CultureMech
- Record: `data/merge_yaml/merged/renibacterium_kdm_2_medium__e65e8296.yaml`
- Started UTC: 2026-09-25T02:01:25Z
- Finished UTC: 2026-09-25T02:02:37Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:002685` for JCM Medium J327 / `mediadive.medium:J327`, generated from `data/normalized_yaml/bacterial/renibacterium_kdm_2_medium.yaml`.

## Validation

- Open schema validation: passed; `linkml-validate` exited 0 with no diagnostics.
- Strict validation: passed; `scripts/validate_strict.py` reported 0 errors and wrote only the TSV header.
- Reference validation: passed; 0 checks.
- Term validation: passed with the known `eutils` / `pkg_resources` deprecation warning.
- Embedded history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` in merged YAML.

## Identity and Grounding

Exact ignored-inclusive searches found `mediadive.medium:J327` only on the direct JCM owner, this generated target, and the manifest row among the searched data and report paths. Exact `GRMD=327` searches found that `data/normalized_yaml/bacterial/TOGO_M322_Renibacterium_KDM-2_Medium.yaml` also imports the same JCM Medium 327 source.

## Evidence

JCM Medium 327 and MediaDive J327 list 10 g/L Bacto peptone, 0.5 g/L yeast extract, 1 g/L L-Cysteine HCl x H2O, 15 g/L agar, 800 ml distilled water, 200 ml fetal bovine serum, and pH 6.5. The JCM/MediaDive preparation step dissolves peptone, yeast extract, and cysteine in 800 ml water, adjusts to pH 6.5 with NaOH, adds agar with heat, autoclaves, cools to 45 C, and adds serum.

## Completeness

The direct JCM generated target carries the pH, four mass ingredients, and the source preparation text, but it omits the distilled water ingredient and assigns a mass unit to a volume-only serum amount.

## Findings

- The `Distilled water` row is missing entirely even though JCM 327 and MediaDive J327 list 800 ml distilled water as a recipe component.
- `Fetal bovine serum` is represented as `200 G_PER_L`, but the JCM/MediaDive source amount is 200 ml.
- The generated target is not source-linked or merged with TOGO M322, even though TOGO M322 imports the same JCM GRMD 327 page.

## Recommended Edits

- Repair `data/normalized_yaml/bacterial/renibacterium_kdm_2_medium.yaml` so distilled water is present as 800 `ML_PER_L` and fetal bovine serum is 200 `ML_PER_L`.
- Add a structured reference to the JCM GRMD 327 page and a repair history entry.
- Source-merge or explicitly source-link the direct MediaDive J327 owner with the TOGO M322 owner for the same JCM medium, then regenerate `data/merge_yaml/merged`.

## Follow-up Checks

- Confirm the regenerated direct JCM target includes exactly the six JCM/MediaDive recipe rows, including the two volume rows.
- Confirm JCM J327 and TOGO M322 no longer emit as unlinked duplicates.
- Re-run open schema, strict, reference, and term validation for the regenerated target.

## Additional Notes

The source gives NaOH only as an adjustment reagent for pH 6.5, so it can remain in preparation text or be kept as a variable pH-adjuster if this owner is merged with TOGO M322.
