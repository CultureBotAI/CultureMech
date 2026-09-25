# YAML Record Review: GAUZE'S SYNTHETIC MEDIUM NO. 1

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/gauzes_synthetic_medium_no_1.yaml
- Started UTC: 2026-09-23T05:29:56Z
- Finished UTC: 2026-09-23T05:31:12Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:003164`, `gauzes_synthetic_medium_no_1`, category `bacterial`, for JCM Medium J81 / MediaDive `mediadive.medium:J81`.

The generated record merged four sources on fingerprint `3b5f355178d55040d1cd70fb0ec745ab9ab6db31fe4014aa4e04e5be43ec8edf`: `JCM_J81_GAUZE_S_SYNTHETIC_MEDIUM_NO._1`, `KOMODO_1048_GAUZE_S_SYNTHETIC_MEDIUM_NO.1`, `gauzes_synthetic_medium_no_1`, and `gauzes_synthetic_medium_no_1_ph_5_3`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gauzes_synthetic_medium_no_1.yaml` | Passed with `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/gauzes_synthetic_medium_no_1.yaml --out /private/tmp/gauzes_synthetic_medium_no_1.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and no error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/gauzes_synthetic_medium_no_1.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator reported zero checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/gauzes_synthetic_medium_no_1.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository documents `just validate-history` for standalone files under `history/`, not for generated `MediaRecipe.curation_history` entries. |

## Identity and Grounding

JCM `J81` resolves to `GAUZE'S SYNTHETIC MEDIUM NO. 1`, pH 7.2-7.4. DSMZ/MediaDive 1048 resolves to `GAUZE'S SYNTHETIC MEDIUM NO.1`, pH 7.4, with the same base formula and 15 g agar in the DSMZ PDF. KOMODO 1048 is already marked in normalized YAML as a source duplicate of the DSMZ/MediaDive 1048 import.

MediaDive `J949` is not the same target: it resolves to `GAUZE'S SYNTHETIC MEDIUM NO. 1 (pH 5.3)` and its only explicit source step is to prepare Medium 81 and adjust the pH to 5.3. It should be a pH-specific variant, not a merged source or synonym for the pH 7.2-7.4 base record.

An ignored-file-inclusive slug search over `data/normalized_yaml` and `data/merge_yaml/merged` found the merged base record, a direct TOGO sibling, the pH 5.3 variant, and the separate 18% NaCl variants. Those variant forms were found in the searched scope and are not absent.

## Evidence

JCM J81, DSMZ 1048, and their MediaDive mirrors agree on the major formula:

| Ingredient | Source amount |
|---|---:|
| Soluble starch | 20 g |
| KNO3 | 1 g |
| NaCl | 0.5 g |
| MgSO4 x 7 H2O | 0.5 g |
| K2HPO4 | 0.5 g |
| FeSO4 x 7 H2O | 10 mg |
| Agar | 15 g |
| Distilled water | 1 L |

The generated record captures the non-water amounts, including the 10 mg FeSO4 x 7 H2O source row as 0.01 g/L. It omits the 1 L distilled-water row and loses the `soluble` qualifier from the starch row.

DSMZ 1048 and KOMODO 1048 specify pH 7.4, which fits the broader JCM 81 range. JCM J949 specifies pH 5.3, which is outside that range and belongs to `gauzes_synthetic_medium_no_1_ph_5_3`.

## Completeness

The generated record is not complete enough as a base Medium 81 / DSMZ 1048 recipe because it lacks water, has an under-specified starch reagent, and still contains a stale legacy `mediaingredientmech_term` on `KNO3`.

The generated record is also not complete enough as a merge product: it folded the pH 5.3 variant into `merged_from` and a synonym entry, while leaving at least one same-source TOGO Gauze base snapshot outside this merge.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | The pH 5.3 JCM J949 variant was merged into the pH 7.2-7.4 / 7.4 base record. | The generated record lists `gauzes_synthetic_medium_no_1_ph_5_3` in `merged_from` and as a synonym, but MediaDive J949 names an explicit `(pH 5.3)` medium whose preparation step adjusts Medium 81 to pH 5.3. | Merge reconciliation over `data/normalized_yaml/bacterial/gauzes_synthetic_medium_no_1_ph_5_3.yaml`. |
| Major | The 1 L distilled-water row is missing. | JCM J81, MediaDive J81, DSMZ 1048, and MediaDive 1048 all include distilled water to 1000 ml / 1 L; the generated YAML has no water ingredient. | JCM and MediaDive normalized inputs for the Gauze base medium, then regeneration. |
| Major | The source reagent `Soluble starch` was weakened to `Starch`. | JCM prints `Soluble starch` and MediaDive carries `attribute: soluble`; the generated `preferred_term` is plain `Starch` with no qualifier note. | `data/normalized_yaml/bacterial/JCM_J81_GAUZE_S_SYNTHETIC_MEDIUM_NO._1.yaml` and `data/normalized_yaml/bacterial/gauzes_synthetic_medium_no_1.yaml`. |
| Minor | `KNO3` retains a stale legacy MediaIngredientMech link. | The row has exact primary CHEBI `CHEBI:63043` but still uses `mediaingredientmech_term: MediaIngredientMech:000170` after the June MIM migration. | All normalized Gauze base and pH-variant inputs that still carry the legacy KNO3 link. |

## Recommended Edits

1. Remove `gauzes_synthetic_medium_no_1_ph_5_3` / JCM J949 from this base merge and keep it as an explicit pH 5.3 child variant of Medium 81.
2. Preserve the 1000 ml distilled-water row when regenerating the JCM J81 / DSMZ 1048 base record.
3. Preserve `soluble` on the starch ingredient as a reagent qualifier.
4. Convert the remaining `KNO3` legacy MIM link to CHEBI-keyed MediaIngredientMech metadata.
5. Re-run merge reconciliation across the JCM, DSMZ/KOMODO, and TOGO Gauze base snapshots after the pH 5.3 variant is excluded.

## Follow-up Checks

After curation, regenerate `data/merge_yaml/merged/` and rerun focused schema, strict, reference, and term validation on the regenerated Gauze base record and the pH 5.3 child record.

Manually compare the base record against:

- JCM `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=81`
- MediaDive REST `https://mediadive.dsmz.de/rest/medium/J81`
- MediaDive REST `https://mediadive.dsmz.de/rest/medium/1048`
- DSMZ `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1048.pdf`
- MediaDive REST `https://mediadive.dsmz.de/rest/medium/J949`

## Additional Notes

The initial slug search included ignored files and found the sibling pH and high-salt Gauze records. A later accession search for `TOGO:M72` also matched neighboring TOGO identifiers such as `TOGO:M720`; those broader hits were not used for absence claims.
