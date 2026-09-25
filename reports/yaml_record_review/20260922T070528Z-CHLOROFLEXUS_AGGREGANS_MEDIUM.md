# YAML Record Review: CHLOROFLEXUS AGGREGANS medium

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml
- Started UTC: 2026-09-22T07:03:00Z
- Finished UTC: 2026-09-22T07:05:29Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Path | `data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml` |
| Class | `MediaRecipe` |
| ID | `CultureMech:006721` |
| Name | `chloroflexus_aggregans_medium` |
| Original name | `CHLOROFLEXUS AGGREGANS medium` |
| Media term | `komodo.medium:87a` / `CHLOROFLEXUS AGGREGANS medium` |
| Source | KOMODO `87a`, mapped in the record to DSMZ / MediaDive Medium 87a |
| Generated status | Derived merge generated from four normalized KOMODO/DSMZ Medium 87 and 87a records |

The reviewed record is generated from these maintained owners:
`data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml`,
`data/normalized_yaml/bacterial/KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml`,
`data/normalized_yaml/bacterial/chloroflexus_aggregans_medium.yaml`, and
`data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml`.
Future repairs belong in those inputs or in merge emission, not in this merged
YAML copy.

## Validation

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml` | Passed with no issues reported. |
| Strict closed-schema validation | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml --out /private/tmp/CHLOROFLEXUS_AGGREGANS_MEDIUM.strict.tsv --workers 1 --quiet` | Passed: 1 file scanned, 0 files with `ERROR`, 0 total `ERROR` rows. |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 1 file validated with 0 reference checks. |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the validator emitted the known `eutils` / `pkg_resources` deprecation warning. |
| Embedded history | `just validate-history` | Not checked: that recipe validates standalone `history/*.yaml` records against `HistoryRecord`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

I used the offline `uv` validator invocations above instead of the `just`
validator wrappers because the local project lock currently tries to build
`llvmlite==0.46.0` under Python 3.13 and fails inside setuptools before the
CultureMech validators run.

## Identity and Grounding

- The canonical fields consistently point to KOMODO `87a` / CHLOROFLEXUS
  AGGREGANS medium, and the record's notes map that KOMODO accession to DSMZ /
  MediaDive Medium 87a.
- DSMZ Medium 87a is a specific modification of DSMZ Medium 87: it adds
  `1.0 ml/litre` sterile Vitamin solution CA to Medium 87.
- The current `SOURCE_DUPLICATE` relationship to KOMODO/DSMZ Medium 87 is
  over-scoped. Medium 87 lacks Vitamin solution CA, while Medium 87a contains
  that stock; grouping `KOMODO_87_CHLOROFLEXUS_medium_modified.yaml` with 87a
  as an exact source duplicate hides a real formulation difference.
- The generated target is stale. It was merged on 2026-08-06 and has no
  `solutions` block, but three of the four normalized owners gained
  `NESTED_FLATTENED_COCKTAIL` curation events on 2026-08-07 or later for
  Vitamin solution CA.
- An ignored-independent `rg --no-ignore --hidden` search for the owner slugs,
  `CultureMech:006719`, `CultureMech:006721`, `komodo.medium:87a`, and merge
  fingerprint `20766fd1b6cf44f2d475e172feb74e49ef787ae1ba75e2e2d4e9cae2791788b9`
  across `data/normalized_yaml` and `data/merge_yaml/merged` found these four
  owners for the reviewed merge fingerprint. The same search also found
  unrelated TOGO Chloroflexus Aggregans records and separate merged records
  with the same normalized name; those are not members of this 87a merge group.

## Evidence

I inspected the DSMZ Medium 87a PDF, the DSMZ Medium 87 PDF, and MediaDive JSON
for media 87a and 87. The inspected sources support pH 8.2 and the main salts
that MediaDive reports for 87a: yeast extract `0.952381 g/L`, glycyl-glycine
`0.952381 g/L`, Na2HPO4 x 2 H2O `0.0952381 g/L`, MgSO4 x 7 H2O
`0.0952381 g/L`, KNO3 `0.0952381 g/L`, NaNO3 `0.47619 g/L`, NaCl
`0.0952381 g/L`, and CaCl2 x 2 H2O `0.047619 g/L`.

The same sources do not support several flattened rows in the generated target:

- DSMZ 87a adds Vitamin solution CA at `1 ml/litre`. Its component rows are
  stock concentrations, not final 87a concentrations. For example, MediaDive's
  final 87a composition reports Na3-EDTA `0.00190476 g/L`, nicotinic acid
  `0.000952381 g/L`, Biotin `0.000047619 g/L`, and Vitamin B12
  `0.00000952381 g/L`; the generated record lists the corresponding stock
  strengths as direct ingredients.
- Medium 87, inherited by 87a, adds Trace element solution SL-6 at `1 ml` into
  `1050 ml` water. The generated record lists the SL-6 stock strengths directly:
  H3BO3 `0.3 g/L`, ZnSO4 x 7 H2O `0.1 g/L`, CoCl2 x 6 H2O `0.2 g/L`, and the
  remaining trace salts all need a roughly 1/1050 dilution in the final 87a
  medium.
- The recipe adds `5 ml` of Fe(III) citrate solution prepared as `0.1 g in
  100 ml H2O`. The generated record stores `Fe(III) citrate` as `5 G_PER_L`,
  converting a stock volume into a gram-per-liter concentration.
- DSMZ Medium 87 uses neutralized sulfide solution as a separately prepared 3%
  stock and injects it after autoclaving. The generated record stores Na2S x 9
  H2O at `30 G_PER_L`, the 3% stock strength, as if sulfide were a direct final
  medium ingredient.
- All DSMZ 87/87a preparation steps are missing from the generated target. That
  loses the pH adjustment, nitrogen sparging, bottle fill, autoclaving, sterile
  sulfide injection, storage, 50 C / 300-500 lux incubation condition, yeast
  extract supplementation note, and Vitamin solution CA filtration step.

## Completeness

- The generated record is missing all solution topology. It should preserve at
  least Vitamin solution CA, Trace element solution SL-6, Fe(III) citrate
  solution, and neutralized sulfide solution rather than publishing their stock
  members as flat final-medium ingredients.
- `data/normalized_yaml/bacterial/medium_87a_modified_for_dsm_13941.yaml`
  correctly treats the `1 ml/l` Vitamin solution CA amount as a
  `CROSS_MEDIUM_INFERENCE` candidate because that variant's own recipe was not
  inspected. A future merge must not erase that uncertainty by promoting it to
  a source-supported assertion.
- Empty `target_organisms` and `growth_metrics` slots are not defects for this
  source-formulation review; the checked DSMZ pages define media formulations,
  not per-strain growth evidence.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | DSMZ/KOMODO Medium 87 is incorrectly treated as a `SOURCE_DUPLICATE` of DSMZ/KOMODO Medium 87a. | DSMZ 87a adds sterile Vitamin solution CA to medium 87. The generated merge folds `KOMODO_87_CHLOROFLEXUS_medium_modified` into the 87a canonical record and exports a `SOURCE_DUPLICATE` edge to it. | Remove the 87a vitamin stock from `data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml` or otherwise repair the 87-vs-87a mapping before regenerating. |
| major | The generated record is stale and lost Vitamin solution CA nesting that exists in maintained 87a owners. | The reviewed merge was written on 2026-08-06 and has no `solutions` block. `KOMODO_87a_CHLOROFLEXUS_AGGREGANS_medium.yaml`, `chloroflexus_aggregans_medium.yaml`, and `medium_87a_modified_for_dsm_13941.yaml` later moved five vitamin stock-strength components into `solutions`. | Fix merge emission to preserve normalized `solutions` blocks, then regenerate `data/merge_yaml/merged/`. |
| major | Fe(III) citrate, Trace element solution SL-6, and neutralized sulfide solution are flattened into unsupported direct concentrations. | DSMZ 87/87a add Fe(III) citrate as `5 ml` of a 0.1 g/100 ml stock, SL-6 as `1 ml` of a 1 L trace stock, and sulfide as a 3% separately neutralized stock injected after autoclaving. The generated record instead has `5 G_PER_L` Fe(III) citrate, SL-6 stock concentrations, and `30 G_PER_L` Na2S x 9 H2O as top-level ingredient rows. | Model those DSMZ stocks in all four normalized owners that inherit Medium 87, or fix the DSMZ resolver / KOMODO import path that expanded them as direct ingredients. |
| major | The generated merge drops all preparation and incubation context even though the DSMZ 87a owner has it. | DSMZ 87 requires pH 8.2, boiling under nitrogen, bottle distribution under nitrogen, autoclaving, post-autoclave neutralized sulfide injection, 50 C incubation at 300-500 lux, and stock-specific preparation for Vitamin solution CA. None of those steps are present in the reviewed generated target. | Change merge emission so source-duplicate groups retain source-supported `preparation_steps` from the selected canonical owner. |

## Recommended Edits

1. Repair `data/normalized_yaml/bacterial/KOMODO_87_CHLOROFLEXUS_medium_modified.yaml`
   so the DSMZ 87 record does not include Vitamin solution CA or declare itself
   an exact source duplicate of DSMZ/KOMODO 87a.
2. Add or retain stock-solution structure in every Medium 87/87a owner: Fe(III)
   citrate solution at 5 ml, Trace element solution SL-6 at 1 ml, neutralized
   sulfide solution injected after autoclaving, and Vitamin solution CA only
   where 87a actually applies it.
3. Preserve `medium_87a_modified_for_dsm_13941.yaml`'s Vitamin solution CA
   addition volume as a candidate until a curator inspects the 87a_13941 source
   directly.
4. Fix the merge writer so it emits normalized `solutions` and source-supported
   `preparation_steps` from the selected canonical recipe rather than choosing a
   flat ingredient list that predates later stock nesting.
5. Regenerate `data/merge_yaml/merged/` after the owner and merge-rule repairs.

## Follow-up Checks

- Run `just validate-strict` on the four normalized owners in this merge group.
- Run `just validate-media-variant-links` to prove the 87 and 87a
  parent/child links no longer assert an exact source duplicate where the
  vitamin stock makes the formulations different.
- Run `just merge-recipes` and `just verify-merges` to prove
  `data/merge_yaml/merged/CHLOROFLEXUS_AGGREGANS_MEDIUM.yaml` is regenerated
  from the fixed normalized inputs.
- Re-open the regenerated merged record and compare DSMZ 87/87a ingredient
  amounts, stock dilution boundaries, pH, nitrogen/autoclave/sulfide handling,
  and 50 C / 300-500 lux incubation context against the DSMZ PDFs.

## Additional Notes

- The record still carries `mediaingredientmech_term` on KNO3 and NaNO3 even
  though the 2026-06-05 history entry says legacy MediaIngredientMech links were
  refreshed to CHEBI-keyed links. That is a non-blocking provenance/grounding
  cleanup after the recipe topology is fixed.
- The ignored-independent search found TOGO Chloroflexus Aggregans records with
  the same normalized label outside this four-record merge. They should be
  reviewed separately at their own generated targets rather than folded into
  this DSMZ/KOMODO 87a judgement.
