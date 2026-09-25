# YAML Record Review: peat_medium_with_sucrose

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/peat_medium_with_sucrose__47d163e7.yaml
- Started UTC: 2026-09-24T20:05:40Z
- Finished UTC: 2026-09-24T20:06:45Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002266 |
| Label | peat_medium_with_sucrose |
| Original label | PEAT MEDIUM WITH SUCROSE |
| Category | bacterial |
| Source identity | JCM Medium J1086 |
| Maintained owner | data/normalized_yaml/bacterial/peat_medium_with_sucrose.yaml |
| Generated review target | data/merge_yaml/merged/peat_medium_with_sucrose__47d163e7.yaml |

`data/merge_yaml/merged/peat_medium_with_sucrose__47d163e7.yaml` is a generated single-source merge from the direct JCM/MediaDive import `data/normalized_yaml/bacterial/peat_medium_with_sucrose.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/peat_medium_with_sucrose__47d163e7.yaml` | Passed; no issues found. |
| Strict CultureMech validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/peat_medium_with_sucrose__47d163e7.yaml --out /private/tmp/peat_medium_with_sucrose__47d163e7.strict.tsv --workers 1 --quiet` | Passed; `/private/tmp/peat_medium_with_sucrose__47d163e7.strict.tsv` had only its header row. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/peat_medium_with_sucrose__47d163e7.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/peat_medium_with_sucrose__47d163e7.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not run | Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

- `mediadive.medium:J1086` resolves to JCM Medium 1086, `PEAT MEDIUM WITH SUCROSE`.
- JCM 1086 describes a liquid base recipe and an optional solid form made by adding 15 g/L agar. The reviewed direct import represents the liquid form.
- The same JCM 1086 source has repaired TOGO-derived records: `TOGO_M1155_Peat_Medium_With_Sucrose.yaml` for the liquid form and `TOGO_M1156_Peat_Medium_With_Sucrose.yaml` for the solid agar form.
- The reviewed direct JCM import is split from the repaired liquid TOGO M1155 record even though both cite the same JCM GRMD 1086 page.

## Evidence

JCM 1086 supports a final medium with 0.25 g peptone, 1.0 g yeast extract, 2.0 g sucrose, 10 ml Major metals from JCM 923, 0.1 ml Trace metal 1 from JCM 923, and 1 L distilled water. After autoclaving and cooling, the recipe adds 40 ml of filter-sterilized 0.5 M MES solution at pH 5.7, then aseptically distributes the medium under an N2-CO2 (4:1, v/v) atmosphere. JCM also says the solid version gets 15 g/L agar.

The generated direct JCM record is not source-faithful:

- It drops the final 10 ml Major metals, 0.1 ml Trace metal 1, 40 ml MES, and 1 L distilled water rows.
- It stores Major metals and Trace metal 1 stock interiors as final top-level ingredients.
- It stores the 40 ml 0.5 M MES solution addition as a 40 g/L MES ingredient.
- It divides the direct peptone, yeast extract, and sucrose masses by an inferred larger final volume while leaving stock interiors undiluted.

## Completeness

- Consequentially incomplete: the reviewed generated record lacks structured Major metals, Trace metal 1, and 0.5 M MES solution additions.
- Consequentially incomplete: the final water row is absent.
- Consequentially incomplete: the liquid/solid agar variant relationship is not represented between the direct JCM import and the TOGO M1156 solid import.
- Empty optional target-organism collections are not independently defective for this imported medium review.
- No required source or owner was found missing. The ignored-inclusive exact search covered `data/normalized_yaml`, `data/merge_yaml`, `data/import_tracking`, `data/culturemech_id_registry.tsv`, and `data/culturemech_recipe_catalog.tsv`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Stock-solution rows are flattened into final ingredients. | JCM 1086 adds 10 ml Major metals and 0.1 ml Trace metal 1 from JCM 923, but the generated record stores KCl, KH2PO4, NH4Cl, and trace-metal stock interiors as top-level final ingredients. | data/normalized_yaml/bacterial/peat_medium_with_sucrose.yaml; MediaDive/JCM importer |
| major | The MES addition is dimensionally wrong. | JCM 1086 adds 40 ml of 0.5 M MES solution after autoclaving; the generated record stores that as a 40 g/L direct MES row. | data/normalized_yaml/bacterial/peat_medium_with_sucrose.yaml |
| major | The direct JCM liquid import is split from the repaired TOGO liquid import. | Ignored-inclusive exact search found TOGO M1155 with the same JCM GRMD 1086 URL and a repaired scoped representation; it generates `data/merge_yaml/merged/PEAT_MEDIUM_WITH_SUCROSE.yaml` separately. | data/normalized_yaml/bacterial/peat_medium_with_sucrose.yaml; data/normalized_yaml/bacterial/TOGO_M1155_Peat_Medium_With_Sucrose.yaml |
| minor | The solid-agar sibling remains disconnected. | JCM 1086 states that 15 g/L agar is added for solid medium, and TOGO M1156 carries that solid sibling, but the generated liquid target has no variant link to it. | data/normalized_yaml/bacterial/TOGO_M1155_Peat_Medium_With_Sucrose.yaml; data/normalized_yaml/bacterial/TOGO_M1156_Peat_Medium_With_Sucrose.yaml |
| minor | A few trace salt groundings need exact hydrate review if the direct import survives. | `NiCl2 x 6 H2O` is grounded to an anhydrous nickel chloride term and `MnSO4 x n H2O` is grounded to a generic manganese sulfate term in the flattened direct import. | data/normalized_yaml/bacterial/peat_medium_with_sucrose.yaml |

## Recommended Edits

1. Retire or source-map the direct `data/normalized_yaml/bacterial/peat_medium_with_sucrose.yaml` JCM copy into the repaired liquid `data/normalized_yaml/bacterial/TOGO_M1155_Peat_Medium_With_Sucrose.yaml`.
2. Preserve `data/normalized_yaml/bacterial/TOGO_M1156_Peat_Medium_With_Sucrose.yaml` as the 15 g/L agar solid sibling and link it to the liquid M1155 record as a physical-state variant.
3. If the direct JCM owner survives, remodel JCM 1086 with scoped Major metals, Trace metal 1, and filter-sterilized 0.5 M MES solution additions and restore the final water row.
4. Regenerate `data/merge_yaml/merged/` so JCM 1086 no longer emits an unscoped direct-import duplicate with stock interiors as final ingredients.

## Follow-up Checks

1. Rerun open schema, strict, reference, and term validation against regenerated Peat Medium With Sucrose records.
2. Manually compare the regenerated liquid record against JCM GRMD 1086 and confirm it has 0.25 g/L peptone, 1.0 g/L yeast extract, 2.0 g/L sucrose, 10 ml/L Major metals, 0.1 ml/L Trace metal 1, 40 ml/L 0.5 M MES, and 1000 ml/L water at the correct recipe scopes.
3. Confirm an ignored-inclusive exact search for `GRMD=1086` finds one active liquid generated record and one active solid generated record, with an explicit variant relationship rather than an accidental duplicate split.

## Additional Notes

- Exact ignored-inclusive searches were used while resolving the liquid and solid JCM 1086 siblings; ignored files were included.
- The repaired TOGO M1155 record is a suitable structural model for the liquid recipe because it was curated directly against TOGO M1155, JCM 1086, and JCM 923.
