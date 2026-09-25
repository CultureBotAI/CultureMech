# YAML Record Review: peat_medium_with_sucrose

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/peat_medium_with_sucrose__71998560.yaml
- Started UTC: 2026-09-24T20:06:46Z
- Finished UTC: 2026-09-24T20:07:37Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:007680 |
| Label | peat_medium_with_sucrose |
| Original label | Peat Medium With Sucrose |
| Category | bacterial |
| Physical state | SOLID_AGAR |
| Source identity | TOGO Medium M1156, originally JCM_M1086-2 |
| Maintained owner | data/normalized_yaml/bacterial/TOGO_M1156_Peat_Medium_With_Sucrose.yaml |
| Generated review target | data/merge_yaml/merged/peat_medium_with_sucrose__71998560.yaml |

`data/merge_yaml/merged/peat_medium_with_sucrose__71998560.yaml` is a generated single-source merge from `data/normalized_yaml/bacterial/TOGO_M1156_Peat_Medium_With_Sucrose.yaml`. It is the solid-agar sibling of the liquid JCM 1086 / TOGO M1155 Peat Medium With Sucrose recipe.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/peat_medium_with_sucrose__71998560.yaml` | Passed; no issues found. |
| Strict CultureMech validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/peat_medium_with_sucrose__71998560.yaml --out /private/tmp/peat_medium_with_sucrose__71998560.strict.tsv --workers 1 --quiet` | Passed; `/private/tmp/peat_medium_with_sucrose__71998560.strict.tsv` had only its header row. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/peat_medium_with_sucrose__71998560.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/peat_medium_with_sucrose__71998560.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not run | Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

- `TOGO:M1156` resolves to the solid JCM 1086 Peat Medium With Sucrose variant with 15 g/L agar.
- The `SOLID_AGAR` physical state is source-supported because this source row includes agar at 15 g/L.
- The liquid sibling, `TOGO:M1155`, has already been repaired in `data/normalized_yaml/bacterial/TOGO_M1155_Peat_Medium_With_Sucrose.yaml`; the solid M1156 owner remains in its older imported shape.
- The generated M1156 record has no explicit variant relationship to the repaired liquid M1155 record.

## Evidence

JCM 1086 and TOGO M1156 support 0.25 g/L Peptone, 1.0 g/L Yeast extract, 2.0 g/L Sucrose, 15 g/L agar, 10 ml/L Major metals from JCM 923, 0.1 ml/L Trace metal 1 from JCM 923, 40 ml/L 0.5 M MES solution at pH 5.7, 1 L distilled water, and an N2-CO2 (4:1, v/v) gas atmosphere.

The generated record keeps the direct peptone, yeast extract, sucrose, and agar quantities, but it does not preserve the three stock additions:

- `solutions[Major metals]` is an empty shell with `10 G_PER_L` instead of a 10 ml/L reference to the JCM 923 Major metals stock.
- `solutions[Trace metal 1 solution]` is an empty shell with `0.1 G_PER_L` instead of a 0.1 ml/L reference to the JCM 923 Trace metal 1 stock.
- `solutions[0.5 M MES solution]` is an empty shell with `40 G_PER_L` instead of a 40 ml/L post-autoclave, filter-sterilized addition.
- The main 1 L distilled water row is encoded as `1 G_PER_L`, which is dimensionally wrong for the final solvent volume.

## Completeness

- Consequentially incomplete: the Major metals, Trace metal 1, and 0.5 M MES solution compositions are empty and have the wrong units.
- Consequentially incomplete: the liquid/solid relationship to TOGO M1155 is absent.
- Consequentially incomplete: N2-CO2 gas handling appears only as gas ingredients, not as a structured headspace/atmosphere or preparation condition.
- Empty optional target-organism collections are not independently defective for this imported medium review.
- No required source or owner was found missing. The ignored-inclusive exact search covered `data/normalized_yaml`, `data/merge_yaml`, `data/import_tracking`, `data/culturemech_id_registry.tsv`, and `data/culturemech_recipe_catalog.tsv`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Three solution additions have wrong units and no composition. | JCM 1086 / TOGO M1156 give 10 ml/L Major metals, 0.1 ml/L Trace metal 1, and 40 ml/L 0.5 M MES solution; the record stores them as empty `G_PER_L` solution shells. | data/normalized_yaml/bacterial/TOGO_M1156_Peat_Medium_With_Sucrose.yaml |
| major | The final water row is dimensionally wrong. | The source says 1 L distilled water; the record stores `Distilled water` as `1 G_PER_L`. | data/normalized_yaml/bacterial/TOGO_M1156_Peat_Medium_With_Sucrose.yaml |
| minor | The solid variant is not linked to the repaired liquid variant. | JCM 1086 states that solid medium is made by adding 15 g/L agar, and TOGO has split that into liquid M1155 and solid M1156 records. The M1156 record has no relationship to M1155. | data/normalized_yaml/bacterial/TOGO_M1156_Peat_Medium_With_Sucrose.yaml |

## Recommended Edits

1. Remodel `data/normalized_yaml/bacterial/TOGO_M1156_Peat_Medium_With_Sucrose.yaml` using the repaired M1155 liquid record as the base, then add 15 g/L agar and `SOLID_AGAR` state for the solid sibling.
2. Convert Major metals, Trace metal 1, and 0.5 M MES solution from empty `G_PER_L` shells to ml/L solution additions with the same scoped compositions used by the repaired M1155/JCM 923 model.
3. Store the main distilled water row as a volume row rather than `1 G_PER_L`.
4. Add an explicit physical-state variant relationship between the solid M1156 record and the liquid M1155 record.
5. Regenerate `data/merge_yaml/merged/` from the corrected normalized owner.

## Follow-up Checks

1. Rerun open schema, strict, reference, and term validation against the regenerated M1156 merged record.
2. Manually compare the regenerated record against TOGO M1156 and JCM GRMD 1086 and confirm it contains all liquid M1155 solution additions plus 15 g/L agar.
3. Confirm the regenerated M1156 record no longer has empty solution `composition` lists or `G_PER_L` units on volumetric stocks.

## Additional Notes

- Exact ignored-inclusive searches were used while resolving the TOGO M1156 owner and JCM 1086 siblings; ignored files were included.
