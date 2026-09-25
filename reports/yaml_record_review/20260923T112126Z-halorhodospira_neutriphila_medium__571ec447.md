# YAML Record Review: HALORHODOSPIRA NEUTRIPHILA MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: `data/merge_yaml/merged/halorhodospira_neutriphila_medium__571ec447.yaml`
- Started UTC: 2026-09-23T11:20:26Z
- Finished UTC: 2026-09-23T11:21:26Z
- Verdict: needs curation

## Target

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| ID | `CultureMech:003257` |
| Name | `halorhodospira_neutriphila_medium` |
| Original name | `HALORHODOSPIRA NEUTRIPHILA MEDIUM` |
| Category | `bacterial` |
| Physical state | `LIQUID` |
| pH | `7.0` |
| Generated from | `data/normalized_yaml/bacterial/halorhodospira_neutriphila_medium.yaml` |
| Source accession | `mediadive.medium:J908` |
| Source URL | `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=908` |
| Merge fingerprint | `571ec447c99d4b25c729010dc6595a3023c122b3e35e7940de06bd9badd5093b` |

I reviewed the generated merged record, its direct MediaDive/JCM normalized
owner, the live JCM 908 HTML, and the MediaDive `J908` REST payload.

I searched `data/normalized_yaml` and `data/merge_yaml` YAML files with
`rg --no-ignore --hidden` for `mediadive.medium:J908`, `JCM Medium J908`,
`jcm_grmd?GRMD=908`, `GRMD=908`, `HALORHODOSPIRA NEUTRIPHILA MEDIUM`, and
`halorhodospira_neutriphila_medium`. Ignored files were included. The search
found this direct JCM/MediaDive branch, a Togo `M952` sibling from the same
JCM page, and the generated outputs for each branch; only
`halorhodospira_neutriphila_medium.yaml` feeds this reviewed fingerprint.

## Validation

| Check | Result |
|---|---|
| Open schema | Passed: `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/halorhodospira_neutriphila_medium__571ec447.yaml` exited 0 with no diagnostics. |
| Strict schema | Passed: `python scripts/validate_strict.py data/merge_yaml/merged/halorhodospira_neutriphila_medium__571ec447.yaml --out /private/tmp/halorhodospira_neutriphila_medium_571ec447.strict.tsv --workers 1 --quiet` scanned one file and reported `total ERROR rows: 0`. |
| References | Passed with no checked references: `linkml-reference-validator validate data data/merge_yaml/merged/halorhodospira_neutriphila_medium__571ec447.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` reported `Total checks: 0`. |
| Terms | Passed: `linkml-term-validator validate-data data/merge_yaml/merged/halorhodospira_neutriphila_medium__571ec447.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 and reported `Validation passed`. |
| Embedded history | Not checked: `just validate-history` validates standalone records under `history/`, not embedded `MediaRecipe.curation_history` entries. |

The `just` validator entrypoints were not used because this checkout attempts
to resolve a Python 3.13 environment with `llvmlite==0.46.0`; the focused
validators above were run offline with Python 3.11 against the local uv cache.

## Identity and Grounding

The record correctly identifies JCM medium 908,
`HALORHODOSPIRA NEUTRIPHILA MEDIUM`, with pH 7.0 and a liquid final medium.
The six directly weighed main-solution salts from the JCM table are all present
with MediaDive's final-volume-normalized g/L values.

The final ingredient list is not scope-correct. The record contains ingredients
from the SL-12 trace-element stock and seven-vitamins stock as if they were
final-medium ingredients, and it turns several ml stock additions from the JCM
main table into g/L ingredient rows.

## Evidence

JCM 908 lists 1 ml trace element solution SL-12, 20 ml `NaHCO3 (10%, w/v)`,
7.5 ml `Na2S x 9 H2O (10%, w/v)`, 1 ml seven vitamins solution, 4 ml
0.5 M sodium acetate solution, 2 ml 0.5 M sodium succinate solution, and
10 ml 5% yeast extract solution as final-medium additions.

MediaDive preserves SL-12 and seven vitamins as separate nested solutions:
SL-12 contains EDTA, Fe, Co, Mn, Zn, Ni, Mo, B, Cu, and 1 L water, with
stock-scoped pH 6.8 and autoclaving steps; the seven-vitamins solution contains
vitamin B12, p-aminobenzoic acid, biotin, nicotinic acid, calcium pantothenate,
pyridoxine hydrochloride, thiamine hydrochloride dihydrate, and 200 ml water.

The generated record flattens those stock recipes into final-medium
ingredients:

| Source row | Source scope | Generated scope |
|---|---|---|
| SL-12 trace components | 1 ml/L stock addition | Top-level g/L ingredients |
| Seven vitamins components | 1 ml/L stock addition | Top-level g/L ingredients |
| 20 ml `NaHCO3 (10%, w/v)` | post-autoclave stock addition | `NaHCO3`, 20 g/L |
| 7.5 ml `Na2S x 9 H2O (10%, w/v)` | post-autoclave stock addition | `Na2S x 9 H2O`, 7.5 g/L |
| 4 ml 0.5 M sodium acetate | post-autoclave stock addition | `Sodium acetate`, 4 g/L |
| 2 ml 0.5 M sodium succinate | post-autoclave stock addition | `Sodium succinate`, 2 g/L |
| 10 ml 5% yeast extract | post-autoclave stock addition | `Yeast extract`, 10 g/L |

The generated preparation text keeps the JCM paragraph, but it is represented
as a single broad `AUTOCLAVE` action even though the source distinguishes
autoclaving the base under an N2-CO2 atmosphere, separately autoclaving
acetate, succinate, and yeast extract stocks, filter-sterilizing NaHCO3 and
Na2S, and adding all six stocks aseptically and anaerobically after
sterilization.

## Completeness

The record omits water from the main recipe, SL-12, and the seven-vitamins
stock. It also omits explicit solution references for SL-12 and seven vitamins
and structured post-autoclave additions for NaHCO3, Na2S, acetate, succinate,
and yeast extract.

No target organisms, growth evidence, incubation temperature, or light
conditions are present in the JCM or MediaDive source payloads. The
corresponding empty optional fields are not defects.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | The SL-12 trace-element stock and seven-vitamins stock were flattened into top-level ingredients at stock concentration. | JCM lists 1 ml of each stock per liter; MediaDive nests both recipes under separate solution IDs. | `data/normalized_yaml/bacterial/halorhodospira_neutriphila_medium.yaml` or the MediaDive importer |
| Major | Five post-autoclave liquid stock additions were converted to unsupported g/L final ingredients. | JCM specifies ml additions of 10% NaHCO3, 10% Na2S, 0.5 M sodium acetate, 0.5 M sodium succinate, and 5% yeast extract. The generated record uses those volume numbers as g/L masses. | `data/normalized_yaml/bacterial/halorhodospira_neutriphila_medium.yaml` or the MediaDive importer |
| Major | Preparation is collapsed into one main-medium `AUTOCLAVE` step plus two unscoped SL-12 steps. | The source distinguishes pH adjustment with 1 M Na2CO3 or 1 M H2SO4, base autoclaving under an N2-CO2 atmosphere, separate autoclaving of three stocks, filter sterilization of two stocks, anaerobic aseptic additions, and SL-12 stock autoclaving and pH 6.8 adjustment. | `data/normalized_yaml/bacterial/halorhodospira_neutriphila_medium.yaml` or the MediaDive preparation importer |
| Major | Water and solution boundaries are missing. | JCM has 1 L water in the main recipe, and MediaDive has 1 L water in SL-12 plus 200 ml water in seven vitamins. The generated record has no water rows and no stock-solution references. | `data/normalized_yaml/bacterial/halorhodospira_neutriphila_medium.yaml` or the MediaDive importer |
| Minor | `NiCl2 x 6 H2O` is grounded to generic `nickel dichloride`. | The SL-12 stock specifies nickel chloride hexahydrate; the generated row uses `CHEBI:34887` with label `nickel dichloride`. | `data/normalized_yaml/bacterial/halorhodospira_neutriphila_medium.yaml` or the ingredient resolver |

## Recommended Edits

1. In `data/normalized_yaml/bacterial/halorhodospira_neutriphila_medium.yaml`
   or the MediaDive importer, preserve `Trace element solution SL-12` and
   `Seven vitamins solution` as stock solutions and reference each at 1 ml/L.
2. Represent the `NaHCO3`, `Na2S x 9 H2O`, sodium acetate, sodium succinate,
   and yeast extract rows as liquid stock additions with their source volumes
   and stock strengths instead of as g/L final ingredients.
3. Restore distilled water to the main medium and to both expanded stocks.
4. Split the preparation paragraph into scoped steps for pH adjustment, base
   autoclaving under N2-CO2, separate autoclaving of acetate/succinate/yeast
   stocks, filter sterilization of NaHCO3 and Na2S stocks, anaerobic aseptic
   additions, and SL-12 pH/autoclaving.
5. Ground `NiCl2 x 6 H2O` to an exact nickel chloride hexahydrate term if one
   exists in the packaged resolver; otherwise leave it unresolved.
6. Regenerate merged recipes from the corrected normalized owner; do not patch
   `data/merge_yaml/merged/halorhodospira_neutriphila_medium__571ec447.yaml`
   directly.

## Follow-up Checks

1. Run `just validate data/normalized_yaml/bacterial/halorhodospira_neutriphila_medium.yaml`
   after the normalized JCM 908 record or importer is corrected.
2. Run `just validate-terms data/normalized_yaml/bacterial/halorhodospira_neutriphila_medium.yaml`
   to confirm exact stock-ingredient and hydrate grounding.
3. Run `just verify-merges` to prove the generated JCM 908 branch regenerates
   from the corrected normalized owner.
4. Manually compare the regenerated record with JCM 908 and MediaDive `J908`
   to confirm six post-autoclave additions remain distinct from direct
   final-medium salts.

## Additional Notes

The Togo `M952` sibling comes from the same JCM 908 page and should be reviewed
independently. It is not part of this fingerprint.
