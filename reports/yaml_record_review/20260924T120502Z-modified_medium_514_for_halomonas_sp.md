# YAML Record Review: MODIFIED MEDIUM 514 FOR HALOMONAS SP.

- Repository: CultureBotAI/CultureMech
- Record: data/merge_yaml/merged/modified_medium_514_for_halomonas_sp.yaml
- Started UTC: 2026-09-24T12:05:02Z
- Finished UTC: 2026-09-24T12:05:02Z
- Verdict: needs curation

## Target

Reviewed `data/merge_yaml/merged/modified_medium_514_for_halomonas_sp.yaml`.

| Field | Value |
|---|---|
| Class | `MediaRecipe` |
| CultureMech ID | `CultureMech:000982` |
| Name | `modified_medium_514_for_halomonas_sp` |
| Source identity | `mediadive.medium:1510` |
| Category | `bacterial` |
| Maintained owner | `data/normalized_yaml/bacterial/modified_medium_514_for_halomonas_sp.yaml` |
| Generated artifact | yes; generated under `data/merge_yaml/merged/` from one MediaDive-normalized source |

## Validation

| Check | Result |
|---|---|
| Open LinkML schema validation | Passed; `linkml-validate -s src/culturemech/schema/culturemech.yaml --target-class MediaRecipe data/merge_yaml/merged/modified_medium_514_for_halomonas_sp.yaml` reported `No issues found`. |
| Strict CultureMech validation | Passed; `scripts/validate_strict.py data/merge_yaml/merged/modified_medium_514_for_halomonas_sp.yaml --out /private/tmp/modified_medium_514_for_halomonas_sp.strict.tsv --workers 1 --quiet` reported 0 errors and wrote only the TSV header line. |
| Reference validation | Passed; `linkml-reference-validator validate data data/merge_yaml/merged/modified_medium_514_for_halomonas_sp.yaml --schema src/culturemech/schema/culturemech.yaml --target-class MediaRecipe` checked one file, ran 0 reference checks, and reported no errors. |
| Term validation | Passed; `linkml-term-validator validate-data data/merge_yaml/merged/modified_medium_514_for_halomonas_sp.yaml -s src/culturemech/schema/culturemech.yaml -t MediaRecipe --labels -c conf/oak_config.yaml` exited 0 after a harmless `pkg_resources` deprecation warning. |
| Embedded history validation | Not checked: the available `just validate-history` target validates standalone files under `history/`, not embedded `MediaRecipe.curation_history` entries in merged YAML. |

## Identity and Grounding

The record denotes MediaDive's DSMZ 1510 copy of "MODIFIED MEDIUM 514 FOR HALOMONAS SP." The identity, title, pH 7.5, solid agar state, and five non-water ingredients all agree with the inspected DSMZ PDF and MediaDive REST payload.

An exact gitignore-independent search under `data/normalized_yaml/` found no second maintained YAML source with the exact normalized name `modified_medium_514_for_halomonas_sp`.

## Evidence

The DSMZ Medium 1510 PDF lists Difco Marine Broth 2216 at 37.4 g, pancreatic digest of casein at 1.0 g, soya peptone at 1.0 g, malt extract at 1.0 g, Agar at 20.0 g, and Distilled water at 1000.0 ml, followed by an instruction to adjust pH to 7.5.

MediaDive medium 1510 exposes the same formula as `Main sol. 1510` with g/L values for the four nutrients and agar, plus a 1000 ml Distilled water row and the pH 7.5 adjustment step. The generated YAML contains the five non-water ingredients and the pH step, but it drops the 1000 ml water row.

## Completeness

The generated record is incomplete only because it omits the explicit 1000 ml distilled-water row.

The inspected DSMZ and MediaDive payloads did not expose organism-specific growth rows, and the record makes no target-organism claims.

## Findings

| Severity | Finding | Evidence | Maintained owner |
|---|---|---|---|
| major | The generated record omits the source distilled-water row. | DSMZ Medium 1510 and MediaDive 1510 list Distilled water at 1000 ml; `data/merge_yaml/merged/modified_medium_514_for_halomonas_sp.yaml` has no water ingredient. | Add or preserve Distilled water in `data/normalized_yaml/bacterial/modified_medium_514_for_halomonas_sp.yaml`, then regenerate. |

## Recommended Edits

1. Add a 1000 ml/L distilled-water row to the maintained DSMZ 1510 source.
2. Regenerate the merged artifact and confirm the water row survives the merge.

## Follow-up Checks

- Rerun focused LinkML, strict, reference, and term validation on the regenerated DSMZ 1510 YAML.
- Re-open the DSMZ Medium 1510 PDF and confirm all six recipe rows, including Distilled water, are present in the generated record.

## Additional Notes

- `just` validators were not used because project dependency resolution attempts to build `llvmlite==0.46.0` under Python 3.13; the focused validators were run with `/usr/local/bin/python3.11` and the offline review cache instead.
