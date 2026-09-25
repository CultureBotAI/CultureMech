# YAML Record Review: glycerol_soil_medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glycerol_soil_medium.yaml
- Started UTC: 2026-09-23T07:14:58Z
- Finished UTC: 2026-09-23T07:17:18Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:002741` |
| Name | `glycerol_soil_medium` |
| Original name | `GLYCEROL-SOIL MEDIUM` |
| Category | `bacterial` |
| Canonical media term | `mediadive.medium:J384` |
| Merged sources | `JCM_J384_GLYCEROL-SOIL_MEDIUM` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glycerol_soil_medium.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glycerol_soil_medium.yaml --out /private/tmp/glycerol_soil_medium.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glycerol_soil_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glycerol_soil_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This generated record is the MediaDive JCM 384 branch of the glycerol-soil medium family. Togo M379 imports the same JCM formula, but the generated August 6 records still keep those two JCM 384 branches separate.

A gitignore-independent exact search for `TOGO:M379`, `TOGO:M2317`, `JCM_M384`, `JCM_J384_GLYCEROL-SOIL_MEDIUM`, `TOGO_M379_Glycerol-Soil_Medium`, `TOGO_M2317_Glycerol-Soil_Medium`, `KOMODO_80_GLYCEROL-SOIL_medium`, `mediadive.medium:80`, `komodo.medium:80`, and `glycerol_soil_medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found the expected five maintained parents, four generated records, and source indexes.

Grounding for glycerol, water, and agar is narrow. The September 2026 maintained parent intentionally leaves Bacto peptone and Beef extract ungrounded vendor products and models Soil extract as a nested solution.

## Evidence

MediaDive J384 lists, per liter, 5 g Bacto peptone with the BD-Difco attribute, 3 g Beef extract with the BD-Difco attribute, 20 g glycerol, 150 ml Soil extract, 850 ml Tap water, 15 g agar, and pH 7.0. Its Soil extract subsolution is prepared by suspending 400 g air-dried garden soil in 960 ml tap water, autoclaving the slurry, cooling and settling it, decanting and paper-filtering the supernatant, then autoclaving and storing the extract until it clears.

The generated JCM record retains the major mass values and pH, but it encodes both volume rows as `G_PER_L`: 150 g/l Soil extract and 850 g/l Tap water. The maintained parent repaired this on September 11, 2026 by changing the main Tap water row to `850.0 ML_PER_L`, moving Soil extract into `solutions` at `150.0 ML_PER_L`, and storing the 400 g soil plus 960 ml tap water extract preparation under that nested solution.

The generated record is also split from the generated Togo M379 record for the same JCM 384 formula.

## Completeness

The generated record is stale and not complete enough to use for the JCM 384 formula because its volume ingredients are mis-united and the soil-extract preparation is unstructured. Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects by themselves for this medium.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The generated JCM 384 record still represents volume components as g/l. | MediaDive J384 lists 150 ml Soil extract and 850 ml Tap water per liter; the generated record has both as `G_PER_L` rows. | Regenerate from `data/normalized_yaml/bacterial/JCM_J384_GLYCEROL-SOIL_MEDIUM.yaml`. |
| Major | Soil extract is not structured as a prepared solution in the generated record. | MediaDive J384 exposes the 400 g garden soil in 960 ml tap-water preparation as a Soil extract subsolution; the maintained parent now models it under `solutions`, but the generated record has no `solutions` block. | Merge regeneration after the September 11 JCM 384 repair. |
| Major | The JCM 384 formula is split between MediaDive J384 and Togo M379 generated records. | `glycerol_soil_medium.yaml` and `glycerol_soil_medium__9b7ad2f4.yaml` are both sourced from JCM Medium 384, and the maintained parents are linked as `SOURCE_DUPLICATE`. | Merge regeneration from repaired JCM/Togo parents. |
| Minor | The generated record loses source-vendor specificity for the peptone and beef extract rows. | MediaDive J384 specifies Bacto peptone and Beef extract with the BD-Difco attribute; the maintained parent preserves those labels while the generated record has `Bacto peptone` and `Beef extract`. | Merge regeneration after JCM 384 repair. |

## Recommended Edits

1. Regenerate this record from the September 11 repaired `JCM_J384_GLYCEROL-SOIL_MEDIUM.yaml` parent.
2. Confirm the regenerated record uses `850.0 ML_PER_L` Tap water and a `150.0 ML_PER_L` Soil extract solution rather than gram-per-liter volume artifacts.
3. Confirm Togo M379 and MediaDive J384 merge to one JCM 384 generated record.
4. Preserve the BD-Difco source attributes on Bacto peptone and Beef extract.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated JCM 384 record.
- Compare the final record against MediaDive J384 and Togo M379.
- Re-run the exact gitignore-independent search for `TOGO:M379`, `JCM_M384`, `JCM_J384_GLYCEROL-SOIL_MEDIUM`, `TOGO_M379_Glycerol-Soil_Medium`, and `glycerol_soil_medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify that the JCM 384 duplicate collapsed as intended.

## Additional Notes

The current JCM `GRMD=384` page returned `Nothing found`; MediaDive J384 and the Togo M379 API still expose the JCM 384 formula.
