# YAML Record Review: METHANIMICROCOCCUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanimicrococcus_medium__85a9f573.yaml
- Started UTC: 2026-09-24T02:36:20Z
- Finished UTC: 2026-09-24T02:36:38Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | MediaRecipe |
| ID | CultureMech:002319 |
| Name | methanimicrococcus_medium |
| Original name | METHANIMICROCOCCUS MEDIUM |
| Category | archaea |
| Medium term | mediadive.medium:J1146, JCM Medium J1146 |
| Source | JCM via MediaDive |
| Source URL | https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1146 |
| Record status | Generated merge output |
| Maintained owner | data/normalized_yaml/archaea/methanimicrococcus_medium.yaml |
| Merge fingerprint | 85a9f5731df5075a185bea297da7dd408eb5886264b2f0699e5dfd7c3b634acf |

This generated record is a single-source merge from `data/normalized_yaml/archaea/methanimicrococcus_medium.yaml`.
Future fixes belong in that maintained MediaDive/JCM owner, the MediaDive import path that flattened staged stock additions, or source-alias rules that merge its TOGO M1228 duplicate, then in regenerated `data/merge_yaml/merged/` outputs.

## Validation

| Check | Command | Result |
|---|---|---|
| LinkML schema | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanimicrococcus_medium__85a9f573.yaml` | Passed with `No issues found`. |
| Strict validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml python scripts/validate_strict.py data/merge_yaml/merged/methanimicrococcus_medium__85a9f573.yaml --out /private/tmp/methanimicrococcus_medium__85a9f573.strict.tsv --workers 1 --quiet` | Passed; 1 file scanned, 0 files with errors, and 0 total error rows. |
| Reference validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-reference-validator linkml-reference-validator validate data data/merge_yaml/merged/methanimicrococcus_medium__85a9f573.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; 0 checkable references. |
| Term validator | `uv --cache-dir /private/tmp/uv-cache-culturemech-review --no-config run --no-project --offline --python /usr/local/bin/python3.11 --with pyyaml --with linkml --with linkml-term-validator linkml-term-validator validate-data data/merge_yaml/merged/methanimicrococcus_medium__85a9f573.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed; emitted only the known eutils/pkg_resources deprecation warning. |
| Embedded curation history | Not run | Not checked: the documented `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` lists in generated YAML. |

The normal `just` validator wrappers were not used because this uv environment tries to build `llvmlite==0.46.0` under Python 3.13 and fails in setuptools before any CultureMech validator can run.

## Identity and Grounding

The MediaDive/JCM identity is correct: MediaDive `J1146` and live JCM `GRMD=1146` both name `METHANIMICROCOCCUS MEDIUM`, and the medium is an archaeal complex liquid recipe with pH 7.1.

A gitignore-independent exact search over `data/normalized_yaml` and `data/merge_yaml/merged` found two maintained MediaRecipe owners for the same JCM 1146 source: this MediaDive owner at `data/normalized_yaml/archaea/methanimicrococcus_medium.yaml` and the TOGO owner at `data/normalized_yaml/archaea/TOGO_M1228_Methanimicrococcus_Medium.yaml`. No third exact MediaRecipe owner or generated medium was found in that bounded, ignored-file-inclusive search; the remaining J1146 hits were indexes and the MediaDive `Main sol. J1146` SolutionRecipe.

The individual ChEBI groundings are mostly plausible for their labels. The problem is that many terms are attached to stock rows that have been moved into the final medium.

## Evidence

JCM 1146 defines an initial 925 ml aqueous medium containing ammonium chloride, magnesium sulfate, calcium chloride, sodium chloride, ferrous sulfate, FeCl2 solution, Trace element solution, yeast extract, Casitone, sodium acetate, and 0.5 mg resazurin. MediaDive normalizes supported final-medium masses across a 1016 ml final volume after all liquid additions.

The source then stages several anaerobic additions:

- 10 ml Phosphate solution, containing 0.35 g K2HPO4 and 0.23 g KH2PO4 in 10 ml water.
- 35 ml of 8% NaHCO3 solution.
- 20 ml of 50% v/v methanol.
- 10 ml of 1.4% Coenzyme M solution.
- 10 ml Trace vitamins.
- 7.2 ml of 5% Na2S x 9 H2O solution.
- 7.2 ml of 5% L-Cysteine HCl x H2O solution.

The generated record loses those use-sites. It records 35 ml bicarbonate as `NaHCO3: 35 G_PER_L`, 20 ml 50% methanol as `Methanol: 20 G_PER_L`, 10 ml 1.4% Coenzyme M as `Coenzyme M: 10 G_PER_L`, and both 7.2 ml reducing solutions as `7.2 G_PER_L` direct ingredients.

The 1 ml FeCl2 solution, 1 ml Trace element solution, and 10 ml Trace vitamins were also flattened. Their stock components appear as top-level final-medium ingredients at stock `g/L` concentrations.

The gas and vessel instructions are present and source-supported: N2-CO2 80:20 during autoclaving, later H2-CO2 80:20 distribution under butyl stoppers, and 100 kPa H2-CO2 pressurization after inoculation.

## Completeness

The record has no target-organism, strain, literature growth, or variant claims, so there were no growth-evidence assertions to check.

The preparation steps refer generically to anaerobic and filter-sterilized stock additions, but the generated record has no stock/use-site structures for any of those additions.

The `Oxoid` and `BD-BBL` attributes on yeast extract and Casitone are dropped in this MediaDive projection; the duplicate TOGO owner preserves those supplier strings.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Multiple milliliter solution additions were stored as gram-per-litre ingredients. | JCM 1146 uses 35 ml 8% NaHCO3, 20 ml 50% v/v methanol, 10 ml 1.4% Coenzyme M, 7.2 ml 5% Na2S x 9 H2O, and 7.2 ml 5% L-Cysteine HCl x H2O. The YAML records those source volumes as `G_PER_L` concentrations. | `data/normalized_yaml/archaea/methanimicrococcus_medium.yaml` and MediaDive importer liquid-addition handling. |
| Major | FeCl2 solution, Trace element solution, and Trace vitamins were flattened at stock strength. | The source doses these stocks at 1 ml, 1 ml, and 10 ml respectively. The YAML records HCl, FeCl2 x 4 H2O, trace metals, and vitamins as final-medium `ingredients` at each stock's own `g/L` value. | `data/normalized_yaml/archaea/methanimicrococcus_medium.yaml` and MediaDive importer stock handling. |
| Major | The anaerobic stock-addition sequence is no longer representable. | JCM separates additions after cooling from reducing solutions added prior to inoculation. The YAML keeps the prose but does not expose stock objects or use-sites that can be connected to those steps. | `data/normalized_yaml/archaea/methanimicrococcus_medium.yaml`. |
| Major | JCM 1146 is duplicated through MediaDive and TOGO import paths. | This owner and `data/normalized_yaml/archaea/TOGO_M1228_Methanimicrococcus_Medium.yaml` both cite JCM `GRMD=1146` and merge to separate generated files. | Source aliasing for MediaDive J1146 and TOGO M1228, plus a regenerated merge. |
| Minor | Supplier attributes were dropped for complex ingredients. | JCM states `Yeast extract (Oxoid)` and `Casitone (BD-BBL)`; the YAML stores only `Yeast extract` and `Casitone`. | `data/normalized_yaml/archaea/methanimicrococcus_medium.yaml`. |

## Recommended Edits

1. Represent the FeCl2, trace-element, phosphate, bicarbonate, methanol, Coenzyme M, trace-vitamin, sulfide, and cysteine additions as stock use-sites with their milliliter doses and stock strengths.
2. Keep post-cooling additions and pre-inoculation reducing additions as separate procedural groups.
3. Remove stock FeCl2, trace metal, and vitamin components from top-level final-medium `ingredients`.
4. Preserve `Oxoid` and `BD-BBL` as source attributes or notes for yeast extract and Casitone.
5. Add a source alias between MediaDive J1146 and TOGO M1228 so one generated Methanimicrococcus Medium record is emitted for JCM 1146.

## Follow-up Checks

- Re-run schema, strict, reference, and term validation on `data/normalized_yaml/archaea/methanimicrococcus_medium.yaml` and the regenerated merge output.
- Compare regenerated additions against live JCM `GRMD=1146`, checking every 1 ml, 10 ml, 35 ml, 20 ml, and 7.2 ml stock dose.
- Search the regenerated YAML for exact unsupported direct ingredient concentrations `35 G_PER_L`, `20 G_PER_L`, `10 G_PER_L`, and `7.2 G_PER_L`; these values should only appear as source volumes, not final concentrations.
- Search `data/merge_yaml/merged` with ignored files included for exact `GRMD=1146`, `mediadive.medium:J1146`, and `TOGO:M1228` after merge regeneration; the same JCM source should not publish as both a MediaDive and TOGO record.

## Additional Notes

The TOGO M1228 sibling retains several solution boundaries as empty `G_PER_L` stubs but has its own source-unit errors, including `0.5 mg` resazurin represented as `0.5 G_PER_L` and main water plus phosphate-stock water summed to 935.
