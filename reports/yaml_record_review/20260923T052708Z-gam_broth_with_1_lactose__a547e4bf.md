# YAML Record Review: GAM BROTH WITH 1% LACTOSE

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/gam_broth_with_1_lactose__a547e4bf.yaml
- Started UTC: 2026-09-23T05:26:49Z
- Finished UTC: 2026-09-23T05:27:08Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:003042`, `gam_broth_with_1_lactose`, category `bacterial`, for JCM Medium J697 / MediaDive `mediadive.medium:J697`.

The generated file has one source, `gam_broth_with_1_lactose`, with merge fingerprint `a547e4bf4a8ed4a0dc83a9ec97f1a6f81dfac4222e7062fb86cf181403532a7d`; future YAML edits belong in `data/normalized_yaml/bacterial/gam_broth_with_1_lactose.yaml`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gam_broth_with_1_lactose__a547e4bf.yaml` | Passed with `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/gam_broth_with_1_lactose__a547e4bf.yaml --out /private/tmp/gam_broth_with_1_lactose_a547e4bf.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and no error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/gam_broth_with_1_lactose__a547e4bf.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator reported zero checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/gam_broth_with_1_lactose__a547e4bf.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository documents `just validate-history` for standalone files under `history/`, not for generated `MediaRecipe.curation_history` entries. |

## Identity and Grounding

MediaDive REST resolves `J697` to JCM `GAM BROTH WITH 1% LACTOSE`; the live JCM `GRMD=697` page confirms the same label and recipe. TOGO `M717` also names original medium `JCM_M697` and the same JCM URL.

An ignored-file-inclusive search over `data/normalized_yaml` and `data/merge_yaml/merged` for `TOGO:M717`, `JCM_M697`, `mediadive.medium:J697`, `CultureMech:010124`, and `gam_broth_with_1_lactose` found this direct JCM source and a TOGO M717 source that still generate separate CultureMech records for the same JCM formulation.

Generic `CHEBI:17716` / `lactose` matches the source ingredient. `GAM broth` is an undefined commercial medium and can remain chemically ungrounded, but its Nissui supplier qualifier is source evidence that must be preserved.

## Evidence

The generated August merge captures two non-water source masses:

| JCM ingredient | Source amount | Generated August value | Current normalized value |
|---|---:|---:|---:|
| GAM broth (Nissui) | 59 g | `GAM broth`, 59 g/L | `GAM broth (Nissui)`, 59 g/L |
| Lactose | 10 g | 10 g/L | 10 g/L |
| Distilled water | 1 L | absent | 1000 ml/L |

The current normalized source was repaired on 2026-09-10 by `repair_official_simple_score20.py`; it now includes the Nissui qualifier, 1000 ml distilled water, a JCM reference, data-quality flags, and preparation/autoclave steps. The generated merged file predates those updates.

## Completeness

The generated direct-JCM record is incomplete because it is stale relative to the repaired normalized source and because the TOGO M717 import has not been reconciled with it. The live JCM recipe has no pH value or free-text preparation comment, so those fields are not missing.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | Direct JCM J697 and TOGO M717 remain split. | The TOGO source cites `JCM_M697` and the same JCM `GRMD=697` page used by MediaDive `J697`; the generated corpus still has two records for that formulation. | `data/normalized_yaml/bacterial/gam_broth_with_1_lactose.yaml`, `data/normalized_yaml/bacterial/TOGO_M717_GAM_Broth_With_1_Lactose.yaml`, and merge reconciliation. |
| Major | The generated direct-JCM merge predates the September JCM repair. | The normalized source now has the Nissui qualifier, distilled water row, preparation steps, autoclave metadata, data-quality flags, and JCM reference; the generated August merge lacks those fields. | Regenerate from `data/normalized_yaml/bacterial/gam_broth_with_1_lactose.yaml`. |
| Minor | The generated `GAM broth` row omits the supplier qualifier. | JCM, MediaDive, and the repaired normalized record specify `GAM broth (Nissui)`. | Regenerate from `data/normalized_yaml/bacterial/gam_broth_with_1_lactose.yaml`. |

## Recommended Edits

1. Reconcile the repaired direct JCM J697 lineage with TOGO M717.
2. Regenerate the direct JCM merged file so it carries `GAM broth (Nissui)`, 1000 ml distilled water, preparation steps, `sterilization`, `data_quality_flags`, and `references`.
3. Confirm the regenerated record keeps the generic lactose CHEBI grounding.

## Follow-up Checks

After regeneration, rerun focused schema, strict, reference, and term validation on the regenerated direct JCM output or reconciled TOGO/JCM output.

Manually compare the result against:

- JCM `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=697`
- MediaDive REST `https://mediadive.dsmz.de/rest/medium/J697`
- TOGO API `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M717`

## Additional Notes

The ignored-file-inclusive search also matched `kg_microbe_match` cross-links to J697 on M17 lactose records. They are linkage rows, not duplicate imports of the JCM 697 recipe.
