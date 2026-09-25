# YAML Record Review: MMJS MEDIUM (modified)

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/mmjs_medium_modified__2e58856f.yaml
- Started UTC: 2026-09-24T09:26:07Z
- Finished UTC: 2026-09-24T09:27:09Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| Stable ID | CultureMech:000558 |
| Record name | mmjs_medium_modified |
| Original name | MMJS MEDIUM (modified) |
| Category | bacterial |
| Source accession | mediadive.medium:1121 |
| Reviewed generated file | data/merge_yaml/merged/mmjs_medium_modified__2e58856f.yaml |
| Maintained owner | data/normalized_yaml/bacterial/mmjs_medium_modified.yaml |
| Merge source | mmjs_medium_modified |
| Merge fingerprint | 2e58856f7e228db8081cb93d87a207477f5dbbc71c38135427e0bffd9d87e210 |

The reviewed file is a generated one-source merge from the maintained MediaDive / DSMZ 1121 normalized record. Direct corrections belong in `data/normalized_yaml/bacterial/mmjs_medium_modified.yaml`; stock-flattening and exact-form grounding problems that recur across MediaDive imports should be fixed at the importer or enrichment layer.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/mmjs_medium_modified__2e58856f.yaml` | Passed; `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/mmjs_medium_modified__2e58856f.yaml --out /private/tmp/mmjs_medium_modified__2e58856f.strict.tsv --workers 1 --quiet` | Passed; one file scanned, zero error rows. `/private/tmp/mmjs_medium_modified__2e58856f.strict.tsv` had one line, the header only. |
| Reference links | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/mmjs_medium_modified__2e58856f.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed structurally; the validator ran zero reference checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/mmjs_medium_modified__2e58856f.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. |
| Embedded history | Not run for this merged record. | Not checked: `just validate-history` validates standalone files under `history/`, not `MediaRecipe.curation_history` inside merged YAML. |

The validators accepted the flattened generated record. They do not verify whether a 10 ml/L or 1 ml/L stock was preserved as a stock or mistakenly promoted to a direct final-medium concentration.

## Identity and Grounding

The core source identity is correct:

- `CultureMech:000558` and `mediadive.medium:1121` identify DSMZ Medium 1121, `MMJS MEDIUM (modified)`.
- `find data/normalized_yaml -name mmjs_medium_modified.yaml -print` resolved the maintained owner to `data/normalized_yaml/bacterial/mmjs_medium_modified.yaml`.
- The fetched MediaDive REST payload for medium 1121 reports the same label, source `DSMZ`, pH 6.8, `complex_medium: no`, and the DSMZ Medium 1121 PDF URL.

The record is not unique in the maintained corpus:

- An ignored-aware exact search for `mediadive.medium:1121`, `komodo.medium:1121`, `CultureMech:003824`, and `KOMODO_1121_MMJS_MEDIUM_modified` across normalized and merged YAML found a second maintained record, `data/normalized_yaml/bacterial/KOMODO_1121_MMJS_MEDIUM_modified.yaml`, that was enriched from the same DSMZ / MediaDive medium, plus its generated merge `data/merge_yaml/merged/mmjs_medium_modified.yaml`.

Exact ingredient grounding remains incomplete:

- DSMZ says `Sulfur, powdered`, but the generated record grounds `Sulfur` to `CHEBI:26833`, `sulfur atom`.
- DSMZ says `NiCl2 x 6 H2O`, but the generated record grounds it to `CHEBI:34887`, `nickel dichloride`, the anhydrous salt.
- DSMZ variable hydrates `MnSO4 x n H2O` and `Fe2(SO4)3 x n H2O` are grounded to non-hydrated sulfate salts.
- `KI` still uses the old `mediaingredientmech_term` slot instead of `mediaingredientmech_chebi_term`.

## Evidence

The MediaDive REST payload and DSMZ Medium 1121 PDF agree on the relevant structure:

- The main recipe contains direct salts, 3 g powdered sulfur, 10 ml Trace mineral solution, 1000 ml distilled water, 1 ml/L Vitamin solution, and final 0.2% NaHCO3.
- The Trace mineral solution is a 1000 ml stock containing nitrilotriacetic acid, MnSO4 x n H2O, CoSO4 x 7 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, AlK(SO4)2 x 12 H2O, H3BO3, Na2MoO4 x 2 H2O, SrCl2 x 6 H2O, NaBr, KI, NiCl2 x 6 H2O, Na2SeO3 x 5 H2O, Fe2(SO4)3 x n H2O, H2WO4, and distilled water.
- The Vitamin solution is a 1000 ml stock containing biotin, folic acid, pyridoxine hydrochloride, thiamine hydrochloride dihydrate, riboflavin, nicotinic acid, D-Calcium pantothenate, vitamin B12, p-aminobenzoic acid, lipoic acid, and distilled water.
- The preparation text adjusts pH with NaOH to 6.8, steams the medium for 3 hours on each of 3 successive days, adds separately autoclaved concentrated solutions, purges 80% N2 / 20% CO2 for 5 minutes, and compresses 79% N2 / 20% CO2 / 1% O2 into the headspace at 2 atm.

The record preserves the pH and imports that preparation text as two coarse `preparation_steps`, but it still drops the stock structure:

- There is no `solutions` array for the 10 ml/L Trace mineral solution or the 1 ml/L Vitamin solution.
- Trace-mineral stock rows are final-medium ingredients at stock concentration. Nitrilotriacetic acid is stored as 1.5 g/L instead of 0.015 g/L final, and H2WO4 is stored as 0.1 g/L instead of 0.001 g/L final.
- Vitamin-stock rows are final-medium ingredients at stock concentration. Biotin is stored as 0.002 g/L instead of 0.000002 g/L final.
- Distilled water rows that define the main and stock final volumes are omitted, so the flattening has no local volume context.

## Completeness

Consequential gaps:

- The two source stocks are absent as first-class solutions and their components are not diluted into final-medium concentrations.
- The preparation strings preserve DSMZ wording but cannot point to the separately autoclaved concentrated solutions because those solution objects are missing.
- The same DSMZ 1121 identity is represented in two maintained normalized records and two generated merge outputs.

Empty optional fields for target organisms, variants, growth evidence, and storage were not treated as defects on their own.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Trace mineral and vitamin stocks were flattened at stock strength. | DSMZ and MediaDive add Trace mineral solution at 10 ml/L and Vitamin solution at 1 ml/L. The generated record promotes each stock formula row to a direct ingredient without applying the 100-fold or 1000-fold dilution. | `data/normalized_yaml/bacterial/mmjs_medium_modified.yaml`; repeated MediaDive flattening belongs in the importer. |
| Major | The duplicate DSMZ 1121 identity is unresolved. | `mediadive.medium:1121` is represented here, while the KOMODO 1121 record in `data/normalized_yaml/bacterial/KOMODO_1121_MMJS_MEDIUM_modified.yaml` was enriched from the same `mediadive.medium:1121` source and still generates a separate `mmjs_medium_modified.yaml` merge. | Merge rules plus both maintained DSMZ 1121 normalized records. |
| Major | Preparation steps are too coarse after stock flattening. | The first generated step mentions separately autoclaved concentrated solutions, but no Trace mineral or Vitamin solution objects remain for those additions, and final NaHCO3 is only a direct ingredient. | `data/normalized_yaml/bacterial/mmjs_medium_modified.yaml` and the MediaDive preparation importer. |
| Major | Exact ingredient grounding is not source-faithful for several forms. | Powdered sulfur is grounded to a sulfur atom; nickel dichloride hexahydrate is grounded to anhydrous nickel dichloride; variable hydrate sulfates are grounded to non-hydrated salts; KI still has a legacy MIM slot. | `data/normalized_yaml/bacterial/mmjs_medium_modified.yaml` and the ingredient enrichment layers. |

## Recommended Edits

1. Restore MediaDive solution 2253 as `Trace mineral solution` used at 10 ml/L and MediaDive solution 584 as `Vitamin solution` used at 1 ml/L, or explicitly dilute their ingredients if the final model must be denormalized.

2. Split the MediaDive preparation text into source-scoped steps that can reference the 5% NaHCO3 solution and the sterilized stock additions instead of leaving them as unlinked prose.

3. Resolve the duplicate DSMZ 1121 representation with `data/normalized_yaml/bacterial/KOMODO_1121_MMJS_MEDIUM_modified.yaml` so the two imports merge or one is superseded.

4. Reground powdered sulfur, nickel dichloride hexahydrate, the variable-hydrate sulfates, and the stale KI MIM link with exact source-form semantics.

5. Regenerate `data/merge_yaml/merged/mmjs_medium_modified__2e58856f.yaml` and derived page outputs from the maintained normalized input.

## Follow-up Checks

- Diff the corrected normalized record against `https://mediadive.dsmz.de/rest/medium/1121` and the DSMZ Medium 1121 PDF.
- Rerun the focused open-schema, strict, reference, and term validators on `data/normalized_yaml/bacterial/mmjs_medium_modified.yaml`.
- Run merge verification and confirm DSMZ 1121 no longer emits one KOMODO merge and one direct MediaDive merge.
- Manually verify that the trace-mineral and vitamin formulas are nested or correctly diluted and that the preparation steps refer to the restored stock additions.

## Additional Notes

- `medium_type: DEFINED` and `composition_type: DEFINED` are supported by the inspected DSMZ / MediaDive formulation.
- This direct MediaDive record is closer to the source than the sibling KOMODO enrichment because it retained MediaDive preparation text and did not convert NaOH into a direct variable ingredient.
