# YAML Record Review: 10_mixotrophic_nitrobacter_medium

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/10_mixotrophic_nitrobacter_medium.yaml`
- Started UTC: 20260921T042700Z
- Finished UTC: 20260921T042843Z
- Verdict: needs curation

## Target

| Field | Observed value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:008935` |
| Label | `10_mixotrophic_nitrobacter_medium` |
| Category | `bacterial` |
| Generated or maintained | Generated merge artifact under `data/merge_yaml/merged/`; future edits belong in `data/normalized_yaml/bacterial/TOGO_M2350_10_Mixotrophic_Nitrobacter_Medium.yaml` or the TOGO/stock-solution import path |
| Merge owner | `merged_from: [TOGO_M2350_10_Mixotrophic_Nitrobacter_Medium]` |
| Maintained owner | `data/normalized_yaml/bacterial/TOGO_M2350_10_Mixotrophic_Nitrobacter_Medium.yaml` |

This TOGO M2350 record wraps DSMZ/MediaDive Medium 756b, `10% MIXOTROPHIC NITROBACTER MEDIUM`. The generated merge is fresh relative to the maintained TOGO input, but the maintained input itself has carried stock-solution migration errors since March.

## Validation

Repository `just` entrypoints were blocked before target-specific validation because the project `uv` environment attempts to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools with `TypeError: Popen.__init__() got an unexpected keyword argument 'dry_run'`.

| Check | Command | Result |
|---|---|---|
| Open LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/10_mixotrophic_nitrobacter_medium.yaml` | Pass; `No issues found` |
| Closed schema / strict | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/10_mixotrophic_nitrobacter_medium.yaml --out /private/tmp/culturemech-review-10-mixotrophic-nitrobacter.strict.tsv --workers 1 --quiet` | Pass; 1 file scanned, 0 files with `ERROR`, TSV at `/private/tmp/culturemech-review-10-mixotrophic-nitrobacter.strict.tsv` |
| References | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/10_mixotrophic_nitrobacter_medium.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Pass; 1 file validated, 0 reference checks |
| Terms | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/10_mixotrophic_nitrobacter_medium.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Pass |
| Embedded curation history | Not checked | No focused embedded `MediaRecipe.curation_history` validator is documented for one merge record; `just validate-history` targets standalone files under `history/` |

The validators do not detect stock/final-medium flattening, wrong stock identifiers, or milligram-to-gram inflation.

## Identity and Grounding

- TOGO M2350 resolves to `10% Mixotrophic Nitrobacter Medium` and cites the DSMZ Medium 756b PDF.
- MediaDive `756b` resolves to `10% MIXOTROPHIC NITROBACTER MEDIUM` with pH 8.6.
- The `TOGO:M2350` source identity on the generated record is therefore correct.

The two solution identities are wrong:

- MediaDive Medium 756b embeds `Trace element solution` as local solution `1545` and `Stock solution` as local solution `1544`.
- The generated record instead points both additions at unrelated global normalized solution records: `mediadive.solution:6187` and `mediadive.solution:6127`.
- `data/normalized_yaml/bacterial/mediadive_6187_Trace_element_solution.yaml` is an EDTA/chloride trace solution and `data/normalized_yaml/bacterial/mediadive_6127_Stock_solution.yaml` is a nitrate/phosphate stock; neither matches the MediaDive 756b embedded trace solution or stock solution.

## Evidence

Supported by inspected source text:

- The main MediaDive 756b solution contains 0.15 g yeast extract, 0.15 g peptone, 0.055 g Na-pyruvate, 1 ml trace-element solution, 100 ml stock solution, 2 g NaNO2, and 899 ml distilled water per liter.
- The MediaDive 756b trace-element stock contains 33.8 mg MnSO4 x H2O, 49.4 mg H3BO3, 43.1 mg ZnSO4 x 7 H2O, 37.1 mg (NH4)6Mo7O24, 97.3 mg FeSO4 x 7 H2O, 25 mg CuSO4 x 5 H2O, and 1000 ml distilled water per liter of stock.
- The MediaDive 756b stock solution contains 0.07 g CaCO3, 5 g NaCl, 0.5 g MgSO4 x 7 H2O, 1.5 g KH2PO4, and 1000 ml distilled water per liter of stock.
- MediaDive says to adjust the final pH to 8.6 with NaOH or KOH.

Unsupported or internally inconsistent:

- The generated record promotes all trace-element-stock salts into top-level ingredients and stores their milligram stock quantities as grams per liter, e.g. `H3BO3` 49.4 g/L instead of 49.4 mg/L within the trace stock or 49.4 micrograms/L in final medium at 1 ml/L.
- The generated record promotes the 100 ml/L stock-solution ingredients into top-level ingredients at undiluted stock concentration: 5 g/L NaCl, 1.5 g/L KH2PO4, 0.5 g/L MgSO4 x 7 H2O, and 0.07 g/L CaCO3.
- `Distilled water` is `2899.0 G_PER_L`, apparently summing the 899 ml final-medium water, 1000 ml trace-stock water, and 1000 ml stock-solution water across three separate preparation contexts.
- The generated `solutions` entries use placeholder `name: Unknown solution`, encode 1 ml and 100 ml additions as `G_PER_L`, and point to the wrong external solution records.
- The pH 8.6 adjustment with NaOH or KOH is absent.

## Completeness

- The record is not complete enough for stock-aware downstream use because neither the two embedded stocks nor their final-medium addition volumes are represented with the right identity and unit.
- A gitignore-independent `rg --no-ignore --hidden` search over `data/merge_yaml/merged` and `data/normalized_yaml` for `10_mixotrophic_nitrobacter_medium`, the 10% Mixotrophic Nitrobacter label, `mediadive.medium:756`, and KOMODO 756 variants found separate DSMZ/TOGO/KOMODO records for the 756-family heterotrophic, mixotrophic, 10% mixotrophic, autotrophic, and Nitrospira media. Those are adjacent variants, not substitutes for TOGO M2350/MediaDive 756b.
- Exact gitignore-independent search for `mediadive.solution:6187` and `mediadive.solution:6127` found many records that reference those generic global solutions, including this one, but the inspected solution records do not match MediaDive 756b's local embedded solutions 1545 and 1544.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Blocker | The two solution references point to the wrong stock recipes. | MediaDive 756b uses local embedded solution IDs 1545 and 1544 with sulfate/carbonate/nitrite-family recipes; `mediadive.solution:6187` is an EDTA/chloride trace solution and `mediadive.solution:6127` is a nitrate/phosphate stock. | `data/normalized_yaml/bacterial/TOGO_M2350_10_Mixotrophic_Nitrobacter_Medium.yaml` plus stock-solution generation rules. |
| Major | Trace-element stock members are flattened into the final medium and inflated from mg to g. | MediaDive 756b lists 25-97.3 mg quantities per liter of trace stock and adds that stock at 1 ml/L; the generated top-level rows record 25-97.3 g/L final-medium concentrations. | TOGO stock-solution importer / `solution-migrator-v1.0`. |
| Major | The stock solution added at 100 ml/L is flattened at full stock strength. | MediaDive 756b adds 100 ml/L of a stock containing 0.07 g CaCO3, 5 g NaCl, 0.5 g MgSO4 x 7 H2O, and 1.5 g KH2PO4 per liter; the generated top-level rows keep those undiluted per-liter stock amounts. | TOGO stock-solution importer / `solution-migrator-v1.0`. |
| Major | Distilled-water quantities from three contexts are merged into one impossible mass concentration. | The source has 899 ml water in the final medium plus 1000 ml in each stock recipe; the generated record has `2899.0 G_PER_L`. | TOGO solution-boundary migration and duplicate-water merge cleanup. |
| Major | The final pH instruction is missing. | MediaDive 756b states pH 8.6 and says to adjust with NaOH or KOH; the generated record has no `ph_value` or preparation step. | `data/normalized_yaml/bacterial/TOGO_M2350_10_Mixotrophic_Nitrobacter_Medium.yaml`. |
| Minor | `high_metal: true` is likely an artifact of the inflated trace stock. | The apparent high metal burden is created by gram-level top-level trace rows that should remain mg/L stock components or microgram/L final-medium contributions. | Recompute quality flags after fixing stock nesting. |

## Recommended Edits

1. Remove the `mediadive.solution:6187` and `mediadive.solution:6127` links from the TOGO M2350 record; they are unrelated stock recipes.
2. Represent the MediaDive 756b `Trace element solution` and `Stock solution` as source-local nested stock recipes, or create distinct maintained `SolutionRecipe` records for solution IDs 1545 and 1544 and reference those at 1 ml/L and 100 ml/L.
3. Move stock-internal H3BO3, FeSO4 x 7 H2O, ZnSO4 x 7 H2O, CuSO4 x 5 H2O, MnSO4 x H2O, (NH4)6Mo7O24, CaCO3, NaCl, MgSO4 x 7 H2O, and KH2PO4 out of final top-level ingredients.
4. Preserve the main solution exactly: yeast extract 0.15 g/L, peptone 0.15 g/L, Na-pyruvate 0.055 g/L, NaNO2 2 g/L, 899 ml distilled water, plus the two stock additions.
5. Add the final pH 8.6 NaOH/KOH adjustment and recompute any `high_metal` or derived quality flags after regeneration.

## Follow-up Checks

- `just validate-strict data/normalized_yaml/bacterial/TOGO_M2350_10_Mixotrophic_Nitrobacter_Medium.yaml` after the maintained TOGO record is repaired.
- `just validate-terms` on any new or corrected MediaDive-756b-local `SolutionRecipe` records.
- `just verify-merges` after regenerating `data/merge_yaml/merged/10_mixotrophic_nitrobacter_medium.yaml`.
- Manual comparison with MediaDive 756b and TOGO M2350 to verify the final medium has 1 ml/L trace-element stock, 100 ml/L stock solution, 899 ml water, and pH 8.6.

## Additional Notes

- `linkml-reference-validator` performed zero checks because this generated record has no `references` block.
