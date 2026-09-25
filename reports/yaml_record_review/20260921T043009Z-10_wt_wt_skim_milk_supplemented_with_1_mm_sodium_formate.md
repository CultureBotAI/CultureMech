# YAML Record Review: 10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml`
- Started UTC: 20260921T042843Z
- Finished UTC: 20260921T043009Z
- Verdict: needs curation

## Target

| Field | Observed value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:009451` |
| Label | `10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate` |
| Category | `bacterial` |
| Generated or maintained | Generated merge artifact under `data/merge_yaml/merged/`; future edits belong in `data/normalized_yaml/bacterial/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml` or merge regeneration |
| Merge owner | `merged_from: [10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate]` |
| Maintained owner | `data/normalized_yaml/bacterial/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml` |

This generated record was merged on Aug 6. The maintained TOGO M2916 input was repaired on Sep 6 with the correct 10% wt/wt skim-milk representation, the source preparation sequence, a sodium formate grounding, a skimmed-milk FoodOn grounding, and a direct TOGO reference.

## Validation

Repository `just` entrypoints were blocked before target-specific validation because the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`.

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml` | Pass |
| Closed schema / strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml --out /private/tmp/culturemech-review-10-wt-skim-milk-formate.strict.tsv --workers 1 --quiet` | Pass; 1 file scanned, 0 files with `ERROR`, TSV at `/private/tmp/culturemech-review-10-wt-skim-milk-formate.strict.tsv` |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 1 file validated, 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merge record; `just validate-history` targets standalone files under `history/` |

The schema validators do not detect the stale percent-to-gram concentration error.

## Identity and Grounding

The source identity is correct:

- TOGO M2916 resolves to `10% (wt/wt) skim milk supplemented with 1 mM sodium formate`.
- `TOGO:M2916` in the generated `media_term` matches that source.

The generated file is stale relative to the maintained owner:

- `Skim milk` is represented as `1 G_PER_L` instead of 10% wt/wt.
- The normalized record now grounds skim milk to `FOODON:03301484` and sodium formate to `CHEBI:62965`; the generated record has neither grounding.
- The generated file has no preparation steps, data-quality flags, or `references`.

## Evidence

Supported by inspected source text:

- TOGO M2916 contains one 10% wt/wt skim-milk component.
- TOGO M2916 contains a 1 mM `Sodium formate (Wako)` component.
- TOGO M2916 says the 10% wt/wt skim milk is heated to 95 C for 2 min and immediately cooled to 43 C.
- TOGO M2916 scopes the 1 mM sodium formate addition to the prepared skim milk medium for monoculture experiments of `L. bulgaricus 2038`.

Unsupported or incomplete in the generated record:

- The generated `Skim milk ` row loses the source `conc_value: 10` / `conc_unit: w/w` and stores only `value: '1'`, `unit: G_PER_L`.
- The generated sodium-formate row preserves 1 mM but lacks the source-scoped Wako vendor note and the monoculture context.
- No generated preparation step covers 95 C heating, 2 min duration, 43 C cooling, or the final formate addition.

## Completeness

- The record is one regeneration behind its authoritative source and should be regenerated from the Sep 6 normalized repair.
- A gitignore-independent `rg --no-ignore --hidden` search over `data/merge_yaml/merged` and `data/normalized_yaml` for `M2916`, the exact `10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate` slug, and the exact 10% wt/wt skim-milk label found only this generated merge, its maintained normalized owner, and normalized index entries.
- Empty optional growth-evidence fields are acceptable: TOGO M2916 itself provides the medium formulation and a monoculture context, not a primary growth-measurement assertion.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The skim-milk concentration is wrong in the generated merge. | TOGO M2916 encodes skim milk as 10% wt/wt; the generated file has `Skim milk ` at `1 G_PER_L`. | `data/normalized_yaml/bacterial/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml` is already repaired; regenerate `data/merge_yaml/merged/`. |
| Major | The generated record is missing all source preparation. | TOGO M2916 says to heat the 10% wt/wt skim milk to 95 C for 2 min, immediately cool to 43 C, and add 1 mM sodium formate for the `L. bulgaricus 2038` monoculture medium; the generated file has no `preparation_steps`. | Regenerate from the maintained normalized owner. |
| Minor | The generated sodium-formate claim drops vendor and scope details. | The live TOGO component says `Sodium formate (Wako)` and the TOGO comment names Wako Pure Chemical Industries in the monoculture addition; the generated row keeps only `Sodium formate (Wako)` with no source note. | Regenerate from the maintained normalized owner, then consider whether the normalized notes should retain the full vendor name. |

## Recommended Edits

1. Regenerate `data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml` from the Sep 6 repaired normalized record.
2. Confirm the regenerated merge carries 10% wt/wt skim milk, 1 mM sodium formate, the three heat/cool/mix steps, FoodOn and CHEBI groundings, the TOGO M2916 reference, and `ingredients_curated`.
3. Preserve source scope in notes: TOGO M2916's 1 mM sodium formate supplement applies to the `L. bulgaricus 2038` monoculture skim-milk medium, while a different 0.1% casein-peptide supplement applies to the `S. thermophilus 1131` monoculture medium.

## Follow-up Checks

- `just verify-merges` to prove this generated artifact is fresh relative to its Sep 6 normalized owner.
- `just validate-strict data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml` after regeneration.
- `just validate-terms data/merge_yaml/merged/10_wt_wt_skim_milk_supplemented_with_1_mm_sodium_formate.yaml` after regeneration to verify the FoodOn and CHEBI labels.
- Manual TOGO M2916 comparison to check the 10% wt/wt amount, 1 mM formate supplement, and 95 C / 43 C preparation sequence.

## Additional Notes

- `linkml-reference-validator` performed zero checks because this stale generated record has no `references` block.
