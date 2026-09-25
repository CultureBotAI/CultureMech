# YAML Record Review: BARBOUR-SFOENNER-KELLY (BSK) II MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/barbour_sfoenner_kelly_bsk_ii_medium.yaml`
- Started UTC: 2026-09-21T18:32:20Z
- Finished UTC: 2026-09-21T18:33:46Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:002533` |
| Merged record | `data/merge_yaml/merged/barbour_sfoenner_kelly_bsk_ii_medium.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/barbour_sfoenner_kelly_bsk_ii_medium.yaml` |
| Source identity | JCM Medium J173 / MediaDive `mediadive.medium:J173` |
| Merge status | Generated from one normalized source, `barbour_sfoenner_kelly_bsk_ii_medium` |

The reviewed record is the generated merge for JCM GRMD 173, "BARBOUR-SFOENNER-KELLY (BSK) II MEDIUM". A gitignore-independent search for `CultureMech:002533`, the record stem, the exact JCM title, `mediadive.medium:J173`, `JCM Medium J173`, and `GRMD=173` across `data`, `history`, `src`, `scripts`, `reports/yaml_record_review`, and `.claude` found one live normalized owner plus the generated merge, registry/index rows, and import-tracking rows. It found no prior review report for this record. The search included ignored files.

## Validation

| Check | Result |
| --- | --- |
| Open schema | Passed with `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/barbour_sfoenner_kelly_bsk_ii_medium.yaml`. |
| Strict schema | Passed with `scripts/validate_strict.py`; 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference snippets | Passed with `linkml-reference-validator validate data ...`; 1 file validated, 0 snippet checks, all validations passed. |
| Term labels | Passed with `linkml-term-validator validate-data ... --labels -c conf/oak_config.yaml`. |
| Embedded curation history | Not checked: no documented focused validator exists for embedded `MediaRecipe.curation_history` on one generated merge record; `just validate-history` targets standalone history files. |

The direct `just` validators remain unavailable in this checkout because project `uv` tries to build `llvmlite==0.46.0` under Python 3.13 and exits inside `setuptools`. I used the no-project Python 3.11 validator workaround for the focused schema, strict, reference, and term checks above.

## Identity and Grounding

The record identity is correct: JCM GRMD 173 names the recipe `BARBOUR-SFOENNER-KELLY (BSK) II MEDIUM`, matching `mediadive.medium:J173`, `CultureMech:002533`, the original name, and the JCM link in `notes`.

Several ingredient identities are not correct or not grounded to the exact local rows:

| Ingredient | Current state | Source or local index state |
| --- | --- | --- |
| CMRL 1066 | Stored as `CMRL 1066`. | JCM specifies `CMRL 1066 with glutamate (Sigma)`. The local MIM index has `CMRL 1066` as an unmapped exact row, so the ungrounded base material is acceptable, but the source qualifier is lost. |
| N-Acetyl-D-glucosamine | Grounded to `CHEBI:506227` and legacy `MediaIngredientMech:000994`. | The exact MIM label maps `N-Acetyl-D-glucosamine` to `CHEBI:8006`. |
| HEPES | Grounded to `CHEBI:46756`. | The exact MIM label maps `HEPES` to `CHEBI:42334`. |
| TC Yeastolate | Missing as such. | JCM specifies `TC Yeastolate (BD-Difco)`, not a generic 2 g/L `Yeast extract` row. |
| Tryptone / 5 g/L Yeast extract / Sodium chloride | Present with LB Miller supplier metadata. | JCM GRMD 173 does not list these LB Medium constituents. |

## Evidence

The JCM page supports a two-solution recipe, not a flat one. Solution A is a 500 ml filtered stock containing CMRL 1066 with glutamate, bovine serum albumin Fraction V, HEPES, trisodium citrate, glucose, sodium pyruvate, N-acetyl-D-glucosamine, NaHCO3, TC Yeastolate, and distilled water. Solution B is a 100 ml stock containing Neopeptone, gelatin, and distilled water. The method then autoclaves Solution B, mixes Solutions A and B, and adds 40 ml heat-inactivated sterile rabbit serum.

The generated record has no `solutions` blocks and no rabbit-serum row. It normalizes Solution A to 500 ml stock strength and Solution B to 100 ml stock strength, then stores those as final top-level `G_PER_L` values. That is misleading for CMRL 1066, HEPES, trisodium citrate, glucose, sodium pyruvate, N-acetyl-D-glucosamine, NaHCO3, Neopeptone, and gelatin.

The record omits source components: bovine serum albumin Fraction V, Solution A distilled water, Solution B distilled water, and the 40 ml heat-inactivated sterile rabbit serum. It also collapses `TC Yeastolate (BD-Difco)` into an unsupported second `Yeast extract` row while a first, unrelated 5 g/L `Yeast extract` row has been added from LB Miller metadata.

The pH 7.6 and the filtration, autoclaving, and heat-inactivation instructions are all supported by the JCM page. The `0.22 um` filter size is only present as mojibake in the generated text because the JCM micro symbol was imported with the wrong encoding.

## Completeness

The source formulation is not complete enough to use because it loses all three source compartments: filtered Solution A, autoclaved Solution B, and the post-mix rabbit-serum addition. The record also contains unsupported LB Medium product notes and LB-derived ingredients.

The absent target-organism, atmosphere, incubation-temperature, and storage fields are optional and not automatically defects for this JCM recipe.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | The JCM Solution A, Solution B, and rabbit-serum boundaries are flattened away. | JCM gives a 500 ml Solution A, a 100 ml Solution B, and a 40 ml sterile rabbit-serum addition; the record has no `solutions` and represents the 500 ml and 100 ml stock strengths as top-level final `G_PER_L` rows. | `data/normalized_yaml/bacterial/barbour_sfoenner_kelly_bsk_ii_medium.yaml` |
| Major | Three LB Miller rows and all LB commercial-product metadata are unsupported. | JCM GRMD 173 does not list 10 g/L Tryptone, 5 g/L generic Yeast extract, or 10 g/L Sodium chloride and says nothing about LB Medium, Sigma L3522, BD 244520, or laboratorynotes.com. | `data/normalized_yaml/bacterial/barbour_sfoenner_kelly_bsk_ii_medium.yaml` |
| Major | Required JCM components are missing or collapsed to a different material. | Bovine serum albumin Fraction V, both distilled-water rows, and 40 ml heat-inactivated sterile rabbit serum are absent; `TC Yeastolate (BD-Difco)` is represented only as generic 2 g/L `Yeast extract`. | `data/normalized_yaml/bacterial/barbour_sfoenner_kelly_bsk_ii_medium.yaml` |
| Major | Two grounded rows disagree with exact local MIM labels. | The local MIM index maps exact `N-Acetyl-D-glucosamine` to `CHEBI:8006`, but the record uses `CHEBI:506227` plus a legacy MIM field; exact `HEPES` maps to `CHEBI:42334`, but the record uses `CHEBI:46756`. | `data/normalized_yaml/bacterial/barbour_sfoenner_kelly_bsk_ii_medium.yaml` |
| Minor | The filter-size text is mojibaked. | JCM encodes the filter pore size as `0.22 &#181;m`; the record stores replacement-character mojibake after `0.22 `. | `data/normalized_yaml/bacterial/barbour_sfoenner_kelly_bsk_ii_medium.yaml` |

## Recommended Edits

1. Remove the LB Miller note block, LB supplier metadata, and unsupported Tryptone, 5 g/L Yeast extract, and Sodium chloride rows.
2. Replace the flat formula with source-scoped `Solution A` and `Solution B` records or nested `solutions`, preserving 500 ml and 100 ml stock preparation volumes instead of publishing those concentrations as final medium amounts.
3. Add bovine serum albumin Fraction V, the two distilled-water rows, and the 40 ml heat-inactivated sterile rabbit serum addition.
4. Restore `TC Yeastolate (BD-Difco)` as its own unresolved ingredient unless an exact local mapping is added; do not collapse it to generic yeast extract.
5. Change N-Acetyl-D-glucosamine and HEPES to the exact local MIM groundings, and migrate the lingering `mediaingredientmech_term` on N-Acetyl-D-glucosamine.
6. Re-encode the filter-size preparation text as ASCII `0.22 um` or valid Unicode before regeneration.

## Follow-up Checks

1. Re-run the focused schema, strict, term, and reference validators on `data/merge_yaml/merged/barbour_sfoenner_kelly_bsk_ii_medium.yaml` after regeneration.
2. Re-open JCM GRMD 173 and compare every regenerated ingredient to its Solution A, Solution B, or rabbit-serum section.
3. Re-run the duplicate-ingredient or merged-duplicate audit and confirm `CultureMech:002533` is no longer flagged for the unsupported 5 g/L and 2 g/L `Yeast extract` duplicate.

## Additional Notes

The exact import-tracking row for this record already flags the duplicate `Yeast extract` values at 5 g/L and 2 g/L. This review confirms that the 5 g/L row is LB contamination and the 2 g/L row is a lossy rendering of JCM's `TC Yeastolate (BD-Difco)`.
