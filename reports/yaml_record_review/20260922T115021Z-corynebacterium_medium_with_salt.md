# YAML Record Review: CORYNEBACTERIUM medium WITH SALT

- Repository: CultureMech
- Record: `data/merge_yaml/merged/corynebacterium_medium_with_salt.yaml`
- Started UTC: 2026-09-22T11:50:21Z
- Finished UTC: 2026-09-22T11:50:21Z
- Verdict: needs curation

## Target

Reviewed generated record `CultureMech:004582` / `corynebacterium_medium_with_salt`, emitted from a merge of DSMZ/KOMODO Medium 229 with DSMZ/KOMODO Medium 53 records and three KOMODO strain-specific Medium 53 records:

- `KOMODO_229_CORYNEBACTERIUM_medium_WITH_SALT`
- `KOMODO_53_CORYNEBACTERIUM_AGAR`
- `corynebacterium_agar`
- `corynebacterium_medium_with_salt`
- `medium_53_modified_for_dsm_16375`
- `medium_53_modified_for_dsm_16377`
- `medium_53_modified_for_dsm_16378`

## Validation

- Open schema validation passed for `MediaRecipe`.
- Strict validation passed and wrote `/private/tmp/corynebacterium_medium_with_salt.strict.tsv`.
- LinkML reference validation passed with zero checks.
- LinkML term validation passed.
- Embedded `curation_history` was not separately checked because the available `validate-history` target validates standalone files under `history/`, not history entries embedded in generated `MediaRecipe` YAML.

## Identity and Grounding

The canonical generated identity points to KOMODO Medium 229 / DSMZ Medium 229, named `CORYNEBACTERIUM medium WITH SALT`. That is a different recipe from DSMZ Medium 53, `CORYNEBACTERIUM AGAR`.

The source PDFs distinguish the two records:

- DSMZ Medium 53 lists casein peptone 10 g/L, yeast extract 5 g/L, glucose 5 g/L, NaCl 5 g/L, agar 15 g/L, distilled water 1000 ml, and pH 7.2 to 7.4.
- DSMZ Medium 229 is defined as "To medium 53 add 6% NaCl."

Because Medium 229 is Medium 53 plus an additional 6% NaCl, the generated 65 g/L NaCl formula is a valid expansion for Medium 229. However, DSMZ/KOMODO Medium 53 itself has only 5 g/L NaCl and should remain a separate parent formula.

## Evidence

Primary source checks:

- `/private/tmp/DSMZ_Medium229.txt` extracted from `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium229.pdf`.
- `/private/tmp/DSMZ_Medium53.txt` extracted from `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium53.pdf`.

Local normalized owner checks:

- `data/normalized_yaml/bacterial/corynebacterium_medium_with_salt.yaml` is the DSMZ 229 owner. It has 65 g/L NaCl, pH 7.2 to 7.4, and only one source-duplicate child, `KOMODO_229_CORYNEBACTERIUM_medium_WITH_SALT.yaml`.
- `data/normalized_yaml/bacterial/corynebacterium_agar.yaml` is the DSMZ 53 owner. It has 5 g/L NaCl, pH 7.2 to 7.4, and only one source-duplicate child, `KOMODO_53_CORYNEBACTERIUM_AGAR.yaml`.
- `data/normalized_yaml/bacterial/medium_53_modified_for_dsm_16375.yaml`, `medium_53_modified_for_dsm_16377.yaml`, and `medium_53_modified_for_dsm_16378.yaml` all cite KOMODO IDs in the `53_*` family and mediadive.medium:53, retain 5 g/L NaCl, and point to the KOMODO Medium 53 record as source duplicates.

## Completeness

The generated Medium 229 ingredient list captures the five non-water constituents for the high-salt DSMZ recipe. It is stale relative to the normalized DSMZ 229 owner because it omits `ph_range` 7.2 to 7.4 and the generated parent/synonym set still crosses the Medium 229 and Medium 53 line.

## Findings

1. Needs curation: the generated record overmerges DSMZ/KOMODO Medium 229 with DSMZ/KOMODO Medium 53 records.

   The generated `merged_from` set includes Medium 53 source records whose normalized NaCl concentration is 5 g/L. Keeping those synonyms under the 65 g/L generated Medium 229 recipe makes the Medium 53 identities look equivalent to the high-salt Medium 229 recipe, even though DSMZ defines Medium 229 as Medium 53 plus extra NaCl.

2. Needs curation: the generated recipe omits the source pH range.

   Both normalized DSMZ owners carry pH 7.2 to 7.4 from the DSMZ formulas, but the generated record has no `ph_range` or pH preparation step.

## Recommended Edits

- Keep `corynebacterium_medium_with_salt.yaml` and `KOMODO_229_CORYNEBACTERIUM_medium_WITH_SALT.yaml` together as DSMZ/KOMODO Medium 229 source duplicates.
- Keep `corynebacterium_agar.yaml`, `KOMODO_53_CORYNEBACTERIUM_AGAR.yaml`, `medium_53_modified_for_dsm_16375.yaml`, `medium_53_modified_for_dsm_16377.yaml`, and `medium_53_modified_for_dsm_16378.yaml` together under DSMZ/KOMODO Medium 53 unless the strain-specific records gain evidence-backed modifications that distinguish them from base Medium 53.
- Prevent the generated merge step from fingerprinting Medium 229 and Medium 53 together solely because Medium 229 expands to Medium 53 plus 6% NaCl.
- Regenerate `data/merge_yaml/merged/corynebacterium_medium_with_salt.yaml` after the upstream relationships are repaired and confirm the Medium 53 names disappear from its `synonyms` and `merged_from` lists.
- Confirm regenerated Medium 229 carries pH 7.2 to 7.4.

## Follow-up Checks

- Re-run open schema, strict, reference, and term validation for the regenerated Medium 229 record.
- Check that the regenerated Medium 53 record remains separate with 5 g/L NaCl.
- Search generated merge output for `medium_53_modified_for_dsm_1637` and verify the three KOMODO records no longer collapse into Medium 229.

## Additional Notes

The relevant Medium 53 searches were rerun with ignored files included via `rg --no-ignore --hidden`; the noisy matches confirmed the normalized Medium 53 family and generated merge references but did not reveal a repaired generated Medium 53/229 split.
