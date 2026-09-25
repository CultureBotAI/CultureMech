# YAML Record Review: METHANOTROPH 1A MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanotroph_1a_medium__3b0a4884.yaml
- Started UTC: 2026-09-24T05:28:23Z
- Finished UTC: 2026-09-24T05:29:44Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methanotroph_1a_medium__3b0a4884.yaml`, a generated `MediaRecipe` for `CultureMech:003165` with `name: methanotroph_1a_medium`, `original_name: METHANOTROPH 1A MEDIUM`, pH 6.5, and source grounding `mediadive.medium:J820`.

The record was merged from one normalized input:

- `data/normalized_yaml/bacterial/methanotroph_1a_medium.yaml`

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanotroph_1a_medium__3b0a4884.yaml` | Passed; exited 0. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methanotroph_1a_medium__3b0a4884.yaml --out /private/tmp/methanotroph_1a_medium__3b0a4884.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methanotroph_1a_medium__3b0a4884.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methanotroph_1a_medium__3b0a4884.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The base medium identity is correct. JCM 820 and MediaDive J820 both describe `METHANOTROPH 1A MEDIUM`, a defined liquid medium at pH 6.5 with methane added to the gas phase after autoclaving.

The stock identity is wrong. The JCM/MediaDive J820 stock is `Trace mineral solution`, MediaDive solution 4776, with six salts plus distilled water. The generated record points the 1 ml stock addition at `mediadive.solution:6140`, a different `Trace metal solution` with different H3BO3, MnCl2 x 4 H2O, ZnSO4 x 7 H2O, Na2MoO4 x 2 H2O, CuSO4 x 5 H2O, and Co(NO3)2 x 6 H2O contents.

## Evidence

Supported source claims:

- JCM 820 and MediaDive J820 support the record's JCM identity, pH 6.5, direct NaNO3, MgSO4 x 7 H2O, Na2HPO4 x 12 H2O, KH2PO4, CaCl2 x 2 H2O, FeSO4 x 7 H2O, and 1 ml Trace mineral solution rows.
- JCM 820 and MediaDive J820 support the preparation steps for pH adjustment, dispensing into vessels with more than 80% gas phase, autoclaving under butyl rubber stoppers, and adding filter-sterilized methane after cooling to about 20% v/v in the gas phase.
- MediaDive solution 4776 supports the stock composition with ZnSO4 x 7 H2O, CuSO4 x 5 H2O, MnSO4 x n H2O, Na2MoO4 x 2 H2O, H3BO3, CoCl2 x 6 H2O, and 1000 ml distilled water.

Unsupported or over-scoped generated claims:

- ZnSO4 x 7 H2O through CoCl2 x 6 H2O are constituents of Trace mineral solution 4776, not final top-level ingredients of JCM 820.
- The `solutions` row points at `mediadive.solution:6140`; that stock is not the Trace mineral solution used by MediaDive J820.
- The generated stock concentration `1 G_PER_L` is not source-equivalent to a 1 ml Trace mineral solution addition.

## Completeness

The schema-optional evidence, discussions, growth, target organism, and recipe variant arrays are empty; empty optional slots were not treated as defects.

Consequential gaps:

- Trace mineral solution is present only as an empty, mislinked `solutions` row.
- The 1000 ml main-medium water row and the 1000 ml stock water row are absent.
- The generated record has no place to show that the trace-salt concentrations are stock concentrations.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Trace mineral solution 4776 was flattened into final-medium ingredients. | MediaDive J820 adds 1 ml of solution 4776 to the main medium. The YAML stores all six non-water stock constituents as top-level ingredients. | `data/normalized_yaml/bacterial/methanotroph_1a_medium.yaml`; MediaDive importer and solution migration. |
| Major | The stock reference points at the wrong MediaDive solution. | MediaDive J820 references solution 4776, while the YAML points to `mediadive.solution:6140`, whose formula differs from solution 4776. | `data/normalized_yaml/bacterial/methanotroph_1a_medium.yaml`; solution cross-reference enrichment. |
| Major | Source water rows were dropped. | JCM 820 and MediaDive J820 list 1 L water in the main solution, and MediaDive solution 4776 has 1000 ml water. The YAML has no Distilled water row. | `data/normalized_yaml/bacterial/methanotroph_1a_medium.yaml`; MediaDive importer. |
| Major | The stock-addition unit is wrong. | The source calls for 1 ml Trace mineral solution, but the YAML stores the empty stock row as `1 G_PER_L`. | `data/normalized_yaml/bacterial/methanotroph_1a_medium.yaml`; solution migration. |

## Recommended Edits

1. Preserve Trace mineral solution 4776 as a scoped 1 ml addition with its six salt constituents and 1000 ml water row.
2. Remove the erroneous `mediadive.solution:6140` link from this JCM 820 record.
3. Restore the main-medium 1000 ml distilled-water row.
4. Keep Trace mineral solution concentrations scoped to the stock rather than emitting them as final top-level ingredients.
5. Regenerate `data/merge_yaml/merged/methanotroph_1a_medium__3b0a4884.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on the regenerated record.
- Diff the regenerated record against JCM 820 and MediaDive J820 and verify that Trace mineral solution 4776, not solution 6140, owns the trace-salt composition.
- Verify that no Trace mineral solution salt appears as a top-level final ingredient unless it is explicitly nested under the 1 ml stock addition.
- Search ignored and generated files for the exact `mediadive.solution:6140` link in `methanotroph_1a_medium` and confirm it is gone or only retained in archived reports.

## Additional Notes

- Empty optional evidence and discussion fields were not treated as defects.
- Exact owner searches used `rg --no-ignore --hidden`, so ignored files were included when resolving `CultureMech:003165`, `data/normalized_yaml/bacterial/methanotroph_1a_medium.yaml`, and `data/normalized_yaml/bacterial/mediadive_6140_Trace_metal_solution.yaml`.
