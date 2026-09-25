# YAML Record Review: METHANOTHERMUS MEDIUM

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/methanothermus_medium__41bda6a4.yaml
- Started UTC: 2026-09-24T05:22:53Z
- Finished UTC: 2026-09-24T05:24:01Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/methanothermus_medium__41bda6a4.yaml`, a generated `MediaRecipe` for `CultureMech:001302` with `name: methanothermus_medium`, `original_name: METHANOTHERMUS MEDIUM`, and source grounding `mediadive.medium:203`.

The record was merged from three normalized duplicate inputs:

- `data/normalized_yaml/archaea/methanothermus_medium.yaml`
- `data/normalized_yaml/bacterial/medium_203_modified_for_dsm_3537.yaml`
- `data/normalized_yaml/bacterial/medium_203_modified_for_dsm_3538.yaml`

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/methanothermus_medium__41bda6a4.yaml` | Passed; exited 0 with no diagnostics. |
| `python scripts/validate_strict.py data/merge_yaml/merged/methanothermus_medium__41bda6a4.yaml --out /private/tmp/methanothermus_medium__41bda6a4.strict.tsv --workers 1 --quiet` | Passed; scanned 1 file and reported 0 error rows. |
| `linkml-reference-validator validate data data/merge_yaml/merged/methanothermus_medium__41bda6a4.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` | Passed; the reference validator performed 0 checks for this file. |
| `linkml-term-validator validate-data data/merge_yaml/merged/methanothermus_medium__41bda6a4.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` | Passed after the known `eutils` `pkg_resources` deprecation warning. |
| Embedded curation history | Not checked: the documented history validator is a standalone `history/` validator, not a focused check for `MediaRecipe.curation_history` entries embedded in merged YAML. |

## Identity and Grounding

The base DSMZ identity is correct: DSMZ/MediaDive medium 203 is `METHANOTHERMUS MEDIUM`, complex, pH 6.5, and the two KOMODO `203_3537`/`203_3538` inputs were imported as source duplicates of DSMZ 203.

The ingredient graph is not correct. DSMZ 203 is a stock-based recipe made from Mineral solution 1, Mineral solution 2, Modified Wolin's mineral solution, and Wolin's vitamin solution, but the record flattens all four stock recipes into final top-level ingredient rows.

## Evidence

Supported source claims:

- DSMZ 203 supports the record's identity, pH 6.5, direct sodium sulfate, sodium carbonate, yeast extract, Trypticase peptone, sulfide, and cysteine rows, and the two main preparation paragraphs.
- The merged KOMODO aliases are source duplicates of DSMZ medium 203 with the same ingredient signature.
- The Modified Wolin and Wolin vitamin preparation text comes from source stock recipes under DSMZ 203.

Unsupported or over-scoped generated claims:

- K2HPO4, KH2PO4, (NH4)2SO4, NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O are stock constituents of Mineral solution 1 or 2, not final top-level ingredients at stock concentration.
- Nitrilotriacetic acid through Na2WO4 x 2 H2O are Modified Wolin stock constituents; the medium uses 10 ml of that stock.
- Biotin through lipoic acid are Wolin 10x vitamin stock constituents; the medium uses 1 ml of that stock.
- NiCl2 x 6 H2O and FeSO4 x 7 H2O have been summed across direct main-medium 0.1% stock additions and the Modified Wolin stock. NaCl, MgSO4 x 7 H2O, and CaCl2 x 2 H2O were similarly merged across Mineral solution 2 and Modified Wolin.

## Completeness

The schema-optional evidence, discussions, growth, target organism, and solution arrays are empty; evidence, discussion, and growth omissions are not defects by themselves.

Consequential gaps:

- No solution entries remain for Mineral solution 1, Mineral solution 2, Modified Wolin's mineral solution, or Wolin's vitamin solution.
- The main 920 ml water row and all stock water rows are absent.
- The Modified Wolin preparation step is appended at the final-medium level rather than scoped to Modified Wolin.
- The two KOMODO alias inputs point their `parent_media.path` at `data/normalized_yaml/bacterial/methanothermus_medium.yaml`; `find data/normalized_yaml` found the two bacterial aliases and `data/normalized_yaml/archaea/methanothermus_medium.yaml`, but found no bacterial `methanothermus_medium.yaml` file.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| Major | Four DSMZ stock recipes were flattened into top-level ingredients. | DSMZ 203 and MediaDive 203 use Mineral solution 1, Mineral solution 2, Modified Wolin's mineral solution, and Wolin's vitamin solution as stock additions. The generated YAML has no `solutions` entries and stores all stock children as final ingredients. | All three normalized duplicate inputs; DSMZ/MediaDive importer and KOMODO DSMZ enrichment. |
| Major | Duplicate cleanup merged ingredients across stock scopes. | NiCl2, FeSO4, NaCl, MgSO4, and CaCl2 notes show summed values from direct main rows, Mineral solution 2, and Modified Wolin. Those are distinct recipe scopes. | All three normalized duplicate inputs; duplicate cleanup. |
| Major | Source water rows were dropped. | DSMZ 203 lists 920 ml main water and 1 L water in Mineral solution 1, Mineral solution 2, Modified Wolin, and Wolin vitamin stocks. The YAML carries none of those rows. | All three normalized duplicate inputs; DSMZ/MediaDive importer. |
| Minor | Modified Wolin preparation lost its solution scope. | MediaDive nests the nitrilotriacetic-acid pH instructions under `Modified Wolin's mineral solution`; the YAML appends them after the final medium H2/CO2 pressurization step. | All three normalized duplicate inputs; preparation importer. |
| Minor | KOMODO duplicate parent paths are stale. | Both bacterial KOMODO aliases point to `data/normalized_yaml/bacterial/methanothermus_medium.yaml`, while the actual parent is `data/normalized_yaml/archaea/methanothermus_medium.yaml`. | `data/normalized_yaml/bacterial/medium_203_modified_for_dsm_3537.yaml` and `data/normalized_yaml/bacterial/medium_203_modified_for_dsm_3538.yaml`; duplicate relationship generation. |

## Recommended Edits

1. Preserve Mineral solution 1, Mineral solution 2, Modified Wolin's mineral solution, and Wolin's vitamin solution as scoped stock additions with their MediaDive solution IDs.
2. Keep repeated chemical names separate when they belong to different stock scopes.
3. Restore the main and stock water rows.
4. Scope the Modified Wolin pH 6.5 and pH 7.0 preparation text to that stock.
5. Regenerate the KOMODO source-duplicate relationship paths so they point to `data/normalized_yaml/archaea/methanothermus_medium.yaml`.
6. Regenerate `data/merge_yaml/merged/methanothermus_medium__41bda6a4.yaml`.

## Follow-up Checks

- Run focused schema, strict, reference, and term validation on the regenerated record.
- Diff the regenerated record against DSMZ 203 and MediaDive 203 and verify that no Modified Wolin, Mineral solution 1/2, or Wolin vitamin constituent appears as a top-level final ingredient.
- Search ignored and generated files for the stale `data/normalized_yaml/bacterial/methanothermus_medium.yaml` string and confirm it is gone or only present in an archived report.

## Additional Notes

- Empty optional evidence and discussion fields were not treated as defects.
- Exact owner searches used `rg --no-ignore --hidden`, and the stale-path check used `find`, so ignored files were included when resolving `CultureMech:001302`, `CultureMech:004299`, `CultureMech:004300`, and the three normalized owner files.
