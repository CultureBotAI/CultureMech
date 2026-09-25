# YAML Record Review: bacillus_tusciae_medium_add_agar

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/bacillus_tusciae_medium_add_agar.yaml
- Started UTC: 2026-09-21T18:10:20Z
- Finished UTC: 2026-09-21T18:12:17Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| Generated record | `data/merge_yaml/merged/bacillus_tusciae_medium_add_agar.yaml` |
| Generated ID | `CultureMech:008976` |
| Label | `bacillus_tusciae_medium_add_agar` |
| Source | TOGO Medium M2393 |
| Maintained owner | `data/normalized_yaml/bacterial/bacillus_tusciae_medium_add_agar.yaml` |
| Merge fingerprint | `87ae6875cd10a73a0e1eec074781b6cd120f26f0f26a18b6eb6a7be4b4c0bf94` |

The generated target is a single-source merge from `data/normalized_yaml/bacterial/bacillus_tusciae_medium_add_agar.yaml`. The generated file is stale relative to its normalized owner for the water duplicate repair, and all substantive fixes belong upstream in the normalized TOGO M2393 owner or source transform.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bacillus_tusciae_medium_add_agar.yaml` | Passed |
| Strict closed schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bacillus_tusciae_medium_add_agar.yaml --out /private/tmp/bacillus_tusciae_medium_add_agar.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with errors, 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bacillus_tusciae_medium_add_agar.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed: 0 checks, all validations passed |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bacillus_tusciae_medium_add_agar.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone `history/` files |

## Identity and Grounding

TOGO Medium M2393 is a Bacillus Tusciae Medium variant that adds 15 g agar to the Medium 369 / Medium 261 formulation. The agar addition and `SOLID_AGAR` physical state are correctly represented, but the pH, temperature, and gas-atmosphere overlay that makes this a DSMZ Medium 369 Bacillus tusciae recipe are absent.

The direct salt groundings are mostly coherent. `MgSO4 x 7 H2O` still has a stale generic `mediaingredientmech_chebi_term`, while `NiCl2 x 6 H2O` is grounded as anhydrous nickel dichloride. `Na2MoO4 x 2 H2O` has the right ChEBI term but a schema-defaulted `VARIABLE` concentration after TOGO M2393 omitted its SL-6 amount.

## Evidence

The TOGO M2393 API payload lists the same Medium 260/261-derived basal components as TOGO M2392, with explicit agar at 15 g and with 3 ml `Trace element solution SL-6`. It links to DSMZ Medium 369, whose text says to adjust Medium 261 to pH 4.0 and incubate at 50 C without agitation under 5% O2, 10% CO2, and 45% H2. DSMZ Medium 261 says to use Medium 260 without pyruvate.

DSMZ Medium 27 supports the SL-6 stock recipe, including `Na2MoO4 x 2 H2O` at 0.03 g/L stock. The generated and normalized M2393 rows put H3BO3, MnCl2, CoCl2, NiCl2, ZnSO4, CuCl2, and variable Na2MoO4 at the top level, but all of those are stock ingredients within the 3 ml/L SL-6 addition.

## Completeness

Consequential gaps:

- Missing Bacillus tusciae pH 4.0.
- Missing Bacillus tusciae incubation temperature and O2/CO2/H2 atmosphere.
- Missing the correct 3 ml/L unit on the SL-6 stock addition.
- Duplicating the SL-6 stock salts as top-level final-medium ingredients at stock strength.
- Losing `Na2MoO4 x 2 H2O` amount entirely to `VARIABLE`.
- Importing DSMZ 5 mg ferric ammonium citrate as 5 g/L.
- Importing water as g/L, with generated water stale at 2000 g/L after the normalized owner was repaired to 1000.

Explicit target-organism and growth-evidence fields are optional here. This review verified TOGO M2393 and the DSMZ Medium 369, 261, 260, and 27 source chain.

An ignored-file-inclusive prior-report search covered `reports/yaml_record_review` for `bacillus_tusciae_medium_add_agar`, `Bacillus Tusciae Medium (add agar)`, `CultureMech:008976`, `TOGO Medium M2393`, and `TOGO:M2393`; it found no prior report for this generated record.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The pH 4.0 and gas-incubation overlay from DSMZ Medium 369 is missing. | DSMZ Medium 369 defines Bacillus Tusciae Medium by adjusting Medium 261 to pH 4.0 and incubating at 50 C under 5% O2 / 10% CO2 / 45% H2 without agitation. The M2393 record has neither pH nor preparation steps. | `data/normalized_yaml/bacterial/bacillus_tusciae_medium_add_agar.yaml`; the TOGO DSMZ-reference importer |
| Major | SL-6 is represented both as a malformed solution and as top-level stock salts. | TOGO M2393 adds 3 ml `Trace element solution SL-6`; the normalized record has `3 G_PER_L` for the solution and still carries six stock salts plus one variable molybdate stock row as top-level ingredients. | `data/normalized_yaml/bacterial/bacillus_tusciae_medium_add_agar.yaml`; TOGO stock-solution migration |
| Major | `Na2MoO4 x 2 H2O` has a fabricated variable amount. | TOGO M2393 omitted the numeric value for this SL-6 row, but DSMZ Medium 27 lists it as 0.03 g/L stock. | `data/normalized_yaml/bacterial/bacillus_tusciae_medium_add_agar.yaml`; TOGO referenced-stock expansion |
| Major | Ferric ammonium citrate is 1000-fold too high. | TOGO imports ferric ammonium citrate as 5 mg in the basal recipe; the normalized and generated row is `5 G_PER_L` instead of 0.005 g/L. | `data/normalized_yaml/bacterial/bacillus_tusciae_medium_add_agar.yaml`; TOGO mg-to-g conversion |
| Major | Main water has the wrong unit and stale generated value. | TOGO lists 1000 ml distilled water. The normalized row is `1000 G_PER_L`; the generated row has `2000.0 G_PER_L`, showing it predates the September 2026 duplicate-merge repair. | `data/normalized_yaml/bacterial/bacillus_tusciae_medium_add_agar.yaml`; merge regeneration |
| Major | Two hydrated salts have inconsistent or overly broad MIM links. | `MgSO4 x 7 H2O` has primary `CHEBI:31795` but `mediaingredientmech_chebi_term: CHEBI:32599`; `NiCl2 x 6 H2O` is mapped to anhydrous nickel dichloride. | `data/normalized_yaml/bacterial/bacillus_tusciae_medium_add_agar.yaml`; the MIM label-index rule for `NiCl2 x 6 H2O` |

## Recommended Edits

1. Add `ph_value: 4.0` and preparation steps for the DSMZ Medium 369 pH adjustment and 50 C, 5% O2 / 10% CO2 / 45% H2, no-agitation incubation.
2. Convert main water to a volume unit, keeping 1000 ml/L, and preserve only one main water row.
3. Convert ferric ammonium citrate from 5 mg/L to 0.005 g/L.
4. Replace the top-level SL-6 trace-salt rows with a correctly typed `solutions` entry for `Trace element solution SL-6` at 3 ml/L; include `Na2MoO4 x 2 H2O` at 0.03 g/L inside the SL-6 stock composition.
5. Preserve the 15 g/L agar addition on this M2393 add-agar variant.
6. Fix `MgSO4 x 7 H2O` so both term slots use `CHEBI:31795`.
7. Re-ground `NiCl2 x 6 H2O` to a hydrate-specific term or leave it unresolved.
8. Regenerate `data/merge_yaml/merged/`.

## Follow-up Checks

- Run `just validate data/normalized_yaml/bacterial/bacillus_tusciae_medium_add_agar.yaml`.
- Run `just verify-merges` and `just audit-merge-freshness` after regeneration.
- Re-run the no-project open-schema, strict, reference, and term validators against `data/merge_yaml/merged/bacillus_tusciae_medium_add_agar.yaml`.
- Recompare the regenerated output with TOGO M2393, DSMZ Medium 369, DSMZ Medium 261, DSMZ Medium 260, and DSMZ Medium 27.
- Check that `Na2MoO4 x 2 H2O` is no longer `VARIABLE`, that SL-6 is not duplicated at the top level, and that the regenerated water row is no longer `2000.0 G_PER_L`.

## Additional Notes

This M2393 record should remain distinct from the liquid TOGO M2392 source because its source explicitly adds 15 g agar. It should nevertheless share the same pH 4.0 and Bacillus tusciae incubation overlay as M2392 after repair.
