# YAML Record Review: glucose_sulfide_medium_richard_et_al_1985

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/glucose_sulfide_medium_richard_et_al_1985.yaml
- Started UTC: 2026-09-23T06:56:40Z
- Finished UTC: 2026-09-23T06:58:21Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Generated status | Generated merge under `data/merge_yaml/merged/` |
| ID | `CultureMech:000593` |
| Name | `glucose_sulfide_medium_richard_et_al_1985` |
| Original name | `GLUCOSE SULFIDE MEDIUM (Richard et al., 1985)` |
| Category | `bacterial` |
| Media term | `mediadive.medium:1154` |
| Maintained parent | `data/normalized_yaml/bacterial/glucose_sulfide_medium_richard_et_al_1985.yaml` |

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/glucose_sulfide_medium_richard_et_al_1985.yaml` | Passed; no issues found. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/glucose_sulfide_medium_richard_et_al_1985.yaml --out /private/tmp/glucose_sulfide_medium_richard_et_al_1985.strict.tsv --workers 1 --quiet` | Passed; 0 ERROR rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/glucose_sulfide_medium_richard_et_al_1985.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/glucose_sulfide_medium_richard_et_al_1985.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` rows. |

## Identity and Grounding

This record denotes DSMZ / MediaDive medium 1154, `GLUCOSE SULFIDE MEDIUM (Richard et al., 1985)`. A gitignore-independent exact search for `mediadive.medium:1154`, `DSMZ_Medium1154.pdf`, and `glucose_sulfide_medium_richard_et_al_1985` across `data/normalized_yaml/` and `data/merge_yaml/merged/` found only this maintained parent, this generated merge, and normalized index references.

The main-medium compound groundings are exact for glucose, ammonium sulfate, calcium carbonate, calcium nitrate, potassium chloride, dipotassium hydrogen phosphate, magnesium sulfate heptahydrate, sodium sulfide nonahydrate, and agar. Co-carboxylase is ungrounded, which is safer than mapping it to an adjacent vitamin term without source evidence.

## Evidence

DSMZ 1154 has a main solution plus a separately filter-sterilized vitamin solution:

| Source row | DSMZ amount |
|---|---:|
| Glucose | 0.150 g |
| (NH4)2SO4 | 0.500 g |
| CaCO3 | 0.100 g |
| Ca(NO3)2 | 0.100 g |
| KCl | 0.050 g |
| K2HPO4 | 0.050 g |
| MgSO4 x 7 H2O | 0.050 g |
| Na2S x 9 H2O | 0.187 g |
| Vitamin solution | 1.000 ml |
| Agar | 15.000 g for solid medium |
| Distilled water | 1000.000 ml |

The vitamin solution is a 1000 ml stock. DSMZ and MediaDive agree that the main medium receives only 1 ml of that stock after autoclaving.

The generated record flattens each vitamin at the stock g/l value as if it were a final-medium amount. Because the medium receives 1 ml of a 1000 ml stock, each generated vitamin concentration is 1000 times too high relative to its final-medium dilution.

The two preparation steps are source-backed in text, but their scope is incomplete: `filter-sterilized, added after autoclaving` applies to the Vitamin solution stock that the generated record omits.

## Completeness

The generated record is incomplete for source structure and final vitamin amounts: it omits the 1 ml vitamin-stock addition row, the vitamin-solution grouping, and both 1000 ml water rows. The main-medium non-vitamin quantities are otherwise supported.

Empty optional fields such as `target_organisms`, `references`, and `discussion` are not defects here.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The Vitamin solution was flattened at stock strength, inflating all vitamin additions 1000-fold in the final medium. | DSMZ 1154 adds 1 ml of a 1000 ml vitamin solution; the generated record stores the vitamin stock g/l rows directly as final `ingredients`. | MediaDive import normalization for `data/normalized_yaml/bacterial/glucose_sulfide_medium_richard_et_al_1985.yaml`. |
| Major | The source solution boundary and water rows are missing. | DSMZ 1154 has a main solution with 1000 ml water, a 1 ml Vitamin solution row, and a 1000 ml vitamin stock; the generated record has no water or stock-addition rows. | MediaDive import normalization for DSMZ 1154. |
| Minor | Thiamine still uses a legacy MIM-keyed link. | `Thiamine` has `mediaingredientmech_term: MediaIngredientMech:000898`, while the June 2026 migration history says legacy MediaIngredientMech IDs were replaced by CHEBI-keyed links. | MIM legacy migration output for `data/normalized_yaml/bacterial/glucose_sulfide_medium_richard_et_al_1985.yaml`. |

## Recommended Edits

1. Recode DSMZ 1154's Vitamin solution as a stock solution and the main medium's Vitamin solution row as a 1 ml stock addition.
2. Preserve the 1000 ml distilled-water rows in the appropriate solution scopes if water rows are represented for direct DSMZ records.
3. Scope the post-autoclave filter-sterilization step to the Vitamin solution rather than flattening it onto the final medium.
4. Replace the lingering `mediaingredientmech_term` on Thiamine with a CHEBI-keyed link or explicitly mark it unresolved if the mapping should stay unavailable.

## Follow-up Checks

- Re-run open LinkML, strict, reference, and term validation after regenerating `data/merge_yaml/merged/glucose_sulfide_medium_richard_et_al_1985.yaml`.
- Compare the regenerated record against the DSMZ 1154 PDF or MediaDive 1154 REST payload and verify the main solution, 1 ml Vitamin solution addition, vitamin stock, preparation steps, and water rows.
- Re-run the exact gitignore-independent search for `mediadive.medium:1154`, `DSMZ_Medium1154.pdf`, and `glucose_sulfide_medium_richard_et_al_1985` across `data/normalized_yaml/` and `data/merge_yaml/merged/`.

## Additional Notes

None found
