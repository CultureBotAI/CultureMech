# YAML Record Review: gs2_medium_with_cellobiose__cafecaac

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/gs2_medium_with_cellobiose__cafecaac.yaml
- Started UTC: 2026-09-23T07:47:54Z
- Finished UTC: 2026-09-23T07:50:10Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:002453` |
| Name | `gs2_medium_with_cellobiose` |
| Original name | `GS2 MEDIUM WITH CELLOBIOSE` |
| Category | `bacterial` |
| Canonical media term | `mediadive.medium:J1291` |
| Merged sources | `gs2_medium_with_cellobiose` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gs2_medium_with_cellobiose__cafecaac.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/gs2_medium_with_cellobiose__cafecaac.yaml --out /private/tmp/gs2_medium_with_cellobiose__cafecaac.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/gs2_medium_with_cellobiose__cafecaac.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/gs2_medium_with_cellobiose__cafecaac.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This generated record is the MediaDive JCM 1291 import. A gitignore-independent exact search for `mediadive.medium:J1291`, `TOGO:M1387`, `GRMD=1291`, `gs2_medium_with_cellobiose`, and `TOGO_M1387_GS2_Medium_With_Cellobiose` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found a split Togo M1387 import generated separately as `data/merge_yaml/merged/GS2_MEDIUM_WITH_CELLOBIOSE.yaml`.

Most small-molecule groundings are narrow. `Trisodium citrate x 2 H2O` is grounded to generic sodium citrate, and the source 1.25% FeSO4 solution is flattened to an anhydrous FeSO4 compound row.

## Evidence

JCM Medium 1291 has a basal solution with 1 L Distilled water, eight solutes, and pH 7.2. After autoclaving, the recipe adds 10 ml autoclaved GS2 salt solution and 8 ml 0.2 M Cellobiose solution. GS2 salt solution is its own 1 L stock containing 100 g MgCl2 x 6 H2O, 15 g CaCl2 x 2 H2O, 0.1 ml 1.25% FeSO4 solution, and 1 L Distilled water.

The generated record omits both water rows, omits the explicit 10 ml GS2 salt solution addition, flattens the 1 L GS2 stock contents into final top-level ingredients, and converts the 8 ml 0.2 M Cellobiose solution into an `8 G_PER_L` Cellobiose row. The split Togo M1387 generated record has the same stock scoping problems and is stale relative to its 2026-09-02 normalized parent water repair.

## Completeness

The MediaDive basal solutes and anaerobic autoclaving instruction are present, but the formula is not complete enough for JCM 1291 while post-autoclave additions and GS2 stock are flattened or misunitized and the Togo copy is split into a separate generated record. Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects by themselves.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | GS2 salt solution was flattened at stock strength. | JCM 1291 adds 10 ml/l of the GS2 stock; the generated record promotes 100 g/l MgCl2 x 6 H2O, 15 g/l CaCl2 x 2 H2O, and a 1.25% FeSO4 solution row directly to final top-level ingredients. | MediaDive J1291 stock expansion. |
| Major | The 0.2 M Cellobiose solution addition has the wrong unit and concentration. | JCM adds 8 ml of 0.2 M Cellobiose solution after autoclaving; the generated record encodes `Cellobiose` as `8 G_PER_L`. | MediaDive J1291 solution-addition normalization. |
| Major | Required water rows and stock-addition rows are missing. | JCM lists 1 L basal Distilled water, 10 ml GS2 salt solution, 8 ml Cellobiose solution, and 1 L GS2-stock Distilled water; none is represented structurally in the generated ingredient list. | MediaDive J1291 nested-solution handling. |
| Major | Togo M1387 remains split from the MediaDive JCM 1291 duplicate group. | Togo M1387 links to the same JCM `GRMD=1291` recipe but is generated separately as `GS2_MEDIUM_WITH_CELLOBIOSE.yaml`. | Duplicate grouping for Togo/MediaDive JCM 1291 records. |
| Minor | Hydrate and solution qualifiers are lost from two grounded rows. | `Trisodium citrate x 2 H2O` is grounded to sodium citrate and `1.25% FeSO4 solution` is flattened to an anhydrous FeSO4 compound row. | CHEBI grounding and compound attribute preservation. |

## Recommended Edits

1. Model GS2 salt solution as a nested 10 ml/l stock addition with its own 1 L recipe.
2. Encode 0.2 M Cellobiose solution as an 8 ml/l post-autoclave addition instead of an 8 g/l Cellobiose row.
3. Restore both Distilled water rows in their basal and GS2-stock scopes.
4. Preserve the 1.25% FeSO4 solution attribute under the GS2 salt solution instead of flattening it as an anhydrous FeSO4 final row.
5. Reground trisodium citrate dihydrate to a hydrate-specific CHEBI term if one is available.
6. Repair Togo M1387 and confirm it joins the same JCM 1291 source-duplicate cluster.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation on the regenerated JCM 1291 record.
- Compare the regenerated record against the JCM 1291 page, MediaDive J1291, and Togo M1387.
- Confirm GS2 salt and Cellobiose solution are represented as post-autoclave additions rather than top-level final masses.
- Re-run the exact gitignore-independent search for `mediadive.medium:J1291`, `TOGO:M1387`, `GRMD=1291`, `gs2_medium_with_cellobiose`, and `TOGO_M1387_GS2_Medium_With_Cellobiose` across `data/normalized_yaml/` and `data/merge_yaml/merged/` to verify the duplicate group is intentional.

## Additional Notes

None found.
