# YAML Record Review: potato_dextrose_agar__04581fbb

- Repository: CultureMech
- Record: data/merge_yaml/merged/potato_dextrose_agar__04581fbb.yaml
- Started UTC: 2026-09-24T21:33:45Z
- Finished UTC: 2026-09-24T21:33:45Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:008982
- Name: potato_dextrose_agar
- Source import: TOGO_M23_Potato-Dextrose_Agar
- Primary external ID: TOGO:M23
- Maintained input: data/normalized_yaml/bacterial/TOGO_M23_Potato-Dextrose_Agar.yaml

This generated record represents TOGO Medium M23 / JCM Medium 30, POTATO-DEXTROSE AGAR.

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/potato_dextrose_agar__04581fbb.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the correct TOGO M23 / JCM 30 identity. TOGO M23 imports JCM_M30, and JCM 30 is headed `POTATO-DEXTROSE AGAR`.

Exact ignored-file searches across `data` for `TOGO:M23`, `JCM_M30`, `GRMD=30`, `Potato-Dextrose_Agar`, and `potato_dextrose_agar` found this TOGO normalized recipe and generated merge, plus a separate direct-JCM import of the same JCM 30 formulation. Other Potato Dextrose Agar records were also present, including commercial and fungal branches, but those do not have the exact JCM 30 source.

## Evidence

- TOGO M23 lists 1 L distilled water, 10 g glucose, 15 g agar, and 200 g peeled/cut potato, followed by comments to boil potatoes for 20 min, strain off the pieces through a fine sieve, add glucose and agar, boil until dissolved, avoid new potatoes, adjust pH to 5.4-5.6, and notes that commercial PDA is also available.
- JCM 30 lists the same 200 g potato, 10 g glucose, 15 g agar, 1 L distilled water, pH 5.4-5.6, preparation instructions, and commercial PDA note.

## Completeness

The generated record is incomplete as a source-faithful TOGO M23 / JCM 30 representation:

- The 1 L distilled water row is imported as `1 G_PER_L`.
- The pH 5.4-5.6 range is absent.
- The source preparation instructions and commercial-PDA note are absent.
- The TOGO and direct-JCM imports of the same JCM 30 formulation remain split.

## Findings

1. Major: The maintained TOGO M23 input and generated merge misrepresent the source 1 L distilled water as 1 G_PER_L. Future repair belongs in `data/normalized_yaml/bacterial/TOGO_M23_Potato-Dextrose_Agar.yaml` or the TOGO importer.
2. Major: The maintained input and generated merge omit JCM 30's pH 5.4-5.6, preparation instruction, and commercial-PDA note.
3. Major: The TOGO M23 import and direct JCM 30 import remain split even though both point at the same JCM GRMD=30 source.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/TOGO_M23_Potato-Dextrose_Agar.yaml` from TOGO M23 / JCM 30 with 1000 ML_PER_L distilled water, pH 5.4-5.6, and the boil, sieve, glucose/agar addition, and no-new-potatoes preparation instructions.
- Reconcile the TOGO M23 normalized record with `data/normalized_yaml/bacterial/potato_dextrose_agar.yaml` so JCM 30 no longer generates two separate PDA records.
- Regenerate `data/merge_yaml/merged` after the maintained inputs are repaired and reconciled.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `TOGO:M23`, `JCM_M30`, and `GRMD=30` with ignored files included to verify the TOGO and direct JCM branches are reconciled or intentionally linked.
- Spot-check the regenerated JCM 30 page to verify the 1 L water row, pH 5.4-5.6, and Potato-Dextrose Agar preparation text render.

## Additional Notes

None found.
