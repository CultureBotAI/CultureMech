# YAML Record Review: GALLIONELLA (ES) MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/gallionella_es_medium.yaml
- Started UTC: 2026-09-23T05:13:16Z
- Finished UTC: 2026-09-23T05:14:22Z
- Verdict: needs curation

## Target

Reviewed generated `MediaRecipe` `CultureMech:000729`, `gallionella_es_medium`, category `bacterial`, for DSMZ Medium 1267b / MediaDive `mediadive.medium:1267b`.

The generated file has one source, `gallionella_es_medium`, and merge fingerprint `dcee2e2d58a5233a451a665123ae81a5fa18c676d9ab11c7e4e7157ca5dc7256`; the maintained YAML owner is `data/normalized_yaml/bacterial/gallionella_es_medium.yaml`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/gallionella_es_medium.yaml` | Passed. |
| `python scripts/validate_strict.py data/merge_yaml/merged/gallionella_es_medium.yaml --out /private/tmp/gallionella_es_medium.strict.tsv --workers 1 --quiet` | Passed; the TSV had one header row and no error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/gallionella_es_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator reported zero checks. |
| `linkml-term-validator validate-data data/merge_yaml/merged/gallionella_es_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded `curation_history` validation | Not checked: the repository documents `just validate-history` for standalone files under `history/`, not for generated `MediaRecipe.curation_history` entries. |

## Identity and Grounding

MediaDive REST resolves `1267b` to DSMZ `GALLIONELLA (ES) MEDIUM`, non-complex, pH 6.1 to 6.4, with the DSMZ Medium 1267b PDF link used in the record notes. The DSMZ PDF title also identifies the same `1267b: GALLIONELLA (ES) MEDIUM` formulation.

An ignored-file-inclusive search over `data/normalized_yaml` and `data/merge_yaml/merged` for `mediadive.medium:1267b`, `CultureMech:000729`, and `gallionella_es_medium` found only this normalized bacterial source, this generated merge, and generated indexes. No duplicate generated recipe for DSMZ 1267b was found in that search scope.

The record still contains a legacy `mediaingredientmech_term` on `Na2SeO4` even though the June 2026 MIM migration history says legacy MediaIngredientMech links were refreshed to CHEBI keying.

## Evidence

The generated record is a flat ingredient projection of a multi-solution DSMZ protocol. DSMZ 1267b has only three top-level ingredients: 901 ml Solution A, 1 ml Solution B, and 100 ml Solution C. MediaDive preserves those as main solution `2531`, Solution A `2532`, Solution B `2533`, Solution C `2534`, Wolfe's mineral elixir `1605`, Wolin's vitamin solution `5980`, and ferrous sulfide sludge `2526`.

The generated `ingredients` array drops those solution-addition rows and instead expands every downstream stock formula as top-level grams per liter:

| Source scope | Supported source content | Generated problem |
|---|---|---|
| Solution A | NH4Cl, MgSO4 x 7 H2O, CaCl2 x 2 H2O, K2HPO4, 1 ml Wolfe's mineral elixir, NaHCO3 for the top layer, agarose for the top layer, and 900 ml water. | Solution A has no boundary; its water row is missing. |
| Wolfe's mineral elixir | One-liter trace stock used at 1 ml in Solution A. | All Wolfe salts are emitted at their one-liter stock concentrations on the final medium. |
| Solution B / Wolin's vitamin solution (10x) | One ml Solution B, which is 1 ml 10x Wolin vitamin stock. | Every vitamin appears at its one-liter stock concentration on the final medium. |
| Solution C / ferrous sulfide sludge | 100 ml ferrous sulfide sludge; the sludge recipe is 15.4 g FeSO4 x 7 H2O plus 12.3 g Na2S x 9 H2O in 100 ml water. | FeSO4 x 7 H2O and Na2S x 9 H2O are emitted as 154 and 123 g/L stock rows on the final medium. |

The generated duplicate-merge notes also show stock boundaries were crossed:

- `MgSO4 x 7 H2O` is `0.221976 + 30.0` g/L, combining Solution A with Wolfe's mineral elixir.
- `CaCl2 x 2 H2O` is `0.110988 + 1.0` g/L, combining Solution A with Wolfe's mineral elixir.
- `FeSO4 x 7 H2O` is `1.0 + 154.0` g/L, combining Wolfe's mineral elixir with ferrous sulfide sludge.

## Completeness

The generated preparation text includes the three high-level DSMZ preparation steps, but the two stock-specific steps are flattened as top-level steps:

- Wolfe's mineral elixir starts with acidification to pH 1.0 before adding salts.
- Ferrous sulfide sludge starts with heating distilled water to 50 C and washing the sludge before storage under nitrogen.

Those instructions are useful, but they must be scoped to the stock recipes. In the flat generated record they appear to apply to the whole GALLIONELLA medium after inoculation.

Water rows for Solution A, Wolfe's mineral elixir, Wolin's vitamin solution, and ferrous sulfide sludge are absent. The source provenance from DSMZ medium 792, DSMZ medium 120, and DSMZ medium 1267 for the nested stock recipes is also not represented.

## Findings

| Severity | Finding | Evidence | Owner |
|---|---|---|---|
| Major | Solution A, Solution B, and Solution C were flattened into one unsupported final-medium ingredient list. | DSMZ and MediaDive both define the top level as three solution additions; the generated YAML contains no solution-addition rows and no separate Solution A/B/C scopes. | `data/normalized_yaml/bacterial/gallionella_es_medium.yaml` and the MediaDive import that writes nested solutions. |
| Major | Wolfe's mineral elixir and the 10x Wolin vitamin stock are present at stock strength. | DSMZ uses 1 ml Wolfe's mineral elixir inside 901 ml Solution A and 1 ml Wolin vitamin stock inside Solution B; the generated record lists their one-liter stock g/L values as final-medium ingredient concentrations. | `data/normalized_yaml/bacterial/gallionella_es_medium.yaml`. |
| Major | Ferrous sulfide sludge was flattened at 100 ml stock strength. | DSMZ Solution C is 100 ml ferrous sulfide sludge; the generated record imports 154 g/L FeSO4 x 7 H2O and 123 g/L Na2S x 9 H2O as final-medium rows. | `data/normalized_yaml/bacterial/gallionella_es_medium.yaml`. |
| Major | Duplicate-ingredient cleanup merged compounds across unrelated stock scopes. | MgSO4 x 7 H2O, CaCl2 x 2 H2O, and FeSO4 x 7 H2O carry generated duplicate notes that add Solution A, Wolfe's mineral elixir, and FeS-sludge values together. | Duplicate merge logic over `data/normalized_yaml/bacterial/gallionella_es_medium.yaml`. |
| Minor | One stale legacy MediaIngredientMech link remains. | `Na2SeO4` still has `mediaingredientmech_term: MediaIngredientMech:000198` instead of a `mediaingredientmech_chebi_term`, despite the migration entry claiming legacy MIM links were refreshed to CHEBI keying. | `data/normalized_yaml/bacterial/gallionella_es_medium.yaml`. |

## Recommended Edits

1. Rebuild `data/normalized_yaml/bacterial/gallionella_es_medium.yaml` as a nested representation: DSMZ 1267b should reference Solution A, Solution B, and Solution C; Solution A should reference Wolfe's mineral elixir; Solution B should reference the 10x Wolin vitamin solution; Solution C should reference ferrous sulfide sludge.
2. Preserve each water row in its actual solution scope: 900 ml for Solution A, 1000 ml for Wolfe's mineral elixir, 1000 ml for the 10x Wolin vitamin stock, and 100 ml for ferrous sulfide sludge.
3. Attach the pH 1.0 instruction only to Wolfe's mineral elixir and the heating/washing/storage instruction only to ferrous sulfide sludge.
4. Prevent duplicate consolidation from summing compounds across nested solution boundaries when regenerating the merged recipe.
5. Convert the `Na2SeO4` legacy MIM link to CHEBI-keyed MediaIngredientMech metadata.

## Follow-up Checks

After curation, regenerate the merged recipe and rerun focused schema, strict, reference, and term validation on `data/merge_yaml/merged/gallionella_es_medium.yaml`.

Manually compare the regenerated solution graph against:

- MediaDive REST `https://mediadive.dsmz.de/rest/medium/1267b`
- DSMZ `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium1267b.pdf`

Confirm that MgSO4 x 7 H2O, CaCl2 x 2 H2O, and FeSO4 x 7 H2O no longer show cross-stock duplicate-merge notes.

## Additional Notes

The `physical_state: SOLID_AGAR` and pH 6.1 to 6.4 range are source-supported for the semisolid top-layer workflow; no finding is needed for those fields.
