# YAML Record Review: atalassotoga_azc2201_medium__2c8a8ada

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/atalassotoga_azc2201_medium__2c8a8ada.yaml
- Started UTC: 2026-09-21T16:26:27Z
- Finished UTC: 2026-09-21T16:28:24Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/atalassotoga_azc2201_medium__2c8a8ada.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:002355` |
| Label | `atalassotoga_azc2201_medium` |
| Original label | `ATALASSOTOGA AZC2201 MEDIUM` |
| Category | `bacterial` |
| Source identity | JCM `J1184`; `mediadive.medium:J1184` |
| Source URL | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1184` |
| Generated status | Generated on 2026-08-06 from `data/normalized_yaml/bacterial/atalassotoga_azc2201_medium.yaml` |
| Merge fingerprint | `2c8a8ada2d946d0caed8e5b78b7d588117d93beac667a20e7fbfacc534941fa1` |

`data/merge_yaml/merged/` is derived output. Future fixes belong in
`data/normalized_yaml/bacterial/atalassotoga_azc2201_medium.yaml`, the
JCM/MediaDive importer, or merge rules that reconcile this record with the Togo
M1269 copy; then this generated file should be regenerated.

## Validation

| Check | Command | Result |
|---|---|---|
| Open schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/atalassotoga_azc2201_medium__2c8a8ada.yaml` | Pass. |
| Strict schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/atalassotoga_azc2201_medium__2c8a8ada.yaml --out /private/tmp/atalassotoga_azc2201_medium__2c8a8ada.strict.tsv --workers 1 --quiet` | Pass; 1 file scanned, 0 error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/atalassotoga_azc2201_medium__2c8a8ada.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 1 file validated, 0 checks. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/atalassotoga_azc2201_medium__2c8a8ada.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass. The only emitted message was the known `eutils`/`pkg_resources` deprecation warning. |
| Embedded curation history | Not checked | No focused validator for embedded `MediaRecipe.curation_history` is documented for one merged recipe. `just validate-history` targets standalone records under `history/`. |

Direct `just` validation was not used because this checkout currently reaches a
project `uv` build of `llvmlite==0.46.0` under Python 3.13 before target-specific
validation and fails in `setuptools` with `TypeError: Popen.__init__() got an
unexpected keyword argument 'dry_run'`.

## Identity and Grounding

- The generated ID, label, and source notes identify the JCM GRMD 1184 record
  for `ATALASSOTOGA AZC2201 MEDIUM`.
- The cited JCM page currently returns "Nothing found" for `GRMD=1184`, so this
  review used the Togo M1269 API as an inspected secondary copy of JCM M1184.
  Togo M1269 states `original_media_id: JCM_M1184` and names the same
  Atalassotoga AZC2201 medium.
- The Togo M1269 owner is generated separately as
  `data/merge_yaml/merged/ATALASSOTOGA_AZC2201_MEDIUM.yaml`; these two records
  represent the same JCM source but diverge in stock-boundary handling.
- The direct base salts and pH 4 preparation are recognizable, but most
  post-autoclave solutions are flattened into unsupported direct final
  ingredients.

## Evidence

| Claim in generated record | Review |
|---|---|
| NaCl, MgCl2.6H2O, MgSO4.7H2O, KCl, `(NH4)2SO4`, K2HPO4, KH2PO4, CaCl2.2H2O, L-Cysteine HCl.H2O, and Resazurin as pre-autoclave components | Broadly supported by the Togo copy of JCM M1184, although the JCM import appears to normalize g/L values downward rather than preserving the per-litre source amounts. |
| Yeast extract at 10 g/L | Wrong boundary. The source adds 10 ml/L of a 1% Yeast extract solution after cooling. |
| Fructose at 20 g/L | Wrong boundary. The source adds 20 ml/L of a 1 M Fructose solution after cooling. |
| Na2S2O3 at 10 g/L | Wrong boundary. The source adds 10 ml/L of a 1 M Na2S2O3 solution after cooling. |
| HCl, FeCl2.4H2O, ZnCl2, MnCl2.4H2O, H3BO3, CoCl2.6H2O, CuCl2.2H2O, NiCl2.6H2O, Na2MoO4.2H2O, FeSO4.7H2O, NiSO4.7H2O, Na2WO4.2H2O, and Na2SeO3.5H2O as direct ingredients | Not supported as direct Atalassotoga ingredients. The source adds FeCl2 solution, Trace element solution, and Fe-Ni-WO-Se solution as 1 ml/L referenced stocks. |
| Vitamin solution at 1 `G_PER_L` | Wrong unit. The source adds 1 ml/L Vitamin solution after cooling. |
| One top-level autoclave preparation step | Supported but incomplete: it retains the pH 4, nitrogen, anaerobic dispensing, autoclaving, and post-cooling addition text, but the supplement rows are not scoped as those post-cooling additions. |

## Completeness

- An ignored-file-inclusive exact search for `CultureMech:002355`,
  `mediadive.medium:J1184`, `JCM_M1184`, `JCM, ID: J1184`,
  `atalassotoga_azc2201_medium__2c8a8ada`, and `GRMD=1184` across `data`,
  `reports`, `history`, and `.claude` found this JCM owner, the Togo M1269
  copy, generated records, import QC reports, and archived validation rows.
- `find data/normalized_yaml -name '*AZC2201*' -o -name '*azc2201*' -print`
  found `data/normalized_yaml/bacterial/atalassotoga_azc2201_medium.yaml` for
  this generated target. This search covered ignored files.
- `find reports/yaml_record_review -maxdepth 1 -name
  '*atalassotoga_azc2201_medium__2c8a8ada.md'` searched the ignored report
  directory and found no prior review for this exact generated record stem
  before this report was written.
- The record is missing explicit FeCl2, trace-element, Fe-Ni-WO-Se,
  1% yeast-extract, 1 M fructose, 1 M Na2S2O3, and vitamin post-autoclave
  solution boundaries.

## Findings

| Severity | Finding | Evidence | Future owner |
|---|---|---|---|
| major | Three defined organic/inorganic post-autoclave solutions are flattened as final g/L ingredients. | Togo's copy of JCM M1184 adds 10 ml/L 1% Yeast extract solution, 20 ml/L 1 M Fructose solution, and 10 ml/L 1 M Na2S2O3 solution; the generated record lists the solutes directly at 10, 20, and 10 g/L. | `data/normalized_yaml/bacterial/atalassotoga_azc2201_medium.yaml` or the JCM/MediaDive importer. |
| major | The FeCl2, trace-element, and Fe-Ni-WO-Se referenced stocks are flattened at stock strength. | The source adds those three solutions at 1 ml/L; the generated record exposes their stock salts, including FeCl2 at 1.5 g/L, FeSO4 at 1.42 g/L, and NiSO4 at 1.6 g/L, as direct ingredients. | Same maintained JCM owner or importer. |
| major | Vitamin solution keeps a stock boundary but uses the wrong unit. | The source adds 1 ml/L Vitamin solution; the generated record says `1 G_PER_L`. | Same maintained JCM owner or importer. |
| major | The JCM and Togo copies of the same M1184 source remain split and disagree. | The Togo copy retains seven source solution rows, while this JCM copy flattens most of them; both cite JCM GRMD 1184. | Merge/deduplication rules plus both maintained owners. |

## Recommended Edits

1. Re-model the JCM owner with explicit post-autoclave solution additions for
   FeCl2 solution, Trace element solution, Fe-Ni-WO-Se solution, 1% Yeast
   extract solution, 1 M Fructose solution, 1 M Na2S2O3 solution, and Vitamin
   solution.
2. Convert the Vitamin solution amount from `1 G_PER_L` to `1 ML_PER_L`.
3. Remove stock-strength trace-metal salts from the direct Atalassotoga
   ingredient list unless the record intentionally materializes final
   concentrations from the referenced stock definitions.
4. Decide whether the direct JCM and Togo M1269 owners should be merged or
   linked as source duplicates before regenerating both generated records.

## Follow-up Checks

- Rerun open-schema, strict, term, and reference validation on the maintained
  JCM Atalassotoga owner after correction.
- Rerun the concentration plausibility audit and confirm it no longer flags
  FeCl2, FeSO4, or NiSO4 as stock-strength direct trace salts.
- Confirm the regenerated merge has seven post-autoclave solution additions and
  no direct `Fe--Ni--WO--Se` stock salts.
- Re-run duplicate-stem review for the Togo and direct JCM Atalassotoga owners
  after curation.

## Additional Notes

- Direct JCM primary-source verification is currently unresolved because the
  cited JCM GRMD 1184 URL returned a "Nothing found" page. Togo M1269 preserves
  a copy of the same original JCM medium and was used for claim-level checks.
