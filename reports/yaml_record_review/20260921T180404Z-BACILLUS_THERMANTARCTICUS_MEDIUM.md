# YAML Record Review: bacillus_thermantarcticus_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml
- Started UTC: 2026-09-21T18:02:20Z
- Finished UTC: 2026-09-21T18:04:04Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml` |
| Generated ID | `CultureMech:006271` |
| Label | `bacillus_thermantarcticus_medium` |
| Source selected by merge | KOMODO Medium 675, `komodo.medium:675` |
| Duplicate parent | `data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml` / DSMZ Medium 675, `mediadive.medium:675` |
| Canonical normalized owner | `data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml` |
| Merge fingerprint | `56fe9506a27a7a4ee8e73e064226121b28ad788ccc037fc1b02f3d05c3ae4f4b` |

The merged artifact is generated from the KOMODO Medium 675 normalized record plus the DSMZ Medium 675 normalized parent. Future fixes belong in `data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml`, `data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml`, or merge generation, followed by regeneration of `data/merge_yaml/merged/`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml` | Passed: no issues found |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml --out /private/tmp/BACILLUS_THERMANTARCTICUS_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 0 checks, all validations passed |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone `history/` files |

## Identity and Grounding

The record identity is sound. DSMZ Medium 675 is `BACILLUS THERMANTARCTICUS MEDIUM`; the KOMODO record states `DSMZ Medium: 675`; and the merged KOMODO/DSMZ parents share the same name, pH 5.6-5.8, liquid state, and three imported non-water ingredients.

The September 2026 local MIM repair grounded `Yeast extract` to `FOODON:03315426` and `Soil extract` to `MICRO:0000457` in both normalized owners. The exact ignored-file-inclusive search of `src/culturemech/data/mediaingredientmech/label_index.csv` found those exact preferred-term mappings, and `NaCl` is grounded as `CHEBI:26710` / sodium chloride.

## Evidence

DSMZ Medium 675 supports the top-level recipe as 6.0 g yeast extract, 3.0 g NaCl, 500.0 ml soil extract, and 500.0 ml distilled water, with pH adjusted to 5.6-5.8. The normalized and generated records correctly retain the yeast extract, NaCl, pH range, and liquid state.

DSMZ Medium 675 does not support `Soil extract` as `500 G_PER_L`; it is a 500 ml liquid component. The maintained MediaDive main-solution capture `data/normalized_yaml/bacterial/mediadive_1426_Main_sol_675.yaml` also carries soil extract as a volume row, though with the legacy unit artifact `PERCENT_V_V`.

DSMZ Medium 80 supports the soil-extract preparation prose copied into the DSMZ normalized parent: sieve air-dried garden soil, autoclave 400 g with 960 ml distilled water at 121 C for one hour, cool and settle, decant the supernatant, filter through paper, autoclave in 200 ml quantities, and store at room temperature until the solution clears by sedimentation. The KOMODO normalized duplicate and generated merge omit those instructions.

## Completeness

Consequential gaps:

- The final medium is missing 500 ml/L distilled water.
- Soil extract has the wrong mass unit; it should be represented as a 500 ml/L volume addition.
- The generated record lacks the DSMZ parent preparation instructions because the merge selected the KOMODO duplicate's sparse preparation payload.

Empty target-organism and explicit growth-evidence fields are not automatically defects for this DSMZ medium recipe. This review checked the source formulation PDFs and did not inspect a primary Bacillus thermantarcticus growth study.

An ignored-file-inclusive prior-report search covered `reports/yaml_record_review` for `BACILLUS_THERMANTARCTICUS_MEDIUM`, `bacillus_thermantarcticus_medium`, `KOMODO_675_BACILLUS_THERMANTARCTICUS_medium`, `CultureMech:006271`, and `CultureMech:001815`; it found no prior report for this record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | `Soil extract` is represented with a mass concentration instead of a volume. | DSMZ Medium 675 prints 500.0 ml soil extract plus 500.0 ml distilled water; both normalized owners and the generated merge encode `Soil extract` as `500 G_PER_L`. | `data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml`; `data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml` |
| Major | The final medium omits distilled water. | DSMZ Medium 675 includes 500.0 ml distilled water. The two normalized Medium 675 owners and the generated merge have no water ingredient. | `data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml`; `data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml` |
| Major | The generated merge loses the soil-extract preparation procedure. | The DSMZ parent records the Medium 80 soil-extract preparation under `preparation_steps`; the KOMODO duplicate and generated merge do not. | `data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml` or `scripts/merge_recipes.py` |

## Recommended Edits

1. In both Medium 675 normalized owners, change `Soil extract` from `500 G_PER_L` to `500.0 ML_PER_L` or the repository's canonical volume unit for ml per liter.
2. Add `Distilled water` as `500.0 ML_PER_L` to both Medium 675 normalized owners.
3. Preserve the DSMZ pH-adjustment and soil-extract preparation notes in the KOMODO Medium 675 duplicate, or update merge generation to keep non-conflicting preparation steps from the DSMZ parent when creating a source-duplicate merge.
4. Regenerate `data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml` after the normalized inputs or merge logic are corrected.

## Follow-up Checks

- Run `just validate data/normalized_yaml/bacterial/bacillus_thermantarcticus_medium.yaml`.
- Run `just validate data/normalized_yaml/bacterial/KOMODO_675_BACILLUS_THERMANTARCTICUS_medium.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Re-run the no-project open-schema, strict, reference, and term validators against the regenerated `data/merge_yaml/merged/BACILLUS_THERMANTARCTICUS_MEDIUM.yaml`.
- Manually compare the regenerated record with DSMZ Medium 675 and DSMZ Medium 80 to confirm 500 ml/L soil extract, 500 ml/L distilled water, pH 5.6-5.8, and the soil-extract preparation instructions survive.

## Additional Notes

One broad ignored-file-inclusive search for Thermantarcticus also included `CultureMech` and therefore matched every normalized index entry; I discarded that noisy output and relied on exact owner paths plus the report-only ignored search above.

`kg_microbe_match: mediadive.medium:74` was left as a low-confidence inherited field during review. It may be a historical cross-link rather than the source identity for DSMZ Medium 675, but it does not drive the generated `media_term` and should be checked only if a future cleanup audits `kg_microbe_match` semantics across generated duplicate merges.
