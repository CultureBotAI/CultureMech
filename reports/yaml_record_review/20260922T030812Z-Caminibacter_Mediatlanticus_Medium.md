# YAML Record Review: Caminibacter Mediatlanticus Medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/Caminibacter_Mediatlanticus_Medium.yaml`
- Started UTC: 2026-09-22T03:05:19Z
- Finished UTC: 2026-09-22T03:08:12Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/Caminibacter_Mediatlanticus_Medium.yaml` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M3122_Caminibacter_Mediatlanticus_Medium.yaml` |
| ID | `CultureMech:009594` |
| Name | `caminibacter_mediatlanticus_medium` |
| Source accession | `TOGO:M3122` |
| Original source URL | `https://www.dsmz.de/microorganisms/medium/pdf/DSMZ_Medium792b.pdf` |
| Source title | `Caminibacter Mediatlanticus Medium` |
| Category | `bacterial` |
| Medium/composition/state | `COMPLEX` / `UNDEFINED` / `LIQUID` |
| Merge lineage | Single-source merge from `TOGO_M3122_Caminibacter_Mediatlanticus_Medium` on fingerprint `18841552c9a8f10d19cbe1e71df8298cf05fc39b948de0345fa6805d3bb4c884` |

The reviewed file is a generated one-source merge. Future edits belong in `data/normalized_yaml/bacterial/TOGO_M3122_Caminibacter_Mediatlanticus_Medium.yaml` or in the TOGO import/solution-migration logic, then `data/merge_yaml/merged/Caminibacter_Mediatlanticus_Medium.yaml` should be regenerated.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/Caminibacter_Mediatlanticus_Medium.yaml` | Pass. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/Caminibacter_Mediatlanticus_Medium.yaml --out /private/tmp/Caminibacter_Mediatlanticus_Medium.strict.tsv --workers 1 --quiet` | Pass: 1 file scanned; 0 files with errors; report at `/private/tmp/Caminibacter_Mediatlanticus_Medium.strict.tsv`. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/Caminibacter_Mediatlanticus_Medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass: 1 file validated; 0 reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/Caminibacter_Mediatlanticus_Medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass. |
| Embedded curation history | `just validate-history ...` | Not checked: the documented history validator validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` events. |

The offline, no-project `uv` workaround above was used because the project environment currently attempts to build `llvmlite==0.46.0` under Python 3.13 and fails inside setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`.

## Identity and Grounding

- **Source identity:** TOGO M3122 resolves to DSMZ `DSMZ_Medium792b.pdf`; both the TOGO API and DSMZ PDF identify the same `Caminibacter Mediatlanticus Medium`.
- **Record identity:** The generated record and maintained TOGO owner keep `TOGO:M3122` and the DSMZ Medium 792b original URL, so they identify the right medium even though the formulation is flattened.
- **Active duplicate:** A gitignore-independent `find data/merge_yaml/merged data/normalized_yaml -iname '*caminibacter*' -print` found an active direct DSMZ record, `data/normalized_yaml/bacterial/caminibacter_mediatlanticus_medium.yaml` (`CultureMech:001934`, `mediadive.medium:792b`), for the same DSMZ Medium 792b formula. A gitignore-independent `rg --no-ignore --hidden` over normalized records, generated merges, registries, catalogs, and import reports confirmed both `CultureMech:009594` and `CultureMech:001934` are active.
- **Classification:** `COMPLEX` / `UNDEFINED` does not match DSMZ 792b: its components are named salts, gas mixtures, and three simple solutions. The direct DSMZ 792b record already classifies the recipe as `DEFINED` / `DEFINED`.
- **Ingredient grounding:** Most salt identities are grounded to appropriate CHEBI terms, and term validation passed. `KI (0.01% w/v)` and `Sodium resazurin (0.1% w/v)` remain ungrounded in the TOGO owner, and `KNO3` still carries a legacy `mediaingredientmech_term` link instead of `mediaingredientmech_chebi_term`.

## Evidence

| Claim | Support |
|---|---|
| Solution topology | Unsupported in the active TOGO owner. TOGO and DSMZ both define a final medium assembled from Solution A 989 ml, Solution B 10 ml, and Solution C 10 ml. The generated record stores those additions as `989`, `10`, and `10` `G_PER_L` solution records and also flattens the solution ingredients to top-level rows. |
| Main-medium components | Partially supported. Source Solution A contains NaCl 30 g, MgSO4 x 7 H2O 3.5 g, MgCl2 x 6 H2O 2.75 g, CaCl2 x 2 H2O 0.75 g, KCl 0.33 g, NaBr 0.05 g, H3BO3 15 mg, 7 ml 0.1% SrCl2 x 6 H2O, 0.5 ml 0.01% KI, 0.5 ml 0.1% sodium resazurin, 1 ml Wolfe's mineral elixir, and 980 ml distilled water. The record represents the three stock additions as gram-per-liter rows, not milliliter additions. |
| Wolfe's mineral elixir | Unsupported at final-medium level. The source adds 1 ml Wolfe's mineral elixir to Solution A and separately defines the Wolfe stock in 1000 ml water adjusted first to pH 1.0 with diluted H2SO4. The TOGO owner flattens those stock rows into the top-level medium and adds the stock salts to matching final salts: MgSO4 x 7 H2O 3.5 + 30 -> 33.5 g/L, NaCl 30 + 10 -> 40 g/L, CaCl2 x 2 H2O 0.75 + 1 -> 1.75 g/L, and H3BO3 15 mg + 0.1 g -> 15.1 g/L. |
| Water arithmetic | Unsupported. DSMZ uses 980 ml distilled water in Solution A, 10 ml in Solution B, 10 ml in Solution C, and 1000 ml inside Wolfe's mineral elixir. The active TOGO record merged those four rows into one top-level `2000.0 G_PER_L` water ingredient. |
| Conditions and preparation | Incomplete. DSMZ specifies pH 5.7, sparging Solution A with 80% H2 / 20% CO2 for 30-45 min before dispensing and autoclaving under the same atmosphere, autoclaving Solution B under 80% N2 / 20% CO2, autoclaving Solution C under 100% N2, and pressurizing inoculated vials with 80% H2 / 20% CO2 to 2 bar overpressure. The TOGO owner has no `ph_value` or `preparation_steps` and models carbon dioxide, hydrogen, and nitrogen as variable ingredients. |

## Completeness

- The record preserves the right TOGO and DSMZ accessions but not the formulation hierarchy needed to reproduce DSMZ Medium 792b.
- The direct DSMZ 792b normalized sibling already demonstrates part of the needed fix by nesting Wolfe's mineral elixir under `solutions` at `1 ML_PER_L`; the active TOGO record still needs that repair and still needs Solution A, Solution B, and Solution C modeled as solution boundaries instead of G/L stubs.
- The active TOGO owner is flagged by existing import reports: `merged_duplicates.tsv` lists the water, MgSO4, NaCl, CaCl2, and H3BO3 rows as sums of differing parts, while `concentration_plausibility.tsv` flags `2000 G_PER_L` water and five trace-salt rows as stock-solution magnitudes.
- Empty organism/growth slots were not treated as defects in this review; DSMZ 792b is a source recipe, not a growth-evidence record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | DSMZ solution structure and final-volume arithmetic are flattened. | TOGO/DSMZ specify Solution A 989 ml, Solution B 10 ml, and Solution C 10 ml; the YAML records them as 989/10/10 `G_PER_L` solution stubs and also emits their internals as top-level final ingredients. | `data/normalized_yaml/bacterial/TOGO_M3122_Caminibacter_Mediatlanticus_Medium.yaml` and the TOGO solution migrator. |
| Major | Wolfe's mineral elixir is flattened into the final medium. | DSMZ adds 1 ml Wolfe's mineral elixir to Solution A and defines a separate 1 L acidified Wolfe stock; the TOGO owner keeps a `1 G_PER_L` Wolfe row and stock-strength Fe, Co, Zn, Cu, Al, Mo, Mn, Ni, W, and Se rows at the medium level. | Replace the placeholder in the TOGO owner with a nested solution reference, using the existing `data/normalized_yaml/bacterial/wolfes_mineral_elixir_medium_792.yaml` or an equivalent source-owned solution. |
| Major | Duplicate rows across main medium and stock solutions have been summed. | The record reports `Distilled water` 2000.0 g/L, `MgSO4 x 7 H2O` 33.5 g/L, `NaCl` 40.0 g/L, `CaCl2 x 2 H2O` 1.75 g/L, and `H3BO3` 15.1 g/L, all explicitly annotated as merges of distinct DSMZ rows from different solution contexts. | Fix `data/normalized_yaml/bacterial/TOGO_M3122_Caminibacter_Mediatlanticus_Medium.yaml`; prevent cross-solution duplicate summing in the importer/cleanup path. |
| Major | Preparation, atmosphere, and pH claims are stored in the wrong shape or missing. | DSMZ 792b states pH 5.7 and gives gas-specific sparging, autoclaving, post-inoculation pressurization, and fresh-use instructions. The TOGO record lacks `preparation_steps` and stores CO2, H2, N2, and an empty variable H2SO4 solution as ingredients/solutions. | Add source-supported preparation steps and pH to the TOGO owner; move gases and H2SO4 to the relevant preparation or Wolfe-stock representation. |
| Major | The same DSMZ 792b source recipe is active twice. | `data/culturemech_recipe_catalog.tsv` marks both `data/normalized_yaml/bacterial/TOGO_M3122_Caminibacter_Mediatlanticus_Medium.yaml` (`TOGO:M3122`) and `data/normalized_yaml/bacterial/caminibacter_mediatlanticus_medium.yaml` (`mediadive.medium:792b`) active with the same normalized slug. | Decide whether to merge TOGO M3122 into the direct DSMZ 792b record, mark one as source-duplicate metadata, or update merge rules so only one canonical recipe reaches `data/merge_yaml/merged`. |
| Minor | The generated record keeps stale or missing ingredient groundings for several imported rows. | `KI (0.01% w/v)` and `Sodium resazurin (0.1% w/v)` have no primary `term`, and `KNO3` still has only `mediaingredientmech_term: MediaIngredientMech:000170` despite the CHEBI migration history. | Ground exact stock-solution identities in the TOGO owner after the solution boundaries are restored. |

## Recommended Edits

1. Curate `data/normalized_yaml/bacterial/TOGO_M3122_Caminibacter_Mediatlanticus_Medium.yaml` to preserve DSMZ Medium 792b's three-solution assembly, including Solution A 989 ml, Solution B 10 ml, Solution C 10 ml, and pH 5.7.
2. Replace top-level Wolfe salts with a `1 ML_PER_L` Wolfe's mineral elixir solution link or inline nested solution equivalent to `data/normalized_yaml/bacterial/wolfes_mineral_elixir_medium_792.yaml`.
3. Delete the summed cross-solution rows and keep main-medium Solution A, Solution B, Solution C, and Wolfe-stock quantities in their original compartments.
4. Convert the 0.5 ml sodium resazurin, 7 ml SrCl2, 0.5 ml KI, and 1 ml Wolfe additions from grams per liter to milliliter stock additions.
5. Encode the DSMZ gas handling as preparation steps: 80% H2 / 20% CO2 for Solution A and post-inoculation headspace, 80% N2 / 20% CO2 for Solution B, and 100% N2 for Solution C.
6. Reconcile `CultureMech:009594` with the direct DSMZ 792b record `CultureMech:001934` so there is one canonical generated recipe for DSMZ Medium 792b instead of two active `caminibacter_mediatlanticus_medium` records.

## Follow-up Checks

- Rerun open schema, strict schema, term, and reference validation on `data/normalized_yaml/bacterial/TOGO_M3122_Caminibacter_Mediatlanticus_Medium.yaml`.
- Rerun the concentration-plausibility and merged-duplicate audits and confirm this record no longer emits `WATER_AS_VOLUME`, `TRACE_SALT_AS_STOCK`, or `DIFFERING_PARTS` rows.
- Regenerate merged recipes and confirm the TOGO M3122 and direct DSMZ 792b records either merge into a single canonical record or are linked as intentional source duplicates.
- Manually compare the regenerated record against TOGO M3122 and `DSMZ_Medium792b.pdf`: all Solution A/B/C volumes, Wolfe's mineral elixir, pH 5.7, and gas-preparation steps should match source text.

## Additional Notes

- MediaDive rejected simple HEAD probes for `/rest/medium/792b` and `/medium/792b` with HTTP 405 during this review; I used the stored DSMZ PDF and the TOGO M3122 API as the inspected sources.
- The direct DSMZ 792b sibling has a `data_quality_flags: ingredients_curated` marker and a 2026-09-13 `repair_komodo_792_pyrolobus_score10.py` curation event, but it still predates any reconciliation with the active TOGO M3122 duplicate.
