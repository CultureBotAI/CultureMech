# YAML Record Review: Archaeoglobus Profundus Medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/archaeoglobus_profundus_medium__c5aebcda.yaml
- Started UTC: 2026-09-21T14:22:05Z
- Finished UTC: 2026-09-21T14:23:31Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Reviewed record | `data/merge_yaml/merged/archaeoglobus_profundus_medium__c5aebcda.yaml` |
| Authoritative owner | `data/normalized_yaml/archaea/TOGO_M207_Archaeoglobus_Profundus_Medium.yaml` |
| Class | `MediaRecipe` |
| Stable ID | `CultureMech:008669` |
| Name | `archaeoglobus_profundus_medium` |
| Original name | `Archaeoglobus Profundus Medium` |
| Category | `archaea` |
| Source | TOGO `M207`, original JCM medium `JCM_M214` |
| Generated state | Generated merge from one source recipe, fingerprint `c5aebcdaecda247c21085f3099b84b4c6a18a4688ac4e54d920450c983833a2e` |

The target is the generated canonical merge for a single TOGO/JCM source record. Future scientific fixes belong in `data/normalized_yaml/archaea/TOGO_M207_Archaeoglobus_Profundus_Medium.yaml`; the reviewed merge should be regenerated, not edited directly.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/archaeoglobus_profundus_medium__c5aebcda.yaml` | Passed: `No issues found`. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/archaeoglobus_profundus_medium__c5aebcda.yaml --out /private/tmp/archaeoglobus_profundus_medium__c5aebcda.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| Reference snippets | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/archaeoglobus_profundus_medium__c5aebcda.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed, but vacuously: 0 checks. |
| Ontology terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/archaeoglobus_profundus_medium__c5aebcda.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed. The only emitted warning was the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merge record; `just validate-history` targets standalone records under `history/`. |
| `just` validator entrypoints | Not run | The repository `uv` environment currently fails before target-specific validation under Python 3.13 while building `llvmlite==0.46.0`, so the same LinkML/reference/term tools were run via an offline Python 3.11 no-project environment. |

## Identity and Grounding

The stable ID and source identity agree: `CultureMech:008669` is registered to `data/normalized_yaml/archaea/TOGO_M207_Archaeoglobus_Profundus_Medium.yaml`, the generated record is merged from `TOGO_M207_Archaeoglobus_Profundus_Medium`, and the source notes identify TOGO `M207` / JCM `M214`.

The inspected TOGO payload and JCM page agree on the final-medium formula: KCl, MgCl2.6H2O, MgSO4.7H2O, NH4Cl, CaCl2.2H2O, K2HPO4, NaCl, NaHCO3, Na2SO4, Fe(NH4)2(SO4)2.6H2O, (NH4)2Ni(SO4)2.6H2O, 10 ml Trace minerals, yeast extract, sodium acetate, Resazurin, Na2S.9H2O, and 990 ml distilled water.

Ingredient grounding is mostly specific enough. The hydrated Mg, Ca, Fe, Ni, and Na2S salts are grounded to exact or exact-enough hydrate terms, and no wrong ontology identity was severe enough to block this record. The primary identity issues are units, stock-solution reference, and preparation scope rather than CHEBI labels.

## Evidence

Supported:

- The JCM page supports a 990 ml water row and a 10 ml `Trace minerals` addition to bring the final recipe to approximately one liter.
- The JCM page supports `Fe(NH4)2(SO4)2.6H2O`, `(NH4)2Ni(SO4)2.6H2O`, and Resazurin as milligram-scale final-medium ingredients.
- The JCM page supports pH 6.9, filtration under H2/CO2, separate neutralized Na2S.9H2O sterilization under N2, anaerobic addition of the sterile sulfide stock under H2/CO2, optional pH readjustment, and 200 kPa H2/CO2 pressurization after inoculation.
- The direct JCM/MediaDive normalized record, `data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml`, preserves the pH and preparation text that the TOGO projection drops.
- Existing import tracking already flags `Resazurin 1 G_PER_L` as an indicator unit slip on `CultureMech:008669`.

Unsupported or over-scoped:

- The JCM source links `Trace minerals` to Medium 151, while the TOGO payload and YAML point to Medium M142. The solution cross-reference is therefore unsupported by the original JCM source.
- The `Trace minerals` addition is represented as an empty `solutions` entry with `10 G_PER_L`; the source gives a 10 ml stock addition.
- Final Fe(NH4)2(SO4)2.6H2O, final (NH4)2Ni(SO4)2.6H2O, and final Resazurin are stored as `2 G_PER_L`, `2 G_PER_L`, and `1 G_PER_L` instead of milligram-equivalent concentrations.
- `Distilled water` is stored as `990 G_PER_L`, but the JCM source states `990 ml` as a preparation volume.
- JCM pH and preparation claims were converted into unscoped H2SO4, CO2, N2, and H2 variable ingredient rows rather than pH/preparation/atmosphere fields.

## Completeness

- The medium lacks a usable Trace minerals reference: `composition: []` plus `Cross-reference to Medium M142` does not let a reader reconstruct JCM Medium 214's intended stock.
- The record does not preserve pH 6.9 or the anaerobic filtration, separate sulfide sterilization, anaerobic sulfide addition, pH readjustment, and 200 kPa pressurization steps.
- The record has no growth evidence or target-organism blocks. That is acceptable for this imported database recipe because the inspected JCM formulation does not report a strain-level growth experiment beyond the recipe name.
- Empty optional slots such as target organisms, growth metrics, and storage conditions were not treated as defects where the inspected sources did not assert a value.
- An ignored-inclusive search across `data/normalized_yaml`, `data/merge_yaml`, the stable-ID registry, recipe catalog, media-content manifest, and import-tracking reports found the expected TOGO owner, generated merge, direct JCM/MediaDive sibling, and a Resazurin plausibility diagnostic. It found no TOGO-side normalized record that already resolves the Medium 151 Trace minerals cross-reference for `CultureMech:008669`.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| Major | Milligram-scale final ingredients are stored as grams per liter. | JCM M214 lists the two ammonium double salts at 2 mg each and Resazurin at 1 mg; the YAML stores numeric values `2`, `2`, and `1` with `unit: G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M207_Archaeoglobus_Profundus_Medium.yaml` |
| Major | The Trace minerals stock reference is wrong and empty. | The original JCM source links the 10 ml Trace minerals addition to Medium 151, while the TOGO record links an empty `solutions` entry to Medium M142 and encodes the 10 ml amount as `10 G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M207_Archaeoglobus_Profundus_Medium.yaml`; the TOGO importer should preserve JCM stock references without mapping JCM Medium 151 to TOGO M142. |
| Major | JCM preparation and pH were dropped. | JCM says pH 6.9 and gives filtration, gas, sulfide, pH readjustment, and pressure instructions. The TOGO owner has no `ph_value` or `preparation_steps`; it only keeps H2SO4, CO2, N2, and H2 as variable ingredients. | `data/normalized_yaml/archaea/TOGO_M207_Archaeoglobus_Profundus_Medium.yaml` |
| Major | The water volume is represented with the wrong dimension. | JCM specifies 990 ml distilled water, paired with 10 ml Trace minerals; the YAML stores `Distilled water 990 G_PER_L`. | `data/normalized_yaml/archaea/TOGO_M207_Archaeoglobus_Profundus_Medium.yaml` |

## Recommended Edits

1. Convert Fe(NH4)2(SO4)2.6H2O, (NH4)2Ni(SO4)2.6H2O, and Resazurin from source milligrams to supported final concentrations.
2. Replace the empty Medium M142 `Trace minerals` placeholder with a Medium 151-backed JCM Trace minerals solution or a correctly scoped unresolved cross-reference, and store its final addition as 10 ml rather than `10 G_PER_L`.
3. Represent 990 ml distilled water with a volume-aware unit or a preparation note rather than `G_PER_L`.
4. Restore `ph_value: 6.9` and JCM M214 preparation steps for H2SO4 adjustment, H2/CO2 filtration, neutralized Na2S.9H2O sterilization under N2, anaerobic sulfide addition, pH readjustment, and 200 kPa H2/CO2 pressurization.
5. Remove unscoped H2SO4, CO2, N2, and H2 variable ingredient placeholders once the same information is represented in proper pH, atmosphere, and preparation slots.
6. Regenerate `data/merge_yaml/merged/archaeoglobus_profundus_medium__c5aebcda.yaml` from the normalized owner.

## Follow-up Checks

- Run `just validate-schema data/normalized_yaml/archaea/TOGO_M207_Archaeoglobus_Profundus_Medium.yaml`.
- Run `just validate-strict data/normalized_yaml/archaea/TOGO_M207_Archaeoglobus_Profundus_Medium.yaml`.
- Run `just validate-terms data/normalized_yaml/archaea/TOGO_M207_Archaeoglobus_Profundus_Medium.yaml`.
- Run `just validate-references data/normalized_yaml/archaea/TOGO_M207_Archaeoglobus_Profundus_Medium.yaml` after adding any structured source references.
- Run `just validate-media-variant-links` if the fix turns the direct JCM/MediaDive import and TOGO import into explicit source duplicates.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating the derived merge.
- Manually compare the regenerated record against JCM `GRMD=214` and TOGO `gmdb_medium_by_gmid?gm_id=M207` to confirm that milligram ingredients, 990 ml water, Medium 151 Trace minerals, pH, and anaerobic preparation are preserved.

## Additional Notes

- The ignored-inclusive pre-report search under `reports/yaml_record_review` found no prior report for `archaeoglobus_profundus_medium__c5aebcda`, `CultureMech:008669`, or `TOGO_M207_Archaeoglobus_Profundus_Medium`.
- `data/normalized_yaml/archaea/JCM_J214_ARCHAEOGLOBUS_PROFUNDUS_MEDIUM.yaml` is a direct JCM/MediaDive import of the same JCM medium. It already corrects the three milligram rows and preserves preparation text, but it also has a flattened Trace minerals composition; the direct JCM record should not be copied blindly as a full fix for the TOGO projection.
