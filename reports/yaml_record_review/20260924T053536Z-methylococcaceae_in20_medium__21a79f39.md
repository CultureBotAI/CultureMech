# YAML Record Review: METHYLOCOCCACEAE IN20 MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methylococcaceae_in20_medium__21a79f39.yaml
- Started UTC: 2026-09-24T05:34:34Z
- Finished UTC: 2026-09-24T05:35:36Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methylococcaceae_in20_medium__21a79f39.yaml`, a generated `MediaRecipe` for `CultureMech:002417` with `name: methylococcaceae_in20_medium`, `original_name: METHYLOCOCCACEAE IN20 MEDIUM`, pH 6.5, and source grounding `mediadive.medium:J1250`.

The record was merged from one normalized input:

- `data/normalized_yaml/bacterial/methylococcaceae_in20_medium.yaml`

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methylococcaceae_in20_medium__21a79f39.yaml` | Passed; exited 0 with no diagnostics. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methylococcaceae_in20_medium__21a79f39.yaml --out /private/tmp/methylococcaceae_in20_medium__21a79f39.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methylococcaceae_in20_medium__21a79f39.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methylococcaceae_in20_medium__21a79f39.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The MediaDive identity is correct: MediaDive J1250 is `METHYLOCOCCACEAE IN20 MEDIUM`, a defined liquid JCM medium with pH 6.5. The original JCM URL currently returns `Nothing found`, so the inspected source was MediaDive's preserved J1250 payload.

The ingredient graph is not correct. MediaDive J1250 has a 1006 ml final main solution that uses 3.3 ml Trace mineral solution, 0.1 ml of a 1 mM CuSO4 solution, 1 ml Trace vitamins, and 1.25 ml of 8% NaHCO3 as later filter-sterilized additions. The generated record has no `solutions` entries and stores Trace mineral solution and Trace vitamins constituents as final top-level ingredients.

## Evidence

Supported source claims:

- MediaDive J1250 supports the direct main-medium rows from NaCl through Fe2(SO4)3 x n H2O.
- MediaDive J1250 supports 3.3 ml Trace mineral solution 5387, 0.1 ml 1 mM CuSO4 x 5 H2O, 1 ml Trace vitamins 3861, and 1.25 ml 8% NaHCO3 as filter-sterilized additions after the main mix is autoclaved.
- MediaDive J1250 supports methane at 30% by volume in the gas phase and a final pH check at 6.4-6.8.

Unsupported or over-scoped generated claims:

- Nitrilotriacetic acid through Na2SeO3 are Trace mineral solution 5387 constituents, not final top-level ingredients.
- Biotin through lipoic acid are Trace vitamins 3861 constituents, not final top-level ingredients.
- The final-medium CuSO4 x 5 H2O row is a 0.1 ml addition of a 1 mM solution, not 0.1 G_PER_L.
- The final-medium NaHCO3 row is a 1.25 ml addition of an 8% solution, not 1.25 G_PER_L.
- The Trace mineral solution pH 6.5 to pH 7.0 instruction is stock-scoped, not a final-medium instruction.

## Completeness

The schema-optional evidence, discussions, growth, target organism, and solution arrays are empty; empty optional slots were not treated as defects.

Consequential gaps:

- Trace mineral solution 5387 and Trace vitamins 3861 are absent as scoped stocks.
- The main 1000 ml water row and the two 1000 ml stock water rows are absent.
- The post-autoclave, filter-sterilized stock addition set is preserved only in prose.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Trace mineral solution and Trace vitamins were flattened into final-medium ingredients. | MediaDive J1250 adds 3.3 ml Trace mineral solution and 1 ml Trace vitamins. The YAML has no stock entries and emits their contents as top-level ingredients. | `data/normalized_yaml/bacterial/methylococcaceae_in20_medium.yaml`; MediaDive importer. |
| Major | Final stock-addition volumes were turned into dry concentrations. | MediaDive J1250 adds 0.1 ml 1 mM CuSO4 x 5 H2O and 1.25 ml 8% NaHCO3. The YAML stores those additions as 0.1 and 1.25 G_PER_L. | `data/normalized_yaml/bacterial/methylococcaceae_in20_medium.yaml`; MediaDive importer. |
| Major | Source water rows were dropped. | MediaDive J1250 lists 1000 ml water in the main solution, Trace mineral solution, and Trace vitamins. The YAML has no Distilled water row. | `data/normalized_yaml/bacterial/methylococcaceae_in20_medium.yaml`; MediaDive importer. |
| Minor | Trace mineral solution preparation lost its stock scope. | The NTA dissolution and pH 6.5 to pH 7.0 instructions belong to Trace mineral solution 5387. The YAML stores that text as final-medium step 3. | `data/normalized_yaml/bacterial/methylococcaceae_in20_medium.yaml`; MediaDive importer. |

## Recommended Edits

1. Preserve Trace mineral solution 5387 and Trace vitamins 3861 as scoped stock additions.
2. Represent 0.1 ml 1 mM CuSO4 and 1.25 ml 8% NaHCO3 as volumetric final additions rather than dry concentrations.
3. Restore the main and stock water rows.
4. Scope the NTA/pH instructions to Trace mineral solution.
5. Regenerate `data/merge_yaml/merged/methylococcaceae_in20_medium__21a79f39.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on the regenerated record.
- Diff the regenerated record against MediaDive J1250 and verify that Trace mineral and Trace vitamins child rows do not appear as final top-level ingredients.
- Verify that the post-autoclave filter-sterile additions remain 3.3 ml Trace mineral solution, 0.1 ml 1 mM CuSO4, 1 ml Trace vitamins, and 1.25 ml 8% NaHCO3.
- Re-check the JCM 1250 URL and, if it still returns no formula, keep MediaDive J1250 as the inspected source of truth for this record.

## Additional Notes

- Empty optional evidence and discussion fields were not treated as defects.
- Exact owner searches used `rg --no-ignore --hidden`, so ignored files were included when resolving `CultureMech:002417` and `data/normalized_yaml/bacterial/methylococcaceae_in20_medium.yaml`.
