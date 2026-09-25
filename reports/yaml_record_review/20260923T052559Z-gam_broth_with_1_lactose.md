# YAML Record Review: GAM Broth With 1% Lactose

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/gam_broth_with_1_lactose.yaml
- Started UTC: 2026-09-23T05:25:06Z
- Finished UTC: 2026-09-23T05:25:59Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:010124`, `gam_broth_with_1_lactose`, category `bacterial`, for TOGO Medium `TOGO:M717`.

The generated file has one source, `TOGO_M717_GAM_Broth_With_1_Lactose`, with merge fingerprint `2e4ab1b04244d48e836441905f96801b8de5fc5dbff5fe549f8d73fd692978d5`; future TOGO YAML edits belong in `data/normalized_yaml/bacterial/TOGO_M717_GAM_Broth_With_1_Lactose.yaml`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gam_broth_with_1_lactose.yaml` | Passed. |
| `python scripts/validate_strict.py data/merge_yaml/merged/gam_broth_with_1_lactose.yaml --out /private/tmp/gam_broth_with_1_lactose.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and no error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/gam_broth_with_1_lactose.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator reported zero checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/gam_broth_with_1_lactose.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository documents `just validate-history` for standalone files under `history/`, not for generated `MediaRecipe.curation_history` entries. |

## Identity and Grounding

TOGO `M717` resolves to `GAM Broth With 1% Lactose`, original medium `JCM_M697`, and the JCM `GRMD=697` URL. The live JCM page and MediaDive medium `J697` confirm the same `GAM BROTH WITH 1% LACTOSE` recipe.

An ignored-file-inclusive search over `data/normalized_yaml` and `data/merge_yaml/merged` for `TOGO:M717`, `JCM_M697`, `mediadive.medium:J697`, `CultureMech:010124`, and `gam_broth_with_1_lactose` found this TOGO import and a direct JCM import at `data/normalized_yaml/bacterial/gam_broth_with_1_lactose.yaml`, emitted separately as `data/merge_yaml/merged/gam_broth_with_1_lactose__a547e4bf.yaml`.

The TOGO row maps source `Lactose` to `CHEBI:36218` / `beta-lactose`, which narrows the source beyond what JCM states. The repaired direct JCM normalized source maps the same row to generic `CHEBI:17716` / `lactose`.

## Evidence

The inspected TOGO JSON, live JCM HTML, and MediaDive JCM REST record agree on:

| Ingredient | Source amount |
|---|---:|
| GAM broth (Nissui) | 59 g |
| Lactose | 10 g |
| Distilled water | 1 L |

The generated TOGO-derived record preserves the two dry ingredient amounts and the supplier-qualified `GAM broth (Nissui)` label. It also includes a distilled-water row, but stores the source `1 L` as `value: '1', unit: G_PER_L`, which is dimensionally wrong.

The direct JCM normalized source was repaired on 2026-09-10 to include `GAM broth (Nissui)`, generic lactose, 1000 ml distilled water, references, data-quality flags, and preparation/autoclave steps. That repaired record still has a stale generated sibling.

## Completeness

The JCM 697 source has no pH value or source-specific preparation comment, so no pH or source comment is missing from the TOGO import. The formula remains incomplete because the water amount is unit-corrupted and the semantically identical direct JCM import was not reconciled with it.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | TOGO M717 and direct JCM J697 remain separate generated records for the same recipe. | TOGO names `JCM_M697` and the same JCM URL used by MediaDive `J697`, but the two lineages have different CultureMech IDs and generated filenames. | `data/normalized_yaml/bacterial/TOGO_M717_GAM_Broth_With_1_Lactose.yaml`, `data/normalized_yaml/bacterial/gam_broth_with_1_lactose.yaml`, and merge reconciliation. |
| Major | The 1 L distilled-water row was converted to `1 G_PER_L`. | TOGO and JCM both list 1 L distilled water; the generated TOGO YAML represents it as a gram-per-liter concentration. | `data/normalized_yaml/bacterial/TOGO_M717_GAM_Broth_With_1_Lactose.yaml`. |
| Major | Lactose is grounded to an unsupported anomer-specific term. | The source says `Lactose`, while the TOGO row uses `CHEBI:36218` / `beta-lactose`; the repaired direct JCM source uses generic `CHEBI:17716` / `lactose`. | `data/normalized_yaml/bacterial/TOGO_M717_GAM_Broth_With_1_Lactose.yaml`. |

## Recommended Edits

1. Reconcile the TOGO M717 and direct JCM J697 lineages so a regenerated corpus does not keep two records for JCM 697.
2. Preserve the TOGO water row as 1 L or 1000 ml rather than `1 G_PER_L`.
3. Re-ground the TOGO `Lactose` ingredient to the generic lactose CHEBI term unless a source states an anomer-specific form.

## Follow-up Checks

After curation, regenerate `data/merge_yaml/merged/` and rerun focused schema, strict, reference, and term validation on the regenerated TOGO/JCM result.

Manually compare the result against:

- TOGO API `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M717`
- JCM `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=697`
- MediaDive REST `https://mediadive.dsmz.de/rest/medium/J697`

## Additional Notes

The ignored-file-inclusive search also found two M17 lactose records whose `kg_microbe_match` values point at `mediadive.medium:J697`; those are cross-links, not separate JCM 697 recipe imports.
