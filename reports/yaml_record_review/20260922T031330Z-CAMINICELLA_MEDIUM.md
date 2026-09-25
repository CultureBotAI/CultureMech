# YAML Record Review: CAMINICELLA medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/CAMINICELLA_MEDIUM.yaml`
- Started UTC: 2026-09-22T03:10:53Z
- Finished UTC: 2026-09-22T03:13:30Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/CAMINICELLA_MEDIUM.yaml` |
| Maintained canonical owner | `data/normalized_yaml/bacterial/KOMODO_964_CAMINICELLA_medium.yaml` |
| Source-duplicate owner | `data/normalized_yaml/bacterial/caminicella_medium.yaml` |
| ID | `CultureMech:006921` |
| Name | `caminicella_medium` |
| Source accessions | `komodo.medium:964`; `mediadive.medium:964` |
| Category | `bacterial` |
| Medium/composition/state | `COMPLEX` / `UNDEFINED` / `LIQUID` |
| Merge lineage | Two-source merge from `KOMODO_964_CAMINICELLA_medium` and `caminicella_medium` on fingerprint `12cd62364dcffc4835b067ac84b441c5df91e8232a058e795ee49d0d94c52bf7` |

The generated record merged a KOMODO Medium 964 import with a direct DSMZ Medium 964 import and chose the KOMODO owner as canonical. Future corrections belong in the normalized owners or merge rules, followed by regeneration of `data/merge_yaml/merged/CAMINICELLA_MEDIUM.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/CAMINICELLA_MEDIUM.yaml` | Pass: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/CAMINICELLA_MEDIUM.yaml --out /private/tmp/CAMINICELLA_MEDIUM.strict.tsv --workers 1 --quiet` | Pass: 1 file scanned; 0 files with errors; report at `/private/tmp/CAMINICELLA_MEDIUM.strict.tsv`. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/CAMINICELLA_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass: 1 file validated; 0 reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/CAMINICELLA_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass. |
| Embedded curation history | `just validate-history ...` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` events. |

I used offline, no-project `uv` validation because the local project install path currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails inside setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`.

## Identity and Grounding

- **Source identity:** `komodo.medium:964` and `mediadive.medium:964` are two imports of DSMZ Medium 964, `CAMINICELLA MEDIUM`. The merge correctly treats them as source duplicates rather than two biological variants.
- **Duplicate search:** A gitignore-independent `find data/merge_yaml/merged data/normalized_yaml -iname '*caminicella*' -print` found only the generated merge and the two normalized owners for DSMZ/KOMODO 964.
- **Ingredient identity:** The eight non-water rows in the generated record match the DSMZ 964 ingredient names and amounts. `Sea Salt`, `PIPES buffer`, `Peptone`, and `Yeast extract` are intentionally ungrounded or unresolved; `Sulfur` is grounded only to `CHEBI:26833` `sulfur atom`, which is adjacent to DSMZ's powdered sulfur.
- **Classification:** The `COMPLEX` medium type is supported by peptone and yeast extract, but `composition_type: UNDEFINED` underspecifies a recipe whose defined salts and glucose are mixed with undefined peptone/yeast components; `SEMI_DEFINED` would better match the source.

## Evidence

| Claim | Support |
|---|---|
| Ingredient amounts | Mostly supported. DSMZ 964 lists 30 g Sea Salt, 6.05 g PIPES buffer, 5 g D-Glucose, 0.50 ml 0.1% sodium resazurin, 12 g powdered sulfur, 1 g peptone, 0.5 g yeast extract, and 0.5 g Na2S x 9 H2O per 1000 ml. The YAML keeps those eight amounts, with the sodium-resazurin stock converted to 0.0005 g/L of final resazurin. |
| Distilled water | Omitted. DSMZ lists 1000 ml distilled water; neither normalized owner nor the generated merge contains a water row. |
| pH | Partially supported. DSMZ says the final pH is 7.5 and the main record has `ph_value: 7.5`, but DSMZ also states a strain-specific pH 6.5-6.8 variant for DSM 106824 that is not represented. |
| Atmosphere and preparation | Dropped from the generated merge. DSMZ instructs the curator to omit sulfur, peptone, yeast extract, and sulfide from the initial solution, sparge with 80% N2 / 20% CO2 for 30-45 min, adjust pH to 7.2-7.4, dispense under the same gas atmosphere into vessels already containing sulfur, autoclave at 110 C for 20 min, then add peptone, yeast extract, and sulfide from anoxic stocks prepared under 100% N2. The direct DSMZ owner has these details, but the generated merge chose the KOMODO owner and lost them. |
| Aerobic claim | Unsupported. The KOMODO owner says `Aerobic: Yes`, while DSMZ Medium 964 describes an anoxic N2/CO2 workflow and sterile anoxic stock additions. |

## Completeness

- The two source owners merge on matching ingredient/concentration signatures, and their bidirectional `SOURCE_DUPLICATE` relation is appropriate.
- The generated record is incomplete for source-supported preparation because the canonical KOMODO owner has only ingredients.
- The generated record is incomplete for water/final volume because the inspected DSMZ PDF explicitly gives 1000 ml distilled water and final volume 1000 ml.
- Empty target-organism and growth-evidence fields were not treated as defects; the inspected source is a medium recipe PDF.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | DSMZ Medium 964's 1000 ml water row is missing. | The DSMZ PDF lists `Distilled water 1000.00 ml`; both normalized owners and the generated merge have only the eight non-water ingredients. | Add source water in both `KOMODO_964_CAMINICELLA_medium.yaml` and `caminicella_medium.yaml`, or repair the DSMZ/KOMODO import that dropped it. |
| Major | The generated merge dropped the supported anaerobic preparation. | The direct DSMZ owner has the DSMZ sparging, pH-adjustment, 110 C autoclave, and anoxic-stock instructions, but the generated file chose the KOMODO owner and has no `preparation_steps`. | Preserve source-supported preparation when merging the KOMODO and direct DSMZ owners, or copy DSMZ preparation into the KOMODO source duplicate before regeneration. |
| Major | The KOMODO canonical owner carries a false aerobic assertion. | `KOMODO_964_CAMINICELLA_medium.yaml` says `Aerobic: Yes` in `notes`; DSMZ describes 80% N2 / 20% CO2 sparging and additions from sterile anoxic stock solutions under 100% N2. | Remove or correct the KOMODO aerobic metadata in the maintained owner. |
| Major | The DSM 106824 pH variant is not represented. | DSMZ Medium 964 says the default final pH is 7.5 and separately says to adjust the complete medium to pH 6.5-6.8 for DSM 106824; the record has only `ph_value: 7.5`. | Add a bounded `MediaVariant` or strain-scoped note for the DSM 106824 pH variant. |
| Minor | Two ingredients have weak exact identity. | `PIPES buffer` is ungrounded, and `Sulfur` is grounded to `sulfur atom` even though DSMZ specifies powdered sulfur. | Ground PIPES and sulfur to exact material terms where available; otherwise leave unresolved identity explicit. |
| Minor | `composition_type` is too broad. | The source is not wholly undefined: only peptone, yeast extract, and Sea Salt are mixtures. | Classify the normalized owners as semi-defined unless a local rule intentionally classifies all Sea Salt recipes as undefined. |

## Recommended Edits

1. Add the missing 1000 ml distilled water row to both normalized source duplicates, with DSMZ Medium 964 as the source.
2. Preserve the DSMZ preparation sequence in the regenerated merge by copying it to the KOMODO owner or teaching the merge to retain the direct DSMZ owner's `preparation_steps` for source duplicates.
3. Correct the KOMODO `Aerobic: Yes` note so it no longer contradicts the anoxic DSMZ workflow.
4. Represent the DSM 106824 pH 6.5-6.8 variant as a child medium or explicit strain-specific variant.
5. Improve exact ingredient grounding for PIPES buffer and powdered sulfur, then reclassify `composition_type` if this corpus treats salt/peptone/yeast formulations as semi-defined.

## Follow-up Checks

- Rerun open schema, strict schema, term, and reference validation on both normalized owners.
- Regenerate the merged recipe and verify that `data/merge_yaml/merged/CAMINICELLA_MEDIUM.yaml` still has one source-duplicate record but now includes water, source-supported preparation, and no false aerobic assertion.
- Re-run the merge freshness audit so the generated two-source merge is checked against both source owners.
- Manually compare the regenerated YAML against `DSMZ_Medium964.pdf`, including final volume, pH, DSM 106824 pH, and every step of the anaerobic preparation.

## Additional Notes

- Existing `reports/media_content_review_manifest.tsv` marks both normalized source duplicates as `PASS`; the manifest does not currently catch missing water or preparation loss across a source-duplicate merge.
