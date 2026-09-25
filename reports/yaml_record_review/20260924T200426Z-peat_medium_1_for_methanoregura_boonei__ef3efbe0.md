# YAML Record Review: peat_medium_1_for_methanoregura_boonei

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/peat_medium_1_for_methanoregura_boonei__ef3efbe0.yaml
- Started UTC: 2026-09-24T20:03:13Z
- Finished UTC: 2026-09-24T20:04:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:003270 |
| Label | peat_medium_1_for_methanoregura_boonei |
| Original label | PEAT MEDIUM 1 FOR METHANOREGURA BOONEI |
| Category | bacterial |
| Source identity | JCM Medium J923 |
| Maintained owner | data/normalized_yaml/bacterial/peat_medium_1_for_methanoregura_boonei.yaml |
| Generated review target | data/merge_yaml/merged/peat_medium_1_for_methanoregura_boonei__ef3efbe0.yaml |

`data/merge_yaml/merged/peat_medium_1_for_methanoregura_boonei__ef3efbe0.yaml` is a generated single-source merge from the direct JCM/MediaDive import `data/normalized_yaml/bacterial/peat_medium_1_for_methanoregura_boonei.yaml`.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/peat_medium_1_for_methanoregura_boonei__ef3efbe0.yaml` | Passed; no issues found. |
| Strict CultureMech validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/peat_medium_1_for_methanoregura_boonei__ef3efbe0.yaml --out /private/tmp/peat_medium_1_for_methanoregura_boonei__ef3efbe0.strict.tsv --workers 1 --quiet` | Passed; `/private/tmp/peat_medium_1_for_methanoregura_boonei__ef3efbe0.strict.tsv` had only its header row. |
| Reference validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/peat_medium_1_for_methanoregura_boonei__ef3efbe0.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed with 0 checks. |
| Term validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/peat_medium_1_for_methanoregura_boonei__ef3efbe0.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded curation history | Not run | Not checked: `just validate-history` validates standalone `history/` files, not `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

- `mediadive.medium:J923` resolves to JCM Medium 923, `PEAT MEDIUM 1 FOR METHANOREGURA BOONEI`.
- The pH value of 5.1 is source-supported as the checked final pH of the completed tubes.
- The `bacterial` category is not source-supported. The source is explicitly a `Methanoregura boonei` methanogen medium and uses H2-CO2 anaerobic pressurization.
- The same JCM 923 source is imported separately through TOGO M969 in `data/normalized_yaml/bacterial/TOGO_M969_Peat_Medium_1_For_Methanoregura_Boonei.yaml`, so the corpus has a direct JCM/MediaDive copy and a TOGO copy of one recipe.

## Evidence

JCM 923 supports a scoped protocol:

- Prepare the basal liter from 10 ml Major metals, 1 ml Trace metal 1 solution, and 1 L distilled water; adjust to pH 5.0 with HCl, boil, cool under N2-CO2, dispense 5 ml per Balch tube, and autoclave.
- Complete each 5 ml tube with 0.06 ml of 83 mM TiNTA solution plus 0.05 ml each of 0.5 M HOMOPIPES, Vitamin solution, 2% Yeast extract solution, 50 mM Coenzyme M, and 20 mM Sodium acetate.
- Pressurize inoculated tubes to 70 kPa H2-CO2 and check final pH near 5.1.
- Prepare Major metals, Trace metal 1, 83 mM TiNTA, and Vitamin solution as separate stocks.

The generated record flattens all scopes into one final `ingredients` list:

- It drops the final 10 ml/L Major metals, 1 ml/L Trace metal 1 solution, and 1000 ml/L distilled water rows and stores Major metals and Trace metal 1 stock components as final ingredients.
- It converts 0.05 ml or 0.06 ml per-tube stock additions into 0.05 or 0.06 g/L direct ingredients where the source gives volumes of molar or percent stocks.
- It stores 1 M Tris base, 0.5 M nitrilotriacetic acid disodium salt, and 15% TiCl3 solution volumes from the TiNTA stock as gram-per-liter ingredients.
- It stores Vitamin solution components at stock concentration, not after 0.05 ml is added to a 5 ml tube.

## Completeness

- Consequentially incomplete: no structured representation distinguishes the basal medium, Major metals stock, Trace metal 1 stock, TiNTA stock, Vitamin stock, and tube-completion additions.
- Consequentially incomplete: final water is absent despite JCM listing 1 L distilled water at the main level.
- Consequentially incomplete: gas handling is present only in prose. The record has no structured atmosphere for N2-CO2 cooling or 70 kPa H2-CO2 incubation/tube pressurization.
- Empty optional target-organism collections are not independently defective for this imported medium review.
- No required source or owner was found missing. The ignored-inclusive exact search covered `data/normalized_yaml`, `data/merge_yaml`, `data/import_tracking`, `data/culturemech_id_registry.tsv`, and `data/culturemech_recipe_catalog.tsv`.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | Stock and per-tube addition scopes are flattened into final ingredients. | JCM 923 uses 10 ml Major metals and 1 ml Trace metal 1 per basal liter, then 0.05-0.06 ml sterile additions per 5 ml tube. The record stores stock interiors and tube stock names as top-level `G_PER_L` rows. | data/normalized_yaml/bacterial/peat_medium_1_for_methanoregura_boonei.yaml; MediaDive/JCM importer |
| major | Several final concentrations are dimensionally unsupported. | Source values such as 0.05 ml of 0.5 M HOMOPIPES solution, 0.05 ml of 50 mM Coenzyme M, 7.2 ml of 1 M Tris base, and 0.55 ml of 15% TiCl3 solution are volumes of stocks; the record converts their numeric values to g/L. | data/normalized_yaml/bacterial/peat_medium_1_for_methanoregura_boonei.yaml |
| major | The direct JCM and TOGO imports are split even though they cite the same JCM recipe. | Ignored-inclusive exact search found TOGO M969 with original source JCM_M923 and the same JCM GRMD 923 URL; it generates `data/merge_yaml/merged/PEAT_MEDIUM_1_FOR_METHANOREGURA_BOONEI.yaml` separately. | data/normalized_yaml/bacterial/peat_medium_1_for_methanoregura_boonei.yaml; data/normalized_yaml/bacterial/TOGO_M969_Peat_Medium_1_For_Methanoregura_Boonei.yaml |
| major | The category is wrong or at least unsupported. | The recipe is for a Methanoregura boonei methanogen medium and includes N2-CO2 and H2-CO2 anaerobic handling, but both JCM and TOGO imports are filed under `bacterial`. | data/normalized_yaml/bacterial/peat_medium_1_for_methanoregura_boonei.yaml |
| minor | A few source chemicals still need exact grounding after structural repair. | `HOMOPIPES` and `TiCl3` are ungrounded; `NiCl2 x 6 H2O` is grounded to an anhydrous nickel chloride term; `MnSO4 x n H2O` is grounded to a generic manganese sulfate term. | data/normalized_yaml/bacterial/peat_medium_1_for_methanoregura_boonei.yaml |

## Recommended Edits

1. Remodel `data/normalized_yaml/bacterial/peat_medium_1_for_methanoregura_boonei.yaml` with explicit solution scopes for Major metals, Trace metal 1, 83 mM TiNTA, Vitamin solution, and sterile per-tube additions.
2. Convert per-tube 0.05 ml and 0.06 ml additions into volume-based additions relative to the 5 ml basal tubes rather than gram-per-liter rows.
3. Keep gas-phase and pressure instructions as preparation or atmosphere data scoped to cooling, dispensing, and inoculated incubation.
4. Merge or retire the TOGO M969 duplicate so the JCM 923 recipe has one canonical record.
5. Verify the taxonomic category for Methanoregura boonei and move the maintained record out of `data/normalized_yaml/bacterial/` if the corpus files methanogen media under `archaea`.
6. Re-ground the ungrounded or hydrate-ambiguous ingredients after the recipe structure is fixed.
7. Regenerate merged YAML and any downstream pages from the corrected normalized record.

## Follow-up Checks

1. Rerun open schema, strict, reference, and term validation against the regenerated JCM 923 merged record.
2. Manually compare the regenerated record against JCM GRMD 923 and confirm that every numeric value remains attached to the original liter stock, 5 ml tube, or final medium scope.
3. Confirm an ignored-inclusive exact search for `GRMD=923` no longer finds two active generated Peat Medium 1 records.
4. Confirm `data/import_tracking/reports/concentration_plausibility.tsv` no longer flags `CultureMech:003270` for stock-strength trace-metal or vitamin quantities.

## Additional Notes

- Exact ignored-inclusive searches were used while resolving the duplicate TOGO M969 import; ignored files were included.
