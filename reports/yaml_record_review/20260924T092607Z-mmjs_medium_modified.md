# YAML Record Review: MMJS MEDIUM (modified)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mmjs_medium_modified.yaml
- Started UTC: 2026-09-24T09:23:57Z
- Finished UTC: 2026-09-24T09:26:07Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:003824 |
| Record name | mmjs_medium_modified |
| Original name | MMJS MEDIUM (modified) |
| Category | bacterial |
| Source accession | komodo.medium:1121 |
| DSMZ / MediaDive source | mediadive.medium:1121 |
| Reviewed generated file | data/merge_yaml/merged/mmjs_medium_modified.yaml |
| Maintained owner | data/normalized_yaml/bacterial/KOMODO_1121_MMJS_MEDIUM_modified.yaml |
| Merge source | KOMODO_1121_MMJS_MEDIUM_modified |
| Merge fingerprint | 3da35bcba1e3041810c7b8c7d94f375d8bab85f826dbf0f66c8074b09a3e9882 |

The reviewed file is a generated one-source merge from a maintained KOMODO 1121 import that was enriched from DSMZ / MediaDive medium 1121. Direct curation belongs in `data/normalized_yaml/bacterial/KOMODO_1121_MMJS_MEDIUM_modified.yaml`; repeated DSMZ enrichment issues should be fixed at the enrichment or importer layer before regenerating the merged YAML.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mmjs_medium_modified.yaml` | Passed; `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mmjs_medium_modified.yaml --out /private/tmp/mmjs_medium_modified.strict.tsv --workers 1 --quiet` | Passed; one file scanned, zero error rows. `/private/tmp/mmjs_medium_modified.strict.tsv` had one line, the header only. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mmjs_medium_modified.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed structurally; the validator ran zero reference checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mmjs_medium_modified.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run for this merged record. | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` inside merged YAML. |

The record passes structural validation despite losing DSMZ stock boundaries, omitting DSMZ preparation instructions, and retaining duplicate source identity.

## Identity and Grounding

The reviewed record resolves to the intended KOMODO / DSMZ recipe:

- `CultureMech:003824`, `komodo.medium:1121`, and the notes all point at DSMZ / MediaDive medium 1121, `MMJS MEDIUM (modified)`.
- `find data/normalized_yaml -name KOMODO_1121_MMJS_MEDIUM_modified.yaml -print` resolved the maintained owner exactly.
- The fetched MediaDive REST payload for medium 1121 reports `complex_medium: no`, pH 6.8, source `DSMZ`, and the DSMZ Medium 1121 PDF URL.

There is also a duplicate-identity risk:

- An ignored-aware exact search for `mediadive.medium:1121`, `komodo.medium:1121`, `CultureMech:003824`, and `KOMODO_1121_MMJS_MEDIUM_modified` across normalized and merged YAML found a second normalized record, `data/normalized_yaml/bacterial/mmjs_medium_modified.yaml`, and a second generated merge, `data/merge_yaml/merged/mmjs_medium_modified__2e58856f.yaml`, for the same MediaDive source.

Several ingredients still need exact-form review:

- DSMZ says `Sulfur, powdered`, but the generated record grounds `Sulfur` to `CHEBI:26833`, `sulfur atom`.
- DSMZ says `NiCl2 x 6 H2O`, but the generated record grounds it to `CHEBI:34887`, `nickel dichloride`, the anhydrous salt.
- DSMZ variable hydrates `MnSO4 x n H2O` and `Fe2(SO4)3 x n H2O` are grounded to non-hydrated sulfate salts; these may need to remain unresolved unless an exact variable-hydrate representation is available.
- `KI` still carries the legacy `mediaingredientmech_term` shape instead of `mediaingredientmech_chebi_term`.

## Evidence

The inspected DSMZ / MediaDive source supports the main formula and nested stocks:

- Main medium: 20 g NaCl, 0.09 g K2HPO4, 0.07 g KH2PO4, 0.80 g CaCl2 x 2 H2O, 1.25 g NH4Cl, 4.00 g MgSO4 x 7 H2O, 3.00 g MgCl2 x 6 H2O, 0.33 g KCl, 0.01 g Fe-citrate, 0.01 g FeSO4 x 7 H2O, 3.00 g Na2S2O3 x 5 H2O, 3.00 g powdered sulfur, 10 ml Trace mineral solution, 1000 ml distilled water, 1.0 ml/L Vitamin solution, and 0.2% final NaHCO3.
- Trace mineral solution: a 1000 ml stock with nitrilotriacetic acid, MnSO4 x n H2O, CoSO4 x 7 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2 x 12 H2O, H3BO3, Na2MoO4 x 2 H2O, SrCl2 x 6 H2O, NaBr, KI, NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, Fe2(SO4)3 x n H2O, H2WO4, and distilled water.
- Vitamin solution: a 1000 ml stock with biotin, folic acid, pyridoxine hydrochloride, thiamine hydrochloride dihydrate, riboflavin, nicotinic acid, D-Calcium pantothenate, vitamin B12, p-aminobenzoic acid, lipoic acid, and distilled water.
- Preparation: adjust pH with NaOH to 6.8, steam the medium for 3 hours on each of 3 successive days, add separately autoclaved concentrated solutions, purge an 80% N2 / 20% CO2 gas mix for 5 minutes, then compress 79% N2 / 20% CO2 / 1% O2 into the headspace at 2 atm.

The generated record matches the main-medium direct salt quantities and pH value but diverges on solution scoping:

- It has no `solutions` array for the 10 ml/L Trace mineral solution or 1 ml/L Vitamin solution.
- All Trace mineral solution ingredients are flattened into final-medium `ingredients` at the stock concentration. For example, nitrilotriacetic acid is stored as 1.5 g/L instead of 0.015 g/L final, and H2WO4 is stored as 0.1 g/L instead of 0.001 g/L final.
- All Vitamin solution ingredients are flattened into final-medium `ingredients` at the stock concentration. For example, biotin is stored as 0.002 g/L instead of 0.000002 g/L final.
- Distilled water entries from the main medium and both stocks are omitted.
- NaOH is converted from pH adjustment text into a variable direct ingredient.

## Completeness

Consequential gaps:

- The two DSMZ stocks are erased as solutions, so a reader cannot distinguish final salts from 1000 ml stock formulas.
- The DSMZ steam-sterilization schedule, separately autoclaved concentrated solutions, gas purge, final 79:20:1 gas headspace, and 2 atm compression are absent.
- The current record has only a prose `notes` mention of `mediadive.medium:1121`; it has no structured MediaDive source cross-reference even though another maintained record in this corpus already uses that accession.
- The duplicate `mediadive.medium:1121` normalized record means this record may not be the canonical local representation of DSMZ 1121 after merge rules are improved.

Empty optional fields for target organisms, variants, and storage were not treated as defects on their own.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Trace mineral and vitamin stocks were flattened at stock strength. | MediaDive and the DSMZ PDF add Trace mineral solution at 10 ml/L and Vitamin solution at 1 ml/L. The generated record contains all stock ingredients directly at the 1000 ml stock concentrations, making trace-mineral entries 100x too high and vitamin entries 1000x too high in the final medium. | `data/normalized_yaml/bacterial/KOMODO_1121_MMJS_MEDIUM_modified.yaml`; recurring flattening fixes belong in the DSMZ enrichment/import path. |
| Major | DSMZ preparation and gas conditions are mostly missing. | The record keeps `ph_value: 6.8` and a variable NaOH ingredient, but omits three 3-hour steaming cycles, separately autoclaved concentrated additions, 80% N2 / 20% CO2 purging, and a final 79% N2 / 20% CO2 / 1% O2 headspace at 2 atm. | `data/normalized_yaml/bacterial/KOMODO_1121_MMJS_MEDIUM_modified.yaml`. |
| Major | The medium has duplicate source identity in the maintained corpus. | This KOMODO record is explicitly enriched from `mediadive.medium:1121`, and an ignored-aware exact search found `data/normalized_yaml/bacterial/mmjs_medium_modified.yaml` plus `data/merge_yaml/merged/mmjs_medium_modified__2e58856f.yaml` carrying the same MediaDive source accession. | Merge rules and the two maintained normalized records that represent DSMZ / MediaDive 1121. |
| Major | Exact ingredient grounding is not fully source-faithful. | Powdered sulfur is grounded to a sulfur atom; nickel dichloride hexahydrate is grounded to anhydrous nickel dichloride; two variable hydrates are grounded to non-hydrated salts; KI still uses a legacy MIM slot. | `data/normalized_yaml/bacterial/KOMODO_1121_MMJS_MEDIUM_modified.yaml` and the ingredient enrichment layers. |

## Recommended Edits

1. Restore `Trace mineral solution` and `Vitamin solution` as nested solutions at their DSMZ usage rates, or divide every stock ingredient by the correct dilution factor if the project deliberately denormalizes stocks into final concentrations.

2. Add DSMZ preparation steps for NaOH pH adjustment, fractional steaming, separately autoclaved concentrated solutions, N2/CO2 purging, the final N2/CO2/O2 gas phase, and 2 atm compression.

3. Add or repair structured source provenance for the DSMZ / MediaDive source, then resolve whether the KOMODO 1121 record should merge with or be superseded by `data/normalized_yaml/bacterial/mmjs_medium_modified.yaml`.

4. Reground powdered sulfur, nickel dichloride hexahydrate, variable-hydrate manganese and ferric sulfate, and stale KI with the exact-form MIM and CHEBI resolver.

5. Regenerate `data/merge_yaml/merged/mmjs_medium_modified.yaml` and derived page outputs from the maintained normalized input.

## Follow-up Checks

- Diff the corrected YAML against both `https://mediadive.dsmz.de/rest/medium/1121` and the DSMZ Medium 1121 PDF.
- Rerun the focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/KOMODO_1121_MMJS_MEDIUM_modified.yaml`.
- Run merge verification to confirm DSMZ / MediaDive 1121 no longer generates two unmerged canonical records.
- Manually confirm that trace-mineral entries are either nested or diluted 100-fold, vitamin entries are either nested or diluted 1000-fold, and NaOH is scoped to pH adjustment instead of a direct final ingredient.

## Additional Notes

- The MediaDive REST formula and the DSMZ PDF agree on the pH 6.8 value and the main formula amounts checked here.
- `medium_type: DEFINED` and `composition_type: DEFINED` are supported by the inspected DSMZ recipe once the two defined stock solutions are represented correctly.
