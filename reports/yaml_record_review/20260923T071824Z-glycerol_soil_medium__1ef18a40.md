# YAML Record Review: glycerol_soil_medium__1ef18a40

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glycerol_soil_medium__1ef18a40.yaml
- Started UTC: 2026-09-23T07:17:18Z
- Finished UTC: 2026-09-23T07:18:24Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:008904` |
| Name | `glycerol_soil_medium` |
| Original name | `Glycerol-Soil Medium` |
| Category | `bacterial` |
| Canonical media term | `TOGO:M2317` |
| Merged sources | `TOGO_M2317_Glycerol-Soil_Medium` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glycerol_soil_medium__1ef18a40.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glycerol_soil_medium__1ef18a40.yaml --out /private/tmp/glycerol_soil_medium__1ef18a40.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glycerol_soil_medium__1ef18a40.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glycerol_soil_medium__1ef18a40.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This generated record is the Togo M2317 import of DSMZ Medium 80, `GLYCEROL-SOIL MEDIUM`. DSMZ Medium 80 is also present as the direct MediaDive DSMZ 80 import and as KOMODO 80, but the generated Togo M2317 record remains split from that DSMZ 80 source cluster.

A gitignore-independent exact search for `TOGO:M379`, `TOGO:M2317`, `JCM_M384`, `JCM_J384_GLYCEROL-SOIL_MEDIUM`, `TOGO_M379_Glycerol-Soil_Medium`, `TOGO_M2317_Glycerol-Soil_Medium`, `KOMODO_80_GLYCEROL-SOIL_medium`, `mediadive.medium:80`, `komodo.medium:80`, and `glycerol_soil_medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found the expected five maintained parents, four generated records, and source indexes.

Grounding for glycerol, water, and agar is narrow. Beef extract, Soil extract, and Peptone are ungrounded in this Togo branch even though the direct DSMZ 80 and KOMODO 80 maintained parents gained local exact mappings for those three ingredients in September 2026.

## Evidence

DSMZ Medium 80 lists 5 g Peptone, 3 g Beef extract, 20 g Glycerol, 150 ml Soil extract, 850 ml Distilled water, 15 g Agar, and pH 7.0. Its soil-extract preparation sieves air-dried garden soil, autoclaves 400 g of that soil with 960 ml distilled water at 121 C for one hour, lets the mixture cool and settle, decants and paper-filters the supernatant, autoclaves it in 200 ml portions, and stores it at room temperature until sedimentation clears it.

Togo M2317 carries the same ingredient names and quantities from the DSMZ source, but the generated record converts both volume components into `G_PER_L`: 850 g/l Distilled water and 150 g/l Soil extract. It also drops the pH 7.0 target and the soil-extract preparation comment entirely.

## Completeness

The generated record is not complete enough for DSMZ Medium 80 because both volume rows have the wrong unit, the pH target and soil-extract instructions are absent, and the same DSMZ medium is split from its MediaDive/KOMODO duplicate group. Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects by themselves for this medium.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | DSMZ volume components are encoded as mass concentrations. | DSMZ Medium 80 and Togo M2317 list 150 ml Soil extract and 850 ml Distilled water; the generated record uses `150 G_PER_L` and `850 G_PER_L`. | `data/normalized_yaml/bacterial/TOGO_M2317_Glycerol-Soil_Medium.yaml`. |
| Major | The generated record drops the pH 7.0 target and soil-extract preparation. | Both the DSMZ PDF and the Togo API include pH 7.0 plus the 400 g soil / 960 ml water extract preparation; the generated record has no `ph_value`, `preparation_steps`, or nested `solutions`. | Togo importer or manual Togo M2317 curation. |
| Major | Togo M2317 is a split duplicate of DSMZ Medium 80. | Togo M2317 links directly to the DSMZ Medium 80 PDF, while `mediadive.medium:80` and `komodo.medium:80` are already linked as duplicates in a separate generated record. | Duplicate grouping for Togo/MediaDive/KOMODO DSMZ 80 records. |
| Minor | The Togo M2317 parent missed later exact ingredient grounding. | MediaDive DSMZ 80 and KOMODO 80 gained local mappings for Beef extract, Peptone, and Soil extract on September 13, 2026; Togo M2317 still leaves them ungrounded. | Exact-term grounding for Togo parents. |

## Recommended Edits

1. Change the Togo M2317 Distilled water and Soil extract rows to milliliter-per-liter rows matching the DSMZ source.
2. Add pH 7.0 and structure the DSMZ soil-extract preparation as a nested 150 ml/l solution.
3. Link Togo M2317 as a source duplicate of the direct MediaDive DSMZ 80 parent.
4. Apply the same Beef extract, Peptone, and Soil extract grounding used by the repaired DSMZ 80 / KOMODO 80 records where the local mappings are appropriate.
5. Regenerate merged records and confirm Togo M2317 no longer creates its own `glycerol_soil_medium__1ef18a40` split.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the repaired generated DSMZ 80 record.
- Compare the final record against Togo M2317 and the DSMZ Medium 80 PDF.
- Re-run the exact gitignore-independent search for `TOGO:M2317`, `KOMODO_80_GLYCEROL-SOIL_medium`, `mediadive.medium:80`, `komodo.medium:80`, and `glycerol_soil_medium` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify that the DSMZ 80 duplicate group is intentional.

## Additional Notes

None found.
