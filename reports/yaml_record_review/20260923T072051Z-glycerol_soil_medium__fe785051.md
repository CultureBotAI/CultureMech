# YAML Record Review: glycerol_soil_medium__fe785051

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glycerol_soil_medium__fe785051.yaml
- Started UTC: 2026-09-23T07:19:44Z
- Finished UTC: 2026-09-23T07:20:51Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:006527` |
| Name | `glycerol_soil_medium` |
| Original name | `GLYCEROL-SOIL medium` |
| Category | `bacterial` |
| Canonical media term | `komodo.medium:80` |
| Merged sources | `KOMODO_80_GLYCEROL-SOIL_medium`, `glycerol_soil_medium` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glycerol_soil_medium__fe785051.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glycerol_soil_medium__fe785051.yaml --out /private/tmp/glycerol_soil_medium__fe785051.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glycerol_soil_medium__fe785051.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glycerol_soil_medium__fe785051.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This generated record correctly groups KOMODO 80 with the direct MediaDive DSMZ Medium 80 import as a source duplicate. Togo M2317 is also a DSMZ Medium 80 import, but that Togo branch remains a separate generated record.

A gitignore-independent exact search for `TOGO:M379`, `TOGO:M2317`, `JCM_M384`, `JCM_J384_GLYCEROL-SOIL_MEDIUM`, `TOGO_M379_Glycerol-Soil_Medium`, `TOGO_M2317_Glycerol-Soil_Medium`, `KOMODO_80_GLYCEROL-SOIL_medium`, `mediadive.medium:80`, `komodo.medium:80`, and `glycerol_soil_medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found the expected five maintained parents, four generated records, and source indexes.

Grounding for glycerol and agar is narrow. Peptone, Beef extract, and Soil extract are ungrounded in the generated record even though both maintained parents gained local exact mappings for those ingredients in September 2026.

## Evidence

DSMZ Medium 80 lists 5 g Peptone, 3 g Beef extract, 20 g Glycerol, 150 ml Soil extract, 850 ml Distilled water, 15 g Agar, and pH 7.0. Its soil-extract preparation sieves air-dried garden soil, autoclaves 400 g of that soil with 960 ml distilled water at 121 C for one hour, lets the mixture cool and settle, decants and paper-filters the supernatant, autoclaves it in 200 ml portions, and stores it at room temperature until sedimentation clears it.

The generated KOMODO/DSMZ duplicate record preserves Peptone, Beef extract, Glycerol, Soil extract, Agar, and pH 7.0. It omits the DSMZ 850 ml Distilled water row, leaves Soil extract as `150 G_PER_L`, and has no preparation step for pH adjustment or Soil extract preparation. It also predates the September 2026 grounding repair in both of its maintained parents.

## Completeness

The duplicate grouping between KOMODO 80 and direct DSMZ 80 is correct, but the generated record is still incomplete because it lacks the DSMZ water row, misrepresents the Soil extract volume, and omits the DSMZ preparation text. Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects by themselves for this medium.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The DSMZ water row is absent. | DSMZ Medium 80 and MediaDive 80 list 850 ml Distilled water; the generated KOMODO/DSMZ record has no water ingredient. | MediaDive/KOMODO DSMZ 80 normalization and merge regeneration. |
| Major | Soil extract remains a gram-per-liter ingredient instead of a volume addition. | DSMZ Medium 80 lists 150 ml Soil extract; the generated record uses `150 G_PER_L` and has no `solutions` block for the soil extract. | MediaDive/KOMODO DSMZ 80 normalization. |
| Major | DSMZ preparation instructions are not preserved. | The DSMZ source gives a pH 7.0 adjustment plus a 400 g soil / 960 ml distilled-water extract preparation; the generated canonical KOMODO record has no `preparation_steps`. | Merge canonicalization for KOMODO/DSMZ duplicates. |
| Minor | The generated record predates exact grounding repairs for all undefined products. | Direct DSMZ 80 and KOMODO 80 parents gained local mappings for Beef extract, Peptone, and Soil extract on September 13, 2026; the generated record still leaves all three ungrounded. | Merge regeneration after September 13 grounding. |
| Minor | Togo M2317 remains outside the DSMZ 80 duplicate group. | Togo M2317 links to the DSMZ Medium 80 PDF but regenerates as `glycerol_soil_medium__1ef18a40.yaml`. | Duplicate grouping for Togo/MediaDive/KOMODO DSMZ 80 records. |

## Recommended Edits

1. Repair the MediaDive/KOMODO DSMZ 80 representation so 850 ml Distilled water and 150 ml Soil extract are not lost or converted to mass concentrations.
2. Preserve the DSMZ pH and soil-extract preparation steps when merging KOMODO 80 with direct DSMZ 80.
3. Regenerate this duplicate group so the September 2026 Peptone, Beef extract, and Soil extract mappings are present.
4. After Togo M2317 is repaired, merge it into the same DSMZ 80 generated record rather than leaving it as a split duplicate.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated DSMZ 80 record.
- Compare the final record against the DSMZ Medium 80 PDF, MediaDive 80, KOMODO 80, and Togo M2317.
- Re-run the exact gitignore-independent search for `TOGO:M2317`, `KOMODO_80_GLYCEROL-SOIL_medium`, `mediadive.medium:80`, `komodo.medium:80`, and `glycerol_soil_medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify that the DSMZ 80 duplicate group is intentional.

## Additional Notes

None found.
