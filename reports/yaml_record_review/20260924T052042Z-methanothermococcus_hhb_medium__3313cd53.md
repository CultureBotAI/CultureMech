# YAML Record Review: METHANOTHERMOCOCCUS HHB MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanothermococcus_hhb_medium__3313cd53.yaml
- Started UTC: 2026-09-24T05:19:34Z
- Finished UTC: 2026-09-24T05:20:42Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methanothermococcus_hhb_medium__3313cd53.yaml`, a generated `MediaRecipe` for `CultureMech:002361` with `name: methanothermococcus_hhb_medium`, `original_name: METHANOTHERMOCOCCUS HHB MEDIUM`, and source grounding `mediadive.medium:J1194`.

The merged record was generated from `methanothermococcus_hhb_medium`; the maintained owner is `data/normalized_yaml/archaea/methanothermococcus_hhb_medium.yaml`.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanothermococcus_hhb_medium__3313cd53.yaml` | Passed; exited 0 with no diagnostics. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methanothermococcus_hhb_medium__3313cd53.yaml --out /private/tmp/methanothermococcus_hhb_medium__3313cd53.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methanothermococcus_hhb_medium__3313cd53.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methanothermococcus_hhb_medium__3313cd53.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The record identity is correct: JCM medium 1194 is `METHANOTHERMOCOCCUS HHB MEDIUM`, and MediaDive `J1194` mirrors the JCM formula from `https://www.jcm.riken.jp/cgi-bin/jcm/jcm_grmd?GRMD=1194`.

The final medium structure is not correctly grounded. JCM 1194 uses basal salts in 1 L water, 10 ml Trace vitamins from JCM 197, 10 ml Trace mineral solution from JCM 852, 1 ml Se/W solution from JCM 852, and post-autoclave additions of 12 ml 8% NaHCO3 solution and 10 ml 5% Na2S x 9 H2O solution. The YAML flattens the JCM 197 and 852 stock formulas into final ingredients and turns the post-autoclave solution volumes into dry `G_PER_L` rows.

## Evidence

Supported source claims:

- The base salt ingredient identities and quantities match JCM 1194 after MediaDive normalizes JCM's source amounts over a 1043 ml final volume.
- The source supports the two preparation steps about boiling and cooling under H2/CO2, autoclaving under H2/CO2, adding post-autoclave solutions anaerobically, and pressurizing inoculated bottles to 200 kPa H2/CO2.
- MediaDive solution 5543 resolves as the selenite-tungstate stock that the record references.

Unsupported or over-scoped generated claims:

- Trace vitamins from JCM 197 and Trace mineral solution from JCM 852 are source stock additions, not direct final-medium ingredient rows. The vitamin and trace-metal rows in the YAML are the stock formula concentrations.
- `NaHCO3: 12 G_PER_L` and `Na2S x 9 H2O: 10 G_PER_L` are unsupported. JCM supplies 12 ml of an 8% bicarbonate stock and 10 ml of a 5% sulfide stock per liter after autoclaving.
- `Selenite-tungstate solution: 1 G_PER_L` is unsupported as a mass concentration; JCM supplies 1 ml of that stock.
- The source water rows are absent: 1 L distilled water in the JCM 1194 main recipe and 1 L water rows in the Trace vitamins, Trace mineral solution, and Selenite-tungstate solution stocks.

## Completeness

The schema-optional evidence, discussions, growth, and target organism fields are empty; those empty slots are not defects by themselves.

Consequential gaps:

- JCM 197 and JCM 852 cross-medium stock references are not preserved.
- The Trace vitamins, Trace mineral solution, and Selenite-tungstate solution compositions are not represented as scoped solution records.
- The NaHCO3 and Na2S post-autoclave stocks are not represented as stocks; the filter-sterilization asterisk on 8% NaHCO3 survives only in the generic preparation prose.
- Distilled water is missing from the main recipe and from all three imported stock formulas.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | JCM stock solutions were flattened into top-level final ingredients. | JCM 1194 cites 10 ml Trace vitamins from JCM 197, 10 ml Trace mineral solution from JCM 852, and 1 ml Se/W solution from JCM 852. MediaDive exposes those as solution IDs 3861, 4825, and 5543, but the YAML lifts the vitamins and trace minerals into final `ingredients` and leaves only an empty selenite-tungstate stub. | `data/normalized_yaml/archaea/methanothermococcus_hhb_medium.yaml`; JCM/MediaDive solution import. |
| Major | Post-autoclave stock volumes were converted to false dry concentrations. | JCM lists 12 ml of 8% NaHCO3 solution and 10 ml of 5% Na2S x 9 H2O solution after cooling; the record stores `NaHCO3: 12 G_PER_L` and `Na2S x 9 H2O: 10 G_PER_L`. | `data/normalized_yaml/archaea/methanothermococcus_hhb_medium.yaml`; JCM/MediaDive concentration mapping. |
| Major | Water rows were dropped. | JCM includes 1 L distilled water in medium 1194. MediaDive also exposes 1 L water rows in Trace vitamins, Trace mineral solution, and Selenite-tungstate solution. The record contains none of those solvent rows. | `data/normalized_yaml/archaea/methanothermococcus_hhb_medium.yaml`; JCM/MediaDive importer. |
| Major | JCM 197 and JCM 852 stock provenance was dropped. | The source formula explicitly names the trace vitamin, trace mineral, and Se/W stocks by JCM medium number. The record has raw stock ingredients and a single MediaDive solution link without preserving the JCM 197 or 852 cross references. | `data/normalized_yaml/archaea/methanothermococcus_hhb_medium.yaml`; JCM cross-medium importer. |
| Minor | Post-autoclave sterilization scope is under-specified. | The 8% NaHCO3 stock is the only filter-sterilized post-autoclave addition in JCM 1194. The record only preserves a generic preparation sentence saying that following additions are autoclaved or filter-sterilized, then no longer represents which following row carried the asterisk. | `data/normalized_yaml/archaea/methanothermococcus_hhb_medium.yaml`. |

## Recommended Edits

1. Recurate JCM 1194 so Trace vitamins, Trace mineral solution, and Selenite-tungstate solution remain solution additions with JCM 197 or 852 provenance and MediaDive solution IDs 3861, 4825, and 5543.
2. Represent the 8% NaHCO3 and 5% Na2S x 9 H2O post-autoclave rows as stock-solution volumes, not dry ingredient masses.
3. Restore the JCM 1194 main water row and the stock water rows under their source solutions.
4. Preserve the NaHCO3 filter-sterilization asterisk on the NaHCO3 stock row or as a row-scoped preparation note.
5. Regenerate `data/merge_yaml/merged/methanothermococcus_hhb_medium__3313cd53.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on the regenerated record.
- Diff the regenerated record against JCM 1194 and MediaDive J1194 and confirm that no row from JCM 197, JCM 852, or MediaDive solution 5543 was promoted to a final ingredient.
- Manually confirm that all source milliliter rows remain volume rows after regeneration.

## Additional Notes

- Empty optional evidence and discussion fields were not treated as defects.
- The exact owner search used `rg --no-ignore --hidden`, so ignored files were included when resolving `CultureMech:002361`, `J1194`, and `methanothermococcus_hhb_medium`.
