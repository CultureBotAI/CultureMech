# YAML Record Review: GAM Agar With 0.5% Arginine

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/gam_agar_with_0_5_arginine.yaml
- Started UTC: 2026-09-23T05:15:25Z
- Finished UTC: 2026-09-23T05:16:34Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:009984`, `gam_agar_with_0_5_arginine`, category `bacterial`, for TOGO Medium `TOGO:M588`.

The generated merge has one source, `TOGO_M588_GAM_Agar_With_0.5_Arginine`, with fingerprint `3d452edb85cc7fc0ce2cf9f62389ceb837d281c74306c05d41a2e3756f619ac8`; the maintained source is `data/normalized_yaml/bacterial/TOGO_M588_GAM_Agar_With_0.5_Arginine.yaml`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gam_agar_with_0_5_arginine.yaml` | Passed. |
| `python scripts/validate_strict.py data/merge_yaml/merged/gam_agar_with_0_5_arginine.yaml --out /private/tmp/gam_agar_with_0_5_arginine.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and no error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/gam_agar_with_0_5_arginine.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator reported zero checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/gam_agar_with_0_5_arginine.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository documents `just validate-history` for standalone files under `history/`, not for generated `MediaRecipe.curation_history` entries. |

## Identity and Grounding

TOGO `M588` resolves to `GAM Agar With 0.5% Arginine`, original medium `JCM_M583`, original URL `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=583`, and pH 7.0. The live JCM page for `GRMD=583` is `GAM AGAR WITH 0.5% ARGININE` with the same ingredients and the `Adjust pH to 7.0.` instruction. MediaDive independently mirrors this as JCM medium `J583`.

An ignored-file-inclusive search over `data/normalized_yaml` and `data/merge_yaml/merged` for the slug, `TOGO:M588`, `CultureMech:009984`, and the JCM identifiers found this TOGO-derived source and a second direct JCM source at `data/normalized_yaml/bacterial/gam_agar_with_0_5_arginine.yaml`, emitted as `data/merge_yaml/merged/gam_agar_with_0_5_arginine__c27f4845.yaml`. Those two records both point to the JCM 583 formulation but remain split.

The TOGO record mis-grounds `Arginine` to `CHEBI:32696` / `argininium(1+)`; the direct JCM record correctly uses neutral `CHEBI:29016` / `arginine`.

## Evidence

The inspected TOGO JSON, JCM HTML, and MediaDive JCM REST record agree on the four recipe rows:

| Ingredient | Source amount |
|---|---:|
| GAM broth / GAM broth (Nissui) | 59 g |
| Arginine | 5 g |
| Agar | 15 g |
| Distilled water | 1 L |

The generated TOGO-derived YAML preserves the two mass rows for arginine and agar and the commercial `GAM broth (Nissui)` label. It does not preserve TOGO's pH 7.0 comment as `ph_value` or as a preparation step, even though both the TOGO API and the JCM source page expose that instruction.

The distilled-water row is not dimensionally correct: TOGO reports `volume: 1, unit: L`, while the generated YAML stores `value: '1', unit: G_PER_L`. That is neither the supplied volume nor a valid mass concentration.

## Completeness

The TOGO-derived generated record is missing the pH 7.0 adjustment, the related preparation step, and the identity link to the direct JCM J583 import. Empty preparation steps would have been acceptable only if the upstream source had no instructions; here the source has one explicit pH adjustment.

The generated record has no ontology term for `GAM broth (Nissui)`. That is acceptable for now because it is a commercial undefined component rather than a resolved chemical compound.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | TOGO M588 and direct JCM J583 remain separate generated recipes for the same JCM formulation. | The TOGO record names original medium `JCM_M583` and the same JCM `GRMD=583` URL used by the direct `mediadive.medium:J583` record, but the merge step emitted two CultureMech IDs and two merged YAML files. | `data/normalized_yaml/bacterial/TOGO_M588_GAM_Agar_With_0.5_Arginine.yaml`, `data/normalized_yaml/bacterial/gam_agar_with_0_5_arginine.yaml`, and merge reconciliation. |
| Major | The TOGO importer dropped the pH/comment evidence. | TOGO carries `ph: "7.0"` and the comment `Adjust pH to 7.0.`; the generated `CultureMech:009984` YAML has no `ph_value` and no `preparation_steps`. | `data/normalized_yaml/bacterial/TOGO_M588_GAM_Agar_With_0.5_Arginine.yaml`. |
| Major | The 1 L distilled-water row was converted to `1 G_PER_L`. | The source row is `1 L`; the YAML row uses a gram-per-liter concentration with value `1`. | `data/normalized_yaml/bacterial/TOGO_M588_GAM_Agar_With_0.5_Arginine.yaml`. |
| Minor | `Arginine` is mapped to protonated argininium instead of neutral arginine. | The JCM direct import for the same ingredient uses `CHEBI:29016` / `arginine`; the TOGO row uses `CHEBI:32696` / `argininium(1+)`. | `data/normalized_yaml/bacterial/TOGO_M588_GAM_Agar_With_0.5_Arginine.yaml`. |
| Minor | A stale legacy MediaIngredientMech link remains on the arginine row. | The row still has `mediaingredientmech_term: MediaIngredientMech:000341` after the June 2026 curation history claims legacy MIM links were refreshed to CHEBI keying. | `data/normalized_yaml/bacterial/TOGO_M588_GAM_Agar_With_0.5_Arginine.yaml`. |

## Recommended Edits

1. Reconcile TOGO M588 and MediaDive/JCM J583 so the two imported snapshots merge or cross-link instead of producing parallel `gam_agar_with_0_5_arginine` records.
2. Add the pH 7.0 value and `Adjust pH to 7.0.` preparation instruction from TOGO/JCM to `data/normalized_yaml/bacterial/TOGO_M588_GAM_Agar_With_0.5_Arginine.yaml`.
3. Preserve the source water amount as 1 L or 1000 ml; do not emit it as `1 G_PER_L`.
4. Re-ground `Arginine` to neutral CHEBI arginine and refresh its MediaIngredientMech link to CHEBI-keyed metadata.

## Follow-up Checks

After curation, regenerate `data/merge_yaml/merged/` and rerun focused schema, strict, reference, and term validation on the regenerated GAM Agar With 0.5% Arginine record or records.

Manually compare the result against:

- TOGO API `https://togomedium.org/sparqlist/api/gmdb_medium_by_gmid?gm_id=M588`
- JCM `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=583`
- MediaDive REST `https://mediadive.dsmz.de/rest/medium/J583`

## Additional Notes

An ignored-file-inclusive search for `JCM.*583` also found unrelated DSMZ Medium 583 / Corynebacterium records and a TOGO archaeal record whose TOGO ID is `M583`; those do not denote JCM 583.
