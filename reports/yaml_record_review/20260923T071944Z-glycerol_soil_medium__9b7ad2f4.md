# YAML Record Review: glycerol_soil_medium__9b7ad2f4

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glycerol_soil_medium__9b7ad2f4.yaml
- Started UTC: 2026-09-23T07:18:24Z
- Finished UTC: 2026-09-23T07:19:44Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:009760` |
| Name | `glycerol_soil_medium` |
| Original name | `Glycerol-Soil Medium` |
| Category | `bacterial` |
| Canonical media term | `TOGO:M379` |
| Merged sources | `TOGO_M379_Glycerol-Soil_Medium` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glycerol_soil_medium__9b7ad2f4.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glycerol_soil_medium__9b7ad2f4.yaml --out /private/tmp/glycerol_soil_medium__9b7ad2f4.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glycerol_soil_medium__9b7ad2f4.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glycerol_soil_medium__9b7ad2f4.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This generated record is the Togo M379 import of JCM Medium 384. It is a source duplicate of the direct MediaDive J384 record, but the generated August 6 records still keep those two branches separate.

A gitignore-independent exact search for `TOGO:M379`, `TOGO:M2317`, `JCM_M384`, `JCM_J384_GLYCEROL-SOIL_MEDIUM`, `TOGO_M379_Glycerol-Soil_Medium`, `TOGO_M2317_Glycerol-Soil_Medium`, `KOMODO_80_GLYCEROL-SOIL_medium`, `mediadive.medium:80`, `komodo.medium:80`, and `glycerol_soil_medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found the expected five maintained parents, four generated records, and source indexes.

Grounding for glycerol, water, and agar is narrow. The September 2026 maintained parent intentionally leaves Bacto peptone and Beef extract ungrounded vendor products and models Soil extract as a nested solution.

## Evidence

Togo M379 / JCM 384 lists 20 g glycerol, 850 ml tap water, 15 g agar, 5 g Bacto peptone (BD-Difco), 3 g Beef extract (BD-Difco), 150 ml Soil extract, and pH 7.0. The Togo source separately lists the Soil extract preparation with 960 ml tap water and 400 g air-dried garden soil.

The generated record has both scopes mixed together. It sums 850 ml final-medium tap water with 960 ml soil-extract tap water into one `1810.0 G_PER_L` Tap water row, keeps the 400 g garden soil as a top-level `400 G_PER_L` ingredient, and keeps Soil extract as `150 G_PER_L` instead of a 150 ml/l solution addition. The maintained Togo M379 parent repaired all of those artifacts on September 11, 2026.

The generated record is also split from the generated MediaDive J384 record for the same JCM Medium 384 formula.

## Completeness

The generated record is stale and not complete enough to use for the JCM 384 formula because the soil-extract stock recipe has been flattened into the final ingredient list and its volume rows have mass units. Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects by themselves for this medium.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Tap-water rows from separate formula scopes were summed and assigned a mass unit. | Togo M379 lists 850 ml tap water in the final medium and 960 ml tap water only inside Soil extract; the generated row is `1810.0 G_PER_L` Tap water with a duplicate-merge note. | Regenerate from `data/normalized_yaml/bacterial/TOGO_M379_Glycerol-Soil_Medium.yaml`. |
| Major | The Soil extract stock recipe is flattened into the main ingredient list. | The source adds 150 ml Soil extract per final liter and prepares the stock from 400 g garden soil plus 960 ml tap water; the generated record has `Soil extract (See below)` and `air--dried garden soil` as top-level g/l ingredients. | Merge regeneration after the September 11 Togo M379 repair. |
| Major | The JCM 384 formula is split between Togo M379 and MediaDive J384 generated records. | `glycerol_soil_medium__9b7ad2f4.yaml` and `glycerol_soil_medium.yaml` are both sourced from JCM Medium 384, and the maintained parents are linked as `SOURCE_DUPLICATE`. | Merge regeneration from repaired JCM/Togo parents. |
| Minor | The generated record predates the pH and preparation-step repair. | Togo M379 has pH 7.0 and a detailed Soil extract preparation; the maintained parent now has `ph_value: 7.0` and structured `preparation_steps`, but the generated record still has neither. | Merge regeneration after Togo M379 repair. |

## Recommended Edits

1. Regenerate this record from the September 11 repaired Togo M379 parent.
2. Confirm the regenerated record keeps final-medium Tap water at `850.0 ML_PER_L`, keeps Soil extract as a nested `150.0 ML_PER_L` solution, and confines 960 ml tap water plus 400 g air-dried garden soil to the Soil extract composition.
3. Confirm Togo M379 and MediaDive J384 merge to one generated JCM 384 source-duplicate record.
4. Preserve pH 7.0 and the structured Soil extract preparation steps.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated JCM 384 record.
- Compare the final record against Togo M379 and MediaDive J384.
- Re-run the exact gitignore-independent search for `TOGO:M379`, `JCM_M384`, `JCM_J384_GLYCEROL-SOIL_MEDIUM`, `TOGO_M379_Glycerol-Soil_Medium`, and `glycerol_soil_medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify that the JCM 384 duplicate collapsed as intended.

## Additional Notes

None found.
