# YAML Record Review: ARTIFICIAL SOIL AGAR

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/artificial_soil_agar__25f1582e.yaml`
- Started UTC: 2026-09-21T15:32:25Z
- Finished UTC: 2026-09-21T15:32:34Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:002598` |
| Name | `artificial_soil_agar` |
| Original name | ARTIFICIAL SOIL AGAR |
| Category | `bacterial` |
| Source identity | MediaDive/JCM `mediadive.medium:J238` |
| Generated status | Generated single-source merge of `data/normalized_yaml/bacterial/artificial_soil_agar.yaml` |

This is the MediaDive/JCM Artificial Soil Agar record. The adjacent generated
`ARTIFICIAL_SOIL_AGAR.yaml` record is the TOGO `M230` sibling and has different
defects.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/artificial_soil_agar__25f1582e.yaml` | Passed; no issues found. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/artificial_soil_agar__25f1582e.yaml --out /private/tmp/artificial_soil_agar__25f1582e.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/artificial_soil_agar__25f1582e.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the validator reported 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/artificial_soil_agar__25f1582e.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not checked: no focused embedded `MediaRecipe.curation_history` validator is documented for one generated merge record; `just validate-history` targets standalone records under `history/`. |

The documented `just` validators were not used directly because this checkout's
project `uv` environment fails building `llvmlite==0.46.0` under Python 3.13
before target validation starts. The no-project commands above ran the focused
validators against this generated merge.

## Identity and Grounding

MediaDive `J238` resolves to `ARTIFICIAL SOIL AGAR`, source `JCM`, and the same
JCM `GRMD=238` link recorded in the YAML. The current JCM page returns
"Nothing found", so exact formulation checks used MediaDive's JSON export.

Simple salts and agar are grounded correctly. `Soil extract` is an undefined
liquid extract in the source, and the record correctly leaves it ungrounded.

## Evidence

MediaDive `J238` exports one `Main sol. J238` solution at 1000 ml. Its recipe
rows match the CultureMech record for CaSO4 x 2 H2O, Ca(NO3)2 x 4 H2O, MgSO4 x
7 H2O, K2SO4, K2HPO4, NaHCO3, FeCl3 x 6 H2O, yeast extract, glucose, agar, pH
6.7, and the two preparation steps.

Two recipe rows are not represented faithfully:

| Source row | Current representation |
|---|---|
| `Soil extract`, 50 ml, attribute `see below` | `Soil extract`, `50 G_PER_L` |
| `Distilled water`, 950 ml | absent |

The source preparation text also preserves the 6.6-6.8 pH range. The scalar
`ph_value: 6.7` matches MediaDive's min/max export, while the preparation step
retains the source range.

## Completeness

The record is complete for the mineral salts, yeast extract, glucose, agar, pH,
and soil-extract preparation. It remains incomplete for the final liquid volume
because the 950 ml distilled water row is absent, and it misstates the soil
extract as a mass concentration instead of a 50 ml volume addition.

Optional target-organism and growth-evidence slots are empty. I did not flag
that as a defect because the inspected MediaDive source establishes the recipe,
not a growth claim.

Before reporting raw-source absence, I searched for `CultureMech:002598`,
`mediadive.medium:J238`, `JCM Medium J238`, and `ARTIFICIAL SOIL AGAR` with
`rg --no-ignore --hidden` across `data`, `scripts`, `history`, `src`, `reports`,
and `references_cache`. That gitignore-independent search found the normalized
owner, generated merge, indexes, and archived reports, but no maintained raw
YAML or source-specific importer file for J238.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The 50 ml soil-extract addition is stored as `50 G_PER_L`. | MediaDive `Main sol. J238` lists `Soil extract`, amount 50, unit `ml`, with attribute `see below`; the generated CultureMech record stores `50 G_PER_L`. | `data/normalized_yaml/bacterial/artificial_soil_agar.yaml` |
| minor | The 950 ml distilled-water row is omitted. | MediaDive lists 950 ml distilled water as recipe row 12 in `Main sol. J238`; no water row appears in the generated CultureMech record. | `data/normalized_yaml/bacterial/artificial_soil_agar.yaml` |

## Recommended Edits

1. Change `Soil extract` from `50 G_PER_L` to the source 50 ml volume addition, or model it as a nested prepared extract with a 50 ml final addition.
2. Add or explicitly account for the 950 ml distilled-water row from the MediaDive main solution.
3. Regenerate `data/merge_yaml/merged/artificial_soil_agar__25f1582e.yaml`.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/bacterial/artificial_soil_agar.yaml`.
- Run `just validate-strict data/normalized_yaml/bacterial/artificial_soil_agar.yaml`.
- Run `just validate-terms data/normalized_yaml/bacterial/artificial_soil_agar.yaml`.
- Run `just validate-references data/normalized_yaml/bacterial/artificial_soil_agar.yaml`.
- Run `just verify-merges` after regeneration.
- Manually compare the regenerated record with MediaDive `J238` to confirm the 50 ml soil extract and 950 ml water rows are represented.

## Additional Notes

- The cited JCM `GRMD=238` URL returned "Nothing found"; MediaDive's `J238`
  JSON export was available and internally consistent.
