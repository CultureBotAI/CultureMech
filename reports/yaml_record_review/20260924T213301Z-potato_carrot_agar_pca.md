# YAML Record Review: potato_carrot_agar_pca

- Repository: CultureMech
- Record: data/merge_yaml/merged/potato_carrot_agar_pca.yaml
- Started UTC: 2026-09-24T21:33:01Z
- Finished UTC: 2026-09-24T21:33:01Z
- Verdict: needs curation

## Target

- MediaRecipe ID: CultureMech:007943
- Name: potato_carrot_agar_pca
- Source import: potato_carrot_agar_pca
- Primary external ID: TOGO:M1407
- Maintained input: data/normalized_yaml/bacterial/potato_carrot_agar_pca.yaml

This generated record represents TOGO Medium M1407 / NBRC Medium 2, Potato Carrot Agar (PCA).

## Validation

- Open LinkML validation: passed with no reported issues.
- Strict validation: passed for 1 file with 0 error rows; `/private/tmp/potato_carrot_agar_pca.strict.tsv` is header-only.
- Reference validation: passed for 1 file with 0 reference checks.
- Term validation: passed.
- Embedded curation history: Not checked: `just validate-history` validates standalone `history/`, not `MediaRecipe.curation_history` entries inside merged YAML.

## Identity and Grounding

The record has the correct TOGO M1407 / NBRC 2 identity. TOGO and NBRC both name the source `Potato Carrot Agar (PCA)` and list 20 g potato, 20 g carrot, 1 L distilled water, 20 g agar, pH 6.0, and a preparation instruction to peel and slice the potato and carrot, boil 20 min with 1 L distilled water, mash and strain through a muslin bag, adjust pH, add agar, make up to 1 L, and autoclave.

Exact ignored-file searches across `data` for `TOGO:M1407`, `medium/M1407`, `gm_id=M1407`, `NBRC_M2`, `NO=2`, and `potato_carrot_agar_pca` found one normalized YAML recipe, this merged YAML record, and generated index/tracking references to that same recipe; no second exact NBRC 2 / TOGO M1407 recipe was found.

## Evidence

- TOGO M1407 imports NBRC_M2 and links the NBRC Medium 2 page.
- TOGO M1407 lists 1 L distilled water, 20 g carrot, 20 g agar, and 20 g potato, followed by `pH 6.0` and the NBRC preparation instruction.
- NBRC 2 lists the same 20 g potato, 20 g carrot, 1 L distilled water, 20 g agar, pH 6.0, and preparation text.

## Completeness

The generated record is incomplete as a source-faithful NBRC 2 representation:

- The 1 L distilled water row is imported as `1 G_PER_L`.
- The source pH 6.0 is absent.
- The source preparation instruction is absent.

## Findings

1. Major: The maintained normalized input and generated merge misrepresent the 1 L water row as 1 G_PER_L. Future repair belongs in `data/normalized_yaml/bacterial/potato_carrot_agar_pca.yaml` or the TOGO importer.
2. Major: The maintained input and generated merge omit NBRC 2's pH 6.0 and preparation instruction. Future repair belongs in the same normalized TOGO M1407 record.

## Recommended Edits

- Rebuild `data/normalized_yaml/bacterial/potato_carrot_agar_pca.yaml` from TOGO M1407 / NBRC 2 with 1000 ML_PER_L distilled water, `ph_value: 6.0`, and a preparation step covering the 20 min boil, muslin-bag strain, pH adjustment, agar addition, 1 L final volume make-up, and autoclaving.
- Regenerate `data/merge_yaml/merged/potato_carrot_agar_pca.yaml` from the corrected normalized record.

## Follow-up Checks

- Re-run open schema, strict, term, and reference validation after regeneration.
- Run exact ignored-file searches for `TOGO:M1407`, `NBRC_M2`, and `NO=2` with ignored files included before adding any new NBRC 2 import.
- Spot-check the rendered TOGO M1407 page to ensure the water unit, pH 6.0, and preparation instruction are visible.

## Additional Notes

None found.
