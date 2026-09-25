# YAML Record Review: MOORELLA THERMOACETICA (TYE-CO) MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/moorella_thermoacetica_tye_co_medium.yaml
- Started UTC: 2026-09-24T14:04:15Z
- Finished UTC: 2026-09-24T14:05:05Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | MediaRecipe |
| ID | CultureMech:001416 |
| Name | moorella_thermoacetica_tye_co_medium |
| Original name | MOORELLA THERMOACETICA (TYE-CO) MEDIUM |
| Primary source owner | data/normalized_yaml/bacterial/moorella_thermoacetica_tye_co_medium.yaml |
| Merged source owner | data/normalized_yaml/bacterial/clostridium_thermoaceticum_medium_tye_co.yaml |
| Generated record | Yes; produced under data/merge_yaml/merged with merge_fingerprint 8cb7906b048f0ba8faa9bcad1a8dd1ff6354af603593077da863e42184b4512c |

## Validation

| Check | Result |
| --- | --- |
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/moorella_thermoacetica_tye_co_medium.yaml` | Passed; `No issues found`. |
| `python scripts/validate_strict.py data/merge_yaml/merged/moorella_thermoacetica_tye_co_medium.yaml --out /private/tmp/moorella_thermoacetica_tye_co_medium.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, 0 total error rows, and the TSV contained only the header. |
| `linkml-reference-validator validate data data/merge_yaml/merged/moorella_thermoacetica_tye_co_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 references were checked. |
| `linkml-term-validator validate-data data/merge_yaml/merged/moorella_thermoacetica_tye_co_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the expected `eutils` / `pkg_resources` warning. |
| Embedded `curation_history` | Not checked: the documented history validator targets the standalone `history/` corpus, not inline `MediaRecipe.curation_history`. |

## Identity and Grounding

The record denotes DSMZ / MediaDive medium 316. The MediaDive REST API and live DSMZ PDF now call the recipe `NEOMOORELLA THERMOACETICA (TYE-CO) MEDIUM`, not `MOORELLA THERMOACETICA (TYE-CO) MEDIUM`, while preserving medium ID 316, final pH 7.0, final volume 1016 ml, and the same TYE-CO recipe.

The merged KOMODO child maps to `komodo.medium:316` and explicitly references DSMZ Medium 316, so it is a plausible source duplicate after it was enriched with the same DSMZ composition.

An ignored-inclusive search over `data/normalized_yaml` and `data/merge_yaml` for exact `mediadive.medium:316`, `DSMZ_Medium316.pdf`, the TYE-CO slug, and the exact DSMZ label found only the expected MediaDive owner, KOMODO child, generated merged output, and index entries.

`NiCl2 x 6 H2O` is grounded to CHEBI:34887 `nickel dichloride`, which is not the hexahydrate named by DSMZ. `Calcium D-(+)-pantothenate` has a CHEBI `term` but no mirrored `mediaingredientmech_chebi_term`.

## Evidence

DSMZ 316 is a 1016 ml medium built from a main solution that includes 10 ml Modified Wolin's mineral solution and 5 ml Wolin's vitamin solution. The main solution also includes 1 ml FeSO4 x 7 H2O at 0.1% w/v and 0.5 ml sodium resazurin at 0.1% w/v. After autoclaving under carbon monoxide, the recipe adds 0.6 g Na2S x 9 H2O from a sterile anoxic stock.

The generated record keeps the main grams but flattens the two stocks:

| Source claim | Generated representation | Assessment |
| --- | --- | --- |
| 10 ml Modified Wolin's mineral solution is added to the main 1016 ml medium | Nitrilotriacetic acid 1.5 g/L, MgSO4 x 7 H2O 3 g/L, MnSO4 x H2O 0.5 g/L, and other mineral-stock rows appear as top-level ingredients | These are the 1 L mineral stock concentrations, not final concentrations after a 10 ml addition. |
| 5 ml Wolin's vitamin solution is added to the main 1016 ml medium | Biotin, folic acid, pyridoxine, thiamine, riboflavin, nicotinic acid, pantothenate, B12, p-aminobenzoic acid, and lipoic acid appear as top-level ingredients | These are the 1 L vitamin stock concentrations, not final concentrations after a 5 ml addition. |
| FeSO4 x 7 H2O appears as a 1 ml 0.1% w/v main addition and as 0.1 g in the mineral stock | The two values were merged into one 0.100984252 g/L top-level row | A trace mineral stock value was summed with the final-medium FeSO4 addition. |
| Na2S x 9 H2O is 0.6 g in the 1016 ml final medium | The generated value is 0.590551 g/L | This value is supported by the final volume conversion. |

The preparation text is supported by the source: the DSMZ record says to dissolve ingredients except sulfide, adjust pH to 7.0, boil, cool under 100% carbon monoxide, dispense under the same gas, autoclave, then add sulfide from a sterile anoxic stock prepared under 100% N2.

## Completeness

No empty optional scalar fields are present, and the absent target organism list is not a schema defect for this provider recipe.

The record is incomplete because it has no structured `Modified Wolin's mineral solution` or `Wolin's vitamin solution`. Their stock rows have been promoted to final ingredients and their water rows have been dropped, so the 10 ml and 5 ml additions cannot be recovered from the YAML.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| Major | Modified Wolin's mineral solution was flattened into the final medium. | DSMZ adds 10 ml mineral stock to 1016 ml final medium; the YAML stores 1 L mineral-stock values such as 1.5 g/L nitrilotriacetic acid and 3 g/L MgSO4 x 7 H2O as final rows. | `data/normalized_yaml/bacterial/moorella_thermoacetica_tye_co_medium.yaml` and the DSMZ/MediaDive import path. |
| Major | Wolin's vitamin solution was flattened into the final medium. | DSMZ adds 5 ml vitamin stock, but the YAML stores the 1 L vitamin-stock concentrations as top-level ingredients. | The DSMZ/MediaDive import path; the KOMODO child inherits the same copied values. |
| Major | FeSO4 x 7 H2O sums a final trace addition with a mineral-stock concentration. | DSMZ has 1 ml 0.1% w/v FeSO4 in the main recipe and 0.1 g/L FeSO4 inside the 10 ml mineral stock; the generated row combines them as `0.10098425200000001 G_PER_L`. | `data/normalized_yaml/bacterial/moorella_thermoacetica_tye_co_medium.yaml` and duplicate ingredient cleanup over flattened stocks. |
| Major | NiCl2 x 6 H2O has the wrong CHEBI grounding. | The row names nickel chloride hexahydrate, but CHEBI:34887 is `nickel dichloride`. | CHEBI enrichment over the MediaDive owner and any KOMODO copy. |
| Minor | The medium label is stale relative to current DSMZ. | Live MediaDive and the downloaded DSMZ PDF now label medium 316 as `NEOMOORELLA THERMOACETICA (TYE-CO) MEDIUM`. | `data/normalized_yaml/bacterial/moorella_thermoacetica_tye_co_medium.yaml`. |
| Minor | Calcium D-(+)-pantothenate is missing its MediaIngredientMech CHEBI mirror. | The row has CHEBI:31345 but no `mediaingredientmech_chebi_term`. | MediaIngredientMech enrichment over the MediaDive owner. |

## Recommended Edits

1. Rebuild DSMZ / MediaDive medium 316 with explicit `Modified Wolin's mineral solution` and `Wolin's vitamin solution` stocks plus final 10 ml and 5 ml stock additions.
2. Keep mineral and vitamin stock concentrations inside those solution objects instead of promoting them to final ingredients.
3. Stop summing FeSO4 x 7 H2O from the final medium and Modified Wolin's mineral solution; those claims belong to different solution scopes.
4. Keep the KOMODO 316 child as a source duplicate only if it continues to resolve to DSMZ Medium 316.
5. Update the label from Moorella to Neomoorella when regenerating from current DSMZ or MediaDive.
6. Correct the NiCl2 x 6 H2O CHEBI grounding and refresh MediaIngredientMech CHEBI enrichment for Calcium D-(+)-pantothenate.

## Follow-up Checks

- Rerun `linkml-validate`, `scripts/validate_strict.py`, `linkml-reference-validator`, and `linkml-term-validator` on the regenerated TYE-CO record.
- Manually compare the regenerated record against the DSMZ 316 PDF or MediaDive REST medium 316, including the 10 ml and 5 ml stock additions and final volume 1016 ml.
- Run an ignored-inclusive search for `mediadive.medium:316`, `DSMZ_Medium316.pdf`, and `moorella_thermoacetica_tye_co_medium` across `data/normalized_yaml` and `data/merge_yaml` to confirm that only the intended DSMZ/KOMODO source duplicate remains.

## Additional Notes

DSMZ's current PDF for medium 316 rendered successfully during review; unlike the DSMZ 527 PDF, this source URL is live.
