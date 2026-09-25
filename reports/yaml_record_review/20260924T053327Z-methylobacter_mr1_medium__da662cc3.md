# YAML Record Review: METHYLOBACTER MR1 MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methylobacter_mr1_medium__da662cc3.yaml
- Started UTC: 2026-09-24T05:32:01Z
- Finished UTC: 2026-09-24T05:33:27Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methylobacter_mr1_medium__da662cc3.yaml`, a generated `MediaRecipe` for `CultureMech:003275` with `name: methylobacter_mr1_medium`, `original_name: METHYLOBACTER MR1 MEDIUM`, pH 6.5, and source grounding `mediadive.medium:J928`.

The record was merged from one normalized input:

- `data/normalized_yaml/bacterial/methylobacter_mr1_medium.yaml`

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methylobacter_mr1_medium__da662cc3.yaml` | Passed; exited 0 with no diagnostics. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methylobacter_mr1_medium__da662cc3.yaml --out /private/tmp/methylobacter_mr1_medium__da662cc3.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methylobacter_mr1_medium__da662cc3.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methylobacter_mr1_medium__da662cc3.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The MediaDive identity is correct: MediaDive J928 is `METHYLOBACTER MR1 MEDIUM`, a defined liquid JCM medium with pH 6.5. The original JCM URL currently returns `Nothing found`, so the reviewed formulation was checked against MediaDive's preserved J928 payload.

The recipe structure is not correct. MediaDive J928 has a final medium that uses 3 ml Trace mineral solution, 0.1 ml of a 1 mM CuSO4 solution, 1 ml Trace vitamins, and 1.25 ml of 8% NaHCO3 after autoclaving. Trace mineral solution and Trace vitamins are their own stocks, but the YAML flattens both stock recipes, converts the volumetric CuSO4 and NaHCO3 additions into G_PER_L rows, and drops all stock-addition context.

## Evidence

Supported source claims:

- MediaDive J928 supports the record's identity, pH 6.5, and direct main-solution salt rows from NaCl through the direct FeSO4 x 7 H2O 0.02 g addition.
- MediaDive J928 supports the final preparation step to adjust the main components to pH 6.6-6.8 before autoclaving, filter-sterilize later additions, purge with N2, add O2 at 1.5% of the gas phase, and overpressure with methane at 50% of the gas phase.
- MediaDive J928 supports Trace mineral solution 4939 and Trace vitamins 3861 as nested stocks.

Unsupported or over-scoped generated claims:

- Nitrilotriacetic acid through Na2SeO3 x 5 H2O are Trace mineral solution 4939 constituents, not final top-level ingredients.
- Biotin through lipoic acid are Trace vitamins 3861 constituents, not final top-level ingredients.
- The generated FeSO4 x 7 H2O concentration sums the direct main-medium row with the Trace mineral solution row.
- The final-medium CuSO4 x 5 H2O row is a 0.1 ml addition of a 1 mM solution, not 0.1 G_PER_L.
- The final-medium NaHCO3 row is a 1.25 ml addition of an 8% solution, not 1.25 G_PER_L.

## Completeness

The schema-optional evidence, discussions, growth, target organism, and solution arrays are empty; empty optional slots were not treated as defects.

Consequential gaps:

- The 3 ml Trace mineral solution and 1 ml Trace vitamins stock additions are absent as scoped `solutions`.
- The main 1000 ml water row, the Trace mineral 1000 ml water row, and the Trace vitamins 1000 ml water row are absent.
- Trace mineral solution preparation is present only as a final-medium pH-adjustment step instead of being scoped to the stock.
- The original JCM URL in `notes` no longer resolves to formula text.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Trace mineral solution and Trace vitamins were flattened into final-medium ingredients. | MediaDive J928 adds 3 ml Trace mineral solution 4939 and 1 ml Trace vitamins 3861. The YAML has no `solutions` rows and promotes all stock children to final ingredients. | `data/normalized_yaml/bacterial/methylobacter_mr1_medium.yaml`; MediaDive importer. |
| Major | Final stock-addition volumes were turned into dry concentrations. | MediaDive J928 uses 0.1 ml of 1 mM CuSO4 and 1.25 ml of 8% NaHCO3. The YAML emits 0.1 G_PER_L CuSO4 x 5 H2O and 1.25 G_PER_L NaHCO3. | `data/normalized_yaml/bacterial/methylobacter_mr1_medium.yaml`; MediaDive importer. |
| Major | Duplicate cleanup merged FeSO4 across final-medium and stock scopes. | The source has 0.02 g FeSO4 x 7 H2O in the main solution and 0.1 g/L in Trace mineral solution; the YAML stores a single 0.11990050000000001 G_PER_L row. | `data/normalized_yaml/bacterial/methylobacter_mr1_medium.yaml`; duplicate cleanup. |
| Major | Source water rows were dropped. | MediaDive J928 lists 1000 ml water in the main solution, Trace mineral solution, and Trace vitamins. The YAML has no Distilled water row. | `data/normalized_yaml/bacterial/methylobacter_mr1_medium.yaml`; MediaDive importer. |
| Minor | Trace mineral preparation lost its stock scope. | MediaDive attaches the NTA dissolution and pH 6.5 to pH 7.0 instructions to Trace mineral solution 4939. The YAML emits that text as final-medium step 3. | `data/normalized_yaml/bacterial/methylobacter_mr1_medium.yaml`; MediaDive importer. |

## Recommended Edits

1. Preserve Trace mineral solution 4939 and Trace vitamins 3861 as scoped stock additions.
2. Keep 0.1 ml 1 mM CuSO4 and 1.25 ml 8% NaHCO3 as final volumetric additions or convert them with explicit stock arithmetic.
3. Keep direct FeSO4 separate from the Trace mineral FeSO4 row.
4. Restore main and stock water rows.
5. Scope the NTA/pH instructions to Trace mineral solution.
6. Regenerate `data/merge_yaml/merged/methylobacter_mr1_medium__da662cc3.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on the regenerated record.
- Diff the regenerated record against MediaDive J928 and verify that Trace mineral and Trace vitamins child rows do not appear as final top-level ingredients.
- Verify that CuSO4 and NaHCO3 retain their 0.1 ml and 1.25 ml stock-addition semantics.
- Re-check the JCM 928 URL and, if it still returns no formula, keep MediaDive J928 as the inspected source of truth for this record.

## Additional Notes

- Empty optional evidence and discussion fields were not treated as defects.
- Exact owner searches used `rg --no-ignore --hidden`, so ignored files were included when resolving `CultureMech:003275` and `data/normalized_yaml/bacterial/methylobacter_mr1_medium.yaml`.
