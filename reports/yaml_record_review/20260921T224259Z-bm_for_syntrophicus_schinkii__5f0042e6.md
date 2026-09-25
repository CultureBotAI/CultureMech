# YAML Record Review: bm_for_syntrophicus_schinkii

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/bm_for_syntrophicus_schinkii__5f0042e6.yaml`
- Started UTC: 2026-09-21T22:43:00Z
- Finished UTC: 2026-09-21T22:43:40Z
- Verdict: needs curation

## Target

| Field | Value |
| --- | --- |
| Class | `MediaRecipe` |
| Generated record ID | `CultureMech:003080` |
| Generated label | `bm_for_syntrophicus_schinkii` |
| Original name | `BM FOR SYNTROPHICUS SCHINKII` |
| Source term | `mediadive.medium:J737` / `BM FOR SYNTROPHICUS SCHINKII` |
| Maintained owner | `data/normalized_yaml/bacterial/bm_for_syntrophicus_schinkii.yaml` |
| Related solution | `data/normalized_yaml/bacterial/mediadive_4668_Main_sol_J737.yaml` |
| Generated status | Derived from one active normalized JCM input by `merge_recipes.py`; future fixes belong in normalized YAML or JCM import/solution-migration rules, followed by merge regeneration |

The ignored-file-inclusive exact search for `CultureMech:003080`,
`mediadive.medium:J737`, and `J737` found one active normalized
`MediaRecipe`, one related normalized `Main sol. J737` `SolutionRecipe`, plus
generated normalized-index and merged-record copies. It did not find a duplicate
maintained `MediaRecipe` owner for `CultureMech:003080` or
`mediadive.medium:J737`.

## Validation

| Check | Command | Result |
| --- | --- | --- |
| Open-schema LinkML | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/bm_for_syntrophicus_schinkii__5f0042e6.yaml` | Passed, `No issues found` |
| Strict closed-schema validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/bm_for_syntrophicus_schinkii__5f0042e6.yaml --out /private/tmp/bm_for_syntrophicus_schinkii__5f0042e6.strict.tsv --workers 1 --quiet` | Passed, 1 file scanned, 0 error rows |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/bm_for_syntrophicus_schinkii__5f0042e6.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed, 0 checks, all validations passed |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/bm_for_syntrophicus_schinkii__5f0042e6.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils`/`pkg_resources` warning |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merged record; `just validate-history` targets standalone files under `history/` |

The documented `just validate-schema`, `just validate-strict`, and
`just validate-terms` entrypoints were not used directly because this checkout's
project `uv` environment currently tries to build `llvmlite==0.46.0` under
Python 3.13 and fails inside `setuptools` before a target-specific check runs.
The no-project Python 3.11 commands above exercise the same target validators.

## Identity and Grounding

- The intended JCM identity matches TOGO M762's original source: both refer to
  JCM medium 737, `BM For Syntrophicus Schinkii`.
- The current JCM `GRMD=737` URL returned a `Nothing found` page; TOGO M762 was
  used as the inspected grouped copy of the same JCM recipe.
- The record preserves pH-free, liquid BM identity, but it flattens all stock
  solutions into one direct final-medium ingredient list and omits final-medium
  water.

## Evidence

Inspected sources:

| Source | Scope checked |
| --- | --- |
| `/private/tmp/jcm-737.html` | Original JCM URL; checked and returned `Nothing found` |
| `/private/tmp/togo-M762.json` | TOGO copy of JCM M737 grouped components, gas phase, post-autoclave solution additions, phosphate-solution composition, and preparation comment |
| `data/normalized_yaml/bacterial/mediadive_4668_Main_sol_J737.yaml` | Related direct-JCM solution state |

Supported:

- TOGO supports the main-solution salts, yeast extract, magnesium chloride,
  calcium chloride, ammonium chloride, sodium chloride, 830 ml water, 0.5 mg
  resazurin, and the `N2--CO2 (80:20, v/v)` preparation gas mixture.
- TOGO supports post-cooling additions of 8% NaHCO3 solution, 0.1 M L-sodium
  lactate solution, 5% Na2S.9H2O solution, phosphate solution, trace vitamins,
  trace metal solution, and selenite-tungstate solution.
- TOGO supports a phosphate stock containing water, KH2PO4, and Na2HPO4; the
  repaired Tepidanaerobacter records show that stock should be represented as a
  source-specific solution rather than flattened into downstream final media.

Unsupported or over-scoped:

- Final-medium water is missing.
- Trace vitamins are represented as `1 G_PER_L`, even though TOGO gives a 1 ml
  trace-vitamin stock addition.
- NaHCO3, L-sodium lactate, and Na2S.9H2O are represented as direct `G_PER_L`
  rows with the source stock-addition volumes as gram values.
- KH2PO4 and Na2HPO4 are represented as direct 4.1 g/L and 4.3 g/L rows rather
  than as the composition of a 25 ml phosphate-solution addition.
- HCl, FeCl2.4H2O, CoCl2.6H2O, MnCl2.4H2O, ZnCl2, H3BO3, Na2MoO4.2H2O,
  NiCl2.6H2O, CuCl2.2H2O, AlCl3, Na2WO4.2H2O, NaOH, and Na2SeO3.5H2O are
  cross-referenced stock constituents, not direct final-medium ingredients.
- The related `mediadive_4668_Main_sol_J737.yaml` solution rescales the source
  recipe to a 1003 ml final volume, turns milliliter stock additions into
  `PERCENT_V_V`, and still carries a `See source for composition` placeholder.

## Completeness

- Consequentially incomplete: no stock solution references remain in the
  maintained direct-JCM medium even though the source is built from multiple
  post-autoclave stocks.
- Consequentially incomplete: the trace metal, selenite-tungstate, trace
  vitamin, lactate, bicarbonate, sulfide, and phosphate stock boundaries are
  all lost.
- Consequentially incomplete: direct final-medium water is missing.
- Empty organism-growth slots are acceptable; TOGO M762 is a recipe page and
  does not assert a growth experiment.
- Bounded search: ignored files were included in the exact J737 search
  described under `Target`, and no duplicate maintained J737 `MediaRecipe`
  owner was found.

## Findings

| Severity | Finding | Evidence | Maintained owner |
| --- | --- | --- | --- |
| major | Every source stock addition has been flattened into direct ingredients, including phosphate, trace-vitamin, trace-metal, selenite-tungstate, bicarbonate, lactate, and sulfide stocks. | TOGO M762 API JSON. | `data/normalized_yaml/bacterial/bm_for_syntrophicus_schinkii.yaml`; related repair may be needed in `data/normalized_yaml/bacterial/mediadive_4668_Main_sol_J737.yaml` |
| major | Stock addition volumes are stored as gram-per-liter final ingredients, e.g. `Trace vitamins` at `1 G_PER_L`, `NaHCO3` at `40 G_PER_L`, `L-Sodium lactate` at `100 G_PER_L`, and `Na2S x 9 H2O` at `5 G_PER_L`. | TOGO M762 API JSON. | `data/normalized_yaml/bacterial/bm_for_syntrophicus_schinkii.yaml` |
| major | The final-medium water row is missing despite TOGO M762 listing 830 ml in the main solution. | TOGO M762 API JSON. | `data/normalized_yaml/bacterial/bm_for_syntrophicus_schinkii.yaml` |
| major | The related `Main sol. J737` solution is itself malformed, with 1003 ml rescaling, `PERCENT_V_V` stock rows, and an `incomplete_composition` placeholder. | `data/normalized_yaml/bacterial/mediadive_4668_Main_sol_J737.yaml`. | `data/normalized_yaml/bacterial/mediadive_4668_Main_sol_J737.yaml` |

## Recommended Edits

1. Rebuild `data/normalized_yaml/bacterial/bm_for_syntrophicus_schinkii.yaml`
   from the grouped TOGO M762 recipe: restore 830 ml water, keep the direct main
   salts in the main final-medium list, and model all post-autoclave additions
   as stock-solution references.
2. Replace direct `G_PER_L` rows for NaHCO3, L-sodium lactate, Na2S.9H2O,
   KH2PO4, Na2HPO4, trace vitamins, and all trace metal and
   selenite-tungstate constituents with source-faithful stock references.
3. Populate a phosphate stock from M762 or reuse the curated equivalent already
   present in the repaired Tepidanaerobacter records.
4. Fetch and wire the trace metal, selenite-tungstate, and trace vitamin source
   stocks instead of preserving flattened direct rows.
5. Repair or retire `data/normalized_yaml/bacterial/mediadive_4668_Main_sol_J737.yaml`
   so no future curation points at a 1003 ml, `PERCENT_V_V` placeholder
   solution.
6. Regenerate merge outputs so
   `data/merge_yaml/merged/bm_for_syntrophicus_schinkii__5f0042e6.yaml`
   reflects the normalized repair.

## Follow-up Checks

- Fetch and inspect TOGO M288, M431, and M190 before filling the
  cross-referenced stock compositions.
- Run focused schema, strict, term, and reference validators on
  `data/normalized_yaml/bacterial/bm_for_syntrophicus_schinkii.yaml` and any
  repaired J737 `SolutionRecipe`.
- Run the same validators on
  `data/merge_yaml/merged/bm_for_syntrophicus_schinkii__5f0042e6.yaml` after
  merge regeneration.
- Run `just verify-merges` and `just audit-merge-freshness` after regenerating
  merge outputs.
- Re-fetch TOGO M762 and manually verify direct ingredients, stock-solution
  references, gas-phase preparation scoping, and the absence of flattened trace
  metal or selenite-tungstate components.

## Additional Notes

- `find reports/yaml_record_review -name '*bm_for_syntrophicus_schinkii__5f0042e6.md'`
  returned no path before this report was created.
- This review intentionally wrote only this Markdown report. The generated
  merge record and normalized owner YAML were left unchanged.
